# IRGS 3.3.C — Agency, Time and Presentation Contract

Design handoff for Claude · 20 October 2026

This document specifies the next engine implementation. It is not a completion report. **3.3.C** is the Codex engine design line; **3.3.E** is Emergent's website and application line. Selected Shared Core 3.3 remains authoritative. Proposed models, source-document instructions and experimental code do not become adopted mechanics through this document.

## 1. Ownership and execution boundary

All people, households, businesses, governments and military institutions occupy one campaign world. Their planners submit intentions to the same Core validation, dependency, allocation, execution and persistence path used for player intentions. A planner cannot directly edit an actor, stock balance, capacity, relationship, legal position, clock or journal. Presentation cannot supply those edits either.

Reuse the established owners: K-ACTOR identities and actual condition; K-STOCK conserved quantities and custody; K-WORK activities and transformations; K-INFO assertions and received information; K-ORG mandates and institutional roles; K-NET routes and shared capacity; K-TIME scheduling and retained outcomes. Planners and projections are consumers, not additional authoritative databases. Existing asset and population owners remain authoritative where involved.

Player control and institutional authority are separate. An actor's current control policy can permit declaring personal intent without permitting requisition, taxation or command. A stored player ID, model response or nonempty authority reference is insufficient permission. Recheck current actor existence, selected control, actual mandate, scope and relevant receipts inside execution-derived observation.

## 2. Planner input: received and bounded information

Construct a detached input for one planning identity and one committed campaign revision. Supply only records legitimately available through that actor's or institution's actual information channels. A household ledger subscription does not grant access to every nearby depot. Institutional knowledge is not automatically the knowledge of every employee or ruler.

The proposed input envelope is:

```json
{
  "campaign_id": "campaign identity",
  "revision": 42,
  "planner_id": "installed policy identity",
  "principal_id": "actor or institution",
  "acting_actor_id": "actual registered actor",
  "policy_ref": "qualified policy and edition",
  "time_context": {"timeline_ref": null, "causal_sequence": 120},
  "authority_refs": ["actual scoped mandate"],
  "observations": [
    {
      "record_ref": "named bounded record",
      "receipt_ref": "actual receipt or qualified subscription",
      "occurrence_time": null,
      "received_at": "explicit information coordinate",
      "observed_at": "explicit observation coordinate",
      "status": "known_value",
      "value": "received value",
      "source_ref": "provenance"
    }
  ],
  "goals": [],
  "needs": [],
  "obligations": [],
  "current_activity_refs": []
}
```

Observation status must distinguish `known_value`, `observed_absent`, `unknown`, `disputed` and `stale`. Observed absence requires a qualified observation of a named scope; missing input never proves absence. Preserve occurrence time, receipt time, observation age, uncertainty and source status. Receiving a report does not establish that its assertion is true. A planner may reason from testimony while Core independently checks actual feasibility.

Goals, needs and obligations must reference actual records or an explicitly selected policy configuration. Never invent hunger rates, tax debts, employment, personality scores, inventory or wages to make planning appear active. Where required observations or selected models are missing, produce an unresolved proposal or an explicit no-action decision with that reason.

## 3. Planner output and institutional scope

A planner returns typed proposals, never executable code or direct state patches. Each proposal carries `proposal_id`, `campaign_id`, `planner_id`, `acting_actor_id`, `input_revision`, `policy_ref`, relevant receipt references, exact selected operation and parameters, authority references, prerequisites and a timing requirement. Retain its decision explanation separately from mechanical facts. No model-generated explanation constitutes evidence of an effect.

Output also supports an explicit decision record: `no_action`, `unknown_information`, `awaiting_selected_rule`, `awaiting_prerequisite` or `awaiting_authorization`. Record why the decision was made and which observations were consulted. `no_action` means an intentional policy decision under available information; `unknown_information` means the planner cannot determine an appropriate action. Neither advances time by itself.

| Institution | Bounded planning responsibility |
| --- | --- |
| Household | Consider recorded members, known provisions, actual obligations and available labour. Request transfers or provisioning only through qualified mechanics. |
| Business | Consider actual orders, workers, qualifications, work capacity, inputs and contractual obligations. Propose feasible work or deliveries without creating demand or stock. |
| Government | Consider received fiscal reports, established claims, lawful jurisdiction and actual administrative capacity. A policy target does not establish collectible revenue. |
| Military | Consider received orders, actual command scope, known personnel, readiness, equipment, supply and route capacity. An order does not establish mobilization or delivery. |

The same worker, material, site or vehicle cannot be independently allocated by these planners. Preserve cross-institution competition through shared Core records. A policy may be installed for multiple institutions, but each invocation retains its own principal, information, mandate and provenance.

## 4. Durable lifecycle and pending work

Retain proposal identity, immutable original payload and digest before consequential execution. Link every execution attempt, allocation decision, committed effect and outcome to that identity. Accepted retries return the existing receipt; altered payloads under the same identity fail. Transport success means the request was retained, not that the intention succeeded.

Persist pending NPC work with its campaign, initiating event, expected revision, input references, policy edition and processing state. A background task may perform computation, but it is not the pending-work authority. After restart, recover or explicitly defer retained work. A timeout must not silently mark an unfinished proposal complete or merely hide its pending status.

Revalidate a stale proposal against current state before committing. Preserve the original proposal and add the new attempt; do not rewrite its input history. State, effect references, request status and durable receipt must share an atomic commit boundary or an explicitly recoverable staged protocol. Restore and action execution require the same revision and serialization protection.

