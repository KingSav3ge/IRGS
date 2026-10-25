"""Verify the portable unified development source without modifying campaigns.

Run with Python 3.12+ (never -O). --refresh intentionally updates only the
development file inventory after a reviewed source change. It does not update
the selected release binding or manufacture behavioural acceptance evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = "DEVELOPMENT_MANIFEST.json"
from versioning import release_metadata

SOURCE_DIRS = {"IRGS_3_3", "IRGS_Web", "IRGS_Catalog", "engine", "provenance", "tools"}
ROOT_FILES = {
    ".gitignore", ".gitattributes", "LICENSE", "LICENSE.txt",
    "Start-IRGS.cmd",
}
EXCLUDED_PARTS = {
    ".git", ".hg", ".svn", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", "node_modules", ".venv", "venv", "saves", "trash", "live",
    "development_results", "dist", "credentials", ".aws", ".ssh", ".codex",
    "cache", "caches", ".cache", ".npm", ".yarn", "userdata", "user_data",
    "tmp", "temp", "backups",
}
SECRET_NAME = re.compile(r"(?:^\.env(?:\..*)?$|^(?:credentials?|secrets?)(?:\..*)?$|\.(?:pem|key|p12|pfx|pyc|pyo)$)", re.I)
SECRET_CONTENT = re.compile(
    rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
    rb"gh[pousr]_[A-Za-z0-9]{30,}|AKIA[A-Z0-9]{16}|"
    rb"sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{24,}"
)
C2_SOURCE_MANIFEST_SHA256 = "d446cdd6df14b71339dc46f311718ed924d124e6da64f8f891d8bb57e9d330e4"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def valid_runtime() -> None:
    require(sys.version_info >= (3, 12), "Python 3.12 or newer is required")
    require(not sys.flags.optimize, "Optimized Python (-O) is unsupported")


def relative_parts(value: str) -> tuple[str, ...]:
    require(isinstance(value, str) and bool(value), "Empty or non-text manifest path")
    require("\\" not in value and ":" not in value and "\0" not in value,
            "Non-portable manifest path: " + value)
    path = PurePosixPath(value)
    require(not path.is_absolute() and path.as_posix() == value,
            "Non-canonical manifest path: " + value)
    require(bool(path.parts) and all(part not in {".", "..", ""} for part in path.parts),
            "Unsafe manifest path: " + value)
    return path.parts


def excluded(parts: tuple[str, ...]) -> bool:
    return (any(part.lower() in EXCLUDED_PARTS for part in parts)
            or any(re.fullmatch(r"tmp[a-z0-9_-]{6,}", part, re.I) for part in parts)
            or any(SECRET_NAME.search(part) for part in parts)
            or parts[-1].lower().endswith((".tmp", ".log", ".bak")))


def allowed(value: str) -> bool:
    parts = relative_parts(value)
    if excluded(parts) or value == MANIFEST:
        return False
    if len(parts) == 1:
        return value in ROOT_FILES or Path(value).suffix.lower() in {".md", ".json"}
    return parts[0] in SOURCE_DIRS


def safe_path(base: Path, value: str) -> Path:
    parts = relative_parts(value)
    path = base.joinpath(*parts)
    current = base
    for part in parts:
        current = current / part
        require(not current.is_symlink() and not current.is_junction(),
                "Linked path is not permitted: " + value)
    require(path.resolve().is_relative_to(base.resolve()), "Path escaped package: " + value)
    return path


def sha256(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def inventory() -> list[str]:
    names = []
    for directory in sorted(SOURCE_DIRS):
        base = ROOT / directory
        require(base.is_dir(), "Missing curated source directory: " + directory)
        for current, dirs, files in os.walk(base, followlinks=False):
            retained = []
            for name in sorted(dirs):
                relative = (Path(current) / name).relative_to(ROOT).as_posix()
                if excluded(relative_parts(relative)):
                    continue
                safe_path(ROOT, relative)
                retained.append(name)
            dirs[:] = retained
            for name in sorted(files):
                relative = (Path(current) / name).relative_to(ROOT).as_posix()
                if allowed(relative):
                    require(safe_path(ROOT, relative).is_file(), "Non-regular source: " + relative)
                    names.append(relative)
    for path in sorted(ROOT.iterdir()):
        if path.is_file() and allowed(path.name):
            safe_path(ROOT, path.name)
            names.append(path.name)
    require(len(names) == len(set(names)), "Duplicate source paths")
    require(len(names) == len({name.casefold() for name in names}), "Case-colliding source paths")
    return sorted(names)


def refresh_manifest() -> None:
    names = inventory()
    result = {
        "schema_version": 1,
        "development_edition": release_metadata(ROOT)["version"],
        "previous_version": release_metadata(ROOT)["previous_version"],
        "release_status": "development",
        "manifest_excludes_itself": True,
        "scope": "curated portable development source; user data and generated local results excluded",
        "source_directories": sorted(SOURCE_DIRS),
        "files": [{"path": name, "bytes": (ROOT / name).stat().st_size,
                   "sha256": sha256(ROOT / name)} for name in names],
    }
    temporary = ROOT / (MANIFEST + ".tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(ROOT / MANIFEST)


def check_file_manifest(base: Path, document: dict, *, development: bool = False) -> int:
    rows = document.get("files")
    require(isinstance(rows, list) and bool(rows), "Missing file inventory")
    seen = set()
    for row in rows:
        require(isinstance(row, dict), "Invalid inventory entry")
        name = row.get("path")
        parts = relative_parts(name)
        require(name not in seen and name.casefold() not in {x.casefold() for x in seen},
                "Duplicate inventory path: " + name)
        seen.add(name)
        require(not excluded(parts), "User data/cache/credential entry rejected: " + name)
        if development:
            require(allowed(name), "Unapproved development path: " + name)
        path = safe_path(base, name)
        require(path.is_file(), "Missing file: " + name)
        require(type(row.get("bytes")) is int and path.stat().st_size == row["bytes"],
                "Byte count mismatch: " + name)
        expected = row.get("sha256")
        require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected) is not None,
                "Invalid SHA-256: " + name)
        require(sha256(path) == expected, "SHA-256 mismatch: " + name)
        if path.suffix.lower() in {".py", ".js", ".json", ".md", ".html", ".txt", ".cmd", ".ps1"}:
            require(SECRET_CONTENT.search(path.read_bytes()) is None,
                    "Potential private credential content rejected: " + name)
    if development:
        actual = set(inventory())
        require(seen == actual, "Development inventory differs; review changes before --refresh. "
                + json.dumps({"unlisted": sorted(actual - seen), "missing": sorted(seen - actual)}))
    return len(rows)


def verify_c2() -> dict:
    engine = ROOT / "engine"
    binding = json.loads((engine / "Core/IRGS_Core_3_3_3_E_C2_Binding.json").read_text(encoding="utf-8"))
    document = safe_path(engine, binding["document"])
    require(sha256(document) == binding["sha256"], "Applied C2 engine text hash mismatch")
    require(binding.get("selected_runtime_core") == "3.3", "Unexpected selected runtime Core")
    require(binding.get("runtime_implemented") is False and binding.get("runtime_deployed") is False,
            "C2 design status changed; review the development verifier before adoption")
    source = engine / "design/C2"
    source_manifest_path = source / "PACKAGE_MANIFEST.json"
    require(sha256(source_manifest_path) == C2_SOURCE_MANIFEST_SHA256,
            "Immutable C2 source manifest changed")
    source_manifest = json.loads(source_manifest_path.read_text(encoding="utf-8"))
    source_count = check_file_manifest(source, source_manifest)
    cases = json.loads(safe_path(engine, binding["acceptance_inventory"]).read_text(encoding="utf-8"))
    records = cases.get("cases", [])
    require(cases.get("case_count") == 121 and len(records) == 121,
            "C2's preserved required-case inventory must contain 121 cases")
    identifiers = [case.get("case_id") for case in records]
    require(all(isinstance(value, str) and value for value in identifiers)
            and len(set(identifiers)) == 121, "Invalid C2 case identities")
    require(cases.get("runtime_validation_claimed") is False
            and all(case.get("status") == "REQUIRED_NOT_EXECUTED" for case in records),
            "The immutable C2 source is design inventory, not executed acceptance evidence")
    return {"source_files_verified": source_count, "required_cases": len(records),
            "acceptance_execution_claimed": False}


def verify() -> dict:
    valid_runtime()
    document = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
    require(document.get("schema_version") == 1 and document.get("manifest_excludes_itself") is True,
            "Unsupported development manifest schema")
    edition = release_metadata(ROOT)
    require(document.get("development_edition") == edition["version"]
            and document.get("previous_version") == edition["previous_version"],
            "Development manifest edition differs from VERSION.json")
    count = check_file_manifest(ROOT, document, development=True)
    c2 = verify_c2()
    environment = dict(os.environ)
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    environment["PYTHONOPTIMIZE"] = "0"
    command = [sys.executable, "-B", str(ROOT / "IRGS_3_3/runtime/irgs.py"), "verify"]
    completed = subprocess.run(command, cwd=ROOT, env=environment,
                               capture_output=True, text=True, encoding="utf-8")
    require(completed.returncode == 0, "Selected release integrity failed: "
            + completed.stdout[-1500:] + completed.stderr[-1500:])
    selected = json.loads(completed.stdout)
    require(selected.get("status") == "verified" and selected.get("core") == "3.3",
            "Selected Core verification returned an unexpected result")
    app = subprocess.run([sys.executable, "-B", str(ROOT / "IRGS_Web/app_integrity.py")],
                         cwd=ROOT, env=environment, capture_output=True, text=True)
    require(app.returncode == 0, "App release integrity failed: " + app.stdout[-1500:] + app.stderr[-1500:])
    catalog = subprocess.run([sys.executable, "-B", str(ROOT / "IRGS_Catalog/verify_catalog.py")],
                             capture_output=True, text=True, cwd=ROOT)
    require(catalog.returncode == 0, "Catalog integrity failed: " + catalog.stdout + catalog.stderr)
    return {"status": "verified", "version": edition["version"], "previous_version": edition["previous_version"], "development_files": count, "catalog_release": json.loads(catalog.stdout),
            "selected_release": selected, "app_release": json.loads(app.stdout),
            "c2": c2, "campaigns_modified": False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true",
                        help="regenerate the curated file manifest after reviewing source changes, then verify")
    args = parser.parse_args()
    try:
        valid_runtime()
        if args.refresh:
            refresh_manifest()
        print(json.dumps(verify(), sort_keys=True))
    except Exception as error:
        print(json.dumps({"status": "failed", "error": str(error)}, sort_keys=True))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
