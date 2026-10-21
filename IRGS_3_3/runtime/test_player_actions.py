"""Bounded equipment action qualification; no historical stock/authority claim."""
import copy
import json
import unittest

from campaign_library import initial_campaign
from core_world import CoreWorld
from irgs_reference import InvalidEvent
from player_actions import (OPERATION, PlayerActionUnavailable, equipment_options,
                            execute_equipment_action)
from r9_runtime import conflicts, frontier, grant, observe


def apply(world, event_id, op, **params):
    world.apply(event_id, world.s['clock'] + 1, op, campaign_id=world.s['campaign_id'],
                source_ref='explicit-synthetic-equipment-fixture', **params)


def fixture(quantity=4, persons=None):
    world = initial_campaign('military', 'equipment-action-fixture')
    for actor in ('commander', 'worker', 'other'):
        apply(world, 'actor:' + actor, 'register_actor', actor_id=actor,
              name='Received identity ' + actor, species='human',
              player_controlled=actor == 'commander', instruction_ref='explicit fixture player selection')
    apply(world, 'stock', 'establish_stock', location='depot', material='kit', quantity=quantity,
          inventory_evidence_ref='explicit synthetic count')
    grant(world, 'issue-authority', 'commander', ['military_issue_equipment'], world.s['clock'],
          'explicit synthetic current issue authority')
    add_order(world, 'order-1', persons=persons)
    return world


def add_order(world, order_id, persons=None):
    apply(world, 'receive:' + order_id, 'receive_order', order_id=order_id, recipient='commander',
          authority_ref='issue-authority', content='Issue one kit to the named recipients.',
          directives={'operation': 'issue_equipment', 'deadline': 100,
                      'persons': ['worker'] if persons is None else persons,
                      'material': 'kit', 'from': 'depot', 'quantity_each': 1})


def event(world, event_id='execute', order_id='order-1'):
    return {'id': event_id, 'at': world.s['clock'] + 1, 'op': OPERATION,
            'params': {'campaign_id': world.s['campaign_id'],
                       'source_ref': 'explicit selected action', 'instruction_ref': 'explicit selected action',
                       'actor': 'commander', 'action': {'kind': 'issue_equipment', 'order_id': order_id}}}


def execute(world, event_id='execute', actor='commander', order_id='order-1'):
    return execute_equipment_action(world, event_id, actor,
                                    {'kind': 'issue_equipment', 'order_id': order_id},
                                    'explicit selected action')


