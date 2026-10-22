# Independent components and joined IRGS

The user selected this layout on 22 October 2026. `KingSav3ge/IRGS/main` remains the joined application. Its former Engine/App branches are retired after integration. Each new repository owns its component and develops on `main`.

| Repository | Owned source | Dependency |
| --- | --- | --- |
| `KingSav3ge/IRGS-Engine` | `IRGS_3_3/`, `engine/`, Engine milestones and source provenance | No App checkout is needed for Core verification or runtime tests. |
| `KingSav3ge/IRGS-APP-WEB` | `IRGS_Web/`, root `Start-IRGS.cmd` | `Engine/` and `Catalog/` are Git submodules pinned to qualified Engine and Catalog commits. |
| `KingSav3ge/IRGS-Catalog` | `IRGS_Catalog/`: campaign listings, preview records and catalogue design documents | No Engine or App needed for source verification. |
| `KingSav3ge/IRGS` | Full sources of all three components plus integration tooling | `COMPONENTS.json` records the integrated component commits. No submodule is needed to run the joined checkout. |

## Work on the app

```bash
git clone --recurse-submodules https://github.com/KingSav3ge/IRGS-APP-WEB.git
cd IRGS-APP-WEB
python -B tools/verify_components.py --component app
python -B IRGS_Web/server.py --port 8766
```

Use `git submodule update --init --recursive` after an ordinary clone. App code first accepts an explicit `IRGS_ENGINE_ROOT`, otherwise it finds joined `IRGS_3_3/` or the pinned `Engine/IRGS_3_3/`. The variable names the Core directory, not its runtime subdirectory. Missing dependencies produce a setup error; no alternate simulator is substituted.

Run Web unittests and `node IRGS_Web/tests/test_gameplay_ui.js` from the App repository root. Windows users can use root `Start-IRGS.cmd`; it delegates to the selected Engine launcher while explicitly supplying this App's host directory. No source or save copying is required.

App edits refresh only `IRGS_Web/release.json`:

```bash
python -B tools/refresh_component_releases.py --component app
```

## Work on the Engine

```bash
git clone https://github.com/KingSav3ge/IRGS-Engine.git
cd IRGS-Engine
python -B tools/verify_components.py --component engine
python -B -m unittest discover -s IRGS_3_3/runtime -v
python -B tools/refresh_component_releases.py --component engine
```

The Engine's `IRGS_3_3/release.json` pins its own executable/content sources. App hashes live in the App's independent release record. Updating an App file therefore requires no Engine commit. Refreshing either record establishes source identity, not passing tests, adopted mechanics or a release approval.

## Work on the Catalog

Clone `https://github.com/KingSav3ge/IRGS-Catalog.git`, edit `IRGS_Catalog/data/` and its design documents, then run `python -B tools/refresh_component_releases.py --component catalog` and `python -B IRGS_Catalog/verify_catalog.py`. Commit the reviewed source before updating the App dependency. The original v0.4 specification remains byte-for-byte preserved; new designs should be separate documents.

The Catalog owns campaign discovery and preview data. It does not own `IRGS_Web/static/catalogue.js`, filtering or projection code, Engine technical libraries/profiles, Kira world canon, historical snapshots or campaign initializers. Those remain with their existing components. Catalogue metadata grants no launch capability, entitlement or completed-campaign release.

App `catalog_paths.py` accepts explicit `IRGS_CATALOG_ROOT`, otherwise sibling `IRGS_Catalog/` or `Catalog/IRGS_Catalog/`. This variable names the content directory. Its release inventory is verified at host startup.

## Qualify a component set and join it

1. Commit Engine changes in its repository and execute the relevant runtime checks. Update the App's `Engine` submodule to that exact commit when testing the new pair. App source edits remain independent of this dependency update.
2. For a Catalog update, select its exact commit in the App's `Catalog` submodule and refresh its independent release binding in the Catalog repository first. Run the relevant App/interface checks and isolated mechanics/recovery probes. Commit the qualified dependency pointer and App changes. A successful Core-only test is not App compatibility evidence.
3. In a clean joined IRGS checkout, preview the import with `python -B tools/sync_components.py --engine /path/to/IRGS-Engine --app /path/to/IRGS-APP-WEB --catalog /path/to/IRGS-Catalog`. The command reads committed snapshots and reports changed paths without writing by default.
4. Repeat with `--apply` to import the explicitly selected component set. The App's pinned Engine and Catalog must equal the selected component commits. Current `engine/qualification/operation_register.json`, `engine/OPERATION_COVERAGE.md` and `provenance/qa/` belong to joined qualification and are retained from joined IRGS; standalone Engine copies are inherited evidence. The tool preserves unrelated integration files and refuses dirty source/destination checkouts.
5. Refresh the joined development manifest, run current qualification and the package smoke check, review the diff, and commit/push `IRGS/main`. The sync tool never commits or pushes.

No direction automatically deploys a site, applies a historical future, imports a user save or grants campaign release approval. Existing playthroughs retain their committed state. Engine, App and Catalog development can proceed independently; joining remains an explicit, tested integration.

## Coordinator review gate

The user now assigns unified integration to **IRGS Enviroment**. Read [COORDINATION.md](COORDINATION.md) and [COORDINATION.json](COORDINATION.json) before importing. All three components need viable updates, exact coordinator approvals and matching App dependency pins. `tools/check_integration_gate.py` reports the held/ready state; `sync_components.py --apply` enforces it. Component work orders are published in each repository. Historical Grand Archive multipart payload belongs to Catalog under `IRGS_Catalog/historical_details/`; Engine owns its reader and App owns the Creator viewer.
