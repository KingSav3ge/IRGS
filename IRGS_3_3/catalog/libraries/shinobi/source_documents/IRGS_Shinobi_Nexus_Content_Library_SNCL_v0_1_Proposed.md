# IRGS — Shinobi Nexus Content Library
## SNCL v0.1 · Complete Proposed Content Release · Core v3.2 / SNWE R0.3 / SCL v1.0

**Document ID:** `IRGS-SNCL-0.1`  
**Edition:** 0.1 — 14 October 2026  
**Status:** PROPOSED library; not adopted, not a new engine, not campaign state, not playtested or calibrated  
**Parent:** `IRGS-CORE-3.2 → IRGS-SNWE-0.3 → this SNCL content catalogue`  
**Shared catalogue:** `IRGS-SCL-1.0` (preserves `SCL:PBC-…@0.2` canonical definitions and per-family activation/readiness)  
**Authority:** Explicit current user instruction → established campaign override → selected SNWE engine and setting → Core; this catalogue adds content only when selected by the campaign  
**Primary source:** SNWE R0.3 §6.4, §§2.4, 7, 9, 12, and Parts III–IV. This library does **not** claim restoration of unseen original SSN Jutsu Compendium, Bloodline Legacies, Canon-Zero or other legacy source files.

## 1. Purpose, scope and status
Use a reusable, auditable catalogue of **technique definitions, field equipment, unit blocks, missions, organizations, services, and unconverted capability candidates**. It is a content/reference layer rather than a competing Core or SNWE procedure. A definition does not instantiate an item, actor, population, location, physical effect or legal authority.
The catalogue intentionally separates **faithfully source-carried operating entries**, **new candidate operational entries**, **conditional organizational/mission templates**, and **held unfinished entries**. The content ledger/registry is the single source of truth for the library; rendered text is a view. Game state remains owned by Core.

### 1.1 Inventory
| Kind | Native/derived | Proposed opt-in | Proposed template | Held incomplete | Total |
|---|---:|---:|---:|---:|---:|
| Technique | 18 | 31 | 0 | 0 | 49 |
| Equipment | 10 | 4 | 0 | 4 | 18 |
| Unit Profile | 4 | 0 | 0 | 0 | 4 |
| Mission Template | 0 | 0 | 11 | 0 | 11 |
| Institution Template | 0 | 0 | 12 | 0 | 12 |
| Service Profile | 7 | 0 | 5 | 0 | 12 |
| Held Candidate | 0 | 0 | 0 | 16 | 16 |
| **Total** | **39** | **35** | **28** | **20** | **122** |

### 1.2 Status and readiness gates
- **`native_source`:** faithful selected R0.3 profile, source R0.1 remains proposed.
- **`native_derived`:** an operating reference view derived from R0.3; no new owner.
- **`proposed_complete_opt_in`:** new playable-scale proposal only on explicit profile activation; uncalibrated.
- **`proposed_template`:** scenario/organization/service template requiring concrete campaign data.
- **`held_incomplete`:** cannot activate as full mechanic without enumerated missing fields.
**Source status warning:** `native_source` means mechanically carried from the *proposed* R0.3/R0.1 selected implementation. It does **not** elevate that implementation to adopted canon. `proposed_complete_opt_in` means sufficiently specified for a bounded scene after explicit campaign activation, but **not** numerically calibrated or unconditionally approved. `held_incomplete` cannot resolve its advertised extraordinary effect.

### 1.3 IDs and reference contract
Stable namespaced catalogue IDs use `SNCL-<domain>-<status>-NNN` internally and resolve as `SNCL:<ID>@0.1`. The public machine registry uses the literal `id` field; changing displayed labels cannot create duplicate identities. No SNCL ID claims to be a canonical `SCL:PBC-…@0.2` entry or a Shared Core system function.
A content selection binds `(library version, ID, mode/variant, status, source/rule edition, prerequisites, target method, permitted campaign scope)`. Later campaign instances get separate stable K-ACTOR/K-ASSET/K-STOCK/K-ORG IDs. One technique entry may have several declared elemental/handling modes without generating separate powers, actions or items.

## 2. Shared rule dependencies and entry usage
SNWE R0.3 **Chapter 6** controls: legal access → committed chakra/stamina once → Mold 2d6 → Precision d20 release when required → effect/mitigation → output/Trauma → duration/termination. No additional Core d100 test. Same-rank escalation is paid even when Mold fails. S-rank carries its additional Trauma. Elemental clash bonuses apply only in direct opposed clashes.
Chapter 4 owns **CU pools, escalation, overclock and recovery**; Chapter 5 owns physical attacks/defense; Chapter 7 owns Trauma/Injury/treatment; Chapter 9 owns abstract Supply and research; Chapter 12 owns unit ratings, Strength and Resource Points. Core owns each actual actor, asset, stock, project, event, message, institution, household and transfer. No Fantasy/Historical attack or armor adapter may be stacked on top.
**Affinities:** Fire, Wind, Lightning, Earth, Water; source clash cycle Fire → Wind → Lightning → Earth → Water → Fire. Nature access grants eligibility rather than an accuracy bonus. Neutral techniques require the discipline/technique; fused techniques require an exact contract and Synthesis. **Ranges** inherit SNWE zone and source targeting vocabulary, not unmeasured global kilometers.
**Task flags:** A printed fixed DC overrides the generic one for that particular technique. Genjutsu uses target Resolve; physical precision uses native d20; Fūinjutsu uses the specified DC or Fortitude. No secondary die test may be created merely because an entry has several descriptive tags.

### 2.1 Standard chakra cost lookup (source, not a discount table)
| Rank | Base CU | Extra CU per earlier paid cast of same rank this scene | Raw damage if damaging jutsu |
|---|---:|---:|---|
| E | 1 | 0 | 1d4 |
| D | 3 | 0 | 1d6 |
| C | 5 | 1 | 2d6 |
| B | 8 | 2 | 3d6 |
| A | 12 | 3 | 4d6 |
| S | 18 | 4 | 5d6 |
Calculate paid cost = base + (earlier paid casts of this rank in current scene × rank tax), plus any separately written nonstacking effect. The same expenditure is counted once for CU stock and once as reference input to output-burden calculation, not deducted twice. Control, nonlethal restraint, healing, intelligence and shields do **not** inherit damage dice.

### 2.2 Persistent-world compatibility
An abstract restock token cannot create physical stock if no valid stock/backing allocation exists under the adopted persistent-world bridge. No ryō exchange rate, liters of produced water, long-distance chakra transport rate, hospital patients/hour, village sensor range, or guaranteed crop yield is defined by this library. A specific technique or selected campaign profile must state those values before they are consequential.

