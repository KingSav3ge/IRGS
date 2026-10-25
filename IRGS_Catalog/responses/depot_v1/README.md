# Campaign-neutral response depot 1.0.0

This Catalog depot supplies **750 system responses and 250 editable player
drafts**, exactly 1,000 distinct stored variants in 127 families, plus **32 mixing
recipes**. Substitutions, recipes and possible combinations do not inflate that
count. It serves any campaign or theme with suitable established facts; Rise is
one compatibility test case.

The text contains no fixed campaign cast, location, resource or settlement
assumptions. Generic families cover request/recovery states, received records,
inventory, work, places, time and player intentions. A campaign need only expose
the families its actual mechanics and actor-visible projections support.
Original authored text is classified for local presentation and synthetic
evaluation; imported archives and private saves are absent.

## Content identity and ownership

`library.json` uses `library_id: irgs-response-depot-v1`, content version
`1.0.0` and schema version **2**. The default source selected by
`scripted_responses.load_library()` is this depot. Every family declares its
channel, source kind, required public state, role, typed slots, variants and
`intent_tag`. System tags are null; editable drafts carry semantic tags.

The earlier `../routine_v1/` pack is preserved byte for byte under its separate
schema-1 identity for historical Rise qualification. It is not the default
campaign-neutral depot. Do not treat its action-bound draft states as depot
routing. The original JSON SHA-256 is
`4f0c629a6c2c11ee79a305fc5910b3f0caa7290f52d141aa3f867ed4facb361a`.
The new identity permits renamed generic families and slots without silently
changing historical records.

Catalog owns authored text, schema and validation/reference fixtures. Engine
owns runtime selection and its implementation; App owns the implementation
layer, projections, editing and display. This delivery changes no consumer
source, provider routing or dependency pin.

## Campaign adapters and editable intentions

A draft tag such as `observe`, `ask`, `travel` or `begin_task` describes intent,
not an Engine operation ID. Every draft has `state: draft` and
`source_kind: player_request`. Campaign adapters select available families,
supply actor-known labels and map an explicitly submitted intention to their
supported operation/proposal flow. Unsupported intentions remain unresolved
declarations. The presence of a template never establishes a handler,
permission, available resource, NPC agreement or successful outcome.

For example, `player.ask` takes `person_label` and `subject_label`;
`player.travel` takes `destination_label`; `player.begin_task` takes
`task_label`. The same text can use a royal court, fantasy expedition, space
station or modern investigation's supplied names. Those labels are inputs, not
facts selected by Catalog. Rendering submits nothing. Players may edit drafts
and retain the normal explicit confirmation/submission step.

Likewise `inventory.item` takes `resource_label`, `quantity` and `unit`.
`place.capacity` takes `capacity_label` and `capacity_quantity`. The adapter
supplies what that capacity means in its campaign. No default material, unit,
population, calendar, task or work requirement is invented.

## Trusted fact packets

Load and validate the source-pinned library at intake, then keep it immutable
to untrusted callers. Every render context has exactly:

| Field | Host responsibility |
| --- | --- |
| `actor_id` | Authenticated recipient/control scope. |
| `snapshot_id` | Identity covering branch, restore, revision and relevant view. |
| `source_ref` | Stable identity of the legitimate source fact or receipt. |
| `source_kind` | `host_status`, `actor_view`, `received_record`, `committed_receipt` or `player_request`. |
| `state` | The selected family's required actor-safe state. |
| `values` | Exactly the declared bounded labels, nonnegative integers or source text. |

Engine/App construct these packets server-side from their actor-filtered view.
A browser/provider's claimed packet is not authorization. Use separate source
references for distinct facts, and the same reference for alternative states of
one fact. Snapshot identity must change across branch/restore/scope changes.
Do not append current-world facts to a replayed older receipt.

The reference formatter checks structure and consistency; it cannot establish
truth or detect arbitrary hidden facts in prose. Private validation reasons must
not select revealing public messages. Reference browsing does not automatically
become character knowledge. Testimony, uncertainty, pending confirmation and
superseded records retain their source/state labels.

## Local assembly and actual outcomes

Variants are complete clauses or sentences. Choose declared fragments and join
them in recipe order; arbitrary word slicing could remove negation or scope.
Variant selection is explicit and requires no model. All pieces must share one
actor/snapshot, consistent source states and shared facts. At most eight ordered
parts are allowed. Player drafts cannot mix with system messages or combine
into new decisions.

Committed-result recipes require `receipt.exact`, whose only variant is
`{receipt_text}`. It preserves the complete actual actor-visible Engine receipt,
including negation and newlines. Optional elapsed facts and prompts append to
that text. A stock sentence cannot replace or rewrite the actual outcome.
Request completion and physical task completion remain separate facts.

`render_fragment(library, family_id, context, variant=0)` formats one fragment.
`compose_recipe(library, recipe_id, contexts, variants=None)` assembles a recipe.
Unknown families, missing/extra facts, invalid quantities, wrong states and
incompatible mixtures raise `ValueError` for the host to handle. Formatting
expressions, attribute/index access and conversions are forbidden. Inserted text,
even braces or instructions, stays literal data and is never evaluated again.

Returned strings are plain text. App must use its escaping/text-node layer.
Source preservation is not HTML sanitization. Catalog does not read a campaign
world or save when formatting.

## Engine/App handoff

After the ordinary authorization, execution and persistence steps, Engine/App
can select a covered recipe from their actor-safe event and render locally.
Reference rendering uses only Python's standard library, makes **zero API
calls**, and preserves actual Engine outcomes. Cache within the same actor,
branch, restore, revision, source, library version and language.

Reserve approved AI capabilities for demanding supported responses under the
existing host policy and finite limits. Missing text, missing facts or missing
rules alone do not authorize paid fallback. Send only the relevant actor-known
facts and intention if AI is needed; never include the whole depot in prompts.
This content supplies no general dialogue simulation or NPC decisions.
Production token savings must be measured after Engine/App adopt the depot.

## Executed qualification

`tools/tests/test_scripted_response_expansion.py` renders all 1,000 variants,
checks normalized uniqueness and exact counts, exercises all 32 recipes with
required and full fact sets, and uses four synthetic campaign themes.
Those themes prove content portability, not implementations of their mechanics.

`tools/tests/test_response_depot_consumers.py` uses the exact Engine/App
selections in `evaluation/solo_r00_proposals_v1/compatibility.json`. Its synthetic
R00 adapter checks actual committed receipts, projected inventory/place facts,
all 250 non-submitting drafts, zero provider dispatches and unchanged save bytes
during rendering. Historical schema-1 pack tests run separately in the same
suite. See root `RESPONSE_DEPOT_VALIDATION.json` for exact commands, results and
dependency commits. All saves used for qualification are temporary synthetic
fixtures.
