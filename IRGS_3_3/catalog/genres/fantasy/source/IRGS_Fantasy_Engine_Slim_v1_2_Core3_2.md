# IRGS — Core Fantasy World Engine
## Slim Genre Edition v1.2 — Linked to Core v3.2

**Document ID:** IRGS-FANTASY-SLIM-1.2  
**Date:** 14 October 2026  
**Parent:** IRGS Integrated Core Engine v3.2  
**Receiving contract:** IRGS-BIND-FANTASY-3.2  
**Shared content:** IRGS Shared Content Library v1.0  
**Fantasy content:** [IRGS Fantasy Content Library v2.0](FantasyLibrary/IRGS_Fantasy_Content_Library_v2_0_Candidate.md), linked through SCL v1.0; source-native FL v1.0 data and proposed extensions retain their status  
**Principal source:** IRGS Core Fantasy World Engine v1.0  
**Development predecessor:** Fantasy Slim Genre Edition v1.1; its v1.0 development history remains provenance  
**Status:** Complete linked Fantasy workshop edition, resubmitted for use with the current parent; campaign adoption and new-clarification acceptance remain separately scoped  
**Validation:** Fresh link, preservation, content and bounded reference checks in the accompanying report; numerical calibration and live playtesting remain outstanding  
**Method:** Compare → Merge → Reconcile → Resubmit  
**Migration:** None authorized or applied

**Load:** [Core 3.2](Core/IRGS_Core_Engine_v3_2.md) → this Fantasy engine → selected setting → campaign profile → actual state.

**Content:** [SCL 1.0 guide](Core/IRGS_Shared_Content_Library_v1_0.md), [normative registry](Core/IRGS_Shared_Content_Registry_v1_0.json), [Fantasy content map](IRGS_Fantasy_Content_Map_v1_2_Core3_2.csv).

**Binding:** [Fantasy 1.2 / Core 3.2 contract](IRGS_Fantasy_Binding_v1_2_Core3_2.json), using the parent's existing IRGS-BIND-FANTASY-3.2 provider contract.

**Version distinction:** Fantasy engine **1.2**, Core **3.2**, SCL catalogue **1.0**, Fantasy content library **2.0**, and immutable content-record revisions such as **@0.2** are different version axes. None is silently converted into another.

This is a complete engine edition. The package contains the current parent and catalogue directly; prior engine editions, historical snapshots and extraction patches are not active dependencies.

---

# PART I — PURPOSE AND AUTHORITY

<a id="fantasy-1"></a>
## 1. Purpose

The Fantasy World Engine extends IRGS Core with the mechanics necessary to simulate fantasy capabilities, environments, creatures and supernatural phenomena.

It supports grounded, heroic, high, mythic and other fantasy genres without requiring a specific setting, class system, cosmology or degree of supernatural power.

Applicable campaigns may emphasize:

- Adventuring and exploration.
- Ordinary life and careers.
- Creature hunting or coexistence.
- Warfare and military service.
- Magic, religion and supernatural investigation.
- Settlement and civilization development.
- Trade, crafting and institutions.
- Generational continuity.
- Peace, prosperity and long-term stability.

None is a compulsory campaign direction.

The engine does not require a sequence of increasingly powerful enemies, recurring catastrophes or predetermined heroic destiny.

<a id="fantasy-2"></a>
## 2. Architecture

**Shared IRGS Core → Fantasy Genre Engine → Setting/Theme Module → Campaign Profile → Campaign State**

Core Content is a companion reference catalogue rather than an additional simulation engine.

### 2.1 Shared Core responsibilities

Core v3.2 owns:

- Action declaration, feasibility and uncertainty.
- Time and commitments.
- Actors and authoritative conditions.
- Information and knowledge.
- Stock, inventory and resource transfers.
- Equipment identity, physical condition and components.
- Projects, labor and production.
- Sites, networks and services.
- Institutions, governments and organizations.
- Population, families and life continuity.
- Logistics, medicine, ecology and ordinary exposure.
- General military and civilization systems.
- Competition administration.
- Content inheritance, identity and instantiation.
- Persistent world state and event history.

### 2.2 Fantasy responsibilities

Fantasy retains:

1. Selected character capability and creation profiles.
2. Fantasy-specific technique access and progression calibration.
3. Tactical reach, engagement and equipment handling.
4. Fantasy weapon Threat and Armor Defeat.
5. Fantasy armor and shield numerical protection.
6. Local material stress and protective equipment failure.
7. Fantasy injury grading and selected recovery parameters.
8. Fantasy creature Scale and natural-weapon interpretation.
9. Extraordinary physiology and materials.
10. Supernatural paradigms, access and costs.
11. Magical Magnitude, Scope, Range and Duration.
12. Magical Complexity and Power Units.
13. Supernatural effects, resistance and counterplay.
14. Magical healing, creation, summoning and other exceptions.
15. Consequences of supernatural capability for world simulation.
16. Fantasy-specific campaign configuration.

These are specialized implementations of Core interfaces, not additional generic state owners.

<a id="fantasy-3"></a>
## 3. Rules authority

Apply:

1. Current explicit user instruction or correction.
2. Established campaign rule or documented override.
3. Relevant adopted Fantasy rule within its scope.
4. Adopted Core v3.2 rule.
5. Scoped provisional ruling where no applicable adopted rule exists.

A selected setting exception may alter an inherited procedure only through an explicit bounded override.

Publication does not automatically adopt rules into existing campaigns.

<a id="fantasy-4"></a>
## 4. Design status

The following distinctions apply throughout:

**Core-established:** Inherited from the confirmed Core v3.2 workshop baseline.

**Fantasy source:** Preserved from Fantasy Engine v1.0 or its source library.

**Proposed clarification:** New reconciliation wording that requires explicit review.

**Profile-dependent:** Requires an actual selected character, creature, setting or technology profile.

**Uncalibrated:** A working numerical abstraction without demonstrated empirical realism or balance.

**Verified:** A specified check that has actually been executed and recorded.

**Playtested:** A mechanic exercised through actual interactive simulation with recorded outcomes.

Structural consistency must not be represented as numerical calibration or live playtesting.

---

# PART II — CORE v3.2 DEPENDENCIES

<a id="fantasy-5"></a>
## 5. Shared provider contract

Use the exact provider groups published in [the current parent binding](Core/IRGS_Engine_Bindings_v3_2.json). All links below point to actual Core 3.2 section anchors.

