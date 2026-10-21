# Interactive Roleplaying Game System
# Post-Apocalyptic Content Library — v2.0
**Document ID:** `IRGS-PACL-2.0`  
**Date:** 14 October 2026  
**Status:** Proposed genre library / complete CMRR resubmission; structurally verified, not live playtested or calibrated  
**Content parent:** `IRGS-SCL-1.0`, immutable family references `@0.2`  
**Core interface:** `IRGS-CORE-3.2` and its `APOCALYPTIC` receiving binding  
**Genre authority:** `IRGS-PAF` v2.0 source revision 2 (pinned to Core v3.1). Compatibility bridge to 3.2 is proposed here; it is not an automatic genre-engine rebind.  
**Predecessor:** Post-Apocalyptic Content Libraries v1.0 (PA-LIB / PL-1.0). Original source included as provenance.  
**Purpose:** Crisis-specific content compositions that interpret historical disruption, emergency use and reconstruction while inheriting generic objects, services and procedures rather than copying them.

---

## 1. Scope, ownership, authority and status
Content is not world state. This library supplies selectable **PA-specific configurations and assessment triggers**, not newly spawned people, supplies, workshops, salvage, disasters, injuries, crises or institutions. Generic content definitions live in Shared Content Library v1.0. Core v3.2 alone owns agency, causality, time, actors, assets, stock, services, projects, information, institutions, and events. PAF v2.0 owns only its thirteen assessment overlays and the genre-specific interpretation of disruption relative to a documented prior order.
Authority: explicit current user direction → established campaign overrides → adopted genre foundation → adopted Core → temporary scoped proposal where no rule applies. An entry drafted here is not thereby adopted, calibrated, enabled, or spawned. Source facts, interpretations, proposals and any external research remain distinct. No external research or invented physical rates were introduced.
The earlier **PAF v2.0 source revision 2 remains pinned to Core 3.1 / SCL 0.2**. Core 3.2 already provides an `APOCALYPTIC` receiving contract referring to `PL-1.0` and SCL 1.0. This library uses that available interface for proposed forward compatibility, but does not silently rewrite PAF, deprecate PL or migrate a campaign. A selected deployment must explicitly approve this bridge, pin versions and execute relevant behavior gates.

### 1.1 Inheritance chain
`SCL family@0.2 + original PL payload when held → PA content composition (optional) → theme/cause-specific module and setting variant → campaign-selected profile → actual Core-owned instance → PAF read-only assessment`
Examples: the shared generator is a real equipment type; a crisis-linked generator-relief configuration is PA content; an enabled electricity/fuel specification determines actual output; the campaign owns a particular generator, its fuel and consumers. The PA overlay records what former service it replaces, without debiting fuel itself.
### 1.2 Namespaces and prerequisites
| Namespace | Role | Can instantiate itself? |
|---|---|---|
| `SCL:PBC-...@0.2` | Canonical generic content identity and source/adapter gates | No |
| `PL:<legacy>@1.0` | Original PA library source alias; original payload retained | No |
| `PA-CNT-*` | New proposed composition/variant schema; not SCL canonical | No |
| `APX-*` | Legacy crisis-cause profile selectors | No; cause requires module/profile/state |
| `PA.*` | Genre assessment overlay attached to real Core facts | No physical writes |
| `CPF-PA-BASE` | Legacy campaign profile extension | No |
Do not infer numerical effectiveness, availability, legal rights, generic disaster stage or setting lore from a selector. A held SCL family retains its exact native payload and profile dependency. Even a selected qualitative SCL definition does not supply absent operational numbers.

## 2. Reconciliation of the original catalogue
The original PL-1.0 contains **193 registered entry IDs**: **191 SCL-family bindings** and **two scoped extensions** (`APX-X01`, `CPF-PA-BASE`). The family bindings include **39 selected qualitative** and **152 held source-backed** entries. Every old entry is mapped in `PA_Legacy_to_SCL_Crosswalk_v2_0.csv` with its original payload reference, target revision, selector and activation/readiness gate. None is renamed to an invented `@1.0` family revision.
The 12 mundane `APX-001..012` are catalogued as generic crisis-content families in SCL with their source-backed limitations. They remain useful as **PA setting/cause selectors**; their existence creates neither an active crisis nor its numerical propagation. `APX-X01` and `CPF-PA-BASE` remain scoped extensions, never flattened into universal Core.
### 2.1 What was relocated instead of copied
| Original PL families | Present owner | Post-Apocalyptic specialization retained |
|---|---|---|
| `RES` (24) | SCL definition + Core operating owners | Inherited-stock history, usability and future support |
| `STO` (9) | SCL definition + Core operating owners | Lost storage dependencies and buffer assessment |
| `EQP` (21) | SCL definition + Core operating owners | Scavenging/cannibalization/field operation variants |
| `SITE` (23) | SCL definition + Core operating owners | Former purpose, surveyed zones, access and depletion history |
| `SVC` (16) | SCL definition + Core operating owners | Previously normal delivery interrupted and temporary substitutes |
| `WRK` (12) | SCL definition + Core operating owners | Emergency deployment and crisis response posture |
| `HAB` (8) | SCL definition + Core operating owners | Refuge status, temporary/durable conversion |
| `POP` (7) | SCL definition + Core operating owners | Crisis-linked displacement and intake concerns |
| `INST` (13) | SCL definition + Core operating owners | Continuity, fracture and contested predecessor claims |
| `NET` (19) | SCL definition + Core operating owners | Partition, isolation and route rejoining |
| `RCN` (15) | SCL definition + Core operating owners | Repair/restore/replace/adapt/redesign/abandon transition from prior function |
| `HAZ` (12) | SCL definition + Core operating owners | Crisis source relationship, actual exposure and response module selection |
| `APX` (13) | SCL definition + Core operating owners | Cause/module selection and uneven regional impact |
The original library’s generic construction explanations, inventory rules and tests are inherited **by reference**, not deleted. They remain in the provenance source and registry. A complete source-section disposition for all 54 sections is supplied separately.

