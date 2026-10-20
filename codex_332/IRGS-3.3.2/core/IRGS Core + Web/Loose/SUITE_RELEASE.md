# IRGS Core 3.3 local release

Core 3.3 is the selected runtime for this local suite. Its six genre bindings are Military, Roman Republic, Fantasy, Post-Apocalyptic, Shinobi Nexus and Space. Eight technical content libraries and seven legacy profile registrations remain installed. Ordinary player discovery lists **The Hundred Years’ War** only; technical registration does not make an engine, library or legacy profile a separate playable campaign.

A Scot’s Tale is a named 1415 starting reference. Its reusable mechanics belong to shared Core/genre handlers, and its preserved adapter, library and profile remain compatibility/archive material. It is not maintained as a separate ongoing campaign or engine. Its new-start reference remains unavailable until its civil date and checkpoint are verified; the generic 11 August opening is not imposed on it.

This selection follows the user’s direction to deliver a live 3.3 version, then the expanded Core + genre engines + content libraries scope. Historical 3.2 source files and the R7/R8/R9 research packages remain preserved. Their embedded instructions are reference content, not permission to change saves or activate every proposed numerical model.

## Start and use

Double-click `Start-IRGS-3.3.cmd` whenever you want to play. It verifies the installed release, starts the local website in the background if needed, and opens **http://127.0.0.1:8765** in your default browser. You can close the launcher window; the host keeps running. Repeating the shortcut reuses an existing IRGS host instead of starting another. The `IRGS_Web/Start-IRGS.cmd` shortcut delegates to the same launcher. No new release is needed to open the website again.

If another application occupies the port, the launcher shows a readable error and leaves that application running. Startup records and logs are kept in `IRGS_3_3/live/`, outside the release payload and campaign saves. For a check without opening the browser, run `Start-IRGS-3.3.ps1 -NoBrowser`; `-Port` selects an explicit alternative port. The adjacent `IRGS_Web` directory must remain beside `IRGS_3_3`.

The website opens in Solo Gameplay, with Story, World and Chronicle views over the selected character's server-filtered information. Character, inventory, relationships, institutions and other inspection panels show available records; inspection does not advance the world. Reading preferences affect only this device.

**New campaign** follows Content Library → The Hundred Years’ War → Starting point → Character → Review → Start. The clicked entry ID and exact preview hash carry into review; stale or mismatched choices fail rather than falling back to another date or profile. Choose a named new character or an existing person made eligible by the selected scenario, then review that person's control scope. No campaign file is written before the final selection succeeds. Cancel and Back leave no saved game. Other installed profiles remain available through authorized Creator tooling and existing-save compatibility.

Optional structured identity, life-path and career fields preserve the creating player's testimony and its explicit receipt. Origin, nationality, control and career remain independent; no faction is mandatory. A named organization must exist in the dated starting world. Claimed current employment or an offer remains a claim: these fields create no contract, relatives, household wealth, competence, possessions, authority or accepted service. This is structured background capture, not a completed Life-Path or employment simulation.

To remove an accidental campaign or branch, select it and choose **Delete campaign**, then **Move to Trash**. It disappears from the active list. **Campaign Trash** provides **Restore**, retaining the complete original save byte for byte. Deletion checks the displayed revision and rejects stale requests; restoration refuses to overwrite an active campaign with the same ID. Branches are separate saves, so removing a branch leaves its original campaign intact. The website does not permanently erase trashed saves.

## Solo Gameplay and Creator workspace

Player requests receive only the controlled character's current record, explicitly received evidence and orders, known identities, and supported commitments. Current stock quantities require explicit inventory-inspection rights; a location name or a claimed possession does not grant access. Global scene notes, other actors' private current records, unreceived evidence, unresolved engine payloads, source policies and full historical snapshots are excluded from player responses. A known identity does not reveal that person's private state.

Submitting a declaration preserves the exact player text through Core `record_player_action`. Its result is `declared_not_resolved`: no outcome, reaction, cost, elapsed time or narrative is invented. One unresolved gameplay declaration per character is allowed. **Withdraw pending attempt** retains the original Core record and changes only the request's withdrawal metadata, permitting a revised declaration. A character who no longer exists at the committed world date retains their selected identity and history; new declarations are refused and no successor is chosen automatically.

The player routes are session-protected `/api/playthrough/{id}`, `/api/availability/{id}`, `/api/chronicle/{id}`, `/api/declaration`, `/api/withdraw-declaration` and `/api/action-result/{campaign}/{request_id}`. Declaration and withdrawal request identities and exact payload digests persist with the same save. A repeated request recovers the original acknowledgement before checking a stale revision; altered payloads are rejected. Result retrieval recovers a lost response. Campaign and actor checks prevent inherited branch receipts from being replayed as the branch's own action.

The final creation review also uses a stable request identity and exact choice digest. Repeating an accepted creation returns the existing campaign, even if the opening source subsequently changes; it cannot create a second game or silently change the chosen character. A retry for a game now in Trash reports that status without restoring it. Creation and declaration acknowledgements follow the atomic save write.

