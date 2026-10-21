# 3.3.C — Timeline and process contract

**Edition:** C2 · 20 October 2026  
**Status:** Proposed engine design for Claude implementation

This contract develops the C1 supplement's time and interruption rules. It uses the same action lifecycle, nine owners, immutable submissions, separately identified attempts/phases and durable receipts. It specifies behaviour to implement and prove; it does not activate a scheduler or adopt numerical rates.

## 1. Coordinates and precision

Keep these coordinates distinct:

| Coordinate | Meaning |
| --- | --- |
| Storage revision | A confirmed persistent head. Metadata acceptance can change it without physical time passing. |
| Causal sequence | An ordering of committed events and dependencies; the existing Core `clock` belongs here. |
| Elapsed simulation time | Duration on an explicitly selected physical/process axis with declared units and origin. |
| Civil calendar position | A dated representation under a qualified calendar and conversion binding. |
| Information time | Observation, transmission, receipt and understanding coordinates, separately retained. |
| Wall-clock time | Host execution, persistence or worker-lease time; no automatic relation to simulated duration. |

A day-precision opening supplies no exact hour. A time-of-day band supplies a range or qualitative relation, not a universal arithmetic step. A causal event number cannot be converted into minutes by counting actions. Julian-labelled dates require a selected Julian calendar procedure; an implementation must not silently substitute its host calendar library. Other calendars and cross-calendar conversions need their own qualified bindings.

Represent an uncertain time as a bounded range or explicit qualitative relation on a named axis, with endpoint conventions and precision. Unknown bounds remain unknown. A display approximation does not replace the actual stored coordinate or justify ordering events within that approximation.

Routine established capability does not require invented statistics. An ordinary walk may be supported without an agility score or exact speed. Its elapsed-time representation can retain a qualified bound or qualitative relation. A material deadline comparison requires enough timing information; it cannot assume either punctuality or failure from an absent number. Use existing evidence, a supported retained adjudication or an explicitly selected assumption when permitted. Record the assumption and scope; never install a convenient default silently.

## 2. Required logical records

These records extend existing owners rather than creating another simulation database. Fields can be mapped to compatible existing schemas.

| Record | Required meanings |
| --- | --- |
| TimelineBinding | Campaign/scope, identity and edition, coordinate domain, units, origin relation, calendar/conversion references, precision rules, provenance and adoption scope. |
| TemporalPosition | Named axis, exact coordinate or bounds/qualitative relation, endpoint conventions, precision, source and uncertainty status. |
| TimeAdvanceRequest | Immutable request identity, principal, authorized horizon or stopping condition, timeline reference, allowed processes, spending/choice limits and interruption policy. |
| TimeProcess | Process/phase identity, responsible owner, actual affected records, selected update law and units, prerequisites, operating interval, committed-through position, next boundary, stop conditions and retained partial state. |
| Frontier | Identity, selected head revision, coordinate or uncertainty window, causal parents, due occurrences/proposals, observed dependencies and unresolved ordering/allocation decisions. |
| ProcessedSpan | Campaign and lineage, process/phase, half-open interval `[start,end)`, model edition, actual input/context references, accumulated progress or use, effects and durable receipt. |

Numerical models must declare their units, domain, boundary conditions, numerical method and tolerance where approximate. Preserve fractional useful work and consumption at the required precision; display rounding cannot delete it. A changed model requires an explicit prospective bridge, not reinterpretation of already processed spans.

Information records retain occurrence, observation and receipt separately. Compare coordinates only through a qualified relation. A later report does not cause the reported occurrence again. Formal revocation and the recipient's knowledge of it may have different effective times under the selected institutional procedure.

## 3. Advancing to a frontier

An authorized advance is a request to continue qualified processes up to a limit, not a guarantee of reaching that limit.

1. Recover the accepted request and existing attempt/phase receipts. Verify current campaign scope, head and continuation authority.
2. Identify active processes and actual commitments in the one world, including due NPC work, transport, information arrivals and institutional reviews. Select only processes with qualified models and timing relations.
3. Find the earliest relevant completion, prerequisite change, threshold, deadline, interruption, message arrival or new voluntary player decision before the requested horizon. Include boundaries produced by coupled processes; domain planners cannot privately advance past them.
4. Determine what interval is justified. If uncertain event ranges overlap and their order materially changes effects, retain an ordering requirement instead of choosing an arbitrary instant. Independent commuting effects may proceed only where that independence and their supported interval are established.
5. Integrate each qualified process over the unprocessed portion up to that boundary, using actual means and conditions. Prepare all coupled effects against a consistent frontier snapshot.
6. Observe authorization, prerequisite and effect accesses. Resolve qualified causal order or allocation; retain unresolved competing proposals. Validate the combined candidate, including conservation, exclusive commitments, capacities and timing.
7. Atomically persist the actual effects, processed spans, outcomes, pending continuations and head change. Then deliver permitted information and presentation from those results.
8. Continue under the same authorized limits, or return control at a material interruption, unsupported dependency or new player decision. Give the actual reached boundary and unresolved remainder; do not label the requested horizon completed when it was not reached.

An unbound process does not prove that the whole world is frozen. Independent qualified processes can continue where their safe frontier is established. Conversely, omitting a relevant unbound process is not permission to assume it had no effect. Apply a conservative dependency barrier where that missing behaviour could change the proposed result.

For simultaneous proposals, identifier order, arrival order and iteration order supply no winner. A supported institutional priority or later authorized decision may establish allocation. A physically established occurrence, such as destruction of reserved stock, is not an optional allocation request that a reservation can veto. Commit its supported actual effects and reconcile backing, claims and interrupted processes through their owners.

## 4. Work, use and interruption

