"""Synthetic integrated physical-loss + selective activity + combat-view fixture."""
import json
from pathlib import Path
from irgs_reference import digest
from test_economic_integration import fresh
from r5_hazards import R5World
from r5_scale import MilitaryProjection
from r5_audit import independent_audit


def main():
    s=fresh().s
    s['actors']['caregiver-1']['ammo']=3
    s['actors']['person-B']['ammo']=2
    w=R5World(initial=s)
    opening={'population':w.display_population()['total'], 'cash':sum(w.s['cash'].values()),
        'kits':sum(v.get('kit',0) for v in w.s['equipment'].values()),
        'seed':w.s['econ3']['stocks']['farm']['seed'],'ammo':{'caregiver-1':3,'person-B':2}}
    w.apply('farm-start',8,'start_job',job_id='farm',recipe_id='grow',start=8,end=12,workers=['farmer-a'])
    w.apply('kitchen-start',8,'start_job',job_id='cook',recipe_id='cook',start=8,end=12,workers=['person-B'])
    w.schedule('warehouse-fire',9,'physical_loss',location='farm',material='seed',quantity=9,
               cause_ref='synthetic-fire-evidence',evidence_ref='synthetic-inventory-count')
    w.schedule('army-grant',9,'transfer_cash',**{'from':'treasury','to':'army','amount':400})
    w.schedule('care-grant',9,'transfer_cash',**{'from':'treasury','to':'caregiver-1','amount':400})
    w.schedule('farm-dispatch',9,'dispatch_stock',shipment_id='D',quantity=4,material='seed',
               **{'from':'farm','to':'house-1'},route_ref='synthetic-road',minimum_transit=1)
    w.schedule('tax-assessment',9,'assess_tax',tax_id='T',payer='farmer-b',amount=4,
               authority_ref='synthetic-legal-provision',basis_ref='synthetic-lot')
    at9=w.run_until(9)
    assert set(at9['committed'])=={'warehouse-fire','tax-assessment'},at9
    assert len(at9['deferred'])==2,at9
    w.schedule('farm-end-attempt',12,'complete_job',job_id='farm')
    w.schedule('kitchen-end',12,'complete_job',job_id='cook')
    at12=w.run_until(12)
    assert at12['committed']==['kitchen-end'],at12
    assert w.s['econ3']['produced']['meal']==12
    assert w.s['econ3']['produced']['grain']==0
    w.apply('tactical-13',13,'simultaneous_exchange',engagement_id='SIM-1',selected_effect_adapter='fixture_effects_only',attacks=[
        {'from':'caregiver-1','to':'person-B','ammo_used':2,'effect':'disable'},
        {'from':'person-B','to':'caregiver-1','ammo_used':1,'effect':'none'}])
    w.apply('brief-14',14,'summarize_engagement',engagement_id='SIM-1')
    w.apply('report-15',15,'report',person='caregiver-1',recipient='command',message='synthetic exchange reported')
    before_views=w.checksum()
    local=MilitaryProjection(w).view(actors=['person-B'],through=15)
    strategic=MilitaryProjection(w).view(actors=['caregiver-1','person-B'],through=15)
    residual=MilitaryProjection(w).residual_population_view(excluded_named_actors=['person-B','caregiver-1'])
    assert local['actor_disablement_count_now']==strategic['actor_disablement_count_now']==1
    assert w.checksum()==before_views
    audit=independent_audit(w.s,initial_ammo=opening['ammo'])
    loaded=R5World.load(w.save())
    assert loaded.checksum()==w.checksum()
    result={'candidate':'IRGS-CORE-3.3-CANDIDATE-R5','status':'synthetic partial execution only; not selected/accepted/calibrated/playtested',
        'opening':opening,'hazard_frontier_at_9':{'committed':at9['committed'],'deferred_groups':at9['deferred'],
            'seed_remaining':w.s['econ3']['stocks']['farm']['seed'], 'seed_lost':w.s['econ3']['losses']['seed'],
            'farm_shortfall':w.s['r5_shortfalls']['farm'], 'tax_paid':w.s['econ3']['tax_claims']['T']['paid']},
        'work_at_12':{'committed':at12['committed'],'unexecuted':at12['deferred'],
            'meals_produced':w.s['econ3']['produced']['meal'],'grain_produced':w.s['econ3']['produced']['grain'],
            'seed_consumed':w.s['econ3']['consumed']['seed']},
        'tactical_strategic':{'local':local,'strategic':strategic,'residual':residual,
            'view_read_only':w.checksum()==before_views},
        'independent_invariant_audit':audit,'closing':{'population':w.display_population()['total'],
            'cash':sum(w.s['cash'].values()),'kits':sum(v.get('kit',0) for v in w.s['equipment'].values()),
            'checksum_same_implementation_save_load':w.checksum()},
        'gaps':['No real authority authentication for disputed funds or taxes',
            'Undetermined causality of same-instant loss and stock shipment remains deferred',
            'Loss-suspended jobs need qualified partial-progress/settlement and reactivation procedures',
            'No transit loss model, repair or replacement process, or quantitative fire physics',
            'No independently coded simulator or cohort aggregation solver',
            'Fixed disable effects are fixture outcomes, not calibrated injury/combat models']}
    outfile=Path(__file__).resolve().parent.parent/'results/round5_loss_and_scale_fixture.json'
    outfile.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
