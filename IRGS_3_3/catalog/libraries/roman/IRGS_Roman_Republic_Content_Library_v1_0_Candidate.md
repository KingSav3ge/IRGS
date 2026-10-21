# IRGS — Roman Republic Content Library
## v1.0 · Rebuilt candidate for Roman Slim v1.2, Core v3.2 and SCL v1.0

**Document ID:** IRGS-RRCL-1.0  
**Scope:** Roman Republic life simulation, default approximately 60–50 BCE in Roman Italy and connected regions.  
**Design status:** Proposed library; not adopted or calibrated. The Roman Slim Engine v1.2 retains its explicit accepted workshop status.  
**Parents:** `IRGS-CORE-3.2` → Roman historical/life selection → `IRGS-RRLS-SLIM-1.2` → this content library → campaign profile/state.  
**Catalogue:** `IRGS-SCL-1.0`, with individual exact content entries retaining `@0.2` identity and their source gates.  
**Source authority:** Roman Slim v1.2 and its **14 exact native content bindings**; full Roman v1.0 preserved for source/provenance. R1/R2 maturation proposals are **not** promoted.  
**Package effects:** No world objects or actors created; no rule overrides; no historical or numerical certification; no retroactive migration.

## 1. Purpose and ownership

The library supplies **Roman-specific content variants, site and institution templates, period filters, recorded source-native equipment adapters and composed scene requirements**. It is not a new Roman engine. A `RRCL-*` entry is a reusable *definition*, never an owned item, employed worker, lawful right, stocked institution, built site, completed task or participant in an event.

Core owns action, time, stock, assets, actors, institutions, commitments, information, work, services, competition, medical outcomes and transactions. The Roman engine owns `ROM-*`/`RRP-*` procedures, selected game abstractions and explicit priority/wear overrides. Shared SCL owns generic types and exact source content identities. **RRCL owns only its dated Roman composition and eligibility conditions.**

### Source versus proposal

- **DIRECT:** Source-derived setting content pattern or named capability present in Roman Slim v1.2 / full Roman v1.0. Individual template wording is still newly proposed; a dated local instance needs evidence.
- **PROPOSED:** New Roman-specific catalogue template, historically plausible as a development candidate but **not independently historically verified** here. Each requires a locality/date/profile gate before consequential activation.
- **SELECTED NATIVE:** The 14 engine-provided bindings are already selected Roman local profiles, preserving their original status and parameters, but they are not proof of empirical performance or item availability.
- **HELD SCL:** Use the full original source-backed payload and selected adapter rather than treating a candidate family definition as a complete new generic item. Qualification drafts do not amend the normative source.

## 2. Resolution and activation contract

Resolve **era (`ERA-ANT`) → actual date/region/local custom → real institution or maker → applicable SCL family and exact revision/selector → Roman native or other selected physical/social profile → instantiated actor/asset/obligation/site through its Core owner**. Wrong date, missing access, incomplete model or an unavailable professional cannot be repaired by a favorable roll. A candidate may remain a planning placeholder and cannot create consequential behavior before its required gate.

**Minimum Roman content-binding record:**
```text
roman_catalogue_entry | exact revision | historical region/date/evidence
shared_family_or_source_payload | source gate | selector | native profile version
asset/actor/site/contract actual ID (only if legitimately instantiated)
owner | physical location | access/custody | condition/quality/coverage/fit
qualified people | operating means | resource inputs | maintenance
legal issuer/jurisdiction/rights (when material) | price/terms (when material)
visibility and received evidence | missing consequential parameter | override and effective date
```

An actor, animal, asset and monetary or food stock has exactly one Core authoritative record, with context-sensitive projections. A sword cut and thrust share one physical weapon. A captive is an actor, never a stock-lot. A buyer recommendation is not a transaction; a contest result is not a wage payment; a house is not a fully functioning service just because it has a name.

## 3. Exactly preserved Roman native equipment adapters (14)

The following records are **copied by reference**, not redefined as new weapon physics. The accompanying `sources/Roman_v1_2_Native_Content_Bindings_Unchanged.json` preserves original selectors, checksums, parameters and composition exclusions. An empty SCL reference means this remains a **Roman native mechanism**, not an attempted shared replacement.

| Native Roman profile | Exact SCL reference | Selector | Original gate | Native values |
|---|---|---|---|---|
| `RR-DAGGER-THRUST-1.0` | `SCL:PBC-WPN-FL-WPN-M-004@0.2` | `modes.thrust` | source_backed_hold | `{"defeat": 1, "threat": 1}` |
| `RR-BLADE-CUT-1.0` | `SCL:PBC-WPN-FL-WPN-M-006@0.2` | `modes.cut` | selected_qualitative | `{"defeat": 1, "threat": 2}` |
| `RR-BLADE-THRUST-1.0` | `SCL:PBC-WPN-FL-WPN-M-006@0.2` | `modes.thrust` | selected_qualitative | `{"defeat": 2, "threat": 2}` |
| `RR-SPEAR-THRUST-1.0` | `SCL:PBC-WPN-FL-WPN-M-013@0.2` | `none` | source_backed_hold | `{"defeat": 2, "threat": 2}` |
| `RR-LIGHT-CLUB-1.0` | `SCL:PBC-WPN-FL-WPN-M-002@0.2` | `none` | source_backed_hold | `{"defeat": null, "threat": 1}` |
| `RR-JAVELIN-1.0` | `SCL:PBC-WPN-FL-WPN-R-002@0.2` | `none` | source_backed_hold | `{"defeat": 1, "threat": 2}` |
| `RR-CLOTHING-1.0` | `SCL:PBC-WPN-FL-ARM-001@0.2` | `none` | source_backed_hold | `{"cut": 0, "impact": 0, "pierce": 0}` |
| `RR-PADDED-1.0` | `SCL:PBC-WPN-FL-ARM-002@0.2` | `none` | source_backed_hold | `{"cut": 1, "impact": 1, "pierce": 0}` |
| `RR-MAIL-1.0` | `SCL:PBC-WPN-FL-ARM-005@0.2` | `none` | selected_qualitative | `{"cut": 3, "impact": 1, "pierce": 2}` |
| `RR-SMALL-SHIELD-1.0` | `SCL:PBC-WPN-FL-SHD-002@0.2` | `none` | source_backed_hold | `{"defensive_circumstance": -10, "source_structure": 2}` |
| `RR-BROAD-SHIELD-1.0` | `SCL:PBC-WPN-FL-SHD-003@0.2` | `none` | source_backed_hold | `{"defensive_circumstance": -10, "source_structure": 3}` |
| `RR-LARGE-SHIELD-1.0` | `SCL:PBC-WPN-FL-SHD-004@0.2` | `none` | source_backed_hold | `{"defensive_circumstance": -15, "source_structure": 3}` |
| `RR-NATIVE-UNARMED-1.0` | `SCL:PBC-WPN-FL-WPN-M-001@0.2` | `none` | source_backed_hold | `{"inventory_object": false, "mechanism_required": true, "native_threat": 0}` |
| `RR-HEAVY-HANDHELD-IMPACT-1.0` | `Roman-local only` | `none` | retained_native_profile | `{"defeat": null, "threat": 2}` |

**Equipment discipline:** generic source models do not assign a gladius, pugio, scutum, pilum, helmet or typical Roman service kit. Each named historical candidate below requires its own period-eligible physical construction and supported profile. Blade cut/thrust are alternate modes on one object; unarmed is a non-inventory method. The 14 native values are provisional operating selections of the *engine*, not values calibrated or amended by this library.

