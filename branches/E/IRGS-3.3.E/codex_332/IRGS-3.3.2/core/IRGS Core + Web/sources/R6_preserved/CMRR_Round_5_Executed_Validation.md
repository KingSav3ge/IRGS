# IRGS Core Unification — CMRR Round 5: Physical-Loss Reconciliation and Tactical/Strategic Provenance

**Status:** PROPOSED / executable reference fixtures only. **Not adopted, selected, calibrated, playtested, independently implemented or migrated.**  
**Design session date:** 17 October 2026 (container timestamps may differ).  
**Source authority:** Selected `IRGS-CORE-3.2` remains authoritative. Previous design candidates R1–R4 remain proposal history; `IRGS-CORE-3.3-CANDIDATE-R5` is a complete proposed receiving specification.

## 1. Purpose, scope, and result

CMRR Round 5 tackles the two gaps explicitly deferred by Round 4:

1. **Actual physical loss versus already reserved and simultaneously requested stock.** The loss must write once even where goods were reserved; shortage must not cancel legal/economic claims, create negative goods, or arbitrarily choose a beneficiary.
2. **Tactical → regional/strategic → tactical continuity.** One source combat event must remain one set of physical effects despite engagement summaries, downstream reports, saves, and different views. A disabled actor is not automatically dead.

Deliverables: complete Core v3.3 R5 Markdown; preserved R4 source and prior documents; R5 binding proposal (unselected); bounded loss coordinator and strategic read-only projection; independent ledger-invariant auditor; 30 new unit tests; a combined synthetic loss/funding/farm/kitchen/engagement fixture; package integrity manifest.

**Executed result:** 138 Python tests pass (108 R1–R4 tests retained + 30 R5 tests numbered 109–138). Structural preservation checks pass for 124 sections, nine existing state owners and 14 new acceptance scenarios. The R5 synthetic fixture executes two described focus flows but **does not pass all 14 integration acceptance cases**. In particular, transit loss, restock/reallocation, causal chronology qualification, and genuinely autonomous multi-month simulation remain unimplemented.

## 2. Compare — bidirectional source inventory

| Source, authority/status | Prior valid functions | Round 5 treatment | Functions not implicitly moved |
|---|---|---|---|
| Selected Core 3.2 / established | K-TIME, K-ACTOR, K-ASSET, K-INFO, K-NET, K-ORG, K-POP, K-STOCK, K-WORK; physical owner and chronology semantics | **Retain** 124 numbered sections in R5 candidate; no selection change | No campaign state touched; selected source unchanged |
| Proposed Core v3.3 R4 | MIL/LIFE unification, selective contention graph, non-writing day/month coverage, 108 tests | **Extend** §§11, 35, 62, 91, 109, 117, 122, 124 with new R5 subsection text | R4 additions §§11.R4/62.R4/91.R4/117.R4/124.R4 preserved |
| R4 `selective_coordinator.py` / proposed fixture | Component partition; deferred decisions; same-time footprint-based isolation | **Reuse** for otherwise independent post-loss proposals, with an added loss-first observed-phase adapter | Still manually declared footprints; not an authoritative general scheduler |
| R4 `economic_extension.py` / proposed fixture | Actual work/material lifecycle, reservations and consumption | **Revise local copy** to add an optional physically lost material ledger and suspend unsupported jobs | Historical R4 implementation preserved in Round 4 package; no global change to its adopted status |
| R4 `scale_coverage.py` / proposed fixture | Read-only source-exclusive interval reporting | **Preserve**; add separate named-actor military journal projection | No full cohort execution or numerical combat model |
| Military Slim v1.2 / proposed | Enlistment, duty, engagement, equipment and report interfaces | **Maintain receiving mapping** in MIL, particularly combat-effect and report source continuity | Detailed military doctrine/warfare remains in specialist models |
| Roman Slim v1.2 / accepted workshop reference | Legal status, custody, recognition, household work/standing | **Preserve unchanged** in `sources` and inherited Core LIFE/GOV design; impacts indirectly through common source and consequence rules | No Roman legal or content change; v1.3 Roman receiving proposal remains unselected |
| Existing campaigns (including AST) | Actual source pins, campaign time, equipment, characters, journal | **No migration or replay applied** | No retrospective conversion of injuries, resources, or chapters |

