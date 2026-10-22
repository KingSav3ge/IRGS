<!-- Readable transcription of the uploaded v0.4 DOCX. Original formatting and embedded document metadata remain in provenance/rise/. This is source design material; requirement status is preserved. -->

# The Rise of... You

IRGS Settlement Campaign Design Specification

Version 0.4 | 21 October 2026 | Document ID IRGS RISE SPEC 0.4

Decision status. The product concept is approved. This specification records that approval and submits the detailed design for review. New procedures, record schemas, interface bindings, defaults, tests, and milestones in this edition are Proposed unless a requirement explicitly cites an adopted source. Publication does not adopt them or start a campaign.

The Rise of... You is the working title of the IRGS Settlement Campaign, a curated, player-configurable experience for establishing a household and a settlement in a chosen place and time. Players select the region, its resident cultures, the founding circumstances, and the company with whom they arrive. A founder can arrive alone, with a family, or with several families, and can begin with or without a grant. The player chooses the name of what rises. The system must support the consequences of those choices through one continuing world.

The design combines an approved product brief with a proposed implementation specification. It describes setup, founding, autonomous inhabitants, everyday life, material production, settlement services, records, runtime, integration, and validation. It is intended for the IRGS designer, rules implementer, content curator, and simulation runner. The catalogue now contains six historical starts, a variable planetary start, and a fantasy start with humans settling in traditionally elven lands. Historical evidence, fictional design, and generation rules remain distinct; no numerical economy is adopted.

Architecture. Shared IRGS Core supplies the reusable simulation rules. Selected genre foundations supply specialized procedures. Setting and theme modules supply premise-specific content. A Rise configuration produces a Campaign Profile and a Campaign State. The curated system coordinates those layers; it does not create another simulation kernel.

Integration finding. The supplied Core 3.3 package contains relevant specifications and a bounded executable suite. Its general household, settlement, and population descriptions are broader than its ordinary executable operations. Several retained Core sections still carry Proposed or not adopted labels. Rise therefore requires a receiving audit and additional adapters before it can claim executable support for its full founding experience.

Use this specification. Confirm the adopted requirements in Section 2, review the proposed procedures in Sections 3 through 23, and use the tests and milestones in Sections 24 through 28 to decide what can be implemented and released. Appendices retain the source reconciliation, integration evidence, record examples, and release checklist.

No Rise campaign is initialized by this document. No existing campaign, save, source archive, or Core rule is changed.

## Contents and reading guide

The DOCX uses editable headings, paragraphs, tables, and lists. Requirement and test IDs remain stable when wording changes. Sections refer to Core section numbers within the exact inspected edition identified in Appendix B.

01 Authority and design status

02 Adopted product requirements

03 Proposed implementation requirements

04 Architecture and ownership

05 Core audit and integration limits

06 Core interface contracts

07 Configuration and world setup

08 Time location and environmental setup

09 Cultures populations and institutions

10 Starting company and arrival options

11 Grants tenure and founding permission

12 Founder household and initial people

13 Settlement land and service development

14 Production trade and material continuity

15 Autonomous actors and population behavior

16 Delegation policies and off screen execution

17 Authoritative state and record ownership

18 Events accounting and information

19 Runtime time advancement and player control

20 Progression households and succession

21 Content curation and configuration coverage

22 Worked founding cases

23 Worked accounting and continuity cases

24 Acceptance and regression test catalogue

25 Interaction scarcity and reproducibility tests

26 Calibration and evidence plan

27 Development milestones and release criteria

28 Open issues and decision register

A Source reconciliation and accounted changes

B Core audit evidence and provenance

C Record examples and setup manifest

D Migration version control and release checklist

E Six historical starting packages

F Planetary and fantasy starting families

Status vocabulary. A marks a requirement adopted in the recovered product brief or current user request. G marks design safeguards retained from the earlier specification; they are proposals unless separately accepted. P marks a proposal in this specification. C identifies an inspected Core source; its embedded status is retained. V identifies a fresh verification result with a stated scope. These marks do not substitute for the separate design, campaign adoption, and validation fields defined in Section 1.

Reading paths. Product review starts with Sections 1 through 4 and 28. Implementation review adds Sections 5, 6, and 17 through 19. Content development starts with Sections 7 through 14 and 21. Validation uses Sections 22 through 27 and Appendices A through F.

## 01 Authority and design status

The approved concept establishes the product direction. It does not establish every earlier assistant suggestion as an adopted rule. The recovered conversation exposes the user's messages, but its assistant messages contain only content-reference placeholders. The user's statement agreeing to all of a preceding reply cannot establish the inaccessible contents of that reply. New details in this edition therefore remain proposals. [S1]

Current explicit user direction controls this amendment. Earlier project instruction files are not treated as renewed authority. The proposed design precedence is current user direction, established campaign rules and overrides, relevant adopted genre foundation, adopted Core or Integrated Framework, then temporary proposals where no rule applies. Source recency matters only within the source's scope. The selected local Core release is evidence of that suite's selection, not automatic adoption of every embedded candidate or a Rise campaign. [S0, S2]

### Separate status dimensions

| Dimension | Required record | Meaning |
| --- | --- | --- |
| Design | Proposed or Accepted with decision reference | Whether the rule or requirement has been accepted within a named scope |
| Ownership | Core, genre, setting, curation, or campaign | Which layer owns the mechanism or selected content |
| Campaign adoption | Not selected or selected with effective time | Whether this campaign actually uses the rule and version |
| Verification | Method, case, result, and limitations | What was checked or executed and on which version |
| Playtest | Session, version, participants, and conditions | Evidence from actual play rather than a worked example |
| Calibration | Parameter, target, evidence, and valid range | Evidence supporting particular values rather than general consistency |

Requirement language. Must expresses an obligation at that requirement's status. A proposed must is a proposed acceptance condition, not an already adopted rule. Should identifies a preferred design with a reasoned exception. May identifies an available option. Unknown is distinct from zero, false, and not applicable.

Each change records its source, old and new meanings, owner, dependencies, affected cases, and migration effect. Conflicts use Compare, Merge, Reconcile, Resubmit. A rebuilt edition must account for removed functions and carry unresolved disagreements forward. Corrections do not silently rewrite historical events.

Product boundaries. This is systems design. No scene, PC statement, relationship, purchase, movement, or political choice is invented by writing the specification. A player may delegate defined generation or routine execution; the delegation and its limits must be recorded. Narrative presentation follows causal resolution.

Approval needed for the design. The unresolved choices in Section 28 require design decisions before dependent implementation. They do not prevent review of this complete specification. Acceptance of a later edition must identify its exact version and any exclusions.

## 02 Adopted product requirements

These requirements preserve the directly recoverable product direction. They describe the approved experience; they are not claims that the experience is already implemented. Source labels resolve in Appendix B.

| ID | Adopted requirement | Source |
| --- | --- | --- |
| A01 | Deliver one curated configurable system from which players create their own founding experience. Replace the earlier framing as two separate fixed campaigns. | S1 user correction |
| A02 | Enable selection of where and when to play. The founding goal is to establish both a household and a settlement. | S1 explicit approval |
| A03 | Let players choose the type of region and its native or resident cultures during campaign configuration. | S1 user correction |
| A04 | Support arrival alone without a grant, including seeking permission to establish a homestead and the possibility that others later settle nearby. | S1 starting options |
| A05 | Support arrival alone with a grant for a small settlement or homestead. | S1 starting options |
| A06 | Support arrival with the founder's family, with or without a grant. | S1 starting options |
| A07 | Support arrival with a small group of families. Do not reduce all starts to a single protagonist with a supplied settlement workforce. | S1 starting options |
| A08 | Use The Rise of... You as the Settlement Campaign working title. Players retain naming choices for their households and settlements. | S6 title update; S1 naming |
| A09 | Pull applicable mechanics from IRGS Core and contribute reusable mechanics to Core when justified. | S1 starting options |
| A10 | Supply a thorough editable design specification with clear adopted and proposed requirements, architecture, world setup, autonomous populations, state, interfaces, tests, milestones, and open issues. | S3 current request |
| A11 | Provide six different pre-prepared historically grounded starts across six time periods, with plausible routes to settlement permission. Preserve the wider configurable system. | S4 user direction |
| A12 | Add a new-planet settlement start using variable generation. | S5 user direction |
| A13 | Add a fantasy settlement start, initially exemplified by humans founding in traditionally elven lands. | S5 user direction |

The original Medieval Dynasty and Sengoku Dynasty inspiration establishes provenance, not imported mechanics, values, or settings. The configurable system direction controls. [S1]

Interpretive limit. Anywhere and whenever remains the scope objective. Eight starting families do not certify universal coverage. Sections 21 and Appendices E and F define support and remaining work.

Founding goal. Establish a household and settlement without compulsory political ascent, expansion, household structure, or guaranteed recruitment. Continuation and failure remain proposed in Sections 20 and 28.

## 03 Proposed implementation requirements

The following requirements translate the approved brief into a reviewable design. They retain the earlier design safeguards as proposals without claiming that every proposed record or procedure is already supplied by Core.

| ID | Proposed acceptance condition | Main sections |
| --- | --- | --- |
| P01 | Compile a configuration into a versioned profile, separate initial state, and explicit unresolved choices before dependent play. | 7, 17, App C |
| P02 | Validate era, location, technology, institutions, cultural context, and selected modules for coherent coexistence. | 8, 9, 21 |
| P03 | Keep starting company, legal permission, wealth, expertise, and actual supplied assets independently selectable where plausible. | 10, 11, 12 |
| P04 | Represent grants as scoped rights and obligations under actual institutions, distinct from possession, acceptance, and supplies. | 11 |
| P05 | Preserve autonomous inhabitants, households, institutions, migrants, and neighbors with knowledge and finite means. | 15, 16 |
| P06 | Derive settlement function from actual land access, people, services, assets, work, and delivered supply. | 13, 14 |
| P07 | Use one authoritative owner per resource or fact and conserve people, stock, commitments, and progress across scales. | 17, 18 |
| P08 | Advance routine qualified work and standing NPC plans without repeated PC instruction; stop at material decision boundaries. | 16, 19 |
| P09 | Preserve physical occurrence, observation, transmission, receipt, and institutional recognition as separate events when consequential. | 9, 18 |
| P10 | Supply useful qualitative procedures where supported; block only the affected quantitative effect when material parameters are missing. | 6, 26 |
| P11 | Present consequences and supported choices without selecting the PC's speech, beliefs, politics, relationships, or new spending. | 19 |
| P12 | Maintain a complete manifest, causal journal, checkpoints, unresolved requests, and version history sufficient to resume play. | 17, 18, App D |
| P13 | Support stability, ordinary life, retirement, succession, relocation, and durable aftermath without forced enemy escalation. | 20 |
| P14 | Qualify content and runtime procedures separately. A matching title, catalogue entry, or schema is insufficient execution evidence. | 5, 21, 27 |
| P15 | Publish explicit support bounds and preserve current campaigns unless a scoped prospective migration is accepted. | 27, App D |
| P16 | Deliver H01 through H06 as versioned starting packages, with sources, defined company, permission status, actual opening means, autonomous neighbors, and a first decision. | 21, App E |
| P17 | Keep documented history, historical inference, fictional scenario design, calibration, and execution evidence separately identifiable for every prepared start. | 21, 26, App E |

G01 through G08 retain agency, feasibility, one clock, conservation, autonomy, inherited ownership, explicit status, and prospective migration as proposed safeguards [S0]. Appendix F adds P18 through P21 for planetary and fantasy starts. No universal development currency is introduced.

## 04 Architecture and ownership

Proposed placement. Rise is a curation and configuration system over IRGS. Its distinctive responsibility is assembling a coherent founding premise and connecting the selected services. It does not own a second economy, population count, timekeeper, injury system, or construction-progress ledger. [P01, P07]

| Layer | Owns | Rise use |
| --- | --- | --- |
| Shared Core | General action contracts, time, identity, resource transactions, information, commitments, work, and reusable domain interfaces within adopted scope | Request shared behavior through verified bindings |
| Genre foundation or engine | Mechanics that require a genre, including specialized effect models and operating assumptions | Select only where the founding premise needs them |
| Setting or theme module | Specific technology, cosmology, ecology, hazards, customs, institutions, and content profiles | Supply dated and located content without promoting lore |
| Rise curation package | Setup questions, compatibility rules, founding-start templates, configuration validation, and support catalogue | Produce a reviewable Campaign Profile and setup transaction plan |
| Campaign Profile | Selected versions, modules, calibration, geography, tone, boundaries, overrides, and initialization policy | Record what this instance will use |
| Campaign State | Actual people, places, property, grants, knowledge, quantities, conditions, relationships, projects, and history | Persist one continuing world |

Definition versus instance. A house design is content; a particular unfinished house is state. A culture profile describes context; an actual person has their own beliefs and conduct. A grant template defines possible terms; the issued grant names an issuer, recipient, scope, and effective period. Selecting a content pack creates none of those actual instances by itself.

Reusable contributions. If founding reveals a missing general mechanism, first identify the parent need. A grant is a scoped entitlement and institutional decision; recruitment is autonomous choice plus movement and membership; public works are projects plus services and authority. Propose a shared change only after comparison with Core. Keep local legal procedures, crop models, architecture, and ritual content at their valid layer.

Extension boundary. Rise may own a SetupSession, ConfigurationChoice, StartTemplate, CoverageEntry, and SetupIssue. Their fields reference shared owners. They may not carry mutable duplicate stock, legal-right, population, or work totals. Any new executable handler must declare its actual read and write owners and prove that its effects occur once.

Dependency policy. Use an optional service only when enabled and needed. A peaceful historical homestead does not need supernatural, military, or space procedures merely because those packages are available. A selected genre still supplies no unsupported current inventory, authority, or numerical defaults.

## 05 Core audit and integration limits

