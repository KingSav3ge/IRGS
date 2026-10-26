# Actor/start-mode readiness — API 1

IRGS 3.4.2 development; schema `irgs-start-readiness-1`. This is the first
Engine increment for IRGS-PLAY-001/002/004. It uses existing Core 3.3 handlers,
requires no App/Catalog checkout or provider, and changes no historical snapshot
or prior fixture identity. General freeform resolution remains unavailable.

## Review before creation

`starting_selection.starting_options(...)` retains its existing fields and adds:

- `start_readiness`: versioned reference/presentation status, civil-date reference
  and new-character modes/requirements. These are out-of-character review data.
- `characters[].start_modes`: eligibility and executable readiness are separate.
- `existing_character_openings`: independently reviewed existing-person options,
  each bound to its actual actor, dated snapshot and content digest.

`start_readiness.review_start(new_world, character)` returns the selected mode,
character eligibility, presentation-only opening status, held reason and civil
reference. It mutates nothing and rejects already started worlds. A current host
recomputes the full options/`selection_digest` before initialization. The public
preview and a caller-supplied digest grant no authority on their own.

| Selection | Mode | Meaning |
| --- | --- | --- |
| Eligible existing John of Lancaster, 1415 | `declaration_only`; playable context `held` | Verified reference/eligibility does not establish his whereabouts, received operational context or a playable handler. |
| Existing Henry V, no explicit opening | `declaration_only` | The new optional context is never attached silently. |
| Existing Henry V, `henry-1415-embarkation-v1` | `supported_slice` | One selected local observation in a sourced broad Portchester/Solent setting. |
| New human, explicit reviewed quay/local opening | `supported_slice` | Existing authored courier fiction, with its own geography, custody and selected durations. |
| New character without an opening | `declaration_only` | Exact declarations can be retained; unsupported acts do not acquire outcomes. |
| Ineligible actor or incompatible opening/species | `held` | A title, background statement, theme or presentation supplies no capability. |

Modes and reasons use selected adapters and received context. They do not query
hidden stock, authorization, weather, NPC locations or action outcomes to choose
successful options. An attemptable option may be rejected by actual Core checks.
Pre-creation metadata is not the character's knowledge. The App must present a
mode choice and its limits explicitly; these Engine fields do not create a UI.

## Existing-person creation and first action

```python
from starting_selection import options_for_world, initialize_player
import start_readiness

options = options_for_world(new_world)
character = {"kind": "existing", "actor_id": "HYW-HENRY-V",
             "opening_id": "henry-1415-embarkation-v1"}
review = start_readiness.review_start(new_world, character)
# Show the actual person, mode, sourced limits and selected observation rule.
world = initialize_player(new_world, character,
    selection_digest=options["selection_digest"], request_ref=reviewed_creation_id)
# The host saves this complete candidate atomically as its initial campaign.
```

`character_background.validate_background` now accepts `opening_id` for an
existing person only when the reviewed option matches that actor and snapshot.
Other existing people cannot borrow Henry's context or the fictional courier
opening. Content digests participate in the starting review; changed pack bytes
cannot pass an old selection or change between review and installation.

The Henry pack is [original technical configuration with citations](../IRGS_3_3/data/henry_1415_observation.json).
Dan Spencer's two research summaries support the broad embarkation setting but
record conflicting boarding dates. Initialization does not choose a room, berth,
barge or ship, or copy later departure/landing into the world. The exact place,
hour, health, possessions, introductions, orders and command authority stay
unestablished. John remains explicitly held for a playable context. Rank grants
no stock, troops, institutional mandate or other person's obedience.

The first actual operation is the existing `execute_player_scene_action`,
`observe-embarkation`. Its **20 seconds** are an explicitly selected bounded
simulation observation rule, not a historically measured or universal duration.
The actual received result establishes the local gathered shipping without
numbers, loading/readiness findings, a secret destination or NPC choices.
It changes legitimate received knowledge and the selected elapsed axis, with no
stock creation/transfer, automatic travel or civil-calendar advancement.

Execute with existing `shared_runtime.prepare_intent` / `execute_intent`, using
the actual capability ID, exact edited intention, explicit boolean acceptance
and mandatory host save/result CAS. Private execution dependencies stay private.
Retry retrieves the original result; it does not repeat perception or elapsed
work. Restores rotate identity. These are the existing shared recovery contracts.