**Reverse check:** Full R4 source retained byte-for-byte under `sources/`. The current R5 builder takes R4 as its input, preserving all numbered sections and all prior R4 proposed subsections. No specialized Roman model, Military content record, or campaign override is deprecated. Existing R1–R3 documents and code remain available in historical packages; the R5 package also carries R4 and its selected-parent evidence.

## 3. Merge/reconcile — ownership and collision decisions

| ID | Collision / possible defect | Disposition | Authority and ownership | Status / unresolved issue |
|---|---|---|---|---|
| R5-01 | A warehouse burns despite supplies being reserved | **Retain actual physical loss** | K-STOCK physical quantity; K-TIME source occurrence | Bounded fixture executed; actual fire simulation absent |
| R5-02 | Treat destroyed goods as workplace use | **Split loss vs consumption** | K-STOCK loss channel vs K-WORK use | Tests 109, 114, 136–137 |
| R5-03 | Depleted pool leaves 2+ active reservations underbacked | **Preserve all claims, suspend ambiguous backing** | K-STOCK backing; K-WORK jobs; K-ORG claims | Tests 110, 124; actual allocation policy missing |
| R5-04 | Suspended work auto-credits projected crop at end date | **Reject output from incomplete feasibility** | K-WORK completion + actual consumed inputs | Test 111; partial progress not settled |
| R5-05 | Unrelated kitchen, tax claim or funding freezes due to warehouse dispute | **Preserve independent continuation** | Same authoritative owners, no fabricated dependencies | Tests 112–113, 117, combined fixture |
| R5-06 | Hazard versus same-time physical departure silently ordered by ID | **Defer ambiguous departure** | K-TIME causal stage, K-STOCK transaction | Test 116; real sequence must be proven before resolution |
| R5-07 | Multiple simultaneous measured losses together exceed existing holdings | **Reject inconsistent combined evidence atomically** | Physical K-STOCK limits, K-INFO evidence | Tests 118–120; alternative chronology/stock corrections require evidence |
| R5-08 | Transit-cargo loss violates shipment quantity invariant | **Safe refusal in bounded adapter** | K-STOCK transit; cargo/shipment K-WORK | Test 121; not a complete solution |
| R5-09 | Daily/strategic summary adds losses to tactical event again | **Source-exclusive read-only projection** | K-ACTOR actual disability/ammo; K-TIME original event | Tests 127–128, 133 |
| R5-10 | A combat incapacitation counted as a death | **Separate status semantics** | K-ACTOR condition; MED profile for injuries/deaths | No mortality inference in fixture |
| R5-11 | Multiple reports count as multiple occurrences | **Separate information from effects** | K-INFO reporting, physical owners unchanged | Tests 129, 134; real report delivery/latency unimplemented |
| R5-12 | Strategic cohort includes named actor already simulated locally | **Reject overlap, do not infer residual casualties** | K-POP contributors, K-ACTOR named people | Test 130; residual cohort effects unimplemented |
| R5-13 | Query a historical state using current actor flags | **Require checkpoint/replay** | K-TIME journal/history | Test 132; archive checkpoint mechanism not added |
| R5-14 | Internal validator hides wrong ledger | **Add independent invariant auditor** | Reads K-STOCK and event journal only | Tests 136–138; this is *not* an independently developed world executor |
| R5-15 | Monetary/medical/legal authority inferred from a string | **Explicit gap, no fictional authority** | GOV/K-ORG and selected procedures | Not resolved; R4 reference remains simplified |

### No double-ownership

- Physical stock is still K-STOCK. `econ3.losses` is an **accounting channel of the same material owner**, not a tenth K owner.
- `r5_shortfalls` records the outstanding claim and suspended backing for an existing K-WORK activity. It is a toy compatibility record, not a separate national inventory.
- Combat projection derives from committed `simultaneous_exchange` records, K-ACTOR present condition, and the journal. It does **not** write a second casualty or ammunition ledger.
- Independent accounting audit is a validation read, not a second source of physical truth.