## 4. Roman content catalogue — 118 proposed entries

Every entry records its Roman purpose, activation prerequisites and a non-inheritance boundary. **No listed content is automatically a campaign instance.** Exact machine-readable records are in `Roman_Content_Catalogue_v1_0.json`/CSV.

### LAW — Legal standing, claims and household relations (13)

**Core owner(s):** `K-ACTOR/K-ORG/GOV/ECO/LIFE`. **Basis:** Roman Slim §§2–4; full §§6–9.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-LAW-001@1.0` — **Person-standing dossier** | DIRECT | Independent freedom, civic position, household dependence, capacity and jurisdiction fields | An actual person and dated competent authority | A label does not grant citizenship, freedom, legal capacity or universal recognition |
| `RRCL-LAW-002@1.0` — **Custody and claimed authority** | DIRECT | Claimant, basis, current custody, restraint and access evidence | Named person, custodian and observed control | Physical custody neither proves legal title nor player assent |
| `RRCL-LAW-003@1.0` — **Sale and transfer arrangement** | DIRECT | Buyer, seller, inspection, consideration, payment, handover and asserted recognition | Eligible counterparties, terms, goods/funds and scope | Sale proposal does not transfer custody or establish an underlying lawful claim |
| `RRCL-LAW-004@1.0` — **Manumission by vindicta candidate** | DIRECT | Particular authority-led route with acts, witnesses, timing and evidence | Dated eligible jurisdiction, route access and required acts | An attempted or promised act is not completed freedom |
| `RRCL-LAW-005@1.0` — **Manumission by censu candidate** | DIRECT | Census-based route requiring locally valid eligibility and registration | Qualified census context, date and participating authorities | Listing alone does not demonstrate a universal emancipation entitlement |
| `RRCL-LAW-006@1.0` — **Manumission by testamento candidate** | DIRECT | Testamentary route linked to actual succession and effective legal changes | Valid particular testament, death/succession and any conditions | Property inheritance and free status are independent decisions |
| `RRCL-LAW-007@1.0` — **Peculium or administered fund** | DIRECT | Legal owner, manager, authorized spending, reserves, withdrawal and pending claims | Actual recorded holdings and permissible transaction terms | Being credited is not owning unrestricted cash |
| `RRCL-LAW-008@1.0` — **Patron–freedperson relationship** | DIRECT | Rights, obligations and enforceability following a specific release | Actual effective change and recognized relationship | Does not grant loyalty, property, office or expertise automatically |
| `RRCL-LAW-009@1.0` — **Household dependency arrangement** | DIRECT | Persons, support providers, provision and constraints under local terms | Actual household, members, means and agreed or imposed terms | Need, affection and legal power remain distinct |
| `RRCL-LAW-010@1.0` — **Local disputed-status claim** | DIRECT | Competing assertions, evidence, actual effects and recognition scope | Specific claimant, jurisdiction, witnesses or documents | Unknown law is neither automatic validity nor automatic invalidity |
| `RRCL-LAW-011@1.0` — **Marriage or family alliance candidate** | PROPOSED | Particular household arrangement, dependants, rights and property consequences | Verified date/status eligibility and actual participants | No universal marital rights or stereotyped household decisions |
| `RRCL-LAW-012@1.0` — **Clientele or sponsorship arrangement** | DIRECT | Person-specific sponsorship, introductions, favors and enforceable undertakings | Existing willing patrons, credible access and dated norms | A social concession is not a guaranteed service or favorable vote |
| `RRCL-LAW-013@1.0` — **Infamia or occupational stigma candidate** | DIRECT | Scoped restrictions and reputation consequences where actually supported | Exact triggering condition, local institution and dated meaning | No universal stat penalty or automatic loss of citizenship |

### ECO — Production, market, property and labor (14)

**Core owner(s):** `ECO/K-STOCK/K-ASSET/K-WORK/K-ORG`. **Basis:** Roman Slim §4; full §§7–9.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-ECO-001@1.0` — **Market stall and seller** | DIRECT | Local merchant, offered stock, quoted terms and delivery possibilities | Actual vendor, physical goods, locality/date, tender and access | Visible goods and quoted price do not guarantee sale |
| `RRCL-ECO-002@1.0` — **Local tender and denomination** | DIRECT | Sestertius-led accounting with denarius conversion for display | Actual coin quantities, accepted tender and transaction counterparties | One denarius equals four sestertii in the selected adapter, not four additional coins |
| `RRCL-ECO-003@1.0` — **Credit or debt undertaking** | DIRECT | Creditors, borrowers, obligations, due dates, collateral and enforcement | Actual legal capacity, funds, terms and applicable local law | Approval, debt or expectation never creates physical stock |
| `RRCL-ECO-004@1.0` — **Lease, tenancy or access grant** | PROPOSED | Defined property use, crop/work rights, rent and termination terms | Owned/controlled property and valid agreements | No universal tenure or rent percentage |
| `RRCL-ECO-005@1.0` — **Estate steward or vilicus office** | DIRECT | Designated steward with delegated estate work and reporting | Named competent person, real mandate, labor and accounts | A title does not manufacture staff, yields or money |
| `RRCL-ECO-006@1.0` — **Latifundium management profile** | DIRECT | Large estate variant with land parcels, staff, inputs, buildings and obligations | Actual land, workforce, seasonal inputs, output market and lawful control | Name alone does not establish size, productivity or slavery policy |
| `RRCL-ECO-007@1.0` — **Small farm household enterprise** | PROPOSED | Family-scale land cultivation with linked household labor and private stock | Land/access, people, seasons, tools and biological profile | No guaranteed harvest or invisible surplus |
| `RRCL-ECO-008@1.0` — **Workshop and craft establishment** | DIRECT | Actual artisan stations, tools, orders, consumables and customers | Skilled workers, equipment, work hours and received orders | Naming a workshop does not confer manufacturing capability |
| `RRCL-ECO-009@1.0` — **Compulsory labor assignment** | DIRECT | Ordered task with controller, stated basis, provision, movement and enforcement | Actual authority or coercive power, available person and feasible task | No compulsory PC compliance or free labor output |
| `RRCL-ECO-010@1.0` — **Skilled apprenticeship or tutelage** | PROPOSED | Tutored practical trade learning with assessment and permissible hours | Competent instructor, station, worker access and selected learning profile | Being enrolled never awards automatic competence |
| `RRCL-ECO-011@1.0` — **Trade consignment in transit** | DIRECT | Seller, carriage, transit location, holder, recipient and settlement | Real quantities, transport capacity, custody and route | Stock in transit is not simultaneously local at both ends |
| `RRCL-ECO-012@1.0` — **Provision or supply contract** | DIRECT | Contracted food, clothing, service or tools for an actual institution | Vendor, qualifying quantity, dates, obligations and ability to deliver | Unpaid invoice or order does not count as delivered provision |
| `RRCL-ECO-013@1.0` — **Wage, allowance or appearance payment** | DIRECT | Amount owed to stated payee under actual work or bout terms | Qualifying service, contract, due event and payer resources | Payment to employer, lanista or household is not personal cash |
| `RRCL-ECO-014@1.0` — **Debt pledge or collateral claim** | PROPOSED | Secured obligation with particular custody, enforcement and priority conditions | Identified obligation, asset, real security and dated law | A claim is not instantaneous seizure or extra collateral stock |

