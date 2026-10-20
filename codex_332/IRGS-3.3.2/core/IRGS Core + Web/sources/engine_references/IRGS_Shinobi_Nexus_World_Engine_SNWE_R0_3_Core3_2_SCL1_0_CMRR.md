# IRGS — Shinobi Nexus World Engine
## Expanded Shinobi Genre/World Foundation R0.3 — Core v3.2 / SCL v1.0 Complete Receiving Rebuild

**Document ID:** `IRGS-SNWE-0.3`  
**Build date:** 14 October 2026  
**Status:** **PROPOSED complete receiving edition**; not automatically adopted, live-playtested or calibrated  
**Shared parent:** `IRGS-CORE-3.2` — current workshop baseline in the Full Maturation R2 release (14 October 2026)  
**Shared catalogue:** `IRGS-SCL-1.0` — current normative catalogue, unchanged `@0.2` identities and individual status gates  
**SNWE engine binding:** `IRGS-BIND-SNWE-0.3-CORE-3.2` — newly authored proposed local receiving binding, **not** a modification of the Core release register  
**Source operating edition:** *SSN — Rebuilt Base R0.1 — Working Playtest Edition* (9 October 2026); original native chapters preserved  
**Immediate predecessor:** `IRGS-SNWE-0.2` (Core 3.1 / SCL 1.0 comparative edition), original file preserved  
**Source method:** Compare → Merge → Reconcile → Resubmit  
**Campaign migration:** None applied; existing checkpoints retain established authority.

> **Authority and release note.** The Full R2 distribution is a source-preserving candidate. Its bundled Core v3.2 and SCL v1.0 are the current receiving references, but R1/R2 content maturation for 228 held families remains proposed. This genre rebuild does not amend locked SSN Canon-Zero, previous campaign state, or native SSN R0.1 numerical behavior. Inheritance does not mean that every missing setting or physical parameter has been supplied.

## Navigation

- **Part I — Receiving architecture and native-model selection** (Core v3.2 / SCL 1.0).
- **Part II — Complete native SSN operating chapters 1–14**, unchanged except explicitly marked Core receiving notes.
- **Part III — All twenty existing Shinobi world conversion/binding sections 17–36**, retargeted without adding general Core mechanisms.
- **Part IV — Original R01–R40 decision and S01–S48 source archives**, copied without edits.
- **Part V — v3.2 source pins, bidirectional CMRR, complete engine manifest, tests, calibration, release and migration.**

---

# Part I — Authority, Inheritance and Runtime

## P1. Purpose and scope

SNWE simulates a continuing Shinobi world whose abilities alter character-scale possibilities and may change medicine, commerce, infrastructure, institutions, environment, espionage, warfare and daily life. It is **not** a light combat plug-in. A comprehensive conversion layer is necessary because extraordinary techniques have material and societal implications, but every universal state fact remains owned by the Shared Core.

**Architecture:** `Shared IRGS Core 3.2 → SNWE R0.3 → Shinobi Setting/Theme Module → Campaign Profile → Campaign State`. SCL is a separately versioned **content/reference catalogue**, not another engine layer or world ledger.

The genre engine defines the Shinobi-specific **means, capability parameters, conversion rules and interpretations**. The setting/module defines **actual permitted techniques, clans, cosmology, species, regional institutions and prevalence**. A campaign profile selects compatible rules and parameters; actual people, places, objects, beliefs, resources and history occur only in Campaign State.

Ordinary life, medicine, teaching, social relationships, business, security, population continuity, military service, strategic government, stable prosperity and peace remain supported without mandatory combat or escalating opposition.

## P2. Source authority and design status

1. Current explicit user direction/correction.
2. Established campaign override and world/campaign facts.
3. Relevant adopted Shinobi genre rules and setting rules within their valid scope.
4. User-confirmed IRGS Core 3.2 baseline where selected/adopted for that scope.
5. Explicit scoped temporary proposal for a genuine unresolved rule or parameter.

SSN's historical Canon-Zero v1.9.2 lock is **not overwritten**. The *SSN Rebuilt Base R0.1* is the selected **working playtest ruleset** reproduced here, not an assertion that all historical conflicts are resolved. Mechanical construction, workshop confirmation, source verification, playtesting and numerical calibration are different statuses.

**Core:** The exact Core v3.2 file is the current Core source in the user-supplied 14 October Full R2 distribution and is marked the current workshop baseline by its receiving register. The combined R2 distribution remains a **source-preserving candidate**; neither its proposed content expansions nor this new SNWE edition are automatically adopted in a campaign. The older Core 3.1 release remains archival provenance, not a concurrent parent.

**Catalogue:** `IRGS-SCL-1.0` is the current normative catalogue supplied with Core v3.2. This is **catalogue selection**, not automatic adoption of all entries: it retains original `@0.2` definition identities, exactly 51 selected qualitative contracts and 228 held families. R1/R2 maturation drafts for held families are **proposals**, not activated replacements. Existing campaigns keep their own recorded catalogue versions until an authorized prospective rebind.

## P3. Core v3.2 receiving provider registry

The **single authoritative** Core 3.2 implementation supplies the shared rules; v2.1, CDI 0.2, Pass A/B/C and CW-SSN extraction patches are provenance, not runtime co-parents.

| Shared function | Core 3.2 provider | SNWE consumption and retained distinction |
|---|---|---|
| Agency, ability feasibility and optional action stages | §§4–9, 90 | SSN 2d6/d20 and costs remain native; no second d100 |
| Time, event frontier, simultaneous action, cost/replay | §§10–12, 47, 62, 91 | SSN rounds, turns, reactions, downtime and Era intervals are selected timing profiles |
| Actor capability, conditions, needs and development | §§14–19, 31, 68–71, 77, 122 | SSN eleven statistics, Level/Band, HP/SP/CU/Trauma/Stress and advancement are native |
| Equipment, stock, claims, custody, transit | §§20–24, 35–38, 105, 111, 114 | SSN attack/Armor Reduction and abstract Supply/RP are selected profiles, not physical duplicates |
| Orders, institutional authority and information delays | §§25–30, 41–46, 60–61, 64–65, 85–86, 107 | Shinobi office, Kage, ANBU and ranks are specialized institutional content |
| Spatial, protection, effects and manifestations | §§47–55, 106 | SSN zone/hit/mitigation rules are the sole selected effect chain; illusion/clone/summon are scoped technique effects |
| Missions, programs, technology diffusion and offscreen work | §§62–63, 73–76, 83–84, 95–96, 108–110 | Native mission phases, research, jutsu tech, teaching and genre dissemination |
| Exceptional changes and history | §§79, 97, 99, 112 | Destiny/Karma/DSSN and rescue/flashbacks use only SSN written exception contracts |
| Networks, flows, capacities and service | §§101–103, 108–109 | Real practitioner labor and jutsu-enabled transport/healing/production need technique-specific rates |
| Population and unit totals | §§41–42, 62, 106 | Unit Strength ratings remain separate from headcount, injury and equipment totals |
| Shared content and profile binding | §§111–112, Appendix B | SCL exact 0.2 handles/selectors; SSN jutsu/bloodline/numeric profiles remain specialized |
| Eleven domain workflows | §§113–123 | GOV, ECO, INV, MAR, CIV, MED, WILD, INTEL, URBAN, LIFE, COMP receive SSN-specific implementations |

**Core extraction receiving crosswalk — inherited, not recreated:** CW-SSN-01 → §5; 02 → §109; 03 → §73; 04 → §55; 05 → §99; 06 → §108; 07 → §24; 08 → §41. These destinations are explicitly recorded in the archived Core v3.1 Appendix G; the receiving destinations remain in Core v3.2. SNWE R0.3 neither retains a separate parallel generic implementation nor represents those eight as pending incorporation.

## P4. Shared state ownership and native records

| Owner | Authoritative facts | Relevant SSN-specific view |
|---|---|---|
| K-TIME | Time, event queue, reservations/commitments, random record and processed spans | Round, reaction, downtime action, phase, three-month Era |
| K-ACTOR | Continuing identity, selected capability and conditions | Eleven stats, HP/SP/CU, Trauma, Stress, techniques and learning links |
| K-STOCK | Real fungible goods, currency, lot identity, custody, title and commitments | Weapons/consumables/provisions; selected entitlement bridge, not duplicate tokens |
| K-ASSET | Physical items, components, condition and nonfungible objects | Tools, puppets, barriers, equipment and artifact embodiments |
| K-WORK | Real tasks and accepted outputs | Technique research, instruction, training and actual construction |
| K-INFO | Actual observations, lineage, report contents and recipient beliefs | Sensor output, disguise, Genjutsu observation, mission intelligence |
| K-ORG | Institutions, membership, appointment, authority and credentials | Hidden Village offices, ANBU assignment, squad roster, clan offices |
| K-NET | Real routes, networks and delivered service | Missions in transit, hospital delivery, technique-assisted infrastructure |
| K-POP | Actual named and residual population conservation | Shinobi corps headcount and individual casualties |

Domain or genre records **refer to these owners**, rather than independently storing spendable totals, actual physical injuries, person counts or installed machinery. Optional derived meters such as Standing and unit Strength must identify their native owner, scope and whether they are independent specialized game state or summaries.

## P5. Exact Shared Content Library contract

**Current receiving catalogue:** `IRGS-SCL-1.0` is the normative Core 3.2 catalogue release, retaining exact per-family `@0.2` identifiers and unchanged entry readiness. The registry has **279 original family records (51 selected qualitative contracts and 228 source-backed held candidates)**, **286 source rows**, **1,416 unmodified aliases**, **304 tracked source references**, **420 original payload blocks**, **61 Fantasy adapters** and **18 scoped extensions**. These are different unit counts and must not be conflated. SCL 1.0 retains **22 non-instantiating physical weapon-parent/mode relationships**, not 22 new physical weapon items.

### Reference/readiness rules

1. Resolve exact `(namespace, family, revision, selector, semantic type)` and validate target checksum/type against the pinned registry. The receiving catalogue uses `SCL:PBC-…@0.2` identities; it **does not** install standalone typed `SCL:<kind>:…@1.0` proposed strings as canonical aliases.
2. A `selected_shared_contract` authorizes only its demonstrated qualitative interface. It does **not** import Fantasy Threat/Armor Defeat or substitute SSN damage, Accuracy, Stamina or Chakra values.
3. A `source_backed_hold` may use only its complete exact preserved source payload/adapter, with the source's original native dependencies, when explicitly selected. It cannot impersonate a complete shared replacement.
4. A `scoped_extension` is never universally enabled merely because it resides in a common catalogue.
5. Shared ordinary family definitions specify construction/eligibility; SSN defines combat/protection, Shinobi-tool activation, medical effect, artifact bonding and other specialist numerical behavior.
6. A family plus two attack-mode selectors is one actual item with two possible uses, not two objects or two attacks. An unarmed entry is a **method**, not an inventory item. Selecting a library entry does not produce equipment, supply or skill.
7. An item/medicine/technology needs actual setting eligibility, issued/owned instance, applicable numeric profile and all relevant requirements. A source material name cannot grant extraordinary capability.
8. Every adapted entry stores `shared_exact_ref | SCL_release/status | selector/semantic_type | native SSN effect/profile ID | source provenance/status | actual instance ref (when any) | override/exclusion`. No invented cross-conversion of dice, mitigation, healing or technical units.

### Content-selection profiles

- **SNWE-R03-NATIVE (Core 3.2 / SCL 1.0):** Current proposed SNWE receiving selection. Native SSN R0.1 numerical models govern gameplay; shared catalogued content is enabled only at its declared readiness and with compatible source-native adapters.
- **SNWE-R02-LEGACY (Core 3.1 / SCL 1.0 or 0.2 as actually recorded):** Historical predecessor selections persist only for campaigns explicitly pinned to them; any upgrade is prospective, scoped and separately authorized.
- **SNWE-HELD-CONTENT (Core 3.2 / SCL 1.0):** One named held item may be referenced through its complete exact original payload and compatible selected adapter; the R1/R2 qualification prose remains non-normative until separately validated/promoted.

**SSN-specific library status:** The base R0.1 starter jutsu and item profiles in Part II are retained as native records. No full Shinobi jutsu, clan, summon, bloodline, creature, ninja-tool or regional library can be generated solely from SCL 1.0. Unconverted historical libraries remain named dependencies/known gaps, not deleted content.

## P6. Native SSN compatibility selections

The default source-preserving operating profile is **SSN R0.1**:

| Mechanism | Selected SSN-owned meaning | Incompatible parallel execution |
|---|---|---|
| Standard uncertain tasks | 2d6 + statistic + proficiency ± situational against native DC | No Core d100 band/Mixed on same attempt |
| Physical and Precision hits | d20 confirmation with native Level/accuracy/defense | No second Core or Fantasy hit confirmation |
| Damage and injury | SSN raw dice → innate Damage Resistance → Armor Damage Reduction → Health → injury trigger | No Fantasy Threat/Defeat/Injury Grade additional chain |
| Native Level/Band/Rank | Independent 0–20 Level, 0–10 Band and actual office/rank | No assumed Core attribute score or promotion-to-power |
| Chakra/Stamina/Trauma | Native actor pools, output threshold, rank escalation and care rules | No stockpile or generic power-meter duplication |
| Time/actions | Native round/Standard/Minor/Movement/Reaction, strategic phase/three-month Era | No action refresh by scale shift |
| Mission/research clocks | R0.1 segments and DCs in **abstract profile**, task time and real work in Core | No repeated work/progress per summary review |
| Personal Supply/faction RP | Native bounded abstract economy or explicit persistent-world bridge | No simultaneous cash/stock duplication |
| Medical and Stress | R0.1 condition/therapeutic numeric profile; Core owns continuing physical facts | No double injury/treatment/recovery |
| Jutsu/exceptions | Rank-cost/effects, synthesis, Genjutsu, seals, summons, Destiny/DSSN | No generic magic formula or free capabilities |
| Unit Strength | SSN tactical effectiveness measure | No 1 Strength = 1 death or full-population copy |

An explicit genre selection replaces only the affected generic **default**. It does not override agency, causality, resource accounting or current campaign authority.

## P7. Native abstract mode and integrated persistent-world mode

**A — SSN R0.1 abstract playtest:** Operates the native §9 token/downtime/project clocks and §12 RP/Strength/military abstractions, while Core 3.2 provides identical physical character/event identities and truth/knowledge semantics where tracked. An abstract token is not simultaneously a second actual stock unit. Use when physical production and finance precision are not needed. Abstract clocks and grants still obey their expressly defined time/scene/interval boundaries.

**B — Persistent Shinobi world:** Operates native resolution, combat, chakra and technique effects, and routes actual production, logistics, income, holdings, services, contracts and casualty state through Core. Each abstract SSN benefit requires an **explicit selected bridge** that states meaning, backing, units, source, scope, and exact redemption or replacement effect. If missing, the dependent abstract-to-physical conversion is unavailable; unrelated native combat/world activity continues. Do not assume one Supply token equals a certain amount of ryō or three Resource Points represent any fixed troop count.

**C — Optional mythic modules:** Explicitly enable bloodline/artifact/Destiny/DSSN content with written effect/authority contracts. The R0.1 Destiny starting value remains part of the selected source game profile; optional *mythic expansions* and setting-specific Nodes require separate campaign selection.

**Mode change:** A mode change is a prospective profile/migration action, not an in-world reward. Preserve actual goods, actor resources, resolved work, injuries, offices, claims and known history. Reconcile unspent abstractions as entitlements/claims only where a supported agreed conversion exists. Do not cash out tokens into invented inventory.

## P8. Runtime and source preservation

**Shared causal runtime:** `Declaration → Feasibility → Commitment/Reservation → Selected SSN execution uncertainty → Feasible Effect → Exposure/Autonomous Reaction → Atomic Owner-Qualified Commit → Observation/Transmission/Receipt → Player Control`. This is a task-specific composition of Core §§5/11/90–91, not another event engine. Omit a dice step when a qualified routine activity is certain.

Each meaningful event has Core campaign-scoped identity, causal time, source versions, authorized actor, real commitments, changed owners, recorded uncertainty and consequences, pending events and information-receipt history. Playback/saves preserve one immutable applied-event marker. Changing scale or rendering a sheet changes **view**, not state or earned action budget.

**Player agency:** A successful negotiation is not mind control. A failed mission does not authorize invented flight or spending by the PC. NPCs can comply, deceive, flee or persist autonomously when their actual knowledge/means and goals support it. No narrative balance escalation overwrites stable success.

**Native source preservation:** Part II retains every native R0.1 Chapter 1–14 passage present in SNWE R0.3; Part IV retains R01–R40 and S01–S48 without editorial revision. Only the explicitly labeled receiving notes in Part II are retargeted to Core 3.2. Chapter content is not rewritten, flattened or rebalanced. The R0.1 starter catalogue is not represented as the complete historical jutsu canon.

**Source verification:** Full direct reconstruction of historical SSN Canon-Zero and complete old jutsu/bloodline library from source snapshots is *not* claimed. Source pages, Drive links and the native decision register preserve provenance, not proof every previous source was recovered or adopted.

---

# Part II — SSN R0.1 Native Operating Rules (complete retained profile)

## 1. The operating contract

Use the rules in this book together. Do not import an older formula, cost table, advancement benefit, or damage multiplier merely because its name resembles a current rule.

Four things describe a character:

- Level measures accumulated development, from 0 through 20.

- Character Band measures the scale of effects they can attempt, from 0 through 10.

- Institutional Rank measures authority, access, responsibility, and obligations.

- Statistics and proficiencies measure capability.

Rank never supplies a numeric bonus. A political promotion does not raise Level or Band. Bloodline Grade, Network Grade, and unit ratings use separate 1–7 scales; they are not Character Bands.

The scene-scale engine uses 2d6 for uncertain tasks, chakra molding, resistance, medicine, social conflict, and projects. It uses 1d20 only to confirm physical or precisely aimed hits. Damage uses the dice written in the attack. No implicit conversion between these engines exists.

A roll requires a possible action, an uncertain outcome, and a meaningful consequence. State the objective, approach, cost, target, and failure consequence first. Impossible actions require a change in circumstances; automatic criticals do not make an impossible declaration legal.

Keep half-points in statistics, totals, and thresholds. Round resource costs and damage up once at the end of their calculation; round only formulas explicitly marked floor downward. Current resources cannot exceed their maxima or fall below zero. A cost cannot be paid with resources the character does not have.

Source basis: S01–S03. Namespaced scales, rounding, and feasibility are reconstruction decisions R01–R03.


### Core v3.2 receiving boundary — Chapter 1 (SNWE R0.3 proposed binding)

> SSN R0.1 is the selected native task/scale profile. Core 3.2 §§4–9 and 90–91 govern feasibility, player authority and persistent event commits. Native Level/Band/Rank are not merged with Core competency tiers.

## 2. Character creation

### 2.1 Build a shinobi

1\. Choose a name, home, civilian background, affiliation, and personal creed or nindō.

2\. Write one commitment, one bond, one rival or obligation, and one situation that tests the creed.

3\. Assign the eleven statistics.

4\. Select proficiencies and an elemental affinity.

5\. Choose starting techniques and equipment.

6\. Calculate resources and defenses.

7\. Record Level, Character Band, Rank, Destiny, injuries, and any heritage permission separately.

A standard new campaign begins at Level 2, Character Band 1, usually Junior Genin. Make a Level 1 character below, then apply one advancement. The institutional rank is a setting decision.

### 2.2 Eleven statistics

Statistic: Strength • Main use: Force, lifting, grappling, physical damage

Statistic: Agility • Main use: Accuracy, movement, balance, stealth

Statistic: Stamina • Main use: Sustained physical effort and stamina capacity

Statistic: Intelligence • Main use: Analysis, research, medicine, seal design

Statistic: Wisdom • Main use: Judgment, insight, mental discipline in practice

Statistic: Perception • Main use: Observation, tracking, threat detection

Statistic: Charisma • Main use: Leadership, persuasion, social presence

Statistic: Chakra Reserves • Main use: Inborn reserve contribution; fixed after creation

Statistic: Constitution • Main use: Bodily resilience, injury resistance, recovery

Statistic: Sensitivity • Main use: Chakra perception, molding, synthesis

Statistic: Willpower • Main use: Mental resistance and maintaining resolve

At Level 1 assign this array once: 2.5, 2, 2, 1.5, 1.5, 1.5, 1.5, 1, 1, 1, 1. Total: 16.5. Values normally use half-steps between 0.5 and 7. Chakra Reserves cannot receive later statistic increases. Its contribution remains static; Level still increases the base chakra pool.

This array is a new controlled starting point. Older arrays use inconsistent stat counts and much larger budgets. Do not combine them.

### 2.3 Proficiency

Tier: Untrained • Task bonus: 0 • Accuracy bonus: 0 • Taijutsu bonus dice: 0

Tier: Proficient • Task bonus: +1 • Accuracy bonus: +1 • Taijutsu bonus dice: 0

Tier: Expert • Task bonus: +2 • Accuracy bonus: +2 • Taijutsu bonus dice: +1

Tier: Master • Task bonus: +3 • Accuracy bonus: +3 • Taijutsu bonus dice: +2

