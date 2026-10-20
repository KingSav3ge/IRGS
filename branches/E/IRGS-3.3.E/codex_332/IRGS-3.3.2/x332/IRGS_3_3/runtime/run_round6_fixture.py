"""Round 6: separate certified work, physical loss, replacement transit, new consent and recovery."""
import json
from pathlib import Path
from test_work_recovery import world,start,step,fire,settle,recover
from economic_extension import total
from r6_work import R6World
from r6_audit import audit_r6

def run():
    w=world(); opening={'population':w.display_population()['total'],
      'currency':sum(w.s['cash'].values()),'seed':total(w.s['econ3'],'seed'),
      'equipment_kits':sum(d.get('kit',0) for d in w.s['equipment'].values())}
    # Two institutions work in parallel; nothing from the burning farm licenses
    # cancelling the independent kitchen's already supported shift.
    start(w)
    w.apply('kitchen-start',8,'start_job',job_id='kitchen',recipe_id='cook',
            start=8,end=12,workers=['person-B'])
    step(w)
    w.schedule('tax',10,'assess_tax',tax_id='T',payer='farmer-b',amount=6,
         authority_ref='synthetic-tax-law',basis_ref='synthetic-plot')
    loss=fire(w)
    assert set(loss['committed'])=={'loss','tax'}
    assert w.s['econ3']['stocks']['farm']['grain']==3
    settle(w)
    w.apply('kitchen-complete',12,'complete_job',job_id='kitchen')
    w.apply('care-complete',12,'complete_care',person='caregiver-1',household='house-1',start=8,end=12)
    recover(w)
    w.apply('serve',18,'provision_meals',household='house-1',quantity=6)
    w.apply('audit',19,'audit_needs',audit_id='daily',household='house-1')
    rec=w.s['r6_settlements']; e=w.s['econ3']
    opening_net=opening['seed']
    audit=audit_r6(w.s)
    assert opening_net == total(e,'seed')+e['consumed']['seed']+e['losses']['seed']
    assert e['produced']['grain']==12 and e['produced']['meal']==12
    assert w.s['wage_due']['farmer-a']==8
    assert w.checksum()==R6World.load(w.save()).checksum()
    result={'candidate':'IRGS-CORE-3.3-CANDIDATE-R6','evidence':'bounded synthetic scenario; not calibration, source authentication, or playtest',
      'opening':opening,
      'fire_frontier':{'committed':loss['committed'],'deferred':loss['deferred'],'farm_grain_previously_accepted':3},
      'jobs':{'original':rec['farm'],'continuation':rec['farm-part2'],
         'milestone_ids':{k:[v['event_id'] for v in p['milestones']] for k,p in w.s['r6_progress'].items()},
         'work_claim_status':w.s['r5_shortfalls']['farm']['status']},
      'stocks':{'seed_opening':opening_net,'seed_consumed_work':e['consumed']['seed'],
         'seed_lost_fire':e['losses']['seed'],'seed_remaining':total(e,'seed'),
         'grain_accepted_total':e['produced']['grain'],'meals_accepted_total':e['produced']['meal'],
         'meals_served':e['meals_delivered']['house-1'],'shipment':e['shipments']['replacement']},
      'institutions':{'tax_assessed':e['tax_claims']['T']['assessed'],
         'tax_paid':e['tax_claims']['T']['paid'],'farmer_wage_due':w.s['wage_due']['farmer-a'],
         'needs_audit':e['needs_audit'][-1]},
      'closing':{'population':w.display_population()['total'], 'currency':sum(w.s['cash'].values()),
         'equipment_kits':sum(d.get('kit',0) for d in w.s['equipment'].values()),
         'save_load_same_checksum':True,'state_sha256':w.checksum()},
      'audit':audit,
      'limitations':['synthetic externally asserted work evidence; no authenticated receipts',
         'unassessed work interval has open wage-entitlement question',
         'R6 work operations are direct events; scheduler read-write certification missing',
         'one-worker fixed recipe and production model for this fixture',
         'no spoilage, co-product, quality, partial unaccepted output, or residual-cohort economic solver',
         'physical fire quantity and legal approvals are supplied assumptions, not internally resolved']}
    out=Path(__file__).resolve().parent.parent/'results/round6_recovery_fixture.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
