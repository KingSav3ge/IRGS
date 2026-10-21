# IRGS — Military Content Library
## Version 1.0 — Shared-Catalogue Rebuild (Proposed)

**Document ID:** `IRGS-MIL-LIB-1.0`  
**Release date:** 14 October 2026  
**Classification:** Military genre content catalogue and equipment/profile blueprint, not a second game engine  
**Reference Core:** `IRGS-CORE-3.2`  
**Shared content:** `IRGS-SCL-1.0`; canonical family revisions preserved as `@0.2`  
**Primary source:** *IRGS Military Equipment and Technology Library v0.1* (`ML-0.1`), seven sections  
**Military genre interface source:** *Soldier and Military Life Simulation — Slim Engine v1.0* (`MLS-SLIM-1.0`), 17 sections  
**Current authority:** Proposed; source-derived descriptions, new contracts, calibration and deployment adoption remain separately classified. No live playtesting or historical/engineering certification is claimed.

> **Design contract:** Reuse Core/SCL identities and ownership, retain exactly the six era tags and twelve military browse categories, and keep genre-owned military loadouts, technology eligibility, weapons/platform operating models and career-related content distinct. A catalogue entry neither creates an actual object nor defines a performance number by naming an item.

## Part I — Purpose, authority, dependencies

### 1. Purpose and limits
This document is a complete military **content reference layer**, not a reprint of shared items or an adoption of equipment statistics. It provides era/category browse content, military-specific content templates, item/crew/station/issue contracts, profile activation rules, campaign manifest fields, source reconciliation and acceptance criteria. Combat, injury, time, logistics, economy, command authority and simulation remain with their adopted owners. The original `ML-0.1` supplies no actual gun dimensions, damage, protection ratings, load capacities, unit costs, aircraft speeds, historical regional eligibility or quantified service performance; this version does not invent them.

### 2. Authority and compatibility
The hierarchy is explicit user direction → established campaign override → adopted compatible genre rules → adopted Core → selected content/model profile → proposal only where unresolved. SCL defines reference *families*, not item existence or procedure outcomes. The 51 selected SCL qualitative contracts and 228 held families retain their source statuses; R1/R2 qualification drafts do **not** automatically lift holds.

**Compatibility caveat:** The uploaded `MLS-SLIM-1.0` is expressly pinned to `IRGS-CORE-3.0` and `IRGS-SCL-0.1`. It is **not silently migrated** by citing this library. Its service/command/duty/leave/equipment workflows are input to this content specification. Deployment on Core 3.2 requires an explicit, reviewed procedure/owner/event/model bridge and user adoption. Until then, run the adopted predecessor for any outcome-changing affected procedure; catalogue lookup is read-only and can be used for design. No automatic retroactive conversion.

### 3. Reference and content identity
Use `MIL-LIB:<CATEGORY>-<TEMPLATE>@1.0` for newly proposed **military specialization templates**. Such an ID is never a physical item, an engine action, or a replacement SCL ID. Reusable physical/content families use the actual `SCL:PBC-...@0.2` registry ID and mode selector, plus a source and native adapter when required. The catalogue as a package is v1.0, but immutable shared entry revisions remain `@0.2`. Source `WPN-M-006A/B` and their selectors identify two modes of one weapon instance, not duplicate swords.

**Content resolution:** `source family → SCL family/selector → MIL template (optional) → dated local design/variant → complete native effect & operating adapter → actual campaign instance`. No step automatically creates the next step. Unsupported fields remain `unknown`, not zero. Records include scoped `source/status/version/owner/visibility` and effective time.

### 4. Contract schema
```yaml
# Specimen schema, not an instantiated item
military_template_id: "MIL-LIB:WPN-FIREARM@1.0"
status: Proposed
source: "ML-0.1 §3"
shared_reference: null          # exact SCL:PBC-...@0.2 if applicable
shared_selector: null           # e.g. modes.thrust if applicable
semantic_kind: equipment-family/operating-template
era_tags: []                   # browse candidates, not entitlement
local_region_date: unknown
institution_eligibility: unknown
configuration: unknown
allowed_modes: []
operator_requirements: unknown
consumable_and_power_bindings: []
performance_and_effect_adapter: unknown
maintenance_support: unknown
activation_gates: []
owner_records: [K-ASSET, K-STOCK, K-ACTOR]
calibration_provenance: unknown
readiness: proposed-unqualified
```
A setting/model may deliberately set `not applicable`, `unsupported` or a measured/accepted value; do not populate an absent value from a period label. The schema defines *what must be known* rather than fabricating it.

## Part II — Six era tags and twelve categories

### 5. Era selection (unchanged from `ML-0.1` and SCL §23)
| ID | Group | Source-defined browsing scope |
| --- | --- | --- |
| ERA-ANT | Antiquity | Ancient societies before the first century AD; bronze and iron technologies where locally established |
| ERA-EAD | Early Centuries AD | Roughly the first–fifth centuries AD; early imperial and late-antique contexts |
| ERA-MED | Middle Ages | Roughly AD 500–1500; later regional/period subdivisions can refine availability |
| ERA-EMD | Early Modern | Roughly AD 1500–1800; expanding gunpowder warfare, maritime systems and organized military supply |
| ERA-CON | Contemporary | Used broadly in this library for industrial and modern military contexts, approximately the nineteenth century to the present |
| ERA-SCI | Science Fiction | Fictional future or alternative technological contexts; availability determined by the setting |

**Important:** Contemporary deliberately includes nineteenth-century industrial to present-day content. Early Centuries AD is a separate browsing group though historically part of Late Antiquity in many schemes. All dates are editorial approximations, not universal technology progression. Regions, institutions, material access, manufacturing, chronology, laws and knowledge determine actual eligibility. Equipment can persist across eras. The six tags are not technology levels.

### 6. Universal military browsing categories (unchanged from `ML-0.1` §2)
| Code | Category | Source scope |
| --- | --- | --- |
| WPN | Personal weapons | Melee weapons, projectile weapons, firearms and other personal weapon systems |
| PRO | Protection and clothing | Armor, shields, helmets, uniforms, footwear and protective gear |
| SUP | Support weapons | Siege equipment, artillery and other crew-operated weapon systems |
| MUN | Ammunition and expendables | Projectiles, propellants, cartridges, shells and setting-specific consumables |
| KIT | Personal and camp equipment | Carrying gear, bedding, shelter, cooking, lighting and hygiene equipment |
| TRN | Land transport and animal equipment | Saddlery, pack equipment, carts, wagons, vehicles and rail transport |
| NAV | Naval equipment | Boats, ships, rigging, propulsion and maritime support |
| AIR | Aviation and space equipment | Balloons, aircraft, spacecraft and associated equipment where applicable |
| COM | Communication and administration | Signals, correspondence, records, printing, telegraphy, radio and digital systems |
| OBS | Observation and navigation | Maps, surveying, optical equipment, sensors and navigation aids |
| ENG | Engineering and production | Hand tools, agriculture, construction, workshops, machinery and utilities |
| MED | Care and medical equipment | Medical supplies, care facilities, evacuation equipment and setting-specific treatment technology |

