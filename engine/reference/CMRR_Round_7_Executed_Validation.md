# IRGS Core Unification — Round 7 CMRR: Qualified Work Frontiers and Physical Intermediates

**Status:** Proposed reference implementation / unselected candidate; **not** an adopted Core release, calibrated economy, verified independent game engine, legal or work-evidence validator, or gameplay playtest.  
**Review date:** 17 October 2026 (user-local).  
**Selected parent:** Core v3.2 maintenance release. **Candidate predecessor:** Core v3.3 R6 (proposed, not selected). **Receiving candidate:** Core v3.3 R7.  
**Migration effect:** None. No campaign state, adopted source, law or authority has changed.

## Purpose and acceptance question

R6 introduced evidence-backed partial work but *refused scheduled execution* for new milestones because its R4/R5 coordinator could not reliably identify their reads and writes. It also could not represent physically produced but **not yet accepted** intermediate goods. R7 addresses these two bounded gaps without moving source ownership out of K-WORK/K-STOCK/K-INFO or inventing a universal manufacturing process.

**Question 1:** When R6 milestones, supply movement, losses and civil-institution events share one event frontier, can supported independent events proceed while disputed dependencies remain unresolved, without lexical event-ID winners or double production?  
**Question 2:** Can raw material become identifiable physical WIP, suffer loss, be inspected/rejected, and yield qualified salvage **without** counting a completed saleable item or reversing already consumed inputs?

## 1. CMRR bidirectional source inventory

| Source | Scope and authority | Carried to R7 | Reconciliation action |
|---|---|---|---|
| Selected Core v3.2 | Adopted/selected parent, 9 K-owners, Core resolution and event invariants | Exact copy in `sources/` | **Retain.** No selection changes |
| Core v3.3 R6 complete candidate | 124 sections; social/military unification; R4 component processing; R5 losses; R6 milestone/settlement | Full exact R6 candidate under `sources/` | **Revise/extend**, not overwrite or treat as adopted |
| Round 6 validation and binding proposal | 165 tests and 18 R6 proposed acceptance requirements; selected campaign pins untouched | R6 documents retained | **Preserve provenance.** R7 evidence adds, never substitutes for it |
| `r6_work.py` | Explicit direct milestone events, disabled for R6 scheduler | Entire old runtime preserved unchanged | **Extend:** R7 optional scheduler dispatches through R6 adapter without changing legacy R6 mode |
| `r5_hazards.py` | Supported physical loss; underbacked reservation and claims; risk of same-time causal uncertainty | Original code retained | **Compose:** actual WIP stock loss reconciles physical lot quantity without presuming inspection or accepted goods |
| `selective_coordinator.py` | R4 bounded component selection and original deferred claims | Original code retained | **Reconcile:** independent R7 footprint grouping reuses existing state owners; conservative conflict handling |
| `economic_extension.py` | Physical stocks, reservations, transit, work/household needs, cash/tax claims | Original code retained | **Retain:** WIP is a physical stock at a real location; no new inventory owner |
| Military Slim v1.2 | Proposed military specialist source and inheritance | Exact source retained | **Retain specialist work.** MIL cannot count WIP as issued equipment by default |
| Roman Republic Slim v1.2 | Accepted workshop reference for Roman-specific legal and historical application | Exact source retained | **No Roman mutation.** Shared labor/custody semantics remain Core-owned |
| Prior R6 `sources/` | Historical R5 candidate, binding, selected parent, specialist sources and Roman setting | Entire directory copied to `sources/R6_preserved/` | **No removal or silent history loss** |
| `test_*.py` suites 1–6 | 165 existing unit cases | Preserved byte-for-byte | **Regression rerun** under R7 package; no test renumbering/reinterpretation |

**Reverse comparison:** R7 adds nine normative subsections to §§11, 35, 62, 91, 109, 114, 117, 122 and 124 plus 18 new Appendix C acceptance specifications. Sections 1–124, Appendices A–D, all nine source-owner identifiers, all twelve proposed domains and all predecessor test implementations remain present. Material quality, finished acceptance and salvage are **not** new K-state owners: they are existing physical lot state, work procedure and source information.

## 2. CMRR reconciliation matrix

