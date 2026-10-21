"""Package exactly the verified portable development inventory, never user data."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

from verify_development import ROOT, MANIFEST, safe_path, verify


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT.parent / "IRGS_3_3_3_Development_D1.zip")
    args = parser.parse_args()
    temporary = None
    try:
        verification = verify()
        manifest = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
        output = args.output.resolve()
        if output.is_relative_to(ROOT):
            raise ValueError("Write the development archive outside its source directory")
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary = output.with_name(output.name + ".tmp")
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for entry in manifest["files"]:
                path = safe_path(ROOT, entry["path"])
                data = path.read_bytes()
                if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
                    raise ValueError("Source changed after verification: " + entry["path"])
                archive.writestr("IRGS_Development/" + entry["path"], data)
            archive.writestr("IRGS_Development/" + MANIFEST, (ROOT / MANIFEST).read_bytes())
        temporary.replace(output)
        checksum = hashlib.sha256(output.read_bytes()).hexdigest()
        checksum_path = output.with_name(output.name + ".sha256")
        checksum_path.write_text(checksum + "  " + output.name + "\n", encoding="utf-8")
        print(json.dumps({"status": "packaged", "archive": str(output), "sha256": checksum,
                          "archive_files": len(manifest["files"]) + 1,
                          "verification": verification, "campaigns_included": False}, sort_keys=True))
    except Exception as error:
        if temporary is not None and temporary.is_file():
            temporary.unlink()
        print(json.dumps({"status": "failed", "error": str(error)}, sort_keys=True))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
