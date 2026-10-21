"""Synthetic qualification of authored local actions, not historical calibration."""
import copy
import unittest

from campaign_library import initial_campaign
from core_world import CoreWorld
from irgs_reference import InvalidEvent
from scene_actions import (OPERATION, SceneActionUnavailable,
                           execute_scene_action, scene_options)


def apply(world, key, op, **params):
    world.apply(key, world.s['clock'] + 1, op, campaign_id=world.s['campaign_id'],
                source_ref='synthetic-opening-selection', **params)


def fixture():
    world = initial_campaign('military', 'synthetic-scene')
    apply(world, 'actor', 'register_actor', actor_id='pc', name='Synthetic courier', species='human',
          player_controlled=True, instruction_ref='explicit synthetic character selection')
    apply(world, 'map', 'record_evidence', evidence_id='setup:scene-map', subject='pc',
          assertion='Authored local map and dispatch custody were selected.', status='established')
    apply(world, 'map-received', 'receive_evidence', evidence_id='setup:scene-map', recipient='pc')
    received = world.s['clock']
    apply(world, 'position', 'record_evidence', evidence_id='setup:position', subject='pc',
          assertion='The courier is at the quay.', status='established')
    apply(world, 'position-received', 'receive_evidence', evidence_id='setup:position', recipient='pc')
    apply(world, 'located', 'confirm_character_field', subject='pc', field='location', value='quay',
          evidence_id='setup:position', authority_ref='synthetic-opening-selection', instruction_ref='explicit setup')
    apply(world, 'letter', 'establish_stock', location='pc', material='sealed_dispatch', quantity=1,
          inventory_evidence_ref='synthetic-opening-selection')
    apply(world, 'tray', 'establish_stock', location='clerk-tray', material='sealed_dispatch', quantity=0,
          inventory_evidence_ref='synthetic-opening-selection')
    rules = {'schema_version': 1, 'id': 'synthetic-delivery', 'source_ref': 'synthetic-opening-selection',
        'actor_id': 'pc', 'received_at': received, 'receipt_evidence_id': 'setup:scene-map',
        'setup_instruction_ref': 'explicit synthetic authored-scene selection',
        'elapsed_axis': 'authored-opening-seconds',
        'places': {
            'quay': {'title': 'Quay', 'description': 'Authored quay.', 'observe': 'You see the passage and the closed gate.',
                     'actions': ['look-quay', 'try-gate', 'enter-passage']},
            'passage': {'title': 'Passage', 'description': 'Authored passage.', 'observe': 'The desk lies ahead.',
                        'actions': ['reach-desk', 'return-quay']},
            'desk': {'title': 'Desk', 'description': 'Authored receiving desk.', 'observe': 'The receiving tray is on the desk.',
                     'actions': ['deliver', 'look-desk']}},
        'actions': {}}
    def action(key, kind, origin, duration, **extra):
        rules['actions'][key] = {'kind': kind, 'from': origin, 'label': key, 'text': 'I attempt ' + key + '.',
            'description': 'Authored choice ' + key, 'duration_seconds': duration,
            'success_text': 'Completed ' + key + '.', 'failure_text': 'The gate remains closed; you stay at the quay.', **extra}
    action('look-quay', 'observe', 'quay', 3)
    action('try-gate', 'move', 'quay', 5, to='desk', blocked_by='quay-gate')
    action('enter-passage', 'move', 'quay', 20, to='passage')
    action('reach-desk', 'move', 'passage', 15, to='desk')
    action('return-quay', 'move', 'passage', 20, to='quay')
    action('look-desk', 'observe', 'desk', 3)
    action('deliver', 'deliver', 'desk', 4, material='sealed_dispatch', destination='clerk-tray', quantity=1,
           failure_text='You no longer carry the dispatch; no item is transferred.')
    world.s['scene_rules'] = rules
    world.s['elapsed_time'] = {'axis': 'authored-opening-seconds', 'seconds': 0,
                               'source_ref': 'synthetic-opening-selection'}
    world.s['site_conditions'] = {'quay-gate': {'passable': False, 'source_ref': 'synthetic-obstruction'}}
    return world


def execute(world, action_id, event_id=None, actor='pc'):
    return execute_scene_action(world, event_id or 'execute:' + action_id, actor,
        {'kind': 'scene_action', 'action_id': action_id}, 'explicit selected action:' + (event_id or action_id))


