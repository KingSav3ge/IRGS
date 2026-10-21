# IRGS — Soldier and Military Life Simulation
## Slim Engine v1.2 — Core v3.2 and Military Content Library v1.0 Receiving Edition

**Document ID:** `IRGS-MLS-SLIM-1.2`  
**Date:** 14 October 2026  
**Status:** **Proposed complete source/receiving edition**, not automatically adopted, calibrated or live-playtested  
**Pinned parent:** `IRGS-CORE-3.2` (IRGS Full Release R2)  
**Pinned shared catalogue:** `IRGS-SCL-1.0` (canonical SCL family revisions remain `@0.2` where named)  
**Military content library:** `IRGS-MIL-LIB-1.0` (proposed, 48 unqualified template candidates)  
**Receiving binding:** `IRGS-BIND-MILITARY-SLIM-1.2`, inheriting existing Core `IRGS-BIND-MILITARY-3.2`  
**Principal military sources:** Soldier/Military Life Slim v1.0; Military Life Simulation v0.4 and Slim v0.5 through v1.0 provenance.

> **Authority and scope:** This edition retains the specialized soldier/military life workflows, selects Core v3.2 shared services, and binds Military Library v1.0 without adding a duplicate military inventory, project clock, human physiology, combat algorithm or troop register. Historical, branch-specific and numerical profiles remain mandatory where their values change the outcome. Neither packaging nor a successful source verifier adopts rules or migrates campaigns.

### Navigation

