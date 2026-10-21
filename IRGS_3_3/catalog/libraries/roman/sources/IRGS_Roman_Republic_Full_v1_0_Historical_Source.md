# IRGS — Roman Republic Life Simulation Engine

**Version:** 1.0 — Consolidated Reference Edition  
**Date:** 12 October 2026  
**Document ID:** IRGS-RRLS  
**Parent:** IRGS Integrated Framework v2.1  
**Classification:** Historical-life engine with a dated Roman Republic setting module  
**Default setting:** Roman Italy and connected regions, approximately 60–50 BCE  
**Status:** Proposed reference edition for campaign adoption; historical and numerical calibration remain open.  
**Validation:** Bounded numerical fixtures and worked acceptance cases; no complete campaign implementation or independent live-play certification.  
**Campaign state:** No campaign instantiated or advanced by publication.

This engine runs a persistent human life across captivity, work, training, violence, institutions, wealth, relationships, status change, recovery and legacy. Gladiatorial activity is a complete supported career, within the same continuing world as ordinary livelihoods. The engine provides operational defaults and record procedures; it does not promise a particular rise or predetermined destination.

**Reading labels:** [CORE] inherited parent procedure; [ROMAN] local engine procedure/selection; [PROFILE] local configuration or calibration; [REFERENCE] evidence/example; [IMPLEMENTATION] optional tool-level detail. Labels identify ownership and evidence, not proof of testing. The global status above governs Roman-owned additions throughout.

## Contents

