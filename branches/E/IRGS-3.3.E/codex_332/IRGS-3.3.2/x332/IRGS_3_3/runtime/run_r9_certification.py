"""Observed-case certification, never a claim that all branches are covered."""
import copy,io,json,unittest,sys
from pathlib import Path
from irgs_reference import World,initial_world
from r7_frontier import R7World
from r9_adapters import ReceiverWorld
from ast_runtime import ASTWorld
from r9_runtime import observe,SUPPORTED

ROOT=Path(__file__).resolve().parent.parent
INSTRUMENTATION_EXCLUDES={'test_strategy_rights.SustainedExecutionTests.test_default_fourteen_day_resources_and_decisions'}

def instrumented_suite():
    discovered=unittest.defaultTestLoader.discover(str(Path(__file__).parent),pattern='test_*.py')
    def cases(suite):
        for item in suite:
            if isinstance(item,unittest.TestSuite):yield from cases(item)
            elif item.id() not in INSTRUMENTATION_EXCLUDES:yield item
    return unittest.TestSuite(cases(discovered))
def run():
    rows={};errors={};depth=0;busy=False
    originals={cls:cls.__dict__['apply'] for cls in (World,R7World,ReceiverWorld,ASTWorld)}
    def wrap(original):
        def audited(self,eid,at,op,**p):
            nonlocal depth,busy
            frame=sys._getframe(1);probing=False
            while frame:
                if frame.f_code.co_name=='observe' and frame.f_globals.get('__name__') in ('r9_runtime','r8_dependencies'):
                    probing=True;break
                frame=frame.f_back
            top=depth==0 and not busy and not probing and op in SUPPORTED
            before=copy.deepcopy(self.s) if top else None
            depth+=1
            try:result=original(self,eid,at,op,**p)
            finally:depth-=1
            if top and result:
                busy=True
                try:
                    c=observe(before,{'id':eid,'at':at,'op':op,'params':p})
                    row=rows.setdefault(op,{'executions':0,'reads':set(),'writes':set(),'validation_reads':set(),'profiles':set(),'backends':set(),'example':c})
                    row['executions']+=1
                    row['profiles'].add(c.get('profile','legacy_research_fixture'));row['backends'].add(c.get('backend','unknown'))
                    for key in ('reads','writes','validation_reads'):row[key].update(c[key])
                except Exception as err:errors.setdefault(op,set()).add(type(err).__name__+': '+str(err))
                finally:busy=False
            return result
        return audited
    for cls,original in originals.items():cls.apply=wrap(original)
    log=io.StringIO()
    try:
        result=unittest.TextTestRunner(stream=log,verbosity=1).run(instrumented_suite())
        w=initial_world()
        w.apply('capture',1,'capture',person='person-B',by='fixture',location='camp')
        w.apply('escape',2,'escape',person='person-B',location='home')
        w.apply('order',3,'issue_order',order_id='o',recipient='person-B',deadline=6)
        w.apply('receive',4,'receive_order',order_id='o')
        w.apply('execute',5,'execute_order',order_id='o')
    finally:
        for cls,original in originals.items():cls.apply=original
    (ROOT/'results/r9_instrumented_tests.txt').write_text(log.getvalue(),encoding='utf-8')
    inventory=[]
    for op in sorted(SUPPORTED):
        row=rows.get(op,{})
        inventory.append({'operation':op,'status':'PASS_OBSERVED_CASES' if row and op not in errors else 'HOLD',
            'executions':row.get('executions',0),**{k:sorted(row.get(k,[])) for k in ('reads','writes','validation_reads','profiles','backends')},
            'example':row.get('example'),'refused_observations':sorted(errors.get(op,[])),
            'all_branches_certified':False})
    output={'test_count':result.testsRun,'tests_passed':result.wasSuccessful(),'operation_count':len(SUPPORTED),
            'instrumentation_excludes':sorted(INSTRUMENTATION_EXCLUDES),
            'observed_count':len(rows),'operations':inventory,
            'scope':'Exact checked code and executed cases; not arbitrary Python, all branches, or all native engine operations'}
    (ROOT/'results/r9_certification_matrix.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in output.items() if k!='operations'}))
    if not result.wasSuccessful():raise RuntimeError(log.getvalue())
if __name__=='__main__':run()
