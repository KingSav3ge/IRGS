# C1/C2 incorporation register — 20 October 2026

The supplied 3.3.3 package and current Engine/Core branch were compared with the preserved C1/C2 design. Status describes the inspected packaged implementation, before this text application. Existing code is credited for its actual scope. A matching concept or document reference is not evidence that the complete contract is implemented.

## Baseline and branch evidence

- Repository: KingSav3ge/IRGS. Existing engine branch: 3.3.3.E at a906b3316712d4f7902bb611eaccf2fc6dd0cf73; App/Web: 3.3.3.A. The unified repository's literal default branch is main, carrying the 3.3.3 package edition.
- Supplied IRGS-3.3.3.zip SHA-256: f1efda6c1747f5cba3c00f0983aac56ed4fc1deab31a208c7a59cea1f7e01c6c. Three nested package hashes and all 274 payload hashes matched the selected baseline. All 57 runtime Python files were unchanged.
- Packaged Core text SHA-256: dd80a3c59477fb24141b47cd8633ad70fb1aea637ce6a2f1a1cf70c2e4e63494. It does not contain the nine applied C2 chapters. Build instructions reference C2 packets and cases; those references do not apply or implement them.
- The inactive IRGS_3_3_C coding experiment was excluded. It is not the packaged or selected runtime and is not evidence of incorporation.

## Contract coverage

| Area | Coverage before application | Evidence and remaining work |
| --- | --- | --- |
| One authoritative world and nine K-owners | Present foundation | Core/binding and scoped Core apply/replay retain shared actors, resources and history. C2 retains these owners. |
| Observed dependencies and simultaneous frontiers | Partial C1 foundation | Runtime r9_runtime.py and dependency observer/frontier code observe handler access conservatively. This is more than manually declared footprints, but is not certification of all decisions, authorization, list reads versus mutations and new handlers across engines. C2 adds the required coverage and evidence contracts. |
| Consequential genre operations | Present, narrow | genre_receivers.py GENRE_OPS contains military_issue_equipment, roman_begin_delegated_activity and revoke_delegation. Supported transfers/bookings do not supply a general freeform action resolver or autonomous institution scheduler. |
| Player action cycle | Missing general resolution | core_world.py record_player_action records declared_not_resolved. r9_runtime.py rejects specialist-effect placeholders. C1/C2 require linked authorization, attempt, actual effects, outcome and receipt phases. |
| Durable requests and retry | Partial C1 foundation | IRGS_Web/server.py gameplay_request retains identities, payload digests and saved results; action_result separates current withdrawal status from saved acknowledgement. C2's per-phase receipts, restore fencing and cross-worker recovery remain to be implemented and qualified. |
| Agency, knowledge and presentation | Partial C1 foundation | IRGS_Web/gameplay_views.py filters actor-scoped records and explicitly reports action_resolution, narrator and time_advance false. C2 requires controlled proposals, committed speech/information and result-grounded presentation. |
| Temporal existence, eligibility and control | Present foundation, future adapters partial | Dated historical setup and live registry availability distinguish initial templates from actual campaign state. C2 continuations must preserve that distinction while effects, leadership and control change. |
| Timeline, process spans and capacity allocation | C2 text missing; general execution missing | Existing causal counters/bookings do not supply elapsed-span processing, exact reservation clipping, joint allocation decisions or recoverable calendar scheduling. The C2 timeline/process contract supplies these requirements without inventing time conversions. |
| Movement, observation and retained uncertainty | C2 text missing; general execution missing | No general movement/observation action adapters are connected to player declarations. Apply C2 support for ordinary movement, physically supported search and retained observations without artificial rolls or regenerated stock. |
| Dialogue, offers and obligations | C2 text missing; general execution missing | Setup testimony and received records already preserve evidence status. General dialogue/social actions still require supported communication, authority, offer/acceptance and obligation effects under the C2 contract. |
| Autonomous institutional execution | Missing general scheduler | A delegated activity booking is not a complete household/business/government/military decision cycle. C2 requires recurring reviews and authorized phases inside the same world. |
| Acceptance evidence | Inventory present as design source | C1's 55 cases are preserved within C2's 121. All remain required, not executed. Source-reported old checks cannot certify the new phases. |

## Application disposition

The complete inherited Core is retained, and all nine C2 chapters are now incorporated in the consolidated engine text. Existing implementation foundations are preserved; missing adapters, durable phase execution and acceptance evidence remain explicitly open. This application neither replaces working handlers nor describes proposed mechanics as live software.

The next implementation milestone is a single consequential action using actual authorization, observed dependencies, atomic effects and recoverable receipts, exposed through the app with accurate status. Subsequent movement, dialogue, process and autonomous review adapters must meet the same contract rather than establish separate worlds. The existing synthetic playable-cycle fixture is the cross-domain target, not a claim of a historical playtest.
