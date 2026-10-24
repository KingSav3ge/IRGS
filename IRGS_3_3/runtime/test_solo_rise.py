"""Actual bounded Rise handler through the shared proposal/acceptance boundary."""
from dataclasses import replace
import json
from pathlib import Path
import tempfile
import time
import unittest

from core_world import CoreWorld
from irgs_reference import canon
from settlement_setup import initialize, preview
from solo_actions import accept_proposal, prepare_request
from solo_provider import (AttemptLedger, CapabilityBroker, CapabilityUnavailable, RISE_OPERATION,
                           SpecialistRegistry, WorldScope)
from test_settlement import choices
from test_solo_provider import AtomicTestHost, FakeTransport, route


class SoloRiseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        selected = choices()
        selected['permission'] = 'held'
        self.world = initialize(selected, preview(selected)['review_digest'], 'synthetic-solo-rise')
        self.host = AtomicTestHost(self.temp.name, self.world)
        self.ledger = AttemptLedger(Path(self.temp.name) / 'attempts.sqlite', budget_units=100)
        self.registry = SpecialistRegistry([route(operations=(RISE_OPERATION,))])
        self.broker = CapabilityBroker(self.registry, self.ledger, enabled=True,
            scope_reader=lambda request: WorldScope(self.world.s['campaign_id'], 'branch-1',
                                                    self.host.restore_id, self.world.checksum()))

    def request(self, key):
        return prepare_request(self.world, request_id=key, actor_id='founder',
            intention='Explicit synthetic intention: ' + key, branch_id='branch-1', restore_id='restore-1',
            allowed_routes=('offline',), classification='synthetic-approved',
            policy_ref='synthetic-transfer-approved-v1', config_version='config-v1', deadline=time.time()+20)

    def propose(self, action, key=None):
        request = self.request(key or action)
        result = self.broker.dispatch(request, 'offline', FakeTransport(action))
        self.assertEqual(result.status, 'proposal_ready', result)
        return request, result.proposal

    def accept(self, request, proposal, **changes):
        params = dict(request_id=request.request_id, proposal_digest=proposal.proposal_digest,
            actor_id='founder', intention=request.intention, branch_id='branch-1', restore_id='restore-1',
            explicitly_accepted=True, persist=self.host.persist, clock=time.time)
        params.update(changes)
        return accept_proposal(self.world, self.ledger, **params)

    def test_continuing_work_uses_actual_reservations_consumption_receipts_and_reload(self):
        for index, action in enumerate(('walk_clearing', 'found', 'build', 'wait_hour', 'wait_hour')):
            request, proposal = self.propose(action, 'step-' + str(index))
            self.assertEqual(request.operation_id, RISE_OPERATION)
            result = self.accept(request, proposal)
            self.world = self.host.load()
            before = self.world.save()
            self.assertEqual(self.accept(request, proposal), result)
            self.assertEqual(self.world.save(), before)
            self.assertNotIn('dependencies', result)
            self.assertNotIn('oren-home', canon(result))
            self.ledger = AttemptLedger(self.ledger.path, budget_units=100)
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 3900)
        self.assertEqual(self.world.s['projects']['shelter']['worked'], 3600)
        self.assertEqual(self.world.s['stocks']['founder-home']['timber'], 3)
        self.assertEqual(self.world.s['stocks']['oren-home']['timber'], 2)
        for material, opening in self.world.s['opening_stock'].items():
            consumed = sum(f['quantity'] for f in self.world.s['material_flows'].values() if f['material']==material)
            self.assertEqual(sum(s.get(material,0) for s in self.world.s['stocks'].values()), opening-consumed)
        self.assertEqual(self.host.writes, 5)

    def test_denied_build_is_atomic_and_retains_rejection_dependencies(self):
        request, proposal = self.propose('build')
        before = self.world.save()
        with self.assertRaises(CapabilityUnavailable) as error:
            self.accept(request, proposal)
        self.assertEqual(error.exception.code, 'action_unavailable')
        self.assertEqual(self.world.save(), before)
        record = json.loads(self.ledger.lookup(request.request_id)['dependencies'])
        self.assertEqual(record['status'], 'rejected_no_effects')
        self.assertTrue(record['reads'])
        self.assertEqual(record['writes'], [])

    def test_hidden_own_or_foreign_feasibility_does_not_change_received_input(self):
        first = self.request('first')
        self.world.s['stocks']['oren-home']['grain'] += 100
        self.world.s['opening_stock']['grain'] += 100
        self.world.s['grants']['founding']['active'] = False
        self.world.s['evaluator_only'] = {'answer': 'EVALUATOR_ONLY_SECRET'}
        CoreWorld(state=self.world.s)
        second = replace(self.request('second'), intention=first.intention)
        self.assertEqual(first.model_input(), second.model_input())
        self.assertNotIn('EVALUATOR_ONLY', canon(second.model_input()))
        self.host.install(self.world)
        request, proposal = self.propose('walk_clearing')
        self.accept(request, proposal)
        request, proposal = self.propose('found')
        before = self.world.save()
        with self.assertRaises(CapabilityUnavailable):
            self.accept(request, proposal)
        self.assertEqual(self.world.save(), before)

    def test_existing_worker_commitment_cannot_be_bypassed_by_new_walk(self):
        for action in ('walk_clearing', 'found', 'build'):
            self.accept(*self.propose(action))
        request, proposal = self.propose('walk_commons')
        before = self.world.save()
        with self.assertRaises(CapabilityUnavailable) as error:
            self.accept(request, proposal)
        self.assertEqual(error.exception.code, 'action_unavailable')
        self.assertEqual(self.world.save(), before)
        self.assertEqual(self.world.s['projects']['shelter']['worked'], 0)

    def test_local_only_route_cannot_dispatch_rise(self):
        self.registry.routes['offline'] = route()
        fake = FakeTransport('walk_clearing')
        self.assertEqual(self.broker.dispatch(self.request('denied-route'), 'offline', fake).code, 'policy_denied')
        self.assertEqual(fake.calls, 0)

    def test_long_received_history_keeps_a_bounded_legitimate_request_window(self):
        from settlement_runtime import execute
        for index in range(70):
            execute(self.world, 'prior-' + str(index), 'founder', 'inspect', 'explicit synthetic inspection')
        request = self.request('after-long-history')
        received = request.model_input()['context']['received']
        self.assertEqual(len(received), 32)
        self.assertEqual(len(request.source_refs), 32)
        self.assertIn('settlement-receipt:prior-69', request.source_refs)
        self.assertNotIn('settlement-receipt:setup', request.source_refs)
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 0)


if __name__ == '__main__':
    unittest.main()
