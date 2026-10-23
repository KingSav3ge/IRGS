"""Build and check Catalog source packages; no runtime or campaign operations.

The complete supplied ZIP is preserved byte for byte. Source data is inspected
without extraction, execution, normalization, or edits to its rights records.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
import zipfile

PART_SIZE = 16 * 1024 * 1024
BLOCK_SIZE = 1024 * 1024
EXPECTED_ARCHIVE = {
    'name': 'IRGS_Historical_Grand_Archive_v1_1.zip',
    'bytes': 533064680,
    'sha256': '51246eb6898a228f42f0794ed19ce69af275a2a4661c0fb6a1d3baebe3efc773',
}
COLLECTIONS = {
    'chronology': '03_Data/archive_chronology_assertions.json',
    'figures': '08_Historical_Character_Library/records.json',
    'research': '03_Data/research_records.jsonl.gz',
    'claims': '03_Data/reviewed_claims.json',
    'sources': '03_Data/archive_source_register.json',
    'rights': '03_Data/merged_rights_inventory.json',
    'concepts': '03_Data/entities.jsonl.gz',
    'places': '03_Data/pleiades_places.jsonl.gz',
    'routes': '03_Data/itiner_routes.jsonl.gz',
    'population': '03_Data/mpd_country_year.jsonl.gz',
}
DEFAULT_MANIFEST = Path(__file__).resolve().parent / 'historical_details/manifest.json'
MAX_MANIFEST = 1024 * 1024
MAX_DELIVERY_MANIFEST = 8 * 1024 * 1024
MAX_INVENTORY = 64 * 1024 * 1024
MAX_COLLECTION = 64 * 1024 * 1024
MAX_EXPANDED = 384 * 1024 * 1024
MAX_ROW = 2 * 1024 * 1024


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key: ' + key)
        result[key] = value
    return result


def _json(data):
    return json.loads(data, object_pairs_hook=_unique_object)


def _hash_stream(stream):
    digest = hashlib.sha256()
    size = 0
    for block in iter(lambda: stream.read(BLOCK_SIZE), b''):
        size += len(block)
        digest.update(block)
    return size, digest.hexdigest()


def _safe_name(name):
    if not isinstance(name, str):
        raise ValueError('Source path must be text')
    path = PurePosixPath(name)
    if (not name or path.is_absolute() or path.as_posix() != name
            or path.parts == () or '..' in path.parts
            or '\\' in name or ':' in name or '\x00' in name):
        raise ValueError('Invalid relative source path: ' + repr(name))
    # Reject Windows device paths and names normalized differently on Windows.
    for part in path.parts:
        if (part.endswith(('.', ' ')) or any(c in part for c in '<>"|?*')
                or any(ord(c) < 32 for c in part)
                or re.fullmatch(r'(?i:con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?', part)):
            raise ValueError('Nonportable source path: ' + repr(name))
    return path


def _contained(root, name):
    parts = _safe_name(name).parts
    path = root.joinpath(*parts)
    if root.is_symlink() or any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('Linked package source path')
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Package source escapes its directory')
    return path


def _identity(archive):
    if (not isinstance(archive, dict) or set(archive) != {'name', 'bytes', 'sha256'}
            or type(archive['bytes']) is not int or archive['bytes'] <= 0
            or not isinstance(archive['sha256'], str)
            or not re.fullmatch(r'[0-9a-f]{64}', archive['sha256'])):
        raise ValueError('Invalid archive identity')
    if len(_safe_name(archive['name']).parts) != 1:
        raise ValueError('Archive name must be a filename')


def load_manifest(path=DEFAULT_MANIFEST, *, expected_archive=EXPECTED_ARCHIVE):
    path = Path(path)
    if path.is_symlink() or path.stat().st_size > MAX_MANIFEST:
        raise ValueError('Linked or oversized package manifest')
    document = _json(path.read_bytes())
    if (not isinstance(document, dict) or type(document.get('schema_version')) is not int
            or document['schema_version'] != 1 or document.get('id') != 'historical-details'
            or document.get('display_name') != 'Historical Details'
            or document.get('part_size_bytes') != PART_SIZE):
        raise ValueError('Unsupported Historical Details manifest')
    _identity(document.get('archive'))
    if document['archive'] != expected_archive:
        raise ValueError('Package identifies a different source archive')
    if document.get('status') not in ('complete', 'blocked_missing_source'):
        raise ValueError('Unsupported Historical Details completion status')
    if not isinstance(document.get('parts'), list):
        raise ValueError('Missing package part inventory')
    return document


def _collection_count(archive, name):
    info = archive.getinfo(name)
    if info.file_size > MAX_COLLECTION:
        raise ValueError('Collection exceeds the bounded indexing capacity: ' + name)
    with archive.open(info) as source:
        if name.endswith('.jsonl.gz'):
            total = count = 0
            with gzip.GzipFile(fileobj=source) as rows:
                while True:
                    line = rows.readline(MAX_ROW + 1)
                    if not line:
                        break
                    total += len(line)
                    if len(line) > MAX_ROW or total > MAX_EXPANDED:
                        raise ValueError('Collection exceeds the bounded indexing capacity: ' + name)
                    if line.strip():
                        if not isinstance(_json(line), dict):
                            raise ValueError('Collection row must be an object: ' + name)
                        count += 1
            return count
        rows = _json(source.read(MAX_COLLECTION + 1))
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise ValueError('Collection must contain object rows: ' + name)
        return len(rows)


def inspect_archive(path):
    """Verify every ZIP member and every declared binding, including non-reader data."""
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len(set(names)):
            raise ValueError('Duplicate archive member')
        for name in names:
            _safe_name(name.rstrip('/'))
        manifests = [name for name in names if len(PurePosixPath(name).parts) == 3
                     and name.endswith('/07_Verification/delivery_manifest.json')]
        if len(manifests) != 1:
            raise ValueError('A single Grand Archive delivery manifest is required')
        manifest_name = manifests[0]
        if archive.getinfo(manifest_name).file_size > MAX_DELIVERY_MANIFEST:
            raise ValueError('Archive delivery manifest is too large')
        delivery = _json(archive.read(manifest_name))
        if (not isinstance(delivery, dict) or delivery.get('edition') != 'Grand 1.1'
                or not isinstance(delivery.get('files'), list)):
            raise ValueError('Unsupported Grand Archive delivery manifest')
        prefix = manifest_name.removesuffix('07_Verification/delivery_manifest.json')
        bindings = {}
        for row in delivery['files']:
            if not isinstance(row, dict):
                raise ValueError('Invalid delivery binding')
            name = row.get('path')
            _safe_name(name)
            if name in bindings or type(row.get('bytes')) is not int or row['bytes'] < 0:
                raise ValueError('Duplicate or invalid delivery binding')
            if not isinstance(row.get('sha256'), str) or not re.fullmatch(r'[0-9a-f]{64}', row['sha256']):
                raise ValueError('Invalid delivery hash')
            bindings[name] = row
        members = []
        by_name = {}
        for ordinal, info in enumerate(infos, 1):
            if info.is_dir():
                continue
            with archive.open(info) as stream:
                size, digest = _hash_stream(stream)
            if size != info.file_size:
                raise ValueError('Archive member size differs: ' + info.filename)
            member = {'ordinal': ordinal, 'path': info.filename, 'bytes': size, 'sha256': digest,
                      'delivery_manifest_bound': False}
            members.append(member)
            by_name[info.filename] = member
        for name, binding in bindings.items():
            member = by_name.get(prefix + name)
            if not member or (member['bytes'], member['sha256']) != (binding['bytes'], binding['sha256']):
                raise ValueError('Archive delivery binding differs: ' + name)
            member['delivery_manifest_bound'] = True
        collections = []
        for collection, relative in COLLECTIONS.items():
            member = by_name.get(prefix + relative)
            if relative not in bindings or member is None:
                raise ValueError('Required collection has no delivery binding: ' + collection)
            collections.append({'id': collection, 'member': prefix + relative,
                                'bytes': member['bytes'], 'sha256': member['sha256'],
                                'record_count': _collection_count(archive, prefix + relative)})
        unbound = [row['path'] for row in members if not row['delivery_manifest_bound']]
        return {'archive_bytes': 'complete', 'member_inventory': 'complete',
                'delivery_manifest': manifest_name, 'delivery_bindings_verified': len(bindings),
                'unbound_members': unbound, 'members': members, 'collections': collections,
                'reader_collections': 'partial_view_of_complete_archive',
                'historical_truth_verified': False, 'rights_expanded': False,
                'campaign_adoption_performed': False}


def _inventory_document(coverage, identity):
    return {'schema_version': 1, 'archive': dict(identity),
            'members': coverage['members'], 'unbound_members': coverage['unbound_members']}


def _coverage_summary(coverage, inventory_bytes):
    # Thousands of original members need a separate index. Keep the runtime
    # selection manifest below the Engine reader's 1 MiB bound.
    return {**{k: v for k, v in coverage.items()
               if k not in ('members', 'unbound_members', 'member_inventory')},
            'unbound_member_count': len(coverage['unbound_members']),
            'member_inventory': {'path': 'member_inventory.json', 'bytes': len(inventory_bytes),
                                 'sha256': hashlib.sha256(inventory_bytes).hexdigest(),
                                 'member_count': len(coverage['members'])}}


def _assemble(document, root, target):
    parts = document['parts']
    identity = document['archive']
    expected_count = (identity['bytes'] + PART_SIZE - 1) // PART_SIZE
    if len(parts) != expected_count:
        raise ValueError('Incomplete archive part inventory')
    names = set()
    total = 0
    digest = hashlib.sha256()
    for ordinal, row in enumerate(parts, 1):
        if not isinstance(row, dict):
            raise ValueError('Invalid archive part record')
        name = row.get('path')
        expected_name = f"parts/{identity['name']}.part{ordinal:04d}"
        if (type(row.get('ordinal')) is not int or row['ordinal'] != ordinal
                or name != expected_name or name in names):
            raise ValueError('Duplicate, reordered or invalid archive part')
        names.add(name)
        size = min(PART_SIZE, identity['bytes'] - total)
        if type(row.get('bytes')) is not int or row['bytes'] != size:
            raise ValueError('Invalid archive part size')
        part = _contained(root, name)
        if not part.is_file() or part.stat().st_size != size:
            raise ValueError('Missing or truncated archive part: ' + name)
        actual = hashlib.sha256()
        read = 0
        with part.open('rb') as stream:
            for block in iter(lambda: stream.read(BLOCK_SIZE), b''):
                read += len(block)
                if read > size:
                    raise ValueError('Archive part grew during verification')
                digest.update(block)
                actual.update(block)
                target.write(block)
        if read != size or actual.hexdigest() != row.get('sha256'):
            raise ValueError('Archive part hash mismatch: ' + name)
        total += read
    part_dir = _contained(root, 'parts')
    actual_names = {p.relative_to(root).as_posix() for p in part_dir.rglob('*')}
    if actual_names != names:
        raise ValueError('Unrecorded or duplicate package parts')
    if total != identity['bytes'] or digest.hexdigest() != identity['sha256']:
        raise ValueError('Reassembled archive identity differs')


def verify_package(manifest=DEFAULT_MANIFEST, *, expected_archive=EXPECTED_ARCHIVE, output=None):
    """Verify reassembly and source bindings; optionally publish a new verified ZIP."""
    manifest = Path(manifest)
    document = load_manifest(manifest, expected_archive=expected_archive)
    if document['status'] != 'complete':
        raise ValueError('Historical Details source archive is unavailable; import remains blocked')
    output = Path(output) if output is not None else None
    # Reconstruction is temporary until all hashes and member bindings agree.
    with tempfile.TemporaryDirectory(prefix='irgs-historical-check-') as temp:
        assembled = Path(temp) / 'source.zip'
        with assembled.open('wb') as stream:
            _assemble(document, manifest.parent, stream)
        coverage = inspect_archive(assembled)
        inventory_path = _contained(manifest.parent, 'member_inventory.json')
        if not inventory_path.is_file() or inventory_path.stat().st_size > MAX_INVENTORY:
            raise ValueError('Missing or oversized archive member inventory')
        inventory_bytes = inventory_path.read_bytes()
        if (_json(inventory_bytes) != _inventory_document(coverage, document['archive'])
                or document.get('coverage') != _coverage_summary(coverage, inventory_bytes)):
            raise ValueError('Archive member/collection coverage differs from the manifest')
        if document.get('source_verification') != 'verified_from_complete_payload':
            raise ValueError('Source verification status differs')
        if output is not None:
            # Never replace an installation's existing source or a package part.
            created = False
            try:
                with output.open('xb') as target:
                    created = True
                    with assembled.open('rb') as source:
                        for block in iter(lambda: source.read(BLOCK_SIZE), b''):
                            target.write(block)
            except BaseException:
                if created:
                    output.unlink(missing_ok=True)
                raise
    return {'status': 'verified', 'parts': len(document['parts']),
            'archive': document['archive'], 'archive_coverage': 'complete',
            'members_verified': len(coverage['members']),
            'delivery_bindings_verified': coverage['delivery_bindings_verified'],
            'collection_bindings_verified': len(coverage['collections']),
            'unbound_members': coverage['unbound_members'], 'historical_truth_verified': False,
            'campaign_adoption_performed': False}


def package_status(manifest=DEFAULT_MANIFEST):
    """Catalog verification can report a truthful, validated missing-source state."""
    document = load_manifest(manifest)
    if document['status'] == 'blocked_missing_source':
        if (document['parts'] or document.get('source_verification') != 'not_run_missing_source'
                or document.get('coverage') != {'archive_bytes': 'unavailable',
                                               'member_inventory': 'not_run', 'collections': []}
                or (Path(manifest).parent / 'parts').exists()
                or (Path(manifest).parent / 'parts').is_symlink()):
            raise ValueError('Blocked package contains inconsistent payload claims')
        return {'status': 'blocked_missing_source', 'payload_present': False,
                'source_identity_verified': False, 'complete_archive_verified': False}
    return verify_package(manifest)


def build_package(source, destination, *, expected_archive=EXPECTED_ARCHIVE):
    """Create a new package atomically; never overwrite an existing import."""
    _identity(expected_archive)
    source, destination = Path(source), Path(destination)
    if destination.exists() or destination.is_symlink():
        raise ValueError('Import destination already exists; use a new reviewed directory')
    if source.is_symlink() or not source.is_file():
        raise ValueError('An accessible original source ZIP is required')
    with source.open('rb') as stream:
        size, digest = _hash_stream(stream)
    if (size, digest) != (expected_archive['bytes'], expected_archive['sha256']):
        raise ValueError('Original archive does not match the expected size and SHA-256')
    with tempfile.TemporaryDirectory(prefix='.historical-import-', dir=destination.parent) as temp:
        staging = Path(temp) / 'package'
        (staging / 'parts').mkdir(parents=True)
        parts = []
        with source.open('rb') as stream:
            ordinal = 1
            while block := stream.read(PART_SIZE):
                name = f"parts/{expected_archive['name']}.part{ordinal:04d}"
                (staging / name).write_bytes(block)
                parts.append({'ordinal': ordinal, 'path': name, 'bytes': len(block),
                              'sha256': hashlib.sha256(block).hexdigest()})
                ordinal += 1
        coverage = inspect_archive(source)
        inventory_bytes = (json.dumps(_inventory_document(coverage, expected_archive),
                                     indent=2, ensure_ascii=False) + '\n').encode('utf-8')
        (staging / 'member_inventory.json').write_bytes(inventory_bytes)
        document = {'schema_version': 1, 'id': 'historical-details',
                    'display_name': 'Historical Details', 'status': 'complete',
                    'archive': dict(expected_archive), 'part_size_bytes': PART_SIZE,
                    'parts': parts, 'source_verification': 'verified_from_complete_payload',
                    'coverage': _coverage_summary(coverage, inventory_bytes)}
        manifest = staging / 'manifest.json'
        manifest.write_text(json.dumps(document, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        # Recheck the staged bytes, not a promise about the original path.
        verify_package(manifest, expected_archive=expected_archive)
        if destination.exists() or destination.is_symlink():
            raise ValueError('Import destination appeared during verification')
        os.rename(staging, destination)
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    verify = commands.add_parser('verify')
    verify.add_argument('manifest', nargs='?', type=Path, default=DEFAULT_MANIFEST)
    assemble = commands.add_parser('reassemble')
    assemble.add_argument('manifest', type=Path)
    assemble.add_argument('output', type=Path)
    build = commands.add_parser('import-archive')
    build.add_argument('source', type=Path)
    build.add_argument('destination', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'import-archive':
            result = build_package(args.source, args.destination)
            result = {'status': result['status'], 'parts': len(result['parts']),
                      'archive': result['archive']}
        else:
            result = verify_package(args.manifest, output=getattr(args, 'output', None))
    except (ValueError, OSError, KeyError, zipfile.BadZipFile, EOFError, RuntimeError) as error:
        parser.exit(2, json.dumps({'status': 'unavailable_or_invalid', 'error': str(error)[:500]}) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