### MAT — Local stocks, supply and material culture (12)

**Core owner(s):** `K-STOCK/K-ASSET/K-WORK`. **Basis:** Roman Slim §§4,7,9,11; full §§7,11,13.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-MAT-001@1.0` — **Grain or prepared grain food lot** | PROPOSED | Tracked food quantity, quality, storage and preparation for the consumer | Actual lot, unit, safe provision and dated local availability | No universal caloric value, daily ration or harvest yield |
| `RRCL-MAT-002@1.0` — **Olive oil lot** | PROPOSED | Consumable or trade good with defined intended use and handling | Particular source, container, condition and unit | Oil is not fuel, medicine or food interchangeably without an eligible method |
| `RRCL-MAT-003@1.0` — **Wine or beverage lot** | PROPOSED | Beverage stock with source, condition, legal control and consumption access | Actual volume or container measure and potable/safety profile | No automatic intoxication, nutrition or cleanliness benefits |
| `RRCL-MAT-004@1.0` — **Potable and nonpotable water** | DIRECT | Physical volume distinguished from available safe drinking-water service | Tested source, delivery, safety and actual recipient needs | Full container does not prove potable service |
| `RRCL-MAT-005@1.0` — **Animal fodder lot** | PROPOSED | Animal provision with type, safe use, location and finite quantity | Specified animal, dietary profile and real stock | Animal needs are not silently satisfied by human rations |
| `RRCL-MAT-006@1.0` — **Textile clothing inventory** | DIRECT | Owned garments, fit, wear, clothing coverage and custody | Actual garment, material, dimension and person | An item name does not give armor coverage to absent body regions |
| `RRCL-MAT-007@1.0` — **Leather working supplies** | PROPOSED | Hide, straps and leatherwork inputs for justified craft/repair | Known material, qualified work, fasteners and time | Repair input is consumed; repair is not instantaneous |
| `RRCL-MAT-008@1.0` — **Iron or bronze raw material lot** | PROPOSED | Metal inputs, usable grade, source and workability | Actual material, furnace/tools, expertise and production plan | Raw metal does not imply a finished blade or standardized metallurgy |
| `RRCL-MAT-009@1.0` — **Timber and wooden component lot** | PROPOSED | Lumber or assembled parts with type, dimensions and condition | Actual source, tools, transport and joinery profile | A wood reserve does not generate a shield or vehicle without work |
| `RRCL-MAT-010@1.0` — **Pottery or storage-vessel item** | PROPOSED | Container shape, usable volume, fragility and custody | Supported vessel, fill/load, condition and access | A container does not mint its contents |
| `RRCL-MAT-011@1.0` — **Roman medical supply lot** | DIRECT | Bandage, water, equipment or medicinal inputs as individually substantiated | Specified item, suitable use, practitioner and supply | Item presence does not guarantee treatment efficacy |
| `RRCL-MAT-012@1.0` — **Physical coin pouch or money cache** | DIRECT | Coins remain actual owned/custodied asset/stock with spendable restrictions | Physical cash, holder, location, legal control and access | Book entries and monetary notation never duplicate coins |

### ARMS — Arms, protection and combat equipment (15)

**Core owner(s):** `K-ASSET/K-STOCK/K-ACTOR`. **Basis:** Roman Slim §§6–8,11; full §§12–13.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-ARMS-001@1.0` — **Roman short sword candidate** | PROPOSED | Period-eligible sword-like implement with independently usable cut/thrust modes | Dated design, length, grip, actual object and selected native mode binding | A sword name cannot establish reach, Roman availability, or two physical swords |
| `RRCL-ARMS-002@1.0` — **Roman pugio candidate** | PROPOSED | Short pointed sidearm requiring its actual piercing geometry | Dated item evidence, accessible hand/holster and short-thrust binding | The generic dagger native value is a selection, not a verified pugio property |
| `RRCL-ARMS-003@1.0` — **Roman spear candidate** | PROPOSED | Long shaft weapon with controlled approach and possible close-use limitations | Actual shaft length, frontage, hands and selected spear-thrust binding | Cannot thrust through a blocked surface or use long reach at Grappled automatically |
| `RRCL-ARMS-004@1.0` — **Roman pilum or throwing-spear candidate** | PROPOSED | One throwable physical implement with mode and retrieval considerations | Verified local form, weight, accessible projectile and native javelin binding | Not automatically reusable while in flight or lodged elsewhere |
| `RRCL-ARMS-005@1.0` — **Club and nonstandard blunt implement** | DIRECT | Plausible local striking implement with declared impact mechanism | Actual shape, durability, hands and light/heavy mode selection | Generic club reference creates no object and no assumed historical army issue |
| `RRCL-ARMS-006@1.0` — **Unarmed grappling and control method** | DIRECT | Body method for positioning, hold, balance or supported impact effects | Actor anatomy, position, instruction where relevant and complete unarmed effect | Never adds an inventory weapon or unavoidable injury |
| `RRCL-ARMS-007@1.0` — **Cloth and padded protection** | DIRECT | Garment construction and actual covered zones with textile channel profile | Real garment, fit, body zones, wear and declared native protection | No numerical stacking or automatic full-body coverage |
| `RRCL-ARMS-008@1.0` — **Mail-based protection candidate** | PROPOSED | Mail garment variant with validated historical eligibility and exposed zones | Actual garment, repair, construction and native mail profile | Preserved FL adapter is not proof of local production or specific Roman form |
| `RRCL-ARMS-009@1.0` — **Small-hand shield candidate** | DIRECT | Small oriented protective object with grip and wear state | Real shield, orientation, fit, contact and small-shield adapter | No shield benefit while uncontrolled or inaccessible |
| `RRCL-ARMS-010@1.0` — **Broad shield candidate** | DIRECT | Broad protective shield whose construction is locally specified | Object construction, stance/arc, covered attack line and adapter | Not an imported heater shield or an automatic scutum |
| `RRCL-ARMS-011@1.0` — **Large frontal shield candidate** | DIRECT | Large frontage barrier operated according to actual space/handling | Eligible construction, carrying requirements, facing and adapter | A −15 circumstance is not unconditional rear protection |
| `RRCL-ARMS-012@1.0` — **Roman scutum candidate** | PROPOSED | Historical shield-form placeholder to be matched only after dated construction review | Supported date/region, exact physical form, holder, durability and selected adapter | Historical name alone cannot import kite/heater shapes, Structure 3 or a universal bonus |
| `RRCL-ARMS-013@1.0` — **Helmet or limb protection candidate** | PROPOSED | Individually covered body regions with physical construction and fit | Exact local form, useful coverage, modeled channels and wearer | No whole-body armor bonus from a helmet |
| `RRCL-ARMS-014@1.0` — **Carry, scabbard and readiness rig** | PROPOSED | Worn attachment controlling item access, retention and encumbrance | Actual gear, fit, fastening and permitted hand access | Equipment is not instantly drawn solely because it is owned |
| `RRCL-ARMS-015@1.0` — **Sling or bow candidate** | PROPOSED | Period-specific ranged method requiring its own complete physical profile | Historically eligible equipment, ammunition, range and training | No native Roman sling/bow damage, reach or accuracy supplied by this library |

### MIL — Military service environments and equipment use (9)

