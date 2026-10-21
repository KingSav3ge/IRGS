# IRGS — Fantasy Content Library
## Version 2.0 — Shared-Catalogue Rebuild (Proposed)

**Document ID:** `IRGS-FANTASY-LIB-2.0`  
**Classification:** Genre content library / native adapter specification (not a replacement Core engine)  
**Core dependency:** `IRGS-CORE-3.2`  
**Shared catalogue:** `IRGS-SCL-1.0`, normative `IRGS_Shared_Content_Registry_v1_0.json`  
**Fantasy source:** `Fantasy Content Libraries v1.0` (`FL-1.0`), plus `Core Fantasy World Engine v1.0` (`F-1.0`) for its native numerical profiles  
**Status:** **Proposed / internally reconciled / structurally verified.** Not adopted into any campaign.  
**Scope:** Grounded to mythic fantasy and any setting enabling particular fantasy content.

> **Release meaning:** This is a complete rebuilt fantasy content specification, not an adoption of new rules or numerical calibration. Definitions, adapters, genre templates and actual campaign state remain different records. Source-preserved `FL-1.0` statistics may be used only under a compatible chosen Fantasy model; Core v3.2 never treats those statistics as universal.

## Part I — Purpose and authority

This library is deliberately slimmer than its predecessor at the **generic-definition** layer. Every mundane category already present in the Shared Content Library is referenced, not re-authored. This document retains the Fantasy-native operational values, supernatural archetypes, genre-specific interfaces, campaign construction and edge cases. The original Fantasy v1.0 and its Core Fantasy v1.0 source are archived in this release as **provenance, not parallel active Core providers**.

**Precedence:** current direction → adopted campaign override → adopted compatible genre specification → Core v3.2 → selected content adapter/profile → proposal where none applies. An original value labelled `Core` in the old Fantasy library means *Core Fantasy v1.0*, not automatic promotion to Core v3.2. Existing campaign precedence and historical resolutions remain untouched.

**Authoritative write ownership:** Core owns actors/organizations, actual stock and objects, conditions/injury, time/work, information, authority, services, projects and continuity. SCL supplies read-only qualitative family definitions and composition metadata. This Fantasy library supplies genre-specific extraordinary content and pinned optional native performance adapters. Setting/campaign determines which entries exist and sets actual parameters. Never create inventory or cast a spell simply by looking up a library entry.

**Canonical identity:** Preserve `SCL:<PBC-family>@0.2` with exact selector (where present). `IRGS-SCL-1.0` is the release version, not a command to rewrite `@0.2`. The CSV crosswalk accompanying this document resolves **all 111 FL-1.0 source bindings:** **95 shared-family bindings** and **16 scoped Fantasy extensions**; it retains original source line, native adapter ref and immutable payload checksum. The **61 original Fantasy adapters** remain in the SCL registry; they are not redefined as global Core ratings.

**Three gates:** (1) reference identity; (2) activation with actual compatible means, model and constraints; (3) deprecation only after qualified scope, explicit adoption and continuity-preserving migration. A selected qualitative SCL entry is not necessarily numerically calibrated. A held SCL entry is looked up through its exact preserved FL source definition. The 228 held families in the overall SCL do not become selected because this library can cite them.

### Runtime binding contract

`CampaignProfile | Core 3.2 | SCL 1.0 registry | selected Fantasy genre ruleset/revision | selected mechanical adapter IDs | enabled paradigm IDs | source-qualified technique/equipment/profile IDs | calibration evidence | actual state refs | overrides`

A compatible native profile must be **complete** for the required interaction. If a Fantasy v1.0 attack uses `Threat` and `Defeat`, use a declared compatible Fantasy protection/injury chain; do not graft just its damage number into an unrelated health system. If the campaign selects a different combat system, provide a derived adapter with documented units, assumptions and test evidence. Unsupported quantitative resolution is held while unrelated supported actions continue.

### Record provenance and readiness

Every operative record names `ID | source/version | semantic type | owner | reference | selector | adapter/model | limits | activation | uncertainty | adoption scope`. Statuses are independently: source-established, SCL-selected/held, genre-established/proposed, campaign-adopted, implementation-tested, calibrated and live-playtested. Similar words are not interchangeable.

## Part II — Equipment and mundane content: references plus Fantasy adapters

### 1. Retained shared definitions

The **object/material/anatomy/template definitions** below belong to the SCL, not this genre library. Fetch them by the accompanying crosswalk or normative registry:

| Original FL families | Shared owner | Fantasy-owned remainder |
|---|---|---|
| `WPN-M-*`, `WPN-R-*` | Physical weapon families; each method/mode selector; unarmed as method | Reach, Threat, Armor Defeat, reloading, weapon-control/handling values under selected Fantasy profile |
| `ARM-*`, `COV-*` | Armor construction and coverage geometry | Cut/Pierce/Impact ratings and location handling under native Fantasy protection |
| `SHD-*` | Shield objects and coverage | Fantasy Defense/Structure values and stress handling |
| `MAT-*` | Material physical definitions | Effect of magical treatment and selected Fantasy construction calibration |
| `BODY-*` | Body-plan templates | Selected Fantasy unresolved-hit mapping and specific physiology |
| `NAT-*`, `CRT-*` | Natural action and behavior/ecology patterns | Threat, Defeat, Force, Exposure, anatomical constraints and exceptional faculties specific to a species |

These shared families **do not guarantee availability, ownership, technology, training or unit performance**. Historical, fantasy and modern variants may share the family label while using different equipment designs and adapters. Composition uses SCL operations (`inherit`, `set supported`, `unknown`, `not applicable`, `remove`) rather than raw addition of totals.

### 2. Weapon-trait mechanics (FL-1.0 native profile)

