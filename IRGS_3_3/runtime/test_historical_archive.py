"""Synthetic external-source attachment: no real archive or campaign required."""
import gzip
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from historical_archive import COLLECTIONS, HistoricalArchive, file_hash, from_registration


def fixture_archive(folder, *, corrupt_member=False, complete=False):
    path = Path(folder) / 'synthetic-reference.zip'
    payloads = {
        'chronology': [{'id': 'A:one', 'title': 'A disputed beginning', 'start_astronomical': 0,
                        'date_text': '1 BCE', 'epistemic_class': 'disputed',
                        'adoption_status': 'unadopted', 'source_ids_json': '["SRC"]'}],
        'figures': [{'id': 'figure', 'source_name': '<script>Henry</script>', 'period_text': '1415',
                     'profile': {'campaign_state': None, 'adoption_status': 'Proposed'}}],
        'research': [{'id': 'namespace:operation', 'record_type': 'operations', 'source_ids': ['SRC', 'MISSING'],
                      'payload': {'id': 'operation', 'title': 'Wheat permit', 'quantity': 1000,
                                  'unit': 'quarters', 'delivery_status': 'not_established', 'campaign_state': None}}],
        'sources': [{'id': 'SRC', 'title': 'Synthetic citation', 'url': 'https://example.invalid/source',
                     'rights_status': 'reference_only'}],
        'rights': [{'id': 'right', 'source_id': 'SRC', 'disposition': 'reference_only'}],
        'concepts': [{'id': 'duplicate-local-id', 'name': 'Game-source concept', 'status': 'source_assertion'},
                     {'id': 'duplicate-local-id', 'name': 'Second source assertion'}],
    }
    files = {}
    if complete:
        for collection in COLLECTIONS:
            payloads.setdefault(collection, [])
    for collection, rows in payloads.items():
        name = COLLECTIONS[collection][1]
        data = (gzip.compress(('\n'.join(json.dumps(r) for r in rows) + '\n').encode())
                if name.endswith('.gz') else json.dumps(rows).encode())
        files[name] = data
    manifest = {'edition': 'Grand 1.1', 'files': [{'path': n, 'bytes': len(b),
                 'sha256': hashlib.sha256(b).hexdigest()} for n, b in files.items()]}
    if corrupt_member:
        files[COLLECTIONS['chronology'][1]] = b'[]'
    with zipfile.ZipFile(path, 'w') as archive:
        for name, data in files.items(): archive.writestr('Synthetic/' + name, data)
        archive.writestr('Synthetic/07_Verification/delivery_manifest.json', json.dumps(manifest))
        archive.writestr('Synthetic/07_Verification/Previous/07_Verification/delivery_manifest.json',
                         json.dumps({'edition': 'Grand 1.0', 'files': []}))
    return path


class HistoricalArchiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent)
        self.path = fixture_archive(self.tmp.name)
        self.library = HistoricalArchive(self.path, file_hash(self.path))

    def tearDown(self): self.tmp.cleanup()

    def test_research_keeps_qualification_units_and_unresolved_sources(self):
        result = self.library.record('research', 1)
        self.assertEqual(result['record']['payload']['delivery_status'], 'not_established')
        self.assertIsNone(result['record']['payload']['campaign_state'])
        self.assertEqual(result['record']['payload']['unit'], 'quarters')
        self.assertEqual(result['sources'][1]['status'], 'unresolved_source_reference')
        self.assertEqual(result['sources'][0]['rights'][0]['disposition'], 'reference_only')
        self.assertFalse(result['adoption_performed']); self.assertFalse(result['campaign_effects'])

    def test_dates_and_source_ids_are_preserved_and_pages_do_not_merge_duplicates(self):
        row = self.library.search('chronology', 'disputed')['results'][0]
        self.assertEqual(row['dates']['start_astronomical'], 0)
        self.assertEqual(row['dates']['date_text'], '1 BCE')
        first = self.library.search('concepts', limit=1)
        second = self.library.search('concepts', offset=first['next_offset'], limit=1)
        self.assertTrue(first['has_more']); self.assertFalse(second['has_more'])
        self.assertEqual(first['results'][0]['source_id'], second['results'][0]['source_id'])
        self.assertNotEqual(first['results'][0]['reference'], second['results'][0]['reference'])

    def test_no_files_are_created_or_changed_by_reads(self):
        before = {p.name: file_hash(p) for p in Path(self.tmp.name).iterdir()}
        self.library.verify_collections(); self.library.search('figures', 'Henry')
        self.library.record('chronology', 1)
        after = {p.name: file_hash(p) for p in Path(self.tmp.name).iterdir()}
        self.assertEqual(before, after)
        self.assertNotIn(str(self.path), json.dumps(self.library.status()))

    def test_changed_attachment_refuses_cached_and_new_reads(self):
        self.library.status()
        with self.path.open('ab') as stream: stream.write(b'changed')
        with self.assertRaisesRegex(ValueError, 'changed'): self.library.search('chronology')

    def test_member_hash_and_invalid_parameters_are_rejected(self):
        bad = fixture_archive(self.tmp.name, corrupt_member=True)
        library = HistoricalArchive(bad, file_hash(bad))
        with self.assertRaises(ValueError): library.search('chronology')
        for params in ({'collection': '../README.md'}, {'offset': -1}, {'limit': 51}, {'query': 'x' * 201}):
            with self.assertRaises(ValueError): self.library.search(**params)

    def test_explicit_registration_preserves_pinned_identity(self):
        config = Path(self.tmp.name) / 'reference.json'
        config.write_text(json.dumps({'schema_version': 1, 'historical_archive':
                         {'path': str(self.path), 'sha256': self.library.sha256}}))
        restored = from_registration(config)
        self.assertEqual(restored.status()['sha256'], self.library.sha256)
        self.assertEqual(restored.record('figures', 1)['record']['profile']['adoption_status'], 'Proposed')


if __name__ == '__main__': unittest.main()
