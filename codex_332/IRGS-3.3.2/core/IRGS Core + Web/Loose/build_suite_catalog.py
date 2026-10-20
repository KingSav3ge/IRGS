"""Build the Core 3.3 suite's source-preserving genre/content catalogue.

Only catalog/ and data/catalog.json are written. No campaign save, original
source, numerical profile or source adoption status is changed. Rebuilds copy
the inspected local sources, so the manifest always records the actual bytes.
"""
from __future__ import annotations

import collections
import hashlib
import importlib
import json
from pathlib import Path
import shutil
import sys

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent
SOURCES = WORKSPACE / "IRGS"
CORE_REF = "IRGS-CORE-3.3"
OWNERS = ["K-TIME", "K-ACTOR", "K-STOCK", "K-ASSET", "K-WORK",
          "K-INFO", "K-ORG", "K-NET", "K-POP"]


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def common_operations():
    """Read the authoritative kernel inventory, rather than freezing a copy."""
    runtime = str(HERE / "runtime")
    sys.path.insert(0, runtime)
    try:
        importlib.invalidate_caches()
        module = importlib.import_module("core_world")
        return sorted(module.CORE_OPS)
    finally:
        sys.path.remove(runtime)


def native_operations(genre):
    """Current bounded campaign routes, distinct from legacy R9 fixtures."""
    runtime = str(HERE / "runtime")
    sys.path.insert(0, runtime)
    try:
        module = importlib.import_module("genre_receivers")
        selected = {"revoke_delegation"}
        if genre in {"military", "roman"}:
            selected.add("military_issue_equipment")
        if genre == "roman":
            selected.add("roman_begin_delegated_activity")
        if not selected.issubset(module.GENRE_OPS):
            raise ValueError("catalogue receiver inventory exceeds implemented runtime")
        return sorted(selected)
    finally:
        sys.path.remove(runtime)