| Trait | Relevant operational effect under original Fantasy v1.0 | Restriction |
|---|---|---|
| Brace | +1 **Force** for actual prepared impact on a materially charging target | Contact, geometry and commitment required; no free attack |
| Concealable | Smaller/concealable construction changes hiding feasibility | No automatic universal stealth bonus |
| Defensive | +5 circumstance for feasible weapon-control contest | Not generic +5 to every defense |
| Hook | +5 for a physically applicable trip/pull/disarm/shield manipulation | No skill-created leverage |
| Long | At too-close geometry, −10 for affected mode or infeasible | Minimum reach is mode-specific |
| Two-Handed | Requires two functioning hands for normal mode | Alternate mode must be defined |
| Versatile | Distinct one-/two-hand or range modes | Mode switch changes use, not asset count |
| Mounted | Built for mounted handling | No automatic damage from mounting alone |
| Sunder +N | Adds N to material/shield **stress** where applicable | Never to flesh Injury Grade |
| Reload N | N primary commitments before the next normal discharge | Real ammunition/loading tools needed |

Other recorded labels such as `Concussive`, `Mechanical`, `Recoverable`, `Fast cycle`, `Capacity-gated` and `Compact` remain **descriptive until their specific profile resolves the actual effect**. Do not assume a constant bonus because a label exists. Default native Fantasy combat assumptions remain pinned to their original owning F-1.0 ruleset.

### 3. Melee source-calibration table

These numbers are **original FL-1.0 profiles**; the physical family and modes are SCL-owned. `—` means no Armor-Defeat value is defined for that damage channel, **not** a zero-value attack. Newly proposed FL profiles are not historical calibration evidence.

| ID | Weapon/mode | Reach | Threat | Defeat | Traits | Status |
|---|---|---|---|---|---|---|
| WPN-M-001 | Unarmed strike | 0–1 | 0 | — | — | Core |
| WPN-M-002 | Club | 1–2 | 1 | — | Concussive | Core-derived |
| WPN-M-003 | Staff | 1–3 | 1 | — | Defensive, Two-Handed | Proposed |
| WPN-M-004A | Dagger thrust | 0–1 | 1 | 1 | Concealable | Core |
| WPN-M-004B | Dagger cut | 0–1 | 1 | 0 | Concealable | Proposed |
| WPN-M-005A | Short blade cut | 1–2 | 1 | 1 | — | Proposed |
| WPN-M-005B | Short blade thrust | 1–2 | 1 | 1 | — | Proposed |
| WPN-M-006A | Sword cut | 1–2 | 2 | 1 | Defensive | Core |
| WPN-M-006B | Sword thrust | 1–2 | 2 | 2 | Defensive | Core |
| WPN-M-007A | Longsword cut | 1–3 | 2 | 1 | Versatile, Defensive | Core |
| WPN-M-007B | Longsword thrust | 1–3 | 2 | 2 | Versatile | Core |
| WPN-M-008A | Great blade cut | 2–3 | 3 | 2 | Two-Handed, Sunder +1 | Proposed |
| WPN-M-008B | Great blade thrust | 2–3 | 2 | 2 | Two-Handed | Proposed |
| WPN-M-009 | Hand axe | 1–2 | 2 | 2 | Hook, Sunder +1 | Core-expanded |
| WPN-M-010 | Battle axe | 2–3 | 3 | 2 | Two-Handed, Sunder +1 | Core |
| WPN-M-011 | Mace | 1–2 | 2 | — | Concussive | Core |
| WPN-M-012A | Warhammer face | 1–2 | 3 | — | Sunder +1 | Core-expanded |
| WPN-M-012B | Warhammer pick | 1–2 | 3 | 2 | Sunder +1 | Core |
| WPN-M-013 | Spear thrust | 2–3 | 2 | 2 | Brace | Core |
| WPN-M-014 | Pike thrust | 3–4 | 2 | 2 | Brace, Long, Two-Handed | Proposed |
| WPN-M-015A | Poleaxe edge | 2–4 | 3 | 2 | Long, Two-Handed, Sunder +1 | Proposed |
| WPN-M-015B | Poleaxe spike | 2–4 | 3 | 3 | Long, Two-Handed, Sunder +1 | Proposed |
| WPN-M-015C | Poleaxe hammer | 2–4 | 3 | — | Long, Two-Handed, Sunder +1 | Proposed |

**Mode and inventory rule:** `WPN-M-006A` and `WPN-M-006B` resolve through the same shared sword family with `modes.cut` and `modes.thrust`; a sword is one physical object. `WPN-M-001` is an unarmed **method**, never a carried weapon. Native source tags `Core`, `Core-expanded` and `Proposed` retain their historical Fantasy v1.0 meaning.

### 4. Ranged source-calibration table

| ID | Weapon | Mode | Threat | Defeat | Reload | Traits | Status |
|---|---|---|---|---|---|---|---|
| WPN-R-001 | Throwing knife | Pierce | 1 | 1 | 0 | Recoverable | Core |
| WPN-R-002 | Javelin | Pierce | 2 | 1 | 0 | Thrown | Core |
| WPN-R-003 | Throwing axe | Cut | 2 | 1 | 0 | Sunder +1 | Proposed |
| WPN-R-004 | Sling | Blunt | 1 | — | 0 | Compact | Core |
| WPN-R-005 | Shortbow | Pierce | 1 | 1 | 0 | Fast cycle | Core |
| WPN-R-006 | Warbow | Pierce | 2 | 1–2 | 0 | Capacity-gated | Core-expanded |
| WPN-R-007 | Light crossbow | Pierce | 2 | 2 | 1 | Mechanical | Core |
| WPN-R-008 | Heavy crossbow | Pierce | 3 | 3 | 2 | Two-Handed, Mechanical | Core |

`WPN-R-006` requires actual draw capacity: skill cannot replace insufficient force. An ammunition item has its own actual stock and may change Threat, Defeat, range or protection interaction through a compatible selected profile. `Reload 0` does not create ammunition or guarantee a projectile is loaded; recovery requires an actual search/retrieval event. For all ranged weapons, distance thresholds require local calibration, not a guessed universal range.

### 5. Armor construction: native numbers only

