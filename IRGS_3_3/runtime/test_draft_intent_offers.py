"""Normal reviewed drafts and offer attempts over existing Core operations."""
import copy
import json
import tempfile
import unittest
from dataclasses import replace
from unittest.mock import patch

import communication_contract as comm
from core_world import CoreWorld
from historical_campaigns import historical_entry
from runtime_contracts import WorldScope
import shared_runtime as shared
import supported_intent as intent
from test_settlement import choices
from test_solo_provider import AtomicTestHost
import world_draft


class DraftIntentOffersTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='irgs-draft-intent-')
        self.addCleanup(self.temp.cleanup)
        for target in ('solo_provider.CapabilityBroker.dispatch', 'openai_proposals.OpenAIProposalTransport.__call__', 'socket.socket.connect'):
            guard = patch(target, side_effect=AssertionError('No provider or network'))
            guard.start(); self.addCleanup(guard.stop)

    def create(self, context, *, select_stock_offers=False):
        if context == 'rise':
            selected = choices(); selected['permission'] = 'seek'
            if select_stock_offers:
                from settlement_setup import OFFER_PROFILE
                selected['offer_profile'] = OFFER_PROFILE
            draft = {'schema_version': world_draft.SCHEMA_VERSION, 'draft_id': 'rise-draft',
                     'classification': 'fictional', 'profile_id': 'rise-r00', 'choices': selected}
        else:
            draft = {'schema_version': world_draft.SCHEMA_VERSION, 'draft_id': 'quay-draft',
                     'classification': 'mixed', 'profile_id': 'historical-quay',
                     'choices': {'character': {'kind': 'new', 'name': 'Synthetic courier', 'species': 'human',
                                               'opening_id': 'quay-contact-v1'},
                                 'snapshot_sha256': historical_entry('hyw-1415')['snapshot_sha256']}}
        reviewed = world_draft.validate(draft)
        world = world_draft.initialize(draft, draft_digest=reviewed['draft_digest'],
            review_digest=reviewed['review_digest'], campaign_id='ordinary-' + context, explicitly_accepted=True)
        return world, world.s['player_actor_ids'][0]

    def scope(self, world, restore='restore-1'):
        return WorldScope(world.s['campaign_id'], 'branch-1', restore, world.checksum())

    def attempt(self, world, actor, host, action, request_id, words):
        capability = next(c for c in shared.capabilities(world, actor) if json.loads(c.action_json).get('action_id') == action)
        before = world.save()
        reviewed = intent.review(world, actor_id=actor, intention=words, capability_id=capability.capability_id,
                                 branch_id='branch-1', restore_id='restore-1')
        self.assertEqual(reviewed['status'], 'supported'); self.assertFalse(reviewed['committed'])
        request = intent.prepare(world, request_id=request_id, actor_id=actor, intention=words,
            capability_id=capability.capability_id, review_id=reviewed['review_id'], branch_id='branch-1', restore_id='restore-1')
        self.assertEqual(world.save(), before)
        with self.assertRaises(shared.SharedActionUnavailable):
            intent.execute(world, request, current_scope=self.scope(world), persist=host.persist, explicitly_accepted=False)
        self.assertEqual(world.save(), before)
        result = intent.execute(world, request, current_scope=self.scope(world), persist=host.persist, explicitly_accepted=True)
        self.assertEqual(result['intention'], words)
        return request, result

    def test_real_rise_offer_requires_separate_acceptance_and_preserves_stock(self):
        world, actor = self.create('rise'); host = AtomicTestHost(self.temp.name, world)
        first = intent.grant_offer_prerequisites(world, actor_id=actor)
        self.assertEqual(first['status'], 'attempts_selected')
        self.assertEqual([a['action_id'] for a in first['actions']], ['request_grant', 'accept_grant'])
        self.assertEqual(first['offer_status'], 'not_inspected')
        self.assertEqual(first['consent_status'], 'not_inferred')
        hidden = CoreWorld.load(world.save())
        hidden.s['organizations']['steward']['active'] = False
        hidden.s['actors']['elin']['current']['location'] = 'PRIVATE_OTHER_PLACE'
        self.assertEqual(intent.grant_offer_prerequisites(hidden, actor_id=actor), first)
        stocks, elapsed = copy.deepcopy(world.s['stocks']), copy.deepcopy(world.s['elapsed_time'])
        cap = next(c for c in shared.capabilities(world, actor) if json.loads(c.action_json).get('action_id') == 'accept_grant')
        review = intent.review(world, actor_id=actor, intention='I accept.', capability_id=cap.capability_id,
                               branch_id='branch-1', restore_id='restore-1')
        request = intent.prepare(world, request_id='premature', actor_id=actor, intention='I accept.',
            capability_id=cap.capability_id, review_id=review['review_id'], branch_id='branch-1', restore_id='restore-1')
        before = world.save()
        with self.assertRaises(shared.SharedActionUnavailable):
            intent.execute(world, request, current_scope=self.scope(world), persist=host.persist, explicitly_accepted=True)
        self.assertEqual(world.save(), before); self.assertEqual(host.writes, 0)
        offered_request, offered = self.attempt(world, actor, host, 'request_grant', 'offer', 'Please offer the limited grant.')
        self.assertEqual(offered['status'], 'completed_successfully')
        self.assertEqual(world.s['grants']['founding']['status'], 'offered')
        self.assertEqual(world.s['stocks'], stocks); self.assertEqual(world.s['elapsed_time'], elapsed)
        accepted_request, accepted = self.attempt(world, actor, host, 'accept_grant', 'accept', 'I accept the limited grant.')
        self.assertEqual(accepted['status'], 'completed_successfully')
        self.assertEqual(world.s['grants']['founding']['status'], 'accepted')
        self.assertEqual(world.s['stocks'], stocks); self.assertEqual(world.s['elapsed_time'], elapsed)
        loaded = host.load(); saved = loaded.save(); writes = host.writes
        self.assertEqual(intent.execute(loaded, offered_request, current_scope=self.scope(loaded), persist=host.persist,
                                       explicitly_accepted=True), offered)
        self.assertEqual(intent.execute(loaded, accepted_request, current_scope=self.scope(loaded), persist=host.persist,
                                       explicitly_accepted=True), accepted)
        self.assertEqual(loaded.save(), saved); self.assertEqual(host.writes, writes)
        with self.assertRaises(shared.SharedActionUnavailable):
            intent.execute(loaded, accepted_request, current_scope=self.scope(loaded, 'restored'), persist=host.persist,
                           explicitly_accepted=True)

    def test_quay_draft_preserves_no_offer_authority_and_real_failed_then_alternative_action(self):
        world, actor = self.create('quay'); host = AtomicTestHost(self.temp.name, world)
        report = intent.grant_offer_prerequisites(world, actor_id=actor)
        self.assertEqual(report['status'], 'not_selected'); self.assertEqual(report['actions'], [])
        self.assertEqual(intent.offer_prerequisites(world, actor_id=actor, channel_id='quay-local',
            recipient='FICTIONAL-QUAY-CONTACT', branch_id='branch-1', restore_id='restore-1')['status'], 'offer_not_selected')
        request = comm.prepare(world, request_id='speech', actor=actor, recipient='FICTIONAL-QUAY-CONTACT',
            channel_id='quay-local', command='speak', details={}, intention='I accept.', source_ref='explicit speech',
            branch_id='branch-1', restore_id='restore-1')
        result = comm.execute(world, request, current_scope=self.scope(world), persist=host.persist, explicitly_accepted=True)
        self.assertEqual(result['status'], 'testimony_received')
        self.assertNotIn('terms', result); self.assertFalse(world.s.get('grants'))
        _, failed = self.attempt(world, actor, host, 'quay-shortcut', 'shortcut', 'I try the shortcut.')
        self.assertEqual(failed['status'], 'completed_unsuccessfully')
        _, alternative = self.attempt(world, actor, host, 'quay-passage', 'passage', 'I take the covered passage.')
        self.assertEqual(alternative['status'], 'completed_successfully')
        self.assertEqual(world.s['elapsed_time']['seconds'], 75)
        self.assertEqual(world.s['actors'][actor]['current']['location']['value'], 'passage')
        self.assertFalse(world.s.get('grants'))

    def test_distinct_stock_offer_and_grant_do_not_imply_each_other(self):
        world, actor = self.create('rise', select_stock_offers=True)
        host = AtomicTestHost(self.temp.name, world)
        terms = {'from': 'founder-home', 'to': 'oren-home', 'material': 'grain', 'quantity': 1,
                 'authority_id': 'founder-household-offer'}
        args = {'actor_id': actor, 'intention': 'I offer one portion.', 'channel_id': 'commons-local',
                'recipient': 'oren', 'command': 'offer', 'details': {'offer_id': 'grain-offer', 'terms': terms},
                'branch_id': 'branch-1', 'restore_id': 'restore-1'}
        before = world.save(); stocks = copy.deepcopy(world.s['stocks'])
        review = intent.review_communication(world, **args)
        self.assertEqual(review['status'], 'supported'); self.assertEqual(world.save(), before)
        request = intent.prepare_communication(world, request_id='stock-offer', review_id=review['review_id'], **args)
        offered = intent.execute_communication(world, request, current_scope=self.scope(world),
                                               persist=host.persist, explicitly_accepted=True)
        self.assertEqual(offered['status'], 'offered')
        self.assertFalse(world.s['grants']); self.assertEqual(world.s['stocks'], stocks)
        _, grant = self.attempt(world, actor, host, 'request_grant', 'request-grant', 'Please offer the grant.')
        self.assertEqual(grant['status'], 'completed_successfully')
        self.assertEqual(world.s['grants']['founding']['status'], 'offered')
        self.assertEqual(world.s['obligations']['grain-offer']['status'], 'offered')
        self.assertEqual(world.s['stocks'], stocks)
        saved = world.save(); writes = host.writes
        self.assertEqual(intent.execute_communication(world, request, current_scope=self.scope(world),
                                                      persist=host.persist, explicitly_accepted=True), offered)
        self.assertEqual(world.save(), saved); self.assertEqual(host.writes, writes)


if __name__ == '__main__': unittest.main()
