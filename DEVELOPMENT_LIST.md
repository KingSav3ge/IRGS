# IRGS continuation development list

Maintained in **KingSav3ge/IRGS-Engine**, updated 2026-10-22. The stable DEV IDs originated in **3.3.3 Unified Development D1**. Selected executable Core: **3.3**. Publish Engine increments to this repository's `main` branch. This list defines completion criteria; it does not adopt new mechanics or certify unfinished capabilities.

The immediate target is a complete Solo action cycle: a player makes a supported decision, the engine commits its legitimate consequences, the player sees the outcome, and play can continue after reload. Complete that cycle before widening the historical catalogue or adding interface sections.

DEV-01–DEV-04 are completed for the qualified bounded equipment action. DEV-05 is completed as an operation inventory with scoped execution evidence and explicit gaps; all other items remain open. DEV-06–DEV-08 are the next priority, with partial collection and rejected-path implementations already present. Authored local scenes, Rise work and dated starts also advance portions of later tasks without completing them. See [ROADMAP.md](ROADMAP.md) for the completed/in-progress/remaining summary and [CONTINUATION_STATUS.md](CONTINUATION_STATUS.md) for scope, evidence and limitations. Existing App setup, filtered inspection, request recovery and campaign Trash are integration foundations in the App repository. Applied C2 text contains 121 required cases; the scoped execution ledger does not claim full completion.

## 1. Deliver the first consequential action

**Depends on:** the current D1 baseline. **Deliverable:** one working path through the engine and Solo app.

- [x] **DEV-01 — Define the supported action.** Use the existing authorized equipment-issue operation as the first candidate. Identify the acting character, actual control, issuing institution, recipient, established stock and selected rule. Qualify it in a synthetic fixture before exposing it in eligible campaigns. Do not invent historical stock or permissions to make it available.
- [x] **DEV-02 — Connect intent to execution.** Link the exact accepted request to the existing handler, its authorization and decision reads, allocation, atomic effects, outcome and receipt. Ambiguity, absent rules and missing facts require an explicit unresolved status. Preserve unsupported declarations without presenting them as completed actions.
- [x] **DEV-03 — Make the result durable.** Persist the accepted identity, committed outcome and receipt together. Retrying or reloading retrieves the original result without issuing equipment twice. Keep the submission acknowledgement separate from the current action status.
- [x] **DEV-04 — Complete the Solo round trip.** Show the legitimate outcome and changed character/world view, clear the appropriate pending state, and allow a second action. Expose this capability only where its real prerequisites and the player's control support it.

**Completion evidence:** a supported action changes conserved stock correctly; unauthorized, revoked, depleted and conflicting attempts leave no partial effects; actual permission/resource dependencies are observed; retry and reload do not duplicate effects; a second supported action works. The app accurately distinguishes saved intent, unresolved requirements and committed outcome.

## 2. Certify dependencies across supported operations

**Depends on:** first-action evidence from stage 1. Basic dependency checks are required in stage 1, not deferred until this stage.

- [x] **DEV-05 — Build an operation coverage register.** For every claimed supported handler, record its implementation, affected owners, actual reads and writes, authorization/decision paths, tests and known limits. Mark unqualified paths explicitly.
- [ ] **DEV-06 — Improve collection observation.** Distinguish list inspection from mutation while retaining coverage for absent records, scans, membership changes and order-sensitive decisions. Keep conservative reservations where finer observation is not yet justified.
- [ ] **DEV-07 — Qualify conflicts and failed paths.** Exercise revocation, dissolution, changed prerequisites, exhausted resources, shared capacity and competing claims. Confirm that failed or deferred decisions retain the dependencies that influenced them.
- [ ] **DEV-08 — Verify cross-engine execution.** Compare valid event orders and simultaneous frontiers across multiple adapters using the same people, stock and capacity. Demonstrate agreement for genuinely independent operations and safe handling of conflicts without arrival-order allocation.

**Completion evidence:** named operations and branches have reproducible coverage. Certification claims state their actual scope. Manually declared footprints and one successful execution are insufficient evidence.

## 3. Support durable phases, elapsed work and recovery

**Depends on:** stage 1's durable action identities and qualified dependencies for each process being added.

- [ ] **DEV-09 — Implement phase identities and receipts.** Distinguish a submission, its scheduled work, each continuation phase, phase outcomes and current status. A scheduled parent remains nonterminal; continuing a process must not book it again.
- [ ] **DEV-10 — Implement supported elapsed processes.** Track processed spans, reservations, interruptions and resource use through the existing owners. Keep storage revision, causal order, elapsed time, civil date and information times separate. Use only supported durations and rates.
- [ ] **DEV-11 — Fence restart and restore.** Serialize competing recovery attempts and prevent discarded future receipts from replaying effects onto a restored branch. Define how a player resumes, interrupts or cancels supported work and sees its remaining commitments.

**Completion evidence:** stop/resume, duplicate delivery, concurrent retry, interruption and restore cannot duplicate stock, payments, work, bookings or knowledge. Equivalent supported elapsed spans reconcile without inventing an opening hour or a universal action duration.

