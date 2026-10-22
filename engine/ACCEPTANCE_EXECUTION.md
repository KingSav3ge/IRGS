# Scoped C2 implementation evidence — Action 1

2026-10-21. This execution ledger is separate from the immutable 121-case design inventory. The inventory remains `REQUIRED_NOT_EXECUTED`; it is not rewritten as a blanket pass. The implementation record gives precise engine test references. The rows below identify covered properties and outstanding parts, not full certification of every referenced C2 case.

| C2 references | Executable evidence | Qualification boundary |
| --- | --- | --- |
| A01 | `runtime/test_player_actions.py`: ten kits become nine plus one with linked outcome; Web `tests/test_equipment_action.py`: actual HTTP outcome, receipt and player chronicle. | One existing equipment operation, selected control and sourced mandate; no invented historical setup. |
| A02–A04 | Native frozen-event replay; HTTP identical retry, new Store reload, concurrent retries, changed request text/order/actor, stale new request and fork receipt isolation. | Single host/writer and atomic file replacement; not restore fencing or multi-process/power-loss qualification. |
| A06–A08 | Current player-control, revoked eligibility, faction representative and dissolved control entity tests. | Rejection semantics; complete awaiting-authorization lifecycle remains unimplemented. |
| A09–A11 | Invalid/unreceived/expired/revoked order, invalid mandate, depleted multi-recipient rollback and vanished recipient. | Generic safe rejection without a saved pending failure; the full C2 pending-reason contract is not implemented. |
| A12–A15 | Competing received orders, separate-stock simultaneous and serial equivalence, revocation and dissolution conflict paths. | Named equipment paths and fixture profiles, not all operations or all failed branches. |
| A21 | Received options unaffected by hidden stock/mandate changes; private certificate omitted; actor-scoped outcome and prompt projection. | Successful transfer facts are disclosed, not ongoing stock inspection rights. |
| A22 | `runtime/test_r9_collections.py` plus constructor-context parity: list reads, mutations, nested references, validation and actual-diff backstop. | R9 reviewed JSON handlers; whole-list granularity remains; no arbitrary-plugin or universal fine-grained claim. |

`runtime/response_options.py` and its tests additionally qualify actor-scoped received response drafts, including risky options that are not filtered into guaranteed success. The UI suite verifies draft-only selection, custom editing, scope, recovery and truthful outcomes. Suggestions do not adjudicate combat, select dice, grant feasibility or advance time.

Actual combined full-suite results and their logs are in [integrated main's ACTION1_VALIDATION.json](https://github.com/KingSav3ge/IRGS/blob/main/ACTION1_VALIDATION.json); the engine branch alone does not claim that its older host contains the connected UI. Preserve future case execution results as distinct records with test locations, dates, scope and limitations. Movement, dialogue adjudication, durable phases, restored branches and full institutional execution require further implementations and evidence.

## Opening1 scoped extension

The authored local scene extends repeated action, exact retry, actor knowledge, conserved transfer and ordinary movement evidence. Runtime scene/setup tests plus real loopback scene tests cover actual duration, blocked/depleted outcomes, current control, failed persistence and concurrent duplicate. This is one-transaction local duration, not scheduled phases or general C2 completion. See PLAYABLE_OPENING_IMPLEMENTATION.md and OPENING1_VALIDATION.json.

## Rejected dependency evidence extension

Dependency-rejections-1 advances the rejection and conflicting-decision properties associated with A09–A15 and A22 through `runtime/test_rejected_dependencies.py`. The tests cover named backend paths, paired atomic rejection, negative lookups, actual scarce-resource/authority/worker reads, retained unresolved intent and save/load. They do not claim full completion of those C2 cases or a general saved-failure lifecycle for player submissions. See REJECTED_DEPENDENCIES_IMPLEMENTATION.md and DEPENDENCY_REJECTIONS_VALIDATION.json.
