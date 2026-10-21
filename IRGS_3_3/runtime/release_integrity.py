"""Startup verification for the selected local Core + genres + libraries suite."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def verify_release():
    release=json.loads((ROOT/'release.json').read_text(encoding='utf-8'))
    if release.get('selected_core')!='3.3' or release.get('scope')!='CORE_GENRES_LIBRARIES':
        raise RuntimeError('No active suite-level Core 3.3 binding')
    for name,expected in release['files_sha256'].items():
        path=(ROOT/name).resolve()
        if not path.is_relative_to(ROOT.resolve()):raise RuntimeError('Invalid release path')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:raise RuntimeError('Release hash mismatch: '+name)
    for name,expected in release.get('host_sha256',{}).items():
        path=(ROOT.parent/name).resolve()
        if not path.is_relative_to(ROOT.parent.resolve()):raise RuntimeError('Invalid host path')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:raise RuntimeError('Host hash mismatch: '+name)
    return release
