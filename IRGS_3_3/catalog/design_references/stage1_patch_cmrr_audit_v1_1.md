# IRGS — Core 3.3, Stage-One and Content Library: Full CMRR Audit

**Audit submission:** v1.1 (proposed reconciliation, not adoption)  
**Basis:** Four user-supplied artifacts and their nested Stage-One patch, inspected in isolated copies.  
**Method:** Compare → Merge → Reconcile → Resubmit (CMRR).  
**Authority:** The explicit October 2026 v1.0 master requirements override older README descriptions where they differ. Existing adopted simulation mechanisms remain authoritative within their proper scope.  
**Important limitation:** This is an audit of the uploaded ZIP snapshots and instruction file, **not of an undisclosed current Git working tree or the user's live Windows process**. No deployment, migration or production website modification occurred in this audit.

## 1. Executive findings

The material provides a real local Core 3.3 runtime and web server, not merely design prose. The standalone Content Library patch and the newer Stage-One patch are **two overlapping change sets**. The Stage-One patch includes the library patch's `features.py`, HTML changes and associated tests, and adds `opening_scene.py` plus opening-state integration. **Apply the latest Stage-One patch as the candidate overlay rather than independently stacking patches without conflict review.** Do not assume either patch is installed in the user's actual working directory.

**What is demonstrably functional within the limits of the uploaded code:** Core event/state mechanisms, local save handling, read-filtered player projections, creator-only actions, reviewed character selection, partial 1415 historical setup, 37-date historical catalogue, HTTP transport, resumable declaration recording, recoverable trash, release integrity checks, a one-card Content Library listing, and a persistent *textual* first-scene record. Existing tests pass when patches are evaluated independently.

**What is not yet demonstrably playable as v1.0 requires:** After reading the opening and submitting a declaration, the normal game path records `declared_not_resolved` rather than a validated consequence, autonomous NPC response and narration. Core's general simulation capabilities are not wired into a complete live player action adjudicator. There is also no completed six-Director AI runtime, no full family/economic Life-Path creator, no general world-time advance, and no developed date-specific starts beyond the supplied 1415 snapshot.

**Two significant new integration defects not caught by the bundled tests:** (1) Content Library `Start new playthrough` ignores the clicked entry ID and opens the generic wizard, where AST is selected by default; (2) the legacy New Campaign dropdown continues to list AST, Military, Roman, Fantasy and other technical or scenario profile selections independently of the one-approved-campaign discovery rule. The catalogue itself is one-card compliant, but the complete launch flow is not yet normalized to it.

**Information and security caveat:** The Stage-One opening inserts an historical **setup-reference** political fact into a player-visible `world_hook`, notwithstanding its `knowledge_scope: historical_setup_reference`. Date-valid historical truth is not by itself an observed or received fact for a character. The feature endpoint also publishes the full development feature registry to unprivileged website requests and the frontend does not filter `availableTo`; there is currently no privileged metadata payload demonstrated in that list, but this violates the intended authorization design for later admin/creator features.

## 2. Inspected sources, provenance and immutable input inventory

| Supplied input | Actual contained material | Interpretation |
|---|---|---|
| `IRGS_Core_3_3_Live(2).zip` | 257 archived files; `IRGS_3_3` Core runtime, six genre bindings, eight technical content libraries, seven existing profile registrations, local `IRGS_Web` server, scripts, tests, HYW historical data and release manifest | **Base snapshot** for evaluation; current user installation not verified |
| `IRGS_Content_Library_Patch_v1.zip` | Eight replacement/additional paths: `IRGS_Web/features.py`, server, frontend HTML/JS, two test changes, release builder and release metadata | **Independent patch set**; largely a subset of Stage-One v2 |
| `files.zip` | Nested `IRGS_Stage1_Patch_v2.zip` plus `opening_first_action_trace.json`; nested ZIP contains 12 replacements/additions | **Later candidate patch** with Content Library and opening-scene additions |
| `IRGS_Unified_Master_Codex_Instructions_v1_0(1).md` | 7,944-line integrated development directive including previous four full source volumes | **Requirements reference**; not proof of implemented mechanics |

Exact SHA-256 hashes and sizes are recorded in companion `IRGS_CMRR_Evidence_Manifest_v1_1.json`. The original ZIPs and Markdown were not modified. Patch-test environments are disposable copies beneath `irgs_audit_workspace/`.

### Patch-file comparison

