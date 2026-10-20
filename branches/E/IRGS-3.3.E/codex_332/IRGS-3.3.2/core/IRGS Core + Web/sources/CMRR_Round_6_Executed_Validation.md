# IRGS Core Unification — Round 6 CMRR: Interrupted Work, Partial Production and Recovery

**Status:** PROPOSED / reference implementation and specification only. **NOT adopted, selected, calibrated, playtested, independently implemented or migrated.**  
**Date of design session:** 17 October 2026.  
**Authority:** Selected IRGS Core v3.2 remains the parent. Core v3.3 R5 is the superseded *proposal*, not an adopted baseline. R6 supersedes R5 **for candidate review only**.

## Purpose and scope

Repair the R5 deficiency: an active job could reserve all its ingredients until the planned end and then be suspended by a fire without any recorded evidence-backed intermediate work or partial output. R6 separates (a) elapsed time and plans, (b) attested actual work, (c) stock physically consumed, (d) qualified accepted output, (e) unresolved work and legal claims, and (f) later authorized completion. Preserve R1–R5 military, social, accounting, event and scale distinctions without importing a universal linear manufacturing law.

## CMRR 1 — Bidirectional source comparison

| Source and authority | Valid function before R6 | R6 addition/reconciliation | Kept out of Core/default | Status |
|---|---|---|---|---|
| Selected Core 3.2 | K-WORK, K-STOCK, K-TIME, K-INFO, K-ACTOR, K-ORG and other owners; actor choice and resource causality | No selected source modified; all 124 sections preserved in proposed Core | No adopted narrative or campaign overrides changed | Established selected parent |
| Proposed Core 3.3 R5 | MIL/LIFE unification, selective transaction components, stock-loss separation, suspended claims, tactical source projection | Extend §§11,35,91,109,114,117,122,124 with explicit milestone/settlement/continuation contracts | No independent extra work/material state owner, no silent model selection | Proposed; preserved source under `sources/` |
| `economic_extension.py` R3–R5 | Certified opening/closing whole jobs, reservations, shipment and household needs, wages | Reuse physical stock and operating record; new *opt-in* tracked-job overlay | No modification to untracked legacy production pathways | Proposed bounded implementation |
| `r5_hazards.py` | Physical loss occurs despite backing and preserves shortfall | Retain physical loss; certified pre-loss output remains, suspended job can be settled | Still refuses in-transit fire without specialist reconciliation | Proposed bounded implementation |
| `selective_coordinator.py` R4 | Hand-declared owner footprint grouping and deferred contests | Retain for legacy events; **do not** pretend it has certified new R6 work-event footprints | No R6 milestone scheduling until read/write contract qualified | Known implementation blocker |
| `r5_audit.py` | Independently rechecks materials and *active* suspended shortfalls | Preserve historical auditor; create `r6_audit.py` recognizing settled/fulfilled shortfalls | Neither auditor is an independent world engine | Validation only |
| Military Slim 1.2 | Service, duty, provisioning, operational records | A military unit inherits same K-WORK work-recovery contract | No specialized military combat model or doctrine imported | Proposed source unchanged |
| Roman Slim 1.2 | Legal standing, labor/custody and household claims | Shared work/claim interface applies irrespective of period | Roman legal entitlement and forced-labor specifics remain setting/profile-owned | Accepted workshop source unchanged |
| Campaigns including AST | Campaign-specific time, inventories, characters, source pins | No automatic file/source migration; continue v3.2 active bindings | No lore, past events or PC decisions rewritten | No migration |

**Reverse reconciliation:** The R6 package contains the exact R5 Core document, R5 validation, R5 binding proposal, selected v3.2 document, and relevant Military/Roman sources. All 138 prior executable tests were copied and rerun in their existing files. No numbered Core section, old R4/R5 proposed text or owner ID has been removed. R6 preserves R5 `loss` reports instead of rewriting prior incidents. Earlier complete archives remain separate historical deliverables.

## CMRR 2 — Source-to-destination and ownership matrix

