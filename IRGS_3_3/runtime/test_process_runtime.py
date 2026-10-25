"""Real Core phase effects, observed dependencies and temporary host CAS."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import copy
from pathlib import Path
import tempfile
import unittest

from core_world import CoreWorld
from irgs_reference import canon
from process_runtime import OPERATION, ProcessRequest, execute, prepare, received_status
from r9_runtime import frontier
from settlement_runtime import execute as act
from settlement_setup import initialize, preview
from solo_provider import CapabilityUnavailable, WorldScope
from test_scene_actions import fixture as scene_fixture
from test_settlement import choices
from test_solo_provider import AtomicTestHost


class ProcessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        c = choices(); c['permission'] = 'held'
        self.world = initialize(c, preview(c)['review_digest'], 'phase-fixture')
        self.host = AtomicTestHost(self.temp.name, self.world)
        self.counter = 0

    def scope(self):
        return WorldScope(self.world.s['campaign_id'], 'branch-1', self.host.restore_id, self.world.checksum())

    def request(self, command, details=None, *, process_id='work', phase_id=None, actor='founder'):
        self.counter += 1
        return prepare(self.world, phase_id=phase_id or 'phase-'+str(self.counter), process_id=process_id,
            actor=actor, command=command, details=details or {}, intention='Explicit synthetic '+command,
            source_ref='synthetic-selected-process', branch_id='branch-1', restore_id=self.host.restore_id)

    def submit(self, request, **overrides):
        args = dict(current_scope=self.scope(), persist=self.host.persist, explicitly_accepted=True)
        args.update(overrides)
        return execute(self.world, request, **args)

    def phase(self, command, details=None, **kwargs):
        return self.submit(self.request(command, details, **kwargs))

    def camp(self):
        act(self.world, 'setup-walk', 'founder', 'walk_clearing', 'explicit synthetic setup')
        act(self.world, 'setup-found', 'founder', 'found', 'explicit synthetic setup')
        self.host.install(self.world)

    def assert_rejected(self, fn, code='process_unavailable'):
        before = self.world.save()
        with self.assertRaises(CapabilityUnavailable) as error:
            fn()
        self.assertEqual(error.exception.code, code)
        self.assertEqual(self.world.save(), before)
        return error.exception

    def test_parent_stays_nonterminal_then_work_finishes_once_across_phase_reload(self):
        self.camp()
        started = self.phase('start', {'kind':'work', 'action_id':'build'})
        self.assertFalse(started['terminal'])
        self.assertEqual(started['worked_seconds'], 0)
        self.assertEqual(self.world.s['stocks']['founder-home']['timber'], 6)
        for seconds in (600, 3600, 3600):
            if self.world.s['projects']['shelter']['status'] == 'complete':
                break
            request = self.request('advance', {'seconds':seconds})
            result = self.submit(request)
            self.world = self.host.load()
            before = self.world.save()
            self.assertEqual(self.submit(request), result)
            self.assertEqual(self.world.save(), before)
        self.assertTrue(result['terminal'])
        self.assertEqual(result['worked_seconds'], 3600)
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 3900)
        self.assertEqual(self.world.s['stocks']['founder-home']['timber'], 3)
        self.assertEqual(len([f for f in self.world.s['material_flows'] if f=='project:shelter']), 1)
        self.assert_rejected(lambda:self.phase('advance', {'seconds':1}))

    def test_pause_resume_does_not_repeat_booking_or_elapsed_work(self):
        self.camp(); self.phase('start', {'kind':'work','action_id':'build'})
        self.phase('advance', {'seconds':600})
        result = self.phase('pause')
        self.assertEqual(result['status'], 'paused')
        act(self.world, 'other-time', 'founder', 'wait_hour', 'explicit paused wait')
        self.assertEqual(self.world.s['projects']['shelter']['worked'], 600)
        self.host.install(self.world)
        self.phase('resume')
        self.phase('advance', {'seconds':3600})
        self.assertEqual(self.world.s['projects']['shelter']['worked'], 3600)
        self.assertEqual(self.world.s['stocks']['founder-home']['timber'], 3)

    def test_cancel_retains_physical_project_and_new_explicit_resume_uses_existing_work(self):
        self.camp(); self.phase('start', {'kind':'work','action_id':'build'})
        self.phase('advance', {'seconds':600})
        cancelled = self.phase('cancel')
        self.assertTrue(cancelled['terminal'])
        self.assertEqual(self.world.s['projects']['shelter']['worked'], 600)
        self.assert_rejected(lambda:self.phase('resume'))
        resumed = self.phase('start', {'kind':'work','action_id':'resume'}, process_id='new-instruction')
        self.assertEqual(resumed['worked_seconds'], 600)
        self.assertEqual(len(self.world.s['projects']), 2)  # One shelter, one existing NPC repair.

    def test_partial_travel_moves_actual_people_and_goods_without_teleporting_on_pause(self):
        initial_stocks = copy.deepcopy(self.world.s['stocks'])
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        self.assertEqual(self.world.s['actors']['founder']['current']['location'], 'route:commons-clearing')
        self.assertEqual(self.world.s['stock_accounts']['founder-home']['site'], 'route:commons-clearing')
        self.phase('advance', {'seconds':100})
        self.phase('pause')
        self.assert_rejected(lambda:self.phase('advance', {'seconds':100}))
        self.assert_rejected(lambda:self.phase('cancel'))
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 100)
        self.phase('resume'); result = self.phase('advance', {'seconds':1000})
        self.assertEqual(result['elapsed_seconds'], 200)
        self.assertEqual(result['elapsed_total'], 300)
        self.assertEqual(self.world.s['actors']['founder']['current']['location'], 'clearing')
        self.assertEqual(self.world.s['stocks'], initial_stocks)
        self.assertEqual(self.world.s['stock_accounts']['founder-home']['site'], 'clearing')

    def test_existing_wait_advances_the_same_journey_and_produces_received_arrival(self):
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        act(self.world, 'shared-time', 'founder', 'wait_hour', 'explicit shared time')
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 300)
        self.assertEqual(self.world.s['processes']['work']['task']['status'], 'complete')
        self.assertIn('process-arrival:work', self.world.s['settlement_receipts']['founder'])

    def test_atomic_and_phased_travel_have_the_same_physical_result(self):
        atomic = CoreWorld.load(self.world.save())
        act(atomic, 'atomic-walk', 'founder', 'walk_clearing', 'explicit atomic walk')
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        for _ in range(3):self.phase('advance', {'seconds':100})
        for key in ('actors','stocks','stock_accounts','projects','elapsed_time'):
            self.assertEqual(self.world.s[key], atomic.s[key])

    def test_reserved_traveller_cannot_start_another_walk(self):
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        before = self.world.save()
        from irgs_reference import InvalidEvent
        with self.assertRaises(InvalidEvent):
            act(self.world, 'another-walk', 'founder', 'walk_commons', 'explicit conflicting walk')
        self.assertEqual(self.world.save(), before)
        self.assert_rejected(lambda:self.phase('start', {'kind':'travel','action_id':'walk_commons'},process_id='other'))

    def test_observation_publishes_knowledge_only_after_the_selected_duration(self):
        self.world = scene_fixture(); self.host.install(self.world)
        before = set(self.world.s['knowledge']['pc'])
        self.phase('start', {'kind':'observation','action_id':'look-quay'}, actor='pc')
        self.phase('advance', {'seconds':1}, actor='pc')
        self.assertEqual(set(self.world.s['knowledge']['pc']), before)
        self.phase('pause', actor='pc')
        self.world = self.host.load()
        self.phase('resume', actor='pc')
        result = self.phase('advance', {'seconds':100}, actor='pc')
        self.assertTrue(result['terminal'])
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 3)
        self.assertGreater(len(self.world.s['knowledge']['pc']), len(before))
        self.assertEqual(len(self.world.s['scene_action_results']), 1)

    def test_observation_reservation_blocks_another_physical_scene_action(self):
        from scene_actions import execute_scene_action, SceneActionUnavailable
        self.world = scene_fixture(); self.host.install(self.world)
        self.phase('start', {'kind':'observation','action_id':'look-quay'}, actor='pc')
        before = self.world.save()
        with self.assertRaises(SceneActionUnavailable):
            execute_scene_action(self.world,'other','pc',{'kind':'scene_action','action_id':'enter-passage'},'explicit')
        self.assertEqual(self.world.save(), before)
        self.phase('cancel', actor='pc')
        execute_scene_action(self.world,'after-cancel','pc',{'kind':'scene_action','action_id':'enter-passage'},'explicit')

    def test_unselected_elapsed_axis_or_rule_source_cannot_start_work(self):
        for axis,source in [('unbound-axis','synthetic'),('authored-opening-seconds','')]:
            self.world=scene_fixture()
            self.world.s['elapsed_time']['axis']=axis
            self.world.s['elapsed_time']['source_ref']=source
            self.host.install(self.world)
            self.assert_rejected(lambda:self.phase('start',{'kind':'observation','action_id':'look-quay'},actor='pc'))
            self.assertEqual(self.world.s['elapsed_time']['seconds'],0)

    def test_revoked_permission_holds_work_without_partial_consumption_and_resume_rechecks(self):
        self.camp(); self.phase('start', {'kind':'work','action_id':'build'})
        self.world.s['grants']['founding']['active'] = False
        self.host.install(self.world)
        result = self.phase('advance', {'seconds':100})
        self.assertEqual(result['status'], 'held')
        self.assertEqual(result['worked_seconds'], 0)
        self.assertEqual(self.world.s['stocks']['founder-home']['timber'], 6)
        self.phase('pause')
        error = self.assert_rejected(lambda:self.phase('resume'))
        self.assertTrue(error.dependencies['reads'])
        self.assertEqual(error.dependencies['writes'], [])

    def test_unsupported_span_or_stale_phase_is_atomic(self):
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        for value in (-1,0,True,1.5,100000):
            self.assert_rejected(lambda:self.phase('advance', {'seconds':value}))
        request = self.request('advance', {'seconds':100})
        self.assert_rejected(lambda:self.submit(replace(request,phase_index=99)))
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 0)

    def test_changed_selected_rule_refuses_continuation(self):
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        self.world.s['settlement_model']['travel_seconds'] += 1
        self.host.install(self.world)
        self.assert_rejected(lambda:self.phase('advance', {'seconds':100}))

    def test_explicit_acceptance_and_actor_control_are_required(self):
        request = self.request('start', {'kind':'travel','action_id':'walk_clearing'})
        self.assert_rejected(lambda:self.submit(request, explicitly_accepted=False),'acceptance_required')
        self.world.s['player_actor_ids'] = []
        self.host.install(self.world)
        self.assert_rejected(lambda:self.submit(request),'stale_state')
        self.assert_rejected(lambda:self.request('start', {'kind':'travel','action_id':'walk_clearing'}),'actor_denied')

    def test_lost_ack_and_host_restart_recover_original_phase_receipt(self):
        request = self.request('start', {'kind':'travel','action_id':'walk_clearing'})
        pending=Path(self.temp.name)/'pending-process.json'
        pending.write_text(request.to_json())
        def lost(scope,save,receipt):
            self.host.persist(scope,save,receipt)
            raise OSError('synthetic lost acknowledgment')
        with self.assertRaises(OSError):self.submit(request,persist=lost)
        self.world = self.host.load()
        request=ProcessRequest.from_json(pending.read_text())
        before = self.world.save()
        recovered = self.submit(request)
        self.assertEqual(recovered['phase_id'], request.phase_id)
        self.assertEqual(self.world.save(), before)
        self.assertEqual(self.host.writes, 1)
        self.assert_rejected(lambda:self.submit(replace(request,intention='changed intent')),'request_identity_conflict')

    def test_restore_fences_old_phase_but_new_request_continues_saved_progress(self):
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        saved = self.world.save()
        discarded = self.request('advance', {'seconds':100})
        self.submit(discarded)
        self.world = CoreWorld.load(saved); self.host.restore_id='restore-2'; self.host.install(self.world)
        self.assert_rejected(lambda:self.submit(discarded),'stale_scope')
        fresh = self.phase('advance', {'seconds':100})
        self.assertEqual(fresh['worked_seconds'], 100)

    def test_concurrent_delivery_commits_one_phase_and_one_elapsed_span(self):
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        request = self.request('advance', {'seconds':100})
        saved,scope = self.world.save(),self.scope()
        def deliver(_):
            w = CoreWorld.load(saved)
            try:return execute(w,request,current_scope=scope,persist=self.host.persist,explicitly_accepted=True)
            except CapabilityUnavailable as error:return error.code
        with ThreadPoolExecutor(2) as pool:results=list(pool.map(deliver,range(2)))
        self.assertEqual(sum(isinstance(r,dict) for r in results),1)
        self.world=self.host.load()
        self.assertEqual(self.world.s['elapsed_time']['seconds'],100)
        self.assertEqual(self.submit(request)['worked_seconds'],100)

    def test_status_is_a_received_record_and_does_not_peek_at_remote_progress(self):
        self.camp(); self.phase('start', {'kind':'work','action_id':'build'})
        recorded = received_status(self.world,'founder','work')
        act(self.world, 'external-time', 'founder', 'wait_hour', 'explicit external time')
        self.assertEqual(received_status(self.world,'founder','work'),recorded)
        self.assertEqual(recorded['worked_seconds'],0)
        self.assertGreater(self.world.s['projects']['shelter']['worked'],0)
        self.assert_rejected(lambda:received_status(self.world,'someone-else','work'),'actor_denied')

    def test_model_context_receives_only_owned_committed_phase_projection(self):
        from solo_actions import prepare_request
        self.phase('start',{'kind':'travel','action_id':'walk_clearing'})
        phase=self.phase('advance',{'seconds':100})
        request=prepare_request(self.world,request_id='provider-after-phase',actor_id='founder',
            intention='Review my committed progress.',branch_id='branch-1',restore_id='restore-1',
            allowed_routes=('offline',),classification='synthetic-approved',
            policy_ref='synthetic-policy',config_version='synthetic-v1',deadline=100)
        projected=request.model_input()['context']['received']
        row=next(row for row in projected if row['id']=='process-phase:'+phase['phase_id'])
        self.assertEqual(row['worked_seconds'],100)
        self.assertEqual(row['remaining_seconds'],200)
        serialized=canon(request.model_input())
        for private in ('"projects"','"stocks"','"journal"','"rule_digest"','"params_digest"','"processes"'):
            self.assertNotIn(private,serialized)

    def test_independent_evidence_and_process_advance_share_a_valid_frontier(self):
        self.phase('start', {'kind':'travel','action_id':'walk_clearing'})
        request=self.request('advance',{'seconds':100})
        params={'campaign_id':self.world.s['campaign_id'],'source_ref':request.source_ref,
            'instruction_ref':request.intention,'actor':request.actor,'process_id':request.process_id,
            'phase_id':request.phase_id,'phase_index':request.phase_index,'command':request.command,
            'details':{'seconds':100},'intention':request.intention}
        at=self.world.s['clock']+1
        movement={'id':'process:'+request.phase_id,'at':at,'op':OPERATION,'params':params}
        evidence={'id':'independent-evidence','at':at,'op':'record_evidence','params':{
            'campaign_id':self.world.s['campaign_id'],'source_ref':'synthetic-testimony',
            'evidence_id':'separate-claim','subject':'elin','assertion':'A separate testimony.',
            'status':'testimony','originator':'elin'}}
        for events in ([movement,evidence],[evidence,movement]):
            w=CoreWorld.load(self.world.save())
            result=frontier(w,events)
            self.assertEqual(set(result['committed']),{'process:'+request.phase_id,'independent-evidence'})
            self.assertEqual(w.s['elapsed_time']['seconds'],100)
            self.assertEqual(w.s['evidence']['separate-claim']['status'],'testimony')


if __name__ == '__main__':unittest.main()
