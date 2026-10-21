# IRGS — Soldier and Military Life Simulation
## Slim Engine v1.0

**Document ID:** IRGS-MLS-SLIM-1.0  
**Date:** 13 October 2026  
**Source editions:** Military Life Simulation Engine v0.4; Soldier/Military Slim v0.5.  
**Status:** Final source edition for the reviewed military/life scope. Design acceptance, campaign adoption and validation retain their separate recorded status.  
**Purpose:** Play a continuing personal life in military service, through ordinary duty, training, operations, career change, recovery, separation and later generations.  
**Pinned parent:** IRGS-CORE-3.0, *IRGS_Core_Engine_v3_0_Integrated.md*, integrated edition dated 13 October 2026. Its header remains Proposed; this engine does not change that status.  
**Content reference:** IRGS-SCL-0.1, *IRGS_Shared_Content_Library_v0_1_Proposed.md*, with entry status retained; Military Equipment and Technology Library v0.1 supplies the era/category index.  
**Activation dependencies:** Explicitly selected institutional, equipment, resolution, learning and physiology/needs/recovery profiles where the activity requires them.

This edition retains the military-specific workflows from v0.4. Shared clocks, inventories, projects, component dependencies, generic service capacity and life/estate machinery are referenced through their owning Core procedures. Military terms, duties, rank, appointment, command, discipline, deployment and branch practice remain here or in the selected service profile.

Finalization closes the transitional Core bindings and military workflow specification within the reviewed v0.4 scope. The integrated parent supplies the shared procedures directly; earlier Core patches are provenance. The source edition can be selected for a deployment once its applicable profile and compatibility gates are met. Publication advances no campaign time and certifies no historical accuracy, equipment performance or live-play balance.

### Navigation

