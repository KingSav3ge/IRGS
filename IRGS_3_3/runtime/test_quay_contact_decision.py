"""Explicit fictional non-Rise decision through ordinary reviewed creation."""
import copy
import json
import tempfile
import unittest
from dataclasses import replace
from unittest.mock import patch

from historical_campaigns import historical_entry
from runtime_contracts import AcceptedIntent, WorldScope
import shared_runtime as shared
import supported_intent as intent
from test_solo_provider import AtomicTestHost
import world_draft


class QuayContactDecisionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='irgs-quay-decision-')
        self.addCleanup(temporary.cleanup)
        self.directory = temporary.name
        for target in ('solo_provider.CapabilityBroker.dispatch', 'openai_proposals.OpenAIProposalTransport.__call__', 'socket.socket.connect'):
            guard = patch(target, side_effect=AssertionError('No provider or network'))
            guard.start(); self.addCleanup(guard.stop)

    def create(self, opening='quay-contact-decision-v1'):
        draft = {'schema_version': world_draft.SCHEMA_VERSION, 'draft_id': 'quay-decision',
                 'classification': 'mixed', 'profile_id': 'historical-quay',
                 'choices': {'snapshot_sha256': historical_entry('hyw-1415')['snapshot_sha256'],
                     'character': {'kind': 'new', 'name': 'Synthetic courier', 'species': 'human', 'opening_id': opening}}}
        review = world_draft.validate(draft)
        world = world_draft.initialize(draft, draft_digest=review['draft_digest'], review_digest=review['review_digest'],
                                       campaign_id='quay-decision-synthetic', explicitly_accepted=True)
        return world, world.s['player_actor_ids'][0]

    def prepare(self, world, actor, action, request_id):
        cap = next(c for c in shared.capabilities(world, actor) if json.loads(c.action_json).get('action_id') == action)
        args = dict(actor_id=actor, intention='My exact chosen words for ' + action,
                    capability_id=cap.capability_id, branch_id='branch-1', restore_id='restore-1')
        review = intent.review(world, **args)
        self.assertEqual(review['status'], 'supported')
        return intent.prepare(world, request_id=request_id, review_id=review['review_id'], **args)

    def scope(self, world):
        return WorldScope(world.s['campaign_id'], 'branch-1', 'restore-1', world.checksum())

    def execute(self, world, request, host):
        return intent.execute(world, request, current_scope=self.scope(world), persist=host.persist, explicitly_accepted=True)

    def test_selected_refusal_then_actual_delivery_retry_and_restore(self):
        world, actor = self.create(); host = AtomicTestHost(self.directory, world)
        stocks = copy.deepcopy(world.s['stocks']); calendar = copy.deepcopy(world.s['campaign_time'])
        request = self.prepare(world, actor, 'request-dispatch-help', 'ask')
        before = world.save()
        with self.assertRaises(shared.SharedActionUnavailable):
            intent.execute(world, request, current_scope=self.scope(world), persist=host.persist, explicitly_accepted=False)
        self.assertEqual(world.save(), before)
        result = self.execute(world, request, host)
        self.assertEqual(result['status'], 'completed_successfully')
        self.assertIn('declines to take custody', json.dumps(result).lower())
        self.assertEqual(world.s['stocks'], stocks); self.assertEqual(world.s['elapsed_time']['seconds'], 15)
        self.assertEqual(world.s['campaign_time'], calendar)
        evidence = [e for e in world.s['evidence'].values() if e.get('assertion') == 'I will not carry the dispatch.']
        self.assertEqual(len(evidence), 1); self.assertEqual(evidence[0]['status'], 'testimony')
        self.assertEqual(evidence[0]['originator'], 'FICTIONAL-QUAY-CONTACT')
        evidence_id = next(k for k, e in world.s['evidence'].items() if e is evidence[0])
        self.assertIn(evidence_id, world.s['knowledge'][actor])
        for action in ('quay-passage', 'passage-desk', 'deliver-dispatch'):
            self.execute(world, self.prepare(world, actor, action, action), host)
        self.assertEqual(world.s['stocks'][actor]['sealed_dispatch'], 0)
        self.assertEqual(world.s['stocks']['clerk-tray']['sealed_dispatch'], 1)
        self.assertEqual(world.s['elapsed_time']['seconds'], 115)
        self.assertEqual(world.s['campaign_time'], calendar)
        world = host.load(); saved = world.save(); writes = host.writes
        self.assertEqual(self.execute(world, AcceptedIntent.from_json(request.to_json()), host), result)
        self.assertEqual(world.save(), saved); self.assertEqual(host.writes, writes)
        with self.assertRaises(shared.SharedActionUnavailable):
            intent.execute(world, request, current_scope=replace(self.scope(world), restore_id='restored'),
                           persist=host.persist, explicitly_accepted=True)
        self.assertEqual(world.save(), saved)

    def test_original_contact_profile_remains_without_selected_decision(self):
        world, actor = self.create('quay-contact-v1')
        actions = [json.loads(c.action_json).get('action_id') for c in shared.capabilities(world, actor)]
        self.assertNotIn('request-dispatch-help', actions)

    def test_missing_contact_rejects_without_state_or_hidden_menu_filter(self):
        world, actor = self.create(); host = AtomicTestHost(self.directory, world)
        old_menu = [c.public() for c in shared.capabilities(world, actor)]
        world.s['actors']['FICTIONAL-QUAY-CONTACT']['current']['location']['value'] = 'other-place'
        self.assertEqual([c.public() for c in shared.capabilities(world, actor)], old_menu)
        request = self.prepare(world, actor, 'request-dispatch-help', 'absent')
        before = world.save()
        with self.assertRaises(shared.SharedActionUnavailable): self.execute(world, request, host)
        self.assertEqual(world.save(), before); self.assertEqual(host.writes, 0)

    def test_worker_under_player_control_does_not_receive_scripted_decision(self):
        world, actor = self.create(); host = AtomicTestHost(self.directory, world)
        world.s['player_actor_ids'].append('FICTIONAL-QUAY-CONTACT')
        request = self.prepare(world, actor, 'request-dispatch-help', 'controlled-contact')
        before = world.save()
        with self.assertRaises(shared.SharedActionUnavailable): self.execute(world, request, host)
        self.assertEqual(world.save(), before); self.assertEqual(host.writes, 0)

    def test_persistence_failure_does_not_record_the_conversation(self):
        world, actor = self.create(); request = self.prepare(world, actor, 'request-dispatch-help', 'failed-save')
        before = world.save()
        def fail(*_): raise OSError('synthetic disk failure')
        with self.assertRaises((OSError, shared.SharedActionUnavailable)):
            intent.execute(world, request, current_scope=self.scope(world), persist=fail, explicitly_accepted=True)
        self.assertEqual(world.save(), before)


if __name__ == '__main__': unittest.main()
