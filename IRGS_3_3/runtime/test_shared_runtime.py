"""Shared contracts over actual selected non-Rise and Rise Core handlers."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import copy
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest
from unittest.mock import patch

from campaign_library import initial_campaign
from core_world import CoreWorld
from irgs_reference import canon
from runtime_contracts import AcceptedIntent, WorldScope
from shared_runtime import (SharedActionUnavailable, actor_view, capabilities, committed_receipt,
                            execute_intent, prepare_intent, received_records)
from settlement_setup import initialize, preview
from test_scene_actions import apply, fixture as scene_fixture
from test_settlement import choices
from test_solo_provider import AtomicTestHost, CapabilityUnavailable


class SharedRuntimeTests(unittest.TestCase):
    def setUp(self):
        for target in ('solo_provider.CapabilityBroker.dispatch',
                       'openai_proposals.OpenAIProposalTransport.__call__','socket.socket.connect'):
            mock=patch(target,side_effect=AssertionError('Offline runtime cannot dispatch'))
            mock.start();self.addCleanup(mock.stop)
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.world=scene_fixture();self.actor='pc'
        self.host=AtomicTestHost(self.temp.name,self.world)
        self.counter=0

    def rise(self):
        c=choices();c['permission']='held'
        self.world=initialize(c,preview(c)['review_digest'],'shared-rise')
        self.actor='founder';self.host.install(self.world)

    def scope(self):
        return WorldScope(self.world.s['campaign_id'],'branch-1',self.host.restore_id,self.world.checksum())

    def view(self):
        return actor_view(self.world,self.actor,branch_id='branch-1',restore_id=self.host.restore_id)

    def prepare(self,action_id=None,*,intention='Exact edited intention. No extra decisions.',request_id=None):
        self.counter+=1
        cap=next((c for c in capabilities(self.world,self.actor)
                  if json.loads(c.action_json).get('action_id')==action_id),None) if action_id else None
        return prepare_intent(self.world,request_id=request_id or 'request-'+str(self.counter),
            actor_id=self.actor,intention=intention,branch_id='branch-1',restore_id=self.host.restore_id,
            capability_id=cap.capability_id if cap else None)

    def submit(self,request,**kwargs):
        args={'current_scope':self.scope(),'persist':self.host.persist,'explicitly_accepted':True}
        args.update(kwargs)
        return execute_intent(self.world,request,**args)

    def test_same_contract_executes_two_actions_in_independently_initialized_contexts(self):
        for context in ('authored-scene','rise'):
            with self.subTest(context=context):
                if context=='rise':self.rise()
                original=copy.deepcopy(self.world.s['opening_stock'])
                ids=('enter-passage','reach-desk') if context=='authored-scene' else ('walk_clearing','found')
                results=[]
                for action in ids:
                    result=self.submit(self.prepare(action))
                    self.assertEqual(result['presentation']['library_id'],'irgs-response-depot-v1')
                    self.assertIn(result['receipt']['exact_text'],result['presentation']['text'])
                    self.assertEqual(result['presentation']['render_usage'],{'provider_calls':0,'model_tokens':0})
                    self.world=self.host.load();results.append(result)
                self.assertEqual(self.world.s['opening_stock'],original)
                if context=='authored-scene':
                    self.assertEqual(self.world.s['elapsed_time']['seconds'],35)
                    self.assertEqual(self.world.s['actors']['pc']['current']['location']['value'],'desk')
                else:
                    self.assertIn('camp',self.world.s['settlements'])
                    self.assertEqual(self.world.s['elapsed_time']['seconds'],300)

    def test_non_rise_actual_delivery_conserves_stock_and_duplicate_does_not_repeat_it(self):
        for action in ('enter-passage','reach-desk'):self.submit(self.prepare(action))
        request=self.prepare('deliver',intention='Deliver this dispatch; do not accept another task.')
        result=self.submit(request);self.world=self.host.load();before=self.world.save()
        self.assertEqual(self.world.s['stocks'],{'pc':{'sealed_dispatch':0},'clerk-tray':{'sealed_dispatch':1}})
        self.assertEqual(self.submit(AcceptedIntent.from_json(request.to_json())),result)
        self.assertEqual(self.world.save(),before)
        self.assertEqual(self.world.s['elapsed_time']['seconds'],39)

    def test_non_rise_blocked_movement_keeps_actual_failure_and_elapsed(self):
        result=self.submit(self.prepare('try-gate'))
        self.assertEqual(result['status'],'completed_unsuccessfully')
        self.assertIn('gate remains closed',result['presentation']['text'])
        self.assertEqual(result['receipt']['elapsed_seconds'],5)
        self.assertEqual(self.world.s['actors']['pc']['current']['location']['value'],'quay')

    def test_missing_adapter_retains_explicit_intention_as_unresolved_without_creating_mechanics(self):
        self.world=initial_campaign('military','generic-context');self.actor='player'
        apply(self.world,'player','register_actor',actor_id='player',name='Player',species='human',
              player_controlled=True,instruction_ref='explicit synthetic player')
        self.host.install(self.world);before=copy.deepcopy(self.world.s['stocks'])
        self.assertEqual(len(self.view()['capabilities']),1)
        intention='I attempt an orbital jump and negotiate a truce.'
        result=self.submit(self.prepare(intention=intention))
        self.assertEqual(result['status'],'declared_not_resolved')
        self.assertIn(intention,result['presentation']['text'])
        self.assertEqual(self.world.s['player_actions'][-1]['declaration'],intention)
        self.assertEqual(self.world.s['stocks'],before)
        self.assertNotIn('elapsed_time',self.world.s)

    def test_generic_semantic_tag_or_unknown_capability_never_routes(self):
        before=self.world.save()
        for identity in ('travel','player.travel','execute_player_scene_action',''):
            with self.assertRaises(SharedActionUnavailable):
                prepare_intent(self.world,request_id='x',actor_id='pc',intention='Travel.',
                    branch_id='b',restore_id='r',capability_id=identity)
        self.assertEqual(self.world.save(),before)

    def test_drafts_are_capability_bound_editable_and_selection_and_preparation_commit_nothing(self):
        before=self.world.save();view=self.view()
        self.assertEqual(len(view['drafts']),24)
        known={c['capability_id'] for c in view['capabilities']}
        for draft in view['drafts']:
            self.assertIn(draft['capability_id'],known)
            self.assertTrue(draft['editable'] and draft['requires_explicit_submission'])
            self.assertFalse(draft['automatic_execution'])
        request=self.prepare('try-gate',intention='Edited custom words, not an automatic action.')
        self.assertEqual(request.intention,'Edited custom words, not an automatic action.')
        self.assertEqual(self.world.save(),before)

    def test_capabilities_and_drafts_do_not_filter_hidden_blockers_or_stock(self):
        original=self.view()
        self.world.s['site_conditions']['quay-gate']['passable']=True
        self.world.s['stocks']['pc']['sealed_dispatch']=0
        self.assertEqual(self.view(),original)
        self.rise();original=self.view()
        self.world.s['stocks']['founder-home']['timber']=0
        self.assertEqual(self.view(),original)

    def test_explicit_acceptance_and_mandatory_persistence_precede_any_effect(self):
        request=self.prepare('enter-passage');before=self.world.save()
        for kwargs in ({'explicitly_accepted':False},{'explicitly_accepted':1},{'persist':None}):
            with self.assertRaises(SharedActionUnavailable):self.submit(request,**kwargs)
        self.assertEqual(self.world.save(),before)

    def test_failed_save_leaves_world_unchanged_and_does_not_acknowledge_result(self):
        request=self.prepare('enter-passage');before=self.world.save()
        def fail(*args):raise OSError('synthetic disk failure')
        with self.assertRaises(OSError):self.submit(request,persist=fail)
        self.assertEqual(self.world.save(),before)
        result=self.submit(request)
        self.assertEqual(result['status'],'completed_successfully')
        self.assertEqual(self.world.s['elapsed_time']['seconds'],20)

    def test_lost_ack_serialized_pending_request_restarts_with_original_receipt(self):
        request=self.prepare('enter-passage');pending=Path(self.temp.name)/'pending.json'
        pending.write_text(request.to_json())
        def lose_ack(*args):self.host.persist(*args);raise OSError('lost acknowledgment')
        before=self.world.save()
        with self.assertRaises(OSError):self.submit(request,persist=lose_ack)
        self.assertEqual(self.world.save(),before)
        self.world=self.host.load()
        result=self.submit(AcceptedIntent.from_json(pending.read_text()))
        self.assertEqual(result,json.loads(self.host.path.read_text())['receipt'])
        self.assertEqual(self.host.writes,1)
        self.assertEqual(self.world.s['elapsed_time']['seconds'],20)

    def test_restore_and_branch_fences_reject_discarded_future_requests(self):
        past=self.world.save();request=self.prepare('enter-passage')
        self.submit(request);self.world=CoreWorld.load(past);self.host.restore_id='restore-2';self.host.install(self.world)
        before=self.world.save()
        with self.assertRaises(SharedActionUnavailable) as error:self.submit(request)
        self.assertEqual(error.exception.code,'stale_scope')
        self.assertEqual(self.world.save(),before)
        with self.assertRaises(SharedActionUnavailable):
            self.submit(request,current_scope=replace(self.scope(),branch_id='another-branch'))

    def test_changed_state_and_revoked_control_reject_fresh_requests(self):
        request=self.prepare('enter-passage');self.submit(self.prepare('look-quay'))
        before=self.world.save()
        with self.assertRaises(SharedActionUnavailable) as error:self.submit(request)
        self.assertEqual(error.exception.code,'stale_state');self.assertEqual(self.world.save(),before)
        request=self.prepare('enter-passage');self.world.s['player_actor_ids']=[]
        with self.assertRaises(SharedActionUnavailable):self.submit(request)

    def test_changed_replay_payload_cannot_reinterpret_an_accepted_request(self):
        request=self.prepare('enter-passage');self.submit(request);before=self.world.save()
        for changed in (replace(request,intention='Changed decision'),replace(request,source_ref='different'),
                        replace(request,action_json=canon({'kind':'scene_action','action_id':'try-gate'})),
                        replace(request,operation_id='execute_settlement_action',action_json=canon({'action_id':'walk_clearing'}))):
            with self.assertRaises(SharedActionUnavailable) as error:self.submit(changed)
            self.assertEqual(error.exception.code,'request_identity_conflict')
        self.assertEqual(self.world.save(),before)

    def test_forged_action_or_capability_is_rechecked_before_core(self):
        request=self.prepare('enter-passage');before=self.world.save()
        for changed in (replace(request,action_json=canon({'kind':'scene_action','action_id':'deliver'})),
                        replace(request,operation_id='transfer_stock'),replace(request,capability_id='travel')):
            with self.assertRaises(SharedActionUnavailable):self.submit(changed)
        self.assertEqual(self.world.save(),before)

    def test_concurrent_host_compare_and_swap_saves_one_effect(self):
        request=self.prepare('enter-passage');save=self.world.save()
        def submit_copy():
            world=CoreWorld.load(save)
            try:
                return execute_intent(world,request,current_scope=request.scope,persist=self.host.persist,explicitly_accepted=True)
            except CapabilityUnavailable:
                return None  # Host CAS refusal; reload then use the actual receipt.
        with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(lambda _:submit_copy(),range(2)))
        self.assertEqual(sum(result is not None for result in results),1)
        self.world=self.host.load()
        self.assertEqual(self.world.s['elapsed_time']['seconds'],20)
        self.assertEqual(self.submit(request),next(r for r in results if r))

    def test_receipt_replay_never_appends_current_information_or_cross_actor_data(self):
        first=self.submit(self.prepare('look-quay'))
        self.submit(self.prepare('enter-passage'));self.world=self.host.load();before=self.world.save()
        receipt=committed_receipt(self.world,'pc',first['receipt']['event_id'],branch_id='branch-1',restore_id=self.host.restore_id)
        self.assertEqual(receipt,first['receipt']);self.assertNotIn('desk lies ahead',receipt['exact_text'])
        with self.assertRaises(SharedActionUnavailable):
            committed_receipt(self.world,'someone-else',receipt['event_id'],branch_id='branch-1',restore_id=self.host.restore_id)
        self.assertEqual(self.world.save(),before)

    def test_snapshot_changes_with_branch_restore_and_actual_received_text(self):
        first=self.view()
        other=actor_view(self.world,'pc',branch_id='other',restore_id=self.host.restore_id)
        self.assertNotEqual(first['snapshot_id'],other['snapshot_id'])
        self.host.restore_id='restored'
        self.assertNotEqual(first['snapshot_id'],self.view()['snapshot_id'])
        self.assertEqual(first['drafts'][0]['text'],other['drafts'][0]['text'])

    def test_private_and_foreign_evidence_is_absent_and_sources_status_and_time_remain(self):
        apply(self.world,'hidden','record_evidence',evidence_id='hidden',subject='pc',assertion='PRIVATE_MARKER',status='testimony')
        apply(self.world,'known','record_evidence',evidence_id='known',subject='pc',assertion='Unverified report.',status='testimony')
        apply(self.world,'known-received','receive_evidence',evidence_id='known',recipient='pc')
        before=self.world.save();view=self.view();raw=json.dumps(view)
        self.assertNotIn('PRIVATE_MARKER',raw)
        for forbidden in ('state_digest','site_conditions','stocks','processed','rule_digest','params_digest'):
            self.assertNotIn('"'+forbidden+'"',raw)
        known=next(r for r in view['received']['records'] if r['record_id']=='known')
        self.assertEqual(known['status'],'testimony');self.assertEqual(known['time_axis'],'causal_sequence')
        self.assertEqual(self.world.save(),before)

    def test_received_record_truncation_is_explicit_and_does_not_imply_absence(self):
        records=received_records(self.world,'pc',limit=1)
        self.assertTrue(records['truncated']);self.assertGreater(records['total'],1)
        self.assertEqual(len(records['records']),1)

    def test_missing_depot_retains_exact_outcome_drafts_and_unresolved_status_without_dispatch(self):
        from response_depot import render_public_status
        with patch('response_depot._depot',side_effect=OSError('missing source')):
            result=self.submit(self.prepare('try-gate'))
            self.assertEqual(result['presentation']['mode'],'literal_receipt')
            self.assertEqual(result['presentation']['text'],result['receipt']['exact_text'])
            self.assertTrue(self.view()['drafts'])
            self.assertTrue(all(d['mode']=='literal_draft' for d in self.view()['drafts']))
            status=render_public_status('pc','snapshot','declared_not_resolved')
            self.assertIn('unresolved',status['text'])

    def test_equipment_without_new_adapter_keeps_existing_honest_result(self):
        from test_player_actions import fixture, execute
        world=fixture();before=world.s['stocks']['depot']['kit']
        result=execute(world)
        self.assertEqual(world.s['stocks']['depot']['kit'],before-1)
        self.assertIn('Issued',result['outcome']['summary'])
        with self.assertRaises(SharedActionUnavailable) as error:
            committed_receipt(world,'commander','execute',branch_id='b',restore_id='r')
        self.assertEqual(error.exception.code,'receipt_adapter_unavailable')
        self.assertNotIn('presentation',result)

    def test_shared_receipt_supports_actual_phase_and_received_communication_without_inventing_rules(self):
        import test_process_runtime as process_cases
        import test_communication_runtime as speech_cases
        process=process_cases.ProcessTests(methodName='runTest');process.setUp();self.addCleanup(process.doCleanups)
        process.camp();phase=process.phase('start',{'kind':'work','action_id':'build'})
        before=process.world.save()
        receipt=committed_receipt(process.world,'founder','process:'+phase['phase_id'],branch_id='branch-1',restore_id='restore-1')
        self.assertEqual(receipt['outcome_status'],'active');self.assertEqual(receipt['elapsed_seconds'],0)
        self.assertIn('not complete',receipt['exact_text']);self.assertEqual(process.world.save(),before)
        speech=speech_cases.CommunicationTests(methodName='runTest');speech.setUp();self.addCleanup(speech.doCleanups)
        spoken=speech.act('speak',text='Do not accept this offer; the report is unverified.')
        event='communication:'+spoken['request_id'];before=speech.world.save()
        heard=committed_receipt(speech.world,'oren',event,branch_id='branch-1',restore_id='restore-1')
        self.assertIn(spoken['utterance'],heard['presentation']['text'])
        self.assertIn('Testimony from founder',heard['exact_text'])
        self.assertIsNone(heard['elapsed_seconds']);self.assertEqual(speech.world.save(),before)

    def test_serialization_is_strict_and_world_scope_remains_backwards_compatible(self):
        from solo_provider import WorldScope as previous_import
        self.assertIs(previous_import,WorldScope)
        request=self.prepare('look-quay')
        self.assertEqual(AcceptedIntent.from_json(request.to_json()),request)
        for raw in ('{"request_id":"a","request_id":"b"}',request.to_json()[:-1]+',"extra":1}'):
            with self.assertRaises((ValueError,TypeError)):AcceptedIntent.from_json(raw)

    def test_core_declaration_observes_current_control_and_rejects_revoked_eligibility(self):
        from r9_runtime import conflicts, observe, observe_rejection
        declaration={'id':'declaration','at':self.world.s['clock']+1,'op':'record_player_action',
            'params':{'campaign_id':self.world.s['campaign_id'],'source_ref':'explicit synthetic declaration',
                      'actor':'pc','declaration':'My unresolved intention.','instruction_ref':'explicit declaration'}}
        revoke={'id':'revoke','at':declaration['at'],'op':'record_entity_eligibility',
            'params':{'campaign_id':self.world.s['campaign_id'],'source_ref':'explicit synthetic revocation',
                      'entity_id':'pc','scenario_id':'individual','eligible':False,
                      'reason':'Explicit current withdrawal','effective_at':self.world.s['entity_registry']['as_of']}}
        self.assertTrue(conflicts(observe(self.world.s,declaration),observe(self.world.s,revoke)))
        self.world.apply(revoke['id'],revoke['at'],revoke['op'],**revoke['params'])
        self.assertIn('pc',self.world.s['player_actor_ids'])
        declaration['at']+=1;before=self.world.save()
        from irgs_reference import InvalidEvent
        with self.assertRaises(InvalidEvent):
            self.world.apply(declaration['id'],declaration['at'],declaration['op'],**declaration['params'])
        rejected=observe_rejection(self.world.s,declaration)
        self.assertFalse(rejected['successful_certificate'])
        self.assertTrue(any(path[0]=='entity_registry' for path in rejected['reads']))
        self.assertEqual(self.world.save(),before)

    def test_fresh_process_executes_non_rise_without_provider_modules_or_other_components(self):
        script='''
import builtins, json, tempfile
from pathlib import Path
original_import=builtins.__import__
def restricted(name,*args,**kwargs):
    if name.split('.')[0] in ('solo_provider','openai_proposals','IRGS_Catalog','IRGS_Web'):
        raise AssertionError('Forbidden runtime dependency: '+name)
    return original_import(name,*args,**kwargs)
builtins.__import__=restricted
from test_scene_actions import fixture
from shared_runtime import capabilities, prepare_intent, execute_intent
from runtime_contracts import WorldScope
world=fixture()
cap=next(c for c in capabilities(world,'pc') if json.loads(c.action_json).get('action_id')=='enter-passage')
request=prepare_intent(world,request_id='independent',actor_id='pc',intention='Enter the passage.',
    branch_id='branch',restore_id='restore',capability_id=cap.capability_id)
with tempfile.TemporaryDirectory() as root:
    def persist(expected,save,receipt):
        assert expected==WorldScope(world.s['campaign_id'],'branch','restore',world.checksum())
        Path(root,'save.json').write_text(json.dumps({'save':save,'receipt':receipt}))
    result=execute_intent(world,request,current_scope=request.scope,persist=persist,explicitly_accepted=True)
    assert world.s['actors']['pc']['current']['location']['value']=='passage'
    assert result['presentation']['render_usage']=={'provider_calls':0,'model_tokens':0}
print('independent non-Rise Core action passed')
'''
        result=subprocess.run([sys.executable,'-B','-c',script],cwd=Path(__file__).resolve().parent,
            capture_output=True,text=True,env={})
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)


if __name__=='__main__':
    unittest.main()
