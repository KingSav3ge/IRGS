# IRGS 3.3.C — Persistence and recovery contract

Design handoff · 20 October 2026 · Proposed implementation contract

## Scope and existing authority

This document specifies engine behaviour for later implementation by Claude. It does not activate a runtime, approve a storage migration, or claim that the acceptance cases below have passed. Codex's 3.3.C work owns engine design; Emergent's 3.3.E work owns website and app presentation. Both must refer to one authoritative campaign world.

The selected baseline remains IRGS Core 3.3. Inspect the actual implementation before changing it. Relevant existing interfaces are `IRGS_3_3/runtime/core_world.py` (`CoreWorld.apply`, `save`, `load`, `checksum`, `_validate`), `r9_runtime.py` (`observe`, `frontier`, retained requests and resolutions), and `irgs_reference.py` (`canon`, `digest`). Existing `CoreWorld.apply` checks campaign scope before processed-event replay and rejects a changed event payload. Extend these guarantees to submitted actions and durable recovery rather than replacing them with a parallel action journal.

The nine owners in `IRGS_3_3/Core/IRGS_Core_Engine_v3_3.md:3028–3036` remain authoritative: K-TIME owns causal scheduling and the campaign journal; K-ACTOR actual people and conditions; K-STOCK conserved quantities; K-ASSET identified objects; K-WORK actual tasks and progress; K-INFO evidence and received knowledge; K-ORG organizations and mandates; K-NET routes and operating capacity; K-POP residual cohorts. Persistence stores those records. It grants no new ownership of their meaning.

## Logical records and identities

The following are logical schemas, not mandated tables or duplicate simulation owners. Identifiers are nonempty opaque strings. Revisions are nonnegative integers. Digests are identified SHA-256 values over a versioned canonical UTF-8 JSON representation. Reject duplicate object keys, nonfinite numbers and unsupported value types before canonicalization. Do not silently normalize semantic identifiers or declaration text.

| Record | Required typed fields |
| --- | --- |
| CampaignHead | `campaign_id: ID`, `revision: Revision`, `state_ref: ID`, `state_digest: Digest`, `core_binding_ref: ID`, `source_edition_refs: ID[]`, `schema_version: ID` |
| ActionRequest | `campaign_id`, `request_id: ID`, `principal_ref: ID`, `actor_ref: ID`, `kind: ID`, `command: JSON`, `declaration_ref: ID?`, `source_refs: ID[]`, `semantic_payload_digest: Digest`, `original_record_digest: Digest`, `submission_at: Coordinate`, `accepted_revision: Revision` |
| SubmissionReceipt | `campaign_id`, `request_id`, `transaction_id: ID`, `accepted_revision: Revision`, `semantic_payload_digest`, `original_record_digest`, `initial_attempt_ref: ID?` |
| AttemptRecord | `campaign_id`, `request_id`, `attempt_id: ID`, `phase_id: ID`, `expected_revision: Revision`, `rule_refs: ID[]`, `original_attempt_digest: Digest`, `status: RequestStatus` |
| OutcomeReceipt | `campaign_id`, `request_id`, `attempt_id`, `phase_id`, `transaction_id: ID`, `revision: Revision`, `state_digest`, `event_refs: ID[]`, `status: RequestStatus`, `result: JSON`, `pending_refs: ID[]` |
| RequestStatusView | `campaign_id`, `request_id`, `head_revision: Revision`, `status: RequestStatus`, `current_attempt_ref: ID?`, `outcome_refs: ID[]`; derived from retained records in the selected lineage |
| PendingWork | `campaign_id`, `work_id: ID`, `request_ref: ID`, `prerequisite_refs: ID[]`, `observed_revision: Revision`, `status: WorkStatus`, `producer_ref: ID`, `claim_epoch: integer`, `attempt_ref: ID?`, `result_ref: ID?` |
| Checkpoint | `campaign_id`, `checkpoint_id: ID`, `revision`, `state_ref`, `state_digest`, `request_boundary_ref: ID`, `schema_version`, `source_edition_refs`, `label: string?` |
| BranchProvenance | `campaign_id: new ID`, `parent_campaign_id: ID`, `parent_checkpoint_id: ID`, `parent_revision`, `parent_state_digest`, `fork_instruction_ref: ID` |

Request identity is the pair `(campaign_id, request_id)`. An attempt/phase has its own scoped identity and immutable receipt. Event, transaction, provider-task and presentation identities remain distinct and explicitly linked. The semantic request digest covers campaign scope, principal, actor, kind, exact semantic command, declaration reference, selected rules and sources. It excludes the coordinator-assigned submission coordinate, wall-clock metadata, expected-head revision and narration preferences. A second original-record digest covers the accepted immutable record, including its frozen submission coordinate. Retrying submission retrieves the first accepted coordinate; it never restamps the request from the current clock.

