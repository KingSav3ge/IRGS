"""Round 6 bounded work interruption, accounting, resumption and independent institutions.

Tests 139-164 are examples, not assertions of real production rates or labor law.
"""
import unittest
from irgs_reference import InvalidEvent
from test_economic_integration import fresh
from r6_work import R6World
from economic_extension import total


def world():
    s=fresh().s
    # Synthetic outside replacement source. This is pre-existing physical stock,
    # not created when recovery is needed.
    s['econ3']['stocks']['warehouse']={'seed':4}
    s['econ3']['opening']['seed']+=4
    s['r6_model_bindings']={'grow':'synthetic-grow-1h','cook':'synthetic-cook-1h'}
    return R6World(initial=s)

def start(w):
    w.apply('start-farm',8,'start_tracked_job',job_id='farm',recipe_id='grow',start=8,end=12,
            workers=['farmer-a'],selected_model_ref='synthetic-grow-1h')

def step(w,eid='milestone1',a=8,b=9,job='farm',recipe='grow'):
    w.apply(eid,b,'record_work_milestone',job_id=job,from_at=a,to_at=b,
            selected_model_ref='synthetic-'+recipe+'-1h',work_evidence_ref='fixture-work-'+eid,
            output_acceptance_ref='fixture-accepted-'+eid)

def fire(w):
    w.schedule('loss',10,'physical_loss',location='farm',material='seed',quantity=9,
               cause_ref='synthetic-fire',evidence_ref='synthetic-inventory')
    return w.run_until(10)

def settle(w):
    w.apply('settle',11,'settle_disrupted_job',job_id='farm',wage_rate=2,
            wage_agreement_ref='synthetic-rate',competent_authority_ref='fixture-supervisor',
            assessment_ref='fixture-assessment')

def recover(w):
    # Distinct occurrence frontiers: replacement travels, is received, work is
    # newly assigned, then continuation obtains a fresh reservation.
    w.apply('dispatch',12,'dispatch_stock',shipment_id='replacement',quantity=3,
            material='seed',**{'from':'warehouse','to':'farm'},route_ref='fixture-road',minimum_transit=1)
    w.apply('arrival',13,'receive_stock',shipment_id='replacement')
    w.apply('shift-2',13,'commit_shift',person='farmer-a',start=14,end=17,role='work:grow')
    w.apply('continue',14,'start_continuation',parent_job_id='farm',job_id='farm-part2',recipe_id='grow',
            start=14,end=17,workers=['farmer-a'],selected_model_ref='synthetic-grow-1h',
            authorization_ref='authorized-new-work')
    for i in range(3): step(w,f'cont-{i}',14+i,15+i,job='farm-part2')
    w.apply('finish-2',18,'finalize_tracked_job',job_id='farm-part2',wage_rate=2,
            wage_agreement_ref='synthetic-rate',competent_authority_ref='fixture-supervisor',
            acceptance_ref='fixture-finished-work')

