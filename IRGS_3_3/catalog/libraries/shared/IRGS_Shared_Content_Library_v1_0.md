# IRGS — Shared Content Library
## Version 1.0 — Current catalogue for Core 3.2

**Document ID:** `IRGS-SCL-1.0`  
**Parent rules:** [IRGS Core 3.2](IRGS_Core_Engine_v3_2.md), especially §§111–112.  
**Status:** Current workshop catalogue. Record readiness, native source status, model calibration and campaign adoption remain separate.  
**Normative registry:** [IRGS_Shared_Content_Registry_v1_0.json](IRGS_Shared_Content_Registry_v1_0.json).  
**Qualitative contracts:** [IRGS_SCL_v1_0_Selected_Contracts.md](IRGS_SCL_v1_0_Selected_Contracts.md).  
**Exact reference map:** [IRGS_SCL_v1_0_Reference_Map.csv](IRGS_SCL_v1_0_Reference_Map.csv).  
**Provider bindings:** [IRGS_Engine_Bindings_v3_2.json](IRGS_Engine_Bindings_v3_2.json).

The library owns reusable descriptions, exact identity, selectors and functional content contracts. Core owns actors, events, time, actual assets, stocks, work, information, institutions and continuity. A library lookup creates no quantity, object, action, authority, skill, service or campaign fact.

### 1. Scope and records

The current registry contains **279 content families**, **1,416 exact aliases**, **304 source references**, **51 complete selected qualitative contracts**, **228 held families**, **235 source-backed reference holds**, **18 scoped extensions**, **61 Fantasy adapter records**, and **420 content/adapter payload blocks**. There are **286 neutral source rows** and **22 non-instantiating weapon-parent relationships**. These counts describe different units.

The 420 payload blocks are the source-qualified entry data and rule fragments needed to preserve content and native adapters. They are current reference data with their source scope; their inclusion does not override Core 3.2 or promote an incomplete entry. The package carries no copies of former Core or library editions.

### 2. Identity and composition

Catalogue release **1.0** and individual record revision **0.2** are separate. Canonical family references remain `SCL:<stable PBC family>@0.2`. Their exact published aliases preserve namespaces, source revision, semantic type, selector and target checksum. Loading a later catalogue does not synthesize new `@1.0` content aliases.

Sword cut and thrust select `modes.cut` and `modes.thrust` on one sword family. The 22 weapon-parent relations describe those existing families; they create no second asset or inventory stock. Unarmed actions and coverage descriptors remain non-inventory methods and geometry. Typed reader-view proposals retained in the reference map are noncanonical and must not resolve as published aliases.

Each definition retains its exact reference, type, provenance, readiness/activation gate, owners, allowed selectors, source fields and selected contract where one exists. Unknown, zero, missing and inapplicable keep their different meanings. Readiness does not establish setting availability or present ownership.

### 3. Lookup and activation

Resolve exact reference and selector → check family/type/checksum → check readiness → select a complete compatible native adapter → check setting eligibility and necessary calibration → bind actual state and access → execute through Core's existing owners.

A held family may use only its preserved source-backed definition and a compatible explicitly selected native profile. It cannot impersonate a completed shared replacement. Missing numerical parameters block dependent effects; they do not create a favorable default. Physical initialization and production require their own Core authorization, time, inputs and event commit.

### 4. Conditions and facets

Quality, condition, maintenance, repair, coverage, possession and reproduction remain distinct. A workshop, its equipment and delivered work may be facets of one installation; stock, staff, station-hours and completed work are each counted once. A cold-storage installation requires actual storage, power, compatible operation and a selected temperature model. A generator needs actual fuel, safe operation and compatible links before downstream service exists.

Physical documentation can be transferred as an asset. Its information must still be accessed, received, interpreted and learned through the appropriate actors; a manual does not confer expertise or authority. An integrated armor definition supplies its selected protection once; component descriptions do not add whole independent protection profiles.

### 5. Source scope and authority

`FL`, `PL`, military era/category metadata and other native namespaces identify exact source-qualified content. Source mechanical labels and numerical values retain their native profile scope. Core 3.2's shared procedure and ownership contracts govern this package; a source fragment does not revive a competing shared runtime. Genre and setting-specific rules require their own declared compatible selection.

### 6. Validation and overrides

The manifest records fresh structural and bounded reference checks. The acceptance tables below are requirements unless their execution is separately recorded. Numerical realism, balance, calibration, full domain implementation and live campaign playtesting are distinct. Publication enables no automatic campaign migration, source deprecation or held-content promotion.

# PART II — SHARED MATERIALS, STOCKS AND STORAGE

## 7. Material families

`MAT` describes substances and their qualitative properties: density, hardness, toughness, flexibility, workability, heat and moisture behavior, corrosion/rot, repairability and compatibility. This table **does not** provide armor ratings, weapon damage bonuses, or an automatic technological era. `RES-CON-001` (a structural timber stock lot) may use `MAT-001` or `MAT-002` (its material). These are **not duplicates**.


### 7.1 Baseline material catalogue

Material variants pin grade/specification and physical provenance before numeric use. Source: `FA-LIB` §20.

| ID | Material family | Source-supported qualitative behaviour |
|---|---|---|
| MAT-001 | Softwood | light, workable, moderate structural performance, vulnerable to sustained moisture/fire |
| MAT-002 | Hardwood | stronger structural baseline, heavier/harder to work |
| MAT-003 | Hide/rawhide | flexible, light, moisture-sensitive |
| MAT-004 | Leather | flexible protective and binding material |
| MAT-005 | Bone/horn | light rigid biological material; useful in small structural/edge components |
| MAT-006 | Stone | hard, heavy, low flexibility, potentially brittle |
| MAT-007 | Bronze-family metal | workable cast metal; good corrosion behavior; weapon/armor performance depends on construction |
| MAT-008 | Iron-family metal | strong general structural metal; quality varies substantially |
| MAT-009 | Steel-family metal | baseline high-performance mundane weapon/armor metal |
| MAT-010 | Hardened high-quality steel | difficult manufacture; improved structural/edge performance where design supports it |
| MAT-011 | Glass/crystal | hard, potentially sharp, normally brittle unless setting changes its material behavior |
| MAT-012 | Ceramic | heat-resistant/hard applications; brittleness must be considered |
| MAT-013 | Textile | flexible; protection depends strongly on layering and construction |


## 8. Stock and commodity families

The following `RES` rows become engine-neutral stock *types*, not PA-only survival currency. The exact substance, grade, unit, compatibility, holder, usable state and quantity belong to setting/campaign records. Documentation `RES-KNW` is a **physical/digital medium reference with informational content**, never a second mutable knowledge ledger; Core's information owners remain authoritative. Food categories describe preservation behaviour, not nutritional equivalence. Source: `PA-LIB` §§8–10.


### 8.1 Standard commodity families

Requirements are boundary fields, not guaranteed stocks.

| ID | Resource / stock family | Neutral function and typical unit | Storage / usability / critical boundary |
|---|---|---|---|
| RES-WAT-001 | Potable Water | Water meeting the campaign’s potable standard; unit: Volume | Safe containment; contamination control; Becomes non-potable if contaminated; quantity may remain unchanged |
| RES-WAT-002 | Untreated Fresh Water | Raw water requiring assessment/treatment before potable use; unit: Volume | Source/container appropriate to raw water; Not automatically drinkable; treatment depends on actual contaminants |
| RES-FOOD-001 | Shelf-Stable Food | Prepared food with comparatively low short-term preservation dependency; unit: Mass/servings/energy unit selected by profile | Dry/protected storage as specified; Shelf life and nutrition remain profile-specific |
| RES-FOOD-002 | Perishable Food | Food whose usable condition materially depends on time/temperature/storage; unit: Mass/servings | Cold chain or other preservation as specified; Loss follows actual storage exposure, not arbitrary scene rolls |
| RES-FOOD-003 | Raw Agricultural Produce | Harvested but not necessarily preserved agricultural output; unit: Mass/volume | Crop-specific handling and storage; Harvested crop is distinct from planted crop and seed stock |
| RES-AGR-001 | Seed/Propagation Stock | Planting material capable of producing future crops where viable; unit: Mass/count | Species-specific preservation; Not interchangeable with ordinary food merely because edible |
| RES-MED-001 | Medical Consumables | Single-use or depleting care materials; unit: Count/mass/kit units | Clean/dry/sterile conditions as relevant; Possession does not create practitioner competence |
| RES-MED-002 | Pharmaceutical Stock | Specific medication or drug family; unit: Dose/count/volume | Drug-specific storage; No generic “medicine points”; identity, dose, shelf life, and contraindications remain specific |
| RES-SAN-001 | Sanitation/Hygiene Consumables | Soap, cleaning agents, sanitary products, and similar consumables; unit: Count/mass/volume | Product-specific storage; Does not replace water or waste-disposal service |
| RES-CHEM-001 | Treatment/Process Chemical | Specific chemical input used by water, sanitation, industry, agriculture, or medicine; unit: Mass/volume | Chemical-specific containment; Chemicals are not interchangeable; hazards require profile |
| RES-FUEL-001 | Gasoline-Family Fuel | Liquid spark-ignition fuel family; unit: Volume/mass | Compatible sealed fuel storage; Grade, degradation, fire risk, and compatibility require profile |
| RES-FUEL-002 | Diesel-Family Fuel | Liquid compression-ignition fuel family; unit: Volume/mass | Compatible sealed fuel storage; Not interchangeable with gasoline without explicit equipment capability |
| RES-FUEL-003 | Gaseous Fuel | Propane/natural-gas/other stored or piped fuel variant; unit: Mass/volume/energy unit | Pressure-rated or network storage; Specific gas, pressure, fittings, and leakage behavior must be defined |
| RES-FUEL-004 | Solid Fuel | Wood, coal, charcoal, biomass, or setting variant; unit: Mass/volume | Dry/protected storage as relevant; Collection/processing and emissions remain specific |
| RES-FLUID-001 | Lubricants and Service Fluids | Equipment-specific oils, coolants, hydraulic fluids, etc.; unit: Volume/mass | Product-specific storage; No universal service-fluid substitute |
| RES-CON-001 | Structural Timber | Processed wood suitable for specified construction; unit: Length/volume/mass | Dry/protected as needed; Grade, dimension, treatment, and structural use must match project |
| RES-CON-002 | Structural Metal Stock | Steel/aluminum/other structural material; unit: Mass/length | Corrosion/protection as relevant; Composition and section matter where load-bearing |
| RES-CON-003 | Fasteners and Joining Supplies | Nails, screws, bolts, wire, adhesives, welding consumables, etc.; unit: Count/mass | Dry/secure as needed; Compatibility and tooling matter |
| RES-IND-001 | Compatible Spare Parts | Named replacement part or compatible component family; unit: Count | Part-specific storage; “Spare parts” is not a universal pool; specify compatibility |
| RES-IND-002 | Electrical/Electronic Components | Specific wiring, controls, breakers, boards, sensors, etc.; unit: Count/length | Dry/ESD/environmental controls where relevant; Technology level and compatibility matter |
| RES-IND-003 | Plumbing/Fluid Components | Pipe, fittings, valves, seals, pumps/components; unit: Count/length | Material-specific storage; Diameter, pressure, material, and fittings matter |
| RES-SCRAP-001 | Mixed Salvage/Scrap | Unsorted recoverable material; unit: Mass/volume | Safe containment if hazardous; Not equivalent to finished stock until processed |
| RES-KNW-001 | Technical Documentation | Manuals, drawings, procedures, specifications; unit: Document set | Physical/digital preservation and access; Information is not practical competence |
| RES-KNW-002 | Maps and Civic/Property Records | Geographic, ownership, infrastructure, or administrative information; unit: Document set | Preservation/access; Age, completeness, and authority matter |