Submission replay returns the immutable acknowledgement and a separately identified current-status projection. A previously pending or scheduled receipt does not prevent a legitimate later attempt or process phase. Executing that continuation requires a new attempt identity, current revision and unchanged selected intention, or an explicit superseding request when the method changes. Retrying an accepted attempt returns that attempt's historical receipt; it never executes the phase again.

`RequestStatus` follows the supplement's canonical lifecycle: `pending`, `awaiting_clarification`, `awaiting_information`, `awaiting_prerequisite`, `awaiting_selected_rule`, `awaiting_authorization`, `awaiting_allocation`, `scheduled`, `in_progress`, `completed_successfully`, `completed_unsuccessfully`, `interrupted`, `invalid`, `cancelled` and `superseded`. A durable accepted request can remain unresolved. `WorkStatus` distinguishes recoverable waiting, claimed execution, completed, cancelled and retryable failure. Each transition preserves its actual cause and prior references.

## Submission and commit ordering

1. Authenticate the caller and verify permission to access the requested campaign and receipt. Validate explicit campaign scope before looking up replay data. A caller-supplied authority string is not proof of permission or an institutional mandate.
2. Validate the request envelope and canonical semantic payload. Acquire the campaign's serialization boundary or an equivalent transactional compare-and-swap mechanism.
3. Look up the scoped submission or attempt identity for the command being retried. Compare the appropriate immutable digest. A mismatch fails. A match returns its original authorized acknowledgement or attempt receipt, with separately labelled current continuation metadata and no execution. Use the frozen accepted submission coordinate. Perform this recovery before rejecting an obsolete expected-head revision.
4. For a new submission or a new attempt/phase on an existing intention, compare the expected revision with the actual head. A mismatch returns a conflict and the permitted current revision; it neither overwrites the head nor silently rebases the action.
5. Construct a detached candidate from the verified head. Check actual actor existence, player control or mandate, information receipts, prerequisites, selected rules, quantities and finite capacities. Use the existing execution-derived dependency machinery. Identifier order supplies no allocation authority.
6. Resolve supported effects through owner interfaces. Preserve unsupported intent with an explicit unresolved reason. Partial activity requires actual committed milestones; elapsed time or narration cannot manufacture completion.
7. Atomically persist the validated authoritative candidate, its journal and processed markers, the immutable request/outcome links, recoverable pending work and the new head revision. Either the complete related commit becomes visible or none of it does. An unresolved accepted request may advance the storage revision without advancing world time.
8. After durable confirmation, acknowledge the receipt and schedule presentation from the committed result and permitted actor projection. A failed acknowledgement or narrator call retries receipt retrieval or presentation, never the Core effects.

Store engine results and pending records consistently with their existing owners. An operational transaction index may reference the authoritative journal; it must not become a second independently editable history of world events.

## Failure and restart boundaries

| Interruption point | Required recovery |
| --- | --- |
| Before durable acceptance | Retain any separately saved draft; do not report acceptance or effects. |
| Accepted but awaiting a rule, report or authorization | Reload the same request and reason; preserve its identity and pending prerequisites. |
| Candidate effects calculated but uncommitted | Discard the candidate; recover the confirmed head. Retry only through the original identity. |
| Storage commit result uncertain | Query the transaction/request record under serialization before attempting execution again. |
| Committed, response lost | Return the original receipt; effect and revision occur once. |
| Committed, narration failed | Regenerate presentation from existing event references without modifying simulation state. |
| NPC worker claimed work, then exited | Recover or expire the claim using an explicit worker policy; revalidate prerequisites before committing once. |
| Interrupted work after real milestones | Preserve settled effects and remaining work; do not roll back actual past consequences. |

NPC work cannot exist solely in an in-memory asynchronous task. Persist its request and dependencies before dispatch. Use a durable claim, attempt identity and completion receipt so restart, duplicate delivery and multiple workers cannot double-commit. A lease timeout permits recovery review; it does not prove the prior attempt failed to commit. Check its receipt first. A new claim carries a monotonic fencing epoch checked at commit; a late worker with an obsolete claim cannot overwrite its successor. Worker outputs are proposals until ordinary Core validation accepts them.

## Checkpoints, restoration and forks

A checkpoint captures one consistent confirmed revision, including its pending-work boundary and compatibility references. It creates no in-world event, elapsed time, healing, resources or NPC decision. Reusing a checkpoint identity cannot silently replace its contents.

