# IRGS 3.4.1 — joined development source

Current coordinated edition: **3.4.1**; previous release: **3.3.3**.
See [3.4.1 release notes](RELEASE_NOTES_3_4_1.md) and [version policy](VERSION_POLICY.md). Historical evidence below retains
its original tested development identities.

Current development: [guide](DEVELOPMENT.md) · [chat continuation](CHAT_CONTINUATION.md).

This repository's `main` combines the Engine, App and Catalog. Independent development now lives in:

| Component | Repository | Source |
| --- | --- | --- |
| Engine, Core routines, campaign foundations | [IRGS-Engine](https://github.com/KingSav3ge/IRGS-Engine) | `IRGS_3_3/`, `engine/` |
| App, website, discovery and previews | [IRGS-APP-WEB](https://github.com/KingSav3ge/IRGS-APP-WEB) | `IRGS_Web/` |
| Campaign catalogue, reference payload and evaluation fixtures | [IRGS-Catalog](https://github.com/KingSav3ge/IRGS-Catalog) | `IRGS_Catalog/` |
| Joined IRGS | [IRGS](https://github.com/KingSav3ge/IRGS) | Full Engine, App and Catalog sources on `main` |

The development edition is 3.4.1; the selected executable Core retains compatibility ID 3.3. See [component integration](COMPONENT_REPOSITORIES.md), [development commands](DEVELOPMENT.md), [roadmap](ROADMAP.md), and [operation coverage](engine/OPERATION_COVERAGE.md).

Run `python -B IRGS_Web/server.py --port 8766`, or use `Start-IRGS.cmd` on Windows. Hosts bind to loopback. Existing user saves are not included or migrated.

Content Library contains 44 expanded v0.5 concept previews: 31 launch targets, 12 future campaigns and one independent simulation system. Filters separate type, genre, setting, period, launch positioning and available slices. The concepts are not 44 released games. See [catalogue scope](IRGS_Catalog/design/campaign_catalogue/README.md).

Century of Conflict has 37 reviewed dated starts with optional bounded fictional openings. The Rise of... You offers a fictional R00 founding slice; its eight design families remain held. Kira v0.5 is the user-adopted working world canon, available as a searchable reference guide with no playable starting snapshot. General freeform resolution, combat, a complete autonomous institutional cycle and full C2 acceptance qualification remain unfinished.

Original uploads and historical qualification evidence remain labelled under `provenance/`. They do not establish fresh verification or automatically apply draft mechanics. Core and App have independent integrity records so either component can develop without rewriting the other's release pins.

Historical Details now includes the complete original archive in Catalog’s 32 verified parts, with a protected Creator browser for ten reference collections. See [the completed integration and next assignments](COORDINATION.md).

The 3.4.0 development update adds an opt-in Solo proposal boundary, direct API transport, durable inference accounting, explicit App review/acceptance and the synthetic R00 evaluation fixture. Authored-scene and Rise actions retain their actual Core rules and receipts. Default assistance is unconfigured; no live model result or general narrator is claimed.