The inspected source is the supplied IRGS_Core_3_3_Live.zip, locally mirrored under sources. Fresh verification found 231 archive entries: 230 manifest-listed payloads plus the manifest. CRC checks passed; all 230 payload lengths and SHA-256 values matched. The selected Core document's hash also matches its binding. This establishes byte identity, not broad simulation correctness. [V1]

The release describes Core 3.3 as selected for its local suite. It contains a complete inherited specification, the R8 candidate, six genre receivers, eight libraries, and seven campaign profiles. The catalogue contains no Rise profile. Its historical candidate labels remain visible; sections 101 through 110 and several domain workflows retain Proposed labels, and section 122 explicitly says not adopted. A top-level release label must not erase those qualifications. [S2]

### Observed implementation boundary

The ordinary CoreWorld backend exposes 14 common operations, plus compatibility aliases and three bounded genre operations. It records declarations, evidence and receipts, confirmed actor fields, initial integer stock, stock transfers, obligations, designs, received orders, actors, capacities, booked activity, and delegation. It does not by those operations alone simulate a household's consumption, harvest, construction acceptance, migration, general land law, or settlement services. [S2 runtime/core_world.py]

Its normal stock invariant conserves an opening total across locations. It is not a generic production or consumption ledger. Research backends contain richer work, loss, economy, and strategic examples; enabling those for Rise requires an explicit supported adapter and model selection. The inspected common activity receiver books concurrent people; booking is not proof that productive work or travel occurred.

Fresh execution of four bundled modules ran 76 tests: 75 passed, one skipped, no failures. The skipped test needs a historical local save absent from the archive. Tested behavior includes shared stock, agency boundaries, information receipts, replay, transactions, bounded native operations, dependency observation, and durable decisions. These are existing Core fixtures, not Rise acceptance tests or playtests. [V2]

The package separately reports a larger historical validation suite. Those results remain source-reported evidence. The current audit did not rerun its sustained scenario, website HTTP tests, all historical verifiers, or every backend branch. No launch or save migration was performed. Appendix B identifies exact sources, hashes, commands, and the integration consequences.

## 06 Core interface contracts

This matrix specifies intended ownership and the integration work needed. C means a relevant procedure is described in the inspected Core text. It does not change that text's embedded status. All Rise receiving bindings remain Proposed. [P07, P14]

| Interface | Source and owner | Rise contract and support limit |
| --- | --- | --- |
| Identity and capability | C sections 14, 64; K-ACTOR | Use stable person IDs and actual capabilities. register_actor supplies identity only; full physiology and skill evidence need selected records. |
| Time and commitments | C sections 10, 11, 90, 91; K-TIME | Reserve actual intervals and process causal boundaries. Integer runtime clock needs a declared mapping to campaign units and calendar. |
| Households and care | C sections 68, 71, 122; LIFE with K owners | Link members, care, private property, and provision. Section 122 is explicitly not adopted in its retained text; a complete Rise workflow is unbound. |
| Population and movement | C section 106; K-POP K-ACTOR | Preserve named and residual people; retain transit and demand on arrival. Section 106 is a Proposed Core promotion; no general migration receiver is established. |
| Authority and grants | C sections 28, 107, 113; K-ORG and GOV | Validate jurisdiction, scope, effective time, and disputes. A nonempty authority_ref alone is not historical or legal verification. |
| Stock and logistics | C sections 12, 20, 35, 105; K-STOCK K-ASSET | Own quantities, title, custody, access, reservations, and transit once. Common stock handles integer establishment and transfer; richer lots need an adapter. |
| Work and technology | C sections 73, 108, 109; K-WORK | Transform actual inputs through qualified work and acceptance. Research fixtures do not establish generic Rise production. |
| Services and development | C sections 72, 103, 121; K-NET and URBAN | Separate asset capacity, allocation, staffing, and delivery. The general service simulation requires qualification. |
| Knowledge and reputation | C sections 30, 61, 66, 85; K-INFO | Keep truth, assertions, observations, and receipt distinct. Common evidence is actor-subject based; site and institution evidence need a supported mapping. |
| Environment and resource sources | C sections 50, 51, 104, 119; WILD | Provide local source state and seasonal process models. No universal yield, renewal rate, or weather generator is verified. |

Contract form. Each adapter identifies exact provider and version; operation; input fields and units; prerequisites; expected pre-state; permission and knowledge basis; finite costs; effect bounds; written fields; event identity; interruption and replay behavior; unsupported cases; acceptance tests; and campaign adoption status. It rejects unsupported effects without inventing defaults.

No semantic shortcuts. Do not use set_scene as consumption, confirm_character_field as an unrestricted physical simulator, establish_stock as replenishment, record_design as construction, or commit_activity as proof of finished work. Separate rich specification compatibility from executable operation support. Research adapters and human-run procedures must each declare their actual persistence and validation limits.

## 07 Configuration and world setup

Purpose and status. Proposed workflow P01 compiles player choices into a coherent founding premise. It depends on versioned content, the authority rules, and sufficient state for the first dependent action. It may be performed by a human runner or software; the output contract is the same.

1. Choose H01 through H06, planetary start N01, fantasy start F01, or a custom configuration. A prepared start supplies reviewable defaults, not compulsory player actions. Then establish the premise envelope: historical, alternate historical, fictional, or another explicitly selected setting; place and date; tone; scope; boundaries; death and continuation policy.

2. Select the region and its resident societies. Establish what is fixed by source, chosen by the player, generated under delegation, or still unknown. Record political geography and physical geography separately.

3. Select the founder and starting company. Record household relationships, travel grouping, any enterprise, actual skills, dependants, obligations, and personal control boundaries.

4. Select tenure and starting permissions. Resolve whether a grant exists, what it authorizes, who recognizes it, and what remains to be negotiated. Select actual property and supplies separately.

5. Bind relevant needs, time, movement, work, effect, climate, economy, and institutional procedures. Identify outcome-changing missing parameters before their use.

6. Compile a profile, initial state proposal, source register, hidden-state policy, issue list, and initialization plan. Check compatibility and conservation.

7. Present the material starting facts and options to the player. Record confirmation of the selected premise and any delegated generation. Commit initialization once and return control before the first voluntary action.

### Configuration behavior

A setup choice must show its causal consequences: different seasons affect crops and travel; different company sizes affect provision and coordination; a grant may add obligations while reducing one permission problem. Do not hide a default that changes legal status, household membership, scarcity, or the first action. Offer custom values when supported, and identify content work when they are not yet supported.

Backtracking before initialization invalidates and rebuilds dependent draft facts. It must not duplicate generated people or merge incompatible starts. After initialization, changes use in-world events or an explicit correction or prospective profile change. Rerolling setup is not a means of replacing an established neighbor or resource site during play.

Completion condition. The first playable situation has a valid clock, declared player control, actual present company, a place or route, decision-relevant rights and constraints, known means, immediate needs, and a meaningful unresolved choice. Distant detail may remain ungenerated. An absent production parameter need not prevent a conversation that does not depend on it.

## 08 Time location and environmental setup

Rise must preserve the adopted freedom to choose time and place while making each selected configuration causally coherent. Date selection includes era, calendar, start date and time precision, season, and any known regional chronology. A historical claim requires a source and confidence appropriate to the detail. Alternate history records its divergence point and what remains unchanged; a divergence is not permission to mix arbitrary institutions and technology. [A02, P02]

### Region record

Record the region's extent and useful travel relationships; terrain, waterways, climate regime, seasonal hazards, soils and land uses; occupied sites and routes; resource sources; political jurisdictions; existing claims; trade access; and information limits. Exact coordinates are optional unless decisions depend on them. An unmeasured distance stays estimated or unknown, with a method for resolving it.

Separate the selected broad region from a candidate founding site. A region may contain several societies, elevations, jurisdictions, and resource zones. A useful river does not guarantee a crossing, potable water at every point, or permission to build on its banks. A timbered area contains standing resource potential, not a stock of prepared beams.

| Setup axis | Required distinction | Validation question |
| --- | --- | --- |
| Date and season | Calendar date versus environmental conditions | Are cultivation, travel, and shelter assumptions coherent with the selected period? |
| Technology | Known design versus local productive capability | Are tools, materials, skills, supply, and maintenance actually available? |
| Geography | Broad regional traits versus actual site facts | Which routes, resources, and hazards are established at the chosen site? |
| Jurisdiction | Claimed territory versus effective control | Who can grant which rights and who may dispute them? |
| Knowledge | World truth versus founder information | What does the founder know, by what source, and as of when? |
| Scarcity | Chosen starting constraints versus missing data | Is a shortage established, or is the quantity simply unknown? |

Environmental processes run at causal intervals: weather changes, planting windows, source depletion, spoilage, flooding, or other selected thresholds. A daily review may summarize those processes; it must not generate a new random catastrophe merely because another day passed. Ecology continues beyond the settlement and can be affected by actual extraction, waste, movement, and cultivation.

Coverage rule. The catalogue target is eight starting families: six historical periods in Appendix E, plus planetary N01 and fantasy F01 in Appendix F. Each states its geographic, temporal, genre, institutional, and execution bounds. A custom place or date request creates an explicit curation task and dependency list. It does not authorize invented historical fact or quietly replace the request with a medieval European default. [P14]

## 09 Cultures populations and institutions

Configuration can select the region's native and resident cultures as part of the founding premise. In a historical configuration, selections must remain consistent with sourced time and place or be identified as alternate history. In a fictional configuration, generation requires delegated scope and internal consistency. Once initialized, cultures and populations are established world state; the player does not revise them by selecting a new menu option. [A03, P02]

### Cultural context without compulsory behavior

A cultural profile can describe language, kinship patterns, customary land use, livelihoods, institutions, material practices, beliefs, etiquette, education, and internal variation. Each entry identifies scope, period, sources, uncertainty, and exceptions. Profiles supply context, opportunities, and expectations. They do not impose personality, virtue, skill, loyalty, hostility, or a universal numerical modifier on every member.

The same person may have several affiliations, speak several languages, dissent from a custom, or act from personal obligations. Household membership, residence, cultural affiliation, legal status, occupational role, and political allegiance remain separate. Interaction depends on actual communication and interpretation. A translation difficulty must identify the relevant language or practice rather than treating an entire people as an encounter penalty.

### Existing people and competing claims

Before founding, establish occupied sites, mobile or seasonal users, households, neighboring communities, resource access, recognized rights, disputed rights, and effective control where relevant. Unbuilt land is not automatically unowned, unused, or available. Seasonal hunting, grazing, water use, sacred significance, and travel corridors may matter independently of permanent buildings.

A grant's issuer may control only one jurisdiction, may lack recognition, or may purport to grant already claimed land. Record the document, validity under the selected institutional procedure, recognition by each relevant audience, and practical access separately. Conflict is possible, not compulsory. Agreements, purchase, tenancy, shared use, incorporation, relocation, or refusal can follow actual choices and authority. No political outcome is selected for the PC.

### Institution records

Each consequential institution needs jurisdiction, function, actual office holders or roles, authority basis, procedures, resources, communications, obligations, and review triggers. A council, clan office, landlord, temple, state agency, corporation, or community assembly is not a staff or service created by a label. Their people and property use the same authoritative records as all other actors.

Acceptance. Two inhabitants of the same cultural group can rationally disagree; local recognition need not match the grant issuer's assertion; information travels through actual witnesses and channels; peaceful cooperation can remain stable. Additional local research remains necessary; Appendix E sources support only their stated regional claims.

## 10 Starting company and arrival options

Starting company means the people arriving with the founder. It is distinct from an incorporated business, military company, or ownership partnership. An enterprise may also exist, but only if selected and established. Company composition and grant status are independent setup axes, constrained by the chosen premise. [A04 through A07, P03]

| Start | Adopted basis | Permission state to establish | Material and social consequences |
| --- | --- | --- | --- |
| Solo without grant | Explicit S1 option | No preissued founding grant; permission and access follow the selected local procedure | One present founder; no automatic workforce, shelter, or local contacts |
| Solo with grant | Explicit S1 option | Issued grant for the selected homestead or settlement scope | Rights and obligations require their own terms; supplies remain separate |
| Family without grant | Explicit S1 option | Family presence grants no universal land right | Care, private property, household decisions, and provision need records |
| Family with grant | Explicit S1 option | Grant names its recipient and beneficiaries if applicable | Family members do not all become workers, coowners, or office holders |
| Several families | Explicit S1 option | Grant status was not fixed in the recovered wording | Distinct households need coordination, rights, property, and consent |
| Several families with a shared or separate grant | Proposed elaboration | Specify grantees, shared rights, allocation, and representation | Avoid treating one founder as owner of every family or asset |
| Other supported company | Proposed extension | Define the actual arrangement | Friends, hired specialists, sponsored parties, or mixed groups require explicit terms |

Arrival boundary. Choose whether play begins before departure, in transit, at a regional entry point, at a host settlement, or at the proposed site. The initial location and elapsed journey determine actual stock, fatigue, knowledge, obligations, and pending events. A stated past journey must not be charged again after setup.

Independent start fields. Company size, household links, species where applicable, age or life stage, practical capability, health, expertise, language access, personal goods, communal goods, money, debts, transport, sponsorship, permission, and local contacts are separate selections or generated facts. No universal points budget is adopted here. Any balancing package must disclose its actual contents and tradeoffs.

No automatic arrivals. A solo founder may attract settlement, but a constructed house does not spawn a family. Potential migrants need an origin, reason, information, willingness or constraints, a route, means, and an actual arrival. Their private property and continuing ties remain theirs until changed by a valid event.

## 11 Grants tenure and founding permission

Purpose. Proposed procedure P04 handles a founder's scoped entitlement to settle or use land. Its parent mechanisms are institutional decisions, agreements, title and access, obligations, communication, and records. Historical legal forms remain content or profile choices. The existence of a grant never proves universal authority or vacant land.

### Minimum grant record