| ID | Construction | Cut | Pierce | Impact | Notes | Status |
|---|---|---|---|---|---|---|
| ARM-001 | Ordinary clothing | 0 | 0 | 0 | Not meaningful armor | Core |
| ARM-002 | Padded textile | 1 | 0 | 1 | Flexible foundation | Core |
| ARM-003 | Soft leather | 1 | 1 | 1 | Flexible | Core |
| ARM-004 | Hardened/reinforced leather | 2 | 1 | 1 | Rigid/flexible composite | Core |
| ARM-005 | Mail | 3 | 2 | 1 | Strong vs cut | Core |
| ARM-006 | Mail over padded foundation | 3 | 2 | 2 | Integrated harness | Proposed |
| ARM-007 | Scale/lamellar harness | 3 | 3 | 2 | Direction/construction sensitive | Proposed |
| ARM-008 | Brigandine/coat of plates | 4 | 3 | 2 | Overlapping rigid elements | Core |
| ARM-009 | Plate component | 5 | 4 | 3 | Rigid articulated protection | Core |
| ARM-010 | Heavy exceptional mundane plate | 5 | 5 | 3 | Requires setting justification | Proposed ceiling profile |

**Coverage lives in SCL:** `COV-01`–`COV-11` remain separate from construction, material, quality, fit and damage. Use actual covered regions; a 'full harness' includes possible gaps. Physical layers are not mechanically summed: an integrated mail-and-padding harness (`ARM-006`) is a single selected profile. Contact → appropriate protective channel → residual force → actual condition/injury; do not apply protection twice from the same layer.

### 6. Shields: native numbers only

| ID | Shield | Defense | Structure | Typical use |
|---|---|---|---|---|
| SHD-001 | Buckler | −5 | 2 | weapon-control, close defense |
| SHD-002 | Small shield | −10 | 2 | mobile personal defense |
| SHD-003 | Reinforced round/heater shield | −10 | 3 | broad mobile defense |
| SHD-004 | Large/kite shield | −15 frontal | 3 | broad coverage |
| SHD-005 | Heavy metal-faced shield | −15 frontal | 3 | durable broad protection |
| SHD-006 | Pavise | up to −20 ranged | 4 | deployed/mobile cover |

Apply a shield's Defense only to attacks its geometry and readiness can plausibly intercept. Structure addresses shield condition and material stress, not a second body-injury reduction. Two shield names referring to one actual shield cannot produce two simultaneously accumulated bonuses. Values retain FL-1.0 native status and are not cross-genre certification.

### 7. Native handling and repair constraints

**Material versus quality:** SCL `MAT-001`–`MAT-013` supply material characteristics. A better metal or superior craft process can change particular properties through a justified setting variant, not grant every armor/weapon bonus at once. Repair changes actual damaged components with equipment, materials, time, competence and inspection. Nothing is repaired by opening a new tactical scene.

**Equipment/tech levels:** fantasy technology is setting-controlled. Chain, brigandine, crossbows, alchemical apparatus and magical foci are not globally available just because named here. Prices, rarity, labor rates, quality shifts and service infrastructure are setting-calibration inputs.

## Part III — Creature and natural-action Fantasy adapters

**Construction interface:** SCL `BODY-*`, `NAT-*` and `CRT-*` describe reusable physical forms and behaviors. A Fantasy species adds actual mass/scale, anatomy, locomotion, senses, needs, reproduction, protection, individual natural attack modes, cognition and supernatural traits. Characters do not gain a whole bestiary merely by enabling a category. Culture, language, learned practice and moral outlook are separate from ancestry and physiology.

### Optional original unresolved-hit profiles

Use only if an actual target region is unresolved and the selected Fantasy injury profile uses a d20 location adapter. These are source-proposed distributions, not measured species universals:

| Body plan | d20 | Location | Additional limit |
|---|---|---|---|
| `BODY-002` quadruped | 1–3 / 4–11 / 12–14 / 15–17 / 18–20 | Head/neck / torso / forelimb / hindlimb / rear body/tail | Tail becomes rear torso when no meaningful tail |
| `BODY-003` winged | 1–2 / 3–8 / 9–13 / 14–16 / 17–20 | Head/neck / torso / wing / leg/talon / wing root/tail/body | Wing injury affects flight only if relevant structures involved |
| `BODY-004` serpentine | 1–3 / 4–7 / 8–15 / 16–20 | Head / neck-forward / central body / rear-tail | Movement depends on actually affected musculature/structures |
| `BODY-001` humanoid | Fantasy World Engine F-1.0 humanoid table | Use exact parent profile | No universal SCL hit table |
| `BODY-005/006/007` | Species/component-specific | No general location roll supplied | Exoskeleton, amorphous body and construct components require specific anatomy |

### Natural-attack use

The original `NAT-001`–`NAT-010` delivery categories remain SCL references. Fantasy specializes them as follows. **Bite, claw, horn, slam, tail strike, stomp, constrict, quill, breath and venom are not automatic numerical attacks:** species, geometry and selected means determine effect. Grip must be the declared objective or an expressly coupled species capability. Constrict requires a preceding real grapple/wrap and another proper activity commitment. A charge may supply the original +1 Force *only when* the selected model, distance and momentum support it; do not add force already embedded in Threat. Venom is a dose/time-specific exposure, separate from contact injury. A predator's size must not add the same scale modifier again when native Threat already incorporates normal anatomy.

**Creature behavior:** `CRT-001`–`CRT-007` remain SCL behavior templates for solitary predators, pack hunters, chargers, flying hunters, swarms, constructs and colossi. A specific organism's autonomy depends on its own needs, goals, senses, learning and current constraints. Swarm losses reduce actual density and effect; constructed bodies use component/service condition, not arbitrary 'monster HP'. Monsters gain no free actions or immunity because of narrative status.

**Species record:** `Species ID | version | ecology | anatomy/body plan | size/mass | movement/flight | senses | cognition | needs | natural protection | natural delivery capabilities | mundane attack profiles | exceptional faculties | reproduction/lifespan | social organization | resource interfaces | actual variants | calibration evidence`. A template is not an actual character or population count.

## Part IV — Extraordinary materials (Fantasy-owned templates)

`XMAT-*` entries are the **five retained FL-1.0 scoped extensions**, not new `MAT-*` shared substances. They require explicit setting material identity, physical source, crafting constraints, market availability, repair route and a selected effect model. **None is enabled universally.** The original optional numerical ranges are **proposal/calibration placeholders**, not adopted defaults.

## 22. Extraordinary material profile

Fantasy materials use:

`Setting name | Mundane analogue | Mass multiplier | Protection shift | Defeat shift | Structure shift | Heat behavior | Magical interaction | Workability | Repair requirements | Rarity | Production source`