## 3. Source-backed starter techniques · 18 entries
The following **Operating effect** fields are transcribed from SNWE R0.3 §6.4. `Spark / Pebble / Droplet` is **one parameterized family record**, not three free techniques or separate inventory objects.
### SNCL-J-N001 — Transformation
**Rank/discipline:** E / Ninjutsu · **Action/range:** Standard / self · **Status:** `native_source`
**Operating effect (native):** Mold DC 7. Change visual appearance for a scene; inspection is Perception against activation total. No physical capabilities copied.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N002 — Illusory Clone
**Rank/discipline:** E / Genjutsu · **Action/range:** Standard / near · **Status:** `native_source`
**Operating effect (native):** Resolve test against one observer. On success impose −1 on its next attack before your next turn. No independent actions or damage.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N003 — Chakra Adhesion
**Rank/discipline:** E / Ninjutsu · **Action/range:** Standard / self · **Status:** `native_source`
**Operating effect (native):** Mold DC 7. Cling to a surface for a scene; still pay normal movement. Carry no more than normal load.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N004 — Spark / Pebble / Droplet
**Rank/discipline:** E / Ninjutsu · **Action/range:** Standard / short · **Status:** `native_source`
**Operating effect (native):** Precision; 1d4 elemental damage. Choose known affinity when learned.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N005 — Substitution
**Rank/discipline:** D / Ninjutsu · **Action/range:** Reaction / self · **Status:** `native_source`
**Operating effect (native):** Declare before hit roll; Mold DC 7 and pay 1 Stamina. Gain +2 Defense against that attack, then move within your zone to available cover. No automatic escape from a pin.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N006 — Body Flicker
**Rank/discipline:** D / Ninjutsu · **Action/range:** Standard / self · **Status:** `native_source`
**Operating effect (native):** Mold DC 7; move two traversable zones. Does not pass through walls or release a grapple.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N007 — Field Mending
**Rank/discipline:** D / Ninjutsu · **Action/range:** Standard / touch · **Status:** `native_source`
**Operating effect (native):** Intelligence + Medicine DC 9; restore 1d6 Health. One successful application per target per scene. Does not cure Injury.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N008 — Chakra Bolt
**Rank/discipline:** D / Ninjutsu · **Action/range:** Standard / short · **Status:** `native_source`
**Operating effect (native):** Precision; 1d6 elemental damage.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N009 — Binding Slip
**Rank/discipline:** D / Fūinjutsu · **Action/range:** Standard / touch · **Status:** `native_source`
**Operating effect (native):** Against Fortitude. On success target is Grappled for one round by the seal, with escape against activation total.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N010 — Elemental Projectile
**Rank/discipline:** C / Ninjutsu · **Action/range:** Standard / short · **Status:** `native_source`
**Operating effect (native):** Precision; 2d6 elemental damage to one target.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N011 — Elemental Wave
**Rank/discipline:** C / Ninjutsu · **Action/range:** Standard / near/short · **Status:** `native_source`
**Operating effect (native):** Force; at most two adjacent targets in one zone, 2d6 elemental damage each. Roll Mold once; compare against each Band DC.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N012 — Smoke Veil
**Rank/discipline:** C / Ninjutsu · **Action/range:** Standard / near · **Status:** `native_source`
**Operating effect (native):** Force; fill one zone with concealment for two rounds. Ranged attacks through it take −2; it provides no armor.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N013 — False Opening
**Rank/discipline:** C / Genjutsu · **Action/range:** Standard / short · **Status:** `native_source`
**Operating effect (native):** Resolve test; target is Distracted (−1 to rolls) for two rounds, with normal break action. No direct damage.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N014 — Restraining Seal
**Rank/discipline:** C / Fūinjutsu · **Action/range:** Standard / touch · **Status:** `native_source`
**Operating effect (native):** Against Fortitude; Restrained for two rounds. Escape Standard Action against original activation total.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N015 — Earthen Screen
**Rank/discipline:** C / Ninjutsu · **Action/range:** Standard / near · **Status:** `native_source`
**Operating effect (native):** Mold DC 9; create cover +2 for two rounds, enough for two allies. Screen has 12 Health, no resistance or armor.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N016 — Piercing Lance
**Rank/discipline:** B / Ninjutsu · **Action/range:** Standard / short · **Status:** `native_source`
**Operating effect (native):** Precision; 3d6 elemental damage. “Piercing” is the fiction, not extra armor bypass.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N017 — Broad Barrier
**Rank/discipline:** B / Ninjutsu · **Action/range:** Standard / near · **Status:** `native_source`
**Operating effect (native):** Mold DC 11; barrier has 20 Health, lasts three rounds and blocks a doorway or route. Attacks may target barrier; it has no mitigation.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

### SNCL-J-N018 — Great Elemental Release
**Rank/discipline:** A / Ninjutsu · **Action/range:** Standard / long · **Status:** `native_source`
**Operating effect (native):** Force; two targets in one zone, 4d6 elemental damage each. May ignite, soak or disrupt terrain only as a recorded non-damaging scene tag.
**Inherited costs/activation:** SNWE rank base cost + same-rank scene escalation (no extra printed free effect) — SNWE R0.3 §6.1–6.3; preserve printed technique-specific exceptions. **Counterplay:** Native target defenses, interruption, terrain and printed removal conditions. 
**Source:** SNWE R0.3 §6.4 (retained R0.1 operating source). **Boundary:** Do not infer durable material, new persons or stock from an abstract/combat effect

