# Historical campaign and website design integration

Decision/account date: **20 October 2026**. Scope: the selected local Core 3.3 suite, the HYW player discovery/creation flow, permissioned navigation, structured background testimony, actor-known opening presentation and read-only historical-plan assessment. This is a consolidated integration account, not adoption of every statement in the supplied master instructions and not full Stage-One acceptance.

## Human authority and source status

The human request is to develop the website through comparison, merge, reconciliation and a coherent resubmission while preserving existing working systems. The HYW 1415 start is the immediate implementation focus. Thirty-seven catalogue entries, ten featured years and three period groups remain; other dates do not acquire researched initializers by appearing in a design table.

The latest AST direction is narrower than earlier campaign-maintenance assumptions: reusable mechanics may serve shared Core or genre handlers, while A Scot's Tale is a named 1415 starting reference rather than a separately maintained campaign/engine. Existing adapters, library payloads, profile identity, archival character registry and saved games are preserved. This does not authorize an inferred civil date, recruitment scene or later service appointment.

The user confirmed that the audited character registry is a post-Day-2 guide and corrected the horse's name to Abel. Those facts remain preserved. A source document calling other claims “established,” “adopted,” “approved,” or “instructions to Codex” is not additional human authorization. Its claims retain their recorded evidentiary scope. Illustrative dialogue, unrelated images, proposed UI and numerical tables are not automatically world facts or operational models.

## Inputs compared

| Input | Exact source path | Status/use |
|---|---|---|
| Campaign Design Integration v0.3 | `C:/Users/ian_c/.codex/attachments/549e30fb-525a-40dc-bb79-9203ca190bc8/Pasted text.txt` | Proposed independent careers, nationality/service separation and scenario hierarchy; earlier no-future-plan wording requires reconciliation |
| Historical Timeline and Event Simulation v0.2 | `C:/Users/ian_c/.codex/attachments/72742e29-89b6-471c-9141-0fa2692b9a67/Pasted text.txt` | Proposed conditional historical baseline/plan/actual-history separation; not an installed scheduler |
| Stage-One Content Library CMRR audit v1.1 | `.integration/patch-20261020/IRGS Patch/IRGS_Core_3_3_Stage1_Content_Library_CMRR_Audit_v1_1.md` | Audit of supplied snapshot/overlays; useful defect inventory, not proof of the current live tree or process |
| Unified Master Codex Instructions v1.1 | `.integration/patch-20261020/IRGS Patch/IRGS_Unified_Master_Codex_Instructions_v1_1_CMRR.md` | Proposed reconciliation with preserved earlier volumes; Parts A–C, VI, historical Volume C and its supersession register inform this scope |
| Live shared mechanisms and sources | `IRGS_3_3/runtime/core_world.py`, `temporal_registry.py`, `starting_selection.py`, `IRGS_Web/server.py`, `gameplay_views.py`, existing source/catalogue payloads | Reuse actual interfaces and preserve their limitations; implementation status is established through current tests and manifests |

Read-only source hashes captured for the four design/audit inputs:

| Input | SHA-256 |
|---|---|
| Campaign v0.3 | `03e79431d75f46a8a754828024525a323e74281effb19e88b23dd103a2d352b7` |
| Timeline v0.2 | `db093854c0400fe0746f2c28828aa06f38c14dff25b57ae106998c6c0e443a36` |
| CMRR audit v1.1 | `4f5155e1189ba67026df68558f711724be51d887cb6fdc7301ad7b3eecdee948` |
| Unified v1.1 | `7515928d715c7c2630c52e22822dfe9be7b76ba587675bb41388a721bebe4741` |

The patch sources overlap. Their release manifests must not be stacked or treated as migrations. Final integrity evidence belongs to the actual assembled code, not an arbitrary supplied manifest. Detailed file/hash accounting and verification remain in the release builder's current evidence.

## Conflicts and decisions

