"""Independent candidate DTO and ordinary App HTTP consumers."""
import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys

from tools.tests import test_current_ordinary_consumers as current
sys.path.insert(0, str(current.ROOT / 'IRGS_Catalog'))
import intent_world_draft_evaluation as selection
import grounding_quality as rubric

ENGINE = os.environ.get('IRGS_CANDIDATE_ENGINE_SOURCE')
APP = os.environ.get('IRGS_CANDIDATE_APP_SOURCE')
ENGINE_SHA = '44ea8b0f66801c12a039c0046128177d2ea6d7d8'
APP_SHA = '4f7cbd703d1207ae32db2bbc90d429415ae1e13f'
APP_PINS = {'Engine': '296e46a1beed10d0ebf2841f133bb52fade83697',
            'Catalog': 'e97d87f0d17a16dbe0ce186badafe663188321a1'}
FIXTURE = current.ROOT / 'IRGS_Catalog/evaluation/intent_world_draft_v1'


class CandidateIntentWorldConsumers(current.CurrentOrdinaryConsumers):
    __unittest_skip__ = not bool(ENGINE and APP)
    __unittest_skip_why__ = 'Exact candidate Engine/App sources required'
    test_quay_reviewed_contact_and_speech = None
    test_rise_reviewed_introductions_and_speech = None

    @classmethod
    def setUpClass(cls):
        chosen = selection.load_fixture()['selection']
        if (chosen['engine'], chosen['app'], chosen['app_engine_pin'], chosen['app_catalog_pin']) != (
                ENGINE_SHA, APP_SHA, APP_PINS['Engine'], APP_PINS['Catalog']):
            raise RuntimeError('Unexpected selection manifest')
        for path, sha in ((ENGINE, ENGINE_SHA), (APP, APP_SHA)):
            if subprocess.check_output(['git', '-C', path, 'rev-parse', 'HEAD'], text=True).strip() != sha:
                raise RuntimeError('Wrong candidate source revision')
            if subprocess.check_output(['git', '-C', path, 'status', '--porcelain'], text=True).strip():
                raise RuntimeError('Candidate sources must be clean')
        for component, sha in APP_PINS.items():
            if subprocess.check_output(['git', '-C', APP, 'rev-parse', 'HEAD:' + component], text=True).strip() != sha:
                raise RuntimeError('Unexpected App committed pin')
        engine, app = Path(ENGINE).resolve() / 'IRGS_3_3', Path(APP).resolve() / 'IRGS_Web'
        os.environ['IRGS_ENGINE_ROOT'], os.environ['IRGS_CATALOG_ROOT'] = str(engine), str(current.ROOT / 'IRGS_Catalog')
        sys.path[:0] = [str(app), str(engine / 'runtime')]
        for name, root in [('server', app), ('solo_provider', engine), ('openai_proposals', engine),
                           ('world_draft', engine), ('offline_responses', engine), ('core_world', engine)]:
            module = importlib.import_module(name)
            if not Path(module.__file__).resolve().is_relative_to(root):
                raise RuntimeError('Unexpected import; use fresh process')
            setattr(cls, name, module)
        cls.cases = json.loads((current.FIXTURE / 'actor_inputs/cases.json').read_text())
        cls.oracle = json.loads((current.FIXTURE / 'evaluator_only/expectations.json').read_text())
        cls.inputs = json.loads((FIXTURE / 'actor_inputs/cases.json').read_text())
        cls.expected = json.loads((FIXTURE / 'evaluator_only/expectations.json').read_text())
        assert cls.inputs['fixture_id'] == 'irgs-intent-world-draft-v1'
        assert cls.expected['classification'] == 'evaluator-only'
        assert cls.expected['marker'] not in json.dumps(cls.inputs)

    def test_engine_world_draft_preview_initialize_and_unsupported_boundaries(self):
        draft = copy.deepcopy(self.inputs['draft']); original = copy.deepcopy(draft)
        self.assertFalse(list(self.store.folder.glob('*.json')))
        result = self.world_draft.inspect(draft)
        self.assertEqual((result['schema_version'], result['status'], result['profile_id']),
                         ('irgs-world-validation-1', self.expected['draft']['status'], self.expected['draft']['profile_id']))
        self.assertFalse(result['committed']); self.assertEqual(draft, original)
        self.assertEqual(result['proposed_initializer'], 'settlement_setup.initialize')
        self.assertIn('custom geography or entities', result['unsupported'])
        args = {'draft_digest': result['draft_digest'], 'review_digest': result['review_digest'],
                'campaign_id': 'catalog-synthetic-draft', 'explicitly_accepted': False}
        with self.assertRaises(ValueError): self.world_draft.initialize(draft, **args)
        self.assertFalse(list(self.store.folder.glob('*.json')))
        world = self.world_draft.initialize(draft, **{**args, 'explicitly_accepted': True})
        self.assertEqual(world.s['player_actor_ids'], [self.expected['draft']['player_actor']])
        self.assertEqual(draft, original); self.assertFalse(list(self.store.folder.glob('*.json')))
        changed = copy.deepcopy(draft); changed['choices']['supplies'] = 'stocked'
        with self.assertRaises(ValueError): self.world_draft.initialize(changed, **{**args, 'explicitly_accepted': True})
        for bad in ({**draft, 'profile_id': 'personal-adventure'}, {**draft, 'classification': 'historical'},
                    {**draft, 'script': 'unsupported'}, {**draft, 'assets': ['unknown']}):
            with self.subTest(draft=bad):
                issue = self.world_draft.inspect(bad)
                self.assertEqual(issue['status'], 'invalid'); self.assertFalse(issue['committed'])
                self.assertTrue(issue['errors'])

    def create_context(self, context):
        if context == 'quay': return self.create('quay')
        choices = self.inputs['draft']['choices']
        review = self.ok('/api/rise/preview', {'choices': choices})
        created = self.ok('/api/rise/create', {'name': 'Synthetic catalog Reed', 'choices': choices,
            'review_digest': review['review_digest'], 'request_id': 'catalog-reed-create'})
        return created['id']

    def reviewed_action(self, key, actor, action, index):
        view = self.view(key); control = view['intent_control']
        cap = next(row for row in control['capabilities'] if row['action'].get('action_id') == action['action'])
        body = {'id': key, 'actor': actor, 'revision': view['revision'], 'view_token': control['view_token'],
                'request_id': 'catalog-intent-' + str(index), 'intention': action['intention'],
                'capability_id': cap['capability_id']}
        before = self.store.path(key).read_bytes()
        review = self.ok('/api/intent/prepare', body)
        self.assertEqual(review['intention'], action['intention'])
        self.assertEqual(review['capability']['action']['action_id'], action['action'])
        self.assertEqual(before, self.store.path(key).read_bytes())
        execute = {k: body[k] for k in ('id', 'actor', 'request_id')}
        self.assertEqual(self.http('/api/intent/execute', {**execute, 'explicitly_accepted': False})[0], 400)
        self.assertEqual(before, self.store.path(key).read_bytes())
        result = self.ok('/api/intent/execute', {**execute, 'explicitly_accepted': True})
        self.assertEqual(result['declaration'], action['intention'])
        event = result['receipt']['event_id']
        world = self.core_world.CoreWorld(state=self.store.read(key)['state'])
        facts = self.offline_responses.receipt_facts(world, actor, event)
        self.assertEqual(result['outcome']['summary'], facts['literal_text'])
        committed = {'event_id': event, 'status': result['status'], 'truth_status': 'committed_receipt',
                     'utterance': facts['literal_text']}
        rendered = {'event_id': result['presentation']['source_ref'], 'status': result['status'],
                    'truth_status': 'committed_receipt', 'utterance': result['outcome']['summary']}
        assessment = rubric.assess_receipt(committed, rendered)
        self.assertEqual(assessment['status'], 'exact_structured_match')
        self.assertFalse(assessment['free_text_semantics_checked'])
        self.assertFalse(assessment['live_model_quality_verified'])
        self.assertTrue(result['presentation']['text'].startswith(facts['literal_text']))
        self.assertEqual(result['presentation']['source_ref'], event)
        self.assertEqual(result['presentation']['render_usage'], {'provider_calls': 0, 'model_tokens': 0})
        self.assertNotIn(self.expected['marker'], json.dumps(result))
        return execute, result

    def check_journey(self, context):
        key = self.create_context(context); actor = self.view(key)['actor_id']
        checkpoint = self.store.path(key).read_bytes(); checkpoint_revision = self.store.read(key)['revision']
        actions, expectation = self.inputs['journeys'][context], self.expected['journeys'][context]
        results = []
        for index, action in enumerate(actions):
            request, result = self.reviewed_action(key, actor, action, index)
            self.assertEqual(result['status'], expectation['statuses'][index])
            results.append((request, result))
            if index == 1:
                self.stop(); self.start()
                self.assertEqual(self.http('/api/intent/execute', {**request, 'explicitly_accepted': True}), (200, result))
        state = self.store.read(key)['state']; self.assertEqual(state['elapsed_time']['seconds'], expectation['elapsed_seconds'])
        if context == 'quay':
            self.assertEqual(state['stocks'][actor]['sealed_dispatch'], expectation['dispatch_actor'])
            self.assertEqual(state['stocks']['clerk-tray']['sealed_dispatch'], expectation['dispatch_tray'])
        else:
            self.assertEqual(state['projects']['shelter']['worked'], expectation['shelter_work_seconds'])
            self.assertEqual(state['stocks']['founder-home']['timber'], expectation['founder_timber'])
        saved = self.store.path(key).read_bytes()
        for request, result in results:
            self.assertEqual(self.http('/api/intent/execute', {**request, 'explicitly_accepted': True}), (200, result))
        self.assertEqual(self.store.path(key).read_bytes(), saved)
        # Install an older synthetic checkpoint, then exercise the real Trash API
        # which rotates restore identity; never read or overwrite a user save.
        self.store.path(key).write_bytes(checkpoint)
        self.ok('/api/delete', {'id': key, 'revision': checkpoint_revision})
        self.ok('/api/restore', {'id': key, 'revision': checkpoint_revision})
        self.assertEqual(self.store.path(key).read_bytes(), checkpoint)
        for request, _ in results:
            self.assertEqual(self.http('/api/intent/execute', {**request, 'explicitly_accepted': True})[0], 400)
        self.assertEqual(self.store.path(key).read_bytes(), checkpoint)

    def test_quay_reviewed_intents_actual_failure_alternative_and_restore(self):
        self.check_journey('quay')

    def test_rise_reviewed_intents_work_and_restore(self):
        self.check_journey('rise')