**Creator workspace** is an explicit opt-in for this local campaign owner. It exposes source lookup, raw inspection and supported event/frontier/mandate/decision tools. Raw `/api/campaign/{id}` and `/api/binding/{id}` require `mode=creator` plus the session token; legacy editing and branch routes likewise require explicit Creator mode and the token. The default player frontend does not fetch raw saves. This is an owner-controlled local workspace with a separate inspection capability, not a multi-account authentication service. Creator tools still use the same authoritative world and Core validation.

The centralized feature tree contains 131 development nodes: 81 in the player projection and 131 in the explicit local-owner Creator projection. Planned or deferred routes are descriptions, not enabled mechanics. The server filters navigation metadata by scope and independently protects underlying data routes; a development-stage query grants no Creator rights. Historical baseline and plan inspection require Creator mode and the session token. This does not establish hosted multi-account authorization.

## Hundred Years’ War historical setting

In **New campaign**, choose **The Hundred Years’ War**. This setting uses the existing Military profile and library. Ten principal years lead to the full catalogue of **37** supplied entries: 12 Edwardian, 14 Caroline/interwar and 11 Lancastrian. The original closing claim of 35 was a counting error; no rows were discarded. Entries retain their proposed status until a dated opening has been developed and checked.

**1415 — The Lancastrian Invasion** is the first developed opening; the other **36** entries remain proposed. Its authored cutoff is **11 August 1415, Julian calendar, before the recorded departure**; the hour is unspecified. The preview provides sourced political, military, territorial and diplomatic context and a practical entry guide. The dated setup contains five historical people and five political entities. The authored Solo scenario permits choosing one of those five individuals or creating a new character. Existing political entities are not selectable national commands in this individual scenario. Operational quantities such as actual deployable troops, ready ships, provisions and balances remain unknown where evidence has not established them.

An explicit creation request identifies the entry, exact snapshot hash, reviewed availability digest and selected character. Inspection and cancellation create no campaign. Creation copies the opening into a new campaign scope and records the explicit player setup before its first save. Optional background testimony receives its own actual setup receipt. These causal setup records advance no elapsed world time and schedule no historical outcome. Other catalogue dates can be inspected but cannot create a substitute 1415 world. A custom year without a matching developed snapshot is unavailable; a nearby date is never substituted.

The opening reference is preserved separately from current scene presentation and the event journal. It records historical setup, not automatically received character knowledge. It remains an opening reference after later campaign changes. Existing AST saves retain their own post-Day-2 checkpoint and are not redated or merged with this setting.

Opening presentation uses the same actor-filtered projection as ordinary player reads. It supplies no political setup fact as automatically known news, no future historical knowledge and no invented nearby actor or scene. Unknown location remains unknown. This saved presentation metadata is not a consequential Core event or an NPC interaction, and it does not override later current-scene records. Declaration and withdrawal presentation remains distinct from resolved action status.

## Conditional historical reference assessment

The revised design requests a conditional historical default: recorded events are intended expectations only while their causes remain supported. That is the integration target, not an implemented automatic scheduler. The current generic `historical_plans` module assesses three researched 1415 references: Harfleur negotiations on 18 September, its handover on 22 September and Agincourt on 25 October. Source-backed dates/outcomes are separated from explicitly authored causal inferences and exact live-record bindings. The disputed landing and siege-start dates are outside this baseline.

New historical worlds save a pinned copy/hash of this prospective reference edition. Forks rebind its campaign scope and retain source provenance and existing terminal plan states. Existing saves acquire no automatic new metadata or historical migration; an unpinned campaign can receive a read-only preview. Historical reference outcomes are never matched to journal entries by guesswork, and a past reference is never replayed as a new occurrence.

Assessments distinguish satisfied, unsatisfied and unknown conditions. Missing/null resources, authority or other bindings cannot establish an intact pathway. A dead or dissolved required identity blocks that exact configuration; supporting changes mark risk, and dependency reevaluation remains local to connected descendants. Prevented, superseded and expired plans do not reactivate merely because conditions improve or a historical date arrives. Every report keeps execution unavailable; no calendar advancement, baseline victory, casualties, actor resurrection, successor selection or world effect is applied. Prospective references remain Creator-only material, not character knowledge.

The supplied gameplay-screen and epoch-memory documents remain archived design references. Their illustrative dialogue is not a recorded scene. Solo Gameplay, filtered Story/World/Chronicle views, the starting review and scoped history retrieval are implemented within the limits described here. Automatic narration, outcome resolution, calendar advancement and a durable epoch-summary service remain unavailable.

The local website records declarations and supported state changes. It does not run a general AI narrator or fabricate unsupported combat, medical, learning or historical outcomes. Those procedures use the supplied genre rules and whatever complete, supported parameters the campaign actually selects.

## Runtime structure

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

## Dependency and transaction guarantees

The observer follows the complete selected dispatch chain, including physical-loss reconciliation, tracked work and fabrication in the supported research profiles. Reads include missing-record lookups, enumeration/phantom dependencies, source profile choices, commitments, receipts, authority and actual scarce resources. Writes include recorded intents and an actual state-difference backstop. Transaction clones retain their observer. Whole-list reads are conservatively treated as potential writes outside constructors/validation; broad invariant reads are retained separately and checked against the assembled candidate.

