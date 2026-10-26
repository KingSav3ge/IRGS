# Engine continuations, communication and accounting

For host-safe participant, received-source and offer views over the selected
communication handler, use [communication capabilities v1](COMMUNICATION_CAPABILITY_API.md).
It keeps forwarded testimony separate from private structured contracts across
the existing receipt/rendering APIs and adds a sanitized atomic host result.

For the new actor-safe host interface over selected observation/Rise work, use
[phase capabilities v1](PHASE_CAPABILITY_API.md). It reuses the native request
and Core rules below while filtering public outcomes and bridging atomic host
persistence. The shared-response source set is already integrated as recorded
in the current development guide; new phase UI/pins need separate qualification.
The earlier source identities and scope notes below retain their original dates.

IRGS 3.4.0 development. These are server-only, explicitly selected Core APIs.
They add no world owner, historical fact, universal duration, NPC decision or
default provider permission. The prior bounded Solo/App integration is qualified
at Engine `8234044c089131314019ecaf6799a2f08028a3f8`, App
`277554aac21a092b8a55562309da274bbe74a3af` and Catalog
`401df26a1f16be864dd15d7c5250da5d75f8ccca`; this increment needs its own App and
coordinator qualification. See the coordinator's
[review](https://github.com/KingSav3ge/IRGS/blob/main/provenance/qa/primary_update_3_4_0_review.json).

## Continuing selected work, travel and observation

`process_runtime.prepare` creates an immutable `ProcessRequest` without effects.
It binds the exact phase intention, actor, process/phase IDs, next phase index,
selected command/details, source and `WorldScope`. Supported commands are
`start`, `advance`, `pause`, `resume`, `cancel` and `inspect`, subject to the
selected kind's actual rules. A host submits explicit acceptance with:

```python
request = process_runtime.prepare(
    world, phase_id=unique_phase_id, process_id=submission_id,
    actor=authenticated_actor, command="start",
    details={"kind": "work", "action_id": "build"},
    intention=exact_player_text, source_ref=reviewed_source,
    branch_id=current_branch, restore_id=current_restore_identity)
result = process_runtime.execute(
    world, request, current_scope=current_authorized_scope,
    persist=host_atomic_compare_and_save, explicitly_accepted=True)
```

The host must authenticate the actor and serialize every campaign writer. Its
`persist(expected_scope, candidate_save, receipt)` atomically compares campaign,
branch, restore identity and state digest, saves the Core candidate and receipt
durably, or raises. A lost acknowledgment requires reloading that durable save.
Reuse the identical stored request for retry; a new phase needs a fresh ID and
current scope. Rotate restore identity on every restore, even identical bytes.
The host retains the submitted immutable command and bounded failure status in
its existing request store. `to_json`/`from_json` preserve typed scope and exact
semantics across restart; these are private host records, never browser-authorized
or provider-supplied commands. Core phase receipts record committed effects.
Core journal identities recover the original receipt without effects. No
technical inference ledger or paid call is needed for these process operations.

Kinds and implemented scope:

- `work`: `build`, `delegate` or `resume` against the existing Rise shelter
  handler. The physical project remains in Core `projects`; the parent is an
  identity/index over it. Starting reserves inputs without consuming them or
  completing work. Positive explicit `advance.seconds` uses the selected
  settlement scheduler and stops at the first existing material boundary.
  Pause/resume retain progress. Cancellation ends the request and pauses/releases
  its remaining reservations; it does not erase physical work. A new explicit
  resume request uses the same unfinished project, without a second booking.
- `travel`: `walk_clearing` or `walk_commons` using the selected Rise travel
  duration. Actual people and, where applicable, household goods remain at the
  existing route location until arrival. Partial progress, pause and resume are
  durable. Existing elapsed advancement progresses the same journeys. Paused
  travellers remain committed in transit. Cancellation/return is unavailable
  because this model selects no return-trip rule; there is no teleportation.
- `observation`: an already received authored `observe` action. Progress uses
  its selected duration; knowledge is delivered only on completion by the
  existing scene handler. Pause/resume/cancel preserve elapsed work without a
  premature observation. There is no new hidden-object search or success roll.
  Mismatched or unsourced elapsed axes are rejected before progress; no mixed
  scene/settlement scheduler binding is inferred.

Core operation `continue_player_process` executes under ordinary atomic cloning
and actual R9 dependency observation. In-progress parents remain nonterminal.
Each received phase distinguishes phase identity/index, original and phase
intentions, status, terminality, committed elapsed span/total, worked/remaining
seconds, source and causal time. Physical stock, workers and provision remain
in existing Core records. Selected-rule changes cannot silently change a newly
submitted continuation's contract. Current control, location, commitments,
permission and resources retain actual handler checks.

`received_status(world, actor, process_id)` returns the last committed received
phase record. It does not reveal remote live work. Local `inspect` supplies a
fresh receipt; an actor's actual arrival has its own received notice. Storage
revision, Core causal sequence and selected elapsed seconds remain distinct.

## Speech, testimony and explicit offers

Core operation `execute_local_communication` is unavailable unless a trusted,
reviewed campaign selects `communication_rules`. This schema is an opt-in
contract, not an automatically installed fictional or historical rule:

```json
{
  "schema_version": 1,
  "source_ref": "reviewed-channel-and-custody-policy",
  "time_model": "causal_only_no_elapsed_rule",
  "stock_profile": "settlement_free_stock",
  "channels": {
    "local": {"mode": "co_located", "actors": ["founder", "oren"]}
  },
  "stock_authorities": {
    "existing-founder-mandate": ["founder-home"]
  }
}
```

The named mandates must actually exist, be current, sourced and scoped to
`transfer_stock`. The example grants no mandate or control. Both speakers and
receivers must exist; the speaker requires actual selected control. Channels
check real co-location and do not infer audibility along a route or remotely.
These operations record causal speech without resolving an elapsed speech
duration: results explicitly say `elapsed_status: not_resolved`.

`communication_runtime.prepare` binds request ID, actor, recipient, channel,
command, details, exact utterance/intention, source and world scope. Its `execute`
uses the same explicit acceptance and atomic host CAS contract above. Commands:

- `speak`, with empty details: records the exact words as attributed testimony
  and explicitly received evidence for both participants. A claim, including
  words of acceptance, creates no established fact, transfer or player decision.
- `offer`: details contain `offer_id` and exact `terms` (`from`, `to`, `material`,
  `quantity`, `authority_id`). The existing obligation record owns the offer.
  Creation checks actual custody scope, not hidden stock feasibility; it reserves
  or transfers nothing and never promises successful fulfillment.
- `accept`, `decline`, `withdraw`: require the original `offer_id` and
  `terms_digest`. Acceptance rechecks current offerer control, mandate, policy,
  account location and free stock, including seed and work reservations. It
  executes the actual Core `transfer_stock` once and marks fulfillment in the
  same transaction. No deferred debt, exchange rate or arbitrary event is invented.
- `counteroffer`: creates a new explicitly proposed transfer in the other
  direction and marks the earlier proposal superseded. It never accepts either
  offer. Withdrawal, decline and supersession retain their distinct statuses.

All offer changes require the selected local communication channel, so a reader
does not learn a remote hidden withdrawal. `received` filters actual evidence
receipts. `presentation` derives status, testimony, sources and any committed
transfer only from a received committed result. No model prose can supply a
purchase, emotion, answer or NPC decision. General NPC voice/semantic evaluation
and additional speech/obligation rules remain separate work.

## Reviewed inference charges

Both continuation and communication execute results now include local `presentation` from the [Engine offline response API](OFFLINE_RESPONSES_API.md). The independently bundled text uses actual phase/received records without a provider or API token. It does not change the authoritative records or the accounting contract below.

`inference_accounting.FinalCharge` and `reconcile` provide an operator-only
technical accounting contract. A trusted authorization callback must check the
current Creator/operator session. The operator supplies a final charge in the
ledger's configured units, the exact price revision, evidence reference/hash and
authority reference. The runtime does not independently verify a provider bill,
convert currencies, infer a fee or authorize inference.

Only finished nonprocessing attempts with known rate provenance can be
reconciled. The review is immutable and idempotent; a different final value
cannot rewrite it. Admission atomically counts reviewed charges plus unreconciled
reservations. A verified lower charge releases only that reviewed difference.
An overrun stays visible and blocks further admission. Unknown or in-flight
charges retain their entire ceiling; failure and reported tokens never imply
zero. A final zero needs the same explicit reviewed evidence/authority.

`budget_status` requires operator authorization and separates held ceilings,
known charges, unknown attempts, available units and overruns. Reconciliation
does not change campaign resources, attempt results, route provenance, previous
Core receipts or dispatch identities. Billing ingestion/corrections, real account
policy review and conditional live smoke are not implemented by synthetic bills.

## Evidence and remaining limits

[Execution evidence](ENGINE_TASKS_VALIDATION.json) records actual process,
communication, accounting and dictionary-observation cases. These include
conservation, competing frontiers, late rollback after attempted stock writes,
worker conflicts, current authority, restart, lost acknowledgment and restore.
R9 now observes C-level dictionary copy/comparison/union reads and clear/popitem
mutations explicitly. Conservative list/map scans remain in place.

These implementations advance DEV-06–DEV-17 and AIP accounting for their named
selected contracts. They do not complete arbitrary movement/search geography,
general freeform/combat, every operation-register branch, distributed persistence,
autonomous NPC institutions or the full C2 acceptance inventory. New App controls,
reviewed pins and joined qualification belong to their owning workstreams. Live
smoke and human/model quality require their separately configured inputs.
