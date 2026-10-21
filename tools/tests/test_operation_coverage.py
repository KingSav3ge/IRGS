"""Qualification must preserve gaps and distinguish evidence from declarations."""
import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import build_operation_register as register
from operation_inventory import inventory, owner_classification


class OperationCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.declarations = inventory(register.RUNTIME)
        cls.inputs = register.source_identity()

    def evidence(self, **changes):
        return {'operation': 'transfer_stock', 'backend': 'CoreWorld',
                'actual_backend': 'CoreWorld', 'profile': 'IRGS-CORE-3.3',
                'test_id': 'synthetic.test_transfer', 'status': 'success', 'usable': True,
                'executions': 1, 'capture_origin': 'actual_apply', 'reads': [('stocks', 'depot', 'kit')],
                'writes': [('stocks', 'recipient', 'kit')],
                'validation_reads': [('opening_stock', 'kit')],
                'attempted_writes': [], **changes}

    def report(self, records=(), outcomes=None):
        summary = {'tests_successful': True, 'tests_run': 1, 'passed': 1,
                   'skipped': 0, 'failures': 0, 'errors': 0,
                   'test_outcomes': outcomes or {'synthetic.test_transfer': 'passed'}}
        return register.merge_evidence(self.declarations, list(records), summary,
                                       self.inputs, generated_at='2026-10-21T00:00:00+00:00')

    def row(self, report, backend='CoreWorld', operation='transfer_stock'):
        return next(row for row in report['operations']
                    if row['backend'] == backend and row['operation'] == operation)

    def test_live_dispatch_is_complete_and_aliases_do_not_invent_a_fifth_engine(self):
        rows = self.declarations
        keys = [(row['backend'], row['operation']) for row in rows]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual({row['backend'] for row in rows},
                         {'World', 'CoreWorld', 'R7World', 'ReceiverWorld'})
        self.assertTrue(all(row['implementation_sources'] for row in rows))
        alias = next(row for row in rows if row['backend'] == 'CoreWorld'
                     and row['operation'] == 'ast_transfer_stock')
        self.assertEqual(alias['canonical_operation'], 'transfer_stock')
        self.assertEqual(alias['alias_of'], 'transfer_stock')

    def test_same_operation_name_retains_different_backend_implementation(self):
        core = next(row for row in self.declarations
                    if row['backend'] == 'CoreWorld' and row['operation'] == 'receive_order')
        research = next(row for row in self.declarations
                        if row['backend'] == 'World' and row['operation'] == 'receive_order')
        self.assertNotEqual(core['implementation_sources'], research['implementation_sources'])

    def test_fixture_and_content_inputs_are_part_of_evidence_identity(self):
        for name in ('IRGS_3_3/data/catalog.json', 'IRGS_3_3/data/ast_registry.json',
                     'IRGS_3_3/data/hyw_1415_opening.json', 'IRGS_3_3/catalog/source_manifest.json',
                     'IRGS_3_3/release.json', 'IRGS_Web/server.py'):
            self.assertIn(name, self.inputs)
        self.assertFalse(any('/saves/' in name or '/results/' in name for name in self.inputs))

    def test_a_declared_operation_with_no_run_is_an_explicit_gap(self):
        report = self.report()
        self.assertEqual(self.row(report)['coverage_status'], 'UNQUALIFIED')
        self.assertEqual(self.row(report)['reads'], [])
        self.assertEqual(report['summary']['pairs_with_success'], 0)
        self.assertFalse(report['summary']['all_branches_certified'])

    def test_only_the_observed_backend_gets_the_actual_paths(self):
        report = self.report([self.evidence(operation='receive_order', backend='R7World')])
        row = self.row(report, 'R7World', 'receive_order')
        self.assertEqual(row['reads'], ['/stocks/depot/kit'])
        self.assertEqual(row['successful_observations'], 1)
        self.assertEqual(self.row(report, 'CoreWorld', 'receive_order')['successful_observations'], 0)
        self.assertFalse(row['all_branches_certified'])

    def test_failed_paths_retain_reads_without_claiming_rolled_back_effects(self):
        report = self.report([self.evidence(status='failed_attempt', writes=[],
                                            attempted_writes=[('stocks', 'depot', 'kit')])])
        row = self.row(report)
        self.assertEqual(row['coverage_status'], 'OBSERVED_FAILURE_ONLY')
        self.assertEqual(row['failed_attempt_reads'], ['/stocks/depot/kit'])
        self.assertEqual(row['writes'], [])
        self.assertEqual(row['failed_attempt_writes'], [])
        self.assertEqual(row['rolled_back_attempted_writes'], ['/stocks/depot/kit'])

    def test_failed_or_skipped_tests_cannot_qualify_an_operation(self):
        for outcome in ('failed', 'error', 'skipped', 'expected_failure', 'unknown'):
            with self.subTest(outcome=outcome):
                row = self.row(self.report([self.evidence()], {'synthetic.test_transfer': outcome}))
                self.assertEqual(row['successful_observations'], 0)
                self.assertEqual(row['reads'], [])

    def test_post_state_mismatch_is_a_refusal_not_success(self):
        row = self.row(self.report([self.evidence(status='observation_refused',
                                                reason_code='post_state_mismatch')]))
        self.assertEqual(row['coverage_status'], 'UNQUALIFIED')
        self.assertEqual(row['observation_refusals'], 1)
        self.assertEqual(row['writes'], [])

    def test_unknown_backend_pair_stays_diagnostic(self):
        report = self.report([self.evidence(backend='not-a-declared-backend')])
        self.assertEqual(report['summary']['pairs_with_success'], 0)
        self.assertEqual(report['summary']['observations_outside_declared_backend_pairs'], 1)

    def test_owner_annotation_preserves_mixed_unknown_and_validation_paths(self):
        owners = owner_classification([('stocks', 'depot', 'kit'),
                                       ('entity_registry', 'entities', 'ambiguous-identity'),
                                       ('unrecognized-domain', 'actual-read')],
                                      validation_paths=[('opening_stock', 'kit')])
        self.assertIn('K-STOCK', owners['owners'])
        self.assertTrue(owners['unmapped_paths'])
        self.assertIn('validation', owners)

    def test_pointer_escaping_does_not_merge_different_resource_keys(self):
        self.assertEqual(register.pointer(('stocks', 'depot/one', 'kit~old')),
                         '/stocks/depot~1one/kit~0old')
        self.assertNotEqual(register.pointer(('a/b',)), register.pointer(('a', 'b')))

    def test_check_rejects_code_drift_missing_pairs_and_blanket_claims(self):
        report = self.report()
        self.assertEqual(register.check_register(report)['status'], 'current')
        with patch.object(register, 'source_identity', return_value={'changed': 'input'}):
            with self.assertRaisesRegex(ValueError, 'stale'):
                register.check_register(report)
        missing = copy.deepcopy(report)
        missing['operations'].pop()
        with self.assertRaisesRegex(ValueError, 'missing'):
            register.check_register(missing)
        overclaim = copy.deepcopy(report)
        overclaim['operations'][0]['all_branches_certified'] = True
        with self.assertRaisesRegex(ValueError, 'overclaims'):
            register.check_register(overclaim)

    def test_output_cannot_target_a_save_or_an_executable(self):
        for target in (register.ROOT / 'IRGS_Web/saves/overwrite.json',
                       register.ROOT.parent / 'outside.json',
                       register.ROOT / 'IRGS_3_3/runtime/core_world.py'):
            with self.subTest(target=target), self.assertRaises(ValueError):
                register.safe_destination(target, '.json')


if __name__ == '__main__':
    unittest.main()
