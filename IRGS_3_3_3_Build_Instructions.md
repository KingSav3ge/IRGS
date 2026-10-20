# IRGS 3.3.3 — Core, Catalog and Live packages: assembly and build instructions

**Prepared:** 20 October 2026 · **Content basis:** the Codex 3.3.2 tree found at `IRGS-3_3_E_1.zip → codex_332/IRGS-3.3.2/x332` (design patch `DESIGN-PATCH-2026-10-20`), as re-split in your `IRGS-3_3_3.zip`, reconciled against `IRGS-3_3_C_1.zip` and the C2 engine design (`CLAUDE_HANDOFF.md`).
**Status of this document:** instructions for implementers. It reports what was verified and what was not; it does not certify any new gameplay.

---

## 1. What you are holding

IRGS **3.3.3** is a package edition of Core 3.3. It is three separately hashed archives, a manifest and a verifier.

| File | Contents | Size |
|---|---|---|
| `IRGS_Core_3_3_3.zip` | `IRGS_3_3/` without the catalog: runtime (57 Python files), genre engines, `data/`, `results/`, release builder and packager, Windows launcher | 101 files, about 1.3 MB |
| `IRGS_Catalog_3_3_3.zip` | `IRGS_3_3/catalog/`: source manifest, genres, libraries, profiles, design references | 155 files, about 24 MB |
| `IRGS_Live_3_3_3.zip` | `IRGS_Web/`: the live loopback host (`server.py`), `features.py`, `gameplay_views.py`, `history_views.py`, `opening_scene.py`, `static/`, `tests/` | 18 files, about 100 KB |
| `IRGS_3_3_3_PACKAGE_MANIFEST.json` | SHA-256 of every zip and of all 274 files in them | |
| `verify_irgs_3_3_3.py` | Standard-library verifier (section 3) | |

No campaign saves, caches or `__pycache__` are included. The zips are deterministic: rebuilding gives byte-identical archives.

### What "3.3.3" does and does not mean
- **File contents are unchanged from 3.3.2.** I confirmed the received Core zip is byte-identical to the 3.3.2 Core minus its catalog, and the catalog matches in all 155 files. This edition re-identifies and re-packages them; it adds no code or mechanics.
- **`release.json` is deliberately untouched.** It still says `release_id: IRGS-CORE-3.3-SUITE` and `version: 3.3`, because those name the **Core** (3.3), and it still verifies. The edition label 3.3.3 lives in the manifest. Changing `release.json` belongs to the official build in your live workspace (section 7), where the saves and result logs exist.
- Packaging fixes carried forward from 3.3.2: `IRGS_Web` sits **beside** `IRGS_3_3` (not inside it), and the catalog is included and placed at `IRGS_3_3/catalog/`, where the release expects it.

## 2. Assemble

Extract **all three zips into the same empty folder** (merge). The result must be:

```
<folder>/
  IRGS_3_3/          Core (runtime, data, results, release.json, Start-IRGS-3.3.cmd ...)
    catalog/         from the Catalog zip
  IRGS_Web/          from the Live zip
```

Do not rename either top folder; `release.json` pins paths such as `IRGS_Web/server.py` and `catalog/...` relative to this layout.

**Run it:** double-click `IRGS_3_3/Start-IRGS-3.3.cmd` (Windows), or `python IRGS_Web/server.py --port 8765` and open `http://127.0.0.1:8765`. Do not run with `-O`; the host refuses.

## 3. Verify the assembly

**Step 1: hashes and integrity.** From anywhere:

```
python verify_irgs_3_3_3.py <assembled-folder> --zips-dir <folder-with-the-zips>
```

It checks each zip hash, every one of the 274 files, that nothing unexpected sits in the pinned trees (saves, caches and logs are ignored), then runs IRGS's own `irgs.py verify`. Expected: `RESULT: PASS`. It was also checked to **fail** on a modified file and on a stray file. It never modifies anything.

**Step 2: tests** (run on a fresh assembly of these exact zips; Python 3.12, Node 22):

