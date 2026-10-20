"""Integration check against isolated test server on 8764, never the live save."""
import json,re,urllib.request,urllib.error
from pathlib import Path
base='http://127.0.0.1:8764'
def get(path):
    with urllib.request.urlopen(base+path,timeout=10) as r:return r.read()
health=json.loads(get('/health'));assert health['core']=='3.3'
html=get('/').decode();token=re.search("const token='([^']+)'",html).group(1)
old=json.loads(get('/api/state'));assert len(old['state']['actors'])==37
payload={'expected_checksum':old['checksum'],'events':[{'id':'http-smoke','at':old['state']['clock']+1,'op':'ast_record_evidence','params':{'campaign_id':'AST','source_ref':'HTTP smoke test ONLY','subject':'AST-08','evidence_id':'smoke','assertion':'Synthetic API probe, not campaign truth','status':'testimony'}}]}
def post(token_value):
    req=urllib.request.Request(base+'/api/events',json.dumps(payload).encode(),{'Content-Type':'application/json','X-AST-Token':token_value})
    try:
        with urllib.request.urlopen(req,timeout=10) as r:return r.status,json.load(r)
    except urllib.error.HTTPError as e:return e.code,json.load(e)
assert post('bad')[0]==403
assert post(token)[0]==200
assert post(token)[0]==409
new=json.loads(get('/api/state'));assert len(new['state']['journal'])==1
assert new['state']['knowledge']=={}
assert new['state']['actors']['AST-04']['name']=='Abel'
p=Path(__file__).resolve().parent/'results/http_smoke_verification.json'
p.write_text(json.dumps({'health':'PASS','registry':'PASS','csrf_rejection':'PASS','atomic_write':'PASS','stale_state_rejection':'PASS','knowledge_not_omniscient':'PASS','scope':'isolated test state only'},indent=2)+'\n')
print(p.read_text())
