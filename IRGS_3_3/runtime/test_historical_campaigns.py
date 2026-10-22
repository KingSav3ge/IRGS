"""Historical setup selection does not execute history or migrate AST."""
import copy
import hashlib
import unittest

from campaign_library import initial_campaign, catalog, presentation_binding
from core_world import CoreWorld
from historical_campaigns import (ROOT, historical_catalogue, historical_entry,
                                 prepare_opening, _validate_snapshot, apply_opening)
from r9_runtime import frontier
from irgs_reference import InvalidEvent


def historical_world(campaign_id='HYW-TEST'):
    preview = historical_entry('hyw-1415')
    return initial_campaign('military', campaign_id, scenario_id='hundred-years-war',
                            entry_id='hyw-1415', snapshot_sha256=preview['snapshot_sha256'])


class HistoricalCatalogueTests(unittest.TestCase):
    def test_developed_entry_requires_detailed_traceable_player_briefing(self):
        preview = historical_entry('hyw-1415')
        for mutate in (
            lambda s: s.pop('entry_guide'),
            lambda s: s['entry_guide'].update(summary=[]),
            lambda s: s['entry_guide'].update(practical_pressures=['']),
            lambda s: s['entry_guide'].update(not_yet_established=[]),
            lambda s: s['entry_guide'].update(source_ids=['unverified-reference']),
            lambda s: s['entry_guide'].update(future_rule='')):
            changed = copy.deepcopy(preview['snapshot'])
            mutate(changed)
            with self.assertRaises(ValueError):
                _validate_snapshot(changed, preview['entry'])

    def test_all_supplied_dates_and_featured_starts_are_retained(self):
        data = historical_catalogue()
        self.assertEqual(len(data['entries']), 37)
        self.assertEqual(len({e['id'] for e in data['entries']}), 37)
        self.assertEqual(len({e['year'] for e in data['entries']}), 37)
        self.assertEqual({p['id']: sum(e['period_id'] == p['id'] for e in data['entries']) for p in data['periods']},
                         {'edwardian': 12, 'caroline': 14, 'lancastrian': 11})
        self.assertEqual(data['featured_years'], [1337,1360,1369,1389,1415,1422,1435,1444,1449,1453])
        self.assertEqual(len(catalog()['campaign_profiles']), 7)
        self.assertEqual(len(catalog()['content_libraries']), 8)

    def test_preview_hash_identifies_exact_source_bytes(self):
        preview = historical_entry('hyw-1415')
        self.assertTrue(preview['ready'])
        raw = (ROOT / 'data/hyw_1415_opening.json').read_bytes()
        self.assertEqual(preview['snapshot_sha256'], hashlib.sha256(raw).hexdigest())
        self.assertEqual(preview['snapshot']['opening']['date'], '1415-08-11')
        self.assertEqual(preview['snapshot']['opening']['calendar'], 'julian')
        proposed = historical_entry('hyw-1360')
        self.assertTrue(proposed['ready'])
        self.assertEqual(proposed['snapshot']['opening']['date'],'1360-12-15')
        self.assertNotEqual(proposed['snapshot_sha256'],preview['snapshot_sha256'])

    def test_invalid_scope_identity_date_and_sources_cannot_be_developed_openings(self):
        preview = historical_entry('hyw-1415')
        for mutate in (
            lambda s: s.update(id='hyw-1360'),
            lambda s: s.update(scenario_id='another-setting'),
            lambda s: s.update(status='proposed'),
            lambda s: s['opening'].update(date='1415-10-25'),
            lambda s: s['opening'].update(calendar='gregorian'),
            lambda s: s['actors'][0].update(source_ids=['unknown-source']),
            lambda s: s['domains']['military'][0].update(effective_not_after='1416-01-01')):
            changed = copy.deepcopy(preview['snapshot'])
            mutate(changed)
            with self.subTest(snapshot=changed['id']), self.assertRaises(ValueError):
                _validate_snapshot(changed, preview['entry'])

    def test_unready_unknown_partial_and_stale_selections_fail(self):
        for profile, scenario, entry, sha in (
            ('ast','hundred-years-war','hyw-1415','0'*64),
            ('military','other-setting','hyw-1415','0'*64),
            ('military','hundred-years-war','../outside','0'*64),
            ('military','hundred-years-war','hyw-1360','0'*64),
            ('military','hundred-years-war','hyw-1415','0'*64),
            ('military','hundred-years-war','hyw-1415',None),
            ('military',None,'hyw-1415','0'*64)):
            with self.subTest(profile=profile, entry=entry, hash=sha), self.assertRaises(ValueError):
                prepare_opening(profile, scenario, entry, sha)


