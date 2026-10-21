"""Executed bounded fixture suite. Tests do NOT calibrate full IRGS simulation."""
import copy, json, unittest
from irgs_reference import World, InvalidEvent, initial_world


def enlist_baseline(w):
    w.apply('M1',1,'authorize_mobilization',mandate='GOV-order-01',target=1000)
    w.apply('M2',2,'enroll',person='caregiver-1')
    w.apply('M3',3,'enroll_from_residual',count=599,batch_id='inducted',source_cohort='region-residents-01',eligible_attestation='candidate-roll-01')
    return ['caregiver-1']+[f'inducted:{i:04d}' for i in range(599)]


def prepare_mobilization(w):
    ids=enlist_baseline(w)
    w.apply('M4',4,'attest_training',persons=ids[:450],external_training_evidence='training-completion-external-01',adapter_ref='fixture-training-profile')
    w.apply('M5',5,'issue_kits',persons=ids[:300])
    w.apply('M6',6,'authorize_budget',name='military-outlay',amount=800)
    return ids


class UnificationTests(unittest.TestCase):
    def test_01_order_target_does_not_create_people(self):
        w=initial_world()
        w.apply('m',1,'authorize_mobilization',mandate='king',target=1000)
        self.assertEqual(w.display_population()['total'],1200)
        self.assertEqual(w.display_population()['enlisted_memberships'],0)

    def test_02_cohort_extract_and_named_enlist_do_not_double_population(self):
        w=initial_world(); enlist_baseline(w)
        self.assertEqual(w.display_population(), {'residual_unnamed':599,'named':601,'total':1200,'enlisted_memberships':600})

    def test_03_duplicate_enrollment_invalid_atomic(self):
        w=initial_world(); enlist_baseline(w); checksum=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('dup',4,'enroll',person='caregiver-1')
        self.assertEqual(w.checksum(),checksum)

    def test_04_over_recruit_invalid_atomic(self):
        w=initial_world(); enlist_baseline(w); checksum=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('oversub',4,'enroll_from_residual',count=401,batch_id='more',source_cohort='region-residents-01',eligible_attestation='list')
        self.assertEqual(w.checksum(),checksum)

    def test_05_equipment_issued_by_real_conserved_transfer(self):
        w=initial_world(); prepare_mobilization(w)
        self.assertEqual(w.s['equipment']['depot']['kit'],0)
        self.assertEqual(sum(x.get('kit',0) for x in w.s['equipment'].values()),300)

    def test_06_readiness_subset_blocks_incompatible_care_shift(self):
        w=initial_world(); prepare_mobilization(w)
        self.assertEqual(len(w.ready_subset(9,10)),299)
        self.assertEqual(len(w.ready_subset(13,14)),300)
        self.assertIn('caregiver-1',w.s['formations']['army']['members'])
        self.assertIn('caregiver-1',w.s['households']['house-1']['members'])

    def test_07_person_can_hold_household_and_army_membership(self):
        w=initial_world(); prepare_mobilization(w)
        self.assertIn('caregiver-1',w.s['households']['house-1']['members'])
        self.assertIn('caregiver-1',w.s['formations']['army']['members'])
        self.assertEqual(w.s['population']['baseline'],1200)

    def test_08_double_booking_rejected_without_changing_membership(self):
        w=initial_world(); prepare_mobilization(w); old=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('shift',7,'commit_shift',person='caregiver-1',start=9,end=11,role='guard_duty')
        self.assertEqual(w.checksum(),old)

    def test_09_budget_authorization_neither_cash_nor_pay(self):
        w=initial_world(); w.apply('auth',1,'authorize_budget',name='army-budget',amount=3000)
        self.assertEqual(w.s['cash']['army'],0)
        self.assertEqual(w.s['cash']['treasury'],1000)
        self.assertEqual(w.s['wage_due'],{})

    def test_10_competing_actual_cash_transfers_prevent_overspend(self):
        w=initial_world();w.apply('A',1,'authorize_budget',name='army',amount=750)
        w.apply('B',2,'authorize_budget',name='civilian-project',amount=750)
        w.apply('C',3,'transfer_cash',**{'from':'treasury','to':'army','amount':750})
        old=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('D',4,'transfer_cash',**{'from':'treasury','to':'caregiver-1','amount':750})
        self.assertEqual(w.checksum(),old)
        self.assertEqual(w.s['cash']['treasury'],250)

    def test_11_accrual_payment_and_unpaid_claim_separate(self):
        w=initial_world(); w.apply('cash',1,'transfer_cash',**{'from':'treasury','to':'army','amount':100})
        w.apply('acc',2,'accrue_pay',person='caregiver-1',amount=40)
        w.apply('pay',3,'pay',person='caregiver-1',amount=15,**{'from':'army'})
        self.assertEqual(w.s['wage_due']['caregiver-1'],25)
        self.assertEqual(w.s['cash']['caregiver-1'],15)
        self.assertEqual(w.s['cash']['army'],85)

    def test_12_scarce_store_competition_is_explicit(self):
        w=initial_world()
        w.apply('alloc',1,'allocate_competing_kits',resolution_policy='priority_then_request_id',requests=[{'id':'u2','priority':2,'qty':100,'to':'unit2'},{'id':'u1','priority':1,'qty':250,'to':'unit1'}])
        self.assertEqual(w.s['equipment']['unit1']['kit'],250)
        self.assertEqual(w.s['equipment'].get('unit2',{}).get('kit',0),0)
        self.assertEqual(w.s['equipment']['depot']['kit'],50)
        self.assertEqual(sum(x.get('kit',0) for x in w.s['equipment'].values()),300)

    def test_13_order_received_after_deadline_cannot_execute(self):
        w=initial_world();w.apply('i',1,'issue_order',order_id='O1',deadline=4,recipient='army')
        w.schedule('receive',5,'receive_order',order_id='O1')
        w.run_until(5)
        self.assertEqual(w.s['orders']['O1']['received_at'],5)
        self.assertFalse(w.s['orders']['O1']['executed'])
        old=w.checksum()
        with self.assertRaises(InvalidEvent): w.apply('do',6,'execute_order',order_id='O1')
        self.assertEqual(old,w.checksum())

    def test_14_pending_queue_survives_save_reload(self):
        w=initial_world();w.apply('i',1,'issue_order',order_id='O1',deadline=10,recipient='army')
        w.schedule('receive',5,'receive_order',order_id='O1')
        restored=World.load(w.save())
        self.assertEqual(restored.checksum(),w.checksum())
        restored.run_until(5)
        self.assertEqual(restored.s['orders']['O1']['received_at'],5)
        self.assertEqual(len(restored.s['pending']),0)

    def test_15_custody_and_delayed_report_not_the_same_event(self):
        w=initial_world();w.apply('capture',1,'capture',person='person-B',by='army',location='holding-site')
        self.assertEqual(w.s['actors']['person-B']['location'],'holding-site')
        self.assertEqual(len(w.s['reports']),0)
        w.apply('report',5,'report',person='person-B',recipient='capital',message='missing')
        self.assertEqual(w.s['actors']['person-B']['custody']['by'],'army')
        self.assertEqual(w.display_population()['total'],1200)

    def test_16_release_promise_neither_custody_nor_legal_status(self):
        w=initial_world();w.apply('c',1,'capture',person='person-B',by='holder',location='compound')
        w.apply('p',2,'propose_release',person='person-B',by='holder',terms='after_formal_hearing')
        self.assertEqual(w.s['gov']['legal_status'],{})
        self.assertEqual(w.s['actors']['person-B']['custody']['by'],'holder')

    def test_17_legal_effect_recognition_and_custody_independent(self):
        w=initial_world();w.apply('c',1,'capture',person='person-B',by='holder',location='compound')
        w.apply('l',2,'legal_status_change',person='person-B',jurisdiction='J',to='free',authorized_decision_ref='decree-1',effective_at=2)
        self.assertEqual(w.s['actors']['person-B']['custody']['by'],'holder')
        self.assertEqual(w.s['recognitions'],[])
        w.apply('r',5,'recognize_status',person='person-B',jurisdiction='J',audience='third-party',claimed_status='free')
        self.assertEqual(len(w.s['recognitions']),1)
        self.assertEqual(w.s['gov']['legal_status']['person-B']['J']['effective_at'],2)

    def test_18_legal_claim_about_person_not_person_equipment(self):
        w=initial_world(); w.apply('c',1,'person_claim',subject='person-B',claimant='holder',basis='disputed indenture',disputed=True)
        self.assertEqual(w.display_population()['total'],1200)
        self.assertNotIn('person',w.s['equipment'].get('holder',{}))
        self.assertEqual(w.s['person_claims'][0]['disputed'],True)

    def test_19_simultaneous_exchange_both_effects_resolve_from_prestate(self):
        initial=initial_world().s
        initial['actors']['caregiver-1']['ammo']=1
        initial['actors']['person-B']['ammo']=1
        w=World(initial=initial)
        w.apply('fight',1,'simultaneous_exchange',engagement_id='E1',selected_effect_adapter='fixture_effects_only',attacks=[{'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'},{'from':'person-B','to':'caregiver-1','ammo_used':1,'effect':'disable'}])
        self.assertTrue(w.s['actors']['caregiver-1']['disabled'])
        self.assertTrue(w.s['actors']['person-B']['disabled'])
        self.assertEqual(w.s['actors']['caregiver-1']['ammo'],0)
        self.assertEqual(w.s['actors']['person-B']['ammo'],0)
        before=w.checksum()
        self.assertFalse(w.apply('fight',1,'simultaneous_exchange',engagement_id='E1',selected_effect_adapter='fixture_effects_only',attacks=[{'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'},{'from':'person-B','to':'caregiver-1','ammo_used':1,'effect':'disable'}]))
        self.assertEqual(before,w.checksum())

    def test_20_strategic_engagement_summary_never_reapplies_loss(self):
        s=initial_world().s;s['actors']['caregiver-1']['ammo']=1;s['actors']['person-B']['ammo']=1
        w=World(initial=s)
        w.apply('fight',1,'simultaneous_exchange',engagement_id='E1',selected_effect_adapter='fixture_effects_only',attacks=[{'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'},{'from':'person-B','to':'caregiver-1','ammo_used':1,'effect':'disable'}])
        w.apply('summary',2,'summarize_engagement',engagement_id='E1')
        self.assertEqual(w.s['engagement_summaries']['E1']['disabled_targets'],['caregiver-1','person-B'])
        self.assertFalse(w.s['engagement_summaries']['E1']['writes_to_actor_state'])
        self.assertEqual(w.s['actors']['caregiver-1']['ammo'],0)

    def test_21_missing_effect_adapter_does_not_roll_impossible_effect(self):
        w=initial_world();before=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('fight',1,'simultaneous_exchange',engagement_id='E',selected_effect_adapter='UNBOUND',attacks=[])
        self.assertEqual(before,w.checksum())
        w.apply('admin',1,'authorize_mobilization',mandate='king',target=1000)
        self.assertIn('mobilization',w.s['gov'])

    def test_22_demobilization_does_not_heal_or_pay_automatically(self):
        seeded=initial_world().s
        seeded['actors']['person-B']['disabled']=True  # explicit initial fixture fact
        w=World(initial=seeded);w.apply('a',1,'authorize_mobilization',mandate='king',target=1000)
        w.apply('e',2,'enroll',person='person-B')
        w.apply('k',3,'issue_kits',persons=['person-B'])
        w.apply('p',4,'accrue_pay',person='person-B',amount=12)
        w.apply('d',5,'demobilize',person='person-B')
        self.assertFalse(w.s['actors']['person-B']['enlisted'])
        self.assertTrue(w.s['actors']['person-B']['disabled'])
        self.assertEqual(w.s['wage_due']['person-B'],12)
        self.assertEqual(w.s['equipment']['depot']['kit'],300)

    def test_23_resume_and_replay_same_source_event_sequence(self):
        w=initial_world();prepare_mobilization(w)
        w.apply('pay',7,'transfer_cash',**{'from':'treasury','to':'army','amount':400})
        restored=World.load(w.save())
        self.assertEqual(restored.checksum(),w.checksum())
        second=initial_world()
        for event in w.s['journal']:
            second.apply(event['id'],event['at'],event['op'],**event['params'])
        self.assertEqual(second.checksum(),w.checksum())

    def test_24_same_event_id_different_payload_rejected(self):
        w=initial_world();w.apply('m',1,'authorize_mobilization',mandate='king',target=1000)
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('m',1,'authorize_mobilization',mandate='king',target=2000)
        self.assertEqual(w.checksum(),before)

    def test_25_peace_does_not_invent_conflict_or_population(self):
        w=initial_world();w.run_until(3650)
        self.assertEqual(w.display_population()['total'],1200)
        self.assertEqual(w.s['engagements'],[])
        # This is only a no-spawn clock fixture: it does NOT simulate 10 years of social/economic life.

    def test_26_separate_campaign_events_are_isolated(self):
        w=initial_world();q=initial_world();q.s['campaign_id']='OTHER-TEST'
        w.apply('shared-id',1,'authorize_mobilization',mandate='a',target=1000)
        q.apply('shared-id',1,'authorize_mobilization',mandate='b',target=500)
        self.assertNotEqual(w.s['gov']['mobilization']['target'],q.s['gov']['mobilization']['target'])
        self.assertEqual(w.display_population()['total'],q.display_population()['total'])

    def test_27_failed_transfer_is_atomic(self):
        w=initial_world();old=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('negative',1,'transfer_cash',**{'from':'treasury','to':'army','amount':1001})
        self.assertEqual(w.checksum(),old)

    def test_28_same_time_multiple_attacks_ammo_capacity_constrained(self):
        s=initial_world().s;s['actors']['caregiver-1']['ammo']=1;s['actors']['person-B']['ammo']=1
        w=World(initial=s);before=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('attack',1,'simultaneous_exchange',engagement_id='E',selected_effect_adapter='fixture_effects_only',attacks=[{'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'},{'from':'caregiver-1','to':'person-B','ammo_used':1,'effect':'disable'}])
        self.assertEqual(before,w.checksum())

    def test_29_legal_status_requires_authorization_reference(self):
        w=initial_world();before=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('legal',1,'legal_status_change',person='person-B',jurisdiction='J',to='free',authorized_decision_ref='',effective_at=1)
        self.assertEqual(w.checksum(),before)

    def test_30_different_event_payload_same_clock_is_allowed(self):
        w=initial_world();w.apply('a',1,'authorize_budget',name='army',amount=500)
        w.apply('b',1,'authorize_budget',name='school',amount=500)
        self.assertEqual(len(w.s['budgets']),2)