## 4. New complete scene-scale technique candidates · 31 proposals
**All entries in this section are new proposals, not legacy SSN powers or Naruto canon.** Activation is opt-in at the campaign profile level. Values are provisional and need numerical and narrative playtesting. Effects do not upgrade themselves into persistent logistics, industry, permanent infrastructure or unrestricted magical creation.
### SNCL-J-P001 — Chakra Signal
**Rank/discipline/affinity:** E / Ninjutsu / neutral · **Action:** Standard · **Range:** near · **Target:** one willing observer with sight
**Activation:** Sensitivity + Ninjutsu; Mold DC 7. **Cost:** SNWE E CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** instant; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Create a visible, non-damaging flare recognizable to any observer with line of sight. It carries no secret text or automatic notice to absent observers.
**Counterplay:** Obstructions, blindness or lack of observation block receipt.  
**Risk/physical boundary:** Ordinary activation/overclock. Light only while activated; not a persistent beacon.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P002 — Marking Touch
**Rank/discipline/affinity:** E / Ninjutsu / neutral · **Action:** Standard · **Range:** touch · **Target:** one accessible mundane object
**Activation:** Sensitivity + Ninjutsu; Mold DC 7. **Cost:** SNWE E CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one scene; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Leave a small visible chakra-glow mark at the touched location; it gives no remote sensing, tracking or ownership rights.
**Counterplay:** Mark can be obscured, erased by ending the effect, or overlooked.  
**Risk/physical boundary:** Ordinary activation/overclock. No material transfer or permanent inscription.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P003 — Quiet Footfall
**Rank/discipline/affinity:** E / Ninjutsu / neutral · **Action:** Standard · **Range:** self · **Target:** caster
**Activation:** Sensitivity + Ninjutsu; Mold DC 7. **Cost:** SNWE E CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** until end of next turn; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Reduce ordinary footstep sound for one traversable-zone movement. Gain +1 situational on a Stealth check relying principally on footstep noise; does not erase sight, scent or existing tracks.
**Counterplay:** Other detection channels remain; suitable sensitive hearing or noise may affect Stealth.  
**Risk/physical boundary:** Ordinary activation/overclock. No teleportation or intangible travel.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P004 — Surface Test
**Rank/discipline/affinity:** E / Ninjutsu / Earth · **Action:** Standard · **Range:** touch · **Target:** one visible hand-sized patch
**Activation:** Sensitivity + Ninjutsu; Mold DC 7. **Cost:** SNWE E CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** instant; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Dislodge loose dust or particles from the patch, revealing otherwise physically present surface markings exposed by the movement; no hidden-information sensor.
**Counterplay:** Solid coverings, bonded paint, enclosed voids unaffected.  
**Risk/physical boundary:** Ordinary activation/overclock. Moves existing loose particles only; creates no stock.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P005 — Breath Steady
**Rank/discipline/affinity:** E / Ninjutsu / neutral · **Action:** Standard · **Range:** self · **Target:** caster
**Activation:** Wisdom + Ninjutsu; Mold DC 7. **Cost:** SNWE E CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one minute; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Assist controlled breathing; +1 situational to one feasible concentration task completed during the minute. Does not remove actual poison, oxygen deficit, Stress or Trauma.
**Counterplay:** Active injury/deprivation can still make task impossible.  
**Risk/physical boundary:** Ordinary activation/overclock. No healing or physiological replenishment.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P006 — Handhold Line
**Rank/discipline/affinity:** D / Ninjutsu / Earth · **Action:** Standard · **Range:** short · **Target:** one existing traversable surface or handhold
**Activation:** Sensitivity + Ninjutsu; Mold DC 7. **Cost:** SNWE D CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Stabilize loose surface footing for one crossing actor per round over one adjacent route segment; ignore at most one -1 footing situational penalty, not a prohibitive gap.
**Counterplay:** Undermining, destruction, prohibited load or loss of line invalidates use.  
**Risk/physical boundary:** Ordinary activation/overclock. No new bridge structure; requires existing route.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P007 — Signal Burst
**Rank/discipline/affinity:** D / Ninjutsu / Fire · **Action:** Standard · **Range:** short · **Target:** visible actors in one zone
**Activation:** Sensitivity + Ninjutsu; Mold DC 7. **Cost:** SNWE D CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** instant; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Bright light reveals illuminated exposed surfaces within one zone until end of this turn. No direct damage or automatic blindness.
**Counterplay:** Occlusion, counter-light, hidden surfaces remain hidden.  
**Risk/physical boundary:** Ordinary activation/overclock. Momentary light, not fire production.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P008 — Static Grip
**Rank/discipline/affinity:** D / Ninjutsu / Lightning · **Action:** Standard · **Range:** touch · **Target:** one nonliving unsecured palm-sized object
**Activation:** Sensitivity + Ninjutsu; Mold DC 7. **Cost:** SNWE D CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one round; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Temporarily adhere object to caster’s usable hand; release freely. Does not bypass a locked mechanism, contest another actor’s grip, or increase lifting capacity.
**Counterplay:** Opposed custody/grip, excessive weight, severed line of contact defeats it.  
**Risk/physical boundary:** Ordinary activation/overclock. No item copy; original object remains same K-ASSET.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P009 — Current Read
**Rank/discipline/affinity:** D / Ninjutsu / Water · **Action:** Standard · **Range:** near · **Target:** one visible flowing-water section
**Activation:** Wisdom + Ninjutsu; Mold DC 7. **Cost:** SNWE D CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** instant; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Reveal visible swirl/flow direction and obvious eddies useful to ordinary navigation; +1 situational to one water-route assessment during the current scene if already feasible.
**Counterplay:** Cannot find unseen water, hidden contaminants or forecast depth/flow without data.  
**Risk/physical boundary:** Ordinary activation/overclock. No water creation or purification.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P010 — Air Pocket
**Rank/discipline/affinity:** D / Ninjutsu / Wind · **Action:** Standard · **Range:** self · **Target:** caster breathing surrounding air
**Activation:** Sensitivity + Ninjutsu; Mold DC 7. **Cost:** SNWE D CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one round; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Deflect loose airborne dust/smoke at immediate face where unconfined air exists, enabling sight for a single short observation; no oxygen creation, toxic-gas filtration or fire suppression.
**Counterplay:** Enclosure, severe toxic atmosphere or lack of oxygen remain.  
**Risk/physical boundary:** Ordinary activation/overclock. No sustained air supply or contaminant removal.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P011 — Cord Release
**Rank/discipline/affinity:** D / Fūinjutsu / neutral · **Action:** Standard · **Range:** touch · **Target:** one already-threaded mundane rope or accessible knot
**Activation:** Intelligence + Fūinjutsu vs DC 9. **Cost:** SNWE D CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** instant; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Loosen a physically accessible simple knot or binding the caster could otherwise untie with tools and time. Does not break sealed locks or restrain an unwilling opponent by automatic declaration.
**Counterplay:** Inaccessible binding, reinforced seal, opposed owner access.  
**Risk/physical boundary:** Ordinary activation/overclock. Changes existing knot arrangement only; does not destroy rope.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P012 — Beacon Imprint
**Rank/discipline/affinity:** D / Fūinjutsu / neutral · **Action:** Standard · **Range:** touch · **Target:** one accessible tag supplied before casting
**Activation:** Intelligence + Fūinjutsu vs DC 9. **Cost:** SNWE D CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one day or until tag destroyed; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Inscribes a visible simple warning symbol chosen at casting; reads by sight. Tag has no tracking, alarm network, or physical defense.
**Counterplay:** Remove or destroy actual tag; visibility and literacy apply.  
**Risk/physical boundary:** Ordinary activation/overclock. Physical tag inventory consumed? No: existing tag is altered, not copied.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P013 — Misleading Sound
**Rank/discipline/affinity:** D / Genjutsu / neutral · **Action:** Standard · **Range:** short · **Target:** one observer with relevant senses
**Activation:** Wisdom + Genjutsu vs target Resolve. **Cost:** SNWE D CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one round; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Observer perceives a brief false footstep originating within the same visible zone, and is Distracted (-1 rolls) until end of its next turn; normal break action. No invented actual person.
**Counterplay:** Genjutsu break; non-affected witnesses can contradict perception.  
**Risk/physical boundary:** Upkeep none for bounded single-round effect. Perception only; no actual sound source/object.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P014 — False Trail
**Rank/discipline/affinity:** C / Genjutsu / neutral · **Action:** Standard · **Range:** short · **Target:** one observer who can perceive path
**Activation:** Wisdom + Genjutsu vs target Resolve. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Observer sees a plausible false trail along one genuinely traversable visible route; Distracted -1 for related navigation/observation checks until effect ends; normal break action.
**Counterplay:** Other investigators, tactile inspection, Genjutsu break.  
**Risk/physical boundary:** Sustained upkeep 1 CU per turn after first, if maintained. No physical footprints or location transfer.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P015 — Earth Lock
**Rank/discipline/affinity:** C / Ninjutsu / Earth · **Action:** Standard · **Range:** near · **Target:** one accessible existing gate hinged in frame
**Activation:** Sensitivity + Ninjutsu; Mold DC 9. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Earth pressure braces a gate closed within its existing frame; attackers must defeat the gate’s existing structure/lock or an actual bypass. No bonus Health created.
**Counterplay:** Remove supporting soil/brace, destroy gate or open alternate path.  
**Risk/physical boundary:** Ordinary activation/overclock. Temporary force on existing gate, no new durable wall.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P016 — Water Slick
**Rank/discipline/affinity:** C / Ninjutsu / Water · **Action:** Standard · **Range:** near · **Target:** one visible bounded dry passage portion, only if actual water available
**Activation:** Sensitivity + Ninjutsu; Mold DC 9. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Redistribute up to one carried/nearby available flask of water onto a small handspan-to-stride-sized area; crossing actors face a -1 situational footing penalty when applicable; no additional water created.
**Counterplay:** Dry/mop or avoid area; feasible non-slip travel.  
**Risk/physical boundary:** Requires actual water and accessible discharge; cost rank C. Deduct physically transferred water once; do not infer unlimited volume.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P017 — Wind Relay
**Rank/discipline/affinity:** C / Ninjutsu / Wind · **Action:** Standard · **Range:** short · **Target:** one openly visible willing listener in adjacent zone
**Activation:** Sensitivity + Ninjutsu; Mold DC 9. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** instant; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Carries up to one ordinary shouted sentence intelligibly between two visible zones along open air; observers along route may also hear.
**Counterplay:** Intervening closed walls, competing noise and recipient comprehension.  
**Risk/physical boundary:** Ordinary activation/overclock. Information signal: occurrence ≠ receipt; no omniscient network.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P018 — Electrical Trip
**Rank/discipline/affinity:** C / Ninjutsu / Lightning · **Action:** Standard · **Range:** near · **Target:** one living target in same visible zone
**Activation:** Sensitivity + Ninjutsu; Force vs target Band DC. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one round; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** On effect impose Suppressed condition only (native -1 Defense, extra 1 Stamina to move/physical Standard); no damage or automatic paralysis.
**Counterplay:** Cover blocking delivery; remove effect at end of next turn.  
**Risk/physical boundary:** Ordinary activation/overclock. Electrical exposure does not independently apply other injuries.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P019 — Fire Line
**Rank/discipline/affinity:** C / Ninjutsu / Fire · **Action:** Standard · **Range:** near · **Target:** one visible unoccupied traversable edge within zone
**Activation:** Sensitivity + Ninjutsu; Mold DC 9. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Creates a visible narrow heat line deterring ordinary crossing: an actor may still cross but needs an explicit heat-exposure assessment before doing so. No direct automatic damage.
**Counterplay:** Water, cover, alternate route, appropriate protection.  
**Risk/physical boundary:** Physical heat exposure model needed to calculate injury; not provided by this entry. Temporary heat only, not a permanent fuel source.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P020 — Stabilizing Earth
**Rank/discipline/affinity:** C / Ninjutsu / Earth · **Action:** Standard · **Range:** near · **Target:** one person-sized patch of existing loose earth
**Activation:** Sensitivity + Ninjutsu; Mold DC 9. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one scene; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Compact existing loose soil into a stable standing spot for one actor, subject to actual load and foundation; +1 situational to one footing-dependent task if feasible.
**Counterplay:** Failure of underlying ground, water, larger load, excavation.  
**Risk/physical boundary:** Ordinary activation/overclock. No large-scale construction or bulk earth production.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P021 — Seal of Warning
**Rank/discipline/affinity:** C / Fūinjutsu / neutral · **Action:** Standard · **Range:** touch · **Target:** one physical accessible paper tag with assigned guardian
**Activation:** Intelligence + Fūinjutsu vs DC 9. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one scene; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** If tag is physically touched, it emits a visible flash at the tag for one round. Does not transmit alert to absent owner. One activation then expires.
**Counterplay:** Avoid tag, shield flash, remove/destroy tag.  
**Risk/physical boundary:** No upkeep. Requires actual tag; no automatic trap damage. Alarm only where actually perceived.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P022 — Sensory Doubt
**Rank/discipline/affinity:** C / Genjutsu / neutral · **Action:** Standard · **Range:** short · **Target:** one perceiving observer
**Activation:** Sensitivity + Genjutsu vs Resolve. **Cost:** SNWE C CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Victim suffers Distracted -1 to Perception and Investigation-relevant rolls from false contradictory percepts; normal break action. No control of choices or compulsory movement.
**Counterplay:** Break Genjutsu, alternate independent witness, physical evidence.  
**Risk/physical boundary:** Upkeep 1 CU per turn after first. Apparent information, no real scene mutation.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P023 — Tether Seal
**Rank/discipline/affinity:** B / Fūinjutsu / neutral · **Action:** Standard · **Range:** touch · **Target:** one physically touched unwilling actor
**Activation:** Intelligence + Fūinjutsu vs Fortitude. **Cost:** SNWE B CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** three rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** On success impose Restrained using native condition and escape vs original activation total; requires accessible surface contact and valid seal application.
**Counterplay:** Target escape action, break/destruction of seal or removal of access.  
**Risk/physical boundary:** No free damaging effect; ordinary overclock. Existing target remains same actor; no custody consent.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P024 — Sheltering Canopy
**Rank/discipline/affinity:** B / Ninjutsu / Earth · **Action:** Standard · **Range:** near · **Target:** one doorway-like existing overhead support with at most two actors
**Activation:** Sensitivity + Ninjutsu; Mold DC 11. **Cost:** SNWE B CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** three rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Temporary overhead screen with 20 Health, no armor/resistance, blocks direct falling light debris and line of sight along its actual footprint. Heavy collapse needs separate structural assessment.
**Counterplay:** Destroy screen, bypass, wait until expiry.  
**Risk/physical boundary:** Ordinary overclock; no independent material stock. Transient force field not harvested building material.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P025 — Silencing Veil
**Rank/discipline/affinity:** B / Genjutsu / neutral · **Action:** Standard · **Range:** short · **Target:** one observer
**Activation:** Wisdom + Genjutsu vs Resolve. **Cost:** SNWE B CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** three rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Target fails to perceive sounds made by one explicitly named visible source; no actual silencing or private thoughts. May break as native Genjutsu.
**Counterplay:** Independent observers, smell/sight, chakra release.  
**Risk/physical boundary:** Upkeep 1 CU each turn after first. Reports can be mistaken, physical acoustics unchanged.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P026 — Barrier Redirect
**Rank/discipline/affinity:** B / Ninjutsu / Wind · **Action:** Standard · **Range:** near · **Target:** one ally already within same zone and clear air route
**Activation:** Sensitivity + Ninjutsu; Mold DC 11. **Cost:** SNWE B CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Provide +2 cover circumstance against up to one ranged attack aimed at the ally before expiry; does not stack with stronger identical cover cause.
**Counterplay:** Attacks circumventing screen, sufficiently strong angle or obstruction.  
**Risk/physical boundary:** Ordinary overclock. Temporary protection, no projectile teleportation or asset creation.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P027 — Chakra Anchorage
**Rank/discipline/affinity:** B / Fūinjutsu / neutral · **Action:** Standard · **Range:** touch · **Target:** one actual movable nonliving object small enough for one person to carry
**Activation:** Intelligence + Fūinjutsu vs DC 11. **Cost:** SNWE B CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one scene; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Temporarily inhibits ordinary accidental movement of the object while resting on existing solid ground; deliberate moving requires a feasible contested Strength/skill task; not immovable against any force.
**Counterplay:** Undermine ground, cut/remove seal, outmatch normal holding force with supported capability.  
**Risk/physical boundary:** Ordinary overclock; no additional item copy. Physical effect lacks fixed force magnitude; for consequential structural/transport use requires local load profile.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P028 — Rapid Encirclement
**Rank/discipline/affinity:** A / Genjutsu / neutral · **Action:** Standard · **Range:** long · **Target:** two perceiving observers in one visible zone
**Activation:** Wisdom + Genjutsu vs each Resolve using one activation total. **Cost:** SNWE A CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Each affected target is Distracted (-1 rolls) by apparent figures; no physical attackers or free attacks.
**Counterplay:** Normal Genjutsu break for each; unaffected witnesses, lack of visibility.  
**Risk/physical boundary:** Upkeep 1 CU per turn after first (one sustained technique). No physical manifestation.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P029 — Fortress Gate
**Rank/discipline/affinity:** A / Ninjutsu / Earth · **Action:** Standard · **Range:** long · **Target:** one pre-existing doorway or narrow route segment
**Activation:** Sensitivity + Ninjutsu; Mold DC 11. **Cost:** SNWE A CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** three rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Barrier has 20 Health, blocks one physically present doorway/route, no armor/mitigation and no independent agency. Greater area than doorway not authorized.
**Counterplay:** Break barrier, circumvent or expiry.  
**Risk/physical boundary:** Ordinary overclock; source A-cost and no damage dice. Barrier disappears without leaving construction stock.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P030 — Grand Smoke Screen
**Rank/discipline/affinity:** A / Ninjutsu / Wind · **Action:** Standard · **Range:** long · **Target:** two adjacent visible zones with accessible airflow
**Activation:** Sensitivity + Ninjutsu; Mold DC 11. **Cost:** SNWE A CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** two rounds; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Conceals sight through both named zones: ranged attacks crossing screen suffer -2; no armor and no harmful toxin invented.
**Counterplay:** Wind/rain/profile, alternate senses, move out of affected area.  
**Risk/physical boundary:** Ordinary overclock. No durable fog water or hidden actors created.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

