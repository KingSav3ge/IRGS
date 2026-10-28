# Selected phase capability contract — version 1

IRGS 3.4.0 development. `phase_contract.py` exposes actor-safe availability,
last received status, supported commands and public outcomes over the existing
`process_runtime.ProcessRequest` / `continue_player_process` implementation.
It adds no world owner or timing/resource rule. The qualified shared response
integration remains complete at the source set recorded in `DEVELOPMENT.md`.
This new API needs its own App controls/pins and coordinator qualification.

## Stable host interface

All calls use the actual host-selected Core world and authenticated actor.

```python
import phase_contract as phases

view = phases.actor_view(world, actor, branch_id=branch, restore_id=restore)
request = phases.prepare_start(world, actor=actor,
    capability_id=selected_option_id, process_id=parent_id, phase_id=unique_phase_id,
    intention=exact_edited_text, source_ref=explicit_source,
    branch_id=branch, restore_id=restore)
# Durably retain request.to_json() in the host's private pending-request store.
result = phases.execute(world, request, current_scope=current_host_scope,
    persist=host_atomic_compare_and_save, explicitly_accepted=True)
```

- `actor_view` returns schema `irgs-phase-capabilities-1`, actor/snapshot IDs,
  `start_options`, last received `processes` and zero rendering usage. The same
  DTO appears as `shared_runtime.actor_view(...)["continuations"]`.
- Start options select received non-Rise authored **observation**, reviewed Rise
  **work** (`build`, `delegate`, `resume`) and selected Rise **travel**
  (`walk_clearing`, `walk_commons`). They are
  **attemptable**, never successful/feasible findings. They do not inspect private
  stock, permission or worker feasibility. Rule source references are preserved.
- `status(world, actor, process_id, branch_id=..., restore_id=...)` returns the
  latest received phase; `received_phase(..., phase_id, ...)` returns that original
  phase. No current remote project/stock/worker facts are appended.
- `prepare_command` takes actor/process/phase IDs, a listed command, `details`,
  exact intention/source and branch/restore. `advance` takes positive integer
  `seconds`; other command details are empty. The selected handler validates
  its actual duration/rate/maximum; this API supplies no universal maximum.

Commands derive from received status: active → advance/pause/cancel/inspect;
paused → resume/cancel/inspect; held → pause/cancel/inspect; completed → inspect;
cancelled → none. They remain attempts subject to current Core validation.
`status_basis: received_phase` and `live_status_probed: false` distinguish a
received boundary from hidden later progress. `inspect` commits a fresh phase
through the selected handler. For travel, `cancel` is omitted in transit; pause
and resume preserve actual route commitments. No return or universal movement
rule is selected. See [the travel handoff](TRAVEL_CAPABILITY_API.md).

## Authority, persistence and recovery

Preparation, viewing and command selection mutate nothing. Execution requires
the exact explicit boolean `True`, actual current control and a mandatory
`persist(expected_scope, candidate_save, public_result)` callback. The host must
serialize every writer, compare actual campaign/branch/restore/state, atomically
durably save both values, or raise. The original world is published only after
persistence returns. This API reuses native parent/phase identities, reservations,
Core rule checks, actual observed dependencies, conservation and atomic rejection.

The pending request stays native `ProcessRequest.to_json()/from_json()` in the
private host store. After lost acknowledgment, reload the actual durable save
and retry the original serialized request. Replay returns the original public
phase without repeating elapsed work. Rotate restore identity on every restore,
even with identical bytes. A new phase requires fresh identity and current scope.

Public DTOs whitelist phase identity/index, actor/kind, actual status/terminality,
original and phase intentions, summary/source/causal time, elapsed span/total and
worked/remaining seconds. They include an actual shared receipt and local neutral
depot presentation. Private parameter/rule hashes, raw projects, reservations and
dependency certificates are excluded. `PhaseUnavailable.code` is public; any
exception `.dependencies` remains host-private. Missing text retains an exact
literal receipt with no provider fallback. The display must escape plain text.

No provider/account/key or App/Catalog checkout is required. Branch/restore
selection and session authentication remain host duties; client-supplied strings
establish no authority. This contract does not expose communication/offer commands,
invent a search or universal travel rule or complete general DEV-06–DEV-17/C2 requirements.

## Qualification

The minimal API was published early at `8ab620099090413ed706aa70894065544347fbf3`
after 53 initial contract/process/shared checks and Engine integrity passed.
The completed [execution record](PHASE_CAPABILITY_VALIDATION.json) now names
28 contract cases: actual handler reads and atomic rejection, competing stock
and actor frontiers, pause/resume/cancel and physical progress, private-data
filtering, failed saves, concurrent delivery, native pending JSON, terminal replay
and restore fences. Source hashes identify the tested runtime and preserved
response content. Run `python -B tools/qualify_phase_capabilities.py` to repeat
the dedicated checks; `DEVELOPMENT.md` supplies full-suite private-fixture policy.

The final standalone runtime run executes 708 cases: 707 pass and the external
private-save case is replaced by the guide's explicit policy skip. All 292
focused checks, 35 shared-system cases, 20 native process cases and 13 native
communication cases pass with zero skips. Engine integrity and Kira canon pass.
Test fixtures are temporary and synthetic, with zero routine provider calls.
These results qualify the selected API/handlers. Subsequent [component interaction
checks](COMPONENT_INTERACTION.md) verify current App continuation controls with
the latest Engine/Catalog sources; adopting start discovery and reviewing new
pins/joined packaging remain separate. The next bounded task is the existing communication/offer
participant and received-source contract; its execution rules remain unchanged.