### 7. Complete six-by-twelve era/category candidate catalogue
Every entry below is a **candidate family**, not a specific invented product, official issue, local technological fact or numeric specification. The original index grouped transport/naval/aircraft together and omitted a dedicated ammunition-by-era table; the following subdivides those source categories conservatively. `AIR` cells marked not sourced do **not** assert global technological impossibility, merely that the original index contains no ordinary deployment entry.

#### Antiquity — `ERA-ANT`
| Category | Candidate content (not automatic availability) | Classification |
| --- | --- | --- |
| WPN | spear, sword, axe, dagger, bow, sling, thrown weapon | source-supported editorial subdivision |
| PRO | shields, helmets, textiles, scale; mail only where locally attested | source-supported editorial subdivision |
| SUP | mechanical artillery, siege engines; chariot armament where used | source-supported editorial subdivision |
| MUN | arrows, sling stones, thrown projectiles; mechanical artillery ammunition | derived candidate; specific munition profiles absent from ML 0.1 |
| KIT | clothing, carrying bags, bedding, camp shelter, cook vessels, lamp | source-supported editorial subdivision |
| TRN | pack/riding animal, cart, wagon, chariot, tack | source-supported editorial subdivision |
| NAV | oared or sailing vessel where established | source-supported editorial subdivision |
| AIR | Not sourced as a routinely available platform | explicit unsupported default (not globally impossible) |
| COM | messengers, oral orders, standards, visual/sound signals, written record where literate | source-supported editorial subdivision |
| OBS | local route knowledge, surveying, maps/charts, astronomical navigation where known | source-supported editorial subdivision |
| ENG | agricultural, carpentry, metalworking, construction and waterworks tools | source-supported editorial subdivision |
| MED | period-specific care supplies, instruments and casualty transport | source-supported editorial subdivision |

#### Early Centuries AD — `ERA-EAD`
| Category | Candidate content (not automatic availability) | Classification |
| --- | --- | --- |
| WPN | iron/steel blades, spears, lance, bow, sling, javelin; regional crossbow | source-supported editorial subdivision |
| PRO | shield, helmet, mail, scale, lamellar, regional protection | source-supported editorial subdivision |
| SUP | siege engine, assault equipment, mechanical artillery | source-supported editorial subdivision |
| MUN | projectiles and other compatible expendables for locally attested systems | derived candidate; specific munition profiles absent from ML 0.1 |
| KIT | tent, blanket, cookware, water container, lamp, repair tools | source-supported editorial subdivision |
| TRN | animal transport, wagon, cavalry tack | source-supported editorial subdivision |
| NAV | merchant and war vessels where local capacity supports them | source-supported editorial subdivision |
| AIR | Not sourced as a routinely available platform | explicit unsupported default (not globally impossible) |
| COM | courier network, written order, administrative record, military signal | source-supported editorial subdivision |
| OBS | map, survey tool, coast knowledge, astronomical aid | source-supported editorial subdivision |
| ENG | craft workshop, mill, road/bridge tool, fortification and supply equipment | source-supported editorial subdivision |
| MED | medical instruments, dressings, medicines and care equipment where organized | source-supported editorial subdivision |

#### Middle Ages — `ERA-MED`
| Category | Candidate content (not automatic availability) | Classification |
| --- | --- | --- |
| WPN | sword, spear, lance, axe, mace, polearm, bow, crossbow; late regional firearm | source-supported editorial subdivision |
| PRO | shield, helmet, padding, mail, lamellar/scale, coat of plates, brigandine, later plate | source-supported editorial subdivision |
| SUP | siege engine/tower; early gunpowder artillery where established | source-supported editorial subdivision |
| MUN | arrow, bolt, siege projectile and later region-specific powder/projectile | derived candidate; specific munition profiles absent from ML 0.1 |
| KIT | clothing, shelter, bedding, cookware, lamp, containers, sewing tools | source-supported editorial subdivision |
| TRN | saddlery, pack train, cart, wagon | source-supported editorial subdivision |
| NAV | sailing ship or galley according to region/date | source-supported editorial subdivision |
| AIR | Not sourced as a routinely available platform | explicit unsupported default (not globally impossible) |
| COM | messenger, correspondence, standard, horn, bell, printing where established | source-supported editorial subdivision |
| OBS | map, compass, survey and maritime navigation aid where locally known | source-supported editorial subdivision |
| ENG | farming/smithy/mill tools, siege engineering, construction and stores | source-supported editorial subdivision |
| MED | period-specific care instruments, dressing, medicines and care facility | source-supported editorial subdivision |

#### Early Modern — `ERA-EMD`
| Category | Candidate content (not automatic availability) | Classification |
| --- | --- | --- |
| WPN | pike, sword, sabre, bayonet, musket, pistol, rifle; matchlock/wheellock/flintlock as applicable | source-supported editorial subdivision |
| PRO | uniform/clothing, selected helmet, cuirass and role-dependent armor | source-supported editorial subdivision |
| SUP | gunpowder cannon, mortar, siege artillery and naval gun | source-supported editorial subdivision |
| MUN | powder, shot, projectile, charge, fuze as supported by specific arm | derived candidate; specific munition profiles absent from ML 0.1 |
| KIT | tents, packs, clothing, bedding, cookware, cleaning/repair kit | source-supported editorial subdivision |
| TRN | animal trains, wagons and their support equipment | source-supported editorial subdivision |
| NAV | sailing warships and merchant vessels | source-supported editorial subdivision |
| AIR | Not sourced as a routinely available platform | explicit unsupported default (not globally impossible) |
| COM | printed material, courier/post, signal flag, institutional record | source-supported editorial subdivision |
| OBS | map, compass, survey equipment, optical instrument and navigation aids | source-supported editorial subdivision |
| ENG | arsenal, foundry, powder mill, print works, shipyard and powered mill | source-supported editorial subdivision |
| MED | medical chest, instruments, dressing and field/naval care equipment | source-supported editorial subdivision |

#### Contemporary — `ERA-CON`
| Category | Candidate content (not automatic availability) | Classification |
| --- | --- | --- |
| WPN | percussion/cartridge/repeating/automatic arms, sidearm, anti-armor weapon by date | source-supported editorial subdivision |
| PRO | uniform, camouflage, helmet, respirator, body armor, carrying system by date | source-supported editorial subdivision |
| SUP | machine gun, mortar, artillery, rocket, missile, remote weapon where fielded | source-supported editorial subdivision |
| MUN | cartridge, shell, rocket, missile and other incompatible specified expendables | derived candidate; specific munition profiles absent from ML 0.1 |
| KIT | manufactured uniforms, shelters, preserved rations, portable light, hygiene, electronics | source-supported editorial subdivision |
| TRN | rail, motor vehicle, armored vehicle by date | source-supported editorial subdivision |
| NAV | ship and submarine by technology/region | source-supported editorial subdivision |
| AIR | balloon, aircraft, helicopter and other aviation by date | source-supported editorial subdivision |
| COM | telegraph, telephone, radio, satellite/digital communications by date | source-supported editorial subdivision |
| OBS | photography, optics, radar, sonar, night vision, thermal and satellite navigation by date | source-supported editorial subdivision |
| ENG | industrial plant, engines, machine tools, generator, refrigeration, diagnostic gear | source-supported editorial subdivision |
| MED | field hospital, ambulance, surgery and advanced diagnostic/life-support by date | source-supported editorial subdivision |

