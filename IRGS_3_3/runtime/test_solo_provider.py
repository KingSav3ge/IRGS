"""Offline SOLO boundary evidence. Real Core effects; no inference/network calls."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import json
import os
from pathlib import Path
import tempfile
import threading
import time
import unittest

from core_world import CoreWorld
from irgs_reference import canon
from solo_actions import accept_proposal, prepare_request
from solo_provider import (ActorRequest, AttemptLedger, CapabilityBroker, CapabilityUnavailable,
    Route, SCHEMA_VERSION, SpecialistRegistry, TransportReply, WorldScope)
from test_scene_actions import apply, fixture, execute


def route(**changes):
    return replace(Route('offline', 'synthetic', 'none', 'in-process', 'fixture-v1', 'v1',
        'config-v1', 'synthetic-transfer-approved-v1', 'synthetic-ceiling-v1', 10,
        enabled=True, approval_ref='test-only-not-live', lifecycle='qualified',
        tested_capabilities=(SCHEMA_VERSION,)), **changes)


class FakeTransport:
    def __init__(self, action='enter-passage', *, change=None, block=None, entered=None):
        self.action, self.change, self.block, self.entered = action, change, block, entered
        self.calls = 0
        self.inputs = []
        self.lock = threading.Lock()

    def __call__(self, model_input, selected_route, **limits):
        with self.lock:
            self.calls += 1
            self.inputs.append(model_input)
        if self.entered:
            self.entered.set()
        if self.block:
            self.block.wait(2)
        body = {'intention': model_input['intention'], 'action_id': self.action,
                'source_refs': model_input['source_refs'][:1]}
        reply = TransportReply(canon(body), canon(selected_route.identity()),
                               canon({'input_tokens': 23, 'output_tokens': 18}), 'synthetic-attempt')
        return self.change(reply) if self.change else reply


class AtomicTestHost:
    """Temporary synthetic host save/receipt CAS, not a production persistence API."""
    def __init__(self, root, world):
        self.path = Path(root) / 'temporary-campaign.json'
        self.lock = threading.Lock()
        self.restore_id = 'restore-1'
        self.writes = 0
        self.install(world)

    def install(self, world):
        self.path.write_text(canon({'save': world.save(), 'branch_id': 'branch-1',
                                   'restore_id': self.restore_id, 'receipt': None}))

    def load(self):
        return CoreWorld.load(json.loads(self.path.read_text())['save'])

    def persist(self, expected, candidate_save, receipt):
        with self.lock:
            current = json.loads(self.path.read_text())
            world = CoreWorld.load(current['save'])
            actual = WorldScope(world.s['campaign_id'], current['branch_id'],
                                current['restore_id'], world.checksum())
            if expected != actual:
                raise CapabilityUnavailable('host_compare_failed')
            candidate = CoreWorld.load(candidate_save)
            temporary = self.path.with_suffix('.pending')
            with temporary.open('w') as stream:
                stream.write(canon({'save': candidate.save(), 'branch_id': current['branch_id'],
                    'restore_id': current['restore_id'], 'receipt': receipt}))
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, self.path)
            self.writes += 1


class SoloProviderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.world = fixture()
        self.host = AtomicTestHost(self.temp.name, self.world)
        self.ledger = AttemptLedger(Path(self.temp.name) / 'attempts.sqlite', budget_units=100,
                                    max_inflight=2)
        self.registry = SpecialistRegistry([route()])
        self.broker = CapabilityBroker(self.registry, self.ledger, enabled=True, scope_reader=self.scope)

    def scope(self, request):
        return WorldScope(self.world.s['campaign_id'], 'branch-1', self.host.restore_id,
                          self.world.checksum())

    def request(self, key='request-1', **changes):
        args = dict(request_id=key, actor_id='pc', intention='I take the passage to the desk.',
                    branch_id='branch-1', restore_id='restore-1', allowed_routes=('offline',),
                    classification='synthetic-approved', policy_ref='synthetic-transfer-approved-v1',
                    config_version='config-v1', deadline=time.time() + 20)
        args.update(changes)
        return prepare_request(self.world, **args)

    def propose(self, request=None, transport=None):
        request = request or self.request()
        transport = transport or FakeTransport()
        result = self.broker.dispatch(request, 'offline', transport)
        self.assertEqual(result.status, 'proposal_ready', result)
        return request, result.proposal

    def accept(self, request, proposal, **changes):
        args = dict(request_id=request.request_id, proposal_digest=proposal.proposal_digest,
            actor_id='pc', intention=request.intention, branch_id='branch-1', restore_id='restore-1',
            explicitly_accepted=True, persist=self.host.persist, clock=time.time)
        args.update(changes)
        return accept_proposal(self.world, self.ledger, **args)

    def assert_code(self, code, fn):
        before = self.world.save()
        with self.assertRaises(CapabilityUnavailable) as error:
            fn()
        self.assertEqual(error.exception.code, code)
        self.assertEqual(self.world.save(), before)

    def test_default_broker_and_candidate_route_are_disabled(self):
        fake = FakeTransport()
        result = CapabilityBroker(self.registry, self.ledger).dispatch(self.request(), 'offline', fake)
        self.assertEqual(result.code, 'provider_disabled')
        self.registry.routes['offline'] = route(enabled=False)
        self.assertEqual(self.broker.dispatch(self.request(), 'offline', fake).code, 'provider_disabled')
        self.assertEqual(fake.calls, 0)
        self.assertIsNone(self.ledger.lookup('request-1'))

    def test_missing_policy_identity_price_or_capability_denies_dispatch(self):
        for changes in ({'policy_ref': ''}, {'host': ''}, {'price_revision': ''},
                        {'tested_capabilities': ()}, {'approval_ref': ''},
                        {'lifecycle': 'deprecated'}, {'classifications': ()}, {'workloads': ()}):
            with self.subTest(changes=changes):
                self.registry.routes['offline'] = route(**changes)
                fake = FakeTransport()
                self.assertEqual(self.broker.dispatch(self.request(), 'offline', fake).status, 'unavailable')
                self.assertEqual(fake.calls, 0)

    def test_received_context_does_not_expose_world_or_hidden_facts(self):
        self.world.s['site_conditions']['quay-gate']['passable'] = True
        first = self.request()
        self.world.s['site_conditions']['quay-gate']['passable'] = False
        self.world.s['private_oracle'] = {'answer': 'EVALUATOR-ONLY-SECRET'}
        apply(self.world, 'secret', 'record_evidence', evidence_id='hidden', subject='pc',
              assertion='PRIVATE UNRECEIVED ASSERTION', status='testimony')
        second = self.request()
        self.assertEqual(first.model_input(), second.model_input())
        fake = FakeTransport()
        before = self.world.save()
        self.propose(second, fake)
        serialized = canon(fake.inputs)
        for private in ('EVALUATOR-ONLY', 'PRIVATE UNRECEIVED', 'site_conditions', 'state_digest',
                        'journal', 'stock', 'scene_rules'):
            self.assertNotIn(private, serialized)
        self.assertEqual(self.world.save(), before)
        fake.inputs[0]['context']['received'].clear()
        self.assertTrue(second.model_input()['context']['received'])

    def test_foreign_actor_cannot_prepare_or_accept(self):
        self.assert_code('actor_denied', lambda: self.request(actor_id='someone-else'))
        request, proposal = self.propose()
        self.assert_code('actor_denied', lambda: self.accept(request, proposal, actor_id='someone-else'))

    def test_invalid_outputs_cannot_commit_or_disclose_exception_text(self):
        cases = [
            ('malformed_output', lambda reply: replace(reply, body='not json')),
            ('malformed_output', lambda reply: replace(reply, body=reply.body[:-1] + ',"events":[]}')),
            ('unsupported_action', lambda reply: replace(reply, body=reply.body.replace('enter-passage', 'combat'))),
            ('intent_changed', lambda reply: replace(reply, body=reply.body.replace('take the passage', 'attack'))),
            ('unknown_source', lambda reply: replace(reply, body=canon({**json.loads(reply.body),
                                                                     'source_refs': ['hidden:oracle']}))),
            ('route_mismatch', lambda reply: replace(reply, reported_identity_json='{}')),
            ('output_limit', lambda reply: replace(reply, body='x' * 20000)),
            ('provider_denied', lambda reply: replace(reply, error='provider_denied')),
            ('provider_error', lambda reply: replace(reply, error='secret API KEY HERE')),
            ('transport_error', lambda reply: replace(reply, usage_json='{"input_tokens":-1}')),
        ]
        before = self.world.save()
        for index, (code, change) in enumerate(cases):
            with self.subTest(code=code):
                fake = FakeTransport(change=change)
                request = self.request('bad-' + str(index))
                result = self.broker.dispatch(request, 'offline', fake)
                self.assertEqual(result.code, code)
                self.assertEqual(self.ledger.lookup(request.request_id)['reserved'], 10)
                self.assertEqual(self.world.save(), before)

    def test_duplicate_and_altered_payload_or_fallback_do_not_redispatch(self):
        request = self.request()
        fake = FakeTransport()
        first = self.broker.dispatch(request, 'offline', fake)
        self.assertEqual(self.broker.dispatch(request, 'offline', fake), first)
        self.assertEqual(self.broker.dispatch(replace(request, intention='different'), 'offline', fake).code,
                         'request_identity_conflict')
        self.assertEqual(self.broker.dispatch(request, 'unlisted-fallback', fake).code, 'route_denied')
        self.assertEqual(fake.calls, 1)

    def test_route_mutation_without_version_change_cannot_reuse_a_proposal(self):
        request = self.request()
        fake = FakeTransport()
        self.propose(request, fake)
        self.registry.routes['offline'] = route(model='replacement-model-with-same-config-version')
        result = self.broker.dispatch(request, 'offline', fake)
        self.assertEqual(result.code, 'route_configuration_changed')
        self.assertIsNone(result.proposal)
        self.assertEqual(fake.calls, 1)

    def test_restart_after_dispatch_and_before_result_never_redispatches(self):
        request = self.request()
        self.ledger.claim(request, route(), time.time())
        reopened = AttemptLedger(self.ledger.path, budget_units=100, max_inflight=2)
        fake = FakeTransport()
        result = CapabilityBroker(self.registry, reopened, enabled=True).dispatch(request, 'offline', fake)
        self.assertEqual(result.code, 'in_progress_or_in_doubt')
        self.assertEqual(fake.calls, 0)
        self.assertEqual(reopened.lookup(request.request_id)['reserved'], 10)

    def test_concurrent_duplicate_reserves_and_dispatches_once(self):
        request = self.request()
        entered, release = threading.Event(), threading.Event()
        self.addCleanup(release.set)
        fake = FakeTransport(entered=entered, block=release)
        with ThreadPoolExecutor(max_workers=2) as workers:
            first = workers.submit(self.broker.dispatch, request, 'offline', fake)
            self.assertTrue(entered.wait(1))
            second = self.broker.dispatch(request, 'offline', fake)
            self.assertEqual(second.code, 'in_progress_or_in_doubt')
            release.set()
            self.assertEqual(first.result(2).status, 'proposal_ready')
        self.assertEqual(fake.calls, 1)

    def test_concurrent_reservations_and_budget_are_finite(self):
        ledger = AttemptLedger(Path(self.temp.name) / 'finite.sqlite', budget_units=10, max_inflight=1)
        broker = CapabilityBroker(self.registry, ledger, enabled=True, scope_reader=self.scope)
        entered, release = threading.Event(), threading.Event()
        self.addCleanup(release.set)
        fake = FakeTransport(entered=entered, block=release)
        with ThreadPoolExecutor(max_workers=2) as workers:
            first = workers.submit(broker.dispatch, self.request('one'), 'offline', fake)
            self.assertTrue(entered.wait(1))
            self.assertEqual(broker.dispatch(self.request('two'), 'offline', fake).code, 'budget_exhausted')
            release.set()
            self.assertEqual(first.result(2).status, 'proposal_ready')
        self.assertEqual(broker.dispatch(self.request('three'), 'offline', fake).code, 'budget_exhausted')
        self.assertEqual(fake.calls, 1)

    def test_deadline_and_cancellation_ignore_late_proposal_but_record_usage(self):
        for cancel in (False, True):
            with self.subTest(cancel=cancel):
                entered, release = threading.Event(), threading.Event()
                self.addCleanup(release.set)
                request = self.request('cancel' if cancel else 'timeout', deadline=time.time() + 0.08)
                fake = FakeTransport(entered=entered, block=release)
                with ThreadPoolExecutor(max_workers=1) as workers:
                    future = workers.submit(self.broker.dispatch, request, 'offline', fake)
                    self.assertTrue(entered.wait(1))
                    if cancel:
                        self.ledger.cancel(request.request_id)
                    result = future.result(1)
                    self.assertEqual(result.code, 'cancelled' if cancel else 'deadline_exceeded')
                    release.set()
                limit = time.monotonic() + 1
                while not self.ledger.lookup(request.request_id)['finished'] and time.monotonic() < limit:
                    time.sleep(0.005)
                row = self.ledger.lookup(request.request_id)
                self.assertEqual(row['reserved'], 10)
                self.assertEqual(json.loads(row['usage'])['output_tokens'], 18)
                self.assertEqual(self.ledger.result(request.request_id), result)
                self.assertEqual(self.broker.dispatch(request, 'offline', fake), result)
                self.assertEqual(fake.calls, 1)

    def test_pre_dispatch_cancel_deadline_or_fallback_has_no_call(self):
        fake = FakeTransport()
        self.assertEqual(self.broker.dispatch(self.request('pre-cancel'), 'offline', fake, cancelled=lambda: True).code,
                         'cancelled')
        self.assertEqual(self.broker.dispatch(self.request('pre-deadline', deadline=time.time() - 1), 'offline', fake).code,
                         'deadline_exceeded')
        self.assertEqual(self.broker.dispatch(self.request('pre-route'), 'different-route', fake).code, 'route_denied')
        self.assertEqual(fake.calls, 0)

    def test_explicit_acceptance_keeps_original_semantics_and_sources(self):
        request, proposal = self.propose()
        self.assert_code('acceptance_required', lambda: self.accept(request, proposal, explicitly_accepted=False))
        self.assert_code('acceptance_changed', lambda: self.accept(request, proposal, intention='I attack.'))
        self.assert_code('acceptance_changed', lambda: self.accept(request, proposal, proposal_digest='changed'))
        result = self.accept(request, proposal)
        self.assertEqual(result['outcome']['summary'], 'Completed enter-passage.')
        event = self.world.s['journal'][-1]
        self.assertIn(request.intention, event['params']['instruction_ref'])
        self.assertEqual(event['params']['action'], {'kind': 'scene_action', 'action_id': 'enter-passage'})
        self.assertNotIn('dependencies', result)
        certificate = json.loads(self.ledger.lookup(request.request_id)['dependencies'])
        self.assertTrue(certificate['reads'])
        self.assertTrue(certificate['writes'])

    def test_two_actions_then_conserved_delivery_survive_reload_and_replay(self):
        for number, action in enumerate(('enter-passage', 'reach-desk', 'deliver')):
            request, proposal = self.propose(self.request('step-' + str(number)), FakeTransport(action))
            result = self.accept(request, proposal)
            self.world = self.host.load()
            before = self.world.save()
            self.assertEqual(self.accept(request, proposal), result)
            self.assertEqual(self.world.save(), before)
            self.ledger = AttemptLedger(self.ledger.path, budget_units=100, max_inflight=2)
            self.broker = CapabilityBroker(self.registry, self.ledger, enabled=True, scope_reader=self.scope)
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 39)
        self.assertEqual(self.world.s['stocks']['pc']['sealed_dispatch'], 0)
        self.assertEqual(self.world.s['stocks']['clerk-tray']['sealed_dispatch'], 1)
        self.assertEqual(self.host.writes, 3)

    def test_lost_save_ack_recovers_from_durable_core_receipt(self):
        request, proposal = self.propose()
        original = self.world.save()
        def lose_ack(scope, save, receipt):
            self.host.persist(scope, save, receipt)
            raise OSError('simulated lost acknowledgment')
        with self.assertRaises(OSError):
            self.accept(request, proposal, persist=lose_ack)
        self.assertEqual(self.world.save(), original)
        self.world = self.host.load()
        self.ledger.cancel(request.request_id)
        before = self.world.save()
        self.assertEqual(self.accept(request, proposal)['status'], 'completed_successfully')
        self.assertEqual(self.world.save(), before)
        self.assertEqual(self.host.writes, 1)

    def test_persist_failure_and_competing_host_revision_leave_world_unchanged(self):
        request, proposal = self.propose()
        def fail(*args):
            raise OSError('synthetic disk unavailable')
        with self.assertRaises(OSError):
            self.accept(request, proposal, persist=fail)
        self.assertEqual(self.world.checksum(), request.scope.state_digest)
        different = self.host.load()
        execute(different, 'look-quay', 'external-commit')
        self.host.install(different)
        self.assert_code('host_compare_failed', lambda: self.accept(request, proposal))
        self.assertEqual(self.host.load().checksum(), different.checksum())

    def test_concurrent_acceptance_never_repeats_effects(self):
        request, proposal = self.propose()
        original = self.world.save()
        def accept_copy():
            try:
                return accept_proposal(CoreWorld.load(original), self.ledger,
                    request_id=request.request_id, proposal_digest=proposal.proposal_digest,
                    actor_id='pc', intention=request.intention, branch_id='branch-1', restore_id='restore-1',
                    explicitly_accepted=True, persist=self.host.persist, clock=time.time)
            except CapabilityUnavailable as error:
                return error.code
        with ThreadPoolExecutor(max_workers=2) as workers:
            results = list(workers.map(lambda _: accept_copy(), range(2)))
        self.assertEqual(sum(isinstance(x, dict) for x in results), 1)
        self.assertEqual(self.host.writes, 1)
        self.assertEqual(self.host.load().s['elapsed_time']['seconds'], 20)

    def test_changed_state_revoked_control_and_restore_fence_old_proposals(self):
        request, proposal = self.propose()
        self.world.s['player_actor_ids'] = []
        self.assert_code('actor_denied', lambda: self.accept(request, proposal))
        self.world = self.host.load()
        execute(self.world, 'look-quay', 'other-observation')
        self.assert_code('stale_state', lambda: self.accept(request, proposal))
        self.world = self.host.load()
        self.assert_code('stale_scope', lambda: self.accept(request, proposal, restore_id='restored-2'))
        self.accept(request, proposal)
        self.world = fixture()
        self.assert_code('restored_future', lambda: self.accept(request, proposal))

    def test_cancelled_or_expired_uncommitted_proposal_cannot_act(self):
        request, proposal = self.propose()
        self.assert_code('deadline_exceeded', lambda: self.accept(request, proposal, clock=lambda: request.deadline))
        self.ledger.cancel(request.request_id)
        self.assert_code('proposal_unavailable', lambda: self.accept(request, proposal))

    def test_late_output_is_unavailable_before_presentation_after_state_restore_or_close(self):
        original = self.world.save()
        for variant in ('state', 'restore', 'closed'):
            with self.subTest(variant=variant):
                self.world = CoreWorld.load(original)
                self.host.restore_id = 'restore-1'
                self.broker.scope_reader = self.scope
                request = self.request('late-' + variant)
                entered, release = threading.Event(), threading.Event()
                self.addCleanup(release.set)
                fake = FakeTransport(entered=entered, block=release)
                with ThreadPoolExecutor(max_workers=1) as workers:
                    future = workers.submit(self.broker.dispatch, request, 'offline', fake)
                    self.assertTrue(entered.wait(1))
                    if variant == 'state':
                        execute(self.world, 'look-quay', 'changed-before-reply')
                    elif variant == 'restore':
                        self.host.restore_id = 'restore-2'
                    else:
                        self.broker.scope_reader = lambda request: None
                    before = self.world.save()
                    release.set()
                    result = future.result(2)
                self.assertEqual(result.code, 'stale_scope_or_state')
                self.assertIsNone(result.proposal)
                self.assertEqual(self.world.save(), before)
                self.assertEqual(fake.calls, 1)
                self.assertEqual(ActorRequest.from_json(self.ledger.lookup(request.request_id)['request']).intention,
                                 request.intention)

    def test_current_conflicting_commitment_rejects_with_observed_reads(self):
        apply(self.world, 'capacity', 'record_capacity', capacity_id='other-site', site='other-site',
              quantity=1, unit='concurrent_people')
        apply(self.world, 'other-work', 'commit_activity', activity_id='other-work', actors=['pc'],
              site='other-site', capacity_id='other-site', start=self.world.s['clock'] + 2,
              end=self.world.s['clock'] + 20, role='existing commitment', authority_ref='fixture',
              instruction_ref='explicit other work')
        self.host.install(self.world)
        request, proposal = self.propose()
        self.assert_code('action_unavailable', lambda: self.accept(request, proposal))
        certificate = json.loads(self.ledger.lookup(request.request_id)['dependencies'])
        self.assertTrue(certificate['reads'])
        self.assertEqual(certificate['writes'], [])

    def test_hidden_blocker_retains_risky_option_and_actual_failed_outcome(self):
        request, proposal = self.propose(transport=FakeTransport('try-gate'))
        result = self.accept(request, proposal)
        self.assertEqual(result['status'], 'completed_unsuccessfully')
        self.assertEqual(self.world.s['actors']['pc']['current']['location']['value'], 'quay')
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 5)

    def test_depleted_stock_uses_existing_rule_without_partial_transfer(self):
        execute(self.world, 'enter-passage')
        execute(self.world, 'reach-desk')
        execute(self.world, 'deliver', 'already-delivered')
        self.host.install(self.world)
        request, proposal = self.propose(transport=FakeTransport('deliver'))
        before = dict(self.world.s['stocks']['clerk-tray'])
        result = self.accept(request, proposal)
        self.assertEqual(result['status'], 'completed_unsuccessfully')
        self.assertEqual(self.world.s['stocks']['clerk-tray'], before)
        self.assertEqual(self.world.s['stocks']['pc']['sealed_dispatch'], 0)


if __name__ == '__main__':
    unittest.main()
