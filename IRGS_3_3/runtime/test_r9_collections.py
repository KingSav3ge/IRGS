"""Whole-list read/mutation qualification for reviewed R9 JSON handlers."""
import copy
import unittest

from irgs_reference import InvalidEvent
from r9_runtime import Trace, TracedDict, plain
from test_player_actions import event, fixture
from r9_runtime import observe


class CollectionObservationTests(unittest.TestCase):
    def wrapped(self, values=None):
        trace = Trace()
        return TracedDict({'rows': [3, 1, 2] if values is None else values}, trace), trace

    def test_read_index_slice_length_order_membership_and_absence_are_not_writes(self):
        state, trace = self.wrapped()
        rows = state['rows']
        self.assertEqual(rows[0], 3)
        self.assertEqual(rows[:2], [3, 1])
        self.assertEqual(len(rows), 3)
        self.assertEqual(list(rows), [3, 1, 2])
        self.assertEqual(list(reversed(rows)), [2, 1, 3])
        self.assertNotIn(9, rows)
        self.assertEqual(rows.index(1), 1)
        self.assertEqual(rows.count(9), 0)
        with self.assertRaises(IndexError):
            rows[99]
        self.assertIn(('rows',), trace.reads)
        self.assertEqual(trace.writes, set())

    def test_standard_mutators_record_whole_list_writes_and_match_python(self):
        def assign(rows):rows[0] = 8
        def delete(rows):del rows[0]
        def slice_assign(rows):rows[1:] = [8, 9]
        def slice_delete(rows):del rows[1:]
        def in_place_add(rows):rows += [8]
        def in_place_multiply(rows):rows *= 2
        mutations = [lambda r: r.append(8), lambda r: r.extend([8, 9]),
                     lambda r: r.insert(1, 8), lambda r: r.pop(), lambda r: r.remove(1),
                     lambda r: r.clear(), lambda r: r.sort(), lambda r: r.reverse(),
                     assign, delete, slice_assign, slice_delete, in_place_add, in_place_multiply]
        for index, mutate in enumerate(mutations):
            with self.subTest(mutator=index):
                state, trace = self.wrapped()
                expected = [3, 1, 2]
                mutate(expected)
                mutate(state['rows'])
                self.assertEqual(plain(state)['rows'], expected)
                self.assertIn(('rows',), trace.writes)
                self.assertIn(('rows',), trace.reads)

    def test_nested_held_reference_keeps_its_new_index_after_insertion(self):
        state, trace = self.wrapped([{'value': 1}, {'value': 2}])
        held = state['rows'][0]
        state['rows'].insert(0, {'value': 0})
        held['value'] = 7
        self.assertEqual(plain(state)['rows'], [{'value': 0}, {'value': 7}, {'value': 2}])
        self.assertIn(('rows', '1', 'value'), trace.writes)

    def test_nested_list_mutation_records_its_container_without_outer_false_write(self):
        state, trace = self.wrapped([[1], [2]])
        state['rows'][0].append(3)
        self.assertEqual(plain(state)['rows'], [[1, 3], [2]])
        self.assertIn(('rows', '0'), trace.writes)
        self.assertNotIn(('rows',), trace.writes)

    def test_self_extend_matches_python_list_semantics(self):
        state, trace = self.wrapped()
        rows = state['rows']
        rows.extend(rows)
        self.assertEqual(plain(state)['rows'], [3, 1, 2, 3, 1, 2])
        self.assertIn(('rows',), trace.writes)

    def test_validation_list_reads_are_separate_and_mutation_is_refused(self):
        state, trace = self.wrapped()

        def validate_example():
            return len(state['rows']) == 3

        def validate_bad_example():
            state['rows'].append(7)

        self.assertTrue(validate_example())
        self.assertIn(('rows',), trace.validation_reads)
        self.assertEqual(trace.reads, set())
        self.assertEqual(trace.writes, set())
        with self.assertRaises(InvalidEvent):
            validate_bad_example()
        self.assertEqual(plain(state)['rows'], [3, 1, 2])

    def test_clone_and_flatten_are_bookkeeping_but_explicit_nested_copy_is_read(self):
        state, trace = self.wrapped()
        cloned = copy.deepcopy(state)
        self.assertEqual(plain(cloned), plain(state))
        self.assertEqual(trace.reads, set())
        self.assertEqual(trace.writes, set())
        detached = copy.deepcopy(state['rows'])
        detached.append(7)
        self.assertEqual(plain(state)['rows'], [3, 1, 2])
        self.assertIn(('rows',), trace.reads)
        self.assertEqual(trace.writes, set())

    def test_native_player_registration_appends_actual_control_list(self):
        world = fixture()
        request = {'id': 'new-player', 'at': world.s['clock'] + 1, 'op': 'register_actor',
                   'params': {'campaign_id': world.s['campaign_id'], 'source_ref': 'fixture selection',
                              'instruction_ref': 'fixture explicit control', 'actor_id': 'second-player',
                              'name': 'Second player', 'species': 'human', 'player_controlled': True}}
        certificate = observe(world.s, request)
        self.assertIn(('player_actor_ids',), certificate['writes'])
        self.assertNotIn('second-player', world.s['actors'])

    def test_successful_equipment_list_reads_do_not_reserve_authority_as_write(self):
        world = fixture()
        certificate = observe(world.s, event(world))
        for path in [('player_actor_ids',), ('orders', 'order-1', 'directives', 'persons'),
                     ('r9', 'mandates', 'issue-authority', 'operations')]:
            self.assertIn(path, certificate['reads'])
            self.assertNotIn(path, certificate['writes'])


if __name__ == '__main__':
    unittest.main()