Restoration is an explicit, authorized management request with its own immutable identity. Serialize it against actions and pending-work commits. Require an expected current revision, verify checkpoint integrity and scope, and install its snapshot as a new storage-head revision. An action calculated against the displaced head must fail its commit comparison, not overwrite the restored world. Old acknowledgements and accepted request identities remain recoverable: replaying an old request ID must never apply its effects anew after restoration. Historical receipts must identify their original revision rather than imply their effects are present in the current restored head.

Reconcile restored pending work against the retained attempt index. A task may have been pending at the checkpoint but completed on the discarded future head. Its historical receipt neither recreates that effect nor proves completion in the restored world. Invalidate displaced worker claims; hold the task or authorize a new continuation under the selected restoration policy, with a new attempt identity and current revision. Preserve the old attempt and both lineage references. Never silently replay an old accepted attempt or leave a restored task blocked merely because a different historical head completed it.

A branch receives a new campaign identity and immutable parent/checkpoint provenance. Preserve the inherited past as a verified snapshot with source-event lineage. Do not re-execute that past to initialize the branch. Rebind active campaign-scoped references through a qualified fork operation. Inherited pending work must be explicitly mapped, held or cancelled; copying an executable worker claim is insufficient. New branch actions receive new scoped identities and may create a different future. Parent and branch must share no mutable state.

## Integrity, clocks and storage choices

Checksums detect accidental or unauthorized byte/state changes relative to a trusted reference; they do not authenticate callers, establish historical truth or prove a rule was adopted. Preserve access control and source provenance separately. Validate saved state through Core invariants and compatibility metadata before use. Opening, inspecting or loading a save must not migrate it, reseed the world, restore historical-template factions or regenerate missing quantities. Migration requires a separately reviewable, source-preserving operation.

Storage revision, causal clock, civil date and elapsed duration are different coordinates. The current Core clock orders causal events; incrementing it does not establish thirty minutes or a civil day. Time advancement needs an explicit selected calendar and duration rule. Saving, inspection and receipt retrieval do not advance simulation time. Restoration reinstates the checkpoint's saved temporal state under a new storage revision without executing intervening events.

SQLite transactions or transactional MongoDB arrangements may implement this contract. A revision-filtered replacement alone is insufficient if request receipts and pending work can fail independently. Choose an atomic arrangement supported by the actual deployment, or a staged recovery protocol with a provable durable commit boundary. Do not introduce another simulation database merely for a new interface.

## Proposed acceptance cases

These are required implementation checks, not executed-test claims.

| ID | Setup and expected result |
| --- | --- |
| PR-01 | Submit one supported transfer; state, journal, receipt and head expose the same committed transaction and conserved quantity. |
| PR-02 | Retry after a lost response with the original request and obsolete head; recover its frozen submission coordinate and original receipt, with no new debit or revision. A new attempt/phase remains possible under a new qualified identity. |
| PR-03 | Reuse that identity with a different amount; reject it without changes. |
| PR-04 | Request another campaign's receipt without permission; reject before revealing whether that request exists. |
| PR-05 | Submit a fresh request against a stale revision; reject before applying any candidate effect. |
| PR-06 | Exit after calculation but before commit; restart shows the prior confirmed state and no successful receipt. |
| PR-07 | Exit immediately after commit; restart returns the one accepted outcome and durable pending-work references. |
| PR-08 | Fail narration repeatedly; world checksum, event count and quantities remain unchanged. |
| PR-09 | Deliver one NPC task twice to independent workers; at most one owner-valid effect commits. An old claim's late result fails the fencing/revision check. |
| PR-10 | Restart with a claimed NPC task; recover its receipt or revalidate a new attempt without creating a duplicate event. |
| PR-11 | Capture and inspect a checkpoint; clock, conditions, resources and NPC activity remain unchanged. |
| PR-12 | Race restoration with an action; one valid revision transition wins and the stale writer receives a conflict. |
| PR-13 | Restore an earlier checkpoint, then retry an old accepted action ID; retrieve its historical receipt without resurrecting the effect. Restored pending work completed on the discarded future is held or assigned a new authorized continuation; it neither replays the old attempt nor remains falsely completed. |
| PR-14 | Fork a checkpoint; inherited events are not replayed, provenance is explicit, and later branch writes leave the parent unchanged. |
| PR-15 | Alter a saved checksum or incompatible schema; refuse activation without reseeding or read-time repair. |
| PR-16 | Accept an unresolved rule-dependent request; persist its reason and pending state while leaving actual world time and resources unchanged. |