Record a stable ID; issuer and asserted authority; recipient and beneficiaries; instrument or decision source; issue, receipt, effective and expiry times; land or activity scope; permitted uses; transfer and inheritance terms; duties and payment or service obligations; conditions; dispute venue or customary remedy; recognition by relevant parties; practical access; and current status. Unknown fields remain explicit. A monetary subsidy, if any, is a separate claim and eventual transfer.

### Founding procedure

1. Identify the intended activity and the rights it requires under the selected institutional context. Physical feasibility and institutional permission are separate checks.

2. Establish the relevant issuer, existing claims, means of communication, evidence, and procedure. An official's willingness to consider an application is not an issued grant.

3. Resolve the declared request. Routine qualified administration may succeed without a roll, consuming actual time and required resources. Consequential uncertainty is scoped to the feasible concession or decision.

4. Record the actual decision and terms. If Mixed introduces a new voluntary cost or obligation, present those terms to the player before acceptance. Do not silently buy a grant or pledge service.

5. Apply valid rights at their effective time under the selected procedure; communicate the result to actual recipients. Recognition and enforcement may be separate.

6. Carry out authorized survey, occupation, construction, registration, or service work through its ordinary owners. Do not manufacture facilities or control from the permission itself.

### Changes and disputes

Expiry, revocation, default, inheritance, transfer, contested title, and remedy require explicit grounds and applicable procedure. A missed obligation may create arrears or review rather than instant eviction. Institutional validity can change before a distant recipient learns of it; that information delay affects decisions without reversing the actual legal event. Actual coercion or removal requires actors, access, authority claims, means, and time.

No grant start. The founder may ask permission, rent, purchase, obtain a use agreement, receive hospitality, choose another site, or act under another selected local arrangement. No universal sequence, fee, feudal status, citizenship rule, or sovereign right is imposed. A solo no-grant start must remain playable without a secretly guaranteed approval.

Acceptance. A disputed grant persists as a record; a successful permission request preserves the concession actually won; different rights can coexist on one site; receiving paperwork creates no money, tools, settlers, buildings, or political obedience.

## 12 Founder household and initial people

The founder is the player-controlled actor selected in setup. Identity, chosen history, household relationships, personal priorities, voluntary commitments, and politics require player input or explicit delegation. The system can generate surrounding detail within delegated bounds, but may not assign the PC an opinion, spouse, child, debt, purchase, or past act merely to fill a form. [G01, P11]

### Household initialization

A household references actual members and dependants, residence, care arrangements, shared and private property, income sources, debts and other claims, provision sources, relationships, outside ties, and decision rights. It can include several adults, a single person, unrelated residents, extended kin, or another supported arrangement. No universal family model or household head authority is implied.

For each decision-relevant person establish actual location; condition and functional capability; knowledge and languages; obligations; willingness or applicable constraints; care responsibilities; personal resources; current commitments; and information available to others. Ordinary supported capability need not be reduced to an invented numeric attribute. Expertise and available work time are distinct.

| Initial record | What must be established | Common error to prevent |
| --- | --- | --- |
| Person | Stable identity and actual presence | Counting an archetype as an additional real person |
| Household membership | Named links and effective terms | Turning membership into ownership or obedience |
| Property | Item or lot, owner, custodian, location, and access | Pooling every family member's goods automatically |
| Care | Recipient, responsible actor, method, and interval | Treating all adults as full-time labor |
| Capability | Evidence, task scope, means, and restrictions | A skill roll supplying absent tools or qualifications |
| Commitment | Actual actor, interval, task, and stop limits | Overbooking care, travel, and productive work |
| Knowledge | What the person has observed or received | Giving new arrivals all regional truth |

### Generated people and residual cohorts

Generate a person once within the agreed scope, assign an ID, and preserve consequential facts. Reveal details through appropriate observation rather than rerolling the person at each meeting. Aggregation is allowed for large routine populations, provided cohorts preserve totals and decision-relevant differences. Naming an existing cohort member subtracts one from the residual cohort and does not create another inhabitant.

Initial means. Every supplied object, quantity, animal, tool, vehicle, skill claim, relationship, or grant has a source in the selected start. A content list establishes available definitions; it does not establish possession. Unknown inventory is not an empty inventory, and it is not permission to spend. Resolve the affected unknown before the dependent action.

## 13 Settlement land and service development

A settlement is persistent habitation and coordination around actual people, land, means, and services. Its name and social recognition may precede or follow substantial building. Camp, homestead, hamlet, village, town, and mobile community are useful descriptions; no universal tier ladder, population gate, or resource bonus follows from a label. [P06; C section 72]

### From a candidate site to a functioning place

Establish lawful or practical access, existing users and claims, local hazards, shelter options, immediate provision, routes, and the actual company. Identify the founder's declared objective. Survey, negotiation, clearing, building, cultivation, and commissioning are separate activities when causally distinct; they are not mandatory stages in every founding case. An existing structure or temporary arrangement can serve a function without recreating an idealized settlement plan.

Each development case references a spatial unit, proposed use, rights and access, physical constraints, affected people, required work, materials, labor, tools, dependencies, acceptance criteria, and operating responsibilities. Plans and reservations do not become physical facilities. Completed valid work persists when a worker leaves unless an actual event damages it.

### Services and demand

For each enabled service record actual users, requirement specification, quantity or rate where needed, available stock or provider, installed and feasible capacity, allocated capacity, delivered service, restrictions, maintenance, and next threshold. Shelter, potable water, food access, sanitation, healthcare, heat or cooling, waste handling, transport, education, and safety are selected according to premise and decisions.

Demand begins when actual users arrive or their circumstances change. A support estimate is a view, not a resident count. If 12 people are present and water provision supports 9 under the selected profile, record 12 people and a deficit affecting 3 people or an explicit allocation. No one disappears. More beds do not add water, care staff, consent, or food.

Operating reality. A completed well can fail to deliver because of access, quality, handling, or missing equipment. An occupied borrowed building can supply real shelter without creating title or a second building. Temporary service, tested physical completion, institutional authorization, and sustained operation may coincide or differ; use only distinctions that affect the case.

Collective decisions. Public works, shared land allocation, dues, service priorities, and local governance depend on actual decision rights and agreements. The player's status as protagonist supplies no universal authority. Autonomous residents can propose, negotiate, undertake, or refuse work within their circumstances. Settlement views read the same household, institution, service, and project records; they do not own parallel totals.

## 14 Production trade and material continuity

Production combines actual inputs, access, qualified labor, tools, workspace, time, and a selected process. It yields specified output, waste, and possibly work in progress. A resource source, design, reserved input, completed labor interval, inspected item, and accepted usable product are distinct where the process makes them distinct. No output exists merely because it is forecast. [P06, P07]

### Work and production contract

Specify deliverable, acceptance criteria, work units, rate basis, maximum useful concurrency, input timing, tool use, site capacity, worker commitments, environmental constraints, interruption rules, quality effects, and output ownership. Routine qualified work succeeds without a compulsory roll. If a check resolves a consequential uncertain interval, its branches must identify the actual progress, elapsed time, losses, and supported consequences before resolution.

A crop model additionally needs land preparation, seed or planting material, seasonal eligibility, labor, water and environmental support, maturation, harvest, storage, and yield uncertainty. A food-processing model cannot turn all grain into both seed and meals. A forestry model must distinguish living trees, felled material, transport, preparation, and supported renewal. Numerical values remain unselected in this edition.

### Exchange and obligations

Trade records parties, actual offers, specification, quantity, price or exchange terms, delivery, title transfer, acceptance, payment, risk, and dispute terms where relevant. Price evidence can be a quote, transaction, or estimate with place and date; it is not a universal market price. A claim for wages, grant money, rent, tax, or a sale is not cash. Payment debits the actual payer and credits the actual recipient once.

Private stocks remain private. Shared storage does not itself transfer title. Access, custody, ownership, eligibility, and physical location can differ. Transit is an actual location with cargo and ongoing risk, needs, and travel time. A shipment is not at both endpoints, and an expected delivery cannot back current consumption.

### Continuous operation and interruption

Maintenance, spoilage, wear, fuel, care, handling, and recovery use selected causal processes. Charge a cost at its actual stage, once. Retain qualifying work already completed. An interruption may suspend future progress, preserve a damaged intermediate, create a replacement requirement, or require reassessment; it does not automatically erase the whole project.

Economic behavior. Households and enterprises can seek livelihood, trade, specialize, save, borrow where available, or stop uneconomic work according to goals and information. Demand and willingness to pay require actual actors and means. Population growth, prosperity, or a settlement name never creates a purchaser, workforce, treasury, or automatic production multiplier.

## 15 Autonomous actors and population behavior

Purpose. P05 makes the region an ongoing world. People and institutions pursue goals, maintain households, work, trade, care, travel, learn, negotiate, and respond to change while the protagonist is elsewhere. Their conduct uses their own knowledge, authority, resources, competence, obligations, procedures, relationships, and risk tolerance. [G05; C sections 64 through 66]

### Decision contract

At a material review boundary, identify the actor, known situation, goals, obligations, options, available means, current commitments, and decision rights. Continue a valid standing plan unless a meaningful trigger changes it. For a new choice, record the selected feasible response and causal basis. Schedule its execution through shared work, movement, communication, or transaction owners. A reasoned autonomous decision does not require a new random roll each turn.

Review triggers include a due commitment, new received information, changed access, a stock or service threshold, completed work, an actual hazard, a relationship event, a seasonal boundary, or an order within recognized authority. A review is not an event quota. If nothing material changes, ordinary life can continue without a dramatic incident.

### Migration and recruitment

Separate awareness, interest, contact, negotiation, agreement, departure, transit, arrival, residence, membership, and work assignment when those states matter. A possible migrant needs an actual source population or delegated generation, plausible information, motivations, constraints, means, and a route. Arrival creates immediate needs and local presence, but does not establish political membership, communal ownership, acceptance of every rule, or unrestricted labor availability.

New residents can bring knowledge, property, debts, affiliations, dependants, skills, illnesses, or obligations only when actually established. They can later leave. Departure changes presence, commitments, service demand, and carried goods at the correct time; it does not erase every relationship or claim. Care duties and relevant promises continue until a supported change occurs.

### Collective behavior

Households and institutions coordinate through actual decision procedures. A representative has bounded authority. Groups can disagree internally; aggregate handling must split when different decisions, locations, conditions, or resources affect outcomes. Preserve morale, cohesion, discipline, legitimacy, willingness, trust, and immediate pressure as distinct concepts where relevant. No universal satisfaction meter substitutes for their causes.

Player boundary. Autonomy never selects the PC's voluntary action. A family member may request help or act within their own rights; the runner does not silently make the founder agree, marry, relocate, spend, or adopt a policy. External constraints and involuntary effects follow supported mechanisms. Present the next meaningful player decision after resolving the world consequences already in motion.

## 16 Delegation policies and off screen execution

Delegation lets the founder act at household or settlement scale without personally directing each routine movement. It transfers bounded execution authority, not ownership of the delegate's mind or an unlimited right to spend. Established NPC roles can also justify autonomous work without a new PC delegation. [P08]

### Standing policy record

Record principal, responsible actor or institution, purpose, subject and place scope, permitted operations, spending and resource ceilings, protected reserves, time horizon, applicable priorities, required information, reporting channel, review triggers, stop conditions, and revocation process. State which choices are left to the delegate and which return to the principal. Actual institutional authority and willingness must support the arrangement.

Examples include maintaining a specified reserve if affordable; conducting a defined building job with supplied materials; trading within a price range; or coordinating care within a household's actual agreement. These are examples of policy structure, not adopted start policies or automatic PC orders. The system must not infer a standing instruction from a broad aspiration such as make the settlement prosper.

### Execution sequence

1. Determine what the delegate has actually received and understood. Validate authority, willingness or obligation, resources, knowledge, and scope at the relevant time.

2. Propose feasible operations using current information. Unknown facts can prompt inquiry, a conservative action, or deferral; they cannot supply imagined stock or permission.

3. Book actual people, tools, sites, and materials. Check existing care, travel, and work commitments across every institution.

4. Execute qualified routine work and supported transactions through shared owners. Review at interruption, completion, threshold, new information, or expiry.

5. Send reports through the actual channel. A report describes physical outcomes; it does not apply those outcomes again. Ask for a new decision only when the policy's limits are reached.

### Scheduling and failure

Priority rules must be actual policy or institutional procedure. If simultaneous requests compete for the same resource, preserve the requests and obtain the applicable allocation decision; identifier order is not a priority rule. Unknown policy is a design or state gap, not permission to favor the protagonist.

If a task cannot continue, retain completed work, unused stock, current reservations, liabilities, and the reason. A delegate can report, seek alternatives, renegotiate, or stop within scope. A missed report does not prove failed execution, and a received instruction does not prove successful work. New voluntary PC resources require a player decision beyond the recorded ceiling.

Implementation limit. Core 3.3's bounded strategic planners demonstrate selected observation and rights boundaries using synthetic scenarios. Rise household and settlement policies, their persistence, and their adapters must be separately qualified before autonomous software execution is claimed.

## 17 Authoritative state and record ownership

The following is a proposed semantic schema. Equivalent concise records are acceptable if they preserve the same meaning and recoverability. It is broader than the ordinary CoreWorld JSON schema and must not be described as directly executable without a receiving adapter. [P07, P12]

