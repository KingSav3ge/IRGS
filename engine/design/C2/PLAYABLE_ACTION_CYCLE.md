# 3.3.C — Playable action cycle and integrated fixture

**Design edition:** C2 · 20 October 2026  
**Status:** Proposed specification for Claude implementation  
**Purpose:** Connect the separate action contracts into one consequential Solo sequence on a single world.

This document specifies what a supported ordinary first interaction must do. It is not a scripted campaign opening or a claim that the current runtime can perform this sequence. The accompanying `fixtures/PLAYABLE_CYCLE.json` is design data for implementation tests, not executable code.

## 1. Execution sequence

Use the same request and outcome path for player and NPC actions:

**Declare → Select method → Validate → Reach next causal boundary → Resolve actual effects → Persist → Deliver information → Present → Continue or return a material decision.**

An interpretation proposes a method, target and authorized limits. Routine wording does not require a questionnaire. A materially different destination, expense, risk, concession or commitment returns for a player choice. Unsupported methods remain unresolved with their actual reason.

Each request retains its original intention. Each physical, communication or work phase has a distinct attempt, applicable model and durable receipt. Completed phases can leave a parent objective open. A pending request's replay retrieves its acknowledgement; it does not launch its next phase. A separately authorized continuation uses a new attempt identity and current revision.

Advance only to the next supported boundary. A broad instruction cannot skip a closure, shared-capacity conflict, safety interruption or new voluntary concession. Save management and presentation are not additional phases of simulated labour or travel.

## 2. Completion and effect boundaries

| Phase | Actual result needed | What it does not establish |
| --- | --- | --- |
| Notice observation | A bounded observation and legitimate receipt of accessible content. | Truth of every statement, a job, or knowledge of hidden people and stock. |
| Movement | Supported departure/transit/arrival or a real local positional change. | Teleportation, automatic companionship, or an invented speed. |
| Question | Actual utterance and the identified receipt/comprehension scope. | A useful answer or a successful negotiation. |
| Offer | Proposed terms actually communicated by the offering party. | Player assent, employment, payment or performed work. |
| Agreement | Qualified actual assents to the same terms, with necessary authority and conditions. | Completed duties, an earned balance or a wider institutional mandate. |
| Work booking | Real actor/site commitment and permitted backing. | Useful progress, consumed inputs, output or wages. |
| Work milestone | Actual useful work and its supported physical/input effects. | Unperformed remainder or automatic acceptance. |
| Interruption | Settled earlier effects, stopped future portions and an explicit continuation requirement. | Erasure of progress, automatic return home or silent assent to new terms. |
| Acceptance and settlement | Actual acceptance, claim basis and funded payment through their respective owners. | Duplicate output, a second monetary balance or a retrospective replay of work. |

The current Core operations are implementation references. New spatial, communication, timing and staged-work adapters are required for this full sequence. Do not substitute generic stamina deductions, scene descriptions or a `resolved` label for these effects.

## 3. Synthetic fixture and selected parameters

Every person, location, quantity, duration and procedure here is an explicit test-fixture selection. None is a historical assertion or a default for ordinary IRGS campaigns.

| Component | Fixture selection |
| --- | --- |
| Timeline | Elapsed minutes from synthetic origin `T=0`; civil-calendar conversion remains unbound. |
| Places | Yard, Stores, a traversable path between them, and one sorting bay within Stores. |
| Actors | Controlled person P; foreman F; worker W. Each is one actual actor in the shared world. F has the separately established capability to inspect this parcel task. |
| Capability | P has established ordinary walking, hearing, speech and reading of the posted language. These are separately selected qualitative functions, not numeric ratings or a template gift to real characters. |
| Information | P initially knows only the permitted local scene. F has actually received the hiring, safety, inspection/acceptance, scoped payment and capacity-allocation mandates and relevant work reports. W's job and availability are actual records. |
| Goods and funds | Four workshop-owned parcels on shelf A, none on shelf B. Workshop cash three units; P cash zero. F has actual access to the workshop funds and authority to settle this accepted task up to three units. Title/custody remain explicit; no second cash representation is added. |
| Public notice | Accessible text says that work inquiries can be made at Stores. Its observation supplies that assertion, not a guarantee of work. |
| Work terms | Relocate the four parcels from A to B; three cash units become due only after all four are relocated and accepted. No partial wage is owed under this particular fixture agreement. |
| Work model | One parcel milestone per qualifying minute; input parcel is relocated, not consumed or manufactured. Shared bay capacity is one worker. |
| Allocation | F has a selected earliest-due-task procedure at allocation reviews T=8, T=11 and T=15. P's accepted job is due at T=14. W's qualified task needs four contiguous bay minutes and is due at T=20. W requests once and waits for allocation after deferral; no policy automatically starts W between reviews. Equal deadlines would require an additional qualified decision; identifiers are not a tie-breaker. |
| Interruption | The accepted work scope includes a stop-on-safety-signal condition. A real signal reaches the bay at T=10 and closes the bay to both workers for [10,11). A qualified clearance is received at T=11. Continuation requires a player decision. |
| Decision pause | Simulation pauses at material player decisions. New bounded advance/continuation requests resume it. Host-clock delay while a decision is pending changes no expected fixture time. |

The fixture selects observation duration one minute, path duration four minutes, and separate question, offer and acceptance communication phases of one minute each. Completion inspection and cash handover each use one minute. These values exist only to make the fixture's expected boundaries explicit.

## 4. Required trace

