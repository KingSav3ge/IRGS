"""Explicitly reviewed fictional founder offers without NPC consent or transfer."""
import copy
import tempfile
import unittest
from unittest.mock import patch

import communication_contract as communication
import supported_intent
from runtime_contracts import WorldScope
from settlement_setup import initialize, preview, OFFER_PROFILE
from test_settlement import choices
from test_solo_provider import AtomicTestHost


class OrdinaryOfferProfileTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        for target in ('solo_provider.CapabilityBroker.dispatch','openai_proposals.OpenAIProposalTransport.__call__','socket.socket.connect'):
            guard=patch(target,side_effect=AssertionError('No network/provider'));guard.start();self.addCleanup(guard.stop)
        selected=choices();selected['offer_profile']=OFFER_PROFILE
        self.review=preview(selected);self.world=initialize(selected,self.review['review_digest'],'ordinary-offer')
        self.host=AtomicTestHost(self.temp.name,self.world)

    def scope(self):
        return WorldScope(self.world.s['campaign_id'],'branch-1','restore-1',self.world.checksum())

    def request(self, request_id, command, details, recipient='oren'):
        return communication.prepare(self.world,request_id=request_id,actor='founder',recipient=recipient,
            channel_id='commons-local',command=command,details=details,intention='Exact reviewed '+command+' words.',
            source_ref='explicit offer',branch_id='branch-1',restore_id='restore-1')

    def submit(self, request, **kwargs):
        args=dict(current_scope=self.scope(),persist=self.host.persist,explicitly_accepted=True);args.update(kwargs)
        return communication.execute(self.world,request,**args)

    def test_optional_review_and_offer_proposal_withdrawal_and_replay(self):
        self.assertIn('no recipient consent',self.review['offer_setup']['notice'])
        mandate=self.world.s['r9']['mandates']['founder-household-offer']
        self.assertEqual(mandate['operations'],['execute_local_communication'])
        self.assertEqual(mandate['offer_scope'],{'purpose':'household-offer','account':'founder-home'})
        packet=supported_intent.offer_prerequisites(self.world,actor_id='founder',channel_id='commons-local',
            recipient='oren',branch_id='branch-1',restore_id='restore-1')
        self.assertEqual(packet['status'],'attemptable');before=self.world.save();stocks=copy.deepcopy(self.world.s['stocks'])
        terms={'from':'founder-home','to':'oren-home','material':'grain','quantity':1,'authority_id':'founder-household-offer'}
        request=self.request('offer-1','offer',{'offer_id':'gift-1','terms':terms})
        with self.assertRaises(communication.CommunicationUnavailable):self.submit(request,explicitly_accepted=False)
        self.assertEqual(self.world.save(),before)
        result=self.submit(request);self.assertEqual(result['status'],'offered')
        self.assertEqual(self.world.s['stocks'],stocks)
        self.assertEqual(self.world.s['obligations']['gift-1']['status'],'offered')
        self.world=self.host.load();saved=self.world.save();writes=self.host.writes
        self.assertEqual(self.submit(request),result);self.assertEqual(self.world.save(),saved);self.assertEqual(self.host.writes,writes)
        withdrawal=self.request('withdraw-1','withdraw',{'offer_id':'gift-1','terms_digest':result['terms_digest']})
        withdrawn=self.submit(withdrawal);self.assertEqual(withdrawn['status'],'withdrawn')
        self.assertEqual(self.world.s['stocks'],stocks)
        self.assertEqual(self.world.s['obligations']['gift-1']['status'],'withdrawn')

    def test_invalid_recipient_and_unauthorized_account_reject_atomically(self):
        terms={'from':'founder-home','to':'oren-home','material':'grain','quantity':1,'authority_id':'founder-household-offer'}
        for recipient,changes in [('elin',{}),('oren',{'from':'oren-home'})]:
            with self.subTest(recipient=recipient,changes=changes):
                before=self.world.save();request=self.request('bad-'+recipient,'offer',{'offer_id':'bad-'+recipient,'terms':{**terms,**changes}},recipient)
                with self.assertRaises(communication.CommunicationUnavailable):self.submit(request)
                self.assertEqual(self.world.save(),before)

    def test_legacy_default_and_stale_review_keep_offer_unselected(self):
        plain=choices();review=preview(plain);world=initialize(plain,review['review_digest'],'default')
        info=supported_intent.offer_prerequisites(world,actor_id='founder',channel_id='commons-local',
                recipient='oren',branch_id='branch-1',restore_id='restore-1')
        self.assertEqual(info['status'],'offer_not_selected')
        plain['offer_profile']=OFFER_PROFILE
        with self.assertRaises(ValueError):initialize(plain,review['review_digest'],'stale')

    def test_selected_offer_mandate_cannot_authorize_raw_stock_transfer(self):
        from irgs_reference import InvalidEvent
        from r9_runtime import frontier, resolve
        at=self.world.s['clock']+1
        def event(key):
            return {'id':key,'at':at,'op':'transfer_stock','params':{
                'campaign_id':self.world.s['campaign_id'],'source_ref':'synthetic conflicting request',
                'authority_ref':'synthetic competing authority','from':'oren-home','to':'founder-home',
                'material':'grain','quantity':1}}
        result=frontier(self.world,[event('one'),event('two')])
        self.assertEqual(set(result['deferred']),{'one','two'})
        before=self.world.save()
        with self.assertRaises(InvalidEvent):
            resolve(self.world,'deny-raw-transfer','one',self.world.s['clock']+1,
                    'founder-household-offer','founder',True)
        self.assertEqual(self.world.save(),before)


if __name__=='__main__':unittest.main()