#### Science Fiction — `ERA-SCI`
| Category | Candidate content (not automatic availability) | Classification |
| --- | --- | --- |
| WPN | setting-defined advanced projectile, energy or other arm; legacy arms may remain | setting-only candidate, not enabled by default |
| PRO | advanced armor, powered protection, environmental suit where enabled | setting-only candidate, not enabled by default |
| SUP | directed-energy, orbital/remote or other advanced support platform where enabled | setting-only candidate, not enabled by default |
| MUN | specific compatible energy, ammunition, propellant or other finite expendable | setting-only candidate, not enabled by default |
| KIT | survival kit, environmental shelter, smart equipment, food/water processing | setting-only candidate, not enabled by default |
| TRN | advanced vehicle, walker/mech or alternative conveyance where enabled | setting-only candidate, not enabled by default |
| NAV | setting-defined advanced naval craft | setting-only candidate, not enabled by default |
| AIR | atmospheric advanced aircraft, spacecraft and orbital facility where enabled | setting-only candidate, not enabled by default |
| COM | advanced network, AI-assisted link, interplanetary link per selected physics | setting-only candidate, not enabled by default |
| OBS | advanced sensor, autonomous reconnaissance, augmented display/navigation | setting-only candidate, not enabled by default |
| ENG | robotic fabrication, advanced production, power and autonomous support | setting-only candidate, not enabled by default |
| MED | advanced diagnostics, cybernetics and setting-defined restorative technology | setting-only candidate, not enabled by default |

### 8. Source and extrapolation boundaries
**Source-backed:** the six eras, twelve categories, the old three period tables, the broad index examples, and absence of numerical equipment models. **Editorial inference:** subdivision of grouped transport into `TRN/NAV/AIR` per original labels, and the separately indexed `MUN` candidate examples implied by named missile and firearm systems. **New proposals:** the 48 military operating templates below, records/gates/acceptance cases, and Core v3.2 bridge. **Explicit exclusions:** none of these tables establishes historical local availability, battlefield use, combat penetration, first-aid efficacy, annual production, price, mass, rate of fire or specific model performance.

## Part III — Exact shared-family crosswalk

### 9. Binding examples checked against normative SCL registry
| Content | Legacy source ID | Exact SCL family | Mode | Military interpretation |
| --- | --- | --- | --- | --- |
| Physical melee weapon | WPN-M-006A/B | SCL:PBC-WPN-FL-WPN-M-006@0.2 | modes.cut / modes.thrust | Legacy Fantasy physical family; no universal Threat or historical rating |
| Spear | WPN-M-013 | SCL:PBC-WPN-FL-WPN-M-013@0.2 | default | Physical family; actual form/mass/skill/period calibrated locally |
| Crossbow | WPN-R-007 | SCL:PBC-WPN-FL-WPN-R-007@0.2 | default | Fantasy source mechanics not usable as firearms/modern ratings |
| Plate armor | ARM-009 | SCL:PBC-WPN-FL-ARM-009@0.2 | none | Construction/coverage adapter required; no universal ballistic resistance |
| Carry/storage container | STO-001 | SCL:PBC-EQP-PL-STO-001@0.2 | none | Capacity is not supply; contents stay independent |
| First aid kit | EQP-MED-001 | SCL:PBC-EQP-PL-EQP-MED-001@0.2 | none | Equipment presence does not create treatment |
| Hand tool kit | EQP-TOOL-001 | SCL:PBC-EQP-PL-EQP-TOOL-001@0.2 | none | Qualified work and materials separately required |
| Workshop equipment | EQP-SHOP-001 | SCL:PBC-EQP-PL-EQP-SHOP-001@0.2 | none | Same real tooling for site/equipment/service facets |
| Generator | EQP-PWR-001 | SCL:PBC-EQP-PL-EQP-PWR-001@0.2 | none | One finite fuel stock and service flow |
| Radio | EQP-COM-001 | SCL:PBC-EQP-PL-EQP-COM-001@0.2 | none | Transmitter is not guaranteed transmission/reception |
| Manuals | RES-KNW-001 | SCL:PBC-EQP-PL-RES-KNW-001@0.2 | none | Information content; physical copy may be separate object |
| Map/records | RES-KNW-002 | SCL:PBC-EQP-PL-RES-KNW-002@0.2 | none | Records are information, not magically current intelligence |
| Rations | RES-FOOD-001 | SCL:PBC-RES-PL-RES-FOOD-001@0.2 | none | Stock and nutritional profile independent |

These examples are *bindings*, not independent duplication of neutral definitions. Several examples were initially sourced through Fantasy v1.0 in SCL; their existence as a shared qualitative family does not import Fantasy `Threat`, `Defeat`, `Defense`, `Structure`, `d100`, or any fantasy physiological statistic into military history. Treat held family status as held; consult its exact preserved source payload and its qualification dossier.

### 10. Physical composition and ownership rules
- **Weapon:** one physical object; attack or service modes are methods linked to the same asset. `SCL` families and mode selectors are read-only; the instance tracks owner, custodian, condition, location, serial/lot where applicable, attached parts and maintenance.
- **Ammunition:** projectile, propellant, primer, fuze, payload, magazine and case can be distinct components. Choose an assembly/lot model and a single actual flow path; a cartridge must not be charged twice as both `cartridge` and all its contents for the same activation. Firing, ejecting and recovering are distinct events.
- **Armor:** coverage, construction, condition, local breach, fit, burden and channel-specific protection are different. A protection value in one model never converts automatically to another; no repeated armor benefit from wearing the same layer.
- **Vehicle/platform:** parent asset and its stations, weapons, sensors, feeds and crew do not independently duplicate hull stock or completed actions.
- **Facilities:** a barracks/workshop/medical site and its service facets can share the exact same power, materials, staff, workspace and machines; view multiple functions without creating additional physical capacity.
- **Knowledge:** manual, chart or radio transmission changes evidence and access, not competence, legal authority, actual action or universally perfect observation.

## Part IV — Military-specific template catalogue

The following 48 **proposed, unqualified** specialization templates are organized by the original twelve categories. Their field lists are obligations on a selected local model; they are deliberately not equipment stat blocks. Where an exact `SCL` family already exists, inherit it. Where none exists, retain the old source family suggestion and author a newly qualified SCL or local item variant without pretending it is already registered.

