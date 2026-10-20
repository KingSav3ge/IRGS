"""Deterministically rebuild *complete* proposed R7 from exact R6 source."""
import re, json, hashlib
from pathlib import Path
root=Path(__file__).resolve().parent
source=(root/'sources/IRGS_Core_Engine_v3_3_Unification_Candidate_R6.md').read_text()
source=source.replace('## Version 3.3 — Proposed complete unification candidate, CMRR Round 6',
  '## Version 3.3 — Proposed complete unification candidate, CMRR Round 7',1)
source=source.replace('`IRGS-CORE-3.3-CANDIDATE-R6`','`IRGS-CORE-3.3-CANDIDATE-R7`',1)
source=source.replace('**Candidate iteration:** R6 (supersedes R5 proposal for design review only; neither edition is adopted).',
'**Candidate iteration:** R7 (supersedes R6 proposal for design review only; neither edition is adopted).',1)
source=source.replace('this R6 delivery does not embed or activate the catalogue.',
'R7 does not embed or activate the catalogue.',1)
source=source.replace('[IRGS_Core_v3_3_Candidate_Binding_Proposal_R6.json](IRGS_Core_v3_3_Candidate_Binding_Proposal_R6.json)',
 '[IRGS_Core_v3_3_Candidate_Binding_Proposal_R7.json](IRGS_Core_v3_3_Candidate_Binding_Proposal_R7.json)',1)
source=source.replace('**Validation:** R1–R5 evidence is retained in `sources/` and predecessor packages; R6 evidence is recorded in [CMRR_Round_6_Executed_Validation.md](CMRR_Round_6_Executed_Validation.md). The R6 harness additionally checks selected, attested incremental production, disrupted-work settlement, replacement-stock receipt, authorized continuation and exact work/stock lineage; it is not a complete implementation, independent solver or field playtest. No active binding compatibility or numerical calibration is established.',
'**Validation:** R1–R6 validation sources remain in predecessor packages and `sources/`; new R7 evidence is in [CMRR_Round_7_Executed_Validation.md](CMRR_Round_7_Executed_Validation.md). The bounded R7 adapter schedules tracked milestones with pre-frontier declared footprints and demonstrates physical work-in-progress, later inspection and accepted completion or salvage. This is not an independently implemented, calibrated, legally qualified or playtested engine, and its footprints remain manually specified.',1)

