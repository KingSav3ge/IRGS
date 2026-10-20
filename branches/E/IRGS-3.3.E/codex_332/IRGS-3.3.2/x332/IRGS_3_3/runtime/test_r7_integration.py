"""R7 proposed bounded acceptance fixtures; NOT qualification of general scheduler."""
import copy, unittest
from irgs_reference import InvalidEvent
from test_work_recovery import world as base_world, start, step, fire, settle
from r7_frontier import R7World, footprint_r7, independent_components
from economic_extension import total, physical

PROFILE={'input':'iron','input_qty':3,'intermediate':'unfinished-shield',
         'intermediate_qty':2,'finished':'shield','finished_qty':1,
         'salvage':'scrap','salvage_per_unit':1}

def world():
    s=base_world().s;s['r7_profiles']={'shield-fixture':copy.deepcopy(PROFILE)}
    e=s['econ3']
    for m in ('iron','unfinished-shield','shield','scrap'):
        e['opening'][m]=0;e['produced'][m]=0;e['consumed'][m]=0
    e['opening']['iron']=10;e['stocks']['farm']['iron']=10
    return R7World(initial=s)

def new_item(w,eid='fabricate',item='A',at=8):
    return w.apply(eid,at,'make_intermediate',item_id=item,site='farm',
       profile_ref='shield-fixture',work_evidence_ref='synthetic-work',
       material_source_ref='synthetic-lot')

def inspect(w,outcome='accept',item='A',at=9):
    return w.apply('inspect-'+item,at,'inspect_intermediate',item_id=item,
       outcome=outcome,inspection_ref='synthetic-inspection',inspector_authority_ref='synthetic-inspector')

def accept(w,item='A',at=10):
    return w.apply('accept-'+item,at,'accept_intermediate',item_id=item,
       acceptance_ref='synthetic-acceptance',competent_authority_ref='synthetic-authority')

def salvage(w,item='A',at=10):
    return w.apply('salvage-'+item,at,'salvage_intermediate',item_id=item,
       salvage_authority_ref='synthetic-authority',salvage_assessment_ref='synthetic-assessment')

def schedule(w,eid,at,op,**p):w.schedule(eid,at,op,**p)

def milestone_p(a,b,job='farm'):
    return {'job_id':job,'from_at':a,'to_at':b,'selected_model_ref':'synthetic-grow-1h',
       'work_evidence_ref':'synthetic-attested-work','output_acceptance_ref':'synthetic-output'}