1. [Scope and authority](#s01)
2. [Core 3.2 bindings, status and deployment profile](#s02)
3. [Entry and service terms](#s03)
4. [Daily duty and military training](#s04)
5. [Rank, appointment and career](#s05)
6. [Comrades, mentors and unit culture](#s06)
7. [Command and orders](#s07)
8. [Conduct, discipline and recognition](#s08)
9. [Deployment, operations and return](#s09)
10. [Pay, provisioning and issued property](#s10)
11. [Leave, restricted duty, missing personnel and captivity](#s11)
12. [Household life during service](#s12)
13. [Separation, retirement and succession](#s13)
14. [Military library, era and branch selection](#s14)
15. [Military records and event procedure](#s15)
16. [Source coverage and acceptance cases](#s16)
17. [Adoption, provenance and migration](#s17)
18. [Operational five-gate playability contract](#s18)
19. [Historical v1.1 receiving record and reconciliation](#s19)
20. [CMRR full reconciliation and receiving verification](#s20)

<a id="s01"></a>
## 1. Scope and authority

The central actor is a person with a life, responsibilities and relationships. Combat, command and advancement are possible activities, not compulsory destinations. A recruit, retainer, ordinary soldier, technical specialist, operator, commander or retired veteran can be a legitimate protagonist. Other careers remain available through the selected life procedures.

Use institution-native roles. Rank, office, personal skill, qualification, service membership and current assignment are separate facts. A commission does not create mastery; a recommendation does not complete enrollment; a victory does not repair equipment or settle personal obligations.

Authority remains current explicit user direction → established campaign rules/overrides → adopted procedures within their scope → selected Core → a scoped ruling in an unresolved gap. Player agency, autonomous NPCs, actual time, limited knowledge and persistent consequences remain inherited. OOC work advances no time.

A Scot’s Tale and Iron Aegis are complementary design references. Their people, current state, technology and specific institutions are not universal starting content. Historical human play retains its selected real-world limits and permanent death. Fictional campaigns supply any exceptional capabilities through explicit modules.

<a id="s02"></a>
## 2. Core 3.2 bindings, status and deployment profile

### 2.1 Inherited procedures (one owner per actual fact)

This edition selects the **MILITARY** provider in `IRGS_Engine_Bindings_v3_2.json`, Core §112. Its complete provider groups and section lists are preserved unchanged in the **engine-specific sidecar receiving binding**. The historical v1.0 Core 3.0 section map is archival; it is not a parallel runtime provider. No d100 roll is added alongside an established d20 or other complete selected resolution adapter.

| Military function | Core v3.2 provider | Specialized retained work |
|---|---|---|
| Player authority, feasibility, uncertainty, agency, resolution | §§4–9, 90–91 | Service tasks, military objectives and declaration/choice checkpoints |
| Clock, time, concurrency, records and idempotence | §§10–12, 47, 85–86, 90–91, 96 | Rosters, relief, dispatch, reporting, event subscriptions |
| Actual actors, capability, fatigue, wounds, care | §§14–19, 31, 43, 64, 68–71, 106, 118, 122 | Duty fitness, training, casualty support and human profile selection |
| Stock, title, claims, financial settlement and movement | §§20–24, 35–38, 105, 109, 114 | Unit provisioning, issue/return, pay, benefits and remittance |
| Assets, modes, protection, components, crew | §§21, 48–58, 101 | Correct weapons/armor/branch equipment adapters, stations, damage and custody |
| Project, infrastructure, readiness, learning | §§23, 41, 71–74, 101–104, 107–110, 119, 121 | Drill, qualification, maintenance, deployment preparation and doctrine rollout |
| Institutions, orders, commands, conduct, personnel, careers | §§25–34, 38–46, 65–69, 76, 107, 113, 117, 122 | Enrollment/appointment/rank, orders, unit culture, justice and awards |
| Reconnaissance, intelligence, operations and aftermath | §§42, 47–63, 83–84, 85–86, 120 | Actual qualified forces, command limits, reports, continuing losses and availability |
| Material content, initialization, overrides and compatibility | §§79, 88, 97–99, 111–112; Appendices A–D | Actual definition/selector/model binding, prospective selection and restoration |

**State owners:** K-TIME, K-ACTOR, K-STOCK, K-ASSET, K-WORK, K-INFO, K-ORG, K-NET, K-POP. They keep their Core Appendix A meanings. Generic GOV/ECO/INV/MAR/CIV/MED/INTEL/URBAN/LIFE services activate only when relevant; COMP and WILD may additionally activate where the actual scenario warrants them. No genre-specific writer duplicates a Core balance, injury, person, asset or event frontier.

**Core reference change:** v3.2 Appendix A owns records; Appendix **B** contains inheritance, deployment, migration and calibration; Appendix **C** contains acceptance/regression requirements; Appendix **D** contains optional scoped profiles. v1.0 references to Appendix F or a Core v3.0 Appendix C deployment contract are historical only. Core §112 and Appendix B now own receiving compilation.

### 2.2 Native and selected numerical profiles

Retain the selected complete effect/resolution chain for the campaign. Core §6 provides a d100 reference adapter, **not mandatory dice alongside an existing d20 engine**. No conversion of a d100 percentage modifier into a d20 modifier is implied. Historical Life and Military Career v0.3 can supply its native human creation, needs, learning, load, injury and care implementation when the actual complete source/profile is explicitly attached. Fantasy-profile values and Historical values are not interchangeable.

Define one valid cause-based profile for condition/recovery, workload/fatigue, load, learning schedule, suppression, collective cohesion, weapons/effects and equipment condition when relevant. Core Appendix D optional values require an explicit compatible selection. An unknown consequential parameter does not become zero, unlimited, free or an invented value. Actual supported routine qualitative procedures can proceed independently.

Military morale, cohesion, discipline and credible threat retain Core §§32–34 separate meanings. Authorization to command is not technical proficiency, and a formation effectiveness rating is not actual headcount. K-POP applies to residual groups while named personnel use K-ACTOR; casualty and readiness views point to one real population.

### 2.3 Receiving deployment manifest

Each campaign chooses only material fields. Missing dependencies block their dependent calculation, not all play. The following is a **schema, not a preloaded campaign**:

```yaml
engine: IRGS-MLS-SLIM-1.2
core: IRGS-CORE-3.2
core_binding: IRGS-BIND-MILITARY-3.2
receiving_binding: IRGS-BIND-MILITARY-SLIM-1.2
shared_library: IRGS-SCL-1.0
military_library: IRGS-MIL-LIB-1.0
status: proposed_source_selection; adoption_is_separate
services: K-TIME, K-ACTOR, K-INFO, K-ORG; other owners only if used
institution_profile: exact identity/version, jurisdiction, eligibility, service terms
resolution_profile: complete model/source and relevant scopes
physiology_learning_load: selected compatible sources/units/limits
morale_cohesion_threat: selected military submodels and triggers
branch_and_equipment: task-specific platform, effect, mode, crew and maintenance models
content: exact library/entry/revision/selector/readiness/source backing
actor_controls: independent NPC goals/knowledge; player-held voluntary decisions
starting_state: locality/time, people, actual stock/claims, commitments, knowledge
resource_constraints: finite inputs, reservations, deliveries, service capacities
runtime: Core §§5, 11, 90–91; source event IDs and known frontier
exceptions: scoped campaign rules, permissions, termination and recovery
acceptance: sections 16 and 18 executed-case evidence; unresolved blockers
migration: explicit effective time, unchanged historical records, remapped references
```

### 2.4 MILITARY binding is not a fully qualified item library

Core's provider binding already covers Military generically; this slim-specific receiving document supplies actual source identity, native workflow ownership, content references, triggers and dependency boundaries. **The Military Content Library v1.0 is a proposed genre catalogue**, not 48 certified functional equipment/platform specifications. Its 14 pinned SCL exemplar definitions match the current R2 registry on names, semantic types, specification readiness and selectors, even though the library verification snapshot was taken against an earlier SCL v1.0 byte edition. Keep its original snapshot for provenance; the combined package supplies a new current-registry comparison.

Use Core §§111–112, Appendix B and this source edition before activating any numeric branch-specific work. Reference, activation and deprecation gates remain distinct. No abstract item template directly creates a weapon, issued object, ammunition, logistics stock or licensed operator.

<a id="s03"></a>
## 3. Entry and service terms

Record how service is entered: recruitment, apprenticeship, household service, levy, conscription, commission or another actual institution-defined route. Check available position, eligibility, claims/references and relevant demonstrated ability. Social access and practical competence remain separate.

Resolve entry through the stages actually required:

1. Identify institution, route, available place and decision authority.
2. Establish claims, references, eligibility and assessment requirements.
3. Perform actual assessment where needed; routine verification uses the selected Core procedure.
4. Establish terms, unresolved promises and any player decision to accept or negotiate. Compulsory enrollment follows an actual institutional process; it is not invented voluntary consent.
5. Record effective enrollment/appointment, duties, pay basis and provision.
6. Record actual accommodation, roster assignment and issue of specified property.

The agreement names service basis, start/end or release condition, role, superior/authority, duties, remuneration, in-kind support, equipment responsibility, restrictions and permitted exit. A successful examination, patron’s recommendation or verbal welcome is not automatically a paid appointment or equipment issue.

An unsuccessful applicant retains their existing life and recorded time spent. No automatic debt, hostility or criminal status follows merely from failure.

<a id="s04"></a>
## 4. Daily duty and military training

### Duty and handover

Roster entries specify duty, person, qualification, location, interval, relief, equipment, reporting and standing authority. Watch, patrol, preparation, maintenance, transport, administration, standby and instruction use real commitments. Reconcile travel, meals, personal care, rest and competing responsibilities under Core time/capacity rules.

Handover changes actual responsibility, custody, outstanding instructions and known hazards. Relief must actually occur. If relief is late, present the resulting decision and institutional expectations; do not silently invent an indefinite voluntary extension of the player's duty.

Standby or on-call duty restricts location/response availability as its terms require. Assess actual activity and sleep interruption through the selected condition/fatigue rules. It is not automatically either strenuous work or protected sleep. No universal eight-hour service day is imposed.

### Training and qualification

Military learning distinguishes practice, demonstrated skill, examination, institutional qualification and permission to perform a role. A training assignment names instructor, learners, objective, prerequisites, resources, exercise, actual hours, feedback, evidence and assessment authority.

Reserve required people and equipment through existing commitments. Interrupted or incompatible hours do not receive full training credit. Ordinary work supplies practice only where challenge and feedback support it. Course completion is not automatically earned through being present on a roster.

Collective drills retain who practiced together, methods demonstrated and conditions. Individual competence, unit coordination/cohesion and formal qualifications remain separate results. Replacements need actual orientation; replacing a specialist can remove a capability even if average unit experience stays high.

Branch transfer, qualification renewal and new-equipment familiarization follow the institution/profile. No expiry arises from a scene change, and familiarity with a new variant does not erase the underlying discipline.

### Doctrine, instruction and fielding

Apply Core §110 to actual military evidence, doctrine and equipment adoption. The service profile names who can change standing instructions, qualification standards and authorized tactics. A report, promising prototype or successful exercise is evidence for review; it is not a force-wide capability or a new credential for everyone.

Link the approved revision to the units/personnel actually informed, trained and equipped. Record which instruction/configuration version each affected role uses and any supported restriction during transition. Training, stock issue, maintenance support and command approval retain their separate completion conditions. An old practice is retired only within the authority and scope of the actual change; different units can be at different supported stages.

<a id="s05"></a>
## 5. Rank, appointment and career

Maintain rank, current appointment, command authority, qualification and duty separately. Temporary, acting or specialized appointments exist only if the institution supports them. A vacancy is not an automatic promotion.

At a relevant review, consider actual service evidence, competence, eligibility, institutional need/vacancy, authorized sponsorship, current condition and the person's goals. Record recommendation, approving authority, decision, effective time and changed duties/pay/provision.

Reviews create opportunities or decisions rather than guaranteed advancement. Holding command can produce evidence and learning through actual work; its title does not grant instant expertise. A protagonist can remain an ordinary soldier, change role, return to civilian work or retire under actual terms.

Injury or family responsibilities can change opportunities only through supported duty, service and household mechanisms. Do not assume universal loss of pay or automatic benefits.

<a id="s06"></a>
## 6. Comrades, mentors and unit culture

Relationships with peers, mentors, superiors and subordinates use the same living actors and selected social procedures. Track professional trust, affection, rivalry, grievance, obligation and confidence in judgment where relevant, with observed/received evidence.

A shared event can affect people differently. Rescue may create gratitude without compulsory intimacy; a successful reckless action may also provoke professional concern. Neither reaction is automatic. A decorated newcomer can still be unfamiliar to their unit.

Individual morale, collective morale, cohesion and discipline remain distinct. Apply the selected military model to actual causes. A collective morale change does not dictate the player character's emotions; coordination does not require universal friendship.

Losses preserve named bonds, vacancies, disrupted routines and dependants. Replacement personnel have their own history and knowledge. They do not inherit the absent person's relationships. Mentorship provides actual instruction, access or sponsorship within the mentor's means; it is not a global advancement bonus.

<a id="s07"></a>
## 7. Command and orders

Use institution-native chains of command and existing Core order records. A military order identifies issuer/authority, recipient, objective, constraints, resources, timing, reporting and known context. Receipt, acknowledgement, interpretation, execution and report remain different facts when they matter.

Command includes planning, assigning means, coordination, evaluating received reports and sustaining personnel. Staff can prepare options and perform authorized administration. They cannot create absent information or make a superior's intent instantly known throughout the force.

For simultaneous demands, identify actual deadlines, dependencies and delegated responsibilities. Use real staffing and commitments; do not impose an arbitrary high-rank penalty or let one commander execute every staff task in zero time.

Delegated orders need qualified assignees, means and valid authority. NPCs act through their instructions, knowledge and motives. Reports can be delayed or mistaken. The player still chooses their own character's voluntary actions; strategic orders do not authorize invented follow-up decisions.

<a id="s08"></a>
## 8. Conduct, discipline and recognition

Record allegation, evidence, institutional finding and actual sanction separately. Identify applicable authority/practice, alleged conduct, witnesses, any supported response process and the resulting decision. Use the institution's own rules; no universal modern trial or appeal structure is imposed.

A failed combat roll is not misconduct by itself. Tactical success does not erase a supported inquiry. Unauthorized absence, desertion, leave, missing status and captivity remain distinct classifications.

Awards and honors require actual evidence, recommendation and authorized approval. Presentation and audience knowledge can occur later. A medal creates no universal competence bonus. Public reputation follows who learned what and how they interpret it under the selected social rules.

Institutional consequences change actual duties, authority, property or entitlements only through their recorded mechanisms. Do not infer forfeiture of wages or equipment solely from a label.

<a id="s09"></a>
## 9. Deployment, operations and return

Use applicable stages: warning/assignment, preparation, movement, arrival/orientation, operations, relief/rotation, return, recovery and review. Each has real commitments and completion conditions rather than automatic narrative transitions.

Preparation considers staffing, qualification, usable equipment, supply, communication, outstanding care and household arrangements. Readiness is for a named task and interval using the selected Core capability procedure. Missing prerequisites create limitations or feasible alternative plans, not compulsory cancellation or a universal readiness penalty.

Before an operation establish objective, authority, force, duration, known threats, provisioning, communications, recovery/withdrawal arrangements and credible exposure. Use the selected conflict/operation model and meaningful decision scale. This engine introduces no universal casualty rate or new combat formula.

Arrival grants no instant local intelligence. Relief requires actual custody, responsibility and information handover. Operations can affect civilians and continuing institutions while the protagonist is elsewhere; ordinary life does not freeze.

Afterward reconcile personnel status, ammunition, property, care, repair demands, reports, evidence and obligations through existing owners. Then process pay, correspondence, leave, disputes, household consequences and the next duty. Detailed scenes and aggregate reports must reference the same underlying outcomes.

Return is not automatic restoration of equipment, fatigue, wages or relationships. Recovery and reintegration are playable activities. Safety, quiet duty or retirement can continue without a compulsory larger threat.

<a id="s10"></a>
## 10. Pay, provisioning and issued property

The service profile determines pay accrual, due dates, actual receipts, lawful deductions, arrears, in-kind support and any relevant benefits. Use Core economic obligations and transfers. Entitlement is not spendable cash; approval is not receipt.

Define who supplies food, accommodation, clothing, transport, tools, animal care or other support. Actual military provision contributes to the same person/household need records. It does not duplicate consumption or satisfy dependants who never receive it.

Issued equipment records institution owner, actual custodian, assignment, condition, permitted use, return requirement and any stated liability. Personal, borrowed and issued property remain distinct. A recommendation or allocation at a depot does not give the character physical custody.

Requisition, authorization, allocation, dispatch, receipt, inspection and issue follow the selected logistics procedure. Requests and expected deliveries are not local stocks. Returning, transferring, losing or damaging issued property changes actual state once; contractual consequences depend on the service terms and institutional decisions.

This section adds military obligations and issue context. It supplies no second inventory, treasury, wage formula or universal compensation policy.

<a id="s11"></a>
## 11. Leave, restricted duty, missing personnel and captivity

### Leave and fitness

Record leave authority, period, conditions, destination/contact where relevant, travel commitments and return obligation. Leave approval is not arrival at home; travel and interruption consume actual time.

Practical function, medical assessment and institutional fitness classification remain distinct. Restricted duty must fit actual limitations and the selected care plan. A person unable to fight may still perform supported instruction or administration; neither full fitness nor total unemployment is automatic.

### Missing and captured personnel

Track actual location/custody separately from unit status and household knowledge. Missing does not prove death. Reclassification does not subtract a second person from headcount.

Captivity, missing status and recovery affect pay, dependants, issued property and service membership only under applicable terms and actual triggers. Do not initiate an estate transfer solely because contact was lost.

Recovery, exchange, ransom, escape and repatriation are setting-dependent processes requiring actual opportunity, authority, contacts, means and decisions. No exit is guaranteed. Recovered personnel may need care, assessment, debriefing, re-equipment and reassignment. Release is not a reset of wounds or duties.

<a id="s12"></a>
## 12. Household life during service

Maintain a support plan linked to actual service terms: ordinary contribution, military provision, remittance method, delivery delay, housing, care arrangements, dependants and contact channels. Departure can reduce household labor while changing income and consumption differently.

Remittances use actual economic transfers and delivery. Expected funds remain forecasts; arrival is not inferred from the sender's intention. Household reviews reconcile existing records rather than duplicate pay or consumption.

Letters/reports carry source, recipient, sending time, channel, actual receipt and revealed information. A family can face a practical shortage before learning its cause. Each person responds from their own knowledge, values and circumstances; no emotion, courtship or relationship outcome is imposed on the player.

Caregiving, civilian work, property management, education and personal promises remain valid commitments during service. A deployment does not erase family autonomy, private ownership or local institutions. Dependants are people with their own needs and rights, not a generic penalty attached to the soldier.

<a id="s13"></a>
## 13. Separation, retirement and succession

Separation can involve completed terms, discharge, transfer, resignation, retirement or another supported institutional route. Record effective time, authorizer, continuing duties/benefits, outstanding pay or claims, returned issued property and unresolved matters. No universal pension or guaranteed civilian employment is assumed.

Retirement changes military obligations and opens actual livelihood/personal choices. It does not end the life simulation or automatically remove condition and reputation history.

On death or an agreed protagonist transition, use the selected LIFE/estate and military appointment procedures. Preserve actual event time, recipient knowledge, independent successor identity, care needs, property custody, claims, institutions and pending work. Resolve dependants' support and the vacant military role under the applicable service arrangements.

A successor receives only actual transferred property or recognized responsibilities. They do not automatically inherit skill, command, private memories, intimate relationships or every debt. A successor need not be an invented child. Death need not destroy an institution with actual continuity arrangements; naming a successor alone does not create competence or recognition.

Historical human implementation retains permanent death. Fictional exceptions remain explicit modules with their own continuity rules.

<a id="s14"></a>
## 14. Military profile, content library and specialized modules

**Source selection:** `IRGS-MIL-LIB-1.0` (Military Content Library v1.0) is the current proposed military-specialization catalogue for this receiving edition. It retains 6 era tags and 12 category codes, 72 era/category candidates, 48 military-specific template candidates and 60 acceptance specifications. These templates are **not yet individually qualified** and must not be treated as automatic loadouts, equipment statistics or branch capability. The original `ML-0.1` index survives in the library's provenance folder, not as a concurrent item library.

Before dependent play, select only the fields needed for the actual campaign:

| Profile field | Required military meaning |
|---|---|
| Institution and service basis | Authority, eligibility, route of entry, terms and release |
| Organization | Native units/households, roles, rank, appointment, chain of command and jurisdiction |
| Duty | Roster, relief, reporting, standby and delegated authority |
| Qualifications | Training/assessment requirements, role permissions and relevant familiarization |
| Career | Review conditions, vacancies, promotions, transfers and specialization |
| Pay/support | Entitlement, payment, provision, remittance, benefits and equipment responsibility |
| Conduct | Applicable duties, allegations, adjudication and recognition processes |
| Deployment | Preparation, transport, communication, operating scale, relief and recovery |
| Equipment/branch | Actual issue and operating profiles, crew stations, maintenance/support and acceptance |
| People and continuity | Selected learning/condition/death models, household support and succession |

The equipment library's six groups remain **Antiquity, Early Centuries AD, Middle Ages, Early Modern, Contemporary and Science Fiction**. Use the preserved tags through SCL v1.0 §23 and Military Library v1.0: `ERA-ANT`, `ERA-EAD`, `ERA-MED`, `ERA-EMD`, `ERA-CON`, `ERA-SCI`. They filter content alongside actual region/date/branch or setting. They are not technology levels, automatic local availability or item statistics.

### Content binding

Resolve each selected definition by namespace, entry, exact version and any required mode selector under Core §§111–112 and SCL v1.0 §§3–6/24. A selected shared family uses its exact `SCL:<family-ID>@0.2` reference and readiness; the **SCL v1.0 catalogue name does not change a preserved `@0.2` family revision**. A held family retains exact compatible native payload/model; it does not become a complete generalized specification. The original source reference remains available when a compatible shared replacement is held or incomplete. SCL's older `CORE` provenance label is not this engine's rules parent; Core **v3.2** supplies current shared behavior.

Bind the definition to the institution's actual issue policy, enabled variant and compatible operating/effect profile. Keep weapon identity separate from its attack mode and compatible ammunition; retain protection construction, coverage, material and condition. Required mass, range, rate, cost or effect values come from the selected profile when consequential. The era index supplies none of them. A source Fantasy numerical entry retains its Fantasy-model dependency and cannot serve as historical equipment statistics through a shared alias.

Definition selection, local eligibility, institutional allocation, physical delivery and custody are separate gates. One actual issued object keeps its stable identity through references, scale changes and record views. A living mount remains an actor with its own needs; its tack and cargo remain separate asset/stock references. Neither the shared catalogue nor this engine creates a starting kit without an actual supported initialization or issue event.

### Branch activation

Specialized modules supply what generic Core interfaces cannot determine: vessel/seamanship operation, aircraft/spacecraft envelopes, particular weapons/effects, multi-operator links, neural strain, fictional automation or other genuinely additional mechanisms. Ordinary crews, stocks, condition and work continue through their existing owners.

Where a specialized pilot/link module uses them, preserve **long-term compatibility, current coordination/synchronization, interface stability and individual neural strain** as separate meanings. Strong synchronization does not cure instability or erase strain. Its selected profile supplies accumulation, triggers, consequences and recovery; these fields do not become historical human fatigue. Automation remains constrained by actual sensors, received information, delegated tasks and controls.

For A Scot’s Tale, retain actual historical canon, existing dice and human assumptions. For Iron Aegis, retain established d20, Mech/Kaiju and interface procedures. Neither reference is a current save supplied by this engine. No fixture values become a character's specification by attachment.

### Specialized library activation contract (v1.2)

For each `MIL` specialization, bind `(template_id, proposal_version, base_SCL_ref_if_any, allowed_mode_or_variant, branch/era/locality, actual means, operator/crew qualification, responsible authority, real asset/stock IDs, effect/condition/throughput profile, hazards, repair/support, acceptance evidence)`. Check source readiness **before** selection; a catalogue template may describe an eligible design while no actual capable object exists. A different SCL registry checksum requires comparing its exact referenced definitions, not silently accepting or rejecting the whole library.

Actual fielding requires compatible construction, personnel, ammunition/fuel, maintenance, infrastructure and institutional approval. A prototype is not an issue-ready stock item; procurement is not delivery; an operational rating does not become a separate physical resource. An incomplete technical envelope limits only the activity depending upon it. Future specialty modules may implement aircraft, naval vessels, orbital vehicles or neural interfaces without moving their native operating physics into Core or this general military-life workflow.

<a id="s15"></a>
## 15. Military records and running procedure

These are military workflow records and views within the Core owner register. They add service context and links; people, credentials, mandates, stock, wounds, money, work and knowledge retain their existing authoritative records. Use Core Appendix A's common fields: campaign-scoped ID, type/schema version, effective time, provenance, authority/status, visibility, record version and last applied event.

```text
SERVICE: id; actor_ref; organization/unit_ref; basis; agreement_ref;
         membership/mandate_refs; credential_refs; career_ref; duty_refs;
         pay/provision_refs; issue_refs; restriction_refs; exit_workflow_ref
ROSTER: id; service_ref; duty; commitment_ref; required_credential_ref;
        asset_refs; standing_order_ref; relief/handover_ref; report_trigger
QUALIFICATION: id; actor_ref; organization_ref; role/method_scope;
               learning/evidence_refs; assessor; credential_decision_ref; next_review
CAREER_REVIEW: id; career/service_refs; evidence_refs; eligibility; vacancy/need_ref;
               recommendation_ref; decision_ref; mandate/pay/duty_change_refs
DEPLOYMENT: id; objective/order_refs; actual_force_refs; capability_binding_ref;
            stage; commitment/work_refs; relief; recovery_refs; report_refs; next_trigger
ISSUE: id; asset_or_lot_ref; service/assignment_ref; receipt/transfer_refs;
       condition_assessment_ref; permitted_use; return/liability_terms
LEAVE/FITNESS: id; service_ref; authority/decision_ref; classification;
              condition/care_refs; commitment_refs; restrictions; return/review
PERSONNEL_STATUS_VIEW: id; roster_scope; as_of; actual_actor_refs;
                       availability_rule; reporting_authority; received_evidence_refs
CONDUCT: id; service_ref; INV_case_ref; applicable_procedure_ref;
         authority/decision_refs; executed_consequence_refs; report_refs
RECOGNITION: id; service_ref; evidence_refs; recommendation/approval_refs;
             presentation_event_ref; audience_report_refs
SERVICE_HOUSEHOLD_PLAN: id; service_ref; LIFE_household_ref; contribution/provision_refs;
                       care/remittance/housing/contact_refs; contingency; next_review
AFTERMATH: id; operation_ref; actual_loss/condition/stock_event_refs;
           care/repair/review_refs; pay/leave/support_refs; choices; next_duty
```

K-ORG holds actual membership, credential, mandate and institutional decisions. LIFE holds learning, career, household and successor workflows; ECO holds agreements/claims; INV holds conduct cases. Military deployment/issue/aftermath extensions hold their stage, objectives and links, with changes to shared facts submitted to the corresponding owner. A rendered rank, balance, location, fitness or casualty total is a view of those owners, never another mutable copy.

### Event subscriptions and completion

Subscribe to causal events under Core §§11/91. An event can change physical state, an institutional position or a recipient's knowledge at different times. Each reaction references its initiating event and records only its distinct military consequence.

| Trigger received by the workflow | Military consequence or request | Completion / next trigger |
|---|---|---|
| Effective enrollment, mandate or terms change | Update service links; request actual roster, pay obligation and issue steps | Separate assignment, settlement and delivery events |
| Duty begins/ends, relief arrives or duty is interrupted | Change applicable responsibility and handover state | Actual relief/handover, authorized continuation or new player decision |
| Qualifying training/assessment evidence is committed | Add military evidence to LIFE learning; request credential/career review | Actual institutional decision; next scheduled requirement if supported |
| Order/report is actually received | Update the recipient's knowledge; consider a feasible authorized response | Acknowledgement, execution or report under actual commitments |
| Injury, absence, capture, death or actual return | Recompute affected role availability; open supported care/relief/support work | Functional review, confirmed report or actual reassignment |
| Pay becomes due, is settled or a remittance arrives | Update the linked obligation/payment view and household support plan | Actual receipt or the next supported due/review event |
| Deployment stage completes or assets are accepted after work | Review the next stage or task-specific return to duty | Its actual prerequisites and authorization; no automatic advance |
| Conduct/award/exit decision becomes effective | Apply its scoped service consequences through the relevant owners | Actual execution, notification, property return or successor appointment |

No universal daily roll or review is added. The selected terms/profile schedules its real deadlines, training reviews and care checks. An interruption preserves actual completed work, costs and evidence. Leave ends under its approved interval/conditions; separation closes only the supported service duties and keeps outstanding claims, property and household matters active. Missing status stays unresolved until supported evidence changes it. A canceled deployment cannot erase completed movement, issue or exposure.

Maintain stable individual records for currently living named people and named animals, with important unnamed placeholders as required. Preserve canon, observations, provisional baseline ratings and unknowns distinctly. Deceased figures retain archival history rather than full active sheets.

For each meaningful scene: identify authorized duty or personal objective; consult actual orders, knowledge, condition and commitments; invoke the selected Core/adapter; link resulting events to the military record; reconcile only changed duties, entitlements or reports; return control when a new decision is required.

Use compact contextual presentation: a duty scene shows assignment, time, condition and next relief; command shows report age, force and decisions; home leave shows travel, obligations and relevant household state; aftermath shows actual changes and the next duty. Do not repeat complete databases in every reply.

<a id="s16"></a>
## 16. Source coverage, military acceptance and v3.2 receiving checks

### All v0.4 sections accounted for

| Source section | Slim treatment |
|---:|---|
| 1 Scope/play loop | Scope retained in §1; generic action loop referenced in §§2/15 |
| 2 Operating contract | Core/selected adapter reference; existing campaign rules and agency preserved |
| 3 Detailed life adoption | Historical dependency remains selected through §2.2; generic life workflows use LIFE |
| 4 Boundaries/standardization | Core v3.2 bindings and the deployment manifest in §2 replace the transitional patch route |
| 5 People/households/commitments | Generic owners referenced; military household context retained in §§4/12/15 |
| 6 Service/command, including 6.1–6.10 | Retained across §§3–13; no military workflow dropped |
| 7 Equipment/components | Shared dependency procedure referenced; issue and specialized platform profiles retained |
| 8 Operating resources/heat | Shared procedure referenced; profile-defined platform limits remain required |
| 9 Crew/interfaces | Shared staffing/control reference; branch stations and neural/other specialty remain scoped |
| 10 Repair/support | Shared work/acceptance reference; military availability/issue obligations remain |
| 11 Readiness/logistics | Shared task-capacity/stock/route reference; deployment preparation and supply issue remain |
| 12 Institutional learning | Core v3.2 §110 supplies the shared workflow; doctrine, instruction and fielding retained in §4 |
| 13 Operations/aftermath | Retained in §9, with selected conflict model and persistent personal consequences |
| 14 Retirement/succession | Military separation retained in §13; generic estate/continuity procedure referenced |
| 15 Records/presentation | Shared owner rules referenced; military link schemas retained in §15 |
| 16 Content/profiles | Generic inheritance referenced; military profile and six-era content retained in §14 |
| 17 Migration | Prospective, fact-preserving selection retained in §17 |
| 18 Fixtures/checks | Prior generic fixture remains original-source evidence; military-specific cases below |
| 19 Provenance/development | Retained in §17; specialized gaps remain explicit |

The ten expanded military-life workflows in source §6 remain individually traceable:

| Source subsection | Military section in this edition |
|---|---|
| 6.1 Service agreement and entry | §3 |
| 6.2 Duty roster and service day | §4, duty and handover |
| 6.3 Training establishment and qualifications | §4, training and qualification |
| 6.4 Comrades, mentors and culture | §6 |
| 6.5 Command as work | §7 |
| 6.6 Conduct, discipline and recognition | §8 |
| 6.7 Leave, restricted duty and absence | §11 |
| 6.8 Deployment cycle | §9 |
| 6.9 Household support during service | §12 |
| 6.10 Capture, missing personnel and dependants | §§11–12 |

### Military acceptance cases

| ID | Case | Required result |
|---|---|---|
| SML-01 | Recommendation/examination succeeds; appointment pending | Evidence retained; no automatic pay/rank/issue |
| SML-02 | Watch 08:00–12:00 overlaps training 10:00–14:00 | Two-hour conflict; actual relief or reduced training attendance |
| SML-03 | Relief does not arrive | Actual situation and institutional expectations presented; no invented voluntary follow-up |
| SML-04 | Promotion awarded | New authority/duties follow terms; no instant skill or relationships |
| SML-05 | Training qualification passed without current assignment | Qualification and actual duty remain distinct |
| SML-06 | Order issued before receipt | Subordinate acts from actual received knowledge |
| SML-07 | Tactical failure triggers allegation | Failure alone is not a misconduct finding |
| SML-08 | Heroic action recommended for an award | Recommendation, approval, presentation and reputation remain separate |
| SML-09 | Five qualifying days at 2 units/day; 6 paid | Entitlement 10, received 6, outstanding 4 |
| SML-10 | Sender remits 3 of the received 6; delivery pending | Sender 3 available; 3 in transit; household has not received it |
| SML-11 | Unit provides food to a soldier | Same person is not charged another identical household meal |
| SML-12 | Equipment allocated but not physically issued | No custody/loadout change until actual receipt |
| SML-13 | Two-day leave includes a one-day outbound journey | Actual remaining time reflects travel; return journey still needs accounting |
| SML-14 | Injury restricts combat but permits defined instruction | Appropriate restricted work remains possible within care requirements |
| SML-15 | Ten people; one wounded unavailable, one missing, later captured | Eight available, one wounded, one captured; total ten |
| SML-16 | Household hears no news of missing person | Actual absence can affect support; death/estate not inferred |
| SML-17 | Unit returns from deployment | Repairs, recovery, payment and personal reintegration remain actual tasks |
| SML-18 | Veteran retires | Actual service terms govern property/benefits; civilian life continues |
| SML-19 | Protagonist dies and control changes | World persists; successor has independent skill/knowledge and actual transfers |
| SML-20 | Deployment proposes another Core without a complete compatibility bridge | Retain the established affected implementation; resolve the bridge before dependent use; independent known activity continues |
| SML-21 | Shared alias names a weapon but omits its required mode or incompatible model | Preserve the exact complete source/selector/model; no favorable stat conversion or source deprecation |
| SML-22 | A previously applied pay/issue event is delivered again | Identical scoped payload is a no-op; a changed payload under that applied ID is a conflict; no duplicate property or settlement |
| SML-23 | A d20 campaign attaches optional d100 military modifiers | No automatic conversion; keep a complete compatible selected adapter or explicitly resolve the bridge |
| SML-24 | Doctrine revision approved; one unit has not received instruction or training | Approval is retained; the unit gains no unlearned method or unissued capability |
| SML-25 | A capture occurs before the unit receives its report | Actual custody changes once; each roster uses its authority's knowledge; later receipt does not remove another person |
| SML-26 | A variant explicitly marks a consequential inherited value unknown | Preserve unknown for that variant; no fallback to the parent value, zero or unlimited; supported independent activity continues |
| SML-27 | A profiled platform interlock blocks an activation | No ammunition/energy charge for the blocked activation; actual preparation remains spent; any override needs an actual choice and defined consequences |
| SML-28 | Save/load occurs after an order is received but before a new player choice | Preserve receipt, commitments, retained uncertainty and pending events; no replay or invented voluntary action |
| SML-29 | Another unit has an authorized standing duty while the protagonist is elsewhere | Actual qualified off-screen work proceeds within means and knowledge; no protagonist-triggered world freeze |
| SML-30 | A successor acquires property after a veteran's death | One actual transfer preserves wear/history; debts, military office and private knowledge use their separate supported processes |

These are acceptance requirements for the selected deployment. Verification below records only checks actually executed for this source edition. It does not represent execution of all thirty behavioral cases in a complete game runtime.

**Historical v1.0 evidence (not rerun merely by copying):** Seventeen sections and navigation anchors; nineteen sequential source-section dispositions; ten source §6 workflow dispositions; thirty unique sequential acceptance-case IDs; table widths and code fences; Core section/appendix references; SCL sections and six era tags; nine owner names and the manifest/interface meanings. The illustrated duty overlap, entitlement/remittance, leave and current headcount arithmetic were also checked. These checks passed.

**Historical v1.0 bounded reference trace (not a new v1.2 execution):** A synthetic service/pay/support fixture exercised accrual versus settlement, finite funding, remittance in transit, actual delivery, duplicate-event replay, changed-payload conflict and continuation from a checkpoint. A separate personnel/report fixture exercised actual capture versus delayed roster knowledge and one-person reclassification. Both passed their stated invariants. Fixture rates and identities are test inputs, not campaign defaults. These reference traces test a small written interpretation of Core v3.0 plus the original v1.0 engine, rather than a production implementation.

**Still required for a selected deployment:** Applicable behavioral cases under its actual institutional, combat/condition, learning and branch profiles; independent reconstruction of its next legal action from persisted state; and recorded live play. Numerical balance and historical/technical calibration require their own scoped evidence. Prior fixture counts do not satisfy those gates.

### New receiving acceptance conditions (v1.2)

| ID | Probe | Required outcome |
|---|---|---|
| M32-01 | Select Core v3.2 and library v1.0 with v1.0 historical engine still on record | New source binding only; no implicit campaign migration |
| M32-02 | 14 original military SCL exemplars against current R2 registry | Identity, type, readiness and selector match despite different snapshot SHA |
| M32-03 | Held weapon definition offers unsupported performance | Return unresolved for dependent numeric outcome; preserve exact source adapter |
| M32-04 | Two orders issued simultaneously use one qualified operator | Actual staffing conflict resolved through time/capacity before either commits |
| M32-05 | Shipment request, authorization and issue | No custody/stock change without delivery and handover |
| M32-06 | Duplicate pay/issue event ID | Identical payload no-op, conflicting payload rejected |
| M32-07 | Wound, missing-person report, delayed capture classification | One person, one actual location/condition, independent report knowledge |
| M32-08 | Approved doctrine not yet trained/issued | No fielded capability until actual learning, issue and authorization |
| M32-09 | Historical training and Fantasy TU references | One selected compatible schedule; actual hours preserved and not silently converted |
| M32-10 | SCL base family plus MIL specialization | No double stock, no extra attacks, no duplicate effect accounting |
| M32-11 | Save/restart before a pending PC decision | Preserve resource/event frontier and open choice; no automated voluntary action |
| M32-12 | Military phase skipped to long-term review | Already spent resources and incurred injuries persist, off-screen qualified work continues |
| M32-13 | Platform unsupported with missing model envelope | Block that action only, not unrelated life/duty activity |
| M32-14 | Attempt 48 proposed templates as immediately usable real items | Reject auto-activation; require each definition's profile/qualification and actual instance |

**Evidence status:** Structural preservation/receiving tests and small independent synthetic probes executed by the accompanying verifier only where stated in its report. The full SML-01–30 and M32-01–14 scenarios are **acceptance requirements**, not a claim of 44 executed live gameplay tests. Library acceptance cases are likewise separate specifications.

<a id="s17"></a>
## 17. Adoption, provenance and prospective migration

### Release meaning and authority

This v1.2 is the **proposed Core v3.2 receiving source** for the complete military-life specialization of Slim v1.0; it preserves the detailed sections on entry, daily service, qualification, command, relationships, conduct, operations, property, captivity, households and career closure without modifying their mechanics. The existing Core v3.2 `MILITARY` binding remains the shared provider and is not altered. Earlier Core v3.0 and v3.1 receipts remain historical provenance, not parallel active rule stacks.

`IRGS-MIL-LIB-1.0` is a **proposed replacement** of the equipment-era index in this edition's content references, with explicit qualification gates; its 48 templates remain unqualified and not silently adopted. SCL v1.0 preserves per-entry `@0.2` identities and their readiness/holds. An actual campaign's established edition continues until its explicit authority selects prospective replacement.

### Provenance and source disposition

| Source | Role and treatment |
|---|---|
| Soldier/Military Life Slim v1.0 | Primary 17-section military specialization; §§3–13 and §15 preserved exactly; §§2/14/16/17 reconciled, not erased; original snapshot included |
| Military Life Simulation Engine v0.4 and Slim v0.5 | Predecessor scope and military workflows as cited by v1.0; not an extra runtime provider |
| Core Engine v3.2 / Full Release R2 | Inherited shared ownership, records, runtime, domains, content and receiving §§111–112 |
| IRGS Engine Bindings v3.2, `MILITARY` | Source-identical general provider contract; slim-specific manifest adds local records and triggers |
| Shared Content Library v1.0 | Current normative catalogue with per-definition readiness and preserved family revision IDs |
| Military Content Library v1.0 | Proposed 6×12 era/category index, 48 specialization templates, 60 acceptance specifications; entire original package preserved |
| Military Equipment and Technology Library v0.1 | Archived and traceable seven-section era/source index; not competing active values |
| Historical Life and Military Career v0.3 | Optional complete human implementation **only when separately selected and available** |

### Existing campaigns and effective cutover

No automatic migration. Record the old effective profile/parent, saved event frontier, actual actors, offices, term claims, monetary holdings, property/custody, ammunition/fuel/food, injuries, recovery, learning hours, issued orders, movements, messages in transit, incomplete work, and all pending player decisions. Compare old and new meanings field by field. Resolve any outcome-changing differences by an explicit prospective decision, with qualified model source/effective time and a non-duplication invariant. Existing past time, casualties, wages, repairs, awards, promotions, judgments and received knowledge stay past facts unless a separately authorized correction is made.

### Outstanding calibration and validation

The engine remains dependent on selected service organizations/branches, dated technology, actual equipment/operating envelopes, medical/physiology and morale submodels. All thirty native SML acceptance cases and fourteen new receiving cases need contextual execution; the library's sixty specifications need applicable technical profiles. Live gameplay, long-term historical calibration, ordnance/vehicle envelope accuracy and independent state reconstruction remain unproven by a source integration build.

<a id="s18"></a>
## 18. Operational five-gate playability contract — inherited from v1.1

**Status:** Proposed receiving clarification. This section introduces no second Core scheduler, generic injury ledger, genre dice system, or universal military statistics.

| Gate | Required enabled military inputs | Result of passing the gate |
|---|---|---|
| P1 Campaign initialization | Core3.2/this engine + selected content, region/era, service institution and native rank/terms, actual character, place, time, duty/decision, conditions, equipment and actual issue | A valid decision point with no assumed enrollment, gear or consent |
| P2 Executable action | Duty/entry/assignment/order authority, feasible method, trained capability, commitments, means, declared consequences and one selected compatible resolution/effect profile | Actual work/response and costs apply through Core once |
| P3 Complete relevant models | Selected character/learning, needs/fatigue, combat only if enabled, specific equipment and injury/care, branch/platform only if needed, legal/institutional terms | Missing consequential models prevent **only that activity**; ordinary duty continues |
| P4 Persistent runtime | Stable people, location and custody, pay/claims, issue, reports, roster, actual time, knowledge and autonomous unit/household tasks | Save/review/scale changes neither refill nor replay |
| P5 Full gameplay loop | Entry or duty → preparation → performance/incident → result → received report → pay/care/leave/reassignment → next player choice | A playable *bounded service/life* activity, not certified universal combat |

### Controlled deployment fixture (synthetic, not historical canon)

At 08:00 an assigned watch ends at 12:00; training is offered for 10:00–14:00. The actual roster has no preauthorized relief. The overlap is **two hours** and therefore at most two unconflicted training hours remain without a real authorized resolution of the conflict. Another existing person is later captured, changing their actual physical availability once. The parent unit learns on report receipt, not at capture time. A delayed or replayed report never creates a second person or removes one again. The protagonist chooses whether to seek relief, not the engine.

These fixtures exercise only shift arithmetic and knowledge/personnel continuity. Service law, pay rates, injury figures, branch technology and the content of the protagonist's decision are **not** supplied by this fixture.

**Required prospective deployment selection:** `IRGS-CORE-3.2` + `IRGS-BIND-MILITARY-3.2` + `IRGS-MLS-SLIM-1.2` + `IRGS-SCL-1.0` + `IRGS-MIL-LIB-1.0` (with exact profile and content gating) + specific service/physiology/equipment profiles. Source v1.0 and its Core3.0/SCL0.1 pin remain unaltered for existing deployments.

<a id="s19"></a>
## 19. Historical v1.1 CMRR receiving reconciliation (provenance)

> This section records the v1.1/Core v3.1 comparison and its limitations as previous source evidence. Core v3.2 and the new library receiving decisions are authoritative **within this proposed v1.2 edition** in §20. Historical v1.1 descriptions do not select previous versions for current deployment.

| Scope | Earlier v1.0 treatment | Complete v1.1 treatment | Evidence/status |
|---|---|---|---|
| Shared parent | Explicit Core3.0 pin | Core3.1 selected for new deployment under its Military binding | Source locator verified; candidate not automatically adopted |
| Content registry | Proposed SCL0.1 | Confirmed v0.2 immutable references; SCL1.0 opt-in only | Reference/name gate only; no invented item stats |
| Military duties and lives | Native sections 3–13 | Retained intact | Full source text retained except documented receiving references |
| Service records/runtime | Native §§14–15, linked to Core | Same records, Core3.1 authoritative owners | No duplicate staffing or stock |
| Historical numerical alternatives | Conditional profiles | Remain conditional; no conversion from d100 to d20 by label | Calibration outstanding |
| Existing test evidence | v1.0 Core3.0 fixture | Preserved as inherited evidence; v1.1 bounded fixture separate | Not an independent long campaign playtest |

**Accounted removals:** Obsolete active Core3.0/SCL0.1 receiving pins are replaced **in this new edition only**; predecessor files and campaigns retain them. No unique military-life workflow, record, term, rank, profile, or method is deleted. No arbitrary service benefits or extra resources are added.

**Regression:** Check watch/training conflict; capture versus report receipt; arrears/remittance; equipment allocation versus custody; training versus credential; order versus receipt; independent household life; institutional authority; replay; scale continuity; intentional retirement. Other behavioral cases in §16 remain specified requirements, not presumed executed for v1.1.

**Open:** Full 3.1 runtime integration, independent runner persistence, branch equipment and tactical selection, economic/medical/physiological calibration, actual interactive campaign evaluation. The new candidate makes bounded service life testable but does not certify unrestricted military play.

**Migration:** None executed. A campaign pinned to v1.0/Core3.0/SCL0.1 remains there until explicit prospective adoption and source-correct record/alias migration. Preserve actor, claims, property, duty, medical state, queues and received information; a rebinding never provides new pay, repairs, training or equipment.
<a id="s20"></a>
## 20. CMRR complete reconciliation and receiving verification

### Bidirectional section disposition

| Original military section | Current disposition | Shared / specialized decision |
|---|---|---|
| v1.0 §1 | Retained text verbatim | Military life scope/agency remains native |
| v1.0 §2 | Rebuilt for v3.2 | Core §112 providers and Appendix B/D corrected |
| v1.0 §3 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §4 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §5 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §6 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §7 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §8 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §9 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §10 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §11 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §12 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §13 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §14 | Retained and updated with explicit receiving constraints | MIL v1.0 specialized templates and exact SCL readiness |
| v1.0 §15 | Retained text verbatim | Native military workflow remains with Core owner references |
| v1.0 §16 | Retained and updated with explicit receiving constraints | Native SML-01–30 retained; M32-01–14 added |
| v1.0 §17 | Rebuilt for v3.2 | Prospective adoption/migration with exact provenance |

### Conflict and change register

| Item | Source conflict | Decision | Why |
|---|---|---|---|
| CMRR-01 | v1.0 Core 3.0 reference | Rebind to Core 3.2 `MILITARY` contract, no copied Core logic | Prevent duplicate owners/runtime |
| CMRR-02 | Core appendix reshuffle | Use A owner, B deployment, C cases, D optional profiles | Prevent false reference/fallback |
| CMRR-03 | v1.0 SCL 0.1 and equipment index | Use SCL 1.0 and military library 1.0 exact versions | Current catalogue without invented equipment |
| CMRR-04 | Library snapshot SHA differs from current SCL R2 | Preserve snapshot; separately verify all 14 exact identity/type/status/selector fields | Byte change ≠ content promotion |
| CMRR-05 | 48 new military candidate templates lack qualification | Remain proposed; no automatic assets or quantitative effects | Avoid phantom capability |
| CMRR-06 | Physical items vs weapons/modes vs service templates | Core §111 typed references; single actual asset instance | Avoid item/effect duplication |
| CMRR-07 | Historical/Fantasy/d20/d100 profiles overlap | Select complete compatible model per cause; no bonus-scale conversion | Avoid double modifiers and mixing mechanics |
| CMRR-08 | Cohort ratings and individual casualty counts | Core K-ACTOR/K-POP single source with actual reports | Avoid duplicate casualties |
| CMRR-09 | Original v1.0 military §§3–13 and §15 | Retain unchanged | Preserve all unique military-life procedures |
| CMRR-10 | SML-01–30, MCL-01–60 vs executable evidence | Preserve acceptance specifications; bounded tests reported separately | No false claim of playtesting |
| CMRR-11 | New Core release vs campaigns in progress | Prospective adoption with exact effective scope/time | No automatic migration, recovery or refunds |

### Verification and ownership

The release verifier compares the original source's §§3–13 and §15 byte-for-byte after section extraction, audits IDs, validates Core/Library versions and all 14 exemplar SCL semantics, checks package hashes and exercises synthetic resource and event-invariant fixtures. Every fixture states its inputs and limitations. The native v1.0 source and the complete Military Library v1.0 original files are preserved. **Passed checks mean the stated properties, not blanket numerical calibration or continuous live play.**

