# IRGS — Space Exploration and Colonization Foundation — Slim Genre Engine

**Version:** 0.2 · **Document:** IRGS-SPACE-SLIM-0.2 · **Date:** 14 October 2026  
**Parent pin:** IRGS-CORE-3.2, Integrated Core Engine, 14 October 2026; IRGS-BIND-SPACE-3.2; IRGS-SCL-1.0.  
**Design status:** Proposed complete CMRR resubmission. Genre ownership is a scope designation, not acceptance.  
**Adoption status:** Not adopted by publication; no campaign initialized, advanced or migrated.  
**Validation:** Specification review and bounded synthetic reference checks only; see §17 and the verification report. No live playtest, balance, empirical calibration, engineering certification or full simulator is claimed.

**Purpose:** Support robot exploration, spacecraft operations, orbital/interplanetary/interstellar transport, research, prospecting, off-world production and settlement. Preserve trajectories, environmental capability, finite mission resources and delayed information. Prosperity, safe routine operations and ordinary life remain valid outcomes.

**Scope:** This document supplies the space-specific extension and a precise Core v3.2 inheritance bridge. Core owns shared procedures; setting modules supply exceptional technology/biology; campaign profiles select parameters and institutions; campaign state holds actual entities. It introduces no compulsory warfare, disaster, empire, species, political system or campaign lore.

**Reading:** §§1–3 define dependencies and records; §§4–9 define specialized operations; §10 preserves content IDs; §§11–13 cover runtime, acceptance and calibration; §§14–18 supply interfaces, CMRR, evidence and migration. This is a complete replacement specification for review, not a patch to v0.1. Core remains a required parent document.

## 1. Dependencies, authority and boundary

Construction: **Shared IRGS Core → this genre foundation → setting/technology modules → campaign profile → campaign state**. Authority, corrections, agency and prospective overrides inherit Core §§1–5/97/99/112. Current explicit user instructions govern this submission. The user explicitly replaced the earlier v3.0 and v3.1 targets with the attached Full Release R2: Core v3.2 and SCL v1.0. This submission follows that correction; unfinished earlier drafts are not authorities or deliverables.

The authoritative receiving parent is [Integrated Core Engine v3.2](inputs/r2/IRGS_Core_Engine_v3_2.md). Its front matter identifies the current workshop parent release, 14 October 2026. R2 is a candidate distribution preserving that normative Core and catalogue; its maturation overlays remain proposals. Parent status does not adopt this new space resubmission, which remains Proposed. Selecting the parent is not campaign adoption. Appendix A of that parent owns shared K-record meanings; §112 and Appendix B own module composition and slim-engine contracts.

The earlier Space v0.1 dependency on Framework v2.1 and proposed CDI 0.2 is replaced by this explicit bridge. Those documents, Military v0.4 and its AIR index remain source provenance or optional content provenance, not additional shared runtime owners. Do not stack their generic algorithms onto v3.2.

| Core v3.2 owner and exact locator | Inherited function | Space extension / activation |
|---|---|---|
| §§4–8/14–15/90 | Agency, action, feasibility, competence, uncertainty and Mixed | Maneuver, EVA and mission declarations bind feasible specialized envelopes; no new space resolution roll |
| §§10–12/62/86/91/109; K-TIME | Clock, event frontier, replay, atomicity, intervals and scale continuity | Burn, coast, contact, threshold and arrival boundaries; no second clock |
| §§20–23/55–57/101/105; K-ASSET | Assets, components, containment, crews, maintenance and dependencies | Flight state, craft operating envelope, pressure-zone geometry and thermal node model |
| §§12/35–37/105/109; K-STOCK | Lots, reservations, resources, mass containment and operating rates | Propellant feed/species, gas transfer/venting, suit inputs and mass-derived performance |
| §§29–30/60–61/79/85/102; K-INFO/K-NET | Channels, observations, estimates, received orders and capacity | Moving endpoints, occultation, light-time, space contact windows and ephemeris validity |
| §§71–74/101–110; K-WORK/K-NET | Needs, projects, commissioning, services, recovery and production | Space environment acceptance, ISRU process envelope and actual off-world access |
| §§17–19/54/118; K-ACTOR/MED | Conditions, exposure, protection and care | Profile-defined vacuum, pressure, acceleration, radiation and thermal channels; no default physiological numbers |
| §§25–29/38–46/64–69/106–108/113–114/117/121–122; K-ORG/K-POP and domains | Institutions, autonomy, careers, households, economy, programs and settlement | Remote mission mandate, settlement transition and task-specific import/escape dependencies |
| §119 WILD | Ecology, habitat and biological processes | Enabled planetary ecology, controlled agriculture and containment profiles |
| §§111–112 | Definitions, aliases, capability bindings, activation, overrides and migration | Eight unchanged SPACE-LIB IDs, version-pinned space variants and scoped extraordinary drives |

GOV, ECO, CIV, URBAN, LIFE, MED and WILD activate only when their functions are consequential. INV (§115) and INTEL (§120) support an investigation or intelligence operation without inventing space-specific substitutes. COMP (§123) owns competition organization/results when enabled; sports are content/modules. No domain activation invents institutions, people or stock.

**MAR boundary:** Core §116 operates on water. Reuse its shared parent interfaces, not its buoyancy/flooding/stability model for vacuum operations. An amphibious spacecraft can use §116 during an actual water phase and SPACE during flight, with the same asset/occupants and an explicit mode boundary. No spacecraft hit-point pool, colony treasury, separate injury ledger or universal space skill is introduced.

## 2. Select a model before resolving its consequences

Use the least detailed model that preserves the decision:

| Mode | Useful scope | Required gate |
|---|---|---|
| Authored route/envelope | Routine transport on a known service | Declared departure/arrival windows, mass/configuration limits, consumption, transit/handling stages and provenance; it cannot answer unmodeled maneuvers |
| Analytic two-body | Circular or Keplerian segments, bounded transfer examples | Central-body model, compatible units/frame/epoch, validity domain and specified impulses |
| Numerical flight | Low thrust, multiple bodies, perturbations, close operations | Force/propulsion models, integrator, event detection, error/convergence criteria and valid initial state |
| Setting drive model | Gates, jump travel, reactionless engines or other explicit exceptions | Scope, access, costs, time, navigation, entry/exit state, failure and interaction with ordinary flight |

An authored route is a declared abstraction, not proof of engineering feasibility. An analytic formula is not a landing, rendezvous or finite-burn simulator. A numerical answer without a selected valid model remains unresolved. Dice resolve actual execution/navigation uncertainty; they cannot supply an absent transfer path, burn budget, safe entry corridor or air supply.

## 3. Minimal space records

All records inherit campaign scope, stable identity, version, provenance, authority/status and visibility from Core Appendix A. The owner binding in §14 is normative: extension records reference shared state rather than copy it. Use owner-qualified records and references, with actual state separated from estimates.

| Record | Fields required where material |
|---|---|
| `SPACE.BodyProfile` | central/parent body, gravity/ephemeris model, reference radius/shape, rotation, surface/atmosphere/hazard refs, validity and parameter provenance |
| `SPACE.FlightState` | existing asset ref, reference frame/axes/origin, epoch/time scale, position vector, velocity vector, units, actual-versus-estimated status, uncertainty, propagation model/last span |
| `SPACE.CraftEnvelope` | configuration ref, structural/acceleration limits, propulsion/feed modes, attitude/control, docking interfaces, thermal/pressure limits, power/support dependencies, approved operating modes |
| `SPACE.Maneuver` | objective, start/window, current state ref, requested vector/time history, predicted path, engine/feed assignments, resource reservations, authorized bounds, uncertainty ID, stop/abort and achieved state |
| `SPACE.MissionLeg` | origin/destination states, departure/arrival conditions, propulsion/coast stages, launch/entry/capture/handling dependencies, cargo/passenger refs, alternate/return plan, next causal frontier |
| `SPACE.ContactPlan` | moving sender/receiver, valid ephemeris refs, link visibility/window, propagation model, bitrate/packet handling, queues, power/pointing, relay and confirmation requirements |
| `SPACE.RemoteCommand` | issuing actor/mandate, payload/version, issue time, actual transmission/receipt, validity window and endpoint semantics, preconditions, local autonomy, accepted/executed/result/ack refs |
| `SPACE.PressureZone` | existing compartment ref, volume/configuration, gas-lot quantities/species, temperature/equation of state, connections/leaks, life-support tasks, sensors and alarm/effect profile |
| `SPACE.ThermalState` | component/node refs, energy/temperature model, internal/environmental inputs, transport/rejection paths, operating limits, method and threshold events |
| `SPACE.ExtravehicularPlan` | participant/suit refs, airlock stages, actual atmosphere transfer, restraint/mobility, route/work, communication, resources, contingency/return and authorization |
| `SPACE.SiteAssessment` | survey coverage/source/time, observed resources/environment, estimates, access, extraction/processing tests, exposure and unresolved feasibility |
| `SPACE.SettlementTransition` | actual location/occupants, URBAN/CIV work refs, required independent functions, acceptance evidence, recurrent support/import obligations, local authority/knowledge, readiness by task |

The spacecraft's location is the flight-state extension of its existing K-ASSET fact, not a second writable position. A compact route view references that same fact. Delta-v is a derived capability forecast for the present mass/configuration, not a stock that can be spent alongside propellant.

## 4. Flight, transfer and rendezvous

### 4.1 Frames and state

Every material vector names its reference frame and epoch. Transform both position and velocity when changing a moving frame; changing a label is not a physical acceleration. Radius is measured from the relevant body center; altitude additionally needs a reference surface. A ship approaching a station needs their relative position **and velocity at the same epoch**, with attitude/contact geometry where relevant.

Navigation is a belief based on observations, clocks and models. The world uses actual state; a crew plans with accessible estimates. A good navigation result narrows supported uncertainty without granting undetectable targets or perfect future forecasts. Known ephemerides may support routine propagation without a roll. Unknown state remains unknown or bounded, not zero.

### 4.2 Bounded analytic adapter

For a declared small craft in a spherical central body's two-body Newtonian model, use positive gravitational parameter `mu` and compatible units. Circular speed is `sqrt(mu/r)`; elliptical vis-viva speed is `sqrt(mu*(2/r - 1/a))`. For coplanar circular start/end orbits and two impulsive burns, let `a=(r1+r2)/2`; the transfer half-period is `pi*sqrt(a^3/mu)`. Burn magnitudes are the absolute differences between circular and transfer speeds at the respective radii. The ESA GODOT reference explicitly identifies circular-orbit, impulsive assumptions; the JPL lesson uses a half-ellipse and phase planning. This adapter is a bounded application of those concepts. [ESA orbital routines](https://godot.io.esa.int/docs/api_reference/generated/generated/godot.core.astro.html#godot.core.astro.hohmannTransferDeltaV), [JPL launch-window lesson](https://www.jpl.nasa.gov/edu/resources/lesson-plan/lets-go-to-mars-calculating-launch-windows/).

The adapter does not include plane change, finite thrust/gravity losses, atmospheric ascent, local departure/capture, target phase errors or docking. It does not claim a Hohmann transfer is the best possible trajectory under every objective or radius ratio. Same-radius output of zero means **no orbital-energy change required**; it does not put separated co-orbiting craft together. Choose a phasing/rendezvous procedure when the target is elsewhere.

For radius2>radius1, departure/arrival burns are prograde in this simple adapter; inward transfers are retrograde. The positive scalar budget is not the maneuver direction. Interplanetary legs also need the local-body departure/arrival interfaces; a heliocentric transfer alone cannot launch from a surface or brake into a destination orbit.

