import copy
import itertools
import unittest
from unittest.mock import patch
from irgs_reference import initial_world, InvalidEvent
from economic_extension import economy_fixture
from r7_frontier import R7World, footprint_r7
from r8_dependencies import Access, observe, conflicts, frontier, domain, SUPPORTED
from r8_strategy import strategic_world, advance

def world(): return R7World(state=economy_fixture(initial_world().s))
def event(eid, op, at=1, **params): return {'id': eid, 'op': op, 'at': at, 'params': params}
def transfer(eid, source, dest, amount=1):
    return event(eid, 'transfer_cash', **{'from': source, 'to': dest, 'amount': amount})

class DependencyTests(unittest.TestCase):
    def test_indirect_tax_payer_read(self):
        w = world(); w.apply('tax', 0, 'assess_tax', tax_id='t', payer='farmer-a', amount=5, authority_ref='law', basis_ref='basis')
        c = observe(w.s, event('pay', 'pay_tax', tax_id='t', amount=2))
        self.assertIn(('econ3','tax_claims','t','payer'), c['reads'])
        self.assertIn(('cash','farmer-a'), c['writes'])

    def test_hidden_formation_dependency_missing_in_r7(self):
        w = world(); w.apply('mandate', 0, 'authorize_mobilization', mandate='fixture', target=2)
        w.apply('enroll', 0, 'enroll', person='farmer-a')
        a = event('kit', 'issue_kits', persons=['farmer-a'])
        b = event('new-recruit', 'enroll', person='farmer-b')
        self.assertFalse(footprint_r7(w.s, a) & footprint_r7(w.s, b))
        self.assertTrue(conflicts(observe(w.s,a), observe(w.s,b)))

    def test_disjoint_cash_orders_equivalent(self):
        events = [transfer('a','farmer-a','army'), transfer('b','farmer-b','person-B')]
        states = []
        for order in itertools.permutations(events):
            w = world(); result = frontier(w,list(order))
            self.assertEqual(len(result['committed']),2); states.append(domain(w.s))
        self.assertEqual(*states)

    def test_contention_has_no_identifier_winner(self):
        w = world(); before = w.save()
        result = frontier(w,[transfer('z','farmer-a','army',80),transfer('a','farmer-a','person-B',80)])
        self.assertEqual(result['committed'],[]); self.assertEqual(w.save(),before)

    def test_independent_component_survives_conflict(self):
        w = world()
        r = frontier(w,[transfer('a','farmer-a','army'),transfer('b','farmer-a','person-B'),
                        event('budget','authorize_budget',name='roads',amount=10)])
        self.assertEqual(r['committed'],['budget']); self.assertEqual(len(r['deferred']),2)

    def test_read_read_does_not_conflict(self):
        a = {'reads':[('cash','x')], 'writes':[]}
        self.assertFalse(conflicts(a,a))

    def test_missing_key_dependency(self):
        reads,writes = set(),set(); s = Access({'claims':{}},reads,writes)
        self.assertIsNone(s['claims'].get('new'))
        self.assertTrue(conflicts({'reads':list(reads),'writes':[]}, {'reads':[], 'writes':[('claims','new')]}))

    def test_scan_detects_phantom(self):
        reads,writes = set(),set(); s=Access({'jobs':{}},reads,writes)
        self.assertEqual(list(s['jobs'].values()),[])
        self.assertTrue(conflicts({'reads':list(reads),'writes':[]},{'reads':[],'writes':[('jobs','new')]}))

    def test_parent_replacement_conflict(self):
        self.assertTrue(conflicts({'reads':[('a','b')],'writes':[]},{'reads':[],'writes':[('a',)]}))

    def test_setdefault_list_mutation(self):
        w=world(); c=observe(w.s,event('shift','commit_shift',person='child-1',start=2,end=3,role='fixture'))
        self.assertIn(('commitments','child-1'),c['writes'])

    def test_deleted_and_same_value_writes(self):
        reads,writes=set(),set(); s=Access({'a':1,'b':2},reads,writes)
        s['a']=1; del s['b']
        self.assertEqual(writes,{('a',),('b',)})

    def test_stale_certificate(self):
        w=world(); events=[transfer('a','farmer-a','army')]; certs=[observe(w.s,events[0])]
        w.apply('change',0,'authorize_budget',name='roads',amount=1)
        with self.assertRaises(InvalidEvent): frontier(w,events,certs)

    def test_altered_certificate(self):
        w=world(); events=[transfer('a','farmer-a','army')]; certs=[observe(w.s,events[0])]
        certs[0]['reads']=[]
        with self.assertRaises(InvalidEvent): frontier(w,events,certs)

    def test_unknown_operation_blocks_batch(self):
        w=world(); before=w.save()
        r=frontier(w,[transfer('a','farmer-a','army'),event('opaque','plugin_magic')])
        self.assertFalse(r['committed']); self.assertEqual(w.save(),before)

    def test_r7_extension_not_silently_certified(self):
        self.assertNotIn('make_intermediate',SUPPORTED)
        self.assertNotIn('record_work_milestone',SUPPORTED)

    def test_failed_precondition_no_live_write(self):
        w=world(); before=w.save()
        r=frontier(w,[transfer('a','farmer-a','army',999)])
        self.assertTrue(r['failures']); self.assertEqual(w.save(),before)

    def test_duplicate_ids_rejected(self):
        w=world(); e=transfer('a','farmer-a','army')
        with self.assertRaises(InvalidEvent): frontier(w,[e,e])

    def test_mixed_times_rejected(self):
        w=world(); a=transfer('a','farmer-a','army'); b=transfer('b','farmer-b','person-B'); b['at']=2
        with self.assertRaises(InvalidEvent): frontier(w,[a,b])

    def test_observation_does_not_mutate_source(self):
        w=world(); before=w.save(); observe(w.s,transfer('a','farmer-a','army'))
        self.assertEqual(before,w.save())

    def test_all_pairwise_cash_predictions_against_actual_interleavings(self):
        names=['farmer-a','farmer-b','person-B','army']
        events=[transfer(str(i),a,b) for i,(a,b) in enumerate(itertools.permutations(names,2)) if a!='army']
        w=world(); certs=[observe(w.s,e) for e in events]
        checked=0
        for i,a in enumerate(events):
            for j,b in enumerate(events[:i]):
                if conflicts(certs[i],certs[j]): continue
                outcomes=[]
                for order in ((a,b),(b,a)):
                    trial=world()
                    for e in order: trial.apply(e['id'],e['at'],e['op'],**e['params'])
                    outcomes.append(domain(trial.s))
                self.assertEqual(*outcomes); checked+=1
        self.assertGreater(checked,0)

