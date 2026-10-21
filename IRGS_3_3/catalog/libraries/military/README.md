# IRGS Military Content Library v1.0 — Proposed Rebuild

Start with `IRGS_Military_Content_Library_v1_0_Candidate.md` for the full authored library. This package includes an indexed machine-readable military template catalogue, a complete 6×12 era/category candidate matrix, an exact shared-family crosswalk, 60 acceptance specifications, CMRR/validation evidence, and the two unmodified military sources under `provenance/`.

Dependencies are **Core v3.2 and SCL v1.0**, referenced, not repackaged. The canonical SCL definitions retain their individual `@0.2` family revision. The uploaded **Soldier/Military Slim v1.0** remains pinned to Core 3.0/SCL 0.1 pending an explicit completed compatibility bridge. This package does not silently migrate it.

Verification: `python tests/verify_military_library.py` (standard-library only).

Status: **Proposed.** The 48 military templates have not been individually qualified, and the 60 acceptance specifications are not live-playtested. No numerical equipment specification or campaign state was manufactured.
