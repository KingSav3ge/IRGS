"""Independent real HTTP checks of current selected ordinary communication."""
import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / 'IRGS_Catalog/evaluation/current_ordinary_communication_v1'
ENGINE = os.environ.get('IRGS_CURRENT_ENGINE_SOURCE')
APP = os.environ.get('IRGS_CURRENT_APP_SOURCE')
ENGINE_SHA = 'f029149cb52721c823e9d416bdf96918d53b92ce'
APP_SHA = '42c4cdf62b8bcc571d5524170baced1294aacf55'
PINS = {'Engine': 'efc84364b86e640f5028bfac2dfd5ae3021695a9',
        'Catalog': '6f927b00e12a3339861ac353bc38d03c68279662'}


@unittest.skipUnless(ENGINE and APP, 'Exact current Engine and App source roots required')
class CurrentOrdinaryConsumers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for path, sha in ((ENGINE, ENGINE_SHA), (APP, APP_SHA)):
            if subprocess.check_output(['git', '-C', path, 'rev-parse', 'HEAD'], text=True).strip() != sha:
                raise RuntimeError('Wrong source revision')
            if subprocess.check_output(['git', '-C', path, 'status', '--porcelain'], text=True).strip():
                raise RuntimeError('Selected source must be clean')
        for name, sha in PINS.items():
            if subprocess.check_output(['git', '-C', APP, 'rev-parse', 'HEAD:' + name], text=True).strip() != sha:
                raise RuntimeError('App committed pin changed')
        engine, app = Path(ENGINE).resolve() / 'IRGS_3_3', Path(APP).resolve() / 'IRGS_Web'
        os.environ['IRGS_ENGINE_ROOT'] = str(engine)
        os.environ['IRGS_CATALOG_ROOT'] = str(ROOT / 'IRGS_Catalog')
        sys.path[:0] = [str(app), str(engine / 'runtime')]
        for name, source in [('server', app), ('solo_provider', engine), ('openai_proposals', engine)]:
            module = importlib.import_module(name)
            if not Path(module.__file__).resolve().is_relative_to(source):
                raise RuntimeError('Wrong imported source; use a fresh process')
            setattr(cls, name, module)
        cls.cases = json.loads((FIXTURE / 'actor_inputs/cases.json').read_text())
        cls.oracle = json.loads((FIXTURE / 'evaluator_only/expectations.json').read_text())
        assert cls.cases['fixture_id'] == 'irgs-current-ordinary-communication-v1'
        assert cls.oracle['classification'] == 'evaluator-only'
        assert cls.oracle['marker'] not in json.dumps(cls.cases)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='irgs-current-ordinary-')
        self.addCleanup(self.temp.cleanup)
        self.store = self.server.Store(Path(self.temp.name) / 'saves')
        for target in ('solo_provider.CapabilityBroker.dispatch', 'openai_proposals.OpenAIProposalTransport.__call__'):
            spy = patch(target, side_effect=AssertionError('Provider called')).start()
            self.addCleanup(patch.stopall)
            self.addCleanup(spy.assert_not_called)
        self.start()
        self.addCleanup(self.stop)

    def start(self):
        self.host = self.server.make_server(0, self.store.folder, reference_config=Path(self.temp.name) / 'no-config.json',
                                            reference_cache=Path(self.temp.name) / 'cache', solo_configuration=None)
        self.thread = threading.Thread(target=self.host.serve_forever, daemon=True)
        self.thread.start()
        self.url = 'http://127.0.0.1:' + str(self.host.server_port)
        self.token = self.http('/api/campaigns')[1]['token']

    def stop(self):
        self.host.shutdown(); self.host.server_close(); self.thread.join()

    def http(self, path, body=None):
        headers = {'X-IRGS-Token': getattr(self, 'token', '')}
        if body is not None:
            headers['Content-Type'] = 'application/json'
        req = Request(self.url + path, data=None if body is None else json.dumps(body).encode(), headers=headers)
        try:
            with urlopen(req, timeout=15) as result:
                code, value = result.status, json.load(result)
        except HTTPError as error:
            code, value = error.code, json.load(error)
        self.assertNotIn(self.oracle['marker'], json.dumps(value))
        return code, value

    def ok(self, path, body=None):
        code, value = self.http(path, body)
        self.assertEqual(code, 200, value)
        return value

    def create(self, context):
        case = self.cases[context]
        if context == 'rise':
            review = self.ok('/api/rise/preview', {'choices': case['choices']})
            self.assertIn('no response, consent or transfer is automatic', review['neighbors'])
            body = {'name': 'Synthetic R00', 'choices': case['choices'], 'review_digest': review['review_digest'],
                    'request_id': 'current-rise-create'}
            self.assertEqual(self.http('/api/rise/create', {**body, 'review_digest': 'stale'})[0], 400)
            path = '/api/rise/create'
        else:
            entry = self.ok('/api/historical-entry/hyw-1415')
            fields = {'profile_id': 'military', 'scenario_id': 'hundred-years-war', 'entry_id': 'hyw-1415',
                      'snapshot_sha256': entry['snapshot_sha256']}
            options = self.ok('/api/starting-options?' + urlencode(fields))
            self.assertTrue(next(o for o in options['playable_openings'] if o['id'] == case['opening_id'])['fictional'])
            preview = self.ok('/api/starting-preview?' + urlencode({**fields, 'selection_digest': options['selection_digest'],
                'starting_scenario_id': 'individual', 'character_kind': 'new', 'species': 'human', 'opening_id': case['opening_id']}))
            self.assertEqual(preview['status'], 'supported_slice')
            body = {**fields, 'name': 'Synthetic quay', 'selection_digest': options['selection_digest'],
                    'request_id': 'current-quay-create', 'character': {'kind': 'new', 'name': 'Synthetic courier',
                    'species': 'human', 'background': '', 'opening_id': case['opening_id']}}
            self.assertEqual(self.http('/api/create', {**body, 'selection_digest': 'stale'})[0], 400)
            path = '/api/create'
        self.assertFalse(list(self.store.folder.glob('*.json')))
        created = self.ok(path, body); key = created['id']
        before = self.store.path(key).read_bytes()
        self.assertEqual(self.ok(path, body)['id'], key)
        self.assertEqual(self.store.path(key).read_bytes(), before)
        return key

    def view(self, key):
        return self.ok('/api/playthrough/' + key)

    def prepare(self, key, actor, case, request):
        view = self.view(key)
        body = {'id': key, 'actor': actor, 'revision': view['revision'],
                'view_token': view['communication_control']['view_token'], 'request_id': request,
                'channel_id': case['channel'], 'recipient': case['recipient'], 'command': 'speak',
                'details': {}, 'intention': case['words']}
        before = self.store.path(key).read_bytes()
        packet = self.ok('/api/communication/prepare', body)
        self.assertEqual(packet['intention'], case['words'])
        self.assertEqual(self.store.path(key).read_bytes(), before)
        return body

    def execute(self, body, accepted=True):
        return self.http('/api/communication/execute', {'id': body['id'], 'actor': body['actor'],
            'request_id': body['request_id'], 'explicitly_accepted': accepted})

    def check_context(self, context):
        case, oracle = self.cases[context], self.oracle[context]
        key = self.create(context); view = self.view(key); actor = view['actor_id']
        channel = next(c for c in view['communication_control']['channels'] if c['channel_id'] == case['channel'])
        self.assertEqual([p['actor_id'] for p in channel['participants']], oracle['participants'])
        self.assertTrue(all(p['supported_commands'] == ['speak'] for p in channel['participants']))
        self.assertEqual(view['communication_control']['offers'], [])
        self.assertNotIn('stocks', json.dumps(view['communication_control']))
        if context == 'rise':
            self.assertFalse(set(oracle['excluded_participants']) & {p['actor_id'] for p in channel['participants']})
            records = view['communication_control']['received_sources']['records']
            self.assertTrue(all(any(r['originator'] == speaker and r['source_ref'] == oracle['source_ref']
                and r['status'] == 'testimony' for r in records) for speaker in oracle['participants']))
        before_state = copy.deepcopy(self.store.read(key)['state'])
        body = self.prepare(key, actor, case, 'current-speech')
        saved = self.store.path(key).read_bytes()
        self.assertEqual(self.execute(body, False)[0], 400)
        forged = {**body, 'actor': 'foreign', 'request_id': 'forged'}
        self.assertEqual(self.http('/api/communication/prepare', forged)[0], 403)
        self.assertEqual(self.store.path(key).read_bytes(), saved)
        code, result = self.execute(body); self.assertEqual(code, 200, result)
        self.assertEqual(result['communication']['status'], self.oracle['speech_status'])
        self.assertEqual(result['communication']['truth_status'], 'testimony')
        self.assertEqual(result['communication']['utterance'], case['words'])
        self.assertIsNone(result['elapsed_time'])
        state = self.store.read(key)['state']
        for field in ('stocks', 'elapsed_time', 'campaign_time'):
            self.assertEqual(state[field], before_state[field])
        saved = self.store.path(key).read_bytes(); self.stop(); self.start()
        self.assertEqual(self.execute(body), (200, result))
        self.assertEqual(self.store.path(key).read_bytes(), saved)
        view = self.view(key)
        movement = {'id': key, 'actor': actor, 'revision': view['revision'], 'request_id': 'current-departure'}
        if context == 'rise':
            path = '/api/rise/action'; movement['action'] = case['departure']
        else:
            path = '/api/action'
            choice = next(a for a in view['supported_actions'] if a['action_id'] == case['departure'])
            movement.update(kind='scene_action', action_id=case['departure'], text=choice['text'])
        self.ok(path, movement)
        distant = self.prepare(key, actor, case, 'current-distant-speech')
        saved = self.store.path(key).read_bytes()
        self.assertEqual(self.execute(distant)[0], 400)
        self.assertEqual(self.store.path(key).read_bytes(), saved)
        self.assertEqual(self.execute(body), (200, result))
        self.assertEqual(self.store.path(key).read_bytes(), saved)

    def test_rise_reviewed_introductions_and_speech(self):
        self.check_context('rise')

    def test_quay_reviewed_contact_and_speech(self):
        self.check_context('quay')


if __name__ == '__main__':
    unittest.main()