**Core owner(s):** `K-ORG/K-ACTOR/K-ASSET/K-STOCK`. **Basis:** Roman Slim §§6,11; full §§12–13,18; Soldier/Military Slim §14 optional.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-MIL-001@1.0` — **Republican armed unit candidate** | PROPOSED | Service organization with dated native roles, members and obligations | Actual muster, appointment authority, period-specific organizational evidence | Unit name does not create personnel or standardized reform-era structure |
| `RRCL-MIL-002@1.0` — **Military watch or guard detail** | DIRECT | Timed watch commitment, post, authority, handover and duty equipment | Existing people, qualified leader, patrol area and relief | No ghost sentries, instant orders or duplicate duty hours |
| `RRCL-MIL-003@1.0` — **Armed escort agreement** | PROPOSED | Escorted movement with guards, clients, routes and supply | Available personnel, transport, threats, contract and travel time | Authority and armed presence do not guarantee safe passage |
| `RRCL-MIL-004@1.0` — **Training yard and drill station** | DIRECT | Place/instructors for weapon, formation or movement practice | Space, credible instruction, equipment and actual qualifying hours | Attendance alone does not earn a new competence tier |
| `RRCL-MIL-005@1.0` — **Muster and equipment inspection** | PROPOSED | Real unit assets, personnel, condition and fitness assessed at a particular time | Known unit identities, inspection access and authority | Roster view is not replacement people or repaired equipment |
| `RRCL-MIL-006@1.0` — **Camp or marching baggage train** | PROPOSED | Temporary lodging, equipment, provision and load-bearing transport | Actual carts/animals, supplies, labor, route and water | Camp label does not restore fatigue or conjure provision |
| `RRCL-MIL-007@1.0` — **Officer and delegated order instrument** | PROPOSED | Officer role bound to actual orders, mandates, communications and reporting | Dated institutional command basis and qualified subordinate | Rank neither guarantees skill nor magically transmits instructions |
| `RRCL-MIL-008@1.0` — **Pay, booty or award claim candidate** | PROPOSED | Specified benefit or property share recorded as claim or transfer | Actual service/authority and valid dated entitlement | No modern standardized pay rate or automatic award |
| `RRCL-MIL-009@1.0` — **Siege tool or field-engineering asset** | PROPOSED | Actual field apparatus with materials, work prerequisites and required crew | Dated local technical profile, transport and qualified operators | No unsupported universal siege damage or throughput |

### PLACE — Sites, land uses and service facilities (12)

**Core owner(s):** `K-ASSET/K-NET/K-ORG/K-WORK`. **Basis:** Roman Slim §§4,10–11; full §§8–9,15,18.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-PLACE-001@1.0` — **Urban household dwelling** | PROPOSED | Occupied residence with real service, property and household capacity | Actual premises, owners, occupants, water and upkeep | Occupancy capacity and living standards are not granted by a name |
| `RRCL-PLACE-002@1.0` — **Rural farmhouse or villa candidate** | PROPOSED | Farm residence, stores and land-service dependencies | Particular land, structures, workers, animals and location | No automatic latifundium, mass slave labor or large yield |
| `RRCL-PLACE-003@1.0` — **Estate workshop or storage yard** | DIRECT | Actual tools, task stations, stores and controlled access | Installed assets, skilled staff, usable materials and work time | A locked warehouse contains only recorded stock |
| `RRCL-PLACE-004@1.0` — **Ludus or fighter training establishment** | DIRECT | School quarters, intake, instruction, equipment, support and accounts | Specific lanista, actual inmates, staff, supplies, rights and space | Naming a ludus creates no arena readiness or legal custody |
| `RRCL-PLACE-005@1.0` — **Arena or temporary contest venue** | DIRECT | Competed event place with bounds, access, event support and authority | Organizer, venue, current configuration and safety/stop rules | No mandatory Imperial amphitheatre or universal contest law |
| `RRCL-PLACE-006@1.0` — **Public marketplace or exchange area** | DIRECT | Specific traders, offers, storage, communication and delivery | Local commerce, date, accessibility and vendor stock | An abstract market never guarantees desired goods |
| `RRCL-PLACE-007@1.0` — **Roadside lodging or resting site** | PROPOSED | Particular accommodation, price/permission, rest and animals | Actual beds/shelter, care, provisions and rights | A roadside label never heals injuries automatically |
| `RRCL-PLACE-008@1.0` — **Stable or animal holding yard** | PROPOSED | Place for keeping animals with feeding, shelter and handlers | Actual animals, occupancy, fodder, secure gates and labor | Mounts remain actors and do not become transport stock |
| `RRCL-PLACE-009@1.0` — **Bathing and water-supply facility candidate** | PROPOSED | Potential civic/private hygiene service with infrastructure dependencies | Date/location support, water, fuel, staff, rights and upkeep | No automatic infection cure, sanitation rate or available hot water |
| `RRCL-PLACE-010@1.0` — **Quay, river port or transport depot** | PROPOSED | Specific embarkation and storage tasks with limited capacity | Geography, vessels, stevedores, routes and cargo | A dock does not transport goods without vessel and work |
| `RRCL-PLACE-011@1.0` — **Dated local temple or shrine candidate** | PROPOSED | Actual social/religious site with custodianship and potential institutions | Local cult/site evidence, authorized roles and real resources | No supernatural power is imported by a shrine |
| `RRCL-PLACE-012@1.0` — **Local forum or civic meeting space** | PROPOSED | Assembly/judicial/public business site with bounded access and participants | Location, dated governing institution, real staff and schedules | Buildings do not automatically decide cases or create mandates |

### ARENA — Gladiatorial activity and organized contests (10)