### 4.3 Mission procedure

1. Define the destination event: flyby, matching orbit, rendezvous, dock, land, deploy instrument or deliver cargo. These are different outcomes.
2. Establish actual craft/loading and accessible navigation state; choose the model/envelope. Check route geometry, phase, engines, attitude, propellant/feed, power, crew and receiving access.
3. Compare feasible windows and authorized alternatives, retaining arrival support, reserve/return obligations and uncertainty. A missed window is a changed opportunity, not an automatic catastrophe.
4. Authorize the specific leg and permitted contingencies. NPC operators may follow standing instructions; new player choices return control.
5. Execute burns and coasts on the shared timeline. Stop at burn completion, feed exhaustion, threshold, new contact, command receipt or decision. Engine shutdown ends thrust; it does not erase existing velocity or gravity-driven motion.
6. Recompute the achieved trajectory from actual execution, preserving error provenance and spent resources. An execution failure can leave a different feasible trajectory; it cannot teleport the ship or invent an unrelated collision.
7. At destination verify relative state and the next envelope. Rendezvous precedes permitted approach/contact; docking precedes transfer handling and any atmosphere connection. A passenger arrival report does not unload cargo or replenish a habitat.

**Rendezvous/docking gate:** Both objects must actually reach compatible relative position, velocity and configuration under the declared capture/approach envelope. A berth reservation grants neither motion nor safe contact. A docking failure applies only supported contact, missed capture or delay effects. Automatic collision, decompression or death requires its causal mechanism.

## 5. Propulsion, mass and spacecraft function

For an ideal fixed-effective-exhaust-velocity reaction engine, `delta_v = ve*ln(m0/m1)` and a requested ideal burn implies `m1=m0*exp(-delta_v/ve)`. `m0` includes actual dry craft, cargo, people and propellant; `m1` must retain the nonexpelled mass. These are ideal capability relations, not complete burn-duration or ascent calculations. Use `ve` directly or a properly defined specific-impulse adapter; do not confuse standard acceleration used in that conversion with universal gravitational constant G. [NASA ideal rocket equation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/ideal-rocket-equation/).

**Procedure:** derive current mass from one set of references; validate the selected engine's species/mix, feed, configuration and vector requirements; reserve eligible inputs; check ideal capability and the selected time/thrust envelope; commit actual expulsion and achieved motion together. Sequential burns begin from actual remaining mass. Loading cargo changes the derived capability. Jettisoning a stage or cargo is a separate custody/location/mass event and does not also consume that mass as propellant. Exhaust leaves active onboard stock through a recorded ejection, not an unexplained disappearing ledger item.

A reaction engine needs its declared reaction mass even if electrical energy is plentiful. A chemically powered engine and an electrically powered low-thrust engine need different input/configuration profiles. No universal efficiency, thrust, boil-off, specific impulse, mass ratio or reserve fraction is supplied. Unknown parameters block dependent numerical maneuvers; a declared qualitative route may still support decisions within its envelope.

Use Core §§21/23/55–57/101/103/108 for faults, maintenance, crews, redundancy, commissioning and production support. Damage to an antenna need not disable propulsion; a coolant leak need not puncture the pressure hull. Assess affected functions and actual connected dependencies. Repaired hardware still needs its declared testing/commissioning, and manuals do not create an onboard specialist. Import no spacecraft hit-point pool or arbitrary reliability roll.

## 6. Planetary environments, arrival and exploration

### 6.1 Environment profile

Declare only consequential properties: gravity and terrain; atmosphere composition/pressure/density and weather; radiation/exposure channels; illumination and local cycles; temperature/thermal exchange; surface/dust/chemical effects; local ecology if any; communications/navigation visibility; and accessible resources with survey provenance. Absence of a field is not evidence that an atmosphere is breathable or a surface is sterile.

Compare the environment with actual craft, suit, equipment and organism capability. A protective suit is not universal protection against heat, radiation, corrosives, pressure and impact. Core §§17–19/118 own consequences and care for existing people; §119 owns biological/environmental processes. No universal oxygen tolerance, decompression injury timer, radiation dose response, low-gravity adaptation or alien infection is invented.

### 6.2 Launch, entry, descent, landing and ascent

Each is a separate mission stage with supported initial/final state, vehicle envelope, controls, inputs, navigation, site and abort options. Atmospheric braking requires an actual atmosphere and vehicle model; thrust-to-weight and finite burn constraints cannot be replaced by an ideal rocket-equation total. Landing at a high-energy approach does not become possible because a piloting check succeeds. A surface-launch budget includes the selected ascent model and losses; an orbital transfer formula does not supply it.

A mission can use a source-supported launch/landing service envelope when detailed dynamics are immaterial. Record its stated mass/weather/site/trajectory limits, duration and resources. Reject extrapolation beyond that envelope rather than silently inventing a penalty.

### 6.3 Survey and discovery

Choose a question, instrument/method, actual coverage, contact opportunities, sample plan, power/data/time commitments and follow-up. Record detection separately from interpretation and physically verified recovery. An orbital image may identify a candidate deposit without establishing ore grade, excavation access, hazardous chemistry or local ownership. Sampling consumes actual equipment/time/sample amounts; failed analysis preserves what was physically collected. Core §§79/104/111 govern discovery, recovery and instantiation; a template asteroid or planet instantiates no resource stock automatically.

Exploration success may remove uncertainty, reveal a workable landing site or resolve a route problem permanently. Further hazards require actual state/processes, not automatic replacement obstacles. Existing sentient inhabitants, where enabled, are autonomous actors with their own knowledge, institutions and rights claims; discovery is not ownership or consent.

## 7. Habitats, pressure zones and life support

### 7.1 Atmosphere and pressure

