"""Reviewed R00 invitation decisions through the public intent and Core path."""
import copy
import json
import tempfile
import unittest
from dataclasses import replace
from unittest.mock import patch

from runtime_contracts import AcceptedIntent, WorldScope
import shared_runtime as shared
import supported_intent as intent
from test_settlement import choices
from test_solo_provider import AtomicTestHost
import world_draft


class OrdinaryInvitationDecisionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='irgs-invitation-decision-')
        self.addCleanup(temporary.cleanup)
        for target in ('solo_provider.CapabilityBroker.dispatch', 'openai_proposals.OpenAIProposalTransport.__call__', 'socket.socket.connect'):
            guard = patch(target, side_effect=AssertionError('No provider or network'))
            guard.start(); self.addCleanup(guard.stop)
        selected = choices(); selected['permission'] = 'held'
        draft = {'schema_version': world_draft.SCHEMA_VERSION, 'draft_id': 'invitation-draft',
                 'classification': 'fictional', 'profile_id': 'rise-r00', 'choices': selected}
        reviewed = world_draft.validate(draft)
        self.world = world_draft.initialize(draft, draft_digest=reviewed['draft_digest'],
            review_digest=reviewed['review_digest'], campaign_id='ordinary-invitation', explicitly_accepted=True)
        self.host = AtomicTestHost(temporary.name, self.world)

    def scope(self):
        return WorldScope(self.world.s['campaign_id'], 'branch-1', 'restore-1', self.world.checksum())

    def prepare(self, action, request_id, words):
        cap = next(c for c in shared.capabilities(self.world, 'founder')
                   if json.loads(c.action_json).get('action_id') == action)
        args = dict(actor_id='founder', intention=words, capability_id=cap.capability_id,
                    branch_id='branch-1', restore_id='restore-1')
        reviewed = intent.review(self.world, **args)
        self.assertEqual(reviewed['status'], 'supported')
        return intent.prepare(self.world, request_id=request_id, review_id=reviewed['review_id'], **args)

    def execute(self, request):
        return intent.execute(self.world, request, current_scope=self.scope(), persist=self.host.persist,
                              explicitly_accepted=True)

    def test_refusal_then_new_decision_and_exact_retry(self):
        for action in ('walk_clearing', 'found', 'walk_commons'):
            self.execute(self.prepare(action, action, action))
        stocks = copy.deepcopy(self.world.s['stocks'])
        elapsed = self.world.s['elapsed_time']['seconds']
        request = self.prepare('invite', 'invite-early', 'Would you move to our camp?')
        before = self.world.save(); writes = self.host.writes
        with self.assertRaises(shared.SharedActionUnavailable):
            intent.execute(self.world, request, current_scope=self.scope(), persist=self.host.persist,
                           explicitly_accepted=False)
        self.assertEqual(self.world.save(), before); self.assertEqual(self.host.writes, writes)
        refused = self.execute(request)
        self.assertEqual(refused['status'], 'completed_successfully')  # the conversation completed
        public = json.dumps(refused).lower()
        self.assertIn('declines to move', public)
        self.assertNotIn('oren-repair', public); self.assertNotIn('seed_reserve', public)
        self.assertNotIn('grain', public)
        self.assertNotIn('oren-move', self.world.s['migrations'])
        self.assertEqual(self.world.s['stocks'], stocks)
        self.assertEqual(self.world.s['elapsed_time']['seconds'], elapsed)
        self.assertIn('shared:invite-early:invitation', self.world.s['settlement_receipts']['oren'])
        self.execute(self.prepare('wait_hour', 'wait', 'I wait.'))
        self.assertEqual(self.world.s['projects']['oren-repair']['status'], 'complete')
        agreed = self.execute(self.prepare('invite', 'invite-later', 'Would you move now?'))
        self.assertIn('agrees to move', json.dumps(agreed).lower())
        self.assertEqual(self.world.s['migrations']['oren-move']['status'], 'agreed')
        self.assertEqual(self.world.s['actors']['oren']['current']['location'], 'commons')
        self.world = self.host.load(); saved = self.world.save(); writes = self.host.writes
        self.assertEqual(self.execute(AcceptedIntent.from_json(request.to_json())), refused)
        self.assertEqual(self.world.save(), saved); self.assertEqual(self.host.writes, writes)
        with self.assertRaises(shared.SharedActionUnavailable):
            intent.execute(self.world, request, current_scope=replace(self.scope(), restore_id='restored'),
                           persist=self.host.persist, explicitly_accepted=True)
        self.assertEqual(self.world.save(), saved)

    def test_refusal_with_completed_repair_and_no_unreserved_provision(self):
        for action in ('walk_clearing', 'found', 'walk_commons'):
            self.execute(self.prepare(action, action, action))
        # Ordinary elapsed work/provision, no privileged stock edits.
        for i in range(100):
            if self.world.s['stocks']['oren-home']['grain'] <= self.world.s['households']['oren-home']['seed_reserve']:
                break
            self.execute(self.prepare('wait_hour', 'wait-' + str(i), 'I wait.'))
        else:
            self.fail('ordinary provision did not reach the selected boundary')
        self.assertEqual(self.world.s['projects']['oren-repair']['status'], 'complete')
        result = self.execute(self.prepare('invite', 'invite-without-provision', 'Would you move?'))
        self.assertIn('declines to move', json.dumps(result).lower())
        self.assertNotIn('grain', json.dumps(result).lower())
        self.assertNotIn('oren-move', self.world.s['migrations'])

    def test_failed_persistence_does_not_record_refusal(self):
        for action in ('walk_clearing', 'found', 'walk_commons'):
            self.execute(self.prepare(action, action, action))
        request = self.prepare('invite', 'failure', 'Would you move?')
        before = self.world.save()
        def fail(*_):
            raise OSError('synthetic persistence failure')
        with self.assertRaises((shared.SharedActionUnavailable, OSError)):
            intent.execute(self.world, request, current_scope=self.scope(), persist=fail, explicitly_accepted=True)
        self.assertEqual(self.world.save(), before)
        self.assertNotIn('shared:failure:invitation', self.world.s['settlement_receipts'].get('oren', {}))


if __name__ == '__main__':
    unittest.main()