**Core owner(s):** `COMP/K-ORG/ECO/MED/K-ACTOR`. **Basis:** Roman Slim §10; full §15.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-ARENA-001@1.0` — **Lanista and school management role** | DIRECT | Organization controller with real property, obligations and qualified work | Named lanista or delegated manager, school and lawful capacity | Lanista title neither guarantees ownership of each fighter nor results |
| `RRCL-ARENA-002@1.0` — **Fighter intake and capability dossier** | DIRECT | Actual person status, skills, health, accessibility and decision authority | Custody or contractual basis, assessor and care information | Intake does not compel future agreement or confer training |
| `RRCL-ARENA-003@1.0` — **Doctor or specialist instructor candidate** | DIRECT | Available skilled teacher of methods and bout preparation | Actual instructor, time, demonstrated expertise and school access | Instructor-hours cannot be spent twice |
| `RRCL-ARENA-004@1.0` — **Bout fixture and matchup** | DIRECT | Specific organizer, date, entrants, rules, available equipment and obligations | Real participants, arena, authority, credible competing schedules | No automatic fair pairing, escalating difficulty or script |
| `RRCL-ARENA-005@1.0` — **Arena rule and official-stop profile** | DIRECT | Authorized objectives, stop/intervention powers, discretion and permissions | Dated actual terms, official authority and feasible intervention means | Submission request does not instantly prevent injury |
| `RRCL-ARENA-006@1.0` — **Appearance and event-payment contract** | DIRECT | Payer, recipient, amount, exclusions, contingent terms and delivery | Real contract, attendance obligation and actual payment event | School revenue is not automatically a fighter's private money |
| `RRCL-ARENA-007@1.0` — **Audience, witness and rumor propagation** | DIRECT | Witness observations, interpretations and distinct report/receipt times | Actual audience, language/access and transmission route | Crowd sentiment is not a universal mercy percentage |
| `RRCL-ARENA-008@1.0` — **Post-bout injury and equipment disposition** | DIRECT | Care needs, actual custody, damaged items and pending payments | Committed result, staffed treatment, inspectable goods and responsible authority | A result does not heal, pay or repair anything by itself |
| `RRCL-ARENA-009@1.0` — **Fighter release, reassignment or retirement** | DIRECT | Separate career status, custody, contractual release and legal standing | Effective authorized route, obligations and physical movement | Leaving the arena is not manumission unless the lawful acts occur |
| `RRCL-ARENA-010@1.0` — **Public celebration or honor report candidate** | PROPOSED | Institutional or social recognition linked to actual witnessed event | Specific audience, sponsor, decisions and dissemination | Recognition does not mint new expertise or universal prestige |

### TRAVEL — Journeys, carriers and communication (8)

**Core owner(s):** `K-NET/K-ACTOR/K-ASSET/K-STOCK/K-INFO`. **Basis:** Roman Slim §11; full §§10–11.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-TRAVEL-001@1.0` — **Land-route segment candidate** | DIRECT | Defined travel edge with terrain, access, mode and time | Actual route, date, movement capacity and known conditions | No universal march speed or free distance |
| `RRCL-TRAVEL-002@1.0` — **Pack animal and carried load candidate** | DIRECT | Living animal with tack, care, carried inventory and human handling | Actual animal, training, suitable load and fodder | Animal is K-ACTOR, not an instantly manufactured vehicle |
| `RRCL-TRAVEL-003@1.0` — **Wheeled cart or wagon candidate** | PROPOSED | Actual vehicle with axle/crew, cargo and operating restrictions | Dated regional vehicle evidence, draught, route and condition | No default payload or rate |
| `RRCL-TRAVEL-004@1.0` — **River ferry or crossing service candidate** | PROPOSED | A transport event depending on craft, crew, queue and water conditions | Actual craft/operator, rights, crossing and fare | A river is not crossed by paying an abstract fare alone |
| `RRCL-TRAVEL-005@1.0` — **Coastal or river vessel candidate** | PROPOSED | Specialized vessel-dependent transport via MAR profile if enabled | Dated vessel form, seamanship, crew, weather, cargo, ports | No naval capability from generic cargo ownership |
| `RRCL-TRAVEL-006@1.0` — **Human courier and message delivery** | DIRECT | Issued message, bearer, route, physical transmission and receipt | Actual sender/courier, permissions, time and destination | A report does not arrive everywhere when issued |
| `RRCL-TRAVEL-007@1.0` — **Guarded conveyance of a captive** | DIRECT | Physical movement and legal claim separately tracked en route | Person, real restraining/control means, orders and conveyance | Escort does not create consent or pre-set future fate |
| `RRCL-TRAVEL-008@1.0` — **Travel provisions and lodging obligations** | DIRECT | Separate person/animal meals, water, bedding, payments and delays | Real held stock, lawful access, stop/service and commitments | Time and needs do not reset at an overnight scene break |

### CARE — Care, exposure and recovery contexts (8)

**Core owner(s):** `MED/K-ACTOR/K-ASSET/K-STOCK`. **Basis:** Roman Slim §§5,9; full §§5,11,14.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-CARE-001@1.0` — **Physician or healer service candidate** | DIRECT | Specific qualified care provider with physical tasks and finite time | Actual practitioner, knowledge, station, care rights and supplies | A title does not guarantee competence or modern treatment |
| `RRCL-CARE-002@1.0` — **Bandaging and wound-stabilization arrangement** | DIRECT | Real care work to address supported injury/bleeding mechanism | Known injury, accessible materials, qualified care and time | Stabilization is neither healing nor restored duty fitness |
| `RRCL-CARE-003@1.0` — **Recovery quarters and protected rest** | DIRECT | Condition-appropriate rest, shelter and actual support | Usable place, protected time, water, food and care | Entering a bed does not erase fatigue or wounds automatically |
| `RRCL-CARE-004@1.0` — **Infection or contamination assessment candidate** | DIRECT | Observed signs, cause-relevant exposure and plausible course | Actual exposure, organism/environment model and evidence | No generic infection roll from Roman atmosphere |
| `RRCL-CARE-005@1.0` — **Heat, cold and unsheltered exertion** | DIRECT | Weather and workload-specific burden on a real actor | Climate, protection, exertion, duration and physiology | No undifferentiated daily hardship roll |
| `RRCL-CARE-006@1.0` — **Animal-force accident candidate** | DIRECT | Contact by actual animal movement or behavior with supported injury | Animal actor, mass/motion, victim position and applied contact | Animal hazard uses exposure/contact, not sword Pierce values |
| `RRCL-CARE-007@1.0` — **Household caregiving arrangement** | DIRECT | Responsibility for dependent's provision and realistic staffing | Actual household members, capacities, rights and schedule | A family member cannot supply two simultaneous full-time services |
| `RRCL-CARE-008@1.0` — **Period injury-recovery milestone** | DIRECT | Acute, stabilized, healing, rehabilitation, resolved or lasting impairment | Particular diagnosis, care, functional test and recovery interval | Reference time ranges do not force healing or death |

### CIVIC — Civic institutions, offices and public records (10)

**Core owner(s):** `GOV/K-ORG/INV/K-INFO`. **Basis:** Roman Slim §§3,10–11; full §§6,9,16.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-CIVIC-001@1.0` — **Dated magistrate and court authority candidate** | DIRECT | Office mandate and case-specific procedural authority | Exact locality, time, known office, competence and case | No blanket empire-wide legal power or modern hearing presumption |
| `RRCL-CIVIC-002@1.0` — **Senate-related deliberation candidate** | PROPOSED | Actual meeting and resolution limited by recognized procedure | Dated body, participants, quorum/authority as researched | Debate is not physical order execution or a guaranteed vote |
| `RRCL-CIVIC-003@1.0` — **Popular assembly candidate** | PROPOSED | Specific civic participation and resulting authorized decisions | Dated locality, eligibility, meeting mechanism and procedure | Not every Roman resident is a voter; no automatic rights |
| `RRCL-CIVIC-004@1.0` — **Local municipal council candidate** | PROPOSED | Local office and administration where historically eligible | Particular municipal polity, dated norms and staff | No universal Roman administrative structure |
| `RRCL-CIVIC-005@1.0` — **Census or status record candidate** | DIRECT | Particular public registration referenced in status adjudication | Actual registrar, legal eligibility, date and evidence | An unverified enrollment does not grant instant freedom |
| `RRCL-CIVIC-006@1.0` — **Tax, levy or public due agreement candidate** | PROPOSED | Particular collection claim, basis and applicable responsible authority | Dated governing law, liable person/property and official means | No universal tax rate, property seizure or invisible treasury |
| `RRCL-CIVIC-007@1.0` — **Civic infrastructure contract candidate** | PROPOSED | Authoritative commission for road, water, public works or upkeep | Real institution, funding, workers, design and commissioning | Commission is neither built asset nor accepted service |
| `RRCL-CIVIC-008@1.0` — **Dated recruitment and enrollment candidate** | PROPOSED | Service-entry claim with eligibility, terms, oath or authority if applicable | Actual army or service institution, role and dated requirements | Recruitment is not instant competence, issue or rank |
| `RRCL-CIVIC-009@1.0` — **Local security or pursuit order** | DIRECT | Particular investigators/guards with knowledge, jurisdiction and means | Real issuer, authorized recipients, cause and transmission | No omniscient empire-wide pursuit state |
| `RRCL-CIVIC-010@1.0` — **Sacred/public ceremony administration candidate** | PROPOSED | Ordinary human institution with actual rites, officials and obligations | Dated cult, local institution and specific participant | No magic, mind control or default universal religious rule |

