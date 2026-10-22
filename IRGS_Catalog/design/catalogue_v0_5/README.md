# IRGS Complete Campaign Catalogue — Concept v0.5

**Package date:** 2026-10-22  
**Entries:** 44 (31 launch-target, 12 future, 1 Curated Simulation System)  
**User decisions preserved; unapproved descriptions and ideas flagged as proposals.**

## Contents

- `catalogue.json` — app-adapter-ready single-file dataset (44 entries).
- `SCHEMA.json` — JSON Schema for individual records.
- `records/` — 44 independently editable JSON records.
- `previews/` — 44 readable per-title markdown briefs, including readiness gates.
- `MANIFEST.json` — launch order and candidate grouping.
- `DECISION_REGISTER.md` — adopted decisions, proposals, superseded concepts and outstanding approvals.
- `INTEGRATION_NOTES.md` — safe integration, Core 3.3 and Kira source notes.

## Classification

1 SS; 1 CC = 6 SS; 1 FC = 5 CC = 30 SS; 1 MC = 4 FC = 120 SS; 1 GC = 2 MC = 240 SS. Curated Simulation Systems are separate. This equivalence does not imply campaign bundle entitlement.

## Caution

- These files are **not deployed into the IRGS app**, do not include copyrighted artwork and do not certify running engine features.
- Proposed app paths are design suggestions only.
- Previews and play buttons are disabled by default. The user must approve publication, and release must be independently verified.
- Historical dates and culturally specific information not user-adopted remain research propositions.

## Implementation handoff

Import records to a draft-only content catalogue, provide review/edit UI with provenance, reconcile actual website paths/API, then approve titles/assets before making previews visible. Implement, test and release campaigns separately using the Core/Genre/Setting/Profile/State architecture.
