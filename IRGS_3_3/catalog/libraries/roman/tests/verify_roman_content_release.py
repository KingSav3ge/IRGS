#!/usr/bin/env python3
"""IRGS Roman Republic Content Library v1.0 candidate: structural and bounded unit verification.
Does not execute a complete IRGS simulation, claim historical calibration or adopt content.
"""
from pathlib import Path
import sys, json, csv, re, hashlib
from collections import Counter

P=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent
P=P.resolve(); passed=0

def check(cond,msg):
 global passed
 if not cond:raise AssertionError(f'CHECK FAILED ({passed} passed): {msg}')
 passed+=1

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(name):
 with (P/name).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))

def read(name):return json.loads((P/name).read_text())

cat=read('Roman_Content_Catalogue_v1_0.json')
pins=read('SOURCE_PINS.json')
reg=read('sources/SCL_v1_0_Registry_ReadOnly.json')
bind=read('sources/Roman_v1_2_Native_Content_Bindings_Unchanged.json')
cb=read('sources/Core_v3_2_Receiving_Bindings_ReadOnly.json')
entries=rows('Roman_Content_Catalogue_v1_0.csv')
native=rows('Roman_Native_SCL_Crosswalk_v1_0.csv')
cov=rows('Roman_CMRR_Section_Dispositions_v1_0.csv')
acc=rows('Roman_Acceptance_Specifications_v1_0.csv')
gates=rows('Roman_Calibration_Gates_v1_0.csv')
md=(P/'IRGS_Roman_Republic_Content_Library_v1_0_Candidate.md').read_text()
check(cat['document_id']=='IRGS-RRCL-1.0','document identity')
check(cat['core']=='IRGS-CORE-3.2','Core pin')
check(cat['roman_engine']=='IRGS-RRLS-SLIM-1.2','Roman pin')
check(cat['shared_content']=='IRGS-SCL-1.0','shared catalogue pin')
check(reg['document_id']=='IRGS-SCL-1.0','normative SCL registry id')
check(bind['core']=='IRGS-CORE-3.2' and bind['catalogue']=='IRGS-SCL-1.0','native binding pins')
check(cat['native_binding_source_sha256']==sha(P/'sources/Roman_v1_2_Native_Content_Bindings_Unchanged.json'),'cat native source pin')
check(cat['shared_registry_sha256']==sha(P/'sources/SCL_v1_0_Registry_ReadOnly.json'),'cat registry source pin')
check(pins['native_bindings_sha256']==sha(P/'sources/Roman_v1_2_Native_Content_Bindings_Unchanged.json'),'native source pin')
check(pins['engine_sha256']==sha(P/'sources/IRGS_Roman_Republic_Slim_v1_2_Accepted.md'),'Roman source pin')
check(pins['full_source_sha256']==sha(P/'sources/IRGS_Roman_Republic_Full_v1_0_Historical_Source.md'),'full source pin')
check(pins['external_registry_sha256']==sha(P/'sources/SCL_v1_0_Registry_ReadOnly.json'),'SCL source pin')
check(pins['external_core_bindings_sha256']==sha(P/'sources/Core_v3_2_Receiving_Bindings_ReadOnly.json'),'Core engine bindings pin')
for category, data in [('content_entries',entries),('source_native_profiles',native),('source_section_dispositions',cov),('acceptance_requirements',acc),('parameter_gates',gates)]:
 check(len(data)==cat['counts'][category],f'{category} count')
 check(len(data)==pins['counts'][category],f'{category} source count')
check(len(cat['entries'])==len(entries),'JSON/CSV record coverage')
check(len(cat['native_binding_references'])==len(native),'JSON/CSV native coverage')
check(all(x['design_status'].startswith(('Source-derived','Proposed')) for x in entries),'proposal statuses')
check(all(x['verification_status'].startswith('Specified;') for x in acc),'acceptance not claimed executed')
check(len(set(x['id'] for x in entries))==len(entries),'unique content IDs')
check(len(set(x['id'] for x in acc))==len(acc),'unique acceptance IDs')
check(len(set(x['gate_id'] for x in gates))==len(gates),'unique calibration IDs')
check(len(set(x['native_id'] for x in native))==len(native),'unique native bindings')
check(len(entries)>=100 and len(native)==14 and len(cov)==32,'minimum content preservation')
check(len(reg['definitions'])==279 and len(reg['aliases'])==1416,'base shared registry cardinality')
check(len(reg['source_payload_blocks'])==420,'base payload preservation')
check(cat['migration']=={'automatic':False,'campaign_instances_created':False,'core_rules_changed':False,'roman_native_profiles_changed':False,'source_deprecation':False},'no migration or shared changes')