### RECORD — Documents, observation and handover (7)

**Core owner(s):** `K-INFO/ECO/K-ORG/K-STOCK`. **Basis:** Roman Slim §§2–4,10–11; full §§10,17–18.

| ID / template | Status | Roman composition or use | Activation gate | Cannot infer |
|---|---|---|---|---|
| `RRCL-RECORD-001@1.0` — **Witness account and interpretation** | DIRECT | Source-scoped report separated from physical occurrence and official findings | Actual observer, sensory access and statement time | A witness assertion is not authoritative truth |
| `RRCL-RECORD-002@1.0` — **Transaction tablet or written undertaking candidate** | PROPOSED | Dated agreement record with copy location, authenticity and holder | Literacy/access, material, witnesses and valid local convention | Possessing a document does not prove enforceable rights by itself |
| `RRCL-RECORD-003@1.0` — **Estate account and inventory** | DIRECT | Owner-scoped claims, holdings, receipts, outgoings and physical stock | Actual books and linked transfers/events | Book balance does not mint produce, coin or labor |
| `RRCL-RECORD-004@1.0` — **Roman-language instruction or translation** | DIRECT | Language register, hearer understanding and faithful/incorrect communication | Actual speaker, target comprehension, channel and evidence | Repeating words is not literacy or private understanding |
| `RRCL-RECORD-005@1.0` — **Delayed message on a road route** | DIRECT | Issued time, departure, transit, receipt and recipient belief | Real sender/route/bearer and communication access | Report arrival cannot re-trigger the earlier physical event |
| `RRCL-RECORD-006@1.0` — **Legal certificate or attestation candidate** | PROPOSED | Particular issuer's record evidencing an actual limited status or right | Dated authority, identity and applicable procedure | Document name alone grants no legal consequence |
| `RRCL-RECORD-007@1.0` — **Contest report and resulting reputation** | DIRECT | Official outcome, witnesses, reports, reach and interpretation | Actual competition event, organizer and transmission | Crowd knowledge is not instantly global fame |

## 5. Roman operational compositions — causal exemplars

**E01 — A captive transferred to a trader.** Required composition: Link existing person to dated asserted custodial claim; establish inspection, price, buyer funds, authorized assent/compulsion rules, real payment and physical handover as independent events. **Boundary:** Custody can change before recognition; a report can arrive later. Neither event creates a second actor or retroactively validates contested legal title.

**E02 — A legal manumission opportunity.** Required composition: Reference `RRCL-LAW-004@1.0`, `RRCL-LAW-005@1.0`, `RRCL-LAW-006@1.0` as distinct route candidates, then bind its particular jurisdiction, relevant date, officials, participants, acts and record. **Boundary:** A patron promise, a release from guard, and an official legal change are different outcomes. Missing eligibility stays unresolved.

**E03 — A lanista considers buying a fighter.** Required composition: One buyer institution, available funds, actual trainer capacity, care, expected contracts and custody terms. Seller, buyer and legal claim are separately assessed. **Boundary:** Sale/payment and actual delivery occur once; no compelled PC motivation, instant skills or compulsory future arena storyline.

**E04 — A school hires an instructor.** Required composition: Actual teacher identity, duty time, salary agreement, station, students, technique scope and qualifying hours. **Boundary:** No second teacher appears from a facility label. Qualified student hours differ from instructor hours and permissions.

**E05 — A sword with two attack modes.** Required composition: One underlying `K-ASSET` object, selected physical form, Roman native `RR-BLADE-CUT-1.0` and `RR-BLADE-THRUST-1.0`, shared wear/condition and actual chosen attack mode. **Boundary:** One blade, not two inventories. Geometry, target access, protection and selected contact model remain prerequisites.

**E06 — A scutum-style shield in a dated town.** Required composition: Research and bind physical form, construction, Structure and orientation; select compatible shield adapter only after eligibility is supported. **Boundary:** The Roman-looking name does not grant the source Fantasy heater/kite shield form or a universal −15 modifier.

**E07 — Shield struck by three simultaneous contacts.** Required composition: Use a single canonical event batch and the Roman engine’s selected ordinal wear rule, based on common pre-contact condition/Structure; commit the final condition once. **Boundary:** The library neither changes `RRP-WEAR-1.1` nor creates a second damage record; reports do not replay the batch.

**E08 — Market purchases provisions for travel.** Required composition: Real vendor stock, buyer permitted tender, quantities, actual sale, physical handling, carriage, animal needs and travel time. **Boundary:** Contract promises are not received goods; stock in transit remains in transit, with real carrying limits.

**E09 — A magistrate’s order delivered late.** Required composition: Actual office authority and order issue, courier, transmission, receipt and possible local execution have separate times; preserve actor-scoped knowledge. **Boundary:** No instant pan-Roman enforcement, global wanted marker or NPC action based on an unknown order.

**E10 — A paid gladiatorial bout.** Required composition: Use Core COMP event, Roman contest terms, actual entrants/gear, fight execution via Roman adapter, official resolution, MED care and ECO payment to the **named payee**. **Boundary:** Submission does not immediately halt violence, prize does not automatically purchase freedom and crowd does not force mercy.

**E11 — Estate makes a productive investment.** Required composition: Real owner or administrator, land/site, worker expertise, investment stock, construction/maintenance tasks, delivery, accepted output and market access. **Boundary:** No automatic yield, modern rate-of-return or success-triggered random disaster.

**E12 — A veteran or freedperson retires peacefully.** Required composition: Change particular service obligations/office and household circumstances at actual effective times; retain standing, relationships, property, wear and unresolved claims. **Boundary:** Prosperous ordinary life is valid and need not provoke a stronger threat or an enforced return to combat.

## 6. Profile governance and Roman historical eligibility

The engine’s default source window is approximately **60–50 BCE**. This is not an asserted full chronology, and the book does not certify archaeological accuracy. The engine specifically warns against later Imperial spectacle conventions, fantasy equipment statistics taken as historical facts, unverified legal benefits, and universal travel/wage values. Every template requiring a historical decision must record `date | locality | evidence/source | confidence | local institution | eligible form | allowed scope | effective revision`.

For an unresolved historical claim, label it **unverified** and use either a sourced profile, an explicitly agreed scenario assumption or an individually scoped prospective ruling under Core §112; do not quietly invent Roman rates or official procedures. Existing established campaigns retain their own precedents until explicitly revised.

### Qualification and compatibility gates

1. **Catalogue**: exact identifier, immutable source revision, semantic type, required selector, completeness gate and full source payload where held.
2. **Date/locale**: specific Roman Republic setting eligibility; no default Augustan/Imperial, medieval or fantasy content.
3. **Means**: actual qualified person, object/stock, construction, operating resources, physical route or institution.
4. **Authority**: particular legal capacity, ownership/custody, control, rights and actual procedural acts.
5. **Effect**: selected Roman genre model and its valid inputs, not a second content-owned simulator.
6. **Release**: campaign adoption/effective time/overrides and an applicable acceptance-run record; no retroactive migration.

## 7. Calibration backlog — 29 explicit gates

