"""Engine-owned local text, actual effects, privacy and zero-dispatch evidence."""
import copy
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from core_world import CoreWorld
from offline_responses import player_drafts, render_receipt, render_status
from routine_format import compose, compose_recipe, load_library, render_fragment, validate_library
from settlement_runtime import execute as settlement_action
from settlement_setup import initialize, preview
from solo_provider import WorldScope
from test_scene_actions import fixture, execute as scene_action, apply
from test_settlement import choices


def context(family, *, actor='pc', snapshot='snapshot-1'):
    values = {key: 2 if kind == 'integer' else '{literal} <text> says no.'
              for key, kind in family['slots'].items()}
    return {'actor_id': actor, 'snapshot_id': snapshot, 'source_ref': family['id'],
            'source_kind': family['source_kind'], 'state': family['state'], 'values': values}


class OfflineResponseTests(unittest.TestCase):
    def rise(self):
        c = choices(); c['permission'] = 'held'
        return initialize(c, preview(c)['review_digest'], 'offline-text-fixture')

    def helper(self, module, name):
        case = getattr(module, name)(methodName='runTest')
        case.setUp(); self.addCleanup(case.doCleanups)
        return case

    def test_all_338_variants_and_15_recipes_format_without_dispatch(self):
        library = load_library()
        self.assertEqual(validate_library(library)['variants'], 338)
        self.assertEqual(len(library['recipes']), 15)
        families = {f['id']: f for f in library['families']}
        with patch('solo_provider.CapabilityBroker.dispatch', side_effect=AssertionError('dispatch forbidden')):
            for family in families.values():
                for variant in range(len(family['variants'])):
                    with self.subTest(family=family['id'], variant=variant):
                        result = render_fragment(library, family['id'], context(family), variant=variant)
                        self.assertTrue(result)
                        if family['slots']:
                            for value in context(family)['values'].values():
                                self.assertIn(str(value), result)
            for recipe in library['recipes']:
                packets = {f: context(families[f]) for f in recipe['families']}
                self.assertTrue(compose_recipe(library, recipe['id'], packets))

    def test_default_scene_result_needs_no_key_transport_or_network(self):
        world = fixture()
        with patch.dict('os.environ', {}, clear=True), \
             patch('solo_provider.CapabilityBroker.dispatch', side_effect=AssertionError('provider forbidden')), \
             patch('openai_proposals.OpenAIProposalTransport.__call__', side_effect=AssertionError('HTTP forbidden')), \
             patch('socket.socket.connect', side_effect=AssertionError('network forbidden')):
            result = scene_action(world, 'try-gate')
            text = result['presentation']['text']
            self.assertEqual(result['presentation']['mode'], 'scripted')
            self.assertIn(result['outcome']['summary'], text)
            self.assertIn('gate remains closed', text)
            self.assertEqual(result['status'], 'completed_unsuccessfully')
            self.assertEqual(result['presentation']['render_usage'], {'provider_calls': 0, 'model_tokens': 0})
            self.assertEqual(world.s['elapsed_time']['seconds'], 5)
            self.assertTrue(player_drafts(world, 'pc')['drafts'])
            self.assertTrue(render_status(actor_id='pc', snapshot_id='s', status='declared_not_resolved')['text'])

    def test_old_receipt_is_identical_after_more_actions_restart_and_changed_hidden_state(self):
        world = fixture()
        first = scene_action(world, 'look-quay')['presentation']
        scene_action(world, 'enter-passage')
        restored = CoreWorld.load(world.save())
        restored.s['site_conditions']['quay-gate']['passable'] = True
        before = restored.save()
        self.assertEqual(render_receipt(restored, 'pc', 'execute:look-quay'), first)
        self.assertEqual(restored.save(), before)
        self.assertNotIn('desk lies ahead', first['text'])

    def test_wording_variants_do_not_rewrite_exact_committed_observations(self):
        world = fixture(); result = scene_action(world, 'look-quay')
        before = world.save()
        texts = {render_receipt(world, 'pc', 'execute:look-quay', variant_seed=i)['text'] for i in range(30)}
        self.assertGreater(len(texts), 1)
        for text in texts:
            self.assertIn(result['outcome']['summary'], text)
            self.assertIn(result['outcome']['observations'][0], text)
        self.assertEqual(world.save(), before)

    def test_actor_control_foreign_receipts_unknown_events_and_stale_scope_fail_closed(self):
        world = fixture(); scene_action(world, 'look-quay')
        apply(world, 'other', 'register_actor', actor_id='other', name='Other', species='human',
              player_controlled=True, instruction_ref='synthetic other')
        for actor, event in [('absent','execute:look-quay'),('other','execute:look-quay'),('pc','not-committed')]:
            with self.assertRaises(ValueError): render_receipt(world, actor, event)
        with self.assertRaises(ValueError):
            render_receipt(world, 'pc', 'execute:look-quay', scope=WorldScope('wrong','b','r',world.checksum()))
        scope = WorldScope(world.s['campaign_id'],'b','r',world.checksum())
        self.assertTrue(render_receipt(world, 'pc', 'execute:look-quay', scope=scope))
        scene_action(world, 'enter-passage')
        with self.assertRaises(ValueError): render_receipt(world, 'pc', 'execute:look-quay', scope=scope)

    def test_no_cross_actor_or_world_response_cache(self):
        left, right = fixture(), fixture()
        right.s['scene_rules']['places']['quay']['observe'] = 'Different received observation.'
        a = scene_action(left, 'look-quay')['presentation']
        b = scene_action(right, 'look-quay')['presentation']
        self.assertNotEqual(a['text'], b['text'])
        self.assertNotIn('Different received', render_receipt(left,'pc','execute:look-quay')['text'])

    def test_missing_or_invalid_library_retains_literal_receipt_without_paid_fallback(self):
        world = fixture()
        with patch('offline_responses._library', side_effect=OSError('missing authored bundle')), \
             patch('solo_provider.CapabilityBroker.dispatch', side_effect=AssertionError('no retry')):
            result = scene_action(world, 'try-gate')
        self.assertEqual(result['presentation']['mode'], 'literal_receipt')
        self.assertEqual(result['presentation']['text'], '\n'.join([result['outcome']['summary'], *result['outcome']['observations']]))
        self.assertIn('execute:try-gate', world.s['processed'])

    def test_rise_52_drafts_remain_editable_without_stock_or_permission_feasibility_filter(self):
        world = self.rise(); before = world.save()
        original = player_drafts(world,'founder')
        self.assertEqual(len(original['drafts']),52)
        self.assertEqual(world.save(),before)
        for row in original['drafts']:
            self.assertTrue(row['editable'] and row['requires_explicit_submission'])
            self.assertFalse(row['automatic_execution'])
        world.s['stocks']['founder-home']['timber']=0
        self.assertEqual(player_drafts(world,'founder'),original)
        self.assertTrue(original['custom_response']['editable'])

    def test_scene_drafts_keep_exact_authored_text_and_blocked_options(self):
        world=fixture(); before=world.save()
        drafts=player_drafts(world,'pc')['drafts']
        self.assertEqual(len(drafts),3)
        self.assertTrue(any(d['action_id']=='try-gate' for d in drafts))
        for draft in drafts:
            self.assertEqual(draft['text'],world.s['scene_rules']['actions'][draft['action_id']]['text'])
        self.assertEqual(world.save(),before)

    def test_settlement_receipts_do_not_mislabel_cumulative_time_as_action_time(self):
        world=self.rise()
        walk=settlement_action(world,'walk','founder','walk_clearing','explicit')
        inspected=settlement_action(world,'inspect','founder','inspect','explicit')
        self.assertEqual(world.s['settlement_receipts']['founder']['inspect']['elapsed_seconds'],300)
        self.assertNotIn('elapsed.action',inspected['presentation']['variants'])
        self.assertNotIn('elapsed.action',walk['presentation']['variants'])
        self.assertEqual(world.s['elapsed_time']['seconds'],300)

    def test_nonterminal_phase_text_replay_uses_received_boundary_not_live_progress(self):
        import test_process_runtime as process_cases
        case=self.helper(process_cases,'ProcessTests');case.camp()
        request=case.request('start',{'kind':'work','action_id':'build'})
        first=case.submit(request)
        self.assertIn('not complete',first['presentation']['text'])
        self.assertEqual(first['presentation']['mode'],'scripted')
        self.assertIn('elapsed.action',first['presentation']['variants'])  # Actual zero span is retained.
        case.phase('advance',{'seconds':600})
        case.world=case.host.load()
        before=case.world.save()
        self.assertEqual(case.submit(request),first)
        self.assertNotIn('600 worked',first['presentation']['text'])
        self.assertNotIn('600/3600',first['presentation']['text'])
        self.assertEqual(case.world.save(),before)

    def test_phase_observation_only_prints_new_knowledge_at_completion(self):
        import test_process_runtime as process_cases
        case=self.helper(process_cases,'ProcessTests')
        case.world=fixture();case.host.install(case.world)
        def step(command,details):
            return case.phase(command,details,actor='pc',process_id='observe')
        start=step('start',{'kind':'observation','action_id':'look-quay'})
        partial=step('advance',{'seconds':2})
        self.assertNotIn('passage and the closed gate',start['presentation']['text'])
        self.assertNotIn('passage and the closed gate',partial['presentation']['text'])
        final=step('advance',{'seconds':1})
        self.assertIn('You see the passage and the closed gate.',final['presentation']['text'])

    def test_speech_negation_braces_html_and_4096_characters_remain_attributed_testimony(self):
        import test_communication_runtime as communication_cases
        case=self.helper(communication_cases,'CommunicationTests')
        words='I do not accept. {stock} <script>literal</script>\n'+'x'*4046
        self.assertEqual(len(words),4096)
        result=case.act('speak',text=words)
        before=case.world.save()
        text=render_receipt(case.world,'oren','communication:'+result['request_id'])
        self.assertEqual(text['mode'],'scripted')
        self.assertIn(words,text['text']);self.assertIn('founder',text['text']);self.assertIn('testimony',text['text'].lower())
        self.assertEqual(text['format'],'plain_text')
        self.assertNotIn('elapsed.action',text['variants'])
        self.assertEqual(case.world.save(),before)
        case.world.s['knowledge']['oren'].pop(result['evidence_id'])
        with self.assertRaises(ValueError): render_receipt(case.world,'oren','communication:'+result['request_id'])

    def test_offer_words_do_not_accept_and_only_actual_fulfillment_is_presented(self):
        import test_communication_runtime as communication_cases
        case=self.helper(communication_cases,'CommunicationTests')
        offer=case.offer();stocks=copy.deepcopy(case.world.s['stocks'])
        speech=case.act('speak',actor='oren',text='I accept everything; transfer it all.')
        self.assertEqual(case.world.s['stocks'],stocks)
        self.assertNotIn('engine.offer',speech['presentation']['variants'])
        accepted=case.act('accept',{'offer_id':'offer-1','terms_digest':offer['terms_digest']},actor='oren')
        self.assertIn('fulfilled',accepted['presentation']['text'])
        self.assertEqual(case.world.s['stocks']['oren-home']['grain'],stocks['oren-home']['grain']+2)
        # Old offer is still offered in its original receipt; no current obligation lookup.
        prior=render_receipt(case.world,'founder','communication:'+offer['request_id'])
        self.assertIn('offered',prior['text']);self.assertNotIn('fulfilled',prior['text'])

    def test_library_schema_rejects_unsafe_templates_duplicate_fields_and_missing_anchor(self):
        library=load_library()
        for template in ('{receipt_text.__class__}','{receipt_text[0]}','{receipt_text!r}','{receipt_text:>20}'):
            invalid=copy.deepcopy(library)
            next(f for f in invalid['families'] if f['id']=='receipt.exact')['variants']=[template]
            with self.assertRaises(ValueError):validate_library(invalid)
        invalid=copy.deepcopy(library);invalid['recipes'][0]['required']=['elapsed.action']
        with self.assertRaises(ValueError):validate_library(invalid)
        with tempfile.TemporaryDirectory() as root:
            path=Path(root)/'duplicate.json';path.write_text('{"schema_version":1,"schema_version":1}')
            with self.assertRaises(ValueError):load_library(path)

    def test_composition_rejects_mixed_actors_snapshots_intentions_conflicts_and_missing_receipt(self):
        library=load_library();fs={f['id']:f for f in library['families']}
        def part(key,**kwargs):return {'family_id':key,'variant':0,'context':context(fs[key],**kwargs)}
        for parts in ([part('receipt.exact'),part('elapsed.action',actor='foreign')],
                      [part('receipt.exact'),part('elapsed.action',snapshot='foreign')],
                      [part('receipt.exact'),part('player.build')],
                      [part('player.build'),part('player.inspect')],
                      [part('elapsed.action')]):
            with self.assertRaises(ValueError):compose(library,parts)
        a,b=part('receipt.exact'),part('elapsed.action')
        b['context']['source_ref']=a['context']['source_ref'];b['context']['state']='unrecorded'
        with self.assertRaises(ValueError):compose(library,[a,b])

    def test_host_status_keeps_general_intentions_unresolved_and_hides_private_diagnoses(self):
        unresolved=render_status(actor_id='pc',snapshot_id='s',status='declared_not_resolved')
        self.assertIn('unresolved',unresolved['text'])
        generic=render_status(actor_id='pc',snapshot_id='s',status='private_stock_depleted')
        self.assertNotIn('stock',generic['text']);self.assertNotIn('depleted',generic['text'])


if __name__=='__main__':
    unittest.main()
