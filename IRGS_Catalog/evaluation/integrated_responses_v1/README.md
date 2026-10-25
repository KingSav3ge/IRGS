# Integrated response consumer compatibility 1

This separately versioned follow-up qualifies the already integrated Engine/App
pair through its actual App HTTP `local_responses` projection and saved
`presentation` result field. It reuses the original nine-case
`irgs-shared-responses-v1` fixture without changing its manifest, payload hashes,
consumer declarations, rights or oracle separation.

## Exact selections

- Engine: `2f9476c6090878257d17cab3ad3a83a7ce18a5dc`.
- App: `aae8a25656c890181e0aa569df2c716968ec3642`.
- That App's committed Catalog pin:
  `27fff8385d1c01fdfe9ad7254b7647e6bc12a01e`.

The follow-up has its own identity, `irgs-integrated-responses-v1`, schema 1.
`compatibility.json` binds the original manifest SHA-256
`fc45e92af7c869924695450f4e995621779e4d4dae6058c72ebe416310ceded1`.
The original record still selects Engine `9ecf3b8...`, App `e1efcfe...` and
Catalog `94b8ca6...`. Run those original tests with their original exact sources
in a separate process; never change their identities to admit the integrated pair.

The loader validates the original fixture, checks the exact manifest bytes and
reuses its actor export and evaluator-only loading functions. This adds no new
world rules, initialization data, actor knowledge, provider configuration or
external-processing permission. The depot remains byte-identical: 750 system
variants, 250 editable drafts and 32 separately counted recipes.

## Actual consumer boundary

The fixture initializes Rise R00 through its existing reviewed setup and the
non-Rise optional fictional quay opening through the existing 1415 campaign
selection. App hosts run with `solo_configuration=None`. Broker dispatch and
direct provider transport are instrumented to fail.

The nine HTTP tests cover:

- The same public response schema in both contexts, actual Catalog/Engine
  library identities and exact neutral depot bytes.
- Read-only editable drafts with semantic tags, no automatic operation binding
  for Catalog drafts, and explicit submission as an unresolved declaration.
- All nine real actions, including failed attempts, one conserved dispatch,
  actual spans, a zero-second inspection and unchanged civil campaign time.
- Exact saved presentations in results, completed actions and every older
  receipt lookup after later actions.
- Lost acknowledgement, host restart, concurrent exact retry, unchanged campaign
  bytes and one committed effect.
- Failed-save atomicity and retry under the same request identity.
- Missing/corrupt Catalog intake plus unavailable Engine text; ordinary actions
  retain the full authorized literal receipt and no private failure diagnostic.
  Restoring text availability leaves the saved fallback result unchanged.
- Foreign actors, forged browser presentation packets, stale new requests and
  identical-byte Trash restore with refreshed draft-view scope.

No reference-renderer recomposition substitutes for the saved native presentation.
Literal comparisons use Engine's actual `receipt_facts` API. Tests use only
temporary synthetic saves and loopback HTTP. Phase/communication App adapters,
other contexts, general generated dialogue, live model quality and wider C2 retain
their separate scope.

## Run

Use Python 3.12+ without `-O`, clean exact repository roots, and a fresh process
for every dependency selection:

```bash
python -B IRGS_Catalog/integrated_response_compatibility.py
python -B -m unittest tools.tests.test_integrated_response_contract -v
IRGS_INTEGRATED_ENGINE_SOURCE=/path/to/selected/Engine \
IRGS_INTEGRATED_APP_SOURCE=/path/to/selected/App \
python -B -m unittest tools.tests.test_integrated_response_consumers -v
```

The consumer tests verify both App submodule pointers and imported module paths.
`IRGS_CATALOG_ROOT` explicitly selects this candidate during qualification; no
dependency pointer is edited. Missing selections are skips, not passing consumer
evidence. Catalog integrity includes this follow-up; hashing alone proves no
runtime behavior.

Root `INTEGRATED_RESPONSE_VALIDATION.json` records the freshly executed commands,
results, hashes, skips and limits. Earlier validation files retain their original
evidence. The original shared response integration is already complete; coordinator
review of this additional fixture/evidence increment is a separate step.
