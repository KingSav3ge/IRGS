# IRGS Historical Campaign Framework

Revised Historical Timeline & Event Simulation Specification — v0.2

Proposed revision

Historical State Database · Event Scheduling · Alternate History

## 1. Governing principle: History is the default, not the limit

This correction changes an important part of the previous Historical State Database design.

Every historical campaign will possess a predetermined historical timeline. That timeline is the intended course of events unless circumstances within the simulation justify a different result.

For the Hundred Years’ War, this means:

- A campaign beginning in 1337 starts with the historical conditions of 1337. Subsequent events are intended to follow their recorded chronology unless earlier developments change their causes, circumstances, or outcomes.
- A campaign beginning in 1389 begins in the historically established world of 1389. Events from 1337 through the selected starting date have already occurred as historically recorded.
- A campaign beginning in 1415 has the siege of Harfleur, Battle of Agincourt, Treaty of Troyes, and subsequent historical developments in its prospective event timeline, with the relevant prerequisites and conditions.
- A campaign that diverges from history must simulate the consequences. The original timeline can continue where unaffected, change where necessary, or become completely unrecognizable if the cumulative changes are significant.

This is neither rigid scripted history nor unrestricted random alternate history.

The intended model is conditional historical determinism, followed by causal simulation when historical conditions are disrupted.

### The three governing rules

Rule 1 — History before entry is established.

Every campaign entry begins from its historically reconstructed state. Events predating the initialization cutoff are part of the world's existing history, not future events to be replayed.

Rule 2 — History after entry is the intended future.

The historical event schedule exists from the first moment of the campaign. Events are prepared to occur at their recorded dates, subject to their causal requirements.

Rule 3 — Simulation takes precedence over historical expectation.

When historical circumstances no longer support a planned event, the event must be reconsidered. It may be modified, moved, replaced, or eliminated. History must never forcibly restore an outcome made impossible by gameplay.

The same system should operate whether the disruption comes from player action, autonomous rulers, economic developments, disease, military defeat, or another properly simulated cause.

## 2. Revised architectural ownership

The event system itself should be reusable, with historical campaigns providing their own event libraries.

| Layer                               | Responsibility                                                                                                                                                 |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IRGS Core                           | Authoritative clock, causality, scheduled actions, event triggers, state changes, autonomous actors, information transmission, continuity, resource accounting |
| Historical Genre Foundation         | Historical timeline interpretation, conditional historical event plans, divergence evaluation, research provenance                                             |
| Historical Campaign Content Library | Historical events, people, treaties, battles, reforms, relationships, and their documented causes and effects                                                  |
| Campaign Profile                    | Historical period, entry point, supported regions, initial historical state, enabled rules, and alternate-history policy                                       |
| Campaign State                      | Events actually occurring in this playthrough, current actors, resources, history, knowledge, and consequences                                                 |

The new historical functionality must inherit Core's scheduling and state-transition mechanisms rather than establishing a second clock or independent resource ledger.

### Two different timelines

Historical Baseline

An immutable reference chronology containing the events that actually occurred in recorded history.

Research-backed · Versioned · Not altered by gameplay

Campaign Timeline

The authoritative history of the active simulation, initially aligned with the historical baseline.

Dynamic · Causal · Updated by actual developments

The baseline remains available for the simulation to compare intended and actual developments. It is not itself the authoritative future of the campaign.

The campaign also maintains a prospective event plan, derived from the historical baseline. That plan is neither past history nor a collection of events that have already occurred.

## 3. How choosing a starting date changes history

Consider the Hundred Years’ War timeline from 1337 to 1453.

Historical entry-point comparison

Select a start

1337

1360

1369

1389

1415

1422

1435

1444

1449

1453

1337

Start: 1415

1453

Established history

Conditional historical future

1415 — Campaign initialization

1369: War resumes — already established

1389: Leulinghem — already established

1415: Invasion — already established

Next intended historical events

1422: Dual monarchy claims — conditional

1435: Arras — conditional

1444: Tours — conditional

Illustrates the historical cutoff rule. The actual database will use precise dates and a much denser event chronology.

There are two vital consequences.

First: Starting in 1389 means that the earlier battles, treaties, successions, deaths, and political changes have already occurred historically. The simulation does not begin in a speculative version of 1389 generated from 1337.

