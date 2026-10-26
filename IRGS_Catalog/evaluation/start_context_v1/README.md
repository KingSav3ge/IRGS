# Published start-context selection 1

Catalog's `irgs-start-context-v1` selects Engine
`cc450a6f00a249d2169cdacdfc9c4b1e03f67cc8` and its published
`irgs-start-readiness-1` contract. It binds the original `player_starts_v1`
manifest by exact hash, preserving every original consumer ID, source and result.
No old baseline is repinned to imply qualification of this newer contract.

This delivery contains six independent actor documents, a separate oracle,
original citation-review notes and an explicitly unexecuted App acceptance list.
It changes no Engine/App implementation or dependency pointer. Engine execution
evidence and App adoption are separate; schema validity proves neither one.
The manifest intentionally names no qualified App revision while adoption is
pending. A future adopted App requires its own exact compatibility record and
executed consumer evidence, retaining this record's original scope.

| Selection | Published Engine mode | Boundary |
| --- | --- | --- |
| Existing Henry, explicitly selected `henry-1415-embarkation-v1` | `supported_slice` | One bounded local observation, not military command or a courier assignment. |
| Existing Henry, default selection | `declaration_only` | Optional context is not silently installed. |
| Existing John of Lancaster | `declaration_only`; playable context held | Missing legitimate personal context; cannot borrow Henry's setting or new-person fiction. |
| New human, default no opening | `declaration_only` | Exact testimony/intent creates no possessions or executable rule. |
| New human, explicitly selected quay opening | `supported_slice` | Existing authored map/custody and actual scene operations. |
| Reviewed R00 | Existing supported settlement adapter | Separate fictional regression, no historical civil-date claim. |

## Source review and uncertainty

Catalog checked the two research summaries cited by Engine: Dan Spencer's
[3–9 August account](https://www.agincourt600.com/2015/08/05/3-9-august-1415-violence-in-salisbury-the-trial-of-the-southampton-plotters-and-the-embarkation-of-the-army/)
and [10–16 August account](https://www.agincourt600.com/2015/08/12/10-16-august-1415-the-expedition-sets-sail-to-france/).
They support only the retained broad embarkation setting for this review; the
boarding chronology remains disputed. No precise room, berth, occupied ship or
hour is selected. Primary editions/rolls cited by those summaries were not
independently collated here. `source_review.json` records original short
paraphrases, locators, provenance and exclusions; no article or image is copied.

The selected 20 seconds come from Engine's explicit simulation rule. They are
neither a historically measured duration nor a universal perception rule.
The actor receives only Engine's actual setup and committed observation records.
Research references and precreation review do not become actor knowledge by
themselves. No fleet quantity/readiness, destination, command receipt, stock,
introduction, order, mandate or scheduled departure/landing is manufactured.

## Engine evidence and App dependency

`test_start_context_engine` uses the real precreation review, initialization,
actor view, shared capability/intent and Core execution APIs. The independent
test-only host atomically CAS-saves Core state and public result together; it
creates no world authority or product persistence layer. Tests cover all six
modes, source-bound received Julian day, unknown hour, no running civil-clock
binding, actual observation, successful/unsuccessful quay outcomes, R00 finite
work, original-result recovery, restart-equivalent reload, failed saves,
concurrency, changed/stale requests, restore fencing, privacy, control revocation,
unsupported actor/opening/snapshot substitutions and continuing reads that do
not consult/reapply templates. Provider dispatch, direct transport and sockets
are forbidden throughout the Engine cases.

`test_start_context_pending_app` separately diagnoses the exact coordinator-patched
App `d8e68848454ac7be68ce87fede6d04cc57bda86a` with an explicit Engine override.
Its committed pins remain Engine `91b2005` and Catalog `3f92125`. Henry's published
option is present in Engine metadata, but that old App preflight rejects it.
Limited-mode previews still omit the adopted context. These are recorded blockers,
not successful App acceptance or desired future behavior. `app_acceptance.json`
remains unexecuted until an actual adopted revision/pin set is available.

## Repeat

Use Python 3.12+ without `-O`, clean exact repositories and fresh processes:

```bash
python -B IRGS_Catalog/start_context_evaluation.py
python -B -m unittest tools.tests.test_start_context_contract tools.tests.test_standalone_catalog -v
IRGS_CONTEXT_ENGINE_SOURCE=/path/to/exact/Engine \
IRGS_CONTEXT_EVIDENCE_OUTPUT=/tmp/start-context-engine.json \
python -B -m unittest tools.tests.test_start_context_engine -v
IRGS_CONTEXT_ENGINE_SOURCE=/path/to/exact/Engine \
IRGS_CONTEXT_PENDING_APP_SOURCE=/path/to/exact/pending/App \
IRGS_CONTEXT_APP_DIAGNOSTIC_OUTPUT=/tmp/start-context-app-gap.json \
python -B -m unittest tools.tests.test_start_context_pending_app -v
```

See root `START_CONTEXT_VALIDATION.json` for actual commands, passes/skips and
limits. All saves are temporary synthetic fixtures. The original historical
archive/citations, 44 previews and unchanged 750 system variants, 250 drafts and
32 recipes are preserved. No live AI, browser/package release, broad historical
playability, Windows or C2 qualification is claimed. App adoption and exact-set
coordinator review remain required; communication extension follows App's bridge.
