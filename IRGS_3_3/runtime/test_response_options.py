"""Explicit contextual drafts remain information, not combat resolution."""
import copy
import json
import unittest

from campaign_library import initial_campaign
from core_world import CoreWorld
from irgs_reference import InvalidEvent
from response_options import response_choices
from r9_runtime import observe


def fixture():
    world = initial_campaign('military', 'synthetic-response-prompt')
    for actor in ('player', 'other-player', 'npc'):
        world.apply('register:' + actor, world.s['clock'] + 1, 'register_actor',
                    campaign_id=world.s['campaign_id'], actor_id=actor, name=actor, species='human',
                    player_controlled=actor != 'npc', instruction_ref='explicit-synthetic-selection',
                    source_ref='synthetic-prompt-fixture')
    return world


def params(world, **changes):
    return {**{'campaign_id': world.s['campaign_id'], 'source_ref': 'PRIVATE_PROMPT_SOURCE',
               'prompt_id': 'encounter-one', 'recipient': 'player', 'title': 'A received question',
               'description': 'A messenger asks what you intend to do.', 'context_kind': 'dialogue',
               'choices': [{'id': 'clarify', 'label': 'Ask for clarification',
                            'text': 'I ask the messenger to clarify the request.'}]}, **changes}


def receive(world, event_id='receive:one', **changes):
    return world.apply(event_id, world.s['clock'] + 1, 'receive_response_prompt', **params(world, **changes))