A task adds one relevant statistic and one proficiency. Accuracy bonuses apply only to hit rolls. Bonus damage dice apply only to Taijutsu strikes, using that strike's die size. A medical or social proficiency never adds damage.

Begin Proficient in Taijutsu and four other entries. You may choose from the skills below and the disciplines Ninjutsu, Genjutsu, Fūinjutsu, and Synthesis. No starting Expert or Master.

Skills: Athletics; Escape/Resist • Usual statistic: Strength or Stamina; Strength or Agility

Skills: Acrobatics; Stealth; Weaponry; Throwing • Usual statistic: Agility

Skills: Chakra Control; Synthesis; Summoning • Usual statistic: Sensitivity

Skills: Sealing Arts; Scientific Ninja Tools • Usual statistic: Intelligence

Skills: Medicine; First Aid; Poisoncraft; Crafting/Repair • Usual statistic: Intelligence

Skills: Perception; Tracking/Survival • Usual statistic: Perception; Perception or Wisdom

Skills: Analysis; Lore/History; Tactics • Usual statistic: Intelligence

Skills: Persuasion; Intimidation; Performance; Politics/Diplomacy • Usual statistic: Charisma

Skills: Deception/Disguise • Usual statistic: Charisma or Intelligence, chosen by approach

Skills: Insight • Usual statistic: Wisdom

Sealing Arts is the noncombat application of the same proficiency recorded as Fūinjutsu. Do not buy or add both. Chakra Control is a skill; Constitution is a statistic. The old abbreviation CON must never silently stand for both.

Choose one of Fire, Wind, Lightning, Earth, or Water as an affinity. An affinity grants access to techniques of that nature, not a free roll bonus. Choose three E-rank techniques at Level 1. At Level 2 add one E- or D-rank technique and one proficiency step within the tier ceiling.

### 2.4 Starting kit and records

Starting kit: suitable clothing, light armor (Armor Rating 1), one melee weapon, six throwing weapons, rope, basic field tools, one medical kit with three uses, and three days of rations. Begin with 1 Destiny Point and 3 personal Supply tokens. The token economy is a playtest abstraction, separate from a faction's Resource Points.

Record: current and maximum Health Points, Stamina Points and Chakra Units; Trauma; Stress; Destiny; Karma imbalance; injuries; learned techniques; gear; bonds; faction standing; and active clocks.

Source basis: S01, S20, S31, S46. Array, starting kit, proficiency schedule, and skill mapping are supplied by R04–R06.


### Core v3.2 receiving boundary — Chapter 2 (SNWE R0.3 proposed binding)

> Use Core §§14–16/77, 106, 122 for identity, physical presence, learning evidence and lifecycle; K-ORG handles rank. R0.1 starting equipment is instantiated exactly once through Core §88 under the selected creation profile. SCL definitions alone are not a second starting kit.

## 3. Resolution

### 3.1 The Golden Equation

2d6 + relevant statistic + proficiency bonus + situational modifiers ≥ Difficulty Class.

Margin is the final total minus the Difficulty Class. Margin 0 succeeds. A negative Margin fails unless a procedure explicitly supplies a partial outcome.

Difficulty: Routine under pressure • DC: 7 • Example: Climb a useful rope while pursued

Difficulty: Trained challenge • DC: 9 • Example: Decode a familiar field cipher

Difficulty: Difficult • DC: 11 • Example: Treat a serious wound in poor conditions

Difficulty: Severe • DC: 13 • Example: Infiltrate an alert specialist's post

Difficulty: Exceptional • DC: 15 • Example: Stabilize a dangerous experimental ritual

For an effect whose difficulty is primarily a scale difference, use 7 + 2 × (target Character Band − actor Character Band), minimum 3. Do not add this difference again to an ordinary defense threshold. Environmental scale is assigned before rolling and written in the scene notes.

Passive physical resistance is Fortitude Threshold = 7 + Constitution. Passive mental resistance is Resolve Score = 7 + Willpower. These thresholds use the 2d6 engine; they are not d20 Defense Targets.

### 3.2 Advantage, assistance, and criticals

Advantage: roll 3d6, keep the highest two. Disadvantage: keep the lowest two. They do not stack and cancel one-for-one to normal; additional copies do not survive cancellation. The kept pair determines criticals. This mechanism is for 2d6 checks only.

Double sixes succeed on a feasible task and give one appropriate benefit: improved position, one extra clock segment, doubled non-damage duration, or one Trauma from a genuinely harmful effect. Double ones fail and cause one stated complication. Criticals do not multiply damage, add damage dice, waive resource costs, or bypass mitigation. No exploding dice operate in R0.1.

One helper may spend their Standard Action and pass a relevant DC 9 task to give Advantage on the next allied 2d6 task before the helper's next turn. For a d20 attack, a successful aid instead gives +1 accuracy. A roll may benefit from one aid only.

Total situational bonuses or penalties are capped at ±3. Statistic, proficiency, Level contribution, and written injury/Trauma penalties are not situational modifiers. Apply only the strongest overlapping version of the same condition.

### 3.3 Clocks and retries

Use four segments for a short obstacle, six for a substantial project, eight for a campaign problem, and twelve for a major research effort. One successful action fills one segment; Margin 3+ fills two; a critical fills three instead. Maximum three per action.

A failed project action adds one setback; a critical failure adds two instead. At three setbacks, resolve a complication, lose one completed segment, and reset setbacks to zero. Completed progress cannot drop below zero.

Do not reroll an unchanged attempt without spending time, resources, accepting increased exposure, or changing the approach. Every clock records its objective, allowed approaches, interval, DC, consequences, and completion effect.

Source basis: S01, S08, S20 and S31. Critical boundaries, thresholds and unified clocks are R07–R09.


### Core v3.2 receiving boundary — Chapter 3 (SNWE R0.3 proposed binding)

> Core §5 supports optional capability stages; §73 owns typed clock semantics and actual work. Retain the native R0.1 roll thresholds and segment numbers, never add Core d100 Mixed or d100 situational modifiers to SSN 2d6/d20 outcomes.

## 4. Resources and chakra

### 4.1 Level baselines

Level: 0 • Base Health: 10 • Base Stamina: 4 • Base Chakra: 0

Level: 1 • Base Health: 20 • Base Stamina: 8 • Base Chakra: 30

Level: 2 • Base Health: 25 • Base Stamina: 9 • Base Chakra: 40

Level: 3 • Base Health: 30 • Base Stamina: 10 • Base Chakra: 50

Level: 4 • Base Health: 35 • Base Stamina: 11 • Base Chakra: 60

Level: 5 • Base Health: 40 • Base Stamina: 12 • Base Chakra: 70

Level: 6 • Base Health: 46 • Base Stamina: 13 • Base Chakra: 82

Level: 7 • Base Health: 52 • Base Stamina: 14 • Base Chakra: 94

Level: 8 • Base Health: 58 • Base Stamina: 15 • Base Chakra: 106

Level: 9 • Base Health: 64 • Base Stamina: 16 • Base Chakra: 118

Level: 10 • Base Health: 70 • Base Stamina: 17 • Base Chakra: 130

Level: 11 • Base Health: 76 • Base Stamina: 18 • Base Chakra: 145

Level: 12 • Base Health: 82 • Base Stamina: 19 • Base Chakra: 160

Level: 13 • Base Health: 88 • Base Stamina: 20 • Base Chakra: 175

Level: 14 • Base Health: 94 • Base Stamina: 21 • Base Chakra: 190

Level: 15 • Base Health: 100 • Base Stamina: 22 • Base Chakra: 205

Level: 16 • Base Health: 107 • Base Stamina: 23 • Base Chakra: 225

Level: 17 • Base Health: 114 • Base Stamina: 24 • Base Chakra: 245

Level: 18 • Base Health: 121 • Base Stamina: 25 • Base Chakra: 265

Level: 19 • Base Health: 128 • Base Stamina: 26 • Base Chakra: 285

Level: 20 • Base Health: 135 • Base Stamina: 27 • Base Chakra: 305

Health maximum = Base Health + 4 × Strength + 4 × Constitution.

Stamina maximum = Base Stamina + 2 × Stamina + 2 × Constitution.

Chakra maximum = Base Chakra + 20 × Chakra Reserves.

Chakra Units are the expendable current pool, not the Chakra Reserves statistic. Spend Stamina Points on physical effort and reactions; spend Chakra Units on chakra techniques. They cannot be converted into each other.

### 4.2 Output and escalation

Chakra Efficiency Rate = Sensitivity + Chakra Control proficiency bonus.

Overclock Threshold = Chakra Efficiency Rate + Willpower ÷ 2.

Efficiency is an output-stability rating, not a percentage or a blanket discount. Track total chakra spent in the round, including upkeep. The first time it exceeds the threshold, take 1 Trauma. Further spending that round causes no additional threshold Trauma. S-rank and synthesis consequences are separate. Reset output counting each round.

A technique has its rank's base cost. Repeated casts of that rank in a scene add cumulative Escalation Tax:

Rank: E • Base Chakra Units: 1 • Tax per earlier paid cast of that rank: 0

Rank: D • Base Chakra Units: 3 • Tax per earlier paid cast of that rank: 0

Rank: C • Base Chakra Units: 5 • Tax per earlier paid cast of that rank: 1

Rank: B • Base Chakra Units: 8 • Tax per earlier paid cast of that rank: 2

Rank: A • Base Chakra Units: 12 • Tax per earlier paid cast of that rank: 3

Rank: S • Base Chakra Units: 18 • Tax per earlier paid cast of that rank: 4

Thus a character's first three C-rank casts cost 5, 6, and 7 before explicit adjustments. Counters belong to each character and each rank. Failed paid activations count. Upkeep does not count as another cast. Cost never falls below 1.

### 4.3 Recovery and exhaustion

At the start of each turn recover 1 Stamina Point. If you took no Standard Action on your preceding turn, recover 2 instead. This cannot be exploited by declaring extra turns outside a scene. A ten-minute safe rest restores Stamina to maximum.

At zero Stamina you are Exposed, cannot Dodge or Parry, and take +5 raw damage from incoming damaging hits before mitigation. Regaining Stamina removes this exhaustion-based Exposed state. Other sources of Exposed last for their own duration.

Chakra never regenerates automatically in combat. One uninterrupted hour of rest restores one quarter of maximum Chakra, rounded up; eight hours of safe sleep restores all. Recovery is limited by actual elapsed time, cannot overlap, and never exceeds the pool maximum. These are reconstruction recovery rates, not legacy CPS.

A short rest does not heal Health. A safe eight-hour rest restores one quarter of maximum Health; serious injuries remain until treated. Longer recovery is specified in Chapter 7.

CPS, Flow Quality Index, Chakra Synthesis Score, and percentage-based Chakra Stress Load formulas are retained in the archive as historical alternatives. They do not silently run in parallel with these rules.

Source basis: resource table and final formulas S01; output/regen boundaries S01 and S20. Efficiency definition, crossing rule, cumulative tax and timed recovery are R10–R13.


### Core v3.2 receiving boundary — Chapter 4 (SNWE R0.3 proposed binding)

> Actor-owned current Health, Stamina, Chakra, Stress and Trauma use K-ACTOR. Core §109 handles resource/output/burden semantics; §10 schedules recovery. SSN costs, thresholds, rank counters and recovery values are unchanged. No generic power or consumption rule stacks on the same cause.

## 5. Tactical combat

### 5.1 Round and turn

A round represents approximately six seconds. Roll initiative once: 2d6 + Agility + Perception. Higher acts first; ties go to higher Agility, then players choose between allies or the GM settles remaining ties.

On your turn you have one Standard Action, one Minor Action, and movement up to one zone. You have one Reaction between the starts of your turns. Refresh it at the start of your turn. A round does not grant extra attacks for having a large resource pool.

A Minor Action draws an item, opens a simple door, issues a short order, or interacts with something uncomplicated. It cannot attack, cast a Standard technique, or complete a project check. A Standard Action attacks, casts, treats a wound, aids, escapes, interacts under serious pressure, or dashes one additional zone. Dash costs 1 Stamina. Difficult terrain costs another 1 Stamina per zone and may demand an appropriate task.

Zones are connected pieces of terrain with a tactical identity. “Engaged” means within melee reach inside a zone. “Near” means same zone; “short” means one adjacent zone; “long” means up to three connected visible zones. Movement between visible zones is not teleportation. Cover, vertical routes, hazards and chokepoints can prevent a path.

### 5.2 Hit confirmation and defenses

Physical or Precision hit = 1d20 + Agility + relevant proficiency + floor(Level ÷ 2) + modifiers.

Evasion Value = 8 + Agility + Level ÷ 2.

Defense Target = Evasion Value + Armor Rating + situational modifiers.

The attacker’s Level contribution is an explicit reconstruction repair: it counters the source's growing defense term without a matching accuracy term. Natural 1 misses; natural 20 hits a feasible target. Neither is a damage critical.

A Dodge Reaction costs 1 Stamina and gives +2 Defense Target against one announced attack before its roll. A Parry costs 1 Stamina and reduces raw damage by 3 from one physical melee hit; declare after confirmation and before damage. It requires a usable weapon or an unarmed style against a credible threat. A character has only one Reaction; a jutsu reaction competes with these options.

Cover gives +1 for partial, +2 for substantial, or +3 for near-total cover. Complete obstruction prevents an attack unless its technique can penetrate or go around it.

### 5.3 Damage

Resolve in this order: hit or effect confirmation → raw damage → Damage Resistance → Armor Damage Reduction → Health loss → injury triggers.

Damage Resistance = floor((Strength + Stamina) ÷ 2).

Armor is deliberately removed from this formula; it already increases Defense Target and supplies separate reduction.

Armor Rating: 0 • Defense bonus: 0 • Armor Damage Reduction: 0

Armor Rating: 1 • Defense bonus: +1 • Armor Damage Reduction: 3

Armor Rating: 2 • Defense bonus: +2 • Armor Damage Reduction: 5

Armor Rating: 3 • Defense bonus: +3 • Armor Damage Reduction: 7

Armor Rating: 4 • Defense bonus: +4 • Armor Damage Reduction: 9

Armor Rating: 5 • Defense bonus: +5 • Armor Damage Reduction: 11

Additional armor rating above 5 adds 2 reduction per point but requires a specific advanced item. Standard player equipment stops at rating 3. A successful damaging attack inflicts at least 1 Health after mitigation. Nondamaging effects, failed attacks and complete obstruction do not inflict this minimum.

Elemental damage ignores up to 2 Damage Resistance. True damage ignores Damage Resistance only; it still faces armor unless the effect explicitly says otherwise. Damage resistance cannot become negative. Apply each layer once.

Optional armor degradation: after resolving a hit whose damage after Damage Resistance is at least 10, reduce Armor Rating by 1 for later attacks. The current hit uses the old rating. Repair restores the item's original rating; never increases it.

### 5.4 Taijutsu

Strike: Light • Raw base: 1d6 + Strength • Stamina cost: 1

Strike: Standard • Raw base: 1d8 + Strength • Stamina cost: 2

Strike: Heavy • Raw base: 1d10 + Strength • Stamina cost: 3

Each is one Standard Action. A weapon supplies reach or a written tag, not a second damage pool. Use Taijutsu or Weaponry proficiency as appropriate, never both.

Add flat Strength scaling: max(0, Strength − 1) × 3.

Add mastery dice of the same size as the strike: +0 at Levels 1–5, +1 at 6–10, +2 at 11–15, +3 at 16–20. Then add Expert +1 or Master +2 Taijutsu/Weaponry dice. This scaling does not transfer to Ninjutsu.

### 5.5 Control, suppression and teamwork

Grapple: Standard Action, 2 Stamina; use a physical hit roll with Strength instead of Agility if desired. Success Grapples the target until released or escaped. The target cannot change zone, use ranged attacks, or form hand seals, and suffers −2 Defense Target. The grappler must remain engaged and commit one hand; moving away ends it.

Escape: Standard Action, 1 Stamina; 2d6 + Strength or Agility + Escape/Resist against the grappler's Fortitude Threshold. Success ends the grapple. A grappler does not get a free damaging attack.

Pin: while Grappling, spend a Standard Action and 2 Stamina; test Strength + Taijutsu against target Fortitude Threshold +2. A Pinned target is Restrained and may use its Standard Action only to attempt escape. Escape uses the same threshold +2.

Suppress: Standard Action, 1 Stamina and appropriate ammunition or the written chakra cost; test 2d6 + Agility + Throwing/Weaponry, or Sensitivity + Ninjutsu, against DC 9. Success suppresses one visible enemy in range until your next turn. Its movement and physical Standard Actions each cost +1 Stamina and its Defense Target is −1. Suppression itself deals no damage.

A coordinated attack uses Aid or separate turns. It never adds an extra unpriced attack or damage pool. A readied Standard Action names one trigger; it consumes your Reaction when executed and expires at your next turn.

Source basis: S01–S02, restored turn concepts S18/S31. Turn definition, accuracy scaling, reactions, single armor contribution and control completion are R14–R18.


### Core v3.2 receiving boundary — Chapter 5 (SNWE R0.3 proposed binding)

> Core §§47–54 supply feasibility, position, coverage and effect ownership; §§10–11 retain chronological response accounting. SSN §5 alone supplies the active hit, defense, damage and armor numeric chain. Core/Fantasy/Historical hit/injury adapters cannot be added again. Health chip damage is a gameplay result, not proof of penetration.

## 6. Jutsu, synthesis and a starter catalogue

### 6.1 Technique record and activation

Every usable technique records: name, discipline, rank, affinity/access, action, range, targets or area, cost, roll/defense, effect, duration, upkeep, counterplay, and special risk. Tags alone do not supply mechanics.

For a chakra technique:

1\. Initiate: verify access, action, legal targets and enough current Chakra Units for the full cost.

2\. Commit: pay cost, increase the rank counter, and count output. No refund on failure.

3\. Mold: make its 2d6 activation test.

4\. Release: for Precision techniques make a d20 hit roll; Force techniques use their Mold result as effect confirmation.

5\. Resolve mitigation, conditions, duration, and stated risk.

Mold DC for Precision is 7. Force uses Band Delta DC. Genjutsu uses Resolve Score and does not make a second d20 roll. Fūinjutsu uses Band Delta DC or the target's stated mental/physical threshold. No technique makes duplicate checks for the same purpose.

On a failed Mold the effect does not occur. Critical failure adds 1 Trauma in addition to any specifically required synthesis consequence. A Precision miss has no effect and still costs Chakra.

Rank: E • Raw damage for a damaging technique: 1d4

Rank: D • Raw damage for a damaging technique: 1d6

Rank: C • Raw damage for a damaging technique: 2d6

Rank: B • Raw damage for a damaging technique: 3d6

Rank: A • Raw damage for a damaging technique: 4d6

Rank: S • Raw damage for a damaging technique: 5d6

A control, healing, barrier, or utility effect does not receive these damage dice for free. An S-rank activation adds 1 Trauma whether it succeeds or fails. SS- and X-rank legacy techniques require individually priced mythic scenarios; they are not ordinary learned combat entries in this base.

### 6.2 Discipline boundaries

Ninjutsu Mold uses Intelligence, Wisdom, or Sensitivity, fixed when the technique is written. Precision release uses the normal d20 accuracy formula and Ninjutsu proficiency. Force can target an area only if the record specifies one. By default a Force wave affects at most two adjacent targets in one visible zone, allies included.

Genjutsu uses Wisdom or Sensitivity + Genjutsu against Resolve Score. It changes perception or imposes a written condition; it does not directly reduce Health. A target or assisting ally can spend a Standard Action to break it: 2d6 + Willpower or Constitution against the original activation total. Upkeep is 1 Chakra per turn after the first. Stopping upkeep ends it. Broken line of sight alone does not end a sustained illusion.

Fūinjutsu uses Intelligence + Fūinjutsu against the indicated threshold. A mobile or resisting subject must be touched, restrained, or caught by an explicitly ranged seal. Baseline duration: D one round, C two, B three, A one scene. Long-term permanent seals require a research project and a defined removal method.

Summoning requires a contract, a technique record, and a creature stat block. A summoned ally does not generate an unlimited extra turn: commanding it uses the summoner's Standard Action; it uses its own statistics and one Reaction. Maintain a single active combat summon per character in R0.1.

### 6.3 Synthesis

Combining two or more affinities requires known component affinities and Synthesis proficiency. Test 2d6 + Sensitivity + Synthesis against 9 + 2 per affinity beyond the first +2 if A-rank or higher.

A listed inherited fusion removes the extra-affinity modifier for that exact combination, not the high-rank modifier or all risk. The synthesis test replaces the normal Mold test; it is not an extra test on top of Mold. Precision release still needs its hit roll.

Failure by less than 3 adds 1 Trauma; failure by 3 to less than 5 adds 2 Trauma; failure by 5+ triggers an Injury Check. The effect fails. A double-one complication adds 1 additional Trauma. No failure erases the resource payment.

Hybrid physical/chakra techniques pay both their stated Stamina and Chakra costs, use synthesis for Mold, a Taijutsu hit for release, and the rank's Ninjutsu damage only. They do not also add a full Taijutsu strike's damage.

Elemental advantage follows Fire → Wind → Lightning → Earth → Water → Fire. When opposed techniques directly clash, the advantaged element receives +1 on its opposed 2d6 test, within the situational cap. No automatic 1.5× damage is imported. Unopposed attacks receive no advantage merely for belonging to an element.

