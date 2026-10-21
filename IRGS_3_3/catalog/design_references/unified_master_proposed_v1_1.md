# IRGS — Unified Master Codex Instructions v1.1

**Revision:** Proposed v1.1 — CMRR-Audited Stage-One Integration Directive  
**Base specification:** Unified Master Codex Instructions v1.0 (verbatim preserved in Appendix B)  
**New evidence:** User-supplied Core 3.3 release, Content Library Patch v1, Stage-One Patch v2 (nested in `files.zip`), and scripted verification results  
**Status:** Design/integration instruction, **not adopted implementation**, historical verification, calibration or actual playtesting.  
**Priority:** One functioning, persistent Hundred Years' War game and complete honest developer navigation **before Workshop and Marketplace**.

> **Codex execution order:** Read this v1.1 reconciliation first; review the full attached CMRR audit and intact v1.0 source below. Inspect the *actual current repository* and compare it to the uploaded base and candidate patches before changing code. Preserve saves, old profiles, genre engines, content libraries and valid Core mechanisms. Reuse the nested **Stage-One Patch v2** as the preferred *candidate* because it already includes Content Library v1 changes; do **not** overwrite the live tree blindly or apply both patch manifests as though independent. Deliver a real, Core-resolved first interaction and one-campaign Content Library launch flow. Make all planned features navigable in development, truthfully disabled as needed. Do not implement destructive anti-copy code or deferred solo wallet operations.

## PART A — Audited authority, current-state evidence, and critical corrections

### A.1 Authority and provenance

Current explicit user decisions govern the Content Library ordering, the sole-HYW playable list, all planned developer tabs, independence of nationality/faction service, civilian and mercenary careers, the post-character-creation interactive opening, and the strictly solo-only **deferred** cross-campaign points concept. Adopted Core 3.3 owns actors, time, events, knowledge, ownership, institutions, economy, resources, contracts and military systems. The Historical Foundation handles researched starting snapshots and eventual **conditional** source-backed future plans. Genre/setting libraries supply specialized content. Campaign profiles select enabled mechanics and start conditions. Campaign State owns each playthrough's actual divergence. The website owns filtered presentations, navigation, drafts and explicit submission. AI orchestrates/proposes/narrates but cannot commit world state.

The uploaded Core 3.3 base is a **snapshot**, not necessarily the user's current working directory. The audit's separate overlay tests pass; passing tests do not prove a deployed build or complete gameplay. Refer to Appendix A for detailed evidence and patch-file accounting.

### A.2 Verified status — do not misreport

| Component | Verified in supplied code/overlay | Stage-One gap |
|---|---|---|
| Core runtime | 362 tests run (one skipped, 361 completed without failure); signed-by-hash *release integrity manifest*, replay/ledger services | Not end-to-end natural language action adjudication |
| Base local website | 81 HTTP tests run (seven skipped, 74 completed without failure); 20 synthetic UI checks; save/reload/declarations | No general narrator, full game loop or automatic time advancement |
| Content Library patch | 88 HTTP tests run (seven skipped, 81 completed without failure); 21 UI checks; one-card HYW endpoint | Clicked date not propagated; legacy wizard shows non-HYW profiles |
| Composite Stage-One patch | 92 HTTP tests run (seven skipped, 85 completed without failure); 21 UI checks; idempotent persisted deterministic intro | First action still `declared_not_resolved`, not Core-adjudicated; hook uses reference-only history |
| Historic HYW data | 37 dated catalogue entries, ten featured years, three broad period groups; 1415 developed start | Other 36 dates remain proposed; HYW AST recruitment-yard date/checkpoint not fully integrated |
| Feature navigation | 11-node registry with planned shells and release flags | v1.0 full feature inventory not routable, role gating missing |
| Six-Director AI, Workshop/Marketplace, universal solo points | Described/planned | Do not claim operational; exchange must stay disabled |

The actual opened and tested Core/Web overlay **must be compared again** with the live repository. If tests fail on the live tree, report the exact blocker rather than claiming the supplied suite's test results still apply.

### A.3 Critical corrections that supersede older developer guesses

1. **Sole player campaign entry:** The visible player-facing Content Library and **every ordinary new-game launch path** must offer only the approved Grand Campaign, **The Hundred Years' War**, with its actual valid starting periods and scenarios nested beneath it. Internal AST, Military, Roman, Fantasy, Shinobi, Space and Post-Apocalyptic profile registrations remain technically installed and available to legitimate internal consumers and legacy saves; they are not additional ordinary playable campaigns.
2. **Preserve exact selected entry:** Fix the actual Stage-One `renderContentLibrary` click handler; it currently ignores `data-start-entry` and enters a wizard defaulting to AST. Capture the entry ID, choose the HYW campaign explicitly, load and validate its snapshot/hash, preselect the clicked entry, and show the exact selection in final review. No silent fallback to AST or a nearby date.
3. **Correct historical grouping:** The current data holds *three broad period groupings*, *37 catalogue entries* and *ten featured years*. Do not manufacture ten backend period objects merely because ten curated years appear in UI; represent existing taxonomy accurately.
4. **Opening source discipline:** A `knowledge_scope: historical_setup_reference` political fact cannot be shown as a PC-known opening hook merely because it is historically true. Scene text must be derived from authorized actor-local observations, available NPCs, scenario-authored playable beats and legitimately delivered reports. Historical creator briefings and future planned events stay restricted.
5. **True gameplay required:** An opening with a textbox followed by a permanent `declared_not_resolved` record is *partial* first-scene work, not a complete playable first interaction. Next immediate objective is the full Core-adjudicated player action, autonomous response, second decision point and exact-once persistence.
6. **Never overwrite working saves/profiles:** Treat patches as source overlays, not migrations. Verify current file hashes, three-way merge if necessary, and regenerate release hashes only after final reconciliation. Legacy saves, Creator tooling and technical libraries survive unchanged.
7. **Permissioned feature discovery:** A `stage=development` query or modified browser flag must not reveal privileged admin/creator data or grant actions. Implement a backend-authorized feature registry and deep-route guards. Current local loopback owner restrictions are not sufficient evidence of public multiuser authorization.
8. **Historical future:** Older README statements that no future events are scheduled describe current *implemented limitations*. v1.0's **conditional historical future** remains intended and must be reconciled with source-backed prerequisites; do not silently enable automatic outcomes or retroactively rewrite existing campaigns.
9. **AST launch hierarchy:** Only after date/checkpoint verification, present A Scot's Tale as a **Hundred Years' War 1415 starting scenario**, not a second player-facing campaign. Preserve its independent legacy profile ID and actual post-Day-2 history in existing saves. Do not assert the 11 August pre-departure snapshot is the AST recruitment yard.
10. **Solo and IP futures:** Provide disabled/clear planned tabs for account-level solo currency conversion and non-destructive licence/build provenance. Do not invent wallet balances, rates, stat boosts, equipment offers, account restrictions or self-wipe measures.

## PART B — Required Stage-One implementation order

### B.1 Phase 0: Audit and safe overlay integration

- Inventory actual repository tree, Git status where available, hash/release files, launcher, test runner, local saves and current changes.
- Inventory the four supplied inputs by hash and nested Stage-One patch inventory; use `IRGS_CMRR_Evidence_Manifest_v1_1.json` for provenance if available.
- Compare live `IRGS_Web/server.py`, `static/app.js`, `static/index.html`, `gameplay_views.py`, `static/style.css`, `IRGS_3_3/build_release_3_3.py`, `release.json` and tests against clean Core 3.3, Content Library v1 and Stage-One v2. New `features.py` and `opening_scene.py` must each have one authoritative implementation.
- Preserve/make backups of user saves. Do not delete modules, move existing campaign chronology, or break Creator mode.
- Merge conservatively with conflicts identified. Do not copy an old `release.json` over altered code. Rebuild integrity metadata for final assembled code and verify. Re-run tests and separately identify changed or skipped tests.

### B.2 Phase 1: One-campaign Content Library + complete planned navigation

- Deliver a real, player-facing **Content Library** before Workshop in main navigation, with precisely one eligible campaign card, **The Hundred Years' War**, and direct drilldown to its dates/scenarios.
- Make all ordinary player “New Campaign”, dashboard shortcuts and campaign selectors enter that same validated registry flow. Do not expose installed Genre Engines as games; do not remove profile/package source or old saved-game access.
- Fix clicked-entry selection and preselection, with read-only previews and `canLaunch` tied to actual backend readiness. The supplied data supports only the **11 August 1415 Julian historical setup** at present, not 36 invented alternatives.
- Build the **entire v1.0 feature inventory as routable parent/child developer-visible tabs** (Story/World/Chronicle, Character/Life-Path, World six workspaces, institutions, AI Network, Workshop, Marketplace, Account, deferred solo exchange, admin/IP). Reuse existing working pages and URL conventions rather than duplicating them. Every unfinished feature must show status, scope, dependency and truthful absence of backend data; no fake operational controls.
- Implement a single navigation registry, role/authorization filtering, correct preview/release visibility, deep linking, browser history and mobile/accessibility behavior. Admin/debug/historical-future data is server restricted, not hidden by CSS alone.

### B.3 Phase 2: Character-to-opening and first Core-resolved decision

1. Content Library → HYW → exact verified entry → valid scenario/control perspective → identity and starting information → validation → atomic creation.
2. Establish initial actor, valid location, starting time precision, family/household/employment and known information **only when documented or successfully authored/validated**. Creating new background prose cannot automatically confer wealth, literacy, rank, faction or equipment.
3. Generate a short, **perceptible local opening** from the created playthrough. The optional scenario-specific hook may involve a real NPC with an actual compatible location/knowledge/intent, local work, a received message or a valid environmental occurrence. The opening should **play out briefly then stop for the player's reaction**; no unrequested PC speech/action, military oath, purchases, movement or assumed emotion.
4. If an NPC speaks or something physical happens, record it once through the appropriate Core-owned event system when the occurrence is mechanically consequential. Descriptive text alone does not commit a world event. Do not invent NPCs/supplies just to provide drama.
5. Make the freeform composer accept voluntary speech, action or observation. Use the Core sequence: Declaration → Feasibility → Execution/Uncertainty → Effect → Exposure/Reaction → State Update → Player Control.
6. Use existing actual Core capabilities; implement only the smallest missing adjudication/adapter mechanism required. AI or a deterministic approved test provider can parse/propose/narrate, but **cannot write arbitrary new state**. Qualified routine actions succeed when feasible without gratuitous rolls. Impossible effects never arise through dice or narration.
7. Persist one action request, state changes, NPC responses, report visibility and narrated presentation; return an actual result and next control point. A retry, reload, double-click, branch or failure must not create another save, event, soldier, item, payment, historical event or NPC response. Differentiate action acceptance, pending processing, physical completion and mere intent.
8. If source-local information is inadequate, report unknown/blocked status or use a **non-fabricated neutral opening**. If the Core cannot resolve an action, report the blocker honestly; do not label that result full gameplay.
9. Cover an HYW 1415 new civilian, independent mercenary, scholarly route, eligible existing historical actor and AST-specific scenario **only where opening data exists and exact chronology is correct**. Ordinary civilian and independent careers must never be funnelled into English/French military allegiance.
10. Demonstrate creation → opening → meaningful player reply/refusal/unlisted act → verified Core event and autonomous response → next decision → exact-once save/reload. Capturing text alone is insufficient.

### B.4 Phase 3: Life-Path and institutional service compatibility

- Reconcile the proposed v0.3 Life-Path: family/guardians/siblings with persistent actor IDs, household economic position/ownership, childhood obligations, education/skill time, formative choices, mentors/bonds, adolescence/adult careers and final biography review.
- Keep birthplace, national origin, culture, legal status, residence, allegiance, **service contract** and player-control scope separate; do not lock a Scot out of English service or force one permanent faction.
- Preserve independent, mercenary, commercial, scientific, civilian, military, freelance and multi-client options. Seeking a patron, job or military service is **not** acceptance.
- Integrate authoring drafts atomically, respecting historical actors/date and no phantom stock/skills. Preserve existing saves without unauthorized migration.

### B.5 Phase 4: World, historical conditional plans, and multi-AI foundation

- Present Atlas, Economy, Politics, Military, Settlements, Institutions and Civilization overview as linked projections of one state. Implement actual data-backed navigation before rich maps; no fabricated coordinates, political ownership, economic figures or units.
- Respect actor knowledge, conflicting territorial claims vs effective control, assets vs access, reports vs stocks, and routine view actions vs authorized Core commands.
- Design the Historical Foundation's conditional future event-plan registry with explicit source provenance and causal prerequisites; current disabled future scheduling is not to be silently changed or misrepresented.
- Grow the six-Director AI system (GM coordinating World/National/Regional/Local/Scene categories) with scoped instances, provider adapters, broker permissions, event coordination and a mock/live vertical-slice trace. The conventional controller maintains operation when AI coordination is unavailable; Core remains authoritative. Advanced AI work must not prevent initial functional play.

### B.6 Deferred stages

Keep the personal Workshop after the playable Content Library/game, and Marketplace after Workshop. Preserve the intended creator royalty/rights rules in intact v1.0. Register IP build/entitlement verification as a safe non-destructive future service; no self-destruct code. Keep solo-only cross-campaign points fully disabled until separate mechanics, security, calibration and explicit authorization exist.

## PART C — Acceptance cases and phase gates (must report tested vs untested)

| Priority | Case | Pass criterion |
|---|---|---|
| P0 | Single ordinary playable catalogue | One HYW card; no engine/profile/demo listings in *any* player launch path |
| P0 | Start button target | Clicking `hyw-1415` preserves that ID/hash and preselects HYW, not AST |
| P0 | Historical starting readiness | 1415 shown ready only if snapshot actually initializes; other 36 accurately disabled |
| P0 | Engine/legacy preservation | Six genre engines and eight technical content libraries preserved; existing AST saves still resume |
| P0 | Planned tab coverage | Every v1.0 parent/child planned feature has reachable dev route; role-scoped, release-hideable |
| P0 | History/deep-link behavior | Browser back/forward, direct entry, refresh, keyboard and mobile remain usable |
| P0 | Release assembly | Actual final code matches regenerated release hash manifest and launcher checks |
| P1 | Opening grounded | PC sees character-perceivable location and hook, not creator-only history |
| P1 | No forced action | Opening stops before PC voluntary speech, movement, oath, attack or purchases |
| P1 | Freeform reaction | Player may talk, refuse, ask, leave, observe or attempt another feasible action |
| P1 | First action resolved | Result contains true Core-adjudicated consequences/uncertainty, lawful NPC response and next control point |
| P1 | Retry/reload | Creation, hook event, first action and narration occur/persist exactly once |
| P1 | No unearned records | No invented resources, NPC, equipment, wages, profession, skills, citizenship or contracts |
| P1 | Absent AI provider | Valid deterministic recovery/fallback; never a fabricated Core result |
| P1 | Causal history | Future historical plans not leaked to player or rigidly enforced as fixed outcomes |
| P2 | Life-Path | Parent/sibling/mentor assets and actor references coherent; time/ownership reconcile |
| P2 | Foreign service | Scottish-origin character can seek English employment under real feasibility checks |
| P2 | Unaffiliated/mercenary | No faction mandatory; contract completion does not delete company/personnel |
| P3 | World views | Same entity/stock across subviews, one ledger, no view-induced time progression |
| P3 | AI director permissions | Six categories with valid instance scopes; AI cannot commit unauthorized state |
| Deferred | Solo points | Tabs visible in dev but wallet/exchange/redemption inactive and multiplayer blocked |
| Deferred | IP protections | No destructive self-wipe/sabotage; protect trusted online services only when policies approved |

**Do not mark Stage One complete** until its real action/result/reaction/save loop passes. Passing the current 92 HTTP tests is necessary regression evidence but insufficient for this gate.

## PART D — Mandatory CMRR report back to the user

Codex must provide: (1) a live repository audit with source paths/hashes and real installed patch state; (2) bidirectional source comparison including this v1.1 plus intact v1.0, Core 3.3, both patches and nested first-action trace; (3) conflict/duplication/reconciliation matrix and accounted removals; (4) exact source files changed with ownership and migration impact; (5) current and completed feature tab/route listing with role/lifecycle/dev/release states; (6) Content Library one-campaign proof and clicked-start end-to-end trace; (7) opening → first resolved response trace and retry/reload; (8) unit/integration/frontend/manual evidence with skipped/failed/untested made explicit; (9) release manifest verification and save preservation; (10) outstanding historical source gaps, balancing questions and deferred commerce/solo points/IP terms. **Resubmit a complete coherent version; no patches-only response, false validation, or silent loss.**

---

# APPENDIX A — Full CMRR Audit of the Four Supplied Inputs

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


---

# APPENDIX B — Unified Master Codex Instructions v1.0 (verbatim preserved)

The complete v1.0 source begins immediately below. This is archival retained specification. When wording conflicts, the higher-precedence v1.1 reconciliations above govern. Nothing below is evidence that mechanisms have already been implemented.

# IRGS — Unified Master Codex Instructions

**Consolidated engineering directive v1.0 | 19 October 2026**  
**Includes:** IRGS Master Development & Commercial Architecture v0.7; Hierarchical Multi-AI Orchestration Network Foundation v0.1; Codex Instructions Part 1 (Hundred Years’ War v0.4 and World & Civilization Interface v0.1); and the deferred Solo-Play Cross-Campaign Currency Exchange proposal.  
**Current navigation and launch requirements:** The **Content Library** is the player-facing campaign directory and must exist **before the Campaign Workshop** in navigation and delivery. **The Hundred Years’ War is the sole campaign shown in the playable catalogue in this version. Genre Engines, engine modules, and technical Content Libraries must not appear as playable campaigns.** All planned-feature tabs remain designated and routable in development and can be hidden in release. **After the player confirms character creation, the game must present a short state-grounded interactive opening and return control for the player's own first action, with exact-once persistence.**
**Protecting the work:** Document signed releases, provenance and future server-side entitlement checks. **Do not implement destructive self-wiping, file deletion, sabotage or retaliation** on suspected copying; verified unauthorized access to protected hosted services can be denied non-destructively under a separately approved policy.  
**Authority:** User-directed design and implementation instruction, subject to established/adopted IRGS Core and campaign rules in their respective scopes. **v1.0 adds the required interactive opening scene after campaign/character creation and a strictly non-destructive build-authenticity/IP protection roadmap.**  
**Status:** A consolidated **Codex instruction and design submission**, **not** evidence of acceptance of every proposal, completed implementation, financial calibration, historical verification, or playtesting.

> **Execute, don't merely summarize:** Audit the real repository, existing IRGS Core 3.3 Live implementation and currently usable website; apply CMRR (Compare → Merge → Reconcile → Resubmit). Build the next working vertical slice of an actual persistent text-based game, **including a functioning player-facing Content Library which lists only The Hundred Years’ War**, and in this same version create working navigation and honest, safe feature-page shells for all planned areas. **A successful new character creation must transition into a brief, state-grounded opening scene with a real first decision, not a blank Story view; save/reload must preserve that opening without replaying effects. Include only non-destructive provenance/licensing protections—never destructive anti-copy traps.** Genre Engines and internal content modules are infrastructure, not playable campaign entries. Preserve functioning features and save files. Avoid mock dashboards pretending to be implemented. Maintain simulation-first authority and protect player knowledge and entitlements. Full source documents reproduced after this integrated directive are mandatory details, not optional reading.

---

## I. Authority, source precedence, and how to use this file

This document is **one actionable instruction**, not four separate Codex jobs to run independently. Codex must treat the **integrated directive** as the reconciliation layer. The four **source volumes** included verbatim below retain their full detailed requirements, test cases, historical tables, and examples; when they overlap, use the specific reconciliations here and log the outcome. No source is implicitly discarded merely because a later summary omits it.

**Precedence:** (1) explicit user decisions, including the latest Content Library, sole-campaign catalogue, and planned-tab directives; (2) adopted campaign overrides; (3) adopted genre foundation; (4) adopted Shared IRGS Core; (5) provisional proposals. New proposed component names, quotas, mockups, API labels and design examples do **not** silently become adopted mechanics. Codex must verify actual implementation before asserting that a capability is missing.

**Required source inventory:** inventory and record file paths, source hashes, version labels and feature ownership for the four attached instructions, the actual project repository, accessible Core 3.3 Live archive, website/server, persistence and relevant historical data. Distinguish **implemented**, **partially implemented**, **documented**, **proposed**, **deferred**, **accepted**, **playtested** and **calibrated**. No silent code removal, user-state migration, or reinterpretation of established campaign history.

**CMRR:** Compare bidirectionally → Merge compatible material → Reconcile conflicts/duplicates by owner, authority and causality → Resubmit a complete changed implementation and specification with tests, source mapping, removals, migration impact and unresolved decisions. Tests are not playtesting, and consistency is not economic balance.

---

## II. Product and engineering priorities

**Business roadmap (binding order):**

1. **Stage One — Playable IRGS + player-facing Content Library:** Implement the Content Library **before the Campaign Workshop** as the actual campaign-discovery and launch surface. In this version it must display **exactly one campaign: The Hundred Years’ War**, with its appropriate historical starting periods and associated scenarios nested within that campaign. Existing local/mock website must support browsing this record, choosing an eligible start, independent playthrough creation, character creation/selection, AI-presented Core action resolution, clock/resources/relationships, save, reload and continuation. At minimum use a working provider or deterministic mock test path. A visible catalogue entry must never falsely claim the playthrough is operational when the required backend is missing.
2. **Stage Two — Personal Campaign Workshop:** Reusable content authoring, campaign/entry configuration, testing, authoring permissions and relevant Workshop entitlement/usage systems once the game and its player-facing Content Library work reliably. The Workshop's **engine Content Libraries / Modules** are internal authoring assets, not entries in the player-facing campaign list.
3. **Stage Three — Publication and marketplace:** Submission, commercial publishing catalogue, rights, entitlements, creator royalties and creator-consented campaign packaging only after the playable game, Content Library and usable Workshop. Future published campaigns may later be added explicitly; this does not authorize populating today's playable list with planned or technical entries.
4. **Deferred feature — Solo Cross-Campaign Exchange:** Register, allocate interface location and document prerequisites now. **Do not turn on a wallet, conversion, store, exchange rates or stat/gear rewards in this development round.**

**The first interactive scene is part of Stage One, not a later optional cinematic. Planned build-authenticity and licence inspection tabs are only shells until authorized service policies exist. New navigation requirement modifies *surface availability* but not the *feature implementation order*.** Build all **tabs and routed feature shells in Stage One**, while the underlying business operations, exchange, advanced AI agents and expensive simulation capabilities remain appropriately staged. A functional tab means its label, route, section hierarchy, location, responsive presentation and accurate state are implemented—not that its future backend mechanism has been approved. Display a clear **Planned / In Development / Available / Restricted** state; do not fabricate live totals, contracts, historical records, marketplace listings, balances, or demo outputs as if authoritative.

**Immediate Stage-One success criterion:** A new player can open the existing website; navigate to **Content Library**; see **The Hundred Years’ War as the sole listed campaign**, never an engine or content module; choose an eligible period/entry and create or select a playable character; **atomically initialize a unique playthrough and automatically see a brief playable opening scene grounded in that state**; freely react to the scene through their own dialogue or action (without compulsory menu choices); receive a Core-resolved, AI-presented result; reload without changing state **or replaying an opening NPC event**; and navigate all designated planned-feature tabs (with appropriate development-only placeholders). Do not build a beautiful storefront around a game that does not work.

---

## III. Architectural invariants and ownership

**Shared IRGS Core → Genre Foundation/Engine → Setting/Theme Module → Campaign Profile → Campaign State**.

- **Core owns:** Actors, agency, decisions/control scope, causality, time, events, knowledge, information dissemination, conditions, capability/progression interfaces, inventories, transfers and finite resources, economy, contracts, institutions, households and population, military organization, logistics, projects, continuity and history. Support extensions rather than separate redundant implementations.
- **Genre/setting owns:** Relevant specialty rules and historical/fictional technology, politics, cultural practices, equipment/abilities, maps and content; the Historical Genre Foundation owns historical-state reconstruction, research provenance and conditional event-plan interpretation.
- **Campaign configuration owns:** Enabled mechanics, period/date, starting scenario, permitted control perspective, calibrated rules/overrides, and source edition. **Campaign State** owns actual player-specific divergent world history. Two playthroughs never share mutable state.
- **AI orchestration owns:** Agent/provider routing, context assembly, permissions, task coordination and narrative proposals. **AI does not own committed world state** and may not directly grant physical outcomes.
- **Website owns:** Feature navigation, read-only permission-filtered projections, inspect/draft/submit interactions, accessibility, user feedback, clear errors and server-confirmed saved state. Client-side views are not separate ledgers.
- **Platform/account owns (future):** Entitlements, one-time purchase and usage/Rest records, creator commerce and royalty ledgers, future solo-only universal point balance. **Separate account transactions from campaign cash and from Workshop usage credits**.

Core execution remains **Declaration → Feasibility → Execution/Uncertainty → Effect → Exposure/Reaction → State Update → Player Control**. Simulate before narrating. No NPC writing/AI narration may add unvalidated state effects, invent a PC's speech/motives/purchases/movement, or make impossible actions possible through dice. Routine qualified work normally succeeds with real resource/time costs; failure must not invent unrelated catastrophes.

One authoritative clock, one source per actor/asset/quantity, debit-credit transfers and explicit transit locations, finite resources, reservation distinct from consumption, forecast distinct from stock, injury distinct from exposure, and occurrence distinct from observation/transmission/receipt. A map zoom, tab navigation, historical summary, time-scale change or AI specialist retry must not create resources or advance the clock. Autonomous offscreen activity continues. Reveal only information legitimately known to the controlled perspective; creator/debug access must remain separate and server-authorized.

---

## IV. Mandatory tab and route designation in the current version

### 4.1 Implement navigation *now* for all planned features

**User's latest direction:** The Codex is to **designate actual website tabs in this version for *all* planned features**. They may be hidden later when the public release is prepared. Treat this as a concrete frontend requirement, **not merely a roadmap note**.

Build every tab or child tab below as part of one coherent navigation system using existing framework conventions. A deep route should work directly, by refresh, through in-app navigation and on mobile. Existing implemented pages should be reused rather than duplicated. Each planned but unfinished route must show a useful, labelled, honest **feature overview / dependency / status** shell, not a blank view or broken button. Development navigation must permit the product owner to reach all planned areas; beta/release builds may hide staged sections through a centralized, reversible configuration. Creator/admin-only pages must never expose restricted records just because a developer makes a tab visible.

**Do not overload the main header with scores of unrelated tabs.** Use top-level domains, then domain subtabs, expandable categories, and contextual nested navigation. Names and URL samples below are logical targets; adapt paths to existing routes without forcing a mass migration.

### 4.2 Central feature registry contract

Implement or reconcile one **single source of navigation truth** with fields equivalent to:

```ts
interface FeatureDefinition {
  id: string;                  // Stable ID; does not change with translated display label
  label: string;
  parentId?: string;            // Nested tab/category
  route: string;                // Existing URL if already implemented
  order: number;
  area: 'public'|'player'|'gameplay'|'creator'|'admin'|'developer';
  lifecycle: 'planned'|'scaffold'|'in_development'|'functional'|'deferred';
  availableTo: string[];       // Server-authorized roles/control perspectives
  showInDevelopment: boolean;
  showInPreview: boolean;
  showInRelease: boolean;
  featureFlag?: string;
  requiredEntitlement?: string; // Future/actual entitlement; never simulate ownership
  requiredBackendCapability?: string;
  description: string;
  dependencyIds?: string[];
}
```

This is a proposed logical shape. Reuse existing router, permission/flag systems, UI component library and actual entitlements where present. Do not create a duplicate navigation authority. Runtime permission and entitlement checks must be enforced by backend/API, not only by hiding a tab. Route visibility, functionality, player control, information access and product ownership are distinct concerns.

The development view should have **Show All Planned Features** enabled in authorized development context (or another obvious equivalent). Release/preview visibility may be configured independently, without removing routes/components. If an incomplete route is called directly in release, handle it safely with intentional restricted/unavailable messaging or a guarded fallback, not unauthorized access. Maintain navigation history, deep-link stability, responsive drawer behaviour, keyboard/screen-reader semantics and consistent labels. Use no fabricated live metrics.

### 4.2a Player-facing Content Library, playable-campaign registry and initial catalogue rules (mandatory)

**This section supersedes any source or older navigation example that places Genre Engines in a playable campaign list, equates the player Content Library with engine Content Libraries, or places campaign discovery exclusively inside the future Workshop/Marketplace.** It is a current user requirement, not an optional future suggestion.

**Terminology and placement**

| Term | Purpose | Appears as a playable campaign card? |
|---|---|---|
| **Content Library** (player-facing, top-level) | Discover, inspect and launch eligible campaigns and their valid starting periods/scenarios | **Contains campaign cards** |
| **Playable Campaign** | A registered campaign product/profile with its own start configuration, presentation metadata and launch eligibility | **Yes, if explicitly included in the current playable catalogue** |
| **Sub-Campaign / Starting Period** | A dated entry inside a campaign, e.g. 1415 for The Hundred Years’ War | **No; child selection inside its parent campaign** |
| **Starting Scenario** | An opening inside a period, e.g. *A Scot's Tale* in the 1415 Hundred Years’ War profile | **No; child selection, not a separate campaign** |
| **Genre Engine / Genre Foundation** | Backend mechanics and reusable rule implementations inherited by campaigns | **Never** |
| **Technical Content Library / Module** | Reusable engine, genre, setting, equipment, template or authoring data | **Never** |
| **Campaign Workshop** | Future authoring environment for creating and configuring campaign products | **No; not the discovery/launch directory** |
| **Marketplace** | Future commerce/publication and purchase mechanisms for separately published products | **No additional playable catalogue listings until a real eligible campaign is approved and registered** |
| **My Campaigns / Saves** | Player's existing independent playthroughs and save/branch navigation | **Not the discovery catalogue; keep accessible separately** |

**Current initial contents:** **The Hundred Years’ War** is the **only** campaign to show in the player-facing playable Content Library. Do not populate the list with Roman, Military, Historical, Fantasy, Star Wars, or other Genre Engines, mechanics packages, technical libraries, example templates, planned campaigns, inactive/unpublished records or test fixtures. Do not infer new campaigns merely because files exist in the repository. If other records or pre-existing saves exist, do not delete them: remove them from this catalogue projection only; inspect and preserve their original identity and state through appropriate administrative or save-specific interfaces. This is a **visibility/eligibility requirement**, not permission for destructive content migration.

**Hundred Years’ War detail flow:** Library → The Hundred Years’ War campaign detail → one of the ten date-specific Sub-Campaign starting periods (or an independently supported validated custom date) → permitted Starting Scenario / Custom Beginning → character or authorized institutional perspective → validate/start/resume a unique playthrough. *A Scot's Tale* must appear inside its relevant 1415 period, not as a second top-level campaign. Show no fictitious playable records to fill the layout. Mark the campaign or any entry as **In Development / Not Yet Playable** if its actual initializer or game loop cannot run; never provide a knowingly broken Launch control.

**Catalogue data contract (proposed logical separation; reconcile with real schema):** Distinguish `CampaignDefinition`/campaign product identity, `CampaignListing` or publication/discovery eligibility, `StartingPeriod`, `StartingScenario`, `GenreEngineRegistration`, and reusable `ContentModule`/genre Content Library. Use the real registry/adapter instead of hardcoding display cards; for this development version enforce an **explicit catalogue allowlist of the verified Hundred Years’ War campaign identifier** as configuration, not a permanent genre mechanic or an invented identifier. A listing requires the campaign to be of the correct content type *and* explicitly visible. Separately derive `canLaunch` from verified initialization, actual backend capability, access rules and starting-date availability; catalogue visibility alone grants no entitlement or gameplay capability.

**Navigation order:** `Home / Dashboard → Content Library → My Campaigns / Saves → Character Creation → Play (Story | World | Chronicle) → AI Network → Campaign Workshop → Marketplace / Publish → Account → Developer / Administration`, adjusted to existing responsive layout and authorization. Features may be nested by relevance, but **Content Library must visibly precede Campaign Workshop**. A player who wants to choose a campaign should find the Content Library without entering the Workshop. For current development, render honest shells for all planned features and preserve independent release visibility controls.

**Provider and technical asset boundaries:** Content Library read endpoints serve playable-campaign metadata and valid child entry/scenario data, not raw engine packages or unrestricted source-module files. The Workshop's later `Content Libraries / Modules` tab may browse and author technical assets under appropriate permissions but cannot contribute additional playable catalogue cards merely by installing/registering an engine. Marketplace product and entitlement records are distinct from actual playable-campaign launch eligibility.

**Data and source rule:** Preserve stable campaign IDs and selected historical research editions. Existing published or private save records remain independent of catalogue membership. Future catalogue expansion must require an explicit eligible campaign registration/publication decision; do not silently widen the initial list through new engine registrations.

### 4.3 Complete tab/feature register (designate in THIS build)

The following is the *minimum consolidated feature inventory* represented in the four source documents. “Now” means **routable, visible to authorized development users, with an actual section**; underlying functionality retains its separate priority.

#### A. Home and player-facing Content Library — `Home / Content Library` (**before Workshop**)

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Home / Dashboard** | Status, resume last game, access the campaign directory and current workspaces | Real navigation and accessible shell |
| **Content Library / Campaigns** | Player-facing directory of actual campaigns, independent of Genre Engines and technical Content Libraries | **Functional Stage-One route. List only The Hundred Years’ War, backed by registered campaign data** |
| **Hundred Years’ War Campaign Detail** | One Grand Campaign's metadata, scope, historical source edition, available entry periods, honest readiness | Real detail linked from its sole campaign card; no fabricated launchability |
| **Starting Periods & Entry Points** | Ten HYW historical period definitions and their actual date-specific availability | Nested under the Hundred Years’ War detail, never separate campaigns |
| **Starting Scenarios** | *A Scot's Tale* and any actually registered eligible predefined/custom beginnings | Nested under the chosen HYW period, never separate playable campaign cards |
| **My Campaigns / Saves** | Independent playthroughs, resume, permitted branches and provenance | Functional saved-game access even if a save's content is excluded from catalogue |
| **My Library / Owned Content** | Account entitlement views, owned campaign products, relevant templates and expansions | Separate from public Content Library; entitlement-backed or clearly planned |

#### B. Create & select a character — `Character Creation`

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Choose Perspective** | Existing character, custom individual, or eligible institution/faction-level play | Functional for Stage One path |
| **Existing Characters** | Date-sensitive search and identity selection | Show existing actual records, not hardcoded roster |
| **Existing Factions / Institutions** | Date-sensitive institutional perspectives, separate from employment | Availability and control permissions |
| **Identity & Origins** | Birthplace, nationality, culture, identity, languages, lawful statuses | Separate nationality from allegiance |
| **Family & Household** | Parents, guardians, siblings, kinship, household members | Stateful life-path draft; persist actual actors on commit |
| **Wealth & Responsibilities** | Family property, debt, work obligations, economic upbringing | Family ownership vs personal access distinction |
| **Education & Capabilities** | Learning, skills, study, experience, qualifications | Core-derived results only |
| **Formative Life Path** | Childhood decisions, mentorship, bonds, adversity and routine life | Conditional guided choice interface |
| **Adolescence / Adult History** | Career, employment, travel, later relationships | Age-sensitive creator |
| **Career / Service / Contracts** | Independent civilian, mercenary, multiclient, foreign service, scientists etc. | *Optional affiliation*, prospective vs active |
| **Starting Assets & Review** | Property, equipment, condition, debts, authority, biography preview | Clear invalid/unresolved state |
| **Confirm & Begin** | Atomic world initialization and unique playthrough | Stage-One requirement, never clone existing actors |
| **Opening Scene Handoff** | Enter Story automatically with a brief causal situation and first player decision | Functional Stage One; persistent state/version, no forced PC speech/action |
| **Standalone Character Templates** | Basic campaign-free character creator/templates | Included base-game feature, not paid Workshop-only |

Distinct Quick / Guided / Detailed creator depths share authoritative initialization; advanced deep editing may remain staged. Creating a character does not require picking a faction, and a Scottish character may seek English service or foreign scholarly employment when feasible. The character may have no employer or multiple compatible relationships. A request to join an institution is **not** acceptance or a permanent allegiance.

#### C. Gameplay shell — `Play`

Keep **Story | World | Chronicle** as the three **primary** views; other controls are **auxiliary** views accessible via sidebar, drawers or contextual tabs.

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Story** | Readable narrative, NPC communication, declaration composer, Core outcomes | Functional Stage-One vertical slice |
| **Opening / First Interaction (within Story)** | Show initial real location, concise setting/NPC hook, freeform player response, then Core outcome | Functional Stage One; no standalone campaign/tab or auto-selected PC action |
| **World** | Shared World & Civilization workspace with subviews below | Working viewer foundation |
| **Chronicle** | Event history, biography, dated records, long-term history | At least actual readable playthrough record |
| **Character** | Condition, skills, assets, affiliations, life history | Actual player character projection |
| **Inventory & Equipment** | Ownership, locations, condition, custody, transactions | One Core inventory source |
| **Relationships & Household** | Known social graph, relatives, responsibilities | Permission-filtered view |
| **Family / Lineage / Legacy** | Ancestry, descendants, estate succession, contributions | Reuse Core continuity; staged advanced graph |
| **Career / Contracts** | Employment, mercenary agreements, offers, obligations | Draft/inspect; real contracts when supported |
| **Projects / Research** | Construction, training, investigations, discoveries and actual progress | Real project records; no auto-completion |
| **Journal / Personal Records** | Character-visible notes, recent events, biographies, bookmarks | Dated filtered records |
| **Notifications / Reports** | Messages, delayed reports, orders, observations and updates | Occurrence/receipt distinction |
| **Action / Time Controls** | Explicit declaration, time advance, delegated orders, pause/inspect | No time progression from mere navigation |
| **Saves / Branches** | Current save, resume, permitted branches, version/provenance | No duplicate events/currency on retry |

#### D. World & Civilization — `Play → World`

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Atlas** | Physical geography, political claims vs actual control, settlements | Functional Stage-One map/list fallback |
| **Atlas Layers / Search / Routes** | Multi-scale overlays, known places, time-aware routes | Staged actual geographic data, not invented geometry |
| **Economy** | Household, enterprise, settlement, nation ledgers | Permission-filtered Core summaries |
| **Resources / Production / Trade / Finance / Labour / Logistics** | Distinct economic projections and stock/forecast/transit data | Subnav for each, at least shell if unsupported |
| **Politics & Government** | Offices, authorities, jurisdiction, claims, diplomacy | Date-specific authority views |
| **Diplomacy / Treaties / Political Networks** | Negotiations, messages, alliances, contested titles | Inspect/draft/submit separation |
| **Military & Command** | Formation hierarchy, orders, reported units and readiness | Command only for authorized scope |
| **Operations / Supply / Mercenary Companies** | Deployment, reconnaissance, contracted force and logistics | Shared actual personnel/resources |
| **Settlements / Cities** | Populations, households, buildings, service provision | Actual records, no fictitious buildings |
| **Infrastructure / Construction / Maintenance** | Repairs, construction proposals, land rights, project progress | Validated projects and ledger accounting |
| **Institutions / Organizations** | Governments, noble houses, guilds, universities, companies | Linked singular identity and assets |
| **Governance / Members / Assets / Contracts / History** | Institution actions, offices, organizational evolution | Actual authority and historical roles |
| **Civilization Overview** | Cross-domain strategic overview, reforms, delegation | Aggregate projections, no seventh simulation |
| **Technology / Discoveries / Research** | Knowledge, feasible innovation, manufacturing and dissemination | Genre-informed Core projects |
| **Historical Comparison** | Historical baseline vs living state, future event plans, divergence | Creator/debug **only**; never normal PC knowledge |

#### E. Campaign Workshop — `Create / Workshop` (**follows Content Library; Stage Two mechanics**)

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Workshop Dashboard** | Personal authoring projects and overview | Planned shell until Stage Two |
| **Campaign Builder** | Campaign profile, settings, modules and optional mechanics | Planned route |
| **Entry Point & Scenario Builder** | Dated and fictional starts, protagonists and constraints | Planned route |
| **Character & NPC Templates** | Reusable actor and personality assets | Basic templates player-side; advanced paid tooling staged |
| **Item & Equipment Templates** | Player item designs and asset copies | Basic permitted tools now if feasible |
| **Geography / Map Authoring** | Regions, settlements, travel links, overlays | Planned route |
| **Governments / Factions / Institutions** | Political, social, economic, military organizations | Planned route |
| **Technical Content Libraries / Modules** | Genre-engine content, reusable specialized mechanics/setting assets and authoring modules—not the player-facing campaign directory | Planned authorized Workshop route; **never automatically listed as playable campaigns** |
| **Templates / Clone / Extend** | Reference, Clone, Modify, Override, Extend | No mutation of shared original source |
| **Research & Historical Data** | Source references, historical start editions and provenance | Planned authorized creator route |
| **Validation / Playtest** | Test own created content against Core and continuity | Planned route, distinct from actual playtesting |
| **Versions / Exports / Dependencies** | Versioned authoring output and compatibility | Planned route |
| **Workshop Access / Time / Credits / Packs** | Paid access, usage and expansions | Tabs only; no unapproved fees/quotas |

#### F. Marketplace, publishing and packaging — `Marketplace / Publish`

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Marketplace Browse** | Future commercial catalogue, campaign publication and pricing distinct from the Stage-One Content Library | Planned browse route; **no unauthorized extra playable campaign cards** |
| **Product Detail / Contributors** | Published campaign info, classification, provenance | Planned route |
| **Bundles / Entry-Point Upgrades** | Ownership-aware campaign completions | Planned; preserve existing entitlements |
| **Merged Campaigns** | Separate newly published combined products | Separate product/entitlement route |
| **Publish / Submission** | Submit content for review and approval | Creator route, planned until Stage Three |
| **Submission Review / Status** | Validation, rights declarations, approval status | Role-based creator/administrator shells |
| **Package Builder** | Select source works, consent, integration, versioning | Restricted creator/admin planned route |
| **Contributor Consent / Splits** | Explicit creator approval and negotiated 80/20 allocation | No auto-approval or arbitrary split |
| **Royalty & Payout Dashboard** | Royalties, eligible proceeds, payout history | Restricted planned route, no made-up money |
| **Rights / Attribution / Provenance** | Source authorship, licensing, reusable assets | Creator/admin planned route |

#### G. AI orchestration — `AI Network`

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Spiderweb Network Map** | Graph of Directors, specialists, system capabilities and connections | Functional real registry visualization in AI foundation phase |
| **Directors & Scopes** | GM; World, National, Regional, Local, Scene; multiple scoped instances | Registry and instance inspector |
| **Specialist Registry** | Character/personality, writing/dialogue, narration, historical, rules, social, strategy, etc. | Registry view, staged capabilities |
| **Providers & Models** | OpenAI/Anthropic/Google/local adapter configuration | Provider-neutral and server-safe |
| **Capability Broker / Access** | Least-privilege access, temporary grants, delegation | Show actual permission routes |
| **Connections / Tasks** | Permanent, temporary, delegated links and task statuses | Real graph links, not decorative-only |
| **Events / Scheduler / Fidelity** | Shared-clock event subscriptions and simulation fidelity policies | Actual state or staged shell |
| **Execution Traces / Errors** | Invocation path, failures, timings, costs | Instrument real activity, sanitize logs |
| **Benchmarks / Comparisons / Budgets** | Model quality, structured reliability, cost and latency evaluation | Planned shell until measured |

The high-level v0.7 “AI Director” is a **logical orchestration responsibility** fulfilled within the **six-Director network**. Do **not** add a conflicting seventh Director. The Game Master coordinates the five categories but has **no dedicated specialists**; scene/local get high fidelity, region/nation/world default to abstract. The conventional orchestration controller enforces deterministic permissions, task routing and Core access. It must continue supporting routine operations if the Game Master model is unavailable.

#### H. Account, access and solo progression — `Account`

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Profile / Settings** | Account identity, accessibility and app preferences | Existing settings or shell |
| **Licences & Distribution** | Official release identity, owned licence information and approved distribution terms when available | Planned/authorized shell; no fabricated licence status or destructive logic |
| **My Purchases / Entitlements** | Base game, campaigns, entry points, workshop/packs | Planned commerce projection |
| **Gameplay Access / Rest** | Usage allowance, Rest/return availability | Distinct from character sleep and world time |
| **Usage & AI Costs** | Player-facing allowance, charge metadata, account logs | Planned; no arbitrary costs |
| **Workshop Credits / Authoring Time** | Separate authoring credit/time accounting | Planned distinct account ledger |
| **Solo Universal Points** | Reserved feature location for cross-campaign points | **Deferred, disabled; no fake wallet balance** |
| **Solo Currency Conversion** | Source campaign currency → universal points | **Deferred, disabled; no functional exchange** |
| **Solo Redemption Catalogue** | Solo currency/stat points/setting gear | **Deferred; no prices/availability invented** |
| **Solo Transaction History** | Auditable authorized point transactions | **Deferred; no fictitious transactions** |
| **Privacy / Connected AI Providers** | Provider settings, account security, export where supported | Secure, server-controlled |

Solo points must **not** be confused with workshop credits, bought gameplay usage, marketplace cash, or fictional campaign money. This is a solo-only future capability. Do not implement conversion formulas, exchange rates, caps, reward catalogues or actual wallet/grant functionality yet. In a later implementation, the account-level service will coordinate atomic/idempotent source-campaign deductions, point balances and destination-Core grants; resist save/branch duplication and block multiplayer transfer.

#### I. Operations & development — `Developer / Administration`

| Tab / child tab | Purpose | Current-version UI target |
|---|---|---|
| **Feature Registry / Release Visibility** | Show all planned tabs in dev, independently hide for release | **Functional now** for authorized developers |
| **Opening / First-Turn Diagnostics** | Inspect start creation request, scene focus, opening status, first action/event IDs, retries and recovery | Authorized development diagnostics using real records |
| **Build Provenance / Licence Verification** | Inspect release/source provenance and plan eventual safe service authorization | Planned restricted shell; no self-wiping or unapproved account lockouts |
| **System Status / Health** | Game backend, Core integration, provider status, persistence | Real health metadata or explicit unknown |
| **Campaign State Inspector** | Version, actor IDs, ledger/events, control scope | Restricted dev diagnostics only |
| **Historical Source / Event Inspector** | Baseline, assertions, provenance, conditional future plans | Restricted dev/creator only |
| **AI Network Diagnostics** | Broker authorization, task traces, cost/errors | Restricted dev only |
| **Validation / Tests / Reconciliation** | CMRR, regression reports, known failures | Execution evidence only |
| **Publication Moderation / Rights** | Approval, consent, rights, trademarks | Planned restricted route |
| **Commerce / Royalty Accounting** | Transaction, entitlement, creator payout liabilities | Planned restricted route |
| **Migration & Versioning** | Schema, historical research edition, compatibility migrations | Planned; no automatic retroactive changes |

The player-facing **Content Library** must appear as a distinct real top-level destination **before the Campaign Workshop**; use existing router naming as appropriate. The ordinary playable list currently contains **The Hundred Years’ War only**; neither any Genre Engine nor its technical Content Libraries may render there.

All listed route labels are **logical UI requirements**, not mandates to replace existing working URLs or create redundant components. A coherent parent/child tab structure is preferable to individual top-level routes for every fine-grained subsystem. If the existing website uses a different naming convention, document a one-to-one mapping and preserve backwards navigation.

### 4.4 Required states for each planned tab

Use an honest, functional component template for features that are not yet implemented: heading, purpose, owner/layer, lifecycle status, dependencies, planned access scope, current capability (including “not yet available”), return navigation, and optional link to relevant specification. Do not display functional *Buy*, *Convert*, *Apply*, *Submit*, *Issue Order*, *Transfer*, or *Accept* controls until backed by approved real operations. Never put a fake monetary amount or misleading progress metric in a preview screen.

**Release handling:** Each tab can be surfaced in the authorized developer build and hidden/restricted in the release build by registry configuration. Hiding is **not** a security mechanism. Even if a client requests a hidden route directly, backend authorization and feature gates must still enforce data and action restrictions. No secrets in client payloads. Provide a single settings view to inspect the release visibility matrix and test expected visibility by role.

### 4.5 Navigation and visibility acceptance tests

- All rows in the inventory above have registered, nonbroken routes or contextually navigable child tabs in the current dev build; navigation is not an illustration only.
- **Content Library is navigable directly from the player-facing interface and is placed before Workshop** in the relevant navigation order; no Workshop purchase/access is needed to browse the current campaign.
- **The playable Content Library lists exactly one campaign: The Hundred Years’ War.** All Genre Engine records, technical Content Libraries/Modules, AST as a standalone campaign, period profiles as standalone campaigns, and unapproved future campaigns are excluded. The ten HYW historical periods and registered scenarios remain reachable *inside* the single campaign.
- The campaign list is derived from actual campaign registry metadata plus an explicit current catalogue visibility/eligibility filter; registration of a new Genre Engine never adds a playable listing. An unavailable HYW initialization produces an honest disabled launch state, not a false gameplay claim.
- Existing legacy saves are not deleted or silently migrated when noncampaign technical records are removed from the visible playable listing.
- Stage-One functioning features really work and are not replaced by placeholders; incomplete sections clearly say so.
- Reload and direct deep-link work for authorized tabs. Search, keyboard focus, screen readers, narrow viewport and back navigation operate correctly.
- Feature tabs can be disabled or hidden for release **without deleting their definitions, changing URLs, or corrupting saved state**.
- Admin/creator/paid/owner-only routes reject unauthorized direct requests; hiding tabs alone never grants/denies their API permissions.
- Switching among Story/World/Chronicle or any tab does not change world time, spending, position, injuries, or contracts.
- The developer registry enumerates exactly what exists, what's functional, what is deferred, and what is blocked by missing backend capabilities.
- Creator marketplace, account currency exchange and AI Network management cannot silently appear to ordinary players as operable until real permissions, billing, entitlements and backend operations exist.

---

## V. Six-Director orchestration integration (reconciled)

Implement a **hierarchical, multi-provider orchestration foundation**, not a second simulation engine and not a mandatory large AI ensemble before gameplay is possible.

| Category | Instances and scope | Fidelity | Main responsibility |
|---|---|---|---|
| **Game Master Director** | Normally one per campaign | Coordination only | Supervises networks, cross-layer tasks, dependencies; **no dedicated specialists** |
| **World Director** | World-wide as applicable | Abstract/minimal | Inter-civilization and large-scale developments |
| **National Director** | Multiple sovereign polities / major factions | Abstract | Government, strategy, diplomacy, institutions |
| **Regional Director** | Multiple provinces/states/duchies | Abstract/selective | Regional administration, economy, security |
| **Local Director** | Multiple settlements and operating areas | Detailed | NPCs, economy, relationships, local institutions |
| **Scene Director** | Multiple concurrent scenes | Maximum detail | NPC intentions, writing, narration, validated scene output |

These are six **Director categories**, with potentially many instances below Game Master, not six processes permanently consuming tokens. Their actual scope graph must support overlapping institutions, political claims and geographic regions; nationality is not a director scope mapping shortcut. Scene/Local details get priority; inactive higher layers can process aggregated events and be lazily activated without loss of history. Fidelity shifts may never replenish stock or duplicate people.

A Director delegates through a **Capability Broker** with backend-enforced, least-privilege read/propose/commit permissions. Model/provider gateway uses adapters, no credentials in browser/source. Specialists are modular roles (Character Intelligence determines NPC private intention; Dialogue Intelligence expresses approved intention; Narration presents Core-confirmed outcomes; Historical/Lore, Social, Political, Military, Economic, Knowledge, Memory and Rules may support as relevant). The Game Master itself does not get a specialist pool. Generic **Director** in v0.7 maps to orchestration, **not a seventh node**.

Maintain one event/clock/state ledger in Core; directives/tasks carry unique IDs, campaign/scope/correlation IDs, expected result type and bounded retry semantics. Use conventional backend controller for routine routing. A failed AI call never commits partial authoritative effects. Demonstrate at least one **real mock-provider vertical slice**: player declaration → authorized Director/specialist tasks → deterministic Core validation → one committed event → appropriate Director notification → narrated response. Never claim a spiderweb visualization is functional when it only renders hardcoded sample nodes. For Stage One, simpler single-model execution may be used where safe and efficient.

**Stage-One prerequisite distinction:** The playable loop can launch with a minimal provider adapter and structured role separation. The six-Director foundation must be implemented in manageable later slices, while its **AI Network tabs already exist** in this version. If feasible in the current round, implement the registry/adapter/broker with a working mock path. Do not block game initiation pending every specialist or every national-scope simulation.

---

## VI. Hundred Years’ War and gameplay integration

Treat **The Hundred Years’ War (1337–1453)** as the **only campaign listed in the player-facing Content Library for this development version**, and as one historical **Grand Campaign**, with ten historically researched starting periods (1337, 1360, 1369, 1389, 1415, 1422, 1435, 1444, 1449, 1453), multiple scenarios and separate persistent playthroughs. *A Scot's Tale* is a scenario in 1415, **not an independent campaign, an independent genre engine, or a mandatory protagonist for all HYW games**. Engines and technical libraries must not be displayed in the playable catalogue. Historical entry-profile dates and the AST recruitment-yard exact start must be individually source-verified. Preserve the complete per-period political/technology/relative-strength and difficulty tables included in Source Volume C.

**Historical baseline policy:** The actual historical past is initialized for the chosen start cutoff. Sufficiently sourced future events have **conditional default plans** and proceed historically only when causal prerequisites, actors and resources remain intact; a changed cause can alter, postpone, supersede or prevent an event. No predetermined outcome can undo a real simulation result or create missing armies, deaths, inventions, money or PC choices. Creator-only comparison and historical-event plans must never leak future omniscient information into player views. Worlds continue beyond 1453 and may develop early/late technology when physical and institutional prerequisites support it.

**Character pre-game flow:** Period/date → scenario/custom beginning → existing or new actor / eligible institution perspective → nationality/identity (separate from allegiance) → family/guardians/siblings → economic upbringing/work obligations → formative choices/education/skills/bonds → adult history → **optional** employment/service/contracts → current resources/relationships/location → validate and review → **one atomic independent playthrough initialization**. A child, existing historical actor, predesigned AST Ian, or elderly starting character has different editable history. National origin never automatically prohibits working for a foreign government or army. No faction membership is mandatory. Mercenaries, civilian independent workers, merchants, scholars, soldiers, officials, researchers and multiclient contractors can be pursued without occupation classes trapping future agency.

**Life paths must create real authorized starting records:** parents/siblings/mentors and friends are autonomous actors; household money differs from personal stock; exposure to a trade differs from demonstrated competence; apprenticeship applications differ from accepted employment; exclusive contracts cannot grant the same individual/time/resources to multiple employers without legitimate terms. Do not use an invented free-form stat point economy; use adopted progression rules. A new character's retrospective history must not rewrite established historical actors or an already-diverged save.

**World views:** Story | World | Chronicle are primary. World child tabs Atlas, Economy, Politics, Military, Settlements, Institutions, and aggregate Civilization draw from shared Core. Map scales/detail depend on source data; no fabricated coordinates/floor plans. Distinguish political sovereignty, effective administration, occupation, private ownership and jurisdiction. Military totals separate assigned/present/available; contracts and companies persist after expiry. Construction, diplomacy, troop orders and research remain drafts until authorized/resolved through Core. Actor knowledge is limited to observed/reported/received information with real timestamps and uncertainties. Inspecting a tab never mutates state. Narrative archive summarization (annual → five-year → 25-year → century, cumulative centuries → 500-year sealed epoch) is a **view**; retained actors, assets and histories survive.

---

## VII. Commercial product rules and postponed features (preserve exactly)

**Five campaign classifications:** Short Story → Curated Campaign → Full Campaign → Major Campaign → Grand Campaign. Equivalencies: **6 Short Stories = 1 Curated; 8 Curated = 1 Full; 3 Full = 1 Major; 2 Major = 1 Grand**; a directly authored high-tier campaign is allowed where justified. Grand Campaigns are IRGS productions; Major Campaigns may be standalone IRGS or approved collaborative efforts. A size equivalence is not proof of substantive content quality.

**One-time base purchase** is the intended model, with starter campaigns/entries, a campaign-free basic character creator/template tools and a **generous but limited** gameplay allowance. Gameplay access tiers vary permitted play before an enforced **Rest**, **not** mechanics, AI quality, purchased campaign content or simulation fidelity. Enforced account Rest is not in-world sleep, in-world time, healing, resource refill, or undeclared player action. No final prices, allowances or schedules are approved.

**Content Library:** Stage-One, player-facing campaign catalogue and launch route; **The Hundred Years’ War alone** is listed now. It is distinct from technical Genre Engine/Content Library assets and the later paid Workshop.

**Workshop:** Paid future campaign-authoring tools and separately metered time/credits; explicit Clone/Reference/Modify/Override/Extend paths and controlled reusable content. Basic player character creation cannot be made Workshop-only. **Marketplace:** v0.7 adopts **80% creator / 20% IRGS** of appropriately defined distributable proceeds for qualifying creator-published products; continuing creator royalties. IRGS intends to acquire specifically identified accepted published creator content through agreed assignment with explicit creator license-back and rights protections; no automatic ownership of drafts/third-party assets. Legal review required. Do not reinstate old 88/12 percentages or assume completed trademark filings.

**Merged campaigns:** A separately sold, separately entitled product, **not a sixth classification**. Each source creator must explicitly consent to the specific package; contributors divide a negotiated collective **80%**, IRGS retains 20%. Sources and contributors are credited in the storefront listing. Buying a merged campaign includes its embedded playable materials but **does not grant separate standalone entitlements** to the original campaigns; buying originals does not unlock the merger. No automatic source/merged discounts. Example: *Eight Realms of Mertup* has eight Curated sources, one independently sold Full Campaign and separately versioned campaign state; equal 10% shares are **example only**, never a default allocation.

**Deferred universal solo points:** A player may eventually convert legitimate in-campaign currency in an eligible solo save into account-level points, then redeem them in another eligible solo campaign for its local currency, compatible stat progression or setting-specific gear. Completely barred from multiplayer and any later multiplayer import. Platform owns future universal wallet/transfers; Core owns campaign currency, stats, inventory and grants. Keep workshop credits, usage tiers, commerce money, and solo points distinct. Save rollback, branching and repeated requests must never duplicate points or rewards. **Only designate planned tabs and dependencies now**. Do not implement balances, rates, costs, rewards, transactions, fees or rules without separate user authorization and calibration.

**Implementation sequencing remains game → Workshop → Marketplace.** Build tabs for all now; do **not** use their existence as a reason to implement commerce or unfinished solo economy prematurely.

---

## VIII. Work order and phase gates

**Phase 0 — Audit/CMRR.** Inspect repository/archives/website APIs/test scripts, check startup and saves, catalogue source versions, identify adopted vs proposed mechanisms, log overlaps and conflicts. Verify exact source documentation, instead of inventing it.

**Phase 1 — Navigation registry + Content Library + game shell.** Reuse existing navigation; add every designated tab and role-scoped route in Section IV, implement honest planned feature shells and dev/release visibility controls. **Implement a working player-facing Content Library before the Workshop**. It must list **only The Hundred Years’ War** as a campaign; route to its period/scenario selections, and never list any Genre Engine or technical Content Library as a playable campaign. Preserve existing saved playthroughs and clearly report missing launch capabilities. Preserve Story/World/Chronicle gameplay hierarchy. No new duplicate route trees. Demonstrate navigation by direct URL and mobile.

**Phase 2 — Stage-One playable vertical slice.** Use a small known state with a real campaign selection and creation path, **a short interactive opening immediately after character confirmation, freeform first input, saved first-turn status and exact-once Core event handling**, Core-authoritative clock/resources, action validation, NPC dialogue/narration, journal/chronicle events, persistent saves and reload. An independent 1415 AST/HYW-compatible scenario can be used if the actual baseline/date/sources exist; otherwise use a transparently labelled controlled test fixture rather than false historical precision. A creator should be able to select a different character or custom life path.

**Phase 3 — AI orchestration foundation.** Registry for six Director categories and multiple instances, provider adapters/mock, specialist registry, broker permissions, event subscriptions, deterministic orchestration, real execution traces, spiderweb view sourced from registry, error-safe demo. Implement in slices or alongside Phase 2 where safe. Never require all specialist models in order for Stage One to work.

**Phase 4 — World viewer and management depth.** Real Atlas/list navigation and permission-filtered inspections; expand Economy, Settlements, Institutions, Politics, Military and Civilization panels only when actual Core records and authority are available; demonstrate same entity/asset across views. Add conditional historical baseline/creator comparison without knowledge leaks.

**Phase 5 — Workshop implementation (after playable game and Content Library).** Reusable authoring and controlled templates, entry points, maps/institutions, testing, versioning, workshop access/credits when defined. No live marketplace dependence.

**Phase 6 — Publishing and commerce.** When operational/legally defined, implement entitlements, entry-point upgrades, publication approval, 80/20 creator ledger, IP agreements, consensual campaign merging and payouts. Exact prices and legal mechanics remain open.

**Later separate project — Solo cross-campaign points.** Create approved exchange rules and security design, stress-test against saves/branches, calibrate rates and rewards, then implement gated transactions; otherwise leave tabs as Deferred.

For each phase report actual changed files/routes, real behavior, commands/tests run, failures, known gaps and next dependencies. Passing test scripts is not playtesting; successful scaffolds are not full features. Refuse to paper over missing systems with fake gameplay values.

---

## IX. Required cross-domain acceptance and regression tests

| Domain | Minimum passing behavior |
|---|---|
| **Navigation completion** | All planned tabs registered/routed/visible to authorized dev users; independent release switches; no broken direct URLs or blank screens; mobile/accessibility work |
| **Content Library order and reachability** | Real player-facing Content Library tab precedes Workshop, supports back/forward/deep links, and never requires Workshop authoring access to browse |
| **Only one playable campaign listed** | The Hundred Years’ War is the **sole** campaign card; Genre Engines, technical modules, example templates, AST as a standalone campaign and period profiles as campaigns are absent; nested entries exist only under HYW |
| **Catalogue registration and readiness** | New engine registration does not create a campaign card; only explicit current HYW catalogue allowlist is visible; actual initializer readiness controls Launch, and unmet dependencies are honestly reported |
| **Existing save safety** | Hiding an invalid catalogue entry or engine card does not delete or change existing playthrough records; saved-game listing remains separate from catalogue |
| **Release safety** | Hidden/preview/admin routes enforce backend permissions even with guessed URLs; no developer historical future leaks |
| **Basic gameplay** | Player chooses campaign and character; immediately receives a state-grounded playable opening; declares a freeform action; Core validates/commits; AI narrates; save/load resumes exact state |
| **First-scene agency** | Opening does not invent PC thought, speech, movement, employment, oath, contract or choice; one meaningful hook and player decision point, no forced quest/combat |
| **Opening persistence and retries** | Initial create, NPC opening event and first submitted action are individually idempotent; reload before/after first action causes no duplicates |
| **Opening variation** | AST recruitment before sponsorship, independent mercenary, civilian and scholarly/institutional starts remain possible and context-appropriate |
| **Character agency** | No fabricated PC speech, travel, motives, purchases, successor, political decision or expenditure |
| **Identity / service** | Scottish actor can seek English employment; nationality unchanged; no mandatory faction; application is not hired status |
| **Life-path continuity** | Siblings, parents, mentors become actual referenced actors; edits do not leave orphan records; no free invented household assets or skills |
| **Date-sensitive history** | 1337 vs 1415 vs 1422 vs 1444 starts show different actual actors/institutions/reforms; 1445 changes not preloaded in 1444 |
| **Conditional historical future** | Agincourt event prerequisites evaluated; destroyed army never resurrected; unaffected events remain eligible; no guaranteed outcomes after altered causes |
| **Independent campaigns** | Two saves never share mutable world history; AST recruitment yard does not start with later service checkpoint state |
| **World views** | Map/search/zoom/tabs never advance clock; claims vs control distinct; map access shows dated information and no omniscience |
| **Resource/military accounting** | Cross-workspace totals and unit hierarchy do not double count stock, troops, casualties, labour, income, reservations or transit |
| **Actions / commitments** | Draft bridge/treaty/order is not built/signed/executed; Core checks rights, resources, recipient communications and outcome |
| **Institutional autonomy** | Households, companies, governments, towns and mercenaries progress through actual world events offscreen |
| **Director network** | GM + multiple scoped Director instances; specialist delegation; least-privilege broker; mock provider; real graph registry; no direct AI Core override |
| **AI failure** | Timeout, retry and duplicate task preserve state; AI costs observable; single-model fallback still produces valid narrative |
| **Rest** | Account Rest never heals the PC, advances world time, refills resources or autoexecutes declared actions |
| **Workshop separation** | Basic creator independent of paid Workshop; clones don't mutate originals; future work tabs don't grant paid privileges |
| **Entitlement separation** | Source vs merged campaign product access independent; rights/provenance intact; no accidental source unlocks |
| **Royalty accounting** | Eligible creator published 80/20 where applicable; merged allocations require consent and sum exactly to 80% creator + 20% IRGS |
| **Solo points (deferred)** | Planned tabs exist but conversion, balances, redemptions, fees and reward grants are **inoperative**; no multiplayer access |
| **Non-destructive IP controls (planned)** | Provenance and licence tab routes designated; unauthorized hosted-service access can be designed to fail closed without deletion, corruption, exfiltration or destructive code |
| **Safe build integrity** | Legitimate backups/offline dev and saves survive failed checks, retries, network outages and copied folders; no false-positive self-wipe |
| **Long-scale continuity** | Centuries, sealed 500-year epochs and scale shifts preserve ledgers, projects, biography IDs and ongoing obligations |

These are **future acceptance criteria** until code and tests run. Test high/low scarcity, edge cases, overlapping authority, simultaneous events, contradictory history, unauthorized tools, network failures, imported/copied saves and source migrations. Do not certify calibration merely because a schema or UI renders.

---

## X. Reconciliation / supersession register

| Overlapping or conflicting instruction | Decision to implement | Provenance |
|---|---|---|
| Generic singular “AI Director” vs six Directors | One overarching **Game Master** coordinating five simulation Director **categories**; generic 'Director' only names orchestration capability, not a seventh hierarchy role | v0.7 + Six-Director v0.1 |
| Finish all AI roles now vs first playable game | Build minimal Core-integrated playable loop; provide expandable six-Director groundwork with a working mock demonstration when feasible, **not a prerequisite for every gameplay turn** | v0.7 Stage One + AI Foundation |
| Tabs for features only at their development phase | **Superseded by user directive:** designate routed tabs for **all planned features now**; backend implementation remains phased | User's earlier tab correction |
| Engines shown in playable campaign list | **Rejected:** Genre Engines and technical engine Content Libraries are backend/authoring resources, not playable campaign entries. **The Hundred Years’ War is the only currently listed campaign.** | Latest user correction |
| Campaign browse within Explore/Workshop versus Content Library | **Relocate/reconcile:** establish **Content Library** as the player-facing campaign catalogue, preceding the **Campaign Workshop**; preserve separate Owned Library, Workshop technical libraries and future Marketplace. | Latest user correction |
| Other existing campaign/saved state omitted from visible catalogue | Filter catalogue display only; **never delete, overwrite, or silently migrate historical playthroughs or engine data**. | Current requirement + Core continuity |
| All planned sections visible in dev vs publicly released | One controlled feature registry with independent developer/preview/release visibility; no unauthorized data access | Current user correction + security policy |
| Author historical outcomes vs player agency | Historical future conditionally defaults when causal pathway intact; Core can alter/prevent plans; never force impossible facts | Part 1 HYW v0.4 |
| National origin vs military or other employment | Separate identity, legal status, allegiance, service, contracts, faction-level control | Part 1 HYW + user directions |
| Mandatory faction selection vs independent career | Faction service **optional**, multiple compatible clients permitted; institutions selected for *control* are separate | Part 1 HYW + user directions |
| Multiple World dashboards vs one source of state | Single Core ledger/world; permission-filtered read projections, explicit action commit | World & Civilization v0.1 |
| Character creator included with base vs paid Workshop | Basic campaign-free character/templates included with base game; advanced campaign-building is separately paid later | v0.7 commercial |
| Permanent game purchase vs unlimited AI calls | Permanent entitlement to base game, but finite usage tiers/Rest; Rest never progresses the game | v0.7 commercial |
| Gameplay tokens, Workshop credits and solo universal points | **Three different ledgers/entitlements**; no automatic exchange or equivalence among them | v0.7 + Solo Points deferred |
| Character confirmation directly enters an empty Story screen | **Superseded by v1.0:** initialize once, present concise context-grounded opening, await freeform first action, resolve and persist without replaying events | Current user directive, v1.0 |
| Request for anti-copy 'self-destruct code' | **Reconcile safely:** plan signed builds, attribution and server-side licence gating; **do not** add destructive, sabotage or data-wiping payloads | Current user protection intent, v1.0; preservation/safety |
| Older 88/12 creator distribution vs newer 80/20 | **80% creators, 20% IRGS** as directed; remove superseded 88/12 from live proposals | v0.7 |
| Campaign acquisition vs rights to unpublished drafts | Only identified accepted published works assigned by agreement; maintain creator rights, consent and provenance | v0.7 |
| Selective IP reuse vs wholesale merged packaging | Reuse and separately published merged campaigns have different agreements; consent required for whole-product merger | v0.7 |
| Source purchase vs merged campaign ownership | Separate entitlements, no automatic source unlocks or cross-product discounts | v0.7 |
| Future solo wallet feature vs playable-runtime immediate scope | Register and show disabled feature-page shells now; do not invent rates, wallet, paid grants or multiplayer spillover | Solo Points instruction |
| Historical UI demo vs researched historical reality | If source lacks exact numbers or geometry, show unknown/estimates with provenance, never fabricated as live | Part 1 HYW v0.4 + World UI |
| App launch/startup | Preserve working startup scripts and localhost conventions; report actual startup/testing | All four sources |

**Accounted removals/relocations:** The older **Explore Campaigns** label is consolidated into the player-facing **Content Library / Campaigns** route (preserve old deep links through compatibility routing when feasible). Any Genre Engine, framework, template, demo or technical Content Library card previously presented as a playable campaign must be **removed from that listing only**, not deleted from source, assets or existing saves. Workshop's `Content Libraries / Modules` is renamed in the integrated navigation inventory to **Technical Content Libraries / Modules** to avoid confusion with the player-facing Content Library. Only The Hundred Years’ War is approved as a current playable-catalogue listing. The archival source text remains untouched and any contrary wording is superseded by this integrated directive.

**Removals:** None of the substantive source specifications is intentionally deleted. Redundant directive wording is consolidated only in the integrated sections; **full source content is preserved below**. The actual implementation must account for any legacy code/system it removes and obtain approval for migrations. Undetermined prices, model assignments, conversion rates, historical values and legal clauses remain undetermined.

---

## XI. Codex completion output contract

Produce a complete report after the development work, including:

1. **Current repository and Core audit:** Exact files, functions, routes, schemas, existing behaviour, missing/incomplete modules, authoritative source versions.
2. **Navigation, Content Library and feature registry:** Show the actual single-record Hundred Years’ War campaign catalogue, nested periods/scenarios, clean separation from Genre Engines/technical Content Libraries, Content Library-before-Workshop order, backwards-compatible routes and existing save preservation. Provide exhaustive table of all planned tabs, their route, parent, role, dev/preview/release flags, lifecycle status, enabled backend capability, and clear 'planned' page behaviour.
3. **CMRR matrix:** Each source requirement mapped to retained, modified, merged, relocated, deferred, or rejected state; justification, provenance and dependencies; account for removals.
4. **Changed working implementation:** Files changed/created, why, backend/frontend integration points, actual API behaviour and save compatibility.
5. **Stage-One playable demonstration:** Steps to start website, choose character/world, **see the actual first scene, freely respond, receive a Core-resolved consequence**, save and resume without the opening replaying events. Include an opening-to-first-action trace, creation and first-turn request IDs, and interrupted/retried-state recovery. If blocked, show exact blocker and smallest honest partial functionality; don't claim completion.
5a. **IP protection planning:** Inventory copyright/licence/provenance and build-integrity controls, designate only truthful planned tabs, recommend trusted-server authorization for protected services. Explicitly confirm that no destructive anti-copy or 'self-destruct' payload, data-wipe, hidden retaliation, or unapproved telemetry has been introduced.
6. **Director-network demonstration:** Real registered nodes and correct permissioned task routing, with mocked provider permitted. If deferred/partial, say so.
7. **Test evidence:** Commands executed; passed/failed tests; separate unit, integration, scripted scenario, simulation, manual UI review and actual playtesting; no unearned balance/accuracy claims.
8. **Ownership and migration impact:** Identify one authoritative source per actor, asset, historical record, economy/commerce wallet, entitlement and clock; warn of all schema/save migrations and do not perform unapproved retroactive changes.
9. **Unresolved issues and calibration:** Exact historical data gaps, Core interfaces, quotas, pricing, royalty legal matters, talent/gear exchange, provider performance, geospatial coverage, startup and scale/performance risks.
10. **Versioned resubmission:** Updated coherent specification and change log, not only patches or a promise of future work.

> **Final priority rule:** Build a usable game, a player-facing **Content Library containing The Hundred Years’ War as its sole campaign entry**, a **brief and genuinely interactive opening after character creation**, and a complete, future-proof navigation skeleton **in this development version**. Genre Engines and their technical Content Libraries are never playable campaign listings. The Content Library precedes the Campaign Workshop. Later hide unfinished tabs for release by configuration, never by throwing away their routes or rewriting architecture. Keep every submitted UI and agent action subordinate to actual IRGS Core state, permissions, player agency, causal history and accounting.

---

## XI.a v0.9 reconciliation and catalogue migration note

**Change source:** User correction after v0.8: engines must not appear under playable campaigns; The Hundred Years’ War is currently the only listed campaign; player-facing **Content Library** is required before the Workshop. This instruction has higher authority than archival examples in the appended source volumes, without modifying their historical or technical content.

**Implemented in specification:** New player catalogue contract and distinction from backend Genre Engines, technical Content Libraries, the owned-content library and the commercial Marketplace; Content Library-first navigation; a one-campaign listing rule; readiness/launch safeguards; updated stages, phase order, acceptance tests and CMRR outcomes. **No repository or real website code has been modified by the preparation of this document.**

**Explicit migration warning:** Do not remove installed engines, source assets, unpublished work, saved playthroughs, or user entitlements. Only alter the player-visible discovery projection with a reversible visibility policy. Record any existing route aliases and maintain compatible navigation where practical. The current single-campaign restriction is a **versioned product catalogue decision**, not a permanent engine prohibition on future campaigns.

**Verification tasks for Codex:** Report (a) current visible catalogue records before change, (b) actual campaign registry identifiers and HYW readiness, (c) resulting single listed campaign, (d) technical engines still registered but absent from playable listings, (e) functional Content Library-first tab order, and (f) saved playthrough integrity.

---

## XI.b — v1.0 Campaign Initialization, Opening Scene & First-Interaction System

**Change source:** Current explicit user direction, 19 October 2026: Completing campaign and character selection must **launch a short beginning that plays out on screen and provides a concrete opportunity for the player to react, speak, decide, or act.** A bare blank Story screen, encyclopaedic introduction, generic welcome message, or indefinite unresponsive dialogue is not an acceptable first playable experience.

**Status:** User-required experience and interface contract; detailed runtime contract below is **proposed for Core and codebase reconciliation**. No implementation or playtesting is claimed.

### 1. Outcome and product boundary

After **Content Library → The Hundred Years' War → period/date → Starting Scenario or Custom Beginning → eligible control perspective / character method → Life-Path or existing-character review → confirmation**, the website must **automatically enter Story and display a coherent playable opening**. The opening should establish a situation already valid in the world and end at a meaningful point where the player can respond. **There is no second mandatory character-selection flow, faction-choice gate, or empty 'now begin your story' page.**

The opening serves the campaign's chosen playable perspective, not an obligatory war narrative. A civilian, independent mercenary, scientist/natural philosopher, merchant, farmer, landholder, officer, or authorized institutional perspective must receive a relevant opening. **Nationality remains independent of service**, and a character who chose no faction remains unaffiliated. Do not turn a career *interest* into an existing contract or appointment.

**Opening experience targets** (editorial, not fixed mechanical quotas):

- **Short and direct:** normally a handful of readable paragraphs, often one scene-setting beat followed by one live NPC or environmental beat and a clear decision point. Do not enforce a word count as a Core mechanic; scale for accessibility and scenario needs.
- **Present tense and immediate:** communicate where the character already is, what they can perceive, and what is happening now. Avoid an unskippable long lore dump or replaying the entire Life-Path biography.
- **Interactive:** offer a real point of engagement—someone asks a question, a situation changes, an ordinary opportunity presents itself, a report arrives, or a task awaits—without pretending there must be combat or dramatic danger.
- **Player-led:** halt at the first meaningful voluntary player decision. The input composer must accept **freeform speech and action declarations**, not require clicking an authored choice. Optional suggested actions are context-sensitive examples, not binding exhaustive options.
- **Causal:** the opening represents already established or Core-resolved facts; neither the scene text nor the AI may invent equipment, locations, spoken PC responses, contracts, wages, assets, NPC compliance or physical consequences.
- **Persistent:** the opening, initial player-control point, and any actual NPC/world events are recorded and recoverable after save/reload, retry, or reconnection without reapplying effects.

### 2. Responsibility boundaries

| Concern | Authoritative owner / responsibility |
|---|---|
| Campaign, date, scenario, initial conditions | Campaign profile, Historical Foundation, scenario content and verified historical start |
| Actor, starting location, possessions, family, bonds, legal status, employment/contract status | **Core-owned committed Campaign State**, initialized from validated character/scenario draft |
| Opening hook parameters, optional authored dialogue prompts, local scene annotations | **Starting Scenario content** or campaign opening profiles, with genre/setting presentation where relevant |
| What NPCs know, choose, do, and intend | Actual actor state and autonomy, aided by Character/Personality Intelligence where configured |
| Physical occurrences, time, location, injuries, expenditures, messages, effects | **Core** action/event/time/information systems |
| Scene focus, context selection, specialist delegation | Scene Director, subordinate to orchestration controller and Core permissions |
| Dialogue wording | Writing/Dialogue Intelligence expressing authorized NPC intent; cannot make player speak |
| Introductory prose and subsequent narration | Narrative specialist presenting established and validated results, filtered by controlled perspective |
| Showing first scene, player composer, pending/streaming/loading, continue/resume navigation | Website **Story** view; not a parallel simulation |
| First-turn control and subsequent user declarations | Player, through existing inspect/draft/submit → Core resolution path |

Do **not** implement a second 'narrative world state' in the AI, browser, or scenario authoring layer. The six-Director hierarchy remains GM plus World, National, Regional, Local, and Scene categories; **the Game Master has no private specialist team**. The ordinary opening can use a single configured model or deterministic fallback and should not require all Directors to activate.

### 3. Campaign launch: atomic handoff into Story

Implement or reconcile the following phases with existing initialization and event infrastructure:

1. **Review:** Player inspects and explicitly approves starting date, control assignment, identity, Life-Path/established biography, household, currency, gear, location, capabilities, knowledge, existing obligations and affiliation status.
2. **Validate:** Check all interrelated actor records, NPC existence, historical date cutoffs, physical locations, employer/contract acceptance, property ownership, permissions, resources, opening scene prerequisites and content/AI availability. Unknown or disputed facts retain appropriate flags rather than fabricated precision.
3. **Commit once:** Create a uniquely identified **independent playthrough** and authoritative initial Campaign State atomically. Record campaign/profile/research edition, scenario revision, controlled perspective, clock, stable actor and asset IDs, knowledge projection boundary, initial state version and an idempotent creation request ID. Do not commit a character-creation draft to an unrelated older save.
4. **Create opening focus:** Build a **provisional opening-context reference**, linked to the saved campaign and known local state, without granting resources, taking a player action or advancing time by itself.
5. **Resolve any actual autonomous opening beat:** If an NPC moves, talks, acts, sends a letter, or otherwise changes state in a mechanically consequential way, it must originate from a valid pre-existing initial circumstance or a **Core-authorized NPC/world event**, with actual time, authority, knowledge and resources. Purely descriptive prose requires no event transaction. The opening must not require an NPC action if no such actor or opportunity exists.
6. **Present opening:** Generate or retrieve the **filtered and validated** opening narrative; persist its presentation ID and completed text / structured narrative representation, relevant state version and linked events. Show it in Story with **freeform action/dialogue input available**.
7. **Await decision:** Stop autonomous storytelling at the decision boundary. No PC speech, movement, acceptance, spending, attack, relationship choice, faction choice or additional player turn occurs automatically.
8. **Process first declaration:** When the player submits, run Declaration → Feasibility → Execution/Uncertainty → Effect → Exposure/Reaction → State Update → Player Control. Return a Core-backed result and then generate the next narration. Existing autonomy and clock processing continue according to adopted Core rules.
9. **Persist/recover:** Reloading the playthrough restores the correct introduction/result and input status; it must not recreate the campaign, repeat NPC effects, grant duplicates, replay opening hooks as fresh events, or advance time again.

The opening is not a pre-recorded cutscene that obliges the player to follow a plot. Optional authored prompts, NPC dialogue and event triggers must remain conditional on the actual campaign state at the moment they are processed.

### 4. Proposed opening lifecycle and concurrency safeguards

Use existing equivalent status/event machinery wherever it exists; the following state names are **logical examples**, not authority to create duplicate state tables:

```text
CHARACTER_DRAFT
    │ approved, validated, atomic unique world commit
    ▼
CAMPAIGN_CREATED
    │ opening context bound to committed world state
    ▼
OPENING_READY
    │ permission-filtered initial view and any Core-valid opening events
    ▼
OPENING_PRESENTED
    │ story text persisted and available to the player
    ▼
AWAITING_PLAYER_INPUT
    │ explicit declaration submitted once
    ▼
ACTION_PROCESSING
    │ Core resolves one request and commits effects once
    ▼
IN_PROGRESS
    └── next meaningful player-control point
```

- `OPENING_PRESENTED` may immediately transition to `AWAITING_PLAYER_INPUT` in one transaction; presentation flags should not become a second game clock.
- Opening generation may fail or time out; it must **not** roll back an already committed campaign or leave the player unable to resume. Show a safe, content-grounded fallback.
- Client retry and double-click on Confirm or the first declaration must return the same committed result, not a second world, duplicate event or second charge.
- Persist `opening_id`, `campaign_state_version`, `scenario_start_id`, `scene_focus_id`, `presentation_status`, `presentation_revision`, `first_player_action_request_id` (when submitted), and source/event references **or comparable existing fields**. Do not persist hidden NPC state in client-visible narrative payloads.
- If pre-existing scenario content or save state does not fit the chosen opening hook, report the conflict, select another **authorized valid hook** or use a neutral accurate environmental opening. Do not silently rewrite the world.
- When multiple players might be present in a future multiplayer design, per-player opening visibility and agency must be separated from global world-state events. This instruction does not add cross-campaign solo points or multiplayer-specific opening mechanics.

### 5. Opening-context contract and information discipline

**Input should derive from actual state** and include, where available:

| Context dimension | Appropriate input |
|---|---|
| Time and location | Exact or qualified world date, scene focus, physical environment, present entities |
| Controlled perspective | Actor or eligible institutional control assignment, actual scope and permissions |
| Biography | Relevant established origins, past experiences, family relationships and known languages; do not re-narrate whole Life-Path |
| Career and service | Existing work/contract/appointment **versus** aspiration/application/unaffiliated status |
| Present NPCs | Identities, observable behaviour, authorized intentions and speech, legitimate relationship histories |
| Situation | Actual nearby activity, pending commitments, known environmental conditions or a scenario-defined potential hook |
| Available actions | Feasible example actions and real inspect commands, filtered by knowledge and authority |
| Knowledge provenance | What was observed, rumoured or received; applicable receipt timestamps and uncertainty |
| Historical plans | **Not player-visible** if not legitimately known; the character cannot preview Agincourt or other future results |

The AI must not invent an earlier voluntary PC choice because the user selected a broad Life-Path category. The player's character might be in an already established place, but cannot be made to walk to a different location, raise a weapon, initiate a conversation, accept a job, pledge service, buy food, decide allegiance, or agree to a marriage merely to complete an introduction.

Avoid railroading through a fixed 'accept quest' contract. The user must be able to leave, refuse, ask questions, observe, pursue another profession, remain civilian, or take any other feasible action. A peaceful day with a market visit or work task is a legitimate beginning.

### 6. Opening profiles and fallback selection

A Starting Scenario may provide an authored opening-profile manifest (names are illustrative):

```yaml
OpeningProfile:
  opening_profile_id: "scenario-scoped, stable"
  scenario_start_id: "linked to actual validated starting checkpoint"
  valid_start_window: "date/time rule; exact or source-qualified"
  required_world_facts: ["only established, verified facts"]
  prohibited_assumptions: ["unearned appointment", "unknown NPC secrets"]
  scene_focus: "existing location and actual initial perspective"
  supported_hook_types:
    - "immediate social interaction"
    - "ordinary work or institutional responsibility"
    - "environmental or public event"
    - "received report or correspondence"
  candidate_participants: "real linked actor IDs, never invented as existing"
  default_first_control_point: "freeform player speech or action"
  fallback: "accurate neutral scene drawn from current state"
  source_provenance: "scenario/content version and event references"
```

Do not mandate a specific number of NPCs, cinematic beats or rolls. Prefer an **actual local interaction** when available; otherwise present a real open situation with an immediately usable input. No fabricated encounter is required to make the game feel dramatic.

### 7. Illustrative openings (noncanonical samples, not license to invent campaign lore)

**A Scot's Tale — 1415 recruitment-yard opening, before sponsorship.** Verify the scenario's **specific opening date in England** instead of inheriting the separate Normandy invasion entry date. Where the starting record establishes Ian in a recruitment yard, the narration could describe the sounds of training, weather and the activity of nearby applicants. A clerk or soldier **only if present or validly initialized** addresses waiting applicants: *“Who seeks service?”* The player may speak, observe, walk away, ask about terms or do something else. **Do not** prewrite Ian's reply, oath, acceptance, voluntary movement, feelings or the later sponsorship by Sir Richard Wycliffe. At a subsequent actual checkpoint, his completed oath/sponsorship may be recognized in state and need not be reenacted.

**Independent mercenary.** A free soldier with no employer receives a grounded scene at their actual location—such as a market, common room, public notice area or hiring ground if it exists—where a legitimate potential lead may be observed. A recruiter or offer is not guaranteed. The player may investigate terms, travel, remain independent or seek civilian work. No faction is assigned through the introduction.

**Civilian merchant or craftsperson.** An existing workplace or market is presented with actual activity and any available order, supply issue, customer approach or ordinary daily choice. A proposed sale is not completed simply because someone speaks. Actual goods, prices and money come from Core and source-backed market knowledge.

**Scholar / natural philosopher.** Present an actual study, workshop, teacher, professional contact or accessible institution when valid. An observation, research problem or request for assistance provides an opening question. No automatic invention, laboratory, patronage, qualifications or modern equipment is awarded.

**Institutional-level perspective.** Open with a scoped, authorized administrative or command briefing derived from real reports, present offices and current pending decisions, with a clear opportunity to issue a lawful order or request more information. Institutional perspective does not imply knowledge of all subjects or the ability to command private property and unaffiliated actors.

The sample hooks are **narrative patterns**, not mandated source facts or forced quest structures.

### 8. Story interface and user interaction

The gameplay shell should implement a recognizable first-scene experience inside **Play → Story**. This is not a new top-level campaign or separate genre engine.

- **Narrative panel:** Show established location/date where known; concise opening prose; NPC utterances attributed to the correct speakers; distinguish observations from reported claims.
- **Player action composer:** Prominent freeform input supporting speech, actions, questions and combined declarations. Optional generated suggestions are never auto-submitted, and must not substitute for free text.
- **Context controls:** Access Character, Inventory, World/Atlas, Chronicle and Saves without losing the opening or advancing time. Show scene-specific knowledge only.
- **Input feedback:** Display preparing, ready, submitting, resolving, recoverable error, and confirmed results without a false success claim.
- **Continuation:** On first valid declaration, narrate the actual Core outcome, NPC reactions and next decision boundary; do not assume the next voluntary player action.
- **Accessible delivery:** Readable layout on desktop/mobile, keyboard navigation, screen-reader live-region discipline, optional skip of decorative transitions, no mandatory cinematic animation, and retained story history.
- **Failure handling:** If the narrator/model is unavailable, a deterministic presenter may construct a minimal opening **only from verified state and approved scenario text**, label any missing capability honestly, and permit a Core-valid first action if the backend supports it. If Core or startup state is unavailable, do not offer a fake playable scene.

When an opening includes a factual NPC utterance or meaningful environmental event, record its occurrence only when actually resolved by the authorized state owner. Re-rendering text from its saved event must not create a new utterance, payment, messenger, injury, or clock increment.

### 9. Acceptance, regression and implementation tests

| Test | Required result |
|---|---|
| Complete a valid new character draft | One unique playthrough is created, Story loads a bounded opening and freeform input is enabled |
| Choose an established historical character | Existing actor ID/history remains unchanged; opening reflects correct current state |
| Choose Quick/Guided/Detailed Life-Path | Each can reach a valid start; creator detail does not change opening authority or invent extra advantages |
| AST recruitment-yard checkpoint | Ian remains Scottish and not yet sponsored; no pre-loaded oath or later relationship |
| AST later checkpoint | Prior actual service history appears only when saved; opening does not replay recruitment as new events |
| Independent mercenary | Opening does not assign a mandatory faction, employment contract or pay |
| Civilian, scholar, or ruler perspective | Opening is professional/perspective-appropriate; no obligatory military recruitment |
| Player refuses the first offered opportunity | Valid refusal is accepted, state responds causally and play continues |
| Player types an unlisted action | Freeform declaration goes to Core; suggestions are not exclusive commands |
| Player changes tabs during opening | Scene and draft/input recover; no time or resource changes solely from navigation |
| Save and reload before first action | Same committed state and opening; no new NPC beat or duplicate initial actors |
| Save and reload after first action | Original action and effects appear exactly once; story resumes at actual point |
| Double-click Confirm / retry network operation | Idempotent creation; no duplicate saves, actor copies or scenario grants |
| Duplicate first-turn request | Exactly one Core event and effect; repeat returns original outcome |
| AI timeout before opening is shown | Existing campaign preserved; safe factual fallback or recoverable error without duplicate world initialization |
| Scenario references absent NPC/asset | Opening rejected/reconciled; no hallucinated state, false contract or forced NPC appearance |
| Character knowledge restriction | Hidden actor motives, future historical event plans and unreceived reports do not leak |
| Opening autonomous NPC act | Actual event recorded in Core with legitimate actor/timing; presentation does not replay it |
| Start date and saved research edition | Exact temporal context retained on launch, reload and retrospective inspection |
| Mobile/keyboard/screen reader | Introduction, first action, error recovery and return navigation remain accessible |

Codex must deliver a demonstrated **creation → opening → player response → Core result → save/reload** slice, not just a screenshot or scripted unconnected chat exchange. In the completion report identify source-backed scene data versus mocked provider text, and **do not call scripted tests playtesting**.

### 10. Development priority and required reconciliation

Place this system inside **Stage One — Playable IRGS**: it is a **blocking user-experience requirement** between atomic playthrough initialization and normal turn-by-turn Story gameplay. Implement the minimum valid opening before broad administrative dashboards, advanced Workshop or marketplace. Reuse existing scene, narration, state and event contracts; do not create a stand-alone opening engine.

**CMRR disposition:** v0.9's 'Confirm & Begin → open Story' remains valid but was functionally incomplete; **expand it into the explicit opening/presentation/first-player-turn state handoff above**. No earlier character-creation, faction independence, conditional-history, six-Director or World-interface requirements are removed. Preserve existing saves; do not retroactively insert an opening into saves already past the first decision. Explicitly version scenario opening profiles when they change.

---

## XI.c — v1.0 Intellectual-Property Provenance, Authorized Distribution & Non-Destructive Replication Protection

**Change source:** Current explicit user direction, 19 October 2026: add protective behaviour so IRGS project materials cannot be casually repackaged by a third party as their own system. **Required interpretation for implementation:** anti-replication **verification, attribution, licensing and safe self-disable of protected platform services**, **not destructive self-wiping code**. This is a security and commercialization design directive, **not** authorization to destroy data on suspicion.

**Status:** Protection intent is user-directed. Concrete licence policy, distribution model, online/offline operation and enforcement terms are unapproved and require later legal/technical review.

### 1. Protection objective and realistic threat model

Protect authorship and source provenance, deter unauthorized redistribution or commercial impersonation, make official builds verifiable, and avoid accidentally enabling unlicensed access to controlled hosted services. Potential threats include public rehosting, rebranding, copied UI/assets, unauthorized modified distributables and theft/misuse of commercial API credentials.

**Do not promise that self-contained source files can detect or prevent all copying.** An adversary with a complete plaintext copy can usually remove purely local licence checks. Reliable enforcement over privately hosted IRGS services must reside on trusted servers and in enforceable agreements; cryptographic checks and provenance marks strengthen detection and attribution but cannot replace a rights strategy.

### 2. Mandatory safety boundaries

**Do not implement any 'self-destruct', sabotage, malware-like or booby-trap functionality that deletes, corrupts, encrypts, overwrites, exfiltrates or damages files, backups, devices or saved games when a copy is suspected.** Do not execute remote shell commands, spread to other systems, silently alter source code, delete user-generated work, destroy developer repositories, install persistence, or trigger destructive operations based on a string/metadata match, missing internet connection, debugger, hostname, copied folder or ownership heuristic.

Never silently delete personal data, player worlds, or legitimate development backups. No concealed, irreversible action against a presumed infringer. Avoid false-positive traps that block authorized local/offline development or create security hazards. Protect legitimate consumer entitlements and respect eventual privacy and legal requirements.

An authorized build failing verification may **decline protected online operations** with a clear non-destructive message and a legitimate support/recovery path; the software should not autonomously attack or erase anything.

### 3. Proposed layered defensive measures

| Control | Intended function | Implementation caution |
|---|---|---|
| **Authorship and licence documentation** | Preserve owner/creator attribution, permitted reuse, rights notices, repository licence and publication terms | Decide precise legal terms with qualified review; do not assert unfiled trademarks or unexecuted agreements |
| **Versioned provenance manifest** | Record build, original source, signed artifact hash, modules, source content owners and released revision | Use existing source and version metadata where available; never contain private signing keys in public files |
| **Signed official builds** | Let users and services verify build integrity and identify authorized distributions | Signing private keys remain protected in a trusted release process; integrity mismatch is not itself proof of theft |
| **Server-side entitlement and identity enforcement** | Protect hosted providers, account APIs, commercial content, publication and paid services | Verify at backend; hiding frontend tabs or adding a browser-only check is not sufficient |
| **Least-privilege credentials** | Keep provider/API keys, signing secrets and deployment credentials out of client-side bundles and exported campaigns | Rotate compromised credentials; avoid public embedded master secrets or hardcoded universal kill switches |
| **Safe licence-state response** | Deny or limit **protected remote services** where authorization is demonstrably invalid | Never tamper with local user data; provide precise errors and recovery/appeal path |
| **Attribution in exports/published content** | Preserve creator credits, derived-work sources and approved IP licence provenance | Contributor credit must follow actual rights and agreements; do not create false ownership claims |
| **Audit/event records** | Record verifiable access denials, publication identity changes and authorization incidents | Minimize personal data; record only what is needed with retention/security controls |
| **Reproducible release checks** | Compare expected product identity, manifest, dependencies and authorised content | Handle normal legitimate developer forks, updates, backups and disaster recovery |

Do **not** silently watermark users' personal documents or collect device identifiers to track alleged copying without a reviewed, disclosed privacy design. Ordinary checks must not access private file contents unrelated to the licensed IRGS operation.

### 4. Safe 'self-disable' behaviour (if later explicitly approved)

Use a **fail-closed server permission decision** rather than an on-disk destructive trap:

```text
Request to use protected IRGS online service
    → authenticate account/build/service principal
    → verify server-side entitlement and applicable scope
    → verify release identity/integrity if that service requires it
    → authorized: execute service request normally
    → unauthorized or revoked: deny protected request, record limited audit,
       return actionable error and approved recovery/support route
    → NEVER alter local source files, saves, unrelated data, backups or devices
```

This gate belongs in relevant **platform/backend services** (publication, account, paid-hosted AI, verified official releases), not in Core simulation, the historical campaign content library, or an NPC/event procedure. Make decisions with reviewed authorization rules rather than probabilistic 'looks copied' guesses. Legitimate offline/local development and recovery should be addressed explicitly before any licence requirement is enabled.

### 5. Protecting campaign state and creator content

The platform must respect the distinction between:

- IRGS-owned Core/software and eligible assigned publisher content;
- third-party licensed or public-domain materials;
- creators' unpublished Workshop drafts, which are **not** silently assigned;
- independently purchased or merged-campaign entitlements;
- user-generated save files and autonomous campaign-state history;
- official or private developer copies and source repositories.

A suspect or invalid build identity must **never** transform creator-owned content into IRGS property, revoke unrelated paid content without valid policy, or make player saves disappear. Content rights, licensing, and authorization should be resolved using actual provenance and valid agreements.

### 6. Current-version Codex work order (minimal, non-destructive)

1. Inventory the repository's current licensing, version fields, source manifests, build IDs, author credits, existing authentication and entitlement logic.
2. Record a **planned** `Build Provenance / License Verification` developer area within the existing feature registry and a relevant **Account / Licences & Distribution** access area. Preserve the existing 'all tabs in development, hide safely for release' rule. Neither tab should pretend a licensing backend is already running.
3. Document a trust-boundary diagram identifying which protective checks are possible only on a trusted server versus signed distribution or local metadata.
4. Preserve source attribution and version information during changes, exports and packaging; reuse existing mechanisms and do not relicense third-party files.
5. Where there is already a working entitlement gate, ensure it fails **non-destructively** and cannot be bypassed by hiding a tab alone.
6. Do **not** activate account lockouts, revoke distribution, invent product keys, require perpetual online access, deploy detection telemetry, or modify existing offline starts without a separate approved threat model and migration plan.
7. Provide a proposal for official-build signing, entitlement verification, incident response, fair recovery, privacy and audits in a later security phase.
8. List unresolved legal terms and technical policy explicitly. Do not claim the system makes copied code impossible to reuse.

### 7. Security acceptance and regression tests

| Test | Expected result |
|---|---|
| Official development build with authorized local backup | Continues functioning; no false-positive destruction or unjustified lockout |
| Modified or unverifiable build attempts restricted hosted API | Server denies only unauthorized protected action; clear error, no file mutation |
| Repeated unauthorized requests | Controlled denial and bounded audit; no runaway process or destructive retaliation |
| Invalid licence / temporary network outage | Data and saves preserved; policy-appropriate recovery/offline handling |
| Signed artifact manifest check | Detects changed integrity without claiming certainty about motive or ownership |
| Browser modifies a local feature flag | Does not grant server-side entitlement or restricted Core access |
| Creator attribution after content export/merge | Preserves actual original sources, contributor permissions and rights provenance |
| Protected service revocation | Does not delete unrelated account content, personal saves, local files, or backups |
| Third-party components | Remain governed by actual upstream licences, not blanket claims of IRGS ownership |
| Developer/admin licence inspection | Secure and access-controlled, not exposed to unauthorized player UI |

**CMRR disposition:** This feature is an **added defensive planning requirement**, not a replacement for the existing ownership/royalty/entitlement system and **not an implemented anti-piracy mechanism**. It must not block the first playable Hundred Years' War vertical slice. No destructive-code insertion, execution, file removal, content deletion or existing-save migration is authorized.

---

## XI.d — v1.0 Integration Status, Source Accounting & Codex Deliverables

### Updated Stage-One definition of done

A verified user can open **Content Library** (before Workshop), see **only The Hundred Years' War**, select a valid historical period and eligible scenario, create or choose a character or authorized institutional perspective, review and **atomically confirm** initial state, **immediately see a brief state-grounded interactive opening**, provide a **freeform** first reply or action, receive the **Core-resolved** consequence and corresponding narration, then save, reload and resume **without duplicate opening events or resources**. Development tabs for all planned features remain reachable but do not impersonate completed systems.

### v1.0 reconciliation summary

| Topic | Prior v0.9 treatment | v1.0 disposition | Ownership/status |
|---|---|---|---|
| Character confirmation → Story | Atomic initialization and enter game | **Expand:** bounded opening scene, causal NPC/world hook, freeform first decision and persistent lifecycle | Core state / Scenario hook / Scene Director / Story UI; new proposed interface requirement |
| Opening behaviour and player agency | General action sequence and scene AI | **Specialize:** no invented PC responses or unearned NPC/contract effects; stop at first voluntary decision | Established agency; new acceptance cases |
| Save/reload at very first turn | General persistence | **Expand:** saved opening presentation and exact-once first-turn effects | Core continuity; implementation to verify |
| Civilian/mercenary/scholar/ruler starts | Supported careers and affiliation freedom | **Retain + expose:** distinct opening hooks, no forced military faction | Campaign content; examples proposed |
| Start-date accuracy / AST | Recruitment vs later checkpoint distinct | **Retain + test** in opening handoff | Historical campaign authority |
| Build ownership and authenticity | Commerce/rights and source provenance | **Expand:** planned non-destructive provenance/licence verification; no self-wiping | Platform security; planned, not implemented |
| Suspected unauthorized copied files | Not previously specified | **Reject destructive response:** deny only protected remote operations under approved policy; preserve all data | Safety/integrity requirement |
| Dev/release navigation | Feature registry for all planned tabs | **Add planned** licences/provenance and opening diagnostics within appropriate existing sections | Frontend registry; shells only where backend absent |
| All archival source volumes | Full four-volume reproduction | **Preserve unchanged:** v1.0 addenda supersede only named integrated lines | Provenance maintained |

### Additional developer-facing routes (current version)

- `Play → Story → Opening`: **contextual runtime state**, not a new top-level tab or a separate campaign; opening is part of Story and should be visible automatically on a new start.
- `Developer → Opening / First-Turn Diagnostics`: actual initialization IDs, state versions, hook selection, presentation status, event/request IDs, observed failures; **strictly authorized** and with secret NPC/history information filtered or isolated from players.
- `Developer → Build Provenance / Licence Verification`: planned feature shell for source/build integrity and future authorized distribution checks, clearly labeled not operational where incomplete.
- `Account → Licences & Distribution`: planned or existing entitlement information, never a fake paid-status or destructive trigger; hide if inappropriate for public release.

### Codex-specific work sequence amendment

1. During audit, locate actual start/confirm functions, scenario loaders, Story renderer, actor and NPC knowledge projections, director/NPC execution, narration and save/load persistence; identify if a functional first scene already exists.
2. Reconcile, extend and test the **new campaign → opening → first player declaration** boundary *before* presenting Stage One as playable. Prefer a bounded, verifiable 1415 case with legitimate dates and an independent civilian/mercenary alternative; do not invent historical facts to populate the demonstration.
3. Verify no second initialization happens when reloading or changing tabs. Record explicit request IDs/event IDs and error recovery behaviour.
4. Add secure planned feature pages for attribution/licence verification and opening diagnostics to the existing single navigation registry without rebuilding the route tree.
5. Preserve commercial, multi-AI, World and Workshop work sequencing: **Playable game + Content Library → Workshop → Marketplace**, with deferred solo-point exchange unchanged.
6. Run all added acceptance cases; report exact passed/failed/manual/unverified status and realistic safeguards rather than claiming anti-copy guarantees or a fully playtested opening.
7. Apply CMRR and resubmit a complete coherent implementation report, source-to-feature matrix, changed files, versioned opening scenario profiles, test evidence, and any migration approval requirements.

**Completion evidence must include both:** (a) at least one verified opening-to-first-action gameplay trace under a mock or live provider, and (b) proof that no destructive anti-copy code was added, while planned provenance/authorization routes accurately reflect their current status.

**v1.0 change log:** Added mandatory short interactive campaign openings and first-turn persistence; added safe, non-destructive IP/provenance and service-authentication planning in response to the requested self-destruct protection; extended Stage-One gates, navigation, acceptance tests and reconciliation; preserved the v0.9 catalogue rule, all original integrated source specifications, six-Director architecture, and deferred universal solo-points feature.

---

---

# XII. Incorporated full source instructions (preserved)

All four original uploaded texts follow in full. These sources retain their original heading hierarchy and contents as archival *source specifications*. When an older source statement conflicts with the reconciled directives above, the explicit reconciliation **above** governs; do not revive a superseded assumption merely because it appears again in a source volume. No extra output file is required to read them.

## Source volumes and integrity manifest

| Volume | Original upload | Source purpose | Lines | Bytes | SHA-256 |
|---|---|---|---:|---:|---|
| A | `writing-block (2).md` | Master Development & Commercial Architecture, v0.7 | 1,394 | 49,212 | `dc8e867ead8011e83efdc831c7827ad3889bbd063ca18a09b1980cb884ccbe74` |
| B | `writing-block (3).md` | Hierarchical Multi-AI Orchestration Network, Foundation v0.1 | 1,095 | 37,636 | `f8f15f09aabba1cc8a3f2b21e26302cd9816173ef93ce653e9743a59676d3be3` |
| C | `Codex_Instructions_Part_1(1).md` | Codex Instructions Part 1: Hundred Years’ War v0.4 + World & Civilization Interface v0.1 | 4,245 | 188,301 | `ab4765d2461553bfff88feb50212ce95d0bb23fdefa57dfdb288670f3ecac308` |
| D | `writing-block (4).md` | Cross-Campaign Currency Exchange & Universal Solo Progression | 308 | 12,616 | `1d1b9f0cfea7ed339ce30a4f6ac5e8cdfe9d23c37ad1f338e76cd2a74d50dd86` |

> The SHA-256 values identify the exact uploaded text copied into the source volumes. Full source contents are reproduced, without semantic deletion or alterations, after this manifest.

---


# SOURCE VOLUME A — Master Development & Commercial Architecture, v0.7

**Original attachment:** `writing-block (2).md`  
**Source status:** Included for provenance and complete implementation detail; apply integrated precedence/reconciliation.

---

# IRGS — Master Development & Commercial Architecture Instructions

**Project:** Interactive Roleplay Game Systems (IRGS)  
**Document:** Integrated Development Direction & Commercial Architecture  
**Revision:** v0.7 — Consolidated Codex Submission  
**Date:** October 19, 2026  
**Authority:** User-directed product decisions, subject to existing adopted IRGS simulation rules  
**Implementation status:** Requirements and design instructions; not a claim of completed implementation or playtesting

---

# PART I — PROJECT DIRECTIVE

## 1. Purpose

IRGS is being developed as a modular, persistent, AI-assisted roleplaying and world-simulation platform.

It must ultimately support:

- Individual character-driven roleplaying.
- Persistent NPC personalities, relationships, memories, and autonomous behaviour.
- Historical, fictional, science-fiction, fantasy, and contemporary settings.
- Social, political, economic, military, institutional, and environmental simulation.
- Campaigns ranging from short, focused experiences to enormous interconnected worlds.
- Multiple AI providers working cooperatively through specialized agents.
- Player-created characters, items, campaign settings, and scenarios.
- A commercial creator marketplace with continuing royalties.
- Creator-approved merging of campaigns into larger playable worlds.

**IRGS must first function as a reliable game before becoming a creator platform or commercial marketplace.**

The long-term development sequence is:

1. **Playable IRGS:** A functional text-based game operating through the existing mock website.
2. **Creation Platform:** Players can develop and play their own campaigns using the Campaign Workshop.
3. **Publishing Platform:** Approved creators can publish, sell, combine, and earn royalties from their work.

Do not reverse this development order.

## 2. Immediate Instructions to Codex

Before implementing changes:

1. Inspect the current IRGS repository and all relevant authoritative project documentation.
2. Include `IRGS_Core_3_3_Live.zip` in the source inventory if available in the workspace.
3. Identify what is already implemented, partially implemented, proposed, accepted, or still missing.
4. Compare these instructions against the existing architecture and adopted rules.
5. Preserve all valid functionality.
6. Identify conflicts, duplication, missing interfaces, incompatible data structures, and potential regressions.
7. Reconcile changes using the project's CMRR procedure.
8. Produce an implementation plan emphasizing the playable text-based runtime.
9. Begin implementation only within the agreed immediate development scope.
10. Document commercial and marketplace architecture for later implementation without prematurely creating the entire business infrastructure.

**Do not rebuild IRGS unnecessarily, discard functioning systems, or substitute a generic chatbot architecture for the simulation engine.**

---

# PART II — FUNDAMENTAL IRGS ARCHITECTURE

## 3. Preserve the Established System Hierarchy

IRGS follows:

**Shared IRGS Core → Genre Foundation/Engine → Setting/Theme Module → Campaign Profile → Campaign State**

### IRGS Core

Owns universally reusable systems and interfaces, including:

- Agency and causality.
- Action declaration and resolution.
- Time and event processing.
- Persistent world state.
- Actors and institutions.
- Information, observation, knowledge, and memory records.
- Social and organizational relationships.
- Economic and resource accounting.
- Equipment, vehicles, logistics, and infrastructure.
- Military and institutional command interfaces.
- Projects, progression, and continuity.
- Applicable shared simulation domains.

### Genre Engines

Implement specialized procedures required by particular genres.

Do not duplicate Core mechanisms unnecessarily.

### Setting/Theme Modules

Supply setting-specific information, technologies, societies, cosmologies, hazards, institutions, and content.

### Campaign Profiles

Define a specific playable campaign's configuration, available starting conditions, enabled mechanics, and permitted overrides.

### Campaign State

Stores the actual evolving world: characters, equipment, resources, institutions, relationships, events, histories, and conditions.

**The AI is not the authoritative simulation engine.**

It may interpret, propose, decide for autonomous actors, and narrate. The Core validates and commits actual state changes.

## 4. Simulation Invariants

Preserve the established operational sequence:

**Declaration → Feasibility → Execution/Uncertainty → Effect → Exposure/Reaction → State Update → Player Control**

Requirements:

- Never invent a player's voluntary actions, speech, intentions, purchases, or decisions.
- Never allow a dice roll or AI judgement to create missing capabilities.
- Qualified routine actions should normally succeed without unnecessary rolls.
- Maintain authoritative time, resources, locations, ownership, injuries, and events.
- Prevent duplicated costs, resources, progress, or casualties.
- NPCs and institutions must act autonomously according to their knowledge, obligations, capabilities, and resources.
- Narration follows simulation; narration cannot secretly alter it.
- Preserve continuity across saves, reloads, time-scale changes, and campaign sessions.

---

# PART III — MULTI-PROVIDER AI INTELLIGENCE SYSTEM

## 5. General AI Philosophy

IRGS should use **the most suitable AI capability for each responsibility**, rather than force one provider or model to perform every task.

The eventual platform should support OpenAI, Anthropic, Google, and compatible local or alternative models through interchangeable provider adapters.

Model assignments must be benchmark-driven.

Do not permanently hardcode a company or model to a specialist role.

For development, OpenAI Codex remains the initial primary implementation tool. Anthropic Claude Code may be used for independent reviews and architectural evaluation, and Google models may be evaluated for large-context or complex reasoning tasks.

For gameplay, model selection should be based on demonstrated performance within IRGS.

## 6. AI Director

Establish an **AI Director** responsible for coordinating specialist intelligences.

Its responsibilities include:

- Understanding the player's declared interaction.
- Identifying which specialists are required.
- Obtaining relevant Core, Genre, setting, and campaign information.
- Delegating work.
- Ordering dependent operations.
- Running independent operations concurrently where safe.
- Resolving workflow dependencies.
- Requesting clarification or specialist revisions when required.
- Managing context and model selection.
- Submitting proposed outcomes for validation.
- Coordinating the final player-facing response.

The Director must operate within deterministic orchestration rules.

It cannot arbitrarily override character decisions, bypass mechanical validation, change player actions, or rewrite authoritative campaign state.

## 7. Specialized AI Responsibilities

Plan the following specialist functions.

These represent logical responsibilities, not a requirement for twelve separate model calls on every interaction.

| Specialist | Responsibility |
|---|---|
| AI Director | Coordination, delegation, context assembly, scheduling, model selection |
| Character Intelligence | Personalities, beliefs, motivations, intentions, autonomous character decisions |
| Dialogue Intelligence | Translation of character intent into natural speech |
| Narrative Intelligence | Environmental description, action narration, atmosphere |
| Scene Director | Scene focus, pacing, interruptions, conversational sequencing |
| Social Intelligence | Relationships, social norms, trust, reputation, interpersonal consequences |
| Strategic Intelligence | Military, political, administrative, and institutional planning |
| World Intelligence | Autonomous societal, political, economic, and environmental developments |
| Knowledge Intelligence | Retrieval and contextual interpretation of appropriate information |
| Memory Intelligence | Organizing character experiences, historical knowledge, and relevant memories |
| Continuity Intelligence | Detecting contradictions and violations of established state |
| Rules Intelligence | Interpreting declarations into applicable Core actions and procedures |

Specialist results must have clearly defined authority and limitations.

## 8. Character Intelligence and Dialogue Intelligence Must Remain Separate

This is a fundamental design requirement.

### Character Intelligence determines:

- What the character knows.
- What the character believes.
- What the character feels.
- What the character wants.
- What the character decides.
- What the character intends to communicate.
- What information the character conceals.
- Whether the character is truthful, deceptive, uncertain, conflicted, or mistaken.

### Dialogue Intelligence determines:

- The words the character uses.
- Speech patterns.
- Vocabulary and language.
- Accent or dialect where appropriate.
- Tone and verbal delivery.
- Expressions of subtext.
- Socially and culturally appropriate phrasing.

Dialogue Intelligence must not change the character's underlying decision.

Narrative Intelligence then describes the scene using the validated action and dialogue information.

The narration cannot invent new motives, change decisions, create physical results, or alter established circumstances.

## 9. Persistent Character Cognition

Characters need persistent profiles independently stored by IRGS.

These should cover:

- Identity and background.
- Personality and temperament.
- Goals and aspirations.
- Values and beliefs.
- Knowledge and misconceptions.
- Emotional and psychological conditions.
- Relationships.
- Personal history and significant memories.
- Behavioural patterns.
- Current responsibilities and obligations.
- Private knowledge and secrets.

A model receives the relevant authorized context when the character participates in an interaction.

Do not rely on an AI provider's conversational memory as the authoritative record.

Different characters must not receive information they could not reasonably possess.

Character knowledge must remain separate from the full campaign world's factual state.

## 10. Provider Gateway and Capability Registry

Build toward a provider-independent gateway.

It should support:

- Model/provider registration.
- Specialist role assignments.
- Structured requests and responses.
- Context assembly.
- Tool and Core access permissions.
- Fallback handling.
- Performance measurement.
- Cost accounting.
- Model comparison.
- Provider replacement without campaign-data migration.

Maintain a capability registry recording measured performance for relevant tasks, including characterization, dialogue, narrative quality, strategic reasoning, continuity, structured-output reliability, latency, and cost.

Use actual IRGS benchmark results, not marketing claims, to determine the eventual preferred model for each function.

## 11. AI Cost and Execution Control

A complicated player action might activate several specialist agents.

That must not automatically consume multiple player turns.

Distinguish:

- Player-facing gameplay turns.
- Internal AI agent operations.
- Core simulation operations.
- Tokens and actual model billing.
- Retried or rejected AI operations.

The AI Director should activate only the necessary specialists.

Routine tasks should not require expensive collaborative reasoning where simpler processing is adequate.

However, cheaper gameplay-access tiers must not receive inferior narrative quality, missing mechanics, or reduced simulation fidelity.

Optimize execution rather than degrading the purchased experience.

---

# PART IV — CAMPAIGN CLASSIFICATION

## 12. Official Five-Tier Campaign Hierarchy

The campaign classification system is:

**Short Story → Curated Campaign → Full Campaign → Major Campaign → Grand Campaign**

The established consolidation ratios are:

- **6 Short Stories = 1 Curated Campaign**
- **8 Curated Campaigns = 1 Full Campaign**
- **3 Full Campaigns = 1 Major Campaign**
- **2 Major Campaigns = 1 Grand Campaign**

### Cumulative Equivalencies

| Campaign Type | Equivalent Short Stories |
|---|---:|
| Short Story | 1 |
| Curated Campaign | 6 |
| Full Campaign | 48 |
| Major Campaign | 144 |
| Grand Campaign | 288 |

These represent structural consolidation ratios and intended scope equivalencies.

They do not require every directly authored campaign to be assembled from separately published lower-tier products.

A directly authored Major Campaign may be developed from scratch if it satisfies the eventual Major Campaign scope and quality requirements.

Numerical equivalence alone does not guarantee classification. Repetitive filler, duplicated content, or mechanically disconnected material must not qualify a product for a higher category.

## 13. Publication Authority

| Campaign Classification | Permitted Production |
|---|---|
| Grand Campaign | IRGS |
| Major Campaign | IRGS standalone or IRGS–creator collaborative |
| Full Campaign | IRGS or independent creators |
| Curated Campaign | IRGS or independent creators |
| Short Story | IRGS or independent creators |

**Major Campaigns are not required to be collaborative.**

IRGS may develop and publish them independently.

Grand Campaigns remain IRGS productions, although they may incorporate creator-contributed material through approved arrangements.

## 14. Proposed Pricing Brackets

The preliminary marketplace price ranges are:

- Short Story: Free or a few dollars.
- Curated Campaign: Approximately $10–15.
- Full Campaign: $20 or more.
- Major Campaign: Undetermined.
- Grand Campaign: Undetermined.

These are planning brackets, not calibrated final prices.

Do not invent mandatory price ceilings, floors, or release schedules beyond these directions.

IRGS intends to release smaller experiences more frequently and larger campaigns less frequently.

---

# PART V — BASE-GAME ACCESS AND MONETIZATION

## 15. Permanent Base-Game Purchase

IRGS is intended to use an affordable, one-time purchase model.

A player purchases base access once.

The purchase includes:

- Access to the IRGS gameplay platform.
- A starter selection of campaigns.
- Selected entry points within those campaigns.
- A generous but limited gameplay-turn allowance.
- The campaign-free character creator.
- Basic reusable character and item/template creation tools.

Additional campaigns and entry points may be purchased separately.

A purchase establishes a persistent ownership entitlement to the purchased product.

Do not interpret permanent ownership as unlimited, unmetered AI inference.

Service availability and eventual shutdown policies require separate legal and operational specifications.

## 16. Campaign and Entry-Point Purchases

Support:

- Individual campaign entry-point purchases.
- Groups of entry points.
- Complete campaigns.
- Ownership-aware upgrades to complete campaigns.

If someone owns several entry points and purchases the remaining campaign content, previously purchased entitlements must be recognized.

The player should receive the appropriate completion discount or adjustment rather than paying again for already owned content.

The exact pricing algorithm remains to be calibrated.

Do not apply this upgrade logic automatically between separate merged campaigns and their source campaigns.

## 17. Gameplay Access Tiers and Enforced Rest

Players may purchase different gameplay-access tiers.

These tiers affect how long a player can play before an enforced **Rest** is required.

They must not affect:

- Available mechanics.
- Owned campaign content.
- AI character intelligence.
- Narrative quality.
- Simulation accuracy.
- Access to features that belong to purchased campaign content.

Higher access tiers provide larger usage allowances or longer uninterrupted play periods.

Exact allowances, refill schedules, Rest durations, tier prices, and upgrade procedures remain undecided.

### Rest Rules

An enforced account Rest is not an in-world action.

It must never automatically:

- Advance campaign time.
- Cause the player character to sleep.
- Heal injuries.
- Replenish resources.
- Complete projects.
- Trigger undeclared character actions.
- Reset campaign conditions.

Gameplay state remains preserved.

Usage accounting should be enforced consistently at the appropriate account level, rather than bypassed simply by changing campaigns.

---

# PART VI — CAMPAIGN WORKSHOP

## 18. Workshop Philosophy

The Campaign Workshop is a future paid authoring system that allows players to create their own campaigns.

The user must first be able to play IRGS reliably before these tools become a development priority.

Separate basic player creation tools from campaign authoring.

The campaign-free character creator remains included in the base purchase.

Basic item and character templates should also be available without requiring full Campaign Workshop ownership.

The exact boundary between free and premium secondary authoring tools remains open.

## 19. Workshop Access

The Workshop should support a commercial structure involving:

- Paid Workshop access.
- Usage-time allowances.
- Purchased credits.
- Optional Workshop tiers.
- Purchasable expansion packs.

Workshop ownership, authoring time, and AI-assisted creation credits must be separately accounted for.

Manual editing and local configuration should not automatically consume AI generation credits.

Any metered operation must declare its cost.

Do not accidentally charge multiple allowances for the same action unless explicitly authorized under a published policy.

Exact prices and allowance formulas are not yet established.

## 20. Text-Based Authoring and Content Reuse

The initial Workshop should be primarily text-based.

Creators will receive controlled access to backend authoring functions through approved interfaces.

They will primarily work by selecting, copying, renaming, modifying, repurposing, and combining existing supported content.

Examples include:

- Character templates.
- Item and equipment templates.
- Settlements.
- Governments.
- Institutions and factions.
- Historical or fictional geography.
- Organizational structures.
- Campaign profiles.
- Starting conditions.
- Entry points.
- Supported setting content.

Support explicit operations such as:

**Reference, Clone, Modify, Override, Extend.**

Editing a copied template must not alter its original shared source.

Creators must not receive unrestricted access to production databases, other players' campaign states, proprietary engine code, or unauthorized content.

The Workshop generates campaign data and configuration. It does not create a competing simulation engine.

## 21. Workshop Expansion Packs

Optional packs may contain:

- Additional content libraries.
- Specialized templates.
- More sophisticated authoring interfaces.
- Historical or genre-specific authoring resources.
- Mapping and organizational design tools.
- Advanced creation aids.

These packs should supplement creation rather than sell access to missing fundamental mechanics.

Campaigns created using approved Workshop facilities must operate through the existing IRGS Core and relevant Genre Engines.

---

# PART VII — CREATOR MARKETPLACE

## 22. Marketplace Purpose

Once the playable game and personal Workshop are established, IRGS will support creator publishing.

Creators can submit completed campaigns for review.

Approved publications may be offered for sale through the IRGS storefront.

The marketplace is intended to:

- Increase the number and variety of playable campaigns.
- Compensate creators.
- Provide continuing revenue opportunities.
- Expand the content catalogue.
- Enable IRGS to acquire original creative properties.
- Support collaborative and merged campaign development.

Marketplace publication is not an automatic consequence of creating a campaign.

Submission, validation, rights transfer, and publication approval are distinct stages.

## 23. Creator Revenue Sharing

The standard split for eligible independently creator-published content is:

**80% Creator / 20% IRGS**

This supersedes all earlier 88/12 proposals.

The split applies to defined distributable proceeds.

For provisional financial modeling:

**Distributable proceeds = eligible collected sales revenue − applicable taxes − payment/distribution fees − refunds/reversals.**

The exact legally binding definition requires further development.

IRGS must not invent undisclosed discretionary deductions.

The creator's 80% is a persistent contractual royalty entitlement on qualifying sales of their published content.

The creator's share does not disappear merely because they stop actively developing, stop using the Workshop, or cease releasing new material.

Refunds, reversals, payment fees, and payout records must be reconciled accurately.

IRGS's 20% contributes to marketplace infrastructure, content review, administration, support, and operating expenses.

It is not automatically net profit.

## 24. Creator-Content Ownership

IRGS intends to acquire ownership of eligible published creator content.

As part of the creator publication agreement:

1. The creator assigns ownership of specifically identified original published content to IRGS.
2. The creator receives the agreed continuing royalty entitlement.
3. IRGS receives creative reuse rights over the assigned content.
4. The creator receives clearly defined intellectual-property rights granted back through the agreement.
5. Attribution, permitted independent reuse, adaptation rights, and other protections must be documented.
6. Third-party content cannot convey rights the creator does not possess.

This transfer applies to specifically identified accepted published content.

It must not silently transfer ownership of:

- Unpublished Workshop drafts.
- Unrelated personal creations.
- Content never submitted or accepted.
- Third-party assets.
- Existing material outside the agreed assignment.

The creator's license-back and moral-right provisions require qualified legal drafting.

**Do not assume that a copyright assignment automatically grants the creator unrestricted continued rights. Those rights must be expressly established in the agreement.**

## 25. IRGS Reuse of Creator Content

IRGS may selectively reuse eligible acquired creative material in other IRGS publications.

Potential examples:

- Characters.
- Items and equipment.
- Locations and settlements.
- Organizations.
- Institutions.
- Fictional historical details.
- Other acquired original creative material.

An IRGS campaign could include a creator-developed merchant, building, settlement, or item without incorporating the creator's entire original campaign.

Selective creative reuse is distinct from wholesale republication or commercial packaging.

IRGS must not rename and resell an essentially unchanged creator campaign merely to bypass its royalty arrangements.

Original campaign sales continue to use their original royalty agreement.

Downstream royalties for selective reuse versus substantial republication need explicit contractual definitions.

Do not assume that incidental appearance of one acquired character automatically entitles the original creator to 80% of the entire subsequent IRGS product.

## 26. Trademark Protection

IRGS requires an intellectual-property protection strategy.

Investigate trademark clearance and registration for:

- IRGS.
- Interactive Roleplay Game Systems.
- The eventual distinctive brand logo.

The exact registration owner, legal jurisdictions, filing strategy, and availability must be verified.

Do not assume trademark registration is already completed or that the name is legally available.

Obtain professional legal review before finalizing marketplace copyright and trademark arrangements.

---

# PART VIII — CAMPAIGN MERGING AND PACKAGING

## 27. Campaign Packaging System

IRGS must eventually support the consensual combination of previously published creator campaigns into larger integrated campaign products.

The resulting product is called a **Merged Campaign** for assembly and publishing purposes.

Merged Campaign is not a sixth campaign classification.

The completed product is classified as Short Story, Curated, Full, Major, or Grand according to its valid scope.

Campaign packaging requires:

- Creator consent.
- Defined source contributions.
- Negotiated contributor royalties.
- IRGS integration work where needed.
- A new publication identity.
- A new ownership entitlement.
- Separate campaign state and continuity.
- Contributor attribution.

## 28. Explicit Consent

Every contributing creator must consent to the proposed merged publication.

This requirement applies even though IRGS owns the eligible previously published content.

Creator agreement to an original publication does not automatically authorize inclusion of the entire original campaign in a subsequent monetized merged campaign.

Consent must be specific to the proposed package and its terms.

If a creator refuses, their campaign cannot be included in that proposed package.

IRGS may revise the package and seek new agreements.

## 29. Negotiated Shared Royalties

Merged campaigns retain the standard combined distribution:

**80% to contributing creators / 20% to IRGS.**

Each creator's share of the collective 80% is negotiated and explicitly approved.

Equal shares are allowed but not mandatory.

IRGS retains 20% even when it performs substantial additional integration work to make the merged campaign function.

Individual allocations must sum to the agreed total.

Implement exact accounting, validation, and deterministic rounding.

Do not publish a package whose contributor distribution is incomplete, invalid, or unapproved.

## 30. Example — The Eight Realms of Mertup

Eight independent creators each publish one Curated Campaign.

The source campaigns focus primarily on their own locations and contain relatively little information about surrounding territories.

IRGS proposes integrating them into a single Full Campaign:

**The Eight Realms of Mertup**

The work may involve:

- Positioning the eight locations on one map.
- Establishing distances and travel routes.
- Connecting trade networks.
- Reconciling political institutions.
- Establishing interregional relationships.
- Resolving incompatible timelines.
- Integrating history and starting circumstances.
- Making the world function through one shared simulation state.

All eight creators consent.

For this example, the creators agree to equal shares:

| Recipient | Share |
|---|---:|
| Creator A | 10% |
| Creator B | 10% |
| Creator C | 10% |
| Creator D | 10% |
| Creator E | 10% |
| Creator F | 10% |
| Creator G | 10% |
| Creator H | 10% |
| IRGS | 20% |
| **Total** | **100%** |

This allocation is specific to the example.

It must not become an automatic formula for every merged campaign.

## 31. Merged Campaign Ownership and Entitlements

**This is an explicit, important ownership rule.**

The Eight Realms of Mertup is a new, separate product from its eight original Curated Campaigns.

Purchasing Mertup grants access to Mertup as an integrated playable campaign.

It does **not** grant separate ownership of the eight source Curated Campaign products.

Likewise, purchasing all eight original Curated Campaigns does not automatically unlock Mertup.

Example:

| Purchase | Granted Access |
|---|---|
| Curated Campaign A | Curated Campaign A |
| Curated Campaign B | Curated Campaign B |
| All eight original Curated Campaigns | Eight independently playable campaigns |
| The Eight Realms of Mertup | The merged Mertup campaign only |
| All originals and Mertup | All nine separately owned products |

All material necessary to play the merged campaign must be included through the merged product's own content package and runtime dependencies.

No automatic standalone source-campaign entitlements are created.

No automatic cross-product ownership discounts are assumed.

Future special promotions would require separately defined commercial rules.

## 32. Contributor Attribution

A merged campaign's storefront description must credit its contributing creators and identify their original works.

For example:

**The Eight Realms of Mertup**

*Full Campaign — Published by IRGS*

Contributors:

- Creator A — Original Curated Campaign A.
- Creator B — Original Curated Campaign B.
- Creator C — Original Curated Campaign C.
- Creator D — Original Curated Campaign D.
- Creator E — Original Curated Campaign E.
- Creator F — Original Curated Campaign F.
- Creator G — Original Curated Campaign G.
- Creator H — Original Curated Campaign H.

Original campaigns remain separately available where still listed.

The listing should clearly state that purchasing the merged campaign does not grant individual ownership of the original publications.

Storefront references may link to the contributing products.

## 33. Independent Campaign Continuity

Merged campaigns must maintain their own independent starting configuration and evolving state.

They must not silently overwrite or rewrite the source campaigns.

For example:

- A player starts the original Campaign A.
- Another player starts Mertup.
- Both products may contain a version of the same fictional character.
- Events affecting that character in one campaign do not automatically affect the other.

Content provenance may identify the shared creative origin, but campaign state remains separate.

Likewise, a source campaign's future update must not automatically alter an already published merged campaign.

Changes require explicit version integration and compatible migration policies.

## 34. Larger Consolidations and Successive Packaging

A merged campaign may subsequently be considered for integration into an even larger product.

Examples:

- Six Short Stories may form a Curated Campaign.
- Eight Curated Campaigns may form a Full Campaign.
- Three Full Campaigns may form a Major Campaign.
- Two Major Campaigns may form a Grand Campaign.

However, consent does not automatically propagate upward.

Approval for a Full Campaign merger does not authorize that Full Campaign's later inclusion in a Major or Grand Campaign without the required new agreements.

Contributing source works, royalty allocations, licensing, and publication rights must be reconciled for each new package.

Do not count duplicated content as multiple independent contributions toward higher classification thresholds.

---

# PART IX — MARKETPLACE, RIGHTS, AND ACCOUNTING INFRASTRUCTURE

## 35. Required Future Systems

Design interfaces for the following systems, but do not prioritize full implementation before the game is functional.

### Commerce System

Responsible for:

- Product prices.
- Purchases.
- Discounts.
- Bundles.
- Refunds.
- Transaction records.

### Entitlement Registry

Responsible for:

- Base-game ownership.
- Campaign ownership.
- Entry-point ownership.
- Campaign Workshop access.
- Expansion-pack ownership.
- Merged-product ownership.

### Campaign Catalogue

Responsible for:

- Campaign identity.
- Classification.
- Official or creator publication status.
- Entry points.
- Dependencies.
- Versions.
- Contributor listings.

### Campaign Workshop Services

Responsible for:

- Authoring projects.
- Templates.
- Cloned content.
- Configuration.
- AI-assisted authoring.
- Usage-time and credit accounting.

### Submission and Review System

Responsible for:

- Creator submissions.
- Validation.
- Rights declarations.
- Approval or rejection.
- Resubmission.
- Publication readiness.

### Creator Royalty Ledger

Responsible for:

- Creator identities.
- Publication agreements.
- Source and merged-product allocations.
- Eligible revenue.
- Refund reversals.
- Accrued royalties.
- Payout balances.
- Payment history.

### Campaign Packaging System

Responsible for:

- Source publication references.
- Contributor consent.
- Negotiated royalty allocations.
- Content provenance.
- Integrated campaign configuration.
- New product publication.

### AI Consumption Ledger

Responsible for:

- Model/provider usage.
- AI specialist invocations.
- Token and inference costs.
- Retries and caching.
- Gameplay and authoring usage.
- Internal cost allocation.

These systems must maintain separate authoritative records.

Do not derive financial liabilities solely from storefront summaries.

Do not permit duplicate payments, duplicate entitlements, or duplicate resource accounting.

## 36. Source Attribution and Reuse Rights

Every reusable content resource should eventually identify:

- Unique content identity.
- Original creator/source.
- Publication version.
- Current rights holder.
- Relevant licensing restrictions.
- Allowed reuse operations.
- Source campaign, if applicable.
- Derived or adapted content relationships.

Distinguish:

- Owned content.
- Licensed content.
- Public-domain content.
- Internal templates.
- Acquired creator content.
- Restricted third-party content.

IRGS cannot acquire or distribute rights that the submitting creator does not possess.

## 37. Publication Updates

Published content must be versioned.

Updating a product does not automatically migrate an active player's campaign state.

Creators and IRGS should be able to publish compatible corrections and improvements through controlled procedures.

Breaking changes require explicit compatibility and migration treatment.

A delisted product and an invalidated ownership entitlement are not automatically the same thing.

Existing purchaser rights and accrued royalties must be considered before changing availability.

---

# PART X — FINANCIAL SUSTAINABILITY

## 38. Revenue Sources

The intended long-term revenue model includes:

1. One-time base-game purchases.
2. Official campaign purchases.
3. Individual campaign entry points and entry-point bundles.
4. Gameplay access-tier upgrades.
5. Paid Campaign Workshop access.
6. Workshop usage-time and credit purchases.
7. Workshop expansion packs.
8. Creator marketplace sales, from which IRGS receives 20% of eligible proceeds.
9. Creator-consented merged campaigns and packaged products.

No mandatory subscription model has been adopted.

## 39. Cost Management

IRGS uses online AI services that can produce recurring operating costs.

A permanent purchase must not be mistaken for permission to consume unlimited inference resources indefinitely.

The business architecture must model:

- Average AI expense per player turn.
- Average AI expense per creation task.
- Number of specialist agents activated.
- Active-player usage patterns.
- Gameplay tier consumption.
- Hosting and data-storage costs.
- Transaction processing.
- Content-review costs.
- Creator payout liabilities.
- Continuing expenses associated with existing customers.

New campaign sales may support ongoing operations, but the platform must not depend exclusively on perpetual growth in new purchasers to remain viable.

Track costs and revenue by appropriate cohort, product, and operation.

Do not invent final prices or allowance limits until representative workloads have been measured.

---

# PART XI — DEVELOPMENT ROADMAP

## 40. Stage One — Playable IRGS

**Highest current priority.**

Develop a fully functional text-based IRGS experience through the existing mock website.

The user should be able to:

1. Open the website.
2. Create or select a character.
3. Select an available campaign and entry point.
4. Enter the simulated world.
5. Interact with NPCs.
6. Declare actions.
7. Experience validated simulation consequences.
8. Save and continue the campaign later.

The initial AI integration should be able to use OpenAI as the first operational provider.

Its tasks should be separated into the appropriate logical functions, with the architecture prepared for future specialist and provider expansion.

For the initial version, specialist functions may share one underlying model when doing so is practical.

Do not require the entire future AI ensemble before gameplay can function.

The website must communicate with a real simulation backend.

The authoritative Core—not the AI's response text—must maintain character state, game time, resources, and campaign history.

A persistent backend API integration is required for the model to operate within the website; an independent ChatGPT conversation is not itself the website runtime.

### Minimum Stage-One Capabilities

- Character creation.
- Background and affiliation independence.
- Campaign entry selection.
- Valid action processing.
- Time progression.
- NPC interaction.
- NPC autonomous behaviour.
- Resource and inventory tracking.
- State persistence.
- Campaign continuation.
- AI narration.
- Diagnostic and error logging.
- Automated regression tests.

Use existing campaigns, including A Scot's Tale where appropriate, as integration and characterization test material.

Also maintain smaller controlled test scenarios with completely known starting states for mechanical validation.

## 41. Stage Two — Personal Campaign Workshop

After the playable runtime is sufficiently reliable:

- Expose supported creation tools.
- Allow personal campaign profiles.
- Support reusable and cloned content.
- Allow creation of entry points.
- Support controlled worldbuilding and campaign configuration.
- Allow users to test their own campaigns.
- Introduce the Workshop's intended usage and credit systems as needed.

Public commercial publishing is not necessary for Stage Two.

## 42. Stage Three — Creator Marketplace

Only after the game and authoring infrastructure are functional:

- Add creator accounts.
- Implement publication submissions.
- Implement content validation and review.
- Finalize rights-transfer and licensing agreements.
- Implement product entitlements.
- Implement the 80/20 royalty system.
- Establish creator payouts.
- Launch approved creator publications.
- Introduce creator-consented campaign packaging.
- Support negotiated multi-creator royalties.

The marketplace must not be allowed to destabilize the simulation runtime.

---

# PART XII — ACCEPTANCE TESTS AND STRESS TESTING

## 43. Gameplay Tests

Test:

- Routine actions.
- Consequential uncertainty.
- Impossible actions.
- Resource scarcity.
- NPC autonomy.
- Player agency.
- Mixed outcomes.
- Simultaneous events.
- Timeline continuity.
- Save/reload behaviour.
- Time-scale transitions.
- Resource conservation.
- Military and institutional authority.
- Character knowledge restrictions.
- AI dialogue preserving intended meaning.
- Narration preserving validated outcomes.

No unresolved critical state-accounting errors should remain in the first playable release.

## 44. Multi-Agent Tests

Verify that:

- The Director delegates to the correct roles.
- Character Intelligence can produce decisions without writing player-facing prose.
- Dialogue Intelligence preserves the character's intent.
- Narrative Intelligence does not modify validated outcomes.
- Agents cannot access unauthorized character knowledge.
- Specialist calls do not automatically consume multiple player turns.
- Failed model calls do not commit partial or duplicate changes.
- Provider changes do not alter authoritative campaign records.
- Model routing remains cost-observable.
- Concurrency does not cause conflicting state commits.

## 45. Commercial Tests

Verify that:

- Owned content is not charged as a new entitlement twice.
- Entry-point upgrades account for existing ownership.
- Gameplay tiers change allowances without locking content.
- Enforced Rest preserves simulation state.
- Workshop time and credits are not unintentionally double charged.
- Refunds reverse appropriate financial liabilities.
- Creator royalties are calculated from the authorized proceeds definition.
- Multiple contributors' allocations total the required amount.
- Royalty entitlements continue according to their agreements.
- A purchase cannot create duplicate entitlements.

## 46. Packaging Tests

Use The Eight Realms of Mertup as a reference test.

Verify that:

1. Eight Curated Campaigns can be integrated into one Full Campaign.
2. Every source creator explicitly consents.
3. Each creator approves their agreed royalty allocation.
4. The eight example creators each receive 10% of eligible proceeds.
5. IRGS retains 20%, even after performing integration work.
6. The original eight campaigns remain independent products.
7. Purchasing Mertup does not unlock their standalone source campaigns.
8. Purchasing the original eight does not automatically unlock Mertup.
9. The storefront credits all contributors and identifies their original works.
10. Geography, travel, politics, economy, and chronology operate as one coherent integrated campaign.
11. Changes within Mertup do not alter the source campaigns' independent states.
12. A subsequent larger merger requires its own contributor agreements.
13. Changes to royalty allocations cannot occur without required approval.
14. Source publication updates do not silently rewrite the merged campaign.
15. Content reused in Mertup retains accurate rights and provenance records.

## 47. Economic Stress Testing

Test low, moderate, and extreme scenarios involving:

- Players who purchase only the base game.
- Highly active lifetime customers.
- Players who purchase many campaigns.
- Expensive multi-agent interactions.
- Popular free Short Stories.
- Workshop users generating high volumes of AI-assisted content.
- Low-priced marketplace transactions.
- Refunded purchases.
- Large creator royalty obligations.
- Multiple simultaneous users.
- Slowdowns in new customer purchases.
- Continued activity from customers who make no further purchases.

Calculate actual cost and contribution margins before deciding final allowances, prices, and tiers.

Consistency of the formulas is not proof of commercial sustainability.

---

# PART XIII — REQUIREMENTS STATUS AND OPEN DECISIONS

## 48. User-Directed Requirements to Preserve

The following should be treated as current product requirements:

- IRGS is simulation-first.
- The Core retains authoritative state.
- Multiple AI providers and specialized AI agents are desired.
- The AI Director coordinates specialists.
- Character intention and dialogue expression are separate functions.
- The base game is a one-time purchase.
- Gameplay access tiers affect play duration/Rest, not content quality or mechanics.
- Basic campaign-free character creation remains included.
- Official and creator campaigns use the five-tier hierarchy.
- Campaign equivalencies are 6:1, 8:1, 3:1, and 2:1.
- Major Campaigns can be standalone IRGS productions or collaborations.
- IRGS obtains ownership of eligible creator-published content through agreed assignment.
- Creators receive continuing 80% royalties from eligible original publication proceeds.
- IRGS retains 20%.
- IRGS may selectively reuse acquired original content in its own works.
- Wholesale campaign packaging requires contributor consent.
- Merged-campaign contributor allocations are negotiated individually.
- The collective creator share of an eligible merged campaign remains 80%.
- IRGS retains 20% even when it performs the integration work.
- Merged campaigns are separate commercial products from their sources.
- Purchasing merged campaigns does not grant standalone ownership of source campaigns.
- Contributors and source works are credited in merged-product descriptions.
- Campaign Workshop creation initially emphasizes controlled text-based authoring and reusable templates.
- Gameplay must work before the Workshop and marketplace are prioritized.

## 49. Matters Requiring Further Decisions

Do not invent final policies for:

- Base-game price.
- Exact gameplay-turn allowances.
- Rest duration and replenishment.
- Gameplay access-tier prices.
- Workshop purchase prices.
- Workshop usage-time and credit formulas.
- Expansion-pack prices.
- Final campaign classification scope standards.
- Major and Grand Campaign prices.
- Creator submission requirements and review procedures.
- Detailed copyright assignment and license-back provisions.
- Moral-rights and attribution terms.
- Exact royalty proceeds definition.
- Creator payout schedules and thresholds.
- Refund and dispute policies.
- Downstream royalties for major reuse outside negotiated packages.
- Collaborator compensation in standalone collaborative Major Campaigns.
- Legal trademark filing and registration.
- Final provider/model assignments.
- Publishing and hosting service guarantees.

Document unresolved decisions explicitly.

Do not silently convert proposals into adopted rules.

---

# PART XIV — CMRR RECONCILIATION AND CODEX DELIVERABLES

## 50. Required Reconciliation

Apply:

**Compare → Merge → Reconcile → Resubmit**

Identify:

- Existing source authority.
- Already implemented mechanisms.
- Missing capabilities.
- Superseded proposals.
- Conflicts.
- Duplicate ownership of functionality.
- Necessary new interfaces.
- Potential regressions.
- Migration requirements.
- Acceptance tests.
- Calibration gaps.

Explicitly recognize the following corrections:

| Superseded assumption | Current direction |
|---|---|
| 88% creator / 12% IRGS | 80% creator / 20% IRGS |
| Major Campaigns must be collaborative | Major Campaigns may be IRGS standalone or collaborative |
| Creator retains ownership of all published content | IRGS acquires identified published content through assignment, with defined creator rights and royalties |
| Creator campaign reuse and packaging are equivalent | Incidental selective reuse and monetized campaign packaging have distinct rules |
| A merged campaign might grant standalone source ownership | Merged campaigns grant no automatic source-product entitlements |
| Campaign size categories have no precise equivalencies | Formal 6:1, 8:1, 3:1, and 2:1 hierarchy |
| Marketplace development should begin early | Playable website runtime first, personal Workshop second, marketplace third |
| All AI tasks belong to a single model | Multi-provider specialist architecture directed through an AI coordination system |

Do not revive superseded assumptions.

## 51. Requested Outputs From Codex

After inspecting the real project sources, produce:

### A. Current State Assessment

Explain which required systems are:

- Implemented.
- Partially implemented.
- Documented but not coded.
- Missing.
- Inconsistent with adopted architecture.

Cite exact repository files, functions, modules, or specifications where possible.

### B. Architecture Reconciliation

Map all affected systems to the proper ownership layers.

Do not duplicate simulation mechanics within AI agents, campaign content, or commerce services.

### C. Updated Development Plan

Provide a practical, dependency-aware implementation sequence beginning with the text-based mock-website runtime.

Distinguish immediate engineering tasks from future commercial architecture.

### D. Stage-One Implementation

Implement or repair the minimum components needed for actual gameplay, subject to the existing repository's condition and established rules.

Preserve current data and working functionality.

### E. Test Results

Provide automated test results where tests were actually executed.

Clearly separate:

- Designed acceptance cases.
- Scripted tests.
- Simulated test cases.
- Actual playtesting.
- Calibrated mechanics.

Never claim something was validated merely because it was documented.

### F. Change Log and Migration Impact

Record what was added, changed, moved, preserved, or deprecated.

Identify any changes requiring migration.

Do not silently migrate existing campaign states or change their history.

### G. Outstanding Decisions

List unresolved business, legal, financial, and technical decisions without fabricating answers.

---

# FINAL ENGINEERING DIRECTIVE

IRGS must be constructed as a coherent, modular simulation platform with a provider-independent AI intelligence layer.

Its commercial future includes permanent game purchases, official campaigns, player creation tools, creator publishing, ongoing royalties, acquired creative intellectual property, and consensual consolidation of independent campaigns into larger worlds.

However, none of these commercial ambitions should obscure the immediate engineering goal:

**Build a reliable, persistent, text-based IRGS experience that players can actually use through the existing mock website.**

First prove the simulation.

Then enable people to create with it.

Finally enable creators to publish, collaborate, and earn continuing royalties through it.

Preserve the existing Core architecture, player agency, world-state integrity, content provenance, and every accepted design decision.

**Do not implement an attractive storefront around an unfinished game. Build the game first, while ensuring that its architecture can support the complete IRGS ecosystem later.**

---

**End of Codex Master Instruction — v0.7**


---


# SOURCE VOLUME B — Hierarchical Multi-AI Orchestration Network, Foundation v0.1

**Original attachment:** `writing-block (3).md`  
**Source status:** Included for provenance and complete implementation detail; apply integrated precedence/reconciliation.

---

# IRGS — Hierarchical Multi-AI Orchestration Network
## Codex Implementation Directive — Foundation v0.1

**Project:** Interactive Roleplay Game Systems (IRGS)  
**Task:** Implement the foundational architecture for a hierarchical, multi-provider, multi-agent AI network integrated into the existing IRGS platform.  
**Priority:** Core architectural groundwork, extensibility, compatibility, simulation integrity, and a functional website management interface.

---

# 1. Project Objective

IRGS is being developed as a persistent, expandable roleplaying and world-simulation framework.

It contains a universal simulation Core, specialized Genre Engines, and associated Content Libraries.

The objective is to introduce an AI orchestration architecture that allows multiple AI providers, models, and specialist agents to cooperate in operating a campaign.

Rather than depending on one AI to simulate the entire world, IRGS will distribute responsibility between specialized Directors operating at different simulation scales.

Each Director manages its own network of AI specialists and access to relevant IRGS systems.

An overarching Game Master Director coordinates the other Directors and manages communication between their networks.

This architecture must be modular, scalable, configurable, and independent of any single AI provider.

**This task is to implement the groundwork, not to finish every AI specialist or completely overhaul the existing simulation.**

The result must be a functional foundation that future development can expand without restructuring the entire application.

---

# 2. Mandatory Initial Repository Assessment

Before modifying the project, inspect the existing IRGS codebase and documentation.

Identify:

- The current Core architecture and simulation subsystems.
- Existing Genre Engines and Content Libraries.
- Existing character, world-state, memory, time, military, economic, political, and social systems.
- How campaigns are created, stored, resumed, and updated.
- Existing APIs and frontend/backend structure.
- Existing plugin, module, or engine registration mechanisms.
- Existing AI integrations, if any.
- Existing testing infrastructure and project startup procedures.

Determine which current components can be reused.

The new AI network must operate **around and through the existing IRGS Core**, not replace it.

Do not duplicate systems that already exist.

Do not remove or substantially rewrite functioning features without a demonstrated architectural necessity.

Preserve backward compatibility where practical, particularly existing campaign data and startup procedures.

Document the existing architecture, identified integration points, and planned changes before implementing substantial modifications.

Where a design choice is not specified here, use the existing project's established conventions.

---

# 3. Six-Director Architecture

IRGS will contain six categories of Directors.

Five are responsible for simulation at different scales. The sixth is responsible for overseeing and coordinating them.

## 3.1 Game Master Director

**Position:** Overarching campaign orchestration authority.

**Specialists:** None.

The Game Master Director is responsible for coordinating the five subordinate Director categories and their respective networks.

Responsibilities:

- Maintain awareness of active Director instances.
- Know each Director's responsibilities, scope, capabilities, and status.
- Coordinate communication between Directors.
- Establish authorized temporary connections when needed.
- Delegate cross-layer tasks to the appropriate Directors.
- Ensure significant events propagate to relevant simulation layers.
- Identify conflicts or inconsistencies between Director outputs.
- Coordinate workflows involving multiple Directors.
- Track significant campaign-wide developments and unresolved tasks.
- Supervise resource allocation and AI workloads.
- Avoid unnecessary AI calls and processing.

The Game Master does not directly control character personalities, write scene narration, simulate economies, or perform the ordinary work of subordinate Directors.

Its role is **orchestration, supervision, and inter-network coordination**.

The Game Master has no dedicated specialist agents.

It may communicate with subordinate Directors and request that they use their specialists.

There should normally be one Game Master instance per campaign.

The Game Master must not be required to relay every routine communication. The underlying orchestration infrastructure should handle established communication paths automatically.

## 3.2 World Director

**Scope:** Entire campaign world or equivalent setting-wide domain.

**Simulation fidelity:** Abstract.

Responsibilities:

- Major international or inter-civilizational developments.
- Global geopolitical changes.
- Major world events.
- Broad economic and demographic trends.
- Interactions between major powers.
- Setting-wide environmental and historical developments.
- Large-scale developments affecting multiple nations.

The World Director should operate primarily through aggregated information and significant events.

It does not need to simulate ordinary individuals, individual settlements, or daily interactions.

## 3.3 National Director

**Scope:** A nation, sovereign polity, major faction, or equivalent political entity.

**Simulation fidelity:** Abstract.

Responsibilities:

- National government and leadership.
- National political developments.
- Military strategy and war administration.
- National economic conditions.
- Diplomacy and foreign relations.
- National institutions.
- Major policy decisions.
- Strategic resource allocation.
- Internal stability and significant national developments.

IRGS must support multiple National Director instances.

England and France, for example, should be capable of having separate Directors with distinct information, interests, decisions, and institutional contexts.

Do not assume that one Director instance represents every nation.

## 3.4 Regional Director

**Scope:** A province, state, county, duchy, administrative region, or equivalent subdivision.

**Simulation fidelity:** Abstract or selectively expanded.

Responsibilities:

- Regional government and administration.
- Regional economy and infrastructure.
- Demographic changes.
- Regional security and military administration.
- Regional institutions.
- Resource distribution.
- Consequences of national decisions.
- Significant developments affecting local settlements.

Regional Directors receive information from relevant National Directors and coordinate effects on subordinate localities.

Multiple Regional Directors may exist within one nation.

## 3.5 Local Director

**Scope:** A settlement, community, military installation, local operating area, or equivalent environment.

**Simulation fidelity:** Detailed.

Responsibilities:

- Local population activity.
- Community interactions.
- NPC schedules and ordinary activities.
- Local employment, trade, and commerce.
- Local institutions and authorities.
- Character relationships.
- Social conditions.
- Local events.
- Settlement and environmental changes.
- Coordination of NPCs and activity across scenes.
- Consequences of player actions on the local community.

Local simulation should receive significant attention because it is directly relevant to the player's experience.

However, the system must avoid assigning a continuously active AI to every individual resident.

Use existing simulation systems, schedules, entity states, and aggregated background activity wherever possible.

Important named characters should retain persistent identities, memories, relationships, and histories.

Ordinary background characters may initially use lighter simulation.

Characters can be promoted to detailed persistent entities when they become important.

## 3.6 Scene Director

**Scope:** An active scene or immediate player interaction.

**Simulation fidelity:** Maximum.

Responsibilities:

- Coordinate active character interactions.
- Manage scene-level AI specialist tasks.
- Coordinate NPC intentions, dialogue, and observable actions.
- Arrange narration.
- Request mechanical resolution from IRGS systems.
- Maintain consistent spatial, environmental, and temporal context.
- Ensure responses respect established character knowledge and campaign history.
- Present the resolved scene to the player.

Multiple Scene Directors must be supportable for campaigns with concurrent scenes or multiple players.

The Scene Director coordinates specialists but does not replace them.

---

# 4. Director Instance and Scope Model

The five simulation layers are categories, not five permanently active AI processes.

IRGS must distinguish between:

1. A Director category or role.
2. A Director instance.
3. The entity or geographic scope managed by that instance.
4. The AI provider/model currently assigned.
5. The available specialists and capabilities.

Every Director instance should have a persistent, uniquely identifiable record.

Suggested fields:

- `director_id`
- `director_type`
- `campaign_id`
- `scope_id`
- `scope_type`
- `parent_scope_id`
- `display_name`
- `status`
- `simulation_fidelity`
- `model_assignment`
- `available_capabilities`
- `active_tasks`
- `event_subscriptions`
- `configuration`

Adapt naming and storage to existing project conventions.

**Geographic location, institutional jurisdiction, and character allegiance must remain distinct.**

A character's nationality must not dictate permanent faction membership or service.

Nations, mercenary organizations, religious institutions, military formations, and similar organizations may have overlapping jurisdictions or influence.

The architecture must support these relationships without assuming that all simulation entities fit into a single rigid geographic hierarchy.

The five standard simulation scales should remain the default structure, but Genre Engines must be able to extend or reinterpret the applicable scopes.

For example, a science-fiction setting might require planets, star systems, sectors, and interstellar governments.

---

# 5. Specialist AI Network

Each simulation Director may have access to specialist AI agents relevant to its responsibilities.

Specialists are modular capabilities.

They should not necessarily be separate continuously running processes or require different AI providers.

A single AI model can fulfil multiple roles through separately defined configurations, prompts, tools, and context.

Initial specialist categories should include:

### Personality AI

Determines how an established character interprets circumstances, what they believe, how they feel, their intentions, motivations, and plausible decisions.

Works with character profiles, relationships, memories, current circumstances, and personal knowledge.

Returns structured character intentions.

### Writing AI

Transforms approved character intentions into dialogue, expressions, gestures, and other forms of character communication.

Must preserve established personality and intentions.

The Writing AI must not independently override a character's decisions.

### Narration AI

Produces scene descriptions and presents observable actions, dialogue, environments, atmosphere, and established consequences.

Must not invent unauthorized mechanical outcomes or significant irreversible events.

### Historical and Lore AI

Interprets historical records, established setting information, and Content Libraries.

Provides contextual research and setting-consistency checks.

### Political and Diplomatic AI

Supports institutional decisions, competing political interests, negotiations, governance, and diplomatic reasoning.

### Military Intelligence AI

Supports operational reasoning, command decisions, strategy, tactics, and military planning.

It does not replace the existing Military System's mechanical resolution.

### Economic and Social AI

Supports contextual interpretation of economic and social developments.

Uses existing Core systems for actual numerical and rule-governed resolution.

### Continuity and Validation AI

Optionally provides additional narrative or interpretive review for complex interactions.

It does not replace deterministic validation performed by IRGS Core.

These specialists are the initial catalog, not a fixed or exhaustive list.

Additional specialists must be installable later without redesigning the hierarchy.

Specialists may be shared between Director categories, with their actual access controlled by the calling Director's scope and authorized capabilities.

---

# 6. Spiderweb Plugin Architecture

Implement a modular, graph-based AI network architecture.

The network contains:

- Director nodes.
- Specialist AI nodes.
- System capability nodes.
- Provider/model connections.
- Communication relationships.
- Authorized task-routing paths.

The system must support three connection types.

## 6.1 Permanent Connections

These represent the normal capabilities and systems accessible to an AI role.

Examples:

- Personality AI → Character Memory.
- Scene Director → Scene State.
- Local Director → NPC Scheduling.
- National Director → Political and Military Systems.

Permanent does not mean unrestricted.

All access remains governed by backend permissions.

## 6.2 Temporary Connections

These are additional capabilities authorized for a specific task.

Example:

The Scene Director requires information from a national political simulation.

The Game Master authorizes a scoped connection to the appropriate National Director.

The connection expires when the task ends or its authorization expires.

## 6.3 Delegated Connections

Rather than granting direct access to a complex or unfamiliar system, the Director requests assistance from another specialist or Director.

Example:

Personality AI requires information about appropriate noble etiquette in medieval England.

The request is routed to the Historical AI.

The Historical AI performs the consultation and returns a structured result to the requesting agent through the orchestration system.

**The preferred solution is to delegate specialized work to an appropriate specialist rather than granting every AI direct access to every system.**

---

# 7. Capability Broker and Permission System

Implement a centralized Capability Broker.

The broker must:

- Maintain a registry of available AI and system capabilities.
- Identify eligible services for requested tasks.
- Validate access requests.
- Grant limited, task-specific permissions.
- Enforce scope restrictions.
- Establish authorized connections.
- Revoke temporary access.
- Track capability usage.
- Return structured results.
- Record failed or rejected access attempts.

Permission enforcement must occur in application code.

Do not rely solely on AI instructions to prevent unauthorized access.

Use least-privilege permissions.

Read access, simulation proposals, and state mutations must be distinct capabilities.

Temporary grants should have an explicit task identity, scope, and expiration.

An AI should only receive the information necessary to complete its assignment.

NPC reasoning must respect character knowledge boundaries. A Personality AI should not receive secret information that the character has no legitimate reason to know.

Design the broker to support reusable tool contracts and established tool-integration standards, including MCP-compatible adapters where suitable.

Do not introduce an unnecessary dependency on an external orchestration service if the required foundation can be implemented within the existing IRGS backend.

---

# 8. AI Provider Gateway

Build a provider-independent AI gateway.

IRGS must support configuring different providers and models for different roles.

The architecture should accommodate providers such as:

- OpenAI.
- Anthropic.
- Google.
- Locally hosted or open-weight models.
- Additional providers installed in the future.

Do not hardcode provider names or model versions into simulation logic.

Implement a standard provider adapter interface for:

- Model invocation.
- Structured input and output.
- Tool invocation where supported.
- Model configuration.
- Error handling.
- Timeouts.
- Usage accounting.
- Provider capability descriptions.
- Optional streaming.
- Optional fallback routing.

Create a configurable role-to-model assignment registry.

A Director or specialist role should be able to change its assigned model without requiring changes to the Core or Genre Engines.

The registry should capture supported capabilities such as structured output, tool calling, and context limits where available.

For the initial implementation, prioritize a working mock provider and reusable adapter contracts.

Implement live provider integrations where safely supported by existing dependencies and credentials.

Do not require paid external API calls for basic tests.

Do not place API keys in browser code, committed source files, or campaign exports.

---

# 9. Inter-Director Communication

Implement controlled communication between Director instances.

Three pathways are required.

### Vertical Communication

Information moving between simulation scales.

Example:

A National Director commits an authorized taxation policy.

Regional and Local Directors receive the relevant consequences through the simulation event system.

### Horizontal Communication

Communication between Directors at the same scale.

Example:

Two National Directors need to coordinate a diplomatic exchange or military negotiation.

### Specialist Delegation

A Director or its specialist requests work from another qualified component.

All non-routine cross-network connections must be validated by the orchestration system and subject to Game Master coordination policies.

The Game Master should be able to authorize direct communication between appropriate Directors.

Established, safe communication channels should operate without requiring a fresh Game Master AI inference every time.

Avoid routing ordinary events through every Director in the hierarchy.

Implement a shared task/message contract containing, where appropriate:

- Unique task identifier.
- Campaign identifier.
- Originating Director or specialist.
- Destination or requested capability.
- Scope.
- Task type.
- Priority.
- Correlation and causation identifiers.
- Permitted contextual information.
- Expected result format.
- Execution status.
- Resource budget.
- Error and retry information.

Support asynchronous task processing and structured results.

Include task timeouts, cancellation, retries, duplicate protection, and failure reporting.

A failed specialist or model call must not corrupt world state or silently count as a successfully completed task.

---

# 10. Shared World State and Event Ledger

**IRGS Core must remain the authority for simulation state.**

Directors and specialist AIs may propose decisions and actions.

They must not independently create contradictory authoritative world states.

Implement or integrate an event-driven state workflow:

1. A player action or simulation event occurs.
2. The responsible Director identifies the required work.
3. Specialists provide interpretations, decisions, or proposals.
4. The appropriate IRGS systems validate and resolve the action.
5. Approved changes are committed to authoritative campaign state.
6. A corresponding event is recorded.
7. Relevant Directors receive notifications.
8. Narrative specialists present observable results.

Reuse existing state, event, and persistence infrastructure wherever possible.

Introduce new infrastructure only when necessary.

Events should carry information such as:

- Event identity.
- Campaign identity.
- Simulation timestamp.
- Originating entity or Director.
- Geographic or institutional scope.
- Event category.
- Significance.
- Affected entities.
- State version.
- Information visibility.
- Structured event payload.

The event ledger must support traceability and deterministic replay of committed state changes where practical.

Use transactions, version checks, or another suitable concurrency mechanism to prevent conflicting updates.

Retrying a task must not apply the same consequential event twice.

---

# 11. Adaptive Simulation Fidelity

The system must prioritize simulation detail based on relevance to active gameplay.

Default processing expectations:

| Layer | Normal Fidelity |
|---|---|
| Scene | Maximum |
| Local | High |
| Regional | Abstract |
| National | Abstract |
| World | Minimal |

These are defaults rather than immutable restrictions.

Scene and Local simulations should operate at much greater resolution.

Higher layers should usually operate through aggregated statistics, significant decisions, scheduled developments, and broad consequences.

A National Director does not need to simulate every citizen individually.

A Local Director should not need to generate individual AI reasoning for thousands of ordinary residents every moment.

Implement a configurable fidelity policy that can consider:

- Player proximity.
- Active scenes.
- Character significance.
- Event significance.
- Ongoing conflicts.
- Campaign priorities.
- Available computational resources.
- Presence of other players.

**Fidelity must be independent of persistence.**

Reducing an area's processing detail must never erase established facts or previously committed events.

Support promotion and demotion of simulation scopes.

When a player enters an abstracted area, IRGS should reconstruct the necessary detailed simulation from its established state, history, and applicable rules.

It must not silently contradict previous events.

When the player leaves an area, the simulation may become more abstract while preserving meaningful developments.

Do not implement a system that permanently requires separate active AI processes for every settlement, province, or nation.

Use lazy activation and scheduled processing.

---

# 12. Campaign Clock and Simulation Scheduling

All five simulation layers must operate against a common authoritative campaign timeline.

Different layers may process developments at different intervals.

For example:

- Scene events may resolve action by action.
- Local events may advance according to short simulation intervals.
- Regional developments may be processed periodically.
- National and World developments may be processed at broader intervals or triggered by important events.

The actual intervals should be configurable and may differ by Genre Engine.

Use the existing time system if available.

Do not introduce a second competing campaign clock.

Support event-driven processing outside normal intervals when a significant development requires immediate attention.

Directors must not create contradictory event ordering.

Provide an extensible scheduling interface, even if the initial implementation uses a minimal scheduler.

---

# 13. Game Master Orchestration Policies

The Game Master Director is the central coordination intelligence.

However, the underlying controller must be conventional software responsible for enforcing execution rules.

Separate:

**Game Master AI:** Determines which Directors need to cooperate and identifies complex cross-layer dependencies.

**Orchestration Controller:** Executes approved routing, permissions, task scheduling, state validation, and recovery procedures.

The controller must remain operable for routine tasks even when the Game Master model is unavailable.

Game Master context should include:

- Active Director registry.
- Campaign-wide significant events.
- Outstanding cross-layer tasks.
- Relevant scope relationships.
- Available capabilities.
- Processing status.
- Relevant conflicts and dependencies.

Maintain this overview through structured data derived from campaign state and event records.

Do not attempt to maintain the entire campaign world exclusively inside the Game Master's conversational context.

The Game Master may coordinate or request reconsideration of conflicting Director proposals.

It must not arbitrarily override authoritative Core calculations or rewrite committed campaign history.

---

# 14. Scene Interaction Workflow

Establish a functional demonstration of cooperation between Scene Director specialists.

Use this general workflow:

1. The player submits an action or dialogue.
2. Scene Director retrieves the relevant scene context.
3. Necessary world, character, and mechanical information is retrieved through approved capabilities.
4. Personality AI interprets affected characters' possible reactions and intentions.
5. Relevant mechanics validate or resolve consequential actions.
6. Writing AI converts approved intentions into character dialogue and expressions.
7. Narration AI combines approved events and dialogue into a coherent scene.
8. Validation checks narrative output against known state and knowledge restrictions.
9. Approved consequences are committed through existing Core interfaces.
10. The player receives the unified result.

Do not allow Writer or Narrator outputs to introduce unapproved state changes.

For the first implementation, provide a working example using mock AI responses and minimal scene data.

The example must demonstrate actual data passing between components, not merely a diagram or several unrelated model calls.

Keep all agent outputs structured internally, even when the final player-facing result is prose.

A simpler single-model execution path should also remain possible for tasks that do not benefit from multiple specialists.

---

# 15. Website — AI Network Management

Add an **AI Network** management section to the existing IRGS website.

The objective is to provide a configurable visual interface for managing Directors, specialists, providers, capabilities, and their connections.

Use the existing frontend framework and design conventions.

## 15.1 Network Visualization

Create a graphical network interface resembling an interconnected spiderweb.

Nodes should represent:

- The Game Master Director.
- World Directors.
- National Directors.
- Regional Directors.
- Local Directors.
- Scene Directors.
- Specialist AI roles.
- IRGS system capabilities.

Connections should visually distinguish:

- Permanent access.
- Temporary authorized access.
- Delegated task relationships.
- Inter-Director communication.

The Game Master should appear as the overarching coordination node.

Users must be able to inspect individual nodes and their established connections.

The interface should handle multiple Director instances within each category.

Avoid restricting the visualization to six total nodes.

## 15.2 Configuration

Provide the groundwork for:

- Registering AI providers.
- Assigning models to Director roles.
- Assigning models to specialist roles.
- Enabling and disabling optional specialists.
- Viewing available capabilities.
- Configuring permitted connections.
- Inspecting Director scopes.
- Viewing active and inactive network components.

Backend validation must govern any configuration changes.

Disabling a specialist must not destroy its persistent data or automatically invalidate campaign history.

## 15.3 Observability

Provide an execution-trace view showing:

- The initiating event.
- Which Director received it.
- Which specialists were invoked.
- Which systems were accessed.
- Inter-Director requests.
- Task outcomes.
- Errors.
- Execution duration.
- Model usage and estimated costs where available.

The initial interface may prioritize operational functionality over visual polish.

However, its displayed network must derive from the actual registry rather than hardcoded mock data.

## 15.4 Persistent Configuration

Store network configuration persistently using the existing application storage conventions.

Provide suitable settings APIs.

Ensure provider credentials remain server-side.

Do not introduce insecure browser-side API key management.

---

# 16. Genre Engine Integration

The AI network must remain universal.

Genre Engines should supply specialized mechanics, capabilities, contextual information, and setting-specific interpretations.

Examples:

**A Scot's Tale / Hundred Years' War**

- Medieval social customs.
- Feudal politics.
- Military organization.
- Historical economic conditions.
- Historical content and chronology.

**Star Wars**

- Galactic political institutions.
- Planetary and system-scale administration.
- Space travel.
- Starship operations.
- Science-fiction military systems.
- Setting-specific species and technologies.

Do not create separate, incompatible AI orchestrators for each genre.

Genre Engines must register their available capabilities through a common interface.

Content Libraries must remain distinguishable from simulation logic.

A character's origin, residence, citizenship, institutional membership, contracts, and allegiances must continue to be treated as separate concepts.

The AI orchestration system must not introduce fixed faction assignments or nationality-based participation restrictions.

---

# 17. Initial Implementation Boundaries

For this development round, implement the infrastructure needed to support the architecture.

**Required initial functionality:**

- A Director registry supporting all six Director categories.
- Multiple instances and scoped assignments.
- A Game Master orchestration interface.
- A specialist AI registry.
- A provider-independent model gateway.
- A mock AI adapter for testing.
- A Capability Broker with enforceable permissions.
- Structured task delegation.
- An event routing/subscription mechanism integrated with existing Core infrastructure.
- A configurable simulation-fidelity policy.
- A shared-clock scheduling interface.
- Persistent configuration.
- A functioning AI Network website section.
- A functional multi-agent demonstration.
- Automated tests.
- Architecture and integration documentation.

**Do not attempt in this round:**

- Fully intelligent NPC simulation for entire cities.
- Continuous LLM processing for all countries and regions.
- Complete national political or economic simulations written from scratch.
- Replacement of existing mechanics.
- Fully autonomous self-modifying AI agents.
- Training new AI models.
- Unbounded parallel model execution.
- Mandatory paid API calls.
- Unrequested changes to established content or campaign lore.

Build the scaffolding properly, then prove that it works through a limited vertical slice.

---

# 18. Suggested Implementation Order

## Phase 0 — Architecture Audit

Inspect the repository.

Identify reusable components and document integration points.

Determine how the AI network will fit into the current backend and frontend.

Avoid introducing unnecessary new frameworks or services.

## Phase 1 — Backend Foundations

Implement the registries, typed interfaces, provider gateway, capability broker, and orchestration controller.

Add Director instance management and task dispatch.

Ensure all six Director categories are represented.

## Phase 2 — State and Event Integration

Connect the new infrastructure to existing campaign state, event, time, and simulation systems.

Implement authorization, state-change validation, event subscriptions, and task lifecycle management.

## Phase 3 — Functional AI Cooperation

Implement a mock multi-agent execution flow involving:

- Scene Director.
- Personality specialist.
- Writing specialist.
- Narration specialist.
- Local Director.
- Game Master coordination where applicable.

Demonstrate a significant event being propagated to another layer.

Verify that all permanent state changes pass through the authoritative Core.

## Phase 4 — Website Network Management

Implement the AI Network configuration area.

Provide working registry views, node inspection, role assignments, connection visualization, and execution traces.

## Phase 5 — Tests, Documentation and Integration

Run existing and new tests.

Resolve regressions.

Document all new interfaces and extension points.

Verify that existing startup procedures and campaign workflows continue functioning.

---

# 19. Required Automated Tests

Include tests demonstrating at minimum:

**Director hierarchy**

- One campaign can register a Game Master and all five simulation Director categories.
- Multiple National, Regional, Local, and Scene instances are supported.
- Director scopes and relationships are correctly recorded.

**Capability permissions**

- Authorized access succeeds.
- Unauthorized access fails.
- Temporary access expires.
- Delegated task results reach the correct requester.
- An AI cannot bypass backend permissions by requesting a tool directly.

**Simulation authority**

- AI proposals cannot directly overwrite world state.
- Consequential changes pass through Core validation.
- Duplicate tasks or event retries do not duplicate state changes.
- Failed tasks do not partially corrupt authoritative state.

**Event propagation**

- Relevant events reach subscribed Directors.
- Irrelevant events do not activate unnecessary Directors.
- A significant scene event can trigger local and national processing when appropriate.

**Adaptive fidelity**

- Different scopes can operate at different fidelity levels.
- Changing fidelity preserves established facts.
- Deactivated scopes can be restored from persistent state.

**Provider gateway**

- Model assignments can be changed through configuration.
- Mock providers can execute a task without external credentials.
- Provider errors and timeouts are reported.
- Model failures do not corrupt campaign state.

**Scene workflow**

- Personality output informs Writing output.
- Approved dialogue and actions inform Narration.
- The final response respects established state.
- Required Core resolution precedes presentation of definitive consequences.

**Website integration**

- Network data comes from the actual backend registry.
- Configuration persists.
- Invalid changes are rejected.
- Existing application pages and startup procedures remain functional.

---

# 20. Required Deliverables

At completion of this development round, provide:

1. The implemented backend architecture.
2. The AI Network website management interface.
3. A working demonstration of multi-AI task delegation.
4. Core integration interfaces for simulation systems.
5. Provider and specialist registration mechanisms.
6. Automated tests with their results.
7. Developer documentation explaining the architecture.
8. Instructions for adding an AI provider.
9. Instructions for registering a new specialist.
10. Instructions for creating additional Director instances and configuring their scopes.

Also provide a concise completion report detailing:

- Existing components reused.
- Files created or modified.
- Architectural decisions.
- Functionality that works.
- Tests passed or failed.
- Any incomplete components.
- Technical debt or limitations.
- Recommended next implementation steps.

Do not describe unimplemented scaffolding as completed functionality.

Do not replace working systems with placeholders.

If an existing system is insufficient, implement the smallest compatible extension required.

---

# 21. Final Architectural Principles

The following principles must guide the implementation.

**One authoritative reality.**  
IRGS Core, not an AI model, owns committed campaign state.

**Six Director categories.**  
One Game Master role and five simulation scales: World, National, Regional, Local, and Scene.

**Multiple Director instances.**  
The system must support as many scoped Directors as the campaign requires.

**The Game Master coordinates rather than simulates.**  
It has no dedicated specialists and communicates through subordinate Directors.

**Specialists are modular.**  
An AI's responsibilities, capabilities, provider, and permissions must be separately configurable.

**Connections are controlled.**  
No AI receives unrestricted access to the entire simulation.

**Detail follows relevance.**  
Scene and Local simulation receive high fidelity; higher layers normally operate abstractly.

**Continuity survives abstraction.**  
Lower processing intensity must never erase established history.

**Providers are interchangeable.**  
IRGS must not become dependent on a single commercial AI vendor.

**The website is a real management interface.**  
It must expose actual registered agents, capabilities, settings, and execution activity.

**Existing IRGS functionality is preserved.**  
This work extends and connects the existing simulation systems rather than rebuilding them unnecessarily.

---

# 22. Execution Instruction to Codex

Begin by inspecting the existing repository and identifying the exact architectural integration points.

Then proceed with implementing the foundational multi-AI network in manageable, testable stages.

Do not stop after producing an architectural proposal or placeholder files.

Implement the registries, orchestration contracts, permission enforcement, event integration, provider abstraction, and functional website groundwork.

Prove that the new components can coordinate a limited campaign interaction without bypassing the existing simulation Core.

Run the available tests, address integration failures, and report the actual implementation status.

The objective of this round is to leave IRGS with a **working, extensible foundation for its six-Director hierarchical AI network**, ready for subsequent development of the individual specialist intelligences and increasingly sophisticated campaign simulations.


---


# SOURCE VOLUME C — Codex Instructions Part 1: Hundred Years’ War v0.4 + World & Civilization Interface v0.1

**Original attachment:** `Codex_Instructions_Part_1(1).md`  
**Source status:** Included for provenance and complete implementation detail; apply integrated precedence/reconciliation.

---

# Codex Instructions Part 1

**IRGS — Hundred Years' War Grand Campaign + World & Civilization Interface**  
**Integrated Codex design submission:** Part 1 · 19 October 2026  
**Bundled design sources:** Hundred Years' War Grand Campaign Integration v0.4 + World & Civilization Interface v0.1  
**Status:** Consolidated requirements and proposals for implementation review. **Not automatically adopted, migrated, implemented, calibrated, or playtested.**

> **Codex directive:** Read this entire document before changing the project. Inspect the actual IRGS Core 3.3 Live repository/archive, website, server, persistence model, tests, historical campaign implementation, and existing APIs. Apply **CMRR (Compare → Merge → Reconcile → Resubmit)**. Preserve established behaviour and existing saves; reuse authoritative Core mechanisms. Implement missing features at the highest valid layer, do not invent historical quantities, and report precisely what was built, not built, tested, or unverified. The two source specifications reproduced in Volumes A and B remain part of this instruction, not optional reference links.

---

## 0. Navigation and document-use rules

This is **one self-contained delivery document** with an integrated implementation directive and the full substantial content of both supplied design sources.

| Location | Material | Source status |
|---|---|---|
| Integrated directive, below | Cross-source design decisions, priorities, shared interfaces, acceptance rules, and reconciliation | Editorial integration; proposed implementation direction |
| **Volume A** | *The Hundred Years' War — Grand Campaign Integration & Historical Simulation Framework*, v0.4, complete substantive specification | User-supplied consolidated campaign design; not automatic code adoption |
| **Volume B** | *World & Civilization Interface*, proposed v0.1, complete substantive specification | User-supplied website design proposal; not automatic code adoption |

**Preservation policy:** Volume A and Volume B are reproduced with section order, examples, historical entry-point tables, technical rules, cases, and source terminology retained. Headings are nested for this combined document. The imported World Interface text had incidental export artifacts (orphan attachment labels and encoded trailing spaces); these were removed without deleting design requirements. Superseded rules are explicitly identified below; do not treat their reappearance within a historical discussion as renewed acceptance.

**Recommended reading order:** Integrated directive → Volume A, Parts I–IV and XVIII–XXI → Volume B, §§1–21 → relevant historical start profiles and complete acceptance sections in Volume A.

---

## 1. Canonical integrated objective

Build IRGS as a **genre-neutral, persistent simulation system** with a **historically initialized Hundred Years' War Grand Campaign** and a **single World & Civilization user interface** that accurately exposes that simulation at personal, institutional, settlement, military, regional, and civilization scales.

The Hundred Years' War (1337–1453) is the historical environment of the Grand Campaign, **not a mandatory occupation, player faction, victory condition, endpoint, or isolated mechanical engine**. Its ten historical entry points are Sub-Campaign start profiles; Starting Scenarios such as *A Scot's Tale* are openings inside those profiles. Independent playthroughs diverge causally and continue indefinitely.

The website shall retain the three gameplay perspectives **Story | World | Chronicle**. The **World** view has six interconnected workspaces: **Atlas, Economy, Politics, Military, Settlements, Institutions**. A civilization-wide overview is a cross-domain aggregation—not a seventh independent simulation. Story, World, and Chronicle show different permission-filtered projections of **one** world clock and **one** authoritative state.

**The interface must serve the same simulated world** whether the player is a Scottish mercenary, a foreign-employed scholar, a landholder, a merchant, a soldier, a military commander, a municipal official, or a sovereign. Knowledge, resources, legal/institutional powers, and actual circumstances determine available controls—not nationality, a permanent faction class, or character level.

### 1.1 Key rules that take precedence during reconciliation

1. **Conditional historical future (v0.4 supersession).** Actual past history is loaded through the selected start-date cutoff. Source-backed future history is represented as conditional intended events whose causal requirements are rechecked. If undisturbed, historical paths are intended to proceed as recorded. No dated event may create missing actors/resources, force outcomes, defeat player agency, or overwrite a divergent simulation. Earlier blanket rules saying the future is entirely unscheduled are **superseded**; a rigid historical script is **also rejected**.
2. **Nationality is independent of faction and service.** Birthplace, national/cultural origin, legal subjecthood or citizenship, residence, institutional membership, employer, contract, political allegiance, and player-control perspective are distinct. Scottish origin never automatically blocks English service; foreign scientific employment is also possible when circumstances permit.
3. **Faction association is optional and non-singular.** Individuals may be unaffiliated, civilian, employed, freelance, mercenary, part of a free company, serving overseas, or involved with multiple compatible institutions. Service applications are not appointments; clients and contracts are not permanent political allegiance. Faction-level control is a separate control assignment, not an individual worker's affiliation.
4. **Only Core commits simulation effects.** The website displays permission-filtered world projections and submits explicit declarations. It does not privately simulate budgets, add soldiers, enact reforms, transfer property, create resources, or independently update the clock.
5. **Information, authority, ownership, competence, and control are not interchangeable.** An army's reported location differs from its actual position; a king's jurisdiction differs from personal ownership; a military command differs from a mercenary contract; an alliance differs from actual deployed reinforcements; a planned shipment differs from stock.
6. **Cross-scale continuity.** Zoom, time-scale changes, aggregate dashboards, save/load, and historical summaries must not replenish or duplicate people, money, goods, institutions, projects, casualties, or events.
7. **Player agency remains absolute within the applicable rules.** Never invent player speech, voluntary movement, purchases, agreements, politics, spouse/successor selection, or expenditure. NPCs and institutions act autonomously through Core. Dice resolve consequential uncertainty, not physical impossibility.
8. **No retroactive mutation.** Do not migrate existing saves or reinterpret old character/campaign histories without authorization and a documented compatibility plan.

---

## 2. Architecture, ownership, and data flow

### 2.1 Authority and layer ownership

| Layer | Owns | Must not own |
|---|---|---|
| **Shared IRGS Core** | Identity/actors, agency, causality, time, state, information, resources, transfers, organizations, contractual obligations, authority interfaces, logistics, projects, population, military organization, continuity | Hundred Years' War historical lore or frontend layouts |
| **Historical Genre Foundation** | Reconstruction from sources, dated assertions, intended conditional historical-event plans, event divergence reconciliation, historical provenance | An independent duplicate army/economy/state simulation |
| **Hundred Years' War Content Library** | Dated historical polities, rulers, geography, technological baselines, institutions, historical events, researched period conditions, historical starting profiles | Universal governance/economy/military/contract mechanics |
| **Campaign Profile and Starting Scenarios** | Enabled rules, starting date, chosen historical research edition, scenario location/participants, permitted player perspective, scenario constraints, overrides | A second world state shared across all playthroughs |
| **Independent Campaign State** | Actual live actors, assets, history, outcomes, institutions, knowledge, geography updates, and continuity per playthrough | Uncommitted action drafts or website-only resource balances |
| **Website presentation/integration** | Navigable world views, filtered entity inspectors, action drafts, visualizations, requests for authorized Core procedures, accessibility/responsiveness | Setting physical effects, inventing source values, NPC hidden knowledge, direct ledger changes |

### 2.2 Required state and information path

```text
Campaign + historical start date + research edition + scenario
    └─> Historic State Database (dated source assertions and reconstruction)
          ├─> Core initialization of independent playthrough state
          └─> Historical foundation's conditional event-plan registry

Actual independent Core Campaign State
    ├─> View-projection and permissions service
    │     ├─> Story view
    │     ├─> World view: Atlas / Economy / Politics / Military / Settlements / Institutions
    │     └─> Chronicle view
    └─> Core action resolution <── validated explicit declaration/order/contract
          ├─> feasibility and execution
          ├─> actual effects, autonomous reactions, and information propagation
          ├─> one committed state/event transaction
          └─> new state version and filtered result for website

Historical event plans ──> reevaluated against actual state/dependencies
Historical source archive ──> creator/debug review, not character future knowledge
Historical summaries ──> derived archive views, never authoritative state
```

### 2.3 Important domain distinctions

- **Territory:** sovereignty claim, administration, military occupation, jurisdiction, property rights, and effective control are separate records/relations.
- **Money:** treasury balance, periodic revenue, outstanding tax claim, reserved expenditure, debt, expected income, and goods in transit are separate notions.
- **People:** population, households, workforce, active employees, military members, assigned/present/available personnel, casualties, and visitors are not additive by default.
- **Contracts:** prospective application, negotiation, offer, acceptance, active service, paid/unpaid liabilities, completion, termination, and historical affiliation have different states.
- **Technical knowledge:** discovery, personal understanding, available tools, manufacturability, physical possession, institutional adoption, and dissemination are separate.
- **Information:** occurrence, observation, transmission, receipt, belief, outdated reporting, and uncertainty are separate.

---

## 3. Integrated website experience

### 3.1 Grand Campaign entry and Life-Path

The full entry sequence shall be:

```text
Grand Campaign: The Hundred Years' War
    → historical period/date (ten curated entries or validated custom date)
    → predefined Starting Scenario or Custom Beginning
    → individual character or eligible institutional control perspective
    → existing character OR new character with identity, family, upbringing,
      education/skills, relationships, finances, and history as applicable
    → optional occupations, employment, service applications, contracts,
      organizational membership, and/or independent status
    → validate exact starting date and historical world-state consistency
    → review provenance, actual assets/authority, unresolved assumptions
    → commit one independent playthrough; open Story | World | Chronicle
```

Do not show every historic polity as a permanently eligible faction. Eligibility and current institutions are derived from the **exact selected date** or, for a continuing divergent save, its **actual current state**. *A Scot's Tale* is one 1415 character Starting Scenario; its recruitment-yard start and later service checkpoint are separate initializations requiring different verified dates/states. Preserve the Scottish identity and English-service possibility.

### 3.2 World view and responsiveness

The user-facing World view should provide a consistent campaign header (campaign, scenario, world time, save state, notifications), a navigation region, a primary workspace, a contextual inspector, and a clear path back to Story and Chronicle. **On desktop**, favour a central wide map or main dashboard with optional left navigation and right entity inspector. **On tablet**, use collapsible drawers. **On mobile**, use one focused workspace and sheets/full-screen inspectors with accessible navigation.

**Six workspaces:**

| Workspace | Contents and characteristic tasks |
|---|---|
| **Atlas** | Physical terrain, geography at multiple supported scales, settlements, travel planning, known routes, political claims vs actual control, known military/market reports; inspection never moves units or reveals secrets |
| **Economy** | Household, enterprise, settlement, government views; stock, income, obligations, production, demand, labour, market reports, logistics, forecasts clearly separate from inventory |
| **Politics** | Officeholders vs offices, jurisdictions, legal powers, contested claims, councils, diplomacy, treaty drafts/communication, authority and institutional reactions |
| **Military** | Formation hierarchy, assigned/present/available strength, equipment, orders, readiness, supply, operations maps, messenger/receipt timelines, mercenary contract arrangements |
| **Settlements** | Households/population, residents vs visitors, buildings and property, infrastructure, local economies/services, public management, construction and maintenance, autonomous changes |
| **Institutions** | Governments, guilds, households, free companies, universities, businesses: governance, membership, contracts, assets, leadership, projects, continuity and succession |

A broader **Civilization Overview** draws on the above without establishing a separate simulation. The creator-only Historical Comparison Inspector may show source baselines, event-plan states, historical divergence and dependencies; ordinary players must not receive secret plans.

### 3.3 Explicit inspect–draft–submit–resolve boundary

1. **Inspect:** maps, charts, records, history, entity selection, time filters, and layer changes are read-only and do not advance world time.
2. **Draft:** route, construction, diplomatic, employment, research, or military-order proposals are not yet actual effects; show estimates and uncertainties clearly.
3. **Submit:** a player deliberately authorizes a state-changing action within their role and authority.
4. **Resolve:** Core evaluates feasibility, uncertainty if warranted, actual execution/effects, exposure, autonomous reactions, and state changes.
5. **Report:** website displays what was actually done, not what the player merely intended, including action status, event provenance, world time and save acknowledgement.
6. **Return control:** do not invent another voluntary act or continue past a required player choice.

Example: Drawing a bridge does **not** build one. An authorized bridge project needs actual land rights, workers, materials, finance, elapsed time, consequences and maintenance. It becomes **one** asset, exposed through Atlas, Economy, Settlement, Institution, Military and Chronicle views without duplicate ownership or material usage.

### 3.4 Suggested projection and action contract

Proposed logical service names only; **map to existing code instead of duplicating it**:

| Read-only projections | Commands and lifecycle |
|---|---|
| `GetWorldProjection`, `GetGeography`, `GetEntityDetails` | `SubmitWorldAction` with explicit permission/agency checks |
| `GetEconomicProjection`, `GetPoliticalProjection` | Draft and review order/contract/project before submission |
| `GetMilitaryProjection`, `GetSettlementProjection` | Submit military or institutional instructions via Core |
| `GetInstitutionProjection`, `GetHistoricalProjection` | `GetActionResolution` / recover by original request ID |

Every state-changing request should be idempotent where technically applicable, with a playthrough identifier, actor/control assignment, expected state version, request ID, and exact declaration. Responses should distinguish **accepted, rejected, pending, interrupted, requires clarification, committed**, and corresponding user-visible state. The returned view must be server-side permission-filtered; do not transmit secret entities or future plans and hide them with CSS.

---

## 4. Integration conflicts and CMRR disposition

| Issue | Volume A | Volume B | Reconciliation / instruction |
|---|---|---|---|
| Historical events after start | Conditional planned baseline; historical default when causes intact | Historical comparisons only in authorized creator view | **Retain Volume A v0.4:** conditional causal plans, not rigid script nor empty unscheduled future; render only known information to normal players |
| Who owns world mechanics | Shared Core and historical foundation/content | Explicitly prohibits a separate frontend simulator | **Merge:** one authoritative Core, domain-specific views and historical adapters only |
| Time, state and historical memory | Persistent history, annual to 500-year summary hierarchy | Dashboard/Chronicle linkage | **Merge:** summaries are derived views, never reset/mutate resources, actors, or clock |
| Campaign and scenario hierarchy | Ten periods, scenarios, independent saves | UI contextual to current campaign | **Retain:** date-sensitive creation and perspectives; no independent 1415 engine or AST game |
| Nation or faction vs personal identity | Birth/nationality distinct from service/control | Tool access depends on authority and knowledge | **Merge:** nationality does not hard-lock foreign employers or world controls |
| Mercenary and civilian careers | Independent individuals, multiple clients/contracts | Military and institutional workspaces | **Merge:** roles and actual contracts determine available controls; not forced national faction selection |
| Sovereignty and maps | Overlapping claims, effective control, occupation | Political overlays and inspectors | **Merge:** distinct layers/entities, no universal owner field |
| Economic/military totals | One ledger/source and no duplicate casualties | Multiple cross-domain dashboards | **Merge:** aggregates are read-only, deduplicated projections of actual records |
| Historical knowledge | Future plans secret from actors; communication timestamps | Atlas displays dated reports and uncertainty | **Merge:** enforce server-side projection filtering by perspective/time |
| Technology and research | Date-specific baseline, free causal innovation | World projects/institution/economic views | **Merge:** invention is an actual Core project, not a UI unlock or automatic dissemination |
| Institution vs resident/subject | Membership, ownership, authority separate | Settlements/institutions show overlapping roles | **Merge:** no state ownership acquired by seeing or administrating residents |
| Map detail | Geographic hierarchy and sourced uncertainty | Multi-resolution Atlas | **Merge:** no fabricated floor plan, exact border, settlement coordinate, or map layer data where not present |
| Player agency | Cannot invent actions; NPCs autonomous | Explicit submission and plan-vs-action display | **Retain, apply to all controls:** no auto orders, commitments, expenditure, or success narration |
| Existing saves | Research versions and no silent migration | UI proposed, existing site not audited | **Retain:** no retroactive migration or source research overwrite |
| Visual system | Not prescribed | Dark-charcoal, 3-column desktop, mobile drawer concepts | **Proposed only:** design targets pending usability review; do not elevate aesthetic choices into Core rules |

**Reconciled removals:** No substantive feature from either supplied document is deliberately removed. The only removed source text consists of malformed export-reference labels and nonsemantic encoding. An older 'historical future is never scheduled' requirement is superseded by Volume A v0.4; it is not reinstated. The UI must not implement 'historical outcome guarantee' simply because v0.4 calls historical events intended defaults. The proposed view/component/API names are interface targets, not proof of absent Core capability.

---

## 5. Recommended execution sequence for Codex

1. **Inventory and compare.** Read Core 3.3 Live and the actual repository. Identify live schema/routes/components, state/event authority, access control, source data, current campaign setup, initializers, test coverage, and whether a map renderer or geospatial data exists. Record mismatches to both volumes.
2. **Specify inherited interfaces.** Reuse Core actor/organization, time, information, economy, military, resource, contract, geography and project records. Specify the historical adapter and permission-filtered frontend projection without duplicating ownership.
3. **Implement a verified historical vertical slice.** Select one 1415 start and its exact date, source-proven historical state, one valid character or institutional perspective, at least one navigable location, linked institution, resource and known report. Keep A Scot's Tale recruitment start distinct from later checkpoint; do not fabricate data to make a demo look complete.
4. **Build base World shell and Atlas.** Provide shared header, six workspace choices, context inspector, responsive layout, accessible navigation, map/list fallback, time- and permission-filtered geographic entities, layered claims vs control, and read-only travel-route planning.
5. **Add civilian domains.** Household/business/settlement/institution economic projections with one source per asset; physical projects and cross-workspace drilldowns. Demonstrate a bridge or workshop project traversing multiple views without duplication.
6. **Add political/military controls.** Offices and authority, treaty proposals, formation and operational reports, communication lag, actual orders, mercenary contracts and current/past memberships.
7. **Add civilization/chronicle integration.** Cross-domain summaries, delegation/reporting, long-range timescale views, and sealed 500-year epoch access. Maintain independent event source and authoritative state.
8. **Integrate conditional history.** Historical schedules remain service-side; evaluate prerequisites and causal dependency changes. Expose comparison tools to creators only, never secret future predictions to ordinary players.
9. **Run acceptance suites.** Execute UI, Core accounting, privacy/knowledge, idempotency, save/load, historical divergence and timescale tests. Mark scripted/manual/simulated/playtested/calibrated evidence separately.
10. **Resubmit fully.** Deliver actual changed files, data provenance, source-to-feature crosswalk, complete change log, any deprecation/removal, test command/results, known gaps, calibration needs, migrations needing approval, and final status for each requirement.

**Delivery priority:** A functioning permission-filtered **Atlas + entity inspector** and one end-to-end validated action/report in an actual 1415 playthrough are preferable to nonfunctional visual dashboards with fabricated state. Work outward to Economy, Settlements, Institutions, Politics, Military and Civilization management, with the shared Core integrity present from the outset.

---

## 6. Integrated acceptance and regression matrix

The full detailed tests in both volumes remain required. At minimum:

| Case | Pass condition |
|---|---|
| Select 1337/1389/1415/1422/1435/1444/1449/1453 | Date-appropriate actual past, actors, institutions, technical state; only future events conditional; no later reforms prematurely present |
| Two independent 1415 saves | No shared mutable world actors, assets, or outcomes |
| Existing AST character from recruitment yard | No preloaded later sponsorship/pledge; exact compatible opening date |
| Scottish character requests English service | Application possible when feasible, origin unchanged, employment not automatically granted |
| Unaffiliated independent mercenary | Playable with no mandatory faction; contracts and organizations remain after termination |
| Open/toggle/zoom Atlas | No world-time advancement, movement, resource consumption, state mutation or hidden intelligence leak |
| Inspect a historical territorial claim | Claim, actual control, property rights and jurisdiction are separately displayed |
| Inspect a reported military location | Shows observation/receipt timing and uncertainty, not omniscient location |
| Kingdom/region/company army reports | No personnel counted twice; assigned/present/available strength distinguished |
| Transfer supply through road/warehouse | Debit/credit and transit location reconcile; no cloned goods or forecast-as-stock |
| Private workshop appears on ruler's map | Not automatically owned or directly commanded by ruler |
| Submit diplomatic offer | Delivery and acceptance have independent state; no instant treaty |
| Propose bridge/construction | Draft is not construction; actual cost/time/authority validated and asset not duplicated |
| Issue military order to distant unit | Authority checked; order issue/transport/receipt/execution separated |
| Historical battle prerequisite removed | Planned event reevaluated without resurrecting forces or undoing actions |
| Unrelated historical event | Not invalidated by arbitrary global butterfly-effect score |
| Early invention | Technical feasibility, production, diffusion and adoption separate, no year-lock |
| Wait/advance across years or centuries | Autonomy, activity, obligations and historical triggers processed exactly once |
| Character death / institution succession | World persists; no automatic PC successor or erased organization |
| 500-year summary sealed | Other historical epochs and authoritative records remain distinct/retrievable |
| Duplicate commit/retry after network failure | No duplicate action, money, project, casualty or historical event |
| Creator comparison vs normal character view | Creator's conditional future plans inaccessible to unauthorized clients |

**Performance/accessibility testing** must include small and large world datasets, list-map fallback, mobile navigation, keyboard/screen-reader operations, deep entity links, scrolling long historical timelines, and reduced motion. Numerical estimates remain **provisional** until calibrated from actual mechanics and sources.

---

## 7. Known unknowns and explicit decisions still required

- Exact existing Core 3.3 Live schema, event/contracts implementation and web routes; **verify**, do not presume new interface names match live code.
- Map geometry and coordinate coverage by historical starting date, and whether detailed property/building mapping exists; avoid invented coordinates and levels of detail.
- Historical entry cutoff verification and research editions, especially scenario-specific AST opening dates and approximate period dates.
- Actual researched population, money, personnel, equipment, resources and territory where historical evidence is incomplete or disputed; preserve unknowns and ranges.
- How institutions delegate command, employment and legal authority across genres, and how the website queries that securely.
- Actual event scheduling, causal dependency evaluation, report transmission and rollback/idempotency contracts.
- Target visual breakpoints, maps/charts packages, map permissions, and creator/admin debugging access.
- Any request to migrate existing campaigns, change adopted Core rules, or reinterpret stored historical facts must be reviewed and authorized separately.

---

## 8. Full source specifications

**Everything following forms part of Codex Instructions Part 1.** These two volumes are bundled so Codex can implement the actual detailed historical state, ten entry points, and every World workspace feature without relying on a separate attachment or shortened summary. Existing authority and supersession rules stated above remain binding.

---

## VOLUME A — THE HUNDRED YEARS’ WAR: GRAND CAMPAIGN FRAMEWORK (SOURCE v0.4)

### IRGS — THE HUNDRED YEARS’ WAR
#### Grand Campaign Integration & Historical Simulation Framework

**Consolidated Design and Implementation Specification v0.4**

**Period:** 1337–1453, with indefinite simulation continuation  
**Architecture:** IRGS Core → Historical Genre Foundation → Hundred Years’ War Content Library → Campaign Profile → Independent Campaign State  
**Source baseline:** IRGS Core 3.3 Live, existing campaign files, Historical Entry Catalogue v0.2, Historical State Database proposals v0.1–v0.2, and the Campaign Design Integration Profile v0.3  
**Status:** Consolidated design submission for Codex review, reconciliation, implementation, and testing. Not automatically adopted.

---

### PART I — CODEX IMPLEMENTATION DIRECTIVE

#### 1. Primary objective

Integrate the Hundred Years’ War as a historically grounded, persistent Grand Campaign within IRGS.

The campaign must support historical military and political events, civilian life, government, business, scientific development, mercenary service, independent careers, families, institutions, and generational continuity.

The war must exist as the historical environment, **not as the player's mandatory occupation or allegiance**.

A player may control a soldier, merchant, ruler, farmer, scholar, independent mercenary, noble, artisan, or another suitable actor. Their decisions must affect the same persistent world through existing IRGS mechanics.

The Grand Campaign contains ten principal historical starting periods and supports additional historically reconstructed starting dates and pre-designed scenarios.

Each starting point establishes historically accurate initial conditions and an **intended historical future**. Historical events are scheduled to occur as recorded unless actual events in the simulation alter, delay, replace, or prevent them.

The world must continue after 1453 without a mandatory ending.

#### 2. Instructions to Codex

Before changing the implementation:

1. Inspect the actual IRGS project, current Core 3.3 Live archive, relevant genre files, website, server, data structures, persistence system, and campaign framework.
2. Inventory existing functionality before proposing replacements or additional mechanisms.
3. Identify the actual ownership of state, time, events, military systems, institutions, technology, contracts, character creation, and campaign initialization.
4. Apply **CMRR: Compare → Merge → Reconcile → Resubmit**.
5. Preserve adopted functions and existing campaign records.
6. Implement reusable mechanisms at the highest appropriate architectural layer.
7. Do not duplicate Core mechanics inside the Hundred Years’ War campaign.
8. Do not invent historical troop counts, treasury balances, population figures, or technological capabilities to fill empty fields.
9. Preserve existing working behaviour unless the new requirements explicitly supersede it.
10. Implement automated acceptance and regression tests where the existing environment supports them.
11. Identify assumptions, missing sources, incompatible dependencies, and incomplete functionality.
12. Deliver a complete consolidated implementation and change report, not merely a collection of proposed patches.

**Authority precedence:** Current explicit instructions → adopted campaign rules → adopted historical genre foundation → adopted IRGS Core → provisional proposals.

This document establishes intended requirements but does not assert that every mentioned interface, schema, or mechanism is absent from Core. Verify before implementing.

---

### PART II — GRAND CAMPAIGN ARCHITECTURE

#### 3. Campaign hierarchy

The intended hierarchy is:

```text
IRGS
│
├── Shared Core
│   ├── Time and Continuity
│   ├── Actors and Organizations
│   ├── Political Authority
│   ├── Military Organizations
│   ├── Economic and Resource Systems
│   ├── Logistics
│   ├── Contracts and Obligations
│   ├── Information and Communication
│   ├── Technology and Projects
│   ├── Population and Society
│   ├── Historical Event Scheduling Interfaces
│   └── Persistent Simulation State
│
├── Historical Genre Foundation
│   ├── Historical State Reconstruction
│   ├── Historical Event Plans
│   ├── Historical Divergence Reconciliation
│   ├── Historical Sources and Provenance
│   └── Period-Specific Data Interpretation
│
└── The Hundred Years' War
    │
    ├── Grand Campaign (1337–1453)
    │   │
    │   ├── Historical World Database
    │   ├── Historical Event Timeline
    │   ├── Political and Institutional Registry
    │   ├── Technology and Equipment Library
    │   ├── Historical Geography
    │   └── Ten Primary Starting Periods
    │
    ├── Historical Sub-Campaigns
    │   ├── 1337 — The War Begins
    │   ├── 1360 — Peace of Brétigny
    │   ├── 1369 — Caroline War
    │   ├── 1389 — The Long Truce
    │   ├── 1415 — Lancastrian Invasion
    │   ├── 1422 — Two Kings, One Crown
    │   ├── 1435 — Burgundian Reversal
    │   ├── 1444 — The Last Truce
    │   ├── 1449 — Final Campaigns
    │   └── 1453 — The Aftermath
    │
    ├── Additional Historical Start Dates
    │
    ├── Starting Scenarios
    │   ├── A Scot's Tale
    │   ├── A Soldier for Hire
    │   ├── Across the Channel
    │   ├── The Scholar's Pursuit
    │   └── Custom Beginning
    │
    └── Independent Persistent Playthroughs
```

The ten Sub-Campaigns are not ten separate game engines.

They use one historical content library, the same inherited mechanics, and distinct historical initialization conditions.

Multiple scenarios may exist within each Sub-Campaign.

A scenario determines opening circumstances, not permanent gameplay restrictions.

#### 4. Four independent starting decisions

Campaign setup must distinguish:

**A. When does the player enter the world?**

The historical period, exact date, and associated historical starting conditions.

**B. Who does the player control?**

An existing character, a newly generated character, or an eligible institutional control perspective.

**C. Who is the character?**

Birthplace, nationality, culture, ancestry, family, upbringing, education, competencies, relationships, property, and existing personal history.

**D. What is the character currently doing?**

Civilian life, employment, military service, independent contracting, scientific investigation, travelling, governing, or another activity.

None of these decisions automatically determines the others.

A Scottish character is not required to support Scotland.

A French character is not automatically in French military service.

A merchant is not required to support a national government.

An individual may have multiple institutional relationships or none.

---

### PART III — HISTORICAL TIMELINE RULES

#### 5. Governing historical principle

**History is the intended future unless the simulation changes the causes that produce it.**

Historical campaigns operate through two parallel representations:

##### Historical Baseline Timeline

An immutable, versioned record of actual historical events.

It contains:

- Event dates and date ranges.
- Participants.
- Political and military circumstances.
- Historical intentions and actions.
- Historically recorded outcomes.
- Consequences.
- Evidence and provenance.
- Causal dependencies.
- Uncertainty and disputed interpretations.

##### Living Campaign Timeline

The authoritative history of the active playthrough.

It contains:

- Events actually occurring in the simulation.
- Current actor states.
- Political relationships.
- Military and economic conditions.
- Changed territorial control.
- New technologies and institutions.
- Player actions.
- Autonomous NPC activity.
- Altered, rescheduled, prevented, and new events.

The historical baseline is not allowed to overwrite the actual campaign state.

#### 6. Historical past versus intended future

The distinction depends on the selected starting date.

##### Starting in 1337

All valid historical conditions up to the initialization date are established.

Historical events scheduled after the start are prospective.

The campaign may diverge immediately.

Consequently, the historical 1389 truce could become unnecessary, take a different form, or be functionally replaced by an earlier settlement.

##### Starting in 1389

The historical events preceding the starting date have already occurred normally.

Crécy, Poitiers, Brétigny, the Caroline War, and other relevant prior events form the established history.

The campaign does not simulate 1337–1389 again.

Future historical events are conditionally planned.

##### Starting in 1415

The prior Anglo-French wars, treaties, royal successions, epidemics, political changes, and other historical events have occurred according to the historical record.

Henry V's 1415 invasion and the subsequent events are part of the intended historical schedule.

Agincourt is expected to occur on 25 October 1415 if its historical causal pathway remains sufficiently intact.

##### Starting in 1453

The selected post-Bordeaux scenario begins with the historically recorded conclusion of the principal war.

England retains Calais, France controls Bordeaux, and the existing political and economic circumstances are initialized.

Gameplay does not end.

Events beyond 1453 may develop through simulation. A future historical extension can add conditional baseline events from later periods, but the completed Hundred Years’ War schedule does not automatically impose events such as the Wars of the Roses.

#### 7. Historical default event policy

Every sufficiently documented historical event must possess a conditional event plan.

An event proceeds according to the historical baseline when the relevant actors, resources, places, political conditions, and causal sequence remain materially intact.

The intended historical outcome is the default when the event has not been meaningfully disturbed.

However:

- The scheduled date does not create missing troops, equipment, money, or supplies.
- Historical outcomes cannot override successful simulated actions.
- An actor cannot be resurrected to fulfil a historical role.
- Defeated or destroyed armies cannot reappear for scheduled battles.
- A treaty cannot automatically exist if the signatories lack authority or refuse to negotiate.
- The simulation cannot create player-character actions, speech, motives, or decisions.
- Autonomous actors continue responding to their actual circumstances.
- Historical records are not secret instructions that characters automatically know.

An intended event that becomes unsupported must be reconciled, not forced.

#### 8. Historical event outcomes

Every historical plan must support:

| Status | Meaning |
|---|---|
| Planned | Scheduled and currently viable |
| Preparing | Relevant actors are taking actions toward it |
| At Risk | A change threatens the historical causal pathway |
| Rescheduled | Event remains viable at a different time |
| Altered | Recognizable event proceeds under different conditions |
| Occurred as Recorded | Event and outcome follow history |
| Occurred Altered | Event occurs, but outcome changes |
| Superseded | Another event fulfils or removes its purpose |
| Prevented | Historical event can no longer occur |
| Expired | Its relevant opportunity has passed |

These statuses describe the **event plan**, not physical changes to the world.

Physical outcomes must be recorded separately using Core's existing state and accounting mechanisms.

#### 9. Historical event record

Proposed logical fields:

```yaml
HistoricalEventPlan:
  event_id:
  historical_date:
  date_precision:
  event_type:
  description:

  participants:
  locations:
  political_context:
  historical_intentions:

  prerequisites:
  supporting_conditions:
  triggering_conditions:

  required_capabilities:
  required_resources:
  required_authority:

  historical_execution:
  historical_outcome:
  historical_consequences:

  temporal_flexibility:
  rescheduling_conditions:
  alternative_paths:
  dependent_events:

  current_plan_status:
  divergence_reasons:

  source_references:
  evidence_classification:
  research_version:
```

The final implementation must reuse existing Core event, time, actor, and resource structures wherever possible.

##### Hard prerequisites

Conditions without which the specific event is impossible.

Example: The historical Battle of Agincourt requires opposing English and French forces capable of meeting in battle.

##### Supporting conditions

Circumstances that materially influence the event without necessarily determining its existence.

Example: English sickness, terrain, French command coordination, weather, and army composition influence Agincourt's course and outcome.

##### Event timing

Events may be:

- Date-sensitive.
- Causally sequenced.
- Institutionally driven.
- Biographical.
- Environmental.
- Economically driven.
- Contingent diplomatic developments.

A treaty may happen earlier if the relevant political and military conditions arise earlier.

A siege may move to another date if logistical or operational changes delay the campaign.

A historical king's death cannot be automatically moved without a corresponding cause.

An epidemic must follow its biological and geographical prerequisites.

#### 10. Historical identity versus historical analogue

A changed event must be classified accurately.

Examples:

- Agincourt occurs on its historical date and England wins: historical event reproduced.
- Agincourt occurs, but France wins: altered historical event.
- The same armies encounter one another at Agincourt several days later: potentially rescheduled event.
- The armies meet somewhere else: a new battle related to the original campaign plan.
- Henry V dies before invading France: his historical invasion is prevented.
- Another English ruler invades years later: a new campaign pursuing similar objectives.

Likewise, an Anglo-French truce negotiated in 1369 might be functionally equivalent to the historical Truce of Leulinghem, but it is not literally the same treaty with the same participants.

#### 11. Causal divergence propagation

Historical divergence must be propagated only where causal relationships justify it.

If England loses Agincourt:

- English casualties and surviving units change.
- Henry V's reputation and political position may change.
- French military and political conditions change.
- Future English campaigns require reevaluation.
- The Treaty of Troyes becomes uncertain.
- Burgundian diplomacy must respond to actual conditions.
- Scottish, Iberian, and other actors react where relevant.

Unrelated events must not automatically change.

The entire future timeline must not be invalidated simply because one local event differs.

There must be no arbitrary global butterfly-effect score.

The event dependency graph determines which future plans need reconsideration.

#### 12. Historical information versus character knowledge

Characters must not automatically know future history.

A French noble in 1415 cannot know that Agincourt will historically be an English victory.

A merchant in 1337 cannot know the future economic consequences of the Black Death.

A commander cannot know of a treaty until information reaches them through a legitimate communication path.

Record separately:

- Event occurrence time.
- Observation time.
- Transmission time.
- Receipt time.
- Interpretation or belief.

Players may possess external historical knowledge, but their characters receive only the information and abilities justified within the game.

---

### PART IV — HISTORICAL STATE DATABASE

#### 13. Purpose

Create or integrate a reusable Historical State Database, hereafter HSDB, capable of reconstructing the historical world at any supported starting date.

The Hundred Years’ War will be its first substantial historical campaign application.

The same framework should eventually support other historical periods without duplicating the underlying mechanics.

The database is not a separate game engine.

It initializes Core-owned world state and supplies conditional historical future plans.

#### 14. Historical record families

The system must support the following logical categories, reusing existing records where compatible.

| Record | Information |
|---|---|
| HistoricalEntity | Stable identity of people, institutions, polities, locations, and organizations |
| HistoricalAssertion | Dated sourced information about an entity |
| HistoricalEvent | Recorded occurrences and consequences |
| HistoricalEventPlan | Conditional prospective historical events |
| HistoricalSource | Sources, citations, evidence quality, and provenance |
| PoliticalAuthority | Rulers, offices, claims, jurisdiction, and actual authority |
| TerritorialState | Sovereignty claims, actual control, settlements, and infrastructure |
| DiplomaticRelationship | Alliances, conflicts, truces, recognition, and obligations |
| MilitaryState | Units, personnel, commanders, equipment, readiness, and logistics |
| EconomicState | Population, goods, taxation, revenue, expenditures, trade, and property |
| SocialState | Families, households, legal statuses, careers, and institutions |
| TechnologyState | Available knowledge, tools, manufacture, and adoption |
| HistoricalStartProfile | A date-specific historical initialization manifest |
| ScenarioStart | A specific playable opening within a historical period |
| CampaignState | The actual persistent state of a particular playthrough |

These categories must not automatically become separate databases or duplicate Core records.

#### 15. Stable historical identity

Every persistent entity needs a stable identifier.

Examples:

```text
polity.england
polity.france
polity.scotland
polity.brittany
polity.burgundy

person.edward_iii
person.henry_v
person.charles_vi
person.charles_vii

place.bordeaux
place.calais
place.harfleur

office.english_crown
office.french_crown
```

Identifiers are logical examples, not mandatory final naming conventions.

A person is separate from their title.

A government is separate from its ruler.

A dynasty is separate from a political institution.

A political claim is separate from actual territorial control.

A historical organization retains its identity through personnel changes, succession, contractual service, and political realignment.

#### 16. Reconstructing a historical entry point

For a new campaign:

1. Select the historical entry date and research edition.
2. Load historically valid entities.
3. Load the political, military, economic, technological, social, and geographical state applicable to the starting date.
4. Apply historical events that have already occurred before the selected initialization boundary.
5. Reconcile territorial control, legal authority, diplomatic relations, military strength, inventories, and outstanding obligations.
6. Record unknown, estimated, disputed, and inferred values appropriately.
7. Initialize the campaign's independent authoritative state.
8. Load conditional historical event plans scheduled after the starting date.
9. Begin autonomous simulation.

The same source edition and initialization assumptions must produce reproducible starting conditions.

The past is established; the intended future is conditional.

#### 17. Exact dates and temporal boundaries

The ten primary entry points require precise initialization cutoffs.

Proposed values:

| Entry | Initialization boundary |
|---|---|
| 1337 | 25 May 1337 |
| 1360 | 25 October 1360 |
| 1369 | 1 July 1369 — provisional scenario date |
| 1389 | 19 July 1389 |
| 1415 | 14 August 1415 |
| 1422 | 22 October 1422 |
| 1435 | 22 September 1435 |
| 1444 | 29 May 1444 |
| 1449 | 1 August 1449 |
| 1453 | 20 October 1453 |

These are initialization choices intended to place the opening immediately after important historical developments. They require historical verification before becoming authoritative.

The 1369 date is a scenario convention, not a claimed exact date of a single opening event.

Historical date precision must support exact dates, approximate dates, ranges, calendar conventions, and uncertainty.

Do not turn a year-only source into a falsely precise day.

#### 18. Historical evidence classifications

Each significant historical assertion must distinguish:

- Documented evidence.
- Corroborated evidence.
- Historical inference.
- Disputed interpretation.
- Unknown information.
- Scenario-specific assumption.

Missing information must never automatically equal zero.

Approximate forces must not become exact headcounts.

Contracted military strength is not identical to present or effective strength.

Estimated annual taxation is not the same thing as treasury stock.

A historical claim to a province is not proof of effective occupation.

Each assertion should identify source, scope, date, confidence, and research edition.

#### 19. Temporal world data

A historical world must distinguish:

- Historical existence.
- Legal sovereignty.
- Effective political control.
- Military occupation.
- Administrative jurisdiction.
- Employment and contract relationships.
- Information available to each actor.
- Technology availability.
- Actual resources and capabilities.

For instance, a French king may claim Gascony while an English government administers parts of it and local lords maintain their own privileges and obligations.

These relationships cannot be collapsed into a single national owner field.

#### 20. Geographical hierarchy

Support:

```text
Kingdom / Realm
  Province / Duchy / County
    Lordship / District
      Settlement / Estate
        Building / Fortification / Physical Asset
```

The hierarchy must be able to represent irregular jurisdiction and overlapping claims.

Control of a provincial capital does not automatically transfer every rural settlement.

Capturing a castle does not create control over distant roads.

An army's occupation of a location is distinct from the legal authority to govern it.

#### 21. Strength and resource accounting

All actual resources must use Core's authoritative ledgers.

Track at appropriate scales:

- Population and households.
- Military personnel.
- Livestock and horses.
- Weapons and armour.
- Ships and transport.
- Food and fodder.
- Currency and debt.
- Buildings and fortifications.
- Production and agricultural capacity.
- Workshops, tools, and materials.
- Contracts, obligations, and unpaid wages.

Transfers must debit and credit appropriately.

Resource reservations are not consumption.

Resources in transit have a location.

Forecasts do not create stock.

Scaling from personal simulation to army, city, or national simulation must not create additional personnel, money, or supplies.

---

### PART V — THE HUNDRED YEARS’ WAR HISTORICAL CHRONOLOGY

#### 22. Grand Campaign period

**Conventional beginning:** 1337  
**Conventional military conclusion:** 1453  
**Total historical span:** Approximately 116 years.

The conflict consists of several overlapping wars, truces, territorial disputes, dynastic struggles, and political realignments.

Do not represent it as uninterrupted Anglo-French warfare.

##### Major phases

| Period | Historical designation | General condition |
|---|---|---|
| 1337–1360 | Edwardian War | Major Anglo-French warfare |
| 1360–1369 | Brétigny settlement | Main war suspended; regional conflicts continue |
| 1369–1389 | Caroline War | Renewed French reconquest and English resistance |
| 1389–1415 | Extended truce and intermittent hostility | Diplomacy, internal conflicts, proxy warfare |
| 1415–1453 | Lancastrian War | Renewed English invasion, competing French governments, French recovery |

These labels are convenient historical periodization, not absolute switches controlling every regional conflict.

#### 23. Historical event and truce inventory

The historical library must contain at least the following principal events, with a more detailed event network to be developed from historical sources.

| Date | Event | Historical significance |
|---|---|---|
| 1337 | French confiscation of Guyenne | Conventional opening of the war |
| 1340 | Battle of Sluys | Major English naval victory |
| 1340 | Truce of Espléchin | Temporary Anglo-French suspension |
| 1341 | Breton Succession War | English- and French-supported rival claims |
| 1343 | Truce of Malestroit | Temporary suspension |
| 1345 | Renewed campaigning | Major operations resume |
| 1346 | Crécy | English battlefield victory |
| 1346 | Neville's Cross | Scottish invasion defeated; David II captured |
| 1347 | Capture of Calais | Strategic English continental foothold |
| 1347 | Truce of Calais | Temporary cessation |
| 1347–1350s | Black Death | Major demographic and economic disruption |
| 1355 | Black Prince's campaign | Renewed English offensive |
| 1356 | Poitiers | John II captured |
| 1357 | Bordeaux and Berwick truces | Separate Anglo-French and Anglo-Scottish settlements |
| 1359 | Edward III's invasion | Renewed major campaigning |
| 1360 | Treaty of Brétigny and confirmation at Calais | Major peace settlement |
| 1364 | Battle of Auray | Decisive Breton succession battle |
| 1365 | Treaty of Guérande | Breton succession settlement |
| 1366–1369 | Castilian Civil War | English and French intervention |
| 1369 | Caroline War resumes | French recovery campaign |
| 1372 | Battle of La Rochelle | Castilian-French naval victory |
| 1373 | Anglo-Portuguese alliance | Important Iberian diplomatic relationship |
| 1375 | Truce of Bruges | Anglo-French military suspension |
| 1377 | Renewed hostilities | Truce expires |
| 1385 | French-Scottish cooperation | Expedition and English-Scottish conflict |
| 1385 | Aljubarrota | Major Portuguese victory over Castile |
| 1389 | Truce of Leulinghem | Major long-term Anglo-French suspension |
| 1396 | Richard II–Isabella marriage diplomacy | Reinforcement of peace arrangements |
| 1399 | Accession of Henry IV | English dynastic change |
| 1400 onward | Welsh rebellion | Internal war with international implications |
| 1402–1403 | Renewed Anglo-French hostility | Limited warfare and support for Welsh resistance |
| 1411–1414 | English interventions in French factional politics | Armagnac–Burgundian conflict |
| 1415 | Henry V invades Normandy | Lancastrian War resumes |
| 1415 | Siege of Harfleur | English siege campaign |
| 25 October 1415 | Agincourt | Historical English victory |
| 1417 | Renewed conquest of Normandy | Sustained English offensive |
| 1419 | Assassination of John the Fearless | Major Burgundian political realignment |
| 1420 | Treaty of Troyes | English-backed French succession settlement |
| 1421 | Battle of Baugé | Franco-Scottish victory |
| 1422 | Deaths of Henry V and Charles VI | Rival succession claims |
| 1429 | Relief of Orléans | Major French turning point |
| 1429 | Coronation of Charles VII | Strengthens Valois legitimacy |
| 1435 | Treaty of Arras | Burgundy reconciles with Charles VII |
| 1436 | French recovery of Paris | Major territorial and political change |
| 1444 | Truce of Tours | Main fighting suspended |
| 1445 | French ordonnance-company reforms | Military institutional development |
| 1448 | Franc-archer system | Additional French recruitment institution |
| 1449 | English seizure of Fougères and truce breakdown | Crisis leading to renewed war |
| 1449 | French reconquest of Normandy | Renewed French offensive |
| 1450 | Formigny | English defeat in Normandy |
| 1453 | Castillon | Major English defeat in Gascony |
| 19 October 1453 | Fall of Bordeaux | Conventional military conclusion |

Exact dates, disputed chronology, and causal relationships must be verified and sourced during database population.

The chronology must also include regional events outside the principal Anglo-French campaigns.

#### 24. Other political powers

The historical registry must include appropriate records for:

- Kingdom of England.
- Kingdom of France.
- Kingdom of Scotland.
- Crown of Castile.
- Kingdom of Portugal.
- Kingdom of Navarre.
- Duchy of Brittany.
- Burgundian territorial state and associated territories.
- County of Flanders and its major towns.
- Relevant Low Countries principalities.
- Crown of Aragon where applicable.
- Holy Roman Empire and relevant constituent rulers.
- Bohemian participation where supported.
- Genoese military and commercial participation.
- Welsh political and military interests.
- Relevant papal and ecclesiastical institutions.

Avoid describing every participant as a consistently mobilized national belligerent.

Historical involvement can take the form of royal armies, princely coalitions, commercial pressure, individual service, mercenaries, dynastic alliances, or diplomacy.

---

### PART VI — TEN PRIMARY CAMPAIGN ENTRY POINTS

All ten entries must preserve their political environment, technological limitations, relative power assessments, and faction-specific challenges.

The following records consolidate the intended profile content.

The faction difficulty scale is:

1. Favourable.
2. Manageable.
3. Challenging.
4. Severe.
5. Critical.

These are qualitative evaluations relative to an identified objective. They are not automatic bonuses or penalties.

#### 25. Entry One — 1337: The War Begins

**Principal rulers:** Edward III of England; Philip VI of France.

##### Political environment

England and France enter conflict over territorial and dynastic authority.

Edward III possesses experienced military institutions but fewer demographic and financial resources than France.

Philip VI has a considerably larger kingdom and access to greater potential manpower, but French royal authority operates through powerful vassals, noble families, and regional institutions.

Scotland is already involved in the Second War of Scottish Independence, with David II in exile and the Balliol cause supported by England.

Flemish commerce is strategically important because of the English wool trade.

Brittany's unresolved succession presents a future source of instability.

##### Technology

- Mail with increasing plate reinforcement.
- Coats of plates and developing limb defences.
- Longbows, crossbows, spears, lances, swords, and axes.
- Early gunpowder artillery of limited reliability and availability.
- Siege engines, mining, blockade, and fortified castles.
- Maritime warfare involving sailing ships, missile fire, and boarding.
- Slow land and maritime communication.

##### Relative strength

France has the larger overall resource base.

England possesses experienced leadership, mobilization capacity, and maritime-commercial opportunities.

Scotland is politically divided and militarily under pressure.

Flemish towns possess economic leverage but are not a single unified political actor.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| England: defend Gascony and organize alliances | 3 |
| England: conquer the French crown | 5 |
| France: enforce royal rights over Guyenne | 3 |
| Bruce loyalists: restore Scottish royal control | 4 |
| Balliol supporters: secure the Scottish crown | 4 |
| Flemish urban interests: defend trade and autonomy | 3 |

##### Available character directions

English and French retainers, Gascon nobles, Scottish Bruce or Balliol supporters, merchants, farmers, Flemish traders, sailors, craftsmen, independent professionals, and noble households.

Scottish origin must not automatically impose allegiance to either Scottish political faction.

##### Event status

The Black Death, Crécy, Poitiers, and the major later treaties have not occurred.

They exist as future historical plans where appropriate.

---

#### 26. Entry Two — 1360: The Peace of Brétigny

**Principal rulers:** Edward III; John II of France.

##### Political environment

England has obtained major territorial and diplomatic advantages.

France has experienced severe military defeats, royal captivity, financial pressure, population losses, and internal unrest.

The territorial settlement creates new administrative responsibilities and disputes over implementation.

Brittany's succession war remains unresolved.

Scotland's David II has returned from captivity but remains burdened by ransom commitments.

##### Technology

- Expanding plate protection.
- Longbows and crossbows remain major weapons.
- Developing artillery.
- Fortified towns and castles retain strategic importance.
- Significant disease and population damage.
- No modern epidemic medicine.

##### Relative strength

England holds a favourable diplomatic position but faces substantial costs governing continental territories.

France retains significant underlying resources but is weakened.

Demobilized soldiers and military companies become important actors.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| England: consolidate French territories | 3 |
| France: restore government and taxation | 4 |
| France: immediately overturn the settlement | 5 |
| Montfort supporters: win the Breton succession | 3 |
| Blois supporters: maintain their claim | 3 |
| Scotland: protect independence and manage obligations | 3 |

##### Character opportunities

Discharged veterans, independent mercenaries, free companies, garrison contractors, estate managers, merchants, reconstruction workers, nobles, artisans, and civilians.

##### Special requirement

Military service ending does not delete soldiers or companies.

Veterans retain their property, experience, relationships, injuries, finances, and history.

Future peace breakdown remains conditionally scheduled.

---

#### 27. Entry Three — 1369: The Caroline War

**Principal rulers:** Charles V of France; Edward III of England.

##### Political environment

The settlement of 1360 breaks down.

France has rebuilt considerable administrative and strategic capability.

England controls extensive continental possessions but faces financial and political difficulties defending them.

Gascon nobles possess competing legal and political obligations.

The Trastámara dynasty has emerged victorious in Castile, creating important French-aligned naval and diplomatic opportunities.

Brittany remains politically distinct and must balance its interests.

##### Technology

- Increasingly advanced plate components.
- Siege warfare and mobile raiding remain central.
- Gunpowder artillery remains logistically constrained.
- Maritime logistics become strategically critical.
- Territorial control depends on garrisons and local cooperation.

##### Relative strength

France has improving organization and strategic opportunities.

England retains significant military capability but is overextended.

Castile possesses important naval resources.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| France: recover English-held territory | 3 |
| England: preserve its enlarged Aquitanian position | 4 |
| Gascon nobles: increase autonomy | 4 |
| Castile: stabilize its monarchy and alliance | 3 |
| Brittany: preserve ducal autonomy | 3 |

##### Character opportunities

Gascon retainers, French and English contract soldiers, Castilian sailors, naval specialists, Breton nobles, merchants, engineers, mercenary companies, and independent travellers.

##### Special requirement

A Gascon noble's nationality, feudal obligations, property, employment, and political alignment must be recorded separately.

---

#### 28. Entry Four — 1389: The Long Truce

**Principal rulers:** Richard II of England; Charles VI of France.

##### Political environment

England and France enter a major truce after prolonged conflict.

France has recovered much of its lost territory but remains economically damaged and politically influenced by powerful magnates.

Richard II faces serious domestic political pressures involving royal authority and noble interests.

Burgundy is increasingly influential.

Scottish and Iberian governments have their own internal interests and separate diplomatic obligations.

Charles VI's later episodes of mental incapacity must not be initialized as already occurring in 1389.

##### Technology

- Sophisticated mail-and-plate equipment.
- Increasing gunpowder artillery usage.
- Traditional cavalry, archery, and fortification warfare.
- Continued dependence on roads, waterways, and sailing vessels.
- Long-term rebuilding after plague and war.

##### Relative strength

France holds the stronger continental territorial position.

England remains militarily credible but faces political difficulties.

Burgundy possesses expanding economic and dynastic influence.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| England: stabilize domestic royal politics | 4 |
| England: preserve peace and remaining possessions | 2 |
| France: rebuild territory and economy | 2 |
| Burgundy: expand influence | 2 |
| Scotland: maintain independence | 3 |
| Iberian powers: maintain regional security | 3 |

##### Character opportunities

Merchants, scholars, court servants, craftsmen, former soldiers, independent professionals, nobles, estate managers, traders, physicians, and families.

##### Special requirement

Entirely civilian careers must be fully viable.

The player does not need to participate in the war.

The truce is part of the initial state, while future political crises and renewed warfare remain conditional historical plans.

---

#### 29. Entry Five — 1415: The Lancastrian Invasion

**Principal rulers:** Henry V of England; Charles VI of France.

##### Political environment

Henry V organizes and begins an invasion of France.

England possesses comparatively cohesive royal leadership and experienced military organization.

France possesses greater underlying resources but is weakened by Armagnac–Burgundian political rivalry.

Charles VI remains king, while recurring incapacity complicates royal government.

John the Fearless and the Burgundian political network retain interests distinct from the Armagnac-led royal administration.

**Burgundy must not be represented as automatically allied with England in 1415.**

James I of Scotland remains captive in England, with Albany exercising governing authority in Scotland.

Brittany and Gascony retain distinct institutions and interests.

##### Technology

- Mature plate harnesses among wealthy soldiers.
- Mail, brigandines, padded armour, and mixed protection.
- Longbows, crossbows, polearms, lances, swords, and cavalry.
- Siege artillery and limited early firearms.
- Disease, sanitation, and supply problems during campaigns.
- Maritime logistics and animal transport.
- Difficult siege warfare against major fortified towns.

##### Relative strength

France possesses the larger potential military and economic base.

England possesses effective expeditionary leadership, but limited resources for long-term overseas campaigning.

Burgundy has significant independent political influence.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| England: execute the invasion | 3 |
| Armagnac-aligned France: resist invasion | 4 |
| Burgundy: preserve influence and autonomy | 3 |
| Scotland: support France militarily | 4 |
| Brittany: preserve autonomy | 2 |
| Anglo-Gascon interests: secure existing positions | 3 |

##### Character opportunities

English military retainers, French defenders, Scottish soldiers seeking foreign service, independent mercenaries, noble squires, court officials, merchants, shipwrights, carpenters, armourers, surgeons, natural philosophers, scholars, and craftsmen.

##### Special requirement

This is the foundation for *A Scot's Tale*.

The historical campaign schedule includes Henry V's invasion, Harfleur, and Agincourt.

Those events are expected to occur as recorded unless the simulation changes their prerequisites or outcomes.

---

#### 30. Entry Six — 1422: Two Kings, One Crown

**Principal rulers/claimants:** Henry VI; Charles VII.

##### Political environment

Henry V and Charles VI have died.

Henry VI is an infant recognized by the Lancastrian government as heir to the English and French crowns under the Treaty of Troyes.

Charles VII asserts his rival French royal claim.

The Lancastrian administration controls important northern territories, including Normandy and Paris, with Burgundian cooperation.

Charles VII governs from the territory remaining under Valois authority.

Philip the Good rules Burgundy and possesses considerable independent resources.

Scottish soldiers have participated in the Valois war effort, while James I remains captive in England.

##### Technology

- Established plate armour.
- Traditional missile infantry remains important.
- Siege artillery increasingly useful.
- Extensive costs of garrisons and occupation.
- Slow communications and contested administration.

##### Relative strength

The Lancastrian-Burgundian alignment possesses a strong immediate strategic position.

Charles VII faces substantial military and fiscal difficulties.

Burgundy has extensive bargaining power and independent resources.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| Lancastrian England: hold northern France | 3 |
| Lancastrian England: fully secure both crowns | 4 |
| Charles VII: establish undisputed French rule | 5 |
| Burgundy: protect autonomy and influence | 2 |
| Scotland: sustain French military assistance | 4 |
| Northern French communities: protect privileges | 4 |

##### Character opportunities

Lancastrian retainers, Valois supporters, Burgundian military households, Scottish soldiers, administrators, townspeople, mercenaries, merchants, scholars, and noble families.

##### Special requirement

The two rival French governmental networks must remain distinct.

They may claim the same crown without possessing the same institutions, personnel, finances, armies, or territory.

---

#### 31. Entry Seven — 1435: The Burgundian Reversal

**Principal rulers:** Charles VII; Henry VI; Philip the Good.

##### Political environment

The Treaty of Arras reconciles Burgundy with Charles VII.

England loses crucial Burgundian diplomatic support.

The Duke of Bedford has recently died.

French legitimacy and political strength have improved, but England still controls Normandy and important continental possessions.

Burgundy remains powerful and autonomous.

##### Technology

- Mature articulated plate armour.
- Longbows and crossbows remain important.
- Developing artillery and siege organization.
- Professional soldiers, garrison contracts, and military households.
- French military reforms of 1445 and 1448 have not occurred.

##### Relative strength

France is improving strategically.

England faces increased political and military difficulty.

Burgundy holds a favourable position for preserving its own institutions and territory.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| France: recover territory following Arras | 3 |
| England: retain northern French holdings | 4 |
| Burgundy: preserve its autonomy and concessions | 2 |
| Brittany: preserve and develop regional influence | 2 |
| Scotland: balance internal authority and French relations | 3 |
| Anglo-Norman nobles: protect their position | 4 |

##### Character opportunities

Diplomatic servants, intelligence agents, merchants, Burgundian retainers, Norman garrison soldiers, military contractors, administrators, and civilian specialists.

##### Special requirement

The Treaty of Arras changes diplomatic relationships and obligations.

It does not automatically transfer every Burgundian soldier, merchant, servant, fortress, treasury, or other asset into direct French ownership or command.

---

#### 32. Entry Eight — 1444: The Last Truce

**Principal rulers:** Charles VII; Henry VI.

##### Political environment

The Treaty of Tours suspends major fighting.

France has recovered much of its political and economic strength.

England retains Normandy, Gascony, and Calais but faces financial and political difficulties.

Burgundy is a powerful separate political actor.

Brittany maintains ducal interests.

Scotland is experiencing minority government and noble competition.

##### Technology

- Advanced plate armour.
- Conventional bows and crossbows.
- Developing artillery.
- Existing royal military institutions and contract forces.
- Significant logistical and fiscal limitations.
- No mature modern scientific or industrial infrastructure.

##### Relative strength

France is increasingly strong institutionally.

England retains experienced military establishments and possessions but struggles financially.

Burgundy has extensive wealth and commercial influence.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| France: strengthen government and military systems | 2 |
| England: negotiate permanent territorial security | 4 |
| England: maintain peaceful continental administration | 3 |
| Burgundy: expand economic prosperity | 2 |
| Brittany: maintain autonomy | 2 |
| Scotland: strengthen royal authority | 3 |

##### Character opportunities

Former soldiers, mercenaries, merchants, scholars, natural philosophers, engineers, artisans, administrators, military reformers, estate managers, and professional specialists.

##### Special requirement

France's future ordonnance reforms of 1445 and franc-archer system of 1448 must **not** be initialized as completed in 1444.

However, their development should exist as conditional historical future plans.

If the government retains the relevant incentives and capabilities, they are expected to occur on the historical schedule.

They may be changed, accelerated, delayed, prevented, or replaced through simulation.

---

#### 33. Entry Nine — 1449: The Final Campaigns

**Principal rulers:** Charles VII; Henry VI.

##### Political environment

The Truce of Tours has broken down.

France possesses the strategic initiative and improved military institutions.

French-Breton cooperation strengthens operations against English Normandy.

England retains experienced troops and substantial fortifications but faces financial and leadership difficulties.

Burgundy remains a separate political power.

##### Technology

- Organized royal artillery.
- Improved siege gun manufacturing and deployment.
- Professional military organizations.
- Mature plate armour.
- Continued use of longbows and crossbows.
- Significant powder, transport, engineering, and ammunition requirements.

##### Relative strength

France possesses a strong strategic advantage in organization, finances, artillery, and regional cooperation.

England retains military capabilities but has difficulty sustaining the defence of Normandy.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| France: reconquer Normandy | 2 |
| England: retain Normandy | 5 |
| Brittany: support France while protecting ducal interests | 2 |
| Anglo-Norman nobility: retain estates and offices | 4 |
| Anglo-Gascon interests: preserve security | 3 |
| Burgundy: preserve autonomy and neutrality where useful | 2 |

##### Character opportunities

Artillerists, engineers, English garrison soldiers, Breton contractors, military logisticians, professional soldiers, merchants, siege specialists, and independent suppliers.

##### Special requirement

A player selecting engineer or artillery service does not receive free specialist equipment, skilled workers, workshops, materials, or military authority.

Such capabilities must actually exist or be acquired.

Historical French advantages are real starting conditions, not guaranteed future victories.

---

#### 34. Entry Ten — 1453: The Aftermath

**Principal rulers:** Charles VII; Henry VI.

##### Political environment

France has recovered Bordeaux and the principal English holdings in Gascony.

England retains Calais.

Henry VI's government faces severe leadership and political difficulties.

France must integrate recovered territories while managing property, jurisdiction, taxation, and regional privileges.

Burgundy and Brittany remain important regional powers.

Scotland continues to pursue its own political objectives.

##### Technology

- Mature plate harnesses.
- Advanced late-medieval artillery relative to earlier campaign periods.
- Established French paid military formations.
- Continued importance of conventional weapons.
- Premodern medicine, communications, and transportation.
- Growing institutional capabilities but no industrial-era technologies.

##### Relative strength

France possesses the strongest continental military and territorial position.

England has suffered major defeats but retains the resources of an established kingdom.

Burgundy remains economically powerful.

Brittany and Scotland retain political autonomy and their own institutional interests.

##### Difficulty

| Alignment and objective | Difficulty |
|---|---|
| France: integrate recovered territories | 2 |
| France: resist immediate renewed English intervention | 2 |
| England: stabilize royal government and preserve Calais | 4 |
| England: immediately reconquer Gascony | 5 |
| Pro-English Gascon interests: retain property and status | 5 |
| Burgundy: preserve prosperity and autonomy | 2 |
| Brittany: protect ducal privileges | 2 |
| Scotland: consolidate royal authority | 3 |

##### Character opportunities

Veterans, merchants, displaced families, administrators, scholars, mercenaries, artisans, engineers, property claimants, nobles, and civilian households.

##### Special requirement

1453 is not a termination condition.

Characters and institutions may continue for generations or centuries.

No later war, dynasty, technological transition, or other historical event is guaranteed merely because it occurred in actual history.

An adopted future-period historical library may extend conditional baseline planning beyond 1453.

---

### PART VII — NATION STRENGTH & FACTION DIFFICULTY

#### 35. Nation strength

Do not represent a kingdom by one unexplained universal strength statistic.

Nation strength must be derived from actual state:

1. Military capacity.
2. Operational readiness.
3. Financial capacity.
4. Territorial control.
5. Logistical reach.
6. Political cohesion.
7. Diplomatic relationships and support.

These are different dimensions and must not be double-counted.

A large population does not automatically create an equally large army.

An alliance does not guarantee immediate allied reinforcements.

A nation's annual revenue does not mean all that money exists in its treasury.

A large army may have insufficient transport, horses, supplies, or political authority to deploy.

#### 36. Faction difficulty

Difficulty is contextual.

The same faction may face a manageable task and an exceptionally difficult task at the same starting date.

For example, in 1415:

- England invading Normandy may be challenging.
- England completely conquering and governing France may be critical.
- An English merchant establishing a business may have different concerns entirely.

Faction difficulty should depend on:

```text
Actor or Faction
+ Objective
+ Starting Date
+ Geographic Conditions
+ Available Capabilities
+ Resources
+ Opposition
+ Political Circumstances
+ Time Horizon
```

Difficulty is a presentation and planning view derived from existing facts.

It must not secretly increase enemy power or penalize the player to preserve challenge.

Success, peace, wealth, institutional stability, and ordinary life are valid outcomes.

---

### PART VIII — CHARACTER CREATION & LIFE PATHS

#### 37. Individual identity

Characters must possess independently recorded identity and background attributes.

Possible fields:

```yaml
ActorIdentity:
  name:
  birth_date:
  birthplace:
  national_origin:
  cultural_background:
  languages:
  legal_statuses:
  residence:
  family_relationships:
  education:
  previous_employment:
  skills:
  personal_history:
```

None of these automatically imposes employment or political allegiance.

Nationality and origin may affect language, reputation, legal rights, access, prejudice, obligations, and opportunities where historically appropriate.

They do not create universal faction eligibility locks.

#### 38. Life-path creation

A character's life path may contain:

- Family and childhood.
- Social conditions.
- Household occupation.
- Education and apprenticeship.
- Military or civilian experience.
- Travel and migration.
- Former employment.
- Existing contracts.
- Relationships and patronage.
- Property and possessions.
- Financial obligations.
- Injuries and other persistent conditions.
- Career objectives.

Established backgrounds must remain consistent with the selected date.

A new character is not automatically assumed to possess a historical position merely because the player selects a career direction.

#### 39. Character control perspectives

Support:

**Existing historical or fictional individual**

Player takes control of an eligible established actor, subject to appropriate starting circumstances.

**New character**

Player creates an individual whose background and initial resources are validated against the historical setting.

**Institutional perspective**

Player controls an eligible government, organization, military command, business, or other institution through explicitly defined authority.

The player does not personally become every member of that institution.

Institutional control does not grant unlimited command over unaffiliated actors or unlimited resources.

---

### PART IX — CAREERS, EMPLOYMENT & MERCENARY SERVICE

#### 40. Careers are arrangements, not classes

A character may begin as:

| Arrangement | Example |
|---|---|
| Independent civilian | Farmer, traveller, artisan |
| Permanent employee | Steward of a noble household |
| Military retainer | Soldier retained by a lord |
| Individual mercenary | Combatant accepting short-term service |
| Free-company member | Soldier in an autonomous military company |
| Professional contractor | Engineer, surgeon, interpreter, shipwright |
| Foreign service member | Scottish-born soldier serving English forces |
| Scholar or institutional specialist | Natural philosopher, physician, administrator |
| Multiple-client contractor | Merchant or specialist serving several clients |
| Unemployed individual | Former soldier or apprentice seeking work |
| Institution-level controller | Authorized government or organizational perspective |

These are not permanent character classes.

Characters may change occupations, employers, relationships, and social positions through play.

The simulation must support ordinary professional advancement and long-term careers as seriously as military advancement.

#### 41. Employment relationships

Employment and institutional affiliation must distinguish:

- Employer.
- Employee or contractor.
- Actual employment status.
- Recruitment application.
- Offer.
- Contract.
- Duties.
- Authority.
- Compensation.
- Duration.
- Exclusivity.
- Termination.
- Historical service record.

A character pursuing a position is not already employed.

A recruitment opportunity is not a guaranteed appointment.

An accepted contract does not necessarily change nationality or permanent political allegiance.

#### 42. Mercenary contracts

Mercenary employment must be a fully supported activity.

Contract records should contain:

| Contract field | Purpose |
|---|---|
| Employer | Hiring person or institution |
| Contractor | Individual or company |
| Assignment | Mission, garrison, escort, expedition, protection, etc. |
| Duration | Fixed term, specified task, campaign, or termination condition |
| Compensation | Money, provisions, rewards, advances, or other consideration |
| Equipment obligations | Who supplies and maintains equipment |
| Command authority | Orders the contractor is required to obey |
| Exclusivity | Whether simultaneous contracts are permitted |
| Legal and political obligations | Relevant service restrictions and jurisdictions |
| Liabilities | Debts, arrears, breaches, and disputes |
| Termination | Expiry, completion, dismissal, release, or breach |

Contracts create obligations, not automatic ownership over a person.

A mercenary can serve multiple employers over their lifetime.

Several simultaneous contracts are possible where their terms and resources permit them.

A mercenary may establish or join an independent company.

#### 43. Autonomous military companies

An independent company must remain a persistent organization with:

- Stable identity.
- Leadership.
- Personnel and recruitment.
- Internal hierarchy.
- Property.
- Equipment.
- Horses and transport.
- Finances.
- Supplies.
- Current contracts.
- Former contracts.
- Reputation and relationships.
- History and succession.

A contract's expiration does not delete the company.

A company dismissed from royal service may seek another employer, disband gradually, reorganize, enter civilian trade, or take other autonomous actions.

Those outcomes require actual decisions and causal state changes.

#### 44. Civilian institutions

The Hundred Years’ War must include civilian organizations such as:

- Farming households.
- Noble households.
- Estates.
- Merchant associations.
- Guilds.
- Workshops.
- Universities and schools.
- Religious institutions.
- Municipal governments.
- Maritime commercial enterprises.
- Construction organizations.
- Professional networks.
- Financial institutions appropriate to the period.

A kingdom's economy cannot consist solely of armies and taxes.

People and institutions continue ordinary activity during war and peace.

---

### PART X — TECHNOLOGY, EDUCATION & SCIENTIFIC DEVELOPMENT

#### 45. Historical technological baselines

Each entry point loads technology appropriate to its date.

This means:

- 1337 does not have the military organization or artillery infrastructure of 1453.
- 1415 does not have modern firearms.
- 1444 does not automatically contain the French reforms established historically in subsequent years.
- 1453 has capabilities that did not exist or were not widely adopted in earlier periods.

Technology must distinguish:

1. Historical existence.
2. Underlying knowledge.
3. Regional availability.
4. Materials and manufacturing.
5. Specialist expertise.
6. Actual equipment possession.
7. Operational readiness.
8. Dissemination and adoption.

The historical technology library defines initial conditions, not absolute future restrictions.

#### 46. Alternative technological development

Players and NPCs may accelerate, delay, or redirect technological development.

A character may pursue:

- Engineering.
- Metallurgy.
- Mechanical innovation.
- Medicine.
- Agricultural techniques.
- Shipbuilding.
- Fortification design.
- Artillery manufacturing.
- Mathematics.
- Natural philosophy.
- Scientific experimentation.

Research requires feasible access to knowledge, materials, tools, time, experience, skilled assistance, and patronage where applicable.

A character's idea does not automatically create a working invention.

A successful prototype does not automatically create mass production.

A technology being discovered does not automatically make it known across Europe.

An invention may appear centuries earlier than historically recorded if the simulation genuinely supports its development.

The consequences must then be propagated through actual production, communication, economics, military use, and institutional adoption.

#### 47. Historical research events and technology

Historical innovations can be included as conditional planned events.

For example, the French military reforms of 1445 and 1448 may occur as historically recorded when the underlying political, financial, and military conditions remain intact.

If the player helps establish a different military institution in 1442, those events must be reevaluated.

The historical reform might occur in altered form, be accelerated, become unnecessary, or fail.

---

### PART XI — A SCOT'S TALE INTEGRATION

#### 48. Campaign placement

**Grand Campaign:** The Hundred Years’ War  
**Sub-Campaign:** 1415 — The Lancastrian Invasion  
**Starting Scenario:** A Scot's Tale  
**Primary controlled character:** Ian Tormod Cameron

*A Scot's Tale* is a pre-designed character scenario within the 1415 historical period.

It must not become a separate duplicate historical engine or disconnected version of the 1415 world.

#### 49. Established character background

| Attribute | Established information |
|---|---|
| Name | Ian Tormod Cameron |
| Birth date | 5 May 1398 |
| Birthplace | Lochaber, Scotland |
| National origin | Scottish |
| Cultural background | Highland Scottish |
| Family | Parents' rural household; no siblings |
| Upbringing | Rural farm life |
| Travel | Journey from Scotland with a Welsh merchant |
| Career direction | English military service |
| Nationality change | Not required |
| Relevant household | Sir Richard Wycliffe's service, at the appropriate later checkpoint |

These are existing character-background facts.

Do not invent additional family details, political commitments, or service history.

#### 50. Two different AST starting states

##### Recruitment-yard opening

Ian has travelled to England and is seeking service.

He has not automatically completed later recruitment events.

His sponsorship, pledge, appointments, relationships, equipment changes, and career progress must be resolved through actual play.

##### Later established checkpoint

Ian has already entered Sir Richard Wycliffe's service.

His relevant prior actions and resulting relationships are part of that saved campaign's authoritative history.

These two configurations cannot be conflated.

Do not apply later developments retroactively to the recruitment-yard opening.

#### 51. Exact-date reconciliation

The principal 1415 campaign entry corresponds to Henry V's August invasion.

However, AST's recruitment-yard opening takes place in England.

The starting scenario therefore needs its own exact opening date and location.

That opening must be reconciled with the historical world state and scheduled events at that particular date.

Do not silently start the English recruitment-yard scenario on the day of the Normandy landing merely because both belong to the 1415 Sub-Campaign.

#### 52. Scottish nationality and English service

Ian's Scottish origin does not prohibit English service.

Recruitment may involve:

- Location.
- Sponsorship.
- Existing obligations.
- Practical competence.
- Reputation.
- Political suspicion.
- Institutional procedures.
- Available positions.
- The prospective employer's authority and decisions.

A Scottish character serving an English noble does not automatically change national origin or cultural identity.

The system should also support contractual rather than permanent political allegiance.

#### 53. Scenario continuity

AST must use the same:

- Core event rules.
- Military systems.
- Political relationships.
- Historical event plans.
- Economic systems.
- Technology.
- Society and institutions.
- Character progression.
- Persistent world accounting.

Player actions within AST may alter historical events just as actions in another 1415 scenario may.

The scenario should not shield historical outcomes from consequences caused by Ian or other simulated actors.

---

### PART XII — STARTING SCENARIOS & WEBSITE FLOW

#### 54. Campaign selection

The intended website flow is:

```text
Select Grand Campaign
        ↓
The Hundred Years' War
        ↓
Choose Historical Starting Period
        ↓
Choose Pre-designed or Custom Start
        ↓
Choose Controlled Perspective
        ↓
Character Identity and Background
        ↓
Starting Career or Arrangement
        ↓
Optional Institutional Relationships
        ↓
Review Historical Starting Conditions
        ↓
Initialize Independent Campaign
```

Players should be able to inspect historical political conditions, technology, faction strength, career possibilities, and major historical context before starting.

The interface must distinguish what happened before the entry date from historical events expected afterward.

#### 55. Starting scenarios

The initial proposed scenarios for the 1415 period are:

##### A Scot's Tale

A Scottish Highlander enters English military service while pursuing a personal military and social career.

##### A Soldier for Hire

An independent military professional seeks employment among competing Western European powers.

##### Across the Channel

A merchant seeks commercial opportunities despite warfare, political restrictions, and regional economic disruption.

##### The Scholar's Pursuit

A scholar or craftsperson seeks knowledge, patronage, employment, and opportunities for experimentation.

##### Custom Beginning

The player creates a new individual or eligible institution-based perspective and defines an appropriate starting situation.

These scenarios share the historical 1415 foundation.

They differ in character, location, circumstances, relationships, and initial opportunities.

Starting as a merchant does not prevent military service later.

Starting as a soldier does not prevent scholarly work or civilian life.

#### 56. Character creation interface

Do not combine nationality and military allegiance as mandatory selections.

Suggested stages:

**Identity and Origin**

Birthplace, cultural background, nationality, family, personal history.

**Education and Capabilities**

Education, skills, experience, qualifications, languages, and relevant knowledge.

**Current Circumstances**

Residence, employment, property, family situation, resources, and obligations.

**Career Direction**

Independent, civilian, mercenary, military retinue, professional service, scholarly work, institutional employment, or another pursuit.

**Institutional Relationships**

Existing membership, employment, contracts, service applications, sponsorships, or no affiliation.

**Starting Confirmation**

Review established facts, unresolved choices, historical date, world conditions, and current relationships.

#### 57. Service interface

When a player chooses a service-related beginning, ask whether the character:

- Already holds a position.
- Has an existing offer.
- Is seeking employment.
- Has completed former service.
- Belongs to an independent organization.
- Wishes to begin without a current arrangement.

Only organizations existing in the selected world state should appear as possible employers or institutions.

Potentially approachable organizations are not guaranteed to accept the character.

The player's control perspective, origin, and desired employer must remain separate fields.

---

### PART XIII — AUTONOMOUS WORLD & GENERATIONAL SIMULATION

#### 58. Autonomous actors

All relevant actors continue to act independently from the player, including:

- Governments.
- Nobles.
- Military commanders.
- Soldiers.
- Households.
- Merchants.
- Businesses.
- Towns.
- Universities.
- Religious institutions.
- Mercenary companies.
- Political factions.
- Agricultural communities.

Their actions follow goals, knowledge, authority, competence, institutions, obligations, and available resources.

Historical event plans guide their intended default behaviour while history remains intact.

They do not eliminate autonomy.

#### 59. Generational continuity

Characters and institutions may persist across decades or centuries.

Record:

- Births and deaths.
- Marriage and kinship.
- Children and descendants.
- Succession and inheritance.
- Estate ownership.
- Business continuity.
- Institutional history.
- Relationships.
- Careers.
- Technological knowledge.
- Fortifications and infrastructure.
- Debts and contractual obligations.
- Military organizations.
- Political changes.

Player characters may die while the world continues.

The system should support succession to an eligible descendant or another authorized actor without retroactively modifying the prior character's decisions.

#### 60. Long-term time scale

Support simulation at individual, local, regional, national, and broader scales.

Historical summarization may use:

- Annual summaries.
- Five-year periods.
- Twenty-five-year periods.
- Cumulative century histories.
- Five-hundred-year epochs for very long playthroughs.

These are summary views, not resets.

A time-scale change must preserve total resources, personnel, population changes, institutions, projects, technology, and historical events.

Fast-forwarding across a scheduled historical event must not ignore its prerequisites or duplicate its consequences.

No automatic disappearance of mercenary companies, businesses, or households merely because time has advanced.

---

### PART XIV — PERSISTENCE & MULTIPLE CAMPAIGNS

#### 61. Independent playthroughs

Two campaigns starting in 1337 use the same historical baseline but maintain separate authoritative states.

One may follow history closely.

Another may produce an early English victory, independent Gascony, a different French succession, or a prolonged peace.

They must not share mutable campaign history.

#### 62. Historical research versions

Separate:

**HSDB Schema Version**

Defines how historical records are stored and interpreted.

**Historical Research Edition**

Defines which historical evidence, dates, entities, and interpretations initialize a world.

**Campaign Initialization Version**

Defines the starting date, scenario, enabled rules, assumptions, and overrides.

**Campaign State Version**

Tracks the active playthrough's authoritative history and state.

Research updates must not automatically modify existing saves.

Where migration is required, it must be explicitly requested, reconciled, documented, and tested.

#### 63. Historical availability versus divergent availability

Starting a new campaign in 1415 uses the historical world of 1415.

Advancing a campaign begun in 1337 until 1415 uses the world produced by that campaign.

If a player-created mercenary company survives from 1370 to 1415, it remains part of the world.

If a historically important dynasty or institution disappeared earlier in a divergent playthrough, it must not reappear merely because the baseline chronology expects it.

---

### PART XV — CORE INTERFACES & DATA DESIGN

#### 64. Proposed interfaces

The following are logical requirements, not necessarily new databases or final code identifiers.

| Interface | Required information |
|---|---|
| CampaignRegistry | Grand Campaign identity and available historical periods |
| HistoricalStartProfile | Date, historical edition, geography, initialization requirements |
| ScenarioStart | Opening scene, controlled actor, location, prior history, scenario conditions |
| HistoricalEntityRegistry | People, polities, offices, organizations, and places |
| HistoricalEventPlan | Intended future event and causal dependencies |
| HistoricalSourceRegistry | Evidence, references, confidence, and versioning |
| ActorIdentity | Origins, language, culture, legal status, and family |
| ActorLifePath | Upbringing, education, experience, and history |
| OrganizationRegistry | Organization identity, membership, leadership, and resources |
| PoliticalRelations | Treaties, claims, alliances, hostility, and obligations |
| InstitutionalRelationship | Employment, membership, service, authority, and history |
| Contract | Parties, terms, compensation, obligations, termination |
| ServiceApplication | Prospective employer, application, qualifications, decision |
| MilitaryOrganization | Command, personnel, equipment, readiness, logistics |
| WorldTechnology | Knowledge, discoveries, production, adoption, equipment |
| ControlAssignment | Controlled actor or authorized institutional perspective |
| CampaignState | Actual world state and committed history |

Use stable IDs and versioned relationships.

Do not treat summaries as independent stores of truth.

#### 65. Illustrative campaign manifest

```yaml
grand_campaign:
  id: hundred_years_war
  historical_period:
    start: 1337
    end: 1453
  continuation_after_baseline: allowed

historical_mode:
  initialize_actual_past: true
  load_conditional_future: true
  default_course: historical
  divergence_policy: causal
  force_historical_outcomes: false

entry:
  id: hyw.1415
  name: Lancastrian Invasion
  start_date: 1415-08-14
  historical_edition: pending_validation

scenarios:
  - a_scots_tale
  - soldier_for_hire
  - across_the_channel
  - scholars_pursuit
  - custom_beginning

character_creation:
  nationality_required_for_identity: when_applicable
  faction_service_required: false
  independent_careers: true
  foreign_service: true
  concurrent_institutional_relationships: true

world:
  autonomous_actors: true
  resource_continuity: true
  historical_event_plans: enabled
  future_knowledge_leakage: forbidden

simulation:
  authority: IRGS_CORE
  persistent_state: true
  predetermined_end: false
```

This is an illustrative configuration only.

Codex must reconcile its fields with the actual existing project.

---

### PART XVI — REQUIRED HISTORICAL EVENT EXAMPLE: AGINCOURT

#### 66. Historical event plan

Agincourt is the primary integration test for conditional historical events.

##### Historical baseline

**Date:** 25 October 1415  
**Location:** Agincourt  
**Historical outcome:** English victory.

##### Preceding historical pathway

1. Henry V organizes his expedition.
2. The English army crosses the Channel.
3. The army campaigns against Harfleur.
4. Harfleur capitulates.
5. Henry moves toward Calais.
6. French commanders mobilize and intercept.
7. Both armies enter an engagement.
8. The battle occurs.
9. Its historical outcome is an English victory.

These are individual historical actions and events with dependencies, not one automatic script.

##### Intended simulation behaviour

If the historical pathway remains intact, events proceed according to the historical baseline.

If a player alters army supply, military movement, diplomacy, recruitment, siege progress, or other material circumstances, dependent historical plans are reevaluated.

Examples:

**England defeats France historically**

Agincourt follows the historical record if its causal pathway remains intact.

**England loses at Harfleur**

The subsequent march and battle require reevaluation.

**Henry V returns to England**

The historical battle may be prevented.

**A French commander changes tactics**

The battle may occur with a different outcome.

**Henry V dies before 1415**

The historical invasion under Henry is impossible. A successor may pursue a new campaign if circumstances permit.

**A mercenary company joins England**

Its actual personnel and supplies may affect the campaign. Its existence does not guarantee a changed outcome merely because it is player-created.

##### Strict accounting rule

No event plan may invent:

- Troops.
- Supplies.
- Weapons.
- Money.
- Casualties.
- Equipment.
- Player decisions.

Historical casualties and force strengths must be drawn from evidence or explicitly identified reconstruction assumptions when necessary.

The simulation must never count the same loss twice.

---

### PART XVII — REQUIRED FUNCTIONAL TESTS

#### 67. Historical initialization tests

| Test | Expected result |
|---|---|
| Start in 1337 | Future historical events remain conditional |
| Start in 1389 | Earlier historical events already occurred |
| Start in 1415 | Agincourt is a scheduled prospective event |
| Start in 1422 | Rival French administrations coexist |
| Start in 1435 | Burgundy's new treaty obligations exist |
| Start in 1444 | Later military reforms are planned but not yet completed |
| Start in 1449 | French military reforms already established historically are present |
| Start in 1453 | War's conventional military conclusion is established |
| Custom starting date | Historically reconstructed state matches the exact cutoff |
| Earlier divergent playthrough reaches 1415 | Uses the simulated world, not a new historical 1415 snapshot |

#### 68. Historical event tests

| Test | Expected result |
|---|---|
| Historical pathway undisturbed | Historical outcome occurs |
| Event's required participant dies | Event is reevaluated |
| Required army destroyed | Battle cannot occur as originally planned |
| Invasion delayed | Dependent events are reconsidered |
| Different battle occurs | Event identity and consequences are accurately recorded |
| Earlier equivalent peace established | Later historical treaty may be superseded |
| Player changes an unrelated local condition | Unrelated historical events remain viable |
| Event is prevented | Cannot later fire automatically |
| Actor lacks information | Cannot act on unknown future history |
| Scale change crosses an event date | Event resolves once, preserving accounting |
| Divergent history extends past 1453 | Simulation continues normally |

#### 69. Character and employment tests

| Test | Expected result |
|---|---|
| Scottish nationality with interest in English service | Permitted to seek service |
| No faction affiliation | Character begins normally |
| Mercenary without employer | Remains playable |
| Contract expires | Character and organization persist |
| Employment changes | Old and new relationships are tracked |
| Multiple simultaneous contracts | Terms and conflicts evaluated |
| Scottish scholar approaches French patron | Individual eligibility assessed |
| Merchant changes occupation | Progression remains possible |
| Professional invents technology | Requires actual capabilities and resources |
| Player selects AST recruitment opening | Later sponsorship is not preloaded |
| Player selects established AST checkpoint | Prior events are retained |
| Institutional control begins | Player receives only authorized control |
| Organization outlives its founder | Continuity is preserved |
| Character dies | World and other actors continue |

#### 70. Accounting and simulation tests

Test:

- Routine activity.
- Failure.
- Mixed outcomes.
- Scarcity.
- Simultaneous events.
- Recruitment and dismissal.
- Military casualties.
- Resource transfer.
- Supply movement.
- Contract expiration.
- Historical treaty implementation.
- Government succession.
- Time-scale changes.
- Technological invention.
- Autonomous institutional activity.
- Multiple campaign saves.
- Historical divergence.
- Save and reload.
- Historical research version migration.

No action, resource, obligation, or casualty should be duplicated through subsystem interaction.

Successful character actions must not be reversed solely to maintain historical difficulty.

---

### PART XVIII — CMRR RECONCILIATION

#### 71. Required source precedence and merging

This consolidated document incorporates several design stages.

Codex must explicitly reconcile overlapping requirements rather than choosing one source silently.

##### Important supersession

An earlier Campaign Design Integration document stated:

> Subsequent history is not scripted.

It also instructed that no predetermined historical future event or outcome should exist.

**That requirement has been superseded.**

The current governing rule is:

> Subsequent history has an intended historical event schedule. Events proceed according to the historical baseline unless simulation changes the circumstances producing them.

This does not authorize rigid scripted history or forced outcomes.

The intended result is conditional historical progression.

##### Reconciliation matrix

| Feature | Disposition |
|---|---|
| Ten historical entry points | Retain |
| Historical political descriptions | Retain and validate |
| Historical technological limits | Retain as starting-state conditions |
| Relative national strength | Retain as derived analytical views |
| Faction difficulty | Retain and clarify as objective-specific |
| Historical past before entry | Establish as actual history |
| Historical future after entry | Replace reference-only model with conditional event plans |
| Historical outcome guarantees | Reject |
| Player-driven divergence | Retain and expand |
| Autonomous NPC reactions | Retain |
| Nationality separate from allegiance | Required |
| Optional faction affiliation | Required |
| Independent and civilian careers | Required |
| Mercenary organizations and contracts | Expand |
| Multiple institutional relationships | Required |
| Foreign military service | Required |
| Scientific development | Expand |
| Technology locked to historical year forever | Reject |
| Multiple scenarios per entry period | Required |
| A Scot's Tale integration | Retain and reconcile |
| Historical database duplication | Reject |
| Core authority over simulation | Retain |
| Historical events beyond initial cutoff | Load conditionally |
| Mandatory ending in 1453 | Reject |
| Generational continuation | Required |
| Retroactive migration | Prohibited without authorization |
| Core resource duplication | Prohibited |
| Future historical knowledge available to NPCs | Prohibited |

#### 72. Historical accuracy versus simulated history

Historical accuracy means:

- Correct initial conditions.
- Correct historically intended event plans.
- Correct political and technological circumstances.
- Correct documented institutions, relationships, and geography.
- Accurate treatment of uncertainty.

It does not mean:

- Forcing predetermined victories.
- Ignoring player actions.
- Artificially restoring destroyed armies.
- Preventing early invention.
- Making diplomacy always follow the historical record.
- Ending the world when the recorded conflict ends.

An undisturbed historical campaign should closely follow recorded history.

A materially altered one should follow its new causes.

---

### PART XIX — DEVELOPMENT SEQUENCE FOR CODEX

#### 73. Phase One: Audit and compatibility

Inspect:

- Core 3.3 Live.
- Existing campaign structures.
- Current historical modules.
- Website and campaign-selection implementation.
- Character-creation structures.
- Event scheduler.
- Simulation state.
- Persistence and saves.
- Test suite.
- Existing AST campaign data.

Produce an actual source and dependency inventory.

Do not presume that conceptual schema names in this document match existing implementation names.

#### 74. Phase Two: Historical registry

Implement or reconcile:

- Grand Campaign registry.
- Historical Sub-Campaign registry.
- Ten primary entries.
- Additional date support.
- Scenario registry.
- Stable historical entity identity.
- Starting-date reconstruction.

#### 75. Phase Three: Historical event timeline

Implement or reconcile:

- Immutable historical baseline.
- Conditional future plans.
- Trigger evaluation.
- Hard and supporting prerequisites.
- Event dependencies.
- Divergence propagation.
- Rescheduling.
- Alteration and prevention.
- Event identity.
- Historical outcome defaults.
- Historical information separation.

#### 76. Phase Four: Political and world state

Populate or integrate:

- Rulers and claims.
- Governments and regencies.
- Territorial control.
- Political institutions.
- Diplomacy.
- Military organizations.
- Economic structures.
- Historical technologies.
- Social institutions.
- Historical sources.

Use documented facts and mark gaps.

#### 77. Phase Five: Character and career integration

Implement or reconcile:

- Character background.
- Family and upbringing.
- Education and skills.
- Optional affiliation.
- Civilian professions.
- Foreign military service.
- Mercenary companies.
- Contracts and applications.
- Institutional control perspectives.
- Career changes.
- Independent livelihoods.

#### 78. Phase Six: Starting scenario manager

Integrate:

- A Scot's Tale.
- Custom historical beginnings.
- Pre-designed character scenarios.
- Scenario-specific dated locations.
- Existing saved checkpoints.
- Optional initial employment.
- Historical state validation.

Do not merge incompatible checkpoints.

#### 79. Phase Seven: Website integration

Create a coherent campaign selection and character creation interface.

The player should be able to:

1. Select the Hundred Years’ War.
2. Browse the ten historical periods.
3. Review political conditions and historical context.
4. Review technological conditions.
5. Inspect faction-specific strategic challenges.
6. Choose a scenario or custom start.
7. Create or select a controlled perspective.
8. Establish identity independently of allegiance.
9. Select optional career and affiliation arrangements.
10. Review all initialization details.
11. Start an independent persistent campaign.

The interface should present accurate options generated from the selected historical state.

#### 80. Phase Eight: Testing and validation

Run all relevant acceptance and regression tests.

Test the complete 1415 flow as an initial end-to-end example:

- Historical state reconstruction.
- Character creation.
- Optional foreign service.
- Military recruitment.
- Event planning.
- Harfleur and Agincourt dependencies.
- Autonomous NPC reactions.
- Resource accounting.
- Save and reload.
- Divergence.
- Historical-state comparison.

Do not describe these tests as completed unless they actually execute.

#### 81. Phase Nine: Documentation and CMRR resubmission

Deliver:

- Rebuilt architecture and integration specification.
- Updated implementation.
- Complete source comparison.
- Change log.
- Reconciliation matrix.
- Accounted removals and deprecations.
- Test results.
- Historical research gaps.
- Quantitative calibration needs.
- Known bugs and unresolved issues.
- Migration impact.
- Final implementation status.

Do not present design consistency as evidence of balance, accuracy, or successful playtesting.

---

### PART XX — HISTORICAL RESEARCH REQUIREMENTS

#### 82. Source standards

Where possible, research should prioritize:

- Historical royal and administrative records.
- Muster and military payment records.
- Treaty texts.
- Financial and taxation records.
- Municipal and territorial documents.
- Academic historical studies.
- Military and technological scholarship.
- Peer-reviewed research.
- Relevant museum and archival collections.

Useful starting resources include:

- The National Archives, United Kingdom.
- The Medieval Soldier project.
- The Gascon Rolls project.
- Royal Armouries.
- French departmental and national archives.
- Scholarly histories of the Hundred Years’ War.
- Academic studies of medieval political institutions, economies, and military logistics.

Document every historical assertion used as authoritative initialization data.

Do not treat incidental illustration URLs or unrelated images in earlier drafts as historical source material.

#### 83. Incomplete evidence

When research cannot establish exact quantities:

- Preserve unknowns.
- Preserve estimated ranges.
- Record conflicting accounts.
- Distinguish scholarly reconstructions from primary evidence.
- Use explicit scenario assumptions only where operationally necessary.
- Never present provisional values as confirmed historical fact.

A historically grounded simulation should be precise about what is known and equally precise about what is not known.

---

### PART XXI — FINAL DESIGN REQUIREMENTS

#### 84. Non-negotiable behaviour

The integrated campaign must satisfy all of the following:

**Historical fidelity**

Starting in 1389 means the historical past up to 1389 has occurred.

**Conditional historical future**

Starting in 1337 loads the events of 1337–1453 as an intended conditional chronology.

**Meaningful divergence**

A player or autonomous actor can change history through causally feasible actions.

**No forced outcomes**

No historical event may violate the authoritative simulation.

**Independent identity**

National origin is not permanent faction allegiance.

**Optional affiliations**

Characters can be unaffiliated, independent, employed, contracted, or members of several compatible institutions.

**Persistent society**

Civilian households, governments, merchants, professional organizations, and military companies continue existing outside the player's direct involvement.

**Historical technology**

Technology begins at its appropriate historical level but may develop differently through simulation.

**True resource accounting**

Money, people, equipment, property, and supplies cannot appear or disappear because a historical event is scheduled.

**Long-term continuity**

The world continues after war, victory, peace, character death, dynastic succession, or 1453.

**Reusable architecture**

The new functionality must serve future historical campaigns and not become an isolated Hundred Years’ War implementation.

#### 85. Intended final product

The intended result is a historical Grand Campaign in which:

A player starting in 1337 enters a living medieval world on the verge of the Hundred Years’ War. History has an intended direction, but the player's actions and the actions of autonomous actors can change it.

A player starting in 1415 enters the world of Henry V's invasion, with the earlier history already established and the historical sequence of Harfleur, Agincourt, and later events intended to proceed unless circumstances change.

A Scottish-born character may pursue English service without losing their national identity.

A mercenary may travel between employers, form a company, change allegiance, or return to civilian life.

A merchant may build a business that survives multiple generations.

A scholar may contribute to technological discoveries that transform the world decades or centuries ahead of their historical development.

A government may preserve peace when history records renewed warfare.

A character may never participate in a battle and still have a complete and consequential life.

**The Hundred Years’ War supplies the historical world and its intended chronology. IRGS Core determines what actually happens.**

---

### FINAL INSTRUCTION TO CODEX

Use this document as the consolidated design target.

First inspect the actual project and identify what already exists. Reconcile the target with the adopted Core and existing campaign systems. Preserve established functions and records, implement missing capabilities at their appropriate architectural layers, and do not silently substitute a rigid historical script or a completely unscheduled sandbox for the conditional historical-timeline system defined here.

Proceed through the development sequence as far as the available project, source material, and execution environment permit.

Deliver the completed work with a full CMRR account, actual test results, outstanding historical research requirements, and any functionality that remains provisional.

**Submission status:** Proposed for reconciliation and implementation. This document does not itself constitute adoption, successful integration, historical-data completion, calibration, or playtesting.

---

## VOLUME B — WORLD & CIVILIZATION INTERFACE (SOURCE v0.1)

### IRGS — World & Civilization Interface

Website & Gameplay Design Specification · Proposed v0.1 · Core Integration

Scope: Interactive World Atlas, Civilization Management, Political Systems, Economies, Military Command, Settlements, Infrastructure, Institutions, and Long-Term World Development.

Design status: Proposed for CMRR reconciliation against IRGS Core 3.3 Live and the existing website. This is a new interface specification, not a claim that all underlying mechanics have been implemented.

#### 1. Purpose and design philosophy

The World & Civilization Interface should let players inspect, understand, influence, and—where they possess legitimate authority—manage the simulated world around them.

It must scale from a single household to an entire civilization without requiring separate game engines or creating independent versions of the world.

A player beginning as a commoner should be able to investigate their neighbourhood, travel between settlements, inspect known businesses, and interact with local institutions.

If they later become a property owner, military officer, merchant, government official, or ruler, the interface should provide the appropriate additional capabilities.

The player's authority, knowledge, and circumstances determine what tools they can use—not their selected campaign genre or an arbitrary gameplay level.

The uploaded Hundred Years' War Grand Campaign Integration v0.4 already establishes the foundations: political authority, militaries, economies, contracts, logistics, information, institutions, technology, historical geography, and persistent campaign state. These must remain owned by their appropriate simulation layers rather than being rebuilt as website-only mechanics.


##### Six governing requirements

1. One authoritative world: Every map, dashboard, ledger, and report refers to the same simulation.
2. Progressive complexity: A civilian does not need to see the administrative tools of a sovereign government.
3. Knowledge-based information: The interface may only reveal information legitimately accessible to the player's perspective.
4. Actual resource accounting: Every person, soldier, building, asset, and item has one authoritative record.
5. Autonomous civilizations: Governments, towns, households, businesses, and military organizations continue acting independently.
6. Indefinite development: A world can evolve from medieval conditions into wholly different political, technological, and economic circumstances without resetting.

The interface should be closer to a combination of an interactive atlas, administrative workspace, and grand-strategy dashboard than a traditional RPG map.

#### 2. The primary World interface

I recommend keeping Story | World | Chronicle as the three principal gameplay views.

Within World View, players gain access to six interconnected workspaces.

WORLD WORKSPACE

#### The Hundred Years' War

Illustrative playthrough · Historical setting

Atlas

Economy

Politics

Military

Settlements

Institutions

##### The World Atlas

Geography, discovered places, roads, rivers, coastlines, borders, and locations.

Known locations

Geographic features

Travel and routes

Territories and claims

Interactive navigation demonstration. These views are different presentations of one world state, not separate simulations.

The six workspaces should not create six independent data stores.

For example, a city-owned warehouse may appear in the Settlement interface, Economy interface, Institutional Assets interface, and Military Logistics interface.

It must still be one warehouse, with one location, one inventory, and one ownership record.

#### 3. Desktop layout

The central map should be the primary visual component when Atlas View is selected.

Other workspaces can replace the map with relevant tables, organizational graphs, charts, or administrative records.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ IRGS │ Campaign / Scenario │ World Date │ Save │ Notifications │ Settings  │
├───────────────┬──────────────────────────────────────────┬──────────────────┤
│ WORLD MENU    │ ATLAS | ECONOMY | POLITICS | MILITARY     │ CONTEXT INSPECTOR│
│               │ SETTLEMENTS | INSTITUTIONS              │                  │
│ Overview      ├──────────────────────────────────────────┤ Selected Entity  │
│ Atlas         │                                          │                  │
│ Economy       │       MAIN WORKSPACE                     │ Identity         │
│ Politics      │                                          │ Current State    │
│ Military      │       Interactive map / dashboard       │ Known Information│
│ Settlements   │                                          │ Authority        │
│ Institutions  │       Contextual overlays / reports     │ Available Actions│
│ Projects      │                                          │                  │
│ Chronicle     │                                          │ Related Records  │
│               │                                          │                  │
│               ├──────────────────────────────────────────┤                  │
│               │ Filters / Time / Search / Map Layers     │                  │
├───────────────┴──────────────────────────────────────────┴──────────────────┤
│ Return to Story │ Action Composer │ Current Time │ Simulation Status       │
└─────────────────────────────────────────────────────────────────────────────┘
```

##### Proposed layout proportions

| Screen size      | Behaviour                                                                  |
| ---------------- | -------------------------------------------------------------------------- |
| Large desktop    | Left navigation, wide map/workspace, and right contextual inspector        |
| Standard desktop | Collapsible left navigation and resizable right inspector                  |
| Tablet           | Full-width workspace with expandable side drawers                          |
| Mobile           | One workspace at a time, with bottom navigation and full-screen inspectors |

I would preserve the same visual identity as the Gameplay Screen: dark blue-charcoal surfaces, neutral high-contrast text, restrained metallic accents, and campaign-specific visual themes.

The workspace should remain recognizable whether the player is looking at medieval Normandy, a modern city, or an interstellar civilization.

#### 4. Interface complexity and player authority

The interface needs an important distinction between what exists in the world, what the character knows, and what the player can command.

##### Example progression

| Character position   | Normal interface access                                                        |
| -------------------- | ------------------------------------------------------------------------------ |
| Traveller            | Known geography, destinations, observed settlements, public information        |
| Local resident       | Neighbourhood, known businesses, household information, community institutions |
| Merchant             | Trade routes, market information, warehouses, business assets, contracts       |
| Property owner       | Owned buildings, land, tenants, costs, maintenance, projects                   |
| Military captain     | Assigned troops, relevant orders, known enemy reports, supplies                |
| Municipal official   | Records and powers within their jurisdiction                                   |
| Noble administrator  | Estates, revenues, obligations, subordinate institutions                       |
| Sovereign ruler      | Authorized governmental, diplomatic, military, and economic administration     |
| Institutional player | Powers defined by the selected organization and its governance rules           |

These are examples, not fixed advancement tiers.

A ruler may possess broad legal authority but poor information about a remote province. A merchant may have more accurate local economic knowledge than the monarch. A general may command thousands of soldiers without owning any of their equipment.

The UI must respect those distinctions.

Inspection is not command. Authority is not competence. Knowledge is not omniscience.

#### 5. World Atlas — geographic simulation interface

The Atlas is not merely a decorative map. It is a navigable representation of the world's geography, infrastructure, settlements, territories, units, and accessible information.

Its underlying data must be maintained independently of the map renderer.

##### 5.1 Map scales

The interface should support the following geographic scales without introducing a new simulation each time the player zooms.

1. World / Continental

   Political geography, major transport networks, climate regions, continental trade, and large-scale relationships.
2. Kingdom / Nation

   Administrative territories, principal settlements, military deployments, economic regions, and major institutions.
3. Province / Region

   Towns, castles, estates, roads, resources, local governments, military formations, and regional commerce.
4. Settlement / City

   Districts, streets, important buildings, local markets, services, households, and infrastructure.
5. Estate / Property

   Fields, workshops, dwellings, warehouses, defensive works, and individual property assets.
6. Building / Local Area

   Rooms, workspaces, accessible objects, people, and physical surroundings where the game actually possesses that resolution of information.

These are navigation scales, not six mandatory map-generation requirements.

An IRGS implementation may possess accurate continental geography while having only descriptive information about individual buildings. Zooming must not automatically fabricate floor plans or exact building placements.

An appropriate genre can extend the geographic hierarchy—for instance, with planetary systems and orbital locations—without changing Core's ownership of location and movement.

##### 5.2 Geographic information layers

The Atlas should contain togglable layers. These are independent visual representations of the same data, not mutually exclusive maps.

| Layer               | What it displays                                                     |
| ------------------- | -------------------------------------------------------------------- |
| Physical geography  | Terrain, rivers, coastlines, mountains, forests, waterways           |
| Political geography | Jurisdictions, borders, recognized polities                          |
| Territorial control | Effective administration, occupation, contested locations            |
| Political claims    | Legal and dynastic claims, disputed sovereignty                      |
| Settlements         | Cities, towns, villages, estates, fortifications                     |
| Infrastructure      | Roads, bridges, canals, ports, warehouses, networks                  |
| Economy             | Production centres, known markets, trade and resource flows          |
| Military            | Known forces, garrisons, deployments, defensible positions           |
| Population          | Settlements and demographic information at an authorized level       |
| Environment         | Weather observations, environmental hazards, relevant conditions     |
| Projects            | Construction sites, research facilities, infrastructure developments |
| Personal            | Known locations, journeys, properties, contacts, bookmarked places   |

The Atlas needs to support overlapping jurisdiction and control.

In the Hundred Years' War, for example, royal claims to territory, actual administrative jurisdiction, local noble authority, and military occupation cannot be reduced to one universal owner field. The uploaded framework explicitly requires these distinctions.


##### 5.3 Distinguishing political boundaries

Political maps should avoid presenting every contested region as if it had a single undisputed sovereign.

A location might simultaneously possess:

- A sovereign claimant.
- A different effective administrator.
- A particular noble's property rights.
- A military garrison serving another authority.
- Local customary privileges.
- Unresolved jurisdictional disputes.

I recommend separate visual conventions for recognized borders, contested claims, occupied territories, and uncertain information.

These should also be configurable for accessibility so the distinctions are not communicated by colour alone.

##### 5.4 Map interaction rules

Selecting a location is an inspection action. It opens the relevant information panel.

A location inspector should offer:

Selected Location

Generic place inspector

Overview

Local Authority

Population

Infrastructure

Markets

Known Events

Further controls appear only if the character has the necessary information, physical access, or institutional authority.

The player might then choose to:

- Inspect available information about the location.
- Plan a journey or trade route.
- Review owned property there.
- Inspect an associated institution.
- Request military movement if properly authorized.
- Begin an applicable project or administrative action.

The last three may be state-changing actions and therefore require validation through Core.

##### 5.5 Travel and routing

Route planning should account for actual infrastructure and movement conditions, including roads, rivers, shipping, terrain, weather, vehicles, supplies, and relevant hazards.

The interface should distinguish:

- Proposed route.
- Feasible route.
- Estimated travel time.
- Actually authorized movement.
- Movement in progress.
- Completed travel.

Planning a journey must not teleport the character, commit resources, or automatically advance the clock.

Similarly, discovering a new road on the map does not mean the character knows of its existence.

##### 5.6 Map uncertainty and knowledge

The Atlas needs more than a simple explored/unexplored state.

A location may be:

| Information state | Presentation                                              |
| ----------------- | --------------------------------------------------------- |
| Directly observed | Information from the character's observations             |
| Reliably reported | Information received through a credible source            |
| Rumoured          | Unverified claims clearly marked as such                  |
| Outdated          | Last known information with an observation or report date |
| Disputed          | Conflicting available reports                             |
| Unknown           | No legitimate information available                       |

For military reports, an army last seen in Normandy several weeks ago must not be depicted as though its location is still confirmed.

The character may know the historical road network without knowing the present location of enemy forces.

The map renderer must never receive hidden data merely to obscure it visually afterward.

#### 6. Economy & Resource Management

This should be the second major workspace.

It needs to serve two very different users: someone managing their personal business and someone administering the economy of a substantial political territory.

Both operate through the same underlying mechanisms.

##### 6.1 Economic dashboard

I recommend six sections.

| Section           | Function                                                          |
| ----------------- | ----------------------------------------------------------------- |
| Resources & Stock | Actual goods, materials, equipment, food, currency, reserves      |
| Production        | Farms, workshops, mines, businesses, manufacturing                |
| Markets & Trade   | Prices, available supply, demand, commercial relationships        |
| Finance           | Income, expenditure, debts, taxes, wages, contractual payments    |
| Labour            | Workers, expertise, employment, availability, obligations         |
| Logistics         | Warehouses, transport, shipping, routes, deliveries, distribution |

A seventh optional section, Forecasts & Plans, should display projected economic developments separately from existing stocks.

##### 6.2 Different economic perspectives

Household Economy

Food, income, maintenance, personal and shared assets, dependants, household expenditure, and obligations.

Enterprise Economy

Inventory, suppliers, customers, labour, workshops, contracts, production capacity, costs, and earnings.

Settlement Economy

Local production, markets, employment, food supply, infrastructure, public revenue, and economic constraints.

Government Economy

Public revenue, treasury holdings, obligations, expenditures, jurisdiction, taxation, military funding, and institutional capacity.

Crucially, a government does not necessarily possess every resource within its borders.

The national economy is a view across households, businesses, institutions, and territories. It is not one enormous royal inventory.

##### 6.3 Resource presentation

A resource should have a single authoritative record or properly reconciled ledger source.

The interface may display aggregations, but those views must never duplicate assets.

For example:

| Record                  | Meaning                                               |
| ----------------------- | ----------------------------------------------------- |
| Current stock           | Goods physically available at a recorded location     |
| Reserved stock          | Goods committed but not necessarily consumed          |
| In transit              | Goods physically moving between locations             |
| Projected production    | Expected future output, not existing inventory        |
| Current demand          | Requirement for consumption or planned activity       |
| Contracted supply       | Promised delivery, not automatically received stock   |
| Maintenance requirement | Resources required to preserve an asset or capability |

The uploaded framework specifically prohibits confusing treasury stock with revenue, treating a reservation as consumption, or creating duplicate resources during simulation-scale changes.


##### 6.4 Economic planning interface

An authorized manager should be able to prepare an economic order, inspect consequences, and submit it for resolution.

For instance, an estate owner might seek to construct a new grain store.

The interface would:

1. Identify the proposed location.
2. Check applicable ownership and construction authority.
3. Retrieve available materials, workers, and technical requirements.
4. Present any feasible alternatives and uncertainties.
5. Show estimated cost and time, with their provenance.
6. Allow the player to authorize the project.
7. Commit reservations and subsequent expenditure through Core as work occurs.
8. Track construction and ongoing maintenance.

Selecting the proposed building in an editor must not itself construct it.

##### 6.5 Markets and price information

Prices should come from applicable economic rules and actual market circumstances.

The interface should distinguish the most recent observed or reported price from a live market quotation.

A medieval merchant may know yesterday's market price in their current town but have only a weeks-old report from a distant port.

The website should not turn local information into omniscient real-time commodity pricing.

##### 6.6 Economic visualization

Useful dashboard visuals include:

- Historical income and expenditure charts.
- Production trends.
- Resource supply and demand comparisons.
- Contract maturity calendars.
- Warehouse stock histories.
- Trade networks.
- Business profit and loss views.
- Settlement provisioning reports.

Every graph should offer access to its underlying records, units, relevant time interval, and information provenance.

No unexplained universal economic health statistic is necessary.

#### 7. Politics & Government

The political interface should support national government, regional administration, city government, noble jurisdictions, councils, diplomatic institutions, and organizations exercising recognized political authority.

It should not assume every historical society uses a modern centralized state.

##### 7.1 Political dashboard

##### Political & Government Workspace

Rulers & Offices

Holders of political authority

Law & Jurisdiction

Legal powers and obligations

Diplomacy

Relations and agreements

Territorial Claims

Sovereignty and control

Political Networks

Parties, nobles, courts and interests

Government Actions

Pending decisions and projects

##### 7.2 Political authority

The website must distinguish a political office from the person occupying it.

For example, a kingdom may have a monarch, a regent, a council, and regional officers exercising different powers.

Being the sovereign does not imply that every subordinate organization always complies, or that every decree is instantly implemented throughout the kingdom.

The interface should display:

| Field             | Function                                                         |
| ----------------- | ---------------------------------------------------------------- |
| Recognized office | The office or role being exercised                               |
| Officeholder      | The individual or institution presently occupying it             |
| Jurisdiction      | Where and over what the authority applies                        |
| Powers            | Decisions and orders legally or institutionally permitted        |
| Obligations       | Duties, restrictions, agreements, and accountability             |
| Delegation        | Powers transferred to subordinate actors or offices              |
| Effective control | Whether commands can actually be carried out                     |
| Disputes          | Competing claims, contested authority, refusal, or noncompliance |

##### 7.3 Diplomacy and political relationships

The diplomatic workspace should show relationships among existing political actors.

Possible relationship categories include alliances, treaties, truces, wars, trade arrangements, tributary relationships, vassalage, recognition, rival claims, and other setting-specific agreements.

These are not automatically mutually exclusive.

Two kingdoms might be nominally at peace while their subjects, private companies, or regional allies continue fighting elsewhere.

A military alliance does not automatically transfer all allied forces into one command hierarchy.

A treaty may obligate a government to provide aid, but the aid still requires actual political authorization, personnel, supplies, transport, and execution.

##### 7.4 Diplomatic action process

An authorized player could submit a proposed treaty or diplomatic message through a structured editor or natural-language declaration.

For example:

Proposed Diplomatic Action

Negotiate a temporary truce with a neighbouring government.

- Identify participants and authorized representatives
- Specify proposed terms and duration
- Determine whether communication is feasible
- Transmit the proposal through actual channels
- Await the other party's autonomous consideration
- Establish an agreement only if legitimate acceptance occurs

Opening a diplomatic interface does not guarantee the target government will negotiate.

Sending a proposal does not create a treaty.

The agreement becomes authoritative only when its necessary procedures and conditions have been fulfilled.

##### 7.5 Political networks

I recommend an interactive network diagram showing the relationships among rulers, dynasties, institutions, households, and political interests.

This would be particularly useful during the Hundred Years' War, including the Armagnac–Burgundian dispute and the rival French governmental networks in 1422.

The uploaded campaign framework requires the Lancastrian and Valois administrations to remain distinct, even when they assert claims to the same French crown.


The interface should therefore allow multiple claims to the same title or territory without duplicating the physical assets being contested.

#### 8. Military & Command

The military interface should integrate with the shared Core military organization, personnel, equipment, logistics, time, and resource systems.

It should not be a separate wargame running an independent army simulation.

##### 8.1 Command dashboard

##### Military Command

Proposed interface

Selected Military Formation

Formation identity · Commanding officer · Current assignment

Personnel

Equipment

Readiness

Logistics

Orders

Reports

##### 8.2 Military organization hierarchy

The website should represent military organizations in a navigable command tree.

For a medieval setting, this may involve royal commands, noble retinues, contracted companies, garrisons, commanders, and smaller military groups.

Modern and science-fiction settings can provide their own organizational structures.

The UI must not assume every military force follows one universal regiment–battalion–company hierarchy.

##### 8.3 Personnel and strength

The interface must distinguish:

| Measure             | Meaning                                                                             |
| ------------------- | ----------------------------------------------------------------------------------- |
| Authorized strength | Personnel the institution is permitted or expected to maintain                      |
| Assigned personnel  | People recorded as members of the formation                                         |
| Present personnel   | People physically present                                                           |
| Available personnel | Those currently capable of the relevant assignment                                  |
| Casualties          | Actual injuries, deaths, disappearances, or other losses according to event records |
| Reinforcements      | Personnel ordered, allocated, or physically arriving                                |
| Contracted strength | Forces promised under an agreement, not necessarily available on site               |

If one company is subordinate to an army, its personnel cannot be counted again as an independent additional force in the army-wide total.

The uploaded campaign specification explicitly distinguishes actual military capacity from nominal strengths, readiness, financing, and logistical reach.


##### 8.4 Orders and operations

The player should be able to inspect assigned forces, give authorized orders, and review operational consequences.

An order interface could support:

- Marching or repositioning a formation.
- Guarding a location.
- Escorting a convoy.
- Establishing a camp.
- Preparing a siege.
- Organizing reconnaissance.
- Arranging supply movements.
- Maintaining or repairing equipment.
- Recruiting additional personnel.
- Negotiating contracts for military service.

Each operation depends on the appropriate mechanisms.

A commander cannot order troops that do not belong to their command unless they possess some other legitimate authority.

An army cannot march without available personnel and feasible movement conditions.

Recruitment does not create soldiers instantly without candidates, recruitment procedures, and applicable resources.

##### 8.5 Military operations map

The Atlas should support a Military Overlay displaying known formations and their reported positions.

For authorized commanders, an operation-planning panel could display:

| Planning area   | Information                                                   |
| --------------- | ------------------------------------------------------------- |
| Objective       | Intended mission or destination                               |
| Assigned forces | Actual available formations                                   |
| Command         | Relevant chain of command and delegated powers                |
| Route           | Terrain, roads, rivers, ports, movement constraints           |
| Supply          | Food, fodder, equipment, transport, ammunition                |
| Intelligence    | Known and uncertain hostile activity                          |
| Timing          | Estimated preparation, movement, and operational intervals    |
| Orders          | Issued, received, accepted, executing, interrupted, completed |

The distinction between issuing an order and the recipient receiving it is especially important.

Orders travel through the world's communication systems. A messenger can be delayed. An officer may misunderstand, be unable to comply, or act autonomously within their authority.

The command interface should show the order's actual transmission and execution state.

##### 8.6 Combat and battles

I recommend separating two interface presentations.

Personal Encounter View supports an individual fighter's immediate perceptions and actions.

Military Operations View supports the broader command perspective, including unit disposition, orders, terrain, formation condition, and logistical status.

Both must use the same combat events and casualty records.

The player cannot switch to a strategic map and thereby gain knowledge of undiscovered enemy deployments or automatically assume control of all allied troops.

##### 8.7 Mercenary companies and contracted forces

The Military View must support independent companies, mercenary employment, and units serving under temporary contracts.

A company should retain its identity, assets, commanders, personnel, and obligations when its contract expires.

A company hired by England does not necessarily become permanently owned by the English crown.

The contract establishes its actual service relationship, compensation, authority, and obligations.

The 1360 and 1444 Hundred Years' War starts particularly benefit from these capabilities because demobilization and independent military careers remain relevant outside periods of active royal warfare.


#### 9. Cities, Towns & Settlements

This workspace should support everything from a small village to a major metropolitan area.

Its purpose is to show how a settlement actually functions, not merely how many buildings are present on its map.

##### 9.1 Settlement overview

##### Settlement Management

Population & Households

Buildings & Property

Food & Resources

Economic Activity

Transport & Infrastructure

Health & Conditions

Administration

Development Projects

##### 9.2 Population and households

Settlement population must be derived from actual population records, households, and the Core's valid aggregation mechanisms.

Important distinctions include:

- Permanent residents.
- Temporary occupants and visitors.
- Military garrisons.
- Displaced or migrating populations.
- Households and dependants.
- Available workforce.
- People already employed or otherwise committed.
- Population changes due to births, deaths, migration, and actual events.

A settlement cannot gain inhabitants merely because the map displays a new residential district.

Equally, its population should not reset when the player switches from a detailed settlement view to a national overview.

##### 9.3 Buildings and infrastructure

Buildings must exist as physical assets, with relevant attributes such as location, purpose, condition, ownership, operational capacity, and maintenance requirements.

Examples include housing, warehouses, roads, walls, workshops, markets, ports, public buildings, and agricultural structures.

Building ownership is different from building use.

A royal authority might exercise administrative power over a town while privately owned workshops and homes remain the property of their actual owners.

The interface should support linked property records and maintenance histories.

##### 9.4 Settlement services

The availability of services should depend on relevant institutions, infrastructure, qualified personnel, and resources.

Possible services include water distribution, waste handling, markets, transport, security, healthcare, education, and government administration.

Not every settlement requires the same systems.

For example, a medieval town's sanitation arrangements should not be rendered as though it possesses a modern municipal wastewater network.

##### 9.5 City planning and construction

I recommend a Settlement Development Editor.

##### Settlement Development Workflow

1. Inspect existing geography, land use, and property boundaries.
2. Identify an eligible location for the proposed development.
3. Select a building, improvement, repair, or infrastructure project.
4. Review ownership, legal authority, engineering feasibility, materials, labour, and costs.
5. Submit an authorized proposal or construction order.
6. Monitor actual work, resource expenditure, delays, maintenance, and completion.

A player who governs a town may still need to acquire private property, negotiate permissions, obtain resources, or follow institutional procedures.

Drawing a road on the map does not automatically create a road. It creates a proposed plan that Core must evaluate.

##### 9.6 Settlement autonomy

A settlement is not necessarily a single actor with unrestricted control over all residents.

Different households, companies, government offices, institutions, and individuals pursue their own activities.

A town may grow through migration and trade even when the player is elsewhere.

It may also decline if actual economic or environmental circumstances support that outcome.

The UI should show changes resulting from the autonomous simulation without making the settlement depend on constant player micromanagement.

#### 10. Institutions & Organizations

I would give institutions their own substantial interface rather than hiding them inside politics or economics.

Institutions connect nearly every part of IRGS.

A government is an institution. A guild, military company, school, workshop, religious organization, corporation, or household may also possess institutional structures.

##### 10.1 Institution profile

##### Institution Inspector

| Identity   | Name, type, origin, history                            |
| ---------- | ------------------------------------------------------ |
| Governance | Leadership, offices, procedures, authority             |
| People     | Members, employees, representatives, contractors       |
| Assets     | Owned and controlled property, equipment, resources    |
| Finances   | Income, costs, debts, obligations                      |
| Operations | Current activities, contracts, projects                |
| Relations  | Other institutions, clients, patrons, rivals           |
| History    | Founding, changes, leadership succession, major events |

##### 10.2 Institutional governance

Institutions may use different decision procedures.

A monarchy, guild council, merchant partnership, mercenary company, municipal government, and university do not necessarily assign authority in the same manner.

Core should provide reusable governance and authority interfaces, while the institution's configuration defines the applicable roles and procedures.

The player-facing UI should adapt accordingly.

A sole proprietor might authorize a purchase directly, while a member of a council may need to submit a motion and obtain approval.

##### 10.3 Organizational charts

I recommend an expandable organizational network that displays:

- Leaders and officeholders.
- Subordinate departments.
- Membership and employees.
- Assigned responsibilities.
- Reporting relationships.
- Delegated authority.
- Current vacancies.
- Contracted external services.
- Institutional partnerships.

These relationships must be temporally indexed.

A retired commander should appear in the institution's history without continuing to occupy the active command position.

##### 10.4 Cross-institutional relationships

An individual may belong to several institutions.

For example, a scholar might be employed by a university, receive funding from a noble patron, and hold a research contract with a government.

The interface must display each arrangement separately.

An institution may also contract services from another organization, including a mercenary company or transport business.

These relationships do not automatically transfer ownership or independent agency.

##### 10.5 Institutional formation and dissolution

Players may be able to found organizations when they possess the necessary resources, authority, personnel, and circumstances.

The interface should support formation, recruitment, governance, financing, operation, reorganization, mergers, divisions, succession, and dissolution.

However, changing an institution's name, ownership, or leadership must not inadvertently erase its contractual history, staff, or existing assets.

An institution can also survive its founder and continue operating for generations.

#### 11. Civilization Management & Grand Strategy

The Civilization interface is not a separate seventh simulation. It is a higher-level workspace combining politics, economy, settlement administration, military capability, institutions, population, and long-term development.

It should become available when the player's knowledge and control perspective justify it.

A civilization or government does not need to own every person or enterprise it encompasses to present useful aggregate information.

##### 11.1 Civilization dashboard

I recommend a strategic overview containing:

| Area               | Information                                                                |
| ------------------ | -------------------------------------------------------------------------- |
| Territory          | Jurisdiction, effective control, claims, administrative regions            |
| Population         | Demographics, households, migration, workforce                             |
| Economy            | Production, commerce, revenue, costs, available assets                     |
| Government         | Institutions, offices, delegated authorities, legal obligations            |
| Military           | Actual forces, readiness, finances, logistics, operational commitments     |
| Infrastructure     | Roads, ports, settlements, fortifications, public works                    |
| Technology         | Known capabilities, research, available specialists, manufacturing         |
| Diplomacy          | Foreign relationships, treaties, disputes, obligations                     |
| Society            | Households, social institutions, demographic and generational developments |
| Strategic Projects | Current reforms, construction, research, settlement expansion              |

This dashboard should support drill-down navigation from a kingdom into its provinces, settlements, institutions, and individual assets.

##### 11.2 Civilization development

A ruler or suitably authorized institution may initiate broad reforms.

For example, a government might attempt to establish a more professional standing army.

That undertaking should involve real institutions, recruitment, funding, equipment, training, administration, and ongoing maintenance.

The player should not receive an instant abstract military-strength increase because they clicked a reform button.

The same applies to taxation changes, public infrastructure, educational expansion, trade policy, and technological development.

Reforms are projects and institutional actions with consequences, not purchased bonuses.

##### 11.3 Delegation and autonomy

A large civilization must be manageable without requiring the player to issue instructions to every household, workshop, or officer.

The interface should allow authorized delegation.

A ruler could appoint an official to oversee provincial tax collection. That official would operate under an actual mandate, with relevant resources, competence, obligations, and institutional procedures.

The player could receive periodic reports, intervene when necessary, or amend the mandate.

Delegation does not guarantee perfect execution, eliminate operating costs, or grant the official abilities they do not possess.

##### 11.4 Civilizations can succeed peacefully

The interface should recognize prosperity, stable government, family life, education, sustained peace, and economic recovery as meaningful outcomes.

A kingdom that becomes peaceful and prosperous should not automatically encounter stronger enemies simply to maintain game difficulty.

The simulation should produce subsequent challenges from actual conditions and autonomous actors.

#### 12. Historical Timeline & Divergent World Development

This interface must follow the current v0.4 Hundred Years' War design rather than the earlier, simpler historical-sandbox proposal.

The uploaded specification distinguishes an immutable historical baseline from a living campaign timeline. Future historical events are conditional plans: they are intended to follow documented history while the relevant causal conditions remain intact, but they cannot overwrite the simulation or force impossible outcomes.


That distinction has major interface implications.

##### 12.1 Three temporal perspectives

| Perspective           | Purpose                                                        | Who can see it?                               |
| --------------------- | -------------------------------------------------------------- | --------------------------------------------- |
| Historical baseline   | Source-backed history and conditional future event plans       | Creators and authorized historical inspectors |
| Living campaign state | Events and circumstances actually produced by the simulation   | Filtered according to player permissions      |
| Character knowledge   | What the player character has legitimately observed or learned | Normal character-level player interface       |

The player-facing Atlas must not expose future historical event plans merely because the website has loaded them.

A player in 1415 should not see a guaranteed marker for Agincourt on 25 October unless their character has legitimately learned relevant plans or circumstances.

##### 12.2 Historical comparison

A separate creator/debugging tool could compare the world with recorded history.

##### Historical Comparison Inspector

Creator/debugger only — not automatically available to player characters.

Historical Baseline

Documented starting conditions, event plans, expected historical relationships, provenance

Living World

Actual state, outcomes, changes, independent actors, unresolved events

Divergence Categories

Occurred

Altered

Rescheduled

Prevented

Superseded

Unresolved

The detailed event-plan status model in the uploaded specification should be reused; the simplified labels above are only presentation groupings.


##### 12.3 Historical events cannot dictate physical outcomes

If an army has been destroyed, it cannot reappear on the map because a scheduled battle requires it.

If a ruler dies early, later historical plans requiring that ruler must be reevaluated.

If a treaty is negotiated decades early, a later treaty may become unnecessary.

Conversely, events unrelated to the divergence should not be automatically invalidated.

The historical comparison interface should trace relevant causal dependencies instead of using a global divergence meter.

##### 12.4 Long-term world evolution

The Atlas and Civilization panels must continue operating after the original historical period concludes.

A campaign beginning in 1337 might continue for centuries.

Its political borders, institutions, technologies, economies, cities, and military structures would be derived from its actual history.

When the player's world no longer resembles fifteenth-century Europe, the interface should reflect those changes without resetting to another historical snapshot.

This means the interface needs flexible categories and data-driven components rather than permanent medieval assumptions.

#### 13. Time Advancement & Autonomous World Activity

The World interface should share the same authoritative world clock as the Story View.

Changing tabs, inspecting an army, viewing an economy, or scrolling a map must not advance time.

Actual time progression occurs through Core-authorized activities, waiting, and time advancement.

##### 13.1 Time scales

The simulation should accommodate:

- Immediate actions and conversations.
- Hours and days of local activity.
- Weeks of travel or construction.
- Months of trade, training, and military operations.
- Years of settlement or institutional development.
- Decades of generational progression.
- Centuries of civilization evolution.

Time acceleration must not bypass resource consumption, scheduled events, autonomous behaviour, or required player decisions.

##### 13.2 Period reports

After longer periods of simulated activity, the World interface should provide a concise report of consequential developments.

An authorized ruler might receive a government report covering treasury changes, construction progress, institutional appointments, wars, and outstanding decisions.

A civilian might instead receive information concerning personal finances, household circumstances, employment, known local events, and correspondence.

The player should not receive information that could not legitimately reach their perspective.

##### 13.3 Historical memory

The World interface should link to the established IRGS memory consolidation structure:

Persistent Historical Summaries

1-Year Records × 5       → 5-Year Summary 5-Year Summaries × 5     → 25-Year Summary 25-Year Summaries × 4    → 100-Year Summary  100 → 200 → 300 → 400 cumulative years 500 completed years      → Sealed Historical Epoch  Next 500 years           → New Epoch

The word budget grows as each cumulative century expands.

Historical narrative consolidation is separate from current world state and retrievable event records.

A business founded 150 years earlier must remain an actual operating institution if the simulation says it still exists.

#### 14. Cross-Workspace Interactions

One of the biggest advantages of having a shared World interface is that changes made through one domain appear in all others.

Consider an authorized project to build a new bridge.

1. Atlas

   The proposed route and bridge location are visible during planning.
2. Politics

   Ownership, jurisdiction, approvals, and land-use authority are evaluated.
3. Economy

   Materials, labour, financing, transport, and ongoing costs are established.
4. Institutions

   Contractors, responsible authorities, and project managers receive their actual assignments.
5. Settlement Management

   Construction progresses and eventually alters local infrastructure.
6. Military

   Once the bridge is usable, it may affect feasible routes and transport capacity.
7. Chronicle

   The event and its consequences become part of historical records.

There must not be seven separate bridge records created independently by seven subsystems.

Instead, the World interface should show multiple views and relationships associated with the same authoritative asset and its history.

#### 15. Actions versus inspections

This distinction must be consistent across every World workspace.

| User interaction              | World-state mutation?                                     |
| ----------------------------- | --------------------------------------------------------- |
| Open a map                    | No                                                        |
| Select a settlement           | No                                                        |
| Inspect an army               | No                                                        |
| Search historical records     | No                                                        |
| Compare economic reports      | No                                                        |
| Draft a construction proposal | No, until explicitly committed                            |
| Issue a military order        | Potentially, after authorized processing                  |
| Sign a contract               | Yes, when properly executed                               |
| Move owned goods              | Yes, through actual transfer or transport                 |
| Authorize expenditure         | Yes, through the applicable accounting procedure          |
| Submit a diplomatic offer     | Yes, as a communication/action; not as an accepted treaty |
| Begin a research project      | Yes, when authorized and feasible                         |

The interface should provide explicit feedback distinguishing a drafted action, an authorized order, a pending activity, and a completed effect.

A successful submission does not necessarily mean the requested physical result has already occurred.

#### 16. Notifications, Reports & Information Provenance

A civilization-scale simulation will generate large amounts of information.

Not all of it should appear in the narrative feed.

I recommend a unified notification and reporting system.

##### Notification categories

| Category      | Examples                                                         |
| ------------- | ---------------------------------------------------------------- |
| Personal      | Injuries, appointments, relationship developments                |
| Institutional | Received orders, contracts, appointments, internal decisions     |
| Economic      | Delivered goods, outstanding payments, production interruptions  |
| Military      | Reports, engagements, casualties, supply problems                |
| Political     | Treaties, diplomatic messages, legal decisions                   |
| Settlement    | Infrastructure completion, local emergencies, population changes |
| Research      | Experiments completed, new discoveries, project delays           |
| Historical    | Relevant changes in the accessible Chronicle                     |

Notifications should identify their basis and, where relevant, the time the underlying event occurred and when the report reached the character.

##### Alerts versus reports

An alert should require attention or indicate something consequential.

Routine activity can be summarized in periodic reports.

For instance, an estate administrator should not necessarily receive a separate popup for every item produced by every workshop.

The system should allow the player to choose presentation detail and notification preferences.

These settings affect what is emphasized, not what actually occurs in the world.

#### 17. Mobile World Interface

The mobile experience should not attempt to squeeze the complete desktop map and administrative dashboards onto a narrow screen.

I recommend three mobile components.

Primary Workspace: The selected map, chart, ledger, organization graph, or other content fills the available space.

Context Drawer: Selecting an entity opens its information as a bottom sheet or full-screen inspector.

Persistent Navigation: The player can move between Story, World, Chronicle, and essential character records without losing their position.

```
┌────────────────────────────┐
│ ←  WORLD              ⋮    │
│ Current Date / Save Status │
├────────────────────────────┤
│ Atlas  Economy  Politics   │
│ Military  Cities  More     │
├────────────────────────────┤
│                            │
│                            │
│      PRIMARY WORKSPACE     │
│                            │
│       Map / Dashboard      │
│                            │
│                            │
├────────────────────────────┤
│ Selected Entity            │
│ Inspect details       ↑    │
├────────────────────────────┤
│ Story   World   Chronicle  │
└────────────────────────────┘
```

Map gestures, panel navigation, search, and filters should be touch-friendly and keyboard-accessible.

Charts, military hierarchies, genealogical trees, and institutional networks need accessible textual alternatives.

#### 18. Implementation Architecture

The frontend should be divided into reusable presentation components rather than separate implementations for every campaign.

```
WorldWorkspace
├── WorldHeader
│   ├── CampaignIdentity
│   ├── WorldClock
│   ├── SaveStatus
│   └── NotificationCentre
│
├── WorldNavigation
│
├── WorldAtlas
│   ├── MapRenderer
│   ├── MapLayerControls
│   ├── GeographicScaleControls
│   ├── LocationSearch
│   ├── RoutePlanner
│   └── LocationInspector
│
├── EconomyWorkspace
│   ├── ResourceLedgers
│   ├── ProductionDashboard
│   ├── MarketInspector
│   ├── FinancialReports
│   ├── LabourOverview
│   └── LogisticsDashboard
│
├── PoliticsWorkspace
│   ├── PoliticalEntityInspector
│   ├── GovernanceChart
│   ├── JurisdictionMap
│   ├── DiplomaticRelations
│   └── PoliticalActionEditor
│
├── MilitaryWorkspace
│   ├── CommandHierarchy
│   ├── FormationInspector
│   ├── OperationsMap
│   ├── OrdersInterface
│   ├── PersonnelReports
│   └── MilitaryLogistics
│
├── SettlementWorkspace
│   ├── SettlementOverview
│   ├── PopulationDashboard
│   ├── BuildingInspector
│   ├── InfrastructureManager
│   └── DevelopmentPlanner
│
├── InstitutionWorkspace
│   ├── InstitutionProfile
│   ├── OrganizationalChart
│   ├── MembershipManager
│   ├── ContractInspector
│   ├── AssetDashboard
│   └── InstitutionalHistory
│
├── CivilizationOverview
├── HistoricalComparisonInspector
├── WorldContextInspector
├── ActionComposer
└── ResponsiveNavigation
```

These are proposed component boundaries, not final code modules.

##### Backend-facing logical interfaces

| Proposed interface         | Responsibility                                              |
| -------------------------- | ----------------------------------------------------------- |
| `GetWorldProjection`       | Retrieve a permission-filtered world view                   |
| `GetGeography`             | Retrieve appropriate map and geographic records             |
| `GetEntityDetails`         | Inspect accessible information about one entity             |
| `GetEconomicProjection`    | Retrieve financial, production, and resource views          |
| `GetPoliticalProjection`   | Retrieve accessible authorities, claims, relations          |
| `GetMilitaryProjection`    | Retrieve known forces, commands, logistics                  |
| `GetSettlementProjection`  | Retrieve settlement and infrastructure information          |
| `GetInstitutionProjection` | Retrieve organization, membership, authority, asset records |
| `GetHistoricalProjection`  | Retrieve accessible historical data as of a specified date  |
| `SubmitWorldAction`        | Submit authorized state-changing declarations to Core       |
| `GetActionResolution`      | Retrieve committed action results by request identifier     |

Each response should identify its playthrough and state version, the information perspective used, and relevant data timestamps.

The website must not mutate authoritative state directly.

##### Separation of information and execution

The frontend should receive a filtered projection for display and route authorized declarations to IRGS Core.

A projected resource total or institutional dashboard is not an independent ledger.

Creator-level historical comparison and full simulation inspection must be protected by separate authorization rules.

#### 19. Testing and Acceptance Criteria

The following are proposed implementation tests, not completed tests.

| Test                                                  | Expected result                                                                          |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Civilian opens World View                             | Accessible geographic and public information appears; no inappropriate command authority |
| Player changes map scale                              | No resources, clock time, populations, or army totals change                             |
| Player opens a province                               | Its settlements and institutions link to the same underlying records                     |
| Royal claimant inspects disputed territory            | Legal claim and effective control remain distinct                                        |
| King selects privately owned workshop                 | No automatic royal ownership is granted                                                  |
| Merchant reviews distant market                       | Reports include their actual information dates                                           |
| Player inspects an army                               | No unauthorized movement or orders occur                                                 |
| Commander issues a march order                        | Authority, route, capability, resources, and communication are evaluated                 |
| Same army appears in region and nation reports        | Personnel are counted once                                                               |
| Mercenary contract expires                            | Soldiers and company remain present                                                      |
| City begins bridge construction                       | Costs, labour, physical work, and progress are recorded                                  |
| Player zooms into an unmodeled building               | No invented floor plan becomes authoritative                                             |
| Two institutions share a project                      | Costs and resources are not duplicated                                                   |
| Political treaty is proposed                          | The other party must legitimately accept                                                 |
| War ends                                              | Economic and institutional simulation continues                                          |
| Town grows over ten years                             | Changes reflect actual demographic and economic processes                                |
| Historical 1415 world is inspected                    | Valid historical starting conditions are loaded                                          |
| Divergent 1415 world is inspected                     | Actual campaign state overrides the historical baseline                                  |
| Historical comparison is opened as ordinary character | Secret future event plans are not exposed                                                |
| Game advances 100 years                               | No duplication or reset of world resources or historical state                           |
| Player loads an old save                              | Relevant ownership, locations, institutions, and history remain consistent               |

##### Critical regression tests

In addition to those user-interface cases, the implementation must verify that:

- Time-scale changes do not replenish resources.
- Aggregate population reports do not invent inhabitants.
- Military strength is not double-counted.
- Ownership does not automatically follow occupation.
- Resource movement creates no duplicate stock.
- Scheduled historical events do not create missing actors or equipment.
- Autonomous NPCs and institutions remain active.
- Infeasible actions are not made possible through arbitrary rolls.
- Failure does not cause unrelated catastrophic consequences.
- A player's success is not undone to preserve historical difficulty.
- Player-character agency is never assumed by the AI.

#### 20. Development priorities

Recommended implementation sequence

1. P0 — World Viewer Foundation

   Main workspace, map/navigation, accessible entity inspection, stable identifiers, permissions, world-state versioning, and links to Story and Chronicle.
2. P1 — Core Civilian World Systems

   Settlements, ownership, institutions, resource ledgers, markets, household/business economic views, and basic projects.
3. P2 — Political and Military Administration

   Authority-aware political dashboards, command hierarchies, military logistics, diplomacy, and authorized action submission.
4. P3 — Civilization Management

   Cross-domain administrative overviews, development planning, delegation interfaces, institutional governance, and expanded long-range reporting.
5. P4 — Advanced Visualization

   Detailed geographic and settlement maps, organizational networks, rich historical comparison tools, advanced economic charts, and additional genre-specific overlays.

The phases describe frontend delivery priorities. Foundational simulation mechanics, persistence, information security, and resource accounting cannot be deferred until the corresponding advanced UI is implemented.

#### 21. CMRR integration with the current Hundred Years' War specification

The uploaded v0.4 campaign document already defines the fundamental world domains. This World & Civilization Interface should provide visual access to those systems rather than redefining them.

| Existing source requirement         | Design treatment                                                               | Owner                                      |
| ----------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------ |
| Historical geography                | Interactive Atlas and dated map projections                                    | Historical content + Core location systems |
| Territorial sovereignty and control | Separate political map layers                                                  | Core authority and territory records       |
| Military organizations              | Command and logistics dashboards                                               | Core military organization                 |
| National strength                   | Derived multidimensional overview                                              | Aggregated Core state                      |
| Historical event plans              | Creator-only timeline comparison and debugging                                 | Historical foundation + event interfaces   |
| Economic accounting                 | Resource, production, trade, and financial reports                             | Core economy/resources                     |
| Institutions and contracts          | Institutional and contract inspectors                                          | Core organization/obligation systems       |
| Autonomous societies                | Reports and state changes from autonomous actors                               | Core actor autonomy                        |
| Historical technology               | Research and technology information panels                                     | Core projects + genre content              |
| Generational persistence            | Settlements, families, organizations, and historical records remain accessible | Core continuity                            |
| No mandatory war participation      | Civilian, economic, scientific, and political workspaces remain playable       | Campaign Profile                           |
| Indefinite playthroughs             | Interface accommodates future political and technological evolution            | Core continuity + adaptive UI              |

##### What must not happen

Codex must not create an independent website version of any Core-owned simulation mechanism simply because its existing UI is incomplete.

It must also not use the historical setting's particular military, political, or economic structures as universal assumptions for every IRGS campaign.

For example, feudal vassalage is a historically appropriate institutional relationship, not a mandatory governance model for science-fiction civilizations.

Likewise, the Hundred Years' War's historical countries, towns, rulers, equipment, military organizations, and technological conditions belong to the corresponding campaign content and state, not the universal Core.

##### Status

- Established: Shared simulation authority, persistent institutions, independent actors, true resource accounting, unrestricted nonmandatory faction service, causal historical progression, and indefinite world continuity.
- Proposed: The six-workspace interface, visual layouts, map controls, economic dashboards, political and military inspectors, civilization overview, and component/API structure.
- Requires verification: Existing Core 3.3 Live capabilities, current website component structure, map/geography storage, historical data completeness, performance, and exact implementation interfaces.
- Not yet validated: Cross-scale visualization, complete world-state reconciliation, UI usability, quantitative simulation performance, and live gameplay integration.

No campaign migration or Core rule replacement is authorized by this interface proposal.

#### Final design direction

The World & Civilization Interface should make IRGS feel like a genuinely simulated world, even when the player is participating in only a small part of it.

A Scottish mercenary in the Hundred Years' War could inspect known towns, seek military contracts, manage personal finances, and examine their company's resources.

A merchant could operate businesses across borders while governments wage war independently.

A scholar could study technologies, establish a workshop, obtain patronage, and eventually influence industrial development.

A noble might manage estates, military obligations, political relationships, and dependent settlements.

A ruler could oversee a government while remaining constrained by actual institutional authority, logistical limits, incomplete information, and autonomous subjects.

All five characters inhabit the same kind of simulated world. Their interfaces differ because their knowledge, authority, resources, and responsibilities differ—not because they are playing different mechanical games.

My recommended next step is to refine the World Atlas and geographical simulation interface first, followed by the Settlement and Institution workspaces. Those establish the locations, assets, actors, and organizational relationships that the Economy, Politics, Military, and Civilization views all need to display.


---


# SOURCE VOLUME D — Cross-Campaign Currency Exchange & Universal Solo Progression

**Original attachment:** `writing-block (4).md`  
**Source status:** Included for provenance and complete implementation detail; apply integrated precedence/reconciliation.

---

# IRGS — Codex Instructions: Cross-Campaign Currency Exchange

**Feature:** Cross-Campaign Currency Exchange & Universal Solo Progression  
**Status:** Planned / Deferred — Not Yet Designed or Calibrated  
**Scope:** Solo-Play Only  
**Primary Ownership:** IRGS Platform / Account Services  
**Integration:** IRGS Core Economy, Character Progression, Inventory, and Campaign Persistence

---

## 1. Feature Objective

IRGS is intended to support a universal points system through which players can transfer economic value between their independently simulated solo campaigns.

A player who has accumulated substantial wealth in one campaign may convert an eligible amount of that campaign's in-game currency into universal IRGS points.

Those points may subsequently be redeemed in another eligible solo campaign to obtain:

1. **Local campaign currency** — Money or another eligible monetary resource used within the destination campaign.
2. **Character progression points** — Points applicable to the destination campaign's established character advancement mechanics.
3. **Campaign-specific equipment** — Eligible weapons, armour, tools, vehicles, or other items appropriate to the destination campaign.

This system is intended to provide cross-campaign progression and an optional means of assisting a player who is struggling in one campaign while succeeding in another.

It must not require every campaign to share the same currencies, economies, technology, or progression rules.

## 2. Solo-Play Restriction

**This feature is exclusively intended for solo-play campaigns.**

Cross-campaign currency conversion and universal-point redemptions must not be available within multiplayer campaigns.

Solo-earned universal points must not be transferable into multiplayer economies, multiplayer equipment inventories, or competitive multiplayer progression.

Where campaign branches or imported saves could cross the solo/multiplayer boundary, the implementation must prevent currency, equipment, and stat improvements obtained through this feature from entering multiplayer progression.

The exact entitlement and eligibility rules require later design.

## 3. Intended Player Workflow

The future player experience should follow this general sequence.

### Step A — Accumulate Currency

The player earns or legitimately acquires currency through ordinary gameplay within an eligible solo campaign.

The campaign's economy remains governed by IRGS Core.

### Step B — Convert to Universal Points

The player accesses a future currency-exchange interface.

They select the source campaign, eligible currency, and amount to convert.

The system presents the applicable exchange rate and resulting universal-point value.

Upon confirmation, the source campaign's currency balance is reduced and the corresponding universal points are credited to the player's account.

Both changes must be recorded reliably.

### Step C — Maintain an Account-Level Balance

The player's universal points exist independently of any single campaign.

The balance is associated with their platform account, not an individual character's inventory or a fictional institution's treasury.

Points remain available for redemption in other eligible solo campaigns.

### Step D — Redeem in Another Campaign

The player selects an eligible destination campaign and a permitted reward.

Potential redemptions include:

- An amount of the destination campaign's currency.
- An allocation of character progression points.
- A permitted piece of campaign-specific equipment.

The universal points are deducted from the account balance.

The purchased benefit is introduced into the destination campaign through an explicitly recorded, authorized external grant.

### Step E — Resume Gameplay

The player resumes their destination campaign with the purchased benefit reflected in its authoritative state.

Subsequent ownership, expenditure, use, deterioration, loss, and other consequences follow the destination campaign's ordinary simulation rules.

---

## 4. Architectural Requirements

The future exchange system must be implemented as a **platform-level progression service**, with controlled interfaces to individual IRGS campaigns.

It must not become an alternative economic simulation inside IRGS Core.

### Platform Responsibilities

The platform should eventually own:

- Universal-point account balances.
- Conversion eligibility.
- Exchange-rate configuration.
- Transaction records.
- Point redemption.
- Cross-campaign transaction validation.
- Solo-play access restrictions.
- Account-level transaction history.
- Fraud, duplication, and save-manipulation safeguards.

### IRGS Core Responsibilities

Core continues owning:

- Campaign currency and economic state.
- Character attributes and advancement.
- Equipment, inventories, and ownership.
- Persistent campaign state.
- Resource accounting.
- Character and institutional records.
- Simulation continuity.

The platform may request authorized grants and deductions, but Core must remain the authoritative owner of the resulting campaign state.

**Do not create parallel currency, item, or stat records that contradict the destination campaign's actual simulation.**

## 5. Currency and Resource Integrity

A conversion must preserve clear accounting.

If currency is converted from Campaign A, that amount must be deducted from Campaign A.

The universal-point wallet must receive only the valid conversion amount.

If points are redeemed in Campaign B, they must be deducted from the universal wallet before or atomically with the corresponding destination grant.

The operation must be safely recoverable if any stage fails.

The implementation must prevent:

- Duplicating currency through repeated transactions.
- Reversing source deductions through save manipulation while retaining points.
- Repeating a conversion by loading an earlier checkpoint.
- Exploiting campaign forks or copied saves to redeem the same economic value multiple times.
- Receiving a purchased reward without paying the required points.
- Charging points multiple times for one redemption.
- Creating benefits through incomplete or failed transactions.
- Moving point-purchased advantages into ineligible multiplayer campaigns.

These are design requirements for future implementation, not authorization to select a particular technical solution yet.

## 6. Character Progression and Equipment

The universal-point system may eventually offer character progression points.

However, their precise operation must be compatible with the destination campaign's adopted progression mechanics.

Do not assume every genre or campaign uses the same attributes, skill points, levels, or advancement limits.

Likewise, equipment redemptions must refer to actual content defined within the applicable campaign or its genre and setting libraries.

For example, purchasing a weapon for a medieval campaign must not automatically generate a weapon that does not exist in its available content.

An authorized external equipment grant should create a real item record with appropriate ownership, location, condition, and other required properties.

Such grants should be identifiable as external purchases rather than falsely recorded as ordinary manufacturing, trade, or historical acquisition.

The same principle applies to currency and character improvements.

## 7. Campaign Independence

Individual IRGS campaigns remain independent simulations.

The universal points system must not merge their world states, histories, economies, populations, or institutions.

A campaign that receives a redemption should record only the authorized benefit and its provenance.

Characters from one campaign do not automatically exist in another.

Likewise, transferring economic value does not transfer political authority, employment relationships, institutional membership, or historical accomplishments.

The account-level points wallet is the only intended cross-campaign progression mechanism described by this feature.

## 8. Future Website Interface

A future interface may be added to the player's account or solo-campaign management area.

Proposed sections include:

**Universal Points Wallet**
- Available points.
- Transaction history.
- Pending or failed exchanges.
- Eligible campaigns.

**Currency Conversion**
- Source campaign.
- Available eligible currencies.
- Amount selected.
- Exchange rate.
- Expected points received.
- Transaction confirmation.

**Campaign Redemption**
- Destination campaign.
- Available rewards.
- Point costs.
- Character or inventory destination, where applicable.
- Compatibility and eligibility validation.
- Redemption confirmation.

The exact interface layout is deferred until feature development begins.

## 9. Explicitly Undetermined Mechanics

Do not invent or implement unapproved values for:

- Universal-point exchange rates.
- Relative values of different campaign currencies.
- Conversion limits.
- Redemption costs.
- Available stat increases.
- Progression caps or exceptions.
- Eligible equipment categories.
- Equipment rarity restrictions.
- Inflation or exchange-rate adjustments.
- Transaction fees.
- Minimum or maximum balances.
- Campaign-specific eligibility.
- Whether conversion rates are fixed or variable.
- How save branches contribute to the account-level economy.

These decisions require dedicated systems design, economic modelling, exploit analysis, and calibration.

The feature's existence must not be treated as approval of any particular exchange formula.

## 10. Required Future Testing

When the system is eventually developed, it must be tested for:

1. Source-campaign currency deduction.
2. Account-level point credit.
3. Destination-campaign redemption.
4. Invalid and insufficient balances.
5. Interrupted and failed transactions.
6. Repeated requests and duplicate submissions.
7. Campaign branching and save restoration.
8. Imported or copied campaign saves.
9. Multiple simultaneous exchange requests.
10. Character progression compatibility.
11. Equipment creation and ownership.
12. Multiplayer access restrictions.
13. Campaign deletion and restoration.
14. Transaction-history and ledger reconciliation.
15. Long-term account and campaign persistence.

Passing ordinary transaction tests will not establish that the exchange economy is balanced.

Exchange rates and rewards require separate calibration.

## 11. Current Codex Implementation Instruction

**Do not implement the complete currency exchange system at this stage.**

For now:

1. Register the system as an intended future IRGS feature.
2. Document its ownership at the platform/account level.
3. Identify the existing Core interfaces on which it would depend.
4. Preserve compatibility with future controlled resource grants and deductions.
5. Identify any obvious conflicts with the current persistence and save-branch architecture.
6. Avoid introducing irreversible design decisions that would obstruct this feature later.
7. Do not add exchange rates, universal-point balances, stores, or functional purchase controls without further authorization.
8. Do not modify existing solo campaign economies to simulate the feature prematurely.
9. Do not introduce the feature into multiplayer gameplay.
10. Include its future development and unresolved dependencies in the IRGS roadmap.

Any additional mechanism required for implementation must first undergo the normal IRGS Compare → Merge → Reconcile → Resubmit process.

## 12. Status and Future Development

**Established intent:**
- Cross-campaign currency conversion.
- Universal points usable across eligible solo campaigns.
- Redemptions for campaign money, progression points, and equipment.
- Solo-play exclusivity.
- Preservation of independent campaign simulations.

**Proposed architecture:**
- Platform-owned universal wallet.
- Core-authoritative campaign debits and grants.
- Auditable transaction records.
- Compatibility and anti-duplication safeguards.

**Deferred:**
- Full economic design.
- Conversion formulas.
- Redemption rules.
- Limits and restrictions.
- UI implementation.
- Calibration.
- Acceptance testing and deployment.

**Final instruction:** Preserve this feature as a future platform capability without prematurely designing its economy or implementing incomplete mechanics.

The objective is to allow success in one solo campaign to support progress in another while keeping every campaign's simulation, resource accounting, and history internally consistent.

**End of Codex Feature Instruction — Solo-Play Cross-Campaign Currency Exchange.**


---

## End of Unified Master Codex Instructions v1.0

This complete document contains the v1.0 integrated directive, the interactive campaign-opening and non-destructive IP-protection extensions, the route/feature registry mandate, reconciliation, and all four original full source volumes preserved without substantive deletion. The archival source volumes may carry their original older version labels; the v1.0 integrated directive and named supersession rules govern.