## 9. Containers and storage archetypes

A container is its own asset, with actual contents referenced as separate stocks. Storage condition can preserve or degrade usability through a declared process; capacity is not inventory and a label is not a compatibility certificate. Source: `PA-LIB` §§11–12.


### 9.1 Standard container and storage types

Use product-specific container material, closure, hygiene, power and compatibility in the selected profile.

| ID | Storage type | Function | Calibrate / failure boundary |
|---|---|---|---|
| STO-001 | Portable General Container | Portable storage for compatible dry goods | Capacity, closure, weather protection, handles/loadability; Mass/bulk and content compatibility |
| STO-002 | Portable Water Container | Portable liquid-water storage | Food/water-safe interior, seal, pour/transfer interface; Cleaning and contamination state matter |
| STO-003 | Bulk Water Tank/Cistern | Stationary or vehicle-mounted bulk water storage | Capacity, material, inlet/outlet, venting, access; Tank volume is not potable reserve if contents are unsafe |
| STO-004 | Fuel Container/Tank | Storage for a specific compatible fuel | Fuel type, capacity, venting, transfer interface, fire/environmental protection; Do not mix incompatible fuels or assume a pump exists |
| STO-005 | Dry-Goods Store | Protected bulk storage for food/materials | Weather/pest control, shelving/pallet access, security; Stored capacity and actual stock are separate |
| STO-006 | Cold Storage | Temperature-controlled storage | Usable volume, temperature range, power/thermal buffer, doors, monitoring; Losing power starts a causal temperature problem; it does not instantly destroy all contents |
| STO-007 | Secure Medical Store | Controlled storage for sensitive medical stocks | Security, cleanliness, environmental requirements, inventory control; Access authority and practitioner use remain separate |
| STO-008 | Hazardous-Material Store | Containment for hazardous chemicals/fuels/waste | Segregation, ventilation, secondary containment, PPE/access; Hazard profile required |
| STO-009 | Bulk Material Yard | Open/covered storage for construction/scrap material | Area, loading access, drainage/weather protection as needed; Possession does not imply handling equipment |


---

# PART III — OBJECTS, EQUIPMENT, WEAPONS AND PROTECTION

## 10. Ordinary equipment and utility archetypes

The following definitions are useful in domestic, military, disaster, fantasy, historical, industrial, space and other campaigns **when that technology exists and the item is selected**. A generator is not available to an ancient Roman because its archetype is listed. Mechanical output, cycle rate, fuel quality, parts, endurance, coverage and human/operator requirements are profile data. Source: `PA-LIB` §§13–14.


### 10.1 Equipment and facility equipment

A workshop (a facility asset) is distinct from a manufacturing service and from its operators.

| ID | Equipment / archetype | Function | Required profile and limits |
|---|---|---|---|
| EQP-WAT-001 | Portable Water Filter/Purifier | Processes a defined input-water range toward a defined output standard | Input-water compatibility; throughput; power/consumables; replacement media; operator procedure; Cannot remove contaminants outside its profile |
| EQP-WAT-002 | Manual Water Pump | Moves compatible liquid through human mechanical input | Lift/head; flow; hose/fitting compatibility; operator effort; No automatic treatment or purification |
| EQP-WAT-003 | Powered Water Pump | Moves compatible liquid using electrical/fuel/mechanical power | Power; flow/head; priming; fittings; operator/maintenance; Power and pumping do not establish potability |
| EQP-PWR-001 | Portable Combustion Generator | Produces electrical power from a compatible fuel | Rated/usable output; fuel type/rate; startup; exhaust; maintenance; connectors; Fuel stock, safe exhaust, and wiring are separate requirements |
| EQP-PWR-002 | Battery Storage Bank | Stores electrical energy and supplies power within defined discharge limits | Energy capacity; output; charging; chemistry; temperature; cycle/maintenance; Energy capacity and instantaneous power are distinct |
| EQP-PWR-003 | Solar Photovoltaic Array | Produces electrical energy under suitable environmental conditions | Area/rated output; sunlight profile; controller; wiring; storage interface; Renewable source does not guarantee continuous service without storage/distribution |
| EQP-PWR-004 | Portable Electrical Distribution Kit | Routes generated power to compatible loads | Voltage/current/connectors; protection; cable length; load limit; Generator ownership does not create usable distribution |
| EQP-COM-001 | Portable Two-Way Radio | Provides local/remote voice/data communications within its profile | Frequency/system; range conditions; power; antenna; encryption/compatibility; Range and interoperability depend on terrain, network, and configuration |
| EQP-COM-002 | Radio Repeater/Relay | Extends compatible communications coverage | Power; location; frequencies; antenna; operator/maintenance; Coverage is geographic and system-specific |
| EQP-TEMP-001 | Portable Heater | Provides local heat | Fuel/power; output; ventilation; safety; maintenance; Heat source does not guarantee whole-building safe temperature |
| EQP-TEMP-002 | Portable Cooling/Ventilation Unit | Provides local cooling/air movement | Power; capacity; environmental range; ventilation path; Cannot exceed physical/environmental limits |
| EQP-COLD-001 | Portable Refrigeration Unit | Maintains defined cold storage when adequately powered | Usable volume; temperature; power; startup; thermal behavior; Contents have their own temperature exposure history |
| EQP-TOOL-001 | General Hand-Tool Kit | Supports ordinary mechanical/construction tasks within included tools | Tool list/coverage; condition; portability; Does not substitute for specialist tooling or competence |
| EQP-TOOL-002 | Electrical/Electronic Tool Kit | Supports electrical diagnosis/repair within technology scope | Meters; hand tools; test equipment; safety gear; Tools do not provide documentation or competence |
| EQP-TOOL-003 | Plumbing/Fluid-System Tool Kit | Supports pipe/fitting/pump service within size/material scope | Cutting/joining tools; test equipment; seals; Compatibility and replacement parts remain necessary |
| EQP-SHOP-001 | General Repair Workshop | Provides workspace/tooling for defined repair/fabrication scope | Tools; machines; power; ventilation; consumables; staff; capacity; Workshop scope must name what it can and cannot repair/fabricate |
| EQP-HND-001 | Manual Material-Handling Set | Pallet jacks, dollies, hoists, slings, ramps or campaign variant | Load limits; geometry; operators; surfaces; Handling capability is not transport capacity |
| EQP-HND-002 | Powered Forklift/Loader | Moves/loads compatible cargo | Rated load; fuel/power; terrain; attachments; operator; maintenance; Cannot move cargo beyond access/geometry/load limits |
| EQP-AGR-001 | Agricultural Hand-Tool Set | Supports manual cultivation/harvest tasks | Tool coverage; labor; maintenance; Does not create land, seed, water, or yield |
| EQP-MED-001 | Field Medical Kit | Carries defined medical consumables/equipment for specified care scope | Contents; sterility; practitioner requirements; replenishment; No universal healing value |
| EQP-SAN-001 | Portable Sanitation Unit | Provides temporary waste containment/treatment function | Capacity; consumables; service interval; disposal path; Waste does not vanish when unit is full |


## 11. Engine-neutral weapon and armament catalogue

An **item** and its **use modes** differ. Multiple rows ending `A/B/C` are variants of attack method for one common parent weapon: e.g. `WPN-M-006A/B` remain two modes of the same sword; owning two mode records is *not* owning two swords. No universal damage, attack roll, penetration, reach rating, defense bonus, free attack, reload-action count or performance adjustment exists in this catalogue.

The physical mode labels and construction cues below are derived from `FA-LIB` §§5–12. The **Fantasy adapter** retains all original numerical `Threat`, `Defeat`, `Reach`, `Reload`, `Sunder`, and outcome rules. Missile/projectile ownership belongs to Core and ammunition profiles; modes never replenish projectiles.

**Qualitative weapon features**: `braced reception` (geometry supports receiving an impact), `concealable` (container/clothing dependent), `weapon-control` (binding/parrying geometry), `hooked` (catching/pulling geometry), `minimum-clearance` (requires space), `two-hand primary use`, `versatile grip/mode`, `mounted-use geometry`, `object stressing` (possible material stressing), `reloading required`, `recoverable` (only if physical recovery succeeds). These are tags for later adapter rules, *not modifiers in their own right*.


### 11.1 Melee objects, natural method, and attack modes

The `WPN-M-001` unarmed method is a *capability/method entry*, not an inventory weapon. Traits identify plausible physical design considerations and have no independent numerical effects.

| Legacy mode ID | Item/method parent | Object or mode | Qualitative design tag | Source |
|---|---|---|---|---|
| WPN-M-001 | WPN-M-001 | Unarmed strike | — | FA-LIB §7 |
| WPN-M-002 | WPN-M-002 | Club | impact transfer | FA-LIB §7 |
| WPN-M-003 | WPN-M-003 | Staff | weapon-control, normally two-handed | FA-LIB §7 |
| WPN-M-004A | WPN-M-004 | Dagger thrust | Concealable | FA-LIB §7 |
| WPN-M-004B | WPN-M-004 | Dagger cut | Concealable | FA-LIB §7 |
| WPN-M-005A | WPN-M-005 | Short blade cut | — | FA-LIB §7 |
| WPN-M-005B | WPN-M-005 | Short blade thrust | — | FA-LIB §7 |
| WPN-M-006A | WPN-M-006 | Sword cut | weapon-control | FA-LIB §7 |
| WPN-M-006B | WPN-M-006 | Sword thrust | weapon-control | FA-LIB §7 |
| WPN-M-007A | WPN-M-007 | Longsword cut | Versatile, weapon-control | FA-LIB §7 |
| WPN-M-007B | WPN-M-007 | Longsword thrust | Versatile | FA-LIB §7 |
| WPN-M-008A | WPN-M-008 | Great blade cut | normally two-handed, object-stressing | FA-LIB §7 |
| WPN-M-008B | WPN-M-008 | Great blade thrust | normally two-handed | FA-LIB §7 |
| WPN-M-009 | WPN-M-009 | Hand axe | hooked geometry, object-stressing | FA-LIB §7 |
| WPN-M-010 | WPN-M-010 | Battle axe | normally two-handed, object-stressing | FA-LIB §7 |
| WPN-M-011 | WPN-M-011 | Mace | impact transfer | FA-LIB §7 |
| WPN-M-012A | WPN-M-012 | Warhammer face | object-stressing | FA-LIB §7 |
| WPN-M-012B | WPN-M-012 | Warhammer pick | object-stressing | FA-LIB §7 |
| WPN-M-013 | WPN-M-013 | Spear thrust | braced reception | FA-LIB §7 |
| WPN-M-014 | WPN-M-014 | Pike thrust | braced reception, minimum-clearance, normally two-handed | FA-LIB §7 |
| WPN-M-015A | WPN-M-015 | Poleaxe edge | minimum-clearance, normally two-handed, object-stressing | FA-LIB §7 |
| WPN-M-015B | WPN-M-015 | Poleaxe spike | minimum-clearance, normally two-handed, object-stressing | FA-LIB §7 |
| WPN-M-015C | WPN-M-015 | Poleaxe hammer | minimum-clearance, normally two-handed, object-stressing | FA-LIB §7 |


### 11.2 Ranged weapons and projectiles

An ammunition or thrown-object profile must identify the *physical item* and relevant launch/flight/handling compatibility.

