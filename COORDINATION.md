# IRGS development coordination

The user assigns **IRGS Enviroment** as coordinator and reviewer for three development chats. Each component chat owns its repository; the coordinator publishes qualified combined source to `KingSav3ge/IRGS/main`.

| Development chat | Repository | Current assignment |
| --- | --- | --- |
| IRGS Engine | [IRGS-Engine](https://github.com/KingSav3ge/IRGS-Engine) | [Verified Catalog multipart reader](https://github.com/KingSav3ge/IRGS-Engine/blob/main/COORDINATOR_WORK_ORDER.md) and continuing dependency qualification. |
| IRGS App/Website | [IRGS-APP-WEB](https://github.com/KingSav3ge/IRGS-APP-WEB) | [Creator Historical Details browser](https://github.com/KingSav3ge/IRGS-APP-WEB/blob/main/COORDINATOR_WORK_ORDER.md), compatible component pins and App plan. |
| IRGS Catalog | [IRGS-Catalog](https://github.com/KingSav3ge/IRGS-Catalog) | [Complete archive multipart payload](https://github.com/KingSav3ge/IRGS-Catalog/blob/main/COORDINATOR_WORK_ORDER.md) under Historical Details, with provenance and a Catalog plan. |

## Current cycle

`historical-details-01` is assigned, not complete. `COORDINATION.json` records baseline commits, thread identities, review status and blockers. The last integrated component set remains selected in `COMPONENTS.json`. Engine's multipart reader, App's reference recovery and Catalog's packaging/intake tools are now published candidates. Fresh scoped checks passed on 22 October; full source review and integration approval remain pending. Catalog identifies the original ZIP on Drive, but its manifest still reports missing source bytes and contains no archive parts.

| Candidate product change | Fresh coordinator checks | Remaining release condition |
| --- | --- | --- |
| Engine `f64ef3132c363925739acbda1e8421fbd4b4642f` | Integrity and 65 historical-reference/plan tests passed. | Full source review and full archive/compatible App qualification. |
| App `02d260e80ee62c90d3563e0c063460f97eeec99c` | Integrity, 10 reference HTTP tests and 72 synthetic interface checks passed. The 10 cases also passed with prospective Engine/Catalog overrides. | Pin exact approved dependencies; actual multipart and broader joined qualification. |
| Catalog `ab3e127f4a0bc504158fd91617e4f76fef5a2f7d` | Integrity and 30 synthetic packaging/intake tests passed. | Complete source payload and actual round-trip verification; metadata is not the archive. |

The exact tested published commits include the subsequent provider work-order additions and are recorded in [the scoped review](provenance/qa/component_review_2026_10_22.json). Process-only dependency overrides did not change App pins. No full runtime/Web suite or manual browser run is claimed for this coordinator follow-up.

All three component updates must be viable before unified source integration. For each exact pushed commit, review its changes, scope, provenance, source integrity and meaningful executed checks. Record findings and coordinator approval separately from author-supplied claims. Root planning commits and checksum refreshes alone do not satisfy the deliverables.

Then select an App commit pinning exactly the approved Engine and Catalog commits. Test an isolated joined assembly, including compatibility, mechanics/privacy/recovery probes, evidence freshness and package integrity where affected. Fixes return to the owning component chat/repository. The coordinator updates `COMPONENTS.json`, the development inventory and source-matched qualification, then commits and pushes unified main after the set passes. Retain the prior working set if any component remains incomplete or fails.

`tools/check_integration_gate.py --engine /path/to/IRGS-Engine --app /path/to/IRGS-APP-WEB --catalog /path/to/IRGS-Catalog` reports readiness. `tools/sync_components.py --apply` refuses a set without matching approvals, a new update in each component and matching App pins. Dry-run/import tools never push. Advancing an independent component is not automatic integration.

Coordination guidance and QA reports may be published on joined main while the component set is held; those commits do not change the selected product sources. The QA watcher tests prospective pushed sets and reports results, but it neither qualifies a complete deliverable by itself nor moves integrated component pointers. Tests passing and integration approval are separate facts.

## Dispatch capability

The coordinator can list/read these existing chats and read/write the repositories. This cloud session has no send, steer or start-thread tool. These linked work orders are published directions; they have not been delivered as chat messages and do not start chats. A chat must read its current work order when resumed. On 22 October the coordinator observed all three chats active after user resumption. No replacement chats or subagents have been created.

## Historical Details

Catalog owns a deterministic multipart preservation of the complete original archive, its source identity and provenance. Engine owns verification and read-only access; App owns Creator presentation and explicit readiness/error states. Full archive preservation includes the source database and assets, not only ten exposed structured collections. Reference storage creates no live campaign facts, new player knowledge or historical schedule.

## AI provider development backlog

The user's provider assessment is reconciled in [AI_PROVIDER_STRATEGY.md](AI_PROVIDER_STRATEGY.md), extending the existing master specification without replacing its six-Director hierarchy or gameplay priorities. [AI_PROVIDER_REVIEW.md](AI_PROVIDER_REVIEW.md) records checked prices, conditions and unresolved claims. All three component work orders carry their relevant responsibilities. The [16 evaluation scenarios](provenance/qa/ai_provider_strategy/EVALUATION_CASES.json) are required but unrun; no model-quality result or paid service is implied.

Engine owns provider contracts, access enforcement, routing, validation and usage records. App owns server-controlled integration and developer presentation. Catalog owns content/provenance and processing-rights metadata. Start offline with fake transport and then qualify one opt-in direct integration. Historical Details remains the current integration cycle, with exact three-component approvals still required. Provider-planning commits do not satisfy that gate or complete archive delivery.