## 3. Native content and instance contract
Every PA composition uses: `ID | proposed status | inherited exact PL/SCL refs + selectors | permitted theme/setting | historical baseline | relevant PA overlay refs | trigger | Core facts read | eligible variant/prerequisites | source profile + operating envelope | consumption/transfer effects (Core requests only) | actor knowledge and authority | limits/unknowns | acceptance evidence | version and migration impact`.
The composition cannot become an independent source of physical stock, capability, injury, work progress, fertility, authority, population or actual location. Effects occur only through selected Core/module procedures. A PAF assessment is a view and reference graph. Duplicate report delivery changes no real quantity.
### 3.1 Actual activation sequence
1. Resolve the exact SCL/PL family, selector, semantic type and source payload/checksum; reject ambiguous or wrong-version lookups.
2. Verify selected/held/scoped status and the native model. Held entries cannot be promoted by this document.
3. Verify setting eligibility, source/cause, technology, site, ownership, valid operator, activity/method and genuine inputs.
4. Select applicable cause, exposure, service, physiology, equipment and support models; record units, bounds, uncertainty and provenance.
5. Initialize or attach only actual Core-owned things/events with authorization; create PA overlays only when decision-relevant.
6. At actual triggers, evaluate Core changes, then update read-only PA assessments and knowledge by receipt time.
7. Preserve version, source status, quantities, history, hidden information and pending events over time/scale changes.

## 4. Shared material/resource and asset compatibility
The original `RES`, `STO`, `EQP` and `SITE` entries are referenced through their shared families rather than redefined. The following distinctions are mandatory:
- **Physical quantity versus usability:** A contaminated water lot remains material; potability changes only through established chemistry/assessment. An expiring medication is a specific identity, dose, storage and indication problem, not a generic medicine pool.
- **Information versus copies:** `RES-KNW-001/002` refer to document media and their informational content; owning a binder neither provides expertise nor creates a second mutable information ledger.
- **Installed capital versus salvage:** Taking a component changes the donor equipment; acceptance and transport determine whether a new useful component exists at its destination.
- **Condition versus quality:** A good machine can be worn; a repaired low-grade machine is not automatically premium grade. Damage, repair and maintenance remain linked to actual components.
- **Storage versus stock and service:** A reservoir is not potable water; cold-room volume is not refrigerated function without power and thermal limits. Inventory in transit is neither present at origin nor at destination.
- **Legal status versus physical access:** A scavenger’s control of a site does not erase ownership, state claims or nearby residents. Institutional decisions follow actual setting processes.

## 5. Historical legacy and salvage composition library (`PA-CNT-LEG`)
Purpose: represent what a functioning prior society left behind, what happened during crisis, and what remains physically accessible and supportable. No procedural loot roll, respawning cache, or universal decay is defined. A successful search changes what the actor detects/retrieves from an already supported site state. A novel room remains unobserved until surveyed.
### PA-CNT-LEG-001 — Abandoned retail recovery survey
**Inherits:** `SITE-002`, `RES-FOOD-001`, `RES-FOOD-002` (resolve via exact crosswalk). **PA views:** `PA.LegacySite`. **Status:** Proposed composition.
**Trigger:** Survey request at formerly active store. **Record:** Previous opening hours/use; closure history; accessed rooms; surveyed zones; observed food lots; theft/spoilage evidence.
**Core result:** Refer to Core discovery and K-STOCK; no loot generation. **Qualification gate:** Actual site access, inventory and storage/exposure profile.
**Acceptance:** Repeat visit to cleared aisles cannot renew food; previously unsearched freezer remains an unknown region.

### PA-CNT-LEG-002 — Pharmacy inventory and cold-chain history
**Inherits:** `SITE-003`, `RES-MED-002`, `STO-007` (resolve via exact crosswalk). **PA views:** `PA.LegacySite`, `PA.LegacyDependency`. **Status:** Proposed composition.
**Trigger:** Former pharmacy assessed. **Record:** Medicine identity and batch; storage time/temperature evidence; access and custodial claims; compatible care profile.
**Core result:** Existing drugs keep quantity with separate suitability/knowledge assessments. **Qualification gate:** Qualified medical assessment; specific storage/indication profile.
**Acceptance:** An unlabeled bottle cannot become generic healing points.

### PA-CNT-LEG-003 — Fuel depot salvage and pumping
**Inherits:** `SITE-006`, `STO-004`, `RES-FUEL-002` (resolve via exact crosswalk). **PA views:** `PA.LegacySite`, `PA.LegacyDependency`. **Status:** Proposed composition.
**Trigger:** Pump/stock condition inspected. **Record:** Existing fuel lot, grade and custody; transfer pump, power, fittings; site control and history.
**Core result:** Only transferred actual fuel enters handling/transit record. **Qualification gate:** Specific fuel quality, safe transfer, available equipment and transport.
**Acceptance:** Powerless station with fuel underground cannot yield delivered fuel without transfer capability.

### PA-CNT-LEG-004 — Installed machinery salvage versus donor function
**Inherits:** `SITE-011`, `EQP-SHOP-001`, `RES-IND-001` (resolve via exact crosswalk). **PA views:** `PA.LegacySite`, `PA.LegacyDependency`. **Status:** Proposed composition.
**Trigger:** Machine cannibalization proposed. **Record:** Donor machine id and component; removed assembly; recipient support; lost donor operation.
**Core result:** Core debit/credit of component and condition/function of donor. **Qualification gate:** Physical access, tooling, qualified labor, component compatibility.
**Acceptance:** Removing the final serviceable controller disables donor operation; does not mint two controllers.

### PA-CNT-LEG-005 — Unknown substructure in searched site
**Inherits:** `SITE-001`, `RES-KNW-002` (resolve via exact crosswalk). **PA views:** `PA.LegacySite`. **Status:** Proposed composition.
**Trigger:** Partial building survey. **Record:** Search coverage, observer access, structural constraints, source maps/uncertainty.
**Core result:** Discovery changes K-INFO; no quantity until established. **Qualification gate:** Access, survey method and hidden-state persistence.
**Acceptance:** Cleared ground floor does not declare unseen basement empty or full.

### PA-CNT-LEG-006 — Recovered document and lost know-how
**Inherits:** `RES-KNW-001`, `SITE-011` (resolve via exact crosswalk). **PA views:** `PA.LegacyDependency`. **Status:** Proposed composition.
**Trigger:** Manual or plans recovered. **Record:** Artifact custody/location; information visibility; language; training/work instructions; personnel competence.
**Core result:** Core receives documents and information, not instant expertise. **Qualification gate:** Readable medium, actual study/training, equipment access.
**Acceptance:** Recovered manual alone cannot commission complex apparatus.

### PA-CNT-LEG-007 — Contaminated inherited potable-water lot
**Inherits:** `RES-WAT-001`, `RES-WAT-002`, `HAZ-005` (resolve via exact crosswalk). **PA views:** `PA.LegacySite`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Evidence of contamination in reserve. **Record:** Lot amount; test evidence; contamination state; drinking suitability; alternate stock.
**Core result:** Quantity persists; qualifying usable potable quantity may fall. **Qualification gate:** Contaminant profile, test validity, treatment and monitoring.
**Acceptance:** One hundred liters can remain physically present yet be unavailable as potable service.

