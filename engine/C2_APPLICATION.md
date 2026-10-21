# IRGS engine 3.3.3.E — C2 application

**Text-engine revision:** 3.3.3.E  
**Applied design:** C2 · 20 October 2026  
**Foundation:** Selected Core 3.3  
**Status:** Applied engine text; implementation and verification outstanding.

This edition incorporates the complete inherited engine and C2's developed rules into one specification. The application changes engine text, not executable handlers, numerical model adoption, live campaign bindings or deployment status. The user's latest direction returns attention to overall IRGS development rather than a separate handoff workstream.

The supplied 3.3.3 package is the current packaging baseline. Its 274 assembled payload files, including all 57 runtime Python files and the complete Core text, match the verified predecessor source. This application is based on the existing 3.3.3.E branch at a906b3316712d4f7902bb611eaccf2fc6dd0cf73 and preserves all seven files in that engine branch, including its deliberate omission of the Live/App ZIP.

## Current development designations

The user's current designations are **3.3.3.E for Engine/Core** and **3.3.3.A for App/Web**. Earlier C2 source documents used 3.3.C for the engine and 3.3.E for the application. Those original documents remain immutable historical references. In the consolidated applied engine, designation prose is relabelled to the current names; hashes continue to identify the original source documents. Historical package filenames and actual Core binding versions retain their original identities.

Publication uses the current Engine/Core branch as its parent and preserves its deliberate package split. The App/Web branch's separate package selection is not changed by an engine update.

## How to use this edition

Read the application decisions below, the inherited Core, then the applied C2 chapters. The complete source contracts remain separately available under `design/C2/` for implementation requirements and acceptance evidence. The binding and application record identify exact versions and hashes.

The inherited source is retained in full. Its release notes describe the then-current local implementation; its candidate sections describe their original source status. They do not activate or repeal mechanics merely by appearing in this branch. C2 specializes the proposed action, information, time, dependency and recovery contracts while retaining all existing owners and supported campaign scopes.

## Reconciled application decisions

| Subject | Meaning in 3.3.3.E |
| --- | --- |
| Authority/version labels | The selected live foundation is Core 3.3. Inherited phrases saying Core 3.2 remains selected, R7/R8 are unselected, or a historical next priority is pending describe their original source editions. They do not redirect this branch to an older active binding. |
| Declaration-only runtime | The existing `declared_not_resolved` behaviour remains an honest runtime limit. C2's consequential actions are now engine-text requirements for implementation; their inclusion is not evidence that the current runtime performs them. |
| d100 and other adapters | Preserve the inherited default/reference adapter and explicit campaign overrides within their already recorded scope. C2's statement that it adopts no new universal dice does not repeal inherited scope or globally activate d100/genre values. Do not invent an adapter where the current campaign's binding leaves the dependent mechanism unresolved. |
| Dependency instrumentation | Old conservative list reservations and manually declared footprints remain historical implementation descriptions. C2 requires execution-derived authorization, decision, prerequisite and effect observations, with actual list-read/mutation distinction and case-specific evidence. |
| Ownership | Keep the nine K-owners and established domain workflows. No application, planner, view or persistence index becomes a second authority for the same people, stock or history. |
| Lifecycle | The C2 supplement's phase/parent meanings and separate submission/attempt receipts govern the new design. Map old status labels explicitly; scheduling is not completed work and a later phase is not a replay of its booking. |
| Time | Causal sequence, storage revision, elapsed time, civil date, information time and wall-clock execution remain distinct. C2 supplies no automatic conversion or unrecorded historical opening hour. |
| Information and speech | NPC agency can propose wording before Core commits an utterance. Player-facing narration describes committed effects and permitted receipts. Neither route can write arbitrary world truth or expose hidden validation facts. |
| Search repetition | An accepted-phase retry or redisplay causes no new work. A new physical search may use supported attention/time; it cannot regenerate established stock or automatically reroll retained uncertainty. |
| Historical continuity | New dated worlds load verified snapshots; continuing worlds use actual committed state. Historical references are not mandatory future occurrences, and absent entities do not resurrect. |
| Fixture values | C2's times, parcels, funds, mandates and bay policies are explicitly synthetic test selections, not historical rates or campaign-wide defaults. |
| Acceptance | The 121 cases and seven packets are implementation requirements. No new runtime, calibration or playtest result is asserted by applying the text. |

If a live campaign's selected rule conflicts with a proposed new mechanism, preserve the selected rule until an explicit compatible adoption bridge is qualified. Do not retroactively reinterpret accepted actions, processed spans, injuries, resources, knowledge, agreements or obligations.

## Consolidated chapter map

The generated engine document contains explicit anchors for the inherited Core and each applied chapter:

- `inherited-core-3-3`
- `c2-shared-engine-contract`
- `c2-actions-and-dependencies`
- `c2-persistence-and-recovery`
- `c2-agency-and-presentation`
- `c2-institutional-execution`
- `c2-timeline-and-processes`
- `c2-movement-and-observation`
- `c2-dialogue-and-social-actions`
- `c2-playable-action-cycle`

The original Core, C2 contracts, acceptance inventory and handoff remain separately traceable. Relative source links, heading depth and current development designation prose are adapted for consolidation; the inherited clauses and C2 rules remain complete. The application record discloses those editorial transformations.

## Incorporation audit

[C1/C2 incorporation register](C1_C2_INCORPORATION.md) records existing foundations, partial coverage and missing implementation. The original package references C2 without applying its chapters to the Core or implementing the general action cycle. This edition supplies the missing engine text; the register does not relabel proposals as working software. Engine and application development now proceed together on 3.3.3.E and 3.3.3.A respectively.
