# IRGS independent QA

Candidate: `c56572caac5e94c2d949d1b83eaa803a415ffa29`
Result: **passed** · 2026-10-22T17:51:24.232441+00:00

Engine Development owns mechanics fixes. QA runs isolated, synthetic campaigns and reports observed behavior.

| Finding | Priority | Status | Result |
| --- | --- | --- | --- |
| IRGS-QA-001 | P1 | not_reproduced | Accepted Core material establishment breaks Rise playthrough views |
| IRGS-QA-002 | P1 | not_reproduced | Canonical Core location records are incompatible with Rise location consumers |

Independent cases: 8 passed, 0 failed, 0 errors.

| Check | Status |
| --- | --- |
| source-integrity | passed |
| evidence-freshness | passed |
| runtime | passed |
| web | passed |
| interface | passed |
| tooling | passed |

## IRGS-QA-001

Accepted Core material establishment breaks Rise playthrough views

**Expected:** Reject an unsupported material atomically, or retain a readable campaign with explicit unknown unit support.

**Boundary:** IRGS_Web/rise_campaigns.py view indexes model.units[material]; Core stock establishment accepts material IDs without that unit binding.

Reproduce:

1. Create a reviewed R00 Rise campaign.
2. Creator POST /api/event: establish_stock(location=founder-home, material=water, quantity=2, inventory_evidence_ref=synthetic-measured-water).
3. Observe the successful save and valid CoreWorld state.
4. GET /api/playthrough/<id> with the normal session token.

## IRGS-QA-002

Canonical Core location records are incompatible with Rise location consumers

**Expected:** A supported, established location confirmation must leave local inventory and supported movement usable.

**Boundary:** Core confirm_character_field writes {value,evidence_id,at}; settlement_runtime.location and Rise view consume the whole record as a site string.

Reproduce:

1. Create R00 at the commons.
2. Creator records and delivers established evidence placing the founder at commons.
3. Creator confirms founder.location=commons through confirm_character_field with authority and player instruction references.
4. Inspect local inventory and submit walk_clearing.

## Scope

Current Core/App regression suites plus independent HTTP checks. Contracts: R00 founding, shared Core interoperability, material continuity, replay, restart, privacy and retained intent.

This report is not full C2/T01–T37 certification. Skips and missing providers are not passes. No user campaign was loaded or migrated.

## Repository and attachment validation

Engine: `2c5590bcb2d7ee7e02f597526c3cb341841bd2dd`

App: `3980e5665814847d3cd02c0f0b86417a231e2be6`

Catalog: `c70dc16d4e48493b833dba5a0f68f43a972bdcb5`

All Git object checks and source integrity checks passed. The App pins match the standalone component commits, and the joined source import dry-run reported no changed or removed files. Fresh standalone Historical Reference checks passed (6 provider and 4 HTTP cases). The archive ZIP remains an external attachment and was not available in this cloud run; synthetic reference archives were used. Package smoke passed on 9 routes without creating campaign records.