### PA-CNT-LEG-008 — Long-term unreplaceable control component
**Inherits:** `RES-IND-002`, `EQP-PWR-001` (resolve via exact crosswalk). **PA views:** `PA.LegacyDependency`. **Status:** Proposed composition.
**Trigger:** Support/parts assessment changed. **Record:** Current operating state; existing spares; diagnostics; manufacturing capability; imports; forecast horizon.
**Core result:** Future support warning; no immediate fabricated component failure. **Qualification gate:** Actual spare specification, qualified maintenance and replenishment evidence.
**Acceptance:** Running generator keeps running while unsupported component reproduction remains unresolved.


## 6. Emergency continuity and disrupted provision (`PA-CNT-PRV`)
These are crisis-specific arrangements built from shared equipment, support services and real time/resources. Temporary continuity can succeed; it is not automatically inferior or guaranteed to degrade. No separate rationing economy or resilience meter exists.
### PA-CNT-PRV-001 — Emergency potable-water distribution point
**Inherits:** `WRK-WAT-001`, `RES-WAT-001`, `STO-003` (resolve via exact crosswalk). **PA views:** `PA.DisruptedProvision`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Ordinary mains are disrupted. **Record:** Consumers, real accessible reserve/source, intake/replenishment, bottlenecks and allocation authority.
**Core result:** Actual delivery transfers water from source through transit/receipts. **Qualification gate:** Water standard, routes/handling, personnel, timing and storage.
**Acceptance:** Road convoy dispatched, receiving water does not appear until arrival and unloading.

### PA-CNT-PRV-002 — Gravity-buffered urban water continuity
**Inherits:** `WRK-WAT-002`, `SVC-WAT-001` (resolve via exact crosswalk). **PA views:** `PA.DisruptedProvision`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Powered pumping interrupted. **Record:** Tank amount, height/flow connection, demand and repair schedule.
**Core result:** Core service forecast reflects buffer; no automatic immediate interruption. **Qualification gate:** Known hydraulic envelope and quality.
**Acceptance:** Pump shuts off; gravity tank still supplies supported users during remaining actual buffer.

### PA-CNT-PRV-003 — Temporary generating supply prioritization
**Inherits:** `WRK-PWR-001`, `EQP-PWR-001`, `SVC-PWR-001` (resolve via exact crosswalk). **PA views:** `PA.Disruption`, `PA.DisruptedProvision`. **Status:** Proposed composition.
**Trigger:** Emergency power activated. **Record:** Fuel, safe generator connection, voltage/load, critical endpoints, operating shifts.
**Core result:** Core allocates one finite output and fuel quantity to actual recipients. **Qualification gate:** Complete generator envelope and compatible distribution.
**Acceptance:** Ten usable units cannot deliver two simultaneous indivisible six-unit services.

### PA-CNT-PRV-004 — Battery-only emergency communications
**Inherits:** `WRK-PWR-002`, `SVC-COM-001`, `EQP-COM-001` (resolve via exact crosswalk). **PA views:** `PA.DisruptedProvision`. **Status:** Proposed composition.
**Trigger:** Primary power lost. **Record:** Charge, discharge bound, radio endpoints, receiving capability and duty schedule.
**Core result:** Actual operating runtime depends on stock/state; messages separate from device condition. **Qualification gate:** Power and link profile, qualified use.
**Acceptance:** Battery expires but already-sent message does not vanish from recipient knowledge.

### PA-CNT-PRV-005 — Emergency feeding point
**Inherits:** `WRK-FOOD-001`, `RES-FOOD-001`, `RES-WAT-001` (resolve via exact crosswalk). **PA views:** `PA.DisruptedProvision`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Central meal service activated. **Record:** Food lots/ownership; potable water; cooking inputs; operators; serving and waste routes.
**Core result:** Meals produced from actual input lots by Core service/work. **Qualification gate:** Menu-specific needs, hygiene, staffing and equipment.
**Acceptance:** Serving 40 meals reduces available ingredients and does not manufacture nutrition.

### PA-CNT-PRV-006 — Temporary healthcare provision
**Inherits:** `WRK-MED-001`, `EQP-MED-001`, `SVC-HEALTH-001` (resolve via exact crosswalk). **PA views:** `PA.DisruptedProvision`, `PA.RefugePosture`. **Status:** Proposed composition.
**Trigger:** Clinic opened after ordinary service interruption. **Record:** Actual practitioners, care scope, beds, equipment, pharmaceuticals, power/water.
**Core result:** Only declared qualified treatments and deliverable capacity available. **Qualification gate:** Selected MED injury/illness/treatment profiles.
**Acceptance:** An open clinic sign and medicine chest do not create a surgeon.

### PA-CNT-PRV-007 — Emergency warming center
**Inherits:** `WRK-HEAT-001`, `SVC-HEAT-001`, `EQP-TEMP-001` (resolve via exact crosswalk). **PA views:** `PA.RefugePosture`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Cold-weather shelter operating. **Record:** Heat source, safe ventilation, fuel, shelter volume, occupants, exposure.
**Core result:** Actual warmth only in supported area; survivor needs assessed through Core. **Qualification gate:** Heating envelope, fuel, building insulation, organism profile.
**Acceptance:** A heater cannot warm an unlimited population or operate without exhaust management.


## 7. Refuge, displacement and actual occupancy (`PA-CNT-REF`)
A shelter designation cannot create safety, beds, potable water, legal status or occupants. A displaced wave is a view over real movement and people, retaining in-transit care and individual property. No default policy of labor mobilization, citizenship, hostile reception or compulsory relocation is inferred.
### PA-CNT-REF-001 — Public shelter conversion
**Inherits:** `SITE-018`, `HAB-002`, `WRK-SHL-001` (resolve via exact crosswalk). **PA views:** `PA.RefugePosture`. **Status:** Proposed composition.
**Trigger:** Former civic building used for shelter. **Record:** Original function; current floor areas; actual arrivals; operators; water/sanitation; exit routes.
**Core result:** No free residents, beds, supplies or new authority. **Qualification gate:** Site capacity, emergency use permissions, service resources.
**Acceptance:** School declared refuge; inhabitants unchanged until actual arrival.

