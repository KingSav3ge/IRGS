# IRGS — Post-Apocalyptic Survival and Reconstruction Foundation
## Version 2.1 — Complete slim engine linked to Core v3.2

**Document ID:** IRGS-PAF-2.1  
**Release date:** 14 October 2026 · complete Core 3.2 receiving edition  
**Publication status:** Complete linked workshop edition, resubmitted. Its version identity, acceptance of individual clauses, campaign adoption and validation remain distinct.  
**Status:** Complete new engine edition. Source rules retain their recorded scope; new receiving clarifications remain subject to acceptance. No campaign adoption, numerical calibration or live playtest is claimed.  
**Parent:** [IRGS-CORE-3.2](Core/IRGS_Core_Engine_v3_2.md), current complete shared parent. Exact current components are pinned in [PAF_PACKAGE_MANIFEST.json](PAF_PACKAGE_MANIFEST.json).  
**Predecessor:** Supplied PAF v2.0 source revision 2, aligned to Core 3.1; earlier v2.0 revision 1 and slim v1.3 remain provenance outside this clean distribution.  
**Architecture:** Shared Core → this genre foundation → Apocalypse/Theme Module → Campaign Profile → Campaign State. Content definitions remain separately versioned.  
**Method:** Compare → Merge → Reconcile → Resubmit. Publication changes no campaign or source file.

**Selected catalogue:** [SCL 1.0](Core/IRGS_Shared_Content_Library_v1_0.md), with its [normative registry](Core/IRGS_Shared_Content_Registry_v1_0.json) and immutable @0.2 family revisions. The PAF version, Core version and catalogue version are independent.

**Genre content:** [Post-Apocalyptic Content Library v2.0](PALibrary/README.md), 43 optional proposed compositions and 63 specified cases. Current receiving applicability is recorded in Appendix E.

**Receiving binding:** [PAF 2.1 / Core 3.2](IRGS_PAF_Binding_v2_1_Core3_2.json). **Content:** [all 193 PL references](IRGS_PAF_Content_References_v2_1.csv). **Review:** [reconciliation](IRGS_PAF_Reconciliation_v2_1.csv) and [verification](IRGS_PAF_Verification_v2_1.md).

This complete engine inherits shared procedures directly from the included parent. It supplies crisis-specific records, procedures, runtime triggers, module boundaries, profile gates, acceptance obligations and migration. It requires no earlier generic Core or whole earlier PAF document to operate at its stated scope.

<a id="paf-1"></a>
## 1. Purpose, scope, status and dependencies

This foundation specializes civilization-scale disruption: crisis propagation in relation to a documented prior order, depletion of inherited capital, emergency replacement of ordinary provision, refuge and displacement, fractured institutions, replacement vulnerability, regional recovery, reconstruction and durable successor societies. It applies before, during and after crisis, including regions that remain intact. It contains no mandatory collapse stage, technology tier, victory threshold or recurring catastrophe.

Core owns action resolution, clock, physical events, actors, stocks, work, services, institutions, population and information. PAF owns only the thirteen crisis-specific assessment records defined below. Modules own their cause-specific mechanisms; profiles select rates and starting assumptions; campaign state holds actual entities. A PAF view is never another spendable inventory, population ledger, progress counter or effect resolver.

<a id="paf-1-1"></a>
### 1.1 Authority and parent pin

Current explicit user direction/correction → established campaign rule/override → adopted relevant genre foundation → adopted Core → scoped temporary proposal where no rule applies. This release does not outrank a campaign's adopted rules. Its normal ownership interfaces do not override Core. Exceptions require explicit scope under Core §112 and prospective application under Core §97.

**Parent status:** Core 3.2 and SCL 1.0 are the confirmed current workshop components selected for this receiving edition. Exact files and providers are supplied in this package. Current component identity does not adopt a campaign, promote held content or calibrate a numerical profile.

The unchanged parent contains two residual editorial phrases: “v0.2 registry” in §111 and “Proposed Core 3.2” in §112. The current-release header, published provider binding and normative SCL 1.0 selection govern this deployment. Immutable @0.2 entry revisions remain valid. Those phrases select no previous catalogue or competing runtime.

**Evidence labels:** Source fact = wording or state supported by a named source; inference = reasoned consequence with premises; proposal = this receiving design or a provisional selection; external research = separately attributed evidence, never canon by itself. No external research or new physical rates were introduced here.

**Validation boundary:** The current parent manifest reports its own structural and bounded checks; Core Appendix C holds acceptance requirements, Appendix B deployment/calibration, and Appendix D optional profiles. Those are inherited evidence/requirements, not a full PAF gameplay pass. This edition's [verification](IRGS_PAF_Verification_v2_1.md) records fresh receiving and finite reference fixtures separately from the 109 retained source cases and twenty inherited CW-PA gates. Writing, acceptance, implementation testing, calibration and playtesting remain separate.

<a id="paf-1-2"></a>
### 1.2 Required Core interfaces and ownership

Each row names a provider in the pinned file. Read/requests mean access to the authorized Core interface, not a second implementation. The nine shared owners remain K-TIME, K-INFO, K-ACTOR, K-POP, K-STOCK, K-ASSET, K-WORK, K-NET and K-ORG; domain workflows coordinate them.

| Interface | Exact Core v3.2 provider | PAF reads / requests | Sole authoritative write owner |
|---|---|---|---|
| I01 Runtime and causality | §§4–5, 8, 10–12, 90–91; Appendix A | Committed events, shared pre-event state, processed spans, authorized response requests | Core event/record owners; PAF writes derived overlays only |
| I02 Information and baseline | §§2, 30, 60–61, 79, 85–86, 99; §117 Incident-linked impact assessment | Source-scoped history, observations, receipt, confidence, unknowns | K-INFO and original fact owners |
| I03 Survival and emergency provision | §§17–19, 36, 68, 71; §§118–119, 122 | Current requirement/delivery, forecast horizon, applicable care/exposure profiles | K-ACTOR/K-STOCK/K-NET, relevant care/environment workflow |
| I04 Legacy stock and sites | §§20–23, 35, 55, 79, 104–105, 109 | Historical site use, scoped discovery, recovery, donor loss, stock and handling | K-ASSET/K-STOCK/K-WORK/K-INFO |
| I05 Dependencies and refuge service | §§72–73, 101–103, 109, 121 | Buffer/alternative, useful configuration, occupancy, delivery, commissioning | K-NET/K-ASSET/K-WORK; URBAN coordinates |
| I06 Displacement | §§43, 68, 106, 113, 118, 121–122 | Existing movements, actual presence, households, carried property, immediate needs | K-POP/K-ACTOR/K-STOCK; GOV controls rights |
| I07 Institutional fracture | §§25, 28–30, 38–40, 64–69, 107, 110, 113 | Surviving functions, branches, claims, records, authority, autonomy and succession | K-ORG/K-INFO/K-ACTOR; GOV/LIFE coordinate |
| I08 Replacement vulnerability | §§23, 41, 73–74, 101, 108–110, 114, 117 | Present operation versus support horizon, imports, training and accepted output | K-ASSET/K-WORK/K-NET/K-ORG |
| I09 Regional recovery and successor society | §§62, 69, 72–73, 95–96, 102–103, 107–108, 113–114, 116–117, 121–122 | Routes, regional impact views, programs, durable support and historical claims | Existing Core owners; CIV owns generic program/region views |
| I10 Content and modules | §§3, 53–54, 79, 88, 97, 111–112; Appendices A–C | Exact definitions/selectors, adapters, cause-specific effects, exceptions, adoption | Core content/module contract; selected module computes its exceptional cause |

Core §112 **Slim-engine contract** and Appendix B **Minimum slim-engine manifest** govern the deployment. The section numbers in this document always refer to the pinned v3.2 when prefixed “Core”; PAF references name this document explicitly.

<a id="paf-1-3"></a>
### 1.3 Dependency gate and selected profiles

The provider contracts above exist in the available specification. That establishes documentary coverage, not a fully implemented or adopted runtime. For each enabled interaction, the deployment manifest must record `provider version/hash | relevant Core sections | implementation/runner | adapter/profile ID/version | units/scope | status/evidence | missing data | effective adoption`.

Select one compatible action/effect chain and the needed biological, deprivation, environmental, transport, service-quality, production, institutional and demographic profiles. Core's d100 reference adapter is not a new PAF probability system. PAF introduces **no numerical defaults**. Use Core §112 for necessary missing parameters: a named bounded prospective ruling or defer that calculation while independent authorized activity continues. Do not manufacture rates or choose a PC's missing decision.

For a deployment that adopts this parent, old v1.1 generic procedures become the corresponding Core references. For a campaign that has not adopted it, keep its existing version; a bridge must name the exact old clause, scope, missing provider, conflict resolution and effective date. A bridge is a deployment exception, not an alternate hidden algorithm inside v2.0. Do not claim unconditional Core v3.2 conformance with missing essential services.

<a id="paf-1-4"></a>
### 1.4 Exact receiving binding and declared scope

Select the published IRGS-BIND-APOCALYPTIC-3.2 provider contract, Core IRGS-CORE-3.2, and SCL IRGS-SCL-1.0 with exact PL-1.0 payloads where selected. The [PAF 2.1 binding](IRGS_PAF_Binding_v2_1_Core3_2.json) declares this new genre version and preserves all thirteen existing record identities. The parent contract remains unchanged; this receiving document supplies its current concrete engine selection.

The source binding selects the following provider groups in addition to the task-facing I01–I10 map. All resolve to the same parent, not competing algorithms:

