"""R3 bounded test cases. These demonstrate invariants, not realistic economic rates."""
import copy, unittest
from irgs_reference import World, InvalidEvent, initial_world
from economic_extension import economy_fixture, free, total


def fresh():
    return World(initial=economy_fixture(initial_world().s))


def begin(w,include_farmer_b=True,include_kitchen=True):
    farmers=['farmer-a']+(['farmer-b'] if include_farmer_b else [])
    w.apply('j-farm',8,'start_job',job_id='farm-day',recipe_id='grow',start=8,end=12,workers=farmers)
    if include_kitchen:
        w.apply('j-kitchen',8,'start_job',job_id='cook-day',recipe_id='cook',start=8,end=12,workers=['person-B'])


def finish(w,include_kitchen=True,carer='caregiver-1'):
    w.apply('c-farm',12,'complete_job',job_id='farm-day')
    if include_kitchen:w.apply('c-kitchen',12,'complete_job',job_id='cook-day')
    if carer:w.apply('c-care',12,'complete_care',person=carer,household='house-1',start=8,end=12)


def run_day(mode='civilian'):
    w=fresh()
    if mode in ('farmer_mobilized','dual_mobilized'):
        w.apply('mandate',1,'authorize_mobilization',mandate='fixture-decision',target=2)
        w.apply('rel-farmer',3,'release_shift',person='farmer-b',start=8,end=12,role='work:grow',authority_ref='work-release-1')
        w.apply('en-farmer',4,'enroll',person='farmer-b')
        w.apply('m-shift-farmer',5,'commit_shift',person='farmer-b',start=8,end=12,role='military_duty')
    if mode in ('caregiver_mobilized','dual_mobilized','uncovered'):
        if mode!='dual_mobilized':w.apply('mandate',1,'authorize_mobilization',mandate='fixture-decision',target=2)
        w.apply('rel-care',6,'release_shift',person='caregiver-1',start=8,end=12,role='household_care',authority_ref='care-release-1')
        w.apply('en-carer',6,'enroll',person='caregiver-1')
        w.apply('m-shift-carer',6,'commit_shift',person='caregiver-1',start=8,end=12,role='military_duty')
        if mode != 'uncovered':
            w.apply('rel-kitchen',7,'release_shift',person='person-B',start=8,end=12,role='work:cook',authority_ref='care-substitution-decision')
            w.apply('substitute-care',7,'commit_shift',person='person-B',start=8,end=12,role='household_care')
    begin(w,include_farmer_b=(mode not in ('farmer_mobilized','dual_mobilized')),
          include_kitchen=(mode not in ('caregiver_mobilized','dual_mobilized')))
    finish(w,include_kitchen=(mode not in ('caregiver_mobilized','dual_mobilized')),
           carer= ('person-B' if mode in ('caregiver_mobilized','dual_mobilized') else None if mode=='uncovered' else 'caregiver-1'))
    if mode not in ('caregiver_mobilized','dual_mobilized'):
        w.apply('serve',13,'provision_meals',household='house-1',quantity=6)
    w.apply('assess',17,'audit_needs',audit_id='day1',household='house-1')
    return w


