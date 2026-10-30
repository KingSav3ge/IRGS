"""Independent selected invitation and bounded draft consumers over real HTTP."""
import copy
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys

from tools.tests import test_adopted_consequences_consumers as previous
from tools.tests import test_current_ordinary_consumers as current

ENGINE = os.environ.get('IRGS_INVITATION_ENGINE_SOURCE')
APP = os.environ.get('IRGS_INVITATION_APP_SOURCE')
ROOT = current.ROOT / 'IRGS_Catalog'
FIXTURE = ROOT / 'evaluation/invitation_decision_v1'


class InvitationDecisionConsumers(previous.AdoptedConsequencesConsumers):
    __unittest_skip__ = not bool(ENGINE and APP)
    __unittest_skip_why__ = 'Exact invitation Engine/App sources required'
    test_rise_permission_refusal_offer_withdrawal_and_later_founding = None

    @classmethod
    def setUpClass(cls):
        manifest = json.loads((FIXTURE / 'manifest.json').read_text())
        expected_selection = {'engine': '74a185104d0d856e951e2e547a0a1d2d06d1499e',
            'app': '4ffd53a351a4d21c2005505076641c1827425147',
            'app_engine_pin': 'fe9c2c10ec3a66f1be590e1b34860119670b22cb',
            'app_catalog_pin': 'cf69a6cf628a6d9249124cc6b0700dfc59287677',
            'catalog': 'containing-commit', 'engine_override': True, 'catalog_override': True}
        if manifest['selection'] != expected_selection:
            raise RuntimeError('Wrong selected source set')
        if manifest['fixture_id'] != 'worldward-invitation-decision-v1' or set(manifest['files_sha256']) != {'actor_inputs/cases.json', 'evaluator_only/expectations.json'}:
            raise RuntimeError('Incomplete fixture manifest')
        for name, digest in manifest['files_sha256'].items():
            if hashlib.sha256((FIXTURE / name).read_bytes()).hexdigest() != digest:
                raise RuntimeError('Changed fixture')
        baseline = manifest['baseline']
        if baseline != {'path': 'evaluation/adopted_consequences_v1/manifest.json',
                        'sha256': '72b3216c1cbcd8eaf0d59e44a681653f6b8273acbd8daa688357e4592aa38be3'}:
            raise RuntimeError('Wrong prior fixture binding')
        if hashlib.sha256((ROOT / baseline['path']).read_bytes()).hexdigest() != baseline['sha256']:
            raise RuntimeError('Prior fixture changed')
        for path, sha in ((ENGINE, expected_selection['engine']), (APP, expected_selection['app'])):
            if subprocess.check_output(['git', '-C', path, 'rev-parse', 'HEAD'], text=True).strip() != sha:
                raise RuntimeError('Wrong selected source revision')
            if subprocess.check_output(['git', '-C', path, 'status', '--porcelain'], text=True).strip():
                raise RuntimeError('Selected sources must be clean')
        for component in ('Engine', 'Catalog'):
            if subprocess.check_output(['git', '-C', APP, 'rev-parse', 'HEAD:' + component], text=True).strip() != expected_selection['app_' + component.lower() + '_pin']:
                raise RuntimeError('Wrong App committed pin')
        engine, app = Path(ENGINE).resolve() / 'IRGS_3_3', Path(APP).resolve() / 'IRGS_Web'
        os.environ['IRGS_ENGINE_ROOT'], os.environ['IRGS_CATALOG_ROOT'] = str(engine), str(ROOT)
        sys.path[:0] = [str(app), str(engine / 'runtime')]
        for name, source in [('server', app), ('solo_provider', engine), ('openai_proposals', engine),
                             ('world_draft', engine), ('offline_responses', engine), ('core_world', engine)]:
            module = importlib.import_module(name)
            if not Path(module.__file__).resolve().is_relative_to(source):
                raise RuntimeError('Wrong imported checkout')
            setattr(cls, name, module)
        cls.cases = json.loads((current.FIXTURE / 'actor_inputs/cases.json').read_text())
        cls.oracle = json.loads((current.FIXTURE / 'evaluator_only/expectations.json').read_text())
        cls.inputs = json.loads((FIXTURE / 'actor_inputs/cases.json').read_text())
        cls.new_oracle = json.loads((FIXTURE / 'evaluator_only/expectations.json').read_text())
        cls.expected = json.loads((previous.FIXTURE / 'evaluator_only/expectations.json').read_text())
        if (cls.inputs['fixture_id'] != manifest['fixture_id'] or
                cls.new_oracle['classification'] != 'evaluator-only' or
                set(cls.new_oracle['unmet_requirements']) != {'npc_decisions', 'institution_decisions',
                    'needs_recovery', 'risk_conflict', 'consequences', 'authoring', 'live_provider'} or
                any(not value for value in cls.new_oracle['unmet_requirements'].values()) or
                cls.new_oracle['marker'] in json.dumps(cls.inputs)):
            raise RuntimeError('Evaluator data leaked into actor inputs')

    def test_refusal_then_separate_agreement_and_exact_recovery(self):
        key = self.create_context('rise'); actor = self.view(key)['actor_id']
        actions = self.inputs['invitation']['actions']; oracle = self.new_oracle['rise']
        for index, action in enumerate(actions[:3]):
            self.reviewed_action(key, actor, action, index)
        state = self.store.read(key)['state']
        stocks, seconds = copy.deepcopy(state['stocks']), state['elapsed_time']['seconds']
        request, refusal = self.reviewed_action(key, actor, actions[3], 3)
        self.assertEqual(refusal['status'], 'completed_successfully')
        self.assertIn(oracle['refusal'], refusal['outcome']['summary'].lower())
        self.assertNotIn(self.new_oracle['marker'], json.dumps(refusal))
        for private in ('oren-repair', 'seed_reserve', 'grain', self.new_oracle['marker']):
            self.assertNotIn(private, json.dumps(refusal).lower())
        state = self.store.read(key)['state']
        self.assertNotIn(oracle['migration_id'], state['migrations'])
        self.assertEqual(state['stocks'], stocks)
        self.assertEqual(state['elapsed_time']['seconds'], seconds)
        saved = self.store.path(key).read_bytes()
        forbidden = {**request, 'actor': 'oren', 'explicitly_accepted': True}
        self.assertEqual(self.http('/api/intent/execute', forbidden)[0], 403)
        self.assertEqual(self.store.path(key).read_bytes(), saved)
        self.reviewed_action(key, actor, actions[4], 4)
        _, agreement = self.reviewed_action(key, actor, actions[5], 5)
        self.assertIn(oracle['agreement'], agreement['outcome']['summary'].lower())
        state = self.store.read(key)['state']
        self.assertEqual(state['migrations'][oracle['migration_id']]['status'], 'agreed')
        self.assertEqual(state['actors']['oren']['current']['location'], 'commons')
        saved = self.store.path(key).read_bytes(); self.stop(); self.start()
        self.assertEqual(self.http('/api/intent/execute', {**request, 'explicitly_accepted': True}), (200, refusal))
        self.assertEqual(self.store.path(key).read_bytes(), saved)