### 6.4 Starter techniques

The following are R0.1 adaptations, not verbatim restorations of all old jutsu entries. All chakra costs use the rank table plus escalation. “Standard” means one Standard Action. Unless noted, they use Sensitivity to Mold and normal discipline rules.

Technique: Transformation • Rank / discipline: E / Ninjutsu • Action and range: Standard; self • Operating effect: Mold DC 7. Change visual appearance for a scene; inspection is Perception against activation total. No physical capabilities copied.

Technique: Illusory Clone • Rank / discipline: E / Genjutsu • Action and range: Standard; near • Operating effect: Resolve test against one observer. On success impose −1 on its next attack before your next turn. No independent actions or damage.

Technique: Chakra Adhesion • Rank / discipline: E / Ninjutsu • Action and range: Standard; self • Operating effect: Mold DC 7. Cling to a surface for a scene; still pay normal movement. Carry no more than normal load.

Technique: Spark / Pebble / Droplet • Rank / discipline: E / Ninjutsu • Action and range: Standard; short • Operating effect: Precision; 1d4 elemental damage. Choose known affinity when learned.

Technique: Substitution • Rank / discipline: D / Ninjutsu • Action and range: Reaction; self • Operating effect: Declare before hit roll; Mold DC 7 and pay 1 Stamina. Gain +2 Defense against that attack, then move within your zone to available cover. No automatic escape from a pin.

Technique: Body Flicker • Rank / discipline: D / Ninjutsu • Action and range: Standard; self • Operating effect: Mold DC 7; move two traversable zones. Does not pass through walls or release a grapple.

Technique: Field Mending • Rank / discipline: D / Ninjutsu • Action and range: Standard; touch • Operating effect: Intelligence + Medicine DC 9; restore 1d6 Health. One successful application per target per scene. Does not cure Injury.

Technique: Chakra Bolt • Rank / discipline: D / Ninjutsu • Action and range: Standard; short • Operating effect: Precision; 1d6 elemental damage.

Technique: Binding Slip • Rank / discipline: D / Fūinjutsu • Action and range: Standard; touch • Operating effect: Against Fortitude. On success target is Grappled for one round by the seal, with escape against activation total.

Technique: Elemental Projectile • Rank / discipline: C / Ninjutsu • Action and range: Standard; short • Operating effect: Precision; 2d6 elemental damage to one target.

Technique: Elemental Wave • Rank / discipline: C / Ninjutsu • Action and range: Standard; near/short • Operating effect: Force; at most two adjacent targets in one zone, 2d6 elemental damage each. Roll Mold once; compare against each Band DC.

Technique: Smoke Veil • Rank / discipline: C / Ninjutsu • Action and range: Standard; near • Operating effect: Force; fill one zone with concealment for two rounds. Ranged attacks through it take −2; it provides no armor.

Technique: False Opening • Rank / discipline: C / Genjutsu • Action and range: Standard; short • Operating effect: Resolve test; target is Distracted (−1 to rolls) for two rounds, with normal break action. No direct damage.

Technique: Restraining Seal • Rank / discipline: C / Fūinjutsu • Action and range: Standard; touch • Operating effect: Against Fortitude; Restrained for two rounds. Escape Standard Action against original activation total.

Technique: Earthen Screen • Rank / discipline: C / Ninjutsu • Action and range: Standard; near • Operating effect: Mold DC 9; create cover +2 for two rounds, enough for two allies. Screen has 12 Health, no resistance or armor.

Technique: Piercing Lance • Rank / discipline: B / Ninjutsu • Action and range: Standard; short • Operating effect: Precision; 3d6 elemental damage. “Piercing” is the fiction, not extra armor bypass.

Technique: Broad Barrier • Rank / discipline: B / Ninjutsu • Action and range: Standard; near • Operating effect: Mold DC 11; barrier has 20 Health, lasts three rounds and blocks a doorway or route. Attacks may target barrier; it has no mitigation.

Technique: Great Elemental Release • Rank / discipline: A / Ninjutsu • Action and range: Standard; long • Operating effect: Force; two targets in one zone, 4d6 elemental damage each. May ignite, soak or disrupt terrain only as a recorded non-damaging scene tag.

A character can learn an affinity-neutral technique or one matching an affinity they know. Genjutsu, seals and medicine also require the appropriate proficiency/access. Renaming a starter does not change its statistics. Named setting techniques, bloodline abilities and the hundreds of legacy entries remain preserved for individual conversion; no universal CU divisor can safely convert them.

Source basis: S01, S37, S41–S43. Activation payment, starter records, summons and conversion boundary are R19–R22.


### Core v3.2 receiving boundary — Chapter 6 (SNWE R0.3 proposed binding)

> Core §5 stages, §55 manifestation/embodiment and §112 extraordinary contracts underpin downstream records. The SSN technique and its exact activation sequence remain authoritative. SCL 1.0 ordinary equipment families carry no jutsu statistics.

## 7. Injury, Trauma, Stress and recovery

### 7.1 Conditions

Condition: Exposed • Effect: +5 incoming raw damage; no Dodge/Parry if caused by zero Stamina • Removal: Regain Stamina, or stated effect ends

Condition: Distracted • Effect: −1 to rolls • Removal: Effect duration or source removed

Condition: Prone • Effect: −3 Defense Target; cannot Dash • Removal: Minor Action and 1 Stamina to stand

Condition: Grappled • Effect: Movement zero, −2 Defense, no ranged attacks or hand seals • Removal: Escape, grappler releases, or separation

Condition: Restrained • Effect: Movement zero, −5 Defense; only escape as Standard Action • Removal: Escape or restraint destroyed

Condition: Suppressed • Effect: −1 Defense; +1 Stamina for movement and physical Standard Actions • Removal: End of suppressor's next turn or break line of effect

Condition: Downed • Effect: At zero Health; no ordinary Standard Actions or movement • Removal: Stabilize and recover Health

Condition: Concealed • Effect: Attacks through concealment take −2 • Removal: Clear sight or leave concealment

Grappled and Restrained defense penalties do not add together; use −5. Multiple sources of the same condition do not stack. Condition duration is counted in the source's turns unless explicitly stated.

### 7.2 Injury checks

Make one Injury Check per damaging event if any of these occurs: the final Health loss is at least 25% of maximum Health; you cross from above half Health to half or below for the first time this scene; or you reach zero Health.

2d6 + Constitution + Level ÷ 2 against Injury DC 9.

Add +2 DC for a Heavy Strike or A/S-rank damaging effect, +2 if armor reduction was explicitly bypassed, and +2 if already Injured. These modifiers stack. Several triggers from one hit still cause one check.

Failure by less than 3 causes a Minor Injury; failure by 3 to less than 5 a Major Injury; failure by 5+ a Critical Injury. The second and later failed Injury Checks in the same scene raise severity one step, maximum Critical.

Minor: −1 on physical checks using an affected body region. Major: −2 on those checks, movement halved, no Heavy Strike; add 1 Trauma. Critical: incapacitated and in need of stabilization. These are task penalties, not reductions to the stored statistics; do not recalculate maxima and start a recursive injury cascade.

Reaching zero Health adds 2 Trauma. Further damaging hits while Downed require 2d6 + Constitution against DC 9; failure means death unless immediately prevented by Destiny or an already-established protection. Agree lethal or nonlethal campaign consequences before play. Nonlethal mode substitutes capture or a lasting consequence, not free recovery.

### 7.3 Trauma

Trauma Capacity = Constitution + Willpower.

Trauma relative to capacity: At or below capacity • State: Stable; no penalty

Trauma relative to capacity: Above capacity, up to capacity +2 • State: Strained; −1 to rolls

Trauma relative to capacity: Above capacity +2, up to capacity +4 • State: Fractured; −2 to rolls; cannot activate S-rank techniques

Trauma relative to capacity: Above capacity +4 • State: Broken; unable to continue the scene

These continuous intervals work with half-point capacity. Broken does not automatically mean dead or retired. Resolve treatment, withdrawal, and lasting consequences after the scene.

Gain Trauma from zero Health, Major Injury, S-rank use, Overclock, synthesis, and specifically written effects. One incident can have different causes—for example an S-rank cast also crossing Overclock—but do not charge the same cause twice.

### 7.4 Mental Resilience and Internal Chakra System

R0.1 retains MRICS as the interface for acute mental strain, not as a second competing Trauma engine. Stress is a short-term track. Stress Threshold = Willpower + Wisdom.

Gain 1 Stress from a declared mental shock or failed hazardous investigation, 2 from witnessing a bonded ally's death, and 2 from DSSN backlash. Ordinary failed Athletics or Stealth checks do not automatically cause Stress. Apply the most severe listed mental-shock trigger once per event.

When Stress crosses above the threshold, test 2d6 + Willpower + Insight against DC 11. Success contains the episode. Failure adds 1 Trauma and makes the character Distracted until a safe break. Reset Stress to the threshold after either result, so another event can test resilience again. An hour of safe rest, meditation or supportive care removes 1 Stress; safe sleep clears it.

This replaces the incompatible legacy /7 percentage track, ten-points-per-band track and derived-Willpower formulas. Lasting scars remain descriptive commitments with explicitly agreed triggers; they do not silently seize player control.

### 7.5 Treatment

A medical action consumes one kit use when available. Without appropriate tools, treatment has Disadvantage; impossible surgery still needs facilities.

Treatment: Stabilize • Test and time: Intelligence + Medicine DC 9; Standard Action • Success: Stops deterioration; remains at zero Health and unable to fight until healed

Treatment: Treat Major Injury • Test and time: Intelligence + Medicine DC 11; one hour • Success: Downgrades it to Minor; once per injury per day

Treatment: Immediate Minor treatment • Test and time: Intelligence + Medicine DC 13; ten minutes • Success: Removes one Minor Injury

Treatment: Treat Critical Injury • Test and time: Intelligence + Medicine DC 13; one day with facilities • Success: Downgrades to Major

Treatment: Support or meditation • Test and time: Wisdom + Insight DC 9; ten-minute safe rest • Success: Removes 1 Trauma; once per character per day

Two safe days of rest remove one Minor Injury and reduce Trauma to capacity if above it. They do not heal untreated Major or Critical Injuries. Daily support can reduce Trauma below capacity. Rest restores Health and Chakra at the rates in Chapter 4; injury treatment and pool recovery are different.

Source basis: S02, S20 and S31. Severity, fractional boundaries, MRICS bridge and treatment timing are R23–R25.


### Core v3.2 receiving boundary — Chapter 7 (SNWE R0.3 proposed binding)

> Core §§17–19 and MED §118 own unified continuing conditions, care work and exposures. R0.1 Health, Injury, Stress, MRICS, Trauma, timing and numeric treatment effects remain the active selected interpretation, with no second healing/injury counter.

## 8. Development, classes, paths and institutions

### 8.1 Advancement

Award a milestone for a completed consequential objective or personal arc, not for repeating safe rolls. A substantial partial contribution can earn a half-milestone; two halves equal one. Every complete milestone raises Level by one, maximum 20, and grants one +0.5 increase to a statistic other than Chakra Reserves, subject to cap. If no legal increase is available, bank it until a later cap permits it.

Also gain one proficiency step and learn one technique within access limits, supported by a mentor, scroll, research or demonstrated training. A proficiency step raises one entry by one tier. Expert requires Level 6; Master requires Level 12. A character's formal instruction need not happen inside combat.

Level: 1 • Statistic cap: 2.5 • Usual technique ceiling: D • Maximum eligible Character Band: 1

Level: 2–3 • Statistic cap: 3.5 • Usual technique ceiling: C • Maximum eligible Character Band: ceil(Level ÷ 2)

Level: 4–5 • Statistic cap: 4 • Usual technique ceiling: C at 4; B at 5 • Maximum eligible Character Band: ceil(Level ÷ 2)

Level: 6–7 • Statistic cap: 5 • Usual technique ceiling: B • Maximum eligible Character Band: ceil(Level ÷ 2)

Level: 8–9 • Statistic cap: 5.5 • Usual technique ceiling: B at 8; A at 9 • Maximum eligible Character Band: ceil(Level ÷ 2)

Level: 10–11 • Statistic cap: 6 • Usual technique ceiling: A • Maximum eligible Character Band: ceil(Level ÷ 2)

Level: 12 • Statistic cap: 6.5 • Usual technique ceiling: A • Maximum eligible Character Band: 6

Level: 13–15 • Statistic cap: 7 • Usual technique ceiling: S • Maximum eligible Character Band: ceil(Level ÷ 2)

Level: 16–20 • Statistic cap: 7 • Usual technique ceiling: S; mythic rituals individually defined • Maximum eligible Character Band: ceil(Level ÷ 2)

Band ascension also requires a demonstrated scale-changing achievement. It is not an automatic flat bonus with Level. The GM records the achievement and new Band. No Band \>10 or statistic \>7 is a standard player progression rule in this edition.

### 8.2 Class framework

Choose one class at Level 3. Class features occur at Levels 3, 5, 7, 9, and 11. They remain known after selecting a Path. The following small feature sets are new operating implementations of the Lexicon's six named class frameworks.

Class: Taijutsu Adept • Level 3: Once/scene reduce a strike cost by 1, minimum 1 • Level 5: Learn one additional physical technique record • Level 7: Once/scene Parry reduces 5 instead of 3 • Level 9: On a hit, pay 1 Stamina to push target within the zone; once/turn • Level 11: Once/scene replace a Standard strike with a Heavy strike at Standard cost

Class: Ninjutsu Specialist • Level 3: Once/scene gain Advantage on Mold • Level 5: Learn one extra elemental technique • Level 7: Once/scene ignore one repeat's Escalation Tax; still increment counter • Level 9: Once/scene a failed noncritical Mold may create concealment instead of its effect until your next turn • Level 11: Once/scene sustain your existing barrier one extra round for 2 Chakra

Class: Genjutsu Practitioner • Level 3: Once/scene extend a successful illusion by one round, paying upkeep • Level 5: Learn one additional illusion • Level 7: Once/scene waive 1 Chakra of upkeep • Level 9: You may willingly end an illusion to learn which sense the target distrusted; narrative information only • Level 11: Once/scene target a second adjacent subject; pay two full activation costs, resolve separately

Class: Fūinjutsu Savant • Level 3: Prepare one seal during downtime; deploy as Standard with normal costs • Level 5: Learn one additional seal • Level 7: Once/scene sustain an expiring seal for one round at 2 Chakra • Level 9: Recognize visible seal purpose with Intelligence + Sealing Arts DC 9, Standard Action • Level 11: Once/scene prepare a seal trigger during combat, paying its normal action and cost in advance

Class: Field Operative • Level 3: Once/scene Dash for zero Stamina • Level 5: Gain one new Proficient investigative skill • Level 7: Once/scene use a Minor Action to Aid a Stealth or Perception check • Level 9: Once/scene spend Reaction to move within your zone after an enemy misses • Level 11: Once/scene lead up to two willing allies through one traversable zone using your Standard; they each pay 1 Stamina

Class: Tactician • Level 3: Once/scene successful Aid gives +2 instead of +1 to a d20 attack • Level 5: Gain Tactics Proficient or one step within cap • Level 7: Once/scene switch initiative positions with a willing ally at round start • Level 9: Once/scene spend Standard to remove Suppressed from one ally who can hear you • Level 11: Once/scene give one willing ally your Standard Action; they act immediately and pay all their own costs

Additional learned techniques must still meet rank/access gates. A class cannot create missing powers by implication. Once-per-scene means one use of that specific feature, not one use of every possible interpretation.

### 8.3 Paths

At Level 12+ select one Path after a qualifying arc. A Path is permanent unless a major story event changes it. The starter Paths are deliberately narrow:

- Martial: once per scene add one strike die to a physical hit by taking 1 Trauma and paying +2 Stamina.

- Chakra: once per scene replace a technique's fixed casting statistic with another of Intelligence, Wisdom or Sensitivity before rolling; pay +2 Chakra.

- Strategic: once per battle use a Rally order without consuming the commander's unit action; spend 1 Destiny and incur its Toll.

- Forbidden: once per arc use one specifically documented technique one rank above normal access, maximum S; pay double final Chakra cost and take 2 Trauma in addition to other risk. It still needs to be learned. No free access to DSSN.

These are reconstruction options, not claims that every legacy prestige tree has been converted.

### 8.4 Rank, ANBU and civilian professions

Use Civilian, Academy, Junior/Senior Genin, Junior/Senior Chūnin, Tokubetsu Jōnin, Junior/Elite Jōnin and setting-specific leadership titles. Rank requires appointment, examinations, vacancies or political trust. Typical associations follow the old ladder but confer no stat changes.

ANBU is an assignment overlay: covert authority, issued equipment, secrecy obligations and a handler. It is neither a universal rank above Jōnin nor a source of free stats. Medical, intelligence, logistics, teaching and crafting occupations provide contacts and job access; mechanical benefits come from skills and written features.

A player can be a strong low-ranking operative or a politically important weak official. Leadership and power are not interchangeable.

Source basis: S01–S02, S20, S31. Advancement bridge, active class features, Paths and ANBU separation are R26–R28.


### Core v3.2 receiving boundary — Chapter 8 (SNWE R0.3 proposed binding)

> Core LIFE §122, §45 and §110 keep evidence, credentials, office and institutional fielding separate. SSN levels, classes, Paths, proficiency gates, jutsu acquisition and shinobi ranks remain local rules. Promotion cannot itself create skills or equipment.

## 9. Missions, downtime, research and equipment

### 9.1 Mission cycle

Brief → prepare → travel/infiltrate → act → extract → debrief → downtime.

A briefing states objective, employer, known threat, deadline, authority, expected payment, constraints and consequences of failure. Assign a rank to risk and scope, not to a guaranteed reward.

Use a four- or six-segment objective clock and a separate four- or six-segment threat clock when time matters. Failed risky actions advance threat once; critical failures twice. At completion, the threat described in the briefing happens. A full threat clock need not cancel progress already achieved.

At debrief record who gained or lost something, resources spent, injuries, faction standing changes, exposed secrets, outstanding promises and any milestone earned. Evidence follows the fiction; no faction automatically learns a secret mission's authors.

A mission generator retained from S31 uses 2d6: 2 escort, 3 retrieval, 4 investigation, 5 elimination, 6 diplomacy, 7 reconnaissance, 8 sabotage, 9 defense, 10 disaster relief, 11 espionage, 12 mythic intervention. A mythic result outside the campaign's scale becomes a rumor, rescue or investigation around the event.

### 9.2 Downtime

After a mission, each character receives two downtime actions, each representing one meaningful activity over the available interval. Rest occurs with actual elapsed time, not merely because a box was ticked. If the fiction provides only an hour, it cannot contain a two-day convalescence.

Action: Train • Procedure: Spend action on a mentor/scroll/practice scene to justify a learned proficiency or technique; no extra stat increase

Action: Recover • Procedure: Apply Chapter 7 treatment; a healer spends their action too if providing extended care

Action: Research/Craft • Procedure: Advance a declared project clock

Action: Bond/Reflect • Procedure: Repair a relationship, establish one usable contact, or attempt the once-daily Trauma support check

Action: Work/Patrol • Procedure: Gain 1 personal Supply or contribute 1 faction Resource Point; choose one

Action: Gather Intelligence • Procedure: Intelligence/Perception + relevant skill against DC 9 or an opposed defense; gain one specific answer or advance a clock

Action: Repair • Procedure: Spend 1 Supply and pass Crafting/Repair DC 9 to restore one damaged item's original Armor Rating

No downtime action grants free Destiny by meditation, automatically promotes a character, or bypasses a Level cap.

### 9.3 Research and crafting

Write the desired output first: exact technique or item record, required rank, facilities, materials, who can use it, and what failure threatens. This is the project's contract. An undefined “legendary weapon” is not a purchasable outcome.

A standard project has six segments and DC 9; an advanced project eight and DC 11; a major/forbidden project twelve and DC 13. Use Intelligence + Crafting/Repair, Sealing Arts, Medicine or Scientific Ninja Tools as appropriate. A basic workspace is required; a specialized laboratory can supply +1 within the situational cap.

Spend 1 Supply per project action. Use the common clock procedure. At completion perform one field test against the project's DC. Success makes the agreed item reliable. Failure keeps it a prototype with a stated fault and requires two additional successful repair segments. No additional random hidden power appears.

A new jutsu is written with Chapter 6's costs, damage budget, targeting, defense and upkeep. Added targets, duration or utility must trade off against another benefit or raise rank. A prototype does not become player-ready until these numbers are written.

Forbidden research adds 1 Trauma to the lead researcher on a failed action and advances a relevant faction/world threat. This is a concrete consequence, not an automatic permission to invent unlimited effects.

### 9.4 Personal economy and gear

Personal Supply represents consumables and ordinary mission funding. One token purchases one restock: six throwing weapons, a three-use medical kit, three days of rations, or materials for one repair/project action. Unused tokens persist. Standard rewards: D mission 1 token each; C 2; B 3; A 4; S by contract. Failure pays only what the employer agreed.

Armor Rating 1 costs 2 Supply; rating 2 costs 4; rating 3 costs 7 and requires a trained armorer. A normal weapon costs 1. Specialized tags require an explicit record. Money can exist in the fiction, but the GM establishes the local conversion before shopping; this draft does not fabricate a universal ryō exchange rate.