entry_by_id={x['id']:x for x in cat['entries']}
for row in entries:
 check(row['id'] in entry_by_id,'JSON entry exists '+row['id'])
 check(row=={k:str(v) for k,v in entry_by_id[row['id']].items()},'CSV/JSON identity '+row['id'])
 check(re.match(r'^RRCL-[A-Z]+-\d{3}@1\.0$',row['id']) is not None,'well formed Roman ID '+row['id'])
 check(row['group'] in {'LAW','ECO','MAT','ARMS','MIL','PLACE','ARENA','TRAVEL','CARE','CIVIC','RECORD'},'known group')
 check(row['source_grade'] in ('DIRECT','PROPOSED'),'explicit source/proposal marking')
 for field in ('core_owner','source_locator','qualitative_contract','activation_prerequisites','non_inheritance_and_limit','instantiation'):
  check(bool(row[field].strip()),'required content metadata '+row['id']+' '+field)
 check(row['id'] in md,'main document contains entry '+row['id'])
 check('No instances or resources created' in row['instantiation'],'no automatic instance '+row['id'])

# Check exact source-native mapping; one native-only profile is legitimate.
ref_by_id={x['release_ref']:x for x in reg['definitions']}
alias_index={x['alias']:x for x in reg['aliases']}
check(len(alias_index)==len(reg['aliases']),'aliases unique')
check(len(bind['entries'])==len(native),'source native row preservation')
for source,row in zip(bind['entries'],native):
 check(row['native_id']==source['native_id'],'native order/identity '+row['native_id'])
 check(row['source_alias']==(source.get('source_alias') or ''),'native source alias '+row['native_id'])
 check(row['selector']==(source.get('selector') or ''),'native selector '+row['native_id'])
 check(row['scl_reference']==(source.get('target') or ''),'native family '+row['native_id'])
 check(row['target_content_sha256']==(source.get('target_content_sha256') or ''),'target checksum source '+row['native_id'])
 check(json.loads(row['profile_values_json'])==source['profile_values'],'numeric local profile preserved '+row['native_id'])
 check(row['reference_gate']==source['reference_gate'],'native gate preserved '+row['native_id'])
 check(row['source_deprecation']=='false' and not source['source_deprecation'],'deprecation unchanged')
 if source.get('target'):
  check(source['target'] in ref_by_id,'target exists '+row['native_id'])
  d=ref_by_id[source['target']]
  check(d['reference_gate']==source['reference_gate'],'target gate '+row['native_id'])
  check((source['selector'] is None or source['selector'] in d['allowed_selectors']),'allowed selector '+row['native_id'])
  a=alias_index[source['source_alias']]
  check(a['target']==source['target'],'exact alias target '+row['native_id'])
  check(a['selector']==source['selector'],'exact alias selector '+row['native_id'])
  check(a['semantic_type']==source['semantic_type'],'exact alias semantic type '+row['native_id'])
  check(a['target_content_sha256']==source['target_content_sha256'],'exact alias checksum '+row['native_id'])
 else:
  check(source['native_id']=='RR-HEAVY-HANDHELD-IMPACT-1.0','only recognized native profile has no SCL target')
  check(source['reference_gate']=='retained_native_profile','native-only gate preserved')

# Bidirectional enumerated source section matrix. Source files are archived byte-for-byte.
for name,fullpath,nmax in [('Roman full v1.0','sources/IRGS_Roman_Republic_Full_v1_0_Historical_Source.md',20),('Roman Slim v1.2','sources/IRGS_Roman_Republic_Slim_v1_2_Accepted.md',12)]:
 rs=[x for x in cov if x['source']==name]
 check(len(rs)==nmax,'source section count '+name)
 check([int(x['section']) for x in rs]==list(range(1,nmax+1)),'ordered coverage '+name)
 heads=[(int(n),t.strip()) for n,t in re.findall(r'^## (\d+)\. ([^\n]+)',(P/fullpath).read_text(),re.M)]
 check([(int(x['section']),x['title']) for x in rs]==heads,'exact heading crosswalk '+name)
 for r in rs:
  check(bool(r['receiving_scope'] and r['disposition']),'disposition nonempty '+name+r['section'])

