"""Neutral content portability is separate from actual campaign mechanics."""
import copy
import hashlib
import io
import json
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

import response_depot
from response_depot import DEPOT, SOURCE_SHA256, draft_variants, render_exact, render_public_status
from routine_format import compose, compose_recipe, load_library, render_fragment, validate_library
from runtime_contracts import ActionCapability


class ResponseDepotTests(unittest.TestCase):
    def test_exact_catalog_bytes_counts_and_compatibility_bank_are_preserved(self):
        self.assertEqual(hashlib.sha256(DEPOT.read_bytes()).hexdigest(),SOURCE_SHA256)
        library=load_library(DEPOT)
        self.assertEqual(validate_library(library)['variants'],1000)
        self.assertEqual(len(library['families']),127)
        self.assertEqual(len(library['recipes']),32)
        for channel,count in [('system',750),('player_draft',250)]:
            self.assertEqual(sum(len(f['variants']) for f in library['families'] if f['channel']==channel),count)
        old=DEPOT.parent.parent/'engine_routine_v1.json'
        self.assertEqual(hashlib.sha256(old.read_bytes()).hexdigest(),
                         '7091a060fdde8aebd233a0ff68dba4480a04fcd7eea3630eb9bd73fa9490603e')

    def packet(self,family,label):
        return {'actor_id':'controlled-actor','snapshot_id':'synthetic-view','source_ref':family['id'],
            'source_kind':family['source_kind'],'state':family['state'],
            'values':{key:2 if kind=='integer' else label if kind=='label' else 'No consent. {literal}\nUnverified.'
                      for key,kind in family['slots'].items()}}

    def test_all_1000_variants_with_four_synthetic_theme_labels_and_no_dispatch(self):
        library=load_library(DEPOT)
        themes=['historical court','fantasy expedition','space station','modern investigation']
        with patch('solo_provider.CapabilityBroker.dispatch',side_effect=AssertionError('No provider')):
            for theme in themes:
                for family in library['families']:
                    packet=self.packet(family,theme)
                    for index,variant in enumerate(family['variants']):
                        result=render_fragment(library,family['id'],packet,variant=index)
                        self.assertEqual(result,variant.format_map(packet['values']))
                        for value in packet['values'].values():self.assertIn(str(value),result)

    def test_all_32_recipes_accept_full_and_required_only_contexts(self):
        library=load_library(DEPOT);families={f['id']:f for f in library['families']}
        for recipe in library['recipes']:
            for fields in (recipe['families'],recipe['required']):
                self.assertTrue(compose_recipe(library,recipe['id'],
                    {key:self.packet(families[key],'actor-known label') for key in fields}))

    def test_semantic_tags_remain_drafts_and_never_become_operation_ids(self):
        library=load_library(DEPOT)
        for family in library['families']:
            self.assertNotIn('operation_id',family)
            self.assertNotIn('capability_id',family)
            if family['channel']=='player_draft':
                self.assertEqual(family['state'],'draft')
                self.assertEqual(family['source_kind'],'player_request')
                self.assertIsInstance(family['intent_tag'],str)
            else:self.assertIsNone(family['intent_tag'])
        rows=[variant for f in library['families'] for variant in f['variants']]
        self.assertEqual(len({' '.join(v.lower().split()) for v in rows}),1000)

    def test_runtime_preserves_exact_text_negation_braces_newlines_and_original_elapsed(self):
        words='No transfer occurred. {do_not_evaluate}\nThe report is testimony, not verified.'
        for seed in range(16):
            result=render_exact('actor','source-receipt',words,elapsed_seconds=0,variant_seed=seed)
            self.assertIn(words,result['text'])
            self.assertEqual(result['mode'],'scripted')
            self.assertIn('elapsed.action',result['variants'])
            self.assertEqual(result['render_usage'],{'provider_calls':0,'model_tokens':0})

    def test_corrupted_source_retains_literal_text_without_provider_or_truncation(self):
        words='Not completed.\n'+'x'*70000
        self.assertEqual(render_exact('actor','s',words)['text'],words)
        self.assertEqual(render_exact('actor','s',words)['mode'],'literal_receipt')
        with tempfile.TemporaryDirectory() as root:
            path=Path(root)/'library.json';path.write_text('{}')
            response_depot._depot.cache_clear()
            self.addCleanup(response_depot._depot.cache_clear)
            with patch('response_depot.DEPOT',path),patch('socket.socket.connect',side_effect=AssertionError('No network')):
                result=render_exact('actor','s','Do not accept.')
                self.assertEqual(result['mode'],'literal_receipt');self.assertEqual(result['text'],'Do not accept.')

    def test_drafts_without_required_known_labels_remain_literal_authored_intentions(self):
        cap=ActionCapability('actual-cap','selected-handler','{}','Known option',('received-source',),
            'player.ask','{}','Original authored intention.')
        rows=draft_variants('actor','view',cap)
        self.assertEqual(len(rows),1);self.assertEqual(rows[0]['mode'],'literal_draft')
        self.assertEqual(rows[0]['text'],'Original authored intention.')
        self.assertIsNone(rows[0]['intent_tag']);self.assertFalse(rows[0]['automatic_execution'])

    def test_public_status_never_uses_a_private_diagnostic_to_select_words(self):
        private=render_public_status('actor','view','stock_secretly_empty')
        unavailable=render_public_status('actor','view','unavailable')
        self.assertEqual(private,unavailable)
        self.assertIn('unresolved',render_public_status('actor','view','declared_not_resolved')['text'])

    def test_invalid_tags_unsafe_placeholders_and_mixed_scopes_are_rejected(self):
        library=load_library(DEPOT)
        for field,value in [('intent_tag','execute_player_scene_action'),('state','walk_clearing')]:
            invalid=copy.deepcopy(library)
            family=next(f for f in invalid['families'] if f['id']=='player.travel')
            family[field]=value
            if field=='state':
                with self.assertRaises(ValueError):validate_library(invalid)
            else:
                # A syntactically valid tag still creates no operation binding.
                validate_library(invalid)
                self.assertNotIn('operation_id',family)
        invalid=copy.deepcopy(library);invalid['families'][0]['variants']=['{private.__class__}']
        with self.assertRaises(ValueError):validate_library(invalid)
        anchor=next(f for f in library['families'] if f['id']=='receipt.exact')
        elapsed=next(f for f in library['families'] if f['id']=='elapsed.action')
        left,right=self.packet(anchor,'known'),self.packet(elapsed,'known')
        right['snapshot_id']='other-restore'
        with self.assertRaises(ValueError):compose(library,[{'family_id':anchor['id'],'variant':0,'context':left},
            {'family_id':elapsed['id'],'variant':0,'context':right}])

    def test_intake_validates_the_exact_hashed_bytes_if_file_changes_during_read(self):
        original=DEPOT.read_bytes()
        changed=json.loads(original)
        changed['families'][0]['variants'][0]='Changed after the source hash check.'
        replaced=json.dumps(changed).encode()
        with tempfile.TemporaryDirectory() as root:
            path=Path(root)/'library.json';path.write_bytes(original)
            open_file=Path.open
            reads=[]
            def changing_open(selected,*args,**kwargs):
                if selected==path:
                    raw=original if not reads else replaced
                    reads.append(raw)
                    return io.BytesIO(raw)
                return open_file(selected,*args,**kwargs)
            response_depot._depot.cache_clear();self.addCleanup(response_depot._depot.cache_clear)
            with patch('response_depot.DEPOT',path),patch.object(Path,'open',changing_open):
                actual=response_depot._depot()
            self.assertEqual(len(reads),1)
            self.assertEqual(actual['families'][0]['variants'][0],json.loads(original)['families'][0]['variants'][0])


if __name__=='__main__':unittest.main()