Encumbrance is descriptive: one worn armor set, two ready weapons, and a reasonable field pack. Excess load makes Athletics and Stealth Disadvantaged and removes free zone movement until reduced. Allies, porters and storage matter.

Source basis: restorative concepts S20, S31. Clock mechanics, token pricing and research output rules are R29–R31.


### Core v3.2 receiving boundary — Chapter 9 (SNWE R0.3 proposed binding)

> Core §§73, 96, 114, 111–112 handle real work, actual elapsed time, claims, stock and content. Native R0.1 abstract Supply/project/downtime procedures remain operable only within the declared abstract mode; persistent mode requires an explicit nonduplicating bridge.

## 10. Social conflict, standing and ideology

Social play begins with a concrete request, leverage and what the other party wants. Ordinary conversation needs no roll. Impossible demands do not become possible because a player rolled well.

Pressure Capacity = 2 × (Willpower + Charisma). Track accumulated Pressure from zero for the encounter.

Test Charisma + Persuasion/Intimidation/Politics, Intelligence + an appropriate evidence-based skill, or another justified pairing against Resolve Score. Success applies max(1, floor(Margin)) Pressure, capped at 4 per action. Critical success adds 1 Pressure beyond that cap. Repeating the same argument cannot generate more Pressure without new evidence or changed stakes.

At capacity, the target must make a meaningful decision within the established stakes: concede part of the request, offer a bargain, withdraw, or accept a stated reputational cost. This is not mind control. Players retain choices about their character's beliefs and personal commitments. Genjutsu is a separate discipline.

Pressure clears after a safe break; written concessions, promises, evidence and consequences remain. Violence ends the negotiation or changes its stakes, not automatically wins it.

Faction Standing ranges from −3 hostile to +3 trusted, with 0 neutral. Significant public help raises it one step; verified betrayal lowers it one or two. Use it to determine access, suspicion and available contacts. It does not become an uncapped bonus on every social roll. At most a relevant contact grants the normal Aid benefit.

Record reputation separately as factual tags—“defended the bridge,” “oath-breaker,” “unknown masked scout”—including who knows them. The same act may earn trust with one faction and hostility with another.

Ideology is represented by a creed, commitment, temptation and obligation. Keep legacy Harmony/Ambition/Discipline/Chaos language if useful to the setting, but do not run a second numerical morality engine. Acting on a costly creed can justify a milestone or Destiny award; neither is automatic or farmable.

Source basis: S02, S29, S31. Pressure closure, standing and ideology bridge are R32–R33.


### Core v3.2 receiving boundary — Chapter 10 (SNWE R0.3 proposed binding)

> Core §66 and LIFE §122 own relationships and audience-scoped evidence. Retain R0.1 numerical Pressure, Standing and creed effects. Pressure never authors a player character voluntary choice, and a second Core persuasion meter does not run.

## 11. Destiny, bloodlines, artifacts and the Spiral

### 11.1 Destiny and Karma

Begin with 1 Destiny Point. Award another for an irreversible sacrifice, major arc resolution, or accepting a major consequence that changes the character's future. No roll or routine rest regenerates Destiny.

Spend 1 Destiny to do one of the following:

- Turn one failed feasible task into Margin 0 success.

- Avoid immediate death, stabilize at 1 Health, and leave the immediate danger by a plausible rescue or concession.

- Establish one justified flashback fact that does not contradict recorded events.

The death option does not remove Injury, Trauma, debts or capture. Destiny cannot erase a consequence created by Destiny. One event receives at most one Destiny intervention per character.

Every spent point creates one Toll. Resolve it immediately as a meaningful obligation, lost opportunity, sacrifice or exposure, or add 1 unresolved imbalance to the Karma Ledger. The player and GM write what settles it.

At 3, 6 and 9 unresolved imbalance, advance the six-segment World Clock one segment. Each threshold fires once until the ledger drops below it; do not retrigger it every turn. Beyond 9, every additional three imbalance adds another segment. Settling a Toll reduces imbalance by one but never reverses a World Clock consequence already resolved.

At six World Clock segments, resolve the forecast campaign event, record it and begin a new clock with a new consequence.

### 11.2 Heritage and legacy

A bloodline records name, lineage, Grade 1–7, access tags, inherited techniques, an obligation or vulnerability, awakening condition and current generation. Grade describes rarity and scope; it does not add to statistics or rolls.

At creation a bloodline may replace one starter technique with a heritage technique of equal permitted rank. It may also give access to an exact fused affinity; learning and using it still follows synthesis. No free second skill, stat array or chakra multiplier is bundled into heritage. A clanless character instead records one contact and one equally significant obligation.

At death, retirement or a long timeskip, build the successor normally. Choose or roll one item from each list:

- Gift (d6): 1–2 a permitted inherited technique; 3–4 a mentor or bond; 5–6 a latent heritage access tag.

- Burden (d6): 1–2 a rival; 3–4 an oath/debt; 5–6 a curse or sealed legacy requiring an arc.

- Event (d6): succession dispute, political marriage/adoption, lost archive, exile, clan schism, external crisis.

An inherited technique occupies normal access and learning allowances. No inherited Rank, full XP pool or automatic statistic increase. Record the predecessor's deeds and unresolved costs in the Legacy Tracker. A curse has an agreed trigger and removal route; a narrative scar is not automatically a new numeric penalty.

### 11.3 Artifacts and resonance

An artifact has one primary effect written as a technique, an activation cost, access requirement, bond clock, consequence, and failure/removal condition. Start with a four-segment bond project at DC 9; advanced artifacts use six/DC 11 or eight/DC 13.

Bonding grants permission to use the effect, not free resources. The wielder pays its normal costs and uses normal defenses. A device with a separate battery records its capacity and recharge method explicitly; no unpriced battery exists by default.

On a critical activation failure, mark one Instability on the artifact and take the normal complication. At three Instability it becomes dormant until a four-segment repair/reconciliation project is completed. A cursed artifact may replace dormancy with a written consequence agreed at discovery. Destroying, stealing, inheriting or breaking a bond changes the world record.

This retains artifact relationships and risks while retiring incompatible 0–100 Sync and percentage multipliers from the active core.

### 11.4 Divine Spiral Seal Network

DSSN is an optional mythic campaign module. Enabling it is a campaign premise, not a benefit gained merely by leveling.

Record a Core Node, each Auxiliary or Forbidden Node, Network Grade 1–7, a six-segment Instability Clock, and the affected people/places. A miracle requires a written event contract: intended change, reach, prerequisites, Destiny cost, irreversible Toll, clock advance, counterplay, and catastrophe.

Every activation costs at least 1 Destiny Point, creates its Toll, advances Node Instability at least one segment and advances the World Clock at least one segment. The GM may require more before the player commits. At full Node Instability, a stated catastrophe occurs: node failure, mutation, loss of access, faction crisis or an era-scale event. Resetting the clock requires a defined stabilization arc; it is not an ordinary rest.

DSSN may exceed normal scale only within its event contract. It is not an unlimited attack that ignores every defense on demand. Resurrection, erasure and timeline change demand explicit stakes and a campaign record. A miracle cannot retrospectively erase its own Toll.

Source basis: S02–S03, S20, S31. Inheritance procedure, artifact normalization and DSSN event contract are R34–R36.


### Core v3.2 receiving boundary — Chapter 11 (SNWE R0.3 proposed binding)

> Core §§79/99/112 distinguish compatible establishment, authorized exception, prospective correction and actual retcon. SSN Destiny/Toll/Karma/DSSN thresholds and artifact mechanics are unchanged; their extraordinary effects apply only by written contract.

## 12. Organizations, war and the Era Engine

### 12.1 Keep scales separate

A unit is an organized body of combatants. Its ratings are integer 1–7: Power, Defense, Skill, Morale and Supply. It also records current/initial Strength, commander, tags, role and actual headcount when known.

Standard text retains cells of 3 Genin plus a Jōnin; assault teams of 4–6; reconnaissance groups of 2–4; medical groups of 3–5 plus protection; and sealing groups of 4–6. Larger formations are built from these components. Do not invent a universal platoon size for every village.

For the abstract battle procedure, Strength is a track: Small 4, Medium 6, Large 8, Extra-large 10. These are formation endurance points, not individual hit points or literal headcount. Record both if casualty precision matters.

Sample units:

- Recon cell: Power 2, Defense 2, Skill 4, Morale 3, Supply 3, Strength 4; Scout tag.

- Assault detachment: Power 4, Defense 3, Skill 3, Morale 4, Supply 4, Strength 6.

- Sealing corps: Power 2, Defense 4, Skill 4, Morale 3, Supply 3, Strength 4; Seal tag.

- Medical support: Power 1, Defense 2, Skill 4, Morale 4, Supply 4, Strength 4; Medical tag.

These are reconstruction sample stat blocks, not a claim that legacy formations have been numerically converted.

### 12.2 Battle phase

One phase represents a meaningful exchange—usually minutes, but agreed before battle. Use fronts or zones, objectives, supply routes and exit routes.

1\. Command: each unit selects Attack, Hold, Support, Maneuver, Rally or Withdraw.

2\. Action: units act in descending current Morale; ties favor defenders. One action per unit.

3\. Consequence: apply Strength losses, test morale, resolve objectives.

4\. Logistics: at the end of every third phase, engaged units consume 1 Supply.

5\. Record: update control, casualties requiring aid, prisoners, routes and clocks.

Attack: 2d6 + Power + one relevant tactical modifier against 7 + enemy Defense. On success remove 1 Strength, 2 at Margin 3+, or 3 on double sixes. The critical replaces the loss quantity, not adds to it.

Hold: give the unit +1 effective Defense until its next action and forgo attack. Maneuver: Skill DC 9 to change one zone, flank or secure a route; terrain may change the DC by up to 3.

Support: Skill DC 9; give one ally Advantage on its next 2d6 action, or with Medical tag restore 1 lost Strength once per ally per battle. This represents returning scattered/treatable troops, not resurrecting casualties. Supply support transfers one actual Supply from the helper to the recipient; it does not create supplies.

Rally: Morale DC 9; restore 1 Morale, maximum initial Morale. Withdraw: move toward a viable exit; if threatened, Skill against 7 + enemy Skill. Failure loses 1 Strength and retreats only to the next safe position.

Morale check: 2d6 + current Morale against DC 9 after losing at least one quarter of initial Strength in a phase, commander defeat, or a catastrophic event. Failure loses 1 Morale; failure by 3+ also forces withdrawal. At Morale zero, the unit routs or surrenders.

At Strength zero the unit is combat-ineffective and cannot act. Survivors, wounded and prisoners are settled from the battle circumstances; zero Strength does not mean every person is dead.

Supply at 1–2 prevents army-scale techniques and advanced Support. At zero, the unit cannot Attack and must Withdraw, Hold or seek resupply; each subsequent logistics step costs 1 Strength and 1 Morale. This supplies an operative consequence for the Lexicon's undefined “collapse.”

### 12.3 Terrain, forces and command

Give the field up to three tags. A relevant tag supplies +1 or −1, with combined tactical modifiers capped at ±3. Flanking requires actual access to a second approach; a label alone is not a bonus.

Fortifications supply +1 to +3 Defense according to prepared works. A Siege-tag unit may make Skill against 9 + fortification bonus; success reduces that bonus by 1.

Naval units need navigable water and supply access; aerial units can cross certain blocked routes but consume 1 additional Supply at each logistics step. They remain vulnerable to appropriate counters. A summon is a unit only if assigned a complete unit block and an upkeep source.

A commander cannot issue orders they cannot communicate. A defeated commander forces a morale test; a named deputy can assume command next phase. Veteran status is a narrative quality translated into the unit's existing Skill/Morale ratings, not an additional stacking dice pool.

A Legendary Action costs 1 Destiny with its Toll: immediately Rally once, shift one unit to an adjacent reachable zone, or let one unit Hold before an incoming attack. One per army per phase. Instant world-spanning redeployment requires DSSN, not this option.

An army's reported average Power/Defense, lowest Morale and median Supply are summaries only. Resolve either constituent units or a single deliberately authored army block, never both for the same exchange.

### 12.4 Player missions affect war

Before a PC scene, write its battle consequence: destroy a depot (−1 enemy Supply), rescue a commander (avoid loss test), breach a gate (remove one fortification point), or secure a route (permit resupply). Apply the result once. Personal Chakra damage cannot be multiplied into arbitrary troop casualties.

After battle record territorial control, losses, medical needs, prisoners, supply consumption, commander status and changes in faction standing. Reinforcements restore Strength only when people and time arrive; they do not automatically restore veteran Skill.

### 12.5 Factions and Era turns

A faction records Resources rating 1–7, Morale 1–7, Influence 1–7, Secrecy 1–7, a Resource Point pool, goals, allies, rivals, and project clocks. These are separate from individual Social Pressure or Chakra.

An Era turn is three in-world months; active wars may use a shorter agreed interval with proportionately reduced income/upkeep. Never advance both calendars independently.

At a three-month turn:

1\. Gain 1d6 × Resources Resource Points.

2\. Pay 5 per maintained army and 5 per major ongoing project.

3\. Choose up to three affordable orders.

4\. Resolve one roll per uncertain order and update clocks, standing and events.

Order: Deploy • Cost: 20 RP • Resolution: Place an available army on a reachable front; does not conjure new recruits

Order: Reinforce • Cost: 10 RP • Resolution: Restore 1 unit Strength if recruits and route exist

Order: Research • Cost: 15 RP • Resolution: Add one segment to an established research project

Order: Diplomacy • Cost: 5 RP • Resolution: 2d6 + Influence against 7 + opposing Influence; success opens a concrete treaty opportunity

Order: Espionage • Cost: 8 RP • Resolution: 2d6 + Secrecy against 7 + opposing Secrecy; success reveals one plan or advances sabotage

Order: Resupply • Cost: 5 RP • Resolution: Restore 1 Supply to one connected unit, maximum initial rating

Unaffordable upkeep places an army/project at risk: mark an unrest clock or suspend the project; never spend negative Resource Points. Three-month income cannot be collected each combat round.

For NPC factions, choose an order consistent with their goal and known information. If uncertain, roll d6: 1 defend, 2 consolidate, 3 research, 4 negotiate, 5 covert action, 6 expansion. Apply affordability and access. The faction does not know hidden PC facts without a source.

Use the World Clock to introduce an event when due: disaster, succession crisis, new alliance, technical discovery, DSSN disturbance or war escalation. Write concrete affected regions and factions. A clock does not authorize erasing player history.

Source basis: S03, S20, S31. The working unit engine, explicit losses/logistics and bounded strategic economy are R37–R40.


### Core v3.2 receiving boundary — Chapter 12 (SNWE R0.3 proposed binding)

> Core §§41–42, 62, 106, CIV §117 and ECO §114 own actual people, logistics, causal events and claims. SSN owns unit Power/Defense/Skill/Morale/Supply ratings, Strength and phase/Era dice. Strength does not equal literal casualties; quarterly Resource Point generation is selected once.

## 13. Running the first session

### 13.1 Worked character

Mika is a Level 2 Junior Genin, Character Band 1.

Statistics: Strength 2, Agility 2.5, Stamina 2, Intelligence 1.5, Wisdom 1.5, Perception 1.5, Charisma 1, Chakra Reserves 1, Constitution 1.5, Sensitivity 1.5, Willpower 1. This is the Level 1 array with +0.5 Sensitivity at Level 2.

Proficient: Taijutsu, Ninjutsu, Chakra Control, Stealth, First Aid; the Level 2 step adds Perception. Techniques: Transformation, Chakra Adhesion, Spark, and Body Flicker. Affinity: Fire. Light armor rating 1.

- Health maximum: 25 + 8 + 6 = 39.

- Stamina maximum: 9 + 4 + 3 = 16.

- Chakra maximum: 40 + 20 = 60.

- Evasion: 8 + 2.5 + 1 = 11.5.

- Defense Target in light armor: 12.5.

- Damage Resistance: floor((2 + 2) ÷ 2) = 2.

- Armor reduction: 3.

- Physical accuracy modifier: 2.5 + 1 + 1 = 4.5.

- Efficiency: 1.5 + 1 = 2.5.

- Overclock Threshold: 2.5 + 0.5 = 3.

- Trauma Capacity: 1.5 + 1 = 2.5.

- Resolve Score: 8. Fortitude Threshold: 8.5. Stress Threshold: 2.5.

Mika makes a Standard Strike against the same defensive profile. A d20 result of 8 gives 12.5 and hits. A damage die of 5 gives 5 + Strength 2 + Strength scaling 3 = 10 raw. Subtract resistance 2 and armor 3: 5 Health lost. The strike costs 2 Stamina. No Injury Check is required unless this crosses the target's first half-Health threshold or another trigger applies.

Body Flicker costs 3 Chakra; on its own it meets but does not exceed Mika's Overclock Threshold. If Mika also pays 1 Chakra upkeep in that round, total output becomes 4 and causes 1 Trauma. Spending another Chakra that round does not charge the threshold a second time.

A character with capacity 2.5 is Strained at Trauma 3 or 4, Fractured at 5 or 6, and Broken at 7. This is why interval boundaries, rather than integer-only labels, matter.

### 13.2 First mission: The Missing Convoy

Premise: a medicine convoy has not reached a frontier clinic. The team must recover the cargo and identify whether the loss was theft, sabotage or an accident. A rival faction is being blamed without proof.

Objective clock: six segments, “Locate convoy and secure the medicine.” Threat clock: six segments, “The clinic is evacuated and the road closes.” Advance threat for substantial delays and failed risky field actions, not every conversational exchange.

Scenes:

1\. Briefing: learn route, patients' deadline, authority to negotiate and payment. Ask who benefits from blaming the rival.

2\. Trail: Tracking DC 9 discovers a detour; Perception DC 11 finds deliberately altered markings.

3\. Broken crossing: Athletics DC 9 with rope, or a prepared alternative, gets the group over. Failure costs time or a Supply token, stated first.

4\. Contact: frightened deserters shelter with the convoy. Social Pressure can secure release; medicine and safe passage are leverage.

5\. Extraction: protect cargo while crossing back. A pursuer or natural hazard provides pressure if the earlier choices warrant it.

6\. Debrief: determine what each faction actually learns and which promises remain binding.

Opposition should be tailored to the actual party. For a three-person Level 2 team, use two Level 1 sentries with Health 24, Stamina 12, Chakra 30, Defense 10, resistance 1, no armor, accuracy +2, and a light strike dealing 1d6+1 at 1 Stamina. These are simplified NPC blocks with explicitly assigned values, not generated by the full player formula. They retreat at half Health or when a leader falls. Avoid a compulsory fight.

Success pays 1 Supply per player plus a meaningful contact. Resolving the humanitarian and political problem can earn one milestone; simply winning a fight does not automatically do so.

### 13.3 Playtest record

For the first three sessions record:

- Combat rounds, hit rates, average final damage, and whether armor repeatedly reduces attacks to 1.

- Chakra spent, Overclock frequency, and whether Mold plus Precision creates too many failed turns.

- Time and resources spent on recovery.

- Whether each class gets useful decisions without dominating turns.

- Whether social Pressure creates choices rather than coerced character behavior.

- Whether unit Supply, morale and personal missions materially affect battle outcomes.

Change one related set of rules at a time. Keep failed experiments in the decision history. Do not label an edition “fully balanced” from a formula audit.


### Core v3.2 receiving boundary — Chapter 13 (SNWE R0.3 proposed binding)

> The worked R0.1 scene is retained as a scripted source fixture, not an adopted campaign or empirical playtest. Core §90 governs the runtime; scenario records must not invent actual stock, communications or actions outside their written premises.

## 14. Sheets and stable records

## Character sheet

Identity / home / affiliation / nindō / bond / rival / obligation.

Level / Character Band / Rank / class / Path / affinity / heritage.

Eleven statistics / proficiency tiers / known techniques.

Health current/max / Stamina current/max / Chakra current/max.

Evasion / Defense Target / resistance / armor reduction / Fortitude / Resolve.

Efficiency / Overclock / output this round / escalation counts by rank.

Stress / Stress Threshold / Trauma / Trauma Capacity / injuries / conditions.

Destiny / unresolved Tolls / Karma / faction standings.

Equipment / personal Supply / current project clocks / milestone halves.

All derived maxima, defenses and ability records show the edition used.

## Technique and item record

Name / source / version / discipline / rank / access / tags.

Action / Stamina cost / Chakra base / escalation / upkeep.

Range / target count / area / duration.

Activation statistic and proficiency / DC or defense / hit procedure.

Damage or effect / mitigation interaction / counterplay / risk.

Any exception is written explicitly.

## Campaign log

Date / scene / declared stakes / rolls / costs / result.

Characters changed / injuries / information learned / promises.

Clock changes / faction knowledge / territory and supply.

Legacy record / Destiny Toll / source or amendment that authorized an exception.

## Amendment record

Identifier / old rule and source / problem / replacement.

Affected tables and examples / conversion effect / validation.

Playtest evidence / status / date.

Statuses: proposed, active in this playtest, revised, retired.

The reconstruction decisions below are active only within R0.1.


### Core v3.2 receiving boundary — Chapter 14 (SNWE R0.3 proposed binding)