| Record family | Authoritative owner | Required meanings |
| --- | --- | --- |
| Campaign and profile | Campaign manifest | IDs, versions, adoption times, enabled models, overrides, and source pins |
| Setup session | Rise curation | Choices, dependencies, confirmations, delegated generation, and unresolved issues |
| Person and condition | K-ACTOR | Identity, presence, capability, restrictions, condition, and actual custody |
| Household and relationship | LIFE referring to K owners | Membership, care, agreements, social ties, property references, and succession |
| Residual population | K-POP | Cohort scope, count, distinctions, presence, and named extraction lineage |
| Organization and office | K-ORG with GOV decisions | Roles, staffing, mandates, authority basis, procedures, and recognition |
| Land and grant case | GOV, ECO, and URBAN by fact type | Jurisdiction, decisions, agreements, claims, occupancy, and use permissions |
| Asset and stock lot | K-ASSET and K-STOCK | Specification, quantity, units, owner, custody, location, condition, and reservations |
| Task and program | K-WORK with domain workflow | Work, inputs, time, qualifying assignments, actual progress, and acceptance |
| Service and route | K-NET | Provider, users, demand, capacity, allocation, delivery, access, and dependencies |
| Habitat and source | WILD with K references | Environmental state, resource potential, renewal, extraction, and observations |
| Evidence and message | K-INFO | Source, assertion, truth status, audience, times, lineage, and uncertainty |
| Commitment and event | K-TIME | Actor, interval, causal parents, preconditions, effects, processing, and replay |

Every consequential record carries campaign_id, stable record_id, semantic type and owner, schema version, effective time or interval, provenance, design and adoption status where relevant, access rules, record revision, and last applied event or equivalent history reference. Quantities identify units; estimates identify their basis; unknowns are explicit.

Physical and social views. A person has one physical location at a time and may have several memberships. A household's asset list references actual ownership records. A region's population panel sums disjoint present individuals and residual cohorts. A service forecast reads delivery and demand; it does not write another stock or condition.

Persistence. Save authoritative state, unresolved requests, standing policies, scheduled boundaries, model versions, event identities, retained resolutions, and restricted knowledge. Summaries cannot replace recoverable facts. Secrecy requires actual private persistence; a shared document cannot conceal facts from its reader.

## 18 Events accounting and information

Event contract. Each event identifies campaign and event IDs, recoverable payload, operation and provider version, causal parents, occurrence time or interval, execution or receipt time where different, source and authority, expected pre-state, affected owners, proposed changes, visibility, retained uncertainty result, and processing status. Atomicity applies to each supported transaction; independent work need not be blocked by an unrelated unresolved component. [P07, P09]

### Accounting invariants

Transfers debit and credit both ends once. Reservations constrain eligible supply but are neither consumption nor new stock. Consumption, loss, recovery, and production require their own qualified transformations and provenance. An opening-balance operation is not a recurring supply source. Material conversions define their input, output, waste, and units rather than assuming conservation across unlike measures.

For a given stock representation, closing quantity equals opening quantity plus actual receipts and qualified production, less actual dispatches, qualified consumption, and physical losses. This is an accounting identity, not adoption of any rate. A source depletion record and harvested goods must be linked so the same timber or crop is not recovered twice. Money, claims, forecasts, and valuations remain distinct.

Living people present equal individually represented living people plus the disjoint residual population present. Birth, death, arrival, departure, and named extraction each have a single causal event. Residence and institutional membership are separate views. A death report updates knowledge; it does not kill another person.

### Information timing

Retain occurrence, observation, transmission, receipt, and understanding times when they differ materially. A claim may be false, outdated, disputed, or misinterpreted without altering world truth. A survey may narrow an estimate without creating the surveyed resource. Reputation changes for actual audiences from received evidence and interpretation, not through a universal instantaneous score.

### Replay and simultaneous events

Same event ID and same payload must not duplicate effects; a changed payload under an already used ID is rejected or handled as an explicit correction. Different IDs do not authorize repeated consumption, milestone acceptance, or processing of the same causal span. Store processed interval coverage and underlying source identity where needed.

Simultaneous events read the relevant pre-event state. A delivery at a frontier is not silently available to a simultaneous job whose preconditions required earlier receipt. Establish a supported causal order or retain the conflict. Later allocation decisions revalidate actual current stock, authority, and time. Scale changes preserve outstanding commitments, people, injuries, goods, project progress, and event identity.

Correction. Correct the identified error and its dependent consequences with explicit provenance. Do not reroll a legitimate result, erase an unrelated success, or backdate a grant to justify an already invalid action.

## 19 Runtime time advancement and player control

Rise inherits the project sequence: Declaration, Feasibility, Execution and Uncertainty, Effect, Exposure and Reaction, State Update, Player Control. The procedure below specializes its use for founding; it does not introduce another resolution system. [G01 through G05]

1. Capture the PC's declared objective, method, target, intended scope, time and spending limits, and any standing delegation. Clarify only an outcome-changing ambiguity; do not invent an action.

2. Check physical and institutional feasibility using actual means, access, capability, obligations, knowledge, and resources. Missing capability or a material rule is not uncertainty that a good roll can overcome.

3. Establish the relevant work, travel, conversation, transaction, or exposure interval and causal stop boundaries. Reserve actual commitments without consuming inputs prematurely.

4. Resolve consequential uncertainty through the selected adapter. Routine qualified work normally succeeds. Retain feasible Success, Mixed, and Failure effects; Mixed cannot choose a new purchase or follow-up for the PC.

5. Apply physically feasible effects through their owners. Resolve autonomous responses and involuntary consequences from actual actors, observation, and exposure. Failure cannot create an unrelated catastrophe.

6. Advance all relevant standing work and environmental processes over the same interval. Stop at the earliest material threshold, interruption, completion, received information, or player decision.

7. Commit state, journal, information, and due events once. Present what the PC can perceive, supported consequences, current constraints, and the next meaningful decision. Return control.

### Scales and review intervals

Conversation, local work, travel, daily household routine, seasonal production, and generational development can use different presentation scales. Scale changes do not replenish resources or reset commitments. A week-long advance must account for consumption, care, travel, work, and material interventions throughout the week. It cannot charge all weekly costs again when the first detailed day resumes.

Use event-driven processing where possible. Review a stable process at its next causal boundary; use a periodic interval only when the model needs it. Forecast to a threshold and stop before an unsupported outcome. A monthly settlement report summarizes the same accepted work and events as local play.

Pacing. Summarize routine authorized execution; expand only the decisions and uncertainties that matter. Do not require the player to personally approve every NPC meal or work step. Do not skip a new household commitment, major expenditure, legal concession, relationship choice, or dangerous voluntary action merely to keep a seasonal schedule moving.

Runner output. Include the current authoritative time, relevant changed records, unresolved uncertainties, known upcoming pressures, and player-facing choices. Keep implementation details out of the fictional decision unless they help the player understand a real constraint.

## 20 Progression households and succession

The founding goal can be fulfilled through a durable household and a functioning community appropriate to the chosen premise. Further progression can include competence, livelihood, relationships, wealth, secure rights, care, institutions, technology, infrastructure, cultural continuity, ordinary life, family, retirement, and legacy. The system must not require recurring conquest or stronger enemies to validate success. [P13; G governing progression]

### Progress without a universal settlement level

Record actual accomplishments and changed capabilities. A household can have secure housing and fragile income; a settlement can have excellent water and poor transport; a respected founder can hold no public office. These are useful distinctions. Do not collapse them into one level that grants unrelated buildings, obedience, fertility, or productive capacity.

Learning requires a selected profile, opportunity, practice, instruction or evidence where applicable, real time, and retention. Practical competence, credentials, appointment, authority, productive institutional capability, and possession of technology are separate. A skilled artisan cannot single-handedly supply an absent supply chain, and an office holder need not possess every technical skill.

### Generations and continuation

Before dependent play, select death and control-transition rules: permanent end, generational continuation, retirement, another explicit supported model, or a defined boundary for later decision. No respawn or successor appears by default. A successor can be an existing related or unrelated actor; generating a child is not required.

On transition preserve the world clock, living people, injuries, property condition, debts and claims, reserves, work, institutions, knowledge histories, promises, and pending events. Separate legal inheritance, practical custody, office succession, household responsibilities, social recognition, and player control. A successor does not automatically inherit expertise, memories, all secrets, authority, affection, or every liability.

Setbacks and aftermath. A failed harvest, household departure, disputed grant, illness, or abandoned project produces the actual supported consequences. It need not end play or secretly supply a replacement benefit. Stable solutions remain solved until a causal change occurs. A ruined building, unpaid debt, damaged relationship, or repaired service persists beyond the scene in which it mattered.

Scope changes. A founder may pursue travel, trade, service, public life, or another goal if the selected campaign supports it. Whether permanent abandonment of founding remains within the branded experience is an open product decision O02. The simulation should preserve agency and world continuity while that product boundary is resolved; it must not force a PC to build or return.

## 21 Content curation and configuration coverage

Rise must provide eight starting families through one curated system: H01 through H06 in Appendix E, variable planetary start N01, and fantasy start F01 in Appendix F. All are specification-stage profiles; no executable or playtested content is claimed. Packs are examples and support units within the configurable system; they must not recreate the superseded two-campaign structure. A custom configuration remains a legitimate request even when additional research and design are required. [A01, A02, P14]

### Required pack contents

Each pack identifies geographic and temporal bounds, historical or fictional basis, languages and cultural variation, institutions and rights procedures, environment and hazards, relevant technology and productive support, buildings and equipment definitions, livelihoods, trade relationships, name conventions, plausible starting templates, sources and uncertainty, model requirements, explicit exceptions, and acceptance fixtures. It identifies unavailable content rather than filling gaps with a different region's lore.

No pack silently supplies current inhabitants, stock, grants, relationships, hazards, or political events to an initialized campaign. The setup compiler creates actual instances only within confirmed scope. Historical sources, fictional generation, inference, and game-design calibration remain separately marked. Game files or other entertainment references may suggest content organization but are not evidence of historical fact.

| Coverage status | Permitted claim | Required next action |
| --- | --- | --- |
| Defined | Scope and intended content are described | Complete procedures and source register |
| Specification compatible | Required providers and meanings map without lost functions | Implement or qualify the stated runtime path |
| Executable for named cases | Particular operations passed recorded cases | State unsupported branches and model gaps |
| Playtested | Named configuration was used in recorded play | Report conditions and issues without claiming universal balance |
| Calibrated for named parameters | Particular values meet declared targets in a valid range | Preserve evidence and reassess outside that range |
| Held or unsupported | An outcome-changing dependency is unresolved | Block the affected claim or effect and record the gap |

### Curation checks

Review date-place coherence, institutional jurisdiction, internal cultural variation, technology support, supply and maintenance, household arrangements, migration sources, local ecology, and plausible starting means. Check that no source status or rejected rule is overwritten. Bind exact content revisions and aliases so an update cannot silently change an already built house or known person.

Research policy. Use scoped historical evidence and retain provenance and uncertainty. Appendix E records the research supporting the six-start target [A11]. Exact sites, instruments, inventories, and delivery order require further work. External evidence does not adopt scenario details, numerical values, or runtime capability. Appendix F defines fictional generation separately. Additional coverage remains open under O03.

## 22 Worked founding cases

These are scripted design cases for the proposed procedures. They are neither initialized campaigns nor playtests. All people and circumstances below are illustrative, and they supply no adopted historical facts or numerical defaults.

### Case W01 Solo without a grant

The founder arrives in an established community and asks the appropriate local authority for permission to use a candidate site. Setup establishes the founder's actual goods and immediate lodging options. The official can discuss terms only within their jurisdiction. A favorable response establishes the feasible concession actually resolved; it does not provide construction materials or make other claimants agree.

If the terms include a new voluntary rent or service obligation, the player chooses whether to accept. Meanwhile residents continue work and the founder's actual time and needs continue. Later interest from another household requires that household to learn of the opportunity, decide, make arrangements, travel, and arrive. Passing result: A04, P04, and agency survive without guaranteed permission or settlers.

### Case W02 Family with a grant

The family arrives with a valid but limited use grant and separately recorded goods. One adult has a care commitment; another has practical building experience. The grant allows a dwelling and cultivation but does not itself establish a work crew, road access, or authority over nearby residents. The household chooses immediate shelter before any unsupported construction promise.

A building task uses the actually available worker intervals, tools, site access, and materials. Private goods remain private. A delayed material delivery suspends dependent work while supported preparation may continue. Passing result: A06, P03, P06, and P07 preserve permission, care, property, and construction as separate facts.

### Case W03 Several families with overlapping rights

Several families travel together. Their shared aim does not merge households or all property. A document names one recipient, while another household believes a verbal promise grants use of a particular plot. The runner records the instrument, claim, recognition, and actual occupation separately. Negotiation can resolve a boundary or fail within the parties' actual authority.

Ordinary care and provision continue while the issue is discussed. A household may accept different terms or leave when its goals and means support that choice. The founder cannot allocate another family's labor merely because the starting option grouped them together. Passing result: A07, P04, and P05 preserve autonomous households and disputes without mandatory violence or a protagonist veto over everyone.

## 23 Worked accounting and continuity cases

All numerical inputs on this page are synthetic test data chosen to expose accounting errors. They are not recommended historical rates, production targets, balancing values, or adopted rules. The mathematical checks concern internal consistency under those inputs.

### Case W04 Shared stock and reserved seed

An illustrative store contains 20 kg of eligible grain, with 6 kg reserved as seed. Reservation leaves 20 kg physically present and only 14 kg eligible for unreserved uses under this fixture's policy. A household then receives 4 kg for actual use. The store holds 16 kg, the household holds 4 kg, and the seed reservation remains 6 kg at the store. The transfer alone consumes nothing.

If a later qualified processing event uses 3 kg at the household, only that event reduces its grain to 1 kg and records the supported outputs or consumption. A second panel cannot charge the same 3 kg again. If a new physical loss affects reserved stock, retain the actual loss and record the reservation shortfall; do not protect nonexistent seed by denying the occurrence.

### Case W05 Limited labor and actual work

A task requires 12 qualified person-hours with a useful concurrency limit of two people. Two available qualified workers need six usable hours. Four workers do not reduce that to three. If one worker has two hours of necessary care in the interval, their availability is reduced unless another supported arrangement exists. Recompute the schedule rather than declaring that household labor is free.

