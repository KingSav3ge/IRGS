# IRGS 3.4.0 development update

Target iteration: **IRGS 3.4.0 — in development**. See the active Solo runtime work order and completion plan. Previously qualified versions and evidence retain their recorded identities.

This is the complete assembled development baseline: the selected Core 3.3 runtime and catalogue, C2's applied engine specification, and the preferred Emergent visual design connected to the canonical Solo host. 3.4.0 identifies this coordinated development update. It does not claim that the remaining C2 mechanics are implemented.

## Source layout

| Path | Role |
| --- | --- |
| `IRGS_3_3/runtime/` | Executable shared Core and its tests. |
| `IRGS_3_3/catalog/` and `IRGS_3_3/data/` | Installed genres, libraries, profiles and dated starting references. |
| `IRGS_3_3/Core/` | Selected runtime binding and inherited Core text. |
| `IRGS_Catalog/` | Independently maintained campaign listings, preview data and catalogue design documents. |
| `IRGS_Web/` | Canonical Solo website, transport and interface tests. |
| `engine/` | Applied C2 engine text, incorporation audit and preserved design sources. |
| `provenance/` | Historical source records; these are not current test results or instructions to adopt mechanics. |
| `tools/` | Unified development verification, packaging and smoke helpers. |

Superseded assembly bundles and their obsolete verifier have been removed. Edit and package the canonical sources above with the unified tools; Git history retains the original assembly inputs. There is no second editable `app/IRGS_Web` tree and no alternate Mongo simulation in the running application.

## Run the website

Double-click the root `Start-IRGS.cmd`. It uses the canonical launcher and defaults to `http://127.0.0.1:8765/`. An existing valid IRGS host on that port may be reused, including a host from the original installation.

For an isolated development host, run this from the repository root and open `http://127.0.0.1:8766/`:

```powershell
python -B IRGS_Web/server.py --port 8766
```

The development copy starts without campaign saves. Existing campaigns remain in the original installation; this assembly does not copy, migrate, restore or redate them. New campaigns created in the development copy are separate saved playthroughs. Runtime-created saves, host metadata and caches stay out of source packages.

## Verify changes

Use Python 3 and Node.js. The canonical host uses the Python standard library. Run these commands from the repository root; do not use Python's `-O` option.

```powershell
python -B tools/verify_development.py
python -B -m unittest discover -s IRGS_3_3/runtime -v
python -B -m unittest discover -s IRGS_Web/tests -v
node IRGS_Web/tests/test_gameplay_ui.js
```

If the interface test cannot locate Python, set `IRGS_TEST_PYTHON` to the Python executable used for the other checks. The interface suite uses synthetic records and transport; it does not open a real save. A historical-save test may explicitly skip when its external historical save is absent. Windows launcher fixtures are platform-specific.

Run checks appropriate to the change. After intentional source edits, run `python -B tools/refresh_component_releases.py --component engine`, `--component app` or `--component catalog` for only the edited component and refresh the unified development manifest:

```powershell
python -B tools/verify_development.py --refresh
python -B tools/verify_development.py
```

Refreshing hashes records the intended files. It does not establish that tests passed, adopt a proposed rule, implement a capability or certify every dependency branch.

## Package and check an extraction

```powershell
python -B tools/package_development.py
python -B tools/smoke_development.py
```

Use the unified helpers for new development distributions. Inherited `IRGS_3_3/build_release_3_3.py` and `IRGS_3_3/package_release.py` describe an earlier release workflow that depends on historical validation records and save backups. They are preserved sources, not the fresh D1 build command.

## Branches and next work

The joined repository keeps `main`. Independent Engine, App and Catalog development use their own repositories and `main` branches. The app pins Engine and Catalog checkouts; joined IRGS contains all three full source directories. See [component ownership and integration](COMPONENT_REPOSITORIES.md).

The equipment action and optional authored 1415 Solo opening are connected to the app. The opening supports repeated observation, local movement and dispatch delivery with atomic local durations and durable successful/unsuccessful outcomes. Wider gameplay, interruptible elapsed phases and operation-level dependency qualification remain work. See [ROADMAP.md](ROADMAP.md) for the bounded sequence and completion evidence.

## Operation coverage and evidence freshness

The bounded equipment action is implemented. The continuation now records supported operations by backend, with actual successful and rejected-path observations, source references and remaining gaps. Inspect [engine/OPERATION_COVERAGE.md](engine/OPERATION_COVERAGE.md) and its linked machine-readable register.

Check whether the stored evidence still matches its code, tests, fixture content and selected release inputs:

```powershell
python -B tools/build_operation_register.py --check engine/qualification/operation_register.json
python -B -m unittest discover -s tools/tests -p "test_*.py" -v
```

The freshness check does not replay tests or certify new branches. To generate new evidence, run:

```powershell
python -B tools/build_operation_register.py --output engine/qualification/operation_register.json --markdown engine/OPERATION_COVERAGE.md --test-log development_results/operation_capture.txt
```

This can take several minutes because it observes synthetic runtime test executions. The external historical-save fixture is skipped by policy, even if present. Existing campaigns and inherited certification files are not inputs. Actual apply calls and detached probes are recorded separately. A listed handler, a named test or a successful observation does not establish complete branch coverage or player availability.

## Historical reference library

Creator workspace → Historical Details browses the complete Catalog delivery by default. Catalog preserves the original Historical Grand Archive 1.1 ZIP in 32 verified byte parts. On first use, Engine reconstructs a verified ZIP into an ignored installation cache. The browser exposes ten structured collections; books, assets and the central database remain preserved in the archive. Source records, uncertainty, citations and rights retain their meanings, and reads create no campaign facts or player knowledge.

Explicit local ZIP attachment remains available with `python -B IRGS_Web/register_historical_archive.py "path/to/archive.zip"`. Each installation maintains its own cache and optional attachment registration; caches and local paths are excluded from source packages. See [integration and limits](engine/HISTORICAL_REFERENCE_INTEGRATION.md).

## Rise settlement foundation

Content Library → The Rise of... You → Begin a founding story starts a reviewed fictional R00 campaign. Company, permission and actual goods are separate choices. The shared Core executes bounded work, provision and household movement; the eight design families remain held. See [the implementation and status table](engine/design/rise/README.md) and [fresh qualification](RISE_FOUNDATION_VALIDATION.json).

## Century of Conflict starts

Content Library → Century of Conflict → entry dropdown reveals the selected starting reference. All 37 entries support reviewed individual Solo initialization and an optional fictional local opening; ten primary starts remain marked. The original 1415 snapshot and scene are preserved. See [implementation and CMRR](engine/CENTURY_STARTS_IMPLEMENTATION.md), [historical review and remaining research](provenance/century_of_conflict/HISTORICAL_REVIEW.md), and [current qualification](CENTURY_STARTS_VALIDATION.json). This adds no general action resolver, historical event schedule or existing-save migration.
