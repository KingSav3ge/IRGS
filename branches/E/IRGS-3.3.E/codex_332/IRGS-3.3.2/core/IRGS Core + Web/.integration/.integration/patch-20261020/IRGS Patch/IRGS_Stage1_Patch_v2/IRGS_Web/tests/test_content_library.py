import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.request import Request, urlopen
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from server import make_server
from features import FEATURES, LIFECYCLES, content_library, feature_registry



class ContentLibraryTests(unittest.TestCase):
    def test_exactly_one_campaign_and_it_is_hyw(self):
        data = content_library()
        self.assertEqual([c['id'] for c in data['campaigns']], ['hundred-years-war'])

    def test_no_engine_or_technical_library_is_listed(self):
        from campaign_library import catalog
        cat = catalog()
        internal = set()
        for key in ('genre_engines', 'content_libraries', 'campaign_profiles'):
            for item in cat[key]:
                internal |= {str(item.get(k)).lower() for k in ('id', 'name', 'title') if item.get(k)}
        internal -= {'hundred-years-war'}
        data = content_library()
        listed = set()
        for c in data['campaigns']:
            listed |= {c['id'].lower(), c['title'].lower()}
            for p in c['periods']:
                listed |= {p['id'].lower(), p['name'].lower()}
                listed |= {e['id'].lower() for e in p['entries']} | {e['title'].lower() for e in p['entries']}
        self.assertTrue(internal)
        self.assertFalse(listed & internal, listed & internal)
        self.assertEqual(set(data['campaigns'][0]), {'id', 'title', 'period', 'status', 'summary', 'periods',
                                                      'entry_count', 'playable_entry_count', 'starts_via'})

    def test_entries_nested_and_only_developed_are_playable(self):
        c = content_library()['campaigns'][0]
        entries = [e for p in c['periods'] for e in p['entries']]
        self.assertEqual(len(entries), 37)
        self.assertEqual(c['entry_count'], 37)
        self.assertEqual([e['id'] for e in entries if e['playable']], ['hyw-1415'])
        self.assertEqual(c['playable_entry_count'], 1)

    def test_registry_order_and_honesty(self):
        ids = [f['id'] for f in feature_registry()['features']]
        self.assertLess(ids.index('content-library'), ids.index('workshop'))
        self.assertLess(ids.index('workshop'), ids.index('marketplace'))
        self.assertEqual(len(ids), len(set(ids)))
        for f in FEATURES:
            self.assertIn(f['lifecycle'], LIFECYCLES)
            if f['lifecycle'] != 'functional':
                self.assertFalse(f['showInRelease'] and f['showInPreview'], f['id'])
        by = {f['id']: f for f in FEATURES}
        self.assertEqual(by['solo-exchange']['lifecycle'], 'deferred')
        self.assertEqual(by['build-provenance']['lifecycle'], 'planned')
        self.assertEqual(by['workshop']['lifecycle'], 'planned')

    def test_release_stage_hides_planned_without_removing_them(self):
        release = {f['id'] for f in feature_registry('release')['features']}
        self.assertIn('content-library', release)
        self.assertNotIn('workshop', release)
        self.assertIn('workshop', {f['id'] for f in FEATURES})

    def test_parents_exist(self):
        ids = {f['id'] for f in FEATURES}
        for f in FEATURES:
            self.assertTrue(f['parentId'] is None or f['parentId'] in ids)
            for d in f['dependencyIds']:
                self.assertIn(d, ids)


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1])
        self.server = make_server(0, self.tmp.name)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f'http://127.0.0.1:{self.server.server_port}'

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.tmp.cleanup()

    def get(self, path):
        with urlopen(Request(self.url + path)) as r:
            return json.load(r)

    def test_routes_are_read_only_and_leave_no_saves(self):
        self.assertEqual(len(self.get('/api/content-library')['campaigns']), 1)
        self.assertTrue(self.get('/api/features')['features'])
        self.assertEqual(self.get('/api/campaigns')['campaigns'], [])


if __name__ == '__main__':
    unittest.main()
