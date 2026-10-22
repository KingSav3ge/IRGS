"""Check campaign catalogue source identity without an Engine or App checkout."""
import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent


def source_files(root):
    return {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()
        and p != root / 'release.json' and '__pycache__' not in p.parts
        and p.suffix not in ('.pyc', '.log', '.tmp', '.bak')}


def safe_path(root, name):
    path = PurePosixPath(name)
    if (not name or path.is_absolute() or path.as_posix() != name
            or '..' in path.parts or '\\' in name or ':' in name):
        raise RuntimeError('Invalid Catalog source path')
    result = root.joinpath(*path.parts)
    if any(p.is_symlink() for p in (result, *result.parents) if p.is_relative_to(root)):
        raise RuntimeError('Linked Catalog source path')
    if not result.resolve().is_relative_to(root.resolve()):
        raise RuntimeError('Catalog source escapes its directory')
    return result


def verify_catalog(root=ROOT):
    release = json.loads((root / 'release.json').read_text(encoding='utf-8'))
    if release.get('component') != 'IRGS-Catalog' or release.get('schema_version') != 1:
        raise RuntimeError('No selected IRGS Catalog binding')
    hashes = release['files_sha256']
    if not hashes or set(hashes) != source_files(root):
        raise RuntimeError('Catalog inventory differs from its release binding')
    for name, expected in hashes.items():
        if hashlib.sha256(safe_path(root, name).read_bytes()).hexdigest() != expected:
            raise RuntimeError('Catalog hash mismatch: ' + name)
    portfolio = json.loads((root / 'data/campaign_portfolio.json').read_text(encoding='utf-8'))
    listings = json.loads((root / 'data/campaign_listings.json').read_text(encoding='utf-8'))
    if (portfolio.get('schema_version') != 1 or not isinstance(portfolio.get('entries'), list)
            or listings.get('schema_version') != 1
            or not isinstance(listings.get('visible_campaign_ids'), list)):
        raise RuntimeError('Unsupported campaign catalogue schema')
    source = portfolio['source']
    prefix = 'IRGS_Catalog/'
    if not source['path'].startswith(prefix):
        raise RuntimeError('Catalogue provenance must identify its owned design source')
    original = safe_path(root, source['path'][len(prefix):])
    if hashlib.sha256(original.read_bytes()).hexdigest() != source['sha256']:
        raise RuntimeError('Catalogue design source hash differs')
    return {'status': 'verified', 'component': 'IRGS-Catalog', 'files': len(hashes),
        'concepts': len(portfolio['entries']), 'campaign_release_approved_by_check': False}


if __name__ == '__main__':
    print(json.dumps(verify_catalog()))
