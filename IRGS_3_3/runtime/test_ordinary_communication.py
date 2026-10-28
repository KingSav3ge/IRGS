"""Ordinary reviewed fictional start, actual communication and recovery."""
import copy
import tempfile
import unittest

import communication_contract as communication
from core_world import CoreWorld
from runtime_contracts import WorldScope
from scene_actions import execute_scene_action
from starting_selection import initialize_player, options_for_world
from test_start_readiness import raw
from test_solo_provider import AtomicTestHost


class OrdinaryCommunicationTests(unittest.TestCase):
    def create(self, opening='quay-contact-v1'):
        world = raw(campaign='ordinary-contact-test')
        options = options_for_world(world)
        character = {'kind': 'new', 'name': 'Synthetic courier', 'species': 'human',
                     'opening_id': opening}
        world = initialize_player(world, character, selection_digest=options['selection_digest'],
                                  request_ref='explicit reviewed synthetic creation')
        return world, world.s['player_actor_ids'][0], options

    def test_review_is_explicit_and_original_start_remains_without_contact(self):
        world, actor, options = self.create('quay-delivery-v1')
        self.assertNotIn('communication_rules', world.s)
        choice = next(x for x in options['playable_openings'] if x['id'] == 'quay-contact-v1')
        self.assertTrue(choice['fictional'])
        self.assertIn('fictional quay worker', choice['review'])
        self.assertIn('not established', choice['review'])
        self.assertEqual(communication.actor_view(world, actor, branch_id='b', restore_id='r')['channels'], [])

    def test_normal_creation_speech_replay_and_reload(self):
        world, actor, _ = self.create()
        before = world.save()
        view = communication.actor_view(world, actor, branch_id='branch-1', restore_id='restore-1')
        self.assertEqual(world.save(), before)
        channel = view['channels'][0]
        self.assertEqual(channel['channel_id'], 'quay-local')
        self.assertEqual([p['actor_id'] for p in channel['participants']], ['FICTIONAL-QUAY-CONTACT'])
        self.assertEqual(channel['participants'][0]['source_record_ids'], ['setup:contact-introduction'])
        self.assertEqual(channel['participants'][0]['supported_commands'], ['speak'])
        stocks = copy.deepcopy(world.s['stocks']); elapsed = copy.deepcopy(world.s['elapsed_time'])
        request = communication.prepare(world, request_id='normal-speech', actor=actor,
            recipient='FICTIONAL-QUAY-CONTACT', channel_id='quay-local', command='speak', details={},
            intention='I have a dispatch for the receiving desk.', source_ref='explicit player speech',
            branch_id='branch-1', restore_id='restore-1')
        self.assertEqual(world.save(), before)
        with tempfile.TemporaryDirectory() as directory:
            host = AtomicTestHost(directory, world)
            scope = WorldScope(world.s['campaign_id'], 'branch-1', 'restore-1', world.checksum())
            with self.assertRaises(communication.CommunicationUnavailable):
                communication.execute(world, request, current_scope=scope, persist=host.persist, explicitly_accepted=False)
            self.assertEqual(world.save(), before)
            result = communication.execute(world, request, current_scope=scope, persist=host.persist, explicitly_accepted=True)
            self.assertEqual(result['truth_status'], 'testimony')
            self.assertEqual(world.s['stocks'], stocks)
            self.assertEqual(world.s['elapsed_time'], elapsed)
            reloaded = host.load(); saved = reloaded.save()
            replay = communication.execute(reloaded, request, current_scope=WorldScope(
                reloaded.s['campaign_id'], 'branch-1', 'restore-1', reloaded.checksum()),
                persist=host.persist, explicitly_accepted=True)
            self.assertEqual(replay, result)
            self.assertEqual(reloaded.save(), saved)
            self.assertEqual(host.writes, 1)

    def test_departure_rejects_actual_speech_without_inventing_remote_contact(self):
        world, actor, _ = self.create()
        execute_scene_action(world, 'go-passage', actor,
            {'kind': 'scene_action', 'action_id': 'quay-passage'}, 'explicit movement')
        before = world.save()
        request = communication.prepare(world, request_id='remote', actor=actor,
            recipient='FICTIONAL-QUAY-CONTACT', channel_id='quay-local', command='speak', details={},
            intention='Can you hear me?', source_ref='explicit player speech', branch_id='b', restore_id='r')
        with self.assertRaises(communication.CommunicationUnavailable):
            communication.execute(world, request, current_scope=WorldScope(world.s['campaign_id'], 'b', 'r', world.checksum()),
                                  persist=lambda *args: self.fail('must not persist'), explicitly_accepted=True)
        self.assertEqual(world.save(), before)

    def test_changed_review_digest_rejected(self):
        world = raw(campaign='digest-test'); before = world.save()
        with self.assertRaises(ValueError):
            initialize_player(world, {'kind': 'new', 'name': 'Synthetic', 'species': 'human',
                'opening_id': 'quay-contact-v1'}, selection_digest='stale', request_ref='explicit')
        self.assertEqual(world.save(), before)


if __name__ == '__main__':
    unittest.main()
