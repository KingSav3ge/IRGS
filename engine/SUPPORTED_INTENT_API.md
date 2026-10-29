# Supported-intent review — API 1

A4-ENG-03 bounded increment, 29 October 2026; IRGS 3.4.5 Pre-Alpha. Module
`IRGS_3_3/runtime/supported_intent.py`, schema `irgs-supported-intent-1`.
This API uses the existing shared actor capabilities and Core execution. It is
available to a trusted host; App has a separate shared-runtime intent bridge and has not adopted this module. No
provider, API key, parser or new simulation rule is required.

## Review and submission

`review(world, actor_id=..., intention=..., capability_id=..., branch_id=...,
restore_id=...)` is read-only and retains exact edited words. A missing selection
returns `clarification_required`; an unknown capability or unresolved declaration
returns `unsupported`. A selected executable actor capability returns `supported`
and its exact operation, action, title and received source references. This is an
attempt, not an authorization or success prediction. No natural-language meaning
is inferred. `review_id` binds the exact text, selected action, actor and current
host scope; it is a review fence, not an authentication token.

`prepare(..., request_id=..., review_id=..., source_ref=...)` recomputes that
review and returns the existing private `AcceptedIntent` only for an unchanged
supported selection. Unsupported text stays editable and uncommitted. The host
may separately offer the existing unresolved declaration API, with its actual
meaning and explicit acceptance. Unknown or changed reviews raise public
`intent_not_supported` or `review_stale`; private state digests and native
requests must not be given to untrusted clients.

`execute(world, request, current_scope=..., persist=...,
explicitly_accepted=True)` uses actual current actor, authority, resources and
Core handler checks. The host must authenticate, serialize writers, and atomically
CAS-save the candidate and exact returned public DTO. The DTO includes the schema,
request and actor IDs, exact intention, capability ID, actual status, received
receipt and locally rendered presentation. A rejected or unaccepted attempt
commits nothing; a legitimately completed unsuccessful action can have its
selected consequences, including its actual elapsed time. After a lost reply,
reload and retry the identical serialized native request. The original DTO and
receipt return without a second effect. Restore identity fences discarded futures.
Failed persistence leaves the in-memory world unchanged.

`offer_prerequisites` returns `attemptable`, `offer_not_selected` or
`participant_unavailable` from the actor's existing received channel view. It
never probes hidden stock or promises consent; actual terms, authority, custody,
resources and explicit submission remain subject to the existing communication
contract. The default ordinary Rise and quay starts return `offer_not_selected`; an
explicit reviewed optional Rise offer profile can expose an attemptable offer.
See [the current extension](OFFER_AND_DRAFT_EXTENSION.md).
This module itself does not grant authority or make NPC decisions.

`grant_offer_prerequisites(world, actor_id=...)` separately reports the
existing Rise `request_grant` and `accept_grant` capability identities when
selected for the controlled actor. `attempts_selected` is not an offer, consent,
authority or a success prediction: `offer_status` is `not_inspected`, consent
is `not_inferred`, and location and authority are checked on execution. Other
contexts return `not_selected`; no hidden location, mandate, stock or grant is
examined to construct the menu. Use `review`, `prepare` and `execute` for each
actual attempt. The existing R00 procedure may offer the bounded fictional grant;
the player must explicitly submit a separate acceptance. No goods transfer.
This selected scripted procedure is distinct from an optional stock offer and
does not create general NPC decisions. Speech remains testimony even when it
contains words such as “I accept.”

For a selected R00 founder, the result has `schema_version` set to
`irgs-grant-offer-prerequisites-1`, `status: attempts_selected`, and two ordered
`actions` containing `action_id`, actor-specific `capability_id`, `title` and
received `source_refs`. It also has `offer_status: not_inspected`,
`consent_status: not_inferred`, `authority_and_location: checked_on_execution`,
`explicit_acceptance_required: true` and `committed: false`. An unsupported
context reports `status: not_selected` and an empty action list. Use the existing
`irgs-supported-intent-1` review and immutable result/retry DTOs for execution;
this prerequisite response is not itself a pending native request.

## Scope and evidence

Six focused tests across this module and the initial world-draft contract include
ordinary reviewed Rise and fictional quay creation, two sequential selected
operations in each, real blocked shortcut and successful effects, actual wrong-
origin rejection, clarification/unsupported input, no-effect review/unaccepted submission,
atomic host persistence, exact original retry after later work and restore fence.
`test_supported_intent.py` supplies executable calls. The original DTO wraps the selected shared scene/settlement action adapters;
the communication extension below also reuses its existing native handler.
Phase APIs retain their separate contract. General freeform parsing, offer
prerequisites, NPC consent and live AI remain open. App/Catalog need independently
versioned adoption, exact pins and reviewer checks. No Alpha gate is qualified.
See [validation evidence](SUPPORTED_INTENT_VALIDATION.json).

## Communication intent extension — 29 October 2026

Selected speech, offers and received-offer commands now have explicit
`review_communication`, `prepare_communication` and `execute_communication`
methods over the existing native communication handler. See the
[contract and limits](COMMUNICATION_INTENT_PREVIEW.md). General language
interpretation and App adoption remain open; the prior evidence above remains
at its originally tested source.