| Legacy mode ID | Parent | Object / mode | Design constraints | Source |
|---|---|---|---|---|
| WPN-R-001 | WPN-R-001 | Throwing knife — Pierce | Recoverable | FA-LIB §10 |
| WPN-R-002 | WPN-R-002 | Javelin — Pierce | Thrown | FA-LIB §10 |
| WPN-R-003 | WPN-R-003 | Throwing axe — Cut | object-stressing | FA-LIB §10 |
| WPN-R-004 | WPN-R-004 | Sling — Blunt | Compact | FA-LIB §10 |
| WPN-R-005 | WPN-R-005 | Shortbow — Pierce | Fast cycle | FA-LIB §10 |
| WPN-R-006 | WPN-R-006 | Warbow — Pierce | capacity prerequisite | FA-LIB §10 |
| WPN-R-007 | WPN-R-007 | Light crossbow — Pierce | Mechanical; reloading process required | FA-LIB §10 |
| WPN-R-008 | WPN-R-008 | Heavy crossbow — Pierce | normally two-handed, Mechanical; reloading process required | FA-LIB §10 |


### 11.3 Additional cross-era equipment family index

`MIL-INDEX` §2 defines stable nonstatistical **catalogue categories**. They are indexing facets, not a second list of physical possessions:

| Family tag | Catalogue scope | Shared classification boundary |
|---|---|---|
| `WPN` | Personal weapons: melee, thrown, bows, firearms, energy weapons where present | Physical family may be shared; projectile/caliber/energy interface and effect model require a tech/genre adapter |
| `PRO` | Protection, armor, shields, helmets, uniforms, suits | Function/coverage reusable; material performance, threat channels and sealing specialized |
| `SUP` | Support weapons, siege engines, artillery, crew-operated systems | Shared family only; emplacement, crew, ammunition and effect rules specialized |
| `MUN` | Projectiles, cartridges, propellants, powered cells and expendables | Compatibility and actual consumable lots mandatory; no universal ammunition |
| `KIT` | Personal/camp tools, baggage, shelters, cooking, hygiene | Ordinary equipment and contained stock distinct |
| `TRN` | Land vehicles and animal tack/transport | Vehicle capability follows components, terrain/route and actual means; animal is an actor |
| `NAV` | Boats/ships, rigging and maritime support | Hull/ship assets are shared; hydrostatics/navigation/crew procedures specialize |
| `AIR` | Balloons, aircraft and spacecraft where enabled | Flight/pressure/orbit not inferred by category membership |
| `COM` | Signals, messages, print, telegraphy, radio, digital networks | Communication hardware differs from information received, authority, and delivery |
| `OBS` | Maps, surveying, sensors and navigation aids | Observation is not interpretation or verified recovery |
| `ENG` | Agriculture, engineering, fabrication, utilities and workshops | Tools and plant do not create expertise, process inputs or accepted outputs |
| `MED` | Medical supplies, treatment equipment, care/evacuation facilities | Treatment competence and disease/injury effects belong to designated owner |

The source additionally indexes era-relevant **families**, including siege equipment, firearms, transport vessels, motors, aviation, satellite communications, mechs and fictional weapons. It supplies *no standardized performance statistics*, so no numerical profiles or model catalogue have been invented here.

## 12. Protection construction, shields and coverage

`ARM` is a **construction archetype**, not an entire fitted suit. `COV` identifies a body region covered, when applicable to the actor's anatomy. `SHD` identifies a shield design family. A head-protection component, a breastplate and an integrated harness can reference shared materials and construction; a Fantasy adapter may map them to protection channels, and another genre can use a different threat model entirely. Sources: `FA-LIB` §§13–17.


### 12.1 Armor construction families

The numerical Cut/Pierce/Impact values deliberately remain in the original Fantasy adapter. A construction neither implies coverage of a body nor creates another layer of full rated protection.

| ID | Construction | Neutral descriptive notes |
|---|---|---|
| ARM-001 | Ordinary clothing | Not meaningful armor |
| ARM-002 | Padded textile | Flexible foundation |
| ARM-003 | Soft leather | Flexible |
| ARM-004 | Hardened/reinforced leather | Rigid/flexible composite |
| ARM-005 | Mail | Strong vs cut |
| ARM-006 | Mail over padded foundation | Integrated harness |
| ARM-007 | Scale/lamellar harness | Direction/construction sensitive |
| ARM-008 | Brigandine/coat of plates | Overlapping rigid elements |
| ARM-009 | Plate component | Rigid articulated protection |
| ARM-010 | Heavy exceptional mundane plate | Requires setting justification |


### 12.2 Shields

The old Fantasy Defense and Structure values remain external. Shield coverage is determined by actual orientation, handling, size and physical configuration.

| ID | Shield family | Illustrative intended use |
|---|---|---|
| SHD-001 | Buckler | weapon-control, close defense |
| SHD-002 | Small shield | mobile personal defense |
| SHD-003 | Reinforced round/heater shield | broad mobile defense |
| SHD-004 | Large/kite shield | broad coverage |
| SHD-005 | Heavy metal-faced shield | durable broad protection |
| SHD-006 | Pavise | deployed/mobile cover |


### 12.3 Coverage descriptors

These describe **humanoid-region coverage terms**; nonhumanoid anatomy needs its own mapping. They never imply perfect coverage or injury immunity.

| ID | Coverage meaning |
|---|---|
| COV-01 | Head |
| COV-02 | Neck |
| COV-03 | Chest |
| COV-04 | Abdomen |
| COV-05 | Arms |
| COV-06 | Hands |
| COV-07 | Legs |
| COV-08 | Feet |
| COV-09 | Torso |
| COV-10 | Torso + limbs |
| COV-11 | Full harness |


---

# PART IV — LIFE, ANATOMY AND ECOLOGICAL CONTENT

## 13. Bodies and locomotor architecture

Living creatures and artificial assemblies share **component/body-plan descriptions**, but not necessarily physiology, death, repair or infection. `BODY` is morphology and function, not a guarantee of human organs. `BODY-007` is an engineered assembly, not automatically sentient or supernatural. Location rolls in Fantasy stay with that adapter. Source: `FA-LIB` §§24–33.


### 13.1 Body-plan archetypes

No creature is created by selecting a body plan.

| ID | Plan | Typical components | Important boundary |
|---|---|---|---|
| BODY-001 | Humanoid | Head, neck, torso, two arms, two legs | Humanoid function/location mapping; physiology selected by species |
| BODY-002 | Quadruped | Head/neck, torso, forelimbs, hindlimbs, optional tail | Gait, limb distribution, and species-dependent tails |
| BODY-003 | Avian/winged | Head/neck, torso, wings, legs/talons, tail | Wing function needed for relevant forms of flight |
| BODY-004 | Serpentine | Head plus contiguous forward, middle, rear/tail regions | Distributed axial locomotion; actual vulnerable structures vary |
| BODY-005 | Arthropod / exoskeletal | Head/sensors, thorax/core, abdomen, limbs, special appendages as applicable | External protective shell and internal functions are distinct |
| BODY-006 | Amorphous | Species-defined core or distributed body; no presumed head | Damage/function follows actual internal organization |
| BODY-007 | Constructed / component body | Core, frame, mobility, sensors, manipulators, power, tools/weapons as relevant | Uses component damage/repair; sentience/biology not implied |


## 14. Natural actions and creature ecology

Natural attacks are action *methods* supported by anatomy; they do not create a held weapon or additional uncommitted attacks. Venom is a delivery/exposure process, not guaranteed physical injury. A fictional monster may apply supernatural capability only from a separate enabled module. Sources: `FA-LIB` §§34–45.


### 14.1 Natural attack methods

The attack strength, reach, effect, damage and species access are **not universal**.

| ID | Natural action | Physical mechanism / conditional trait |
|---|---|---|
| NAT-001 | Bite | Pierce/Crush; Grip where anatomy supports |
| NAT-002 | Claw | Cut; multi-limb anatomy possible |
| NAT-003 | Horn/gore | Pierce; Brace/Charge |
| NAT-004 | Slam | Blunt; Scale-sensitive contests |
| NAT-005 | Tail strike | Blunt; extended Reach |
| NAT-006 | Stomp | Crush; target-size/position limited |
| NAT-007 | Constrict | Crush; requires established grapple/control |
| NAT-008 | Quill/spine | Pierce; may be contact or ranged |
| NAT-009 | Breath/projected organ | setting-defined; uses ranged/area effect procedure |
| NAT-010 | Venom delivery | Exposure; requires successful delivery mechanism |


### 14.2 Ecological / engineered actor templates

`CRT` defines a design pattern, not a species or encounter difficulty; actors are instantiated and operated through Core.

| ID | Template | Required aspects | Limits |
|---|---|---|---|
| CRT-001 | Ordinary predator | Territory, prey, method, hunger, risk, weapons, avoidance/escape | No compulsory aggression or boss behaviour |
| CRT-002 | Pack hunter | Coordination, communication, hierarchy, flanking, prey selection | Membership does not grant skill or simultaneous pressure unless achieved |
| CRT-003 | Large charger | Mass, locomotive momentum, gore/slam, terrain, turning space | Physical charge requires distance/timing and suitable geometry |
| CRT-004 | Flying predator | Flight envelope, wing condition, takeoff/landing, altitude, wind, carrying | Wing damage changes actual flight function |
| CRT-005 | Swarm | Area, density, movement, collective mechanism, depletion | Counts/area remain finite; aggregation does not create creatures |
| CRT-006 | Construct / artificial actor | Power, command, maintenance, sensors, autonomy, faults | Construct is not automatically immune to mental or environmental effects |
| CRT-007 | Colossal organism | Scale, support, frontage, reach, terrain, local vs systemic injury | Local damage and systemic incapacitation are different |


---

# PART V — PLACES, SERVICES AND COMMUNITY CONTENT

## 15. Physical places and sites

A site is a **spatial functional archetype**; its likely installed systems and possible stock are *questions to investigate*, not treasure or surviving infrastructure. `SITE-023` is a security/military facility type; it does not produce armaments. A construction may appear in ancient, modern, speculative or devastated worlds only if its type and technology are eligible. Source: `PA-LIB` §§15–16.


### 15.1 Site archetype catalogue

Original expected use and plausible installations are descriptive metadata only.

