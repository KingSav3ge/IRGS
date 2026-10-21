# IRGS Core 3.3.C — Engine Development Supplement

**Edition:** C2 · 20 October 2026  
**Status:** Proposed engine specification for implementation by Claude  
**Selected foundation:** IRGS Core 3.3  
**Development ownership:** Codex develops the engine text; Claude implements and verifies it. Emergent's website and app work is 3.3.E.

This supplement develops the consequential action, dependency, persistence and autonomous execution contracts already described by Core. It does not establish that these additions run, that every numerical model is adopted, or that a campaign has been playtested. The supplied v1.4 master is a proposed design reference. Direct user instructions determine the present engine-only scope.

## 1. One world and explicit ownership

Each playthrough has one authoritative world. A historical template initializes a new world; it never overwrites a continuing one. Character play, household management, business, government and military activity submit requests against the same actors, resources, commitments, institutions and event history.

3.3.E submits proposals and displays authorized results. It must not maintain an independent simulation kernel that generates a second set of outcomes. Classification, narration, dialogue proposals, summaries and images have no direct world-writing authority. A provider's successful response establishes neither a successful action nor an actual occurrence.

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

## 2. What an action means

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

### Lifecycle

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

## 3. The resolution contract

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

## 4. Ordinary action adapters

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

## 5. Dependency certification

Each executable adapter must reveal the records it actually reads and changes during validation, authorization, selection and effects. Observation includes negative lookups, existence checks, scans, container access, actual list mutations, retained decisions and external selected-rule identity. Handwritten footprints can explain a model, but cannot alone certify independence.

Authorization and execution must be observed as one path. An action reading a delegation cannot appear independent of simultaneous revocation. A capacity request reading an empty schedule cannot appear independent of another request that fills it. Reading a list is not itself a list mutation; genuinely mutating an ordered container reserves its actual affected scope conservatively.

The coordinator builds a conflict graph against a shared frontier snapshot. Independent qualified operations may commit together after final invariant validation. Conflicting requests remain unresolved unless an applicable authorized allocation or causal ordering is established. Sorting identifiers, request arrival, UI order and database order cannot select a winner.

Read conflicts do not mean that every contender is physically cancelled. Actual physical occurrences, such as independently established destruction of reserved backing, require their occurrence procedure; a reservation cannot veto reality. Reconcile resulting shortfalls without fabricating replacement stock or erasing obligations.

Certification identifies the exact code, rule and source editions, snapshot, operation, exercised branch and observations. It demonstrates that case, not every branch or arbitrary plugin safety. Changed code or bindings invalidate reuse of old certificates for new claims. Failed and deferred branches need evidence as well as successful examples. See the action and dependency contract for acceptance cases.

## 6. Time and autonomous institutions

The Core causal sequence, elapsed simulation time, civil calendar, information receipt time and wall-clock persistence time are separate coordinates. Bind them explicitly where a process needs them. A journal sequence increment is not thirty minutes. A time-of-day band is a presentation range, not an elapsed-time arithmetic unit. Navigation, inspection, saving, retry and narration do not advance the world.

An actor's planner receives only information actually available to that actor or institution. It can propose ordinary Core actions within real mandates, resources and commitments. A household cannot consume a meal that a business merely plans to produce. A government claim is not a paid tax. Military readiness is not equipment duplicated from a depot view. Institutions continue in the same world while the protagonist acts or waits.

Each autonomous process declares goals, needs, obligations, known conditions, policy, scope, authorized spending/time limits, next review and stop conditions. Missing observations produce an information requirement or a bounded decision under explicit uncertainty. They are not evidence of an empty warehouse, a dead actor or a free resource.

The scheduler advances to the next causal boundary across all due processes, resolves shared frontiers and retains processed spans. Coarse reviews must preserve meaningful interruptions and individual commitments. Domain plans never simulate private substitute populations or balances. See the agency/time contract for the first four-institution acceptance slice.

## 7. Historical worlds and character continuity

New historical playthroughs load a designated dated starting snapshot. Continuing worlds use their actual committed temporal registry. Existence, conflict participation, scenario eligibility and player control are different properties. Collapsed or dissolved entities cannot return because a later historical template names them; new simulated organizations may become available through actual formation and eligibility records.

Historical baseline events remain prospective reference assertions until their qualified live causes execute. Check relevant participants, resources, political circumstances and dependencies at the applicable frontier. A failed prerequisite can prevent, alter, postpone or supersede the prospective configuration; it does not require a substitute battle, mandatory victory or global historical correction. Reference outcomes are not actual Chronicle events or player knowledge.

Retain all 37 proposed HYW entry dates and ten featured entries. Only the developed 1415 initializer has the current researched readiness. A Scot's Tale remains a named 1415 starting reference, with its unresolved civil-date reconciliation preserved. Its archived post-Day-2 character guide and the corrected name Abel do not justify an inferred date, recovery, employment or next voluntary act. Reusable mechanics belong to their shared Core or genre owner.

## 8. Implementation and adoption gates

Claude's first coding milestone is a durable typed action workflow over the existing Military equipment-issue and Roman delegated-activity handlers, with current control and authority checks inside observed execution. Equipment issue can establish completed transfers. A future Roman capacity booking establishes a schedule, not completed labour. Unsupported action families remain honestly unresolved until their adapter is implemented and qualified.

The subsequent milestone binds actual elapsed time and receipt-backed autonomous proposals to that same path. Ordinary movement, observation and dialogue then need their own genuine effect contracts and acceptance evidence before a general first-action or Living Day claim.

Design completion, implementation, passing tests, deployment, campaign adoption, calibration and playtesting are separate statuses. A package checksum establishes integrity, not authority or correctness. This supplement is text development ready for implementation review; it is not a live replacement for the selected runtime.

## 9. C2 ordinary-action development

The C2 contracts develop the ordinary-action meanings in section 4: `TIMELINE_AND_PROCESS_CONTRACT.md`, `MOVEMENT_AND_OBSERVATION_CONTRACT.md` and `DIALOGUE_AND_SOCIAL_ACTION_CONTRACT.md`. They preserve the common lifecycle, receipt identities, current authority and nine-owner boundaries. Routine capability remains qualitative where supported; missing numerical fields do not impose arbitrary rolls or incapacity.

`PLAYABLE_ACTION_CYCLE.md` connects those contracts through an explicitly synthetic fixture with actual movement, communicated terms, shared-capacity allocation, partial parcel work, interruption, continuation, acceptance and payment. Its selected values belong to the fixture, not to HYW or all IRGS campaigns. `IMPLEMENTATION_PACKETS.md` divides that design into coding scopes while preserving the C1 foundation.

C2 adds 66 proposed acceptance cases to the original 55. It does not add runtime acceptance results. Unimplemented contracts remain visible in the Claude handoff and machine-readable indexes.