| Check | Command | Expected |
|---|---|---|
| Core/runtime | `cd IRGS_3_3/runtime && python -B -m unittest discover -p "test_*.py"` | 393 run, OK, 1 skipped (about 75 s) |
| Web | `cd IRGS_Web/tests && python -B -m unittest test_gameplay test_history_views test_host test_starting_flow test_stage1` | 13 + 24 + 22 + 15 + 12, all OK |
| Frontend (synthetic DOM) | from the assembled folder: `node IRGS_Web/tests/test_gameplay_ui.js` | 30 checks passed |
| Launcher | `test_launcher` | skipped on non-Windows |

These are scripted tests, **not playtesting**. No real-browser session was run.

## 4. Ground rules (carry these into every change)

1. **Authority.** Core 3.3 decides what happens. Agency proposes; presentation narrates only committed results. Source order: actual repository, then verified records, then established canon, then `IRGS_Unified_Master_Codex_Instruction_v1_4_CMRR.md`.
2. **Lines.** **3.3.C** is the engine; **3.3.E** is Emergent's website/app line. The `E` archive's own `backend/engine.py` is a separate lightweight kernel and is **not** an adapter to this Core. Do not assume integration; inspect imports and mutations.
3. **Preserve saves and the previous release.** Any migration must be explicit and reviewable. Old saves must not gain invented opening events or grants.
4. **No fabricated values.** Missing skills, resources, durations, populations, prices and map geometry stay unknown. No fixed action length is adopted.
5. **No destructive IP protection.** Hash verification only; no wipes, traps or telemetry.
6. **AI narration cannot** change inventory, injure, award qualifications, advance the calendar, create obligations, reveal hidden information, rewrite history or repeat committed effects. A structured non-AI fallback is mandatory.
7. **Never hand-edit `release.json`.** See section 7.

## 5. Where the code hooks in (verified in this tree)

| Concern | Location |
|---|---|
| Declarations stored verbatim, status `declared_not_resolved` | `IRGS_Web/server.py` → `Store.gameplay_request` (idempotent receipts under `record['gameplay_requests']`) |
| Capability flags `action_resolution`, `narrator`, `time_advance` (all **False**) | `IRGS_Web/gameplay_views.py` (about line 179) |
| Player-safe projection / opening | `gameplay_views.playthrough`, `opening_scene.py` |
| Core operations the engine can already commit | `CoreWorld` (`runtime/core_world.py`): includes `military_issue_equipment`, `roman_begin_delegated_activity`, `record_delegation`, `transfer_stock`, `commit_activity`, `set_scene`, `record_evidence`, `receive_evidence` |
| Why the existing resolve will not approve a player action | `runtime/r9_runtime.py`: a player action needs a **new specialist event**, not automatic approval |
| Registry, role filtering, library, creation guard | `IRGS_Web/features.py` (`feature_registry`, `content_library`, `validate_player_creation`) |

## 6. Outstanding content, in build order

### Already present in 3.3.2 (do not rebuild)
Content Library with The Hundred Years' War (37 entries, 10 featured, one developed 1415 start); server-side creation guard and role-filtered feature registry; actor-known opening built through the player permission projection (no setup facts); withdrawal-aware opening status; origin/family/career drafts as received testimony; read-only historical comparison; recoverable Trash.

### Blocker: first action is recorded, never resolved
A first action ending at `declared_not_resolved` is **not** a passing gameplay demonstration (audit C-03). Build it through the C2 packets. The authoritative text is in `IRGS-3.3.C-Engine-Design-C2.zip` (`IMPLEMENTATION_PACKETS.md`, `HANDOFF_STATE.json`, 121 acceptance cases). Summary only; read the packet text before coding.