class ResponsePromptTests(unittest.TestCase):
    def test_receipt_changes_information_only_and_cannot_resolve_a_choice(self):
        world = fixture()
        before = copy.deepcopy(world.s)
        receive(world)
        self.assertEqual(world.s['response_prompts']['encounter-one']['status'], 'received_prompt')
        for field in ('actors', 'stocks', 'opening_stock', 'orders', 'activities', 'campaign_time', 'player_actions'):
            self.assertEqual(world.s[field], before[field])
        prompt = response_choices(world.s, 'player')
        self.assertEqual(prompt['execution'], 'draft_only')
        self.assertTrue(prompt['own_response_allowed'])
        self.assertEqual(prompt['choices'], params(world)['choices'])
        self.assertNotIn('PRIVATE_', json.dumps(prompt))

    def test_only_explicit_received_context_creates_response_drafts(self):
        world = fixture()
        world.s['actors']['npc']['current']['private_combat'] = 'PRIVATE_COMBAT_PLAN'
        before = world.save()
        self.assertIsNone(response_choices(world.s, 'player'))
        self.assertEqual(world.save(), before)
        receive(world, context_kind='combat', choices=[], title='Received encounter',
                description='The character has received this encounter prompt.')
        choices = response_choices(world.s, 'player')['choices']
        self.assertEqual(len(choices), 5)
        self.assertEqual({choice['id'] for choice in choices},
                         {'attempt-strike', 'protect-myself', 'reposition', 'break-contact', 'speak'})
        self.assertTrue(all(choice['text'].startswith('I attempt') or choice['text'].startswith('I try') for choice in choices))
        self.assertNotIn('PRIVATE_', json.dumps(choices))

    def test_supplied_combat_choices_override_generic_drafts(self):
        world = fixture()
        choice = {'id': 'call', 'label': 'Call for assistance', 'text': 'I try to call for assistance.'}
        receive(world, context_kind='combat', choices=[choice])
        self.assertEqual(response_choices(world.s, 'player')['choices'], [choice])

    def test_risky_received_choice_is_not_filtered_into_a_guaranteed_winning_list(self):
        world = fixture()
        risky = {'id': 'reckless-charge', 'label': 'Charge across the exposed ground',
                 'text': 'I charge immediately across the exposed ground before checking what lies ahead.'}
        receive(world, context_kind='combat', choices=[risky])
        offered = response_choices(world.s, 'player')
        world.s['actors']['npc']['current']['private_opposition_strength'] = 'PRIVATE_OVERWHELMING_OPPOSITION'
        world.s['actors']['player']['current']['private_constraint'] = 'PRIVATE_NOT_AN_ELIGIBILITY_ORACLE'
        before = world.save()
        self.assertEqual(response_choices(world.s, 'player'), offered)
        self.assertEqual(offered['choices'], [risky])
        self.assertEqual(set(offered['choices'][0]), {'id', 'label', 'text'})
        self.assertEqual(offered['execution'], 'draft_only')
        self.assertNotIn('PRIVATE_', json.dumps(offered))
        self.assertEqual(world.save(), before)

    def test_noncombat_empty_choices_still_allow_own_response(self):
        world = fixture()
        receive(world, context_kind='negotiation', choices=[])
        prompt = response_choices(world.s, 'player')
        self.assertEqual(prompt['choices'], [])
        self.assertTrue(prompt['own_response_allowed'])

    def test_other_recipients_and_uncontrolled_characters_do_not_share_prompts(self):
        world = fixture()
        receive(world)
        receive(world, 'receive:other', prompt_id='other', recipient='other-player', title='PRIVATE_OTHER_TITLE')
        receive(world, 'receive:npc', prompt_id='npc', recipient='npc', title='PRIVATE_NPC_TITLE')
        self.assertEqual(response_choices(world.s, 'player')['prompt_id'], 'encounter-one')
        self.assertEqual(response_choices(world.s, 'other-player')['prompt_id'], 'other')
        self.assertIsNone(response_choices(world.s, 'npc'))
        self.assertIsNone(response_choices(world.s, 'missing'))
        self.assertIsNone(response_choices(world.s, None))
        world.s['player_actor_ids'].remove('player')
        self.assertIsNone(response_choices(world.s, 'player'))

    def test_latest_active_received_prompt_is_selected_without_mutation(self):
        world = fixture()
        receive(world)
        receive(world, 'receive:two', prompt_id='encounter-two')
        self.assertEqual(response_choices(world.s, 'player')['prompt_id'], 'encounter-two')
        world.s['response_prompts']['encounter-two']['active'] = False
        self.assertEqual(response_choices(world.s, 'player')['prompt_id'], 'encounter-one')
        world.s['response_prompts']['encounter-two']['active'] = True
        world.s['response_prompts']['encounter-two']['received_at'] = world.s['clock'] + 1
        before = world.save()
        self.assertEqual(response_choices(world.s, 'player')['prompt_id'], 'encounter-one')
        self.assertEqual(world.save(), before)

    def test_tied_latest_prompts_do_not_create_priority_from_ids(self):
        world = fixture()
        receive(world)
        receive(world, 'receive:two', prompt_id='encounter-two')
        world.s['response_prompts']['encounter-one']['received_at'] = world.s['clock']
        self.assertIsNone(response_choices(world.s, 'player'))

    def test_projection_and_input_are_detached_from_authoritative_records(self):
        world = fixture()
        incoming = params(world)
        world.apply('receive:one', world.s['clock'] + 1, 'receive_response_prompt', **incoming)
        incoming['choices'][0]['text'] = 'tampered input'
        projection = response_choices(world.s, 'player')
        projection['choices'][0]['text'] = 'tampered view'
        self.assertEqual(response_choices(world.s, 'player')['choices'][0]['text'],
                         'I ask the messenger to clarify the request.')

    def test_invalid_prompts_are_atomic_and_do_not_establish_world_facts(self):
        invalid = ({'recipient': 'missing'}, {'prompt_id': ''}, {'title': ' '},
                   {'description': 'x' * 4001}, {'context_kind': 'combat / automatic'},
                   {'choices': [{'id': 'bad', 'label': 'Bad', 'text': 'Words', 'effect': 'win'}]},
                   {'choices': [{'id': 'same', 'label': 'One', 'text': 'I try.'}] * 2},
                   {'choices': [{'id': str(i), 'label': 'Many', 'text': 'I try.'} for i in range(9)]},
                   {'choices': [{'id': 'empty', 'label': 'One', 'text': ''}]},
                   {'choices': [{'id': 'long', 'label': 'One', 'text': 'x' * 2001}]},
                   {'active': True}, {'source_ref': ''})
        for changes in invalid:
            with self.subTest(changes=changes):
                world = fixture()
                before = world.save()
                with self.assertRaises(InvalidEvent):
                    receive(world, **changes)
                self.assertEqual(world.save(), before)

    def test_duplicate_prompt_and_replayed_event_do_not_repeat_receipt(self):
        world = fixture()
        receive(world)
        accepted = copy.deepcopy(world.s['journal'][-1])
        world = CoreWorld.load(world.save())
        before = world.save()
        self.assertFalse(world.apply(accepted['id'], accepted['at'], accepted['op'], **accepted['params']))
        self.assertEqual(world.save(), before)
        with self.assertRaises(InvalidEvent):
            receive(world, 'new-event-same-prompt')
        self.assertEqual(world.save(), before)

    def test_prompt_receipt_has_observed_information_dependencies(self):
        world = fixture()
        event = {'id': 'receive:observed', 'at': world.s['clock'] + 1,
                 'op': 'receive_response_prompt', 'params': params(world)}
        certificate = observe(world.s, event)
        self.assertIn(('actors', 'player', '@exists'), certificate['reads'])
        self.assertTrue(any(path[0] == 'response_prompts' for path in certificate['writes']))
        self.assertFalse(any(path[0] in ('stocks', 'opening_stock', 'campaign_time')
                             for path in certificate['writes']))


if __name__ == '__main__':
    unittest.main()
