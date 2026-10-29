"""Normal-start review, explicit acceptance, actual effects and immutable replay."""
import json
import tempfile
import unittest
from dataclasses import replace
from unittest.mock import patch

import supported_intent as api
import shared_runtime as shared
from runtime_contracts import AcceptedIntent, WorldScope
from settlement_setup import initialize, preview
from starting_selection import initialize_player, options_for_world
from test_settlement import choices
from test_start_readiness import raw
from test_solo_provider import AtomicTestHost


class SupportedIntentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        for target in ('solo_provider.CapabilityBroker.dispatch', 'openai_proposals.OpenAIProposalTransport.__call__', 'socket.socket.connect'):
            guard = patch(target, side_effect=AssertionError('No provider or network')); guard.start(); self.addCleanup(guard.stop)

    def world(self, context):
        if context == 'rise':
            selected=choices(); world=initialize(selected,preview(selected)['review_digest'],'synthetic-intent-rise')
        else:
            new=raw(campaign='synthetic-intent-quay'); options=options_for_world(new)
            world=initialize_player(new,{'kind':'new','name':'Synthetic courier','species':'human','opening_id':'quay-contact-v1'},
                selection_digest=options['selection_digest'],request_ref='explicit reviewed start')
        return world, world.s['player_actor_ids'][0]

    def capability(self, world, actor, action):
        return next(c for c in shared.capabilities(world, actor) if json.loads(c.action_json).get('action_id')==action)

    def test_two_ordinary_contexts_review_actual_action_and_immutable_retry(self):
        for context, action, expected in [('rise','walk_clearing','completed_successfully'),
                                          ('quay','quay-shortcut','completed_unsuccessfully')]:
            with self.subTest(context=context):
                world,actor=self.world(context); host=AtomicTestHost(self.temp.name,world)
                cap=self.capability(world,actor,action); words='  Exact attempt: '+action+'\nNo silent rewrite.  '
                before=world.save(); review=api.review(world,actor_id=actor,intention=words,capability_id=cap.capability_id,branch_id='b',restore_id='r')
                self.assertEqual(review['status'],'supported'); self.assertEqual(review['selection']['action']['action_id'],action)
                request=api.prepare(world,request_id='run-'+context,actor_id=actor,intention=words,capability_id=cap.capability_id,
                    review_id=review['review_id'],branch_id='b',restore_id='r')
                self.assertEqual(world.save(),before)
                host.install(world)
                # AtomicTestHost uses branch-1/restore-1; bind review to its actual scope.
                review=api.review(world,actor_id=actor,intention=words,capability_id=cap.capability_id,branch_id='branch-1',restore_id='restore-1')
                request=api.prepare(world,request_id='run-'+context,actor_id=actor,intention=words,capability_id=cap.capability_id,
                    review_id=review['review_id'],branch_id='branch-1',restore_id='restore-1')
                scope=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
                with self.assertRaises(shared.SharedActionUnavailable):
                    api.execute(world,request,current_scope=scope,persist=host.persist,explicitly_accepted=False)
                self.assertEqual(world.save(),before)
                result=api.execute(world,request,current_scope=scope,persist=host.persist,explicitly_accepted=True)
                self.assertEqual(result['status'],expected);self.assertEqual(result['intention'],words)
                self.assertEqual(json.loads(host.path.read_text())['receipt'],result)
                next_action='walk_commons' if context=='rise' else 'look-quay'
                next_cap=self.capability(world,actor,next_action)
                next_args=dict(actor_id=actor,intention='Second explicit action.',capability_id=next_cap.capability_id,
                               branch_id='branch-1',restore_id='restore-1')
                next_review=api.review(world,**next_args)
                second=api.prepare(world,request_id='next-'+context,review_id=next_review['review_id'],**next_args)
                next_scope=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
                self.assertEqual(api.execute(world,second,current_scope=next_scope,persist=host.persist,
                                             explicitly_accepted=True)['status'],'completed_successfully')
                world=host.load();saved=world.save();writes=host.writes
                current=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
                replay=api.execute(world,AcceptedIntent.from_json(request.to_json()),current_scope=current,persist=host.persist,explicitly_accepted=True)
                self.assertEqual(replay,result);self.assertEqual(world.save(),saved);self.assertEqual(host.writes,writes)
                with self.assertRaises(shared.SharedActionUnavailable):
                    api.execute(world,request,current_scope=replace(current,restore_id='restored'),persist=host.persist,explicitly_accepted=True)

    def test_unsupported_and_ambiguous_preserve_exact_text_and_do_not_prepare(self):
        world,actor=self.world('quay');before=world.save();words='  Request an unknown effect.  '
        for capability,status in [(None,'clarification_required'),('unknown','unsupported')]:
            reviewed=api.review(world,actor_id=actor,intention=words,capability_id=capability,branch_id='b',restore_id='r')
            self.assertEqual(reviewed['status'],status);self.assertEqual(reviewed['intention'],words)
            with self.assertRaises(shared.SharedActionUnavailable):
                api.prepare(world,request_id='not-committed',actor_id=actor,intention=words,capability_id=capability,
                    review_id=reviewed['review_id'],branch_id='b',restore_id='r')
        self.assertEqual(world.save(),before)

    def test_changed_review_and_actual_wrong_origin_reject_without_effect(self):
        world,actor=self.world('rise'); cap=self.capability(world,actor,'walk_commons'); before=world.save()
        args=dict(actor_id=actor,intention='Walk to the commons.',capability_id=cap.capability_id,branch_id='b',restore_id='r')
        review=api.review(world,**args)
        with self.assertRaises(shared.SharedActionUnavailable):api.prepare(world,request_id='x',review_id='stale',**args)
        request=api.prepare(world,request_id='x',review_id=review['review_id'],**args)
        with self.assertRaises(shared.SharedActionUnavailable):
            api.execute(world,request,current_scope=WorldScope(world.s['campaign_id'],'b','r',world.checksum()),
                persist=lambda *_:self.fail('refusal must not persist'),explicitly_accepted=True)
        self.assertEqual(world.save(),before)

    def test_ordinary_offer_prerequisites_do_not_invent_authority_or_consent(self):
        for context, channel, recipient in [('rise','commons-local','oren'),
                                             ('quay','quay-local','FICTIONAL-QUAY-CONTACT')]:
            with self.subTest(context=context):
                world,actor=self.world(context); before=world.save()
                args=dict(actor_id=actor,channel_id=channel,recipient=recipient,branch_id='b',restore_id='r')
                packet=api.offer_prerequisites(world,**args)
                self.assertEqual(packet['status'],'offer_not_selected')
                self.assertEqual(packet['authority_and_resources'],'checked_on_execution')
                self.assertFalse(packet['committed'])
                args['recipient']='unknown'
                self.assertEqual(api.offer_prerequisites(world,**args)['status'],'participant_unavailable')
                self.assertEqual(world.save(),before)


if __name__=='__main__':unittest.main()
