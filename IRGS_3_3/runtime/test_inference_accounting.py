"""Synthetic final-charge evidence, never actual provider bills or paid calls."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import hashlib
from pathlib import Path
import tempfile
import time
import unittest

from inference_accounting import FinalCharge, budget_status, reconcile
from solo_actions import prepare_request
from solo_provider import AttemptLedger, CapabilityBroker, CapabilityUnavailable, SpecialistRegistry
from test_scene_actions import fixture
from test_solo_provider import FakeTransport, route


class AccountingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.world=fixture()
        self.ledger=AttemptLedger(Path(self.temp.name)/'ledger.sqlite',budget_units=10)
        self.registry=SpecialistRegistry([route()])
        self.broker=CapabilityBroker(self.registry,self.ledger,enabled=True,scope_reader=lambda request:request.scope)

    def request(self,key):
        return prepare_request(self.world,request_id=key,actor_id='pc',intention='I take the passage.',
            branch_id='branch-1',restore_id='restore-1',allowed_routes=('offline',),
            classification='synthetic-approved',policy_ref='synthetic-transfer-approved-v1',
            config_version='config-v1',deadline=time.time()+20)

    def charge(self,attempt='one',amount=4):
        return FinalCharge(attempt,'review-'+attempt,amount,'synthetic-ceiling-v1',
            'synthetic-final-account-statement',hashlib.sha256(b'synthetic-bill').hexdigest(),
            'explicit-operator-test-review',True)

    def reconcile(self,charge):return reconcile(self.ledger,charge,authorize=lambda _:True)
    def status(self):return budget_status(self.ledger,authorize=lambda:True)

    def assert_code(self,code,fn):
        with self.assertRaises(CapabilityUnavailable) as error:fn()
        self.assertEqual(error.exception.code,code)

    def test_final_charge_releases_only_reviewed_difference_without_changing_campaign_or_attempt(self):
        self.broker.dispatch(self.request('one'),'offline',FakeTransport())
        before=self.world.save();attempt=self.ledger.lookup('one')
        self.assertEqual(self.status()['available_units'],0)
        charge=self.charge();receipt=self.reconcile(charge)
        self.assertEqual(self.status(),{'ceiling_units':10,'held_units':0,'known_charged_units':4,
            'unknown_attempts':0,'available_units':6,'overrun_units':0})
        self.assertEqual(self.world.save(),before);self.assertEqual(self.ledger.lookup('one'),attempt)
        reopened=AttemptLedger(self.ledger.path,budget_units=10)
        self.assertEqual(reconcile(reopened,charge,authorize=lambda _:True),receipt)

    def test_missing_permission_evidence_rate_or_finality_cannot_refund_uncertainty(self):
        self.broker.dispatch(self.request('one'),'offline',FakeTransport())
        charge=self.charge()
        self.assert_code('operator_denied',lambda:reconcile(self.ledger,charge))
        for bad,code in [(replace(charge,final=False),'final_charge_required'),
            (replace(charge,evidence_sha256='unknown'),'accounting_evidence_required'),
            (replace(charge,charged_units=-1),'invalid_charge'),
            (replace(charge,price_revision='different'),'rate_revision_mismatch')]:
            self.assert_code(code,lambda:self.reconcile(bad))
        self.assertEqual(self.status()['held_units'],10)

    def test_inflight_or_legacy_uncertainty_cannot_be_reclassified_free(self):
        request=self.request('one');self.ledger.claim(request,route(),time.time())
        self.assert_code('attempt_in_doubt',lambda:self.reconcile(self.charge(amount=0)))
        self.assertEqual(self.status()['held_units'],10)

    def test_reported_tokens_or_error_never_automatically_mean_zero_charge(self):
        fake=FakeTransport(change=lambda reply:replace(reply,error='provider_denied'))
        self.assertEqual(self.broker.dispatch(self.request('one'),'offline',fake).code,'provider_denied')
        self.assertEqual(self.status()['unknown_attempts'],1)
        self.assertEqual(self.status()['held_units'],10)
        self.reconcile(self.charge(amount=0))
        self.assertEqual(self.status()['available_units'],10)

    def test_overrun_is_retained_and_blocks_new_admission(self):
        self.broker.dispatch(self.request('one'),'offline',FakeTransport())
        self.reconcile(self.charge(amount=14))
        self.assertEqual(self.status()['overrun_units'],4)
        fake=FakeTransport()
        self.assertEqual(self.broker.dispatch(self.request('two'),'offline',fake).code,'budget_exhausted')
        self.assertEqual(fake.calls,0)

    def test_concurrent_reconciliation_is_idempotent_and_changed_final_value_conflicts(self):
        self.broker.dispatch(self.request('one'),'offline',FakeTransport())
        with ThreadPoolExecutor(2) as pool:results=list(pool.map(lambda _:self.reconcile(self.charge()),range(2)))
        self.assertEqual(results[0],results[1])
        self.assert_code('reconciliation_conflict',lambda:self.reconcile(self.charge(amount=0)))
        self.assertEqual(self.status()['known_charged_units'],4)

    def test_new_admission_uses_actual_reviewed_charge_plus_remaining_reservations(self):
        self.broker.dispatch(self.request('one'),'offline',FakeTransport())
        self.reconcile(self.charge(amount=4))
        self.registry.routes['offline']=route(reservation_units=6)
        fake=FakeTransport()
        self.assertEqual(self.broker.dispatch(self.request('two'),'offline',fake).status,'proposal_ready')
        self.assertEqual(fake.calls,1)
        self.assertEqual(self.status()['held_units'],6)
        self.assertEqual(self.status()['known_charged_units'],4)
        self.assertEqual(self.status()['available_units'],0)

    def test_diagnostics_require_operator_access(self):
        self.assert_code('operator_denied',lambda:budget_status(self.ledger))
        def broken_authorizer(*args):raise RuntimeError('private operator configuration')
        self.assert_code('operator_denied',lambda:budget_status(self.ledger,authorize=broken_authorizer))
        self.assert_code('operator_denied',lambda:reconcile(self.ledger,self.charge(),authorize=broken_authorizer))

    def test_large_reviewed_overruns_remain_exact_and_block_admission(self):
        self.ledger=AttemptLedger(Path(self.temp.name)/'large.sqlite',budget_units=20)
        self.broker.ledger=self.ledger
        for key in ('one','two'):
            self.assertEqual(self.broker.dispatch(self.request(key),'offline',FakeTransport()).status,'proposal_ready')
        for key in ('one','two'):self.reconcile(self.charge(attempt=key,amount=2**63-1))
        self.assertEqual(self.status()['known_charged_units'],2*(2**63-1))
        self.assertEqual(self.status()['overrun_units'],2*(2**63-1)-20)
        fake=FakeTransport()
        self.assertEqual(self.broker.dispatch(self.request('three'),'offline',fake).code,'budget_exhausted')
        self.assertEqual(fake.calls,0)


if __name__=='__main__':unittest.main()