insertions={
11:"""### 11.R7 — Qualified selected work frontiers, physical occurrences and isolation (PROPOSED)

A selectable runtime adapter SHALL publish the pre-frontier read/write and scarce-capacity footprint of each event operation. Tracked production start, incremental milestone, disruption settlement, authorized continuation, finalization, inspection, physical loss and material disposition SHALL be dispatched through their actual record-owning procedure; routing an unfamiliar operation through a generic legacy dispatcher is prohibited. Unknown or incomplete footprints create a conservative dependency barrier rather than permission to commit.

Each occurrence frontier SHALL use one pre-event snapshot for dependency partition, and SHALL commit only after the entire frontier's evidence and physical consistency checks succeed. Independent components may complete notwithstanding an unresolved competing component. A shared-source component requiring allocation, authority, or physical ordering stays unexecuted and source-retained; event IDs never select a winner. A supported physical loss is an occurrence, not a competing budget application: recognize actual loss once and retain same-instant work claims as causally unresolved absent an evidential ordering. If aggregate claimed physical losses exceed measured stock, reject the entire inconsistent frontier pending evidence reconciliation. A deferred claim is not a consumed resource or a completed work milestone.

**R7 implementation boundary:** The reference scheduler has manual, fixture-bounded footprints, conservative same-time contention and same-implementation replay. Neither independent transitive dependency certification nor full authority/observation-time ordering is established. Administrative timestamps alone do not authorize a substage.
""",
35:"""### 35.R7 — Intermediate physical stock and disposition (PROPOSED)

Materials consumed during manufacturing are actual debits at consumption time, not a reservation or a reversible promise. Material physically converted into an intermediate becomes actual stock at its current location under K-STOCK, but it SHALL retain a separate intermediate/WIP identifier, state, selected source model and lineage. It is not usable as accepted finished stock merely because work finished or time elapsed.

Loss of an intermediate adjusts its actual physical quantity and recorded loss at the same source event. Inspection is an observation/quality decision and by itself performs no physical transformation. Acceptance, rejection, rework, salvaging and disposal require their applicable selected procedures and actual material disposition. Scrap, waste and remaining intermediate pieces must each be accounted once; only explicitly qualified transformations may create usable finished output. No material or item is reconstructed from a forecast, unfulfilled order, changed recipe or later report.
""",
62:"""### 62.R7 — One event source across process and reporting scales (PROPOSED)

Intermediate work, damage, inspection, acceptance, salvage and completed operations SHALL be represented by distinct source events while strategic, daily, workplace and character-scale views reference those same event IDs. Displaying WIP as expected future production does not add an accepted output to K-STOCK. A reporting-scale transition must not replay accepted completion or rescue an already destroyed intermediate; historical as-of views require an actual source-aware checkpoint or replay boundary. R7's fixture exercises one site across work and economic perspectives, **not** an independently executing month-scale simulator.
""",
91:"""### 91.R7 — Work lifecycle event contracts and failure classification (PROPOSED)

The shared coordinator SHALL support qualified source-bearing operations for `start_tracked_job`, `record_work_milestone`, `settle_disrupted_job`, `start_continuation` and `finalize_tracked_job` without bypassing the generic calendar and authoritative journal. Proposed specialist-interface operations `make_intermediate`, `inspect_intermediate`, `accept_intermediate` and `salvage_intermediate` must commit atomically against the existing K-STOCK/K-WORK records. Recorded outputs must identify an original event, selected process profile and evidence or competent decision as applicable.

A contested group stays pending as an unresolved claim, not a guessed failure or success. Classify physically incompatible evidence, missing prerequisite, invalid action, legal/authority deficiency, competing allocation, and unresolved chronology separately. Distinguish a physical occurrence from a proposed work request. If current evidence is insufficient, preserve the source event and return the unresolved decision to its competent authority; do not invent a resolution or charge costs. Idempotent replay and save/load shall preserve operation identity and preexisting state.
""",
109:"""### 109.R7 — Qualified intermediate manufacturing and recovery (PROPOSED)

A production profile SHALL explicitly identify input types/quantities, intermediate types/quantities, acceptable completed output and the applicable salvage or waste model. Inputs are consumed when the qualified operation actually occurs; intermediate output enters physically owned stock only through that event. Intermediate units remain separate from final production until an inspection and valid acceptance operation. An inspected rejection produces no finished article automatically. Scrap or salvage is a later material transformation with actual resulting quantity and its own source.

Each workpiece instance snapshots the selected profile revision at its source event, protecting historical yield and quality requirements from future profile edits. Any nonlinear, fractional, multi-stage, quality-dependent or labor-dependent process requires an appropriately calibrated specialist adapter; the R7 integer fixed-yield fixture is not a universal manufacturing formula. Do not charge labor, time, energy or disposal costs without applicable selected rules; an omitted cost is an explicit calibration/coverage gap, not proof that the activity is free.
""",
114:"""### 114.R7 — Economic separation of WIP, accepted stock and claims (PROPOSED)

ECO SHALL distinguish capital and raw material consumed in ongoing work, physical work-in-progress, accepted finished inventory, rejected goods, recovered scrap, and the costs/claims of assessment or recovery. Goods are not saleable as completed merely because the factory reports scheduled production; buyers, military quartermasters and households may recognize acceptance status differently under actual contractual/institutional rules. An inspection entry establishes a finding; only an authorized physical conversion or asset status transition may change the source stock. Aggregate production and cash displays are read-only projections, not newly minted stock or income.
""",
117:"""### 117.R7 — National continuity across industrial and military demand (PROPOSED)

A region's farm, household, workshop and armed forces share resource locations, labor capacities and institutional budgets. An unresolved contract or allocation dispute at one workplace shall not freeze unrelated production. A verified warehouse or workshop loss shall continue to affect all actual claimants through remaining stock, not by rescinding the event. A province/monthly summary shall include supported finished and intermediate stocks separately; it must not turn WIP into final deliveries when switching scales. Strategic mass-balance and independent long-term autonomous production remain separate unqualified acceptance gates.
""",
122:"""### 122.R7 — Social obligation continuity through interrupted production (PROPOSED)

Household service requirements, wages owed and legal work claims remain separate from physical WIP or destroyed stock. A rejected tool, ration process, housing component or medical supply batch may delay actual delivery without erasing household need or creating an invented injury. Actual care, institutional assistance or new purchases require competent real actors, physical resources and clock time. Subsequent salvage or acceptance cannot rewrite previous family obligations, authority decisions or work already certified.
""",
124:"""### 124.R7 — Military provisioning from unfinished civil output (PROPOSED)

A military requisition cannot count a workshop's incomplete goods as issued finished equipment. The army may claim, reserve or fund production through Core ECO/K-WORK/K-STOCK, but must receive actual qualified completed stock (or explicitly configured field-use intermediate) before readiness or issued-equipment state changes. A physical loss to incomplete equipment is reflected in the same source ledger as civilian losses; it is not counted again as a second tactical casualty or logistics loss. MIL domain governance, obligation and allocation procedures do not override manufacturing feasibility.
"""
}
for n,section in insertions.items():
    match=re.search(rf'^## {n} [^\n]+$',source,re.M)
    if not match:raise RuntimeError(f'missing numbered section {n}')
    following=re.search(r'^(?:## \d+ |# Appendix [A-D])',source[match.end():],re.M)
    if not following:raise RuntimeError(f'no next section {n}')
    at=match.end()+following.start()
    source=source[:at]+section+'\n'+source[at:]