| Packet | Scope | Gate (from the handoff) |
|---|---|---|
| PKT-00 | Source/authority audit | Done: Web and Core must be siblings, and the catalog must be at `IRGS_3_3/catalog/` |
| PKT-01 | Durable consequential action: immutable request, attempt and outcome around existing `CoreWorld` operations; first bounded effects are Military equipment issue and Roman delegated booking; durable acceptance, retry, restore, pending work | A01–A22 and PR-01–PR-16 pass where applicable; both real receiving profiles execute the effects; no duplicate transfer, authority bypass, false work completion or stale restore overwrite. **Does not** establish freeform gameplay. |
| PKT-02 | Explicit time and staged processes | TP-01–TP-18 |
| PKT-03 | Movement, observation and search | MO-01–MO-18 |
| PKT-04 | Dialogue and social action (utterance, receipt, response, agreement kept distinct) | DS-01–DS-18 |
| PKT-05 | Integrated synthetic playable cycle (`fixtures/PLAYABLE_CYCLE.json`) | IC-01–IC-12 |
| PKT-06 | Autonomous institutions on shared records | the 17 agency/time cases plus the shared-world fixture |

**First usable gameplay gate (C2):** at least one ordinary player interaction changes the world or legitimately received information, survives reload and retry, and is presented from its committed result; the report names exactly which action families work. Only then flip the matching capability flags, and only for what is actually implemented.

**Do not** add an unrestricted stock-transfer endpoint or arbitrary world-patch route because a low-level handler accepts an authority string.

### Then, in this order (each needs fresh verification against 3.3.2 before starting)
1. **Living Day vertical slice** (v1.4 §20): an isolated test branch or transparently synthetic fixture (A Scot's Tale is a test entry, not an active campaign), one controlled character, at least three autonomous NPCs, multiple locations, work, resource use, social interaction, time advancement, NPC scheduling, Chronicle recording, save/reload and continued play, through general Core interfaces, not an AST-specific script. Do not modify canonical AST history.
2. **Narration/AI runner seam:** a provider-neutral adapter that proposes; Core validates and commits; a deterministic non-AI fallback. Test fixtures must be labelled as such.
3. **Remaining 36 historical entries:** sourced snapshots one at a time; catalogue entries stay "proposed" until their snapshot and initializer exist.
4. **World workspaces and Chronicle depth, Life-Path depth, conditional historical event plans** (opt-in and audited; never forced future history).
5. **Six-Director AI network, Workshop, Marketplace:** later stages. Solo-exchange and licence enforcement remain deferred.

Items 3–5 were identified in the audit of earlier snapshots. I confirmed only what is listed under "Already present" against 3.3.2, so recheck each before treating it as open.

## 7. Per-change workflow and rebuilding the release

1. Work in a copy; keep saves backed up.
2. Write failing tests first for each acceptance case; run the commands in section 3.
3. **Web-only change:** the host files are pinned in `release.json` (`host_sha256`). Do not edit it by hand; regenerate it with `build_release_3_3.py` in your live workspace.
4. **Runtime change:** `code_identity()` changes, so the R9 certification matrix (`results/r9_certification_matrix.json`) must be regenerated for the new code. Old certification counts are not evidence for new code.
5. **`build_release_3_3.py` cannot fully run in a clean extraction.** It requires passing result logs in `results/`, the `*_save_preservation_before.json` records, and **your real saves** under `IRGS_Web/saves` (or `trash`) to prove preservation. Run it in your live workspace, then `package_release.py` (it excludes saves) and re-verify.
6. Report design, implementation, automated verification, deployment, calibration and playtesting **separately**.

## 8. Required return evidence (from the C2 handoff)

Exact source revision and code/binding hashes; request and outcome schemas; owner/reuse mapping; migration or compatibility policy; named acceptance results; actual access traces; unresolved cases; recorded before/after examples for a successful effect, a rejected prerequisite, an allocation conflict, crash recovery and presentation failure; regenerated integrity evidence; residual blockers and a CMRR resubmission.

## 9. Known limits of this delivery

- Verified only by scripted tests on a Linux sandbox. The Windows launcher, a real browser and long-form play were **not** exercised.
- I compared the `E` copy of the Codex tree; I did not byte-compare it against the `live/` folder in `C.1`'s `IRGS Core + Web.zip`. Both carry 57 runtime files.
- No gameplay mechanics were added in 3.3.3; it is a re-hash, packaging and instruction deliverable.
- My earlier Stage-1 patches (v1 to v3) are not part of this release; 3.3.2 supersedes them.
