# Development interoperability matrix 1

This Catalog-owned follow-up checks the three pulled development sources.
Historical compatibility records, case payloads and consumer guards remain
unchanged. `irgs-development-interop-v1` binds the previous integrated
compatibility JSON by exact hash and adds explicit Engine roles:

| Role | Engine |
| --- | --- |
| Development head | `0fdfc21f45510e3fd99fd6a8087cd3314d077267` |
| App's committed pin | `2f9476c6090878257d17cab3ad3a83a7ce18a5dc` |

Both roles use App `67411f8ef5214c8cb51af2b244590751e6ea20df` and this Catalog
candidate. App's committed Catalog pin remains
`27fff8385d1c01fdfe9ad7254b7647e6bc12a01e`. Catalog at pull was
`4bd572843cebc94e7d043c3706d1be85249d6c10`.
The development role explicitly overrides the older Engine pointer for testing;
it is not a pointer update or coordinator approval.

## Catalog-side checks

`test_development_interop_consumers` reuses the nine native HTTP cases under a
new class with its own strict matrix identity guard. The original integrated
class and manifests keep their original exact selectors. Every role runs in a
fresh process and checks clean dependency commits, actual App pointers and
imported module paths. Missing selectors are explicit skips.

Two additional tests exercise App's published received-process controls in
independently initialized non-Rise observation and Rise work contexts. Trusted
synthetic setup uses the actual typed Engine API to establish a process before
the host starts; no public process-start flow is created or claimed. It uses the
existing reviewed quay and R00 setup, not a new campaign adapter or rule.

Real HTTP preparation is effect-free and preserves exact intentions; execution
requires explicit acceptance. Observation delivers information on completion.
Work preserves progress through zero-second pause/resume phases and reaches the
existing material boundaries. Actual phase receipts use Catalog-backed local
presentation and survive saved-result lookup, restart and exact retry. The
inherited tests retain failed-save, missing/corrupt-source fallback, foreign/stale
request rejection and older-presentation recovery. Broker dispatch and direct
provider transport remain forbidden throughout.

This qualifies the named supported contexts and handlers. App still reports
`process_control.start_available: false`; the newer Engine's discovery API does
not automatically add App starts. Communication controls and further contexts
require their own published interfaces and qualification.

## Repeat

Use Python 3.12+ without `-O`:

```bash
python -B IRGS_Catalog/development_interop_compatibility.py
python -B -m unittest tools.tests.test_development_interop_contract -v
IRGS_INTEROP_ENGINE_SOURCE=/path/to/current/Engine \
IRGS_INTEROP_APP_SOURCE=/path/to/current/App \
IRGS_INTEROP_ENGINE_ROLE=development \
python -B -m unittest tools.tests.test_development_interop_consumers -v
```

Repeat the consumer command with the exact App-pinned Engine root and
`IRGS_INTEROP_ENGINE_ROLE=app_pinned`. The tests explicitly select this Catalog
through `IRGS_CATALOG_ROOT`; no consumer code or pointer is changed.

See root `DEVELOPMENT_INTEROP_VALIDATION.json` for actual commands, source hashes,
results, integrity checks and remaining dependencies. The depot stays at 750
system variants, 250 editable drafts and 32 recipes. No private save or live
inference is used; no measured production saving or joined release is claimed.
