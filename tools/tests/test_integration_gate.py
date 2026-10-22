"""Component qualification must precede importing a new joined source set."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_integration_gate import assess


class IntegrationGateTests(unittest.TestCase):
    def setUp(self):
        self.commits = {'engine': '1' * 40, 'app': '2' * 40, 'catalog': '3' * 40}
        self.pins = {'engine': self.commits['engine'], 'catalog': self.commits['catalog']}
        self.document = {'schema_version': 1, 'cycle_id': 'synthetic-reviewed-set',
            'baseline_components': {name: '0' * 40 for name in self.commits},
            'reviews': {name: {'status': 'approved', 'commit': commit,
                'deliverable': 'component_update', 'checks': [{'name': 'synthetic qualification', 'status': 'passed'}]}
                for name, commit in self.commits.items()}}

    def test_all_three_exact_approved_updates_with_matching_pins_are_ready(self):
        self.assertTrue(assess(self.document, self.commits, self.pins)['ready'])

    def test_one_missing_or_unchanged_component_holds_the_entire_set(self):
        for name in self.commits:
            with self.subTest(name=name):
                document = copy.deepcopy(self.document)
                document['baseline_components'][name] = self.commits[name]
                self.assertFalse(assess(document, self.commits, self.pins)['ready'])
                document = copy.deepcopy(self.document)
                document['reviews'][name]['status'] = 'pending'
                self.assertFalse(assess(document, self.commits, self.pins)['ready'])

    def test_stale_approval_failed_checks_and_planning_only_delivery_are_held(self):
        for changes in ({'commit': '4' * 40}, {'checks': []},
                {'checks': [{'status': 'failed'}]}, {'deliverable': 'coordination_guidance'}):
            with self.subTest(changes=changes):
                document = copy.deepcopy(self.document)
                document['reviews']['engine'].update(changes)
                self.assertFalse(assess(document, self.commits, self.pins)['ready'])

    def test_mismatched_pins_and_missing_cycle_cannot_approve_an_import(self):
        for name in self.pins:
            pins = dict(self.pins, **{name: '4' * 40})
            self.assertFalse(assess(self.document, self.commits, pins)['ready'])
        self.assertFalse(assess({}, self.commits, self.pins)['ready'])
        document = copy.deepcopy(self.document)
        document['baseline_components'] = {}
        self.assertFalse(assess(document, self.commits, self.pins)['ready'])


if __name__ == '__main__':
    unittest.main()
