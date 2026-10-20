"""Read-only independent arithmetic/package checks, not a second simulator."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def read(name): return json.loads((ROOT/name).read_text(encoding='utf-8-sig'))

def verify():
    s=read('results/r8_strategy_final_state.json')
    e=s['econ3']; balances={}
    for mat,opening in e['opening'].items():
        physical=sum(location.get(mat,0) for location in e['stocks'].values())
        expected=opening+e['produced'][mat]-e['consumed'][mat]-e.get('losses',{}).get(mat,0)
        assert physical==expected,(mat,physical,expected)
        assert all(location.get(mat,0)>=0 for location in e['stocks'].values())
        balances[mat]=physical
    assert sum(s['cash'].values())==s['cash_baseline']==1000
    assert len(s['actors'])+s['population']['residual']==s['population']['baseline']==1200
    assert sum(location.get('kit',0) for location in s['equipment'].values())==s['kit_baseline']==300
    journal_ids=[r['id'] for r in s['journal']]
    assert len(journal_ids)==len(set(journal_ids))==len(s['processed'])
    assert set(journal_ids)==set(s['processed'])
    decisions=s['r8_strategy']['decisions']
    assert [d['tick'] for d in decisions]==list(range(540))
    assert len({d['code_hash'] for d in decisions})==1
    assert all(eid in s['processed'] for d in decisions for eid in d['committed'])
    assert s['econ3']['active_jobs']=={}
    assert read('IRGS_Core_v3_3_Candidate_Binding_Proposal_R8.json')['existing_core_ref']=='IRGS-CORE-3.2'
    assert all(row['native_dependency_certification']=='NOT CERTIFIED' for row in read('results/r8_cross_engine_gate_matrix.json'))
    for name,expected in read('results/file_sha256_manifest_R8.json').items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==expected,name
    print(json.dumps({'independent_arithmetic':'PASS','manifest':'PASS','native_status_honest':True,
                      'materials_remaining':balances,'journal_events':len(journal_ids)}))

if __name__=='__main__': verify()
