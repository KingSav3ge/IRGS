# Reviewed communication intents and draft preview

29 October 2026; 3.4.5 Pre-Alpha. This bounded A4-ENG-03/WB-ENG-01 increment
extends `irgs-supported-intent-1` over the existing local communication handler
and adds `irgs-world-initialization-preview-1`. The selected scenes, settlement
rules and Core remain authoritative. Neither extension qualifies an Alpha gate.

## Explicit communication review

`review_communication(world, actor_id=..., intention=..., channel_id=...,
recipient=..., command=..., details=..., branch_id=..., restore_id=...)` returns
an actor-scoped review with exact words, selection, `review_id`, status and
`committed: false`. The authenticated host supplies the channel, participant and
structured command independently of the words. No parser, model or semantic tag
selects an operation. Missing choices return `clarification_required`; unavailable
or unsupported selections return `unsupported`. A valid, attemptable selection
returns `supported` without checking hidden stock, presence or authority. For an attemptable command, malformed
selected terms return a clarification status. Text and detail sizes are bounded.

For a reviewed fictional R00 offer, `details` is for example:

```json
{"offer_id":"unique-offer", "terms":{"from":"founder-home", "to":"oren-home", "material":"grain", "quantity":1, "authority_id":"founder-household-offer"}}
```

The offered profile and the founder's account must have been explicitly selected
in the original start review. This JSON supplies an attempt; no quantity is
created or reserved, and it conveys no recipient consent. Quay starts support
selected local `speak`; R00 also supports `speak` and, when the optional reviewed
profile is selected, `offer` and received-offer commands. No NPC is impersonated.

`prepare_communication` recomputes the review with exact choices and returns an
existing private `CommunicationRequest`; changed reviews raise `review_stale` and
unsupported attempts `intent_not_supported`. A host persists the private request
and authenticates actor/branch/restore. `execute_communication` requires explicit
boolean acceptance and host save/result CAS, calls the native Core handler, and
returns the versioned result with actual status, exact intention, received
communication, receipt and presentation. Validation/execution failures use the
existing `CommunicationUnavailable` codes; private dependency evidence remains
host-only. Lost replies are recovered by reloading the saved world and retrying
the same serialized request. Identical replay returns the same original DTO;
restore identities fence discarded futures. The host owns request IDs across its
adapters, atomic persistence, authentication and recovery.

Current App code uses its separate shared-intent and communication bridges, not
these new DTO methods. App adoption and Catalog's independently versioned consumer
for the new contract remain open. The existing shared scene/settlement intent API
and standalone communication API remain compatible.

## Disposable world initialization preview

`world_draft.preview_initialization(draft)` validates either already selected
`rise-r00` or `historical-quay` draft, initializes a disposable candidate in
memory, and returns `preview_only`, the draft/review digests and the candidate's
controlled actor view. It performs no campaign save, provider call or action.
No raw world, private stock, historical template or entity registry is returned.
The actor view is scoped to actual received facts, with day precision and unknown
hour retained where applicable. Preview actor, snapshot and capability identities
are explicitly marked non-reusable: the host must create a fresh actual candidate
and review/rebind its identity before action submission.

This preview shows only the existing bounded initializers; custom geography,
assets, external package import/export, arbitrary actors and atomic host playtest
creation remain unsupported. No source-only preview creates an independent world
owner or changes a continuing campaign. See [draft API](WORLD_DRAFT_API.md).

## Qualification and remaining dependencies

`test_intent_communication.py` runs ordinary Rise and non-Rise creation, exact
review, accepted testimony, refusal, explicit offer/withdrawal, actual invalid
account rejection, persistence failure, reload/replay and restore fencing.
`test_world_draft.py` checks both disposable previews, actor-filtered output,
unchanged drafts and distinct real/preview identity. Existing communication,
intent and phase tests remain applicable. [Execution evidence](COMMUNICATION_INTENT_PREVIEW_VALIDATION.json)
records source selections and actual checks; App's current bridges, browser and
independent Catalog consumer qualify only their own declared scope. No live AI,
Windows, package or joined Alpha qualification is implied.
