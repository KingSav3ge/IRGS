# Routine response library 1.0.0

The user requested reusable scripted responses to reduce Player and System API
token usage, reserving AI for more demanding responses. This first library
contains **325 authored variants in 82 families and 12 composition recipes**.
It covers routine request/recovery messages, received information, inventory,
elapsed time, projects, camp facts and editable player drafts. No imported
campaign prose, historical archive, private save or evaluator oracle is included.

`library.json` is versioned Catalog content. `IRGS_Catalog/scripted_responses.py`
validates and formats it deterministically with the Python standard library. A
local rendering makes zero provider requests and requires no model input/output
tokens. This does not refund or reinterpret accounting for any earlier attempt.
Production token savings require Engine/App to select this path; this Catalog
delivery does not change their sources, dependency pins or provider routing.

## Reuse whole clauses

Variants are complete clauses or sentences. Combine these declared pieces rather
than slicing arbitrary words, which could remove negation, attribution or scope.
Choose the family from an actor-safe public event/status, then select a stored
variant without a model call. Variant selection is explicit and deterministic;
retain that choice for repeat presentation of the same event. Labels/numbers
fill strict named slots. Format expressions, attribute/index access, conversions
and undeclared fields are rejected at content intake.

Recipes provide compatible ordering and required facts. All pieces must belong
to the same actor and snapshot, with consistent states and shared values for
the same source fact. Player intention drafts cannot mix with system messages or
be combined into new decisions. Rendering a draft submits nothing; the player
can edit it and retains the normal explicit submission/confirmation step.
There are four draft variants for each of the current 13 Rise action IDs.
Their presence does not establish feasibility, permission or guaranteed success.

Committed-result recipes always include `receipt.exact`, preserving the complete
actual actor-visible receipt text, including negation and line breaks. They may
append the actual elapsed span and a neutral next-decision prompt. They cannot
replace a real result with a stock success sentence. A request completing and a
physical project completing remain distinct. Zero elapsed seconds stay zero;
no fixed duration, civil date, material, event or NPC decision is invented.

## Trusted host contract

Load and validate the source-pinned library once at host intake. Formatting APIs
accept that validated library; keep it immutable to untrusted callers. Catalog
does not authenticate actors, inspect a world, select rules or establish truth.
Engine/App must build each context server-side from their current actor-filtered
projection, a legitimate received record, an actual committed receipt, an
actor-safe host status or an explicitly selected player draft. Never accept a
browser/provider's claimed context as authorization.

Every context contains exactly:

| Field | Meaning |
| --- | --- |
| `actor_id` | Authenticated recipient/control scope, supplied by the host. |
| `snapshot_id` | Opaque identity of the relevant branch/restore/revision/view. |
| `source_ref` | Identity of the actor-legitimate source fact or receipt. |
| `source_kind` | `host_status`, `actor_view`, `received_record`, `committed_receipt` or `player_request`. |
| `state` | The family's required public state, explicitly supplied by the host. |
| `values` | Only declared scalar slots: bounded label, nonnegative integer or received source text. |

For example, use `view:project:shelter:status` for a project status fact and
`view:project:shelter:progress` for the separate progress fact. Give alternative
states of the same fact the same reference so conflicting assembly is rejected.
Snapshot identity must change across restore, branch, revision or relevant scope
changes, even when a restored save has identical bytes. A replayed result uses
its original result snapshot; do not append current-world facts to an older
receipt. Do not use private world hashes as visible prose or cache keys exposed
to the player. Returned text contains no actor/snapshot metadata.

Only choose error/cause messages from public facts the actor may receive. A
private validator certificate cannot select a revealing rejection explanation.
Testimony stays testimony, uncertainty stays uncertain, and superseded records
stay superseded. Do not turn historical reference browsing into character
knowledge. Inventory quantities/units require the App's actual inspection view;
absence of that view establishes no empty stock or ownership. Source-text slots
remain data even if they contain instructions or braces.

The result is **plain text**. Use App text nodes or its existing escaping layer;
never treat inserted names or received records as HTML. Source text is preserved,
not sanitized into a different assertion. The Catalog formatter cannot detect
all hidden facts or false claims inside arbitrary prose: actor filtering and
source validation remain mandatory host duties.

## API example

```python
from scripted_responses import load_library, compose_recipe

library = load_library()
# This example frame is supplied only after the host validates the real receipt.
scope = dict(actor_id='founder', snapshot_id='branch-A:restore-B:revision-3')
message = compose_recipe(library, 'routine.result', {
    'receipt.exact': dict(**scope, source_ref='receipt:event-3',
        source_kind='committed_receipt', state='committed',
        values={'receipt_text': 'Inputs are reserved; the shelter is not complete.'}),
    'elapsed.action': dict(**scope, source_ref='receipt:event-3',
        source_kind='committed_receipt', state='committed',
        values={'elapsed_seconds': 0})
}, variants={'elapsed.action': 1})
```

This produces the exact receipt followed by “This action recorded 0 elapsed
seconds.” `render_fragment(library, family_id, context, variant=0)` formats one
piece; `compose(library, parts)` accepts at most eight ordered whole pieces.
Unknown families, missing facts, wrong sources/states and incompatible mixtures
raise `ValueError`. No missing fact is filled by a guess or automatic API call.

## Routine-first handoff to Engine/App

1. Complete the ordinary authorization, action and persistence procedures. Build
   the actor-safe presentation event; the library never causes an action.
2. For a covered routine response, bind a recipe to those existing facts and
   render locally. Use selected canned player drafts as editable suggestions.
3. Cache only the small rendered message/recipe selection within the same actor,
   branch, restore, revision, source identities, library version and language.
   Do not share personalized caches across actors or restored branches.
4. For demanding reasoning or supported expressive responses, Engine may use its
   approved AI capability after normal consent, scope, policy and finite-limit
   checks. Send only relevant actor-known facts and intent, not this whole library
   or a raw save. A missing template alone must not authorize a paid call.
5. Unsupported mechanics and missing established facts remain unresolved. The
   existing general narration/dialogue contract is still unfinished; these local
   presentation phrases do not implement it or supply new NPC speech/decisions.

Suggested current mappings include `proposal_ready` → `proposal.ready`,
`declared_not_resolved` → `request.unresolved`, `unconfigured` →
`request.unconfigured`, and `unsupported_action` → `request.unsupported`.
The host must explicitly review mappings rather than equating every technical
failure with a public cause. Do not load the library into every provider prompt.
It is local content that avoids those calls for covered presentation tasks.

## Checks and scope

```bash
python -B IRGS_Catalog/scripted_responses.py
python -B -m unittest tools.tests.test_scripted_responses -v
IRGS_SCRIPT_ENGINE_SOURCE=/path/to/selected/Engine \
IRGS_SCRIPT_APP_SOURCE=/path/to/selected/App \
python -B -m unittest tools.tests.test_scripted_response_consumers -v
```

Consumer selection reuses the exact commits in
`evaluation/solo_r00_proposals_v1/compatibility.json`. Five consumer tests use the
actual App projections and five actual R00 actions, preserve the receipt and
save bytes during rendering, and assert the Engine provider dispatcher is never
called. The 13 standalone tests render all 325 variants and exercise missing or
conflicting facts, actors/snapshots, quantity types, expression injection,
negation, attribution, state/role rules and player agency. Source validation is
not proof of runtime integration or semantic quality. Engine/App pinning and
their actual routine-first use remain coordinator/consumer work; no production
API saving or live model evaluation is claimed by this content-only handoff.
