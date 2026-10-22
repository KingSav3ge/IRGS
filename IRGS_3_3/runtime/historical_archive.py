"""Read-only findings from a separately supplied, pinned historical ZIP.

This provider has no world, event dispatcher, adoption procedure or save access.
Archive prose and source assertions are data, never executable instructions.
"""
from __future__ import annotations

import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import threading
import zipfile

COLLECTIONS = {
    'chronology': ('Chronology assertions', '03_Data/archive_chronology_assertions.json'),
    'figures': ('Historical figure references', '08_Historical_Character_Library/records.json'),
    'research': ('Research, economics, institutions and operations', '03_Data/research_records.jsonl.gz'),
    'claims': ('Reviewed historical claims', '03_Data/reviewed_claims.json'),
    'sources': ('Sources and citations', '03_Data/archive_source_register.json'),
    'rights': ('Rights and attribution records', '03_Data/merged_rights_inventory.json'),
    'concepts': ('Source concept catalogue', '03_Data/entities.jsonl.gz'),
    'places': ('Historical place references', '03_Data/pleiades_places.jsonl.gz'),
    'routes': ('Reconstructed route references', '03_Data/itiner_routes.jsonl.gz'),
    'population': ('Country-year economic estimates', '03_Data/mpd_country_year.jsonl.gz'),
}
NOTICE = ('Historical research for the Creator. Assertions, reconstructions and game-source '
          'concepts retain their supplied status. Reading creates no campaign facts, people, '
          'resources, character knowledge or scheduled outcomes.')
MAX_MEMBER = 64 * 1024 * 1024
MAX_EXPANDED = 384 * 1024 * 1024
MAX_ROW = 2 * 1024 * 1024