> Sheets are read-only/presentation views of shared owners as applicable, with native SSN-specific values stored in actor/genre profile records. Core §§12–13/91 prevent duplicate mutations from two forms.


---

---

# Part III — Shinobi World Conversion Engine (specialized implementations)

**Status:** All seventeen conversion sections below remain **proposed SSN genre-specific world rules**, distinct from Core 3.2's accepted workshop provider contracts and SSN R0.1's native working numbers. Their technical and societal scope depends on actual setting/technique prevalence and available profiles. They do not add a second Core runtime or physical owner.

## Conversion provider matrix

| Section | Specialized problem | Direct Core 3.2 service | SSN-owned remainder |
|---|---|---|---|
| §17 | Shinobi world capability declaration | §§5, 53–55, 109, 112 | Jutsu/affinity/rank actual capability and limits |
| §18 | Chakra physiology and actor function | §§14, 17–19, 109, 118 | CU/SP, output, Trauma, specialized biology |
| §19 | Production and physical output of jutsu | §§73, 101–103, 108–109, 119 | Actual technique-produced matter/effect rules |
| §20 | Shinobi movement/travel | §§47–50, 62, 102, 105–106, 116 | Zones, adhesion, Flicker, technique speed/load |
| §21 | Genjutsu/sensor deception | §§60–61, 79, 85–86, 115, 120 | Perceptual illusions, counterplay, chakra sensing |
| §22 | Clone/summon/puppet/seal manifestations | §§14, 55, 57, 106, 112 | SSN creation/control/activation/action constraints |
| §23 | Combat/medical interpretation | §§17–19, 47–54, 118 | SSN hit/armor/HP/Injury/Trauma/treatment |
| §24 | Academy, shinobi education/careers | §§31, 45, 76–77, 110, 122 | Jutsu learning, Bands, shinobi class/Rank |
| §25 | Missions and covert operations | §§29–30, 60–63, 79, 115, 120 | SSN contract/clock/rank/stealth methods |
| §26 | Hidden Villages/clans | §§25–29, 64–65, 107, 113, 117, 122 | Kage, clan/academy/ANBU setting institutions |
| §27 | Economy and requisition | §§24, 35–38, 73, 105, 114 | Supply tokens, RP, ninja tools and missions |
| §28 | Shinobi public health | §§17–19, 43, 118–119 | Medical chakra effects and specialist patients |
| §29 | Strategic warfare/Era | §§32–35, 41–42, 62, 106, 117 | Unit Strength, war phase, Era/RP rules |
| §30 | Formal examinations | §§45, 63, 110, 123 | Shinobi trials, exam scoring and promotion |
| §31 | Mythic legacy and intervention | §§69–70, 79, 99, 112, 122 | Destiny/Toll, bloodlines, artifacts, DSSN |
| §32 | Creation/genre manifest | §§88, 97, 111–112 | Shinobi-specific enabled modules/profiles |
| §33 | Effect/reporting overlay | §§5, 11–12, 85–86, 90–91 | SSN native action/effect references only |

**Boundary:** A Core service is selected once. An SSN numerical profile is likewise selected once. Specialized conversions below should be read as a complete genre rulebook alongside Part II, not as additive duplicates of these Core algorithms.

## 17. Shinobi world-capability contract

**Purpose:** Connect SSN native capacities to a continuing physical and institutional world without turning the entire simulation into an unbounded supernatural free-for-all.

**Trigger:** A technique, bloodline, artifact, summon, technological tool or established extraordinary feature is used for an effect that changes something beyond its user's immediate abstract game state, or is introduced at enough prevalence to affect a wider institution, service or environment.

**Specialized SSN capability record:**

`Technique/source ID | SSN rule edition | discipline/rank/access | affected targets | activation and delivery procedure | Chakra/Stamina/other costs | output/effect | effect channel | target resistance/mitigation | range and geometry | persistence | maintenance/upkeep | created/transferred/altered state | detection and counterplay | special risk | relevant Core owners | setting authorization | validation status`

The **effect channel** distinguishes at least: physical impact, imposed movement, heat/cold, electrical or elemental process, information/perception, restraint/control, treatment, transformation, material creation/transfer, temporal/causal intervention or other specifically defined effect. Labels do not supply effects. A technique described as “water” does not establish a drinking-water rate; “healing” does not cure all injuries; “clone” does not mean a new autonomous worker.

**Procedure:**

1. Determine the written technique and access of this specific actor, including level, Band, known components, affinity, hands or other method, institutional/contract rights if relevant, and available resources.
2. Select its existing R0.1 activation/check sequence; do not add unpriced checks.
3. Identify the *actual* world object, actor, location, audience, environment or contract the effect can reach.
4. Identify the part of reality it changes and the owner-qualified record fields impacted; state its duration and whether a continuing process requires support.
5. Apply precisely the written benefit, supported residual effects, and real exposures. A successful attack may still fail to alter a heavily protected target where the chosen effect model says so.
6. Schedule observation, information transfer, upkeep, release, termination, decay and any supported ongoing consequences at their actual times.
7. Use the selected profile to assess repeatable productivity and institutional impact; the power's mere existence does not equip a village with its infrastructure.

**Result reference:** `source/capability ref | actor | committed cost event | SSN effect result | target refs | owner-qualified Core effect event | persistence/termination ref | witnesses/reports | follow-ups`. This is a genre-facing view of Core §91’s authoritative event, never another spendable ledger.

**Unresolved:** Durable output rates, detailed channel matching and technique-specific world impacts require per-technique calibration. The generic contract does not invent them.

## 18. Chakra physiology, energetic limits and extraordinary biology

Chakra's native numerical behavior is specified by R0.1 Chapter 4, including static Chakra Reserves contribution, the Level-dependent maximum Chakra Units pool, Chakra Efficiency Rate, Overclock Threshold, rank escalation, and source-defined recovery. These are **SSN-only**, not Core attributes.

**Chakra phenomena** can interact with ordinary body function, the environment, information and external objects only where specific techniques or setting mechanisms permit. Having a Chakra pool does not automatically imply that the actor can channel it into arbitrary strength, enhanced senses, immunity, transmutation, self-healing or permanent labor output.

**Body/resource record:** `actor_ref | health/current/max | stamina/current/max | chakra/current/max | Chakra Reserves statistic | output_this_round | escalation_by_rank | Trauma | Stress | effects | injuries | functions | recovery processes | edition`. R0.1's named equations control the numeric profile; Core stores the continuing actor and authorized condition references, not a competing copy of the same pool.

**Output and burden:** An actor may possess sufficient current Chakra Units for a technique but cross the R0.1 Overclock Threshold, receiving the documented Trauma. Its once-per-round crossing rule does not charge identical threshold Trauma again on subsequent spending that same round. Distinct S-rank, critical, synthesis or technique-specific costs are retained when their sources are different.

**Source and regeneration:** Do not assume an ambient infinite Chakra stock or a universal biological Chakra-conservation law. A technique claiming energy extraction, sharing, storage or Chakra transfer needs its own actual mechanism, applicable capacity and security rules. Regeneration occurs only through the selected R0.1 recovery process or a clearly declared authorized exception; presenting an extra scene does not regenerate the pool.

**Physiology beyond ordinary humans:** A setting module can define nonstandard species, constructs, altered bodies, enhanced senses, unusual aging, or extraordinary resilience. Assign one coherent embodiment and condition adapter per represented cause; a physically persistent injury is not independently charged twice as both generic Core injury and a second SSN injury for the same mechanism.

**Validation gates:** R0.1 exact formula tests; inability to spend below zero; high-output threshold non-duplication; recovery at correct time; finite or justified external transfer; no unexpected resource creation.

## 19. Technique effect conversion: production, material and service

The R0.1 starter catalogue is illustrative gameplay content, not a catalogue of every possible world-level use. To promote a technique into physical production or an institutional service, prepare an **SSN use profile**:

`Technique/ability | target function | required practitioner and proficiency | usable actions or operating time | resource expenditure | supported amount/output rate | quality/composition | temporary vs durable | infrastructure/tools | cleanup/byproducts | hazard/exposure | actual recipients | stop conditions | maintenance | permitted scale`.

**Material production:** Resolve whether the effect generates material, transforms existing matter, moves material, temporarily manifests a construct or merely produces a damaging visual/elemental effect. A declared durable created output may enter K-STOCK or K-ASSET under a supported extraordinary source event, but not before. A short-lived water attack does not supply drinking water, and an Earthen Screen used for cover does not automatically become a permanent masonry component.

**Work augmentation:** Skill cannot bypass an absent capability. If a documented jutsu improves worker throughput, apply it to K-WORK only for the actual supported task stages and only during genuine use, with actual Chakra/time costs and any limits on operators working in parallel. Do not translate jutsu damage dice into production kilograms or technician-hours.

**Infrastructure and public service:** Useful service capacity requires available users, trained practitioners, duty schedules, accessibility, reliability, distribution and upkeep. Create no universal free labor or municipal service simply because one NPC knows a technique. Substitution for existing infrastructure requires a comparable output measure and a plausible operating organization.

**Environment:** Heating, chilling, fire, groundwater, flooding, erosion and crop effects follow the technique's demonstrated channel and the enabled environment profile. A combat description may be insufficient to calculate large-area ecological effects; record the gap, not a universal penalty.

**Example (hypothetical, not canon):** a technique producing 20 liters of drinkable water per activation could support a settlement only to the extent the profile also defines safe capture, available casters, recoverable Chakra, distribution, and actually scheduled production. Twenty liters is an explanatory test fixture, not an adopted jutsu yield.

## 20. Movement, zones, transport and traversable paths

SSN Chapter 5 owns combat zones, range labels, dash, Standard/Minor/Reactions, positioning and stamina expenditure. Core time and location persist across scales.

**Movement procedure:** determine exact current location, path/access, technique reach, traversability, obstacle, physical ability, declared costs, origin/destination and arrival time. A technique named “Flicker” does not move through solid walls where its record disallows that. Chakra Adhesion authorizes supported surface traversal but does not increase carry limits or create a road. Substitution requires the SSN tactical trigger and suitable available cover; it is not a generic instant escape from a locked restraint.

**Travel distinction:** An action's combat-zone movement entitlement is not a quantified kilometers-per-hour overland capability. For longer movement, define a travel profile or use the relevant MAR/WILD/K-NET means with supported speeds, duration, resources and actor endurance. No invented universal conversion from zones to distance.

**Cargo and followers:** Moving the caster does not implicitly transport another actor or inventory unless the technique's load/target field permits it. Mobile stock and attached gear follow explicit load permissions and actual ownership/location. Transporting a person does not rewrite their agency or legal status.

**Visibility/information:** Extraordinary travel can change what an observer could notice; a successful move does not automatically erase evidence, reports or pursuit tracks. Movement and observation are distinct events.

## 21. Genjutsu, concealment, senses and identity

**Genjutsu:** The native R0.1 discipline changes perception or supplies specifically written conditions, uses its printed resistance and upkeep, and does not directly reduce Health unless an explicit separate effect exists. K-INFO stores the difference between actual object/state and observer-specific perception, beliefs and later reports.

**Transformation:** A visual disguise alters apparent identity only to the scope in the written technique (for example, R0.1 Transformation does not copy physical capabilities). The same actor retains their real identity, physical location, known techniques, legal property and injuries. If a character successfully impersonates an official, the deception can affect witnesses' beliefs and practical access without creating a genuine appointment.

**Sensing:** Detection is bounded by modality, range, line/path, sensitivity, concealment, source signatures and counterplay as stated by the selected technique. A result may reveal one detectable fact; it does not provide the entire K-INFO database. A successful concealment does not change a witness's already delivered earlier report.

**Investigations:** INV owns cases, evidence custody and hypothesis workflow. SSN supplies methods such as sensory jutsu, supernatural tracking or extraordinary disguise. Record who observed what, source, event time, report delay and interpretation. Duplicated rumors do not count as independent evidence.

**Communication:** Mind-to-mind information, if a setting explicitly supports it, still requires a source with actual knowledge and the declared transmission/reception limitations. Instant communication cannot invent remote facts.

**Acceptance example:** a Genjutsu victim perceives a second attacker. K-INFO records that perception; K-ACTOR/K-POP do not create a second physical person. Actual self-defensive actions remain player-declared where applicable.

## 22. Clones, summons, puppets, barriers and other manifestations

An SSN feature's **name** does not determine whether it creates an independent actor, a temporary controlled extension, a physical construct or an illusion. Its explicit record does.

**Manifestation setup:** `source ability | controller/source actor | appearance identity | actual physical entity/asset ID if any | persistence | spatial reach | allowed senses/actions | control authority | upkeep | damage/termination | equipment/material supplied | autonomous decision rules | provenance`.

**Illusory clone:** R0.1's Illusory Clone remains a perceptual Genjutsu with its described one-target penalty. It has no independent action, carried inventory, legal identity or real damage ability. Do not infer shadow-clone capabilities.

**Summon:** R0.1 requires contract, technique record and creature stat block, limits one active combat summon per summoner, and requires the specified Standard Action to command it. Summon arrival, control and independent willingness are separate when the summon has genuine autonomy. A summoned individual does not duplicate an existing actor when recalled and re-summoned; use persistent identity where appropriate to the setting.

**Physical duplicate/remote puppet:** Other specialized modules may introduce physically usable duplicates or puppets. Those require explicit capacity, independent/controlled actions, material durability, inventory, communication/control and resource costs. Their existence is not authorized merely by generic Core support for constructed actors.

**Barrier/seal:** SSN records the actual covered geometry, Health/durability and expiration as specified. A barrier blocking a route must occupy a real route, cannot impede absent targets outside its actual coverage, and does not automatically grant an extra attack. Permanent or long-term seals remain a qualified research or specialized technique requirement.

**Termination:** Removing or destroying a manifestation closes only the existence/control/effect described. It cannot retroactively undo actions or observations already caused. If actual durable by-products survive, a dedicated technique profile specifies them.

## 23. Combat, injury, medicine and incapacitation conversion

**Combat model:** SSN R0.1 Chapter 5 is the only selected physical hit/mitigation model. Native defense uses SSN's Evasion Value, Armor Rating, Dodge/Parry, innate Damage Resistance and Armor Damage Reduction with the printed resolution order. Do not stack the Fantasy Threat/Defeat model or convert d20 natural results into Core d100 criticals.

**Combat effect vs physical fact:** Health loss represents the selected SSN gameplay effect, not necessarily a literal wound, organ rupture or penetrated armor. Chapter 7 Injury Checks represent R0.1's explicit transition into injury state. Store anatomical detail only when supported by actual description or mechanism; avoid automatically inferring amputations from numerical Health damage. The native minimum-one-Health successful-damaging-hit convention remains active in this playtest profile; it is flagged for calibration because fully stopped physical penetration and Health depletion can differ.

**Treatment:** The SSN R0.1 treatment tables and Medical Ninjutsu are the operative specialized effect profiles. MED owns the episode, staff, triage, facilities, supplies, transport and records; K-ACTOR owns the same actual injuries and recovery. Stabilization does not equal full biological healing; the native Field Mending explicitly restores Health without clearing Injury.

**Poison/disease:** The Shinobi module must give each compound's transmission, exposure, latency, condition, counteragent and detection. Poisoncraft skill alone supplies no universal instant poison or antidote. Environmental exposure and injury are distinct linked states.

**Fatality and exceptional rescue:** SSN Downed/Injury/death settings apply within the selected campaign. Destiny intervention can avert immediate death only as R0.1 states and must retain actual Injury, Trauma and obligations. Ordinary Core resurrection does not occur by default. Real bodies, corpses and existing estate/appointment events remain governed by the setting's adopted resurrection/continuity rules.

**Calibrate:** armored low-rank damage floors; Precision double gates; high-Level Taijutsu vs Ninjutsu output; medical success frequency; one-hit injury checks; recovery, Trauma and stamina pressure. These are explicitly not proven balanced.

## 24. Training, growth, Academy, profession and careers

Character Level, Band, Rank, proficiencies, statistics, classes and Paths remain exactly the selected R0.1 native model. LIFE provides actual educators, mentors, learning opportunities, commitments and career history; it does not replace SSN numerical progression.

**Academy/mentorship record:** `actor | affiliation | instructor/source | accessible curriculum | discipline/technique | eligibility and access | scheduled time | actual qualifying attendance | demonstrations | examination/mentor decision | permitted R0.1 advancement grant | recognized institutional qualification`.

**Procedure:** Establish time/teacher/source, execute feasible practice, record evidence of learning or achievement, apply R0.1 Level milestone/benefits when actually earned, and separately record institutional rank/qualification when an appointment or authorized exam procedure says so. An R0.1 milestone cannot appoint a character Kage; a political appointment cannot automatically improve Taijutsu.

**Specialization:** Medical-nin, field operators, sensory specialists, instructors, investigators, logistics officers, sealers and civilian professions can share genuine Core careers while using SSN proficiency/access. No new universal profession bonuses are implied.

**Long-term progression:** Allow peace, retirement, teaching, business, civil administration, relationships and family progression. Ordinary expertise and quality of life can advance without triggering a stronger enemy. For missing long-term schedules, preserve uncertainty rather than inventing exact hours per Level or jutsu.

## 25. Mission commissioning, reconnaissance and covert operations

The R0.1 mission cycle (brief, prepare, travel/infiltrate, act, extract, debrief, downtime) remains the SSN gameplay workflow. Its mission generator 2d6 table remains genre content, not generic Core events.

**Mission contract:** `issuer | goal | mandate and legitimacy claims | pay/claim terms | constraints | known evidence and uncertainty | team and current resources | deadline | locations/routes | permitted methods | secrecy rules | exposure triggers | withdrawal/debrief | objectives and threat conditions`.

Briefing creates no hidden knowledge; the team's information depends on delivered reports. Actual preparation reserves available people/equipment (reservations ≠ consumption). Travel uses continuous world time. A mission's target may relocate, recover or act off-screen if their goals and knowledge support it. Extraction is a separate physical task, not an automatic consequence of mission success. Debrief changes recipients' knowledge when reports arrive.

**Covert tradeoff:** Illicit access can physically succeed while having institutional consequences; legal authority does not guarantee stealth. An intelligence-gathering success does not imply remaining undetected unless the relevant procedure establishes that distinct outcome. Unknown truths remain unknown after an inconclusive inquiry rather than converting automatically into clues.

**Clocks:** Objective and threat clocks retain R0.1's selected 4/6 segments, but are bound to actual declared triggers. A failed roll does not unconditionally produce unrelated enemy reinforcements, discoveries or catastrophes. Physical results of an objective can be achieved before a threat completes; neither automatically erases the other.

**Reward:** Mission rank describes risk/scope; contract determines any actual reward. A promised Supply token or payment is not actual delivered money/equipment until the chosen abstract/persistent resource profile says so.

## 26. Shinobi institutions, Hidden Villages and clan governance

**Village organization:** K-ORG owns the actual village, offices, members, assignments, credentials, jurisdictional claims and delegation. SSN defines Shinobi-specific offices, ranks, ANBU overlays, Academy and village command customs supplied by a setting profile. GOV records decisions, treaties, jurisdiction and real authority; actual political relationships may be contested.

**Political/operational split:** Kage appointment, military capacity, professional skill, personally known jutsu and de facto legitimacy are independent. A village leader can give a lawful order only within established mandate; a capable subordinate may physically disobey, with appropriate institutional consequences. Secret intelligence authorization does not create a rank-stat bonus.

**Clan organization:** A clan is a real organization/kinship network composed of actual actors, related but separately recorded families, assets, obligations, rank, succession and extraordinary bloodline access. Biological kinship does not prove bloodline awakening. An individual can be clanless or politically outside a clan; the R0.1 creation alternative remains available.

**Village autonomy:** Appointed NPC staff train, heal, administer, patrol, buy, produce and investigate within finite means and received directions. Off-screen activity proceeds without requiring protagonist micromanagement, but no village instantly learns the PC's secret action just because the GM knows it.

**Setting ownership:** The particular Hidden Village names, geography, timeline, clans, traditions, schools and politics belong to a Shinobi setting module, not this universal genre engine.

## 27. Economy, mission Supply, local business and logistical conversion

R0.1's **personal Supply tokens** and **faction Resource Points** remain playable abstractions. The named numerical mission rewards, repair costs, army upkeep and quarter income remain the source profile in Part II. IRGS's more detailed actual stock, production and finance may be enabled only under an explicit profile with one consistent backing basis.

**Economy choices:**

- **SSN-A / Abstract playtest:** Apply R0.1 tokens/RP, their listed purchases and costs. Ordinary quantities created by the abstract purchase are recorded once; no second cash/stock system independently spends the same allowance.
- **SSN-P / Persistent-world (proposed):** Treat selected tokens as specified entitlements, funding or expense views when they actually represent those things. Authorize procurement, delivery, stock/title transfer and institution-funded payment with Core ECO/K-STOCK mechanisms. Convert only where a campaign supplies the economic backing and a valid bridge; do not assume 1 Supply = fixed currency or kilograms. The unresolved mapping does not generate a free item.

**Military supply:** A unit's SSN Supply rating is a profile metric with its own combat consequences; it is not automatically a pile of food or ammunition. Establish a mapping from real available cargo/consumption to the operational rating before using the same military stock at both levels. Transfers and replenishment must reach actual recipients.