Every improvement must specify its cost or constraint.

---

### Original FL-1.0 extraordinary-material design notes

These are design templates, not universal fantasy substances.

### XMAT-L — Lightweight structural material

Typical purpose:

reduce mass/burden while retaining approximately equivalent protective behavior.

Possible setting calibration:

`Mass ×0.5–0.75`

Do not automatically increase Resistance.

---

### XMAT-H — Extreme hard/tough material

Possible behavior:

- +1 relevant Resistance;
- +1 Structure;
- +1 Armor Defeat for suitable edges.

Such benefits require:

- appropriate construction;
- difficult workability;
- rarity or production constraints.

Do not apply all three automatically.

---

### XMAT-C — Supernatural conductor

Mechanical purpose:

- channels magical effects;
- supports enchantment;
- stores or transmits supernatural resources.

It need not be physically stronger than steel.

---

### XMAT-I — Supernatural insulator

Mechanical purpose:

provide Resistance against one or more supernatural channels.

It may be physically poor armor.

---

### XMAT-R — Regenerative/living material

Mechanical purpose:

recover Local Stress or Condition through defined biological/supernatural processes.

It still requires:

- time;
- nutrients or magical resources;
- survival of the relevant material.

---

**Material composition gate:** extraordinary material changes *only named properties*. Heat protection, magical conductivity, density and Armor Defeat may be independent. Magical affinity is not necessarily physical durability. Recording a mass multiplier does not auto-create an identical protective behavior if impact transfer changes; recalibrate affected interfaces. `XMAT-R` replenishment requires a real supported nutrient/power/time source; neither repair nor creature growth occurs for free.

## Part V — Supernatural paradigms (Fantasy-only content)

The nine `PAR-*` templates below are **retained source material from FL-1.0**, made operational by Core §112's extraordinary-mechanism interface. Their names do not assert that a particular setting has them. Each enabled paradigm must explicitly answer: source, access, training, finite and recurrent costs, reach/scope, achievable causal effect, maintenance, duration, interruption, detection, resistance, counterplay, limits, social institutions and propagation of world effects. If an autonomous being is involved, it acts as an actor rather than as a resource meter.

**Effect binding:** Extraordinary effect → existing affected object/stock/actor/condition/location/information/authority/time, with actual quantities and event IDs. A magic system never owns a second parallel stock or injury ledger. Effects require the declared mechanism rather than universal bypass of physics, death or agency.

#### 46. Paradigm record

Every paradigm must establish:

`Source | Access | User requirements | Capacity | Method | Knowledge | Cost | Limits | Recovery | Detection | Resistance | Counterplay | Failure | Institutions | Prevalence | Economic effect | Military effect | Legal effect`

---

#### 47. Paradigm acceptance gate

A paradigm is incomplete unless the following questions can be answered:

- What supplies its power?
- Who can access it?
- Why cannot every user perform every effect?
- What is consumed or constrained?
- How is capability learned?
- What resists it?
- What interrupts it?
- How is it detected?
- What happens when use succeeds?
- What happens when it fails?
- How quickly does capacity return?
- What institutions have developed around it?
- What common uses changed society?

---

### 1. Arcane

#### 48. PAR-ARC — Manipulative Arcane Magic

**Status:** Generic paradigm template, not universal setting fact.

##### Source

An impersonal supernatural medium, field, law, substance, or structure.

##### Access

Usually:

- study;
- innate sensitivity plus study;
- tools/foci;
- formal techniques.

##### Capacity

Possible models:

- internal reserve;
- external draw;
- prepared patterns;
- focus tolerance.

##### Method

- formula;
- gesture;
- language;
- diagrams;
- ritual;
- mathematical/symbolic procedure.

##### Typical strengths

- reproducibility;
- teachability;
- broad technical specialization.

##### Typical limits

- knowledge;
- complexity;
- preparation;
- components;
- interruption.

##### Counterplay

- wards;
- interruption;
- dispelling;
- resource denial;
- counter-technique.

##### Institutional consequences

Likely where prevalent:

- schools;
- guilds;
- licensing;
- research;
- magical manufacturing.

No setting is required to contain any of these.

---

### 2. Divine

#### 49. PAR-DIV — Granted/Divine Power

Distinguish two fundamentally different systems.

##### Granted capability

The deity/power has already granted an ability.

Once granted, use operates according to the technique's rules.

##### Petitionary intervention

The practitioner is **requesting another autonomous entity to act**.

This is not ordinary spell execution.

The divine entity's:

- goals;
- promises;
- doctrine;
- relationship;
- willingness

matter.

Do not disguise an autonomous god as a mana pool.

##### Possible costs

- obligation;
- ritual;
- vow;
- offering;
- limited grant;
- office.

##### Counterplay

May include:

- severed access;
- desecration;
- opposing divine authority;
- broken covenant.

Setting profile must define what actually works.

---

### 3. Spirit and Primal

#### 50. PAR-SPR — Spirit/Relational Magic

##### Source

Autonomous or semi-autonomous:

- spirits;
- place-beings;
- ancestral entities;
- natural intelligences.

##### Access

Usually through:

- relationships;
- pacts;
- offerings;
- mediation;
- attunement.

##### Critical rule

**Contact does not equal control.**

##### Cost

May involve:

- offerings;
- obligation;
- taboo;
- negotiated service;
- reciprocal protection.

##### Strength

Local relationships may provide powerful context-specific effects.

##### Limitation

A practitioner cannot necessarily command an unrelated spirit merely because both belong to the same paradigm.

---

### 4. Psionic

#### 51. PAR-PSI — Psionic/Mental Capability

##### Source

Mind, nervous system, psychic field, or setting-defined equivalent.

##### Access

Innate and/or trained.

##### Typical resource

- concentration;
- strain;
- internal reserve;
- fatigue.

##### Typical channels

- Mental;
- Spiritual;
- physical only where explicitly converted.

##### Core restrictions

Telepathy accesses:

**information present in the target or channel**

not objective world truth.

Mind reading does not reveal facts the target does not know.

Precognition must define exactly what kind of information it provides.

---

### 5. Internal Energy

#### 52. PAR-INT — Internal Energy / Ki

##### Source

Actor's own physiological/supernatural internal system.

