# Claude implementation handoff — IRGS 3.3.C

**Handoff edition:** C2 · 20 October 2026  
**Purpose:** Implement the engine design developed by Codex, retaining verified existing behaviour.  
**Status:** Ready for implementation review; coding and acceptance remain to be completed.

## Human scope and source authority

The user has directed that Codex primarily develop the engine in text and hand coding to Claude. **3.3.C** is this engine line. **3.3.E** is Emergent's website and app line. The immediate task is engine implementation and its integration contract. Website redesign, commercial services and wholesale replacement of working subsystems are outside this handoff.

Read these files in order:

1. `README.md` for package status and source baseline.
2. `IRGS_Core_3_3_C_Engine_Supplement.md` for the common semantics, ownership, lifecycle and ordinary-action design.
3. `ACTION_AND_DEPENDENCY_CONTRACT.md` for the first consequential actions and certification requirements.
4. `PERSISTENCE_AND_RECOVERY_CONTRACT.md` for durable acceptance, retries, restoration and pending work.
5. `AGENCY_TIME_AND_PRESENTATION_CONTRACT.md` for subsequent autonomy, scheduling and the 3.3.E boundary.
6. `INSTITUTIONAL_EXECUTION_MODEL.md` for the four reference policy procedures and shared-resource integration fixture.
7. `CMRR_AND_ACCEPTANCE.md` for reconciliation, implementation gates and acceptance evidence.
8. `IMPLEMENTATION_PACKETS.md` and `HANDOFF_STATE.json` for bounded coding scopes and return evidence.
9. The C2 timeline, movement/observation and dialogue contracts for ordinary-action implementation.
10. `PLAYABLE_ACTION_CYCLE.md` and `fixtures/PLAYABLE_CYCLE.json` for the integrated synthetic trace.

The immutable C1 archive is the previous design edition. C2 preserves its 55 foundation cases and adds 66 ordinary-action/integration cases. `CHANGES_C2.md` records the new scope and clarifications. Document edition labels and implementation milestone labels are separate; use PKT-00–PKT-06 to identify a bounded coding handoff.

The bundled reference Core and master are source material, not evidence that every attached instruction or proposed mechanic has been adopted. The selected foundation remains Core 3.3. Preserve its nine owners, source status distinctions, campaign continuity and existing supported handlers. Do not treat the 3.3.C label as permission to activate a replacement runtime without qualified evidence.

The supplied `IRGS-3.3.C.zip` is a container of nested archives. Its clean `IRGS_3_3_2.zip` contains the same 57 runtime Python files as the selected local engine. Either catalogue archive supplies identical content. In `IRGS-3.3.E.zip`, the active `backend.engine` is a separate lightweight kernel; the preserved `codex_332` folder is not an active Core adapter. Inspect actual imports and mutations rather than inferring integration from archived files.

## Canonical semantics and field mapping

The supplement's lifecycle table is the common vocabulary. `completed_successfully` refers to the stated completion condition; `scheduled` is not completed work and must permit later progress, interruption or cancellation. A scheduling phase can be completed while its parent process remains scheduled. Keep phase status and parent-process status explicit.

Map legacy names instead of blindly replacing them:

| Existing representation | Required interpretation |
| --- | --- |
| `declared_not_resolved` | Retained intention, no inferred physical outcome. |
| R9 `unresolved` | An attempt is unresolved; use its reason to distinguish rule, authorization, prerequisite and allocation states. |
| R9 `committed` | That Core operation committed; determine whether it completed a transfer, booked work or only recorded metadata. |
| Prototype `resolved` | Insufficient to infer general success; inspect the actual effect and completion condition. |
| Historical plan status | Prospective reference assessment, not an action status or an actual occurrence. |

The documents use existing native parameter names in examples and logical persistence fields in record tables. Implement one explicit mapping:

| Action example | Logical record meaning |
| --- | --- |
| `campaign_id`, `request_id` | Immutable scoped request identity. |
| `actor` | `actor_ref`; authenticated caller/principal remains separately established. |
| `controller` | Player or delegated-proposal mode; never a caller-supplied authority grant. |
| Exact `declaration` | Preserved declaration record referenced by the action. |
| `selection.operation`, `selection.params` | Typed semantic command; effective rule/binding edition must also be retained. |
| `source_ref`, `instruction_ref` | Source and player instruction references; they do not prove legal authority by themselves. |
| `at` | Coordinator-assigned causal submission coordinate. It is not client-selected elapsed time. |
| `expected_revision` | Commit precondition outside the semantic action digest. Retain the accepted attempt's evaluated revision. |

Use one versioned canonical JSON encoding and publish it. Reject duplicate object keys, nonfinite values and unsupported types. Preserve exact semantic strings. Different field spellings may be adapted, but their meanings and scope must not change.