class HistoricalInitializationTests(unittest.TestCase):
    def test_initialization_rejects_existing_unresolved_intent_at_sequence_zero(self):
        world = initial_campaign('military', 'EXISTING')
        events = [{'id': key, 'at': 0, 'op': 'record_design', 'params': {
            'campaign_id': 'EXISTING', 'design_id': 'same-design', 'name': name,
            'source_ref': 'fixture-source'}} for key, name in (('a', 'First proposal'), ('b', 'Second proposal'))]
        result = frontier(world, events)
        self.assertEqual(len(result['deferred']), 2)
        self.assertEqual(world.s['clock'], 0)
        self.assertEqual(world.s['journal'], [])
        preview = historical_entry('hyw-1415')
        selection = prepare_opening('military', 'hundred-years-war', 'hyw-1415', preview['snapshot_sha256'])
        before = world.save()
        with self.assertRaises(ValueError):
            apply_opening(world.s, selection)
        self.assertEqual(world.save(), before)

    def test_default_ast_creation_is_unchanged(self):
        ordinary = initial_campaign('ast', 'AST-EXISTING')
        explicit = initial_campaign('ast', 'AST-EXISTING', scenario_id=None, entry_id=None, snapshot_sha256=None)
        self.assertEqual(ordinary.save(), explicit.save())
        self.assertNotIn('historical_start', ordinary.s)
        self.assertEqual(ordinary.s['campaign_time']['day'], 2)
        self.assertEqual(ordinary.s['actors']['AST-04']['name'], 'Abel')
        self.assertEqual(ordinary.s['player_actor_ids'], ['AST-01'])

    def test_opening_is_a_sourced_setup_with_no_player_or_scheduled_history(self):
        w = historical_world()
        self.assertEqual(w.s['binding']['campaign_profile'], 'military')
        self.assertEqual(w.s['binding']['library_ids'], ['shared', 'military'])
        self.assertEqual(w.s['binding']['scenario_id'], 'hundred-years-war')
        self.assertEqual(w.s['binding']['entry_id'], 'hyw-1415')
        self.assertEqual(len(w.s['actors']), 5)
        self.assertTrue(all(a['source_ids'] and a['historical_reference_only'] and a['current'] == {}
                            for a in w.s['actors'].values()))
        self.assertEqual(w.s['clock'], 0)
        self.assertEqual(w.s['campaign_time']['day'], 0)
        for field in ('player_actor_ids','stocks','opening_stock','capacities','activities','knowledge',
                      'orders','journal','processed','pending','player_actions'):
            self.assertFalse(w.s[field], field)
        start = w.s['historical_start']
        self.assertFalse(start['automatic_future_history'])
        self.assertFalse(start['automatic_narration'])
        self.assertFalse(start['automatic_consolidation'])
        self.assertFalse(start['clock_origin']['elapsed_time_binding'])
        self.assertEqual(start['history_origin']['status'], 'unbound')
        self.assertTrue(start['history_origin']['partial_opening_year'])

    def test_opening_survives_save_load_and_scene_changes(self):
        w = historical_world()
        before = copy.deepcopy(w.s['historical_start'])
        loaded = CoreWorld.load(w.save())
        self.assertEqual(loaded.save(), w.save())
        loaded.apply('scene', 1, 'set_scene', campaign_id='HYW-TEST', source_ref='explicit-scene-source',
                     instruction_ref='explicit-host-request', day=1, time=None,
                     precision='unresolved', description='A separately declared scene')
        self.assertEqual(loaded.s['historical_start'], before)
        self.assertEqual(loaded.s['historical_start']['date'], '1415-08-11')
        self.assertEqual(presentation_binding(loaded.s)['snapshot_sha256'], before['snapshot_sha256'])

    def test_snapshot_copies_and_campaign_scopes_are_independent(self):
        raw = (ROOT / 'data/hyw_1415_opening.json').read_bytes()
        first, second = historical_world('FIRST'), historical_world('SECOND')
        first.s['historical_start']['snapshot']['unknowns'].append('A local alteration')
        first.s['actors']['HYW-HENRY-V']['current']['test'] = 'local'
        self.assertNotEqual(first.s['historical_start']['snapshot'], second.s['historical_start']['snapshot'])
        self.assertEqual(second.s['actors']['HYW-HENRY-V']['current'], {})
        self.assertEqual((ROOT / 'data/hyw_1415_opening.json').read_bytes(), raw)
        self.assertNotIn('A local alteration', historical_entry('hyw-1415')['snapshot']['unknowns'])
        with self.assertRaises(InvalidEvent):
            second.apply('cross', 1, 'record_design', campaign_id='FIRST', source_ref='test',
                         design_id='bad', name='A cross-campaign design')


if __name__ == '__main__':
    unittest.main()