class WorkRecoveryTests(unittest.TestCase):
    def test_139_milestone_uses_actual_inputs_and_output(self):
        w=world();start(w);step(w)
        e=w.s['econ3'];self.assertEqual(e['consumed']['seed'],1)
        self.assertEqual(e['produced']['grain'],3)
        self.assertEqual(e['active_jobs']['farm']['reserved_inputs'],{'seed':3})
    def test_140_milestone_cannot_recur_under_new_id(self):
        w=world();start(w);step(w);old=w.checksum()
        with self.assertRaises(InvalidEvent):step(w,'duplicate-attempt')
        self.assertEqual(w.checksum(),old)
    def test_141_original_event_retry_is_idempotent(self):
        w=world();start(w);step(w);old=w.checksum()
        step(w)
        self.assertEqual(w.checksum(),old)
    def test_142_future_milestone_not_conjured(self):
        w=world();start(w);old=w.checksum()
        # Elapsed clock alone does not attest work or accepted output.
        with self.assertRaises(InvalidEvent):
            w.apply('unsupported',12,'record_work_milestone',job_id='farm',from_at=8,to_at=12,
              selected_model_ref='synthetic-grow-1h',work_evidence_ref='',output_acceptance_ref='')
        self.assertEqual(w.checksum(),old)
    def test_143_unsupported_model_is_rejected(self):
        w=world();old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('bad',8,'start_tracked_job',job_id='farm',recipe_id='grow',start=8,end=12,
                    workers=['farmer-a'],selected_model_ref='unselected')
        self.assertEqual(w.checksum(),old)
    def test_144_loss_does_not_erase_accepted_output(self):
        w=world();start(w);step(w);fire(w)
        self.assertEqual(w.s['econ3']['stocks']['farm']['grain'],3)
        self.assertEqual(w.s['econ3']['losses']['seed'],9)
        self.assertEqual(w.s['econ3']['consumed']['seed'],1)
        self.assertEqual(w.s['econ3']['active_jobs']['farm']['status'],'suspended_unallocated')
    def test_145_original_work_is_not_completed_from_clock(self):
        w=world();start(w);step(w);fire(w);w.apply('review',12,'review_no_change')
        self.assertEqual(w.s['econ3']['produced']['grain'],3)
        self.assertIn('farm',w.s['econ3']['active_jobs'])
    def test_146_legacy_completion_for_tracked_job_forbidden(self):
        w=world();start(w);step(w);fire(w)
        old=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('old-finish',12,'complete_job',job_id='farm')
        self.assertEqual(w.checksum(),old)
    def test_147_unsupported_scheduler_work_events_blocked(self):
        w=world();old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.schedule('planned',8,'start_tracked_job',job_id='farm',recipe_id='grow',start=8,end=12,
                       workers=['farmer-a'],selected_model_ref='synthetic-grow-1h')
        self.assertEqual(w.checksum(),old)
    def test_148_disruption_settlement_only_certified_hours(self):
        w=world();start(w);step(w);fire(w);settle(w)
        self.assertEqual(w.s['wage_due']['farmer-a'],2)
        self.assertEqual(w.s['r6_settlements']['farm']['hours_verified'],1)
        self.assertEqual(w.s['r6_settlements']['farm']['hours_remaining'],3)
    def test_149_unassessed_work_is_not_auto_cancelled(self):
        w=world();start(w);step(w);fire(w);settle(w)
        self.assertEqual(w.s['r6_settlements']['farm']['unassessed_elapsed_interval'],[9,10])
        self.assertEqual(w.s['r6_settlements']['farm']['wage_claim_for_unassessed_time'],'unresolved')
    def test_150_settlement_does_not_consume_more_seed(self):
        w=world();start(w);step(w);fire(w);settle(w)
        self.assertEqual(w.s['econ3']['consumed']['seed'],1)
        self.assertEqual(w.s['econ3']['active_jobs'],{})
        self.assertEqual(w.s['r5_shortfalls']['farm']['status'],'settled_with_unfulfilled_claim')
    def test_151_no_duplicate_settlement(self):
        w=world();start(w);step(w);fire(w);settle(w)
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('another-settle',12,'settle_disrupted_job',job_id='farm',wage_rate=2,
                wage_agreement_ref='synthetic-rate',competent_authority_ref='fixture',assessment_ref='fixture')
        self.assertEqual(w.checksum(),old)
    def test_152_cannot_resume_before_supply_arrives(self):
        w=world();start(w);step(w);fire(w);settle(w)
        w.apply('shift-early',11,'commit_shift',person='farmer-a',start=12,end=15,role='work:grow')
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('too-soon',12,'start_continuation',parent_job_id='farm',job_id='fake',recipe_id='grow',
                start=12,end=15,workers=['farmer-a'],selected_model_ref='synthetic-grow-1h',authorization_ref='fixture')
        self.assertEqual(w.checksum(),old)
    def test_153_replacement_is_real_transit_stock(self):
        w=world();start(w);step(w);fire(w);settle(w)
        w.apply('dispatch',12,'dispatch_stock',shipment_id='R',quantity=3,material='seed',
            **{'from':'warehouse','to':'farm'},route_ref='fixture',minimum_transit=1)
        self.assertEqual(w.s['econ3']['stocks']['warehouse']['seed'],1)
        self.assertEqual(w.s['econ3']['stocks']['transit:R']['seed'],3)
        self.assertEqual(w.s['econ3']['stocks']['farm']['seed'],2)
    def test_154_supply_arrival_not_work_approval(self):
        w=world();start(w);step(w);fire(w);settle(w)
        w.apply('dispatch',12,'dispatch_stock',shipment_id='R',quantity=3,material='seed',
            **{'from':'warehouse','to':'farm'},route_ref='fixture',minimum_transit=1)
        w.apply('arrival',13,'receive_stock',shipment_id='R')
        self.assertNotIn('farm-part2',w.s['econ3']['active_jobs'])
        self.assertEqual(w.s['econ3']['produced']['grain'],3)
    def test_155_recovery_total_outputs_and_inputs(self):
        w=world();start(w);step(w);fire(w);settle(w);recover(w)
        self.assertEqual(w.s['econ3']['produced']['grain'],12)
        self.assertEqual(w.s['econ3']['consumed']['seed'],4)
        self.assertEqual(w.s['econ3']['losses']['seed'],9)
        self.assertEqual(total(w.s['econ3'],'seed'),3)
    def test_156_wage_liability_accrued_once_across_jobs(self):
        w=world();start(w);step(w);fire(w);settle(w);recover(w)
        self.assertEqual(w.s['wage_due']['farmer-a'],8)
        self.assertEqual(len(w.s['r6_settlements']),2)
    def test_157_continuation_cannot_duplicate_remaining_work(self):
        w=world();start(w);step(w);fire(w);settle(w);recover(w)
        w.apply('another-shift',19,'commit_shift',person='farmer-a',start=20,end=23,role='work:grow')
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('cont-again',20,'start_continuation',parent_job_id='farm',job_id='extra',recipe_id='grow',
              start=20,end=23,workers=['farmer-a'],selected_model_ref='synthetic-grow-1h',authorization_ref='fixture')
        self.assertEqual(w.checksum(),old)
    def test_158_save_load_after_partial_loss(self):
        w=world();start(w);step(w);fire(w);settle(w)
        w2=R6World.load(w.save())
        self.assertEqual(w.checksum(),w2.checksum())
        self.assertEqual(w2.s['r6_progress']['farm']['hours_verified'],1)
    def test_159_save_load_after_recovery(self):
        w=world();start(w);step(w);fire(w);settle(w);recover(w)
        self.assertEqual(w.checksum(),R6World.load(w.save()).checksum())
    def test_160_unauthorized_resume_rejected(self):
        w=world();start(w);step(w);fire(w);settle(w)
        w.apply('dispatch',12,'dispatch_stock',shipment_id='R',quantity=3,material='seed',
            **{'from':'warehouse','to':'farm'},route_ref='fixture',minimum_transit=1)
        w.apply('arrival',13,'receive_stock',shipment_id='R')
        w.apply('shift',13,'commit_shift',person='farmer-a',start=14,end=17,role='work:grow')
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('unapproved',14,'start_continuation',parent_job_id='farm',job_id='extra',recipe_id='grow',
              start=14,end=17,workers=['farmer-a'],selected_model_ref='synthetic-grow-1h',authorization_ref='')
        self.assertEqual(w.checksum(),old)
    def test_161_untouched_kitchen_continues(self):
        w=world();start(w)
        w.apply('start-cook',8,'start_job',job_id='cook',recipe_id='cook',start=8,end=12,workers=['person-B'])
        step(w);fire(w);settle(w)
        w.apply('finish-cook',12,'complete_job',job_id='cook')
        self.assertEqual(w.s['econ3']['produced']['meal'],12)
        self.assertEqual(w.s['econ3']['produced']['grain'],3)
    def test_162_tax_does_not_create_money(self):
        w=world();start(w);step(w)
        w.schedule('tax',10,'assess_tax',tax_id='T',payer='farmer-b',amount=3,
           authority_ref='synthetic-law',basis_ref='synthetic-lot')
        fire(w)
        self.assertEqual(w.s['econ3']['tax_claims']['T']['paid'],0)
        self.assertEqual(sum(w.s['cash'].values()),1000)
    def test_163_wealth_population_kits_unchanged_by_loss(self):
        w=world();start(w);step(w);fire(w);settle(w);recover(w)
        self.assertEqual(w.display_population()['total'],1200)
        self.assertEqual(sum(w.s['cash'].values()),1000)
        self.assertEqual(sum(d.get('kit',0) for d in w.s['equipment'].values()),300)
    def test_164_full_output_cannot_be_settled_early(self):
        w=world();start(w);step(w)
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('too-early',10,'finalize_tracked_job',job_id='farm',wage_rate=2,
                wage_agreement_ref='agreement',competent_authority_ref='supervisor',acceptance_ref='inspection')
        self.assertEqual(old,w.checksum())

    def test_165_fulfilled_claim_keeps_loss_history(self):
        w=world();start(w);step(w);fire(w);settle(w);recover(w)
        short=w.s['r5_shortfalls']['farm']
        self.assertEqual(short['status'],'fulfilled_by_continuation')
        self.assertEqual(short['original_reserved_inputs'],{'seed':3})
        self.assertEqual(short['fulfilling_job_id'],'farm-part2')
        self.assertEqual(w.s['econ3']['losses']['seed'],9)

if __name__=='__main__':unittest.main()