Second: Starting in 1337 gives the simulation the opportunity to change any subsequent historical development, including events normally associated with 1389, 1415, or 1453.

A campaign beginning in 1337 could therefore create a diplomatic settlement in 1369 similar in function to the historical Truce of Leulinghem. However, it would not automatically be the identical treaty: Richard II and Charles VI would not yet be the reigning monarchs. The database must distinguish an altered version of an identifiable event from an earlier historical analogue involving different participants.

## 4. Historical event plans: triggers, prerequisites, and outcomes

A historical event must contain more than a date and a description.

Every event requires a Historical Event Plan, which specifies why it happened, what conditions allowed it to happen, who participated, when it should occur, and which consequences it historically produced.

### Event plan record

| Field                     | Purpose                                                                        |
| ------------------------- | ------------------------------------------------------------------------------ |
| `event_id`                | Stable identifier of the historical event                                      |
| `historical_date`         | Recorded historical date or date range                                         |
| `historical_description`  | What actually happened                                                         |
| `historical_participants` | Actors and institutions involved                                               |
| `prerequisites`           | Conditions necessary for the event to remain possible                          |
| `supporting_conditions`   | Circumstances that make its historical progression plausible                   |
| `historical_intentions`   | Documented or inferred objectives and plans of participating actors            |
| `location_requirements`   | Geographical constraints on the event                                          |
| `resource_requirements`   | Forces, supplies, authority, or other resources required                       |
| `trigger_conditions`      | When preparation or execution should begin                                     |
| `historical_outcome`      | The documented result of the event                                             |
| `historical_consequences` | State changes that followed historically                                       |
| `dependent_events`        | Other planned events relying on this event or its consequences                 |
| `temporal_flexibility`    | Whether the event may occur earlier, later, or only within a particular window |
| `substitution_rules`      | What to do if the event cannot occur in its historical form                    |
| `source_references`       | Evidence supporting the plan and its individual assertions                     |

Historical sources will not establish every prerequisite. Where the system infers causal dependencies, they must be explicitly marked as design inferences rather than historical facts.

### Two categories of prerequisites

Hard prerequisites are necessary conditions without which the event cannot occur as defined.

Supporting conditions are historically influential circumstances that can change without making the event impossible.

For Agincourt:

| Condition                                                                  | Classification                              | Implication                                                                                  |
| -------------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| English and French forces exist and are capable of combat                  | Hard                                        | Without opposing combatants, the battle cannot happen.                                       |
| Both forces are within operational reach of one another                    | Hard                                        | No encounter can occur if they cannot physically meet.                                       |
| Relevant commanders remain alive and in command                            | Hard for the exact historical configuration | The battle might still occur under different commanders, but is no longer identical.         |
| Henry V's army has suffered losses and sickness during the campaign        | Supporting                                  | Changes the English army's capabilities, not the existence of war.                           |
| French forces attempt to intercept the English                             | Hard for the historical encounter pathway   | Without interception or another encounter mechanism, that particular battle does not emerge. |
| Weather and ground conditions favour the historical tactical sequence      | Supporting                                  | Different conditions may produce a different battle outcome.                                 |
| Both armies possess their historically documented equipment and formations | Supporting                                  | Different equipment or formation alters tactical resolution.                                 |

Hard prerequisites are evaluated literally. Supporting conditions affect the event's feasibility, likely execution, and resulting circumstances; they are not arbitrary switches that cancel it.

### Historical default resolution

The engine should use two resolution paths.

| Situation                                                                             | Behaviour                                                                                  |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| The historical causal pathway is materially intact                                    | The event proceeds on its historical schedule, with the documented outcome as the default. |
| A relevant actor, resource, location, decision, or condition has meaningfully changed | The affected portions are resolved through ordinary simulation.                            |
| The event remains feasible but conditions have changed                                | It can still occur, but timing, participants, conduct, or outcome may differ.              |
| The event's prerequisites cannot be satisfied                                         | The historical event is prevented; autonomous actors may pursue alternative actions.       |
| A different event has already resolved the underlying objective                       | The planned historical event becomes redundant or is superseded.                           |

No hidden historical correction rolls: The system must not grant historical commanders bonus capability, fabricate reinforcements, override player successes, or force a preferred result merely to recreate the historical record.

Conversely, the simulation should not randomly rewrite history everywhere simply because the campaign has started. Undisturbed historical event pathways retain their intended outcomes.