| Conflict | Reconciled disposition on 20 October |
|---|---|
| Engine/library registrations versus player games | Preserve all six genres, eight technical libraries and seven legacy profiles. Ordinary discovery and creation list only HYW; appropriate Creator tools and existing saves retain technical access. |
| Ten principal starts versus 37 catalogue entries | Preserve the existing three groups and all 37 entries. Ten featured years are a presentation subset, not ten replacement engines or period objects. Only 1415 currently launches. |
| Historical opening date | Retain the selected authored 11 August 1415 Julian before-departure cutoff, with no exact hour. The proposed 13/14 August alternatives are separate research/design claims and are not silently substituted. |
| AST recruitment versus saved personal checkpoint | Keep the named reference disabled until its civil date/checkpoint is verified. Preserve the post-Day-2 record; do not preload later events into recruitment or reinterpret prospective sponsorship as formal appointment/wages/muster. |
| Nationality, control and career | Keep them independent. Structured origin/family/career text is received testimony; an organization to approach is not an accepted employer or granted authority. |
| Earlier unscheduled future versus revised conditional history | Conditional historical progression is the intended design target. The present implementation supplies reference assessment only. It neither claims a finished unscheduled sandbox meets that target nor enables historical execution prematurely. |
| Setup history versus actor knowledge | Historical truth is not automatic receipt. Opening presentation uses actor-filtered current/received records, supplies no source-only political hook and never exposes prospective outcomes to the player. |
| Source edition updates versus campaign continuity | New HYW worlds pin a prospective baseline snapshot/hash. Existing saves are not migrated on read. Forks retain the selected edition and explicit provenance under a new campaign scope. |
| Planned navigation versus working mechanics | Register and scope routes truthfully. A visible planned tab grants no API permission, assets, time advance, AI provider, contracts or numerical model. |
| Stage-One text intro versus resolved gameplay | Preserve useful presentation and retry machinery, but explicitly retain `declared_not_resolved`. No opening text, testimony receipt or planning metadata is represented as an adjudicated physical consequence. |

## Ownership and reuse matrix

| Owner | Reused or added interface | Scope and boundary |
|---|---|---|
| Shared Core | `runtime/core_world.py` | Authoritative actor/evidence/receipt/control/resource transactions. No new historical execution operation is introduced here. |
| Shared temporal registry | `runtime/temporal_registry.py` | Actual committed existence, identity, relations and eligibility. Historical reference data does not restore dissolved entities or create future identities. |
| Historical foundation | `runtime/historical_campaigns.py`, `historical_plans.py` | Existing snapshot/hash selection plus generic pure assessment; reference chronology, prospective metadata and actual journal remain distinct. |
| HYW content | `data/hyw_entry_catalogue.json`, `hyw_1415_opening.json`, `hyw_historical_baseline.json` | Date-specific references and source provenance; no Core copy, invented stocks or additional 36 initializers. |
| Shared starting review | `runtime/starting_selection.py`, `character_background.py` | Optional structured identity/life-path/career testimony and receipt, reviewed explicit control, pinned prospective reference at new-world creation. |
| Web discovery and authorization | `IRGS_Web/features.py`, `server.py`, `data/campaign_listings.json` | Sole ordinary HYW launch allowlist, exact selection, protected feature and historical inspection routes. This is local-owner scope, not hosted account authentication. |
| Player projections/opening | `IRGS_Web/gameplay_views.py`, `opening_scene.py` | Actor-known presentation metadata; no knowledge grant, world event or later scene override. |
| Website interface | `IRGS_Web/static/app.js`, `index.html`, `style.css` | Carry selected IDs/hashes through review, present optional drafts and routed views, keep unavailable functions visibly unavailable. |
| Chronicle/memory | `IRGS_Web/history_views.py` | Existing permission-scoped retrieval and exact interval planning reused. No automatic calendar closure, durable summaries or dialogue reconstruction. |
| AST compatibility/archive | Existing `catalog/libraries/ast`, legacy profile/adapter and saved records | Preserve existing bytes and compatibility; reusable behavior uses shared owners. No new standalone AST engine or maintenance track. |

## Implemented scope

### Discovery, navigation and reviewed creation

The player Content Library contains HYW alone. Ordinary creation validates a playable registered entry and its exact snapshot hash. The clicked 1415 entry is retained through creation review; missing, stale or mismatched selection cannot fall back to AST, a generic engine profile or a nearby year. Other 36 entries remain inspectable proposals. The named A Scot's Tale reference is visible under 1415 with its date-reconciliation reason and no launch capability.

The central feature tree currently contains **131 development nodes**, with **81 player nodes** and **131 local-owner Creator nodes** in the corresponding projections. It includes planned/deferred children and historical comparison. Metadata filtering and underlying endpoint protection are independent. Development visibility does not elevate a player request into Creator access. Nodes marked planned, scaffold or deferred are not claimed as operational workspaces.

### Background and opening information

Optional `identity`, `life_path` and `career` fields are validated structured testimony. They separate nationality/cultural origin from desired service, civilian work, mercenary work or independence. `offer_claimed`, `current_claimed` and related stages remain player claims. A selected organization must exist in the reviewed dated registry; selecting it creates no membership or command right.

The same Core evidence/receipt mechanisms record these statements for the new character. No relatives are spawned, household balances allocated, skills conferred, contracts accepted or equipment created. Full family/household, education, progression and employment initialization remains future work.

The saved opening presents the character's permitted identity, established location when available and legitimately received material. If local information is absent, it says so. It does not use historical setup facts as PC-known news, invent nearby people, replay sample dialogue or replace later current-scene records. The presentation has no world effects. Declaration/withdrawal status describes intent and presentation, not resolved action.

