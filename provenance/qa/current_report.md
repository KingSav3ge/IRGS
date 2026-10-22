# IRGS independent QA

Candidate: `69c0f4f6bd7c65f9a41adc76d9eba807ce3b6b83`
Result: **passed** · 2026-10-22T17:01:23.699870+00:00

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
| runtime_operation_capture | passed |
| web | passed |
| interface | passed |
| tooling | passed |
| fresh_recursive_clone | passed |

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

Fresh independent HTTP checks against the exact assembled Engine/App/Catalog commits. Completed runtime capture, Web, interface and tooling checks from this update are included only after every recorded source hash matched the assembly. See CATALOG_V0_5_VALIDATION.json. No all-branch certification or new campaign release is claimed.

This report is not full C2/T01–T37 certification. Skips and missing providers are not passes. No user campaign was loaded or migrated.

## Component identities

Engine: `c0777be7e68021bd1bee66437d555390778c0adb`

App: `aac20055270cc64ba870061085cd8f6bfe43a93c`

Catalog: `c70dc16d4e48493b833dba5a0f68f43a972bdcb5`

App dependency pins match the candidate. Regression evidence matches every recorded source hash; the eight independent HTTP cases were newly executed against this assembly.