| ID | Site archetype | Original role / plausible installed systems | Typical dependencies / caution |
|---|---|---|---|
| SITE-001 | Residence/Apartment Building | Housing; possible: Food/water containers, household tools, clothing, records, furnishings | Building water/power/heat; stairs/elevators; Private ownership, occupancy, fire/structural access |
| SITE-002 | Grocery/Market | Retail food distribution; possible: Shelf-stable/perishable food, water, sanitation goods, shelving/cold storage | Grid/cold chain; loading access; Prior consumer depletion, spoilage, ownership/security |
| SITE-003 | Pharmacy | Medication retail/storage; possible: Specific pharmaceuticals, medical consumables, hygiene goods, controlled storage | Power/environmental control; records/security; Drug identity, shelf/storage, access controls; no generic medicine cache |
| SITE-004 | Clinic/Hospital | Healthcare; possible: Medical consumables, pharmaceuticals, equipment, oxygen/utility systems, records | Power, water, sanitation, staff, supply chain; Installed equipment may outlast consumables; patient/biological hazards profile-specific |
| SITE-005 | Fuel Station | Retail fuel distribution; possible: Specific fuels, lubricants, small goods, underground/aboveground tanks | Electrical pumps, compatible transfer gear, tank integrity; Fuel presence/quality and pumping access must be established |
| SITE-006 | Fuel Depot/Terminal | Bulk fuel storage/distribution; possible: Large compatible fuel stocks, pumps, tanks, piping, loading equipment | Power, transfer systems, transport access, fire control; High strategic value; no assumed surviving stock |
| SITE-007 | Warehouse/Distribution Center | Bulk storage/logistics; possible: Campaign-specific stored commodities, racks, forklifts, loading docks | Transport routes, handling equipment, inventory records; Contents depend entirely on historical stock and prior distribution |
| SITE-008 | Hardware/Building Supply | Construction retail/wholesale; possible: Tools, fasteners, lumber, plumbing/electrical supplies, chemicals | Storage/loading access; Mixed compatibility and hazardous materials possible |
| SITE-009 | Farm/Agricultural Holding | Food production; possible: Crops/livestock if established, seed, feed, fertilizer, tools, fuel, water systems | Season, water, soil, labor, storage, machinery; Field is productive potential, not harvested stock |
| SITE-010 | Water Treatment Facility | Potable-water service; possible: Pumps, tanks, filters, treatment equipment/chemicals, controls | Raw-water source, power, chemicals, operators, distribution network; Physical plant can survive while potable service fails |
| SITE-011 | Wastewater Facility | Sanitation service; possible: Pumps, treatment equipment, chemicals, controls | Power, inflow/outflow network, operators; Failure can create downstream environmental hazards |
| SITE-012 | Electrical Substation | Power transmission/distribution; possible: Transformers, switchgear, controls, conductors | Upstream supply, downstream network, technical access; Salvage can permanently reduce restoration potential |
| SITE-013 | Power Generation Site | Electrical generation; possible: Generation equipment, fuel/input systems, switchgear, controls, spares | Fuel/resource source, cooling, staff, transmission; Installed capacity is not delivered service |
| SITE-014 | Communications Facility | Telecommunications; possible: Radios/network gear, towers, servers, batteries/generators, records | Power, backhaul, antennas, compatible endpoints; Function may survive locally while wider network fails |
| SITE-015 | Municipal/Public Works Yard | Infrastructure maintenance; possible: Vehicles, tools, pipe, road materials, pumps, records, fuel where established | Staff, fuel, routes, workshops; Often high maintenance value even without strategic stock |
| SITE-016 | School/Community Center | Education/public assembly; possible: Shelter space, kitchens/toilets, records, basic supplies | Water, sanitation, heat/power, access; Can serve as refuge without being a mature settlement |
| SITE-017 | Industrial Workshop/Factory | Manufacturing/repair; possible: Installed machinery, tooling, stock/feedstock, documentation | Power, staff, inputs, ventilation, logistics; Portable depletion does not erase installed productive capability |
| SITE-018 | Cold Storage Facility | Food/temperature-controlled logistics; possible: Perishable stock if established, refrigeration equipment, pallets | Power, refrigeration, monitoring, transport; Loss of power creates time-dependent temperature exposure |
| SITE-019 | Rail Yard/Intermodal Terminal | Transport/logistics; possible: Rolling stock/containers if established, handling gear, fuel/service equipment | Track network, locomotives/vehicles, staff, route control; Cargo contents are separate records; transit stock is not site-owned by default |
| SITE-020 | Scrap Yard/Landfill | Waste/material recovery; possible: Mixed scrap, vehicles/appliances/materials, hazardous waste | Sorting/handling, PPE, processing, transport; High quantity does not equal ready material quality |
| SITE-021 | Government/Administrative Office | Administration/records; possible: Records, maps, communications, office equipment, emergency plans | Power, staff, authority, data access; Records can retain institutional value after office function stops |
| SITE-022 | Library/Archive/Data Repository | Knowledge preservation; possible: Books, maps, technical records, digital data where established | Environmental preservation, power/data access for digital holdings; Information survives only if media/access remain usable |
| SITE-023 | Security/Military Facility | Security/service installation; possible: Equipment and stores only as actually established by setting/state | Authority, access, staffing, logistics; No automatic weapons/ammunition cache; exact establishment required |


## 16. Service chains, continuity methods, and habitation

A service profile specifies an **output delivered to identified users**, with quality, actual capacity, demand, allocation, dependencies and acceptance. It is never conflated with the physical equipment that supplies it, the institution responsible for it, or an authorization to receive it. Continuity/temporary-mode templates have the same requirements even during normal festivals, seasonal work, military movement or disaster response. Source: `PA-LIB` §§17–22.


### 16.1 Service archetypes

Actual outputs and consumer service quality are setting/instance data.

| ID | Service | Useful output | Dependencies / limits |
|---|---|---|---|
| SVC-WAT-001 | Potable Water Service | Potable water delivered to defined users | Raw/treated source; treatment; pumping/gravity; storage; distribution; operators; Raw-water quantity is not potable service |
| SVC-SAN-001 | Wastewater/Sewage Service | Safe collection/removal/treatment of wastewater | Collection network; pumps/gravity; treatment/disposal; power; operators; Failure can create environmental/health exposure rather than simple “service off” |
| SVC-PWR-001 | Electrical Power Service | Electrical energy delivered within defined voltage/quality/area | Generation/import; transmission; distribution; control; staff; fuel/environment; Installed generation is not the same as delivered power |
| SVC-FUEL-001 | Fuel Distribution Service | Compatible fuel delivered to consumers/equipment | Bulk stock/source; pumps; transport; containers; access/control; Fuel family/grade compatibility remains specific |
| SVC-FOOD-001 | Food Distribution Service | Food delivered/available to defined population | Stock/production; storage; transport; allocation; preparation where relevant; Regional abundance does not equal local access |
| SVC-HEAT-001 | Space-Heating Service | Thermal protection for defined occupied spaces | Heat source; fuel/power; distribution; building envelope; operators; Delivered heat depends on building/environment, not just heater ownership |
| SVC-COLD-001 | Cold-Chain Service | Maintains specified temperature through storage/transport stages | Power; refrigeration; insulated storage; monitoring; transport; A break in one stage may affect only stock exposed after that time |
| SVC-COM-001 | Local Communications Service | Voice/data connectivity within defined area/system | Endpoints; repeater/tower; power; frequencies/network; operators; Contact does not imply material route or political agreement |
| SVC-COM-002 | Long-Distance Communications Service | Information exchange between distant nodes | Backhaul/satellite/radio/courier chain; power; endpoints; staff; Latency and confidence remain explicit |
| SVC-ROAD-001 | Road Transport Service | Movement of people/cargo by supported road vehicle class | Road/bridge condition; vehicles; fuel; drivers; security/access; Route may be open to one mode and blocked to another |
| SVC-RAIL-001 | Rail Transport Service | Movement along a compatible rail network | Track; rolling stock; motive power; signaling/operations; loading facilities; Track existence alone does not provide service |
| SVC-WATERWAY-001 | Water Transport Service | Movement by boat/barge/ship within defined waterway | Navigable water; vessels; fuel/crew; docks/handling; weather; Season/weather/draft may constrain service |
| SVC-WASTE-001 | Solid Waste Service | Collection, transfer, processing/disposal of solid waste | Containers; collection; transport; disposal/process site; staff; Waste accumulates physically if service stops |
| SVC-HEALTH-001 | Healthcare Service | Defined diagnosis/treatment capacity to a population | Qualified staff; facilities; equipment; medicine; water/power/sanitation; records; A building or medical cache alone is not healthcare capacity |
| SVC-EDU-001 | Education/Training Service | Instruction and competence-development capacity | Instructors; learners; space; materials; curriculum; time; Information access is not completed training |
| SVC-MFG-001 | Repair/Manufacturing Service | Repeatable maintenance/fabrication within a declared scope | Staff; workshop; tools; power; materials; documentation; quality control; Name exact products/repairs supported; no generic “industry points” |


### 16.2 Temporary / alternate service methods

The legacy `WRK` prefix names an *arrangement*, not a worker or independent project ledger.

| ID | Continuity arrangement | Intended function | Requirements / bounded limitations |
|---|---|---|---|
| WRK-WAT-001 | Water Trucking/Container Distribution | Potable/raw water moved from another source | Tank/container, transport, loading, route, receiving storage, staff; Limited by transport cycle and source; not a permanent distribution network |
| WRK-WAT-002 | Gravity-Fed Emergency Water | Stored/elevated water delivered without normal pumping | Elevated storage, viable piping/hoses, valves, water quality; Finite buffer unless replenished |
| WRK-PWR-001 | Portable Generator Support | Temporary electrical service to selected loads | Generator, fuel, distribution, exhaust/safety, operator; Load selection and fuel endurance matter |
| WRK-PWR-002 | Battery Emergency Supply | Temporary electrical continuity | Charged storage, compatible inverter/DC loads, discharge limit; Must be recharged or replaced |
| WRK-COM-001 | Radio Relay | Temporary communications bridge | Compatible radios/repeater, elevated location, power, operators; Provides information link, not transport |
| WRK-COM-002 | Courier/Runner Network | Physical message delivery | People/vehicles, route, schedules, security; Latency is actual travel time |
| WRK-SAN-001 | Portable/Field Sanitation | Temporary human-waste containment/disposal | Units/latrines, consumables, servicing/disposal, hygiene; Capacity and disposal path limit endurance |
| WRK-SHL-001 | Temporary Shelter Consolidation | Concentrates population in usable protected space | Building/tents, bedding, heat/ventilation, water/sanitation, management; Shelter space alone does not satisfy all services |
| WRK-FOOD-001 | Community Feeding Point | Centralizes food preparation/distribution | Food stock, water, cooking fuel/power, kitchen, staff, sanitation; Does not produce food; it converts stock into meals |
| WRK-MED-001 | Temporary Aid/Clinic Station | Temporary defined medical service | Qualified staff, supplies, clean space, water/power as needed; Capability limited to declared care scope |
| WRK-TRN-001 | Temporary Crossing/Ferry | Temporary route across a blocked gap | Vessel/structure, operators, approaches, load profile, weather; Mode/load limits must be stated |
| WRK-HEAT-001 | Localized Heated Refuge | Concentrates heating on selected occupied areas | Heat source, fuel/power, ventilation, shelter; Reduces service area rather than creating more heat |


### 16.3 Habitation and community forms

Forms are spatial/organizational patterns, **not mandatory settlement tiers**. Any number of people may inhabit one when actual capacity supports it; retained legacy source titles remain aliases.

| ID | Shared display name | Definition | Requirements / boundary |
|---|---|---|---|
| HAB-001 | Household Refuge | One or more households sheltering in an ordinary residence/property | Existing domestic shelter, private stores, local utilities or alternatives; Low service redundancy; household labor/care obligations |
| HAB-002 | Public Emergency Shelter | Temporary congregate refuge in school, arena, church, hall, etc. | Large shelter space, registration/coordination, water, sanitation, feeding, safety; Often dependent on external supply and intact civic institutions |
| HAB-003 | Temporary Camp | Purpose-built short/medium-term habitation | Shelter units, water, sanitation, food logistics, access, management; Weather and service burden increase quickly if population persists |
| HAB-004 | Mobile Group/Convoy | Population whose habitation and supply move with transport | Vehicles/animals, route access, carried stock, fuel/feed, camps; Destination stock cannot support the group before arrival |
| HAB-005 | Distributed Rural Community | Population dispersed across farms/homesteads but sharing services/institutions | Local production, roads/comms, shared trade/security/medical/administrative links; Distance can reduce service access and response speed |
| HAB-006 | Fixed Community / Recovery Settlement | Persistent habitation with recurring local services | Shelter, water, sanitation, food access, coordination, security, maintenance; No implied walls, government model, or self-sufficiency |
| HAB-007 | Service / Industrial Community Hub | Settlement organized around high-value service/production capability | Workforce, infrastructure, inputs, housing, transport, institutional operation; May remain import-dependent for food or other needs |
| HAB-008 | Regional Center | Settlement providing substantial services to surrounding nodes | Local services plus network capacity, institutions, storage, transport/comms; Regional role depends on actual links and exportable capacity |


