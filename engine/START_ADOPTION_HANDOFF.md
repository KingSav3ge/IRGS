# Start-context adoption handoff — 26 October 2026

Engine's bounded owner task is to support adoption of the published
`irgs-start-readiness-1` contract. The current App can commit the selected Henry
observation through Core, but its normal preflight rejects that selection and
its player view omits the received context. No Engine runtime correction is
indicated by these probes. Runtime/data bytes, schema, release hashes and
component version **3.4.2** remain unchanged from the accepted Engine product
`cc450a6f00a249d2169cdacdfc9c4b1e03f67cc8`.

Use [API 1](START_READINESS_API.md), the executable
[inspection tool](../tools/inspect_start_adoption.py), its
[actual response examples](START_ADOPTION_INSPECTION.json) and the
[execution summary](START_ADOPTION_VALIDATION.json). These are Engine-owned
handoff tooling and evidence; App/Catalog adoption remains with those owners.

## Exact sources inspected

| Owner | Checked-out commit |
| --- | --- |
| Engine parent | `612eb2d7710e28f05b4876e0858eccfbf510cb64` |
| App | `d8e68848454ac7be68ce87fede6d04cc57bda86a` |
| Catalog | `43b3e34cf6bd2463c6998b86e4e87aa60afa75b3` |

App and Catalog are clean independent checkouts. Explicit source selectors load
this Engine and the listed Catalog; App's committed gitlinks still select Engine
`91b20056e7db651966c9e92925313494917f47b1` and Catalog
`3f921252e50a0976cb88321b6ff8249a5f12466d`. No other owner's source or pins are
changed. Keep App's collision fix: `start_preview.py` and
`tests/test_start_preview.py`; Engine owns `start_readiness.py`.

## App review and creation

The following is a call recipe over the selected Engine; it supplies no App
route implementation. The host validates source selection and authenticates the
request before these calls. For an ephemeral preview:

```python
from campaign_library import initial_campaign
from starting_selection import options_for_world, initialize_player
import start_readiness as engine_start_context

raw = initial_campaign(
    'military', 'ephemeral-preview', scenario_id='hundred-years-war',
    entry_id='hyw-1415', snapshot_sha256=reviewed_snapshot_sha256)
options = options_for_world(raw)
character = {'kind': 'existing', 'actor_id': 'HYW-HENRY-V',
             'opening_id': 'henry-1415-embarkation-v1'}
review = engine_start_context.review_start(raw, character)
candidate = initialize_player(raw, character,
    selection_digest=reviewed_selection_digest,
    request_ref='explicit-ephemeral-preview')
actor = candidate.s['gameplay_started']['actor_id']
preview_context = engine_start_context.actor_view(candidate, actor,
    branch_id='ephemeral-preview', restore_id='ephemeral-preview')
```

`review_start` is read-only and requires a fresh, unstarted world. The candidate
is disposable and remains in memory. Execute no action, persist no campaign and
send no provider request during preview. Return the selected mode/limits and
actor-safe projection, retaining the distinction between out-of-character review
and the candidate actor's received context. The inspection JSON includes both.
The App's existing `engine_start_context_contract` marker is recorded for
diagnosis; flipping that flag alone cannot qualify adoption.

Actual creation rebuilds a fresh world with its own campaign identity, revalidates
the reviewed source/options digest, and initializes exactly the accepted
character/opening before the existing atomic initial save. Keep the original
creation request identity and replay behavior. Derive live actor/scope/capability
identities from that world; preview identities cannot authorize actions there.

Display Engine's actor-bound `existing_character_openings` and
`characters[].start_modes` as explicit choices. Let Engine validate the selected
actor, snapshot, opening and digest. A blanket rejection of every existing-person
`opening_id` currently blocks Henry at HTTP 400. Default Henry and John remain
`declaration_only`; John still has a held playable context. The sourced Henry
option does not grant the authored new-character courier setup, a dispatch,
movement, possessions, orders or institutional authority.

## Continuing actor view and time

For a continuing campaign call `engine_start_context.actor_view` on the actual
saved world and currently controlled actor, supplying the host's actual branch
and restore identities. It is also available as
`shared_runtime.actor_view(...)["start_context"]`. Forward that structured actor
context instead of reconstructing it from the historical review. A read must
neither initialize a player nor reload/reapply an opening template. Preserve
actor/source filters and unknown legacy context.

