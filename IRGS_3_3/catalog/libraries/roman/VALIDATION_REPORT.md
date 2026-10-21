# IRGS Roman Republic Content Library v1.0 — Verification Summary

**Status:** Candidate release; no automatic campaign adoption or migration. Roman Slim v1.2's accepted workshop reference remains unchanged.

## Checks actually performed

- **2066 passing executable checks** of source snapshot hashes, manifest sizes/checksums, 118-entry JSON/CSV reconciliation, 14 original Roman content bindings and 13 SCL-backed aliases, and source section dispositions.
- Checks of **all 32** source sections (20 full v1.0 plus 12 Roman Slim v1.2) and no missing source section in the CMRR matrix.
- **64 acceptance specifications** are fully enumerated and marked *not executed in complete IRGS runtime*.
- **29 calibration and historical-eligibility gaps** enumerated without assigning unsupported numerical defaults.
- Bounded synthetic probes of denarius-accounting versus actual coin count, payee-specific transfer, finite consignment in transit, one sword with multiple modes, non-inventory unarmed method, simultaneous local wear aggregation and duplicate-event prevention.

## Explicit limitations

No full Roman runtime was exercised. No physical protection realism, gladiatorial balance, historical research, medical/physiological realism, live gameplay, adoption or existing campaign migration was certified. These remain future qualifications with exact profile, evidence and acceptance case records.

## Source policy

The accepted Roman Slim v1.2 and its original native content-binding JSON are preserved byte-for-byte in `sources/`. The SCL v1.0 registry is included read-only, independently pinned by hash. The Roman library adds **118 proposed dated content compositions** while retaining all **14** native selections and immutable SCL identity boundaries.

`python tests/verify_roman_content_release.py <unpacked_package_folder>` reproduces these checks.
