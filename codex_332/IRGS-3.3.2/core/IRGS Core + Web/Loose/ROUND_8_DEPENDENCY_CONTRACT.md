# Round 8 — observed dependencies and strategic continuity

**Proposed / unselected, 18 October 2026. Core v3.2 remains selected. R7 and R8 are candidates.**

## What counts as evidence

A manually declared footprint is a hypothesis. An execution certificate identifies the exact pre-state hash, event payload, runtime source hash, observed reads and write intents, and actual changed paths. It is evidence for that execution only. A union of observed paths is a coverage report, never a reusable permission to skip observation. Neither test success nor a document hash selects a new Core.

R8 observes the existing shared `World._operate` and economic helper code through a mapping access boundary. It does not substitute a second economic or military state. A speculative copy is discarded; the existing R7 dispatcher validates actual operations on a transaction copy and the live state is swapped only after the entire selected frontier succeeds. Operation results must agree with the observed execution before qualification. R5 loss, R6 tracked work and R7 fabrication are deliberately refused by this new frontier until their full dispatch paths are instrumented. Their old direct APIs remain inherited candidate behavior.

## Dependency rules

1. Read paths include decisions and prerequisites, not just quantities eventually changed: actor condition/location, qualifications, institutional mandates, received orders, recipe/profile values, reservations, capacities and work windows.
2. Missing-record lookups are reads. Inserting the missing record conflicts with them. Enumeration reads a whole subtree: inserting a new reservation or active job conflicts with a scan that previously found none.
3. Container navigation records existence without assuming all child values were read. Whole-record replacement/deletion conflicts with descendant accesses. Paths are structured tuples, avoiding colon-concatenation ambiguity.
4. List access conservatively reserves the entire list for reading and writing because inherited handlers mutate lists directly. This can overblock; it cannot be advertised as exact leaf-level access. Same-value mapping writes still count as writes.
5. Read/read overlap is allowed; write/read and write/write overlap create a conflict. Additive accounting is not presumed commutative. Shared material totals can therefore block otherwise separable jobs until a qualified reduction protocol exists.
6. Every proposal is observed against the same immutable pre-frontier snapshot. Unknown or invalid proposals conservatively block the batch; observed conflicting proposals remain unexecuted, while disjoint proposals may commit. IDs never choose a scarce-resource winner.
7. Observation is rerun at each commit attempt. A supplied certificate with different state, code, parameters or access sets is rejected. Frontier IDs are unique and timestamps identical. Old processed IDs are not treated as fresh proposals.
8. Global invariant validation occurs on the assembled candidate. Its broad reads are not interpreted as resource consumption. If combined validation fails, the entire live frontier remains unchanged. Clock, processed identities and journal are coordinator bookkeeping, explicitly excluded from domain interference comparisons; no domain handler may use them to hide resource effects.
9. The current boundary is reviewed deterministic, in-process JSON handler code. It is not a security sandbox: arbitrary Python can evade proxies, consult globals, perform I/O or use nondeterminism. Such adapters cannot earn certification by self-declaration. Production plugins require a mediated state API, restricted external effects and complete adapter dispatch instrumentation.
10. Rejected/contested requests preserve original intent and reason. The strategic executor stores these in decision records. Standalone `frontier` callers must persist its returned deferred records; it is not yet a durable queue or adjudication service. Any later grant requires a new genuine decision and revalidation, not backdating.

## Strategic execution

The bounded controller generates proposals from current records at six reviews per day, with hours retained on the same clock. It advances a kitchen business, a household, a tax institution and a military institution. It creates future work commitments, starts feasible work, completes it, provisions meals, records wage liabilities, assesses and pays taxes, and enrolls/equips one authorized member. There is no prewritten 90-day action list. Inputs, disablement, claims and membership change later choices.

The explicitly selected synthetic policy is stored with its hash in `r8_strategy`. Each review records policy/code hashes, source-state hash, actual decision-read paths, proposals, committed IDs and unresolved proposals. These are planning/audit records, not duplicate cash, population or inventory. No player choices are delegated. Mutating the selected policy is rejected; prospective rebinding needs a future procedure.

This is bounded reactive autonomy, not open-ended strategic intelligence. The recipe uses inherited synthetic legacy job completion and does not fabricate R6 work evidence. Wage liability is not payment. Food provisioning is not a complete physiology model. There are no calibrated seasons, supply markets, military readiness, legal reasoning or independent institution beliefs. The planner currently sees authoritative fixture state; recipient-specific information constraints remain a gate before deployment.

## Cross-engine qualification gate

Military, Roman, AST, Fantasy, PAF, SNWE and Space documents are source references with their own retained statuses. Each engine must bind an executable operation to these shared owners or provide a separately instrumented extension. Reusing the same Core implementation under different labels is not independent engine validation.

For each native operation require: source and profile version; all supported branches; actual access observations; negative/phantom/alias/capacity tests; all relevant cross-engine pairings and perturbations; independent serial-order comparison; joint invariant validation; unknown-external-effect rejection; save/replay; and reviewer disposition. Current native certification is **OPEN**, not passed. `results/r8_operation_inventory.json` describes exercised shared handlers only. Engine-source hashes and the gate matrix are separate evidence.

## Acceptance register

| Gate | R8 evidence / disposition |
|---|---|
| Dynamic shared-handler observations | Executed cases for 37 shared handlers; path unions and example certificates |
| Hidden institutional dependencies | Equipment issue vs enrollment regression detects membership-list interference |
| Missing keys and phantom insertions | Executed negative lookup and enumeration tests |
| Scarce pool and no ID winners | Executed conflict/defer and independent-component tests |
| Cached certificate invalidation | Executed stale-state and tampered-access tests; code is hash-bound |
| Serial-order comparison | Executed cash-pair permutation comparison; not all operation pairs |
| Atomicity and source isolation | Executed invalid-operation/source-preservation tests; candidate validation |
| Sustained autonomous continuity | Reproducible 90-day four-institution fixture and 45-day save/reload comparison |
| Constraint adaptation | Resource-exhaustion and disabled-worker tests |
| Every native engine operation/branch | OPEN; source mapping is not executable certification |
| R5/R6/R7 extension dispatch | OPEN; rejected by the new selective frontier |
| External effects, independent runtime, deployment | OPEN; no certification or adoption claimed |

The next implementation priority is a mandatory state-access API spanning the complete R5–R7 dispatcher and native engine adapters. Then qualify adversarial interleavings for shared labor, space, authority, information and logistics; only afterwards broaden autonomous goals and information-limited decision making.
