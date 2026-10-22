# IRGS independent QA

Candidate: `86528c60a0a3d3946cf7f81177b0115cf1528e34`
Result: **passed** · 2026-10-22T16:23:26.349840+00:00

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
| browser | passed |

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

Fresh independent HTTP cases against this assembled pair. Existing completed regression runs are included only after verifying the exact Engine/App release hashes match their recorded source identities. See CATALOGUE_COMPONENT_VALIDATION.json and COMPONENT_PUBLISH_VALIDATION.json.

This report is not full C2/T01–T37 certification. Skips and missing providers are not passes. No user campaign was loaded or migrated.

## Component identities

Engine: `c0777be7e68021bd1bee66437d555390778c0adb`

App: `3ec412c8e383022fa7a3b79b477daed27a122c95`

This is an isolated assembly, not an integration or deployment. App dependency matches candidate: **true**.

Regression evidence was reused only after matching both component release hashes to the completed fresh runs. The independent HTTP cases were newly executed against this assembly.
