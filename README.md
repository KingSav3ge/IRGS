# IRGS — joined development source

This repository's `main` combines the Engine and App. Independent development now lives in:

| Component | Repository | Source |
| --- | --- | --- |
| Engine, Core routines, campaign foundations | [IRGS-Engine](https://github.com/KingSav3ge/IRGS-Engine) | `IRGS_3_3/`, `engine/` |
| App, website, discovery and previews | [IRGS-APP-WEB](https://github.com/KingSav3ge/IRGS-APP-WEB) | `IRGS_Web/` |
| Joined IRGS | [IRGS](https://github.com/KingSav3ge/IRGS) | Full Engine and App sources on `main` |

The selected executable Core is 3.3; D1 is the assembled development edition. See [component integration](COMPONENT_REPOSITORIES.md), [development commands](DEVELOPMENT.md), [roadmap](ROADMAP.md), and [operation coverage](engine/OPERATION_COVERAGE.md).

Run `python -B IRGS_Web/server.py --port 8766`, or use `Start-IRGS.cmd` on Windows. Hosts bind to loopback. Existing user saves are not included or migrated.

Content Library contains 44 concept previews: 31 launch targets, 12 future campaigns and one independent simulation system. Filters separate type, genre, setting, period, launch positioning and available slices. The concepts are not 44 released games. See [catalogue scope](IRGS_Catalog/design/campaign_catalogue/README.md).

Century of Conflict has 37 reviewed dated starts with optional bounded fictional openings. The Rise of... You offers a fictional R00 founding slice; its eight design families remain held. Kira v0.5 is the user-adopted working world canon, available as a searchable reference guide with no playable starting snapshot. General freeform resolution, combat, a complete autonomous institutional cycle and all 121 C2 acceptance cases remain unfinished.

Original uploads and historical qualification evidence remain labelled under `provenance/`. They do not establish fresh verification or automatically apply draft mechanics. Core and App have independent integrity records so either component can develop without rewriting the other's release pins.