##### Access

Training and/or innate anatomy.

##### Typical strengths

- self-enhancement;
- movement;
- physical reinforcement;
- close-range projection.

##### Costs

Possible:

- internal reserve;
- Fatigue;
- concentration;
- recovery time.

##### Core limit

Skill cannot create superhuman physical effects merely because the discipline is named “Ki.”

Any superhuman:

- Force;
- speed;
- protection;
- healing

must explicitly declare its supernatural effect.

---

### 6. Sacrificial

#### 53. PAR-BLD — Blood/Sacrificial Magic

##### Source

Life, blood, tissue, sacrifice, or equivalent metaphysical principle.

##### Cost provenance

Every sacrifice must come from an actual:

- actor;
- stored material;
- ritual resource.

The source loses what was spent.

##### Anti-exploit rule

If magical healing can immediately restore sacrificed tissue/blood, the setting must explicitly decide whether this also restores the magical value sacrificed.

Otherwise:

> sacrifice → spell → healing → sacrifice

creates infinite power.

The default is:

**restoring physical tissue does not automatically restore already-expended supernatural sacrificial value.**

---

### 7. Runic

#### 54. PAR-RUN — Runic/Inscribed Magic

##### Source

Setting-defined supernatural power fixed through symbols, geometry, bindings, or inscriptions.

##### Strength

Preparation and persistence.

##### Typical method

Uses the project system.

##### Requirements

- substrate;
- design;
- tools;
- expertise;
- time;
- power source.

##### Failure

A failed inscription does not automatically explode.

Actual failure follows:

- flawed binding;
- incomplete function;
- wasted material;
- instability

where causally supported.

---

### 8. Alchemical

#### 55. PAR-ALC — Alchemical Magic

Use:

`Formula | Ingredients | Quantity | Purity | Equipment | Process | Time | Batch | Stability | Dose | Shelf life | Effect`

Production is an actual project.

A rare ingredient cannot be replaced by rolling higher unless the formula permits substitution.

Alchemy integrates naturally with:

- trade;
- harvesting;
- agriculture;
- mining;
- medicine;
- guilds.

---

### 9. Necromantic

#### 56. PAR-NEC — Death/Necromantic Magic

A setting must distinguish:

- corpse;
- biological life;
- consciousness;
- soul;
- memory;
- supernatural animation.

These are not interchangeable.

##### Reanimation

Animating a body does not automatically restore:

- identity;
- memory;
- personality;
- soul.

##### Resurrection

Restoring the original person requires whatever additional metaphysical mechanisms the setting defines.

##### Corpse state

The corpse retains:

- location;
- condition;
- ownership/legal status;
- decomposition;
- injuries.

Death magic does not receive permission to ignore physical state unless its effect explicitly does so.

---

### 10. Interaction

#### 57. Multiple paradigms

A setting may contain several paradigms.

Do not assume they:

- share resources;
- share terminology;
- use the same countermeasures;
- detect each other;
- cooperate.

Each pair should establish interaction where relevant.

Example matrix fields:

| Interaction | Arcane | Divine | Spirit |
|---|---|---|---|
| Can detect | setting-defined | setting-defined | setting-defined |
| Can dispel | setting-defined | setting-defined | setting-defined |
| Shared ward | setting-defined | setting-defined | setting-defined |
| Resource compatibility | setting-defined | setting-defined | setting-defined |

---

### Paradigm interface checks

1. **Arcane**: no guaranteed 'mana pool'; costs must be selected from actual operating model.
2. **Granted versus petitionary divine**: a retained grant is executable under its grant terms; a petition is a request to another autonomous actor. No automatic compelled compliance.
3. **Spirits**: contact, permission and actual control are separate.
4. **Psionics**: perception accesses target-available information, not objective unknown truth; mental harm requires declared channels.
5. **Ki**: a superhuman effect must declare its extraordinary physical modification, not substitute naming for capacity.
6. **Sacrifice**: cost provenance and supernatural spent-value must remain; physical healing cannot automatically replenish prior sacrifice.
7. **Runic**: preparation is project work; object condition and enchantment function are separate.
8. **Alchemy**: recipe ingredients, yields, waste, purity, safe process and doses are actual records.
9. **Necromancy**: corpse, animation, consciousness, identity, memory and soul require explicit separate state/causal relationships.

### Cross-paradigm interaction matrix

An enabled setting declares each direction of **detection, resistance, interruption, resource compatibility, effect stacking and dispelling** by effect channel and means. No universal arcane-divine-spirit interoperability is implied. If an interaction lacks a supported operating model, it remains unresolved; this does not disable unrelated effects.

## Part VI — Extraordinary technique and item record contracts

### Technique record

Retain FL-1.0 fields as separate dimensions: `ID | version | paradigm | discipline | technique access tier | magnitude | scope | range | duration | complexity | cost | execution | resistance type | effect | harmful threat | potency | protection channel | secondary conditions | detection | counterplay | recovery | legal status`. Extend where material with `target identity/selection | source lot | output owner | recurrence/rearm | ongoing upkeep | authority | stop/abort | accepted effect | observation/receipt time | provenance`. The underlying Core owners record the changes, not the library.

### Source illustrative technique — not automatically available

**Focused Thermal Bolt** (`FL-1.0 section 59`, retained scoped demonstration): unspecified paradigm; Magnitude 2, Scope 1, Range 2, Duration 0; Burn, Threat 2, Potency 2, Heat protection channel, Protection resistance, no secondary condition. These *numerical terms are only a worked-format example under its original Fantasy mechanics*; they do not themselves confer casting access, fuel, range in meters, or balance certification.

### Production and transformation

A charm, potion, enchanted blade, standing ward, portal, familiar bond or undead animation is a **configured variant of an existing asset/actor/service or an extraordinary operating method**, not a fresh generic resource pool. Required work is represented as Core projects with materials, time, competence, infrastructure, inspection and commissioned function. A ritual's successful execution modifies only the declared world state; Mixed/failure never creates unrelated side-effects by default.

## Part VII — New optional Fantasy specialization templates (v2.0 proposals)

