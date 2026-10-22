"""Domain routines execute through Core; legacy imports own no separate world."""
from pathlib import Path
import subprocess
import sys
import unittest

from core_world import CoreWorld, GENRE_OPS
from genre_receivers import GENRE_OPS as LEGACY_OPS, operate
from test_player_actions import fixture, event


class CoreDomainTests(unittest.TestCase):
    def test_core_bootstrap_and_equipment_execution_need_no_genre_receiver_module(self):
        script = '''import sys
from test_player_actions import fixture, execute
assert 'genre_receivers' not in sys.modules
world = fixture()
result = execute(world)
assert result['status'] == 'completed_successfully'
assert world.s['stocks']['depot']['kit'] == 3
assert world.s['stocks']['worker']['kit'] == 1
assert 'genre_receivers' not in sys.modules
'''
        result = subprocess.run([sys.executable, '-B', '-c', script],
            cwd=Path(__file__).resolve().parent, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_creator_compatibility_import_forwards_to_the_same_core_routine(self):
        self.assertIs(LEGACY_OPS, GENRE_OPS)
        world = fixture()
        state = world.s
        directive = state['orders']['order-1']['directives']
        operate(world, state, state['clock']+1, 'military_issue_equipment',
            {'order_id': 'order-1', 'commander': 'commander', 'persons': directive['persons'],
             'material': directive['material'], 'from': directive['from'],
             'quantity_each': directive['quantity_each'], 'authority_ref': 'issue-authority',
             'source_ref': 'synthetic compatibility request'})
        world._validate(state)
        self.assertEqual(state['stocks']['depot']['kit'], 3)
        self.assertEqual(state['stocks']['worker']['kit'], 1)
        self.assertTrue(state['orders']['order-1']['executed'])
        self.assertIsInstance(world, CoreWorld)


if __name__ == '__main__': unittest.main()
