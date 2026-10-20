# A Scot’s Tale: Become a Legend
# Features and Mechanics Engine Specification

**Document:** AST-ENGINE@0.5 · **Date:** 17 October 2026  
**Edition:** 0.5, ChatGPT continuity integration; inherited rules retain their individual recorded status.
**Status:** Complete continuity-enabled reference edition. The user-requested recording procedure is specified in E12; inherited established rules and other proposals retain their recorded statuses. No gameplay advancement, world-state migration, numerical calibration or live playtest is performed by this document.

**Companions:** [Content Library](AST_Content_Library_v0_5.md) · [Art Direction](AST_Art_Direction_v0_5.md).

## Current ChatGPT continuity selection — edition 0.5

Use [IRGS ChatGPT Play Continuity Adapter 1.0](IRGS_ChatGPT_Play_Continuity_Adapter_v1_0.md) for recording during play and source-backed recaps. Core 3.2 maintenance R3 and SCL 1.0 remain unchanged. New recording behavior is prospective; it creates no past events or current-state migration. Prior review receipts below describe their original editions, not the fresh 0.5 validation.

## Current reference and correction status — v0.4

The running game remains authoritative for current state. The user has now supplied **29 character concept boards** (S12) and identified a separate **current but somewhat inaccurate Coopian shield image** (S13). These are available visual references, not automatic approval of every caption, scene or accidental detail. The original user photographs, separate sire/mare references and complete founding/inscription text remain unavailable in this task. The source v0.4 receipt reports overview inspection of all 29 boards and individual inspection of Ian, Abel and Martin Cooper. R1 rechecks their source bytes and reference mappings; it does not repeat image QA or transcribe every caption.

**Latest explicit correction (S14):** the shield uses **two traditional shield arm straps plus one smaller strap connecting to the over-bracer harness**. The smaller connection is intended to improve control while not gripping the handle. Its clasp is intended to release quickly so the shield can be discarded if another person takes control of it. This supersedes the earlier reading of three matching full-length harness straps. The correction does not specify all anchor positions, exact dimensions, the complete release linkage or a guaranteed release time under load. Keep uncorrected design requirements, including five front steel bands, direct-painted heraldry, relief cuts and wearer-relative handle position.

## Use alongside the running game

This is a project reference for the **ongoing game**, not a restart, handoff or replacement save. The game chat retains its current clock, inventory, injuries, relationships, orders, knowledge and open player decisions. No current save was inspected in this revision. May 1415 bench details are historical examples only; do not load them over later events.

The user's supplied art consolidation (S11) supersedes earlier “unknown” statements within its stated scope. It reports approved designs and references; the actual images, photographs and complete inscription text were not attached at v0.3; S12/S13 now supply concept boards and the current shield draft, while original photographs and complete inscription text remain unavailable. Their absence does not revoke approval. Preserve the supplied specifications, and retrieve the actual references before claiming an exact visual match. New procedures and optional aesthetic suggestions remain Proposed; established designs do not automatically become built, owned, tested or mechanically effective equipment.

## E1. Purpose, scope and authority

Support the ongoing grounded historical life and military-service campaign. The recovered May 1415 handoff supplies rule evidence, not a mandatory starting point. Support ordinary work, relationships, travel, service, war, captivity, retirement and generational continuity. “Become a Legend” expresses an opportunity; it guarantees neither fame nor survival, knighthood, battle participation or escalating enemies.

This file owns AST procedure selections and campaign overrides. The Library owns content definitions and a **read-only historical snapshot**. The running game’s Campaign State owns actual current quantities and events. Art owns presentation choices only. None is an alternative inventory or clock.

Authority: current explicit user direction/correction → established campaign rule/override → relevant adopted genre foundation → adopted Core → named temporary proposal in an unresolved gap. Newer publication is not adoption. The proposed dependency chain is **IRGS Core 3.2 → military/historical life application → AST 1415 setting → AST campaign profile → actual saved state**. Do not import another campaign’s lore.

Status vocabulary:

| Label | Meaning here |
|---|---|
| Established—recovered | Explicit AST rule/fact preserved in source S1; original chronicle not available for direct verification |
| Campaign precedent | A resolved example, not a general bonus or universal procedure |
| Core provider | Identified Core 3.2 shared procedure; prospective AST binding, subject to overrides |
| Genre-owned | Military/historical application; not universal setting lore |
| Proposed | New organization, binding, procedure or content awaiting adoption |
| Accepted | Requires an explicit decision naming scope and version; not inferred from this delivery |
| Playtested / Calibrated | Require separately recorded live-play / parameter evidence; neither claimed here |

## E2. Dependencies and receiving contract

Pin `IRGS-CORE-3.2` maintenance R3, `IRGS-SCL-1.0`, and source `IRGS-MLS-SLIM-1.2` with `IRGS-BIND-MILITARY-3.2`. These are the proposed receiving references, not a statement that the existing campaign already migrated. Core’s HISTORICAL provider is a compatibility reference; it does not activate H-0.3 human numbers. The generic MILITARY binding still names ML-0.1 classification metadata; the military 1.2 receiving edition introduces proposed MIL-LIB-1.0 references. Use the latter as a catalogue candidate only, not an unrecorded rewrite of the generic binding.

The selected parent text is bundled at [Core 3.2, maintenance R3](dependencies/Core/IRGS_Core_Engine_v3_2.md), alongside [SCL 1.0](dependencies/Core/IRGS_Shared_Content_Library_v1_0.md), its complete registry/native payloads and the selected Military 1.2 specification. [AST_Receiving_Binding_v0_5.json](AST_Receiving_Binding_v0_5.json) pins the exact selected bytes. The original R2 archive remains historical provenance only; it is not the receiving parent. These three AST documents remain separate extension specifications. Packaging does not select missing numerical models, adopt proposed Military/AST procedures or migrate the running game.

