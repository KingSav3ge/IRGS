> **Current selection: maintenance R3.** See [MAINTENANCE_R3.md](MAINTENANCE_R3.md) and the top-level deployment binding. Parent pins and validation changes are explicit; historical reports/snapshots retain their original scope.

# IRGS Core v3.2 + Shared Content Library v1.0 — Full Maturation R2 Package

**Date:** 14 October 2026  
**Status:** Consolidated, source-preserving *candidate*. Core 3.2 and SCL 1.0 normative definitions remain unchanged; R1/R2 content is **proposed**, not selected or adopted.

## Start here

1. **`IRGS_Core_Engine_v3_2.md`** — complete normative shared Core, 123 numbered topics / eleven domains.
2. **`IRGS_Shared_Content_Library_v1_0.md`** — complete normative shared catalogue prose.
3. **`IRGS_Shared_Content_Registry_v1_0.json`** — authoritative 279-family, 1,416-alias registry (51 selected / 228 held; individual revision `@0.2`).
4. **`IRGS_SCL_v1_0_Selected_Contracts.md`** — the 51 existing selected qualitative definitions.
5. **`IRGS_SCL_v1_0_Complete_Qualification_Compendium.md`** — consolidated editorial reading of all 228 held-family maturation drafts (36 R1 + 192 R2).
6. **`IRGS_SCL_Consolidated_Qualification_R2.json`** — combined machine-readable review overlay, explicitly non-normative.
7. **`IRGS_SCL_Full_Reconciliation_Matrix.csv`** / **`IRGS_SCL_Qualification_Acceptance_Matrix.csv`** — exhaustive family crosswalk and unexecuted acceptance case specifications.
8. **`IRGS_SCL_v1_0_Full_Release_Migration_Impact.md`** — prospective promotion and migration requirements.
9. **`IRGS_Full_Release_CMRR_Validation.md`** — reconciliation, test evidence, limitations, and accounted removals.

## Also included

- Original standalone R1 and R2 qualification Markdown, JSON, hold/calibration registers and CMRR reports.
- Exact reference map and Core v3.2 genre bindings.
- `tests/verify_full_release.py`, `tests/verify_maturation_r1.py`, `tests/verify_maturation_r2.py`.
- `provenance/IRGS_Core_v3_1_Complete_Release_Archived.zip` and the original v3.2 manifest. These are historical and **not active**.

## Reproduce checks

```bash
python tests/verify_full_release.py
python tests/verify_maturation_r1.py
python tests/verify_maturation_r2.py
```

Tests check structural integrity, exact source retention, typed aliases, text/case coverage, and bounded synthetic accounting. They do **not** establish calibration, complete live simulation, independent engineering certification, playtesting, or approval to deprecate original source records.

## Authority note

This is a **full distribution**, not a silent rules migration. Existing Core, catalogue, and campaign authority remain unchanged. Individual held entries cannot be promoted until their required validation, immutable revision, and explicit adoption occur.
