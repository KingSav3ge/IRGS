"""Institution observations and rights constrain planning before truth checks."""
import copy
import unittest

from economic_extension import total
from irgs_reference import InvalidEvent
from strategic_execution import (advance, strategic_world, select_institution,
                                 observable_projection, Planner, plan_business)


def selected(world, institution):
    ledger = world.s['r8_strategy']
    return copy.deepcopy(ledger['selections'][ledger['institutions'][institution]]['selection'])


def replace_selection(world, institution, **changes):
    old = selected(world, institution)
    old.update(changes)
    return select_institution(world, institution,
        f'test:{institution}:{len(world.s["r8_strategy"]["selection_history"])}',
        old['operations'], old['observations'], world.s['clock'], 'test:explicit-source-selection',
        scope=old['scope'], active=old['active'])


class KnowledgeTests(unittest.TestCase):
    def test_projection_contains_selected_records_and_has_no_world_reference(self):
        w = strategic_world()
        view = observable_projection(w.s, selected(w, 'business'), 1)
        self.assertTrue(view.read('actors', 'person-B', 'disabled').known)
        self.assertFalse(view.read('cash', 'farmer-b').known)
        self.assertFalse(view.read('registry').known)
        self.assertFalse(hasattr(view, 'state'))
        self.assertFalse(hasattr(view, 'world'))
        recipe = view.require('econ3', 'recipes', 'cook')
        recipe['inputs']['grain'] = 999
        self.assertEqual(w.s['econ3']['recipes']['cook']['inputs']['grain'], 2)
        self.assertEqual(view.require('econ3', 'recipes', 'cook')['inputs']['grain'], 2)

    def test_hidden_change_does_not_change_business_projection_or_proposal(self):
        a, b = strategic_world(), strategic_world()
        b.s['cash']['farmer-b'] -= 20
        b.s['cash']['treasury'] += 20
        plans = []
        for w in (a, b):
            selection = selected(w, 'business')
            view = observable_projection(w.s, selection, 1)
            plan = Planner('business', selection, w.s['r8_strategy']['profile'], view, 0)
            plan_business(plan)
            plans.append((view.checksum(), plan.events))
        self.assertEqual(plans[0], plans[1])

    def test_unreceived_stock_cannot_be_assumed_available(self):
        w = strategic_world()
        observations = selected(w, 'business')['observations']
        for grant in observations:
            if grant['path'] == ['econ3', 'stocks', 'house-1']:
                grant['received_at'] = None
        replace_selection(w, 'business', observations=observations)
        advance(w, 1)
        decision = w.s['r8_strategy']['decisions'][0]['institutions']['business']
        self.assertEqual(decision['proposals'], [])
        self.assertTrue(any(r['status'] == 'unknown' for r in decision['reads']))
        self.assertNotIn('person-B', w.s['commitments'])

    def test_unknown_disability_is_not_assumed_false(self):
        w = strategic_world()
        observations = [g for g in selected(w, 'business')['observations']
                        if g['path'] != ['actors', 'person-B', 'disabled']]
        replace_selection(w, 'business', observations=observations)
        advance(w, 1)
        self.assertEqual(w.s['r8_strategy']['decisions'][0]['institutions']['business']['proposals'], [])
        self.assertNotIn('person-B', w.s['commitments'])

    def test_receipt_is_prospective_and_old_selection_survives(self):
        w = strategic_world()
        observations = selected(w, 'business')['observations']
        for grant in observations:
            grant['received_at'] = None
        hidden = replace_selection(w, 'business', observations=observations)
        advance(w, 1)
        for grant in observations:
            grant['received_at'] = w.s['clock']
        received = replace_selection(w, 'business', observations=observations)
        advance(w, 7)
        ledger = w.s['r8_strategy']
        self.assertEqual(ledger['decisions'][0]['institutions']['business']['selection_id'], hidden)
        self.assertEqual(ledger['decisions'][6]['institutions']['business']['selection_id'], received)
        self.assertTrue(ledger['decisions'][6]['institutions']['business']['committed'])
        self.assertTrue(all(e['params']['start'] >= 26 for e in w.s['journal'] if e['op'] == 'commit_shift'))
        self.assertIn(hidden, ledger['selections'])


