"""Real authored pack initialization and execution, isolated new worlds only."""
import copy
import unittest
from unittest.mock import patch

from campaign_library import initial_campaign
from historical_campaigns import historical_entry
from starting_selection import initialize_player, options_for_world
from scene_actions import execute_scene_action
from scene_setup import initialize_opening


class SceneSetupTests(unittest.TestCase):
    def base(self):
        preview = historical_entry('hyw-1415')
        return initial_campaign('military', 'synthetic-pack', scenario_id='hundred-years-war',
                                entry_id='hyw-1415', snapshot_sha256=preview['snapshot_sha256'])

    def create(self, *, opening='quay-delivery-v1', world=None, species='human'):
        world = world or self.base()
        options = options_for_world(world)
        character = {'kind': 'new', 'name': 'Synthetic courier', 'species': species}
        if opening is not None:
            character['opening_id'] = opening
        return initialize_player(world, character, selection_digest=options['selection_digest'],
                                 request_ref='explicit-synthetic-opening-review')

    def test_pack_is_reviewed_fiction_and_no_option_for_other_profile(self):
        options = options_for_world(self.base())
        self.assertEqual(options['playable_openings'][0]['id'], 'quay-delivery-v1')
        self.assertTrue(options['playable_openings'][0]['fictional'])
        self.assertEqual(options_for_world(initial_campaign('military', 'other'))['playable_openings'], [])

    def test_default_does_not_invent_a_scene_or_possessions(self):
        world = self.create(opening=None)
        self.assertEqual(world.s['stocks'], {})
        self.assertNotIn('scene_rules', world.s)
        self.assertNotIn('elapsed_time', world.s)

    def test_human_capitalization_is_accepted_without_rewriting_identity(self):
        for species in ('human', 'Human', 'HUMAN', 'hUmAn', ' Human '):
            with self.subTest(species=species):
                world = self.create(species=species)
                actor = world.s['player_actor_ids'][0]
                self.assertEqual(world.s['actors'][actor]['species'], species.strip())
                self.assertEqual(world.s['entity_registry']['entities'][actor]['versions'][-1]['identity']['category'], 'person')
                self.assertEqual(world.s['scene_rules']['actor_id'], actor)
                self.assertEqual(world.s['stocks'][actor]['sealed_dispatch'], 1)

    def test_actual_pack_arc_commits_movement_observation_failure_and_delivery(self):
        world = self.create()
        actor = world.s['player_actor_ids'][0]
        calendar = copy.deepcopy(world.s['campaign_time'])
        for key in ('look-quay', 'quay-shortcut', 'quay-passage', 'passage-desk', 'deliver-dispatch'):
            result = execute_scene_action(world, 'synthetic:' + key, actor,
                {'kind': 'scene_action', 'action_id': key}, 'explicit-synthetic-' + key)
            self.assertEqual(result['status'], 'completed_unsuccessfully' if key == 'quay-shortcut'
                             else 'completed_successfully')
        self.assertEqual(world.s['elapsed_time']['seconds'], 150)
        self.assertEqual(world.s['stocks'][actor]['sealed_dispatch'], 0)
        self.assertEqual(world.s['stocks']['clerk-tray']['sealed_dispatch'], 1)
        self.assertEqual(world.s['campaign_time'], calendar)
        self.assertFalse(world.s['historical_start']['automatic_future_history'])

    def test_scene_content_change_invalidates_old_review(self):
        import scene_setup
        world = self.base()
        old = options_for_world(world)
        content = scene_setup._pack()
        content['actions']['look-quay']['duration_seconds'] = 99
        with patch.object(scene_setup, '_pack', return_value=content):
            with self.assertRaises(ValueError):
                initialize_player(world, {'kind': 'new', 'name': 'Courier', 'species': 'human',
                    'opening_id': 'quay-delivery-v1'}, selection_digest=old['selection_digest'])
        self.assertEqual(world.s['clock'], 0)

    def test_loaded_campaign_uses_saved_rules_not_changed_pack(self):
        import scene_setup
        world = self.create()
        actor = world.s['player_actor_ids'][0]
        with patch.object(scene_setup, '_pack', side_effect=AssertionError('Do not reload a template')):
            result = execute_scene_action(world, 'new-look', actor,
                {'kind': 'scene_action', 'action_id': 'look-quay'}, 'explicit synthetic look')
        self.assertEqual(result['outcome']['elapsed_seconds'], 20)

    def test_initializer_cannot_insert_scene_after_continuing_play(self):
        world = self.create(opening=None)
        actor = world.s['player_actor_ids'][0]
        world.apply('play:declared', world.s['clock'] + 1, 'record_player_action',
            campaign_id=world.s['campaign_id'], source_ref='synthetic', instruction_ref='explicit',
            actor=actor, declaration='A continuing declaration')
        before = world.save()
        with self.assertRaises(ValueError):
            initialize_opening(world, {'kind': 'new', 'species': 'human', 'opening_id': 'quay-delivery-v1'},
                               actor, 'explicit')
        self.assertEqual(world.save(), before)


if __name__ == '__main__':
    unittest.main()