---

# PART VI — POPULATIONS, INSTITUTIONS AND NETWORKS

## 17. Movement / intake templates

Templates describe *patterns* of arrival, displacement or resettlement; they do not determine consent, legal status, allegiance, work capacity, births or individual intentions. Population records live in Core, preserving household membership, physical arrival, needed services, existing possessions and claims. Source: `PA-LIB` §23.


### 17.1 Population movement templates

These can be used for migration, evacuation, urbanization, commerce, war, disaster, space settlement or historical relocation when applicable.

| ID | Population pattern | Typical use | Tracked issues and limitation |
|---|---|---|---|
| POP-001 | Evacuating Household Group | Households leaving an at-risk area under partial planning | Household integrity, private property, transport, destination/route, information carried; Not automatically destitute, hostile, or willing to settle |
| POP-002 | Displaced Civilian Cohort | Civilians forced from ordinary residence | Immediate needs, dependants, health, property, origin ties, intended duration; Population count is not workforce count |
| POP-003 | Injured/Sick Arrival Cohort | Arrivals with elevated care requirements | Triage, isolation only where hazard supports it, shelter, caregivers, medical capacity; Do not infer disease from displacement alone |
| POP-004 | Specialist Arrival | One or more people claiming useful technical/professional skill | Identity, claim/evidence, health, tools, willingness, household ties; Skill claim requires evidence appropriate to context; no instant institution |
| POP-005 | Organized Evacuation Convoy | Population movement with leadership/transport/logistics | Manifest/headcount, vehicles, route, fuel, communications, destination; Convoy resources remain with actual owners/custodians |
| POP-006 | Returning Residents | Former residents returning to a prior community/property | Claims, property records, current occupants, service capacity, relationships; Return does not automatically restore ownership/control where contested |
| POP-007 | Voluntary Migrant/Immigrant Group | People moving toward perceived opportunity/safety | Motives, destination agreements, skills, households, property, legal status; Presence, residency, service eligibility, and membership remain distinct |


## 18. Institutions

`INST` records institutional **role/function**, not government form, recognition, mandate or material assets. An instantiated organization requires actual actors, authority relationships, budget, procedures, access, staffing, capacity, succession and records. Roman magistracies and military ranks remain local institution variants, not generic names assigned here. Source: `PA-LIB` §§24–25.


### 18.1 Reusable institution roles

Some entries use modern names as readable examples; premodern and speculative settings can implement equivalent functions through locally appropriate institutions without granting modern law or equipment.

| ID | Institution function | Role | Required elements / caveat |
|---|---|---|---|
| INST-001 | Emergency Coordination Cell | Coordinates information, priorities, tasking, and inter-service response | Decision authority; representatives; communications; situation records; meeting/process cadence; Coordination cannot execute tasks without capable subordinate services |
| INST-002 | Water Utility/Water Service Team | Operates and maintains water source/treatment/distribution | Operators; technical staff; parts/chemicals; infrastructure access; quality procedures; Institution can exist while service is capacity-limited |
| INST-003 | Public Works/Maintenance Service | Maintains roads, waste, buildings, utilities, and civic assets within scope | Staff; workshops/tools; vehicles; materials; authority; work-order system; Scope must be declared; cannot repair every technology |
| INST-004 | Medical Service | Provides defined healthcare functions | Qualified staff; facilities; supplies; records; referral/triage procedures; Service capability is narrower than “hospital exists” |
| INST-005 | Food/Agricultural Coordination Service | Coordinates production, storage, distribution, or communal agriculture where adopted | Farmers/producers; storage; logistics; records; agreements/authority; Does not seize private production absent authority |
| INST-006 | Security/Law-Enforcement Service | Provides patrol, response, investigation, custody or defense within defined authority | Personnel; training; equipment; command; law/mandate; logistics; Security, military morale, legitimacy, and civilian confidence remain distinct |
| INST-007 | Fire/Rescue Service | Responds to fire, rescue, collapse, and related emergencies | Personnel; protective equipment; water/agents; vehicles; communications; Capability depends on hazard and equipment profile |
| INST-008 | Logistics/Transport Service | Schedules and operates movement of people/materials | Dispatch; drivers/operators; vehicles; fuel; routes; manifests; maintenance; Allocation is not delivery |
| INST-009 | Technical Maintenance Bureau/Workshop | Coordinates maintenance, diagnosis, repair, fabrication within scope | Technicians; tools; parts; documentation; work-order/acceptance system; Naming a bureau creates no technicians or spares |
| INST-010 | Education/Training Service | Preserves and develops competence | Instructors; curriculum; learners; facilities/materials; records; evaluation; Documents alone do not create competence |
| INST-011 | Civil Administration/Council | Performs defined civic decisions/records/services | Authority basis; membership; procedures; records; staff; communications; accountability; No preferred democratic/authoritarian/customary model is assumed |
| INST-012 | Records/Archive Office | Preserves and serves institutional/property/technical records | Custodians; storage; indexing/access; preservation; authority; Records are evidence/information, not automatic legal recognition |
| INST-013 | Market/Trade Administration | Operates market, contracts, weights/measures, scrip/credit or trade coordination where adopted | Participants; rules; accounting; security; dispute procedure; No universal barter or currency model |


## 19. Networks and transfers

Nodes = actual places/services; links = actual infrastructure/access opportunities; flows = **planned or executed movements** of existing people, goods, services or reports. A link profile does not itself create usable throughput. Transit, receipt and knowledge events remain Core's responsibility. Source: `PA-LIB` §§26–29.


### 19.1 Node archetypes

A network node must reference a real place/institution.

| ID | Network type | Purpose | Required profile |
|---|---|---|---|
| NET-N-001 | Settlement Node | Habitation/community participating in exchange | Services, imports/exports, storage, institutions, access |
| NET-N-002 | Production Node | Farm, mine, factory, power plant or other productive site | Output, local demand, inputs, storage, operator, transport |
| NET-N-003 | Depot/Storage Node | Concentrated storage/distribution point | Stocks, handling, security, access, throughput |
| NET-N-004 | Service Node | Hospital, workshop, school, communications center or similar | Service capacity, local demand, export/referral capacity, dependencies |
| NET-N-005 | Transfer Node | Port, rail terminal, bridgehead, intermodal yard, distribution junction | Mode interfaces, handling capacity, storage, route dependencies |


### 19.2 Link archetypes

A link requires compatible endpoints, capacity, availability and practical access.

| ID | Network type | Purpose | Required profile |
|---|---|---|---|
| NET-L-001 | Road Link | People/cargo movement by defined road vehicle classes | Distance, condition, modes/load, capacity, travel time, control/security, fuel/vehicle dependencies |
| NET-L-002 | Rail Link | Rail cargo/passenger movement | Track/bridge condition, rolling stock, motive power, operations, terminals |
| NET-L-003 | Waterway Link | Boat/barge/ship movement | Navigability, vessel class, docks, weather/season, crew/fuel |
| NET-L-004 | Air Link | Aircraft movement where setting supports it | Aircraft, landing sites, weather, fuel, crew, maintenance, payload |
| NET-L-005 | Pipeline Link | Fluid/gas transport | Product compatibility, pressure/pumps, valves, integrity, power/control |
| NET-L-006 | Electrical Intertie | Electrical power transfer | Voltage/frequency/system compatibility, line capacity, control/protection |
| NET-L-007 | Radio/Data Link | Information transfer | System compatibility, range/path, power, endpoints, latency/reliability |
| NET-L-008 | Courier Link | Scheduled physical message/document transfer | Route, courier, schedule, transport, security, latency |
| NET-L-009 | Service Referral Link | Movement/booking/access to a remote service | Eligibility/agreement, communication, physical travel where needed, service capacity |


### 19.3 Flow archetypes

A schedule or allocation is not a completed transfer.

| ID | Network type | Purpose | Required profile |
|---|---|---|---|
| NET-F-001 | Scheduled Commodity Flow | Recurring movement of a named commodity | Source stock/output, quantity/rate, schedule, route, transport, receiving capacity, responsible actor |
| NET-F-002 | Emergency Aid Flow | Temporary prioritized movement of defined aid | Trigger, donor stock, authority/agreement, transport, recipient, termination condition |
| NET-F-003 | Shared Service Allocation | Remote service capacity allocated across nodes | Provider capacity, local demand, exportable capacity, recipient access/link, allocation policy |
| NET-F-004 | Information/Report Flow | Recurring reports or data exchange | Source, channel, frequency, latency, recipients, confidence/verification |
| NET-F-005 | Population Movement Flow | Planned recurring or one-time movement of people | Origin, destination, numbers, households, route, transport, services, arrival capacity |


---

# PART VII — PROGRAMS, HAZARDS AND CRISIS REFERENCES

## 20. Development, renewal and reconstruction templates

The historical source names these `RCN` (reconstruction). Shared ownership interprets each as a **program template for achieving a real deliverable**, whether recovering damaged capacity, expanding a functioning service, or building an entirely new one. The program requires actual scope, actors, work, inputs, acceptance, maintenance and operational handover. *Repair → restore → replace → adapt → redesign → abandon* are available strategies, not obligatory stages. A restored power plant does not mean commissioned electricity service. Source: `PA-LIB` §§30–31.


### 20.1 Program archetypes

A scenario must choose the strategy and define corresponding acceptance evidence; these rows supply no automatic work credit.

| ID | Template | Outcome | Acceptance domains |
|---|---|---|---|
| RCN-001 | Potable Water Restoration | Restore/replace reliable potable-water service | Source; treatment; storage; distribution; operators; chemicals/consumables; testing; maintenance; acceptance |
| RCN-002 | Decentralized Water Replacement | Build local wells/catchment/treatment instead of old centralized service | Source rights/quality; treatment; local distribution; staffing; seasonal capacity; testing |
| RCN-003 | Electrical Grid Restoration | Restore viable generation/import and distribution | Generation/source; transmission; distribution; protection/control; staffing; fuel/input; testing/commissioning |
| RCN-004 | Microgrid/Distributed Power Redesign | Replace centralized dependency with local generation/storage networks | Generation; storage; control; distribution; maintenance; replacement inputs; load priorities |
| RCN-005 | Transport Corridor Restoration | Restore a route for defined modes/loads | Road/bridge/rail/waterway works; clearing; inspection; maintenance; security/access |
| RCN-006 | Agricultural Production Expansion | Create durable seasonal food production | Land; water; seed; soil inputs; labor; tools; storage; processing; season; training |
| RCN-007 | Cold-Chain Reconstruction | Restore temperature-controlled food/medical logistics | Power; refrigeration; storage; transport; monitoring; maintenance |
| RCN-008 | Medical Service Reconstruction | Move from emergency care toward durable healthcare capacity | Facilities; staff; training; equipment; medicine; utilities; records; referral; supply |
| RCN-009 | Repair-to-Manufacturing Transition | Develop repeatable local fabrication from a repair workshop | Product scope; drawings/specs; tooling; feedstock; skilled labor; quality control; maintenance |
| RCN-010 | Communications Backbone Restoration | Restore durable local/regional communications | Sites; power; links/backhaul; endpoints; operators; procedures; maintenance |
| RCN-011 | Housing and Sanitation Expansion | Increase safe habitation capacity | Housing/shelter; water; sanitation; heat/cooling; access; waste; maintenance |
| RCN-012 | Education and Apprenticeship System | Create durable workforce/knowledge renewal | Instructors; curriculum; institutions; facilities; learners; assessment; succession |
| RCN-013 | Civic Records and Administration Recovery | Restore durable civic records/procedures | Archives; identity/property records; offices; staff; authority; procedures; backup |
| RCN-014 | Waste Management Recovery | Create durable solid/liquid-waste handling | Collection; transfer; treatment/disposal; staff; transport; environmental safeguards |
| RCN-015 | Regional Supply Corridor | Create dependable multi-node movement of a critical commodity | Suppliers; agreements; storage; transport; route; scheduling; security; contingencies |