1. [Scope and authority](#s01)
2. [Core bindings and retained profiles](#s02)
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
14. [Military profile and specialized modules](#s14)
15. [Military records and running procedure](#s15)
16. [Source coverage and acceptance cases](#s16)
17. [Adoption and provenance](#s17)

<a id="s01"></a>
## 1. Scope and authority

The central actor is a person with a life, responsibilities and relationships. Combat, command and advancement are possible activities, not compulsory destinations. A recruit, retainer, ordinary soldier, technical specialist, operator, commander or retired veteran can be a legitimate protagonist. Other careers remain available through the selected life procedures.

Use institution-native roles. Rank, office, personal skill, qualification, service membership and current assignment are separate facts. A commission does not create mastery; a recommendation does not complete enrollment; a victory does not repair equipment or settle personal obligations.

Authority remains current explicit user direction → established campaign rules/overrides → adopted procedures within their scope → selected Core → a scoped ruling in an unresolved gap. Player agency, autonomous NPCs, actual time, limited knowledge and persistent consequences remain inherited. OOC work advances no time.

A Scot’s Tale and Iron Aegis are complementary design references. Their people, current state, technology and specific institutions are not universal starting content. Historical human play retains its selected real-world limits and permanent death. Fictional campaigns supply any exceptional capabilities through explicit modules.

<a id="s02"></a>
## 2. Core bindings and retained profiles

### 2.1 Shared procedures used by reference

All references in this table name **Core v3.0**. The nine owner labels and domain boundaries have their exact meanings in Core Appendix A. Military procedures apply those interfaces to the service context.

| Shared function | Authoritative owner / Core v3.0 locator | Military application |
|---|---|---|
| Action, uncertainty, agency and runtime | Core §§4–9, 90–91 | Duty, personal activity and command use the same action/commit contract |
| Time, commitments and received information | K-TIME/K-INFO; Core §§10–13, 30, 85–86 | Rosters, handovers, order receipt and reports |
| Capability, learning, conditions and recovery | K-ACTOR/LIFE/MED; Core §§14–19, 31, 43, 96, 118, 122 | Military training and duty fitness read the selected models |
| Agreements, claims, pay and actual transfers | ECO/K-STOCK; Core §§12, 24, 38, 114 | Service entitlements, settlement and remittance |
| Stock, custody, handling and supply | K-STOCK/K-ASSET; Core §§20–22, 35–37, 105 | Requisition, issue, loadout and return of property |
| Asset configuration, components and crew | K-ASSET/K-ACTOR/K-ORG; Core §§21, 55–57, 101 | Equipment, stations and supported substitutions |
| Operating resources, output and burdens | K-STOCK/K-ASSET/K-NET; Core §109 | Actual branch profiles supply units, rates and limits |
| Work, repair, care and accepted return | K-WORK/MED; Core §§23, 43, 73, 96, 108, 118 | Repair/care completion and later duty assignment remain distinct |
| Organization, authority, credentials and accountability | K-ORG/GOV/INV/LIFE; Core §§25–29, 39–46, 107, 113, 115, 122 | Native rank, appointment, command and military procedure |
| Task capability, routes and delivered support | K-NET with stock/actor/asset references; Core §§35–36, 41, 101–103, 108 | Deployment readiness and sustained support |
| Institutional learning and fielding | K-ORG/K-WORK/K-INFO; Core §110 | Doctrine review, approval, instruction and actual adoption |
| Operations, scale and casualty views | Core §§42, 47–63, 106; K-POP only for residual cohorts | Unit operations read the same people and losses as individual scenes |
| Households, ordinary life and succession | LIFE/ECO/K-ORG; Core §§64–71, 76, 114, 122 | Service support, civilian life, estates and vacant offices |
| Content, initialization and compatibility | Core §§79, 88, 97, 111–112; Appendices A/C | Exact definitions, supported instances and prospective mappings |

The v0.4 shared paragraphs are source history for this v3.0 binding, rather than an additional runtime provider. Core §112's Military Life bridge covers commitments, dependencies, resources, work, readiness, productive support and institutional learning. Selecting this engine selects that ownership arrangement within the deployment's recorded scope.

A deployment using another parent edition needs an explicit compatibility bridge identifying complete equivalent procedures and preserved meanings. Until that bridge is complete, retain its existing adopted engine for affected functions. An unresolved outcome-changing parameter needs a supported profile or named prospective ruling before the dependent calculation; independent known activity continues under Core §112. A new Core publication does not change this version pin automatically.

### 2.2 Specialized selections preserved

| Selection | Retained meaning |
|---|---|
| Resolution/conflict | Select one complete compatible adapter under Core §§5–9/112. Core §6 supplies the d100 reference; established d20 or other campaign adapters keep their actual scope |
| Human historical implementation | Selected Historical Life and Military Career v0.3 creation, needs, learning, load, injury, care and context procedures remain profiles/dependencies, not silently universal Core values |
| Progression | Actual qualifying hours and demonstrations survive; Historical and Fantasy TU schedules do not convert by name |
| Conditions/recovery | One compatible model and recovery plan per condition; duty fitness reads its result |
| Morale/cohesion/suppression | Core §§32–34 supply shared meanings. Select a supported military implementation; Core Appendix F3–F5 preserves optional military tracks and values. These never become affection or civilian recognition |
| Platform effects | Select actual weapon/protection/component/hull/interface profiles; generic asset records do not supply naval flight, spaceflight or neural mechanics |
| Local service institutions | Pay, eligibility, rank, justice, leave, benefits and exit terms come from the chosen service profile |

The v0.4 powered-carrier values were neutral test inputs, not military platform specifications. They stay as source test evidence, not active values in this engine or the Core.

For the optional Historical v0.3 implementation, retain the selected source procedures and their status: §3 character creation; §5 human needs/deficits; §8 learning and familiarity; §14 optional load; §§15–17 tactical effects, injury and care; §§19–20 household, aging and succession context. Its numerical creation, training, load and recovery defaults remain provisional game abstractions. This slim edition does not silently accept or recalibrate them.

Core Appendix F1/F2's optional human modifiers/fatigue and the Historical profiles are alternative or explicitly reconciled selections where they represent the same cause. Record the actual source, version, scope and calculation order. Preserve qualifying hours and earned competence; do not merge Historical and Fantasy TU schedules, duplicate fatigue/load penalties or run two care counters. A numerical military morale track requires a compatible modifier adapter; d100 reference modifiers do not become d20 bonuses by renaming them.

### 2.3 Deployment manifest

Use Core §112 and Appendix C's manifest contract. Complete only fields consequential to the selected play; a field marked unknown supplies no hidden default. This is a template, not an initialized campaign.

```text
engine: IRGS-MLS-SLIM-1.0
core: IRGS-CORE-3.0
design/adoption/validation: separately recorded scope and evidence
services: K-TIME, K-ACTOR, K-INFO, K-ORG; stock/assets/work/net as used
domains: LIFE and ECO for service/life; MED, INV, GOV and others as used
cohort_model: K-POP + exact aggregation profile only when residual cohorts are used
institution_profile: exact ID/version; section 14 selections and unresolved fields
profiles: resolution, effects/protection, physiology, needs, load, recovery,
          learning, military willingness/coordination/threat; exact source/scope
branch_modules: exact versions, additional mechanisms, activation prerequisites
content: library/entry/version/selector; entry status; eligible variant; adapter
interfaces: authoritative owner references; section 15 workflow links
triggers: section 15 event subscriptions; no additional military clock
parameters: meaning, unit, source/status, bounds, limits and missing values
termination: terms, release/cancellation, interruption, recovery and next review
overrides/migration: affected behavior, effective scope/time, mappings, snapshots
acceptance: applicable section 16 cases, observed evidence and unresolved defects
```

For ordinary individual service, only active shared records and domains are needed. Medical work activates MED; a conduct case uses INV; public appointments use GOV where applicable. Naval operation activates MAR plus an actual vessel/envelope profile. A formation activates K-POP only for its residual people and keeps named members in K-ACTOR. No deployment must initialize all eleven domains, every equipment era or a numerical model for every field.

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
## 14. Military profile and specialized modules

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

The equipment library's six groups remain **Antiquity, Early Centuries AD, Middle Ages, Early Modern, Contemporary and Science Fiction**. Use the preserved tags through SCL §23: `ERA-ANT`, `ERA-EAD`, `ERA-MED`, `ERA-EMD`, `ERA-CON`, `ERA-SCI`. They filter content alongside actual region/date/branch or setting. They are not technology levels, automatic local availability or item statistics.

### Content binding

Resolve each selected definition by namespace, entry, exact version and any required mode selector under Core §111 and SCL §§3–6/24. A proposed `SCL:<entry-ID>@0.1` retains its proposed import status. The original source reference remains available when no complete compatible shared replacement has been selected. SCL's older `CORE` provenance label is not this engine's rules parent; Core v3.0 supplies current shared behavior.

Bind the definition to the institution's actual issue policy, enabled variant and compatible operating/effect profile. Keep weapon identity separate from its attack mode and compatible ammunition; retain protection construction, coverage, material and condition. Required mass, range, rate, cost or effect values come from the selected profile when consequential. The era index supplies none of them. A source Fantasy numerical entry retains its Fantasy-model dependency and cannot serve as historical equipment statistics through a shared alias.

Definition selection, local eligibility, institutional allocation, physical delivery and custody are separate gates. One actual issued object keeps its stable identity through references, scale changes and record views. A living mount remains an actor with its own needs; its tack and cargo remain separate asset/stock references. Neither the shared catalogue nor this engine creates a starting kit without an actual supported initialization or issue event.

### Branch activation

Specialized modules supply what generic Core interfaces cannot determine: vessel/seamanship operation, aircraft/spacecraft envelopes, particular weapons/effects, multi-operator links, neural strain, fictional automation or other genuinely additional mechanisms. Ordinary crews, stocks, condition and work continue through their existing owners.

Where a specialized pilot/link module uses them, preserve **long-term compatibility, current coordination/synchronization, interface stability and individual neural strain** as separate meanings. Strong synchronization does not cure instability or erase strain. Its selected profile supplies accumulation, triggers, consequences and recovery; these fields do not become historical human fatigue. Automation remains constrained by actual sensors, received information, delegated tasks and controls.

For A Scot’s Tale, retain actual historical canon, existing dice and human assumptions. For Iron Aegis, retain established d20, Mech/Kaiju and interface procedures. Neither reference is a current save supplied by this engine. No fixture values become a character's specification by attachment.

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
## 16. Source coverage and acceptance cases

### All v0.4 sections accounted for

| Source section | Slim treatment |
|---:|---|
| 1 Scope/play loop | Scope retained in §1; generic action loop referenced in §§2/15 |
| 2 Operating contract | Core/selected adapter reference; existing campaign rules and agency preserved |
| 3 Detailed life adoption | Historical dependency remains selected through §2.2; generic life workflows use LIFE |
| 4 Boundaries/standardization | Core v3.0 bindings and the deployment manifest in §2 replace the transitional patch route |
| 5 People/households/commitments | Generic owners referenced; military household context retained in §§4/12/15 |
| 6 Service/command, including 6.1–6.10 | Retained across §§3–13; no military workflow dropped |
| 7 Equipment/components | Shared dependency procedure referenced; issue and specialized platform profiles retained |
| 8 Operating resources/heat | Shared procedure referenced; profile-defined platform limits remain required |
| 9 Crew/interfaces | Shared staffing/control reference; branch stations and neural/other specialty remain scoped |
| 10 Repair/support | Shared work/acceptance reference; military availability/issue obligations remain |
| 11 Readiness/logistics | Shared task-capacity/stock/route reference; deployment preparation and supply issue remain |
| 12 Institutional learning | Core §110 supplies the shared workflow; doctrine, instruction and fielding retained in §4 |
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

**Executed source checks:** Seventeen sections and navigation anchors; nineteen sequential source-section dispositions; ten source §6 workflow dispositions; thirty unique sequential acceptance-case IDs; table widths and code fences; Core section/appendix references; SCL sections and six era tags; nine owner names and the manifest/interface meanings. The illustrated duty overlap, entitlement/remittance, leave and current headcount arithmetic were also checked. These checks passed.

**Executed bounded reference trace:** A synthetic service/pay/support fixture exercised accrual versus settlement, finite funding, remittance in transit, actual delivery, duplicate-event replay, changed-payload conflict and continuation from a checkpoint. A separate personnel/report fixture exercised actual capture versus delayed roster knowledge and one-person reclassification. Both passed their stated invariants. Fixture rates and identities are test inputs, not campaign defaults. These reference traces test a small written interpretation of Core v3.0 plus this engine, rather than a production implementation.

**Still required for a selected deployment:** Applicable behavioral cases under its actual institutional, combat/condition, learning and branch profiles; independent reconstruction of its next legal action from persisted state; and recorded live play. Numerical balance and historical/technical calibration require their own scoped evidence. Prior fixture counts do not satisfy those gates.

<a id="s17"></a>
## 17. Adoption and provenance

### Release and selection

This v1.0 supersedes v0.5 as this workshop's Soldier/Military slim source reference. It preserves the nineteen-section v0.4 scope and its military-life expansion, while binding shared functions directly to IRGS-CORE-3.0. The original engine and numerical/profile sources remain available as provenance and compatible selected implementations within their actual scope.

For a deployment, select the exact parent, this edition, content and applicable profiles through §2.3. Record actual design acceptance, adopted scope/effective time and validation evidence separately. Core v3.0 and SCL v0.1 keep their own published Proposed statuses unless accepted through their respective authorities. This source finalization changes neither.

An older parent is supported only by a declared complete compatibility bridge; it is not an automatic fallback for this v3.0 edition. Once a bridge is selected, the corresponding generic v0.4 paragraphs are applications/references to Core. Retained specialty profiles supply their additional meanings and values, without becoming a second shared engine.

### Existing campaigns

For an ongoing campaign, preserve the last valid snapshot and decision point, actual actors/assets, earned competence, conditions, quantities, knowledge, terms and obligations. Map military records by stable ID without advancing time. Resolve outcome-changing incompatibilities under existing authority. Resume prospectively with no free healing, repair, promotion or payment.

### Provenance and remaining module work

| Source | Role in this edition |
|---|---|
| Military Life Simulation Engine v0.4 | Primary scope and military procedures, especially §6 and §§13–14; all nineteen sections accounted for in §16 |
| Soldier/Military Slim v0.5 | Prior slim organization and the first twenty acceptance requirements |
| IRGS Core Engine v3.0 Integrated | Pinned shared provider: §§1–123 and Appendices A/C; optional scoped reference profiles in Appendix F |
| IRGS Shared Content Library v0.1 Proposed | Reference identity/composition and era/equipment descriptors; proposed entry status retained |
| Military Equipment and Technology Library v0.1 | Six era groups and twelve catalogue categories; no numerical item specifications |
| Historical Life and Military Career v0.3 | Selected historical creation, needs, learning, load, tactical/injury/care and continuity profiles |
| Library/Engine Extractions v0.1, CDI 0.2 and Pass A/B/C | Reconciliation history incorporated into the integrated parent; no separate runtime dependency imposed by this engine |

This edition does not reread or migrate current A Scot’s Tale/Iron Aegis campaign state. Branch-specific naval, aerial, space and interface procedures remain specialized development work. Historical calibration, particular institutions, equipment specifications and long-duration campaign playtests remain profile/module tasks.

The original twelve shared contracts are supplied through the integrated parent and explicit content/profile bindings. The retained military engine concentrates on the person, their service institution and the consequences of military life.

**v1.0 changes:** Replaced the temporary patch/fallback bindings with Core v3.0 locators; added the complete deployment manifest and owner/event interfaces; made shared-content and era selection explicit; restored explicit doctrine/fielding context; preserved all source military-life workflows; added ten compatibility/persistence cases and fresh bounded verification. No new universal equipment, combat, pay, training or physiological numbers were introduced.
