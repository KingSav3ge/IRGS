# Synthetic Solo R00 evaluation fixture 1.0.0

Fixture ID: `irgs-solo-r00-eval-v1`. JSON schema version: `1`, implemented by
`IRGS_Catalog/solo_evaluation.py`. This is original synthetic evaluation content
derived from the fictional `rise-foundation-1` R00 demonstration. It is
uncalibrated and contributes no public discovery entry, canon, playable start,
entitlement or release approval. The existing 44 previews are unchanged.

## Loading and the information boundary

`manifest.json` binds each file by SHA-256, records provenance and explicit
processing rights, and selects the tested operation contract and dependencies:

- Engine `723627e629231b5e90f38b9d52b65c9a3967b92a`.
- App `d8dc35ed653e516ccd0cacf91ee9693258491032`.
- Core operation `execute_settlement_action`; its supported action IDs are
  checked against the actual Engine registry by the consumer tests.

Load and validate this fixture from a trusted Catalog release at evaluation
intake. Schema validation is independent of source hash refresh; actual consumer
tests establish behavior. Neither check grants campaign approval.

```bash
python -B IRGS_Catalog/solo_evaluation.py
python -B IRGS_Catalog/solo_evaluation.py --export-actor solo-walk
```

For programmatic use, put `IRGS_Catalog/` on the import path and use:

```python
from solo_evaluation import validate_fixture, export_actor_input, load_evaluator_data

validate_fixture()  # Evaluator intake; checks all files and their separation.
actor_input = export_actor_input('solo-walk')  # The only model-input export API.
evaluator = load_evaluator_data()  # Evaluator process only; never send this object.
```

`actor_inputs/` contains one small document per case: identity, source and intent
references, processing classification, explicit founder intent and a limited
actor-visible context. Every context field is checked against the actual App
projection at that point in the sequence. Only the founder is controlled. Own
inventory, protected seed and work reservations are finite quantities. These
documents contain neither expected action answers nor hidden NPC inventories.

`evaluator_only/setup.json` contains reviewed setup choices, not a raw world.
Engine `settlement_setup.preview` produces the review digest and
`settlement_setup.initialize` creates the entire temporary world. App consumers
use its existing `rise_campaigns.create` and `rise_campaigns.action` services
with a temporary `Store`. Catalog supplies no alternate initializer or executor.

`evaluator_only/oracle.json` contains ordered case requests, expected results,
private NPC quantities and a boundary marker. Load it only in the evaluator
process. Do not put this file, the manifest, setup review, full template, raw save
or Historical Details archive in a prompt. The actor exporter reads only the
manifest and the single selected actor file; it never opens either evaluator
file. It rejects wrong audiences/paths, extra fields, changed hashes and reserved
evaluator markers. Intake rejects marker contamination even after hashes are
refreshed. This is a boundary for reviewed content, not a semantic sanitizer for
arbitrary untrusted prose.

The actor input is test content, not authority to act. Engine/App must supply
their current supported proposal schema and current actor-scoped observations,
validate authorization and freshness, and require the normal explicit action
commit. A proposed action has no effect merely because it appears in the oracle.
Never replace current runtime observations with these canned contexts in a live
campaign. The case's `request_revision` can intentionally be stale; its actor
`context.revision` describes the current state where the case is evaluated.

## Ordered cases and actual outcomes

| Case | Request | Required behavior |
| --- | --- | --- |
| `solo-denied-build` | `build` at the commons | Denied; save, resources and elapsed time unchanged. |
| `solo-unsupported-grain` | Deliberately unsupported `invent_grain` proposal | No matching handler; forced execution is rejected atomically. |
| `solo-walk` | `walk_clearing` | Existing founder and supplies move; 300 elapsed seconds. |
| `solo-stale-inspect` | Fresh `inspect` request at revision 0 after the walk | App rejects the stale revision without effects. |
| `solo-found` | `found` under the accepted limited grant | Camp established; no shelter, new goods or elapsed time. |
| `solo-replay-walk` | Exact retry of the original walking request | App returns its durable original result despite the old revision; no second movement or elapsed charge. |
| `solo-changed-replay` | Same request identity with `wait_hour` instead | Rejected without effects. |
| `solo-build` | `build` at the camp | Reserve three timber bundles and one axe; shelter remains incomplete. |
| `solo-work-boundary` | `wait_hour` | Stop after 1,500 seconds at the first work completion boundary. Founder work remains active. |
| `solo-finish-shelter` | `wait_hour` | Stop after another 2,100 seconds with 3,600 founder work seconds complete. |

The evaluator independently checks the standing NPC repair: one existing NPC
timber bundle is consumed at elapsed 1,800. Founder shelter consumes three
existing founder timber bundles at 3,900. Starting total stock is grain 16,
timber 9 and axes 2; final stock plus consumption equals those same totals at
every step. Grain and axes are conserved unchanged; two shelter places are
produced by the completed founder project. Elapsed seconds, causal clock and App
storage revision are checked separately. No civil date advancement is inferred.

## Rights and processing

The manifest explicitly permits local/offline evaluation and external evaluation
of the authored actor exports. This permission covers only the fixture's original
synthetic text. It does not grant rights over upstream software, imported source
documents, historical material, private saves or any future derivative content.
Unknown imported rights remain unknown. No imported material is included here.
Engine access policy and the normal user authorization still govern any actual
transfer. Content records select no provider, model, key, price or route. No live
provider call was made in fixture qualification.

## Consumer qualification

Use exact, unedited dependency checkouts; the tests check their full Git SHAs and
module paths. All state and failed-write/concurrency checks use temporary
synthetic saves. This command must finish with zero skips for qualification:

```bash
IRGS_SOLO_ENGINE_SOURCE=/path/to/selected/IRGS-Engine \
IRGS_SOLO_APP_SOURCE=/path/to/selected/IRGS-APP-WEB \
python -B -m unittest discover -s tools/tests -p 'test_solo_evaluation*.py' -v
```

The two environment variables identify repository roots, not runtime directories.
The consumer harness selects this Catalog through `IRGS_CATALOG_ROOT` and the
selected Engine through `IRGS_ENGINE_ROOT`; it edits neither dependency. Without
those explicit snapshots, the six cross-component checks report skips. This is
not a qualified consumer run. Twelve standalone schema tests need no dependency.

The baseline App can consume this content through the test harness; production
fixture loading, any new proposal/provider contracts, exact App dependency pins,
joined acceptance and live provider smoke tests remain component/coordinator
work. Requalify a new fixture version against a newly selected runtime contract.