### PA-CNT-REF-002 — Moving emergency convoy
**Inherits:** `HAB-004`, `POP-002`, `SVC-ROAD-001` (resolve via exact crosswalk). **PA views:** `PA.DisplacementWave`. **Status:** Proposed composition.
**Trigger:** Displacement group departs. **Record:** Named people/cohort; vehicles; food/water; transit legs, destination forecast.
**Core result:** Core moves existing persons/assets; arrivals only on receipt. **Qualification gate:** Transport capacity, crew, fuel, route profile.
**Acceptance:** Split 120 travellers: 70 arrived and 50 transit; total 120.

### PA-CNT-REF-003 — Temporary camp on constrained services
**Inherits:** `HAB-003`, `SVC-SAN-001`, `SVC-WAT-001` (resolve via exact crosswalk). **PA views:** `PA.RefugePosture`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Camp starts operating. **Record:** People physically present; real sanitation/water service; staff, weather and supply.
**Core result:** Unmet needs remain visible; excess occupants do not disappear. **Qualification gate:** Species physiological and service throughput profiles.
**Acceptance:** Shelter holds 500 but potable water supports 300: unmet water remains.

### PA-CNT-REF-004 — Rural distributed refuge network
**Inherits:** `HAB-005`, `NET-L-002`, `SVC-HEALTH-001` (resolve via exact crosswalk). **PA views:** `PA.RefugePosture`, `PA.RegionalRecovery`. **Status:** Proposed composition.
**Trigger:** Households coordinate remote assistance. **Record:** Independent properties, travel times, clinics, information latency.
**Core result:** Access depends on real transport and service capacity. **Qualification gate:** Rural geography, medical resources and reliable communications.
**Acceptance:** Radio call received does not deliver medicine across broken route.

### PA-CNT-REF-005 — Displacement reception and rights
**Inherits:** `POP-003`, `INST-001`, `HAB-002` (resolve via exact crosswalk). **PA views:** `PA.DisplacementWave`, `PA.RefugePosture`. **Status:** Proposed composition.
**Trigger:** Newcomers arrive at intake. **Record:** Actual presence; property; care needs; registration progress; rights claims; authority.
**Core result:** Demand applies on arrival; legal classification decided separately. **Qualification gate:** Local law/protection, personnel and genuine support.
**Acceptance:** Unregistered children consume water as present people; are not assigned jobs.

### PA-CNT-REF-006 — Transition from refuge to durable housing
**Inherits:** `HAB-002`, `HAB-006`, `RCN-011` (resolve via exact crosswalk). **PA views:** `PA.RefugePosture`, `PA.ReconstructionTransition`. **Status:** Proposed composition.
**Trigger:** Housing conversion project accepted. **Record:** Work stages; inspected components; sanitation/power/water; occupancy terms; institution.
**Core result:** Accepted housing service only when actual support exists. **Qualification gate:** Usability criteria, construction inputs, resident rights.
**Acceptance:** Finishing walls without water does not automatically produce habitable capacity.


## 8. Institutional remnants, claims and continuity (`PA-CNT-INS`)
A crisis may interrupt a capital or communications while actual local institutional functions continue. Authority, evidence, practical control, legitimacy, recognition and personal skill remain distinct. Do not impose government extinction or guaranteed restoration from a narrative label.
### PA-CNT-INS-001 — Continuing local-government branch
**Inherits:** `INST-001`, `RES-KNW-002` (resolve via exact crosswalk). **PA views:** `PA.InstitutionFracture`. **Status:** Proposed composition.
**Trigger:** Capital government links fail. **Record:** Current staff/mandates; prior offices; available records; received orders; local procedures.
**Core result:** Institution continues functions it can actually perform. **Qualification gate:** Authority and governance/records profile.
**Acceptance:** Mayor displaced but municipal sanitation office still operates within its actual mandate.

### PA-CNT-INS-002 — Competing successor claims
**Inherits:** `INST-002`, `INST-001` (resolve via exact crosswalk). **PA views:** `PA.InstitutionFracture`, `PA.SuccessorAssessment`. **Status:** Proposed composition.
**Trigger:** Branches assert continuity. **Record:** Separate claims, recognition, control, contract/legal evidence.
**Core result:** No automatic legitimacy or inherited treaty rights. **Qualification gate:** Setting law/jurisdiction and relevant GOV process.
**Acceptance:** Two councils claim authority; neither gains universal assent by selecting entry.

### PA-CNT-INS-003 — Emergency public-health remnant
**Inherits:** `INST-004`, `SVC-HEALTH-001` (resolve via exact crosswalk). **PA views:** `PA.InstitutionFracture`, `PA.DisruptedProvision`. **Status:** Proposed composition.
**Trigger:** Health authority fragments. **Record:** Surviving staff and jurisdiction, records, real clinic support, information.
**Core result:** Surviving institution may coordinate support; cannot cause free treatments. **Qualification gate:** MED profile, communications, authority.
**Acceptance:** Outdated hospital report not equal current staffed bed capacity.

### PA-CNT-INS-004 — Emergency mutual-aid compact
**Inherits:** `INST-009`, `NET-F-002`, `NET-L-002` (resolve via exact crosswalk). **PA views:** `PA.RegionalRecovery`, `PA.InstitutionFracture`. **Status:** Proposed composition.
**Trigger:** Two local authorities negotiate aid. **Record:** Approved agreement, donor/receiver property, access routes, service/stock terms.
**Core result:** Obligations change only on effective agreement; real aid needs actual delivery. **Qualification gate:** Contract law, signatory mandate, stock and transport.
**Acceptance:** Signed food donation does not itself replenish recipient pantry.

### PA-CNT-INS-005 — Archives as continuity without technicians
**Inherits:** `INST-006`, `RES-KNW-001`, `RCN-012` (resolve via exact crosswalk). **PA views:** `PA.LegacyDependency`, `PA.SuccessorAssessment`. **Status:** Proposed composition.
**Trigger:** Institution recovers knowledge archive. **Record:** Preserved source documents, readability, specialists and trainees.
**Core result:** Records support training but do not replace it. **Qualification gate:** Education/certification and work model.
**Acceptance:** Reconstituted archives cannot run factory absent competent operators.