| Binding group | Core 3.2 providers |
|---|---|
| resolution_agency | [§4](Core/IRGS_Core_Engine_v3_2.md#core-4), [§5](Core/IRGS_Core_Engine_v3_2.md#core-5), [§6](Core/IRGS_Core_Engine_v3_2.md#core-6), [§7](Core/IRGS_Core_Engine_v3_2.md#core-7), [§8](Core/IRGS_Core_Engine_v3_2.md#core-8), [§9](Core/IRGS_Core_Engine_v3_2.md#core-9), [§90](Core/IRGS_Core_Engine_v3_2.md#core-90) |
| time_events | [§10](Core/IRGS_Core_Engine_v3_2.md#core-10), [§11](Core/IRGS_Core_Engine_v3_2.md#core-11), [§12](Core/IRGS_Core_Engine_v3_2.md#core-12), [§47](Core/IRGS_Core_Engine_v3_2.md#core-47), [§62](Core/IRGS_Core_Engine_v3_2.md#core-62), [§85](Core/IRGS_Core_Engine_v3_2.md#core-85), [§90](Core/IRGS_Core_Engine_v3_2.md#core-90), [§91](Core/IRGS_Core_Engine_v3_2.md#core-91), [§96](Core/IRGS_Core_Engine_v3_2.md#core-96) |
| actors_conditions | [§14](Core/IRGS_Core_Engine_v3_2.md#core-14), [§15](Core/IRGS_Core_Engine_v3_2.md#core-15), [§16](Core/IRGS_Core_Engine_v3_2.md#core-16), [§17](Core/IRGS_Core_Engine_v3_2.md#core-17), [§18](Core/IRGS_Core_Engine_v3_2.md#core-18), [§19](Core/IRGS_Core_Engine_v3_2.md#core-19), [§64](Core/IRGS_Core_Engine_v3_2.md#core-64), [§68](Core/IRGS_Core_Engine_v3_2.md#core-68), [§69](Core/IRGS_Core_Engine_v3_2.md#core-69), [§70](Core/IRGS_Core_Engine_v3_2.md#core-70), [§71](Core/IRGS_Core_Engine_v3_2.md#core-71), [§106](Core/IRGS_Core_Engine_v3_2.md#core-106), [§118](Core/IRGS_Core_Engine_v3_2.md#core-118), [§122](Core/IRGS_Core_Engine_v3_2.md#core-122) |
| stock_economy | [§12](Core/IRGS_Core_Engine_v3_2.md#core-12), [§20](Core/IRGS_Core_Engine_v3_2.md#core-20), [§22](Core/IRGS_Core_Engine_v3_2.md#core-22), [§24](Core/IRGS_Core_Engine_v3_2.md#core-24), [§35](Core/IRGS_Core_Engine_v3_2.md#core-35), [§36](Core/IRGS_Core_Engine_v3_2.md#core-36), [§37](Core/IRGS_Core_Engine_v3_2.md#core-37), [§38](Core/IRGS_Core_Engine_v3_2.md#core-38), [§105](Core/IRGS_Core_Engine_v3_2.md#core-105), [§109](Core/IRGS_Core_Engine_v3_2.md#core-109), [§114](Core/IRGS_Core_Engine_v3_2.md#core-114) |
| assets_components | [§21](Core/IRGS_Core_Engine_v3_2.md#core-21), [§23](Core/IRGS_Core_Engine_v3_2.md#core-23), [§48](Core/IRGS_Core_Engine_v3_2.md#core-48), [§49](Core/IRGS_Core_Engine_v3_2.md#core-49), [§53](Core/IRGS_Core_Engine_v3_2.md#core-53), [§54](Core/IRGS_Core_Engine_v3_2.md#core-54), [§55](Core/IRGS_Core_Engine_v3_2.md#core-55), [§56](Core/IRGS_Core_Engine_v3_2.md#core-56), [§57](Core/IRGS_Core_Engine_v3_2.md#core-57), [§58](Core/IRGS_Core_Engine_v3_2.md#core-58), [§101](Core/IRGS_Core_Engine_v3_2.md#core-101) |
| work_services | [§23](Core/IRGS_Core_Engine_v3_2.md#core-23), [§41](Core/IRGS_Core_Engine_v3_2.md#core-41), [§43](Core/IRGS_Core_Engine_v3_2.md#core-43), [§71](Core/IRGS_Core_Engine_v3_2.md#core-71), [§72](Core/IRGS_Core_Engine_v3_2.md#core-72), [§73](Core/IRGS_Core_Engine_v3_2.md#core-73), [§101](Core/IRGS_Core_Engine_v3_2.md#core-101), [§102](Core/IRGS_Core_Engine_v3_2.md#core-102), [§103](Core/IRGS_Core_Engine_v3_2.md#core-103), [§104](Core/IRGS_Core_Engine_v3_2.md#core-104), [§107](Core/IRGS_Core_Engine_v3_2.md#core-107), [§108](Core/IRGS_Core_Engine_v3_2.md#core-108), [§110](Core/IRGS_Core_Engine_v3_2.md#core-110), [§119](Core/IRGS_Core_Engine_v3_2.md#core-119), [§121](Core/IRGS_Core_Engine_v3_2.md#core-121) |
| information | [§2](Core/IRGS_Core_Engine_v3_2.md#core-2), [§30](Core/IRGS_Core_Engine_v3_2.md#core-30), [§60](Core/IRGS_Core_Engine_v3_2.md#core-60), [§61](Core/IRGS_Core_Engine_v3_2.md#core-61), [§79](Core/IRGS_Core_Engine_v3_2.md#core-79), [§85](Core/IRGS_Core_Engine_v3_2.md#core-85), [§86](Core/IRGS_Core_Engine_v3_2.md#core-86), [§115](Core/IRGS_Core_Engine_v3_2.md#core-115), [§120](Core/IRGS_Core_Engine_v3_2.md#core-120) |
| institutions_life | [§25](Core/IRGS_Core_Engine_v3_2.md#core-25), [§26](Core/IRGS_Core_Engine_v3_2.md#core-26), [§27](Core/IRGS_Core_Engine_v3_2.md#core-27), [§28](Core/IRGS_Core_Engine_v3_2.md#core-28), [§29](Core/IRGS_Core_Engine_v3_2.md#core-29), [§31](Core/IRGS_Core_Engine_v3_2.md#core-31), [§32](Core/IRGS_Core_Engine_v3_2.md#core-32), [§33](Core/IRGS_Core_Engine_v3_2.md#core-33), [§34](Core/IRGS_Core_Engine_v3_2.md#core-34), [§38](Core/IRGS_Core_Engine_v3_2.md#core-38), [§39](Core/IRGS_Core_Engine_v3_2.md#core-39), [§40](Core/IRGS_Core_Engine_v3_2.md#core-40), [§44](Core/IRGS_Core_Engine_v3_2.md#core-44), [§45](Core/IRGS_Core_Engine_v3_2.md#core-45), [§46](Core/IRGS_Core_Engine_v3_2.md#core-46), [§65](Core/IRGS_Core_Engine_v3_2.md#core-65), [§66](Core/IRGS_Core_Engine_v3_2.md#core-66), [§67](Core/IRGS_Core_Engine_v3_2.md#core-67), [§68](Core/IRGS_Core_Engine_v3_2.md#core-68), [§69](Core/IRGS_Core_Engine_v3_2.md#core-69), [§76](Core/IRGS_Core_Engine_v3_2.md#core-76), [§107](Core/IRGS_Core_Engine_v3_2.md#core-107), [§113](Core/IRGS_Core_Engine_v3_2.md#core-113), [§117](Core/IRGS_Core_Engine_v3_2.md#core-117), [§122](Core/IRGS_Core_Engine_v3_2.md#core-122) |
| content_modules | [§88](Core/IRGS_Core_Engine_v3_2.md#core-88), [§97](Core/IRGS_Core_Engine_v3_2.md#core-97), [§98](Core/IRGS_Core_Engine_v3_2.md#core-98), [§99](Core/IRGS_Core_Engine_v3_2.md#core-99), [§111](Core/IRGS_Core_Engine_v3_2.md#core-111), [§112](Core/IRGS_Core_Engine_v3_2.md#core-112) |

Domains activate as needed: GOV, ECO, INV, MAR, CIV, MED, WILD, INTEL, URBAN and LIFE. Competitions remain Core §123 when an actual competition is enabled; PAF creates no new domain. Shared legacy runtime dependencies are empty under this binding. Historical shared sources and patches are provenance, while genuine local model/content dependencies remain selected.

This specification's default scope is crisis-linked qualitative assessment over supported Core facts; it provides no universal physiology, weapon, hazard or catastrophe-rate model. Its qualitative fallback is a source-scoped statement of known functioning dependencies, unknowns, alternatives and causal review triggers. It may identify vulnerability without inventing a depletion time, probability, casualty count or legal result. Any outcome requiring absent data waits for a complete compatible model or an explicitly named prospective ruling under Core §112. Independent supported activity continues. No gameplay default is silently delegated to improvisation.

<a id="paf-2"></a>
## 2. PAF overlay records and triggers `[PA]`

**Core interface:** I01–I02; Core §§11–12, 85–86, 91 and §117. Overlay identity and visibility do not grant access to hidden Core truth.

An overlay record has `campaign_id | overlay_id/version | as_of/event time | Core entity/event refs | source/provenance/confidence | affected region/function | actor visibility | assessment | next material trigger`. It **cannot** contain an independent spendable stock or duplicate population total. A derived assessment may change when the underlying world changes; its recalculation is not a second physical event.

| PAF overlay | Genre-specific question | Create/update only when |
|---|---|---|
| `PA.Crisis` | Which crisis mechanisms, periods and geographic scope matter? | A cause begins, changes scope, overlaps or ends |
| `PA.RegionalDisruption` | How does a region differ from its established prior functions? | A meaningful function, evidence or assessment horizon changes |
| `PA.Disruption` | Which crisis event threatens multiple dependent functions? | A physical event materially changes connected functions/risks |
| `PA.Pressure` | What crisis-linked consequence is foreseeable, and why? | Its causal forecast, options or affected users change |
| `PA.LegacySite` | What inherited resources/capital have been lost, stripped or remain uncertain? | New site history, depletion, access or evidence changes |
| `PA.DisruptedProvision` | Which former everyday supply pathway is interrupted? | Former/actual provider, substitutes or vulnerability changes |
| `PA.RefugePosture` | What emergency use and constraints apply to an actual inhabited site? | Crisis shelter purpose, occupancy situation or exit options change |
| `PA.DisplacementWave` | Which real movements are related by a crisis and emergency intake burden? | Movement groups, bottlenecks or responding services change |
| `PA.InstitutionFracture` | How has the prior institution split in response to the crisis? | Branches, claims, lost links or reconstitution change |
| `PA.LegacyDependency` | What inherited function lacks reliable future replacement support? | Supply, spares, expertise, replacement horizon or evidence changes |
| `PA.RegionalRecovery` | How does isolation/reconnection affect crisis recovery? | Critical physical/information routes or obligations change |
| `PA.ReconstructionTransition` | How is a specifically disrupted former function being handled? | Restoration strategy, actual program results or vulnerability change |
| `PA.SuccessorAssessment` | What relation does the present social order claim and sustain to the prior one? | Institutional reality, recognition, population or memory changes |

**No compulsory maintenance cycle:** If an overlay is irrelevant, do not instantiate it. If a region is stable for years and no material trigger fires, leave its valid prior state intact. Reports can revise *knowledge/confidence* without rewriting the real event or replenishing stock.

---

<a id="paf-3"></a>
## 3. Crisis context, uneven disruption and propagation `[PA]`

**Core interface:** I01–I03/I05; Core §71 owns forecasts, §§101–103 physical dependency propagation, §109 rates and §117 the generic impact view. The procedure below attaches crisis meaning; it does not rerun propagation.

<a id="paf-3-1"></a>
### 3.1 Crisis and regional context

`Crisis ID | source/module | onset and continuing causal drivers | affected geography | historical baseline refs | present event refs | expected termination/change conditions | confidence/known observers | next trigger`.

The baseline is a recorded historical condition, credible sourced estimate or explicitly proposed starting assumption—never an omniscient reconstruction of an unknown past. Distinguish an actual event from a witness report or interpretation. More than one crisis can affect the same population; each retains its provenance while the shared effects are committed **only once** in Core.

A regional assessment identifies former and current **particular functions** (e.g., potable water, emergency care, administration, food access). Descriptions such as *operating, restricted, interrupted, reconstituting, replaced* are optional local views. “Early collapse,” “recovery,” and “successor era” are contextual labels, not transitions that unlock or penalize anything.

<a id="paf-3-2"></a>
### 3.2 Crisis-specific propagation

`PA.Disruption = initiating event refs | dependent Core service/institution/stock refs | affected users | alternatives/buffers refs | predicted effects/times | evidence and uncertainty | responders and authority | next trigger`.

1. Identify the real initiating physical or social change already processed by Core.
2. Link only genuinely dependent exposed functions; consult actual alternatives, operating modes and service delivery in Core.
3. Record distinct downstream concerns and their causal timing by referencing Core’s supported scheduled or committed effects. An unresolved dependency is passed to its Core owner for evaluation; this assessment never schedules a duplicate physical effect.
4. Update actor-facing information only as observation/reporting occurs.
5. Reassess the overlay on actual capacity, demand, knowledge or causal changes.

A widespread blackout does not automatically break pumps, poison water, terminate government or erase communications. A buffer may delay harm; an independent region can remain intact. A forecasted cascade has not happened until its physical/social preconditions actually occur.

<a id="paf-3-3"></a>
### 3.3 Crisis Continuity Pressure

`PA.Pressure = crisis/disruption refs | affected function/population | Core needs/service/stock forecast refs | expected loss/consequence | projected horizon and assumptions | responses under actual authority | confidence | next review`.

This is the **crisis-facing interpretation** of a Core forecast, not a new survival counter. A need may be supplied now yet vulnerable later; a problem may be resolved permanently. Competing response plans draw on one Core inventory, schedule and authority. When a dependency is restored or demand genuinely changes, revise/remove the pressure rather than forcing a new crisis.

---

<a id="paf-4"></a>
## 4. Inherited scarcity, legacy sites and technical dependence `[PA]`

**Core interface:** I04/I08; Core §§79, 104–105 own discovery/recovery/handling; §§20–23 and 109 stock and condition; §§73, 108–110 support, production and learning.

<a id="paf-4-1"></a>
### 4.1 Legacy-site history

`PA.LegacySite = Core site ref | prior societal function | interruption and occupation history | affected area/resource categories | known Core stocks and installed capital refs | material extracted/lost historically | source observations | unassessed potential | next discovery/change trigger`.

Its distinctive function is relating a **former productive/supply system** to what remains after abandonment, damage, occupation and repeated recovery. Use category- and area-scoped depletion descriptions only when helpful: *Untouched, Disturbed, Picked Over, Stripped, Salvage Exhausted*. These are optional Core-recognized descriptive assessments, not PAF-only depletion mechanics or guaranteed stock quantities. A stripped shop may retain a working lathe; an unknown basement is not empty because an upstairs survey found nothing.

Core establishes underlying contents, search, access, physical recovery, transport, dismantling and condition. PAF may refer to *legacy reserve, recovered inheritance, imported aid, restored production or new production* as source provenance. The tags cannot mint a spare part, make a medicine safe, or grant manufacturing capability. Repeat site visits do not respawn contents; other actors can change actual site state through normal autonomous activity.

<a id="paf-4-2"></a>
### 4.2 Inherited technical-capability gap

`PA.LegacyDependency = asset/product/service refs | inherited original support environment | present operating role | Core sustain/repair/fabrication/reproduction assessments | lost/fragile supporting prerequisites | known substitute/import options | operating horizon forecast | ongoing closure work refs | confidence`.

PAF tracks **historical dependency on capital that still works despite loss of the society that supplied it**. It does not own the universal ladder from possession to industrial production. Distinguish two independent questions:

- Can the capability operate **now**, under actual staffing, inputs, service and available spares?
- Can the society maintain or replace it **over the stated horizon**, locally or through reliable accessible external networks?

Current success is not erased by future vulnerability. Conversely, a complete manual, a salvaged device or one prototype does not establish reproducibility. No arbitrary “tech decay” or universal civilization-level penalty applies. Change the actual support dependency or the exposure assessment only when there is a cause.

---

<a id="paf-5"></a>
## 5. Emergency provision, refuges and displacement `[PA]`

**Core interface:** I03/I05/I06; Core §§71–72, 103, 106, 118, 121–122 own needs, occupation, movements, care and service delivery. Core §113 owns relevant rights and authority.

<a id="paf-5-1"></a>
### 5.1 Provision disrupted from its normal source

`PA.DisruptedProvision = Core consumer/requirement refs | previous ordinary provision source | crisis-disrupted dependency | actual substitute/reserve refs | unresolved critical exposure | time/season | responding institution | relocation/continuity alternatives`.

A customary supplier may disappear while remaining supplies, private property, alternative delivery, emergency assistance or local production continue. The overlay asks **which formerly normal support is broken** and how its loss alters the crisis response. Core owns requirement amounts, treatment, rationing, inventories and allocation. No special apocalypse starvation, disease or panic roll is implied by a label.

<a id="paf-5-2"></a>
### 5.2 Emergency refuge posture

`PA.RefugePosture = Core site/population refs | previous site function | emergency habitation/use | existing and forecast occupants kept distinct | unmet services / access / hazards | temporary management arrangement | relocation or durable-use options | decision authority`.

A school, convoy, home, hospital, camp or functioning town can serve as refuge. The designation creates no additional beds, residents, personnel or stock. A refuge can remain temporary, become a permanent settlement through *actual* Core development, or be abandoned without an automatic progression sequence. If demand exceeds capability, the affected people remain present and the unmet requirement is real.

<a id="paf-5-3"></a>
### 5.3 Crisis-linked displacement waves

`PA.DisplacementWave = crisis/region ref | underlying Core movement event refs/cohorts | displacement causes/windows | access and transit constraints | dependants/care/cargo dependencies | receiving services | unresolved safe-return or resettlement issues`.

This groups **already existing or authorized** movements for emergency coordination; it is not a second population count. Core processes each departure, transit, arrival, injury, provision and custody event. Reports of people en route can change forecast demand and actual preparation commitments; they do not add actual occupants or their consumption at the destination before arrival. People in transit retain their own current needs through Core §§71 and 106. Displacement does not automatically establish citizenship, work consent, hostility, infection or communal ownership. The wave record tracks crisis-specific intake strain, prolonged emergency accommodation and return/relocation alternatives, never an imposed political policy.

---

<a id="paf-6"></a>
## 6. Institutional fracture and regional isolation `[PA]`

**Core interface:** I07/I09; Core §§28–30, 107, 113 own authority and succession; §§102, 116–117 own flows and regional coordination; §§64–65 preserve autonomous actors.

<a id="paf-6-1"></a>
### 6.1 Fracture relative to the prior order

`PA.InstitutionFracture = prior Core institution ref | interrupted people/offices/records/links | independently surviving branches | functions still delivered | rival or partial continuity claims | emergency substitutes | historical obligations | possible reconstitution/reconnection | evidence`.

A crisis can sever coordination without automatically dissolving every office, law, contract or department. Record **what survived**, which branches can act with their own actual information/resources, which continuation claims conflict, and what institutional ties would require restoration or replacement. Core GOV/K-ORG adjudicates authority, recognition, control, staffing and succession; PAF explains the crisis relationship to the former structure. A later successor may inherit employees and archives without inheriting every treaty, debt or claim.

<a id="paf-6-2"></a>
### 6.2 Crisis-related network loss and rejoining

`PA.RegionalRecovery = affected region/node refs | documented prior interdependence | crisis-broken material/information links | surviving alternative pathways | shortages/response consequences | restoration projects/agreements refs | remaining exposure | next review`.

PAF highlights what **regional separation means for survival/recovery**, not how network traffic is mechanically routed. Communication may survive while freight fails. Regional surplus may be inaccessible. Mutual aid, trade, shared facilities, federated government and annexation are distinct choices and outcomes. Reconnection can provide genuine prosperity without forcing political unity, independence or a new vulnerability penalty.

---

<a id="paf-7"></a>
## 7. Reconstruction transitions and successor societies `[PA]`

**Core interface:** I08–I09; Core §§72–73, 103, 107–108, 117 and 121 own projects, acceptance and support; §§69, 95–96, 113 and 122 own generational/legal/life consequences.

<a id="paf-7-1"></a>
### 7.1 Transition from disrupted inheritance

`PA.ReconstructionTransition = crisis/prior function ref | damaged or interrupted present support | chosen response: repair, restore, replace, adapt, redesign or abandon | Core program/service refs | temporary arrangements and real obligations | achieved acceptance refs | residual inherited dependencies | population/institution effects`.

The overlay records the **relationship between prior failure and the society's chosen replacement**, not project progress or actual commissioning. A temporary workaround may give real service now, while long-term capability is unresolved. An adapted system can legitimately outperform the old one; rebuilding original topology is not obligatory. Core handles qualified work, installed assets, inspection, commissioning, deliveries, operator coverage and accepted durable output. An optional abandonment decision preserves relevant environmental, legal, social and material consequences.

<a id="paf-7-2"></a>
### 7.2 Successor assessment

`PA.SuccessorAssessment = polity/society and prior-order refs | explicit continuity/novelty claims | current Core authority/recognition/control | surviving population, property, records and obligations | actually supported ordinary services | dependent/renewable productive capability | institutional and cultural memory | unresolved historical claims | crisis residues`.

A “successor society” is a historical/organizational assessment, not an upgrade tier, second government or automatically legitimate heir. Some institutions survive unchanged; others fragment or arise anew. Later people remember events through actual teaching, records, observation and interpretations. A stable successor order can persist indefinitely; return to crisis needs an event, not a narrative balancing requirement.

---

<a id="paf-8"></a>
## 8. Crisis and extraordinary modules `[MODULE]`

**Core interface:** I10; Core §112 owns the module contract, §§17–19 and 53–54 effects/exposure, §§118–119 care/environment, and §70 ordinary death. No exception is active in base PAF v2.1.

The foundation works with mundane disasters alone. Fires, floods, droughts, epidemics, contamination, industrial failure and conventional war use the appropriate Core procedure plus **selected cause-specific environment, medical, technological or conflict profiles**. PAF links their consequences into crisis assessments; it does not own a second dose, infection, force, injury or power system.

Optional nuclear, zombie, alien, magical, mutational, temporal or death-loop premises require an explicit module contract:

`Module ID/version | causal mechanism | source, extent and triggers | target and exposure rules | required Core interfaces | actual effects/events | observation/detection | interventions | limits/costs | explicit overrides | calibration evidence | stop/termination behavior | acceptance cases`.

The sequence **source → spread/presence → exposure → impairment/effect → observation/intervention** is an interface description, not free automatic harm at each arrow. The module defines its own exceptional mechanics and applies results once to actual Core actors/assets/services. One attack/exposure never becomes several independent injuries merely because multiple overlays reference it. **Zero-theme requirement:** disable every extraordinary module; crisis/disruption/recovery remain supported.

---

<a id="paf-9"></a>
## 9. Game initialization and running the genre overlay

**Core interface:** I01/I02/I10; Core §§79, 88–91, 97, 99, 111–112. This section supplies genre inputs and subscriptions to the shared runtime, not another clock or event loop.

<a id="paf-9-1"></a>
### 9.1 Campaign profile additions `[PROFILE]`

`Selected Core and PAF versions/status | CCL/genre-content identities | date/place/geography | crisis cause/onset/tempo/extent | continuing drivers/stop conditions | baseline evidence and uncertainty | actual starting regional functions | legacy sites/resources/support | displaced populations/emergency use | institutional remnant claims | affected supply and networks | relevant successor context | enabled modules | calibrated parameters | visibility/hidden-state capability | pending events | overrides/compatibility bridge`.

These are **profile inputs**, not initialized quantities or retrospective world facts. Do not generate an apocalypse-wide ruin state because the genre is selected. Prepare only the detail needed for starting decisions and warranted background processes.

<a id="paf-9-2"></a>
### 9.2 Initialization procedure

1. Pin adopted Core/CCL/genre/profile versions, including compatible physical, care and effect adapters; identify missing Core functions and select a documented bridge or defer the unsupported deployment.
2. Establish premise and actually selected crisis drivers/geography. Gather sourced pre-disruption history, proposed assumptions and genuine unknowns without conflating them.
3. Generate or load actual starting people, property, infrastructure, routes, institutions, stock and events **through Core once** under an authorized world-generation policy.
4. Record true material state and each actor's known information separately.
5. Instantiate only decision-relevant PAF overlays from linked Core data; identify their causal next review, not a daily blanket refresh.
6. Test required dependencies, starting resource balances and initial scene/player choice. No automatically imposed goal, political loyalty or voluntary act.

<a id="paf-9-3"></a>
### 9.3 Runtime update triggers

When Core commits a relevant event, PAF may update affected overlays as a derived phase of the same event; **PAF never commits the same event again**. Recommended triggers: crisis onset/change; asset/service interruption; newly observed resource depletion; emergency change of site use; real population movement; institution split/reconnection; disappearance/replacement of specialist support; network partition/relink; accepted restoration/redesign; material change in continuity forecast; new incoming report. Independent simultaneous physical effects use the Core pre-event state; a later report revises beliefs/confidence only.

Detail and review cadence follow actual decision relevance. Aggregated regions and detailed scenes read the same people, inventory, work, service, ownership and history. Off-screen actors remain autonomous. No free work, fresh stores, reset hazard or doubled casualty on a scale change.

<a id="paf-9-4"></a>
### 9.4 Content boundary and SCL v1.0

Use **Core Content Entry → Crisis/Setting Variant → Campaign Instance** under Core §111. Pin SCL v1.0 and its exact registry; resolve namespace, family, revision, selector, semantic type and target checksum. The [193-entry PAF map](IRGS_PAF_Content_References_v2_1.csv) resolves 191 shared references—39 selected qualitative and 152 source-backed holds—and two retained scoped extensions, APX-X01 and CPF-PA-BASE. Scoped extensions have exact source/payload identities, not invented shared aliases. The catalogue remains read-only and implies neither setting availability nor operational performance. Reference, activation and deprecation are separate gates. An original `PL:<ID>@1.0` alias may resolve to a selected shared contract, exact source-backed content or a retained scoped extension. Keep its exact payload and necessary profile available; a name/hash alone is not the usable definition.

The registry retains 51 selected qualitative contracts, 228 held family candidates (235 source references) and 18 scoped extensions across its source families. These are catalogue-wide counts, not PAF-only counts. A held candidate can use its preserved original content without reactivating an older generic engine loop; it cannot masquerade as a completed shared replacement. This release checks PL source bindings, aliases and payload checksums against the pinned registry; no campaign instances are generated.

Ordinary item, site, service and project behavior inherits Core. Apocalypse-specific APX variants, crisis-damaged or abandoned-site context, legacy vulnerability presets and exceptional theme profiles retain their scoped application. No APX name grants an effect, and no catalogue attachment imports Hour Zero history. A campaign selects actual entries and profiles at its decision-relevant scope; this foundation does not preload the catalogue as world state.

The packaged [Post-Apocalyptic Content Library v2.0](PALibrary/IRGS_Post_Apocalyptic_Content_Library_v2_0_Candidate.md) adds 43 optional PA-CNT compositions over those same 193 references. Its exact content and proposed status remain unchanged. This new PAF v2.1 supplies the current receiving pin; the library’s references to PAF v2.0/Core 3.1 describe its predecessor context. See Appendix E and [the current library receiving record](PALibrary/PAF_Library_Receiving_v2_1.json). No composition is enabled or instantiated by packaging.

<a id="paf-9-5"></a>
### 9.5 Overlay lifecycle and output contract

PAF consumes committed Core event references or received evidence. It produces `overlay_assessment_created`, `overlay_assessment_revised` or `overlay_assessment_closed` metadata, plus references to possible responses for an authorized actor. These are proposed PAF audit labels, not new Core physical event types. A response is an option until actually authorized under Core §§4–5/29/83; existing NPC mandates continue under §§64–65.

One record may link several causes; one cause may inform several views. Use `campaign_id + overlay_id + source_event_id + assessment_revision` to identify the assessment update. Core §91 remains the authority for physical replay; repeated rendering or delivery of an already processed source event cannot create another physical transaction. A corrected assessment adds its evidence/revision history; Core §99 governs any separate correction of world state.

Close an active pressure when its causal forecast no longer applies. Archive a crisis/refuge/wave assessment when its decision-relevant emergency purpose ends; retain its historical links. A legacy dependency or successor assessment can remain relevant after the active crisis ends. Ending the crisis does not delete injuries, obligations, loss, pollution or unfinished work. No update is required merely because a turn, day, generation or scale presentation changed.

Projection visibility is actor-scoped. A runner's hidden assessment must not leak into a PC-facing panel. If hidden-state persistence is unavailable, record that limitation under Core §§86/112; unknown sites and future outcomes cannot be silently invented anew each visit.

<a id="paf-9-6"></a>
### 9.6 Module-specific activation checklist

The §8 contract specializes Core §112 with `crisis ID | source/access/method | valid targets | presence/spread | exposure | optional accumulated burden | impairment channel | evidence/detection | intervention/counterplay | persistence | termination`. The module must name costs, units, update law, retained processed spans, limits, exact read/write owners and applicable overrides. State whether two effects are distinct causal channels or two reports of the same effect. Distinct injuries may coexist; deduplication removes duplicate application, not real additional harm.

For nuclear, epidemic or contamination premises, choose a cause-specific profile before calculating exposure/effect. For zombie, alien or magical premises, define actual capabilities and limits rather than infer them from the name. For death loops/resurrection, explicitly reconcile identity, inventory, clock, memory, estates, offices and other actors with Core §§3–4, 12, 69–70, 97 and 112. Base v2.1 selects none of these overrides. Cessation of a source stops future contribution; accumulated exposure and downstream processes retain their own Core/profile recovery rules.

<a id="paf-10"></a>
## 10. Acceptance and regression matrix

**All rows in §§10.1–10.3 are specified acceptance requirements, not executed gameplay or simulation results in this release.** “Retained” means its expected behavior is preserved. The structural audit verifies presence and reference coverage only. A future run records `case ID | exact release set | profiles and synthetic/empirical input status | prestate | declarations/authority | timed events | expected output | observed output | discrepancy | correction/retest | runner`.

<a id="paf-10-1"></a>
### 10.1 Retained v1.3 genre gates

Old case IDs remain stable for traceability. PA13-17 now tests explicit bridge/deployment handling under Core §112 rather than treating the old v2.2 intake as the current provider. No test grants adoption.

| ID | Scenario | Required result | Provider | Status |
|---|---|---|---|---|
| PA13-01 | One storm: region A restores power, region B loses water, region C remains intact | Separate regional/domain crisis views; no global stage or level | I02/I09 | Specified; retained |
| PA13-02 | Ordinary blackout; water tank still delivers water | Crisis pressure forecasts delayed vulnerability using Core; no immediate fake loss | I03/I05 | Specified; retained |
| PA13-03 | Outage report arrives after repair | Report updates actor knowledge/assessment only; no second service interruption | I01/I02 | Specified; retained |
| PA13-04 | Two crises expose one hospital's same generator | Two linked causes, one actual generator and finite capacity/fuel; no duplicated consumption | I01/I05 | Specified; retained |
| PA13-05 | Known former pharmacy has no actual usable medication | LegacySite history cannot create medicine or override Core inventory | I04 | Specified; retained |
| PA13-06 | Stripped factory still contains usable installed machines | Separate category/area and installed-capital assessment; do not erase productive asset | I04 | Specified; retained |
| PA13-07 | Technicians depart while their equipment still works | LegacyDependency horizon worsens; no immediate invented machine failure | I08 | Specified; retained |
| PA13-08 | Radio contact restored; food convoy route still impassable | RegionalRecovery improves information only; no phantom food delivery | I09 | Specified; retained |
| PA13-09 | School becomes emergency refuge during flood | RefugePosture creates no additional people, beds, water or civic authority | I05 | Specified; retained |
| PA13-10 | A 120-person displaced wave splits across two actual destinations | Wave groups real movements; no duplicate population or automatic citizenship | I06 | Specified; retained |
| PA13-11 | Government's branches operate separately and claim succession | InstitutionFracture preserves function-specific service, claims and partial continuity | I07 | Specified; retained |
| PA13-12 | Bridge construction complete but access approaches unready | ReconstructionTransition remains limited to accepted Core service; no false durable completion | I05/I09 | Specified; retained |
| PA13-13 | New distributed power replaces failed historic centralized service | Redesign is legitimate transition; former topology need not be restored | I09 | Specified; retained |
| PA13-14 | Stable successor society persists through uneventful years | No imposed scarcity decay, uprising, apocalypse phase or harder foe | I09 | Specified; retained |
| PA13-15 | Nuclear and ordinary fire profiles affect same real casualty | Cause-specific module effects, Core injury once per supported physical event; overlays do not re-injure | I03/I10 | Specified; retained |
| PA13-16 | Disable every extraordinary module | Mundane crisis, legacy depletion, fracture, refuge, recovery and successor paths remain supported | I10 | Specified; retained |
| PA13-17 | Incomplete proposed Core implementation selected | Reject unconditional adoption; use an explicitly scoped bridge or defer unsupported deployment under Core §112 | I10 | Specified; retained |
| PA13-18 | Change presentation from region to building and back | Same Core event/stock/actor IDs; overlay summaries cause no additional charges | I01/I09 | Specified; retained |
| PA13-19 | No inherited reserves left but newly accepted local production is adequate | Legacy scarcity can end without invented replacement shortage | I04/I08 | Specified; retained |
| PA13-20 | Child arrives within refugee wave with private supplies | Actual demands/property/rights determined in Core; PA wave neither creates worker nor communal confiscation | I06 | Specified; retained |
| PA13-21 | Two successor governments claim an old treaty | PAF represents competing historical claims; GOV determines legal/practical status through actual process | I07/I09 | Specified; retained |
| PA13-22 | A long-term rebuilding program is canceled for a peaceful local alternative | Program choice remains real; no compelled reconstruction ladder or punishment | I09 | Specified; retained |

<a id="paf-10-2"></a>
### 10.2 New v2.0 integration gates

| ID | Scenario | Required result | Provider | Status |
|---|---|---|---|---|
| PA20-01 | The preceding PAF pins Core 3.1; this deployment selects confirmed Core 3.2 and SCL 1.0 | Pin exact current bytes, providers and catalogue; preserve separate PAF clause status and campaign adoption; no automatic later upgrade | I10 | Specified; receiving locator revised in v2.1 |
| PA20-02 | Known legacy store revisited repeatedly after stock exhausted | No respawn; newly opened area changes access/evidence only until Core establishes/retrieves real stock | I04 | Specified; new |
| PA20-03 | A 120-person wave splits: 70 arrive A; 50 remain in transit | Origin 0, A 70, transit 50, B 0 for this cohort; destination forecast separate from current need; total 120 | I06 | Specified; new |
| PA20-04 | Two indivisible services each require 6 units; shared budget is 10 | At most one runs simultaneously unless another supported configuration exists; no two fractional full services | I05 | Specified; new |
| PA20-05 | Generator and powered fuel pump each require the other to start | No bootstrap; record required black-start means without fabricating them | I05 | Specified; new |
| PA20-06 | Relief proposal needs new PC payment or evacuation after Mixed | Preserve actual work/costs; return the new voluntary decision; no implied spending or movement | I01/I06 | Specified; new |
| PA20-07 | Local part fabrication unavailable but reliable imports support the horizon | Record imported support; no compulsory self-sufficiency penalty; current service persists | I08/I09 | Specified; new |
| PA20-08 | Source stops while accumulated exposure remains | Stop future input only; apply selected persistence/recovery; no instant cure | I03/I10 | Specified; new |
| PA20-09 | Same cause appears in three overlays and its event is replayed | One Core effect; reference updates only; distinct real downstream effects still occur at their times | I01 | Specified; new |
| PA20-10 | A crisis ends with an unfinished repair and private debt | Archive crisis context; preserve work, obligations, property and consequences | I07/I09 | Specified; new |
| PA20-11 | Only source report says an unknown controller cannot be reproduced | Preserve source/confidence and unknown truth; do not turn a claim into proven impossibility | I02/I08 | Specified; new |
| PA20-12 | Two campaigns share content IDs and a similarly named event | Campaign-scoped identities; no cross-campaign stock, lore or event application | I01/I10 | Specified; new |
| PA20-13 | SCL/PBC alias points to an incomplete replacement definition | Retain complete selected source definition; no substitute performance inferred from identifier | I10 | Specified; new |
| PA20-14 | Refuge demand rises at arrival before administrative registration | Immediate physical demand; legal status and labor availability remain independent | I03/I06 | Specified; new |
| PA20-15 | Quiet ten-year interval with no selected demographic or wear rates | No fabricated counts or decay; preserve supported state, flag required unresolved projections and continue independent supported activity | I08/I09 | Specified; new |

<a id="paf-10-3"></a>
### 10.3 Retained Core and v1.1 backlog

Core v3.2 Appendix C **Post-apocalyptic interface gates** is the exact home of CW-PA-01–20; do not execute a second PAF copy of the same event procedure. The source matrix (§12) links all twelve intake rows to receiving Core sections. The complete v1.1 PA-01–62 scenario/expected-result inventory is retained in Appendix A below with provider mapping. This preserves recoverable legacy checks without treating all 62 as new or independent tests.

Standalone PAF v1.2 has now been recovered in full from the named source. Its 26 exact PA12-01–26 scenario/expected-result rows are retained in Appendix D and the acceptance inventory, with current provider routing and original wording recorded separately. The former documentary source gap is closed. Recovered requirements are specifications, not newly executed gameplay or proof of full runtime equivalence. Library v2 adds 63 separate content acceptance specifications in its companion CSV; Appendix E defines their receiving scope.

<a id="paf-10-4"></a>
### 10.4 Coverage and future execution

Routine/zero-theme: PA13-14/16/19, PA20-15. Edge/extreme: PA13-06/20, PA20-04/05. Scarcity/repetition: PA13-05, PA20-02. Failure/Mixed/agency: PA13-12/22, PA20-06. Simultaneity/accounting: PA13-04/10, PA20-03/04/09. Scale: PA13-18, CW-PA-14. Information: PA13-03, PA20-11. Modules/persistence: PA13-15/16, PA20-08. Exploits: PA20-02/05/09/12/13. Migration/status: PA13-17, PA20-01/13.

For AI reproducibility, give two independent runners the same pinned sources, profile, hidden/visible state, event order, choices and random record if used. Compare committed IDs, quantities, times, authorized actions and information receipts; narrative wording may differ. Test coarse and fine presentation over identical processed spans. Record divergence rather than labeling agreement on a prose expectation a mechanical pass. This independent reconstruction/live execution remains pending.

<a id="paf-11"></a>
## 11. Worked specification traces and evidence limits

These are retained manually reasoned synthetic examples, **not live gameplay or calibration**. The fresh v2.1 reference suite exercises explicitly named bounded portions of their arithmetic/state behavior; it does not claim full scenario implementation. Numbers exist only inside their stated fixtures.

| Trace | Given state / cause | Expected causal result | Core reference and PAF output |
|---|---|---|---|
| W1 Buffered outage | At 08:00 pump loses power; usable tank 120 L, constant delivered demand 10 L/h, no replenishment or other limits; repair actually finishes 10:00 | At 10:00 tank is 100 L; no downstream water outage occurred. Original no-repair exhaustion forecast was 20:00. Any new replenishment rate must be supplied before projecting farther | §§71, 101, 103, 109; PA.Disruption records pump outage; PA.Pressure revises forecast, does not inflict dehydration |
| W2 Finite inherited stock | 12 usable units at site, authorized transfer 7 to transit; later receipt of those 7; report received again | Site 5, transit 7, destination 0 before receipt; then 5/0/7; report changes no quantity. Global physical total stays 12 absent another event | §§12, 35, 104–105; PA.LegacySite records extraction history, not a new stock |
| W3 Wave split | 120 existing people depart; 70 reach A and 50 remain travelling to B | Physical cohort count 0 at origin + 70 at A + 50 in transit + 0 at B = 120. Transit needs continue; B forecasts 50 but has no arrivals yet | §§71, 106; PA.DisplacementWave groups existing movement IDs |
| W4 Replacement gap | Working generator has supported fuel, crew and service; controller fabrication lost; replacement forecast unknown; reliable import later established | Current delivery is unchanged by loss of fabrication alone. Horizon assessment first becomes uncertain, then references evidence-supported imports; no invented failure date | §§103, 108; PA.LegacyDependency separates present operation, unknown replacement, supported import horizon |
| W5 Accepted redesign | Old grid remains broken; newly built microgrid passes declared tests with actual operators, inputs, distribution and support | Only demonstrated end-user service is accepted; its users can have durable recovery without reconstructing the old grid. Other regions may remain interrupted | §§72–73, 103, 117, 121; PA.ReconstructionTransition records redesign and residual scope |
| W6 Late report | Bridge fails 14:00, repaired 14:15, outage report reaches dispatcher 14:20; dispatcher has no repair report | Truth is repaired; dispatcher may believe bridge remains closed. No second break at 14:20. Its resulting routing choice uses actual knowledge/authority | §§30, 85, 91, 102; PA.RegionalRecovery keeps truth and actor-visible assessment distinct |

No trace establishes plausible human consumption, repair time, yield, demographic rates or balance. The current verification report and verification_results.json distinguish structural checks and bounded transition probes from these full worked scenarios, inherited acceptance requirements and unexecuted gameplay.

<a id="paf-12"></a>
## 12. CMRR source, ownership and removals matrix

<a id="paf-12-1"></a>
### 12.1 Comparison basis and limits

This receiving comparison uses supplied complete PAF 2.0 revision 2, original PAF v1.1, recovered standalone slim PAF v1.2, slim v1.3, original PL v1.0, the new PACL v2.0 package, and current Core 3.2/SCL 1.0. Each recovered numbered heading and each PA-CNT composition has a disposition in the expanded reconciliation matrix. The former v1.2 source gap is closed by direct full-text recovery, size verification and a retained SHA256; no inherited requirement becomes a gameplay pass merely through recovery.

Comparison is bidirectional: old functions are assigned receiving owners below and in Appendices A/D; each current genre overlay is traced to its source lineage and the exclusion register; Core's twelve intake dispositions are checked against their actual receiving sections. Direct v1.2 source headings and all 26 case definitions are compared; complete runtime equivalence remains a behavioral qualification requirement.

<a id="paf-12-2"></a>
### 12.2 Intake-to-Core and retained genre functions

| Patch / recovered v1.2 locator | Earlier v1.1 scope | Verified Core v3.2 receiving owner | Current v2.1 retained destination | Reconciliation |
|---|---|---|---|---|
| PA-CW-01; §§2–3 | §4 | §117 Incident-linked impact assessment; §§2, 11, 85, 91 | §§2–3: PA.Crisis, PA.RegionalDisruption, PA.Disruption | Split generic impact view from crisis interpretation; no new incident ledger |
| PA-CW-02; §3 | §§5, 12 | §§71, 101, 103, 109 | §3: PA.Pressure; §5: PA.DisruptedProvision | Remove survival/countdown arithmetic from genre ownership; retain lost-normal-support meaning |
| PA-CW-03; §4 | §6 | §§79, 104–105; §§20–23, 35, 109 | §4: PA.LegacySite | Relocate discovery, extraction, donor loss, containers and depletion quantities; keep inherited history |
| PA-CW-04; §5 | §§5, 8 | §§71–72, 103, 121–122 | §5: PA.DisruptedProvision, PA.RefugePosture | Core owns temporary/durable service gates; PAF emergency purpose remains |
| PA-CW-05; §6 | §9 | §§106, 113, 118, 121–122 | §5: PA.DisplacementWave | Actual movements, needs, property and rights remain Core; wave is grouping only |
| PA-CW-06; §7 | §10 | §§28, 107, 113; §§64–69, 110 | §6: PA.InstitutionFracture | Core normal succession/function, PAF prior-order fragmentation; no legitimacy meter |
| PA-CW-07; §8 | §§11–12 | §§108, 117; §§73, 109–110 | §4: PA.LegacyDependency | Independent support assessments replace any implied ladder; imports can sustain recovery |
| PA-CW-08; §9 | §13 | §§102, 116–117 | §6: PA.RegionalRecovery | Core routing/flow and agreements; PAF crisis isolation/reconnection meaning |
| PA-CW-09; §10 | §14 | §§72–73, 103, 117, 121; §§69, 107–108, 113 | §7: PA.ReconstructionTransition, PA.SuccessorAssessment | Generic program ownership moves from old PA-RECON to CIV/K-WORK; PAF relation to past remains |
| PA-CW-10; §11 | §15 | §§5, 17, 19, 53–54, 112, 118–119 | §8 and §9.6: cause-specific module integration | No PAF dose/injury solver; preserve exceptional mechanism contract |
| PA-CW-11; §12 | §§4, 16 | §§79, 88–91, 111–112 | §9: crisis profile and overlay subscriptions | Remove parallel generation/runtime; content type does not instantiate campaign facts |
| PA-CW-12; §§13–16 | §§17–19 | §§97, 99, 112; current Appendices A–D | §§10–15: tests, Hour Zero boundary, adoption and provenance | Rebuild documentation; do not import old validation/adoption claims |

The historical patch dispositions remain provenance: PA-CW-01 was merged, 04/07/09 revised, and the others covered by shared owners. Current functions are located directly in the table above, not an absent historical Core appendix. E-01 uses §117; E-02 §108; E-03 §§72/103. No patch is an additional active runtime layer.

<a id="paf-12-3"></a>
### 12.3 v1.3 section coverage and receiving changes

| v1.3 source | Current v2.1 destination | Retain / change / reason |
|---|---|---|
| Header; §1 | Header; §1 | Replace unresolved v2.2 intake dependencies with exact v3.2 pin; parent baseline confirmed, campaign adoption separate |
| §2 | §2; §9.5 | Retain all thirteen record identities/triggers; add lifecycle, visibility and assessment-only output contract |
| §3 | §3 | Retain uneven crisis propagation and pressure; bind physical propagation to Core §§101–103 |
| §4 | §4 | Retain inherited stock history and replacement vulnerability; bind Core §§104–105/108 |
| §5 | §5 | Retain emergency survival/refuge/displacement; clarify destination forecast versus actual presence and transit needs |
| §6 | §6 | Retain fracture and regional isolation; no automatic rights or political union |
| §7 | §7 | Retain reconstruction/successor functions; explicitly include repair alongside other strategies |
| §8 | §8; §9.6 | Retain zero-theme and extraordinary contracts; require persistence, channel, identity and exact overrides |
| §9 | §9 | Retain trigger-based overlay runtime; reference Core generation/content and one runtime |
| §10 | §§10–11; Appendix A | Retain 22 cases/IDs; add 15 integration gates, six worked traces and legacy backlog; execution status explicit |
| §11 | §12; Appendix A/D | Rebuild ownership/removals matrix against actual receiving Core; recovered v1.2 clauses and cases now directly inventoried |
| §12 | §§13–15 | Preserve Hour Zero boundary and prospective migration; replace old dependency/status register with exact source hashes |

<a id="paf-12-4"></a>
### 12.4 Accounted removals, corrections and holds

| Removed/replaced interpretation or ownership | Receiving treatment | Why no valid function is lost |
|---|---|---|
| v1.3 unpinned K-owner references and v2.2 dependency requirements | §1.2 names v3.2 section providers | Owner aliases remain useful; actual procedure is locatable |
| Generic PAF stock/needs/survival-horizon arithmetic from v1.1 | Core §§12, 36, 71, 109 | Same function inherited once; forecasts never current stock |
| v1.1 provision formula could be read as adding accessible future supply to current provision | Core §71 separates actual usable stock/delivery from expected scenario | Correct ambiguity; no convoy counted before actual arrival |
| PAF-only site depletion/recovery/handling procedure | Core §§79, 104–105 | Scope-specific histories remain §4; finite resources and donor loss retained |
| Generic infrastructure, population, institution, technology, route and reconstruction algorithms | Core §§101–109, 117/121 and related owners | Every family mapped in §12.2; old generic record IDs migrate by meaning, not deletion |
| Any reading of capability assessments or service gates as a compulsory ladder | Core §§72, 103, 108 | Independent capability and applicable accomplishments preserved |
| Automatic bridge from v1.1 merely because a provider is missing | §1.3 and §14 require explicit scoped selection | Unsupported deployment is identified; adopted campaign rule persists until changed |
| PAF-specific content identifiers treated as automatically replaced by SCL/PBC | Hold under Core §111 and §9.4 | Full definitions/selectors remain selected until a validated explicit mapping exists |
| v1.2 completeness inferred from successor summaries | Direct recovered source; Appendix D and 26 PA12 rows | Replace inference with a source/heading/case comparison; runtime equivalence still requires execution |
| Global collapse levels, repeat loot, forced regression, new resource charges from views | Rejected; Core §§4, 12, 79, 91–95 and this genre's causal limits | These are invalid behaviors, not functions to preserve |
| Hour Zero lore as general default | §14.4 module/campaign boundary | Reference precedent preserved; campaign content never transferred |

No adopted rule is deprecated in an existing campaign by this publication. No unique crisis-specific function in the directly recovered v1.1/v1.2/v1.3 sources is intentionally removed. Every recovered numbered heading and exact case row has a disposition; full semantic and behavioral equivalence remains subject to the stated implementation and acceptance gates.

<a id="paf-13"></a>
## 13. Calibration gaps and unresolved decisions

No PAF-wide consumption, depletion, decay, panic, political legitimacy or recovery multiplier is supplied. Each necessary parameter record must contain `purpose | owner | profile ID/version | unit | formula/update law | bounds/extremes | inputs | uncertainty | evidence/status | time span/threshold | stop/recovery | tests`. Unknown is not zero. Qualitative ranges are sufficient when exact values do not affect the decision.

| Gap | Owner / dependency | Required evidence and acceptance target |
|---|---|---|
| Crisis onset, spread, overlapping drivers and cessation | Module; Core §§19, 101, 109, 112, 119 | Cause-specific supported mechanism; no generic catastrophe clock; test overlapping causes and cessation |
| Needs, deprivation, care and refuge quality | Profile; Core §§17–19, 71, 118, 121–122 | Species/context, season, minimum/preferred service, onset/recovery; test shortfall without duplicate injury |
| Legacy stock history, survey reach, spoilage and contamination | Content/profile; Core §§79, 104–105 | Plausible pre-crisis holdings and actual prior losses; survey uncertainty separate from quantity; no age-based free depletion |
| Recovery yield, handling, transport and route constraints | Profile; Core §§35, 102, 104–105, 116 | Units, loading/travel/unloading, tools, quality and donor impacts; test finite stock and route competition |
| Service capacity, buffers, startup and acceptance | Profile; Core §§101–103, 109 | Useful operating bundles, quality, start/run needs, maintenance; test partial backup and black start |
| Replacement, production and specialist renewal | Profile/content; Core §§73, 108–110 | Wear/fault mechanisms, tooling, yield, throughput, training evidence, imports and horizon; distinguish working now from replaceable later |
| Displacement tempo and household demand | Campaign/profile; Core §§68, 106, 118, 122 | Geography, actual movements, care, property and feasible travel; no universal labor fraction |
| Institutional fracture, succession and contested obligations | Setting/profile; Core §§107, 113–114 | Applicable authority/law/recognition, records and communication; no automatic treaty inheritance or obedience |
| Seasonal, ecological and generational reconstruction | Profile; Core §§69, 96, 117, 119, 122 | Configured demographic/ecological/renewal processes and processed spans; test fine/coarse agreement |
| AI runner and table usability | Selected deployment | Independently reproduce coupled scenarios, hidden information and agency boundaries; then live playtest practical load |
| Shared content replacement | Core §111 and selected library | Use the now-available SCL v1.0 crosswalk; verify exact entry/selector/payload and resolve remaining activation/deprecation holds; identifiers alone insufficient |

Outstanding release questions: exact deployment profiles and runner; full inherited Foundation, library and Core behavioral execution; physical/cause-specific calibration; long-span population/institution continuity; independent AI reproducibility and live playtesting. The recovered v1.2 text and 26 cases are no longer a source-availability gap.

<a id="paf-14"></a>
## 14. Migration, deployment and reference boundary

<a id="paf-14-1"></a>
### 14.1 New deployment

Select exact Core/PAF/module/library/profile sources. Record scope and adoption separately for each. Satisfy §1.3 and Core §§88/112; initialize real state once, then the decision-relevant overlays. Execute applicable §10 cases against the selected runner and record defects. An explicit prospective adoption record, not this document's title, activates the release. Begin at a real player decision without importing a campaign goal, faction allegiance or voluntary action.

<a id="paf-14-2"></a>
### 14.2 Existing campaign migration

1. Freeze the valid clock, event history, actor knowledge, stock, location, claims, conditions, people, work, institutional records and pending events. Retain the rollback snapshot.
2. Inventory the currently adopted rule and profile for each interface. Mark compatible, conflicting, missing or calibration-dependent against the pinned parent. Preserve established overrides until explicitly changed.
3. Assign each generic v1.1 record to its existing Core owner using §12. Do not create a second physical instance. Map old IDs through campaign-scoped aliases; preserve original source/version and unknown fields.
4. Retain v1.3 PA.* identities as assessments. A generic old PA-RECON program maps to CIV Program/K-WORK references; its crisis-history component maps to PA.ReconstructionTransition. PA-NET topology maps to K-NET, while crisis-related isolation maps to PA.RegionalRecovery. Do not infer that matching labels imply equal meaning.
5. Preserve current operation separately from future support, actual presence from membership, forecasts from stock, and construction from service acceptance. Additional distinctions can be unknown until evidenced; do not rewrite resolved success because an old record was less detailed.
6. For any genuine gap, select a precisely scoped bridge or defer the affected migration. Do not run both old and new algorithms. Resolve aliases through SCL v1.0; held replacement/deprecation gates remain closed until their separate Core §111 requirements are met.
7. Exercise relevant old and new gates with the selected runtime, including replay, simultaneous claims, late reports, population transit, scale changes and Mixed agency. Record observed results and unresolved defects; no retrospective claim of tests.
8. Record changed behavior, scope, exact sources, authorized overrides and effective time. Apply prospectively. Core §99 governs specifically authorized corrections/retcons; publishing v2.1 does not reverse payments, repair history, refill stock or erase deaths.

<a id="paf-14-3"></a>
### 14.3 Version and migration impact

PAF 2.1 rebuilds the supplied PAF 2.0 revision 2 against Core 3.2 and SCL 1.0. The thirteen assessment identities and their crisis-specific procedures remain. Shared provider tables, appendix locations, content reference maps, deployment records and evidence are rebuilt. PAF 2.0's earlier move from slim 1.3 to integrated Core remains history. No new progression, catastrophe phase, consumption rate or other numerical default is introduced. Existing worlds may need prospective record/owner/alias mapping; mapping alone changes no quantity or history.

No campaign migration was applied while creating this artifact. Recovery of v1.2 and receipt of PACL v2.0 triggered the complete receiving reconciliation included here. Later changed sources or parent contracts require another CMRR pass. Preserve campaign histories and accepted overrides until an authorized prospective transition.

<a id="paf-14-4"></a>
### 14.4 Hour Zero boundary

Hour Zero is a reference for shortages, persistent site visits, recruitment, institutional continuity, regional links and rebuilding. It establishes no default NPC, resource, location, institution or event. Grey-Zones, Charred ecology, Living Anchors, Project Ark, Feedback Loops, Genesis, Echo-Step, Chronos-Grip, Divergent Echoes, Looms and death-loop exceptions require explicit Hour Zero module/campaign sources and Core §112 contracts. Names alone establish no capability, number or chronology. Rejected loot respawns, scale resets, premature insertion, stage jumps and forced escalation remain rejected.

<a id="paf-15"></a>
## 15. Provenance and release record

**Receiving edition:** IRGS-PAF-2.1 + IRGS-PACL-2.0, 14 October 2026. This is a complete rebuilt engine against current Core 3.2 and SCL 1.0, using the supplied PAF 2.0 source revision 2 as its principal receiving source.

| Source | Function | Current treatment |
|---|---|---|
| Supplied PAF 2.0 revision 2, 83,493 bytes | Immediate complete receiving source | All fifteen operating sections, thirteen records, 109 stable case rows and historical receiving functions accounted |
| Original PAF v1.1 | Generic survival/recovery and crisis-development function inventory | Shared procedures inherit Core once; prior-order/crisis assessments remain PAF |
| Recovered slim PAF v1.2, 37,490 bytes | Direct 16-section intermediate source and 26 PA12 cases | All numbered headings routed; exact case rows retained in Appendix D |
| Slim PAF v1.3 | Thirteen-overlay lineage and twenty-two genre requirements | Records and unique procedures retained |
| Original PL Content v1.0 | Reusable content and two scoped templates | All 193 references resolve through current SCL; no whole prior library is required |
| Post-Apocalyptic Content Library v2.0 | 43 optional compositions, 193 exact references and 63 content cases | Six original current data/specification files retained unchanged; package receiving contract in Appendix E |
| Core 3.2 clean release | Complete shared runtime, nine owners and eleven domains | Eight current components included unchanged |
| SCL 1.0 normative registry | Exact families, aliases, payloads and activation holds | Current source of truth for shared content |
| Earlier patch / Core 3.0 and 3.1 integrations | Earlier reconciliation provenance | No parallel active runtime stack |

Exact hashes, source identifiers and current component files are recorded in the [binding](IRGS_PAF_Binding_v2_1_Core3_2.json) and [manifest](PAF_PACKAGE_MANIFEST.json). The source reconciliation is a function/section inventory, not proof of every unimplemented gameplay outcome.

Standalone PAF v1.2 is recovered: 37,490 bytes, complete 16-section text, SHA256 `e6bc7ea2ed8c7911c0dfe4ac70bc7f012c0d9c150be4e2c80924bbb27e6cc4e8`. All numbered headings and the 26 PA12 case rows now have current dispositions. The source was retrieved as complete backing-file text in two contiguous windows; reconstructed UTF-8 byte size matches the recorded source. It remains a proposed historical edition, not a second active runtime. The former gap mentioned inside the unchanged PACL v2.0 document is historical and resolved for this package.

The 62 PA, 26 PA12, 22 PA13, 15 PA20 and ten PA31 case rows remain available with stable IDs in [the acceptance inventory](IRGS_PAF_Acceptance_Inventory_v2_1.json): 135 Foundation specification/evidence rows. The new library contributes 63 separately specified cases, giving 198 Foundation/library rows plus twenty inherited Core CW-PA obligations. Old executed PA31 labels retain their historical receiving scope. Fresh checks and deliberate fault controls are recorded in the current report. Numerical calibration, complete domain/gameplay implementation and live playtesting remain outstanding.

**Migration:** None. Creating this edition changes neither actual time nor campaign people, stock, assets, injuries, authority, knowledge, work, pending events or history.

## Appendix A. Complete recoverable v1.1 regression inventory

The original scenario and expected-result text is retained below. Provider columns locate the receiving rule, not a second implementation. All rows are retained specification requirements; none is newly executed here. PA-33's “uncommissioned” applies to the attempted function/configuration; a failed test does not revoke unrelated supported service or undo completed work. Old numerical fixtures remain synthetic examples, not new defaults.

| Legacy ID | Scenario | Required result from v1.1 | Receiving Core / PAF scope |
|---|---|---|---|
| PA-01 | Mundane crisis with all extraordinary modules disabled | All principal loops remain playable. | Core §112; PAF §8 |
| PA-02 | Stores remain stocked during institutional collapse | Access/distribution determine availability; stock does not vanish globally. | Core §§79, 104–105; PAF §4 |
| PA-03 | Excellent search at empty pharmacy | No medicine is created. | Core §§79, 104–105; PAF §4 |
| PA-04 | Failed search of established concealed cache | Cache persists. | Core §§79, 104–105; PAF §4 |
| PA-05 | Another team revisits depleted site | Updated depletion/history applies; no fresh loot allocation. | Core §§79, 104–105; PAF §4 |
| PA-06 | Factory stripped of portable goods | Installed machinery may remain. | Core §§79, 104–105; PAF §4 |
| PA-07 | Site secured but basement unmapped | Control and knowledge remain separate. | Core §§79, 104–105; PAF §4 |
| PA-08 | Generator found without lifting/transport capability | Discovery does not produce extraction/delivery. | Core §§79, 104–105; PAF §4 |
| PA-09 | Machine cannibalized for required component | Source capability reflects missing component. | Core §§79, 104–105; PAF §4 |
| PA-10 | Building wiring removed as salvage | Recovered material increases; building restoration potential decreases. | Core §§79, 104–105; PAF §4 |
| PA-11 | Stock dispatched between settlements | Source decreases at dispatch; transit is location; destination increases at receipt. | Core §§10–12, 35, 71, 73, 109; PAF §§3–4 |
| PA-12 | Same delivery appears in later report | No second inventory change. | Core §§10–12, 35, 71, 73, 109; PAF §§3–4 |
| PA-13 | One worker assigned to overlapping duties | Hours cannot be double allocated. | Core §§10–12, 35, 71, 73, 109; PAF §§3–4 |
| PA-14 | 12 technician-hour project, max 2 parallel workers | Two technicians require six usable hours; four do not make it three. | Core §§10–12, 35, 71, 73, 109; PAF §§3–4 |
| PA-15 | Power fails two hours into two-person repair | Credit only feasible work completed before interruption. | Core §§10–12, 35, 71, 73, 109; PAF §§3–4 |
| PA-16 | Expected harvest lies beyond reserve exhaustion | Future harvest does not count as current stock. | Core §§10–12, 35, 71, 73, 109; PAF §§3–4 |
| PA-17 | Seven days food, two days water | Water is immediate limiting requirement. | Core §§71–72, 103, 121; PAF §5 |
| PA-18 | Full water tank contaminated | Physical quantity can remain while potable reserve falls. | Core §§71–72, 103, 121; PAF §5 |
| PA-19 | Settlement food-secure in summer but not winter | Seasonal continuity can fail despite current surplus. | Core §§71–72, 103, 121; PAF §5 |
| PA-20 | 300 evacuees occupy school | Refuge can exist without mature settlement. | Core §§71–72, 103, 121; PAF §5 |
| PA-21 | Shelter supports 500, water supports 300 | Water remains binding service. | Core §§71–72, 103, 121; PAF §5 |
| PA-22 | 100 new beds constructed | Water/sanitation/food do not magically expand. | Core §§71–72, 103, 121; PAF §5 |
| PA-23 | Stable settlement solves its water deficit | Do not create compensating shortage without cause. | Core §§71–72, 103, 121; PAF §5 |
| PA-24 | Intact water plant loses grid power | Asset condition unchanged; service follows backup/buffer. | Core §§101–103, 109; PAF §§3, 7 |
| PA-25 | Elevated tank provides 12 hours after pumps stop | Consumer service does not instantly fall to zero. | Core §§101–103, 109; PAF §§3, 7 |
| PA-26 | Pump power returns but treatment chemical absent | Pumping can return without potable service. | Core §§101–103, 109; PAF §§3, 7 |
| PA-27 | Bridge damaged | Supported transport modes assessed separately. | Core §§101–103, 109; PAF §§3, 7 |
| PA-28 | Demand exceeds generation | Shortfall requires allocation; equipment not automatically damaged. | Core §§101–103, 109; PAF §§3, 7 |
| PA-29 | Hospital backup supports critical loads only | Critical service may continue while noncritical load is shed. | Core §§101–103, 109; PAF §§3, 7 |
| PA-30 | Generator/fuel pump startup loop exists | No self-start without black-start capability. | Core §§101–103, 109; PAF §§3, 7 |
| PA-31 | Alternate transmission line has capacity | Actual rerouting can preserve service. | Core §§101–103, 109; PAF §§3, 7 |
| PA-32 | Alternate line capacity insufficient | Partial continuity follows bottleneck. | Core §§101–103, 109; PAF §§3, 7 |
| PA-33 | Repair complete but functional test fails | Asset remains uncommissioned. | Core §§101–103, 109; PAF §§3, 7 |
| PA-34 | Plant commissioned but distribution broken | Plant works; end-user service remains interrupted. | Core §§101–103, 109; PAF §§3, 7 |
| PA-35 | Sole qualified operator leaves | Physical asset remains; operational capability changes. | Core §§101–103, 109; PAF §§3, 7 |
| PA-36 | One outage affects water/refrigeration/comms | Initiating event applied once; downstream systems use own buffers. | Core §§101–103, 109; PAF §§3, 7 |
| PA-37 | Temporary generators restore power | Temporary service recorded without declaring permanent reconstruction. | Core §§101–103, 109; PAF §§3, 7 |
| PA-38 | 100 refugees arrive | Demand changes at arrival. | Core §§68, 106, 118, 122; PAF §5 |
| PA-39 | 40 arrivals are dependants | Do not count all 100 as workers. | Core §§68, 106, 118, 122; PAF §5 |
| PA-40 | Injured exhausted surgeon arrives | Expertise exists; current capacity may be limited. | Core §§68, 106, 118, 122; PAF §5 |
| PA-41 | Arrivals bring private food | Ownership remains private until transfer. | Core §§68, 106, 118, 122; PAF §5 |
| PA-42 | Newcomer claims specialist credentials | Claim recorded/assessed; no automatic capability unlock. | Core §§68, 106, 118, 122; PAF §5 |
| PA-43 | Mayor dies with valid succession | Institution can continue without deletion. | Core §§28, 107–108, 113; PAF §§4, 6 |
| PA-44 | Government loses building but relocates staff/records | Institution may continue displaced. | Core §§28, 107–108, 113; PAF §§4, 6 |
| PA-45 | Department named without staff/tools/authority | Naming grants no service. | Core §§28, 107–108, 113; PAF §§4, 6 |
| PA-46 | Archive survives but experts die | Knowledge may survive while practical capability falls. | Core §§28, 107–108, 113; PAF §§4, 6 |
| PA-47 | Militia controls area without civil recognition | Control and legitimacy remain separate. | Core §§28, 107–108, 113; PAF §§4, 6 |
| PA-48 | Towns have radio contact but no viable road | Information link exists; material network may not. | Core §§30, 85, 102, 117; PAF §6 |
| PA-49 | Grain surplus exists beyond bottleneck bridge | Bridge can limit export. | Core §§30, 85, 102, 117; PAF §6 |
| PA-50 | Hospital serves three settlements | Local and external demand draw from same capacity. | Core §§30, 85, 102, 117; PAF §6 |
| PA-51 | Region has surplus but no transport vehicles | Delivery remains constrained. | Core §§30, 85, 102, 117; PAF §6 |
| PA-52 | Bridge fails at 14:00, report arrives 14:20 | Physical flow changes at 14:00; recipient knowledge at 14:20. | Core §§30, 85, 102, 117; PAF §6 |
| PA-53 | Water plant construction completes without operators/inputs | Construction complete; service commissioning incomplete. | Core §§72–73, 93–96, 103, 107, 113, 117; PAF §7 |
| PA-54 | Microgrid replaces old centralized grid | Valid reconstruction through redesign. | Core §§72–73, 93–96, 103, 107, 113, 117; PAF §7 |
| PA-55 | Successor government occupies old capital | Does not automatically inherit every prior legal claim/treaty. | Core §§72–73, 93–96, 103, 107, 113, 117; PAF §7 |
| PA-56 | Stable network supports ordinary life | No compulsory threat escalation. | Core §§72–73, 93–96, 103, 107, 113, 117; PAF §7 |
| PA-57 | Reconstructed service later damaged by war | Regression occurs through actual cause. | Core §§72–73, 93–96, 103, 107, 113, 117; PAF §7 |
| PA-58 | Successor society remains stable for decades | No forced return to apocalypse aesthetics. | Core §§72–73, 93–96, 103, 107, 113, 117; PAF §7 |
| PA-59 | Regional summary zooms into local component | Detailed state reconciles with existing totals/history. | Core §§12, 62, 91; PAF §9 |
| PA-60 | Partial solution requires extra day/resources | Player/authority decides new voluntary commitment. | Core §§4–5, 8; PAF §9 |
| PA-61 | Successor PC takes over after death | History, obligations and actual transfers persist. | Core §§69–70, 97, 99; PAF §§7, 14 |
| PA-62 | v1.1 attached to existing Hour Zero save | No automatic temporal reset, NPC insertion, resource creation or retrospective conversion. | Core §§3, 97, 99, 112; PAF §14 |



## Appendix B. Core 3.2 receiving CMRR and finalization record

### B.1 Compared changes and ownership

The current parent retains all 123 Core topic IDs. The table below preserves mechanisms already reconciled in the preceding PAF receiving source; it is not a claim that they were newly added to Core 3.2. Critical §§71–72, 101–107 and §117 retain their current locators. This edition's actual dependency and distribution changes are recorded in Appendix C and the manifest:

| Core change | Receiving PAF treatment | Ownership/removal decision |
|---|---|---|
| §5 optional capability stages | Recovery, intervention and extraordinary actions reference actual stage prerequisites/cost timing; no automatic seven-roll chain | Core owns action stages; no new PAF activation procedure |
| §24 abstract resource/entitlement semantics | Relief allocation or a derived pressure label cannot be spent as a second stock | Core owns backing/claims; no generic survival points introduced |
| §30 queued commands | Evacuation/relief/reconstruction orders distinguish issue, receipt, execution and acknowledgment | Core owns transmission; PA views reflect actual knowledge, not instant remote completion |
| §41 personnel versus effectiveness | Crisis disorganization does not become invented casualties or recruits | K-ACTOR/K-POP retain people; pressure/readiness labels are not headcount |
| §55 identities/manifestations | Optional illusion, clone or remote-body apocalypse modules declare actual identity/embodiment | No free population, actions, obedience or capabilities imported |
| §61 measurement | Forecasts, contamination readings and service inspections retain method, units, uncertainty and lineage | K-INFO owns evidence; no new precision from descriptive labels |
| §73 typed track views | Any displayed survival deadline, reconstruction bar or threat track references its real owner and trigger | Remove any interpretation as independent progress/resource clock |
| §99 exceptional intervention | Death-loop/preservation/retcon modules require exact authority, costs and permitted historical scope | No default resurrection, refund or rewritten PC history |
| §108 capability impact view | A newly available purifier/healing/transport method affects forecasts first; actual adoption requires real means and acceptance | Core owns neutral impact assessment; PAF retains disrupted prior-order relation |
| §109 model envelope and actor-bound pools | Support horizons use valid units/state/model; burden recovery does not refund supplies; cost/output limits remain distinct | No imported SSN chakra/SP/Trauma values or PAF substitute solver |
| §111 SCL identity/gates | Pin SCL 1.0 and exact original payloads; preserve candidate holds | Supersede the earlier unresolved crosswalk availability note, not held definitions |
| §112 receiving manifest/model contract | Pin APOCALYPTIC binding; complete native profiles before dependent use; preserve qualitative assessment scope | Historical generic rule stacks become provenance; no title/hash-only runtime model |
| §123 competition adjudication/measurement | If a successor society runs competitions, use current COMP providers and selected sport content | No apocalypse-specific scoring, refunds or sport promotion |
| Current header / Appendix B deployment / published provider contract | Core 3.2 and SCL 1.0 are current; PAF 2.1 is this complete receiving edition with clause/campaign status kept separate | Earlier parent pins are provenance only; no archived appendix required at runtime |

### B.2 Retained earlier receiving-specific acceptance cases

These stable PA31 identifiers retain their original scope. Rows labelled executed describe prior source receiving evidence, not newly executed full gameplay. Fresh Core 3.2 results are reported separately in this edition's verification; the four gameplay/module rows remain specified.

| ID | Case / expected result | Evidence status |
|---|---|---|
| PA31-R01 | Every APOCALYPTIC required provider resolves in the pinned Core; all thirteen local records preserved | Executed structural receiving check |
| PA31-R02 | Every PL neutral source binding resolves to its exact release definition and original payload | Executed catalogue receiving check |
| PA31-R03 | PL alias target/type/selector/checksum agrees with its definition-local alias | Executed catalogue receiving check |
| PA31-R04 | Repeated alias lookup changes neither registry nor supplied sentinel campaign state | Executed bounded read-only resolver check |
| PA31-R05 | Unknown version, missing identity or incorrect selector rejects resolution | Executed resolver rejection probes |
| PA31-R06 | Held PL content remains source-backed, with deprecation disabled | Executed gate preservation check |
| PA31-G01 | Evacuation order issued before communications restore: no execution from an unreceived instruction; local autonomous action remains possible | Specified gameplay case; not executed |
| PA31-G02 | New water-producing method exists but lacks distribution/operators: forecast changes, actual refuge delivery does not | Specified gameplay case; not executed |
| PA31-G03 | A survival clock is redrawn into more segments: reserve, threshold time and processed spans unchanged | Specified gameplay case; not executed |
| PA31-G04 | A preservation effect prevents death but grants no healing/refund unless its declared contract does | Specified module case; not executed |

### B.3 Finalization and migration impact

All thirteen PAF assessments and their procedures remain. The active parent is Core 3.2 and the catalogue SCL 1.0. No numeric model, setting power, shared algorithm or world-state owner is added. Standalone v1.2, selected profile completion, held-content activation/deprecation, full gameplay execution, calibration and live play remain open at their original scopes.

Use §14 for an actual campaign migration. Compare the currently adopted deployment against this edition's exact providers; retain quantities, unknowns, identities, work, obligations, knowledge, pending events and history. Map exact content references without generating instances. Record the effective change before dependent use. A Core baseline confirmation does not retroactively adopt PAF or enable optional modules.




## Appendix C. Current receiving changes and operative record contract

### C.1 Complete change and removal accounting

| Change from supplied PAF 2.0 revision 2 | Result and reason |
|---|---|
| Core 3.1 → Core 3.2 | Exact current APOCALYPTIC provider contract; one shared runtime |
| SCL 0.2 → SCL 1.0 | All 193 PL source identities, exact selectors/payloads, holds and scopes preserved |
| Old Core Appendix C/D/E/G locations | Current Appendix B for manifest/deployment, C for cases, D for optional profiles; historical bridge documents remain provenance |
| Approximate/historical provider and source pins | Actual current files, hashes and current receiving manifest supplied directly |
| Fifteen PAF operating sections and thirteen assessments | Retained in full; no new stock, survival, population, injury or project owner |
| PA20-01 parent-status gate | Same stable ID; current pin requirement revised to Core 3.2/SCL 1.0 |
| 109 immediate-source rows, 26 recovered PA12 rows, 63 library cases and twenty Core CW-PA requirements | Preserved with stable IDs, applicability and original evidence distinctions; no automatic gameplay pass |
| Six manual worked traces | Retained; fresh bounded portions identified separately |
| Whole prior engines, libraries and source snapshots | Omitted from distribution; original sources are unchanged and their required functions/payloads remain available |
| Formerly missing standalone PAF v1.2 | Recovered, hashed and compared; 26 exact cases retained in Appendix D; no invented replacement |
| Numerical defaults, modules and campaign migration | None introduced or enabled |

The reconciliation matrix assigns every recovered numbered heading to current procedures, owners or source-only provenance. Omitted historical documentation is accounted here and in the binding. Corrected invalid interpretations—respawning loot, duplicate stock, mandatory collapse tiers, false commissioning and forced regression—do not return through another source alias.

### C.2 Minimum actual overlay record

An assessment stores campaign and overlay identity/version, source event/evidence refs, as-of time, relevant Core entity/function refs, purpose, observer/visibility, assessment revision, description, uncertainty, lifecycle and next material trigger. Quantity, occupancy, injury, work progress, legal authority and service delivery remain owner-qualified references; a displayed total is derived from that owner at its stated time.

An assessment update key is campaign + overlay + source event/evidence + revision. A duplicated update has no additional effect. A changed assessment is a new revision, not a second physical loss. If evidence conflicts, preserve source/time/confidence and the uncertainty; resolve actual world corrections through Core §99 separately.

Overlay lifecycle can be active, superseded, closed or archived as appropriate. Closing removes no actual debt, injury, contamination, completed work, damaged asset, obligation or historical record. No lifecycle state grants a new capability.

### C.3 Runtime decision sequence

1. Use Core's current clock, journal, actual records, pending events, adopted profiles and actor knowledge.
2. Resolve the declared action, authorized autonomous activity and cause-specific effects through the existing Core providers.
3. At material committed changes or received evidence, retrieve only relevant PAF assessments.
4. Reconcile source and as-of time; update assessment metadata and reference current facts without committing them again.
5. Generate feasible response options within actual means/authority. An option spends no resources and chooses no player action.
6. Present only actor-visible information through Core §90, keeping hidden facts and forecasts distinct from observations and present stock.
7. Return control for a new voluntary commitment. Continue supported off-screen work, needs, logistics and autonomous activity under the same Core schedule.

Physical occurrence, observation, transmission and receipt can have different times. Simultaneous events use common pre-event state. A regional view, detailed scene, save/load, repeated report or extra overlay changes no already processed interval, quantity or casualty.

### C.4 Selected content and profile boundary

The 193 PL references comprise 191 exact shared bindings and two scoped templates. The 39 selected qualitative bindings, 152 source-backed holds and two scopes are source-reference counts, distinct from the catalogue's overall family counts. No record is promoted by being linked.

Select one complete compatible model per actual cause. Define units, validity, actual inputs, output/quality, capacity/demand, uncertainty, update law and stop/recovery conditions before a dependent numerical operation. Unknown depletion, disease, wear, transport or reproduction rates remain unknown. Supported qualitative assessment and unrelated authorized actions continue.

APX-X01 is a module template, not an enabled extraordinary catastrophe. CPF-PA-BASE is configuration guidance, not a generated world. No theme, mandatory emergency policy, communal ownership, citizenship, hostile attitude or hidden history follows from a lookup.

### C.5 New receiving acceptance obligations

| ID | Required receiving result | Evidence boundary |
|---|---|---|
| PA32-01 | Current Core/SCL pins, actual provider anchors and unique owners resolve | Fresh documentary/integrity checks |
| PA32-02 | All thirteen overlays retain purpose, trigger, identity and assessment-only writes | Fresh preservation/schema checks and bounded view fixture |
| PA32-03 | All 193 content identities/types/selectors/payloads match SCL in both directions | Fresh resolver/data checks |
| PA32-04 | No catalogue hold is promoted and no scoped template receives an invented alias | Fresh data checks and deliberately invalid outputs |
| PA32-05 | Buffer, finite recovery, movement/transit, acceptance and delayed knowledge remain distinct | Named bounded state fixtures; not full domain implementation |
| PA32-06 | Repeated rendering, event replay and scale changes create no new physical effects | Named bounded replay/projection fixtures |
| PA32-07 | New PC payment/movement/politics require a declaration; stability permits ordinary continuation | Bounded contract/metadata fixtures; independent live adjudication outstanding |
| PA32-08 | Unknown material parameters block only dependent calculations without arbitrary filler | Named bounded gate fixtures and explicit profile contract |

These receiving obligations supplement the inherited acceptance inventory. Evidence from a bounded implementation supports only its implemented invariants. Controlled live play and independent AI-runner reconstruction remain separate work.

**End of IRGS PAF Engine v2.1 — complete linked edition for Core 3.2 and SCL 1.0.**


<a id="paf-appendix-d"></a>
## Appendix D. Recovered PAF v1.2 acceptance and function reconciliation

The complete source is recovered and compared directly. Original PA12 IDs, scenarios and expected results below are preserved. Current provider routing is added without claiming live execution. PA12-21 permits only a retained already-adopted procedure or an expressly selected compatible bridge; a missing provider never activates v1.1 automatically. PA12-22 uses the current exact alias map and the same saved instance identities.

| ID | Recovered source scenario | Recovered source expected result | Current receiving route |
|---|---|---|---|
| PA12-01 | Two regions under one disaster retain different government/power conditions | No universal phase/state switch | PAF §§2–3/6; Core 101–103/107 |
| PA12-02 | Power station fails while downstream water tank remains usable | Buffered service survives until real limit; no double outage | PAF §3; Core 101–103/109 |
| PA12-03 | Same outage is reported later | Report changes knowledge, not physical loss again | PAF §§3/9; Core 60–61/85/90 |
| PA12-04 | Several simultaneous crisis drivers affect one service | Shared dependency/cost applied once; remaining causes separately recorded | PAF §3; Core 101–103/109 |
| PA12-05 | Pharmacy previously stripped and revisited | No new stock from search, scene change or site label | PAF §4; Core 79/104–105/109 |
| PA12-06 | Factory portable stock exhausted, machines still installed | Portable depletion does not delete productive capital | PAF §4; Core 21–23/104–105 |
| PA12-07 | Generator found but cannot be transported | Knowledge without physical delivery or service | PAF §4; Core 35/79/104–105 |
| PA12-08 | Building stripped for copper | Real material transfer and corresponding donor capability loss | PAF §4; Core 21–23/104–105 |
| PA12-09 | Refuge receives 100 evacuees including children/injured | One population count, immediate service demand, realistic work availability | PAF §5; Core 106/118/121–122 |
| PA12-10 | Food forecast good, potable reserve nearly gone | Water pressure from Core provision, no separate survival meter | PAF §§3/5; Core 71/103/109 |
| PA12-11 | Refuge becomes permanent settlement | Only real Core habitation/service/institution changes; no time unlock | PAF §§5/7; Core 72–73/103/121–122 |
| PA12-12 | Mayor lost; two offices claim continuity | Existing institution need not disappear; recognition and control distinct | PAF §6; Core 28–30/107/113 |
| PA12-13 | Technical archive survives loss of technicians | Information remains; competence does not spontaneously return | PAF §§4/6; Core 60–61/108/117 |
| PA12-14 | Working legacy machine lacks replaceable control component | Current use distinct from future replacement vulnerability | PAF §4; Core 108/117 |
| PA12-15 | Communication survives, freight bridge fails | Information network without material delivery | PAF §6; Core 102/116 |
| PA12-16 | Region produces surplus but lacks usable transport | No automatic distant satisfaction | PAF §6; Core 102/116–117 |
| PA12-17 | New microgrid commissioned rather than old grid rebuilt | Valid redesigned recovery after all real acceptance requirements | PAF §7; Core 101–103/108 |
| PA12-18 | Successor government occupies former capital | No automatic transfer of treaties, legitimacy or private property | PAF §§6–7; Core 28–30/107/113 |
| PA12-19 | Stable successor society survives decades | No compulsory relapse or stronger enemy | PAF §7; Core 62/69/96/117 |
| PA12-20 | Extraordinary modules disabled | Ordinary disruption and recovery still work | PAF §§8–9; Core 112 |
| PA12-21 | New slim PAF selected with incomplete generic Core service machinery | Stop adoption or retain explicit v1.1 bridge; don't lose mechanics | PAF §§1/14; Core 97/112; Appendix B |
| PA12-22 | Source PAF site IDs migrate to Core/CCL aliases | Same assets/stocks/conditions/history; no new instances | PAF §§9/14; Core 88–89/111; exact PL map |
| PA12-23 | Simultaneous aid, transport, and institutional requests contend for one stock | Core arbitration prevents double claim | PAF §§3/5/6; Core 11–12/71/109 |
| PA12-24 | Mixed solution needs fresh purchase or PC evacuation decision | Return control; preserve authorized outcomes only | PAF §§1/9; Core 4–5/83/90 |
| PA12-25 | Zoom from national network to local repair then back | No reset/duplicate materials, work, losses or time | PAF §9; Core 10–12/90–91/96 |
| PA12-26 | Resolved water shortage followed by no new cause | Relief persists; no automatic replacement crisis | PAF §§3/7; Core 71/101–103 |

The source’s inherited-versus-reproduced supply distinction (§4.3), separate present/replacement capability (§8), regional information-versus-material links (§9), acceptance before durable service (§10), Hour Zero boundary (§13), source-compatibility bridge (§§1/16), and source-deprecation gate (§15) remain explicit in current PAF §§1/3–9/12/14 and Core. The source-heading matrix lists every numbered heading, including governance and migration clauses. No unique source function is intentionally dropped; full behavioral equivalence remains unexecuted.

<a id="paf-appendix-e"></a>
## Appendix E. PACL v2.0 receiving contract

**Purpose/scope/status:** package the complete current PA content specification and its six unchanged data files with PAF v2.1. PACL v2.0 remains proposed; packaging and structural reconciliation do not adopt or activate a composition. **Dependencies/ownership:** exact Core 3.2, SCL 1.0, PAF 2.1; the same thirteen read-only PA assessments and nine Core owners. **Records:** 43 PA-CNT templates, 193 exact PL mappings, 54 prior-library source-section dispositions and 63 content acceptance specifications.

**Procedure/runtime:** select an eligible PA-CNT ID and exact revision; resolve each legacy reference through the provided crosswalk and current SCL; preserve type, selector, source payload, hold and scope; select required cause/effect/service/need profiles; attach only authorized actual Core instances; assess committed facts at actual occurrence/receipt times. No library tick, duplicate stock, automatic effect, default rate, active catastrophe or forced player choice is introduced.

**Interface/overrides:** [PAF_Library_Receiving_v2_1.json](PALibrary/PAF_Library_Receiving_v2_1.json) maps each composition to exact references, overlays and the selected parent. It defines no Core override. The unchanged PACL document’s Core 3.1/PAF 2.0 bridge language remains true of that older source. This separate rebuilt PAF 2.1 explicitly supplies the current Core 3.2 receiving contract; neither old source nor existing campaign is silently rebound.

**Acceptance/applicability:** all 63 library scenarios and expected results are preserved verbatim in the library CSV and machine-readable inventory. PA-L2-058 applies when a campaign still selects PAF 2.0; it does not repin the new 2.1 engine. PA-L2-062 applies when a source is unverified; this package records recovery of v1.2, all its headings and 26 exact cases. PA-L2-046 disabling APX selectors does not disable explicitly selected ordinary Core causes. PA-L2-055 cannot freeze actual supported aging, ecological, institutional or autonomous processes; a missing numerical profile blocks only its dependent operation. These are applicability clarifications, not silently altered source expectations.

**Calibration/unresolved:** retain 152 source-backed holds, 39 selected qualitative references and two scoped extensions. Exact equipment, care, disease, radiation, weather, agriculture, logistics, institutional and long-span profiles still require selection and appropriate evidence. All 63 behavior specifications, complete Foundation/Core behavior, AI reproducibility and live play remain outstanding beyond named bounded verification.

**Provenance/migration/removals:** the new library ZIP is SHA256 `9f46fbeafd2a67ee4972667a8d4160ceb1875790fb301de0e3790debfe1344d6`; its six current specification/data files are byte-identical here. Whole prior PAF/PL engines, duplicate current reference data, superseded bridge/readme/manifests and older test reports/scripts are omitted or replaced by current receiving documentation. Each original archive component has a disposition in [the package reconciliation](PALibrary/PA_Package_Reconciliation_v2_1.md). Original PL payloads remain in the sole normative SCL registry, not merely hashes. No campaign migration is applied; prospective adoption preserves IDs, histories, stock, claims, knowledge and unfinished work.
