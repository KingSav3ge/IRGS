# Qualified rejected dependencies — dependency-rejections-1

2026-10-22. Continues the selected Core 3.3 from `bf6cf48`, including the bounded fictional Rise foundation. This increment advances DEV-07 and named cross-backend evidence under DEV-08. Those broader milestones and DEV-06 remain open.

## Retained rejection evidence

`r9_runtime.observe_rejection` executes a fresh supported request on two detached copies using the same backend selection as successful R9 observation. Ordinary and traced execution must raise the same exception type and arguments, leave the initial snapshot unchanged and avoid constructor normalization. Unsupported handlers, processed identities, a successful ordinary execution, differing errors or mutated failure state receive no qualified rejection record.

The resulting private record contains the actual read paths, code/snapshot identity, backend/profile and validation reads. Its committed `writes` are empty. Mutator calls made inside the rolled-back transaction are retained separately as `attempted_writes`. The record explicitly says `rejected_no_effects` and `successful_certificate: false`; it does not prove a completed player action or create an outcome.

R9 frontiers now retain that verified record with the original unresolved request, its payload digest and an explicit dependency qualification status. Failed-path reads can establish a recorded conflict with a peer's writes. Existing conservative deferral and physical-occurrence policies remain in force. Rejection does not gain allocation priority, authorize delayed execution or complete an unsupported operation. Later decisions still revalidate the original request against current state.

The equipment and authored-scene failure helper reuses the paired check. An instrumentation failure whose ordinary action succeeds is labelled `observation_refused`, rather than being misreported as a reproduced rejection. Existing safe public error text and actor-filtered presentation remain unchanged. Validation scans stay separate from allocation reads and are omitted from persisted frontier certificates, as before.

## Named executable checks

`runtime/test_rejected_dependencies.py` exercises:

- Reference-world late failure after a cash write: attempted changes roll back while the missing-account read remains visible.
- Economic-backend scarce cash; military/Roman receiver revoked delegation; selected Core depleted equipment and absent order.
- Fictional settlement revoked founding permission and a worker already reserved for shelter construction; reference shared-worker booking rejection.
- Both orderings of a failed request and a conflicting peer: neither receives a winner, original requests and qualified reads survive save/load, and reused submission identity is rejected.
- Unknown handlers, processed requests, successful ordinary execution, error mismatch and non-atomic failures cannot acquire a qualified rejection record.
- A successful action refused by instrumentation remains unqualified and produces no live effects.

The capture tooling distinguishes calls inside `observe_rejection` from actual committed events. Its regression test verifies that a detached successful probe does not inflate the committed-event count. Existing equipment, scene, receiver, decision, settlement, host and interface suites retain their respective scope. Results are recorded separately in `DEPENDENCY_REJECTIONS_VALIDATION.json`.

## Limits

This is execution evidence for named reviewed JSON handlers across four selected backends. It does not certify all branches or arbitrary Python plugins, refine whole-container dependency granularity, repair every legacy caller/backend mismatch, introduce a universal scheduler, implement general freeform/combat resolution or migrate existing saves. Rejection evidence in the engine frontier is distinct from the host's player-submission lifecycle; there is no new promise that every rejected HTTP attempt becomes a saved player action.