class Bundle:
    def __init__(self):
        self.entries = {}

    def record(self, target, *, origin, role, status):
        target = Path(target)
        key = target.relative_to(HERE).as_posix()
        entry = {"path": key, "sha256": sha256(target),
                 "bytes": target.stat().st_size, "origin": origin,
                 "role": role, "source_status": status}
        old = self.entries.get(key)
        if old is not None and old != entry:
            raise ValueError(f"conflicting bundle identity: {key}")
        self.entries[key] = entry
        return key

    def copy(self, source, relative, *, role="preserved_source", status="Source status retained"):
        source = Path(source)
        if not source.is_file():
            raise FileNotFoundError(source)
        target = HERE / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        if sha256(source) != sha256(target):
            raise ValueError(f"source copy differs: {source}")
        try:
            origin = source.relative_to(WORKSPACE).as_posix()
        except ValueError:
            origin = str(source)
        return self.record(target, origin=origin, role=role, status=status)

    def tree(self, source, relative, *, status):
        """Retain the complete library tree, including its source payloads."""
        source = Path(source)
        paths = []
        for path in sorted(source.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            # Archives of whole previous distributions are not current content.
            if path.suffix.lower() in {".zip", ".7z"}:
                raise ValueError(f"unexpected historical archive in library: {path}")
            paths.append(self.copy(path, Path(relative) / path.relative_to(source), status=status))
        return paths

    def generated(self, relative, value, *, role):
        target = HERE / relative
        write_json(target, value)
        return self.record(target, origin="build_suite_catalog.py", role=role,
                           status="Core 3.3 prospective receiving metadata; source status unchanged")


def refresh_packaged():
    """Refresh receiver code bindings from an already verified standalone bundle."""
    manifest=read_json(HERE/'catalog/source_manifest.json')
    for row in manifest['files']:
        if sha256(HERE/row['path'])!=row['sha256']:raise ValueError('Packaged source changed: '+row['path'])
    data=read_json(HERE/'data/catalog.json');ops=common_operations()
    data['core']['runtime_operations']=ops
    for engine in data['genre_engines']:
        path=HERE/engine['receiving_binding'];binding=read_json(path)
        binding['runtime_operations']=sorted(set(ops)|set(native_operations(engine['id'])))
        binding['runtime_sources_sha256']={name:sha256(HERE/name) for name in binding.get('runtime_sources_sha256',{})}
        write_json(path,binding);engine['runtime_operations']=binding['runtime_operations']
    path=HERE/'catalog/profiles/ast_core_3_3.json';binding=read_json(path)
    binding['runtime_operations']=sorted(set(ops)|set(native_operations('military')));write_json(path,binding)
    for row in manifest['files']:
        row['sha256']=sha256(HERE/row['path']);row['bytes']=(HERE/row['path']).stat().st_size
    manifest['total_bytes']=sum(r['bytes'] for r in manifest['files'])
    write_json(HERE/'catalog/source_manifest.json',manifest)
    data['source_integrity']={'manifest_sha256':sha256(HERE/'catalog/source_manifest.json'),
                              'total_files':manifest['total_files'],'total_bytes':manifest['total_bytes']}
    write_json(HERE/'data/catalog.json',data)
    print(json.dumps({'mode':'verified standalone bundle','genres':len(data['genre_engines']),
                      'libraries':len(data['content_libraries']),'all_hashes_verified':True}))

def main():
    if not SOURCES.exists():return refresh_packaged()
    bundle = Bundle()
    ops = common_operations()
    base = {
        "shared": SOURCES / "IRGS_Full_Release_R2",
        "fantasy": SOURCES / "IRGS_Fantasy_Core32_Library20",
        "paf": SOURCES / "IRGS_PAF_Core32_Library20",
        "military": SOURCES / "IRGS_Military_Slim_v1_2_Core3_2_and_Military_Library_v1_0_Combined_Release",
        "roman": SOURCES / "IRGS_Roman_Republic_v1_2_Engine_Content_v1_0_Complete",
        "shinobi": SOURCES / "IRGS_SNWE_R0_3_and_SNCL_v1_0_Combined_Release",
        "space": SOURCES / "IRGS_Space_Exploration_and_Colonization_Slim_v0_2_Core3_2_R2",
        "ast": SOURCES / "AST_v05" / "AST_v05" / "IRGS_AST",
    }
    specs = {
        "military": {
            "name": "Soldier and Military Life", "version": "1.2",
            "engine": "MilitarySlim/IRGS_Soldier_Military_Life_Slim_v1_2_Core3_2_MCL1_0_Proposed.md",
            "binding": "MilitarySlim/IRGS_Military_Slim_v1_2_Core3_2_Receiving_Binding.json",
            "source_status": "Proposed complete receiving edition; not automatically campaign adopted",
            "extras": ["MilitarySlim/Military_Current_SCL_Reference_Recheck.json", "MilitarySlim/Military_1_0_to_1_2_CMRR.csv"],
            "requirements": ["Actual service institution and qualification", "Received orders and scoped authority", "Actual equipment instances and readiness", "Selected physiological, learning and effect profiles when material"],
            "limits": ["Military native service/combat mechanics beyond listed Core operations are source references", "48 library templates remain proposed and unqualified"],
            "research_ops": ["mil_issue_received_order"],
        },
        "roman": {
            "name": "Roman Republic Life", "version": "1.2",
            "engine": "IRGS_Roman_Republic_Life_Simulation_Engine_Slim_v1_2.md",
            "binding": "ROMAN_SUITE_DEPLOYMENT_BINDING.json",
            "source_status": "Accepted finalized workshop reference; numerical and historical calibration provisional",
            "extras": ["roman_republic_slim_v1_2/content_bindings.json"],
            "requirements": ["Actual date, locality and institutional/legal eligibility", "Exact native selector and complete compatible profile", "Actual finite instances with Core owners", "Preserve Roman heavy-blunt and three-way order profiles"],
            "limits": ["118 library templates remain proposed", "Historical calibration and full native execution are not established by source packaging"],
            "research_ops": ["rom_start_delegated_job", "rom_revoke_delegation"],
        },
        "fantasy": {
            "name": "Fantasy", "version": "1.2",
            "engine": "IRGS_Fantasy_Engine_Slim_v1_2_Core3_2.md",
            "binding": "IRGS_Fantasy_Binding_v1_2_Core3_2.json",
            "source_status": "Complete linked workshop specification; individual proposals and profile gates retained",
            "extras": ["IRGS_Fantasy_Content_Map_v1_2_Core3_2.csv", "IRGS_Fantasy_Reconciliation_v1_2.csv"],
            "requirements": ["Select complete character, effect, injury, physiology, learning and travel profiles when used", "Resilience, shield contact and transmission required when material", "Enable a specific supernatural paradigm and finite resource translation before use", "Fantasy nominal 20-hour TU is not the historical 4-hour TU"],
            "limits": ["Native Fantasy arithmetic and supernatural execution remain unqualified specialty operations", "Twelve new archetypes remain proposed and opt-in"], "research_ops": [],
        },
        "paf": {
            "name": "Post-Apocalyptic Survival and Reconstruction", "version": "2.1",
            "engine": "IRGS_PAF_Engine_v2_1_Core3_2.md",
            "binding": "IRGS_PAF_Binding_v2_1_Core3_2.json",
            "source_status": "Complete linked workshop edition; profile adoption and calibration remain distinct",
            "extras": ["IRGS_PAF_Content_References_v2_1.csv", "IRGS_PAF_Acceptance_Inventory_v2_1.json"],
            "requirements": ["Assessments reference actual Core facts and actor-visible evidence", "Actual cause-specific needs, recovery, service and logistics profiles", "No universal ration, collapse, hazard or deterioration rate", "Extraordinary modules require explicit finite compatible models"],
            "limits": ["PA assessment overlays must not create a second physical ledger", "43 compositions remain proposed; no extraordinary module enabled by default"], "research_ops": [],
        },
        "shinobi": {
            "name": "Shinobi Nexus", "version": "0.3",
            "engine": "SNWE_R0.3/IRGS_Shinobi_Nexus_World_Engine_SNWE_R0_3_Core3_2_SCL1_0_CMRR.md",
            "binding": "SNWE_R0.3/IRGS_SNWE_R0_3_Core3_2_Receiving_Binding.json",
            "source_status": "Proposed complete Core 3.2 receiving edition; source mechanics retained",
            "extras": [],
            "requirements": ["SSN native 2d6 task and d20 Precision; no parallel Core d100", "SSN HP/SP/CU and action economy; no parallel Fantasy Threat", "Explicit abstract-to-physical bridge in persistent mode", "Exact permitted technique, finite cost, affected existing owners and actor knowledge"],
            "limits": ["Native resolution/chakra/technique execution is a source reference, not an implemented Core 3.3 specialty receiver", "415 legacy techniques are unconverted and blocked; AP, CSLS and million-unit CU cannot be imported directly"], "research_ops": [],
        },
        "space": {
            "name": "Space Exploration and Colonization", "version": "0.2",
            "engine": "IRGS_Space_Exploration_and_Colonization_Foundation_Slim_v0_2_Proposed.md",
            "binding": "source_space_binding.json",
            "source_status": "Complete proposed CMRR specification; no calibration or automatic campaign adoption",
            "extras": ["content_bindings.json"],
            "requirements": ["Selected frame, epoch and ephemerides", "Supported flight/propulsion/arrival envelopes", "Pressure, chemistry, thermal and EVA models where material", "Moving-endpoint signal receipt, remote command authority and ISRU parameters"],
            "limits": ["Flight, thermal, pressure, signals and ISRU specialty calculations are not Core 3.3 executable receivers", "No spacecraft certification or universal physical rates claimed"], "research_ops": [],
        },
    }

    # Preserve all current shared catalogue, qualification and receiving data.
    # The top-level Core 3.2 document is retained solely as source provenance.
    shared_files = []
    for path in sorted(base["shared"].iterdir()):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".csv"}:
            shared_files.append(bundle.copy(path, Path("catalog/libraries/shared") / path.name,
                status="SCL 1.0 source status unchanged; Core 3.2 references are preserved provenance"))

    engines = []
    for genre, spec in specs.items():
        native_ops = native_operations(genre)
        profile_ops = sorted(set(ops) | set(native_ops))
        copied = []
        for filename in [spec["engine"], spec["binding"], *spec["extras"]]:
            copied.append(bundle.copy(base[genre] / filename,
                Path("catalog/genres") / genre / "source" / filename,
                status=spec["source_status"]))
        binding_path = f"catalog/genres/{genre}/receiving_core_3_3.json"
        receiving = {
            "id": f"IRGS-BIND-{genre.upper()}-CORE-3.3", "genre_id": genre,
            "core_ref": CORE_REF, "core_version": "3.3", "status": "LIVE_LOCAL_REFERENCE_ROUTING",
            "source_status": spec["source_status"], "source_core_ref": "IRGS-CORE-3.2",
            "source_files": [{k: bundle.entries[p][k] for k in ("path", "sha256", "bytes")} for p in copied],
            "shared_library": "shared", "library_ids": ["shared", genre],
            "runtime_class": "core_world.CoreWorld", "runtime_operations": profile_ops,
            "runtime_operation_inventory": "runtime/core_world.py:CORE_OPS",
            "bounded_receiver_operations": native_ops,
            "bounded_receiver_source": "runtime/genre_receivers.py:GENRE_OPS",
            "runtime_sources_sha256": {p: sha256(HERE / p) for p in ["runtime/core_world.py", "runtime/genre_receivers.py"]},
            "lookup_operations": ["classify_record"],
            "specialty_runtime_operations": native_ops, "required_owners": OWNERS,
            "profile_requirements": spec["requirements"],
            "compatibility_research_receivers": {"operations": spec["research_ops"],
                "runtime": "runtime/r9_adapters.py", "scope": "Synthetic R9 research state only; not this campaign route", "certifies_native_engine": False},
            "single_state": "All effects use the selected campaign's authoritative Core owners and clock",
            "selection_authority": "User requested live Core 3.3 plus genre engines and content libraries",
            "activation_effect": "Selects routing and available source references; does not adopt proposed numbers or create instances",
            "automatic_source_adoption": False, "automatic_campaign_migration": False,
            "numeric_profile_adoption": False, "source_deprecation": False,
            "certification": "This catalogue and binding make no execution or branch certification claim",
            "limitations": spec["limits"],
        }
        bundle.generated(binding_path, receiving, role="prospective_receiving_binding")
        engines.append({"id": genre, "name": spec["name"], "version": spec["version"],
            "status": "LIVE_LOCAL_REFERENCE_ROUTING", "source_status": spec["source_status"],
            "core_ref": CORE_REF, "source_core_ref": "IRGS-CORE-3.2",
            "source_files": copied, "primary_source": copied[0], "source_binding": copied[1],
            "receiving_binding": binding_path, "runtime_operations": profile_ops,
            "lookup_operations": ["classify_record"], "specialty_runtime_operations": native_ops,
            "runtime_sources_sha256": receiving["runtime_sources_sha256"],
            "library_ids": ["shared", genre], "limitations": spec["limits"],
            "profile_requirements": spec["requirements"], "numeric_profile_adoption": False})

    library_statuses = {
        "fantasy": "Selected source dependency for linked Fantasy release; guide and twelve new archetypes remain proposed; complete native projection retained",
        "paf": "Proposed Post-Apocalyptic Library 2.0; 43 optional compositions; no automatic activation",
        "military": "Proposed qualification candidate; 48 templates remain unqualified and opt-in",
        "roman": "Proposed Roman Content Library 1.0; accepted Roman engine status does not adopt these 118 templates",
        "shinobi": "Finalized source edition; original 122 record statuses retained; 415 legacy conversions held and blocked",
    }
    trees = {"fantasy": ("FantasyLibrary", "2.0", "Fantasy Content Library"),
             "paf": ("PALibrary", "2.0", "Post-Apocalyptic Content Library"),
             "military": ("MilitaryLibrary", "1.0", "Military Content Library"),
             "roman": ("Roman_Content_Library", "1.0", "Roman Republic Content Library"),
             "shinobi": ("SNCL_v1.0", "1.0", "Shinobi Nexus Content Library")}
    libraries = [{"id": "shared", "name": "IRGS Shared Content Library", "type": "shared_library",
        "version": "1.0", "status": "AVAILABLE_SOURCE_REFERENCE", "core_ref": CORE_REF,
        "source_status": "51 selected qualitative definitions; 228 held families; qualification drafts proposed",
        "source_files": shared_files, "registry_file": "catalog/libraries/shared/IRGS_Shared_Content_Registry_v1_0.json",
        "definition_revision": "0.2", "automatic_numeric_adoption": False}]
    for genre, (directory, version, name) in trees.items():
        files = bundle.tree(base[genre] / directory, Path("catalog/libraries") / genre,
                            status=library_statuses[genre])
        libraries.append({"id": genre, "name": name, "type": "genre_library", "version": version,
            "status": "AVAILABLE_SOURCE_REFERENCE", "source_status": library_statuses[genre],
            "core_ref": CORE_REF, "genre_id": genre, "source_files": files,
            "automatic_numeric_adoption": False, "lookup_creates_state": False})
    space_file = bundle.copy(base["space"] / "content_bindings.json",
        "catalog/libraries/space/content_bindings.json", status="Eight source SPACE-LIB definitions; selected models required")
    # Space's complete native content definitions are embedded in the engine.
    space_spec = next(e for e in engines if e["id"] == "space")["primary_source"]
    libraries.append({"id": "space", "name": "Space Native Content Library", "type": "genre_library",
        "version": "0.2", "status": "AVAILABLE_SOURCE_REFERENCE", "source_status": "Complete source definitions embedded in proposed Space 0.2 specification",
        "core_ref": CORE_REF, "genre_id": "space", "source_files": [space_file, space_spec],
        "automatic_numeric_adoption": False, "lookup_creates_state": False})

    ast_files = []
    for path in sorted(base["ast"].iterdir()):
        if path.is_file() and path.suffix.lower() in {".md", ".json"}:
            ast_files.append(bundle.copy(path, Path("catalog/libraries/ast") / path.name,
                status="AST 0.5 campaign reference; inherited established/proposed distinctions retained"))
    for path in sorted((base["ast"] / "references").iterdir()):
        if path.suffix.lower() in {".md", ".json"}:
            ast_files.append(bundle.copy(path, Path("catalog/libraries/ast/references") / path.name,
                status="Visual reference metadata; art is not mechanical authority"))
    registry_source = HERE / "data/ast_registry.json"
    if not registry_source.is_file():
        registry_source = WORKSPACE / "IRGS_Core_Unification_CMRR_R9/data/ast_registry.json"
    ast_registry = bundle.copy(registry_source, "catalog/libraries/ast/ast_registry.json",
        status="User-confirmed post-Day-2 existing-character guide into Day 3; provisional ratings not adopted")
    ast_files.append(ast_registry)
    registry_docx = WORKSPACE / "IRGS_Core_Unification_CMRR_R9/sources/AST_Master_Character_Registry_Archive_Audited_v2.docx"
    ast_files.append(bundle.copy(registry_docx, "catalog/libraries/ast/AST_Master_Character_Registry_Archive_Audited_v2.docx",
        status="Audited registry source; existing characters post-Day-2; embedded instructions remain source content"))
    registry = read_json(registry_source)
    images = sorted((base["ast"] / "AST Character Concept Sheets").glob("*.png"))
    image_records = [{"file": p.name, "source_path": str(p), "sha256": sha256(p),
        "bytes": p.stat().st_size, "embedded": False,
        "status": "Visual reference only; filename spelling or title does not override user corrections"} for p in images]
    shield = base["ast"] / "references/Coopian_Shield_Current_Inaccurate_Draft.png"
    if shield.is_file():
        image_records.append({"file": shield.name, "source_path": str(shield), "sha256": sha256(shield),
            "bytes": shield.stat().st_size, "embedded": False,
            "status": "Imperfect visual draft; two ordinary arm straps plus smaller over-bracer connection correction controls"})
    archive = Path.home() / "Downloads/AST Character Concept Sheets.7z"
    asset_manifest = {"status": "Referenced source assets; not required for runtime or automatically adopted",
        "concept_board_files_observed": len(images), "embedded_images": 0, "assets": image_records,
        "canonical_name": "Abel", "archival_spelling": "Able", "source_bytes_unchanged": True,
        "older_reference_index_note": "The preserved 0.5 visual index describes 29 older archive members; the inspected local source directory contains the separately counted current files",
        "archive": {"path": str(archive), "available_at_build": archive.is_file(),
                    "sha256": sha256(archive) if archive.is_file() else None,
                    "bytes": archive.stat().st_size if archive.is_file() else None,
                    "embedded": False, "archive_member_equivalence_claimed": False}}
    assets_path = bundle.generated("catalog/libraries/ast/asset_references.json", asset_manifest,
                                    role="external_asset_inventory")
    ast_files.append(assets_path)
    ast_binding_path = "catalog/profiles/ast_core_3_3.json"
    bundle.generated(ast_binding_path, {"id": "AST-CAMPAIGN-PROFILE-CORE-3.3", "profile_id": "ast",
        "type": "campaign_profile", "genre_id": "military", "library_ids": ["shared", "military", "ast"],
        "core_ref": CORE_REF, "status": "LIVE_LOCAL_CAMPAIGN_LIBRARY_ROUTING",
        "campaign_procedure_source": "catalog/libraries/ast/AST_Engine_v0_5.md",
        "ast_is_standalone_engine": False, "registry_file": ast_registry,
        "registry_use": registry["use"], "canonical_horse_name": "Abel",
        "selected_resolution": "Recovered AST-R01 d100 bands; other numerical defaults remain unresolved",
        "unselected_profiles": ["physiology", "combat effect", "learning rate"],
        "runtime_operations": sorted(set(ops) | set(native_operations("military"))),
        "lookup_operations": ["classify_record"],
        "no_automatic_day_advance": True, "registry_provisional_ratings_adopted": False,
        "existing_save_policy": "Existing saved facts, clock, IDs and journal prevail; no overwrite or retroactive migration",
        "source_files": [{k: bundle.entries[p][k] for k in ("path", "sha256", "bytes")} for p in ast_files],
        "bounded_receiver_operations": native_operations("military"),
        "automatic_numeric_adoption": False}, role="prospective_campaign_binding")
    libraries.append({"id": "ast", "name": "A Scot's Tale · Archived Starting Sources",
        "type": "campaign_library", "version": "0.5 + audited registry v2", "status": "ARCHIVED_SCENARIO_SOURCES",
        "core_ref": CORE_REF, "genre_id": "military", "source_status": "Mixed recovered campaign facts and proposals; audited registry guides existing characters into Day 3",
        "source_files": ast_files, "receiving_binding": ast_binding_path, "registry_file": ast_registry,
        "character_count": len(registry["characters"]), "asset_references": assets_path,
        "automatic_numeric_adoption": False, "lookup_creates_state": False,
        "standalone_maintenance": False, "named_start": {"campaign_id": "hundred-years-war", "entry_id": "hyw-1415", "scenario_id": "ast"},
        "mechanics_reuse": "data/ast_mechanics_reuse.json",
        "limitations": ["Source guide does not itself advance Day 3 or replace a later save", "Provisional capability ratings remain unadopted", "Art captions are subordinate to user identity and design corrections"]})

    shared = read_json(base["shared"] / "IRGS_Shared_Content_Registry_v1_0.json")
    overlay = read_json(base["shared"] / "IRGS_SCL_Consolidated_Qualification_R2.json")
    fan = read_json(base["fantasy"] / "FantasyLibrary/Fantasy_Native_Source_Projection_v2_0.json")
    pa = read_json(base["paf"] / "PALibrary/PA_Native_Compositions_v2_0.json")
    mil = read_json(base["military"] / "MilitaryLibrary/IRGS_Military_Content_Catalogue_v1_0.json")
    roman = read_json(base["roman"] / "Roman_Content_Library/Roman_Content_Catalogue_v1_0.json")
    shinobi = read_json(base["shinobi"] / "SNCL_v1.0/IRGS_SNCL_v1_0_Registry.json")
    space = read_json(base["space"] / "content_bindings.json")
    holds = {"shared": {"counts": shared["counts"], "qualification_counts": overlay["counts"],
                  "definition_revision": "0.2", "rule": "Selected means qualitative source definition; held family replacement and numerical activation remain held"},
        "fantasy": {"source_bindings": len(fan["source_bindings"]), "native_adapters": len(fan["native_adapters"]),
                    "source_payloads": len(fan["source_payload_blocks"]), "proposed_archetypes": len(fan["new_proposed_archetypes"])},
        "paf": {"proposed_compositions": len(pa["templates"])},
        "military": {"proposed_unqualified_templates": len(mil["templates"])},
        "roman": {"proposed_templates": len(roman["entries"]), "native_profiles": len(roman["native_binding_references"])},
        "shinobi": {"records": len(shinobi["records"]), "source_counts": shinobi["counts"],
                    "status_rule": shinobi["active_allowed_rule"], "readiness": shinobi["readiness"]},
        "space": {"source_definitions": len(space["space_entries"]), "optional_shared_aliases": len(space["optional_shared_content"])},
        "ast": {"characters": len(registry["characters"]), "provisional_ratings_adopted": False,
                "post_day_2_guide": True, "canonical_horse_name": "Abel"},
        "promotion_applied": False, "lookup_creates_state": False}
    holds_path = bundle.generated("catalog/hold_summary.json", holds, role="source_readiness_summary")
    for library in libraries:
        library["hold_summary"] = holds[library["id"]]

    profiles = [{"id": genre, "name": spec["name"], "version": "3.3",
        "status": "LIVE_LOCAL_PROFILE", "genre_id": genre, "core_ref": CORE_REF,
        "library_ids": ["shared", genre], "source_status": spec["source_status"],
        "receiving_binding": f"catalog/genres/{genre}/receiving_core_3_3.json",
        "initial_state": "Empty campaign state; actual people, stocks, capacities and policies require sourced initialization",
        "automatic_numeric_adoption": False} for genre, spec in specs.items()]
    profiles.insert(0, {"id": "ast", "name": "A Scot's Tale · legacy checkpoint adapter", "version": "3.3", "status": "ARCHIVED_LEGACY_PROFILE",
        "genre_id": "military", "core_ref": CORE_REF, "library_ids": ["shared", "military", "ast"],
        "source_status": "User-confirmed audited post-Day-2 guide for existing characters into Day 3",
        "receiving_binding": ast_binding_path, "registry_file": ast_registry,
        "canonical_horse_name": "Abel", "automatic_numeric_adoption": False})
    missing_r3 = {"artifact": "RELEASE_BINDING_R3.json", "status": "NOT_PRESENT_IN_INSPECTED_WORKSPACE",
        "source_claim": "Legacy package README/MAINTENANCE_R3.md cite this top-level record",
        "consequence": "Its historical deployment claim is unverified; actual bundled files have fresh SHA-256 evidence",
        "reconstructed_or_invented": False}
    # The historical setting extends the existing Military library. Proposed
    # dates and screen/history design references never adopt new mechanics.
    historical = read_json(HERE / 'data/hyw_entry_catalogue.json')
    opening = read_json(HERE / 'data/hyw_1415_opening.json')
    assert len(historical['entries']) == 37 and len(historical['featured_years']) == 10
    assert opening['id'] == 'hyw-1415'
    for name in ('hyw_entry_catalogue.json', 'hyw_1415_opening.json', 'hyw_design_references.json',
                 'campaign_listings.json', 'hyw_historical_baseline.json', 'ast_mechanics_reuse.json'):
        bundle.record(HERE / 'data' / name, origin='User-requested design and patch integration, 20 October 2026',
                      role='historical_setting_content', status='Historical setup reference; proposal and unknown statuses retained')
    for reference in read_json(HERE / 'data/hyw_design_references.json'):
        assert sha256(HERE / reference['path']) == reference['sha256']
        bundle.record(HERE / reference['path'], origin='User-supplied design reference',
                      role='design_reference', status=reference['status'])
    for library in libraries:
        if library['id'] == 'military':
            library['historical_settings'] = [{'id':historical['id'], 'catalogue':'data/hyw_entry_catalogue.json',
                'developed_opening':'data/hyw_1415_opening.json', 'catalogue_entries':37, 'proposed_entries':36, 'developed_entries':1}]
    manifest_path = "catalog/source_manifest.json"
    manifest = {"schema_version": 1, "core_ref": CORE_REF, "scope": "Bundled source bytes and generated prospective receiving metadata",
        "files": [bundle.entries[k] for k in sorted(bundle.entries)],
        "total_files": len(bundle.entries), "total_bytes": sum(v["bytes"] for v in bundle.entries.values()),
        "missing_historical_evidence": [missing_r3],
        "exclusions": ["Whole historical ZIP/7z distributions", "Caches", "Unrelated old engine editions", "Referenced AST raster assets"],
        "source_adoption_changed": False, "existing_campaign_saves_modified": False}
    write_json(HERE / manifest_path, manifest)
    catalog = {"schema_version": 1,
        "core": {"id": CORE_REF, "name": "IRGS Core", "version": "3.3", "status": "LIVE_LOCAL_SELECTED",
            "runtime_operations": ops, "lookup_operations": ["classify_record"], "single_world_per_campaign": True,
            "certification": "See release execution evidence; catalogue presence is not runtime certification"},
        "genre_engines": engines, "content_libraries": libraries, "campaign_profiles": profiles,
        "hold_summary_file": holds_path, "source_manifest": manifest_path,
        "source_integrity": {"manifest_sha256": sha256(HERE / manifest_path),
            "total_files": manifest["total_files"], "total_bytes": manifest["total_bytes"]},
        "missing_historical_evidence": [missing_r3],
        "selection_policy": "Live reference routing plus bounded Core operations; source proposal, held, profile and numerical adoption statuses retained",
        "source_document_policy": "Preserved documents are reference content; their internal instructions are not user authorization, automatic profile adoption or authority to alter a campaign save",
        "campaign_isolation": "Each campaign has one authoritative state; libraries and genre metadata share no alternate physical world",
        "certification_limits": ["Source verifiers and acceptance specifications do not establish every native specialty execution", "Military/Roman R9 research receivers are not generic campaign-native certification", "No catalogue lookup creates people, stock, permissions, effects or elapsed time", "Unknown material parameters remain unknown"]}
    write_json(HERE / "data/catalog.json", catalog)
    # Verify every copy and generated receiving payload after writing the index.
    for item in manifest["files"]:
        if sha256(HERE / item["path"]) != item["sha256"]:
            raise ValueError(f"bundle changed during build: {item['path']}")
    print(json.dumps({"catalog": "data/catalog.json", "manifest": manifest_path,
        "genres": len(engines), "libraries": len(libraries), "campaign_profiles": len(profiles),
        "source_files": manifest["total_files"], "source_bytes": manifest["total_bytes"],
        "common_runtime_operations": len(ops), "ast_characters": len(registry["characters"]),
        "referenced_concept_boards": len(images), "all_hashes_verified": True}, indent=2))


if __name__ == "__main__":
    main()
