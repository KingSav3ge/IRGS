# Bounded player equipment action — implementation scope

Implemented 2026-10-21 against the unified D1 source. This is a narrow Core 3.3 runtime increment for DEV-01–DEV-04, not adoption of the complete C2 action system. Host persistence and the Solo interface qualify their own connected behavior separately.

## Supported operation

`IRGS_3_3/runtime/player_actions.py` supplies `execute_player_equipment_issue`, registered in `core_world.py` and dispatched inside the existing cloned Core transaction. The operation reuses `military_issue_equipment` and its conserved stock transfer; it does not create an inventory, institution, authority, recipient or historical starting fact.

The caller explicitly selects an existing received equipment order with `{kind: "issue_equipment", order_id: "..."}`. Quantity, material, depot and recipients come from that structured order. Client-supplied replacement quantities or recipients are refused. Free text is not parsed into an equipment operation.

Execution checks:

- The selected actor is actually controlled and exists at the saved registry coordinate. If a temporal registry exists, current eligibility and control are revalidated for the selected scenario and entity. A stale player list cannot override revoked eligibility or a dissolved controlling faction. A faction representative uses the faction's actual policy rather than unrelated individual eligibility.
- The military or Roman receiving profile is selected; the order was actually received by that actor, is unexecuted and unrevoked, and its causal deadline is still valid.
- `order.authority_ref` names a real, active, sourced `r9.mandates` entry for that actor covering `military_issue_equipment`. Its effective coordinate and optional validity bound must permit execution. A title, background claim or arbitrary reference string is insufficient.
- Every named recipient still exists and the conserved stock is sufficient. Failure after an intermediate scratch transfer rolls back all recipients and the order's executed flag.

The mandate is an explicit source selection using the existing R9 ledger, not independent proof of real historical legal authority. A legacy save without a temporal registry retains its actual player-control list, but still requires the explicit received order and mandate. This increment installs neither missing registry policies nor authority into existing saves.

## Observation, outcome and persistence boundary

The public engine function `execute_equipment_action(world, event_id, actor_id, action, instruction_ref)` observes the actual new Core handler with R9 before committing. Authorization, current-control, existence, order, decision and stock reads are in its private certificate. Instrumented and ordinary execution must agree. The returned outcome reports the committed transfer quantities and the order fulfilled; it does not disclose remaining stocks or hidden rejection facts.

The causal event coordinate is not elapsed time. The operation does not advance the civil date, supply an action duration, produce narration or select a dice rule. A successful fresh action returns its outcome, event receipt and dependency evidence. The host must atomically save that result and the changed world before acknowledging it. Request recovery occurs before calling the fresh-action function again; reusing its event identity cannot create another transfer. Native Core replay with the original frozen event is also effect-free.

An invalid action raises `PlayerActionUnavailable` with a generic public message and private failed-attempt reads. Its writes are explicitly empty; scratch writes are labelled `attempted_writes`, and it is not a successful certificate. The current host rejects such an attempt without a save write. A durable pending/deferred-attempt workflow with later phase continuation is still future C2 work; this increment does not claim that every failed request is accepted or scheduled.

## Received choices and information limits

`equipment_options(state, actor_id)` offers only this actor's received structured equipment orders. It does not inspect hidden depot quantities, mandate validity or other actors' names to decide which choices to display. A stale received instruction can therefore remain attemptable while execution returns a generic failure. This avoids turning the menu into an oracle about private stocks or uncommunicated authorization changes. Current player control is still required.

Actual stock inspection remains subject to the app's explicit information grants. A successful issue establishes that the reported transfer occurred; it does not automatically grant ongoing inspection rights over every involved inventory.

## Observer correction and remaining certification limits

The existing observer used any ancestor named `__init__` to suppress conservative list-write reservations. An unrelated caller constructor, including `unittest.TestProgram`, could consequently change the reported footprint. Removing that context dependence exposed false conflicts from recording every list read as a write, including independent cash transfers and institutional decisions.

`r9_runtime.py` now wraps lists in `TracedList`. Indexing, membership, ordering, length and iteration record whole-list reads. Standard mutators, including append, insertion, deletion, slice assignment, sorting and in-place operations, record whole-list writes. Nested elements remain instrumented; list position changes preserve held child references and update their paths. Actual state differences remain the write backstop for successful execution. Read-only control, registry and authority lists no longer invent writes.

Direct invocation and invocation under an unrelated constructor produce identical certificates. Construction and transaction cloning do not invent domain reads, and validator list mutations are refused. Separate-stock equipment operations have equal physical results in both serial orders and in the supported simultaneous frontier. Existing disjoint-cash and sustained institutional checks pass without changing those tests or their expected behavior.

Granularity remains conservative: a list read depends on the whole list, and any mutation conflicts with another read or mutation of that list. Fine-grained index independence, arbitrary-plugin safety and complete cross-engine branch certification are not claimed. Explicit bypasses of Python overrides are outside the reviewed-handler contract; successful state changes still receive the actual-diff backstop.

## Verification references

`IRGS_3_3/runtime/test_player_actions.py` has 24 bounded qualification tests, and `test_r9_collections.py` has nine collection-observation tests. All 33 executed successfully on 2026-10-21. The existing `test_r9_runtime` and `test_strategy_rights` suites also passed all 48 tests, including disjoint cash transfers and the fourteen-day institutional fixture. Relevant coverage for the separate C2 execution ledger is:

| C2 reference | Engine evidence | Limit |
| --- | --- | --- |
| A01 | `test_success_is_one_committed_conserved_effect_without_elapsed_time`: ten opening kits become depot nine and recipient one, with linked outcome and receipt. | Host persistence is qualified separately. |
| A02 | `test_native_core_replay_keeps_frozen_event_without_repeating_effects`; second action after save/load is also exercised. | Exact request-result recovery is a host responsibility. |
| A03 | `test_caller_cannot_change_quantities_or_recipients` and caller-detachment test. | Reused request ID with changed text is a host check. |
| A06–A08 | Noncontrolled actor, revoked current eligibility, selected faction representative, dissolved faction and dissolved control actor cases. | This increment rejects unavailable operations; it does not implement the entire pending-authorization lifecycle. |
| A09–A11 | Received-order validity, actual mandate validity, insufficient stock with multi-recipient rollback, and recipient dissolution. | Public rejection is generic to preserve information boundaries; durable unresolved requests are not implemented here. |
| A12 | `test_competing_received_orders_have_no_simultaneous_arrival_winner`. | Existing frontier retains both requests; the new Solo route submits one supported action at a time. |
| A13 | `test_separate_stock_effects_agree_and_observed_reads_allow_independence`. | Equal physical results in either serial order and the named simultaneous fixture; no broad independence claim. |
| A14–A15 | Simultaneous current-eligibility revocation and recipient dissolution conflict with an issue. | Named paths only; no claim that every handler branch is qualified. |
| A21 | Received choices ignore hidden stock, mandate validity and unrelated identities/directives. | Host/player-projection checks are separate. |
| A22 | Constructor-context parity, construction/clone checks and `test_r9_collections` read/mutator/negative-membership/nested-reference/validation cases. | Whole-list granularity; no arbitrary-plugin or exhaustive-handler claim. |

The immutable C2 source inventory is unchanged. These references are scoped implementation evidence, not a declaration that all 121 acceptance cases passed. Sustained institutional autonomy, movement, elapsed phases, dialogue resolution, restore fencing, multi-process persistence and general freeform action resolution remain outside this increment.
