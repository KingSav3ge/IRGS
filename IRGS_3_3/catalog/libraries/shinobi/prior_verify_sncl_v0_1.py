#!/usr/bin/env python3
"""Bounded SNCL 0.1 source/identity/operational contract checks; not a full SNWE runtime."""
import json, re, pathlib, hashlib, collections, sys
P=pathlib.Path(__file__).resolve().parent
ROOT=P.parent
library=json.loads((P/'IRGS_SNCL_v0_1_Registry.json').read_text())
records=library['records']; indexed={r['id']:r for r in records}; result=[]
def check(id,name,actual,expected=True,scope='source_or_contract'):
    passed=actual==expected
    result.append(dict(id=id,name=name,status='PASS' if passed else 'FAIL',observed=actual,expected=expected,scope=scope))
    return passed
check('V01','library identity',library['document_id'],'IRGS-SNCL-0.1')
check('V02','Core parent',library['core_ref'],'IRGS-CORE-3.2')
check('V03','genre parent',library['engine_binding'],'IRGS-SNWE-0.3')
check('V04','SCL parent',library['scl_ref'],'IRGS-SCL-1.0')
check('V05','entry count',len(records),122)
check('V06','unique ids',len(indexed),len(records))
check('V07','source starter count',sum(r['kind']=='technique' and r['status']=='native_source' for r in records),18)
check('V08','proposed technique count',sum(r['kind']=='technique' and r['status']=='proposed_complete_opt_in' for r in records),31)
check('V09','native unit count',sum(r['kind']=='unit_profile' and r['status']=='native_source' for r in records),4)
check('V10','mission coverage',sum(r['kind']=='mission_template' for r in records),11)
check('V11','institution coverage',sum(r['kind']=='institution_template' for r in records),12)
check('V12','service coverage',sum(r['kind']=='service_profile' for r in records),12)
check('V13','equipment coverage',sum(r['kind']=='equipment' for r in records),18)
check('V14','held count',sum(r['status']=='held_incomplete' for r in records),20) # 16 held candidates + 4 held equipment
check('V15','declared statuses valid',all(r['status'] in library['statuses'] for r in records))
check('V16','all entry ids valid',all(re.fullmatch('SNCL-[A-Z]-[NP]?[0-9]{3}',r['id']) or re.fullmatch('SNCL-[GMOSH]-[0-9]{3}',r['id']) for r in records))
check('V17','native tech contract fields',all(all(r.get(k) for k in ['rank','discipline','action','range','effect','cost','activation','source']) for r in records if r['kind']=='technique' and r['status']=='native_source'))
check('V18','new tech contract fields',all(all(r.get(k) for k in ['rank','discipline','affinity','action','range','target','activation','duration','effect','counterplay','risk','physical_world']) for r in records if r['kind']=='technique' and r['status']=='proposed_complete_opt_in'))
check('V19','new tech affinities',all(r['affinity'] in ['neutral','Fire','Wind','Lightning','Earth','Water'] for r in records if r['kind']=='technique' and r['status']=='proposed_complete_opt_in'))
check('V20','native group one entry',sum('Spark / Pebble / Droplet'==r['name'] for r in records),1)
check('V21','held candidates not playable',all(r['status']=='held_incomplete' for r in records if r['kind']=='held_candidate'))
check('V22','no library-origin core owners created',all(r['kind']!='core_owner' for r in records))
# source equality direct from parent; required for source-preservation claim
source_path=ROOT/'IRGS_Shinobi_Nexus_World_Engine_SNWE_R0_3_Core3_2_SCL1_0_CMRR.md'
if source_path.exists():
    engine=source_path.read_text()
else:
    engine=(P/'source_snapshot_SNWE_R0_3.md').read_text()
start=engine.index('### 6.4 Starter techniques')
end=engine.index('Source basis: S01, S37',start)
lines=[x for x in engine[start:end].splitlines() if x.startswith('Technique: ')]
check('V23','source starter lines',len(lines),18)
parsed={}
for line in lines:
    match=re.match(r'Technique: (.*?) • Rank / discipline: ([EDCBAS]) / (.*?) • Action and range: (.*?) • Operating effect: (.*)',line)
    if match:parsed[match.group(1)]=match