| Function | Core 3.2 provider | Authoritative owner / AST use |
|---|---|---|
| Authority, evidence, agency, actions | §§1–9, 79, 82, 90 | K-INFO evidence; K-ACTOR actors; AST-R01 override below |
| Time, concurrency, event commit | §§10–12, 47, 85, 90–91 | K-TIME; one event frontier and journal |
| Capability, injury, exertion, development | §§14–19, 31, 41, 45 | K-ACTOR conditions and competence; K-WORK actual practice |
| Items, ammunition, repairs | §§20–23, 53–55, 105 | K-ASSET condition/custody; K-STOCK consumables; K-WORK repair |
| Money, supplies, claims | §§24, 35–38, 109, 114 | K-STOCK actual holdings; ECO obligations, not a second purse |
| Institutions, service, orders | §§25–46, 107, 110, 113 | K-ORG; linked service/authority records |
| Communication and reputation | §§30, 60–61, 66, 85–86 | K-INFO source, interpretation and receipt; K-ACTOR relationships |
| Life, households, death, succession | §§64–76, 106, 122 | K-ACTOR, K-ORG, K-POP; no cloned heirs or population |
| Routes, work and services | §§73, 101–108 | K-NET links, K-WORK progress, existing stock/assets |
| Content, composition, adoption | §§88, 97–99, 111–112 | Exact definitions and explicit prospective mappings |
| Trials and examinations | §123 COMP | COMP rules/results; actual performance uses its activity procedure |

AST extension records add references and decisions to these owners. They do not create new shared owners. All eleven Core development domains resolve explicitly to §§113-123: GOV 113, ECO 114, INV 115, MAR 116, CIV 117, MED 118, WILD 119, INTEL 120, URBAN 121, LIFE 122, COMP 123. The receiving binding retains §116 for Maritime; it enables no naval model by itself. AST does not require every domain to run every day.

### Selected and unselected models

| Cause | AST selection in this candidate | Boundary |
|---|---|---|
| Consequential uncertainty | AST-R01 recovered d100 bands | No automatic adoption of Core competence ladder, opposed formula or roll-twice system |
| Human/horse function | Supported descriptive capability and persistent conditions | No HP, stamina pool, recovery timer or diagnosis invented |
| Injury/effect/protection | Actual method, contact, protection and supported consequence | Outcome-changing gaps require a bounded ruling or later adopted complete profile |
| Service | AST established terms; E5 proposed workflow for unsettled terms | No default wage, lodging, enrollment or authority |
| Learning | Evidence, real instruction/practice, actual time | No XP, level, 4-hour TU or 20-hour TU selected |
| Travel/needs/load | Actual route, means and support; unknown rates remain unknown | No default pace, forage/ration amount or capacity |
| Extraordinary effects | None enabled | No magic, death loop, supernatural healing or imported power system |

Do not call unrestricted tactical combat or quantitative logistics calibrated or fully executable while their material models are unresolved. Supported conversation, observation, ordinary inspection and duty decisions remain possible.

## E3. Campaign profile and overrides

`AST-1415` is a proposed project identifier, not a replacement for any existing game identifier. This engine records the feature profile; it selects no live cutover time. Library L3–L7 preserve historical evidence, while L11 records the newly supplied identity/design constraints. Read the running game’s actual state for play; do not initialize it from these files.

**AST-R01—Established, recovered resolution.** For a feasible, uncertain action whose failure matters: `total = d100 + applicable situational modifiers`; 60+ Success, 30–59 Mixed, ≤29 Failure. A uniform integer 1–100 is the mathematical interpretation used in the source’s probability table. Qualified routine work succeeds without compulsory dice, consuming actual time and resources. The GM rolls automatically for a required check, displays it briefly and resolves its consequences in the same reply. Do not request permission merely to roll.

The source leaves criticals, rerolls, advantage, modifier caps, opposed ties and clamping undefined. This candidate proposes retaining ordinary arithmetic without clamping and no special natural-1/100 effect, consistent with Core §6; this is a **proposed clarification**, not recovered AST canon. Do not assign Ian permanent competence ratings from individual +5/+10/+15 precedents. Use supported situational reasons and count each cause once. Any future standardized scale needs prospective adoption and regression against preserved outcomes.

**AST-R02—Established agency/time.** Only the player chooses Ian’s dialogue, thoughts, motives, emotions, purchases, politics, voluntary movement and actions. OOC/design discussion freezes campaign time. Advance only by reasonably consumed activity; return control after a meaningful exchange. NPCs and the wider world act autonomously within actual time, knowledge and means. No forced jump to France or a famous battle; no future historical knowledge.

**AST-R03—Established continuity.** Injury, exertion, property and consequences persist. Permanent death, capture, retirement and suitable successor play are possible. No guaranteed promotion or recovery. A successor requires their own identity and actual transfers; this candidate’s detailed transfer workflow is prospective, not an invented existing inheritance law.

**AST-R04—Campaign precedent, trial.** The completed wooden-weapon exercise used first to three clean touches, with Ian winning 3–2. That local score is neither hit points nor a lethal damage scale. No retroactive reroll or symmetric contest repair changes the recorded result. A future contest must define permissions, scoring, ties, interruption and adjudication before a consequential commitment.

## E4. Runtime entry and resolution

Use Core §§5/11/90/91 as the single runtime. The following is the AST adapter checklist, not another scheduler.