## 5. Time, deadlines and interruptions

Keep causal sequence, elapsed simulation time and civil-calendar position distinct. A causal counter orders commits; it does not measure minutes. A day-precision opening does not establish dawn or an exact hour. Existing activity coordinates must retain their documented axis until an explicit compatible timeline binding is selected.

A qualified timeline binding specifies units, origin, supported calendar conversion, precision and duration models. Julian dates require Julian arithmetic. Other calendars require their own selected rules. Unsupported conversions remain unbound. Never adopt a fixed thirty-minute action, six-band day, recovery rate or journey duration merely because a prototype used it.

With a qualified elapsed-time model, find the next relevant deadline, completion, interruption or information arrival. Evaluate simultaneous ready proposals against the same pre-frontier world. Include actual authorization, availability, resource, capacity and prerequisite reads in observed dependencies. Commit independent effects only where their combined candidate satisfies invariants. Preserve competing requests when no qualified allocation rule or authorized decision selects a winner; identifiers and incidental iteration order select none.

Long actions need explicit stages. Retain actual partial work, consumed inputs, injuries, reservations or deliveries when an interruption occurs. Cancel only unperformed stages under the selected rules. An interruption cannot erase committed consequences, and scheduling cannot establish that future work occurred. Without an elapsed-time model, qualified ledger effects may be recorded at their supported precision while duration remains unknown; this does not establish zero duration. A duration-dependent process cannot advance beyond its supported timing.

## 6. Two required execution traces

**Received military order.** A registered NPC receives a specific equipment-issue directive. Its planner sees that receipt and the bounded records legitimately available to it. It proposes the existing Military issue operation with the actual recipient, persons, material, depot, quantity and authority. Core rechecks the directive, deadline, actor existence, command scope and conserved stock. Success transfers the stock once and marks that order executed. Missing stock leaves the request unresolved; a contradictory rumour cannot manufacture stock. A restart or retry preserves the same outcome.

**Roman future booking.** A delegation identifies delegate, principal, people, role, site and permitted window. Actual delegation alone does not establish that an autonomous delegate received it; missing communication leaves autonomous planning awaiting prerequisite. After a legitimate receipt and selected timing basis, Core may book a qualified activity against shared people and capacity. The outcome is `scheduled`. It establishes neither performed labour nor manufactured output, wages, elapsed time or automatic completion. Later revocation or interruption follows the qualified cancellation and partial-effect rules.

## 7. Conditional history and presentation

Historical baseline events remain prospective reference material, privately scoped to qualified Creator inspection. They are not actor knowledge, journal occurrences or mandatory outcomes. A scheduler can submit a conditional historical proposal only when its model, prerequisites, participants and timing are qualified against the actual playthrough. A collapsed kingdom or dead participant cannot reappear because a template expects it.

For a new historical game, use its designated starting snapshot. Continuing games use their committed world and source edition. Reevaluate affected causal descendants when prerequisites change; do not impose a global divergence score, forced victory or predetermined end date. Unknown causal bindings remain unknown.

3.3.E receives committed outcome references and legitimately filtered observations. Narration follows resolution and cannot supply additional effects. Report an unresolved intention as unresolved. A failed, repeated or corrected narration must not repeat mechanical execution. Preserve presentation errors separately from committed world outcomes. No provider selection, UI implementation or website redesign is prescribed here.

## 8. Acceptance cases for implementation

| ID | Case | Concrete expected outcome |
| --- | --- | --- |
| AG-01 | Missing household report | Planner returns unknown information; it does not infer an empty pantry. |
| AG-02 | Observed empty pantry | A qualified scoped observation permits planning from absence; no food appears automatically. |
| AG-03 | Unreceived military order | NPC cannot plan its execution from global world truth. |
| AG-04 | Received equipment directive | Exact qualified issue transfers conserved stock once and produces a linked receipt. |
| AG-05 | Lost response and retry | Same identity returns the original outcome; stock and clock are unchanged by the retry. |
| AG-06 | Altered accepted payload | Engine rejects it without changing the original request or world. |
| AG-07 | Competing depot requests | Shared dependency is detected; no identifier-order winner is chosen. |
| AG-08 | Independent institutions | Both qualified effects commit with equivalent domain results under either evaluation order. |
| AG-09 | Revoked authority | A pending proposal cannot use the obsolete mandate; no partial effect commits. |
| AG-10 | Roman booking | Outcome is scheduled; output stock, wages and completed-work history remain unchanged. |
| AG-11 | Interrupted work | Actual committed partial consequences survive; unperformed stages do not become complete. |
| AG-12 | Unbound calendar | Causal commits produce no inferred minutes, hour, date or day transition. |
| AG-13 | Julian leap boundary | Under a selected Julian binding, 28 February 1500 is followed by 29 February. |
| AG-14 | Restart during NPC planning | Retained pending work is recovered or explicitly deferred without duplicate execution. |
| AG-15 | Concurrent restore | Stale action commit fails its revision check instead of overwriting the restored world. |
| AG-16 | Historical participant absent | Exact historical proposal is blocked or reassessed; no actor or kingdom is resurrected. |
| AG-17 | Narration failure | Mechanical receipt remains valid; retrying presentation produces no additional effect. |

Historical durations, consumption, productivity, recovery, wages, travel capacity, command practice and causal event conditions require sourced, versioned model selections. Until researched and qualified, their absence remains visible. These acceptance cases define work to prove, not results already achieved.
