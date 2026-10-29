"""Verify a development ZIP and serve only its extracted host on loopback.

No existing save is opened. All HTTP requests are GET requests against a fresh
temporary campaign directory. The packaged verifier and host run in fresh
isolated Python processes, without importing a checkout's project modules.
"""
from __future__ import annotations

import argparse
from versioning import archive_name
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import tempfile
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent.parent
PREFIX = "IRGS_Development/"
MAX_UNCOMPRESSED_BYTES = 1024 * 1024 * 1024


def extract_safely(archive: Path, destination: Path) -> tuple[Path, int]:
    """Extract regular entries with a single expected top-level directory."""
    seen: set[str] = set()
    count = 0
    with ZipFile(archive) as zipped:
        entries = zipped.infolist()
        if sum(entry.file_size for entry in entries) > MAX_UNCOMPRESSED_BYTES:
            raise ValueError("Development archive exceeds the extraction limit")
        for entry in entries:
            name = entry.filename
            if not name.startswith(PREFIX) or "\\" in name or ":" in name:
                raise ValueError("Unexpected archive path: " + name)
            relative = name[len(PREFIX):]
            if not relative:
                if entry.is_dir():
                    if "" in seen:
                        raise ValueError("Duplicate archive root")
                    seen.add("")
                    continue
                raise ValueError("The archive root must be a directory")
            parts = relative.rstrip("/").split("/")
            if any(part in ("", ".", "..") for part in parts):
                raise ValueError("Unsafe archive path: " + name)
            if PurePosixPath(relative).is_absolute():
                raise ValueError("Absolute archive path rejected")
            identity = "/".join(parts).casefold()
            if identity in seen:
                raise ValueError("Duplicate archive path: " + name)
            seen.add(identity)
            mode = entry.external_attr >> 16
            kind = stat.S_IFMT(mode)
            if stat.S_ISLNK(mode) or kind not in (0, stat.S_IFREG, stat.S_IFDIR):
                raise ValueError("Non-regular archive entry: " + name)
            if entry.flag_bits & 1:
                raise ValueError("Encrypted archive entries are unsupported")
            target = (destination / "IRGS_Development" / Path(*parts)).resolve()
            if not target.is_relative_to(destination.resolve()):
                raise ValueError("Archive path escaped the temporary directory")
            if entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as output:
                output.write(zipped.read(entry))
            count += 1
    package = destination / "IRGS_Development"
    if not (package / "DEVELOPMENT_MANIFEST.json").is_file():
        raise ValueError("Development manifest is absent")
    return package, count


HOST_PROBE = r'''
import importlib.util
import json
from pathlib import Path
import sys
import threading
import urllib.request

root = Path(sys.argv[1]).resolve()
saves = Path(sys.argv[2]).resolve()
host = root / "IRGS_Web" / "server.py"
sys.path.insert(0, str(host.parent))
spec = importlib.util.spec_from_file_location("irgs_packaged_host", host)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
for name in ("core_world", "campaign_library", "gameplay_views", "features"):
    loaded = sys.modules[name]
    if not Path(loaded.__file__).resolve().is_relative_to(root):
        raise RuntimeError("A project import escaped the extracted package: " + name)
server = module.make_server(port=0, folder=saves)
if server.server_address[0] != "127.0.0.1":
    raise RuntimeError("Smoke host must bind only loopback")
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
base = "http://127.0.0.1:" + str(server.server_port)
checked = []

def get(path, token=None):
    headers = {"X-IRGS-Token": token} if token else {}
    request = urllib.request.Request(base + path, headers=headers, method="GET")
    with opener.open(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError("Unexpected HTTP status: " + path)
        body = response.read()
        if not body:
            raise RuntimeError("Empty HTTP response: " + path)
        checked.append(path)
        return body

try:
    html = get("/")
    if not any(name in html for name in (b"IRGS", b"WorldWard")) or b"/app.js" not in html:
        raise RuntimeError("The packaged page did not reference its application")
    get("/app.js")
    get("/rise.js")
    get("/catalogue.js")
    get("/style.css")
    catalogue = json.loads(get("/api/catalog"))
    core = catalogue.get("core", {})
    if core.get("id") != "IRGS-CORE-3.3" or str(core.get("version")) != "3.3":
        raise RuntimeError("Unexpected selected Core identity")
    if core.get("single_world_per_campaign") is not True:
        raise RuntimeError("Single-world campaign contract was not supplied")
    campaigns = json.loads(get("/api/campaigns"))
    if campaigns.get("campaigns") != []:
        raise RuntimeError("A clean smoke host unexpectedly contained campaigns")
    token = campaigns.get("token")
    if not isinstance(token, str) or len(token) < 16:
        raise RuntimeError("The local session token was not supplied")
    library = json.loads(get("/api/content-library", token))
    if not isinstance(library.get("campaigns"), list):
        raise RuntimeError("The Content Library response was invalid")
    if library.get("portfolio", {}).get("counts", {}).get("total") != 44:
        raise RuntimeError("The campaign portfolio was not packaged")
    after = json.loads(get("/api/campaigns"))
    if after.get("campaigns") != [] or list(saves.rglob("*.json")):
        raise RuntimeError("Read-only smoke inspection created campaign records")
    print(json.dumps({"status":"passed", "loopback_only":True,
        "selected_core":"3.3", "single_world_per_campaign":True,
        "routes_checked":checked, "campaign_files_created":0,
        "project_imports_from_extracted_package":True}))
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)
'''


def child(command: list[str], cwd: Path, *, timeout: int = 180) -> dict:
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    result = subprocess.run(command, cwd=cwd, env=environment,
                            capture_output=True, text=True, timeout=timeout)
    if result.returncode:
        raise RuntimeError("Child check failed: " +
                           (result.stderr.strip() or result.stdout.strip())[-6000:])
    try:
        parsed = json.loads(result.stdout)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass
    for line in reversed(result.stdout.splitlines()):
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    raise RuntimeError("Child check returned no machine-readable result")


def run(archive: Path) -> dict:
    if not __debug__:
        raise RuntimeError("IRGS requires validation; do not use Python -O")
    archive = archive.resolve(strict=True)
    with tempfile.TemporaryDirectory(prefix="irgs-development-smoke-") as temporary:
        destination = Path(temporary)
        package, files = extract_safely(archive, destination)
        verifier = package / "tools" / "verify_development.py"
        verification = child([sys.executable, "-I", "-B", str(verifier)], package)
        saves = destination / "fresh-smoke-campaigns"
        saves.mkdir()
        smoke = child([sys.executable, "-I", "-B", "-c", HOST_PROBE,
                       str(package), str(saves)], package)
        return {"status":"passed", "archive":str(archive),
                "extracted_files":files, "packaged_verification":verification,
                "http_smoke":smoke, "existing_saves_opened":False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", nargs="?", type=Path,
                        default=ROOT.parent / archive_name(ROOT))
    args = parser.parse_args()
    try:
        result = run(args.archive)
    except Exception as error:
        print(json.dumps({"status":"failed", "error":str(error)}))
        return 1
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