Keep the semantic-payload digest distinct from the original accepted-record digest. The first excludes coordinator-assigned submission time and revision preconditions; the second includes the frozen accepted coordinate. Submission retry recovers that coordinate. Submission acknowledgements, attempt/phase outcomes and the current-status projection are separate records. This permits legitimate later execution of a scheduled process without replaying its booking.

## Coding sequence and completion gates

### C1 — Durable consequential action foundation

Build the immutable request/attempt/outcome workflow around existing CoreWorld operations. Instrument current actor existence, control, authority and effects together. Use the existing Military equipment-issue and Roman delegated-booking handlers as the first bounded effects. Expose no unrestricted stock transfer or arbitrary world-patch endpoint merely because a low-level handler accepts an authority string.

Persist the candidate world, journal links, accepted receipt and recoverable pending work together. Check campaign access and scope first; an accepted identical retry returns its original receipt before a stale revision is rejected. New submissions and new attempt/phases must pass the expected-revision check. Restore must serialize against every world writer. Preserve the original accepted receipt even when its effect belongs to a head that has subsequently been restored away. Reconcile restored pending work through a new authorized attempt or an explicit hold; a discarded future head's completion receipt must neither recreate its effect nor block the restored task forever.

Reuse the actual dependency observer/frontier. Improve actual sequence observation where read-only lists are currently conservatively reserved as writes, with semantic parity and mutation tests. Do not replace observed dependencies with manually written footprints. Trace rejected branches and decision reads; revalidate combined candidates.

**Gate:** A01–A22 and PR-01–PR-16 pass where applicable, with explicit holds for unsupported behaviour. Both real CoreWorld receiving profiles execute the bounded effects. No duplicate transfer, hidden authority bypass, false work completion or stale restore overwrite occurs. This gate does not establish general freeform gameplay or a Living Day.

### C2 — Explicit time and ordinary first interaction

Implement a selected elapsed-time/calendar binding and an ordinary-action adapter with actual effects. Movement and observation are suitable initial candidates; a dialogue request must distinguish utterance, receipt, response and agreement. Preserve qualitative routine capability instead of requiring invented statistics. Define clocks, precision, route or local-position semantics and stop conditions before claiming completion.

Implement the C2 timeline, movement/observation and dialogue contracts through PKT-02–PKT-04. Their TP, MO and DS cases define 54 required checks for actual movement, reachable evidence, communicated terms, real elapsed-time effects, Julian boundaries where selected and player decisions encountered before an authorized horizon. Unsupported durations remain unknown. No fixed thirty-minute action or six-band arithmetic is adopted.

**Gate:** At least one supported ordinary player interaction changes the world or legitimately received information, survives reload and retry, and is presented from its committed result. The implementation report identifies exactly which action families work.

The broader C2 design is not fully qualified by that first interaction. PKT-05 requires IC-01–IC-12, including real staged work and claim/payment effects. Use the fixture's explicitly selected capabilities, mandates, time policy, bay windows and quantities. Preserve the safety stop and player's continuation choice. A synthetic successful trace does not establish historical calibration or a complete Living Day.

### C3 — Campaign-native autonomous institutions

Install qualified receipt-backed policies for household, business, government and military actors on the same world. A policy submits ordinary typed actions; it cannot write stock, conditions, time or events directly. Retain genuine no-action decisions and unknown-information states separately.

Run the 17 agency/time acceptance cases and an integrated shared-world fixture. Include competing access to one actual resource or worker, an earlier interruption, a received order, a missing report, a pending task across restart and a delayed information arrival. Record actual work, consumption, claims, settlement and equipment effects distinctly. A synthetic policy fixture is not historical calibration.

**Gate:** The four institutions execute qualified actions over shared records through the same engine. Show what changed, why, which information enabled each decision and which processes remain unsupported.

### C4 — Extended rule qualification

Develop the remaining ordinary action adapters, sourced historical conditions, longer horizons and qualified genre extensions. Keep historical reference, actual history and actor knowledge separate. Preserve the 37-entry HYW catalogue and its current initializer readiness. Do not broaden a narrow successful fixture into a claim that every engine or historical date is qualified.

## Required implementation return

Return the exact source revision, code/binding hashes, request and outcome schemas, owner/reuse mapping, migration or compatibility policy, named acceptance results, actual access traces and unresolved cases. Include recorded before/after examples for successful effects, rejected prerequisites, allocation conflicts, crash recovery and presentation failure.

Report design, implementation, automated verification, deployment, calibration and playtesting separately. Regenerate package integrity evidence for changed code. Do not reuse old certification counts as proof of a new implementation. Preserve the previous release and user saves; a migration must be explicit and reviewable.

The inactive coding experiment in the author's local `IRGS_3_3_C` folder is excluded from this handoff. It has not passed integrated acceptance and is not a mandatory code starting point. The verified supplied archives and these reconciled text contracts are the implementation references.
