"""Synthetic selected channels; actual Core effects, received facts and host CAS."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import communication_contract as api
import communication_runtime as native
from core_world import CoreWorld
from r9_runtime import frontier, grant
from runtime_contracts import WorldScope
from settlement_setup import initialize, preview
from test_scene_actions import apply, fixture as scene_fixture
from test_settlement import choices
from test_solo_provider import AtomicTestHost


class CommunicationContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        c = choices(); c['permission'] = 'held'
        self.world = initialize(c, preview(c)['review_digest'], 'communication-contract-fixture')
        # This synthetic fixture tests an unreceived channel roster; ordinary
        # starts separately receive both reviewed introductions.
        for speaker in ('elin', 'oren'):
            self.world.s['knowledge']['founder'].pop('setup:local-introduction:' + speaker)
        self.world.s['player_actor_ids'].append('oren')  # Explicit dual control for the test only.
        for actor in ('founder', 'oren'):
            grant(self.world, actor+'-custody', actor, ['transfer_stock'], self.world.s['clock']+1,
                  'synthetic selected custody')
        self.world.s['communication_rules'] = {'schema_version': 1, 'source_ref': 'synthetic reviewed channel',
            'time_model': 'causal_only_no_elapsed_rule', 'stock_profile': 'settlement_free_stock',
            'channels': {'local': {'mode': 'co_located', 'actors': ['founder', 'oren', 'elin']}},
            'stock_authorities': {'founder-custody': ['founder-home'], 'oren-custody': ['oren-home']}}
        self.introduce('founder', 'oren'); self.introduce('oren', 'founder')
        self.host = AtomicTestHost(self.temp.name, self.world); self.counter = 0
        for target in ('solo_provider.CapabilityBroker.dispatch',
                       'openai_proposals.OpenAIProposalTransport.__call__', 'socket.socket.connect'):
            blocker = patch(target, side_effect=AssertionError('No inference/network in communication contract'))
            blocker.start(); self.addCleanup(blocker.stop)

    def introduce(self, listener, speaker):
        key = 'introduction:'+listener+':'+speaker
        apply(self.world, key, 'record_evidence', evidence_id=key, subject=listener,
              originator=speaker, assertion='Exact unverified introduction from '+speaker+'.', status='testimony')
        apply(self.world, key+':received', 'receive_evidence', evidence_id=key, recipient=listener)
        return key

    def scope(self):
        return WorldScope(self.world.s['campaign_id'], 'branch-1', self.host.restore_id, self.world.checksum())

    def view(self, actor='founder'):
        return api.actor_view(self.world, actor, branch_id='branch-1', restore_id=self.host.restore_id)

    def request(self, command='speak', details=None, actor='founder', text=None):
        self.counter += 1
        return api.prepare(self.world, request_id='speech-'+str(self.counter), actor=actor,
            recipient='oren' if actor == 'founder' else 'founder', channel_id='local', command=command,
            details=details if details is not None else {}, intention=text or 'Exact edited '+command+' intention.',
            source_ref='synthetic explicit communication', branch_id='branch-1', restore_id=self.host.restore_id)

    def submit(self, request, **overrides):
        args = dict(current_scope=self.scope(), persist=self.host.persist, explicitly_accepted=True)
        args.update(overrides)
        return api.execute(self.world, request, **args)

    def act(self, command='speak', details=None, **kw):
        return self.submit(self.request(command, details, **kw))

    def terms(self, actor='founder', quantity=2):
        return {'from': actor+'-home', 'to': 'oren-home' if actor == 'founder' else 'founder-home',
                'material': 'grain', 'quantity': quantity, 'authority_id': actor+'-custody'}

    def offer(self, key='offer-1', **kw):
        return self.act('offer', {'offer_id': key, 'terms': self.terms(**kw)})

    def close(self, command, offered, actor='oren'):
        return self.act(command, {'offer_id': offered['offer_id'], 'terms_digest': offered['terms_digest']}, actor=actor)

    def status(self, key='offer-1', actor='founder'):
        return api.offer_status(self.world, actor, key, branch_id='branch-1', restore_id=self.host.restore_id)

    def commands(self, key='offer-1', actor='founder'):
        return [r['command'] for r in self.status(key, actor)['supported_commands']]

    def rejected(self, fn, code='communication_unavailable'):
        before = self.world.save()
        with self.assertRaises(api.CommunicationUnavailable) as caught: fn()
        self.assertEqual(caught.exception.code, code)
        self.assertEqual(self.world.save(), before)
        return caught.exception

    def test_participants_require_received_attribution_and_do_not_parse_words_or_channel_roster(self):
        before = self.world.save(); view = self.view()
        participants = view['channels'][0]['participants']
        self.assertEqual([p['actor_id'] for p in participants], ['oren'])
        self.assertEqual(participants[0]['source_record_ids'], ['introduction:founder:oren'])
        self.assertEqual(participants[0]['supported_commands'], ['speak', 'offer'])
        self.assertEqual(self.world.save(), before)
        self.rejected(lambda: api.prepare(self.world, request_id='hidden-person', actor='founder', recipient='elin',
            channel_id='local', command='speak', details={}, intention='I speak to Elin.', source_ref='explicit',
            branch_id='branch-1', restore_id=self.host.restore_id))

    def test_source_contract_preserves_exact_testimony_attribution_and_both_information_sources(self):
        source = next(r for r in api.received_sources(self.world, 'founder')['records']
                      if r['record_id'] == 'introduction:founder:oren')
        self.assertEqual(source['status'], 'testimony'); self.assertEqual(source['originator'], 'oren')
        self.assertEqual(source['text'], 'Exact unverified introduction from oren.')
        self.assertEqual(source['source_ref'], 'synthetic-opening-selection')
        self.assertEqual(source['receipt_source_ref'], 'synthetic-opening-selection')
        self.assertLess(source['recorded_at'], source['received_at'])
        self.assertEqual(source['time_axis'], 'causal_sequence')
        source['text'] = 'changed copy'
        self.assertNotEqual(api.received_sources(self.world, 'founder')['records'][-1]['text'], 'changed copy')

    def test_hidden_stock_permissions_presence_and_unreceived_evidence_do_not_choose_a_menu(self):
        before = self.view()
        self.world.s['actors']['oren']['current']['location'] = 'PRIVATE_REMOTE_PLACE'
        self.world.s['r9']['mandates']['founder-custody']['active'] = False
        self.world.s['stocks']['founder-home']['grain'] = 0
        # Stock mutation uses an explicitly balanced synthetic fixture, not a transfer.
        self.world.s['stocks']['oren-home']['grain'] += 12
        apply(self.world, 'hidden', 'record_evidence', evidence_id='PRIVATE_EVIDENCE', subject='elin',
              assertion='PRIVATE_SECRET', status='established', originator='elin')
        self.assertEqual(self.view(), before)

    def test_no_selected_or_supported_channel_is_explicitly_empty(self):
        for mutation in ('missing', 'unsupported_time', 'unsupported_mode'):
            world = CoreWorld.load(self.world.save())
            if mutation == 'missing': del world.s['communication_rules']
            elif mutation == 'unsupported_time': world.s['communication_rules']['time_model'] = 'invented'
            else: world.s['communication_rules']['channels']['local']['mode'] = 'remote'
            self.assertEqual(api.actor_view(world, 'founder', branch_id='b', restore_id='r')['channels'], [])

    def test_non_rise_selected_local_testimony_uses_same_core_without_inventing_stock_or_time(self):
        self.world = scene_fixture()
        apply(self.world, 'witness', 'register_actor', actor_id='witness', name='Synthetic witness',
              species='human', player_controlled=False)
        self.world.s['actors']['witness']['current']['location'] = 'quay'
        self.introduce('pc', 'witness')
        self.world.s['communication_rules'] = {'schema_version': 1, 'source_ref': 'synthetic quay channel',
            'time_model': 'causal_only_no_elapsed_rule',
            'channels': {'quay': {'mode': 'co_located', 'actors': ['pc', 'witness']}}}
        self.host.install(self.world); before = copy.deepcopy(self.world.s['elapsed_time'])
        self.assertEqual(api.actor_view(self.world, 'pc', branch_id='branch-1', restore_id='restore-1')
                         ['channels'][0]['participants'][0]['supported_commands'], ['speak'])
        request = api.prepare(self.world, request_id='quay-speech', actor='pc', recipient='witness',
            channel_id='quay', command='speak', details={}, intention='I cannot verify that claim.',
            source_ref='synthetic quay words', branch_id='branch-1', restore_id='restore-1')
        result = self.submit(request)
        self.assertEqual(result['truth_status'], 'testimony')
        self.assertEqual(result['utterance'], request.intention)
        self.assertEqual(self.world.s['elapsed_time'], before)
        self.assertEqual(result['elapsed_status'], 'not_resolved')

    def test_preparation_and_words_of_acceptance_do_not_transfer_or_accept(self):
        offered = self.offer(); before = self.world.save()
        request = self.request('speak', actor='oren', text='I accept and own all the grain.\nStill exact words.')
        self.assertEqual(self.world.save(), before)
        stocks = copy.deepcopy(self.world.s['stocks']); result = self.submit(request)
        self.assertEqual(result['utterance'], request.intention)
        self.assertEqual(self.status()['status'], 'offered')
        self.assertEqual(self.world.s['stocks'], stocks)
        self.assertEqual(offered['status'], 'offered')

    def test_offer_creation_ignores_hidden_feasibility_and_preserves_exact_terms(self):
        offered = self.offer(quantity=1000)
        self.assertEqual(offered['terms']['quantity'], 1000)
        self.assertEqual(self.commands(actor='oren'), ['accept', 'decline', 'counteroffer'])
        self.assertEqual(self.commands(), ['withdraw'])
        self.assertEqual(self.world.s['stocks']['founder-home']['grain'], 12)
        error = self.rejected(lambda: self.close('accept', offered))
        self.assertTrue(error.dependencies['reads']); self.assertEqual(error.dependencies['writes'], [])

    def test_acceptance_is_explicit_conserved_and_persisted_with_same_safe_dto(self):
        offered = self.offer(); stocks = copy.deepcopy(self.world.s['stocks'])
        result = self.close('accept', offered)
        self.assertEqual(result['status'], 'fulfilled'); self.assertEqual(self.commands(), [])
        self.assertEqual(self.world.s['stocks']['founder-home']['grain'], stocks['founder-home']['grain']-2)
        self.assertEqual(self.world.s['stocks']['oren-home']['grain'], stocks['oren-home']['grain']+2)
        self.assertEqual(json.loads(self.host.path.read_text())['receipt'], result)
        self.assertEqual(self.host.load().save(), self.world.save())

    def test_decline_withdraw_and_counteroffer_retain_distinct_received_meanings(self):
        offered = self.offer(); self.close('decline', offered)
        self.assertEqual(self.status()['status'], 'declined')
        offered = self.offer('offer-2'); self.close('withdraw', offered, actor='founder')
        self.assertEqual(self.status('offer-2')['status'], 'withdrawn')
        self.offer('offer-3'); stocks = copy.deepcopy(self.world.s['stocks'])
        counter = self.act('counteroffer', {'offer_id': 'counter', 'counter_to': 'offer-3',
            'terms': self.terms('oren', 1)}, actor='oren')
        self.assertEqual(self.status('offer-3')['status'], 'superseded')
        self.assertEqual(self.status('counter')['status'], 'offered')
        self.assertEqual(counter['supersedes'], 'offer-3'); self.assertEqual(self.world.s['stocks'], stocks)
        self.assertEqual(self.commands('counter'), ['accept', 'decline', 'counteroffer'])

    def test_received_status_does_not_probe_live_obligation_or_append_remote_updates(self):
        offered = self.offer(); before = self.view()
        self.world.s['obligations']['offer-1'].update(status='withdrawn', closing_intention='PRIVATE_REMOTE')
        self.assertEqual(self.view(), before)
        self.assertEqual(self.status()['status'], 'offered')
        self.host.install(self.world)
        self.rejected(lambda: self.close('accept', offered))
        self.assertEqual(self.status()['status'], 'offered')

    def test_original_offer_receipt_stays_offered_after_fulfillment(self):
        offered = self.offer(); self.close('accept', offered)
        original = api.received_communication(self.world, 'founder', offered['request_id'],
            branch_id='branch-1', restore_id=self.host.restore_id)
        self.assertEqual(original, offered)
        self.assertEqual(self.status()['status'], 'fulfilled')

    def test_only_received_terminal_status_is_projected(self):
        offered = self.offer(); self.close('withdraw', offered, actor='founder')
        self.assertEqual(self.commands(actor='oren'), [])
        self.rejected(lambda: self.close('accept', offered))
        self.assertEqual(self.world.s['obligations']['offer-1']['status'], 'withdrawn')

    def test_current_authority_is_checked_by_core_and_rejected_reads_stay_private(self):
        offered = self.offer(); self.world.s['r9']['mandates']['founder-custody']['active'] = False
        self.host.install(self.world)
        self.assertEqual(self.commands(actor='oren'), ['accept', 'decline', 'counteroffer'])
        error = self.rejected(lambda: self.close('accept', offered))
        self.assertTrue(any('mandates' in str(r) for r in error.dependencies['reads']))
        self.assertEqual(str(error), 'communication_unavailable')
        self.assertNotIn('dependencies', json.dumps(self.view('oren')))

    def test_current_offerer_control_is_rechecked_without_hiding_received_offer(self):
        offered = self.offer(); self.world.s['player_actor_ids'].remove('founder'); self.host.install(self.world)
        self.assertEqual(self.status(actor='oren')['status'], 'offered')
        self.rejected(lambda: self.close('accept', offered))
        self.rejected(lambda: self.view(), 'actor_denied')

    def test_actual_colocation_rejects_without_publishing_hidden_whereabouts(self):
        request = self.request()
        self.world.s['actors']['oren']['current']['location'] = 'PRIVATE_REMOTE'
        self.host.install(self.world); request = replace(request, scope=self.scope())
        error = self.rejected(lambda: self.submit(request))
        self.assertTrue(error.dependencies['reads'])
        self.assertNotIn('PRIVATE_REMOTE', json.dumps(self.view()))

    def test_changed_selected_policy_cannot_silently_fulfill_original_offer(self):
        offered = self.offer(); self.world.s['communication_rules']['source_ref'] = 'new reviewed policy'
        self.host.install(self.world)
        self.rejected(lambda: self.close('accept', offered))
        self.assertEqual(self.status()['terms'], offered['terms'])

    def test_private_fields_and_hidden_actor_records_do_not_enter_public_result_or_shared_view(self):
        from shared_runtime import actor_view
        result = self.act(); before = self.world.save()
        public = actor_view(self.world, 'founder', branch_id='branch-1', restore_id=self.host.restore_id)
        self.assertEqual(public['communications'], self.view())
        for forbidden in ('params_digest', 'rule_digest', 'dependencies', 'certificate', 'state_digest',
                          '"stocks"', '"obligations"', '"journal"', '"mandates"'):
            self.assertNotIn(forbidden, json.dumps([result, public['communications']]))
        self.assertEqual(self.world.save(), before)

    def test_forwarded_testimony_does_not_reveal_structured_offer_terms_or_audience(self):
        offered = self.offer(); self.world.s['player_actor_ids'].append('elin')
        apply(self.world, 'forwarded', 'receive_evidence', evidence_id=offered['evidence_id'], recipient='elin')
        view = self.view('elin')
        self.assertEqual(view['offers'], [])
        self.assertEqual([p['actor_id'] for p in view['channels'][0]['participants']], ['founder'])
        self.rejected(lambda: api.received_communication(self.world, 'elin', offered['request_id'],
            branch_id='branch-1', restore_id=self.host.restore_id))

    def test_legacy_receipt_apis_also_keep_forwarded_words_separate_from_private_contract(self):
        from offline_responses import render_receipt
        from shared_runtime import committed_receipt
        from solo_provider import CapabilityUnavailable
        offered = self.offer(); self.world.s['player_actor_ids'].append('elin')
        apply(self.world, 'forwarded', 'receive_evidence', evidence_id=offered['evidence_id'], recipient='elin')
        self.assertEqual(native.received(self.world, 'elin'), [])
        with self.assertRaises(CapabilityUnavailable): native.presentation(self.world, 'elin', offered['request_id'])
        with self.assertRaises(ValueError): render_receipt(self.world, 'elin', 'communication:'+offered['request_id'])
        with self.assertRaises(ValueError): committed_receipt(self.world, 'elin', 'communication:'+offered['request_id'],
            branch_id='branch-1', restore_id=self.host.restore_id)
        sources = api.received_sources(self.world, 'elin')['records']
        self.assertEqual(sources[-1]['text'], offered['utterance'])

    def test_foreign_or_unreceived_sources_and_requests_are_unavailable(self):
        result = self.act()
        self.rejected(lambda: self.view('elin'), 'actor_denied')
        self.rejected(lambda: api.received_sources(self.world, 'elin'), 'actor_denied')
        self.rejected(lambda: api.received_communication(self.world, 'founder', 'unknown',
            branch_id='b', restore_id='r'))
        self.rejected(lambda: self.status('unknown'))
        self.assertEqual(api.received_communication(self.world, 'oren', result['request_id'],
            branch_id='branch-1', restore_id=self.host.restore_id)['utterance'], result['utterance'])

    def test_acceptance_and_persistence_are_mandatory(self):
        request = self.request()
        for value in (False, None, 1, 'true'):
            self.rejected(lambda: self.submit(request, explicitly_accepted=value), 'acceptance_required')
        self.rejected(lambda: self.submit(request, persist=None), 'persistence_required')

    def test_malformed_terms_unsupported_commands_and_changed_digest_fail_closed(self):
        self.rejected(lambda: self.request('teleport'), 'invalid_command')
        self.rejected(lambda: self.request(details={'hidden': 'claim'}), 'invalid_command')
        terms = self.terms(); terms['quantity'] = True
        self.rejected(lambda: self.request('offer', {'offer_id': 'bad', 'terms': terms}), 'invalid_command')
        self.offer()
        self.rejected(lambda: self.request('accept', {'offer_id': 'offer-1', 'terms_digest': 'changed'}, actor='oren'), 'invalid_command')

    def test_source_window_is_explicitly_bounded_and_detached(self):
        self.act()
        rows = api.received_sources(self.world, 'founder', limit=1)
        self.assertEqual(len(rows['records']), 1); self.assertGreater(rows['total'], 1)
        self.assertTrue(rows['truncated'])
        for limit in (0, True, 129):
            self.rejected(lambda: api.received_sources(self.world, 'founder', limit=limit), 'invalid_limit')

    def test_snapshot_tracks_actor_branch_restore_and_received_status_not_private_state(self):
        first = self.view()
        for branch, restore in (('other', self.host.restore_id), ('branch-1', 'other')):
            self.assertNotEqual(first['snapshot_id'], api.actor_view(self.world, 'founder',
                branch_id=branch, restore_id=restore)['snapshot_id'])
        self.assertNotEqual(first['snapshot_id'], self.view('oren')['snapshot_id'])
        self.act(); self.assertNotEqual(first['snapshot_id'], self.view()['snapshot_id'])

    def test_failed_host_save_leaves_stock_evidence_and_offer_unchanged(self):
        offered = self.offer(); request = self.request('accept',
            {'offer_id': 'offer-1', 'terms_digest': offered['terms_digest']}, actor='oren')
        before, disk = self.world.save(), self.host.path.read_bytes()
        def fail(*args): raise OSError('synthetic disk failure')
        with self.assertRaises(OSError): self.submit(request, persist=fail)
        self.assertEqual(self.world.save(), before); self.assertEqual(self.host.path.read_bytes(), disk)

    def test_pending_json_restart_lost_ack_and_terminal_replay_transfer_only_once(self):
        offered = self.offer(); request = self.request('accept',
            {'offer_id': 'offer-1', 'terms_digest': offered['terms_digest']}, actor='oren')
        pending = Path(self.temp.name)/'pending.json'; pending.write_text(request.to_json())
        def lost(scope, save, public):
            self.host.persist(scope, save, public); raise OSError('synthetic lost ack')
        before = self.world.save()
        with self.assertRaises(OSError): self.submit(request, persist=lost)
        self.assertEqual(self.world.save(), before)
        self.world = self.host.load(); request = native.CommunicationRequest.from_json(pending.read_text())
        saved, writes = self.world.save(), self.host.writes
        result = self.submit(request)
        self.assertEqual(result, json.loads(self.host.path.read_text())['receipt'])
        self.assertEqual(self.world.save(), saved); self.assertEqual(self.host.writes, writes)
        self.assertEqual(self.world.s['stocks']['founder-home']['grain'], 10)

    def test_restore_branch_and_stale_state_fences_reject_discarded_future(self):
        saved = self.world.save(); request = self.request(); self.submit(request)
        self.world = CoreWorld.load(saved); self.host.restore_id = 'restore-2'; self.host.install(self.world)
        self.rejected(lambda: self.submit(request), 'stale_scope')
        request = self.request()
        self.rejected(lambda: self.submit(request, current_scope=replace(self.scope(), branch_id='other')), 'stale_scope')
        self.act(); self.rejected(lambda: self.submit(request), 'stale_state')

    def test_changed_replay_identity_cannot_change_words_terms_or_recipient(self):
        request = self.request(); self.submit(request)
        for changed in (replace(request, intention='changed'), replace(request, recipient='elin'),
                        replace(request, details_json='{"quantity":10}'), replace(request, command='offer')):
            self.rejected(lambda: self.submit(changed), 'request_identity_conflict')

    def test_concurrent_acceptance_persists_one_conserved_result(self):
        offered = self.offer(); request = self.request('accept',
            {'offer_id': 'offer-1', 'terms_digest': offered['terms_digest']}, actor='oren')
        saved, scope = self.world.save(), self.scope()
        def submit(_):
            try: return api.execute(CoreWorld.load(saved), request, current_scope=scope,
                                    persist=self.host.persist, explicitly_accepted=True)
            except api.CommunicationUnavailable as error: return error.code
        with ThreadPoolExecutor(2) as pool: results = list(pool.map(submit, range(2)))
        self.assertEqual(sum(isinstance(r, dict) for r in results), 1)
        self.assertEqual(self.host.load().s['stocks']['founder-home']['grain'], 10)

    def test_late_failure_rolls_back_transfer_with_actual_attempted_dependencies(self):
        offered = self.offer(); request = self.request('accept',
            {'offer_id': 'offer-1', 'terms_digest': offered['terms_digest']}, actor='oren')
        apply(self.world, 'collision', 'record_evidence', evidence_id='communication:'+request.request_id,
              subject='founder', assertion='Unrelated prior evidence.', status='testimony')
        self.host.install(self.world); request = replace(request, scope=self.scope())
        error = self.rejected(lambda: self.submit(request))
        self.assertTrue(error.dependencies['attempted_writes']); self.assertEqual(error.dependencies['writes'], [])

    def test_competing_offer_acceptances_defer_both_in_either_frontier_order(self):
        offered = [self.offer('scarce-'+str(i), quantity=10) for i in range(2)]
        events = []
        for row in offered:
            request = self.request('accept', {'offer_id': row['offer_id'], 'terms_digest': row['terms_digest']}, actor='oren')
            events.append({'id': 'communication:'+request.request_id, 'at': self.world.s['clock']+1,
                'op': native.OPERATION, 'params': {'campaign_id': self.world.s['campaign_id'],
                    'source_ref': request.source_ref, 'instruction_ref': request.intention, 'actor': request.actor,
                    'recipient': request.recipient, 'request_id': request.request_id, 'channel_id': request.channel_id,
                    'command': request.command, 'details': json.loads(request.details_json), 'intention': request.intention}})
        before = self.world.save()
        for ordered in (events, list(reversed(events))):
            world = CoreWorld.load(before); result = frontier(world, ordered)
            self.assertEqual(result['committed'], [])
            self.assertEqual(world.s['stocks'], self.world.s['stocks'])
            self.assertTrue(all(world.s['obligations'][r['offer_id']]['status'] == 'offered' for r in offered))

    def test_missing_text_preserves_actual_literal_outcome_without_inference(self):
        with patch('response_depot._depot', side_effect=OSError('PRIVATE_MISSING_TEXT')):
            result = self.act(text='Exact words are still testimony.')
        self.assertEqual(result['presentation']['mode'], 'literal_receipt')
        self.assertIn(result['utterance'], result['presentation']['text'])
        self.assertNotIn('PRIVATE_MISSING_TEXT', json.dumps(result))
        self.assertEqual(self.view()['render_usage'], {'provider_calls': 0, 'model_tokens': 0})


if __name__ == '__main__':
    unittest.main()
