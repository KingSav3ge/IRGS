# IRGS Core Unification — Round 8

**PROPOSED / UNSELECTED. Core v3.2 remains selected. Neither R7 nor R8 is adopted.**

Round 8 adds execution-derived dependency observations and a bounded autonomous institutional controller. Native multi-engine certification remains open.

Start with `CMRR_Round_8_Executed_Validation.md` and `ROUND_8_DEPENDENCY_CONTRACT.md`.

- `runtime/r8_dependencies.py`: observed reads, writes, negative lookups, structural scans, snapshot/code-bound evidence and conservative atomic frontiers.
- `runtime/r8_strategy.py`: household, business, government and military policies generate actions from one current world ledger.
- `runtime/test_r8_dependencies.py`: 26 new tests; 203 inherited tests preserved.
- `runtime/run_round8_evidence.py`: shared-handler inventory, 90-day execution, save/resume parity and exhausted-input scenario.
- `results/r8_operation_inventory.json`: observed evidence for 37 shared handlers; no universal branch-completeness claim.
- `results/r8_strategy_summary.json` and `r8_strategy_final_state.json`: actual long-run quantities and auditable state.
- `results/r8_cross_engine_gate_matrix.json`: seven source-pinned engines, each explicitly NOT CERTIFIED for native dependency coverage.
- `IRGS_Core_Engine_v3_3_Unification_Candidate_R8.md`: complete inherited R7 candidate plus R8 Appendix E.
- `IRGS_Core_v3_3_Candidate_Binding_Proposal_R8.json`: unselected proposal only.

From `runtime`, run `python -m unittest discover -p "test_*.py" -v` and `python run_round8_evidence.py`. The second command executes two 90-day runs and may take several minutes. No third-party Python packages are required. Run `python build_r8.py` from the package root to refresh document/binding hashes and the manifest after evidence generation.

Historical R7 files and results remain unchanged. Their paths and counts describe R7, not this adapter. The character concept archive was listed as visual reference material; no image captions were imported as simulation facts or instructions.