class R7IntegrationTests(unittest.TestCase):
    def test_166_scheduled_tracked_start(self):
        w=world()
        schedule(w,'start',8,'start_tracked_job',job_id='farm',recipe_id='grow',start=8,end=12,
          workers=['farmer-a'],selected_model_ref='synthetic-grow-1h')
        got=w.run_until(8)
        self.assertIn('start',got['committed'])
        self.assertIn('farm',w.s['r6_progress'])
    def test_167_scheduled_tracked_milestone(self):
        w=world();start(w)
        schedule(w,'mile',9,'record_work_milestone',**milestone_p(8,9))
        self.assertIn('mile',w.run_until(9)['committed'])
        self.assertEqual(w.s['econ3']['produced']['grain'],3)
    def test_168_unrelated_tax_proceeds_with_work(self):
        w=world();start(w)
        schedule(w,'mile',9,'record_work_milestone',**milestone_p(8,9))
        schedule(w,'tax',9,'assess_tax',tax_id='T',payer='farmer-b',amount=2,
                 authority_ref='fictional-statute',basis_ref='fictional-plot')
        r=w.run_until(9)
        self.assertEqual(set(r['committed']),{'mile','tax'})
    def test_169_same_time_same_job_does_not_pick_winner(self):
        w=world();start(w)
        schedule(w,'mile-a',9,'record_work_milestone',**milestone_p(8,9))
        schedule(w,'mile-b',9,'record_work_milestone',**milestone_p(8,9))
        r=w.run_until(9)
        self.assertEqual(len(r['deferred']),1)
        self.assertEqual(w.s['econ3']['produced']['grain'],0)
        self.assertEqual(w.s['r6_progress']['farm']['hours_verified'],0)
    def test_170_independent_kitchen_progress_not_blocked(self):
        w=world();start(w)
        w.apply('kstart',8,'start_tracked_job',job_id='kitchen',recipe_id='cook',start=8,end=12,
               workers=['person-B'],selected_model_ref='synthetic-cook-1h')
        for id in ('a','b'):schedule(w,id,9,'record_work_milestone',**milestone_p(8,9))
        schedule(w,'k',9,'record_work_milestone',job_id='kitchen',from_at=8,to_at=9,
             selected_model_ref='synthetic-cook-1h',work_evidence_ref='synthetic',output_acceptance_ref='synthetic')
        out=w.run_until(9)
        self.assertIn('k',out['committed'])
        self.assertEqual(w.s['econ3']['produced']['meal'],3)
        self.assertEqual(w.s['econ3']['produced']['grain'],0)
    def test_171_loss_precedes_ambiguous_milestone_no_new_output(self):
        w=world();start(w)
        schedule(w,'fire',9,'physical_loss',location='farm',material='seed',quantity=9,cause_ref='synthetic-fire',evidence_ref='synthetic-inspection')
        schedule(w,'milestone',9,'record_work_milestone',**milestone_p(8,9))
        result=w.run_until(9)
        self.assertIn('fire',result['physical_losses'])
        self.assertEqual(len(result['deferred']),1)
        self.assertEqual(w.s['econ3']['produced']['grain'],0)
    def test_172_milestone_at_prior_time_survives_fire(self):
        w=world();start(w)
        schedule(w,'mile',9,'record_work_milestone',**milestone_p(8,9))
        schedule(w,'fire',10,'physical_loss',location='farm',material='seed',quantity=9,cause_ref='synthetic-fire',evidence_ref='synthetic-inspection')
        got=w.run_until(10)
        self.assertEqual(set(got['committed']),{'mile','fire'})
        self.assertEqual(w.s['econ3']['produced']['grain'],3)
        self.assertEqual(w.s['econ3']['losses']['seed'],9)
    def test_173_same_time_start_then_milestone_undetermined(self):
        w=world()
        schedule(w,'start',8,'start_tracked_job',job_id='farm',recipe_id='grow',start=8,end=12,workers=['farmer-a'],selected_model_ref='synthetic-grow-1h')
        schedule(w,'mile',8,'record_work_milestone',**milestone_p(8,9))
        result=w.run_until(8)
        self.assertTrue(result['deferred']);self.assertEqual(w.s['r6_progress'],{})
    def test_174_missing_prerequisite_categorized_not_committed(self):
        w=world();schedule(w,'mile',9,'record_work_milestone',**milestone_p(8,9))
        r=w.run_until(9)
        self.assertEqual(r['committed'],[])
        self.assertIn('invalid_or_missing_prerequisite',w.s['r4_deferred'][r['deferred'][0]]['diagnostic'])
    def test_175_schedule_idempotence_is_not_duplicate_allocation(self):
        w=world();start(w)
        schedule(w,'mile',9,'record_work_milestone',**milestone_p(8,9))
        before=w.checksum()
        with self.assertRaises(InvalidEvent):schedule(w,'mile',9,'record_work_milestone',**milestone_p(8,9))
        self.assertEqual(w.checksum(),before)
    def test_176_replay_same_state_after_scheduler(self):
        w=world();start(w);schedule(w,'mile',9,'record_work_milestone',**milestone_p(8,9));w.run_until(9)
        self.assertEqual(w.checksum(),R7World.load(w.save()).checksum())
    def test_177_fabrication_consumes_raw_material(self):
        w=world();new_item(w)
        self.assertEqual(w.s['econ3']['stocks']['farm']['iron'],7)
        self.assertEqual(w.s['econ3']['consumed']['iron'],3)
        self.assertEqual(physical(w.s['econ3'],'wip:A','unfinished-shield'),2)
    def test_178_work_in_progress_is_not_accepted(self):
        w=world();new_item(w)
        self.assertEqual(w.s['econ3']['stocks']['farm'].get('shield',0),0)
        self.assertEqual(w.s['r7_intermediates']['A']['status'],'uninspected')
    def test_179_inspection_not_physical_transformation(self):
        w=world();new_item(w);inspect(w)
        self.assertEqual(w.s['econ3']['produced']['shield'],0)
        self.assertEqual(w.s['r7_intermediates']['A']['status'],'inspected_accept')
    def test_180_acceptance_consumes_wip_and_produces_one_item(self):
        w=world();new_item(w);inspect(w);accept(w)
        self.assertEqual(w.s['econ3']['consumed']['unfinished-shield'],2)
        self.assertEqual(w.s['econ3']['produced']['shield'],1)
        self.assertEqual(w.s['r7_intermediates']['A']['status'],'accepted')
    def test_181_acceptance_twice_not_double_counted(self):
        w=world();new_item(w);inspect(w);accept(w);old=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('accept-again',11,'accept_intermediate',item_id='A',acceptance_ref='a',competent_authority_ref='b')
        self.assertEqual(w.checksum(),old)
    def test_182_rejection_can_salvage_actual_remaining_stock(self):
        w=world();new_item(w);inspect(w,'reject');salvage(w)
        self.assertEqual(w.s['econ3']['produced']['shield'],0)
        self.assertEqual(w.s['econ3']['produced']['scrap'],2)
        self.assertEqual(w.s['r7_intermediates']['A']['status'],'salvaged')
    def test_183_salvage_requires_inspection(self):
        w=world();new_item(w);old=w.checksum()
        with self.assertRaises(InvalidEvent):salvage(w)
        self.assertEqual(w.checksum(),old)
    def test_184_physical_wip_loss_reconciles_records(self):
        w=world();new_item(w)
        w.apply('loss',9,'physical_loss',location='wip:A',material='unfinished-shield',quantity=1,cause_ref='synthetic-damage',evidence_ref='synthetic-inspection')
        self.assertEqual(w.s['r7_intermediates']['A']['physical_qty'],1)
        self.assertEqual(w.s['r7_intermediates']['A']['status'],'damaged')
        self.assertEqual(w.s['econ3']['losses']['unfinished-shield'],1)
    def test_185_damaged_intermediate_cannot_be_accepted(self):
        w=world();new_item(w)
        w.apply('loss',9,'physical_loss',location='wip:A',material='unfinished-shield',quantity=1,cause_ref='synthetic-damage',evidence_ref='synthetic-inspection')
        old=w.checksum()
        with self.assertRaises(InvalidEvent):inspect(w,'accept',at=10)
        self.assertEqual(w.checksum(),old)
    def test_186_damaged_reject_and_recover_one_actual_unit(self):
        w=world();new_item(w)
        w.apply('loss',9,'physical_loss',location='wip:A',material='unfinished-shield',quantity=1,cause_ref='synthetic-damage',evidence_ref='synthetic-inspection')
        inspect(w,'reject',at=10);salvage(w,at=11)
        self.assertEqual(w.s['econ3']['produced']['scrap'],1)
        self.assertEqual(w.s['econ3']['produced']['shield'],0)
        self.assertEqual(w.s['econ3']['losses']['unfinished-shield'],1)
    def test_187_selected_profile_required(self):
        w=world();old=w.checksum()
        with self.assertRaises(InvalidEvent):w.apply('invalid',8,'make_intermediate',item_id='A',site='farm',profile_ref='unselected',work_evidence_ref='x',material_source_ref='y')
        self.assertEqual(w.checksum(),old)
    def test_188_no_raw_stock_conjured_on_shortage(self):
        w=world();new_item(w,item='A');new_item(w,eid='B-make',item='B',at=9);new_item(w,eid='C-make',item='C',at=10)
        old=w.checksum()
        with self.assertRaises(InvalidEvent):new_item(w,eid='D-make',item='D',at=11)
        self.assertEqual(w.checksum(),old)
    def test_189_contested_raw_stock_fabrication_unexecuted(self):
        w=world()
        for jid in ('A','B'):
            schedule(w,'make-'+jid,8,'make_intermediate',item_id=jid,site='farm',profile_ref='shield-fixture',work_evidence_ref='synthetic',material_source_ref='synthetic')
        got=w.run_until(8)
        self.assertEqual(got['committed'],[])
        self.assertEqual(w.s['econ3']['stocks']['farm']['iron'],10)
        self.assertEqual(len(got['deferred']),1)
    def test_190_independent_tax_not_blocked_by_fabrication_conflict(self):
        w=world()
        for jid in ('A','B'):
            schedule(w,'make-'+jid,8,'make_intermediate',item_id=jid,site='farm',profile_ref='shield-fixture',work_evidence_ref='synthetic',material_source_ref='synthetic')
        schedule(w,'tax',8,'assess_tax',tax_id='F',payer='farmer-a',amount=1,authority_ref='fictional',basis_ref='fictional')
        r=w.run_until(8)
        self.assertIn('tax',r['committed'])
        self.assertEqual(w.s['econ3']['produced']['unfinished-shield'],0)
    def test_191_scheduled_full_fabrication_disposition(self):
        w=world()
        schedule(w,'make',8,'make_intermediate',item_id='A',site='farm',profile_ref='shield-fixture',work_evidence_ref='synthetic',material_source_ref='synthetic')
        schedule(w,'inspect',9,'inspect_intermediate',item_id='A',outcome='accept',inspection_ref='synthetic',inspector_authority_ref='synthetic')
        schedule(w,'accept',10,'accept_intermediate',item_id='A',acceptance_ref='synthetic',competent_authority_ref='synthetic')
        r=w.run_until(10)
        self.assertEqual(set(r['committed']),{'make','inspect','accept'})
        self.assertEqual(w.s['econ3']['produced']['shield'],1)
    def test_192_same_frontier_inspection_and_acceptance_need_order(self):
        w=world();new_item(w)
        schedule(w,'inspect',9,'inspect_intermediate',item_id='A',outcome='accept',inspection_ref='synthetic',inspector_authority_ref='synthetic')
        schedule(w,'accept',9,'accept_intermediate',item_id='A',acceptance_ref='synthetic',competent_authority_ref='synthetic')
        r=w.run_until(9)
        self.assertEqual(len(r['deferred']),1)
        self.assertEqual(w.s['r7_intermediates']['A']['status'],'uninspected')
    def test_193_same_frontier_raw_loss_committed_before_claimed_production(self):
        w=world()
        schedule(w,'loss',8,'physical_loss',location='farm',material='iron',quantity=4,cause_ref='synthetic-fire',evidence_ref='synthetic-inspection')
        schedule(w,'fabrication',8,'make_intermediate',item_id='A',site='farm',profile_ref='shield-fixture',work_evidence_ref='synthetic',material_source_ref='synthetic')
        r=w.run_until(8)
        self.assertIn('loss',r['physical_losses'])
        self.assertEqual(w.s['econ3']['consumed']['iron'],0)
        self.assertEqual(w.s['econ3']['losses']['iron'],4)
        self.assertTrue(r['deferred'])
    def test_194_material_conservation_and_save_load(self):
        w=world();new_item(w);inspect(w,'reject');salvage(w)
        e=w.s['econ3']
        for m in ('iron','unfinished-shield','shield','scrap'):
            self.assertEqual(total(e,m),e['opening'][m]+e['produced'][m]-e['consumed'][m]-e.get('losses',{}).get(m,0))
        self.assertEqual(w.checksum(),R7World.load(w.save()).checksum())
    def test_195_wip_and_accepted_goods_are_separate_stock(self):
        w=world();new_item(w)
        self.assertEqual(total(w.s['econ3'],'unfinished-shield'),2)
        self.assertEqual(total(w.s['econ3'],'shield'),0)
        inspect(w);accept(w)
        self.assertEqual(total(w.s['econ3'],'unfinished-shield'),0)
        self.assertEqual(total(w.s['econ3'],'shield'),1)


    def test_196_unsubstantiated_combined_losses_roll_back_full_frontier(self):
        w=world();old=w.checksum()
        schedule(w,'tax',8,'assess_tax',tax_id='R',payer='farmer-a',amount=1,authority_ref='law',basis_ref='source')
        schedule(w,'loss-a',8,'physical_loss',location='farm',material='iron',quantity=6,cause_ref='fire',evidence_ref='record-1')
        schedule(w,'loss-b',8,'physical_loss',location='farm',material='iron',quantity=6,cause_ref='fire',evidence_ref='record-2')
        staged=w.checksum()
        with self.assertRaises(InvalidEvent):w.run_until(8)
        self.assertEqual(w.checksum(),staged)
        self.assertNotIn('R',w.s['econ3']['tax_claims'])
    def test_197_damage_after_inspection_invalidates_prior_acceptance(self):
        w=world();new_item(w);inspect(w)
        w.apply('wip-fire',10,'physical_loss',location='wip:A',material='unfinished-shield',quantity=1,cause_ref='fire',evidence_ref='stock-count')
        self.assertEqual(w.s['r7_intermediates']['A']['status'],'damaged')
        self.assertEqual(w.s['r7_intermediates']['A']['inspection_outcome'],None)
        with self.assertRaises(InvalidEvent):accept(w,at=11)
    def test_198_salvage_not_a_renewed_material_source_without_transfer(self):
        w=world();new_item(w);inspect(w,'reject');salvage(w)
        self.assertEqual(physical(w.s['econ3'],'farm','scrap'),2)
        self.assertEqual(w.s['econ3']['stocks']['farm']['iron'],7)
        self.assertEqual(w.s['econ3']['produced']['iron'],0)
    def test_199_unknown_schedule_operation_does_not_mutate_world(self):
        w=world();schedule(w,'future-action',8,'miracle_factory',material='shield')
        r=w.run_until(8)
        self.assertEqual(r['committed'],[])
        self.assertEqual(len(r['deferred']),1)
        self.assertEqual(total(w.s['econ3'],'shield'),0)
    def test_200_deferred_claims_roundtrip_save_reload(self):
        w=world()
        for jid in ('A','B'):
            schedule(w,'make-'+jid,8,'make_intermediate',item_id=jid,site='farm',profile_ref='shield-fixture',work_evidence_ref='e',material_source_ref='m')
        w.run_until(8)
        same=R7World.load(w.save())
        self.assertEqual(w.checksum(),same.checksum())
        self.assertEqual(len(same.s['r4_deferred']),1)
    def test_201_corrupt_wip_quantity_fails_validation(self):
        w=world();new_item(w)
        bad=copy.deepcopy(w.s)
        bad['r7_intermediates']['A']['physical_qty']=50
        with self.assertRaises(AssertionError):R7World(state=bad)


    def test_202_source_profile_snapshot_controls_later_completion(self):
        w=world();new_item(w)
        w.s['r7_profiles']['shield-fixture']['finished_qty']=999  # simulate later profile revision
        inspect(w);accept(w)
        self.assertEqual(w.s['econ3']['produced']['shield'],1)
    def test_203_corrupt_saved_profile_snapshot_is_detected(self):
        w=world();new_item(w)
        bad=copy.deepcopy(w.s)
        bad['r7_intermediates']['A']['profile_snapshot']['finished_qty']=50
        with self.assertRaises(AssertionError):R7World(state=bad)

if __name__=='__main__':unittest.main()
