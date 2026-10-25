"""Explicit synthetic channel/authority policies; no adopted historical rule."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import copy
from pathlib import Path
import tempfile
import unittest

from communication_runtime import CommunicationRequest, OPERATION, execute, prepare, presentation, received
from core_world import CoreWorld
from irgs_reference import canon
from r9_runtime import frontier, grant
from settlement_setup import initialize, preview
from solo_provider import CapabilityUnavailable, WorldScope
from test_settlement import choices
from test_solo_provider import AtomicTestHost


class CommunicationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        c=choices();c['permission']='held'
        self.world=initialize(c,preview(c)['review_digest'],'communication-fixture')
        self.world.s['player_actor_ids'].append('oren')  # Explicit synthetic dual actor control.
        for actor in ('founder','oren'):
            grant(self.world,actor+'-custody',actor,['transfer_stock'],self.world.s['clock']+1,'synthetic custody selection')
        self.world.s['communication_rules']={'schema_version':1,'source_ref':'synthetic-reviewed-local-channel',
            'time_model':'causal_only_no_elapsed_rule','stock_profile':'settlement_free_stock',
            'channels':{'local':{'mode':'co_located','actors':['founder','oren']}},
            'stock_authorities':{'founder-custody':['founder-home'],'oren-custody':['oren-home']}}
        self.host=AtomicTestHost(self.temp.name,self.world);self.counter=0

    def scope(self):
        return WorldScope(self.world.s['campaign_id'],'branch-1',self.host.restore_id,self.world.checksum())

    def request(self,command,details=None,actor='founder',text=None):
        self.counter+=1
        return prepare(self.world,request_id='speech-'+str(self.counter),actor=actor,
            recipient='oren' if actor=='founder' else 'founder',channel_id='local',command=command,
            details=details or {},intention=text or 'Explicit synthetic '+command,
            source_ref='synthetic-speech-source',branch_id='branch-1',restore_id=self.host.restore_id)

    def submit(self,request,**changes):
        kwargs=dict(current_scope=self.scope(),persist=self.host.persist,explicitly_accepted=True)
        kwargs.update(changes)
        return execute(self.world,request,**kwargs)

    def act(self,command,details=None,**kwargs):return self.submit(self.request(command,details,**kwargs))

    def terms(self,quantity=2,actor='founder',material='grain'):
        return {'from':actor+'-home','to':'oren-home' if actor=='founder' else 'founder-home',
                'material':material,'quantity':quantity,'authority_id':actor+'-custody'}

    def offer(self,offer_id='offer-1',**kwargs):
        return self.act('offer',{'offer_id':offer_id,'terms':self.terms(**kwargs)})

    def assert_rejected(self,fn,code='communication_unavailable'):
        before=self.world.save()
        with self.assertRaises(CapabilityUnavailable) as error:fn()
        self.assertEqual(error.exception.code,code);self.assertEqual(self.world.save(),before)
        return error.exception

    def test_preparation_changes_nothing_and_speech_remains_attributed_testimony(self):
        before=self.world.save()
        request=self.request('speak',text='A witness says the ferry operates at dawn; this is unverified.')
        self.assertEqual(self.world.save(),before)
        result=self.submit(request)
        evidence=self.world.s['evidence'][result['evidence_id']]
        self.assertEqual(evidence['status'],'testimony');self.assertEqual(evidence['originator'],'founder')
        self.assertEqual(evidence['assertion'],request.intention)
        self.assertIn(result['evidence_id'],self.world.s['knowledge']['oren'])
        self.assertEqual(self.world.s['elapsed_time']['seconds'],0)
        self.assertEqual(result['elapsed_status'],'not_resolved')
        from solo_actions import prepare_request
        model=prepare_request(self.world,request_id='review-testimony',actor_id='founder',
            intention='Recall the sourced statement.',branch_id='branch-1',restore_id='restore-1',
            allowed_routes=('offline',),classification='synthetic-approved',policy_ref='synthetic-policy',
            config_version='synthetic-v1',deadline=100)
        projected=next(row for row in model.model_input()['context']['received'] if row['id']==result['evidence_id'])
        self.assertEqual(projected['originator'],'founder');self.assertEqual(projected['status'],'testimony')
        narrated=presentation(self.world,'oren',request.request_id)
        self.assertEqual(narrated['speaker'],'founder');self.assertEqual(narrated['at'],result['at'])

    def test_words_of_acceptance_do_not_purchase_transfer_or_accept_an_offer(self):
        self.offer();stocks=copy.deepcopy(self.world.s['stocks'])
        result=self.act('speak',actor='oren',text='I accept and take all the grain.')
        self.assertEqual(self.world.s['obligations']['offer-1']['status'],'offered')
        self.assertEqual(self.world.s['stocks'],stocks)
        self.assertIsNone(presentation(self.world,'oren',result['request_id'])['committed_transfer'])

    def test_explicit_acceptance_transfers_conserved_stock_once_and_grounds_presentation(self):
        offer=self.offer();before=copy.deepcopy(self.world.s['stocks'])
        request=self.request('accept',{'offer_id':'offer-1','terms_digest':offer['terms_digest']},actor='oren')
        result=self.submit(request);self.world=self.host.load()
        saved=self.world.save();self.assertEqual(self.submit(request),result);self.assertEqual(self.world.save(),saved)
        self.assertEqual(self.world.s['stocks']['founder-home']['grain'],before['founder-home']['grain']-2)
        self.assertEqual(self.world.s['stocks']['oren-home']['grain'],before['oren-home']['grain']+2)
        self.assertEqual(self.world.s['obligations']['offer-1']['status'],'fulfilled')
        narrated=presentation(self.world,'founder',request.request_id)
        self.assertEqual(narrated['committed_transfer']['quantity'],2)
        self.assertEqual(narrated['utterance_status'],'testimony')

    def test_malformed_or_changed_terms_do_not_change_original_semantic_payload(self):
        offer=self.offer()
        self.assert_rejected(lambda:self.act('accept',{'offer_id':'offer-1','terms_digest':'changed'},actor='oren'))
        self.assert_rejected(lambda:self.act('accept',{'offer_id':'offer-1','terms_digest':offer['terms_digest'],
                                                     'quantity':1000},actor='oren'))
        self.assertEqual(self.world.s['obligations']['offer-1']['quantity'],2)

    def test_insufficient_stock_and_protected_seed_reject_atomically_without_partial_information(self):
        offer=self.offer(quantity=11)  # Offers do not use hidden feasibility to select winners.
        count=len(self.world.s['evidence'])
        error=self.assert_rejected(lambda:self.act('accept',{'offer_id':'offer-1','terms_digest':offer['terms_digest']},actor='oren'))
        self.assertEqual(len(self.world.s['evidence']),count)
        self.assertTrue(error.dependencies['reads']);self.assertEqual(error.dependencies['writes'],[])
        self.assertEqual(self.world.s['stocks']['founder-home']['grain'],12)

    def test_revoked_authority_and_lost_offerer_control_revalidate_on_acceptance(self):
        offer=self.offer();self.world.s['r9']['mandates']['founder-custody']['active']=False
        self.host.install(self.world)
        self.assert_rejected(lambda:self.act('accept',{'offer_id':'offer-1','terms_digest':offer['terms_digest']},actor='oren'))
        self.world.s['r9']['mandates']['founder-custody']['active']=True
        self.world.s['player_actor_ids'].remove('founder');self.host.install(self.world)
        self.assert_rejected(lambda:self.act('accept',{'offer_id':'offer-1','terms_digest':offer['terms_digest']},actor='oren'))

    def test_withdraw_decline_and_counteroffer_preserve_distinct_meanings(self):
        offered=self.offer()
        self.act('withdraw',{'offer_id':'offer-1','terms_digest':offered['terms_digest']})
        self.assert_rejected(lambda:self.act('accept',{'offer_id':'offer-1','terms_digest':offered['terms_digest']},actor='oren'))
        offered=self.offer('offer-2')
        self.act('decline',{'offer_id':'offer-2','terms_digest':offered['terms_digest']},actor='oren')
        self.assertEqual(self.world.s['obligations']['offer-2']['status'],'declined')
        self.offer('offer-3')
        counter=self.act('counteroffer',{'offer_id':'counter','counter_to':'offer-3',
            'terms':self.terms(quantity=1,actor='oren')},actor='oren')
        self.assertEqual(counter['supersedes'],'offer-3')
        self.assertEqual(self.world.s['obligations']['offer-3']['status'],'superseded')
        self.assertEqual(self.world.s['obligations']['counter']['status'],'offered')

    def test_missing_selected_channel_or_remote_recipient_cannot_invent_reception(self):
        self.world.s['actors']['oren']['current']['location']='clearing';self.host.install(self.world)
        self.assert_rejected(lambda:self.act('speak'))
        self.world.s['actors']['oren']['current']['location']='commons'
        del self.world.s['communication_rules'];self.host.install(self.world)
        self.assert_rejected(lambda:self.act('speak'))

    def test_no_explicit_acceptance_or_foreign_view_is_authorized(self):
        request=self.request('speak')
        self.assert_rejected(lambda:self.submit(request,explicitly_accepted=False),'acceptance_required')
        self.submit(request)
        self.assert_rejected(lambda:received(self.world,'elin'),'actor_denied')
        self.assert_rejected(lambda:presentation(self.world,'elin',request.request_id),'actor_denied')
        self.assertEqual(received(self.world,'oren')[0]['request_id'],request.request_id)

    def test_lost_acknowledgment_and_restore_preserve_receipt_without_repeating_transfer(self):
        offered=self.offer();saved=self.world.save()
        request=self.request('accept',{'offer_id':'offer-1','terms_digest':offered['terms_digest']},actor='oren')
        pending=Path(self.temp.name)/'pending-communication.json';pending.write_text(request.to_json())
        def lost(scope,save,receipt):self.host.persist(scope,save,receipt);raise OSError('synthetic lost acknowledgment')
        with self.assertRaises(OSError):self.submit(request,persist=lost)
        self.world=self.host.load();request=CommunicationRequest.from_json(pending.read_text())
        before=self.world.save();self.submit(request)
        self.assertEqual(self.world.save(),before)
        self.world=CoreWorld.load(saved);self.host.restore_id='restore-2';self.host.install(self.world)
        self.assert_rejected(lambda:self.submit(request),'stale_scope')

    def test_concurrent_delivery_accepts_once(self):
        offered=self.offer()
        request=self.request('accept',{'offer_id':'offer-1','terms_digest':offered['terms_digest']},actor='oren')
        saved,scope=self.world.save(),self.scope()
        def accept(_):
            try:return execute(CoreWorld.load(saved),request,current_scope=scope,persist=self.host.persist,explicitly_accepted=True)
            except CapabilityUnavailable as error:return error.code
        with ThreadPoolExecutor(2) as pool:results=list(pool.map(accept,range(2)))
        self.assertEqual(sum(isinstance(r,dict) for r in results),1)
        self.assertEqual(self.host.load().s['stocks']['founder-home']['grain'],10)

    def test_late_evidence_collision_rolls_back_transfer_and_retains_attempted_dependencies(self):
        offered=self.offer()
        request=self.request('accept',{'offer_id':'offer-1','terms_digest':offered['terms_digest']},actor='oren')
        self.world.apply('prior-evidence',self.world.s['clock']+1,'record_evidence',
            campaign_id=self.world.s['campaign_id'],source_ref='synthetic collision fixture',
            evidence_id='communication:'+request.request_id,subject='founder',
            assertion='Existing unrelated testimony.',status='testimony')
        self.host.install(self.world)
        request=replace(request,scope=self.scope())
        error=self.assert_rejected(lambda:self.submit(request))
        self.assertEqual(self.world.s['obligations']['offer-1']['status'],'offered')
        self.assertEqual(error.dependencies['writes'],[])
        self.assertTrue(error.dependencies['attempted_writes'])

    def test_competing_acceptances_have_no_arrival_order_resource_winner(self):
        offers=[self.offer('scarce-'+str(i),quantity=10) for i in range(2)]
        events=[];at=self.world.s['clock']+1
        for i,offer in enumerate(offers):
            request=self.request('accept',{'offer_id':'scarce-'+str(i),'terms_digest':offer['terms_digest']},actor='oren')
            events.append({'id':'communication:'+request.request_id,'at':at,'op':OPERATION,'params':{
                'campaign_id':self.world.s['campaign_id'],'source_ref':request.source_ref,
                'instruction_ref':request.intention,'actor':request.actor,'recipient':request.recipient,
                'request_id':request.request_id,'channel_id':request.channel_id,'command':request.command,
                'details':{'offer_id':'scarce-'+str(i),'terms_digest':offer['terms_digest']},'intention':request.intention}})
        stocks=copy.deepcopy(self.world.s['stocks'])
        for ordered in (events,list(reversed(events))):
            w=CoreWorld.load(self.world.save());result=frontier(w,ordered)
            self.assertEqual(result['committed'],[])
            self.assertEqual(w.s['stocks'],stocks)
            self.assertTrue(all(w.s['obligations']['scarce-'+str(i)]['status']=='offered' for i in range(2)))


if __name__=='__main__':unittest.main()