## First known view and civil precision

`start_readiness.actor_view(world, actor, branch_id=..., restore_id=...)` is also
available as `shared_runtime.actor_view(...)["start_context"]`. It exposes only
the controlled actor's saved selected mode, actual shared-adapter capabilities,
legitimately received setup records and received initial civil checkpoint.
`capability_scope` names the shared execution adapters; native-only/equipment
interfaces retain their separate APIs. No read installs or repairs context.

For newly initialized historical worlds `campaign_time.civil` records the exact
selected Julian date, day precision, ordinal and snapshot source, with no hour.
Creation explicitly receives a separate calendar reference for the selected
actor. Generic/legacy profiles without established civil dates retain unknowns.
The calendar receipt precedes later exact player background testimony, so it
does not replace that testimony in existing latest-received opening views.
The actor contract reads this received record, never the historical template.
It labels the date `received_initial_checkpoint` and
`current_calendar_binding: false`. Campaign day, causal sequence, storage
revision and local elapsed seconds retain their independent meanings. Advancing
20 local seconds does not manufacture an opening hour or a current civil clock.

Only new-world initialization receives this context. Continuing saves, restores,
diverged actors and historical reference reads are never reset or reseeded.
Existing snapshots, archives, canonical history and old manifests remain intact.
Views contain no full templates, raw saves, hidden resources or dependency hashes.

## Qualification and component handoff

The initial API was published early at
`ea3b9a24f3254b4e230469b31843abad6c25fdf2`, with ten new cases and 57 focused
regressions passing. [Final Engine qualification](START_READINESS_VALIDATION.json)
now records **33 dedicated cases**; the full runtime runs **773**, with **772
passes and one prescribed private-save exclusion**. Shared (35), phase (28),
communication (32), original pinned R00 (10), Engine integrity (367 source files)
and Kira canon checks pass. The 33 cases are included in the full suite.

Real [App HTTP qualification](START_INTERACTION_VALIDATION.json) passes three
checks for starting metadata, default/new/existing-mode separation, Henry
creation and two actual observations (20 seconds each), durable result lookup,
changed replay rejection and reload/continuation. It selects App
`00634b15f2d8d4a8626d3eb3cb0a139559ac1fcc` and Catalog
`3f921252e50a0976cb88321b6ff8249a5f12466d` explicitly. Their source and pins are
unchanged; this is candidate compatibility, not joined/UI release qualification.

The [complete delivery record](START_DELIVERY_VALIDATION.json) records the
existing App suite against this candidate: **229 run, 219 pass, three failures,
seven Windows skips**. The three assertions require empty knowledge at historical
creation, conflicting with the new sourced calendar receipt. All three pass
against App's original Engine pin `91b20056e7db651966c9e92925313494917f47b1`.
App must adopt structured context/date presentation and update those expectations
while preserving the exclusion of unsourced operational news. No App source/test
or dependency pointer is changed by this Engine delivery. This increment remains
blocked from exact-set joined qualification until its consumers are updated.

All 37 original historical snapshot files and both response banks are unchanged.
No user save, provider call, new browser/package qualification or version increase
participates. John and other unsupported starts remain explicitly held; one
optional Henry observation is not general historical campaign playability.

App owns review/creation controls, first-known-view presentation, civil-date
display and supported-intent mapping. Catalog owns independent source requirements
and consumer cases. Exact compatible pins and coordinator joined/package review
follow the final Engine evidence. Communication remains delivered; selected
travel expansion follows this bounded start increment.

## Current adoption support — 26 October 2026

[The current handoff](START_ADOPTION_HANDOFF.md) provides concrete pre-creation
and continuing-view call recipes, actual Engine JSON examples and a repeatable
six-context App probe. [Fresh evidence](START_ADOPTION_VALIDATION.json) selects
App `d8e6884` and Catalog `43b3e34` without changing their code, pins or historical
consumer identities. It reproduces the coordinator's App adoption gaps and an
additional hardcoded elapsed-axis label in the App's saved result. Engine
runtime/data, this schema and release hashes remain identical to accepted
`cc450a6`. The preceding delivery counts remain dated evidence at their stated
sources. App/Catalog adoption and coordinator exact-set review still precede
selected native travel and joined publication.