**Production and markets:** Village trade, clinics, workshops, farms and services follow actual resource/labor/access under ECO, LIFE and K-NET. Special chakra technology or jutsu production enters only through specifically calibrated technique profiles. A shinobi's prestige or high Level does not create a guaranteed market or profitable business.

**Scarcity:** Reserving eight kits does not protect them from a physically real loss. Actual loss commits, leaving physical availability and unbacked commitments distinct; continuing contracts remain obligations until fulfilled or legitimately adjusted. Prepaid promises, unpaid missions and shipped cargo are different records.

**Profile completeness gate:** If a market decision needs precise prices, the setting must supply that specific price/market method; generic R0.1 Supply costs are only an abstract campaign convenience. No invented universal ryō conversion.

## 28. Medical institutions, hospitals, environment and public health

MED owns care and public-health workflows. SSN owns chakra-specific treatments, poisons, physical/cognitive impact profiles and supernatural exceptions. WILD owns actual environment/exposure conditions where relevant; K-ACTOR retains only one physiological condition.

**Medical-nin facility:** actual practitioners, qualification, usable duty hours, Chakra/Stamina, beds, tools, sterility/period suitability, patient access, medicines, facility services, and referral links are all independent. One master healer cannot treat two incompatible critical operations in the same hour unless the method permits parallel activity. A successful technique may bypass a particular physiological restriction only if its written effect includes that capability.

**Public health:** An extraordinary heal effect is not automatically widespread clinic availability, disease immunity, sanitation improvement or higher life expectancy. Wider consequences depend on trained practitioner prevalence, repeated treatments, transmission, early detection, supply and actual access. Epidemiological rates and treatment effectiveness remain setting/technique calibrated.

**Environmental effects:** Chakra-using organisms, summons, poison ecosystems, specialized hazards and altered habitats are admitted only through actual world modules. A campaign's physical and ecological laws can be extraordinary, but a named element does not establish infinite natural renewal.

## 29. Strategic warfare, population, command and Era turns

SSN Chapter 12 defines the selected tactical unit profile, phases, action menu, Morale, Power, Defense, Skill, Supply rating, abstract Strength, and three-month Era Resource Point economy. These **numbers** remain SSN-owned.

**Actual people:** K-POP and K-ACTOR hold real headcounts, individual conditions, prisoners, wounded, dead and available personnel. SSN Strength is abstract unit effectiveness, not headcount. Losing Strength does not automatically kill its matching number of people; rallying/restoring Strength does not resurrect anyone. The setting requires an explicit casualty resolution when individual totals matter.

**Scale transfer:** When a character-scale mission changes a real fortification, command channel, captured asset or depot, apply the physical event **once**. Calculate its military rating consequence if the actual SSN bridge supports it. A later strategic phase cannot also apply an additional hidden copy of the same destruction.

**Command:** Orders require real chain of authority, transmission and receipt; a defeated commander may have a deputy under the profile. Actual subordinates act through their knowledge and instructions; issuing a command cannot teleport a formation. Unit decisions consume genuine time and supported resources.

**Era turn:** The 3-month R0.1 period is an accounting interval inside K-TIME. Income, upkeep and selected orders apply once under the abstract mode. Zooming into one battlefield scene does not collect another quarter. A proposed persistent economy mode must substitute actual income/expenditure calculations for any abstract resource flow representing the same source and period.

**Unresolved numerical bridge:** Need calibrated distributions between abstract battle Strength/Morale and named casualties, morale, retreat routes, medical response and equipment loss. No universal “1 Strength = n people” is asserted.

## 30. Competitions, exams and formal shinobi evaluation

Core COMP owns organizer, ruleset, eligibility, entry, fixture, performance record, adjudication and prizes. SSN defines the selected exam content and how the participant performs through SSN's skills, jutsu and combat.

**Shinobi examination profile:** `organizer and mandate | participants and actual attendance | qualification and level/rank gates | contest format | environment | permitted jutsu/equipment | physical danger policy | objectives/scoring | tie/forfeit/appeals | judges and knowledge | promotion decision | benefits/claims`.

**Procedure:** Evaluate eligibility first. Resolve actual tasks and effects under the native SSN adapter, preserving spent Chakra, Stamina, injuries and found information. Score only according to the published examination rules. Separate combat performance, intelligence, leadership, judgment, teamwork and political appointments. A Chūnin Examination victory is not mechanically guaranteed promotion unless the specific adopted setting procedure says it is.

**No compulsory combat:** An exam may include written, survival, reconnaissance, teamwork, leadership or tactical components. Neither Core nor SSN creates competition formats automatically from the setting name; the selected event profile defines them.

## 31. Destiny, bloodlines, artifacts, succession and mythic intervention

SSN Chapter 11 retains the **native** Destiny, Karma, bloodline, artifact and DSSN rules. Core v3.2 §99's inherited exceptional-intervention interface supplies only the audit/authority boundary and is never a new universal Destiny resource.

**Destiny:** Spend, rescue, retrospective compatible fact, Toll and World Clock effects remain R0.1 exactly. A flashback must not contradict recorded history or conjure unrelated existing property. The source's permitted rescue does not clear separate injuries, Trauma, debts, promises or actual captures except as the rule explicitly specifies.

**Bloodlines:** Store actual parentage, biological lineage, access tags, qualification and awakening conditions separately. Bloodline Grade is not Character Band, institutional office or proficiency bonus. Inheritance records do not create a copied actor or duplicate knowledge. Existing property/claims transfer via actual inherited mechanisms.

**Artifacts:** An artifact is one persistent asset with access, bond, source effects and failure. A separate battery must have its own supported capacity and replenishment source. A bond clock alone cannot manufacture a second artifact. Ownership, theft and physical loss remain real world events.

**DSSN:** The Divine Spiral Seal Network is an optional mythic premise, not a generic Core feature, standard Ninjutsu or auto-unlocked Level reward. Each activated node and event contract names who/what can be changed, irreversible cost, actual resources, instability, counterplay and affected locations. Cosmic or historical changes are constrained by the selected override and campaign authority. No setting-wide lore is presumed.

**Succession:** Retirement, death and protagonist change occur while the world continues. Household and institutional duties, legacy and estate transfer through actual events; successor choice remains the player's. Extraordinary resurrection, if selected, does not retroactively undo settled office appointments or transfers by default.

## 32. Genre-specific world initialization and configuration

**Profile identifiers:** `campaign_id | Core_version/hash | SCL_selected_release/status/hash | SCL_effective_reference_baseline | SNWE_version/hash | native_R0.1_profile | setting_module/version | enabled_expansions | economy_model | injury/effect_model | resolution_adapter | time origin | organizational/medical/casualty profiles | definition selectors and source profile dependencies | ruled unknowns | adoption/effective date | override registry | test evidence`. Source-proposed fields never silently override adopted campaign state.

**Initialization sequence:**

1. Pin reference versions and explicit authority before actual actors are created.
2. Create or recover the real setting locations, people and institutions from adopted sources or an authorized campaign-generation rule. A textbook example is not a live NPC by default.
3. Select numerical SSN native rules as the actual playable profile, unless a more authoritative scoped override exists.
4. Define only the world-conversion parameters needed for the opening decisions: enabled jutsu/ability effects, actual medical/civil services, supply interpretation, transportation capabilities, and any meaningful extraordinary ecology.
5. Build actual actors, property, known techniques, affiliations, conditions, knowledge and standing without assigning lore or objects by genre inference.
6. Schedule relevant independent NPC work and off-screen effects through K-TIME. No mandatory three-month jump or extra repair action occurs during initialization.
7. Run the applicable acceptance fixtures and record which unresolved parameters block particular calculations; continue unrelated feasible activities.
8. Present the player with a meaningful decision and do not author their voluntary choice.

**Minimal profile:** SSN R0.1 basic scenes can run with few records. High-fidelity village planning may activate expanded GOV/ECO/MED/CIV/URBAN/WILD as needed. A domain's existence does not impose empty periodic bookkeeping.

## 33. Operational event, resource and information boundary

Use Core §§11–12/91 owner-qualified commits, rather than a Shinobi-only duplicate journal. The following is **a nonauthoritative event view** whose fields resolve to one Core event and its selected native rule records:

`SSN.ActionView = core_event_ref | campaign_id | time | actor_ref | declaration_ref | skill/technique/ref and exact SSN version | action commitment refs | actual cost events | recorded dice/effect result | owner-qualified actual changed refs | condition refs | sustain/termination refs | witness/recipient knowledge refs | unresolved PC choices` (derived, not independently mutable).

On an activated technique, K-ACTOR pays Chakra/Stamina once; K-TIME schedules eligible reactions and round boundaries; K-ASSET/K-STOCK change actual objects or stock only if the technique's declared world effect supports them; K-INFO records what observers could know. Where a source effect has no material-world conversion (for example a mere combat damage description), apply only its native SSN game effect.

**Player control:** No Mixed result may spend a new technique, accept a bargain, decide to retreat or place an extra clone without declaration. Autonomous NPCs may react within their goals, authority, action budget and available knowledge; report authors do not magically know hidden facts.

**Observations:** Differentiate when an event occurred, when it was observed, when a report was transmitted and when each recipient received it. Illusion/altered perception can yield honest but false reports; truth and belief retain separate provenance.

**Replay and scale:** Same event ID/payload replays as no-op. Conflicting reuse is rejected. Tactical-to-strategic conversion preserves every actual remaining resource, named casualty, captured item, work completion, unresolved action and message in flight.

---


## 34. Receiving-model validity, completeness and rejection gates (originally added in R0.2)

Before applying an SSN ability to a material-world system, bind a **complete specified technique profile** to an existing actor, location and selected Core model. A native damage roll, flavor label or brief starter technique is insufficient to infer mass yield, thermodynamics, potable-water quality, persistent lifespan or work rate.

| Missing or conflicting input | Permitted behavior |
|---|---|
| Unsupported numeric output rate | Resolve the already written combat/utility effect; defer only the numerical production/service calculation |
| Jutsu has no permanent-material statement | Keep the actual written temporary effect; no additional harvestable resource |
| Technique can appear as an actor but cannot exert force | Record the perceived/projected manifestation; do not add labor/headcount |
| SSN and SCL both describe an item | Select SCL physical definition **and** SSN numeric attack adapter only when the exact fields are compatible; never combine two mitigation chains |
| No supported income↔resource bridge | Use one abstract economy *or* one independently backed actual economy, not both for the same source |
| One unit's Strength reduced but casualty mechanism omitted | Change the native combat-effectiveness track; retain actual headcount and conditions unresolved, not falsely zero |
| Layered injury from multiple true causes | Retain genuinely distinct injury/exposure channels but apply no duplicate report/update to one event |
| New technique distribution across village unknown | Local practitioner capability exists; society-wide capacity is an assessment unknown until real training/staffing evidence |

**No invisible default conversion:** Core §112 requires units, owner-qualified inputs/outputs, valid envelope, thresholds, supported method and prospective scope when they affect outcome. Select qualitative judgment only when it can answer the particular decision without invented precision. The genre does not invent national population rates or engineering numbers to make every table look complete.

## 35. Specialized content and source adapter contract (originally added in R0.2)

Every enabled SSN technique, weapon mode, bloodline feature, summon or artifact stores one exact native source/profile reference. Where a common ordinary item uses the current SCL 1.0 catalogue, store the **exact unchanged 0.2 family reference and selector**, the individual SCL entry readiness status, its original payload/adapter if held, and the SSN-native numeric mode separately.

`SNWE.ProfileBinding = campaign | native_rule_set | SSN technique/skill/item ID | exact selected SCL family@0.2 when applicable | selector/type/checksum | source readiness/adapter | eligible setting variant | activation gates | actor/asset/stock refs | chosen numeric effect/care/resource model | unsupported fields | overrides | effective time`.

**Weapon example (illustrative):** one actual sword can have two physical mode selectors (cut/thrust), but neither SCL's Fantasy injury Threat values nor an old Roman cut formula is automatically valid within SSN combat. SSN R0.1 gives the sword reach/tag and its Taijutsu/Weaponry damage mode; selecting a more precise alternate weapon profile would require an explicitly documented SSN compatible model and regression review.

**Medical example:** a real kit definition plus its actual stocked components can support an SSN medical action only within the selected SSN treatment procedure. SCL does not contribute a second healing result or dispense stock not physically held.

**Information example:** possessing a sealing manual is physical possession of recorded data, not innate ability to perform Fūinjutsu or institutional license to do so.

**Technique content:** SNWE R0.3 preserves all R0.1 starter techniques; names from unrecovered historical catalogues are not silently invented or treated as integrated. Full numeric techniques require individual source-by-source conversion to maintain access, effect, cost, counters and balance.

## 36. Complete SSN receiving event handoffs (originally added in R0.2)

| Trigger | SSN-specific computation | One actual Core write / domain request | Separate observation or follow-up |
|---|---|---|---|
| Standard jutsu paid/molded | Cost, rank counter, output threshold, selected dice | K-ACTOR resource debit and correct targeted actual effect only on eligible outcome | Witness sensory evidence; knowledge on receipt |
| Genjutsu lands | SSN Resolve effect and counterplay | Actor condition + observation/perception relationship; **no** physical world rewrite by inference | Incorrect but honestly believed reports possible |
| Summon appears | SSN contract/method/required upkeep | Existing/new explicitly supported actor embodiment/location under one identity and available action budget | Command control and willingness as separate conditions |
| Field Mending succeeds | SSN healing roll, target/scene restriction | Modify target's current Health once, Injury remains unless separately treated | MED care episode/recipient knowledge if relevant |
| S-rank or Overclock strain | SSN profile calculates distinct sources | K-ACTOR Trauma change once per source/threshold | Subsequent effects/recovery use real intervals |
| Training activity finishes | SSN prerequisite/learning test/Level gate | K-WORK/LIFE evidence; if native award condition satisfied apply eligible SSN advancement | Institution awards Rank only under valid K-ORG decision |
| Mission objective completed | Native objective/clock/contract outcome | Actual work/stock/location/casualty state once | Employer learns and pays separately |
| RP income/strategic upkeep due | Native Era/RP mode only when selected | Single abstract balance/claim entry per interval or explicit actual economy substitution | Reporting cannot repeat credit |
| Tactical unit loses Strength | Native battle effectiveness loss | SSN native track; K-POP casualty only via actual supported loss profile | Reports may misestimate real losses |
| Exam judged | SSN activity result | COMP official result once, possible ECO prize claim | K-ORG promotion may follow actual separate decision |
| Destiny flashback | Native SSN point/Toll and scope | Historical-compatible fact record or explicitly authorized exception under Core §§79/99 | Never modify settled history by implication |

**Cross-scale cutover:** Every scene-to-Era transition records (a) the exact time boundary, (b) actors/cohorts and activities covered in detail, (c) physical owner balances and authoritative injuries, (d) selected SSN native phase/abstract tracks, (e) pending events/reactions/upkeep and (f) messages and retained uncertainty. Strategic resolution excludes all already resolved detailed work and losses. An unconsumed abstract clock is not an extra staff-hour pool.


---

# Part IV — Preservation and Original SSN Reconstruction Archive

**Verbatim R0.1 source-register/decision preservation block.** The decisions former proposal status persists; links are source citations and not automatically queried original live docs.

## Appendix A — Original R0.1 reconstruction decisions and preserved alternatives



These decisions make R0.1 usable. They are editorial proposals enacted for this draft, not previously approved canon.

ID: R01 • Decision and reason: Treat R0.1 as a new operating edition. Preserve the historical lock and originals rather than claiming a retroactive amendment.

ID: R02 • Decision and reason: Separate Character Band 0–10, Level 0–20, Rank, and 1–7 grades. Lexicon I and III otherwise use incompatible “Band” meanings.

ID: R03 • Decision and reason: Define feasibility, half-points and rounding. The source mixes half-stat values and integer-only thresholds.

ID: R04 • Decision and reason: Supply an eleven-stat starting array and explicit Level 2 build. Legacy arrays and stat counts disagree.

ID: R05 • Decision and reason: Name Constitution and Sensitivity fully; make Chakra Control a skill. Do not reinterpret old CON formulas as Constitution.

ID: R06 • Decision and reason: Supply skill mapping, tier gates and starting kit. Preserve old arrays/gear lists for later comparison.

ID: R07 • Decision and reason: Retain 2d6 tasks/d20 hits; remove explosions and margin-based damage criticals from active rules.

ID: R08 • Decision and reason: Supply Fortitude and Resolve thresholds and restrict modifiers. Both are named but incompletely defined in the Lexicon.

ID: R09 • Decision and reason: Use one clock procedure for projects and missions. Legacy progress and setback formulas are mutually inconsistent.

ID: R10 • Decision and reason: Keep Lexicon Level resource baselines; static reserve statistic is compatible with a Level-dependent total pool. Retire million-unit costs here.

ID: R11 • Decision and reason: Define efficiency from Sensitivity and Chakra Control. This is a new formula, not a renamed legacy Control/Constitution formula.

ID: R12 • Decision and reason: Charge Overclock once on crossing per round; make rank escalation cumulative and personal.

ID: R13 • Decision and reason: Supply actual rest durations and recovery quantities; remove CPS from active combat.

ID: R14 • Decision and reason: Supply Standard/Minor/movement/Reaction economy. Do not simultaneously use the old AP pool.

ID: R15 • Decision and reason: Add floor(Level/2) to physical/Precision accuracy. Source defense grows with Level while hit bonuses do not.

ID: R16 • Decision and reason: Define one Dodge/Parry Reaction and its timing.

ID: R17 • Decision and reason: Remove Armor Rating from innate Damage Resistance, retaining Defense bonus and armor reduction. Avoid a third armor benefit.

ID: R18 • Decision and reason: Complete grapples, pins, suppression, escape and ready-action procedures.

ID: R19 • Decision and reason: Pay chakra at commitment and require current resources. Capacity alone cannot pay for a cast.

ID: R20 • Decision and reason: Give each discipline one clear Mold/effect/hit sequence. Resolve malformed Ninjutsu bullets through explicit prohibitions.

ID: R21 • Decision and reason: Supply adapted starter records, summon action limits and synthesis failure boundaries.

ID: R22 • Decision and reason: Do not auto-convert the whole legacy jutsu corpus by a scalar; preserve access, effects and risks for item-level conversion.

ID: R23 • Decision and reason: Make Injury triggers per event, define failure severity and avoid stat-maximum feedback loops.

ID: R24 • Decision and reason: Use fractional Trauma intervals; Broken is an incapacity state, not automatic permanent character deletion.

ID: R25 • Decision and reason: Restore an acute-Stress/MRICS interface and operational treatment. Do not add every historical stress system together.

ID: R26 • Decision and reason: Use milestone advancement and a Level-cap bridge; maximum normal statistic 7. Legacy \>7 and Band-10/5.5 concepts remain alternatives.

ID: R27 • Decision and reason: Implement the six class frameworks and four Path categories with priced features. Source frameworks do not contain complete feature lists.

ID: R28 • Decision and reason: Keep institutions, ANBU and occupations separate from numerical power.

ID: R29 • Decision and reason: Restore two downtime activities and the mission/debrief cycle. They cannot generate unlimited stat or Destiny gains.

ID: R30 • Decision and reason: Translate research into common clocks with an explicit output contract.

ID: R31 • Decision and reason: Supply a small personal Supply economy. Keep it distinct from organizational Resource Points.

ID: R32 • Decision and reason: Supply a Social Pressure endpoint and faction-specific standing; preserve player choice.

ID: R33 • Decision and reason: Retain ideology and reputation as recorded commitments and witnessed deeds rather than conflicting global bonus engines.

ID: R34 • Decision and reason: Clarify Destiny thresholds and inheritance outcomes. A Toll is a cost, not a spendable point.

ID: R35 • Decision and reason: Restore artifact bonding and instability with common clocks, without importing incompatible percentage scaling.

ID: R36 • Decision and reason: Make DSSN an explicit event contract. A list of world-changing possibilities is not an unlimited combat permission.

ID: R37 • Decision and reason: Use separate unit ratings and Strength tracks. Keep actual troop counts and organizations when known.

ID: R38 • Decision and reason: Replace the unconditional “2d6 + Power ≥ 7” attack with a target defense and explicit losses.

ID: R39 • Decision and reason: Define morale, supply, withdrawal, support and commander interventions. Do not resolve the same battle at unit and army scale twice.

ID: R40 • Decision and reason: Restore faction/Era procedures with bounded orders, costs and causal knowledge. Personal missions change war states once.

### Remaining content work, not hidden omissions

The core procedures above are executable. The following are preserved as source material rather than falsely represented as fully converted:

- The complete named jutsu, summoning, clan and bloodline catalogues.

- Full prestige trees and class-specific technique lists beyond the supplied starter features.

- Detailed civilian careers, prices, production chains and unit rosters.

- Percentage-based environmental flow, Sync/FQI/CPS metrics, the old /7 Stress models and old XP/legacy mathematics.

- The full setting chronology, named factions and regional lore.

- Digital/VTT schemas and automation hooks.

- Source files' embedded media, native layout, comments and prior Drive revisions.

The recovery package contains text snapshots, source links and hashes. It is not a binary-format backup of every native Google Doc or a complete version-history export. Within each copied text, legacy contradictions remain visible instead of being silently deleted.

