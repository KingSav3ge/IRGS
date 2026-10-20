"""R7 integrated synthetic scheduler/work, fire, household, transit and rejected WIP."""
import json
from pathlib import Path
from test_r7_integration import world, PROFILE
from economic_extension import total
from r7_frontier import R7World
from r7_audit import audit_r7

def run():
    w=world()
    w.apply('farm-start',8,'start_tracked_job',job_id='farm',recipe_id='grow',start=8,end=12,workers=['farmer-a'],selected_model_ref='synthetic-grow-1h')
    w.apply('kitchen-start',8,'start_job',job_id='kitchen',recipe_id='cook',start=8,end=12,workers=['person-B'])
    w.schedule('farm-hour-one',9,'record_work_milestone',job_id='farm',from_at=8,to_at=9,
       selected_model_ref='synthetic-grow-1h',work_evidence_ref='synthetic-farm-attestation-1',output_acceptance_ref='synthetic-grain-acceptance-1')
    w.schedule('fire',10,'physical_loss',location='farm',material='seed',quantity=9,cause_ref='scenario-fire',evidence_ref='scenario-stock-count')
    w.schedule('tax',10,'assess_tax',tax_id='R7-T',payer='farmer-b',amount=6,authority_ref='fictional-statute',basis_ref='fictional-assessment')
    w.schedule('farm-assessment',11,'settle_disrupted_job',job_id='farm',wage_rate=2,wage_agreement_ref='fictional-contract',competent_authority_ref='fictional-supervisor',assessment_ref='synthetic-disruption-assessment')
    w.schedule('replacement-dispatch',12,'dispatch_stock',shipment_id='replacement',quantity=3,material='seed',**{'from':'warehouse','to':'farm'},route_ref='fictional-road',minimum_transit=1)
    w.schedule('kitchen-complete',12,'complete_job',job_id='kitchen')
    w.schedule('fabrication',12,'make_intermediate',item_id='shield-A',site='farm',profile_ref='shield-fixture',work_evidence_ref='synthetic-metalwork',material_source_ref='synthetic-iron-lot')
    w.schedule('replacement-arrive',13,'receive_stock',shipment_id='replacement')
    w.schedule('shift-new',13,'commit_shift',person='farmer-a',start=14,end=17,role='work:grow')
    w.schedule('workpiece-loss',13,'physical_loss',location='wip:shield-A',material='unfinished-shield',quantity=1,cause_ref='synthetic-accident',evidence_ref='synthetic-measurement')
    w.schedule('farm-continue',14,'start_continuation',parent_job_id='farm',job_id='farm-part2',recipe_id='grow',start=14,end=17,workers=['farmer-a'],selected_model_ref='synthetic-grow-1h',authorization_ref='fictional-new-consent')
    w.schedule('inspect-workpiece',14,'inspect_intermediate',item_id='shield-A',outcome='reject',inspection_ref='synthetic-inspection',inspector_authority_ref='fictional-inspector')
    for idx in range(3):
        w.schedule('farm-continued-'+str(idx),15+idx,'record_work_milestone',job_id='farm-part2',from_at=14+idx,to_at=15+idx,selected_model_ref='synthetic-grow-1h',work_evidence_ref='synthetic-hour-'+str(idx),output_acceptance_ref='synthetic-grain-'+str(idx))
    w.schedule('farm-finish',18,'finalize_tracked_job',job_id='farm-part2',wage_rate=2,wage_agreement_ref='fictional-contract',competent_authority_ref='fictional-supervisor',acceptance_ref='synthetic-farm-completion')
    w.schedule('salvage',19,'salvage_intermediate',item_id='shield-A',salvage_authority_ref='fictional-salvage-lead',salvage_assessment_ref='synthetic-recovery-measurement')
    result=w.run_until(20)
    e=w.s['econ3'];p=w.s['r7_intermediates']['shield-A']
    assert not result['deferred'],result
    assert e['consumed']['seed']==4 and e['losses']['seed']==9 and total(e,'seed')==3
    assert e['produced']['grain']==12 and e['produced']['meal']==12
    assert e['consumed']['iron']==3 and e['losses']['unfinished-shield']==1
    assert e['produced']['scrap']==1 and e['produced']['shield']==0
    assert p['status']=='salvaged'
    assert w.s['r5_shortfalls']['farm']['status']=='fulfilled_by_continuation'
    assert w.s['wage_due']['farmer-a']==8
    assert R7World.load(w.save()).checksum()==w.checksum()
    output={
      'status':'PROPOSED R7 bounded deterministic fixture; not authority/evidence authentication or a playtest',
      'scheduler':result,
      'population':w.display_population()['total'],
      'cash_total':sum(w.s['cash'].values()),
      'physical':{'seed':{'opening':16,'consumed':e['consumed']['seed'],'lost':e['losses']['seed'],'remaining':total(e,'seed')},
          'grain_accepted':e['produced']['grain'],'meals_accepted':e['produced']['meal'],
          'iron':{'opening':10,'consumed':e['consumed']['iron'],'remaining':total(e,'iron')},
          'intermediate':{'made':e['produced']['unfinished-shield'],'physically_lost':e['losses']['unfinished-shield'],
              'used_for_salvage':e['consumed']['unfinished-shield'],'remaining':total(e,'unfinished-shield')},
          'finished_shields':e['produced']['shield'],'salvage_scrap':e['produced']['scrap']},
      'work':{'original':w.s['r6_settlements']['farm'],'continuation':w.s['r6_settlements']['farm-part2'],
         'claim':w.s['r5_shortfalls']['farm']['status'],'wage_liability':w.s['wage_due']['farmer-a']},
      'workpiece':p,'tax':e['tax_claims']['R7-T'],
      'audit':audit_r7(w.s),'save_load_identical':True,'checksum':w.checksum(),
      'caveats':['selected rates and quantity conversions are synthetic','WIP conversion does not yet simulate worker hours or time/energy demand',
        'evidence and legal authority are supplied assertions','event footprints are bounded hand-declared contracts',
        'no independently qualified generic engine runtime','no actuarial casualty or calibrated civil economy model']}
    dest=Path(__file__).resolve().parent.parent/'results/round7_integration_fixture.json'
    dest.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'committed':len(result['committed']),'deferred':len(result['deferred']),
        'grain':e['produced']['grain'],'finished_shields':e['produced']['shield'],
        'scrap':e['produced']['scrap'],'checksum':w.checksum()},indent=2))
if __name__=='__main__':run()
