# IRGS development guide — 3.4.5

This update adopts the user-requested continuous story UI. Actor-received entries
and committed results read from oldest to newest on one surface. Current choices
and the retained editable response form follow the newest entry in the same scroll
area. Exact source text, status, provenance, drafts and explicit review/recovery
remain. Rise no longer displays only twelve receipts; completed process records
and source details remain available without crowding the tale.

Engine and Catalog runtime/data match the qualified 3.4.4 source. Their release
updates align edition metadata and development instructions. This UI adoption and
its guide refresh do not implement new mechanics or close functional Alpha gates.
All four editions are 3.4.5; previous_version remains 3.3.3; next unified push is
3.4.6. Preserve original archives, accurate evidence, saves and personal settings.

| Owner | Next implementation | Required handoff |
| --- | --- | --- |
| Engine | A4-ENG-03 supported-intent DTOs; ordinary offer prerequisites | Explicit supported/unsupported review and immutable execution/retry in two ordinary contexts including non-Rise; no invented consent |
| App | A4-APP-01 protected operator/provider setup, then A4-APP-03 intent review | Server-side configuration, finite budget, exact eligible route and non-secret readiness; preserve chronological story and drafts |
| Catalog | A4-CAT-04 grounding rubric and independent ordinary journeys | Actor inputs separate from evaluator truth; exact source selections, actual committed consequences and explicit unmet systems |

World Builder remains a shared contract/editor/original-pack track under
WORLD_BUILDER_PLAN.md. The shared Alpha plan and stable DEV/C2 IDs remain active.
Broader NPC/institution decisions, needs/recovery, selected conflict, sustained
AI play, native Windows and live-provider quality qualification remain open.
Historical Details is complete. The watcher retains QA reports while its process
runs; it does not wake idle chats, integrate source or reload a host.

## Coordinator workflow

Read AGENTS.md and COORDINATION.json; preserve local edits, fetch correct origins and fast-forward clean checkouts only. Review exact published component commits, committed App dependency pins and actual product differences. Use tools/check_integration_gate.py and tools/sync_components.py --apply with coordinator approvals. Fresh operation capture, full joined regression, relevant real browser/independent Catalog checks and a clean extracted package are required before publishing. Every unified main push increases the edition. Never reset user work, open private saves or relabel historical logs as newly executed checks.

Use Python 3.12+ without -O and Node 20+. tools/verify_development.py verifies source; tools/build_operation_register.py --check engine/qualification/operation_register.json verifies current execution evidence. Refresh hashes only after intentional edits; hashes are not tests. Keep generated QA outside source and use tools/package_development.py/tools/smoke_development.py for the clean distribution. Stop/restart only proven owned stale hosts and verify running build fingerprints after an update.
