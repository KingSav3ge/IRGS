# Public process response qualification 1

`irgs-phase-responses-v1` qualifies Catalog presentation through the now-published
App process-start controls. It binds the original development interoperability
record by exact hash. All older manifests, case payloads, consumer declarations,
rights and validation records retain their original identities.

| Selected source | Commit |
| --- | --- |
| Engine, also App's committed Engine pin | `aa30bb63a3828cbaeb5ee3d1db57edd388a8dc86` |
| App | `919427cf16cf72574a581d7e6f712e638740a1df` |
| App's committed Catalog pin | `526404128830a99fe8ea5c2bce43b6ea7d45fe6f` |

Tests explicitly select this Catalog candidate through `IRGS_CATALOG_ROOT`.
They change no App dependency pointer. Engine selects capabilities through
`irgs-phase-capabilities-1`; App publishes `process_control` schema 1 and
`/api/process/prepare`, `/execute`, `/status`. Preparation is effect-free;
execution requires explicit acceptance of the exact intention. Catalog content
never supplies a scheduler, authorization decision or campaign rule.

## Supported contexts and actual outcomes

The original shared fixture initializes two independent temporary worlds, with
actor inputs and evaluator-only expectations kept separate. Non-Rise selects
the existing optional fictional quay opening in Hundred Years' War 1415. Rise
uses the existing R00 setup and public walk/found actions to establish its site.
Both processes start through public HTTP controls; no process is injected during
fixture setup.

The selected quay observation starts with zero elapsed work and no new evidence.
An explicit one-second advance leaves evidence unchanged; pause/resume take zero
seconds. A later requested advance stops at the actual 20-second completion
boundary and receives information then. This fixture's 20-second rule is distinct
from Engine's smaller three-second synthetic test world.

Rise shelter work starts without stock consumption or elapsed work. It retains
100 seconds of progress across zero-second pause/resume, respects actual material
boundaries and reaches 3,600 seconds of work. Received status is distinct from a
live world probe. Inspect and cancellation are separately tested on observation.

The new seven HTTP cases cover discovery against the actual Engine contract,
private feasibility not selecting menus, atomic rejection, both real starts and
continuations, failed start/advance saves, durable preparations, concurrent exact
retry, restart, forged/foreign/stale inputs, identical-byte restore fencing and
saved presentation recovery. Missing Catalog text retains complete authorized
Engine phase text, zero usage and the original saved fallback after source recovery.

Nine inherited native response cases additionally preserve all original real
outcomes, editable non-submitting drafts, actor/oracle separation, source fallback,
failed saves and old receipts. Broker dispatch and direct provider transport are
forbidden throughout; loopback HTTP is the only network use. Phase presentation
identifies Engine's neutral depot separately from its older ordinary receipt pack.

## Repeat

Use Python 3.12+ without `-O`, with clean exact consumer repositories, in a fresh
process:

```bash
python -B IRGS_Catalog/phase_response_compatibility.py
python -B -m unittest tools.tests.test_phase_response_contract tools.tests.test_standalone_catalog -v
IRGS_PHASE_ENGINE_SOURCE=/path/to/selected/Engine \
IRGS_PHASE_APP_SOURCE=/path/to/selected/App \
python -B -m unittest tools.tests.test_phase_response_consumers -v
```

Schema validation certifies source identity and scope, not runtime execution.
See root `PHASE_RESPONSE_VALIDATION.json` for executed commands/results. The depot
remains 750 system variants, 250 editable drafts and 32 recipes, with no content
changes. Only temporary synthetic saves participate. Communication/source
discovery, further adapters, measured production savings and coordinator
joined/browser/package review retain separate dependencies.
