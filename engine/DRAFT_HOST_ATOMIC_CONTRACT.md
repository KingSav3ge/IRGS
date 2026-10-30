# Bounded world-draft host creation and recovery contract

Status: design contract for App/host adoption, 29 October 2026. The existing
Engine `world_draft` validates and initializes only the selected fictional Rise
and mixed historical-quay profiles. It creates an in-memory candidate; this
document does not implement durable creation, a host API, or a Creator playtest.
Preview remains disposable and its identities are not creation identities.

## Creation boundary

A trusted host authenticates the owner and authorizes creation before accepting
any draft, request, or campaign identifier. It binds a new host-scoped, stable
request ID to the authenticated principal, exact draft, draft/review digests,
explicit acceptance, intended campaign ID and a host-assigned initial branch and
restore identity. The host must bound and validate all fields; IDs are opaque,
not paths or proof of authority. A changed bound field under the same request ID
is a conflict, not a second creation. IDs and conflict responses must not disclose
another principal's campaigns or requests.

Under a serializable transaction or equivalent crash-safe compare-and-set, the
host checks request uniqueness and campaign absence, recomputes the Engine review
and invokes `world_draft.initialize` with the reviewed digests and explicit
acceptance. The candidate stays private until a single durable commit publishes
all of: initialized Core state, authenticated ownership/access, campaign and
branch/restore identities, an immutable request fingerprint and the original
actor-scoped public creation result. The result identifies the campaign, branch,
restore identity, controlled actor and actor-filtered initial view; it contains no
raw world, hidden template, other actor's records, or private draft contents. It
must not treat the review digest as an authentication token. Use only actual
Engine data: do not infer NPC consent, assets, resources or historical hours.

Rejection, stale review, duplicate campaign ID, lost authorization, initialization
error or failed persistence must leave no visible campaign, owner record, request
receipt, partial save, or in-memory authoritative world. Concurrent identical
requests must produce one campaign and one result; conflicting requests cannot
overwrite one another. Publication must make the complete tuple visible at once.
A success response is sent only after durable commit. Process interruption before
commit leaves no published creation; after commit, lookup recovers the same result.
No provider dispatch belongs in this transaction.

## Retry, continuation and restore

A retry is authorized against the original principal and submits the same bound
payload and request ID. It returns the exact stored public result, including its
original actor-scoped initial view, with no second initializer, effect, or write;
current world state must never be substituted for that result. An altered payload
is rejected even if the first response was lost. Subsequent game operations use
the existing shared-intent/communication APIs and their own scope and immutable
receipts; the creation receipt is not authority to submit them.

Backups/restores must preserve ownership, original creation request fingerprint
and receipt consistently with the campaign state. Restoring an earlier state
must install a fresh restore identity and fence submissions from discarded
futures. A pre-restore creation retry may return its original immutable receipt
only after authorization and only if the host can establish it belongs to the
same surviving creation; it must not re-create a deleted campaign or reopen a
discarded branch. The stored original restore identity is historical: it must not
be presented as the current submission scope. If identity or retained receipt
cannot be established, return a safe recovery error and require an explicit new
creation; never guess or silently generate a replacement. Atomic restore must not
expose a mixed state/ownership/receipt set. Host retention and deletion policy
must specify how long retry evidence and tombstones survive, including backups.

## Qualification required before claiming playtest support

Exercise both profiles through the real host and App: review and cancel without a
write; authorized explicit creation; exact retry after lost response, restart and
later play; concurrent identical and altered requests; identity collisions;
stale review; failed/partial disk writes and crash on both sides of commit;
unauthorized lookup; backup/restore and discarded-future fences; actor-filtered
results and actual subsequent play. Verify persistence on supported platforms and
run independent Catalog consumers using exact selected pins. No such host or App
qualification is claimed by this document.