| File | Content Library v1 | Stage-One v2 | Merge/disposition |
|---|---|---|---|
| `IRGS_Web/features.py` | New campaign listing/feature registry | Identical source | **One owner**; retain later equivalent |
| `IRGS_Web/server.py` | New GET endpoints for registry/library | Same endpoints plus opening init hook | Prefer Stage-One and reconcile with live diffs |
| `IRGS_Web/static/index.html` | Content Library navigation mount | Identical | Retain once |
| `IRGS_Web/static/app.js` | Campaign listing, planned feature shells and nav | Same plus first-action prompt | Stage-One supersedes library patch variant |
| `IRGS_Web/static/style.css` | No replacement | Opening record styling | Stage-One addition |
| `IRGS_Web/gameplay_views.py` | No replacement | Player-visible opening/chronicle projection | Stage-One addition; repair knowledge semantics |
| `IRGS_Web/opening_scene.py` | Not present | New deterministic opening/presentation | Retain as interim authored opening, refine or replace on owned interface |
| `IRGS_Web/tests/test_content_library.py` | New tests | Identical | Retain once, expand |
| `IRGS_Web/tests/test_gameplay_ui.js` | Added frontend checks | Identical | Retain once, expand |
| `IRGS_Web/tests/test_opening_scene.py` | Not present | New HTTP first-action tests | Retain and extend to real resolution |
| `IRGS_3_3/build_release_3_3.py` | Includes features module | Includes features + opening module | Stage-One build manifest supersedes |
| `IRGS_3_3/release.json` | Rehashed for library changes | Rehashed for Stage-One changes | Use manifest matching **exact assembled code**, not arbitrary older manifest |

**Do not concatenate the two `server.py` files, or install the library manifest over the Stage-One code.** Both patch ZIPs were tested independently against clean copies of the supplied base. A real repository must be compared again before application.

## 3. Test evidence (scripted testing, not playtesting)

| Candidate | Python HTTP tests | JavaScript UI harness | Source of execution |
|---|---|---|---|
| Supplied unmodified base Web | **81 run; seven skipped; 74 completed without failure** | **20 synthetic checks passed** | `python -m unittest discover -s tests -q` in `IRGS_Web`; `node IRGS_Web/tests/test_gameplay_ui.js` from suite root |
| Base + Content Library v1 | **88 run; seven skipped; 81 completed without failure** | **21 synthetic checks passed** | Same commands on separate overlay |
| Base + Stage-One v2 | **92 run; seven skipped; 85 completed without failure** | **21 synthetic checks passed** | Same commands on separate overlay |
| Base Core 3.3 | **362 run; one skipped; 361 completed without failure** | Not applicable | `python -m unittest discover -p 'test_*.py' -q` in Core runtime |
| Release hash verification | **Passed** for base, library overlay and Stage-One overlay | Not applicable | Called `verify_release()` against each matching release manifest |

Additional Core subset: 29 selected historical/setup/integrity tests passed. HTTP tests exercised a real temporary local HTTP server with temporary saves; frontend tests used synthetic DOM/transport fixtures. **No manual browser UI session and no actual long-form playtest were performed.** The provided `opening_first_action_trace.json` records `first_action.result = declared_not_resolved`; it is not a record of resolved gameplay.

### What these tests do not establish

Passing suites do not verify that every v1.0-required feature tab exists, that the 1415 start button chooses the correct historical entry, that a true NPC interaction plays out, that an action acquires consequences, or that the historical information boundary is correct. Add explicit failing tests for these before marking the vertical slice complete.

## 4. Detailed status by component

