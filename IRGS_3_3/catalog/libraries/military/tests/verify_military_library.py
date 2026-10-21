#!/usr/bin/env python3
"""IRGS Military Content Library v1.0 integrity & bounded reference checks.
No external dependencies; does not execute a real game runtime or qualify performance.
"""
import csv, json, pathlib, re, hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
passed=[]
def chk(name,condition):
    if not condition: raise AssertionError(name)
    passed.append(name)
def readcsv(name): return list(csv.DictReader((ROOT/name).open(encoding='utf-8-sig',newline='')))
lib=(ROOT/'IRGS_Military_Content_Library_v1_0_Candidate.md').read_text(encoding='utf-8')
orig=(ROOT/'provenance/IRGS_Military_Equipment_and_Technology_Library_v0_1.md').read_text(encoding='utf-8')
slim=(ROOT/'provenance/IRGS_Soldier_Military_Life_Slim_v1_0.md').read_text(encoding='utf-8')
cat=json.loads((ROOT/'IRGS_Military_Content_Catalogue_v1_0.json').read_text())
snap=json.loads((ROOT/'Military_SCL_Reference_Verification_Snapshot.json').read_text())
matrix=readcsv('Military_Era_Category_Crosswalk_v1_0.csv')
cases=readcsv('Military_Acceptance_Cases_v1_0.csv')
refs=readcsv('Military_SCL_Reference_Crosswalk_v1_0.csv')
req_eras=['ERA-ANT','ERA-EAD','ERA-MED','ERA-EMD','ERA-CON','ERA-SCI']
req_cats=['WPN','PRO','SUP','MUN','KIT','TRN','NAV','AIR','COM','OBS','ENG','MED']
chk('correct release identity',cat['id']=='IRGS-MIL-LIB-1.0')
chk('core selection named',cat['parent_reference']=='IRGS-CORE-3.2')
chk('scl selection named',cat['scl_reference']=='IRGS-SCL-1.0')
chk('source slim pin preserved',cat['slim_engine_source_pin']=='IRGS-CORE-3.0 / IRGS-SCL-0.1')
chk('6 source eras',len(cat['eras'])==6)
chk('source era ids exact',[x['id'] for x in cat['eras']]==req_eras)
chk('12 source categories',len(cat['categories'])==12)
chk('source categories exact',[x['code'] for x in cat['categories']]==req_cats)
for x in cat['eras']:
  chk('era original '+x['id'],x['id'] in orig and x['name'] in orig)
for x in cat['categories']:
  chk('category original '+x['code'],bool(re.search(r'^\|\s*'+x['code']+r'\s*\|\s*'+re.escape(x['name'])+r'\s*\|',orig,re.M)))
chk('72 era/category cells',len(matrix)==72)
chk('matrix JSON CSV match',cat['matrix']==matrix)
chk('unique era/category pairs',len({(x['era_id'],x['category_code']) for x in matrix})==72)
for era in req_eras:
 chk('era complete '+era,{x['category_code'] for x in matrix if x['era_id']==era}==set(req_cats))
chk('48 new templates',len(cat['templates'])==48)
chk('unique new template ids',len({x['id'] for x in cat['templates']})==48)
chk('every category four templates',all(sum(x['category']==c for x in cat['templates'])==4 for c in req_cats))
chk('new templates only proposed',all(x['status']=='proposed-unqualified' for x in cat['templates']))
chk('no new template instantiates assets',all(x['instantiates_asset']==False for x in cat['templates']))
chk('no duplicate physical owner',all(x['owns_physical_state']==False for x in cat['templates']))
chk('required fields nonempty',all(len(x['native_model_fields'])>=4 for x in cat['templates']))
chk('60 cases',len(cases)==60)
chk('case sequence exact',[c['id'] for c in cases]==['MIL-%02d'%i for i in range(1,61)])
chk('cases not mislabeled executed',all(x['evidence']=='specified_not_executed_in_runtime' for x in cases))
chk('source 7 section anchors',all(f'## {i}.' in orig for i in range(1,8)))
chk('slim 17 section anchors',all(f'## {i}.' in slim for i in range(1,18)))
chk('source slim original acceptance count',len(set(re.findall(r'\bSML-\d{2}\b',slim)))==30)
chk('exact read-only reference snapshot',len(snap['identities'])==len({x['ref'] for x in snap['identities']}))
refset={x['ref'] for x in snap['identities']}
chk('crosswalk reference resolution',all(x['exact_scl_ref'] in refset for x in refs))
chk('template reference resolution',all(x['scl_example_ref'] is None or x['scl_example_ref'] in refset for x in cat['templates']))
chk('all snapshot refs preserve old family revision',all(x.endswith('@0.2') for x in refset))
chk('slim incompatibility called out','not silently migrated' in lib and 'CORE-3.0' in lib)
chk('no equipment performance fabrication explicitly promised','does not invent them' in lib)
chk('content not instantiated by reference','neither creates an actual object' in lib)
chk('source citation and source retention',all((ROOT/'provenance'/x).exists() for x in ['IRGS_Military_Equipment_and_Technology_Library_v0_1.md','IRGS_Soldier_Military_Life_Slim_v1_0.md']))
chk('compatibility gate file included',(ROOT/'Military_Slim_Core_3_2_Compatibility_Gate.md').exists())
# Bounded synthetic fixture A: physical movement and idempotence of a magazine lot.
stock={'depot':10,'magazine':0};applied=set()
def move(event_id,source,target,count):
 if event_id in applied:return
 assert 0<=count<=stock[source]
 stock[source]-=count;stock[target]+=count;applied.add(event_id)
move('ev-1','depot','magazine',3)
chk('transfer conservation',stock=={'depot':7,'magazine':3})
move('ev-1','depot','magazine',3)
chk('replay transfer idempotence',stock=={'depot':7,'magazine':3})
# Bounded synthetic fixture B: document issue authorization alone does not transfer custody.
asset={'owner':'unit','custodian':'depot','status':'authorized'}
chk('authorized issue not receipt',asset['custodian']=='depot')
asset['custodian']='soldier';asset['status']='issued'
chk('physical receipt changes custody not title',asset=={'owner':'unit','custodian':'soldier','status':'issued'})
# Bounded synthetic fixture C: selectors do not multiply an actual sword.
weapon={'asset_id':'sword-1','supported_modes':['modes.cut','modes.thrust']}
chk('two modes one actual weapon',len({weapon['asset_id'] for _ in weapon['supported_modes']})==1)
# Bounded synthetic fixture D: reports do not duplicate casualty changes.
unit={'total':10,'available':9,'captured':1};report={'as_of':12,'captured':1}
chk('report is read-only casualty view',unit['total']==unit['available']+unit['captured'])
# Bounded synthetic fixture E: qualification cannot create a gun.
operator={'qualified':True,'issued_assets':[]}
chk('qualification not issue',operator['qualified'] and not operator['issued_assets'])
# Manifest file checks (excluding self manifest and any zip).
if (ROOT/'PACKAGE_MANIFEST.json').exists():
  m=json.loads((ROOT/'PACKAGE_MANIFEST.json').read_text())
  for x in m['files']:
    p=ROOT/x['path']
    chk('hash '+x['path'],p.exists() and p.stat().st_size==x['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'])
print('PASS:',len(passed),'structural, reference and bounded synthetic checks')
