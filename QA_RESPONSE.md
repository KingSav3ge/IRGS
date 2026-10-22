# Environment QA response — 2026-10-22

Report source: `qa/engine-validation` at `a28d1d44f31e00ba2cab4f91a894cf266e7d4bec`, testing `bf6cf48`. That branch is a report stream with separate history, not engine source to merge.

| Finding | Reproduced | Correction | Regression evidence |
| --- | --- | --- | --- |
| IRGS-QA-001 | The accepted `water` inventory caused the Rise view to disconnect. | Unconfigured units remain explicit; physical quantity and readable inspection are preserved. The UI displays “unit not configured” without inventing units. | `IRGS_Web/tests/test_rise.py`, the interface suite and the unmodified independent QA case. |
| IRGS-QA-002 | Canonical Core location confirmation hid local stores and blocked movement. | Settlement consumers read the established value from either a canonical field record or the existing reviewed starting string. | `IRGS_3_3/runtime/test_settlement.py`, the Rise HTTP suite and the unmodified independent QA case. |

The same eight-case independent script produced six passes/two failures before correction and eight passes after correction against the local working candidate. Current aggregate results and source identity are in `DEPENDENCY_REJECTIONS_VALIDATION.json` and the operation register. Remote confirmation must identify the new published candidate; an older report does not become a retest merely because the source changed.

For continued development, inspect the latest QA report's candidate commit before acting on a finding. Preserve unresolved reports and compare their reproduction with current code. Fixes belong in the source branches, while QA retains its independent report history. No user campaign is an input to this qualification.