class PlayerEquipmentActionTests(unittest.TestCase):
    def assert_rejected(self, world, **kwargs):
        before = world.save()
        with self.assertRaises(PlayerActionUnavailable) as error:
            execute(world, **kwargs)
        self.assertEqual(world.save(), before)
        self.assertEqual(error.exception.dependencies['status'], 'rejected_no_effects')
        self.assertFalse(error.exception.dependencies['successful_certificate'])
        self.assertEqual(error.exception.dependencies['writes'], [])
        return error.exception

    def test_success_is_one_committed_conserved_effect_without_elapsed_time(self):
        world = fixture(quantity=10)
        calendar = copy.deepcopy(world.s['campaign_time'])
        result = execute(world)
        self.assertEqual(result['status'], 'completed_successfully')
        self.assertEqual(world.s['stocks'], {'depot': {'kit': 9}, 'worker': {'kit': 1}})
        self.assertEqual(world.s['opening_stock'], {'kit': 10})
        self.assertTrue(world.s['orders']['order-1']['executed'])
        self.assertEqual(world.s['campaign_time'], calendar)
        self.assertEqual(result['receipt']['event_id'], 'execute')
        self.assertEqual(result['outcome']['transfers'], [
            {'from': 'depot', 'to': 'worker', 'material': 'kit', 'quantity': 1}])
        self.assertNotIn('remaining_stock', result['outcome'])
        self.assertEqual(world.s['journal'][-1]['op'], OPERATION)

    def test_success_certificate_contains_actual_authorization_and_stock_reads(self):
        result = execute(fixture())
        reads = result['dependencies']['reads']
        for path in [('r9', 'mandates', 'issue-authority', 'active'),
                     ('r9', 'mandates', 'issue-authority', 'actor'),
                     ('r9', 'mandates', 'issue-authority', 'operations'),
                     ('orders', 'order-1', 'authority_ref'),
                     ('orders', 'order-1', 'directives', 'deadline'),
                     ('stocks', 'depot', 'kit'), ('player_actor_ids',)]:
            self.assertIn(path, reads)
        self.assertTrue(any(path[0] == 'entity_registry' for path in reads))
        self.assertIn(('stocks', 'depot', 'kit'), result['dependencies']['writes'])

    def test_native_core_replay_keeps_frozen_event_without_repeating_effects(self):
        world = fixture()
        execute(world)
        accepted = copy.deepcopy(world.s['journal'][-1])
        world = CoreWorld.load(world.save())
        before = world.save()
        self.assertFalse(world.apply(accepted['id'], accepted['at'], accepted['op'], **accepted['params']))
        self.assertEqual(world.save(), before)
        with self.assertRaises(InvalidEvent):
            execute(world)
        self.assertEqual(world.save(), before)

    def test_caller_cannot_change_quantities_or_recipients(self):
        world = fixture()
        before = world.save()
        for action in ({'kind': 'issue_equipment', 'order_id': 'order-1', 'quantity_each': 20},
                       {'kind': 'issue_equipment', 'order_id': 'order-1', 'persons': ['commander']},
                       {'kind': 'transfer_stock', 'order_id': 'order-1'}):
            with self.subTest(action=action), self.assertRaises(InvalidEvent):
                execute_equipment_action(world, 'execute', 'commander', action, 'instruction')
        self.assertEqual(world.save(), before)

    def test_noncontrolled_actor_cannot_impersonate_commander(self):
        self.assert_rejected(fixture(), actor='other')

    def test_revoked_mandate_is_observed_and_rejected(self):
        world = fixture()
        world.s['r9']['mandates']['issue-authority']['active'] = False
        error = self.assert_rejected(world)
        self.assertIn(('r9', 'mandates', 'issue-authority', 'active'), error.dependencies['reads'])

    def test_missing_authority_has_negative_lookup_evidence(self):
        world = fixture()
        del world.s['r9']['mandates']['issue-authority']
        error = self.assert_rejected(world)
        self.assertIn(('r9', 'mandates', 'issue-authority', '@exists'), error.dependencies['reads'])

    def test_wrong_actor_scope_future_or_expired_mandate_is_rejected(self):
        for key, value in [('actor', 'other'), ('operations', ['record_design']),
                           ('effective_at', 1000), ('valid_until', 0), ('source_ref', '')]:
            with self.subTest(key=key):
                world = fixture()
                world.s['r9']['mandates']['issue-authority'][key] = value
                self.assert_rejected(world)

    def test_revoked_expired_or_unreceived_order_is_rejected(self):
        for key, value in [('revoked', True), ('received_at', 1000), ('recipient', 'other')]:
            with self.subTest(key=key):
                world = fixture()
                world.s['orders']['order-1'][key] = value
                self.assert_rejected(world)
        world = fixture()
        world.s['orders']['order-1']['directives']['deadline'] = world.s['clock']
        self.assert_rejected(world)

    def test_first_recipient_write_rolls_back_when_second_exhausts_stock(self):
        world = fixture(quantity=1, persons=['worker', 'other'])
        error = self.assert_rejected(world)
        self.assertIn(('stocks', 'depot', 'kit'), error.dependencies['reads'])
        self.assertIn(('stocks', 'depot', 'kit'), error.dependencies['attempted_writes'])
        self.assertNotIn('worker', world.s['stocks'])

    def test_available_choices_do_not_reveal_stock_or_hidden_authority_validity(self):
        world = fixture()
        choices = equipment_options(world.s, 'commander')
        world.s['r9']['mandates']['issue-authority']['active'] = False
        world.s['stocks']['depot']['kit'] = 0
        world.s['stocks']['hidden-vault'] = {'kit': 4}
        world.s['actors']['other']['name'] = 'HIDDEN_PERSON_NAME'
        self.assertEqual(equipment_options(world.s, 'commander'), choices)
        self.assertNotIn('HIDDEN', json.dumps(choices))
        self.assertNotIn('remaining_stock', json.dumps(choices))
        self.assertEqual(choices[0]['order_id'], 'order-1')

    def test_other_characters_orders_and_unrelated_directives_are_not_options(self):
        world = fixture()
        world.s['orders']['private'] = {**copy.deepcopy(world.s['orders']['order-1']),
                                       'recipient': 'other', 'content': 'HIDDEN_ORDER'}
        world.s['orders']['unrelated'] = {**copy.deepcopy(world.s['orders']['order-1']),
                                        'directives': {'hidden': 'HIDDEN_DIRECTIVE'}}
        self.assertEqual(len(equipment_options(world.s, 'commander')), 1)
        self.assertNotIn('HIDDEN', json.dumps(equipment_options(world.s, 'commander')))
        self.assertEqual(equipment_options(world.s, 'other'), [])

    def test_completed_order_disappears_and_second_received_action_works(self):
        world = fixture()
        add_order(world, 'order-2')
        execute(world)
        self.assertEqual([x['order_id'] for x in equipment_options(world.s, 'commander')], ['order-2'])
        world = CoreWorld.load(world.save())
        execute(world, event_id='execute-2', order_id='order-2')
        self.assertEqual(world.s['stocks']['worker']['kit'], 2)
        self.assertEqual(equipment_options(world.s, 'commander'), [])

    def test_competing_received_orders_have_no_simultaneous_arrival_winner(self):
        world = fixture(quantity=1)
        add_order(world, 'order-2', ['other'])
        left, right = event(world, 'left'), event(world, 'right', 'order-2')
        self.assertTrue(conflicts(observe(world.s, left), observe(world.s, right)))
        result = frontier(world, [left, right])
        self.assertEqual(result['committed'], [])
        self.assertEqual(set(result['deferred']), {'left', 'right'})
        self.assertEqual(world.s['stocks'], {'depot': {'kit': 1}})
        self.assertFalse(world.s['orders']['order-1']['executed'])

    def test_recipient_dissolution_conflicts_and_then_blocks_execution(self):
        world = fixture()
        issue = event(world)
        dissolve = {'id': 'dissolve', 'at': issue['at'], 'op': 'transition_entity',
                    'params': {'campaign_id': world.s['campaign_id'], 'source_ref': 'fixture dissolution',
                               'entity_id': 'worker', 'exists': False,
                               'effective_at': world.s['entity_registry']['as_of']}}
        self.assertTrue(conflicts(observe(world.s, issue), observe(world.s, dissolve)))
        world.apply(dissolve['id'], dissolve['at'], dissolve['op'], **dissolve['params'])
        self.assert_rejected(world)

    def test_revoked_current_individual_eligibility_blocks_stale_player_list(self):
        world = fixture()
        apply(world, 'revoke-control', 'record_entity_eligibility', entity_id='commander',
              scenario_id='individual', effective_at=world.s['entity_registry']['as_of'],
              eligible=False, reason='Explicit fixture withdrawal of player eligibility')
        self.assertIn('commander', world.s['player_actor_ids'])
        self.assert_rejected(world)
        self.assertEqual(equipment_options(world.s, 'commander'), [])

    def test_simultaneous_eligibility_revocation_conflicts_with_issue(self):
        world = fixture()
        issue = event(world)
        revoke = {'id': 'revoke-control', 'at': issue['at'], 'op': 'record_entity_eligibility',
                  'params': {'campaign_id': world.s['campaign_id'], 'source_ref': 'fixture revoke',
                             'entity_id': 'commander', 'scenario_id': 'individual', 'eligible': False,
                             'reason': 'Explicit fixture revocation',
                             'effective_at': world.s['entity_registry']['as_of']}}
        self.assertTrue(conflicts(observe(world.s, issue), observe(world.s, revoke)))
        result = frontier(world, [issue, revoke])
        self.assertEqual(set(result['deferred']), {'execute', 'revoke-control'})
        self.assertEqual(result['committed'], [])
        self.assertEqual(world.s['stocks'], {'depot': {'kit': 4}})

    def test_separate_stock_effects_agree_and_observed_reads_allow_independence(self):
        world = fixture()
        apply(world, 'stock-2', 'establish_stock', location='other-depot', material='kit', quantity=4,
              inventory_evidence_ref='explicit synthetic second count')
        add_order(world, 'order-2', ['other'])
        world.s['orders']['order-2']['directives']['from'] = 'other-depot'
        left, right = event(world, 'left'), event(world, 'right', 'order-2')
        # Shared read-only control/registry/mandate lists do not invent writes.
        self.assertFalse(conflicts(observe(world.s, left), observe(world.s, right)))
        first, second = CoreWorld(state=world.s), CoreWorld(state=world.s)
        execute(first, 'left')
        execute(first, 'right', order_id='order-2')
        execute(second, 'right', order_id='order-2')
        execute(second, 'left')
        self.assertEqual(first.s['stocks'], second.s['stocks'])
        simultaneous = CoreWorld(state=world.s)
        self.assertEqual(set(frontier(simultaneous, [left, right])['committed']), {'left', 'right'})
        self.assertEqual(simultaneous.s['stocks'], first.s['stocks'])

    def test_observation_is_identical_inside_unrelated_constructor(self):
        world = fixture()
        request = event(world)
        direct = observe(world.s, request)

        class OrdinaryCaller:
            def __init__(self):
                self.certificate = observe(world.s, request)

        nested = OrdinaryCaller().certificate
        self.assertEqual(direct, nested)
        self.assertIn(('player_actor_ids',), direct['reads'])
        self.assertNotIn(('player_actor_ids',), direct['writes'])
        self.assertIn(('r9', 'mandates', 'issue-authority', 'operations'), direct['reads'])
        self.assertNotIn(('r9', 'mandates', 'issue-authority', 'operations'), direct['writes'])

    def test_instrumentation_construction_and_transaction_clone_invent_no_reads(self):
        from r9_runtime import Trace, TracedDict
        world = fixture()
        trace = Trace()
        wrapped = TracedDict(world.s, trace)
        cloned = copy.deepcopy(wrapped)
        self.assertEqual(trace.reads, set())
        self.assertEqual(trace.writes, set())
        from r9_runtime import plain
        self.assertEqual(plain(cloned), plain(wrapped))

    def faction_control(self):
        world = fixture()
        point = world.s['entity_registry']['as_of']
        apply(world, 'faction', 'register_entity', entity_id='fixture-unit', kind='faction',
              identity={'name': 'Synthetic unit', 'category': 'institution'}, effective_at=point)
        apply(world, 'faction-policy', 'record_entity_eligibility', entity_id='fixture-unit',
              scenario_id='individual', effective_at=point, eligible=True,
              reason='Explicit fixture institutional player selection',
              control={'mode': 'institutional', 'actor_ids': ['commander'], 'powers': ['declare_own_intent']})
        apply(world, 'faction-control', 'select_entity_control', entity_id='fixture-unit',
              scenario_id='individual', actor_id='commander', effective_at=point,
              instruction_ref='Explicit fixture choice of unit representative')
        apply(world, 'individual-ineligible', 'record_entity_eligibility', entity_id='commander',
              scenario_id='individual', effective_at=point, eligible=False,
              reason='Only institutional play is selected in this synthetic scenario')
        return world

    def test_faction_representative_uses_actual_faction_policy(self):
        world = self.faction_control()
        self.assertEqual(len(equipment_options(world.s, 'commander')), 1)
        self.assertEqual(execute(world)['status'], 'completed_successfully')

    def test_dissolved_controlling_faction_blocks_its_stale_representative(self):
        world = self.faction_control()
        apply(world, 'dissolve-unit', 'transition_entity', entity_id='fixture-unit', exists=False,
              effective_at=world.s['entity_registry']['as_of'])
        self.assert_rejected(world)

    def test_dissolved_control_actor_cannot_execute(self):
        world = fixture()
        apply(world, 'dissolve-actor', 'transition_entity', entity_id='commander', exists=False,
              effective_at=world.s['entity_registry']['as_of'])
        self.assert_rejected(world)

    def test_changed_client_action_after_execution_does_not_alter_committed_event(self):
        world = fixture()
        action = {'kind': 'issue_equipment', 'order_id': 'order-1'}
        result = execute_equipment_action(world, 'execute', 'commander', action, 'explicit selected action')
        before = world.save()
        action['order_id'] = 'altered'
        result['outcome']['transfers'][0]['quantity'] = 999
        self.assertEqual(world.save(), before)


if __name__ == '__main__':
    unittest.main()
