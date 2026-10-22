# Environment QA response — 2026-10-22

Report source: `qa/engine-validation` at `a28d1d44f31e00ba2cab4f91a894cf266e7d4bec`, testing `bf6cf48`. That branch is a report stream with separate history, not engine source to merge.

| Finding | Reproduced | Correction | Regression evidence |
| --- | --- | --- | --- |
| IRGS-QA-001 | The accepted `water` inventory caused the Rise view to disconnect. | Unconfigured units remain explicit; physical quantity and readable inspection are preserved. The UI displays “unit not configured” without inventing units. | `IRGS_Web/tests/test_rise.py`, the interface suite and the unmodified independent QA case. |
| IRGS-QA-002 | Canonical Core location confirmation hid local stores and blocked movement. | Settlement consumers read the established value from either a canonical field record or the existing reviewed starting string. | `IRGS_3_3/runtime/test_settlement.py`, the Rise HTTP suite and the unmodified independent QA case. |

The same eight-case independent script produced six passes/two failures before correction and eight passes after correction against the local working candidate. Current aggregate results and source identity are in `DEPENDENCY_REJECTIONS_VALIDATION.json` and the operation register. The independent cloud retest now confirms the published candidate, as recorded below.

For continued development, inspect the latest QA report's candidate commit before acting on a finding. Preserve unresolved reports and compare their reproduction with current code. Fixes belong in the source branches, while QA retains its independent report history. No user campaign is an input to this qualification.

## Independent cloud confirmation

The report stream at `0f5e10fd8904a72acc603d0c6505ed45abf29590` tested source commit `59f24344d2ff51404071822f8975f3d70b972814` and passed at 2026-10-22 14:29:51 UTC. The supplied LATEST.md matches that report's text. IRGS-QA-001 and IRGS-QA-002 were both **not reproduced**; all eight independent cases passed with no failures, errors or skips.

Source integrity, evidence freshness, runtime, Web, interface and tooling checks passed. The cloud runtime ran 486 tests with one skip; Web ran 142 with seven platform skips; interface passed 56 checks and tooling ran 20 with no skips. Skips are not passes. These are independently reported cloud results, not new local executions.

The exact reports are preserved as [Markdown](provenance/core_consolidation_validation/cloud_QA_59f2434.md) and [JSON](provenance/core_consolidation_validation/cloud_QA_59f2434.json). This closes the two named findings for the tested candidate. It does not certify every dependency branch or the full C2/T01–T37 scope. No user campaign was loaded or migrated. This confirmation changes evidence and status only; executable sources remain those tested at `59f2434`.