### SNCL-J-P031 — Emergency Chakra Shelter
**Rank/discipline/affinity:** A / Ninjutsu / neutral · **Action:** Standard · **Range:** near · **Target:** two present willing people in same zone
**Activation:** Intelligence + Ninjutsu; Mold DC 11. **Cost:** SNWE A CU cost, cumulative same-rank escalation; commit and no refund; native overclock. **Duration:** one scene; upkeep: Genjutsu: 1 CU per subsequent turn only where sustained; otherwise none unless printed.
**Effect:** Establish a temporary protective screen over two stationary people, Health 20, no mitigation, blocks direct line-of-sight attacks from one designated direction; moving out loses cover.
**Counterplay:** Flank, destroy screen, expire, move around.  
**Risk/physical boundary:** Ordinary overclock; not medical treatment. Actual shelter footprint only.  
**Status:** `proposed_complete_opt_in` — not adopted or calibrated.

## 5. Field equipment, consumables and ninja tools · 18 references
Do not invent dimensions, mass, tool effect statistics, availability, fabrication capability, or cash prices merely because an item name appears. `Native Source` abstract costs may operate only in the selected native economy; persistent physical accounting needs real stock and provenance.
### SNCL-G-001 — Thrown weapon (ordinary)
**Status:** `native_source` · **Acquisition/availability:** 6 items per 1 personal Supply restock  
**Operating scope:** Ammunition count=6 per selected transaction; accuracy/damage require actual weapon attack-mode profile  
**Owner:** K-ASSET/K-STOCK · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-002 — Field medical kit
**Status:** `native_source` · **Acquisition/availability:** 3 medical uses per 1 personal Supply restock  
**Operating scope:** One use per qualifying Chapter 7 medical action; the physical kit persists until actually exhausted  
**Owner:** K-ASSET/K-STOCK/MED · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-003 — Field ration bundle
**Status:** `native_source` · **Acquisition/availability:** 3 ration-days per 1 personal Supply restock  
**Operating scope:** Supply token does not itself feed a person; bundle must be acquired, moved and consumed; actual specific nutritional profile still selected  
**Owner:** K-STOCK/K-ACTOR · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-004 — Normal melee weapon
**Status:** `native_source` · **Acquisition/availability:** 1 personal Supply when purchased in native abstract mode  
**Operating scope:** Actual weapon identity and mode depend on selected content instance; no universal attack damage from item title  
**Owner:** K-ASSET · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-005 — Light armor AR 1
**Status:** `native_source` · **Acquisition/availability:** 2 personal Supply in native abstract mode  
**Operating scope:** Native AR1: Defense +1, damage reduction 3; actual fit/condition/owner tracked  
**Owner:** K-ASSET · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-006 — Armor AR 2
**Status:** `native_source` · **Acquisition/availability:** 4 personal Supply in native abstract mode  
**Operating scope:** Native AR2: Defense +2, damage reduction 5; worn one item, exact construction requires selected content  
**Owner:** K-ASSET · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-007 — Armor AR 3
**Status:** `native_source` · **Acquisition/availability:** 7 personal Supply; trained armorer access required  
**Operating scope:** Native AR3: Defense +3, damage reduction 7; configuration/care tracked  
**Owner:** K-ASSET · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-008 — Rope
**Status:** `native_source` · **Acquisition/availability:** Starting kit provided  
**Operating scope:** Actual length, safe load, strength, wear, knots and route compatibility require object/scene profile  
**Owner:** K-ASSET · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-009 — Basic field tools
**Status:** `native_source` · **Acquisition/availability:** Starting kit provided  
**Operating scope:** Tool access allows only actually qualified tasks; no free access to special devices  
**Owner:** K-ASSET · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-010 — Repair/project materials allocation
**Status:** `native_source` · **Acquisition/availability:** 1 personal Supply per project action  
**Operating scope:** Native abstract reservation must map to actual parts/inputs before persistent material accounting  
**Owner:** K-STOCK/K-WORK · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-011 — Signal paper tags
**Status:** `proposed_complete_opt_in` · **Acquisition/availability:** Quantity and price selected in campaign  
**Operating scope:** Physical, destructible writing substrate; no automatic remote network; requires technique for an extraordinary effect  
**Owner:** K-ASSET/K-STOCK · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-012 — Document roll and seal case
**Status:** `proposed_complete_opt_in` · **Acquisition/availability:** Quantity and price selected in campaign  
**Operating scope:** Secure portable paper holder, with ordinary physical access and custody; cannot grant legal authority by item name  
**Owner:** K-ASSET · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-013 — Medical dressing stock
**Status:** `proposed_complete_opt_in` · **Acquisition/availability:** Quantity and price selected in campaign  
**Operating scope:** Ordinary finite dressings; qualified medical use; no universal injury recovery modifier  
**Owner:** K-STOCK/MED · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-014 — Water flask
**Status:** `proposed_complete_opt_in` · **Acquisition/availability:** Capacity from selected physical profile  
**Operating scope:** Holds actual finite potable/nonpotable contents; purchase is not automatic refill  
**Owner:** K-ASSET/K-STOCK · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-015 — Chakra measurement scroll
**Status:** `held_incomplete` · **Acquisition/availability:** Requires a calibrated sensor technique/device contract  
**Operating scope:** Device proposal only: no universal scan range, chakra units measurement or automatic detection  
**Owner:** K-ASSET/K-INFO · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-016 — Explosive seal tag
**Status:** `held_incomplete` · **Acquisition/availability:** Requires explicit damage, radius, timing, safety and counterplay profile  
**Operating scope:** No damage, detonation, quantity or universal price invented  
**Owner:** K-ASSET/K-STOCK · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-017 — Puppet control assembly
**Status:** `held_incomplete` · **Acquisition/availability:** Requires puppet body/component, actuation, sensory and action budget profiles  
**Operating scope:** No free autonomous turn, unlimited string range or assembled robot inferred  
**Owner:** K-ASSET/K-ACTOR · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