Track actual gas amounts/species, volume, temperature and connected zones only to the detail required. Under a selected ideal-gas approximation, `P*V=n*R*T` with absolute temperature; mixed-gas partial pressures additionally depend on the species amounts. The equation is an operating-state relation, not a complete leak, chemical or physiological model. [NASA ideal-gas notes](https://www.grc.nasa.gov/www/k-12/Numbers/Math/Mathematical_Thinking/ideal_gases_under_constant.htm).

Pressure is not an air inventory, oxygen percentage is not oxygen amount, and total pressure alone does not establish breathability. Opening more volume can lower pressure without losing gas. Repressurizing from a tank transfers actual gas; using it again requires it still to exist. A leak profile defines actual outflow/species and pressure dependence; a constant leak is allowed only within a declared fixture/envelope, not as universal fluid physics.

**Zone procedure:** apply actual connections/breaches/control actions; transfer or expel gas once; recompute the supported state; evaluate engineering alarms and any separately configured organism/equipment exposure; schedule earliest thresholds. Isolation changes the connected system after a real valve/hatch action. Alarm receipt changes knowledge, while the physical process may have already begun.

### 7.2 Consumables, recycling and shared capability

Core §§71/101–103/109 own needs, dependencies, useful service bundles, allocation, buffers, stock/rate accounting and interruptions. Core §§73/108 own transformations and accepted output; §119 supplies selected agriculture/ecology. This engine does not repeat those algorithms.

For a space habitat, bind separate oxygen supply, carbon-dioxide removal, pressure regulation, thermal management, water, sanitation and food functions to actual equipment and occupied pressure zones. A room's volume or nominal beds do not establish a habitable service. Atmosphere already in an occupied zone is not also stored tank gas.

The recycling profile must identify chemical/material inputs and outputs, species balance, contaminants, losses/waste, energy, maintenance and throughput. A recovery percentage is valid only against eligible processed input and its defined basis. It neither creates input nor processes the same water twice. Select real reserve tanks and accessible gas. Hydroponics requires its actual environmental/biological process, light/energy, nutrients and labor; selecting the entry yields no food.

When life support and cargo handling compete, use Core §§102–103's allocation and useful operating configuration. Retain actual interruption costs and occupant demand through §106; no shortage deletes people. Missing atmosphere-care parameters block only dependent claims, not unrelated supported maintenance or communication.

### 7.3 Thermal operation

A spacecraft's thermal state depends on internal generation, environmental inputs, transport and rejection; exterior vacuum does not supply ordinary atmospheric convection. Internal gas/fluid circulation may still move heat to rejection surfaces. Radiators, orientation, shadowing and compatible temperature limits therefore belong in the selected spacecraft envelope. [NASA thermal-control reference](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/).

Core §109 owns the burden/peak/threshold procedure. Supply a space energy-balance/process law, actual operating geometry, units/state meaning, rates and thresholds; temperature and stored thermal energy require a declared conversion model. A battery's stored energy, electrical output and heat rejection are different constraints. Check action peaks before later cooling. “Cold space” does not provide instantaneous cooling; coolant stock does not replenish because a scene ends. A thermal alarm alone does not imply a reactor explosion or medical injury.

### 7.4 EVA and airlocks

1. Establish the actual task, route and participant authorization. Check suit pressure/atmosphere/thermal capability, mobility/restraint, tools, communication and resources for departure, work and return.
2. Establish the airlock's occupants, volume, connections and staging. Transfer/recover/vent actual gas through a declared process; cycling is not free unless a supported recovery system supplies that result.
3. Separate suit operation, hatch actions, external movement and task work. A tether provides only its actual attachment/range/strength; it does not create propulsion or retrieve an unreachable person automatically.
4. Advance to actual resource, communication or environmental thresholds; continue within authorized contingency instructions. A Mixed repair cannot silently commit another EVA or consume the crew's reserved return supply.
5. Reenter through actual stages and account for gas/resources once. Inspect/service equipment and refer actual exposures to MED where supported. Reentry does not reset fatigue, damaged seals or earlier conditions.

## 8. Communication, remote authority and delayed operations

Radio/optical messages travel at finite propagation speed; visibility, receiver availability and link capacity also matter. NASA describes distance-induced latency and interruptions such as occultation. This foundation applies those constraints through Core's existing channel and information records. [NASA space-communications overview](https://www.nasa.gov/missions/tech-demonstration/space-communications-7-things-you-need-to-know/).

For a declared fixed-endpoint approximation, one-way delay is `distance/c`. For moving endpoints in a shared inertial flat-spacetime model, solve receipt consistently with sender position at emission and receiver position at reception, rather than always using separation at issue. A message's last-bit arrival also depends on serialization/transmission time and processing/relay delays. No link budget, data rate, interstellar radio range or perfect reception is provided by this foundation.

**Space contact procedure:** Core §§29–30/85/102/113 own command lifecycle, authority, receipt and network allocation. Bind that procedure to the selected ContactPlan:

1. At actual transmission, verify the moving endpoints, ephemeris interval, visibility/occultation, pointing, power, receiver availability, packet volume and actual link allocation. Issue time is not emission time.
2. Determine arrival using the selected propagation method; add serialization and actual relay/processing stages. Store-and-forward waits for both receipt of the required packet and a usable next-hop window. Partial packets follow the selected reassembly/expiry policy.
3. At reception, update K-INFO once; bind identity/version, local preconditions, validity endpoints and remote mandate through Core §§10/29/113. Repeated packets or later acknowledgments cannot repeat an executed action. A command may be received but stale, infeasible or outside authority.
4. Local NPC operation follows Core §64 and the actual autonomy profile. An unavailable return link does not cancel standing authority or grant new authority. A PC decision outside prior authorization returns control.
5. Completion and acknowledgment remain different events. Acknowledgments travel over a real return contact plan; missing confirmation establishes uncertainty, not failure or a reason to repeat the effect.

For a fixed-link synthetic example, command issue0, one-way delay10, onboard task duration2 and immediate reply yields receipt10, completion12 and confirmation at the original sender22. The sender cannot claim task completion at0 or10 merely from the command. If a deadline excludes receipt at10, use that declared rule. These are test timings, not Earth/Mars data.

Autonomy profiles specify permitted actions, expenditure limits, threat response, abort authority and communication-loss behavior. They create no unrestricted AI competence or institutional mandate. Remote operators use delayed telemetry; a displayed position carries its as-of time. Estimated arrival and actual docking can diverge without rewriting the earlier report.

## 9. Interplanetary/interstellar logistics and colonization

### 9.1 Supply routes

Core §§12/24/35–37/102/105–106/114 own cargo, claims, routes, queues, passenger movement and usable capacity. The space extension supplies departure windows, actual flight/envelope, propellant/payload coupling, receiving trajectory, docking/landing and handling dependencies. Track last-mile support: material in orbit is not material at a surface workshop. A cargo manifest is not a replenishment event.

For interstellar routes, explicitly select trajectory/time convention and technology. Nonrelativistic authored cruise legs need acceleration/braking, endurance and destination/capture arrangements where consequential. A constant-speed duration `distance/speed` is only its declared coast abstraction; it is not a relativistic mission solution. When relativistic motion or timing would affect play, use a separately specified adapter distinguishing world coordinate time, crew proper time, communications and supported propulsion. The Newtonian adapter cannot be extrapolated to light-speed travel.

Generation ships, suspended animation, cloning, synthetic crews and autonomous seed probes are optional content with declared biology, maintenance, continuity and authority. They do not erase needs, copy skills or grant infinite endurance by name. FTL travel never implies FTL communication, free entry/exit velocity matching or restored fuel unless the selected setting module explicitly establishes those effects.

### 9.2 Off-world settlement and ISRU adapter

Core §§72–74/103–108/113–114/117/121–122 own settlement, construction, production, governance, programs, economy and life. Select the actual project and responsible institutions through those procedures. SPACE supplies these additional acceptance gates:

1. **Site and access:** survey environment, illumination cycles, terrain, communications, local material evidence, landing/docking/handling and delivery/escape windows (§§4/6/8/9.1). Separate a discovery/claim from physical access, accepted product, sovereignty and community consent.
2. **Mission support:** bind imported equipment, people, support/return commitments and time horizons to actual flight stages. Surface demand cannot draw orbital cargo until descent and handling actually finish. Keep cargo/passengers in their real transit locations under Core §§102/105–106.
3. **Habitation acceptance:** verify pressure, atmosphere quality, thermal rejection, power, shielding and any organism-specific environmental requirements for the actual occupants (§7). Construction completion alone is not accepted service; use Core §103 testing/commissioning.
4. **ISRU feasibility:** choose a proven source/access and extraction/processing chain: survey → sample → test → extract → process → inspect/accept → store → transport. Specify feedstock composition/uncertainty, recoverable fraction, equipment and operators, energy and heat rejection, consumables, reaction inputs, output purity/specification, waste, capacity, storage and downstream delivery. Core §§104/108/109 perform the work and material accounting. Ice detection supplies neither an excavator nor propellant production; oxygen output alone does not supply a fuel/oxidizer pair.
5. **Sustained viability:** assess each function separately over a declared horizon: atmosphere, water, food, medical capability, maintenance/spares, staff succession, industrial reproduction, import/export links, communication and escape. Forecasts use current eligible stock and actual feasible future supply separately (Core §§36/41/71/107–108). Independence in water grants no medicine or replacement machinery.

### 9.3 Colony-specific risk and continuity overlay

This overlay subscribes to real environmental, component, access, staffing and information changes. It adds no universal disaster roll, colony level, risk points or population penalty.

| Trigger / space dependency | Evaluate through | Supported response / stop |
|---|---|---|
| Breach, atmosphere contamination or airlock fault | Connected §7 zones and Core §§19/101/118 | Existing isolation/control, usable shelter and care; evacuation requires actual suit/transport capacity and authorization |
| Loss of power, thermal rejection or timed illumination | §7 thermal/environment profile; Core §§101–103/109 | Real buffers and supported operating modes; threshold frontier precedes reserve exhaustion |
| Missed launch window, lost receiving interface or delayed import | §§4/6/9.1; Core §§35–37/102/105 | Reforecast the next supported arrival and local deficit; remote stock and contractual obligation persist |
| ISRU rejects product or extraction encounters different material | §9.2; Core §§104/108 | Preserve spent input/work and actual rejected product/waste; use accepted compatible output only |
| Critical specialist, machine or knowledge carrier unavailable | Core §§14/41/107–108/122 | Evaluate actual substitutes and support; manuals and population totals do not create competence |
| Remote policy change or long communication outage | §8; Core §§29/64/113 | Local knowledge and formal mandate assessed separately; ongoing feasible autonomous work continues |

A warning changes knowledge only when detected/received. Common-cause faults can defeat supposedly redundant systems if they share a real dependency; account for each physical fault once through Core §101. Preservation, maintenance and reproducible local manufacture are different capabilities. A prosperous settlement may remain safe and ordinary; success does not require replacement hazards. Long intervals use Core §§11/62/69/86/96/106 to preserve age/process law, people, tools, knowledge carriers, conditions, stock, work, messages and succession. Births, cloning, suspended animation and protagonist family choices require their own enabled processes or declarations.

## 10. Space content starter library

These are substantive reusable templates with required activation fields; no actual craft, site or organization is spawned. Namespace `SPACE-LIB`; all eight IDs and their activation payloads below are retained from v0.1. Definitions are pinned as `SPACE-LIB@0.1`, interpreted through this proposed Core-3.2 bridge; instances separately pin their campaign variant. Core §111 governs identity and activation. No ID is renamed, retired or automatically rebound. Missing values remain unresolved only for the dependent calculation.

| Entry | Specialized content/procedure | Activation/calibration fields |
|---|---|---|
| `SPACE-LIB.CRAFT.IMPULSIVE-TRANSFER` | Two-body coast segments and declared short burns; supports orbit-to-orbit delivery | Body/frame/state, mass references, engine/feed and burn-duration validity, phase, receiving envelope, support/return plan |
| `SPACE-LIB.CRAFT.LOW-THRUST` | Continuous thrust with changing mass/power/orientation; never substitutes instantaneous Hohmann timing | Force/mass-flow model, controls, integrator/event/error criteria, generation/thermal limits, approach model |
| `SPACE-LIB.HAB.PRESSURE-ZONE` | Compartment with real gas, connections, atmosphere-control tasks and alarms | Volume, species, temperature, equation of state, leaks, control capability, engineering limits and organism effects separately |
| `SPACE-LIB.SVC.AIRLOCK` | Staged transfer/recovery/venting with occupancy and interlocks | Zone refs, gas routing/recovery/storage capacity, duration, power, hatch state, policy and failure envelope |
| `SPACE-LIB.LINK.STORE-FORWARD` | Buffered packets through actual relay contact windows | Nodes/ephemerides, propagation and serialization, power, capacity, packet identity/expiry/order, receipt/ack policy |
| `SPACE-LIB.SITE.EXTRACTION-OUTPOST` | Survey→sample→test→mine→process→accept→store→transport chain | Proven source, access/rights, machinery, staff, consumables, yields/waste, power/heat, output specs and recurrent support |
| `SPACE-LIB.OP.SURFACE-DELIVERY` | Orbit/approach→descent→landing→handling→accepted delivery | Actual initial state, craft/site/weather envelope, stage inputs/time, receiving means, abort and ascent/return if required |
| `SPACE-LIB.SET.INTERSTELLAR-ROUTE` | Authored distant route with explicit technology/time/authority constraints | Drive and brake model, mass/endurance, world/crew time, information delay, destination verification and continuity |

An equipment family from Military's AIR index may provide provenance/category, then a space variant supplies genuine missing flight/support fields. Do not manufacture statistics for the entire index. A surface sport, vacuum arena or station career can use the sports library while this foundation supplies environment and transportation; sport-specific performance/scoring definitions stay with the selected entry, while Core §123 owns organizer/ruleset/eligibility/fixture/results/records/consequences. The entry uses the activity mechanics; space supplies only its actual environment and transport.

## 11. Events and runtime

Subscribe through Core §§11/91/112 to actual component/stock/crew/service changes, observations, received commands, project acceptance and authority transitions. The following event names are retained; compound names denote separate lifecycle events, not simultaneous repeated costs. Emit only triggered events:

| Event | Owned consequence / interface |
|---|---|
| `SPACE.maneuver_started/completed/interrupted` | Actual input expulsion, time and flight-state write set; derived forecast refreshed |
| `SPACE.contact_window_changed` | K-NET link access changes; queued messages remain until transmitted/expired under terms |
| `SPACE.command_received/rejected/executed` | K-INFO receipt/assessment plus separate actual action; no duplicate effect on later acknowledgment |
| `SPACE.rendezvous_achieved`, `SPACE.docked/landed` | Supported relative/craft state; enables only actual next transfer/connection tasks |
| `SPACE.atmosphere_changed`, `SPACE.thermal_limit_reached` | Existing gas/energy/asset state; exposures or equipment effects only through profiles |
| `SPACE.EVA_started/returned/interrupted` | Existing participant locations, real airlock/suit resource use and supported exposure |
| `SPACE.site_sampled/process_verified` | Actual sample/product plus scoped evidence; no automatic commercial reserve |
| `SPACE.habitat_function_accepted` | K-WORK acceptance and K-NET supported service activation; no duplicated project or restored residents |

Core §§11/91 are the only event coordinator and commit procedure. Space callbacks return proposed owner-qualified changes and their next frontier; they do not maintain a second scheduler. Core §§10–12/62/86/109 govern retained outcomes, allocations, spans, snapshots and views.

**Runtime activation:** start a mission leg, maneuver, contact plan, pressure/thermal process, EVA or accepted settlement function only after its dependent records/profile fields are available. Recompute on an actual configuration, environmental, input, route, instruction or knowledge change. Advance continuous models to the earliest supported threshold/queued event; discrete processes use declared intervals. No mandatory per-turn background roll is added.

**Stop and recovery:** stop thrust on its actual exhaustion/completion/cutoff; continue coasting dynamics. Stop an expired contact transmission and retain packets per policy; propagation already underway persists. Isolate a leak only after a real closure/repair; gas already lost remains lost. Interrupt EVA at actual limits within authorized return/abort instructions; new voluntary acts require control. Stop ISRU at exhausted input, rejected configuration or completion; preserve partially processed matter and work. Revalidate repaired systems through Core §103 before restart. Forecast recomputation never changes executed history.

**Information and scheduling:** all emitted observations carry occurrence/observation/transmission/receipt times where distinct. A remote report cannot deliver cargo, repair hardware or apply damage a second time. Frame/epoch/trajectory state and contact queues persist across scale changes. Involuntary breaches, radiation exposure or real losses continue when a competing discretionary allocation is unresolved; reservations do not prevent physical damage (Core §§11–12).

## 12. Acceptance requirements

These 24 source acceptance IDs are preserved verbatim. They are requirements, not pass claims. §17 maps bounded evidence to portions of these requirements; unmapped behavior remains an implementation/acceptance backlog.

| ID | Trigger | Required behavior |
|---|---|---|
| SPACE-01 | Same orbit represented in two frames/epochs | Transform supported state consistently; no relabel-induced thrust; unknown transform blocks dependent comparison |
| SPACE-02 | Analytic transfer outside its assumptions | Reject/defer unsupported calculation or select explicit other model; no skill-created transfer |
| SPACE-03 | Equal-radius craft have different phase | Zero orbit-change budget grants no rendezvous or docking |
| SPACE-04 | Target matches position with incompatible relative velocity | No safe capture unless actual envelope supports it |
| SPACE-05 | Sequential ideal burns and extra cargo | Current mass drives each burn; cargo changes capability; no separately spent delta-v stock |
| SPACE-06 | Propellant/feed missing, zero/negative input, replay/conflict | Invalid proposal atomic rejection; exact replay no additional mass/velocity/resource effect |
| SPACE-07 | Stage/cargo jettison | One actual location/mass change; no duplicate propellant debit or erased property history |
| SPACE-08 | Burn fails/Mixed after actual use | Record achieved path and real costs; no invented collision, refund or new voluntary rescue |
| SPACE-09 | Long coast crosses a queued event | Stop at actual frontier; changing review cadence/save cannot skip or repeat it |
| SPACE-10 | Command and delayed acknowledgment | Receipt/execution/confirmation distinct; stale knowledge and endpoint validity retained |
| SPACE-11 | Moving endpoints, occultation or relay wait | Use selected propagation/link method; issue does not imply receipt; unsupported precise arrival remains unresolved |
| SPACE-12 | Revocation precedes distant receipt | Institutional terms and actor knowledge differ; no telepathic stop or invented PC decision |
| SPACE-13 | Same gas expands into added volume | Recompute supported pressure without creating/destroying gas; total pressure not guaranteed breathability |
| SPACE-14 | Leak, valve closure and delayed alarm | Apply physical changes once, then supported thresholds/exposures; closure/notification must actually occur |
| SPACE-15 | Recycling or airlock cycle | Actual input/output/waste/resource accounting; no duplicated recovered gas/water or free cycle |
| SPACE-16 | Heat burst followed by cooling | Check actual peak and supported limit before dissipation; no vacuum-convection shortcut |
| SPACE-17 | EVA task reaches authorized reserve/stop | Preserve return resources/actual costs and return control where required; suit is not universal protection |
| SPACE-18 | Arrival with no powered handling | Cargo aboard, local stock unchanged; later actual handover once, reports read-only |
| SPACE-19 | Survey discovers resource estimate | Belief/evidence changes; usable product needs actual recovery/processing and acceptance |
| SPACE-20 | Colony power/medical/food deficit | Existing population persists; actual useful service allocation, independent institutions and obligations continue |
| SPACE-21 | Long-term colony/ship succession | Preserve people, tools, knowledge carriers and support; no automatic births, expertise or restored conditions |
| SPACE-22 | FTL or relativistic mission proposed | Require selected compatible module/model; no inferred instant communication, free braking or cloned identity |
| SPACE-23 | Orbit cargo delivered to surface workshop | Required descent/access/handling actually completed; regional stock cannot bypass last-mile transfer |
| SPACE-24 | Cross-campaign flight/message replay or scale transition | Scoped references and IDs; no imported lore/state, duplicated transit or repeated intervals |

## 13. Calibration, unresolved work and migration

**Ready to specify:** ownership and procedures above. **Requires campaign/profile data:** ephemerides/frames, craft masses and performance, force/engine/feed models, launch/entry/docking envelopes, atmosphere/thermal/chemistry, organism care, communications/link budgets, resource yields, local institutions and route support. Define units, valid range, source/status, numerical method/tolerance, thresholds, extreme cases and relevant interactions for each selected family.

**Unresolved implementations:** general multi-body/low-thrust flight propagation; validated docking/contact and entry/landing envelopes; pressure-dependent leaks and full atmosphere chemistry; spacecraft radiation/thermal and organism models; moving-endpoint link solver; relativistic travel/time; detailed ISRU and long-duration biological/ecological continuity. Optional orbital combat also requires explicit sensor, geometry, weapon/effect and debris models; an AIR index entry does not supply them. These gaps do not prevent a bounded authored mission, but they prevent unsupported quantitative claims.

Migrating an existing campaign is prospective. Pin its actual adopted Core and current state; keep asset/person/lot IDs and processed history. Attach frame/epoch/units only from supported evidence; do not invent a trajectory from a narrative location. Preserve actual remaining propellant, cargo, messages in transit, conditions, mandates, work and commitments. Add unknown fields rather than granting an atmosphere, engine, pressure hull or competent crew. If previous delta-v was treated as an abstract reserve, identify its meaning and conversion evidence before mapping; never also spend newly reconstructed propellant for the same resolved burn. Keep ongoing route/mission rules pinned until an authorized transition.

This foundation makes no new Core promotion. The complete §15–16 matrix accounts for the receiving ownership bridge. Any later broadly reusable discovery is a separate proposal tested in another genre before Core adoption. External scientific references support the selected ideal relations; they do not validate the IRGS procedures, numerical craft profiles or actual campaigns. Sections 15–16 record source locators, new mechanics, inherited interfaces and rejected interpretations within this complete specification.


## 14. Receiving interfaces, models and initialization

### 14.1 Record ownership and write boundaries

`SPACE.*` names describe extension schemas/workflows, not additional global state owners. All twelve v0.1 record types remain available. The R2 binding lists seven representative local records; it does not explicitly retire BodyProfile, CraftEnvelope, Maneuver, MissionLeg or ExtravehicularPlan. Those five are retained here with explicit bindings. No original field is discarded; the §3 field list and this table form one contract.

| Extension schema | Authoritative storage / read inputs | Permitted output and boundary |
|---|---|---|
| `SPACE.BodyProfile` | Versioned definition/profile; actual body/place facts referenced through Core §79 world records | Selected gravity, shape, ephemeris and environmental model; discovery writes K-INFO evidence, not a new body or material stock |
| `SPACE.FlightState` | K-ASSET location extension; estimate/uncertainty in K-INFO; epoch tied to K-TIME | Actual position/velocity and propagation span; estimates never overwrite actual state; contained cargo moves by the same asset reference |
| `SPACE.CraftEnvelope` | Versioned profile and K-ASSET configuration; Core §§55/101/112 | Supported modes and derived limits for actual configuration; no second component condition or performance stock |
| `SPACE.Maneuver` | K-WORK operation plus K-TIME commitment; actual asset, eligible K-STOCK feed, actor/instruction references | Requests coupled gas/propellant expulsion and achieved K-ASSET flight-state change; retained uncertainty and authorization remain Core records |
| `SPACE.MissionLeg` | K-WORK stages/K-NET route with K-TIME windows; same asset/actor/cargo references | Actual departure, transit and arrival conditions; forecast arrival does not move anyone |
| `SPACE.ContactPlan` | K-NET channel/window/queue; K-ASSET pointing/power configuration; ephemeris profile | Actual access/allocation/transmission and scheduled propagation; receipt updates K-INFO only when delivered |
| `SPACE.RemoteCommand` | K-INFO message and instruction references; K-ORG/GOV mandate; Core §30 lifecycle | Receipt/interpretation, accepted task references and separately transmitted acknowledgments; execution writes through its actual task's owners |
| `SPACE.PressureZone` | K-ASSET compartment volume/connections; K-STOCK gas lots; profiled thermodynamic state | Transfers/ejection/species transformation and derived pressure; no second gas quantity; medical consequences are separate supported events |
| `SPACE.ThermalState` | K-ASSET component/node process extension; K-TIME processed spans; actual inputs and geometry | Thermal energy or temperature as selected authoritative state; the other is derived through a declared model, not a duplicate energy balance |
| `SPACE.ExtravehicularPlan` | K-WORK operation/K-TIME commitments; K-ACTOR participants; K-ASSET suits/airlock; K-STOCK inputs | Actual staged movement, work, transfers and exposures; no invented voluntary EVA, return maneuver or resource commitment |
| `SPACE.SiteAssessment` | K-INFO evidence/estimates; Core §104 actual site/resource references | Updated coverage/sample evidence; actual extraction writes source and outputs through K-WORK/K-STOCK |
| `SPACE.SettlementTransition` | CIV/URBAN workflow and K-WORK acceptance; Core owner references for population/services | Function-specific acceptance, demand and support assessment; no duplicated colony progress, inhabitants, treasury or stock |

Reads and writes carry campaign scope, expected record version, causal time, profile/units, provenance, instruction/mandate and knowledge access as applicable. The coordinator is always Core §11/91. A physical loss can reduce reservation backing; a blocked discretionary allocation cannot suspend an independent breach. Source event names in §11 remain stable.

### 14.2 Material model contract

Core §§61/109/112 own measurement interpretation, model validity and derived capability. Each enabled model pins `model_id/version/status/source, task/configuration, input owner fields and as-of time, output meanings/owners, units/time basis, assumptions/envelope, update law, uncertainty, thresholds, stopping/recovery, method/event detection/tolerance`. Use one compatible interpretation per cause. The following local adapters are defined here; their IDs are new proposed adapter identifiers, not replacements for content IDs.

| Adapter | Inputs, valid use and outputs | Limits and numerical/qualitative handling |
|---|---|---|
| `SPACE-MODEL.AUTHORED-LEG@0.2` | §2/4.3/6.2/9.1: source-supported route, actual configuration/mass, departure/arrival windows, stage time/resources, receiving/return envelope | Qualitative operation is allowed only inside explicitly supported bounds. Unknown transfer, landing or feed parameters cannot be invented. No trajectory precision beyond the authored envelope |
| `SPACE-MODEL.TWO-BODY@0.2` | §4.2: positive finite `mu` [length³/time²], radii and semimajor axis [length]; circular coplanar transfer assumptions; speed [length/time], half-period [time] | Positive finite compatible units and geometrically valid radii required. Impulsive idealization excludes finite thrust, phase solution, atmospheric losses and local launch/capture. At equal radii return no energy-change transfer and no arrival time; choose a separate phasing/coast task |
| `SPACE-MODEL.IDEAL-REACTION@0.2` | §5: `m0 > 0`, `ve > 0`, eligible propellant and retained mass in consistent mass/speed units; ideal consumed mass and delta-v | Requested ideal delta-v must be finite and nonnegative; zero is a no-burn forecast, not a positive consumption event. Reject insufficient compatible feed; reserve is not expulsion. No scalar ideal delta-v substitutes for vector/time/thrust feasibility |
| `SPACE-MODEL.IDEAL-GAS@0.2` | §7.1: finite nonnegative species amounts [mol], positive volume [m³], absolute temperature [K], consistent R [Pa·m³/(mol·K)]; total/partial pressure [Pa] | Amount-to-mass conversion requires species molar masses. Zero gas gives zero pressure, not habitability. Volume/temperature changes require actual events; a maintained-temperature expansion needs its specified thermodynamic assumption. No leak flow, chemistry or physiological effect follows from the equation alone |
| `SPACE-MODEL.FIXED-LINK@0.2` | §8: nonnegative separation [length], positive signal speed [length/time], fixed endpoint approximation during transmission/propagation; arrival time | Include actual queue, serialization, relay and processing. Real ordinary electromagnetic communication uses its supported light-speed model; normalized fixture `c=10` is test data. Moving endpoints require the next adapter |
| `SPACE-MODEL.MOVING-LINK@0.2` | §8: sender state at emission, receiver ephemeris and compatible inertial time/frame; solve `norm(x_receiver(t_receive)-x_sender(t_emit)) = c*(t_receive-t_emit)` | Proposed solver contract, not a supplied general solver. Find a physically valid future solution within the ephemeris interval; check visibility and actual receiving access. Each emitted portion/relay has its own causally applicable path. Curved spacetime or relativistic clock corrections require another model |
| `SPACE-MODEL.CONFIGURED-PROCESS@0.2` | §§6–9: selected finite-thrust, entry, leak/chemistry, thermal, exposure, EVA, ISRU, ecology or relativistic process | This is an activation contract, not an implementation. Supply the complete local law/envelope, units, inputs/output/waste, uncertainty and threshold method before dependent use. A name or hash does not supply missing physics |

Closed-form evaluations declare precision where a decision depends on it. Numerical propagation must specify error bounds, convergence checks and event detection; no default integration step or universal tolerance is supplied. Synthetic tests use their stated tolerances only. Actual frame conversions must transform both position and velocity, including motion/rotation effects relevant to the chosen frames; an unknown transform blocks the comparison rather than relabeling vectors.

The analytic transfer equations concern orbital energy/path geometry. Interplanetary plans additionally bind departure and arrival local frames, sphere-of-influence or other transition model, compatible epoch, planetary encounter phase, and capture/escape resources where relevant. Interstellar setting models must define world/crew time, navigation, acceleration/braking and receipt semantics; enabling FTL motion never implicitly enables FTL messaging.

### 14.3 Content bindings and qualification gates

Pin `IRGS-SCL-1.0` as catalogue release and its actual immutable family revisions `@0.2`. Pin `SPACE-LIB@0.1` as the specialized source library. This engine's `0.2` version does not silently revise those eight entries. Their original payloads are embedded in §10 and preserved in the supplied source snapshot; an instance separately names its supported variant/configuration.

The R2 normative registry explicitly retains SPACE-LIB as eight specialized templates with no wholesale neutral promotion. The R1/R2 maturation overlay is non-normative and unselected: its 228 held-family proposals and 420 authored acceptance specifications do not change the registry's 51 selected / 228 held gates. No SCL alias is invented for a SPACE-LIB ID.

When ordinary shared content is useful, exact optional examples are:

| Original alias | Exact SCL target | Type / selector / receiving status |
|---|---|---|
| `PL:RES-WAT-001@1.0` | `SCL:PBC-RES-PL-RES-WAT-001@0.2` | stock / null / selected qualitative |
| `PL:RES-IND-001@1.0` | `SCL:PBC-RES-PL-RES-IND-001@0.2` | stock / null / selected qualitative |
| `PL:STO-003@1.0` | `SCL:PBC-EQP-PL-STO-003@0.2` | storage_system / null / selected qualitative |

These references are resolved and checksum-pinned in `content_bindings.json`. They do not provide spacecraft certification, compatibility, quantities, rates or actual installed equipment. A bulk-water tank is not automatically a pressure vessel for oxygen. Additional entries require their exact namespace/revision/type/selector/checksum and native profile. Held definitions may use their exact source-backed content under Core §111; they may not impersonate a promoted shared replacement.

### 14.4 Campaign activation and overrides

Before dependent use, record: Core/binding/catalogue/engine versions; enabled domains and model versions; actual source-supported actors/assets/sites; world and knowledge state; units/time conventions; flight/environment/organism/needs/recovery profiles; exact content variants; authority and autonomy limits; actual commitments/resources; start snapshot and pending events. Apply Core §§88/111–112. Initial state is created only by authorized initialization or actual production, never by attaching this document.

There is no default FTL, artificial gravity, resurrection, cryostasis or cloning override. A setting module states the exact parent behavior replaced, targets, access, time/costs, entry/exit state, detection/counterplay, persistence, recovery and effective adoption. Preserve unaffected Core rules. Gravity changes may affect trajectory, local mobility, fluid/thermal behavior and organism requirements differently; an override must state its supported scope rather than grant all benefits.

For fully specified routine work, use Core's automatic qualified execution. For unresolved outcome-changing parameters, resolve a complete prospective profile or named bounded ruling before dependent action; otherwise leave that calculation pending. Continue independent known processes. No implied player choice, unsupported quantity or favorable engineering answer fills the gap.

### 14.5 Exact R2 provider contract

Pinned `IRGS-BIND-SPACE-3.2`; all ten provider groups are retained. Enable each only when its function is relevant.

| Shared function | Core v3.2 sections |
|---|---|
| resolution_agency | §4, §5, §6, §7, §8, §9, §90 |
| time_events | §10, §11, §12, §47, §62, §85, §90, §91, §96 |
| actors_conditions | §14, §15, §16, §17, §18, §19, §64, §68, §69, §70, §71, §106, §118, §122 |
| stock_economy | §12, §20, §22, §24, §35, §36, §37, §38, §105, §109, §114 |
| assets_components | §21, §23, §48, §49, §53, §54, §55, §56, §57, §58, §101 |
| work_services | §23, §41, §43, §71, §72, §73, §101, §102, §103, §104, §107, §108, §110, §119, §121 |
| information | §2, §30, §60, §61, §79, §85, §86, §115, §120 |
| institutions_life | §25, §26, §27, §28, §29, §31, §32, §33, §34, §38, §39, §40, §44, §45, §46, §65, §66, §67, §68, §69, §76, §107, §113, §117, §122 |
| content_modules | §88, §97, §98, §99, §111, §112 |
| competitions | §6, §47, §61, §91, §99, §112, §123 |
| maritime | §116 |

## 15. CMRR source and reconciliation matrix

### 15.1 Source authority and provenance

| Key | Input / locator | Role and status |
|---|---|---|
| U | Current user instructions, including explicit switch to R2 | Controlling task scope; replaces earlier v3.0/v3.1 target, not campaign history |
| S | `inputs/Space_Exploration_and_Colonization_Foundation_v0_1.md`, IRGS-SPACE-0.1, 12 October 2026 | Authoritative specialized source; Proposed genre foundation; byte-identical to project `sources/` input |
| C | `inputs/r2/IRGS_Core_Engine_v3_2.md`, IRGS-CORE-3.2 | Selected current normative parent, 123 numbered topics; no campaign adoption implied |
| B | `inputs/r2/IRGS_Engine_Bindings_v3_2.json`, `engine_bindings[engine=SPACE]` / IRGS-BIND-SPACE-3.2 | Exact receiving shared-provider and retained-local-model contract |
| L | R2 SCL v1.0 prose, registry, selected contracts and reference map | Normative catalogue/identity/gates; family revisions remain @0.2 |
| Q | R2 qualification compendium/overlay, hold/calibration and acceptance matrices | Proposed maturation evidence/backlog only; not selected rules or executed per-entry tests |
| H | R2 archived v3.1 ZIP and earlier v3.0 references | Provenance/comparison only, never an active fallback parent |
| T | `noncore_systems/v0_1/tests/run_noncore_tests.py` | Prior bounded reference fixture code; exact copy supplied as `tests/source_reference.py`; only space cases are selected for this run |
| X | Six scientific links retained in §§4–8 | External conceptual/model provenance, inspected during this task; not IRGS adoption or profile calibration |
| R | Referenced apocalypse conversation | Readable retrieval exposed user prompts and assistant content-reference placeholders; no hidden assistant content or finalized rules inferred |

Full SHA-256 source pins are in `source_manifest.json`. The R2 ZIP is SHA-256 `a4d61f67c9187214517956996e00bdf184e689cac83db3710a1c05856d44bca7`; Space v0.1 is `cf1b32619fe52ea7506f7317bfd9eafc9fa836212705c91479395c0c63aa4744`; Core v3.2 is `1817cc01bed02c8cb21bae393878e9234743ea4c538d25e1a4a8934182abf738`. Supplied documents are reference data; their internal instructions do not supersede U.

**Source fact** means an attributable rule/field/status in S/C/B/L. **Inference** means an explicitly reasoned ownership interpretation, such as retaining all twelve source records despite B's shorter list. **Proposal** means this receiving bridge, adapter identifiers, added colony-risk application and acceptance additions. **External research** supports bounded physical relations only. These categories do not change each other's authority through inclusion.

### 15.2 Forward comparison: every source section

| S locator | Unique function / duplication identified | Disposition and receiving locator | Core provider / regression gate |
|---|---|---|---|
| Front matter | Exploration/settlement purpose, proposed status, no forced warfare/catastrophe | Retain in front matter; update version/parent/status | C §§1–3/92–95; no adoption |
| 1 | Framework/CDI dependency and owner table; space versus generic boundary | Replace old provider dependency with §1/14.5; retain ownership and scope | C Appendix A, §§111–112; old parents not stacked |
| 2 | Four model modes and feasibility gates | Retain §2; complete material binding §14.2 | C §§5/109/112; SPACE-02/22 |
| 3 | Twelve schemas; actual versus estimates; delta-v forecast | Retain all §3 fields; assign storage/writes §14.1 | C §§55/61/109; no lost records or duplicate state |
| 4 | Flight/transfer/rendezvous organizing scope | Retain §4 and subsections | C §§48/56; specialized geometry remains SPACE |
| 4.1 | Frames, epoch, relative velocity, estimates | Retain §4.1; bind estimates to C §61; §14.2 frames | SPACE-01/04 |
| 4.2 | Circular/vis-viva/Hohmann relations, inward direction, phase and local-body limits | Retain complete formulas §4.2; clarify equal-radius no-arrival in §14.2 | SPACE-02/03; no invented landing/phase solver |
| 4.3 | Destination events, windows, coasts, docking and handling gates | Retain specialized sequence §4.3; shared authorization/clock inherited | C §§5/11/102–105; SPACE-04/08/09/18/23 |
| 5 | Rocket mass/exhaust, feed, sequential burns, cargo/jettison and component limits | Retain §5; generic component upkeep becomes exact Core reference | C §§12/21/23/55/101/109; SPACE-05–08 |
| 6 | Planetary environment/arrival/exploration scope | Retain §6 | C §§19/79/104/118–119 |
| 6.1 | Gravity, atmosphere, radiation, illumination, dust/chemistry/ecology and capability | Retain §6.1; no universal physiology | SPACE-14/17/20 |
| 6.2 | Separate launch, entry, descent, landing, ascent; service envelopes | Retain §6.2 | SPACE-02/23; no skill-created capability |
| 6.3 | Instrument coverage, samples, resource interpretation, inhabitants' agency | Retain space method §6.3; discovery/stock ownership references C | C §§60–61/79/104/113; SPACE-19 |
| 7 | Habitat/support organizing scope | Retain §7 | C §§71/101–103/109 |
| 7.1 | Gas amounts/species/volume/temperature, pressure, connections/leaks/isolation | Retain §7.1; clarify state/derived variables §14.1–2 | SPACE-13/14; pressure is not inventory or breathability |
| 7.2 | Recycling chemistry, CO2 removal, real reserve gas, agriculture and shared service power | Split: retain specialized requirements §7.2; replace generic accounting/allocation with C | C §§73/101–103/108–109/119; SPACE-15/18/20 |
| 7.3 | Vacuum thermal paths, geometry, radiator/peak constraints | Retain §7.3; replace generic burden algorithm with C §109 | SPACE-16; no free cooling |
| 7.4 | EVA task/return resources, staged airlock, restraint and suit boundaries | Retain full specialized sequence §7.4 | C §§4/10/19/109/118; SPACE-15/17 |
| 8 | Light-time/moving endpoints, serialization/relay, remote mandate and 0/10/12/22 example | Retain space propagation/contact and example; generic command lifecycle now C §30 | §§8/14.2; C §§29–30/61/85/102/113; SPACE-10–12 |
| 9 | Mission logistics/colonization scope | Retain §9 | C §§35–37/102/105–108 |
| 9.1 | Windows, mass/payload coupling, last mile, interstellar/relativistic/FTL boundaries | Retain §9.1, profiles §14.2/14.4 | SPACE-18/21–23 |
| 9.2 | Settlement objective/authority, site, delivered construction, acceptance, occupants, ISRU, viability | Split: C owns generic projects/population/governance; space gates §9.2 and risk application §9.3 retain each stage's function | C §§72–74/103–108/113–114/117/121–122; SPACE-19–21/23 |
| 10 | Eight exact IDs and full activation payloads; equipment/sport interoperability | Retain §10 table unchanged; clarify SCL and COMP bindings §14.3 | C §§111–112/123; ID/payload equality check |
| 11 | Eight lifecycle event rows and scheduling/atomicity/scale requirements | Retain all event names §11; replace shared event algorithm with C §§11/91 | §14.1 write bindings; SPACE-06/09/24 |
| 12 | Twenty-four acceptance requirements | Retain exact IDs and row text §12; segregate evidence §17 | No test-number substitution or implied live playtest |
| 13 | Calibration gaps, advanced implementations, optional combat, prospective migration | Retain §13; add model gates §14.2, gaps §17.3 and operational migration §18 | C §§97/99/112; no hidden solver or conversion |

### 15.3 Reverse comparison: Core and R2 → space

| Receiving provider/requirement | Space consumer and required reconciliation | Result / excluded duplication |
|---|---|---|
| C §§4–9/90: action, feasible stages, Mixed | §§4–8 bind physically supported effects; authorized alternatives only | Inherited; no new universal space die/stat or consequence table |
| C §§10–12/47/62/85–86/91/96: shared time, journal, contention and scales | §§3/11/14 retain spans, snapshots, queues, decisions and actual losses | Inherited; no separate flight/colony clock |
| C §§14–19/64/68–71/106/118/122: people, conditions, needs, life | §§6–9 bind organisms, crew, colony/ship continuity | Inherited; no colony rating converted into deaths or free crew |
| C §§12/20/22/24/35–38/105/109/114: stock, economy, rates and claims | §§5/7–9 couple feed/gas/cargo to actual lots | Inherited; no independently spent delta-v or mission-budget duplicate |
| C §§21/23/48–49/53–58/101: components, spatial effects, dependencies | §§3–7 actual spacecraft/suit states and effect envelope | Inherited; optional combat still needs explicit specialized profiles |
| C §§23/41/43/71–73/101–110/119/121: work and services | §§7/9 acceptance, ISRU, useful support and long-term reproduction | Inherited; no new generic colony economy, industry or maintenance subsystem |
| C §§2/30/60–61/79/85–86/115/120: information/measurement/commands | §§4.1/6.3/8/14.2 estimates, survey and actual receipt | Generic command/measurement contracts relocated to Core; propagation/geometry remain SPACE |
| C §§25–29/31–34/38–40/44–46/65–69/76/107/113/117/122: institutions/life | §§8–9 remote mandates, settlement authority, autonomy and succession | Inherited without campaign politics, automatic obedience or protagonist micromanagement |
| C §§88/97–99/111–112 and Appendix B: deployment/identity/migration | §§1/10/14/18 exact pins and supported state mapping | Active parent only C; historical archives are provenance |
| C §116 and B's listed MAR domain | §1 water-phase boundary for amphibious craft; shared vessel interfaces already Core | Conditional water operation retained; no water flooding model applied to vacuum |
| C §123 and B's competition provider group | §10 optional station sport/exhibition module | Core administers contests; selected activity model performs them |
| B seven local-record names versus S twelve | §14.1 retains seven plus five omitted source schemas | Short list treated as non-exhaustive; no additional global state owner |
| L exact aliases, selectors, checksum and native-model holds | §§10/14.3, machine content bindings | SPACE-LIB stays specialized; catalogue v1.0 is not family revision @1.0 |
| Q R1/R2 proposals, authored case specs and hold registers | §14.3/17 record status; no selection | No held-entry promotion, deprecation, calibration or execution inferred |

The exact ten provider groups from B, including all section numbers, are reproduced as references in §14.5. Remaining Core topics continue to govern their actual applicable functions; a slim engine's consumer table neither deletes Core nor forces every domain to run on every review.

## 16. Accounted removals, conflicts and change log

| ID | Removed/replaced expression or conflict | Function retained at | Reason / migration effect |
|---|---|---|---|
| RM-01 | S §1's active Framework v2.1/CDI interface baseline | §1 and C §§111–112/Appendix A/B | Superseded shared provider pin; no campaign auto-upgrade |
| RM-02 | S §7.2 `Core B5` shorthand and generic bundle/allocation prose | C §§101–103; local recycling/atmosphere constraints §7.2 | Exact current provider replaces ambiguous legacy locator |
| RM-03 | S §8 `Core B2` shorthand and locally restated command/authority lifecycle | C §§10/29–30/113; space contact §8 | Retains revocation versus receipt/execution; no telepathic control |
| RM-04 | Generic service, accounting, construction/population operation portions of S §§5/7/9 | C §§12/23/72–74/101–109/113–114/117/121–122; §§5/7/9 applications | Algorithms inherited once; local gas, ISRU, habitat, access and viability gates kept |
| RM-05 | S §11 generic transaction/scheduler restatement | C §§11/91; §11 triggers/termination | No second engine loop; all original event names retained |
| RM-06 | S §12's unspecified companion-report implication | §17 explicit current evidence mapping/report | Old test numbering differs from acceptance IDs; no inherited coverage claim |
| RM-07 | Potential deletion of five records omitted by B | All twelve source schemas, §§3/14.1 | Retained, not deprecated; source's complete payload wins over a non-exhaustive summary |
| RM-08 | Earlier requested Core v3.0/v3.1 target | Explicitly selected R2 v3.2/SCL v1.0 | User correction; unfinished authoring artifacts are not a release or migration |
| RM-09 | Possible reading that S's sport entry owns contest administration | C §123 and §10 | Scoring/performance definition remains specialized; organizer/results/records stay Core |
| RM-10 | Possible equal-radius half-period misread as arrival | §§4.2/14.2 | Zero energy change has no inferred destination event; source fixture semantics made explicit |
| RM-11 | Possible R2 “full release” = promoted held catalogue | §14.3; normative registry unchanged | Qualification overlays remain proposed; original payloads and gates preserved |

**No source content ID, acceptance ID, source record type, specialized equation, space operating stage or listed unresolved implementation is retired.** No source file is edited. Removal here means removing a duplicate/obsolete statement from this receiving specification, with its valid function assigned above; it does not deprecate source definitions or erase history.

**v0.1 → v0.2 change log:** explicit Core v3.2/SCL v1.0 bridge; complete record-owner mapping; generic lifecycle/model/measurement rules inherited from current Core; explicit material model/activation contracts; complete specialized content pinning; colony-specific risk application; section-by-section forward/reverse CMRR; accounted removals; separate source acceptance and executable evidence identities; prospective migration and remaining calibration. These are proposed receiving changes, not new Core promotions.

## 17. Acceptance evidence, additional cases and calibration

### 17.1 Evidence levels and reference fixtures

`SPACE-01`–`SPACE-24` in §12 are source requirement IDs. The inherited Python script independently reused `SPACE-01`–`SPACE-16` for differently numbered fixture titles. This package labels those executions `REF-01`–`REF-16`, retains their original titles in `verification_results.json`, and maps them explicitly below. Passing a fixture supports only its modeled slice.

| Evidence label | Bounded implemented behavior | Source requirements partially exercised |
|---|---|---|
| REF-01/02/03 | Independent high-precision normalized Hohmann oracle, reverse-transfer symmetry, invalid input rejection | SPACE-02 |
| REF-04 | Equal-radius no-arrival result, phase gate and unsupported transfer rejection | SPACE-02/03; simplified docking gate only |
| REF-05/06/07 | Sequential ideal burns, mass conservation, payload, jettison, insufficient propellant, replay/conflict/campaign isolation | SPACE-05/06/07/24 |
| REF-08/09 | Fixed-link receipt/execution/ack timing and telemetry as-of versus receipt | SPACE-10; no moving-endpoint or institutional validity solver |
| REF-10/11 | Ideal gas expansion without new gas and distinct total/oxygen partial pressures | SPACE-13; no organism model |
| REF-12 | Habitat cargo arrives at time 4; adequate shared power at 6; handling completes at 8; actual water provision | SPACE-18/20; engineering service fixture, not medical survival |
| REF-13/14/15/16 | Review cadence, serialized checkpoint, independent simultaneous input order, continued shortage | SPACE-09/18/20/24; fixture events only |

All fixture quantities are synthetic: normalized orbital `mu=1`, engine `ve=1`, signal `c=10`, and explicit example gas/handling/consumption values. They are not planet, craft, human physiology or campaign defaults. Floating analytic oracle comparisons use absolute/relative tolerance `1e-12`; rational accounting is exact. Reference code is neither a general flight integrator nor the authoritative Core runtime.

Additional receiving checks in this package inspect source hashes, every source section disposition, all twelve schema names, eight exact content rows, all 24 acceptance rows, all source lifecycle event rows, exact parent anchors/provider groups, catalogue pins/readiness and absence of active legacy shorthand. Bounded new fixtures exercise moving-link timing, airlock gas recovery, peak-before-cooling, ISRU balances, docking relative velocity and independent uncertain-model gating. Deliberately faulty examples check that their oracles detect gas creation, premature unloading, double-allocated power and report-created stock. See the generated verification report for actual counts/results.

**Limits:** no claim of full acceptance coverage. Frame transformations/ephemeris validation, a physical finite-thrust solver, actual docking/contact/entry dynamics, pressure-dependent flows, radiation/organism responses, detailed EVA movement, legal remote mandates, general relay solver, industrial chemistry, ecosystem/generational dynamics, relativistic flight and live runner behavior remain unimplemented or untested here beyond stated fixture slices. Structural preservation is not behavioral validation. The R2 package's historical test claims are source evidence, not reclassified as fresh space tests.

### 17.2 Added acceptance specifications

The following are proposed cases. Only portions explicitly named in the verification report are executed; other outcomes below are acceptance criteria.

| ID | Given / trigger | Required observable result |
|---|---|---|
| SPACE-R2-01 | Replay an already executed remote command after propellant changes | Exact identity/payload is no-op before checking current feasibility; conflicting payload is rejected without mutation |
| SPACE-R2-02 | Moving receiver in normalized inertial fixture: initial distance 100, recession speed 2, signal speed 10, emission 0 | Receipt 12.5, not fixed-endpoint 10; no precision claim outside fixture |
| SPACE-R2-03 | Indivisible habitat support and cargo handling contend for one inadequate power provider | Honor actual policy; neither duplication nor unsupported fractional useful output; no invented player priority |
| SPACE-R2-04 | Airlock holds 10 synthetic gas units; actual recovery transfers 8; remaining 2 vent | Zone 0, storage gain 8, ejected 2; repressurization debits real storage once |
| SPACE-R2-05 | Thermal burden 4, action increment 7, engineering limit 10, later cooling 5 | Evaluate peak 11 before cooling; execute only if permitted override exists; no invented explosion |
| SPACE-R2-06 | ISRU processes 10 synthetic material units into 6 accepted product and 4 waste | Debit input 10; product 6; waste 4; acceptance cannot create more output or erase spent work |
| SPACE-R2-07 | Station-relative position meets approach gate but relative speed exceeds configured capture envelope | Docking unavailable; good piloting does not replace feasible braking/contact |
| SPACE-R2-08 | Numerical transfer unsupported while an independent supported atmosphere leak is active | Transfer calculation remains pending; actual leak continues to its next frontier |
| SPACE-R2-09 | Catalogue release 1.0 requested with fabricated family `@1.0`, or missing mode selector | Reject unsupported reference; do not substitute last-loaded or favorable content |
| SPACE-R2-10 | R2 qualitative proposal covers a held family | Preserve registry hold; no stock, parameters, acceptance or deprecation inferred |
| SPACE-R2-11 | Water-operating spacecraft switches to vacuum flight | Same asset/cargo/occupants; select SPACE physics; neither MAR flooding nor a new vessel instance is implied |
| SPACE-R2-12 | Settlement has water independence but imports medicine and machine parts | Report function-specific viability; no universal self-sufficiency, automatic births or competence |
| SPACE-R2-13 | Validity window closes at command receipt time | Use declared inclusive/exclusive and receipt/start/completion semantics; no implicit favorable endpoint |
| SPACE-R2-14 | Scientific sample analyzed by different observers at different times | Preserve sample custody/amount and assertion lineage; interpretations can differ without recreating sample or deposit |
| SPACE-R2-15 | FTL setting supplies travel only | No inferred FTL communications, free exit velocity matching, refill or restored conditions |
| SPACE-R2-16 | Same-age, same-resource, same-event state reviewed at day/year scales | Same processed history and obligations; genuine clock-law events retained; no fabricated reproduction or doubled progress |

### 17.3 Calibration and implementation gates

| Family / owner | Required before dependent quantitative use | Extreme and interaction checks still needed |
|---|---|---|
| Flight/frames — SPACE | Frame origin/axes/time scale, ephemerides, gravity, actual state/uncertainty, thrust/feed/control, integrator and error policy | Perturbed/multi-body cases, close approach, long coasts, tiny/large burns, frame changes, coupled moving contact |
| Arrival/spacecraft — SPACE/profile | Launch/entry/descent/ascent/capture envelopes, loads, heat, control/structure, site/weather, docking hardware | Vacuum versus atmosphere, no braking, failed engine, altered payload, unavailable berth, common-cause fault |
| Pressure/chemistry — SPACE/profile | Species/volume/temperature/state law, transfer/leak/vent law, storage/recovery, contamination/sensor models | Empty/isolated/connected zones, species depletion, delay to alarm, extreme pressures, recovery capacity |
| Thermal/power — SPACE/profile + Core §109 | Generation, transport/rejection, geometry/shadow, compatible thermal masses, thresholds/interlocks, output/storage limits | Peak versus steady state, simultaneous loads, loss of radiator, eclipse, startup cycles and no vacuum-convection shortcut |
| EVA/exposure — SPACE + MED/profile | Suit/environment limits, restraint/mobility, tasks, return/abort resources, exposure law and medical response | Failed return path, communication loss, damaged suit, exhausted buffer, unavailable care; no universal death timer |
| Contact/navigation — SPACE + Core §61 | Ephemeris validity, propagation, occultation, pointing/link budget, bitrate/packet/relay policy, uncertainty/correlation | Moving endpoints, long latency, out-of-order/expired/repeated commands, lost acknowledgment, windows shorter than packet |
| ISRU/ecology — profile + Core §§104/108/119 | Source composition, extraction/process chemistry, yields/waste, accepted quality, energy/heat, tooling, recurring consumables | False survey inference, impure product, depleted source, no replacement parts, competing services, biosphere limitations |
| Colony/mission continuity — Core domains/profile | Import/escape windows, demand/aging/needs, staff succession, authority, medical/industrial support | Isolation, delayed resupply, uneven capacity, demographic uncertainty, stable prosperity and ordinary autonomous life |
| Interstellar/extraordinary — setting/profile | Drive and brake law, world/crew time, endurance/continuity, communication, arrival/exit and exceptions | Relativistic validity, loss of guidance, unsupported destination, persistent automation and identity constraints |

Each profile states units, source/status, formula or qualitative bounds, assumptions, dependencies and extremes. Unknown outcome-changing values are gaps, not filler zeroes. Engineering validation, gameplay balance, AI-run reproducibility and live play require their own evidence. No universal reserve fraction, leak rate, failure frequency, ISRU yield, radiation response or numerical colony rating is introduced.

## 18. Version, finalization and prospective migration

**Release identity:** IRGS-SPACE-SLIM-0.2, 14 October 2026; derived from IRGS-SPACE-0.1, receiving `IRGS-CORE-3.2`, `IRGS-BIND-SPACE-3.2`, `IRGS-SCL-1.0`, and retained `SPACE-LIB@0.1`. This is the complete Proposed specification for that declared scope. Its authored-route and bounded analytic procedures are specified; advanced physics and biological models remain explicit activation-dependent extensions, not secretly completed implementations.

**Finalization record:** shared-provider mapping, source dispositions, specialized procedures, content payloads, records/interfaces, runtime hooks, overrides, acceptance and migration are delivered here. The generated report records checks actually executed. Specification completeness does not mean the user has accepted this engine or that any campaign/profile is calibrated or adopted. The archived earlier drafts and Core editions have no active rule authority in this submission.

For an existing campaign:

1. Preserve a recoverable snapshot of actual state, active rule/profile versions, clock, processed spans, queues, retained uncertainty, event payloads, owner references, custody, authority, commitments and recipient knowledge. Record the requested adoption scope and effective time; do not change prior resolved play.
2. Compare old shared behavior with Core v3.2 and this bridge. Preserve exact actors/assets/lots/content IDs, histories, conditions, remaining supplies, pending messages, missions and project progress. No current stock is charged again for a resolved burn or already-built habitat.
3. Map spacecraft position to the single FlightState extension only with supported frame, epoch and velocity evidence. A narrative location is not enough for a precise trajectory; retain unknowns and supported old route abstractions pending a deliberate compatible transition.
4. If an old delta-v or mission resource meter was genuinely abstract stock, document its meaning, represented scope and conversion evidence through Core §§24/109/112. Do not simultaneously charge it and reconstructed propellant. Missing conversion evidence blocks the conversion, not unrelated actual state.
5. Keep gas in its actual compartment/tank, cargo in actual transit, and people in their actual locations. Reference existing quantities from new schemas; never initialize them twice. Define thermal state meaning before mapping old heat ratings. Preserve contamination, exposure, fatigue, maintenance and ongoing biological effects.
6. Resolve exact SCL references with their immutable revisions/types/selectors/checksums. Preserve held original definitions and selected native chains. SPACE-LIB IDs remain unchanged. Added R2 proposal text creates no new installed capability and changes no readiness gate.
7. Test the relevant migrations, accounting, delays, interruption, scarcity, scale and module cases. Record known gaps and any explicitly authorized scoped exception. Keep an ongoing leg's valid rules pinned until a prospective transition can preserve its state and obligations.
8. Record the actual authority's adoption decision and effective boundary separately from publication. Until then, this remains a reviewable proposal. After adoption, old sources stay provenance; they do not provide competing shared runtime rules or silently restore rejected behavior.

**Migration impact:** ownership/provider bindings and additional required metadata may be incompatible even though the genre version increments from 0.1 to 0.2. Physical resources, identity, history and resolved consequences remain invariant. No automatic retcon, repair, replenishment, resettlement, birth, training, resurrection, government change or simulation-time advance is permitted by this release.


## 19. Core v3.2 locator index

All links below target explicit anchors in the pinned parent; they resolve to the attached v3.2 snapshot, not an unpinned latest version.

- [Core §1 — Runtime Architecture and Ownership](inputs/r2/IRGS_Core_Engine_v3_2.md#core-1)
- [Core §2 — Canon, Evidence and Scoped Corrections](inputs/r2/IRGS_Core_Engine_v3_2.md#core-2)
- [Core §3 — Campaign Isolation](inputs/r2/IRGS_Core_Engine_v3_2.md#core-3)
- [Core §4 — Player Agency](inputs/r2/IRGS_Core_Engine_v3_2.md#core-4)
- [Core §5 — Core Resolution Loop and Action Contract](inputs/r2/IRGS_Core_Engine_v3_2.md#core-5)
- [Core §6 — Default d100 Reference Adapter](inputs/r2/IRGS_Core_Engine_v3_2.md#core-6)
- [Core §7 — Advantage and Disadvantage](inputs/r2/IRGS_Core_Engine_v3_2.md#core-7)
- [Core §8 — Failure and Mixed Results](inputs/r2/IRGS_Core_Engine_v3_2.md#core-8)
- [Core §9 — Consequence Scale](inputs/r2/IRGS_Core_Engine_v3_2.md#core-9)
- [Core §10 — Time, Commitments and Concurrency](inputs/r2/IRGS_Core_Engine_v3_2.md#core-10)
- [Core §11 — Event Frontier, Scheduling and Atomic Processing](inputs/r2/IRGS_Core_Engine_v3_2.md#core-11)
- [Core §12 — Persistent Records, Accounting and Commitments](inputs/r2/IRGS_Core_Engine_v3_2.md#core-12)
- [Core §13 — Context Sensitive State Panels](inputs/r2/IRGS_Core_Engine_v3_2.md#core-13)
- [Core §14 — Actor Capability](inputs/r2/IRGS_Core_Engine_v3_2.md#core-14)
- [Core §15 — Competency Ladder](inputs/r2/IRGS_Core_Engine_v3_2.md#core-15)
- [Core §16 — Progression](inputs/r2/IRGS_Core_Engine_v3_2.md#core-16)
- [Core §17 — Conditions, Injury, Treatment and Recovery](inputs/r2/IRGS_Core_Engine_v3_2.md#core-17)
- [Core §18 — Fatigue, Exertion and Recovery Constraints](inputs/r2/IRGS_Core_Engine_v3_2.md#core-18)
- [Core §19 — Hazards, Exposure and Deprivation Interfaces](inputs/r2/IRGS_Core_Engine_v3_2.md#core-19)
- [Core §20 — Inventory, Compatibility and Access](inputs/r2/IRGS_Core_Engine_v3_2.md#core-20)
- [Core §21 — Equipment Condition, Configuration and Quality](inputs/r2/IRGS_Core_Engine_v3_2.md#core-21)
- [Core §22 — Ammunition](inputs/r2/IRGS_Core_Engine_v3_2.md#core-22)
- [Core §23 — Maintenance and Work Orders](inputs/r2/IRGS_Core_Engine_v3_2.md#core-23)
- [Core §24 — Economy, Claims and Settlement](inputs/r2/IRGS_Core_Engine_v3_2.md#core-24)
- [Core §25 — Organizations as Persistent Actors](inputs/r2/IRGS_Core_Engine_v3_2.md#core-25)
- [Core §26 — Actor Service and Career Dossiers](inputs/r2/IRGS_Core_Engine_v3_2.md#core-26)
- [Core §27 — Context-Appropriate Organization](inputs/r2/IRGS_Core_Engine_v3_2.md#core-27)
- [Core §28 — Authority, Reporting and Succession Links](inputs/r2/IRGS_Core_Engine_v3_2.md#core-28)
- [Core §29 — Orders, Requests and Delegated Execution](inputs/r2/IRGS_Core_Engine_v3_2.md#core-29)
- [Core §30 — Communications](inputs/r2/IRGS_Core_Engine_v3_2.md#core-30)
- [Core §31 — Individual and Collective Training](inputs/r2/IRGS_Core_Engine_v3_2.md#core-31)
- [Core §32 — Willingness, Cohesion, Discipline and Immediate Pressure](inputs/r2/IRGS_Core_Engine_v3_2.md#core-32)
- [Core §33 — Task-Specific Willingness and Morale](inputs/r2/IRGS_Core_Engine_v3_2.md#core-33)
- [Core §34 — Credible Threat and Exposure Restrictions](inputs/r2/IRGS_Core_Engine_v3_2.md#core-34)
- [Core §35 — Shared Logistics and Resource Flow](inputs/r2/IRGS_Core_Engine_v3_2.md#core-35)
- [Core §36 — Supply, Endurance and Planning Views](inputs/r2/IRGS_Core_Engine_v3_2.md#core-36)
- [Core §37 — Requests and Resource Authorization](inputs/r2/IRGS_Core_Engine_v3_2.md#core-37)
- [Core §38 — Service Terms, Pay and Continuing Obligations](inputs/r2/IRGS_Core_Engine_v3_2.md#core-38)
- [Core §39 — Conduct, Procedure and Accountability](inputs/r2/IRGS_Core_Engine_v3_2.md#core-39)
- [Core §40 — Institutional Findings and Remedies](inputs/r2/IRGS_Core_Engine_v3_2.md#core-40)
- [Core §41 — Task-Specific Capability and Readiness](inputs/r2/IRGS_Core_Engine_v3_2.md#core-41)
- [Core §42 — Casualties, Availability and Reporting](inputs/r2/IRGS_Core_Engine_v3_2.md#core-42)
- [Core §43 — Care Movement, Referral and Handover](inputs/r2/IRGS_Core_Engine_v3_2.md#core-43)
- [Core §44 — Staff Replacements and Integration](inputs/r2/IRGS_Core_Engine_v3_2.md#core-44)
- [Core §45 — Qualification, Appointment and Advancement](inputs/r2/IRGS_Core_Engine_v3_2.md#core-45)
- [Core §46 — Professional and Personal Relationships](inputs/r2/IRGS_Core_Engine_v3_2.md#core-46)
- [Core §47 — Spatial Conflict, Commitments and Ordering](inputs/r2/IRGS_Core_Engine_v3_2.md#core-47)
- [Core §48 — Reach, Range and Participation](inputs/r2/IRGS_Core_Engine_v3_2.md#core-48)
- [Core §49 — Cover vs Concealment](inputs/r2/IRGS_Core_Engine_v3_2.md#core-49)
- [Core §50 — Terrain](inputs/r2/IRGS_Core_Engine_v3_2.md#core-50)
- [Core §51 — Weather](inputs/r2/IRGS_Core_Engine_v3_2.md#core-51)
- [Core §52 — Spatial Arrangement and Collective Coordination](inputs/r2/IRGS_Core_Engine_v3_2.md#core-52)
- [Core §53 — Weapon and Harmful-Effect Modes](inputs/r2/IRGS_Core_Engine_v3_2.md#core-53)
- [Core §54 — Protection, Coverage and Residual Effect](inputs/r2/IRGS_Core_Engine_v3_2.md#core-54)
- [Core §55 — Assets, Vehicles and Components](inputs/r2/IRGS_Core_Engine_v3_2.md#core-55)
- [Core §56 — Specialized Platform Modules](inputs/r2/IRGS_Core_Engine_v3_2.md#core-56)
- [Core §57 — Crew, Automation and Specialized Interfaces](inputs/r2/IRGS_Core_Engine_v3_2.md#core-57)
- [Core §58 — Protected Sites and Defensive Systems](inputs/r2/IRGS_Core_Engine_v3_2.md#core-58)
- [Core §59 — Sustained Access Denial and Attrition](inputs/r2/IRGS_Core_Engine_v3_2.md#core-59)
- [Core §60 — Reconnaissance](inputs/r2/IRGS_Core_Engine_v3_2.md#core-60)
- [Core §61 — Intelligence](inputs/r2/IRGS_Core_Engine_v3_2.md#core-61)
- [Core §62 — Operations and Resolution Scales](inputs/r2/IRGS_Core_Engine_v3_2.md#core-62)
- [Core §63 — After Action Report](inputs/r2/IRGS_Core_Engine_v3_2.md#core-63)
- [Core §64 — Autonomous Actors and Off-Screen Work](inputs/r2/IRGS_Core_Engine_v3_2.md#core-64)
- [Core §65 — Faction Simulation](inputs/r2/IRGS_Core_Engine_v3_2.md#core-65)
- [Core §66 — Social Resolution, Relationships and Reputation](inputs/r2/IRGS_Core_Engine_v3_2.md#core-66)
- [Core §67 — Romance](inputs/r2/IRGS_Core_Engine_v3_2.md#core-67)
- [Core §68 — Households, Property and Care](inputs/r2/IRGS_Core_Engine_v3_2.md#core-68)
- [Core §69 — Succession and Generational Continuity](inputs/r2/IRGS_Core_Engine_v3_2.md#core-69)
- [Core §70 — Death](inputs/r2/IRGS_Core_Engine_v3_2.md#core-70)
- [Core §71 — Needs, Provision and Continuity Forecasts](inputs/r2/IRGS_Core_Engine_v3_2.md#core-71)
- [Core §72 — Settlement and Community Services](inputs/r2/IRGS_Core_Engine_v3_2.md#core-72)
- [Core §73 — Projects, Programs, Production and R&D](inputs/r2/IRGS_Core_Engine_v3_2.md#core-73)
- [Core §74 — Technology Development and Diffusion](inputs/r2/IRGS_Core_Engine_v3_2.md#core-74)
- [Core §75 — Enemy Adaptation](inputs/r2/IRGS_Core_Engine_v3_2.md#core-75)
- [Core §76 — Ordinary Life and Careers](inputs/r2/IRGS_Core_Engine_v3_2.md#core-76)
- [Core §77 — Attribute and Progression Profiles](inputs/r2/IRGS_Core_Engine_v3_2.md#core-77)
- [Core §78 — Objectives](inputs/r2/IRGS_Core_Engine_v3_2.md#core-78)
- [Core §79 — Discovery and Bounded Establishment of World Facts](inputs/r2/IRGS_Core_Engine_v3_2.md#core-79)
- [Core §80 — Choice Presentation](inputs/r2/IRGS_Core_Engine_v3_2.md#core-80)
- [Core §81 — Response Pacing](inputs/r2/IRGS_Core_Engine_v3_2.md#core-81)
- [Core §82 — Design, OOC and Simulation Boundaries](inputs/r2/IRGS_Core_Engine_v3_2.md#core-82)
- [Core §83 — Strategic Player Orders](inputs/r2/IRGS_Core_Engine_v3_2.md#core-83)
- [Core §84 — Parallel Operations](inputs/r2/IRGS_Core_Engine_v3_2.md#core-84)
- [Core §85 — Information Delay](inputs/r2/IRGS_Core_Engine_v3_2.md#core-85)
- [Core §86 — Hidden State](inputs/r2/IRGS_Core_Engine_v3_2.md#core-86)
- [Core §87 — World Consequences](inputs/r2/IRGS_Core_Engine_v3_2.md#core-87)
- [Core §88 — Campaign Initialization](inputs/r2/IRGS_Core_Engine_v3_2.md#core-88)
- [Core §89 — Scene Initialization](inputs/r2/IRGS_Core_Engine_v3_2.md#core-89)
- [Core §90 — One Shared Runtime Procedure](inputs/r2/IRGS_Core_Engine_v3_2.md#core-90)
- [Core §91 — Event Commit and Derived Updates](inputs/r2/IRGS_Core_Engine_v3_2.md#core-91)
- [Core §92 — Anti Railroad Rule](inputs/r2/IRGS_Core_Engine_v3_2.md#core-92)
- [Core §93 — Anti Escalation Rule](inputs/r2/IRGS_Core_Engine_v3_2.md#core-93)
- [Core §94 — Anti Protagonist Centrism](inputs/r2/IRGS_Core_Engine_v3_2.md#core-94)
- [Core §95 — Aftermath Rule](inputs/r2/IRGS_Core_Engine_v3_2.md#core-95)
- [Core §96 — Downtime, Development and Reviews](inputs/r2/IRGS_Core_Engine_v3_2.md#core-96)
- [Core §97 — Campaign Overrides and Prospective Migration](inputs/r2/IRGS_Core_Engine_v3_2.md#core-97)
- [Core §98 — Presentation Adapters and Randomness](inputs/r2/IRGS_Core_Engine_v3_2.md#core-98)
- [Core §99 — Corrections, Reversals and History Recovery](inputs/r2/IRGS_Core_Engine_v3_2.md#core-99)
- [Core §100 — Master Game-Running Principle](inputs/r2/IRGS_Core_Engine_v3_2.md#core-100)
- [Core §101 — Dependencies, Buffers, Redundancy and Substitution](inputs/r2/IRGS_Core_Engine_v3_2.md#core-101)
- [Core §102 — Networks, Routes and Concurrent Flows](inputs/r2/IRGS_Core_Engine_v3_2.md#core-102)
- [Core §103 — Infrastructure Services, Startup and Commissioning](inputs/r2/IRGS_Core_Engine_v3_2.md#core-103)
- [Core §104 — Sites, Discovery, Recovery and Resource Sources](inputs/r2/IRGS_Core_Engine_v3_2.md#core-104)
- [Core §105 — Containers, Handling, Carrying and Storage](inputs/r2/IRGS_Core_Engine_v3_2.md#core-105)
- [Core §106 — Population, Presence, Movement and Membership](inputs/r2/IRGS_Core_Engine_v3_2.md#core-106)
- [Core §107 — Institutional Functions, Authority and Continuity](inputs/r2/IRGS_Core_Engine_v3_2.md#core-107)
- [Core §108 — Technology Support and Productive Capability](inputs/r2/IRGS_Core_Engine_v3_2.md#core-108)
- [Core §109 — Operating Stocks, Rates, Power and Bounded Burdens](inputs/r2/IRGS_Core_Engine_v3_2.md#core-109)
- [Core §110 — Institutional Learning, Revision and Fielding](inputs/r2/IRGS_Core_Engine_v3_2.md#core-110)
- [Core §111 — Content Identity, Composition, Binding and Instances](inputs/r2/IRGS_Core_Engine_v3_2.md#core-111)
- [Core §112 — Module Contracts, Compatibility and Adoption](inputs/r2/IRGS_Core_Engine_v3_2.md#core-112)
- [Core §113 — GOV — Political/Government](inputs/r2/IRGS_Core_Engine_v3_2.md#core-113)
- [Core §114 — ECO — Business/Economic](inputs/r2/IRGS_Core_Engine_v3_2.md#core-114)
- [Core §115 — INV — Crime/Investigation](inputs/r2/IRGS_Core_Engine_v3_2.md#core-115)
- [Core §116 — MAR — Maritime/Naval](inputs/r2/IRGS_Core_Engine_v3_2.md#core-116)
- [Core §117 — CIV — Civilization & Grand Strategy](inputs/r2/IRGS_Core_Engine_v3_2.md#core-117)
- [Core §118 — MED — Medical/EMS](inputs/r2/IRGS_Core_Engine_v3_2.md#core-118)
- [Core §119 — WILD — Wilderness/Ecological](inputs/r2/IRGS_Core_Engine_v3_2.md#core-119)
- [Core §120 — INTEL — Espionage/Intelligence](inputs/r2/IRGS_Core_Engine_v3_2.md#core-120)
- [Core §121 — URBAN — Urban/City Development and Management](inputs/r2/IRGS_Core_Engine_v3_2.md#core-121)
- [Core §122 — LIFE — Social/Generational/Life](inputs/r2/IRGS_Core_Engine_v3_2.md#core-122)
- [Core §123 — COMP — Competitions](inputs/r2/IRGS_Core_Engine_v3_2.md#core-123)