The following are **new proposed genre content patterns**. They are *not present as individual adopted species or objects in FL-1.0* and cannot rewrite SCL families. They exist to prevent campaigns independently inventing the same fantasy-specific data structures. Each entry has a **qualitative effect only**; no artificial default numerical values, creature personalities, populations or availability are supplied.

| Fantasy ID | Template | Actual owner/type | Qualitative function | Activation prerequisites | Critical limit |
|---|---|---|---|---|---|
| `FAN-EXT-001` | Enchanted equipment facet | Object/configuration | A physically existing item with a persistent extraordinary function | Substrate, compatible inscription/binding, energy/source, crafting project, activation rule, maintenance and countermeasure | An item broken beyond function does not remain operational unless independent anchoring is specified |
| `FAN-EXT-002` | Bound focus or reservoir | Object/resource interface | A focus channels or stores a bounded supernatural resource | Resource species, initial charge lot/pool, capacity, allowed users, input/output, leakage/recharge model | Possessing focus does not give expertise; charging is not free |
| `FAN-EXT-003` | Potion or infused consumable | Stock item + effect method | A consumable delivers an effect upon qualified use | Formula, dosage, contents, potency model, ingestion/contact path, shelf life, side effects, effect channel | One consumed dose cannot also remain as inventory |
| `FAN-EXT-004` | Ward or boundary field | Installed service / environmental effect | A constrained area/object protection against named channels | Anchor/location, source/upkeep, protection target, coverage, limits, detection, bypass/maintenance | Protection applies once and is not universal invulnerability |
| `FAN-EXT-005` | Portal / teleportation link | Transport service | Actual identified actors/assets can move through an extraordinary link | Endpoint geometry, direction, payload/mass capacity, energy/time, authorization, transit state, abort/failure | Opening portal does not spawn arriving cargo or reset supplies |
| `FAN-EXT-006` | Summoned autonomous ally | Actor arrival / contract | An actually identified autonomous actor may be transported or instantiated by setting mechanism | Origin/identity, consent/control terms, arrival, duration, upkeep, return, communication | Summoning is not a free extra attack or automatic obedience |
| `FAN-EXT-007` | Conjured commodity | Stock output effect | An explicit supernatural transformation yields usable matter/food/water | Source/cost, product spec, quantity, acceptance, permanence and degradation | Forecast quantity and effect description are not actual new stock until successful creation |
| `FAN-CRT-001` | Dragonlike organism variant | Species with extraordinary abilities | A winged, massive or otherwise dragonlike organism with bespoke biological and supernatural capability | Actual anatomy, flight mass and environment, breath delivery, ecology, needs, intelligence and prey | No free flight, breath, immunity or boss actions from the name |
| `FAN-CRT-002` | Undead animated body | Corpse asset + optional actor | A corpse may move under setting-defined animation without reinstating its old person | Corpse provenance/location/condition, animation source, control, upkeep, sensory/motion means | Animation does not restore original soul, rights, memories or healing by default |
| `FAN-CRT-003` | Elemental / manifest spirit | Autonomous being or bounded manifestation | An explicitly enabled extraordinary entity interacting with material state | Substrate, identity, agency, location, duration, limits, environmental needs and harm channels | Elemental does not mean immunity to all mundane causes |
| `FAN-CRT-004` | Shapeshifter / cursed form | Actor condition + body configuration | An existing actor's actual body configuration can change within a bounded mechanism | Trigger, anatomy, mass, inventory interaction, cognition, duration, reversibility, injuries | No duplication of body/gear; existing injuries persist unless explicitly changed |
| `FAN-CRT-005` | Construct or golem | Component equipment + controller/actor | Manufactured frame with specified independent or delegated tasks | Power, sensors, autonomy, control authority, means, maintenance, damage map and shutdown | No universal mental immunity; cannot execute commands beyond capability |

**Combination examples:** A fire-breathing dragon instantiates a species from `BODY-003` or another suitable body plan with `NAT-009`, plus a **specific** generated-organ/exposure effect. A necromantic servant attaches `FAN-CRT-002` to an existing corpse and a control contract; it does not spawn duplicate physical bodies. A teleport circle composes `FAN-EXT-005` with an actual facility, labor and source stock. These are construction recipes, not enabled campaign facts.

## Part VIII — Fantasy campaign profile (`CPF-BASE`, retained scoped source)

This remains Fantasy-owned because its specialization concerns world premise, creature ecology and extraordinary prevalence. It references Core institutions, information, movement, survival, economy and persistence **without duplicating those systems**. Campaign creation must select a legal profile before any new world state is initialized.

### CPF-BASE — Source template, adapted for Core v3.2

Every new Fantasy campaign completes this profile before runtime.

---

#### 61. Identity

`Campaign ID:`  
`Title:`  
`Premise:`  
`Genre:`  
`Tone:`  
`Starting date:`  
`Calendar:`  
`Geography scope:`  
`Player premise:`  

---

#### 62. Authority and sources

`Primary campaign sources:`  
`Setting sources:`  
`Explicit overrides:`  
`Forbidden/retconned assumptions:`  
`Migration version:`  

---

#### 63. Resolution

`Default dice system:` selected compatible genre adapter / F-1.0 d100 when explicitly selected / override  
`Competence ladder:`  
`Technique-access rule:`  
`Difficulty modifiers:`  
`Special resolution overrides:`  

---

#### 64. Character model

`Attribute profile:`  
`Attribute range:`  
`Capacity derivations:`  
`Disciplines:`  
`Specializations:`  
`Background rules:`  
`Profession/class rules:`  
`Starting competence ceiling:`  
`Progression model:`  

---

#### 65. Ancestries/species

For each:

`ID | Physiology | Scale | Lifespan | Development | Senses | Movement | Needs | Carry profile | Fatigue profile | Recovery profile | Resistances | Vulnerabilities | Innate supernatural capability`

Culture remains separate.

---

#### 66. Equipment calibration

`Weapon library version:`  
`Allowed weapon entries:`  
`Armor library version:`  
`Allowed armor entries:`  
`Shield library:`  
`Material technology:`  
`Exceptional materials:`  
`Repair infrastructure:`  
`Craft capability:`  

---

#### 67. Movement and travel

`Tactical distance assumptions:`  
`Foot travel baseline:`  
`Mounted baseline:`  
`Water travel:`  
`Flight travel:`  
`Road network quality:`  
`Weather model:`  
`Travel supply detail:`  