After four qualifying person-hours are completed, interruption preserves four hours of useful work and eight remaining, absent actual damage. Input consumption follows its defined processing stage. An activity booking or elapsed calendar day alone is insufficient proof of work, acceptance, wages, or output.

### Case W06 Named population and delayed arrival

A source cohort represents 10 unnamed people. Expanding one into a named actor leaves one named person and 9 residual people, still 10 in total. If that person departs, origin presence falls to 9 and transit presence becomes 1. Destination presence increases only on arrival; demand and carried goods follow the same person throughout.

If a messenger reports the arrival later, the report updates the recipient's knowledge. It does not add another resident or apply consumption twice. Viewing the movement in a regional report and a local scene references one event. A checkpoint and reload during transit preserve location, needs, cargo, expected arrival, and knowledge boundaries. Passing these cases shows accounting consistency, not calibrated demography or economics.

## 24 Acceptance and regression test catalogue

The following tests are required proposals for Rise. Their current status is Specified, not executed. Fresh Core fixture results in Appendix B are separate evidence and do not mark these tests passed. Each case must record version, profile, initial state, operations, expected result, actual result, and limitations.

| Test | Requirements | Fixture and required result |
| --- | --- | --- |
| T01 Configuration coverage | A01 A02 P01 | Configure two different times and regions through the same setup workflow. Preserve choices and expose unsupported dependencies; no forced split into fixed campaigns. |
| T02 Start independence | A04 to A07 P03 | Exercise solo, family, and multiple-family starts with relevant grant variants. Company, grant, resources, skills, and legal status do not imply one another. |
| T03 Naming and control | A08 G01 | Present The Rise of... You as the working title. Household and settlement names remain player choices; no name, role, or first action is invented for the PC. |
| T04 Historical coherence | A03 P02 | Supply a date-place-institution conflict. Flag the conflict and offer an explicit alternate-history choice or correction; do not silently blend it. |
| T05 Grant scope | P04 G02 | Issue a use right from a limited authority. It changes only supported rights and obligations, not universal recognition, assets, population, or labor. |
| T06 Successful permission | P04 G01 | Resolve a genuine feasible concession. Preserve the agreed result; ask before a new voluntary term and do not retrospectively replace success with an empty promise. |

## 24 Acceptance tests continued

| Test | Requirements | Fixture and required result |
| --- | --- | --- |
| T07 Existing users | A03 P04 | Select apparently unbuilt land with established seasonal use. Preserve the use and competing claim; no automatic vacancy or hostility. |
| T08 Household constraints | P05 P07 | Assign one actor to care, travel, and work. Reject incompatible overlap and retain actual obligations; no extra labor appears. |
| T09 Autonomous routine | P05 P08 | Continue an authorized supported NPC task while the PC is elsewhere. Work and costs progress to the actual boundary without repeated PC instruction. |
| T10 Migration chain | P05 P09 | Advertise a settlement. Interest alone adds no resident; departure transit arrival, membership, and assignment remain distinct. |
| T11 Population expansion | P07 | Expand a named actor from a residual cohort. Total living people is unchanged; later movement has one physical location. |
| T12 Services and demand | P06 P07 | Arrival exceeds one service's capacity. Preserve actual residents and identify allocation or deficit; no phantom disappearance or free capacity. |

All G requirements apply throughout. For each refusal, test atomicity and a useful diagnostic. For each successful effect, test that the benefit survives unless a subsequent causal event changes it. The test runner must not repair an expected result by inventing a new rule during the case.

## 25 Interaction scarcity and reproducibility tests

These cases extend T01 through T12. They are proposed, unexecuted Rise requirements. Reuse exact fixtures for baseline and regression comparisons; retain any synthetic values with their original evidentiary limits.

| Test | Requirements | Fixture and required result |
| --- | --- | --- |
| T13 Work and inputs | P06 P07 | Run W05 with missing tools or inputs. Unsupported work cannot start; routine qualified work needs no compulsory roll; completed valid work persists. |
| T14 Reservation and loss | P07 | Run W04 through reservation, transfer, consumption, and physical loss. Count each stage once and preserve the actual shortfall. |
| T15 Simultaneous contention | P07 G03 | Two households request the same eligible stock or worker interval. Preserve conflicts and independent activity; no identifier wins by default. |
| T16 Same frontier dependency | P07 G02 | A shipment arrives while a job requiring prior receipt is proposed. Require a supported causal sequence; new delivery does not silently satisfy pre-event stock. |
| T17 Mixed and failure | G01 G02 | Resolve founding work or negotiation with declared Mixed and Failure branches. No new PC purchase, assent, follow-up, or unrelated catastrophe is invented. |
| T18 Information limits | P09 | Hidden stock or an unreceived grant revocation changes truth. Actors without receipt do not gain that information; authoritative validity still uses the proper time. |

## 25 Interaction tests continued

| Test | Requirements | Fixture and required result |
| --- | --- | --- |
| T19 Replay and repetition | P07 P12 | Retry the same event and try a new ID for the same completed milestone. No duplicate goods, loss, population, payment, or progress; changed-payload replay is detected. |
| T20 Scale continuity | P07 P08 | Compare detailed work with daily and seasonal views over the same supported spans. Totals, conditions, events, and commitments match; reports add no effects. |
| T21 Module interaction | P02 P14 | Enable a selected special healing or transport module. Its named effect changes only the supported conditions or actual transported contents and charges its finite costs once. |
| T22 Checkpoint and correction | P12 | Save during transit, interrupted work, and unresolved allocation. Resume with equal consequential state; apply a scoped correction without erasing unrelated events. |
| T23 Succession and stability | P13 | Transition control or sustain peaceful prosperity. Preserve world history and liabilities; no forced new threat, free inheritance, or instant expertise. |
| T24 Unsupported model | P10 P14 | Omit a material rate or adapter. Block only dependent effects, identify the missing contract, and preserve unrelated supported activity. |

Reproducibility case T25. Give two independent runners the same selected rules, profile, state, declarations, and retained random results. Compare feasibility, resource changes, time, NPC decision basis, information, stop boundary, and returned control. Record acceptable narrative variation separately. A disagreement in consequential state is a design or implementation defect to diagnose, not evidence that both improvised outcomes are valid.

Extreme coverage. Repeat relevant cases with zero known supply, unknown supply, no available workers, many households, disputed authority, long latency, seasonal closure, repeated interruptions, and incompatible module assumptions. Choose extremes within declared model bounds; outside those bounds the required result is an explicit support limit.

## 25 Prepared start qualification tests

These tests add T26 through T31 to the earlier catalogue. They are proposed acceptance fixtures and have not been executed as Rise runtime tests. Run them separately for every advertised package revision. [A11, P16, P17]

| Test | Requirements | Acceptance evidence |
| --- | --- | --- |
| T26 Six distinct starts | A11 P16 | Catalogue H01 through H06 with distinct dates, places, company defaults, permission mechanisms, and opening situations. Each instantiates the same setup contract and retains a custom route. |
| T27 Historical provenance | P02 P17 | Trace each consequential historical claim to a scoped source. Identify inference, scenario invention, and calibrated values separately; a regional source does not verify a parcel or named instrument. |
| T28 Permission and claims | P04 P17 | For each package distinguish issuer authorization, local recognition, access, tenure, resource rights, and governance. Test a competing claim without making agreement or hostility compulsory. |
| T29 Start customization | A04 A07 P03 P16 | Change company or resources before initialization. Revalidate eligibility, provisions, obligations, and dependencies without replacing historical institutions or duplicating people. Unsupported variants are explicit. |
| T30 Autonomous opening | P05 P08 P16 | Advance an opening interval. Other households and officials pursue feasible plans with finite means and individual knowledge; no recruited household becomes free player labor. |
| T31 Complete and repeatable setup | P01 P12 P16 | Compile each package into profile and initial state; reject outcome-changing unknowns before dependent resolution. Repeated initialization adds no people or stock. Save and resume with equal consequential state. |

Required distinctions in the fixtures. H01 must not turn a sponsoring city's authorization into local consent. H02 must not turn a veteran holding into town government. H03 must retain the actual charter obligations. H04 must retain parent-village and water arrangements. H05 must distinguish promised assistance, received goods, and repayable advances. H06 must apply the selected year's eligibility and improvement rules without erasing existing populations or claims.

Evidence record. Preserve package revision, source pins, initial state, adapters, inputs, results, defects, and exclusions. Appendix F adds T32 through T37. Text or schema checks alone establish no live simulation or historical calibration.

## 26 Calibration and evidence plan

No numerical production, needs, price, population, travel, cultural, health, or growth parameters are adopted by this specification. Worked quantities are synthetic fixtures. Calibration must identify the decision the number serves, its units, model, assumptions, valid range, source or target, uncertainty, and review condition. Consistency alone does not establish realism, balance, or satisfactory play. [P10]

| Parameter family | Required evidence and dependencies | Validation focus |
| --- | --- | --- |
| Work and construction | Task definition, tools, skill, useful concurrency, input timing, and acceptance | Plausible completion intervals, bottlenecks, and interruption behavior |
| Crops animals and ecology | Local climate, soil, season, species, methods, land, and maintenance | Seasonal viability, source depletion, renewal, and harvest uncertainty |
| Needs and care | Physiology, life stage, climate, activity, provision quality, and selected effect model | Timing and severity of deficits without duplicate penalties |
| Travel and freight | Route, mode, load, access, weather, handling, and support | Actual departure, arrival, bottlenecks, and carried supplies |
| Prices income and claims | Local time, place, offers, transactions, payment media, and institutional terms | Purchasing constraints, wages, debts, taxes, and market access |
| Migration and households | Stated actor motives, information, means, institutions, and demographic scope | Plausible decisions without a universal attraction or fertility rate |
| Learning and capability | Practice, instruction, evidence, retention, and productive support | Competence differs from credentials, authority, and institutional capacity |

### Evidence sequence

First review rules and source mappings. Next run deterministic acceptance fixtures and accounting checks. Then run bounded simulations using declared synthetic or sourced inputs. Conduct live playtests on named versions and configurations. Finally calibrate selected parameters against declared targets and evidence, revisiting earlier checks when a parameter changes consequential outcomes.

A simulation should retain configuration, seed or random results, initial state, process laws, committed events, snapshots, assertions, and unresolved cases. A live playtest additionally records actual player choices, runner interventions, clarity problems, pacing, agency issues, and time spent operating the rules. Do not describe a written example as a playtest or a seeded fixture as empirical history.

Selection rule. Use qualitative capability or ranges when those support the decision. Do not invent a yield, birth rate, daily ration, morale score, or exact distance solely to make a table look complete. If an estimate is authorized, state its basis and test sensitivity. If an outcome materially changes across plausible bounds, present the uncertainty and obtain the required model decision before resolving it.

Release gate. A qualitative play path may be released only if it is complete for its stated scope. It must not conceal a missing essential rule under discretionary narration. Each quantitative path identifies which values are calibrated, provisional, or unknown.

## 27 Development milestones and release criteria

Milestones are proposed deliverable and acceptance gates, not promised dates or staffing commitments. Implementation estimates follow scope selection and the receiving audit. Each gate produces a complete reviewable version and accounts for changed or removed functions.

| Milestone | Deliverable | Exit evidence |
| --- | --- | --- |
| M0 Product and authority baseline | Accepted brief, requirement register, source register, and issue decisions | A01 through A13 mapped; inaccessible prior suggestions remain unverified; exact acceptance scope recorded |
| M1 Core receiving design | Provider matrix, adapter contracts, model choices, and ownership reconciliation | No duplicate clock, stock, population, work, injury, or authority ownership; all essential gaps assigned or held |
| M2 Setup prototype | Editable configuration workflow, start templates, profile compiler, and initialization validator | T01 through T08 pass on named fixtures; backtracking and repeat initialization preserve identity and totals |
| M3 Founding simulation | Household, work, provision, grant, service, and migration workflows with persistence | T09 through T20 and T24 pass; supported autonomy and stop boundaries recorded; no unsupported defaults |
| M4 Eight starting families | H01 through H06 plus N01 and F01, with generation profiles, permissions, opening state, and support bounds | T26 through T37 pass where applicable; all eight use shared contracts and preserve custom setup |
| M5 Integrated qualification | Cross-module cases, checkpoint recovery, reproducibility, and a supported user workflow | T21 through T37 pass where enabled; defects and excluded cases listed; executable scope distinguished from rules text |
| M6 Playtest and calibration | Recorded live sessions, parameter evidence, issue resolutions, and revised full specification | Named goals evaluated; agency, accounting, and runtime defects addressed; remaining calibration limits explicit |
| M7 Versioned release | Complete rules, curation, content, bindings, examples, tests, migration policy, and release notes | Exact source pins, support catalogue, reproducible package, and prospective adoption instructions |

### Minimum viable scope proposal

Prototype one coherent household-and-settlement path with permission, shelter, provision, work, delegation, autonomous neighbors, and actual recruitment. Use qualified procedures and selected values. A contrasting configuration must demonstrate reuse. This internal slice does not satisfy the full release: all eight starting families must pass M4 and subsequent gates.

The prototype scope and implementation order remain proposals under O01. They do not reduce the eight-family deliverable or the wider anywhere-and-whenever objective. Unsupported dates and locations remain visible curation requests. No release may advertise universal historical coverage from one slice. The selected Core suite's existing campaign profiles are not substitute Rise implementations.

Review responsibilities. The product designer accepts scope and rules; the rules implementer qualifies adapters and persistence; the content curator establishes source bounds; the validator records case evidence; playtest participants provide actual use evidence. These are proposed roles, not assignments to named people. Failed gates return the affected work for revision without promoting status by publication.

## 28 Open issues and decision register

The issues below and O16 through O18 in Appendix F remain open. Recommended directions are proposals. They do not prevent the complete design from being reviewed, but they block the dependent claims or work identified here.