| Required function | Core 3.2 providers |
|---|---|
| Agency, action feasibility and selected resolution | [§4](Core/IRGS_Core_Engine_v3_2.md#core-4), [§5](Core/IRGS_Core_Engine_v3_2.md#core-5), [§6](Core/IRGS_Core_Engine_v3_2.md#core-6), [§7](Core/IRGS_Core_Engine_v3_2.md#core-7), [§8](Core/IRGS_Core_Engine_v3_2.md#core-8), [§9](Core/IRGS_Core_Engine_v3_2.md#core-9), [§90](Core/IRGS_Core_Engine_v3_2.md#core-90) |
| Time, events, commitments and scale continuity | [§10](Core/IRGS_Core_Engine_v3_2.md#core-10), [§11](Core/IRGS_Core_Engine_v3_2.md#core-11), [§12](Core/IRGS_Core_Engine_v3_2.md#core-12), [§47](Core/IRGS_Core_Engine_v3_2.md#core-47), [§62](Core/IRGS_Core_Engine_v3_2.md#core-62), [§85](Core/IRGS_Core_Engine_v3_2.md#core-85), [§90](Core/IRGS_Core_Engine_v3_2.md#core-90), [§91](Core/IRGS_Core_Engine_v3_2.md#core-91), [§96](Core/IRGS_Core_Engine_v3_2.md#core-96) |
| Actor capability, physiology and conditions | [§14](Core/IRGS_Core_Engine_v3_2.md#core-14), [§15](Core/IRGS_Core_Engine_v3_2.md#core-15), [§16](Core/IRGS_Core_Engine_v3_2.md#core-16), [§17](Core/IRGS_Core_Engine_v3_2.md#core-17), [§18](Core/IRGS_Core_Engine_v3_2.md#core-18), [§19](Core/IRGS_Core_Engine_v3_2.md#core-19), [§64](Core/IRGS_Core_Engine_v3_2.md#core-64), [§68](Core/IRGS_Core_Engine_v3_2.md#core-68), [§69](Core/IRGS_Core_Engine_v3_2.md#core-69), [§70](Core/IRGS_Core_Engine_v3_2.md#core-70), [§71](Core/IRGS_Core_Engine_v3_2.md#core-71), [§106](Core/IRGS_Core_Engine_v3_2.md#core-106), [§118](Core/IRGS_Core_Engine_v3_2.md#core-118), [§122](Core/IRGS_Core_Engine_v3_2.md#core-122) |
| Inventory, resources, claims and transactions | [§12](Core/IRGS_Core_Engine_v3_2.md#core-12), [§20](Core/IRGS_Core_Engine_v3_2.md#core-20), [§22](Core/IRGS_Core_Engine_v3_2.md#core-22), [§24](Core/IRGS_Core_Engine_v3_2.md#core-24), [§35](Core/IRGS_Core_Engine_v3_2.md#core-35), [§36](Core/IRGS_Core_Engine_v3_2.md#core-36), [§37](Core/IRGS_Core_Engine_v3_2.md#core-37), [§38](Core/IRGS_Core_Engine_v3_2.md#core-38), [§105](Core/IRGS_Core_Engine_v3_2.md#core-105), [§109](Core/IRGS_Core_Engine_v3_2.md#core-109), [§114](Core/IRGS_Core_Engine_v3_2.md#core-114) |
| Equipment, components and physical dependencies | [§21](Core/IRGS_Core_Engine_v3_2.md#core-21), [§23](Core/IRGS_Core_Engine_v3_2.md#core-23), [§48](Core/IRGS_Core_Engine_v3_2.md#core-48), [§49](Core/IRGS_Core_Engine_v3_2.md#core-49), [§53](Core/IRGS_Core_Engine_v3_2.md#core-53), [§54](Core/IRGS_Core_Engine_v3_2.md#core-54), [§55](Core/IRGS_Core_Engine_v3_2.md#core-55), [§56](Core/IRGS_Core_Engine_v3_2.md#core-56), [§57](Core/IRGS_Core_Engine_v3_2.md#core-57), [§58](Core/IRGS_Core_Engine_v3_2.md#core-58), [§101](Core/IRGS_Core_Engine_v3_2.md#core-101) |
| Work, production, services and acceptance | [§23](Core/IRGS_Core_Engine_v3_2.md#core-23), [§41](Core/IRGS_Core_Engine_v3_2.md#core-41), [§43](Core/IRGS_Core_Engine_v3_2.md#core-43), [§71](Core/IRGS_Core_Engine_v3_2.md#core-71), [§72](Core/IRGS_Core_Engine_v3_2.md#core-72), [§73](Core/IRGS_Core_Engine_v3_2.md#core-73), [§101](Core/IRGS_Core_Engine_v3_2.md#core-101), [§102](Core/IRGS_Core_Engine_v3_2.md#core-102), [§103](Core/IRGS_Core_Engine_v3_2.md#core-103), [§104](Core/IRGS_Core_Engine_v3_2.md#core-104), [§107](Core/IRGS_Core_Engine_v3_2.md#core-107), [§108](Core/IRGS_Core_Engine_v3_2.md#core-108), [§110](Core/IRGS_Core_Engine_v3_2.md#core-110), [§119](Core/IRGS_Core_Engine_v3_2.md#core-119), [§121](Core/IRGS_Core_Engine_v3_2.md#core-121) |
| Observation, search and intelligence | [§2](Core/IRGS_Core_Engine_v3_2.md#core-2), [§30](Core/IRGS_Core_Engine_v3_2.md#core-30), [§60](Core/IRGS_Core_Engine_v3_2.md#core-60), [§61](Core/IRGS_Core_Engine_v3_2.md#core-61), [§79](Core/IRGS_Core_Engine_v3_2.md#core-79), [§85](Core/IRGS_Core_Engine_v3_2.md#core-85), [§86](Core/IRGS_Core_Engine_v3_2.md#core-86), [§115](Core/IRGS_Core_Engine_v3_2.md#core-115), [§120](Core/IRGS_Core_Engine_v3_2.md#core-120) |
| Institutions, lives, households and succession | [§25](Core/IRGS_Core_Engine_v3_2.md#core-25), [§26](Core/IRGS_Core_Engine_v3_2.md#core-26), [§27](Core/IRGS_Core_Engine_v3_2.md#core-27), [§28](Core/IRGS_Core_Engine_v3_2.md#core-28), [§29](Core/IRGS_Core_Engine_v3_2.md#core-29), [§31](Core/IRGS_Core_Engine_v3_2.md#core-31), [§32](Core/IRGS_Core_Engine_v3_2.md#core-32), [§33](Core/IRGS_Core_Engine_v3_2.md#core-33), [§34](Core/IRGS_Core_Engine_v3_2.md#core-34), [§38](Core/IRGS_Core_Engine_v3_2.md#core-38), [§39](Core/IRGS_Core_Engine_v3_2.md#core-39), [§40](Core/IRGS_Core_Engine_v3_2.md#core-40), [§44](Core/IRGS_Core_Engine_v3_2.md#core-44), [§45](Core/IRGS_Core_Engine_v3_2.md#core-45), [§46](Core/IRGS_Core_Engine_v3_2.md#core-46), [§65](Core/IRGS_Core_Engine_v3_2.md#core-65), [§66](Core/IRGS_Core_Engine_v3_2.md#core-66), [§67](Core/IRGS_Core_Engine_v3_2.md#core-67), [§68](Core/IRGS_Core_Engine_v3_2.md#core-68), [§69](Core/IRGS_Core_Engine_v3_2.md#core-69), [§76](Core/IRGS_Core_Engine_v3_2.md#core-76), [§107](Core/IRGS_Core_Engine_v3_2.md#core-107), [§113](Core/IRGS_Core_Engine_v3_2.md#core-113), [§117](Core/IRGS_Core_Engine_v3_2.md#core-117), [§122](Core/IRGS_Core_Engine_v3_2.md#core-122) |
| Content identities, variants, overrides and modules | [§88](Core/IRGS_Core_Engine_v3_2.md#core-88), [§97](Core/IRGS_Core_Engine_v3_2.md#core-97), [§98](Core/IRGS_Core_Engine_v3_2.md#core-98), [§99](Core/IRGS_Core_Engine_v3_2.md#core-99), [§111](Core/IRGS_Core_Engine_v3_2.md#core-111), [§112](Core/IRGS_Core_Engine_v3_2.md#core-112) |
| Competitions and tournaments | [§6](Core/IRGS_Core_Engine_v3_2.md#core-6), [§47](Core/IRGS_Core_Engine_v3_2.md#core-47), [§61](Core/IRGS_Core_Engine_v3_2.md#core-61), [§91](Core/IRGS_Core_Engine_v3_2.md#core-91), [§99](Core/IRGS_Core_Engine_v3_2.md#core-99), [§112](Core/IRGS_Core_Engine_v3_2.md#core-112), [§123](Core/IRGS_Core_Engine_v3_2.md#core-123) |

The eleven Core workflows remain GOV, ECO, INV, MAR, CIV, MED, WILD, INTEL, URBAN, LIFE and COMP. Fantasy uses them when a relevant activity requires them. Competition administration belongs to COMP; a sport, tournament discipline or magical contest supplies its own compatible performance model.

Use only the selected procedures necessary to resolve the current activity. The engine does not reproduce a second Core event loop. Shared mechanics use the current parent directly; a source paragraph once labelled “Core” does not restore an older shared algorithm.

<a id="fantasy-6"></a>
## 6. Fantasy extension records

Fantasy maintains specialized parameters and references such as:

`FANTASY.CharacterProfile`  
`FANTASY.AttackMode`  
`FANTASY.ProtectionProfile`  
`FANTASY.InjuryAdapter`  
`FANTASY.CreatureProfile`  
`FANTASY.SupernaturalParadigm`  
`FANTASY.Technique`  
`FANTASY.ActiveEffect`  
`FANTASY.ExtraordinaryMaterial`  
`FANTASY.PrevalenceProfile`

These refer to existing actors, assets, sites, conditions and events.

An ActiveEffect may impose a condition or modify an asset, but it does not create a competing inventory or medical ledger.

### 6.1 Owner-qualified extension fields

| Fantasy data | Authoritative record and rule |
|---|---|
| Identity, attributes, skills, bodily injury, fatigue and internal supernatural capacity | K-ACTOR; one selected representation per cause |
| Consumable reagents, ammunition, material and actual created output | K-STOCK; named holders and locations |
| Weapon, armor, shield, focus, rune substrate and constructed embodiment | K-ASSET; actual components and condition |
| Ritual, enchantment, alchemy, study or repair work | K-WORK; real labor, dependencies and completed quantities |
| Casting, interruption, upkeep and expiry times | K-TIME and the existing event journal |
| Divination, telepathy, detection and reports | K-INFO; source, observation and receipt boundaries |
| Orders, obligations, licenses, temple/guild authority | K-ORG and the relevant domain |
| Magical routes, transport and operating service links | K-NET; actual capacity and supply |
| Creature populations and household/cohort membership | K-POP; no new individuals from a display view |

An ActiveEffect records Effect ID/version, source event, source/controller, actual targets, selected technique/model, start, next causal trigger, sustain requirement, expiry/termination, owner-field changes already committed and visibility. It references authoritative costs and conditions; it does not hold another spendable copy.

A constructed actor may refer to a physical embodiment in K-ASSET. A damaged sensor is one component fault; cognition, knowledge and any separately supported biological condition remain their own facts. Describing the same fault in an actor sheet does not apply it twice.

<a id="fantasy-7"></a>
## 7. Runtime interaction

Fantasy actions follow:

**Declaration → Feasibility → Execution/Uncertainty → Effect → Exposure/Reaction → State Update → Player Control**

Fantasy supplies a specialized effect calculation when necessary.

Core owns the resulting actual state change.

### 7.1 Runtime handoff

1. Read actual current time, actor, target, position, means, conditions, standing commitments and knowledge.
2. Bind the selected Fantasy profile and exact content selector. Check only parameters material to this operation.
3. Submit the declared objective, method, interval/stopping condition, authorized expenditure, feasible effect, distinct stages and Mixed branch to [Core §5](Core/IRGS_Core_Engine_v3_2.md#core-5).
4. Use [Core §6](Core/IRGS_Core_Engine_v3_2.md#core-6) only when the campaign selects that adapter. An established campaign dice system continues within its declared scope. Routine qualified work normally needs no roll.
5. Apply this engine's relevant contact, protection, injury, creature or supernatural procedure. Activation, delivery and effect are distinct causal questions; they do not require separate rolls for the same uncertainty.
6. Schedule and commit actual changes through [Core §11](Core/IRGS_Core_Engine_v3_2.md#core-11) and [§91](Core/IRGS_Core_Engine_v3_2.md#core-91). Preserve event identity, retained outcomes, partial time/work and simultaneous pre-event state.
7. Present observations and received information through [Core §90](Core/IRGS_Core_Engine_v3_2.md#core-90), then return control at the next meaningful voluntary decision.

An effect-ending event stops its defined future output. It does not erase an existing wound, spent sacrifice, received message or completed work. One upkeep interval, spell emission, injury or stock transfer is charged once despite multiple subscribers or scale changes.

The extension manifest records reads/writes, triggers, intervals, cost timing, target bounds, persistence and termination. Undefined rates block dependent numerical operations while supported independent and qualitative actions continue.

Examples:

- A sword strike uses Fantasy protection and injury grading, then changes a Core-owned condition.
- A spell creates an item through a declared magical effect, then creates the actual item/stock through Core.
- A summoned entity enters the actor and location systems through a supported event.
- Teleportation changes actual location without creating another copy of the traveler.
- Magical healing changes an existing injury state rather than adding a parallel healing meter.

---

# PART III — CHARACTER CAPABILITY

<a id="fantasy-8"></a>
## 8. Attribute-agnostic parent

IRGS Core does not require a universal attribute set.

Fantasy may use a selected attribute model, including the following optional default.

This profile originated in Fantasy v1.0 and remains a valid Fantasy selection. It is not imposed on every campaign.

<a id="fantasy-9"></a>
## 9. Optional ten-attribute Fantasy profile

| Attribute | Scope |
|---|---|
| Strength | Force, leverage, lifting |
| Constitution | Health, endurance, physiological resilience |
| Agility | Whole-body movement and gross coordination |
| Dexterity | Fine manipulation and precision |
| Nimbleness | Reactions, footwork and flexibility |
| Cunning | Improvisation, deception and tactical trickery |
| Intelligence | Knowledge and formal analysis |
| Wisdom | Perception, judgment and intuition |
| Charisma | Presence, persuasion and leadership |
| Resolve | Willpower, discipline and coercion resistance |

A campaign may replace this entire profile.

### 9.1 Attribute scale

| Score | Interpretation |
|---:|---|
| 0–3 | Severely limited |
| 4–7 | Below ordinary |
| 8–11 | Ordinary |
| 12–15 | Strong |
| 16–19 | Exceptional |
| 20–23 | Extraordinary |
| 24–27 | Superhuman |
| 28–30 | Extreme natural/supernatural boundary |
| 31+ | Explicit extraordinary cause required |

### 9.2 Independent capacity modifier

Where the selected model uses this scale:

| Score | Modifier |
|---:|---:|
| 4–7 | −5 |
| 8–11 | 0 |
| 12–15 | +5 |
| 16–19 | +10 |
| 20–23 | +15 |
| 24–27 | +20 |
| 28–30 | +25 |

Only apply this modifier when the capacity makes an independent causal difference to execution.

Physical impossibility remains impossible regardless of modifier.

Do not add a Strength modifier when its relevant effect is already represented by Threat, load capacity, mass, or a separately applied physical advantage.

Scores outside the table require their selected profile's interpretation.

<a id="fantasy-10"></a>
## 10. Character-creation power profiles

For the optional ten-attribute implementation, all ten attributes initially begin at 8.

| Profile | Additional points | Creation cap |
|---|---:|---:|
| Grounded | 40 | 16 |
| Heroic | 60 | 17 |
| High Fantasy | 80 | 18 |

Ancestry changes apply after base allocation only where the selected setting permits them.

These are design benchmarks, not universal Core creation rules.

Aethelgard selects High Fantasy and its own class/character overrides.

<a id="fantasy-11"></a>
## 11. Character origins and specialization

Keep distinct:

**Ancestry:** physiology and inherited capabilities.

**Culture:** learned social context.

**Background:** personal history and acquired experience.

**Profession/Class:** sustained specialization.

No ancestry automatically establishes a particular personality, morality, profession or learned cultural skill.

### 11.1 Background package

Source Fantasy default:

**2 Familiar disciplines + 2 Trained disciplines + one contextual language, tool, contact or resource benefit.**

### 11.2 Profession package

Source Fantasy default:

**2 Trained disciplines + 1 Experienced discipline + suitable tools/access.**

The ordinary starting discipline ceiling is Experienced 3 unless the campaign establishes a justified exception.

Overlapping packages must specify whether training is redundant or demonstrates a higher rating; they do not automatically grant duplicate numerical bonuses.

### 11.3 Narrow specialization

A relevant narrow specialization may grant:

**+5 circumstance**

Normally one specialization applies to a check.

It requires an actual supported connection to the task.

<a id="fantasy-12"></a>
## 12. Technique access

| Competence rating | Fantasy access ceiling |
|---:|---|
| 0 | Intuitive/simple |
| 1 | Rehearsed fundamentals |
| 2 | Standard professional |
| 3 | Advanced combinations |
| 4 | Expert techniques |
| 5 | Exceptional mastery |

A technique one rating beyond current competence may be attempted at **−10** if it is physically feasible and the actor plausibly understands the method.

Unknown techniques cannot be produced merely through favorable dice.

Supernatural techniques may impose additional prerequisites.

<a id="fantasy-13"></a>
## 13. Training schedule

The Fantasy v1.0 optional schedule is retained.

**1 Training Unit ≈ 20 focused hours.**

| Advancement | TU | Focused hours |
|---|---:|---:|
| 0→1 | 2 | 40 |
| 1→2 | 8 | 160 |
| 2→3 | 20 | 400 |
| 3→4 | 60 | 1,200 |
| 4→5 | 160 | 3,200 |

Cumulative benchmark: approximately **5,000 focused hours**, plus demonstrated competence.

Actual learning requires suitable practice, instruction, feedback and evidence.

Hours alone never award a competence level.

Routine work is not automatically equivalent to focused development.

<a id="fantasy-14"></a>
## 14. Attribute development

For the optional ten-attribute implementation:

| Current score | Minimum focused development before +1 review |
|---:|---:|
| 0–11 | 200 hours |
| 12–15 | 400 hours |
| 16–19 | 800 hours |
| 20+ | Extraordinary or campaign-specific mechanism |

A completed time threshold permits review, not automatic improvement.

The character must demonstrate a real increase in capability.

This schedule is a provisional game abstraction.

Other character models may supply their own development procedures.

<a id="fantasy-15"></a>
## 15. Noncombat progression

Progress includes:

`Competence | Physical capacity | Career | Wealth | Property | Authority | Relationships | Reputation | Institutions | Magic | Infrastructure | Legacy`

Core LIFE, ECO, GOV and CIV own the ordinary world processes.

Fantasy retains the effects of extraordinary longevity, power, ancestry or supernatural institutions.

Source v1.0 also supplies two optional descriptive conventions: relationship dimensions such as Trust, Respect, Affection, Loyalty, Fear, Obligation and Resentment may use −3 to +3; availability may use 0 Common, 1 Uncommon, 2 Scarce, 3 Rare, 4 Exceptional, 5 Unique/restricted. These are optional views of Core-owned relationships and supply/access facts, not extra universal meters. Availability is separate from price; neither rating creates a relationship change or stock.

---

# PART IV — FANTASY TACTICAL ADAPTER

<a id="fantasy-16"></a>
## 16. Tactical time and commitments

Use Core v3.2 §§10, 47 and 48 for time, action commitments and reactions.

The Fantasy source profile expects one primary commitment within a meaningful tactical exchange, compatible incidental activity, and ordinary defense when physically available.

A substantial emergency response may consume the next available primary commitment.

The same future commitment cannot be borrowed repeatedly.

No arbitrary fixed number of seconds is required for every Fantasy exchange; actual elapsed time follows the actions and selected profile.

<a id="fantasy-17"></a>
## 17. Engagement states

Fantasy describes relevant engagement as:

**Grappled → Contact → Melee → Reach → Disengaged**

These are relational positions, not absolute distances.

Actual weapon dimensions, body size, obstacles and control determine which modes are possible.

<a id="fantasy-18"></a>
## 18. Movement

| Action | Meaning |
|---|---|
| Shift | Local adjustment |
| Advance | Meaningful positional transition |
| Rush | Faster approach with applicable exposure/precision changes |
| Sprint | Maximum purposeful movement |
| Withdraw | Departure that may be opposed where feasible |

Movement never creates an attack by implication.

Leaving an enemy's reach does not automatically generate a free strike.

<a id="fantasy-19"></a>
## 19. Terrain effects

Fantasy reference modifiers:

| Terrain | Modifier |
|---|---:|
| Mild constraint | −5 |
| Poor footing | −10 |
| Severe constraint | −20 |
| Prohibitive geometry | Infeasible |

Do not stack several labels for the same physical limitation.

<a id="fantasy-20"></a>
## 20. Reach control

A prepared actor controlling an approach with superior effective reach imposes:

**−10 to the opponent's relevant closing attempt.**

Success establishes the intended feasible closer engagement.

Mixed produces partial closure or a declared exposure.

Failure leaves the actor outside the intended engagement.

A prepared intercepting attack requires an available reserved commitment or an explicitly selected ability.

Reach is not a source of unlimited free actions.

<a id="fantasy-21"></a>
## 21. Multiple attackers

Only attackers exerting credible simultaneous pressure count.

| Simultaneous attackers | Modifier to relevant attacker |
|---:|---:|
| 1 | 0 |
| 2 | +5 |
| 3 | +10 |
| 4+ | +15 |

Exclude attackers who:

- are out of range;
- are physically blocked;
- cannot act;
- cannot contribute to the defender's current defensive problem.

The modifier represents divided defense, not mere nearby population.

<a id="fantasy-22"></a>
## 22. Defensive choices

### Ordinary guard

Incorporated into the selected active-opposition procedure.

### Shield guard

Applies the shield's declared directional, readiness and handling benefit.

### Emergency evasion

May impose an additional **−10 to −20** against the attacker where supported.

Consumes the applicable emergency or next primary commitment.

### Reserved defense

Requires actual advance reservation and a feasible trigger.

### No automatic counterattack

A failed enemy attack does not automatically authorize a damaging response.

<a id="fantasy-23"></a>
## 23. Maneuvers and prone conditions

Standard maneuvers:

`Shove | Trip | Disarm | Grapple | Escape | Bind | Feint | Tackle`

Use Core contested objectives with actual geometry and means.

A maneuver's success accomplishes its declared feasible objective; it does not automatically provide additional attacks.

Typical prone effects:

- −10 to unsuitable melee execution.
- +10 to an appropriately positioned attacker.
- Real movement and handling restrictions.

Each applies only where causally relevant.

---

# PART V — FANTASY WEAPON MODEL

<a id="fantasy-24"></a>
## 24. Selected physical-effect chain

The Fantasy physical adapter uses:

**Position → Execution → Contact → Protection → Residual Threat → Injury/Material Effect**

Exposure and autonomous reaction then follow the Core action sequence.

Do not combine this chain with a separate incompatible historical, modern or science-fiction damage-reduction model without an explicit conversion.

<a id="fantasy-25"></a>
## 25. Weapon modes

A weapon may support multiple actual attack modes.

Minimum mode record:

`Item ID | Mode selector | Reach | Hands | Damage channel | Threat | Armor Defeat | Handling | Requirements | Traits | Secondary transfer`

For example, a sword cut and thrust are different attack modes attached to one object.

They are not separate inventory items.

<a id="fantasy-26"></a>
## 26. Threat

| Threat | Effect scale |
|---:|---|
| 0 | Incidental |
| 1 | Light |
| 2 | Standard lethal |
| 3 | Heavy |
| 4 | Severe |
| 5 | Extreme human-scale |
| 6+ | Extraordinary/monstrous |

Threat is an abstract effect parameter.

Native Threat **0** means **Incidental**. It is not by itself proof of absent contact or a terminated channel. An unarmored unarmed contact may still have a separately justified Force/anatomical consequence under its selected effect profile. Conversely, a channel actually stopped by protection remains stopped even with a large placement or Force modifier. Keep numerical rating and causal transmission/termination separate.

It is not automatically measured as energy, wound size, or probability of death.

<a id="fantasy-27"></a>
## 27. Armor Defeat

Armor Defeat describes interaction with a relevant protective construction.

It does not alter attack accuracy.

Penetrating, cutting, crushing and blunt modes may interact differently with the same armor.

<a id="fantasy-28"></a>
## 28. Mundane effect channels

Fantasy v1.0 defines:

`Cut | Pierce | Blunt | Crush | Burn | Corrosive`

The channel must correspond to the actual mechanism.

A weapon label alone cannot impose arbitrary channels.

<a id="fantasy-29"></a>
## 29. Source melee reference profiles

| Weapon/mode | Reach | Threat | Defeat |
|---|---:|---:|---:|
| Unarmed strike | 0–1 | 0 | — |
| Club | 1–2 | 1 | — |
| Dagger thrust | 0–1 | 1 | 1 |
| Sword cut | 1–2 | 2 | 1 |
| Sword thrust | 1–2 | 2 | 2 |
| Longsword cut | 1–3 | 2 | 1 |
| Longsword thrust | 1–3 | 2 | 2 |
| Hand axe | 1–2 | 2 | 2 |
| Battle axe | 2–3 | 3 | 2 |
| Mace | 1–2 | 2 | — |
| Warhammer blunt face | 1–2 | 3 | — |
| Warhammer pick | 1–2 | 3 | 2 |
| Spear thrust | 2–3 | 2 | 2 |
| Heavy polearm | 2–4 | 3 | Mode-specific |
| Great weapon | 2–3 | 3 | Mode-specific |

The compatible Fantasy Content Library v1.0 provides separate exact source selectors and proposed additional modes for staff, short blades, great blades, pikes and poleaxes.

Where a source row combines multiple modes, use the selected exact mode, not a merged favorable profile.

A source entry's numeric status remains unchanged through reference binding.

<a id="fantasy-30"></a>
## 30. Weapon traits

| Trait | Fantasy interpretation |
|---|---|
| Brace | +1 distinct Force against an actual suitable charge where prepared |
| Concealable | Physical concealment advantage when supported by clothing/search |
| Defensive | +5 to suitable weapon-control contests, not every defense |
| Hook | +5 to feasible relevant pulling/tripping/disarming |
| Long | −10 or infeasibility inside a mode's minimum distance |
| Two-Handed | Normal mode requires two usable hands |
| Versatile | Different supported handling modes |
| Mounted | Suitable mounted configuration, not automatic damage |
| Sunder +N | Adds only to material/shield stress |
| Reload N | Requires N applicable primary reloading commitments |

Traits never create unpriced attacks, abilities or resources.

The source's Concussive descriptor requires an explicit secondary-transfer mechanism before it can inflict additional bodily effects through otherwise stopped protection.

<a id="fantasy-31"></a>
## 31. Ranged weapons

Retained reference:

| Weapon | Threat | Defeat | Reload |
|---|---:|---:|---:|
| Thrown knife | 1 | 1 | — |
| Javelin | 2 | 1 | — |
| Sling | 1 | — | — |
| Shortbow | 1 | 1 | 0 |
| Warbow | 2 | 1–2 | 0 |
| Light crossbow | 2 | 2 | 1 |
| Heavy crossbow | 3 | 3 | 2 |

The selected attack mode and projectile define the actual effect.

A projectile cannot be used twice because it appears in different display views.

Use Core stock/asset records for Ready, Carried, Fired, Recoverable, Recovered, Damaged and Lost. Recoverable is a possibility, not a credited item. Recovery requires actual search/access, elapsed work and a usable surviving projectile. Reload 0 grants no extra primary commitment; Reload N charges its N actual commitments once. Aiming preparation is lost when materially disrupted.

### Range bands

**Close → Effective → Long → Extreme**

Long: −10.

Extreme: −20.

Beyond feasible range: unavailable.

Exact physical distances require a selected weapon profile.

### Aiming

One primary commitment may provide:

**+10 to the next maintained precision attack.**

Subsequent aim commitments do not stack without an explicit compatible technique.

### Called shots

| Target | Modifier |
|---|---:|
| Large region | 0 |
| Limb | −10 |
| Hand/foot | −15 |
| Small armor gap/vital location | −20 or worse |

An inaccessible gap cannot be targeted through a high roll.

### Capacity-gated weapons

Bows, heavy crossbows and similar weapons may require minimum strength, draw capacity or mechanical assistance.

Missing mechanical capability blocks normal operation; skill cannot substitute for it.

---

# PART VI — ARMOR, PROTECTION AND SHIELDS

<a id="fantasy-32"></a>
## 32. Protection profile

Each applicable protection layer has:

`Construction | Material | Coverage | Condition | Cut Resistance | Pierce Resistance | Impact Protection | Other explicit channels | Burden`

Material, quality, construction, coverage and condition remain distinct.

The Core asset system owns the actual armor object and physical state.

Fantasy owns the numerical interpretation.

<a id="fantasy-33"></a>
## 33. Reference armor

| Armor construction | Cut | Pierce | Impact |
|---|---:|---:|---:|
| Ordinary clothing | 0 | 0 | 0 |
| Padded textile | 1 | 0 | 1 |
| Soft leather | 1 | 1 | 1 |
| Reinforced leather | 2 | 1 | 1 |
| Mail | 3 | 2 | 1 |
| Brigandine/coat of plates | 4 | 3 | 2 |
| Plate | 5 | 4 | 3 |

The Fantasy library also supports coherent integrated constructions such as mail with an appropriate padded foundation.

**Do not sum entire Resistance values from multiple complete armor profiles.**

A combination requires an approved integrated construction model.

<a id="fantasy-34"></a>
## 34. Zero Resistance

If relevant Resistance is **0** and the selected adapter defines this as absent protection:

**Retain full primary Threat. Do not run the reduction table.**

Unknown Resistance is not zero.

This rule prevents armorlessness from accidentally reducing damage.

<a id="fantasy-35"></a>
## 35. Cut/Pierce protection

For relevant Resistance ≥1:

**Difference = Armor Defeat − Resistance**

| Difference | Interpretation | Threat adjustment |
|---:|---|---:|
| ≤−2 | Stopped | Residual 0; terminate primary channel |
| −1 | Strong attenuation | −3 |
| 0 | Partial | −2 |
| +1 or +2 | Penetration | −1 |
| ≥+3 | Overmatch | 0 |

Floor residual Threat at zero.

### Channel termination

A Stopped primary attack cannot be revived through:

- placement;
- vulnerability;
- skill margin;
- a favorable roll;
- a later unrelated modifier.

A separate transfer channel requires its own declared mechanism and effect profile.

**Proposed clarification:** Where attenuation reduces an ordinary attack's only transmitted damaging channel to zero, do not create a new injury from later placement or Force alone. Require a genuinely separate supported transfer mechanism if one exists.

This follows the Core causal termination principle and does not change the source's explicit Stopped branch. It is retained reconciliation wording, not proof that every native numerical zero means absence. The selected adapter states whether attenuation eliminated the transmitted primary channel; record that result explicitly. Unknown transfer is not silently declared present or absent.

<a id="fantasy-36"></a>
## 36. Blunt protection

Apply Impact Protection:

| Impact rating | Threat reduction |
|---:|---:|
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3+ | 2, plus supported exceptional interaction |

Blunt injury does not require penetration through a cutting/piercing layer.

The actual transmission must still be physically supported.

<a id="fantasy-37"></a>
## 37. Local armor stress

Fantasy v1.0 uses:

**Material Stress = max(0, Threat + Force + Sunder − Relevant Resistance)**

Only an actual supported material contact generates stress.

| Stress | Result |
|---:|---|
| 0 | No automatic material damage |
| 1 | One local Stress Mark |
| 2 | Immediate Local Damage |
| 3+ | Local Breach |

Two local Stress Marks on the same component establish Local Damage.

### Local condition

**Intact:** normal relevant Resistance.

**Local Damage:** −1 relevant Resistance.

**Local Breach:** −2 relevant Resistance.

Floor effective Resistance at zero.

Subsequent repeated damage must be assessed against the actual already-damaged component, without duplicating the initial damage transition.

Further destruction, detached sections, lost coverage or total item failure require a supported component-failure rule.

Repair targets actual damaged components.

<a id="fantasy-38"></a>
## 38. Shield defense

| Shield | Defensive circumstance |
|---|---:|
| Buckler | −5 relevant melee |
| Small | −10 |
| Medium | −10 with broader coverage |
| Large | −15 frontal relevant attacks |
| Deployed pavise | Up to −20 appropriate ranged attacks |

Orientation, coverage, readied state and available hands control applicability.

A shield benefit does not prove every missed attack hit the shield.

<a id="fantasy-39"></a>
## 39. Shield Structure

| Shield construction | Structure |
|---|---:|
| Buckler | 2 |
| Light wooden | 2 |
| Reinforced wooden | 3 |
| Heater/kite | 3 |
| Metal-faced heavy | 3 |
| Pavise | 4 |

Materials can modify Structure through an explicit profile.

<a id="fantasy-40"></a>
## 40. Shield stress

**Shield Stress = Threat + Force + Sunder − Structure**

| Stress | Consequence |
|---:|---|
| ≤0 | No automatic damage |
| 1 | One Stress Mark |
| 2 | Degrade one Condition state |
| 3+ | Degrade two states or supported structural failure |

Two Stress Marks degrade one Condition state.

Only confirmed shield contact applies shield stress.

A shield strike and subsequent bodily effect cannot charge the same transferred harm twice.

The precise relationship between shield interception and subsequent attack contact requires the selected shield-interaction profile; it must not be improvised after seeing a favorable damage result.

---

# PART VII — FANTASY INJURY AND CARE

<a id="fantasy-41"></a>
## 41. Injury Grade

The source Fantasy formula is:

**Injury Grade = Residual Threat + Force + Placement + Vulnerability − Resilience**

Use it only after protection establishes a real transmitted bodily effect.

The result is an injury severity guide, not a pool of hit points.

Required inputs include actual anatomy/location and a declared transmission result, in addition to the formula's numbers. Do not implement the gate as Residual Threat ≤0 for every mode: that would silently erase the source's Incidental Threat 0. Do not implement it as “every contact transmits” either: that would revive a stopped attack. A genuinely separate secondary channel has its own declared transfer and protection.

A stopped effect cannot create an injury through this formula.

<a id="fantasy-42"></a>
## 42. Force

| Circumstance | Modifier |
|---|---:|
| Ordinary | 0 |
| Distinct major momentum/charge | +1 |
| Extreme separate force/mass | +2 |
| Extraordinary | +3 or greater |

Do not add a Force modifier merely because a weapon is already heavy or a creature already large if that characteristic was incorporated into the attack profile.

<a id="fantasy-43"></a>
## 43. Placement

| Contact result | Modifier |
|---|---:|
| Ordinary successful damaging contact | 0 |
| Mixed reduced-quality damaging contact | −1 |
| Justified exceptional precision | +1 |

Precision needs both a feasible method and an actual supported execution result.

<a id="fantasy-44"></a>
## 44. Vulnerability

| Location | Typical modifier |
|---|---:|
| Limb | 0 |
| Abdomen | 0 |
| Chest | +1 for relevant severe penetration/crush |
| Neck | +1 |
| Head | +1 |

A location modifier represents relevant actual anatomy.

It cannot create damage without a transmitted effect.

<a id="fantasy-45"></a>
## 45. Resilience

The original Fantasy formula includes Resilience but does not universally define its numerical derivation.

This edition therefore treats Resilience as a **profile-required parameter** whenever it changes an outcome.

The selected physiology model must specify:

`Resilience value/derivation | Applicable harm channels | Conditions | Bounds | Interaction with other resistance`

Constitution, creature Scale, armor, injury mitigation and Resilience must not count the same defense repeatedly.

**Proposed testing fixture only:** Ordinary human Resilience 0, where no other physiological resilience offset is selected.

The fixture is not an adopted universal rule.

<a id="fantasy-46"></a>
## 46. Severity grades

| Grade | Interpretation |
|---:|---|
| ≤0 | Superficial/no structural injury |
| 1 | Minor |
| 2 | Moderate |
| 3 | Serious |
| 4 | Critical |
| 5+ | Mortal potential |

Mortal potential is not automatic death.

Actual affected anatomy, ongoing physiological processes and intervention determine prognosis.

<a id="fantasy-47"></a>
## 47. Functional consequences

| Injury | Default affected-function modifier |
|---|---:|
| Minor | −5 |
| Moderate | −10 |
| Serious | −20 |
| Critical | Specific capability assessment |
| Mortal | Specific survival/capability assessment |

Use the most severe applicable injury for the same function unless different injuries produce independent physical constraints.

This does not make repeated wounds harmless.

A second injury may worsen damaged structures, create new limitations, increase bleeding, or change survival prospects through the Core repeated-harm procedure.

<a id="fantasy-48"></a>
## 48. Humanoid hit location

Where the applicable anatomy and geometry permit:

| d20 | Location |
|---:|---|
| 1–2 | Head |
| 3 | Neck |
| 4–8 | Chest |
| 9–11 | Abdomen |
| 12–13 | Right arm |
| 14–15 | Left arm |
| 16–18 | Right leg |
| 19–20 | Left leg |

Known contact geometry overrides an irrelevant random location.

Nonhumanoid creatures use their own body-plan tables.

<a id="fantasy-49"></a>
## 49. Bleeding

| Level | State |
|---:|---|
| 0 | None |
| 1 | Minor |
| 2 | Significant |
| 3 | Severe |
| 4 | Catastrophic |

Source review guidance:

- Level 1: no automatic rapid deterioration.
- Level 2: major exertion or approximately 30 minutes untreated.
- Level 3: approximately 10 minutes or major exertion.
- Level 4: immediate minute/exchange-scale emergency.

These are provisional review intervals rather than calibrated survival timers.

Actual bleeding changes the existing physiological condition state.

<a id="fantasy-50"></a>
## 50. Shock

| Level | State |
|---:|---|
| 0 | Stable |
| 1 | Stressed |
| 2 | Compromised |
| 3 | Severe |
| 4 | Collapse risk |

Shock requires an identifiable physical or supernatural cause.

<a id="fantasy-51"></a>
## 51. Care and recovery

The shared MED domain owns care work and actual conditions.

Fantasy retains selected reference healing parameters.

### Treatment objectives

`Assessment | Bleeding control | Stabilization | Cleaning | Immobilization | Closure | Extraction | Pain management | Infection treatment | Surgery | Rehabilitation`

One intervention does not automatically complete all objectives.

Routine trained first aid with adequate means ordinarily succeeds under safe conditions without rolling.

### Recovery phases

**Acute → Stabilized → Healing → Rehabilitation → Resolved / Lasting Impairment**

### Optional ordinary-human recovery scale

| Severity | Review | Broad uncomplicated recovery |
|---|---|---|
| Minor | Daily | 1–7 days |
| Moderate | Several days | 1–4 weeks |
| Serious | Weekly | 1–4 months |
| Critical | Daily until stable, then weekly | 2–12+ months |
| Mortal | Case-specific | Case-specific |

These intervals are not guaranteed recovery deadlines.

Actual injury, health, care, rest, infection, nutrition and supernatural effects matter.

---

# PART VIII — FATIGUE, NEEDS AND TRAVEL

<a id="fantasy-52"></a>
## 52. Fantasy fatigue profile

The optional source profile is:

| Level | State | Modifier |
|---:|---|---:|
| 0 | Rested | 0 |
| 1 | Taxed | −5 |
| 2 | Tired | −10 |
| 3 | Exhausted | −20 |
| 4 | Depleted | −30 |

This is a selected representation of actual fatigue, not a second condition ledger.

Use this schedule as one selected profile of [Core §18](Core/IRGS_Core_Engine_v3_2.md#core-18). Do not also charge the parent's optional fatigue schedule for the same exertion. Preserve fractional Load Points and processed intervals across narration, rest checks, save/load and scale changes; split reviews of unchanged activity do not create extra Load or new independent work checks.

### Human exertion reference

One Load Point per:

- 2 hours strenuous work.
- 8 hours ordinary active duty.
- One exchange of maximum exceptional exertion.

Each two accumulated Load Points increase Fatigue by one step and consume the two points.

### Rest

Two hours protected low-demand rest remove one unconverted Load Point.

Suitable full sleep ordinarily reduces Fatigue by two steps and clears ordinary remaining Load Points.

Disrupted sleep may reduce Fatigue by one step.

Other conditions may restrict recovery.

<a id="fantasy-53"></a>
## 53. Deprivation

Possible tracks:

`Hydration | Nutrition | Sleep | Temperature protection`

| State | Consequence |
|---|---|
| Supplied | Normal |
| Short | Deficit without automatic modifier |
| Deprived | −5 affected function |
| Severe | −10; ordinary fatigue recovery blocked |
| Critical | −20; deterioration evaluation |

Species/environment profiles determine transition rates.

A single physical deficit must not be charged twice through overlapping deprivation/fatigue labels. At Deprived, recovery is constrained by the actual shortage even before the Severe block applies. Meeting a need ends or reduces that cause according to its profile; it does not instantly erase accumulated injury or fatigue.

<a id="fantasy-54"></a>
## 54. Carrying capacity

Optional humanoid source formula:

**Sustainable Carry (kg) = 10 + 1.5 × Strength**

Only applicable with a compatible Strength score and species profile.

**Load Ratio = Carried Mass / Sustainable Carry**

| Ratio | State | Mobility effect |
|---:|---|---:|
| 0–25% | Light | 0 |
| >25–50% | Working | 0 |
| >50–75% | Heavy | −5 |
| >75–100% | Overloaded | −10 |
| >100% | Unsustainable | Feasibility-dependent |

Mass is not the sole constraint. Volume, balance, containers, equipment fit and occupied hands can matter independently.

<a id="fantasy-55"></a>
## 55. Travel pace

Reference healthy humanoid travel on suitable routes:

| Pace | Approximate distance/day |
|---|---:|
| Cautious | 20 km |
| Normal | 30 km |
| Fast | 40 km |

Healthy riding animals may sustain approximately **35–50 km/day** where actual species, terrain, load, fodder and care support it.

These are provisional travel profiles. Normal pace uses the ordinary activity Load already incurred. Fast/Forced pace and Heavy/Overloaded load are alternative states within each respective cause; do not charge both members of a pair for the same interval. Distinct pace and load contributions require actual supported activity.

### Fatigue adjustments

Fast pace: +1 additional Load Point/day.

Forced pace: +3 additional Load Points/day.

Heavy load: +1 additional Load Point/day.

Overloaded travel: +2 additional Load Points/day.

The next suitable sleep after Forced Travel restores at most one Fatigue step under this source profile.

At Tired or worse, further forced travel requires a feasible exertion/condition assessment.

<a id="fantasy-56"></a>
## 56. Fantasy navigation and exploration

Ordinary travel, routing and sites inherit Core.

Fantasy may add setting-specific:

- supernatural concealment;
- enchanted roads;
- portals;
- dangerous wilderness creatures;
- impossible geography;
- magical navigation;
- cursed environments.

Every exceptional mechanism requires a declared setting rule.

A dungeon remains a persistent site with occupants, structure, ecology, evidence, resources and history.

There is no automatic loot or encounter respawn.

---

# PART IX — CREATURES AND ANATOMY

<a id="fantasy-57"></a>
## 57. Creature construction

A fantasy creature profile records:

`Species | Scale | Anatomy | Physiology | Movement | Senses | Cognition | Needs | Natural weapons | Protection | Behavior | Ecology | Extraordinary traits`

Use Core biological/ecological ownership for ordinary processes.

Fantasy supplies specialized Scale, attack, protection and exceptional features.

<a id="fantasy-58"></a>
## 58. Scale

| Scale | Category |
|---:|---|
| 0 | Tiny |
| 1 | Small |
| 2 | Human |
| 3 | Large |
| 4 | Huge |
| 5 | Colossal |
| 6 | Titanic |

For relevant mass-dependent contests, the source proposes:

**+5 per meaningful Scale advantage**, normally capped at +20.

Scale may affect reach, lifting, grappling, movement, structures, charges and trampling.

No general Scale modifier automatically applies to every action.

<a id="fantasy-59"></a>
## 59. Natural weapons

A natural weapon's ordinary profile already incorporates its species' usual anatomy, mass and musculature.

Do not automatically add extra Scale Force.

Additional Force requires a distinct supported event such as a substantial charge, fall, trample or supernatural enlargement.

Fantasy Content Library natural-weapon families include:

`Bite | Claw | Gore | Slam | Tail | Stomp | Constrict | Quill/Spine | Breath | Venom Delivery`

A bite that delivers venom may cause a physical injury and a separate toxic exposure.

Each has its own effect mechanism.

<a id="fantasy-60"></a>
## 60. Body plans

The Fantasy library retains:

| Source ID | Body plan |
|---|---|
| BODY-001 | Humanoid |
| BODY-002 | Quadruped |
| BODY-003 | Avian/Winged |
| BODY-004 | Serpentine |
| BODY-005 | Arthropod/Exoskeletal |
| BODY-006 | Amorphous |
| BODY-007 | Constructed body |

Each supplies different meaningful anatomical regions and failure consequences.

For example, wing injury may affect flight while leaving unrelated structures intact.

Constructed beings may have component dependencies but are not automatically immune to particular effects.

Actual composition and metaphysics determine vulnerability.

<a id="fantasy-61"></a>
## 61. Creature autonomy

Creatures act from real motives and capabilities.

They may hunt, defend territory, avoid danger, flee, protect offspring, migrate, cooperate or negotiate.

A creature labeled “monster” does not thereby become suicidal, permanently hostile or narratively obligated to fight.

Ecological populations persist beyond encounters.

Removing one named creature from a cohort does not add another individual.

---

# PART X — SUPERNATURAL FOUNDATION

<a id="fantasy-62"></a>
## 62. Optional supernatural activation

Magic and other supernatural abilities are not mandatory.

An enabled paradigm defines:

**Source → Access → Capacity → Method → Cost → Limits → Effect → Persistence → Detection → Counterplay**

No universal mana resource is imposed.

A paradigm must state how its power is generated, stored, borrowed or supplied.

<a id="fantasy-63"></a>
## 63. Paradigm record

`Paradigm ID | Source | Access | Capacity | Method | Knowledge | Resource/cost | Recovery | Limits | Effect channels | Duration | Detection | Countermeasures | Failure | World consequences`

A setting can enable one paradigm, several or none.

Paradigms need not share resources or numerical scales unless an explicit compatible model connects them.

<a id="fantasy-64"></a>
## 64. Technique record

`Technique ID/version | Paradigm | Discipline/required tier | Magnitude | Scope | Range | Duration | Method | Special factors | Complexity | Cost | Target | Resistance | Channel | Effect | Secondary consequences | Termination`

A technique profile must distinguish activation from delivery, target resistance and actual effect.

A successful cast is not automatic successful penetration.

<a id="fantasy-65"></a>
## 65. Magnitude

| Rating | Interpretation |
|---:|---|
| 0 | Trivial |
| 1 | Minor |
| 2 | Standard |
| 3 | Major |
| 4 | Great |
| 5 | Legendary |
| 6 | Mythic |

Magnitude represents selected supernatural capability scale.

It is not automatically interchangeable with bodily injury grade or physical force.

<a id="fantasy-66"></a>
## 66. Scope

| Rating | Reach of effect |
|---:|---|
| 0 | Self/object |
| 1 | Individual |
| 2 | Small group/room |
| 3 | Building/large group |
| 4 | Battlefield/district |
| 5 | Settlement |
| 6 | Region or greater |

<a id="fantasy-67"></a>
## 67. Range

| Rating | Range |
|---:|---|
| 0 | Self/touch |
| 1 | Close |
| 2 | Sight/local |
| 3 | Long/local area |
| 4 | Remote known location |
| 5 | Extreme/planar |

Remote capability does not create knowledge of unknown destinations.

<a id="fantasy-68"></a>
## 68. Duration

| Rating | Duration |
|---:|---|
| 0 | Instant |
| 1 | Exchange/minutes |
| 2 | Scene |
| 3 | Hours |
| 4 | Day |
| 5 | Persistent |
| 6 | Permanent |

Persistent and permanent effects still require actual supporting mechanisms and termination definitions.

---

# PART XI — MAGIC CONSTRUCTION AND COSTS

<a id="fantasy-69"></a>
## 69. Complexity

Source formula:

**Complexity = Magnitude + Scope + Range + Duration + Special Factors**

Examples of special factors:

- Complex transformation: +1.
- Matter creation: +1–2.
- Remote divination: +1.
- Planar interaction: +2.
- Bypassing ordinary resistance: +2.

These factors apply only when they represent a real additional capability rather than one already included in the technique's profile.

<a id="fantasy-70"></a>
## 70. Complexity difficulty

| Complexity | Casting modifier |
|---:|---:|
| 0–3 | +10 |
| 4–6 | 0 |
| 7–9 | −10 |
| 10–12 | −20 |
| 13–15 | −30 |
| 16+ | Normally ritual/legendary |

Routine qualified magical activity may succeed without rolling where safe, properly resourced and genuinely routine.

The complexity schedule is a working design model, not empirically calibrated.

<a id="fantasy-71"></a>
## 71. Power Units

Retain the source formula:

**PU = max(1, Magnitude + max(0, Scope−1) + max(0, Range−1) + ceil(Duration/2))**

PU is an abstract design currency.

The paradigm determines its actual resource interpretation.

A cost derived in PU is not automatically an energy quantity or something held in inventory.

The selected paradigm must define actual expenditure, storage, regeneration and resource constraints.

---

# PART XII — SUPERNATURAL EFFECTS AND RESISTANCE

<a id="fantasy-72"></a>
## 72. Harmful supernatural effects

A harmful technique records:

`Damage Mode | Threat | Protection Channel | Defeat/Potency | Secondary conditions`

The source benchmark is:

**Maximum ordinary direct-damage Threat = Magnitude**, for Magnitude 0–6.

A technique may choose less direct harm.

Extraordinary damage beyond that benchmark requires a specific effect profile.

<a id="fantasy-73"></a>
## 73. Focused Potency

For a compatible focused direct effect:

**Default Potency = Magnitude**

where a Potency rating is meaningful to the chosen protection channel.

An area spell may trade localized penetration for Scope.

A specialized magical lance may possess a specific penetration trait.

Neither change is automatic.

<a id="fantasy-74"></a>
## 74. Supernatural protection channels

### Physical

`Cut | Pierce | Impact`

### Environmental/energy

`Heat | Cold | Corrosive | Toxic | Electrical`

### Supernatural

`Arcane | Mental | Spiritual | Divine/Profane`

Each protective effect lists the channels it actually covers.

A steel breastplate does not provide automatic mental or spiritual protection.

The Cut/Pierce armor reduction table is **not automatically** a universal rule for every supernatural channel.

The selected channel adapter must establish the actual reduction, block or counter-effect procedure.

<a id="fantasy-75"></a>
## 75. Zero supernatural protection

Where channel protection 0 is defined as absence:

- no reduction applies through that protection;
- the valid primary effect continues.

Unknown protection is not treated as zero.

This preserves the original source's zero-protection principle while requiring compatible nonphysical channel interpretation.

<a id="fantasy-76"></a>
## 76. Supernatural Mixed outcomes

For direct harmful magic, the source default is:

**Threat −1**, minimum 0.

Alternative declared Mixed branches may include:

- reduced Scope;
- reduced Duration;
- additional authorized cost;
- worsened position;
- exposure to an existing threat.

A Mixed outcome cannot silently spend new voluntary resources or select a new PC action.

<a id="fantasy-77"></a>
## 77. Resistance types

A technique selects:

| Resistance type | Interpretation |
|---|---|
| None | No target resistance beyond actual feasibility/protection |
| Capacity | Independent relevant target capacity |
| Discipline | Active opposition with a relevant defense technique |
| Protection | Delivery resolved against actual channel protection |
| Combined | Explicit independent mechanisms, counted once |

### Capacity resistance

Under a compatible ten-attribute profile, reverse the target's independent attribute modifier against the caster.

Example:

Target Resolve 18 has independent modifier +10.

Caster receives −10 on the relevant coercive interaction.

### Discipline resistance

Use the selected active-opposition procedure.

Spell dueling, trained mental defense and spirit negotiation are not necessarily the same discipline.

### Protection resistance

Resolve successful delivery through the defined channel.

A Mental Ward must supply actual Mental protection semantics.

Its name alone does not establish complete effect immunity.

<a id="fantasy-78"></a>
## 78. Area effects

One area casting constitutes one activation event.

Use one casting execution result.

Apply relevant target-specific resistance, geometry and protection separately.

Independent target reactions remain possible where the selected model supports them.

A homogeneous group may use cohort resolution without losing actual total casualties or effects.

The casting cost is not duplicated for each target unless the technique explicitly defines a target-dependent cost.

For the retained native d100 area profile, preserve one raw activation result and apply target-specific independent resistance/circumstances to that same emission. Do not resample its existence or add another full casting cost per target. A target lacking a complete required protection adapter remains unresolved for that channel; other supported targets can still resolve. Genuinely independent target responses follow their selected reaction procedure.

---

# PART XIII — SUPERNATURAL APPLICATIONS

<a id="fantasy-79"></a>
## 79. Mental effects

Distinguish:

`Communication | Emotional Pressure | Suggestion | Illusion | Compulsion | Domination | Memory Alteration`

Every power defines its actual effect and agency boundary.

It may cause an involuntary perception, restriction, or specifically enabled compelled action.

It does not authorize inventing the PC's sincere thoughts, voluntary agreement, motives or dialogue.

A coerced action must be represented as coercion, not voluntary choice.

<a id="fantasy-80"></a>
## 80. Healing

Source Magnitude benchmarks:

| Magnitude | Typical ceiling |
|---:|---|
| 1 | Pain control, basic stabilization, minor bleeding |
| 2 | Simple closure and appropriate Minor–Moderate repair |
| 3 | Serious tissue repair or difficult fracture |
| 4 | Critical restoration or substantial regeneration |
| 5 | Major tissue/limb regeneration if enabled |
| 6 | Possible death-state intervention if enabled |

The actual paradigm may prohibit some categories.

Healing changes specified existing conditions.

Stopping bleeding does not automatically close structural damage.

Regrowing tissue does not automatically restore spent magical resource value.

<a id="fantasy-81"></a>
## 81. Divination

Divination requires an actual information mechanism.

Possible functions include:

- supernatural detection;
- remote observation;
- memory access;
- symbolic information;
- location;
- probability assessment.

Successful divination produces only information accessible to that technique.

Mind reading does not reveal information never possessed by the target.

Remote visions do not automatically disclose true future certainty.

Information enters K-INFO with source, recipient and confidence.

<a id="fantasy-82"></a>
## 82. Summoning

Distinguish:

**Creation | Teleportation | Invitation | Manifestation | Binding**

A summoned autonomous entity retains its independent goals and knowledge unless a specific control mechanism establishes otherwise.

Arrival does not automatically grant control.

A spirit may refuse service despite successful contact.

A binding must define duration, constraints, cost, resistance and termination.

<a id="fantasy-83"></a>
## 83. Teleportation

A teleportation technique requires:

`Range | Destination knowledge | Mass/passenger limits | Preparation | Cost | Entry/exit conditions | Error | Detection | Counterplay`

Teleportation changes actual location.

It does not automatically transfer ownership, reveal hidden locations, replenish supplies, or eliminate local environmental hazards.

Large-scale availability requires explicit economic, military and political assessment.

<a id="fantasy-84"></a>
## 84. Matter creation

Creation requires:

`Material/product | Quantity | Quality | Source mechanism | Duration/stability | Cost | Frequency | Limits | Termination`

Created matter enters real stock and property systems.

Repeated creation requires repeated actual means and resources.

Temporary creations require consistent expiration consequences.

Permanent created quantities remain real quantities, with economic implications.

<a id="fantasy-85"></a>
## 85. Resurrection and death alteration

A resurrection paradigm defines:

`Eligible identity | Soul/continuity model | Time limit | Remains | Willingness/consent where applicable | Practitioner | Cost | Repeatability | Effects | Conditions | Institutional consequences`

Reanimation is not necessarily resurrection.

Returning biological function is not necessarily restoring the previous consciousness or soul.

Resurrection alters the permitted death-state facts.

It does not rewind unrelated deaths, transactions, marriages, inheritances, wars or other history.

A campaign must explicitly enable its chosen death exception.

<a id="fantasy-86"></a>
## 86. Enchantment

An enchantment requires:

`Base asset | Effect | Power source | Activation | Cost | Duration | Maintenance | Compatibility | Detection | Counterplay`

The base object remains real and vulnerable according to its physical state.

An enchanted item does not automatically recharge or remain functional after structural failure.

<a id="fantasy-87"></a>
## 87. Alchemy

Alchemy uses the inherited Core production/project system.

Its fantasy-specific record contains:

`Formula | Ingredients | Quantity | Purity | Tools | Process | Time | Batch | Stability | Dose | Shelf life | Supernatural effect if any`

A missing indispensable reagent cannot be replaced by rolling higher.

The formula must permit a substitution.

<a id="fantasy-88"></a>
## 88. Rituals

Rituals inherit the Core project/work system.

Fantasy supplies:

`Paradigm | Objective | Source | Participants | Roles | Site | Materials | Preparation | Power | Stages | Timing | Interruptions | Effect | Termination`

Completing preparatory work does not guarantee magical activation unless the selected technique provides for it.

Ritual failure follows actual supported causes, not an automatic explosion.

---

# PART XIV — PARADIGM LIBRARY

<a id="fantasy-89"></a>
## 89. Paradigm templates

The Fantasy library preserves:

| ID | Paradigm | Specialized mechanism |
|---|---|---|
| PAR-ARC | Arcane | Learned manipulation of a supernatural source |
| PAR-DIV | Divine | Granted capability or petition to divine agency |
| PAR-SPR | Spirit/Primal | Negotiation or relationship with autonomous spirits |
| PAR-PSI | Psionic | Mental/psychic capability |
| PAR-INT | Internal Energy/Ki | Internal supernatural capability and training |
| PAR-BLD | Blood/Sacrificial | Expenditure of blood, life or sacrificial value |
| PAR-RUN | Runic | Inscribed/prepared persistent mechanisms |
| PAR-ALC | Alchemical | Formulaic transformation with supernatural processes |
| PAR-NEC | Necromantic | Corpses, animation, death and metaphysical interactions |

These are reusable paradigms, not mandatory setting facts.

<a id="fantasy-90"></a>
## 90. Specific safeguards

### Divine

Distinguish granted power from petitionary intervention by an autonomous entity.

### Spirit

Successful contact does not create compulsory obedience.

### Psionic

Actual cognition and information access bound results.

### Internal Energy

Exceptional effects require explicit supernatural functions.

### Blood/Sacrifice

Physical healing does not automatically refund metaphysical value already sacrificed.

### Runic

Requires real substrate, preparation, work and source.

### Alchemy

Input materials and production remain finite.

### Necromancy

Distinguish corpse, biological life, consciousness, memory, identity and soul.

<a id="fantasy-91"></a>
## 91. Multiple paradigms

A setting may permit several supernatural paradigms.

Inter-paradigm compatibility must define, where consequential:

`Detection | Resistance | Dispel | Shared ward | Resource conversion | Interference | Source access | Persistence`

No universal assumption that one paradigm can counter another is imposed.

A spell can fail to interact with a spirit, divine effect or psionic power because its declared mechanism does not support that interaction.

---

# PART XV — EXTRAORDINARY MATERIALS

<a id="fantasy-92"></a>
## 92. Materials and construction

Mundane material definitions inherit Shared Content Library v1.0 and compatible source profiles.

Fantasy extraordinary materials remain genre/setting extensions.

<a id="fantasy-93"></a>
## 93. Extraordinary material templates

| Template | Possible specialty |
|---|---|
| XMAT-L | Reduced mass |
| XMAT-H | Exceptional hardness/toughness |
| XMAT-C | Supernatural conduction/storage |
| XMAT-I | Supernatural insulation/protection |
| XMAT-R | Regenerative/living material |

Every specific variant defines:

`Base material | Mass | Relevant protection/Defeat/Structure changes | Workability | Maintenance | Repair | Source | Cost | Rarity | Extraordinary effect`

Proposed source examples include:

- Reduced mass multiplier 0.5–0.75 for an appropriate lightweight material.
- Selected +1 Resistance, Defeat or Structure benefits for exceptional hard/tough materials.
- Supernatural channel behavior for conductors or insulators.
- Time/resource-dependent recovery for living materials.

These are possible template values, not automatic combined benefits.

Every actual improvement needs a physical or supernatural explanation and compatible acquisition/production constraints.

---

# PART XVI — FANTASY WORLD APPLICATIONS

<a id="fantasy-94"></a>
## 94. Supernatural prevalence

For each major capability, choose:

| Tier | Meaning |
|---:|---|
| 0 | Nonexistent |
| 1 | Legendary |
| 2 | Rare |
| 3 | Specialist |
| 4 | Common institutional |
| 5 | Ubiquitous |

Rate independently:

`Combat Magic | Healing | Divination | Enchantment | Communication | Teleportation | Conjuration | Summoning | Resurrection`

A world may have common healing but nearly impossible resurrection.

One generic “high magic” rating is insufficient.

<a id="fantasy-95"></a>
## 95. Social and institutional consequences

For capabilities rated 4 or 5, assess effects on:

**Economy | Warfare | Medicine | Law | Infrastructure | Daily Life**

Examples:

### Healing

Who can heal, at what scale, with what cost, and how does this affect conventional medicine?

### Teleportation

How do travel, supply, fortifications, borders and trade operate when distance can be bypassed under defined conditions?

### Conjuration

What happens to ordinary material production, prices and logistics?

### Resurrection

How are inheritance, succession, identity and legal death interpreted?

These are required questions, not compulsory results.

A setting may have strong limitations that preserve otherwise familiar institutions.

<a id="fantasy-96"></a>
## 96. Fantasy settlements

Settlements inherit Core sites, populations, production and services.

Fantasy-specific additions may include:

- Enchanted infrastructure.
- Wards.
- Supernatural healing institutions.
- Magical transport systems.
- Extraordinary agriculture.
- Nonhuman physiology/settlement requirements.
- Metaphysical hazards or obligations.

Each remains subject to actual inputs, maintenance and operating capacity.

<a id="fantasy-97"></a>
## 97. Fantasy warfare

Use Core military, logistical and institutional systems.

Fantasy units may include:

`Manpower | Training | Cohesion | Morale | Equipment | Supply | Mobility | Leadership | Magical assets | Condition`

Battlemages require actual:

`Personnel | Competence | Techniques | Power sources | Range | Scope | Protection | Recovery | Command relationships`

A battlemage is not an infinite artillery resource.

Summoned forces require declared autonomy, duration, logistics and applicable control.

<a id="fantasy-98"></a>
## 98. Fantasy life and legacy

Ordinary work, households, politics, property, relationships, illness, succession and generational development inherit LIFE and associated Core domains.

Fantasy-specific exceptions may include:

- Extraordinary lifespan.
- Magical inheritance.
- Bloodline abilities.
- Curses.
- Reincarnation.
- Resurrection.
- Metaphysical identity transfer.
- Supernatural obligations.

None is automatically enabled.

A later protagonist does not inherit the former protagonist's skills, memories or secret knowledge unless actual inheritance/transfer mechanisms establish that effect.

---

# PART XVII — FANTASY CAMPAIGN PROFILE

<a id="fantasy-99"></a>
## 99. Campaign Profile — FANTASY-CPF-1.2

A campaign pins:

### Rules and versions

`Core v3.2 | Fantasy v1.2 | Shared Content v1.0 | Fantasy Content version | Setting modules | Overrides`

Select resolution, character, physical effect, injury/Resilience, fatigue, load, learning, travel, supernatural cost and channel profiles before their dependent operations. Preserve unknown and not-applicable values. A blank receives neither another campaign's lore nor a favorable zero.

Each override records parent clause/profile, replacement, scope/targets, reason/authority, effective time, state conversion if any and acceptance case. Selecting this engine does not itself override an established campaign.

### Character

`Selected attributes | Creation profile | Ancestries | Culture/background/profession | Competence | Learning schedule | Specialization`

### Physical effects

`Combat adapter | Weapon modes | Armor/protection | Shields | Material stress | Injury | Resilience | Physiology | Death`

### Environment

`Needs | Fatigue | Load | Travel | Weather | Hazards | Species needs`

### Creature

`Body plans | Scale | Natural weapons | Behavior | Ecology | Extraordinary capabilities`

### Supernatural

`Enabled paradigms | Sources | Capacity | Costs | Techniques | Protection channels | Resistance | Recovery | Duration | Prevalence`

### World

`Economy | Institutions | Magic services | Warfare | Settlements | Technology | Geography | Calendar | Information`

### Continuity

`Actual starting state | Active actors | Time | Events | Resource owners | Persistence | Migration policy`

<a id="fantasy-100"></a>
## 100. Aethelgard binding

Aethelgard is a campaign/setting implementation, not the default Fantasy world.

Its existing selections include:

- Ten-attribute model.
- High Fantasy creation.
- +80 attribute points.
- Creation cap 18 before ancestry.
- Existing classes, levels, feats and spell libraries.
- Detailed life, property, relationship and political systems.

Established Aethelgard rules retain precedence within their documented scope.

No Aethelgard lore or campaign history is imported into other fantasy campaigns.

---

# PART XVIII — ACCEPTANCE AND TESTING

<a id="fantasy-101"></a>
## 101. Reference calculation checks

The accompanying reference suite reruns the following preserved formulas using controlled synthetic values.

They verify only the displayed arithmetic and selected guard behavior.

| Case | Inputs | Result |
|---|---|---|
| Dagger against unarmored target | Threat 1, Defeat 1, Resistance 0 | Residual Threat 1 |
| Dagger against plate Pierce 4 | Threat 1, Defeat 1 | Stopped; residual 0 |
| Sword cut against mail Cut 3 | Threat 2, Defeat 1 | Stopped; residual 0 |
| Sword thrust against Pierce Resistance 0 | Threat 2, Defeat 2 | Residual Threat 2 |
| Heavy crossbow against plate Pierce 4 | Threat 3, Defeat 3 | Strong attenuation; residual 0 |
| Warhammer face against Impact 3 | Threat 3, reduction 2 | Residual Threat 1 |

These results do not prove weapon balance, historical realism, injury lethality or complete repeated-impact behavior.

<a id="fantasy-102"></a>
## 102. Fantasy regression requirements

| ID | Required result |
|---|---|
| FSL-01 | Missing physical means cannot be overcome by a Master roll |
| FSL-02 | Ordinary trained tasks succeed without arbitrary rolls |
| FSL-03 | Sword cut and thrust remain separate modes of one object |
| FSL-04 | Armorless contact does not receive phantom protection |
| FSL-05 | Stopped primary channel remains stopped |
| FSL-06 | Secondary transfer requires actual separate mechanism |
| FSL-07 | Local armor stress does not damage unrelated armor components |
| FSL-08 | Sunder changes material stress, not bodily injury directly |
| FSL-09 | Shield guard without shield contact does not create shield wear |
| FSL-10 | Reach control does not create free attacks |
| FSL-11 | Multiple attackers count only when actually exerting pressure |
| FSL-12 | Physical creature Scale is not double-counted in natural Threat |
| FSL-13 | Repeat wounds can worsen actual harm |
| FSL-14 | Long travel preserves exhaustion and supplies |
| FSL-15 | A nonhumanoid wing injury changes supported flight capacity |
| FSL-16 | One area spell has one activation event |
| FSL-17 | Magical casting success is separate from target protection |
| FSL-18 | Mind magic respects the defined player-agency boundary |
| FSL-19 | Summoned autonomous entities retain agency |
| FSL-20 | Magical creation enters actual stock once |
| FSL-21 | Teleportation moves actual people/items rather than duplicating them |
| FSL-22 | Healing changes specific injury states |
| FSL-23 | Resurrection does not rewrite unrelated history |
| FSL-24 | Sacrifice/healing cannot generate unlimited power by accident |
| FSL-25 | Multiple paradigms do not automatically share countermeasures |
| FSL-26 | High-prevalence magic has traceable world consequences |
| FSL-27 | Settlement/campaign scale changes do not repeat resources or casualties |
| FSL-28 | Library aliases preserve exact attack-mode selectors |
| FSL-29 | Mundane fantasy works when all supernatural paradigms are disabled |
| FSL-30 | A campaign selecting another effect adapter does not stack it with Fantasy armor/injury arithmetic |

<a id="fantasy-103"></a>
## 103. Stress-test program

Execute:

- Routine, difficult and infeasible attempts.
- Low, moderate and extreme capacity.
- Armorless and fully protected contacts.
- Repeated armor and shield impacts.
- Physical and magical mixed effects.
- Multiple attackers and simultaneous engagements.
- Creature Scale extremes.
- Scarcity and unavailable material.
- Recovery, deterioration and repeated injury.
- Long-term travel and fatigue.
- Magical resource conservation.
- Powerful area spells and counterplay.
- Autonomous NPC and institutional reactions.
- Cross-scale travel/combat/settlement continuity.
- Save/load replay and event ordering.
- Campaign-profile and content-module conflicts.

Each execution should record:

`Initial state | Selection/version | Method | Feasibility | Costs | Result | Physical effect | State changes | Remaining quantities | Failure/violation | Correction`

The benchmark is mechanical reproducibility, not simply whether narrative examples appear plausible.

---

# PART XIX — CALIBRATION AND UNRESOLVED QUESTIONS

<a id="fantasy-104"></a>
## 104. Open numerical issues

| Area | Unresolved problem |
|---|---|
| Weapon Threat | Empirical and gameplay lethality |
| Armor Defeat | Interaction with actual construction and materials |
| Blunt transfer | Relationship between transmitted impact and tissue effect |
| Local stress | Durability and repeated-hit progression |
| Shield interception | Exact hit/contact/coverage procedure |
| Injury Grade | Trauma realism and severity thresholds |
| Resilience | Physiology-based derivation and applicability |
| Bleeding/shock | Quantitative deterioration and treatment |
| Fatigue/travel | Rates across species, terrain and workloads |
| Training | Advancement hours, quality of practice and learning evidence |
| Creature Scale | Mass, leverage and extraordinary physiology |
| Supernatural channel protection | Nonphysical resistance semantics |
| Magic Complexity | Effects of combined Scope/Range/Duration |
| Power Units | Resource cost and recovery consistency |
| Matter creation | Throughput and production-economy balance |
| Resurrection | Identity, repeatability and world consequences |
| Paradigm interaction | Detection, dispelling, warding and source compatibility |

The absence of these calibrated values must not be hidden by inventing universal numbers.

<a id="fantasy-105"></a>
## 105. Runtime completeness boundary

The engine is a complete linked specification of Fantasy-owned systems and Core v3.2 dependencies at the declared profile-selection boundary.

That does **not** mean every possible campaign configuration is numerically executable.

A configuration requiring a missing effect-channel adapter, physiology parameter or extraordinary process must supply one before resolving the dependent event.

A mundane Fantasy campaign may be operational with far fewer selected modules.

No missing profile is silently replaced by Aethelgard values or another campaign's rules.

---

# PART XX — CMRR RECONCILIATION

<a id="fantasy-106"></a>
## 106. Source-to-destination matrix

| Fantasy Engine v1.0 | Reconciliation | New destination |
|---|---|---|
| §§1–7 | Core generic rules inherited | Parts I–II; Core v3.2 |
| §8 | Fantasy technique access retained | §12 |
| §§9–13 | Core uncertainty, opposition, Mixed and margin inherited | Core v3.2 |
| §§14–18 | Character record generic; ten-attribute implementation retained | §§8–9 |
| §§19–23 | Creation and background/profession selections retained | §§10–11 |
| §§24–27 | Training and progression split | §§13–15 plus Core LIFE |
| §§28–30 | Generic time/priority inherited, selected exchange application retained | §16; Core |
| §§31–34 | Reach, terrain and movement retained | §§17–20 |
| §§35–36 | Optional Fantasy carry/load model retained | §54 |
| §§37–43 | Fantasy combat application retained | §§21–24 |
| §§44–54 | Weapon profiles and modes retained through adapter/library | §§25–31 |
| §§55–65 | Physical protection, wear and shields retained | §§32–40 |
| §§66–74 | Fantasy injury parameters retained; condition ownership inherited | §§41–50 |
| §§75–78 | General treatment inherited; Fantasy recovery benchmarks retained | §51; Core MED |
| §§79–82 | Fatigue, exertion and deprivation profile retained | §§52–53 |
| §§83–87 | Creature anatomy/Scale/behavior split | §§57–61; Core WILD |
| §§88–96 | Generic travel/sites inherited; Fantasy numerical applications retained | §§55–56; Core |
| §§97–100 | Generic item, quality and projects inherited | Core K-ASSET/K-WORK |
| §§101–107 | Social, economy, reputation and institutions inherited; optional relationship/availability conventions retained | Core GOV/ECO/LIFE; §15 |
| §§108–116 | Supernatural construction retained | §§62–71 |
| §§117–128 | Magical effect/resistance retained | §§72–78 |
| §§129–130 | Mental magic and agency retained | §79 |
| §§131–139 | Specialized supernatural applications retained | §§80–88 |
| §§140–143 | Magic prevalence retained; ordinary world systems inherited | §§94–96 |
| §§144–146 | Generic military inherited; Fantasy magical unit applications retained | §97 |
| §§147–150 | Generic lives/generations inherited; exceptional variants retained | §98 |
| §§151–154 | Generic campaign runtime inherited; Fantasy configuration retained | §99 and Core |
| §155 | Aethelgard relocated to selected profile | §100 |
| §§156–158 | Behavior and acceptance invariants preserved | §§101–105 |

<a id="fantasy-107"></a>
## 107. Fantasy Content Library disposition

Fantasy Content Library v2.0 is the selected genre-content companion. It retains exact FL v1.0 source-qualified identities, specialist models and readiness status, while adding twelve proposed optional Fantasy templates.

Shared Content Library v1.0 supplies eligible reusable mundane/reference definitions, but its unresolved held entries remain tied to their exact original source payloads.

The [Fantasy content map](IRGS_Fantasy_Content_Map_v1_2_Core3_2.csv) covers every **111 FL source references** and links all **61 native Fantasy adapter records** through the [binding](IRGS_Fantasy_Binding_v1_2_Core3_2.json). Source data are included in SCL; a separate original library document is not needed to retrieve them.

Published aliases FL:WPN-M-006A@1.0 and FL:WPN-M-006B@1.0 both resolve to SCL:PBC-WPN-FL-WPN-M-006@0.2, with selectors modes.cut and modes.thrust. They refer to one physical sword family. Never synthesize @1.0 family revisions from the catalogue release number.

Scoped templates such as PAR, XMAT, CPF and the illustrative thermal technique retain their exact FL identity and payload block. They have no invented shared alias where the registry publishes none. Their presence enables neither a supernatural paradigm nor a campaign fact.

Source labels such as “Core,” “Core-derived,” “Proposed” and “Accepted for Fantasy v1.0” retain that source scope. They do not become new universal Core acceptance or calibration claims. A typed-candidate reader view is not a canonical alias.

Definition composition produces a configuration. Actual armor, weapons, creatures, enchantments or created matter require supported initialization or actual authorized production through Core. Construction + coverage + material + quality does not itself create an item.

The Fantasy engine does not assume all library candidates have been promoted to shared canonical definitions.

Retained Fantasy-specialized families include:

`WPN-M | WPN-R | ARM | SHD | MAT adapters | XMAT | BODY specialized profiles | NAT | CRT | PAR | CPF`

Every actual entry selection must preserve:

- namespace;
- ID;
- version;
- required attack or technique selector;
- compatible effect model;
- source status;
- actual variant/configuration.

The SCL catalogue does not create campaign items.

The v2.0 companion is bound to this engine through Appendix E and the receiving manifest. Its source-native F-1.0/FL-1.0 profiles map to the preserved procedures in Fantasy 1.2; they require no parallel old Core. Its FAN-EXT and FAN-CRT patterns remain proposed, noncanonical in SCL and opt-in at setting/profile level. Packaging them creates no spell, creature, reservoir or item.

<a id="fantasy-108"></a>
## 108. Accounted removals

The following duplicated generic procedure ownership is removed from the Fantasy slim edition:

- Core action resolution.
- Generic time and event processing.
- Resource and inventory bookkeeping.
- Generic equipment component records.
- Generic projects and repairs.
- General medicine and conditions.
- Population and organization bookkeeping.
- Ordinary ecology.
- Site and network records.
- General travel/transport logistics.
- Business, property and transaction processing.
- Generic life, careers and succession.
- Campaign state persistence.
- Shared content inheritance.

No valid Fantasy-specific numerical chain or exceptional mechanism is intentionally deleted.

The original Fantasy Engine v1.0 remains provenance and a source reference, not a simultaneous competing runtime engine.

<a id="fantasy-109"></a>
## 109. Changes from Fantasy Slim v1.1

| Change | Reason and disposition |
|---|---|
| Parent changed from Core 3.1 to Core 3.2 | Exact existing Fantasy provider contract selected; no old shared runtime retained |
| Active catalogue changed from SCL 0.2 to SCL 1.0 | Exact aliases, @0.2 revisions, readiness gates and native payloads preserved |
| All 112 Fantasy sections retained | Complete resubmission; no partial patch dependency |
| Native tables and formula statements preserved | No new weapon, armor, injury, training, travel, creature or magic values assigned |
| Provider table rebuilt from the actual Core 3.2 manifest | Corrects approximate/omitted provider links in preceding text |
| Owner fields, runtime handoff and triggers made explicit | Prevents duplicate clocks, stocks, wounds, capacity and event application |
| Native Threat 0 distinguished from terminated transfer | Prevents an overbroad zero guard from deleting Incidental attacks or reviving stopped attacks |
| Travel load, ammunition recovery and deprivation constraints restored explicitly | Preserves original v1.0 functions under current shared ownership |
| Optional relationship and availability conventions retained | Earlier slim text omitted source scales; these remain optional views |
| All 111 FL references and 61 adapters linked | No universal promotion, new aliases or held-definition substitution |
| Fantasy Content Library v2.0 incorporated | Exact current companion, 168 source payloads, twelve proposed templates and forty specified cases; statuses preserved |
| Parameter gates, overrides and source status clarified | Complete specification remains distinct from calibrated profiles and campaign adoption |
| Fresh verification and reconciliation files included | Bounded executed evidence separated from outstanding FSL acceptance program |

No readiness hold is promoted. No source is deprecated. Publication creates or alters no actor, asset, skill, resource, injury, effect, obligation or campaign history.

See [the reconciliation matrix](IRGS_Fantasy_Reconciliation_v1_2.csv) for all 158 original-engine sections, all 112 preceding-slim sections and all 93 original-library sections.

---

# PART XXI — ADOPTION AND MIGRATION

<a id="fantasy-110"></a>
## 110. Workshop edition and prospective campaign adoption

This is the complete Fantasy v1.2 linked workshop edition requested for Core 3.2. Its current document/version identity is distinct from acceptance of every inherited proposal or adoption into a campaign.

Core 3.2 and SCL 1.0 retain their confirmed current workshop status. Fantasy source rules and proposed clarifications retain individual provenance and status; new interface clarifications in this resubmission do not claim prior acceptance. The user may accept a declared scope prospectively after reviewing its ownership, mechanics, content selectors and acceptance evidence.

Acceptance of the engine does not automatically certify numerical realism or balance.

Any further calibration or substantial mechanical changes require their own recorded versions.

<a id="fantasy-111"></a>
## 111. Existing campaign migration

Default:

**No automatic migration.**

Preserve:

`Time | Actor identities | Skills | Attributes | Actual resources | Equipment | Injuries | Fatigue | Magic capacity and spent resources | Locations | Institutions | Knowledge | Relationships | Projects | History`

A documentation ownership change does not alter campaign facts.

If an old campaign used a different damage, attribute or magic model, retain it until a prospective explicit conversion is authorized.

Converting a record requires actual meaning equivalence, not merely similar terminology.

<a id="fantasy-112"></a>
## 112. Final governing principle

Shared Core determines how the ordinary world continues.

The Fantasy Engine determines how its specialized physical and supernatural capabilities operate.

Shared and Fantasy Content Libraries define reusable things and their compatible profiles.

Setting Modules determine what actually exists and which exceptional mechanisms are possible.

Campaign Profiles select relevant rules and calibration.

Campaign State preserves actual entities, quantities and history.

**Fantasy expands what is causally possible without dispensing with agency, resources, time, information or consequence.**

**Simulate first. Narrate second.**

---

**End of the Fantasy v1.2 operating specification. Linked references and receiving records follow.**

---

# APPENDIX A — CURRENT COMPONENTS AND LINKAGE

| Component | Exact edition | Role |
|---|---|---|
| [IRGS Core Engine](Core/IRGS_Core_Engine_v3_2.md) | IRGS-CORE-3.2 | Single shared runtime and eleven domain workflows |
| [Shared Content Library guide](Core/IRGS_Shared_Content_Library_v1_0.md) | IRGS-SCL-1.0 | Catalogue usage and definition boundaries |
| [Normative registry](Core/IRGS_Shared_Content_Registry_v1_0.json) | Catalogue 1.0; exact record revisions retained | Definitions, aliases, native adapters and source payloads |
| [Selected contracts](Core/IRGS_SCL_v1_0_Selected_Contracts.md) | SCL 1.0 | 51 selected qualitative contracts; no automatic calibration |
| [Parent reference map](Core/IRGS_SCL_v1_0_Reference_Map.csv) | SCL 1.0 | Complete shared source map |
| [Parent engine bindings](Core/IRGS_Engine_Bindings_v3_2.json) | IRGS-BIND-FANTASY-3.2 | Published shared-provider contract |
| [Fantasy receiving binding](IRGS_Fantasy_Binding_v1_2_Core3_2.json) | Fantasy 1.2 / Core 3.2 | Exact provider, profile and content selection |
| [Fantasy content map](IRGS_Fantasy_Content_Map_v1_2_Core3_2.csv) | FL 1.0 through SCL 1.0 | 111 source references and exact payload addresses |
| [Fantasy Content Library v2.0](FantasyLibrary/IRGS_Fantasy_Content_Library_v2_0_Candidate.md) | IRGS-FANTASY-LIB-2.0 | Selected Fantasy companion, native projection, twelve proposed templates and forty acceptance cases |
| [Fantasy library deployment](FantasyLibrary/README.md) | This linked package | Clean current deployment and source-file dispositions |
| [Reconciliation matrix](IRGS_Fantasy_Reconciliation_v1_2.csv) | This resubmission | Complete source-section dispositions |
| [Verification report](IRGS_Fantasy_Verification_v1_2.md) | This resubmission | Fresh checks and bounded evidence limits |
| [Package manifest](FANTASY_PACKAGE_MANIFEST.json) | This release | Integrity and numerical preservation |

The package includes these current dependencies directly. Source sections survive as necessary scoped content/adapter data inside the registry; entire older engine/library editions are excluded.

# APPENDIX B — RECORD AND EVENT CONTRACT

| Event or trigger | Fantasy interpretation | Core commit |
|---|---|---|
| Feasible attack contact | Exact mode, coverage, protection and residual effect | Actual spent ammunition, local wear and supported conditions once |
| Activation succeeds; delivery fails | Activation establishes only its supported stage | Retain actual paid costs; no target effect or unrelated catastrophe |
| Area emission | One activation and shared raw result | One activation cost; supported target-specific consequences |
| Sustain ends or source interrupted | Advance or stop according to the technique | Charge processed interval once; stop future output; preserve existing conditions |
| Temporary creation expires | Named material changes through its defined mechanism | Reconcile actual location and derivatives; no debit to nonexistent origin stock |
| Teleport or summoning arrival | Move an identified traveler or perform declared creation/invitation | One actual identity/location; arrival grants no ownership or control |
| Healing or resurrection | Modify enabled named condition/death facts | Preserve identity, other conditions, spent resources and unrelated history |
| Ritual/alchemy accepted | Actual staged work and validated output | Consume inputs, credit real output and commit work once |
| Construct component fails | Actual component and dependent function change | One K-ASSET fault; no duplicate biological wound |
| Earlier-event report arrives | Recipient can now know the report | Update K-INFO; repeat no physical loss/output |

Technique-specific expiry must identify what happens to consumed, transformed, assembled or transferred temporary material. Until that mechanism exists, operations depending on it remain unresolved; the runner invents neither retroactive deletion nor duplicate consumption.

# APPENDIX C — REQUIRED PROFILE CHOICES AND BOUNDS

| Operation | Required compatible selection | Missing-data result |
|---|---|---|
| Consequential execution | Adopted dice/opposition adapter, discipline, circumstances and feasible effect | Routine supported work proceeds; defer only the undefined uncertain operation |
| Character allocation | Ten-attribute model or complete replacement; enabled creation/ancestry rules | No unsupported attributes, history, tools or contacts |
| Physical injury | Mode, contact/location, protection/transmission, Force/Placement/Vulnerability and applicable Resilience | Material unknown blocks severity calculation; known contact/expenditure may stand |
| Shield interception | Orientation, readiness, geometry, contact rule and condition/Structure | Guard modifier proves no impact; no invented wear/residual hit |
| Repeated harm/local wear | Actual component/condition, native stress and Core repeated-harm rules | Preserve prior damage; no whole-suit degradation or repeat-wound immunity |
| Fatigue/travel | One physiology/exertion/load profile, intervals, rest and means | Preserve fractions/supplies; no daily reset or stacked parent track |
| Learning | Schedule and actual hours/evidence/method | No automatic skill from elapsed time |
| Creature/construct | Body plan, physiology/components, Scale and mode | No label-derived headshot, immunity, extra action or Scale damage |
| Magic use | Enabled paradigm/access/technique, real PU translation and cost timing, target/stage limits | No invented spell, mana stock, device charge or new stage |
| Nonphysical protection | Exact channel semantics and Potency/protection interpretation | Do not apply physical penetration by name similarity |
| Healing/creation/teleport/resurrection | Enabled exception, bounds, termination and state consequences | Magnitude alone grants no exceptional function |
| Common supernatural capability | Cost/throughput and economy/warfare/medicine/law/infrastructure/life effects | Record setting questions; invent no institutional past |

Resilience 0 occurs only in a declared synthetic ordinary-human fixture unless separately selected for a campaign. The suite supplies no default for unknown physiology, ward strength, travel rate, shield contact or supernatural recovery.

# APPENDIX D — PROVENANCE, PRESERVATION AND EVIDENCE

The supplied Fantasy Slim v1.1 is the principal receiving source. Its 112 sections survive in this full edition. Original Fantasy Engine v1.0 supplies the 158-section function inventory and restored conventions in §109. Original Fantasy Content Libraries v1.0 supplies its 93-section inventory, numerical adapters and scoped templates already preserved in SCL 1.0.

Core 3.2 and SCL 1.0 are used as published in the clean eight-file parent package. This Fantasy release adds no patch to that parent. Bindings select existing providers, aliases and payloads. Parent hashes record identity; they confer no rule acceptance.

The unchanged parent has two editorial discrepancies: §111 refers to a “v0.2 registry,” and §112 uses “Proposed Core 3.2” despite the current-release header. This deployment follows the confirmed current Core 3.2 header, its published provider binding and the normative SCL 1.0 catalogue. The immutable @0.2 record revisions remain valid; those older phrases select no previous catalogue or competing runtime. The receiving binding and verification report record both discrepancies.

Source self-descriptions such as “Certified operational baseline,” old examples marked “Pass,” and numerical “Core” labels retain their original scope. This release claims only checks executed in its accompanying report.

Existing tables and numerical/formula statements in preceding-slim §§8–98 remain unchanged. Added wording distinguishes transmission from native Threat 0, restores source functions and specifies owner/parameter contracts. The reconciliation matrix accounts for every source section; original files remain unedited and undeclared as deprecated.

FSL-01–FSL-30 is an acceptance program. Formula/state fixtures support only their stated portions. A package check is neither a live playtest nor a full eleven-domain simulation. Calibration, advanced spell/creature profiles, campaign adjudication and independent AI-runner reproduction remain outstanding.





# APPENDIX E — FANTASY CONTENT LIBRARY v2.0 RECEIVING CONTRACT

The selected genre companion is [IRGS-FANTASY-LIB-2.0](FantasyLibrary/IRGS_Fantasy_Content_Library_v2_0_Candidate.md). Core 3.2 remains the shared parent; SCL 1.0 remains the normative common catalogue. The Fantasy-native projection is a read-only subset and proposed-extension reference, not another normative SCL or actual-state ledger.

The companion's 111 source references, 61 native adapters and 168 immutable payload blocks agree with the packaged SCL registry. Its 95 shared references include both held and selected records; the other 16 are scoped Fantasy extensions. No hold is promoted. Legacy “weapon” labels in the source-type column retain historical metadata; the normative unarmed semantic type remains method.

## Native-rule equivalence

F-1.0/FL-1.0 names identify the preserved native profile provenance. Fantasy engine 1.2 supplies the source-compatible character, technique, Threat/Defeat/protection/injury, training, exertion, load, travel, creature and supernatural procedures directly. Exact content records select the matching native mode. Current Core providers supply generic resolution, scheduling, resources, work, information, institutions and continuity.

This records a complete receiving specification at its declared profile-selection boundary. It does not adopt another campaign, calibrate all profiles or give unknown Resilience, shield transfer, ward semantics or supernatural recovery a default. A campaign using another effect chain needs its own explicit conversion.

## Twelve proposed extension bindings

| Content ID | Template | Fantasy procedures | Actual owner boundary |
|---|---|---|---|
| FAN-EXT-001 | Enchanted equipment facet | [§6](#fantasy-6), [§86](#fantasy-86) | K-ASSET; K-WORK; K-TIME |
| FAN-EXT-002 | Bound focus or reservoir | [§62](#fantasy-62), [§63](#fantasy-63), [§71](#fantasy-71), [§86](#fantasy-86) | K-ASSET; K-ACTOR or K-STOCK for the actual resource; K-TIME |
| FAN-EXT-003 | Potion or infused consumable | [§7](#fantasy-7), [§19](#fantasy-19), [§74](#fantasy-74), [§87](#fantasy-87) | K-STOCK; K-ASSET; K-ACTOR; K-TIME |
| FAN-EXT-004 | Ward or boundary field | [§6](#fantasy-6), [§74](#fantasy-74), [§86](#fantasy-86), [§96](#fantasy-96) | K-ASSET; K-NET; K-ACTOR; K-TIME |
| FAN-EXT-005 | Portal / teleportation link | [§7](#fantasy-7), [§83](#fantasy-83), [§96](#fantasy-96) | K-NET; K-ACTOR; K-ASSET; K-STOCK; K-TIME |
| FAN-EXT-006 | Summoned autonomous ally | [§7](#fantasy-7), [§82](#fantasy-82), [§91](#fantasy-91) | K-ACTOR; K-ORG; K-TIME; K-INFO |
| FAN-EXT-007 | Conjured commodity | [§7](#fantasy-7), [§84](#fantasy-84) | K-STOCK; K-ASSET when applicable; K-TIME |
| FAN-CRT-001 | Dragonlike organism variant | [§57](#fantasy-57), [§58](#fantasy-58), [§59](#fantasy-59), [§60](#fantasy-60), [§61](#fantasy-61), [§72](#fantasy-72), [§78](#fantasy-78) | K-ACTOR; K-POP; K-TIME |
| FAN-CRT-002 | Undead animated body | [§60](#fantasy-60), [§82](#fantasy-82), [§85](#fantasy-85), [§90](#fantasy-90) | K-ASSET; K-ACTOR when an actor exists; K-TIME; K-INFO |
| FAN-CRT-003 | Elemental / manifest spirit | [§57](#fantasy-57), [§62](#fantasy-62), [§63](#fantasy-63), [§64](#fantasy-64), [§82](#fantasy-82) | K-ACTOR; K-TIME; K-INFO |
| FAN-CRT-004 | Shapeshifter / cursed form | [§57](#fantasy-57), [§85](#fantasy-85), [§98](#fantasy-98) | K-ACTOR; K-ASSET; K-TIME |
| FAN-CRT-005 | Construct or golem | [§6](#fantasy-6), [§60](#fantasy-60), [§86](#fantasy-86) | K-ASSET; K-ACTOR when an actor exists; K-ORG; K-INFO; K-TIME |

All twelve remain proposed and require explicit setting/profile activation. Each must supply its actual source, access, geometry, finite costs, method, targets, persistence, interruption, counterplay and supported output. The original requirements and limitations are retained exactly in the receiving binding. No proposed ID becomes an SCL alias or an instantiated actor, asset or stock.

The companion's [forty acceptance cases](FantasyLibrary/Fantasy_Acceptance_Cases_v2_0.csv) remain specified rather than live tested. Fresh crosswalk and numerical-preservation checks support only their stated structural/bounded portions.

## Clean deployment and source accounting

The supplied v2.0 archive is preserved unchanged as the source reference outside this active distribution. This clean linked package includes its current guide, crosswalk, native projection, 93-section reconciliation and forty cases. Its two complete v1.0 provenance documents are omitted from the distribution; their immutable entry/adapter data remain available in SCL and the native projection, and their full original files are not deleted or deprecated.

The v2.0 README, integrity manifest, deployment checker and report are rebuilt around these current files and this engine's explicit binding. Original checks requiring archived full texts were executed against the supplied archive before deployment, then replaced here with exact normative-registry/native-data checks. Removals, retained hashes and receiving evidence are recorded in FantasyLibrary/VERIFY_MANIFEST.json. The v2.0 source's references to its archived originals describe that original archive, not a dependency on another active engine in this package.

**End of IRGS Fantasy Engine — Slim v1.2, linked to Core 3.2, SCL 1.0 and Fantasy Content Library 2.0.**