### 11.1 `WPN` — Personal weapons

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:WPN-MELEE@1.0` — Service melee weapon | A purpose-built or issued weapon used through one or more physical contact modes | construction; mode geometry; reach; user handling; protection/effect adapter | Physical object; qualifying user; feasible action mode | `SCL:PBC-WPN-FL-WPN-M-006@0.2` |
| `MIL-LIB:WPN-MISSILE@1.0` — Human-powered projectile weapon | Bow, sling, crossbow or comparable projectile-delivery equipment | launcher mode; draw/operating requirement; projectile compatibility; range envelope; loading cycle | Compatible ammunition; physical capacity; supported line of effect | `SCL:PBC-WPN-FL-WPN-R-005@0.2` |
| `MIL-LIB:WPN-FIREARM@1.0` — Individual firearm family | Region/date-supported individual firearm or setting-defined projectile arm | chamber/feed; cartridge compatibility; cycle; ignition; handling; effect adapter; storage | Technology proof; functioning action; permitted user; stock separately tracked | No exact SCL family assigned; hold |
| `MIL-LIB:WPN-ADVANCED@1.0` — Speculative personal weapon | Science-fiction personal armament without assumed energy mechanism | source/medium; power/feed; effect type; range; counterplay; failure envelope | Specific setting authorization; complete compatible effect/power model | No exact SCL family assigned; hold |

### 11.2 `PRO` — Protection and clothing

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:PRO-UNIFORM@1.0` — Service clothing and identification | Uniform, insignia and occupational clothing used for identification and ordinary function | cut/material; climate; fit; durability; recognition/issue policy | Actual issued or owned clothing; does not confer rank or legal authority | No exact SCL family assigned; hold |
| `MIL-LIB:PRO-ARMOR@1.0` — Military protective ensemble | Assembled protective pieces with coverage, construction and protective channels | regions; layers; coverage gaps; mass/fit; threats; condition; mobility interface | Selected protection model; no summing full ratings for overlapping layers | `SCL:PBC-WPN-FL-ARM-009@0.2` |
| `MIL-LIB:PRO-RESPIRATOR@1.0` — Hazard/environmental protective gear | Respiratory or environmental protection for specified hazards | hazard channel; filter/air supply; seal; fit; duration; thermal burden; maintenance | Actual appropriate components/supply; not universal hazard immunity | No exact SCL family assigned; hold |
| `MIL-LIB:PRO-POWERED@1.0` — Powered protective suit or exoskeleton | Powered worn system distinct from ordinary clothing and armor | actuation; power; control; mass; load; mobility; failure; protection modes | Setting technology; operator qualification; actual energy and maintenance | No exact SCL family assigned; hold |

### 11.3 `SUP` — Support weapons

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:SUP-MECHANICAL@1.0` — Mechanical support/siege weapon | Crew-operated mechanical artillery and siege systems | assembly; ammunition; crew stations; traverse; emplacement; range/effect envelope | Real crew, emplacement and suitable projectiles; no free coordinated shots | No exact SCL family assigned; hold |
| `MIL-LIB:SUP-GUNPOWDER@1.0` — Gunpowder artillery family | Crew-served cannon, mortar or related support arm | tube/launcher; projectile; charge; fuze; recoil; emplacement; crew; exposure | Historical/setting availability; separate munitions and service procedures | No exact SCL family assigned; hold |
| `MIL-LIB:SUP-GUIDED@1.0` — Guided or remote support weapon | System requiring target, control, guidance and effect configuration | launcher; munition; sensor/tracking; authorization; network; flight/effect model | No omniscient targeting or unlimited ammunition; actual contact/lock | No exact SCL family assigned; hold |
| `MIL-LIB:SUP-FIXED@1.0` — Installed defensive/vehicle armament | Weapon physically integrated into fortification, vessel or platform | mount; orientation; stabilization; control; magazines; power; crew; maintenance | Parent asset configuration; component damage affects only linked functions | No exact SCL family assigned; hold |

### 11.4 `MUN` — Ammunition and expendables

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:MUN-PROJECTILE@1.0` — Recoverable projectile expendable | Arrows, bolts, stones, sling ammunition or equivalent launched objects | material; dimension; compatible launcher; count/mass; recovered condition | Separate stock; fired/recovered only through actual location/condition change | No exact SCL family assigned; hold |
| `MIL-LIB:MUN-CHARGE@1.0` — Propellant/charge input | Powder or other propellant consumed by a compatible weapon/engine | chemistry/energy type; storage; charge unit; compatibility; ignition; effects | Actual finite stock; incompatible charges rejected; never abstract bullets | No exact SCL family assigned; hold |
| `MIL-LIB:MUN-CARTRIDGE@1.0` — Integrated firearm ammunition | Cartridge or ammunition assembly including declared consumable parts | caliber/chamber; projectile; propellant; primer; lot; condition; feed | Must match actual weapon; spent cases and recoverability per selected model | No exact SCL family assigned; hold |
| `MIL-LIB:MUN-PAYLOAD@1.0` — Specialized expendable effect package | Fuze, charge, missile, flare, smoke or other configured expendable | payload/effect; arming; delivery; safe handling; storage; counterplay | Effect must be separately modeled; no generic explosion or casualty | No exact SCL family assigned; hold |

### 11.5 `KIT` — Personal and camp equipment

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:KIT-CAMP@1.0` — Personal camp and bivouac kit | Bedding, shelter, cooking, lighting and hygiene kit for personnel | component inventory; mass/bulk; water/fuel dependency; weather protection | Possession does not perform setup, preparation or personal care | `SCL:PBC-EQP-PL-STO-001@0.2` |
| `MIL-LIB:KIT-CARRY@1.0` — Load-carrying system | Pack, harness and carrying structures for personal supplies | capacity; volume/bulk; attachment; condition; actual item positions | Load uses real mass distribution; capacity not stock | No exact SCL family assigned; hold |
| `MIL-LIB:KIT-FIELDREPAIR@1.0` — Portable repair and cleaning kit | Occupation-specific supplies for maintaining issued field equipment | tools; compatible spare parts; consumables; expertise; repair scope | Kit cannot create parts, competence or accepted equipment without work | `SCL:PBC-EQP-PL-EQP-TOOL-001@0.2` |
| `MIL-LIB:KIT-RATIONS@1.0` — Field food and water package | Prepared or carried food/water/support selection | identity; actual lots; nutrition/water; packaging; shelf life; use | One source of stock; rations and feeding not charged twice | `SCL:PBC-RES-PL-RES-FOOD-001@0.2` |

### 11.6 `TRN` — Land transport and animal equipment

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:TRN-SADDLERY@1.0` — Mounted and pack-animal equipment | Tack, saddles, reins and burden attachment for living mounts | animal fit; pressure/load; tack condition; cargo attachment; skill | Animal remains autonomous living actor with actual needs | No exact SCL family assigned; hold |
| `MIL-LIB:TRN-WAGON@1.0` — Cart/wagon/chariot carriage | Wheeled conveyance requiring actual propulsion/animals and road access | payload; traction; axles; terrain/route; maintenance; handling crew | Real route, draft means, loading and transfer | No exact SCL family assigned; hold |
| `MIL-LIB:TRN-MOTOR@1.0` — Motorized land transport | Fuel/electrically powered military transport platform | engine/feed; range/consumption; load; route; crew; failures; maintenance | Vehicle operating profile; no fuel or instant travel granted | No exact SCL family assigned; hold |
| `MIL-LIB:TRN-ARMORED@1.0` — Armored fighting/support land vehicle | Land platform combining mobility, crew stations and protective/weapon subsystems | hull; mobility; power; crew; protection channels; weapons; sensors; logistics | Platform composition no independent duplicated component/munition stock | No exact SCL family assigned; hold |

