import copy
import json
import unittest
from irgs_reference import InvalidEvent
from r9_runtime import observe, frontier, grant, resolve, conflicts, TracedDict, Trace, plain
from r9_adapters import ReceiverWorld
from test_r7_integration import world, new_item, inspect, milestone_p
from test_work_recovery import start

def ev(eid,op,at=8,**p):return {'id':eid,'at':at,'op':op,'params':p}
def money(eid,amount=80):return ev(eid,'transfer_cash',**{'from':'farmer-a','to':'army','amount':amount})
def receiver():
    w=world();s=w.s
    s['r9_engine_bindings']={'military':'R9-proposed-receiver-v1','roman':'R9-proposed-receiver-v1'}
    s['r9_delegations']={'farm':{'active':True,'delegate':'steward','grantor':'owner','start':0,'end':20,
                                  'recipe_id':'grow','site':'farm','workers':['farmer-a']}}
    s['r9_issue_directives']={'order':{'authorized':True,'persons':['farmer-a']}}
    w=ReceiverWorld(state=s)
    w.apply('mandate',0,'authorize_mobilization',mandate='fixture',target=2)
    w.apply('enroll',1,'enroll',person='farmer-a')
    w.apply('order',2,'issue_order',order_id='order',recipient='captain',deadline=20)
    w.apply('received',3,'receive_order',order_id='order')
    return w
def roman():return ev('roman','rom_start_delegated_job',delegation_id='farm',delegate='steward',job_id='farm',recipe_id='grow',workers=['farmer-a'],start=8,end=12)
def military():return ev('mil','mil_issue_received_order',order_id='order',commander='captain',persons=['farmer-a'])

class FullPathTests(unittest.TestCase):
    def test_fabrication_observed(self):
        w=world();e=ev('fab','make_intermediate',item_id='A',site='farm',profile_ref='shield-fixture',work_evidence_ref='test',material_source_ref='test')
        c=observe(w.s,e)
        self.assertIn(('r7_intermediates','A'),c['writes'])
        self.assertIn(('r7_profiles','shield-fixture','input_qty'),c['reads'])
    def test_wip_loss_post_dispatch_reconciliation(self):
        w=world();new_item(w)
        c=observe(w.s,ev('loss','physical_loss',9,location='wip:A',material='unfinished-shield',quantity=1,cause_ref='test',evidence_ref='test'))
        self.assertIn(('r7_intermediates','A','physical_qty'),c['writes'])
        self.assertIn(('r7_intermediates','A','status'),c['writes'])
    def test_milestone_traces_model_and_progress(self):
        w=world();start(w);c=observe(w.s,ev('mile','record_work_milestone',9,**milestone_p(8,9)))
        self.assertTrue(any(p[:2]==('r6_progress','farm') for p in c['writes']))
        self.assertTrue(any(p[:1]==('r6_model_bindings',) for p in c['reads']))
    def test_loss_and_milestone_conflict(self):
        w=world();start(w)
        a=ev('mile','record_work_milestone',9,**milestone_p(8,9))
        b=ev('loss','physical_loss',9,location='farm',material='seed',quantity=9,cause_ref='test',evidence_ref='test')
        self.assertTrue(conflicts(observe(w.s,a),observe(w.s,b)))
    def test_validation_separate(self):
        c=observe(world().s,money('a',1))
        self.assertTrue(c['validation_reads'])
        self.assertNotIn(('population','baseline'),c['reads'])
    def test_negative_and_scan(self):
        t=Trace();d=TracedDict({'jobs':{}},t)
        self.assertIsNone(d['jobs'].get('missing'));list(d['jobs'].values())
        self.assertIn(('jobs','missing','@exists'),t.reads);self.assertIn(('jobs',),t.reads)
    def test_clone_retains_observer(self):
        t=Trace();d=copy.deepcopy(TracedDict({'a':{'b':1}},t));d['a']['b']=2
        self.assertIn(('a','b'),t.writes);self.assertEqual(plain(d),{'a':{'b':2}})
    def test_observation_preserves_source(self):
        w=world();before=w.save();observe(w.s,money('a',1));self.assertEqual(w.save(),before)
    def test_unknown_rejected(self):
        with self.assertRaises(InvalidEvent):observe(world().s,ev('x','fantasy_unbound_spell'))