### SNCL-G-018 — Permanent sealing matrix
**Status:** `held_incomplete` · **Acquisition/availability:** Needs long-term project, removal trigger, target and specialist parameters  
**Operating scope:** Fūinjutsu source specifically withholds instant permanent-seal default  
**Owner:** K-ASSET/K-WORK · **Instantiation:** No actual object/stock until initialized or acquired; source/native models apply only to exact eligible mode.

## 6. Military unit profiles · 4 native samples
These are **abstract unit profiles**, not units that spawn when their row is selected. Ratings are not literal troop headcount. Units require actually assigned personnel, supplies, authority, command and transport. K-POP/K-ACTOR own real persons; no double-counting of losses at strategic and tactical scale.
| ID | Unit | Power | Defense | Skill | Morale | Supply | Strength (abstract) | Tag |
|---|---|---:|---:|---:|---:|---:|---:|---|
| SNCL-U-N001 | Recon cell | 2 | 2 | 4 | 3 | 3 | 4 | Scout |
| SNCL-U-N002 | Assault detachment | 4 | 3 | 3 | 4 | 4 | 6 | — |
| SNCL-U-N003 | Sealing corps | 2 | 4 | 4 | 3 | 3 | 4 | Seal |
| SNCL-U-N004 | Medical support | 1 | 2 | 4 | 4 | 4 | 4 | Medical |
**Reference:** SNWE R0.3 §12.2: one unit action per phase, 2d6 + Power vs 7 + Defense to Attack; Strength loss 1 success / 2 Margin 3+ / 3 double-six; logistics −1 Supply per third engaged phase. Native support, morale, zero-strength and zero-supply rules remain in §12; the unit block alone does not execute combat.

