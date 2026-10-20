# IRGS Core Unification — CMRR Round 7

**Status: PROPOSED / UNSELECTED.** Current selected Core remains **v3.2**. This archive is a candidate design/research package; no live engine/campaign migration or adoption is implied.

## Deliverables

- `IRGS_Core_Engine_v3_3_Unification_Candidate_R7.md`: **complete rebuilt** 124-section Core candidate with 9 R7 subsections and 18 Appendix C acceptance requirements. Earlier R1–R6 material remains, not patch-only.
- `CMRR_Round_7_Executed_Validation.md`: source comparison, function disposition, ownership reconciliation matrix, execution evidence, test limitations, accounted removals, acceptance/calibration gaps and migration impact.
- `IRGS_Core_v3_3_Candidate_Binding_Proposal_R7.json`: **unselected** candidate binding containing the document hash.
- `runtime/r7_frontier.py`: bounded opt-in event scheduler with R6 tracked-work dispatch, conservative dependency components, physical-loss reconciliation, and opt-in intermediate/quality/disposition lifecycle.
- `runtime/r7_audit.py`: separately coded read-only material/provenance audit (not a second simulator).
- `runtime/test_r7_integration.py`: 38 new tests, cases 166–203. Inherited 165 tests are untouched.
- `runtime/run_round7_fixture.py`: reproducible synthetic multi-institution scenario; material balances, actual events, obligations and stock dispositions are recorded in `results/round7_integration_fixture.json`.
- `sources/`: source-preservation copies for v3.2, R6, Military, Roman and R6's complete historical source inventory.
- `results/`: actual unit test output, structural check, source-integrity/checksum manifest, fixture output.

## Reproduce

```bash
cd runtime
python -m unittest discover -p 'test_*.py' -q
python run_round7_fixture.py
```

Expected in the current reference environment: **203 tests passing**; 17 scheduled fixture events committed and zero fixture contests. Population remains 1,200; cash remains 1,000. Opening seed 16 = 4 consumed + 9 lost + 3 remaining; iron 10 = 3 consumed + 7 remaining. Two intermediate units made; one destroyed and one salvaged, producing one scrap unit and **zero finished shields**. Farm accepted grain is 12; kitchen makes 12 meals. Outcomes use chosen synthetic input data, not validated agricultural, industrial, wage, legal, or medical models.

## Critical boundaries

- This adapter does not authenticate source evidence, verify actual legal authority, prove general cross-module footprints, or implement all original CE case specifications.
- Workpiece conversion does **not** model worker-hour commitments, machine runtime, power, real quality, realistic losses or multi-stage manufacture; users must supply a compatible selected profile. This is a documented gap, not a free activity by Core rule.
- Same-time contentious operations remain unresolved, except verified physical loss committed to actual stock with conflicting work claims retained; this is not universal causality arbitration.
- Test success and checksum equivalence within one implementation are not independent validation, calibration, acceptance, playtesting or deployment.