## 5. Historical event lifecycle

Planned historical event

Exists in the future event schedule

Evaluate causal prerequisites

Check actors, locations, relationships, capabilities, resources, and time

Path intact

Historical result

Path altered

Simulated result

Path blocked

Delayed or replaced

Commit actual campaign consequences

Update the authoritative world state and reevaluate dependent events

Internally, the plan should support the following statuses:

| Status                 | Definition                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------- |
| `PLANNED`              | Historical event remains scheduled and causally viable.                                 |
| `PREPARING`            | Required actors have begun the actions leading toward the event.                        |
| `AT_RISK`              | Relevant conditions have changed and the intended event requires reevaluation.          |
| `RESCHEDULED`          | Its core event remains possible but has moved to another date.                          |
| `ALTERED`              | The event remains recognizable, but its participants, circumstances, or outcome differ. |
| `OCCURRED_AS_RECORDED` | Historical event and outcome occurred as planned.                                       |
| `OCCURRED_ALTERED`     | Recognizable historical event occurred, but with a different result.                    |
| `SUPERSEDED`           | Another event fulfilled or removed its underlying purpose.                              |
| `PREVENTED`            | The historical event can no longer occur.                                               |
| `EXPIRED`              | The plan's historically meaningful opportunity has passed without occurrence.           |

These statuses concern the historical plan. Actual battles, deaths, treaties, and other occurrences are separately recorded in Core's authoritative event history.

An event must not consume resources or alter the world simply by changing from `PLANNED` to `PREPARING`. Physical or institutional consequences follow only from actual actions and effects.

## 6. Event movement and alternative history

Historical events will have different degrees of temporal flexibility.

| Temporal class            | Example                                               | Permitted changes                                                                                                                          |
| ------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Date-sensitive event      | A particular battle between identified armies         | Can move if the participating forces and actual operational conditions support a later or earlier encounter.                               |
| Causal-sequence event     | Peace following military exhaustion                   | Can occur whenever the necessary political and strategic conditions develop.                                                               |
| Institutional development | Military reform                                       | Can occur earlier, later, or differently if actors possess the knowledge, authority, resources, and incentive.                             |
| Biographical event        | A ruler's death, marriage, or succession              | Requires age, survival, personal circumstances, and the relevant cause or decision.                                                        |
| Environmental event       | Epidemic, storm, crop failure                         | Must follow biological, ecological, meteorological, and geographical causes rather than political convenience.                             |
| Historical analogue       | A different treaty accomplishing a similar settlement | Is recorded as a new campaign event, linked to the original event's function but not falsely identified as the same historical occurrence. |

### Example A: The Truce of Leulinghem occurs earlier in function

Historical baseline: England and France enter the Truce of Leulinghem in July 1389, after prolonged war, financial pressures, and negotiations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://en.wikipedia.org\&sz=32)

Wikipedia



Alternative campaign beginning in 1337:

Suppose England suffers more severe defeats in the 1360s, while the French monarchy is exhausted by maintaining expensive campaigns. Political incentives for peace could develop sooner.

The simulation may produce negotiations culminating in a lasting Anglo-French truce in 1369.

The result would be:

| Historical plan                                          | Campaign outcome                                                  |
| -------------------------------------------------------- | ----------------------------------------------------------------- |
| Leulinghem truce, 1389                                   | New Anglo-French settlement, 1369                                 |
| Richard II and Charles VI as historical rulers           | Edward III and Charles V, if both retain their historical offices |
| Historical late-fourteenth-century settlement conditions | New conditions produced by the preceding campaign                 |
| Historical cessation of large-scale campaigning in 1389  | Earlier cessation, with its own terms and duration                |

The historical Leulinghem event may be superseded if its purpose has been resolved. Its existence is no longer necessary merely because it appears in the historical timeline.

It must not be renamed Leulinghem by default, given the different participants and circumstances.

### Example B: The English invasion of 1415 is delayed

If the English crown experiences serious internal conflict, lacks sufficient money, or cannot secure the necessary ships, Henry V's planned invasion may become infeasible in August 1415.

The event can be delayed while the crown attempts to obtain resources or resolve its political constraints.

If an expedition becomes viable in 1416, the invasion could then proceed.

