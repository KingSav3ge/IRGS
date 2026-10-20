import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from server import make_server, Store


class HostTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.server = make_server(0, self.tmp.name)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.url = f'http://127.0.0.1:{self.server.server_port}'
        self.token = self.call('/api/campaigns')['token']

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.tmp.cleanup()

    def call(self, path, data=None, token=None):
        headers = {'Content-Type': 'application/json', 'X-IRGS-Token': token or getattr(self, 'token', '')}
        req = Request(self.url+path, data=json.dumps(data).encode() if data is not None else None, headers=headers)
        with urlopen(req) as response:
            return json.load(response)

    def create(self):
        return self.call('/api/create', {'name': 'Test campaign'})

    def event(self, r, **overrides):
        return self.call('/api/event', {**{'id': r['id'], 'revision': r['revision'], 'op': 'ast_record_player_action',
            'params': {'actor':'AST-01','instruction_ref':'test player','source_ref':'test source','declaration':'Inspect the gate'}}, **overrides})

    def test_event_persists_and_does_not_resolve_outcome(self):
        r = self.create()
        changed = self.event(r)
        saved = Store(self.tmp.name).read(r['id'])
        self.assertEqual(changed, saved)
        self.assertEqual(saved['state']['player_actions'][0]['status'], 'declared_not_resolved')
        self.assertEqual(saved['state']['stocks'], {})
        self.assertEqual(saved['revision'], 1)
        self.assertEqual(self.call('/api/campaign/'+r['id']), saved)

    def test_rejected_and_stale_events_preserve_save(self):
        r = self.create()
        with self.assertRaises(HTTPError):
            self.event(r, params={'actor':'AST-01','declaration':'bad'})
        self.assertEqual(Store(self.tmp.name).read(r['id']), r)
        changed = self.event(r)
        with self.assertRaises(HTTPError): self.event(r)
        self.assertEqual(Store(self.tmp.name).read(r['id']), changed)

    def test_branch_is_independent(self):
        original = self.create()
        branch = self.call('/api/fork', {'id': original['id']})
        self.event(branch)
        self.assertEqual(Store(self.tmp.name).read(original['id']), original)
        self.assertNotEqual(original['id'], branch['id'])

    def test_token_origin_host_and_paths(self):
        with self.assertRaises(HTTPError) as err:
            self.call('/api/create', {'name':'bad'}, token='invalid')
        self.assertEqual(err.exception.code, 403)
        for headers in ({'Origin':'https://example.com','X-IRGS-Token':self.token}, {'Host':'attacker.example','X-IRGS-Token':self.token}):
            with self.assertRaises(HTTPError) as err:
                urlopen(Request(self.url+'/api/create',data=b'{"name":"bad"}',headers=headers))
            self.assertEqual(err.exception.code, 403)
        with self.assertRaises(ValueError): Store(self.tmp.name).read('../outside')

    def test_inventory_runs_actual_engine_and_conserves(self):
        r=self.create()
        r=self.event(r,op='ast_establish_stock',params={'source_ref':'test','location':'store','material':'grain','quantity':10,'inventory_evidence_ref':'count'})
        r=self.event(r,op='ast_transfer_stock',params={'source_ref':'test','from':'store','to':'camp','material':'grain','quantity':3,'authority_ref':'host'})
        self.assertEqual(r['state']['stocks'], {'store':{'grain':7},'camp':{'grain':3}})
        with self.assertRaises(HTTPError):
            self.event(r,op='ast_transfer_stock',params={'source_ref':'test','from':'store','to':'camp','material':'grain','quantity':99,'authority_ref':'host'})
        self.assertEqual(Store(self.tmp.name).read(r['id']),r)

    def test_static_entrypoint(self):
        with urlopen(self.url) as r:
            self.assertIn(b'IRGS',r.read())
            self.assertIn("frame-ancestors 'none'",r.headers['Content-Security-Policy'])


if __name__ == '__main__': unittest.main()
