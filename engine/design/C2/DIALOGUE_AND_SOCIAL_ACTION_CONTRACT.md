# 3.3.C — Dialogue and social action contract

**Edition:** C2 · 20 October 2026  
**Status:** Proposed engine design for Claude implementation. Selected Core 3.3 remains authoritative. The cases below are requirements, not executed tests.

This contract develops ordinary speaking, questions, NPC responses, persuasion and agreements. It uses the supplement's lifecycle, immutable intentions, separate attempt/phase receipts and persistence rules. Dialogue operates in the same world as work, travel and institutions. It creates no independent social simulation or presentation-owned facts.

## 1. Distinct events and owners

Keep the following meanings separate:

| Meaning | Authoritative result |
| --- | --- |
| Intention | The speaker's exact declaration and authorized scope are retained. |
| Proposed utterance | Wording or a bounded communicative objective awaits ordinary Core validation. |
| Production | The actor actually speaks, signs, writes or otherwise produces the communication through supported means. |
| Transmission | Sound, gesture, a document or another channel reaches an actual place or recipient under its conditions. |
| Receipt | A particular actor receives the accessible content, possibly only part of it. |
| Comprehension | The recipient understands a supported meaning; receipt alone does not establish this. |
| Response or undertaking | A separate actor makes a decision or commitment within actual capability and authority. |
| Presentation | An authorized account describes those committed events and the viewer's legitimately available information. |

K-ACTOR owns speakers, listeners, relevant capability, location and condition. K-INFO owns assertions, communicated content, source lineage, receipts and beliefs. K-TIME owns sequencing and commitments; K-NET owns an applicable delivery channel and capacity. Identified documents retain K-ASSET/K-STOCK custody. K-ORG, ECO and GOV retain their respective authority, agreement and public-decision records. A transcript references these events; it is not another authoritative history.

`completed_successfully` must identify the phase and completion condition. Successfully asking a question means its qualified utterance and intended receipt occurred; it does not mean an answer was obtained. An unanswered inquiry can have a completed communication phase and an unresolved parent objective.

## 2. Logical records for implementation

These are semantic requirements, not prescribed database tables or existing handler names.

| Record | Required meanings |
| --- | --- |
| CommunicationSelection | Request/actor; exact supplied words or bounded objective; intended recipients; method/channel; language or sign system; permitted disclosure; duration/attention limits; stop conditions; selected adapter edition. |
| UtteranceOccurrence | Scoped event and attempt/phase identities; actual speaker; produced content; method; supported occurrence interval and precision; causal parents; source references. |
| CommunicationReceipt | Scoped recipient; originating occurrence; received fragments/content references; receipt time/precision; channel; comprehension status and supported meaning; uncertainty and source status. |
| DialogueDecision | Acting NPC and policy edition; received inputs; actual goals/obligations; proposed response or explicit nonresponse; explanation separated from world facts. |
| SocialProposal | Offer/request/promise type; parties; exact terms and conditions; required authority/assent; expiry or unresolved timing; backing references; supersession links. |
| AgreementEvent | Actual assents and their receipt references; qualified terms edition; authority basis; resulting agreement/obligation references; outstanding conditions. |

Preserve exact supplied dialogue separately from an interpretation. If the player says only “ask the guard about work,” a selected procedure may express that bounded inquiry. It cannot add a claimed military service history, promise payment, reveal a secret or accept employment. Material ambiguity requiring such a choice produces `awaiting_clarification`; routine wording needs no needless player interruption.

Ordinary established speech and hearing do not require invented numerical statistics. Speaking, understanding speech, reading, writing and copying are different functions. Literacy does not follow from conversational fluency. Missing a numerical rating is not evidence of muteness or incomprehension; a relevant actual restriction or uncertainty still needs its supported procedure.

## 3. Production, receipt and answers

Validate the actor's current existence and control, available method, actual audience/channel, attention conflicts and supported conditions inside the observed execution path. Resolve actual production and transmission before recording who heard or understood it. An intended recipient absent from the channel receives nothing. Co-location alone need not imply hearing every word: distance, barriers, noise, attention and method matter where consequential.

Each legitimate listener, including an incidental bystander, receives only the accessible content. A bystander does not inherit the intended recipient's private knowledge. Hearing a claim establishes that the speaker made that claim; it does not establish the claim's truth. Information-time and occurrence-time precision remain explicit.

An NPC response is an ordinary agency proposal based on that NPC's received information, supported memories, goals, obligations and current circumstances. It passes through Core before becoming a spoken occurrence. The NPC can answer, ask a question, refuse, remain silent, defer, give an estimate or make an offer. A missing relevant fact is not permission to invent an authoritative answer.

An NPC can make a mistaken statement or deliberately deceive where its actual selected decision supports that behaviour. Retain assertion, belief, evidence and any private intention separately. An unknown world fact remains unknown even if the statement is confident. Presentation may report the words and supported observable behaviour; it cannot announce hidden sincerity, truth or deception merely because internal validation knows them.

Completed utterances and received answers survive replay without regeneration. A new genuine question can cause a new NPC decision under changed or continuing circumstances, but a repeated query of the same recorded exchange cannot reroll an answer or establish fresh hidden facts. Authorized world refinement follows the retained-generation rules rather than inventing content because a conversation needs it.

## 4. Persuasion, promises and agreements

Persuasion identifies its actual requested change, interlocutor, arguments, means and applicable qualitative or selected contested procedure. A positive result may establish willingness, an immediate concession or a genuine undertaking within its resolved scope. It does not grant impossible ability, property, legal authority or the recipient's unsupported knowledge. Retain the actual decision and relevant uncertainty instead of converting all social interaction into a universal score.

