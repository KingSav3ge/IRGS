# Shared response consumer fixture 1

This separately versioned synthetic evaluation material qualifies the unchanged
campaign-neutral depot against published Engine/App interfaces in two independently
initialized contexts. It adds no campaign, playable start, adapter or simulation rule.

- Rise R00 uses the existing synthetic setup and actual
  `rise_campaigns.create/action` → `execute_settlement_action` path.
- The non-Rise case explicitly selects the existing optional fictional
  `quay-delivery-v1` opening in Hundred Years' War 1415 through
  `starting_options` and `Store.create`, then uses `Store.supported_action` →
  `execute_player_scene_action`. The historical checkpoint, fictional map,
  dispatch custody and selected durations remain Engine-owned.

The same Catalog `routine.result` recipe preserves actual actor-visible
summaries and observations and appends the actual action duration. Rise and
authored-scene public results use different duration field names; the evaluator
reads those existing fields explicitly. Cumulative elapsed time is never
presented as a new action's duration. All 1,000 depot variants, 750/250 split and
32 recipes remain byte-identical to the previous delivery.

## Provenance and separation

`manifest.json` binds exact Engine/App commits, the App's committed Catalog
pointer, the depot hash and the three payload hashes. `actor_inputs/` contains
only evaluation case/action/request identities and an authored source reference.
`evaluator_only/oracle.json` separately contains expected outcomes, spans,
conserved dispatch counts and an evaluator privacy marker.

`response_depot_compatibility.export_actor_input(context_id)` validates and
exports only the selected actor document; no oracle is returned. This fixture
uses original authored evaluation instructions, with local/offline synthetic
processing rights. It grants no external-provider processing permission and
copies no archive, historical prose, private save or campaign canon.

Initialization uses each owner's existing interface. The evaluator reads the
actual listed action wording and current player projection; it does not install
new scene rules, bypass campaign creation review or infer feasibility from
private conditions. Evaluator expectations never select Engine outcomes.

## Qualification scope

Nine reference cases exercise two Rise actions and seven quay actions. The quay
arc includes an unsuccessful gate attempt, observation, movement, one conserved
dispatch delivery and a second unsuccessful delivery. Final elapsed time is
180 local seconds for the quay case and 300 for the short Rise regression.
Civil campaign time is unchanged. These checks qualify only those selected
handlers and starts.

Eight actual-consumer tests also exercise lost acknowledgement, fresh Store
instances, concurrent exact retries, stale requests, foreign actors, stable older
receipts, incompatible actor/snapshot mixtures, non-submitting drafts, unresolved
unbound declarations and Engine's authorized literal-receipt fallback. Provider
broker dispatch, direct HTTP transport and socket connections are instrumented
to fail during these routine operations. Rendering checks save-byte immutability.

Engine's independent offline runtime still selects its own 338-variant pack;
its provenance retains 325 original Catalog variants. App owns its separate UI
pack. This fixture tests current outcomes through Catalog's reference recipe;
it does not claim either consumer automatically adopts the newer 1,000-variant
depot or that production token savings have been measured.

## Run

Use Python 3.12+ without `-O`. Consumer selections require clean exact repository
roots, including the App's recorded Engine and Catalog pointers. Run in a fresh
process to prevent Python imports from another dependency selection:

```bash
python -B IRGS_Catalog/response_depot_compatibility.py
python -B -m unittest tools.tests.test_shared_response_contract -v
IRGS_SHARED_ENGINE_SOURCE=/path/to/selected/Engine \
IRGS_SHARED_APP_SOURCE=/path/to/selected/App \
python -B -m unittest tools.tests.test_shared_response_consumers -v
```

See root `SHARED_RESPONSE_VALIDATION.json` for executed commands, exact source
identities and limits. Prior fixture, depot and proposal evidence remains
unchanged. General dialogue, freeform mechanics, other campaign adapters,
production savings and joined release qualification retain their separate scope.