| ID | Conflict / lost function risk | Decision | Owner and causal rationale | Evidence / boundary |
|---|---|---|---|---|
| R7-01 | R6 milestones bypass/select different event scheduler | **Combine:** R7 dispatches new operations through the R6 tracked-work adapter | K-TIME orders, K-WORK commits, existing R6 milestone identity | Tests 166–167; not generic runtime certification |
| R7-02 | Parallel authorized work unfairly halted by a disputed claim | **Retain and refine** selective independent components | Pre-frontier footprints, conservative conflict grouping; no lexical winner | Tests 168–170, 189–190 |
| R7-03 | Same-time physical loss and work accepted in arbitrary order | **Split:** supported physical occurrence, unexecuted conflicting work | K-STOCK loss is a physical event; work interval/claim needs proof of causal ordering | Tests 171–172, 193; external evidence not authenticated |
| R7-04 | Candidate frontier commits some effects before discovering impossible stock loss | **Revise:** construct the entire current frontier on a candidate state and commit only after preflight/integrity | Avoids corruption and half-committed frontier on false combined loss evidence | Test 196 |
| R7-05 | R6 fixed-rate output treated as a universal manufacturing lifecycle | **Reject** generic inference; **add** opt-in content-profile operation | K-WORK governs selected process; no Core universal yield, labor, energy or loss multiplier | Tests 177–188; fixture-only synthetic conversions |
| R7-06 | Unaccepted product silently increases army/market finished inventory | **Split** WIP, quality finding and completed acceptance | K-STOCK physical intermediate distinct from finished stock, K-INFO inspection, K-WORK disposition | Tests 178–182, 195 |
| R7-07 | Fire destroys part of WIP but document still claims all units exist | **Reconcile** actual lot and loss event | Same physical location ledger and tracked lot quantity; no retroactive raw-input refund | Tests 184–186, 197 |
| R7-08 | Salvage creates full finished product or material without actual surviving quantity | **Require** reject assessment and selected salvage yield | Recovery is a new physical transformation of surviving intermediate stock; no free reproduction | Tests 182–186, 198 |
| R7-09 | Future revision of recipe changes past manufacturing yields | **Freeze** selected source profile on each workpiece at fabrication | Per-instance profile snapshot/digest prohibits retroactive profile effects | Tests 202–203 |
| R7-10 | Unknown extension op assumed safely disjoint | **Retain conservative barrier** | Missing footprint is not proof of independence | Test 199; cross-engine audit not done |
| R7-11 | Save/reload may duplicate deferred events, WIP or material | **Retain source identities and replay** | Journal event ID, processed set, actual stocks, source-tethered workpiece | Tests 176, 194, 200, fixture |
| R7-12 | Wages, claims and inspection costs become free because not represented | **Defer** unselected rate/time/energy/labor model | No invented quantities; record gap explicitly rather than asserting zero physical cost | **NOT fully executed:** proper industrial process and law needed |
| R7-13 | Strategic view re-adds WIP as an accepted item | **Retain exclusive source projection** | Same actual K-STOCK quantities; reports do not manufacture stock | Tests 178, 195; no independent month-scale strategic executor |

## 3. New bounded operations and minimal source records

**Tracked work:** `start_tracked_job`, `record_work_milestone`, `settle_disrupted_job`, `start_continuation`, `finalize_tracked_job` retain R6 record semantics. In R7, these operations can enter the optional `R7World` scheduler; `R6World` itself remains unchanged and continues to prohibit their scheduling.

**Intermediate physical goods:** `make_intermediate`, `inspect_intermediate`, `accept_intermediate`, `salvage_intermediate` are narrow, optional fixture operations. They use actual `econ3` material locations, opening stock, consumed/produced/lost quantities, and a separate item record that is an illustrative K-WORK/K-STOCK view **rather than a new authoritative owner**.

Each item includes source event ID; site, actual intermediate and quantity; original selected source profile **snapshot/hash**; status; assessment/inspection IDs; loss event IDs and quantities; and final disposition reference. Accepted or salvaged items have no remaining intermediate stock. A changed future model definition cannot silently change an already produced item. In the bounded profile used here, 3 iron units are transformed into 2 unaccepted workpiece units, a later measured loss destroys 1, and a qualified synthetic assessment recovers 1 scrap unit. **Zero finished shields** are credited.

**Scheduler:** Gather eligible same-time proposals, calculate pre-event footprints, construct transitive conflict groups, execute supported disjoint components, preserve contested groups as unexecuted, recognize supported physical loss, and atomically swap a fully validated frontier. Event IDs affect deterministic serialization for commutative physical loss sources, not scarce-resource allocation. Unknown operations are conservatively deferred; new causal stages require genuine ordering evidence. For this bounded harness, aggregate stock accounting is additive and the actual scarce pool uses site+material keys; this grouping is **not** mechanically checked against every possible indirect cross-engine effect.

## 4. Executed mixed-institution fixture

The R7 fixture supplies fictional law, work attestations and rates. There are 1,200 people; an original farm shift, kitchen, tax authority, external warehouse and metalwork source all operate against one world state.

| Frontier | Event | Actual state consequence |
|---|---|---|
| 8 | Farm tracked job and kitchen legacy job already started | Farm reserves inputs; neither produces by clock alone |
| 9 | Farm one-hour certified milestone | 1 seed consumed and 3 grain accepted |
| 10 | Warehouse/farm-region seed fire and separate tax assessment | 9 seed physically lost; farm suspended; tax **claim** assessed, no money received |
| 11 | Farm work/disruption settlement | 1 worker-hour verified; 3 hours remain, separate unresolved wage-entitlement interval |
| 12 | External replacement dispatched, kitchen completed, metal intermediate fabricated | Physical replacement enters transit; 12 meals accepted; 3 iron converted into 2 unaccepted units |
| 13 | Replacement arrives; new farm shift made; intermediate loss occurs | Farm's seed restored prospectively; 1 unfinished unit destroyed, **not** a finished article |
| 14 | Authorized farm continuation and intermediate inspected/rejected | New work reserves 3 seed; inspection itself creates no shield or scrap |
| 15–17 | Farm three independent certified milestones | 3 seed used and 9 more grain accepted |
| 18 | Farm final settlement | Total farm grain 12; certified wage liability 8; original loss/claim history retained |
| 19 | Authorized salvage | 1 physically surviving WIP converted into 1 scrap unit; no shield |
| 20 | Review frontier | Snapshot/replay and read-only audit |