## 4. Executed synthetic fixture — national physical loss and tactical continuity

**Source:** `runtime/run_round5_fixture.py` and `results/round5_loss_and_scale_fixture.json`.

Initial: 1,200 people (six named and 1,194 residual), 1,000 currency units, 300 kits, farm with 12 physical seed units, two local jobs starting at time 8, and two fully specified starting ammunition allocations. Rates and amounts are synthetic fixture constants only.

At time 9 a supported test fire destroys 9 seed units, **without canceling the original four-unit farm reservation claim**. The resulting physical seed is 3; the farm job is marked `suspended_unallocated`, its pre-loss claim of 4 preserved, and backing set to 0 pending requalification. There is a one-unit original backing shortfall; the three surviving units remain unassigned, not automatically credited to one claimant. Consumed seed remains 0 and crop production remains 0. A tax claim is assessed but not paid. Two competing treasury requests totaling 800 from a 600-unit treasury are deferred. A same-time farm-seed dispatch is separately held for causal-order proof; no loading is assumed to have occurred before the fire merely from event-ID order.

At time 12 the independent kitchen completes 12 meal units; farm completion is rejected/deferred as unqualified. The separate kitchen consumes its qualifying pre-reserved ingredients, which were not damaged by the farm-stock event.

At time 13 a fixed-result synthetic tactical engagement expends **three** ammunition units (two from the first named actor and one from the second) and incapacitates the second actor. At times 14 and 15, an engagement summary and report are recorded. A read-only single-actor and two-actor strategic projection both indicate exactly **one** disabled person, with the same combat source ID. Neither claims a death. No projection changes the world checksum. The reported information does not create physical injury a second time.

Final invariant checks: population 1,200; total cash 1,000; kits 300; material identities equal opening + produced − consumed − lost; tested actors retain source-supported remaining ammunition. Save and load via the **same** R5 reference implementation yield matching checksums. A separately written **invariant audit**, using its own accounting formulas, cross-checks loss totals against original event journal entries and ammunition expenditures against the source attacks; it is not an independent implementation of the simulation rules.

## 5. Executed tests and evidence boundaries

Command, from `runtime/`:

```bash
python -m unittest -q test_unification test_economic_integration test_selective_and_scale test_loss_and_scale
python run_round5_fixture.py
```

Result: `Ran 138 tests` / `OK`. Tests 109–126 cover loss, reservation claims, suspended work, independent jobs, ambiguous same-frontier stock operations, aggregate loss claims, transit safe refusal and conservation. Tests 127–135 cover tactical/strategic projection, reporting as information, actor exclusion, historical-state refusal, idempotent read-only views and save/load. Tests 136–138 are separate invariant-audit checks, including deliberately tampered loss data.

**Interpretation:** Unit-test count is not a count of end-to-end accepted scenarios. CE-HZD-R5-07 (actual cargo-loss reconciliation), CE-HZD-R5-08 (work restoration), and CE-MIL-R5-14 (autonomous multi-month, dual-scale world) remain **not executed**. All other acceptance cases have bounded evidence for only listed properties. No human playtest or calibration is claimed.

## 6. Newly identified defects and limitations

**R5-D01: Work interruption is conservative but incomplete.** Affected jobs are prevented from completing; the fixture does not settle the actual partial labor and input consumption before the disruption, restore backing, or select revised completion times. This avoids fictional full output but is not yet a qualified work recovery system. Actual obligations and entitlements remain unresolved.

**R5-D02: Source time versus observation time.** The fixture supplies measured loss and effective time as premises; it does not independently verify that the observer knew at that moment, or that the event was causally prior to another physical transfer. Same-instant overlapping transfers are held, but the scheduler needs owner-certified stage ordering and evidence admission.

**R5-D03: Transit loss unsupported.** The adapter raises an invalid-event exception when loss targets `transit:<shipment>` with real cargo. This is the safe bounded outcome, not a model for damaged cargo or shipwreck. A specialist must reconcile actual survivors, shipment obligation and destination receipt.

