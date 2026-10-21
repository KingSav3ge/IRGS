# IRGS 3.3.C — Engine design and Claude handoff

**Edition:** C2 · 20 October 2026  
**Delivery status:** Text specification ready for implementation review  
**Runtime status:** No new engine activated  
**Foundation:** Selected IRGS Core 3.3

Codex develops the text of the engine. Claude implements and verifies it. Emergent's website and app development remains 3.3.E. The integration target is one authoritative world, with player and autonomous proposals resolved through Core and presentation drawn from committed results.

Start with [Claude handoff](CLAUDE_HANDOFF.md). The developed engine text is in [Core 3.3.C Engine Supplement](IRGS_Core_3_3_C_Engine_Supplement.md).

| Document | Purpose |
| --- | --- |
| [Engine supplement](IRGS_Core_3_3_C_Engine_Supplement.md) | Shared ownership, lifecycle, ordinary-action mechanics, certification, time and historical continuity. |
| [Action and dependency contract](ACTION_AND_DEPENDENCY_CONTRACT.md) | Typed requests, actual authority, effects and 22 proposed acceptance cases. |
| [Persistence and recovery contract](PERSISTENCE_AND_RECOVERY_CONTRACT.md) | Durable receipts, retries, crash boundaries, restore/fork safety and 16 proposed acceptance cases. |
| [Agency, time and presentation contract](AGENCY_TIME_AND_PRESENTATION_CONTRACT.md) | Shared-world institutional planning, information, calendars, presentation and 17 proposed acceptance cases. |
| [Institutional execution model](INSTITUTIONAL_EXECUTION_MODEL.md) | Concrete household, business, government and military policy procedures, with a shared-resource integration fixture. |
| [Timeline and process contract](TIMELINE_AND_PROCESS_CONTRACT.md) | Named time axes, precise frontiers, partial work, interruption and 18 proposed acceptance cases. |
| [Movement and observation contract](MOVEMENT_AND_OBSERVATION_CONTRACT.md) | Actual position/transit, accessible evidence, retained searches and 18 proposed acceptance cases. |
| [Dialogue and social action contract](DIALOGUE_AND_SOCIAL_ACTION_CONTRACT.md) | Communication, comprehension, NPC responses, offers/agreements and 18 proposed acceptance cases. |
| [Playable action cycle](PLAYABLE_ACTION_CYCLE.md) | One integrated synthetic journey from observation through interrupted work and payment, with 12 proposed acceptance cases and a companion fixture. |
| [Implementation packets](IMPLEMENTATION_PACKETS.md) | Bounded coding scopes, dependencies, stable interfaces and the evidence Claude should return. |
| [Claude handoff](CLAUDE_HANDOFF.md) | Reading order, field/status reconciliation, implementation milestones and required return evidence. |
| [CMRR and acceptance register](CMRR_AND_ACCEPTANCE.md) | Source conflicts, preserved behaviour, dispositions and exact status of all 121 design cases. |
| [C2 change record](CHANGES_C2.md) | Additions, clarifications, compatibility and preserved C1 requirements. |
| `HANDOFF_STATE.json`, `ACCEPTANCE_CASES.json` | Machine-readable packet and acceptance indexes; no execution claims. |
| `reference/` | Unchanged source Core/binding/master and input hashes; reference status remains explicit. |

The supplied C archive contains nested packages, with 57 runtime Python files matching the selected engine. The E archive contains Emergent's active lightweight backend and preserved Codex sources. Compatible E work can be adapted to the engine contract; its presence does not prove Core integration.

The first coding milestone is durable typed action execution using existing Military equipment issue and Roman delegated activity booking. Later milestones bind real elapsed time, ordinary first interactions and four autonomous institutional planners to that same world. Equipment transfer, a scheduled activity, completed work and presented prose remain different outcomes.

The 121 cases are requirements for Claude to prove. They are not passed tests. The original C1 archive remains available as the previous design edition; C2 preserves its 55 case IDs and adds 66. This package contains text and source references, with no executable runtime, user saves or inactive coding draft. The existing live release remains selected until a coded successor is qualified and adopted.