| ID | Domain or unresolved parameter | Requires from selected source |
|---|---|---|
| `RRCL-CAL-01` | Dated legal authority | Jurisdiction/office, eligibility, authorized acts, evidence and rights |
| `RRCL-CAL-02` | Slavery claims and disputed transfer | Effective local law, claims, custody, transfer and refusal consequences |
| `RRCL-CAL-03` | Manumission routes | Dated applicability, prerequisites, completion, recognition and restrictions |
| `RRCL-CAL-04` | Peculium arrangements | Legal title, authorization, revocation and asset control |
| `RRCL-CAL-05` | Market prices, wages and commissions | Dated local quote, currency unit, delivery and recorded counterparty |
| `RRCL-CAL-06` | Cash tender and exchange | Accepted physical coin/denomination rules and money-holder access |
| `RRCL-CAL-07` | Work productivity and crop yield | Inputs, qualified labor, land/season, output rate and useful acceptance |
| `RRCL-CAL-08` | Roman arms chronology | Period/region, construction provenance, bearer role and historical confidence |
| `RRCL-CAL-09` | Weapon physical envelopes | Length/reach, usable mode, hands, action readiness and injury channel |
| `RRCL-CAL-10` | Protection coverage/condition | Body zones, construction, wear, fit, angle and handedness |
| `RRCL-CAL-11` | Shield geometry and history | Size, form, arc, Structure source, handling, failure and repair |
| `RRCL-CAL-12` | Unarmed injury mechanism | Target anatomy, force, method, feasibility and injury thresholds |
| `RRCL-CAL-13` | Simultaneous contact grouping | Prestate, memberships, event ordering and correction boundary |
| `RRCL-CAL-14` | Roman unit service rules | Date, institution, roles, pay, muster, authority and doctrine |
| `RRCL-CAL-15` | Staffed care and recovery | Personnel, supplies, wound type, prognosis, disability and triggers |
| `RRCL-CAL-16` | Fatigue and physiological load | Selected context, actual qualifying intervals and extrema |
| `RRCL-CAL-17` | Contamination and infection | Specific cause/exposure, delay, progression and intervention |
| `RRCL-CAL-18` | Gladiatorial contest and official powers | Jurisdiction, venue, organizer, fight limits, stop/submission/decision |
| `RRCL-CAL-19` | Gladiator wages, award and release | Contract, real payer/payee, official result, legal release and liability |
| `RRCL-CAL-20` | Ludus staffing and expenses | Real people, housing, teaching, tools, care and financial obligations |
| `RRCL-CAL-21` | Roman regional site eligibility | Exact time/place, archaeology/text sources and uncertainty |
| `RRCL-CAL-22` | Road and carrier operating rate | Route distance, terrain, animal/vehicle capability and handling |
| `RRCL-CAL-23` | Water travel operating profiles | Actual vessel, crew, capacity, navigation and seasonal weather |
| `RRCL-CAL-24` | Language and literacy | Particular register, comprehensibility, scripts and communication method |
| `RRCL-CAL-25` | Civic and provincial power | Particular locality/office/date, decision authority and appeals if any |
| `RRCL-CAL-26` | Historical dated backdrop and divergence | Source provenance, event prerequisites, dates and actor knowledge |
| `RRCL-CAL-27` | Asset/material quality and deterioration | Actual use, environment, repair means, provenance and triggers |
| `RRCL-CAL-28` | Finite role population | Existing actor pool, specialization, recruitment/replacement policy |
| `RRCL-CAL-29` | Randomness/hidden-state persistence | Runner capability, event IDs, secrecy, deterministic replay and scope |

No filler values for coin market prices, physiological recovery, Roman unit numbers, weapon geometry, output, travel speed, institutional legality or contest frequencies are introduced. The engine’s existing selected numerical abstractions remain **provisional**.

## 8. Acceptance requirements — 64 specified cases

These are **unexecuted complete-runtime requirements**. Source/hash/crosswalk validations and a separate bounded synthetic accounting check are reported in the release verification file; that evidence does not constitute playtesting or historical calibration.

