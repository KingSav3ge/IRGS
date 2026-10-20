# Round 8 CMRR — dependency evidence and autonomous continuity

**18 October 2026 · Proposed / unselected. Selected authority: IRGS Core v3.2.**

Round 8 implements an execution-derived dependency gate and a bounded autonomous controller. It does **not** finish certification of every native engine. The distinction is material: 37 observed shared handlers are not 37 certified engine integrations or proof of every reachable branch.

## Source and reconciliation record

| Source/function | Disposition | Reason / resulting behavior |
|---|---|---|
| Selected Core v3.2 and existing engine bindings | Retain unchanged | Authority is explicitly unchanged by this request |
| Complete R7 candidate, runtime, sources and results | Preserve | Prior evidence remains identifiable; no R7 tests are rewritten |
| R7 handwritten footprint inference | Supersede only in opt-in R8 frontier | Actual handler access replaces manually declared scheduling tokens |
| R7 list membership and other indirect reads | Refine | Issue/enrollment regression exposes a missing dependency in old tokens |
| Unknown operations | Fail closed | Cannot infer independence from absent evidence |
| R5 physical loss, R6 work evidence, R7 WIP | Hold for R8 simultaneous qualification | Observing only a base operation would miss adapter behavior |
| Owner state | Retain existing ledger | Transaction copies are ephemeral; strategy records contain references and audit only |
| Household/business/government/military reviews | Add bounded autonomous policy | Actions derive from current means and obligations, not a fixed event script |
| Character concept archive | Retain as visual reference only | Listed PNG members; captions are not instructions, legal facts or runtime state. No visual inspection or character-state import claimed |
| Native genre engines | Source-hash and gate inventory | Documents do not establish native executable coverage |

## Executed checks

The inherited 203 tests passed before modification. R8 adds 26 adversarial and continuity tests, for 229 tests in the combined suite. Actual output is recorded in `results/r8_validation_tests.txt`. An instrumented inherited-suite pass plus explicit escape/order execution cases builds the operation inventory; this is a separate diagnostic pass, not additional independent tests.

Observed records include cash and wages, equipment and membership, actor/legal/custody state, orders and receipt, work and qualifications, site capacities, actual material locations, reservations, recipes, household care and tax claims. Read/write unions identify exercised accesses and retain example event/state/code certificates. They are not static contracts or full branch-coverage claims.

The 90-day fixture, exact quantities, checkpoint parity, committed/deferred counts and final ledger are recorded by `run_round8_evidence.py`. A second scarce-input run demonstrates that later work stops when actual resources run out. Synthetic rates are explicit and are not historical calibration.

**Recorded result:** 540 review ticks, 479 committed institutional operations, zero deferred proposals in this staged fixture, and 1,019 total journal events including reviews. Uninterrupted execution and save/reload at day 45 have identical final checksums. The business produced and the household consumed 270 meals; 60 grain and 30 fuel remain. Taxes actually paid total 26; wages owed but not paid total 90. Population remains 1,200, total cash 1,000 and total kits 300, with one kit issued. The scarce-input ten-day run completed only two jobs and produced six meals, leaving 24 meals of its selected target unmet. No automatic injury was inferred.

`verify_round8.py` independently recomputed material, cash, population and equipment conservation from the saved JSON, checked unique journal/processed identities and all 540 decision ticks, and verified package hashes. These checks passed. It is a read-only arithmetic verifier, not an independently implemented world simulator.

## Limitations affecting acceptance

The proxy is an instrumentation mechanism for reviewed shared handlers, not a security boundary. Lists and structural scans deliberately overapproximate. Domain validation is broad and can reject a candidate batch. The scheduler does not qualify external I/O, hidden globals, arbitrary plugins, all branch paths, every pair of operations or a second independent simulator. Full native engine operation inventories and executable receivers remain unqualified. The strategic controller is a fixture policy with authoritative-state visibility; institution-specific beliefs, broad goal selection, durable adjudication, policy rebinding and R6 evidence-backed production are not implemented.

No accepted campaign is migrated. No selected parent, engine law, historical character state or existing inventory is changed. R7 remains a proposal; R8 adds another proposal rather than adopting either one.

## Reproduce

From `runtime`, using Python 3 without external dependencies:

```text
python -m unittest discover -p "test_*.py" -v
python run_round8_evidence.py
```

From the package root, run `python build_r8.py` followed by `python verify_round8.py` to refresh packaging and check the saved results.

The long fixture performs both uninterrupted and checkpointed 90-day runs. `build_r8.py` packages source hashes, a complete candidate text, binding proposal, coverage matrix and archive manifest. Its relative-path integrity checks verify preservation of the original R7 inputs. Historical R7 result files remain historical and do not describe the R8 runtime.
