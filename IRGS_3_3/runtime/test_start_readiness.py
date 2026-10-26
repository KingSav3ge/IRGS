"""Actual new-world historical starts and existing Core observation effects."""
from dataclasses import replace
from concurrent.futures import ThreadPoolExecutor
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from campaign_library import initial_campaign
from core_world import CoreWorld
from historical_campaigns import historical_entry
from runtime_contracts import AcceptedIntent, WorldScope
from shared_runtime import SharedActionUnavailable, capabilities, execute_intent, prepare_intent
from solo_provider import CapabilityUnavailable
from starting_selection import initialize_player, options_for_world
import start_readiness as api
from test_solo_provider import AtomicTestHost

HENRY = 'HYW-HENRY-V'
JOHN = 'HYW-JOHN-BEDFORD'
OPENING = 'henry-1415-embarkation-v1'


def raw(entry='hyw-1415', campaign='synthetic-start-readiness'):
    preview = historical_entry(entry)
    return initial_campaign('military', campaign, scenario_id='hundred-years-war',
        entry_id=entry, snapshot_sha256=preview['snapshot_sha256'])


class StartReadinessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.world = raw(); self.counter = 0
        for target in ('solo_provider.CapabilityBroker.dispatch',
                       'openai_proposals.OpenAIProposalTransport.__call__', 'socket.socket.connect'):
            guard = patch(target, side_effect=AssertionError('No network/provider in start qualification'))
            guard.start(); self.addCleanup(guard.stop)

    def create(self, character=None):
        self.character = character or {'kind':'existing','actor_id':HENRY,'opening_id':OPENING}
        options = options_for_world(self.world)
        self.world = initialize_player(self.world, self.character, selection_digest=options['selection_digest'],
                                       request_ref='explicit reviewed synthetic start')
        self.actor = self.world.s['player_actor_ids'][0]
        self.host = AtomicTestHost(self.temp.name, self.world)

    def view(self, actor=None):
        return api.actor_view(self.world, actor or self.actor, branch_id='branch-1', restore_id=self.host.restore_id)

    def scope(self):
        return WorldScope(self.world.s['campaign_id'],'branch-1',self.host.restore_id,self.world.checksum())

    def request(self, text='I observe the embarkation setting without issuing an order.'):
        self.counter += 1
        cap = next(c for c in capabilities(self.world,self.actor) if c.operation_id == 'execute_player_scene_action')
        return prepare_intent(self.world, request_id='observation-'+str(self.counter), actor_id=self.actor,
            intention=text, capability_id=cap.capability_id, branch_id='branch-1', restore_id=self.host.restore_id)

    def submit(self, request, **overrides):
        args = dict(current_scope=self.scope(),persist=self.host.persist,explicitly_accepted=True)
        args.update(overrides)
        return execute_intent(self.world,request,**args)

    def test_john_is_eligible_but_his_playable_mode_stays_held_without_personal_context(self):
        before = self.world.save()
        review = api.review_start(self.world, {'kind':'existing','actor_id':JOHN})
        self.assertTrue(review['character_eligible'])
        self.assertEqual(review['reference_status'],'verified_dated_reference')
        self.assertEqual(review['selected_mode']['status'],'declaration_only')
        self.assertEqual(review['playable_context']['status'],'held')
        self.assertEqual(review['presentation_opening']['status'],'presentation_only')
        self.assertFalse(review['presentation_opening']['grants_capabilities'])
        self.assertEqual(self.world.save(),before)

    def test_existing_henry_requires_a_separate_explicit_sourced_opening(self):
        default = api.review_start(self.world, {'kind':'existing','actor_id':HENRY})
        selected = api.review_start(self.world, {'kind':'existing','actor_id':HENRY,'opening_id':OPENING})
        self.assertEqual(default['selected_mode']['status'],'declaration_only')
        self.assertEqual(selected['selected_mode']['status'],'supported_slice')
        options = options_for_world(self.world)
        self.assertEqual(options['existing_character_openings'][0]['actor_id'],HENRY)
        self.assertEqual(options['existing_character_openings'][0]['review']['location_precision'],'embarkation_region_only')
        self.assertNotIn(OPENING,[r['id'] for r in options['playable_openings']])

    def test_new_authored_and_declaration_modes_are_distinct_from_existing_person(self):
        character = {'kind':'new','name':'Synthetic courier','species':'Human'}
        self.assertEqual(api.review_start(self.world,character)['selected_mode']['status'],'declaration_only')
        character['opening_id'] = 'quay-delivery-v1'
        self.assertEqual(api.review_start(self.world,character)['selected_mode']['status'],'supported_slice')
        character['species'] = 'elf'
        self.assertEqual(api.review_start(self.world,character)['selected_mode']['status'],'held')
        character.update(kind='existing',actor_id=JOHN)
        self.assertEqual(api.review_start(self.world,character)['selected_mode']['status'],'held')

    def test_precreation_contract_does_not_probe_hidden_resources_or_choose_a_winning_menu(self):
        character = {'kind':'existing','actor_id':HENRY,'opening_id':OPENING}
        before = api.review_start(self.world,character)
        self.world.s['actors'][JOHN]['current']['location'] = 'PRIVATE_SITE'
        self.world.s['private_fixture'] = {'stocks':123,'authority':'PRIVATE','weather':'PRIVATE'}
        self.assertEqual(api.review_start(self.world,character),before)
        self.assertNotIn('PRIVATE',json.dumps(before))

    def test_sourced_start_initializes_only_reviewed_personal_context_and_calendar(self):
        self.create(); current = self.world.s['actors'][HENRY]['current']
        self.assertEqual(set(current),{'location'})
        self.assertEqual(current['location']['value'],'portchester-solent-embarkation')
        self.assertFalse(self.world.s['stocks']); self.assertFalse(self.world.s['orders'])
        self.assertFalse(self.world.s['starting_control']['institutional_mandate_granted'])
        self.assertNotIn('authored_opening',self.world.s['gameplay_started'])
        known = self.world.s['knowledge'][HENRY]
        self.assertEqual(set(known),{'setup:scene-map','setup:scene-location','setup:civil-date'})
        self.assertFalse(self.world.s['knowledge'].get(JOHN))
        self.assertNotIn('Harfleur',json.dumps(self.view()['received_context']))

    def test_first_explicit_core_attempt_delivers_observation_and_actual_elapsed_without_free_stock(self):
        self.create(); before = copy.deepcopy(self.world.s['campaign_time'])
        known = len(self.world.s['knowledge'][HENRY]); request = self.request()
        result = self.submit(request)
        self.assertEqual(result['status'],'completed_successfully')
        self.assertEqual(result['intention'],request.intention)
        self.assertIn('Shipping is gathered',result['receipt']['exact_text'])
        self.assertEqual(result['receipt']['elapsed_seconds'],20)
        self.assertEqual(self.world.s['elapsed_time']['seconds'],20)
        self.assertEqual(len(self.world.s['knowledge'][HENRY]),known+1)
        self.assertEqual(self.world.s['campaign_time'],before)
        self.assertEqual(self.host.load().save(),self.world.save())
        self.assertFalse(self.world.s['stocks'])

    def test_plain_existing_selection_never_silently_receives_the_optional_scene(self):
        self.create({'kind':'existing','actor_id':HENRY})
        self.assertNotIn('scene_rules',self.world.s)
        self.assertEqual(self.view()['current_mode'],'declaration_only')
        self.assertEqual(set(self.world.s['knowledge'][HENRY]),{'setup:civil-date'})

    def test_civil_date_is_sourced_received_day_precision_separate_from_other_axes(self):
        self.create(); civil = self.view()['civil_time']
        self.assertEqual(civil['date'],'1415-08-11'); self.assertEqual(civil['calendar'],'julian')
        self.assertEqual(civil['precision'],'day'); self.assertEqual(civil['ordinal'],2238109)
        self.assertIsNone(civil['time']); self.assertIsNone(civil['opening_hour'])
        self.assertFalse(civil['elapsed_calendar_binding']); self.assertFalse(civil['current_calendar_binding'])
        self.assertEqual(self.world.s['campaign_time']['day'],0)
        self.assertGreater(self.world.s['clock'],0)
        self.assertEqual(self.world.s['elapsed_time']['seconds'],0)

    def test_unknown_civil_date_in_generic_profile_remains_unknown(self):
        self.world = initial_campaign('fantasy','generic-unknown-time')
        self.create({'kind':'new','name':'Synthetic traveller','species':'human'})
        self.assertIsNone(self.view()['civil_time'])
        self.assertNotIn('civil',self.world.s['campaign_time'])
        self.assertEqual(self.view()['current_mode'],'declaration_only')

    def test_sourced_calendar_does_not_replace_later_exact_own_background_testimony(self):
        self.create({'kind':'new','name':'Synthetic reader','species':'human','background':'  My own exact account.  '})
        known=self.world.s['knowledge'][self.actor]
        self.assertLess(known['setup:civil-date']['received_at'],known['setup:background']['received_at'])
        self.assertEqual(self.world.s['evidence']['setup:background']['assertion'],'  My own exact account.  ')
        self.assertEqual(self.world.s['evidence']['setup:background']['status'],'testimony')

    def test_failed_persistence_cannot_publish_observation_or_elapsed(self):
        self.create(); request = self.request(); before = self.world.save(); disk = self.host.path.read_bytes()
        def fail(*args): raise OSError('synthetic persistence failure')
        with self.assertRaises(OSError): self.submit(request,persist=fail)
        self.assertEqual(self.world.save(),before); self.assertEqual(self.host.path.read_bytes(),disk)

    def test_incompatible_existing_person_and_fictional_openings_fail_atomically(self):
        options = options_for_world(self.world); before = self.world.save()
        for actor, opening in ((JOHN,OPENING),(HENRY,'quay-delivery-v1'),('missing-person',OPENING)):
            with self.assertRaises(ValueError):
                initialize_player(self.world,{'kind':'existing','actor_id':actor,'opening_id':opening},
                                  selection_digest=options['selection_digest'])
            self.assertEqual(self.world.save(),before)

    def test_other_snapshot_cannot_select_henrys_1415_context(self):
        self.world = raw('hyw-1417')
        options = options_for_world(self.world)
        self.assertEqual(options['existing_character_openings'],[])
        before = self.world.save()
        with self.assertRaises(ValueError):
            initialize_player(self.world,{'kind':'existing','actor_id':HENRY,'opening_id':OPENING},
                              selection_digest=options['selection_digest'])
        self.assertEqual(self.world.save(),before)

    def test_changed_opening_content_invalidates_review_without_mutating_source_world(self):
        pack = json.loads(api.PACK.read_bytes()); path = Path(self.temp.name)/'changed-opening.json'
        path.write_text(json.dumps(pack)); before = self.world.save()
        with patch.object(api,'PACK',path):
            options = options_for_world(self.world)
            pack['actions']['observe-embarkation']['duration_seconds'] = 21
            path.write_text(json.dumps(pack))
            with self.assertRaises(ValueError):
                initialize_player(self.world,{'kind':'existing','actor_id':HENRY,'opening_id':OPENING},
                                  selection_digest=options['selection_digest'])
        self.assertEqual(self.world.save(),before)

    def test_content_change_between_review_check_and_installation_is_refused(self):
        pack = json.loads(api.PACK.read_bytes()); path = Path(self.temp.name)/'racing-opening.json'
        path.write_text(json.dumps(pack)); original = api.initialize_context; before = self.world.save()
        def change_after_review(*args):
            result = original(*args)
            pack['map_text'] += ' Changed unreviewed context.'
            path.write_text(json.dumps(pack))
            return result
        with patch.object(api,'PACK',path), patch.object(api,'initialize_context',side_effect=change_after_review):
            options = options_for_world(self.world)
            with self.assertRaisesRegex(ValueError,'changed after review'):
                initialize_player(self.world,{'kind':'existing','actor_id':HENRY,'opening_id':OPENING},
                                  selection_digest=options['selection_digest'])
        self.assertEqual(self.world.save(),before)

    def test_save_load_and_read_do_not_reload_templates_or_reapply_context(self):
        from shared_runtime import actor_view
        self.create(); self.submit(self.request()); before = self.world.save()
        view = self.view()
        with patch.object(api,'PACK',Path('/unavailable-historical-pack.json')), \
                patch('historical_campaigns.historical_entry',side_effect=AssertionError('No template read')):
            self.world = CoreWorld.load(before)
            self.assertEqual(self.view(),view)
            self.assertEqual(actor_view(self.world,self.actor,branch_id='branch-1',restore_id=self.host.restore_id)
                             ['start_context'],view)
        self.assertEqual(self.world.save(),before)

    def test_diverged_template_and_elapsed_do_not_reset_received_initial_date_or_location(self):
        self.create(); civil = self.view()['civil_time']
        self.world.s['historical_start']['opening']['date'] = 'PRIVATE_UNRECEIVED_DATE'
        self.world.s['historical_start']['snapshot']['briefing'] = 'PRIVATE_CHANGED_TEMPLATE'
        self.host.install(self.world)
        self.submit(self.request())
        self.assertEqual(self.view()['civil_time'],civil)
        self.assertNotIn('PRIVATE',json.dumps(self.view()))
        self.assertEqual(self.world.s['elapsed_time']['seconds'],20)

    def test_unreceived_calendar_and_context_are_not_recovered_from_template_or_review(self):
        self.create()
        del self.world.s['knowledge'][HENRY]['setup:civil-date']
        view = self.view()
        self.assertIsNone(view['civil_time'])
        self.assertNotIn('1415-08-11',json.dumps(view))
        self.assertNotIn('known_time_at_creation',view['selected_start'])
        del self.world.s['knowledge'][HENRY]['setup:scene-map']
        self.assertEqual(self.view()['current_mode'],'declaration_only')
        self.assertNotIn('setup:scene-map',[r['record_id'] for r in self.view()['received_context']])

    def test_foreign_actor_cannot_receive_henrys_start_or_capabilities(self):
        self.create(); before = self.world.save()
        with self.assertRaises(ValueError): self.view(JOHN)
        with self.assertRaises(SharedActionUnavailable):
            prepare_intent(self.world,request_id='foreign',actor_id=JOHN,intention='I look.',
                capability_id='guessed',branch_id='branch-1',restore_id=self.host.restore_id)
        self.assertEqual(self.world.save(),before)

    def test_private_results_and_hidden_world_fields_are_absent_from_actor_contract(self):
        self.create(); self.world.s['hidden_fixture'] = {'sentinel':'PRIVATE_WORLD','stocks':100}
        raw_view = json.dumps(self.view())
        for forbidden in ('PRIVATE_WORLD','state_digest','params_digest','rule_digest','dependencies',
                          '"snapshot"','"stocks"','"orders"','"r9"','"entity_registry"'):
            self.assertNotIn(forbidden,raw_view)
        before = self.world.save(); detached = self.view(); detached['selected_start']['selected_mode']['status']='changed'
        self.assertEqual(self.world.save(),before)
        self.assertEqual(self.view()['selected_start']['selected_mode']['status'],'supported_slice')

    def test_exact_json_pending_request_restart_and_lost_ack_replay_once(self):
        self.create(); request = self.request('Exact words.\nI give no order.')
        pending = Path(self.temp.name)/'pending.json'; pending.write_text(request.to_json())
        before = self.world.save()
        def lost(scope,save,receipt):
            self.host.persist(scope,save,receipt); raise OSError('synthetic lost acknowledgment')
        with self.assertRaises(OSError): self.submit(request,persist=lost)
        self.assertEqual(self.world.save(),before)
        self.world = self.host.load(); saved = self.world.save(); writes = self.host.writes
        result = self.submit(AcceptedIntent.from_json(pending.read_text()))
        self.assertEqual(result,json.loads(self.host.path.read_text())['receipt'])
        self.assertEqual(self.world.save(),saved); self.assertEqual(self.host.writes,writes)
        self.assertEqual(self.world.s['elapsed_time']['seconds'],20)

    def test_concurrent_acceptance_commits_one_observation_and_elapsed_span(self):
        self.create(); request = self.request(); save, scope = self.world.save(), self.scope()
        def submit(_):
            try:
                return execute_intent(CoreWorld.load(save),request,current_scope=scope,
                                      persist=self.host.persist,explicitly_accepted=True)
            except CapabilityUnavailable as error: return error.code
        with ThreadPoolExecutor(2) as pool: results = list(pool.map(submit,range(2)))
        self.assertEqual(sum(isinstance(r,dict) for r in results),1)
        self.assertEqual(self.host.load().s['elapsed_time']['seconds'],20)

    def test_restore_and_branch_fences_reject_discarded_future_without_reinitialization(self):
        self.create(); save = self.world.save(); request = self.request(); self.submit(request)
        self.world = CoreWorld.load(save); self.host.restore_id = 'restore-2'; self.host.install(self.world)
        with self.assertRaises(SharedActionUnavailable) as caught: self.submit(request)
        self.assertEqual(caught.exception.code,'stale_scope')
        self.assertEqual(self.world.save(),save)
        request = self.request()
        with self.assertRaises(SharedActionUnavailable):
            self.submit(request,current_scope=replace(self.scope(),branch_id='other'))

    def test_changed_replay_and_stale_new_request_cannot_rewrite_outcome(self):
        self.create(); request = self.request(); stale = self.request(); result = self.submit(request)
        before = self.world.save()
        self.assertEqual(self.submit(request),result)
        for changed,code in ((replace(request,intention='Changed'), 'request_identity_conflict'),(stale,'stale_state')):
            with self.assertRaises(SharedActionUnavailable) as caught: self.submit(changed)
            self.assertEqual(caught.exception.code,code)
        self.assertEqual(self.world.save(),before)

    def test_actual_control_revocation_rejects_even_with_the_old_player_list(self):
        self.create(); request = self.request()
        self.world.s['entity_registry']['eligibility']['individual:'+HENRY]['versions'][-1]['eligible'] = False
        self.host.install(self.world); before = self.world.save()
        with self.assertRaises(SharedActionUnavailable): self.submit(replace(request,scope=self.scope()))
        with self.assertRaises(ValueError): self.view()
        self.assertEqual(self.world.save(),before)

    def test_real_actor_reservation_rejects_with_observed_reads_and_no_knowledge_or_time_leak(self):
        import phase_contract
        self.create()
        option = phase_contract.actor_view(self.world,HENRY,branch_id='branch-1',restore_id=self.host.restore_id)['start_options'][0]
        request = phase_contract.prepare_start(self.world,actor=HENRY,capability_id=option['capability_id'],
            process_id='held-observation',phase_id='held-start',intention='Begin this observation as a process.',
            source_ref='explicit synthetic process',branch_id='branch-1',restore_id=self.host.restore_id)
        phase_contract.execute(self.world,request,current_scope=self.scope(),persist=self.host.persist,explicitly_accepted=True)
        # The menu is not a hidden commitment/feasibility oracle.
        request = self.request(); before = self.world.save()
        with self.assertRaises(SharedActionUnavailable) as caught: self.submit(request)
        self.assertEqual(caught.exception.code,'action_unavailable')
        self.assertTrue(caught.exception.dependencies['reads'])
        self.assertEqual(caught.exception.dependencies['writes'],[])
        self.assertEqual(self.world.save(),before)

    def test_evidence_identity_collision_rejects_with_actual_observed_dependencies(self):
        self.create(); request = self.request()
        eid = 'scene:shared:'+request.request_id
        self.world.apply('collision',self.world.s['clock']+1,'record_evidence',
            campaign_id=self.world.s['campaign_id'],source_ref='synthetic collision',evidence_id=eid,
            subject=HENRY,assertion='Unrelated prior evidence.',status='testimony')
        self.host.install(self.world); request = replace(request,scope=self.scope()); before = self.world.save()
        with self.assertRaises(SharedActionUnavailable) as caught: self.submit(request)
        self.assertTrue(caught.exception.dependencies['reads'])
        self.assertEqual(caught.exception.dependencies['writes'],[])
        self.assertEqual(self.world.save(),before)

    def test_competing_observations_have_no_arrival_order_winner(self):
        from r9_runtime import frontier
        self.create(); events=[]
        for key in ('one','two'):
            events.append({'id':'shared:'+key,'at':self.world.s['clock']+1,'op':'execute_player_scene_action',
                'params':{'campaign_id':self.world.s['campaign_id'],'source_ref':'explicit synthetic observation',
                    'instruction_ref':'I observe this setting.','actor':HENRY,
                    'action':{'kind':'scene_action','action_id':'observe-embarkation'},'action_event_id':'shared:'+key}})
        for order in (events,list(reversed(events))):
            candidate=CoreWorld.load(self.world.save())
            result=frontier(candidate,order)
            self.assertEqual(result['committed'],[])
            self.assertEqual(candidate.s['elapsed_time']['seconds'],0)
            self.assertEqual(candidate.s['knowledge'],self.world.s['knowledge'])

    def test_reinitialization_and_precreation_review_of_a_continuing_world_are_refused(self):
        self.create(); before=self.world.save()
        with self.assertRaises(ValueError): api.review_start(self.world,self.character)
        with self.assertRaises(ValueError): initialize_player(self.world,self.character)
        with self.assertRaises(ValueError):
            api.initialize_context(self.world,self.character,{},'explicit reviewed synthetic start')
        self.assertEqual(self.world.save(),before)

    def test_three_distinct_supported_contexts_use_existing_handlers_without_template_seeding(self):
        from settlement_setup import initialize,preview
        from test_settlement import choices
        self.create({'kind':'new','name':'Synthetic courier','species':'human','opening_id':'quay-delivery-v1'})
        result=self.submit(self.request('I observe this authored quay.'))
        self.assertEqual(result['status'],'completed_successfully')
        self.assertEqual(self.world.s['stocks'][self.actor]['sealed_dispatch'],1)
        self.assertTrue(self.world.s['gameplay_started']['authored_opening']['fictional'])
        c=choices(); self.world=initialize(c,preview(c)['review_digest'],'synthetic-rise-regression')
        self.actor='founder'; self.host.install(self.world)
        cap=next(c for c in capabilities(self.world,self.actor) if json.loads(c.action_json).get('action_id')=='inspect')
        request=prepare_intent(self.world,request_id='rise-inspect',actor_id=self.actor,intention='Inspect my actual surroundings.',
            capability_id=cap.capability_id,branch_id='branch-1',restore_id=self.host.restore_id)
        result=self.submit(request)
        self.assertEqual(result['status'],'completed_successfully')
        self.assertEqual(self.view()['current_mode'],'supported_slice')
        self.assertIsNone(self.view()['civil_time'])

    def test_acceptance_and_host_cas_are_mandatory_for_sourced_observation(self):
        self.create(); request=self.request(); before=self.world.save()
        for flag in (False,None,1,'true'):
            with self.assertRaises(SharedActionUnavailable): self.submit(request,explicitly_accepted=flag)
        with self.assertRaises(SharedActionUnavailable): self.submit(request,persist=None)
        self.assertEqual(self.world.save(),before)

    def test_all_37_dated_reference_entries_distinguish_default_existing_mode_from_playability(self):
        from historical_campaigns import historical_catalogue
        for entry in historical_catalogue()['entries']:
            with self.subTest(entry=entry['id']):
                world=raw(entry['id']); options=options_for_world(world)
                actor=next(c['id'] for c in options['characters'] if c['eligible'])
                review=api.review_start(world,{'kind':'existing','actor_id':actor})
                self.assertEqual(review['reference_status'],'verified_dated_reference')
                self.assertTrue(review['character_eligible'])
                self.assertEqual(review['selected_mode']['status'],'declaration_only')
                self.assertEqual(review['playable_context']['status'],'held')
                date=review['known_time_at_creation']['civil']
                self.assertEqual(date['date'],world.s['historical_start']['opening']['date'])
                self.assertIsNone(date['time'])

    def test_literal_fallback_preserves_the_actual_observation_without_paid_narration(self):
        self.create()
        with patch('response_depot._depot',side_effect=OSError('PRIVATE_MISSING_TEXT')):
            result=self.submit(self.request())
        self.assertEqual(result['presentation']['mode'],'literal_receipt')
        self.assertEqual(result['presentation']['text'],result['receipt']['exact_text'])
        self.assertNotIn('PRIVATE_MISSING_TEXT',json.dumps(result))


if __name__ == '__main__':
    unittest.main()