## 21. Causal hazard templates

A hazard template identifies its *possible source and effect route*. It never creates an active exposure. Actual onset, source, field, route, intensity, duration/dose, detection, protection, spread, limits, treatment and termination are selected in a competent genre or setting profile. Fire may burn structures or expose people only after a real event. Source: `PA-LIB` §§32–33.


### 21.1 Hazard families

Source-specific scientific and medical models are required before numerical effects; some hazards need enabling technology (ordnance, electric machinery, industrial chemicals).

| ID | Hazard | Potential causal channels | Required calibration and limits |
|---|---|---|---|
| HAZ-001 | Fire/Heat | Thermal injury, ignition, smoke generation, structural damage | Heat/fire source; spread conditions; fuel; ventilation; suppression; evacuation; |
| HAZ-002 | Smoke/Combustion Products | Respiratory/visibility/toxic exposure | Source; concentration/ventilation; breathing exposure; respiratory protection; detection; |
| HAZ-003 | Flood/Standing Water | Drowning, contamination, access loss, structural/electrical damage | Water depth/flow; contamination; duration; routes; drainage; |
| HAZ-004 | Structural Instability/Collapse | Crush/fall/entrapment and access obstruction | Structure condition; loads; damaged elements; inspection; exclusion/support; |
| HAZ-005 | Unsafe Water/Microbial Contamination | Disease/toxic exposure through water | Contaminant; source; concentration/assay; treatment compatibility; consumption/exposure; |
| HAZ-006 | Industrial Chemical Contamination | Toxic/corrosive/flammable exposure | Specific chemical; release; medium; PPE; detection; decontamination; medical profile; |
| HAZ-007 | Infectious Disease | Biological transmission and illness | Specific pathogen/disease profile; transmission; incubation; infectious period; prevention/treatment; |
| HAZ-008 | Ionizing Radiation | Radiation exposure/contamination | Source; radiation type/field; dose method; shielding/distance/time; contamination where applicable; |
| HAZ-009 | Extreme Cold | Hypothermia/frost injury and infrastructure stress | Temperature; wind/wetness; shelter/clothing; exposure time; heat service; |
| HAZ-010 | Extreme Heat | Heat illness and infrastructure stress | Temperature/humidity/radiant heat; water; shelter/cooling; exertion; |
| HAZ-011 | Ash/Dust/Particulate | Respiratory/visibility/machinery contamination | Particle type; concentration; wind; filtration; cleaning; equipment sensitivity; |
| HAZ-012 | Unexploded Ordnance/Mines | Localized explosive hazard | Known/unknown device field; detection; access control; qualified disposal; No explosion absent actual ordnance and exposure |


## 22. Crisis and disruption patterns

Most `APX` rows are **not exclusive to apocalypse campaigns**: a regional war, public-health emergency, loss of credit, or isolated community can be part of ordinary historical, military, civic or space play. They are *optional scenario-design patterns* that must be invoked, specified and instantiated with an actual event and state. The `APX-X01` template is deliberately **not imported as an enabled universal phenomenon**; it remains a theme extension shell. The legacy `APX` prefix is kept as an alias for these optional patterns pending a future formal rename. Source: `PA-LIB` §§34–35.


### 22.1 Ordinary disruption and crisis catalogue

No imported entry creates global collapse, disease lethality, damage radius or geopolitical reactions.

| ID | Crisis archetype | Potential effects | Specialization / boundary |
|---|---|---|---|
| APX-001 | Conventional Interstate/Regional War | Physical destruction, displacement, military logistics, transport disruption, institutional strain | Weapons/equipment effects; geography; combatants; laws/institutions; actual damage; UXO where relevant; Does not imply total state collapse; functioning regions may remain |
| APX-002 | Civil Conflict/State Fragmentation | Competing authority, disrupted services, displacement, contested infrastructure/claims | Factions; jurisdictions; security; communications; service control; Physical infrastructure may remain intact while governance fragments |
| APX-003 | Pandemic/Epidemic Crisis | Illness, workforce loss, medical overload, behavior/policy changes, supply disruption | Specific disease profile; transmission; treatment; public-health institutions; No generic lethality or immunity; disease module required |
| APX-004 | Grid/Cyber/Systems Disruption | Loss/degradation of electrical, communications, financial, or control systems | Affected technologies; physical vs software failure; restart/support; regional interties; Does not physically destroy every electronic device by default |
| APX-005 | Severe Natural Disaster | Localized/regional physical destruction, displacement, route/service failure | Hazard type: storm, earthquake, flood, wildfire, etc.; geography; building/infrastructure profiles; May be surrounded by functioning external society |
| APX-006 | Ecological/Agricultural Crisis | Falling food/water/ecosystem output, migration, economic and institutional pressure | Specific ecological cause; crop/water systems; seasons; trade network; Does not imply immediate infrastructure destruction |
| APX-007 | Nuclear Conflict/Accident | Blast/fire where applicable, radiation/contamination, infrastructure and institutional disruption | Specific event geometry; yield/source only when calibrated; radiation hazard profile; fallout/weather; actual strikes; No universal fallout map or instant global extinction; exact effects require scenario data |
| APX-008 | Solar/Geomagnetic Technology Disruption | Electrical/communications disruption where technology is vulnerable | Event severity; grid/electronic susceptibility; geography; restoration capability; Do not generalize fictional EMP effects to every device |
| APX-009 | Volcanic/Ash Crisis | Ashfall, air/transport/agriculture/water/infrastructure effects | Eruption/ash profile; wind; geography; duration; particulate hazard; Effects vary strongly by region and event |
| APX-010 | Economic/Distribution Collapse | Loss of market, credit, distribution, employment or institutional capacity with potentially intact physical stock | Economy; contracts; logistics; institutions; access/ownership; Goods can physically exist while becoming inaccessible or undistributed |
| APX-011 | Slow Institutional Decline | Progressive service degradation, maintenance backlog, migration, local adaptation | Affected institutions; budgets/resources; demographic/economic causes; timeline; No single “collapse day” required |
| APX-012 | Localized Isolation Crisis | One community/region cut off from wider functioning society | Cause of isolation; routes/comms; local stocks/services; external response; Supports disaster-survival games without world apocalypse |


### 22.2 Theme-only crisis shell — excluded from universal activation

`APX-X01` (Extraordinary/Theme Crisis Template) remains a **conditional wrapper** supplied by the PA theme library or another specialized module. Alien contact, necromancy, mutation, paranormal infection, temporal alteration and comparable causes are not features of IRGS worlds by default. The shared catalogue may **reference** such a local type once enabled; its powers, transmission, counterplay, persistence and consequences remain specialized. In the same way, Fantasy's `PAR-*` supernatural paradigms and `XMAT-*` extraordinary material *effect templates* are intentionally **not** copied into the mundane shared reference collection.

---

# PART VIII — TECHNOLOGY, ERA AND GENRE ADAPTER CONTRACTS

## 23. Era and availability tags

The Military index's six browse facets are useful for **historical indexing**, not universal chronological laws. An item can survive into later periods; a nominal era does not make technology available everywhere. Regional, institutional, trading and setting records determine actual eligibility. Source: `MIL-INDEX` §1.


### 23.1 Legacy era lookup

No era automatically enables all tagged content. A science-fiction period can include prior technology.

| ID | Source-era label | Index description |
|---|---|---|
| ERA-ANT | Antiquity | Ancient societies before the first century AD; bronze and iron technologies where locally established |
| ERA-EAD | Early Centuries AD | Roughly the first–fifth centuries AD; early imperial and late-antique contexts |
| ERA-MED | Middle Ages | Roughly AD 500–1500; later regional/period subdivisions can refine availability |
| ERA-EMD | Early Modern | Roughly AD 1500–1800; expanding gunpowder warfare, maritime systems and organized military supply |
| ERA-CON | Contemporary | Used broadly in this library for industrial and modern military contexts, approximately the nineteenth century to the present |
| ERA-SCI | Science Fiction | Fictional future or alternative technological contexts; availability determined by the setting |


## 24. Adapter boundary matrix

| Domain | Shared content owns | Adapter must supply | Specifics that must remain local |
|---|---|---|---|
| Melee/ranged weapon | Weapon body, modes, handling features, projectile relations | Hit/effect interface, injury/protection mapping, attack timing, ranges, ammunition behaviour | Fantasy Threat/Defeat/Reach; Roman period eligibility; firearm ballistics; SSN only by explicit external agreement |
| Protective equipment | Material/construction, covered components and handling | Actual threat channels, penetration, effect transfer, condition changes | Fantasy Cut/Pierce/Impact, shield numeric Defense/Structure; modern ballistic and sealed suit ratings |
| Material stock | Physical material and goods, processing dependencies | Technical conversions, specifications and quality acceptance | Metallurgy, fictional alloys, enchantment, manufacturing technology |
| Biological actor | Body plan, ecology/needs fields, locomotor/natural-action possibilities | Physiology, injury, exposure, cognition/behaviour as actually established | Fantasy monsters, extraterrestrial biology, historical breeds, magic and artificial sentience |
| Transport/platform | Type, functional components, load/cargo/interface concepts | Motion, propulsion, navigation, manoeuvre and environmental operating envelope | Naval seamanship, airflight, space trajectory/thermal/pressure, creature/mount handling |
| Communications & sensors | Hardware/software family and compatibility fields | Propagation, detection, operating modes, effective quality, information events | Telegraph, encrypted radio, optical/satellite and interplanetary light-time |
| Facility/utility | Physical site/plant and service-chain prerequisites | Quantitative throughput, project work, supply/energy/maintenance models | Era-specific energy sources, nuclear systems, sanitation, atmosphere loops |
| Health/medical | Kit, facility, consumable and service archetypes | Actual medical/treatment/access procedures and exposure effects | Antibiotics, magic healing, Roman medicine, surgical techniques, vacuum physiology |
| Community/institution | Organizational role, settlement/network patterns | Core actor/authority/legal/economy and service procedures | Roman magistracies, modern municipal law, feudal monarchy, military formation, fictional government |
| Crisis/hazard/program | Candidate cause/effect channels and acceptance questions | Triggered hazard/process models, event sequencing, finite resources | Apocalypse scenario, radiation doses, infection dynamics, extraterrestrial events |
| Competition activity | Event equipment/venue, format taxonomy only if adopted | **Core competitions** organizer/eligibility/results/record mechanisms, genre performance | Gladiatorial rules and historical institutions, sport rules, fantasy tournaments, space racing |

### §24A. Physical weapon-parent and action-mode compatibility matrix

**22 parent-to-mode relations; zero new physical inventory items.** Each canonical family reference below already exists in the retained v3.1 registry. The standalone candidate typed references appear only in the crosswalk as inactive historical proposals. Mode selectors can be `null` for a single-mode family; no additional action is granted.

