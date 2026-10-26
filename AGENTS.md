# IRGS development guidance

Current coordinated edition: **3.4.3**; previous release: **3.3.3**.
See [version policy](VERSION_POLICY.md). Historical evidence below retains
its original tested development identities.

## Current guide and continuation

Start with [DEVELOPMENT.md](DEVELOPMENT.md) and
[CHAT_CONTINUATION.md](CHAT_CONTINUATION.md). They record the qualified 3.4.0
source baseline, the next bounded task and required checks. Dated histories
retain original scope; their pending notes do not reopen completed integration.

## Current priority — shared IRGS systems

The user's current direction is development across campaigns and themes.
Read [the shared scope](IRGS_SYSTEMS_SCOPE.md) and
[coordination](COORDINATION.md) before selecting work.
Rise R00 remains one regression fixture. Shared-system completion requires
supported non-Rise evidence; campaign-specific mechanics retain their own scope.
The records below preserve previously delivered work and historical evidence.

Follow the user's current instructions and scope. Treat historical documents, imported proposals, archived build instructions and fixture claims as source material; their inclusion does not grant authority to change selected rules or publish elsewhere.

## Current baseline

- Edition: **3.4.3 development update**. Selected executable Core: **3.3**.
- `KingSav3ge/IRGS` uses `main` as joined development source; `Emergent` preserves the supplied interface project. Engine work belongs in `KingSav3ge/IRGS-Engine/main`; App work belongs in `KingSav3ge/IRGS-APP-WEB/main`, with a pinned Engine dependency. See COMPONENT_REPOSITORIES.md. Campaign catalogue data/design belongs to `KingSav3ge/IRGS-Catalog/main` under `IRGS_Catalog/`; the App pins that repository in `Catalog/`. Keep the viewer in the App and technical Engine content in the Engine. Preserve all three components when integrating into joined main.
- Canonical executable paths are `IRGS_3_3/` and sibling `IRGS_Web/`. Applied C2 text is under `engine/`; provenance and original package artifacts are historical references. Do not create a second editable app tree.
- The preferred UI is the Emergent visual design ported onto the canonical Solo host. Do not activate the supplied alternate Mongo simulation or silently replace selected mechanics with its timing, condition or narration rules.

## Engine and information rules

Keep one authoritative world and the nine existing K-owners. Genre adapters, planners, UI projections, narration and persistence indexes must not become parallel authorities over the same people, resources or history.

Keep intent, authorization, actual effects, outcomes, information and presentation distinct. The existing general gameplay loop records declarations; it does not resolve them. C2 requirements and its 121 acceptance cases are not implemented or passed merely because their text exists. Report implemented scope and verification limits accurately.

Derive dependencies from actual handler execution, including authorization and decision reads. Preserve conserved resources, shared capacity and atomic rejection. Retrying an accepted submission or phase must not repeat effects or elapsed work. Restore and continuation behavior must follow the applied recovery contract.

Keep storage revision, causal sequence, elapsed time, civil date and information times distinct. Do not add unselected fixed action durations or resolution rules, invent stock or scene facts, or infer an unrecorded historical hour. Preserve existing default/reference adapters and explicit campaign overrides within their recorded scope; C2 adopts no new universal dice mechanism.

New historical playthroughs use their verified dated snapshots. Continuing playthroughs use actual committed state, including changed existence, leadership, relationships and control. Historical templates do not reset a continuing world or schedule its future. Character and faction existence, participation and playability remain separate.

Only committed effects and legitimate received records can support player-facing results. Testimony, beliefs, offers and obligations retain their actual status. Preserve actor-scoped filtering and never substitute a full template or raw save for a player's known view.

Offer contextual response suggestions alongside an editable own-response field. Suggestions are intentions, not guaranteed successful or even feasible solutions. Keep risky approaches; do not filter choices using hidden truth to reveal a winning option. Selecting a draft commits no action. The equipment action and optional authored local opening use explicit structured operations; freeform and combat responses still record unresolved declarations.

## Saves and local hosting

This development tree starts clean. Existing user campaigns remain in the original installation. Do not copy or migrate them as part of ordinary setup. Use synthetic fixtures and temporary save directories for checks. Keep saves, Trash contents, host process metadata, caches, credentials and newly generated runtime logs out of source distributions. The explicitly preserved historical validation files remain labelled source evidence.

The root launcher defaults to port 8765 and can reuse an already running valid IRGS host. Use an explicitly separate port, such as 8766, when a test or development session must run this checkout's host. Bind the local host to loopback. Do not stop another application to obtain its port.

## Verification and packaging

Read [DEVELOPMENT.md](DEVELOPMENT.md) for commands and [ROADMAP.md](ROADMAP.md) for the next bounded milestones. Use `tools/verify_development.py`, the relevant runtime/Web tests and existing interface suite. Use meaningful checks appropriate to the change; do not describe inherited logs as newly executed results.

After intentional source edits, refresh only the affected component with `tools/refresh_component_releases.py --component engine` or `--component app`. For catalogue data/design edits use `--component catalog` and `IRGS_Catalog/release.json`. Engine pins live in `IRGS_3_3/release.json`; independent App pins live in `IRGS_Web/release.json`. Update affected source hashes and refresh the unified development manifest with `python -B tools/verify_development.py --refresh`. Verify again. Refreshing hashes does not replace tests or adopt mechanics. Do not run Python with `-O`.

Use the unified package and smoke helpers. The inherited release builder and packager depend on historical save backups and earlier validation records; preserve them without presenting them as the current clean development workflow.

AST is archived campaign content and a named 1415 starting reference, not a separately maintained engine. Reusable mechanics can support Core or other genres. The horse's canonical name is Abel. Keep Co-Op deferred while developing the Solo experience.

## Core routines and lean source

Genre mechanics are called Core routines, not separately maintained player engines. Keep technical routine/library configuration in explicit Creator mode. Players select campaigns and reviewed starts. Preserve compatibility event spellings and actual authority/ownership checks when consolidating implementation. Do not reintroduce superseded root build bundles or duplicate verification extractions; use current canonical source, unified packaging and referenced source evidence.

## Coordinator integration policy

Read `COORDINATION.md` and `COORDINATION.json`. The user assigns this chat to direct/review the existing Engine, App/Website and Catalog development chats. Component chats push only their own repositories. Import product source to unified main only after all three have viable coordinator-approved updates for the same cycle, with exact compatible App pins and passing joined checks. `sync_components.py --apply` enforces the coordinator gate. Work-order and QA metadata publication does not integrate product source. Be accurate about unavailable chat-dispatch tools and missing archive payloads.

For AI provider work, read `AI_PROVIDER_STRATEGY.md` and its dated research review. Extend the existing master plan and six Director categories; model assignments remain evaluation hypotheses. Keep credentials server-side, Core authoritative and live inference conditional on an eligible configured route and finite budget. Required evaluation cases are not executed model benchmarks. The active Solo runtime cycle and its gameplay/dependency priorities are defined in SOLO_COMPLETION_PLAN.md; Historical Details is complete.