| ID | Case | Required outcome |
|---|---|---|
| `RRCL-AC-001` | A person detained at a holding site and a written sale claim exists | One actor and physical control; sale claim remains separate from validated legal standing |
| `RRCL-AC-002` | Promise of manumission made before the route is performed | Pending undertaking only; no effective freedom field change |
| `RRCL-AC-003` | Manumission candidate lacks relevant dated jurisdiction | Keep unknown/unresolved and require a scoped ruling, not presumed eligibility |
| `RRCL-AC-004` | Custodian loses physical control while ownership is disputed | Physical custody change only; legal case stays open |
| `RRCL-AC-005` | Roman status certificate bears an unknown issuer | Treat as evidence to evaluate, not instant recognized standing |
| `RRCL-AC-006` | Peculium account is administered for an enslaved worker | Only authorized spending is available; legal ownership remains distinct |
| `RRCL-AC-007` | Patron offers a recommendation for a position | Recommendation does not create appointment, credentials or wages |
| `RRCL-AC-008` | Existing household has multiple dependants | Each actor persists with real needs; no second household consumption ledger |
| `RRCL-AC-009` | An actor holds one denarius and no other cash | Roman account displays four sestertii equivalent; physical coins still one denarius |
| `RRCL-AC-010` | One coin is handed over in an authorized purchase | One transfer, no simultaneous duplicate monetary display units |
| `RRCL-AC-011` | Appearance fee paid to lanista | School account receives it; fighter receives only a separately authorized transfer |
| `RRCL-AC-012` | Supplier invoice issued and still unpaid | Claim exists; no customer stock before physical receipt |
| `RRCL-AC-013` | Two buyers each request the last available tool | Only one compatible sale can reserve/transfer the single item |
| `RRCL-AC-014` | Transported consignment is between towns | Source debited and transit credited; destination not yet credited |
| `RRCL-AC-015` | Craft workshop lacks smith and forge | Production remains infeasible regardless of demand |
| `RRCL-AC-016` | Successful harvest market offer but no available transport | Stock remains at source; no automatic remote sale/delivery |
| `RRCL-AC-017` | One sword has both cut and thrust modes | One asset; two selected selectors share its condition/custody |
| `RRCL-AC-018` | Unarmed technique chosen | Use actor/method; no inventory object created |
| `RRCL-AC-019` | A large shield is slung on the back | No frontal shield defense without actual control/orientation |
| `RRCL-AC-020` | Roman scutum label but no construction specified | Do not import heater/kite form or Structure 3 automatically |
| `RRCL-AC-021` | Dagger thrust against actual impervious coverage | Physical protection applies; high skill does not create penetration |
| `RRCL-AC-022` | Mail garment covers torso but not hands | Hand strike resolves exposed hand without torso armor |
| `RRCL-AC-023` | Two fighters wear the same named armor, different condition | Condition-specific protection differs; no shared global mutable gear state |
| `RRCL-AC-024` | Throwing implement is released and not recovered | One physical item changes location; cannot throw the same item again |
| `RRCL-AC-025` | A bow is mentioned without dated local effect profile | Do not infer damage/range from name or fantasy source |
| `RRCL-AC-026` | One simultaneous contact batch contains three Stress-1 contacts | Selected Roman wear rule uses common pre-state, advances once, clears marks |
| `RRCL-AC-027` | Later report repeats a shield strike | Report does not create second damage or spend |
| `RRCL-AC-028` | Equipment is issued to a captive with limited use permissions | Owner/custodian/use access distinct; no automatic title transfer |
| `RRCL-AC-029` | An arena organizer pairs an unavailable fighter | Fixture cannot summon actor or ignore commitments |
| `RRCL-AC-030` | Fighter requests submission during a live bout | Request is not automatic safety; actual official response and timing matter |
| `RRCL-AC-031` | Arena crowd supports a fighter | Influences actual decision-maker only if observed; no generic mercy roll |
| `RRCL-AC-032` | Fighter wins but fee belongs to establishment | Result, money recipient and personal status remain separate |
| `RRCL-AC-033` | Gladiator is declared retired | Arena career changes; captivity/manumission requires separate authority |
| `RRCL-AC-034` | Fighter injured and school has one competent caregiver | Finite staff capacity; not all casualties treated instantaneously |
| `RRCL-AC-035` | A bout is canceled after weapons transported | Previous handling cost and time remain; no automatic refunds |
| `RRCL-AC-036` | Arena event is rendered in large and small scales | Only one match/result and underlying injury/inventory state |
| `RRCL-AC-037` | Person has serious injury and restorative bandages | Supply and treatment access are necessary but not automatic recovery |
| `RRCL-AC-038` | Disrupted sleep after strenuous labor | Use selected fatigue rule once; retain appropriate residual load |
| `RRCL-AC-039` | Person enters clean recovery quarters | Rest occurs only over actual protected time, not instant reset |
| `RRCL-AC-040` | Animal kicks a handler | Animal-force contact mechanism, not sword-pierce table |
| `RRCL-AC-041` | Medical official reports healed while functional limitation remains | Evidence/prognosis/fit-for-duty remain separate |
| `RRCL-AC-042` | Missing medical ingredient advertised at market | No usable care output from unreceived goods |
| `RRCL-AC-043` | Contamination exposure ends | Future exposure stops; already accrued condition follows supported recovery |
| `RRCL-AC-044` | Letter conveys order from magistrate after long road delay | Authority subject to dated scope; action not received until actual delivery |
| `RRCL-AC-045` | Two offices claim control of a storehouse | Authority and actual possession distinct; supplies remain one ledger |
| `RRCL-AC-046` | Local council votes for road project | Authorization is not completed construction or available budget |
| `RRCL-AC-047` | New civic appointment title recorded | Authority limited to effective mandate; skill not increased |
| `RRCL-AC-048` | Candidate senate resolution without researched period rule | Retain proposed content; do not assert universal vote or binding effect |
| `RRCL-AC-049` | Rumor of pursuit reaches district later | No omniscient empire-wide wanted state |
| `RRCL-AC-050` | Citizen status contested | Record evidence and limited acceptance, not automatic permanent global recognition |
| `RRCL-AC-051` | Courier departs at noon and arrives after bridge reopened | Report receipt updates knowledge only, not bridge state |
| `RRCL-AC-052` | A cart carried by an owner lacks draught animals | Cargo transport infeasible until legitimate means exist |
| `RRCL-AC-053` | Pack animal in transit requires food and rest | Living animal needs persist; stock and load stay finite |
| `RRCL-AC-054` | Riverboat has crew but no supported hull profile | No invented operating envelope or transit rate |
| `RRCL-AC-055` | Captive is escorted and changes location | No voluntary consent or legal release implied |
| `RRCL-AC-056` | Trip broken into finer scenes after 2h travel | No free additional hours or replenished food |
| `RRCL-AC-057` | Historical divergence changes one supplier | Only dependent trajectories revisited, no total history rewrite |
| `RRCL-AC-058` | An actor is deceased and successor play selected | No copied private knowledge or untransferred property |
| `RRCL-AC-059` | Workshop entry reused in separate campaigns | IDs, actors, goods and events remain campaign-scoped |
| `RRCL-AC-060` | A Roman template is looked up repeatedly | Read-only lookup does not instantiate people, stock, currency or site |
| `RRCL-AC-061` | A content ID is pinned at wrong revision | Reject/require explicit compatibility mapping; no silent alias upgrade |
| `RRCL-AC-062` | A held SCL definition has only a candidate summary | Preserve complete original source payload and native Roman adapter |
| `RRCL-AC-063` | The Core v3.2 parent receives later patches | New version not silently inherited without compatibility rebind |
| `RRCL-AC-064` | Stable Roman household lives peacefully for a decade | No compulsory escalation, income or population change without configured causes |

## 9. Reconciliation and removed duplication

**CMRR source coverage:** all 20 numbered source sections of full Roman v1.0 and all 12 of accepted Slim v1.2 receive dispositions in `Roman_CMRR_Section_Dispositions_v1_0.csv`. Core/SCL providers are not copied as new Roman algorithms; native Roman numerical/priority/wear/legal profile references retain their source authority.

**Accounted non-transfers:** broad Fantasy weapon and shield shapes are not imported as Roman form, original Roman numerical profiles are not promoted into SCL, original source full-engine clock/stock is not resurrected, proposed historical candidates are not adopted law, and campaign lore/state is not initialized. The previous Roman source edition and binding are packaged unchanged for provenance. No formerly supported Roman native entry is deleted or renumbered.

**No silent omissions:** Original full engine §§1–20 are reconciled in the matrix even where their procedures are fully owned by Core or the Roman genre engine and therefore intentionally absent from content. The 14 Roman native bindings are carried exactly. The original source has no authoritative exhaustive Roman object inventory; new entries are explicit proposed coverage, not a claim to have recovered omitted canon.

## 10. Adoption, migration and record interface

The library is **proposed**, independently of Roman Slim v1.2 acceptance. To activate it, record the exact library/engine/Core/SCL versions, date/locality scope, historical evidence, content/profile gates, adopted entry set and effective campaign boundary. Each `RRCL-*` ID is a content definition, not a migrated instance. Existing actor IDs, custody, injury, hours, coin quantity, work and reports survive unchanged. No automatic state migration, conversion or retroactive gear grant occurs.

A later SCL family promotion may require a new exact family revision and an explicit source/binding comparison. Held content remains usable only via its complete preserved source and selected Roman adapter; neither a draft compendium nor a library title can remove these gates. R1/R2 maturation documents are available separately but **not active rules** for Roman Slim v1.2.

## 11. Provenance and release

| Source | Use | Authority/status | SHA-256 |
|---|---|---|---|
| Roman Slim v1.2 | Exact source snapshot | Accepted Roman engine reference | `402c80e30727b086bd4b5289154f29679aac08494ae303734a3f3c26961a1710` |
| Roman v1.2 native content bindings | Exact source snapshot | Selected Roman profiles and gates | `b1acd807495fdc5ced05659592600c365fa958b30155dd332461d3fef39e6d2a` |
| Roman full v1.0 | Exact source snapshot | Prior source / provenance | `0a77a92d7ee6140566baa85f199dc3b4eec9a57544aa0785258d2dfa44bf82a4` |
| SCL v1.0 registry | Read-only external provider; hash pinned | Existing shared identity and reference gate | `67c4e0eb4b67fbc8f2cf874dae06381bf2e4c9eb48850a35d7ffc10c8a4a35b9` |
| Core v3.2 engine bindings | Exact source snapshot | Receiving Core binding context | `e7d6a4250921787b673e4c2974711b3dc53a3b5d3a344a09da8ec9995242b0b7` |

**Version:** Roman Republic Content Library v1.0 Candidate, 14 October 2026. **Change summary:** built an independent Roman-specific catalogue, preserved every selected native binding by reference, supplied 12 causal exemplars, source-to-target CMRR, dated qualification and explicit calibration gates, with regression acceptance specifications. **Validation status:** source and structural checks only; no independent campaign runtime or historical calibration.