| Original parent | Existing canonical family | Source attack-mode IDs (selectors) |
|---|---|---|
| `WPN-M-002` | `SCL:PBC-WPN-FL-WPN-M-002@0.2` | WPN-M-002 (default) |
| `WPN-M-003` | `SCL:PBC-WPN-FL-WPN-M-003@0.2` | WPN-M-003 (default) |
| `WPN-M-004` | `SCL:PBC-WPN-FL-WPN-M-004@0.2` | WPN-M-004A (`modes.thrust`), WPN-M-004B (`modes.cut`) |
| `WPN-M-005` | `SCL:PBC-WPN-FL-WPN-M-005@0.2` | WPN-M-005A (`modes.cut`), WPN-M-005B (`modes.thrust`) |
| `WPN-M-006` | `SCL:PBC-WPN-FL-WPN-M-006@0.2` | WPN-M-006A (`modes.cut`), WPN-M-006B (`modes.thrust`) |
| `WPN-M-007` | `SCL:PBC-WPN-FL-WPN-M-007@0.2` | WPN-M-007A (`modes.cut`), WPN-M-007B (`modes.thrust`) |
| `WPN-M-008` | `SCL:PBC-WPN-FL-WPN-M-008@0.2` | WPN-M-008A (`modes.cut`), WPN-M-008B (`modes.thrust`) |
| `WPN-M-009` | `SCL:PBC-WPN-FL-WPN-M-009@0.2` | WPN-M-009 (default) |
| `WPN-M-010` | `SCL:PBC-WPN-FL-WPN-M-010@0.2` | WPN-M-010 (default) |
| `WPN-M-011` | `SCL:PBC-WPN-FL-WPN-M-011@0.2` | WPN-M-011 (default) |
| `WPN-M-012` | `SCL:PBC-WPN-FL-WPN-M-012@0.2` | WPN-M-012A (`modes.face`), WPN-M-012B (`modes.pick`) |
| `WPN-M-013` | `SCL:PBC-WPN-FL-WPN-M-013@0.2` | WPN-M-013 (default) |
| `WPN-M-014` | `SCL:PBC-WPN-FL-WPN-M-014@0.2` | WPN-M-014 (default) |
| `WPN-M-015` | `SCL:PBC-WPN-FL-WPN-M-015@0.2` | WPN-M-015A (`modes.edge`), WPN-M-015B (`modes.spike`), WPN-M-015C (`modes.hammer`) |
| `WPN-R-001` | `SCL:PBC-WPN-FL-WPN-R-001@0.2` | WPN-R-001 (default) |
| `WPN-R-002` | `SCL:PBC-WPN-FL-WPN-R-002@0.2` | WPN-R-002 (default) |
| `WPN-R-003` | `SCL:PBC-WPN-FL-WPN-R-003@0.2` | WPN-R-003 (default) |
| `WPN-R-004` | `SCL:PBC-WPN-FL-WPN-R-004@0.2` | WPN-R-004 (default) |
| `WPN-R-005` | `SCL:PBC-WPN-FL-WPN-R-005@0.2` | WPN-R-005 (default) |
| `WPN-R-006` | `SCL:PBC-WPN-FL-WPN-R-006@0.2` | WPN-R-006 (default) |
| `WPN-R-007` | `SCL:PBC-WPN-FL-WPN-R-007@0.2` | WPN-R-007 (default) |
| `WPN-R-008` | `SCL:PBC-WPN-FL-WPN-R-008@0.2` | WPN-R-008 (default) |

**Thrown objects and launcher/ammunition:** A physically thrown knife or javelin changes location, not item count; recovery changes actual custody once. Launchers consume or release separately existing compatible ammunition where required. No mode reference creates an extra thrown object or an extra attack. `WPN-M-001` has no physical parent and no inventory record.


### §24B. Composite facilities and legal/type boundaries

- **Workshop:** `SITE-017` is a site archetype; `EQP-SHOP-001` is actual tooling/configuration. A shop with one lathe has one lathe and one finite work allocation even when both facets are referenced.
- **Cold chain:** `SITE-018` + `STO-006` + `EQP-COLD-001` + `SVC-COLD-001` are site/storage/hardware/service facets of actual installations. Their combination does not duplicate goods, volume, power, or achieved temperature. Temperature has a real time-dependent model if decisions require it.
- **Electricity:** `EQP-PWR-001` may be physically present and running without a functioning downstream connection. Fuel debit, generated energy, heat/exhaust and delivered service are distinct supported facts.
- **Knowledge:** `RES-KNW-001/002` remain information content per v3.1; a physical manual (if separately present) is an asset, not expertise, successful research or institution-wide knowledge.
- **Mobile loader:** `EQP-HND-002` remains vehicle-class equipment per v3.1; possession never grants an operator, route, fuel, lifting performance or legal eligibility.
- **Composite protection:** `ARM-006` and its constituent materials/coverage never sum multiple full protection ratings for the same effect.
- **Institution/competitions:** `INST` describes content, not automatically held legal authority. The v3.1 judged craft exhibition remains a COMP template, not a sport/genre rule or automatically scored event.

These are anti-double-counting **contracts**, not a new mechanic or inventory ledger.

## 25. Scoped adapter record and examples

```yaml
adapter_id: 'FL-1.0:WPN-M-006A'
implements: 'SCL:PBC-WPN-FL-WPN-M-006@0.2'
selector: 'modes.cut'
owner: 'Core Fantasy World Engine / Fantasy Content Libraries'
resolution_owner: 'Fantasy weapon and protection system'
assumptions: ['compatible humanoid usage', 'enabled physical blade technology']
requirements: ['usable blade', 'feasible reach', 'free/functional grip']
mechanics:
  threat: 2            # inherited Fantasy value; NOT universal
  armor_defeat: 1      # inherited Fantasy value; NOT universal
  reach_profile: '1–2' # inherited Fantasy rating; NOT universal
  mode: 'Cut'
source: 'FA-LIB §7 WPN-M-006A'
status: 'illustrative bridge; no campaign migrated'
```

**Worked example:** A Roman iron blade, a medieval steel sword, and a hypothetical advanced-material sword may inherit `SCL:WPN-M-006A/B` *only when their usable constructions genuinely support the corresponding modes*. The Roman campaign selects dated availability and a legal/quality profile; Fantasy applies its combat numbers; a speculative campaign defines its own adapter. They never use a shared universal "Sword 2 damage" entry. A sword with a damaged edge can retain a thrust mode without gaining any new item or free attack.

**Second example:** `SCL:EQP-PWR-001` identifies a combustion generator. A functioning modern disaster site may possess an actual 5 kW-rated generator only if the campaign establishes that rating and the instance. A medieval campaign does not gain one. A space campaign might use the same archetype for a compatible backup unit, but power, heat, exhaust, atmosphere and local load-network restrictions still apply. The equipment template does not confer usable electricity without fuel, connection and operation.

**Third example:** `SCL:BODY-002` may describe a horse, ox, wolf or fictional quadruped, but not dictate their individual behaviour, gait performance, diet, lifespan, training or capacity. A pack animal's actual location and feed are tracked once, and its tack is separate equipment. Fantasy's damage-location table remains its own adapter.

## 26. Genre residual-library specifications

| Existing library / engine | Sections eligible for **proposed shared import** | Must be retained as specialized references | Result after *explicit* migration |
|---|---|---|---|
| Fantasy Content Libraries v1.0 | Mundane weapon identities/modes, armor constructions, shield types, materials, body-plan and natural-action/creature archetype identities | Numeric weapon/armor/shield tables and trait effects; range/reload; supernatural `PAR` paradigms; `XMAT` extraordinary effects; theme-specific species/statistics; campaign profile | Thin Fantasy compatibility adapter + supernatural and fantasy-specific content |
| Post-Apocalyptic Content Libraries v1.0 | Ordinary resources, storage, tools, site, service/continuity, habitation, population/institution/network, program, hazard, ordinary disruption templates | Crisis-specific `APX-X01`; scenario stock distributions, salvage circumstances, depletion, reconstruction/PAF rules, specific hazards/effects and PA campaign profile | Thin PAF-compatible reference to SCL + disaster/theme specializations |
| Military Equipment and Technology Library v0.1 | Broad twelve-category tags, six era browse tags, reusable general material and equipment references | Era/region actual eligibility, military issue and loadouts, military platform models, weapon caliber/munition and engineering ratings, doctrine | Military specialization and era-specific model catalogue, not a duplicate generic object index |
| Military Life Simulation Engine v0.4 | Interface to common asset/maintenance/stock entries | Service agreements, command, military training, discipline, deployment, support and life details | Reuses SCL types through its existing Core owners |
| Roman Republic Life Simulation Engine v1.0 | Shared physical materials, sword/shield/clothing, tools, animals, institutions as *functions* | Dated Roman culture, legal relations, currency, gladiatorial arrangements, source-supported technology and geography | Historical selector/adapter, no silent modern or fantasy equipment |
| Space Exploration and Colonization Foundation v0.1 | Generic goods, life-support equipment *components*, handling tools, sites, services, networks and habitats where physically compatible | `SPACE-LIB` flight/mission hardware, pressure/thermal/EVA/flight parameters, trajectory and communications models, colonization procedures | Space-specific module points to shared generic assets without losing special models |
| SSN Working Playtest R0.1 | **None automatically** | Whole SSN internal stat/dice/chakra/jutsu and content canon | No change; separate future opt-in translation if explicitly requested |

**Special retention note:** Military's source *index* is not a completed equipment encyclopedia. Do not "slim" the original by pretending named weapons, individual aircraft, ships, historical armors or specialist devices already have calibrated shared definitions. Future entries can be authored once into SCL with explicit localized profiles.

---

## 29. Migration procedure — prospective only

For this v1.0 catalogue release, use the normative external `IRGS_Shared_Content_Registry_v1_0.json` with the exact unchanged `@0.2` family references and aliases. The following original v0.1 migration plan is retained as provenance; no phase here adopts a campaign or assigns global canonical IDs.

1. **Freeze source versions and campaign interfaces.** Record active Core, genre library versions, overrides, live campaign states and each referenced entry ID. Unresolved sources remain named as such.
2. **Compare references bidirectionally.** Inventory every imported old ID and every outgoing genre definition. Classify unchanged meaning, split, merged alias, conditional, excluded or incompatible. If a source definition contains numbers, isolate that numeric profile as an adapter instead of deleting it.
3. **Publish and accept shared definitions as an independent library.** Acceptance requires a user decision; this v0.1 document is a proposal.
4. **Create genre adapters referencing exact SCL entry versions.** Never apply numeric traits twice or let two genre libraries own the same stock/service.
5. **Slim the original libraries** only after a complete entry-by-entry crosswalk and regression comparison. Replace repeated generic definitions with pointers; retain unique specialized mechanics, examples, compatibility constraints, profile forms and exclusions.
6. **Select campaign migration scope and effective time.** Existing campaign gear/persons/structures retain their actual quantities, condition, ownership, locations, provenance and previous outcomes. Migration does not provide lost goods, repair damage or retcon earlier events.
7. **Validate at multiple scales.** Re-run accepted fixtures and material/compatibility checks; audit unconverted references, double costs, missing functions and unexpected access to new technology. Record results and revisions as **scripted checks** or **playtests**, never confuse them.

### 29.1 Legacy ID mapping rule

For imported rows in Parts II–VII, the mapping is **total and deterministic** by original family: `PA-LIB:<original ID> → proposed SCL:<original ID>@0.1` for `RES/STO/EQP/SITE/SVC/WRK/HAB/POP/INST/NET/RCN/HAZ` and ordinary `APX-001..012`; `FA-LIB:<original ID> → proposed SCL:<original ID>@0.1` for `MAT/WPN-M/WPN-R/ARM/SHD/COV/BODY/NAT/CRT`. Existing numeric fields remain under `FA-LIB` and must not be copied into the neutral entry. `MIL-INDEX` `ERA` and category tags become **catalogue tags**, not inventory records. Excluded objects/templates and special overrides are listed in §28. If the source includes a mode suffix `A/B/C`, preserve it and its shared parent.