However, the associated campaigns must also be reconsidered. The siege of Harfleur and the Battle of Agincourt cannot simply be shifted forward one year as an identical chain regardless of French defensive preparation, weather, command appointments, and other changes.

The historical campaign plan provides intended objectives and operational context. Its actual implementation follows the state of the world.

### Example C: A historical participant no longer exists

Suppose Henry V dies before 1415 in a campaign beginning decades earlier.

The historical 1415 campaign under Henry V is impossible.

That does not mean England becomes incapable of invading France. His successor, if politically and militarily capable, may pursue similar objectives.

The engine should:

1. Prevent the historical invasion under Henry V.
2. Resolve the actual succession and resulting political arrangements.
3. Reevaluate England's war aims, obligations, finances, and military preparations.
4. Allow a successor or other authority to pursue an alternative invasion if appropriate.
5. Classify any replacement operation as a new simulated event rather than pretending Henry V commanded it.

The objective may survive the individual. The individual's historical participation cannot.

## 7. The Hundred Years’ War historical event network

The historical campaign library will contain a network of events from 1337 through 1453, with related developments outside that period where necessary to establish causes or consequences.

This is not a single chain in which every event depends on the preceding event. It is a collection of interconnected political, military, economic, environmental, and biographical histories.

### Principal historical anchors

| Date      | Intended historical event                      | Important causal dependencies                                                          |
| --------- | ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| 1337      | Opening Anglo-French conflict                  | French confiscation of Guyenne, English territorial interests, political relations     |
| 1340      | Battle of Sluys                                | English and French naval operations and available fleets                               |
| 1346      | Battle of Crécy                                | Edward III's campaign, French military response, army movement                         |
| 1346      | Battle of Neville's Cross                      | Anglo-Scottish conflict, David II's invasion, English defence                          |
| 1347–1349 | Black Death devastates England and France      | Disease introduction, travel networks, population exposure                             |
| 1356      | Battle of Poitiers                             | Black Prince's campaign, French military response, John II's participation             |
| 1360      | Treaty of Brétigny                             | Military positions, John II's captivity and ransom, political negotiations             |
| 1369      | Anglo-French war resumes                       | Breakdown of the settlement, Gascon appeals, French and English decisions              |
| 1372      | Battle of La Rochelle                          | Castilian-French naval cooperation, English maritime operations                        |
| 1389      | Truce of Leulinghem                            | War exhaustion, diplomacy, political objectives, fiscal conditions                     |
| 1399      | Henry IV takes the English throne              | Richard II's government, political opposition, Bolingbroke's actions                   |
| 1415      | Harfleur campaign and Agincourt                | Henry V's invasion, French response, military movement and encounters                  |
| 1420      | Treaty of Troyes                               | Military and political balance, Charles VI's government, Burgundian relationships      |
| 1422      | Deaths of Henry V and Charles VI               | Survival, health and personal circumstances; succession institutions                   |
| 1429      | Relief of Orléans and Charles VII's coronation | The English siege, French resistance, Joan of Arc's participation, royal authority     |
| 1435      | Treaty of Arras                                | Burgundian and French negotiations, diplomatic objectives, previous political conflict |
| 1444      | Truce of Tours                                 | Negotiation, political authority, military circumstances                               |
| 1445–1448 | French military reorganizations                | Crown finances, administrative authority, recruitment, and reform policy               |
| 1449      | Renewed French campaigns in Normandy           | Truce breakdown, French military capacity, English territorial position                |
| 1450      | Battle of Formigny                             | French reconquest campaign and English military response                               |
| 1453      | Castillon and the recovery of Bordeaux         | Anglo-Gascon resistance, French campaign, field armies, artillery, siege operations    |

This is the initial event inventory, not a completed event database. Each anchor will be expanded into multiple smaller plans and dependencies. Major events and dates are supported by the Royal Armouries chronology and broader historical references.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://royalarmouries.org\&sz=32)

Royal Armouries

+2



### Historical events must be decomposable

The 1415 campaign is a particularly good example.

Henry V's historical objective

Campaign in France and advance English dynastic and territorial interests

August 1415 — English landing

The expedition crosses the Channel and lands in Normandy, provided ships, troops, resources, and the operational decision remain available.

August–September — Siege of Harfleur

English forces undertake siege operations. French defenders react according to orders, resources, fortifications, and the actual circumstances.

October — English movement toward Calais

