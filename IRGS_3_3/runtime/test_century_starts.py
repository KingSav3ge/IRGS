"""All real Century of Conflict entries through existing Core owners; no user saves."""
import copy
import unittest

from campaign_library import initial_campaign
from core_world import CoreWorld
from historical_campaigns import historical_catalogue, historical_entry, _validate_snapshot
from historical_plans import campaign_plan_view, baseline_view
from scene_actions import execute_scene_action
from starting_selection import options_for_world, initialize_player
from temporal_registry import julian_day
from irgs_reference import InvalidEvent


def opening(entry_id):
    preview = historical_entry(entry_id)
    return initial_campaign('military', 'SYNTHETIC-'+entry_id,
        scenario_id='hundred-years-war', entry_id=entry_id,
        snapshot_sha256=preview['snapshot_sha256'])


class CenturyStartsTests(unittest.TestCase):
    def test_every_entry_has_its_own_exact_valid_snapshot_and_sources(self):
        entries=historical_catalogue()['entries']
        self.assertEqual(len(entries),37)
        hashes=set()
        for entry in entries:
            with self.subTest(entry=entry['id']):
                p=historical_entry(entry['id']); self.assertTrue(p['ready'])
                s=p['snapshot']; date=s['opening']['date']
                self.assertEqual(s['id'],entry['id'])
                self.assertEqual(date[:4],str(entry['year']))
                self.assertIsNone(s['opening']['time'])
                self.assertEqual(s['entity_registry_template']['as_of'],julian_day(*map(int,date.split('-'))))
                self.assertTrue(s['unknowns']); self.assertTrue(s['entry_guide']['source_ids'])
                hashes.add(p['snapshot_sha256'])
                for mutate in (lambda v:v['opening'].update(date='1415-08-11' if entry['year']!=1415 else '1415-08-12'),
                               lambda v:v['entity_registry_template'].update(as_of=0)):
                    bad=copy.deepcopy(s);mutate(bad)
                    with self.assertRaises(ValueError):_validate_snapshot(bad,entry)
        self.assertEqual(len(hashes),37)

    def test_dated_rosters_do_not_restore_dead_people_or_give_an_infant_adult_control(self):
        for entry,absent in [('hyw-1377','HYW-EDWARD-III'),('hyw-1419','HYW-JOHN-FEARLESS'),
                             ('hyw-1422','HYW-HENRY-V'),('hyw-1435','HYW-JOAN-ARC')]:
            self.assertNotIn(absent,opening(entry).s['actors'])
        opts=options_for_world(opening('hyw-1422'))
        infant=next(c for c in opts['characters'] if c['id']=='HYW-HENRY-VI')
        self.assertTrue(infant['exists']);self.assertFalse(infant['eligible'])
        late=options_for_world(opening('hyw-1453'))
        king=next(c for c in late['characters'] if c['id']=='HYW-HENRY-VI')
        self.assertTrue(king['exists']);self.assertFalse(king['eligible'])
        self.assertIn('1453 incapacity',king['eligibility_reason'])
        self.assertIn('Martin V',historical_entry('hyw-1417')['snapshot']['research_extension']['religious_context'])

    def test_every_entry_creates_an_independent_character_without_free_resources_or_news(self):
        for entry in historical_catalogue()['entries']:
            with self.subTest(entry=entry['id']):
                raw=opening(entry['id']); before=raw.save(); opts=options_for_world(raw)
                world=initialize_player(raw,{'kind':'new','name':'Independent traveller','species':'human',
                    'identity':{'nationality':'Scottish'},'career':{'arrangement':'independent','relationship_stage':'undecided'}},
                    selection_digest=opts['selection_digest'],request_ref='synthetic-reviewed-start')
                self.assertEqual(raw.save(),before)
                self.assertEqual(world.s['stocks'],{})
                self.assertEqual(len(world.s['player_actor_ids']),1)
                actor=world.s['player_actor_ids'][0]
                self.assertNotIn('national_allegiance',world.s['actors'][actor]['current'])
                self.assertFalse(world.s['historical_start']['automatic_future_history'])
                self.assertEqual(CoreWorld.load(world.save()).save(),world.save())
                self.assertEqual(world.s['historical_start']['entry_id'],entry['id'])

    def test_every_entry_supports_opt_in_local_play_conservation_retry_and_reload(self):
        for entry in historical_catalogue()['entries']:
            with self.subTest(entry=entry['id']):
                raw=opening(entry['id']);opts=options_for_world(raw)
                pack=opts['playable_openings'][0];self.assertTrue(pack['fictional'])
                world=initialize_player(raw,{'kind':'new','name':'Synthetic courier','species':'human','opening_id':pack['id']},
                    selection_digest=opts['selection_digest'],request_ref='synthetic-fictional-scene-consent')
                actor=world.s['player_actor_ids'][0];calendar=copy.deepcopy(world.s['campaign_time'])
                prefix='quay' if entry['year']==1415 else 'yard'
                for action in ['look-'+prefix,prefix+'-shortcut',prefix+'-passage','passage-desk','deliver-dispatch']:
                    result=execute_scene_action(world,'test:'+action,actor,{'kind':'scene_action','action_id':action},'reviewed:'+action)
                    self.assertEqual(result['status'],'completed_unsuccessfully' if action.endswith('-shortcut') else 'completed_successfully')
                self.assertEqual(world.s['stocks'][actor]['sealed_dispatch'],0)
                self.assertEqual(world.s['stocks']['clerk-tray']['sealed_dispatch'],1)
                self.assertEqual(world.s['elapsed_time']['seconds'],150)
                self.assertEqual(world.s['campaign_time'],calendar)
                before=world.save()
                with self.assertRaises(InvalidEvent):
                    execute_scene_action(world,'test:deliver-dispatch',actor,{'kind':'scene_action','action_id':'deliver-dispatch'},'reviewed:deliver-dispatch')
                self.assertEqual(world.save(),before)
                self.assertEqual(CoreWorld.load(world.save()).save(),before)

    def test_all_conditional_references_are_read_only_and_pinned(self):
        for entry in historical_catalogue()['entries']:
            with self.subTest(entry=entry['id']):
                raw=opening(entry['id']); opts=options_for_world(raw)
                world=initialize_player(raw,{'kind':'new','name':'Observer','species':'human'},selection_digest=opts['selection_digest'])
                before=world.save(); report=campaign_plan_view(world)
                self.assertFalse(report['execution_available'])
                self.assertFalse(report['installed_schedule'])
                self.assertEqual(world.save(),before)
                baseline=world.s['historical_planning']['baseline_snapshot']
                self.assertEqual(baseline['scope']['scenario_id'],'hundred-years-war')
                if entry['year']!=1415:self.assertEqual(baseline['scope']['entry_id'],entry['id'])
        self.assertEqual(len(baseline_view()['events']),3)


if __name__=='__main__':unittest.main()
