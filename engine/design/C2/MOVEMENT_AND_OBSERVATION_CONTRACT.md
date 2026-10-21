# 3.3.C — Movement and observation contract

**Edition:** C2 · 20 October 2026  
**Status:** Proposed engine design for Claude implementation; acceptance cases are not executed results.  
**Foundation:** Selected Core 3.3, the Engine Supplement's lifecycle and the C1 action, dependency and persistence contracts.

This contract develops ordinary movement and observation into consequential actions on the shared world. It prescribes no universal speed, perception score, probability or action duration. Existing `CoreWorld.apply`, temporal identities, evidence/receipt records and the R9 observer/frontier are implementation foundations. The movement, spatial and sensory procedures below are extensions to implement and qualify, not claims about existing handlers.

## 1. Owners and minimum records

K-ACTOR owns an individual's actual position, conditions and availability. K-NET owns route access, operating capacity and actual passage/delivery. K-TIME owns commitments, elapsed-process boundaries and causal order. K-INFO owns observations, claims, search results and receipt. K-ASSET and K-STOCK retain vehicle/object condition, title, custody and contents; movement references them. K-ORG owns relevant mandates, while existing domain owners retain legal decisions. No new map or perception subsystem becomes another world authority.

| Logical record | Required meanings |
| --- | --- |
| SpatialPosition | Actor; place reference; supported local position or relation; precision; effective interval; cause event. Unknown coordinates remain unknown. |
| MovementSelection | Original request/actor; origin constraint; destination or bounded spatial objective; method; path/route basis; companions or conveyance; authorized limits; timing/model references; stop conditions. |
| TransitProcess | Request/phase; departure event; actual route segment or supported transit relation; last settled progress; current restrictions; next boundary; arrival condition; commitments and capacity references. |
| ObservationSelection | Observer; question or phenomenon; method/sense; bounded spatial/content scope; attention and access; time opportunity; selected procedure; retained-result references. |
| ObservationRecord | Observation identity; observer; actual occurrence and collection coordinates; accessible content; method and source lineage; uncertainty/coverage; related evidence; observer receipt reference. |
| SearchResult | Search scope/method; relevant world and observer dependencies; examined coverage; positive findings or qualified absence; unresolved remainder; prior-result/supersession references. |

These are logical meanings, not mandatory database tables. Current-position projections refer to authoritative position history; transit and a displayed map cannot maintain independent copies of where an actor is.

## 2. Selecting ordinary movement

Interpret the exact declaration into the material objective, method and voluntary limits. “Walk to the nearby doorway” can use an established local relation without invented coordinates or a route-planning questionnaire. Clarify only ambiguities that would materially change the chosen action, exposure, expenditure, authority or destination. Do not silently substitute a distant destination sharing the same name.

Check current existence and control, actual origin, relevant bodily/custody restrictions, route feasibility and any needed access or means. Routine established walking on suitable ground requires neither an agility number nor a success roll. An unmeasured exceptional load, inaccessible boat or unsupported hazardous crossing is a different feasibility problem. Missing incidental detail does not invalidate an otherwise established ordinary capability.

Distinguish physical possibility, legal permission, mandate and the actor's knowledge. A rule requiring institutional authorization must validate it. A physically possible prohibited movement may instead be an attempted breach under a qualified procedure; lack of legal permission does not make a wall appear. Record any genuine player choice before a new unlawful or materially riskier method. Unknown guard behaviour cannot be resolved by assuming automatic passage or automatic capture.

## 3. Position, transit and completion

A place identifier may represent a settlement, room or other coarse scope. Local movement can keep that identifier while changing an actual supported position, such as “beside the west doorway.” It must record a real positional effect and its cause; deducting stamina and retaining unchanged position is not successful movement. Descriptions cannot invent a surveyed distance or geometry.

A journey outside the current local scope distinguishes departure, transit and arrival. After departure, the actor has one actual transit position or relation, not simultaneous presence at both endpoints. Being aboard a moving vehicle references that actual conveyance and its route; it creates no duplicate vehicle, actor or cargo. Companions remain their own actors with their own control, capability and commitments. One player's instruction does not command an unrelated person to accompany them.

Bind elapsed movement to a selected timing procedure and its actual units, precision and conditions. Coarse or bounded timing is valid where adequate. Temporal completion at supported precision is allowed when that procedure establishes it without choosing among unresolved intervening events. Where a duration range overlaps a material deadline, threat, closure or capacity change, refine the relevant uncertainty or hold that stage; do not invent an exact speed, assign zero time or choose a convenient endpoint. Causal sequence increments are not duration.

`scheduled` means a permitted future journey or commitment exists. `in_progress` requires actual departure. `completed_successfully` requires the stated spatial completion condition. An interrupted journey retains its actual transit position, settled progress, elapsed interval and real costs. Fractions require a selected progress model; otherwise retain a supported segment/position, not a fabricated percentage. A return journey requires its own feasible continuation; cancellation cannot teleport the actor home.

## 4. Observation and search

Observation reads actual accessible phenomena at the observation opportunity. Check observer presence, relevant sensory capability/condition, attention, obstruction, medium and actual method. Qualitative evidence can establish ordinary visibility or audibility without exact coordinates or numerical ranges. Darkness, distance or concealment matters only through supported applicable circumstances; do not impose an invented universal penalty.

An observation creates a bounded K-INFO record and legitimate receipt for the actual observer. It does not expose every actor, global fact or hidden component in the encompassing place. Other witnesses receive only what their own opportunities support. Store world truth, collected content and interpretation separately. Seeing a uniform may support “a person wearing that uniform,” not identity, loyalty or lawful office. Hearing an announcement establishes received speech, not the truth or legal effect of its contents. Institutional validity requires its actual owner-qualified basis.

