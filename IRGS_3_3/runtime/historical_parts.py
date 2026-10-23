"""Verify explicitly selected Catalog byte parts into an installation cache.

No archive members are extracted and no supplied source instructions are run.
"""
from __future__ import annotations

import errno
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile
import threading

MAX_MANIFEST = 1024 * 1024
MAX_PART = 16 * 1024 * 1024
MAX_PARTS = 4096
CHUNK = 1024 * 1024


class HistoricalPartsError(ValueError):
    """A bounded display message and stable availability code for callers."""

    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


def _sha(value):
    return isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value) is not None


def _relative(value):
    return (isinstance(value, str) and 0 < len(value) <= 512
            and not PurePosixPath(value).is_absolute()
            and all(p not in ('', '.', '..') for p in value.split('/'))
            and not any(c in value for c in '\\:')
            and not any(ord(c) < 32 for c in value)
            and all(not p.endswith(('.', ' ')) and not any(c in p for c in '<>"|?*')
                    and not re.fullmatch(r'(?i:con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?', p)
                    for p in value.split('/')))


def _stamp(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise HistoricalPartsError('invalid_manifest', 'Historical Details manifest has duplicate fields')
        result[key] = value
    return result


class PinnedParts:
    def __init__(self, manifest_path, manifest_sha256, cache_dir):
        if not _sha(manifest_sha256):
            raise HistoricalPartsError('invalid_manifest', 'A pinned Historical Details manifest SHA-256 is required')
        self.manifest_path = Path(manifest_path)
        if self.manifest_path.is_symlink():
            raise HistoricalPartsError('invalid_manifest', 'Historical Details manifest must not be a link')
        self.manifest_sha256 = manifest_sha256
        self.root = self.manifest_path.parent.resolve()
        self.cache_dir = Path(cache_dir).resolve()
        if self.cache_dir.is_relative_to(self.root):
            raise HistoricalPartsError('invalid_manifest', 'Use an installation cache outside Historical Details source data')
        document = self._document()
        self._validate(document)
        self.archive_sha256 = document['archive']['sha256']
        self.archive_bytes = document['archive']['bytes']
        self.parts = document['parts']
        self.path = self.cache_dir / self.archive_sha256 / 'archive.zip'
        self._inputs = None
        self._cache_stamp = None
        self._lock = threading.RLock()

    def _document(self):
        try:
            if self.manifest_path.is_symlink() or not stat.S_ISREG(self.manifest_path.stat().st_mode):
                raise HistoricalPartsError('invalid_manifest', 'Historical Details manifest must be a regular source file')
            with self.manifest_path.open('rb') as stream:
                data = stream.read(MAX_MANIFEST + 1)
        except OSError as exc:
            raise HistoricalPartsError('unavailable', 'Historical Details manifest is unavailable') from exc
        if len(data) > MAX_MANIFEST:
            raise HistoricalPartsError('invalid_manifest', 'Historical Details manifest exceeds the reader limit')
        if hashlib.sha256(data).hexdigest() != self.manifest_sha256:
            raise HistoricalPartsError('corrupt', 'Historical Details manifest changed; select the intended source pin')
        try:
            return json.loads(data, object_pairs_hook=_unique_object)
        except (ValueError, UnicodeError) as exc:
            if isinstance(exc, HistoricalPartsError):
                raise
            raise HistoricalPartsError('invalid_manifest', 'Historical Details manifest is not valid JSON') from exc

    @staticmethod
    def _validate(document):
        if not isinstance(document, dict) or type(document.get('schema_version')) is not int or document['schema_version'] != 1:
            raise HistoricalPartsError('invalid_manifest', 'Unsupported Historical Details manifest version')
        if document.get('status') != 'complete':
            raise HistoricalPartsError('incomplete', 'Historical Details archive is incomplete; a complete part set is required')
        archive = document.get('archive')
        size = document.get('part_size_bytes')
        parts = document.get('parts')
        if (not isinstance(archive, dict) or not _relative(archive.get('name'))
                or '/' in archive['name'] or not archive['name'].lower().endswith('.zip')
                or not _sha(archive.get('sha256')) or type(archive.get('bytes')) is not int
                or archive['bytes'] <= 0 or type(size) is not int or not 1 <= size <= MAX_PART
                or not isinstance(parts, list) or not 1 <= len(parts) <= MAX_PARTS):
            raise HistoricalPartsError('invalid_manifest', 'Invalid Historical Details archive or part inventory')
        expected_count = (archive['bytes'] + size - 1) // size
        if len(parts) != expected_count:
            raise HistoricalPartsError('incomplete', 'Historical Details part count does not match the original archive size')
        seen = set()
        for ordinal, part in enumerate(parts, 1):
            expected_size = min(size, archive['bytes'] - (ordinal - 1) * size)
            if (not isinstance(part, dict) or type(part.get('ordinal')) is not int
                    or part['ordinal'] != ordinal or not _relative(part.get('path'))
                    or part['path'].casefold() in seen or not _sha(part.get('sha256'))
                    or type(part.get('bytes')) is not int or part['bytes'] != expected_size):
                raise HistoricalPartsError('invalid_manifest', 'Historical Details parts must be unique, ordered and correctly sized')
            seen.add(part['path'].casefold())

    def _snapshot(self):
        result = []
        for part in self.parts:
            ordinal = part['ordinal']
            try:
                path = self.root
                for component in part['path'].split('/'):
                    path = path / component
                    if path.is_symlink():
                        raise HistoricalPartsError('invalid_manifest', 'Historical Details parts must not contain links')
                path = path.resolve(strict=True)
                if not path.is_relative_to(self.root):
                    raise HistoricalPartsError('invalid_manifest', 'Historical Details part escapes its source directory')
                info = path.stat()
            except RuntimeError as exc:
                raise HistoricalPartsError('invalid_manifest', 'Historical Details part has an invalid link target') from exc
            except OSError as exc:
                raise HistoricalPartsError('incomplete', f'Historical Details part {ordinal} is missing or unreadable') from exc
            if not stat.S_ISREG(info.st_mode) or info.st_size != part['bytes']:
                raise HistoricalPartsError('corrupt', f'Historical Details part {ordinal} has an incorrect size or type')
            result.append((path, _stamp(info)))
        # Catalog's flat parts/ directory is an exact source inventory. Ignore
        # sibling documentation/indexes, but never silently ignore extra parts.
        if all(PurePosixPath(part['path']).parent == PurePosixPath('parts') for part in self.parts):
            expected = {part['path'] for part in self.parts}
            with os.scandir(self.root / 'parts') as entries:
                for entry in entries:
                    if entry.is_symlink() or 'parts/' + entry.name not in expected:
                        raise HistoricalPartsError('invalid_manifest', 'Historical Details contains unrecorded parts or links')
        return tuple(result)

    def _stream(self, snapshot, output):
        archive_hash = hashlib.sha256()
        total = 0
        for part, (path, stamp) in zip(self.parts, snapshot):
            digest, count = hashlib.sha256(), 0
            with path.open('rb') as stream:
                if _stamp(os.fstat(stream.fileno())) != stamp:
                    raise HistoricalPartsError('corrupt', 'Historical Details parts changed during verification')
                while block := stream.read(CHUNK):
                    count += len(block)
                    if count > part['bytes']:
                        raise HistoricalPartsError('corrupt', f'Historical Details part {part["ordinal"]} grew during verification')
                    digest.update(block)
                    archive_hash.update(block)
                    if output is not None:
                        output.write(block)
                if _stamp(os.fstat(stream.fileno())) != stamp:
                    raise HistoricalPartsError('corrupt', 'Historical Details parts changed during verification')
            if count != part['bytes'] or digest.hexdigest() != part['sha256']:
                raise HistoricalPartsError('corrupt', f'Historical Details part {part["ordinal"]} failed SHA-256 verification')
            total += count
        if total != self.archive_bytes or archive_hash.hexdigest() != self.archive_sha256:
            raise HistoricalPartsError('corrupt', 'Historical Details reconstruction differs from the original archive pin')
        self._unchanged(snapshot)

    def _unchanged(self, snapshot):
        self._document()
        if self._snapshot() != snapshot:
            raise HistoricalPartsError('corrupt', 'Historical Details parts changed during verification')

    def _cached(self):
        if self.path.is_symlink() or self.path.parent.is_symlink():
            raise HistoricalPartsError('corrupt', 'Historical Details cache must be a regular file')
        if not self.path.exists():
            return None
        info = self.path.stat()
        if not stat.S_ISREG(info.st_mode) or info.st_size != self.archive_bytes:
            raise HistoricalPartsError('corrupt', 'Historical Details cache has an incorrect size or type')
        return _stamp(info)

    def _verify_cache(self, stamp):
        digest = hashlib.sha256()
        with self.path.open('rb') as stream:
            while block := stream.read(CHUNK):
                digest.update(block)
        if digest.hexdigest() != self.archive_sha256 or self._cached() != stamp:
            raise HistoricalPartsError('corrupt', 'Historical Details cache failed original archive verification')

    def prepare(self, validate=None):
        """Return only a verified complete ZIP; failed assembly publishes no file."""
        with self._lock:
            temporary = None
            try:
                self._document()
                snapshot = self._snapshot()
                cached = self._cached()
                if self._inputs == snapshot and cached is not None and cached == self._cache_stamp:
                    return self.path
                if cached is not None:
                    self._stream(snapshot, None)
                    self._verify_cache(cached)
                    if validate is not None:
                        validate(self.path)
                else:
                    self.cache_dir.mkdir(parents=True, exist_ok=True)
                    temporary = Path(tempfile.mkdtemp(dir=self.cache_dir, prefix='.assembling-'))
                    staged = temporary / 'archive.zip'
                    with staged.open('wb') as stream:
                        self._stream(snapshot, stream)
                        stream.flush()
                        os.fsync(stream.fileno())
                    if validate is not None:
                        validate(staged)
                    self._unchanged(snapshot)
                    try:
                        # Rename a complete directory. Concurrent publication
                        # cannot replace a populated cache or alter its file.
                        os.rename(temporary, self.path.parent)
                    except OSError as exc:
                        if exc.errno not in (errno.EEXIST, errno.ENOTEMPTY):
                            raise
                        self._verify_cache(self._cached())
                self._unchanged(snapshot)
                self._inputs = snapshot
                self._cache_stamp = self._cached()
                return self.path
            except OSError as exc:
                raise HistoricalPartsError('unavailable', 'Historical Details verification or cache write could not finish; retry is safe') from exc
            finally:
                if temporary is not None:
                    shutil.rmtree(temporary, ignore_errors=True)