### Validation status

Arithmetic examples, probability checks and document consistency checks accompany the package. No live group playtest or comprehensive high-Level balance test has been performed. In particular, test armor floors, low-rank damage at high Levels, double-gated Precision casting, and late-game resource abundance before locking a release.

## Appendix B — Original R0.1 source register

S-numbers identify the recovery snapshot, not a canonical precedence order. Dates are Drive modification timestamps, which may reflect import or editing rather than original authorship.

- S01 — SSN Lexicon 1.9.2 I. Original — https://docs.google.com/document/d/1W-g2ZjaU96Rz766AsF9xJCEVtCZvRqwrvSlfK1uOwbQ/edit?usp=drivesdk. Modified 2025-12-28. Text snapshot retained.

- S02 — SSN Lexicon 1.9.2 III. Original — https://docs.google.com/document/d/1ZdmsLfNNDV1Evm5e6HrrBOjMPmnBEIJ6mKshfgZPdAI/edit?usp=drivesdk. Modified 2025-12-28. Text snapshot retained.

- S03 — SSN Lexicon 1.9.2 II. Original — https://docs.google.com/document/d/1ciULiCyUBbmFzEQcT5-2KdQQ-\_P3qggKRueIneIcH7c/edit?usp=drivesdk. Modified 2025-12-28. Text snapshot retained.

- S04 — SSN Lexicon Draft. Original — https://docs.google.com/document/d/1Orx1UFvjqXMke2xuSmqUPMOX0vJn7GWdzQGRkkp5GfY/edit?usp=drivesdk. Modified 2025-12-25. Text snapshot retained.

- S05 — ssn_revised. Original — https://docs.google.com/document/d/1YaqhkeJNPvQKjp7IltlIQ4CkZA3a2YFbedJJ2WDATWs/edit?usp=drivesdk. Modified 2025-12-25. Text snapshot retained.

- S06 — SSN Lexicon 1.9.2.2. Original — https://docs.google.com/document/d/1F9mSMpo7QGVKlCnWA1CoLjuds7wBhMxMTPCyIBD27U8/edit?usp=drivesdk. Modified 2025-12-25. Text snapshot retained.

- S07 — qqq. Original — https://docs.google.com/document/d/1mK6kS0AqNRR9cvY-k4fjpThC8sldrbJ0zzbpfLGz3Rk/edit?usp=drivesdk. Modified 2025-12-25. Text snapshot retained.

- S08 — SSN Agent Build 3. Original — https://docs.google.com/document/d/19dC8P96zXtdp_UcioL_TXHuXkCwrQ-aBp8-cBk8_t1M/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S09 — Untitled document. Original — https://docs.google.com/document/d/1bRsH2HpBpZqjzhalAQZnatdlp4pSapRAn29CKDwaV8A/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S10 — Shinobi Systems Nexus V2. Original — https://docs.google.com/document/d/17GL7Zj0xog5B58-PacyCDhFvg5GYoOcNZHfe0n0odiM/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S11 — Shinobi Systems Nexus 2.0. Original — https://docs.google.com/document/d/1NXUhR8HPkHrBo8V0dBAcT7JuEDZV1F7PNGMskly1GiU/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S12 — Untitled document. Original — https://docs.google.com/document/d/1bptT-zM2QK7LAu4IczmAQKWWTot07OvwJH0nE4BqdlI/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S13 — SSN Pre-Alpha 2. Original — https://docs.google.com/document/d/1QAgevJ3yhPgg1vMFTjEXfIOLWyydJWt0dXCp2_EGXH4/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S14 — SSN\_ The Dice. Original — https://docs.google.com/document/d/1jNcSuUDQfyDGYUJwUXskHxPYPoTttQLwkbnu1pMysP0/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S15 — Shinobi Systems Nexus: 1.x-5.x Compendium. Original — https://docs.google.com/document/d/1gVFr68_uqZN90_dCGlb3kcZ6hQPnZQmEnmeorxY24-o/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S16 — SSN Pre-Alpha 2. Original — https://docs.google.com/document/d/1ydT2rF8meCwTowCx4iHw6kO4fdUfcP0yE6GII7GJtt4/edit?usp=drivesdk. Modified 2025-12-14. Empty text returned.

- S17 — SSN Pre-Alpha 1. Original — https://docs.google.com/document/d/1h1Txzf3yABj9R3z8RjL6Ysih4Kdnswp_kBsetiq8Ojs/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S18 — SSN 1.0: Shinobi Combat Protocols. Original — https://docs.google.com/document/d/12pYuBBm3EtQJIyMeskGPaxpID3KnqKsE3tcOAnTnqZE/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S19 — SSN 1.0\_ Internal Layers. Original — https://docs.google.com/document/d/1i0bSkp9FkCOTYfo6QPGG7nbr8T6tAa5CChvlOtF74A8/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S20 — SSN Alpha V0.1.1. Original — https://docs.google.com/document/d/1gs2CXEw5WLIFfi42AXmXFkGkemjIyXOtFQL0LHmGWNI/edit?usp=drivesdk. Modified 2025-12-14. Text snapshot retained.

- S21 — Shinobi Chronicles Archive. Original — https://docs.google.com/document/d/1jhmLHnoNjcBHSc3fKYfMRvTxr_K8OQUDopR0ZcbeSQw/edit?usp=drivesdk. Modified 2025-11-26. Text snapshot retained.

- S22 — SSN Alpha: V1.0.0. Original — https://docs.google.com/document/d/1ML-REqBKMS3rqYtxptq5ob8432o6rkZQO3d8--WbAHE/edit?usp=drivesdk. Modified 2025-11-11. Text snapshot retained.

- S23 — Shinobi Systems Nexus 6.2.1. Original — https://docs.google.com/document/d/1XRZuMobgfq7Vk1gCekLSLWcRf1JzurAqX8B1Lw2OzZ8/edit?usp=drivesdk. Modified 2025-11-10. Text snapshot retained.

- S24 — Shinobi Systems Nexus 6.1.3 Draft. Original — https://docs.google.com/document/d/1FTPmlX3aXJ5w8Ywal-6cdAxwvhfFLxMWZ5KMrJNvzWg/edit?usp=drivesdk. Modified 2025-11-10. Text snapshot retained.

- S25 — SSN 5.6.2 Skeleton. Original — https://docs.google.com/document/d/1lwaglHIlBBhYnfXEY6ted1aQArp8C3mzx55ZwBvfqYs/edit?usp=drivesdk. Modified 2025-11-07. Text snapshot retained.

- S26 — Shinobi Systems Nexus 5.6 Draft. Original — https://docs.google.com/document/d/1lc5lrnODbmxLwbP794edFEwxge7OWm-9JCP1Cqa5fAA/edit?usp=drivesdk. Modified 2025-11-07. Text snapshot retained.

- S27 — SSN_5.1.3_Rebuilt. Original — https://docs.google.com/document/d/1YjjWvk56ztnMvRrGFQNoDD3wOmtSmXFavZXV0AKhBP8/edit?usp=drivesdk. Modified 2025-11-07. Text snapshot retained.

- S28 — SSN 5.1.2. Original — https://docs.google.com/document/d/1Nqwkw1EosR9McslLKqDNj7jWiu5uf6tr43EZ1XZdH2s/edit?usp=drivesdk. Modified 2025-11-06. Text snapshot retained.

- S29 — SSN_Layers_15_to_20_Core_Extension. Original — https://docs.google.com/document/d/1wLuhO_doSAdr-5cDGQI32et7HOiim6dt7INF5zV_D2Y/edit?usp=drivesdk. Modified 2025-11-06. Text snapshot retained.

- S30 — SSN 5.0.3. Original — https://docs.google.com/document/d/13SGhy3v6xTiGuv4_zTTx9GZ8RF7B0kmjl0R0CwAbEFE/edit?usp=drivesdk. Modified 2025-11-06. Text snapshot retained.

- S31 — SSN 4.9.3. Original — https://docs.google.com/document/d/1TYRoij4V0RcvrjABrNyHgc2SWrQqAg6iXUhdu_hjGLI/edit?usp=drivesdk. Modified 2025-11-06. Text snapshot retained.

- S32 — SSN 5.0. Original — https://docs.google.com/document/d/1M2kBB-VpFlk-QWtUu2O_47aSnA2Gx_4naOeKkScg_RI/edit?usp=drivesdk. Modified 2025-11-06. Text snapshot retained.

- S33 — SSN 4.7.5. Original — https://docs.google.com/document/d/1S2yM-pURO8HP20JI6XbWikjbf2Q5WogYjAFvd_qnoSs/edit?usp=drivesdk. Modified 2025-11-05. Text snapshot retained.

- S34 — Shinobi Systems Nexus V4.6 Master Edition 1.0. Original — https://docs.google.com/document/d/1V0Ge46a8vxx77SUT590PYrpZBirEA0mZWjm18ONMZlE/edit?usp=drivesdk. Modified 2025-11-05. Text snapshot retained.

- S35 — Shinobi Systems Nexus V4.5 Master Edition 1.1. Original — https://docs.google.com/document/d/1Ekz2O7Ekdf_gnyMadUueIWwaO-76RDSp0cL1qgK_1sY/edit?usp=drivesdk. Modified 2025-11-04. Text snapshot retained.

- S36 — report. Original — https://docs.google.com/document/d/1_LsIIGsO8l77PM4Nj7oHaGW5nkatP88upo7cNc80uIc/edit?usp=drivesdk. Modified 2025-11-04. Text snapshot retained.

- S37 — SSN 1.0: Chakra Synthesis System. Original — https://docs.google.com/document/d/1ySdIE-mmgS7gqiMpDW23uBptBDqxDQa0zZPVWXEIthk/edit?usp=drivesdk. Modified 2025-11-04. Text snapshot retained.

- S38 — SSN_Master_Development_Matrix. Original — https://docs.google.com/spreadsheets/d/1ryOZMPb_wf7WJPzsRCvi1QVjaK5N5BrHhG4qXTLLz5w/edit?usp=drivesdk. Modified 2025-11-04. Text snapshot retained.

- S39 — SSN_4_5_Front_Matter. Original — https://docs.google.com/document/d/15MII8Xd0p8y8EyNDDUxqRvyF-W-CA2qzOiIYJwezzJ4/edit?usp=drivesdk. Modified 2025-09-07. Text snapshot retained.

- S40 — SSN 4.5 Development Tracker. Original — https://docs.google.com/spreadsheets/d/199l1m8q9r5ned3yt-A4dh4XyFtTnhxfdT7pJBAAGneA/edit?usp=drivesdk. Modified 2025-08-17. Text snapshot retained.

- S41 — SSN_Jutsu_Master_Index. Original — https://docs.google.com/document/d/1MNMhT6MuSymLOb2cGc2kqHC52V4ae14QP3bt31DPb4U/edit?usp=drivesdk. Modified 2025-08-08. Text snapshot retained.

- S42 — SSN: Jutsu Compendium V1. Original — https://docs.google.com/document/d/12yOoe9KWVlWbQQ29FqraTTNfc4VQEt0C9OZL1bZNccE/edit?usp=drivesdk. Modified 2025-08-08. Text snapshot retained.

- S43 — SSN: Jutsu lists. Original — https://docs.google.com/document/d/1FswmhguW3oOXKOknpBYaV9myoF-zkvkowXNkXQSrOfI/edit?usp=drivesdk. Modified 2025-08-08. Text snapshot retained.

- S44 — Shinobi Chronicles Timeline. Original — https://docs.google.com/document/d/1PXgtRJSEI0ntEqwaHkbq9K253cPw6RDcu0nvs4nQelA/edit?usp=drivesdk. Modified 2025-08-07. Text snapshot retained.

- S45 — Rebuilding SSN. Original — https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221suNa3MDpBE9sxoSAYpukN7NyxlcMDIyk%22%5D,%22action%22:%22open%22,%22userId%22:%22112396045214517516781%22,%22resourceKeys%22:%7B%7D%7D. Modified 2025-08-04. AI Studio prompt metadata; no readable rules text returned.

- S46 — SSN Character Sheet. Original — https://docs.google.com/document/d/19c2Q5Q_lke5MYk3146nGvpeme63T_77z8fRo14Ez0B0/edit?usp=drivesdk. Modified 2025-07-26. Text snapshot retained.

- S47 — SWarriorSSN.tga. Original — https://drive.google.com/file/d/1UrZy97T23bnZBhHY6ylDJubrA5YLySd0/view?usp=drivesdk. Modified 2013-11-29. Binary asset inventoried; not converted into rules.

- S48 — SWarriorSSN2.tga. Original — https://drive.google.com/file/d/1o6FOp3ubn2wAz9kYzn7wnG8-cw7b7KbO/view?usp=drivesdk. Modified 2013-11-29. Binary asset inventoried; not converted into rules.


---

---

# Part V — CMRR, Exact Core 3.2 Binding, Verification and Migration

## 37. Exact receiving source register and authority

| Source | Exact file | SHA-256 | Use and authority |
|---|---|---|---|
| Core v3.2 | `IRGS_Core_Engine_v3_2.md` | `1817cc01bed02c8cb21bae393878e9234743ea4c538d25e1a4a8934182abf738` | Current shared parent; no second Core runtime |
| Core v3.2 binding register | `IRGS_Engine_Bindings_v3_2.json` | `e7d6a4250921787b673e4c2974711b3dc53a3b5d3a344a09da8ec9995242b0b7` | Existing `SSN_EXTRACTION` binding is **portable extraction only**, not a complete SNWE engine contract |
| SCL v1.0 | `IRGS_Shared_Content_Library_v1_0.md` | `4f0a90687958bd6d54b0ab21dc0cfac4e02e0ed40992a3b86eb1cf1725164376` | Current normative catalogue, per-item readiness unchanged |
| SCL v1.0 registry | `IRGS_Shared_Content_Registry_v1_0.json` | `67c4e0eb4b67fbc8f2cf874dae06381bf2e4c9eb48850a35d7ffc10c8a4a35b9` | 279 families: 51 selected and 228 held; 1,416 aliases |
| SNWE R0.2 predecessor | `IRGS_Shinobi_Nexus_World_Engine_SNWE_R0_2_Core3_1_SCL1_0_CMRR.md` | `39add316e414ca92eeb49855fd77c860216baa2b895b2ba7211d13832340ba35` | Complete previous genre source; comparisons and unchanged native rules |
| Native SSN R0.1 | `SSN — Rebuilt Base R0.1 — Working Playtest Edition.docx` | `04853241ce5bb09f9f092450263ff464e45259f75c00230e0e1969e08b21fd4c` | Playtest numerical/profile source; historically separate from Canon-Zero |

**Release-level source:** `IRGS_Full_Release_R2(2).zip` uploaded by the user; its package manifest confirms the pinned normative files and marks qualitative maturation R1/R2 as non-normative. Core's recorded workshop status is not an assertion of a campaign's adoption. The Core v3.1 package and its Appendix G are **historical provenance only**, not separate active providers.

### Version delta (Core v3.1 to v3.2)

- Core shared mechanics §§5, 24, 41, 55, 73, 99, 108 and 109—the eight originally extracted SSN destinations—remain text-identical after line-ending normalization.
- Core §111 changes the selected current catalogue reference from SCL v0.2 to **SCL v1.0** without changing the unchanged family revision `@0.2`.
- Core §112 changes the named Core release parent to v3.2; its compatibility/activation responsibilities remain.
- Core §§113–123 redirect their CE acceptance cases from former Appendix D to new **Appendix C**.
- The v3.2 appendices are A Owners, B Inheritance/Deployment/Migration/Calibration, C Acceptance/Regression, D Optional Scoped Profiles. The previous v3.1 Appendices B/E/G are not live sources.
- Core v3.2 supplies `IRGS-BIND-SSN_EXTRACTION-3.2`, which has portable shared providers but explicitly no general native SSN numeric adapter. This build supplies its own proposed `IRGS-BIND-SNWE-0.3-CORE-3.2` consuming those providers.

### SCL scope and exclusions

SCL v1.0 contains 279 family definitions, 1,416 aliases, 304 source bindings, 420 source payload blocks, 61 Fantasy adapters and 18 scoped extensions. Its 51 selected contracts supply only their demonstrated qualitative content meanings. **All 228 held families remain held**; their R1/R2 expanded descriptions and the 420 authored per-entry acceptance specifications are not automatically tested or selected. Selecting a definition does not instantiate inventory, equipment, chakra, rank or magic. SSN's own technique/access/effect record is mandatory before an item or capability can operate.

## 38. Bidirectional native SSN chapter disposition

| ID | Complete SSN source function | Core 3.2 receiving sections | Specialized retained functions | Reconciliation |
|---|---|---|---|---|
| N01 | SSN 1 operating contract | §§5, 90, 112 | Native action criteria, rounding, Level/Band/Rank | Retain native; replace only old generic parent |
| N02 | SSN 2 character creation/stats | §§14–16, 45, 77, 88, 122 | 11 stats, array, proficiency, levels, kit, ancestry tags | Retain SSN; one K-ACTOR/starting issuance |
| N03 | SSN 3 resolution/clocks | §§5–9, 10–11, 73 | Golden Equation, DCs, advantage, 4/6/8/12 segments | Retain dice; typed clock and time via Core |
| N04 | SSN 4 chakra/resources | §§17–19, 109 | Level base pools, CU, CER, Overclock, costs, rest | Retain stats and resource formulas; Core actor ownership |
| N05 | SSN 5 combat | §§47–55, 62 | turn economy, d20, armor, damage, Taijutsu, control | Retain complete numeric chain; disallow stacked Fantasy |
| N06 | SSN 6 techniques | §§5, 55, 79, 109, 112 | all written starter jutsu, chakra disciplines, synthesis | Retain genre and setting content; apply bounded world effects |
| N07 | SSN 7 conditions | §§17–19, 43, 118 | SSN Injury, Trauma, Stress, MRICS and care | Retain profile; one condition and MED episode |
| N08 | SSN 8 classes/Paths/Rank | §§31, 45, 76–77, 110, 122 | class/Path/proficiency and Shinobi advancement | Retain native; institution/evidence linked |
| N09 | SSN 9 mission/downtime/economy | §§24, 62–63, 73, 96, 114 | native mission, Supply, research, gear and tokens | Split abstract/Persistent; no duplicate stock/work |
| N10 | SSN 10 social | §§66, 79, 122 | Pressure capacity, ideology, Standing | Retain native pressure; audience knowledge via Core |
| N11 | SSN 11 Destiny/heritage | §§69–70, 79, 99, 112 | Toll, Karma, bloodlines, artifacts, DSSN | Retain supernatural exceptions with Core audit |
| N12 | SSN 12 warfare/Era | §§32–35, 41–42, 62, 106, 117 | unit 1–7 ratings, Strength, phases, RP, upkeep | Retain native warfare; actual persons and economy via Core |
| N13 | SSN 13 first session | §§88–91, 96 | worked character, Missing Convoy, playtest log | Retain as fixture, not campaign state |
| N14 | SSN 14 record sheets | §§12–13, 91 | native SSN character/technique/log views | Retain templates as derived views; one owner |

**Bidirectional test:** Every R0.1 operating chapter 1–14 is represented above. Every Part III world-conversion chapter 17–33 is represented in Part III's provider matrix; new specialized binding §§34–36 are also explicitly owned. The original R01–R40 decisions and S01–S48 source register below are copied without edits. Older general paragraphs remain source history, not a second Core algorithm.

## 39. Core→SNWE receiving reconciliation

| Core receiving capability | Already present in Core 3.2 | SNWE R0.3 correct destination | Prevented regression |
|---|---|---|---|
| CW-SSN-01: action activation stages | §5 | Native jutsu phases and technique effect contract §§6/17 | No re-rolling for same uncertainty or new generic dice |
| CW-SSN-02: actor-bound output/burden | §109 | Chakra, Stamina, Trauma §4/18 | No extra Chakra meter or multiple overclock charges |
| CW-SSN-03: clocks/work/risks | §73 | SSN segments §3/9/17, project bridge §27 | No physical work award per report/segment copy |
| CW-SSN-04: manifestations and identity | §55 | Genjutsu/clones/summons §§21–22 | No illusory extra workers or automatic summon obedience |
| CW-SSN-05: exceptional history | §99 | Destiny/DSSN §11/31 | No unauthorized retroactive rewrite |
| CW-SSN-06: cross-domain capability diffusion | §108 | Shinobi technical prevalence §§19/24–28 | No instant village-level industry from one caster |
| CW-SSN-07: entitlements and backing | §24 | Abstract Supply/RP §9/27 | No cash/stock created twice by one token |
| CW-SSN-08: effectiveness/headcount | §41 | Strength/rosters §12/29 | No literal deaths or replacement people from abstract Strength |
| Generic item and mode identity | §111 + SCL registry | §35 profile binding | No damage profile stacking or duplicate weapon item |
| All 11 domain workflows | §§113–123 | Specialized Part III procedures | No second payroll, clinic, intelligence or competition engine |

**Terminology correction:** Core's confirmed version resolves CW-SSN-01–08 already. No “pending Core Workshop promotion” remains a dependency. SCL 1.0 is the current *normative catalogue* but does not promote source-backed held content or supply a new numeric SSN adapter. This engine retains the exact selected numerical profile for each game mechanism and its original source status.