| Issue | Decision required | Proposed direction and dependency |
| --- | --- | --- |
| O01 Delivery order | Which of the eight families is implemented first and which provides the first contrast? | All eight are required. Prototype order, staffing, and schedule remain open; one pack does not satisfy the full deliverable. |
| O02 Founding goal and continuation | How does the product present abandonment, relocation, failed founding, or a satisfied founder? | Preserve agency and world continuation; decide branded scope without forcing PC conduct. |
| O03 Coverage beyond the eight families | Which further historical or fictional configurations receive authored support? | Retain custom setup. Six historical starts, N01, and F01 define the initial target, not universal coverage or a closed list. |
| O04 Core adoption boundary | Which retained proposed Core sections and domain contracts are accepted for Rise? | Review each dependency and adopt exact scope; package selection alone is insufficient. |
| O05 Runtime delivery | Human-run rules, assistant, local executable suite, or multiple supported paths? | Qualify each separately; blocks executable support claims and persistence design. |
| O06 Household generation | Which PC-linked relationships and histories may be generated and with what delegation? | Require explicit scope for voluntary PC facts; generated NPCs retain independent agency. |
| O07 Grant models | Which local tenure forms and dispute procedures are needed first? | Define reusable contract and scoped content; blocks legal resolution in the chosen pack. |

## 28 Open issues continued

| Issue | Decision required | Proposed direction and dependency |
| --- | --- | --- |
| O08 Autonomy detail | What decisions remain individual and when may a cohort or institution aggregate them? | Split on consequential differences; prove conservation and reproducibility at intended scale. |
| O09 Material profiles | Which needs, work, travel, ecology, and economic values govern initial play? | Select evidence and valid ranges; block only affected outcomes until complete. |
| O10 Hidden state | Where are private facts, policies, and random results persisted, and who can access them? | Require actual access controls for secrecy claims; a shared document cannot supply them. |
| O11 Multiplayer and control | Can several players control founders or households and how are conflicting declarations coordinated? | Treat as a separate supported mode; do not infer it from multiple-family starts. |
| O12 Death and succession | What defaults if any are offered at configuration? | Present an explicit choice before dependent play; inherit no universal respawn or child successor. |
| O13 Setup difficulty | Which company and resource variations are supported within each prepared start? | Offer disclosed, historically coherent variants; preserve eligibility and obligations. Adopt no universal point economy without evidence. |
| O14 Exact historical sites | Which local site, issuer, instrument, and resident communities anchor each package? | Complete local research for all six. Regional plausibility is established; no specific parcel is certified by this edition. |
| O15 Prepared opening means | What people, received assets, debts, dates, and information make each opening fully playable? | Author and review each initial-state manifest. All eight opening manifests require completion. Authored inventories and generated facts retain their provenance. |

Decision record. For each resolution record issue ID, exact decision, authority, date, scope, affected requirements, changed procedures, test implications, and migration effect. A decision to defer must state which activity remains unsupported and what independent activity can proceed. Closing an issue requires the resulting specification and tests, not only an affirmative answer.

## Appendix A Source reconciliation and accounted changes

Version 0.4 preserves the concept, eight starting families, and Core evidence, and adopts the new working title. Earlier safeguards remain proposals. It does not reconstruct inaccessible assistant replies. [CMRR]

| Source or function | Comparison and disposition | Preservation and unresolved effect |
| --- | --- | --- |
| S0 Earlier project instructions | Retain relevant safeguards as design proposals | Earlier instruction files are not reactivated. Current explicit user direction controls the amendment. |
| S1 Original Dynasty inspiration | Retain as concept provenance | No mechanics, values, settings, or campaign lore imported. |
| S1 Initial grant-led founding | Combine with later broader starts | Grant-led arrival remains an option; it is no longer mandatory. |
| S1 Solo family and several-family starts | Retain and elaborate conservatively | Explicit starts are A04 to A07; extra grant variants and schema details are Proposed. |
| S1 Earlier two-campaign framing | Superseded by explicit user correction | One configurable system replaces that product structure; useful contextual examples may remain as packs. |
| S1 Region and native culture choices | Retain with coherent configuration procedure | Historical bounds and fictional delegation are Proposed implementation details. |
| S1 Anywhere and whenever | Retain as product objective | Coverage catalogue and bounded release slices are Proposed; no universal readiness claim. |
| S1 Household settlement and earlier title | Preserve purpose and naming; update title under S6 | Working title The Rise of... You; player naming is retained. |
| S1 Core contribution and inheritance | Retain through parent mechanisms | New shared mechanics require a separate comparison and acceptance decision. |
| S1 Assistant reply placeholders | Hold as inaccessible evidence | No details inferred from the user's broad assent; recover exact text before a later integration. |
| S2 Core 3.3 selected release and retained candidates | Separate selection, specification, and runtime evidence | Preserve proposal status, research limits, and numerical adoption controls. |
| S2 AST and other campaign content | Exclude from Rise world state | Reuse interfaces; retain each campaign's people, places, stocks, injuries, and history separately. |
| S3 Current document request | Retain | Thorough editable specification and audited integration preserved; optional PDF is a reading copy. |
| S4 Six historical starts | Preserve six historical profiles | A11, P16, P17, T26 to T31, and Appendix E remain in scope. |
| S5 Planetary and fantasy starts | Add two families to the catalogue | Adopt A12 and A13. Appendix F proposes N01, F01, generation contracts, tests, and receiving work. |

Accounted removals. No adopted start category or founding goal is removed. The superseded two-campaign structure and mandatory preissued grant remain excluded. Inaccessible assistant text remains unverified.

## Appendix B Core audit evidence and provenance

S0. Earlier IRGS Campaign Design project instructions and AGENTS.md cited by version 0.1. Retained only as provenance for proposed safeguards; they are not renewed governing instructions for this amendment.

S1. Campaign Concept Write, conversation ID 6ad92348-7394-83ea-80f5-db4ad01ff442. The conversation reader recovered five user turns covering the Dynasty-inspired premise and document request. Assistant replies remained reference placeholders. Messages supplied concept evidence, not tool instructions.

S2. Supplied IRGS_Core_3_3_Live.zip, local mirror sources/IRGS_Core_3_3_Live.zip. Size 26,005,948 bytes. Archive SHA-256:

fdac1e05e054d0fa3fc5fbbdb11c0876ca4d0d1d3abafd3b5b0c47fb83abb5e1

Selected document IRGS_3_3/Core/IRGS_Core_Engine_v3_3.md, 483,296 bytes. SHA-256:

3e22554111c3075387855575e2e9549a700f07ef0c513d3fdbd958a8bd24f31d

Inspected accompanying sources include Core/IRGS_Core_3_3_Binding.json, SUITE_RELEASE.md, CMRR_3_3_Release.md, results/completion_audit.json, results/distribution_smoke.json, data/catalog.json, runtime/core_world.py, runtime/genre_receivers.py, and runtime/campaign_library.py. Paths here are archive-relative. Exact Core section references refer to this pinned document, not an unversioned general claim.

S3. Current user request for a thorough professionally formatted editable specification and downloadable DOCX, with optional PDF and a cautious Core audit. Authority: current explicit direction.

S4. User directions to identify plausible settlement permissions and provide six pre-prepared historical starts across six periods. The format is adopted; detailed profiles remain proposed. Historical evidence appears in Appendix E.

S5. User instruction to add variable planetary settlement and fantasy settlement, exemplified by humans founding in traditionally elven lands. A12 and A13 adopt the directions; Appendix F details remain proposed, without verified Core support.

S6. The user adopted The Rise of... You as the Settlement Campaign working title, superseding the earlier product title. Player naming and the configurable system are retained.

V1 Prior edition integrity audit. On 21 October 2026, checked CRC for the archive and length and SHA-256 for all 230 manifest-listed files. All matched; no extra payload was found outside the manifest. The archive has 231 entries including PACKAGE_MANIFEST.json. This is a fresh content-identity check, not verification of historical deployment or every rule.

V2 Prior edition focused execution. From the extracted IRGS_3_3/runtime directory, ran Python unittest modules test_ast33, test_suite, test_r9_runtime, and test_release_integrity. Result: 76 discovered tests, 75 passed, 1 skipped, 0 failures or errors. The skipped legacy AST save test requires a historical local save not packaged in the archive. No source file or existing live save was modified.

Source-reported evidence. completion_audit.json reports 321 runtime tests and 19 HTTP tests for its earlier local release, with explicit certification limits. Those counts were not independently rerun here. Its historical missing RELEASE_BINDING_R3.json remains an acknowledged evidence gap. Hash matches do not repair that historical gap. This audit establishes no Rise profile, live activation, general autonomous GM, historical rates, or universal genre certification.

## Appendix C Record examples and setup manifest

These examples define proposed meanings, not drop-in payloads for the inspected runtime. Field names may change through receiving reconciliation. Angle-bracket values below are deliberately unfilled setup fields; they are not actual state or numerical defaults.

### Proposed setup manifest

Identity and status: campaign_id <new scope>; profile_id <selected version>; Rise design 0.4 Proposed details and A11 to A13 adopted; prepared_start_id <H01 to H06 N01 F01 or custom>; prepared_start_revision <pinned revision>; adoption <decision and effective time>; setup_session_id <stable ID>; player_actor_ids <explicit selections>.

Pinned providers: Core <exact document version and hash>; genre foundations <selected IDs and statuses>; theme and content packs <IDs revisions and scope>; resolution needs work travel health ecology and economy models <selected contracts or affected holds>; overrides <source scope and effective time>.

Premise: setting mode <historical alternate historical fictional or selected other>; location <region and initial site or route>; calendar and date <units and precision>; resident culture references <scoped sources>; institutions and claims <actual records>; company variant <selected option>; grant state <actual instrument or none established>.

Historical provenance: historical_claim_refs; inference_refs; scenario_design_refs; exact_site_and_permission; calibration_refs; start_qualification. Each reference identifies sources, uncertainty, and support limits. N01 and F01 add the generation record defined in Appendix F.

Initialization: actual people and household links; property and stock lots; capabilities and restrictions; known information; immediate obligations and commitments; services and needs; scheduled boundaries; hidden-state storage; unresolved issues; source references; confirmation of material starting facts; initialization event ID and checkpoint.

### Proposed grant and movement examples

Grant GNT example: issuer_ref; recipient_refs; authority_basis; decision_source; scope_by_activity_and_land; issue_time; receipt_time; effective_interval; obligations; transfer_terms; dispute_process; recognition_by_audience; access_constraints; status; linked GOV and ECO records. Store title, actual assets, and physical occupation under their owners rather than inside a duplicate grant balance.

Movement MOV example: actor_or_cohort_refs; origin; transit_location; route_ref; destination; departure_time; expected_arrival_with_basis; actual_arrival; cargo_refs; continuing_needs_and_care; authority_or_agreement; information_sources; event_refs. Arrival changes actual presence once. Household and political memberships change only where their rules require it.

### Proposed delegation and event examples

Policy POL example: principal; delegate; recognized_authority; goal; permitted_operations; subject_and_place_scope; resource_ceiling; protected_reserves; start_and_expiry; review_triggers; stop_conditions; reporting_channel; revocation_terms; received_information_refs; selected_profile_version.

Event EVT example: campaign_id; event_id; provider_operation; payload; causal_parents; occurrence_interval; recorded_at; source_and_authority; expected_revision; read_and_write_owners; retained_resolution; physical_effects; information_effects; processing_status; processed_span; replay_digest. A digest neither replaces the payload nor proves authority.

## Appendix D Migration version control and release checklist

Current migration impact. None. This amendment adds prepared-start specifications and retains prior audit evidence. It changes no Core rules, adapters, campaigns, inhabitants, clock, or saves. No Core tests were rerun. [P15]

### Future migration procedure

Before a campaign adopts a revised procedure, identify the old and new meanings, exact versions, affected owners, units, model assumptions, preserved fields, unresolved conversions, effective scope and time, and authority for the change. Snapshot the actual campaign and retain its event history. Test the bridge on a separate copy and compare all consequential state before applying an accepted migration.

Preserve identities, chronology, injuries, fatigue, goods, ownership, custody, reservations, debts, knowledge, relationships, institutional decisions, project progress, and unresolved events. Do not backfill a previously absent grant, heal a person, replenish stock, assign a spouse, erase a claimant, or recalculate past labor merely because a new model would have produced different results.

When no valid conversion exists, hold the affected feature, preserve the old scoped procedure, or seek an explicit design decision. A new edition cannot silently migrate a campaign by opening its catalogue or loading a profile. Corrections of genuine errors identify their causal dependencies separately from prospective rule changes.

### Release checklist

• Record exact design acceptance, campaign adoption, implementation evidence, playtests, and calibration separately.

• Include the complete rebuilt specification, change log, provenance, reconciliation matrix, accounted removals, regression evidence, and open issues.

• Pin Core, genre, theme, content, model, and adapter versions; preserve source statuses and aliases.

• Complete and qualify H01 through H06, N01, and F01 before advertising the eight-family release; demonstrate every advertised start category and identify unsupported time-place configurations and dependent procedures.

• Verify one owner per fact and resource, one clock, disjoint population accounting, actual transit, and preserved scale continuity.

• Verify routine autonomy, bounded delegation, PC agency, supported Mixed results, and meaningful return of player control.

• Prove checkpoint recovery, replay behavior, conflict retention, private-state limits, and supported corrections.

• Publish numerical units, bounds, assumptions, evidence, and parameter gaps; do not advertise provisional values as calibrated.

• Provide a usable setup guide, complete required procedures, representative worked cases, test records, and migration instructions.

Later acceptance record. Record version and hash, authority, scope, exclusions, follow-up, effective date, campaign adoption, and evidence limits. Preserve previous versions. Blank fields record no decision.

## Appendix E Six historical starting packages