1. Distinguish a design message from an in-world declaration. For design, make no world event.
2. Read the actual save, selected versions, open player choice, relevant Library references and actor knowledge. Do not overwrite current state from the handoff.
3. Bind objective, method, target, scope, stopping condition, commitments, feasible effect and authorized resources. Resolve only material unknowns. If a player-authored sword history is missing, ask for it during play; never roll it into existence.
4. Check actual capability, tools, access, geometry, time, protection and institutional requirements. Skill cannot supply missing means or authorization.
5. Resolve routine work directly. Otherwise state independent modifiers, identify a causal Mixed branch and retain one result per unchanged uncertainty. A suggested compact display is `Masonry: 45 +15 experience −5 missing tools = 55 — Mixed` (source example, not a new event).
6. Separate execution from effect. An accurate arrow can be stopped by effective protection; a successful inspection reveals only accessible signs. Mixed can give partial effect or actual exposure within authorization; extra spending, voluntary risk, another day or a follow-up attack requires a new choice unless already bounded by the declaration.
7. Process exposure and autonomous reactions to the next causal frontier. Simultaneous activity shares pre-event state; scarce means require an actual allocation policy/decision. Do not freeze independent events while resolving a contested allocation.
8. Commit related changes once to their owners; record observations and later reports separately. Apply E12 to capture the exchange and due checkpoint without processing another world event. Narrate supported knowable results, append the separate visible continuity record/checkpoint, then return control at the next material choice.

### Gap and temporary-ruling protocol—Proposed

Record `ruling_id, missing procedure, applicable sources, affected action, assumptions, bounded effect, costs, duration, status, review trigger`. Offer a concrete ruling before resolving when it changes material stakes or introduces a new model. Mere uncertainty about an unimportant detail does not require stopping. A missing numeric input stays unknown; use a supported qualitative outcome when sufficient. Do not use a roll to conceal a missing rule. A temporary ruling is scoped and reviewable, not a silently permanent subsystem.

Lethal conflict specifically needs declared scope, actual offensive/defensive method, possible contact, protection, supported wound consequence, exposure, withdrawal/surrender options and persistence. This document supplies those required questions; it does not fabricate a calibrated damage engine.

## E5. Historical service and ordinary-life application—Proposed workflow

This application preserves Military Slim §§3–13 functions while using AST’s established facts. It enables only institutionally supported stages, not a modern universal military bureaucracy.

| Trigger | Procedure and result | Limits |
|---|---|---|
| Entry or offer | Identify household, route, position, assessor and approver; distinguish assessment, recommendation, terms, acceptance, authorization, muster and issue | Richard’s personal acceptance cannot supply Camoys’s pending approval |
| Terms negotiation | Record role, superior, duties, start/release, pay, support, property responsibilities and unsettled promises | No automatic standard wage, pension or ownership of the squire |
| Duty / handover | Record assignment, location, interval, means, relief and reporting; reconcile care/rest/travel | No invented voluntary overtime when relief fails |
| Training / assessment | Use instructor, method, prerequisites, actual usable time, feedback and evidence; distinguish learning from credential and permission | Presence or a title grants no instant competence |
| Doctrine revision | Evidence → authorized revision → communication → actual training/issue | Approval alone creates no fielded capability |
| Appointment review | Check actual evidence, vacancy, eligibility, sponsorship and authority; record effective decision | Recommendation is not promotion; authority is not skill |
| Order | Record issuer, authority, recipient, objective, constraints, means, send/receipt/response | Ian may convey Richard’s explicit instructions to Thomas, not command him generally |
| Conduct concern | Separate allegation, witness evidence, applicable practice, finding and executed sanction | Failed dice are not misconduct; success does not erase recklessness |
| Recognition | Record deed, witness/report, interpretation, recommendation and authorized recognition | No automatic fame or mechanical honor bonus |
| Deployment | Preparation → actual movement → arrival → operation → relief → recovery/review where applicable | No teleportation, compulsory historical participation or reset on return |
| Pay / issue | Separate entitlement, accrual, due, receipt, title, custody and return liability | Promised pay is not purse cash; allocated goods are not carried goods |
| Leave / restricted duty | Establish authorization, period, actual travel, functional limits and return obligations | No automatic full recovery or total incapacity |
| Missing / captivity | Preserve actual actor location/condition separately from report and service classification | No second casualty on reclassification; missing is not dead |
| Household support | Link actual remittance, delivery, care, labor and communication; permit independent household action | No invented dependants, automatic delivery or compulsory PC emotion |
| Separation / retirement | Record supported exit, effective time, continuing claims, duties and returned property | Ordinary life remains valid; no universal pension |
| Death / succession | Confirm supported event, actual knowledge and applicable estate/appointment process; retain world consequences | No automatic heir, inherited skills, private memories or office |

Civilian craft, literacy, care, relationships and livelihood use the same owners and actual commitments. Mentorship can supply instruction or access within the mentor’s means. Reputation is audience-specific evidence and interpretation, not one universal “legend” meter. The gatehouse ethical disagreement remains unresolved; it is not standing permission to abandon a post.

## E6. Task-specific interfaces

**Inspection/repair:** identify item, owner/custodian, location, observed defects, accessible tests and missing tools. Separate recommendation, quote, authorization, work, acceptance and actual condition change. Do not spend from an unknown purse. A known unsafe shield remains so until supported repair or replacement; an attractive sword gains no damage bonus.

**Archery:** bind each authorized shot, actual arrow, distance, lane, wind/elevation, release, exertion and protection. Firing changes location/status; search, recovery and inspection are different operations. A hit is not necessarily penetration. A Mixed hit does not become a miss by label. Reusing a shot result to score the same attempt requires no second execution roll.