The received `civil_time` is an **initial Julian day checkpoint**, with its own
record/source/status. Preserve explicit unknown hour/time and
`current_calendar_binding: false`. A missing checkpoint stays unknown. Day zero,
storage revision, causal sequence and selected local elapsed seconds are separate
axes. An observation's 20 seconds does not establish a current historical hour
or advance a civil calendar. Pending declarations can suppress action menus
without erasing legitimately received time/context.

Use the received selected scene classification and actual supported operations
for the scene label and first-decision guidance. Henry currently gets
`authored_fiction` and a prompt to move/observe/deliver a dispatch. The selected
context supports only its bounded observation and carries sourced uncertainty;
the original authored courier remains a distinct choice for a new character.

The inspection additionally reproduces a **START-INT-003 result-axis bug**:
`Store._supported_action` hardcodes `authored-opening-seconds` into the immutable
App result for every scene action. Henry's Core result actually uses
`selected-historical-observation-seconds`. At the native action's successful
commit boundary, copy the selected `world.s['scene_rules']['elapsed_axis']`,
consistent with Core's `elapsed_time.axis`, together with the actual resolved
`elapsed_seconds`/`elapsed_total`. Persist the world and correctly labelled
result together once. Retry/result lookup must return that original DTO.
Do not relabel old saved receipts using the current world's later state.
Live elapsed projection likewise follows the actor's received selected context,
instead of matching only the courier axis. None of this introduces a timing rule.

## Catalog selection and independent consumers

`player_starts_v1` keeps its original strict fixture/consumer identities. The
inspection loads its validated actor inputs and records the unchanged manifest
hash. It also uses original R00 setup choices/actions without transmitting its
evaluator oracle into actor/model packets. That reuse does not qualify a Catalog
new-contract consumer or authorize repinning the historical fixture.

Catalog's START-INT-006 needs a separate versioned selection, independent
expectations and consumers for selected/default Henry, John, default/authored new
character and R00. Retain source uncertainty, actor privacy, original receipt
replay and save/reload checks, received day precision, independent local elapsed
time and absence of fabricated stock/authority. Baseline schema checks passing
below do not close that owner task.

## Executed checks and next dependencies

Run the probe from Engine with explicit clean independent roots:

```bash
python -B tools/inspect_start_adoption.py \
  --app-root ../IRGS-APP-WEB --catalog-root ../IRGS-Catalog \
  --output /tmp/start-adoption-inspection.json
```

Exit **2** records `BLOCKED_CONSUMER_ADOPTION`; exit **0** means only that the
probed App boundaries agree within the stated limits. Unexpected Engine/backend
errors raise. The current run makes **33 real loopback HTTP requests** over six
contexts. Henry commits one actual 20-second observation with exact retry,
original-result lookup and fresh-store reload; R00 completes five actions and
3,900 selected seconds. Default/selected modes and received evidence sets remain
distinct. Separate direct backend creation is diagnostic and cannot count as a
successful wizard journey when preflight fails.

The current 23 field comparisons contain **15 mismatches**, overlapping
START-INT-002/003. They are diagnostic comparisons, not 23 unittest cases or 15
independent bugs. Fresh checks also pass **33 Engine readiness**, **32 Engine
communication**, **nine Catalog baseline contract** and **five App legacy
preflight** cases, with zero skips in those selections. The three old App
empty-knowledge expectations were rerun against the candidate: **three failures,
zero passes/skips**. App must assert the legitimate calendar provenance while
retaining its privacy/no-operational-news checks (START-INT-004).

Engine integrity passes for 367 source files. The runtime/data tree is identical
to the accepted product, so the full 773-case runtime suite was not rerun here;
the coordinator's 772 passes/one absent historical-save skip remain attributed
prior evidence. No private-save fixture, user campaign/configuration, live
inference, browser, Windows or package qualification participates in this run.

Engine's bounded handoff support is delivered. App still owns START-INT-002/003/004
and its exact dependency update START-INT-005; Catalog owns START-INT-006.
Support concrete contract feedback first. Resume selected native travel only
after adoption. The coordinator owns all-three approval, exact compatible pins,
joined/browser/package qualification and the eventual unified 3.4.3 publication.