### Historical reference assessment

The generic API validates baseline provenance/DAG/date intervals, initializes prospective reference metadata and assesses typed live-record predicates without executing code from content. The partial HYW baseline contains three researched anchors: 18 September negotiations and 22 September Harfleur handover from Henry V's contemporary report in an edited translation, and 25 October Agincourt from Royal Armouries. The source perspectives and their limits are recorded in the baseline. No disputed landing or siege-start date is adopted.

Historical descriptions and outcomes are reference assertions. Condition bindings and dependency edges are explicitly design inferences; they do not certify exhaustive historical causation. Actual records are checked only at the live registry's committed coordinate. Same-day or overlapping dates are held because within-day order is unknown; unsupported calendar axes remain unbound. Past reference IDs do not replay events or establish journal occurrences.

Missing/null bindings remain unknown. A known dead/dissolved required identity blocks the exact configuration; a changed supporting condition marks risk. Dependency reevaluation follows connected descendants, with no global divergence score. Existing terminal states do not resurrect. Explicit journal links remain links, not automatic historical matching or proof of a victory.

New HYW worlds store their baseline snapshot/hash as prospective reference metadata. Old saves are not automatically modified; unpinned worlds can receive a detached preview. Fork helpers rebind campaign scope while preserving source edition, terminal states and provenance. Plan inspection never writes either campaign. Every assessment keeps execution unavailable, historical-path completeness uncertified and actual outcome unresolved.

Creator-only `/api/historical-baseline` and `/api/historical-plans/{id}` are separate from default player projections and Chronicle. No prospective expectation becomes actor knowledge merely because it is loaded or saved.

## Supplied audit disposition

| Audit item | Current disposition |
|---|---|
| C-01/C-02 discovery and clicked selection | Addressed within the HYW allowlist, exact entry/hash review and ordinary creation flow; technical profiles preserved. |
| C-03 actual resolved first action | **Still open.** Declaration recording is not outcome execution or an NPC/world reaction. |
| C-04 setup-reference knowledge leak | Corrected in opening presentation using the existing player projection; no historical future data is exposed. |
| C-05 grounded opening interaction | **Still open.** Honest actor-known presentation is not a locally grounded NPC interaction or physical opening event. |
| C-06 historical future mismatch | Partial foundation: generic reference assessment and pinned metadata. No calendar-driven scheduler or historical outcome resolver. |
| C-07/C-08 navigation and scope | Expanded centralized scoped tree and protected data routes. This does not certify complete operational child mechanics, public multi-account security or a manual browser/visual pass. |
| C-09 AST hierarchy | Named 1415 reference only, blocked pending chronology; archived profile/source/saves preserved. |
| C-10 Life-Path depth | Structured testimony capture only. Actual family NPCs, household economy, learning histories and full contracts remain open. |
| C-11 World workspaces | Addressable navigation and available record projections; no invented map geometry, markets, populations or command models. |
| C-12 manifests/overlap | One assembled codebase requires a matching regenerated release manifest; supplied patch hashes are not interchangeable with final hashes. |
| C-13 opening status | Intent/withdrawal presentation is scoped and retained separately from actual outcome. No claim of a complete consequential opening-state machine. |
| C-14 existing protection | Session/Creator boundaries, integrity checks and recoverable saves retained. No destructive anti-copy mechanism or deferred wallet operation added. |

The original supplied Stage-One patch contains no actual Core-resolved first turn. This integration does not relabel its metadata as physical gameplay or mark that acceptance gate passed.

## Evidence and remaining gates

Exact current counts and run identities belong to [results/completion_audit.json](results/completion_audit.json), current runtime/HTTP logs including [results/stage1_all_web_tests.txt](results/stage1_all_web_tests.txt), [results/gameplay_ui_tests.txt](results/gameplay_ui_tests.txt), dependency certification, saved-state preservation and package verification evidence. Counts from the supplied audit or earlier local runs remain historical evidence of their own source identity. They are not repeated here as proof of the final assembled release.

This is not a full Stage-One completion or calibrated HYW simulation. Remaining gates include general freeform adjudication, grounded NPC reaction, supported narration, live calendar advancement, durable epoch archives, actual family/skills Life-Path creation, complete service contracts, general autonomous historical institutions and operational conditional-history execution. Research remains necessary for AST's named start chronology, detailed 1415 local openings, complete inventories/authority, causal event dependencies, calibrated conditions and the other 36 starts.

No full campaign playtest, complete visual/browser review, historical casualty/resource calibration or six-Director provider runtime is claimed by this document. Workshop, Marketplace, solo currency conversion and hosted entitlement enforcement remain outside this integration's implemented mechanics. The historical reference horizon does not impose an ending in 1453.
