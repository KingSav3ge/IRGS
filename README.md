# IRGS 3.3.3 — Unified Development D1

**The World of Kira** is available as a campaign-world guide in the Content Library. Its revival package preserves nine original Word documents and catalogues six mapped regions on separate continental shelves, including Aldain’s supplied political colour key. Starting snapshots remain in development. See [the Kira package](IRGS_3_3/catalog/campaigns/kira/README.md).

This is the combined development source for IRGS: the selected Core 3.3 runtime and complete catalogue, C2 engine specification, and the preferred Emergent visual design on the canonical Solo website. It is a verified development baseline, not a claim that the proposed general gameplay engine is finished.

Start the local site with [Start-IRGS.cmd](Start-IRGS.cmd). It verifies the installed files and opens the existing loopback host at http://127.0.0.1:8765/. An already running compatible host may be reused. To inspect this clean checkout independently, run `python -B IRGS_Web/server.py --port 8766` and open http://127.0.0.1:8766/. Existing campaigns remain in the original installation; this copy includes no user saves or migration.

| Source | Continue work here |
| --- | --- |
| Executable engine, data and genre catalogue | `IRGS_3_3/` |
| Website and app | `IRGS_Web/` |
| Applied C2 engine specification | [engine/Core/IRGS_Core_3_3_3_E_C2.md](engine/Core/IRGS_Core_3_3_3_E_C2.md) |
| Development workflow | [DEVELOPMENT.md](DEVELOPMENT.md) |
| Remaining implementation and gates | [ROADMAP.md](ROADMAP.md) |
| Prioritised continuation checklist | [DEVELOPMENT_LIST.md](DEVELOPMENT_LIST.md) |
| Current operation inventory and gaps | [engine/OPERATION_COVERAGE.md](engine/OPERATION_COVERAGE.md) |
| Qualification of the operation register | [COVERAGE1_VALIDATION.json](COVERAGE1_VALIDATION.json) |
| Original D1 verification evidence | [VALIDATION.json](VALIDATION.json) |
| Published source records | `provenance/` and [DEVELOPMENT_STATE.json](DEVELOPMENT_STATE.json) |

Setup requires a selected character; dated availability, filtered inspection, exact-intent recovery, withdrawal and recoverable campaign Trash are implemented. The first continuation increment adds a bounded authorized equipment action with an atomic outcome and recoverable receipt, plus contextual response drafts and an editable own-response field. Suggested approaches may fail; they are not a list of guaranteed solutions. See [CONTINUATION_STATUS.md](CONTINUATION_STATUS.md) for scope and evidence.

New human characters at the 1415 entry can opt into **A dispatch before departure**, a playable fictional opening with local movement, observation, failed attempts, conserved delivery and saved elapsed consequences. Review it during character creation. See [the implementation scope](engine/PLAYABLE_OPENING_IMPLEMENTATION.md). General freeform resolution, combat, interruptible timed phases and the complete autonomous institutional cycle remain implementation work. The original C2 inventory remains unchanged; scoped implementation evidence is tracked separately rather than claiming all 121 cases passed.

This integrates [engine C2](https://github.com/KingSav3ge/IRGS/commit/96af47961b33df83031f98d0524415bba299ce03) and [app UI1](https://github.com/KingSav3ge/IRGS/commit/2022c922fb10bbcb1bb08c1ef160e38d6f449f8d). The primary branch is `main`; Engine/Core development uses `3.3.3.E`, App/Web uses `3.3.3.A`. Continue both from this unified layout, keeping one editable app and one campaign-state kernel. Historical overlays are retained through Git ancestry and their provenance records rather than duplicate editable app folders.

The three original root ZIPs, original packaging manifest/checksums, build instructions and verifier are unchanged archival 3.3.3 inputs. They do not contain this new development consolidation. Historical validation under `IRGS_3_3/results/` is inherited evidence, not the fresh D1 verification. Use the new development tools for clean verification and packaging; do not run the old release rebuild scripts as if they were standalone development commands.

The **Rise v0.4 implementation source** is now available as a [readable specification and implementation plan](engine/design/rise/README.md), with the original DOCX retained under `provenance/rise/`. The first executable Rise qualification will use the user-selected fictional founding example. This source import does not yet supply a playable settlement initializer. The original Kira package is retained under `provenance/kira/`.

The [Century of Conflict paused submission](provenance/century_of_conflict/README.md) preserves the uploaded WIP archive, original pause note and expanded source changes. Its 36 additional opening drafts remain inactive pending historical and executable qualification.