def file_hash(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()


def _safe_name(name):
    p = PurePosixPath(name)
    return bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name and ':' not in name


class HistoricalArchive:
    def __init__(self, path, sha256):
        self.path = Path(path)
        if not isinstance(sha256, str) or not re.fullmatch(r'[0-9a-f]{64}', sha256):
            raise ValueError('A pinned historical archive SHA-256 is required')
        self.sha256 = sha256
        self._stamp = None
        self._manifest = {}
        self._prefix = None
        self._lock = threading.RLock()

    def _stat(self):
        stat = self.path.stat()
        return (stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns, stat.st_ino)

    def _ready(self):
        stamp = self._stat()
        if self._stamp == stamp:
            return
        # A changed attachment must match the pinned bytes before any cached use.
        if file_hash(self.path) != self.sha256 or self._stat() != stamp:
            raise ValueError('Historical archive changed; register the intended source again')
        with zipfile.ZipFile(self.path) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)) or any(not _safe_name(n.rstrip('/')) for n in names):
                raise ValueError('Historical archive contains ambiguous or unsafe paths')
            manifests = [n for n in names if len(PurePosixPath(n).parts) == 3
                         and n.endswith('/07_Verification/delivery_manifest.json')]
            if len(manifests) != 1:
                raise ValueError('A single Grand Archive delivery manifest is required')
            self._prefix = manifests[0].removesuffix('07_Verification/delivery_manifest.json')
            info = archive.getinfo(manifests[0])
            if info.file_size > 8 * 1024 * 1024:
                raise ValueError('Historical archive manifest is too large')
            document = json.loads(archive.read(info))
            if not isinstance(document, dict):
                raise ValueError('Unsupported historical archive manifest')
            rows = document.get('files')
            if document.get('edition') != 'Grand 1.1' or not isinstance(rows, list):
                raise ValueError('Unsupported historical archive manifest')
            manifest = {}
            for row in rows:
                if not isinstance(row, dict):
                    raise ValueError('Invalid historical archive manifest row')
                name = row.get('path', '')
                if not _safe_name(name) or name in manifest:
                    raise ValueError('Ambiguous historical archive manifest')
                manifest[name] = row
            self._manifest = manifest
        if self._stat() != stamp:
            raise ValueError('Historical archive changed during inspection')
        self._stamp = stamp

    def _bytes(self, name):
        self._ready()
        row = self._manifest.get(name)
        if not row:
            raise ValueError('Historical collection has no source-integrity record')
        with zipfile.ZipFile(self.path) as archive:
            info = archive.getinfo(self._prefix + name)
            if info.file_size > MAX_MEMBER or info.file_size != row.get('bytes'):
                raise ValueError('Historical collection exceeds its declared size')
            data = archive.read(info)
        if hashlib.sha256(data).hexdigest() != row.get('sha256') or self._stat() != self._stamp:
            raise ValueError('Historical collection source-integrity mismatch')
        return data

    def _rows(self, collection):
        if collection not in COLLECTIONS:
            raise ValueError('Unknown historical reference collection')
        name = COLLECTIONS[collection][1]
        data = self._bytes(name)
        if name.endswith('.jsonl.gz'):
            with gzip.GzipFile(fileobj=io.BytesIO(data)) as stream:
                total = 0
                while True:
                    line = stream.readline(MAX_ROW + 1)
                    if not line:
                        break
                    total += len(line)
                    if len(line) > MAX_ROW or total > MAX_EXPANDED:
                        raise ValueError('Historical collection exceeds the bounded reader capacity')
                    if line.strip():
                        row = json.loads(line)
                        if not isinstance(row, dict):
                            raise ValueError('Historical reference row must be an object')
                        yield row
        else:
            rows = json.loads(data)
            if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
                raise ValueError('Historical reference collection must contain object rows')
            yield from rows

    def status(self):
        with self._lock:
            self._ready()
            return {'id': 'historical-grand-archive', 'title': 'Historical Grand Archive',
                    'edition': '1.1', 'status': 'attached_read_only', 'sha256': self.sha256,
                    'notice': NOTICE, 'campaign_effects': False,
                    'collections': [{'id': key, 'title': title} for key, (title, name) in COLLECTIONS.items()
                                    if name in self._manifest],
                    'scope': 'Structured chronology, figures, research, citations, rights, concepts, places, routes and country-year estimates. Raw game files, books and the central database remain in the external archive.'}

    def verify_collections(self):
        with self._lock:
            status = self.status()
            for collection in status['collections']:
                self._bytes(COLLECTIONS[collection['id']][1])
            return status

    def _summary(self, collection, index, row):
        payload = row.get('payload') if isinstance(row.get('payload'), dict) else row
        title = next((str(payload[key]) for key in ('title', 'source_name', 'name', 'label', 'statement', 'country', 'countryname', 'id')
                      if payload.get(key) is not None), 'Source record')
        if collection == 'population':
            title += ' · ' + str(payload.get('year', 'Year unknown'))
        status = {key: payload[key] for key in ('epistemic_class', 'adoption_status', 'evidence_status',
                  'historicity_status', 'historical_status', 'delivery_status', 'slot_status', 'rights_status',
                  'status', 'certainty', 'label_status', 'historical_origin_status', 'historical_end_status') if key in payload}
        dates = {key: payload[key] for key in ('date_text', 'date', 'start', 'end', 'period_text', 'year',
                 'calendar', 'precision', 'start_astronomical', 'end_astronomical', 'lower_date',
                 'lower_date_error', 'upper_date', 'upper_date_error') if key in payload}
        source_id = next((row[key] for key in ('id', 'record_id', 'publisher_id', 'source_row') if key in row), None)
        return {'row': index, 'source_id': source_id, 'title': title[:400],
                'record_type': row.get('record_type', collection), 'source_status': status, 'dates': dates,
                'excerpt': str(payload.get('statement', payload.get('significance_text', payload.get('notes', ''))))[:700],
                'reference': {'archive_sha256': self.sha256, 'collection': collection,
                              'source_file': COLLECTIONS[collection][1], 'row': index}}

    def search(self, collection='chronology', query='', *, offset=0, limit=20):
        if not isinstance(query, str) or len(query) > 200:
            raise ValueError('Use a historical search of at most 200 characters')
        if type(offset) is not int or not 0 <= offset <= 1000000 or type(limit) is not int or not 1 <= limit <= 50:
            raise ValueError('Invalid historical reference page')
        terms = query.casefold().split()
        with self._lock:
            results = []
            matches = 0
            for index, row in enumerate(self._rows(collection), 1):
                text = json.dumps(row, ensure_ascii=False).casefold()
                if not all(term in text for term in terms):
                    continue
                matches += 1
                if matches <= offset:
                    continue
                results.append(self._summary(collection, index, row))
                if len(results) > limit:
                    break
            more = len(results) > limit
            return {'collection': collection, 'query': query, 'offset': offset, 'limit': limit,
                    'results': results[:limit], 'has_more': more,
                    'next_offset': offset + limit if more else None, 'notice': NOTICE,
                    'campaign_effects': False, 'total_matches': None if more else matches}

    def record(self, collection, index):
        if type(index) is not int or index < 1:
            raise ValueError('Invalid historical reference row')
        with self._lock:
            row = next((row for number, row in enumerate(self._rows(collection), 1) if number == index), None)
            if row is None:
                raise ValueError('Historical reference row not found')
            summary = self._summary(collection, index, row)
            payload = row.get('payload') if isinstance(row.get('payload'), dict) else row
            refs = row.get('source_ids', payload.get('source_ids', []))
            if 'source_ids_json' in row:
                refs = json.loads(row['source_ids_json'])
            refs = refs if isinstance(refs, list) else []
            sources = list(self._rows('sources'))
            rights = list(self._rows('rights'))
            resolved = []
            for ref in refs:
                source = next((s for s in sources if s.get('id') == ref), None)
                resolved.append({'id': ref, 'status': 'found' if source else 'unresolved_source_reference',
                                 'record': source,
                                 'rights': [r for r in rights if r.get('source_id') == ref]})
            return {**summary, 'record': row, 'sources': resolved, 'notice': NOTICE,
                    'campaign_effects': False, 'adoption_performed': False}


def from_registration(path):
    """Load only the owner's explicit local attachment; never discover files."""
    document = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(document, dict) or document.get('schema_version') != 1:
        raise ValueError('Unsupported local reference registration')
    source = document.get('historical_archive')
    if not isinstance(source, dict) or not isinstance(source.get('path'), str):
        raise ValueError('Invalid local historical reference attachment')
    return HistoricalArchive(source['path'], source['sha256'])