| ID | Mechanism or conflict | Decision and destination | Reason / invariant | Validation and unresolved |
|---|---|---|---|---|
| R6-01 | Job input considered only at completion | **Refine K-WORK/K-STOCK milestone interface** | Actual milestone debits consumed input, frees reserved portion and credits accepted output once | Tests 139–141; bound integer process |
| R6-02 | Four hours elapsed implies four hours productive | **Reject universal inference** | Clock is not evidence of output or competence | Test 142; authenticity of external evidence not implemented |
| R6-03 | A source calls an unknown production model | **Require selected model binding** | Generic Core must not invent yield/conversion | Test 143; names literal fixture IDs |
| R6-04 | Fire after prior accepted output | **Retain historical production and loss separately** | Physical loss of remaining ingredient cannot erase previously accepted goods | Tests 144–145 |
| R6-05 | Legacy complete_job would double-count tracked output | **Reject mixed lifecycle procedures** | One owner/one source per effect | Tests 146–147 |
| R6-06 | Interrupted job worked but is not fully complete | **Settle certified portion and preserve open legal/work questions** | Accepted goods, labor entitlement, reservations and obligation are distinct | Tests 148–151; wage law unresolved |
| R6-07 | Lost inputs replaced with a magical inventory credit | **Require real source, transit and receipt** | Stock in transit is physical and not arrived until receipt | Tests 152–154 |
| R6-08 | Resume an already partially completed contract | **New authorized continuation linked to old job** | Hours and goods in original job not repeated | Tests 155,157,160,165; changing workers not yet qualified |
| R6-09 | Wages accrue at both partial and total settlement | **Accrue selected verified hours exactly once** | Wage payable is claim; treasury money remains actual stock | Test 156; no universal unpaid-time decision |
| R6-10 | Shortfall remains permanently “unfulfilled” after valid continuation | **Record `fulfilled_by_continuation` with intact source** | Current claim state changes, historical loss remains | Test 165; settlement source trace |
| R6-11 | Audit assumes every shortfall belongs to active suspended job | **Retain R5 audit; add R6-aware read-only audit** | Historic settled claims continue to exist without phantom active work | Composite fixture and read-only audit |
| R6-12 | A validation error after partial commit leaks mutations | **Candidate-state commit for inherited R5 op path** | Failed qualification must not alter actual state | Code path revised; negative tests |
| R6-13 | An unrelated kitchen or household frozen by farm fire | **Retain isolated completion of independent jobs** | Causal isolation rather than global interruption | Test 161 and combined fixture |
| R6-14 | Tax assessment creates cash | **Retain ECO claim/cash separation** | Assessment is a liability, not a transfer | Test 162 and combined fixture |
| R6-15 | Production replacement creates extra people/kits | **Retain K-POP/K-STOCK conservation** | Recovery cannot mint population or equipment | Test 163 |
| R6-16 | Simultaneous R6 milestones lack vetted scheduler footprint | **Explicit safe refusal** | No accidental event-ID ordering masquerading as causal priority | Test 147; integration not yet solved |
| R6-17 | Batch, nonlinear and damaged intermediate products | **Deferred specialized process/profile contract** | Avoid false continuous yield from every task type | Not executed |
| R6-18 | Seasonal national recovery with independent strategic runner | **Future Core runtime qualification** | Coherent long-duration autonomous simulation must operate from the same state | Not executed |

## Proposed canonical records and operation contracts

Each tracked K-WORK job references its selected process/recipe, site, people, shift, planned worker-hours, actual certified milestones, source event IDs, accepted outputs, consumed stock, still-backed reservations, obligations, and any disrupted/unassessed interval. K-STOCK remains physical owner; K-WORK is the work lifecycle; ECO retains the wage claim, not duplicate money; K-INFO retains what was asserted/observed; GOV/K-ORG own any relevant authority. There are still **nine** state-owner types; `r6_progress` and `r6_settlements` are **reference-harness records** illustrating K-WORK lifecycle views, not newly proposed K-state owners.

Reference operations (directly and prospectively staged only):