if __name__=='__main__':
    unittest.main(verbosity=2)

class ConcurrencyRegression(unittest.TestCase):
    def test_31_simultaneous_underfunded_transfers_neither_silently_wins(self):
        w=initial_world()
        w.schedule('A',1,'transfer_cash',**{'from':'treasury','to':'army','amount':700})
        w.schedule('B',1,'transfer_cash',**{'from':'treasury','to':'caregiver-1','amount':700})
        before=w.checksum()
        with self.assertRaises(InvalidEvent): w.run_until(1)
        self.assertEqual(before,w.checksum())
        self.assertEqual(w.s['cash']['treasury'],1000)

    def test_32_same_time_incompatible_shifts_are_atomic_rejection(self):
        w=initial_world()
        w.schedule('A',1,'commit_shift',person='person-B',start=10,end=12,role='duty1')
        w.schedule('B',1,'commit_shift',person='person-B',start=11,end=13,role='duty2')
        before=w.checksum()
        with self.assertRaises(InvalidEvent): w.run_until(1)
        self.assertEqual(before,w.checksum())

    def test_33_same_time_independent_funded_transfers_both_commit(self):
        w=initial_world()
        w.schedule('A',1,'transfer_cash',**{'from':'treasury','to':'army','amount':300})
        w.schedule('B',1,'transfer_cash',**{'from':'treasury','to':'caregiver-1','amount':400})
        w.run_until(1)
        self.assertEqual([w.s['cash'][x] for x in ['treasury','army','caregiver-1']], [300,300,400])

    def test_34_same_time_capture_and_escape_requires_causal_order(self):
        w=initial_world()
        w.schedule('A',1,'capture',person='person-B',by='guard',location='cell')
        w.schedule('B',1,'escape',person='person-B',location='street')
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(1)
        self.assertEqual(before,w.checksum())

    def test_35_undisclosed_invalid_event_does_not_partially_commit_epoch(self):
        w=initial_world()
        w.schedule('A',1,'authorize_budget',name='army',amount=100)
        w.schedule('B',1,'legal_status_change',person='person-B',jurisdiction='J',to='free',authorized_decision_ref='',effective_at=1)
        before=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(1)
        self.assertEqual(before,w.checksum())

    def test_36_order_issue_and_same_time_receipt_not_sorted_by_id(self):
        w=initial_world()
        w.schedule('A',1,'issue_order',order_id='O',recipient='army',deadline=2)
        w.schedule('B',1,'receive_order',order_id='O')
        with self.assertRaises(InvalidEvent):w.run_until(1)
        self.assertNotIn('O',w.s['orders'])
