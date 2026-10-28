"""Host-safe phase DTOs over selected actual Core observation and work."""
from dataclasses import replace
from concurrent.futures import ThreadPoolExecutor
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from core_world import CoreWorld
import phase_contract as api
from process_runtime import ProcessRequest
from runtime_contracts import WorldScope
from settlement_runtime import execute as settlement_action
from settlement_setup import initialize, preview
from test_scene_actions import fixture as scene_fixture
from test_settlement import choices
from test_solo_provider import AtomicTestHost, CapabilityUnavailable


class PhaseContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.world = scene_fixture()
        self.actor = 'pc'
        self.host = AtomicTestHost(self.temp.name, self.world)
        self.counter = 0
        for target in ('solo_provider.CapabilityBroker.dispatch',
                       'openai_proposals.OpenAIProposalTransport.__call__', 'socket.socket.connect'):
            blocker = patch(target, side_effect=AssertionError('No provider/network in phase API'))
            blocker.start(); self.addCleanup(blocker.stop)

    def rise(self):
        c = choices(); c['permission'] = 'held'
        self.world = initialize(c, preview(c)['review_digest'], 'phase-contract-fixture')
        self.actor = 'founder'
        settlement_action(self.world, 'setup-walk', self.actor, 'walk_clearing', 'explicit synthetic setup')
        settlement_action(self.world, 'setup-camp', self.actor, 'found', 'explicit synthetic setup')
        self.host.install(self.world)

    def scope(self):
        return WorldScope(self.world.s['campaign_id'], 'branch-1', self.host.restore_id, self.world.checksum())

    def view(self):
        return api.actor_view(self.world, self.actor, branch_id='branch-1', restore_id=self.host.restore_id)

    def start_request(self, *, action=None, process_id='parent', phase_id=None):
        self.counter += 1
        action = action or ('build' if self.actor == 'founder' else 'look-quay')
        option = next(row for row in self.view()['start_options'] if row['action_id'] == action)
        return api.prepare_start(self.world, actor=self.actor, capability_id=option['capability_id'],
            process_id=process_id, phase_id=phase_id or 'phase-'+str(self.counter), intention='Exact selected '+action,
            source_ref='explicit synthetic phase contract', branch_id='branch-1', restore_id=self.host.restore_id)

    def command_request(self, command, details=None, *, process_id='parent'):
        self.counter += 1
        return api.prepare_command(self.world, actor=self.actor, process_id=process_id,
            phase_id='phase-'+str(self.counter), command=command, details=details or {},
            intention='Exact selected '+command, source_ref='explicit synthetic phase contract',
            branch_id='branch-1', restore_id=self.host.restore_id)

    def submit(self, request, **overrides):
        args = dict(current_scope=self.scope(), persist=self.host.persist, explicitly_accepted=True)
        args.update(overrides)
        return api.execute(self.world, request, **args)

    def command(self, command, details=None):
        return self.submit(self.command_request(command, details))

    def test_both_selected_contexts_expose_attemptable_starts_without_effects(self):
        for context in ('observation', 'work'):
            if context == 'work': self.rise()
            before = self.world.save(); view = self.view()
            self.assertEqual({r['kind'] for r in view['start_options']},
                             {'work', 'travel'} if context == 'work' else {context})
            for row in view['start_options']:
                self.assertTrue(row['source_refs'])
                self.assertTrue(row['requires_explicit_submission'])
                self.assertEqual(row['availability'], 'attemptable')
            self.start_request()
            self.assertEqual(self.world.save(), before)

    def test_observation_completes_once_with_actual_elapsed_and_received_knowledge(self):
        started = self.submit(self.start_request())
        self.assertFalse(started['terminal'])
        partial = self.command('advance', {'seconds': 2})
        self.assertEqual(partial['worked_seconds'], 2)
        self.assertNotIn('passage and the closed gate', partial['presentation']['text'])
        final = self.command('advance', {'seconds': 1})
        self.assertEqual(final['status'], 'completed')
        self.assertTrue(final['terminal'])
        self.assertEqual(final['elapsed_total'], 3)
        self.assertIn('You see the passage and the closed gate.', final['presentation']['text'])
        self.assertEqual([r['command'] for r in final['supported_commands']], ['inspect'])

    def test_work_uses_existing_project_reservations_and_conserved_inputs(self):
        self.rise(); started = self.submit(self.start_request())
        self.assertEqual(started['worked_seconds'], 0)
        self.assertEqual(self.world.s['stocks']['founder-home']['timber'], 6)
        self.assertEqual(self.world.s['projects']['shelter']['worker'], 'founder')
        boundary = self.command('advance', {'seconds': 3600})
        self.assertEqual(boundary['status'], 'active')
        self.assertGreater(boundary['worked_seconds'], 0)
        self.assertLess(boundary['worked_seconds'], 3600)  # Actual selected provision boundary.
        self.assertEqual(boundary['worked_seconds'], boundary['elapsed_seconds'])
        final = boundary
        for _ in range(4):
            if final['terminal']: break
            final = self.command('advance', {'seconds': 3600})
        self.assertEqual(final['status'], 'completed')
        self.assertEqual(final['worked_seconds'], 3600)
        self.assertEqual(self.world.s['stocks']['founder-home']['timber'], 3)
        self.assertEqual(len([k for k in self.world.s['material_flows'] if k == 'project:shelter']), 1)

    def test_safe_phase_and_shared_actor_views_omit_private_records_and_certificates(self):
        from shared_runtime import actor_view
        self.submit(self.start_request())
        before = self.world.save()
        view = actor_view(self.world, self.actor, branch_id='branch-1', restore_id=self.host.restore_id)
        self.assertEqual(view['continuations'], self.view())
        raw = json.dumps(view['continuations'])
        for forbidden in ('params_digest', 'rule_digest', 'dependencies', 'certificate', 'state_digest',
                          '"stocks"', '"projects"', '"journal"', '"task"'):
            self.assertNotIn(forbidden, raw)
        self.assertEqual(self.world.save(), before)
        self.assertEqual(view['continuations']['processes'][0]['status_basis'], 'received_phase')

    def test_original_received_phase_and_snapshot_are_bound_to_actor_branch_and_restore(self):
        result = self.submit(self.start_request())
        first = self.view()
        other = api.actor_view(self.world, self.actor, branch_id='another', restore_id=self.host.restore_id)
        self.assertNotEqual(first['snapshot_id'], other['snapshot_id'])
        for reader in (lambda: api.actor_view(self.world, 'absent', branch_id='b', restore_id='r'),
            lambda: api.received_phase(self.world, 'absent', result['phase_id'], branch_id='b', restore_id='r'),
            lambda: api.status(self.world, self.actor, 'absent', branch_id='b', restore_id='r')):
            with self.assertRaises(api.PhaseUnavailable): reader()

    def test_persistence_receives_the_same_filtered_public_result_as_acknowledgment(self):
        result = self.submit(self.start_request())
        stored = json.loads(self.host.path.read_text())['receipt']
        self.assertEqual(stored, result)
        self.assertNotIn('params_digest', stored)
        self.assertIn('params_digest', self.world.s['process_phase_receipts'][result['phase_id']])

    def test_explicit_acceptance_and_persistence_are_required_before_effects(self):
        request = self.start_request(); before = self.world.save()
        for overrides in ({'explicitly_accepted': False}, {'explicitly_accepted': 1}, {'persist': None}):
            with self.assertRaises(api.PhaseUnavailable): self.submit(request, **overrides)
        self.assertEqual(self.world.save(), before)

    def test_unsupported_contexts_and_generic_tags_do_not_create_phase_capabilities(self):
        self.world.s.pop('scene_rules'); self.host.install(self.world)
        self.assertEqual(self.view()['start_options'], [])
        with self.assertRaises(api.PhaseUnavailable):
            api.prepare_start(self.world, actor=self.actor, capability_id='observe', process_id='p', phase_id='x',
                intention='Observe.', source_ref='explicit', branch_id='b', restore_id='r')

    def event(self, request):
        return {'id': 'process:'+request.phase_id, 'at': self.world.s['clock']+1,
            'op': 'continue_player_process', 'params': {
                'campaign_id': self.world.s['campaign_id'], 'source_ref': request.source_ref,
                'instruction_ref': request.intention, 'actor': request.actor, 'process_id': request.process_id,
                'phase_id': request.phase_id, 'phase_index': request.phase_index, 'command': request.command,
                'details': json.loads(request.details_json), 'intention': request.intention}}

    def test_hidden_stock_permission_and_worker_changes_do_not_select_a_winning_menu(self):
        self.rise(); original = self.view()
        self.world.apply('move-stock', self.world.s['clock']+1, 'transfer_stock',
            campaign_id=self.world.s['campaign_id'], source_ref='explicit synthetic competing custody',
            authority_ref='synthetic selected authority', **{'from': 'founder-home', 'to': 'oren-home',
            'material': 'timber', 'quantity': 5})
        self.world.s['grants']['founding']['active'] = False
        self.assertEqual(self.view(), original)

    def test_actor_control_foreign_phases_and_parent_identity_never_leak(self):
        from test_scene_actions import apply
        own = self.submit(self.start_request())
        apply(self.world, 'other', 'register_actor', actor_id='other', name='Other', species='human',
              player_controlled=True, instruction_ref='explicit synthetic other actor')
        before = self.world.save()
        other = api.actor_view(self.world, 'other', branch_id='b', restore_id='r')
        self.assertEqual(other['processes'], [])
        self.assertNotIn(own['phase_id'], json.dumps(other))
        for read in (lambda: api.received_phase(self.world, 'other', own['phase_id'], branch_id='b', restore_id='r'),
                     lambda: api.status(self.world, 'other', 'parent', branch_id='b', restore_id='r')):
            with self.assertRaises(api.PhaseUnavailable) as error: read()
            self.assertEqual(error.exception.code, 'phase_unavailable')
        self.world.s['player_actor_ids'] = ['other']
        with self.assertRaises(api.PhaseUnavailable) as error: self.view()
        self.assertEqual(error.exception.code, 'actor_denied')
        self.world.s['player_actor_ids'] = ['pc', 'other']
        self.assertEqual(self.world.save(), before)

    def test_observation_pause_resume_cancel_retains_elapsed_and_reservation(self):
        self.submit(self.start_request()); self.command('advance', {'seconds': 1})
        paused = self.command('pause')
        self.assertEqual([c['command'] for c in paused['supported_commands']], ['resume', 'cancel', 'inspect'])
        self.assertIn('pc', __import__('process_runtime').reserved_actors(self.world.s))
        resumed = self.command('resume'); self.assertEqual(resumed['worked_seconds'], 1)
        cancelled = self.command('cancel')
        self.assertEqual(cancelled['status'], 'cancelled'); self.assertEqual(cancelled['supported_commands'], [])
        self.assertNotIn('pc', __import__('process_runtime').reserved_actors(self.world.s))
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 1)
        self.assertNotIn('process-observation:'+cancelled['phase_id'], self.world.s.get('scene_action_results', {}))

    def test_work_pause_cancel_and_new_explicit_resume_keep_one_physical_project(self):
        self.rise(); self.submit(self.start_request()); self.command('advance', {'seconds': 100})
        existing_projects = set(self.world.s['projects'])
        self.command('pause'); self.command('resume'); cancelled = self.command('cancel')
        self.assertEqual(cancelled['status'], 'cancelled')
        self.assertEqual(self.world.s['projects']['shelter']['worked'], 100)
        self.submit(self.start_request(action='resume', process_id='replacement'))
        self.assertEqual(set(self.world.s['projects']), existing_projects)
        self.assertEqual(self.world.s['projects']['shelter']['worked'], 100)
        self.assertEqual(self.world.s['stocks']['founder-home']['timber'], 6)

    def test_changed_permission_holds_actual_work_and_resume_revalidates_authority(self):
        self.rise(); self.submit(self.start_request())
        original_stock = copy.deepcopy(self.world.s['stocks'])
        self.world.s['grants']['founding']['active'] = False
        self.host.install(self.world)
        held = self.command('advance', {'seconds': 100})
        self.assertEqual(held['status'], 'held'); self.assertEqual(held['worked_seconds'], 0)
        self.assertEqual([row['command'] for row in held['supported_commands']], ['pause', 'cancel', 'inspect'])
        self.assertEqual(self.world.s['stocks'], original_stock)
        self.command('pause'); request = self.command_request('resume'); before = self.world.save()
        with self.assertRaises(api.PhaseUnavailable) as error: self.submit(request)
        self.assertTrue(any(path[0] == 'grants' for path in error.exception.dependencies['reads']))
        self.assertEqual(error.exception.dependencies['writes'], [])
        self.assertEqual(self.world.save(), before)

    def test_last_received_status_and_commands_do_not_probe_live_work_and_inspect_refreshes(self):
        self.rise(); start = self.submit(self.start_request()); before = self.view()
        settlement_action(self.world, 'external-time', self.actor, 'wait_hour', 'explicit selected external advancement')
        self.assertGreater(self.world.s['projects']['shelter']['worked'], 0)
        self.assertEqual(self.view(), before)
        self.host.install(self.world)
        updated = self.command('inspect')
        self.assertGreater(updated['worked_seconds'], start['worked_seconds'])
        original = api.received_phase(self.world, self.actor, start['phase_id'],
                                     branch_id='branch-1', restore_id=self.host.restore_id)
        self.assertEqual(original, start)

    def test_changed_selected_rule_rejects_atomically_with_private_actual_reads(self):
        self.submit(self.start_request())
        self.world.s['scene_rules']['actions']['look-quay']['duration_seconds'] += 1
        self.host.install(self.world); request = self.command_request('advance', {'seconds': 1})
        before = self.world.save()
        with self.assertRaises(api.PhaseUnavailable) as error: self.submit(request)
        self.assertEqual(error.exception.code, 'process_unavailable')
        self.assertTrue(error.exception.dependencies['reads'])
        self.assertEqual(error.exception.dependencies['writes'], [])
        self.assertEqual(self.world.save(), before)

    def test_actual_success_observes_control_location_rules_and_reservations(self):
        from r9_runtime import observe
        request = self.start_request(); before = self.world.save()
        cert = observe(self.world.s, self.event(request))
        roots = {path[0] for path in cert['reads'] if path}
        self.assertTrue({'actors', 'entity_registry', 'scene_rules', 'elapsed_time', 'processes'} <= roots)
        self.assertEqual(self.world.save(), before)
        result = self.submit(request)
        self.assertEqual(self.world.checksum(), cert['post_state'])
        self.assertNotIn('certificate', json.dumps(result))

    def test_rejected_stock_attempt_keeps_actual_dependencies_private_and_no_effects(self):
        self.rise()
        self.world.apply('move-stock', self.world.s['clock']+1, 'transfer_stock',
            campaign_id=self.world.s['campaign_id'], source_ref='explicit synthetic stock change',
            authority_ref='synthetic selected authority', **{'from': 'founder-home', 'to': 'oren-home',
            'material': 'timber', 'quantity': 5})
        self.host.install(self.world); request = self.start_request(); before = self.world.save()
        with self.assertRaises(api.PhaseUnavailable) as error: self.submit(request)
        deps = error.exception.dependencies
        self.assertTrue(any(path[0] == 'stocks' for path in deps['reads']))
        self.assertFalse(deps['successful_certificate']); self.assertEqual(deps['writes'], [])
        self.assertEqual(str(error.exception), 'process_unavailable')
        self.assertEqual(self.world.save(), before)

    def test_scarce_stock_and_parent_claims_have_no_arrival_order_frontier_winner(self):
        from r9_runtime import frontier
        self.rise(); request = self.start_request(); start = self.event(request)
        move = {'id': 'competing-stock', 'at': start['at'], 'op': 'transfer_stock', 'params': {
            'campaign_id': self.world.s['campaign_id'], 'source_ref': 'explicit synthetic claim',
            'authority_ref': 'synthetic selected authority', 'from': 'founder-home', 'to': 'oren-home',
            'material': 'timber', 'quantity': 5}}
        saved = self.world.save()
        for events in ([start, move], [move, start]):
            world = CoreWorld.load(saved); result = frontier(world, events)
            self.assertEqual(result['committed'], [])
            self.assertEqual(set(result['deferred']), {start['id'], move['id']})
            self.assertEqual(world.s['stocks'], self.world.s['stocks'])
            self.assertNotIn('shelter', world.s['projects'])

    def test_two_observations_cannot_book_the_same_actor_by_event_id_order(self):
        from r9_runtime import frontier
        first = self.event(self.start_request(process_id='one'))
        second = self.event(self.start_request(process_id='two'))
        for events in ([first, second], [second, first]):
            world = CoreWorld.load(self.world.save()); result = frontier(world, events)
            self.assertEqual(result['committed'], [])
            self.assertEqual(set(result['deferred']), {first['id'], second['id']})
            self.assertFalse(world.s.get('processes', {}))

    def test_invalid_commands_spans_and_travel_adapter_do_not_commit(self):
        request = self.start_request(); before = self.world.save()
        forged = replace(request, details_json=json.dumps({'kind': 'travel', 'action_id': 'walk_clearing'}))
        with self.assertRaises(api.PhaseUnavailable): self.submit(forged)
        self.assertEqual(self.world.save(), before)
        self.submit(request); before = self.world.save()
        for value in (0, -1, True, 0.5):
            with self.assertRaises(api.PhaseUnavailable): self.command_request('advance', {'seconds': value})
        with self.assertRaises(api.PhaseUnavailable): self.command_request('invented_action')
        self.assertEqual(self.world.save(), before)

    def test_stale_request_and_scope_refuse_before_any_new_phase_effect(self):
        request = self.start_request()
        from test_scene_actions import execute
        execute(self.world, 'look-quay', 'other-time'); self.host.install(self.world)
        before = self.world.save()
        with self.assertRaises(api.PhaseUnavailable) as error: self.submit(request)
        self.assertEqual(error.exception.code, 'stale_state')
        with self.assertRaises(api.PhaseUnavailable) as error:
            self.submit(request, current_scope=replace(self.scope(), branch_id='other'))
        self.assertEqual(error.exception.code, 'stale_scope')
        self.assertEqual(self.world.save(), before)

    def test_failed_save_leaves_world_unchanged_and_exact_retry_can_commit(self):
        request = self.start_request(); before = self.world.save()
        def fail(*args): raise OSError('synthetic failed save')
        with self.assertRaises(OSError): self.submit(request, persist=fail)
        self.assertEqual(self.world.save(), before)
        self.assertEqual(self.submit(request)['phase_id'], request.phase_id)
        self.assertEqual(self.host.writes, 1)

    def test_lost_ack_restart_and_terminal_replay_return_original_public_receipt(self):
        request = self.start_request(); pending = Path(self.temp.name)/'pending.json'
        pending.write_text(request.to_json())
        def lose_ack(*args): self.host.persist(*args); raise OSError('synthetic lost acknowledgment')
        with self.assertRaises(OSError): self.submit(request, persist=lose_ack)
        self.world = self.host.load(); request = ProcessRequest.from_json(pending.read_text())
        original = self.submit(request)
        self.assertEqual(original, json.loads(self.host.path.read_text())['receipt'])
        self.command('advance', {'seconds': 3}); self.world = self.host.load()
        before = self.world.save()
        self.assertEqual(self.submit(request), original)
        self.assertEqual(self.world.save(), before)
        self.assertEqual(self.host.writes, 2)

    def test_restore_fences_discarded_future_and_new_request_resumes_saved_progress(self):
        self.submit(self.start_request()); saved = self.world.save()
        discarded = self.command_request('advance', {'seconds': 1}); self.submit(discarded)
        self.world = CoreWorld.load(saved); self.host.restore_id = 'restore-2'; self.host.install(self.world)
        before = self.world.save()
        with self.assertRaises(api.PhaseUnavailable) as error: self.submit(discarded)
        self.assertEqual(error.exception.code, 'stale_scope'); self.assertEqual(self.world.save(), before)
        result = self.command('advance', {'seconds': 1}); self.assertEqual(result['worked_seconds'], 1)

    def test_concurrent_host_delivery_commits_one_phase_and_one_elapsed_span(self):
        self.submit(self.start_request()); request = self.command_request('advance', {'seconds': 1})
        saved = self.world.save()
        def deliver(_):
            world = CoreWorld.load(saved)
            try:
                return api.execute(world, request, current_scope=request.scope,
                                   persist=self.host.persist, explicitly_accepted=True)
            except api.PhaseUnavailable as error: return error.code
        with ThreadPoolExecutor(2) as workers: results = list(workers.map(deliver, range(2)))
        self.assertEqual(sum(isinstance(r, dict) for r in results), 1)
        self.world = self.host.load()
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 1)
        self.assertEqual(self.submit(request), next(r for r in results if isinstance(r, dict)))

    def test_changed_replay_intention_details_or_parent_cannot_rewrite_identity(self):
        request = self.start_request(); self.submit(request); before = self.world.save()
        for changed in (replace(request, intention='Changed intention'), replace(request, process_id='different'),
                        replace(request, details_json='{}')):
            with self.assertRaises(api.PhaseUnavailable) as error: self.submit(changed)
            self.assertEqual(error.exception.code, 'request_identity_conflict')
        self.assertEqual(self.world.save(), before)

    def test_no_selected_time_axis_and_no_received_map_mean_no_observation_adapter(self):
        self.world.s['elapsed_time']['axis'] = 'unselected-axis'
        self.assertEqual(self.view()['start_options'], [])
        self.world = scene_fixture(); self.world.s['knowledge']['pc'].pop('setup:scene-map')
        self.assertEqual(self.view()['start_options'], [])

    def test_public_dto_mutation_and_literal_fallback_do_not_change_core(self):
        self.submit(self.start_request()); before = self.world.save()
        view = self.view(); view['processes'][0]['summary'] = 'Changed display'
        view['processes'][0]['supported_commands'].clear()
        self.assertEqual(self.world.save(), before)
        self.assertNotEqual(self.view(), view)
        with patch('response_depot._depot', side_effect=OSError('synthetic missing text')):
            result = self.command('advance', {'seconds': 1})
            self.assertEqual(result['presentation']['mode'], 'literal_receipt')
            self.assertEqual(result['presentation']['text'], result['receipt']['exact_text'])
            self.assertEqual(result['presentation']['render_usage'], {'provider_calls': 0, 'model_tokens': 0})


if __name__ == '__main__': unittest.main()