A reservation or activity booking records future access or commitment. It is not performed labour, consumed food, delivered service, earned wages or manufactured output.

At a process start, validate actual availability and acquire only the permitted commitments or backing. As work occurs, debit inputs at their selected process stages and record actual qualifying progress. Completion, inspection and acceptance remain distinct. Wages or claims accrue only under their actual agreement and basis; a booked interval is not automatically useful work.

An interruption splits the processed interval at its real supported boundary. Preserve completed work, consumed inputs, physical changes, earned claims and remaining fractions. End or release only unperformed portions allowed by the cancellation procedure. Reusable input, consumed input, scrap and unfinished output retain distinct actual identities or quantities. No rollback of past occurrences is implied by changing a process status to `interrupted`.

Continuation uses a new attempt/phase identity linked to the same retained intention where its method and scope remain valid. Recheck current means, authority and timing. A changed method requires a superseding request; an expired window cannot be repaired by rewriting the original payload. Replaying a scheduling receipt cannot create another booking, and replaying a progress receipt cannot earn the same work twice.

## 5. Consistency across review scales

Half-open processed intervals assign an endpoint to exactly one adjacent span. The same process cannot settle overlapping intervals twice. A coarse advance and a partition into shorter advances must produce equivalent owner state under the same model, inputs, boundaries and retained decisions, within declared approximation tolerance.

When rates or constraints change, split at that cause. Do not apply the final rate retrospectively to the whole interval. Coupled demand, stock depletion, available capacity and process output must agree at each consequential boundary. Two domain summaries cannot both consume or credit the same portion.

Events with zero modeled duration may still have causal order. Process their finite dependency closure without inventing elapsed time. Detect repeated non-progressing states or cycles lacking an independent enabling cause. Retain the diagnostic and unresolved dependent processes; do not drop queued events, advance an arbitrary tick, or invent fuel/capacity to escape the cycle. Legitimately recurring activity requires a model that establishes its next boundary.

## 6. Recovery, restoration and timeline changes

Retain processed spans, phase identities, decisions and pending boundaries in the same recoverable commit as their effects. A worker lease expires on the host clock; expiry does not advance simulation time or prove the old attempt failed to commit. Apply the C1 receipt, revision and fencing rules before a new worker can settle an interval.

Restoration selects the checkpoint's actual temporal state under a new storage revision. It does not execute intervening time. A pending checkpoint process may have completed on a discarded future head. Its historical receipt proves that old occurrence, not completion in the restored lineage. Invalidate displaced worker claims, then hold or authorize a newly identified continuation under the restoration policy. Preserve lineage links and revalidate the current window; never replay the old effect or falsely mark the restored task complete.

A timeline migration must explicitly map coordinates, precision, pending windows and processed spans, preserve original references and validate supported conversions. If no sound mapping exists, hold affected processes and report incompatibility. Loading a save cannot silently convert its dates, choose an hour, reseed historical events or reset accumulated work.

## 7. Proposed acceptance cases

All durations, quantities and model selections below are synthetic test fixtures, not historical calibration. These cases have not been executed.

| ID | Before / attempted operation | Required actual result |
| --- | --- | --- |
| TP-01 | Accept an unresolved intention at storage revision 4 | Receipt/head may advance; physical duration and civil date do not. |
| TP-02 | Day-only opening; request an hour-dependent deadline comparison | No invented dawn; retain bounds or the specific unresolved timing requirement. |
| TP-03 | Healthy actor, feasible ordinary path, no agility number | No artificial capability failure or mandatory roll; retain supported movement/time precision. |
| TP-04 | Selected Julian profile; advance from 28 February 1500 by one civil day | Result is 29 February under that binding, not host-Gregorian substitution. |
| TP-05 | A process has no applicable duration model; independent known ledger occurrence is due | Hold its dependent timed effects; do not freeze or falsely complete the independent occurrence. |
| TP-06 | Authorize one hour; a new player concession is needed after twenty minutes | Settle only actual first-span effects and return the concession; do not reach the hour silently. |
| TP-07 | Same work/model advanced once over `[0,10)` or over `[0,4)` then `[4,10)` | Equal supported progress, inputs and claims within declared tolerance; no endpoint duplication. |
| TP-08 | Retry a committed span after response loss | Same receipt; no extra work, consumption, claim or elapsed duration. |
| TP-09 | Productive rate changes at coordinate 4 during `[0,10)` | Integrate separate valid spans; do not apply the later rate to all ten units of time. |
| TP-10 | Future activity is booked, then inspected | One commitment exists; no completed work, output or wages appear. |
| TP-11 | Work consumes one input before interruption, leaving useful unfinished progress | Consumed input and progress persist; only unperformed portions are cancelled or held. |
| TP-12 | Two simultaneous processes request the same exclusive worker | Conflict survives; no duplicate labour or identifier-order winner. |
| TP-13 | Independently established loss destroys reserved backing | Actual loss persists; reconcile reservation/obligation shortfall without replacement stock. |
| TP-14 | Report arrives after the occurrence and a decision deadline | Receipt changes qualified knowledge then; no replay or retroactive informed decision. |
| TP-15 | Overlapping uncertain event windows have order-sensitive effects | No guessed order; retain the material ordering requirement and any safe independent progress. |
| TP-16 | Zero-duration prerequisite cycle has no enabling state | Persist a non-progress diagnostic and hold dependent work; no arbitrary tick or fabricated input. |
| TP-17 | Restore a checkpoint with a task completed only on its discarded future head | Restore saved progress; old receipt stays historical; hold or issue a new authorized continuation without replay. |
| TP-18 | Load a save whose timeline has no qualified conversion to the proposed new axis | Preserve original coordinates and fractions; require explicit migration or hold, with no read-time conversion. |
