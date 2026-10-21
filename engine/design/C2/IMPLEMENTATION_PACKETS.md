# 3.3.C — Incremental implementation packets for Claude

**Design edition:** C2 · 20 October 2026  
**Status:** Handoff plan and interface contract; implementation evidence remains outstanding.

Codex can continue developing the text while Claude implements a bounded packet. The numbered C1/C2 labels on documents identify design editions; they are not claims that the similarly named implementation milestones have passed. Use the packet IDs below to identify coding scope and return evidence precisely.

## 1. Packet dependency map

| Packet | Required input | Implementation scope | Acceptance references | Completion evidence |
| --- | --- | --- | --- | --- |
| PKT-00 | Supplied C/E archives and preserved reference hashes | Audit current source, active imports, selected bindings, actual save formats and inherited checks. Reuse working behaviour; classify unimplemented contracts. | Baseline/source verification, not a new behavioural test count. | Exact source revision; owner/reuse map; compatibility findings; selected implementation baseline. |
| PKT-01 | PKT-00 | Durable intentions, attempts, phase receipts, current control/authority, actual dependency observation, safe replay/restore and the two existing consequential native handlers. | A01–A22; PR-01–PR-16. | Military transfer and Roman scheduling examples; actual traces; crash/retry/restore evidence; explicit unsupported states. |
| PKT-02 | PKT-01 | Named timeline bindings, duration/precision semantics, processed spans, coupled frontiers, interruption and continuation. | TP-01–TP-18. | Actual reached frontier; retained partial effects; coarse/fine equivalence; calendar and restoration cases. |
| PKT-03 | PKT-01; PKT-02 for timed stages | Actual local movement/transit, bounded observation and retained searches. | MO-01–MO-18. | Genuine position/receipt changes with no invented ratings or omniscient projection. |
| PKT-04 | PKT-01; PKT-02 for timed exchanges | Spoken communication, recipient comprehension, NPC response proposals, offers, assent and actual agreement consequences. | DS-01–DS-18. | Phase-linked utterances/receipts/terms; no prose-created truth or player assent. |
| PKT-05 | PKT-02, PKT-03, PKT-04 and qualified staged-work/claim adapters | The integrated observe → travel → negotiate → work → interrupt → continue → accept → settle sequence. Implement missing work/claim adapters through their existing owners. | IC-01–IC-12. | Fixture trace, owner-state before/after, knowledge projection, dependency decisions and recovery evidence. |
| PKT-06 | PKT-01; PKT-02 for timed policies; relevant action adapters | Receipt-backed household, business, government and military policies acting on the same records. | AG-01–AG-17 and the institutional shared-resource fixture. | Each actual proposal, information basis, authority, result or truthful no-action reason; no substitute world state. |

Packets describe dependencies, not a requirement to rewrite completed components. A packet may be implemented in smaller reviewed slices, with required holds visible. Completing one slice does not qualify unsupported sibling actions or the whole packet. PKT-05's synthetic work example needs no historically calibrated production economy, but it does need genuine staged work, parcel transfers, claim and payment effects.

## 2. Stable semantic boundary

The implementation must preserve these meanings even if its programming interfaces use different names:

| Operation | Input identity and conditions | Required response semantics |
| --- | --- | --- |
| Submit intention | Scoped request identity, exact declaration, actor, selected method/parameters, source and instruction references. Caller identity is authenticated separately. | Immutable submission acknowledgement plus a separately labelled current-status view. Acceptance alone is not success. |
| Attempt or continue a phase | Scoped new attempt/phase identity, original request reference, current expected revision, qualified rule/timing bindings and permitted continuation. | That attempt's immutable receipt, actual effects or explicit unresolved reason, and the reached boundary. |
| Retrieve receipt | Authorized campaign scope and the particular submission or attempt/phase identity. | Original historical receipt without replay; identify its lineage and whether its effects belong to the current selected head. |
| Query actor view | Authenticated access to the actual controlled or delegated perspective. | Permitted actual/received records only. Neither querying nor presenting advances the world. |
| Advance under limits | Immutable authorized horizon/stop conditions, timeline binding, current revision and allowed processes/choices. | Reached boundary, committed spans, pending continuations and any material decision. Requested horizon is not guaranteed. |
| Checkpoint, restore or fork | Separate scoped management identity, source revision/checkpoint, access and compatibility. | Durable management result with preserved provenance. No simulated work or replay of inherited events. |

No remote request may supply executable code, arbitrary owner-state patches, trusted caller identity or an authority grant. Typed method and source fields are proposed input; actual control and institutional validity are checked by Core. New adapters join the same transaction, information and dependency path.

The public response is an authorized projection of the internal outcome. An internal blocked reason can refer to a hidden actor, false report or secret mandate; it must not disclose that fact by returning raw validation detail. Preserve the detailed cause under its proper access scope and expose only legitimate character knowledge or necessary service status.

### Speech and presentation

A proposed NPC utterance can be generated before it occurs, from that NPC's permitted knowledge and policy. Core validates the proposed production, channel, commitments and effects before it becomes an occurrence. This is agency input. Player-facing narration of what happened is a separate post-commit presentation operation. Reusing one language model for both roles does not merge their authority or records.

## 3. Version and change control

The C1 design archive remains an immutable previous edition. C2 adds ordinary-action, timeline and integrated-work design while preserving the C1 foundation meanings and 55 case identifiers. The 66 additional cases have new identifiers. A reference to C1 acceptance remains traceable and must not silently acquire a different expected outcome.

For each later change, record its requirement ID, old and new meaning, source reason, compatibility classification, affected owners, packets and cases. Classify changes as a clarification preserving meaning, an additive capability, a correction of a contradiction, or an incompatible semantic change requiring a new binding/schema and migration policy.

Pending actions retain the rule and schema editions under which they were accepted. A new design file does not retroactively reinterpret an accepted action. A sound prospective bridge can map its unexecuted remainder; otherwise hold that remainder explicitly. Retain past effects and original records.

`HANDOFF_STATE.json` is the delivery index for this edition. It identifies packet dependencies, acceptance ranges and current evidence status. It is design metadata, not an authoritative world record or a claim that Claude has started implementation.

## 4. Claude's return package

For each implemented packet, return:

1. Source revision and exact code/binding identities.
2. A reuse/change map naming the existing logical owners and adapter mappings.
3. Actual request, attempt, phase, outcome and permitted projection examples.
4. Per-case results and evidence, including failures and unsupported holds.
5. Observed authorization/prerequisite/effect accesses and same-frontier cases.
6. Persistence, replay, restore and compatibility/migration evidence for affected data.
7. Any unresolved model, source, authority or timing decisions, with a precise blocked capability.
8. Separate implementation, verification, deployment, model-adoption, calibration and playtest status.

Update the handoff index from supplied implementation evidence only. A test's existence, a completed mock screen or a model-generated narrative does not satisfy a behavioural case. Reconcile returned code with the next design edition before expanding the packet.