1. `start_tracked_job`: select compatible real work model, site, qualified staff, future-work commitment and physical input reservation.
2. `record_work_milestone`: resolve a new covered interval; require provided evidence and selected model; debit only actual input; accept actual output; close this segment of remaining reservation.
3. Physical loss uses R5 `physical_loss`: physical stock/loss accounting first; if remaining reservations cannot be backed, suspend the affected jobs and record the original surviving claim.
4. `settle_disrupted_job`: close the interrupted job with verified hours, certified output already posted, earned money claims under the *supplied* agreement, and an explicitly unassessed interval/entitlement. Do not remove its shortfall history.
5. Physical `dispatch_stock` and `receive_stock` from R3 move externally existing inputs through transit; they do not approve extra work.
6. `start_continuation`: require current physical backing, qualified renewed future shift, competent authorization and exactly the unfinished amount of planned work. Link the original job so later attempted duplicate continuations fail.
7. `finalize_tracked_job`: only after all selected segments genuinely complete; accrue verified wages once; no second material debit/output credit; mark original shortfall fulfilled when linked completion actually satisfies it.

**Known simplification:** The reference uses synthetic fixed integer input/output rates per *verified* worker-hour. A valid four-hour acceptance milestone is possible where the evidence actually attests four hours; clock passage on its own is not evidence. No independent evidence authentication occurs. The reference assumes one selected wage agreement authorizes pay per certified hour; other employment-law policies need distinct modeling. Time potentially worked but not attested remains an open entitlement, not necessarily unpaid legally.

## CMRR 3 — Executed synthetic scenario

Inputs are *chosen fixture values*, **not calibration**: 1,200 people, 1,000 monetary units, 300 equipment kits, **16 units of seed** split 12 at the farm and 4 at an external warehouse; test work recipe consumes **1 seed per certified worker-hour**, produces **3 accepted grain per certified hour**, and uses **2 owed monetary units per certified worker-hour** under the fictional agreement. A kitchen independently uses prior grain and fuel to produce meals.

| Frontier | Actual event | K-WORK/K-STOCK/ECO consequence |
|---|---|---|
| 8 | Qualified farm and kitchen work start | Farm reserves 4 seed for four-hour plan; no production yet |
| 9 | One farm hour certified | 1 seed actually consumed; 3 grain actually accepted; remaining farm reservation 3 |
| 10 | Actual fire destroys 9 farm seed | Farm has 2 physical seed and a 3-seed remainder claim; farm suspends; 3 grain remains physically produced. Independent tax of 6 assessed, not paid |
| 11 | Farm interruption assessed | 1 verified hour/2 owed units credited; 3 planned hours still needed; unassessed elapsed interval [9,10] retained |
| 12 | Independent kitchen finishes, caregiver duty completed, replacement shipped | 12 meals accepted; replacement of 3 seed leaves warehouse and enters transit, no teleporting |
| 13 | Shipment received; new farm commitment made | Farm receives 3 seed; no production or authority inferred from delivery |
| 14–17 | Competently authorized linked continuation, three certified hours | 3 seed used; 9 **additional** grain accepted; no duplicate first hour |
| 18 | Continuation accepted; household provided 6 meals | Total grain 12; farm wages owed 8 total; historical loss retained; original performance claim fulfilled |
| 19 | Household needs audited | 4 required/actual care hours; 6 required/served meals; zero uncovered care/meal deficit in this fixture |

**Material identity:** opening seed 16 = remaining 3 + actually consumed 4 + loss 9. The internal shipment moves three physically existing units; it is neither production nor a new creation source. Original job and continuation have distinct milestone source IDs and verified hours **1 + 3**, not 4 + 3. Farm accepted output is **3 + 9 = 12** grain units. Kitchen accepted output is **12** meals; **6** later served. Cash still totals **1,000** because wages are liabilities and the tax remains assessed but unpaid. Population stays **1,200**, kit quantity stays **300**.

