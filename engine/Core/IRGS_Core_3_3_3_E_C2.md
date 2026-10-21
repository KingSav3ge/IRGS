# IRGS Engine/Core 3.3.3.E — C2 applied specification

# IRGS engine 3.3.3.E — C2 application

**Text-engine revision:** 3.3.3.E  
**Applied design:** C2 · 20 October 2026  
**Foundation:** Selected Core 3.3  
**Status:** Applied engine text; implementation and verification outstanding.

This edition incorporates the complete inherited engine and C2's developed rules into one specification. The application changes engine text, not executable handlers, numerical model adoption, live campaign bindings or deployment status. The user's latest direction returns attention to overall IRGS development rather than a separate handoff workstream.

The supplied 3.3.3 package is the current packaging baseline. Its 274 assembled payload files, including all 57 runtime Python files and the complete Core text, match the verified predecessor source. This application is based on the existing 3.3.3.E branch at a906b3316712d4f7902bb611eaccf2fc6dd0cf73 and preserves all seven files in that engine branch, including its deliberate omission of the Live/App ZIP.

## Current development designations

The user's current designations are **3.3.3.E for Engine/Core** and **3.3.3.A for App/Web**. Earlier C2 source documents used 3.3.C for the engine and 3.3.E for the application. Those original documents remain immutable historical references. In the consolidated applied engine, designation prose is relabelled to the current names; hashes continue to identify the original source documents. Historical package filenames and actual Core binding versions retain their original identities.

Publication uses the current Engine/Core branch as its parent and preserves its deliberate package split. The App/Web branch's separate package selection is not changed by an engine update.

## How to use this edition

Read the application decisions below, the inherited Core, then the applied C2 chapters. The complete source contracts remain separately available under `design/C2/` for implementation requirements and acceptance evidence. The binding and application record identify exact versions and hashes.

The inherited source is retained in full. Its release notes describe the then-current local implementation; its candidate sections describe their original source status. They do not activate or repeal mechanics merely by appearing in this branch. C2 specializes the proposed action, information, time, dependency and recovery contracts while retaining all existing owners and supported campaign scopes.

## Reconciled application decisions

| Subject | Meaning in 3.3.3.E |
| --- | --- |
| Authority/version labels | The selected live foundation is Core 3.3. Inherited phrases saying Core 3.2 remains selected, R7/R8 are unselected, or a historical next priority is pending describe their original source editions. They do not redirect this branch to an older active binding. |
| Declaration-only runtime | The existing `declared_not_resolved` behaviour remains an honest runtime limit. C2's consequential actions are now engine-text requirements for implementation; their inclusion is not evidence that the current runtime performs them. |
| d100 and other adapters | Preserve the inherited default/reference adapter and explicit campaign overrides within their already recorded scope. C2's statement that it adopts no new universal dice does not repeal inherited scope or globally activate d100/genre values. Do not invent an adapter where the current campaign's binding leaves the dependent mechanism unresolved. |
| Dependency instrumentation | Old conservative list reservations and manually declared footprints remain historical implementation descriptions. C2 requires execution-derived authorization, decision, prerequisite and effect observations, with actual list-read/mutation distinction and case-specific evidence. |
| Ownership | Keep the nine K-owners and established domain workflows. No application, planner, view or persistence index becomes a second authority for the same people, stock or history. |
| Lifecycle | The C2 supplement's phase/parent meanings and separate submission/attempt receipts govern the new design. Map old status labels explicitly; scheduling is not completed work and a later phase is not a replay of its booking. |
| Time | Causal sequence, storage revision, elapsed time, civil date, information time and wall-clock execution remain distinct. C2 supplies no automatic conversion or unrecorded historical opening hour. |
| Information and speech | NPC agency can propose wording before Core commits an utterance. Player-facing narration describes committed effects and permitted receipts. Neither route can write arbitrary world truth or expose hidden validation facts. |
| Search repetition | An accepted-phase retry or redisplay causes no new work. A new physical search may use supported attention/time; it cannot regenerate established stock or automatically reroll retained uncertainty. |
| Historical continuity | New dated worlds load verified snapshots; continuing worlds use actual committed state. Historical references are not mandatory future occurrences, and absent entities do not resurrect. |
| Fixture values | C2's times, parcels, funds, mandates and bay policies are explicitly synthetic test selections, not historical rates or campaign-wide defaults. |
| Acceptance | The 121 cases and seven packets are implementation requirements. No new runtime, calibration or playtest result is asserted by applying the text. |

If a live campaign's selected rule conflicts with a proposed new mechanism, preserve the selected rule until an explicit compatible adoption bridge is qualified. Do not retroactively reinterpret accepted actions, processed spans, injuries, resources, knowledge, agreements or obligations.

## Consolidated chapter map

The generated engine document contains explicit anchors for the inherited Core and each applied chapter:

- `inherited-core-3-3`
- `c2-shared-engine-contract`
- `c2-actions-and-dependencies`
- `c2-persistence-and-recovery`
- `c2-agency-and-presentation`
- `c2-institutional-execution`
- `c2-timeline-and-processes`
- `c2-movement-and-observation`
- `c2-dialogue-and-social-actions`
- `c2-playable-action-cycle`

The original Core, C2 contracts, acceptance inventory and handoff remain separately traceable. Relative source links, heading depth and current development designation prose are adapted for consolidation; the inherited clauses and C2 rules remain complete. The application record discloses those editorial transformations.

## Incorporation audit

[C1/C2 incorporation register](../C1_C2_INCORPORATION.md) records existing foundations, partial coverage and missing implementation. The original package references C2 without applying its chapters to the Core or implementing the general action cycle. This edition supplies the missing engine text; the register does not relabel proposals as working software. Engine and application development now proceed together on 3.3.3.E and 3.3.3.A respectively.


<a id="inherited-core-3-3"></a>

## Complete inherited Core 3.3


## IRGS Core 3.3 selected local receiving edition

Current selection and operational limits follow. The complete inherited rule baseline is retained afterwards; historical candidate labels describe their original scope. Unresolved profiles and numerical proposals remain unresolved unless explicitly selected.

## IRGS Core 3.3 local release

Core 3.3 is the selected runtime for this local suite. Its six genre bindings are Military, Roman Republic, Fantasy, Post-Apocalyptic, Shinobi Nexus and Space. Eight technical content libraries and seven legacy profile registrations remain installed. Ordinary player discovery lists **The Hundred Years’ War** only; technical registration does not make an engine, library or legacy profile a separate playable campaign.

A Scot’s Tale is a named 1415 starting reference. Its reusable mechanics belong to shared Core/genre handlers, and its preserved adapter, library and profile remain compatibility/archive material. It is not maintained as a separate ongoing campaign or engine. Its new-start reference remains unavailable until its civil date and checkpoint are verified; the generic 11 August opening is not imposed on it.

This selection follows the user’s direction to deliver a live 3.3 version, then the expanded Core + genre engines + content libraries scope. Historical 3.2 source files and the R7/R8/R9 research packages remain preserved. Their embedded instructions are reference content, not permission to change saves or activate every proposed numerical model.

### Start and use

Double-click `Start-IRGS-3.3.cmd` whenever you want to play. It verifies the installed release, starts the local website in the background if needed, and opens **http://127.0.0.1:8765** in your default browser. You can close the launcher window; the host keeps running. Repeating the shortcut reuses an existing IRGS host instead of starting another. The `IRGS_Web/Start-IRGS.cmd` shortcut delegates to the same launcher. No new release is needed to open the website again.

If another application occupies the port, the launcher shows a readable error and leaves that application running. Startup records and logs are kept in `IRGS_3_3/live/`, outside the release payload and campaign saves. For a check without opening the browser, run `Start-IRGS-3.3.ps1 -NoBrowser`; `-Port` selects an explicit alternative port. The adjacent `IRGS_Web` directory must remain beside `IRGS_3_3`.

The website opens in Solo Gameplay, with Story, World and Chronicle views over the selected character's server-filtered information. Character, inventory, relationships, institutions and other inspection panels show available records; inspection does not advance the world. Reading preferences affect only this device.

**New campaign** follows Content Library → The Hundred Years’ War → Starting point → Character → Review → Start. The clicked entry ID and exact preview hash carry into review; stale or mismatched choices fail rather than falling back to another date or profile. Choose a named new character or an existing person made eligible by the selected scenario, then review that person's control scope. No campaign file is written before the final selection succeeds. Cancel and Back leave no saved game. Other installed profiles remain available through authorized Creator tooling and existing-save compatibility.

Optional structured identity, life-path and career fields preserve the creating player's testimony and its explicit receipt. Origin, nationality, control and career remain independent; no faction is mandatory. A named organization must exist in the dated starting world. Claimed current employment or an offer remains a claim: these fields create no contract, relatives, household wealth, competence, possessions, authority or accepted service. This is structured background capture, not a completed Life-Path or employment simulation.

To remove an accidental campaign or branch, select it and choose **Delete campaign**, then **Move to Trash**. It disappears from the active list. **Campaign Trash** provides **Restore**, retaining the complete original save byte for byte. Deletion checks the displayed revision and rejects stale requests; restoration refuses to overwrite an active campaign with the same ID. Branches are separate saves, so removing a branch leaves its original campaign intact. The website does not permanently erase trashed saves.

### Solo Gameplay and Creator workspace

Player requests receive only the controlled character's current record, explicitly received evidence and orders, known identities, and supported commitments. Current stock quantities require explicit inventory-inspection rights; a location name or a claimed possession does not grant access. Global scene notes, other actors' private current records, unreceived evidence, unresolved engine payloads, source policies and full historical snapshots are excluded from player responses. A known identity does not reveal that person's private state.

Submitting a declaration preserves the exact player text through Core `record_player_action`. Its result is `declared_not_resolved`: no outcome, reaction, cost, elapsed time or narrative is invented. One unresolved gameplay declaration per character is allowed. **Withdraw pending attempt** retains the original Core record and changes only the request's withdrawal metadata, permitting a revised declaration. A character who no longer exists at the committed world date retains their selected identity and history; new declarations are refused and no successor is chosen automatically.

The player routes are session-protected `/api/playthrough/{id}`, `/api/availability/{id}`, `/api/chronicle/{id}`, `/api/declaration`, `/api/withdraw-declaration` and `/api/action-result/{campaign}/{request_id}`. Declaration and withdrawal request identities and exact payload digests persist with the same save. A repeated request recovers the original acknowledgement before checking a stale revision; altered payloads are rejected. Result retrieval recovers a lost response. Campaign and actor checks prevent inherited branch receipts from being replayed as the branch's own action.

The final creation review also uses a stable request identity and exact choice digest. Repeating an accepted creation returns the existing campaign, even if the opening source subsequently changes; it cannot create a second game or silently change the chosen character. A retry for a game now in Trash reports that status without restoring it. Creation and declaration acknowledgements follow the atomic save write.

**Creator workspace** is an explicit opt-in for this local campaign owner. It exposes source lookup, raw inspection and supported event/frontier/mandate/decision tools. Raw `/api/campaign/{id}` and `/api/binding/{id}` require `mode=creator` plus the session token; legacy editing and branch routes likewise require explicit Creator mode and the token. The default player frontend does not fetch raw saves. This is an owner-controlled local workspace with a separate inspection capability, not a multi-account authentication service. Creator tools still use the same authoritative world and Core validation.

The centralized feature tree contains 131 development nodes: 81 in the player projection and 131 in the explicit local-owner Creator projection. Planned or deferred routes are descriptions, not enabled mechanics. The server filters navigation metadata by scope and independently protects underlying data routes; a development-stage query grants no Creator rights. Historical baseline and plan inspection require Creator mode and the session token. This does not establish hosted multi-account authorization.

### Hundred Years’ War historical setting

In **New campaign**, choose **The Hundred Years’ War**. This setting uses the existing Military profile and library. Ten principal years lead to the full catalogue of **37** supplied entries: 12 Edwardian, 14 Caroline/interwar and 11 Lancastrian. The original closing claim of 35 was a counting error; no rows were discarded. Entries retain their proposed status until a dated opening has been developed and checked.

**1415 — The Lancastrian Invasion** is the first developed opening; the other **36** entries remain proposed. Its authored cutoff is **11 August 1415, Julian calendar, before the recorded departure**; the hour is unspecified. The preview provides sourced political, military, territorial and diplomatic context and a practical entry guide. The dated setup contains five historical people and five political entities. The authored Solo scenario permits choosing one of those five individuals or creating a new character. Existing political entities are not selectable national commands in this individual scenario. Operational quantities such as actual deployable troops, ready ships, provisions and balances remain unknown where evidence has not established them.

An explicit creation request identifies the entry, exact snapshot hash, reviewed availability digest and selected character. Inspection and cancellation create no campaign. Creation copies the opening into a new campaign scope and records the explicit player setup before its first save. Optional background testimony receives its own actual setup receipt. These causal setup records advance no elapsed world time and schedule no historical outcome. Other catalogue dates can be inspected but cannot create a substitute 1415 world. A custom year without a matching developed snapshot is unavailable; a nearby date is never substituted.

The opening reference is preserved separately from current scene presentation and the event journal. It records historical setup, not automatically received character knowledge. It remains an opening reference after later campaign changes. Existing AST saves retain their own post-Day-2 checkpoint and are not redated or merged with this setting.

Opening presentation uses the same actor-filtered projection as ordinary player reads. It supplies no political setup fact as automatically known news, no future historical knowledge and no invented nearby actor or scene. Unknown location remains unknown. This saved presentation metadata is not a consequential Core event or an NPC interaction, and it does not override later current-scene records. Declaration and withdrawal presentation remains distinct from resolved action status.

### Conditional historical reference assessment

The revised design requests a conditional historical default: recorded events are intended expectations only while their causes remain supported. That is the integration target, not an implemented automatic scheduler. The current generic `historical_plans` module assesses three researched 1415 references: Harfleur negotiations on 18 September, its handover on 22 September and Agincourt on 25 October. Source-backed dates/outcomes are separated from explicitly authored causal inferences and exact live-record bindings. The disputed landing and siege-start dates are outside this baseline.

New historical worlds save a pinned copy/hash of this prospective reference edition. Forks rebind its campaign scope and retain source provenance and existing terminal plan states. Existing saves acquire no automatic new metadata or historical migration; an unpinned campaign can receive a read-only preview. Historical reference outcomes are never matched to journal entries by guesswork, and a past reference is never replayed as a new occurrence.

Assessments distinguish satisfied, unsatisfied and unknown conditions. Missing/null resources, authority or other bindings cannot establish an intact pathway. A dead or dissolved required identity blocks that exact configuration; supporting changes mark risk, and dependency reevaluation remains local to connected descendants. Prevented, superseded and expired plans do not reactivate merely because conditions improve or a historical date arrives. Every report keeps execution unavailable; no calendar advancement, baseline victory, casualties, actor resurrection, successor selection or world effect is applied. Prospective references remain Creator-only material, not character knowledge.

The supplied gameplay-screen and epoch-memory documents remain archived design references. Their illustrative dialogue is not a recorded scene. Solo Gameplay, filtered Story/World/Chronicle views, the starting review and scoped history retrieval are implemented within the limits described here. Automatic narration, outcome resolution, calendar advancement and a durable epoch-summary service remain unavailable.

The local website records declarations and supported state changes. It does not run a general AI narrator or fabricate unsupported combat, medical, learning or historical outcomes. Those procedures use the supplied genre rules and whatever complete, supported parameters the campaign actually selects.

### Runtime structure

| Component | Responsibility | State effect |
|---|---|---|
| `core_world.CoreWorld` | Common campaign transactions, identities, evidence, knowledge, stocks, commitments and journal | One authoritative state per campaign |
| Genre receivers | Explicit domain preconditions using Core owners | Same transaction and ledger |
| Content libraries | Definitions, source payloads, aliases, profiles, holds and evidence | Lookup creates no actors, goods, effects or time |
| Campaign profile | Chooses genre/libraries and supported initial context | Initializes a new campaign only |
| Temporal registry | Dated identity, existence, relations and explicit scenario eligibility/control | Same Core state and instrumented journal |
| Historical plan assessment | Versioned baseline references, prospective metadata and read-only condition checks | No execution, scheduling, calendar advancement or outcome grants |
| Local host | Player projections, reviewed creation, revision checks, serialized writes, frontiers and decisions | Atomically persists the same campaign state |
| Strategic executor | Institutional observations, rights and policies | Proposes operations to the shared frontier |

Nineteen canonical common operations cover evidence/receipt, declarations, scenes, supported character-field confirmation, sourced stock initialization and transfer, obligations, designs, received orders, actor registration, capacity, activity booking, delegation and the five shared temporal operations: `register_entity`, `transition_entity`, `record_entity_relation`, `record_entity_eligibility` and `select_entity_control`. The ten historical AST event spellings remain compatibility aliases, with equivalent domain effects.

The registry distinguishes existence, conflict participation and scenario eligibility. A sourced control policy names actual control actors and the supported `declare_own_intent` power; it does not confer an institutional mandate. Identity and relation versions use explicit effective coordinates on a named time axis. Core's causal event sequence is separate from that calendar coordinate. Actor registration and dated identity creation share one instrumented transaction when a registry is configured. Death or dissolution closes affected effective relations and eligibility while retaining their provenance; it creates no replacement actor, institution or authority.

Historical templates seed only a newly created world. Continuing-game availability queries use that playthrough's committed registry coordinate and actual versions, including departures from the historical opening. They do not reload a template, restore a dissolved entity, reveal future versions or infer a civil date from the event count. Existing saves without a temporal registry remain readable and report registry availability as unavailable; inspection performs no automatic migration.

Bounded campaign-native receivers additionally issue equipment against received Military directives, start a Roman delegated activity against an active grant, and revoke a delegation. They use actual stock and shared person/site capacity. They do not independently complete manufacture, confer military readiness or resolve Roman law. Earlier R9 receiver operations remain available only in their explicitly identified legacy research fixtures.

### Dependency and transaction guarantees

The observer follows the complete selected dispatch chain, including physical-loss reconciliation, tracked work and fabrication in the supported research profiles. Reads include missing-record lookups, enumeration/phantom dependencies, source profile choices, commitments, receipts, authority and actual scarce resources. Writes include recorded intents and an actual state-difference backstop. Transaction clones retain their observer. Whole-list reads are conservatively treated as potential writes outside constructors/validation; broad invariant reads are retained separately and checked against the assembled candidate.

Each certificate identifies the event, pre-state hash, code hash, backend/profile, observed reads, writes and post-state hash. Every commit attempt observes afresh. Read/read overlap is permitted; write/read and write/write overlap preserve conflicting proposals without choosing an ID winner. Unknown or invalid operations cannot acquire independence by omission. Qualified physical losses remain actual occurrences: compatible measured losses commit, while causally conflicting work remains unexecuted. Incompatible combined loss measurements reject the frontier atomically.

Submitted nested parameters are detached from the caller. Journal signatures are verified. Same ID/same payload replays without effects; changed-payload replay fails. WIP loss replay does not repeat its reconciliation. New campaigns and explicit branches have distinct scopes; legacy saves retain their existing scope and bytes on read.

This is instrumentation of reviewed deterministic JSON-state Python. It is not a security sandbox for hostile plugins, external side effects, hidden globals or arbitrary C-level reads. Observed executions and interleaving checks are evidence for their named scope; they do not prove every reachable branch or every native genre procedure.

### Durable decisions

Simultaneous requests retain original payloads, digests, dependency edges and reasons in the campaign state. Mandates name an actual actor, source and operation scope. A genuinely later decision revalidates current resources, executes once or denies without applying the request. Occurrence evidence and player actions cannot be turned into delayed automatic approvals. A denial-only right can close an unqualified request without granting permission to execute it.

The host exposes submission, mandate and resolution routes under one lock and persisted revision. Single invalid events return an error without a save revision; batch submissions retain unresolved intent. Offline CLI changes write a new output file, preventing the older stale-memory overwrite pattern. Complete workflow state is preserved by save/reload; replay of only the older domain journal does not reconstruct every workflow metadata action.

### Strategic execution

Four bounded planners—household, business, government and military—receive detached projections of only selected, received observations. Their operation rights and subject scopes constrain proposals. Unknown information withholds a plan; actual shared handlers revalidate its consequences. Source selections, read paths, proposal decisions and changes of rights remain in the same world ledger.

The provided subscriptions, rates and rights are explicit synthetic verification inputs. They can advance a multi-institution verification scenario over days without a prewritten event list. They are not a general historical NPC planner, a live-game calendar binding, or adopted historical economic rates.

### Chronicle and epoch planning

Chronicle search and pagination operate only on records already filtered for the campaign, selected character and access scope. Personal history, biographies, relationships, institutions, timeline and archive are views of those supplied records. Missing sources stay missing; retrieval does not reconstruct dialogue or turn historical setup into personal memory. Read requests do not write sidecars, summaries or campaign state.

The history module also provides an interval planner for an explicitly supplied number of complete campaign-relative years. It partitions closed coverage without gaps or overlaps into annual, five-year, twenty-five-year, cumulative-century and separate sealed 500-year epoch ranges, leaving the current incomplete year outside closed coverage. It returns a coverage plan, not generated or published prose. Numeric word allowances require an explicit budget policy; none is silently selected. The website does not infer closed years, an adopted calendar consolidation origin or elapsed years from causal records. No durable summaries, automatic consolidation, narrator or time-advance service is activated.

### Preserved AST reference and compatibility

The archived audited v2 registry preserves 37 identities: 36 humans and **Abel**, one horse. “Able” was accidental and remains an archival alias. Its source status and provisional ratings remain unchanged. Archive preservation does not create a separately maintained AST engine or promise an ongoing campaign update.

The preserved personal checkpoint is post-Day-2, with no verified civil date for a new HYW initializer. It must not be silently replaced by a recruitment-yard scene or the generic historical cutoff. Existing saved records and compatibility access remain intact; reusable procedures continue through shared Core and genre owners.

### Genre and content limits

All six receiving bindings pin inspected source bytes to Core 3.3 without rewriting the older specifications. Complete source content is bundled, including selected and held SCL material. Lookup preserves statuses. Shinobi’s native resolution/resources, Fantasy’s effect profiles, Roman local legal/calibration choices, historical/Fantasy learning units and Space flight/life-support models remain distinct. No universal conversion or missing numerical default is invented.

The catalogue’s hold summary records 228 held SCL families, proposed genre templates and blocked legacy Shinobi records. A missing historical `RELEASE_BINDING_R3.json` is recorded as unverified historical deployment evidence; it was not reconstructed. Fresh hashes prove which local source bytes are actually bundled.

### Verification and packaging

The current completion audit and exact counts are in `results/completion_audit.json`, with runtime, HTTP, certification and strategic evidence alongside it. The current integration account is [DESIGN_INTEGRATION_2026_10_20.md](../reference/DESIGN_INTEGRATION_2026_10_20.md). Test results apply to their recorded code identity and scope; uploaded patch-audit counts are not evidence for an altered live tree. The catalogue/source manifest verifies bundled sources and receiving payloads. Release startup verifies runtime, data, source and host hashes. Existing-save preservation reports and distribution verification remain separate evidence.

This update does **not** complete the full Stage-One gameplay specification. General freeform adjudication, grounded autonomous NPC reactions, automatic narration, calendar advancement, a durable epoch-summary service, full contracts and a Core-backed family/skills Life-Path remain unavailable. Background receipts, opening text and reference-plan metadata are not substitutes for a resolved first interaction. No full campaign playtest or complete visual/browser pass is claimed by these notes.

From `IRGS_3_3`, with Python 3 and no third-party packages:

```text
python -m unittest discover -s runtime -p "test_*.py" -q
python runtime/run_r9_certification.py
python runtime/run_r9_scenario.py
python runtime/irgs.py catalog
python runtime/irgs.py library ast --query Abel --limit 3
python runtime/irgs.py verify
```

From the adjacent `IRGS_Web`, run `python -m unittest discover -s tests -v` for actual HTTP checks. The long tests perform sustained execution and save/reload comparisons; the instrumented pass excludes one repeated sustained test and records that exclusion explicitly. Source and runtime checks are complementary, not additional gameplay calibration.


## Preserved complete rule baseline

## IRGS Core v3.3 — Round 8 complete candidate

**PROPOSED / UNSELECTED. Core v3.2 remains selected.**

The full R7 text follows unchanged as the inherited candidate baseline. Its R7 labels and evidence retain their original scope. Appendix E adds the R8 proposal; it neither selects R7 nor grants native engine certification.

## IRGS — Integrated Core Engine
### Version 3.3 — Proposed complete unification candidate, CMRR Round 7

**Document ID:** `IRGS-CORE-3.3-CANDIDATE-R7`  
**Date:** 17 October 2026  
**Candidate iteration:** R7 (supersedes R6 proposal for design review only; neither edition is adopted).  
**Source baseline:** `IRGS-CORE-3.2` workshop parent, 14 October 2026, maintenance R3; unchanged sections are carried verbatim where possible. This candidate has new bytes and **is not the selected Core v3.2 maintenance R3 release**.  
**Status:** **PROPOSED CMRR resubmission only.** Core v3.2 remains the selected parent until explicit acceptance and a compatible deployment rebind. No numerical calibration, playtesting or campaign migration is asserted.  
**Purpose:** Supply the complete setting/theme-neutral procedures inherited by IRGS slim engines, modules and campaigns.  
**Scope:** Agency, causality, resolution, time, records, actors, information, institutions, resources, logistics, work, continuity, and all twelve proposed Core domains, including MIL.  
**Catalogue:** `IRGS-SCL-1.0` remains an external selected catalogue reference from the source package; R7 does not embed or activate the catalogue. Exact source entry revisions and receiving pins require separate verification.  
**Bindings:** [IRGS_Core_v3_3_Candidate_Binding_Proposal_R7.json](../reference/IRGS_Core_v3_3_Candidate_Binding_Proposal_R7.json) is an unselected migration design. Active systems continue to use their pinned v3.2 binding.  
**Validation:** R1–R6 validation sources remain in predecessor packages and `sources/`; new R7 evidence is in [CMRR_Round_7_Executed_Validation.md](../reference/CMRR_Round_7_Executed_Validation.md). The bounded R7 adapter schedules tracked milestones with pre-frontier declared footprints and demonstrates physical work-in-progress, later inspection and accepted completion or salvage. This is not an independently implemented, calibrated, legally qualified or playtested engine, and its footprints remain manually specified.  
**Migration:** None applied. Current user direction and established campaign overrides retain their stated precedence.

This engine contains its operating procedures directly. A selected genre supplies its specialized effect models, physiology, technology, institutions and extraordinary mechanisms. Missing parameters block only dependent calculations. Qualified routine work consumes real time and inputs without compulsory dice.

**Architecture:** Shared IRGS Core → Genre Foundation/Engine → Setting/Theme Module → Campaign Profile → Campaign State.

**Runtime perspectives:** Canon, World State, Actors, Simulation, Resolution and Presentation cooperate over the same owners and records.

**Authority:** Current explicit user direction/correction → established campaign rule or override → adopted genre foundation within scope → adopted Core → a named temporary proposal in an unresolved gap.

#### Use this engine

1. For existing campaigns, keep Core 3.2 and the established pins. Select this **candidate** only after explicit acceptance, receiving rebind and prospective migration.
2. Establish supported state through §88, preserving unresolved and hidden facts under §79.
3. Resolve actions through §5, scheduling through §11 and actual event commits through §91.
4. Enable domain workflows when they materially affect a decision. Core ownership does not require daily processing of every domain.
5. Present supported observable or received results under §90 and return player control.

#### Governing invariants

- One authoritative owner per actual fact, resource, condition, person and work total; summaries are views.
- Feasible actions require actual means, access, finite time and bounded effects.
- Player speech, thoughts, feelings and voluntary choices remain player-controlled.
- Occurrence, observation, interpretation, assertion, recognition, transmission and receipt remain distinct.
- Transfers debit and credit actual locations once; transit is a location; reservations, claims and forecasts are not new stock.
- Simultaneous activities share real capacity and consistent pre-event state; contention requires an allocation decision or selected policy.
- Retained uncertainty, work fractions, processed spans and event identities survive review, save/load and scale changes.
- Autonomous actors act from knowledge, goals, authority, obligations, competence and finite means. Off-screen execution continues.
- Stable success, ordinary life, prosperity, peace, development and legacy remain valid outcomes.

#### Navigation

| Sections | Function |
|---|---|
| 1–9 | Authority, agency, feasibility, action contract and selected resolution |
| 10–24 | Time, events, records, capability, conditions, stocks and claims |
| 25–46 | Institutions, staffing, delegation, service terms and accountability |
| 47–63 | Spatial interaction, reactions, effect channels, components, information and scales |
| 64–79 | Autonomous life, households, needs, projects, development and discovery |
| 80–100 | Presentation, runtime, persistence, adoption and correction |
| 101–112 | Dependencies, networks, services, sources, handling, population, support, learning and module contracts |
| 113–124 | GOV, ECO, INV, MAR, CIV, MED, WILD, INTEL, URBAN, LIFE, COMP and MIL |
| Appendix A | Shared owners, status and minimum records |
| Appendix B | Inheritance, deployment, migration and calibration |
| Appendix C | Complete acceptance cases and regression requirements |
| Appendix D | Optional scoped reference profiles |

**Unification design boundary:** Core may represent functioning social orders and armed institutions without a required military or historical-genre engine; specialist tactical/physical models, period institutions and equipment entries remain externally selected as needed. This candidate carries forward all other v3.2 provisions without changing their adoption status.

## Foundations and Resolution

<a id="core-1"></a>
### 1 Runtime Architecture and Ownership

| Runtime domain | Responsibility |
|---|---|
| Canon | Valid campaign facts, sources, corrections and history |
| World State | Current physical, social, environmental and economic state |
| Actors | PCs, NPCs, animals, cohorts, households and organizations |
| Simulation | Causal time, access, resources, work, dependencies and consequences |
| Resolution | Meaningful uncertainty within feasible limits |
| Presentation | Knowable narration, rolls, panels, reports and decisions |

Apply rules in this order: current explicit user direction/correction; established campaign rule or documented override; relevant adopted genre rule within its scope; this adopted Core edition; named temporary ruling where no adopted procedure exists. A genre rule outside its ownership does not replace a shared procedure. A scoped override identifies the exact behavior replaced, affected targets, effective time and migration.

Module composition has an additional check: two modules cannot silently own the same quantity or select incompatible effect models. Resolve the ownership/adapter conflict before dependent play (§112). Neither later publication nor a more specific-looking paragraph automatically migrates a campaign.

Core services may be optional to activate while remaining universally reusable. They do not require fantasy, military or catastrophe lore. Adding a service initializes supported facts only. Do not invent past people, assets or competence to complete a schema.

Within a selected compatible procedure, the specific rule governs its general description. Agency, causality, isolation, information boundaries and accounting invariants remain applicable. A genuine exception needs an explicit, bounded override; it is not permission to rewrite unrelated state.

<a id="core-2"></a>
### 2 Canon, Evidence and Scoped Corrections

Current explicit user corrections govern the corrected fact/rule and scope. Reconcile campaign transcripts and authoritative source facts, established active records, and the event-derived current ledger. An old transcript quantity does not undo a later valid transfer. A summary is a view of its sources.

Distinguish source-supported fact, inference, generated provisional detail, proposal and external research. An inference cannot fabricate earlier equipment, achievements, institutions, relationships, resources or chosen PC history. A generated skill/capability baseline states rationale and uncertainty rather than claiming observed evidence.

Maintain an audit trail of what the prior version established, why it was corrected and the new valid scope. Old wording is invalid within that scope and cannot return through another summary or module. New design remains prospective unless explicitly retconned.

Use §99 to distinguish invalid proposals, erroneous representations, later institutional reversals and actual-history retcons. Correct a false recorded payment without inventing an in-world refund; preserve a payment that actually occurred despite a later loss of entitlement. Facts and rule authority are distinct from actor knowledge.

<a id="core-3"></a>
### 3 Campaign Isolation

Campaigns share mechanics without sharing lore. Names, vocabulary, organizations, technologies, species, cosmology, powers and historical events stay within their own campaign unless explicitly imported.

Maintain a vocabulary/source register of approved terminology, established capabilities, forbidden or corrected concepts, reserved names and tone boundaries. A familiar word or a selected content template does not establish a setting fact.

Generalize the causal mechanism when reusable. Retain the premise-specific mechanism in its module: exposure can be Core-owned while a particular temporal hazard remains theme-owned; an equipment dependency can be Core-owned while a neural interface remains setting-specific.

<a id="core-4"></a>
### 4 Player Agency

The player controls their character's dialogue, thoughts, emotions, motives, voluntary movement, attacks, purchases, political choices, assent and follow-up actions. Resolve only declared actions, supported autonomous reactions and genuine involuntary effects.

An action contract can authorize a bounded sequence, conditional response, spending cap, duration or best effort. Resolve within that authorization; return control at the next material choice outside it. A Mixed result cannot invent the player's agreement, extra purchase, new route, additional day or chosen retreat. Offering terms is different from accepting them.

The runner controls the world and other actors under their actual goals, knowledge, capabilities, resources and institutions. NPCs can refuse, help, deceive, delegate, renegotiate or breach obligations when supported. Their actions cannot choose the protagonist's voluntary response.

A genuine involuntary mechanism must be enabled and explicitly scoped. Injury, restraint, force or another supported effect can restrict feasible options; do not narrate a voluntary surrender or emotional response as its automatic result. An extraordinary agency exception is governed by §112 and the campaign's explicit rule.

Player control is retained across abstraction, strategic orders, downtime, succession and content generation. World generation does not fill in the protagonist's chosen history or motives.

<a id="core-5"></a>
### 5 Core Resolution Loop and Action Contract

**Declaration → feasibility → execution → effect → exposure → reaction → state update → player control.** These are questions and processing stages, not mandatory separate rolls.

Before consequential resolution record actor, objective, method, target/area, duration or stopping condition, commitments, resources and limits, feasible effect, known risks, selected adapter and Mixed branch. Publicly state what the character can understand; preserve hidden facts.

1. **Feasibility:** check capacity, method access, position, means, target susceptibility and actual prerequisites. Legal prohibition alone does not make an action physically impossible; lack of required institutional approval can prevent a legitimate appointment, allocation or authorized service.
2. **Execution:** routine qualified activity is automatic when conditions support it. Check only meaningful consequential uncertainty.
3. **Effect:** successful execution changes only the agreed target and scope. Accuracy, penetration, purification, repair and permission are distinct mechanisms.
4. **Exposure:** process threats and costs that actually operate during the attempt, including on success.

An attempt consumes only actual authorized activity and expenditure. Explain obvious impossibility before committing a misunderstood declaration. For insufficient stock or time, present the feasible limit; do not silently choose a different action, smaller target or additional purchase for the player. A declaration authorizing a bounded best effort can resolve within that bound.

Extended activity is divided only at causal interruptions, not every message. Duration and commitments use §§10–11. Overlapping independent actors can act concurrently; an extended player action does not freeze everyone else.

#### Effect contract

Specify valid targets, reach/geometry, relevant effect/protection channels, magnitude/capacity, persistence, condition changes and termination. Follow the selected effect model consistently through execution, target contact/access, protection, residual effect and state change. Skill cannot repair a severed dependency, create an absent tool, penetrate an impervious layer or identify inaccessible information.

Zero relevant protection means no reduction **when the selected profile explicitly defines zero as absence**. Unknown protection is unknown. A stopped primary channel stays stopped; placement or vulnerability cannot reactivate it. A distinct secondary channel requires its own declared mechanism and exposure, not an improvised damage bonus.

For one emitted area effect, resolve shared execution once. Apply actual geometry, protection and resistance separately to affected targets or homogeneous cohorts through the chosen adapter. Do not reroll whether the same emission exists for every target, duplicate its cost or include people outside its reach. Independent target responses may remain genuinely independent under that adapter.

Repeated unchanged checks do not generate unlimited attempts or fresh contents. New method, access, evidence or separately authorized effort can matter. A search does not create what it discovers (§104).

#### Causal termination of effect channels

Resolve effect through the selected model's actual causal channels. Where that model establishes that a channel is blocked, terminated, or has no transmitted effect, later placement, vulnerability, skill, margin, or other downstream modifiers cannot recreate an effect through that channel. A separately supported transferred or secondary effect is resolved through its own mechanism, target, protection, and condition consequences. Do not count the same input twice across channels.

The selected adapter defines what its variables represent and when a channel ends. A numerical zero alone does not universally mean termination: an ordinal profile value, native zero rating, threshold, or rounded measurement may have another defined meaning. If a method bypasses protection, establish that method and change the relevant protection/contact stage; do not revive an already terminated result by adding a later bonus.

Terminating a source or transmission prevents further effect through that channel under its defined mechanism. It does not erase an existing condition, accumulated burden, or already initiated downstream process. Those retain their own persistence, recovery, and termination requirements.

#### Optional capability stages — CW-SSN-01

When a real capability requires distinct operations, declare only its relevant stages: access, preparation, commitment, activation, delivery, effect and sustain/terminate. These are conceptual boundaries, not seven mandatory actions or rolls. Each stage states trigger, prerequisites, initiating/controller authority, actual cost timing, distinct uncertainty identity, supported outcome, credible failure, continuation and termination.

Resolve dependencies before their consumers. Reuse a retained outcome when two labels refer to the same uncertainty; separate activation and delivery checks occur only when they represent different consequential uncertainties. A stage's successful execution establishes only its supported result, not every later stage. Prior committed costs stay spent on later failure unless the enabled mechanism explicitly refunds them. Failed prerequisites stop dependent stages; they do not manufacture unrelated harm or new voluntary actions.

Sustain uses actual means, time, resources and declared interruption rules. One activation/emission can affect several eligible targets without repeating its initial cost or existence roll. Actual target-specific contact/protection/responses remain distinct under the selected adapter. SSN's molding dice, d20 confirmation, rank costs and upkeep remain native implementations.

<a id="core-6"></a>
### 6 Default d100 Reference Adapter

Campaign-specific dice systems override this default. New simulation campaigns without an established mechanic use d100.

Roll a uniform integer from 1 through 100. Adjusted result = raw roll + net modifier. Never clamp the adjusted result.

| Adjusted result | Outcome | Default interpretation |
|---|---|---|
| 60 or greater | Success | Achieve the agreed feasible effect |
| 30 through 59 | Mixed | Partial effect or success with an established cost |
| 29 or less | Failure | Intended effect is not achieved; apply credible consequences |

Negative results are failures. Results above 100 remain successes. Natural 1 and natural 100 carry no universal fumble, miracle, or automatic outcome.

Before rolling, select the mixed-result branch when it matters: reduced effect, additional time, additional resources, or exposure to an existing threat. If additional expenditure or continued action requires a fresh player decision, offer it after the roll rather than silently spending or acting for the player. Costs already inherent in the declared action apply regardless of result.

Use margins for quality only within the agreed effect ceiling. A result of 90 does not allow an extra attack, invent penetration, complete unrelated work, or resolve the rest of a battle. Further benefit must be a plausible improvement to the same action, such as better placement or less wastage.

#### Competence and difficulty

The reference check is a trained actor attempting a standard consequential task. Routine professional activity remains automatic when unopposed and adequately resourced.

| Competence | Rating | Modifier |
|---|---:|---:|
| Untrained | 0 | -20 |
| Familiar | 1 | -10 |
| Trained | 2 | 0 |
| Experienced | 3 | +10 |
| Expert | 4 | +20 |
| Master | 5 | +30 |

| Task difficulty for a trained actor | Modifier |
|---|---:|
| Favorable but still uncertain | +20 |
| Straightforward under pressure | +10 |
| Standard consequential task | 0 |
| Difficult | -10 |
| Very difficult | -20 |
| Exceptional | -30 |

A competence rating is specific to a discipline. Expertise with medicine does not grant engineering expertise. Innate capacity normally sets feasibility and sustainable output. Where it independently affects execution, use the circumstance scale below; do not count a strength advantage both as a skill bonus and an identical physical advantage.

Net modifier = competence + difficulty + independent circumstances. Slight, meaningful, major, and decisive circumstances are worth 5, 10, 20, and 30 respectively, with the appropriate sign.

Record each material cause once. Low visibility cannot be charged separately as darkness, poor sight, obscured target, and difficult aiming when these describe the same obstacle. Separate causes may stack. A broken sight and a moving target are independent. Armor normally affects effect, not hit probability.

Net modifiers outside -40 to +40 require a feasibility and uncertainty review, not an automatic cap. Retain the calculated modifier if meaningful uncertainty remains. Do not reroll until success without changed circumstances; continuing work may consume time, but an unchanged failed approach does not generate free independent chances.

#### Probability calibration

| Net modifier | Failure | Mixed | Success |
|---:|---:|---:|---:|
| -40 | 69% | 30% | 1% |
| -20 | 49% | 30% | 21% |
| 0 | 29% | 30% | 41% |
| +10 | 19% | 30% | 51% |
| +20 | 9% | 30% | 61% |
| +30 | 0% | 29% | 71% |
| +40 | 0% | 19% | 81% |

These probabilities preserve the baseline thresholds. At +30 an outright failure is impossible, although costly or incomplete execution remains possible. This is an explicit property of the default engine, not a hidden minimum failure chance. Campaigns wanting a different competence curve must revise and test the thresholds or competence mapping.

#### Active opposition

Use one roll per contested objective by default. Add 10 × (2 minus the opposing competence rating) as the opposition modifier; the acting character's competence modifier still applies. Task difficulty covers independent complexity, not the opponent's skill a second time. NPC competence uses the same ladder.

Two trained opponents have no relative skill adjustment. An expert acting against a trained opponent gains +20; a trained actor facing an expert takes -20. On success the acting side obtains the feasible objective. Mixed produces the predeclared partial or costly result. Failure preserves the defense or permits an established countereffect. Failure does not automatically grant the defender a free attack.

This execution adapter is role-asymmetric: Success, Mixed and Failure describe an acting objective and a defense. It is not a fair binary tiebreaker for who acts first. Use §47's ordering adapter for an unresolved priority tie. A race may instead compare actual progress over the same interval. Do not roll once for each side against the same contested outcome. Independent actions occur at their causal times; one success does not automatically cancel the other.

#### Adapter scope

This is the existing selectable reference adapter for consequential uncertainty. It is not a mandatory universal skill, attribute or probability model. Retain campaign-established dice and scopes. The listed competence/difficulty/circumstance values are provisional design defaults until calibrated for declared tasks. Numerical consistency establishes their exact outcome curve only.

Before selecting a contested or priority interpretation, identify whether roles are genuinely asymmetric or interchangeable. The acting-objective adapter does not become a fair race, election, scoring model or initiative rule by relabeling Success/Failure. COMP (§123) and §47 supply the required selection and symmetry gates.

<a id="core-7"></a>
### 7 Advantage and Disadvantage

Some campaigns already use d20 Advantage/Disadvantage.

For the d100 engine, use circumstance modifiers instead unless the campaign explicitly uses roll-twice mechanics.

Existing campaigns retain their established systems. An established d20 campaign continues under its selected structure until an explicit prospective conversion.

<a id="core-8"></a>
### 8 Failure and Mixed Results

Failure can arise from opposition, timing, means, position, incomplete knowledge or condition. An effect limit is not execution failure: a projectile can hit and be stopped; a pump can run while delivering unsafe water.

Mixed uses the branch fixed for the attempt: partial effect, additional time, additional resource, worse position or exposure to an existing threat. It cannot invent unrelated catastrophe, a free counterattack or a new player action. Apply only already committed costs automatically. An offer requiring more time, resources or continued action beyond authorization returns control.

Known costs remain on success. Firing expends ammunition, a profiled activation creates heat, travel consumes time, and structural overload can impose a declared burden even when the objective succeeds. Failure consumes only actually used, spoiled or exposed inputs—not every reserved material by default.

Outcome quality is bounded by feasible effect and credible consequences. Further benefit concerns the same action: placement, efficiency, precision or useful evidence. It grants no extra attack, unsolicited follow-up or unrelated project progress.

<a id="core-9"></a>
### 9 Consequence Scale

Consequences match the action's actual exposure and scale.

| Action scale | Typical consequence |
|---|---|
| Minor | Delay, noise, wasted resources |
| Tactical | Lost position, wounds, damaged equipment |
| Operational | Casualties, failed objective, major supply loss |
| Strategic | Campaign defeat, loss of a city, political collapse |

One minor failed check does not ordinarily cause strategic catastrophe. Repeated failures can accumulate into one through traceable events. A small action may have large consequences only where an established dependency makes that credible; identify foreseeable stakes before resolution.

A low roll can expose an existing lethal danger. It cannot invent one. Margins can refine severity only within the consequence range established for the attempt.

## Time, Records and Actor State

<a id="core-10"></a>
### 10 Time, Commitments and Concurrency

One campaign clock governs every actor, domain, route and task. Time advances through authorized activity or a selected standing simulation policy, never because a reply, review or document is produced.

A commitment records actor/asset, task and objective, actual location, start/end or stop condition, capacity/attention used, compatible overlaps, action-instruction and mandate references, endpoint semantics, interruptibility and reporting triggers. Incompatible full-capacity work cannot share the same actor, equipment or interval. Compatible activities can overlap only under an established method; reduced rates must identify their interference.

Accrual uses start-inclusive/end-exclusive spans by default. Time-limited instructions, mandates, entry windows and submission deadlines separately identify whether the limit constrains starting, continuing, completing, receiving or submitting, and whether the endpoint is included. Missing outcome-changing terms are resolved before the dependent act. Work earned before a deadline remains physically earned; its institutional/scoring validity follows the actual terms.

Physical execution, institutional validity, issued instructions and received/understood instructions are separate. A distant revocation does not inform its recipient instantaneously. An NPC may continue physical work from received instructions while authority has already expired; actual execution and its legal consequences are resolved separately. Never invent the protagonist's choice to continue or disobey.

Use one retained resolution ID, sampled outcome, authorized span, planned rate and realized work per unchanged uncertainty. Review cadence, save/load, narration and scale changes preserve it. A genuinely material change closes the former span prospectively and creates only the newly justified contract; completed work and actual costs persist.

Bound progress by remaining work, real inputs, current qualifications/availability, location/access and useful parallel capacity (§73). Qualified substitutes can cover an absence without increasing an unchanged workstation cap. Stop stage-specific labor and consumption at its actual completion, interruption or authorization limit. New PC commitments return control.

<a id="core-11"></a>
### 11 Event Frontier, Scheduling and Atomic Processing

An event contains `event_id, campaign_id, cause/parent_id, causal_time, producer/coordinator, write_set[(owner, refs, expected_pre_state, proposed_changes)], action_instruction_refs, institutional_authority, information_visibility, dependencies, status`. Each participating owner validates its part; the coordinator commits the whole related transaction or none. A payment can therefore transfer K-STOCK funds and settle an ECO claim without giving either a duplicate ledger or arbitrary ownership of the other's facts. Single-owner events use a one-item write set. Scheduled events additionally identify prerequisites, reservations, cancellation and uncertainty. Transaction identity is scoped by campaign and event ID. Reject a mismatched campaign or state reference before looking up a replay or reading/writing that state. Receiving systems subscribe by scoped event ID and keep a processed marker; subscribers derive their own consequences, not the original debit again.

For an authorized advance toward target time T:

1. Find the earliest relevant completion, prerequisite exhaustion, threshold, arrival, deadline, report receipt, or meaningful decision. Recompute this frontier whenever execution schedules an earlier event; a requested long advance cannot skip a newly scheduled acceptance or other causal event.
2. Advance unfinished activities only over their unprocessed usable intervals, using start-inclusive/end-exclusive spans for accrual. Preserve fractions and retained uncertainty. Complete work earned before a boundary once at that boundary; apply separate legal/contest endpoint terms. Presentation review frequency is not a process update interval (§§19/109).
3. Validate campaign/reference scope and classify each due event by scoped identity before considering prerequisites, allocations or other new effects. Same applied ID and payload is a no-op; reused ID with different content is a conflict. Reject conflicts without mutation. Rejected new events leave neither partial writes nor an applied marker. A replay never reopens a completed allocation decision.
4. Establish the pre-event state. Order causal dependencies first. Independent simultaneous effects must commute; evaluate their effects consistently from that state. Contending requests are not independent. An input list has priority only when it explicitly represents the adopted policy.
5. For shared scarce commitments, apply existing reservations/allocation policy before execution. Conflicting proposed allocations require a feasible allocation decision; “simultaneous” never licenses overdraw. If no authorized tie-break exists, preserve the unresolved allocation and defer only the dependent competing commitment. Independent hazards, actual losses and other authorized work continue. Do not invent a protagonist choice or let each claimant reserve the entire surviving pool.
6. Validate all participating owners and atomically commit the related write set: nonnegative quantities, unit compatibility, actual location/access, institutional/claimed authority distinctions, labor/asset exclusivity and ownership. Any rejected payment/transfer leaves funds, claims, locations and applied markers unchanged. Physical involuntary loss is reconciled with commitments under §12, rather than rejected because a reservation would become unbacked. A valid theft can change custody without valid title; validation does not make illegal acts physically impossible.
7. Recompute affected capabilities, queues and forecasts; schedule only real downstream events. An exhausted input closes the productive contribution and waits for a state change, preventing endless zero-time exhaustion events.
8. Deliver observations/reports at their actual availability times. Return control at a new meaningful player decision; otherwise continue within existing authorization.

Checkpoint the pending queue, causal dependencies, allocation/shortfall policy, unresolved decisions, retained outcomes, processed spans, transaction payload identity and recipient knowledge alongside quantities. A stock-only save cannot reconstruct causal processing.

**Simultaneous transaction epoch rule (R2 clarification):** Event IDs, queue insertion order, presentation order, alphabetical party names and chronological loop iteration have no default priority for allocating scarce stocks, money, labor or exclusive custody. Classify the complete due epoch, identify read/write dependencies and evaluate supported simultaneous effects from one valid pre-event frontier. An epoch contains one atomic causal transaction or multiple proven independent/commutative transactions. If a group competes for the same finite means and no authorized allocation policy exists, keep that contested group unresolved without partially executing its members; independent due events may still proceed. Store the decision/policy, affected event IDs and previously settled time spans. Same-time command issue and its receipt require a causal sequence or subtime/phase supported by the communication profile; sorting their event IDs does not establish causality.

A subscriber may create a later consequence: an injury creates a care request, a missed shift changes production, an unpaid invoice changes a cash forecast. Each has its own cause and time. No universal ordering such as “politics before economy” can override causality.

#### Thresholds and execution spans

Each time-dependent process states its update law, units, causal interval or continuous interpretation, thresholds and last processed spans/boundaries. Discrete transitions execute at declared causal boundaries; continuous processes use a consistent event/solver method. Approximation requires a stated, justified tolerance and convergence checks. Narrative review frequency is not a biological, financial, aging or ecological update interval.

Locate exhaustion or completion before extrapolating a process beyond available inputs. Do not obtain negative stock and clamp it after infeasible work. Split at a real threshold, arrival, mode change, interruption or decision. An exhausted process waits for a state change; it does not schedule an endless zero-time exhaustion event. Actual scheduled review/decision events can change future policy and remain in the queue.

The event coordinator stores the canonical payload or a verified recoverable reference, scoped identity and validation state. A payload digest can assist comparison; it cannot recover missing event content or hidden state. Concurrent invalid proposals are rejected as proposals. A real involuntary loss commits the supported physical event and reconciles backing; reservation guarantees cannot make damage or theft impossible.

#### R3 proposed frontier refinement — dependent activity and aggregated capacity

An input, assessed claim, assignment, signed mandate, arrived shipment, credential, product or completed-job evidence originating **at** a frontier is not automatically available as a pre-existing prerequisite at that frontier. When a selected process truly allows instantaneous chains, it must provide an explicit causal micro-order or atomic transaction contract; event IDs do not establish one. Same-time independent transactions whose owner-qualified claims commute may proceed. Conflicting requests draw against available physical resources and valid prior reservations, never against expected output from unfinished work. Validate concurrent site staffing with the **sum of all overlapping worker demands over every affected interval**, not merely pairwise job comparisons. A blocked contested subgraph does not authorize freezing unrelated world activity; a reference runtime that cannot isolate the subgraph must mark that as an implementation limitation.

An assignment is effective at its authorized start or later applicable notice, never retroactively creates completed duty. Correct an erroneous past record through an explicit correction/evidence procedure (§§91/98), without manufacturing prior work or resource rights.


#### 11.R4 — Qualified selective event graph and unresolved requests (PROPOSED)

**Purpose and ownership.** The same §11 coordinator remains K-TIME's authoritative event/scheduling service. It does not create a new state owner. An event proposal has immutable scoped request identity and full payload, an actual occurrence/effective time (if committed), prerequisite and qualified read/write/capacity sets, a declared resource/authority scope, and an owner-validation contract. Graph edges connect requests sharing a noncommutative owner record, a finite capacity over overlapping intervals, a resource eligible pool, a prerequisite/result dependency, or an indivisible multi-owner transaction. An unclassified event lacks proof of independence: place it behind a conservative compatibility barrier and seek its owning interface rather than optimistically proceeding.

**Selective frontier procedure.** (1) Freeze the pre-frontier snapshot, gather all due proposals and retrieve their stable payloads. (2) Compute and qualify their owner read/write, causal and aggregate capacity footprints, including indirect subscriptions and underlying shared pools. (3) Form transitive contention/dependency components; a component may include three or more claimants. (4) For each component, evaluate authority and physical feasibility against the frozen pre-state and all claims within the component. Prove distinct components commute or conservatively join them. (5) Atomically commit qualified independent components, with one event identity and only its real writes per physical effect. (6) Preserve invalid, contested and awaiting-prerequisite proposals as **unexecuted** requests with classification, reason, references and required deciding action. They create no paid balances, stock receipts, work, casualties, or applied-event markers. (7) Continue other authorized time-dependent activity and future frontiers. An unresolved prior request does not freeze unrelated work, but cannot be silently applied later at its old time. (8) If a competent subsequent decision supplies an allocation, execute its newly authorized prospective events at their *actual* decision/operation times, revalidating current resources, authority and feasibility; explicitly dispose of remaining requests. No event-ID or application order supplies authority.

**Boundary conditions.** Reservations, already-in-progress work and involuntary hazards are not indistinguishable future requests. A supported hazard must still commit its physical loss despite commitments, then reconcile shortfall once (§12). Causal dependencies can run at selected explicit substages only when a compatible domain contract defines them. Exclusive record collisions and shared stock/cash/site/worker capacity must include all related demands. Independent transactions can be certified by owner-qualified footprints; mere differently spelled resource names or lack of known relation is not sufficient proof. The reference R4 key-footprint graph is a deliberately limited implementation requiring external model qualifications. A rejected proposal must be distinguished from an unresolved political/allocation dispute in a full runtime.

**Minimal recoverable record proposals:** `EventProposal(id,scope,proposed_at,earliest_effective_at,payload_digest,payload_ref,prerequisite_refs,owner_read_set,owner_write_set,capacity_interval_claims,authority_ref,status)`; `ContentionComponent(id,frontier,request_ids,shared_basis,owner_validation,allocation_policy_or_pending,decision_ref,settled_event_ids)`; `DeferredRequest(id,original_frontier,reason,status,deciding_authority,validity_window,decision_ref,outcome_ref)`; `CoverageSpan(source_effect_id,contributor_scope,measure,interval,quantity,units,evidence,exclusive_coverage)`.

**Status constraints:** Request submission ≠ execution; rejection ≠ occurrence; disputed reservation ≠ stock consumption; decision issuance ≠ material delivery. Preserve original request IDs against resubmission regardless of decision. A later authorized corrective action gets a new ID and effect time. Missing authority evidence remains missing rather than inferred from a nonempty text reference.

#### 11.R5 — Involuntary occurrence, reserved-stock collisions and causal stage proof (PROPOSED)

A supported physical occurrence is not an allocatable promise. A fire, flood, theft, spoilage event or other actual loss must not be denied solely because a party reserved the affected stock or a simultaneous administrative request lacks consent. First determine **what physically occurred, where, when, and from which source**, then settle the resulting material decrease exactly once under K-STOCK with K-TIME occurrence provenance. The information reporting that occurrence, and the later time someone learns of it, are separate K-INFO events. An unsupported or contradictory quantity is an evidence/feasibility issue, not permission to infer or fabricate inventory.

**Same-time ambiguity.** Where a loss and a physical withdrawal touch the same stock at a recorded instant, neither event ID nor the narrative order of reporting supplies which occurred first. Commit independently supported effects and hold the dependent withdrawal as an *unexecuted causal-order question*, unless authoritative subevent order, causal stage or physical evidence explicitly resolves it. Nothing here creates a universal rule that hazards always precede an otherwise established earlier loading operation. A later resolution may produce only supported prospective or duly timestamped events; no backdating.

**Contract:** preserve hazard occurrence ID, scoped physical stock, quantity/units, evidence/cause references and actual state write. After committing the loss, reconcile reservations, claims, institutional obligations, work prerequisites, capacity and any pending shipments against the **remaining physical stock** without first-writer preference. This procedure does not permit a hazard to create an unrelated injury, consume supplies not physically used, or retroactively cancel valid previously completed work. The R5 reference exercises only selected stationary stock and qualified same-time deferrals; it does not simulate hazards, inspect evidence, or solve temporal ambiguity.

#### 11.R6 — Verified work intervals, shocks and future continuation (PROPOSED)

A process need not wait until its planned end to commit every actual effect. Under a **selected divisible-work protocol** (§109), work may settle at certified intermediate frontiers; consumed stock and accepted output then become historical facts and must not be reprocessed at final completion. Every milestone has an event ID, actual interval, selected model/source and applicability envelope, qualified people/capacity, materials physically used, accepted output and evidence/observation lineage. Elapsed time, a shift roster or a projected production rate alone is not proof that an intermediate product exists.

When an involuntary loss intervenes, historical certified milestones survive. The job's remaining input reservation, incomplete work, unassessed intervals and contractual obligations are recomputed at the actual loss frontier. A later replacement delivery is not a retroactive completion: further work requires new eligible material, people, time, feasible production mode and any fresh authorization. Distinct causal stages may occur at the same displayed time only when a selected rule and provenance establish their order; event ID and tool invocation order are not general priority policies.

**Reference limitation:** R6 implements attested hourly synthetic milestones as directly staged atomic events. Its new operations are **not** registered with R4's general scheduler footprints; attempting to schedule them must fail safely until a certified integration exists.

<a id="core-12"></a>
#### 11.R7 — Qualified selected work frontiers, physical occurrences and isolation (PROPOSED)

A selectable runtime adapter SHALL publish the pre-frontier read/write and scarce-capacity footprint of each event operation. Tracked production start, incremental milestone, disruption settlement, authorized continuation, finalization, inspection, physical loss and material disposition SHALL be dispatched through their actual record-owning procedure; routing an unfamiliar operation through a generic legacy dispatcher is prohibited. Unknown or incomplete footprints create a conservative dependency barrier rather than permission to commit.

Each occurrence frontier SHALL use one pre-event snapshot for dependency partition, and SHALL commit only after the entire frontier's evidence and physical consistency checks succeed. Independent components may complete notwithstanding an unresolved competing component. A shared-source component requiring allocation, authority, or physical ordering stays unexecuted and source-retained; event IDs never select a winner. A supported physical loss is an occurrence, not a competing budget application: recognize actual loss once and retain same-instant work claims as causally unresolved absent an evidential ordering. If aggregate claimed physical losses exceed measured stock, reject the entire inconsistent frontier pending evidence reconciliation. A deferred claim is not a consumed resource or a completed work milestone.

**R7 implementation boundary:** The reference scheduler has manual, fixture-bounded footprints, conservative same-time contention and same-implementation replay. Neither independent transitive dependency certification nor full authority/observation-time ordering is established. Administrative timestamps alone do not authorize a substage.

### 12 Persistent Records, Accounting and Commitments

Use Appendix A's single-owner and minimum-record contracts. A persistent fact is known, estimated with source/bounds, unknown, or not applicable. Unknown is never zero, free, unlimited or absent. IDs retain campaign scope and survive display-name changes.

Keep physical quantity, task usability, ownership, custody, access, assignment, reservation backing and contractual obligation distinct. A view may combine these facts without becoming another ledger. Exact values are used when they affect decisions; aggregates must preserve totals and relevant differences.

For each stock and interval, use opening quantity + actual receipts + accepted production − actual consumption − dispatched quantity − physical losses. Account for transformation outputs, waste and source inputs explicitly. Reservations reduce free availability, not physical stock. Assess backing against stock actually eligible by specification, owner/access and timing. Sum backed commitments only over nonoverlapping allocations: one surviving unit cannot back incompatible claims twice. Commit destruction, contamination, expiry, seizure or access loss even when reservations become unbacked. Destroyed quantity is a loss; contamination changes usability; seizure changes custody/access as actually occurred; temporary access loss does not destroy stock. Return of access is not a second receipt.

Apply specific-lot effects first, then the established shortfall policy for shared eligible pools. Keep physical stock, usable accessible stock, backed reservation, unbacked commitment and contractual obligation distinct. With no deciding policy, retain the surviving pool once and mark the contested backing allocation unresolved; do not assign invented priority. Usable free stock cannot be negative. Releasing or cancelling a reservation is not consumption and does not by itself discharge the associated obligation. For example, 10 units with one reservation of 8 and a loss of 5 leaves physical 5, backed 5, unbacked 3 and obligation 8. These values are a synthetic accounting example.

Transit is a location. Reports, forecasts and invoices do not deliver goods.

ECO claims reference one obligation with debtor, creditor, unit, basis, amount accrued, amount settled, adjustments, due conditions and dispute status. Receivable/payable panels are views of that same claim. Payment couples transfer of actual ownership/custody under its terms with settlement of the named claim. Partial payment leaves a balance. Arrears is a state of the outstanding amount, not a second debt. Money creation, credit issuance, debt write-off and currency conversion require explicit institutional mechanisms; “cash cannot be negative” does not prohibit a separately recorded loan or liability.

A tax assessment, court award, prize and promised wage can each create claims; none is cash until delivered. A confiscation, theft, escrow deposit, loan of equipment and sale have different custody/title effects. Record them rather than treating every movement as purchase.

Corrections preserve the distinction between a proposed transaction, a completed physical transfer and its present institutional justification. Reject an invalid proposal before mutation. A later award reversal, contract cancellation or finding does not erase settled payments, actual use or elapsed time. Record the correction and create a compensating transfer/recovery or replacement obligation only where the governing terms and authority support it. Recovery is still a claim until actual return; paying a replacement recipient needs actual funds. Use new event IDs linked to the originals, never a changed payload under an applied ID. No universal clawback right is implied. Correcting an erroneous historical record of what actually occurred requires evidence, scoped authority and an auditable amendment: a falsely recorded payment that never happened is repaired as a representation, without inventing an in-world refund. Changing actual resolved history is a distinct explicitly authorized retcon, not an ordinary record correction or migration.

<a id="core-13"></a>
### 13 Context Sensitive State Panels

Do not dump the entire ledger every response.

Display only the state relevant to the present situation.

Combat panel Position, wounds, ammunition, suppression, immediate threats. Vehicle/Mech panel Damage, heat, power, weapons, ammo, mobility.

Military command panel Unit strength, casualties, morale, supply, current orders, communications.

Community panel Population, food, power, security, morale, active projects.

Life-sim panel Date, money, employment, home, relationships, commitments.

Panels appear primarily when:

- something materially changes;
- the player requests status;
- a planning decision requires the information.

<a id="core-14"></a>
### 14 Actor Capability

Core is attribute-, class-, species- and technology-agnostic. A capability assessment distinguishes:

| Dimension | Question |
|---|---|
| Capacity | Can body, mind or mechanism supply the required force, endurance, precision or processing? |
| Discipline | Can the actor execute the learned method? |
| Experience | In what relevant conditions has that competence been exercised? |
| Condition | What functions are currently restricted by injury, fatigue, faults or exposure? |
| Means | Are tools, workspace, materials and qualified help available? |
| Knowledge | Does the actor know the facts/method needed now? |
| Authorization | Are institutional decisions, services or use permissions valid? |

The selected profile defines actual attributes, anatomy, senses, movement, physiological/mechanical needs and extraordinary capabilities. Ancestry/body, culture, background and profession are separate: anatomy does not grant learned beliefs or weapon skill.

Absolute competence can gate method access and effect even when equal relative ratings cancel in a contest. Record required training, understood technique and means before rolling. A difficult roll cannot invent advanced knowledge. The fantasy one-tier-above technique penalty and its attribute formulas remain that profile's values, not universal Core defaults.

Animals and other living actors have actual motives, senses, needs and care. Constructed bodies use component profiles; living animals do not become vehicle components. A threat, monster or important NPC gains no extra actions or immunity solely from narrative importance.

Claims, qualifications, institutionally recognized competence and demonstrated ability are separate evidence. Background-supported secondary skills may be assigned as **provisional**, with rationale, before they matter; do not label them observed or retroactively alter outcomes. Advancement uses §96.

#### Ordinary functions without compulsory measurements

An established entity profile supports its ordinary functions under established conditions. Missing numerical measurements do not by themselves establish incapacity. Use supported profile functions, demonstrated competence, actual equipment, and known restrictions to resolve routine activity without inventing attributes merely to permit it.

Assess or provisionally bound only the uncertainty material to the present task. Ordinary capability does not establish exceptional strength, specialist knowledge, an absent function, unprovided equipment, or independence from required inputs. A costly or dangerous assessment is an actual task with its own opportunity, risks, time, and agency boundary.

<a id="core-15"></a>
### 15 Competency Ladder

Use the following discipline-specific ladder where no campaign rating system exists.

| Rating | Competence | Default execution modifier |
|---:|---|---:|
| 0 | Untrained | -20 |
| 1 | Familiar | -10 |
| 2 | Trained | 0 |
| 3 | Experienced | +10 |
| 4 | Expert | +20 |
| 5 | Master | +30 |

Professional competence generally begins at 2. The values are the same mapping used in section 6, not an additional bonus. Other attributes and campaign systems retain their established meaning. Progression requires relevant practice and demonstrated capability, as detailed in section 96.

#### Functional scope within competence

A capability or qualification applies to its established functions, methods, context, and relevant limitations. Where a broad label hides a consequential difference, retain the necessary functional distinctions without manufacturing a separate statistic for every subtask.

For language, comprehension, expression, reading, and writing may differ by language, medium, register, or specialist vocabulary. Fluency in one function does not automatically establish the others. Familiarity with repeated instructions need not grant general literacy or broad technical understanding. Equivalent scope distinctions apply to other disciplines where demonstrated evidence supports them.

Routine familiar communication proceeds without a roll while consuming any actual time or resources. Receipt does not itself establish comprehension. Resolve only consequential uncertainty; do not invent arbitrary misunderstanding to force a complication.

Resolve the task through all functions materially required. Do not collapse them into an invented average or apply multiple penalties for the same limitation. A combined capability check, an established limiting-stage rule, or separate genuinely uncertain stages may be used under the selected resolution adapter; do not add redundant rolls. Existing supported competence need not be replaced with detailed subratings unless a real decision requires the distinction.

<a id="core-16"></a>
### 16 Progression

Progression operates on multiple axes.

| Axis | Examples |
|---|---|
| Personal | Attributes, skills, health |
| Professional | Qualifications, promotion |
| Social | Contacts, reputation |
| Material | Money, equipment, property |
| Institutional | Command, clearance, title |
| Strategic | Unit, business, settlement |
| Historical | Family legacy, doctrine |

A character need not gain supernatural power to progress. A veteran becoming more influential, better connected, or more technically competent is valid advancement. Do not award unrelated skills because a character gained a level. Section 96 defines training records and review.

<a id="core-17"></a>
### 17 Conditions, Injury, Treatment and Recovery

Core owns condition identity and persistent function. An adopted effect/physiology profile determines how injury occurs, prognosis, treatment efficacy and recovery rates. Use one compatible effect chain; do not combine points, severity steps and Threat formulas by name alone.

Each condition records affected actor/component/function, true state if supported, assessed state and assessor, onset/source event, severity, restrictions, modifiers if adopted, deterioration trigger, recovery requirements, linked plan and next review. Unknown severity remains unknown. Naming a condition does not make every actor aware of it.

The selected condition profile supplies functional restrictions and any modifier mapping. Apply the worst overlapping modifier for the same function without discarding later physical harm. Additional restrictions require actual distinct mechanisms. An arm injury can restrict handling while suitable instruction remains possible. The optional human modifier bands are specified in Appendix D; they are provisional game values, not evidence of live playtesting or universal physiology.

#### Treatment objectives

Separate assessment, bleeding control, stabilization, cleaning, immobilization, closure/extraction, pain management, disease/infection treatment, definitive repair and rehabilitation as applicable. One successful action completes only its declared feasible objective. Routine trained care with suitable means can be automatic; it still uses actual supplies, attention and time.

A recovery plan names condition, objective, provider, required means, stages, practical limits, elapsed qualifying care, review criteria and interruption/deterioration events. Other modules read that plan's resulting function; they do not add parallel healing counters or repeat a processed care day.

Useful phases are **Acute → Stabilized → Healing → Rehabilitation → Resolved/Lasting impairment**, where the condition supports them. Stabilization controls a specified immediate deterioration; it does not guarantee structural repair, remove every risk or restore duty fitness. Stages can overlap or differ by condition, rather than imposing one universal sequence.

Normal recovery progresses automatically when the selected requirements are met. Roll for actual consequential uncertainty, not every healthy body's daily progress. Rest can relieve exertion without repairing a fracture; restored machinery does not biologically heal. Extraordinary healing declares the exact state changed and any remaining impairment, cost or dependency.

A dangerous condition requires a supported deterioration mechanism and next threshold/review. Numerical examples are game abstractions, not real medical guidance. Do not infer death time from a poor execution roll. Care, fitness certification, duty assignment and household consequences are separate decisions and facts.

#### Repeated harm and condition history

Modifier selection and physical condition accumulation are separate procedures. Using the worst applicable modifier for a function does not discard later damaging events. For each new event, identify the affected entity, structure/component, mechanism, actual contact/exposure, and current protection. Determine whether it damages an intact part, worsens an existing condition, or contributes to an ongoing burden shared by several sources.

Update the affected condition once, retaining its causal history; create an additional condition only where a distinct condition is supported. Recompute practical restrictions, protection, available functions, and relevant deterioration/recovery events. Count each actual damage contribution once. Reading a report, changing scale, or repeating a condition summary is not another damaging event.

Combine effects only through a supported mechanism. There is no universal conversion from a count of minor conditions into a severe condition, nor immunity to repeated harm merely because a displayed modifier has stopped increasing. The selected profile defines accumulation, thresholds, and recovery where these matter.

<a id="core-18"></a>
### 18 Fatigue, Exertion and Recovery Constraints

Fatigue is a persistent condition produced by actual activity and recovery constraints. It is distinct from injury, sleep deficit, hunger, trauma, morale and specialized interface strain. Use the established entity's physiology/mechanism and selected activity profile; machine or nonhuman actors do not automatically inherit human exertion.

Record active mode/effort, usable interval, profiled accumulation, residual fractions, thresholds, affected functions, recovery requirements and last processed spans. One interval is not charged both as ordinary and strenuous activity for the same exertion cause. Combat does not automatically count as maximum effort.

Recovery consumes actual qualifying rest/sleep and compatible provision. It does not repair unrelated injury, erase knowledge or refund expended ammunition. A deprivation forecast is not a second penalty; actual deprivation can constrain recovery through its defined mechanism.

At a limit, assess remaining feasible function and any supported further-effort exposure. An exceptional PC effort or continued march is a voluntary declaration, never a response invented by the runner. Routine NPC rest/duty changes follow their actual plans and standing authority.

The complete optional human fatigue profile and its timing are specified in Appendix D. Select one compatible cause-accounting profile; do not stack that track with another genre's load/fatigue formula for the same represented impairment. New rates or sleep qualification remain explicit calibration needs.

<a id="core-19"></a>
### 19 Hazards, Exposure and Deprivation Interfaces

A hazard profile states source, medium/area, delivery route, intensity measure, duration/dose if relevant, protection, valid targets, onset, effects, persistence/spread, detection, countermeasures, treatment and termination. Biological, thermal, chemical, electrical, radiation and speculative hazards can use this interface while retaining their cause-specific mechanisms.

Keep separate source strength, environmental presence, contact/exposure, accumulated burden when the profile requires it, detected evidence and resulting impairment. A bite can cause an injury plus biological exposure through distinct channels; the infection is not guaranteed merely because the wound exists. A toxin's dose and an ordinary physical attack's Threat are incompatible measures unless an explicit adapter defines the relation.

Process actual exposed interval, protection and route. Use a numerical accumulation only where the phenomenon and calibrated profile support it. Otherwise use causal milestones and known restrictions. A condition module emits changes to the same actor/item records; it does not create a second injury ledger.

Moving to safety ends further environmental exposure where the mechanism permits, without automatically removing retained contamination, illness, dose or existing damage. Cleaning/decontamination, treatment and repair address different states. Unseen exposure remains hidden until detection or symptoms provide evidence.

Core provides no generic dose table, disease lethality, fallout radius or contamination-removal percentage. Select an applicable profile before dependent play. A named hazard without a complete effect mechanism is an unresolved design gap, not a license to invent a catastrophe after the roll.

<a id="core-20"></a>
### 20 Inventory, Compatibility and Access

Use the stock/asset records in §12. Carried, worn, stored, mounted, issued, communal and privately owned are custody/use relationships, not duplicate inventories. Ownership, possession, assignment, access and lawful claim can differ.

Resource families are browsing categories. Actual specification controls compatibility: fuel grade, connector, dimensions, medicine identity, material quality or ammunition type. Spare parts and medicine are not universal points. Substitution needs a declared conversion or alternate method with inputs, work, output and limits (§101).

Available provision is actual usable stock/service at the relevant consumer. Promised deliveries, undiscovered supplies, planted crops and distant surplus are forecasts until production, access or movement makes them available. A resource can exist but be unknown, inaccessible, unrecoverable, untransportable or unusable (§104).

Changing a container's location moves its referenced contents, not a second copy. Sustained carry, lifting, loading, storage and transport have different constraints (§105). Equipment cannot teleport between scenes.

<a id="core-21"></a>
### 21 Equipment Condition, Configuration and Quality

Condition is **Excellent → Serviceable → Worn → Damaged → Critical → Destroyed** where that scale is selected. Worn requires service when profiled; it does not automatically penalize every use. Damaged specifies reduced function. Critical states remaining function and a supported failure trigger. Destroyed removes that function until actual replacement/reconstruction.

Physical condition, fault, operating mode, usability, configuration and quality are separate. An intact pump can be offline without power; a damaged device can retain an unaffected mode. Quality names construction/handling/reliability properties, not a universal bonus. Material properties change only the functions their mechanism supports.

Track components only when local damage or dependency matters. A damaged plate does not reduce an undamaged helmet. An integrated protective harness uses its selected construction/coverage profile; do not sum whole armor ratings because layers exist.

Field repair restores named functions with limits, not every condition. Full restoration requires actual work, inputs and any acceptance. Local stress or hit points can be retained under an adopted effect profile; describing the same event in component terms is not another deduction (§55). Maintenance uses §23; dependency propagation uses §101.

<a id="core-22"></a>
### 22 Ammunition

Track exact ammunition when individual weapon use matters. For large formations, track by:

- rounds;
- magazines;
- basic load percentage;
- ammunition class;
- supply days.

Do not invent reloads.

Do not forget expended magazines because the next scene needs action.

At individual combat scale, declare ammunition expenditure before firing and subtract actual expenditure. A short magazine permits only the remaining rounds. At unit scale, use an explicit expenditure estimate per interval for the declared fire plan, bounded by available stores. Mark estimates as estimates. Do not invent individual magazine counts when zooming back in; preserve known totals and allocate previously untracked stock conservatively as a new recorded detail.

Ammunition accounting cannot create magazines or reloads. Basic-load percentages and supply-day estimates require a stated reference quantity or consumption assumption.

<a id="core-23"></a>
### 23 Maintenance and Work Orders

Service requirements follow profiled use, storage, environment, overload or actual damage. Record due work and failure exposure; being overdue is not an automatic random breakdown every scene.

Use applicable stages: **inspect → diagnose/make safe → restore limited operation → repair/replace → test → accept/return to service**. A work order references fault/asset, target function, access, expertise, tools, parts, maximum concurrent labor, remaining work, priority, restrictions, completion criteria and next review.

Core Projects (§73) owns actual progress. A workaround has an explicit supported mode and review trigger. Removing a part updates donor function at removal; the recipient gains function only after compatibility, installation and acceptance as required. Finding or reserving a part completes none of those operations.

Mechanical completion and acceptance are separate when reliability or institutional release matters. Routine inspection/testing needs no compulsory roll. A failed test creates the supported rework/blocker, not erasure of all unrelated completed work. Queue priority changes allocation of existing staff/assets, not total capacity.

Service return uses commissioning where a wider service depends on the asset (§103). Equipment repaired in a powerless, unstaffed facility is still unable to provide its full service.

<a id="core-24"></a>
### 24 Economy, Claims and Settlement

Economics uses actual stocks, assets, time, institutions, work and delivery. ECO (§114) owns agreements, orders, claims, quotes and enterprise/market assessments; K-STOCK owns the actual monetary balance/stock representation selected by the financial model. An account panel references that representation rather than duplicating a balance.

An agreement records parties, authority, subject/specification, quantity/unit, consideration, dates, delivery/acceptance, payment, title/custody/risk transfer and dispute/cancellation terms. Track agreement, obligation, fulfillment and payment as independent axes. Prepayment, credit, partial delivery and installment terms do not require one fixed sequence.

Accrue claims only under actual qualifying events and terms. Wages due, a tax assessment, award, invoice or receivable is not delivered cash. Arrears is the outstanding claim's state, not another debt. Payment atomically couples the funded transfer and specified claim settlement under §§11–12. If any participant rejects a new proposal, none of its funds, claims or applied markers changes.

Delivery and payment each need their real causes; negotiation cannot create stock, customers, funds or instantaneous service. Deposits, escrow, loans, theft, confiscation, refunds and credit have distinct title/custody/obligation effects. A later reversal preserves completed transfers and actual use; supported recovery or compensation is a new claim/event, not automatic money.

Prices, wages, financial institutions, exchange and credit issuance are profile-owned. Money creation requires an enabled institutional mechanism. Successful operation can earn actual profit through real inputs, demand and sales; merely naming a business does not guarantee income. Full ECO procedure is in §114; the accounting definitions are owned once by §12.

## Organizations, Staffing and Accountability

#### Abstract resource and entitlement interpretation — CW-SSN-07

A spendable or descriptive abstraction declares whether it represents physical stock; money/transferable asset; enforceable claim/entitlement; institutional allocation; purchasing/requisition capacity; derived rating; or a campaign-level abstract budget. State its unit, actual authoritative owner, allowed spending/transfer, backing and reconciliation when applicable, represented scope and conversion/profile. Similar labels imply no exchange rate.

Use one authoritative balance for a spendable value. If a rating merely derives from actual money, capacity or influence, it is not separately spendable. An abstract budget that deliberately replaces detailed accounting declares that covered scope and cannot coexist as an independently spendable duplicate balance. A claim/allocation may authorize acquisition without providing goods or receipt. Delivery and production still require their selected supported mechanism.

Bind expenditure timing and resulting entitlement/stock/financial effects before commitment. Repeated resolution cannot create another kit or spend the same backed value twice. A genuine abstract supply procedure can resolve goods only as its complete enabled profile permits; no unspecified stock, currency, conversion or institutional authority is invented. Migration preserves actual balances, rights, obligations, backing and completed delivery. SSN's Supply and RP values remain native profiles.

#### R3 proposed income, taxes and obligations interaction

Earnings **accrued from actually completed or interruption-settled work** become a dated ECO obligation; they are not transferred cash. An assessed tax becomes a claim, not state revenue. The same underlying claim may be partially settled once per debit/credit event, never collected again from a duplicate report. Assessment, receipt, payment, wage accrual and treasury authorization have different effective times. Simultaneous taxes, civilian transfers, military payroll and budget commitments compete over the same K-STOCK balances under §11's allocation rules. Revenues expected later may inform budgets without becoming present purchasing power.


<a id="core-25"></a>
### 25 Organizations as Persistent Actors

An organization is a persistent actor made of actual people, roles, mandates, assets, obligations, information, procedures and finite support. Use K-ORG and §107 for those records. Shared functions may include operations, personnel, logistics, information, records, finance and care; names, hierarchy and titles are supplied by context.

An organization profile establishes purpose, recruitment/membership, service terms, doctrine/methods, training distribution, leadership culture, equipment establishment versus actual holdings, shortages, support and institutional relationships. The profile describes requirements; a label creates no staff, stock or authority.

One person may hold several functions within finite time. Delegation provides bounded actual authority and means while recipients remain autonomous (§29). Ordinary institutional work can proceed without the protagonist.

Use aggregate personnel, named supporting members and full significant actor records at the detail needed. Expanding an existing cohort member transfers their represented identity/state and removes one from the residual cohort; it is not recruitment. Named animals remain actors. Recruitment, deployment, service and operations use shared MIL §124; branch practice, period-specific doctrine, platform operating envelopes and effect models come from applicable setting or specialist modules.

<a id="core-26"></a>
### 26 Actor Service and Career Dossiers

A dossier is a view of one person's shared records: identity/origin and age, memberships, role/trade, appointments, qualifications, experience, conditions, fatigue/availability, personal/issued equipment, audience-specific reputation, conduct findings, relationships and career transitions.

Optional profile fields such as branch, unit, rank, campaigns, battles, command relationships, commendations or offenses apply where that service exists. They do not create a separate military person, inventory or health record.

Full significant records preserve actionable competence, limits, resources, knowledge and obligations. Routine personnel can remain residual cohorts until detail matters; disaggregation preserves actual totals, allocations, conditions and uncertainty (§106). A dossier may contain provisional generated baselines, clearly separate from demonstrated or source-established capability.

<a id="core-27"></a>
### 27 Context-Appropriate Organization

Use the organization and terminology established by the setting/profile. Do not impose modern staff, regiment, police, corporate, democratic or household structures on a different institution.

Record actual units/groups, membership, functions, scope, reporting relationships, resource/control links and succession. Hierarchical, distributed, customary, voluntary or contested arrangements all use the same state interfaces. Structure is not proof of manpower, funding, competence or compliance.

Historical and fictional formation chains remain context content. Shared Core needs the relationship and its consequences, rather than a universal team-to-division ladder.

<a id="core-28"></a>
### 28 Authority, Reporting and Succession Links

For a consequential office/function establish holder, responsible/deputy actors where applicable, subordinate or peer links, reporting channels, mandate scope, decision limits and succession/temporary cover.

Rank, qualification, appointment, office, current duty, recognized authority and practical control are distinct. A title grants only its actual rights/obligations; it grants neither omniscience nor competence. A junior or unaffiliated specialist can outperform an office holder technically.

Issue and receive directions through §29/§30. Conflicting jurisdictions/claims can remain explicit. Office loss changes authority under its rule; transfer of keys, staff, money, records or information needs the relevant actual events. GOV decisions (§113) grant applicable mandates; K-ORG stores the resulting role/mandate.

#### Independent standing and control view

Where standing affects a decision, distinguish applicable rights and obligations, qualifications and eligibility, office/role and mandate, ownership and custody, practical control and access, and what particular actors recognize or believe. Reference each authoritative owner. A change in one dimension changes another only through its actual governing mechanism.

Represent legal or institutional rules under their applicable jurisdiction, scope, effective conditions, and procedure. Do not make all forms of standing one exclusive progression ladder. A title describes its actual authority, obligations, recognition, and limits; it does not automatically supply skill, personnel, property, universal respect, or practical enforcement.

This is a derived view. It does not create a second property, authority, eligibility, or knowledge ledger. Omit irrelevant dimensions and preserve unknowns. An institution's claim, an actor's belief, and the applicable rule can disagree without rewriting physical custody or previously completed acts.

<a id="core-29"></a>
### 29 Orders, Requests and Delegated Execution

Record issuer/requester, recipient, institutional authority or agreement, objective/purpose, method constraints, priority, issue time, channel, actual receipt, relevant comprehension, deadline semantics, assigned means, decision limits and reporting triggers. Use meaningful states such as issued, in transit, received, acknowledged, executing, completed, failed, superseded or cancelled. An acknowledgment is not required when no return channel exists.

Receipt is neither understanding, willingness, feasibility nor completion. Ordinary valid duties need no obedience lottery. A recipient considers actual knowledge, goals, commitments, risk, authority and means; a conflict or impossible task may produce clarification, refusal, adaptation within mandate or breach when supported.

The institutional effective condition of expiry/revocation is declared by the applicable rule: issue, receipt, publication or another actual trigger. Its transmission/receipt is separately recorded. An NPC can physically continue from unrevoked received instructions while formal validity has changed; that execution and its consequences remain real. Do not automatically stop physical acts because headquarters changed its record. Do not choose the PC's compliance or disobedience.

Delegation creates no labor, equipment, skill, rights or instant delivery. A transfer of responsibility needs actual communication/access and capacity, plus assent where terms require it. Standing authority permits routine NPC remedies without repeated protagonist approval; decisions outside it return to the actual decision maker. Unreceived orders are not available knowledge.

<a id="core-30"></a>
### 30 Communications

Information moves through actual channels.

Possible systems:

- voice;
- runner;
- signal flags;
- radio;
- satellite;
- data-link;
- messenger;
- courier ship.

Track:

range / latency / reliability / interception / jamming

A commander cannot instantly micromanage a unit whose communications have failed.

Delayed information produces delayed decisions.

Transmission, receipt and comprehension are separate. Bind channels to actual range, latency, reliability, interception/jamming where applicable, and accessible sender/recipient equipment. A courier's travel and a radio's shared capacity use the same clock. Language or technical-function limits use §15; familiar qualified communication normally proceeds without a roll.

#### Queued command, execution and confirmation interface

Where timing is consequential, distinguish creation/issue, queueing, actual transmission, complete receipt, interpretation, accepted execution, completion and acknowledgment. First/last transmitted or received portions matter only when the selected channel/application requires them. Contact windows, message size, serialization, relay processing and receiving access are profiled constraints; no universal radio or signal model is implied.

Receipt of an instruction is not completion of its task. An acknowledgment of receipt confirms receipt, not physical success. Lack of acknowledgment does not prove failure. Remote actors use actual received information, current local preconditions, delegated limits and applicable validity terms. Legal revocation, recipient knowledge and a physical stop remain separate.

The same message/event identity is retained through queues, saves and scale changes. A report updates received knowledge without repeating stock loss, work or injury. Space supplies propagation/endpoint models; messengers, delayed institutions and ordinary data networks use the same interface with their own channel profiles.

<a id="core-31"></a>
### 31 Individual and Collective Training

Training uses actual instructors/methods, learner availability, suitable tasks, tools, feedback, materials and elapsed qualifying hours (§96). Exercises, supervised work, specialist schooling, procedural drills and team practice can serve different evidence requirements.

Separate individual competence, demonstrated performance, qualification, institutional authorization and collective coordination. Repetition or mere attendance does not guarantee advancement; a coordination improvement does not award every participant an extra personal skill.

New arrivals restore available headcount only after actual arrival/assignment. They do not restore veteran proficiency, tacit methods or shared coordination merely by filling a roster. Military basic training, weapons qualification, officer education and combined-arms practice remain service-specific content.

<a id="core-32"></a>
### 32 Willingness, Cohesion, Discipline and Immediate Pressure

Keep concepts separate when their behavior differs.

| State | Meaning |
|---|---|
| Willingness/morale | Task- and context-specific willingness to continue |
| Cohesion | Capacity to coordinate together using shared methods |
| Discipline | Reliable procedural performance under relevant pressure |
| Immediate pressure/suppression | Current restrictions produced by a credible continuing threat |

Qualified newcomers can lack shared methods. A disciplined group can remain coordinated while unwilling to undertake a particular objective. Temporary formation disruption is not necessarily enduring loss of cohesion. Missing a communication path first imposes that real restriction; do not charge the same loss again through generic low readiness and cohesion labels.

Record trigger, affected function, actual state change, practical restriction, persistence and recovery. Add numerical tracks only where a selected profile improves decisions. One causal obstacle is represented once in one calculation; distinct actual downstream effects remain possible.

Military track values and training/replacement thresholds are specified in Appendix D as optional scoped reference data. They are not default city happiness, household affection, business confidence or universal loyalty.

<a id="core-33"></a>
### 33 Task-Specific Willingness and Morale

Assess an actor/group's willingness against its actual goals, knowledge, relationships, obligations, risk and means. A material loss, relief, danger or prolonged shortage can change willingness through the selected profile. A new report may cause a knowledge-dependent response without repeating the underlying physical loss.

Update the state only when its causal trigger occurs. Test an uncertain response only where consequential; an ordinary continuation or every display needs no new morale roll. The player chooses their character's voluntary response.

Restrictions and recovery are task-specific. A group unable to undertake a coordinated offensive action may remain capable of withdrawal, self-defense, care or other support. Rest, resolved danger, credible leadership, supply or changed circumstances can support recovery; numerical reset by scene change cannot.

The optional 0–100 military track, band modifiers, event shifts and initial value are specified in Appendix D. Select it explicitly under a compatible genre/profile. No universal population, loyalty or happiness score is supplied.

<a id="core-34"></a>
### 34 Credible Threat and Exposure Restrictions

A restriction requires an actual credible threat capable of affecting the target/function or a supported actor perception. Record source, reach/coverage, duration, observation and protection. Physical threat and believed threat remain distinct.

Resolve a suppression/denial action only within its real coverage, expenditure and selected effect profile. One emitted event may cause injury and pressure through supported separate consequences, without rerolling its existence or spending its cost twice. Multiple sources do not automatically impose duplicated penalties for the same restriction.

Ongoing restrictions persist only while their defined sustaining cause or retained burden persists. Reaching genuinely protective cover can remove exposure restrictions while leaving existing stress or injury intact. Ending a source does not automatically remove an accumulated condition.

The protagonist's choice to cross a dangerous area, withdraw or remain exposed is theirs. Continuous protection requires no additional action. The optional suppression states, modifiers and exchange recovery are specified in Appendix D; another genre may select a different supported threat-response profile.

<a id="core-35"></a>
### 35 Shared Logistics and Resource Flow

Every household, organization and service can require supply. The common chain is **source → allocation → handling → transport → receipt/inspection → storage → issue → consumption**. Use only meaningful stages. Allocation and requests are not local stock.

For each critical resource track specification, unit, quantity, owner/custodian, location, condition, task usability, reservations, actual demand, replenishment, transport and receipt conditions.

**Closing physical stock = opening physical stock + actual receipts/production − outgoing transfers − actual consumption − actual physical losses.** A condition change may separately alter usability without removing quantity. Retain conversion/waste records for transformation. Reservations are not consumption; planned deliveries are not receipts.

Actual route/handling/storage, compatible transport, qualified crew, usable time and return trips determine throughput (§102/§105). A distant stockpile does not feed another place until delivered. Route failure changes future flow and forecasts without destroying stock elsewhere.

Discrete activations and continuous rates use §109's interval accounting. Do not charge the same ammunition, ration, fuel or component once in a detailed event and again in an operational estimate. Exact losses and actual delivery trump prior forecasts. Distribution to a person satisfies that provision from one source; household and employer panels cannot both consume a ration for the same meal.

#### R3 proposed transit and reserved production inputs

A transfer's in-transit location is an actual K-STOCK location with a shipment identity and earliest supportable arrival condition. Sending goods debits the source once, and receipt transfers the same identified quantity out of transit once. Material inputs reserved for qualified work remain in their physical location until consumed or otherwise released; an unrelated shipment cannot consume their uncommitted balance. Staged future delivery does not fulfill an earlier stock demand or create output in advance of physical receipt.


#### 35.R5 — Physical depletion, prior reservations and obligations (PROPOSED)

Keep independent, bounded records for `physical_quantity`, `reserved_backing`, `open_claim`, `actual_consumption`, `physical_loss`, `transport_location` and `recovery_or_replacement`. A physical loss decreases the material at its true location. It must also enter an auditable **loss** channel; it is not workplace use, meal delivery, a monetary expense or a material transfer. For any material and interval, opening physical stock + measured production + receipts − actual consumption − outward transfers − losses must equal closing physical stock, with inter-location transfers canceling in aggregate.

After loss, recompute backing of existing reservations against actual surviving stock. If simultaneous claims overrun the remaining pool, do not choose a claimant by ID, list order, profession or already-written reservation token. Apply a legitimately selected allocation rule or place all incompatible claims into an explicitly unresolved backing/priority state. Preserve each original obligation, time, entitlement, quantity and evidence, even if a formerly backed reservation becomes unbacked. Do not treat released or suspended backing as debt forgiven, goods consumed, promised goods delivered, or progress completed. All claims that remain feasible must be distinguished from those requiring new authorized allocation.

**Transit:** Cargo in transit is still a physical location; loss there also requires updating surviving shipment quantity, received quantity and claim shortfalls. The R5 reference intentionally *rejects* transit-cargo losses pending a separate shipment-qualified procedure rather than silently violating transit identity.

#### 35.R6 — Input consumption, loss and replacement remain separate (PROPOSED)

For each K-STOCK material `m` across all locations including transit, `closing(m) = opening(m) + actual_produced(m) - actual_consumed(m) - actual_lost(m)`; internal transfers sum to zero. A production milestone debits only physically consumed input and releases precisely that portion of the reservation. Accepted output credits the same physical owner with its provenance, without a second production credit at job finalization. Destroyed stock is not classified as work consumption. An unsatisfied material claim is not physical stock, and late replenishment does not automatically grant the claimant exclusive allocation.

A disruption can leave multiple simultaneous claims unresolved. Preserve initial claim, lost backing, suspended status, authorized allocation history, replacement source/transit, and later fulfillment. Mark a historical shortfall *fulfilled* only by a linked actual fulfillment transaction or specifically supported settlement; do not delete evidence of the original loss. Replacement may arrive at a usable site while personnel, service capacity or authority remain missing. Work stays incomplete until its selected prerequisites are present.

**Reference limitation:** R6 demonstrates ordinary surviving stock, physical fire loss and replacement transport. It does not model spoilage, damaged output, co-product, unusable quality or in-transit loss; these remain explicitly open.

<a id="core-36"></a>
#### 35.R7 — Intermediate physical stock and disposition (PROPOSED)

Materials consumed during manufacturing are actual debits at consumption time, not a reservation or a reversible promise. Material physically converted into an intermediate becomes actual stock at its current location under K-STOCK, but it SHALL retain a separate intermediate/WIP identifier, state, selected source model and lineage. It is not usable as accepted finished stock merely because work finished or time elapsed.

Loss of an intermediate adjusts its actual physical quantity and recorded loss at the same source event. Inspection is an observation/quality decision and by itself performs no physical transformation. Acceptance, rejection, rework, salvaging and disposal require their applicable selected procedures and actual material disposition. Scrap, waste and remaining intermediate pieces must each be accounted once; only explicitly qualified transformations may create usable finished output. No material or item is reconstructed from a forecast, unfulfilled order, changed recipe or later report.

### 36 Supply, Endurance and Planning Views

Distinguish physical stock, eligible usable/accessibly allocated stock, free stock, delivered service, scheduled receipts and uncertain projected supply. Use §12 for backing and §103 for actual service; forecasts create no transfers or penalties.

For stable compatible units, stock coverage equals accessible usable stock divided by a positive consumption rate. Net reserve endurance equals usable reserve divided by consumption minus actual replenishment, only when net depletion is positive and stable. A scheduled convoy is not current stock. Stop/refine the forecast at a relevant allocation, delivery, seasonal or dependency change.

At genuinely zero demand, coverage is not applicable. At zero/negative net depletion, no depletion deadline follows under those assumptions; this does not promise indefinite sustainability. Missing staff, machinery, access, replacement parts or authority can still block the task.

Derived current/provision/forecast panels identify their time basis and attributable source/use/portion records. Do not count tank opening stock and water delivered from that same portion as separate supply. Distinct backed portions and supported co-products may contribute under their profile. Splitting containers/lots preserves lineage and totals.

The inherited optional Full/Adequate/Reduced/Short/Critical/Exhausted horizon labels are retained in Appendix D. They describe a selected planning view and add no generic penalty. Export planning reserves only eligible actual stock/capacity after relevant commitments; a future output estimate is not current dispatchable stock.

<a id="core-37"></a>
### 37 Requests and Resource Authorization

A request identifies desired function/specification, quantity, timing, requester, basis/authority, priority, limits and recipient. A requested item or service is not allocated or delivered by asking.

The responsible actor/institution checks genuine availability, competing reservations, access, cost/funding, policy, urgency, workload and delivery capacity. It may approve, partially approve, delay, propose substitution or refuse under the actual process. Routine known approvals need no roll.

Approval can authorize a reservation, order, task or funded claim through its owner. It cannot create stock, skill or capacity. A proposed substitution or new voluntary payment outside the action contract returns to the relevant actor. A title affects only its established eligibility/authority; military requisition channels remain genre content.

<a id="core-38"></a>
### 38 Service Terms, Pay and Continuing Obligations

Service terms can establish wages, allowances, bonuses, pensions, contingent proceeds, family support, duties or property-return obligations where that institution supports them. Custom, levy, patronage, contract or payroll are context mechanisms; no modern employer relationship is assumed.

Record basis, qualifying interval/event, unit, debtor/creditor, due conditions and settlement under §12/ECO. Pay accrued, due, received and remitted are different. A household cannot spend unpaid wages without an actual credit agreement; sending money does not establish its receipt.

Duty, leave, injury, retirement, capture or disappearance affect accrual only according to actual terms. A pension or loot right is not created merely by retirement or battle. Delayed pay can affect an NPC's decisions when they know it and their circumstances support that reaction; it is not universal automatic desertion.

<a id="core-39"></a>
### 39 Conduct, Procedure and Accountability

Applicable institutions distinguish conduct rules, actual acts, allegations, evidence, findings and consequences. A person's morality and an institution's classification can differ. A low performance roll is not itself proof of misconduct.

Establish scope/jurisdiction, actual authority and procedure before a consequential finding or sanction. Context may support warnings, duty changes, privilege loss, fines, demotion, custody, dismissal or formal referral; none is automatic or universally lawful.

INV (§115) owns cases and evidence-based disposition, GOV (§113) supplies applicable public authority, and K-ORG supplies role/mandate procedure. A fine creates a claim; collection, confinement or reassignment requires actual execution through the appropriate owner. Military disciplinary law and its summary/formal powers remain specialized content.

<a id="core-40"></a>
### 40 Institutional Findings and Remedies

Use incident → allegation → available evidence → competent authority → applicable consideration/hearing → finding → remedy/sanction → execution only where those stages actually apply. No universal court, warrant, jury or appeal right is assumed.

INV (§115) supplies the complete case workflow. Authority, evidence standard, finding and physical enforcement remain separate. An office holder can have limited summary powers, require referral or face the same applicable rules as others. Rank or title alone establishes no exemption.

Record scope, versioned procedure, considered evidence, effective result, review/appeal and real execution. A later reversal corrects current institutional position without erasing completed transfers, exertion, custody or elapsed time; supported compensation/recovery follows §99.

<a id="core-41"></a>
### 41 Task-Specific Capability and Readiness

Readiness answers **which task, where, over which interval, under which constraints**. Assess available people/qualifications, functional equipment, resources, geometry/access, authority where required, information, support, condition, time and continuing endurance.

Return **available/ready**, **restricted** with named limits, or **unavailable** with missing prerequisites and feasible alternatives. This is a derived assessment, not a consumable readiness pool or universal percentage.

An expert crew without compatible ammunition cannot fire. Three possessed vehicles are not three transports if drivers, route, fuel or acceptance are missing. A person can be medically restricted for one task and capable of another. Rank or a signed order supplies no physical capability.

Trace serial/parallel dependencies (§101) and competing commitments (§10). Average competence, headcount or a composite readiness display cannot erase a binding bottleneck. Already represented limitations are not counted again as generic poor-readiness modifiers.

Military readiness can additionally read selected morale, cohesion, command and doctrine states. Civil services use their actual institutional and task constraints instead of inheriting military morale automatically.

#### Personnel, availability and aggregate effectiveness — CW-SSN-08

Keep actual people, task availability, operational effectiveness, morale/cohesion/discipline, material support and a derived/explicit abstract rating as separate facts. An effectiveness/Strength loss is not a casualty count. Casualties require an actual event or selected valid casualty-resolution profile; no universal conversion from rating points exists.

A routed or disorganized unit may retain its people. Full headcount does not establish functioning leadership, equipment, supply or useful capacity. Recovery can restore readiness/cohesion under actual causes without generating recruits, restoring stock or resurrecting dead members. Reinforcement requires actual arriving/returning people or supported authorized creation, not a refreshed abstract bar.

Detailed scenes and aggregate reviews read the same persons/conditions/equipment. Named individuals are removed from the residual cohort exactly once; multiple appearances or embodiments are not additional personnel. Earlier character-scale casualties are included in later summaries rather than charged again. Keep each group's native effectiveness profile and context; SSN unit Strength does not become universal headcount.

<a id="core-42"></a>
### 42 Casualties, Availability and Reporting

Core actor identity/headcount persists through injury, disappearance, capture and death. Current operational availability categories must be mutually exclusive **within a named roster view**: available, wounded unavailable, nonbattle unavailable, missing/unknown to that authority, known captured or dead. Historical casualty labels are event history, not extra people or deductions.

Separate actual location/custody, functional condition, duty assignment and each observer's knowledge. Missing is an information/administrative state; it does not make a person dead or erase the GM's supported location. A wounded person can remain available for restricted work. A later death changes their current state without creating another person.

At physical injury/capture/death update the true supported records. At report receipt update the recipient's roster/knowledge. Reclassifying one missing member as captured changes the classification, not headcount. KIA/WIA/MIA and other report totals can describe overlapping lifetime events; only current mutually exclusive partitions are used to reconcile a roster.

Consequences propagate into actual staffing, care workload, command, supply demand, relationships and obligations where caused. Repeated reports do not reapply loss, morale shifts or stock debits. A report can produce a distinct knowledge-dependent reaction, linked to the same historical event with no duplicate physical change.

<a id="core-43"></a>
### 43 Care Movement, Referral and Handover

Use applicable functions such as immediate aid, collection, field/community care, definitive care and rehabilitation. They are functions/routes, not mandatory modern facilities.

Moving a patient requires actual people/transport, compatible capacity, route, elapsed time, custody and receiving capability. A reservation, bed, dispatch or referral is neither arrival nor treatment. Conditions, deterioration, needs and actual accompanying care continue in transit under the selected profile.

K-ACTOR owns the individual's location, custody/constraints and bodily conditions. K-NET/transport owns movement capacity; MED (§118) owns the care episode and handover; K-POP references presence/membership without a second location. Providers reference one patient and the same conditions. Release, biological recovery and return-to-duty authorization are separate.

<a id="core-44"></a>
### 44 Staff Replacements and Integration

A replacement needs actual recruitment/arrival, capability, assignment, access, equipment and time. It changes staffing, expertise coverage, training distribution, coordination and leadership workload only through supported effects.

Refilling headcount does not recreate lost veteran competence, institutional memory or tacit coordination. Qualified substitutes can cover an absence while respecting the same useful parallel cap (§10/§101); extra people do not automatically create workstations.

If a profile makes large personnel turnover affect durable cohesion, apply that scoped rule once per actual batch. Immediate missing command/skill/access restrictions remain distinct and are not charged again as duplicate generic penalties. Source military turnover values remain optional in Appendix D.

<a id="core-45"></a>
### 45 Qualification, Appointment and Advancement

An institution can require competence, vacancy, seniority, education, evidence, patronage, performance, politics or other explicit eligibility for advancement. Good performance does not itself guarantee appointment.

Distinguish recommendation, assessment, qualification, eligibility, selection, appointment, effective mandate, duty assignment, pay terms and actual provisioning. A promotion changes only the rights/responsibilities its process establishes; it is not a universal skill bonus, salary payment or equipment issue.

K-ACTOR retains competence/evidence, K-ORG the office/mandate, LIFE (§122) career transitions and ECO actual obligations. Applicable GOV decisions and communication control public appointments. No military rank ladder or universal career progression is imposed.

<a id="core-46"></a>
### 46 Professional and Personal Relationships

Professional trust, confidence in competence, acceptance of authority, respect, affection, fear, resentment and obligation can differ by direction and audience. A superior can rely on someone professionally while disliking them personally; a subordinate can respect skill while resenting authority.

LIFE (§122) owns consequential relationship records referencing actual evidence/communications. Roles and hierarchy are K-ORG facts, not relationship scores. Reputation follows actual information channels. No command relationship forces the PC's emotions or another actor's intimate consent.

## Spatial Interaction, Effects and Scales

<a id="core-47"></a>
### 47 Spatial Conflict, Commitments and Ordering

Use relative position, orientation, range, cover, concealment, elevation, terrain, frontage, visibility, mobility, preparation and reserves. Use a grid only where geometry needs it. Access and actual ability to participate precede numerical advantage.

#### Exchanges and reactions

An exchange covers one meaningful primary commitment and immediate reactions. Set its duration from activity/setting before resolution; there is no universal six-second round. Compatible incidental activity is allowed only when it grants no additional meaningful action. Long activities remain in progress across exchanges (§10).

A reserved primary commitment names its trigger and feasible action beforehand. It can trigger once and replaces the ordinary primary action, not add one. NPC reserves are not created retroactively.

The retained default permits one eligible immediate defensive response when awareness and physical reaction allow. Ordinary guard is included in attack opposition/circumstances, without another roll. Continuous cover and armor do not require reactions. A substantial dodge/interruption consumes the actor's next primary commitment unless a reserved current commitment pays it. The player declares their own chosen response.

Track response use and future commitment debt. The same future commitment cannot be borrowed repeatedly. Paying debt consumes that exchange's primary action. A reserved defense is charged once, not both now and next exchange. Additional response capacity requires an explicit selected profile. Routine protection stays effective when no emergency response remains.

#### Causal ordering

Determine order from awareness, readiness, preparation, distance/travel, current commitment and previously established timing. Independent genuinely simultaneous effects use common pre-impact state. Do not roll priority where neither action can interrupt the other or where ordering is already established.

**Proposed d100 binary ordering adapter:** for a remaining consequential priority tie, designate sides A/B before rolling. Score = d100 + relevant relative ordering-competence modifier + independent circumstances. Using the inherited competence mapping, the relative term is 10 × (rating A − rating B). Score **51+** gives A priority; **50 or less** gives B priority. It resolves order only, with no Mixed damage, free attack or extra commitment. Natural 1/100 have no special effect. Applicable capacity/readiness must be selected without double-counting the facts that already resolved order.

This symmetric midpoint replaces v2.1's use of 60/30 execution bands for a binary priority decision. At equal inputs it is 50/50 instead of 41% challenger priority, 29% other priority and 30% tie. This is a mathematically symmetric **proposal**, not a calibrated initiative system. Other dice adapters retain their explicitly selected ordering rules.

Then resolve each actor's feasible action normally at its actual execution time. An earlier effect can remove a later action's capability; it cannot erase a simultaneous effect already committed from pre-impact state. Involuntary physical consequences may be described without inventing the protagonist's chosen retreat, surrender, speech or emotion.

<a id="core-48"></a>
### 48 Reach, Range and Participation

Contact, Close, Effective, Long and Extreme are optional relative bands. Each method/profile supplies useful distances, minimum range, geometry and effect limits. A shared band name is not a metre conversion between weapons or settings.

Determine who can actually reach, observe or affect the target, then apply the adopted range/handling model. Poor accuracy and inadequate terminal effect are distinct. A high roll does not extend an effect beyond its defined reach.

Multiple actors provide pressure or assistance only where frontage, timing and geometry allow simultaneous participation. People blocked by allies, out of range or committed elsewhere provide no automatic numerical bonus. Reach can deny closure without creating free intercepting attacks; a real reserved attack uses §47.

<a id="core-49"></a>
### 49 Cover vs Concealment

Cover physically protects.

Concealment prevents observation.

Smoke may conceal without stopping bullets.

A stone wall may provide both.

<a id="core-50"></a>
### 50 Terrain

Terrain influences:

- movement;
- visibility;
- formation;
- weapon use;
- fatigue;
- cover;
- logistics.
Examples:

Urban rubble slows vehicles.

Mud limits heavy equipment.

Woodland shortens engagement range.

Steep slopes exhaust infantry and animals.

<a id="core-51"></a>
### 51 Weather

Weather can affect:

- visibility;
- flight;
- navigation;
- weapons;
- supply;
- movement;
- health;
- morale;
- communications.

Weather is not merely scenery.

<a id="core-52"></a>
### 52 Spatial Arrangement and Collective Coordination

A formation/layout defines actual participant positions, orientation, frontage, spacing, access, maneuver, coverage, mutual support and exposure where consequential. It applies to organized conflict, work teams, processions, rescue and other spatial tasks without assuming military doctrine.

Check who can participate simultaneously and what paths/hands/attention are available. A larger headcount provides no automatic benefit where frontage, access or workstations exclude them. Reconfiguration takes actual time and may displace a different function.

Temporary disruption can reduce immediate coordination or mutual support without changing enduring team cohesion. Any lasting effect needs its own supported trigger/profile. Military formations and tactical values remain genre/module content; the spatial and commitment interface is shared.

<a id="core-53"></a>
### 53 Weapon and Harmful-Effect Modes

A weapon is an asset with distinct operating/attack modes: reach/range, handling, volume, penetration/potency, terminal effect, ammunition/resources, reload, exposure and condition. A material, ammunition type or trait changes only the supported mechanism.

A sword's cut, thrust and pommel strike can use different channels. A launcher and projectile are separate compatible profiles. Draw/load capacity can gate use despite high skill. Natural attack profiles incorporate ordinary anatomy/mass already; a separate charge or fall may add distinct momentum under the selected model, without adding normal scale twice.

Traits grant concrete methods or effects, not universal bonuses. Sunder-like material effects change material stress when defined; they do not automatically increase bodily injury. Grip/control requires a declared objective or an explicitly coupled ability. Reload requires actual time, hands, ammunition and access.

Core supplies the effect interface (§5), not a universal sword, rifle, claw or energy-weapon damage table. Select one compatible effect profile for each interaction, with explicit mappings where different models meet (§112).

<a id="core-54"></a>
### 54 Protection, Coverage and Residual Effect

Protection records construction, material, coverage/orientation, channel, condition, required operation and applicable model/version. It affects only profiled channels and reached locations. Smoke can conceal without stopping projectiles; a physical barrier can protect without resisting information access or mental effects.

Execution success, contact, protection interaction and injury are separate. Resolve stopping, attenuation, penetration or other profiled interaction before residual effect. A stopped primary channel cannot return through location or placement bonuses. Secondary heat, blast or another transmission needs its own declared mechanism; it is not assumed from a weapon's name.

Absence of relevant protection supplies no automatic reduction. Unknown, unassessed and zero protection are different states. Layering uses an integrated profile or explicit independent mechanisms; do not sum complete ratings from incompatible models. Local damage changes the actual affected component/channel, not every armor region.

Inherited numerical fantasy Defeat/Resistance, injury grade, location and stress tables stay in their selected effect package. Historical severity steps and campaign point systems retain their own complete chain. Core promotion reuses their structural separation without combining their numbers.

<a id="core-55"></a>
### 55 Assets, Vehicles and Components

Core assets record owner, custodian, location, configuration/version, functions, components, operating modes, resources, qualifications/stations, faults, maintenance and history. Use one simple item record when additional components would not affect decisions.

A vehicle can separate structure, propulsion, steering, crew, sensors, weapons, fuel and ammunition. Mobility damage, lost sensing and occupant injury are different effects. Subsystems depend on actual links, operators and resources (§101); a universal effectiveness percentage cannot replace these limits.

After an effect, update the affected component or selected point/threshold state once, propagate actual dependencies, evaluate separately exposed occupants and recompute task capability. Retain adopted hull/condition points with explicit thresholds; the same hit described as a fault is not a second loss unless the effect profile separately defines both consequences.

A component record does not supply flight, buoyancy, flooding, seamanship, vacuum survival or weapon penetration. Those need relevant physical/effect modules and profiles. Living mounts remain actors with care and needs, using equipment records only for tack/cargo.

#### Embodiment binding

Use this interface only where the selected actor/device profile calls for it. Core supports the relationship; it supplies no autonomous-machine technology or consciousness theory.

K-ACTOR retains actor identity, goals, knowledge references and competence and control-relevant actor state. Physical components/faults use the declared authoritative embodiment owner: usually K-ASSET for machinery, or K-ACTOR for biological structures under the selected physiology profile. Every actual component/condition has one owner-qualified reference.

Capability reads actual body/asset functions through the binding. A sensor fault recorded on a robot's asset prevents that actor's sensor observation where no supported alternative exists. Do not add a second independent “sensor wound” and repair only one of the two ledgers. Distinct mind/interface/strain effects can coexist when they represent distinct supported mechanisms.

A device can be controlled by another actor rather than be an autonomous actor. Control rights, received commands, sensors, processing, bodily function and legal identity remain different facts. K-POP membership/presence counts use the appropriate cohort/profile and actual identities; an asset/actor binding does not silently add a human resident.

Damage, repair, control transfer or replacement writes actual affected state once, then recomputes capability views. Replacing a chassis does not automatically copy an actor's private knowledge or identity; the applicable setting/profile must establish how that works.

#### Identity, presentation and manifestations — CW-SSN-04

Separate continuing actor identity, physical embodiment, observer-specific presented identity, claimed identity, manifestation and actual control relationship. Presented/claimed identity is K-INFO evidence/belief; physical configuration/conditions use the actual actor/asset embodiment; genuine additional actors and population membership use their existing owners.

An enabled module may classify a manifestation as perceptual illusion, disguise/transformation, physical projection/extension, independent created/summoned actor or remote embodiment. A classification enables no power. Illusions do not create physical people. Appearance changes do not confer legal identity, capabilities or ownership. A physical transformation changes only its explicitly supported properties while preserving continuing identity and actual history.

One controller using three devices remains one actor with three asset references and actual communication/control/time constraints. Additional autonomous actions require supported controllers/agents, means and available commitments; a visual double has no free action. Genuine independently existing created actors receive supported identity, embodiment, resources and autonomy once through authorized initialization/production. Arrival, control and obedience are separate. Projection destruction does not automatically kill the controller; permanent population membership/persistence requires its own declared profile. No illusion/clone/summoning cost, duration or SSN catalog is imported.

<a id="core-56"></a>
### 56 Specialized Platform Modules

Complex platforms can add reactors, coolant, actuators, sensors, limbs, mounted equipment or operator interfaces only where the setting supports them. Use Core components, resources, crews, work and service dependencies; the specialized module supplies its additional mechanisms.

Heat, recharge and bounded operating burdens use §109 with actual profile limits. They are not automatically percentages, universal explosions or physiological strain. Equipment availability, power/energy, command authorization and competent operation remain separate.

A platform module declares anatomy/configuration, operating limits, modes, inputs, damage model, crews, movement, failure behavior, repair and interfaces. Choosing the module creates no actual platform. Existing campaign-specific systems remain until prospectively migrated (§97/§112).

<a id="core-57"></a>
### 57 Crew, Automation and Specialized Interfaces

Each station names tasks, access/controls, qualifications, authority, attention/capacity, staffing interval and fallback. Essential roles need actual people or an established substitute. Independent crew can work concurrently while sharing finite platform resources. A passenger or replacement is not automatically qualified.

On station loss, accessible controls may be reassigned to a capable actor with actual transition time and abandoned duties. Automation continues only tasks its sensors, data, design and delegated authority support. It cannot observe through missing equipment or know an unreceived report. Inferences retain confidence. It does not choose the player's voluntary actions.

For explicitly enabled linked/multi-operator interfaces keep long-term compatibility, current coordination, interface stability and individual strain distinct. Strong coordination cannot cure an unstable link or erase accumulated strain. The module defines accumulation, threshold, consequences and recovery; ordinary historical humans acquire no neural-strain track.

Loss of an operator can restrict a function without stopping every platform function. Role redistribution, automatic control, reduced operation and shutdown depend on actual design. Joint objectives and assistance use §10 rather than adding every crew member's full skill modifier.

<a id="core-58"></a>
### 58 Protected Sites and Defensive Systems

Record actual construction, access, observation/coverage, protection, obstacles, structural/component condition, personnel, stock, communications and maintenance. An access-control system or defensible site provides only the supported detection, delay, protection and response functions.

Fields of fire, walls, gates, barriers or fortification layouts are context-specific configurations. Protection is channel/coverage-specific (§54); no defensive label supplies invulnerability, complete sight or adequate supplies. A breach changes the affected structure/access, not unrelated stock or morale automatically.

Staffed response uses real readiness, route, authority and communication. Siege fortifications, security technology and extraordinary wards require their own compatible content/effect profiles; they share the existing assets, stocks, actors and work.

<a id="core-59"></a>
### 59 Sustained Access Denial and Attrition

An ongoing blockade, siege, isolation or other access-denial operation requires an objective, coverage, actual enforcing means, route geometry, communication, endurance, stop conditions and affected users. It does not automatically delete all trade or teleport enforcement to uncovered routes.

Track real food/water/operating inputs, protective works, access/breach work, conditions/exposure, civilian/user state, outside aid/relief and continuing service. Logistics, engineering, willingness, supported disease/exposure and elapsed time can be decisive without repeated combat rolls.

Advance those existing processes through the same event frontier and resource owners. Relief must actually arrive and obtain access; a successful message supplies knowledge rather than transport. Partial coverage, alternate routes, real reserves or a completed remedy can solve the problem.

Warfare's detailed siege engineering, breach effects, disease model and tactical procedures remain specialized modules. The shared Core supplies persistent consequences, time and feasible operations across scales, not a universal siege timer.

<a id="core-60"></a>
### 60 Reconnaissance

Reconnaissance determines what an actor/group can know. Information carries a source, observation time, age, reliability, and confidence. Good reconnaissance improves decisions through the evidence actually acquired.

An appropriately equipped expert automatically notices plainly accessible evidence when time and access permit. Concealment, incomplete coverage, deception, and urgent interpretation can require checks. Success reveals evidence within the method's reach. It cannot identify cargo through an opaque wall without a suitable means.

Access to plainly observable evidence is automatic for qualified observers with sufficient access and time. This does not guarantee correct conclusions about concealed causes.

<a id="core-61"></a>
### 61 Intelligence

Maintain world facts separately from reports. A report contains observer, observation time, observed content, method, confidence, transmission time, arrival time, recipients, and interpretation. Confirmed means confirmed to a specified observer by a stated means, not universal omniscience.

Record observation and interpretation separately. Three trucks seen entering a compound is an observation; a resupply operation is an interpretation. New intelligence revises confidence with a traceable cause. Report age increases as time passes, while relevance depends on how quickly the subject can change; static terrain information and moving patrol reports do not expire at the same rate.

Classify intelligence as confirmed, probable, possible, or unknown relative to a named observer or recipient. A rumor in a briefing is not an objective world fact. Intelligence failures remain valid emergent complications. Section 85 controls delivery delays.

#### Assertion lineage and observer access

K-INFO preserves provenance per material assertion when a report combines sources. Reference the underlying observations and intermediate copies in a derivation graph or equivalent component/source sets. Distinct report IDs do not imply distinct observations; distinct origins do not establish independence. Preserve materially new correlated observations, shared components, contradictory assertions and unknown origins separately. A circular chain of citations supplies no new originating observation. Actual hidden lineage, claimed provenance and each recipient's known provenance are distinct; an analyst cannot read hidden truth merely because the engine stores it. No numerical confidence rule is implied by counting roots.

An evidence object's physical custody uses K-ASSET/K-STOCK; its content and collection history use K-INFO. A population cohort carries relevant distribution/conditions; named people are removed from the residual count when expanded. Do not assign a single cohort a uniform skill when the source only establishes an average.

#### Measurement and interpretation binding

An observation or measurement records its actual target/process, observation/as-of time, method/sensor/witness, accessible scope, reported value or supported interval, relevant units, uncertainty/resolution, calibration/status and transmission/receipt. A belief or derived estimate references its inputs and model rather than overwriting hidden actual state.

More digits do not establish more precise instruments. Overlapping supported intervals remain unresolved or follow the applicable published tie/decision rule; they do not imply an invented coin flip or numerical confidence. Error correlations and shared sources retain lineage. A medical reading, navigation estimate, quality inspection and contest measurement use this common record contract, with their actual method/effect models remaining specialized.

Institutional adjudication can change recognized results or permitted action under its actual authority. It does not change the physical trajectory, elapsed exertion, prior consumption or what a witness previously saw.

<a id="core-62"></a>
### 62 Operations and Resolution Scales

#### Resolution scales

| Scale | Scope |
|---|---|
| Individual | One person's immediate action |
| Tactical | Squad or local engagement |
| Operational | Coordinated formations pursuing an objective |
| Strategic | Campaigns, force generation, industry, and political commitments |

Choose the smallest resolution scale necessary for the player's current decision. Name the participating force, objective, area, interval, committed assets, credible loss exposure, and stop conditions. Evaluate direct combat, reconnaissance, mobility, protection, engineering, transport, and endurance separately where relevant.

A force ratio affects the task only where forces can actually participate. Troops outside the frontage, weapons without line of effect, and vehicles without fuel do not provide a universal bonus. Assign force advantage through the ordinary circumstance scale with a written reason. This release does not claim a calibrated universal casualty formula across eras and technologies.

Resolve each operational interval through preparation, contact, execution, reactions, and reconciliation. Use the core check for one meaningful contested objective. Before rolling, specify success, mixed, and failure effects on that objective and a credible cost range where losses are uncertain. Exact casualties require an established campaign damage model or a predeclared bounded loss procedure; never infer a percentage solely from the words mixed or failure.

Pause when a command decision, major new contact, decisive loss of capability, or player-scale scene becomes relevant. Remote routine operations can continue autonomously within their orders. Do not finish an entire major battle from one ordinary declaration.

At a scale change, record a boundary timestamp and reconcile headcount, casualties, ammunition, fuel, equipment, locations, and unresolved actions. Detailed scenes replace the corresponding abstract activity for that interval. They are not added on top of it.

If a squad starts with 12 people, two named members become wounded during a detailed scene, and both remain with the unit, the operational record is ten uninjured plus two wounded. A later report of those same two casualties adds zero new casualties. Physical loss, report receipt, and administrative reclassification are different events.

#### Mission assessment

Record objective, constraints, deadline, committed assets, and reporting requirements before execution to the extent they are known. Evaluate objective achievement, compliance with constraints, timeliness, cost, and continuing capability separately. Capturing a bridge after destroying it may win the engagement while failing the mission.

Operational planning includes routes, supply, intelligence, terrain, timetable, reserves, communications, and enemy intentions. Do not resolve an entire campaign from a tactical success unless that action actually had strategic leverage.

#### Boundary reconciliation

Use the scale-change procedure above whenever entering or leaving detailed play. Preserve ongoing actions and remaining commitments; a scale change does not refresh reactions, ammunition, fatigue, or resources. Section 42 governs casualty classification.

#### Coverage of aggregate intervals

Record participating entity IDs, area, start/end and activity covered by each abstract resolution. A detailed scene consumes/replaces the matching coverage. Remaining abstract work applies only to disjoint actors, time or effects. Estimated future expenditure is superseded by corresponding actual events; it is not committed as an additional loss.

If a scene concerns two of a twelve-person unit, retain their named records and the residual ten-person cohort. Aggregation reads both. Preserve remaining work, initiative, response debt, reservations, locations and threshold times at the boundary. Changing scale never provides a new exchange unless actual time advances into one.

#### 62.R4 — Source-exclusive coverage over scale changes (PROPOSED)

Every actual effect on personnel, output, injury, equipment, provision, or other conserved stream is committed once under its source event ID and owner. A view at tactical, daily, monthly or strategic resolution reads those sources and cannot create another stock, casualty, wage or completed-work increment. `CoverageSpan` records contributor(s), process/stream, owner-qualified metric, start-inclusive/end-exclusive causal interval, source effect and the applied model. Aggregate simulation may generate **new** events only for an identified residual contributor/time/effect domain not already covered by a detailed resolved source. The aggregate domain must prove its residual population/actor/asset partition and effective intervals; overlapping claimed coverage is rejected or explicitly split with qualified evidence.

**Temporal attribution:** A completed source span wholly inside a requested view can be summed directly. A span crossing a view boundary must use established time-distribution evidence or remain an identified unattributed partial contribution; do not divide its output equally merely to fill a report. Quantities with unlike units, effects, qualifiers or population bases are not silently additive. Independently generated reports, after-action accounts or revised public knowledge refer to the original source rather than causing fresh losses. Scale shifts never reset elapsed work, resource reservations, cooldowns, injuries, force readiness or institutional decisions.

**Reference qualification limit:** The R4 coverage adapter checks exact contributor identifiers for one synthetic stream and read-only interval views. It neither proves cohort-membership partition from K-POP nor integrates an independently authored daily/monthly producer. A production runtime must verify contributors and source ownership through K-ACTOR/K-POP/K-WORK/K-STOCK and support partial-interval settlement under the selected production law.

#### 62.R5 — Tactical, daily and strategic military source equivalence (PROPOSED)

A tactical engagement commits each real expenditure, injury/incapacitation, fatality, capture, physical damage and positional effect once using its selected model, pre-event state and event provenance. A strategic formation view aggregates **the same committed owner records**; it is not a second engine allowed to issue a fresh casualty or expenditure. An incapacitation is not presumed death, and reported losses are claims/observations until reconciled against actual events. Separate *occurrence → observation → report preparation → transmission → receipt* times and information access. Duplicate report deliveries must never increase the physical casualty count.

Scale-qualified views require exact contributor and time coverage, source identity, selected model and consistent owner scope. Transitioning tactical→daily→strategic→tactical must preserve all injuries, remaining ammunition, materiel, troop memberships, household obligations, pending orders and event backlog. A named person already resolved tactically must be excluded from residual cohort effects over overlapping intervals. A report about a contested or unresolved casualty does not establish a physical outcome. A historical as-of view requires an archived checkpoint or actual bitemporal replay; current actor conditions cannot be projected backwards as if unchanged.

**Reference limit:** R5 uses explicit named actors, fixture-confirmed `disable` effects and a read-only journal projection; it does not resolve actual combat probabilities, residual-cohort losses, injury severity, two genuinely independent tactical/strategic solvers, or multi-month strategic operations.

<a id="core-63"></a>
#### 62.R7 — One event source across process and reporting scales (PROPOSED)

Intermediate work, damage, inspection, acceptance, salvage and completed operations SHALL be represented by distinct source events while strategic, daily, workplace and character-scale views reference those same event IDs. Displaying WIP as expected future production does not add an accepted output to K-STOCK. A reporting-scale transition must not replay accepted completion or rescue an already destroyed intermediate; historical as-of views require an actual source-aware checkpoint or replay boundary. R7's fixture exercises one site across work and economic perspectives, **not** an independently executing month-scale simulator.

### 63 After Action Report

After a substantial operation, update the authoritative records.

| Category | Update |
|---|---|
| Objective | Achieved, partial, or failed; constraints and deadline |
| Personnel | Casualties, availability, replacements |
| Equipment | Damage and losses |
| Ammunition | Expenditure |
| Supply | Consumption and remaining endurance |
| Intelligence | Observations, interpretations, report recipients |
| Morale | Event-based change |
| Experience | Relevant lessons |
| Reputation | Consequences |
| Doctrine | Lessons awaiting evaluation or adoption |
| Follow-up | Unresolved tasks and continuing capability |

The report summarizes existing event records; it does not apply losses or costs again. Provide a visible report when useful, limited to what its author and recipient can know.

## World Actors, Life and Development

<a id="core-64"></a>
### 64 Autonomous Actors and Off-Screen Work

A significant NPC/group maintains goals, knowledge, role, competence, current condition, resources, relationships, obligations, risk tolerance, task and decision limits. Actors use their own information and available means; the world continues through the shared clock.

Routine assigned work progresses without repeated protagonist intervention when resources, authority and capacity permit. A technician can finish a repair, a service can reroute supply and a household can make ordinary arrangements within its established responsibilities. New decisions outside delegated bounds belong to the appropriate NPC or player authority.

Off-screen action requires a recorded cause/plan, not a retroactive event added to defeat the player. Other actors can consume, trade, recover or relocate finite supplies (§104). A solved problem can remain solved. Current task states and reports preserve delays, interruptions and failures through §§10–12.

Use aggregate detail for routine actors but retain distinct decision-relevant capabilities, knowledge, relationships and conditions. A threatening animal is motivated by actual ecology/behavior, not the label monster; a named animal remains a living actor.

#### Autonomous obligation choices and review triggers

At a meaningful plan boundary, consider threats, goals, obligations, commitments, knowledge, relationships, risk tolerance, expected consequences, and available means. These are decision inputs, not a universal compulsory obedience hierarchy. An NPC may keep, evade, delegate, renegotiate, or breach an obligation when their established circumstances support that choice.

Record the consequential choice and its implementation. Reconsider at its due review, interruption, or material new information; routine continuation does not require a new decision roll every turn. Actual communication determines what the actor knows. A distant revocation does not magically inform its recipient, while formal validity follows the applicable institutional rule.

Autonomy creates no additional time, labor, authority, or resources. Departure leaves an actual staffing gap unless another actor covers it; delegation transfers a task only when authority, communication, acceptance where required, and capacity support it. Independent simultaneous physical events still follow the shared event contract. This procedure never chooses the player character's voluntary conduct.

<a id="core-65"></a>
### 65 Faction Simulation

Each major faction should track:

- leadership;
- goals;
- manpower;
- resources;
- territory;
- military strength;
- economy;
- relationships;
- current operations;
- internal factions;
- intelligence.

Factions act according to their own interests.

They should not wait passively for the protagonist.

<a id="core-66"></a>
### 66 Social Resolution, Relationships and Reputation

Establish request, current relationship, relevant values, cost, authority, leverage, alternatives, knowledge and actual willingness. Successful persuasion changes willingness within plausible limits; it does not rewrite personality or dictate the protagonist's thoughts, emotions or voluntary compliance.

Track trust, respect, affection, loyalty, fear, obligation and resentment separately when they affect decisions. Descriptive states are sufficient until a selected numeric model improves decisions. Professional confidence can differ from personal affection. One interaction may affect them differently for different witnesses.

Reputation is audience-specific: originating event → witness/source → transmitted report → audience interpretation → consequence. Fame and recognition require actual information channels; no global score instantly reaches strangers. Gratitude is not automatic romance, and absence is not automatic universal resentment.

A social restriction and material impossibility are separate. An autonomous helper, official or entity can refuse a request despite the requester possessing access. Contact, recruitment, arrival and control are distinct. Extraordinary coercion must define a scoped agency override; it is not treated as sincere voluntary agreement (§4/§112).

#### Concession, commitment and delivered result

Before resolving a consequential social action, identify the feasible change sought: information, willingness, permission, an undertaking, a commitment, or immediately performable assistance. Resolve only the declared change within the recipient's actual authority, motives, knowledge, and means.

Carrying out a concession remains subject to actual communication, resources, access, work, time, and other actors' decisions. Create the necessary tasks, reservations, messages, and due events through their existing owners. Distinguish willingness, promise, institutional decision, receipt of an instruction, execution, delivery, acceptance, and settlement where the differences affect behavior. A stage may be immediate or unnecessary; do not impose extra rolls, delays, or approvals merely to populate the record.

Success must obtain the agreed feasible result. Once authorized assistance has actually been performed, do not withhold it by retrospectively redefining the successful concession as a mere promise. Conversely, an undertaking to seek another person's decision does not establish that person's assent. Later breach or inability requires a supported intervening choice or circumstance and its consequences.

An expressed assurance, genuine willingness/undertaking, and institutional validity are distinct. A valid permission or delivered assistance requires actual authority and means. An actor may make a false claim, issue an invalid permission, or promise beyond their capacity when their behavior supports it; record the assertion, belief, and validity separately. Such an assertion does not fulfill an objective requiring a genuinely valid concession. A check explicitly resolved as obtaining a genuine feasible undertaking must establish it; do not retrospectively substitute a false assurance to cancel success. Preserve hidden motives and each actor's knowledge rather than making the public description omniscient.

Mixed terms cannot silently impose a new voluntary purchase, concession, route, or time commitment. Return new voluntary decisions to the relevant decision maker under the existing action contract. NPCs may carry out routine delegated work within their standing authority without repeated protagonist approval.

The procedure may resolve NPC reactions. It cannot choose the player character's beliefs, emotions, assent, or voluntary compliance when the player character is the recipient. Resolve actual involuntary constraints and consequences through their supported mechanisms, then return the voluntary decision to the player.

<a id="core-67"></a>
### 67 Romance

Romance develops through:

- compatibility;
- attraction;
- trust;
- shared experience;
- availability;
- personal priorities.

One-sided attraction remains possible indefinitely.

No relationship is predetermined by genre expectations.

<a id="core-68"></a>
### 68 Households, Property and Care

Households reference actual independent members, dependants, shared/private property, custody, care responsibilities, income/claims, provision sources, housing, relationships and obligations. Family membership does not place every asset in communal ownership or make every adult fully available labor.

Employer/service provision and household provision use the same person's needs. A meal delivered by one source is not consumed again by another panel. Sending money is not its receipt; expected wages are not cash (§24). Care duties and travel constrain usable work (§10).

Household members retain goals, skills, knowledge and relationships through deployment, absence, retirement or succession. Institutional terms determine actual support or benefits; injury or missing status does not universally stop pay, transfer property or create a pension. Ordinary family life is legitimate progression.

<a id="core-69"></a>
### 69 Succession and Generational Continuity

When enabled, retirement/death or an agreed control transition introduces a successor into the same history. Preserve valid people, places, property, claims, debts, technology, institutions, events and historical memory.

Separate protagonist control, legal succession, asset custody, household obligations and institutional appointment. Transfer specific assets once through actual institutions/agreements, retaining faults, condition, reservations and liabilities where terms apply. A successor does not automatically inherit skills, memories, intimate relationships, secret knowledge, office or every debt.

An institutional replacement needs qualified people, valid authority, information/access and resources (§107/§108). Existing projects and NPC lives continue. The successor may be an existing unrelated actor; inventing a child is not necessary. Later audiences may remember history inaccurately while actual event records remain unchanged.

<a id="core-70"></a>
### 70 Death

There is no universal respawn. Declare the campaign's death model before play.

| Model | Result |
|---|---|
| Permanent | The character's life ends; campaign continuation follows the agreed premise |
| Generational | A successor continues in the same history |
| Setting resurrection | Established setting rules apply |
| Explicit time loop | Established loop rules apply |
| Nonlethal campaign | Severe complications replace ordinary death |

Death follows credible causality rather than random punishment. A poor roll does not invent a reset mechanic. The injury procedure in section 17 records genuine deterioration and treatment limits.

<a id="core-71"></a>
### 71 Needs, Provision and Continuity Forecasts

This optional **Core service** applies to households, travelers, workplaces, units, settlements and nonhuman actors. It is not owned by a survival genre. Track only needs that affect current or foreseeable decisions.

A requirement record names consumer, function, specification, quantity/rate, interval, minimum viable provision, preferred provision, current sources, actual reserve, substitutes, deficit consequence, onset/recovery rule and next review. The profile defines physiology and rates; Core supplies no universal water, food, sleep or climate table.

Available provision consists of usable accessible stock and **actually delivered** service over the interval. Expected supply is a separate scenario. A preference shortfall is not automatically mortal danger; satisfying bare survival does not guarantee full productivity or recovery.

Apply one selected deprivation procedure per need/cause. Useful optional descriptors are Supplied, Short, Deprived, Severe and Critical, with profile-defined transitions, affected functions and recovery. Do not automatically import the fantasy modifier ladder. Actual shortage can block fatigue recovery or cause a condition through a named mechanism; its forecast adds no second penalty.

Forecast separately by requirement, using compatible units, assumptions, confidence and horizon. With stable positive net depletion, endurance = usable reserve/net depletion (§36). Stop the forecast at the first delivery, season, allocation or dependency change; recalculate beyond it. If reserves run out before an expected harvest, the harvest does not sustain the preceding gap.

A **continuity pressure** records cause, affected function/users, reserves/buffers, threshold, estimated consequence/time, assumptions, possible responses, responsible actor and review. It is a derived prediction, not a quest marker or a second countdown resource. Resolving the cause changes/removes the pressure.

Substitution, conservation, rationing, imports, relocation and new production require actual methods, authority, inputs and time (§101). Reduced consumption extends reserves only if feasible, with actual consequences under the selected needs profile. Test relevant seasons/cycles and support/replacement dependencies, not just a favorable daily balance.

<a id="core-72"></a>
### 72 Settlement and Community Services

This optional Core service models persistent habitation and recurring coordination. Refuge, camp, settlement, mobile group and distributed community are spatial/organizational descriptions, not levels or unlocked phases.

Reference actual site/area, people/households, control/claims, shelter, service systems, stocks, institutions, routes, environment, spatial subdivisions, security, specialists, projects and relocation options. Create no walls, government, farms, clinics or guards from the label.

Record service demand and actual delivery for water, food access, sanitation, environmental protection, healthcare, waste, transport or other selected needs. Population stays at its actual count when service capacity is inadequate. If 800 people occupy shelter whose water supports 600, there are 800 people and a water deficit; no one disappears at a support cap.

Presently supportable population can be a diagnostic minimum of compatible essential-service capacities under stated per-user assumptions. Capacity differs across districts and populations. Adding beds does not increase water, food or staffing automatically. Each household's private stock remains private until actual transfer.

Formation identifies existing inhabitants, site control, services, stocks, leadership and links, then schedules real work/consumption. Expansion/contraction follow people, land, means, services and events. Relocation uses actual transport of people, property and essential equipment (§106).

Security can assess detection, delay, response and sustainment separately. Institutions and civilians use confidence, safety, legitimacy, cooperation, tensions and grievances where useful, rather than automatically inheriting military morale. Stable services can support education, employment, leisure, politics and generations without forced escalation.

#### Temporary use and durable outcomes

Temporary configuration, physical change, functional test/acceptance, applicable commissioning/authorization, actual delivery and supported ongoing operation are distinct applicable accomplishments. They may coincide, be unnecessary or occur in another supported order; they are not a compulsory development ladder.

An occupied school can supply shelter without creating occupants or utilities. A real temporary bypass can supply critical loads without rebuilding the old network. A durably viable redesigned topology can satisfy the declared objective even if it differs from the historical arrangement. Acceptance reads the same K-WORK/K-NET state and actual rights, staff, supply and support (§103); there is no extra durability progress counter.

<a id="core-73"></a>
### 73 Projects, Programs, Production and R&D

A project records owner, deliverable, acceptance criteria, work units, remaining work, qualified people, means, materials, workspace, dependencies, maximum useful concurrency, stages, quality, restrictions and next review. Prefer quantities, hours or milestones; abstract segments state what they represent.

**Progress = qualified effective rate × usable elapsed time**, bounded by remaining work, accepted inputs, access, dependencies and parallel capacity. Rate/work units must match. Completed valid work persists; interruption removes future contribution, not past achievement unless an actual event destroys it.

Routine qualified work proceeds without dice. For a genuinely uncertain work interval, retained d100 defaults are planned progress on Success, half on Mixed and no usable progress on Failure unless another branch was fixed beforehand. Elapsed time remains real. Preserve fractional work; round only display. Use this interval default only when one check meaningfully represents that interval, not as a compulsory penalty on all routine work.

Consume inputs at their actual processing/installation stage. A failed experiment or test consumes only actual used/spoiled material and may yield evidence. Further voluntary spending or work beyond authorization returns to the player. Acceptance failure creates supported rework; it does not automatically reset unrelated progress.

Example fixture: 12 technician-hours, maximum two simultaneous technicians. Two qualified technicians need six usable hours; four do not reduce it to three. If no work can start until a part arrives at hour two, completion is hour eight. A separate one-hour acceptance ends at hour nine. Preparation before the part arrives requires its own feasible task.

Production is **inputs → assets/infrastructure → qualified work/time → output → inspection → storage/distribution**, with declared yield/conversion and waste where relevant (§108). Field, forest, ore, scrap and an installed machine are not their finished products. Avoid claiming mass conservation across unlike units without a defined conversion.

R&D is **problem → hypothesis → research → prototype → trial/evidence → revision → reproducible production**. A prototype does not establish a factory, operator training or maintenance chain. Advancement of knowledge, authorization and fielding are separate (§110).

A program links several projects to an enduring capability/service objective. It owns dependencies, priorities, acceptance and assessments, **not a second progress total that advances the projects again**. Program acceptance includes actual staffing, inputs, support, distribution and commissioning where relevant (§103/§107/§108).

#### Typed clock and track views — CW-SSN-03

A clock/track states `ID, type, owning fact and scope, eligible trigger, update law, unit/segments and bounds, causal/review interval, threshold consequence, reset/termination and event history`. It is a view or the owner's explicit abstract record, never another physical work/stock/clock ledger.

| Track type | Owner relationship |
|---|---|
| Time/deadline | K-TIME's scheduled actual temporal boundary |
| Physical work | K-WORK's actual progress; segmentation is a view |
| Abstract objective | Relevant domain's supported objective progress |
| Threat/exposure | Actual risk/source/condition mechanism and eligible exposure |
| Relationship/access | LIFE/K-ORG or specialized relationship/qualification/control fact |
| Instability/burden | Existing actor/asset/condition or specialized burden owner |

Progress needs its declared cause. A failed roll does not universally advance unrelated danger; a risky failure can do so only where the supported activity and selected consequence create that exposure. A forecast is not a guaranteed event. Objective progress is not elapsed time or material stock. Decreased abstract progress does not automatically destroy completed physical work. Partitioned review retains the same work/outcome span; no extra growth or reroll. Threshold completion applies the named supported consequence, and reset/rearm cannot erase already applied history.

<a id="core-74"></a>
### 74 Technology Development and Diffusion

New technology builds on actual knowledge, evidence, tools, materials, facilities and institutions. Record which problem a revision addresses and changes in capability, mass/space, inputs, operator roles, manufacturing, maintenance, training, interfaces and failure behavior. Unchanged fields are acceptable where justified.

A higher model number or prestigious name is not a universal upgrade. A valid improvement need not acquire arbitrary drawbacks solely to balance it; its actual means, constraints and consequences must be supported. Different designs can legitimately outperform old designs when their mechanisms permit it.

Knowledge access, a successful prototype, reproduction, useful-rate production, delivered equipment, trained use and durable support are distinct (§108/§110). Diffusion requires actual reports, instruction, trade, capture, access or research. Losing a sole expert can remove practical capability while manuals survive.

<a id="core-75"></a>
### 75 Enemy Adaptation

Enemies may learn from repeated exposure where their biology/intelligence supports it.

Adaptation should follow:

- selection;
- observation;
- doctrine;
- engineering;
- mutation;
- institutional learning.

Do not buff enemies merely because the player is winning.

<a id="core-76"></a>
### 76 Ordinary Life and Careers

The same actor retains skills, conditions, property, knowledge, relationships and obligations through work, family, education, service, travel, retirement and adventure. Track age/calendar, residence, livelihood, qualifications, institutions, finances and commitments only where meaningful.

Entry to a career or office requires its actual eligibility, assessment, terms, authorizer and effective appointment. A passed assessment can demonstrate skill without granting rank, salary, authority or issued equipment. Qualification, appointment, current duty and performance are separate.

Work rosters identify role, qualified person, place, start/end, relief, tools, custody and reporting. Handover transfers actual responsibility and known unfinished tasks. Missing relief creates a situation and choices, not silently extended protagonist duty. On-call status consumes only the attention and availability its terms require.

Career reviews, recognition, leave and separation follow institutional terms and evidence. Leave approval does not create days at home before travel. Retirement changes duties, property return and claims without ending life simulation. No universal pension or automatic promotion is assumed. Genre engines supply detailed careers and setting-native procedures.

<a id="core-77"></a>
### 77 Attribute and Progression Profiles

Core remains attribute-agnostic. A profile specifies attributes/capacities, meanings, units, starting rules, discipline structure and advancement. Do not import a campaign's ten attributes, class levels or creation points into every setting.

Historical, fantasy and specialized-platform models can share state interfaces without numerical equivalence. Record the selected adapter and provenance. Similar labels such as Strength, Training Unit, Armor or Condition are not enough to establish interchangeability (§112).

Campaign-specific profiles and overrides remain authoritative in their scope. A profile change requires explicit prospective conversion where a number's meaning changes; it does not regenerate a character.

<a id="core-78"></a>
### 78 Objectives

Separate:

Immediate What is happening now.

Operational Current mission/project.

Strategic Long-term campaign objective.

Personal Character-defined ambition.

Not every game needs a constantly updating “quest log.”

Some goals arise naturally from life.

<a id="core-79"></a>
### 79 Discovery and Bounded Establishment of World Facts

Distinguish an unresolved world fact from a fact established in authoritative state but unknown to an actor. Lack of actor knowledge never authorizes regeneration of established hidden state. An unresolved availability fact establishes neither presence nor absence.

When an unresolved fact becomes necessary for a decision, first consult existing records and their constraints. If the selected scenario/profile authorizes generation, establish the minimum necessary detail once under a bounded method before resolving the dependent search, transaction, or task. Record scope, effective time, source or generation method, constraints, result, visibility, and what remains unresolved. A qualitative bound is sufficient where it preserves the decision; random selection is optional.

A result may remain a bounded unresolved world quantity when exact detail is unnecessary. Distinguish a binding generation constraint from an observational estimate: the former constrains newly established world detail; the latter records an assessment that may be wrong and does not constrain hidden truth. Label the kind, source, and uncertainty. Resolve further world detail consistently within binding constraints when it becomes consequential; revise an actor's estimate through actual evidence or assessment. Do not reroll unchanged uncertainty because the player asks again, narration changes, a scene ends, or the world is displayed at another scale.

Distinguish existence, knowledge, access, availability for the relevant interval, and usability for the task. These are separate predicates, not a mandatory progression: an actor may know a resource exists while being unable to reach or use it. Search reveals or gains supported access to existing eligible resources; execution success does not create the desired object, willing actor, authority, or service capacity.

Generate detail within established location, time, exclusions, quantities, and finite capacity. Extract a newly named member from an existing cohort when appropriate; naming does not recruit an extra person. Later arrivals, production, loss, sale, departure, or other actual causes may change availability through recorded events.

World-detail generation does not authorize inventing the player character's identity, motives, dialogue, voluntary conduct, or chosen history. Use player-supplied facts or their explicit delegation for those choices. Generation cannot revise already resolved history.

If the necessary method or material bound is missing, establish a scoped provisional ruling through the existing authority procedure. Request only information or authorization genuinely required by that procedure. Do not substitute an unsupported zero, a convenient success, or an exhaustive world database.

#### Discovery procedure

After authoritative state or binding unresolved constraints are established, bind the declared search/survey method, access, coverage, time, capability and uncertainty. Qualified observation of plainly accessible evidence normally proceeds automatically. An execution check resolves consequential uncertainty about reaching/detecting/interpreting that evidence, not whether the desired object is created.

Record evidence, interpretation and hypothesis separately (§61). A successful search reaches only supported contents within its method. A failure can leave established hidden contents undiscovered. Further real coverage, access, new evidence or changed world conditions can matter; mere repeat requests cannot regenerate unchanged contents.

K-INFO stores observation, actor estimates and generation provenance references; the relevant state owner stores actual stock, actors, assets, services or institutional facts. An unresolved generated bound is a constraint on eligible refinement, whereas an observer estimate is a fallible belief. Use the one campaign event journal for establishment and later actual changes.

## Presentation, Runtime and Continuity

<a id="core-80"></a>
### 80 Choice Presentation

Suggested actions may be provided when useful, but they are examples.

Never imply that only those options exist.

Prefer:

Inspect the damage Question the prisoner Return to command

...or something else.

Do not use suggestions when the player clearly has momentum and does not need them.

<a id="core-81"></a>
### 81 Response Pacing

Typical response structure during play:

brief sensory/situational update → resolution if needed → immediate reactions/consequences → relevant state change → return control

Do not re-explain the entire setting every turn.

Do not end every response with generic urgency.

<a id="core-82"></a>
### 82 Design, OOC and Simulation Boundaries

An out-of-character question, rule clarification, design revision, source comparison or record review advances no campaign time by itself. No NPC reaction or crisis is generated while the game is paused for it.

Use the campaign's established OOC syntax/presentation; parentheses or square brackets are adapter conventions, not extra simulation rules. Resume in-world processing only on an authorized action/time advance. Systems-design simulations use separately labeled fixture state, never alter an actual campaign, and never become evidence that the fixture values are canon or calibrated.

<a id="core-83"></a>
### 83 Strategic Player Orders

If the player commands multiple NPCs, the order itself is the player's action.

Afterward the NPCs execute autonomously.

The player does not need to personally determine every subordinate's footstep.

This preserves agency without requiring micromanagement.

<a id="core-84"></a>
### 84 Parallel Operations

When multiple teams operate simultaneously:

Track each separately:

task / leader / personnel / location / ETA / status / communications

Do not resolve an entire remote mission instantly because the player assigned it.

Advance the remote task as campaign time advances.

Assign each operation an event schedule and process it through section 11. Parallel teams share one campaign clock; overlapping work consumes time once while each team consumes its own resources. One person's hours or one vehicle's capacity cannot be allocated twice.

<a id="core-85"></a>
### 85 Information Delay

Reports arrive when communication permits.

The player may therefore make decisions using incomplete information. This is a feature of the simulation.

<a id="core-86"></a>
### 86 Hidden State

The GM may maintain concealed enemy morale, secret objectives, relationship attitudes, unrevealed injuries, faction plans, and intelligence confidence.

Hidden state obeys the same causal and accounting rules as visible state. It cannot be rewritten after the fact simply to surprise the player.

Hidden state is private game data, not something assumed to persist in an AI's unrecorded reasoning. Use a supported private ledger when available. If the platform cannot persist hidden records, acknowledge that limitation and maintain explicit recoverable checkpoints to the extent possible. Do not promise exact secret-state continuity that the platform cannot support.

A public checkpoint must respect fog of war. If durable private storage is unavailable, do not expose secret values as a workaround or claim exact hidden-state recovery. Record the limitation and preserve only what the supported mechanism can recover.

#### Compact journals and contextual views

Use the least detailed representation that preserves consequential decisions and the existing event contract. A small campaign may express that contract through a compact journal rather than database forms for every routine interaction. Contextual panels are views of the same authoritative records.

A consequential entry identifies campaign/event scope, causal time and cause/authorization, affected records, consequential changes, actual costs/transfers, visibility, and new or cancelled pending events. Include resolution details where used; exact source/destination and units for transfers; and commitment expenditure or reaction debt where relevant. Keep the preceding state reconstructible from the checkpoint and journal. Preserve the existing outcome and transaction identity needed for replay/conflict detection.

Automated versions, explicit write sets, and full before/after forms are optional representations. Their required meanings remain: validate affected current state; commit related changes atomically; prevent duplicate application and conflicting use; preserve action limits, fractional work, processed intervals, retained outcomes, and unresolved allocations. Same scoped event ID and same payload is a replay with no new effect; a reused ID with different content is a conflict and must be rejected without partial mutation.

Contiguous routine activity may be one interval entry while its relevant prerequisites and conditions remain unchanged. Retain fractions and stop or split at meaningful interruptions, thresholds, deadlines, or decisions. Compression, reviewing, saving, loading, and changing scale do not process that interval again. A report changes recipient knowledge rather than repeating the underlying loss, work, or transfer.

Hidden continuity requires actually recoverable storage with appropriate access. Unrecorded reasoning is not a save, and a hash cannot reconstruct missing state. State the deployment's actual privacy and persistence limits.

<a id="core-87"></a>
### 87 World Consequences

Important actions can affect:

- law;
- public opinion;
- military doctrine;
- politics;
- trade;
- infrastructure;
- diplomacy;
- technology;
- culture.

Consequences need not appear instantly.

Some may emerge months later.

<a id="core-88"></a>
### 88 Campaign Initialization

Complete only the decisions required before dependent play. Unknown world facts stay unknown; unresolved rule/parameter choices are named design gaps, not silently invented history.

| Domain | Required selection or record |
|---|---|
| Architecture | Campaign ID; exact Core, genre, theme, library and profile versions; scoped overrides |
| Premise | Geography, starting facts, tone, boundaries, calendar and date |
| Actors | Attribute/capacity profile, disciplines, physiology, ordinary capabilities, generation/status policy |
| Resolution | Dice/competence mapping, effect model, ordering/reactions, assistance and Mixed branches |
| Time | Commitments, work, travel, interruption and routine schedules |
| Health/needs | Injury, hazard, care, exertion, deprivation and death rules where enabled |
| Stock/assets | Units, specifications, custody/access, configurations, compatibility and reservations |
| Society | Households, economy, claims, institutions, authority, roles and obligations |
| Work/services | Capacities, inputs, concurrency, acceptance, infrastructure/topology where relevant |
| Information | Observers, channels, latency, uncertainty and reputation distribution |
| Persistence | Authoritative owners, event journal, private-state support and checkpoints |
| Adoption | Effective time, compatibility bridges, inherited states and unresolved conversions |

A module manifest identifies required records, read/write owners, consumed events, produced effects, triggers, parameters, adapter and overrides (§112). Selecting content defines permitted references, not an inventory or roster (§111).

Initialize actual actors, places, assets, stock, knowledge, institutions, work and events from supported sources. Test binding cases for active procedures. Numerical calibration is selected explicitly: retain existing campaign meanings; do not infer fuel rates, medical efficacy or crop yield from a template.

A new game can run Core services with all extraordinary modules disabled. An existing game begins from the last valid snapshot and prospectively adopts compatible additions without free healing, repairs, training, supplies, offices or backfilled history.

#### Sufficient state and unresolved detail

Before dependent execution, distinguish an unresolved world fact, actor ignorance of established truth and an unresolved rule/model choice. Use §79 for authorized bounded fact establishment; use §112 for missing semantics/parameters. No category is filled by unsupported zero.

Healthy/profile-supported ordinary activity needs no compulsory numerical attribute merely to be possible (§14). Initialize only task-relevant capabilities and restrictions. PC identity, dialogue, motives, purchases and chosen history require player facts or explicit delegation. A definition/archetype supplies eligible structure, not actual contents or staff (§111).

<a id="core-89"></a>
### 89 Scene Initialization

Whenever a scene begins, internally establish:

time / location / participants / knowledge / physical state / resources / immediate environment / unresolved events

This prevents NPCs from materializing with information or equipment they should not possess.

<a id="core-90"></a>
### 90 One Shared Runtime Procedure

1. Identify the authorized declaration, objective, method, target, limits, duration/stopping conditions and existing standing instructions. A design/OOC message instead uses §82.
2. Read pinned rule/profile versions, affected authoritative state, actor knowledge, current commitments, retained uncertainties and pending events.
3. Resolve any consequential unresolved world fact through §79, preserving established hidden state and player-controlled choices. Resolve only outcome-changing rule/model gaps through §112.
4. Bind the action contract (§5), real participants/means, time commitments (§10), dependencies (§101), useful operating configuration (§103) and shared allocation (§102).
5. Establish feasibility, attainable effect, exposure and authorization. Separate physical possibility, institutional validity and each actor's received/understood instructions. Select automatic qualified work versus meaningful uncertainty; fix independent modifiers and the feasible Mixed branch.
6. Retain one real supported random result per unchanged uncertainty. Advance ongoing activity only to the earliest causal frontier (§11); preserve fractions, completed work, actual inputs and process-law boundaries.
7. Resolve actual effects and autonomous reactions in causal order. Blocked channels remain blocked (§5); new harm is assessed once (§17). Independent simultaneous effects share consistent pre-state; contention needs policy/allocation. Reserved/future commitments are charged once (§47).
8. Validate and commit the related owner-qualified write set atomically (§91). Reconcile physical loss/backing (§12); recompute only affected capabilities, service/demand, forecasts and event times.
9. Observe, interpret, transmit and deliver information at its actual times (§61). Record recoverable consequential state/journal entries (§86), then narrate knowable results.
10. Return control at a new meaningful voluntary choice. Otherwise continue only within existing authorization, while autonomous actors use their own knowledge and finite means.

The same procedure governs a single attempt, household routine, court decision, investigation, voyage, clinic, repair, regional program or competition. A domain specifies a workflow over it, never another clock or parallel ledger.

<a id="core-91"></a>
### 91 Event Commit and Derived Updates

The complete event coordinator, replay/conflict classification, frontier and atomic validation procedure is owned by §11. This section defines its update interface; it is not a second processing order.

An event references campaign-scoped identity/payload, causal parents/time, action instructions, institutional authority, visibility and an owner-qualified write set containing expected current state and proposed changes. Every affected owner validates its part. Reject cross-campaign references before replay lookup; an unchanged applied payload is a no-op even if its prior expected version is now obsolete. A changed payload under an applied ID is a conflict, not a correction.

Commit all related physical/economic changes or none. Payment includes both funded title/custody transfer and claim settlement. A physically supported theft can change custody without valid title; reservations cannot veto involuntary physical destruction. Rejected new proposals leave no partial writes or applied marker.

After commit, update derived capability, demand, backing, service allocation, thresholds, queues and forecasts from actual state. Subscribers receive a scoped cause and generate only their distinct real consequence; they do not debit the initiating loss again. Independent simultaneous effects must commute from consistent pre-state. Shared scarce inputs are contending commitments requiring an allocation policy/decision, not independent full-capacity events.

Observation and report receipt update recipient knowledge rather than reapply harm, wages or transport. A generator failure can legitimately stop pumping and later exhaust a refrigeration buffer; these actual downstream effects are not duplicate destruction of the generator. Count one causal limitation once in one modifier/effect calculation.

Snapshots retain payload identity/content references, processed spans, retained outcomes, queue/dependencies, authority/knowledge, allocation/shortfall policies and unresolved decisions. A stock-only or public-summary checkpoint is insufficient for precise recovery; §86 governs actual privacy/persistence limits.

#### 91.R4 — Dependency graph, partial commits and recovery (PROPOSED)

Use §11's qualified components as *transaction groups*, not independent timelines. For any group, apply all valid owner writes or none; no partially granted pays, stock deliveries, job products or institutional status changes. A component's failure does not bar unrelated groups from processing. Record both the committed group and unexecuted request groups in the checkpoint. Replaying the same processed event payload is inert, and re-issuing a previously decided unexecuted request does not silently create a new claim. Later decisions can create new prospective effects after current-state revalidation. Report receipt or daily/monthly visualization is an observer update/view, not a second physical occurrence.

A runtime MAY use conservative false-positive components (reducing concurrency) while qualification is incomplete; it MUST NOT silently split a potentially noncommutative component, fabricate authority, or claim independent confluence without testing event permutations and equivalent owner state. Progress should not be inferred from the number of attempts, reports or displayed reviews.

#### 91.R5 — Authoritative physical loss and recoverable failure categories (PROPOSED)

Distinguish committed `physical_loss` (actual K-STOCK write) from unexecuted `allocation_pending`, `causal_order_undetermined`, `prerequisite_missing`, `invalid_action` and `institutional_decision_pending`. These represent different reasons and permissible subsequent actions. The occurrence and every downstream shortfall, backed-reservation update, work suspension and dependent decision must remain traceable to exact source events. Independent transactions should still commit; no unrelated region-wide freeze.

A disrupted process has an explicit status and retains its authorized work interval, already completed progress, inputs consumed, remaining prerequisites and any earned obligations. It cannot auto-complete from the original planned elapsed time after losing required materials. Restoration/reallocation must be prospective, qualified and explicitly authorized when authority is needed; a restored stock quantity by itself is not proof of renewed labor, consent or full output. Keep actual occurrence, observation, transmission and receipt timestamps distinct. Save/load must retain unresolved events and not replay their physical effects.

#### 91.R6 — Interrupted-work lifecycle, certified transitions and replay (PROPOSED)

K-WORK maintains the actual task and all milestone/settlement source references, with statuses distinguishing planned, underway, interrupted/suspended, settled with unfinished work, authorized continuation and actually completed. Retain original interval, eligible personnel, work source, genuinely completed work, separately unassessed elapsed time, outstanding deliverable and contingent claims. A disruption may create a *real interruption* without creating automatic injury, lost wages, wasted inputs, negligence, cancellation or default.

**Work transitions:** (1) bind a divisibility/acceptance model and enter real commitments; (2) at qualified milestones debit actual input, credit accepted output and record work performed; (3) on externally caused loss suspend only jobs whose remaining prerequisites fail; (4) assess verified work, unverified time and contractual implications independently; (5) preserve original monetary and performance obligations with any authorized adjustments; (6) deliver actual replacement assets or inputs; (7) authorize prospective continuation with new time/capacity; (8) accept further work without recounting old milestones; (9) settle the remaining claims with linked provenance. An event retry with an unchanged source ID must be idempotent; altered payload under the same ID must fail.

Replay and save/load retain committed milestones, unverified intervals, shortfalls, lineage and payment obligations. Existing R4/R5 scheduling and scale contracts still apply; a stage that is not qualified for scheduler use must be rejected, not silently converted to a legacy `complete_job`. The bounded R6 proof asserts source identifiers but **does not authenticate the authenticity of supplier invoices, labor evidence, supervisory mandates or acceptance reports**.

<a id="core-92"></a>
#### 91.R7 — Work lifecycle event contracts and failure classification (PROPOSED)

The shared coordinator SHALL support qualified source-bearing operations for `start_tracked_job`, `record_work_milestone`, `settle_disrupted_job`, `start_continuation` and `finalize_tracked_job` without bypassing the generic calendar and authoritative journal. Proposed specialist-interface operations `make_intermediate`, `inspect_intermediate`, `accept_intermediate` and `salvage_intermediate` must commit atomically against the existing K-STOCK/K-WORK records. Recorded outputs must identify an original event, selected process profile and evidence or competent decision as applicable.

A contested group stays pending as an unresolved claim, not a guessed failure or success. Classify physically incompatible evidence, missing prerequisite, invalid action, legal/authority deficiency, competing allocation, and unresolved chronology separately. Distinguish a physical occurrence from a proposed work request. If current evidence is insufficient, preserve the source event and return the unresolved decision to its competent authority; do not invent a resolution or charge costs. Idempotent replay and save/load shall preserve operation identity and preexisting state.

### 92 Anti Railroad Rule

The campaign may contain plans, threats and likely developments.

It does not contain a predetermined protagonist path.

If the player abandons the presumed story, the world adapts.

An NPC may pursue the abandoned objective themselves.

An enemy may win.

A mystery may remain unsolved.

<a id="core-93"></a>
### 93 Anti Escalation Rule

Do not respond to every success by introducing a larger enemy.

Progress can produce:

- stability;
- wealth;
- authority;
- peace;
- reconstruction;
- ordinary responsibilities.

A campaign need not escalate from gunfight to city threat to world threat to reality collapse.

This is one of the strongest lessons from the older long-form campaigns.

<a id="core-94"></a>
### 94 Anti Protagonist Centrism

The protagonist can be important without secretly being the cosmic center of everything.

Avoid automatically making:

- their biology unique;
- every conspiracy about them;
- every enemy specifically attracted to them;
- ancient prophecy revolve around them.

Exceptional status should emerge from established achievements or campaign premise.

<a id="core-95"></a>
### 95 Aftermath Rule

Major events require aftermath.

After battles consider:

- wounded;
- dead;
- prisoners;
- damaged equipment;
- ammunition;
- salvage;
- civilians;
- repairs;
- reports;
- morale;
- legal consequences;
- political response.

Do not jump immediately to the next boss fight.

<a id="core-96"></a>
### 96 Downtime, Development and Reviews

Downtime is authorized activity: work, maintenance, repair, care, instruction, research, administration, correspondence, shopping, family, leave, travel and leisure. NPCs use the same elapsed time. Compress only the interval authorized by the player; stop for changed choices.

Review when a cause or actual interval warrants it: engagement aftermath, field routine, duty handover, care reassessment, training demonstration, pay period, procurement, seasonal production, institutional succession. A review reads processed events; it does not consume another ration, accrue another wage day or perform more work.

#### Learning records

Record learner, discipline/objective, instructor/method, prerequisites, actual qualifying hours, exercises, feedback, evidence, selected advancement schedule/version, accumulated progress and assessment. Mere exposure, study access, routine repetition and completed hours do not automatically prove the next competence level. Conversely, routine demonstrated qualified work need not be denied by an arbitrary final roll.

Skill, qualification, institutional recognition and authority are distinct. A capable person can lack a license or appointment; passing an assessment creates no automatic job, issue of equipment or increase in unrelated skills. Collective learning and coordination use actual participating people, not an average skill award.

Store **hours and evidence**, with any display-unit conversion tied to its named profile. The supplied Military Life §4 reports historical training units of four hours and fantasy units of about twenty; Pass A later inspected the historical dependency; neither numerical schedule becomes universal Core. Core does not choose either advancement schedule. Forty qualifying hours can display as ten or two of those units, but matching the label TU cannot migrate advancement or prove mastery.

Migrating future progress preserves earned competence and valid evidence. Convert known units through their actual provenance and explicit new schedule. Unknown-unit progress remains unresolved, rather than receiving the favorable conversion. No universal hours-to-Master threshold is promoted.

Relationship maintenance follows actual witnessed/communicated events and commitments. Missing an appointment can create a practical obligation without automatically changing every affection score. Care, professional duties and household availability use the same commitment records. Ordinary progress can be wealth, trust, education, authority, institutions, stable services, peace or legacy (§16).

Institutional learning, doctrine revisions and equipment fielding use §110. A local improvisation can work before formal adoption; formal adoption does not retroactively train or equip everyone.

<a id="core-97"></a>
### 97 Campaign Overrides and Prospective Migration

Existing campaigns retain established dice, physiology, equipment effects, progression, institutions and exceptional rules until an explicit migration selects replacements. New source publication does not automatically adopt or cement a rule.

Freeze the last valid decision point without advancing time; preserve state, commitments, knowledge, resources, work, pending events and corrections. Identify selected additions/replacements, compatibility mappings, numerical profiles, effective time and unresolved fields. Preserve the old snapshot and convert only supported records.

Old current-state values are not regenerated from new defaults. Adoption grants no free people, restoration, money, power, skills, qualifications, offices or knowledge. Rejected accidental rules remain rejected. Resolved history changes only through explicit retcon/error correction, not routine migration.

Examples of retained scopes: an established d20 platform campaign keeps its d20/platform/interface effects; an established fantasy campaign keeps its attributes and class/spell rules; a historical campaign keeps its selected human and effect profiles; a catastrophe campaign retains only its explicitly adopted exceptional hazards/death rules. These are compatibility examples, not imports of their lore into another campaign.

For the shared mechanisms in this edition, select the bridges in §112/Appendix B. Genre modules retain specialized workflows and assessments but reference the new shared owner. Selected native implementations remain scoped dependencies, not simultaneous competing shared procedures.

<a id="core-98"></a>
### 98 Presentation Adapters and Randomness

Direct GM play, compact application fields and document-based campaigns share rules and authoritative state. Adapters change presentation, not accounting, authority or information limits. A stats panel is a view; it cannot replace the full recoverable ledger.

Configure live stats, descriptions, repeatable commands, stages, hidden prompts and long-term sources only within the deployment's verified capabilities and limits. This reference makes no claim about a platform's current field sizes or private-storage support. Preserve compatible state outside a compact panel where supported.

Show material known changes, obligations, outstanding costs and decision-relevant assumptions. A visible check can read **Roll 47 + 20 = 67 — Success**. If the modifier or total reveals hidden information, withhold the revealing arithmetic and present only the outcome and knowable consequences; retain full calculation in supported private records.

Use a supported random source and record its actual result. If unavailable, disclose the limit and use a user-provided roll or agreed fallback. Never present an authored fixture, convenient outcome or simulated display as a real random roll. Appendix C cases are specification fixtures, not campaign dice results.

Source/adoption metadata belongs in design records. Routine in-world presentation shows relevant practical consequences without dumping implementation fields the character cannot use.

<a id="core-99"></a>
### 99 Corrections, Reversals and History Recovery

Pause simulation advancement while identifying the error or changed ruling, affected scope, evidence, valid state and causal dependents. Preserve unrelated events. Record the corrected current rule/fact and invalidate the rejected version only within that scope.

| Case | Required treatment |
|---|---|
| Invalid new proposal | Reject before mutation; no partial writes or applied marker |
| Replay/collision | Same scoped ID/payload is a no-op; changed payload is rejected without mutation |
| Erroneous representation | Amend the false historical/current record with evidence, scoped authority and audit trail; do not invent a physical event that never occurred |
| Later institutional reversal | Preserve actual completed transfers, exertion, custody, use and elapsed time; revise present entitlement/standing and create only supported recovery/compensation claims or new funded events |
| Actual resolved-history retcon | Requires explicit user authorization and bounded scope; preserve the earlier snapshot/audit and recompute only affected causal dependents |
| New design/migration | Apply prospectively from the recorded effective boundary; no retroactive resource, injury or competence reset |

A recovery claim is not recovered money; a replacement award needs actual funds. No universal clawback right is implied. If a falsely recorded payment never happened, correct the representation rather than create an in-world refund. A real payment cannot be undone by relabeling it invalid after spending.

Use new event IDs linked to original events for actual compensating causes; do not mutate a previously applied payload to implement a correction. For an authorized record repair or retcon, recalculate affected views/events from the valid corrected state without double charging and without importing unsupported past choices.

Reconciliation, adoption and record repair consume no in-world time. Required in-world assessment, treatment, repair, communication or transfer remains an actual authorized task. Resume from the corrected meaningful decision point; acknowledge the material correction plainly.

#### Exceptional intervention categories — CW-SSN-05

An enabled exceptional intervention records `ID, enabling rule, invoking authority/authorization, scope, trigger, prerequisites, permitted exception, committed costs, affected owner records, evidence/continuity, counterplay, consequences, excluded changes and effective time`. Core grants no intervention currency or default permission.

Distinguish prospective exception; compatible establishment of a previously unresolved past fact under §79; extraordinary preservation of a consequence; and explicitly authorized historical retcon. An unresolved fact cannot contradict established authoritative history, grant favorable goods outside the approved generation/exception scope, or invent chosen PC history. A retcon requires the applicable explicit authority and an audit of the replaced facts, derived effects and effective scope.

Apply only actually authorized, supported state changes and committed costs once under §91. A rejected unsupported amendment does not mutate state. A preservation effect may prevent death without clearing wounds, observed events, debt, spent resources or destroyed equipment. Compensating consequences remain unless separately authorized. No Destiny, Karma, Toll, DSSN node or miraculous history rule becomes a universal Core mechanic.

<a id="core-100"></a>
### 100 Master Game-Running Principle

**Simulate first. Narrate second.**

The player chooses their character's voluntary action. Other actors have their own goals and information. Institutions have authority, procedures and finite staff. Equipment has functions, dependencies and limits. Places contain persistent resources and history. Information needs a real source and channel.

Time advances through actual activities. Finite resources move, transform and deplete through explicit events. Damage persists until an actual mechanism changes it. Recovery, learning, production, commissioning and succession are distinct processes. Reports, assessments and scale changes cannot duplicate them.

Dice resolve meaningful uncertainty within feasible effect. They do not manufacture missing capability, unrelated catastrophe, extra commitments or dramatic necessity. Success may create security, prosperity, ordinary responsibility and peace. A solved problem stays solved until another actual cause changes it.

## Shared Services and Module Contracts

<a id="core-101"></a>
### 101 Dependencies, Buffers, Redundancy and Substitution

**Status/ownership:** Proposed Core promotion from Military Life §§7–11 and PAF §§7/11–13.  
**Dependencies:** actors, assets, stock, commitments, work, events and profiles.  
**Records:** component/function, requirement edge, actual provider, alternatives, startup/mode, buffer reference and fault.

A required-function edge records input/state/specification, amount/rate, provider, timing, access, alternatives, buffer and consequence of loss. Use simple listed prerequisites when a graph would add no decisions.

#### Capability evaluation

1. Name task, location, interval and selected mode.
2. Trace required people, components, resources, upstream services, knowledge/access and actual conditions.
3. Normalize capacities through stated conversion/output ratios. Serial throughput is bounded by the lowest **comparable supported** stage; incomparable litres/hour, power and staff counts cannot be placed in an unexplained minimum formula.
4. Evaluate actual shared allocations (§102). Parallel paths add only where the mechanism permits and shared upstream capacity is not counted twice.
5. Check real buffers, redundancy, switching time and start/run prerequisites.
6. Return available, restricted or unavailable, with named bottlenecks and alternatives (§41).

A buffer references existing usable reserve/capacity. With stable positive net draw its endurance is reserve/net draw; changing demand/replenishment schedules new thresholds (§11). A reserve appears once even when several systems refer to it.

Redundancy names a real alternate provider/path, capacity, compatibility, activation requirements, delay and limits. A good roll cannot invent a backup. Switching can restore only supported functions; temporary manual traverse can leave propulsion intact while reducing tracking.

Substitution records original requirement, replacement method, conversion/preparation, inputs, competence, time, capacity, accepted quality, side effects and endurance. It can remove one bottleneck while introducing another. Routine valid substitution can proceed automatically within authority; a new player commitment remains a choice.

#### Dependency changes and cycles

Apply the initiating change once, evaluate directly affected functions, then propagate actual downstream changes at their causal times. Check each buffer/alternative before declaring an outage. One upstream failure can cause distinct later consequences without multiplying its physical loss.

Start requirements and run requirements may differ. A stopped generator and electrically powered fuel pump cannot bootstrap each other simply because both exist. A real battery, manual pump, gravity feed, external supply or other startup capability must break the cycle. An already running supported loop is not forced to restart at every review.

Process cyclic same-time derived updates to a stable, supported allocation without generating stock or work. If a physical feedback loop has growth, dissipation, delay or instability, the relevant profile must define it; a graph alone is not its physics. Unsupported cyclic activation stays unavailable.

**Acceptance:** no nonexistent redundancy, serial capacity not summed, shared reserves consumed once, causal startup required, only affected functions lost.  
**Calibration:** component performance, switching times, conversions, overload/failure mechanisms and buffer demand remain profile-owned.

<a id="core-102"></a>
### 102 Networks, Routes and Concurrent Flows

**Status/ownership:** Proposed Core promotion from PAF §§6.14/13 and both equipment/PA content interfaces.  
**Dependencies:** stock/assets, actors, commitments, dependencies and time.  
**Records:** node references, physical/information links, flow schedule, allocation and shipment manifest.

Nodes reference actual sites, organizations, depots, services or settlements. They own no duplicate stock. Links record endpoints, direction/modes, specification, capacity, travel/latency, access/control, condition, operator, required means, shared constraints and alternatives. A link can be open to people and closed to heavy freight. A radio link is not a road or political treaty.

A flow records source/destination, commodity/service/information, quantity/rate, schedule, route, actual transport/handling, reservations, losses, owner/authority and receipt conditions. A planned flow is not dispatch. Departure changes stock/custody and availability; receipt changes destination custody/stock; news changes recipient knowledge separately.

#### Capacity allocation

For a simple isolated chain, feasible throughput is bounded by comparable source, loading, transport/link, unloading, storage and distribution limits. Include travel, loading, unloading, rest/service and return where required. Vehicle payload multiplied by trips actually completed bounds delivered quantity; no return-free recurring trips.

For shared paths, do **not** add independent per-route minima as if every route owns the bridge, truck, driver or loading crew. Give each physical constraint one capacity budget over the interval. In comparable normalized units, allocations x obey **Σ aᵢⱼ xⱼ ≤ cᵢ** for each constraint i; coefficients state the actual resource/capacity used by each flow j. Source stocks and destination free space impose additional quantity limits.

Use actual prior reservations, agreements and authorized allocation policy. If no priority exists and the conflict matters, obtain/resolve that actor's decision; don't grant both flows full capacity or pick the protagonist's political allocation. Understanding the allocation requires no compulsory optimization roll. A larger network can use explicit feasible allocations without claiming a global optimum.

Unused capacity during a short interval does not guarantee later availability. Transit has travel time; delivery from one end of a route cannot occur immediately because throughput is high. Material and information schedules can diverge. Continuous services use §103 rather than pretending every unit is stored cargo.

A broken link leaves existing stock where it is. Recompute routes, departures, arrivals and forecasts; do not erase an institution, agreement or independent communication path. A backup must provide useful capacity with its own activation and bottlenecks (§101).

Shared hospital/education/repair capacity serves local and external users from the **same** provider budget. A referral/booking does not complete physical travel or treatment. A regional surplus without accessible links can coexist with local shortage.

**Acceptance:** shared-link budgets respected, cargo in one location, reports do not deliver cargo, path partitions preserve remote stock, incoming/outgoing flow cannot bypass latency.  
**Calibration:** geography, transport cycles, handling, modes, loss mechanisms and service conversion rates remain profile-owned.

<a id="core-103"></a>
### 103 Infrastructure Services, Startup and Commissioning

**Status/ownership:** Proposed Core promotion from PAF §7 and Military Life §§7–12.  
**Dependencies:** actual assets/components, actors/institutions, requirements, networks, stock and work.  
**Records:** service specification, users, demand, installed capacity, feasible capacity, allocation, delivery, dependencies, operating mode and acceptance.

An **asset** is physical equipment/facility; a **service** is useful function delivered to specified users through assets, operators, inputs and links. An intact plant may deliver nothing. A damaged plant may deliver a restricted service. Physical repair, operability, authority and actual delivery are separate.

Define service unit, accepted quality, geography/endpoints and required continuity. Enough unsafe water does not equal enough potable water; installed generation does not establish power at a disconnected building.

Compute feasible capacity from compatible stage capacities, people, inputs, access and dependencies (§101). Allocate within shared budgets (§102), then record actual delivered service over the processed interval. **Deficit = max(0, demand − actual delivered service)** in compatible units. A forecast or rated capacity is not actual delivery.

An unmet demand normally leads to curtailed service, priority allocation or a queue. It damages equipment only through a defined overload/failure mechanism. The authorized actor's existing policy determines curtailment; the protagonist chooses only within their authority. Downstream effects follow which actual users/functions were denied.

Operational descriptors—Available, Restricted, Offline, Isolated—and modes—Normal, Reduced, Emergency, Bypass, Shutdown, Commissioning—describe function/configuration, not physical condition levels. Failure can arise from an actual fault, lost input/staff/access, overload, control failure or network isolation.

#### Restoration and startup

Use applicable stages: assess → isolate/make safe → stabilize/bypass → repair/replace → test → commission → deliver service. Start/run dependencies and black-start capability use §101. A commissioning record states required test results, configuration, qualified operators, inputs, distribution, authorizer if applicable, restrictions and effective time.

Keep separate physical work complete, test passed, commissioned, service delivered and sustained support. A completed hospital building supplies no treatment without staff, equipment, utilities and care capacity. A repaired generator does not restore a broken distribution network.

A temporary workaround records function/quality, capacity, setup, people, inputs, cost, limits, endurance and termination. Restoring service by a portable generator is valid without claiming a permanent grid. Replacing old centralized service with a viable new topology can meet program acceptance; historical restoration is not the only solution.

Sustained service references maintenance, replenishment, staff succession and replacement capability (§107/§108). Confidence and source/last verification belong to assessments; supported true state and actor knowledge remain distinct.

**Acceptance:** actual end-user service rather than installed capacity, real startup path, buffer-delayed outage, partial backup, failed acceptance leaves a specific blocker.  
**Calibration:** service standards, capacities, quality tests, thermal/storage behavior and operator requirements remain profile-owned.

#### Useful operating configurations

The selected service profile states whether output is divisible, requires an essential simultaneous bundle, uses whole/exclusive slots or permits a supported reduced mode. The shared capacity inequality is necessary but insufficient: all essential roles, equipment, utilities and inputs must coexist for the declared configuration. Below an essential minimum, output is zero unless a supported reduced configuration exists.

Synthetic fixture: a capacity budget of 10 cannot run two indivisible services each requiring 6 at the same instant. One can run, leaving 4 for another supported use or unused. Queueing/sequential service is possible only through real available time; a fractional allocation does not supply a fractional indivisible operation.

Preparation and interrupted work can consume actual resources despite zero output. Interruption/restart costs and harms need their own profile mechanism; there is no automatic refund or generic damage. Qualified substitutes can cover a missing operator within unchanged station/parallel caps. Installed, feasible, allocated and actually delivered capacity remain different states.

<a id="core-104"></a>
### 104 Sites, Discovery, Recovery and Resource Sources

**Status/ownership:** Proposed Core promotion of PAF §6's neutral mechanisms and Fantasy exploration/resource interfaces.  
**Dependencies:** places, actors, inventory, information, access, projects and transport.  
**Records:** site/area, underlying resources, actor knowledge, claims/control, installed assets and recovery activity.

A site records location, original/current function, layout/access, structure, occupants, hazards, stock references, installed systems, links, claims, resource history and last change. Original function constrains plausible content; it guarantees none. Establish supported underlying content/potential before resolving discovery. If world detail must be generated, record its rationale/provisional status independently of the search roll, preserving it for later visits.

Keep distinct **exists → known → accessible → recoverable → transportable → usable**. These are questions, not obligatory sequential levels: an object can be usable but inaccessible. Knowledge descriptions—Unknown, Reported, Located, Observed, Surveyed, Mapped—are observer- and area-specific. Cleared/security status and control are separate; a secured building may have an unmapped basement.

#### Recovery work

Use applicable activities: discover/survey → access/search → recover/extract → inspect/process → transport → store/install → accept/repurpose. Define target area, objective, method, personnel, tools, time, handling, transport, exposure, claims and commitments. Routine qualified recovery is work; genuine uncertainty uses the selected adapter. Finding a generator completes neither lifting nor transport nor commissioning.

Search success yields evidence/objects within the method's actual reach and the persistent world state. Excellent search at an empty store yields no stock; failed search at an established cache leaves it there. New method, access or authorized coverage can support further search; unchanged rerolls cannot generate a new inventory. Other actors can recover or consume the same finite stock off-screen.

Recovery/deconstruction transfers material from the source, changes remaining source function/condition, and records outputs, waste, custody and acceptance once. Cannibalizing wiring or a required component can reduce the donor's future capability. Unassessed, contaminated, damaged or incompatible recovered items do not become accepted usable stock by being found.

Depletion is recorded by exact known quantity or a descriptive assessment of resource category and area. Untouched, Disturbed, Picked Over, Stripped and Salvage Exhausted are optional recovery assessments, not automatic global stages. Stripped portable stock can coexist with valuable installed machinery. New supply needs production, delivery, renewal, incoming stock, new access or corrected knowledge.

#### Source types

Finite stock depletes without inherent renewal. Renewable sources replenish only through their actual biological/environmental process. Productive sources transform inputs through capacity and time. Legacy recovery retrieves prior output. Forest is not lumber, seed is not harvest, ore is not a finished part and a well is not refined fuel.

**Acceptance:** no loot creation, failed discovery preserves hidden facts, repeated visits preserve depletion, extraction needs handling, source loss reflects salvage.  
**Calibration:** search coverage, local history, extraction, processing, renewable rates and seasonal ecology remain profile-owned. Crisis-specific legacy-scarcity assessments stay with PAF.

<a id="core-105"></a>
### 105 Containers, Handling, Carrying and Storage

**Status/ownership:** Proposed Core promotion from PAF §6.13, Military Life §§4/7/11 and the content libraries.  
**Dependencies:** assets/stock, actors, profiles, access, work and transport.  
**Records:** container/contents references, mass/volume/shape, handling profile, storage requirements and exposure history.

Container capacity, actual contents, compatible uses, condition, closure/security, protection, portability, access and location are separate. One item/stock has one physical container/location. A container inside another forms an acyclic containment tree; moving its parent moves the same referenced contents. A manifest or parent total is a view, not another quantity.

Where mass matters, loaded mass is tare plus actual referenced contents, recursively without counting an already-loaded child total again. Keep mass, volume, count, dimensions and strength/load limits separate. A liquid-volume conversion needs density/specification; a stock estimate and its later expanded item detail must reconcile.

Lifting, sustained carrying, loading/unloading, securing cargo and transport differ. Check load, bulk, shape, fragility, packaging, available handlers, equipment, openings/access, ground and vehicle/storage limits. A person who can momentarily lift a machine may not carry it all day or fit it through a doorway. A strong operator supplies no missing hoist or container.

Select one carry/encumbrance profile: kilograms with a physiological capacity, slots defined by a packing model, or another explicitly adopted system. The fantasy Strength formula and historical slot fixture are incompatible defaults until mapped; do not apply both penalties. Bulk/distribution can matter as distinct mechanisms only when not already built into the selected load state.

Storage requirements specify compatible container, dryness, cleanliness, temperature, security, sealing, pests or preservation where relevant. Shelf dates, packaging damage, contamination and actual spoilage are different states. An elapsed date does not independently certify usability or physical loss.

Loss of refrigeration initiates the profiled temperature/exposure process at its actual time. It does not instantly destroy every stored item. Different batches can have different exposure histories. Protection only addresses its declared contaminant/route; pumping, filtering and purification are distinct functions.

Contamination records source, affected stock, detection, route, isolation, processing/disposal and accepted use. Usable quantity may fall while physical volume remains. Treatment can restore a permitted use only through an actual compatible process and its costs; it does not necessarily remove structural damage or every hazard.

**Acceptance:** no nested inventory duplication, no kg/litre interchange without conversion, handling distinct from payload, no instant spoilage from a mode label.  
**Calibration:** capacities, dimensions, carry limits, packaging, storage exposure and condition changes remain profile-owned.

<a id="core-106"></a>
### 106 Population, Presence, Movement and Membership

**Status/ownership:** Proposed Core promotion from PAF §§8–9 and Military Life personnel/household continuity.  
**Dependencies:** actors/cohorts, places, needs, stock, commitments, knowledge and institutions.  
**Records:** individual/residual cohort, movement event, household links, location and separate membership/assignment states.

At a location, living population = individually represented people present + unexpanded people in residual cohorts present. Named records are removed from their source cohort; cohorts split when different location, custody, condition, skills or decisions require it. Do not count the aggregate and its expanded members together. Historical deaths and bodies can remain records without being living residents.

Keep separate physical presence, recognized residence, service eligibility, political/institutional membership, work assignment, condition and duty availability. Arrival does not create citizenship, communal ownership, military service or productive labor. Departing a place need not immediately terminate membership or ownership.

#### Movement event

Record people/households, origin, destination, purpose/cause, authority/agreement, departure, route, transport, ETA/actual arrival, condition, cargo/ownership, information and status. At departure remove presence from origin and establish transit; at arrival change actual presence and local demand. Travel, care, supplies and custody continue en route. Death, birth and other real population changes use the appropriate profile/events rather than unrecorded demographic percentages.

On arrival process only applicable reception, safety, health/hazard assessment, shelter, registration, claims, skill evidence, service access and role decisions. Emergency sequences may vary. Demand begins at actual arrival, not at administrative acceptance. Private food, tools or vehicles remain private until a real transfer.

Usable work depends on condition, capacity, care duties, willingness/obligation, qualifications, means, assignment and existing commitments (§10). Total population is not workforce; an exhausted injured specialist can possess expertise while being unavailable for a particular task. Claims of skill can be verified through credentials, history, interview, demonstration or supervised work appropriate to the context.

Integration is multidimensional: housing, language/communication, service access, duties, relationships, legal status, education and participation. No universal integration meter is required, and no preferred intake or political policy is imposed by Core.

Departure updates actual presence, carried property, assigned roles, service demand and capability at its real time. Shared assets do not automatically depart with a member. Arrival information is limited to actual witnesses, records, expertise and rumors; it is not omniscient knowledge of the origin.

**Acceptance:** people in one physical location at a time, transit retained, named expansion preserves total, immediate arrival demand, private property preserved, no instant labor unlock.  
**Calibration:** needs, habitation, local membership rights, roles and demographic processes remain profile-owned; displacement/crisis policy belongs to the genre/context.

<a id="core-107"></a>
### 107 Institutional Functions, Authority and Continuity

**Status/ownership:** Proposed Core promotion from PAF §10 and Military Life §§5–6/12–15.  
**Dependencies:** actors, commitments, means, information, work, resources and social/economic records.  
**Records:** organization, function/office, staff assignment, workload/backlog, authority, procedures, succession and knowledge continuity.

An institution records purpose, functions, jurisdiction, authority basis, recognition, leadership, staffing, facilities, resources, procedures, records, communications, dependencies, commitments, accountability, internal factions, relationships and succession. A department name supplies no staff, tools or authority.

For each function record required authority, qualified people, facilities, resources, information, procedures, workload, feasible capacity, actual output and bottlenecks. A town can retain water administration while courts are suspended. Operating, Degraded, Suspended, Fragmented, Displaced, Reconstituting, Dissolved and Successor are scoped descriptions, not global levels.

Keep **authority** (recognized right), **capability** (practical ability), **recognition/legitimacy** (acceptance by relevant actors) and **control** (actual administration/enforcement) distinct. Title does not produce expertise or information; local control does not automatically establish lawful/accepted authority. Social/legal profile determines rights, not a generic Core decree.

#### Work and commitments

Institutional duties use §10. Workload/backlog has compatible units and actual priorities. In an interval, backlog increases by newly admitted work and decreases by work actually completed/cancelled/transferred as applicable; a review adds no duplicate arrivals or completions. Demand beyond capacity can cause queue, delay, triage or reduced scope. Busy staff do not randomly fail unless a real mechanism creates meaningful uncertainty.

Handover identifies actual successor, authority, custody, records, outstanding tasks, known hazards and communication. A recommendation, qualification, appointment, active assignment, award and payment are separate states with effective times. Allegation, evidence, institutional finding and sanction also remain distinct; success is not immunity, and a low roll is not proof of misconduct.

#### Formation, succession and expertise

Formation needs actual purpose, participants, agreement/authority, roles, resources, procedures, information and communications. Institutions need not use modern or democratic structures; the profile supplies context. Missing premises remain explicit.

Succession records trigger, office/person, selection, effective authority, access/resource control, documents and communications. A valid replacement can preserve function after leadership loss; naming one cannot cure missing access or competence. A displaced institution can continue from another site while maintaining history and claims.

Expertise continuity references capable people, substitutes, documentation/media, access, tools, demonstrations, training pipeline and single points of failure. Manuals retain information without automatically training a replacement. A successor may inherit some people, functions, facilities or records without inheriting every debt, treaty or legal identity.

**Acceptance:** no capacity from titles, staffing hours finite, backlog conserved, leader loss not automatic deletion, records distinct from skill.  
**Calibration:** law, jurisdiction, workload units, service targets, appointments, recognition and succession terms remain profile-owned.

<a id="core-108"></a>
### 108 Technology Support and Productive Capability

**Status/ownership:** Proposed Core promotion from PAF §11 and Military Life §§10/12/14.  
**Dependencies:** actors/institutions, assets, knowledge, inputs, services, projects and networks.  
**Records:** capability assessment with scope, location, responsible people, evidence, facilities, dependencies, rates and uncertainty.

| Assessment | Evidence required within named scope |
|---|---|
| Possessed | Actual example available |
| Operable | Functioning example, suitable operators, inputs and environment |
| Maintainable | Routine service knowledge, access, tooling and consumables |
| Repairable | Ability to diagnose/correct named substantial faults |
| Part-fabricable | Accepted replacement parts of named specifications |
| Reproducible | New accepted examples from a real supply/production chain |
| Industrialized | Repeatable accepted output at stated useful rate and support |
| Developing | Actual research/test capacity for adaptation/improvement |

These are independent scoped assessments, not a level ladder. A workshop can reproduce casings while importing controls, or study an artifact it cannot operate. A technology-family label does not make every variant reproducible.

Record current people, documents, tools/facilities, power/infrastructure, consumables, suppliers, output specification, throughput, bottleneck, evidence and review. Reassess when a sole expert, external supplier, asset or access changes. Existing equipment does not vanish when replacement capability falls.

#### Production and acceptance

Use §73 projects and §109 rate accounting. Define input quantities/specifications, conversion/yield, equipment/process, qualified capacity, work/time, intermediate products, waste, inspection and accepted output. Consumption and output occur at their real stages. Unharvested crops or incomplete products can exist as work/state while not yet usable stock.

A successful prototype establishes only its observed performance in tested conditions. Reproduction needs materials, tooling, drawings/process knowledge, trained staff, service, supply and quality control. Useful production rate and durable support require further evidence. Documentation can be copied with appropriate media/work without being a conserved physical stock of knowledge; copies do not grant skill.

Current sufficiency and long-term replacement dependency are different axes. A service can be locally supplied today while dependent on imported or irreplaceable-known controllers. Reserve-only, recovered-stock, imported, local and network-supplied are source descriptions; reproducible, partly dependent, legacy-dependent and irreplaceable-known are replacement assessments. None impose a generic penalty beyond their actual bottleneck.

An improvement changes only supported mechanisms. No automatic tech-tier upgrade changes every service or actor. Routine accepted production remains automatic; uncertainty attaches to actual new methods, access, quality problems or hazards. Production cannot consume reserved conflicting stock or exceed shared labor/facility capacity.

**Acceptance:** possession distinct from reproduction, prototype distinct from fielded production, partial fabrication scope retained, expert loss changes capability without destroying assets.  
**Calibration:** process yield, throughput, tooling, skills, quality and support requirements remain profile-owned.

#### Information, expansion and support assessments

The crossover XO-06 terms add distinct scoped questions without replacing the existing maintenance/repair/fabrication distinctions:

| Assessment | Required scoped meaning |
|---|---|
| Understood | Relevant technical information has been received/accessed and comprehension is supported to the stated scope; accessible documents alone do not establish practical competence |
| Scalable | A supported expansion plan can increase accepted throughput to the named target using actual additional inputs, staff, tooling, workspace, networks and operating support |
| Supportable | Real upkeep, replacement, staffing, knowledge and supply arrangements can sustain the stated service over a declared horizon, with evidence and uncertainty |

Maintainable addresses routine service; repairable addresses named substantial faults. XO's shorter wording about repair/support does not collapse these different capabilities. Industrialized means repeatable accepted output at a stated useful rate; scalable concerns a feasible increase beyond current capacity. An organization can possess one without the other.

Present usable delivery and renewal/replacement viability are independent axes. Assess the latter through maintenance inputs, qualified substitutes, documents and understood methods, spare parts, fabrication/reproduction, accepted external supply, routes and responsible institutions. Reliable import arrangements can support sustained service without local self-sufficiency. Unknown replacement capability is unknown, not absent. Losing local fabrication does not immediately damage a functioning machine; present and forecast states carry source/confidence and time basis.

#### Cross-domain capability impact assessment — CW-SSN-06

On introducing or materially changing a capability with plausible consequences beyond its immediate user, use a derived assessment: `capability/mechanism reference, actual access/practitioner/device population, prevalence and skill distribution, costs/output/repeatability, duration/persistence, infrastructure/training/support, countermeasures, relevant domains, observed adoption and uncertainty`. The assessment references existing facts; it has no additional production, population or treasury balance and no universal impact score.

Establish the demonstrated function and who actually can use it. Check available actors/devices, sustainable inputs, throughput, reliability and support. Compare real alternatives and effects on existing service chains. Actors/institutions adopt only through their actual information, incentives, authority, finite investment/training/work and acceptance. Update affected actual capacity only after those changes occur. An unadopted possibility changes forecasts and knowledge, not everyone's services.

Preserve regional/social variation. A water-creating method's existence does not prove sufficient useful quantity, quality, frequency, storage or distribution. Healing, automation, remote observation, transport and fabrication can alter MED/ECO/URBAN/CIV/INTEL/WILD and other domains when their supported adoption actually occurs. The workflow neither automatically improves civilization nor forces stronger opponents, regulation or crises.

<a id="core-109"></a>
### 109 Operating Stocks, Rates, Power and Bounded Burdens

**Status/ownership:** Proposed Core promotion from Military Life §8 and PAF resource/service/buffer procedures.  
**Dependencies:** stock, components, activities, events, profiles and allocation.  
**Records:** resource units, rates/modes, discrete costs, capacity, source/recovery, thresholds, interlocks and processed interval.

For stock S over a processed interval Δt with supported constant rates:

**S′ = S + actual receipts + (actual production rate − actual consumption rate) × usable Δt − discrete actual costs − actual losses/outgoing transfers.**

Split at deliveries, failures, mode changes, threshold crossings and exhausted inputs. Do not extrapolate negative stock and then clamp it to hide infeasible work. Discrete activations are charged once at their execution time; a rate that already includes that activation cannot debit it again. Conservation covers transfers and specified transformations; creation/recovery of a resource requires a real producing mechanism or explicitly enabled exceptional rule.

#### Energy, power and output

Stored energy, power/output rate, fuel, coolant and ammunition are different quantities. Available energy does not guarantee sufficient instantaneous output. Demand from simultaneous modes must fit current output plus an actual compatible buffer's permitted discharge; duration must also fit stored energy/fuel and recharge limits. Essential loads are counted alongside optional loads.

Load selection follows actual interlocks/policy or operator choice. Over-capacity demand normally makes the combination unavailable or curtailed, not automatically damaged. Exceptional operation needs a defined override, resources, duration, displaced functions and stress/failure consequences. It cannot be obtained from a favorable action roll.

Recharge/replenishment has source, rate, usable interval, free capacity and actual cost. Surplus production without storage/distribution does not provide later service. A leak consumes stock through its profiled rate; refilling does not repair the fault. Cooling capacity is not consumed unless its mechanism spends something.

#### Bounded operating burdens

Heat, pressure, charge, accumulated exposure or another burden may use a common threshold procedure when a module defines units and behavior. They are not physically interchangeable. Record baseline, initial value, generation by mode/action, dissipation/recovery, warning/limit, consequences, detection, interlocks and override rules.

For a discrete burden b at activation, evaluate **peak = current + b** before later recovery. For a continuous profile use its net rate to find the earliest threshold; stop/reassess there. Constant cooling without further generation can use **H′ = max(baseline, H − cooling rate × Δt)**. Do not silently clamp an excessive peak below a safety limit.

A known interlock blocks a prohibited activation before ammunition/energy for that activation is spent. Actual assessment or manipulation still consumes declared time. If an override is permitted, the operator must actually choose it; consequences are fixed beforehand. Warning does not universally mean explosion, and successful execution does not erase known heat/stress costs.

Physical/tissue recovery does not automatically refund a different expended resource or authorization. A module explicitly defines resource restoration and prevents repeated refunds or sacrifice/healing loops from generating undefined power.

**Acceptance:** no stock below zero, no activation counted in both discrete and rate costs, stored energy distinct from output, peak checked before cooling, blocked action no phantom expenditure.  
**Calibration:** operating/dissipation rates, units, limits, buffers, resource conversion and exceptional output remain profile-owned.

#### Process-law and review invariance

Configure an update law, units, causal interval or continuous-time interpretation, thresholds and retained processed boundaries/spans for every burden, financial, biological or renewal process. Use §11's frontier. A real scheduled policy review can change future behavior; presentation reviews cannot become extra growth, interest, mortality or cooling events.

Preserve unchanged input/outcome spans under finer/coarser display. Numerical approximations declare supported tolerance and convergence evidence. Ending an input stops future contribution without erasing accumulated burden or an already initiated downstream process. Each condition/process keeps its own persistence and recovery requirements.

#### Model envelope and derived capability

Before a material numerical or qualitative projection, bind its source/version, applicability, actual input state and as-of time, units/time basis, assumptions, supported process law and validity envelope under §112. A nominal or authored operating envelope is not proof of behavior outside its scope. A table label is not a solver.

Distinguish stored inputs, rates, actual output and derived capability. Endurance, range, carrying forecast and delta-v are consequences of supported current state/model; do not debit them alongside the stock whose consumption already changes that capability. A supported resource model may itself define a genuine abstract stock, but its units and conversion semantics must be explicit and cannot coexist as a duplicate charge for the same cause.

Use the earliest real mode change, depletion, contact, completion or threshold. A numerical implementation declares its method, event detection and tolerance where consequential. Recompute projections after changed configuration or inputs without erasing processed history. Model invalidity blocks only the dependent prediction/action; it creates no unrelated catastrophe or retroactive refund.

#### Actor-bound pools, throughput and burden — CW-SSN-02

A bounded capability resource binds `identity, authoritative owner field, current/max quantity, units, permitted uses, access/transfer policy, replenishment law, output/throughput constraints and evaluation interval, burden/threshold rules, rearm policy, recovery and source profile`. Choose the existing K-ACTOR/K-ASSET/K-STOCK owner appropriate to its actual meaning; never copy the same quantity into a second pool.

Stored quantity, physically achievable throughput and safe operating threshold differ. A hard output limit remains a feasibility bound. Exceeding a safe threshold requires the profile's actual permitted exceptional operation, authorization, costs and consequences; a large pool alone supplies none of those. Expenditure and incurred burden are separate causes when the profile defines both, without duplicate charges.

Record one-time threshold application identity and the declared interval/episode or rearm condition. A repeated display or later expenditure in the same interval cannot repeat an already-fired one-time consequence. A genuine rearmed exposure or continuing rate effect follows its own supported law; this does not exempt repeated harm from §17 reassessment. Interruption preserves spent quantity and actual burden. Nontransferable actor resources are not ordinary inventory; transfer/recovery needs its own enabled mechanism. No universal energy meter, chakra formula, stamina scale or burden threshold is introduced.

#### R3 proposed actual work and discrete output evidence

A production recipe or operating profile binds input/output units, process duration, worker and worksite qualifications, supported capacity, required equipment, physical inputs, stop/interrupt conditions, and declared synthetic or calibrated coefficients. A work reservation is not consumption and a forecast is not output. Completed work or an interruption settlement may commit only actual elapsed work and used inputs once; usable products appear only upon the selected process's output/acceptance event. A discrete batch whose yield is not safely proratable must specify work-in-progress, spoilage and partial completion rather than assuming linear fractionated output.


#### 109.R5 — Work interruption from unexpected stock losses (PROPOSED)

If a material loss invalidates an active job's previously qualified inputs, record the loss separately from workplace consumption and preserve the job's underlying input claim. Suspend precisely those activities whose mandatory prerequisites are no longer backed; do not terminate unrelated qualified work. Settlement after disruption requires the selected production law to account for **work genuinely performed before interruption**, committed input consumption, usable partial output, wages and time already elapsed, as distinct from remaining work. Do not credit planned full output simply because the original completion time arrived. If the selected model cannot determine partial production, carry an unresolved progress state rather than assigning guessed rates.

The bounded R5 job adapter freezes output for affected jobs and stores the pre-loss reservation claim, but does not implement fair reallocation, partial-progress credits or restoration. Those omissions are explicit acceptance blockers, not zero-valued accepted outcomes.

#### 109.R6 — Divisible work, partial acceptance, interruption and resumption (PROPOSED)

**Process choice:** A divisible-work model defines useful milestone boundaries, input/output mapping, units, time basis, staff and facility capacity, inspection or acceptance, losses/rework, tolerances and stop conditions. A batch process may yield **no accepted output** until its actual acceptance threshold; a genuinely continuous process may commit partial accepted output earlier. Do not automatically convert either into a universal linear labor-output law. Unsupported rates and partial-output evidence leave output unresolved, while actual consumption and safe interrupted state remain recorded.

**Canonical records:** `job_id`, origin work contract and parties, selected process/profile/version, deliverable and quantity, planned versus certified worker-hours, actual worked intervals and any unassessed elapsed interval, worker/site/capacity references, accepted milestone IDs, inputs physically consumed, surviving/freed input backing, usable output accepted, waste/loss, contractual wage basis, wage_due versus cash_paid, outstanding performance claims, interruption cause/occurrence time, eligible continuation predecessor/successor, and settlement authority/decision evidence. Records use K-WORK, K-STOCK, K-TIME, ECO and K-ORG owners; they are not duplicate physical ledgers.

**Settling interruption:** Count genuine completed work once and retain any unassessed time as an explicit evidentiary/entitlement question. Pay accrual for verified time only where an applicable selected agreement authorizes that basis; zero accepted output does **not** universally mean zero earned wages. Lost output, partial workmanship, rejected goods, already expended material and compensation need the selected employment/production rules. Work cancelled by a party, paused by a fire and voluntarily resumed by a qualified party are different event categories. When full work is later accepted, record its source and mark the original claim fulfilled by a traceable continuation without editing the interruption history.

**R6 bounded adapter:** `start_tracked_job → record_work_milestone → [physical_loss/suspension] → settle_disrupted_job → actual dispatch/receipt + renewed commitment → start_continuation → record_work_milestone → finalize_tracked_job`. It only demonstrates explicitly bound integer-rate synthetic recipes with asserted external evidence, mostly one worker. An unauthenticated text reference cannot serve as a secure real-world proof. A simultaneous full scheduler implementation, independent runtime and alternate nonlinear/batch process are future acceptance gates.

<a id="core-110"></a>
#### 109.R7 — Qualified intermediate manufacturing and recovery (PROPOSED)

A production profile SHALL explicitly identify input types/quantities, intermediate types/quantities, acceptable completed output and the applicable salvage or waste model. Inputs are consumed when the qualified operation actually occurs; intermediate output enters physically owned stock only through that event. Intermediate units remain separate from final production until an inspection and valid acceptance operation. An inspected rejection produces no finished article automatically. Scrap or salvage is a later material transformation with actual resulting quantity and its own source.

Each workpiece instance snapshots the selected profile revision at its source event, protecting historical yield and quality requirements from future profile edits. Any nonlinear, fractional, multi-stage, quality-dependent or labor-dependent process requires an appropriately calibrated specialist adapter; the R7 integer fixed-yield fixture is not a universal manufacturing formula. Do not charge labor, time, energy or disposal costs without applicable selected rules; an omitted cost is an explicit calibration/coverage gap, not proof that the activity is free.

### 110 Institutional Learning, Revision and Fielding

**Status/ownership:** Proposed Core promotion from Military Life §12 and Fantasy/PA research and continuity mechanisms.  
**Dependencies:** events/evidence, information, actors, institutions, work, resources and content versions.  
**Records:** lesson, hypothesis, trial, authorization, acceptance, revision, dissemination and actual fielded state.

An incident creates bounded evidence, not a universal upgrade. Record origin event, witnesses/data, conditions, uncertainty, interpretation, problem, proposed response, sponsor, means, criteria and recipients.

Useful gates are **observation → review → trial authorization → trial → adoption → distribution → fielding**. They describe distinct accomplishments, not a compulsory slow sequence for every change. A known routine correction can take the applicable short path; an urgent precaution can be justified without proving a final explanation.

Observation requires actual recipients. Review distinguishes explanation from evidence. Trial needs authorized people/means, scope, risk, criteria and time; failure can produce usable findings without useful equipment. Adoption records the authorized procedure/design version. Distribution sends actual information or equipment. Fielding requires installation, trained use, tests and support where applicable.

No gate automatically completes the next. Signing a doctrine revision does not retrain a unit. Owning a new device does not authorize or qualify its user. Sending instructions does not guarantee receipt or successful implementation. A locally effective improvisation may remain local until relevant actors learn and assess it.

State each revision's capability, requirements, costs, mass/space, maintenance, manufacturing, staffing, learning and failure changes where relevant. Record unchanged values explicitly where justified. Preserve old configurations until actually updated; migration does not rewrite old events.

Institutional learning survives an individual through records, capable instructors, recipients, facilities and recurring resources (§107/§108). Other actors learn only through plausible observation, communication, capture, exchange or research. They do not adapt merely because the protagonist succeeded.

**Acceptance:** data distinct from hypothesis, adoption distinct from trained use, failed test preserves evidence, no instant global fielding.  
**Calibration:** trial duration, instruction, production/installation and institutional authorization remain profile-owned.

<a id="core-111"></a>
### 111 Content Identity, Composition, Binding and Instances

Core Systems supplies behavior. The separately versioned Shared Content Library supplies reusable definitions and source-backed content references. Genre/theme libraries supply specialized mechanisms and profiles. Campaign State holds actual things. The twelve catalogue collections remain retrieval namespaces, not additional runtime domains.

#### Exact release identity and aliases

For this package pin `IRGS-SCL-1.0` and resolve `(namespace, family ID, exact revision, selector, semantic type)`. Its family proposals use `SCL:<stable PBC family handle>@0.2`; this is a receiving-release reference convention, not automatic global canonical assignment. The exact registry reconciles all 286 neutral source rows, 279 family candidates, 304 source references, and the separately added craft-exhibition template. The counts describe different units.

Version-pinned `PBC-…@0.1`, original `FL/PL:<ID>@1.0`, and legacy `SCL:<ID>@0.1` aliases resolve through the published crosswalk. Both central and definition-local records must agree on target, revision, type, selector and target content checksum. An unqualified display name, a later revision, a family-only label or a missing selector does not authorize substitution. Do not resolve by last attached file, favorable value or unchecked “latest.”

A sword's cut and thrust aliases select different methods on the same physical-family definition. They do not create two swords, two attacks or a second quantity. Unarmed `WPN-M-001` is a **method**, with an explicit correction of Pass B's broad weapon classification; its native numerical profile is preserved, but it is not an inventory asset. Coverage, behavior, natural delivery, information, services, institutions, projects, hazards and movement templates likewise retain their proper record kinds. An institution may have actual organizational state through K-ORG; its catalogue definition is not a stock lot.

Each definition states purpose/type, provenance/status, pinned parents, supported functions, activation requirements, limitations, owner/domain interfaces, model dependencies, maintenance/acceptance and unresolved calibration fields. Typed relations such as requires, hosts, operates, supports, is_a and may_use are not interchangeable inheritance or identity relationships.

#### Composition

Resolve the exact parent closure. Inheritance must terminate; missing versions, cycles or unresolved parent conflicts make the dependent definition unresolved. A variant records explicit field operations:

| Operation | Meaning |
|---|---|
| No override | Inherit the pinned field and its source/model status |
| Set supported value | Replace with the declared value/source, including a known zero |
| Set unknown | Replace an inherited usable value with unknown; no fallback |
| Mark not applicable | The field does not apply; this is neither zero cost nor free capability |
| Remove | Remove the field/capability and revalidate dependent functions |

Multiple parents require an explicit coherent composition and conflict decision. Do not sum complete protection profiles, capacities or modifiers merely because definitions are attached. Construction, coverage, material, condition and quality remain distinct. Composition produces a definition/configuration proposal; modifying an actual object requires authorized work or an explicit prospective migration.

Distinguish three graph cycles: definition inheritance must have a resolved base; physical dependency loops may operate with real startup/running support; citation cycles create no new originating observation. Use each owning procedure rather than a blanket graph rule.

#### Three content readiness gates

| Gate | What it establishes | What it does not establish |
|---|---|---|
| Reference | Exact identity, semantics, selector and source/profile preservation | Installed capability or calibrated performance |
| Activation | Actual compatible means, access, model and material parameters for the task | Global acceptance or removal of source definitions |
| Deprecation | Complete replacement, adopted scope and fact-preserving migration | Retroactive repair, new gear or rewritten history |

Pass B's **51 complete selected qualitative contracts** are retained. **228 family candidates** remain source-backed holds, corresponding to **235 original source references**. **18 specialized source records** stay in their genre/theme/profile scopes. All 61 Fantasy adapter records and all 420 original payload blocks remain available in the SCL v1.0 registry, with immutable @0.2 record revisions. Adding an alias, a schema or the SCL description does not upgrade a held replacement.

A slim engine can bind shared procedures to Core 3.2 while using an exact preserved source definition/profile for held content. This is a content dependency, not a requirement to run an older generic Core algorithm in parallel. The reference states one of: selected shared contract with a native adapter; exact source-backed content; or retained scoped extension. Unsupported dependent calculations remain unresolved. Independent supported actions continue. Quantitative calibration is separately tracked; a qualitatively supported task does not require invented precision.

#### Actual instances

| Mode | Required behavior |
|---|---|
| Starting initialization | Source-supported facts or authorized generation policy, exact scope/identities/quantities/provenance; do not recraft established objects from present stock |
| In-world creation | Actual authorized work, prerequisites, finite inputs, transformation/output/waste, elapsed time and acceptance |
| Migration/rebinding | Preserve identity, quantity, location, title/custody, condition, obligations, competence and history; apply only the declared prospective mapping |

Definition lookup, composition, aliases, tests and scale changes create no objects, money, people, services, rights, evidence or completed work. Initializing or producing an actual item uses campaign-scoped event identity; exact replay is a no-op, changed payload under an applied ID is a conflict. Assembly cannot duplicate donor components.

Bind actual actor/asset/site, configuration, geometry, control/body interface, location, access, means, staffing/time and the compatible selected profile. An absent outcome-changing parameter blocks only its dependent calculation. Unknown, not applicable, unsupported, known zero and measured zero preserve their meanings. A broad material, era or category supplies no model mass, price, treatment efficacy or engineering rate.

Preserve asset/service/institution; material/product/stock; weapon/mode; anatomy/learned behavior; source/recovered output; and program/actual project distinctions. The catalogue remains a read-only reference; the nine state owners remain authoritative.

<a id="core-112"></a>
### 112 Module Contracts, Compatibility and Adoption

**Purpose/status:** General receiving interface carried from the current selected Core v3.2 workshop parent, maintenance R3. This v3.3 text is a **proposed candidate only**; the R3 binding remains active unless separately replaced after acceptance. It reconciles source dependencies without adopting campaigns or certifying every implementation. **Owners:** existing state owners plus the relevant domain. **Records:** release/engine manifest, ownership register, task/model binding, selected profiles, explicit overrides, compatibility decisions and migration snapshot.

#### Required extension manifest

Pin engine/module ID and version, Core ID/version, source status, required Core services/domains, owned extension records, read/write owner addresses, consumed events, produced changes, triggers/intervals, selected content/aliases, model/parameter profiles, units/validity, access/detection, exceptions, termination/recovery, acceptance cases and unresolved requirements. Only material fields need initialization. A trigger subscribes to an event; it does not apply the underlying loss a second time.

The **selected v3.2 historical binding** carries seven engine/library records covering Fantasy, Military, Apocalyptic, Roman, Historical Life, Space and Sports, plus the CW-SSN extraction-only record. In this **unselected v3.3 proposal**, the general military capability is Core MIL §124; the old Military receiving record survives as source/compatibility data and must be reconciled prospectively, not assumed valid under the candidate bytes. Sports remains a library/module binding to COMP rather than an additional new domain. SSN's native numerical rules, catalogue and setting remain outside Core until separately qualified. The proposal contains **twelve Core domains and the same nine authoritative K-state owners**; all selected v3.2 binding records are unchanged until a future explicit rebind.

#### Receiving compilation

1. Select the exact adopted Core (currently v3.2), engine/module, library and profile versions. Only select the proposed v3.3 after explicit acceptance, receiving rebind and source checksums. “Newer” alone does not mean adopted or compatible.
2. Resolve every required shared function to its named Core provider. In this receiving deployment, Framework v2.1, v2.2, CDI and extraction patches are provenance for shared procedures, not additional runtime rule stacks.
3. Retain native genre/application records and complete local numerical chains. Record field-level overrides and their scope. An old source paragraph labelled Core refers to its original parent unless this binding explicitly relocates it.
4. Select one compatible effect, resolution, needs, load, recovery, learning, movement and other material model per represented cause. Historical 4-hour TU and Fantasy nominal 20-hour TU are different schedules; store actual hours and evidence. Roman's 35/30/35 ordering is a scoped three-way priority profile, not a replacement for d100 action bands or all Core ordering.
5. Resolve catalogue references through §111. A held definition uses its exact preserved original payload/profile; it cannot activate an incomplete shared replacement. Native profile dependence does not reintroduce a duplicate clock, stock, injury, work, service or population ledger.
6. Bind actual owner-qualified records, means, access and material parameters. Validate applicability, units/time basis, model envelope, invariants and event frontier. Unknown parameters remain explicit; routine supported qualitative functions proceed without filler measurements.
7. Run relevant receiving and engine cases. Record specification compatibility, implemented-case results, calibration and live playtests separately. Finalize the slim engine only when its declared scope has no missing shared provider, lost native function, duplicate owner or unresolved outcome-changing default.
8. Record design/campaign adoption separately, with effective scope/time. Existing campaign rules prevail until the selected prospective migration; source publication and a passed schema do not perform adoption.

#### Slim-engine contract

A finalized slim specification contains its extension/application procedures, selected local profiles, content references, actual-state interfaces, initialization/runtime entry points, exceptions, acceptance cases and migration. It inherits §§5/11/90/91 and domain providers directly. It repeats neither the shared loop nor duplicate stock, wounds, work, population or capacity totals.

“Finalized” identifies a complete versioned specification at its declared scope. It does not mean accepted in every campaign, empirically calibrated, balanced, independently reproduced or live-playtested. A finalization record lists remaining context/profile choices and which supported qualitative fallback is permitted; it cannot hide a missing rule as a runner's discretionary invention.

The Core can be used without the entire library loaded. At runtime retrieve the selected engine, relevant task/content/profile bindings and supported current state. Previous source texts need not remain open for shared rules. A native profile reference must still resolve to its complete applicable rule, either embedded in the slim engine or included as a pinned adapter; a title or checksum alone does not supply missing procedure text.

#### Binding and model validity

A material model binding states ID/version/status/source; supported activity and target/configuration; authoritative input/output owner fields; units and time basis; initial/as-of state; assumptions and valid envelope; lawful qualitative/equation/update method; uncertainty/measurement interpretation; thresholds; stop/recovery conditions; and, when numerical, solver/tolerance/event-detection requirements. It is a procedure/profile binding, not another world-state ledger.

Forecast output, measurement and actual state stay distinct. A model that computes endurance, range or delta-v provides derived capability, not an additional spendable stock. Changed initial state, configuration, units, assumptions or model validity requires reassessment before dependent execution. An invalid forecast does not itself move a ship, injure a person, empty fuel or retrospectively invalidate an actual outcome.

#### Extraordinary and specialized modules

An extraordinary mechanism states access/source/method, prerequisites, finite costs, duration, causal channel, actual bounded effect, detection/counterplay, persistence/recovery and explicit exceptions. Stock creation produces a real bounded quantity; teleportation moves actual identified contents; healing changes named conditions; summoning does not imply control; resurrection does not clone identity or rewind estates/offices. No agency, death, resource or physics exception follows from a name.

Flight frames/orbits, pressure chemistry, particular sports geometry/scoring, historical law, biological effect rates, weapons, supernatural paradigms and local institutional terms stay with the appropriate genre/theme/profile. Core owns their reusable interfaces and actual write owners.

**Acceptance:** complete source/provider mapping; exact aliases and selectors; preserved native models; no duplicate ledger or numerical chain; publication causes no world-state changes; unresolved parameters constrain only the affected task. **Calibration/implementation gaps:** domain-specific rates, advanced solvers, activity performance, physiology and live runner reproducibility remain explicitly scoped.

## The Twelve Core Domain Workflows

<a id="core-113"></a>
### 113 GOV — Political/Government

**Purpose and scope:** Decisions about collective rules, authority, public resources, representation, diplomacy and enforcement. Supports household councils, customary assemblies, monarchies, bureaucracies, federations and other profile-defined institutions without imposing a preferred regime. **Status:** Proposed Core domain, integrating inherited topics §§28–30, 39–40, 65–66, 87 and PAF §10.

**Dependencies/ownership:** K-ORG owns institutions/offices/mandates; K-INFO owns who knows or recognizes them; ECO owns fiscal obligations; CIV coordinates large programs; INV handles contested cases; URBAN delivers local services. GOV owns jurisdiction, public decision, policy lifecycle, recognition claims and intergovernmental agreement records. Authority, practical capability, audience-specific legitimacy and territorial control remain separate.

**Records:** `Jurisdiction(subject, area, persons, authority_basis, overlapping_claims, applicable_rules)`; `Decision(proposer, issue, participants, eligibility, process_version, quorum/threshold_if_applicable, evidence_refs, objections, result, authorizer, effective_time, communication, implementation_refs, review/expiry)`; `MandateGrant(scope, holder, constraints, resources, validity_conditions/endpoints, revocation_effective_condition, communication/knowledge_refs, succession)`; `GOV.Agreement(parties, commitments, ratification, monitoring, dispute/exit_terms, ECO_clause_refs)`. Record vote preferences only as decisions or actor-specific evidence, not a universal loyalty meter.

**Legal-position owner contract (R2 proposed schema refinement):** `GOV.LegalPosition(subject_KACTOR_ref, jurisdiction_ref, classification_rule_ref, qualifying_decision_or_act_ref, legal_capacity_and_restriction_refs, effective_interval, governing_process_version, challenged_or_contested_claim_refs, amendment_or_termination_event_refs)` is a single GOV-owned factual record where the jurisdiction actually maintains a public/legal classification. The act or decision must satisfy the selected jurisdiction's rule; a merely nonempty decree label or witness attestation is not validation of legal effectiveness. When a classification can operate without a written registry, preserve the supported rule, act and effective facts rather than inventing a modern registration requirement. K-INFO stores each audience's notice/recognition, K-ACTOR stores actual custody and location, ECO/K-ASSET store contractual/property title claims, and LIFE supplies only social/career views and transition workflow links. A law, claim or judgment need not be factually valid or universally recognized merely because it appears in a report.

**Procedure:**

1. Establish the issue, affected jurisdictions, competent deciding body and procedure. A title alone does not grant unlimited authority. Competing claims may remain unresolved.
2. Collect admissible/available reports, proposals and actor positions; administration uses actual staff time. Identify who can participate, who can block, and what resources implementation requires.
3. Resolve negotiation or persuasion only where uncertain. Determine each autonomous participant's actual decision from knowledge, commitments, goals and pressures. Routine uncontested administration needs no roll.
4. Apply the established decision procedure. Count actual eligible ballots/assents where used, including abstention, absence and tie handling. A favorable persuasion result is not extra votes or ratification.
5. Record authorized result, scope and effective time; issue messages, orders, fiscal claims or projects through their owners. Legal effectiveness and practical receipt/enforcement can occur at different times under the profile; use §§5/10 endpoint and knowledge distinctions. Revocation cannot instantaneously inform a distant holder or erase their actual subsequent physical acts.
6. Review implementation at due triggers: compliance, noncompliance, challenge, expiry, changed coalition or succession. Enforcement needs real personnel, access and procedure. A passed policy can remain unimplemented.

**Events/interfaces:** consumes reports, petitions, office vacancies, mandate expiry, shortfalls and case findings; produces `decision_recorded`, `mandate_changed`, `policy_effective`, `agreement_ratified`, `implementation_requested`, `recognition_changed`. Tax adoption goes to ECO for assessment/collection; mobilization authorizes Core MIL (§124) and actual service institutions, not instant troops; lawful access decisions can enable INV without finding evidence.

**Outcomes:** a Mixed negotiation may produce a narrower proposal or conditional assent. New concessions require acceptance. Failure can leave opposition unchanged; it cannot invent a coup. A revolution or breakdown requires participating actors, means, coordination and causal events. Success can yield durable compliance and stability.

**Example:** a council approves funding for a ferry. The decision creates spending authority; ECO still needs funds, MAR needs a vessel/crew, and URBAN needs viable landing access. Opponents may accept the process while disputing the policy. The ferry starts only after its actual prerequisites are met.

**Overrides/calibration/unresolved:** the profile supplies selection rules, eligibility, legislative/customary processes, fiscal competence, enforcement powers, treaty procedure, recognition audiences and communication rules. No universal legitimacy threshold, tax rate, election swing, corruption chance or revolution clock. Supernatural legitimacy can influence specified audiences only through enabled lore/effects. **Acceptance:** Appendix C CE-GOV-01 through CE-GOV-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

<a id="core-114"></a>
### 114 ECO — Business/Economic

**Purpose and scope:** Livelihoods, enterprises, exchange, finance, production commitments and economic coordination from one person to regional markets. **Status:** Proposed Core domain, integrating inherited topics §§24, 35–38, 73 and Fantasy §§104–107/142 with Historical §§6–7 and PAF §§11–13.

**Dependencies/ownership:** K-STOCK owns cash/goods; K-WORK owns production; K-ORG owns firms and staff; K-NET owns delivery; GOV supplies fiscal/legal authority; LIFE supplies labor and household commitments. ECO owns agreements, claims, accounts, orders, quotes, enterprise plans and market assessments. It does not own a parallel stockpile or invent demand.

**Records:** `ECO.Agreement(parties, specification, quantity, unit/price, delivery, acceptance, payment, risk/title_transfer, cancellation/default_terms)`; `Order(status, reservation_refs/backing_shortfalls, work/shipment_refs, accepted_quantity, claim_refs, correction_refs)`; `Claim` as §12; `Enterprise(owners, management_authority, accounts, capacity_refs, inputs, customers, obligations, operating_plan)`; `Market(location, time, commodity_spec, offers, bids/demand_evidence, access, stock_refs, information_age)`. A valuation records basis and uncertainty; it is not spendable cash.

**Procedure:**

1. Identify the good/service, genuine supplier and customer, rights, quality, local availability, funding/credit and capacity. Separate scarcity from price and appraisal from bargaining.
2. Establish a quote or negotiate feasible terms. Routine purchases at known terms need no roll. A social success cannot compel an unwilling party outside plausible limits.
3. Accept terms through authorized actors. Reserve exact stock, work/transport slots and funds only as agreed. Track quote, agreement, obligation, dispatch/delivery, acceptance and payment separately; prepayment or partial delivery need not follow a fixed sequence.
4. Produce or procure through K-WORK, with actual inputs, qualified time, accepted output and waste. A shop opening or an investment buys no automatic revenue stream.
5. Ship, inspect and transfer custody/title according to terms. Invoice/accrue only the supported obligation. Pay through §12; preserve partial balances and disputes.
6. Reconcile at contractual/accounting triggers. Compare usable cash, upcoming liabilities, available input, expected sales and capacity. Shortfalls may prompt authorized borrowing, renegotiation, curtailment or default; no automatic bankruptcy catastrophe.

**Markets and credit:** Prices arise from established quotes, transactions or an explicitly selected market model. Regional supply/demand estimates support forecasts, not a universal automatic price multiplier. Credit creates a lender asset and borrower liability under a named instrument; drawing it transfers or issues spendable means only through the specified monetary institution. An unsettled claim cannot be spent as money unless a real counterparty accepts its transfer. Interest/fees require stated terms, processing periods and §§19/109 process-law metadata. Reservation shortfall and later contract correction follow §12; recovery receivables are not recovered cash. Exchange rates and account units require a conversion source; unsupported conversions remain unresolved.

**Events/interfaces:** consumes work acceptance, delivery, due dates, policy changes and loss; produces `agreement_accepted`, `claim_accrued`, `payment_settled`, `default_recorded`, `order_fulfilled`, `enterprise_plan_changed`. INV can examine fraud; GOV can assess taxes; LIFE can receive wages; CIV can read production capacity. Loss of a cargo and insurance payment are separate events; insurance requires an actual agreement and payer capability.

**Example:** a mill completes accepted work, earns a receivable and has no cash receipt yet. Its owner cannot pay staff from the invoice alone. An agreed partial payment transfers actual funds and reduces the same claim; the remainder becomes arrears only when due. Family and enterprise cash remain separate unless actually transferred.

**Overrides/calibration/unresolved:** currencies, account rules, contracts/customs, demand formation, production yields, wages, prices, taxes, credit, insurance, insolvency, seasonal cycles and price discovery require local profiles. No universal growth rate, guaranteed investment return or perfectly efficient market. **Acceptance:** Appendix C CE-ECO-01 through CE-ECO-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

#### 114.R3 Combined civilian production, tax and household economy — proposed

The same K-ACTOR and K-WORK availability constrains household provision, agriculture, manufacturing, civic employment and MIL service. Production depends on **committed eligible labor**, actual equipment/site capacity, available input stock, transport, duration and a bound production/quality model; it is not produced by a mobilization policy's forecast. A workforce diverted to military duty changes unworked civilian capacity prospectively; it cannot erase already accepted output, create unemployment compensation automatically or retroactively reassign time. Conversely, enlistment alone does not silently cancel an existing agricultural or household shift. Schedule relief, reassignment, labor replacement, work interruption and obligations as distinct actual events.

**Minimum records** (owner-qualified references, not a second ledger): `WorkSlot(person_ref, activity_ref, site_ref, start, end, authority/consent_basis, status)`; `WorkOrder(input_stock_and_reservation_refs, worker_refs, site_capacity_profile, planned_span, actual_completed_span, output_acceptance, interruption_reason)`; `ECO.TaxClaim(jurisdiction_and_basis, payer, assessed, paid, outstanding, effective_times)`; `ECO.WageClaim(employee, agreement_ref, actual_qualifying_hours, rate_profile, accrued, paid, due_time)`; `ProvisionDemand(household_or_service_ref, amount, due_interval, service_profile)` and a separate `ActualProvision` referencing stock consumption, K-WORK care or K-NET delivery. Rate, needs and ability values remain profile-owned.

**Economic interval procedure:** (1) identify obligations and authorized commitments; (2) evaluate overlapping labor/worksite capacity and reserve qualifying inputs; (3) execute actual bounded work over unprocessed spans; (4) commit accepted material output and input consumption atomically, and record interruptions; (5) accrue qualifying financial claims without creating money; (6) transfer actual goods, money and support through K-STOCK/K-NET; (7) assess delivered services against independently specified needs and record any deficit without guessing medical effects; (8) notify CIV, GOV, LIFE and MIL of actual changed capabilities. A product's location, quality and usability continue to matter after production.

**Rate-calibration boundary:** Work-hours, kg, items, meals, currencies and persons are distinct dimensions. The R3 test harness uses synthetic integer units with *fixture-specific* linear recipes (including prorated interruptions); these are not default Core yield rates or universal childcare requirements. Real engines must bind uncertainty, seasonality, equipment, skill, weather, nutrition, wages, taxable activity and production-law envelopes where consequential. A nation never obtains GDP, food or weapons from a category label alone.


#### 114.R6 — Economic recovery, labor liabilities and acceptance (PROPOSED)

ECO reconciles promised deliverables, settled partial goods, replacement procurement, outstanding debt, wage obligations and actual payments **by reference to K-WORK/K-STOCK events**. Input replacement is an actual transfer from a source, not a credit to production. An assessment of taxes or accrued pay creates a claim, not new money. A completed milestone may produce usable goods even if the enclosing project later suffers disruption; a later full settlement cannot mint those goods again. Distinguish paid wages from owed wages, and verified labor under the chosen contract from time whose work or compensation remains disputed.

The reference tests only a supplied fixed monetary rate with authorized recorded accrual and no actual payment; it does not select universal compensation law, insurance, price discovery, taxation, credit or substitution costs.

<a id="core-115"></a>
#### 114.R7 — Economic separation of WIP, accepted stock and claims (PROPOSED)

ECO SHALL distinguish capital and raw material consumed in ongoing work, physical work-in-progress, accepted finished inventory, rejected goods, recovered scrap, and the costs/claims of assessment or recovery. Goods are not saleable as completed merely because the factory reports scheduled production; buyers, military quartermasters and households may recognize acceptance status differently under actual contractual/institutional rules. An inspection entry establishes a finding; only an authorized physical conversion or asset status transition may change the source stock. Aggregate production and cash displays are read-only projections, not newly minted stock or income.

### 115 INV — Crime/Investigation

**Purpose and scope:** Incidents, detection, evidence acquisition, competing explanations, responsibility and institutional disposition. Crime is conduct classified by the applicable institution; investigation also covers accidents, missing persons and technical failures. **Status:** Proposed Core domain, integrating inherited topics §§39–40, 60–61/79, Military §6.6 and historical custody procedures.

**Dependencies/ownership:** K-INFO owns evidence and beliefs; GOV supplies jurisdiction/rules; K-ASSET owns physical evidence; K-ACTOR owns people/custody location; MED can supply scoped findings; INTEL uses the same provenance tools. INV owns incidents, cases, hypotheses, investigative tasks and disposition records. The actual offender, observer suspicion, accusation, finding and sanction are distinct.

**Records:** `Incident(time/location, actual_event_refs, reports, affected_parties, classification_claims)`; `Case(mandate, investigator, questions, jurisdiction, evidence_refs, hypotheses, open_tasks, status, review)`; `EvidenceHandling(item_ref, collector, method, time, custody_transfers, alterations, access, authenticity_questions)`; `Hypothesis(claim, supporting/refuting_evidence, predicted_observations, alternatives, confidence_rationale)`; `Disposition(authority, standard/procedure, considered_evidence, finding, remedy/sanction, appeal/review, execution_refs)`.

**Procedure:**

1. Establish the incident and reported problem. Preserve known underlying truth; create unresolved world detail only from supported context before a discovery result, with provenance. Do not change the culprit to defeat a successful theory.
2. Establish mandate, access and scope. Lack of lawful authority can create legal consequences without physically preventing an unauthorized act. No procedure assumes universal police, warrants, juries or appeals.
3. Identify threatened evidence, witnesses and preservation tasks. Collection uses actual time, method, access, equipment and sample consumption; obvious accessible evidence is automatic for a qualified observer.
4. Record what was found, how, and any gaps. Search success cannot yield nonexistent evidence or conclusions beyond the method. Absence counts against a hypothesis only to the extent coverage/detectability make it informative.
5. Compare hypotheses and choose a discriminating next task: corroborate, interview, test, reconstruct, trace a transfer, or seek access. Test predictions against persistent state. Pure copies of one rumor share its lineage. Compound reports retain new and shared assertions separately under §12 and Appendix A, including contradictions and correlated observations; an investigator uses available provenance rather than hidden actual lineage.
6. Submit a supported assessment to the actual authority. Institutional finding follows the applicable process and evidence standard, not the investigator's raw roll. Execute any custody/property/remedy changes separately through real actors.
7. Close, suspend or reopen with reasons. Unsolved cases persist without mandatory hints or unrelated catastrophe. New evidence can revise beliefs while preserving earlier records.

**Events/interfaces:** consumes incident reports, evidence access/loss, interview/test findings, deadlines and judicial orders; produces `evidence_collected`, `hypothesis_revised`, `case_referred`, `finding_recorded`, `custody_requested`, `case_closed/reopened`. A court award becomes an ECO claim, not immediate cash. Evidence destroyed physically may remain in earlier photographs or testimony; preservation affects reliability, not retroactive erasure of all knowledge.

**Example:** a warehouse ledger suggests theft, but a shipment was redirected. A qualified inspection finds the accessible dispatch record. It supports a routing hypothesis, not certainty about motive. A delayed receiving report can later confirm arrival; it does not create the cargo a second time or prove every allegation false.

**Outcomes and limits:** Mixed collection might preserve only part of a damaged record, with the lost portion defined by the cause. Failure does not invent a confession or murderer. Coercion can produce speech without proving truth and never controls the protagonist's voluntary admissions. Generic crime operations use normal action/exposure rules; no global “wanted level” or universal police response exists.

**Overrides/calibration/unresolved:** evidence methods and limits, preservation, forensic capability, jurisdiction, standards of proof, procedure duration, sanctions and appeal rights are profile-owned. Magical truth/divination requires an explicit channel and separate institutional acceptance. **Acceptance:** Appendix C CE-INV-01 through CE-INV-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

<a id="core-116"></a>
### 116 MAR — Maritime/Naval

**Purpose and scope:** Operating on water: voyages, seamanship, navigation, cargo, ports, fleets, damage control and rescue. **Status:** Proposed Core domain. Core §§30, 35, 47–63 supply supporting mechanics; Military §1 explicitly warns that a component record alone supplies no seamanship, flooding or buoyancy rules. PAF routes and library waterway entries supply interfaces, not a complete maritime engine.

**Dependencies/ownership:** K-ASSET owns vessel/components; K-STOCK owns cargo and stores; K-NET owns routes/ports/capacity; K-ACTOR owns crew; ECO owns charter, freight and claims; GOV supplies jurisdiction; MED owns casualty care. MAR owns vessel operating envelope, voyage plan, navigational estimate, watch/maneuver plan, compartment hazard state and maritime operation assessment. Naval combat calls the selected combat/effect model; no new universal naval hit-point pool is introduced.

**Records:** `VesselProfile(hull/form, draft/load_envelope, stability_constraints, propulsion, steering, watertight_boundaries, pumps, crew_stations, modes, environmental_limits, failure_effects)`; `Voyage(route_legs, departure, actual_position, estimated_position/error, forecasts, load_manifest_refs, watches, provisions, destination/alternates, stop_conditions)`; `PortCall(berth, approach/access_window, pilotage_if_required, handling, queues, repair/refuel_refs, clearance)`; `Compartment(state, connected_openings, flooding/burden_profile, ingress/outflow, isolation, dependencies, observed_state)`.

**Procedure:**

1. Define voyage objective, actual vessel/load, people, route and knowledge. Check seaworthiness for this route and weather, compatible draft/clearance, load distribution, trained watches, endurance, access and arrival handling. “A ship exists” supplies none of these automatically.
2. Plan legs and contingencies within authority. Reserve berth/handling where applicable; reservations can still be disrupted. Dispatch moves the vessel, passengers and referenced cargo into transit once.
3. Advance each leg through current propulsion, wind/current profile, navigational information, weather, crew commitments and fuel/provisions. Routine passage is automatic. Uncertain position remains an estimate; failed navigation changes course/time/exposure rather than erasing distance traveled.
4. Resolve contacts and maneuver at the smallest decision-relevant scale. Visibility, geometry, weapon bearing, reload, crew, sea state and shared power constrain action. One helmsman cannot concurrently provide incompatible full-capacity gunnery. Boarding requires actual approach, access and participants; it is not granted by a ship combat success.
5. For damage, apply the actual breached/disabled component first. Update only connected compartments/functions. Track ingress, removal, isolation and effects through the vessel profile; recalculate operating limits and threshold times. Schedule foundering, capsizing, fire spread or loss of steering only when supported, not from “hull zero” shorthand without a mapping.
6. At arrival, anchor/berth, handle actual transfers, hand over watches and conduct required inspections. Repair, salvage, abandonment and rescue use real resources, transport and time. Port entry is not unloading or payment. Arrival, berth access, powered/staffed handling progress and cargo handover are separate triggers; handling uses §103 feasible service configurations, and the same cargo remains aboard until actually transferred.

**Maritime effect gate:** A consequential flooding/stability scenario needs a declared envelope or causal profile: permissible loading/configuration; breach exposure; compartment connectivity; pumping capability; reserve/threshold meaning; and resulting capability states. With compatible volume units a bounded fixture may use `flooded_volume' = flooded_volume + ingress − removal`, stopping at actual thresholds. That accounting equation alone cannot determine buoyancy or stability. Without those parameters, record a known breach and supported restrictions; leave the unsupported precise sinking time unresolved. A temporary qualitative ruling must be named before its consequences are resolved.

**Events/interfaces:** consumes weather/contact reports, route access changes, component damage, fatigue/relief, port allocation and rescue calls; produces `voyage_departed`, `leg_completed`, `position_estimate_updated`, `compartment_state_changed`, `vessel_capability_changed`, `port_arrival`, `cargo_handed_over`. Naval blockade/interdiction is an ongoing operation with coverage and endurance, not an automatic deletion of all regional trade.

**Example:** a damaged pump reduces dewatering capacity but leaves propulsion intact. Closing an existing watertight boundary can limit spread after the actual control action. A distant rescue ship cannot save people before reaching them; a successful distress signal changes recipients' knowledge, not rescue position.

**Overrides/calibration/unresolved:** vessel performance, wind/current, safe loading, damage effects, waterway access, watches, port throughput, naval weapon profiles and rescue envelopes require content. No common sea-state penalty, sinking timer or historical naval doctrine is assumed. Fantasy floating vessels and extraordinary propulsion declare exactly what constraints change. **Acceptance:** Appendix C CE-MAR-01 through CE-MAR-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

<a id="core-117"></a>
### 117 CIV — Civilization & Grand Strategy

**Purpose and scope:** Coordinate societies, regions and long programs across institutions, generations and material networks. **Status:** Proposed Core domain, integrating inherited topics §§62, 65, 69, 72–75, 83–87 and PAF §§10–14. This is an orchestration scale over persistent systems, not a second economy or a universal civilization level.

**Dependencies/ownership:** GOV owns political authority/agreements; ECO owns finance and trade; URBAN owns settlements; WILD owns landscapes; LIFE/K-POP own demographic state; K-WORK owns progress; Core MIL (§124) coordinates armed institutions and military operations; specialist genre/setting modules own only their distinct effect and operating models. CIV owns regional dependency assessments, strategic objectives, program portfolios, territorial relationship views and coordinated review schedules.

**Records:** `Region(geographic_refs, populations/sites, claims, effective_control_by_function, networks, productive/support_capability, information_quality)`; `StrategicObjective(owner, desired_state, scope, horizon, constraints, measures, stop/review)`; `Program(project_refs, prerequisites, shared_allocations, stage_acceptance, recurrent_costs, workforce/knowledge_renewal, risks)`; `StrategicAssessment(as_of, evidence, actual_vs_reported_state, scenarios, binding_limits, assumptions)`. These reference existing entities. They cannot contain independent treasury, military-strength or population totals that write back as new state.

**Procedure:**

1. State objectives and decision authority: improve service, secure a route, negotiate union, rebuild industry, preserve knowledge or sustain ordinary prosperity. A player controls only the office/resources actually delegated.
2. Assess actual and reported regional conditions separately. Compare task-specific capacity, maintenance, population needs, knowledge, access, territorial claims and functioning networks. Identify bottlenecks and dependencies without assigning a global “advanced” score.
3. Form feasible program alternatives using real budgets, projects, institutions, labor and operating commitments. Compare opportunity costs; an actor can choose resilience, trade dependence, specialization or abandonment according to their goals.
4. Authorize allocations and communicate orders. Institutions implement autonomously within mandate. A strategic order is neither instant compliance nor completed work.
5. Advance authorized time through §11. Summarize uneventful intervals, retaining dated flows, completions, interruptions and configured §§19/109 process boundaries. Zoom in where a meaningful decision requires it and mark the replaced abstract scope.
6. At review assess objective attainment, cost, distribution, ongoing support and remaining vulnerabilities separately. A conquest can change military control without civil administration, recognition or service provision. A treaty can change obligations without moving borders physically.
7. Update long-term support: replenishment, equipment replacement, training, institutional succession and environmental viability. Stable success remains success; no balancing enemy or mandatory collapse appears.

**Demography and technology:** Births, deaths, movements and cohort transitions require actual events or a named demographic process. Regional review does not roll extra mortality for people already resolved locally. Adoption of a technology, possession of an example, and repeatable productive capability remain distinct. Diffusion needs information, access, training and support. Culture and historical memory belong to particular carriers, institutions and audiences; they are not a civilization-wide obedience modifier.

**Events/interfaces:** consumes service/capability changes, treaties, movement, accepted projects, institutional succession and operational reports; produces `program_authorized`, `allocation_requested`, `strategic_review_completed`, `objective_revised`, `regional_dependency_changed`. Actual work and resources remain with their owners. There is no `civilization_level_up` event.

**Example:** three towns agree to share a repair center. The agreement establishes obligations; the center still needs trained staff, tools and actual access. Each town's local demand competes for the same workshop slots. One participant's withdrawal may change funding while leaving the road, workshop and technicians physically intact.

**Overrides/calibration/unresolved:** planning horizons, demographic processes, territorial administration, military operational effects, fiscal capacity, technological diffusion and environmental cycles require selected profiles. Coarse aggregation must specify cohort boundaries, uncertainty and local-scene exclusions. No universal casualty fraction, development cost, GDP-to-army conversion or deterministic historical ladder. **Acceptance:** Appendix C CE-CIV-01 through CE-CIV-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

#### Incident-linked impact assessment

PA-CW-01/E-01 adds an optional ImpactAssessment presentation of CIV.StrategicAssessment, not an independent mutable world record or disaster meter. Use it for any consequential incident, including storms, service interruption, labor stoppage, migration, reform, innovation or war.

Record assessment ID/as-of time; identified baseline/source and confidence; cause/event references; geographic/function scope; actual owner-state references; observed/reported references; service/stock/workforce/institutional bottlenecks; actual exposed users; buffers/alternatives; scenario thresholds and assumptions; affected obligations/programs; responsible actors and decision rights; next causal trigger.

The baseline is a supported prior state or observation, not a reconstructed ideal. Unknown historical quantities stay unknown. Compare relevant functions at timestamps without advancing time, refilling stocks, completing work, changing law, assigning blame or granting omniscience. Reports change the observed side at receipt, not physical reality again. Forecast pressures remain derived assessments.

Review only at a relevant source change, received report, authorized planning interval or meaningful decision. Crisis-specific PA.Crisis, PA.Pressure and legacy-history overlays remain with the selected PAF. One shared assessment can inform that genre view without importing its premise into an ordinary campaign.

#### R3 proposed mobilization-production feedback

At civilization scale, national recruitment, requisition and duty scheduling allocate actual K-POP/K-ACTOR members and finite K-WORK hours rather than applying independent military and civilian workforce multipliers. Missing labor can reduce output where a real production binding supports that consequence; substitution can restore one service while displacing another. Account for transport, food, fuel, seed, replacement staff, wage arrears, tax claims and dependent household provision in the same dated stocks/commitments. Published aggregate production and unemployment figures are derived views of actual resolved work and identified residual cohorts. If aggregate process coverage includes individually resolved work, subtract/exclude those intervals and people before committing aggregate deltas.

Political demand does not create troops; troop enrollment does not create readiness; readiness does not create food or accepted taxes. Current and projected supply are separate, and a population count is not a labor-supply forecast without appropriate qualifications, location, effective time and participation constraints.


#### 117.R4 — Civil-military continuity through a selectively processing world (PROPOSED)

CIV consumes only actual corresponding Core MIL, LIFE, ECO and K-WORK owner changes. If army financing is contested at a given frontier, authorized planting, local medical care, unrelated taxation and physical transport remain eligible to proceed. Subsequent grants do not retroactively provide earlier equipment, seed, training, meals or troop readiness. At each regional summary, reconcile locally resolved actors and interval coverage against the remaining eligible aggregate cohorts before computing additional work or demographic effects. A static aggregated report cannot write physical output. Preserve unresolved authority decisions and known obligations in state and disclose them only through supported recipient information.

#### 117.R5 — Civilian and military exposure to common physical shocks (PROPOSED)

CIV consumes the same source K-STOCK hazard event through ECO, LIFE, MED, MIL, K-WORK and K-ORG links. A warehouse loss can reduce civilian food availability, army provisions and outstanding contracts simultaneously; the loss is written only once, while consequences unfold from real surviving resources, authority and time. A competing government allocation can remain undecided while an independent hospital, kitchen or taxation process continues. Actual lack of provision can create a service deficit, but not an unrelated medical consequence without a selected causal model. Strategic and personal perspectives remain different views of the same people and material balances.

#### 117.R6 — Regional shocks, parallel industries and work continuity (PROPOSED)

CIV may observe a fire, flood, mobilization or other source disruption through shared K-STOCK and K-WORK references without freezing independent industries or households. Affected work recomputes its feasible remaining stages; independent work continues when its people, access, inputs, facilities and capacities are actually distinct. A strategic summary reads prior completed milestone events and unresolved work claims; it does not add another yield when reviewed monthly or forecast a repaired workplace simply because a new shipment exists. Multisite congestion and downstream input dependencies still need qualified read/write footprints and real supply-chain models.

<a id="core-118"></a>
#### 117.R7 — National continuity across industrial and military demand (PROPOSED)

A region's farm, household, workshop and armed forces share resource locations, labor capacities and institutional budgets. An unresolved contract or allocation dispute at one workplace shall not freeze unrelated production. A verified warehouse or workshop loss shall continue to affect all actual claimants through remaining stock, not by rescinding the event. A province/monthly summary shall include supported finished and intermediate stocks separately; it must not turn WIP into final deliveries when switching scales. Strategic mass-balance and independent long-term autonomous production remain separate unqualified acceptance gates.

### 118 MED — Medical/EMS

**Purpose and scope:** Individual care, emergency response, transport/referral, service capacity, rehabilitation and public-health coordination. **Status:** Proposed Core domain, integrating Core §§17–19/43, Fantasy §§73–82/131, Military care/duty links and PAF healthcare/service interfaces. These are game procedures; specific medical effects require the selected physiology/care profile.

**Dependencies/ownership:** K-ACTOR owns conditions and functional limits; K-INFO owns observations/diagnostic beliefs; K-WORK owns care tasks; K-NET owns facility/transport capacity; LIFE owns care obligations; GOV owns public authority. MED owns episodes, assessment, prioritization, care plans, referral/handover and public-health response plans. A care episode references existing injuries; transfer between providers creates no new wound or healing ledger.

**Records:** `Episode(patient_ref, presenting_problem, onset/cause, observations, assessed_state/uncertainty, active_condition_refs, responsible_provider)`; `CarePlan(objectives, method/profile, prerequisites, consent/authority, stages, expected_effect, risks, resources, review, stop/transfer_conditions)`; `Dispatch(request_time, known_problem, available_units, location/route, capability, assignment, arrival, handover)`; `TriageEntry(assessment_time, urgency_reason, required_capability, feasible_options, priority_policy, reassessment)`; `PublicHealthEvent(exposure/cohort_refs, case_definition, observations, transmission_profile, response, reports)`.

**Procedure:**

1. Receive or observe a care need. Separate actual condition from dispatch description and provider assessment. Unknown diagnosis does not prevent treating an observable problem within capability.
2. Check immediate environment, provider access, skills, supplies and actual ability to reach the patient. Assign available responders under established authority; unavailable units cannot answer two calls simultaneously.
3. Assess and prioritize using observed condition, available interventions, time sensitivity and the adopted policy. Do not reveal hidden prognosis to an NPC or derive it from a low roll. Reassess when material state or capacity changes.
4. Define the treatment objective: assessment, stabilization, repair, infection management, symptom relief, rehabilitation or another supported effect. Routine qualified treatment is automatic with real inputs/time. One action does not achieve every objective.
5. Apply the supported effect to the existing condition; schedule deterioration/recovery only through its profile. Stabilization can halt a threat while structural impairment persists. Treatment failure consumes what was actually used and applies only credible exposure.
6. Arrange transport/referral where necessary. Reserve transport, receiving capability and handover; booking is neither travel nor care. During transit the same patient has the same needs/conditions and actual accompanying support.
7. Review care progress, functional status and discharge/ongoing support. Return-to-duty certification and biological recovery are separate. Rehabilitation, livelihood and family care use the same finite time.

**Capacity and public health:** Distinguish staffed capability, rooms/beds, equipment, consumables, utility continuity and specialist availability. A building or empty bed is not a treatment slot if essential inputs are absent. Use §103 operating bundles and supported reduced modes; partial power/staffing is not automatically proportional treatment. An interruption records actual prior use and only profile-supported effects, without an automatic refund or invented deterioration. Backlogs contain actual cases/tasks; recurrence cannot duplicate them. A hazard profile owns transmission/exposure; MED assesses cases and coordinates response. Quarantine, reporting and vaccination or analogous interventions exist only where supported by profile and authority. A reported case and an infection event are not two patients.

**Events/interfaces:** consumes injury/exposure, care requests, utility loss, staffing changes and diagnostic results; produces `assessment_recorded`, `care_started/completed`, `condition_change_requested`, `referral_accepted`, `patient_handed_over`, `care_capacity_changed`. MED can supply evidence to INV; that does not establish criminal responsibility. A magical healer changes only named conditions/costs through the enabled paradigm, sharing capacity and custody rules.

**Example:** a field team stabilizes a patient, requests referral and hands over at a staffed facility. Stabilization does not restore mobility. A later casualty report updates command knowledge; it does not add another patient, reduce unit headcount again or consume a second treatment kit.

**Overrides/calibration/unresolved:** anatomy, prognosis, treatment efficacy, deterioration, recovery, transport suitability, triage policy, staff capability and disease dynamics need explicit profiles. No universal mortality rate, dose, staffing ratio, recovery counter or moral utility score. Undefined prognosis blocks that calculation, not all care/logistics. **Acceptance:** Appendix C CE-MED-01 through CE-MED-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

<a id="core-119"></a>
### 119 WILD — Wilderness/Ecological

**Purpose and scope:** Travel, exploration, habitats, living populations, renewable resources and environmental change. **Status:** Proposed Core domain, integrating inherited topics §§19, 50–51, 71/79, Fantasy §§83–96 and creature libraries, PAF §§5–7/11–12. Nonhuman creatures are actors with needs and motives, not encounter difficulty tokens.

**Dependencies/ownership:** K-ACTOR owns individual organisms; K-POP owns residual populations under their declared species/population profile; K-STOCK owns harvested output; K-NET owns routes; K-WORK owns cultivation/extraction; MED owns care. WILD owns habitat state, environmental processes, resource-source assessments, ecological relationships and expedition coverage. Ecological and habitation views reference the same individually tracked actors and residual cohorts; no organism is counted twice across populations.

**Records:** `Habitat(area, season, water/soil/cover_state, hazards, species/cohort_refs, access, disturbances, support_dependencies)`; `RenewalProcess(source, state, enabling_conditions, update_law, losses, harvest/removal, bounds, causal_interval/continuous_interpretation, last_processed_boundary/span, numerical_method/tolerance_if_needed, uncertainty)`; `SpeciesProfile(anatomy, locomotion, senses, needs, behavior, reproduction/lifespan, interactions, extraordinary_traits)`; `Expedition(objective, party, route, means, needs, navigation/coverage, known_hazards, return/abort)`; `Survey(area, method, effort, detection_limits, observations, population_estimate, uncertainty)`.

**Procedure:**

1. Establish geography, season, existing habitat/resources and what actors know. An unexplored area is not an empty world, and a site template is not a resource allotment.
2. Define expedition, use or intervention: travel, forage, hunt, survey, cultivate, conserve, drain, restore or extract. Check access, tools, competence, carrying/processing, commitments and known exposure.
3. Advance actual movement/work. Navigation and search use method-limited evidence; routine travel on a clear route is automatic. Search, capture/harvest, processing and transport are distinct activities.
4. Remove actual harvested organisms/material from the source; add only the recovered usable output through the declared yield, retaining waste/by-products when relevant. A forest is not stored timber and standing crops are not meals.
5. Advance environmental/biological processes only through configured causal mechanisms: growth, reproduction, mortality, migration, predation, seasonal inputs or disturbances. Keep native source units until a supported conversion exists. Use §§19/109 process-law semantics; renewal never occurs because a scene or presentation review changed.
6. Reassess habitat capacity, depletion and downstream effects at relevant thresholds. A harvest can reduce later renewal if the profile connects them; it does not cause an arbitrary universal ecological penalty.
7. Preserve observed evidence and revise estimates separately from actual state. A new survey can reveal earlier undercounting without a birth event. Aggregate/detail transitions conserve organisms and removals.

**Ecological accounting:** For countable populations, closing population equals opening + births/recruitment + immigration − deaths − emigration − removals, with each event represented once. Births consume no fictional “population points”; their feasibility and ecological costs come from the profile. Biomass, organism count, habitat area and food-energy yield are not interchangeable. A renewable label guarantees neither sustained yield nor a fixed carrying capacity. If renewal is uncalibrated, preserve known stock and observed changes; do not promise infinite harvest.

**Events/interfaces:** consumes weather, contamination, land-use change, harvest, animal movement and surveys; produces `habitat_changed`, `source_yield_accepted`, `population_transition`, `route_condition_changed`, `exposure_created`, `survey_recorded`. URBAN land use and ECO production can change habitat; downstream consequences require named pathways and elapsed time. MED reads exposure, not a generic wilderness-danger penalty.

**Example:** a settlement gathers from a known patch. Collection removes available stock and consumes travel time; processing yields usable food. A later party encounters the depleted patch unless a real renewal or new-access event occurred. Good fieldcraft may find another established source, not replenish the first one.

**Overrides/calibration/unresolved:** travel rates, physiology, seasonal cycles, species behavior, renewal/yield, ecosystem feedback, environmental spread and survey detectability need profiles. No universal predator aggression, daily encounter roll, food yield, breeding rate or ecological equilibrium. Extraordinary ecology alters named mechanisms through a setting module. **Acceptance:** Appendix C CE-WILD-01 through CE-WILD-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

<a id="core-120"></a>
### 120 INTEL — Espionage/Intelligence

**Purpose and scope:** Information requirements, collection, analysis, dissemination, clandestine work and counterintelligence. **Status:** Proposed Core domain, integrating inherited topics §§30, 60–61, 79/85–86, Military learning and shared investigation. No separate truth-generating espionage roll.

**Dependencies/ownership:** K-INFO owns evidence, beliefs and lineage; K-ORG owns agencies/mandates; K-ACTOR owns personnel; K-NET owns channels; INV owns formal cases; GOV/ECO supply authority and funds. INTEL owns intelligence requirements, collection plans, source relationships, access/cover state, assessments and dissemination restrictions. Cover is an audience's supported belief/access condition, not a second actor identity with duplicated assets.

**Records:** `Requirement(question, decision_supported, requester, deadline, scope, priority, known_gaps)`; `CollectionTask(method, accessible_targets, collector, authority, means, time, exposure, stop)`; `SourceRelationship(source_ref, access_basis, motives, contact_channel, reliability_evidence, handling_limits, last_contact)`; `Assessment(question, evidence_refs/lineage, alternatives, confidence_rationale, gaps, valid_as_of, expiry/review)`; `AccessCover(audience, claimed_role, supporting_records, actual_permissions, contradictions, known_exposure)`; `Dissemination(product, recipients, need/access, channel, sent/received, restrictions)`.

**Procedure:**

1. Tie a question to an actual decision. Distinguish what is unknown, what would change the decision and when information remains useful.
2. Choose a feasible collection method and source with genuine access. Allocate personnel, time, communications and funds. Authority and covert access differ; a clandestine act may proceed with real exposure rather than being legalized by its success.
3. Resolve acquisition through the shared action contract. Routine accessible collection is automatic. Uncertainty concerns actual concealment, incomplete coverage, deception, contact or interpretation. Acquisition success does not imply being undetected.
4. Preserve observed content, provenance, alterations, reporting delays and source dependence. Assess credibility and competing explanations. Preserve each materially new observation/assertion and its derivation, including correlated evidence. Count duplicated components once and assess dependence separately under §12 and Appendix A; claimed/known provenance can differ from hidden actual lineage.
5. Build a bounded assessment with confidence rationale and decision-relevant gaps. With no calibrated probabilistic model, use qualitative confidence and its evidence basis; do not assign invented percentages.
6. Disseminate to authorized/actual recipients through channels. Compartmentation can protect sources while reducing recipient understanding. A recipient can act only on arrived information and their own knowledge.
7. Reassess after source loss, contradictory evidence, access change or deadline. Counterintelligence investigates supported anomalies; it does not reveal every agent when a generic suspicion meter fills.

**Deception and concealment:** A deception creates fabricated evidence, messages or behavior at a real point of access. It changes truth only where there is an actual physical act; otherwise it may change beliefs. Exposure is scoped: one guard can doubt an identity while a distant office remains unaware. Track what the observer detected and how it can spread. Avoid both automatic universal cover destruction and repeated risk-free rerolls. A failed operation may yield nothing while leaving a source intact; the predeclared exposure and actual observers determine consequences.

**Events/interfaces:** consumes requirements, contact windows, observations, access changes and contradictory reports; produces `collection_completed`, `source_contact_changed`, `assessment_issued`, `report_received`, `cover_questioned`, `counterintelligence_referral`. INV and INTEL can share evidence objects but not duplicate investigative labor. An intelligence allegation is not a legal finding; legal admissibility and analytic usefulness differ.

**Example:** several intercepted messages repeat one depot rumor. The analyst records the common source and cannot treat them as independent confirmation. A later observation shows vehicles leaving but not their cargo. A useful assessment narrows possibilities without claiming certainty about supply or destination.

**Overrides/calibration/unresolved:** collection technology, access methods, institutional policy, language, communication, source behavior and detection mechanisms require context. No universal infiltration percentage, loyalty roll, heat clock or omniscient spy network. Telepathy/divination reads only its enabled information channel and still needs source/recipient records. **Acceptance:** Appendix C CE-INTEL-01 through CE-INTEL-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

<a id="core-121"></a>
### 121 URBAN — Urban/City Development and Management

**Purpose and scope:** Habitation, land use, development, urban services, maintenance and distribution of access across a settlement. **Status:** Proposed Core domain, integrating inherited topics §§72–73 and PAF §§7–10/13–14. Applies to villages, camps, distributed communities and mature cities without compulsory size tiers.

**Dependencies/ownership:** K-ASSET owns buildings; K-NET owns services/links; K-POP owns occupants; K-WORK owns construction; ECO owns contracts/funds; GOV owns policy/authority; WILD owns surrounding ecology; MED owns treatment. URBAN owns spatial plans, occupancy/use permissions, development cases, service-access plans and municipal work portfolios. A city panel is a view of those owners.

**Records:** `SpatialUnit(parcel/district, geometry/access, physical_asset_refs, current_use, claims, occupancy_refs, service_connections, hazards, constraints)`; `DevelopmentCase(objective, rights/access, proposal, impacts, authorization, work_refs, acceptance, occupancy/operating_transition)`; `ServiceAccess(users, provider/link_refs, eligibility, demand, actual_delivery, deficits, alternatives)`; `MunicipalPlan(priorities, work_queue_refs, budget_refs, maintenance, staffing, reviews)`.

**Procedure:**

1. Record actual habitation, rights/control, service access and needs by location. A refuge exists when people inhabit it, even with inadequate services. Deficit does not erase population or impose an artificial cap.
2. Diagnose a concrete problem: overcrowding, access, sanitation, housing condition, transport, utilities, affordability or maintenance. Use evidence and affected groups; citywide averages cannot hide a disconnected district.
3. Compare feasible alternatives using land/access, environmental constraints, authority, finance, qualified labor, materials, network capacity and future operating obligations. A permit authorizes; it does not build.
4. Approve through GOV/actual authority where applicable, contract through ECO, and execute K-WORK projects. Schedule utility disruption, relocation and construction access if real. Residents keep property/rights unless an actual process changes them.
5. Inspect against predeclared functional acceptance. Separate construction complete, safe/authorized occupancy, connected service, staffing and sustainable operation. Extra beds do not create water, jobs or residents.
6. Admit actual occupants/users and update demand at arrival/use. Allocate shortages through policy and technical constraints; actual operators can follow standing rules. Deficits propagate only to affected needs/functions.
7. Maintain assets and services through real work queues. Review access, backlog, operating costs and hazards at due intervals. A successful improvement can produce stable ordinary life without a new scripted crisis.

**Service model:** Demand, installed capacity, deliverable capacity and actual service remain distinct. Allocate useful configurations under §103, preserving minimum bundles, startup and handling delays; mere arrival or unused fractional capacity supplies no service. A city with sufficient total water may still leave one district without a viable connection. Building new pumping capacity does not fix absent treatment supplies. Track waste at collection, transport and final treatment/disposal; an absent service leaves physical accumulation when the profile supports it. Commute/travel access consumes actual time and capacity; a workplace elsewhere is not automatically available to every resident.

**Events/interfaces:** consumes arrival/departure, occupancy requests, utility changes, land-use decisions, work completion, hazards and budgets; produces `development_authorized`, `occupancy_changed`, `service_access_changed`, `maintenance_requested`, `development_accepted`. GOV handles contested authorization, INV incidents, WILD environmental effects, MED health response, CIV regional coordination. A project crossing multiple domains has one K-WORK owner.

**Example:** an empty school becomes a shelter. Existing rooms provide actual shelter under the profile, but staffing, food, sanitation and water remain separate. New occupants increase demand immediately, including while registration is delayed. Their private stores are not municipal inventory.

**Overrides/calibration/unresolved:** property/use rights, planning procedure, building/occupancy envelopes, service standards, work rates, demand, waste/storage effects, rents, accessibility and network performance need profiles. No universal desirability score, automatic zoning growth or happiness-to-population formula. Fantasy infrastructure must specify source, throughput, upkeep and compatible recipients. **Acceptance:** Appendix C CE-URBAN-01 through CE-URBAN-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

<a id="core-122"></a>
### 122 LIFE — Social, Legal Position, Generational and Personal Development

**Purpose and scope:** Support continuing individual and collective social existence independently of historical period or genre: kinship, residence, households, care, obligations, social position, constrained agency, practical custody, reputations, careers, learning, stratification, opportunity, retirement and succession. The universal mechanism describes who can do, claim, recognize, control, enter, leave or inherit *what*, under which institutions and actual conditions. A setting supplies its particular laws, customs, classifications, prohibitions, remedies, and expected behavior. **Status: proposed Core v3.3 replacement of §122, not adopted.** It subsumes the reusable workflows already inherited from Core §§14–18, 26/28, 38, 45–46, 64–70/76/96, Historical/Roman §§3–9, and Military §§3–5/11–13, without importing their local values.

**Dependencies and ownership:** K-ACTOR owns each person's identity, capability, condition, actual presence, and bodily/physical custody constraints. K-POP owns only residual cohorts and membership reconciliation. K-TIME owns commitments and effective event order. K-ORG owns membership, posts, mandates, duty allocation and institutional decisions. GOV owns jurisdiction, public/legal rules, legal classifications and recognized changes within its actual scope. ECO owns agreements, property/financial claims and settlement, while K-STOCK/K-ASSET own actual assets, title/custody and quantities. K-WORK owns real labor and output. K-INFO owns communicated claims, recognition by named audiences and beliefs. MED owns care episodes. LIFE owns household/care arrangements, social and relationship evidence, learning/career processes, life transitions, and estate/successor workflows. **LIFE never creates a second legal-rights ledger, independent cash or property balance, person count, work progress, or office registry.**

#### 122.1 Minimum records and differentiated views

```text
LIFE.Household: id; member_actor_refs; residence_ref; kinship_refs;
  common_use_agreement; care_affected_refs; resource/provision_refs;
  household_decision_limits; contributed_work_refs; review_events
LIFE.Relationship: id; directional_party_refs; dimensions_relevant_to_action;
  source_event_refs; audience_knowledge_refs; undertakings; changes/effective_time
LIFE.SocialPositionView: id; subject_ref; as_of; jurisdiction_refs;
  GOV legal classification/rights/restriction_refs; K-ORG memberships/roles/mandates;
  ECO/K-STOCK/K-ASSET ownership/claims/administration_refs;
  K-ACTOR actual custody/access/condition_refs; LIFE relationships/occupation_refs;
  K-INFO recognized/disputed assertion_refs; unresolved_dimensions
LIFE.DependenceArrangement: id; actor_refs; basis/terms; relevant decision authority;
  supervision/control; actual work/needs/compensation_refs;
  consent_or_compulsion_basis; exit/review_conditions; enforcement_refs
LIFE.Opportunity: id; target_role/status/asset_or_benefit; prerequisites;
  institution/access_authority; scarcity/capacity/competition; process;
  support/evidence_refs; unknown_or_disputed_conditions; decision_trigger
LIFE.Learning: id; actor_ref; objective; prerequisites; qualifying_activity_refs;
  time_and_feedback; demonstrations; assessment_scope; selected_progress_model
LIFE.Career: id; actor_ref; work/service_history_refs; terms; qualifications;
  current_role_and_competence_refs; advancement/restriction/exit opportunities
LIFE.Transition: id; type; initiation/evidence_refs; decision_authority;
  conditions; acts/work/notification; effective_time; resulting_owner_writes;
  unfulfilled_obligations; review_or_reversal_path
LIFE.Estate: id; person/estate_ref; asset/claim/debt_refs; custodian;
  jurisdiction/procedure; potential_successors_and_evidence; actual_transfers
```

`SocialPositionView` is derived; it cannot be used as a write target or single universal caste, class, liberty, virtue or status score. A person may have high income, limited rights, social esteem in one audience, no public office, and control assets they do not own. Each dimension can change without the others. A disputed legal claim, recognized social convention, practical obstruction and physical restraint are distinct states. **R2 validation:** Effective public/legal capacity changes must cite an actual jurisdiction-specific rule and supported completed act/competent decision, not merely a nonempty authorization token. The absence of that model remains an unresolved decision, never an automatic change or a universal modern legal default.

#### 122.2 Social and legal standing

1. Identify the person, applicable jurisdiction/institution, relevant rule and time. Rights may differ by place, role, activity and legal capacity; an obligation does not create the power to enforce it.
2. Separate a claimed classification, valid rule, formal decision, effective change, known/recognized change and practical enforcement. Record whom the recognition applies to. An unofficial title or ceremony does not automatically establish a public entitlement.
3. Determine actual opportunity to invoke or enforce the right, including people, records, travel, communication and available institutional capacity. A valid right need not already be accessible; an invalid command can still exert practical pressure.
4. Apply only the specified effect of the completed procedure. A change in citizenship, guardianship, membership, occupational license, household dependence, public office or contract terms does not automatically change wealth, skill, affection, physical custody or every jurisdiction's recognition.
5. Preserve pending challenges, conflicts, claims and obligations. A later reversal uses an actual authority/event and Core §99; it does not retroactively reverse unrelated work or transfers.

GOV supplies the locally applicable legal process; K-ORG stores granted role/mandate; ECO stores contractual claims. The social view only references their actual consequences. Historical forms of citizenship, estate, caste, slavery, guild status or class must be attached through a dated setting profile. Do not assume equal hearing, modern rights, hereditary succession, enforceable release or compulsory harm where the setting does not support them.

#### 122.3 Dependence, compelled work, custody, and release

People remain K-ACTOR people even if an institution treats them as transferable dependants or asserts a property-like legal claim. The simulator may record a *claim concerning a person* but must never represent the person as K-STOCK, turn restraint into consent, or duplicate them upon transfer.

For physical custody record subject, custodian, location, real means of control, guards/restraints, permitted movement, provision/care arrangements, asserted basis, relevant recognition, outside knowledge and pending action. Actual custody may contradict applicable law, the custodian's claim and third-party beliefs. A purported sale, arrest, detention, compulsory service, debt arrangement or surrender proposal has independent agreement, authorization, payment, handover, recognition and enforcement stages where material. No stage proves another by narrative implication.

Compelled work establishes a demand, not voluntary player compliance or free productive capacity. Determine task, actual tools/inputs, ability, schedule, supervisor, risks, provision/compensation arrangements, restrictions, opportunity for refusal/resistance and credible enforcement. Apply involuntary physical changes only through real means and effects; return player control before each unsupported voluntary choice. An NPC's threats do not create a successful task or manufacture an admission.

Release, escape, discharge, emancipation, invalidation of a claim and removal of restraint are separate events. For a consequential change select the route and prerequisites *before* spending scarce resources: claimant, decision authority, required acts, access, costs, timing, evidence, the exact field(s) changed and surviving obligations. Promise → eligible route → performed act → effective change → receipt/recognition → continuing consequences is a possible sequence, not an obligatory universal legal process. Missing local law requires a bounded explicit ruling rather than an invented universal right. Escape changes actual presence/custody immediately; discovery and search occur when supported observers act and messages arrive.

#### 122.4 Labor, provision, economy and social mobility

Distinguish free, contractual, compelled, household, reciprocal, civic, charitable and institutional labor according to the actual arrangement; those labels do not determine universal wage rates or output. Labor commits the same persons' availability as military, household and ordinary work. Work and equipment use K-WORK/K-ASSET; entitlements, unpaid wages, remittances and administered funds use ECO/owner records. Responsibility to manage a business does not confer legal ownership of its assets. A provision source serves the same recipient's need once.

Social mobility occurs through specific opportunities and transitions: education, demonstrated expertise, employment, patronage, investment, property transfer, marriage/kinship where enabled, institutional appointment, loss or acquisition of rights, public recognition, displacement, coercion, inheritance, emancipation or retirement. For each opportunity specify barriers, applicable rules, admission/assessment authority, competing demand, real vacant capacity, time, cost, actor decision and exact consequences. Wealth, rights, rank, skill, reputation and practical influence never move as a bundled `status level`. Both progress and durable stability are valid outcomes; loss requires an actual cause and event.

#### 122.5 Relationships, education and life continuity

Use Core §§14–16, 31, 64–70, 76 and 96 for capability, autonomous decisions, relationships, learning and succession. Track trust, respect, affection, obligation, loyalty, fear and resentment only when they affect decisions; reputation propagates through actual witnesses and channels. Persuasion obtains only a feasible named concession (§66). Neither roleplay narration nor an abstract social advantage selects the player's inner state or voluntary assent.

Training requires real time, instructional capacity, qualifying work, feedback and assessment. Use one selected progression schedule; no unqualified `training unit` conversion, automatic credential or skill award for office appointment. Biological aging, births, deaths, caregiving and household reproduction use selected species/health/demographic processes, not automatic daily story beats. Retirement or death may open estate and office processes, but inherits no guaranteed pension, child, successor authority, transferred skill or restored health.

#### 122.6 Execution and event interface

For a material LIFE event: (a) identify authoritative actors/rights/claims and what each knows; (b) establish feasible actions and governing institutions; (c) schedule authorized time, labor, access and inputs; (d) resolve meaningful uncertainty within the selected effect profile; (e) commit each actual physical/economic/institutional change through its owner; (f) propagate observation, report and recognition at their respective times; (g) update LIFE transitions/views once; (h) return control on new player decisions. An ordinary independent NPC household or enterprise continues off-screen under its actual delegated authority and finite means.

Subscribe to births/deaths, care needs, pay and provision, court or administrative decisions, custody/location changes, contracts, learning evidence, appointment decisions, relationships and household communication. Outputs may include `life_transition_opened`, `relationship_evidence_added`, `career_review_due`, `standing_view_invalidated`, `dependent_care_reassigned`, `estate_process_opened`. These are process notifications or derived view changes, **not duplicate owner writes**. No global daily standing roll is introduced; schedule only actual deadlines and configured process intervals.

**Example:** a legally restricted craftsperson operates a workshop for its owner, learns management, gains trusted clients, and later obtains a valid release under a local procedure. Workshop cash remains with its owner until transferred; practical ability and clients can persist through the legal change; whether the craftsperson can own property or hold public office depends on actual local rules. A distant audience may not yet recognize the release. None of those changes automatically confers military command or transfers another person's affections.

**Overrides, calibration and unresolved:** Dated legal jurisdiction and procedure, dependency arrangements, effective emancipation methods, education and opportunity, law enforcement, labor productivity, demographic transitions, household needs and social network propagation need setting/campaign profiles. Unresolved authority conflicts and unknown evidence remain explicit. This section introduces **no universal caste hierarchy, coercion effectiveness percentage, wage, fertility, mandatory social decay or numerical prestige progression**. New acceptance cases: CE-LIFE-05 through CE-LIFE-12 and combined CE-INT-01 through CE-INT-04 in Appendix C. Test declarations are not executed empirical evidence.

#### 122.R3 Household work, care and service-deficit records — proposed

A household's members may concurrently belong to military, civic and economic institutions while retaining distinct commitments. A person cannot supply full hands-on care, full agricultural labor and full military duty in one overlapping interval without a selected physically credible split-capacity profile. Genuine substitution must identify an actually available, authorized and capable provider, the time spent and its opportunity cost. Household welfare demands (care, meals, heat, shelter, support) derive from named needs or qualified cohort processes; responsibility does not imply actual delivery.

Required care, committed care, performed care and accepted care are distinct. Food production, stock at home, prepared meals, distribution and actual use likewise differ. Audits compare actual supported provision over the declared interval with the specified need. Deficits remain obligations, exposures or risk factors; they do not instantly generate a death, illness, emotional state, crime or cascade without a relevant selected model and causal trigger. Military leave or deployment changes actual availability only, not automatically the family's legal status, affection or finances.


#### 122.R5 — Households, service deficit and knowledge of disruptions (PROPOSED)

If a household's reserved provision is destroyed, record the physical location and quantity of the loss and the household's unmet claim/need separately. A delivered meal, currently planned meal, accepted obligation, service shortfall and eventual health consequence are distinct. Dependants and caregivers act from their actual information-receipt times and household responsibilities; the narrator may not use unreceived casualty or supply reports to rewrite their earlier choices. A person's military service, household membership, and paid civilian obligations continue to refer to that one actor.

#### 122.R6 — Household continuity during interrupted production (PROPOSED)

Care, meal preparation, provision and household consumption remain explicit K-WORK/K-STOCK effects. A grain-shortfall incident does not erase unrelated meals already prepared or custody and family responsibilities already performed. Household service audits reference actually completed care and delivered goods. Disrupted work may change income, availability and expectations, but legal standing, consent, injuries or household need consequences must be supported by separate rules and facts. Wage uncertainty remains a household-relevant claim, not an automatically settled monetary loss.

<a id="core-123"></a>
#### 122.R7 — Social obligation continuity through interrupted production (PROPOSED)

Household service requirements, wages owed and legal work claims remain separate from physical WIP or destroyed stock. A rejected tool, ration process, housing component or medical supply batch may delay actual delivery without erasing household need or creating an invented injury. Actual care, institutional assistance or new purchases require competent real actors, physical resources and clock time. Subsequent salvage or acceptance cannot rewrite previous family obligations, authority decisions or work already certified.

### 123 COMP — Competitions

**Purpose and scope:** Structured comparison under agreed rules: races, trials, examinations, exhibitions, tournaments, judged work, games and other bounded contests. **Status:** Proposed Core domain, building on Core §6's contested-objective rule and shared time/work/institutions. **Sports remain genre/module content libraries**, supplying particular disciplines, equipment, scoring and competition rules; no sport is a universal Core subsystem.

**Dependencies/ownership:** K-ACTOR owns competitors; K-TIME schedules; K-WORK owns preparation/performance tasks; K-INFO measurements and judge observations; K-ORG organizer authority; ECO fees/prizes; MED injury care; INV disputed conduct. COMP owns entry/eligibility decisions, ruleset, format, match/attempt records, scoring, standings and adjudication. It does not own separate stamina, injury or prize-money pools.

**Records:** `Ruleset(version, objective, permitted_methods, eligibility, safety/equipment_conditions, attempt_limits, time_structure/endpoint_validity, measurement/scoring, tie/no_result, interruption/forfeit, adjudication, appeals, resource_requirements)`; `Entry(competitor/team_refs, qualifications, consent/authorization, fees, status)`; `Fixture(schedule, participants, venue, officials, resources, dependencies)`; `Performance(action_contracts, actual_results, measurements, uncertainty, violations, effective_time)`; `Result(scoring_inputs, rules_version, provisional/final, adjudication, standings_effect, award_claim_refs)`.

**Procedure:**

1. Publish/select a complete ruleset before material commitment. Define how performance is compared and whether the activity is direct opposition, parallel performance, judged output or a scheduled series. Missing tie/disqualification rules remain explicit before they become outcome-changing.
2. Check eligibility, actual entrants, venue, equipment, officials, scheduling and access. Registration does not compel the protagonist to compete. Teams use real available members; one athlete/official cannot appear in incompatible fixtures.
3. Resolve preparation through ordinary time, learning, equipment and work. Rules can restrict methods, but cannot create physical capability.
4. Run the authorized attempt(s). Directly opposed objectives use one selected contested resolution. Parallel races compare supported progress over the same elapsed interval; judged outputs use actual work and recorded criteria. Do not roll each side again against the same opposed objective or reroll success as a scoring test without a distinct uncertainty.
5. Record measurement and scoring separately from true performance where judges/sensors are imperfect. Apply the published scoring/tie/interruption rules. A Mixed execution means a defined feasible partial/costly performance; “Mixed” alone does not mean draw, half points or injury.
6. Adjudicate protests using evidence and organizer authority. Preserve provisional results until finalized; a finding may correct standings and supported award obligations without replaying physical exertion. Preserve already settled transfers; §§91/99 correction and compensating-event procedures govern any recovery and replacement award. Neither a reversed result nor a replacement claim creates funds. Actual fraud/violence can invoke INV independently.
7. Settle authorized awards and fees through ECO, update reputation through actual reports, and schedule recovery or further fixtures with persistent conditions. Winning does not grant unrelated skill, universal fame or effortless promotion.

**Formats and fairness:** A symmetrical contest must not acquire an advantage solely from choosing which competitor is named first. If the inherited challenger-oriented d100 method is used, the profile must define reciprocal outcomes and Mixed handling and demonstrate relabeling symmetry for the particular scoring purpose. The naive mapping Success → challenger win, Failure → opponent win, Mixed → draw is invalid for equal interchangeable roles under net-zero inherited thresholds: its exact d100 enumeration is 41/29/30. This does not change the parent action-success engine for genuinely asymmetric actions. Otherwise use a declared symmetric performance model. Test relabeling, ties, differing capability, resource effects and repeated attempts before dependent use. Separate performance resolutions are allowed for genuinely separate performances, not two rolls against the same resolved opposed objective; equal-skill symmetry alone does not establish a calibrated progression curve. COMP supplies the contract, not a new numerical ranking formula. Qualifiers, seeding, handicaps, season standings and championship succession belong to a ruleset; they cannot be invented mid-contest to preserve drama.

**Events/interfaces:** consumes eligibility evidence, fixture availability, performance, measurements and protests; produces `entry_accepted`, `attempt_completed`, `result_provisional`, `adjudication_recorded`, `result_final`, `award_due`. An election uses GOV's eligible decision procedure even if it has campaigning and winners; ordinary market competition stays ECO; warfare stays the selected conflict engine. Only an actual rules-based competitive event invokes COMP scoring.

**Example:** two craftspeople submit finished objects to a judged exhibition. K-WORK records actual materials and quality; judges assess the published criteria using what they can inspect. A tie follows the established rule. The winner receives a prize claim, then actual payment when the organizer pays. Neither object is manufactured again at scoring.

**Overrides/calibration/unresolved:** specific performance models, disciplines, measurement error, officiating, scoring, attempt/recovery schedules and sport safety rules remain library/profile-owned. No universal sports attributes, injury chance, league points, prize values or fair-handicap formula. **Acceptance:** Appendix C CE-COMP-01 through CE-COMP-04. The stated acceptance cases remain requirements unless execution evidence is recorded.

#### Activity and measurement adapter contract

Bind each performance to the ruleset's permitted activity, actual competitor/team/means, compatible physical or work model, feasible outputs, authorized attempts and independent uncertainty. Bind measurement separately to actual evidence, resolution, clock basis, uncertainty and review access. Keep actual performance, observation, provisional score, final adjudication, standings and award claims as separate linked facts.

A sport or exhibition may have a complete administrative format while one physical calculation needs its selected profile. Entry, scheduling or funded contracts can proceed independently; an impossible interception or unsupported finish time cannot be supplied by a favorable timing roll. Replays, lap summaries and appeals create no new performance uncertainty for an unchanged completed attempt.

Changed adjudication applies the published procedure through existing records and compensating events. Actual payment remains paid; an award reversal creates only supported recovery/replacement obligations and funded transfers. It neither refunds exertion nor creates prize money. The Sports source's four format/career entries remain specialized content; numerical dimensions/attempt counts are declared format choices, not physiological calibration.

<a id="core-124"></a>
### 124 MIL — Armed Institutions, Military Life and Conflict

**Purpose and scope:** Enable a nation, city, clan, household, community or other actual institution to create, sustain, direct, deploy, use, disband and remember armed forces under the same persistent world simulation. Military institutions are ordinary world actors even when no military-focused genre engine is loaded. MIL coordinates military-specific plans, force organization, operations, readiness reviews, conflict consequences, personnel-service transitions and reintegration. It does **not** invent a separate troop population, war clock, map, treasury, supply source, wound pool, combat probability system or compulsory war event. **Status:** Proposed Core v3.3 domain extracted from Military Slim v1.2 and inherited Core §§25–63/64–76/113/117; not adopted or playtested.

#### 124.1 Dependencies and owner boundaries

- K-ORG owns armed institutions, formation structure, membership, rank/appointments, authority, doctrine adoption, credentials, command mandates and duty rosters; K-ACTOR and K-POP own the actual individually tracked members and residual cohorts, with exclusive disjoint coverage.
- K-TIME owns the one event frontier, actual duty periods and concurrent commitments. K-INFO owns orders' received content, intelligence, reports and uncertainty. K-NET owns route throughput and transmissions, not new transported supplies.
- K-STOCK/K-ASSET own actual stores, ammunition, weapons, mounts/equipment, transport, conditions, custody, locations and transfers; ECO owns claims/pay and budgets; K-WORK owns training, construction, preparation, repair and other performed work.
- GOV owns conscription/war policy, lawful force authorization, jurisdiction, institutional regulation, treaties and public mandates. LIFE owns members' households, careers and dependency/leave consequences; MED owns actual care; INV owns investigations. CIV assesses whole-society opportunity costs and strategic impacts. MAR and specialized modules own vessel and other physical/domain models.
- MIL owns **MobilizationPlan, ForceTask/Operation, DeploymentStage, EngagementSummary, MilitaryReadinessAssessment and AftermathWorkflow** as linked procedural records and views, not independent populations, effects or spending balances. A military-service record can be a K-ORG/LIFE service dossier with MIL annotations; a rendered force-strength total is a derived view.

#### 124.2 Records and minimum contracts

```text
MIL.MobilizationPlan: id; mandate_ref; scope/target; eligibility_rule_ref;
  recruitment_routes; potential_member_cohort_refs; actual_enrollment_refs;
  staff/training/equipment/supply_dependencies; scheduled_work_refs;
  funding_refs; reporting_and_review_events; completion/stop_conditions
MIL.ForceTask: id; responsible_KORG_force_refs; actual_membership_view;
  objective/decision_authority_refs; KINFO_order_refs; geographic/time_scope;
  real_assets_and_supply_refs; known_threat/evidence; required_effect_adapter;
  dependencies; commitments; stage/status; stopping/withdrawal_conditions
MIL.DeploymentStage: id; force_task_ref; type; prerequisites;
  actual_movement/work/issue_refs; readiness_review_ref; completed_event_refs;
  responsible_actor_and_handover; next_trigger
MIL.MilitaryReadinessAssessment: id; force_refs; as_of; mission/interval;
  actual_available_members_and_roles; qualification/command/function_refs;
  equipment/transport/supply/maintenance_refs; received_information_age;
  operating_limits; derived_conclusion; unresolved_factors; next_review
MIL.EngagementSummary: id; common_pre_event_boundary; participant_scope;
  selected_resolution/effect_refs; committed_actual_events; losses/withdrawal_refs;
  observation_report_refs; coverage_exclusions; unresolved_reactions
MIL.AftermathWorkflow: id; operation_ref; person/casualty/availability_refs;
  issue/consumption/repair_refs; report/evidence_refs; med/household/support_refs;
  command_review_tasks; return/continuation/closure_constraints
```

All quantities and memberships derive from their K-owner IDs. Unfilled mobilization targets are objectives, not real recruits; a forecast of ration requirement is not stores. Each record includes Core Appendix A's campaign-scoped ID, source, owner/status, effective time, visibility, revision and last applied event. `EngagementSummary` cannot apply damage a second time when aggregating a battle already resolved locally.

#### 124.3 Recruitment, military service and daily institutions

1. Confirm the actual sponsoring institution, recruitment/levy/conscription/contract route, scope of authority, eligible people, available positions, and required evidence or assessment. A public mobilization order is not an enrollment event; a reputation or reference is not a credential.
2. Identify authorization, qualification, consent where legally applicable, or specific compulsory mechanism. Compulsory recruitment is an institutional demand and possibly an involuntary constraint, **never manufactured voluntary consent** from the player. Refusal, evasion and enforcement follow real actors, access, rules and causes.
3. Record actual enrollment and service terms in K-ORG/ECO/LIFE, then separately assign a duty, roster slot, formation, station, issued assets and provisions through their owners. A title creates neither training, equipment nor a person.
4. Duty uses actual shifts, patrols, travel, standing watch, administrative work, exercise and standby constraints. A late relief does not silently extend a player's voluntary commitment. Actual handover transfers responsibility, knowledge and custody when completed, not when scheduled.
5. Training uses Core §§15/31/96/110/122 and the selected learning profile: qualifying hours, assessment, exercise, collective coordination, doctrine version, instructor/material capacity and genuine credentials are distinct. A replacement soldier changes the real roster and any supported coordination/capability state, without a new permanent arbitrary penalty.
6. Promotion, appointment, discipline, award, transfer, leave and separation require applicable terms, decision authority, evidence, communication and effective events. Service rank, office, current assigned command, qualification, trust and actual function remain independent. Unpaid earned pay is a claim; an issued item is still institution-owned unless its title is actually transferred.

#### 124.4 Formation, readiness and operational command

A formation is a K-ORG organization/group with named or coherent cohort member references, chain of authority, real equipment and a mission-specific operational capability binding. Establish type and role by setting/era profile: no universal squad/platoon/regiment structure, rank ladder, headcount, ideal ratio or combat unit. A nation's active armed forces and local militias use the same organization/person records, even if the campaign never enters a soldier-level scene.

Mission readiness is a **derived multidimensional assessment** of available people, relevant skills, cohesion, discipline, command links, transport, ammunition/fuel, provision endurance, serviceable assets, access, information quality and the intended interval. It is not a fungible readiness currency. Morale, cohesion, discipline and immediate suppression retain Core §§32–34 distinct meanings. A competent commander cannot negate an impossible route, absent ammunition, or unreceived order. Readiness can improve during peace without mandatory escalation.

For an order: establish valid sender/authority, intended recipients, achievable objective, constraints, means, time, channel and report requirements. Issue, receipt, comprehension, acknowledgement, commitment, execution and returned reporting may occur at different times. Autonomous subordinates act within their actual mandates and knowledge; chain of command is not omniscience or automatic obedience. Consider simultaneous demands across formations using K-TIME/K-WORK capacities.

#### 124.5 Mobilization and national-simulation integration

1. GOV authorizes a policy/mandate within applicable jurisdiction. CIV records strategic objective, competing civilian needs and regional consequences; ECO establishes funded authority and obligations rather than minting troop pay.
2. MIL establishes recruitment target, actual recruitment routes, eligibility/capacity and a feasible schedule. Distinguish potential eligible people, contacted people, applicants, actual accepted enrollees, inducted people, deployable people and the public count reported to leadership.
3. Every accepted person is transferred or linked to K-ORG membership once, with K-ACTOR/K-POP boundary reconciliation. If an aggregate labor cohort is reduced by individualization or service reassignment, do not duplicate workers or subtract both from the same total. A population extraction must retain the original cohort membership basis, selected counted subset, eligibility evidence, actor identity allocation and count delta in one atomic transition. A recruitment report or target does not constitute such an extraction. Training/qualification attestations used for readiness require a verifiable selected qualification/evidence contract: a free-text assertion is not certification.
4. K-WORK/K-ORG process actual instruction, equipment issuance and staff appointments; K-STOCK/K-ASSET/K-NET process actual provisioning/movement. Continued civilian production and household care reflect the actual people/time/inputs still available, not an abstract national military tax automatically charged twice.
5. MIL reviews mission-specific readiness and issues feasible operations; CIV/ECO/GOV adjust plans, not past stock. Mobilization may stall, partially succeed, be reversed or be demobilized without retroactive erasure of completed work or costs.

**National-simulation invariant:** `available_population_after` must equal the supported distribution of **the same actual people/cohorts**, not opening civilians plus newly created soldiers. Recruitment itself does not mean a death, migration or magical population increase. A citizen can be simultaneously a legal resident, household member and enlisted service member because these are relationships, but may not supply incompatible hours of labor at the same time.

#### 124.6 Deployment, engagement, and effects

Use task-relevant stages: mandate/warning → preparation → movement → arrival/handover → mission/engagement → relief/withdrawal → return/recovery → review. The actual workflow can omit inapplicable stages. Stage completion requires real events and prerequisites; arriving does not create a complete intelligence picture or refuel a vehicle.

Before fighting select the smallest necessary resolution scale (Core §§47–63/84): identify participants, positions, available actions, authority, committed time, actual ammunition/equipment, visibility, terrain, weather, communications, objectives and withdrawal conditions. Use one compatible action/effect model per cause. Tactical numeric envelopes—projectile behavior, formation frontage, armor penetration, naval damage, aerial engagement, science-fiction weapons and specific species effects—belong to selected specialist profiles, **not to MIL itself**. Missing consequential parameters block dependent effect calculations and may allow other tasks to continue. A generic favorable roll cannot make an impossible shot, movement or penetration feasible.

At aggregate scale bind scope, interval, disjoint participants, coverage of local events, uncertainty and the selected model. Resolve effects once against actual K-ACTOR/K-ASSET/K-STOCK records; the `EngagementSummary` only references those events. A simultaneous exchange shares the same pre-event boundary under §11; do not allow a casualty report to produce additional casualties or a scale shift to restore readiness/exertion. National, operational and individual views are projections of the same battle history.

Warfare can damage civilian infrastructure, block transport, injure noncombatants, strain institutions and cause displacement *when* the actual actions, effects and dependencies support those results. MIL passes event references to MED, WILD, URBAN, LIFE, GOV, ECO and CIV as relevant. It never declares an automatic empire collapse, insurgency, famine or enemy reinforcement merely because a battle was won or lost.

#### 124.7 Status, casualty handling, recovery, and civilian continuation

Separate actual death, injury, capture, disappearance, restricted duty, reported missing status, administrative casualty classification, receipt of a report and relatives' knowledge. In particular: actual injury changes the person once; operational availability derives from the new condition and role; a delayed headquarters report changes knowledge once. Captivity changes physical custody/access through K-ACTOR and relevant legal claims; a missing-person notice neither creates a death nor triggers an automatic estate transfer.

After a mission audit actual headcount/capability, equipment/ammunition, repair, supply, care, payroll, orders, civilian harm, intelligence, evidence, remaining duties, reserve needs, household contact, training and demobilization. Tasks persist as normal K-WORK/K-ORG/ECO/LIFE/MED records. Leave/rotation does not automatically heal, settle wages or restore family relationships. Veterans may resume civilian work, pursue careers, remain disabled, teach, receive contractual benefits or live peaceful lives; no war escalation is mandatory.

#### 124.8 Events, scheduling, interface and activation

MIL subscribes to mobilization authorization; candidate enrollment; duty start/relief; training/assessment; order or intelligence receipt; maintenance/asset acceptance; deployment stage completion; injury/death/absence/capture; material stock/use; actual payment/remittance; conduct/recognition decisions; and service exit. MIL may emit `mobilization_plan_opened`, `force_requirement_revised`, `military_assignment_requested`, `readiness_recalculated`, `deployment_stage_completed`, `engagement_summary_committed`, `aftermath_opened` and `demobilization_requested`. All physical, institutional and financial changes write through the existing qualified owner—not an independent MIL event clock or storage.

Activate only as required: no military exists unless actual organizations, eligible people and resources exist, and not all nations maintain standing forces. A campaign may run national and military administration using Core without loading the Military Life genre, while attaching a branch/era profile or historical setting library to determine material outcomes. `IRGS-MLS-SLIM-1.2` remains available as a **source and compatibility reference** until a separate receiving rebind verifies every military service function; no existing campaign is automatically migrated.

**Acceptance:** CE-MIL-01 through CE-MIL-12 and CE-INT-01 through CE-INT-04 in Appendix C. **Calibration requirements:** recruitment/retention rates, training envelopes, doctrine, organizational ratios, daily provision, physical effect laws, logistical throughput, casualty risk, fatigue, morale/coordination, medical prognosis, intelligence and off-screen aggregation depend on explicit profiles and executed validation. No canonical numbers, inevitable military victory rate or readiness scalar are created by this integration.

#### 124.R3 Armed service and productive labor coexistence — proposed

Core MIL owns the service/muster/operations workflow but **not** a shadow labor force. Enrollment changes K-ORG membership. A subsequent authorized duty commitment uses existing K-TIME/K-WORK/K-ACTOR availability and may require actual release from civilian work. Military training, repairs, farming, healthcare and provisioning all compete for trained people, time, sites and stocks; a legal mobilization order can leave duties unfilled until implementation. Demobilization frees future availability when effective but neither reinstates former employment nor cures injury, debt or depleted stock. Civilian labor absence, alternate provision, tax receipts and field logistics must feed CIV's same national assessment without double-counting.


#### 124.R4 — Armed-forces participation in selective transactions (PROPOSED)

MIL's recruiting, equipping, deployment, pay and casualty requests declare shared K-ORG/K-ACTOR/K-TIME/K-STOCK/K-WORK owner footprints and qualified K-POP contributions. Two commands requesting the same remaining kits or service hours share a contention component; a physician's separate care job or farm's prior funded work can proceed. MIL readiness remains derived from *actual* people, available time, supported qualifications, equipment and relevant effects. No blocked requisition converts itself into deployment, nor does a strategic report credit unpaid wages or replaced casualties. Later legal/financial decisions require their own effective events and cannot backfill earlier readiness.


#### 124.R5 — Operational losses, requisitions and tactical/strategic continuity (PROPOSED)

MIL's food, ammunition, equipment, payroll and personnel records share Core K-STOCK/K-ACTOR/K-POP/K-ORG/K-TIME owners with civilian ECO/LIFE. An involuntary destruction event immediately affects actual physical holdings; preexisting military requisitions become shortfalls if no longer supportable, not negative stores or magically funded shipments. A battle's resolved incapacitations and ammunition expenditures are committed at tactical resolution once, then projected into operational readiness, communications and strategic summaries. Multiple unit reports about the same encounter are distinct information events rather than additional losses. Neither movement from individual actor scale to formation scale nor later demobilization resets fatigue, casualties, ammunition, obligations or world time.

Active military losses and transfer requests require specialized competent adapters for injuries, weapon penetration, ammunition units, convoy cargo, leadership decision rights and observed-versus-received intelligence. The R5 reference's synthetic effects do not stand in for those adapters.

#### 124.R6 — Military and civilian work competition during recovery (PROPOSED)

MIL mobilization, garrison supply and requisition use exactly the shared working-time, personnel, production, transit and stock records. An army cannot take replacement seed from a civilian job's reservation by a bare narrative claim; the applicable legal/command order, actual access and allocation must be established. An interrupted civilian shift is not silently replaced by military duty, nor does demobilization automatically satisfy the farm's previous contractual work. A mobile unit's own medical, repair or provision jobs obey the same milestone and shortage distinctions where applicable, with specialist tactical effect models remaining optional.

#### 124.R7 — Military provisioning from unfinished civil output (PROPOSED)

A military requisition cannot count a workshop's incomplete goods as issued finished equipment. The army may claim, reserve or fund production through Core ECO/K-WORK/K-STOCK, but must receive actual qualified completed stock (or explicitly configured field-use intermediate) before readiness or issued-equipment state changes. A physical loss to incomplete equipment is reflected in the same source ledger as civilian losses; it is not counted again as a second tactical casualty or logistics loss. MIL domain governance, obligation and allocation procedures do not override manufacturing feasibility.

## Appendix A — Owners, Status and Minimum Records

An owner is a logical authoritative record/procedure, not necessarily a separate file, office or app. Domains request changes through owner-qualified transactions; they never copy another owner's mutable totals.

| Owner | Authoritative state | Boundary |
|---|---|---|
| K-TIME | Clock, queue, commitments, processed spans, retained resolutions, campaign-scoped journal | Reviews and panels do not create time or reapply events |
| K-ACTOR | Individual identity, goals, physiology/capability, bodily conditions, actual location/custody constraints and availability | Knowledge refers to K-INFO; a machine embodiment refers to its physical owner |
| K-STOCK | Fungible/product quantities or the selected monetary balance representation; specification, owner/title, custody, location, eligibility, reservation/backing refs | Claims, capacity, forecasts and duplicate monetary representations are excluded |
| K-ASSET | Identified physical assets/components, configuration, condition/faults, containment and their title/custody/location | One actual asset is not an independent counted stock copy; contained lots remain K-STOCK references |
| K-WORK | Tasks, stages, actual useful work, transformations, accepted outputs, completion/acceptance | Programs and care episodes reference this work, not another progress counter |
| K-INFO | Observations, assertions, source lineage, reports, beliefs, received/understood information and access | Physical exhibits/media retain physical custody under their owner; beliefs can disagree with truth |
| K-ORG | Organizations, offices, mandates, roles, qualification/credential decisions, staffing links, procedures and succession | Capability evidence stays with actual actors; decisions granting public authority belong to GOV |
| K-NET | Routes/links, shared operating capacity, supported service configurations, allocations, buffers by reference, actual delivery | Installed assets, stock buffers and physical users retain their own owners |
| K-POP | Residual cohorts under declared population/species profiles, membership and presence links | Individual location remains K-ACTOR; named expansion conserves the residual total |

GOV owns jurisdiction/decisions/public agreements; ECO agreements/orders/claims; INV cases/hypotheses/disposition; MAR voyages/operating-envelope/compartment workflows; CIV programs/strategic assessments; MED care episodes; WILD habitat/renewal processes; INTEL requirements/assessments; URBAN development/access plans; LIFE household/relationship/learning/career/estate workflows and derived social-position views; COMP rulesets/fixtures/results; MIL mobilization/operation/readiness/aftermath workflows (all force personnel and property remain with their K-owners). These records reference K-state. A vessel's physical breach is a K-ASSET fact; MAR can own the resulting modeled compartment process while referencing its actual affected component.

People remain actors, including when detained or subject to disputed institutional claims. Do not represent a person as a stock lot. A newly named animal/construct likewise needs a declared population/identity treatment, not automatic extra human residency.

#### Status contract

| Label | Meaning |
|---|---|
| Established/Core | Inherited shared behavior within its actually adopted scope; no claim of universal campaign adoption |
| Genre-owned | Specialized behavior/parameters belong to that genre; ownership alone is not acceptance |
| Campaign precedent | Evidence from one implementation, without rule or lore transfer |
| Proposed | New/promoted/reconciled design awaiting acceptance |
| Accepted | Explicitly accepted design within recorded scope; separate from campaign deployment |
| Playtested | Named version actually used in recorded play under stated conditions |
| Calibrated | Particular values evaluated against declared targets/evidence |

Store design status, adoption status and validation evidence separately. Scripted examples, reference assertions, seeded synthetic runs and live play are different evidence. Publication, a passed invariant or a source's certification phrase does not change those statuses automatically.

#### Minimal shared records

Common fields: `id, campaign_id, owner-qualified type, schema_version, effective_time, provenance/source, authority/status, visibility/access, record_version/last_applied_event`. Values distinguish known, estimate with rationale/bounds, unknown and not applicable. References retain campaign scope. Equivalent concise prose can supply these meanings.

| Record | Meaning required where consequential |
|---|---|
| ActionContract | Actor/objective/method/target; actual scope; authorization/time/spending/stop limits; means; feasible result; exposure; adapter and retained resolution; Mixed branch |
| Commitment | Actor/asset and task; place; start/end/stop; capacity/attention; overlap compatibility; instructions/mandate refs; endpoints; interruption and next decision |
| Event | Scoped ID and recoverable payload; causal parents/time; coordinator; owner-qualified expected-state/write set; action instructions; institutional validity; visibility; dependencies/status |
| Reservation | Obligation/order; eligible specification/lot/pool; quantity; owner/access/timing; unique backing or unresolved allocation; shortfall/priority policy; release/cancellation |
| StockLot | Specification/unit/physical quantity; owner/custodian/location/container; usability/contamination; lineage and reservation refs |
| Condition | Actor/component/function; cause/onset; supported actual state; assessor/belief/uncertainty; restrictions; deterioration/recovery profile; next causal review |
| WorkItem | Deliverable and stage; units/rate; actual qualifying assignments/inputs; parallel cap; completed/remaining work; acceptance; process span and stop conditions |
| Function/Service | Provider/scope/quality/users; demand; installed/feasible/allocated/delivered capacity; actual dependency refs; useful bundle/divisibility/exclusive slots/reduced modes; start/run/restart/acceptance |
| TimeProcess | Owning state refs; update law; units; causal interval/continuous interpretation; thresholds; last processed spans/boundaries; supported numerical method/tolerance if approximate |
| Observation/Assertion | Material assertion/component ID; origin/source/event; collection method/time; accessible content; actual/claimed/known lineage; uncertainty/preservation |
| Report/Belief | Assertion/evidence refs; interpretation and dependence; sent/received/understood; recipients/access; confidence rationale and review |
| PopulationMovement | Actual individual/cohort refs; origin/transit/destination; departure/arrival; cargo/ownership; continuing needs/care; affiliation and knowledge |
| Claim | One obligation; debtor/creditor/unit/basis; accrued/settled/adjusted amounts; due/dispute terms; linked payment/correction events |
| DefinitionRef | Namespace/source, exact entry ID/version and selector; original alias; candidate/canonical status and retained model |
| CapabilityBinding | Task/function; definition/model versions; actual actor/asset/site refs; real mode/means; scope/interval; required parameters and limits |
| EmbodimentBinding | Actor; actual physical embodiment; owner-qualified component/condition refs; controls; dependency profile |
| ProvisionView | Consumer/function; current-stock/completed-provision/forecast basis; interval; attributable source/use/portion refs; quality/eligibility; assumptions |
| AdoptionBridge | Old/new meanings and procedures; owners; preserved fields; source/models; exact override/scope/effective time; conversions/unresolved gaps; snapshots and evidence |
| Workflow | Domain/owner/objective; affected refs; prerequisites; responsible actors; instructions and institutional authority/knowledge; actual commitments; state; completion/stop; next trigger; unresolved fields |

Required meanings survive compact journals, saves and scale changes (§86). A payload hash, summary panel or unrecorded reasoning cannot substitute for missing recoverable state. Hidden state requires actual private persistence; no such capability is promised by this specification.

## Appendix B — Inheritance, Deployment, Migration and Calibration

#### Candidate Core 3.3 consolidation gate — proposed, not selected

The v3.2 deployment and engine-binding rules below remain descriptive of the **selected v3.2 parent**, not automatic certification of this candidate. Before any actual adoption: (1) explicitly authorize the candidate; (2) reconcile every enabled engine/setting binding, manifest and exact content/profile pin; (3) show that Military Slim §§3–15 have no lost function and that Roman Slim §§3–4 still inherit the correct LIFE/GOV/ECO/MIL owners; (4) execute CE-MIL, CE-LIFE and CE-INT regressions with snapshots and independent runners; (5) document campaign-specific effective time and state mapping, if requested. Historical event IDs, state, knowledge, stores, injuries, service arrangements, manumission and office decisions are not backdated or recalculated. The reference Military Slim and accepted Roman Slim remain valid within their existing selected scopes.

The proposed receiving manifest is a **compatibility review tool**, not a substitute for the active `IRGS_Engine_Bindings_v3_2.json`. New binding IDs and hashes must be finalized only for an actual adopted rebuild. Retain both old and proposed artefacts with clear source identity; never silently rebind a currently running campaign.


#### Minimum slim-engine manifest

```text
engine_id/version; design/adoption/validation status; core_id/version;
required Core services/domains; genre-specific purpose and mechanics;
setting/theme modules and explicit exceptions; content versions/aliases;
selected resolution/effect/physiology/load/needs/recovery/learning profiles;
parameter units/source/bounds and required activation fields;
extension-owned records; Core read/write interfaces; consumed/produced events;
triggers/causal intervals; actual access/knowledge/detection rules;
completion/interruption/recovery/termination; tests and unresolved fields;
prospective overrides, effective scope/time, old/new mappings and snapshots.
```

A slim engine repeats neither the Core event loop nor stock, wounds, work or population ledgers. It identifies its special mechanisms and selected implementation profiles. The Core owns shared behavior; content supplies type definitions; the campaign profile selects calibration, tone, geography, local institutions, enabled modules and overrides; actual entities remain state.

#### Genre application boundaries

| Source/extension | Shared inherited behavior | Retained owned behavior |
|---|---|---|
| Fantasy engine/content | Core action/capability, condition interfaces, biology/ecology, learning, work, institutions, shared content contract | Selected attributes, load/travel, Threat/Defeat/Resistance/stress/body tables, training schedule, extraordinary resources/powers and content profiles |
| Military Life/Equipment | Shared commitments, assets, crew, stocks/rates, work, readiness, support, learning, life/institutions | Entry/service, branches/ranks, deployment, doctrine, military discipline/justice, selected military morale/cohesion/suppression and era/family content |
| Post-Apocalyptic specialization | Neutral needs, sites, handling, services, population, institutions, support, routes, programs and incident-linked assessments | Crisis grouping/history, legacy depletion/dependency, refuge/displacement, institution fracture, regional recovery and successor-society overlays |
| Roman extraction | Shared channel guard, harm reassessment, bounded establishment, ordinary functions, social fulfillment, autonomous obligations, standing, competence and journal semantics | Roman law/currency/status, actual institutions/prices/history, selected physiological/combat/training numbers and campaign death model |
| Any future genre/module | Existing shared procedure at its valid owner; explicitly declared specialized effects and state interfaces | A genuinely new phenomenon keeps its mechanism until a portable parent is actually designed/tested |

These bridges apply only after explicit scoped adoption. A library reference is not campaign adoption. Provider compatibility does not certify a complete genre implementation. Specialized records use declared compatible interfaces without importing campaign lore.

#### Numerical/profile reconciliation

| Interaction | Retained source difference | Binding decision |
| --- | --- | --- |
| Resolution | Shared d100 default versus established campaign d20/other adapters | One selected interaction adapter; no scale-by-five conversion or automatic new initiative rule |
| Training | H uses 4 hours/TU; F uses approximately 20; advancement thresholds also differ | Store real qualifying hours/evidence and selected schedule/version; no automatic favorable conversion |
| Character capacity/load | Fantasy attribute-derived kg/ratio model versus Historical optional slots | One selected load/physiology model; physical bulk/containers remain real without duplicate encumbrance |
| Protection/injury | Fantasy Threat/Defeat/Resistance chain versus Historical optional severity/protection steps | One complete compatible chain or an explicit bridge; no stacked mitigation |
| Recovery | Fantasy phases/broad windows versus Historical care-day counters | One condition and selected pacing model; no double healing progress |
| Deprivation/fatigue | Different need transitions, load/fatigue accrual and food-deficit abstractions | One representation per actual cause; forecasts are not second penalties |
| Materials/equipment | Broad material/era families versus model properties | Identity/requirements may transfer; quantitative performance requires actual specification/model |
| Body/creature effects | Biological anatomy versus machine components | Owner-qualified embodiment; applicable biology/component model; no generic humanoid hit table |
| Relationships | Optional −3..+3 dimensions versus contextual records | Preserve meaning/evidence; no military morale used as affection or city confidence |
| Power/heat/extraordinary resources | Energy/power, heat burden, neural strain and Fantasy PU have different meanings | Keep units, access, costs and profile scope; never combine into universal “energy” |
| Competition | Asymmetric execution outcome curve versus interchangeable contest roles | Use a ruleset-appropriate adapter; symmetry is a gate, not proof every activity needs a coin flip |
| Extraordinary effects | Paradigms/modules define access, costs, channels and causal exceptions | Compatible owner events for real effects; no lore, free restoration or implicit death/agency override |

**Training illustration:** using the source's nominal 20-hour Fantasy display unit, 40 qualifying hours display as 10 Historical TU or approximately 2 Fantasy TU. H's 24×4 threshold and F's 20×20 threshold are 96 versus nominal 400 focused hours for the compared advancement. Neither time alone proves competence, and this comparison calibrates neither model.

**Fantasy effect guards retained together:** stopped primary attacks terminate; Resistance 0 bypasses the reduction table; separate secondary channels need actual defined mechanisms; Sunder affects material stress rather than flesh injury; local damage stays local; ordinary natural-weapon profiles already include normal anatomy/scale; integrated armor is not a sum of entire independent resistance profiles. These remain safeguards inside the selected Fantasy effect package, not a new universal numeric combat system.

#### Activation data by domain

The following are proposed content slots, not a claim these libraries already contain finished entries. Reuse a supplied entry when its mechanism fits; add a variant only for a real difference.

| Core domain | Content belongs in library/profile | Minimum activation data |
|---|---|---|
| GOV | Regimes, offices, customary/legal procedures, treaty forms | Jurisdiction, deciding actors/process, actual authority and implementation means |
| ECO | Trades, commodities, enterprises, currencies, financial instruments | Specification, counterparties, terms, real input/capacity/stock and payment method |
| INV | Offense definitions, forensic methods, investigative organizations | Questions, access, evidence method, applicable institutional process |
| MAR | Vessel classes, propulsion, seamanship methods, ports, naval doctrine | Operating envelope, route/weather, crew, handling and relevant failure behavior |
| CIV | Governance/network arrangements, regional programs, historical contexts | Regions, dependencies, authority, institutions, resources and aggregation scope |
| MED | Care methods, equipment, facilities, disease/physiology profiles | Effect scope, qualified people, inputs, care objectives and actual condition |
| WILD | Biomes, species, crops, routes, climate/hazard profiles | Existing habitat/source, process boundaries, season, method and supported renewal |
| INTEL | Collection channels, institutional mandates, source/analysis methods | Accessible information, actual source/channel, timing, exposure and recipients |
| URBAN | Building/service types, habitation forms, planning standards | Site/rights, people, assets, networks, demand and acceptance |
| LIFE | Careers, household forms, education, cultural practices, lifespan models | People/obligations, selected progression/biology and social/legal context |
| COMP | Sports, games, examinations, craft exhibitions, tournament formats | Complete ruleset, feasible performance model, participants and adjudication |

**Sports content starter schema:** `sport_id/version, governing_rules_version, discipline/methods, team/role_requirements, field/course, equipment, permitted_actions, timing, performance_adapter, scoring, ties, substitutions, rest/interruption, fouls, officials, appeals, season_structure, costs, care_interfaces`. Values stay unset until selected. One sport may require new specialized ball/vehicle/body interaction mechanics; those belong to its module if the generic action/position engine cannot represent them. COMP still owns the contest lifecycle.

**Non-sport example:** a craft exhibition selects criteria, submission deadline, qualified judges, ties and award terms. It uses COMP without sports physiology or team formations. **Sport example:** a footrace variant selects course geometry, distance, start/finish measurement, pacing model, interruption and tie procedure. It uses the same COMP lifecycle; this Core supplies no running speed. **Boundary example:** rival shops use ECO competition for customers, not a compulsory tournament bracket.

#### New deployment

1. Pin exact Core/genre/theme/library/profile versions and status. Declare active domains and unresolved model choices.
2. Establish one campaign scope, clock, owner register, event journal and supported persistence/privacy boundary.
3. Initialize the actual actors, sites, assets, stock, institutions, knowledge, commitments and due events needed for the first decisions. Use §79's bounded policy for unresolved detail.
4. Supply only outcome-changing rates/effect/procedure fields. Supported ordinary functions proceed without filler measurements; missing material parameters remain explicit.
5. Exercise relevant acceptance cases and one cross-domain trace under the selected profiles. Record observed outputs/defects without calling a scripted trace a playtest.
6. Begin at a meaningful decision and run §90. Initialization, adoption and source review advance no world time.

#### Existing-campaign migration

Freeze the last valid decision snapshot/journal without advancing time. Identify existing adopted corrections first. Preserve IDs, quantities, title/custody/access, locations/transit, bodily/component conditions, earned competence/evidence, actual knowledge, claims, completed work, commitments, retained outcomes, pending queue and resolved history. Save pre-migration and mapped states.

Map only supported meanings and declare effective time, rule/profile changes, override scope, conversions, grandfathering if explicitly selected, unresolved fields and recovery reference. Do not infer past training hours from a skill rating, manufacture injuries from another HP system, add pumps/crew to an incomplete vessel, or grant private information to a successor. A migration grants no money, repairs, healing, people, supplies, progress or authority.

| Changed interface | Specific migration gate |
|---|---|
| Nine owners/domain workflows | Replace competing summary totals with references; preserve actual facts, not new default records |
| Event coordinator | Preserve scoped payload identity, processed spans, retained outcomes, unresolved allocations, dependencies and queues; no replay during mapping |
| Reservations | Preserve stock and obligations; derive unique eligible backing under supported shortfall policy, otherwise keep allocation unresolved |
| Payment/claims | Reconcile cash, custody/title and settlement references; no invented historic payment or automatic recovery |
| Services | Add only supported useful bundles/divisibility/whole slots/restart requirements; unknowns remain unknown and past output remains actual history |
| Time/process law | Preserve existing processed history; change future law from its effective boundary with units/schedule/tolerance recorded |
| Authority/deadlines | Preserve actual acts and recipient knowledge; new endpoint/revocation terms do not retrospectively disqualify resolved acts |
| Evidence | Keep prior observations and beliefs; add assertion lineage only from evidence; hidden origins remain hidden to recipients |
| Care/embodiment | Link plans to the same condition/component; no extra wound or restarted healing counter |
| Population/scales | Remove individually expanded members from residual cohorts; preserve conditions, private property, presence and local-scene exclusions |
| Content references | Pin exact alias/selector/model; preserve actual allowed modes and state; holds/deprecation gates remain closed |
| Competitions | Ongoing rules stay pinned; new scoring/priority applies prospectively; reversed awards use supported compensation rather than erasing payment |
| Roman clarifications | No reroll of old availability, reopening completed concessions or retrospective worsening of every prior injury |

If a needed function was delegated to Core but is absent from the actually adopted parent, explicitly retain/select the old bounded compatibility implementation or complete the adoption bridge before dependent use. Do not silently omit startup, operating bundles, commissioning, content selectors or any required behavior. Independent known events continue while a different calculation is unresolved.

Core 3.2 supplies the complete current shared procedures and bindings. Version selection records compatibility and effective scope; publication applies no campaign migration.

#### Calibration and unresolved implementation

The structural rules are usable with qualitative capabilities and concrete records. A numerical simulation needs a named parameter profile with units, source/status, valid range, rate/capacity, input/output conversions, dependencies, thresholds, uncertainty, stop conditions and recovery. Missing parameters block only the dependent calculation. Do not invent precision to complete a table or hide a proposed ruling as established fact.

| Family | Still unresolved | Evaluation target |
|---|---|---|
| Political/institutional | Context-specific procedure, discretion, compliance and legitimacy evidence | Outcomes trace to actors/authority; administration remains feasible without protagonist intervention |
| Economic | Demand, quotes/price discovery, finance and macro feedback | Finite orders/inputs; claims reconcile; no guaranteed profit or spontaneous purchasing power |
| Investigative/intelligence | Method reach, detection, source reliability, evidence evaluation | Good methods yield reachable evidence; uncertainty and source dependence persist |
| Maritime | Operating envelopes, stability/flooding, voyage performance, fleet contact and damage profiles | No skill-created buoyancy or instantaneous rescue; thresholds tied to vessel state |
| Strategic/demographic | Cohort resolution, regional time steps, birth/death/migration processes | Detail/aggregate conservation; uncertainty stable across reporting cadence |
| Medical | Physiology, efficacy, urgency, recovery, service capacity | Condition-specific effects; capacity and elapsed time constrain care |
| Ecological | Renewal, seasonality, extraction yield, interspecies and habitat feedback | Sustained output comes from actual regeneration; extreme harvest affects supported dependencies |
| Urban | Building/service capacity, maintenance, access, land-use impact | Constructed assets deliver only supported service to actual users |
| Social/life | Development/aging, training, institutions, care, relationship interpretation | Agency preserved; finite schedules; successors have independent identity |
| Competitions | Symmetric performance, scoring, judging, scheduling and incentives | Outcome not biased by arbitrary labels or extra rolls; awards funded |
| Runtime burden | Required detail, queue growth, cross-domain triggers, hidden persistence | An independent runner can reconstruct next legal action from checkpoint; summaries stay read-only |

Before calibration, specify what the model should reproduce or what decisions it should support. Test one parameter family against fixed cases; retain scope and evidence. Mathematical consistency does not establish realism, fairness, fun or balance. No external empirical research was used for new numerical claims in this edition because no such claims are made.

Core 3.2 supplies no invented physical rates. Service configurations, shortfall priorities, deadline semantics, process laws/solver tolerances and supported evidence dependence require scoped profiles where outcome-changing.

Open questions requiring later design or a campaign choice include: which symmetric multi-competitor performance model to adopt; how much ecological feedback a campaign needs; what evidence model merits numerical confidence; which financial institutions exist; which vessel families receive detailed envelopes first; and how to aggregate population without hiding politically or medically relevant differences. The answer need not be universal. A selected simpler profile is valid when it preserves the decisions at stake.

For each numerical/profile decision record purpose/target, unit, formula, inputs/dependencies, valid range/extremes, adjacent causes, uncertainty, stop/recovery, evidence/status and acceptance cases. Synthetic fixture arithmetic is not empirical evidence. Qualitative supported envelopes can be sufficient where precision would not improve a decision.

This is a written parent specification, not a complete production simulator or assurance that an AI will run every clause correctly. Outstanding work includes full-domain implementations, context-specific performance/care/effect/ecological models, multi-competitor competition adapters, live cross-domain playtests, queue/bookkeeping measurements and independent checkpoint reconstruction. Missing physiology, engineering or finance rates are not filled with attractive table values.

## Appendix C — Acceptance Cases and Regression Requirements

#### Candidate unification acceptance — unexecuted requirements

| ID | Scenario | Expected invariant / failure condition |
|---|---|---|
| CE-MIL-01 | GOV issues order to recruit 1,000 from a real population | Order creates target; only actual entrants change membership; no soldiers spontaneously appear. |
| CE-MIL-02 | One recruit belongs to a household, workforce and formation | Same actor; overlapping memberships valid; overlapping hours of labor invalid without an actual schedule. |
| CE-MIL-03 | Incomplete equipping/training at mobilization deadline | Only supported ready personnel/means can deploy; shortfall does not fabricate weapons or readiness. |
| CE-MIL-04 | War funds approved but not paid or stocks delivered | Authority/claim is not cash, ammunition, rations or physical custody. |
| CE-MIL-05 | Order reaches remote formation after its deadline | No anticipatory response; preserve issued/received/execution timestamps. |
| CE-MIL-06 | Two units compete for one transport corridor and stores | Capacity and stock allocated once; one unit cannot consume another's delivered supply. |
| CE-MIL-07 | Tactical encounter then strategic campaign aggregation | Exact same losses, exertion, ammunition and effects once; processed local interval excluded from aggregate. |
| CE-MIL-08 | Simultaneous exchange kills/disabled both combatants | Same pre-event state; resolved attacks honor actual commitments; later report does not wound again. |
| CE-MIL-09 | Injured member reported missing then captured | K-ACTOR condition/location/custody independent of report; no duplicate headcount losses or premature estate. |
| CE-MIL-10 | Demobilization and equipment return after ceasefire | Army membership/authorization changes; property transfer, unpaid pay, injury and pension claims persist independently. |
| CE-MIL-11 | Peaceful decade with garrison duty/training | Autonomous work and civilian lives continue; no mandatory conflict or readiness reset. |
| CE-MIL-12 | Naval/air/fictional unit requests missing tactical envelope | Core MIL can administer service/stock/duty; dependent physical calculation remains blocked pending specialist model. |
| CE-LIFE-05 | Wealthy person lacks civic standing but manages employer's shop | Wealth, public rights, practical control and ownership remain independent. |
| CE-LIFE-06 | Constrained worker is ordered to perform impossible task | Demand cannot create competence, material inputs, output or player consent. |
| CE-LIFE-07 | Captured person moved; third parties have not learned | Actual K-ACTOR custody/location change; GOV status and K-INFO recognition unchanged until their own events. |
| CE-LIFE-08 | Payment for purported transfer of a person | Record transaction and contested claims separately; person is never K-STOCK or duplicated. |
| CE-LIFE-09 | Release promised, qualifying act not yet performed | Undertaking does not change effective standing or custody automatically. |
| CE-LIFE-10 | Effective local emancipation recognized by some audiences | Exact legal fields and effective time change once; no automatic wealth, skill or universal recognition. |
| CE-LIFE-11 | Guild official appointed despite limited craft competence | Mandate may change while skill and qualifying work remain unchanged. |
| CE-LIFE-12 | Caregiver mobilized; household lacks replacement | Civilian care capacity and labor adjust through same time/person; no invisible substitute or duplicate meal. |
| CE-INT-01 | Kingdom recruits while taxes fund two competing projects | GOV/MIL/ECO/CIV/K-WORK resolve same funds, people and work once. |
| CE-INT-02 | Escaped prisoner becomes enlisted under disputed identity | Physical custody, legal/organizational status and received claims can differ without double person or automatic legal erasure. |
| CE-INT-03 | Veteran acquires craft status and retires from command | LIFE and K-ORG/ECO updates independent; injury, pay, property and continuity maintained. |
| CE-INT-04 | Roman soldier manumitted, promoted and posted to another region | Chronological legal, career, rank and location changes; dated Roman rules only; no global instant recognition or imported campaign lore. |

**Execution status:** These CE-* scenarios are complete integrated-engine acceptance requirements and remain **not fully validated**. R2 separately executed 36 tests against a limited Python reference implementation, with coverage/limitations in `CMRR_Round_2_Executed_Validation.md` (including a national-mobilization scenario). R3 extends this with 39 additional bounded economic/social tests (75 total) and independent scenario comparisons, still using a single implementation. A passed limited implementation test is not adoption, numerical calibration, independent-engine equivalence or live playtesting. Required evidence when an acceptance case is fully executed: pinned initial state, profile/units, authorized inputs, event IDs, event frontier, engine versions, expected/actual owner diffs, paired scale views, rerun idempotence, independent-run comparison, failure diagnosis and follow-up retest.


Acceptance cases specify expected behavior. A clause included in prose is not an executed pass. The package manifest records the fresh checks actually executed; the complete acceptance backlog still needs suitable implementations, live runs and profile calibration. All numerical case inputs are synthetic unless explicitly supported elsewhere.

This edition retains **223 explicit acceptance cases**: 44 receiving-domain cases, 31 Roman cases plus four Roman cross-rule cases, 30 CP-CL cases, 24 XO cases, 20 post-apocalyptic interface gates and 70 combined Core cases. They overlap in useful regression targets; this is not a claim of 223 independent executed implementations.

#### Eleven domain gates

These 44 CE cases are this receiving edition's explicit cases. Companion acceptance ranges do not establish execution of their individual cases. The full domain procedures are in §§113–123.

| ID | Situation | Required result |
|---|---|---|
| CE-GOV-01 | Uncontested valid public decision with known procedure | Record actual authority/result; implementation still uses real staff, funds and delivery. |
| CE-GOV-02 | Favorable persuasion but absent eligible assent or quorum | No invented votes or ratification; participants decide from their own knowledge. |
| CE-GOV-03 | Revocation effective on issue reaches subordinate later | Separate formal validity and known instructions; preserve actual intervening work. |
| CE-GOV-04 | Leader dies with real authorized replacement and records | Office/function continuity follows selection, access, competence and communication; no automatic institution deletion. |
| CE-ECO-01 | Buyer prepays; supplier delivers partly | Payment/fulfillment axes persist independently; no phantom delivered goods. |
| CE-ECO-02 | Funded cash transfer references invalid claim | Reject all participating writes and marker; cash/claim remain unchanged. |
| CE-ECO-03 | Physical loss of five from ten backing obligation eight | Physical five, uniquely backed five, unbacked three, obligation eight under stated sole-order policy. |
| CE-ECO-04 | Paid award later reversed after spending | Preserve actual payment/use; create only supported recovery and funded replacement obligations. |
| CE-INV-01 | Qualified observer can inspect accessible dispatch ledger | Acquire available evidence automatically with actual access/time; no forced clue roll. |
| CE-INV-02 | Successful search of empty place or incomplete room coverage | No manufactured exhibit or universal absence conclusion; record scope/detectability. |
| CE-INV-03 | Several reports repeat one allegation, plus new conflicting evidence | Preserve shared/new assertions and contradictions; allegation is not finding. |
| CE-INV-04 | Case finding requests custody/property remedy | Actual authority/enforcement changes state separately; a report does not move people or property. |
| CE-MAR-01 | Routine voyage with real vessel, watches, provisions and envelope | Advance leg/position/needs once; cargo remains the same identified cargo. |
| CE-MAR-02 | Known breach but no supported flooding/stability threshold | Keep breach/restrictions; no invented precise sinking timer or skill-created buoyancy. |
| CE-MAR-03 | Arrival while unloading power/operator unavailable | Cargo remains aboard until real handling configuration and handover; port entry is not receipt. |
| CE-MAR-04 | Distress signal received by distant rescue vessel | Knowledge changes first; rescue requires real travel, capacity and elapsed time. |
| CE-CIV-01 | Regional program delegates funded repair to real institutions | Child projects progress within means; program owns no second treasury/work total. |
| CE-CIV-02 | Local scene already processed part of a strategic interval | Exclude matching activity/participants/time from abstract updates; preserve unresolved actions/debt. |
| CE-CIV-03 | Incident assessment compares uncertain past baseline and actual present | View retains provenance/unknowns; it cannot refill stock, grant knowledge or assign unsupported blame. |
| CE-CIV-04 | Present service depends on viable import chain | Separate present delivery, local reproduction and horizon support; no mandatory autarky or failure. |
| CE-MED-01 | Known observable care objective and qualified provider/means | Routine supported care modifies named condition with actual supplies/time. |
| CE-MED-02 | Stabilized patient retains structural impairment | Immediate threat can stop without full recovery or duty certification. |
| CE-MED-03 | Empty bed but indispensable utility/staff bundle missing | No treatment slot without supported reduced configuration; prior actual use is not refunded. |
| CE-MED-04 | One named patient transferred between providers | Same person/location/conditions and care history persist; no second wound/healing pool. |
| CE-WILD-01 | Harvest actual finite patch, process and transport output | Source debited, supported yield/waste retained; destination receives only actual delivery. |
| CE-WILD-02 | Revisit source at several display cadences | Only real renewal law and causal boundaries alter source; no loot respawn. |
| CE-WILD-03 | Population estimate differs from hidden truth | Estimate can revise through survey evidence without a birth/removal event or cap on truth. |
| CE-WILD-04 | Large animal named from an existing tracked population | One organism retains anatomy, condition and ecological history across scales. |
| CE-INTEL-01 | Routine reachable source reports observed vehicles | Record method/time/content; cargo/intent remains unresolved absent supporting method. |
| CE-INTEL-02 | Copied rumors plus correlated and novel assertions | Keep derivation and dependence; unique report IDs do not imply independent evidence. |
| CE-INTEL-03 | Report delivered after decision deadline or revocation | Recipients cannot act on it earlier; physical events are not reapplied at receipt. |
| CE-INTEL-04 | One observer doubts a cover identity | Audience-scoped exposure persists; no automatic omniscient cover destruction or legal finding. |
| CE-URBAN-01 | People shelter in existing occupied school | Use can change while same building/people/property persist; no spawned water or residents. |
| CE-URBAN-02 | Service supports fewer people than actually present | Actual headcount remains; allocate/record deficit, including district-specific access. |
| CE-URBAN-03 | Construction complete but test/commissioning fails | Work stays complete; actual blocker prevents required function/service without total reset. |
| CE-URBAN-04 | Temporary bypass replaced by viable redesigned durable topology | Declared acceptance can succeed without recreating former topology; support is separately assessed. |
| CE-LIFE-01 | Employer supplies meal while household panel also reviews need | One provision/use portion; no duplicate food or carried ration. |
| CE-LIFE-02 | Mixed social offer needs new PC payment or commitment | Present feasible terms and return control; no silently accepted concession. |
| CE-LIFE-03 | Unqualified TU amount or language label hides required function | Unknown hours remain unknown; speech does not imply reading/writing; assess only relevant gap. |
| CE-LIFE-04 | Retirement/death opens estate and successor control | Preserve injuries, tool wear, claims and time; actual transfers do not copy skill/private knowledge. |
| CE-COMP-01 | Judged craft contest with complete pinned scoring and real outputs | Score actual finished work once; prize becomes claim before funded settlement. |
| CE-COMP-02 | Equal interchangeable competitors swap labels | Outcome mapping is symmetric for that purpose; asymmetric action bands cannot be assumed fair. |
| CE-COMP-03 | Same competitor/official scheduled in incompatible fixtures | Resolve real schedule/capacity; no duplicate person, stamina reset or automatic assent. |
| CE-COMP-04 | Final award reversed after payment and use | Correct standings/claims by authority; do not replay exertion or erase past funded payment. |

#### Roman cases retained from CP-RR

The 31 AC cases and four X-RR cross-rule cases retain their original identifiers and expected meanings. Roman-specific numerical/effect adapters remain outside Core.

| ID | Setup / attempted failure | Required result |
|---|---|---|
| AC-01 | The selected adapter explicitly ends a primary damage channel at protection. A downstream placement bonus would otherwise make its arithmetic positive. | No injury through the ended channel. The modifier cannot revive it. |
| AC-02 | A supported secondary impact transfers through protection that stops the primary channel. | Resolve the actual secondary mechanism once with its own applicable protection; no automatic immunity and no duplicate primary effect. |
| AC-03 | An adapter uses native rating 0 for a supported control/contact method, or rounds a small transmitted quantity to 0 for display. | Interpret the adapter's semantics. Do not infer universal termination merely from the numeral. |
| AC-04 | A later strike affects an already compromised structure/component. The displayed functional penalty is already the worst available. | Assess supported worsening and restrictions; the unchanged modifier is not physical immunity. |
| AC-05 | Several distinct small injuries contribute to a supported common ongoing burden. Another collection of superficial marks has no such mechanism. | Aggregate the supported burden once; do not infer severe damage solely from wound count. |
| AC-06 | The same damage event is reported, reloaded, and shown again at strategic scale. | Condition changes once; reports/scale changes create no extra damage or healing. |
| AC-07 | Shop stock is unresolved. Authorized bounded generation establishes none of the requested item. The player repeats the same search without a world change. | Retain the absence result; no fresh stock-generation chance. A later actual delivery can change it. |
| AC-08 | Hidden authoritative stock already exists, but the player does not know it. | Search uses that stock and reachable evidence; do not regenerate the shop because the player's knowledge is blank. |
| AC-09 | One instructor exists in an eligible pool and is occupied. The player requests another; an incidental member is also given a name. | No duplicate instructor or extra population. Naming conserves the pool; a real arrival/recruitment can add capacity. |
| AC-10 | A binding scenario/generation constraint establishes a pool of 3–5 eligible workers. A consequential allocation now needs exact membership/count. | Refine consistently within the binding bound, record the detail once, and conserve it through later disaggregation. Do not sample beyond 5 or add another independent pool. |
| AC-11 | An established healthy person walks across suitable ground with no numeric agility or walking-capacity field. | Ordinary movement proceeds with actual time and any supported restrictions; no invented statistic or mandatory roll. |
| AC-12 | The same person attempts an unusually heavy load, or a machine without its required input is asked to operate. | Resolve the actual material uncertainty/dependency. Unmeasured capacity grants neither exceptional lifting nor input-free operation. |
| AC-13 | An intermediary successfully agrees to seek an appointment from an official. | Record and schedule the undertaking. The official's decision and actual meeting remain unresolved until their causes occur. |
| AC-14 | A willing owner agrees to hand over an accessible item immediately and does so within the authorized scene. | Apply the actual transfer once. Do not require an artificial fulfillment roll or defer a completed concession. |
| AC-15 | A Mixed negotiation offers a narrower service requiring an additional voluntary payment. | Present the new terms for acceptance; do not deduct money or invent the player's agreement. |
| AC-16 | A reliable guard and an established negligent guard face different incentives to keep their posts. | Their supported choices may differ. An unattended post has a real gap; autonomy does not preserve fictitious staffing. |
| AC-17 | A subordinate has not received an order's revocation. The rule says revocation is institutionally effective on issue. | Preserve actual knowledge and possible continuation; assess formal validity separately. No instant notification or erasure of completed work. |
| AC-18 | An NPC delegates work to an actor already committed to another exclusive task in the same interval. | Resolve acceptance, conflict, and feasible capacity. Do not record both jobs as completed from the same unavailable labor. |
| AC-19 | An actor owns a tool but cannot access it; another holds it without valid title; a distant institution still records an earlier custodian. | Preserve distinct ownership, custody, access, and knowledge/recognition facts. No field silently synchronizes the others. |
| AC-20 | An actor receives a title with a narrow mandate. | Record its actual scope and explanation. Do not add staff, wealth, expertise, or universal recognition without their own mechanisms. |
| AC-21 | A person speaks a language fluently but cannot read its script; another can copy familiar text without understanding it. | Resolve the particular required functions. Speech grants no literacy; copying grants no comprehension by itself. |
| AC-22 | One missing technical function is described by several labels during the same task. | Represent its practical restriction once. No duplicate penalties, invented average, or redundant checks. |
| AC-23 | A compact interval records 5 units earned/transferred and fractional unfinished work; a checkpoint is reloaded and the entry replayed unchanged. | Preserve the 5-unit transfer and fractions once. No extra payment, work, fatigue, or training credit. |
| AC-24 | The same scoped event ID is submitted with a changed transfer amount. A new transfer also attempts an invalid partial multi-owner update. | Reject the collision and the invalid transaction without partial writes or a new applied marker. |
| AC-25 | A routine interval encounters an earlier interruption or meaningful player decision than its requested end. | Stop/split at the event frontier, preserve earned fractions, and return new voluntary choices. Display frequency does not add process updates. |
| AC-26 | A summary and an alleged private save omit the hidden state they claim can be recovered. | Report the actual persistence/privacy limitation. Do not reconstruct secrets from a hash or treat unrecorded reasoning as stored state. |
| AC-27 | A harmful source or transmission ends after an existing condition or accumulated burden has been established. | Stop further contribution under the channel's mechanism. Preserve the existing condition/burden and its actual recovery or downstream process; no automatic healing or reset. |
| AC-28 | Local world generation is needed, but the player's motives, chosen history, or next voluntary action are unspecified. | Establish only authorized world detail. Leave player-controlled choices to the player or their explicit delegation; do not manufacture past voluntary acts or revise resolved history. |
| AC-29 | An observer estimates 3–5 workers; authoritative hidden state establishes 8, or later evidence supports a different count. | Keep actual state and the actor's estimate distinct. The estimate does not cap truth; update knowledge through actual evidence rather than regenerating the workers. |
| AC-30 | An NPC makes a successful persuasive appeal to the player character. Separately, another NPC gives an assurance that may be deceptive. | Leave the player's voluntary response to the player. Preserve assurance, genuine undertaking, and institutional validity separately; do not reinterpret a resolved genuine undertaking as deception to cancel success. |
| AC-31 | A detained person moves to another custodian while the claimed legal basis is disputed and a distant actor has not learned of the move. | Keep the same actor identity; update actual custody/location once. Retain the dispute and each audience's knowledge separately. No stock lot, duplicated person, or automatic legal recognition is created. |

- **X-RR-01 — Simultaneous last item:** Two accepted requests depend on one available item at the same causal time. Establish the stock once; apply the existing allocation/decision procedure; complete at most one transfer unless a supported shared-use arrangement exists. Two successful social concessions cannot create a second item. Preserve the unfulfilled obligation and any supported remedy.
- **X-RR-02 — Successful procurement, delayed delivery:** A supplier accepts an order for real stock. Reservation, dispatch, transit, receipt, acceptance, and payment occur under their terms. A successful negotiation does not teleport the goods; a transit loss does not leave both intact delivered stock and a lost copy. Existing claim/reservation shortfall rules handle the consequences.
- **X-RR-03 — Later institutional reversal:** An award was validly paid and spent; a later ruling changes the recipient's entitlement. Preserve the actual transfer, use, and elapsed time. Record any supported recovery claim or compensating transfer under its actual authority. Do not erase history or create an automatic refund. A payment falsely recorded but never made is a different record-correction case.
- **X-RR-04 — Delegated life off-screen:** An NPC agrees to arrange care while the protagonist travels. Schedule real people, communication, supplies, and work. Advance the same commitments and conditions once. Return only new player decisions; ordinary authorized NPC work can complete without the protagonist's attendance.

#### CP-CL library/engine cases

| Case | Clause | Fixture/trigger | Required result |
|---|---|---|---|
| CL-AC-01 | 01 | Two libraries use the same bare entry ID | Source namespace/version disambiguates them |
| CL-AC-02 | 01/12 | Source row says Core; its parent is Fantasy | Parent provenance is retained; no universal adoption inferred |
| CL-AC-03 | 02 | Cut/thrust aliases share one sword family | Both selectors persist; one instance does not become two swords |
| CL-AC-04 | 02 | Variant explicitly replaces inherited capacity with unknown | No fallback to the convenient inherited number |
| CL-AC-05 | 02/03 | Editor combines construction, coverage and material | A configuration definition results; inventory is unchanged |
| CL-AC-06 | 03 | Existing starting armor predates campaign time | Initialization does not debit today's materials or rerun fabrication |
| CL-AC-07 | 03/08 | One component is cannibalized from a donor | Actual donor function/part custody changes once; recipient function awaits necessary work |
| CL-AC-08 | 04 | Tank has capacity 100 units, contents 20 | Stock remains 20; capacity is not reserve |
| CL-AC-09 | 04 | Fuel/part exists but is incompatible | Dependent operation/repair remains unavailable unless a supported conversion is performed |
| CL-AC-10 | 04 | Reserved backing is physically lost | Loss commits; obligation survives with its backing state reconciled |
| CL-AC-11 | 05 | One five-unit portion appears in tank and service-delivery views | Selected provision basis counts five, not ten |
| CL-AC-12 | 05 | Reserve 120; demand 50/day; replenishment 30/day | Forecast six days under unchanged assumptions; forecast performs no debit |
| CL-AC-13 | 06 | Two parallel routes each nominally handle 8 units/hour but share a 10-unit/hour loader | Combined throughput cannot exceed the shared 10-unit/hour constraint |
| CL-AC-14 | 06 | A required pump/fuel/startup dependency cycle has no independent start path | Mere asset possession does not start the cycle |
| CL-AC-15 | 06 | Demand exceeds rated output without a profiled damage mechanism | Shortfall/curtailment follows; arbitrary damage does not |
| CL-AC-16 | 07 | Watch 08:00–12:00 overlaps training 10:00–14:00 | Two-hour conflict remains; relief/rescheduling or reduced actual credit required |
| CL-AC-17 | 07/08 | Four technicians offered to a two-station repair | Substitute coverage can improve; concurrent cap remains two |
| CL-AC-18 | 08 | Installation finishes; commissioning has not occurred | Mechanical completion does not create delivered service |
| CL-AC-19 | 08/10 | Program summary repeats child-project completion | No additional work or consumption is applied |
| CL-AC-20 | 09 | Manual or revised doctrine reaches an institution | Information access changes; unearned competence or universal fielding does not |
| CL-AC-21 | 09 | A leader dies but valid substitutes/records/support exist | Continuity follows actual succession; institution is not erased by default |
| CL-AC-22 | 10 | Radio link works while freight route is blocked | Information and material connectivity remain different |
| CL-AC-23 | 11 | Robot actor and asset reference one sensor fault | One physical fault controls affected sensing; no duplicate wound ledger |
| CL-AC-24 | 11/12 | One blocked attack has no supported secondary transmission | The selected model's termination guard survives the integration |
| CL-AC-25 | 12 | Old progress says 8 TU without known schedule | Hours and advancement remain unresolved; no assumed conversion |
| CL-AC-26 | 12 | Incomplete candidate is referenced from a slim genre library | Complete source definition remains on hold; candidate pointer does not activate a replacement |
| CL-AC-27 | 12 | Referenced model version changes or a selector is missing | Dependent resolution is unresolved; no silent latest/favorable substitute |
| CL-AC-28 | 03/10/12 | Same initialized asset is referenced by site, service and program | One instance and one underlying state persist |
| CL-AC-29 | 11/12 | Biological care and machine repair share work infrastructure | Condition owners remain distinct; rates/effects are not copied across |
| CL-AC-30 | All | All extraordinary/theme mechanisms are disabled | Ordinary content, service, institutions and life remain usable |

#### XO cross-engine cases

| ID | Test | Required result |
|---|---|---|
| XO-T01 | A medieval sword is listed in two compatible catalogues | One actual item, multiple source references |
| XO-T02 | Sword cut and thrust modes are grouped by an alias | Both modes and their distinct profiles preserved |
| XO-T03 | Armor material changes without changing coverage | Only supported properties change |
| XO-T04 | A machine's one component fails | Only supported dependent functions fail; no duplicate fault |
| XO-T05 | A robot has an asset fault and an actor profile | One physical damage state, consistent capability loss |
| XO-T06 | Two workers compete for one required workstation | Output constrained by workstation capacity |
| XO-T07 | Repair finishes but required inspection fails | Repair work remains recorded; acceptance/service not granted |
| XO-T08 | Ruin searched repeatedly without changed evidence | No generated extra loot or independent reroll |
| XO-T09 | Resource extracted but not processed or transported | Source reduced, recovered material exists, destination stock unchanged |
| XO-T10 | Mine exhausted; no renewal process exists | Further extraction yields no new stock |
| XO-T11 | Hospital and workshop share insufficient power | Supported service allocation; no double use of energy or power capacity |
| XO-T12 | Pump repaired, but supply or distribution absent | Asset operability may improve; delivered water still constrained |
| XO-T13 | Officer qualified in a specialty but lacks appointment | Competence exists; missing office authority remains missing |
| XO-T14 | Ancient machine recovered and studied | Possession/knowledge do not imply manufacture capability |
| XO-T15 | One person extracted from a population cohort | Total population conserved |
| XO-T16 | Ten residents, three qualified workers, one unavailable | Work capacity based on actually eligible available workers |
| XO-T17 | Venomous bite inflicts injury and toxic exposure | Separate mechanisms, no duplicate contact or damage |
| XO-T18 | Protective equipment blocks exposure channel | No effect through blocked channel unless separate supported mechanism exists |
| XO-T19 | Campaign changes from personal scene to regional review | No repeated losses, gains, progress or population |
| XO-T20 | One event replayed after save/load | No additional stock transfer, damage, labor, or service |
| XO-T21 | Simultaneous actors claim the last resource | Allocation/contest resolves scarcity before atomic transfer |
| XO-T22 | A system has an unknown required parameter | Dependent calculation unresolved; independent work continues |
| XO-T23 | An NPC institution handles authorized routine repair | Work progresses within actual resources without PC micromanagement |
| XO-T24 | A setting has no magic, advanced technology or apocalypse | All applicable mundane Shared Core systems remain usable |

#### Post-apocalyptic interface gates

| Gate | Situation | Required Core observation |
|---|---|---|
| CW-PA-01 | Failure of supply input while a user-facing buffer remains available | Input failure applies once; real buffer can delay downstream service loss without fake asset damage |
| CW-PA-02 | Delayed report of an already applied outage | Recipient knowledge changes at receipt; physical service is not interrupted again |
| CW-PA-03 | Two simultaneous causes depend on one shared facility | Distinct causes retain provenance; the same physical loss/resource charge applies only once |
| CW-PA-04 | Survey one room of a warehouse; another room unassessed | Depletion knowledge is scoped by place and material class; unknown ≠ empty |
| CW-PA-05 | Retrieve components from an installed machine | Physical recovery adds real components; donor asset loses its affected capability; no free fabrication |
| CW-PA-06 | Discover a generator without means to move/install it | Discovery changes knowledge; custody, transport and delivered service remain constrained |
| CW-PA-07 | Shelter opens in an occupied school | Use classification changes without creating people, water, guards or another building |
| CW-PA-08 | A child, injured specialist and caregiver arrive in the same group | One movement/population total; immediate actual demand; workforce assessed person-by-person or grounded cohort |
| CW-PA-09 | Official dies, records remain, divided successor branches assert power | Functions, claims, authority, recognition, actual control, documents and expertise stay distinct |
| CW-PA-10 | Working production equipment lacks future replaceable electronics | It keeps current supported service; horizon vulnerability is a forecast, not immediate failure |
| CW-PA-11 | Grain abundance beyond an impassable freight link with radio intact | Material delivery and information connectivity differ; no instantaneous destination stock |
| CW-PA-12 | Facility construction done, commissioning unsuccessful | Work remains complete; failed functional/service acceptance records actual blocker rather than undoing built work |
| CW-PA-13 | Emergency bypass later replaced by viable redesigned permanent system | Different accepted topology can meet service objective; old topology need not be rebuilt |
| CW-PA-14 | Same project viewed locally and at civilization scale | Existing work, labor, stock, casualties and events are not counted twice |
| CW-PA-15 | Three organizations compete for one usable stock while stock is involuntarily lost | Commit actual loss; reconcile backed/unbacked allocations and obligations without overdraw or retroactive prevention of loss |
| CW-PA-16 | Historical state is disputed and a recent report is incorrect | Baseline/confidence, physical reality and recipients' beliefs remain separate; impact view grants no omniscience |
| CW-PA-17 | Normal supply and stable institutions operate through a long uneventful interval | Continued stable function is valid; no mandatory decline, threat, new meter or apocalypse stage |
| CW-PA-18 | Selected Core lacks startup, operating-bundle or commissioning procedure | Reject incomplete migration, or explicitly select the old bounded compatibility bridge; never silently omit function |
| CW-PA-19 | Two campaigns use the same template and reuse an event ID | IDs are campaign-scoped; content selection creates no instances; replay remains idempotent within scope |
| CW-PA-20 | A solution requires a new PC purchase, evacuation or political concession | Preserve already authorized work; return voluntary decision to player, no silent commitment |

#### Combined Core cases

Case labels identify stable requirements, not executed passes. CORE-69 follows §99: a previously false record differs from an actual transfer later judged mistaken. No blanket rollback is authorized.

| ID | Inputs/action | Required state/result | Prior evidence or specified status |
|---|---|---|---|
| CORE-01 | Enumerate d100 values at seven inherited modifier totals | Original Failure/Mixed/Success percentages retained | Verified arithmetic |
| CORE-02 | Equal binary ordering inputs | 50 A priorities, 50 B priorities | Verified arithmetic |
| CORE-03 | Reverse sides, modifier sign and paired raw r → 101−r | Priority reverses for every paired result | Verified arithmetic |
| CORE-04 | A has 80 units; dispatch 30; transit loses 2; B receives 28 | A 50, transit 0, B 28; total 78 | Verified transactions |
| CORE-05 | Replay a previously applied dispatch/report interval | No second change | Verified transactions/interval cursor |
| CORE-06 | Two simultaneous claims of 6 each on shared capacity 8 | Cannot both be accepted; authorized 5+3 allocation feasible | Verified capacity constraints |
| CORE-07 | Two distinct usable parallel paths with separate budgets | Can add their capacity within actual source constraints | Verified capacity constraints |
| CORE-08 | Full 100-unit tank becomes incompatible with potable use | Physical 100, usable potable 0 | Verified stock usability |
| CORE-09 | Four-shot magazine, request 6 without bounded-best-effort authorization | Full request rejected; no negative stock or silent new choice | Verified validation |
| CORE-10 | Reserve 30 of 80, consume that reserved 30 | Physical/free 50; consumed reservation cleared | Verified reservations |
| CORE-11 | Conflicting reserve exceeds free stock | Rejected atomically; stock/reservations unchanged | Verified reservations |
| CORE-12 | A transfer would make source negative | No source/destination change or applied ID; corrected valid retry possible | Verified atomicity |
| CORE-13 | Twelve technician-hours, two-worker cap, part at hour 2 | Work complete at hour 8; one-hour acceptance ends hour 9 | Verified work arithmetic |
| CORE-14 | Four technicians offered to CORE-13 | Same earliest finish; excess workers add no rate | Verified cap |
| CORE-15 | Two-person work usable only hours 2–4, then power loss | Four technician-hours credited; eight remain | Verified interruption |
| CORE-16 | Reprocess an already processed work interval | No additional progress | Verified interval cursor |
| CORE-17 | Watch 08:00–12:00 and training 10:00–14:00 for one person | Two-hour conflict; only 12:00–14:00 unconflicted before travel/terms | Verified overlap |
| CORE-18 | Two people perform independent parallel two-hour tasks | Two clock-hours, four person-hours | Verified concurrency arithmetic |
| CORE-19 | Reserve 120, demand 50/day, actual replenishment 30/day | Six-day exhaustion forecast; day one reserve 100 | Verified rates |
| CORE-20 | Then demand rises to 55/day, replenishment stays 30 | Four days remain at changed rate; forecast no debit | Verified changed rates |
| CORE-21 | Continuous use would exhaust reserve halfway through authorized interval | Stop at exhaustion; no negative extrapolation | Verified threshold |
| CORE-22 | Delivery arrives at hour 2 after reserve exhaustion at hour 1 | One-hour gap; no retroactive supply | Verified segmented rate processing |
| CORE-23 | Five qualifying wage days at 2/day, 6 paid | Accrued 10, cash 6, outstanding 4; repeat review adds zero | Verified accrual cursor |
| CORE-24 | Three living individuals plus residual cohort 7; expand one cohort member | Four individuals plus cohort 6; total stays 10 | Verified population |
| CORE-25 | Person departs origin, travels, then arrives destination | Present at one location; transit not omitted | Verified movement |
| CORE-26 | One missing of 10 reclassified captured | Still 10 total; no extra unavailable member | Verified classification |
| CORE-27 | Bridge fails 14:00; report arrives 14:20 | Physical link false at 14:00, remote knowledge unchanged until 14:20 | Verified event ordering |
| CORE-28 | Two independent simultaneous disabling hits | Both evaluate from pre-impact capability; neither narration erases the other | Verified simultaneous commit fixture |
| CORE-29 | Output 10; essential 2 + move 4 + fire 6; no buffer | Full combination 12 infeasible | Verified output arithmetic |
| CORE-30 | Ammo 4, heat 3, shot +4, cooling 1/minute, peak limit 10 | First shot ammo 3, peak 7, after minute 6 | Verified peak ordering |
| CORE-31 | Next shot, minute cooling, immediate further shot | Second peak 10; ammo 2, heat 9; third blocked at prospective 13, no ammo debit | Verified interlock |
| CORE-32 | Wait three minutes, then shot | Heat 6 then peak 10, ammo 1 | Verified recovery/activation |
| CORE-33 | Generator/pump require each other's startup output | Neither starts without independent input; real startup input enables chain | Verified bounded dependency reachability |
| CORE-34 | Ten-kilo empty parent, two-kilo child, three-kilo contents | Loaded mass 15, not 18; containment cycle rejected | Verified containment |
| CORE-35 | Forty qualifying hours displayed under reported 4-hour or 20-hour TU | Ten or two TU; no automatic advancement assertion | Verified conversion arithmetic only |
| CORE-36 | Routine: qualified familiar maintenance | Automatic progress, actual time/parts only | Specified |
| CORE-37 | Agency/Mixed: further repair needs another day and a new part | Offer choice; do not silently extend/spend | Specified |
| CORE-38 | Failure: failed search of established concealed cache | Cache persists; no unrelated explosion | Specified |
| CORE-39 | Extreme: perfect execution against an unaffected channel | No impossible penetration or purification | Specified |
| CORE-40 | Effect: primary channel stopped, vital-location bonus present | Primary injury remains stopped; secondary mechanism only if defined | Specified |
| CORE-41 | Repeated use: search emptied site again | No fresh generic loot; new access/evidence can matter | Specified |
| CORE-42 | Reactions: repeatedly borrow next commitment | One debt; reserved defense paid only once | Specified |
| CORE-43 | Crew: qualified operator unavailable, passenger present | No spontaneous qualification/controls | Specified |
| CORE-44 | Commissioning: repair complete, test fails | Specific rework, no declared service restoration/reset of all work | Specified |
| CORE-45 | Quality: pump runs, required contaminant not removed | Output is not potable service | Specified |
| CORE-46 | Cascades: one outage affects three services | One initiating fault, distinct buffers and downstream times | Specified |
| CORE-47 | Physiology: moving to shelter ends exposure | Retained contamination/illness/injury not instantly erased | Specified |
| CORE-48 | Scale: detailed casualties/ammunition inside aggregate interval | Detailed events replace matching estimates; no reset or double charge | Specified |
| CORE-49 | Economy: buyer prepays, seller later delivers partly | Separate payment and fulfilment; no phantom goods | Specified |
| CORE-50 | Property: arrivals bring private food | Arrival changes demand; communal stock unchanged until transfer | Specified |
| CORE-51 | Population: 800 present, essential service supports 600 | Population remains 800; allocate/resolve deficit | Specified |
| CORE-52 | Staffing: surgeon arrives injured/exhausted with dependants | Expertise present, task capacity/care obligations assessed separately | Specified |
| CORE-53 | Institutions: mayor/commander dies with competent authorized successor | Actual function can continue; no automatic deletion | Specified |
| CORE-54 | Knowledge: manual survives, only competent technician lost | Information remains, practical capability can fall | Specified |
| CORE-55 | Learning: doctrine adopted but not sent/trained | Local capability remains unchanged until fielded | Specified |
| CORE-56 | Production: prototype works once | No instant industrial line, spare chain or deployment | Specified |
| CORE-57 | Seasons: summer surplus, winter gap | Forecast both periods; no universal sustainability label | Specified |
| CORE-58 | Exploit: healed tissue after a profiled sacrificial cost | No automatic refund of unrelated expended value | Specified; extraordinary module required |
| CORE-59 | Autonomy: water service delegated repair with means | NPC team can actually solve it off-screen within authority | Specified |
| CORE-60 | Success: deficit solved durably | Pressure removed; no compensating crisis from design fiat | Specified |
| CORE-61 | Zero theme: no magic, anomalies or Mechs enabled | Ordinary core services remain complete | Specified |
| CORE-62 | Migration: training amount survives only as 8 TU with unknown origin | Conversion unresolved; no favorable invented hours | Specified |
| CORE-63 | Hidden state: reports and public panels | No revealing secret arithmetic or unsupported private persistence | Specified |
| CORE-64 | Bookkeeping: one tank referenced by inventory, site, service and program | One quantity; views create no updates | Specified |
| CORE-65 | Scale/geometry: huge creature, small real local injury | Actual affected function, no arbitrary boss immunity or double normal-size force | Specified |
| CORE-66 | Authority: senior officer with no technical skill | Can direct within rights; cannot personally supply missing expertise | Specified |
| CORE-67 | Simultaneous contention: two new stock claims with no prior allocation | Resolve real authority/ordering; no both-spend-last-resource outcome | Specified beyond tested validation |
| CORE-68 | Cyclic physics: feedback process claimed from graph alone | Require scoped dynamic mechanism; no free energy from connectivity | Specified |
| CORE-69 | A delivery record is erroneous, or an actual delivered award is later reversed | Classify under §99: repair representation or create supported compensating causes; preserve actual physical history and unrelated events | Revised specified regression; no fresh full-domain run |
| CORE-70 | Bookkeeping: ordinary monitoring during travel | Compatible activity accounted once; demanding incompatible work constrained | Specified |

#### Runtime and combined-case acceptance

Test routine, edge, extreme, scarcity, failure, Mixed, repeated use, simultaneity, scale transition, accounting, module interaction, agency, exploit and bookkeeping behavior. Include stable solved problems and autonomous routine institutions; do not design every fixture to force collapse.

For a run retain initial state; scoped source/profile versions; declaration/authority; feasible method/outcomes; actual costs; causal queue; retained uncertainty; observed result; resulting/remaining state; detected defect; revision and recheck. A synthetic reference fixture can establish a bounded invariant, not full domain realism or table usability. R2 narrow-scope result: 36 reference-harness unit tests currently pass and one national fixture replays exactly under the same implementation; this is *bounded executable evidence*, not completion of the 24 CE-MIL/LIFE/INT acceptance specifications.

An independent runner must reconstruct the next feasible/authorized action from checkpoint, journal, known information, pending queue and unresolved decisions. A public panel is neither private state nor proof of recoverability. Measure bookkeeping burden and identify any information omitted by compression.


#### Provider-binding acceptance requirements

| ID | Required result |
|---|---|
| BIND31-01 | Every manifest pins Core 3.2 and resolves every required shared provider to an existing section |
| BIND31-02 | Native effect/needs/load/learning/recovery profiles remain selected; no mixed numerical chain |
| BIND31-03 | All 286 SCL rows resolve to the correct source family/type/mode; 304 source references are accounted for |
| BIND31-04 | All 61 Fantasy adapters and 420 source payload blocks retain exact source semantics and values |
| BIND31-05 | A held candidate can use exact preserved source-backed content but cannot activate a completed replacement |
| BIND31-06 | Alias lookup, repeated lookup and manifest compilation change no actual actor/asset/stock state |
| BIND31-07 | Sword cut/thrust share one physical family and retain distinct native mode profiles |
| BIND31-08 | Unarmed and coverage remain non-inventory reference kinds |
| BIND31-09 | Invalid model envelope, unit or state basis cannot produce a physical event |
| BIND31-10 | Derived range/endurance/delta-v is not consumed alongside its actual input stock |
| BIND31-11 | Issue, receipt, completion and acknowledgment remain causally ordered and replay-safe |
| BIND31-12 | Overlapping measurement intervals follow actual tie/decision rules, without invented precision |
| BIND31-13 | An appeal changes recognized results/claims without replaying exertion or duplicating money |
| BIND31-14 | ROM-INIT-01 and H/F learning units keep their complete scoped meanings |
| BIND31-15 | Eight Space templates and four Sports entries remain specialized; SSN has no implicit adapter |
| BIND31-16 | Every original Core topic and unaffected procedure remains preserved; source files retain their hashes |

These requirements are not all full implementations. Fresh executable checks identify their actual bounded scope. Domain performance, biology, finance, history, flight and sports parameter calibration remain explicit local work.

#### R3 cross-domain requirements — proposed, not fully executed

| ID | Required integrated acceptance scenario | Required result |
|---|---|---|
| CE-ECO-R3-01 | Farmer mobilized out of scheduled planting shift | No automatic cancellation; authorized future reassignment changes only real remaining work and its inputs |
| CE-ECO-R3-02 | Caregiver mobilized; cook reassigned into care | Care delivered by the replacement only if qualified/present; cooking output and meal provision adjust from actual work |
| CE-ECO-R3-03 | Caregiver absent without substitute | A measured unmet care service appears, not an invented casualty or compulsory PC response |
| CE-ECO-R3-04 | Workshop receives missing inputs after shift began | No retroactive production; shipment remains in transit until actual receipt |
| CE-ECO-R3-05 | Multiple farms, civilian projects and garrison compete for labor and facilities | Overlap checked across **all** claimants and time spans; no id-order arbitration |
| CE-ECO-R3-06 | Taxes assessed and wages owed at the same treasury | No actual revenue from assessment; no actual wages from accrual; physical payments conserve currency |
| CE-ECO-R3-07 | Long-duration production scales to individual workshop scene and back | No duplicate production, work hours, consumption, wage claims or welfare provision across covered intervals |
| CE-ECO-R3-08 | A household receives goods but lacks cooking labor and care | Stocks, usable output, actual care, receipt and unmet need remain distinguishable |
| CE-ECO-R3-09 | Two linked operations on one event frontier | Explicit causal dependency/transaction staging rather than event-ID order creating same-time authority or output |
| CE-ECO-R3-10 | Eligible civilian and military workers have incompatible roles | Actual availability, authority, duty notice and effective time determine feasible work and exposure |
| CE-ECO-R3-11 | Scarcity forces a partial production interruption | Actual elapsed work settles once under the selected continuous/batch process, residual input stock remains conserved |
| CE-ECO-R3-12 | Decade-long stable nation with variable recruitment, crop failures and births | Selected demographic/production models evolve autonomous world state without fabricated free growth or global freezes |

The limited R3 fixture executes **75 code-level unit tests** (36 retained + 39 new), not twelve complete CE-ECO-R3 acceptance cases. Real cross-engine model validity, labor substitution, production calibration, independent implementation agreement, aggregate-to-local exclusion and long-horizon autonomy remain unproven. See `CMRR_Round_3_Executed_Validation.md` and executable inputs.

#### R4 qualified partial-commit and cross-scale cases — PROPOSED, partially bounded-tested

| ID | Stimulus | Mandatory result | Bounded R4 evidence / gap |
|---|---|---|---|
| CE-EVT-R4-01 | Two same-time insufficient treasury claims while an unrelated farm begins | Farm can execute; both grants remain unexecuted awaiting competent decision | Synthetic fixture + tests 76–79; legal authority not verified |
| CE-EVT-R4-02 | Three claimants exceed a shared capacity or stock | Entire contested component is identified; no ID-order winner or pairwise-only acceptance | Tests 82/104 and carried R3 tests; no optimized allocator |
| CE-EVT-R4-03 | Unknown extension emits an event without declared owner set | Conservative barrier, not assumed independent physical side effect | Tests 91/102; external module contracts not validated |
| CE-EVT-R4-04 | Past proposed grant gets a later competent allocation | New prospective actual transaction, current capacity rechecked, denied requests retained | Tests 78/87–90/105; authority is fixture reference only |
| CE-EVT-R4-05 | Unresolved funding survives next day's farm work | No world freeze and no retrospective products | Tests 77/80; not a full autonomous scheduler |
| CE-EVT-R4-06 | Same-time dependent tax, job, order and command stages | Dependent effect requires pre-frontier evidence or explicit selected substage | Tests 83–84 and earlier R3 tests; no arbitrary microstep ordering |
| CE-EVT-R4-07 | Tactical work later summarized by day and month | View does not increment output again; original event is sole source | Tests 92/96/107 and mixed R4 fixture; no second runtime |
| CE-EVT-R4-08 | Local worker already covered by a strategic cohort | Overlap rejected unless residual contributor/interval proven distinct | Tests 94–95; K-POP partition not independently authenticated |
| CE-EVT-R4-09 | Source interval crosses a reporting boundary | No unlicensed prorated quantity | Test 97; selected partial-interval process pending |
| CE-EVT-R4-10 | Save/replay, reordered independent requests and double-submit | Same-implementation canonical state, committed inputs stable, unexecuted IDs retained | Tests 88/92–93/100–103; independent solver absent |
| CE-EVT-R4-11 | Physical hazard depletes a reserved pool at same frontier | Hazard commits once; new shortfall backing assessed, unrelated work continues | NOT EXECUTED in R4; requires hazard/loss adapter |
| CE-EVT-R4-12 | Long-duration multi-region autonomous society with operational combat | Exact residual populations, costs, injuries and event backlog across every scale | NOT EXECUTED; requires demographic, combat and economic profiles |

**Execution status:** The R4 code suite passes 108 Python unit tests (75 inherited unchanged + 33 new); test counts are not twelve full CE-EVT-R4 scenario passes. `run_round4_fixture.py` executes one synthetic mixed-frontier case and one read-only cross-scale output projection. The submitted Python modules are a bounded first implementation with hand-written footprint declarations, not an independently qualified producer/consumer graph. A complete implementation requires proven owner sets, pre-state model validity, causal-stage semantics, interval partition and independent replay comparators. See `CMRR_Round_4_Executed_Validation.md`.

#### R5 physical-loss and cross-scale acceptance cases — PROPOSED; bounded fixture evidence only

| ID | Trigger | Required outcome | Executed R5 evidence and outstanding condition |
|---|---|---|---|
| CE-HZD-R5-01 | Measured warehouse fire destroys previously reserved input stock | Hazard occurs once regardless of reservation; loss counted separately from consumption | Test 109; real physical cause/quantity not simulated |
| CE-HZD-R5-02 | Loss leaves several equally eligible jobs underbacked | No ID-order winner; all contested claims explicitly retained | Tests 110, 124; no authenticated allocation rule |
| CE-HZD-R5-03 | Unbacked farm job reaches planned completion time | No invented output or consumed stock | Test 111; partial work laws missing |
| CE-HZD-R5-04 | Independent tax, kitchen and cash operations at hazard frontier | Qualified independent activity proceeds | Tests 112, 113, 117 and combined fixture; footprints not independently qualified |
| CE-HZD-R5-05 | Stock departure and physical loss share unresolved same-instant source pool | Loss retained; unsupported physical ordering of loading not invented | Test 116; requires verified chronology for later decision |
| CE-HZD-R5-06 | Several loss assertions exceed actual source physical stock | No guessed negative inventory or ID-order winner; evidence problem exposed | Tests 118–120; observation disputes not resolved |
| CE-HZD-R5-07 | Goods lost in transit | Surviving shipment, reservations and transit quantity reconcile | Test 121 confirms safe refusal; full scenario NOT EXECUTED |
| CE-HZD-R5-08 | Restock and suspended production restart | New backing and actual work/time qualify any further output, retain existing claim | NOT EXECUTED; restoration/partial-progress model required |
| CE-MIL-R5-09 | Tactical engagement causes confirmed incapacitation and ammunition expenditure | Strategic view reads same source effects, no additional casualty or ammunition write | Tests 127–128, 133; fixed outcome fixture only |
| CE-MIL-R5-10 | Multiple reports/engagement summaries describe same exchange | Reports represent information events, not extra physical effects | Tests 129, 134; real observation/transmission/receipt model missing |
| CE-MIL-R5-11 | Detailed person included in a residual strategic population | No overlap or inferred residual casualty | Test 130 checks identifier exclusion; residual effects not executed |
| CE-MIL-R5-12 | Query past scale state after current world changed | No present-state leakage into unarchived historical as-of snapshot | Test 132 rejects unsupported historical view; checkpoint replay not implemented |
| CE-MIL-R5-13 | Same-world journal save/load and independent conservation audit | Replay stable, conservation independently recomputed from event evidence | Tests 122, 135–138; no independent world executor |
| CE-MIL-R5-14 | Fully autonomous daily-to-monthly nation with combat, losses and household economy | Exact population, output, physical costs, decisions, causal reports across scale | NOT EXECUTED; requires calibrated profiles and secondary simulator |

**Execution status:** 108 R1–R4 bounded tests continue to pass. Thirty R5 regression/audit tests (109–138) also pass, for **138 Python tests**. One mixed synthetic hazard/work/funding/combat fixture executes. Tests establish only their specified bounded properties, not independent playtesting, realistic casualties, universal hazard physics, lawful decision validation, or full multi-engine acceptance. See `CMRR_Round_5_Executed_Validation.md`.

#### R6 interrupted-work, recovery and multi-institution acceptance cases — PROPOSED; bounded evidence only

| ID | Required scenario | Required outcome | R6 evidence boundary |
|---|---|---|---|
| CE-WORK-R6-01 | Certified farm hour completes before a fire | Physical input consumed and accepted output credited once | Test 139; source evidence synthetically attested |
| CE-WORK-R6-02 | Duplicate milestone with new or old event identity | No duplicate work, input or output | Tests 140–141 |
| CE-WORK-R6-03 | Elapsed clock or unselected model used to demand output | Reject unless selected process and actual evidence qualify | Tests 142–143; no evidence authentication |
| CE-WORK-R6-04 | Fire occurs after partial production and remaining reservation fails | Preserve accepted output and loss as distinct causes | Tests 144–145 |
| CE-WORK-R6-05 | Legacy completion tries to override tracked milestones | Stop unsafe double-process and unqualified scheduler use | Tests 146–147 |
| CE-WORK-R6-06 | Disrupted job has verified and unassessed intervals | Settle verified work once; retain unresolved labor claim, no fabricated wages | Tests 148–151; labor law not selected |
| CE-WORK-R6-07 | Replacement input has not arrived | No authorized/fictitious continuation | Tests 152–154 |
| CE-WORK-R6-08 | Authorized new work completes exact remaining hours | One total deliverable; original loss stays historical | Tests 155, 165; hourly synthetic process only |
| CE-WORK-R6-09 | Wages accrued at interruption and renewed completion | Distinct actual liability once per certified hour | Test 156; non-hourly agreements untested |
| CE-WORK-R6-10 | Duplicate unauthorized continuation attempts | No additional work or output by lineage duplication | Tests 157, 160 |
| CE-WORK-R6-11 | Save/reload across suspension, settlement and recovery | Exact same-implementation state checksum and references | Tests 158–159 |
| CE-WORK-R6-12 | Unaffected kitchen proceeds during farm interruption | Independent production completes normally | Test 161, combined fixture |
| CE-WORK-R6-13 | Tax assessment while physical stock is lost | No cash from assessment, no duplicated treasury money | Test 162 and fixture |
| CE-WORK-R6-14 | Local labor crisis changes population or unrelated equipment | No invented migration, kits or currency | Test 163 |
| CE-WORK-R6-15 | Early finalization attempted | Cannot claim remaining work or settlement prematurely | Test 164 |
| CE-WORK-R6-16 | Fire and work milestone declared at same physical instant | Qualified causal order required; no ID-order priority | NOT EXECUTED for new work scheduler |
| CE-WORK-R6-17 | Batch manufacturing interrupted with damaged unaccepted intermediate product | Preserve spent input, WIP and salvage via selected nonlinear model | NOT EXECUTED |
| CE-WORK-R6-18 | An autonomous nation recovers over seasons with competing armies and care demands | Multi-scale exact ledger/decision continuity with qualified labor law | NOT EXECUTED |

**Execution status:** 138 inherited R1–R5 Python tests plus 27 new R6 bounded tests numbered 139–165 = **165 passing tests**. One deterministic farm/fire/warehouse/kitchen/household/tax fixture executes. These are *not* 18 fully certified integrated acceptance-case passes, adoption, calibration, playtesting or an independently implemented engine. See `CMRR_Round_6_Executed_Validation.md`.

#### R7 shared-coordinator and work-in-progress acceptance cases — PROPOSED; bounded evidence only

| ID | Trigger and required outcome | Bounded R7 evidence | Still unqualified |
|---|---|---|---|
| CE-FRT-R7-01 | Schedule a tracked job and later actual milestone, committing through correct K-WORK path | Tests 166–167 | Model/evidence validity supplied by fixture |
| CE-FRT-R7-02 | Independent tax assessment proceeds alongside work | Test 168 | General government authority not authenticated |
| CE-FRT-R7-03 | Two same-time milestones attempt same work: neither may win by event ID | Test 169 | Competent reconciliation of competing attestations |
| CE-FRT-R7-04 | Unrelated kitchen work proceeds while farm milestone is contested | Test 170 | Third-party dependency verification |
| CE-FRT-R7-05 | Physical fire and disputed work share frontier: loss acknowledged, unproved work deferred | Tests 171–172 and 193 | True occurrence/observation order and staged dispute resolution |
| CE-FRT-R7-06 | Same-instant prerequisite and result, missing job, or repeated event identity | Tests 173–175 | Structured typed invalidity and dependency diagnostics |
| CE-FRT-R7-07 | Save/load and deferred-claim recovery do not duplicate execution | Tests 176 and 200 | Independent engine replay equivalence |
| CE-WIP-R7-08 | Raw input becomes tracked physical intermediate without finished output | Tests 177–179 and 195 | Selected industrial process and time/energy cost |
| CE-WIP-R7-09 | Qualified inspection and acceptance converts WIP exactly once | Tests 180–181 and 191–192 | Qualified inspector and material/quality model |
| CE-WIP-R7-10 | Rejected/damaged goods salvage only surviving physical quantity | Tests 182–186 and 197–198 | Actual salvageability and waste disposition |
| CE-WIP-R7-11 | Unselected model, impossible stock or source replay cannot create product | Tests 187–188 | External process/evidence authenticity |
| CE-WIP-R7-12 | Competing raw material use defers while unrelated taxes proceed | Tests 189–190 | Optimized authorized same-frontier allocation |
| CE-WIP-R7-13 | Combined loss evidence exceeds holdings: entire current frontier stays uncommitted | Test 196 | Reconciliation of contradictory physical evidence |
| CE-WIP-R7-14 | Unknown operation lacks qualified footprint: never silently execute | Test 199 | Complete module audit/certification |
| CE-WIP-R7-15 | Source profile is fixed per instance, damaged historical binding detectable | Tests 201–203 | Version-aware external profile registry and migration |
| CE-WIP-R7-16 | Integrated work/fire/replacement/fabrication/inspection/salvage sequence | `run_round7_fixture.py` (17 committed events) | Full independent multi-institution engine |
| CE-WIP-R7-17 | Three industries, military procurement and autonomous households over months | NOT EXECUTED | Calibrated strategic producer/consumer and MIL readiness link |
| CE-WIP-R7-18 | Real multi-stage facility with partial goods, energy, workforce, quality grades and nonlinear scrap | NOT EXECUTED | Chosen industrial specialism and rate calibration |

**Execution boundary:** 165 inherited R1–R6 tests and 38 new R7 tests (166–203) pass, for **203 bounded unit tests** in the reference harness. These do not constitute eighteen complete independent acceptance cases, adoption, playtesting, real-world legal validity or a general-purpose game engine. The R7 workpiece model uses a supplied synthetic selected conversion profile and asserted evidence; it does not independently model workpiece manufacture time, energy, wages or the inspection process. Runtime footprints are hand-declared and conservative rather than exhaustively qualified.

## Appendix D — Optional Scoped Reference Profiles

These are the current optional reference profiles, available for explicit compatible selection. They are **outside automatic shared-Core inheritance**. They are provisional design numbers with incomplete calibration; inclusion is neither acceptance nor live playtesting. A campaign keeps its established profile until an explicit prospective selection/mapping (§97). Core transactions, channel semantics, actual knowledge and PC agency still govern.

#### D1. Human functional injury modifiers

For baseline human functional presentation, the inherited modifiers are Minor −5, Moderate −10 and Serious −20; Critical/Mortal require a specific capability/survival assessment. These are optional provisional game values, not a universal physiological scale. A disabled function cannot be restored by a favorable roll. Apply the worst overlapping injury restriction to a function; additional effects require a distinct causal limitation. An arm injury may restrict weapon use while leaving suitable instruction possible.

No anatomical, lethality, treatment or accumulation profile follows from those modifiers. §17's repeated-harm assessment remains required; an unchanged displayed penalty is not immunity.

#### D2. Human fatigue reference

Fatigue is a persistent condition generated by actual activity and recovery constraints. It is separate from injury, sleep deficit, hunger, trauma, morale and interface strain. Robots, nonhumans and extraordinary bodies use suitable profiles rather than automatically inheriting human exertion.

**Optional human fatigue profile:** Rested 0, Taxed 1, Tired 2, Exhausted 3, Depleted 4; affected exertion/sustained-attention modifiers 0, −5, −10, −20, −30. Mark one load point per two hours strenuous work, one per eight hours ordinary active duty, or one exchange of explicitly exceptional maximum exertion. Every two points raise fatigue one step and consume those points. Retain fractional elapsed load internally.

Two hours protected low-demand rest remove one unconverted load point but do not reduce established fatigue. Full suitable sleep lowers fatigue two steps and clears remaining ordinary load; disrupted sleep lowers it one. Clamp the selected track to 0–4. Its exact sleep qualification, deprivation restrictions, continuous-review timing and over-limit deterioration require the campaign profile.

Do not classify the same interval as both ordinary and strenuous work or charge combat automatically as maximum exertion. At Depleted, a further brief exceptional effort needs a declared choice and credible exposure; do not continue a forced march on the player's behalf.

The fantasy forced-travel recovery cap and its load formula are optional compatible profile additions, not universal fatigue changes. Select one cause-accounting model and document the combined triggers. A shortage forecast imposes no second fatigue penalty: actual deprivation/recovery restrictions do (§71).

#### D3. Military cohesion reference

**Scope:** Retained military application/reference defaults; activate and calibrate through the adopted genre/profile. Shared owners remain Core actors, commitments, institutions, conditions, stock and projects.

Morale, cohesion, discipline, and suppression are distinct.

| State | Meaning |
|---|---|
| Morale | Willingness to continue |
| Cohesion | Ability to function together |
| Discipline | Ability to follow procedures and orders under pressure |
| Suppression | Immediate restriction caused by credible hostile threat or fire |

A veteran unit may retain discipline after its morale collapses. Skilled newcomers may lack shared procedures.

Cohesion uses Forming -10, Functional 0, Practiced +5, and Integrated +10 on tasks requiring coordination. Default new units are Forming. One uninterrupted week of relevant collective training can raise Forming to Functional; four further weeks with stable personnel can reach Practiced; eight further weeks plus meaningful evaluated exercises or shared field experience can reach Integrated. These are provisional rates. Each advancement requires suitable leadership, attendance, resources, and review; combat participation alone is insufficient.

Replacing at least one quarter of a unit's personnel within seven days lowers cohesion one state, once per such replacement batch. Losing a command link imposes the actual communication restriction; do not also lower cohesion unless lasting coordination damage is established. Discipline is a separate competence rating used for procedural performance; high discipline does not remove grief or make contradictory orders executable.

Temporary formation disruption is not automatically a permanent cohesion loss. Apply an immediate coordination restriction when warranted; change the enduring cohesion state only when the event produces lasting coordination damage.

Civilian institutional confidence and voluntary community cooperation do not inherit this military cohesion track by default. Replacement integration can also remove a specific specialist capability independently of the selected enduring-cohesion change.

#### D4. Military morale reference

**Scope:** Retained military application/reference defaults; activate and calibrate through the adopted genre/profile. Shared owners remain Core actors, commitments, institutions, conditions, stock and projects.

| Morale | State | Check modifier |
|---:|---|---:|
| 80–100 | Confident | +10 |
| 60–79 | Steady | 0 |
| 40–59 | Strained | -10 |
| 20–39 | Shaken | -20 |
| 1–19 | Breaking | -30 |
| 0 | Combat ineffective for coordinated offensive action | See restriction below |

For units without established values, start at 70. Shift morale only on a material event: local setback or success ±5, serious loss or relief ±10, catastrophic loss or transformative relief ±20. Record one primary change per causal event; do not charge the same deaths again under defeat, fear, and bad news. Distinct later effects, such as prolonged shortage, may apply at their own review interval. Clamp to 0–100.

A morale check uses trained baseline, difficulty appropriate to the shock, and morale modifier: Confident +10, Steady 0, Strained -10, Shaken -20, Breaking -30. A justified leader intervention may add one circumstance modifier. Do not also apply the same shock as several duplicate penalties. Success preserves organized intent; mixed narrows the achievable task or requires regrouping; failure changes NPC willingness according to their orders, escape routes, loyalties, and survival priorities. The player character's choices remain theirs.

At morale 0, a unit cannot undertake coordinated offensive action until recovered. This does not make every member unconscious or prohibit self-defense, aid, or withdrawal. Morale recovery can come from resolved dangers, rest, leadership credibility, supplies, or relief, rather than automatic daily resets.

Test morale only when a material shock challenges it, such as a leader's death, a collapsed flank, catastrophic casualties, exhausted ammunition, encirclement, or unexpected terror. Updating the numerical state and checking an uncertain response are separate steps; not every change requires a check.

At 0, defensive survival and withdrawal remain possible as described above. If an uncertain defensive response needs a morale modifier, use Breaking's -30; this does not remove the prohibition on coordinated offensive action.

The inherited 0–100 values and ±5/10/20 event shifts are optional military calibration. They do not create a universal civilian happiness or loyalty score.

#### D5. Military suppression reference

**Scope:** Retained military application/reference defaults; activate and calibrate through the adopted genre/profile. Shared owners remain Core actors, commitments, institutions, conditions, stock and projects.

Only a threat capable of affecting or credibly endangering the target can generate suppression. Record its source, covered area, and duration. Ordinary fire stopped by known adequate protection does not automatically suppress a sealed armored crew; obscured vision, vulnerable equipment, or uncertain threats may still matter.

| State | Trigger and effect |
|---|---|
| None | No effective ongoing suppressive threat; no penalty |
| Pressured | Effective hostile fire constrains exposed activity; -5 to exposed observation and precision |
| Suppressed | Sustained or converging credible fire; -10 to exposed observation and precision; crossing the covered area creates a separate exposure problem |
| Pinned | Effective coverage prevents safe exposed work or movement; -20 to exposed observation and precision; movement remains a player choice with stated risks |

A successful suppression action raises pressure by one state within its feasible coverage. Mixed creates Pressured if currently None, otherwise sustains the existing state for the exchange. Failure provides no new suppression. Existing pressure persists only while its recorded sustaining cause remains. Fire volume, area, and ammunition commitment are specified before the attempt. The same burst can inflict damage and pressure when causally justified, without rerolling the burst as a second attack.

At exchange end, if the source has ceased or lost coverage, reduce suppression by one state. Reaching genuinely protected cover clears exposure-based restrictions while protection holds; it does not erase independently accumulated stress. Additional hostile sources do not each impose a full duplicate penalty. A successful rally permits one extra step of recovery only if the threat has reduced or protection now supports recovery.

Suppression can also limit movement, command, and observation through its stated exposure restrictions. Do not add separate generic accuracy or command penalties for the same cause. Willingness to expose oneself is an NPC decision or the player's choice, not compulsory movement.

A physical danger and the target's perceived danger can differ. False beliefs can affect an NPC's decisions without giving an ineffective attack physical suppressive capability. Any psychological pressure uses the selected actor/social profile; it is not a second automatic fire penalty.

#### D6. Stock-coverage display reference

The retained optional supply display compares stock coverage D with an adopted horizon H: Full D ≥ 2H; Adequate H ≤ D < 2H; Reduced 0.75H ≤ D < H; Short 0.5H ≤ D < 0.75H; Critical 0 < D < 0.5H; Exhausted D = 0 for a required resource. Labels add no penalties and hide no binding category. Food and ammunition may have different status.

Example fixture: 120 person-days of food for 30 people gives four days at the adopted rate. With H = three days it is Adequate. An expected 60 person-days tomorrow changes a projection only. Existing reservations reduce free stock for a competing plan, not physical stock.

These labels are planning displays, not extra supply ledgers or automatic penalties. Physical stock, eligible accessible stock, unique backing, actual provision and forecasts retain §§12/36/71 meanings.

#### D7. Default action and priority adapter scope

§6 preserves the existing selected d100 competence/difficulty/circumstance/outcome curve. §47 preserves the optional symmetric binary priority proposal. Neither imports a genre's damage, travel, biology, authority, sport performance or equipment values. Alternate complete campaign adapters remain valid within their recorded scope; no automatic scale conversion is supplied.



## Appendix E — Round 8 proposal

## Round 8 — observed dependencies and strategic continuity

**Proposed / unselected, 18 October 2026. Core v3.2 remains selected. R7 and R8 are candidates.**

### What counts as evidence

A manually declared footprint is a hypothesis. An execution certificate identifies the exact pre-state hash, event payload, runtime source hash, observed reads and write intents, and actual changed paths. It is evidence for that execution only. A union of observed paths is a coverage report, never a reusable permission to skip observation. Neither test success nor a document hash selects a new Core.

R8 observes the existing shared `World._operate` and economic helper code through a mapping access boundary. It does not substitute a second economic or military state. A speculative copy is discarded; the existing R7 dispatcher validates actual operations on a transaction copy and the live state is swapped only after the entire selected frontier succeeds. Operation results must agree with the observed execution before qualification. R5 loss, R6 tracked work and R7 fabrication are deliberately refused by this new frontier until their full dispatch paths are instrumented. Their old direct APIs remain inherited candidate behavior.

### Dependency rules

1. Read paths include decisions and prerequisites, not just quantities eventually changed: actor condition/location, qualifications, institutional mandates, received orders, recipe/profile values, reservations, capacities and work windows.
2. Missing-record lookups are reads. Inserting the missing record conflicts with them. Enumeration reads a whole subtree: inserting a new reservation or active job conflicts with a scan that previously found none.
3. Container navigation records existence without assuming all child values were read. Whole-record replacement/deletion conflicts with descendant accesses. Paths are structured tuples, avoiding colon-concatenation ambiguity.
4. List access conservatively reserves the entire list for reading and writing because inherited handlers mutate lists directly. This can overblock; it cannot be advertised as exact leaf-level access. Same-value mapping writes still count as writes.
5. Read/read overlap is allowed; write/read and write/write overlap create a conflict. Additive accounting is not presumed commutative. Shared material totals can therefore block otherwise separable jobs until a qualified reduction protocol exists.
6. Every proposal is observed against the same immutable pre-frontier snapshot. Unknown or invalid proposals conservatively block the batch; observed conflicting proposals remain unexecuted, while disjoint proposals may commit. IDs never choose a scarce-resource winner.
7. Observation is rerun at each commit attempt. A supplied certificate with different state, code, parameters or access sets is rejected. Frontier IDs are unique and timestamps identical. Old processed IDs are not treated as fresh proposals.
8. Global invariant validation occurs on the assembled candidate. Its broad reads are not interpreted as resource consumption. If combined validation fails, the entire live frontier remains unchanged. Clock, processed identities and journal are coordinator bookkeeping, explicitly excluded from domain interference comparisons; no domain handler may use them to hide resource effects.
9. The current boundary is reviewed deterministic, in-process JSON handler code. It is not a security sandbox: arbitrary Python can evade proxies, consult globals, perform I/O or use nondeterminism. Such adapters cannot earn certification by self-declaration. Production plugins require a mediated state API, restricted external effects and complete adapter dispatch instrumentation.
10. Rejected/contested requests preserve original intent and reason. The strategic executor stores these in decision records. Standalone `frontier` callers must persist its returned deferred records; it is not yet a durable queue or adjudication service. Any later grant requires a new genuine decision and revalidation, not backdating.

### Strategic execution

The bounded controller generates proposals from current records at six reviews per day, with hours retained on the same clock. It advances a kitchen business, a household, a tax institution and a military institution. It creates future work commitments, starts feasible work, completes it, provisions meals, records wage liabilities, assesses and pays taxes, and enrolls/equips one authorized member. There is no prewritten 90-day action list. Inputs, disablement, claims and membership change later choices.

The explicitly selected synthetic policy is stored with its hash in `r8_strategy`. Each review records policy/code hashes, source-state hash, actual decision-read paths, proposals, committed IDs and unresolved proposals. These are planning/audit records, not duplicate cash, population or inventory. No player choices are delegated. Mutating the selected policy is rejected; prospective rebinding needs a future procedure.

This is bounded reactive autonomy, not open-ended strategic intelligence. The recipe uses inherited synthetic legacy job completion and does not fabricate R6 work evidence. Wage liability is not payment. Food provisioning is not a complete physiology model. There are no calibrated seasons, supply markets, military readiness, legal reasoning or independent institution beliefs. The planner currently sees authoritative fixture state; recipient-specific information constraints remain a gate before deployment.

### Cross-engine qualification gate

Military, Roman, AST, Fantasy, PAF, SNWE and Space documents are source references with their own retained statuses. Each engine must bind an executable operation to these shared owners or provide a separately instrumented extension. Reusing the same Core implementation under different labels is not independent engine validation.

For each native operation require: source and profile version; all supported branches; actual access observations; negative/phantom/alias/capacity tests; all relevant cross-engine pairings and perturbations; independent serial-order comparison; joint invariant validation; unknown-external-effect rejection; save/replay; and reviewer disposition. Current native certification is **OPEN**, not passed. `results/r8_operation_inventory.json` describes exercised shared handlers only. Engine-source hashes and the gate matrix are separate evidence.

### Acceptance register

| Gate | R8 evidence / disposition |
|---|---|
| Dynamic shared-handler observations | Executed cases for 37 shared handlers; path unions and example certificates |
| Hidden institutional dependencies | Equipment issue vs enrollment regression detects membership-list interference |
| Missing keys and phantom insertions | Executed negative lookup and enumeration tests |
| Scarce pool and no ID winners | Executed conflict/defer and independent-component tests |
| Cached certificate invalidation | Executed stale-state and tampered-access tests; code is hash-bound |
| Serial-order comparison | Executed cash-pair permutation comparison; not all operation pairs |
| Atomicity and source isolation | Executed invalid-operation/source-preservation tests; candidate validation |
| Sustained autonomous continuity | Reproducible 90-day four-institution fixture and 45-day save/reload comparison |
| Constraint adaptation | Resource-exhaustion and disabled-worker tests |
| Every native engine operation/branch | OPEN; source mapping is not executable certification |
| R5/R6/R7 extension dispatch | OPEN; rejected by the new selective frontier |
| External effects, independent runtime, deployment | OPEN; no certification or adoption claimed |

The next implementation priority is a mandatory state-access API spanning the complete R5–R7 dispatcher and native engine adapters. Then qualify adversarial interleavings for shared labor, space, authority, information and logistics; only afterwards broaden autonomous goals and information-limited decision making.



<a id="c2-shared-engine-contract"></a>

## Shared Engine Contract


### IRGS Core 3.3.3.E — Engine Development Supplement

**Edition:** C2 · 20 October 2026  
**Status:** Proposed engine specification for implementation by Claude  
**Selected foundation:** IRGS Core 3.3  
**Development ownership:** Codex develops the engine text; Claude implements and verifies it. Emergent's website and app work is 3.3.E.

This supplement develops the consequential action, dependency, persistence and autonomous execution contracts already described by Core. It does not establish that these additions run, that every numerical model is adopted, or that a campaign has been playtested. The supplied v1.4 master is a proposed design reference. Direct user instructions determine the present engine-only scope.

#### 1. One world and explicit ownership

Each playthrough has one authoritative world. A historical template initializes a new world; it never overwrites a continuing one. Character play, household management, business, government and military activity submit requests against the same actors, resources, commitments, institutions and event history.

3.3.3.A submits proposals and displays authorized results. It must not maintain an independent simulation kernel that generates a second set of outcomes. Classification, narration, dialogue proposals, summaries and images have no direct world-writing authority. A provider's successful response establishes neither a successful action nor an actual occurrence.

The existing logical owners remain:

| Owner | Responsibilities used by this supplement |
| --- | --- |
| K-TIME | Causal order, calendar bindings, schedules, commitments, event identities, retained outcomes and processed intervals. |
| K-ACTOR | Actual persons and other individual actors, conditions, capabilities, location, custody constraints and availability. |
| K-STOCK | Quantities, selected monetary representation, specifications, title, custody, locations, reservations and backing. |
| K-ASSET | Identified objects, components, configuration, condition and physical containment. |
| K-WORK | Tasks, useful work, transformations, accepted outputs, partial progress and completion. |
| K-INFO | Evidence, assertions, estimates, beliefs, information access, reports and actual receipt. |
| K-ORG | Institutions, offices, mandates, roles, qualifications, staffing and succession. |
| K-NET | Routes, operating capacity, allocation and actual delivery. |
| K-POP | Residual cohorts and membership or presence links, conserving totals when individuals are named. |

Domain workflows retain their existing scope: for example, ECO agreements and claims, GOV public decisions, LIFE household and career processes, and MIL mobilization and operations. Workflow records reference the actual K-owner records. A request ledger, database table, application page or planner is not another owner of stock, population or history.

#### 2. What an action means

An action has distinct records and meanings:

1. **Declaration:** the actor's exact expressed intention. It does not establish a consequence.
2. **Selected action:** the proposed method, targets, scope, limits and exact rule or adapter edition.
3. **Attempt:** a specific evaluation of that selected action against a particular world revision.
4. **Occurrence:** what actually happened, including a failed attempt's real exertion, expenditure or exposure where supported.
5. **Outcome:** the resulting actual changes and unresolved remainder.
6. **Information:** which actors observed, received or understood what happened.
7. **Presentation:** an authorized account of the committed outcome and legitimately available information.

Several attempts may refer to one intention. A request identity must never be reused to change the declaration or selected parameters. A revised method is a new request with an explicit supersession link. An event may occur without an actor request, such as an established physical loss; it must retain its actual cause and owner-qualified effects.

Interpretation may propose a typed action or ask for clarification. It cannot introduce a voluntary player commitment, choose an unapproved concession, supply missing inventory or silently replace an unavailable rule with an arbitrary probability.

##### Lifecycle

| Status | Meaning |
| --- | --- |
| `pending` | A durable intention exists and has not yet received a terminal disposition. |
| `awaiting_clarification` | Material method, target or scope is ambiguous. |
| `awaiting_selected_rule` | No applicable executable rule or sufficiently specified qualitative procedure is selected. |
| `awaiting_information` | Required information is genuinely unavailable to the responsible decision maker. Unknown is not zero or observed absence. |
| `awaiting_prerequisite` | A real material, capability, timing or access prerequisite is unmet or unresolved. |
| `awaiting_authorization` | Required control, mandate or voluntary assent is absent, expired or outside scope. |
| `awaiting_allocation` | A shared resource, person or capacity conflict needs a qualified allocation decision. |
| `scheduled` | A valid future commitment is recorded. Its work and outputs have not occurred. |
| `in_progress` | An actual staged process has begun; committed partial consequences persist. |
| `completed_successfully` | The specified completion condition occurred. Success is limited to that condition. |
| `completed_unsuccessfully` | A supported attempt ended without its intended result; real costs and partial effects remain. |
| `interrupted` | An actual process stopped before completion. It may require a new decision or a qualified continuation. |
| `invalid` | The submitted envelope or scope is invalid. No new world effects are committed. |
| `cancelled` | A valid cancellation ended unexecuted or future portions. It does not undo past occurrences. |
| `superseded` | A new request replaces the unexecuted remainder, preserving provenance and past effects. |

These are semantic states, not a requirement to replace functioning existing status strings. Claude must provide an explicit mapping from legacy values, including `declared_not_resolved`, R9 unresolved requests and historical-reference statuses. An existing `resolved` label is insufficient evidence of success. Scheduling is nonterminal while its process remains open; retrying its scheduling event cannot create a second booking.

#### 3. The resolution contract

For every consequential attempt, Core establishes:

- The unique campaign, request, attempt and actor identities, original payload and expected revision.
- Current actor existence, actual control, institutional validity and the relevant actor's information.
- Actual method, targets, means, access, resources and shared capacities.
- The selected rule edition, required inputs, scope, uncertainty and stop conditions.
- The decision frontier and any allocation or new player choice that prevents automatic continuation.
- Actual owner-qualified effects, causal parents, outcome and information consequences.

A nonempty authority string is not a grant. A character may exist without being playable. Being playable permits the selected control scope; it does not confer command over an institution or another actor's property. Formal revocation and knowledge of that revocation remain separate facts.

Resolve routine established capabilities without inventing missing statistics or demanding meaningless rolls. The inherited ordinary-movement case remains valid. Material uncertainty still needs a selected procedure, sufficient evidence, bounded refinement or a truthful unresolved state. Lack of a numeric field is neither universal incapacity nor permission for exceptional ability.

An atomic attempt either commits its complete authorized effect set or commits no effect from that attempted transaction. Long actions use explicitly staged commits. A later interruption preserves earlier actual work, transfers, travel, injuries and consumed materials. It releases only the remaining commitments or reservations that the applicable procedure permits.

A failed physical attempt can have real consequences. A rejected malformed request has none. The engine must distinguish these cases in both the journal and the result envelope.

#### 4. Ordinary action adapters

The following contracts extend the text design. They do not claim that current runtime handlers already implement every adapter.

| Action family | Required meanings and actual effects |
| --- | --- |
| Movement | Identify actor, actual origin, destination or bounded spatial objective, route or local path, custody/access restrictions and method. Ordinary feasible movement needs no invented agility score. Departure, transit, interruptions and arrival update actual presence under an appropriate elapsed-time binding. A distant arrival cannot precede travel. Within-location movement may use a supported positional description; changing a location label is not required when the actual spatial scale is finer than that label. The outcome must nevertheless state what position or movement actually occurred. |
| Observation and investigation | Identify accessible phenomena, method, opportunity, attention and supported sensory or investigative limits. Read actual state; create only justified observations, including uncertainty or a qualified observed absence. Hidden truth does not automatically become a receipt. Authorized bounded generation is retained once and cannot be rerolled by repeating a query. |
| Speech, questions and dialogue | Record utterance, intended recipient, actual transmission and receipt separately. A spoken request does not establish an answer, agreement, appointment or transfer. Resolve NPC responses from their knowledge, motives, capabilities and authority. New voluntary concessions by a player return for acceptance. An interlocutor's claim, genuine undertaking, deception and institutional validity remain distinct. |
| Item handling and transfer | Resolve actual object or stock identity, reachability, access, custody and any required authority. Change physical custody, location or quantity once. Title and institutional recognition change only through their own supported causes. An accessible agreed immediate handover does not need an artificial additional success roll. |
| Eating and drinking | Identify one actual eligible portion, access, actual consumption and the applicable physiological model. Debit that portion once. Employer provision, household accounting and inventory views reference the same use. Do not infer immediate healing, full nutrition or a carried ration from a meal label. |
| Work | Bind actual workers, tools, site, useful inputs, method, shared capacity, intervals and acceptance criteria. Scheduling reserves or commits capacity; actual qualifying work advances K-WORK; accepted output changes its physical owner. Rejected output and unfinished fractions remain distinct from completion. |
| Rest and care | Record actual conditions, opportunity, elapsed rest or care, support and the selected recovery mechanism. Sleep is not an account allowance. Rest does not automatically heal an established wound, supply food, remove obligations or restore an arbitrary percentage. |
| Waiting | Apply the authorized horizon and stop conditions, advance due processes once, and stop at the first material interruption or new player decision. Waiting a week cannot skip an earlier crisis merely because the requested end was later. |
| Training and learning | Identify the function being learned, actual practice, instruction or materials, attention, prerequisites and a selected learning procedure. Record useful learning history and supported capability changes. Background testimony, hours merely booked and possession of a book grant no automatic competence or universal experience points. |
| Purchases and agreements | Preserve offered terms, acceptance, claim or reservation, actual backing, payment, dispatch, delivery and acceptance. Debit or credit the selected monetary ledger once. An accepted procurement request does not teleport goods or create funds; a changed price or new player concession requires a new decision. |
| Institutional requests | Record actual submission, transmission, receipt, responsible office, scope and the decision process. Seeking employment or an appointment does not grant service, wages, rank or access. A supported institution can decide autonomously under its actual procedures. |
| Contested actions | Use a pinned applicable resolution procedure and actual opposing means, constraints, protection and conditions. Retain random or adjudicated outcomes for replay. Apply only supported channels and effects; no universal d100, damage scale, morale rate or historical casualty model is adopted by this supplement. |

#### 5. Dependency certification

Each executable adapter must reveal the records it actually reads and changes during validation, authorization, selection and effects. Observation includes negative lookups, existence checks, scans, container access, actual list mutations, retained decisions and external selected-rule identity. Handwritten footprints can explain a model, but cannot alone certify independence.

Authorization and execution must be observed as one path. An action reading a delegation cannot appear independent of simultaneous revocation. A capacity request reading an empty schedule cannot appear independent of another request that fills it. Reading a list is not itself a list mutation; genuinely mutating an ordered container reserves its actual affected scope conservatively.

The coordinator builds a conflict graph against a shared frontier snapshot. Independent qualified operations may commit together after final invariant validation. Conflicting requests remain unresolved unless an applicable authorized allocation or causal ordering is established. Sorting identifiers, request arrival, UI order and database order cannot select a winner.

Read conflicts do not mean that every contender is physically cancelled. Actual physical occurrences, such as independently established destruction of reserved backing, require their occurrence procedure; a reservation cannot veto reality. Reconcile resulting shortfalls without fabricating replacement stock or erasing obligations.

Certification identifies the exact code, rule and source editions, snapshot, operation, exercised branch and observations. It demonstrates that case, not every branch or arbitrary plugin safety. Changed code or bindings invalidate reuse of old certificates for new claims. Failed and deferred branches need evidence as well as successful examples. See the action and dependency contract for acceptance cases.

#### 6. Time and autonomous institutions

The Core causal sequence, elapsed simulation time, civil calendar, information receipt time and wall-clock persistence time are separate coordinates. Bind them explicitly where a process needs them. A journal sequence increment is not thirty minutes. A time-of-day band is a presentation range, not an elapsed-time arithmetic unit. Navigation, inspection, saving, retry and narration do not advance the world.

An actor's planner receives only information actually available to that actor or institution. It can propose ordinary Core actions within real mandates, resources and commitments. A household cannot consume a meal that a business merely plans to produce. A government claim is not a paid tax. Military readiness is not equipment duplicated from a depot view. Institutions continue in the same world while the protagonist acts or waits.

Each autonomous process declares goals, needs, obligations, known conditions, policy, scope, authorized spending/time limits, next review and stop conditions. Missing observations produce an information requirement or a bounded decision under explicit uncertainty. They are not evidence of an empty warehouse, a dead actor or a free resource.

The scheduler advances to the next causal boundary across all due processes, resolves shared frontiers and retains processed spans. Coarse reviews must preserve meaningful interruptions and individual commitments. Domain plans never simulate private substitute populations or balances. See the agency/time contract for the first four-institution acceptance slice.

#### 7. Historical worlds and character continuity

New historical playthroughs load a designated dated starting snapshot. Continuing worlds use their actual committed temporal registry. Existence, conflict participation, scenario eligibility and player control are different properties. Collapsed or dissolved entities cannot return because a later historical template names them; new simulated organizations may become available through actual formation and eligibility records.

Historical baseline events remain prospective reference assertions until their qualified live causes execute. Check relevant participants, resources, political circumstances and dependencies at the applicable frontier. A failed prerequisite can prevent, alter, postpone or supersede the prospective configuration; it does not require a substitute battle, mandatory victory or global historical correction. Reference outcomes are not actual Chronicle events or player knowledge.

Retain all 37 proposed HYW entry dates and ten featured entries. Only the developed 1415 initializer has the current researched readiness. A Scot's Tale remains a named 1415 starting reference, with its unresolved civil-date reconciliation preserved. Its archived post-Day-2 character guide and the corrected name Abel do not justify an inferred date, recovery, employment or next voluntary act. Reusable mechanics belong to their shared Core or genre owner.

#### 8. Implementation and adoption gates

Claude's first coding milestone is a durable typed action workflow over the existing Military equipment-issue and Roman delegated-activity handlers, with current control and authority checks inside observed execution. Equipment issue can establish completed transfers. A future Roman capacity booking establishes a schedule, not completed labour. Unsupported action families remain honestly unresolved until their adapter is implemented and qualified.

The subsequent milestone binds actual elapsed time and receipt-backed autonomous proposals to that same path. Ordinary movement, observation and dialogue then need their own genuine effect contracts and acceptance evidence before a general first-action or Living Day claim.

Design completion, implementation, passing tests, deployment, campaign adoption, calibration and playtesting are separate statuses. A package checksum establishes integrity, not authority or correctness. This supplement is text development ready for implementation review; it is not a live replacement for the selected runtime.

#### 9. C2 ordinary-action development

The C2 contracts develop the ordinary-action meanings in section 4: `TIMELINE_AND_PROCESS_CONTRACT.md`, `MOVEMENT_AND_OBSERVATION_CONTRACT.md` and `DIALOGUE_AND_SOCIAL_ACTION_CONTRACT.md`. They preserve the common lifecycle, receipt identities, current authority and nine-owner boundaries. Routine capability remains qualitative where supported; missing numerical fields do not impose arbitrary rolls or incapacity.

`PLAYABLE_ACTION_CYCLE.md` connects those contracts through an explicitly synthetic fixture with actual movement, communicated terms, shared-capacity allocation, partial parcel work, interruption, continuation, acceptance and payment. Its selected values belong to the fixture, not to HYW or all IRGS campaigns. `IMPLEMENTATION_PACKETS.md` divides that design into coding scopes while preserving the C1 foundation.

C2 adds 66 proposed acceptance cases to the original 55. It does not add runtime acceptance results. Unimplemented contracts remain visible in the Claude handoff and machine-readable indexes.



<a id="c2-actions-and-dependencies"></a>

## Actions And Dependencies


### 3.3.3.E — Action and dependency contract

**Status:** proposed engine design for Claude implementation. This document does not certify draft code, activate a release or adopt new numerical models. The selected authority remains IRGS Core 3.3. 3.3.3.E develops the text engine; 3.3.3.A presents and submits requests to that engine.

#### Existing interfaces and ownership

`core_world.CoreWorld.apply(eid, at, op, **params)` supplies campaign scope, immutable event replay, clone/validate/commit behavior and the journal/processed ledger. `r9_runtime.observe(state, event)` executes instrumented and ordinary handlers; `frontier(world, events)` derives conflicts and retains unresolved requests. `temporal_registry.available_entities` uses committed registry coordinates. `starting_selection` supplies explicit control. `genre_receivers` contains the existing Military and Roman effects below.

Retain the nine existing authoritative owners. Workflow records reference their facts rather than duplicating them.

| Owner | Required boundary |
| --- | --- |
| K-TIME | Causal order, actual time and scheduling; one campaign event coordination path. |
| K-ACTOR | Actual identities, location, condition and individual availability. |
| K-STOCK | Physical quantities and selected monetary balances; transfers conserve quantity. |
| K-ASSET | Actual assets, components and asset-specific constraints. |
| K-WORK | Activities, actual progress, acceptance and work settlement; reference stock reservations and network capacity through their owners. |
| K-INFO | Evidence, provenance, receipt and observer-specific knowledge. |
| K-ORG | Organizations, roles and mandates. |
| K-NET | Networks, transport and delivery capacity. |
| K-POP | Population membership/accounting referencing actual identities. |

Specialist records retain their established scope: for example, ECO claims do not create cash and GOV decisions do not themselves move people or goods. A workflow outcome is a reference to committed owner events, not a second stock, condition or authority ledger.

#### Request, selection and occurrence

Keep these distinct:

1. **Intent:** the actor's exact declaration, without treating prose as accomplished fact.
2. **Selected operation:** a typed, versioned interpretation accepted under the supported rules. It may remain unknown.
3. **Attempt:** validation and execution against a particular current world revision, producing a recorded decision.
4. **Occurrence/effects:** what the Core actually committed, with source events and supported effective times.
5. **Presentation:** actor-permitted description of those effects after commitment.

A request's immutable accepted record includes schema version, request ID, campaign ID, actor, controller type, exact declaration, selected operation/parameters, causal submission coordinate, source reference and player instruction reference when applicable. Hash canonical finite JSON; preserve exact strings. The semantic payload digest excludes the coordinator-assigned submission coordinate and expected head revision. A separate original-record digest covers the full accepted record with its frozen coordinate. A retry recovers that accepted coordinate; it does not assign a new current-clock value. A changed interpretation creates a new request linked to the original. Never rewrite an accepted request to make an expired window valid.

Illustrative persisted synthetic request, using existing native parameter names. `at` is the coordinator-assigned causal submission coordinate, not permission for a client to backdate an action:

```json
{
  "schema_version": 1,
  "request_id": "issue-01",
  "campaign_id": "fixture-campaign",
  "actor": "commander",
  "controller": "player",
  "declaration": "Issue the kit authorized by order O-1.",
  "selection": {
    "operation": "military_issue_equipment",
    "params": {
      "order_id": "O-1",
      "commander": "commander",
      "persons": ["worker"],
      "material": "kit",
      "quantity_each": 1,
      "from": "depot",
      "authority_ref": "authority-A"
    }
  },
  "at": 12,
  "source_ref": "fixture:reviewed-request",
  "instruction_ref": "player:instruction-01"
}
```

The nested parameters cannot override campaign, instruction, source or attempt identity. Identifiers must be unique within campaign scope. Verify scope before replay lookup. Submission and attempt/phase receipts have separate identities. An identical accepted retry returns its original acknowledgement or attempt receipt, including after reload; changed payload under that identity fails. A pending or scheduled intention can receive a new qualified attempt under a new identity; replaying the original submission does not execute that continuation.

An attempt records its own identity, request digest, expected world revision, code/rule identities, evaluated prerequisites, result status, dependency evidence and committed event references. Publish state effects and the recoverable receipt atomically behind the revision check. A database or process-local lock alone does not satisfy this contract. Save/restore uses the same serialization boundary; it cannot be silently overwritten by an older in-flight attempt.

#### Authorization and lifecycle

Inside the instrumented execution path, validate actual actor existence, current control policy, instruction, received authority, selected rules, resources, capacities and temporal feasibility. `player_actor_ids` alone is insufficient after eligibility revocation. A selected faction's policy may authorize its named control actor without a separate individual eligibility grant. Existence, participation and control remain different properties.

Orders/delegations must match the actor, exact scope, active interval and established authority basis under the campaign's selected rules. A nonempty `authority_ref` proves none of these. Trusted synthetic fixture setup is an explicit source selection, not proof of historical legal power. Player and autonomous proposals share the same validation/effect path; unsupported autonomous authority remains pending.

The supplement's lifecycle table is canonical: `pending`, `awaiting_clarification`, `awaiting_selected_rule`, `awaiting_information`, `awaiting_prerequisite`, `awaiting_authorization`, `awaiting_allocation`, `scheduled`, `in_progress`, `completed_successfully`, `completed_unsuccessfully`, `interrupted`, `invalid`, `cancelled` and `superseded`. The first bounded implementation must distinguish the states it can reach and explicitly hold unsupported transitions. Reasons identify the failed requirement. Existing status names require an explicit semantic mapping. A failed prerequisite creates no physical effects. Cancellation terminates remaining intent; it never erases earlier occurrences. Scheduling is not completion of the scheduled work, and a later execution phase must remain possible.

The current Core `clock` is causal sequence. `campaign_time` and `entity_registry.as_of` are distinct coordinates without an adopted elapsed-time binding. This milestone must not infer hours or advance civil dates from request counts. Timed effects require an explicit calendar/profile binding.

#### Native examples

**Military issue:** existing `military_issue_equipment` reads a received order, verifies matching directives and deadline, transfers actual kits through Core stock operations and marks that order executed. Validate every recipient's current existence. Outcome `completed_successfully` means those specified transfers occurred; it establishes no travel, enlistment, wages or general victory.

**Roman booking:** existing `roman_begin_delegated_activity` reads an active delegation and uses shared actor/site capacity. An illustrative selection is:

```json
{
  "operation": "roman_begin_delegated_activity",
  "params": {
    "delegation_id": "D-1",
    "delegate": "delegate",
    "activity_id": "work-01",
    "actors": ["worker"],
    "site": "yard",
    "capacity_id": "yard-capacity",
    "start": 50,
    "end": 60,
    "role": "craft",
    "authority_ref": "authority-B"
  }
}
```

These synthetic coordinates are prospective bounds on the selected fixture axis, not universal durations. Outcome `scheduled` means the booking exists. It grants no completed work, consumed materials, output or pay.

#### Execution-derived dependencies

Instrument authorization and effects together. External prechecks cannot supply an unobserved permission dependency. Capture actual positive and negative lookups, existence tests, scans, container navigation and selected list reads. Record list writes only for actual mutation; ordinary reads must not invent shared writes. Include C-level mutation backstops and prove instrumented/ordinary semantic parity.

Qualify successful and rejected executions. Preserve reads leading to rejection, reason, rollback proof and any independently established occurrence. A missing branch/case remains unqualified. Global validator scans may be distinguished from allocation dependencies only when the combined candidate is independently validated before commit; validators cannot mutate state.

Build conflict edges for noncommutative records, resource pools, overlapping finite capacities, prerequisites and indivisible transactions. Do not choose winners by request ID, array order or hash. Retain allocation conflicts for a later authorized decision and revalidate then. Unsupported handlers receive a conservative compatibility barrier; absence of a footprint is not independence. Actual measured physical losses remain occurrences, subject to evidence reconciliation rather than administrative allocation preference.

Certification evidence identifies exact code/rule hashes, input snapshot, request/attempt payloads, observed reads/writes, validator checks, post-state or rejection, and exercised branch. A passed case does not certify all handlers or all branches. Adding an operation requires its own evidence and integration into the operation inventory.

#### Acceptance cases for implementation

All quantities and identities below are explicitly selected test fixtures.

| ID | Input state and operation | Observable required assertion |
| --- | --- | --- |
| A01 | Ten kits; matching received order; issue one | Depot nine, recipient one; total ten; one linked completed outcome. |
| A02 | Retry A01 with identical request/attempt | Same receipt; no extra transfer, event or time change. |
| A03 | Reuse A01 ID with changed quantity/text | Reject altered payload; world unchanged. |
| A04 | A01 under another campaign ID | Reject before lookup or disclosure. |
| A05 | Valid declaration; unsupported selected operation | Await selected rule; no inferred physical success. |
| A06 | Existing actor lacks current player control | Await authorization; no stock change. |
| A07 | Previously controlled actor; eligibility revoked | Old player list grants no continuing authority. |
| A08 | Selected faction authorizes its actual control actor | Validate faction policy; do not require unrelated individual eligibility. |
| A09 | Order absent, unreceived, expired or mismatched | Specific pending reason; no partial transfer or executed flag. |
| A10 | Correct order; stock now insufficient | No negative stock or partial issue; preserve request. |
| A11 | Recipient ceased to exist before execution | No receipt of equipment; current existence read appears in evidence. |
| A12 | Two requests claim the same finite pool | Conflict retained for both; ID ordering selects neither. |
| A13 | Separate orders/stocks; execute in either order | Equal physical results; certify independence or disclose conservative barrier. |
| A14 | Simultaneous eligibility revocation and issue | Actual authorization read conflicts with revocation write. |
| A15 | Simultaneous recipient dissolution and issue | Conflict detected before either inferred order of occurrence. |
| A16 | Valid Roman delegation and free capacity | One scheduled booking; no work/output/pay or elapsed-time claim. |
| A17 | Roman booking overlaps full site/actor capacity | Await allocation/prerequisite; no second booking. |
| A18 | Delegation revoked alongside Roman booking | Conflict detected from actual delegation access. |
| A19 | Cancel pending request, save and reload | Cancellation persists and retries idempotently; no later execution. |
| A20 | Crash/retry or restore during in-flight attempt | Recover committed receipt or definite uncommitted status; no stale overwrite. |
| A21 | Hidden fact/NPC location changes | Player projection unchanged without legitimate receipt. |
| A22 | List read, append, deletion and negative lookup cases | Read/write traces match actual accesses; parity and rollback hold. |

#### Known limits

Current native handlers and R9 fixtures do not establish general movement/combat, freeform adjudication, complete lawful authority, campaign-native institutional autonomy, automatic calendars or crash-safe host persistence. Emergent's active lightweight engine is not yet a CoreWorld adapter. Preserved coding drafts are inactive and excluded from the design handoff; isolated component tests are not integrated acceptance. Claude should implement and qualify this bounded contract before expanding those systems.



<a id="c2-persistence-and-recovery"></a>

## Persistence And Recovery


### IRGS 3.3.3.E — Persistence and recovery contract

Design handoff · 20 October 2026 · Proposed implementation contract

#### Scope and existing authority

This document specifies engine behaviour for later implementation by Claude. It does not activate a runtime, approve a storage migration, or claim that the acceptance cases below have passed. Codex's 3.3.3.E work owns engine design; Emergent's 3.3.3.A work owns website and app presentation. Both must refer to one authoritative campaign world.

The selected baseline remains IRGS Core 3.3. Inspect the actual implementation before changing it. Relevant existing interfaces are `IRGS_3_3/runtime/core_world.py` (`CoreWorld.apply`, `save`, `load`, `checksum`, `_validate`), `r9_runtime.py` (`observe`, `frontier`, retained requests and resolutions), and `irgs_reference.py` (`canon`, `digest`). Existing `CoreWorld.apply` checks campaign scope before processed-event replay and rejects a changed event payload. Extend these guarantees to submitted actions and durable recovery rather than replacing them with a parallel action journal.

The nine owners in `IRGS_3_3/Core/IRGS_Core_Engine_v3_3.md:3028–3036` remain authoritative: K-TIME owns causal scheduling and the campaign journal; K-ACTOR actual people and conditions; K-STOCK conserved quantities; K-ASSET identified objects; K-WORK actual tasks and progress; K-INFO evidence and received knowledge; K-ORG organizations and mandates; K-NET routes and operating capacity; K-POP residual cohorts. Persistence stores those records. It grants no new ownership of their meaning.

#### Logical records and identities

The following are logical schemas, not mandated tables or duplicate simulation owners. Identifiers are nonempty opaque strings. Revisions are nonnegative integers. Digests are identified SHA-256 values over a versioned canonical UTF-8 JSON representation. Reject duplicate object keys, nonfinite numbers and unsupported value types before canonicalization. Do not silently normalize semantic identifiers or declaration text.

| Record | Required typed fields |
| --- | --- |
| CampaignHead | `campaign_id: ID`, `revision: Revision`, `state_ref: ID`, `state_digest: Digest`, `core_binding_ref: ID`, `source_edition_refs: ID[]`, `schema_version: ID` |
| ActionRequest | `campaign_id`, `request_id: ID`, `principal_ref: ID`, `actor_ref: ID`, `kind: ID`, `command: JSON`, `declaration_ref: ID?`, `source_refs: ID[]`, `semantic_payload_digest: Digest`, `original_record_digest: Digest`, `submission_at: Coordinate`, `accepted_revision: Revision` |
| SubmissionReceipt | `campaign_id`, `request_id`, `transaction_id: ID`, `accepted_revision: Revision`, `semantic_payload_digest`, `original_record_digest`, `initial_attempt_ref: ID?` |
| AttemptRecord | `campaign_id`, `request_id`, `attempt_id: ID`, `phase_id: ID`, `expected_revision: Revision`, `rule_refs: ID[]`, `original_attempt_digest: Digest`, `status: RequestStatus` |
| OutcomeReceipt | `campaign_id`, `request_id`, `attempt_id`, `phase_id`, `transaction_id: ID`, `revision: Revision`, `state_digest`, `event_refs: ID[]`, `status: RequestStatus`, `result: JSON`, `pending_refs: ID[]` |
| RequestStatusView | `campaign_id`, `request_id`, `head_revision: Revision`, `status: RequestStatus`, `current_attempt_ref: ID?`, `outcome_refs: ID[]`; derived from retained records in the selected lineage |
| PendingWork | `campaign_id`, `work_id: ID`, `request_ref: ID`, `prerequisite_refs: ID[]`, `observed_revision: Revision`, `status: WorkStatus`, `producer_ref: ID`, `claim_epoch: integer`, `attempt_ref: ID?`, `result_ref: ID?` |
| Checkpoint | `campaign_id`, `checkpoint_id: ID`, `revision`, `state_ref`, `state_digest`, `request_boundary_ref: ID`, `schema_version`, `source_edition_refs`, `label: string?` |
| BranchProvenance | `campaign_id: new ID`, `parent_campaign_id: ID`, `parent_checkpoint_id: ID`, `parent_revision`, `parent_state_digest`, `fork_instruction_ref: ID` |

Request identity is the pair `(campaign_id, request_id)`. An attempt/phase has its own scoped identity and immutable receipt. Event, transaction, provider-task and presentation identities remain distinct and explicitly linked. The semantic request digest covers campaign scope, principal, actor, kind, exact semantic command, declaration reference, selected rules and sources. It excludes the coordinator-assigned submission coordinate, wall-clock metadata, expected-head revision and narration preferences. A second original-record digest covers the accepted immutable record, including its frozen submission coordinate. Retrying submission retrieves the first accepted coordinate; it never restamps the request from the current clock.

Submission replay returns the immutable acknowledgement and a separately identified current-status projection. A previously pending or scheduled receipt does not prevent a legitimate later attempt or process phase. Executing that continuation requires a new attempt identity, current revision and unchanged selected intention, or an explicit superseding request when the method changes. Retrying an accepted attempt returns that attempt's historical receipt; it never executes the phase again.

`RequestStatus` follows the supplement's canonical lifecycle: `pending`, `awaiting_clarification`, `awaiting_information`, `awaiting_prerequisite`, `awaiting_selected_rule`, `awaiting_authorization`, `awaiting_allocation`, `scheduled`, `in_progress`, `completed_successfully`, `completed_unsuccessfully`, `interrupted`, `invalid`, `cancelled` and `superseded`. A durable accepted request can remain unresolved. `WorkStatus` distinguishes recoverable waiting, claimed execution, completed, cancelled and retryable failure. Each transition preserves its actual cause and prior references.

#### Submission and commit ordering

1. Authenticate the caller and verify permission to access the requested campaign and receipt. Validate explicit campaign scope before looking up replay data. A caller-supplied authority string is not proof of permission or an institutional mandate.
2. Validate the request envelope and canonical semantic payload. Acquire the campaign's serialization boundary or an equivalent transactional compare-and-swap mechanism.
3. Look up the scoped submission or attempt identity for the command being retried. Compare the appropriate immutable digest. A mismatch fails. A match returns its original authorized acknowledgement or attempt receipt, with separately labelled current continuation metadata and no execution. Use the frozen accepted submission coordinate. Perform this recovery before rejecting an obsolete expected-head revision.
4. For a new submission or a new attempt/phase on an existing intention, compare the expected revision with the actual head. A mismatch returns a conflict and the permitted current revision; it neither overwrites the head nor silently rebases the action.
5. Construct a detached candidate from the verified head. Check actual actor existence, player control or mandate, information receipts, prerequisites, selected rules, quantities and finite capacities. Use the existing execution-derived dependency machinery. Identifier order supplies no allocation authority.
6. Resolve supported effects through owner interfaces. Preserve unsupported intent with an explicit unresolved reason. Partial activity requires actual committed milestones; elapsed time or narration cannot manufacture completion.
7. Atomically persist the validated authoritative candidate, its journal and processed markers, the immutable request/outcome links, recoverable pending work and the new head revision. Either the complete related commit becomes visible or none of it does. An unresolved accepted request may advance the storage revision without advancing world time.
8. After durable confirmation, acknowledge the receipt and schedule presentation from the committed result and permitted actor projection. A failed acknowledgement or narrator call retries receipt retrieval or presentation, never the Core effects.

Store engine results and pending records consistently with their existing owners. An operational transaction index may reference the authoritative journal; it must not become a second independently editable history of world events.

#### Failure and restart boundaries

| Interruption point | Required recovery |
| --- | --- |
| Before durable acceptance | Retain any separately saved draft; do not report acceptance or effects. |
| Accepted but awaiting a rule, report or authorization | Reload the same request and reason; preserve its identity and pending prerequisites. |
| Candidate effects calculated but uncommitted | Discard the candidate; recover the confirmed head. Retry only through the original identity. |
| Storage commit result uncertain | Query the transaction/request record under serialization before attempting execution again. |
| Committed, response lost | Return the original receipt; effect and revision occur once. |
| Committed, narration failed | Regenerate presentation from existing event references without modifying simulation state. |
| NPC worker claimed work, then exited | Recover or expire the claim using an explicit worker policy; revalidate prerequisites before committing once. |
| Interrupted work after real milestones | Preserve settled effects and remaining work; do not roll back actual past consequences. |

NPC work cannot exist solely in an in-memory asynchronous task. Persist its request and dependencies before dispatch. Use a durable claim, attempt identity and completion receipt so restart, duplicate delivery and multiple workers cannot double-commit. A lease timeout permits recovery review; it does not prove the prior attempt failed to commit. Check its receipt first. A new claim carries a monotonic fencing epoch checked at commit; a late worker with an obsolete claim cannot overwrite its successor. Worker outputs are proposals until ordinary Core validation accepts them.

#### Checkpoints, restoration and forks

A checkpoint captures one consistent confirmed revision, including its pending-work boundary and compatibility references. It creates no in-world event, elapsed time, healing, resources or NPC decision. Reusing a checkpoint identity cannot silently replace its contents.

Restoration is an explicit, authorized management request with its own immutable identity. Serialize it against actions and pending-work commits. Require an expected current revision, verify checkpoint integrity and scope, and install its snapshot as a new storage-head revision. An action calculated against the displaced head must fail its commit comparison, not overwrite the restored world. Old acknowledgements and accepted request identities remain recoverable: replaying an old request ID must never apply its effects anew after restoration. Historical receipts must identify their original revision rather than imply their effects are present in the current restored head.

Reconcile restored pending work against the retained attempt index. A task may have been pending at the checkpoint but completed on the discarded future head. Its historical receipt neither recreates that effect nor proves completion in the restored world. Invalidate displaced worker claims; hold the task or authorize a new continuation under the selected restoration policy, with a new attempt identity and current revision. Preserve the old attempt and both lineage references. Never silently replay an old accepted attempt or leave a restored task blocked merely because a different historical head completed it.

A branch receives a new campaign identity and immutable parent/checkpoint provenance. Preserve the inherited past as a verified snapshot with source-event lineage. Do not re-execute that past to initialize the branch. Rebind active campaign-scoped references through a qualified fork operation. Inherited pending work must be explicitly mapped, held or cancelled; copying an executable worker claim is insufficient. New branch actions receive new scoped identities and may create a different future. Parent and branch must share no mutable state.

#### Integrity, clocks and storage choices

Checksums detect accidental or unauthorized byte/state changes relative to a trusted reference; they do not authenticate callers, establish historical truth or prove a rule was adopted. Preserve access control and source provenance separately. Validate saved state through Core invariants and compatibility metadata before use. Opening, inspecting or loading a save must not migrate it, reseed the world, restore historical-template factions or regenerate missing quantities. Migration requires a separately reviewable, source-preserving operation.

Storage revision, causal clock, civil date and elapsed duration are different coordinates. The current Core clock orders causal events; incrementing it does not establish thirty minutes or a civil day. Time advancement needs an explicit selected calendar and duration rule. Saving, inspection and receipt retrieval do not advance simulation time. Restoration reinstates the checkpoint's saved temporal state under a new storage revision without executing intervening events.

SQLite transactions or transactional MongoDB arrangements may implement this contract. A revision-filtered replacement alone is insufficient if request receipts and pending work can fail independently. Choose an atomic arrangement supported by the actual deployment, or a staged recovery protocol with a provable durable commit boundary. Do not introduce another simulation database merely for a new interface.

#### Proposed acceptance cases

These are required implementation checks, not executed-test claims.

| ID | Setup and expected result |
| --- | --- |
| PR-01 | Submit one supported transfer; state, journal, receipt and head expose the same committed transaction and conserved quantity. |
| PR-02 | Retry after a lost response with the original request and obsolete head; recover its frozen submission coordinate and original receipt, with no new debit or revision. A new attempt/phase remains possible under a new qualified identity. |
| PR-03 | Reuse that identity with a different amount; reject it without changes. |
| PR-04 | Request another campaign's receipt without permission; reject before revealing whether that request exists. |
| PR-05 | Submit a fresh request against a stale revision; reject before applying any candidate effect. |
| PR-06 | Exit after calculation but before commit; restart shows the prior confirmed state and no successful receipt. |
| PR-07 | Exit immediately after commit; restart returns the one accepted outcome and durable pending-work references. |
| PR-08 | Fail narration repeatedly; world checksum, event count and quantities remain unchanged. |
| PR-09 | Deliver one NPC task twice to independent workers; at most one owner-valid effect commits. An old claim's late result fails the fencing/revision check. |
| PR-10 | Restart with a claimed NPC task; recover its receipt or revalidate a new attempt without creating a duplicate event. |
| PR-11 | Capture and inspect a checkpoint; clock, conditions, resources and NPC activity remain unchanged. |
| PR-12 | Race restoration with an action; one valid revision transition wins and the stale writer receives a conflict. |
| PR-13 | Restore an earlier checkpoint, then retry an old accepted action ID; retrieve its historical receipt without resurrecting the effect. Restored pending work completed on the discarded future is held or assigned a new authorized continuation; it neither replays the old attempt nor remains falsely completed. |
| PR-14 | Fork a checkpoint; inherited events are not replayed, provenance is explicit, and later branch writes leave the parent unchanged. |
| PR-15 | Alter a saved checksum or incompatible schema; refuse activation without reseeding or read-time repair. |
| PR-16 | Accept an unresolved rule-dependent request; persist its reason and pending state while leaving actual world time and resources unchanged. |



<a id="c2-agency-and-presentation"></a>

## Agency And Presentation


### IRGS 3.3.3.E — Agency, Time and Presentation Contract

Design handoff for Claude · 20 October 2026

This document specifies the next engine implementation. It is not a completion report. **3.3.3.E** is the Codex engine design line; **3.3.3.A** is Emergent's website and application line. Selected Shared Core 3.3 remains authoritative. Proposed models, source-document instructions and experimental code do not become adopted mechanics through this document.

#### 1. Ownership and execution boundary

All people, households, businesses, governments and military institutions occupy one campaign world. Their planners submit intentions to the same Core validation, dependency, allocation, execution and persistence path used for player intentions. A planner cannot directly edit an actor, stock balance, capacity, relationship, legal position, clock or journal. Presentation cannot supply those edits either.

Reuse the established owners: K-ACTOR identities and actual condition; K-STOCK conserved quantities and custody; K-WORK activities and transformations; K-INFO assertions and received information; K-ORG mandates and institutional roles; K-NET routes and shared capacity; K-TIME scheduling and retained outcomes. Planners and projections are consumers, not additional authoritative databases. Existing asset and population owners remain authoritative where involved.

Player control and institutional authority are separate. An actor's current control policy can permit declaring personal intent without permitting requisition, taxation or command. A stored player ID, model response or nonempty authority reference is insufficient permission. Recheck current actor existence, selected control, actual mandate, scope and relevant receipts inside execution-derived observation.

#### 2. Planner input: received and bounded information

Construct a detached input for one planning identity and one committed campaign revision. Supply only records legitimately available through that actor's or institution's actual information channels. A household ledger subscription does not grant access to every nearby depot. Institutional knowledge is not automatically the knowledge of every employee or ruler.

The proposed input envelope is:

```json
{
  "campaign_id": "campaign identity",
  "revision": 42,
  "planner_id": "installed policy identity",
  "principal_id": "actor or institution",
  "acting_actor_id": "actual registered actor",
  "policy_ref": "qualified policy and edition",
  "time_context": {"timeline_ref": null, "causal_sequence": 120},
  "authority_refs": ["actual scoped mandate"],
  "observations": [
    {
      "record_ref": "named bounded record",
      "receipt_ref": "actual receipt or qualified subscription",
      "occurrence_time": null,
      "received_at": "explicit information coordinate",
      "observed_at": "explicit observation coordinate",
      "status": "known_value",
      "value": "received value",
      "source_ref": "provenance"
    }
  ],
  "goals": [],
  "needs": [],
  "obligations": [],
  "current_activity_refs": []
}
```

Observation status must distinguish `known_value`, `observed_absent`, `unknown`, `disputed` and `stale`. Observed absence requires a qualified observation of a named scope; missing input never proves absence. Preserve occurrence time, receipt time, observation age, uncertainty and source status. Receiving a report does not establish that its assertion is true. A planner may reason from testimony while Core independently checks actual feasibility.

Goals, needs and obligations must reference actual records or an explicitly selected policy configuration. Never invent hunger rates, tax debts, employment, personality scores, inventory or wages to make planning appear active. Where required observations or selected models are missing, produce an unresolved proposal or an explicit no-action decision with that reason.

#### 3. Planner output and institutional scope

A planner returns typed proposals, never executable code or direct state patches. Each proposal carries `proposal_id`, `campaign_id`, `planner_id`, `acting_actor_id`, `input_revision`, `policy_ref`, relevant receipt references, exact selected operation and parameters, authority references, prerequisites and a timing requirement. Retain its decision explanation separately from mechanical facts. No model-generated explanation constitutes evidence of an effect.

Output also supports an explicit decision record: `no_action`, `unknown_information`, `awaiting_selected_rule`, `awaiting_prerequisite` or `awaiting_authorization`. Record why the decision was made and which observations were consulted. `no_action` means an intentional policy decision under available information; `unknown_information` means the planner cannot determine an appropriate action. Neither advances time by itself.

| Institution | Bounded planning responsibility |
| --- | --- |
| Household | Consider recorded members, known provisions, actual obligations and available labour. Request transfers or provisioning only through qualified mechanics. |
| Business | Consider actual orders, workers, qualifications, work capacity, inputs and contractual obligations. Propose feasible work or deliveries without creating demand or stock. |
| Government | Consider received fiscal reports, established claims, lawful jurisdiction and actual administrative capacity. A policy target does not establish collectible revenue. |
| Military | Consider received orders, actual command scope, known personnel, readiness, equipment, supply and route capacity. An order does not establish mobilization or delivery. |

The same worker, material, site or vehicle cannot be independently allocated by these planners. Preserve cross-institution competition through shared Core records. A policy may be installed for multiple institutions, but each invocation retains its own principal, information, mandate and provenance.

#### 4. Durable lifecycle and pending work

Retain proposal identity, immutable original payload and digest before consequential execution. Link every execution attempt, allocation decision, committed effect and outcome to that identity. Accepted retries return the existing receipt; altered payloads under the same identity fail. Transport success means the request was retained, not that the intention succeeded.

Persist pending NPC work with its campaign, initiating event, expected revision, input references, policy edition and processing state. A background task may perform computation, but it is not the pending-work authority. After restart, recover or explicitly defer retained work. A timeout must not silently mark an unfinished proposal complete or merely hide its pending status.

Revalidate a stale proposal against current state before committing. Preserve the original proposal and add the new attempt; do not rewrite its input history. State, effect references, request status and durable receipt must share an atomic commit boundary or an explicitly recoverable staged protocol. Restore and action execution require the same revision and serialization protection.

#### 5. Time, deadlines and interruptions

Keep causal sequence, elapsed simulation time and civil-calendar position distinct. A causal counter orders commits; it does not measure minutes. A day-precision opening does not establish dawn or an exact hour. Existing activity coordinates must retain their documented axis until an explicit compatible timeline binding is selected.

A qualified timeline binding specifies units, origin, supported calendar conversion, precision and duration models. Julian dates require Julian arithmetic. Other calendars require their own selected rules. Unsupported conversions remain unbound. Never adopt a fixed thirty-minute action, six-band day, recovery rate or journey duration merely because a prototype used it.

With a qualified elapsed-time model, find the next relevant deadline, completion, interruption or information arrival. Evaluate simultaneous ready proposals against the same pre-frontier world. Include actual authorization, availability, resource, capacity and prerequisite reads in observed dependencies. Commit independent effects only where their combined candidate satisfies invariants. Preserve competing requests when no qualified allocation rule or authorized decision selects a winner; identifiers and incidental iteration order select none.

Long actions need explicit stages. Retain actual partial work, consumed inputs, injuries, reservations or deliveries when an interruption occurs. Cancel only unperformed stages under the selected rules. An interruption cannot erase committed consequences, and scheduling cannot establish that future work occurred. Without an elapsed-time model, qualified ledger effects may be recorded at their supported precision while duration remains unknown; this does not establish zero duration. A duration-dependent process cannot advance beyond its supported timing.

#### 6. Two required execution traces

**Received military order.** A registered NPC receives a specific equipment-issue directive. Its planner sees that receipt and the bounded records legitimately available to it. It proposes the existing Military issue operation with the actual recipient, persons, material, depot, quantity and authority. Core rechecks the directive, deadline, actor existence, command scope and conserved stock. Success transfers the stock once and marks that order executed. Missing stock leaves the request unresolved; a contradictory rumour cannot manufacture stock. A restart or retry preserves the same outcome.

**Roman future booking.** A delegation identifies delegate, principal, people, role, site and permitted window. Actual delegation alone does not establish that an autonomous delegate received it; missing communication leaves autonomous planning awaiting prerequisite. After a legitimate receipt and selected timing basis, Core may book a qualified activity against shared people and capacity. The outcome is `scheduled`. It establishes neither performed labour nor manufactured output, wages, elapsed time or automatic completion. Later revocation or interruption follows the qualified cancellation and partial-effect rules.

#### 7. Conditional history and presentation

Historical baseline events remain prospective reference material, privately scoped to qualified Creator inspection. They are not actor knowledge, journal occurrences or mandatory outcomes. A scheduler can submit a conditional historical proposal only when its model, prerequisites, participants and timing are qualified against the actual playthrough. A collapsed kingdom or dead participant cannot reappear because a template expects it.

For a new historical game, use its designated starting snapshot. Continuing games use their committed world and source edition. Reevaluate affected causal descendants when prerequisites change; do not impose a global divergence score, forced victory or predetermined end date. Unknown causal bindings remain unknown.

3.3.3.A receives committed outcome references and legitimately filtered observations. Narration follows resolution and cannot supply additional effects. Report an unresolved intention as unresolved. A failed, repeated or corrected narration must not repeat mechanical execution. Preserve presentation errors separately from committed world outcomes. No provider selection, UI implementation or website redesign is prescribed here.

#### 8. Acceptance cases for implementation

| ID | Case | Concrete expected outcome |
| --- | --- | --- |
| AG-01 | Missing household report | Planner returns unknown information; it does not infer an empty pantry. |
| AG-02 | Observed empty pantry | A qualified scoped observation permits planning from absence; no food appears automatically. |
| AG-03 | Unreceived military order | NPC cannot plan its execution from global world truth. |
| AG-04 | Received equipment directive | Exact qualified issue transfers conserved stock once and produces a linked receipt. |
| AG-05 | Lost response and retry | Same identity returns the original outcome; stock and clock are unchanged by the retry. |
| AG-06 | Altered accepted payload | Engine rejects it without changing the original request or world. |
| AG-07 | Competing depot requests | Shared dependency is detected; no identifier-order winner is chosen. |
| AG-08 | Independent institutions | Both qualified effects commit with equivalent domain results under either evaluation order. |
| AG-09 | Revoked authority | A pending proposal cannot use the obsolete mandate; no partial effect commits. |
| AG-10 | Roman booking | Outcome is scheduled; output stock, wages and completed-work history remain unchanged. |
| AG-11 | Interrupted work | Actual committed partial consequences survive; unperformed stages do not become complete. |
| AG-12 | Unbound calendar | Causal commits produce no inferred minutes, hour, date or day transition. |
| AG-13 | Julian leap boundary | Under a selected Julian binding, 28 February 1500 is followed by 29 February. |
| AG-14 | Restart during NPC planning | Retained pending work is recovered or explicitly deferred without duplicate execution. |
| AG-15 | Concurrent restore | Stale action commit fails its revision check instead of overwriting the restored world. |
| AG-16 | Historical participant absent | Exact historical proposal is blocked or reassessed; no actor or kingdom is resurrected. |
| AG-17 | Narration failure | Mechanical receipt remains valid; retrying presentation produces no additional effect. |

Historical durations, consumption, productivity, recovery, wages, travel capacity, command practice and causal event conditions require sourced, versioned model selections. Until researched and qualified, their absence remains visible. These acceptance cases define work to prove, not results already achieved.



<a id="c2-institutional-execution"></a>

## Institutional Execution


### 3.3.3.E — Shared-world institutional execution model

Proposed engine design · C1 · 20 October 2026

This model develops the household, business, government and military planning procedures for implementation after the durable action foundation. It supplies decision structure without adopting historical rates, fixed personalities, universal needs or fabricated institutional powers. It extends the agency contract and uses the same canonical action lifecycle.

#### 1. Installed policy and review

A policy installation identifies its institution, actual operating actor, effective interval, source edition, goals, observation channels, mandate limits, spending and time limits, decision procedure, relevant models, next review and stop conditions. Policies are versioned selections. Installing one creates no goods, employees, tax claims, orders or knowledge.

A review follows this order:

1. Recover accepted pending work and receipts before proposing anything again.
2. Obtain the institution's bounded, received information at the review frontier.
3. Identify due actual obligations, unmet modeled needs and relevant goals.
4. Generate feasible candidate methods from qualified action adapters.
5. Check the policy's mandate, voluntary-choice limits, means and information.
6. Apply the selected decision procedure among candidates. If several materially different options remain and no policy covers the choice, retain an unresolved policy decision. Identifier order supplies no preference.
7. Submit typed proposals with their input revision, observations, causal parents and model references.
8. Let Core revalidate and resolve them against the shared world. Update plans from actual receipts, not from intended outcomes.

An actor may act on stale or mistaken information where the policy supports that choice. Core still resolves the actual physical and institutional circumstances. The policy's belief must not overwrite world truth. A review can legitimately choose no action; frequent review does not itself create useful work or elapsed time.

#### 2. Household policy

The household uses actual members and responsibilities, known accessible provisions, commitments, funds and qualified needs models. For a selected horizon, distinguish required provision, already received eligible portions, reserved incoming provision, unconfirmed expected delivery and actual consumption.

Determine an expected deficit only where units, horizon and model are qualified. A forecast is a planning value, not stock and not a debit. A missing pantry report leaves the quantity unknown. A qualified report of no food is different.

For a known deficit, the policy may propose collection of already-owned accessible goods, a permitted purchase, a transfer request, or work under an actual agreement. It must respect its spending limit and any new voluntary decision reserved to the player. A request for help is not receipt of help.

On actual provision, link the delivered portion to its physical stock and permitted consumer. Consumption settles that portion once through the selected physiological model. A workplace meal and a household accounting entry can describe the same portion; they cannot supply two meals. Future delivery does not satisfy current consumption. Care, childcare and housework require real actors, time and shared commitments.

#### 3. Business policy

The business considers actual accepted orders, contracted obligations and explicitly selected inventory targets. A target is a policy objective, not a customer order or revenue. Candidate work identifies qualified workers, available intervals, tools, site capacity, accessible inputs, specification and acceptance requirements.

For each feasible candidate, use the selected ordering procedure: for example, an actual contractual priority or a formally selected deadline policy. Where commitments compete without such a procedure, request allocation rather than using an incidental list order.

Scheduling creates the permitted booking and any properly backed reservations. Production progresses only during actual qualifying work. If a model supplies a rate, its units and operating limits must match the accumulated work. Useful progress is bounded by remaining work, actual duration, worker capability, shared capacity and inputs; adding idle or unqualified workers creates no extra progress.

Debit inputs at their real process stages. Retain partially consumed inputs and unfinished work on interruption. Completion, inspection and acceptance are different events. Only accepted output establishes the product under its physical owner. A transformation must use a qualified conservation/lineage model rather than evade the existing opening-stock invariant by copying a new material total.

Accrue wages, invoices or other claims only under actual agreements and supported useful work or other agreed basis. Payment requires the selected monetary ledger and actual settlement. Booking a shift creates neither wages earned nor cash transferred.

#### 4. Government policy

The government uses actual jurisdiction, institutions, lawful procedures, received reports, administrative capacity and qualified fiscal models. A policy revenue target does not establish a debtor or an amount due.

Assessment requires the applicable authority, period, liable party, tax basis, evidence and amount rule. Retain one assessment identity for that basis and period. A later correction references the earlier assessment and changes the claim under an actual decision; another review cannot charge the same assessment again.

Collection requires an actual due claim and an applicable payment or enforcement procedure. A willing payer's funded payment, a disputed claim and an attempted levy are different actions. Settlement updates the one selected monetary representation and the linked claim once. Recording a receivable never increases treasury cash by itself.

Public spending uses actual appropriations, obligations, funds, procurement and delivery. A budget line does not create services, staff or goods. An appointment or legal decision changes its actual scope; any subsequent physical implementation still needs its own causes.

#### 5. Military policy

The military uses actual command scope, received orders, personnel, known readiness, obligations, supply and route capacity. A roster entry, headcount forecast and physically available soldier are different records. The same soldier remains an actor when also a household member or worker.

Mobilization and recruitment require their selected institutional procedures, actual commitments and any necessary assent. An order does not by itself enlist an unwilling person, create a kit or move a force. Evaluate personnel availability against the shared commitments used by all institutions.

Equipment issue requires the actual received directive, qualified issuer, recipients, material and backed supply. It transfers existing equipment once. Delivery beyond the current site requires real dispatch, transport and receipt rather than a duplicated depot balance. Readiness is derived from supported actual functions and conditions, with unknown requirements visible.

Marches, watches, training, maintenance and operations use ordinary action/work contracts. An instruction to hold a position is not proof that it remains staffed. A negligent or unavailable actor can leave a real gap; outcomes depend on supported agency and conditions. An institutional assessment may remain mistaken until information arrives.

#### 6. Shared-frontier execution and long horizons

With an explicit timeline binding, select the earliest relevant completion, deadline, message arrival, interruption or scheduled review across all institutions. Advance qualified processes only over the unprocessed interval to that boundary. Evaluate simultaneous proposals from the same frontier snapshot and resolve actual dependency conflicts before further continuation.

Long-horizon compression preserves processed spans, useful fractions, people, goods, obligations and material decisions. Coarser display does not authorize another round of production or tax assessment. A threshold or crisis earlier than the requested end stops or splits the interval. Any new voluntary player concession returns for decision.

If a process lacks a duration, needs model, productive rate, authority or causal rule, hold that dependent process explicitly. Other independent qualified processes may continue where the compatibility barrier is safe. Never fill the gap with a second simplified economy or a private military simulation.

#### 7. Integrated implementation fixture

Use an explicitly synthetic world with one shared inventory pool containing four ration units. A household requests two units and a military institution requests three from that same backing at one frontier. Both have actual scoped authority. Without an applicable priority/allocation decision, retain both competing requests unresolved; neither identifier order nor two successful negotiations creates a fifth unit.

In that world, a business with separate qualified inputs and a free worker may perform an independent accepted job; a government may establish a correctly evidenced claim. The business's progress and the government's claim use their actual owners. The claim creates no treasury cash. The household's anticipated transfer creates no consumption. The military's anticipated transfer creates no issued supply.

An authorized later allocation can grant one request or a supported partial arrangement. Record any remaining obligation, revalidate actual backing and transfer only the settled quantities. Consumption, equipment use or transport then require their own applicable causes. A restart retains the requests, decision and actual effects. A delayed report changes only its recipients' knowledge and subsequent decisions; it does not replay the ration transfer.

This fixture supplies the shared-world behaviour to demonstrate under the existing agency acceptance cases. It is not historical calibration or an additional claim of passed tests.



<a id="c2-timeline-and-processes"></a>

## Timeline And Processes


### 3.3.3.E — Timeline and process contract

**Edition:** C2 · 20 October 2026  
**Status:** Proposed engine design for Claude implementation

This contract develops the C1 supplement's time and interruption rules. It uses the same action lifecycle, nine owners, immutable submissions, separately identified attempts/phases and durable receipts. It specifies behaviour to implement and prove; it does not activate a scheduler or adopt numerical rates.

#### 1. Coordinates and precision

Keep these coordinates distinct:

| Coordinate | Meaning |
| --- | --- |
| Storage revision | A confirmed persistent head. Metadata acceptance can change it without physical time passing. |
| Causal sequence | An ordering of committed events and dependencies; the existing Core `clock` belongs here. |
| Elapsed simulation time | Duration on an explicitly selected physical/process axis with declared units and origin. |
| Civil calendar position | A dated representation under a qualified calendar and conversion binding. |
| Information time | Observation, transmission, receipt and understanding coordinates, separately retained. |
| Wall-clock time | Host execution, persistence or worker-lease time; no automatic relation to simulated duration. |

A day-precision opening supplies no exact hour. A time-of-day band supplies a range or qualitative relation, not a universal arithmetic step. A causal event number cannot be converted into minutes by counting actions. Julian-labelled dates require a selected Julian calendar procedure; an implementation must not silently substitute its host calendar library. Other calendars and cross-calendar conversions need their own qualified bindings.

Represent an uncertain time as a bounded range or explicit qualitative relation on a named axis, with endpoint conventions and precision. Unknown bounds remain unknown. A display approximation does not replace the actual stored coordinate or justify ordering events within that approximation.

Routine established capability does not require invented statistics. An ordinary walk may be supported without an agility score or exact speed. Its elapsed-time representation can retain a qualified bound or qualitative relation. A material deadline comparison requires enough timing information; it cannot assume either punctuality or failure from an absent number. Use existing evidence, a supported retained adjudication or an explicitly selected assumption when permitted. Record the assumption and scope; never install a convenient default silently.

#### 2. Required logical records

These records extend existing owners rather than creating another simulation database. Fields can be mapped to compatible existing schemas.

| Record | Required meanings |
| --- | --- |
| TimelineBinding | Campaign/scope, identity and edition, coordinate domain, units, origin relation, calendar/conversion references, precision rules, provenance and adoption scope. |
| TemporalPosition | Named axis, exact coordinate or bounds/qualitative relation, endpoint conventions, precision, source and uncertainty status. |
| TimeAdvanceRequest | Immutable request identity, principal, authorized horizon or stopping condition, timeline reference, allowed processes, spending/choice limits and interruption policy. |
| TimeProcess | Process/phase identity, responsible owner, actual affected records, selected update law and units, prerequisites, operating interval, committed-through position, next boundary, stop conditions and retained partial state. |
| Frontier | Identity, selected head revision, coordinate or uncertainty window, causal parents, due occurrences/proposals, observed dependencies and unresolved ordering/allocation decisions. |
| ProcessedSpan | Campaign and lineage, process/phase, half-open interval `[start,end)`, model edition, actual input/context references, accumulated progress or use, effects and durable receipt. |

Numerical models must declare their units, domain, boundary conditions, numerical method and tolerance where approximate. Preserve fractional useful work and consumption at the required precision; display rounding cannot delete it. A changed model requires an explicit prospective bridge, not reinterpretation of already processed spans.

Information records retain occurrence, observation and receipt separately. Compare coordinates only through a qualified relation. A later report does not cause the reported occurrence again. Formal revocation and the recipient's knowledge of it may have different effective times under the selected institutional procedure.

#### 3. Advancing to a frontier

An authorized advance is a request to continue qualified processes up to a limit, not a guarantee of reaching that limit.

1. Recover the accepted request and existing attempt/phase receipts. Verify current campaign scope, head and continuation authority.
2. Identify active processes and actual commitments in the one world, including due NPC work, transport, information arrivals and institutional reviews. Select only processes with qualified models and timing relations.
3. Find the earliest relevant completion, prerequisite change, threshold, deadline, interruption, message arrival or new voluntary player decision before the requested horizon. Include boundaries produced by coupled processes; domain planners cannot privately advance past them.
4. Determine what interval is justified. If uncertain event ranges overlap and their order materially changes effects, retain an ordering requirement instead of choosing an arbitrary instant. Independent commuting effects may proceed only where that independence and their supported interval are established.
5. Integrate each qualified process over the unprocessed portion up to that boundary, using actual means and conditions. Prepare all coupled effects against a consistent frontier snapshot.
6. Observe authorization, prerequisite and effect accesses. Resolve qualified causal order or allocation; retain unresolved competing proposals. Validate the combined candidate, including conservation, exclusive commitments, capacities and timing.
7. Atomically persist the actual effects, processed spans, outcomes, pending continuations and head change. Then deliver permitted information and presentation from those results.
8. Continue under the same authorized limits, or return control at a material interruption, unsupported dependency or new player decision. Give the actual reached boundary and unresolved remainder; do not label the requested horizon completed when it was not reached.

An unbound process does not prove that the whole world is frozen. Independent qualified processes can continue where their safe frontier is established. Conversely, omitting a relevant unbound process is not permission to assume it had no effect. Apply a conservative dependency barrier where that missing behaviour could change the proposed result.

For simultaneous proposals, identifier order, arrival order and iteration order supply no winner. A supported institutional priority or later authorized decision may establish allocation. A physically established occurrence, such as destruction of reserved stock, is not an optional allocation request that a reservation can veto. Commit its supported actual effects and reconcile backing, claims and interrupted processes through their owners.

#### 4. Work, use and interruption

A reservation or activity booking records future access or commitment. It is not performed labour, consumed food, delivered service, earned wages or manufactured output.

At a process start, validate actual availability and acquire only the permitted commitments or backing. As work occurs, debit inputs at their selected process stages and record actual qualifying progress. Completion, inspection and acceptance remain distinct. Wages or claims accrue only under their actual agreement and basis; a booked interval is not automatically useful work.

An interruption splits the processed interval at its real supported boundary. Preserve completed work, consumed inputs, physical changes, earned claims and remaining fractions. End or release only unperformed portions allowed by the cancellation procedure. Reusable input, consumed input, scrap and unfinished output retain distinct actual identities or quantities. No rollback of past occurrences is implied by changing a process status to `interrupted`.

Continuation uses a new attempt/phase identity linked to the same retained intention where its method and scope remain valid. Recheck current means, authority and timing. A changed method requires a superseding request; an expired window cannot be repaired by rewriting the original payload. Replaying a scheduling receipt cannot create another booking, and replaying a progress receipt cannot earn the same work twice.

#### 5. Consistency across review scales

Half-open processed intervals assign an endpoint to exactly one adjacent span. The same process cannot settle overlapping intervals twice. A coarse advance and a partition into shorter advances must produce equivalent owner state under the same model, inputs, boundaries and retained decisions, within declared approximation tolerance.

When rates or constraints change, split at that cause. Do not apply the final rate retrospectively to the whole interval. Coupled demand, stock depletion, available capacity and process output must agree at each consequential boundary. Two domain summaries cannot both consume or credit the same portion.

Events with zero modeled duration may still have causal order. Process their finite dependency closure without inventing elapsed time. Detect repeated non-progressing states or cycles lacking an independent enabling cause. Retain the diagnostic and unresolved dependent processes; do not drop queued events, advance an arbitrary tick, or invent fuel/capacity to escape the cycle. Legitimately recurring activity requires a model that establishes its next boundary.

#### 6. Recovery, restoration and timeline changes

Retain processed spans, phase identities, decisions and pending boundaries in the same recoverable commit as their effects. A worker lease expires on the host clock; expiry does not advance simulation time or prove the old attempt failed to commit. Apply the C1 receipt, revision and fencing rules before a new worker can settle an interval.

Restoration selects the checkpoint's actual temporal state under a new storage revision. It does not execute intervening time. A pending checkpoint process may have completed on a discarded future head. Its historical receipt proves that old occurrence, not completion in the restored lineage. Invalidate displaced worker claims, then hold or authorize a newly identified continuation under the restoration policy. Preserve lineage links and revalidate the current window; never replay the old effect or falsely mark the restored task complete.

A timeline migration must explicitly map coordinates, precision, pending windows and processed spans, preserve original references and validate supported conversions. If no sound mapping exists, hold affected processes and report incompatibility. Loading a save cannot silently convert its dates, choose an hour, reseed historical events or reset accumulated work.

#### 7. Proposed acceptance cases

All durations, quantities and model selections below are synthetic test fixtures, not historical calibration. These cases have not been executed.

| ID | Before / attempted operation | Required actual result |
| --- | --- | --- |
| TP-01 | Accept an unresolved intention at storage revision 4 | Receipt/head may advance; physical duration and civil date do not. |
| TP-02 | Day-only opening; request an hour-dependent deadline comparison | No invented dawn; retain bounds or the specific unresolved timing requirement. |
| TP-03 | Healthy actor, feasible ordinary path, no agility number | No artificial capability failure or mandatory roll; retain supported movement/time precision. |
| TP-04 | Selected Julian profile; advance from 28 February 1500 by one civil day | Result is 29 February under that binding, not host-Gregorian substitution. |
| TP-05 | A process has no applicable duration model; independent known ledger occurrence is due | Hold its dependent timed effects; do not freeze or falsely complete the independent occurrence. |
| TP-06 | Authorize one hour; a new player concession is needed after twenty minutes | Settle only actual first-span effects and return the concession; do not reach the hour silently. |
| TP-07 | Same work/model advanced once over `[0,10)` or over `[0,4)` then `[4,10)` | Equal supported progress, inputs and claims within declared tolerance; no endpoint duplication. |
| TP-08 | Retry a committed span after response loss | Same receipt; no extra work, consumption, claim or elapsed duration. |
| TP-09 | Productive rate changes at coordinate 4 during `[0,10)` | Integrate separate valid spans; do not apply the later rate to all ten units of time. |
| TP-10 | Future activity is booked, then inspected | One commitment exists; no completed work, output or wages appear. |
| TP-11 | Work consumes one input before interruption, leaving useful unfinished progress | Consumed input and progress persist; only unperformed portions are cancelled or held. |
| TP-12 | Two simultaneous processes request the same exclusive worker | Conflict survives; no duplicate labour or identifier-order winner. |
| TP-13 | Independently established loss destroys reserved backing | Actual loss persists; reconcile reservation/obligation shortfall without replacement stock. |
| TP-14 | Report arrives after the occurrence and a decision deadline | Receipt changes qualified knowledge then; no replay or retroactive informed decision. |
| TP-15 | Overlapping uncertain event windows have order-sensitive effects | No guessed order; retain the material ordering requirement and any safe independent progress. |
| TP-16 | Zero-duration prerequisite cycle has no enabling state | Persist a non-progress diagnostic and hold dependent work; no arbitrary tick or fabricated input. |
| TP-17 | Restore a checkpoint with a task completed only on its discarded future head | Restore saved progress; old receipt stays historical; hold or issue a new authorized continuation without replay. |
| TP-18 | Load a save whose timeline has no qualified conversion to the proposed new axis | Preserve original coordinates and fractions; require explicit migration or hold, with no read-time conversion. |



<a id="c2-movement-and-observation"></a>

## Movement And Observation


### 3.3.3.E — Movement and observation contract

**Edition:** C2 · 20 October 2026  
**Status:** Proposed engine design for Claude implementation; acceptance cases are not executed results.  
**Foundation:** Selected Core 3.3, the Engine Supplement's lifecycle and the C1 action, dependency and persistence contracts.

This contract develops ordinary movement and observation into consequential actions on the shared world. It prescribes no universal speed, perception score, probability or action duration. Existing `CoreWorld.apply`, temporal identities, evidence/receipt records and the R9 observer/frontier are implementation foundations. The movement, spatial and sensory procedures below are extensions to implement and qualify, not claims about existing handlers.

#### 1. Owners and minimum records

K-ACTOR owns an individual's actual position, conditions and availability. K-NET owns route access, operating capacity and actual passage/delivery. K-TIME owns commitments, elapsed-process boundaries and causal order. K-INFO owns observations, claims, search results and receipt. K-ASSET and K-STOCK retain vehicle/object condition, title, custody and contents; movement references them. K-ORG owns relevant mandates, while existing domain owners retain legal decisions. No new map or perception subsystem becomes another world authority.

| Logical record | Required meanings |
| --- | --- |
| SpatialPosition | Actor; place reference; supported local position or relation; precision; effective interval; cause event. Unknown coordinates remain unknown. |
| MovementSelection | Original request/actor; origin constraint; destination or bounded spatial objective; method; path/route basis; companions or conveyance; authorized limits; timing/model references; stop conditions. |
| TransitProcess | Request/phase; departure event; actual route segment or supported transit relation; last settled progress; current restrictions; next boundary; arrival condition; commitments and capacity references. |
| ObservationSelection | Observer; question or phenomenon; method/sense; bounded spatial/content scope; attention and access; time opportunity; selected procedure; retained-result references. |
| ObservationRecord | Observation identity; observer; actual occurrence and collection coordinates; accessible content; method and source lineage; uncertainty/coverage; related evidence; observer receipt reference. |
| SearchResult | Search scope/method; relevant world and observer dependencies; examined coverage; positive findings or qualified absence; unresolved remainder; prior-result/supersession references. |

These are logical meanings, not mandatory database tables. Current-position projections refer to authoritative position history; transit and a displayed map cannot maintain independent copies of where an actor is.

#### 2. Selecting ordinary movement

Interpret the exact declaration into the material objective, method and voluntary limits. “Walk to the nearby doorway” can use an established local relation without invented coordinates or a route-planning questionnaire. Clarify only ambiguities that would materially change the chosen action, exposure, expenditure, authority or destination. Do not silently substitute a distant destination sharing the same name.

Check current existence and control, actual origin, relevant bodily/custody restrictions, route feasibility and any needed access or means. Routine established walking on suitable ground requires neither an agility number nor a success roll. An unmeasured exceptional load, inaccessible boat or unsupported hazardous crossing is a different feasibility problem. Missing incidental detail does not invalidate an otherwise established ordinary capability.

Distinguish physical possibility, legal permission, mandate and the actor's knowledge. A rule requiring institutional authorization must validate it. A physically possible prohibited movement may instead be an attempted breach under a qualified procedure; lack of legal permission does not make a wall appear. Record any genuine player choice before a new unlawful or materially riskier method. Unknown guard behaviour cannot be resolved by assuming automatic passage or automatic capture.

#### 3. Position, transit and completion

A place identifier may represent a settlement, room or other coarse scope. Local movement can keep that identifier while changing an actual supported position, such as “beside the west doorway.” It must record a real positional effect and its cause; deducting stamina and retaining unchanged position is not successful movement. Descriptions cannot invent a surveyed distance or geometry.

A journey outside the current local scope distinguishes departure, transit and arrival. After departure, the actor has one actual transit position or relation, not simultaneous presence at both endpoints. Being aboard a moving vehicle references that actual conveyance and its route; it creates no duplicate vehicle, actor or cargo. Companions remain their own actors with their own control, capability and commitments. One player's instruction does not command an unrelated person to accompany them.

Bind elapsed movement to a selected timing procedure and its actual units, precision and conditions. Coarse or bounded timing is valid where adequate. Temporal completion at supported precision is allowed when that procedure establishes it without choosing among unresolved intervening events. Where a duration range overlaps a material deadline, threat, closure or capacity change, refine the relevant uncertainty or hold that stage; do not invent an exact speed, assign zero time or choose a convenient endpoint. Causal sequence increments are not duration.

`scheduled` means a permitted future journey or commitment exists. `in_progress` requires actual departure. `completed_successfully` requires the stated spatial completion condition. An interrupted journey retains its actual transit position, settled progress, elapsed interval and real costs. Fractions require a selected progress model; otherwise retain a supported segment/position, not a fabricated percentage. A return journey requires its own feasible continuation; cancellation cannot teleport the actor home.

#### 4. Observation and search

Observation reads actual accessible phenomena at the observation opportunity. Check observer presence, relevant sensory capability/condition, attention, obstruction, medium and actual method. Qualitative evidence can establish ordinary visibility or audibility without exact coordinates or numerical ranges. Darkness, distance or concealment matters only through supported applicable circumstances; do not impose an invented universal penalty.

An observation creates a bounded K-INFO record and legitimate receipt for the actual observer. It does not expose every actor, global fact or hidden component in the encompassing place. Other witnesses receive only what their own opportunities support. Store world truth, collected content and interpretation separately. Seeing a uniform may support “a person wearing that uniform,” not identity, loyalty or lawful office. Hearing an announcement establishes received speech, not the truth or legal effect of its contents. Institutional validity requires its actual owner-qualified basis.

An investigation may combine earlier received information, accessible evidence and actual search actions. A question does not grant access to private records or to another NPC's memory. Necessary missing information can yield `awaiting_information`; a missing applicable procedure can yield `awaiting_selected_rule`; an unperformed search is not a negative finding. A completed search can legitimately find nothing within its examined scope without proving universal absence.

Retain the result and dependencies of a completed search. Retrying or redisplaying the same accepted phase reuses its result and receipt; it creates no new generation chance, findings or elapsed work. Deliberately performing another physical search is a new action and uses its actual attention and supported duration even when the finding remains unchanged. Repetition cannot regenerate established stock or silently resample the same retained uncertainty. A genuinely new opportunity, changed object position, different supported method or additional coverage can justify new findings under the selected procedure. Changes to unrelated world records do not invalidate the search automatically. Retained results describe their original observation time; stale knowledge does not silently become current truth.

Where authorized bounded world generation is needed, refine only permitted unestablished detail and retain that choice once. Existing hidden authoritative state takes precedence over generation. Never generate the player's motives, prior voluntary actions or an extra person to satisfy a search. A record saying “unknown” is not a pool of free objects.

#### 5. Dependencies, outcomes and persistence

Instrument selection-sensitive authorization, physical feasibility, observation opportunity and effects together. Actual reads include origin/position, actor restrictions, route state, negative access lookups, shared capacity, selected timing/sensory rules, examined objects and retained search results. Capture predicate scope when a decision depends on “no other occupant” or “no matching object”; observing one returned record alone is insufficient.

At a common frontier, movement can conflict with confinement, doorway closure or allocation of the same passage. Observation can conflict with movement of its target or a change in visibility. Determine actual causal ordering or retain the material conflict; identifier order cannot decide what was seen. A later report of an already committed journey does not reapply movement. Observing an independently established physical occurrence cannot administratively veto that occurrence.

Commit each actual movement stage, observation/receipt, outcome and durable attempt receipt atomically or under the qualified staged protocol. A completed observation phase can leave its parent investigation open. Retry returns that phase's receipt; later coverage uses a new phase/attempt identity. On interruption, save/reload or restoration, preserve the C1 lineage and pending-work reconciliation rules. Presentation receives the actual spatial result and permitted observations after commitment, including unresolved remainder; prose supplies no additional travel or discovery.

#### 6. Proposed acceptance cases

All identities, geometry and conditions below are explicitly selected fixtures. No historical measurements are implied.

| ID | Preconditions and attempted action | Required owner-qualified result |
| --- | --- | --- |
| MO-01 | Healthy controlled actor; nearby accessible doorway; no agility field; walk there | Ordinary movement succeeds without invented score/roll; K-ACTOR records supported local position. |
| MO-02 | Both endpoints share a coarse room ID; move beside the west doorway | Coarse ID may remain; actual positional relation changes once and outcome identifies it. |
| MO-03 | Two distant places have the same label; target is materially ambiguous | Await clarification; no chosen destination, departure or invented expense. |
| MO-04 | Actual accessible route and selected duration; travel between settlements | Departure, single transit presence and later arrival persist; no early destination presence. |
| MO-05 | A material closure falls inside the journey's duration range | Refine timing or hold the affected stage; no convenient endpoint or inferred zero duration. |
| MO-06 | Journey departs, then supported obstruction interrupts it | Preserve actual progress/position, elapsed span and settled costs; arrival remains uncompleted. |
| MO-07 | Cancel an interrupted journey away from origin | Release permitted future commitments; actor stays at actual position until a real continuation moves them. |
| MO-08 | Actor lacks physical access to a required conveyance | Await prerequisite or valid alternative choice; title alone creates no accessible vehicle. |
| MO-09 | Movement and closure/confinement change share a frontier | Actual dependencies conflict; no request-ID passage winner or unexplained escape. |
| MO-10 | Two independent routes and actors; valid movement stages | Equivalent domain effects under either execution order, or an explicitly disclosed conservative barrier. |
| MO-11 | Visible local object; sufficient qualitative scene evidence; no exact coordinates | Observation records accessible content and observer receipt without demanding fictitious geometry. |
| MO-12 | Unmet remote NPC and private inventory exist in the same campaign | Local observation exposes neither private state nor remote location through a global registry view. |
| MO-13 | Observer hears an official-sounding announcement | K-INFO records speaker/content and actual receipt; assertion does not itself establish legal authority or truth. |
| MO-14 | Qualified search examines one cabinet and finds no key | Retain scoped negative result; unopened rooms and unknown compartments remain unresolved. |
| MO-15 | Retry the accepted MO-14 phase, then deliberately request a new physical search under unchanged relevant circumstances | Retry causes no new effects; the new action can use supported time/attention but cannot regenerate stock or automatically resample retained uncertainty. |
| MO-16 | A key is actually placed in that cabinet after MO-14 | New qualified attempt can find it; preserve earlier correct scoped absence and later receipt. |
| MO-17 | Hidden existing stock and authorized bounded generation both apply | Use established hidden stock; generation neither duplicates it nor replaces it because the player is unaware. |
| MO-18 | Crash/retry after a movement or observation phase commits | Recover the same phase receipt and effects once; later phase has a new identity; no extra travel, discovery or receipt. |

Claude must supply actual access traces, ordinary/instrumented parity, relevant same-frontier cases and durable before/after evidence. These 18 cases define required implementation evidence, not a claim that the current engine implements movement or observation.



<a id="c2-dialogue-and-social-actions"></a>

## Dialogue And Social Actions


### 3.3.3.E — Dialogue and social action contract

**Edition:** C2 · 20 October 2026  
**Status:** Proposed engine design for Claude implementation. Selected Core 3.3 remains authoritative. The cases below are requirements, not executed tests.

This contract develops ordinary speaking, questions, NPC responses, persuasion and agreements. It uses the supplement's lifecycle, immutable intentions, separate attempt/phase receipts and persistence rules. Dialogue operates in the same world as work, travel and institutions. It creates no independent social simulation or presentation-owned facts.

#### 1. Distinct events and owners

Keep the following meanings separate:

| Meaning | Authoritative result |
| --- | --- |
| Intention | The speaker's exact declaration and authorized scope are retained. |
| Proposed utterance | Wording or a bounded communicative objective awaits ordinary Core validation. |
| Production | The actor actually speaks, signs, writes or otherwise produces the communication through supported means. |
| Transmission | Sound, gesture, a document or another channel reaches an actual place or recipient under its conditions. |
| Receipt | A particular actor receives the accessible content, possibly only part of it. |
| Comprehension | The recipient understands a supported meaning; receipt alone does not establish this. |
| Response or undertaking | A separate actor makes a decision or commitment within actual capability and authority. |
| Presentation | An authorized account describes those committed events and the viewer's legitimately available information. |

K-ACTOR owns speakers, listeners, relevant capability, location and condition. K-INFO owns assertions, communicated content, source lineage, receipts and beliefs. K-TIME owns sequencing and commitments; K-NET owns an applicable delivery channel and capacity. Identified documents retain K-ASSET/K-STOCK custody. K-ORG, ECO and GOV retain their respective authority, agreement and public-decision records. A transcript references these events; it is not another authoritative history.

`completed_successfully` must identify the phase and completion condition. Successfully asking a question means its qualified utterance and intended receipt occurred; it does not mean an answer was obtained. An unanswered inquiry can have a completed communication phase and an unresolved parent objective.

#### 2. Logical records for implementation

These are semantic requirements, not prescribed database tables or existing handler names.

| Record | Required meanings |
| --- | --- |
| CommunicationSelection | Request/actor; exact supplied words or bounded objective; intended recipients; method/channel; language or sign system; permitted disclosure; duration/attention limits; stop conditions; selected adapter edition. |
| UtteranceOccurrence | Scoped event and attempt/phase identities; actual speaker; produced content; method; supported occurrence interval and precision; causal parents; source references. |
| CommunicationReceipt | Scoped recipient; originating occurrence; received fragments/content references; receipt time/precision; channel; comprehension status and supported meaning; uncertainty and source status. |
| DialogueDecision | Acting NPC and policy edition; received inputs; actual goals/obligations; proposed response or explicit nonresponse; explanation separated from world facts. |
| SocialProposal | Offer/request/promise type; parties; exact terms and conditions; required authority/assent; expiry or unresolved timing; backing references; supersession links. |
| AgreementEvent | Actual assents and their receipt references; qualified terms edition; authority basis; resulting agreement/obligation references; outstanding conditions. |

Preserve exact supplied dialogue separately from an interpretation. If the player says only “ask the guard about work,” a selected procedure may express that bounded inquiry. It cannot add a claimed military service history, promise payment, reveal a secret or accept employment. Material ambiguity requiring such a choice produces `awaiting_clarification`; routine wording needs no needless player interruption.

Ordinary established speech and hearing do not require invented numerical statistics. Speaking, understanding speech, reading, writing and copying are different functions. Literacy does not follow from conversational fluency. Missing a numerical rating is not evidence of muteness or incomprehension; a relevant actual restriction or uncertainty still needs its supported procedure.

#### 3. Production, receipt and answers

Validate the actor's current existence and control, available method, actual audience/channel, attention conflicts and supported conditions inside the observed execution path. Resolve actual production and transmission before recording who heard or understood it. An intended recipient absent from the channel receives nothing. Co-location alone need not imply hearing every word: distance, barriers, noise, attention and method matter where consequential.

Each legitimate listener, including an incidental bystander, receives only the accessible content. A bystander does not inherit the intended recipient's private knowledge. Hearing a claim establishes that the speaker made that claim; it does not establish the claim's truth. Information-time and occurrence-time precision remain explicit.

An NPC response is an ordinary agency proposal based on that NPC's received information, supported memories, goals, obligations and current circumstances. It passes through Core before becoming a spoken occurrence. The NPC can answer, ask a question, refuse, remain silent, defer, give an estimate or make an offer. A missing relevant fact is not permission to invent an authoritative answer.

An NPC can make a mistaken statement or deliberately deceive where its actual selected decision supports that behaviour. Retain assertion, belief, evidence and any private intention separately. An unknown world fact remains unknown even if the statement is confident. Presentation may report the words and supported observable behaviour; it cannot announce hidden sincerity, truth or deception merely because internal validation knows them.

Completed utterances and received answers survive replay without regeneration. A new genuine question can cause a new NPC decision under changed or continuing circumstances, but a repeated query of the same recorded exchange cannot reroll an answer or establish fresh hidden facts. Authorized world refinement follows the retained-generation rules rather than inventing content because a conversation needs it.

#### 4. Persuasion, promises and agreements

Persuasion identifies its actual requested change, interlocutor, arguments, means and applicable qualitative or selected contested procedure. A positive result may establish willingness, an immediate concession or a genuine undertaking within its resolved scope. It does not grant impossible ability, property, legal authority or the recipient's unsupported knowledge. Retain the actual decision and relevant uncertainty instead of converting all social interaction into a universal score.

An NPC's persuasive appeal cannot choose the player's voluntary response. A supported change in what the player character perceives or suffers is different from an invented assent. An authorized player's standing delegation may cover routine decisions only within its recorded scope and limits.

Distinguish an offered term, claimed promise, genuine undertaking, accepted agreement, due obligation and actual fulfilment. A genuine resolved undertaking must not later be relabelled deceptive merely to cancel success. Changed circumstances may prevent fulfilment, producing an actual shortfall and any qualified remedy. Institutional validity remains separate from the parties' beliefs and personal willingness.

When a response offers narrower service, a new price or another voluntary concession, retain those terms and return the new decision to the player. Do not deduct funds or insert acceptance. Once exact terms receive all required genuine assent and authority, a qualified agreement may form immediately; no artificial extra success roll is required. Its future performance, wages, delivery or appointment still need their own causes.

##### Work inquiry trace

The player asks an actual foreman whether work is available. The foreman hears and understands the inquiry. Its policy consults received staffing information and actual hiring authority, then proposes an offer using an existing terms record. Core records that offer, not employment.

The player receives the offer and chooses whether to accept its exact terms. If required assent, authority and conditions are satisfied, Core records the agreement once. A valid future work booking can become `scheduled`; completed labour and wages earned remain unestablished. If the foreman can only seek approval, its genuine undertaking is to request that approval, with the employer's decision still unresolved. Neither path grants rank, equipment or an invented career history.

#### 5. Time, interruption and dependency evidence

Conversation uses actual attention and the selected timeline/communication model. No fixed turn duration, thirty-minute action or unlimited speech within a frozen world is adopted. A coarse occurrence interval may be sufficient; exact ordering remains unresolved when its precision cannot establish which event happened first. Without adequate timing support, do not advance duration-dependent stages or fabricate an exact receipt hour.

While actors converse, independent qualified work, travel, messages and institutional processes continue through the shared scheduler. A meaningful interruption splits the exchange. Preserve words actually produced, fragments actually heard, agreed terms and real elapsed commitments. Cancel only the unperformed remainder; interrupted delivery cannot erase earlier receipt or guarantee receipt of unsent content.

A delayed letter or messenger uses actual production, custody, dispatch, transit and delivery. The intended addressee cannot act on its content before receipt. Reading and understanding are separately supported functions. Delivery cannot execute the requested order automatically.

Observe actual actor/control, audience, channel, capability, attention, mandate, terms and information dependencies together. A conversation can conflict with simultaneous departure, exclusive work, revoked hiring authority or changed offer terms. Retain unresolved allocation or ordering instead of choosing by request ID. Public reasons and projections must omit hidden facts; preserve a detailed internal cause under its legitimate access scope and provide the actor only the consequence or blocker it can know.

#### 6. Proposed acceptance cases

All people, terms and channels below are explicit test fixtures.

| ID | Preconditions and request | Required outcome |
| --- | --- | --- |
| DS-01 | Capable co-present speaker/listener; ask a plain question | Record production, receipt and supported comprehension; no automatic answer. |
| DS-02 | Intended listener is elsewhere; ordinary quiet speech | No remote receipt or invented reply; actual spoken occurrence can remain recorded. |
| DS-03 | Shared spoken language, no established literacy; deliver writing | Delivery does not establish reading or comprehension. |
| DS-04 | Listener hears a confident unsupported claim | Receipt records the claim and speaker; world truth is unchanged. |
| DS-05 | NPC lacks the requested information | Supported uncertainty, refusal or inquiry remains possible; no authoritative invented fact. |
| DS-06 | NPC genuinely believes a false report | Response can express that belief; receipt does not overwrite actual state. |
| DS-07 | Supported NPC decision deliberately deceives | Preserve private intention and public words separately; player view does not reveal deception automatically. |
| DS-08 | Bystander can hear only the final fragment | Record only that fragment and its justified meaning; no complete private transcript. |
| DS-09 | Player requests a work inquiry without specifying wording | Express only the bounded inquiry; no invented biography, payment or acceptance. |
| DS-10 | NPC offers work under actual terms and hiring authority | Record and deliver the offer; no employment, wages or stock yet. |
| DS-11 | Player accepts exact valid offered terms; required assent exists | Form the qualified agreement once; future work stays scheduled or pending. |
| DS-12 | Response requires a new fee or narrower service | Present changed terms for player decision; no automatic debit or assent. |
| DS-13 | NPC agrees genuinely to seek an appointment | Record that undertaking; official approval and meeting remain unresolved. |
| DS-14 | NPC successfully appeals for the player's cooperation | Preserve the appeal and supported effects; voluntary player choice remains open. |
| DS-15 | Departure or interruption occurs during a qualified exchange | Preserve produced/heard fragments and actual commitments; no unsent-content receipt. |
| DS-16 | Letter arrives after a decision deadline | No earlier knowledge or retroactive action; delivery does not execute its request. |
| DS-17 | Offer authority is revoked at the same unresolved frontier | Observe the dependency; do not select convenient ordering or conceal it with an automatic agreement. |
| DS-18 | Reload/retry a committed exchange; narration fails | Return the existing phase receipt; no new utterance, agreement, debit or elapsed-time effect. |

Claude must implement adapter bindings, actual channel/attention models, information projections and the applicable social procedures before claiming these cases pass. This contract supplies no new default historical values, universal persuasion die or active dialogue runtime.



<a id="c2-playable-action-cycle"></a>

## Playable Action Cycle


### 3.3.3.E — Playable action cycle and integrated fixture

**Design edition:** C2 · 20 October 2026  
**Status:** Proposed specification for Claude implementation  
**Purpose:** Connect the separate action contracts into one consequential Solo sequence on a single world.

This document specifies what a supported ordinary first interaction must do. It is not a scripted campaign opening or a claim that the current runtime can perform this sequence. The accompanying `fixtures/PLAYABLE_CYCLE.json` is design data for implementation tests, not executable code.

#### 1. Execution sequence

Use the same request and outcome path for player and NPC actions:

**Declare → Select method → Validate → Reach next causal boundary → Resolve actual effects → Persist → Deliver information → Present → Continue or return a material decision.**

An interpretation proposes a method, target and authorized limits. Routine wording does not require a questionnaire. A materially different destination, expense, risk, concession or commitment returns for a player choice. Unsupported methods remain unresolved with their actual reason.

Each request retains its original intention. Each physical, communication or work phase has a distinct attempt, applicable model and durable receipt. Completed phases can leave a parent objective open. A pending request's replay retrieves its acknowledgement; it does not launch its next phase. A separately authorized continuation uses a new attempt identity and current revision.

Advance only to the next supported boundary. A broad instruction cannot skip a closure, shared-capacity conflict, safety interruption or new voluntary concession. Save management and presentation are not additional phases of simulated labour or travel.

#### 2. Completion and effect boundaries

| Phase | Actual result needed | What it does not establish |
| --- | --- | --- |
| Notice observation | A bounded observation and legitimate receipt of accessible content. | Truth of every statement, a job, or knowledge of hidden people and stock. |
| Movement | Supported departure/transit/arrival or a real local positional change. | Teleportation, automatic companionship, or an invented speed. |
| Question | Actual utterance and the identified receipt/comprehension scope. | A useful answer or a successful negotiation. |
| Offer | Proposed terms actually communicated by the offering party. | Player assent, employment, payment or performed work. |
| Agreement | Qualified actual assents to the same terms, with necessary authority and conditions. | Completed duties, an earned balance or a wider institutional mandate. |
| Work booking | Real actor/site commitment and permitted backing. | Useful progress, consumed inputs, output or wages. |
| Work milestone | Actual useful work and its supported physical/input effects. | Unperformed remainder or automatic acceptance. |
| Interruption | Settled earlier effects, stopped future portions and an explicit continuation requirement. | Erasure of progress, automatic return home or silent assent to new terms. |
| Acceptance and settlement | Actual acceptance, claim basis and funded payment through their respective owners. | Duplicate output, a second monetary balance or a retrospective replay of work. |

The current Core operations are implementation references. New spatial, communication, timing and staged-work adapters are required for this full sequence. Do not substitute generic stamina deductions, scene descriptions or a `resolved` label for these effects.

#### 3. Synthetic fixture and selected parameters

Every person, location, quantity, duration and procedure here is an explicit test-fixture selection. None is a historical assertion or a default for ordinary IRGS campaigns.

| Component | Fixture selection |
| --- | --- |
| Timeline | Elapsed minutes from synthetic origin `T=0`; civil-calendar conversion remains unbound. |
| Places | Yard, Stores, a traversable path between them, and one sorting bay within Stores. |
| Actors | Controlled person P; foreman F; worker W. Each is one actual actor in the shared world. F has the separately established capability to inspect this parcel task. |
| Capability | P has established ordinary walking, hearing, speech and reading of the posted language. These are separately selected qualitative functions, not numeric ratings or a template gift to real characters. |
| Information | P initially knows only the permitted local scene. F has actually received the hiring, safety, inspection/acceptance, scoped payment and capacity-allocation mandates and relevant work reports. W's job and availability are actual records. |
| Goods and funds | Four workshop-owned parcels on shelf A, none on shelf B. Workshop cash three units; P cash zero. F has actual access to the workshop funds and authority to settle this accepted task up to three units. Title/custody remain explicit; no second cash representation is added. |
| Public notice | Accessible text says that work inquiries can be made at Stores. Its observation supplies that assertion, not a guarantee of work. |
| Work terms | Relocate the four parcels from A to B; three cash units become due only after all four are relocated and accepted. No partial wage is owed under this particular fixture agreement. |
| Work model | One parcel milestone per qualifying minute; input parcel is relocated, not consumed or manufactured. Shared bay capacity is one worker. |
| Allocation | F has a selected earliest-due-task procedure at allocation reviews T=8, T=11 and T=15. P's accepted job is due at T=14. W's qualified task needs four contiguous bay minutes and is due at T=20. W requests once and waits for allocation after deferral; no policy automatically starts W between reviews. Equal deadlines would require an additional qualified decision; identifiers are not a tie-breaker. |
| Interruption | The accepted work scope includes a stop-on-safety-signal condition. A real signal reaches the bay at T=10 and closes the bay to both workers for [10,11). A qualified clearance is received at T=11. Continuation requires a player decision. |
| Decision pause | Simulation pauses at material player decisions. New bounded advance/continuation requests resume it. Host-clock delay while a decision is pending changes no expected fixture time. |

The fixture selects observation duration one minute, path duration four minutes, and separate question, offer and acceptance communication phases of one minute each. Completion inspection and cash handover each use one minute. These values exist only to make the fixture's expected boundaries explicit.

#### 4. Required trace

| Boundary/span | Cause and required shared-world result |
| --- | --- |
| T=0 setup | P exists under actual control before play. No work agreement, earned pay or private foreman knowledge is granted. |
| [0,1) | P deliberately reads the accessible notice. At T=1 its content and source are received. The notice's claim remains distinct from institutional truth. |
| [1,5) | P walks to Stores using the selected route. Actual presence moves from origin to transit and then destination. A save at T=3 records transit, not arrival or a second person. |
| [5,6) | P asks the person at the work counter about available work. F actually receives the question. The player's knowledge is limited to observable introduction and received speech. |
| [6,7) | F's qualified policy offers the recorded parcel-work terms. P receives the offer. Cash and employment remain unchanged. |
| [7,8) | P expressly accepts those exact terms. Qualified agreement forms. It permits this task, not general access to workshop property or command over W. |
| T=8 frontier | P and W request the same sorting bay. The engine first detects contention. F's actual authorized allocation decision applies the selected deadline procedure to book P for [8,12); W remains unfulfilled. No array ordering selects P. |
| [8,10) | P performs two actual parcel milestones. A has two parcels and B has two; total remains four. The bay and P's attention are committed. No pay is due yet. |
| T=10 interruption | Settle valid work over the preceding half-open span and the newly effective stop condition in one qualified boundary transaction. No third parcel starts. Preserve two units of useful work and all physical relocations. Release the unperformed booking [10,12); actual bay closure prevents either worker starting during [10,11). Return the continuation decision. |
| [10,11) | In this trace, P chooses a bounded wait. F's actual safety process produces the clearance and P receives it at T=11. Receipt alone does not choose to resume. |
| [11,13) | P chooses a new continuation attempt under unchanged task terms. Revalidate clearance, P, the bay and backing. At the T=11 allocation review, W has not begun or obtained a booking; the selected deadline policy grants P a new [11,13) booking. Complete the remaining two parcel milestones. A has zero, B four. W's unfulfilled task remains pending for the T=15 review. No running W task is preempted or erased. |
| [13,14) | F performs qualified completion inspection and accepts the actual work. The agreement's three-unit claim becomes due once. Physical cash remains with the workshop. |
| [14,15) | A funded, authorized cash handover settles the claim. Workshop cash becomes zero, P cash three, and the same claim is settled. No additional wage award occurs because the story is displayed. |

The T=10 ordering is part of this explicitly selected process model: the valid `[8,10)` span is settled jointly with the stop condition effective at its boundary. It is not a general permission to order simultaneous operations by identifier. An uncertain signal interval overlapping a parcel's milestone would require a qualified joint resolution or an unresolved ordering case.

F's actual schedule supports the stated exchanges, safety communication, inspection and payment without an exclusive-attention overlap. Allocation decisions use the selected review procedure; required communications are actual supported receipts, not changes granted by reading a result panel. P's work request authorizes flexible booking within its accepted task window, so a new valid phase can use [11,13) without rewriting the original declaration. W's remaining task is preserved; the fixture ends at T=15 before executing its next allocation review.

The initial work horizon is interrupted at T=10. It cannot report that T=15 was reached. The later bounded wait, continuation, inspection and settlement require their own authorized stages. A player-decision pause follows the selected time-control policy; time spent looking at the interface does not simulate a wait.

#### 5. Observable and private outcomes

Core retains the actual parcels, work, mandate and payment records. P receives only the notice, its journey/observable circumstances, actual exchange, safety messages and applicable work/payment information. W's private thoughts, F's hidden reports and unrelated inventory are not automatically exposed.

Detailed internal reasons may identify hidden prerequisites. The player projection must not turn them into free information. An unauthorized proposal is retained internally with its appropriate status; the public explanation reports only what the character can know or what an out-of-world service must communicate without revealing hidden facts.

Each presented scene references committed phase effects and permitted information. A failed narrator can be retried from those references. It cannot produce another utterance, parcel movement, payment or time advance. A late report of payment creates receipt then; it does not transfer cash again.

#### 6. Proposed integrated acceptance cases

| ID | Setup or action | Required assertion |
| --- | --- | --- |
| IC-01 | Initialize the fixture before play | One controlled P; no invented past work, agreement, earnings or private knowledge. |
| IC-02 | Read the notice | Exactly one qualified observation/receipt; no automatic job or global fact disclosure. |
| IC-03 | Save/reload at T=3 during movement | P remains one actor in transit; resume retains the original journey's progress and arrival condition. |
| IC-04 | Ask F about work at Stores | Real question receipt precedes the response; successful asking does not imply useful employment. |
| IC-05 | F offers the valid terms | Offer is recorded and received; no acceptance, cash change or work begins. |
| IC-06 | P accepts the exact terms | One qualified agreement and scoped task permission; no output, earned claim or wider authority. |
| IC-07 | P and W contend for the bay | Conflict is observed before a recorded authorized allocation using due times; changing IDs changes no outcome. |
| IC-08 | Safety stop at T=10 | A=2, B=2, progress=2 of 4; no third parcel, payment, erased work or automatic continuation. |
| IC-09 | Clearance arrives, then P chooses continuation | Receipt does not resume by itself; the new attempt revalidates and settles only the remaining two parcels. |
| IC-10 | Completion, inspection and payment | Work complete before acceptance; due claim before payment; final cash totals conserved at three and parcel total at four. |
| IC-11 | Retry any committed phase or lose its presentation | Same historical phase receipt; no duplicate speech, work, claim, payment or elapsed span. |
| IC-12 | Request coarse advance instead of short reviews | Preserve T=8 contention, T=10 stop, later player choices and the same actual effects; no coarse-step bypass. |

These twelve cases supplement the separate movement, dialogue, time and foundation cases. Passing the integrated fixture would demonstrate these selected mechanisms, not general employment, historical calibration or a complete Living Day.
