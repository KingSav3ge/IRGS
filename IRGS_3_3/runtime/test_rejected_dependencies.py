"""Named failed-path evidence across existing backends, not all-branch proof."""
import copy
import itertools
import json
import unittest
from unittest.mock import patch

from irgs_reference import InvalidEvent, World, initial_world, digest
from r9_runtime import (TracedDict, frontier, observe, observe_rejection)
from player_actions import _failed_dependencies
from test_player_actions import fixture as equipment_world, event as equipment_event
from test_r7_integration import world as economic_world
from test_r9_runtime import receiver, roman
import test_settlement as settlement_fixtures


def transfer(world, identity='failed', amount=1001, source='treasury', target='army'):
    return {'id': identity, 'at': world.s['clock']+1, 'op': 'transfer_cash',
            'params': {'from': source, 'to': target, 'amount': amount}}


class RejectedDependencyTests(unittest.TestCase):
    def rejection(self, world, event, backend, required_path):
        before = world.save()
        certificate = observe_rejection(world.s, event)
        self.assertEqual(world.save(), before)
        self.assertEqual(certificate['backend'], backend)
        self.assertEqual(certificate['status'], 'rejected_no_effects')
        self.assertIs(certificate['successful_certificate'], False)
        self.assertEqual(certificate['snapshot'], digest(world.s))
        self.assertEqual(certificate['post_state'], certificate['snapshot'])
        self.assertEqual(certificate['writes'], [])
        self.assertIn(required_path, certificate['reads'])
        self.assertEqual(certificate['event'], event)
        with self.assertRaises(InvalidEvent): observe(world.s, event)
        return certificate

    def test_reference_late_rejection_retains_reads_and_rolled_back_attempts(self):
        world = initial_world()
        cert = self.rejection(world, transfer(world, amount=1, target='missing-account'),
                              'World', ('cash', 'treasury'))
        self.assertIn(('cash', 'treasury'), cert['attempted_writes'])
        self.assertIn(('cash', 'missing-account', '@exists'), cert['reads'])
        self.assertNotIn(('population', 'baseline'), cert['reads'])

    def test_economic_rejection_uses_the_selected_backend(self):
        world = economic_world()
        event = transfer(world, amount=world.s['cash']['farmer-a']+1, source='farmer-a')
        self.rejection(world, event, 'R7World', ('cash', 'farmer-a'))

    def test_receiver_rejection_retains_actual_revoked_delegation_read(self):
        world = receiver()
        world.s['r9_delegations']['farm']['active'] = False
        self.rejection(world, roman(), 'ReceiverWorld', ('r9_delegations', 'farm', 'active'))

    def test_selected_core_rejection_retains_scarce_stock_read(self):
        world = equipment_world(quantity=0)
        self.rejection(world, equipment_event(world), 'CoreWorld', ('stocks', 'depot', 'kit'))

    def test_missing_order_retains_the_negative_lookup(self):
        world = equipment_world()
        event = equipment_event(world, order_id='missing-order')
        self.rejection(world, event, 'CoreWorld', ('orders', 'missing-order', '@exists'))

    def test_settlement_rejection_retains_actual_permission_and_worker_reads(self):
        fixture = settlement_fixtures.SettlementTests()
        world = fixture.world(permission='held')
        fixture.camp(world)
        world.s['grants']['founding']['active'] = False
        event = {'id': 'blocked-build', 'at': world.s['clock']+1,
            'op': 'execute_settlement_action', 'params': {'campaign_id': world.s['campaign_id'],
                'actor': 'founder', 'action': 'build', 'request_id': 'blocked-build',
                'instruction_ref': 'synthetic choice', 'source_ref': 'synthetic choice'}}
        self.rejection(world, event, 'CoreWorld', ('grants', 'founding', 'active'))
        world.s['grants']['founding']['active'] = True
        fixture.act(world, 'build')
        event['id'] = 'double-booked-worker'; event['at'] = world.s['clock']+1
        event['params']['request_id'] = event['id']
        self.rejection(world, event, 'CoreWorld', ('projects', 'shelter', 'worker'))

    def test_shared_worker_rejection_keeps_actual_capacity_reads(self):
        world = initial_world()
        event = {'id': 'busy-worker', 'at': 1, 'op': 'commit_shift',
            'params': {'person': 'caregiver-1', 'start': 9, 'end': 11, 'role': 'military'}}
        self.rejection(world, event, 'World', ('commitments', 'caregiver-1'))

    def test_frontier_retains_rejection_and_its_conflict_for_both_input_orders(self):
        base = initial_world()
        failed, peer = transfer(base), transfer(base, 'peer', amount=1)
        for events in itertools.permutations([failed, peer]):
            world = World.load(base.save())
            before = copy.deepcopy(world.s)
            result = frontier(world, list(events))
            self.assertEqual(result['committed'], [])
            self.assertEqual(set(result['deferred']), {'failed', 'peer'})
            self.assertEqual({frozenset(edge) for edge in result['edges']}, {frozenset(['failed', 'peer'])})
            self.assertEqual({k:v for k,v in world.s.items() if k not in {'clock', 'r9'}},
                             {k:v for k,v in before.items() if k not in {'clock', 'r9'}})
            restored = World.load(world.save())
            request = restored.s['r9']['requests']['failed']
            self.assertEqual(request['status'], 'unresolved')
            self.assertEqual(request['dependency_status'], 'qualified_rejected_probe')
            self.assertIsNone(request['dependency_refusal'])
            self.assertEqual(request['certificate']['writes'], [])
            self.assertIn(['cash', 'treasury'], request['certificate']['reads'])
            self.assertNotIn('validation_reads', request['certificate'])
            self.assertEqual(request['original_digest'], digest(failed))
            saved = restored.save()
            with self.assertRaises(InvalidEvent): frontier(restored, [failed])
            self.assertEqual(restored.save(), saved)

    def test_unknown_or_successful_operations_cannot_be_labelled_qualified_rejections(self):
        world = initial_world(); before = world.save()
        with self.assertRaisesRegex(InvalidEvent, 'not qualified'):
            observe_rejection(world.s, {'id': 'unknown', 'at': 1, 'op': 'unknown', 'params': {}})
        with self.assertRaisesRegex(InvalidEvent, 'did not reject'):
            observe_rejection(world.s, transfer(world, amount=1))
        self.assertEqual(world.save(), before)
        result = frontier(world, [{'id': 'unknown', 'at': 1, 'op': 'unknown', 'params': {}}])
        self.assertEqual(result['deferred'], ['unknown'])
        self.assertEqual(world.s['r9']['requests']['unknown']['dependency_status'], 'unqualified')
        self.assertIsNone(world.s['r9']['requests']['unknown']['certificate'])

    def test_freshness_guard_refuses_an_already_processed_event(self):
        world = initial_world(); event = transfer(world, amount=1)
        world.apply(event['id'], event['at'], event['op'], **event['params'])
        before = world.save()
        with self.assertRaisesRegex(InvalidEvent, 'not a fresh request'):
            observe_rejection(world.s, event)
        self.assertEqual(world.save(), before)

    def test_error_mismatch_and_nonatomic_probes_are_refused(self):
        world = initial_world(); before = world.save(); event = transfer(world)
        def mismatch(worker, *args, **kwargs):
            raise InvalidEvent('traced failure' if isinstance(worker.s, TracedDict) else 'plain failure')
        def non_atomic(worker, *args, **kwargs):
            worker.s['cash']['treasury'] -= 1
            raise InvalidEvent('failure after mutation')
        def traced_mutation(worker, *args, **kwargs):
            if isinstance(worker.s, TracedDict): worker.s['cash']['treasury'] -= 1
            raise InvalidEvent('same failure')
        for behavior, reason in [(mismatch, 'differs'), (non_atomic, 'changed state'),
                                  (traced_mutation, 'changed state')]:
            with self.subTest(reason=reason), patch.object(World, 'apply', behavior):
                with self.assertRaisesRegex(InvalidEvent, reason): observe_rejection(world.s, event)
            self.assertEqual(world.save(), before)

    def test_instrumentation_refusal_does_not_manufacture_a_failed_action_certificate(self):
        world = equipment_world()
        evidence = _failed_dependencies(world.s, equipment_event(world))
        self.assertEqual(evidence['status'], 'observation_refused')
        self.assertFalse(evidence['successful_certificate'])
        self.assertEqual(evidence['writes'], [])
        world = initial_world(); event = transfer(world, amount=1)
        with patch('r9_runtime.observe', side_effect=InvalidEvent('synthetic observer refusal')):
            frontier(world, [event])
        request = world.s['r9']['requests'][event['id']]
        self.assertEqual(request['status'], 'unresolved')
        self.assertEqual(request['dependency_status'], 'unqualified')
        self.assertIsNone(request['certificate'])
        self.assertIn('did not reject', request['dependency_refusal'])
        self.assertEqual(world.s['cash']['army'], 0)


if __name__ == '__main__': unittest.main()