If the army remains in the relevant operational position, Henry may pursue the historical march. Its route and condition follow the actual situation.

French interception

French commanders organize their response. An encounter requires real forces with the capability and opportunity to engage.

25 October 1415 — Historical Battle of Agincourt

Default intended outcome: English victory, provided the historical causal pathway remains intact

This is based on the historical sequence in which the English siege of Harfleur preceded the march and battle at Agincourt.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://royalarmouries.org\&sz=32)

Royal Armouries

+1



Importantly, the French interception is not merely a switch that becomes active on 25 October. It results from French leaders using actual intelligence, resources, geography, and available military formations.

If Henry instead withdraws by sea, or the French army is unable to assemble, the encounter will not be manufactured.

### Illustrative event definition

```

event_id: hyw.1415.agincourt
record_type: HISTORICAL_EVENT_PLAN
status: PROPOSED

baseline:
  date: 1415-10-25
  location: Agincourt
  category: FIELD_BATTLE
  outcome: ENGLISH_VICTORY

historical_participants:
  english_command: person.henry_v_england
  french_command: historical_french_command_1415
  formations: REFERENCE_HISTORICAL_MUSTER_RECORDS

dependencies:
  - hyw.1415.english_invasion
  - hyw.1415.harfleur_campaign
  - hyw.1415.march_toward_calais
  - hyw.1415.french_interception

hard_requirements:
  - opposing_forces_exist
  - engagement_is_physically_possible
  - participants_are_available

supporting_conditions:
  - army_condition
  - terrain_and_weather
  - command_organization
  - current_equipment
  - supply_and_morale

execution:
  intact_path: HISTORICAL_BASELINE
  altered_path: IRGS_CORE_RESOLUTION
  arbitrary_history_correction: FORBIDDEN

divergence:
  allow_reschedule: IF_CAUSALLY_FEASIBLE
  allow_altered_outcome: true
  allow_replacement: true
  allow_prevention: true

consequences:
  apply_only_after_actual_resolution: true
  recheck_dependent_events: true
  enforce_resource_accounting: true

evidence:
  historical_sources: REQUIRED
  reconstructed_dependencies: MARK_AS_INFERENCE

```

The specific trigger predicates will be mapped to existing IRGS Core state records during implementation. This definition deliberately does not invent muster numbers or casualty totals.

## 8. Managing divergence without destroying the entire timeline

One changed event should not automatically invalidate every historical event that comes afterward.

Instead, the system must trace causal dependencies.

For example, if England loses at Agincourt:

| Subsequent historical development                    | Required response                                                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Henry V's personal reputation and political position | Reevaluate based on defeat, casualties, survival, and political reactions.                              |
| English military resources                           | Deduct actual losses and account for surviving forces.                                                  |
| French political divisions                           | Continue existing factional conflicts unless the battle changes their circumstances.                    |
| Burgundian relationships                             | Reevaluate diplomatic incentives rather than automatically preserving or cancelling the later alliance. |
| Treaty of Troyes                                     | Mark the historical plan at risk; its conditions may no longer develop.                                 |
| Black Death's earlier demographic consequences       | Unaffected by the 1415 battle.                                                                          |
| Scottish internal affairs                            | Continue from their own conditions, except where material connections to the war exist.                 |
| Unrelated commercial or social events                | Continue normally unless affected by actual consequences.                                               |

This creates localized divergence with causal propagation.

An alternate English defeat can change military politics in France without instantly rewriting economic conditions in distant settlements that have not yet been affected.

As consequences spread through trade, communications, diplomacy, population movements, and other mechanisms, additional events may become affected.

There should be no universal alternate-history percentage or automatic butterfly-effect roll.

### Historical equivalence and identity

The system also needs to distinguish between an altered event and a replacement.

| Situation                                                             | Event identity                                                |
| --------------------------------------------------------------------- | ------------------------------------------------------------- |
| Agincourt occurs on 25 October with the same armies, and England wins | Historical Agincourt                                          |
| Agincourt occurs with the same armies, but France wins                | Altered Agincourt                                             |
| Armies meet at Agincourt several days later                           | Rescheduled Agincourt, if the causal continuity is preserved  |
| Armies fight near a different town                                    | New battle linked to the historical encounter plan            |
| Henry V never invades                                                 | Historical Agincourt prevented                                |
| Another English king invades France years later                       | New campaign, potentially serving a similar strategic purpose |