| Domain | Verified implemented | Missing, partial or deferred | Status distinction |
|---|---|---|---|
| Shared Core 3.3 | Core event/state transactions, temporal/ownership/ledger frameworks, genre bindings, receiver tests and local persistence | Not all domain numerical models are certified for complete freeform gameplay; v1.0 integration is incomplete | **Implemented foundation; incomplete player-game integration** |
| Local website | HTTP host, Solo and Creator views, save creation/retry, selected actor projection, declarations, Chronicle, recoverable Trash | Cross-domain administrative workspace and full navigation not built | **Partially implemented** |
| Player Content Library | Stage-One patch provides `/api/content-library` with exactly **The Hundred Years' War**; engines excluded from that response | UI selected start loses entry ID; existing new-campaign selector bypasses catalogue policy | **Functional catalogue endpoint; launch integration defective** |
| Genre/content registry | Existing six genre engines and eight technical libraries remain installed | Must remain separate from campaign discovery | **Retain as backend infrastructure** |
| Historical entry catalogue | Three broad historical phase groups, **37 dated entries**, **10 featured years** | **Only 1415** has a developed dated snapshot; other 36 inspectable but not launchable | **One implemented start; remaining proposed** |
| Historical chronology | Historical cutoff and sourced 1415 reference; current divergent state survives | No conditional historic future event-plan interpreter, dependency assessment or dated event scheduler found | **v1.0 requirement not implemented** |
| Historical date integrity | 1415 supplied opening **11 Aug 1415, Julian**, before departure; exact hour unknown | AST recruitment-yard-specific date/checkpoint not integrated into HYW subscenario | **Preserve distinction** |
| Character selection | Existing/new character; explicit selected control; freeform background testimony | Seven-stage Life-Path, parents/siblings/household economic and skill reconciliation not realized | **Minimal creator only** |
| Nationality/service/mercenaries | Core supports distinct actor and organization/obligation interfaces; user background can be entered | Dedicated nationality/legal status controls, cross-national recruitment UI, actual contracts and company service not complete | **Architectural prerequisites, not completed feature** |
| Opening scene | Stage-One patch commits/presents an idempotent factual text opening in the same save; first action can be entered | No scene-specific valid nearby NPC hook, no actual first-turn adjudication or consequence; public setup-reference facts leak | **Partial, not v1.0 complete** |
| NPC autonomy/narration | Core/specialist design references and existing Core event mechanisms | No general natural-language adjudicator, automated NPC dialogue/narrator live gameplay | **Not connected** |
| Story/World/Chronicle | Three primary views, filtered projections and a basic World inspector; Chronicle search | World Atlas map engine, Economy/Politics/Military/City/Institution subworkspaces and civilization dashboard largely absent | **Viewer foundation only** |
| Six-Director AI | Comprehensive design specification | No functioning six-category Director registry/provider gateway/broker/graph runtime demonstrated in uploaded source | **Planned** |
| Feature registry | 11 registered nodes, development and release flags, honest planned shells | v1.0 inventory has many more required child sections; only parent children are displayed as rows, not routable tabs; role filter missing, history/deep routes incomplete | **Scaffold, not complete v1.0 navigation** |
| Workshop/Marketplace | Core design and placeholder navigation | No commerce/authoring product runtime in patch | **Deferred per roadmap** |
| Universal solo points | Planned account child entry; no transactions | Exchange rates, wallet, purchases and multiplayer safeguards intentionally undecided | **Correctly deferred** |
| IP/licence protection | Non-destructive policy and planned navigation shells | No trusted hosted licence service or signed official distribution implemented | **Correctly planned** |

## 5. Material inconsistencies and required fixes

### C-01 — Campaign catalogue vs actual New Campaign selector (HIGH)

**Evidence:** `IRGS_Web/features.py::content_library` lists one HYW campaign. `IRGS_Web/static/app.js::loadProfiles` still loads non-HYW campaign profiles and defaults to AST, exposing Military/Roman/etc. as new-game choices outside the catalogue. **Required:** Route all ordinary player-facing new playthrough creation through the verified HYW campaign listing and eligible child entry/scenario; retain legacy technical profiles for internal creator tools and existing saves. Never delete those packages.

### C-02 — Clicked historical entry not propagated (HIGH)

**Evidence:** `IRGS_Web/static/app.js::renderContentLibrary` binds every `data-start-entry` button to `openCreateDialog()` without an entry argument; `openCreateDialog` resets wizard state; `loadProfiles` selects AST by default. **Required:** Preserve the exact selected HYW entry (including the verified snapshot hash), preselect the HYW profile, populate the correct period/scenario and present it in review. Reject stale/mismatched selection. Cover with an end-to-end click-through UI test, not only markup assertions.

### C-03 — No Core-resolved first action (BLOCKER for Stage One)

**Evidence:** `IRGS_Web/gameplay_views.py` returns `action_resolution:false`, `narrator:false`, `time_advance:false`; supplied first-action trace reports `declared_not_resolved`; README confirms this limitation. **Required:** Connect action parsing/validation to existing Core procedures, NPC autonomous response and grounded narration, with one event transaction, outcome/provenance, subsequent player decision and exact-once reload. Never invent missing skill or resources.

### C-04 — Opening describes reference-only history as character knowledge (HIGH)