## 9. Reconstruction transition and durable successor content (`PA-CNT-REC`)
Reconstruction refers to a former function and the strategy selected for it; K-WORK/CIV owns projects and acceptance, K-NET owns useful services, and K-ORG/GOV owns authority. Repair, restoration, replacement, adaptation, redesign and deliberate abandonment are all valid outcomes. Stable peace and ordinary prosperity count as success.
### PA-CNT-REC-001 — Distributed microgrid successor
**Inherits:** `RCN-004`, `SVC-PWR-001` (resolve via exact crosswalk). **PA views:** `PA.ReconstructionTransition`, `PA.LegacyDependency`. **Status:** Proposed composition.
**Trigger:** Alternative power topology built. **Record:** Distributed installed generation; storage; distribution; operator skills; acceptance.
**Core result:** Current consumers receive only delivered power; old grid need not be restored. **Qualification gate:** Generation profile, commissioning and ongoing supplies.
**Acceptance:** Microgrid passes test; old regional station remains inoperable without denying local success.

### PA-CNT-REC-002 — Clinic-capability replacement
**Inherits:** `RCN-008`, `SVC-HEALTH-001` (resolve via exact crosswalk). **PA views:** `PA.ReconstructionTransition`, `PA.LegacyDependency`. **Status:** Proposed composition.
**Trigger:** Temporary aid becomes regional healthcare. **Record:** Real qualified staff, inventory, referral routes, facility support.
**Core result:** Capability established service-by-service, not one hospital level. **Qualification gate:** MED profile, working utilities and repeatable stock supply.
**Acceptance:** Care ward commissioned without pharmaceuticals cannot perform drug-dependent services.

### PA-CNT-REC-003 — Repair-to-reproduction industrial transition
**Inherits:** `RCN-009`, `EQP-SHOP-001`, `RES-IND-001` (resolve via exact crosswalk). **PA views:** `PA.ReconstructionTransition`, `PA.LegacyDependency`. **Status:** Proposed composition.
**Trigger:** Workshop proposes repeated fabrication. **Record:** Specific product drawing/standard; feedstock; tooling; qualified staff; trials/inspection.
**Core result:** Accepted batch outputs are real stock; prototype does not prove sustainable volume. **Qualification gate:** Quality control, measured production envelope.
**Acceptance:** One prototype valve does not create industrial-scale spare-part supply.

### PA-CNT-REC-004 — Reconstructed regional supply corridor
**Inherits:** `RCN-015`, `SVC-ROAD-001`, `NET-F-001` (resolve via exact crosswalk). **PA views:** `PA.RegionalRecovery`, `PA.ReconstructionTransition`. **Status:** Proposed composition.
**Trigger:** Road access and route services re-open. **Record:** Route ownership and geometry; vehicles; drivers; transload; legal access; throughput.
**Core result:** Network useful flow only within actual logistical envelope. **Qualification gate:** Road/bridge mode load limits, transport resource.
**Acceptance:** Bridge usable for foot travel but not heavy loads; no heavy cargo delivery.

### PA-CNT-REC-005 — Agriculture without guaranteed harvest
**Inherits:** `RCN-006`, `RES-AGR-001`, `RES-FOOD-003` (resolve via exact crosswalk). **PA views:** `PA.ReconstructionTransition`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Local planting capacity expanded. **Record:** Land/seed/water, inputs, people and growing-season calendar.
**Core result:** Future yield forecast is not edible current stock. **Qualification gate:** Crop/weather/ecology and labor models.
**Acceptance:** Crop planted today cannot feed hungry person today.

### PA-CNT-REC-006 — Industrial import-dependent stability
**Inherits:** `RCN-009`, `NET-F-002`, `SVC-MFG-001` (resolve via exact crosswalk). **PA views:** `PA.LegacyDependency`, `PA.SuccessorAssessment`. **Status:** Proposed composition.
**Trigger:** Imports reliably support essential machines. **Record:** Actual imports, terms, route risk, recurrent spares and skill needs.
**Core result:** Local nonmanufacture does not imply present incapacity. **Qualification gate:** Real sustained import agreements, deliveries, support horizon.
**Acceptance:** Stable imported parts can legitimately support durable service.

### PA-CNT-REC-007 — Civic records and succession restoration
**Inherits:** `RCN-013`, `RES-KNW-002`, `INST-001` (resolve via exact crosswalk). **PA views:** `PA.InstitutionFracture`, `PA.SuccessorAssessment`. **Status:** Proposed composition.
**Trigger:** Authority rebuilds records system. **Record:** Recovered documents, validity, staff, backup, laws, procedures, appeals.
**Core result:** Rights and claims established only by applicable process. **Qualification gate:** Institutional authorization and specific law.
**Acceptance:** Archive ownership documents alone do not confer universal sovereignty.

### PA-CNT-REC-008 — Water service redesign after central-system failure
**Inherits:** `RCN-002`, `SVC-WAT-001`, `RES-WAT-002` (resolve via exact crosswalk). **PA views:** `PA.ReconstructionTransition`, `PA.DisruptedProvision`. **Status:** Proposed composition.
**Trigger:** Community commissions local treatment. **Record:** New source, plant, operators, distribution and potable tests.
**Core result:** Only accepted output supports current consumers. **Qualification gate:** Water-quality and service test profiles.
**Acceptance:** Source found without treatment does not create potable supply.


## 10. Crisis-cause selector library and compositions (`PA-CNT-CRI`)
All listed crisis causes require their own actual enabling events and applicable physical/institutional models. The special APX selector never supplies automatic global collapse, random death, predetermined epidemic severity, nuclear fallout, magical power, or arbitrary infrastructure failure. An event may have distinct real causal effects but cannot be applied again for each PA overlay that mentions it.
### 10.1 Preserved original crisis archetypes
| Original crisis selector | Name | SCL registry status | Meaning of selection |
|---|---|---|---|
| `APX-001` | Conventional Interstate/Regional War | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-002` | Civil Conflict/State Fragmentation | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-003` | Pandemic/Epidemic Crisis | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-004` | Grid/Cyber/Systems Disruption | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-005` | Severe natural disaster event | selected_qualitative | Source-backed theme/cause design input; no instantiated crisis |
| `APX-006` | Ecological/Agricultural Crisis | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-007` | Nuclear Conflict/Accident | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-008` | Solar/Geomagnetic Technology Disruption | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-009` | Volcanic/Ash Crisis | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-010` | Economic/distribution disruption | selected_qualitative | Source-backed theme/cause design input; no instantiated crisis |
| `APX-011` | Institutional decline process | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-012` | Localized Isolation Crisis | source_backed_hold | Source-backed theme/cause design input; no instantiated crisis |
| `APX-X01` | Extraordinary/Theme Crisis Template | scoped_extension | Source-backed theme/cause design input; no instantiated crisis |
### 10.2 Crisis-specific compositional profiles
### PA-CNT-CRI-001 — War-driven infrastructure disruption
**Inherits:** `APX-001`, `SITE-022`, `SVC-ROAD-001` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.Disruption`. **Status:** Proposed composition.
**Trigger:** Documented military action affects civilian functions. **Record:** Conflict events; casualties via Core; damage to actual assets; civilian access.
**Core result:** One attack event links multiple dependent disruption views. **Qualification gate:** Applicable combat/protection and law, no universal damage.
**Acceptance:** One bridge strike assessed in several overlays cannot damage it repeatedly.

