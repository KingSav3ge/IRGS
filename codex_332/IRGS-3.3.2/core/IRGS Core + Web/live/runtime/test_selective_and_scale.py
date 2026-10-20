"""R4 additional bounded executable regressions; numbered 76-101."""
import unittest
from irgs_reference import World, InvalidEvent, initial_world
from selective_coordinator import R4World, footprint, components
from scale_coverage import Coverage
from test_economic_integration import fresh


def r4():return R4World(initial=fresh().s)


def treasury_request(w,eid,amount,to,at=2):
    w.schedule(eid,at,'transfer_cash',**{'from':'treasury','to':to,'amount':amount})


class Round4Tests(unittest.TestCase):
    def test_76_competing_treasury_and_independent_work(self):
        w=r4();treasury_request(w,'req-army',400,'army',8);treasury_request(w,'req-care',400,'caregiver-1',8)
        w.schedule('farm-start',8,'start_job',job_id='farm',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        # R3 fixture treasury holds 600: 800 submitted exceeds actual stock.
        report=w.run_until(8)
        self.assertEqual(report['committed'],['farm-start'])
        self.assertEqual(len(report['deferred']),1)
        self.assertEqual(w.s['cash']['treasury'],600)
        self.assertIn('farm',w.s['econ3']['active_jobs'])
        self.assertEqual(len(w.s['r4_deferred'][report['deferred'][0]]['requests']),2)

    def test_77_deferred_requests_do_not_preempt_future_unrelated_job(self):
        w=r4();treasury_request(w,'req-army',400,'army',2);treasury_request(w,'req-care',400,'caregiver-1',2)
        w.run_until(2)
        w.schedule('farm-start',8,'start_job',job_id='farm',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.schedule('farm-finish',12,'complete_job',job_id='farm')
        r=w.run_until(12)
        self.assertEqual(r['committed'],['farm-start','farm-finish'])
        self.assertEqual(w.s['econ3']['produced']['grain'],12)
        self.assertEqual(w.s['cash']['treasury'],600)

    def test_78_explicit_cash_allocation_at_later_frontier(self):
        w=r4();treasury_request(w,'req-army',400,'army');treasury_request(w,'req-care',400,'caregiver-1')
        gid=w.run_until(2)['deferred'][0]
        w.run_until(3)
        d=w.decide_deferred(gid,['req-care'],at=4,authority_ref='competent-treasurer-decision')
        self.assertEqual(d['approved_ids'],['req-care']);self.assertEqual(d['denied_ids'],['req-army'])
        self.assertEqual(w.s['cash']['treasury'],200)
        self.assertEqual(w.s['cash']['caregiver-1'],500)
        self.assertEqual(w.s['cash']['army'],0)
        self.assertEqual(w.s['r4_deferred'][gid]['at'],2)
        self.assertEqual(w.s['r4_deferred'][gid]['decision_at'],4)

    def test_79_no_default_priority_or_request_id_winner(self):
        for ids in [('aa','zz'),('zz','aa')]:
            w=r4();treasury_request(w,ids[0],400,'army');treasury_request(w,ids[1],400,'caregiver-1')
            w.run_until(2)
            self.assertEqual(w.s['cash']['treasury'],600)
            self.assertEqual(w.s['cash']['army'],0)
            self.assertEqual(w.s['cash']['caregiver-1'],100)

    def test_80_invalid_local_group_does_not_block_independent_tax(self):
        w=r4();w.schedule('bad',2,'transfer_cash',**{'from':'army','to':'caregiver-1','amount':1})
        w.schedule('tax',2,'assess_tax',tax_id='TX',payer='farmer-b',amount=12,authority_ref='tax-mandate',basis_ref='land')
        r=w.run_until(2)
        self.assertEqual(r['committed'],['tax'])
        self.assertEqual(len(r['deferred']),1)
        self.assertEqual(w.s['econ3']['tax_claims']['TX']['paid'],0)

    def test_81_independent_cash_from_distinct_source(self):
        w=r4();w.s['cash']['treasury']=500;w.s['cash']['army']=100;w.s['cash']['farmer-a']=100
        w.s['cash_baseline']=1000
        w=R4World(initial=w.s)
        w.schedule('aa',2,'transfer_cash',**{'from':'army','to':'caregiver-1','amount':80})
        w.schedule('zz',2,'transfer_cash',**{'from':'farmer-a','to':'farmer-b','amount':80})
        r=w.run_until(2)
        self.assertEqual(sorted(r['committed']),['aa','zz'])
        self.assertEqual(w.s['cash']['farmer-b'],180)

    def test_82_start_job_same_frontier_competing_stock_defers_all_competitors(self):
        w=r4()
        w.s['econ3']['sites']['farm']['workers_capacity']=2
        w.s['econ3']['stocks']['farm']['seed']=4;w.s['econ3']['consumed']['seed']=8
        w=R4World(initial=w.s)
        w.schedule('j1',8,'start_job',job_id='j1',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.schedule('j2',8,'start_job',job_id='j2',recipe_id='grow',start=8,end=12,workers=['farmer-b'])
        w.schedule('external',8,'assess_tax',tax_id='TX',payer='farmer-b',amount=5,authority_ref='tax-law',basis_ref='lot')
        r=w.run_until(8)
        self.assertIn('external',r['committed'])
        self.assertEqual(len(r['deferred']),1)
        self.assertFalse(w.s['econ3']['active_jobs'])

    def test_83_simultaneous_new_mandate_and_enrollment_remain_contested(self):
        w=r4();w.schedule('mandate',1,'authorize_mobilization',mandate='law',target=2)
        w.schedule('enrol',1,'enroll',person='farmer-a')
        w.schedule('tax',1,'assess_tax',tax_id='T',payer='farmer-b',amount=3,authority_ref='law',basis_ref='lot')
        r=w.run_until(1)
        self.assertEqual(r['committed'],['tax'])
        self.assertNotIn('mobilization',w.s['gov'])

    def test_84_simultaneous_job_finish_and_claim_need_two_frontiers(self):
        w=r4();w.apply('start',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.schedule('finish',12,'complete_job',job_id='j')
        w.schedule('wage',12,'accrue_job_wages',job_id='j',rate=2,wage_agreement_ref='W')
        w.schedule('unrelated',12,'assess_tax',tax_id='X',payer='farmer-b',amount=2,authority_ref='law',basis_ref='lot')
        r=w.run_until(12)
        self.assertEqual(r['committed'],['unrelated'])
        self.assertEqual(w.s['econ3']['produced']['grain'],0)
        self.assertNotIn('farmer-a',w.s['wage_due'])

    def test_85_different_sites_independent_and_conserve(self):
        w=r4();w.schedule('farm',8,'start_job',job_id='farm',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.schedule('kitchen',8,'start_job',job_id='kitchen',recipe_id='cook',start=8,end=12,workers=['person-B'])
        r=w.run_until(8)
        self.assertEqual(set(r['committed']),{'farm','kitchen'})
        self.assertEqual(w.s['econ3']['consumed']['grain'],0)

    def test_86_kit_overcommit_does_not_block_other_source(self):
        w=r4();w.apply('mandate',1,'authorize_mobilization',mandate='M',target=2)
        w.apply('enroll-1',2,'enroll',person='farmer-a')
        w.apply('enroll-2',3,'enroll',person='farmer-b')
        w.s['equipment']['depot']['kit']=1;w.s['kit_baseline']=1
        w=R4World(initial=w.s)
        w.schedule('k1',4,'issue_kits',persons=['farmer-a'])
        w.schedule('k2',4,'issue_kits',persons=['farmer-b'])
        w.schedule('tax',4,'assess_tax',tax_id='T',payer='farmer-a',amount=1,authority_ref='law',basis_ref='lot')
        r=w.run_until(4)
        self.assertEqual(r['committed'],['tax'])
        self.assertEqual(w.s['equipment']['depot']['kit'],1)

    def test_87_allocation_cannot_be_replayed(self):
        w=r4();treasury_request(w,'r1',400,'army');treasury_request(w,'r2',400,'caregiver-1')
        gid=w.run_until(2)['deferred'][0]
        w.decide_deferred(gid,['r1'],at=3,authority_ref='gov')
        chk=w.checksum()
        with self.assertRaises(InvalidEvent):w.decide_deferred(gid,['r2'],at=4,authority_ref='gov')
        self.assertEqual(w.checksum(),chk)

    def test_88_allocation_cannot_fake_time_or_authority(self):
        w=r4();treasury_request(w,'r1',400,'army');treasury_request(w,'r2',400,'caregiver-1')
        gid=w.run_until(2)['deferred'][0];chk=w.checksum()
        with self.assertRaises(InvalidEvent):w.decide_deferred(gid,['r1'],at=2,authority_ref='gov')
        with self.assertRaises(InvalidEvent):w.decide_deferred(gid,['r1'],at=3,authority_ref='')
        self.assertEqual(w.checksum(),chk)

    def test_89_unauthorized_selection_invalid_atomic(self):
        w=r4();treasury_request(w,'r1',400,'army');treasury_request(w,'r2',400,'caregiver-1')
        gid=w.run_until(2)['deferred'][0];chk=w.checksum()
        with self.assertRaises(InvalidEvent):w.decide_deferred(gid,['unknown'],at=3,authority_ref='gov')
        self.assertEqual(w.checksum(),chk)

    def test_90_overspend_at_decision_time_invalid_atomic(self):
        w=r4();treasury_request(w,'r1',400,'army');treasury_request(w,'r2',400,'caregiver-1')
        gid=w.run_until(2)['deferred'][0]
        w.apply('new',3,'transfer_cash',**{'from':'treasury','to':'army','amount':300})
        chk=w.checksum()
        with self.assertRaises(InvalidEvent):w.decide_deferred(gid,['r2'],at=4,authority_ref='gov')
        self.assertEqual(w.checksum(),chk)

    def test_91_unknown_operation_uses_global_footprint(self):
        w=r4();fp=footprint(w.s,{'id':'none','at':1,'op':'not_registered','params':{}})
        self.assertIn('global:unclassified-operation',fp)

    def test_92_source_idempotent_replay(self):
        c=Coverage();v=dict(source_id='s1',contributors=['farmer-a'],stream='grain',start=8,end=12,quantity=12,evidence_ref='job:j1')
        self.assertTrue(c.record(**v));chk=c.checksum()
        self.assertFalse(c.record(**v));self.assertEqual(chk,c.checksum())

    def test_93_source_replay_change_rejected(self):
        c=Coverage();c.record(source_id='a',contributors=['worker'],stream='grain',start=0,end=4,quantity=12,evidence_ref='j')
        with self.assertRaises(InvalidEvent):c.record(source_id='a',contributors=['worker'],stream='grain',start=0,end=4,quantity=13,evidence_ref='j')

    def test_94_aggregate_same_actor_overlap_rejected(self):
        c=Coverage();c.record(source_id='tactical',contributors=['farmer-a'],stream='grain',start=8,end=12,quantity=12,evidence_ref='completed:j')
        with self.assertRaises(InvalidEvent):c.record(source_id='aggregate',contributors=['farmer-a','farmer-b'],stream='grain',start=8,end=12,quantity=24,evidence_ref='unverified cohort')

    def test_95_aggregate_residual_excludes_already_detailed_actor(self):
        c=Coverage();c.record(source_id='tactical',contributors=['farmer-a'],stream='grain',start=8,end=12,quantity=12,evidence_ref='j')
        c.record(source_id='aggregate-residual',contributors=['farmer-b'],stream='grain',start=8,end=12,quantity=12,evidence_ref='cohort-B')
        self.assertEqual(c.view(0,24,'grain')['quantity_from_complete_intervals'],24)

    def test_96_daily_monthly_views_do_not_write_more_grain(self):
        w=r4();w.apply('start',8,'start_job',job_id='day',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.apply('finish',12,'complete_job',job_id='day')
        c=Coverage();c.record(source_id='finish',contributors=['farmer-a'],stream='grain',start=8,end=12,quantity=12,evidence_ref='completed_job:day')
        before=w.checksum();a=c.view(0,24,'grain');b=c.view(0,24*30,'grain')
        self.assertEqual(a['quantity_from_complete_intervals'],12)
        self.assertEqual(b['quantity_from_complete_intervals'],12)
        self.assertEqual(w.s['econ3']['produced']['grain'],12)
        self.assertEqual(before,w.checksum())

    def test_97_partial_span_does_not_claim_prorated_quantity(self):
        c=Coverage();c.record(source_id='j',contributors=['w'],stream='grain',start=23,end=26,quantity=6,evidence_ref='j')
        v=c.view(0,24,'grain')
        self.assertEqual(v['quantity_from_complete_intervals'],0)
        self.assertEqual(v['unattributed_partial_sources'],['j'])
        self.assertFalse(v['complete'])

    def test_98_nonoverlapping_same_worker_can_continue(self):
        c=Coverage();c.record(source_id='a',contributors=['w'],stream='grain',start=0,end=4,quantity=4,evidence_ref='a')
        c.record(source_id='b',contributors=['w'],stream='grain',start=4,end=8,quantity=4,evidence_ref='b')
        self.assertEqual(c.view(0,8,'grain')['quantity_from_complete_intervals'],8)

    def test_99_conservative_empty_cohort_rejected(self):
        c=Coverage()
        with self.assertRaises(InvalidEvent):c.record(source_id='unknown',contributors=[],stream='grain',start=0,end=4,quantity=4,evidence_ref='untracked')

    def test_100_serialization_replay_same_code(self):
        import json
        w=r4();treasury_request(w,'r1',400,'army');treasury_request(w,'r2',400,'caregiver-1')
        w.run_until(2)
        u=R4World.load(w.save())
        self.assertEqual(u.checksum(),w.checksum())
        self.assertEqual(u.s['r4_deferred'],w.s['r4_deferred'])

    def test_101_permutation_independent_components_equivalent_resources(self):
        def go(names):
            w=r4()
            w.schedule(names[0],8,'start_job',job_id='farm',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
            w.schedule(names[1],8,'assess_tax',tax_id='A',payer='farmer-b',amount=4,authority_ref='law',basis_ref='lot')
            w.schedule(names[2],8,'transfer_cash',**{'from':'treasury','to':'army','amount':40})
            w.run_until(8)
            return (w.s['cash'],w.s['econ3']['active_jobs'],w.s['econ3']['tax_claims'])
        self.assertEqual(go(['z','a','m']),go(['a','z','m']))

    def test_102_unknown_operation_cannot_commit_independent_known_side_effects(self):
        w=r4();w.schedule('unknown',2,'not_registered')
        w.schedule('cash',2,'transfer_cash',**{'from':'treasury','to':'army','amount':10})
        r=w.run_until(2)
        self.assertEqual(r['committed'],[])
        self.assertEqual(w.s['cash']['army'],0)
        self.assertEqual(len(w.s['r4_deferred']),1)

    def test_103_submission_id_not_reused_after_deferral(self):
        w=r4();treasury_request(w,'r1',400,'army');treasury_request(w,'r2',400,'caregiver-1')
        w.run_until(2)
        with self.assertRaises(InvalidEvent):treasury_request(w,'r1',10,'army',3)

    def test_104_three_party_contention_blocks_only_shared_cash_component(self):
        w=r4()
        for eid,to in [('a','army'),('b','caregiver-1'),('c','person-B')]:
            treasury_request(w,eid,300,to)
        w.schedule('unrelated',2,'assess_tax',tax_id='new',payer='farmer-a',amount=8,authority_ref='law',basis_ref='lot')
        r=w.run_until(2)
        self.assertEqual(r['committed'],['unrelated'])
        self.assertEqual(len(w.s['r4_deferred'][r['deferred'][0]]['requests']),3)
        self.assertEqual(w.s['cash']['treasury'],600)

    def test_105_no_partial_application_of_invalid_decision(self):
        w=r4();treasury_request(w,'r1',400,'army');treasury_request(w,'r2',400,'caregiver-1')
        gid=w.run_until(2)['deferred'][0];prior=w.checksum()
        with self.assertRaises(InvalidEvent):w.decide_deferred(gid,['r1','r2'],at=3,authority_ref='gov')
        self.assertEqual(w.checksum(),prior)

    def test_106_independent_law_and_cash_no_cross_inference(self):
        w=r4();w.schedule('law',2,'legal_status_change',person='caregiver-1',to='free',jurisdiction='J',effective_at=2,authorized_decision_ref='council')
        w.schedule('money',2,'transfer_cash',**{'from':'treasury','to':'army','amount':20})
        r=w.run_until(2)
        self.assertEqual(set(r['committed']),{'law','money'})
        self.assertEqual(w.s['gov']['legal_status']['caregiver-1']['J']['status'],'free')

    def test_107_coverage_save_restore_and_monthly_projection(self):
        import json
        c=Coverage();c.record(source_id='a',contributors=['a'],stream='grain',start=0,end=4,quantity=4,evidence_ref='work-A')
        n=Coverage(json.loads(c.save()))
        self.assertEqual(n.checksum(),c.checksum())
        self.assertEqual(n.view(0,720,'grain')['quantity_from_complete_intervals'],4)

    def test_108_overlap_in_different_streams_is_not_automatically_same_stock(self):
        c=Coverage()
        c.record(source_id='grain-output',contributors=['a'],stream='grain',start=0,end=4,quantity=12,evidence_ref='job')
        c.record(source_id='seed-input',contributors=['a'],stream='seed-consumed',start=0,end=4,quantity=4,evidence_ref='job')
        self.assertEqual(c.view(0,4,'grain')['quantity_from_complete_intervals'],12)
        self.assertEqual(c.view(0,4,'seed-consumed')['quantity_from_complete_intervals'],4)

if __name__=='__main__':unittest.main()
