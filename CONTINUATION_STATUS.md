# First action and contextual-response increment

2026-10-21. Continues unified D1 with selected executable Core 3.3. Engine/Core changes belong to `3.3.3.E`, website changes to `3.3.3.A`, and the integrated source to `main`.

## Completed bounded milestone

DEV-01â€“DEV-04 implement one consequential Solo action: explicitly execute an existing received equipment order using actual current player control and a sourced operation-scoped mandate. The same Core transaction validates recipients and conserved stock, commits the transfer and marks the order executed. No historical inventory, permission or recipient is manufactured.

The host saves the accepted semantic request, resulting world, outcome, private dependency evidence and public receipt in one atomic save replacement. An identical retry retrieves the accepted result before current-revision and execution checks. Changed identity payloads, stale new requests and foreign character/campaign requests cannot repeat it. Invalid attempts and failed persistence leave the saved world unchanged. The interface displays the committed outcome, preserves a separate unsent draft, survives reload and permits the next action.

This qualifies the single-host, single-writer path. Multi-process coordination, power-loss durability, accepted pending failures, timed phases and restored-branch fencing remain future work. A failed equipment attempt is currently rejected without a new saved request; it is not a scheduled process.

## Suggested responses and custom answers

`receive_response_prompt` records an explicitly supplied, actor-scoped information prompt. Its choices remain suggestions, not feasibility findings or objective world changes. The Solo interface offers those choices and an editable own-response field. Selection copies text into a local draft; only explicit submission records the resulting declaration.

Choices may fail, carry risks or prove unsuitable. Hidden stock, private opponents or uncommunicated permissions do not select a guaranteed winning menu. Explicit combat prompts can provide situational choices; empty combat prompts use tentative generic approaches. Combat and other freeform responses remain unresolved declarations until their domain adjudication exists.

Prompts do not create an encounter, advance time or resolve combat. New historical games are not seeded with invented prompts or equipment merely to display a feature. Multiple equally recent active prompts do not silently acquire a priority from their IDs.

## Dependency work

The new equipment path observes actual current-control, authorization, order, recipient and stock reads. It checks instrumented against ordinary execution and retains actual differences as a write backstop. Competing claims cannot acquire a simultaneous winner through arrival order.

Collection qualification also corrects a caller-context dependency: unrelated constructors must not change observed footprints. R9 now distinguishes whole-list reads from standard list mutations. Reads remain coarse; arbitrary native plugins and every cross-engine branch are not certified by this increment. The separate implementation record and execution ledger identify named evidence and limits.

## Evidence and next work

See [ACTION1_VALIDATION.json](ACTION1_VALIDATION.json) for the actual executed checks, [engine/EQUIPMENT_ACTION_IMPLEMENTATION.md](engine/EQUIPMENT_ACTION_IMPLEMENTATION.md) for engine scope, and [engine/ACCEPTANCE_EXECUTION.md](engine/ACCEPTANCE_EXECUTION.md) for the C2 coverage mapping. The immutable 121-case source inventory has not been rewritten into a passing test report.

DEV-05 is now complete: [the operation register](engine/OPERATION_COVERAGE.md) lists all 168 declared backend/operation contracts, current observations, test identities and explicit gaps. See [COVERAGE1_VALIDATION.json](COVERAGE1_VALIDATION.json). Next: broader collection/failed-branch/conflict qualification under DEV-06â€“DEV-08. Durable phases, movement, dialogue, evolving historical control and sustained institutional autonomy remain on the continuation list. Suggested responses are a universal presentation feature alongside these capabilities, not a separate combat world.

The coverage capture also records 381 refused post-state matches across legacy caller/observer backend selections and 23 failed-probe rollback anomalies. These observations are excluded from qualification, with their named test contexts retained for DEV-06–DEV-08. There are no such refusals in the selected Core observations. These are repeated synthetic observation counts, not player incidents.