---

#### 68. Health

`Injury model:`  
`Bleeding model:`  
`Shock model:`  
`Disease detail:`  
`Poison detail:`  
`Medical capability:`  
`Recovery calibration:`  
`Disability/lasting-injury assumptions:`  

---

#### 69. Survival

For each important need:

`Need | Supplied condition | Short trigger | Deprived trigger | Severe trigger | Critical trigger | Recovery`

Potential needs:

- water;
- food;
- sleep;
- warmth;
- breathable atmosphere;
- sunlight;
- supernatural sustenance.

---

#### 70. Economy

`Currency:`  
`Coin/denomination structure:`  
`Typical wages:`  
`Market scale:`  
`Availability assumptions:`  
`Taxation:`  
`Banking/credit:`  
`Trade routes:`  
`Property rules:`  
`Business rules:`  

Prices belong here rather than in Fantasy Core.

---

#### 71. Social institutions

Define relevant:

- household;
- guild;
- nobility;
- temple;
- university;
- army;
- mercenary organization;
- town/city authority.

For each:

`Authority | Membership | Resources | Procedures | Offices | Obligations | Internal factions`

---

#### 72. Creature ecology

`Common mundane animals:`  
`Common extraordinary creatures:`  
`Predators:`  
`Domestic species:`  
`Intelligent nonhumans:`  
`Monsters:`  
`Creature-harvesting economy:`  
`Ecological supernatural effects:`  

---

#### 73. Supernatural paradigms

For each active paradigm:

`Paradigm ID | Local name | Source | Access | Capacity | Cost | Recovery | Institutions | Detection | Counterplay | Legal status`

---

#### 74. Supernatural prevalence matrix

Rate each independently.

| Capability | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Combat magic |  |  |  |  |  |  |
| Healing |  |  |  |  |  |  |
| Divination |  |  |  |  |  |  |
| Enchantment |  |  |  |  |  |  |
| Communication |  |  |  |  |  |  |
| Teleportation |  |  |  |  |  |  |
| Conjuration |  |  |  |  |  |  |
| Summoning |  |  |  |  |  |  |
| Resurrection |  |  |  |  |  |  |

Where:

**0 nonexistent**  
**1 legendary**  
**2 rare**  
**3 specialist**  
**4 common institutional**  
**5 ubiquitous**

Do not replace this with one “low/high magic” slider.

---

# 75. Supernatural world-consequence review

For every capability rated **4 or 5**, document consequences for at least:

`Economy | Warfare | Medicine | Law | Infrastructure | Daily life`

Where a capability rated as common has no visible societal consequences, the setting requires an explanation.

---

#### 76. Death model

Select:

`Permanent | Generational | Setting Resurrection | Reincarnation | Explicit Loop | Nonlethal`

Then define exact procedure.

---

#### 77. Military profile

`Organization:`  
`Recruitment:`  
`Equipment establishment:`  
`Training:`  
`Command:`  
`Supply:`  
`Fortification:`  
`Siege doctrine:`  
`Magical assets:`  
`Communication:`  
`Medical evacuation:`  

Do not assume modern ranks or organization.

---

#### 78. Settlement profile

Track as needed:

`Population | Food | Water | Shelter | Sanitation | Medicine | Security | Industry | Wealth | Transport | Communications | Specialists | Magical capability`

Define update interval.

---

#### 79. Information profile

`Ordinary communication speed:`  
`Literacy:`  
`Courier systems:`  
`Magical communication:`  
`Divination:`  
`Records:`  
`Rumor transmission:`  
`Map quality:`  

---

#### 80. Persistence profile

`Character ledger:`  
`Inventory ledger:`  
`Property ledger:`  
`Faction ledger:`  
`World ledger:`  
`Event queue:`  
`Hidden-state support:`  
`Checkpoint method:`  

---

**Required additions for v2.0:** `Core revision: IRGS-CORE-3.2 | SCL release: IRGS-SCL-1.0 | exact SCL references and selectors | Fantasy parent rule revision/compatibility mapping | source-backed hold permissions | enabled extraordinary archetypes | declared effect/health model per cause | activation certificates for critical systems | numerical model validity | acceptance evidence | decision authority | migration effective time`. A prevalence rating describes **world distribution**, not a probability of success, training/access, guaranteed item or automatic availability.

**Start order:** premise/boundaries → authority and inherited rules → mundane technology/economy → ancestry/body/ordinary ecology → permitted supernatural paradigms → prevalence for each *capability* → world consequences → institutions/markets/logistics → calibrated equipment, transport and protection → campaign-specific actual assets, inhabitants, knowledge and history. Stable ordinary life is a valid long-term outcome.

## Part IX — Variant construction, continuity and compatibility

### SCL-backed item variant

Resolve an actual `SCL:<family>@0.2` and selector; inspect source status and applicable Fantasy performance adapter; determine supported changes to geometry/handling/material/quality/attack mode; preserve unchanged values explicitly; require actual craftsmanship, inputs, time, location and ownership for a new in-world item. `FL-1.0:WPN-M-006A` can inform the `modes.cut` profile of a setting variant; local prestige alone cannot increase Threat. An attachment or enhancement does not multiply the source item, and removal of an enchantment does not restore destroyed steel.

### Protective variant

Compose *construction* (`ARM-*`) + actual *coverage* (`COV-*`) + compatible `MAT-*` + quality/fit/condition, plus optional explicitly bound `XMAT-*` effect. Do not independently add the complete rating for every layer. Record breach and repair at the affected component, location and channel. Extraordinary protection needs power, scope and resistance model; otherwise it grants no global immunity.

### Creature or ancestry variant

Start with actual biology/soul/construct operating model, not an opponent difficulty target. Distinguish ancestry physiology from cultural training, natural armor from worn armor, and actual innate capabilities from access to an external paradigm. A named monster does not receive extra actions, food, tactical knowledge or unique resistances without causal sources.

### Genre-engine binding

Core v3.2 is the shared runtime. `F-1.0`/`FL-1.0` profiles supply a **source-preserved genre numerical system** only when a particular campaign or adopted Fantasy foundation selects it, with explicit compatibility reconciliation against Core v3.2. A 'native adapter' is not permission to run two clocks, two injury ledgers, two economies or two project systems. Refer to genre owners instead of reproducing their generic mechanics in the content library.