Each certificate identifies the event, pre-state hash, code hash, backend/profile, observed reads, writes and post-state hash. Every commit attempt observes afresh. Read/read overlap is permitted; write/read and write/write overlap preserve conflicting proposals without choosing an ID winner. Unknown or invalid operations cannot acquire independence by omission. Qualified physical losses remain actual occurrences: compatible measured losses commit, while causally conflicting work remains unexecuted. Incompatible combined loss measurements reject the frontier atomically.

Submitted nested parameters are detached from the caller. Journal signatures are verified. Same ID/same payload replays without effects; changed-payload replay fails. WIP loss replay does not repeat its reconciliation. New campaigns and explicit branches have distinct scopes; legacy saves retain their existing scope and bytes on read.

This is instrumentation of reviewed deterministic JSON-state Python. It is not a security sandbox for hostile plugins, external side effects, hidden globals or arbitrary C-level reads. Observed executions and interleaving checks are evidence for their named scope; they do not prove every reachable branch or every native genre procedure.

## Durable decisions

Simultaneous requests retain original payloads, digests, dependency edges and reasons in the campaign state. Mandates name an actual actor, source and operation scope. A genuinely later decision revalidates current resources, executes once or denies without applying the request. Occurrence evidence and player actions cannot be turned into delayed automatic approvals. A denial-only right can close an unqualified request without granting permission to execute it.

The host exposes submission, mandate and resolution routes under one lock and persisted revision. Single invalid events return an error without a save revision; batch submissions retain unresolved intent. Offline CLI changes write a new output file, preventing the older stale-memory overwrite pattern. Complete workflow state is preserved by save/reload; replay of only the older domain journal does not reconstruct every workflow metadata action.

## Strategic execution

Four bounded planners—household, business, government and military—receive detached projections of only selected, received observations. Their operation rights and subject scopes constrain proposals. Unknown information withholds a plan; actual shared handlers revalidate its consequences. Source selections, read paths, proposal decisions and changes of rights remain in the same world ledger.

The provided subscriptions, rates and rights are explicit synthetic verification inputs. They can advance a multi-institution verification scenario over days without a prewritten event list. They are not a general historical NPC planner, a live-game calendar binding, or adopted historical economic rates.

## Chronicle and epoch planning

Chronicle search and pagination operate only on records already filtered for the campaign, selected character and access scope. Personal history, biographies, relationships, institutions, timeline and archive are views of those supplied records. Missing sources stay missing; retrieval does not reconstruct dialogue or turn historical setup into personal memory. Read requests do not write sidecars, summaries or campaign state.

The history module also provides an interval planner for an explicitly supplied number of complete campaign-relative years. It partitions closed coverage without gaps or overlaps into annual, five-year, twenty-five-year, cumulative-century and separate sealed 500-year epoch ranges, leaving the current incomplete year outside closed coverage. It returns a coverage plan, not generated or published prose. Numeric word allowances require an explicit budget policy; none is silently selected. The website does not infer closed years, an adopted calendar consolidation origin or elapsed years from causal records. No durable summaries, automatic consolidation, narrator or time-advance service is activated.

## Preserved AST reference and compatibility

The archived audited v2 registry preserves 37 identities: 36 humans and **Abel**, one horse. “Able” was accidental and remains an archival alias. Its source status and provisional ratings remain unchanged. Archive preservation does not create a separately maintained AST engine or promise an ongoing campaign update.

The preserved personal checkpoint is post-Day-2, with no verified civil date for a new HYW initializer. It must not be silently replaced by a recruitment-yard scene or the generic historical cutoff. Existing saved records and compatibility access remain intact; reusable procedures continue through shared Core and genre owners.

## Genre and content limits

All six receiving bindings pin inspected source bytes to Core 3.3 without rewriting the older specifications. Complete source content is bundled, including selected and held SCL material. Lookup preserves statuses. Shinobi’s native resolution/resources, Fantasy’s effect profiles, Roman local legal/calibration choices, historical/Fantasy learning units and Space flight/life-support models remain distinct. No universal conversion or missing numerical default is invented.

The catalogue’s hold summary records 228 held SCL families, proposed genre templates and blocked legacy Shinobi records. A missing historical `RELEASE_BINDING_R3.json` is recorded as unverified historical deployment evidence; it was not reconstructed. Fresh hashes prove which local source bytes are actually bundled.

## Verification and packaging

The current completion audit and exact counts are in `results/completion_audit.json`, with runtime, HTTP, certification and strategic evidence alongside it. The current integration account is [DESIGN_INTEGRATION_2026_10_20.md](DESIGN_INTEGRATION_2026_10_20.md). Test results apply to their recorded code identity and scope; uploaded patch-audit counts are not evidence for an altered live tree. The catalogue/source manifest verifies bundled sources and receiving payloads. Release startup verifies runtime, data, source and host hashes. Existing-save preservation reports and distribution verification remain separate evidence.

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