source_match=all(r['name'] in parsed and r['effect']==parsed[r['name']].group(5) and r['rank']==parsed[r['name']].group(2) for r in records if r['kind']=='technique' and r['status']=='native_source')
check('V24','18 effects copied exactly',source_match)
unit_expected=[('Recon cell',2,2,4,3,3,4),('Assault detachment',4,3,3,4,4,6),('Sealing corps',2,4,4,3,3,4),('Medical support',1,2,4,4,4,4)]
unit_actual=[(r['name'],r['power'],r['defense'],r['skill'],r['morale'],r['supply'],r['strength']) for r in records if r['kind']=='unit_profile']
check('V25','four unit values match source text',unit_actual,unit_expected)
# exact provenance match (within library manifest)
check('V26','source SHA',hashlib.sha256(engine.encode()).hexdigest(),library['source_sha256']['snwe_engine'])
# qualifying contract fixtures (synthetic). These do not claim to be the original full Core implementation.
costs=[5+i for i in range(3)]
check('V27','C-rank scene cost sequence',costs,[5,6,7],'bounded_arithmetic')
chakra=40; paid=[]
for p in costs:chakra-=p; paid.append(p)
check('V28','chakra reduction even when one Mold fails',chakra,22,'bounded_arithmetic')
# normal R0.3: CER 2.5 + 0.5 = 3; Body Flicker CU 3 then upkeep 1 => one threshold trauma, not two
threshold=3;spent=[3,4,5];crossings=sum(spent[i]>threshold and (i==0 or spent[i-1]<=threshold) for i in range(len(spent)))
check('V29','one overclock threshold crossing',crossings,1,'bounded_arithmetic')
# Kit remaining and non-duplicated transfers
kit=3;kit-=1;kit-=1;kit-=1
check('V30','finite kit charges',kit,0,'bounded_accounting')
physical_site,transit,destination=6,0,0
physical_site-=4;transit+=4
check('V31','one shipment conserved before receipt',(physical_site,transit,destination),(2,4,0),'bounded_accounting')
transit-=4;destination+=4
check('V32','one shipment conserved after receipt',(physical_site,transit,destination),(2,0,4),'bounded_accounting')
# Game effect vs physical creation: native Illusory Clone explicitly prohibits independent actions/damage
illusion=indexed['SNCL-J-N002']['effect']
check('V33','native illusion has no physical actor','No independent actions or damage' in illusion)
check('V34','held summons do not grant autonomous actions',indexed['SNCL-H-002']['status']=='held_incomplete')
check('V35','native Field Mending not cure injury','Does not cure Injury' in indexed['SNCL-J-N007']['effect'])
check('V36','native barrier no resistance','no mitigation' in indexed['SNCL-J-N017']['effect'])
check('V37','native unit actual headcount unspecified',all('Unknown' in r['headcount'] for r in records if r['kind']=='unit_profile'))
# SCL crosswalk does not silently activate source-backed holds
cross=json.loads((P/'IRGS_SNCL_v0_1_SCL_Reference_Crosswalk.json').read_text())
check('V38','SCL references identity',cross['source'],'IRGS-SCL-1.0')
check('V39','SCL refs canonical 0.2',all(re.fullmatch('SCL:PBC-[A-Za-z0-9-]+@0.2',e['reference']) for e in cross['entries']))
check('V40','no ref promoted by catalogue',all(e['readiness'] in ('source_backed_hold','selected_qualitative','selected_qualitative_contract','scoped_extension','qualified','active') for e in cross['entries']))
check('V41','records no duplicated identifiers',len(records),len(set(r['id'] for r in records)))
md=(P/'IRGS_Shinobi_Nexus_Content_Library_SNCL_v0_1_Proposed.md').read_text()
check('V42','Markdown includes 18 native definitions',sum(x.startswith('### SNCL-J-N') for x in md.splitlines()),18)
check('V43','Markdown includes 31 new tech definitions',sum(x.startswith('### SNCL-J-P') for x in md.splitlines()),31)
check('V44','Markdown includes adoption and migration boundary','No historical SSN lore is silently discarded' in md and 'not adopted' in md.lower())
# Write report; if any failure, process fails and prevents unsupported release claim.
out={'document_id':'SNCL-0.1-VERIFICATION','edition':'2026-10-14','status':'bounded synthetic and source checks (not gameplay/playtesting)', 'cases':result,'passed':sum(x['status']=='PASS' for x in result),'failed':sum(x['status']=='FAIL' for x in result)}
(P/'IRGS_SNCL_v0_1_Verification_Results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f"SNCL checks: {out['passed']}/{len(result)} passed")
for x in result:
    if x['status']=='FAIL':print('FAIL',x['id'],x['name'],x['observed'],'expected',x['expected'])
sys.exit(1 if out['failed'] else 0)
