# Migration and versioning impact — Core 3.2 / SCL 1.0 Full Maturation R2

**Status:** Candidate assembly, not automatic adoption. Baseline Core v3.2 and normative SCL v1.0 are unchanged byte-for-byte.

## Invariants

- Keep `IRGS-CORE-3.2` as the parent Core, `IRGS-SCL-1.0` as catalogue release, and immutable `@0.2` family revisions and aliases unchanged.
- Do not convert 228 held entries to `selected_qualitative` in the existing registry; there is no source-deprecation authority.
- All `K-*` actual facts and event writes remain with their established Core owners; contract texts are readonly references until selected and instantiated.
- Preserve every campaign's exact actors, conditions, stocks, custody, transit, time, commitments, messages, observations, ownership and historical events; do not infer new capabilities from added content.
- Preserve original v3.1 source/evidence under `provenance/` only. That archive is not a live dependency.

## Later promotion (per family only)

1. Compare source payload and original runtime adapter against drafted contract, resolving differences in both directions.
2. Supply unit-bounded local configuration, calibration provenance, prerequisites, and failure envelopes for any consequential operation.
3. Execute the authored entry-level acceptance cases in a compatible engine, including scarcity, simultaneity, Mixed, repetition, scale changes and resource conservation as appropriate.
4. Publish a **new immutable family revision** and an exact alias/selector crosswalk. Old immutable `@0.2` references still resolve to the old definition.
5. Test native genre adapters, selected combinations, and full release manifest before proposing adoption.
6. Seek explicit authorization to adopt the new catalogue and separately authorize any prospective campaign migration.

## No retroactivity

Importing this release package or an R1/R2 dossier does not modify prior play, set new prices, invent output rates, revise resolved casualties, or move inventory. The 420 acceptance **specifications** included here have not all been run in a live IRGS runtime. Synthetic package checks provide implementation confidence only within their stated envelope.