acceptance="""### R7 shared-coordinator and work-in-progress acceptance cases — PROPOSED; bounded evidence only

| ID | Trigger and required outcome | Bounded R7 evidence | Still unqualified |
|---|---|---|---|
| CE-FRT-R7-01 | Schedule a tracked job and later actual milestone, committing through correct K-WORK path | Tests 166–167 | Model/evidence validity supplied by fixture |
| CE-FRT-R7-02 | Independent tax assessment proceeds alongside work | Test 168 | General government authority not authenticated |
| CE-FRT-R7-03 | Two same-time milestones attempt same work: neither may win by event ID | Test 169 | Competent reconciliation of competing attestations |
| CE-FRT-R7-04 | Unrelated kitchen work proceeds while farm milestone is contested | Test 170 | Third-party dependency verification |
| CE-FRT-R7-05 | Physical fire and disputed work share frontier: loss acknowledged, unproved work deferred | Tests 171–172 and 193 | True occurrence/observation order and staged dispute resolution |
| CE-FRT-R7-06 | Same-instant prerequisite and result, missing job, or repeated event identity | Tests 173–175 | Structured typed invalidity and dependency diagnostics |
| CE-FRT-R7-07 | Save/load and deferred-claim recovery do not duplicate execution | Tests 176 and 200 | Independent engine replay equivalence |
| CE-WIP-R7-08 | Raw input becomes tracked physical intermediate without finished output | Tests 177–179 and 195 | Selected industrial process and time/energy cost |
| CE-WIP-R7-09 | Qualified inspection and acceptance converts WIP exactly once | Tests 180–181 and 191–192 | Qualified inspector and material/quality model |
| CE-WIP-R7-10 | Rejected/damaged goods salvage only surviving physical quantity | Tests 182–186 and 197–198 | Actual salvageability and waste disposition |
| CE-WIP-R7-11 | Unselected model, impossible stock or source replay cannot create product | Tests 187–188 | External process/evidence authenticity |
| CE-WIP-R7-12 | Competing raw material use defers while unrelated taxes proceed | Tests 189–190 | Optimized authorized same-frontier allocation |
| CE-WIP-R7-13 | Combined loss evidence exceeds holdings: entire current frontier stays uncommitted | Test 196 | Reconciliation of contradictory physical evidence |
| CE-WIP-R7-14 | Unknown operation lacks qualified footprint: never silently execute | Test 199 | Complete module audit/certification |
| CE-WIP-R7-15 | Source profile is fixed per instance, damaged historical binding detectable | Tests 201–203 | Version-aware external profile registry and migration |
| CE-WIP-R7-16 | Integrated work/fire/replacement/fabrication/inspection/salvage sequence | `run_round7_fixture.py` (17 committed events) | Full independent multi-institution engine |
| CE-WIP-R7-17 | Three industries, military procurement and autonomous households over months | NOT EXECUTED | Calibrated strategic producer/consumer and MIL readiness link |
| CE-WIP-R7-18 | Real multi-stage facility with partial goods, energy, workforce, quality grades and nonlinear scrap | NOT EXECUTED | Chosen industrial specialism and rate calibration |

**Execution boundary:** 165 inherited R1–R6 tests and 38 new R7 tests (166–203) pass, for **203 bounded unit tests** in the reference harness. These do not constitute eighteen complete independent acceptance cases, adoption, playtesting, real-world legal validity or a general-purpose game engine. The R7 workpiece model uses a supplied synthetic selected conversion profile and asserted evidence; it does not independently model workpiece manufacture time, energy, wages or the inspection process. Runtime footprints are hand-declared and conservative rather than exhaustively qualified.

"""
needle='# Appendix D — Optional Scoped Reference Profiles'
assert needle in source
source=source.replace(needle,acceptance+needle,1)