## 7. Mission templates · 11 source-category adaptations
SNWE §9.1 supplies the 2d6 generator categories in order: 2 Escort, 3 Retrieval, 4 Investigation, 5 Elimination, 6 Diplomacy, 7 Reconnaissance, 8 Sabotage, 9 Defense, 10 Disaster relief, 11 Espionage, 12 Mythic intervention. The following deadlines, objectives, threat interpretations and ranks are **SNCL-authored proposals**, not universally bound to the roll result.
### SNCL-M-001 — Escort (D)
**Brief:** Protect an authorized person or shipment along a selected reachable route. **Completion:** Physical arrival with recipient acknowledgment  
**Threat to author before play:** Threat to passage, delivery deadline or cargo integrity. **Required actual state:** Evidence/actor movement and actual owner-custody transfers  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-002 — Retrieval (D)
**Brief:** Recover a specific identifiable item and establish who may receive it. **Completion:** Item in actual recipient custody  
**Threat to author before play:** Rival claimant, damage or loss while moving. **Required actual state:** Single item ID, search/contact, no discovered auto-stock  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-003 — Investigation (C)
**Brief:** Determine a question from actual traces, records and witness claims. **Completion:** Credible scoped finding delivered to requested party  
**Threat to author before play:** Evidence disappears or suspects learn of inquiry. **Required actual state:** Known/unknown facts, report provenance, no auto-discovery  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-004 — Elimination (B)
**Brief:** Neutralize a specific authorized threat without prescribing killing. **Completion:** Threat unable to complete stated objective by feasible means  
**Threat to author before play:** Exposure, third-party harm and retaliation. **Required actual state:** No mandatory combat or player forced violence  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-005 — Diplomacy (C)
**Brief:** Seek a specifically defined agreement between real agents. **Completion:** Terms authorized and mutually communicated  
**Threat to author before play:** Negotiation delay or breakdown. **Required actual state:** An offer does not force consent or cause settlement  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-006 — Reconnaissance (D)
**Brief:** Observe named sites/routes without altering them. **Completion:** Requested report received by issuing office  
**Threat to author before play:** Target relocation, sighting or report delay. **Required actual state:** Observation time distinct from report receipt  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-007 — Sabotage (B)
**Brief:** Interrupt one identified real component/function. **Completion:** Actual component unusable or service disrupted to agreed extent  
**Threat to author before play:** Detection and independent repair. **Required actual state:** Physical damage applied once; no arbitrary system-wide cascade  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-008 — Defense (C)
**Brief:** Protect designated passage, site or convoy for a time window. **Completion:** Threat prevented within defined physical coverage  
**Threat to author before play:** Scarcity, flank, attrition. **Required actual state:** No unlimited reinforcement or all-seeing defenses  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-009 — Disaster relief (C)
**Brief:** Restore some defined urgent support using real people and resources. **Completion:** Actual delivered care, safe evacuation or provision to designated people  
**Threat to author before play:** Disease/exposure/route and demand under real limits. **Required actual state:** No abstract Supply automatically turned into medicine  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-010 — Espionage (B)
**Brief:** Acquire specifically named protected information. **Completion:** Actor receives valid scoped information and can report  
**Threat to author before play:** Detection, misleading evidence, time. **Required actual state:** Access != truth; receipt != broadcast  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

### SNCL-M-011 — Mythic intervention (S by contract)
**Brief:** Investigate or address a defined mythic anomaly, if enabled by campaign. **Completion:** Explicitly accepted limited objective  
**Threat to author before play:** DSSN Toll, instabilities, site consequences. **Required actual state:** Requires module contract; no instant resurrection or timeline edit  
**Clocks:** Objective 4 or 6 segments if consequential and selected; explicit event triggers; threat 4 or 6 segments if consequential; failed risky actions as defined.  
**Compensation:** Contract selected by issuer; R0.3 default D=1, C=2, B=3, A=4 personal Supply, S by contract; not delivered until paid **Sequence:** Brief → prepare → travel/infiltrate → act → extract → debrief → downtime  
**Scope:** Template is not an actual mission, site, NPC, inventory or guaranteed event

## 8. Institutional templates · 12 proposed service organizations
These define **what must exist for an institution to perform its function**; they do not instantiate named Hidden Villages, canon clans, real people, Kage, estates or political claims.
### SNCL-O-001 — Village administration
**Core owners:** K-ORG/GOV. **Responsibilities:** Mandates, Kage office, policy, budgets, public obligations.  
**Activation prerequisites:** Settlement/setting location; actual officeholders and legal scope  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-002 — Mission assignment office
**Core owners:** K-ORG/K-WORK/ECO. **Responsibilities:** Contracts, rosters, mission grading, pay claims.  
**Activation prerequisites:** Actual employer, work authorization, finite budget  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-003 — Academy
**Core owners:** K-ORG/LIFE/K-ACTOR. **Responsibilities:** Training, records, assessment, qualification.  
**Activation prerequisites:** Teachers, curriculum, training place, attendance and time  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-004 — Medical station
**Core owners:** K-NET/MED/K-ASSET/K-STOCK. **Responsibilities:** Triage, qualified care, bed capacity, consumables.  
**Activation prerequisites:** Staff/stock/space, treatment eligibility, health reporting  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-005 — Field logistics depot
**Core owners:** K-STOCK/K-ASSET/K-NET. **Responsibilities:** Orders, reservations, allocation, dispatch and actual delivery.  
**Activation prerequisites:** Actual depot stock, handlers, routes, approvals  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-006 — ANBU operations branch
**Core owners:** K-ORG/INTEL/INV. **Responsibilities:** Covert assignment, secrecy, source handling, lawful mandate.  
**Activation prerequisites:** Setting authority, handler, assets, actual intelligence  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-007 — Clan council
**Core owners:** K-ORG/LIFE/GOV. **Responsibilities:** Membership, kinship, inheritance and authority decisions.  
**Activation prerequisites:** Actual families/actors and recognized rules  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-008 — Sealing laboratory
**Core owners:** K-WORK/K-ASSET/K-ORG. **Responsibilities:** Sealing research and inspected output.  
**Activation prerequisites:** Qualified personnel, materials, facility, containment and research profile  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-009 — Border watch
**Core owners:** K-ORG/K-INFO/K-NET. **Responsibilities:** Observation, patrol, delay-aware reporting.  
**Activation prerequisites:** Named posts, coverage, actual sensors and assigned rosters  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-010 — Municipal works office
**Core owners:** K-ORG/URBAN/CIV. **Responsibilities:** Maintenance, projects, utilities and access.  
**Activation prerequisites:** Installed assets and real supply/production rates  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-011 — Shinobi field hospital
**Core owners:** MED/K-ACTOR/K-STOCK. **Responsibilities:** Acute care, triage, stabilized patient movement.  
**Activation prerequisites:** Treatment rules and actual supplies; no extra wound ledger  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

### SNCL-O-012 — Exam board
**Core owners:** COMP/K-ORG/LIFE. **Responsibilities:** Eligibility, fixtures, evaluation, records and credential decisions.  
**Activation prerequisites:** Actual exam conditions/officials; results != promotions  
**Authority/outputs:** Template supplies neither actor appointment nor institutional jurisdiction; Linked views, records and decisions through sole Core owners only