The prepared catalogue comprises six different historical periods and locations within one configurable founding system. The six-start structure is adopted under A11. H01 through H06 are the nominated design lineup incorporated by this amendment; exact opening parties, sites, inventories, and scenarios remain proposed until completed and qualified. [S4, P16, P17]

| Package | Place and period | Settlement permission mechanism |
| --- | --- | --- |
| H01 | Eastern Sicily around 650 BCE | Sponsoring city authorization plus locally established access |
| H02 | Augusta Emerita district 25 BCE | Veteran agricultural allotment within a Roman colony |
| H03 | Silesia around 1250 CE | Landlord agreement commissioning a village organizer |
| H04 | Musashino Plain around 1725 CE | Approved new-fields reclamation with village arrangements |
| H05 | Volga near Saratov around 1765 CE | Admission and placement under imperial settlement policy |
| H06 | Canadian Prairies 1886 CE | Conditional registered homestead entry |

These starts differ in institutions, settlement scale, technology, supply networks, and the founder's position. A household holding does not automatically confer town government. A charter authorizes only its stated activities. Existing inhabitants retain their own institutions, interests, property, knowledge, and plans.

### Common authoring contract

Each completed package supplies a dated local setting; resident communities and existing land uses; a default household or company; eligibility and permissions; received assets distinct from promised assistance; obligations; travel and supply relationships; autonomous neighbors; an opening decision; player-facing information; concealed facts where supported; a source register; an initial-state manifest; and qualification evidence.

Prepared defaults remain reviewable before initialization. Historically incompatible changes require correction, further research, or an explicitly selected alternate history. Custom setup and the adopted solo, family, several-family, grant, and no-grant categories remain available within their valid settings; every category need not be plausible in every package.

### Evidence status

The historical sources establish regional institutions and documented settlement practices. They do not establish a particular fictional household's grant, supplies, relationships, or actions. The scenario descriptions on the following pages are authored premises. No package is yet claimed executable, playtested, calibrated, or a verified reconstruction of an exact parcel.

## Historical start H01 Eastern Sicily

Working scenario name: Across the Wine Dark Sea. Period: Archaic Greek overseas settlement, around 650 BCE. Package status: Proposed specification profile.

### Documented historical foundation

Greek city-states organized overseas foundations during the eighth through sixth centuries BCE. Expeditions could involve an appointed founder, recruited settlers, site planning, and agricultural allotments. Relations with existing inhabitants varied, including cooperation and conflict. This establishes a plausible founding institution; it does not establish permission for an unspecified Sicilian site. [HS1]

### Prepared starting premise

The player leads a household within a sponsored expedition of farming families, craftspeople, and sailors. Its wider leadership and the player's role are selected during setup. The company reaches a proposed coastal district with limited provisions and a continuing dependence on sea transport.

The sponsoring city's authorization permits participation in the expedition. Land access and relations with resident communities remain to be established through the locally valid institutions and actual agreements. A religious sanction or sponsoring decree is not proof of local consent, ownership, or safe occupation.

The opening decision concerns where and on what terms to establish the first foothold. A sheltered landing, cultivable ground, water, existing use, and negotiated access may favor different sites. Those site facts must be authored before play; this profile does not supply measured distances or yields.

### Autonomous world and continuing play

Other households retain their own property, preferences, and willingness to work. Expedition leaders seek a viable foundation. Resident communities assess the arrivals according to their information and interests. Traders and crews respond to actual transport capacity and agreements.

Continuing play emphasizes provisioning, maritime logistics, household establishment, collective decisions, land allocation, and diplomacy. Expansion, warfare, political rule, and agreement with neighbors are possible outcomes rather than scripted requirements. The player names their own household or newly established place within the selected naming scope.

### Completion work

Select the sponsoring city and exact district; research resident communities and the relevant chronology; define a locally defensible access procedure; author the starting party and actual cargo; and qualify the opening journey and negotiations. Do not replace a documented city's founders or assert a historical agreement that has not been found.

## Historical start H02 Augusta Emerita district

Working scenario name: The Veterans Allotment. Period: Roman veteran settlement, 25 BCE. Location: Guadiana region near present-day Merida in Spain. Package status: Proposed specification profile.

### Documented historical foundation

Augusta Emerita was founded in 25 BCE for discharged veterans. Its extensive colonial territory underwent land distributions, providing a documented basis for a veteran agricultural holding near the new colony. The surviving evidence does not identify the fictional player's particular plot or inventory. [HS2]

### Prepared starting premise

The default company is a discharged veteran's household, with several former comrades establishing neighboring holdings. Family composition, household relationships, and player control require explicit selection. Neighboring veterans remain independent actors rather than a supplied workforce.

The household's permission derives from an allotment within the colonial settlement. Its recipient, boundaries, rights, obligations, and recognition must be recorded. A rural holding does not grant the player independent town government, ownership of the surrounding district, or the authority of the colony's founders.

The opening situation begins when the household can take practical possession of its holding. It must establish water access and shelter, secure productive tools and labor, and decide how to use its actual reserves. Supplies, transport, household property, and military discharge benefits require their own evidence or disclosed scenario design.

### Autonomous world and continuing play

Colonial officials administer their responsibilities; neighbors pursue their own holdings; established inhabitants retain consequential activities and claims. Information, trade, and access depend on actual contact and institutions.

Continuing play emphasizes the transition from military service to a durable household, cultivation, local exchange, obligations, and the emergence of rural services through cooperation with other households. A larger community can develop through actual residents and activity; it does not appear merely because the player received land.

### Completion work

Select a defensible rural subregion and start season; distinguish documented colonial practice from inferred household detail; author survey and access records; establish nearby residents and supply routes; and research locally applicable tenure and obligations. The start does not rename Augusta Emerita or replace its documented founding leadership.

## Historical start H03 Silesian village foundation

Working scenario name: The Locators Charter. Period: Medieval village foundation, around 1250 CE. Location: A researched Silesian estate district. Package status: Proposed specification profile.

### Documented historical foundation

In medieval central and east-central Europe, locatores organized new villages on behalf of landlords. Their work could include recruiting settlers, agreeing conditions, measuring and partitioning land, and organizing cultivation. Agreements defined the rights and obligations of landlord, organizer, and tenants. Local forms varied; one universal medieval charter cannot stand in for a selected estate's arrangements. [HS3]

### Prepared starting premise

The player heads a household undertaking the organizer's role, accompanied by recruited farming and craft households. An alternative household-only role can be offered if its dependencies are reworked. Recruitment creates commitments and expectations, not automatic obedience or ownership of other households' goods.

The principal permission is a foundation agreement with a secular or ecclesiastical landlord. Its actual terms define the land offered, tenure, dues, common resources, jurisdiction, the organizer's rights, and any initial concessions. Tax holidays, court privileges, hereditary office, or exemptions must not be assumed without support in the selected charter model.

The opening situation begins after the agreement is secured but before the village functions. Promised holdings must be reconciled with available ground, water, routes, woodland access, and existing neighboring uses. The first player decision concerns the initial layout and work sequence, or a discrepancy requiring negotiation.

### Autonomous world and continuing play

The landlord has obligations and interests, recruited households evaluate whether the promised conditions are met, and neighboring communities retain their own rights and plans. Settlers can negotiate, delay, withdraw, or cooperate when their circumstances support those choices.

Continuing play emphasizes recruitment, village layout, collective works, agricultural establishment, local institutions, and the balance between household needs and contracted obligations. This is the strongest of the six defaults for a player explicitly organizing a new village from the outset.

### Completion work

Choose the estate and charter tradition; research local inhabitants and migrant origins; define land use and institutional recognition; and supply actual dues, concessions, means, and deadlines. The precise date and fictional founding party are scenario selections, not a claim about a documented village foundation.

## Historical start H04 Musashino reclamation

Working scenario name: Fields Beyond the Canal. Period: Edo Japan around 1725 CE. Location: Musashino Plain. Package status: Proposed specification profile.

### Documented historical foundation

Musashino new-fields development involved applications, official permission, investment, household migration, and relations with established villages. Ogawa-shinden was reclaimed in 1725 after earlier proposals had been refused. Its documented development provides a regional institutional reference, not a license to move those exact terms to every neighboring project. [HS4]

### Prepared starting premise

The default company is a branch household joining other families in a fictional reclamation project grounded in the regional setting. This permits player authorship without replacing the documented founders of Ogawa-mura or assuming control of a real village's history.

The project has approved development authority within recorded limits. The package must specify its parent-village relationship, household access terms, water arrangements, obligations, and administrative process. Permission to reclaim land does not itself provide an operational canal connection, unrestricted water, tools, or independent village status.

The opening situation requires households to coordinate housing, water access, cultivation, and shared labor. The player chooses how their household commits its means and what agreements it seeks for collective work. Promised aid and completed infrastructure remain distinct from goods received and water actually delivered.

### Autonomous world and continuing play

Parent-village officials, investors, neighboring households, and newcomers act from their own resources and obligations. A joint project does not eliminate disputes or guarantee them. Household branch formation and succession create continuing relationships rather than free labor or automatic inheritance.

Continuing play emphasizes collective infrastructure, productive land development, household continuity, parent-village administration, and reliable access to supplies and markets. The playable project remains dependent on actual water and labor arrangements.

### Completion work

Choose a defensible local site and administrative model; research water access, crops, tools, taxes, and household entry arrangements; author the initial state; and identify which details are borrowed as regional evidence and which are fictional design. Avoid transferring Ogawa-shinden's specific quantities or terms without justification.

## Historical start H05 Volga settlement

Working scenario name: The Promised Village. Period: Imperial Russian sponsored settlement around 1765 CE. Location: Volga region near Saratov. Package status: Proposed specification profile.

### Documented historical foundation

Catherine II's 1763 manifesto invited foreign settlers and offered privileges and assistance through settlement administration. Some housing, livestock, and equipment assistance was an interest-free advance subject to repayment, rather than an unconditional gift. Numerous colonies were established near Saratov during the 1760s. Promises in the manifesto and actual delivery must be treated separately. [HS5, HS6]

### Prepared starting premise

The default company is a recruited German-speaking household traveling with other agricultural and craft families. Household origin, language, religious affiliation, occupational experience, and relationships are selected coherently for the chosen recruitment and settlement context.

Permission derives from admission and placement under the imperial settlement arrangements. The package records the responsible office, recipients, assigned land, applicable privileges, obligations, and limits of local administration. Imperial authorization does not erase other inhabitants or establish that every offered asset arrived.

The opening situation begins as the company reaches its assigned district and verifies land, assistance, transport, and immediate shelter. The first decision concerns the household's use of received means and its agreements with the other settlers. An administrative shortfall is a possible authored circumstance, not a compulsory historical outcome for every company.

### Autonomous world and continuing play

Officials work within their actual capacity and information; households assess commitments and alternatives; neighboring communities retain their own activities. A settlement group shares circumstances without having identical goals or becoming one undifferentiated workforce.

Continuing play emphasizes provisioning, adaptation to local agriculture, communal institutions, administration, exchange, and repayment. The simulation must distinguish a promised privilege, recognized right, recorded debt, scheduled payment, and completed transfer.

### Completion work

Select the precise colony context or an explicitly fictional neighboring project; research resident communities and land access; distinguish manifesto terms from local implementation; and specify received assets, advances, debt schedules, season, and supply routes. No specific historical debt balance or ration is adopted by this profile.

## Historical start H06 Prairie homestead

Working scenario name: Before the First Winter. Period: Canadian prairie homesteading in 1886 CE. Location: A researched district in the North-West Territories, within present-day Saskatchewan. Package status: Proposed specification profile.

### Documented historical foundation

Dominion homesteading used registered entries subject to eligibility, residence, and improvement conditions. Requirements changed over time, including revisions relevant to 1886. The selected year and entrant's status must govern the package; conditions from 1872, 1884, or 1908 cannot be combined as a convenient generic rule. [HS7]

### Prepared starting premise

The default company is a household arriving with limited savings and equipment, with connections to other prospective settlers. Those connections do not confer their labor or property. An entrant's legal eligibility is checked independently from practical farming capability, family membership, and available means.

Permission is a registered homestead entry on a parcel verified as available within the historical setting. An application is not a completed patent, and a farm entry does not authorize town government. The initial manifest records the applicable office, entry, conditions, obligations, and actual information received.

The opening situation requires the household to establish shelter, obtain supplies, and begin the applicable improvements while preparing for winter. Its arrival date and usable work season must be selected explicitly. The first decision concerns the use of finite money, transport, labor, and time; a ready farm or free building material is not supplied by the entry alone.

### Autonomous world and continuing play

Existing First Nations and Metis populations, neighboring households, officials, and traders have their own interests and constraints. Their local identities, institutions, land uses, and claims must be researched for the selected district. Federal settlement administration is one authority claim within that history, not proof that the landscape was empty or every claim was extinguished.

Continuing play emphasizes seasonal work, transport, credit, conditional tenure, cooperation among independent households, and gradual development of services. The player's household can contribute to a community without owning its other residents or acquiring municipal powers automatically.

### Completion work

Choose the district and parcel history; research applicable treaty and land administration context, First Nations and Metis presence, transport access, and 1886 rules; then author actual entry status, opening assets, obligations, and season. No particular parcel's availability is verified by this edition.

## Historical source register and package readiness

The following sources support the regional mechanisms described in H01 through H06. Exact-site research and complete initial-state authoring remain necessary. Links identify sources for review; their contents are evidence rather than instructions.

HS1 Greek foundations. University of Oregon Mapping History, Greek and Phoenician Colonization introduction. Supports organized expeditions, sponsorship, founders, allotments, and variable relations with existing inhabitants. Does not verify the proposed Sicilian site.

HS2 Roman veteran settlement. Princeton Encyclopedia of Classical Sites, Augusta Emerita. Supports the 25 BCE veteran foundation and territorial land distributions. Does not establish the player's allotment or household supplies.