**Horse activity:** evaluate actor, horse, familiarity, cue, route, bystanders, tack, load direction, condition and welfare. Abel (earlier Able) is an autonomous animal, not equipment. Known cue performance is task-specific; no unrestricted language comprehension, guaranteed rescue, battle certification or numerical mount bonus. Track horse and tack changes in their existing owners separately.

**Needs/travel:** establish route, actual intervals, passengers/loads, available support and relevant consumption profiles. A quantity without recipients and duration cannot establish sufficiency. Keep current stocks distinct from forecast needs. Missing rates block a numeric forecast only; no fabricated starvation or replenishment.

**Care:** describe accessible signs, supported functional restrictions, actual care and next meaningful review. Bandaging is not diagnosis or complete healing. No real-world medical advice is supplied. Unknown depth and recovery time remain unknown until supported assessment/profile selection.

## E6A. Equipment design, construction and visual evidence

**Status:** The supplied design facts are established directions/reported approvals from S11. The following lifecycle procedure is Proposed, using Core work, assets, institutions and content interfaces. It creates no new Core subsystem.

### One design, distinct lifecycle records

Keep `design reference → accepted draft → assessed design → authorized work → fabrication → fitting → controlled test → accepted usable configuration` distinct. These are possible stages, not a claim that every design has completed them. A repair or revision may loop through the relevant stages. Record designer/source, approved features, unresolved questions, material requirements, builder/access, authorization, actual inputs/time, inspection and test evidence, limitations and actual owner/custodian.

An accepted drawing is not an owned item. Construction consumes actual authorized resources and time; costs, mass and performance remain unresolved until supported. Completed fabrication is not proof of safe fit or effective protection. Experts may propose changes for concrete reasons; neither an expert opinion nor an image silently revises the approved design or spends Ian’s resources. Record any accepted revision and actual subsequent work separately.

### Coopian shield application

Library L11 owns the accepted **design draft**: enlarged curved heater form, opposing reliefs, deeper sword-side cut, protection above/below, exactly five front steel bands with directly painted heraldry, two traditional shield arm straps plus one smaller strap connecting to the over-bracer harness, and sword-side handle beside the deeper relief. Padding, bracer connections, fastening and release arrangements must agree across views.

These features grant no automatic defense, block, damage, extra action, hands-free use, quick-release time or encumbrance benefit. Before a consequential use, establish real material/construction, dimensions and fit where relevant, handling/reach, coverage under actual posture, attachments, release operation, load transfer, fatigue and compatibility with existing gear. Do not assume missing dimensions, Ian’s handedness, a tested arm harness or a fabricated shield. Expert construction/fitting/testing may reveal necessary changes; preserve both the design revision and the actual tested configuration.

The old wooden shield, removable heraldic leather and Coopian draft are distinct records. The Coopian heraldry is painted on steel bands; it is not automatically the old leather transferred or consumed. Reusing the leather or other parts requires actual authorization and accounting. Five bands describe one shield assembly, not five stacked independent armor bonuses or five shields.

### Arrival armor, sword and horse

Treat integrated mail/leather construction as one configured assembly with actual components and coverage, not a pretext to count one protective effect twice. Preserve the approved arrival-armor design while letting current conditions and later modifications follow game events. No armor score follows from appearance.

The family sword’s engraving, founding narrative and generational sequence are content/history. Use only supplied or retrieved established text; a successful examination cannot invent it. Legendary importance grants no magic or superior performance by itself.

Abel and earlier “Able” identify the same male horse. Preserve existing event/record IDs through an alias; do not create a second animal or rewrite historical spoken cues. Portraits and parent references establish visual identity only within their approved scope; they confer no new training, carrying capacity or battle steadiness.

### Additional record/interface fields

`AST.Design(id, revision, approval_scope, source_refs, protected_features, proposed_changes, unresolved_parameters)` links to K-INFO. `AST.Build` links that definition to K-WORK materials/commitments and the existing K-ASSET instance only when actually produced. `AST.Test` records configuration, method, conditions, result and limited acceptance. Art reads these records and current state; it cannot write performance, ownership or completed work.

| ID | Acceptance specification | Expected result |
|---|---|---|
| E-T23 | Load accepted Coopian draft | No item, completed work, protection bonus or cost created |
| E-T24 | Render five steel bands | One assembly; no fivefold protection or duplicated stock |
| E-T25 | Expert proposes a deeper cut | Proposed revision only; no fabrication, PC assent or payment invented |
| E-T26 | Record build, fit and test at different times | Separate evidence/stages; conditions and costs persist |
| E-T27 | Encounter Abel/Able aliases | One horse and unchanged historical cue/event records |
| E-T28 | Load integrated mail/leather design | Actual coverage and effect resolved once; no automatic additive armor |
| E-T29 | Use old bench evidence with a current save | Later repairs, injuries, possessions and decisions remain authoritative |

## E7. Records, triggers and persistence

Required fields are initialized only from supported facts. Unknown is neither zero nor not-applicable. Local record names below are proposed schema labels.

| Record | Minimum fields | Owner and trigger |
|---|---|---|
| AST.Profile | versions, override IDs, effective scope/time, content selection, unresolved models | Profile metadata; adoption/change only |
| AST.Action | actor, declaration, method, target, limits, uncertainty ID, modifiers, result, authorized cost | Links Core action and K-TIME event; declaration |
| AST.Evidence | proposition, status, originating source, observer, interpretation, occurrence/observation/send/receipt times | K-INFO; observation or report |
| AST.Service | person, institution, recommendation, approval, terms, muster, role, duties, claims | K-ORG/ECO linked records; actual decision or accrual |
| AST.ConditionView | actor/component, cause, observations, restrictions, care, review, uncertainties | Read-through K-ACTOR/K-ASSET; actual harm/care |
| AST.ItemView | instance, definition, title/custodian, location, quantity/unit, condition, reservation | Read-through K-ASSET/K-STOCK; transfer/work/use |
| AST.RelationshipEvidence | people, witnessed/received event, interpretation, supported change | K-ACTOR with K-INFO evidence; relevant interaction |
| AST.Work | task, prerequisites, worker/asset commitments, inputs, completed work, acceptance | K-WORK; actual processed interval/completion |
| AST.Ruling | missing rule, scope, assumptions, procedure, status, review | Profile metadata; unresolved material model |

