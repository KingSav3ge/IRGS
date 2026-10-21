# IRGS Military Content Library v1.0 — CMRR and qualification report

**Status:** Proposed and source-reconciled; not adopted, numerically calibrated or live-playtested.

## Compare

- `ML-0.1` provides seven sections: six eras, twelve categories, three tables of period families, nonnumeric expansion guidance and representative historical research links.
- `MLS-SLIM-1.0` provides 17 military-life sections and thirty genre acceptance cases, pinned to Core 3.0 and SCL 0.1. Its equipment and qualification workflows are source requirements, not silently upgraded to Core 3.2.
- SCL v1.0 contains 279 neutral family records with retained `@0.2` identities and source holds. Generic equipment definitions and resource accounting are inherited, not copied into an additional military ledger.

## Merge and reconcile

| Issue | Decision | Risk prevented |
|---|---|---|
| Era tags and period grouping | Preserve six labels and source descriptions | False universal tech progression |
| Category ontology | Preserve twelve original codes and scope | Missing operational or daily-life equipment |
| Mixed transport table | Split conservatively to TRN/NAV/AIR | Silent loss of vessel, aviation, space branches |
| Missing by-era ammunition column | Add explicitly derived candidate MUN entries | Fictional claim of original statistical ammo data |
| Generic vs military specific content | Use SCL exact refs for physical families; new MIL templates for specialization | Duplication and conflicting ownership |
| Weapon source modes | Keep selectors and one asset | Duplication of inventory or attacks |
| Soldier/Military Slim Core 3.0 pin | Mark compatibility bridge pending | False migration to Core 3.2 |
| Fantasy values in shared aliases | Keep scope-qualified, do not transfer | Unsupported historical/modern ballistic effects |
| New templates | Proposed and unqualified | False adoption/calibration |
| Campaign state | Untouched | Retroactive repairs, ammunition, pay or knowledge |

**No silent removals:** Every source section has a documented disposition in the main library. Seven ML sections and 17 Slim sections remain readable in the archived original files.

## Completeness and evidence

- 6 exact era tags; 12 exact category codes; 72 unique era/category cells.
- 48 proposed military-specialization templates, no duplicates.
- 13 exact example SCL references validated against the normative registry.
- 60 uniquely numbered acceptance specifications. These are not claimed as executed playtest cases.
- Execute the accompanying `tests/verify_military_library.py` for machine-checkable catalogue and provenance invariants; this is structural/synthetic validation only.

## Calibration and gating

Before a specific model is active: require dated setting availability, actual construction/performance/units, compatible mechanism and resolution model, qualified operator/crew, stock/maintenance/fuel/route, owner and authority, failure/counterplay, and appropriately executed acceptance cases. No numbers invented from a family index. `R1/R2` held SCL contract drafts do not automatically promote the normative SCL held families. The library is a candidate, not a deployment migration.
