"""The collector must refuse misleading evidence and restore live methods."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'tools'), str(ROOT / 'IRGS_3_3/runtime')]
from coverage_capture import capture_suite
from campaign_library import initial_campaign
from core_world import CoreWorld
from irgs_reference import InvalidEvent
import r9_runtime


def event(world, key):
    return {'id': key, 'at': world.s['clock'] + 1, 'op': 'register_actor',
            'params': {'campaign_id': world.s['campaign_id'], 'source_ref': 'explicit-synthetic-capture-test',
                       'actor_id': key, 'name': key, 'species': 'human', 'player_controlled': False}}


class CaptureSafetyTests(unittest.TestCase):
    def capture(self, body):
        class Example(unittest.TestCase):
            def runTest(example):
                body(example)
        suite = unittest.TestSuite([Example()])
        with patch.object(unittest.TestLoader, 'discover', return_value=suite):
            return capture_suite(ROOT / 'IRGS_3_3/runtime')

    def test_actual_apply_and_detached_probe_are_distinct(self):
        def body(test):
            world = initial_campaign('military', 'capture-origin-fixture')
            first = event(world, 'actual')
            world.apply(first['id'], first['at'], first['op'], **first['params'])
            r9_runtime.observe(world.s, event(world, 'probe-only'))
            test.assertNotIn('probe-only', world.s['actors'])
        summary, records, _ = self.capture(body)
        self.assertTrue(summary['tests_successful'])
        self.assertEqual({row['capture_origin'] for row in records if row['status'] == 'success'},
                         {'actual_apply', 'direct_observe'})

    def test_instrumentation_failure_is_not_a_failed_handler_case(self):
        def body(test):
            world = initial_campaign('military', 'capture-probe-failure')
            with test.assertRaises(InvalidEvent):
                r9_runtime.observe(world.s, event(world, 'valid-ordinary-operation'))
            test.assertEqual(world.s['actors'], {})
        with patch.object(r9_runtime, 'observe', side_effect=InvalidEvent('synthetic observer refusal')):
            summary, records, _ = self.capture(body)
        self.assertTrue(summary['tests_successful'])
        self.assertTrue(records)
        self.assertTrue(all(row['status'] == 'observation_refused' for row in records))
        self.assertTrue(all(not row['writes'] for row in records))

    def test_rejecting_actual_handler_with_live_mutation_is_not_rollback_evidence(self):
        def broken_apply(world, *args, **kwargs):
            world.s['capture-test-mutation'] = True
            raise InvalidEvent('synthetic broken transaction')
        def body(test):
            world = initial_campaign('military', 'capture-atomicity-fixture')
            current = event(world, 'bad')
            with test.assertRaises(InvalidEvent):
                world.apply(current['id'], current['at'], current['op'], **current['params'])
        with patch.object(CoreWorld, 'apply', broken_apply):
            summary, records, _ = self.capture(body)
        self.assertTrue(summary['tests_successful'])
        self.assertTrue(any(row['status'] == 'observation_refused'
                            and 'atomicity_violation' in row.get('reason_code', '') for row in records))
        self.assertFalse(any(row['status'] == 'failed_attempt' for row in records))

    def test_uninstrumentable_state_is_not_a_failed_handler_path(self):
        def body(test):
            with test.assertRaises((InvalidEvent, KeyError, AssertionError)):
                r9_runtime.observe({'profile': 'IRGS-CORE-3.3', 'processed': {}},
                    {'id': 'invalid-state', 'at': 1, 'op': 'register_actor', 'params': {}})
        summary, records, _ = self.capture(body)
        self.assertTrue(summary['tests_successful'])
        self.assertTrue(records)
        self.assertTrue(all(row['status'] == 'observation_refused' for row in records))

    def test_valid_rejected_attempt_has_reads_and_no_committed_writes(self):
        def body(test):
            world = initial_campaign('military', 'capture-real-rejection')
            before = world.save()
            with test.assertRaises(InvalidEvent):
                world.apply('no-stock', 1, 'transfer_stock', campaign_id=world.s['campaign_id'],
                    source_ref='synthetic-explicit-attempt', authority_ref='fixture',
                    **{'from': 'missing', 'to': 'recipient', 'material': 'kit', 'quantity': 1})
            test.assertEqual(world.save(), before)
        summary, records, _ = self.capture(body)
        self.assertTrue(summary['tests_successful'])
        failed = [row for row in records if row['status'] == 'failed_attempt']
        self.assertTrue(failed)
        self.assertTrue(all(row['reads'] and row['writes'] == [] for row in failed))

    def test_patches_are_restored_after_an_unsuccessful_test(self):
        original_apply, original_observe = CoreWorld.apply, r9_runtime.observe
        def body(test):
            raise RuntimeError('synthetic fixture error')
        summary, _, _ = self.capture(body)
        self.assertFalse(summary['tests_successful'])
        self.assertIs(CoreWorld.apply, original_apply)
        self.assertIs(r9_runtime.observe, original_observe)


if __name__ == '__main__':
    unittest.main()
