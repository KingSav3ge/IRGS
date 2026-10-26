# Shared Engine systems — API 1

Target: IRGS 3.4.0 development. This API uses one authoritative Core and its existing owners, selected rules and handlers across supported campaigns. It requires no App/Catalog checkout, API token, provider account or inference budget. It implements the [current work order](../COORDINATOR_WORK_ORDER.md); it does not complete all DEV/C2 mechanics.

## Public contracts

| Contract | API | Source/authority |
| --- | --- | --- |
| Actor scope | `runtime_contracts.WorldScope` | Host-authenticated campaign, branch, restore and current state identity. Also re-exported from `solo_provider` for compatibility. |
| Available capabilities | `shared_runtime.capabilities(world, actor)` | Actual selected adapter and actor-received options. Each immutable `ActionCapability` binds an operation, structured action and source references. |
| Actor projection/drafts | `actor_view(world, actor, branch_id=..., restore_id=...)` | Detached capabilities, actual received records, capability-bound editable drafts and a custom response field. No hidden stock/condition feasibility filtering. |
| Selected continuations | `actor_view(...)["continuations"]` / [phase API](PHASE_CAPABILITY_API.md) | Observation/Rise work start options, last received phase/status/commands and sanitized outcomes. Native typed execution/CAS remains authoritative. |
| Selected communication | `actor_view(...)["communications"]` / [communication API](COMMUNICATION_CAPABILITY_API.md) | Received participant/source and offer views, exact speech/terms, role-dependent command attempts and sanitized atomic native execution. Forwarded words confer no private contract access. |
| Exact accepted intention | `prepare_intent(...) → AcceptedIntent` | Immutable edited text plus separately selected capability/action, source and scope. JSON round trip supports pending-request recovery. Preparation commits nothing. |
| Explicit execution | `execute_intent(world, request, current_scope=..., persist=..., explicitly_accepted=True)` | Current capability/control checks, actual observed Core handler, cloned atomic effects and mandatory host save/result CAS. |
| Received records | `received_records(world, actor, limit=64)` | Received evidence, actor settlement records and own phase receipts. Original testimony/status/source and causal information times remain distinct from elapsed spans. Truncation is explicit. |
| Committed receipt | `committed_receipt(world, actor, event_id, branch_id=..., restore_id=...)` | Actual immutable Core result or received communication, exact text and local depot presentation. No caller-supplied outcome facts. |

Import from the Engine runtime directory. The host authenticates actors and selects the actual current world/branch/restore before calling these functions. Scope strings supplied by an untrusted client establish no authority. `WorldScope.state_digest` is a private host validation value; `actor_view` does not expose it or raw saves/templates, private conditions, resources or dependency certificates. Returned text is plain text and must be escaped by its display surface.

## Intention and execution

```python
from runtime_contracts import WorldScope
from shared_runtime import actor_view, prepare_intent, execute_intent

view = actor_view(world, actor_id, branch_id=branch_id, restore_id=restore_id)
# The user reviews an actual capability and their independently editable text.
request = prepare_intent(world, request_id=request_id, actor_id=actor_id,
    intention=exact_edited_text, capability_id=selected_capability_id,
    branch_id=branch_id, restore_id=restore_id)
# Host durably retains request.to_json() as its pending request.
result = execute_intent(world, request,
    current_scope=WorldScope(world.s['campaign_id'], branch_id, restore_id, world.checksum()),
    persist=host_atomic_compare_and_save, explicitly_accepted=True)
```

Draft selection/editing and preparation commit nothing. The host must show the text and structured action together for explicit review; editing words never silently changes the selected operation. This API adds no natural-language interpreter. A semantic depot tag such as `travel` or `ask` cannot select a handler. Unknown capability IDs fail closed. `capability_id=None` explicitly selects only a recorded unresolved declaration, preserving the exact intention without resolving unsupported mechanics.

The `AcceptedIntent` name identifies the exact immutable text/action contract; `execute_intent` still requires the explicit boolean `True`. It rejects changed text/action/source, revoked current control, absent/changed capability, stale state, mismatched campaign/branch/restore and identity conflicts. Shared request identities use one event namespace across adapters, so changing an operation cannot reuse an accepted request as another action. `SharedActionUnavailable.code` is public; any `.dependencies` evidence stays private.

