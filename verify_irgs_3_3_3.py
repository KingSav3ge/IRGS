#!/usr/bin/env python3
"""Verify an assembled IRGS 3.3.3 folder against IRGS_3_3_3_PACKAGE_MANIFEST.json (standard library only).

Usage:  python verify_irgs_3_3_3.py <assembled-folder> [--manifest PATH] [--zips-dir DIR] [--no-release]
Checks, in order: (1) each package zip hash (if --zips-dir is given), (2) every manifest file exists with the
recorded SHA-256, (3) nothing unexpected sits in the pinned trees (saves, __pycache__ and logs are ignored),
(4) IRGS's own release verification (irgs.py verify). Never modifies anything.
"""
import argparse, hashlib, json, os, subprocess, sys
IGNORED_PARTS = {'__pycache__', 'saves', 'backups', '.git'}; IGNORED_SUFFIX = ('.pyc', '.pyo', '.log')
def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''): h.update(chunk)
    return h.hexdigest()
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('folder'); ap.add_argument('--manifest'); ap.add_argument('--zips-dir'); ap.add_argument('--no-release', action='store_true')
    a = ap.parse_args(); here = os.path.dirname(os.path.abspath(__file__))
    mpath = a.manifest or os.path.join(here, 'IRGS_3_3_3_PACKAGE_MANIFEST.json'); m = json.load(open(mpath, encoding='utf-8'))
    problems = []; expected = {}
    for pid, pkg in m['packages'].items():
        if a.zips_dir:
            zp = os.path.join(a.zips_dir, pkg['zip'])
            if not os.path.isfile(zp): problems.append(f'missing zip {pkg["zip"]}')
            elif sha(zp) != pkg['zip_sha256']: problems.append(f'zip hash mismatch {pkg["zip"]}')
        expected.update(pkg['files_sha256'])
    for rel, want in expected.items():
        p = os.path.join(a.folder, *rel.split('/'))
        if not os.path.isfile(p): problems.append('missing ' + rel)
        elif sha(p) != want: problems.append('hash mismatch ' + rel)
    for top in {r.split('/')[0] for r in expected}:
        for r, d, fs in os.walk(os.path.join(a.folder, top)):
            d[:] = [x for x in d if x not in IGNORED_PARTS]
            for f in fs:
                rel = os.path.relpath(os.path.join(r, f), a.folder).replace(os.sep, '/')
                if rel not in expected and not f.endswith(IGNORED_SUFFIX): problems.append('unexpected ' + rel)
    print(f'manifest files checked: {len(expected)} | edition {m["release_edition"]} | core {m["core_version"]}')
    if not a.no_release:
        rp = subprocess.run([sys.executable, '-B', os.path.join(a.folder, 'IRGS_3_3', 'runtime', 'irgs.py'), 'verify'], capture_output=True, text=True)
        ok = rp.returncode == 0 and '"verified"' in rp.stdout
        print('irgs.py verify:', 'verified' if ok else 'FAILED')
        if not ok: problems.append('irgs.py verify failed: ' + (rp.stderr.strip().splitlines() or ['?'])[-1])
    for p in problems: print('PROBLEM:', p)
    print('RESULT:', 'PASS' if not problems else 'FAIL'); return 1 if problems else 0
if __name__ == '__main__': sys.exit(main())