class RightsTests(unittest.TestCase):
    def test_denied_operation_does_not_reach_frontier(self):
        w = strategic_world()
        replace_selection(w, 'business', operations=[])
        advance(w, 2)
        first = w.s['r8_strategy']['decisions'][0]['institutions']['business']
        self.assertEqual(first['proposals'], [])
        self.assertEqual(first['withheld'][0]['reason'], 'operation_right_not_selected')
        self.assertNotIn('person-B', w.s['commitments'])
        self.assertFalse(w.s['econ3']['active_jobs'])

    def test_subject_scope_prevents_plan_for_uncontrolled_worker(self):
        w = strategic_world()
        scope = selected(w, 'business')['scope']
        scope['worker_ids'] = []
        replace_selection(w, 'business', scope=scope)
        advance(w, 1)
        self.assertNotIn('person-B', w.s['commitments'])
        self.assertEqual(w.s['r8_strategy']['decisions'][0]['institutions']['business']['withheld'][0]['reason'],
                         'decision_outside_selected_scope')

    def test_right_can_be_revoked_between_commitment_and_work(self):
        w = advance(strategic_world(), 1)
        old = selected(w, 'business')
        replace_selection(w, 'business', operations=[op for op in old['operations'] if op != 'start_job'])
        advance(w, 2)
        self.assertTrue(w.s['commitments']['person-B'])
        self.assertFalse(w.s['econ3']['active_jobs'])
        self.assertEqual(w.s['r8_strategy']['decisions'][1]['institutions']['business']['withheld'][0]['reason'],
                         'operation_right_not_selected')

    def test_site_scope_can_be_revoked_before_starting_work(self):
        w = advance(strategic_world(), 1)
        scope = selected(w, 'business')['scope']
        scope['site_ids'] = []
        replace_selection(w, 'business', scope=scope)
        advance(w, 2)
        self.assertFalse(w.s['econ3']['active_jobs'])
        self.assertEqual(w.s['r8_strategy']['decisions'][1]['institutions']['business']['withheld'][0]['reason'],
                         'decision_outside_selected_scope')

    def test_government_cannot_pay_with_assessment_right_only(self):
        w = strategic_world()
        replace_selection(w, 'government', operations=['assess_tax'])
        advance(w, 2)
        self.assertEqual(w.s['econ3']['tax_claims']['tax:0']['paid'], 0)
        self.assertEqual(w.s['cash']['farmer-b'], 100)

    def test_truth_revalidation_refuses_now_unbacked_work(self):
        w = advance(strategic_world(), 1)
        w.apply('physical-inventory-loss', 1, 'physical_loss', location='house-1', material='grain',
                quantity=240, cause_ref='test-loss', evidence_ref='test-count')
        advance(w, 2)
        self.assertFalse(w.s['econ3']['active_jobs'])
        self.assertEqual(w.s['econ3']['produced']['meal'], 0)
        request = w.s['r9']['requests']['irgs33:1:business:start_job']
        self.assertEqual(request['status'], 'unresolved')
        self.assertEqual(w.s['econ3']['stocks']['house-1']['grain'], 0)

    def test_selection_cannot_be_silently_edited(self):
        w = strategic_world()
        sid = w.s['r8_strategy']['institutions']['government']
        w.s['r8_strategy']['selections'][sid]['selection']['operations'] = []
        with self.assertRaises(InvalidEvent):
            advance(w, 1)

    def test_revoked_binding_cannot_be_silently_restored(self):
        w = strategic_world()
        old = w.s['r8_strategy']['institutions']['government']
        replace_selection(w, 'government', operations=[])
        w.s['r8_strategy']['institutions']['government'] = old
        with self.assertRaises(InvalidEvent):
            advance(w, 1)

    def test_selection_cannot_expose_entire_world(self):
        w = strategic_world()
        grants = selected(w, 'business')['observations']
        grants[0]['path'] = []
        with self.assertRaises(InvalidEvent):
            replace_selection(w, 'business', observations=grants)


class SustainedExecutionTests(unittest.TestCase):
    def assert_conserved(self, world):
        state, econ = world.s, world.s['econ3']
        self.assertEqual(sum(state['cash'].values()), state['cash_baseline'])
        self.assertEqual(len(state['actors']) + state['population']['residual'], state['population']['baseline'])
        for material, opening in econ['opening'].items():
            self.assertEqual(total(econ, material), opening + econ['produced'][material]
                             - econ['consumed'][material] - econ.get('losses', {}).get(material, 0))
        world._validate(state)

    def test_default_fourteen_day_resources_and_decisions(self):
        w = advance(strategic_world(), 14 * 6)
        self.assertEqual(w.s['econ3']['produced']['meal'], 42)
        self.assertEqual(w.s['econ3']['meals_delivered']['house-1'], 42)
        decisions = w.s['r8_strategy']['decisions']
        self.assertEqual(sum(len(d['committed']) for d in decisions), 77)
        self.assertTrue(all(set(d['institutions']) == {'business', 'household', 'government', 'military'} for d in decisions))
        self.assertTrue(all(d['selection_source_ref'] for review in decisions for d in review['institutions'].values()))
        self.assert_conserved(w)

    def test_save_resume_preserves_boundaries_and_exact_decisions(self):
        full = advance(strategic_world(), 2 * 6)
        split = advance(strategic_world(), 6)
        split = advance(type(split).load(split.save()), 2 * 6)
        self.assertEqual(full.save(), split.save())
        self.assert_conserved(split)


if __name__ == '__main__':
    unittest.main()