Event envelope uses Core §11: campaign-scoped ID, cause, causal time, action/authority references, visibility, dependencies, expected pre-state and owner-qualified write set. Same ID/same payload is a no-op; same ID/different payload is a conflict; reject cross-campaign references before reading or replaying state. Commit all related transfer changes or none. Physical loss is not prevented merely because stock is reserved.

Save current time (including uncertainty), identities, locations, quantities/units, condition history, money/claims, commitments, work fractions and processed spans, retained rolls, event payloads/IDs, queues, actor knowledge and open choices. Reopening the bench scene never repeats prior shots, heals Ian or reissues the recommendation.

For ChatGPT play, E12 additionally requires chronological scene history and visible checkpoint triggers. This is an export/capture procedure over these records, not another state owner. A latest-state panel alone is insufficient evidence for a full day/chapter recap.

## E8. Acceptance and regression specifications

These are **specified acceptance cases**, not executed gameplay. The appended verification receipt separately reports bounded checks actually run.

| ID | Setup / action | Required result |
|---|---|---|
| E-T01 | Open design discussion at handoff | Time and campaign state unchanged |
| E-T02 | Qualified routine observation with adequate access | Supported observations without mandatory roll; real time retained |
| E-T03 | Superb accuracy against protection that stops the channel | No revived penetration from margin or skill |
| E-T04 | Mixed inspection suggests paid repair | No purchase, new work or voluntary expenditure without authorization |
| E-T05 | Repeat unchanged search/inspection | Retain uncertainty; no spawned objects or free rerolls |
| E-T06 | Read Library on a newer save | Snapshot cannot overwrite later valid events |
| E-T07 | Apply recommendation | No formal muster, wages, lodging or title |
| E-T08 | Two jobs require the same person/tool simultaneously | Resolve real contention; no double progress |
| E-T09 | Move scene → day → scene | Same wounds, exertion, arrows, stock and work fractions |
| E-T10 | Repeat payment event / alter its payload | Exact replay no-op; conflict rejected without partial changes |
| E-T11 | Delayed capture report | Changes recipient knowledge; no second casualty or estate transfer |
| E-T12 | Bandaged palm / familiar horse exercise | No automatic healing or battle certification |
| E-T13 | Later Library draft gives sword a maker | Reject unsupported PC family lore |
| E-T14 | New contest with equal interchangeable roles | Specify symmetry/ties; do not map 41/29/30 action bands directly to fair win/loss/draw |
| E-T15 | Successful quiet service | Stability can persist without stronger enemies |
| E-T16 | Missing ration rate or damage model | Block dependent calculation only; continue independent supported work |
| E-T17 | Successor proposed | No inherited skills, title, memories or duplicated assets |
| E-T18 | Approve doctrine but no training or issue | No fielded capability |
| E-T19 | Actor sees an image of a hidden fact | Image must not grant knowledge; Art visibility gate rejects it |
| E-T20 | Independent runner reconstructs from save | Same next legal choice, pending events and available means; no invented action |
| E-T21 | Death, deprivation, scarce resources or repeated harm | Resolve actual supported mechanism; no immunity from summary caps or unrelated catastrophe |
| E-T22 | Load Fantasy/Roman/Shinobi numerical content | Remains inactive without explicit complete compatible AST selection |

## E9. Calibration and unresolved requirements

| Priority | Gap | Evidence needed before quantitative activation |
|---|---|---|
| Immediate | Modifier scale and opposed contests | Repeatable cause mapping; boundary, repetition and relabeling tests |
| Immediate | Lethal combat, protection, wounds | Complete contact/effect chain, valid envelope, retreat/capture/death and persistent-care tests |
| Immediate | Purse, quotes, pay and provision | Actual campaign terms/amounts; dated currency convention; no guessed conversion |
| Immediate | Existing gear/tack | Supported inspection and repair constraints; no arbitrary durability |
| Next | Human/horse exertion, needs, travel, load | Units, intervals, rates/bounds, rest and scarcity cases; historical evidence separated from game defaults |
| Next | Service authority and practice | Dated institution-specific authority, duties, release and conduct rules |
| Later | Learning, reputation, succession | Evidence thresholds, information spread, transfer/legal process and long-term continuity cases |

The supplied consolidation establishes Ian’s name/build/likeness basis, arrival armor, heraldic arrangement, sword design/engraving structure and Abel’s male identity; Library L11 specifies the boundaries. Exact approved images, full inscriptions/founding narrative, current purse/date/save, biological recovery schedule and battlefield horse qualification are not supplied here. Do not treat these unavailable details as nonexistent in the running game or fill them with invented values. Empirical realism, balance, AI reproducibility and live play remain open even after structural checks pass.

## E10. CMRR, provenance and migration

Source inventory and byte pins follow below. S1’s original chronicle is absent; only its derivative reference is available. The originally linked chat supplies only the request. The later supplied S11 text now adds authoritative design direction and reported approvals. No external historical research was performed for this source-conservative rebuild. Visual and catalogue proposals must not be cited as historical research.

