# Engine-side App and Catalog compatibility

The three development repositories were pulled on 25 October 2026. This
qualification selects their current source explicitly without changing App's
committed Engine/Catalog pointers or Catalog's historical consumer declarations.
Engine Core remains independently usable. The new checker is a development tool,
not a production dependency on App or Catalog.

| Selected runtime/source | Commit |
| --- | --- |
| Engine | `0fdfc21f45510e3fd99fd6a8087cd3314d077267` |
| App/Web | `67411f8ef5214c8cb51af2b244590751e6ea20df` |
| Catalog | `4bd572843cebc94e7d043c3706d1be85249d6c10` |

App still commits Engine `2f9476c6090878257d17cab3ad3a83a7ce18a5dc` and Catalog
`27fff8385d1c01fdfe9ad7254b7647e6bc12a01e`. Its local submodules were updated to
those exact pointers after pulling, leaving App clean. The candidate checks
instead set `IRGS_ENGINE_ROOT` and `IRGS_CATALOG_ROOT` to the independent latest
checkouts. Imported module paths and source hashes are recorded in
[the execution report](COMPONENT_INTERACTION_VALIDATION.json). An override tests
compatibility; it does not update a pin or authorize joined release integration.

## Repeat the Engine-side checks

From IRGS-Engine, in a fresh Python process with loopback sockets permitted:

```bash
python -B tools/qualify_component_interaction.py \
  --app-root ../IRGS-APP-WEB --catalog-root ../IRGS-Catalog \
  --output engine/COMPONENT_INTERACTION_VALIDATION.json
```

The five checks use actual App HTTP endpoints, Engine initializers/Core handlers,
Catalog intake and temporary synthetic saves. They:

- Reuse the original nine-case Catalog actor inputs and separate oracle in
  independently initialized Rise and authored quay worlds. Real successful,
  blocked and depleted outcomes, elapsed spans, conserved dispatch delivery and
  original saved-receipt lookup are checked. The original fixture and its older
  declared consumers remain unchanged; this is a separate latest-source record.
- Verify App and Engine load the same exact 1,000-variant depot, preserve editable
  non-submitting drafts and exclude evaluator-only facts from public responses.
- Start selected work/observation with the new Engine `phase_contract` as trusted
  synthetic setup, atomically persist through App `Store`, then continue through
  actual `/api/process/prepare` and `/api/process/execute` endpoints. Commands,
  exact intentions, pause/resume, actual completion and replay reconcile across
  the interfaces. This does not qualify a browser start flow.
- Keep literal actual outcomes when Engine/Catalog presentation text is missing.
  Provider dispatch and direct provider transport are forbidden throughout.
- Identify the remaining start-discovery adapter gap without inventing an HTTP
  feature: Engine exposes start options; current App `process_control` correctly
  retains `start_available: false`.

## Executed regressions

With both source selectors above, App runs **218 Python tests: 211 pass and seven
Windows-only checks skip on Linux**. Its 17 process-bridge and ten shared-response
checks also pass independently. All 110 gameplay UI checks and 13 response-library
checks pass. Real Chromium process and shared-response suites pass in both
contexts, including lost replies, reload/recovery, stale navigation, zero-second
phases and a 390px viewport. They record zero browser errors and provider calls.

Catalog's 39 depot/shared/integrated source-contract tests pass. Engine's 35 shared
and 28 phase-contract cases pass. All three component integrity checks and Kira
canon pass. Runtime/source distributions and the depot are unchanged by this
Engine qualification; no user campaign, credential or live inference is used.
The previously recorded full Engine run (707 passed plus one policy skip) remains
at the unchanged Engine runtime source; it is not counted as a new execution here.

## Remaining ownership

The current App already continues existing typed Engine processes. App must adopt
Engine's new actor-safe phase start discovery before offering starts. App owns
its reviewed dependency-pointer update; the coordinator owns the exact joined
set and package qualification. The next Engine bounded development task remains
the communication/offer participant and received-source contract. General C2,
freeform/combat and additional campaign mechanics keep their existing limits.