## 9. Reusable service profiles · 12 references
### SNCL-S-001 — Field stabilization
**Status:** `native_derived`. **Access:** Medicine + medical kit use. **Procedure:** SNWE §7.5: Intelligence + Medicine DC9, Standard action.  
**Result:** Stops deterioration; no Health recovery or cure by stabilization  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-002 — Major-injury treatment
**Status:** `native_derived`. **Access:** Medicine + one hour + kit use. **Procedure:** SNWE §7.5: DC11.  
**Result:** Downgrades Major→Minor once per injury per day  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-003 — Immediate minor treatment
**Status:** `native_derived`. **Access:** Medicine + ten minutes + kit use. **Procedure:** SNWE §7.5: DC13.  
**Result:** Removes one Minor Injury  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-004 — Critical-injury intervention
**Status:** `native_derived`. **Access:** Medicine + one day + facilities + kit use. **Procedure:** SNWE §7.5: DC13.  
**Result:** Downgrades Critical→Major  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-005 — Psychological support
**Status:** `native_derived`. **Access:** Safe ten-minute rest + Insight. **Procedure:** SNWE §7.5: Wisdom + Insight DC9.  
**Result:** One Trauma removed on success once per character/day  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-006 — Field Mending treatment
**Status:** `native_derived`. **Access:** Access learned Field Mending + touch + chakra. **Procedure:** SNWE §6.4.  
**Result:** Restores 1d6 Health per success once per target per scene; no Injury cure  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-007 — Academy instruction
**Status:** `proposed_template`. **Access:** Actual instructor, attendance, curriculum. **Procedure:** SNWE §§8/24 + Core LIFE.  
**Result:** Learning evidence only; no instant Level/proficiency reward absent eligible advancement  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-008 — Escort logistics
**Status:** `proposed_template`. **Access:** Guards, convoy, route, physical goods. **Procedure:** Core K-STOCK/K-NET/K-TIME.  
**Result:** Transfers actual goods; delivery separate from order/report  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-009 — Border report relay
**Status:** `proposed_template`. **Access:** Witness, channel, receiving office. **Procedure:** Core K-INFO/INTEL.  
**Result:** Record occurrence, observation, send, arrival, interpretation  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-010 — Shinobi-assisted civil works
**Status:** `proposed_template`. **Access:** Actual technique effect + workers and infrastructure. **Procedure:** SNWE §§17–19, §27 + Core WORK/NET.  
**Result:** Output conditional on technique-specific throughput; no universal productivity bonus  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-011 — Village emergency triage
**Status:** `proposed_template`. **Access:** Available qualified staff and actual demand. **Procedure:** SNWE §28 + MED.  
**Result:** Prioritize available tasks; no phantom treatment or patient duplication  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

### SNCL-S-012 — Sealing research
**Status:** `native_derived`. **Access:** Known effect contract, workstation, Supply/materials. **Procedure:** SNWE §9.3 and §22.  
**Result:** Standard 6/DC9, advanced 8/DC11, major 12/DC13; completion still needs field test  
**Capacity constraint:** No service is delivered without actual eligible providers, consumers, stocks, time and authorization

## 10. Held/unconverted specialist catalogue · 16 tracked gaps
These are **placeholders**, not half-powered abilities. Each identifies the missing information required before adoption. An existing campaign-specific complete legacy profile may continue to operate under its own established status, but this proposed catalogue does not silently migrate or deactivate it.
| ID | Candidate | Kind | Minimum missing contract |
|---|---|---|---|
| SNCL-H-001 | Physical shadow clone | manifestation | Independent actions/identity, body stats, originating actor continuity, chakra duplication rules |
| SNCL-H-002 | Summoned scout animal | creature | Species body, all combat stats, contract terms, lifespan/feeding, command range, summon technique |
| SNCL-H-003 | Summoned combat animal | creature | Attack/resistance, size, injury, actual actor identity, contract, control/action budget |
| SNCL-H-004 | Puppet operator | specialist | Construct components/HP/control strings, command bandwidth, sensor and attack modes |
| SNCL-H-005 | Healing extraction technique | medical_jutsu | Exact pathogen/exposure/effect, latency and cure bounds; no universal antidote |
| SNCL-H-006 | Persistent water-producing ninjutsu | world_utility | Output in liters/time, source, purity, energy, duration, storage and field evidence |
| SNCL-H-007 | Long-distance transit technique | mobility | Load, line, accuracy, endpoints, travel time, identity and unsafe-arrival effects |
| SNCL-H-008 | Advanced Chakra sensor | intelligence | Detection geometry, thresholds, countermeasures, false positives, energy and signal transmission |
| SNCL-H-009 | Ocular inherited lineage | bloodline | Grade, awakening, cost, actual technique, weakness, family/scoped setting authority |
| SNCL-H-010 | Fused-element lineage | bloodline | Actual exact known combination, learned techniques, grade, hereditary status, inheritance evidence |
| SNCL-H-011 | Forbidden resurrection seal | mythic | Reversal/retcon/identity, consequences, cost, authorization, death and estate interactions |
| SNCL-H-012 | Village-scale healing network | institutional_capability | Providers, patients per hour, CU demand, equipment, supply lines, adverse effects |
| SNCL-H-013 | Mass-production chakra agriculture | institutional_capability | Yield, inputs, energy, labor, maintenance, ecological consequences, repeatability |
| SNCL-H-014 | Sealed explosive charge | equipment | Real explosive content or magic damage, timing, blast range, hazards, trigger and safe counterplay |
| SNCL-H-015 | Clan-specific canon jutsu compendium | legacy_intake | Actual complete historical source payload, per-entry access/rank/terms and conflict review |
| SNCL-H-016 | Complete historic bloodline catalogue | legacy_intake | Original locked material, named entries, grades and CMRR conversion decisions |

## 11. Shared SCL v1.0 crosswalk (references only)
These are exact **registry evidence**, not automatically usable SSN numerical effects. In particular, Fantasy attack adapters must not be imported as Shinobi damage ratings. Where readiness is on hold, the complete source-native definition/compatible adapter must be retained or the content remains unavailable.
| Shared name | Exact SCL release reference | Semantic type | Registry gate |
|---|---|---|---|
| Unarmed strike | `SCL:PBC-WPN-FL-WPN-M-001@0.2` | `method` | `source_backed_hold` |
| Club | `SCL:PBC-WPN-FL-WPN-M-002@0.2` | `weapon` | `source_backed_hold` |
| Staff | `SCL:PBC-WPN-FL-WPN-M-003@0.2` | `weapon` | `source_backed_hold` |
| Dagger | `SCL:PBC-WPN-FL-WPN-M-004@0.2` | `weapon` | `source_backed_hold` |
| Padded textile | `SCL:PBC-WPN-FL-ARM-002@0.2` | `armor` | `source_backed_hold` |
| Shortbow | `SCL:PBC-WPN-FL-WPN-R-005@0.2` | `weapon` | `source_backed_hold` |
| Mail | `SCL:PBC-WPN-FL-ARM-005@0.2` | `armor` | `selected_qualitative` |
The complete exact crosswalk is also in `IRGS_SNCL_v0_1_SCL_Reference_Crosswalk.json`. No implicit item instantiation or trans-genre stat migration follows from a reference.