class StrategyTests(unittest.TestCase):
    def test_autonomous_four_institutions(self):
        w=advance(strategic_world(),12)
        self.assertEqual(w.s['econ3']['meals_delivered']['house-1'],6)
        self.assertEqual(w.s['cash']['treasury'],602)
        self.assertEqual(w.s['equipment']['farmer-a']['kit'],1)
        self.assertEqual(w.s['wage_due']['person-B'],2)

    def test_exhaustion_stops_real_production(self):
        w=advance(strategic_world(grain=2,fuel=1),18)
        self.assertEqual(w.s['econ3']['produced']['meal'],3)
        self.assertEqual(w.s['econ3']['consumed']['grain'],2)
        self.assertEqual(len(w.s['econ3']['completed_jobs']),1)

    def test_save_resume_same_state(self):
        continuous=advance(strategic_world(),18)
        split=advance(strategic_world(),7)
        split=advance(R7World.load(split.save()),18)
        self.assertEqual(continuous.checksum(),split.checksum())

    def test_policy_edit_rejected(self):
        w=strategic_world(); w.s['r8_strategy']['profile']['tax_amount']=50
        with self.assertRaises(InvalidEvent): advance(w,1)

    def test_disabled_worker_changes_decisions(self):
        w=strategic_world(); w.s['actors']['person-B']['disabled']=True
        advance(w,6)
        self.assertEqual(w.s['econ3']['produced']['meal'],0)
        self.assertEqual(w.s['econ3']['active_jobs'],{})

    def test_planner_records_condition_reads(self):
        w=advance(strategic_world(),1)
        paths=w.s['r8_strategy']['decisions'][0]['reads']
        self.assertIn(('actors','person-B','disabled'),paths)
        self.assertIn(('econ3','stocks','house-1','grain'),paths)

if __name__=='__main__': unittest.main()
