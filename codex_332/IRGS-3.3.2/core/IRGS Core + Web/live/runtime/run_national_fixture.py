import json, pathlib
from irgs_reference import initial_world, World
from test_unification import prepare_mobilization

ROOT=pathlib.Path(__file__).resolve().parents[1]
w=initial_world(); ids=prepare_mobilization(w)
w.apply('M7',7,'transfer_cash',**{'from':'treasury','to':'army','amount':400})
w.apply('M8',8,'accrue_pay',person='caregiver-1',amount=50)
w.apply('M9',9,'pay',person='caregiver-1',amount=20,**{'from':'army'})
w.run_until(10)
ready_at_duty=w.ready_subset(9,10)
ready_after_duty=w.ready_subset(13,14)
loaded=World.load(w.save())
replayed=initial_world()
for e in w.s['journal']:
    replayed.apply(e['id'],e['at'],e['op'],**e['params'])
assert loaded.checksum()==replayed.checksum()==w.checksum()
summary={
    'fixture_id':'NAT-MOB-01','status':'executed bounded fixture only',
    'authority':'IRGS-CORE-3.3-CANDIDATE-R1, not selected',
    'population':w.display_population(),
    'target':w.s['gov']['mobilization']['target'],
    'actual_enrolled':len(w.s['formations']['army']['members']),
    'target_shortfall':w.s['gov']['mobilization']['target']-len(w.s['formations']['army']['members']),
    'documented_training_qualifications':sum(bool(w.s['actors'][p]['training_evidence']) for p in ids),
    'issued_equipment_kit_count':sum(w.s['equipment'].get(p,{}).get('kit',0) for p in ids),
    'depot_kit_balance':w.s['equipment']['depot']['kit'],
    'compatible_training_equipment_availability_at_9_10':len(ready_at_duty),
    'compatible_training_equipment_availability_at_13_14':len(ready_after_duty),
    'note':'subset gate, not tactical readiness or proven combat competence',
    'budget_authorized':w.s['budgets']['military-outlay']['authorized'],
    'cash_balances':{k:w.s['cash'][k] for k in ['treasury','army','caregiver-1']},
    'wage_owed_caregiver':w.s['wage_due']['caregiver-1'],
    'equipment_total_check':sum(loc.get('kit',0) for loc in w.s['equipment'].values()),
    'cash_total_check':sum(w.s['cash'].values()),
    'event_count':len(w.s['journal']),
    'post_save_checksum':loaded.checksum(),
    'independent_same_implementation_replay_match':replayed.checksum()==w.checksum(),
    'limitations':['eligible_attestation externally supplied not independently checked',
        'training completion attested not calculated', 'no production losses or population vital events',
        'no tactical, medical, economic, transport, or social calibration'],
}
(ROOT/'fixtures'/'national_mobilization_scenario.json').write_text(json.dumps({
 'input_source':'synthetic fixture only','population_initial':1200,
 'residual_initial':1198,'named_initial':['caregiver-1','person-B'],
 'population_source_cohort':'region-residents-01',
 'recruit_target':1000,'actual_enrollments':600,'training_attested':450,'kits_issued':300,
 'available_kits_initial':300,'household_care_shift':[8,12],
 'budget_authorized':800,'treasury_initial':1000,'cash_transfer':400,
 'wage_accrued':50,'wage_paid':20,'time_unit':'abstract fixture steps; 8–12 same local clock for care and assessment'},indent=2)+'\n')
(ROOT/'results'/'national_mobilization_result.json').write_text(json.dumps(summary,indent=2)+'\n')
(ROOT/'results'/'national_mobilization_events.json').write_text(json.dumps(w.s['journal'],indent=2)+'\n')
(ROOT/'results'/'national_mobilization_checkpoint.json').write_text(json.dumps(w.s,indent=2)+'\n')
print(json.dumps(summary,indent=2))