### PA-CNT-CRI-002 — Civil fragmentation without physical devastation
**Inherits:** `APX-002`, `INST-001` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.InstitutionFracture`. **Status:** Proposed composition.
**Trigger:** Authority splits after crisis. **Record:** Competing mandates, communications, service continuity, observed control.
**Core result:** No blanket shutdown of physically intact services. **Qualification gate:** Institutional and public security profile.
**Acceptance:** Two administrations dispute legitimacy while water system remains working.

### PA-CNT-CRI-003 — Specific-disease epidemic module socket
**Inherits:** `APX-003`, `HAZ-007` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Confirmed infectious cause present. **Record:** Source-specific disease, actual transmission, care capacity, observations.
**Core result:** PA groups exposure effects committed by configured MED/WILD module. **Qualification gate:** No generic transmission/lethality; module must be selected.
**Acceptance:** One infection exposure cannot be duplicated by clinic and district overlays.

### PA-CNT-CRI-004 — Grid and control-system dependency outage
**Inherits:** `APX-004`, `SVC-PWR-001`, `SVC-COM-001` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.Disruption`. **Status:** Proposed composition.
**Trigger:** Identified control failure or outage. **Record:** Affected network nodes; operating alternatives; alarm/report delay.
**Core result:** Actual service chain determines function; no universal electronics destruction. **Qualification gate:** Technological vulnerability and restart envelope.
**Acceptance:** Blackout leaves offline laptop intact absent actual damage cause.

### PA-CNT-CRI-005 — Regional flood and functional refuges
**Inherits:** `APX-005`, `HAZ-003`, `HAB-002` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.RefugePosture`. **Status:** Proposed composition.
**Trigger:** Flood actually reaches selected areas. **Record:** Water depth/route, shelter service, accessibility, real arrivals.
**Core result:** Only affected sites/habitations take hazards; intact region continues. **Qualification gate:** Specific flood and care/transport models.
**Acceptance:** Flooded district does not turn unaffected town into ruins.

### PA-CNT-CRI-006 — Agricultural disruption and regional trade
**Inherits:** `APX-006`, `SVC-FOOD-001` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.Pressure`. **Status:** Proposed composition.
**Trigger:** Harvest forecast downgraded by ecological cause. **Record:** Affected crops, reserve stock, importing routes, recipients.
**Core result:** Current food and future projection maintained separately. **Qualification gate:** Selected crop/weather/market profile.
**Acceptance:** Harvest fails; existing storehouse food remains in place.

### PA-CNT-CRI-007 — Nuclear event under explicit module
**Inherits:** `APX-007`, `HAZ-008` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.Disruption`. **Status:** Proposed composition.
**Trigger:** Nuclear source/geometry established. **Record:** Blast/thermal/radiological channels from selected module with actual timing.
**Core result:** One physical injury per distinct supported effect channel; reports not exposures. **Qualification gate:** Event-specific yield/source, geography, dose and medical profile.
**Acceptance:** Fallout is not automatically lethal everywhere and source termination does not erase dose.

### PA-CNT-CRI-008 — Geomagnetic disruption with bounded susceptibility
**Inherits:** `APX-008`, `SVC-PWR-001` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.Disruption`. **Status:** Proposed composition.
**Trigger:** Solar/geophysical event declared. **Record:** Actual field/technical susceptibility, isolation/protection, power network state.
**Core result:** Only supported equipment/services affected. **Qualification gate:** Validated or declared fictional event model; no blanket EMP.
**Acceptance:** Off-grid stored hand tools do not fail because grid electronics do.

### PA-CNT-CRI-009 — Distribution/economic crisis without missing goods
**Inherits:** `APX-010`, `SVC-FOOD-001` (resolve via exact crosswalk). **PA views:** `PA.Crisis`, `PA.DisruptedProvision`. **Status:** Proposed composition.
**Trigger:** Payment/trade access fails. **Record:** Standing stock, ownership, pricing/claims, truck access and people’s needs.
**Core result:** Goods remain physically present; access/service may be interrupted. **Qualification gate:** ECO and GOV profile; transport contract details.
**Acceptance:** Warehouse holds tons of food but consumers lack legal/economic access.

### 10.3 Extraordinary module boundary
`APX-X01` is a scoped template for zombie, alien, magical, mutational, temporal, death-loop or other exceptional causes. It is **not** a granted creature, disease, attack, power, resurrection or player ability. The theme module must define source, eligible targets, exposure, mechanisms, strength/limits, observations, intervention/counterplay, duration/persistence, cancellation, history/identity effects if any, and a compatible Core §§97/99/112 override. Disabling extraordinary modules must preserve ordinary disaster and recovery play. `Hour Zero` names and chronology are campaign/module lore and remain excluded from this generic library.

## 11. Variant authoring and practical composition
### 11.1 Variant steps
Choose: (a) unchanged SCL physical definition, (b) PA composition and former-function history, (c) actual cause-specific and technology/setting profile, (d) Core-owned instance with one ID per asset/person/lot, and (e) PAF-derived overlay. Change a shared object variant only if actual property/function/constraints change; changes in paint, jurisdiction or historical description normally alter only local presentation/context.
### 11.2 Worked case — abandoned clinic and emergency treatment
A clinic building is identified as `SITE-004`, not a guaranteed source of medicine. The real site record contains a locked treatment room, a powered refrigerator, some unassessed medication lots and absent qualified doctors. The survey first adds `K-INFO` evidence about the room. Entry permits inspection, not automatic healing. A recovered refrigerated drug lot requires its specific identity, dose and temperature history before it can be used. A qualified medical worker may run the `WRK-MED-001` temporary service if actual tools, consumables, safe workspace and care profile permit. `PA.LegacySite` records the inherited clinic function and extraction history; `PA.DisruptedProvision` records lost ordinary healthcare; `PA.RefugePosture` may track actual refuge use. All three refer to the **same** medicine, personnel, site, power and patient records. An improved report does not refill the refrigerator.
### 11.3 Worked case — old pump fails, stored water remains
A real power failure stops an electric pump at 08:00. A separate elevated tank remains available with actual usable water, connections and a selected hydraulic/service envelope. `PA.Disruption` links the power and water system; `PA.Pressure` tracks a time-supported vulnerability forecast. Do not declare instantaneous dehydration or empty the tank. If repair succeeds before service interruption, pressure closes without needing replacement peril. This is a causal example; it prescribes no general pump power or household-consumption rate.
### 11.4 Worked case — importing critical replacement parts
A surviving workshop is capable of operating an installed machine but cannot produce a particular controller. `PA.LegacyDependency` notes lost original manufacturing support. If import routes and accepted supply deliveries can sustainably provide this controller, current operation and long-term support may both be adequate. It is false to impose an automatic civilization level, a forced local manufacturing project or random breakdown merely because the workshop cannot make the part itself.

