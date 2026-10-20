"""Package the verified Core 3.3 suite without copying any campaign saves.

Run after the final release build and verified live activation. Distribution
payloads are selected solely by release.json's two hash allowlists, with the
explicit rebuild/evidence additions below. This script does not stop the host,
change selection, rebuild runtime code, or alter a saved campaign.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import zipfile


ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent
ARCHIVE_NAME = "IRGS_Core_3_3_Live.zip"
MANIFEST_NAME = "PACKAGE_MANIFEST.json"
FORBIDDEN_PARTS = {"live", "backup", "backups", "save", "saves", "cache", "caches",
                   "__pycache__", ".git", ".agents", ".codex", "logs"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo", ".log", ".zip", ".7z"}
SUITE_TOP_FILES = {"README.md", "SUITE_RELEASE.md", "CMRR_3_3_Release.md",
                   "DESIGN_INTEGRATION_2026_10_20.md",
                   "Start-IRGS-3.3.ps1", "Start-IRGS-3.3.cmd",
                   "build_suite_catalog.py", "build_release_3_3.py", "package_release.py"}
SUITE_PAYLOAD_DIRS = {"runtime", "data", "catalog", "Core"}
HOST_TOP_FILES = {"server.py", "features.py", "opening_scene.py", "gameplay_views.py", "history_views.py", "README.md", "Start-IRGS.ps1", "Start-IRGS.cmd"}
HOST_PAYLOAD_DIRS = {"static", "tests"}
EVIDENCE_FILES = (
    "completion_audit.json", "live_activation.json",
    "r9_certification_matrix.json", "r9_instrumented_tests.txt",
    "r9_scenario_summary.json", "suite_http_tests.txt",
    "sustained_unit_test.txt", "save_preservation_before.json",
    "save_preservation_verified.json", "hyw_runtime_tests.txt",
    "hyw_save_preservation_before.json", "hyw_save_preservation_verified.json",
    "gameplay_save_preservation_before.json", "gameplay_save_preservation_verified.json",
    "gameplay_ui_tests.txt", "gameplay_ui_verification.json",
    "launcher_fixture_tests.txt",
    "stage1_backend_tests.txt", "stage1_save_preservation_before.json", "stage1_save_preservation_verified.json",
)
OPTIONAL_EVIDENCE_FILES = ("distribution_smoke.json", "ui_campaign_selection_tests.txt", "hyw_ui_tests.txt")
REBUILD_BASELINE = "IRGS_Core_Engine_v3_3_Unification_Candidate_R8.md"


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def relative_name(name):
    if not isinstance(name, str) or not name or "\\" in name or "\x00" in name or ":" in name:
        raise ValueError(f"invalid distribution path: {name!r}")
    path = PurePosixPath(name)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in name.split("/")):
        raise ValueError(f"non-relative distribution path: {name!r}")
    if any(part.casefold() in FORBIDDEN_PARTS for part in path.parts):
        raise ValueError(f"campaign/cache path cannot be packaged: {name}")
    if path.suffix.casefold() in FORBIDDEN_SUFFIXES:
        raise ValueError(f"archive/log/cache payload cannot be packaged: {name}")
    return path


def safe_file(base, name):
    relative_name(name)
    path = (base / name).resolve(strict=True)
    if not path.is_relative_to(base.resolve()) or not path.is_file():
        raise ValueError(f"payload escapes its distribution root: {name}")
    return path


def validate_final_evidence(release):
    if release.get("selected_core") != "3.3" or release.get("scope") != "CORE_GENRES_LIBRARIES":
        raise ValueError("a selected suite-level Core 3.3 release is required")
    audit = read_json(ROOT / "results/completion_audit.json")
    live = read_json(ROOT / "results/live_activation.json")
    if audit.get("release_id") != release.get("release_id"):
        raise ValueError("completion audit belongs to another release")
    requirements = audit.get("requirements", {})
    if not requirements or any(result != "PASS" for result in requirements.values()):
        raise ValueError("all completion audit requirements must pass before packaging")
    if audit.get("validation") != release.get("validation"):
        raise ValueError("completion and release validation evidence differ")
    # The first extraction smoke run can precede the audit's final completion
    # label. Live activation itself must already have independent evidence.
    if live.get("status") != "LIVE_VERIFIED":
        raise ValueError("activation record must say LIVE_VERIFIED")
    expected = {"core": "3.3", "genre_engines": release["genre_count"],
                "content_libraries": release["library_count"],
                "campaign_profiles": release["campaign_profiles"],
                "ast_classification": "campaign_library", "canonical_horse": "Abel",
                "startup_hash_verification": True}
    for key, value in expected.items():
        if live.get(key) != value:
            raise ValueError(f"live activation evidence differs: {key}")
    if release.get('historical_settings'):
        if live.get('historical_entries') != 37 or live.get('developed_historical_opening') != 'hyw-1415':
            raise ValueError('live historical setting must match the selected content edition')
    if release.get('content_edition') in ('SOLO-GAMEPLAY-2026-10-19','DESIGN-PATCH-2026-10-20'):
        for key in ('solo_character_review', 'filtered_player_views', 'temporal_registry', 'detailed_entry_briefing', 'on_demand_launcher_verified'):
            if live.get(key) is not True:
                raise ValueError('live Solo activation evidence missing: ' + key)
    if release.get('content_edition') == 'DESIGN-PATCH-2026-10-20':
        for key in ('content_library_one_campaign','exact_entry_launch','scoped_feature_routes','actor_known_opening',
                    'background_testimony','historical_plan_assessment','ast_named_start_reference'):
            if live.get(key) is not True:
                raise ValueError('live design integration evidence missing: ' + key)


def collect_payload(release):
    payload = {}
    folded = set()

    def add(name, source, role, expected=None):
        relative_name(name)
        if name.casefold() in folded:
            if name in payload and payload[name]["source"] == source and payload[name]["sha256"] == expected:
                return
            raise ValueError(f"duplicate or Windows-case-colliding payload path: {name}")
        actual = sha256(source)
        if expected is not None:
            if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
                raise ValueError(f"invalid release digest: {name}")
            if actual != expected:
                raise ValueError(f"stale release digest; rebuild the final release first: {name}")
        folded.add(name.casefold())
        payload[name] = {"source": source, "sha256": actual, "bytes": source.stat().st_size,
                         "role": role}

    suite_allowlist = release.get("files_sha256")
    host_allowlist = release.get("host_sha256")
    if not isinstance(suite_allowlist, dict) or not suite_allowlist:
        raise ValueError("release.files_sha256 must be a nonempty allowlist")
    if not isinstance(host_allowlist, dict) or not host_allowlist:
        raise ValueError("release.host_sha256 must be a nonempty allowlist")
    for name, digest in sorted(suite_allowlist.items()):
        parts = relative_name(name).parts
        if not ((len(parts) == 1 and name in SUITE_TOP_FILES)
                or (len(parts) > 1 and parts[0] in SUITE_PAYLOAD_DIRS)):
            raise ValueError(f"obsolete or unapproved suite payload in release allowlist: {name}")
        add("IRGS_3_3/" + name, safe_file(ROOT, name), "release_allowlist", digest)
    host_root = WORKSPACE / "IRGS_Web"
    for name, digest in sorted(host_allowlist.items()):
        parts = relative_name(name).parts
        if len(parts) < 2 or parts[0] != "IRGS_Web":
            raise ValueError(f"host allowlist path must start with IRGS_Web/: {name}")
        host_name = PurePosixPath(*parts[1:]).as_posix()
        if not ((len(parts) == 2 and host_name in HOST_TOP_FILES)
                or (len(parts) > 2 and parts[1] in HOST_PAYLOAD_DIRS)):
            raise ValueError(f"unapproved host payload in release allowlist: {name}")
        add(name, safe_file(host_root, host_name), "host_allowlist", digest)
    add("IRGS_3_3/release.json", safe_file(ROOT, "release.json"), "release_selection")
    for name in ("package_release.py", REBUILD_BASELINE):
        archive_name = "IRGS_3_3/" + name
        if archive_name not in payload:
            add(archive_name, safe_file(ROOT, name), "packaging_script" if name.endswith(".py") else "required_rebuild_baseline")
    evidence = list(EVIDENCE_FILES) + [name for name in OPTIONAL_EVIDENCE_FILES
                                     if (ROOT / "results" / name).is_file()]
    for name in evidence:
        if name == 'distribution_smoke.json' and read_json(ROOT/'results'/name).get('release_manifest_sha256') != sha256(ROOT/'release.json'):
            # A prior edition's extraction report is not this edition's proof.
            continue
        if Path(name).suffix not in {".json", ".txt"} or "package" in name.casefold():
            raise ValueError(f"invalid selected evidence name: {name}")
        add("IRGS_3_3/results/" + name, safe_file(ROOT, "results/" + name), "selected_release_evidence")
    if "IRGS_3_3/results/package_verification.json" in payload:
        raise ValueError("package evidence must not refer to its own archive")
    return payload


def verify_archive(path, expected_manifest):
    with zipfile.ZipFile(path, "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise ValueError(f"archive CRC verification failed: {bad}")
        names = archive.namelist()
        expected = {row["path"]: row for row in expected_manifest["files"]}
        if len(names) != len(set(names)) or set(names) != set(expected) | {MANIFEST_NAME}:
            raise ValueError("archive member inventory differs from its exact manifest")
        manifest = json.loads(archive.read(MANIFEST_NAME))
        if manifest != expected_manifest:
            raise ValueError("internal package manifest differs")
        for name, row in expected.items():
            relative_name(name)
            info = archive.getinfo(name)
            digest = hashlib.sha256()
            with archive.open(name) as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(block)
            if info.file_size != row["bytes"] or digest.hexdigest() != row["sha256"]:
                raise ValueError(f"archive payload hash/size verification failed: {name}")
    return {"testzip": "PASS", "payload_hashes": "PASS", "exact_member_inventory": "PASS"}


def main():
    release = read_json(ROOT / "release.json")
    validate_final_evidence(release)
    payload = collect_payload(release)
    manifest = {"schema_version": 1, "release_id": release["release_id"], "version": "3.3",
        "distribution_roots": ["IRGS_3_3", "IRGS_Web"],
        "files": [{"path": name, **{key: row[key] for key in ("sha256", "bytes", "role")}}
                  for name, row in sorted(payload.items())],
        "payload_files": len(payload), "payload_bytes": sum(row["bytes"] for row in payload.values()),
        "manifest_scope": "Every payload member is hashed; this manifest excludes its own bytes",
        "evidence_scope": "Current selected JSON/TXT release evidence; no previous packaging evidence",
        "excluded": ["Actual campaign saves", "Live state", "Backups", "Caches", "Log files",
                     "Obsolete standalone AST release documents", "Previous archive verification reports"],
        "rebuild_note": "The inherited R8 baseline is included. Full source-catalogue rebuild and preservation audits still require the original local authoring sources and protected campaign backups; those are intentionally not distributed."}
    target = WORKSPACE / ARCHIVE_NAME
    temporary = WORKSPACE / (ARCHIVE_NAME + ".tmp")
    if temporary.exists():
        raise FileExistsError(f"unfinished temporary archive already exists; inspect before retry: {temporary}")
    try:
        with zipfile.ZipFile(temporary, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name, row in sorted(payload.items()):
                archive.write(row["source"], name)
            archive.writestr(MANIFEST_NAME, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        verification = verify_archive(temporary, manifest)
        # Check that the selection itself did not change during packaging.
        if sha256(ROOT / "release.json") != payload["IRGS_3_3/release.json"]["sha256"]:
            raise ValueError("release selection changed during packaging")
        temporary.replace(target)
    except BaseException:
        if temporary.exists():
            temporary.unlink()
        raise
    archive_hash = sha256(target)
    checksum_path = WORKSPACE / (ARCHIVE_NAME + ".sha256")
    checksum_path.write_text(f"{archive_hash}  {ARCHIVE_NAME}\n", encoding="ascii")
    report = {"status": "VERIFIED", "release_id": release["release_id"], "archive": ARCHIVE_NAME,
        "sha256": archive_hash, "bytes": target.stat().st_size,
        "payload_files": len(payload), "archive_members": len(payload) + 1,
        "payload_bytes": manifest["payload_bytes"], "internal_manifest": MANIFEST_NAME,
        "external_checksum": checksum_path.name, "verification": verification,
        "campaign_saves_included": False, "previous_package_evidence_included": False,
        "self_reference": False}
    # This result is intentionally produced only after the completed ZIP exists,
    # and is excluded from all evidence additions on every subsequent build.
    report_path = ROOT / "results/package_verification.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