**Conservation:** Seed 16 opening = 4 actually consumed + 9 physically destroyed + 3 physically remaining. Iron 10 opening = 3 consumed + 7 remaining. Intermediate production 2 = 1 physically lost + 1 consumed in salvage; finished shield production = **0**; recovered scrap = **1**. Separate kitchen produces 12 meals. Population 1,200, cash 1,000 and depot kit total 300 are unchanged in the fixture. Wage liability is not paid cash; tax assessment is not tax receipt.

`run_round7_fixture.py` recorded **17 committed scheduled events**, zero deferred in this fully staged fixture. This does **not** suggest that every conflict is resolvable automatically: contested same-time milestones, overlapping production, unsupported methods and ambiguous loss order are separately verified to remain unexecuted.

## 5. Tests, verification, provenance and rejected claims

Execute from `runtime/`:

```bash
python -m unittest discover -p 'test_*.py' -q
python run_round7_fixture.py
```

**Executed:** 203 Python unit tests passed: 165 inherited R1–R6 tests plus 38 new R7 tests numbered **166–203**. The 18 Appendix C R7 acceptance specifications are **not 18 fully certified engine passes**. `r7_audit.py` separately recomputes materials, journal-linked loss and WIP provenance using the same program state, not an independent engine. `results/` contains actual test and scenario outputs and the SHA-256 inventory.

**Not proven:** Real process physics, suitability of fabrication yields, scrap/material quality, operation energy consumption, environmental effect on industrial process, actual employee labor hours for the WIP conversion, fire causality and timestamp evidence, legal authority of inspectors, lawful wages/salvage ownership, module-supplied footprints, cross-engine independent replay, full national economic mobility, multi-month autonomous simulation, physical military readiness, calibrated play balance and actual playtesting. `R7World` is an optional research adapter, not production-ready software.

## 6. Removals and changes

**Preserved:** All prior Core sections 1–124 and Appendices A–D, R1–R6 accepted/unaccepted status distinctions, nine authoritative owner IDs, twelve proposed domains, original 165 regression tests, Military/Roman reference material, original R6 adapter and all existing selected pins.

**Added:** Candidate §§11,35,62,91,109,114,117,122,124 R7 subsections; 18 declared acceptance requirements; `runtime/r7_frontier.py`, `runtime/r7_audit.py`, `runtime/test_r7_integration.py`, `runtime/run_round7_fixture.py`, and evidence outputs; source-profile snapshot/digest and frontier candidate-state protection.

**Nothing adopted, deleted, deprecated for active campaigns or silently reassigned.** R6's *deliberate prohibition* of milestone scheduling still applies to an R6 deployment; R7 proposes qualified scheduling only when the R7 adapter is explicitly selected. Existing claims or accepted goods are never changed retroactively.

## 7. Blockers, calibration and migration impact

1. **Owner/footprint coverage:** Certify every operation's direct and indirect reads, writes, capacity and institutional prerequisites; hand-written tokens are insufficient for broad cross-module reliance.
2. **Causal-stage and evidence authority:** Distinguish occurrence from observation/transmission/receipt; support disputed physical sequences, qualified decision rights and cause-specific requalification rather than generic defer-and-forget.
3. **Workpiece physical fidelity:** Calibrate selected assembly/rework/scrap/quality, usable components, partial and nonlinear output, labor and energy, waste and environmental exposure profiles; do not universalize one fixture yield.
4. **Production and wage law:** Identify compensation for unassessed work and authorized work conditions by period/institution. No default rule may force historical or modern laws into another setting.
5. **True strategic continuity:** Execute independent autonomous weeks/months, military requisitions, production constraints, population shifts, reports and liabilities against one source ledger, with secondary implementation parity.
6. **Runtime hardening:** Structured typed errors, persistent deferred-resolution workflows, immutable external source version registry, property-based interleaving tests, independent state verifier, corruption/fuzz tests and transaction logging.

**No existing campaign migration.** A future prospective migration must explicitly map already accepted work, material inventory, work-in-progress, sources, reservations, wages, decisions and time stamps without doubling any effect. Unsupported historical completion remains unknown. Core v3.2 remains selected until user acceptance and a qualified deployment binding update.

## Provenance and disposition conclusion

R7 is a **positive bounded integration result** for event scheduling and work-in-progress preservation, not a completed Questner-class game runtime or genre-wide simulation engine. The next logical gate is independently qualified owner/footprint inference and disposition-recovery decisions across ambiguous causal order, followed by sustained autonomous strategic execution. Resubmission alone **does not change authority status**.
