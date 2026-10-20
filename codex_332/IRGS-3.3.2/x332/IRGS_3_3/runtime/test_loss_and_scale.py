"""R5 synthetic tests 109-135; no calibration or independent implementation."""
import unittest
from irgs_reference import InvalidEvent,World
from r5_hazards import R5World
from r5_scale import MilitaryProjection
from economic_extension import total, free
from test_economic_integration import fresh


def world():return R5World(initial=fresh().s)
def burn(w, *, at=9, quantity=9, loc='farm', mat='seed', id='loss'):
    w.schedule(id,at,'physical_loss',location=loc,material=mat,quantity=quantity,
               cause_ref='test-confirmed-fire',evidence_ref='test-observation')
def farm(w,jid='farm',worker='farmer-a'):
    w.apply('start:'+jid,8,'start_job',job_id=jid,recipe_id='grow',start=8,end=12,workers=[worker])

def military():
    w=world()
    w.s['actors']['caregiver-1']['ammo']=3
    w.s['actors']['person-B']['ammo']=2
    return R5World(state=w.s)

class LossAndScaleTests(unittest.TestCase):
    def test_109_involuntary_loss_over_reservation_commits(self):
        w=world();farm(w);burn(w);r=w.run_until(9)
        self.assertEqual(r['physical_losses'],['loss'])
        self.assertEqual(w.s['econ3']['stocks']['farm']['seed'],3)
        self.assertEqual(w.s['econ3']['losses']['seed'],9)
        self.assertEqual(w.s['econ3']['consumed']['seed'],0)
        self.assertEqual(w.s['econ3']['active_jobs']['farm']['status'],'suspended_unallocated')
    def test_110_shortfall_retains_original_claim(self):
        w=world();farm(w);burn(w);w.run_until(9)
        self.assertEqual(w.s['r5_shortfalls']['farm']['original_reserved_inputs'],{'seed':4})
        self.assertEqual(w.s['econ3']['active_jobs']['farm']['reserved_inputs'],{'seed':0})
        self.assertEqual(w.s['r5_pool_shortfalls'][0]['shortfall_at_hazard'],1)
    def test_111_no_production_from_suspended_job(self):
        w=world();farm(w);burn(w);w.run_until(9)
        w.schedule('finish',12,'complete_job',job_id='farm')
        out=w.run_until(12)
        self.assertFalse('finish' in out['committed'])
        self.assertEqual(w.s['econ3']['produced']['grain'],0)
        self.assertEqual(len(out['deferred']),1)
    def test_112_unrelated_tax_still_runs(self):
        w=world();farm(w);burn(w)
        w.schedule('tax',9,'assess_tax',tax_id='A',payer='farmer-b',amount=6,
                   authority_ref='tax-law',basis_ref='lot')
        out=w.run_until(9)
        self.assertIn('tax',out['committed'])
        self.assertEqual(w.s['econ3']['tax_claims']['A']['paid'],0)
    def test_113_independent_cooking_continues(self):
        w=world();farm(w)
        w.apply('kitchen-start',8,'start_job',job_id='cook',recipe_id='cook',start=8,end=12,workers=['person-B'])
        burn(w);w.run_until(9)
        w.schedule('kitchen-finish',12,'complete_job',job_id='cook')
        out=w.run_until(12)
        self.assertIn('kitchen-finish',out['committed'])
        self.assertEqual(w.s['econ3']['produced']['meal'],12)
        self.assertEqual(w.s['econ3']['produced']['grain'],0)
    def test_114_loss_identity_with_quantity_and_no_double_consumption(self):
        w=world();burn(w,quantity=2);w.run_until(9)
        self.assertEqual(total(w.s['econ3'],'seed'),10)
        self.assertEqual(w.s['econ3']['losses']['seed'],2)
        self.assertEqual(w.s['econ3']['consumed']['seed'],0)
    def test_115_loss_already_applied_cannot_reapply(self):
        w=world();burn(w,quantity=2);w.run_until(9)
        before=w.checksum()
        self.assertFalse(w.apply('loss',9,'physical_loss',location='farm',material='seed',quantity=2,cause_ref='test-confirmed-fire',evidence_ref='test-observation'))
        with self.assertRaises(InvalidEvent):burn(w,at=10,quantity=2,id='loss')
        self.assertEqual(w.checksum(),before)
    def test_116_disputed_same_frontier_shipment_not_backdated(self):
        w=world();burn(w,at=8,quantity=9)
        w.schedule('load',8,'dispatch_stock',shipment_id='S',quantity=4,material='seed',**{'from':'farm','to':'house-1'},route_ref='road',minimum_transit=1)
        out=w.run_until(8)
        self.assertEqual(out['physical_losses'],['loss'])
        self.assertEqual(w.s['econ3']['stocks']['farm']['seed'],3)
        self.assertNotIn('S',w.s['econ3']['shipments'])
        self.assertEqual(w.s['r4_deferred'][out['deferred'][0]]['status'],'causal_order_undetermined')
    def test_117_independent_same_frontier_cash_commits(self):
        w=world();burn(w,at=8)
        w.schedule('money',8,'transfer_cash',**{'from':'treasury','to':'army','amount':20})
        out=w.run_until(8)
        self.assertEqual(set(out['committed']),{'loss','money'})
        self.assertEqual(w.s['cash']['army'],20)
    def test_118_overobserved_loss_rejects_atomically(self):
        w=world();burn(w,quantity=13);prior=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(9)
        self.assertEqual(prior,w.checksum())
    def test_119_two_losses_more_than_supported_total_rejected(self):
        w=world();burn(w,quantity=7,id='a');burn(w,quantity=7,id='b')
        prior=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(9)
        self.assertEqual(w.checksum(),prior)
    def test_120_two_supported_losses_sum_without_extra(self):
        w=world();burn(w,quantity=5,id='a');burn(w,quantity=4,id='b');out=w.run_until(9)
        self.assertEqual(set(out['physical_losses']),{'a','b'})
        self.assertEqual(w.s['econ3']['losses']['seed'],9)
        self.assertEqual(total(w.s['econ3'],'seed'),3)
    def test_121_transport_specialist_needed(self):
        w=world()
        w.apply('departure',8,'dispatch_stock',shipment_id='abc',quantity=2,material='seed',**{'from':'farm','to':'house-1'},route_ref='route',minimum_transit=2)
        burn(w,loc='transit:abc',quantity=1)
        # A real stocked transit location is still rejected until shipment records can be updated.
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(9)
        self.assertEqual(w.checksum(),before)
    def test_122_same_implementation_save_load(self):
        w=world();farm(w);burn(w);w.run_until(9)
        loaded=R5World.load(w.save())
        self.assertEqual(w.checksum(),loaded.checksum())
        self.assertEqual(w.s['r5_shortfalls'],loaded.s['r5_shortfalls'])
    def test_123_hazard_without_backing_shortfall_keeps_job_live(self):
        w=world();farm(w);burn(w,quantity=6)
        w.run_until(9)
        self.assertNotIn('status',w.s['econ3']['active_jobs']['farm'])
        w.schedule('finish',12,'complete_job',job_id='farm')
        self.assertIn('finish',w.run_until(12)['committed'])
        self.assertEqual(w.s['econ3']['stocks']['farm']['seed'],2)
        self.assertEqual(w.s['econ3']['produced']['grain'],12)
    def test_124_claims_for_two_jobs_no_id_priority(self):
        w=world();farm(w,'job-z','farmer-a');farm(w,'job-a','farmer-b')
        burn(w,quantity=6);w.run_until(9)
        self.assertEqual(set(w.s['r5_shortfalls']),{'job-z','job-a'})
        self.assertTrue(all(j['status']=='suspended_unallocated' for j in w.s['econ3']['active_jobs'].values()))
    def test_125_original_population_cash_equipment_conserved(self):
        w=world();farm(w);burn(w);w.run_until(9)
        self.assertEqual(w.display_population()['total'],1200)
        self.assertEqual(sum(w.s['cash'].values()),1000)
        self.assertEqual(sum(q.get('kit',0) for q in w.s['equipment'].values()),300)
    def test_126_hazard_on_unreserved_other_material_keeps_job(self):
        w=world();farm(w);burn(w,loc='house-1',mat='fuel',quantity=2);w.run_until(9)
        self.assertNotIn('farm',w.s.get('r5_shortfalls',{}))
        self.assertEqual(w.s['econ3']['active_jobs']['farm']['reserved_inputs'],{'seed':4})
    def test_127_engagement_view_no_double_casualties(self):
        w=military();w.apply('battle',5,'simultaneous_exchange',engagement_id='E',selected_effect_adapter='fixture_effects_only',attacks=[
            {'from':'caregiver-1','to':'person-B','ammo_used':2,'effect':'disable'},
            {'from':'person-B','to':'caregiver-1','ammo_used':1,'effect':'none'}])
        w.apply('summary',6,'summarize_engagement',engagement_id='E')
        old=w.checksum();v=MilitaryProjection(w).view(actors=['caregiver-1','person-B'],from_time=0,through=6)
        self.assertEqual(v['actor_disablement_count_now'],1)
        self.assertEqual(v['ammunition_spent_from_sources'],{'caregiver-1':2,'person-B':1})
        self.assertEqual(v['effect_source_ids'],['battle'])
        self.assertEqual(v['information_summary_ids'],['summary'])
        self.assertEqual(w.checksum(),old)
    def test_128_local_and_regional_views_read_same_effect(self):
        w=military();w.apply('E',5,'simultaneous_exchange',engagement_id='eng',selected_effect_adapter='fixture_effects_only',attacks=[
            {'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'}])
        m=MilitaryProjection(w)
        local=m.view(actors=['person-B'],through=5)
        allp=m.view(actors=['caregiver-1','person-B'],through=5)
        self.assertEqual(local['actor_disablement_count_now'],1)
        self.assertEqual(allp['actor_disablement_count_now'],1)
        self.assertEqual(w.s['actors']['caregiver-1']['ammo'],2)
    def test_129_reporting_not_physical_casualty(self):
        w=military();w.apply('E',5,'simultaneous_exchange',engagement_id='eng',selected_effect_adapter='fixture_effects_only',attacks=[
            {'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'}])
        w.apply('reporting',6,'report',person='caregiver-1',recipient='command',message='one disabled opponent')
        v=MilitaryProjection(w).view(actors=['caregiver-1','person-B'],through=6)
        self.assertEqual(v['actor_disablement_count_now'],1)
        self.assertEqual(v['report_ids'],['reporting'])
        self.assertEqual(w.s['actors']['person-B']['disabled'],True)
    def test_130_no_residual_named_person_overlap(self):
        w=military();m=MilitaryProjection(w)
        self.assertEqual(m.residual_population_view(excluded_named_actors=['person-B'])['unnamed_residual_people'],1194)
        with self.assertRaises(InvalidEvent):m.residual_population_view(excluded_named_actors=['person-B','person-B'])
    def test_131_missing_actor_disallowed(self):
        w=military()
        with self.assertRaises(InvalidEvent):MilitaryProjection(w).view(actors=['unknown'],through=0)
    def test_132_missing_historical_checkpoint_disallowed(self):
        w=military();w.apply('t1',4,'review_no_change')
        with self.assertRaises(InvalidEvent):MilitaryProjection(w).view(actors=['caregiver-1'],through=3)
    def test_133_same_provenance_in_day_and_month(self):
        w=military();w.apply('E',5,'simultaneous_exchange',engagement_id='eng',selected_effect_adapter='fixture_effects_only',attacks=[
            {'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'}])
        m=MilitaryProjection(w)
        day=m.view(actors=['caregiver-1','person-B'],through=5,from_time=0)
        month=m.view(actors=['caregiver-1','person-B'],through=5,from_time=0)
        self.assertEqual(day,month)
        self.assertEqual(day['effect_source_ids'],['E'])
    def test_134_multiple_report_ids_still_one_effect(self):
        w=military();w.apply('E',5,'simultaneous_exchange',engagement_id='eng',selected_effect_adapter='fixture_effects_only',attacks=[
            {'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'}])
        w.apply('r1',6,'report',person='caregiver-1',recipient='command',message='casualty')
        w.apply('r2',7,'report',person='caregiver-1',recipient='headquarters',message='same casualty')
        v=MilitaryProjection(w).view(actors=['caregiver-1','person-B'],through=7)
        self.assertEqual(v['actor_disablement_count_now'],1)
        self.assertEqual(v['report_ids'],['r1','r2'])
    def test_135_save_replay_views_identical(self):
        w=military();w.apply('E',5,'simultaneous_exchange',engagement_id='eng',selected_effect_adapter='fixture_effects_only',attacks=[
            {'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'}])
        loaded=R5World.load(w.save());actors=['caregiver-1','person-B']
        self.assertEqual(MilitaryProjection(w).view(actors=actors,through=5),MilitaryProjection(loaded).view(actors=actors,through=5))
        self.assertEqual(w.checksum(),loaded.checksum())

from r5_audit import independent_audit

class Round5IndependentAuditTests(unittest.TestCase):
    def test_136_audit_loss_journal_and_material_identity(self):
        w=world();farm(w);burn(w);w.run_until(9)
        a=independent_audit(w.s)
        self.assertEqual(a['losses_by_journal'],{'seed':9})
        self.assertEqual(a['original_claim_count'],1)
    def test_137_audit_detects_tampered_loss_ledger(self):
        w=world();burn(w,quantity=3);w.run_until(9)
        w.s['econ3']['losses']['seed']=2
        with self.assertRaises(ValueError):independent_audit(w.s)
    def test_138_audit_ammunition(self):
        w=military();w.apply('E',5,'simultaneous_exchange',engagement_id='eng',selected_effect_adapter='fixture_effects_only',attacks=[
            {'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'}])
        self.assertEqual(independent_audit(w.s,initial_ammo={'caregiver-1':3,'person-B':2})['ammunition_spent_by_source'],{'caregiver-1':1})