## 12. PAF v2.0 thirteen-record interface and events
| Overlay | Library content relation | Owned truth/source of actual change |
|---|---|---|
| `PA.Crisis` | APX cause/theme and onset variant | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.RegionalDisruption` | Prior versus current service/function variants | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.Disruption` | Affected dependency/asset/service compositions | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.Pressure` | Crisis-facing supported forecast, no second meter | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.LegacySite` | Former site, salvage and provenance configuration | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.DisruptedProvision` | Previous supplier and actual emergency substitute | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.RefugePosture` | Temporary refuge service and occupant planning | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.DisplacementWave` | Crisis-grouped real movements | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.InstitutionFracture` | Historical branches and claims | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.LegacyDependency` | Support/reproduction/import horizon | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.RegionalRecovery` | Broken/reconnected routes and assistance | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.ReconstructionTransition` | Former function and accepted redesign strategy | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
| `PA.SuccessorAssessment` | Historically continuous/new society description | Existing K-INFO/K-ASSET/K-STOCK/K-NET/K-WORK/K-ORG/K-ACTOR/K-POP plus applicable Core domains |
No PA-specific tick or loss ledger is added. PAF receives only committed Core event IDs and actual actor-scoped observations. Identical references/reports cannot apply physical changes twice. Separate occurrence, observation, sending and receipt times; a report can lag actual repair. Simultaneous events share pre-event state; conflict over finite stock/work is resolved once. Save/load/scale change retains processed spans and commitments.

## 13. PA campaign profile (`CPF-PA-BASE`, source-retained extension)
Record only decision-relevant selections; do not populate the world merely by filling a template:
```text
core_release: IRGS-CORE-3.2 (proposal for receiving bridge)
shared_catalogue: IRGS-SCL-1.0 (underlying family refs @0.2)
PAF_foundation: exact adopted/pinned version and authorized compatibility bridge
PA_content: IRGS-PACL-2.0; enabled PA-CNT IDs and revisions
setting_theme: crisis cause, onsets, geography, pre-crisis baseline/evidence/unknowns
modules: selected hazard/technology/disease/extraordinary sources + limits
content: exact PL/SCL family, required selector, readiness, native payload and profile
instances: actual Core actors, organizations, land, sites, lots, services, projects, routes
needs_care: species/medical/hygiene and environmental profiles with valid units/rates
crisis: historical disruption and current actual causal drivers (no mandatory stage)
legacy: site history, survey coverage, support/reproduction/import dependencies
relief: emergency use, legal authority, ownership, stocks, transport and acceptance
movement: actual groups, destinations, transit and destination forecasts separated
recovery: pursued/abandoned programs, limits and accepted useful outputs
information: as-of truth, observations, receipt times, hidden-state capability
continuity: actual aging, ecology, maintenance, deferred events, period processing
validation: selected acceptance cases, observed evidence, calibration status
status: source/adoption/implementation/playtest/calibration separately recorded
```
Profile absence does not mean zero or unlimited capability. A needed missing numeric model blocks only its dependent calculation under Core §112; other supported activity continues. No universal consumption, birth, decay, salvage yield, panic or enemy-escalation rates are offered.

## 14. Calibration and qualification requirements
| Dependent calculation | Calibration evidence required | No unsupported inference |
|---|---|---|
| Drinkable water and medical safety | Contaminant/pathogen, dose/testing, treatment efficacy, user profile | Clean water cannot be inferred from raw volume |
| Food supply and spoilage | Commodity, storage/temperature exposure, nutrition, demand, preservation | No universal spoilage at scene boundary |
| Fuel and power | Fuel grade, actual machine configuration, electrical demand, start/run capacity | No generic generator hours or power-to-services conversion |
| Cold chain | Thermal model, internal stock temperatures, backup buffers, operating boundaries | Power outage not instant destruction of medicine |
| Transportation and recovery | Accessible roads, travel/handling rates, payload, skilled labor, donor impact | Found object not automatically available at destination |
| Salvage/search | Prior site history, surveyed extent, fixed or justifiably generated stock, access and knowledge | No random restocked caches after repeats |
| Sustained medical operation | Staff qualifications, relevant medicine, care standards, referral, facilities | A first-aid bag does not enable all medical care |
| Infection/radiation/contamination | Cause module, source law, exposure/dose, target response, protective means | No universal disease or fallout effects |
| Agriculture and ecology | Crop/soil/climate/season, inputs, labor, yield and harvesting timeline | Planting is not immediate supply |
| Refuge and displacement | Actual people/needs, service and route capacity, protection/rights | No generic headcount-to-worker fraction |
| Replacement technology | Component wear/support, build quality, documentation, training, imports, testing | Possession and local reproduction not identical |
| Institutions and legal inheritance | Authority, applicable law, record validation, control and recognition | No automatic sovereignty or inherited treaties |
| Long spans and succession | Population, family, biological/ecological processes with processed spans | No arbitrary births or aging resets |
A complete implementation specifies units, formula/law, valid envelope, state owner, triggers, intervals, uncertainty, evidence, extreme/zero cases, interaction effects and one-time cost accounting. A library contract is **qualified** only after its source/identity gates, actual selected profile, reproducible behavioral execution and appropriate calibration evidence meet its documented acceptance targets. This document does not promote the 152 held PL family mappings or assert empirical validation.

## 15. Acceptance and regression specification
The companion `PA_Acceptance_Cases_v2_0.csv` contains **63 specified cases**: one specific case for each of the **43 proposed PA compositions** plus **20 cross-library/runtime/agency cases**. These are not declared executed live gameplay. Selected examples:
| Test ID | Scenario | Expected invariant |
|---|---|---|
| PA-L2-001 | Abandoned retail recovery survey: Survey request at formerly active store | Repeat visit to cleared aisles cannot renew food; previously unsearched freezer remains an unknown region |
| PA-L2-002 | Pharmacy inventory and cold-chain history: Former pharmacy assessed | An unlabeled bottle cannot become generic healing points |
| PA-L2-003 | Fuel depot salvage and pumping: Pump/stock condition inspected | Powerless station with fuel underground cannot yield delivered fuel without transfer capability |
| PA-L2-004 | Installed machinery salvage versus donor function: Machine cannibalization proposed | Removing the final serviceable controller disables donor operation; does not mint two controllers |
| PA-L2-005 | Unknown substructure in searched site: Partial building survey | Cleared ground floor does not declare unseen basement empty or full |
| PA-L2-006 | Recovered document and lost know-how: Manual or plans recovered | Recovered manual alone cannot commission complex apparatus |
| PA-L2-007 | Contaminated inherited potable-water lot: Evidence of contamination in reserve | One hundred liters can remain physically present yet be unavailable as potable service |
| PA-L2-008 | Long-term unreplaceable control component: Support/parts assessment changed | Running generator keeps running while unsupported component reproduction remains unresolved |
| PA-L2-052 | Site quantity is genuinely unknown | Unknown remains unknown; cannot substitute zero, filled store, or expected loot |
| PA-L2-053 | Two simultaneous relief services compete for one fuel stock | Allocation uses same pre-event state, finite shared resource, and no duplicated source |
| PA-L2-054 | End crisis while debt and surgery continue | Crisis overlay can archive; debt, injuries and ongoing care retain real state |
| PA-L2-055 | Quiet twenty-year settlement history without configured birth/decay rate | Do not invent people or wear; assess only configured processes; institutions remain autonomous |
| PA-L2-056 | Replaced generator with repaired unit and new local technicians | Old damage/maintenance history preserved; new duty ability requires actual staff and acceptance |
| PA-L2-057 | Precise radiation harm requested with no dose-response model | Defer dependent calculation; do not assign fake fatalities; independent play continues |
| PA-L2-058 | Existing PAF v2.0 still references Core3.1/SCL0.2 | Record scoped compatibility bridge and adoption; do not silently rewrite parent authority |
| PA-L2-059 | Theme extension APX-X01 requested with no selected module | No anomaly power, undead, mutation, temporal reset or resurrection by title alone |
| PA-L2-060 | Selected SCL family vs source-backed hold | Held original source remains with exact payload; no automatic deprecation or generic performance |
| PA-L2-061 | One old PA-RECON program appears with regional recovery assessment | Existing K-WORK/CIV progress has one owner; PAF holds historical relation only |
| PA-L2-062 | Availability of needed historical v1.2 source not verified | Do not claim all v1.2 cases were reconciled; preserve provenance gap |
| PA-L2-063 | Two independent runners given identical source, state and events | Compare IDs, times, quantities, knowledge, commitments; differing outcomes are test failures |
Source PAF v2.0 contains **22 PA13 cases, 15 PA20 cases and 62 PA v1.1 legacy cases** plus receiving tests; the separate v1.2 completeness gap remains unresolved. Those are Foundation/legacy tests, not newly executed results or duplicated content-specific tests. The full source remains in the archive. To qualify cross-engine operation, run independent reproducible traces with the same pinned sources/state/events, compare quantitative outcomes and actual knowledge, and separately record live campaign playtests and numerical calibration.

## 16. Provenance, CMRR outcomes, adoption and migration
### 16.1 Compare → Merge → Reconcile → Resubmit
**Compared:** complete PL-1.0 source (54 numbered sections), the uploaded PAF v2.0 source revision 2 (Core 3.1), Core 3.2 engine and `APOCALYPTIC` binding, SCL v1.0 normative registry and the original source-qualified PL payloads. **Recovered:** all 193 PL entry IDs exactly through original source binding records. **Merge:** shared families remain immutable and generic; PA-only thematic compositions and crisis/history semantics reside here. **Reconcile:** preserve qualifiers, no duplicate ownership, no source lore, no uncontrolled stats/rights/resource creation. **Resubmit:** complete specification plus crosswalk, all-section source matrix, proposed native compositions, acceptance specifications, verifier and migration contract.
### 16.2 Source status and gaps
PL-1.0 was proposed and structurally checked but not independently playtested. PAF v2.0 is a proposed complete source revision pinned to Core 3.1. SCL v1.0 is the current Core 3.2 catalogue, but individual readiness gates remain distinct. Two PL extensions (`APX-X01`, `CPF-PA-BASE`) retain their scoped identity. Neither the missing direct text of PAF v1.2 nor quantitative disease/transport/resource evidence is reconstructed from speculation. Optional Hour Zero lore, extraordinary capabilities and campaign conditions remain outside this generic content library.
### 16.3 Migration impact and compatibility
1. Do not alter a campaign unless an authorized prospective migration is requested. Snapshot time, assets, stock, actor/household conditions, knowledge, work, actual movement, ownership, institutions and pending events first.
2. Preserve complete PL aliases, original payloads and `@0.2` SCL canonical revisions. Mapping a source entry is **not** permission to retire its source-backed definition.
3. Map generic equipment/site/stock/infrastructure state to existing Core owners by stable ID; PA compositions should reference that same state. Historical interpretations may become PA.* overlays without duplicating physical facts.
4. Obtain an explicit receiving compatibility decision for PAF v2.0 Core 3.1 pin against Core 3.2; document any changed provider behavior and exact scoped profile. No silent adoption or source rewriting.
5. Hold outcome-dependent operations where needed implementation/calibration is absent, or select a bounded prospective ruling under Core §112. Avoid running old and new generic algorithms simultaneously.
6. Verify identity resolution, event replay, scarcity, service dependence, simultaneous claims, delayed information, autonomy, Mixed voluntary costs, migration and coarse/fine scale continuity; record real results.
7. Keep all rejected/retired interpretations accounted for: loot respawn, compulsory scarcity stages, instant infrastructure restoration, infinite emergency stock, automatic successor legitimacy, invented injuries/panic, and campaign-specific Hour Zero content are *not* valid universal behaviors.
### 16.4 Adoption status
**Proposed v2.0**, complete specification available for review; the source and newly added compositions are *not* automatically adopted or instantiated. Structural verification confirms file/reference consistency only. These are not claims of successful calibration, 100% behavioral acceptance, independent runner parity or live play. An adopted future version must record exact enabled scope, effective date, data/model profiles and executed evidence. Reconciliation alone does not authorize changes to an existing game.

**End of IRGS-PACL-2.0 — proposed standalone Fantasy/Military-style slim genre content library.**
