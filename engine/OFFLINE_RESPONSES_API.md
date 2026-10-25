# Engine responses without an API token

For cross-campaign contracts and the new exact 750-system/250-draft depot, use [Shared Engine API 1](SHARED_SYSTEMS_API.md). This document preserves the earlier 338-variant compatibility API and its original scope.

The Engine bundles its own validated text library and renders actual Core results locally. It needs no API key, provider account, network connection, Catalog installation or inference budget. Supported action APIs return a `presentation` field automatically; presentation changes no world state, elapsed time, stock, accepted intention or outcome.

The Engine library contains **338 variants in 86 families, with 15 mixing recipes**: 285 system responses and 53 player draft templates. It retains Catalog's 325 authored variants and adds 13 Engine variants for phase progress, attributed speech, offer status and exact authored scene drafts. Source attribution, commit and hashes are preserved in [provenance](../IRGS_3_3/data/responses/PROVENANCE.json). The [Engine bank](../IRGS_3_3/data/responses/engine_routine_v1.json) and [formatter](../IRGS_3_3/runtime/routine_format.py) ship independently of Catalog.

## Result API

From the Engine runtime import path:

```python
from offline_responses import render_receipt, player_drafts, render_status

# world is the host's actual selected CoreWorld; authenticate actor first.
response = render_receipt(world, actor, committed_event_id)
display_plain_text(response['text'])

# Selection/editing commits nothing. Explicit submission is still required.
suggestions = player_drafts(world, actor)
status = render_status(actor_id=actor, snapshot_id='host-request-42',
                       status='declared_not_resolved')
```

`scene_actions.execute_scene_action`, `settlement_runtime.execute`, `solo_actions.accept_proposal`, `process_runtime.execute` and `communication_runtime.execute` automatically attach the same local presentation to their public results. The authoritative Core records and checksums contain no rendered text. Existing equipment summaries also remain local and require no provider.

`render_receipt(world, actor, event_id, scope=None, variant_seed=0)` accepts an actual committed event identity, never a caller-supplied outcome packet. It checks current player control, the event actor or actual communication reception, and optional `WorldScope` campaign/state freshness. The host authenticates sessions, selects the current branch/restore world, and durably stores the original public result with its save. Scope checks do not authenticate a client or independently establish branch identity.

The returned DTO includes `text`, `format: plain_text`, actor/snapshot identity, library ID/version, selected family/variant indexes, and `render_usage: {provider_calls: 0, model_tokens: 0}`. This usage describes rendering only. Earlier inference attempts retain their own charges and reservations. `variant_seed` changes wording; it cannot select effects. The display must escape text for HTML or other markup surfaces.

## Sources and recovery

- Local scenes preserve the exact committed summary, observations and action elapsed span, including unsuccessful attempts.
- Rise preserves original actor receipts and the same event's inspection. Its stored elapsed value is cumulative, so the renderer does not label it an action duration.
- Processes preserve the original phase summary, status, progress and elapsed span, including zero. A completed observation may add its actually received observation. Later live project progress is never appended to an older phase.
- Communication preserves the speaker's exact words as **testimony**. Offer status and terms come from that communication's immutable result. Only actual explicit fulfillment can be described as fulfilled; words claiming acceptance transfer nothing. Causal ticks are never turned into speech duration.

Rendering and replay never execute an action. Only the authored library is cached; actor/world responses are recomputed from the selected actual receipt. Restart, later stock changes and another actor's context cannot supply new facts to an old response. If text is missing, invalid or too large for scripted formatting, an authorized committed result uses its exact literal receipt, retaining attribution and phase facts. There is no paid fallback, recursive string expansion, truncation or invented success. Missing authorization or an unknown receipt fails closed.

The lower-level formatter accepts trusted fact packets for hosts implementing additional projections. It is presentation code, not a truth validator. It rejects unsafe placeholders, source/state mismatches, conflicting facts, mixed actors/snapshots, mixed player/system text and committed compositions lacking the exact receipt anchor. Additional bank families are reusable presentation vocabulary; their presence establishes no Engine mechanic or automatic projection of private inventory.

## Editable intentions and public status

`player_drafts` exposes all 52 Rise draft variants for the selected founder, or exact authored scene text for received local options, plus an editable custom response field. It does not inspect private blockers, remaining stock or outcome feasibility to choose a winning menu. Draft selection changes no world or save. Editing text never silently authorizes its associated structured action; hosts retain explicit intention review, submission and current Core validation.

`render_status` accepts explicit public `proposal_ready`, `declared_not_resolved`, `acceptance_required` and `unavailable` states. Unknown/private diagnostic codes receive generic unavailable wording. Freeform intentions and combat keep their existing unresolved status; local text adds no adjudication or general natural-language interpreter.

## Verification and remaining integration

Run the standalone Engine qualification:

```bash
python -B tools/qualify_offline_responses.py --output engine/OFFLINE_RESPONSES_VALIDATION.json
python -B -m unittest discover -s IRGS_3_3/runtime -q
```

The [execution record](OFFLINE_RESPONSES_VALIDATION.json) covers all 338 variants and all 15 recipes, default result adoption, unsuccessful outcomes, editable drafts, actor/privacy checks, stale scope, replay/restart, phase information timing, offer fulfillment, literal fallback and forbidden provider/network access. Tests use synthetic temporary saves. Catalog's 132 prior test executions describe its own delivery; Engine evidence is reported separately. App display/adapters, updated component pins and joined qualification remain with their respective owners.