## 4. Add movement and observation through the shared cycle

**Depends on:** stages 1–3 for any action that consumes time or reserves capacity.

- [ ] **DEV-12 — Resolve supported movement.** Establish actual location, route/access facts, movement conditions and justified elapsed progress. Ordinary supported walking must not acquire an invented difficulty roll.
- [ ] **DEV-13 — Resolve observation and search.** Separate existing receipt retrieval from a new physical investigation. A new search requires supported time and conditions; retry cannot reroll, regenerate stock or repeat work.
- [ ] **DEV-14 — Preserve the character's knowledge.** Deliver only information legitimately received or perceived. Keep uncertainty, source and information timing; hidden validation facts must not enter the player view.

**Completion evidence:** location and knowledge changes are committed through the same world. Interrupted movement/search, retry and changed access behave correctly, and another actor cannot inspect hidden facts through the interface.

## 5. Add dialogue, offers and obligations

**Depends on:** stage 1's shared action/result path and stage 3 wherever timing or continuation applies.

- [ ] **DEV-15 — Establish speech and testimony records.** Distinguish a speaker's words, claims, beliefs and the listener's received information from objective world truth. Character background statements do not automatically establish assets, skills or authority.
- [ ] **DEV-16 — Implement proposals and acceptance.** Give offers, counteroffers, authorization, acceptance and obligations their own statuses. Revalidate actual authority and resources before a binding consequence; a promise alone does not transfer property or complete work.
- [ ] **DEV-17 — Ground character responses and narration.** NPC decisions propose authorized actions through Core. Present committed facts and legitimate information after resolution, with no independent narrator state or arbitrary truth writes.

**Completion evidence:** contradictory testimony, rejected or withdrawn offers, authority changes and duplicate acceptance retain correct meanings without duplicated effects or hidden-information leakage.

## 6. Qualify historical setup and the evolving world

**Depends on:** existing dated setup; use the qualified action and phase paths for new changes during play.

- [ ] **DEV-18 — Verify the 1415 playable opening.** Check that its detailed description, dated characters/factions, selected scenario, actual control and available actions agree with the established starting state. Keep unsupported opening facts explicit.
- [ ] **DEV-19 — Verify continuing-world availability.** Test formation, dissolution, succession, allegiance, territorial change and loss of control against committed simulation state. A historical template must not revive a collapsed polity or replace a simulated ruler.
- [ ] **DEV-20 — Complete eligibility and setup regressions.** Keep existence, participation, playability and control separate for both characters and factions. Preserve entry point → scenario → character/faction selection or creation → review → atomic campaign creation. Retain all 37 catalogue entries with accurate readiness and evidence limits; deepen dated starting facts without inventing unsupported operational state.

**Completion evidence:** a fresh historical start and a continuing playthrough at the same date can legitimately offer different choices. Neither setup nor reload creates a characterless game or silently resets world history.

## 7. Extend autonomous institutional execution

**Depends on:** qualified shared actions, dependencies and durable elapsed phases for the operations each institution uses. Extend the existing bounded synthetic foundations.

- [ ] **DEV-21 — Establish recurring institutional reviews.** Give households, businesses, government and military institutions scoped observations, real decision authority, review conditions and retained plans. Plans propose actions through Core rather than writing effects directly.
- [ ] **DEV-22 — Run competing institutions in one world.** Make reviews use the same actors, stock, workplaces, assets, capacity and commitments. Include scarcity, changed authority, interrupted work and unfulfilled obligations.
- [ ] **DEV-23 — Qualify sustained operation.** Compare continuous and save/resume runs, and equivalent supported coarse/fine elapsed advancement. Reconcile resources and unresolved commitments over longer synthetic periods. Document fixture rates and review policies separately from historical calibration.

**Completion evidence:** all four institutional categories advance through shared ownership without duplicate resources, retrospective permissions or separate simulated states. Historical realism remains a separate evidence claim.

## 8. Maintain honest Solo behaviour and release evidence

**Depends on:** each implemented increment. These are continuing requirements, not work to postpone until all other stages finish.

- [ ] **DEV-24 — Track executable acceptance evidence.** Extend [the scoped execution ledger](engine/ACCEPTANCE_EXECUTION.md) with implemented capabilities, relevant C2 case IDs, test locations, actual results and limitations. Preserve the immutable 121-case design inventory; distinguish required, implemented, tested and qualified scope.
- [ ] **DEV-25 — Keep the Solo interface truthful.** Track this as an App-owned integration requirement: preserve the preferred design while showing saved declarations, awaiting requirements, active work, interruptions and completed outcomes accurately. Engine results must support filtered knowledge and truthful status. Interface, character creation, recoverable Trash and launcher changes belong in IRGS-APP-WEB. Co-Op stays deferred.
- [ ] **DEV-26 — Qualify each delivered increment.** Run relevant Engine runtime checks, refresh affected Engine source pins and verify this component. Host/interface checks belong to the App workstream; qualify the pinned pair when integration is requested. Package and smoke-test an extraction before calling it a distributable version. Keep existing saves outside development fixtures; use an explicit compatibility/migration plan before applying new mechanics to them.
- [ ] **DEV-27 — Publish and report Engine capabilities.** Commit and push verified Engine changes to `KingSav3ge/IRGS-Engine` on its `main` branch. Maintain completed, in-progress and remaining work here. Keep Catalog development, App dependency updates and joined IRGS publication in their own workstreams. Report implemented scope, supporting evidence and remaining limits without implying that all C2 requirements or a connected App feature are complete.