| Source function | Disposition / destination | Reconciliation reason |
|---|---|---|
| S1 §1 resolution, probability table | Retain E3; probabilities in numerical reference below | AST bands precede optional parent numbers |
| S1 §2 agency/time | Retain E3–E4 | OOC freeze and no forced historical travel |
| S1 §3 competence/modifier precedents | E3 constraints; Library L6 evidence | No permanent ratings from examples |
| S1 §4 combat/archery | E3/E6; L6 exact trial/shot record | Scores, performance and harmful effect separated |
| S1 §5 injury/fatigue | E6; L3 conditions | Descriptive persistence retained; numeric gaps explicit |
| S1 §6 equipment/ammunition | E6–E7; L4 instances | Inspection ≠ repair; recovery ≠ serviceability |
| S1 §7 horses | E6; L5 cues and precedents | Animal autonomy and tack distinct |
| S1 §8 money/supplies/travel | E5–E7; L7 merchant and account evidence | No invented rates or continuing debt |
| S1 §9 service/reputation | E5; L3/L7 terms and claims | Approval, appointment, authority, trust distinct |
| S1 §10 information/craft | E4/E7; L6/L7 evidence | Observation cannot invent structural proof or family lore |
| S1 §11 advancement/death | E3/E5/E9 | Preserve career and successor premise; formulas not invented |
| S1 §12 handoff | L3–L4 sole snapshot | Read-only snapshot, not live state |
| S1 §13 unresolved mechanics | E2/E9 | Gaps preserved, not silently filled |
| S1 §14 templates/continuation | E4/E7; L3 open decision | New schemas preserve functions; scene unadvanced |
| S2 shared Core 3.2 | E2 provider map | Inherit once; no copied generic subsystem |
| S2 SCL R1/R2 maturation | Library L2/L8 | Held remains held; proposed qualification is not selection |
| S3 Military §§3–13 | E5 application table, E6–E7 | All life/service functions retained at relevant scope |
| S3 Military §§14–20 | E2/E8–E10, Library L8 | Content gates, evidence limits and prospective migration |
| S3 older compatibility checklist | Historical to v1.0, superseded in scope by 1.2 receiving proposal | Do not treat it as veto of later receiving source or proof of AST adoption |
| S4 Roman accepted engine | Comparison only | Acceptance within Roman does not select Roman numbers/lore for AST |
| S5 Fantasy; S6 PAF; S7 Space; S8 Shinobi | Reference boundaries, not active dependencies | Shared procedures already inherited; no foreign lore or duplicate mechanics |
| Prior art draft vs S11 | Rebuild Art around reported approved references and explicit supplied designs | Earlier blanket unknowns are superseded; optional palette/type suggestions stay subordinate |

**Accounted removals:** no valid recovered AST function or settled outcome removed. Duplicated shared rules are replaced by named parent interfaces; campaign examples move to Library. Optional foreign numerical profiles and speculative appearance are excluded from activation, not deleted from sources. Obsolete campaign titles remain provenance aliases in Library. No source file is changed or deprecated.

**Retained changes from S1 v0.1:** separates engine/content/art ownership; adds prospective Core 3.2 receiving map, complete military-life application, typed records, content gates, acceptance requirements and migration procedure; preserves unresolved parameters and historical results.

**Migration procedure:** (1) obtain the actual latest save and explicit scope/effective-time adoption; (2) snapshot identities, state, queued events, retained rolls and open choices; (3) compare fields against this proposal, preserving unknowns and actual totals; (4) map existing records to owners without re-creation or guessed past events; (5) select each needed complete model and run applicable tests; (6) record prospective cutover and reversible pre-cutover copy. If compatibility fails, keep the prior profile active for that scope. No retroactive rerolls, refunds, repairs, training, muster, wages, appointments or recovered health. A later explicit correction receives its own scoped audit; it is not an in-world compensating event unless an actual event occurred.

### Version 0.3 reconciliation

The user clarified that the game continues and these are three project-reference files. Remove the v0.2 implication of beginning from a handoff; retain its rule evidence and all generic interfaces. S11 supplies corrected identity and design facts to Library L11 and Art A1–A10. Add E6A for design/build/test distinctions. No new combat numbers, material properties, current-world transactions or rule adoption are inferred. Existing gameplay remains unchanged; only this document set is rebuilt.

## Source identity appendix

Paths below are relative to the supplied project, or ZIP members as stated. Hashes identify inspected bytes; they do not establish adoption. S4–S8 were inspected at inventory/README/status scope, not substantively validated as AST engines.