An investigation may combine earlier received information, accessible evidence and actual search actions. A question does not grant access to private records or to another NPC's memory. Necessary missing information can yield `awaiting_information`; a missing applicable procedure can yield `awaiting_selected_rule`; an unperformed search is not a negative finding. A completed search can legitimately find nothing within its examined scope without proving universal absence.

Retain the result and dependencies of a completed search. Retrying or redisplaying the same accepted phase reuses its result and receipt; it creates no new generation chance, findings or elapsed work. Deliberately performing another physical search is a new action and uses its actual attention and supported duration even when the finding remains unchanged. Repetition cannot regenerate established stock or silently resample the same retained uncertainty. A genuinely new opportunity, changed object position, different supported method or additional coverage can justify new findings under the selected procedure. Changes to unrelated world records do not invalidate the search automatically. Retained results describe their original observation time; stale knowledge does not silently become current truth.

Where authorized bounded world generation is needed, refine only permitted unestablished detail and retain that choice once. Existing hidden authoritative state takes precedence over generation. Never generate the player's motives, prior voluntary actions or an extra person to satisfy a search. A record saying “unknown” is not a pool of free objects.

## 5. Dependencies, outcomes and persistence

Instrument selection-sensitive authorization, physical feasibility, observation opportunity and effects together. Actual reads include origin/position, actor restrictions, route state, negative access lookups, shared capacity, selected timing/sensory rules, examined objects and retained search results. Capture predicate scope when a decision depends on “no other occupant” or “no matching object”; observing one returned record alone is insufficient.

At a common frontier, movement can conflict with confinement, doorway closure or allocation of the same passage. Observation can conflict with movement of its target or a change in visibility. Determine actual causal ordering or retain the material conflict; identifier order cannot decide what was seen. A later report of an already committed journey does not reapply movement. Observing an independently established physical occurrence cannot administratively veto that occurrence.

Commit each actual movement stage, observation/receipt, outcome and durable attempt receipt atomically or under the qualified staged protocol. A completed observation phase can leave its parent investigation open. Retry returns that phase's receipt; later coverage uses a new phase/attempt identity. On interruption, save/reload or restoration, preserve the C1 lineage and pending-work reconciliation rules. Presentation receives the actual spatial result and permitted observations after commitment, including unresolved remainder; prose supplies no additional travel or discovery.

## 6. Proposed acceptance cases

All identities, geometry and conditions below are explicitly selected fixtures. No historical measurements are implied.

| ID | Preconditions and attempted action | Required owner-qualified result |
| --- | --- | --- |
| MO-01 | Healthy controlled actor; nearby accessible doorway; no agility field; walk there | Ordinary movement succeeds without invented score/roll; K-ACTOR records supported local position. |
| MO-02 | Both endpoints share a coarse room ID; move beside the west doorway | Coarse ID may remain; actual positional relation changes once and outcome identifies it. |
| MO-03 | Two distant places have the same label; target is materially ambiguous | Await clarification; no chosen destination, departure or invented expense. |
| MO-04 | Actual accessible route and selected duration; travel between settlements | Departure, single transit presence and later arrival persist; no early destination presence. |
| MO-05 | A material closure falls inside the journey's duration range | Refine timing or hold the affected stage; no convenient endpoint or inferred zero duration. |
| MO-06 | Journey departs, then supported obstruction interrupts it | Preserve actual progress/position, elapsed span and settled costs; arrival remains uncompleted. |
| MO-07 | Cancel an interrupted journey away from origin | Release permitted future commitments; actor stays at actual position until a real continuation moves them. |
| MO-08 | Actor lacks physical access to a required conveyance | Await prerequisite or valid alternative choice; title alone creates no accessible vehicle. |
| MO-09 | Movement and closure/confinement change share a frontier | Actual dependencies conflict; no request-ID passage winner or unexplained escape. |
| MO-10 | Two independent routes and actors; valid movement stages | Equivalent domain effects under either execution order, or an explicitly disclosed conservative barrier. |
| MO-11 | Visible local object; sufficient qualitative scene evidence; no exact coordinates | Observation records accessible content and observer receipt without demanding fictitious geometry. |
| MO-12 | Unmet remote NPC and private inventory exist in the same campaign | Local observation exposes neither private state nor remote location through a global registry view. |
| MO-13 | Observer hears an official-sounding announcement | K-INFO records speaker/content and actual receipt; assertion does not itself establish legal authority or truth. |
| MO-14 | Qualified search examines one cabinet and finds no key | Retain scoped negative result; unopened rooms and unknown compartments remain unresolved. |
| MO-15 | Retry the accepted MO-14 phase, then deliberately request a new physical search under unchanged relevant circumstances | Retry causes no new effects; the new action can use supported time/attention but cannot regenerate stock or automatically resample retained uncertainty. |
| MO-16 | A key is actually placed in that cabinet after MO-14 | New qualified attempt can find it; preserve earlier correct scoped absence and later receipt. |
| MO-17 | Hidden existing stock and authorized bounded generation both apply | Use established hidden stock; generation neither duplicates it nor replaces it because the player is unaware. |
| MO-18 | Crash/retry after a movement or observation phase commits | Recover the same phase receipt and effects once; later phase has a new identity; no extra travel, discovery or receipt. |

Claude must supply actual access traces, ordinary/instrumented parity, relevant same-frontier cases and durable before/after evidence. These 18 cases define required implementation evidence, not a claim that the current engine implements movement or observation.