**Evidence:** `IRGS_Web/opening_scene.py` imports `snapshot['domains']['political'][0]` into a player-visible `world_hook` labelled `Known at this date`. In `IRGS_3_3/data/hyw_1415_opening.json`, that fact's `knowledge_scope` is explicitly `historical_setup_reference`, not personal character knowledge. **Required:** Separate creator setup references from PC-perceivable local facts and legitimately transmitted rumours/news. The opening may show public and visible context only after deriving a permitted knowledge projection; otherwise use a neutral sensory description from real scene records. A politically true fact is not automatically known to a character.

### C-05 — Opening is not yet a scene interaction (HIGH)

**Evidence:** Opening blocks consist of an entry-date guide, character name, political background fact and instruction to type; no grounded present NPC/action trigger or result. **Required:** Resolve an actual short beginning (e.g. recruitment yard, market, household, natural philosopher's workspace) from the real selected start checkpoint, then stop at a meaningful voluntary decision. A narrated NPC utterance requires real actor/location and Core-originating event where consequential. Do not invent AST's later sponsorship or force military service.

### C-06 — Historical future policy mismatch (HIGH design ownership)

**Evidence:** `IRGS_3_3/README.md`, `SUITE_RELEASE.md` and `historical_campaigns.apply_opening` document no automatic future history; v1.0 explicitly requires **conditional source-backed historical event plans** with causal prerequisites, not rigid future scripting. **Required:** Reconcile with Historical Foundation: implement an opt-in, audited plan registry/evaluator when dependencies and authoritative actor/state records exist. Do not change old saves, schedule Agincourt immediately, or claim implemented future policy. Until then show limitation honestly.

### C-07 — Navigation coverage and deep linking incomplete (MEDIUM/HIGH)

**Evidence:** `features.py` defines 11 items versus the complete v1.0 inventory; child features are only descriptive list rows; `app.js` lacks a `hashchange`/`popstate` handler and current route selection does not support full nested deep links; no actual six World workspace routes. **Required:** Expand one centralized registry using the v1.0 minimum inventory, make all planned sections addressable, support refresh/back/mobile/accessibility, preserve functioning routes and safe feature flags. Building planned tabs does **not** turn on unapproved mechanics.

### C-08 — Feature-role enforcement missing (HIGH before public/multiuser deployment)

**Evidence:** `/api/features?stage=development` returns the same whole registry without checking caller role; frontend code does not enforce `availableTo`. **Required:** Authorize actor/account/developer scope on the server, return only permissible navigation metadata, separately enforce every protected underlying endpoint, and disallow unprivileged stage escalation. Current loopback-only owner's environment does not by itself demonstrate multi-account security.

### C-09 — AST and HYW scenario hierarchy (MEDIUM)

**Evidence:** AST remains a separate legacy campaign profile. The HYW 1415 `individual` scenario initializes 11 August before departure, while AST uses an established later/post-Day-2 personal state. **Required:** Make AST an HYW child scenario *in the player Content Library* only after verifying its exact start date, authoritative character/checkpoint and compatible source edition. Preserve existing AST saves/profile IDs, provide aliases/mapping if needed; do not silently rewrite AST history or create false 11 August recruitment location.

### C-10 — Life-Path and non-faction careers (MEDIUM, foundational)

**Evidence:** Starting wizard records name/species/background text and eligible selected actors. The adopted detailed design requires parents, siblings, household wealth vs ownership, learning histories, relationship NPCs, nationality and optional service contracts. **Required:** Incremental core-backed life-path initialization with draft-only records until atomic commit and no mandatory faction. Do not assume funds or competence from text background.

### C-11 — World workspaces not fully implemented (MEDIUM)

**Evidence:** `renderWorld` renders four sections (resources, institutions, projects, places) and disabled time advance; the v1.0 spec includes six World workspaces plus Civilization Overview. **Required:** Implement navigation and honest read-only subview shells first, then populate from validated Core projections; do not invent map geometry, troop totals or market values. Cross-domain asset IDs must deduplicate.

### C-12 — Genre patch vs build manifest and version reconciliation (HIGH operational)

**Evidence:** Library and Stage-One patch ZIPs modify overlapping server/front-end and `release.json` and rebuild script. They are not incrementally distinct migration scripts. **Required:** Prefer candidate Stage-One v2 as the composite, re-diff against current working tree, preserve unknown user changes, back up saves, regenerate integrity manifest from final files and run verification. Do not use library-patch release manifest with Stage-One code.

### C-13 — Opening status semantics (MEDIUM)

**Evidence:** `opening_view` considers any recorded player action for the selected actor a `first_action_declared` signal and derives display status from the journal rather than a persisted structured opening-phase transition. **Required:** Reconcile with transaction IDs, first valid declaration, withdrawal and resolution events; status must be stable under retries, branching and resumption. Avoid storing a second incompatible world clock.

### C-14 — Existing service and security boundaries (RETAIN)

**Evidence:** Local host has creator-mode gates, session tokens, Host/Origin validation and release manifest checks. **Required:** Preserve these, do not add destructive self-destruct measures. Hosted entitlement enforcement and code signing are separate future functions requiring approval and privacy/legal review.

## 6. Source-authority reconciliation matrix

| Requirement | Highest relevant authority | Base | Library patch | Stage-One patch | Action | Classification |
|---|---|---|---|---|---|---|
| Core transaction/state continuity | Adopted Core 3.3 | Present | Unchanged | Unchanged | Retain; do not duplicate | Established/Core |
| Sole playable HYW listing | User v1.0 | Absent (legacy selectable profiles) | Added endpoint | Preserved | Retain endpoint; unify all launch entry paths | Partly implemented |
| Technical engines absent from playable catalogue | User v1.0 | Mixed older creator/start presentation | Correct catalogue filtering | Same | Preserve engines; filter player catalogue and wizard | Partly implemented |
| Content Library before Workshop | User v1.0 | Absent | Present top-level nav | Same | Retain; repair deep routes/roles | Partly implemented |
| All planned feature tabs in dev | User v1.0 | Absent | 11-node starter registry | Same | Expand complete inventory with routed children | Scaffold |
| Family/siblings/economic Life-Path | User v0.3 design | Text background only | Unchanged | Unchanged | Add validated Core-backed drafts in stages | Proposed/not implemented |
| Scottish origin vs foreign service | User instruction | Not enforced as nationality lock | Unchanged | Unchanged | Explicit identity and relationship types, test | Required; not complete |
| Mercenaries/multi-client service | User instruction | Core obligations infrastructure | Unchanged | Unchanged | Contract/service UI + actual Core contracts | Proposed specialization |
| One developed 1415 start | Source-backed campaign data | Present | Preserved | Preserved | Retain 11 August Julian snapshot; no false substitutes | Implemented scoped |
| Ten featured dates/37 entries | v1.0 + real catalogue | Present | Nested in HYW | Same | Preserve all 37; count 10 featured, 3 period groupings | Implemented browse only |
| AST HYW child scenario | User v1.0 | AST independent legacy profile | Unchanged | Unchanged | Relocate catalogue representation after source reconciliation | Proposed integration |
| State-grounded opening | User v1.0 | No first-scene generator | None | Deterministic reference intro | Retain idempotence; add real local hook and knowledge | Partly implemented |
| First action resolution + narration | User v1.0 | Pending declaration | Same | Same | **Blocking work**; implement real Core loop | Not implemented |
| Six-Director network | User v1.0 | No actual orchestrator found | Planned tab | Same | Foundation later; thin provider path for vertical slice | Planned |
| Six World workspaces | User v1.0 | Simple World view | Unchanged | Unchanged | Real subtab routing, then data-backed viewers | Partly implemented |
| Conditional historical future | v1.0 supersedes older policy | Explicitly disabled | Unchanged | Unchanged | Historical Foundation dependency/event-plan design | Not implemented |
| Solo-point conversion | User deferred | None | Disabled planned shell | Same | Do not implement rates/wallet or redemptions | Correctly deferred |
| Anti-copy protection | v1.0 non-destructive | Local integrity checking | Planned shell | Same | Retain hashes; later signed builds/server policy | Planned |
| Legacy saves and active profiles | Core continuity | Existing data | No destructive change | No destructive change | Never delete/migrate silently | Retain |

## 7. Accounted removals, relocations and compatibility impact

**Remove from ordinary player discovery (visibility only):** Technical engine cards, technical library cards, independent AST campaign cards, placeholder/demo campaign cards, future unpublished campaign cards, and directly selectable generic genre profiles. **Do not delete their source files, profile identities, technical registries, content assets, or existing saves.** Continue to permit appropriate Creator-mode technical inspection and legacy save resume.

**Relocate:** AST presentation beneath the Hundred Years' War 1415 scenario hierarchy after date and checkpoint verification; it need not migrate its historical save identity. Internal Genre Content Libraries remain technical asset lookups; the player Content Library is a new discovery projection.

**Retain:** Core state owner; existing consistent historical snapshot; exact user text declarations; idempotent request receipts; legal scenario and control checks; read-only projections; Creator mode permissions; backups and Trash; versioned manifests.

**Deprecate only with compatibility plan:** Any legacy player launch route that bypasses the HYW allowlist. Preserve old deep links by redirecting to a correct detail/legacy save view where possible. Do not destroy existing campaign profiles simply to simplify the UI.

**No silent migration:** Files on disk were audited in copies only. If actual user files differ from the supplied baseline, abort direct overlay and perform a three-way diff or cherry-pick with recorded conflicts. Old save schemas must not acquire invented opening events or currency grants retroactively.

## 8. Stress-test priorities and calibration gaps

**Immediate regression cases:** click HYW 1415 entry from library → exact 1415 wizard/review without AST default; no legacy engine campaigns offered; a single role-filtered registry; opening uses only character-known facts; first freeform response receives exactly one actual Core outcome and new NPC/autonomy state where feasible; reload between every step; no duplicate money, actors or events; a player can refuse/leave without forced service; old AST save unchanged; a developer can inspect all planned tab shells, ordinary player cannot inspect protected admin routes.

**Edge/extreme cases:** missing historical source or NPC, inconsistent start date, multiple simultaneous creation clicks, network failures, cancelled/withdrawn first declarations, two distinct campaign branches, no faction affiliation, concurrent contracts, overlapping political claims, resource scarcity, offscreen world activity, historical event invalidation, mid-opening save, cross-workspace asset accounting, unknown map geometry, inaccessible AI provider, and long time advancement without resets.

**Undetermined:** Full historic data for other 36 entries; calibration of upbringing wealth and skills; exact AI provider choice/latency and hosting costs; valid unit population inventories; map resolution; specific contracts and military wages; future historical-plan trigger rules; anti-copy legal terms; solo exchange prices. **Do not invent missing values.**

## 9. Recommended next engineering sequence

**P0 — Safe integration and visibility:** Audit live tree against supplied hashes; use Stage-One v2 as candidate only; preserve backups and legacy saves; fix Content Library entry ID/preselection; remove legacy technical profiles from ordinary playable-start picker; enforce role/visibility safely; register all v1.0 planned child features as navigable development tabs.

**P1 — Actual playable opening-to-second-decision slice:** Reconcile correct scenario location and PC knowledge; create a locally grounded opening; expose freeform declaration; resolve through Core with actual actors, resources, time and NPC reactions; narrate only committed/known effects; save/reload exact once; provide deterministic fallback when AI is unavailable.

**P2 — Character/Scenario depth:** Implement Core-backed family/household, nationality, education, childhood choices, independent/mercenary/professional service options, contracts and a legitimate HYW AST child scenario with correct start checkpoint.

**P3 — World interface:** Wire six World subviews to read-only permission-scoped Core projections and a cross-domain Civilization view; then authorized inspect/draft/submit management actions as Core supports.

**P4 — Historical conditional-plan machinery and AI director expansion:** Reconcile adopted Historical Foundation and build causal historic event plans without forcing outcomes; build six-Director AI registry/broker/provider adapter in manageable slices. Core remains authoritative.

**P5 — Workshop → Marketplace:** Preserve planned navigation now; operational commerce follows playable runtime. Keep solo currency exchange and aggressive licence enforcement deferred.

## 10. Required Codex completion evidence

The next Codex run must produce: source path/hash inventory; actual live-repository audit; a per-file merge log; resolved conflicts and accounted removals; before/after feature registry and player campaign selectors; demonstration that clicking the HYW card/1415 start opens the correct creation flow; a verified actor-local opening with *no reference-only knowledge leak*; freeform first action with a **Core-resolved event and NPC/world reaction**, and next player decision; save/reload and retry traces; test commands and results; updated release manifest verification; rollback/migration precautions; residual blockers; and a full CMRR resubmission. A first action merely recorded as `declared_not_resolved` is not a passing gameplay demonstration.

**Acceptance is not granted by this audit.** The Stage-One patch is a useful partial foundation, not yet the complete v1.0 user experience. This audit and the companion Codex v1.1 instruction are proposed for implementation review.
