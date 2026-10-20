"""Build proposed R8 documents and hash manifest; never change selected sources."""
import hashlib
import json
import shutil
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(path, value): path.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')

def build():
    predecessor=ROOT.parent/'IRGS_Core_Unification_CMRR_R7'
    if predecessor.exists():
        checks={}
        for p in predecessor.rglob('*'):
            if not p.is_file() or '__pycache__' in p.parts: continue
            rel=p.relative_to(predecessor)
            dest=ROOT/rel
            if str(rel)=='README.md':
                dest=ROOT/'sources/README_R7_preserved.md'
                shutil.copyfile(p,dest)
            checks[str(rel)]={'sha256':sha(p),'preserved':dest.exists() and sha(dest)==sha(p)}
        assert all(x['preserved'] for x in checks.values()),'inherited source changed'
        write(ROOT/'results/r8_predecessor_integrity.json',checks)
    source_specs=[
      ('Military','IRGS_Soldier_Military_Life_Slim_v1_2_Core3_2_MCL1_0_Proposed.md','membership, equipment, orders, commitments'),
      ('Roman','IRGS_Roman_Republic_Life_Simulation_Engine_Slim_v1_2.md','household work, obligations, authority, custody'),
      ('AST','AST_Engine_v0_5.md','continuity, household work, military inheritance, player agency'),
      ('Fantasy','IRGS_Fantasy_Engine_Slim_v1_2_Core3_2.md','genre effects, actor state, common time and resources'),
      ('PAF','IRGS_PAF_Engine_v2_1_Core3_2.md','scarcity, work, shared stock and infrastructure'),
      ('SNWE','IRGS_Shinobi_Nexus_World_Engine_SNWE_R0_3_Core3_2_SCL1_0_CMRR.md','setting techniques and shared state'),
      ('Space','IRGS_Space_Exploration_and_Colonization_Foundation_Slim_v0_2_Proposed.md','life support, logistics, infrastructure')]
    out=ROOT/'sources/engine_references'; out.mkdir(exist_ok=True)
    matrix=[]
    for name,filename,scope in source_specs:
        local=list((ROOT.parent/'IRGS').rglob(filename))
        dest=out/filename
        if local:
            # Prefer the shortest primary release path over nested historical copies.
            src=min(local,key=lambda p:len(p.parts)); shutil.copyfile(src,dest)
        if not dest.exists(): raise FileNotFoundError(filename)
        matrix.append({'engine':name,'source_file':str(dest.relative_to(ROOT)),
                       'source_sha256':sha(dest),'review_scope':scope,
                       'shared_handler_evidence':'r8_operation_inventory.json; no automatic native equivalence',
                       'native_operation_inventory':'OPEN: extraction and executable binding required',
                       'native_dependency_certification':'NOT CERTIFIED',
                       'selected_core':'3.2','migration':False})
    write(ROOT/'results/r8_cross_engine_gate_matrix.json',matrix)
    inventory=json.loads((ROOT/'results/r8_operation_inventory.json').read_text())
    with (ROOT/'results/r8_operation_coverage.csv').open('w',newline='',encoding='utf-8') as stream:
        writer=csv.writer(stream)
        writer.writerow(['operation','observed_executions','distinct_read_paths','distinct_write_paths','status'])
        for row in inventory['operations']:
            writer.writerow([row['operation'],row['executions'],len(row['reads_union']),len(row['writes_union']),row['status']])
    original=(ROOT/'IRGS_Core_Engine_v3_3_Unification_Candidate_R7.md').read_text(encoding='utf-8')
    contract=(ROOT/'ROUND_8_DEPENDENCY_CONTRACT.md').read_text(encoding='utf-8')
    candidate=ROOT/'IRGS_Core_Engine_v3_3_Unification_Candidate_R8.md'
    candidate.write_text('# IRGS Core v3.3 — Round 8 complete candidate\n\n'
        '**PROPOSED / UNSELECTED. Core v3.2 remains selected.**\n\n'
        'The full R7 text follows unchanged as the inherited candidate baseline. Its R7 labels and evidence retain their original scope. '
        'Appendix E adds the R8 proposal; it neither selects R7 nor grants native engine certification.\n\n'
        +original+'\n\n# Appendix E — Round 8 proposal\n\n'+contract,encoding='utf-8')
    binding=json.loads((ROOT/'IRGS_Core_v3_3_Candidate_Binding_Proposal_R7.json').read_text())
    # Preserve R7 binding as a source; new proposal is explicit and minimal.
    write(ROOT/'IRGS_Core_v3_3_Candidate_Binding_Proposal_R8.json',{
        'document_id':'IRGS-BIND-PROPOSAL-CORE-3.3-CMRR-R8','status':'PROPOSED_UNSELECTED',
        'existing_core_ref':'IRGS-CORE-3.2','candidate_core_ref':'IRGS-CORE-3.3-CANDIDATE-R8',
        'candidate_file':candidate.name,'candidate_sha256':sha(candidate),
        'selected_source_sha256':sha(ROOT/'sources/IRGS_Core_Engine_v3_2_Selected_Source.md'),
        'preserved_owner_ids':binding['preserved_owner_ids'],'campaign_migration':False,
        'native_multi_engine_certification':'OPEN','runtime_mode':'explicit opt-in research adapter'})
    manifest={str(p.relative_to(ROOT)):sha(p) for p in sorted(ROOT.rglob('*'))
              if p.is_file() and '__pycache__' not in p.parts and p.name!='file_sha256_manifest_R8.json'}
    write(ROOT/'results/file_sha256_manifest_R8.json',manifest)
    print(json.dumps({'files':len(manifest),'native_engines_reviewed':len(matrix),'status':'PROPOSED_UNSELECTED'}))

if __name__=='__main__': build()
