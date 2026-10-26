# Unified IRGS development and coordination guide

## Latest App communication delivery included in 3.4.3

The newly pulled App bridge adds actor-received channels/sources and reviewed
Speak, Offer, Counteroffer, Accept, Decline and Withdraw operations. Exact words
remain testimony; saying “I accept” under Speak accepts no offer. Core retains
authority, conserved transfers and distinct closure outcomes. Prepare/accept,
lost replies, restart/restore and original-result lookup preserve identity and
effects. Legacy unattributed sources retain their established private-provenance
boundary, and other R00 characters gain no founder inspection or actions.

This bridge operates only where legitimate channels and participants have been
selected. Normal initializers do not install the synthetic test fixtures. Next:
Engine/content channel selection and native travel, separate Catalog communication
consumers, protected App operator setup, build identity and supported-intent
mapping. Broader freeform/combat, NPC/institutional completion, live quality and
full C2 remain open. Current source replaces superseded generated installations;
original archives, accurate dated evidence, Git history, saves/config remain.

Current coordinated edition: **3.4.3**; previous release: **3.3.3**.
See [version policy](VERSION_POLICY.md). Historical evidence below retains
its original tested development identities.

Current guide: 25 October 2026. Owner: `KingSav3ge/IRGS/main`.
Start with [CHAT_CONTINUATION.md](CHAT_CONTINUATION.md).

## Current 3.4.3 coordinated update

Read RELEASE_NOTES_3_4_3.md and COMPONENTS.json. This selection combines the
Engine start-readiness/context contract, explicit App start-mode adoption and
Catalog's separate six-path requirements/qualification. The optional sourced
Henry observation, authored new-person opening and R00 are bounded actual
slices; John and other unsupported starts remain declaration/reference modes.
Received initial civil day and local elapsed time retain separate meanings.
Next: selected Engine travel, normal-start communication channel selection and matching Catalog
consumers. No general freeform, full C2 or live model-quality completion is
claimed. Earlier sections retain their original dated scope and qualification.

## Current 3.4.2 coordinated update

See RELEASE_NOTES_3_4_2.md and the exact component selection in COMPONENTS.json.
The candidate combines Engine communication capabilities/private-offer filtering,
the refined Emergent App interface and separately versioned Catalog phase checks.
Current qualification must cover this exact set; dated evidence below retains its
original identities. App communication HTTP/UI controls and operator configuration
remain open. The next Engine increment is selected travel capability discovery;
Catalog communication evaluation follows the published App bridge.

## Prior 3.4.1 integration

The reviewed source set is recorded in COMPONENTS.json and
[the 3.4.1 review](provenance/qa/phase_integration_3_4_1_review.json).
This increment integrates selected Engine phase capabilities, App Begin/review/
continuation/recovery controls and separately versioned Catalog compatibility
fixtures. Observation in the non-Rise authored opening and Rise work remain
selected handlers; their rules do not become universal campaign mechanics.

Next, advance Engine communication/offer participant and legitimate received-
source contracts, then matching App controls and Catalog evaluation. Preserve
completed phase controls and exact older fixtures. Operator configuration,
general freeform/combat, wider DEV/C2 and live model quality remain open.
Every unified main publication increments the version; QA stays local until a
qualified versioned coordinator push. The previous release is recorded as 3.3.3.

## Prior qualified baseline and scope

IRGS **3.4.0 development**, Core compatibility **3.3**. Develop shared systems
across campaigns and themes. Rise R00 and the existing non-Rise authored opening
are actual supported regression contexts. Synthetic theme/profile checks prove
their recorded formatting/declaration behavior, not new campaign mechanics.

