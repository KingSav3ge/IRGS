"""Synthetic R4 comparison fixture; outputs evidence, not a model forecast."""
from __future__ import annotations
import json
from pathlib import Path
from irgs_reference import digest
from selective_coordinator import R4World
from scale_coverage import Coverage
from test_economic_integration import fresh


def main():
    w=R4World(initial=fresh().s)
    opening={'population':w.display_population()['total'],'cash_total':sum(w.s['cash'].values()),
             'kit_total':sum(x.get('kit',0) for x in w.s['equipment'].values()),
             'grain':sum(x.get('grain',0) for x in w.s['econ3']['stocks'].values())}
    w.schedule('army-budget-claim',8,'transfer_cash',**{'from':'treasury','to':'army','amount':400})
    w.schedule('public-care-claim',8,'transfer_cash',**{'from':'treasury','to':'caregiver-1','amount':400})
    w.schedule('field-activity',8,'start_job',job_id='farm-local',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
    w.schedule('lawful-assessment',8,'assess_tax',tax_id='T-01',payer='farmer-b',amount=12,authority_ref='governing-tax-order',basis_ref='land-record')
    first=w.run_until(8)
    assert set(first['committed'])=={'field-activity','lawful-assessment'}
    assert len(first['deferred'])==1
    pending_cash=w.s['cash']['treasury']
    w.schedule('completed-work',12,'complete_job',job_id='farm-local')
    second=w.run_until(12)
    assert second['committed']==['completed-work']
    assert w.s['econ3']['produced']['grain']==12
    coverage=Coverage()
    coverage.record(source_id='completed-work',contributors=['farmer-a'],stream='grain',start=8,end=12,quantity=12,evidence_ref='completed_job:farm-local')
    stock_before_views=digest(w.s['econ3']['stocks'])
    day=coverage.view(0,24,'grain');month=coverage.view(0,720,'grain')
    assert day['quantity_from_complete_intervals']==month['quantity_from_complete_intervals']==12
    assert stock_before_views==digest(w.s['econ3']['stocks'])
    decision=w.decide_deferred(first['deferred'][0],['public-care-claim'],at=13,authority_ref='legally-competent-budget-holder')
    assert decision['approved_ids']==['public-care-claim']
    assert sum(w.s['cash'].values())==opening['cash_total']
    assert w.display_population()['total']==opening['population']
    reloaded=R4World.load(w.save())
    assert w.checksum()==reloaded.checksum()
    result={
       'candidate':'IRGS-CORE-3.3-CANDIDATE-R4',
       'status':'bounded synthetic reference harness; NOT accepted/selected/calibrated/playtested',
       'opening':opening,
       'at_8':{'committed_ids':first['committed'],'unresolved_contests':first['deferred'],
               'treasury_after_competing_claims':pending_cash,'physical_farm_seed_held_or_reserved':12},
       'at_12':{'committed_ids':second['committed'],'grain_produced':w.s['econ3']['produced']['grain'],
                'seed_consumed':w.s['econ3']['consumed']['seed']},
       'scale_views':{'daily':day,'monthly':month,'physical_stock_unchanged_by_both_views':True},
       'at_13':{'authority_ref':decision['authority_ref'],'approved_request_ids':decision['approved_ids'],
                'denied_request_ids':decision['denied_ids'], 'treasury_cash':w.s['cash']['treasury'],
                'caregiver_cash':w.s['cash']['caregiver-1'], 'army_cash':w.s['cash']['army']},
       'closing':{'population':w.display_population()['total'],
                   'cash_total':sum(w.s['cash'].values()),
                   'kit_total':sum(x.get('kit',0) for x in w.s['equipment'].values()),
                   'grain_total':sum(x.get('grain',0) for x in w.s['econ3']['stocks'].values()),
                   'same_implementation_save_load_checksum':w.checksum()},
       'limitations':[
           'No third-party validation of legal allocation authority or tax jurisdiction',
           'No calibrated crop or production coefficients',
           'No independent solver comparison',
           'Views are source-exclusive aggregate accounting, not autonomous monthly simulation',
           'R4 footprints are hand-declared subsets rather than comprehensive owner-qualified interface proofs'
       ]}
    path=Path(__file__).resolve().parent.parent/'results/round4_selective_world_fixture.json'
    path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