### 11.7 `NAV` — Naval equipment

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:NAV-OARED@1.0` — Oared or sail-equipped military craft | Era/region-dependent naval transport or combat vessel | hull/loading; propulsion; weather; crew; seamanship; route; support | MAR module and actual qualified crew, not generic movement numbers | No exact SCL family assigned; hold |
| `MIL-LIB:NAV-SAILING@1.0` — Sailing ship and nautical equipment | Sailing transport/warship rigging and navigation systems | sail/rigging; hull; weather; berth; crew; maintenance; cargo | MAR module; physical ports/loading; separate weapons and supplies | No exact SCL family assigned; hold |
| `MIL-LIB:NAV-POWERED@1.0` — Powered surface or subsurface vessel | Engine-powered naval platform with optional subsurface operation | propulsion/feed; hull; endurance; crew; environmental envelope; sensors | MAR/vessel profile including pressure/depth where applicable | No exact SCL family assigned; hold |
| `MIL-LIB:NAV-FUTURE@1.0` — Speculative naval platform | Setting-enabled advanced marine platform or ship | propulsion; environmental interface; command; power; failure/repair | No automatic FTL, invulnerability or artificial intelligence | No exact SCL family assigned; hold |

### 11.8 `AIR` — Aviation and space equipment

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:AIR-LIGHTER@1.0` — Lighter-than-air observation/transport craft | Balloons or airships where era/region support them | lift/gas; weather; controls; launch/landing; personnel/payload | Flight model and operational envelope; no airspeed by era | No exact SCL family assigned; hold |
| `MIL-LIB:AIR-AIRCRAFT@1.0` — Powered atmospheric aircraft | Fixed-wing or rotary-wing military aircraft | lift; propulsion; flight/landing; crew; payload; maintenance; weather | Compatible aviation model; airframe not a generic vehicle speed | No exact SCL family assigned; hold |
| `MIL-LIB:AIR-UNMANNED@1.0` — Uncrewed aerial vehicle | Uncrewed flight platform controlled locally or remotely | autonomy; sensor; communication; flight; endurance; control mandate | Real channels, operator knowledge and power; no omniscience | No exact SCL family assigned; hold |
| `MIL-LIB:AIR-SPACE@1.0` — Spacecraft and orbital platform | Technology-gated space transport, station or combat craft | flight frame/epoch; propulsion; life support; power; thermal; crew; docking | SPACE foundation; no inferred FTL, gravity or vacuum immunity | No exact SCL family assigned; hold |

### 11.9 `COM` — Communication and administration

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:COM-SIGNAL@1.0` — Visual/sound signal system | Standards, horns, flags and other line-of-sight signaling | signals/code; visibility/acoustics; recipient; training; latency | Actual observation/receipt; authority not transferred by flag alone | No exact SCL family assigned; hold |
| `MIL-LIB:COM-COURIER@1.0` — Military records and courier equipment | Dispatch cases, written orders, routes and administrative carriers | message identity; sender/recipient; route; security; issue/receipt times | Written order is information; copy possession not command execution | `SCL:PBC-EQP-PL-RES-KNW-001@0.2` |
| `MIL-LIB:COM-RADIO@1.0` — Radio/telegraph/telephone equipment | Era-enabled electrical communications | power; compatibility; medium; bandwidth; range; network; delay | Actual path and receivers; source messages separate from receipt | `SCL:PBC-EQP-PL-EQP-COM-001@0.2` |
| `MIL-LIB:COM-NETWORK@1.0` — Digital or speculative command network | Connected communications and administration service | interfaces; cyber/security; link; traffic; credentials; synchronization | No automatically global knowledge or unlimited AI agency | No exact SCL family assigned; hold |

### 11.10 `OBS` — Observation and navigation

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:OBS-MAP@1.0` — Cartographic/route/navigation aids | Map, chart, compass and route planning references | scale/coverage; date; provenance; accuracy; update; literacy | Observation differs from interpretation; map is not route feasibility | `SCL:PBC-EQP-PL-RES-KNW-002@0.2` |
| `MIL-LIB:OBS-OPTICAL@1.0` — Optical observation equipment | Binoculars, scopes or suitable era optics | field of view; environmental limits; effective detection; handling | Better observation never creates invisible target data | No exact SCL family assigned; hold |
| `MIL-LIB:OBS-SENSOR@1.0` — Electronic and remote sensor system | Radar, sonar, thermal or other spectrum sensors | channel; sensitivity; range; obstruction; power; processing; uncertainty | Detect ≠ classify ≠ locate precisely; genre channel required | No exact SCL family assigned; hold |
| `MIL-LIB:OBS-SURVEY@1.0` — Military surveying and intelligence tools | Measuring and mapping equipment, sampling and reconnaissance record | instrument; method; coverage; error; operator; data storage | Separate observation, interpretation, report receipt and actual state | No exact SCL family assigned; hold |