**Audit:** `r6_audit.py` recomputes global material identity, loss-journal provenance, milestone/settlement hours, and active-versus-settled shortfall legitimacy without using the world validator; it is a *separately coded invariant check*, not a second implementation of the state transition engine. Load/save with the same R6 reference yields an identical checksum. The output is in `results/round6_recovery_fixture.json`.

## Executed validation and acceptance boundary

Command from `runtime/`:

```bash
python -m unittest -q test_unification test_economic_integration test_selective_and_scale test_loss_and_scale test_work_recovery
python run_round6_fixture.py
```

**Result:** **165 passing tests** = 138 retained R1–R5 tests and **27 new R6 cases (139–165)**. The scenario executes a deterministic mixed-industry and household recovery, and structural checks confirm 124/124 numbered sections and all nine owners preserved. R6 Appendix C specifies **18 acceptance requirements**; many are broader than what tests prove. CE-WORK-R6-16–18 remain unexecuted, and other cases are only *partially* implemented under synthetic assumptions.

The suite does **not** certify selected validity of a real recipe, real-world process realism, rates, evidence authenticity, labor law, authority, industrial failure probabilities, medical harm, third-party independent engine equivalence, or sustained autonomous grand strategy. It is neither playtesting nor calibration. New work lifecycle operations deliberately refuse entry to the older scheduler; this is a **known runtime integration blocker**, not evidence of full scheduled execution.

## CMRR 4 — Regression, accounted removals and change log

- **Preserved:** Core sections 1–124; R4 selective-event and scale subsections; R5 physical-loss, reservation, strategic report and casualty-source rules; unchanged Roman and Military sources; the entire prior 138 tests.
- **New:** R6 additions to §§11,35,91,109,114,117,122,124; 18 acceptance declarations; milestone/settlement reference model; 27 new tests; household/work/fire/replacement fixture; read-only R6-aware audit; R6 unselected binding proposal.
- **Revised:** Reference shortfall status can evolve from `settled_with_unfulfilled_claim` to `fulfilled_by_continuation` after the linked job truly completes; old loss and original input claim remain. R6-world inherited-operator calls validate candidate state before committed swap, avoiding leak on failure.
- **Deprecated for selected play:** **Nothing.** R5 remains a historical source; no already-selected engine or campaign binding has been changed.
- **Excluded rather than silently lost:** Complex batch damage, actual fire physics, actor injuries, external evidence validation, choice of labor law, multi-worker substitutions, authorized priority allocations, scheduling read/write qualification, independently coded simulation, monthly demographic/economic execution.

## Migration impact, dependencies and unfinished requirements

**Campaign migrations: NONE.** Core 3.2 and campaign-pinned Military, Roman and AST assets remain authoritative. Adoption would require an explicit acceptance instruction and qualified receiving bindings with exact source hashes. Existing completed work and financial claims must be mapped prospectively without re-crediting earlier output, altering prior events, or applying new wage policies retroactively. Data migration for R5-type suspended jobs would need recorded evidence; absent proof, partial work is *unknown*, never automatically zero or completed.

Dependencies: Core §§5,11,12,24,35,62,91,109,114,117,122,124; R4 selective coordinator; R5 physical-loss coordinator; K-TIME, K-STOCK, K-WORK, K-ORG, ECO, LIFE, CIV and MIL interfaces; a selected mode-specific production/inspection model and applicable real authority. `runtime/r6_work.py` is a bounded implementation, not a replacement for either adopted genre models or the general Core runtime.

**Prioritized remaining gates:** (1) qualify R6 operations for full selective scheduler and same-frontier causal-order disputes; (2) implement a batch/intermediate-inventory process and independently test non-linear output/quality; (3) authenticate competent instructions and real evidentiary claim sources; (4) model replacement allocation among multiple genuinely competing civilian/military claimants without ID order; (5) reconcile shipment losses and waste/salvage; (6) validate long-duration autonomous national simulation and independent world executor; (7) profile-specific calibration and recorded playtests.

**Status:** Resubmission is not adoption. The R6 candidate should be reviewed critically and may be revised, rejected or selectively accepted in future rounds without changing current campaign state.