**Completion evidence:** each delivered capability has an accurate status, reproducible tests and a clean distribution. Engine-only or app-only progress does not claim an end-to-end feature until the connected cycle works.

## Current playable-opening increment

Opening1 advances DEV-10, DEV-12–DEV-14, DEV-18 and DEV-25 with an optional reviewed fictional 1415 delivery scene. Local movement, observation, failed attempts, stock transfer and elapsed seconds have durable outcomes. These broad tasks remain open: there is no interruption/phase scheduler, hidden search, dialogue, combat or autonomous NPC response. See [the implementation record](engine/PLAYABLE_OPENING_IMPLEMENTATION.md) and OPENING1_VALIDATION.json.

## Start here

Completed: **DEV-01–DEV-04**, including their bounded dependency, recovery and acceptance checks. DEV-05 now records 85 operation spellings across 170 backend/operation contracts. Next extend the named collection, failed-path and cross-engine cases under **DEV-06–DEV-08**, using [the coverage register](engine/OPERATION_COVERAGE.md) to choose gaps. The reviewable result is a supported equipment action with real consequences, a durable result visible in the Solo app, and a working next action. This is the first continuation milestone; no new live-version designation is assigned by this list.

Use [ROADMAP.md](ROADMAP.md) for the broader sequence, [DEVELOPMENT.md](DEVELOPMENT.md) for working and verification commands, and [the preserved D1 check summary](provenance/D1_validation/CHECK_SUMMARY.json) for historical D1 evidence. This list records continuation progress; supporting execution evidence is linked separately.

## Core consolidation and rejected dependencies

The 2026-10-22 increment advances named DEV-07–DEV-08 paths, keeps verified rejected-probe reads with unresolved requests, consolidates domain routines inside Core and restricts technical configuration to Creator mode. It also corrects independent environment findings IRGS-QA-001 and IRGS-QA-002. The broader milestones remain open; see `engine/CORE_CONSOLIDATION.md`, `engine/REJECTED_DEPENDENCIES_IMPLEMENTATION.md` and `DEPENDENCY_REJECTIONS_VALIDATION.json`.

## Completed reference integration — historical-reference-1

Attached the supplied Grand Archive 1.1 through an external, read-only source provider and a Creator-only search/detail interface. Preserved record identity, source qualifications, uncertainty and rights metadata; local attachment configuration and mixed-rights payload remain outside published source. See HISTORICAL_REFERENCE_VALIDATION.json. This completes reference browsing only; adopting sourced starting facts, resolving historical identities and wider C2 certification remain separate work.

## Historical Details — historical-details-01

Completed the Engine reader increment: pinned manifest/part verification, exact reconstruction into an ignored installation cache, atomic publication/retry, bounded failure codes, ten-collection binding validation and unchanged source-row identity through the existing reference API. Explicit local ZIP attachment remains supported. See [the API and cross-component contract](engine/HISTORICAL_DETAILS_API.md).

The subsequent delivery increment verifies Catalog `58ce55672bdd75076b94882bd8715a1d2a1f383a`: 32 actual parts reconstruct the original archive, and all ten reader collections match their pinned record counts. It adds deep verification and a repeatable qualification command, plus stricter portable-path, link and exact part-directory checks. App's reviewed dependency pins and coordinator integration remain separate gates. This reference verification does not complete DEV-06–DEV-08 or establish historical truth.

## Staged AI provider foundation — AIP-01–AIP-09

Read [the Engine provider plan](engine/AI_PROVIDER_PLAN.md) for all nine open requirements, AIP-S1–S4 sequencing and the 16 unexecuted model-evaluation cases. Preparation is complete; provider implementation is not started. Historical Details integration, supported gameplay and DEV-06–DEV-08 retain priority. The first provider increment uses a disabled-by-default registry, scoped contracts, fake transport, validation and attempt ledger before one reviewed opt-in direct adapter. No credentials, budget, entitlement, paid calls, model-quality winner or new authoritative owner is supplied by that plan.

## Kira atlas reference delivery

The [six-region atlas](IRGS_3_3/catalog/campaigns/kira/atlas/README.md) adds the creator-requested maps and companion regional foundations to Kira’s existing world files. The atlas manifest and checksums identify the delivered artwork; component verification pins it with the rest of the Engine content. No DEV gameplay milestone is completed by this reference addition. App dependency updates and joined publication remain separate workstreams.
