"""Execute five synthetic national microeconomy variants and write reproducible evidence."""
from __future__ import annotations
import json
from pathlib import Path
from irgs_reference import World
from test_economic_integration import run_day

MODES=('civilian','farmer_mobilized','caregiver_mobilized','uncovered','dual_mobilized')

def main():
    outputs={}
    for name in MODES:
        w=run_day(name)
        e=w.s['econ3']; audit=e['needs_audit'][0]
        redo=World.load(w.save())
        assert redo.checksum()==w.checksum()
        outputs[name]={
          'population_total':w.display_population()['total'],
          'army_enrollees':len(w.s['formations']['army']['members']),
          'grain_produced_units':e['produced']['grain'],
          'meal_produced_units':e['produced']['meal'],
          'meals_served_units':audit['meals_served'],
          'unmet_meals_units':audit['unmet_meals'],
          'actual_care_hours':audit['actual_care_hours'],
          'unmet_care_hours':audit['unmet_care_hours'],
          'physical_seed_remaining':sum(q.get('seed',0) for q in e['stocks'].values()),
          'seed_consumed':e['consumed']['seed'],
          'cash_total':sum(w.s['cash'].values()),
          'journal_length':len(w.s['journal']),
          'state_sha256':w.checksum(),
          'serialization_replays_identically_same_implementation':True
        }
    civilian=outputs['civilian']
    for name,v in outputs.items():
        assert v['population_total']==1200 and v['cash_total']==1000
        assert v['physical_seed_remaining'] + v['seed_consumed']==12
    assert civilian['grain_produced_units']==24
    assert outputs['farmer_mobilized']['grain_produced_units']==12
    assert outputs['caregiver_mobilized']['meal_produced_units']==0
    assert outputs['caregiver_mobilized']['unmet_care_hours']==0
    assert outputs['uncovered']['unmet_care_hours']==4
    assert outputs['dual_mobilized']['grain_produced_units']==12
    result={'candidate':'IRGS-CORE-3.3-CANDIDATE-R3','simulation_type':'synthetic discrete integer reference fixture',
        'time_unit':'synthetic time steps: 8–12 four units of possible work',
        'products':'seed, grain and meal are illustrative integer stock units; no real yield or nutrition calibration',
        'baseline_population':1200,'baseline_actual_cash_units':1000,
        'purpose':'Demonstrate shared civilian/military labor constraints, stock conservation, care allocation and income separation',
        'cases':outputs,
        'interpretation':'These are executed same-code bounded fixtures, not national-economy calibration, policy forecasts, independent implementation agreement or playtest.'}
    target=Path(__file__).resolve().parent.parent/'results/economic_mobilization_comparison.json'
    target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
