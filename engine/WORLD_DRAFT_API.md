# World draft preview — first Engine contract

WB-ENG-01 bounded implementation, 29 October 2026; IRGS 3.4.5 Pre-Alpha.
`IRGS_3_3/runtime/world_draft.py` defines `irgs-world-draft-1` and validation
DTO `irgs-world-validation-1`. The selected profiles are the existing fictional `rise-r00` and
the `mixed` historical setting with fictional `historical-quay` opening; this is
not an editor, package importer or general world initializer. No external source code, artwork or user campaign is involved.

A draft has exactly `schema_version`, `draft_id`, `classification`, `profile_id`
and selected profile `choices`. Rise uses `fictional`/`rise-r00` and choices
accepted by `settlement_setup.preview`; the quay uses `mixed`/`historical-quay`,
the exact selected snapshot SHA and a new human selecting `quay-contact-v1`.
Extra keys, including scripts, are rejected. `inspect(draft)` returns a detached
valid review or an `invalid` DTO with an actionable error; `validate(draft)`
returns the same valid result or raises `ValueError`. Validation copies choices,
uses the existing selected profile/rules and has no campaign effects. Its valid
DTO contains draft and review digests, the actual selected-profile review, proposed existing
initializer, and explicit unsupported areas.

`initialize(draft, draft_digest=..., review_digest=..., campaign_id=...,
explicitly_accepted=True)` validates again and produces a new Core world through the selected existing
Rise or historical-start initializer. Changed drafts/rules, unsupported profiles and
non-boolean acceptance reject. The caller owns unique campaign IDs, access
control, atomic creation/save/result handling, duplicate retry and restore
fencing; this function alone does not publish, save, edit a live world or qualify
those host obligations. Existing Rise content and rules remain authoritative.

Custom geography/entities, general historical drafts, assets, package
import/export, arbitrary scripting, mutable playthrough editing and two-context
creator acceptance remain unsupported. App owns a Creator editor and persistence;
Catalog owns independent original examples and source review. See the shared
[World Builder plan](../WORLD_BUILDER_PLAN.md) and
[validation evidence](SUPPORTED_INTENT_VALIDATION.json).

## Existing initializer inventory

- `campaign_library.initial_campaign` builds a selected campaign profile and,
  when requested, checks the historical entry and snapshot digest. It is not a
  generic world-pack importer.
- `starting_selection.options_for_world` reviews selection on a new world;
  `initialize_player` validates the selected character and digest and initializes
  a new candidate before its first save.
- `scene_setup.initialize_opening` installs an explicitly selected, reviewed
  existing authored local opening or sourced person context. It does not accept
  arbitrary editor-provided scene rules.
- `settlement_setup.preview` and `settlement_setup.initialize` supply the Rise
  binding; the selected quay binding uses the existing historical and player
  initialization entries above. Core owns the resulting state;
  this wrapper supplies no independent simulation authority.

These are existing implementation entry points, not a claim that all are already
exposed through this draft schema. Source assertions, coordinates, topology,
custom items, arbitrary actors and external package dependencies require their
own versioned validation and reviewed initializer before they can be accepted.

See [the current two-context extension](OFFER_AND_DRAFT_EXTENSION.md) and its
[executed evidence](OFFER_AND_DRAFT_VALIDATION.json). The earlier validation
record remains dated at its actual source.

## Disposable initialization preview — 29 October 2026

`preview_initialization(draft)` returns a scoped controlled-actor view from a
disposable in-memory candidate for either selected profile. It does not save a
campaign, and preview identities cannot authorize the later world. See
[details and evidence](COMMUNICATION_INTENT_PREVIEW.md).