sections=re.findall(r'^## (\d+)\s',source,re.M)
assert sorted(map(int,sections))==list(range(1,125)), ('numbered section failure',len(sections))
for owner in ['K-ACTOR','K-ASSET','K-INFO','K-NET','K-ORG','K-POP','K-STOCK','K-TIME','K-WORK']:
    assert owner in source,owner
for domain in ['GOV','ECO','INV','MAR','CIV','MED','WILD','INTEL','URBAN','LIFE','COMP','MIL']:
    assert re.search(rf'^## \d+ {domain} ',source,re.M),domain
path=root/'IRGS_Core_Engine_v3_3_Unification_Candidate_R7.md'
path.write_text(source)
sha=hashlib.sha256(path.read_bytes()).hexdigest()
original=json.loads((root/'sources/IRGS_Core_v3_3_Candidate_Binding_Proposal_R6.json').read_text())
original['document_id']='IRGS-BIND-PROPOSAL-CORE-3.3-CMRR-R7'
original['status']='R7 design proposal only: UNSELECTED; NOT adopted, calibrated, playtested or migrated'
original['candidate_core_ref']='IRGS-CORE-3.3-CANDIDATE-R7'
for k,v in list(original.items()):
    if isinstance(v,str) and 'R6' in v and k!='historical_source_ref':
        original[k]=v.replace('R6','R7')
original['r7_proposal']={'current_selection':'IRGS Core 3.2 unchanged',
  'source_migration':'none','owners_preserved':9,'numbered_sections':124,
  'read_write_footprints':'bounded hand-declared only',
  'r6_work_scheduler':'candidate R7 dispatch through tracked-work adapter',
  'work_in_progress':'physical lot under existing K-STOCK, quality/disposition K-WORK',
  'source_profile':'snapshotted selected recipe per workpiece, not mutable lookup'}
original['reference_runtime_evidence']='203 bounded Python unit tests (165 inherited + 38 R7); one 17-event staged synthetic fixture; read-only cross-check audit; NOT an independent simulator or engine qualification'
original['candidate_core_sha256']=sha
# Preserve existing key names while recording actual new version document digest.
(root/'IRGS_Core_v3_3_Candidate_Binding_Proposal_R7.json').write_text(json.dumps(original,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'sections':len(sections),'owners':9,'domains':12,
  'sha256':sha,'candidate_bytes':path.stat().st_size,'r7_acceptance':18},indent=2))
(root/'results/structural_checks_R7.json').write_text(json.dumps({
  'section_count':len(sections),'sections_sequential':True,'state_owners':9,
  'domains':12,'r7_acceptance':18,'candidate_sha256':sha},indent=2)+'\n')