### 11.11 `ENG` — Engineering and production

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:ENG-FIELD@1.0` — Field engineering/entrenchment tools | Tools and materials for fieldworks and obstacle alteration | tooling; material; qualified crew; site; work; inspection | Actual work and material debit; no instant completed fortification | `SCL:PBC-EQP-PL-EQP-TOOL-001@0.2` |
| `MIL-LIB:ENG-WORKSHOP@1.0` — Military workshop/arsenal support | Repair/manufacturing work areas using appropriate machines | site; tooling; skill; drawings; feeds; throughput; commissioning | Workshop/site/tool/service capacity one physical source of truth | `SCL:PBC-EQP-PL-EQP-SHOP-001@0.2` |
| `MIL-LIB:ENG-UTILITY@1.0` — Power, water and field utility equipment | Generation, water, cold chain, heating and sanitation support | actual input/output; feeds; network; capacity; quality; maintenance | Service capacity not stock; no free energy or created water | `SCL:PBC-EQP-PL-EQP-PWR-001@0.2` |
| `MIL-LIB:ENG-FORT@1.0` — Fortifications and fixed defense sites | Fieldworks, walls, prepared emplacements, shelters and fortresses | structure; position; maintenance; access; garrison; storage | Construction project accepted before functional site; no fortress HP | No exact SCL family assigned; hold |

### 11.12 `MED` — Care and medical equipment

| Military template | Use | Native profile fields | Activation / no-free-effect constraint | SCL exemplar |
| --- | --- | --- | --- | --- |
| `MIL-LIB:MED-AID@1.0` — First-aid equipment | Dressing, splint, assessment and first-response supplies | stock; sterility; care objective; qualified provider; exposure | Possession does not treat; medicine follows selected MED model | `SCL:PBC-EQP-PL-EQP-MED-001@0.2` |
| `MIL-LIB:MED-EVAC@1.0` — Casualty transport equipment | Litters, stretchers, ambulance platforms and recovery transport | patient state; handling crew; route; movement; stabilization | Evacuation changes location only when executed; does not heal | No exact SCL family assigned; hold |
| `MIL-LIB:MED-FACILITY@1.0` — Military care facility | Organized field/hospital care facility and service | space; sanitation; staff; supplies; procedures; beds; power | Beds ≠ staffed care capacity; no automatic recovery | No exact SCL family assigned; hold |
| `MIL-LIB:MED-ADVANCED@1.0` — Speculative medical technology | Fictional diagnostics, cybernetics or restorative intervention | power; method; anatomy; inputs; outputs; constraints; side effects | Setting enables intervention; no resurrection/instant healing by tag | No exact SCL family assigned; hold |

## Part V — Operational interfaces (military residual content, not duplicate Core rules)

### 12. Model / issued kit / actual instance
**Model** defines supported capability under calibrated construction, environment and qualified crew. **Issue-kit template** lists required items and authorized roles; it is not a starting inventory and has no quantitative entitlement unless a real service policy grants it. **Loadout** is a derived view of actual assets, finite ammunition, supplies, armor, carried load, operator capacity and access at a specified time. **Instance** is a campaign-owned real thing. **Condition and availability** are not quality or possession.

### 13. Service issue and accountability adapter
The Soldier/Military Slim source separates enrollment, assignment, pay, custody, requisition, issue and return. Military content provides required records: `service profile | approved model/variant | required credential | item/lot | requested/authorized/reserved/allocated/dispatch/received/issued/returned/lost | owner | custodian | restrictions | maintenance | receipt event`. These are stage links to authoritative Core records, not a second inventory or independent Military treasury. Stock reservation is not consumption; an approval is not delivery; missing status is not proof of physical loss. If a player character faces a discretionary decision (purchase, acceptance, voluntary reassignment), return control.

### 14. Crew station and integrated-system adapter
A crewed weapon or platform has station definitions `role | authorization | competence | presence | attention/time | controls | applicable subsystem | power/feed | shared operating window | limits | relief`. Concurrent operation is limited by real stations, tasks, visibility, controls and finite resources. A commander can order but cannot personally operate all stations unless actually qualified and available. One actuator cannot fire twice merely because two roles reference it. A disabled sensor does not automatically destroy the propulsion chain.

### 15. Ammunition and operating resource adapter
The specific model binds `weapon mode ↔ chamber/feed/launcher ↔ compatible lot ↔ actual loaded/ready/reserve/recoverable states`. Define type, mass/count, packaging, suitability/condition, maximum local service capacity, feed availability, safety gates and emitted effects. A firearm or gun remains unusable for a particular firing method when ammunition or another essential part is unavailable; a roll cannot substitute for it. Blocked activations do not consume charges unless an actual attempt had a declared consuming stage. Post-use ejected cases, gases, spent power/heat and debris follow their own established physics/stock events, where relevant.

### 16. Load/transport/supply and service-life requirements
`Task | interval | actor/crew | permitted means | actual asset + condition | supplies | route/network | supporting services | service limits | reserve policy | authorized contingencies`. Readiness is a derived task-specific question, not a permanent bonus meter. Weapons need maintenance and compatible spares; armor and clothing wear, vehicles use finite fuel/parts, rations deplete, mounts need food/rest/care. Sustained service remains possible and peaceful; a successful mission does not force stronger opposition.

### 17. Communications, observation, fire-control separation
Observation event → recorded estimate/belief → interpretation/classification → transmission → receipt → authorized action. Each requires real sensors/observers, line-of-effect or propagation channel, processing and an as-of timestamp. Command, spotting, sensor tracking and physical engagement are separate prerequisites. Poor communication does not magically move the target or create unrelated catastrophe. Science-fiction communication has no automatic instantaneous propagation or perfect bandwidth.

### 18. Specialized platform interface routing
| Effect/operation | Owner/required interface | Military-local content |
| --- | --- | --- |
| Object condition/configuration/location | K-ASSET | Military selects component, allowed station and doctrine roles; no duplicate asset |
| Stock/amount/consumption/transit | K-STOCK | Military selects lots, compatibility, magazine and issue policy; one ledger |
| People/qualification/condition | K-ACTOR / LIFE / MED | Military records assignment and role restrictions; no second person or injury |
| Organization/command/credentials | K-ORG / GOV | Military identifies native chain of command, issue and task authority |
| Time/work/repair/acceptance | K-TIME / K-WORK | Military supplies operating, maintenance, training scope; same clock |
| Information/observation/receipt | K-INFO | Military provides signal codes, sensors, orders and reporting procedures |
| Transport/link/service networks | K-NET | Military supplies routes, comm channels, magazines/feeds, physical envelope |
| Household/pay/claims | LIFE / ECO | Military provides service terms, pay/issue policy, no new treasury |
| Operations/casualties/formation | Core operations / K-POP residual cohorts | Military provides tactics, stations, roster; no duplicate casualty ledger |
| Naval craft | MAR specialization (when adopted) | Ship handling/naval physics and vessel operating envelopes |
| Spacecraft | SPACE specialization (when adopted) | Orbital flight/pressure/thermal/communications envelopes |
| Aircraft | Aviation specialization (when defined) | Aerodynamic/control/flight performance and applicable service |
| Supernatural/fictional technology | Selected setting/genre module | Power sources, extraordinary physics, constraints and actual access |
| Equipment family/era/category | SCL-1.0 reference registry; MIL-LIB specialization | Read-only identities, overlays and eligibility; never physical instances |

### 19. Installation, fielding, withdrawal, return
`Prototype → accepted type → authorized procurement → delivery → installation → inspected/commissioned → staffed/qualified → operated within envelope → maintained → withdrawn/repaired → returned/replaced`. These are possible distinct stages, not a mandatory new queue with its own second Core clock. Military doctrine approval and instruction rollout remain institutional decisions and real communications/training/issue processes; an approved weapon model does not upgrade every unit at once. A destroyed gun, spent ammunition, stolen property or retired vessel preserves its causal history and records.

### 20. Model-family uncertainty and numerical calibration gate
If a parameter is outcome-changing—effective range, lethality/protection channel, ammunition rate, mobility, lift, endurance, repair time, reliability, medical efficacy, environmental exposure, mass/carry or throughput—specify `unit | quantity/qualitative bracket | measurement/model | applicability | bounded range | assumptions | source & status | uncertainties | extreme/failure cases`. No baseline number is adopted here because the source is an index. Unknown values block *only* decisions dependent on that precision. Ordinary known work proceeds and still consumes real time/resources. Historical assertions require local period/region research and are not guaranteed merely by naming an era.

## Part VI — Genre/setting and campaign manifest

### 21. Required campaign selections
```text
core_ref: IRGS-CORE-3.2 (only after explicit compatibility/adoption)
scl_ref: IRGS-SCL-1.0
scl_identity_revision: 0.2
military_library: IRGS-MIL-LIB-1.0 (proposed; adopted status separately)
military_life_engine: MLS-SLIM-1.0 (currently pinned to CORE-3.0/SCL-0.1)
bridge: exact version + reconciled owner/procedure/trigger crosswalk; status
era_facet: ERA-ANT | ERA-EAD | ERA-MED | ERA-EMD | ERA-CON | ERA-SCI
setting_region_date: actual local evidence; allow mixed-technology inventories
institution: ID; service terms; issue doctrine; qualifications; chain; supply policy
branch: land/naval/air/space/other; activated specialist module, if any
selected_records: exact SCL refs, selector, MIL template, local variant, adapter
resolution_and_effects: complete compatible model(s), scoped status, units
operations: actor/asset/stocks/services/knowledge owner references
medical_and_recovery: selected physiological/condition profile
work_and_acceptance: test/safety/maintenance/commissioning requirements
readiness: unresolved profiles and independent possible actions
adoption_scope: who/where/effective time; pre-existing campaign overrides
validation: structural; scripted; bounded simulation; live play; calibration status separately
```

### 22. Era-bound deployment examples (illustrative, not initialized)
**Medieval garrison:** Select `ERA-MED`, dated place and an actual fortress/castle profile. A mailed guard and crossbowman can use shared armor/weapon construction families only with a complete compatible historical/fantasy mode adapter. A crossbow is not loaded with arrows by generic label. Watch, pay, fatigue, food, repairs and unit command flow through the selected life engine and Core owners. No starting inventory appears merely from the category list.

**Early-modern gun crew:** Select `ERA-EMD`, local artillery technology, trained crew, gun, carriage, powder/shot lots, emplacement, weather and timing. The artillery template requires a site-specific operating/effect model; loading, laying, firing and reloading are actual actions constrained by resources. No default cannon range or ammunition quantity is created.

**Contemporary vehicle section:** Select `ERA-CON`, exact time/region, vehicle type, issued communications, ammunition/fuel lots, crew assignments and maintenance capacity. Engine, sensors, armament and radios have independent failures and shared platform requirements. Readiness for a transport run is not interchangeable with readiness for a combat patrol.

**Science-fiction Mech or orbital crew:** Select `ERA-SCI`, an explicit setting/module for reactor, actuation, weapons, command/AI, aviation/space movement and environmental survivability. A setting can preserve legacy projectile arms, deny FTL, use delayed communication and impose finite ammunition/heat without inheriting fantasy stats. Link strain/synchronization belongs to a specifically selected specialty module and cannot automatically be applied to ordinary historical soldiers.

## Part VII — Acceptance and stress tests

The following cases are **specifications**, not claims of live-play results. The accompanying CSV maps one expected result per case. The packaged verifier independently runs bounded reference/structural checks for IDs, matrix coverage, source and crosswalk validity; it does not execute the complete IRGS runtime or certify performance numbers.

| ID | Case | Required result |
| --- | --- | --- |
| MIL-01 | Six era labels survive unchanged | Exactly ERA-ANT/EAD/MED/EMD/CON/SCI |
| MIL-02 | Twelve categories survive unchanged | Exactly WPN/PRO/SUP/MUN/KIT/TRN/NAV/AIR/COM/OBS/ENG/MED |
| MIL-03 | Every era-category cell covered | Exactly 72 indexed pairs; no duplicate pair |
| MIL-04 | Old source has no weapon numbers | No new range/damage/penetration assigned from source index |
| MIL-05 | Modern tag on historical setting | Not available without date/region/institution evidence |
| MIL-06 | Old sword persists into future setting | Age is no automatic retirement; local availability determines |
| MIL-07 | Select identical physical sword in 2 attack modes | One asset, two compatible modes, no doubled sword count |
| MIL-08 | Firearm equipped without ammunition | Cannot fire with missing compatible ammo/feed |
| MIL-09 | Cross-era cartridge mismatch | Reject unsupported firing; do not consume incompatible cartridge |
| MIL-10 | Fire one projectile then recover | Debit ready stock or move projectile once; recovery conditional on actual find/condition |
| MIL-11 | Weapon mode selected without parent object | No equipped weapon materializes |
| MIL-12 | Issue recorded as approved but not delivered | No inventory custody or carried mass change |
| MIL-13 | Issue under valid authority and received | Transfer same physical asset once; preserve institution ownership |
| MIL-14 | Duplicate issue event replay | No second asset, ammo or custody transfer |
| MIL-15 | Lost item becomes a report | Physical loss recorded once; report is knowledge not another debit |

| ID | Case | Required result |
| --- | --- | --- |
| MIL-16 | Qualification exists without assignment | Actor has qualification, not automatic weapon or duty slot |
| MIL-17 | Rank increases without training | No skill improvement, repair or equipment issue implied |
| MIL-18 | Uncrewed support gun used | No operation when required crew stations unavailable |
| MIL-19 | Two crew operate one station | No duplicate gun cycle or free extra attack |
| MIL-20 | Crew uses a source Fantasy damage value in modern campaign | Block absent complete compatible adapter |
| MIL-21 | Armor made of multiple layers | Count each physical layer/effect once using compatible protection model |
| MIL-22 | Environmental suit has armor | Armor does not create oxygen/heat/radiation protection without channels |
| MIL-23 | Don respirator without filter or seal | Unsupported exposure protection cannot be assumed |
| MIL-24 | Powered armor out of energy | No assisted functions where source unavailable; passive elements assessed separately |
| MIL-25 | Transport platform with no route or qualified crew | No journey from a catalogue lookup |
| MIL-26 | Cargo authorized but aboard/in transit | Origin, transit and destination not counted as three stocks |
| MIL-27 | Mount with tack gets fatigued | Animal physiology and cargo persist; tack not a second animal |
| MIL-28 | Naval ship listed but no marine model | Cannot calculate propulsion/docking from generic vessel family |
| MIL-29 | Sci-fi spacecraft without SPACE profile | No FTL, propulsion, docking or pressure envelope invented |
| MIL-30 | Command sent by courier without receipt | Recipient lacks command until actual channel receipt |

| ID | Case | Required result |
| --- | --- | --- |
| MIL-31 | Radio detected a contact | Detection does not establish classification or exact location |
| MIL-32 | Report received after physical casualty | Casualty remains one actual event; delayed knowledge updated separately |
| MIL-33 | Workshop and base both list same lathe | One physical lathe and one competing work capacity |
| MIL-34 | Generator is on but downstream line disconnected | Fuel use may occur; downstream service cannot be assumed |
| MIL-35 | Field kitchen lists ration and meals | Consumption counted once; meal does not multiply underlying food |
| MIL-36 | Medical kit present without provider | No automatic healing, triage or surgery |
| MIL-37 | Bed present with no clinical staff | Bed availability != medical throughput |
| MIL-38 | Repair completed but lacks acceptance test | Equipment condition/provision and readiness not automatically restored |
| MIL-39 | Ammo storage disrupted | Only actual stocks, conditions, locations and supported hazards affected |
| MIL-40 | Training introduces improved doctrine | No rollout without approval/instruction/equipment receipt |
| MIL-41 | Loadout has issued and owned copies | Two actual items if truly distinct; no conflated owner |
| MIL-42 | Unit shifts from detailed combat to aggregate | No replenished ammo, people, equipment condition, or repeated injuries |
| MIL-43 | Two orders demand same gun simultaneously | One valid resource allocation; conflict resolved under Core |
| MIL-44 | Undeclared science-fiction autonomous combat system | No independent omniscient AI actions |
| MIL-45 | Historical technology unavailable locally | Entry remains candidate, deployment disallowed until eligibility |

| ID | Case | Required result |
| --- | --- | --- |
| MIL-46 | Military slim engine pin is Core 3.0 | No automatic rebinding to Core 3.2 without complete bridge/adoption |
| MIL-47 | SCL v1.0 releases an @0.2 family | Immutable @0.2 content identity and selectors retained |
| MIL-48 | Existing campaign loads proposed library | No automatic inventory, pay, command, casualty, legal or progression changes |
| MIL-49 | Narrator reports offscreen repair | Work occurred only if real actor/means/time/support and accepted result |
| MIL-50 | Failure of limited radio message | No automatic unrelated crash/casualty; only feasible failure effects |
| MIL-51 | Deploy with unknown missile engagement envelope | Defer only dependent quantitative engagement; other actions proceed |
| MIL-52 | Transfer ammunition to magazine | Debit storage and credit magazine; no consumed shot yet |
| MIL-53 | Ammo loaded, fired and casing ejected | Spent components persist/leave according to specific profile; no duplicate debit |
| MIL-54 | Crew casualty disables station | Recompute linked capability only; other stations remain per actual configuration |
| MIL-55 | Issue standard kit selection | Template spawns no goods until actual approved issue and delivery event |
| MIL-56 | Military competition with marksmanship event | Core competition owns eligibility/results; weapon method owns performance |
| MIL-57 | Long-term service without battle | Ordinary duty, training, pay, family and retirement remain playable |
| MIL-58 | Ambiguous era boundary | Region/date evidence prevails over era tag; do not impose cross-cultural inevitability |
| MIL-59 | Partial equipment specification | Explicit unknown not overwritten by legacy Fantasy or zero/default |
| MIL-60 | Replayed event at different scale | Same event ID and write-set prevents repeated cost or physical result |

### 23. Runtime qualification matrix
A genre deployment must execute the relevant cases using its actual state records, time/commitment model, authoritative ledgers, simultaneous operations, interference, scale shifts and cross-module dependencies. Additional checks must include scarcity, maintenance loss, failure/Mixed results, repeated attempts, invalid/duplicate event payloads, human/animal requirements, legal authority, medical consequences and success without escalating encounters. Scripted cases or synthetic fixtures are not live playtests; consistency does not establish realism or balance.

## Part VIII — CMRR register and migration

### 24. Source-by-source disposition
| Source | Content/function | Decision | Preservation / reason |
| --- | --- | --- | --- |
| ML-0.1 §1 | Six eras | Retain through SCL tags and MIL browse | All six IDs, labels and scope language kept |
| ML-0.1 §2 | Twelve categories | Retain through SCL and Military facets | All twelve codes and descriptions kept |
| ML-0.1 §§3–5 | Family index by historical period | Reorganize into 72 cells | Examples preserved as historically contingent candidate families; MUN derived separately |
| ML-0.1 §6 | Later expansion sequence | Retain/revise | Era→region/date→branch→family→specific model preserved plus exact SCL/adapter and ownership |
| ML-0.1 §7 | Historical source/research basis | Preserve as source bibliography in provenance | Does not certify every locally dated item or quantitative model |
| SCL-1.0 §23 | Era/category tags | Inherit | Do not create duplicate global tag authority |
| SCL-1.0 §§24–26 | Shared asset/adapter/genre interface | Inherit with specific military specialization | No duplicate family stats or owners |
| SCL-1.0 registry | 279 family records, aliases, source payloads | Reference only; do not modify | Retain checksum-bound @0.2 family references and holds |
| MLS-SLIM-1.0 §§1–17 | Military-life workflows and 30 cases | Preserve via source/bridge; do not rewrite | Uses service, command, leave, issue, household/career controls; pinned 3.0 needs prospective bridge |
| FANTASY-LIB-2.0 | Fantasy native equipment methods | Comparison only | No conversion of Fantasy numerical values into historical/modern defaults |
| This v1.0 | 48 military specialization templates / 60 cases | New proposed content | Enable individually with source- and setting-calibrated adapters; no state created |

### 25. Reject or hold
Reject: `era tag ⇒ local item available`, `military category ⇒ combat performance`, `source Fantasy numerical adapter ⇒ military mechanical truth`, `requested or reserved property ⇒ issued`, `station template ⇒ additional gun/action`, `hospital bed ⇒ treatment`, `naval/air/space tag ⇒ movement physics`, `AI label ⇒ unrestricted agency`, and `qualification ⇒ experience/authority/complete duty`. Hold all specific unproven model parameters, unverified historical claims and any proposed new template lacking its actual supporting content/model. These exclusions are not losses of adopted functions.

### 26. Controlled migration and retirement of the previous index
**Before:** pin old Core/MLS/SCL profiles and existing campaign snapshot. **Compare:** identify every old `ERA`/category/name and any actual asset item; map catalogue metadata without changing instance or source-stat identity. **Merge:** use new military templates only as reference overlays; keep exact `SCL` family ref/selector and historical source payload. **Reconcile:** test qualification, institutional eligibility, operating model and resource ownership; if a parameter changes an outcome, record approval and effective time. **Resubmit:** explicit adoption/bridge statement, version pin, resolved dependency matrix, source-to-new crosswalk, observed regression evidence. No saved campaign inventories, wages, injuries, duty time, unit headcounts or historical events are retroactively rebuilt. Adoption does not delete original provenance.

### 27. Version, provenance, status and open questions
This candidate is derived from `ML-0.1` (11 October 2026) and `MLS-SLIM-1.0` (13 October 2026), checked against active Core 3.2 / SCL 1.0 references (14 October 2026) and analogous Fantasy library formatting. The template IDs are new, proposed and do not replace the normative SCL catalogue. No complete Core 3.0→3.2 Soldier/Military behavioral bridge is claimed. **Calibration:** individual historical models, ammunition/cartridge compatibility, weapon effects, armor channels, vehicle/ship/air/space operating envelopes, power/communications, care, service capacity, prices/mass/dates, and issue/legal procedure all remain local. **Tests:** see companion report for executed structural checks; individual behavior cases are specified.

**Unresolved decisions:** Which service/branch technology profiles are first to be selected? Which campaigns use a historical-only versus multi-era/fictional catalogue? Which saved Soldier/Military engine deployment is pinned to Core 3.0, and who authorizes the Core 3.2 compatibility bridge? Which source-backed SCL holds require new immutable family revisions before deprecation? These do not block catalogue browsing and content authoring, but they do block affected quantitative or automatic deployment.

**Change summary:** Preserved original tags and all source category scope; organized 72 era/category selection slots; added 48 proposed native military templates and 60 acceptance specifications; linked exact existing shared IDs; kept item/mode/stock/authority distinct; flagged the Soldier/Military Slim parent mismatch; added qualification, continuity, compatibility and source-status contracts. No Core/SCL normative file, campaign ledger or adopted military rule was changed.