| Source | Locator / role | SHA-256 |
|---|---|---|
| S1 | `A_Scots_Tale_Systems_Reference_v0_1.md`; all 14 sections read; derivative of unavailable `Ian_Cameron_1415_Campaign_Chronicle_and_Handoff.md`, §§1–25 | `180335f01f946c3f6aa419bfdf980d8093f3befe963c35baf4309e3cc9587dc3` |
| S2 | `sources/IRGS_Full_Release_R2.zip`; Core 3.2, SCL 1.0; candidate maturation overlays | `a4d61f67c9187214517956996e00bdf184e689cac83db3710a1c05856d44bca7` |
| S3 | `sources/IRGS_Military_Slim_v1_2_Core3_2_and_Military_Library_v1_0_Combined_Release.zip`; Military 1.2 receiving proposal and Library 1.0 candidates | `4df218f9d3e9010e756cc2937126481c1eaeda30f480666a12f5cf3fb014ef94` |
| S4 | `sources/IRGS_Roman_Republic_v1_2_Engine_Content_v1_0_Complete.zip`; README/status and package comparison; no Roman lore/model import | `bf194fa406df343c4a179940cd240a09df82802058ff1acda659189074205fb2` |
| S5 | `sources/IRGS_Fantasy_Core32_Library20.zip`; README/status and package comparison; no Fantasy model import | `8ed89804b3d14ba7e07a6b40b02be5edf7a9783b35ae944a41c844fdd7f1c056` |
| S6 | `sources/IRGS_PAF_Core32_Library20.zip`; README/status and package comparison; no crisis model import | `bc3a7b5d4d8cfedf38730c9f5a7568419dd01ab9c3fd43f1e9edbaa350d6c259` |
| S7 | `sources/IRGS_Space_Exploration_and_Colonization_Slim_v0_2_Core3_2_R2.zip`; README/status and package comparison; no Space model import | `3172c7f1cc7d9d7b59e69385f0daf427ce831303a12424163f213e08296be1be` |
| S8 | `sources/IRGS_SNWE_R0_3_and_SNCL_v1_0_Combined_Release.zip`; README/status and package comparison; no Shinobi model import | `58148fe4cdc7f9ce1829f0b0610e642b2a7d8c339df060002e478d87e6bbfab6` |
| S9 | `sources/IRGS.zip`; container compared against all seven standalone releases | `58d52b29f60fa2123de47172e7556fc717a6f194ffcfe13a9b1fa23a63bf0cdf` |
| S10 | Referenced chat `6ad01a16-0a7c-83ea-84a1-c1420141d762`, “Write Game Files”; read via chat tool; one user request, no delivered files or additional facts | Not a filesystem source |

Primary ZIP member locators:

- S2: `IRGS_Core_Engine_v3_2.md`, `IRGS_Engine_Bindings_v3_2.json`, `README.md`. Core introduction/provider map and relevant procedures were inspected; this is not a claim to rerun the entire parent release’s tests.
- S3: `MilitarySlim/IRGS_Soldier_Military_Life_Slim_v1_2_Core3_2_MCL1_0_Proposed.md`; `MilitaryLibrary/IRGS_Military_Content_Library_v1_0_Candidate.md`; `MilitaryLibrary/Military_Slim_Core_3_2_Compatibility_Gate.md`.
- S4–S8: `README.md` and archive inventories/byte comparison.

Project instructions supplied in this task govern layer ownership, CMRR and agency. No external research or live campaign interaction is represented as evidence.


### S11 — Supplied art consolidation and current task clarification

The user supplied `Pasted text.txt` (attachment `9214b159-9989-4d95-91a7-63beb02c657d`; SHA-256 `a99453d655a388e98829cbf819659219605b170f17bc1ea9cad896a462b6d414`). Its eleven numbered contributions govern the corrected identity/design facts and approval distinctions in this revision. Although introduced as combined direction, the text describes itself as the Art Design chat's contribution to consolidation; underlying Character Sheet/Art Design chats and their image references were not independently inspected. Preserve its explicit directions without claiming a full two-chat or image audit.

Current user clarification: the game is still running; retain **three separate project files**. These documents describe features, mechanics, content and visual requirements without restarting play. Version 0.2 remains a historical draft, not a competing current project specification. The user's later corrections and actual game events continue to govern.

## Numerical reference: recovered d100 bands

Assuming uniform integer rolls 1–100 and ordinary addition, the established thresholds imply these exact distributions. These calculations are not calibration of modifiers or a new rule. Routine qualified work still avoids unnecessary rolls.

| Net modifier | Failure | Mixed | Success |
|---:|---:|---:|---:|
| -10 | 39% | 30% | 31% |
| -5 | 34% | 30% | 36% |
| +0 | 29% | 30% | 41% |
| +5 | 24% | 30% | 46% |
| +10 | 19% | 30% | 51% |
| +15 | 14% | 30% | 56% |

## E11. Concept references and shield retention/release interface

S12 supplies named-character visual references; it adds no new resolution system, capability ratings, inventory or completed events. Use Library L12 and Art A11 for exact reference identity and conflicts. The old handoff remains historical evidence only.

**S14 established design intention:** two traditional shield arm straps plus one smaller strap connecting to the over-bracer harness. The smaller connection supports additional control when not gripping the handle. Its clasp is intended to release quickly so the shield can be released when another person takes control of it.

**Proposed operating interface, not a calibrated benefit:** distinguish handle grip, the two ordinary arm straps, the smaller over-bracer connection and its clasp. Read the actual fitted configuration and retention state. Releasing the clasp is not automatically complete separation if other straps still retain the arm. Before consequential use, define whether/how the ordinary straps clear the wearer, accessible release actuation, load/jam behavior, range of motion and the actual time/effort needed. Preserve the user's desired release function as a design goal while testing a feasible implementation.

No automatic extra hand action, guaranteed shield defense while ungripped, instant escape, zero encumbrance, theft immunity or numerical control bonus follows. If Ian declares a release during a grab, resolve actual access, configuration, load, opposition and consequences through the existing action/effect procedure. Do not invent Ian's release decision, a successful disarm, dropped weapon or unrelated injury. One loss/transfer is committed once; attached components keep their actual ownership/custody and location.

Testing should distinguish normal ungripped control, actual clasp operation, a loaded/grabbed shield and full separation from the wearer. Record configuration and narrow results without claiming comprehensive engineering validation. Outcomes remain unresolved until an actual supported test or ruling; no implementation is performed by this document.

| ID | Acceptance specification | Required result |
|---|---|---|
| E-T30 | Load concept board saying “warhorse” or showing equipment | No new qualification, measured capacity or item issue |
| E-T31 | Release smaller connection while ordinary straps retain arm | Do not assert complete separation until actual clearing mechanism permits it |
| E-T32 | Opponent takes control of shield | Return meaningful choice; release only if declared or within prior authorization |
| E-T33 | Test release in unloaded configuration | Do not certify under-load reliability or universal timing |
| E-T34 | Successful actual release | Update grip/attachment/location once; no duplicated shield or component |