### Migration

No active campaign is automatically rebound. Retain old item IDs, finite quantities, source references, actor conditions, material damage, history, hidden knowledge, active projects, obligations and pending events. New variants must be activated prospectively under a declared effective scope; source aliases must remain resolvable. Incompatible combat/injury figures require conversion and validation rather than silent numerical substitutions. Deletion/replacement of the original Fantasy library is not authorized by this proposal.

## Part X — Acceptance and calibration

The accompanying `Fantasy_Acceptance_Cases_v2_0.csv` specifies **40 reproducible behavior requirements**, including original source stress tests and new Core/SCL interface regressions. Their status is **specified, not live tested**. The package checker only verifies references, source coverage, data extraction and schema consistency; it does not simulate a campaign.

### Priority scripted fixtures

**P1: sword/armor.** Resolve `WPN-M-006A` and `WPN-M-006B` from one actual sword; apply the original Fantasy parent chain to an armor-covered target with compatible selected profiles. Neither a high roll nor an alias may grant impossible penetration or a second attack.

**P2: magical food logistics.** A spell with declared input/cost creates 3 units of accepted food only if its explicit profile says so; it must be credited once to the same stock ledger, transferred only when physically available, and spoil at the selected process rate. The value 3 here is a synthetic test input, **not** a universal spell yield.

**P3: sacrifice/healing.** Pay a defined sacrificial metaphysical cost from one owner; healing a tissue injury may modify the physical body without refunding that earlier extraordinary payment.

**P4: summoning/deity.** A summoned spirit or petitioned god decides according to actual relation, knowledge and autonomy; no compulsory obedience, additional voluntary PC action or unpriced NPC action is supplied by the content label.

**P5: scale shift/portal.** A party departs through a portal mid-supply interval; actor and cargo location change once, supply quantities remain, ongoing recovery/production continues with the same processed interval, and older received messages remain as-of their receipt times.

**P6: anatomy/exposure.** A winged animal suffers injury and venom exposure via separate channels. Targeted wing impairment changes supported flight while systemic toxin effect follows its explicit onset; an earlier wing hit does not automatically disable other anatomy.

### Calibration register

| Category | Required inputs before dependent numerical use | Current status |
|---|---|---|
| Weapon and protection | Material/edge configuration, relevant mode, penetration/impact and resistance chain, units, local geometry | Original F-1.0/FL-1.0 defaults retained; extension values provisional |
| Carry and movement | Species/strength, load distribution, terrain, gait, weather, timed distances | Campaign/genre calibration |
| Body-plan hits | Species anatomy, exposed region, attack line, nonhuman table fit | Provisional; do not impose universally |
| Venom, disease, magical exposure | Channel, dose, onset, effect duration, treatment and recovery | Profile-specific; no invented biological constants |
| Spell costs and recovery | Source/stock ownership, resource units, upkeep, reset interval, upper/lower bounds | Paradigm/setting-specific |
| Material/magic | Mass behavior, physical quality, effective protection, workability, repair and resource provenance | XMAT figures illustrative/proposed |
| Economy/prevalence | Availability, prices, institutions, user distribution, transport throughput | Setting/campaign-owned |
| Cross-adapter mechanics | Conversion map for native F-1.0 versus any replacement Fantasy engine; overlap/double count checks | Unresolved until compatible genre engine selected |

### Release acceptance conditions

1. Resolve all 111 original FL source entries to **95 exact shared bindings and 16 retained scoped extensions**; no dropped entry.
2. Preserve all 61 source-native numerical adapter references, selectors, payload checksums and source scope.
3. Keep the Shared Content Library and Core v3.2 normative records unchanged; no new generic Core authority claimed.
4. No ability or source entry can create an actual item/creature, spend resources or override agency merely through lookup.
5. Require complete selected numerical model before resolving consequential quantitative effects; missing numerical data blocks only dependent work.
6. New fantasy archetypes remain proposed and opt-in; no invented setting facts or automatic creature abilities.
7. Cross-engine runtime, calibration and live playtest status remain explicitly separate from passing structural tests.

**Open design questions:** Which future Fantasy Foundation revision is adopted against Core v3.2? Are F-1.0 values to remain a long-term optional native model or be superseded with explicit conversions? Which paradigms and species merit quantitatively calibrated reference profiles? Which of the proposed `FAN-EXT`/`FAN-CRT` archetypes should be promoted to accepted Fantasy content after tests? No answers are silently assumed.

## Part XI — Version history and source reconciliation

| Source | Authority and disposition |
|---|---|
| `IRGS — Fantasy Content Libraries v1.0.md` | Full original archived for exact native traits, mechanical numbers, supernatural/source text, campaign profile and worked scenarios; all 93 numbered sections accounted in matrix |
| `IRGS — Core Fantasy World Engine v1.0.md` | Native F-1.0 mechanical dependency preserved as historical genre source; not automatically a Core v3.2 substitute |
| `IRGS-CORE-3.2` | Current general simulation, owner and content-interface contract inherited |
| `IRGS-SCL-1.0` | Normative family identities, original bindings, 61 Fantasy adapters and shared content definitions; immutable revision/selector map |
| R1/R2 maturation work | Qualification dossiers and held/readiness distinction acknowledged; none automatically promoted |
| This Fantasy v2.0 | New proposed genre-specific rebuild, compatibility/crosswalk and optional extraordinary archetypes |

**CMRR decisions:** generic objects/materials/biology are *relocated* to SCL; numerical Fantasy presentation *split* from generic definitions and source-preserved; the nine paradigms, five extraordinary-material archetypes and campaign profile *retained in Fantasy*; construction procedures *revised* to SCL composition; acceptance/calibration requirements *retained and expanded*. No legacy source deletion is authorized. See `Fantasy_CMRR_93_Sections.csv` for all 93 original sections.

**Migration impact:** this library has no automatic effect on campaigns or the Core release. Replace the *active Fantasy content library dependency* only after genre/profile review and adoption. Retain older `FL-1.0` native data and original file until all held source replacements and numerical adapter qualifications are demonstrably complete.