An NPC's persuasive appeal cannot choose the player's voluntary response. A supported change in what the player character perceives or suffers is different from an invented assent. An authorized player's standing delegation may cover routine decisions only within its recorded scope and limits.

Distinguish an offered term, claimed promise, genuine undertaking, accepted agreement, due obligation and actual fulfilment. A genuine resolved undertaking must not later be relabelled deceptive merely to cancel success. Changed circumstances may prevent fulfilment, producing an actual shortfall and any qualified remedy. Institutional validity remains separate from the parties' beliefs and personal willingness.

When a response offers narrower service, a new price or another voluntary concession, retain those terms and return the new decision to the player. Do not deduct funds or insert acceptance. Once exact terms receive all required genuine assent and authority, a qualified agreement may form immediately; no artificial extra success roll is required. Its future performance, wages, delivery or appointment still need their own causes.

### Work inquiry trace

The player asks an actual foreman whether work is available. The foreman hears and understands the inquiry. Its policy consults received staffing information and actual hiring authority, then proposes an offer using an existing terms record. Core records that offer, not employment.

The player receives the offer and chooses whether to accept its exact terms. If required assent, authority and conditions are satisfied, Core records the agreement once. A valid future work booking can become `scheduled`; completed labour and wages earned remain unestablished. If the foreman can only seek approval, its genuine undertaking is to request that approval, with the employer's decision still unresolved. Neither path grants rank, equipment or an invented career history.

## 5. Time, interruption and dependency evidence

Conversation uses actual attention and the selected timeline/communication model. No fixed turn duration, thirty-minute action or unlimited speech within a frozen world is adopted. A coarse occurrence interval may be sufficient; exact ordering remains unresolved when its precision cannot establish which event happened first. Without adequate timing support, do not advance duration-dependent stages or fabricate an exact receipt hour.

While actors converse, independent qualified work, travel, messages and institutional processes continue through the shared scheduler. A meaningful interruption splits the exchange. Preserve words actually produced, fragments actually heard, agreed terms and real elapsed commitments. Cancel only the unperformed remainder; interrupted delivery cannot erase earlier receipt or guarantee receipt of unsent content.

A delayed letter or messenger uses actual production, custody, dispatch, transit and delivery. The intended addressee cannot act on its content before receipt. Reading and understanding are separately supported functions. Delivery cannot execute the requested order automatically.

Observe actual actor/control, audience, channel, capability, attention, mandate, terms and information dependencies together. A conversation can conflict with simultaneous departure, exclusive work, revoked hiring authority or changed offer terms. Retain unresolved allocation or ordering instead of choosing by request ID. Public reasons and projections must omit hidden facts; preserve a detailed internal cause under its legitimate access scope and provide the actor only the consequence or blocker it can know.

## 6. Proposed acceptance cases

All people, terms and channels below are explicit test fixtures.

| ID | Preconditions and request | Required outcome |
| --- | --- | --- |
| DS-01 | Capable co-present speaker/listener; ask a plain question | Record production, receipt and supported comprehension; no automatic answer. |
| DS-02 | Intended listener is elsewhere; ordinary quiet speech | No remote receipt or invented reply; actual spoken occurrence can remain recorded. |
| DS-03 | Shared spoken language, no established literacy; deliver writing | Delivery does not establish reading or comprehension. |
| DS-04 | Listener hears a confident unsupported claim | Receipt records the claim and speaker; world truth is unchanged. |
| DS-05 | NPC lacks the requested information | Supported uncertainty, refusal or inquiry remains possible; no authoritative invented fact. |
| DS-06 | NPC genuinely believes a false report | Response can express that belief; receipt does not overwrite actual state. |
| DS-07 | Supported NPC decision deliberately deceives | Preserve private intention and public words separately; player view does not reveal deception automatically. |
| DS-08 | Bystander can hear only the final fragment | Record only that fragment and its justified meaning; no complete private transcript. |
| DS-09 | Player requests a work inquiry without specifying wording | Express only the bounded inquiry; no invented biography, payment or acceptance. |
| DS-10 | NPC offers work under actual terms and hiring authority | Record and deliver the offer; no employment, wages or stock yet. |
| DS-11 | Player accepts exact valid offered terms; required assent exists | Form the qualified agreement once; future work stays scheduled or pending. |
| DS-12 | Response requires a new fee or narrower service | Present changed terms for player decision; no automatic debit or assent. |
| DS-13 | NPC agrees genuinely to seek an appointment | Record that undertaking; official approval and meeting remain unresolved. |
| DS-14 | NPC successfully appeals for the player's cooperation | Preserve the appeal and supported effects; voluntary player choice remains open. |
| DS-15 | Departure or interruption occurs during a qualified exchange | Preserve produced/heard fragments and actual commitments; no unsent-content receipt. |
| DS-16 | Letter arrives after a decision deadline | No earlier knowledge or retroactive action; delivery does not execute its request. |
| DS-17 | Offer authority is revoked at the same unresolved frontier | Observe the dependency; do not select convenient ordering or conceal it with an automatic agreement. |
| DS-18 | Reload/retry a committed exchange; narration fails | Return the existing phase receipt; no new utterance, agreement, debit or elapsed-time effect. |

Claude must implement adapter bindings, actual channel/attention models, information projections and the applicable social procedures before claiming these cases pass. This contract supplies no new default historical values, universal persuasion die or active dialogue runtime.