## New source provenance

- **S12:** user-supplied `AST Character Concepts.zip`; SHA-256 `897a2d5b3cc067858bb912ab3afd1dcb9dcc8c50b444a79ee43c4b717c1b863e`. Twenty-nine PNG members were preserved in the source reference set. R1 retains exact member/hash mappings to the separate concept archive; its shield image is bundled. Names/roles and visual observations are source-backed concept metadata, not independently verified biographies or historical research. Embedded wording is reference data, not instructions to the assistant.
- **S13:** current Coopian image supplied by the user, preserved as `Coopian_Shield_Current_Inaccurate_Draft.png`; SHA-256 `fb27f4f253177b7d3d82680b21c5657e0ed1a61454b7fade9530cc2304a56492`. The user explicitly says it is still somewhat inaccurate; do not promote it to a final engineering or exact-design reference.
- **S14:** current direct user clarification: two traditional arm straps, one smaller over-bracer connection for control without gripping, and a quick-release clasp for releasing the shield if another person takes control. This correction outranks prior strap wording and conflicting pixels.

**Source precedence for this revision:** current user corrections → explicit earlier design requirements within uncorrected scope → the user's identified current imperfect shield image within compatible scope → character concepts for their respective subjects. A character board's equipment vignette does not displace the dedicated shield reference. Images do not select new mechanics, create assets or prove events.

## v0.4 change and migration record

Compared with v0.3, add the 29 available concept references, replace obsolete blanket image-unavailability statements, record character-board conflicts, pin the user's current imperfect shield image, and replace the uniform-three-straps interpretation with the explicit two-arm-straps-plus-smaller-over-bracer correction. Retain all unrelated mechanics, source precedence, design requirements, historical evidence and unresolved calibration. No prior images are edited or deleted. No gameplay state, current character condition, completed work or rule adoption changes. The concept metadata and latest design correction are documented; engineering performance remains unproved.

## Prior v0.4 verification receipt - reported evidence

The earlier v0.4 source reports 76 file/link/reference checks passed, zero failed. This is historical evidence, not the fresh R1 result. The 29 extracted originals match their archive-member hashes; all linked local references and companion files resolve. All boards were overview-inspected and the three specified boards inspected individually; the supplied current shield image was visually reviewed. Written corrections were reconciled with active strap descriptions. These are document/reference checks, not full caption transcription, finalized image QA, engineering tests, live playtesting or calibration.

## Prior maintenance R1 receiving and evidence record

No campaign adoption or automatic migration is performed by this maintenance revision.

Compared bidirectionally with the supplied v0.3 archive and the recovered v0.4 documents. Retain the later explicit S14 shield correction, all historical trial outcomes, stable actor/item handles, approved-design boundaries and every acceptance specification. The corrected package selects Core 3.2 maintenance R3 and SCL 1.0 by exact hashes; Military 1.2 and its catalogue retain their proposed status. No default Historical/Fantasy numbers, held content or current campaign quantities are activated.

The three AST project specifications remain separate. The reference index preserves all 29 concept-board identities against their separate original archive; the current imperfect shield PNG is included unchanged. Source v0.4's image observations and prior verification receipts remain reported evidence. R1 performs document, dependency, source-preservation and bounded reference-fixture checks only. See [the review and CMRR record](CMRR_Chat_Continuity_v0_5.md) and [fresh verification evidence](verification/RESULTS_v0_5.json).

No save, latest character-sheet registry or campaign transcript is imported. Current locations, wounds, appointments, purse, possession, completed construction and open player decisions remain with the running game. This maintenance revision changes documentation and receiving references only. Outcome-changing quantitative gaps and live playtesting remain open.

## E12. ChatGPT play continuity and recaps

**Current requested presentation procedure:** use [IRGS ChatGPT Play Continuity Adapter 1.0](IRGS_ChatGPT_Play_Continuity_Adapter_v1_0.md), selected in [the receiving binding](AST_Receiving_Binding_v0_5.json). The shared procedure implements Core §§86/98; it is not an AST-only simulation subsystem.

After every GM gameplay reply, capture the resolved exchange in a short separate visible Continuity note, including dialogue meaning, actual actions, material changes and the open player choice. Preserve ordinary work, kindness, disagreement, instruction and relationship interactions even without numerical changes. Do not invent Ian's emotions, speech or follow-up action to complete a log.

Checkpoint at scene breaks, after five GM gameplay replies since the last checkpoint, after critical continuity changes, and on pause/transfer/request. Coalesce coincident triggers. Five replies is an adjustable editorial default, not game time or a guarantee of unlimited recall. OOC and recap-only replies do not advance the counter or world.

Maintain ordered scene records across checkpoint segments. At day/chapter recap, account for all available scenes and known gaps, including conversations and unresolved terms. A brief recap remains an additional view. It cannot replace the source-backed chronicle or replay its events. An unfinished day, unpaid quote, unanswered question and pending approval remain unfinished.

A transfer checkpoint includes actual supported state, retained uncertainty, work/queue and the open decision, plus recoverable history at a declared detail level. Treat state recovery and history coverage separately. Save to a file only through available authorized tools and confirmed success; otherwise label the export posted in chat only. Keep secret information out of public records and do not promise unsupported private persistence.

Enable this presentation procedure prospectively from the supported current frontier. No current save was loaded for this build, and no historical day was reconstructed. Existing historical snapshots stay historical. Inaccessible earlier material is a named source gap, not a blank to fill with plausible narration.

Acceptance specifications CC-01 through CC-28 and the adapter's ready-to-use play instruction apply. Fresh scripted checks identify their narrower executed scope; no live-session retention test is claimed.
