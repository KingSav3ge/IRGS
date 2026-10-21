# 3.3.C — Action and dependency contract

**Status:** proposed engine design for Claude implementation. This document does not certify draft code, activate a release or adopt new numerical models. The selected authority remains IRGS Core 3.3. 3.3.C develops the text engine; 3.3.E presents and submits requests to that engine.

## Existing interfaces and ownership

`core_world.CoreWorld.apply(eid, at, op, **params)` supplies campaign scope, immutable event replay, clone/validate/commit behavior and the journal/processed ledger. `r9_runtime.observe(state, event)` executes instrumented and ordinary handlers; `frontier(world, events)` derives conflicts and retains unresolved requests. `temporal_registry.available_entities` uses committed registry coordinates. `starting_selection` supplies explicit control. `genre_receivers` contains the existing Military and Roman effects below.

Retain the nine existing authoritative owners. Workflow records reference their facts rather than duplicating them.

| Owner | Required boundary |
| --- | --- |
| K-TIME | Causal order, actual time and scheduling; one campaign event coordination path. |
| K-ACTOR | Actual identities, location, condition and individual availability. |
| K-STOCK | Physical quantities and selected monetary balances; transfers conserve quantity. |
| K-ASSET | Actual assets, components and asset-specific constraints. |
| K-WORK | Activities, actual progress, acceptance and work settlement; reference stock reservations and network capacity through their owners. |
| K-INFO | Evidence, provenance, receipt and observer-specific knowledge. |
| K-ORG | Organizations, roles and mandates. |
| K-NET | Networks, transport and delivery capacity. |
| K-POP | Population membership/accounting referencing actual identities. |

Specialist records retain their established scope: for example, ECO claims do not create cash and GOV decisions do not themselves move people or goods. A workflow outcome is a reference to committed owner events, not a second stock, condition or authority ledger.

## Request, selection and occurrence

Keep these distinct:

1. **Intent:** the actor's exact declaration, without treating prose as accomplished fact.
2. **Selected operation:** a typed, versioned interpretation accepted under the supported rules. It may remain unknown.
3. **Attempt:** validation and execution against a particular current world revision, producing a recorded decision.
4. **Occurrence/effects:** what the Core actually committed, with source events and supported effective times.
5. **Presentation:** actor-permitted description of those effects after commitment.

A request's immutable accepted record includes schema version, request ID, campaign ID, actor, controller type, exact declaration, selected operation/parameters, causal submission coordinate, source reference and player instruction reference when applicable. Hash canonical finite JSON; preserve exact strings. The semantic payload digest excludes the coordinator-assigned submission coordinate and expected head revision. A separate original-record digest covers the full accepted record with its frozen coordinate. A retry recovers that accepted coordinate; it does not assign a new current-clock value. A changed interpretation creates a new request linked to the original. Never rewrite an accepted request to make an expired window valid.

Illustrative persisted synthetic request, using existing native parameter names. `at` is the coordinator-assigned causal submission coordinate, not permission for a client to backdate an action:

```json
{
  "schema_version": 1,
  "request_id": "issue-01",
  "campaign_id": "fixture-campaign",
  "actor": "commander",
  "controller": "player",
  "declaration": "Issue the kit authorized by order O-1.",
  "selection": {
    "operation": "military_issue_equipment",
    "params": {
      "order_id": "O-1",
      "commander": "commander",
      "persons": ["worker"],
      "material": "kit",
      "quantity_each": 1,
      "from": "depot",
      "authority_ref": "authority-A"
    }
  },
  "at": 12,
  "source_ref": "fixture:reviewed-request",
  "instruction_ref": "player:instruction-01"
}
```

The nested parameters cannot override campaign, instruction, source or attempt identity. Identifiers must be unique within campaign scope. Verify scope before replay lookup. Submission and attempt/phase receipts have separate identities. An identical accepted retry returns its original acknowledgement or attempt receipt, including after reload; changed payload under that identity fails. A pending or scheduled intention can receive a new qualified attempt under a new identity; replaying the original submission does not execute that continuation.

An attempt records its own identity, request digest, expected world revision, code/rule identities, evaluated prerequisites, result status, dependency evidence and committed event references. Publish state effects and the recoverable receipt atomically behind the revision check. A database or process-local lock alone does not satisfy this contract. Save/restore uses the same serialization boundary; it cannot be silently overwritten by an older in-flight attempt.

## Authorization and lifecycle

Inside the instrumented execution path, validate actual actor existence, current control policy, instruction, received authority, selected rules, resources, capacities and temporal feasibility. `player_actor_ids` alone is insufficient after eligibility revocation. A selected faction's policy may authorize its named control actor without a separate individual eligibility grant. Existence, participation and control remain different properties.

Orders/delegations must match the actor, exact scope, active interval and established authority basis under the campaign's selected rules. A nonempty `authority_ref` proves none of these. Trusted synthetic fixture setup is an explicit source selection, not proof of historical legal power. Player and autonomous proposals share the same validation/effect path; unsupported autonomous authority remains pending.

The supplement's lifecycle table is canonical: `pending`, `awaiting_clarification`, `awaiting_selected_rule`, `awaiting_information`, `awaiting_prerequisite`, `awaiting_authorization`, `awaiting_allocation`, `scheduled`, `in_progress`, `completed_successfully`, `completed_unsuccessfully`, `interrupted`, `invalid`, `cancelled` and `superseded`. The first bounded implementation must distinguish the states it can reach and explicitly hold unsupported transitions. Reasons identify the failed requirement. Existing status names require an explicit semantic mapping. A failed prerequisite creates no physical effects. Cancellation terminates remaining intent; it never erases earlier occurrences. Scheduling is not completion of the scheduled work, and a later execution phase must remain possible.