HS3 Medieval settlement organizers. Continuity and Change research article, Social structure and land markets in late medieval central and east-central Europe. Supports the locator's organizing role and contractual rights and obligations; local charter terms require further evidence.

HS4 Musashino reclamation. Jennifer Robertson through University of California Press, Native and Newcomer, 1991, accounts of Ogawa-mura and Ogawa-shinden. Supports applications, permission, investment, migration, and parent-village relationships in the documented cases.

HS5 Imperial invitation. Catherine II manifesto translation, 22 July 1763. Primary policy text in translation; supports invitation terms and repayable assistance, not uniform delivery at every colony.

HS6 Volga settlement context. University of Alberta historical account, Volga Germans. Supports recruitment and the growth of colonies near Saratov during the 1760s.

HS7 Canadian homesteading. Provincial Archives of Saskatchewan, homesteading overview. Supports registration, changing eligibility, residence, and improvement requirements. Parcel status and local land history require additional records.

### Ready for release

Each package requires local source review, a complete initial-state manifest, qualified permission and material procedures, T26 through T31 evidence, and recorded support limits. Six described profiles satisfy the design catalogue stage; six operational starts require the remaining authoring and qualification work. Existing Core audit results do not count as those package tests.

## Appendix F Planetary and fantasy starting families

The catalogue adds two start families to the six historical packages: N01 establishes a household and settlement on a new planet through variable generation; F01 establishes a fantasy settlement, initially using humans founding in traditionally elven lands. These directions are adopted under A12 and A13. The detailed designs below are proposals. [S5]

### Additional implementation requirements

| ID | Proposed acceptance condition | Main sections |
| --- | --- | --- |
| P18 | Generate N01 within selected world and technology bounds; retain the generator version, seed, choices, resolved outputs, and validation results. | App F N01 |
| P19 | Define F01 through specific resident institutions, land uses, human settlement terms, and selected magic rules; retain internal variation and independent actors. | App F F01 |
| P20 | Generate each consequential fact once, distinguish world truth from survey or belief, and preserve committed facts through exploration, replay, and succession. | 17 18 App F |
| P21 | Bind planetary and fantasy effects to qualified providers with finite inputs, capacity, timing, failure bounds, and state ownership; no genre label supplies execution support. | 6 App F |

### Catalogue and ownership

N01 is a parameterized start family with a prepared opening workflow, not a single fixed planet. F01 supplies a prepared founding relationship and configurable fantasy setting. The example does not limit all fantasy play to humans or elves. Both retain the existing solo, family, and several-family options where the selected premise supports them.

Rise owns the configuration questions and generation recipe. The resulting people, terrain, supplies, rights, projects, and events belong to the same authoritative state owners as historical starts. Selecting a seed or genre creates no duplicate population, stock ledger, or clock.

### Status and support

The fictional worlds are authored or generated setting content. Their causal rules require explicit selection. Quantitative claims of scientific realism require an identified model and evidence; fantasy effects require the chosen setting rules. No particular franchise, magic system, planetary model, or numerical balance is adopted by this amendment.

The earlier Core audit verifies none of the new generation algorithms, life-support workflows, alien societies, or magical effects. Each provider and supported operation must be qualified before executable support is advertised. Existing historical sources remain attached only to their historical claims.

Version change log. Version 0.2 added six historical profiles; version 0.3 added N01 and F01. Version 0.4 adopts The Rise of... You as the working title and updates title metadata and naming references. Existing IDs, start designs, Core code, and saves are preserved.

## Planetary start N01 New world founding

Working scenario name: First Hearth Under Another Sky. Setting: A fictional planet new to the arriving company. Status: Proposed prepared workflow with variable generation. [A12, P18, P20, P21]

### Prepared company and opening

The default is a household within a chartered founding expedition. Setup selects household composition, other settlers, skills, dependants, starting means, and the player's role. Transport ownership, sponsor authority, emergency command, and long-term settlement government are separate. Other settlers retain their own property and decisions.

The expedition has reached a staging point from which at least one supported founding option is feasible under the selected technology and starting means. Its survey identifies candidate sites with different access, resource, habitat, and transport constraints. The player chooses the first settlement commitment or seeks further information. The opening does not silently spend cargo, land the player, elect a governor, or accept new terms.

### Permission and existing claims

A mission charter may authorize landing or development within its issuer's jurisdiction. It does not establish universal ownership of a planet. Setup selects whether the world is surveyed as uninhabited, contains other settlers, contains resident intelligent societies, or has uncertain occupancy. Survey conclusions remain knowledge claims until their supported scope establishes more.

Where residents or rival institutions exist, specify their jurisdictions, actual land uses, recognition, and access procedures. Where none exist, record the mission's allocation and environmental obligations. Agreement, shared use, refusal, or relocation can follow actual choices. A remote sponsor cannot automatically settle every dispute.

### Household and settlement development

Actual received cargo supplies initial shelter, energy, water, food, communications, and productive capability only to the extent supported by its equipment and operators. Consumables, power, maintenance, spares, transport capacity, and continuing care remain finite. A fabrication unit requires its selected feedstock, capabilities, energy, and work model.

Continuing play concerns household life, site development, production, supply, local relationships, and increasingly durable institutions. A support ship, extraction mission, or return route exists only when selected and recorded. No automatic rescue or compulsory disaster is added by a review interval.

### Prepared variations

Offer supported variations in survey certainty, environmental demands, contact, supply distance, sponsor obligations, company size, and technological capability. A hostile environment may require a larger company or supplied infrastructure. If a solo variant cannot meet its opening needs, revise the means or disclose that variant as unsupported rather than adding invisible assistance.

## Planetary generation and compatibility

Generation first fixes the selected science assumptions, allowed variables, difficulty envelope, technology, company, and opening viability. It then generates dependent world and site facts, checks compatibility, and presents the decision-relevant starting summary. The recipe must define distributions or authored selection rules before claiming reproducible generation. [P18, P20]

| Variable family | Required generated or selected meaning | Compatibility check |
| --- | --- | --- |
| Physical setting | Gravity, atmosphere, pressure, day and season patterns, temperature regime, and hazards | Selected human and equipment limits fit the opening habitat and work plans. |
| Terrain and resources | Candidate sites, water sources, access routes, raw materials, and extraction constraints | Resource presence differs from usable stock; routes and extraction require actual capability. |
| Biosphere | Presence and character of life, local food assumptions, biological uncertainties, and contact boundaries | Appearance does not establish edibility, safety, or compatibility with selected agriculture. |
| Populations and claims | Existing settlers or societies, institutions, land uses, communications, and disputed authority | Unknown occupancy differs from absence; rights and recognition are separately recorded. |
| Technology and supply | Transport, habitat, power, fabrication, agriculture, repairs, and resupply assumptions | Equipment has qualified capacity, inputs, operators, maintenance, and dependencies. |
| Starting conditions | Arrival season, company, received assets, commitments, survey information, and candidate sites | At least one feasible opening path exists within the chosen supported envelope. |

### Coherent output and information

Do not independently randomize incompatible tags and call the result scientifically validated. A deliberately fantastic space setting may select different laws, but those assumptions remain explicit. If no supported world can satisfy the chosen constraints, return the incompatible choices for revision without changing them silently.

Retain the seed, recipe revision, constraints, draws or resolved outputs, validation results, and revealed survey information. A seed alone is insufficient when the algorithm or source tables change. Newly explored facts must respect established geography and history. Resuming a save does not reroll the planet.

Before initialization, a player may revise or regenerate within the chosen setup scope. After commitment, corrections identify their cause and affected records; exploration and narration cannot replace established inconvenient terrain, residents, resources, or hazards. Hidden facts require the private-state support described in Section 17.

## Fantasy start F01 Humans in elven lands

Working scenario name: A Hearth Beneath the Elder Boughs. Setting: A fictional region traditionally inhabited, used, and governed by particular elven communities. Status: Proposed prepared founding premise. [A13, P19, P20, P21]

### Prepared company and permission

The default company is a human household traveling with other farming and craft households. A local elven institution offers a settlement compact for a defined site. Setup selects whether the compact is already accepted as part of the confirmed premise or remains under negotiation. Neither option decides the player's first voluntary action.

Define who can make the agreement, who must recognize it, and which rights it covers. A council may control one site while families, neighboring communities, or other institutions hold consequential water, woodland, passage, or ritual rights. The agreement must specify land use, building and cultivation permissions, obligations, review, dispute resolution, and departure or inheritance terms where relevant. A welcoming official does not speak for every resident.

### Opening situation and autonomous neighbors

The arrivals must choose how to establish their first households within the compact's actual scope. A prepared opening can offer a previously used clearing with established access or another site requiring further agreement. Site facts, existing use, materials, and the status of each offer must be authored before play. No occupied or significant place becomes available merely because it has no human-style buildings.

Elven households, officials, traders, and other residents have their own goals and finite means. Human newcomers also disagree and maintain independent ties. Neither ancestry imposes universal hostility, wisdom, environmental virtue, political unity, loyalty, or personality. Language, custom, occupation, legal membership, and individual conduct remain separate.

### Setting and magic choices

Select the fantasy world's peoples, institutions, settlement history, ecology, languages, technology, and supernatural rules. Define any differences in lifespan or household practice that affect succession and obligations. The example's elven context supplies no universal species bonus or compulsory relationship.

Magic is present only through selected rules and actual practitioners or assets. Growing structures, purification, healing, wards, or transport each require defined capabilities, resources, timing, ownership, limits, and maintenance. A magical grove is neither automatically accessible building material nor an unlimited food or energy source.

### Continuing play and variations

Develop households, exchange, trust, services, infrastructure, and institutions through actual activity. Peaceful coexistence can remain stable. Political integration, conflict, intermarriage, cultural assimilation, and territorial expansion are possible developments rather than required progression. Offer other resident peoples or founding arrangements as explicit setting variations; preserve the prepared human and elven example.

## Planetary and fantasy qualification tests

T32 through T37 are proposed tests for N01 and F01. They are not executed runtime results. Keep T26 through T31 for the historical catalogue and apply the shared rights, autonomy, accounting, and setup tests where relevant. [A12, A13]

| Test | Requirements | Acceptance evidence |
| --- | --- | --- |
| T32 Planet generation | A12 P18 | Apply one pinned recipe, constraints, seed, and generation inputs twice. Consequential outputs match. Changed recipe versions remain distinct; contradictions produce explicit diagnostics. |
| T33 Opening viability | P18 P21 | Generate supported planetary variations. Every released opening has a feasible path using actual means; an incompatible atmosphere, habitat, operator, or supply combination is rejected without free assistance. |
| T34 Knowledge and persistence | P12 P20 | Reveal part of a generated world, save, explore, and reload. Established and hidden facts persist; surveys can remain mistaken without rewriting world truth or leaking undiscovered facts. |
| T35 Fantasy permission | A13 P19 | Run the human founding compact with separate local rights and recognizers. No official grants powers outside their scope; no ancestry determines consent, hostility, or allegiance. |
| T36 Genre effects and resources | P07 P21 | Exercise one selected life-support or fabrication process and one magical service. Charge qualified inputs and capacity once; interruption, loss, maintenance, and replay preserve state. |
| T37 Eight family integration | A11 A12 A13 P01 | Compile H01 through H06, N01, and F01 through one setup contract. Preserve historical sources, fictional provenance, supported customization, control, and all existing identities on resume. |

### Deliberate boundary cases

N01 must test uncertain occupancy, unavailable resupply, a raw resource without extraction capability, and a proposed company unable to maintain its selected habitat. F01 must test overlapping rights, an offered compact awaiting assent, independent elven and human households, and a magical service whose practitioner or inputs become unavailable.

Test these as declared fixtures rather than compulsory campaign events. A defect does not authorize changing the world to match an expected result. Preserve inputs, recipe versions, state, resolutions, results, unsupported branches, and replay evidence. A successful generator test does not establish scientific calibration, complete autonomous play, or a functioning Core adapter.

## Generated world records and remaining decisions

### Proposed generation and instance records

The configuration record identifies start family and revision; authored setting references; genre assumptions; permitted variation; locked player choices; generator and algorithm versions; source-table versions; seed and retained results; constraints; validation findings; and initialization status. F01 may use an authored world, constrained generation, or both; the selected method is recorded.

The resulting world state identifies actual sites, residents, institutions, rights, habitats, resources, goods, projects, and events under their existing owners. Link each consequential fact to its authored source or generation result. Preserve confirmed facts and ungenerated areas separately. Later detail must satisfy established constraints and does not regenerate the entire world.

Record what each actor knows through survey, testimony, observation, or other selected channels. World truth, estimated conditions, claims, and received information remain distinct. Keep restricted facts outside shared player-visible documents where actual secrecy is required. Rerolls are setup operations before commitment, not an in-play ability to replace established facts.

### Open decisions added by this edition

| Issue | Decision required | Proposed direction and dependency |
| --- | --- | --- |
| O16 Generation envelope | Which variables, distributions, constraints, and regeneration choices are supported? | Author bounded recipes and a feasible opening envelope; retain resolved output and provenance. Blocks claims of a working generator. |
| O17 Fantasy setting rules | Which institutions, peoples, lifespan assumptions, ecology, and magic govern F01? | Begin with a defined local elven community and human compact. Select explicit effect rules; no borrowed franchise canon or universal ancestry traits. |
| O18 Planetary providers | Which transport, habitat, energy, production, biological, and communication procedures are supported? | Qualify each essential provider and its finite dependencies. An optional technology cannot be assumed from a science-fiction label. |

### Release evidence

Complete one usable N01 recipe and its supported variation bounds, one fully authored F01 example, initial-state manifests, institutional and resource procedures, and T32 through T37 evidence. Describe excluded variants and unqualified effects. All eight families use the same release and adoption controls; adding these specifications does not initialize a world, activate modules, or rerun the earlier Core audit.
