# R00 proposal consumer compatibility 1

`compatibility.json` selects reproducible consumer checks for the existing
`irgs-solo-r00-eval-v1` fixture through `solo-proposal-1`. It introduces no new
campaign, initialization state, action, actor input or oracle. The complete
original R00 fixture and its loader remain byte-identical, including its original
Engine/App dependency contract and explicit authored-synthetic processing rights.
Those rights do not extend to imported archives, private saves or future material.

The source fixture manifest remains pinned at SHA-256
`2d30e863c4f769f0e2039469807ca0c6eeef3f30edd17d96778cebcba65bdbe5`.
Catalog integrity checks validate both the original fixture and this compatibility
record. Source hashes and schema validation do not establish consumer execution.

## Selected sources

- Engine `8234044c089131314019ecaf6799a2f08028a3f8`.
- Integrated development App `277554aac21a092b8a55562309da274bbe74a3af`.
- Subsequent component App `4f45f5ab8473a2bddb500fe3a49122575b6483e1`.

Both Apps commit the selected Engine pin and Catalog
`401df26a1f16be864dd15d7c5250da5d75f8ccca`. Tests check those pins, exact clean
Git identities and imported module locations. This Catalog candidate is explicitly
selected for qualification with `IRGS_CATALOG_ROOT`; this does not update App
dependency pins or approve a new joined build. The newer App is a separate
component qualification, not a claim that its changes were already integrated.

## Run

Use Python 3.12+ without `-O`. Select unedited repository roots, not runtime
directories. Run each dependency combination in a fresh Python process:

```bash
python -B IRGS_Catalog/solo_proposal_compatibility.py
python -B -m unittest tools.tests.test_solo_proposal_contract -v
IRGS_PROPOSAL_ENGINE_SOURCE=/path/to/selected/Engine \
IRGS_PROPOSAL_APP_SOURCE=/path/to/selected/App \
python -B -m unittest tools.tests.test_solo_proposal_consumers -v
```

Repeat the final command for each of the two selected App commits. It must run
all eight consumer tests with zero skips. The original six consumer checks still
use `IRGS_SOLO_ENGINE_SOURCE`/`IRGS_SOLO_APP_SOURCE` and their original exact
commits; run those separately. The source snapshots must not be edited to satisfy
an assertion. Missing proposal source selections produce explicit skips, not
qualification.

## Actual boundary exercised

The evaluator exports only the selected actor document and loads expectations in
a separate evaluator namespace. It supplies the exact exported intention to the
App; it never sends canned context, an oracle or a world to the proposal endpoint.
Engine builds model input from current founder receipts and published conditional
action descriptions. Tests compare every received assertion/source/time to the
actual founder receipt and reject hidden NPC inventory, evaluator markers and
private state/restore/dependency fields in model input and public results.

The fake transport returns the evaluator-selected candidate action and received
source references. Its outputs are test expectations, not AI reasoning or a
semantic/voice benchmark. It is injected into an actual temporary App HTTP host
with the actual Engine broker, validator, ledger and action bridge. Synthetic
route/limit configuration exists only in test code, never in content records.
No live adapter, external provider, key, price lookup or user save is used.

The ten original cases retain their sequence and expected finite resources:
five legitimate actions complete founder shelter at elapsed 3,900; denial,
unsupported output, stale revision, exact replay and changed identity are checked
at their actual boundaries. Proposals change no save bytes. Accepted results
match actual committed Core receipt summaries. Each accepted action survives a
host restart and concurrent retries without repeating effects or another attempt.
Remaining stock plus recorded consumption equals opening stock after every step.

Additional tests exercise exact whitespace retention and explicit acceptance,
forged browser context and foreign actors, malformed/denied/changed-intent/unknown-
source provider output, durable failure recovery, identical-byte Trash restore,
late output after state change, cancellation and an unconfigured host. Original
fixture source/intent references remain in the fixture; runtime provider source
references name actual received Core receipts. Catalog provenance cannot grant
actor knowledge, control or transfer permission.

## Narration/dialogue dependency

The selected Engine exposes only `propose_local_action`; the selected App returns
committed Core summaries and `narrative: null`. General narration/dialogue and
semantic/voice review remain unfinished in the coordinator's Solo plan. There is
no supported generation/validation contract for a new Catalog narration/dialogue
fixture to qualify. That conditional follow-up remains
`awaiting_engine_app_contract`; metadata cannot mark it passed. Once those owners
publish the contract, add separately versioned synthetic inputs/oracles and
actual consumer checks. Do not reinterpret Core summaries as generated narration
or invent speech/obligation mechanics in Catalog.