`persist(expected_scope, candidate_save, public_result)` must serialize with all host writers, compare the actual campaign/branch/restore/state, and atomically durably save both values or raise. The Engine publishes its in-memory candidate only after this callback returns. A failed save leaves the original world unchanged. If persistence succeeded but acknowledgment was lost, reload the actual host save, deserialize the original pending request and retry. Replay retrieves the original result before new-state checks and does not repeat effects. A restored/discarded future request cannot pass changed restore identity. Cross-process durability and authentication remain host responsibilities.

Core's existing `record_player_action` now checks actual current control inside its handler. A stale player-list entry cannot bypass revoked current eligibility. R9 observes the decision and conflicting revocation/rejected execution; declaration remains unresolved and creates no physical outcome.

## Supported adapters and receipts

| Context | Execution through shared acceptance | Receipt/information support |
| --- | --- | --- |
| Received authored scene | Existing movement, observation and delivery handler with selected rules/durations. Blocked/depleted results retain their actual unsuccessful outcome. | Exact summary/observations and actual action elapsed span. |
| Rise | Existing 13 settlement operations under the selected setup/rules. | Original actor receipts and same-event inspection; cumulative time is never presented as an action span. |
| Any currently controlled actor | Explicit `record_player_action` declaration. | Exact declaration remains `declared_not_resolved`; no new adjudication. |
| Existing work/travel/observation processes | Existing [native typed phase API](CONTINUATION_COMMUNICATION_API.md); no new shared command mapping. | Shared receipt and received-record projection preserve original phase status/progress/time without reading current remote progress. |
| Existing selected communication | Existing native typed communication API; no new channel/stock/recipient rules. | Actual received testimony and original offer statuses/terms; speaker attribution and no invented speech duration. |
| Equipment/general operations lacking this adapter | Existing APIs/results retain their supported behavior. | Explicit `receipt_adapter_unavailable`; an existing honest result is not replaced by invented narration. |

Scene capabilities come from the actor's actual received map and location. Hidden blockage, remaining stock and permission feasibility do not choose a winning menu. Rise uses its selected published operation set; it does not define capabilities for other campaigns. Labels originate in these adapters; a theme or campaign name grants no handler, authority, stock or playable start.

## Offline neutral response runtime

The Engine bundles Catalog's **exact** `irgs-response-depot-v1` schema-2 content: **750 system responses and 250 editable drafts**, 127 families and 32 mixing recipes. [Source provenance](../IRGS_3_3/data/responses/depot_v1/SOURCE.json) pins Catalog commit `94b8ca6d976da48b3c6ca65e014b28c6d9a120c2` and SHA-256 `8b397ae8cd72cf5ed59c330c0572e34922579726740edbeed9fca957044a6ae4`. Runtime intake verifies that hash. Engine owns `response_depot.py` selection and the compatible formatter; Catalog owns the authored text. The previous Engine 338-variant library and compatibility API remain preserved under their original identities.

Shared result APIs return `presentation` using the neutral depot. Every committed composition includes the exact receipt anchor; substitutions cannot rewrite outcomes, negation, testimony or accepted intentions. Missing/corrupt templates or unavailable formatting retain the exact literal receipt; drafts retain actual authored wording where available, and public status retains honest unresolved/unavailable text. No fallback calls a provider. `render_usage` records zero rendering provider calls/model tokens; it does not refund earlier optional inference.

Only authored library content is cached. Views/receipts are recomputed from the host's actual world and scoped to actor, campaign, branch, restore and relevant legitimate source facts. No response cache crosses actors or restores. Older receipt rendering never appends current stock, project status or new observations. `response_depot` formatting helpers are trusted presentation functions; they do not authenticate supplied packets or establish their truth. Public truth-sensitive entry points are the guarded shared view/receipt APIs.

## Evidence and remaining work

Run `python -B tools/qualify_shared_systems.py --output engine/SHARED_SYSTEMS_VALIDATION.json`, then the full Engine runtime suite and component checks. [The execution record](SHARED_SYSTEMS_VALIDATION.json) names each test, exact source hashes and scope. Actual shared execution is independently tested in a non-Rise authored scene and a Rise world, with consequential transfer, blocked movement, selected elapsed time, explicit acceptance, temporary host CAS/restart/restore and zero provider dispatch. A fresh process completes a non-Rise action while provider/App/Catalog imports are forbidden.

All 1,000 variants render with four synthetic themes and all 32 recipes render with full and required-only facts. This proves content portability; it establishes no historical-court, fantasy, space or modern campaign mechanics. The evidence does not qualify new App controls/pins, a joined release, general freeform/combat, NPC decisions, sustained institutions, live models or production token savings. Broader DEV milestones remain open.