**No ownership migration is executed by this document.** The v1.0 catalogue release preserves the v0.2 release mappings and supersedes only the original untyped v0.1 proposal within this catalogue; exact source identities and selectors remain pinned. The mapping is a proposal for downstream tool/genre-library rewrites, not a current broken reference alias.

## 30. Acceptance and regression cases

| Test ID | Situation | Required result |
|---|---|---|
| SCL-01 | Two genres reference same mundane sword | One shared identity/mode family; separate calibrated adapters; no shared Threat value |
| SCL-02 | Fantasy sword cut and sword thrust both known | One actual sword, two attack modes; ammunition/attacks/ownership are not duplicated |
| SCL-03 | Shield material is strong and workmanship is excellent | Construction, quality, condition and coverage assessed separately; no counted-twice defense |
| SCL-04 | A manual is found in a warehouse | Physical documentation obtained if present; information must be read/accessed; no automatic expertise |
| SCL-05 | Potable water stored in an unsafe tank | Actual water quantity persists; usability changes only via supported contamination/exposure |
| SCL-06 | Two pumps feed one water service | Equipment capacity and link losses govern delivered throughput; neither equipment nor service creates water |
| SCL-07 | Generator runs but power cable is missing | Fuel use and local generator operation may occur; downstream service remains unavailable |
| SCL-08 | Cold storage loses electrical power | Time/thermal process begins; stock does not spoil all at once absent applicable thresholds |
| SCL-09 | Hospital site exists but no medics or medicines | Building still exists; no unsupported healthcare service capacity |
| SCL-10 | Warehouse archetype selected during search | No goods spontaneously instantiate or become visible; actual history controls contents |
| SCL-11 | Mixed salvage is designated structural steel | Sorting/processing/testing and stock conversion required; no free ready-to-build metal |
| SCL-12 | New settlers arrive at city gates | Population count, care demand, property and status remain distinct; presence not instant citizenship or labor |
| SCL-13 | Institution created without staff or authority | Registry/template alone cannot carry out policy or produce services |
| SCL-14 | Shipment scheduled across map | No destination stock increase until actual physical receipt/acceptance; transit remains a location |
| SCL-15 | Hazard `HAZ-008` listed in setting | No radiation without an actual source and a selected dose/effect profile |
| SCL-16 | Extraordinary crisis `APX-X01` not enabled | No automatic mutants, magic, anomalies, infectious monsters or time loops |
| SCL-17 | Fantasy quadruped location table queried in military sim | Anatomy available; no automatic Fantasy d20 location roll outside a selected adapter |
| SCL-18 | Underwater vehicle and aircraft reference military category tags | Same broad taxonomy, but specialized flotation/flight models are needed; no free capability |
| SCL-19 | Generic settlement archetype used in Roman Republic | No modern utilities, school system, police mandate or post-apocalyptic institutions automatically enabled |
| SCL-20 | Space habitat uses generic water-storage and power entries | Gas/pressure/orbit/thermal/oxygen calculations remain Space; no refill on module transition |
| SCL-21 | One item is claimed by two genres on migration | Keep one campaign asset with one owner, actual location, condition, quantity and history; aliases only |
| SCL-22 | Old PA and Fantasy catalogues remain in live campaigns | Publication makes no changes until explicitly selected/pinned |
| SCL-23 | Name changed but original object data remain | Stable ID/alias resolves; no new asset or history overwrite |
| SCL-24 | Battle scales shift from actor to formation and back | No additional issued kit, projectiles, casualties or resources caused by catalogue aggregation |
| SCL-25 | Campaign attempts to use uncalibrated pump, aircraft or medication quantitatively | Block dependent numerical effect; allow other supported actions and require profile-specific calibration |


### Complete receiving acceptance requirements (R1-01 through R1-36)

All **36** cases from the previous standalone v1.0 candidate are carried forward below under `R1-` to avoid reusing the existing v3.1 `SCL-01..25` meanings. They are requirements, not assertions of real campaign execution.

| Merged case ID (standalone origin) | Trigger | Required result |
|---|---|---|
| `R1-01` (`SCL-01`) | All source entries indexed | Exactly 191 PA table rows + 81 FA table rows + 14 FA prose templates; all 286 retain typed references and source pointers |
| `R1-02` (`SCL-02`) | Physical weapon-parent normalization | 22 tangible parent records; 31 attack-mode descriptions; no owned `WPN-M-001` unarmed inventory object |
| `R1-03` (`SCL-03`) | Source ID collides as weapon item/mode name | Different typed canonical references; composite legacy source maps to roles, not two items |
| `R1-04` (`SCL-04`) | Sword cut/thrust | One physical owner/location/condition; two selectable lawful modes without duplicate action or resources |
| `R1-05` (`SCL-05`) | Throw a knife, recover it | Item relocates through Core; no consumed duplicate projectile stock or new knife on retrieval |
| `R1-06` (`SCL-06`) | Bow/launcher has no ammunition | No shot created; launcher ownership preserved; actual ammunition needed |
| `R1-07` (`SCL-07`) | PA and FA name an ordinary tool identically | Compare actual meaning and provenance; only unify on supported equivalence, not string similarity |
| `R1-08` (`SCL-08`) | Upgrade modern site label in Roman game | No electricity/refrigeration/pharmaceuticals by label; explicit era/variant profile required |
| `R1-09` (`SCL-09`) | `MAT-010`, steel, structural stock | Classification and grade may overlap; exactly one substance/lot with accepted specification; no multiplied mass/protection |
| `R1-10` (`SCL-10`) | `ARM-006` over padded/mail | Use adopted composite armor profile once; no second full protection bonus from constituent layer labels |
| `R1-11` (`SCL-11`) | Shield and suit both present | Physical shield separate asset and coverage/orientation; no permanent body-wide shield effect |
| `R1-12` (`SCL-12`) | `SITE-017` + `EQP-SHOP-001` | One actual workshop and tooling capacity; source location separate from repair capability |
| `R1-13` (`SCL-13`) | Cold storage triad | Same equipment/storage/service facets do not multiply physical storage, stock or cooling power |
| `R1-14` (`SCL-14`) | Pump by lake but no operator/power/connection | Does not generate clean water or delivered service; item still exists |
| `R1-15` (`SCL-15`) | Generator disconnected or exhaust unsafe | Installed machine remains; no invented usable downstream electricity; actual risks only through cause/trigger |
| `R1-16` (`SCL-16`) | Documentation acquired | Physical document custody changes; knowledge acquisition, expertise and legal right remain independent |
| `R1-17` (`SCL-17`) | Drug/chemical/spare part family selected | No actual substitute dose/chemical/compatible part until a specific variant and stock lot established |
| `R1-18` (`SCL-18`) | Existing settlement selects HAB/POP entries | No extra residents, entitlement, shelter supplies, jobs or automatically filled beds |
| `R1-19` (`SCL-19`) | Institutional role template enabled | Does not create staff, powers, votes, legal capacity or enforceable orders |
| `R1-20` (`SCL-20`) | Shipment appears on a NET-F flow map | Manifest is not delivery; actual transit and acceptance required; no stock duplication |
| `R1-21` (`SCL-21`) | RCN program listed | No funds, work completed, production or commissioned services from template alone |
| `R1-22` (`SCL-22`) | Fire, illness or radiation HAZ added | No exposure without source, connection, time/intensity and applicable effect model |
| `R1-23` (`SCL-23`) | APX war/pandemic pattern selected | Does not automatically declare a war/disease/casualties/global collapse |
| `R1-24` (`SCL-24`) | Extraordinary APX-X01/PAR/XMAT not enabled | No supernatural or theme effects created by common library |
| `R1-25` (`SCL-25`) | Aircraft, ship, craft or habitat listed | No flight, buoyancy, gravity, pressure, FTL, safe oxygen or launch without relevant specialized model |
| `R1-26` (`SCL-26`) | Core competition venue template present | No universal scoring/eligibility/results; Core competition and sport/activity owner decide |
| `R1-27` (`SCL-27`) | Unit scale ↔ actor scale | One physical roster, equipment, ammunition and consumed stock; no resources or skills appear from projection |
| `R1-28` (`SCL-28`) | Simultaneous service draws on one fuel lot | Source reservation/commit policy governs; no secondary local fuel counter or double-debit |
| `R1-29` (`SCL-29`) | Source PA/FA status varied | Preserve each source status and separate SCL adoption status, never convert proposal to tested standard |
| `R1-30` (`SCL-30`) | Legacy 0.1 alias and 1.0 typed ID | Resolve through reviewed mapping, never blind textual replacement or two canonical targets for a single type use |
| `R1-31` (`SCL-31`) | Existing live campaign on old library | Publication changes nothing; migration requires explicit authority and tested prospective cutover |
| `R1-32` (`SCL-32`) | A Core release other than the verified v3.1 becomes selected | Require a new versioned interface/owner audit before use; the historical premise that v3.1 was unavailable is superseded by its inspected source. |
| `R1-33` (`SCL-33`) | Unknown pump throughput while qualitative search underway | Numeric dependent calculation blocked; unrelated supported actions continue without filler rates |
| `R1-34` (`SCL-34`) | Material transferred and later recovered after report | Exactly one actual stock transfer, one observation/report of it; no duplicate loss/recovery |
| `R1-35` (`SCL-35`) | One skilled crew member assigned to two simultaneous jobs | Work assignment cannot grant duplicate worker hours; actual time and authorization limit both |
| `R1-36` (`SCL-36`) | Cancel or replace a proposed version | Only reference-mapping/configuration changes; no retcon, refund or reset of in-world state |

**Interpretation:** `R1-02` counts 31 original weapon/method rows as 30 physical modes plus the single unarmed method; it does not claim 31 physical modes. `R1-32` has been updated to reflect the now-inspected Core v3.2 while preserving the original wording in the packaged standalone source.

All `SCL-01..25` from the confirmed v3.1 catalogue remain as originally specified above. Executed machine checks and synthetic fixtures are reported separately; specifying 61 cases does **not** mean 61 gameplay tests passed.

## 31. Calibration and remaining work

To turn an archetype into executable model content, record **unit**, supported range, provenance, technology/setting eligibility, dependencies, assumptions, tolerances, source quality, uncertainty, replenishment/decay, thresholds, maintenance, failure mode, and cross-system effect precedence. Choose numbers only where decisions require them, from an adopted source or an explicitly labeled provisional fixture. Required modules include: (a) physical grades/processing/mass and load, (b) item/weapon range and effects, (c) storage decay and environmental hazards, (d) installed service/power/transport throughput, (e) organism nutrition/injury/biological rates, (f) site and demographic variation, (g) qualified labor/project rates, (h) historical/setting technology gates and costs, and (i) cross-genre adapter conflict controls.

**Known risks:** broad IDs such as `RES-MED-001` cannot replace actual drug/chemical identity; the Fantasy mode/weapon split may require separate parent object IDs for clean inventory implementations; site archetypes should be omitted from generation if historical contents are already known; numerical Fantasy weapon/protection tables are still coupled to their own engine and cannot be deleted without compatibility pointers; Space's `SPACE-LIB` includes specialist content whose shared generic component needs a separate design pass rather than a wholesale import.

**Validation status:** this is a *document/source consolidation*. The source content was inventoried and its old IDs enumerated. That is not balanced gameplay, statistical calibration, real engineering or historical research. After acceptance, separately run automated schema/reference checks and controlled cross-engine playtest fixtures against the real simulation runtime.

