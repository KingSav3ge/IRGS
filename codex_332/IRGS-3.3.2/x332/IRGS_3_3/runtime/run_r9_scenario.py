import json
from pathlib import Path
from r9_strategy import strategic_world,advance
from r7_frontier import R7World
from test_r9_runtime import receiver,military,roman,money
from r9_runtime import frontier,grant,resolve
ROOT=Path(__file__).resolve().parent.parent
def run():
    full=strategic_world()
    for day in (7,14):
        advance(full,day*6);print('Continuous strategic day',day,flush=True)
    split=advance(strategic_world(),7*6)
    split=advance(R7World.load(split.save()),14*6)
    assert full.checksum()==split.checksum()
    assert full.s['econ3']['produced']['meal']==42
    assert full.s['econ3']['meals_delivered']['house-1']==42
    native=receiver();frontier(native,[military(),roman()])
    # If structural reads conservatively couple these, test separately against
    # the same initial source. No claim of blanket native independence.
    independent=receiver();frontier(independent,[military()])
    assert independent.s['equipment']['farmer-a']['kit']==1
    decision=receiver();grant(decision,'cash','treasurer',['transfer_cash'],3,'fixture-law')
    frontier(decision,[money('one'),money('two')]);decision=type(decision).load(decision.save())
    resolve(decision,'approve-one','one',9,'cash','treasurer',True)
    resolve(decision,'deny-two','two',10,'cash','treasurer',False)
    assert decision.s['cash']['army']==80
    result={'days':14,'meals_produced':42,'meals_consumed':42,'save_resume_identical':True,
            'checksum':full.checksum(),'cash_total':sum(full.s['cash'].values()),
            'population':full.display_population()['total'],
            'committed_operations':sum(len(d['committed']) for d in full.s['r8_strategy']['decisions']),
            'unresolved':sum(x['status']=='unresolved' for x in full.s['r9']['requests'].values()),
            'durable_decisions':{k:v['status'] for k,v in decision.s['r9']['requests'].items()},
            'scope':'Synthetic profile only; no AST Day 3 advancement'}
    for name,value in [('r9_scenario_summary.json',result),('r9_synthetic_final_state.json',full.s),('r9_resolved_example.json',decision.s)]:
        (ROOT/'results'/name).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result),flush=True)
if __name__=='__main__':run()