| Boundary/span | Cause and required shared-world result |
| --- | --- |
| T=0 setup | P exists under actual control before play. No work agreement, earned pay or private foreman knowledge is granted. |
| [0,1) | P deliberately reads the accessible notice. At T=1 its content and source are received. The notice's claim remains distinct from institutional truth. |
| [1,5) | P walks to Stores using the selected route. Actual presence moves from origin to transit and then destination. A save at T=3 records transit, not arrival or a second person. |
| [5,6) | P asks the person at the work counter about available work. F actually receives the question. The player's knowledge is limited to observable introduction and received speech. |
| [6,7) | F's qualified policy offers the recorded parcel-work terms. P receives the offer. Cash and employment remain unchanged. |
| [7,8) | P expressly accepts those exact terms. Qualified agreement forms. It permits this task, not general access to workshop property or command over W. |
| T=8 frontier | P and W request the same sorting bay. The engine first detects contention. F's actual authorized allocation decision applies the selected deadline procedure to book P for [8,12); W remains unfulfilled. No array ordering selects P. |
| [8,10) | P performs two actual parcel milestones. A has two parcels and B has two; total remains four. The bay and P's attention are committed. No pay is due yet. |
| T=10 interruption | Settle valid work over the preceding half-open span and the newly effective stop condition in one qualified boundary transaction. No third parcel starts. Preserve two units of useful work and all physical relocations. Release the unperformed booking [10,12); actual bay closure prevents either worker starting during [10,11). Return the continuation decision. |
| [10,11) | In this trace, P chooses a bounded wait. F's actual safety process produces the clearance and P receives it at T=11. Receipt alone does not choose to resume. |
| [11,13) | P chooses a new continuation attempt under unchanged task terms. Revalidate clearance, P, the bay and backing. At the T=11 allocation review, W has not begun or obtained a booking; the selected deadline policy grants P a new [11,13) booking. Complete the remaining two parcel milestones. A has zero, B four. W's unfulfilled task remains pending for the T=15 review. No running W task is preempted or erased. |
| [13,14) | F performs qualified completion inspection and accepts the actual work. The agreement's three-unit claim becomes due once. Physical cash remains with the workshop. |
| [14,15) | A funded, authorized cash handover settles the claim. Workshop cash becomes zero, P cash three, and the same claim is settled. No additional wage award occurs because the story is displayed. |

The T=10 ordering is part of this explicitly selected process model: the valid `[8,10)` span is settled jointly with the stop condition effective at its boundary. It is not a general permission to order simultaneous operations by identifier. An uncertain signal interval overlapping a parcel's milestone would require a qualified joint resolution or an unresolved ordering case.

F's actual schedule supports the stated exchanges, safety communication, inspection and payment without an exclusive-attention overlap. Allocation decisions use the selected review procedure; required communications are actual supported receipts, not changes granted by reading a result panel. P's work request authorizes flexible booking within its accepted task window, so a new valid phase can use [11,13) without rewriting the original declaration. W's remaining task is preserved; the fixture ends at T=15 before executing its next allocation review.

The initial work horizon is interrupted at T=10. It cannot report that T=15 was reached. The later bounded wait, continuation, inspection and settlement require their own authorized stages. A player-decision pause follows the selected time-control policy; time spent looking at the interface does not simulate a wait.

## 5. Observable and private outcomes

Core retains the actual parcels, work, mandate and payment records. P receives only the notice, its journey/observable circumstances, actual exchange, safety messages and applicable work/payment information. W's private thoughts, F's hidden reports and unrelated inventory are not automatically exposed.

Detailed internal reasons may identify hidden prerequisites. The player projection must not turn them into free information. An unauthorized proposal is retained internally with its appropriate status; the public explanation reports only what the character can know or what an out-of-world service must communicate without revealing hidden facts.

Each presented scene references committed phase effects and permitted information. A failed narrator can be retried from those references. It cannot produce another utterance, parcel movement, payment or time advance. A late report of payment creates receipt then; it does not transfer cash again.

## 6. Proposed integrated acceptance cases

| ID | Setup or action | Required assertion |
| --- | --- | --- |
| IC-01 | Initialize the fixture before play | One controlled P; no invented past work, agreement, earnings or private knowledge. |
| IC-02 | Read the notice | Exactly one qualified observation/receipt; no automatic job or global fact disclosure. |
| IC-03 | Save/reload at T=3 during movement | P remains one actor in transit; resume retains the original journey's progress and arrival condition. |
| IC-04 | Ask F about work at Stores | Real question receipt precedes the response; successful asking does not imply useful employment. |
| IC-05 | F offers the valid terms | Offer is recorded and received; no acceptance, cash change or work begins. |
| IC-06 | P accepts the exact terms | One qualified agreement and scoped task permission; no output, earned claim or wider authority. |
| IC-07 | P and W contend for the bay | Conflict is observed before a recorded authorized allocation using due times; changing IDs changes no outcome. |
| IC-08 | Safety stop at T=10 | A=2, B=2, progress=2 of 4; no third parcel, payment, erased work or automatic continuation. |
| IC-09 | Clearance arrives, then P chooses continuation | Receipt does not resume by itself; the new attempt revalidates and settles only the remaining two parcels. |
| IC-10 | Completion, inspection and payment | Work complete before acceptance; due claim before payment; final cash totals conserved at three and parcel total at four. |
| IC-11 | Retry any committed phase or lose its presentation | Same historical phase receipt; no duplicate speech, work, claim, payment or elapsed span. |
| IC-12 | Request coarse advance instead of short reviews | Preserve T=8 contention, T=10 stop, later player choices and the same actual effects; no coarse-step bypass. |

These twelve cases supplement the separate movement, dialogue, time and foundation cases. Passing the integrated fixture would demonstrate these selected mechanisms, not general employment, historical calibration or a complete Living Day.