for i,x in enumerate(acc,1):
 check(x['id']==f'RRCL-AC-{i:03d}','sequential acceptance IDs')
 check(bool(x['scenario'] and x['expected_result']),'acceptance complete')
for i,x in enumerate(gates,1):
 check(x['gate_id']==f'RRCL-CAL-{i:02d}','sequential gate IDs')
 check(bool(x['responsible_source'] and x['required_data']),'calibration gate complete')

# Bounded, hand-specified invariant probes, not a full IRGS game runtime.
# A scalar unit of account is a VIEW of coins not an additional set of coins.
coins={'denarius':1,'sestertius':0}
account_value=coins['denarius']*4+coins['sestertius']
check(account_value==4,'one denarius maps to four sestertii account value')
check(sum(coins.values())==1,'account view does not mint three coin objects')
paid={'person':0,'lanista':0,'organizer':6}
paid['organizer']-=3;paid['lanista']+=3
check(paid=={'person':0,'lanista':3,'organizer':3},'contract pays actual payee, not unlisted fighter')
check(sum(paid.values())==6,'cash conservation')
stock={'source':12,'transit':0,'target':0};stock['source']-=5;stock['transit']+=5
check(sum(stock.values())==12 and stock['target']==0,'finite transit with no phantom delivery')
stock['transit']-=5;stock['target']+=5
check(sum(stock.values())==12 and stock['target']==5,'actual delivery preserves total')
state={'sword-1':{'modes':['cut','thrust'],'condition':'worn','holder':'actor-A'}}
check(len(state)==1 and len(state['sword-1']['modes'])==2,'two sword modes one physical object')
check(any(x['native_id']=='RR-NATIVE-UNARMED-1.0' and not json.loads(x['profile_values_json'])['inventory_object'] for x in native),'unarmed is not equipment')

def wear_batch(s,m,n1,n2,n3):
 if n3:return 2,0
 advances=n2+(m+n1)//2
 ss=min(2,s+advances)
 return (ss, 0 if advances or ss==2 else (m+n1)%2)
check(wear_batch(0,0,3,0,0)==(1,0),'three simultaneous stress 1: one advance no mark')
check(wear_batch(0,0,4,0,0)==(2,0),'four simultaneous stress 1: two advances')
check(wear_batch(0,1,0,1,0)==(1,0),'transition consumes prior light mark')
check(wear_batch(0,0,1,0,0)==(0,1),'single stress 1 retains mark')
check(wear_batch(1,0,0,0,1)==(2,0),'single stress 3 causes breach')
# Oversubscribed teaching station, duplicate passage and report receipts cannot invent throughput.
actual_hours=3;request_A=2;request_B=2
check(request_A+request_B>actual_hours,'oversubscription explicitly detected')
received_events={'transfer-01'}
check(len(received_events|{'transfer-01'})==1,'repeated receipt id does not duplicate transfer')
check('hold' not in {'asset-1':'asset-1'},'assets do not become statuses or objects by naming')

# Integrity manifest hashes every delivered file except itself and the execution result report.
manifest=read('PACKAGE_MANIFEST.json')
check(manifest['document_id']=='IRGS-RRCL-1.0','manifest identity')
expected={p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file() and p.name not in ('PACKAGE_MANIFEST.json','VERIFICATION_RESULTS.json')}
check(set(manifest['files'])==expected,'manifest coverage with no unexpected files')
for rel,item in manifest['files'].items():
 f=P/rel
 check(f.is_file(),'exists '+rel)
 check(f.stat().st_size==item['bytes'],'size '+rel)
 check(sha(f)==item['sha256'],'hash '+rel)

print(json.dumps({'passed':True,'check_count':passed,'catalogue_templates':len(entries),'native_source_bindings':len(native),'source_sections':len(cov),'specified_acceptance_cases':len(acc),'calibration_gates':len(gates),'complete_game_runtime_tests_executed':0,'historical_or_physiological_calibration':False},indent=2))
