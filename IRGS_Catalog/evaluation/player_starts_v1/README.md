# Player-start requirements and baseline diagnostics 1

This Catalog-owned evaluation supports IRGS-PLAY-001/002/004. It supplies four
separate actor instruction documents, evaluator-only acceptance criteria, a
John/1415 source dossier and an offline evaluator evidence schema. It adds no
initializer, runtime readiness API, capability, campaign release or save repair.
Content presence, reference verification, character eligibility and an executable
slice remain separate facts.

The baseline is the coordinator's evaluated unified 3.4.2 commit
`ba551af285a6e1eb0766a9d06f83cbc0e5335b35`. Consumer diagnostics select exactly
Engine `91b20056e7db651966c9e92925313494917f47b1` and App
`00634b15f2d8d4a8626d3eb3cb0a139559ac1fcc`; App commits Catalog
`3f921252e50a0976cb88321b6ff8249a5f12466d`. Tests explicitly select this Catalog
candidate. No dependency pointer is changed. Later owner instruction commits
publish no new start contract. Future runtime fixes need a new compatibility
selection and fresh acceptance, retaining this baseline record.

## Cross-component acceptance matrix

| Finding / path | Engine requirement | App requirement | Catalog evidence |
| --- | --- | --- | --- |
| PLAY-001: John of Lancaster, 1415 | Source-backed personal context, actual actor access and a bounded supported operation; eligibility alone is insufficient. | Review the selected person's actual readiness before creation; show legitimate received context and exact results. | Dossier ties identity/role to the adopted snapshot and separates unknown placement, resources, authority and information. No fictional courier assignment. |
| PLAY-002: new human, default no opening | Publish actual supported mode/capabilities without inventing context or possessions from background testimony. | Explicit reference/declaration choice or a separately reviewed supported slice. No unlabeled executable-start claim. | Negative declaration test checks unchanged physical state and absent invented elapsed time; baseline missing classification remains an open gap. |
| PLAY-002 regression: new human, explicit quay opening | Preserve the actual fictional map/custody/rules and actor-scoped setup. | Explicit review, confirmed listed action, received result, save/reload/retry. | Five actual actions, including unsuccessful shortcut, 150 local seconds and one conserved dispatch delivered. |
| R00 regression | Preserve reviewed setup, finite materials and actual work handler. | Reviewed creation, explicit actions, received result and recovery. | Actual walk/found/build/two `wait_hour` requests: 3,600 work seconds, 3,900 elapsed seconds and founder timber 6 to 3. |
| PLAY-004: historical paths | Sourced initial Julian date and day precision; unknown hour remains unknown; keep elapsed/causal/civil axes separate. | Present the actual date/precision distinctly from local elapsed time. | Adopted source is 11 August 1415, Julian, day precision, no hour. Current historical view's unresolved civil date remains a gap, including in the working quay slice. R00 has no required historical date. |

A positive loop requires reviewed actor context, legitimate receipt of that
context, a listed actual operation, explicit confirmation, an actor-received
result, retained save/reload and exact request recovery. `assess_evidence` checks
these independently from reference readiness and explicit mode/date acceptance.
Its inputs are evaluator observations, not browser claims or an Engine/App DTO.
Schema-valid examples do not establish real execution or confer authorization.

The current John/default empty starts are diagnostic observations, never desired
positive expectations. Actor instruction `actions: []` means this baseline has
no selected supported operation for that diagnostic; the goal still requires a
reviewed existing-person loop or honest explicit limited mode. The diagnostic
report marks unmet gates as gaps. Passing tests of the evaluator are not passing
product acceptance for those gaps.

## Provenance, uncertainty and access

`requirements/john_1415.json` references exact Engine snapshot bytes and JSON
pointers. John is `HYW-JOHN-BEDFORD`, distinct from John the Fearless. The adopted
April-council source supports the role reference; individual eligibility comes
from the separate authored Solo policy. Neither is a current operational mandate.
Reference sources do not automatically become actor receipts. Exact location,
nearby people, possessions, retinue readiness and who received which information
need reviewed evidence; unknown does not mean zero. No hour, army, cash, NPC choice
or historical future is supplied here. Engine owns any new initializer/rule;
App owns its authenticated controls and presentation. Continuing saves are never
reseeded from these requirements.

Actor exports contain only their selected instructions. Acceptance criteria and
the privacy marker stay in `evaluator_only/`. R00 reuses the original fixture's
reviewed setup, without exporting its private oracle. This material consists of
new authored instructions and source references, not copied historical prose or
archive/private-save payloads. Local synthetic processing is permitted; external
provider processing is not authorized by the fixture.

## Run and limits

Use Python 3.12+ without `-O`, clean exact owner checkouts and a fresh process:

```bash
python -B IRGS_Catalog/player_start_evaluation.py
python -B -m unittest tools.tests.test_player_start_contract tools.tests.test_standalone_catalog -v
IRGS_START_ENGINE_SOURCE=/path/to/Engine \
IRGS_START_APP_SOURCE=/path/to/App \
IRGS_START_EVIDENCE_OUTPUT=/tmp/player-start-observations.json \
python -B -m unittest tools.tests.test_player_start_consumers -v
```

The seven HTTP cases use actual reviewed creation, owner handlers, fresh Store
instances, exact result lookup and restart. They check retained unsupported
intent/withdrawal without physical effects, hidden stock/permission not selecting
menus, fictional-opening rejection for the historical person, adopted source
references and the revised Catalog availability copy reaching App. Both provider
dispatch and direct transport are forbidden. Synthetic hidden-stock mutation has
a matching opening conservation basis and is used only for privacy/menu checks.

See root `PLAYER_START_VALIDATION.json` for executed results and unmet product
gates. Engine's versioned existing-person context/readiness and App's selected-mode
and civil-date contracts remain pending. Communication evaluation follows its
future App bridge. All previous fixtures, 750 system variants, 250 drafts,
32 recipes, 44 previews and original archive bytes remain preserved. No new
historical start, browser/package qualification, live AI or full C2 is claimed.