## 12. Content usage and campaign activation manifest
The deployment chooses which new candidates become **locally active proposals**. Selection is prospective, versioned, and scoped to an explicitly agreed campaign. Player speech, motives and action declarations remain exclusively theirs.
```yaml
library: IRGS-SNCL-0.1
library_status: proposed
core: IRGS-CORE-3.2
genre_engine: IRGS-SNWE-0.3
shared_catalogue: IRGS-SCL-1.0
content_identity_policy: SNCL separate; SCL:PBC-...@0.2 unchanged
mode: SNWE-R03-NATIVE # or approved persistent-world bridge
enabled_native_entries: [SNCL-J-N001, SNCL-G-001] # examples, not facts
enabled_new_proposals: [] # add only after explicit review
held_candidates: never auto-activate
character_and_setting: campaign_supplied
actual_inventory_population_organizations: campaign_state_only
exact_effect_adapter: SSN R0.3 2d6/d20, NOT Core d100
resource_bridge: select if persistent economic/physical accounting is enabled
source_and_approval_records: per campaign
new_content_effective_date: prospective only
```

### 12.1 Instantiation/activation procedure
1. Select exact library, engine, Core and shared registry versions; verify `id`, variant, type and status.  
2. Verify the campaign setting supplies affinity, actor capability, learning, anatomy, technique access, physical inventory, location and relevant equipment.  
3. Ensure an opt-in proposed record has been reviewed and enabled; require complete output, cost, scope, duration, counterplay, termination and owner mapping.  
4. Create **only actually established** game-state actor/item/site/org/mission records through the proper Core owner and link this immutable definition.  
5. Before an uncertain action, announce feasible consequences and costs; resolve it with one complete SNWE procedure, commit event exactly once, report observations at receipt.  
6. Preserve prices/throughput/geometry unknowns if consequential and unsupported; do not use convenient defaults.  
7. Retire an entry only prospectively through a documented supersession; preserve past instances, event history, paid costs and contractual effects.

## 13. CMRR source and ownership matrix
| Source | Imported/retained | Not imported/held | Destination and ownership |
|---|---|---|---|
| SNWE R0.3 §6.4 | 18 native starter technique records, exact operating effects | Historical extra technique lists not recovered | SNCL J-N; actual CU/rolls stay SNWE/K-ACTOR |
| SNWE R0.3 §§2.4, 5, 9 | Kit, gear pricing/restock, abstract token meaning | Item masses, physical rates and unpriced ninja tools | SNCL G; K-ASSET/K-STOCK at instantiation |
| SNWE R0.3 §§7, 9 | Native treatment/service, research, mission generator | Unsupported universal illness/care/cost statistics | SNCL S and M; MED/K-WORK |
| SNWE R0.3 §12 | 4 unit example blocks and warfare link | No literal troop counts, equipment or formation members | SNCL U; K-POP/K-ORG |
| SNWE R0.3 Part III | Shinobi-specific institution/capability requirements | No particular named village, clan lore or free economic outputs | SNCL O/H; inherited Core services |
| SCL v1.0 R2 | Exact selected shared family references and per-entry hold status | No blanket adoption of 228 held shared families or Fantasy numeric adapter | External SCL pointers, not duplicate SNCL definitions |
| New SNCL authored proposals | 31 opt-in techniques, institutional/mission/service templates | Not historic source canon, not playtested/calibrated | SNCL J-P/M/O/S |

**Accounted exclusion:** Personal attribute tables, HP/SP/CU formulae, chakra core rules, social pressure, classes, levels, Destiny/DSSN, army combat resolution and generic event ownership are **not duplicated as content records**. They remain SNWE and Core procedures. No historical SSN lore is silently discarded or converted; unavailable content is tracked by held-intake record and requires exact source recovery.

## 14. Acceptance and validation plan
The accompanying verifier performs syntax/provenance/identity/status and bounded causal fixtures. It is **not** a full AI GM or live-play test. Required deployment scenarios:
| Test | Expected condition | Evidence status at publication |
|---|---|---|
| CL-01 | One parameterized Spark/Pebble/Droplet learned: choose affinity once; no extra free techniques | Specified, unless separately executed in verifier |
| CL-02 | One Level 2 character casts three C-rank jutsu in scene: costs 5,6,7 CU; no refund on Mold miss | Specified, unless separately executed in verifier |
| CL-03 | Exactly one Output Threshold Trauma on first crossing in round; upkeep included, no repeated charge | Specified, unless separately executed in verifier |
| CL-04 | Failed Precision release spends CU but creates no hit or material damage | Specified, unless separately executed in verifier |
| CL-05 | Illusory Clone and all proposed genjutsu create no physical actor or inventory | Specified, unless separately executed in verifier |
| CL-06 | A proposed transformation cannot copy another actor’s Strength or equipment | Specified, unless separately executed in verifier |
| CL-07 | Field Mending restores Health only, not Injury, and obeys per-target-per-scene cap | Specified, unless separately executed in verifier |
| CL-08 | One field kit with 3 uses supports at most 3 qualifying treatment events | Specified, unless separately executed in verifier |
| CL-09 | An abstract Supply token cannot buy nonexistent physical stock in persistent-world mode | Specified, unless separately executed in verifier |
| CL-10 | Shared SCL source-backed hold refuses native Shinobi numerical effect without compatible profile | Specified, unless separately executed in verifier |
| CL-11 | 4 native unit stat blocks retain their exact separate Power/Defense/Skill/Morale/Supply/Strength | Specified, unless separately executed in verifier |
| CL-12 | A unit loses abstract Strength but campaign population cannot be deducted automatically | Specified, unless separately executed in verifier |
| CL-13 | An academy appointment does not award Level or techniques; instruction may still occur off-screen | Specified, unless separately executed in verifier |
| CL-14 | A mission template does not create enemies, medicine, cash or an obligation until instantiated | Specified, unless separately executed in verifier |
| CL-15 | Two observers receive the same delayed report at different times; no duplicated physical event | Specified, unless separately executed in verifier |
| CL-16 | A held summon lacks stats/contract: cannot instantiate autonomous animal for free | Specified, unless separately executed in verifier |
| CL-17 | One scene's costs and expiry remain conserved through save/reload or scale shift | Specified, unless separately executed in verifier |
| CL-18 | All 18 printed starter effects and 4 printed native units match the exact R0.3 source | Specified, unless separately executed in verifier |
| CL-19 | Draft technique scene effects cannot create permanent water/energy/infrastructure without specified production interface | Specified, unless separately executed in verifier |
| CL-20 | A current campaign retains adopted content/actual state until prospective migration is authorized | Specified, unless separately executed in verifier |
**Calibration:** Chakra throughput and low-rank usefulness, 2d6 vs d20 turn consumption, deception duration/agency, area control, physical protection, actual medical effects, unit-scale mixed play, logistics, training pace, eventual industry and social consequences. New candidate numbers remain provisional. Testing consistency never establishes balance or historical realism.

## 15. Migration and provenance
This is a **new proposed content catalogue**, not SNWE R0.4 and not Core v3.3. Previous engines and source files remain intact. Existing games retain their recorded libraries and actual things until a user-authorized prospective adoption. Rebinding a definition must not spawn gear, heal injury, refund Chakra, restore Supply, duplicate personnel, replay a completed contract or change political allegiance. Source text bytes and release manifests are checksummed separately; a rendered page is not an authority upgrade.
**SNWE R0.3 SHA-256:** `2b4e2e496af03224d9f3aee6902bf9629538a9033c119141b89fdf35741e9e84`  
**SNWE R0.3 receiving binding SHA-256:** `e135f37604f0c9c4111682a97da26b201d2cae954d9d03633251bcae5a34de27`  
**SCL v1.0 registry SHA-256 (from R2):** `67c4e0eb4b67fbc8f2cf874dae06381bf2e4c9eb48850a35d7ffc10c8a4a35b9`

**Outstanding:** Complete historical jutsu, summons, bloodlines, ninja-tool effects and named setting profiles require their original source payloads and CMRR review; no invented completion is asserted. Physical and institutional throughput need separately calibrated ability/profile models. The library’s bounded tests cannot certify an unrestricted game.