The current Core `clock` is causal sequence. `campaign_time` and `entity_registry.as_of` are distinct coordinates without an adopted elapsed-time binding. This milestone must not infer hours or advance civil dates from request counts. Timed effects require an explicit calendar/profile binding.

## Native examples

**Military issue:** existing `military_issue_equipment` reads a received order, verifies matching directives and deadline, transfers actual kits through Core stock operations and marks that order executed. Validate every recipient's current existence. Outcome `completed_successfully` means those specified transfers occurred; it establishes no travel, enlistment, wages or general victory.

**Roman booking:** existing `roman_begin_delegated_activity` reads an active delegation and uses shared actor/site capacity. An illustrative selection is:

```json
{
  "operation": "roman_begin_delegated_activity",
  "params": {
    "delegation_id": "D-1",
    "delegate": "delegate",
    "activity_id": "work-01",
    "actors": ["worker"],
    "site": "yard",
    "capacity_id": "yard-capacity",
    "start": 50,
    "end": 60,
    "role": "craft",
    "authority_ref": "authority-B"
  }
}
```

These synthetic coordinates are prospective bounds on the selected fixture axis, not universal durations. Outcome `scheduled` means the booking exists. It grants no completed work, consumed materials, output or pay.

## Execution-derived dependencies

Instrument authorization and effects together. External prechecks cannot supply an unobserved permission dependency. Capture actual positive and negative lookups, existence tests, scans, container navigation and selected list reads. Record list writes only for actual mutation; ordinary reads must not invent shared writes. Include C-level mutation backstops and prove instrumented/ordinary semantic parity.

Qualify successful and rejected executions. Preserve reads leading to rejection, reason, rollback proof and any independently established occurrence. A missing branch/case remains unqualified. Global validator scans may be distinguished from allocation dependencies only when the combined candidate is independently validated before commit; validators cannot mutate state.

Build conflict edges for noncommutative records, resource pools, overlapping finite capacities, prerequisites and indivisible transactions. Do not choose winners by request ID, array order or hash. Retain allocation conflicts for a later authorized decision and revalidate then. Unsupported handlers receive a conservative compatibility barrier; absence of a footprint is not independence. Actual measured physical losses remain occurrences, subject to evidence reconciliation rather than administrative allocation preference.

Certification evidence identifies exact code/rule hashes, input snapshot, request/attempt payloads, observed reads/writes, validator checks, post-state or rejection, and exercised branch. A passed case does not certify all handlers or all branches. Adding an operation requires its own evidence and integration into the operation inventory.

## Acceptance cases for implementation

All quantities and identities below are explicitly selected test fixtures.

| ID | Input state and operation | Observable required assertion |
| --- | --- | --- |
| A01 | Ten kits; matching received order; issue one | Depot nine, recipient one; total ten; one linked completed outcome. |
| A02 | Retry A01 with identical request/attempt | Same receipt; no extra transfer, event or time change. |
| A03 | Reuse A01 ID with changed quantity/text | Reject altered payload; world unchanged. |
| A04 | A01 under another campaign ID | Reject before lookup or disclosure. |
| A05 | Valid declaration; unsupported selected operation | Await selected rule; no inferred physical success. |
| A06 | Existing actor lacks current player control | Await authorization; no stock change. |
| A07 | Previously controlled actor; eligibility revoked | Old player list grants no continuing authority. |
| A08 | Selected faction authorizes its actual control actor | Validate faction policy; do not require unrelated individual eligibility. |
| A09 | Order absent, unreceived, expired or mismatched | Specific pending reason; no partial transfer or executed flag. |
| A10 | Correct order; stock now insufficient | No negative stock or partial issue; preserve request. |
| A11 | Recipient ceased to exist before execution | No receipt of equipment; current existence read appears in evidence. |
| A12 | Two requests claim the same finite pool | Conflict retained for both; ID ordering selects neither. |
| A13 | Separate orders/stocks; execute in either order | Equal physical results; certify independence or disclose conservative barrier. |
| A14 | Simultaneous eligibility revocation and issue | Actual authorization read conflicts with revocation write. |
| A15 | Simultaneous recipient dissolution and issue | Conflict detected before either inferred order of occurrence. |
| A16 | Valid Roman delegation and free capacity | One scheduled booking; no work/output/pay or elapsed-time claim. |
| A17 | Roman booking overlaps full site/actor capacity | Await allocation/prerequisite; no second booking. |
| A18 | Delegation revoked alongside Roman booking | Conflict detected from actual delegation access. |
| A19 | Cancel pending request, save and reload | Cancellation persists and retries idempotently; no later execution. |
| A20 | Crash/retry or restore during in-flight attempt | Recover committed receipt or definite uncommitted status; no stale overwrite. |
| A21 | Hidden fact/NPC location changes | Player projection unchanged without legitimate receipt. |
| A22 | List read, append, deletion and negative lookup cases | Read/write traces match actual accesses; parity and rollback hold. |

## Known limits

Current native handlers and R9 fixtures do not establish general movement/combat, freeform adjudication, complete lawful authority, campaign-native institutional autonomy, automatic calendars or crash-safe host persistence. Emergent's active lightweight engine is not yet a CoreWorld adapter. Preserved coding drafts are inactive and excluded from the design handoff; isolated component tests are not integrated acceptance. Claude should implement and qualify this bounded contract before expanding those systems.
