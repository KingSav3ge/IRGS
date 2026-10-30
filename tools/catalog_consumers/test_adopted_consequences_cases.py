"""Independent adopted-set draft and consequence consumers over real HTTP."""
import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys

from tools.tests import test_intent_world_draft_consumers as prior
from tools.tests import test_current_ordinary_consumers as current
sys.path.insert(0, str(current.ROOT / 'IRGS_Catalog'))
import adopted_consequences_evaluation as selection

ENGINE = os.environ.get('IRGS_ADOPTED_ENGINE_SOURCE')
APP = os.environ.get('IRGS_ADOPTED_APP_SOURCE')
FIXTURE = current.ROOT / 'IRGS_Catalog/evaluation/adopted_consequences_v1'


class AdoptedConsequencesConsumers(prior.CandidateIntentWorldConsumers):
    __unittest_skip__ = not bool(ENGINE and APP)
    __unittest_skip_why__ = 'Exact adopted Engine/App sources required'
    test_engine_world_draft_preview_initialize_and_unsupported_boundaries = None
    test_quay_reviewed_intents_actual_failure_alternative_and_restore = None
    test_rise_reviewed_intents_work_and_restore = None

    @classmethod
    def setUpClass(cls):
        selected = selection.load_fixture()['selection']
        for path, sha in ((ENGINE, selected['engine']), (APP, selected['app'])):
            if subprocess.check_output(['git', '-C', path, 'rev-parse', 'HEAD'], text=True).strip() != sha:
                raise RuntimeError('Wrong adopted source revision')
            if subprocess.check_output(['git', '-C', path, 'status', '--porcelain'], text=True).strip():
                raise RuntimeError('Selected sources must be clean')
        for name, sha in (('Engine', selected['app_engine_pin']), ('Catalog', selected['app_catalog_pin'])):
            if subprocess.check_output(['git', '-C', APP, 'rev-parse', 'HEAD:' + name], text=True).strip() != sha:
                raise RuntimeError('Wrong App committed pin')
        engine, app = Path(ENGINE).resolve() / 'IRGS_3_3', Path(APP).resolve() / 'IRGS_Web'
        os.environ['IRGS_ENGINE_ROOT'], os.environ['IRGS_CATALOG_ROOT'] = str(engine), str(current.ROOT / 'IRGS_Catalog')
        sys.path[:0] = [str(app), str(engine / 'runtime')]
        for name, source in [('server', app), ('solo_provider', engine), ('openai_proposals', engine),
                             ('world_draft', engine), ('offline_responses', engine), ('core_world', engine)]:
            module = importlib.import_module(name)
            if not Path(module.__file__).resolve().is_relative_to(source): raise RuntimeError('Wrong imported checkout')
            setattr(cls, name, module)
        cls.cases = json.loads((current.FIXTURE / 'actor_inputs/cases.json').read_text())
        cls.oracle = json.loads((current.FIXTURE / 'evaluator_only/expectations.json').read_text())
        cls.inputs = json.loads((FIXTURE / 'actor_inputs/cases.json').read_text())
        cls.expected = json.loads((FIXTURE / 'evaluator_only/expectations.json').read_text())
        assert cls.expected['marker'] not in json.dumps(cls.inputs)

    def test_two_bounded_drafts_preview_and_explicit_initialize(self):
        for context in ('quay', 'rise'):
            with self.subTest(context=context):
                draft = copy.deepcopy(self.inputs['drafts'][context]); before = copy.deepcopy(draft)
                self.assertFalse(list(self.store.folder.glob('*.json')))
                review = self.world_draft.inspect(draft)
                self.assertEqual(review['status'], 'valid'); self.assertFalse(review['committed'])
                preview = self.world_draft.preview_initialization(draft)
                self.assertEqual(preview['status'], 'preview_only'); self.assertFalse(preview['committed'])
                self.assertFalse(preview['preview_identities_reusable'])
                self.assertNotIn(self.expected['marker'], json.dumps(preview))
                self.assertNotIn('state_digest', json.dumps(preview))
                self.assertNotIn('opening_npc_inventory', json.dumps(preview))
                args = {'draft_digest': review['draft_digest'], 'review_digest': review['review_digest'],
                        'campaign_id': 'catalog-adopted-' + context, 'explicitly_accepted': False}
                with self.assertRaises(ValueError): self.world_draft.initialize(draft, **args)
                world = self.world_draft.initialize(draft, **{**args, 'explicitly_accepted': True})
                self.assertTrue(world.s['player_actor_ids']); self.assertEqual(before, draft)
                self.assertFalse(list(self.store.folder.glob('*.json')))
                if context == 'quay':
                    self.assertIsNone(world.s['campaign_time']['civil']['time'])
                    self.assertEqual(world.s['binding']['snapshot_sha256'], draft['choices']['snapshot_sha256'])
                    self.assertNotEqual(preview['actor_view']['actor_id'], world.s['player_actor_ids'][0])
                changed = copy.deepcopy(draft)
                if context == 'rise': changed['choices']['supplies'] = 'stocked'
                else: changed['choices']['character']['name'] = 'Different courier'
                with self.assertRaises(ValueError): self.world_draft.initialize(changed, **{**args, 'explicitly_accepted': True})
                self.assertIn('custom geography or entities', review['unsupported'])

    def create_context(self, context):
        if context == 'quay': return self.create('quay')
        choices = self.inputs['drafts']['rise']['choices']
        review = self.ok('/api/rise/preview', {'choices': choices})
        self.assertIn('no recipient consent', review['offer_setup']['notice'])
        return self.ok('/api/rise/create', {'name': 'Synthetic adopted Reed', 'choices': choices,
            'review_digest': review['review_digest'], 'request_id': 'adopted-reed-create'})['id']

    def test_quay_failure_alternative_delivery_and_original_result_recovery(self):
        key = self.create_context('quay'); actor = self.view(key)['actor_id']; results = []
        expected = self.expected['quay']
        for index, action in enumerate(self.inputs['journeys']['quay']):
            request, result = self.reviewed_action(key, actor, action, index)
            self.assertEqual(result['status'], expected['statuses'][index]); results.append((request, result))
            if index == 1:
                self.stop(); self.start()
                self.assertEqual(self.http('/api/intent/execute', {**request, 'explicitly_accepted': True}), (200, result))
        state = self.store.read(key)['state']
        self.assertEqual(state['elapsed_time']['seconds'], expected['elapsed_seconds'])
        self.assertEqual(state['stocks'][actor]['sealed_dispatch'], expected['dispatch_actor'])
        self.assertEqual(state['stocks']['clerk-tray']['sealed_dispatch'], expected['dispatch_tray'])
        self.assertEqual(sum(row.get('sealed_dispatch', 0) for row in state['stocks'].values()), 1)
        saved = self.store.path(key).read_bytes()
        for request, result in results:
            self.assertEqual(self.http('/api/intent/execute', {**request, 'explicitly_accepted': True}), (200, result))
        self.assertEqual(self.store.path(key).read_bytes(), saved)

    def communication(self, key, actor, command, details, request_id, words):
        view = self.view(key); case = self.inputs['stock_offer']
        body = {'id': key, 'actor': actor, 'revision': view['revision'],
            'view_token': view['communication_control']['view_token'], 'request_id': request_id,
            'channel_id': case['channel'], 'recipient': case['recipient'], 'command': command,
            'details': details, 'intention': words}
        before = self.store.path(key).read_bytes(); review = self.ok('/api/communication/prepare', body)
        self.assertEqual(review['intention'], words); self.assertEqual(self.store.path(key).read_bytes(), before)
        self.assertEqual(self.execute(body, False)[0], 400); self.assertEqual(self.store.path(key).read_bytes(), before)
        code, result = self.execute(body); self.assertEqual(code, 200, result)
        self.assertEqual(result['presentation']['render_usage'], {'provider_calls': 0, 'model_tokens': 0})
        self.assertNotIn(self.expected['marker'], json.dumps(result))
        return body, result

    def test_rise_permission_refusal_offer_withdrawal_and_later_founding(self):
        key = self.create_context('rise'); actor = self.view(key)['actor_id']; case = self.inputs['stock_offer']
        initial = copy.deepcopy(self.store.read(key)['state']['stocks'])
        offer, offered = self.communication(key, actor, 'offer', {'terms': case['terms']}, 'adopted-stock-offer', case['words'])
        self.assertEqual(offered['communication']['status'], self.expected['rise']['stock_offer_states'][0])
        self.assertEqual(self.store.read(key)['state']['stocks'], initial)
        self.assertFalse(self.store.read(key)['state']['grants'])
        unauthorized = {'id': key, 'actor': 'oren', 'request_id': offer['request_id'], 'explicitly_accepted': True}
        self.assertEqual(self.http('/api/communication/execute', unauthorized)[0], 403)
        details = {'offer_id': offered['communication']['offer_id'], 'terms_digest': offered['communication']['terms_digest']}
        _, withdrawn = self.communication(key, actor, 'withdraw', details, 'adopted-stock-withdraw', 'I withdraw my offer.')
        self.assertEqual(withdrawn['communication']['status'], self.expected['rise']['stock_offer_states'][1])
        self.assertEqual(self.store.read(key)['state']['stocks'], initial)
        actions = self.inputs['journeys']['rise']; results = []
        request, result = self.reviewed_action(key, actor, actions[0], 0); results.append((request, result))
        view = self.view(key); control = view['intent_control']
        capability = next(c for c in control['capabilities'] if c['action'].get('action_id') == actions[1]['action'])
        body = {'id': key, 'actor': actor, 'revision': view['revision'], 'view_token': control['view_token'],
                'request_id': 'adopted-refused-found', 'intention': actions[1]['intention'], 'capability_id': capability['capability_id']}
        before = self.store.path(key).read_bytes(); self.ok('/api/intent/prepare', body)
        self.assertEqual(self.http('/api/intent/execute', {'id': key, 'actor': actor, 'request_id': body['request_id'], 'explicitly_accepted': True})[0], 400)
        self.assertEqual(self.store.path(key).read_bytes(), before)
        for index, action in enumerate(actions[2:], start=2):
            request, result = self.reviewed_action(key, actor, action, index)
            self.assertEqual(result['status'], 'completed_successfully'); results.append((request, result))
            state = self.store.read(key)['state']
            if action['action'] == 'request_grant': self.assertEqual(state['grants']['founding']['status'], self.expected['rise']['grant_states'][0])
            if action['action'] == 'accept_grant': self.assertEqual(state['grants']['founding']['status'], self.expected['rise']['grant_states'][1])
        state = self.store.read(key)['state']
        self.assertEqual(state['elapsed_time']['seconds'], self.expected['rise']['elapsed_seconds'])
        self.assertEqual(state['stocks'], initial); self.assertIn('camp', state['settlements'])
        saved = self.store.path(key).read_bytes(); self.stop(); self.start()
        for request, result in results:
            self.assertEqual(self.http('/api/intent/execute', {**request, 'explicitly_accepted': True}), (200, result))
        self.assertEqual(self.execute(offer), (200, offered))
        self.assertEqual(self.store.path(key).read_bytes(), saved)
