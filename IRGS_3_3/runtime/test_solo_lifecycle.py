"""Deterministic registration/admission/cancellation and replay race evidence."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from pathlib import Path
import sqlite3
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

from irgs_reference import canon
from solo_actions import accept_proposal, prepare_request
from solo_provider import (AttemptLedger, CapabilityBroker, ValidatedResult,
                           SpecialistRegistry, WorldScope)
from test_scene_actions import fixture
from test_solo_provider import AtomicTestHost, FakeTransport, route


class SoloLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.world = fixture()
        self.host = AtomicTestHost(self.temp.name, self.world)
        self.ledger = AttemptLedger(Path(self.temp.name)/'inference.sqlite', budget_units=100)
        self.registry = SpecialistRegistry([route()])
        self.broker = CapabilityBroker(self.registry, self.ledger, enabled=True,
            scope_reader=lambda request: WorldScope(self.world.s['campaign_id'], 'branch-1',
                                                    'restore-1', self.world.checksum()))

    def request(self, key='lifecycle-request'):
        return prepare_request(self.world, request_id=key, actor_id='pc', intention='I take the passage.',
            branch_id='branch-1', restore_id='restore-1', allowed_routes=('offline',),
            classification='synthetic-approved', policy_ref='synthetic-transfer-approved-v1',
            config_version='config-v1', deadline=time.time()+20)

    def wait_finished(self, request_id):
        limit = time.monotonic()+2
        while time.monotonic() < limit:
            row = self.ledger.lookup(request_id)
            if row and row['finished']:
                return row
            time.sleep(0.005)
        self.fail('transport worker did not finish')

    def test_cancellation_before_registration_survives_restart_without_reservation(self):
        request = self.request()
        before = self.world.save()
        self.assertEqual(self.ledger.cancel(request.request_id).code, 'cancelled')
        reopened = AttemptLedger(self.ledger.path, budget_units=100)
        broker = CapabilityBroker(self.registry, reopened, enabled=True, scope_reader=self.broker.scope_reader)
        fake = FakeTransport()
        result = broker.dispatch(request, 'offline', fake)
        self.assertEqual(result.code, 'cancelled')
        self.assertIsNone(result.proposal)
        self.assertEqual(fake.calls, 0)
        self.assertIsNone(reopened.lookup(request.request_id))
        self.assertEqual(self.world.save(), before)

    def test_callback_cancellation_before_registration_also_prevents_later_retry(self):
        request = self.request()
        fake = FakeTransport()
        result = self.broker.dispatch(request, 'offline', fake, cancelled=lambda: True)
        self.assertEqual(result.code, 'cancelled')
        self.assertTrue(self.ledger.is_cancelled(request.request_id))
        self.assertEqual(self.broker.dispatch(request, 'offline', fake).code, 'cancelled')
        self.assertEqual(fake.calls, 0)
        self.assertIsNone(self.ledger.lookup(request.request_id))

    def test_cached_proposal_cancellation_hides_draft_and_preserves_private_recovery(self):
        request = self.request()
        fake = FakeTransport()
        original = self.broker.dispatch(request, 'offline', fake)
        cancelled = self.broker.dispatch(request, 'offline', fake, cancelled=lambda: True)
        self.assertEqual(cancelled.code, 'cancelled')
        self.assertIsNone(cancelled.proposal)
        self.assertEqual(self.ledger.result(request.request_id).proposal, original.proposal)
        self.assertEqual(self.broker.dispatch(request, 'offline', fake), cancelled)
        self.assertEqual(fake.calls, 1)

    def test_cancellation_wins_between_preflight_and_registration(self):
        request = self.request()
        ready, release = threading.Event(), threading.Event()
        original_claim = self.ledger.claim
        def blocked_claim(*args):
            ready.set()
            self.assertTrue(release.wait(2))
            return original_claim(*args)
        fake = FakeTransport()
        self.addCleanup(release.set)
        with patch.object(self.ledger, 'claim', side_effect=blocked_claim), ThreadPoolExecutor(1) as pool:
            pending = pool.submit(self.broker.dispatch, request, 'offline', fake)
            self.assertTrue(ready.wait(1))
            self.ledger.cancel(request.request_id)
            release.set()
            self.assertEqual(pending.result(2).code, 'cancelled')
        self.assertEqual(fake.calls, 0)
        self.assertIsNone(self.ledger.lookup(request.request_id))

    def test_cancellation_after_reservation_and_before_admission_never_enters_transport(self):
        request = self.request()
        ready, release = threading.Event(), threading.Event()
        original_claim = self.ledger.claim
        def blocked_claim(*args):
            claimed = original_claim(*args)
            ready.set()
            self.assertTrue(release.wait(2))
            return claimed
        fake = FakeTransport()
        self.addCleanup(release.set)
        with patch.object(self.ledger, 'claim', side_effect=blocked_claim), ThreadPoolExecutor(1) as pool:
            pending = pool.submit(self.broker.dispatch, request, 'offline', fake)
            self.assertTrue(ready.wait(1))
            self.ledger.cancel(request.request_id)
            release.set()
            self.assertEqual(pending.result(2).code, 'cancelled')
        row = self.wait_finished(request.request_id)
        self.assertEqual(fake.calls, 0)
        self.assertEqual(row['reserved'], 10)
        self.assertEqual(row['transport_state'], 'not_started')
        self.assertIsNone(row['dispatch_started'])
        self.assertIsNone(row['usage'])
        self.assertEqual(self.ledger.result(request.request_id).code, 'cancelled')

    def test_deadline_after_reservation_prevents_transport_admission(self):
        request = self.request()
        now = [request.deadline-10]
        self.broker.clock = lambda: now[0]
        original_claim = self.ledger.claim
        def expire_after_claim(*args):
            claimed = original_claim(*args)
            now[0] = request.deadline+1
            return claimed
        fake = FakeTransport()
        with patch.object(self.ledger, 'claim', side_effect=expire_after_claim):
            self.assertEqual(self.broker.dispatch(request, 'offline', fake).code, 'deadline_exceeded')
        row = self.wait_finished(request.request_id)
        self.assertEqual(fake.calls, 0)
        self.assertEqual(row['reserved'], 10)
        self.assertEqual(row['transport_state'], 'not_started')

    def test_session_closure_after_reservation_prevents_transport_admission(self):
        request = self.request()
        original_claim = self.ledger.claim
        def close_after_claim(*args):
            claimed = original_claim(*args)
            self.broker.scope_reader = lambda request: None
            return claimed
        fake = FakeTransport()
        with patch.object(self.ledger, 'claim', side_effect=close_after_claim):
            self.assertEqual(self.broker.dispatch(request, 'offline', fake).code, 'stale_scope_or_state')
        row = self.wait_finished(request.request_id)
        self.assertEqual(fake.calls, 0)
        self.assertEqual(row['transport_state'], 'not_started')

    def test_route_revocation_or_replacement_after_reservation_prevents_transport(self):
        original_claim = self.ledger.claim
        for index, (replacement, code) in enumerate((
                (route(enabled=False), 'provider_disabled'),
                (route(model='replacement-with-unchanged-version'), 'route_configuration_changed'))):
            with self.subTest(code=code):
                self.registry.routes['offline'] = route()
                request = self.request('route-change-'+str(index))
                def replace_after_claim(*args):
                    claimed = original_claim(*args)
                    self.registry.routes['offline'] = replacement
                    return claimed
                fake = FakeTransport()
                with patch.object(self.ledger, 'claim', side_effect=replace_after_claim):
                    self.assertEqual(self.broker.dispatch(request, 'offline', fake).code, code)
                row = self.wait_finished(request.request_id)
                self.assertEqual(fake.calls, 0)
                self.assertEqual(row['transport_state'], 'not_started')

    def test_wrong_route_duplicate_cannot_terminate_an_authorized_inflight_attempt(self):
        request = self.request()
        entered, release = threading.Event(), threading.Event()
        self.addCleanup(release.set)
        fake = FakeTransport(entered=entered, block=release)
        with ThreadPoolExecutor(1) as pool:
            pending = pool.submit(self.broker.dispatch, request, 'offline', fake)
            self.assertTrue(entered.wait(1))
            wrong = self.broker.dispatch(request, 'unlisted-route', fake)
            self.assertEqual(wrong.code, 'route_denied')
            row = self.ledger.lookup(request.request_id)
            self.assertEqual(row['status'], 'processing')
            self.assertEqual(row['transport_state'], 'admitted')
            self.assertIsNotNone(row['dispatch_started'])
            release.set()
            self.assertEqual(pending.result(2).status, 'proposal_ready')
        self.assertEqual(fake.calls, 1)
        self.assertEqual(self.ledger.result(request.request_id).status, 'proposal_ready')

    def test_expired_cached_draft_is_unavailable_without_losing_its_recovery_record(self):
        request = self.request()
        fake = FakeTransport()
        original = self.broker.dispatch(request, 'offline', fake)
        self.assertEqual(original.status, 'proposal_ready')
        self.broker.clock = lambda: request.deadline+1
        expired = self.broker.dispatch(request, 'offline', fake)
        self.assertEqual(expired.code, 'deadline_exceeded')
        self.assertIsNone(expired.proposal)
        self.assertEqual(self.ledger.result(request.request_id), original)
        self.assertEqual(fake.calls, 1)
        self.assertEqual(self.host.writes, 0)

    def test_admitted_attempt_cannot_be_admitted_twice_or_reclassified_unsent(self):
        request = self.request()
        self.assertTrue(self.ledger.claim(request, route(), time.time()))
        self.assertTrue(self.ledger.begin_transport(request.request_id, request.deadline, time.time))
        self.assertFalse(self.ledger.begin_transport(request.request_id, request.deadline, time.time))
        before = self.ledger.lookup(request.request_id)
        self.ledger.finish_without_transport(ValidatedResult(request.request_id, 'unavailable', 'cancelled'), time.time())
        self.assertEqual(self.ledger.lookup(request.request_id), before)
        reopened = AttemptLedger(self.ledger.path, budget_units=100)
        broker = CapabilityBroker(self.registry, reopened, enabled=True, scope_reader=self.broker.scope_reader)
        fake = FakeTransport()
        self.assertEqual(broker.dispatch(request, 'offline', fake).code, 'in_progress_or_in_doubt')
        self.assertEqual(fake.calls, 0)

    def test_legacy_unknown_attempt_stays_unknown_across_schema_upgrade(self):
        path = Path(self.temp.name)/'legacy.sqlite'
        request = self.request('legacy-attempt')
        with sqlite3.connect(path) as db:
            db.execute('CREATE TABLE limits (id INTEGER PRIMARY KEY,budget INTEGER,inflight INTEGER)')
            db.execute('INSERT INTO limits VALUES (1,100,1)')
            db.execute('CREATE TABLE attempts (id TEXT PRIMARY KEY,fingerprint TEXT NOT NULL,'
                'request TEXT NOT NULL,route TEXT NOT NULL,reserved INTEGER NOT NULL,status TEXT NOT NULL,'
                'finished INTEGER NOT NULL DEFAULT 0,result TEXT,requested_identity TEXT NOT NULL,'
                'reported_identity TEXT,usage TEXT,provider_request_id TEXT,started REAL NOT NULL,'
                'completed REAL,accepted TEXT,dependencies TEXT,route_config TEXT,provider_response_id TEXT)')
            db.execute('INSERT INTO attempts (id,fingerprint,request,route,reserved,status,requested_identity,started)'
                ' VALUES (?,?,?,?,?,?,?,?)', (request.request_id, request.fingerprint(), canon(asdict(request)),
                                             'offline',10,'processing',canon(route().identity()),time.time()))
        upgraded = AttemptLedger(path, budget_units=100)
        before = upgraded.lookup(request.request_id)
        self.assertEqual(before['transport_state'], 'unknown')
        self.assertIsNone(before['dispatch_started'])
        self.assertFalse(upgraded.begin_transport(request.request_id, request.deadline, time.time))
        upgraded.finish_without_transport(ValidatedResult(request.request_id, 'unavailable', 'cancelled'), time.time())
        self.assertEqual(upgraded.lookup(request.request_id), before)
        fake = FakeTransport()
        broker = CapabilityBroker(self.registry, upgraded, enabled=True, scope_reader=self.broker.scope_reader)
        self.assertEqual(broker.dispatch(request, 'offline', fake).code, 'in_progress_or_in_doubt')
        self.assertEqual(fake.calls, 0)

    def test_cancelling_accepted_action_preserves_durable_core_receipt(self):
        request = self.request()
        proposal = self.broker.dispatch(request, 'offline', FakeTransport()).proposal
        def accept():
            return accept_proposal(self.world,self.ledger,request_id=request.request_id,
                proposal_digest=proposal.proposal_digest,actor_id='pc',intention=request.intention,
                branch_id='branch-1',restore_id='restore-1',explicitly_accepted=True,
                persist=self.host.persist,clock=time.time)
        original = accept()
        before = self.world.save()
        self.ledger.cancel(request.request_id)
        self.assertFalse(self.ledger.is_cancelled(request.request_id))
        self.assertEqual(accept(), original)
        self.assertEqual(self.world.save(), before)
        self.assertEqual(self.host.writes, 1)


if __name__ == '__main__':
    unittest.main()