A replacement should not inherit the original event's name or consequences without justification.

Once an event is prevented or superseded, it cannot later fire merely because the engine has reached its original scheduled date.

## 9. Autonomous historical actors and an intact baseline

This system requires a careful balance between historical planning and NPC autonomy.

Historical actors must still be agents with objectives, knowledge, capabilities, obligations, and finite resources.

Historical event plans guide their default intended behaviour; they do not override their ability to react.

For example, Henry V may have a historically grounded expedition plan. If his treasury, army, political authority, and diplomatic circumstances remain compatible with history, the English government undertakes the intended preparations.

If the English fleet has been destroyed through preceding simulation, the planned invasion cannot occur as recorded. Henry and his government may instead attempt to rebuild the fleet, negotiate, postpone, or pursue an alternative.

Likewise, a French commander does not know that history expects a defeat at Agincourt.

### Operational resolution policy

| Simulation context                                                                     | Resolution                                                                                                               |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Historical pathway intact; event outside meaningful simulation interference            | Reproduce the historical event and documented outcome, subject to available evidence and accounting constraints.         |
| Player participates, but produces no material changes to the event's causal conditions | Historical outcome can remain intact; the character's individual actions and consequences are still resolved normally.   |
| Player or autonomous actions materially alter the event                                | Resolve the affected operation through Core, without historical outcome protection.                                      |
| Resources cannot support the proposed action                                           | Prevent or modify execution even if the historical date has arrived.                                                     |
| Historical records do not specify a precise quantity                                   | Preserve uncertainty or apply an explicitly identified reconstruction assumption; never fabricate documentary precision. |

The intact-baseline procedure must not silently manufacture casualties, supplies, or military units. If the historical sources only support an approximate result, the campaign may reproduce that result while keeping unsupported quantities appropriately uncertain.

For focused, operational play, the event must follow the existing declaration, feasibility, execution, effect, exposure, and state-update procedures.

## 10. Information and player agency

The historical event schedule is an engine-level planning resource, not information automatically available to the characters.

A French knight in September 1415 cannot know the result of Agincourt in October.

A Burgundian court official in 1422 cannot know with certainty that Philip the Good will reconcile with Charles VII in 1435.

A merchant in 1337 cannot know the future extent of the Black Death.

Even if the human player knows those events from history, the simulated character only possesses information acquired through legitimate experience, observation, education, messages, rumours, and other knowledge mechanisms.

The campaign can allow players to use their outside historical knowledge to make decisions, but cannot automatically grant their characters information, capabilities, or contacts they do not possess.

The event scheduler must also preserve the distinction between a historical actor's intention and an action actually taken. Player characters cannot be assigned future speech, decisions, purchases, travel, or other voluntary actions merely because a historical event plan calls for participation.

## 11. Updated campaign initialization

Each of the ten Hundred Years’ War entries should now load two separate historical datasets.

| Dataset                      | Contents                                                                | Treatment                                       |
| ---------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------- |
| Historical Past Snapshot     | Everything historically established up to the selected cutoff           | Initialize as actual campaign history and state |
| Historical Future Event Plan | Events intended to occur after the cutoff through the baseline end date | Load as conditional future event plans          |

### Example: Campaign beginning in 1415

```

campaign_id: hundred_years_war
entry_id: hyw.entry.1415

initialization:
  historical_date: 1415-08-14
  research_edition: hyw.research.v0.2

past:
  source: HISTORICAL_STATE_DATABASE
  cutoff: 1415-08-14
  status: ESTABLISHED
  reconstruct_actual_state: true

future:
  source: HISTORICAL_EVENT_LIBRARY
  historical_baseline_end: 1453-10-19
  status: CONDITIONAL
  include_events_after_cutoff: true
  default_course: FOLLOW_HISTORY
  divergence_policy: CAUSAL_RECONCILIATION

runtime:
  authority: IRGS_CORE
  historicity_override: false
  autonomous_world: true
  resource_continuity: required
  future_knowledge_leakage: forbidden
  extend_beyond_historical_end: allowed

```

The `FOLLOW_HISTORY` setting means the intended historical progression continues while its prerequisites remain satisfied.

It does not mean event plans supersede Core's physical feasibility, autonomous decisions, resource accounting, or the actual consequences of player actions.

