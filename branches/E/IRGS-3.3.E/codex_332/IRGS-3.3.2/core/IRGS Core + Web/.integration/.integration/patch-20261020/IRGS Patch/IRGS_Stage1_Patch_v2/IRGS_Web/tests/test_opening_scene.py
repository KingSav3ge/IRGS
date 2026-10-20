"""Opening scene and first-action trace over the real HTTP host (mock-free: opening text is deterministic)."""
import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from server import make_server

TRACE = []


class OpeningTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1])
        self.server = make_server(0, self.tmp.name)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f'http://127.0.0.1:{self.server.server_port}'
        self.token = self.call('/api/campaigns')['token']

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.tmp.cleanup()

    def call(self, path, data=None):
        headers = {'Content-Type': 'application/json', 'X-IRGS-Token': getattr(self, 'token', '')}
        req = Request(self.url + path, data=None if data is None else json.dumps(data).encode(), headers=headers)
        with urlopen(req, timeout=15) as r:
            return json.load(r)

    def start(self, request_id='create-req-1', name='Mara'):
        entry = self.call('/api/historical-entry/hyw-1415')
        fields = {'profile_id': 'military', 'scenario_id': 'hundred-years-war', 'entry_id': 'hyw-1415',
                  'snapshot_sha256': entry['snapshot_sha256']}
        options = self.call('/api/starting-options?' + urlencode(fields))
        payload = {'name': 'Opening test', **fields, 'character': {'kind': 'new', 'name': name, 'species': 'human',
                   'background': 'A wool factor from Southampton.'}, 'starting_scenario_id': 'individual',
                   'selection_digest': options['selection_digest'], 'request_id': request_id}
        return payload, self.call('/api/create', payload)

    def view(self, cid):
        return self.call('/api/playthrough/' + cid)

    def test_opening_to_first_action_trace_is_exact_once(self):
        payload, created = self.start()
        cid = created['id']
        first = self.view(cid)
        opening = first['opening']
        TRACE.append({'step': 'create', 'request_id': payload['request_id'], 'campaign': cid,
                      'revision': created['revision'], 'replayed': created.get('creation_replayed', False)})
        self.assertEqual(opening['status'], 'awaiting_first_action')
        self.assertFalse(opening['effects_applied'])
        self.assertEqual([b['kind'] for b in opening['blocks']],
                         ['setting', 'character', 'world_hook', 'first_decision'])
        self.assertIn('Mara', opening['blocks'][1]['text'])
        self.assertTrue(first['capabilities']['can_declare'])
        self.assertFalse(first['capabilities']['narrator'])
        self.assertEqual([e['id'] for e in first['chronicle'] if e['kind'] == 'opening_scene'], [opening['id']])

        # interrupted/retried creation: same request ID returns the existing save, no second world or opening
        _, replay = self.start()
        TRACE.append({'step': 'create_retry', 'request_id': payload['request_id'], 'campaign': replay['id'],
                      'replayed': replay.get('creation_replayed')})
        self.assertTrue(replay['creation_replayed'])
        self.assertEqual(replay['id'], cid)
        self.assertEqual(len(self.call('/api/campaigns')['campaigns']), 1)

        # reload and tab changes are reads: identical opening, no new records
        again = self.view(cid)
        self.call('/api/chronicle/' + cid)
        self.assertEqual(again['opening'], opening)
        self.assertEqual(again['revision'], first['revision'])
        self.assertEqual(len(again['chronicle']), len(first['chronicle']))

        # first free-form action
        declaration = {'id': cid, 'revision': again['revision'], 'request_id': 'first-action-1',
                       'actor': first['actor_id'], 'declaration': 'I ask a clerk at the muster whether wool is wanted.'}
        ack = self.call('/api/declaration', declaration)
        TRACE.append({'step': 'first_action', 'request_id': 'first-action-1', 'result': ack.get('status')})
        retry = self.call('/api/declaration', declaration)
        self.assertEqual(retry, ack)
        after = self.view(cid)
        declared = [e for e in after['chronicle'] if e['kind'] == 'player_declaration']
        self.assertEqual(len(declared), 1)
        self.assertEqual(declared[0]['text'], declaration['declaration'])
        self.assertEqual(declared[0]['status'], 'declared_not_resolved')
        self.assertEqual(after['opening']['status'], 'first_action_declared')
        self.assertEqual(after['opening']['blocks'], opening['blocks'])
        self.assertEqual(len([e for e in after['chronicle'] if e['kind'] == 'opening_scene']), 1)
        TRACE.append({'step': 'reload', 'opening_status': after['opening']['status'], 'declarations': len(declared),
                      'opening_entries': 1})

    def test_player_payload_exposes_no_state_and_stays_scoped(self):
        _, created = self.start()
        data = self.view(created['id'])
        self.assertNotIn('state', data)
        text = json.dumps(data)
        for secret in ('historical_start', 'snapshot_sha256', 'selection_digest', 'entity_registry'):
            self.assertNotIn(secret, text)

    def test_other_campaigns_get_no_opening_and_are_unchanged(self):
        record = self.call('/api/create', {'name': 'AST', 'profile_id': 'ast', 'mode': 'creator'})
        self.assertNotIn('opening_scene', record['state'])
        data = self.view(record['id'])
        self.assertIsNone(data['opening'])
        self.assertFalse(data['capabilities']['opening_scene'])
        self.assertFalse([e for e in data['chronicle'] if e['kind'] == 'opening_scene'])

    def test_opening_is_grounded_in_sourced_facts_only(self):
        _, created = self.start()
        opening = self.view(created['id'])['opening']
        entry = self.call('/api/historical-entry/hyw-1415')['snapshot']
        facts = {f['id']: f for fs in entry['domains'].values() for f in fs}
        hook = next(b for b in opening['blocks'] if b['kind'] == 'world_hook')
        self.assertIn(facts[hook['fact_id']]['statement'], hook['text'])
        self.assertTrue(hook['source_ids'])
        self.assertLessEqual(facts[hook['fact_id']]['effective_not_after'], '1415-08-11')


if __name__ == '__main__':
    unittest.main()
