# Selected Rise travel — A4-ENG-02

28 October 2026; 3.4.3 Pre-Alpha. This increment adds selected Rise travel to the
existing `irgs-phase-capabilities-1` actor/host contract. It advances A4-G04 and
DEV-06–14 without closing those gates or general C2 coverage. The native Core
`continue_player_process` handler and `rise-foundation-1` travel rule are unchanged.
The previous phase API remains available; its `start_options` can now contain
`kind: travel` in addition to work and observation. Consumers must handle this
additional attemptable kind rather than treating an exhaustive old set as a grant.

## Selecting and executing a journey

For a reviewed ordinary R00 start, `phase_contract.actor_view` and
`shared_runtime.actor_view(...)["continuations"]` expose `walk_clearing` and
`walk_commons` as source-attributed, explicit-submission travel options. Options
indicate attempts and do not filter against hidden state or promise that a route
can currently be taken. New starts require actual founder control. The existing
native handler checks the actual origin, selected destination, actor/household
commitments, stock-account location and reviewed model. It knows this selected
local route; no general road, access, weather or blocked-route model is introduced.

Use `prepare_start` with the selected `capability_id`, fresh process/phase IDs,
exact intention and source, plus the host branch and restore identity. Preparation
is read-only. Submit explicit boolean acceptance via `execute` and host
`persist(expected_scope, candidate_save, public_result)` CAS. Keep native pending
request JSON private for recovery. The player is placed on the actual route at
start. Before founding, the existing household members and stock-account site
move with them; quantities are conserved. After founding, the selected rule moves
only the actor. The selected R00 route takes 300 local seconds, not a universal
travel or civil-calendar rule.

Public received phases expose original/phase intention, status, worked/remaining
seconds and selected elapsed span/total through the existing whitelist. They do
not expose internal task records, other people's inventories or dependency
certificates. Active travel advertises `advance`, `pause` and `inspect`; paused
travel advertises `resume` and `inspect`. `cancel` is intentionally unavailable:
the selected rule supplies no mid-route return or teleportation. Completion moves
actual committed actors/goods to the destination and creates the founder's received
arrival notice. Reads return the last received phase; shared time may advance the
same journey and a later explicit inspection captures its current boundary.

Current rules, control, actual actor/location/stock-account reservations and host
scope are rechecked on execution. Wrong origin, competing journeys, stale state,
changed selected rule and failed saves do not commit another phase. A restored
branch rotates identity. A lost acknowledgment is recovered by reloading the
actual host save and replaying the original serialized request; this returns the
original public result without repeating progress or persistence. Host session
authentication and durable save/result synchronization remain App responsibilities.

## Qualification and remaining work

The three new `test_travel_capability` cases use normal reviewed Rise creation and
cover attemptable projection/privacy, actual origin rejection and competing actor
claims, paused household and goods, partial progress, resume, rule-change rejection,
failed save, arrival notice, reload, exact replay and restore fencing. Existing
native process and phase tests cover additional dependency and lifecycle paths.
[The HTTP executable](../tools/qualify_travel_http.py) uses ordinary App review and
creation, actual process prepare/accept, 100-second partial progress, pause,
resume, arrival, retry and Store reload without provider calls. It selects Engine
and Catalog explicitly and uses temporary synthetic state:

```bash
IRGS_ENGINE_ROOT=/workspace/IRGS-Engine/IRGS_3_3 \
IRGS_CATALOG_ROOT=/workspace/IRGS-Catalog/IRGS_Catalog \
PYTHONPATH=/workspace/IRGS-APP-WEB/IRGS_Web:/workspace/IRGS-Engine/IRGS_3_3/runtime \
python -B tools/qualify_travel_http.py
```

[Execution evidence](TRAVEL_CAPABILITY_VALIDATION.json) identifies the exact
candidate source hashes, App/Catalog checkouts and App's committed pins. Browser,
Windows, package, independent Catalog current-set acceptance and coordinator
operation/dependency capture remain separate. This selected travel path does not
complete broader routes, dynamic access/interruptions, non-Rise phased travel,
AI-supported intent, NPC autonomy, or sustained play. A4-ENG-01 offer prerequisites
and independent qualification, and A4-ENG-03 intent DTOs, remain open. WB-ENG-01
world-authoring contracts and the coordinator's 3.4.4 integration are separate work.
