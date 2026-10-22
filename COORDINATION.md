# IRGS development coordination

The user assigns **IRGS Enviroment** as coordinator and reviewer for three development chats. Each component chat owns its repository; the coordinator publishes qualified combined source to `KingSav3ge/IRGS/main`.

| Development chat | Repository | Current assignment |
| --- | --- | --- |
| IRGS Engine | [IRGS-Engine](https://github.com/KingSav3ge/IRGS-Engine) | [Verified Catalog multipart reader](https://github.com/KingSav3ge/IRGS-Engine/blob/main/COORDINATOR_WORK_ORDER.md) and continuing dependency qualification. |
| IRGS App/Website | [IRGS-APP-WEB](https://github.com/KingSav3ge/IRGS-APP-WEB) | [Creator Historical Details browser](https://github.com/KingSav3ge/IRGS-APP-WEB/blob/main/COORDINATOR_WORK_ORDER.md), compatible component pins and App plan. |
| IRGS Catalog | [IRGS-Catalog](https://github.com/KingSav3ge/IRGS-Catalog) | [Complete archive multipart payload](https://github.com/KingSav3ge/IRGS-Catalog/blob/main/COORDINATOR_WORK_ORDER.md) under Historical Details, with provenance and a Catalog plan. |

## Current cycle

`historical-details-01` is assigned, not complete. `COORDINATION.json` records baseline commits, thread identities, review status and blockers. The last integrated component set remains selected in `COMPONENTS.json`. The new Engine framing/atlas work has initial source checks but is not integrated yet; App and Catalog still need viable updates. The original Grand Archive ZIP is not available in this cloud workspace.

All three component updates must be viable before unified source integration. For each exact pushed commit, review its changes, scope, provenance, source integrity and meaningful executed checks. Record findings and coordinator approval separately from author-supplied claims. Root planning commits and checksum refreshes alone do not satisfy the deliverables.

Then select an App commit pinning exactly the approved Engine and Catalog commits. Test an isolated joined assembly, including compatibility, mechanics/privacy/recovery probes, evidence freshness and package integrity where affected. Fixes return to the owning component chat/repository. The coordinator updates `COMPONENTS.json`, the development inventory and source-matched qualification, then commits and pushes unified main after the set passes. Retain the prior working set if any component remains incomplete or fails.

`tools/check_integration_gate.py --engine /path/to/IRGS-Engine --app /path/to/IRGS-APP-WEB --catalog /path/to/IRGS-Catalog` reports readiness. `tools/sync_components.py --apply` refuses a set without matching approvals, a new update in each component and matching App pins. Dry-run/import tools never push. Advancing an independent component is not automatic integration.

Coordination guidance and QA reports may be published on joined main while the component set is held; those commits do not change the selected product sources. The QA watcher tests prospective pushed sets and reports results, but it neither qualifies a complete deliverable by itself nor moves integrated component pointers. Tests passing and integration approval are separate facts.

## Dispatch capability

The coordinator can list/read these existing chats and read/write the repositories. This cloud session has no send, steer or start-thread tool. These linked work orders are published directions; they have not been delivered as chat messages and do not start the idle chats. A chat must read its work order when resumed. No replacement chats or subagents have been created.

## Historical Details

Catalog owns a deterministic multipart preservation of the complete original archive, its source identity and provenance. Engine owns verification and read-only access; App owns Creator presentation and explicit readiness/error states. Full archive preservation includes the source database and assets, not only ten exposed structured collections. Reference storage creates no live campaign facts, new player knowledge or historical schedule.