The timeline's date range is also not a hard simulation boundary. A 1337 campaign may reach 1453 with the war already concluded, still ongoing, or replaced by a different geopolitical situation. It may continue into 1454 and beyond.

## 12. Revised acceptance and stress tests

| Test                      | Required result                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Baseline fidelity         | A campaign without meaningful divergence reproduces the documented principal historical chronology and outcomes.              |
| 1389 entry                | All pre-entry historical events are already established; no prior war events replay.                                          |
| 1337 early peace          | An alternative settlement may prevent the Caroline War or supersede the later Leulinghem truce.                               |
| Agincourt untouched       | The battle occurs on 25 October 1415 with its historical outcome when the entire relevant pathway remains intact.             |
| Agincourt altered         | A material tactical or operational change permits a different outcome without historical correction.                          |
| Agincourt avoided         | Without a feasible encounter, no artificial battle or casualties are created.                                                 |
| Event rescheduling        | Delaying an invasion shifts dependent events only when their circumstances still support them.                                |
| Succession divergence     | Early death or survival of a ruler changes dependent offices, relationships, and event plans.                                 |
| Unrelated chronology      | An English defeat does not automatically cancel unrelated events elsewhere.                                                   |
| Autonomous intervention   | NPCs react to changed conditions without needing player direction.                                                            |
| Information separation    | Characters do not acquire knowledge of scheduled historical outcomes from the engine.                                         |
| Temporal consistency      | A replacement event cannot occur before its necessary people, technology, and institutions exist.                             |
| Accounting                | A historical event cannot introduce unsupported resources or count the same losses twice.                                     |
| Multiple scale simulation | Switching between individual, army, and national simulation does not reset or duplicate scheduled events.                     |
| Campaign independence     | Two campaigns beginning in 1337 can develop completely different futures while sharing the same historical reference edition. |
| No retroactivity          | A campaign beginning in 1435 does not inherit divergent outcomes from a separate campaign that began in 1337.                 |

### CMRR reconciliation with HSDB v0.1

| Earlier design element                                | Revised disposition                                                                      |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Historical starting-state reconstruction              | Retained. Still necessary for each entry point.                                          |
| Historical future used solely as reference            | Replaced. Future history now provides conditional event plans.                           |
| Future historical events excluded from initialization | Revised. Excluded from actual state, but included in the prospective event schedule.     |
| No predetermined events after initialization          | Rejected. The default historical chronology is now explicitly intended.                  |
| Autonomous actor simulation                           | Retained. Actor autonomy determines responses to changed circumstances.                  |
| Historical event outcomes                             | Reconciled. Default to recorded outcomes while historical causal pathways remain intact. |
| Divergent event outcomes                              | Expanded. Support rescheduling, alteration, substitution, prevention, and supersession.  |
| Historical research provenance                        | Retained and expanded. Trigger conditions and causal inferences also require provenance. |
| Nation strength and faction difficulty                | Retained as derived views. Reevaluate when history diverges.                             |
| Campaign independence and nonretroactivity            | Retained. Later research and other campaign histories do not overwrite active campaigns. |

### Remaining calibration work

Before adoption, the system needs to establish how it detects material divergence without either overreacting to minor differences or ignoring changes that would make an event impossible.

It also needs verified historical event dependencies. Historians often know what happened better than they know precisely why it happened, so the framework must distinguish documented causes from plausible reconstructions.

The baseline-reproduction policy will need tests across the entire 1337–1453 period, followed by stress tests involving alternate successions, military defeats, early peace, economic crises, epidemics, and localized interventions.

Design status: Proposed and internally specified; not yet integrated, calibrated, or playtested against the actual IRGS Core 3.3 code or rules.

## 13. Resulting historical campaign model

This establishes a reusable system with three distinct historical functions:

Historical Reconstruction establishes the actual world at the selected entry point.

Historical Event Planning supplies the intended historical future, including dated events, actors, causal requirements, expected outcomes, and subsequent developments.

Causal Divergence Reconciliation determines which events remain on schedule, which shift, which occur differently, and which must be replaced or prevented.

The important distinction is that starting in 1389 means inheriting the history that actually occurred, whereas reaching 1389 through a campaign begun in 1337 means inheriting the history that the campaign has actually produced.

That should be the governing rule for every historical IRGS campaign, regardless of whether it covers the Hundred Years’ War, ancient Rome, or a modern historical period.