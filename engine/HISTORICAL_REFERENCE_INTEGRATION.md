# Historical Grand Archive reference integration

The separately supplied Grand Archive 1.1 is attached as a read-only Creator reference library. It does not replace the selected Core, initialize a historical start, populate a continuing world, infer character eligibility or grant a player knowledge of historical outcomes.

## Ownership and provenance

`IRGS_3_3/runtime/historical_archive.py` reads a ZIP selected explicitly by the local owner. Registration pins the entire archive SHA-256 and verifies the delivery manifest bindings for supported collections. Each search/detail read checks the relevant member's size and hash. Changed attachments fail closed until the intended source is registered. Original payloads, namespaces, dates, uncertainty, units, rights dispositions and missing values remain source data. Duplicate local IDs retain different source-row addresses; finding two assertions does not merge their subjects or count quantities twice.

Reference addresses include the archive SHA-256, collection, member path and one-based row. Source IDs remain separate. Details preserve the complete original record; resolvable source IDs show their registry and rights records, while unresolved source references are labelled explicitly. The provider performs no calendar conversion, interpolation, currency conversion, unit inference or adoption. Source instructions and game definitions are never executed.

The initial supported collections are chronology, figure references, supplement research, reviewed claims, citations, rights, concepts, places, reconstructed routes and country-year economic estimates. Large compressed JSONL collections are read in bounded streams without unpacking the central database. Search is literal case-insensitive matching of all words in the selected collection. Pagination reports more available results rather than inventing a total. Raw game files, book pages, HTML readers, every ancillary table and the 1.56 GB database are not exposed as website assets.

## Attach once on each installation

From the joined IRGS or standalone App repository root:

```text
python -B IRGS_Web/register_historical_archive.py "path/to/IRGS_Historical_Grand_Archive_v1_1.zip"
```

The command stores only a local attachment path and hash under `IRGS_Web/cache/reference_sources.json`. The cache directory is ignored by Git and excluded from the unified source package. It does not copy the archive or write a campaign. The normal website launcher loads this registration. The source ZIP must remain accessible at that location; a moved or revised attachment requires explicit re-registration. `--config` can select an installation-specific registration location, and the host accepts `--reference-config` for the corresponding path.

Project source-file availability in one local workspace does not mount that file in a cloud task. A cloud installation can register its accessible copy with the same command. No Windows owner path is embedded in published code. The mixed-rights source payload itself is not redistributed by this integration; the archive's source-specific access and rights records remain controlling source metadata.

## Website boundary

Choose **Creator workspace → Historical Reference Library**. The view works without a selected campaign and offers collection search, paging, original records, citations and provenance. It has no adopt, initialize, import-to-world or event button. All three HTTP routes require the normal local session and explicit Creator mode. They execute outside the campaign-store lock and do not acquire or modify campaign records. Player discovery still lists only existing campaign entries. Historical references never select a response suggestion or change actor-filtered views.

The reference routes accept collection IDs and row numbers from a fixed collection registry. They accept no arbitrary file paths, SQL or executable archive assets. Source text is escaped, links allow only HTTP(S), and delayed responses are discarded after navigation or a switch to player view. Attachments are configured through the local tool, not through an unauthenticated upload route.

## Validation scope

See `HISTORICAL_REFERENCE_VALIDATION.json` for freshly executed tests and the actual source-attachment check. Those checks establish read-only interoperability and source preservation, not scholarly verification, rights expansion, historical snapshot adoption or complete C2 dependency certification. The original independent cloud confirmation remains tied to its named earlier source commit until a new cloud report identifies this increment.
