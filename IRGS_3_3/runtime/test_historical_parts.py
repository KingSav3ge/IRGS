"""Multipart identity, atomic recovery and unchanged source-record semantics."""
import concurrent.futures
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from historical_archive import HistoricalArchive, file_hash, from_catalog_manifest, from_registration
from historical_parts import HistoricalPartsError
from test_historical_archive import fixture_archive


class HistoricalPartsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.catalog = self.root / 'historical_details'
        (self.catalog / 'parts').mkdir(parents=True)
        self.manifest = self.catalog / 'manifest.json'
        self.cache = self.root / 'cache'
        self.install_archive(fixture_archive(self.root, complete=True))

    def install_archive(self, original):
        self.original = original
        self.data = self.original.read_bytes()
        for old in (self.catalog / 'parts').glob('archive.*'):
            old.unlink()
        size = 512  # Small synthetic parts exercise the same bounded reader.
        parts = []
        for start in range(0, len(self.data), size):
            block = self.data[start:start + size]
            name = f'parts/archive.{len(parts) + 1:04d}'
            (self.catalog / name).write_bytes(block)
            parts.append({'ordinal': len(parts) + 1, 'path': name, 'bytes': len(block),
                          'sha256': hashlib.sha256(block).hexdigest()})
        self.document = {'schema_version': 1, 'status': 'complete', 'display_name': 'Historical Details',
                         'archive': {'name': self.original.name, 'bytes': len(self.data),
                                     'sha256': file_hash(self.original)},
                         'part_size_bytes': size, 'parts': parts}
        self.write_manifest()

    def write_manifest(self):
        self.manifest.write_text(json.dumps(self.document), encoding='utf-8')
        self.pin = file_hash(self.manifest)

    def library(self):
        return from_catalog_manifest(self.manifest, self.pin, cache_dir=self.cache)

    def assert_atomic_failure(self, code):
        with self.assertRaises(HistoricalPartsError) as caught:
            self.library().status()
        self.assertEqual(caught.exception.code, code)
        self.assertLess(len(str(caught.exception)), 200)
        self.assertNotIn(str(self.root), str(caught.exception))
        self.assertFalse(self.cache.exists() and list(self.cache.iterdir()))

    def test_exact_reconstruction_retains_records_dates_citations_and_rights(self):
        before = {p.relative_to(self.catalog): file_hash(p) for p in self.catalog.rglob('*') if p.is_file()}
        library = self.library()
        status = library.verify_collections()
        self.assertEqual(library.path.read_bytes(), self.data)
        self.assertEqual(file_hash(library.path), file_hash(self.original))
        self.assertEqual(status['title'], 'Historical Details')
        self.assertEqual(status['manifest_sha256'], self.pin)
        self.assertNotIn(str(self.root), json.dumps(status))
        legacy = HistoricalArchive(self.original, file_hash(self.original))
        for collection in ('chronology', 'research', 'concepts'):
            self.assertEqual(library.search(collection), legacy.search(collection))
            self.assertEqual(library.record(collection, 1), legacy.record(collection, 1))
        self.assertEqual(library.record('chronology', 1)['dates']['start_astronomical'], 0)
        self.assertEqual(library.record('concepts', 1)['record']['name'], 'Game-source concept')
        after = {p.relative_to(self.catalog): file_hash(p) for p in self.catalog.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_retry_and_new_reader_reuse_complete_verified_cache(self):
        first = self.library()
        first.status()
        before = first.path.stat()
        with patch('historical_parts.os.rename', side_effect=AssertionError('cache was rewritten')):
            first.record('chronology', 1)
            self.library().record('chronology', 1)
        self.assertEqual(first.path.stat().st_mtime_ns, before.st_mtime_ns)

    def test_missing_part_fails_before_publishing_then_recovers(self):
        part = self.catalog / self.document['parts'][1]['path']
        data = part.read_bytes()
        part.unlink()
        self.assert_atomic_failure('incomplete')
        part.write_bytes(data)
        self.assertEqual(self.library().status()['sha256'], self.document['archive']['sha256'])

    def test_corrupt_part_publishes_no_partial_archive(self):
        part = self.catalog / self.document['parts'][-1]['path']
        data = bytearray(part.read_bytes())
        data[-1] ^= 1
        part.write_bytes(data)
        self.assert_atomic_failure('corrupt')

    def test_truncated_part_is_rejected(self):
        part = self.catalog / self.document['parts'][0]['path']
        part.write_bytes(part.read_bytes()[:-1])
        self.assert_atomic_failure('corrupt')

    def test_changed_or_missing_parts_cannot_be_hidden_by_cached_archive(self):
        for change in ('alter', 'remove'):
            with self.subTest(change=change):
                library = self.library()
                library.status()
                part = self.catalog / self.document['parts'][0]['path']
                data = part.read_bytes()
                if change == 'remove':
                    part.unlink()
                else:
                    part.write_bytes(b'!' + data[1:])
                with self.assertRaises(HistoricalPartsError):
                    library.record('chronology', 1)
                self.assertEqual(library.path.read_bytes(), self.data)
                part.write_bytes(data)

    def test_manifest_pin_is_checked_after_cache_is_ready(self):
        library = self.library()
        library.status()
        self.manifest.write_text(self.manifest.read_text() + ' ')
        with self.assertRaisesRegex(HistoricalPartsError, 'manifest changed'):
            library.search('chronology')

    def test_reordered_and_duplicate_parts_are_not_sorted_or_deduplicated(self):
        original = copy.deepcopy(self.document['parts'])
        for mode in ('reorder', 'duplicate_path', 'duplicate_ordinal'):
            with self.subTest(mode=mode):
                self.document['parts'] = copy.deepcopy(original)
                if mode == 'reorder':
                    self.document['parts'][:2] = reversed(self.document['parts'][:2])
                elif mode == 'duplicate_path':
                    self.document['parts'][1]['path'] = self.document['parts'][0]['path']
                else:
                    self.document['parts'][1]['ordinal'] = 1
                self.write_manifest()
                self.assert_atomic_failure('invalid_manifest')

    def test_reordered_bytes_fail_individual_hashes(self):
        first, second = [self.catalog / p['path'] for p in self.document['parts'][:2]]
        a, b = first.read_bytes(), second.read_bytes()
        first.write_bytes(b)
        second.write_bytes(a)
        self.assert_atomic_failure('corrupt')

    def test_original_archive_hash_is_checked_even_when_all_parts_match(self):
        self.document['archive']['sha256'] = '0' * 64
        self.write_manifest()
        self.assert_atomic_failure('corrupt')

    def test_original_size_and_part_count_must_agree(self):
        self.document['parts'].pop()
        self.write_manifest()
        self.assert_atomic_failure('incomplete')

    def test_incomplete_placeholder_is_not_a_ready_archive(self):
        self.document['status'] = 'awaiting_source'
        self.write_manifest()
        self.assert_atomic_failure('incomplete')

    def test_nonportable_and_escaping_paths_are_rejected(self):
        for name in ('../outside', '/absolute', 'parts/../outside', 'parts\\outside', 'C:/outside',
                     'parts//one', 'parts/CON', 'parts/NUL.bin', 'parts/part.', 'parts/part ', 'parts/a?b'):
            with self.subTest(path=name):
                self.document['parts'][0]['path'] = name
                self.write_manifest()
                self.assert_atomic_failure('invalid_manifest')

    def test_internal_links_and_linked_part_directory_are_rejected(self):
        first = self.catalog / self.document['parts'][0]['path']
        copy_path = self.catalog / 'part-copy'
        copy_path.write_bytes(first.read_bytes())
        first.unlink()
        first.symlink_to(copy_path)
        self.assert_atomic_failure('invalid_manifest')
        first.unlink()
        first.write_bytes(copy_path.read_bytes())
        source = self.catalog / 'parts'
        source.rename(self.catalog / 'source-parts')
        source.symlink_to(self.catalog / 'source-parts', target_is_directory=True)
        self.assert_atomic_failure('invalid_manifest')

    def test_unrecorded_parts_are_refused_even_after_cache_is_ready(self):
        library = self.library()
        library.status()
        (self.catalog / 'parts' / 'extra.part').write_bytes(b'unrecorded')
        with self.assertRaisesRegex(HistoricalPartsError, 'unrecorded'):
            library.search('chronology')

    def test_linked_manifest_is_refused(self):
        original = self.catalog / 'original-manifest.json'
        self.manifest.rename(original)
        self.manifest.symlink_to(original)
        self.assert_atomic_failure('invalid_manifest')

    def add_coverage(self):
        counts = {'chronology': 1, 'figures': 1, 'research': 1, 'sources': 1, 'rights': 1, 'concepts': 2,
                  'claims': 0, 'places': 0, 'routes': 0, 'population': 0}
        from historical_archive import COLLECTIONS
        with zipfile.ZipFile(self.original) as archive:
            rows = []
            for key, (_, name) in COLLECTIONS.items():
                member = 'Synthetic/' + name
                data = archive.read(member)
                rows.append({'id': key, 'member': member, 'bytes': len(data),
                             'sha256': hashlib.sha256(data).hexdigest(), 'record_count': counts[key]})
        self.document['coverage'] = {'collections': rows}
        self.write_manifest()
        return counts

    def test_deep_verification_checks_actual_row_counts_and_original_member_bindings(self):
        expected = self.add_coverage()
        result = self.library().verify_delivery()
        self.assertEqual(result['record_counts'], expected)
        self.assertTrue(result['catalog_coverage_verified'])
        self.assertFalse(result['historical_truth_verified'])
        self.assertFalse(result['campaign_effects'])
        for field, value in (('record_count', 999), ('sha256', '0' * 64), ('member', 'other/source.json')):
            with self.subTest(field=field):
                self.add_coverage()
                self.document['coverage']['collections'][0][field] = value
                self.write_manifest()
                with self.assertRaisesRegex(HistoricalPartsError, 'coverage differs'):
                    self.library().verify_delivery()

    def test_deep_verification_refuses_duplicate_or_missing_collection_metadata(self):
        self.add_coverage()
        self.document['coverage']['collections'][1] = self.document['coverage']['collections'][0]
        self.write_manifest()
        with self.assertRaisesRegex(HistoricalPartsError, 'incomplete or duplicated'):
            self.library().verify_delivery()

    def test_symlink_to_source_outside_manifest_directory_is_rejected(self):
        part = self.catalog / self.document['parts'][0]['path']
        external = self.root / 'outside'
        external.write_bytes(part.read_bytes())
        part.unlink()
        part.symlink_to(external)
        self.assert_atomic_failure('invalid_manifest')

    def test_oversized_manifest_is_bounded(self):
        self.manifest.write_bytes(b' ' * (1024 * 1024 + 1))
        self.pin = file_hash(self.manifest)
        self.assert_atomic_failure('invalid_manifest')

    def test_manifest_types_sizes_and_duplicate_fields_are_rejected(self):
        original = copy.deepcopy(self.document)
        for field, value in (('schema_version', True), ('part_size_bytes', 0),
                             ('part_size_bytes', 16 * 1024 * 1024 + 1)):
            with self.subTest(field=field, value=value):
                self.document = copy.deepcopy(original)
                self.document[field] = value
                self.write_manifest()
                self.assert_atomic_failure('invalid_manifest')
        self.manifest.write_text('{"schema_version": 1, "schema_version": 1}')
        self.pin = file_hash(self.manifest)
        self.assert_atomic_failure('invalid_manifest')

    def test_reference_validation_failure_publishes_no_cache(self):
        with patch('historical_archive.HistoricalArchive.verify_collections', side_effect=ValueError('invalid member')):
            self.assert_atomic_failure('corrupt')

    def test_incomplete_collection_set_and_invalid_zip_do_not_publish(self):
        self.install_archive(fixture_archive(self.root, complete=False))
        self.assert_atomic_failure('corrupt')
        self.original.write_bytes(b'not a ZIP archive')
        self.install_archive(self.original)
        self.assert_atomic_failure('corrupt')

    def test_source_changed_during_reference_validation_does_not_publish(self):
        library = self.library()
        validate = library._verify_zip

        def change_source(path):
            validate(path)
            part = self.catalog / self.document['parts'][0]['path']
            part.write_bytes(b'!' + part.read_bytes()[1:])

        with patch.object(library, '_verify_zip', side_effect=change_source):
            with self.assertRaisesRegex(HistoricalPartsError, 'parts changed'):
                library.status()
        self.assertEqual(list(self.cache.iterdir()), [])

    def test_missing_manifest_is_unavailable(self):
        self.manifest.unlink()
        self.assert_atomic_failure('unavailable')

    def test_source_directory_cannot_be_used_as_installation_cache(self):
        with self.assertRaisesRegex(HistoricalPartsError, 'outside Historical Details'):
            from_catalog_manifest(self.manifest, self.pin, cache_dir=self.catalog / 'cache')

    def test_corrupt_cache_fails_instead_of_exposing_changed_records(self):
        library = self.library()
        library.status()
        library.path.write_bytes(b'!' + self.data[1:])
        with self.assertRaisesRegex(HistoricalPartsError, 'cache failed'):
            library.record('chronology', 1)

    def test_failed_publication_cleans_temporary_file_and_retry_succeeds(self):
        library = self.library()
        with patch('historical_parts.os.rename', side_effect=OSError('synthetic interrupted write')):
            with self.assertRaises(HistoricalPartsError) as caught:
                library.status()
        self.assertEqual(caught.exception.code, 'unavailable')
        self.assertEqual(list(self.cache.iterdir()), [])
        library.status()
        self.assertEqual(library.path.read_bytes(), self.data)

    def test_concurrent_instances_publish_only_complete_identical_bytes(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
            results = list(pool.map(lambda _: self.library().record('chronology', 1), range(3)))
        self.assertTrue(all(r == results[0] for r in results))
        files = list(self.cache.iterdir())
        self.assertEqual(len(files), 1)
        self.assertEqual((files[0] / 'archive.zip').read_bytes(), self.data)

    def test_explicit_registration_resolves_relative_paths_without_discovery(self):
        config = self.root / 'reference_sources.json'
        config.write_text(json.dumps({'schema_version': 1, 'historical_archive': {
            'type': 'catalog_parts', 'manifest_path': 'historical_details/manifest.json',
            'manifest_sha256': self.pin, 'cache_dir': 'cache'}}))
        result = from_registration(config).record('research', 1)
        self.assertFalse(result['campaign_effects'])
        self.assertFalse(result['adoption_performed'])
        self.assertEqual(result['sources'][1]['status'], 'unresolved_source_reference')


if __name__ == '__main__':
    unittest.main()
