"""Reproduce execution-derived operation inventory and multi-month fixtures."""
import copy
import io
import json
import unittest
from pathlib import Path
from irgs_reference import World, initial_world
from r7_frontier import R7World
from r8_dependencies import observe, SUPPORTED, code_identity
from r8_strategy import strategic_world, advance
from economic_extension import total

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT/'results'

def write(name, data):
    (RESULTS/name).write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')

def inventory():
    seen = {}; failures = {}; busy = False
    original = World.apply
    def audited(self, eid, at, op, **params):
        nonlocal busy
        before = copy.deepcopy(self.s) if not busy and op in SUPPORTED else None
        result = original(self, eid, at, op, **params)
        if before is not None and result:
            busy = True
            try:
                state = (R7World if 'econ3' in before else World)(state=before).s
                c = observe(state, {'id':eid,'at':at,'op':op,'params':params})
                entry = seen.setdefault(op, {'executions':0,'reads':set(),'writes':set(),'example':c})
                entry['executions'] += 1
                entry['reads'].update(c['reads']); entry['writes'].update(c['writes'])
            except Exception as error:
                failures.setdefault(op,set()).add(type(error).__name__+': '+str(error))
            finally: busy = False
        return result
    suite = unittest.TestSuite()
    for path in sorted(Path(__file__).parent.glob('test_*.py')):
        if path.name.startswith('test_r8'): continue
        suite.addTests(unittest.defaultTestLoader.loadTestsFromName(path.stem))
    World.apply = audited
    output = io.StringIO()
    try:
        result = unittest.TextTestRunner(stream=output, verbosity=1).run(suite)
        # Explicit missing shared branches; these do not impersonate native engines.
        extra = initial_world()
        extra.apply('capture', 1, 'capture', person='person-B', by='fixture', location='camp')
        extra.apply('escape', 2, 'escape', person='person-B', location='home')
        extra.apply('order', 3, 'issue_order', order_id='o', recipient='person-B', deadline=6)
        extra.apply('receive', 4, 'receive_order', order_id='o')
        extra.apply('execute', 5, 'execute_order', order_id='o')
        assert extra.s['actors']['person-B']['custody'] is None
        assert extra.s['orders']['o']['executed']
    finally: World.apply = original
    (RESULTS/'r8_instrumented_inherited_tests.txt').write_text(output.getvalue(),encoding='utf-8')
    if not result.wasSuccessful(): raise RuntimeError(output.getvalue())
    rows=[]
    for op in sorted(SUPPORTED):
        entry=seen.get(op,{})
        rows.append({'operation':op,'status':'observed_in_executed_cases' if entry else 'UNEXERCISED_HOLD',
                     'executions':entry.get('executions',0), 'reads_union':sorted(entry.get('reads',[])),
                     'writes_union':sorted(entry.get('writes',[])), 'example':entry.get('example'),
                     'refused_observations':sorted(failures.get(op,[]))})
    write('r8_operation_inventory.json', {'scope':'Shared World/economic handlers only; unions are evidence, never scheduler contracts',
          'code_hash':code_identity(),'inherited_tests':result.testsRun,'operations':rows})
    return {'eligible':len(SUPPORTED),'observed':len(seen),'inherited_tests':result.testsRun}

def strategy():
    # Run uninterrupted and save/reload midway, including an exhausted-resource run.
    full=advance(strategic_world(),90*6)
    split=advance(strategic_world(),45*6)
    split=advance(R7World.load(split.save()),90*6)
    assert full.checksum()==split.checksum()
    scarce=advance(strategic_world(grain=4,fuel=2),10*6)
    e=full.s['econ3']
    assert e['produced']['meal']==270 and e['consumed']['meal']==270
    assert total(e,'grain')==60 and total(e,'fuel')==30
    assert full.s['cash']['treasury']==626 and full.s['wage_due']['person-B']==90
    assert sum(full.s['cash'].values())==1000
    assert full.display_population()['total']==1200
    assert scarce.s['econ3']['produced']['meal']==6
    result={'status':'PROPOSED synthetic policy execution; no native engine certification',
            'days':90,'review_ticks':540,'save_resume_equal':True,'checksum':full.checksum(),
            'meals_produced':270,'meals_delivered':e['meals_delivered']['house-1'],
            'grain_remaining':total(e,'grain'),'fuel_remaining':total(e,'fuel'),
            'tax_paid':26,'wages_due_not_paid':90,'population':1200,'cash_total':1000,
            'army_members':full.s['formations']['army']['members'],
            'issued_kits':full.s['equipment']['farmer-a']['kit'],
            'committed_operations':sum(len(d['committed']) for d in full.s['r8_strategy']['decisions']),
            'deferred_proposals':sum(len(d['deferred']) for d in full.s['r8_strategy']['decisions']),
            'scarce_10_day_run':{'completed_jobs':len(scarce.s['econ3']['completed_jobs']),
                               'meals_produced':scarce.s['econ3']['produced']['meal'],
                               'unmet_selected_meal_target':30-scarce.s['econ3']['meals_delivered']['house-1']}}
    write('r8_strategy_summary.json',result)
    write('r8_strategy_final_state.json',full.s)
    return result

if __name__=='__main__':
    print(json.dumps(inventory()),flush=True)
    print(json.dumps(strategy()),flush=True)