## 40. CMRR conflict and exclusion register

| ID | Original conflict or unsafe integration | Rebuilt decision | Accounted outcome |
|---|---|---|---|
| C01 | Original SNWE previously pinned Core v2.1 and proposed CDI/Pass A as separate parents | Replace with the single complete `IRGS-CORE-3.2` parent | Historical texts retained for source genealogy only |
| C02 | Original called CW-SSN-01–08 proposed pending Core approval | Bind every candidate to its already received 3.2 provider | No second runtime implementation |
| C03 | SCL 1.0's label suggests new `@1.0` canonical typed IDs | Keep unchanged `SCL:PBC…@0.2` exact refs; typed proposals noncanonical | Preserves all 1,416 original aliases and source selectors |
| C04 | SCL held content can be mistaken for adopted complete gear | Retain 228 held; use exact source-backed profile or require a missing data ruling | No invented prices/mass/protection or premature deprecation |
| C05 | SCL Fantasy weapon modes could replace SSN Taijutsu damage | Store compatible common physical definition; SSN chosen numeric effect remains sole combat adapter | No double attack/mitigation |
| C06 | R0.1 fixed one-damage minimum where all physical mitigation absorbs nominal effect | Keep R0.1 gameplay chip result; do not infer penetration or compound tissue injury | Flag cause interpretation and high-Level scaling calibration |
| C07 | Native two-stage Precision versus Core generic dice | Keep Mold + applicable d20 release only as distinct SSN uncertainties; no extra Core roll | Retained native balance gap |
| C08 | Resource pool and throughput might use same quantity or deduct twice | Native CU/SP is actor-owned with single cost and output counter; §109 semantics | No SCL-stock Chakra and no extra drain |
| C09 | Abstract Supply/RP versus real currency/inventory | Select abstract or exact backed conversion/replacement per scope and interval | No universal ryō exchange or duplicate quarterly economy |
| C10 | Mission clocks/downtime actions versus real work | Abstract scenario procedure permitted only in selected mode; persistent mode references real intervals/work | No one segment = one hour claim or clock manufacture |
| C11 | Temporary jutsu construct versus permanent resource | Require technique-level explicit persistence, matter origin/quality and services | No indefinite wall, water or timber from combat effect alone |
| C12 | Perceived Genjutsu state versus objective evidence | Perception/misdirection recorded with source; physical truth unchanged absent authorized effect | No phantom witnesses or cloned inventory |
| C13 | Summoned beings and clones can be counted twice | Use §55 embodiment/control; SSN action/upkeep/identity mechanisms; K-POP if genuine population | No unlimited parallel turns or duplicated actors |
| C14 | HP/Injury/Trauma/MRICS versus Core clinical conditions | One K-ACTOR condition state with native SSN numerics; MED distinct care work | No double damage, recovery or treatment |
| C15 | SSN unit Strength versus actual casualties | Preserve separate effectiveness; resolve actual casualties only by supported model | No fabricated deaths or revived personnel |
| C16 | SSN social Pressure/Standing versus Core relationships | Retain written numerical SSN track, Core retains individual relationships and audiences | No second persuasion roll, no compelled PC thoughts |
| C17 | Destiny intervention and already settled history | §99 intervention/retcon contract with native cost/Toll | No contradiction or free erasure of obligations |
| C18 | Training, rank, proficiency, Band, Level all treated as advancement | Separate actor capability, evidence and institutional appointment | No promotion=stat bonus, free jutsu or universal legacy inheritance |
| C19 | SCL full Shinobi content assumed to exist | R0.1 starter entries only + source-backed historical corpus retained as pending | No fabricated legacy jutsu or clan catalogue |
| C20 | Published fixture counts can be mislabeled playtesting | Distinguish inherited Core/SCL checks, current source checks, bounded new fixtures and pending field play | No false calibration/validation |

### Accounted removals and retained status

**Removed from active SNWE runtime:** duplicate descriptions of a separate proposed Core event journal, Core d100 as an additional SSN roll, the need to run CDI/Pass A concurrently, implicit use of Fantasy Threat/Defeat/injury on SSN attacks, and silent SCL1.0 typed-ID promotion. These are rejected *interpretations or obsolete dependency instructions*, not loss of a unique native mechanic.

**Retained unchanged:** All R0.1 native 14 chapter bodies, its starting array, native Resource table, hit/armor/damage formula, class/Path/proficiency rules, chakra mechanics, jutsu catalogue, social, mission, economy, war, Destiny, DSSN, R01–R40 decisions and S01–S48 register. All specialized world-conversion functions 17–33 have receiving destinations; new specialized §§34–36 add no compulsory numbers. SSN archives, alternative formulas and old source references are preserved as archival records, not reactivated.

**No campaign removals, retrospective conversions or source mutations occur.** SCL1.0's 22 added relations are non-instantiating metadata, not deleted or excluded; they are usable only through their verified selectors and unchanged model dependencies.

## 41. Complete SNWE R0.3 receiving manifest and runtime interface

**New proposed engine binding:** `IRGS-BIND-SNWE-0.3-CORE-3.2`, recorded in the companion file `IRGS_SNWE_R0_3_Core3_2_Receiving_Binding.json`. It is a genre-side receiving record; the downloaded Core v3.2 binding register is preserved **byte-for-byte**. The existing `SSN_EXTRACTION` contract authorizes the shared portable interface only.

```yaml
engine_id: IRGS-SNWE-0.3
design_status: proposed_complete_receiving_edition
core: IRGS-CORE-3.2
core_sha256: 1817cc01bed02c8cb21bae393878e9234743ea4c538d25e1a4a8934182abf738
core_bindings_sha256: e7d6a4250921787b673e4c2974711b3dc53a3b5d3a344a09da8ec9995242b0b7
catalogue: IRGS-SCL-1.0
catalogue_sha256: 4f0a90687958bd6d54b0ab21dc0cfac4e02e0ed40992a3b86eb1cf1725164376
registry_sha256: 67c4e0eb4b67fbc8f2cf874dae06381bf2e4c9eb48850a35d7ffc10c8a4a35b9
content_identity_revision: '0.2'
parent_portable_contract: IRGS-BIND-SSN_EXTRACTION-3.2
engine_specific_contract: IRGS-BIND-SNWE-0.3-CORE-3.2
resolution: native_SSN_2d6_task_plus_d20_hits_as_written
attack_effect_and_armor: native_SSN_R0.1_only
conditions_and_recovery: native_SSN_R0.1_with_single_Core_actor_owner
strategic: native_SSN_mission_and_Era_models_with_real_Core_people_and_assets
abstract_economy: select_native_abstract_or_exact_persistent_bridge
content: selected_SCL_contract_or_exact_retained_source_adapter_only
content_hold_promotions: none
original_native_chapters: 1-14
world_conversion_sections: 17-36
archive: R01-R40_and_S01-S48
core_deployment_appendix: B
core_acceptance_appendix: C
core_optional_profiles_appendix: D
campaign_adoption: not_applied
prospective_migration: not_applied
```

### Owner-qualified handoffs

- **K-TIME:** one event ID, causal timestamp, commitment and replay coverage; native rounds/turns are selected views of that time.
- **K-ACTOR / MED:** HP/SP/CU/Trauma/Injury and applied treatment affect the same actor; no extra parallel medical damage chain.
- **K-STOCK / K-ASSET / ECO:** physical rations, medical supplies, ammunition, real cash and equipment transfer only under actual owner-qualified events; Supply and Resource Points remain abstract unless an exact backed bridge is selected.
- **K-WORK / K-NET / CIV / URBAN:** physical jutsu-assisted production, work, access and infrastructure require measured feasible effect and completed acceptance; abstract clock completion is not new physical stock.
- **K-INFO / INTEL / INV:** sight, illusions, sensors, decoded reports and delays modify received beliefs/evidence, not historic physical outcomes.
- **K-ORG / GOV / LIFE / COMP:** village authority, exams, rank appointments, wages, service/career changes and successor identity follow distinct records and decisions.
- **K-POP:** named/cohort population is conserved across battle Strength summaries, medical statuses, transit and scale shifts.

### Activation and incomplete parameters

This engine provides no world-creation default setting, full jutsu library, magical industrial output rate, village wage scale or universal model for bloodline power. Before the relevant action is committed, bind a supported source-native technique, a compatible Core service model, actual source/target, required means, time/rate/units, and limited consequences. If a material quantity is unavailable, defer that calculation while independent feasible activity continues; do not secretly choose a number or create another authoritative store.

## 42. Retained and updated acceptance requirements

| ID | Fixture | Required result | Verification type |
|---|---|---|---|
| SNE32-01 | Copy native chapters 1–14 | Source paragraphs identical after removing editorial boundary notes | Automated source invariant |
| SNE32-02 | R01–R40 and S01–S48 retained | Every ID present once in preserved archive | Automated source invariant |
| SNE32-03 | Core 3.2 provider pin | Every CW-SSN-01–08 resolves to v3.2 receiving destinations | Source/section check |
| SNE32-04 | SCL content status | 279 original families, 51 selected/228 held; 1,416 aliases preserved | Registry integrity check |
| SNE32-05 | Unarmed and physical weapon modes | No item instantiation from method; two modes one physical family | Registry/type reference check |
| SNE32-06 | R0.1 three paid C casts | Costs 5, 6, 7; one actor/rank/scene counter | Bounded native computation |
| SNE32-07 | Overclock multiple crossings | One threshold Trauma per round plus distinct written sources | Bounded native computation |
| SNE32-08 | Damage mitigation | SSN-only chain, successful damaged attack floor, no inferred physical penetration | Bounded native logic |
| SNE32-09 | Chakra/rest split | Time/frequency preserves actual recoverable intervals, no extra rest by scene split | Bounded event/interval invariant |
| SNE32-10 | Inactive/dead actors do not act | No free action from summoned/illusory actor state | Specified scenario |
| SNE32-11 | Illusory clone | Observation may change; actual named headcount and stock unchanged | Bounded synthetic state |
| SNE32-12 | Summoned persistent being | One actor embodiment and valid command budget | Specified scenario |
| SNE32-13 | Field Mending | Health modification, Injury unchanged and 1/scene restriction | Bounded synthetic state |
| SNE32-14 | Abstract Supply | Token redeemable only once, actual inventory only on authorized issue | Bounded synthetic state |
| SNE32-15 | Quarterly RP | One credit per distinct three-month Era period | Bounded synthetic event |
| SNE32-16 | Research failure / physical work | A setback cannot erase accepted physical output without actual rework/loss | Bounded synthetic state |
| SNE32-17 | Battle Strength/headcount | Combat effectiveness changes, no invented deaths | Bounded synthetic state |
| SNE32-18 | Orders/receipt/observer | Actual occurrence, sensing, report, receipt and execution remain distinct | Bounded synthetic state |
| SNE32-19 | Village diffusion | One caster ability does not become an institution-wide service without support | Specified cross-domain scenario |
| SNE32-20 | Chūnin exam | Judged COMP result does not automatically authorize Rank/issue/pay | Specified cross-domain scenario |
| SNE32-21 | Destiny flashback/rescue | Scope/cost/Toll; no overwritten settled claims and actor agency | Specified scenario |
| SNE32-22 | Atomic replay | Same applied identity inert; changed payload rejected; no partial debit | Bounded synthetic event |
| SNE32-23 | Save/load/scale boundary | Work, consumed CU, queued effects, populations preserved | Specified runtime scenario |
| SNE32-24 | Autonomous peaceful period | No spontaneous danger, resources, immigration, skills or catastrophic change | Specified sustained scenario |
| SNE32-25 | SCL held source | Exact original payload/mode and adapter required; no completed fantasy defaults | Registry/source check |
| SNE32-26 | Campaign migration | Preserves actual identities/stocks/claims/injuries/knowledge and event journal; prospectively rebinding only | Specified prospective test |

**Execution evidence:** The companion verification report records which checks were actually run. Entries marked “specified” are requirements, *not* passes. Core 3.1's inherited 84 receiving checks, and the independent Core 3.2/R2 and SCL 1.0 release checks, belong to their original release evidence and are **not** fresh SNWE R0.3 combined-runtime results.

## 43. Calibration and unresolved work

| Area | Precise unresolved question | Needed demonstration |
|---|---|---|
| Direct damage/armor | Native min-one Health despite blocked physical penetration; Taijutsu multi-dice growth versus fixed-rank Ninjutsu | Exact probability sweeps and physical/game-state interpretation |
| Precision and chakra | Two-stage Mold/d20 success, resource economy, escalation, late-game reserve abundance | Encounter/campaign economy across Levels 1, 10, 20 |
| Body/condition interactions | Injury-check severity and recovery at different frequencies, trauma stacking and independent channel effects | Sustained combat/care traces including repeated wounds |
| Physical production | Technique-specific material source, quantity, quality, persistence, work rate and fatigue | Explicit jutsu-profiled work/services and edge cases |
| Travel | Zone distance versus overland travel and actual burden | Declared technique speeds, cost and transport profiles |
| Civil population adoption | Chakra prevalence, credentials, labor time, output and service access | Named practitioners/institutions and supported uptake modeling |
| Personal economy | Token-to-stock and RP-to-finance backing; organization budget | Choose either abstract profile or completed nonduplicating binding |
| Military | Native Strength versus actual casualties, morale, wounded recovery, reconnaissance and real supply | Character/unit/Era scale transition with conserved people |
| Exceptional authority | Destiny flashback factual scope, resurrection/cosmology, artifact power and setting permissions | Scope-aware replay-safe extraordinary cases |
| Institutions/society | Kage/clan rights, exams, Academy qualification, secrecy and reporting | Detailed selected setting/module records and local policy |
| Content | Complete jutsu corpus, summoning/clan/bloodline lists and correct SSC/native adaptation | Item-by-item source recovery and profile testing |
| Software/playtests | Same state and rolls produces same applied events for independent runners | Executable runtime, two-runner reproducibility and actual interactive play |

**No invented filler numbers:** All new proposed world model rates must have a unit, valid envelope, actual sources, triggering interval, applicable setting/profile and calibration/status. Unknown values block only their dependent calculations.

## 44. Prospective adoption and migration

This is a **complete proposed rebuild** of the genre edition, not a patch. It does not migrate or retcon current campaigns and does not automatically select SCL 1.0 for every existing campaign; the receiving baseline is selected for this new edition.

**Adoption gates:** verify native preservation, authenticate required v3.2/SCL reference bytes and readiness, execute behavioral integration cases, choose complete live profiles, resolve material conflicts, complete necessary specialized setting content, test prolonged autonomous campaigns, document calibration debt, then explicitly adopt this engine for the desired scope/version/effective time.

**Migration procedure:** freeze a canonical checkpoint; inventory old source/profile versions, actors, physical locations/embodiments, inventory, money, Supply/RP claims, promises, work, injuries/trauma, techniques/permissions, offices, actual population, state history, rolled/retained uncertainty, pending events and recipient knowledge. Map each independently. For unsupported mappings preserve the previous implementation for the affected existing rule or make a named prospective decision under actual authority. No free healing, equipment, promotion, currency, work, time, people, knowledge or dramatic history follows from a version change. Resume at the same meaningful decision point without replay.

## 45. R0.3 complete change log, accounted removals and provenance

| Change | R0.2 source state | R0.3 disposition |
|---|---|---|
| R32-01 Parent version | Core 3.1 baseline | Select exact Core 3.2 release and SHA-256; preserve prior source as provenance |
| R32-02 Content release | SCL1.0 described as candidate | Recognize SCL1.0 as Core3.2 current normative catalogue; retain 228 holds, unchanged `@0.2` handles |
| R32-03 Deployment reference | Older Appendix C | Point to new Appendix B and Core §112 |
| R32-04 Acceptance reference | Older Appendix D | Point to Appendix C and retained genre tests |
| R32-05 Historical provenance | Core3.1 Appendix G cited as current receiving evidence | Core3.1 Appendix G is history; actual same provider sections verified in 3.2 |
| R32-06 Genre binding | `SSN_EXTRACTION` was portable but not a full engine | Add separate proposed SNWE engine receiving manifest, keep Core original immutable |
| R32-07 Native profile | 14 complete SSN chapters | Retain native passage text; only 14 separately labeled receiving notes retargeted |
| R32-08 World conversion | Sections 17–36 | Retain all twenty sections and their scoped specialized functions, change only receiving references |
| R32-09 Historical recovery | R01–R40/S01–S48 | Preserve exact archive, no source rewriting |
| R32-10 Gameplay evidence | Bounded Core3.2 replay 31/31 and 15/15 seed continuity | Carry as earlier bounded evidence, rerun source/model checks; no invented live gameplay certification |

**Accounted removals:** Old *active* dependency claims that Core3.1 and SCL0.2 are current are superseded; the content hold rules, source identities, previous engine source file and historical provenance are not deleted. The obsolete current-reference meanings of Core3.1 Appendices C/D/G are replaced by Core3.2 Appendices B/C and archived provenance. No universal rule, native numeric method, SSN fiction, campaign person, resource or project is removed.

**Unchanged native content:** All source passages in Chapters 1–14; all decisions R01–R40 and references S01–S48; all specialized §17–36 functions. No automatic import of Fantasy/Space/Roman numerical values or unrelated campaigns. No unrequested retroactivity or source deprecation.

## 46. Core 3.2 / SCL 1.0 receiving acceptance and evidence ledger

| ID | Required observation | Test classification | Current evidence |
|---|---|---|---|
| SNE32-R01 | Same native R0.1 Chapters 1–14 after removing editorial receiving notes | Exact source-body comparison | Executed in accompanying source verifier |
| SNE32-R02 | Decision register R01–R40 and S01–S48 preserved byte-for-byte within the archived Part IV body | Exact source comparison | Executed |
| SNE32-R03 | Core file hashes, provider and archive references match R2 | SHA-256 and schema/heading inspection | Executed |
| SNE32-R04 | 51 selected / 228 held, all 1,416 aliases unchanged; no content promotion | Registry and release manifest inspection | Executed |
| SNE32-R05 | Native C-rank escalation 5+6+7=18; output threshold cost charged once | Bounded native computation | Executed |
| SNE32-R06 | One hour rest at 60 maximum chakra can grant 15 CU; cap at maximum | Bounded native computation | Executed |
| SNE32-R07 | SSN damage 7 raw, DR 2, armor 9 → native 1 HP floor after confirmed damage | Bounded native computation | Executed |
| SNE32-R08 | Same event replay once; changed payload under same ID rejected | Bounded reference fixture / prior Core3.2 campaign replay | Prior 31-check Core3.2 regression; not new production runtime pass |
| SNE32-R09 | Ten-day scenario 44 events, 15 seeded continuity cases remain identical | Prior executed reference campaign harness | Prior 31-check regression with 15/15 continuations; not a new open-world test |
| SNE32-R10 | Source-native SSN event correctly updates K-ACTOR/K-ASSET/K-STOCK/K-INFO without duplicate owner | Specified integrated test | **Pending** |
| SNE32-R11 | Missing chakra-technique material-production rate does not invent stock | Specified integrated test | **Pending** |
| SNE32-R12 | Named/cohort casualties, wounds and Strength remain conserved across tactical/era cuts | Specified integrated test | **Pending** |
| SNE32-R13 | One clinic and two competing institutional orders allocate scarce personnel without duplicate time | Specified integrated test | **Pending** |
| SNE32-R14 | Two independent runners reproduce event IDs, state and recipient information after save/resume | Specified independent runtime test | **Pending** |

Retain the complete prior SNE31-01–26 scope under renumbered SNE32-01–26 in §42. The release's 420 authored held-family acceptance cases and Core Appendix C 223 acceptance cases are **requirements**, not all executed game simulations. Passing package checks and reproducing older fixtures are not balance calibration or unrestricted interactive campaign playtests.

## 47. Prospective adoption, calibration and migration impact

**Status:** Written and mechanically rebound, not adopted. The new document can be selected for a new proposed campaign; its deployment must record Core/SCL/engine hashes, chosen native models, enabled extraordinary modules, actually available content, selected profiles, known missing parameters and the meaningful initial player decision.

**Existing campaign migration:** No automatic migration. At an authorized prospective cutover keep each actor ID, condition and current pool; inventories, item modes, title and locations; actual and abstract claims; injury/care state; offices and orders; active or disabled techniques; clock/work completion; random records; applied event IDs; reports in flight; and the exact decision frontier. Rebind only identified interfaces. Replays are no-op; conflicting identity/payload is a reconciliation event. No free healing, food, money, promotion, retroactive loss, jutsu access or clock progress is conferred by the new parent pin.

**Calibration debt:** Character Level 1–20 damage economy and d20 accuracy; one-HP floor interpretation; C/B/A/S resource rates and overclock; treatment, injury and Chakra recovery; emergency actions; abstract-to-physical Supply/RP mapping; jutsu transport/production throughput; village education and budget; unit effectiveness and casualties; summoned independent actor constraints; Destiny and irreversible event authorizations. Choose numerical parameters only where actual decisions require them, with source, units, envelope, bounds and failure behavior.

**Release outcome:** Complete Core3.2-linked candidate with native source conservation and document/arithmetical verification, not a claim that any unmodeled capability, runtime integration, high-level calibration or open-ended multiplayer gameplay has already passed.
