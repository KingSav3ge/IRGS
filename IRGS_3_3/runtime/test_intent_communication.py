"""Reviewed communication intents over normal selected campaign creation."""
import copy
import json
import tempfile
import unittest
from unittest.mock import patch

import communication_contract as communication
from communication_runtime import CommunicationRequest
from runtime_contracts import WorldScope
import shared_runtime as shared
import supported_intent as api
from settlement_setup import initialize, preview, OFFER_PROFILE
from starting_selection import initialize_player, options_for_world
from test_start_readiness import raw
from test_settlement import choices
from test_solo_provider import AtomicTestHost


class IntentCommunicationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        for target in ('solo_provider.CapabilityBroker.dispatch','openai_proposals.OpenAIProposalTransport.__call__','socket.socket.connect'):
            guard=patch(target,side_effect=AssertionError('No provider/network'));guard.start();self.addCleanup(guard.stop)

    def world(self, context):
        if context=='rise':
            c=choices();c['offer_profile']=OFFER_PROFILE
            world=initialize(c,preview(c)['review_digest'],'communication-intent-rise');return world,'founder','commons-local','oren'
        w=raw(campaign='communication-intent-quay');options=options_for_world(w)
        world=initialize_player(w,{'kind':'new','name':'Synthetic courier','species':'human','opening_id':'quay-contact-v1'},
            selection_digest=options['selection_digest'],request_ref='explicit reviewed start')
        return world,world.s['player_actor_ids'][0],'quay-local','FICTIONAL-QUAY-CONTACT'

    def args(self, actor, channel, recipient, command, details):
        return dict(actor_id=actor,intention='  Exact reviewed words.\nNo rewrite.  ',channel_id=channel,
            recipient=recipient,command=command,details=details,branch_id='branch-1',restore_id='restore-1')

    def test_normal_starts_review_actual_speech_retry_and_restore_fence(self):
        for context in ('quay','rise'):
            with self.subTest(context=context):
                world,actor,channel,recipient=self.world(context);host=AtomicTestHost(self.temp.name,world)
                before=world.save();args=self.args(actor,channel,recipient,'speak',{})
                review=api.review_communication(world,**args);self.assertEqual(review['status'],'supported')
                self.assertEqual(review['intention'],args['intention']);self.assertEqual(world.save(),before)
                request=api.prepare_communication(world,request_id='speech-'+context,review_id=review['review_id'],**args)
                scope=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
                with self.assertRaises(communication.CommunicationUnavailable):
                    api.execute_communication(world,request,current_scope=scope,persist=host.persist,explicitly_accepted=False)
                self.assertEqual(world.save(),before)
                result=api.execute_communication(world,request,current_scope=scope,persist=host.persist,explicitly_accepted=True)
                self.assertEqual(result['status'],'testimony_received');self.assertEqual(result['intention'],args['intention'])
                self.assertEqual(result['communication']['truth_status'],'testimony')
                self.assertEqual(json.loads(host.path.read_text())['receipt'],result)
                loaded=host.load();saved=loaded.save();writes=host.writes
                current=WorldScope(loaded.s['campaign_id'],'branch-1','restore-1',loaded.checksum())
                recovered=api.execute_communication(loaded,CommunicationRequest.from_json(request.to_json()),
                    current_scope=current,persist=host.persist,explicitly_accepted=True)
                self.assertEqual(recovered,result);self.assertEqual(loaded.save(),saved);self.assertEqual(host.writes,writes)
                with self.assertRaises(communication.CommunicationUnavailable):
                    api.execute_communication(loaded,request,current_scope=WorldScope(loaded.s['campaign_id'],
                        'branch-1','new-restore',loaded.checksum()),persist=host.persist,explicitly_accepted=True)

    def test_ordinary_offer_review_commit_withdraw_and_invalid_account(self):
        world,actor,channel,recipient=self.world('rise');host=AtomicTestHost(self.temp.name,world)
        terms={'from':'founder-home','to':'oren-home','material':'grain','quantity':1,'authority_id':'founder-household-offer'}
        args=self.args(actor,channel,recipient,'offer',{'offer_id':'offer-1','terms':terms})
        before=world.save();stocks=copy.deepcopy(world.s['stocks']);review=api.review_communication(world,**args)
        self.assertEqual(review['status'],'supported');self.assertEqual(review['selection']['details']['terms'],terms)
        self.assertEqual(world.save(),before)
        with self.assertRaises(shared.SharedActionUnavailable):
            api.prepare_communication(world,request_id='offer',review_id='stale',**args)
        request=api.prepare_communication(world,request_id='offer',review_id=review['review_id'],**args)
        scope=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
        result=api.execute_communication(world,request,current_scope=scope,persist=host.persist,explicitly_accepted=True)
        self.assertEqual(result['status'],'offered');self.assertEqual(world.s['stocks'],stocks)
        self.assertEqual(world.s['obligations']['offer-1']['status'],'offered')
        withdrawal=self.args(actor,channel,recipient,'withdraw',{'offer_id':'offer-1','terms_digest':result['communication']['terms_digest']})
        review=api.review_communication(world,**withdrawal);self.assertEqual(review['status'],'supported')
        request=api.prepare_communication(world,request_id='withdraw',review_id=review['review_id'],**withdrawal)
        scope=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
        self.assertEqual(api.execute_communication(world,request,current_scope=scope,persist=host.persist,explicitly_accepted=True)['status'],'withdrawn')
        self.assertEqual(world.s['stocks'],stocks)
        bad=self.args(actor,channel,recipient,'offer',{'offer_id':'bad','terms':{**terms,'from':'oren-home'}})
        review=api.review_communication(world,**bad);self.assertEqual(review['status'],'supported')
        request=api.prepare_communication(world,request_id='bad',review_id=review['review_id'],**bad)
        before=world.save();scope=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
        with self.assertRaises(communication.CommunicationUnavailable):
            api.execute_communication(world,request,current_scope=scope,persist=host.persist,explicitly_accepted=True)
        self.assertEqual(world.save(),before)

    def test_unsupported_missing_and_invalid_command_are_never_committed(self):
        world,actor,channel,recipient=self.world('quay');before=world.save()
        for command,details,status in [(None,None,'clarification_required'),('invented',{},'unsupported'),('offer',{},'unsupported')]:
            args=self.args(actor,channel,recipient,command,details);review=api.review_communication(world,**args)
            self.assertEqual(review['status'],status);self.assertIsNone(review['selection'])
            with self.assertRaises(shared.SharedActionUnavailable):api.prepare_communication(world,request_id='x',review_id=review['review_id'],**args)
        self.assertEqual(world.save(),before)

    def test_failed_persistence_keeps_world_and_explicit_request(self):
        world,actor,channel,recipient=self.world('rise');args=self.args(actor,channel,recipient,'speak',{})
        review=api.review_communication(world,**args);request=api.prepare_communication(world,request_id='fail',review_id=review['review_id'],**args)
        before=world.save();scope=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
        def fail(*_):raise OSError('synthetic failed save')
        with self.assertRaises(OSError):api.execute_communication(world,request,current_scope=scope,persist=fail,explicitly_accepted=True)
        self.assertEqual(world.save(),before)


if __name__=='__main__':unittest.main()