class EconomicIntegrationTests(unittest.TestCase):
    def test_37_baseline_actual_work_changes_stocks(self):
        w=run_day()
        e=w.s['econ3']
        self.assertEqual(total(e,'grain'),24)
        self.assertEqual(total(e,'seed'),4)
        self.assertEqual(total(e,'meal'),6)
        self.assertEqual(e['consumed']['grain'],8)
        self.assertEqual(e['produced']['grain'],24)
        self.assertEqual(e['produced']['meal'],12)

    def test_38_mobilization_releases_civilian_work_not_population(self):
        base=run_day();war=run_day('farmer_mobilized')
        self.assertEqual(base.display_population()['total'],1200)
        self.assertEqual(war.display_population()['total'],1200)
        self.assertEqual(len(war.s['formations']['army']['members']),1)
        self.assertEqual(base.s['econ3']['produced']['grain'],24)
        self.assertEqual(war.s['econ3']['produced']['grain'],12)
        self.assertEqual(war.s['econ3']['stocks']['farm']['seed'],8)
        self.assertEqual(war.s['econ3']['needs_audit'][0]['unmet_meals'],0)

    def test_39_conscription_alone_does_not_erase_civilian_shift(self):
        w=fresh();w.apply('mandate',1,'authorize_mobilization',mandate='M',target=3)
        w.apply('enroll',2,'enroll',person='farmer-b')
        self.assertIn([8,12,'work:grow'],w.s['commitments']['farmer-b'])
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('army-shift',3,'commit_shift',person='farmer-b',start=8,end=12,role='military_duty')
        self.assertEqual(old,w.checksum())

    def test_40_release_requires_authorization_before_commencement(self):
        w=fresh();old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('rel',1,'release_shift',person='farmer-b',start=8,end=12,role='work:grow',authority_ref='')
        self.assertEqual(old,w.checksum())
        w.apply('advance',9,'review_no_change')
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('late',9,'release_shift',person='farmer-b',start=8,end=12,role='work:grow',authority_ref='D')
        self.assertEqual(old,w.checksum())

    def test_41_caregiver_mobilization_substitute_diminishes_cooking(self):
        w=run_day('caregiver_mobilized');audit=w.s['econ3']['needs_audit'][0]
        self.assertEqual(audit['unmet_care_hours'],0)
        self.assertEqual(audit['unmet_meals'],6)
        self.assertEqual(w.s['econ3']['produced']['meal'],0)
        self.assertIn('caregiver-1',w.s['formations']['army']['members'])

    def test_42_no_substitute_produces_care_gap_without_catastrophe(self):
        w=run_day('uncovered');audit=w.s['econ3']['needs_audit'][0]
        self.assertEqual(audit['unmet_care_hours'],4)
        self.assertEqual(audit['unmet_meals'],0)
        self.assertFalse(w.s['actors']['child-1']['disabled'])

    def test_43_dual_mobilization_combines_distinct_shortfalls_once(self):
        w=run_day('dual_mobilized');audit=w.s['econ3']['needs_audit'][0]
        self.assertEqual(w.s['econ3']['produced']['grain'],12)
        self.assertEqual(w.s['econ3']['produced']['meal'],0)
        self.assertEqual(audit['unmet_care_hours'],0)
        self.assertEqual(audit['unmet_meals'],6)
        self.assertEqual(len(w.s['formations']['army']['members']),2)

    def test_44_shift_no_success_without_inputs_reserved_at_start(self):
        w=fresh();e=w.s['econ3'];e['stocks']['farm']['seed']=0;e['consumed']['seed']=12
        w=World(initial=w.s);old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('invalid',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        self.assertEqual(old,w.checksum())

    def test_45_nonqualified_person_cannot_work_by_rolling(self):
        w=fresh();w.s['commitments']['child-1']=[[8,12,'work:grow']]
        w.s['actors']['child-1']['location']='farm'
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('invalid',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['child-1'])
        self.assertEqual(old,w.checksum())

    def test_46_site_maximum_and_worker_time_matter(self):
        w=fresh();w.s['econ3']['sites']['farm']['workers_capacity']=1
        before=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('over',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a','farmer-b'])
        self.assertEqual(before,w.checksum())

    def test_47_reservation_neither_consumes_nor_adds_stock(self):
        w=fresh();w.apply('begin',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        e=w.s['econ3']
        self.assertEqual(physical_stock(e,'farm','seed'),12)
        self.assertEqual(e['consumed']['seed'],0)
        self.assertEqual(free(e,'farm','seed'),8)
        self.assertEqual(e['produced']['grain'],0)

    def test_48_transfer_cannot_use_reserved_seed(self):
        w=fresh();w.apply('begin',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        before=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('move',9,'dispatch_stock',shipment_id='S1',**{'from':'farm','to':'house-1'},material='seed',quantity=9,route_ref='short-haul',minimum_transit=2)
        self.assertEqual(before,w.checksum())
        w.apply('move-small',9,'dispatch_stock',shipment_id='S1',**{'from':'farm','to':'house-1'},material='seed',quantity=8,route_ref='short-haul',minimum_transit=2)
        self.assertEqual(w.s['econ3']['stocks']['farm']['seed'],4)
        self.assertEqual(w.s['econ3']['stocks']['transit:S1']['seed'],8)
        w.apply('finish',12,'complete_job',job_id='j')
        self.assertEqual(w.s['econ3']['stocks']['farm']['seed'],0)

    def test_49_transport_is_physical_in_transit(self):
        w=fresh();w.apply('ship',1,'dispatch_stock',shipment_id='X',**{'from':'house-1','to':'farm'},material='grain',quantity=3,route_ref='route-A',minimum_transit=3)
        self.assertEqual(w.s['econ3']['stocks']['house-1']['grain'],5)
        self.assertEqual(w.s['econ3']['stocks']['transit:X']['grain'],3)
        self.assertEqual(w.s['econ3']['stocks']['farm']['grain'],0)
        with self.assertRaises(InvalidEvent):w.apply('early',3,'receive_stock',shipment_id='X')
        w.apply('receipt',4,'receive_stock',shipment_id='X')
        self.assertEqual(w.s['econ3']['stocks']['farm']['grain'],3)
        self.assertEqual(total(w.s['econ3'],'grain'),8)

    def test_50_ongoing_work_interrupt_settles_only_elapsed_hours(self):
        w=fresh();w.apply('begin',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.apply('interrupt',10,'interrupt_job',job_id='j')
        e=w.s['econ3']
        self.assertEqual(e['completed_jobs']['j']['hours_done'],2)
        self.assertTrue(e['completed_jobs']['j']['interrupted'])
        self.assertEqual(e['stocks']['farm']['seed'],10)
        self.assertEqual(e['stocks']['farm']['grain'],6)
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('repeat',12,'complete_job',job_id='j')
        self.assertEqual(before,w.checksum())

    def test_51_no_labor_credit_before_completion_or_interruption(self):
        w=fresh();w.apply('start',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        self.assertEqual(w.s['econ3']['produced']['grain'],0)
        self.assertEqual(w.s['econ3']['completed_jobs'],{})

    def test_52_payroll_requires_completed_work_and_one_accrual(self):
        w=fresh();w.apply('start',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        with self.assertRaises(InvalidEvent):w.apply('early-pay',9,'accrue_job_wages',job_id='j',rate=2,wage_agreement_ref='C1')
        w.apply('finish',12,'complete_job',job_id='j')
        w.apply('wage',13,'accrue_job_wages',job_id='j',rate=2,wage_agreement_ref='C1')
        self.assertEqual(w.s['wage_due']['farmer-a'],8)
        with self.assertRaises(InvalidEvent):w.apply('double',14,'accrue_job_wages',job_id='j',rate=2,wage_agreement_ref='C1')
        self.assertEqual(w.s['cash']['farmer-a'],100)

    def test_53_tax_assessment_not_revenue(self):
        w=fresh();w.apply('assess',1,'assess_tax',tax_id='T1',payer='farmer-a',amount=70,authority_ref='tax-rule-profile',basis_ref='taxable-activity')
        self.assertEqual(w.s['cash']['treasury'],600)
        self.assertEqual(w.s['econ3']['tax_claims']['T1']['paid'],0)
        w.apply('payment',2,'pay_tax',tax_id='T1',amount=40)
        self.assertEqual(w.s['cash']['farmer-a'],60)
        self.assertEqual(w.s['cash']['treasury'],640)
        self.assertEqual(w.s['econ3']['tax_claims']['T1']['assessed']-w.s['econ3']['tax_claims']['T1']['paid'],30)

    def test_54_tax_insufficient_cash_keeps_claim_unpaid(self):
        w=fresh();w.apply('assess',1,'assess_tax',tax_id='T1',payer='farmer-a',amount=150,authority_ref='rule',basis_ref='basis')
        old=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('pay',2,'pay_tax',tax_id='T1',amount=150)
        self.assertEqual(old,w.checksum())

    def test_55_simultaneous_claims_neither_allocate_by_id_nor_partial_commit(self):
        w=fresh()
        w.s['econ3']['stocks']['farm']['seed']=6
        w.s['econ3']['consumed']['seed']=6
        w.schedule('B',8,'start_job',job_id='b',recipe_id='grow',start=8,end=12,workers=['farmer-b'])
        w.schedule('A',8,'start_job',job_id='a',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(8)
        self.assertEqual(before,w.checksum())
        self.assertEqual(w.s['econ3']['active_jobs'],{})

    def test_56_simultaneous_independent_jobs_can_both_begin(self):
        w=fresh()
        w.schedule('z-farm',8,'start_job',job_id='farm-day',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.schedule('a-cook',8,'start_job',job_id='cook-day',recipe_id='cook',start=8,end=12,workers=['person-B'])
        w.run_until(8)
        self.assertEqual(set(w.s['econ3']['active_jobs']),{'farm-day','cook-day'})
        self.assertEqual(w.s['econ3']['produced']['grain'],0)

    def test_57_future_output_not_usable_at_same_frontier(self):
        w=fresh()
        w.s['econ3']['recipes']['mill']={'site':'farm','inputs':{'grain':4},'outputs':{'meal':1},'qual':'grow'}
        w.apply('start',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.apply('other-commit',9,'commit_shift',person='farmer-b',start=12,end=14,role='work:mill')
        w.schedule('A-complete',12,'complete_job',job_id='j')
        w.schedule('Z-new',12,'start_job',job_id='j2',recipe_id='mill',start=12,end=14,workers=['farmer-b'])
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(12)
        self.assertEqual(before,w.checksum())

    def test_58_missing_household_meals_are_not_phantom_consumption(self):
        w=run_day('caregiver_mobilized');e=w.s['econ3']
        self.assertEqual(e['consumed']['meal'],0)
        self.assertEqual(e['needs_audit'][0]['unmet_meals'],6)
        self.assertEqual(e['stocks']['house-1']['meal'],0)

    def test_59_household_care_not_full_just_from_a_commitment(self):
        w=fresh();w.apply('no-work',17,'review_no_change')
        w.apply('audit',17,'audit_needs',audit_id='audit',household='house-1')
        self.assertEqual(w.s['econ3']['needs_audit'][0]['unmet_care_hours'],4)

    def test_60_serialization_and_replay_identical_under_same_implementation(self):
        w=run_day('farmer_mobilized')
        restore=World.load(w.save())
        self.assertEqual(w.checksum(),restore.checksum())
        replay=fresh()
        for ev in w.s['journal']:
            replay.apply(ev['id'],ev['at'],ev['op'],**ev['params'])
        self.assertEqual(w.checksum(),replay.checksum())

    def test_61_tax_plus_wages_never_double_counts_cash(self):
        w=fresh();w.apply('tax',1,'assess_tax',tax_id='T',payer='farmer-a',amount=20,authority_ref='rule',basis_ref='base')
        w.apply('paid',2,'pay_tax',tax_id='T',amount=20)
        w.apply('start',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.apply('done',12,'complete_job',job_id='j')
        w.apply('accrue',13,'accrue_job_wages',job_id='j',rate=3,wage_agreement_ref='wage-contract')
        w.apply('payment',14,'pay',person='farmer-a',amount=8,**{'from':'treasury'})
        self.assertEqual(w.s['wage_due']['farmer-a'],4)
        self.assertEqual(sum(w.s['cash'].values()),1000)

    def test_62_demand_is_not_output_and_supply_is_not_delivery(self):
        w=fresh();self.assertEqual(w.s['econ3']['needs']['house-1']['meal_required'],6)
        self.assertEqual(w.s['econ3']['meals_delivered'],{})
        w.apply('no-work',17,'review_no_change');w.apply('audit',17,'audit_needs',audit_id='audit',household='house-1')
        self.assertEqual(w.s['econ3']['needs_audit'][0]['unmet_meals'],6)
        self.assertEqual(w.s['econ3']['stocks']['house-1']['grain'],8)


    def test_63_same_time_tax_and_regular_transfer_compete_for_payer_cash(self):
        w=fresh()
        w.apply('tax',1,'assess_tax',tax_id='T',payer='farmer-a',amount=70,authority_ref='rule',basis_ref='basis')
        w.schedule('A-transfer',2,'transfer_cash',**{'from':'farmer-a','to':'army','amount':70})
        w.schedule('Z-tax',2,'pay_tax',tax_id='T',amount=70)
        old=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(2)
        self.assertEqual(old,w.checksum())
        self.assertEqual(w.s['cash']['farmer-a'],100)

    def test_64_same_time_tax_and_wage_compete_for_treasury(self):
        w=fresh()
        w.apply('tax',1,'assess_tax',tax_id='T',payer='farmer-a',amount=80,authority_ref='rule',basis_ref='basis')
        w.apply('owed',1,'accrue_pay',person='farmer-a',amount=550)
        w.schedule('tax-collection',2,'pay_tax',tax_id='T',amount=80)
        w.schedule('wage-payment',2,'pay',**{'from':'treasury'},person='farmer-a',amount=550)
        w.run_until(2)
        self.assertEqual(w.s['cash']['treasury'],130)
        self.assertEqual(w.s['wage_due']['farmer-a'],0)
        self.assertEqual(sum(w.s['cash'].values()),1000)

    def test_65_two_same_time_wage_claims_cannot_spend_one_obligation_twice(self):
        w=fresh();w.apply('owed',1,'accrue_pay',person='farmer-a',amount=30)
        w.schedule('a',2,'pay',**{'from':'treasury'},person='farmer-a',amount=20)
        w.schedule('b',2,'pay',**{'from':'treasury'},person='farmer-a',amount=20)
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(2)
        self.assertEqual(before,w.checksum())

    def test_66_two_simultaneous_tax_payments_cannot_double_collect_one_claim(self):
        w=fresh();w.apply('tax',1,'assess_tax',tax_id='T',payer='farmer-a',amount=70,authority_ref='rule',basis_ref='basis')
        w.schedule('a',2,'pay_tax',tax_id='T',amount=50)
        w.schedule('b',2,'pay_tax',tax_id='T',amount=50)
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(2)
        self.assertEqual(before,w.checksum())


def physical_stock(e,loc,mat):
    return e['stocks'].get(loc,{}).get(mat,0)


if __name__=='__main__':unittest.main()

class EconomicConcurrencyRegressionTests(unittest.TestCase):
    def test_67_three_simultaneous_jobs_cannot_overbook_two_person_site(self):
        from irgs_reference import actor
        w=fresh(); e=w.s['econ3']
        w.s['population']['residual']-=1
        w.s['actors']['farmer-c']=actor('farmer-c','farm')
        e['qualifications']['farmer-c']=['grow']
        w.s['commitments']['farmer-c']=[[8,12,'work:grow']]
        w._validate(w.s)
        for i,worker in enumerate(('farmer-a','farmer-b','farmer-c')):
            w.schedule('request-'+str(i),8,'start_job',job_id='job-'+str(i),recipe_id='grow',start=8,end=12,workers=[worker])
        prior=w.checksum()
        with self.assertRaises(InvalidEvent): w.run_until(8)
        self.assertEqual(prior,w.checksum())
        self.assertEqual(e['produced']['grain'],0)

    def test_68_commit_shift_cannot_claim_past_work_time(self):
        w=fresh(); w.apply('now',11,'review_no_change')
        old=w.checksum()
        with self.assertRaises(InvalidEvent):
            w.apply('backdate',11,'commit_shift',person='farmer-a',start=9,end=12,role='alternate')
        self.assertEqual(old,w.checksum())

    def test_69_mandate_and_enrollment_same_frontier_not_sorted_into_authority(self):
        w=fresh();w.schedule('a-authorize',1,'authorize_mobilization',mandate='M',target=1)
        w.schedule('z-enroll',1,'enroll',person='farmer-a')
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(1)
        self.assertEqual(before,w.checksum())

    def test_70_simultaneous_release_and_same_shift_assignment_need_staging(self):
        w=fresh();w.schedule('a-release',3,'release_shift',person='farmer-a',start=8,end=12,role='work:grow',authority_ref='lawful-supervisor')
        w.schedule('z-reassign',3,'commit_shift',person='farmer-a',start=8,end=12,role='military_duty')
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(3)
        self.assertEqual(before,w.checksum())

    def test_71_independent_same_time_tax_assessment_and_different_claim_payment(self):
        w=fresh();w.apply('old-tax',1,'assess_tax',tax_id='old',payer='farmer-a',amount=20,authority_ref='tax-law',basis_ref='land')
        w.schedule('A-tax',2,'assess_tax',tax_id='new',payer='farmer-b',amount=30,authority_ref='tax-law',basis_ref='land')
        w.schedule('Z-pay-old',2,'pay_tax',tax_id='old',amount=20)
        w.run_until(2)
        self.assertEqual(w.s['econ3']['tax_claims']['old']['paid'],20)
        self.assertEqual(w.s['econ3']['tax_claims']['new']['paid'],0)
        self.assertEqual(w.s['cash']['treasury'],620)

    def test_72_unrelated_work_settlement_and_wage_accrual_commute(self):
        w=fresh()
        w.apply('j1',8,'start_job',job_id='j1',recipe_id='grow',start=8,end=10,workers=['farmer-a'])
        w.apply('j2',8,'start_job',job_id='j2',recipe_id='cook',start=8,end=12,workers=['person-B'])
        w.apply('j1-end',10,'complete_job',job_id='j1')
        w.schedule('a-accrue',12,'accrue_job_wages',job_id='j1',rate=2,wage_agreement_ref='W')
        w.schedule('z-complete',12,'complete_job',job_id='j2')
        w.run_until(12)
        self.assertEqual(w.s['wage_due']['farmer-a'],4)
        self.assertIn('j2',w.s['econ3']['completed_jobs'])

    def test_73_same_job_completion_and_wage_credit_require_two_frontiers(self):
        w=fresh();w.apply('j',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        w.schedule('a-finish',12,'complete_job',job_id='j')
        w.schedule('z-credit',12,'accrue_job_wages',job_id='j',rate=2,wage_agreement_ref='W')
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(12)
        self.assertEqual(before,w.checksum())

    def test_74_same_time_independent_ship_receive_and_dispatch(self):
        w=fresh()
        w.apply('dispatch-first',1,'dispatch_stock',shipment_id='old',**{'from':'house-1','to':'farm'},material='grain',quantity=2,route_ref='road',minimum_transit=2)
        w.schedule('receive-first',3,'receive_stock',shipment_id='old')
        w.schedule('dispatch-next',3,'dispatch_stock',shipment_id='new',**{'from':'house-1','to':'farm'},material='grain',quantity=1,route_ref='road',minimum_transit=2)
        w.run_until(3)
        self.assertEqual(w.s['econ3']['shipments']['old']['status'],'received')
        self.assertEqual(w.s['econ3']['shipments']['new']['status'],'transit')
        self.assertEqual(total(w.s['econ3'],'grain'),8)

    def test_75_same_epoch_job_uses_only_prior_stock_not_new_receipt(self):
        w=fresh()
        w.s['econ3']['stocks']['farm']['seed']=0
        w.s['econ3']['stocks']['house-1']['seed']=12
        # Adding a location without moving opening stock is valid: total conserved.
        # Seed the earlier lawful shipment through a real dispatch rather than a phantom receipt.
        w.apply('ship',2,'dispatch_stock',shipment_id='old',**{'from':'house-1','to':'farm'},material='seed',quantity=4,route_ref='road',minimum_transit=6)
        w.schedule('a-arrive',8,'receive_stock',shipment_id='old')
        w.schedule('z-start',8,'start_job',job_id='j',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(8)
        self.assertEqual(before,w.checksum())