class SceneActionTests(unittest.TestCase):
    def assert_rejected(self, world, action='look-quay', event_id=None, actor='pc'):
        before = world.save()
        with self.assertRaises(SceneActionUnavailable) as error:
            execute(world, action, event_id, actor)
        self.assertEqual(world.save(), before)
        self.assertEqual(error.exception.dependencies['writes'], [])
        self.assertFalse(error.exception.dependencies['successful_certificate'])
        return error.exception

    def test_complete_arc_commits_conserved_delivery_and_repeatable_next_action(self):
        world = fixture()
        calendar = copy.deepcopy(world.s['campaign_time'])
        self.assertEqual(execute(world, 'look-quay')['outcome']['observations'],
                         ['You see the passage and the closed gate.'])
        blocked = execute(world, 'try-gate')
        self.assertEqual(blocked['status'], 'completed_unsuccessfully')
        self.assertEqual(world.s['actors']['pc']['current']['location']['value'], 'quay')
        self.assertEqual(world.s['stocks']['pc']['sealed_dispatch'], 1)
        execute(world, 'enter-passage')
        execute(world, 'reach-desk')
        delivered = execute(world, 'deliver')
        self.assertEqual(delivered['status'], 'completed_successfully')
        self.assertEqual(delivered['outcome']['elapsed_total'], 47)
        self.assertEqual(world.s['stocks'], {'pc': {'sealed_dispatch': 0}, 'clerk-tray': {'sealed_dispatch': 1}})
        self.assertEqual(world.s['opening_stock'], {'sealed_dispatch': 1})
        self.assertEqual(world.s['campaign_time'], calendar)
        self.assertEqual(execute(world, 'look-desk')['outcome']['elapsed_total'], 50)
        self.assertEqual(execute(world, 'look-desk', 'another-look')['outcome']['elapsed_total'], 53)
        self.assertEqual(len(world.s['scene_action_results']), 7)

    def test_movement_is_evidence_backed_and_actually_received(self):
        world = fixture()
        result = execute(world, 'enter-passage')
        current = world.s['actors']['pc']['current']['location']
        evidence = world.s['evidence'][current['evidence_id']]
        self.assertEqual(current['value'], 'passage')
        self.assertEqual(evidence['status'], 'established')
        self.assertIn(current['evidence_id'], world.s['knowledge']['pc'])
        self.assertEqual(current['at'], result['receipt']['at'])
        self.assertEqual(world.s['actors']['pc']['current']['current_activity']['value'], 'Authored passage.')

    def test_options_do_not_filter_hidden_conditions_or_depleted_stock(self):
        world = fixture()
        before = scene_options(world.s, 'pc')
        world.s['site_conditions']['quay-gate']['passable'] = True
        self.assertEqual(scene_options(world.s, 'pc'), before)
        execute(world, 'enter-passage'); execute(world, 'reach-desk')
        before = scene_options(world.s, 'pc')
        execute(world, 'deliver')
        self.assertEqual(scene_options(world.s, 'pc'), before)
        self.assertTrue(any(row['action_id'] == 'deliver' for row in before))
        before_stock = copy.deepcopy(world.s['stocks'])
        failed = execute(world, 'deliver', 'deliver-again')
        self.assertEqual(failed['status'], 'completed_unsuccessfully')
        self.assertEqual(failed['outcome']['elapsed_seconds'], 4)
        self.assertEqual(world.s['stocks'], before_stock)

    def test_real_route_condition_changes_outcome(self):
        world = fixture()
        world.s['site_conditions']['quay-gate']['passable'] = True
        result = execute(world, 'try-gate')
        self.assertEqual(result['status'], 'completed_successfully')
        self.assertEqual(world.s['actors']['pc']['current']['location']['value'], 'desk')

    def test_actual_reads_include_control_map_location_elapsed_and_condition(self):
        result = execute(fixture(), 'try-gate')
        reads = result['dependencies']['reads']
        for path in [('player_actor_ids',), ('knowledge', 'pc', 'setup:scene-map', 'received_at'),
                     ('actors', 'pc', 'current', 'location', 'value'),
                     ('scene_rules', 'actions', 'try-gate', 'duration_seconds'),
                     ('scene_rules', 'setup_instruction_ref'), ('elapsed_time', 'seconds'),
                     ('site_conditions', 'quay-gate', 'passable')]:
            self.assertIn(path, reads)
        self.assertTrue(any(path[0] == 'entity_registry' for path in reads))
        self.assertNotIn(('stocks', 'pc', 'sealed_dispatch'), result['dependencies']['writes'])

    def test_delivery_reads_actual_stock_and_changes_conserved_custody(self):
        world = fixture()
        execute(world, 'enter-passage'); execute(world, 'reach-desk')
        result = execute(world, 'deliver')
        self.assertIn(('stocks', 'pc', 'sealed_dispatch'), result['dependencies']['reads'])
        self.assertIn(('stocks', 'clerk-tray', 'sealed_dispatch'), result['dependencies']['writes'])

    def test_other_actor_no_control_and_revoked_eligibility_are_refused(self):
        self.assert_rejected(fixture(), actor='other')
        world = fixture()
        world.s['entity_registry']['eligibility']['individual:pc']['versions'][-1]['eligible'] = False
        self.assertEqual(scene_options(world.s, 'pc'), [])
        self.assert_rejected(world)

    def test_absent_future_or_wrong_map_receipt_is_refused(self):
        for mutation in ('absent', 'future', 'wrong-subject', 'no-consent', 'map-not-established'):
            with self.subTest(mutation=mutation):
                world = fixture()
                if mutation == 'absent': del world.s['knowledge']['pc']['setup:scene-map']
                elif mutation == 'future': world.s['scene_rules']['received_at'] = world.s['clock'] + 1
                elif mutation == 'wrong-subject': world.s['evidence']['setup:scene-map']['subject'] = 'other'
                elif mutation == 'no-consent': world.s['scene_rules']['setup_instruction_ref'] = ''
                else: world.s['evidence']['setup:scene-map']['status'] = 'testimony'
                self.assertEqual(scene_options(world.s, 'pc'), [])
                self.assert_rejected(world)

    def test_location_wrong_action_invalid_duration_or_axis_is_refused(self):
        self.assert_rejected(fixture(), 'deliver')
        for value in (None, 0, -1, True, '3'):
            with self.subTest(duration=value):
                world = fixture(); world.s['scene_rules']['actions']['look-quay']['duration_seconds'] = value
                self.assert_rejected(world)
        world = fixture(); world.s['elapsed_time']['axis'] = 'unrelated-axis'
        self.assert_rejected(world)

    def test_native_frozen_replay_and_public_duplicate_do_not_repeat_work(self):
        world = fixture(); execute(world, 'look-quay')
        accepted = copy.deepcopy(world.s['journal'][-1])
        loaded = CoreWorld.load(world.save()); before = loaded.save()
        self.assertFalse(loaded.apply(accepted['id'], accepted['at'], accepted['op'], **accepted['params']))
        with self.assertRaises(InvalidEvent): execute(loaded, 'look-quay')
        self.assertEqual(loaded.save(), before)

    def test_late_failure_rolls_back_transfer_and_elapsed_work(self):
        world = fixture(); execute(world, 'enter-passage'); execute(world, 'reach-desk')
        apply(world, 'prior-evidence', 'record_evidence', evidence_id='scene:duplicate', subject='pc',
              assertion='Existing synthetic evidence.', status='established')
        error = self.assert_rejected(world, 'deliver', 'duplicate')
        self.assertTrue(any(path[0] == 'stocks' for path in error.dependencies['attempted_writes']))
        self.assertEqual(world.s['elapsed_time']['seconds'], 35)

    def test_action_payload_cannot_override_effects(self):
        world = fixture(); before = world.save()
        for action in ({'kind': 'scene_action', 'action_id': 'look-quay', 'duration_seconds': 0},
                       {'kind': 'deliver', 'action_id': 'deliver'},
                       {'kind': 'scene_action', 'action_id': ''}):
            with self.subTest(action=action), self.assertRaises(InvalidEvent):
                execute_scene_action(world, 'bad', 'pc', action, 'explicit request')
        self.assertEqual(world.save(), before)
        self.assertEqual(OPERATION, 'execute_player_scene_action')

    def test_other_activity_cannot_be_bypassed_without_elapsed_binding(self):
        world = fixture()
        apply(world, 'capacity', 'record_capacity', capacity_id='other-site', site='other-site',
              quantity=1, unit='concurrent_people')
        apply(world, 'other-work', 'commit_activity', activity_id='other-work', actors=['pc'],
              site='other-site', capacity_id='other-site', start=world.s['clock'] + 2,
              end=world.s['clock'] + 20, role='existing commitment', authority_ref='fixture',
              instruction_ref='explicit other work')
        self.assert_rejected(world, 'enter-passage')
        self.assertEqual(world.s['elapsed_time']['seconds'], 0)


if __name__ == '__main__':
    unittest.main()