The [coordinator integration](https://github.com/KingSav3ge/IRGS/blob/65351ebcfe2538d880f576a3ce4aa2230537e08d/provenance/qa/shared_response_integration_3_4_0_review.json) qualified joined `65351ebcfe2538d880f576a3ce4aa2230537e08d`:

| Component source | Qualified commit |
| --- | --- |
| Engine | `2f9476c6090878257d17cab3ad3a83a7ce18a5dc` |
| App/Web | `aae8a25656c890181e0aa569df2c716968ec3642` |
| Catalog | `27fff8385d1c01fdfe9ad7254b7647e6bc12a01e` |

Recorded integration results: 680 Core tests run (679 passed, one private-fixture
policy skip); 201 Web run (194 passed, seven Windows skips); 105 interface checks;
104 Catalog checks; eight independent HTTP checks. Two-context Chromium and
clean-package qualification passed with zero live inference. These are attributed
prior results, not tests newly executed by this guide update.

Later guide-only commits do not alter this qualified source set. Preserve
independent content/schema versions and historical evidence. See
[shared scope](IRGS_SYSTEMS_SCOPE.md), [continuation](CHAT_CONTINUATION.md) and
[the work order](COORDINATOR_WORK_ORDER.md).

## Repository boundaries and current state

| Repository | Owns |
| --- | --- |
| IRGS-Engine | `IRGS_3_3/`, Engine contracts/design and Core behavior. |
| IRGS-APP-WEB | `IRGS_Web/`, local host/interface/viewer, pinned `Engine/` and `Catalog/`. |
| IRGS-Catalog | `IRGS_Catalog/` content, provenance, response depot and evaluations. |
| IRGS | Full joined source, coordination, qualification and packaging. |

See [COMPONENTS.json](COMPONENTS.json), [coordination](COORDINATION.md),
[current machine state](DEVELOPMENT_STATE.json), [integration policy](COMPONENT_REPOSITORIES.md)
and [shared completion plan](SOLO_COMPLETION_PLAN.md). Original dated evidence
stays preserved. `DEVELOPMENT_STATE_HISTORY_2026-10-22.json` archives the superseded
3.3.3 state; it is not the active task list.

The current merge aligns App pins and integrates Engine-selected process starts
and received continuation commands with App durability/recovery and Catalog
presentation. The earlier verified-byte Catalog intake fix remains in place.
Communication controls, further semantic adapters, operator setup and broader
DEV/C2 remain open.

## Next coordination increment

Review the next exact pushed component set against its published contracts and
this shared scope. Preserve the integrated phase/capability interface, App process controls and
Catalog compatibility fixtures. Track communication/source contracts and their
App/Catalog consumers as the next coordinated dependencies.
Keep useful owner work moving when another interface is pending. Resolve actual
compatibility bugs in the owning repo, align App pins, then capture fresh source-
bound evidence and test an isolated candidate. Gate the import, prove identical
runtime inputs, check real browser play and a clean package, then push joined main.
Guide-only metadata commits are not new viable product deliveries. Monitor only
while this environment runs; do not claim a chat was resumed by a repository push.

## Run and verify

```bash
python -B IRGS_Web/server.py --port 8766
python -B tools/verify_development.py
python -B tools/build_operation_register.py --check engine/qualification/operation_register.json
```

The Windows launcher defaults to 8765 and may reuse another valid host. Keep
development sessions separate and preserve user saves. Server startup, templates
and an API key alone do not configure eligible live inference.

`tools/qa_irgs.py --source-root <clean-candidate-root> --commit <exact-candidate-SHA>
--output <outside-source-report.json>` runs joined Core/Web/interface/tooling and
eight independent HTTP checks. It excludes the external private-save test by
policy even if present. Use it for changed product inputs; guide-only edits retain
attributed existing results after proving code/data/release equality.

For changed runtime/test/release inputs, generate actual new operation evidence:

```bash
python -B tools/build_operation_register.py --output engine/qualification/operation_register.json --markdown engine/OPERATION_COVERAGE.md --test-log development_results/runtime_capture.txt
```

All three destinations belong inside the candidate; test log ends in `.txt`.
Capture observes synthetic execution and discloses unqualified paths. Rehashing
old evidence does not qualify changed inputs. Do not use the inherited release
builder that expects historical backups/certification files.

## Gated integration and packaging

1. Preserve local work; fetch exact main commits and inspect actual owner code
   and evidence. Work orders and guide-only commits are metadata, not viable
   new product increments. Keep current code pins until a reviewed pair is chosen.
2. Qualify a clean isolated Engine/App/Catalog candidate, including compatible
   committed App pins, real non-Rise/Rise effects, actor privacy, retries, restart,
   restore and zero-call routine rendering. Preserve legacy fixture guards.
3. Record exact approvals in `COORDINATION.json`. Use
   `tools/check_integration_gate.py` then `tools/sync_components.py --apply`, each
   with `--engine`, `--app`, `--catalog` repository paths. The gate must hold when
   no new viable set exists; do not bypass it to import partial work.
4. Retain fresh candidate operation evidence only after proving identical source
   inputs in joined source. Refresh `DEVELOPMENT_MANIFEST.json` with
   `python -B tools/verify_development.py --refresh`, then verify again.
5. Package the actual committed tree and test extraction before pushing main:

```bash
python -B tools/package_development.py --output ../IRGS_3_4_2_Development.zip
python -B tools/smoke_development.py ../IRGS_3_4_2_Development.zip
```

Use explicit candidate/import paths. For clean-package checks clear only stale
`IRGS_ENGINE_ROOT` / `IRGS_CATALOG_ROOT` selectors or point them to extraction;
preserve proxy/TLS settings. Keep artifacts, test saves, credentials and caches
outside curated source. Run actual extracted browser play for changed UI/contracts.

## QA monitor and guide-only publication

`tools/watch_component_qa.py` polls pushed component mains while the environment
runs, tests isolated sets and retains local QA reports for versioned coordinator review. It does not implement work,
start chats, import product source or deploy. Recheck PID/cmdline, lock and fresh
state before claiming it is running. Pause only its verified process while
coordinating publication; restore it afterward.

For guide-only commits, prove all selected runtime/data/release bindings and
operation inputs remain byte-identical. Record documentation equivalence with
the existing qualification; do not manufacture a fresh test run or advance
product pins solely for prose. Preserve watcher history and truthfully identify
any metadata-only seeded qualification. This avoids redundant full regressions.

## Rules for every increment

Keep one authoritative Core and the nine K-owners; provider work retains the six
existing Director categories. Distinguish intent, authorization, committed effects,
received information and presentation. Only actual actor-legitimate records may
support a response. Testimony and uncertain information retain their status.
Keep storage revision, causal order, elapsed spans, civil dates and information
times distinct. Select real rules/adapters; themes and text create no capability.

Routine responses require no provider, key or model tokens. Preserve exact
receipts, negation, actual zero/absent durations, editable intentions and explicit
submission. Missing text or rules retain a literal/unresolved result and cannot
authorize paid fallback. Keep pinned code/content intake on the exact verified
bytes; retain the component-update regression in App.

Use temporary synthetic saves. Never read/migrate user campaigns or run the
external private-save fixture. Preserve original archives, source records,
rights, adopted canon and 44 previews. Historical Details is fully delivered;
archive reacquisition is complete. Preview/content presence grants no release
or mechanical authority. General freeform/combat, generated dialogue, sustained
institutions, full C2, live model quality and wider hosting retain their open
requirements; Co-op remains deferred.

## Handoff and records

The three component continuation briefs are linked in [CHAT_CONTINUATION.md](CHAT_CONTINUATION.md).
Repository publication supplies the available handoff; no direct chat-send/start
tool is present. Status reads can fail, so commit/owner evidence and actual checks
must support review. Generate paste-ready instructions without claiming delivery.
Previous operational notes remain in [dated history](DEVELOPMENT_HISTORY_2026-10-25.md).
