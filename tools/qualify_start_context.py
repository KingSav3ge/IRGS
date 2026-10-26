"""Qualify Catalog's six reviewed starts through the actual selected App host.

Synthetic stores and local requests only. Fixture actor inputs are sent to the
host; evaluator-only requirements remain in this checker. No old fixture pin is
modified and no continuing user campaign is opened or initialized.
"""
import argparse
from contextlib import ExitStack
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import ProxyHandler, Request, build_opener

SERVER = EVALUATION = CATALOG = None
OBSERVATIONS = {}


class CatalogStartTests(unittest.TestCase):
    def setUp(self):
        stack = ExitStack()
        self.addCleanup(stack.close)
        self.dispatch = stack.enter_context(patch('solo_provider.CapabilityBroker.dispatch', side_effect=AssertionError('No inference')))
        self.transport = stack.enter_context(patch('openai_proposals.OpenAIProposalTransport.__call__', side_effect=AssertionError('No provider transport')))
        stack.enter_context(patch('http.server.BaseHTTPRequestHandler.log_message'))
        self.folder = stack.enter_context(tempfile.TemporaryDirectory(prefix='irgs-catalog-starts-'))
        self.store = SERVER.Store(self.folder)
        self.token = None
        self.opener = build_opener(ProxyHandler({}))
        self.start()
        self.addCleanup(self.stop)
        self.oracle = EVALUATION.load_evaluator_data()

    def tearDown(self):
        self.dispatch.assert_not_called()
        self.transport.assert_not_called()

    def start(self):
        self.host = SERVER.make_server(0, self.folder, solo_configuration=None)
        self.thread = threading.Thread(target=self.host.serve_forever, daemon=True)
        self.thread.start()
        self.base = 'http://127.0.0.1:' + str(self.host.server_port)
        self.token = self.call('/api/campaigns')['token']

    def stop(self):
        self.host.shutdown()
        self.host.server_close()
        self.thread.join()

    def call(self, path, body=None):
        headers = {'Content-Type': 'application/json'}
        if self.token:
            headers['X-IRGS-Token'] = self.token
        request = Request(self.base + path, headers=headers,
                          data=None if body is None else json.dumps(body).encode())
        with self.opener.open(request, timeout=15) as response:
            result = json.load(response)
        self.assertNotIn(self.oracle['hidden_marker'] if hasattr(self, 'oracle') else 'PRIVATE_START_CONTEXT_ORACLE', json.dumps(result))
        return result

    def journey(self, case):
        actor_input = EVALUATION.export_actor_input(case)
        expected = self.oracle['cases'][case]
        selection = actor_input['selection']
        historical = expected['historical']
        if historical:
            entry = self.call('/api/historical-entry/' + selection['entry_id'])
            fields = {k: selection[k] for k in ('profile_id', 'scenario_id', 'entry_id')}
            fields['snapshot_sha256'] = entry['snapshot_sha256']
            options = self.call('/api/starting-options?' + urlencode(fields))
            character = selection['character']
            query = {**fields, 'selection_digest': options['selection_digest'], 'character_kind': character['kind']}
            query.update({k: character[k] for k in ('actor_id', 'opening_id', 'species') if k in character})
            preview = self.call('/api/starting-preview?' + urlencode(query))
            self.assertEqual(preview['engine_start_context_contract'], EVALUATION.ENGINE_SCHEMA)
            self.assertEqual(preview['status'], expected['selected_mode'])
            body = {**fields, 'name': 'Synthetic ' + case, 'character': character,
                    'selection_digest': options['selection_digest'], 'request_id': 'catalog-create-' + case}
            creation_path = '/api/create'
        else:
            setup = json.loads((CATALOG / 'evaluation/solo_r00_v1/evaluator_only/setup.json').read_text())['choices']
            preview = self.call('/api/rise/preview', {'choices': setup})
            body = {'name': 'Synthetic R00', 'choices': setup, 'review_digest': preview['review_digest'],
                    'request_id': 'catalog-create-r00'}
            creation_path = '/api/rise/create'
        created = self.call(creation_path, body)
        key = created['id']
        view = self.call('/api/playthrough/' + key)
        actor = view['actor_id']
        self.assertEqual(view['play_readiness']['status'], expected['selected_mode'])
        initial_time = view['campaign_time']
        if historical:
            civil = view['start_context']['civil_time']
            self.assertEqual(view['campaign_time']['civil'], civil)
            for field, value in self.oracle['civil_checkpoint'].items():
                self.assertEqual(civil[field], value)
            self.assertEqual(civil['status'], 'received_initial_checkpoint')
            self.assertIsNone(civil['opening_hour'])
            self.assertEqual([p['id'] for p in view['known_actors']], [actor])
        if case == 'henry-1415-observation':
            self.assertEqual(view['scene']['scope'], 'sourced_setting_with_selected_simulation_observation_rule')
            self.assertEqual([a['action_id'] for a in view['supported_actions']], ['observe-embarkation'])
            self.assertEqual(view['inventory'], [])
            prompt = next(b['text'] for b in view['opening']['blocks'] if b['kind'] == 'first_decision')
            for forbidden in ('dispatch', 'deliver', 'travel'):
                self.assertNotIn(forbidden, prompt.lower())
        receipts = []
        last_body = last_path = None
        for index, action_id in enumerate(actor_input['actions']):
            view = self.call('/api/playthrough/' + key)
            action_body = {'id': key, 'actor': actor, 'revision': view['revision'],
                           'request_id': 'catalog-action-' + str(index)}
            if historical:
                action = next(a for a in view['supported_actions'] if a.get('action_id') == action_id)
                # This existing route accepts the exact published structured
                # action text. Editable own responses use /api/declaration;
                # changing that mapping would be an unimplemented resolver.
                action_body.update(kind='scene_action', action_id=action_id, text=action['text'])
                path = '/api/action'
            else:
                action_body.update(action=action_id)
                path = '/api/rise/action'
            receipt = self.call(path, action_body)
            self.assertIn(receipt['status'], ('completed_successfully', 'completed_unsuccessfully'))
            self.assertEqual(self.call(path, action_body), receipt)
            self.assertEqual(self.call('/api/action-result/' + key + '/' + action_body['request_id'] + '?actor_id=' + actor), receipt)
            receipts.append(receipt)
            last_body, last_path = action_body, path
        if not actor_input['actions']:
            self.assertEqual(view['supported_actions'], [])
            self.assertIsNone(view['scene']['location'])
            declaration = {'id': key, 'revision': view['revision'], 'actor': actor,
                           'request_id': 'limited-intent', 'declaration': actor_input['intention']}
            receipt = self.call('/api/declaration', declaration)
            self.assertEqual(receipt['status'], 'declared_not_resolved')
            self.assertEqual(self.call('/api/declaration', declaration), receipt)
        view = self.call('/api/playthrough/' + key)
        if expected['full_elapsed_seconds'] is not None:
            elapsed = view['elapsed_time']['seconds'] if historical else view['settlement']['elapsed_seconds']
            self.assertEqual(elapsed, expected['full_elapsed_seconds'])
        else:
            self.assertIsNone(view['elapsed_time'])
        if historical:
            self.assertEqual(view['campaign_time'], initial_time)
        if case == 'new-1415-quay':
            state = self.store.read(key)['state']
            self.assertEqual(state['stocks'][actor]['sealed_dispatch'], 0)
            self.assertEqual(state['stocks']['clerk-tray']['sealed_dispatch'], 1)
            self.assertEqual(sum(r['status'] == 'completed_unsuccessfully' for r in receipts), 1)
        if case == 'rise-r00':
            state = self.store.read(key)['state']
            self.assertEqual(state['stocks']['founder-home']['timber'], 3)
        raw = self.store.path(key).read_bytes()
        revision = view['revision']
        self.stop()
        self.start()
        self.assertEqual(self.call('/api/playthrough/' + key)['revision'], revision)
        self.assertEqual(self.call(creation_path, body)['id'], key)
        if receipts:
            self.assertEqual(self.call(last_path, last_body), receipts[-1])
            with self.assertRaises(HTTPError) as denied:
                self.call('/api/playthrough/' + key + '?actor_id=not-the-controlled-actor')
            self.assertEqual(denied.exception.code, 403)
        self.assertEqual(self.store.path(key).read_bytes(), raw)
        self.call('/api/delete', {'id': key, 'revision': revision})
        self.call('/api/restore', {'id': key, 'revision': revision})
        self.assertEqual(self.store.path(key).read_bytes(), raw)
        self.assertEqual(self.call('/api/playthrough/' + key)['revision'], revision)
        OBSERVATIONS[case] = {'mode': expected['selected_mode'], 'historical': historical,
            'confirmed_operations': len(receipts), 'elapsed_seconds': expected['full_elapsed_seconds'],
            'civil_day_precision': historical, 'restart_and_exact_retry': True,
            'restore_preserved_save': True, 'provider_calls': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if sys.flags.optimize:
        raise ValueError('Do not use optimized Python')
    root = args.source_root.resolve()
    global SERVER, CATALOG, EVALUATION
    CATALOG = root / 'IRGS_Catalog'
    os.environ.update(IRGS_ENGINE_ROOT=str(root / 'IRGS_3_3'), IRGS_CATALOG_ROOT=str(CATALOG))
    sys.path.insert(0, str(root / 'IRGS_Web'))
    import server as SERVER
    spec = importlib.util.spec_from_file_location('coordinator_catalog_start_contract', CATALOG / 'start_context_evaluation.py')
    EVALUATION = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(EVALUATION)
    EVALUATION.load_fixture()
    for case in EVALUATION.CASES:
        def test(self, selected=case):
            self.journey(selected)
        setattr(CatalogStartTests, 'test_' + case.replace('-', '_'), test)
    log = io.StringIO()
    result = unittest.TextTestRunner(stream=log, verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(CatalogStartTests))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_suffix('.log').write_text(log.getvalue())
    report = {'status': 'passed' if result.wasSuccessful() else 'failed', 'fixture_id': EVALUATION.FIXTURE_ID,
              'catalog_fixture_sha256': hashlib.sha256((CATALOG / EVALUATION.FIXTURE / 'manifest.json').read_bytes()).hexdigest(),
              'selected_components': json.loads((root / 'COMPONENTS.json').read_text()),
              'tests_run': result.testsRun, 'failed': len(result.failures), 'errors': len(result.errors),
              'skipped': len(result.skipped), 'cases': OBSERVATIONS, 'provider_calls': 0, 'user_saves_used': False}
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': report['status'], 'tests_run': result.testsRun, 'report': str(args.output)}))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
