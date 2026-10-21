#!/usr/bin/env python3
"""SNCL v1.0 deterministic integrity checks. Documentary, NOT runtime playtesting."""
from pathlib import Path
import json,hashlib,collections,csv,zipfile
from docx import Document
P=Path(__file__).resolve().parent
R=json.loads((P/'IRGS_SNCL_v1_0_Registry.json').read_text())
M=json.loads((P/'IRGS_SNCL_v1_0_Source_Manifest.json').read_text())
prev=json.loads((P/'source_documents'/'IRGS_SNCL_v0_1_Registry.json').read_text())
checks=[]
def check(label, ok):
 checks.append((label,bool(ok)))
 if not ok:print('FAIL:',label)
check('Record count',len(R['records'])==537)
check('Prior 122 dictionaries unchanged',R['records'][:122]==prev['records'])
check('Native effect text unchanged',all(a.get('effect')==b.get('effect') for a,b in zip(R['records'][:18],prev['records'][:18])))
check('Source archive 415 count',len(R['records'][122:])==415)
check('All source records blocked',all(x['status']=='legacy_unconverted' and x['activation'].startswith('BLOCKED') for x in R['records'][122:]))
check('Unique IDs',len({x['id'] for x in R['records']})==537)
check('Rank distribution',dict(collections.Counter(x['legacy_rank'] for x in R['records'][122:]))==R['counts']['rank_distribution_legacy'])
DOC=Document(str(P/'source_documents'/'SSN_ Jutsu Compendium V1.docx'))
fields=['name','legacy_type','legacy_rank','legacy_tags','legacy_cost','legacy_band_min','legacy_description_effect']
def clean(s):return ' '.join(s.replace('\u00a0',' ').split())
for x in R['records'][122:]:
 t=DOC.tables[x['legacy_source_table_index']]
 vals=[clean(c.text) for c in t.rows[x['legacy_source_row_index']].cells]
 check('Source row '+x['id'],vals==[x[k] for k in fields])
for x in M['source_files']:
 p=P/'source_documents'/x['name']
 check('Source hash '+x['name'],p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'])
check('Markdown contains all 415 IDs',all(x['id'] in (P/'IRGS_Shinobi_Nexus_Content_Library_SNCL_v1_0_Final.md').read_text() for x in R['records'][122:]))
with (P/'IRGS_SNCL_v1_0_Legacy_Source_Crosswalk.csv').open(encoding='utf-8-sig',newline='') as f: check('CSV archive count',sum(1 for _ in csv.DictReader(f))==415)
check('PDF reference only',all(x['readiness']=='reference_only_not_mechanically_converted' for x in R['legacy_sources']['browse_pdf_manifest']))
check('All PDFs available',len(list((P/'source_documents').glob('*.pdf')))==11)
print(f'{sum(v for _,v in checks)}/{len(checks)} checks passed')
if not all(v for _,v in checks):raise SystemExit(1)