1. [Purpose, architecture and authority](#s01)
2. [Shared resolution and agency](#s02)
3. [People, creation and assessment](#s03)
4. [Capabilities, learning and progression](#s04)
5. [Needs, compulsory work and fatigue](#s05)
6. [Legal position, captivity and release](#s06)
7. [Property, money, contracts and markets](#s07)
8. [Livelihood, production and households](#s08)
9. [Relationships, NPCs and institutions](#s09)
10. [Information, search and pursuit](#s10)
11. [Travel, burden, exposure and animals](#s11)
12. [Encounters, commitments and priority](#s12)
13. [Tactics, equipment and physical effects](#s13)
14. [Anatomical injury, care and recovery](#s14)
15. [Gladiatorial institutions and continuing careers](#s15)
16. [Runtime, historical change and scale](#s16)
17. [Records, persistence and presentation](#s17)
18. [Content, profiles and deployment](#s18)
19. [Worked acceptance cases, validation and version policy](#s19)
20. [Source ownership and provenance](#s20)
21. [Appendix A — Campaign profile and selected defaults](#appendix-a)
22. [Appendix B — Illustrative dossier and contextual views](#appendix-b)

<a id="s01"></a>

## 1. Purpose, architecture and authority

[CORE / ROMAN / PROFILE]

This engine models a continuing human life within dated Roman institutions, physical limits and a world that acts independently. Its default application is the late Republic, approximately 60–50 BCE, with a captured frontier teenager entering slavery. Captivity, agricultural or household labor, training, gladiatorial work, civilian livelihoods, freedom, patronage, business, family, authority, recovery and retirement are supported trajectories. None is a required plot stage. Legendary reputation is a possible consequence of observed achievements, not a victory condition or guarantee.

Use **Shared IRGS Core → Historical Life interface → Roman Republic setting module → Campaign Profile → Campaign State**. This publication packages a thin historical-life interface with its Roman application; it does not promote Roman laws or local numerical selections into the universal Core.

| Owner | Responsibility |
|---|---|
| Core | Agency, feasibility, resolution, clock, resources, information, projects, actors and continuity |
| Historical Life interface | Particular human capacities, disciplines, obligations, livelihood, injury and permanent death |
| Roman setting module | Dated legal relations, institutions, money, material culture, spectacle arrangements and historical context |
| Campaign profile | Locality/date, enabled activities, content eligibility, calibration, generation rules and explicit overrides |
| Campaign state | Actual persons, property, claims, knowledge, quantities, injuries, events and history |

Authority is: current explicit user direction; established campaign rules/overrides; adopted relevant genre procedures; Integrated Framework; temporary scoped ruling where no adopted rule resolves the case. Publication alone neither adopts these proposed rules in an existing campaign nor changes resolved play. A correction invalidates the old rule only for its stated scope.

Simulate first, narrate second. Preserve finite means, actual time, practical access, actor knowledge, institutional procedure and consequences. Never invent the PC's dialogue, motives, emotions, consent, purchases, politics or voluntary acts. Mixed results cannot silently make a fresh choice or spend newly volunteered resources. The difficulty comes from the world's circumstances, not adjustment to player performance. Success may produce stability and ordinary responsibility.

The required parent is **IRGS Integrated Framework v2.1**. Source mechanisms are selected explicitly in the relevant sections. The military source's citation of Historical v0.3 is not adoption of that separate document. No fantasy, post-apocalyptic, modern military or science-fiction lore, powers or technology are enabled by this engine. [C §§1–5,64–70,88–100; M §§1–4]

<a id="s02"></a>

## 2. Shared resolution and agency

[CORE / ROMAN]

Use **Declaration → feasibility → meaningful uncertainty → resolution → autonomous reaction → update → control**. Identify objective, method, target, means, location, duration, committed costs, feasible effect ceiling and credible stakes before resolving. Physical feasibility, practical access, legal permission and personal willingness are different questions. Unlawful actions can be possible; legal entitlements can be unenforceable.

Routine qualified work normally proceeds automatically, consuming actual time and resources. Meaningful uncertainty uses uniform integer d100 plus the net modifier: **Success 60+, Mixed 30–59, Failure ≤29**. Do not clamp results or add universal natural-roll criticals. Select one lead discipline:

| Rating | Scope description | Modifier |
|---:|---|---:|
|0|Untrained|−20|
|1|Familiar|−10|
|2|Trained|0|
|3|Experienced|+10|
|4|Expert|+20|
|5|Master within human limits|+30|

Against active opposition add `10 × (2 − opposing rating)` once. The combined relative-competence adjustment is therefore `10 × (actor rating − opposing rating)`. Do not then add both ratings again or roll a second full defense. Independent complexity and slight/meaningful/major/decisive circumstances use±5/10/20/30. Record causal reasons; one injured grip does not also become generic weakness, poor readiness and a second injury penalty. Totals beyond±40 trigger a feasibility/uncertainty review, not automatic success, failure or a hidden cap.

Choose the material Mixed branch before rolling: reduced effect, authorized extra time, existing exposure or a bounded committed cost. A new payment, dangerous continuation, surrender, promise, attack or retreat is a fresh PC decision. A failure never invents an unrelated catastrophe, a free counterattack or an absent object. Retrying unchanged conditions does not provide unlimited independent chances.

Success achieves its feasible agreed effect. If a successful search establishes absence, preserve that information. A successful repair restores its specified function. Do not secretly remove solved problems to maintain hardship. For composite commands, identify impossible components and execute only independently authorized feasible parts. If removing a component materially changes the user's intent or exposure, return control before commitment.

Use an actual supported random source with recoverable raw rolls or an agreed disclosed fallback. Do not narrate an unperformed roll. Record hidden modifiers privately only where recoverable private storage exists; a public numerical breakdown must not reveal unknown opposition. [C §§4–9,47,86,99]

<a id="s03"></a>

## 3. People, creation and assessment

Creation has three passes: **establish supported facts → assess relevant capabilities → instantiate the immediate situation**. Begin with the user's premise and any player choices. Mark additional generation as proposed; do not present a generated family tragedy, personality, nationality, capture story, or ambition as the player's existing decision. Ask only the questions that affect creation or the first meaningful choice. Other unknowns can stay unknown until they matter.

First record identity: stable ID, names currently used, approximate age, origin where established, languages, cultural and work experience, physical appearance, handedness, size/fit, and particular limitations. An imposed name can differ from the character's own name. Neither a cultural label nor appearance automatically supplies a complete personality or skill package.

Then record capacities through useful evidence: lifting or carrying demonstrated, sustained work tolerated, ordinary mobility, reach where combat depends on it, fine manipulation, sensory limitations, memory or reasoning demonstrated, and recovery constraints. Prefer a supported comparison or task to invented precision. "Can carry this assigned load for the observed interval" establishes more than an unsupported Strength 47. Unknown capacity can be assessed through a safe task; a costly or dangerous test requires the character's actual opportunity and voluntary decision where relevant.

Create scoped disciplines only where history or assessment supports them. Examples include agricultural labor, animal handling, cooking, textile repair, woodworking, accounts, negotiation in a particular social context, instruction, close blade fighting, shield use, wrestling, riding, and field care. Ratings 0–5 inherit the Core competence ladder. A background provides candidate experience, then evidence establishes its scope. An agricultural worker is not automatically a smith; an arena fighter is not automatically a military commander.

Record each language in separate comprehension, speech, reading, and writing fields, with register and specialist vocabulary when relevant. A person can follow common Latin work instructions while misunderstanding a legal declaration, speak fluently while unable to read, or copy letters without understanding their contents. Conversation uses the weakest function materially required, rather than a generic language bonus. Repeated familiar instructions can become understood without granting general literacy.

Finally establish bodily condition, custody, available relationships, actual provisions, commitments, and goods. Clothing, containers, bedding, tools, ornaments, weapons, documents, restraints, and keepsakes are possible item functions, not compulsory possessions. Every actual item needs a source and present location. A richer character record does not justify furnishing a captive with convenient secret assets.

Creation ends with a **known dossier**, an **authoritative state record**, and **unresolved facts**. The known dossier contains only what the person can know. A hidden NPC fact is not a blank the model must fill in public. No player goal, emotional response, dialogue, or voluntary act is generated during creation. [C §§4, 12–16, 20; F §§14–23; M §§5–6]

Before the opening scene, initialize the complete **immediate** situation: place/date; custody and asserted basis; shelter/current provision; observable bodily restrictions; communication and demonstrated experience; actual held/issued goods; nearby responsible actors; and the next meaningful event. Generate necessary local world facts within the selected scenario profile, recording provenance. Leave remote history and irrelevant detail unresolved. Ordinary human functions appropriate to the established person remain available unless a specific limitation applies; unmeasured capacity is not incapacity.

Do not convert the PC's modern historical knowledge into character knowledge. A player-supplied background establishes the supported experience it actually describes. Starting assessment can recognize that competence without manufacturing past training hours. Future advancement uses §4.

The minimum dossier and illustrative contextual views are in Appendix B. An item is instantiated only with a source, present location and actual custody/access. More detailed records never justify convenient secret assets or an imposed personality.

<a id="s04"></a>

## 4. Capabilities, learning and progression

### Capabilities and techniques

A discipline describes what the actor has learned, its operating contexts, and demonstrated limits. Useful scopes include close blade fighting, spear use, shield use, wrestling, throwing, riding, animal handling, field care, language, craft, instruction and accounts. Do not give every fighter every discipline at the same rating. Use one lead discipline for a declared method; relevant support normally establishes feasibility or grants one independent circumstance, not a second full skill bonus.

Technique access uses absolute competence and actual instruction. Rating 0 permits intuitive simple acts; 1 rehearsed fundamentals; 2 ordinary professional methods; 3 advanced adaptation; 4 specialized expert methods; 5 exceptional mastery within human limits. An unfamiliar technique one tier beyond capability can be attempted at −10 only if its method is plausibly understood and physically feasible. Missing instruction is not overcome by an ever higher roll. [F §§8, 15]

A person may know how to thrust while being unable to supply the present leverage, range, free hand or foot placement. Capacity, injury, technique, means and permission are independent. No stage of fame grants additional primary actions, stronger bones or immunity.

Technique records are small: `method | discipline/prerequisite | valid positions | hands/means | objective/effect | time commitment | exposure | Mixed branch | evidence`. Feints, trips, disarms, binds, shoves, grapples and escapes use the same contested-objective contract. A successful feint creates a defined opening; it does not include an undeclared follow-up attack. A declared combination must fit one meaningful commitment, use a trained technique and a bounded objective. Otherwise its parts take separate commitments.
### Training, instructors and assessment

A training plan specifies objective, discipline, current evidence, desired rating/technique, prerequisites, method, instructor, feedback, safe equipment, scheduled intervals, exertion and evaluation. Instructors possess subject competence and ability to provide feedback. Merely being present near an expert is not focused instruction. Group instruction is allowed when the method, space, equipment and instructor attention support that group; individual supervision has a different capacity. Learner-hours and instructor-hours are separate units.

Actual qualifying hours are usable focused practice, instruction, study or evaluated relevant experience. Travel, watching a gate and fighting for survival are not automatically full simultaneous training. Routine work can produce output and learning where challenge and feedback genuinely occur; record the dual use rather than duplicate hours. Injury, exhaustion, absent equipment or a diverted trainer can reduce or stop useful practice. Preserve completed hours when a lesson is interrupted unless actual loss of learning is established.

Apply ROM-TRAIN-01's incremental threshold only to the discipline being developed. At a threshold, review whether the next description is demonstrated in relevant conditions. Familiar needs repeatable fundamentals; Trained ordinary competent work with appropriate safety and decisions; Experienced adaptation to varied real conditions; Expert consistently demanding specialized work; Master broad exceptional performance inside the discipline's actual scope. The evidence gate can be satisfied through prior observations and need not demand a dangerous arena test. An institutional qualification or permission is a separate decision with its own authority.

If the hours gate is met but evidence is missing, identify the missing demonstration and a suitable task. Do not erase hours, award expertise anyway, or demand repetitive unchanging checks. If evidence is convincing but the selected time schedule misrepresents development, record a calibration issue and revise prospectively with explicit migration; do not silently switch to the faster source schedule for a favored character.

No score increases merely because time passed. Physical conditioning records actual changes in capacity and sustainable work; it has no automatic Strength+1 timer. Age, illness and injury can constrain development without predetermining failure. A trained fighter may progress as instructor, negotiator, organizer, craftsperson or administrator through those separately learned skills.

**ROM-TRAIN-01:** incremental 40/160/400/1,200/3,200 qualifying hours for 0→1/1→2/2→3/3→4/4→5, each with demonstrated capability. Cumulative gates are 40/200/600/1,800/5,000 h. This selects F §§24–25's hour schedule without fantasy levels or attributes. Store hours and schedule ID; bare Training Units are invalid across engines. These rates are provisional across different disciplines. Hours are not calendar days or an automatic qualification. A new title, permission or certificate is a separate institutional act.

Progression includes communication, earning capacity, useful equipment, trust, enforceable rights, family/household stability, delegated responsibility, institutional capability and legacy. It is not a conversion of every achievement into attack power. [C §§14–16,31,96; F §§24–25; M §4]

<a id="s05"></a>

## 5. Needs, compulsory work and fatigue

### Needs and compulsory work

Each dependent person or group has requirement records for food, water, shelter, suitable sleep opportunity, sanitation, environmental protection, and necessary care. Their minimum viable and preferred levels differ. Bare survival provision does not imply normal growth, recovery, or productive capacity. Quantities are selected from the actual consumer, work, climate, and supplies; no new universal calorie or water table is supplied here. [P §5; C §§17–19, 71]

Before advancing an interval, identify actual provision and its controller. A ration entitlement is a claim until delivery. A serving prepared from shared stores consumes those stores once; the recipient's provision record references that event rather than subtracting again. Received but spoiled food is a quantity with unusable function, not adequate nutrition. Recalculate endurance forecasts after changes in demand, delivery, rationing, or usable condition.

Actual work is bounded by **opportunity, functional capacity, access, supervision where required, tools, inputs, and elapsed time**. Use the selected fatigue and injury procedures in §5 and §§12–14 once. Hunger, inadequate sleep, and a wound can be separate causes; the same physical limitation cannot acquire three generic penalties through different labels. Consequences follow unmet functions and evidence, not a universal daily hardship roll.

A custodian may assign labor, withhold access, impose a demand, or attempt punishment. Assignment creates an institutional expectation, not a voluntary PC action. At the decision boundary present the demand and credible enforcement. The player determines voluntary response. NPC enforcement can physically restrain, relocate, injure, or prevent a task when the actors and means support it. Coercion does not manufacture consent, confession, loyalty, or belief.

Sick, injured, young, or exhausted people require task-specific assessment. Unable to sprint does not imply unable to sew or understand an account. Conversely, an owner's insistence does not restore a disabled limb. The simulator can resolve an impossible order as unmet and an abusive response as an NPC action; it does not secretly complete the labor to preserve the institution's production forecast.
### Exertion and recovery

Use Rested 0, Taxed 1, Tired 2, Exhausted 3, Depleted 4; relevant exertion/attention modifiers 0/−5/−10/−20/−30. Mark one load point per 2 h strenuous work, per 8 h ordinary active duty, or per exchange explicitly exceptional maximum exertion. Do not count the same interval as ordinary and strenuous. Each two points converts to one fatigue step and consumes those points. Preserve fractional ordinary work/load across interruptions. [C §18]

At Depleted, sustained strenuous activity stops being feasible. A brief exceptional effort is a separate player declaration with credible exposure; it does not silently continue a long march or training session. Split an activity at the point a meaningful fatigue threshold is reached. Being hungry or injured can limit useful training without erasing existing competence.

Two protected low-demand rest hours with necessities remove one unconverted load point, without reducing established fatigue. Full suitable sleep with needs met lowers fatigue 2 and clears residual load; disrupted sleep lowers 1, with recovery constrained by the actual disturbance and needs profile. **Package clarification:** retain ordinary unconverted load after disrupted sleep unless actual protected rest clears it; the inherited source does not specify an automatic full clear for disrupted sleep. Full sleep is not available because a calendar day ends. Treat roster, safety, shelter, temperature, sleep opportunity and interruptions as facts.

Food, water, sleep and environmental protection are separate requirements. Track their actual supply and deficit; use supplied/short/deprived/severe/critical descriptors only when their trigger is supported by a profile or visible physiological evidence. Source F's descriptor penalties can guide a provisional specific ruling, but a descriptor does not automatically multiply fatigue for the same effect. A forecast of empty stores does not inflict damage early. A full meal supplies the present need; it does not instantly repair chronic malnutrition or a wound.

Eight hours of strenuous practice gives four load points and two fatigue steps under the selected source budget. With fully adequate sleep, both steps can clear. This may be too forgiving for a real harsh training schedule; the test exposes calibration, not a reason to invent a secret cumulative penalty. Reduce the actual useful training opportunity, identify a distinct deprivation/injury cause, or prospectively revise the exertion profile from evidence. Do not silently use the arithmetic trace after Depleted as permission for continued work.

<a id="s06"></a>

## 6. Legal position, captivity and release

### Captivity and transfer

Keep **claimed status, legal position, custody, and actual control** distinct. Captured, missing, detained, offered for sale, transferred, escaped, released, and dead describe different events or information states. A free person may be unlawfully detained or falsely sold. A sale does not itself prove the legitimacy of an original claim. [C §§4, 12, 64–66; M §6.10]

Custody schema:

`Subject | custodian | claimed basis | recognized/disputed status | physical location | restraint/guard arrangement | practical movement/access | provisioning/care controller | transfer authority asserted | witnesses/records | pending demand/transfer | outside knowledge`

For a sale or transfer: identify seller's asserted authority, buyer, subject or goods, actual terms, price or exchange if known, inspection/access, promises and disclosures, payment arrangement, handover location, and recognition. Resolve bargaining only where uncertainty is meaningful. Record agreement, payment, change of physical custody, claimed ownership, and third-party recognition as distinct events. One can occur without another: an unpaid buyer may take custody, a dispute may follow, or a transfer may fail before handover.

The player retains decisions about speech, attempted resistance, cooperation, concealment, bargaining, or escape where physically possible. An NPC can physically move a restrained person without asking the player to choose that displacement. Explain the involuntary mechanism. If the PC is absent, unconscious, or unable to understand the transaction, the known dossier receives only what is later observable or reported.

Escape changes actual custody and location before it changes anybody's beliefs or legal claims. A custodian learns through discovery, witnesses, or reports and then chooses a response from available means. There is no instant universal wanted-state update. Searches require people, routes, time, information, and opportunity costs. Repeated searches do not automatically locate a fugitive; failed searches do not erase existing tracks, claims, or memories.

Recovery, exchange, ransom, release, and repatriation are supported workflows when their actors and resources exist. They are not guaranteed exits. An offer of rescue creates a proposition and possible commitments; it cannot automatically spend the PC's administered funds or choose the PC's allegiance.
### Legal position and recognition

Use independent fields:

`freedom condition | civic standing | former-slave/patron relation | household dependencies | capacity/restrictions by transaction | occupation/terms | office/authority | allegation/adjudication | jurisdiction | documentary/witness evidence | local recognition/dispute`

A person's occupation is not their legal status. Freedom, citizenship, former-slave relations, money, reputation, and institutional authority may change at different times. A freed person can have civic standing and continuing obligations. A person may be famous but unable to enforce a claim. A business operator can administer assets whose legal owner is somebody else. A military appointment or arena victory does not change every field.

Roman legal effects need dated grounding. The historical evidence register supports separating formal manumission, freedom/civic consequences, and a peculium's ownership from its administration. It does not establish a complete legal code for 60–50 BCE. Later legal compilations can report earlier practices, but a passage's date, subject, exceptions, and continuity must be examined before applying it. Do not silently import later restrictions or guarantees into this decade.

**Roman default ROM-LEGAL-01:** every material claim identifies the actor asserting it, the local decision-maker or enforcement mechanism, the evidence, and the practical consequence. If the specific legal rule is unresolved, preserve the disputed field and use only established practical powers. A guard may refuse access while the legal validity of the refusal remains unresolved. Where continued play needs a local procedural rule, label a narrow provisional ruling with its scope, effect, and review trigger. Do not invent a universal right or doctrine to finish the scene.

Case schema:

`Case ID | parties | claim/allegation | jurisdiction/venue or practical authority | applicable rule/provisional ruling | evidence/witnesses | intermediaries/access | acts required | costs/delays | decision/effective time | enforcement | reporting/recognition | unresolved disputes`

Process a case by recording the claim, obtaining information through actual channels, determining access to the relevant actor, conducting whatever procedure is actually available, recording a decision, and enforcing its supported effect. This workflow promises no equal hearing, impartial decision-maker, modern legal representation, appeal, or identical testimony rules. An owner's command, private violence, patron's intervention, and magistrate's act remain different processes. A failed skill roll is not proof of a crime.

Use *infamia* only with a researched dated meaning and actual consequence. Until those are specified, record audience stigma or a particular institutional exclusion in plain terms. Do not make the word a universal negative charisma score or presume every later legal disability applied identically to this person. Conversely, fame does not erase a real exclusion merely because it inconveniences the intended rise.

When a new title or recognized status is received, explain briefly what it means locally: authority, obligations, eligibility, recognition, and limits. The explanation describes this event; it does not grant unrecorded property, staff, votes, combat competence, or universal respect. [C §§38–40, 64–69, 97; F §§103, 107; M §§5–6]
### Release and manumission

Distinguish **promise → eligibility/terms → required act → effective release/status change → recognition/enforcement → continuing obligations**. A promise is a claim, a document is evidence, and actual legal effect requires the applicable route. Being allowed to leave a particular bout, discharge from fighting, removal of restraints, escape, and manumission are separate facts.

The dated research shortlist is **vindicta** (act before an appropriate magistrate), **censu** (census enrollment), and **testamento** (a testamentary disposition taking effect through the applicable succession). These are candidates for the Roman profile, not interchangeable instant actions. Their broad Republican presence is supported by [Zhao's research, printed pp 24 and 115](https://api.repository.cam.ac.uk/server/api/core/bitstreams/a2a56e2c-a4b6-4fd5-838a-0a55dd922600/content). Eligibility, authority, access, effective acts and resulting rights still require the particular case. Do not backdate later Augustan restrictions or later categories.

For a proposed route record who has the relevant authority, what act is required, who must be present or informed, applicable conditions, present cost, timing, evidence, intended changed fields, and consequences for administered property. A patron's help can obtain access or pressure an actor; it cannot substitute for a legally necessary act unless the selected rule permits that substitution.

**Runtime procedure:** check the promised act against current authority and conditions; schedule the actual meeting or other necessary step; reserve only authorized costs; run travel and intervening obligations; resolve any meaningful uncertainty in access or compliance; record what actually occurred; update only the affected legal fields at the effective timestamp; send reports through actual channels; preserve remaining claims and obligations.

If an owner reneges, the simulation records a breach of promise and what witnesses know. Response options depend on actual contacts, authority, physical opportunities, evidence, and danger. There is no automatic compensation, successful petition, revenge, or forced player submission. If a procedure succeeds, preserve the resulting freedom or other status until a credible later event changes it; do not undo it because the game needs another arena arc.

A hypothetical fixture can contain a witnessed release meeting scheduled for Day 12. Before it occurs, the record remains "release promised; meeting pending." The completion event changes precisely those status fields named by the profile's selected route. If only physical release occurs, legal emancipation remains unresolved. This example specifies bookkeeping and chronology, not the historical legality of a fictional release ceremony.

Before a material legal commitment, record the dated route or narrow provisional ruling, eligible parties, required acts, effective consequences, continuing obligations and review scope. Once those prerequisites and acts occur, apply the recorded result. Unknown research cannot become a retrospective veto on a completed success. Later corrections follow §17's correction procedure and§18's migration policy; no universal right is invented to finish a scene.

<a id="s07"></a>

## 7. Property, money, contracts and markets

### Possessions and administered funds

For meaningful goods use:

`Item/lot ID | profile | quantity/unit | legal owner/claimants | custodian/holder | location/container | access/use authority | reservations | condition/quality/fit | provenance | last event`

Ownership, custody, access, and ability to use differ. A blade issued for a lesson can be in the learner's hand while owned by the school and prohibited outside training. An owned tool locked in a distant store is unavailable now. A borrowed garment can improve fit without becoming a gift. Containers are locations with their own capacity and access; moving a container moves its actual contents once.

Simple items remain simple records. Track individual coins, nails, or servings only when identity or quantities affect a decision. Otherwise use compatible lots while preserving owner, location, quality, and reservations. Separate lots that differ in usability, claims, or access. Equipment condition does not silently reduce ownership or quantity; destruction, theft, confiscation, consumption, and transfer are different events.

Peculium or another administered fund has an account controller, legal owner, permitted transactions, withdrawal/revocation conditions, outstanding claims, and actual holdings. Do not equate "credited to the fighter" with money freely disposable by the fighter. Where the legal terms are unknown, record control and claims rather than pretending modern beneficial ownership. A revocation must be an event by an actor with practical means; the simulator cannot reset the account merely because the character changes scenes.

An institutional award paid to a lanista credits the establishment. An individual allowance is a separate owed or paid transfer on its actual terms. Expected prizes are forecasts; a claim is not tender. **ROM-MONEY-01 selects sestertii as the account unit, with 1 denarius =4 sestertii**, supported for the Republican system by [Carbone and Yarrow, ANS Magazine 2019 issue 3, p15 and note 27](https://livyarrow.org/wp-content/uploads/2019/09/yarrow-carbone-2019-opening_access_to_roman_republican_die_s.pdf). This accounting relation does not specify the physical coins present or a market price. Use exact fractions where necessary. Tender, foreign money and exchange availability remain particular facts. Changing the displayed unit changes a view, not physical holdings. [C §§12, 20–24; F §§104–106; M §§5, 7–11; FL §§1–4; PL §§5–14]
### Transactions, contracts and credit

Inherit **Quoted → Agreed → Owed → Delivered → Paid** from F §104, allowing partial delivery/payment and a different agreed order. A purchase requires an actual seller with stock or a feasible supply undertaking. Price, quality, quantity, delivery, payment, liability, permitted cancellation, witnesses, and practical enforcement determine the agreement. Promised work does not establish free consent when made under coercion.

Before commitment verify authority to dispose of each resource, actual availability, transport, and whether the player authorized these terms. On settlement, subtract source and add destination atomically, citing one transaction ID. An amount reserved is still physically held but unavailable to conflicting uses. Release reservations on cancellation; return actual paid money only through a real refund. A creditor's claim is distinct from the debtor's cash and cannot become both parties' available funds.

A transaction record is:

`ID | parties/authority | purpose | quoted/agreed terms | amounts/units | delivery/payment milestones | reservations | actual transfers | due times | witnesses/evidence | breach/remedy | status`

Credit supplies a recorded liability and a real lender or seller's exposure. Money appears in the debtor's cash only if actually advanced. Interest, penalties, securities, and remedies require the selected local agreement and dated rules. Failure to pay does not automatically enslave a citizen, confiscate every asset, or create a modern bankruptcy process. Determine what the creditor can and does attempt.

**Fictional accounting fixture, not historical prices:** a workshop opens with 100 account-units(AU); pays 30 AU for actual inputs; owes 12 AU for completed labor; delivers goods generating a60 AU receivable; receives 40 AU today. Cash is 110 AU, net outstanding receivable 20 AU, payable 12 AU, and cash available after reserving wages 98 AU. If wages are then paid, cash becomes 98 AU and the payable/reservation clear. Do not count the 60 AU sale and 40 AU collection as100 AU revenue. The fixture'sAU is an accounting unit only, not an asserted Roman coin or exchange rate.

Prices require commodity/specification, quantity, place/date, actual availability, seller, quoted basis, and uncertainty. An unknown price can be discovered through a quote or bounded local estimate labeled provisional; it is not filled from fantasy tables. The engine can run a negotiated fictional quote while retaining historical calibration debt. It cannot call that quote representative Roman market data.

Unknown market availability is not established absence. When it first matters, establish a bounded local availability record from the place/date, role, supply situation and existing world constraints before resolving a search or purchase. Preserve it until actual causes change it. A provisional quote is this seller's offer for this stock and these terms, not a representative Roman price. Bind the agreed feasibility and terms before committing resources. [C §§5,24,79,97,99; F §§104–107]

<a id="s08"></a>

## 8. Livelihood, production and households

### Livelihood, property and production

A work arrangement records employer/controller, task, terms, schedule, compensation or provision, supervision, tools, hazard, access, duration, exit constraints, and reporting. Work can be paid, household, compulsory, dependent, or reciprocal. Its outputs and obligations differ. No universal modern working week, wage, promotion ladder, or labor protection is assumed.

For an interval calculate usable worker time after travel, care, rest, prior commitments, and actual interruption. Routine qualified work creates accepted progress without dice. Uncertain work uses the Core predeclared branches; the default Mixed branch supplies half planned usable progress where appropriate, not arbitrary unrelated damage. Actually consumed or spoiled inputs are charged once.

Project schema:

`Project ID | owner/controller | deliverable/acceptance | remaining work by task | qualified roles | concurrency limits | tools/workspace | inputs | dependencies | scheduled workers | progress/consumption | inspection | next review`

For a defined task, `progress = effective qualified rate × usable time`, bounded by remaining work, input supply, serial dependencies, workspace, and concurrency. Different stages retain their own units. Do not add forging hours to weaving hours into a universal production pool. Completion and acceptance are separate when quality or safety matters. Possessing an example does not provide the ability to reproduce it. [C §73; P §§7, 11–14; M §§7–12]

**Fictional throughput fixture:** six items each require 2 qualified finishing-hours, one prepared blank, and one station. Two qualified finishers and two stations can finish six in 6 working hours. Four finishers with the same two stations still need 6 h. If only four blanks exist, output is bounded at four until replenishment. Adding untrained labor may support transport or preparation; it does not double qualified finishing capacity.

Property records separate land/buildings, access/title claims, usable functions, occupants, stored goods, security, maintenance, and obligations. A roof needing repair does not delete the workshop's tools. Rent paid for a future interval is not present ownership. An absent owner needs actual arrangements for supervision, receipts, repairs, and disputes; the simulation does not require personal attendance at every minor decision once delegation exists.

A business uses `inputs → staffed operations → accepted output → available stock → actual demand/orders → delivery → collection`. Forecast revenue is not guaranteed sales. Measure profit over an explicit interval using recognized income and actual costs/consumed inputs, separately from cash flow. Owner withdrawals reduce business cash; purchases of durable productive assets change asset position as well as liquidity. Maintenance, spoilage, theft, and taxes/fees occur only through supported causes or selected local obligations.

For agriculture and other seasonal work, record the actual crop or task, land, labor windows, water/access, input stocks, storage, and expected harvest interval. A favorable day does not guarantee annual sustainability. Do not supply arbitrary yields or automatic percentage profits. Unknown yields stay a forecast until sufficient profile evidence or actual harvest supports quantities.
### Households and relationships

A household is a changing organization of particular people and dependencies, not a passive income or morale bonus. Record membership/residence, recognized authority, relationships, owned/administered property, ordinary income/provision, care responsibilities, labor availability, housing, obligations, and information channels. Do not assume every member has equal legal power, freely chosen residence, or the same knowledge.

For each relevant relationship keep the dimension that affects behavior: trust in a promise, confidence in skill, affection, fear, resentment, loyalty, obligation, or dependency. Descriptors with supporting events are the default. Numeric ratings are optional only if an adopted social adapter needs them. A person can respect ability, fear violence, resent treatment, and still refuse an offer. [C §§64–69; F §§101–103; M §6.4, §6.9]

Resolve a social request from its content, target's goals and values, existing relationship, cost, authority, alternatives, knowledge, and means. Routine plausible agreement needs no die. Meaningful contested willingness can use the Core check with defined possible changes. Success obtains the agreed plausible response; it cannot erase a central value or determine the PC's emotions. An NPC's adaptation follows what they actually observed or learned.

Maintenance is causal. Correspondence, shared work, care, payment, and broken promises can change particular relationships. No universal daily decay meter forces the player to visit every acquaintance. Absence may remove opportunities, delay support, or change an NPC's interpretation when circumstances justify it. A household capable of managing a routine task continues without protagonist intervention.

Romance and family formation need compatibility, availability, actual interaction, and voluntary decisions; neither is an advancement reward. Existing relatives remain independent actors with their own tasks and property. For a young captive, do not invent adult relationships or substitute sexual exploitation as a routine numerical development mechanism. Coercive conditions are represented through actual constraints and consequences, without authoring the PC's consent.

<a id="s09"></a>

## 9. Relationships, NPCs and institutions

### Social concessions and group behavior

Before a contested social check, name the feasible concession: permission within the target's authority, a change in willingness, an undertaking or particular assistance. Success obtains that concession; Mixed obtains the predeclared narrower concession, delay or existing cost; Failure leaves it unobtained. It cannot erase a central value, dictate the PC's response or grant authority the target lacks.

Carrying out a concession may require travel, resources, communication, work or another person's decision. Create those tasks rather than instantly completing them. Persuading an intermediary to seek an appointment creates an undertaking, not an appointment already granted. Preserve promise, reservation, receipt of an order and actual performance separately. Relationship dimensions change through specific known events, not a mandatory daily decay roll. [C §§64–69; F §§101–104]

For groups distinguish willingness to continue, coordination and procedural discipline. A leader's loss changes actual communications and decisions; it does not force every member to rout. NPC fear, withdrawal or surrender follows particular goals and perceived danger. PC emotions and voluntary surrender remain player decisions. Do not import a universal military morale meter into a small household or pair of fighters.

### Autonomous plans and schedules

Every significant NPC has `goals | priorities | knowledge | role/authority | competence | available resources | relationships | current plan/task | risk tolerance | next review`. Routine unnamed workers can be cohorts with a defined membership and capacity basis. Promote one to an individual when identity matters, subtracting them from cohort totals. Their prior state is preserved; naming is not recruitment. [C §§64–65, 83–85; M §§5–6]

**ROM-PLAN-01:** at a plan boundary, identify urgent threats, obligations, commitments and feasible goals. These are decision inputs, not a compulsory obedience hierarchy. The NPC chooses from their goals, knowledge, relationships, risk tolerance, expected consequences and means. They may keep, evade, delegate, renegotiate or breach an obligation when their circumstances support that decision. Record the choice and implementation. Reconsider at its review trigger or after material new information. Routine continuation needs neither a new decision roll nor a new complete schedule.

This governs the individual's proposed commitments. It does not serialize independent same-time effects or override shared-resource arbitration. An unreliable guard's absence leaves the actual security gap; it does not magically preserve both their post and other activity.

A plan contains objective, tasks/dependencies, assigned actor, location, earliest start, duration or work remaining, required means, authority, completion evidence, failure/cancellation triggers, and next review. A decision is not communicated authority until recipients receive it. An absent subordinate acts on the last received instruction and local judgment. A report can be wrong without changing the underlying physical state.

Schedules reserve **person-time, place/response conditions, and scarce means**. Mark full work, travel, standby, protected rest, and incompatible overlap. Standby may permit a compatible task but is not automatically uninterrupted sleep. A person cannot conduct individual instruction, supervise a distant workshop, and treat an emergency simultaneously. Group instruction can produce several learner-hours per instructor-hour where its method supports that group; it does not create individual attention.

**Fictional day fixture, not a universal Roman routine:** an instructor has 06:00–08:00 group practice; 08:00–09:00 meal/care/travel; 09:00–11:00 individual assessment; 11:00–12:00 accounts; later duties/rest separately assigned. A 09:30 emergency taking two hours interrupts the assessment after 30 minutes. Credit only the actual qualifying practice; reschedule or cancel the remainder. The instructor returns at 11:30, leaving only 30 minutes for the one-hour accounts task before noon. It needs another authorized worker or a later finish. The event does not erase earlier completed practice.

At handover identify the actual relieving actor, custody of keys/tools/stores, outstanding tasks, observed hazards, and messages. A missing relief leaves a real gap. It does not silently extend the PC's voluntary shift. NPCs can choose to remain or abandon duties under their own constraints; the player receives the actual situation for the PC's decision.
### Institutional services

Institutions deliver particular services through people, assets, consumables, access, and communication. A ludus needs actual instructors, space, kit, provision, care, custody arrangements, management, finance, and customers or organizers. It is not a modern military unit with labels changed. Households, estates, workshops, associations, and governing bodies use the same neutral capacity procedure with their own functions. [P §§7–13; PL §§17–31; M §§7–11]

Service schema:

`Service | beneficiaries | required specification | demand/interval | available qualified personnel-hours | asset/station capacity | inputs | access/operating window | actual deliverable capacity | allocations | delivered service | unmet demand | next review`

For a serial service, delivery is bounded by its least-supported necessary stage. For several competing services, allocate shared people, stations, and inputs through the actual controller's standing priorities or current decision. No single scalar capacity replaces a named missing role. Unmet demand stays unmet; over-demand does not damage assets unless a real overload mechanism exists.

**Fictional care fixture:** one qualified practitioner has 4 usable hours; two urgent procedures each require 2 h of their attention, while routine dressing work requires another 1 h. The institution can supply 4 h, not 5 h. A suitable assistant may perform specified routine tasks if competent and supplied; their mere presence does not provide a second qualified practitioner. Priorities determine who receives attention and when. Ongoing bleeding progresses during waits through the injury record, rather than a generic institution failure roll.

A buffer can delay consequences: existing food stores, prepared materials, reserve water, or completed paperwork. Draw it once. Alternative provision requires actual access and capacity. Repairs restore supported functions after labor, inputs, and acceptance. A wealthy institution can buy substitutes only when goods/services exist, terms are authorized, and delivery can occur in time. Money does not itself treat a wound or convey an order.

<a id="s10"></a>

## 10. Information, search and pursuit

Information schema:

`Information ID | proposition | physical event/reference | observer/source | observation time | transmission/channel | sent/received times | recipient | confidence | interpretation | audience/visibility`

Separate event, observation, report, and interpretation. A sale occurs at its timestamp; a household may learn later; its members may misunderstand the report. A witness cannot report an unseen anatomical detail, exact hidden account balance, or private motive merely because the simulator knows it. Sources can be mistaken, deceptive, incomplete, or stale for specific reasons.

Rumor and reputation propagate through actual audiences. Record who saw an appearance, who heard the story, how they interpreted it, and the consequence for a particular offer or response. No automatic empire-wide fame increase follows one victory. A locally celebrated performer can be unknown to a distant merchant. Institutional records may contradict rumor, and access to those records matters.

Search, inquiry, and assessment establish availability and knowledge separately. A successful inquiry can truthfully find no seller or no usable record. Repeating the same inquiry without a new source, method, or changed situation does not create independent chances to generate the desired answer. Paying for information spends actual authorized funds and buys the agreed service, not guaranteed truth.

Messages need author, recipient, content, channel, bearer or route, expected delay, actual receipt, and failure cause where applicable. A returned message is an event; an absent reply is an information state. Oral delivery can preserve imperfect content only where memory or deception plausibly changes it. Do not create arbitrary mistranslations to force conflict. [C §§30, 60–61, 66, 85–86; F §103; M §6.9]
### Detection, tracking and pursuit

Use **observable trace → detection → interpretation/identification → reported or local decision → tracking/pursuit → contact or lost trail**. A sound, footprint, witness report or missing person establishes only what it supports. Seeing a stranger is not identifying a fugitive, and identifying someone is not locating them now.

A search plan names searchers, starting knowledge, area/route, elapsed effort, methods, light/weather/terrain, access, authority, supplies and review trigger. Resolve meaningful uncertainty once per changed evidence/opportunity; routine examination of an obvious accessible trace needs no roll. Success finds the agreed evidence or position if it exists and is reachable; Mixed follows the predeclared incomplete clue, delay or existing exposure. Failure does not create a bandit attack or erase every earlier observation.

Pursuers move and rest through actual routes, receive information at its arrival time and can lose contact. Escape does not update an empire-wide wanted database. Lost trail is an information state, not deletion of the fugitive's location, history or legal claims. No repeated rolls against unchanged empty evidence. [C §§60–61,64,85; F §§88–93; P §8.11]

<a id="s11"></a>

## 11. Travel, burden, exposure and animals

The clock is monotonic elapsed campaign time with a human-facing date/location label. The profile records the calendar convention and uncertainty. For 60–50 BCE, do not silently pretend a modern calendar conversion is exact where the date basis has not been established. Never perform date arithmetic by moving directly from 1 BCE to 1 CE through an invented year zero. Undated fixtures use Day 0 plus elapsed hours and make no historical calendar claim.

Travel records mode, party, route segments, distance or known duration, terrain/access, actual movement capacity, load, provisions, rests, transport dependencies, custody, expected arrival, and events. Use researched or explicitly provisional segment estimates, then preserve actual elapsed time. No universal march or sea-speed value is selected. Routine known travel proceeds with costs; roll only where consequential uncertainty exists. A failed route search does not instantly produce a bandit attack.

Transit is a location. A remittance sent with a bearer leaves available sender funds when handed over and becomes recipient funds when delivered. A cart's goods cannot supply two places while moving. Departure removes real household labor, alters local consumption, and changes communication opportunities; appropriate delegated arrangements continue independently.

Historical events are baseline processes with actors, resources, prerequisites, date ranges, causal dependencies, and information channels. Use researched occurrences when sufficiently unaffected. A local intervention changes the dependencies it actually touches. When a material dependency changes, reassess its downstream consequences and record the divergence; do not force the original outcome or extrapolate the entire future from one invented roll.

An NPC does not know a future event because a historical reference names it. The PC has no unexplained access to modern historical knowledge. The user's historical knowledge is not automatically the character's belief or testimony. Long absences can permit ordinary institution, household, or business changes through their actual plans, not an obligatory disaster. [C §§10–12, 30, 62, 76, 85, 87; F §§88–93; ML §§1, 4, 6]
### Carried burden and handling

Record decision-relevant carried/worn mass, bulk, occupied hands, fit, access and demonstrated sustainable capacity. Use actual measured loads when available; otherwise a supported task comparison. Ordinary unmeasured carrying remains possible within the person's established human function. No Strength-derived kilogram formula or invented slot total is selected.

Before movement/work, identify whether the present burden permits the method, blocks a hand, impedes a route, requires assistance, increases the activity's exertion category or demands additional time/rest. Apply one cause once. A heavy chest may be impossible to lift alone even for an expert; a bulky bundle may obstruct a narrow opening despite modest weight. Dropping, transferring or purchasing a substitute requires the actor's actual decision and time. Travel does not relocate stored goods unless actually taken. [C §§14,18,20; F §§35–36; M §§7–11]

### Nonweapon harm, environments and animals

Exposure records name source, mechanism, intensity or supported severity, duration, affected person/structure, protection/avoidance, symptoms/evidence, intervention and next review. Falls, fire, smoke, drowning, contaminated food/water, disease, weather, animal force and crushing route through their actual mechanisms into condition/injury/care. They are not forced through Cut/Pierce Defeat or a universal daily catastrophe roll.

Automatic physical consequences occur when established; dice resolve only meaningful uncertainty in avoidance, exposure, diagnosis or intervention. A profile must supply a supportable rate/timeline where a material decision requires one, or bind a narrow provisional assessment before resolution. Ordinary animals are actors with condition, needs, behavior and training history. Handling success obtains a feasible response; it does not tame an unavailable or physically unsuitable animal instantly. [C §§17–19,71; P hazard interface; FL ordinary animal/content records]

<a id="s12"></a>

## 12. Encounters, commitments and priority

### Encounter initialization

Establish a boundary timestamp, participants, their actual knowledge, positions, reachable paths, weapons, usable hands, condition, protection coverage, bystanders, officials and exits. Decide what each NPC is attempting from its goals, information and obligations. Ask only the missing facts that change the immediate PC decision. A surprise attack needs an actual concealment/readiness explanation.

The encounter record contains `objective | area | participants | timing | positions | contact opportunities | committed/reserved actions | reaction debt | exposure | stop conditions | unresolved reports`. Ordinary arena practice, hostile escape, punishment, a brawl, an organized bout and a lethal ambush have different objectives and termination conditions even if the same blade is present.

Choose an exchange duration from the declared actions before resolving them. The engine has no universal six-second combat round. Record elapsed seconds/minutes where bleeding, travel, fatigue, crowd intervention or aid depends on them. Exchanging a few strikes is not automatically two hours of training or an exceptional maximum-exertion event.
### Commitments, responses and priority

Each actor has one primary commitment in an exchange. Compatible incidental movement or speech may accompany it when it adds no second substantial objective and fits physical timing. A long task carries its remaining work into the next interval. Issuing a lengthy order, changing a difficult piece of equipment, or dragging a casualty can occupy the commitment.

Ordinary guard is included in opposition and geometry. One eligible immediate defensive response is available if the actor can perceive and react. A substantial evasion, emergency movement or interruption spends an actually reserved commitment or borrows the next primary commitment. Track which was spent. A future commitment already owed cannot be borrowed again. At the next exchange, paying the debt consumes the commitment; ordinary protection remains. The GM chooses NPC responses, the player chooses the PC's voluntary response. [C §47]

**ROM-DEFEND-01:** a feasible declared emergency evasion gives the attacker−10 on that same attack check, in addition to its reserved/borrowed commitment cost. A distinct major positional withdrawal can justify−20 if actual time, space and awareness permit; bind this before resolution. No second full defense roll or automatic safety. If an escape route physically removes contact before execution, apply that geometry instead of adding a duplicate avoidance modifier. Ordinary guard is already opposition; a substantial shield interception must still spend its applicable commitment. [F §40; C §47]


An actor may reserve a commitment for a specified observable trigger and method. A reserved interception fires once when its prerequisites hold. A missed trigger does not grant a retroactive strike. A reserved attack and an ordinary attack cannot use the same commitment. Withdrawal creates an exposure opportunity only when an actual prepared action and geometry support it; failure alone never creates a free attack.

Established readiness, distance, travel and commitments settle priority first. **Roman priority override ROM-INIT-01:** if consequential order remains uncertain, designate a challenger and roll d100 plus the relative initiative competence and independent circumstances. Adjusted ≤35 gives the other actor priority; 36–65 gives simultaneous execution if physically possible, otherwise no priority; 66+ gives the challenger priority. Equal conditions are 35%/30%/35%, fixing the 41%/30%/29% challenger asymmetry when ordinary outcome bands are reused. This override changes priority only. Attack success still uses 60/30 bands. The challenger may not be chosen after seeing the roll.

If one action physically disables the other actor before its execution, the later action is cancelled or altered to its remaining feasible effect. Independent simultaneous attacks are evaluated from the pre-impact state and both committed. Competing access to one item or one position is a contested objective, not two independent successes. No fresh exchange, scale change or panel refresh restores spent commitments.

<a id="s13"></a>

## 13. Tactics, equipment and physical effects

### Movement, reach, frontage and control

Use relative engagement states: **Grappled → Contact → Melee → Reach → Disengaged**. These are context labels; a weapon profile states which it can use and actual distance when needed. Local shifts, advances, rushes, sprints and withdrawals consume the actual time and commitment their objectives require. Sprinting and accurate delicate work are not automatically compatible.

A prepared longer weapon controlling an approach gives the closer −10 when attempting to cross that controlled space. Success reaches the declared feasible engagement; Mixed gives partial closure or the predeclared exposure; Failure leaves the closer outside the desired range. An established reserved intercept is separate and consumes the holder's commitment. Longer reach provides no attack through an intervening body or wall. Once the closer controls inside the weapon's useful range, the longer weapon must use a feasible close mode, create space or change means. [F §§31–34]

Count only simultaneous credible attackers. One gives no numerical attention modifier; two +5 to each relevant attack; three +10; four or more +15. Blocked, out-of-range, incapacitated or nonparticipating actors do not count. A narrow entrance may admit one threat while the rest maneuver or obstruct escape. Numbers also affect available actions and routes; do not add a second generic outnumbered penalty for the same divided attention. [F §41]

Cover stops a physical channel; concealment impedes observation. Terrain affects the actual movement or method: −5 mild constraint, −10 poor footing, −20 severe constraint; prohibitive geometry is infeasible. A prone fighter's difficulty and an attacker's positional advantage must name different effects before stacking. Do not charge one fall as prone, bad footing, reduced agility and generic disadvantage four times.

Grappling establishes particular control: limb, weapon, balance, neck or torso. Record free limbs, leverage, relative mass, supports and available escape paths. It does not automatically make a person helpless in every function. A subsequent constriction or damaging joint action requires its own commitment unless the declared trained technique explicitly includes it. Control of a body does not dictate the PC's speech or consent.

### Ranged methods and projectile accounting

**ROM-RANGE-01:** use Close/Effective/Long/Extreme with actual profile-supported distances. Long−10 and Extreme−20 are the selected F-derived circumstances; beyond feasible range no attack is resolved. Light, visibility, trajectory, intervening bodies and cover apply to the actual method. No firearm, later weapon design or fantasy capability is enabled by a generic range label.

One primary commitment spent aiming gives+10 to the next precision attack against its maintained target/line. It does not stack through repeated aiming. Meaningful disruption or a material target/line change clears it; the next applicable attack consumes it. Aiming does not fire, reload, retrieve a projectile or create contact. Close quarters can make drawing, slinging, throwing or loading infeasible regardless of skill. [F §§50–54]

Track the actual object/lot through ready/carried→in flight or fired→landed/recoverable→recovered/damaged/lost. Expenditure transfers a real projectile from the actor at release, not at recovery. Fired/recoverable are states or views, never duplicate stock. A thrown implement cannot be thrown again while still on the ground. Readying, loading and recovery require appropriate hands, access, time and commitments; usable recovery is not guaranteed. Shared projectiles retain original ownership/claims and location. [C §§12,20,22; F §54]

### Material culture and profiles

Every weapon instance references an eligible profile and records owner, custodian, location, accessible modes, material, quality, condition, fit and faults. A profile records reach, hands, damage mechanism, Threat, Armor Defeat where relevant, handling, prerequisites, supported secondary transfer and maintenance. Condition and workmanship differ. A prestigious name grants no automatic damage bonus.

The following are **mechanical reference profiles**, selected from F/FL for test play. Their presence here grants no particular object to the starting character and does not prove a specific historical gladiator equipment class. Local construction, dated eligibility and physical dimensions can replace the profile explicitly.

| Reference mode | Threat | Defeat | Use |
|---|---:|---:|---|
| Short pointed implement/dagger thrust | 1 | 1 | Short-range piercing; access to the target remains essential |
| Sword-like blade cut | 2 | 1 | Cutting mode; usable reach and edge matter |
| Sword-like blade thrust | 2 | 2 | Piercing mode; directed point and leverage matter |
| Spear-like thrust | 2 | 2 | Longer controlled reach; close mode must be separately supported |
| Light club impact | 1 | — | Blunt channel; impact transmission matters |
| Heavy hand weapon impact | 2 | — | Blunt channel within a feasible human profile |
| Thrown javelin-like point | 2 | 1 | One real projectile; recoverability assessed afterward |

Native unarmed Threat 0 in F is not a complete physiological model. Use a separately declared unarmed mechanism: balance/control, superficial strike, damaging impact against a vulnerable supported body, constriction or joint damage. For injury, establish actual force and affected structure; do not give every ordinary fist contact a damaging head bonus. Grappling can succeed without injury. Do not import superhuman force or fantasy resilience.

Protection is construction plus actual coverage, condition, fit and supported channels. F/FL candidate values are ordinary clothing 0/0/0; padded textile Cut 1/Pierce 0/Impact 1; mail Cut 3/Pierce 2/Impact 1. These are test abstractions. A shirt does not cover the head and a worn strap can change retention without changing the metal's resistance. Do not insert plate, later harnesses or advanced materials because the library lists them. Integrated layers receive one documented construction profile; their entire resistance values are never simply summed.

Shields give a relevant defensive circumstance only while controlled and oriented: small −10, broad −10, large frontal −15 in the selected F-derived fixture. The profile must declare its actual size/material and access. These labels do not automatically identify historical shield classes.
### Contact, protection and wound assessment

For a damaging action resolve **position/feasibility → execution → actual contact → protection → transmitted effect → anatomical injury → ongoing exposure**. One ordinary check resolves the contested attack objective. A successful attack can be stopped by protection. A failure does not generate a bodily wound just to make the exchange consequential.

Success gives effective contact within the declared objective. Mixed uses the chosen branch; the ordinary damaging-contact branch gives Placement −1. Failure gives no effective damaging contact. A non-damaging Mixed branch may instead affect position or time, in which case do not also apply reduced damage unless both were declared and feasible.

When the contact region remains genuinely unresolved, F's d20 humanoid table is a candidate: 1–2 head; 3 neck; 4–8 chest; 9–11 abdomen; 12–13 right arm; 14–15 left arm; 16–18 right leg; 19–20 left leg. Condition the possibilities on actual access, declared method and protection. A table is unnecessary when contact is already known. Do not randomly strike a hidden limb or teleport a blade around a shield. Small deliberate targets impose the source's −10 limb, −15 hand/foot, −20 or worse gap/vital difficulty where distinct from other causes. A high roll is no substitute for access.

For Cut/Pierce with Resistance ≥1 calculate `Defeat − Resistance`. At ≤−2 the primary channel is Stopped; at −1 reduce Threat 3; at 0 reduce 2; at +1/+2 reduce 1; at +3 or more no reduction. Floor residual Threat at 0. At Resistance 0 bypass the table and retain Threat. For Blunt, Impact 0 reduces 0, Impact 1 reduces 1, Impact 2 reduces 2; higher protection needs its declared exceptional behavior. [F §§55–60]

**Roman default ROM-EFFECT-01:** a primary channel whose damaging transmission is exhausted by protection does not regain injury from placement, vulnerability or later arithmetic. A separately supported transferred blunt or other physical effect uses its own mechanism. This is distinct from a native zero-Threat unarmed profile. Skill never invents penetration.

For supported active residual channels use `Grade = residual Threat + independent Force + Placement + applicable Vulnerability − Resilience`. The selected test Resilience is **0 for ordinary human fixtures**; no Constitution-derived subtraction exists. This is a selected numerical convention; anatomical function and prognosis still differ. Physiology changes which actual structures are affected, their function and prognosis. A different resilience value requires a named prospective profile and its sensitivity tests.

Ordinary Force 0; distinct major momentum/charge +1; extraordinary human-scale impact may justify +2 from a specified physical mechanism. Do not add mass or force already included in Threat. Placement 0 on ordinary success, −1 on Mixed contact, +1 only for exceptionally precise successful placement justified by method and margin; no universal raw-roll threshold guarantees it. Head/neck vulnerability +1 applies only to actual injuring mechanisms; chest +1 requires the relevant severe penetration/crush, not every shirt contact. The profile and scene must justify each term. No generic high-margin execution creates an extra attack.

Grades guide assessment: ≤0 superficial/no structural injury; 1 Minor; 2 Moderate; 3 Serious; 4 Critical; 5+ Mortal potential. **They are not hit points, universal incapacity thresholds or death orders.** An injury event identifies what happened anatomically. Serious injury to a leg may stop running while permitting speech, work or instruction. Mortal potential requires a particular lethal process and possible intervention.
### Wear, maintenance and restoration

Resolve bodily protection using the pre-impact local state. Then apply that impact's material consequences for future use. Candidate armor stress is `Threat + Force + Sunder − relevant Resistance`, floor 0. Stress 0 no automatic damage; Stress 1 one local mark, a second mark gives Local Damage; Stress 2 immediate Local Damage; Stress 3+ Local Breach. Sunder affects this calculation, not injury to flesh. [F §§49, 61–62]

**Roman default ROM-WEAR-01:** store the undamaged base resistance, local state and one pending stress mark. Intact has reduction 0, Local Damage reduction 1, Local Breach reduction 2; effective resistance is never negative. Two Stress 1 contacts move Intact→Damage or Damage→Breach and clear the pending marks. Stress 2 advances one state; Stress 3+ establishes at least Breach. Every state change clears pending marks; they represent strain already included in that change. At Breach, retain no pending marks and use further severe contacts to assess a mechanism-specific component fault or physical destruction only if the impact can cause it; never subtract resistance indefinitely. A breach can be a hole, failed seam or lost retention rather than an entire suit disappearing. Repair resets only the named restored state/marks after actual work and inspection. This transition is Roman-owned; the source does not completely specify repeated-hit behavior.

Shield material stress requires shield contact. To close the missing event link, a declared shield-control/interception objective can produce shield contact on its predeclared success/Mixed branch; otherwise use established physical contact evidence. Do not treat every failed attack as shield contact. Ordinary guard plus a shield circumstance is sufficient for many attacks, with no shield damage inferred when the method of avoidance is unknown. When the shield is actually struck use `Threat + Force + Sunder − Structure`: ≤0 no automatic damage; 1 a mark, second mark degrades one condition state; 2 degrades one state; 3+ two states or supported structural failure. A selected profile supplies Structure; the F-derived reinforced wooden fixture uses 3. Damage changes the actual supporting function and coverage. Record how a compromised shield remains usable before applying another defensive modifier.

Work orders name damage, target function, parts/material, qualified worker, tools, access, usable hours, concurrency cap and acceptance. Routine progress is rate×usable time, bounded by real inputs and remaining work. If uncertainty exists, the default Success gives planned progress, Mixed half and Failure no usable progress unless another branch was agreed. Actually spent or spoiled material is charged once. Field repairs restore named limited function; full restoration clears only completed maintenance debt. A better roll cannot manufacture a missing grip, strap, forge or worker.

<a id="s14"></a>

## 14. Anatomical injury, care and recovery

Record each wound's site and structure, mechanism, impaired functions, severity, onset, source event, contamination/exposure, bleeding/shock, care requirements and next review. Apply the worst penalty to a function: Minor −5, Moderate −10, Serious −20, Critical and Mortal case-specific restrictions. Add another penalty only for a distinct causal limitation. The same pain does not become injury plus fatigue plus low morale.

Worst-penalty selection is an execution rule; it does **not** mean further wounds do nothing. For each new damaging event:

1. Determine whether it affects an intact structure, an already compromised structure, or a different location.
2. Resolve current protection and actual contact.
3. Reassess cumulative structural damage at that particular site. Further cutting of an already damaged muscle, repeated force on a fractured limb, or a larger reopening can worsen that injury when the mechanism supports it.
4. Record a new injury or replace the affected condition with its worsened state, retaining event history. Do not count the old wound as a second new strike.
5. Recompute bleeding, mobility, hand use, attention and other actual function; schedule any new deterioration.

There is no rule “two minor wounds always equal a moderate wound,” and no safe unlimited wound count. Several unrelated scratches cannot automatically become organ failure; many small bleeding wounds can share a real systemic blood-loss consequence. Repeated-use testing exposed the need for this procedure: a fixture using only the worst single grade allowed dozens of wounds without a bout endpoint.

Bleeding levels from F §73 are observation/triage descriptors: 0 none; 1 minor; 2 significant; 3 severe; 4 catastrophic. For level 2, schedule review after major exertion or about 30 minutes untreated; level 3 on about 10-minute scale or major exertion; level 4 immediately on minute/exchange scale. These are provisional review windows, **not automatic death timers or reliable clinical rates**. A wound-specific credible emergency can override them. At review assess continued loss, actual function, control and treatment; do not roll an arbitrary new catastrophe. Multiple wounds contribute to one systemic blood-loss assessment while retaining their sources.

Shock describes a supported physiological consequence, separately from fear and morale: stable, stressed, compromised, severe, collapse risk. Collapse restricts actual physical action; it is not voluntary surrender. No action roll directly sets a death deadline. If the record lacks enough medical specificity to decide a material prognosis, use a bounded named provisional assessment with explicit uncertainty and an early review; do not pretend a generic number is a diagnosis.

Treatment tasks are separate: assessment, pressure/bandaging, cleaning, immobilization, bleeding control, stabilization, wound management, appropriate extraction or surgery, nutrition/rest support and rehabilitation. A trained practitioner with adequate materials and safe conditions performs routine simple aid without rolling. Treatment success restores only the supported effect. Skill cannot replace absent tools, time, access or an unavailable period procedure. Stable does not mean structurally healed, fit for combat or infection-proof.

Care plans use **Acute → Stabilized → Healing → Rehabilitation → Resolved/Lasting impairment**. F §78 fallback scales are Minor 1–7 days, Moderate 1–4 weeks, Serious 1–4 months, Critical 2–12+ months, Mortal case-specific. These are broad uncomplicated review scales, not guaranteed healing or Roman survival estimates. For each injury name activities permitted, blockers, supplies, responsible caregiver, functional milestones and next review. Normal supported healing advances without daily luck rolls. A scar, altered gait, chronic limitation or lost function can persist while the person develops other livelihoods.

Infection requires an actual exposure and plausible progression, with observation and interpretation distinct. Determine whether the wound is contaminated, what care occurred and what period capabilities are available. Do not import antibiotics or modern sterile facilities, impose an unsourced universal infection percentage, or declare every untreated scrape fatal. Prognosis uncertainty belongs in the record and can make care decisions meaningful.
The selected wound grade is an assessment aid, never a universal incapacitation or death threshold. Establish affected anatomy, function and ongoing process. Resolve permanent death only from a supported lethal process, intervention opportunity and actual elapsed time. Numerical vulnerability and recovery values remain uncalibrated references. No plot armor, retrospective death to restore difficulty, resurrection or mandatory execution after defeat is enabled. [C §§17–19,70]

<a id="s15"></a>

## 15. Gladiatorial institutions and continuing careers

### Gladiatorial institutions and contest lifecycle

A gladiatorial establishment is an organization: people, custody/terms, instructors, accommodation, stores, equipment, care capacity, management, relationships, customers/organizers, finance and records. Admission, training, selection for a show, transport, actual performance and aftermath each consume time and means. A captive is not automatically an arena-ready fighter; a famous performer is not automatically the owner or manager.

Before a proposed bout establish:

1. Organizer, venue, jurisdiction, responsible authorities and the source of their practical powers.
2. Who supplies each fighter, under what arrangement, with what payment/liability and ability to refuse or be coerced.
3. Actual identities/condition, compatible equipment, permitted methods and any known constraints.
4. Match objective, official control/stopping process, recognized submission communication and who can intervene; uncertain historical details are visibly local proposed terms, not universal customs.
5. Preparation, movement, holding, rest, aid/care, transport and reporting capacity.
6. What the PC knows of these terms, including credible risks and unresolved promises.

Matchmaking follows actual availability, business and organizer goals, local practice, perceived capability, existing obligations and practical safety or cruelty. It never secretly matches every opponent to the PC's power level. Someone can receive an unfair assignment for a causal institutional reason. An opponent can be weaker because the world contains weaker people. Performance may improve a future offer through actual witnesses, not automatically summon an unbeatable champion.

Run the bout through preparation→arrival/inspection where applicable→declared contest→decision/stop event→immediate safety or violence→care→accounts/reporting→longer consequences. Each arrow is an event, not a guaranteed protection. A surrender request can create an official or opponent decision; it does not teleport the requesting fighter to safety. An attempted execution is a physical action by an actor with actual means, time and opportunities for intervention. Losing a combat check does not itself execute the fighter.

Maintain separate fields for tactical objective, functional ability, NPC willingness/PC-declared response, official decision, survival, injury/care, payment/claim, legal consequence and audience knowledge. Defeat, release from a bout, career discharge and manumission are different processes. Victory can coexist with expensive injuries, delayed pay or a missed contract deadline. A loss can coexist with survival and useful learning. Crowd approval influences actual decision-makers only where their goals/authority permit it.

For NPC discretion use goals, obligations, costs, alternatives and information. Routine authorized judgments need no die. Where a persuasion effort or an actual uncertain institutional decision matters, define plausible branches before one check. Do not substitute one universal “mercy percentage,” crowd meter or fame threshold. Particular event terms may set a condition in advance; honor it unless an actual actor changes or violates it and accepts the resulting consequences.
### Accounts, care and continuing careers

The appearance fee, prize, reimbursement, liability and amount permitted to the fighter are separate contract fields. A sponsor payment to a school changes that school's ledger; only an actual permitted transfer changes the fighter's administered funds. Promised freedom is a claim/obligation until its actual legal route takes effect. Performance creates evidence, not automatic cash or citizenship.

After an appearance reconcile injuries, equipment, missing/held property, physical custody, immediate treatment, transport, work restrictions, claims and reports. An establishment's finances respond to actual fees, instruction, provisions, upkeep, treatment, foregone work and hiring. No universal assumption says every profitable owner preserves every fighter or every cruel owner kills valuable people; particular motives and institutions decide.

Staffed care capacity is binding. One practitioner treating an emergency is unavailable for incompatible routine work. Supplies at a remote store do not treat a fighter until delivered. When simultaneous casualties exceed aid capacity, established priorities and NPC judgment allocate real attention; this is not a roll that creates extra healers. An injured fighter can teach, mend equipment, study language or administer accounts when those activities fit actual ability, authorization and voluntary decisions.

Career states describe current reality rather than unlock tiers: held for sale, in transit, under assessment, under instruction, fit for a particular task, restricted, selected, performing, recovering, reassigned, discharged, free, employed, retired or dead. Several different fields can coexist. A slave instructor, free contracted fighter, wounded celebrity and retired patron are possible configurations; none is a mandatory stage.

Death ends the person's future action capacity at its actual timestamp. Orders already received can continue through other actors; messages already sent remain in transit; debts/claims and property pass through applicable institutions. Death does not cancel unrelated projects or start an automatic revenge plot. Continued play with another protagonist needs an agreed continuation premise and preserves history.
### Death, retirement and succession

Permanent death follows a supported lethal process at an actual timestamp. It ends the person's future action capacity. It does not reverse money already sent, commands already received, an accepted delivery, other people's lives, or independent projects. Missing, presumed dead, and confirmed dead remain distinct knowledge/status fields. [C §§68–70, 95–96; M §§6.10, 14]

At death: close future personal commitments; preserve pre-death actions and pending effects; identify property the person actually owned, administered, held, or owed; record who knows; apply supported custody/estate procedures and claims; update the affected organizations' staffing; schedule notifications and consequences. Do not treat an administered peculium as a modern freely inheritable estate or automatically assign another person's property to relatives. Unresolved legal claims remain unresolved until processed.

Retirement is likewise an arrangement, not disappearance. Record livelihood, housing, care, relationships, residual duties, property management, and the person's own decisions. A former fighter can teach, trade, manage, recover, or live quietly when capacities, terms, means, and authorization support it. Opposition does not escalate simply because stable life succeeds.

Continued play through another protagonist is **opt-in**. The successor must exist or be explicitly created, have their own dossier and knowledge, and receive only property, authority, obligations, or information that actual mechanisms transfer. They do not inherit the previous person's skills, memories, universal reputation, or all assets by default. World state and surviving NPC autonomy continue; the new player character is not a reset of the campaign.

<a id="s16"></a>

## 16. Runtime, historical change and scale

An authorized activity interval is processed by event boundaries, not by narrating its whole duration and repairing contradictions afterward:

1. Confirm the PC's authorized objective, interval, means, continuation limits, and standing instructions.
2. Build compatible NPC schedules and reservations from received instructions and current plans.
3. Find the earliest event that changes feasibility, cost, risk, service allocation, or a meaningful player choice.
4. Advance work, consumption, travel, care, and learning only to that boundary, using each authoritative owner once.
5. Resolve causal dependencies first. Evaluate independent simultaneous effects from the preceding state and commit together. Competing claims on one resource need allocation or contest before commitment.
6. Record transactions, status/function changes, completed work, reports actually received, and new events. Validate quantities, time, custody, capacity, and duplicate event IDs.
7. Return control when a fresh PC decision is required. Otherwise continue the original authorized activity. OOC discussion advances no campaign time.

Stop conditions include a new purchase or promise, changed danger beyond authorization, unavailable prerequisites, meaningful involuntary restriction, or an event requiring a choice. A reasonable NPC implementation within delegated authority can continue. The player is not asked to approve every routine grain serving, but a simulation cannot infer permission for a new voluntary gamble or dangerous career commitment.

Daily, weekly, and institutional summaries are views. Detailed scenes replace the same people/time/task portion of an abstract interval. Mark `period | actors/resources | resolved activity | event IDs | residual unresolved scope`. When a bout consumes two hours already inside the day's schedule, remove those hours from remaining institutional capacity. Do not add a second day's provisions, repeat wounds, refresh fatigue, or award both detailed and abstract training.

**Fictional scale fixture:** a ten-person cohort is scheduled for 4 h practice, nominally 40 learner-hours. Extracting one named person for 1 h care leaves that person 3 h and the other nine 36 h, totaling 39 h if all other prerequisites hold. The extracted person remains one of the ten; naming does not make the cohort ten plus one. The caregiver loses the actual conflicting service time. No arithmetic averaging makes a missing instructor qualified.

Keep exact consequential quantities and named relationships. Aggregation can retain homogeneous lots or cohorts, but unknown individual allocation remains unknown until required. Disaggregation draws conservatively from preserved totals and records the new detail. It cannot supply convenient coins, food, skills, or injury-free personnel that were never present. [C §§11–12, 62, 84, 90–91; P §§15–17; M §§15–18]
### Historical baseline and divergence

Baseline records identify the researched event/process, source/date/uncertainty, actors/places, prerequisites/resources, expected interval, dependency links, divergence status and reporting channels. A change to a prerequisite triggers reassessment of the affected consequences; unrelated processes continue. Do not force an original outcome after a sufficient causal divergence or extrapolate the whole future from one invented roll.

A divergence record names its campaign trigger, changed prerequisite, affected baseline records, causal mechanism, revised forecast, remaining uncertainties and review event. History is knowledge only when an actor could receive it. [C §§10–12,76,85,87]

<a id="s17"></a>

## 17. Records, persistence and presentation

[CORE / ROMAN / IMPLEMENTATION]

Keep one authoritative owner for each fact and resource. Panels, forecasts, roster totals and summaries derive from it. Use the least detailed record that preserves the next meaningful decisions; expand an item, person or function only when identity matters.

**Minimum journal entry:** event ID; causal time; cause/authorization; affected record IDs; consequential changes; actual costs/transfers; result; visibility; new/cancelled pending events. Add raw rolls, independent modifiers and Mixed branch when a check occurs; source/destination and exact units for a transfer; action expenditure and reaction debt when relevant. Contiguous routine work under unchanged conditions may be one interval entry bounded by meaningful events, retaining fractional work, exertion and learning internally.

Automated implementations may add record versions, read/write sets, simultaneous groups and full before/after states. These are implementation fields, not a compulsory form for every meal or conversation. Manual play instead checks current affected records before commitment. Both reject conflicting spending, negative stock, duplicate application and repeated costs.

**Checkpoint:** campaign ID, selected engine/profile versions and adoption status; clock/date convention; authoritative current records; active commitments/debt/reservations; pending events; work/training/load fractions; information/report records; applied-event boundary and recoverable IDs/payloads; unresolved rulings and invalidations; storage/privacy limits.

An applied event with the identical payload is a replay and changes nothing. The same ID with a different payload is an integrity conflict: reject and repair it. Independent simultaneous effects read the valid pre-event state; exclusive resource writes are allocated or contested before atomic commitment. Recompute dependent views after commit. A report updates knowledge rather than reapplying the underlying damage, payment or loss.

A correction freezes advancement, records the invalid event, restores the last valid affected state, recomputes dependent consequences and retains unrelated valid events. Correction costs no campaign time. New design defaults apply prospectively; resolved play changes only through an explicitly authorized correction/retcon. [C §§11–13,62,86,90–91,97,99; M §15]

### Information privacy and presentation

The simulator's authoritative state differs from each actor's knowledge. Private state needs actually supported recoverable private storage. An ordinary user-readable workspace file is recoverable, not inherently secret. Unrecorded reasoning is not persistence, and hashes cannot restore missing hidden records. Disclose deployment limits rather than promising unavailable private continuity.

Each ordinary scene contains **Situation → perceptible causal factors → open opportunity to act**. Aim for 100–150 words where practical, with a brief relevant state view if needed. Never shorten away a meaningful decision or mandatory accounting. Contextual panels emphasize custody, assessment, work, combat, care, household or management while reading the same dossier. Hidden modifiers and motives are not exposed as exact statistics. Design/OOC discussion advances no time.

<a id="s18"></a>

## 18. Content, profiles and deployment

Establish a place's eligible population, roles, goods, institutions, routes, and services from supported world data or explicitly proposed generation. Distinguish **exists → known → accessible → available now → usable**. A prosperous market may have many sellers without guaranteeing this rare item, sympathetic buyer, qualified healer, or affordable offer.

Where individuals are not yet named, preserve finite role/cohort capacity and their location/time basis. Instantiate a person by extracting from an existing eligible pool, or by a recorded arrival, recruitment, birth, or other supported event. Name, capabilities, role, schedule, resources, and relevant knowledge must fit that basis. Do not create an extra instructor because the only instructor is busy or a richer purchaser because the player wants a high price.

If the world was not detailed enough to decide availability, make one bounded generation decision under the profile's declared method, with provenance, before resolving the search or transaction. Preserve its outcome. It is a newly established detail, not a recovered historical fact. Random selection is optional; no universal rarity probability is supplied. Success in searching establishes the agreed information or access, not permission to override an empty eligibility pool.

NPC emergence can follow actual events: an injured worker needs care; a creditor sends a representative; a delivery brings a bearer. Each consumes or assigns real institutional capacity. Persistent relevant NPCs retain their record. Incidental people can remain a cohort unless identity matters. Exits and absences require causes, not deletion to clear narrative space. [C §§64–65, 79, 89; P §6; FL §§1–4; PL §§15–16; ML §§1, 6.]
### Campaign initialization and prospective adoption

Complete Appendix A before resolving the opening scene. A necessary local parameter can be a researched value, explicit scenario assumption or scoped provisional ruling with a review trigger. Keep these distinct. Establish enough for the immediate situation; do not demand an encyclopedic world database or treat an unknown peripheral fact as incapacity.

The default premise supplies youth, frontier origin in broad terms and entry into slavery. It does not supply an exact ethnicity, motives, family fate, talents, ownership chain or convenient possessions. Necessary world generation may set a dated locality, custodian, immediate provision, goods and nearby actors under the selected profile. Player-controlled identity/background choices remain player-supplied or explicitly delegated. The illustrative profile below is replaceable and uninstantiated.

For a new campaign record the selected edition, enabled rules, calibration/rulings, storage/randomness support and adoption scope. For an existing campaign inventory its established rules, state, unresolved events and conflicts first. Map records conservatively; preserve earned competence, injuries, claims, custody, money, commitments and knowledge. Unknown-unit training stays unresolved. Do not convert a rejected HP/attribute array into invented anatomical damage or capacities. A new edition never advances the campaign clock.

This 1.0 consolidates the 0.1 operating selections and makes the additional interfaces explicit. Preserve stable ROM rule IDs. ROM-PLAN-01 now treats duties as decision inputs; NPCs are not compelled to obey. Evasion/range selections are new prospective rules. Historical/numerical values require their own evidence and calibration; sibling sources' certification does not transfer. [C §§88–100; F/FL selection boundaries; M §§15–19]

<a id="s19"></a>

## 19. Worked acceptance cases, validation and version policy

The companion [validation report](roman_republic_v1_0/IRGS_Roman_Validation_Report_v1_0.md) distinguishes numerical regression, worked acceptance cases, proposed repairs and remaining calibration. The [seven-source audit](roman_republic_v1_0/Source_Audit.md) preserves original section/line provenance. The original 0.1 audit is retained as prior design evidence; it is not relabeled as an independently repeated historical review.

| Acceptance case | Required result |
|---|---|
| Impossible attack, maximum roll | No reach, penetration, means or extra action appears |
| Emergency evasion | One eligible response, cost once, selected effect on same attack; debt persists |
| Aim/repeated aim/release/recovery | One preparation bonus; real projectile changes location once; unusable recovery remains unusable |
| Several lesser wounds | Functional modifiers do not erase anatomical aggravation or combined blood loss |
| Training interrupted by duty/care | Only actual qualifying hours; no automatic advancement or double person-time |
| Captive released physically | Custody changes; legal emancipation follows its configured route only |
| Social undertaking | Willingness/commitment changes; dependent work and third-party decisions remain pending |
| NPC evades duty | Supported autonomous decision; actual absence, opportunity costs and institutional consequences |
| Unknown stock or quote | Bounded fact established before commitment; no guaranteed desired goods or retrospective veto |
| Simultaneous double sale | Shared last item allocated before commitment; no duplicate ownership |
| Delayed bridge report | Physical passage changes immediately; distant knowledge changes on receipt |
| Detail inside a workday | Matching abstract interval replaced; no duplicate hours, provisions or casualties |
| Save/reload/report review | No repeated costs, learning, losses or awards; conflicting ID payload rejected |
| Successful livelihood/retirement | Security persists until an actual cause changes it; no automatic escalation |

The numerical fixtures are bounded models, not a full campaign implementation or natural-language GM evaluation. Grades ≥3 and 60-exchange caps in the experimental bouts are experiment endpoints, not medical rules. Tests exposing indefinite T1 wound accumulation and continuous-coverage immunity remain documented limitations of those fixtures. This edition includes anatomical reassessment and actual coverage/wear procedures; those have not been turned into a validated physiological simulator.

Highest-priority calibration: human injury/protection/bleeding and care; sustainable workloads and deprivation; discipline-specific learning; dated legal procedures and enforcement; provision, tender, prices and throughput; arena stopping/liability/frequency; travel and information delays; long-period household/institution continuity; and record burden. Human playtesting and adversarial GM trials remain separate from arithmetic verification.

**Version policy:** incompatible ownership/behavior changes require a major revision; compatible extensions a minor revision; corrections without changed behavior a patch. Every revision records affected rules/interfaces, evidence, migration and scope.1.0 is the first consolidated reference edition, not a declaration of balance or certification. Existing campaign status remains Proposed unless explicitly adopted through its own record.

<a id="s20"></a>

## 20. Source ownership and provenance

| ID | Reviewed source | Contribution and boundary |
|---|---|---|
|C|IRGS Integrated Framework v2.1|Required parent; agency, uncertainty, time, resources, information, organizations and continuity|
|F|IRGS Core Fantasy World Engine v1.0|Selected mundane competence/training/tactics/protection/injury interfaces; no fantasy attributes, powers or lore|
|FL|IRGS Fantasy Content Libraries v1.0|Entry/variant/instance and material/profile discipline; no automatic equipment or creature availability|
|P|IRGS Post-Apocalyptic Survival and Reconstruction Foundation, internallyv 1.1|Finite provision, qualified service/work and infrastructure dependencies; no apocalypse premise|
|PL|IRGS Post-Apocalyptic Content Libraries v1.0, parentPAF 1.1|Mundane stock, storage, service and content schema; no modern technology|
|M|IRGS Military Life Simulation Engine v0.4|Commitments, rosters, delegated work, care/repair and career aftermath; no modern law/rank/pay|
|ML|IRGS Military Equipment and Technology Library v0.1|Era/category eligibility filter; no supplied Roman weights, prices or performance calibration|

Roman-owned rules are local selections/proposals in this publication; they are not automatically promoted into Core. The external evidence links for denomination accounting and manumission appear in §§6–7. The companion report records limits of research on gladiatorial institutions and later-dated material. External history, source-supported IRGS mechanisms, inference and proposed campaign generation remain distinct.

<a id="appendix-a"></a>

## Appendix A — Campaign profile and selected defaults

A campaign profile is configuration, not current state. Record:

`profile/version/adoption status | date/place/calendar convention | premise and player-controlled creation fields | enabled activities/overrides | local authorities and legal routes | languages/disciplines | provision/work/rest assumptions | equipment eligibility/profiles | injury/care/review assumptions | training schedule and access | denominations/tender/market quotes | arena terms if present | travel/routes | NPC generation and institutions | baseline history/divergence policy | randomness/persistence/privacy | provisional rulings/calibration debt`

**Replaceable starter scenario — uninstantiated:** a local holding establishment in Roman Italy during 60–50 BCE, before sale or assignment. The generated situation must establish a particular town/date, custody and claimed authority, shelter/current provision, observable physical condition, communication, held/issued goods, nearby custodian and other relevant actors, and an imminent assessment, transfer or demand. An arena school may be a possible buyer; selection is not guaranteed. No fixed attribute array, HP total, ownership chain, iron collar or secret asset is mandatory.

This scenario supplies a useful opening boundary while leaving identity/background choices to the player. Generate the necessary world records once, label their provenance and retain them. It is not a historical case study or an already-started campaign.

### Selected operating register

| Rule | Selected package default | Local profile supplies |
|---|---|---|
|Resolution|Core d100, scoped 0–5 competence, one cause/charge|Meaningful objective and independent difficulty|
|ROM-INIT-01|Priority ≤35 other/36–65 simultaneous/66+ challenger|Actual readiness and duration first|
|ROM-DEFEND-01|Emergency evasion−10; supported major withdrawal−20; one reserved/borrowed cost|Awareness, space/time, eligible response and trigger|
|ROM-RANGE-01|Long−10/Extreme−20; one-commitment aim+10, nonstacking and consumed|Actual distances, readiness, line, projectile profile|
|ROM-EFFECT-01|Exhausted protected primary channel terminates; supported second mechanism separate|Coverage, actual anatomy, transmitted effect|
|Human reference|Resilience 0|Actual function, physiology and prognosis; explicit prospective overrides|
|ROM-WEAR-01|Local reductions 0/1/2, floor 0; state change clears marks|Base construction, damage location and repair|
|ROM-TRAIN-01|Incremental 40/160/400/1,200/3,200 h plus evidence|Subject, instructor, usable time, suitable assessment|
|Fatigue|Core 0–4; selected load/rest, disrupted sleep retains residual load|Actual activity, sleep, provision and physiological limits|
|ROM-LEGAL-01|Independent fields and particular routes/claims|Dated authority, acts, consequences and review scope|
|ROM-PLAN-01|Goals/knowledge/obligations inform autonomous choices|Particular personality, resources and actual schedule|
|ROM-MONEY-01|Sestertii account; 1 denarius=4 sestertii|Actual tender, foreign exchange, quotes and funds control|
|Continuity|Permanent death; successor play opt-in; one state/clock|Actual transfers, succession and private storage support|

<a id="appendix-b"></a>

## Appendix B — Illustrative dossier and contextual views

These entries are illustrative and **uninstantiated**. They do not create a PC, existing NPC, duty or property.

| Dossier field | Illustrative entry EX-PER-01 | Mechanical use |
|---|---|---|
| Identity | Young household clerk; names/origin not assigned | Identity questions remain open rather than acquiring invented biography |
| Embodiment | Right-handed; fit for ordinary seated work; lifting capacity unassessed | Fine work is possible; heavy carrying needs evidence |
| Capacities | Copies a short familiar entry legibly; notices a mismatch between two visible counts | Observed tasks establish particular capability |
| Latin | Everyday speech/comprehension; reads familiar accounts; unfamiliar legal formulae require explanation | Speech, literacy, register, and legal understanding differ |
| Other languages | Unresolved | No automatic native language or complete cultural package |
| Accounts | Familiar 1; can enter a straightforward receipt with supervision; independent reconciliation unproven | Scoped competence, not universal intelligence |
| Close blade fighting | Untrained 0; no demonstrated advanced techniques | A good roll cannot grant technique access |
| Learning record | Prior familiarity attested; historical hours unrecorded; future qualifying hours start from actual instruction | Creation assessment is not fabricated practice credit |
| Condition | Right wrist painful during forceful grip; cause/care assessment unresolved | Apply its actual limitation to gripping, not every social or cognitive task |
| Exertion/needs | Rested 0 in this illustration; current provision source not assigned | Fatigue is independent from anatomical injury |
| Status | Freedom/civic/household relations unresolved | Occupation does not establish legal position |
| Held goods | Example writing board: issued by an unspecified household; kept in its office; use limited to assigned work | Holding/access does not establish ownership |
| Clothing example | Example working belt: Worn; repair needed at one fastening; ownership unresolved | Worn creates a service requirement; no automatic universal penalty |
| Money | No account instantiated; holdings and administration terms unresolved | Missing data are not zero wealth or unlimited credit |
| Relationships | Supervisor relies on accurate copying; broader personal trust unknown | Confidence in one skill does not establish affection or loyalty |
| Commitments | Example assessment scheduled; no actual duty assigned | The sample cannot silently consume campaign time |
| Knowledge | Knows the two visible counts differ; does not know why | Observation does not reveal deception or hidden motive |
| Goals | No PC goals supplied; NPC goals assigned only if instantiated as an NPC | Role does not author the player's ambition |

An actual dossier attaches evidence and timestamps to these entries. Use adjectives where they suffice; precise measurements belong only where decisions depend on them. A newly assessed skill can be supported by prior experience without inventing its past hour-by-hour ledger. Future advancement follows the selected qualifying-hour and demonstration procedure.

Contextual panels draw from that dossier:

**Work/assessment view:** date/location; assigned task and controller; relevant language/discipline; usable tools; wrist limitation; actual time available; expected deliverable; next interruption. Display no unrelated combat rating unless it matters.

**Captivity/access view:** current custodian/location; visible restraints/guards; claimed status and known disputes; immediate provision; issued versus owned goods; pending demand/transfer. Secret escape-search plans stay outside this panel.

**Combat/care view:** position/reach; usable hands; active injuries and physical restrictions; fatigue; actual protection; commitments/reaction debt; immediate aid and next deterioration review. There is no total HP or global readiness number.

**Livelihood/household view:** accessible cash, administered funds and permitted use, due claims, reservations, next work obligation, household provision, delegated tasks, and reports actually received. Forecasts are labeled; views never spend resources.

[Parents: C §§12–16, 20, 64–69; F §§14–23, 101–107; M §§5–6.]