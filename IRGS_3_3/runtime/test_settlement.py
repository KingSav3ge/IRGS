"""Executable fictional contracts, not certification of all Rise T01–T37."""
import copy
import unittest
from core_world import CoreWorld
from irgs_reference import InvalidEvent
from settlement_setup import initialize, preview, templates
from settlement_runtime import execute, OPERATION, _advance
from r9_runtime import observe, frontier


def choices(**overrides):
    return dict(template_id='R00', founder_name='Ari', household_name='Ari household',
        settlement_name='Willow Camp', region_name='Greywater Reach', date_label='Spring, Year 1',
        company='solo', permission='seek', supplies='basic', **overrides)


class SettlementTests(unittest.TestCase):
    def world(self, **overrides):
        c = choices(); c.update(overrides)
        review = preview(c)
        return initialize(c, review['review_digest'], 'settlement-fixture')

    def act(self, w, action, request=None):
        return execute(w, request or f'action-{w.s["clock"]+1}', 'founder', action, 'explicit-fixture-request')

    def camp(self, w):
        if not w.s['grants']:
            self.act(w, 'request_grant'); self.act(w, 'accept_grant')
        self.act(w, 'walk_clearing'); self.act(w, 'found')

    def test_eight_families_remain_unqualified_and_setup_digest_fences_backtracking(self):
        entries = templates()['templates']
        self.assertEqual(len(entries), 9)
        self.assertEqual([e['id'] for e in entries if e['ready']], ['R00'])
        for entry in entries[1:]:
            c = choices(); c['template_id'] = entry['id']
            with self.assertRaises(ValueError): preview(c)
        c = choices(); review = preview(c); c['company'] = 'sibling'
        with self.assertRaises(ValueError): initialize(c, review['review_digest'], 'fixture')

    def test_configuration_axes_are_independent_and_population_stock_are_physical(self):
        for company, people in [('solo', 3), ('sibling', 4), ('two_households', 4)]:
            for permission in ('seek', 'held'):
                w = self.world(company=company, permission=permission, region_name='Another fictional reach', date_label='Autumn, Year 8')
                self.assertEqual(len(w.s['actors']), people)
                self.assertEqual(w.s['stocks']['founder-home'], {'grain': 12, 'timber': 6, 'axe': 1})
                self.assertEqual(bool(w.s['grants']), permission == 'held')
                self.assertEqual(w.s['player_actor_ids'], ['founder'])
                self.assertEqual(w.s['journal'], [])

    def test_no_permission_means_atomic_rejection_and_no_free_goods_from_grant(self):
        w = self.world(); initial = copy.deepcopy(w.s['stocks'])
        self.act(w, 'request_grant')
        self.assertEqual(w.s['grants']['founding']['status'], 'offered')
        self.assertEqual(w.s['stocks'], initial)
        self.act(w, 'walk_clearing'); before = w.save()
        with self.assertRaises(InvalidEvent): self.act(w, 'found')
        self.assertEqual(w.save(), before)
        self.act(w, 'walk_commons'); self.act(w, 'accept_grant'); self.camp(w)
        self.assertEqual(w.s['stocks'], initial)
        self.assertEqual(w.s['land_claims']['clearing']['existing_use'], 'seasonal footpath')

    def test_reserved_inputs_partial_work_completion_and_new_identity_do_not_duplicate(self):
        w = self.world(permission='held'); self.camp(w); self.act(w, 'build')
        self.assertEqual(w.s['stocks']['founder-home']['timber'], 6)
        self.act(w, 'wait_hour')  # Stops first at Oren's repair boundary.
        self.assertEqual(w.s['projects']['shelter']['worked'], 1500)
        self.assertNotIn('shelter', w.s['assets'])
        self.act(w, 'wait_hour')
        self.assertEqual(w.s['projects']['shelter']['status'], 'complete')
        self.assertEqual(w.s['stocks']['founder-home']['timber'], 3)
        before = w.save()
        with self.assertRaises(InvalidEvent): self.act(w, 'build', 'new-physical-project-attempt')
        self.assertEqual(w.save(), before)
        w2 = CoreWorld.load(w.save()); self.assertEqual(w2.s, w.s)

    def test_pause_retains_progress_and_prevents_double_booking(self):
        w = self.world(permission='held'); self.camp(w); self.act(w, 'build'); self.act(w, 'wait_hour')
        before = w.save()
        with self.assertRaises(InvalidEvent): self.act(w, 'walk_commons')
        self.assertEqual(w.save(), before)
        self.act(w, 'pause'); self.act(w, 'wait_hour')
        self.assertEqual(w.s['projects']['shelter']['worked'], 1500)
        self.act(w, 'resume'); self.act(w, 'wait_hour')
        self.assertEqual(w.s['projects']['shelter']['worked'], 3600)

    def test_delegated_and_autonomous_work_share_inputs_while_founder_is_elsewhere(self):
        w = self.world(company='sibling', permission='held'); self.camp(w); self.act(w, 'delegate')
        self.act(w, 'walk_commons')
        for _ in range(3): self.act(w, 'wait_hour')
        self.assertEqual(w.s['projects']['shelter']['status'], 'complete')
        self.assertEqual(w.s['projects']['oren-repair']['status'], 'complete')
        self.assertEqual(w.s['stocks']['founder-home']['timber'], 3)
        self.assertEqual(w.s['stocks']['oren-home']['timber'], 2)
        self.assertEqual(w.s['actors']['rowan']['current']['location'], 'clearing')
        self.assertNotIn('shelter project is complete', w.s['settlement_receipts']['founder'][f'action-{w.s["clock"]}:inspection']['text'])

    def test_migration_preserves_existing_people_goods_and_delays_membership_until_arrival(self):
        w = self.world(permission='held'); self.camp(w); self.act(w, 'walk_commons'); self.act(w, 'wait_hour')
        stocks = copy.deepcopy(w.s['stocks']); people = set(w.s['actors'])
        self.act(w, 'invite')
        self.assertEqual(w.s['migrations']['oren-move']['status'], 'agreed')
        self.assertEqual(w.s['settlements']['camp']['households'], ['founder-home'])
        self.act(w, 'arrange_departure')
        self.assertEqual(w.s['migrations']['oren-move']['status'], 'transit')
        self.assertEqual(w.s['households']['oren-home']['settlement'], None)
        self.act(w, 'wait_hour')
        self.assertEqual(w.s['migrations']['oren-move']['status'], 'arrived')
        self.assertEqual(w.s['settlements']['camp']['households'], ['founder-home', 'oren-home'])
        self.assertEqual(w.s['stocks'], stocks); self.assertEqual(set(w.s['actors']), people)
        self.assertEqual(w.s['player_actor_ids'], ['founder'])

    def test_provision_consumes_once_retains_seed_and_never_erases_people(self):
        w = self.world(company='sibling')
        for _ in range(44): self.act(w, 'wait_hour')
        before = copy.deepcopy(w.s)
        self.assertEqual(len(w.s['actors']), 4)
        self.assertGreaterEqual(w.s['stocks']['founder-home']['grain'], 2)
        self.assertTrue(any(a['deficit'] > 0 for a in w.s['provision']['assessments'].values()))
        for material, opening in w.s['opening_stock'].items():
            consumed = sum(f['quantity'] for f in w.s['material_flows'].values() if f['material'] == material)
            self.assertEqual(sum(q.get(material, 0) for q in w.s['stocks'].values()), opening-consumed)
        # A malformed quantity or unsupported flow cannot legalize stock drift.
        corrupt = copy.deepcopy(before); corrupt['material_flows']['forged'] = {'kind': 'consumption', 'quantity': -1, 'material': 'grain'}
        with self.assertRaises((AssertionError, KeyError)): CoreWorld(state=corrupt)

    def test_coarse_and_fine_advances_produce_equal_consequential_state(self):
        a = self.world(permission='held'); self.camp(a); self.act(a, 'build')
        b = CoreWorld.load(a.save())
        target = 21600
        while a.s['elapsed_time']['seconds'] < target: _advance(a.s, target-a.s['elapsed_time']['seconds'])
        while b.s['elapsed_time']['seconds'] < target: _advance(b.s, min(60, target-b.s['elapsed_time']['seconds']))
        a._validate(a.s); b._validate(b.s)
        self.assertEqual(a.s, b.s)

    def test_revoked_permission_holds_work_without_rewriting_history(self):
        w = self.world(permission='held'); self.camp(w); self.act(w, 'build')
        w.s['grants']['founding']['active'] = False
        self.act(w, 'wait_hour')
        self.assertEqual(w.s['projects']['shelter']['status'], 'held')
        self.assertEqual(w.s['projects']['shelter']['worked'], 0)
        self.assertEqual(w.s['stocks']['founder-home']['timber'], 6)

    def test_missing_construction_model_holds_only_its_dependent_action(self):
        w = self.world(permission='held'); self.camp(w)
        del w.s['settlement_model']['shelter_timber']
        before = w.save()
        with self.assertRaisesRegex(InvalidEvent, 'No effects or elapsed work'): self.act(w, 'build')
        self.assertEqual(w.save(), before)
        self.act(w, 'wait_hour')
        self.assertEqual(w.s['projects']['oren-repair']['status'], 'complete')

    def test_control_scope_and_exact_core_replay(self):
        w = self.world(); before = w.save()
        with self.assertRaises(InvalidEvent): execute(w, 'not-controlled', 'oren', 'wait_hour', 'fixture')
        self.assertEqual(w.save(), before)
        self.act(w, 'request_grant', 'grant-request')
        event = copy.deepcopy(w.s['journal'][-1]); saved = w.save()
        self.assertFalse(w.apply(event['id'], event['at'], event['op'], **event['params']))
        self.assertEqual(w.save(), saved)
        event['params']['action'] = 'accept_grant'
        with self.assertRaises(InvalidEvent): w.apply(event['id'], event['at'], event['op'], **event['params'])

    def test_actual_dependency_observation_and_conflicts_never_choose_by_identity(self):
        w = self.world(permission='held'); self.camp(w)
        def event(key):
            return {'id': key, 'at': w.s['clock']+1, 'op': OPERATION,
                'params': {'campaign_id': w.s['campaign_id'], 'actor': 'founder', 'action': 'build',
                           'request_id': key, 'source_ref': 'fixture', 'instruction_ref': 'fixture'}}
        certificate = observe(w.s, event('one'))
        paths = ' '.join('/'.join(p) for p in certificate['reads'])
        self.assertIn('grants/founding', paths); self.assertIn('stocks/founder-home', paths)
        self.assertIn('projects', paths); self.assertIn('actors/founder', paths)
        for ids in [('one', 'two'), ('two', 'one')]:
            clone = CoreWorld.load(w.save()); result = frontier(clone, [event(k) for k in ids])
            self.assertEqual(set(result['deferred']), set(ids)); self.assertEqual(result['committed'], [])
            self.assertNotIn('shelter', clone.s['projects'])

    def test_established_core_location_record_remains_usable_by_settlement_actions(self):
        w = self.world(permission='held')
        for key, operation, parameters in [
            ('where', 'record_evidence', {'evidence_id': 'where', 'subject': 'founder',
                'status': 'established', 'assertion': 'Founder observed at commons.'}),
            ('heard', 'receive_evidence', {'evidence_id': 'where', 'recipient': 'founder'}),
            ('confirmed', 'confirm_character_field', {'subject': 'founder', 'field': 'location',
                'value': 'commons', 'evidence_id': 'where', 'authority_ref': 'synthetic observation',
                'instruction_ref': 'explicit synthetic confirmation'})]:
            w.apply(key, w.s['clock']+1, operation, campaign_id=w.s['campaign_id'],
                source_ref='synthetic interoperability test', **parameters)
        self.assertIsInstance(w.s['actors']['founder']['current']['location'], dict)
        event = {'id': 'canonical-location-walk', 'at': w.s['clock']+1, 'op': OPERATION,
            'params': {'campaign_id': w.s['campaign_id'], 'actor': 'founder', 'action': 'walk_clearing',
                'request_id': 'canonical-location-walk', 'instruction_ref': 'explicit synthetic walk',
                'source_ref': 'synthetic interoperability test'}}
        self.assertIn(('actors', 'founder', 'current', 'location', 'value'), observe(w.s, event)['reads'])
        self.act(w, 'walk_clearing')
        self.assertEqual(w.s['actors']['founder']['current']['location'], 'clearing')
        self.assertEqual(w.s['elapsed_time']['seconds'], 300)
        self.assertIn('where', w.s['evidence'])


if __name__ == '__main__': unittest.main()