class ReceiverTests(unittest.TestCase):
    def test_military_executes_shared_issue_and_order(self):
        w=receiver();c=observe(w.s,military());r=frontier(w,[military()])
        self.assertEqual(r['committed'],['mil']);self.assertEqual(w.s['equipment']['farmer-a']['kit'],1)
        self.assertTrue(w.s['orders']['order']['executed'])
        self.assertIn(('r9_issue_directives','order','authorized'),c['reads'])
    def test_roman_actual_reservation(self):
        w=receiver();c=observe(w.s,roman());frontier(w,[roman()])
        self.assertEqual(w.s['econ3']['active_jobs']['farm']['reserved_inputs'],{'seed':4})
        self.assertIn(('r9_delegations','farm','active'),c['reads'])
    def test_revocation_conflicts_with_roman_start(self):
        w=receiver();revoke=ev('revoke','rom_revoke_delegation',delegation_id='farm',authority='owner',decision_ref='test')
        result=frontier(w,[roman(),revoke]);self.assertEqual(set(result['deferred']),{'roman','revoke'})
    def test_authorized_revocation_is_recorded(self):
        w=receiver();e=ev('revoke','rom_revoke_delegation',delegation_id='farm',authority='owner',decision_ref='test')
        w.apply(e['id'],e['at'],e['op'],**e['params'])
        self.assertFalse(w.s['r9_delegations']['farm']['active'])
        self.assertEqual(w.s['r9_delegations']['farm']['revoked_at'],8)
    def test_unreceived_military_order_has_no_effects(self):
        w=receiver();w.s['orders']['order']['received_at']=None;before=w.save()
        with self.assertRaises(InvalidEvent):observe(w.s,military())
        self.assertEqual(before,w.save())
    def test_unauthorized_military_directive(self):
        w=receiver();w.s['r9_issue_directives']['order']['authorized']=False
        with self.assertRaises(InvalidEvent):observe(w.s,military())
    def test_expired_delegation(self):
        w=receiver();w.s['r9_delegations']['farm']['end']=9
        with self.assertRaises(InvalidEvent):observe(w.s,roman())
    def test_cross_engine_actor_interference(self):
        w=receiver();a=roman();b=ev('capture','capture',person='farmer-a',by='army',location='camp')
        self.assertTrue(conflicts(observe(w.s,a),observe(w.s,b)))
    def test_order_execution_interferes_with_native_issue(self):
        w=receiver();b=ev('execute','execute_order',order_id='order')
        self.assertTrue(conflicts(observe(w.s,military()),observe(w.s,b)))
    def test_native_replay_idempotent(self):
        w=receiver();e=military();w.apply(e['id'],e['at'],e['op'],**e['params']);before=w.save()
        self.assertFalse(w.apply(e['id'],e['at'],e['op'],**e['params']));self.assertEqual(before,w.save())
    def test_native_failed_final_validation_atomic(self):
        w=receiver();w.s['r9_issue_directives']['order']['persons']=['farmer-b'];before=w.save()
        e=military()
        with self.assertRaises(InvalidEvent):w.apply(e['id'],e['at'],e['op'],**e['params'])
        self.assertEqual(before,w.save())

class DecisionTests(unittest.TestCase):
    def prepared(self):
        w=world();grant(w,'m','treasurer',['transfer_cash'],0,'synthetic-law')
        frontier(w,[money('a'),money('b')]);return w
    def test_conflicts_survive_reload(self):
        w=self.prepared();v=type(w).load(w.save())
        self.assertEqual(v.s['r9']['requests']['a']['status'],'unresolved')
        self.assertEqual(v.checksum(),w.checksum())
    def test_approval_executes_once_at_later_time(self):
        w=self.prepared();resolve(w,'d','a',9,'m','treasurer',True);before=w.save()
        resolve(w,'d','a',9,'m','treasurer',True)
        self.assertEqual(w.save(),before);self.assertEqual(w.s['cash']['army'],80)
        self.assertNotIn('a',w.s['processed']);self.assertEqual(w.s['journal'][-1]['at'],9)
    def test_other_request_revalidated_against_remaining_cash(self):
        w=self.prepared();resolve(w,'d','a',9,'m','treasurer',True);before=w.save()
        with self.assertRaises((InvalidEvent,AssertionError)):resolve(w,'d2','b',10,'m','treasurer',True)
        self.assertEqual(w.save(),before);self.assertEqual(w.s['r9']['requests']['b']['status'],'unresolved')
    def test_deny_has_no_cash_effect(self):
        w=self.prepared();resolve(w,'d','a',9,'m','treasurer',False)
        self.assertEqual(w.s['cash']['army'],0);self.assertEqual(w.s['r9']['requests']['a']['status'],'denied')
    def test_wrong_authority(self):
        w=self.prepared()
        with self.assertRaises(InvalidEvent):resolve(w,'d','a',9,'m','stranger',True)
    def test_revoked_mandate(self):
        w=self.prepared();w.s['r9']['mandates']['m']['active']=False
        with self.assertRaises(InvalidEvent):resolve(w,'d','a',9,'m','treasurer',True)
    def test_no_backdating(self):
        w=self.prepared()
        with self.assertRaises(InvalidEvent):resolve(w,'d','a',8,'m','treasurer',True)
    def test_altered_decision_identity(self):
        w=self.prepared();resolve(w,'d','a',9,'m','treasurer',True)
        with self.assertRaises(InvalidEvent):resolve(w,'d','a',9,'m','treasurer',False)
    def test_original_identity_cannot_be_resubmitted(self):
        w=self.prepared()
        with self.assertRaises(InvalidEvent):frontier(w,[money('a')])
    def test_unknown_persisted_without_execution(self):
        w=world();r=frontier(w,[ev('x','unsupported'),money('a')])
        self.assertEqual(set(r['deferred']),{'x','a'});self.assertEqual(w.s['cash']['army'],0)
    def test_disjoint_cash_still_commits(self):
        w=world();a=money('a',1);b=ev('b','transfer_cash',**{'from':'farmer-b','to':'person-B','amount':1})
        self.assertEqual(set(frontier(w,[a,b])['committed']),{'a','b'})
    def test_json_certificate_is_inspectable_after_save(self):
        w=self.prepared();saved=json.loads(w.save())
        self.assertTrue(saved['r9']['requests']['a']['certificate']['reads'])

if __name__=='__main__':unittest.main()
