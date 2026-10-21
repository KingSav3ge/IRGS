# IRGS 3.3.3 — Unified Development D1

This is the combined development source for IRGS: the selected Core 3.3 runtime and complete catalogue, C2 engine specification, and the preferred Emergent visual design on the canonical Solo website. It is a verified development baseline, not a claim that the proposed general gameplay engine is finished.

Start the local site with [Start-IRGS.cmd](Start-IRGS.cmd). It verifies the installed files and opens the existing loopback host at http://127.0.0.1:8765/. An already running compatible host may be reused. To inspect this clean checkout independently, run `python -B IRGS_Web/server.py --port 8766` and open http://127.0.0.1:8766/. Existing campaigns remain in the original installation; this copy includes no user saves or migration.

| Source | Continue work here |
| --- | --- |
| Executable engine, data and genre catalogue | `IRGS_3_3/` |
| Website and app | `IRGS_Web/` |
| Applied C2 engine specification | [engine/Core/IRGS_Core_3_3_3_E_C2.md](engine/Core/IRGS_Core_3_3_3_E_C2.md) |
| Development workflow | [DEVELOPMENT.md](DEVELOPMENT.md) |
| Remaining implementation and gates | [ROADMAP.md](ROADMAP.md) |
| Current verification evidence | [VALIDATION.json](VALIDATION.json) |
| Published source records | `provenance/` and [DEVELOPMENT_STATE.json](DEVELOPMENT_STATE.json) |

Setup requires a selected character; dated availability, filtered inspection, exact-intent recovery, withdrawal and recoverable campaign Trash are implemented. The runtime also supports observed event frontiers and specific domain operations. General player action resolution, elapsed-time gameplay and the complete autonomous institutional cycle remain implementation work. C2's 121 acceptance cases remain required and unexecuted.

This integrates [engine C2](https://github.com/KingSav3ge/IRGS/commit/96af47961b33df83031f98d0524415bba299ce03) and [app UI1](https://github.com/KingSav3ge/IRGS/commit/2022c922fb10bbcb1bb08c1ef160e38d6f449f8d). The primary branch is `main`; Engine/Core development uses `3.3.3.E`, App/Web uses `3.3.3.A`. Continue both from this unified layout, keeping one editable app and one campaign-state kernel. Historical overlays are retained through Git ancestry and their provenance records rather than duplicate editable app folders.

The three original root ZIPs, original packaging manifest/checksums, build instructions and verifier are unchanged archival 3.3.3 inputs. They do not contain this new development consolidation. Historical validation under `IRGS_3_3/results/` is inherited evidence, not the fresh D1 verification. Use the new development tools for clean verification and packaging; do not run the old release rebuild scripts as if they were standalone development commands.