**R5-D04: Footprints remain hand-authored.** The R4 selective coordinator's conservative key graph persists, including global barriers for unknown operations. It does not qualify every indirect resource, actor and institution subscriber or guarantee maximal parallelism.

**R5-D05: Fixed combat is not a model.** The tactical fixture uses an externally supplied `disable` or `none` effect and a synthetic ammo debit. It does not simulate projectiles, armor, injury severity, mortality, combat readiness or soldier training. It verifies single-source accounting only.

**R5-D06: Cross-scale views do not execute residual world activity.** They read named actors and source events only; there is no multi-month residual-cohort engine, no simulated training/production between views and no independent second simulator. Current state can be used only for current as-of views; past-state requests correctly refuse unless an archived checkpoint exists.

**R5-D07: Authority and status classifications still incomplete.** R4 deferral stores validation-failed groups under a coarse classification. R5 distinguishes one same-time causality case explicitly, but it does not solve resource arbitration, legitimate authority, claims ranking, appeal procedures or fact-admission workflows.

**R5-D08: Physical-loss coverage is stationary stock only.** The conservation channel assumes integer units, existing physical inventory, and explicit qualified loss quantity. It does not cover component damage, recoverable salvage, contamination, fractional goods, uncertain loss estimates or losses exceeding the observed stock due to erroneous pre-existing state. These need parent mechanism or specialist profiles as appropriate.

## 7. Specifications, interfaces and receiving requirements

The rebuilt R5 specification adds proposed subsections `11.R5`, `35.R5`, `62.R5`, `91.R5`, `109.R5`, `117.R5`, `122.R5` and `124.R5`; the R4 paragraphs remain intact. Fourteen R5 acceptance scenarios are appended to the complete Core candidate; none is silently elevated to an adopted requirement. The R5 binding proposal preserves all nine K owners and twelve previously proposed domains.

Before selection: certify domain owner footprints, source clocks/causal stage, actual loss and recovery interface, incident observation and transmission, arbitration authority, material reservations, operational work suspension, tactical effect and report provenance, verified named-actor exclusion and historical checkpoints. Require active receivers—including Military, Roman, Space, Fantasy, PAF, Shinobi and AST—to confirm whether the new procedures duplicate or contradict existing specialized behaviour. A full release must have a selected hash manifest and an independent implementation comparison.

## 8. Calibration needs

- **Production:** work-unit basis, supported input consumption before a disruption, partial output, wastage, restarts and finite labor availability.
- **Logistics:** transport location, partial cargo loss, dispatch and receipt, damage, salvage, reservations and replacement.
- **Medical/combat:** actual effect adapters for injuries, incapacity, fatalities, protective equipment and ammunition expenditure.
- **Civilization:** group contributor partition, autonomy, recruitment and economic responses, strategic process rates and long-term population outcomes.
- **Information/authority:** legal decision validity, causal observation and report latency, audit challenges, claims and resolution.

No general probability or rate has been assigned by R5.

## 9. Migration, provenance, and final disposition

- Selected `IRGS-CORE-3.2` stays selected; no override, new engine pin, campaign restatement, replay, manual ledger adjustment or automatic migration has been made.
- Core 3.3 R5 is a complete **candidate** rather than a patch. R4 and the selected Core 3.2 are preserved in `sources/`.
- Military Slim 1.2 and Roman Slim 1.2 retain their prior proposed/accepted workshop statuses respectively; historical/genre models are not discarded.
- No migration procedure may infer that a saved R4 reservation should be suspended retroactively: only a *future* incident under a subsequently accepted profile can produce that state change without explicit user-authorized reconstruction.
- R5 document and binding are hashed in the manifest; archive verification is for bytes/structure, not proof of simulation realism.

**CMRR decision:** **Resubmit R5 for review; do not adopt.** The principal architectural improvement is explicit owner-preserving shock reconciliation with continued independent civilian activity and unchanged physical source identity across tactical/strategic views. The principal blockers are true work-interruption settlement, independently verified causal event ordering and multi-scale world execution.
