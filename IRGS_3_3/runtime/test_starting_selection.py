"""A playable Solo campaign is never an unreviewed empty world."""
import copy
import unittest

from campaign_library import initial_campaign
from core_world import CoreWorld
from historical_campaigns import historical_entry
from starting_selection import starting_options, initialize_player, options_for_world
from temporal_registry import available_entities


def historical_options():
    preview = historical_entry('hyw-1415')
    args = dict(scenario_id='hundred-years-war', entry_id='hyw-1415',
                snapshot_sha256=preview['snapshot_sha256'])
    return args, starting_options('military', **args)


class StartingSelectionTests(unittest.TestCase):
    def test_ast_preserves_canonical_character_and_requires_no_invented_stats(self):
        options = starting_options('ast')
        self.assertEqual(len(options['characters']), 37)
        self.assertEqual([row['id'] for row in options['characters'] if row['eligible']], ['AST-01'])
        original = initial_campaign('ast', 'AST-NEW')
        before = original.save()
        world = initialize_player(original, {'kind': 'existing', 'actor_id': 'AST-01'},
                                  selection_digest=options['selection_digest'])
        self.assertEqual(world.s['player_actor_ids'], ['AST-01'])
        self.assertEqual(world.s['actors']['AST-04']['name'], 'Abel')
        self.assertEqual(world.s['campaign_time']['day'], 2)
        self.assertEqual(world.s['actors']['AST-01']['current'], original.s['actors']['AST-01']['current'])
        self.assertEqual(original.save(), before)

    def test_all_generic_profiles_can_create_one_actual_player_without_free_resources(self):
        for profile in ('military', 'roman', 'fantasy', 'paf', 'shinobi', 'space'):
            with self.subTest(profile=profile):
                options = starting_options(profile)
                raw = initial_campaign(profile, 'NEW-' + profile)
                exact = 'My background.\nNo further promises or actions were declared.'
                world = initialize_player(raw, {'kind': 'new', 'name': 'Chosen name',
                    'species': 'human', 'background': exact}, selection_digest=options['selection_digest'])
                self.assertEqual(len(world.s['player_actor_ids']), 1)
                actor = world.s['player_actor_ids'][0]
                self.assertEqual(world.s['actors'][actor]['name'], 'Chosen name')
                self.assertEqual(world.s['evidence']['setup:background']['assertion'], exact)
                self.assertEqual(world.s['evidence']['setup:background']['status'], 'testimony')
                self.assertIn('setup:background', world.s['knowledge'][actor])
                for field in ('stocks', 'opening_stock', 'orders', 'capacities', 'activities', 'player_actions'):
                    self.assertFalse(world.s[field], field)
                self.assertEqual(world.s['campaign_time'], raw.s['campaign_time'])
                self.assertEqual(CoreWorld.load(world.save()).save(), world.save())
                self.assertFalse(raw.s['actors'])

    def test_historical_options_are_dated_and_separate_participation_from_playability(self):
        args, options = historical_options()
        self.assertEqual(options['source'], 'historical_template')
        self.assertEqual(options['as_of']['ordinal'], 2238109)
        self.assertEqual(len(options['characters']), 5)
        self.assertEqual(len(options['factions']), 5)
        factions = {row['id']: row for row in options['factions']}
        self.assertEqual(factions['HYW-ENGLAND']['participation'], 'participating')
        self.assertEqual(factions['HYW-BURGUNDY']['participation'], 'unknown')
        self.assertTrue(factions['HYW-ENGLAND']['exists'])
        self.assertFalse(factions['HYW-ENGLAND']['eligible'])
        self.assertTrue(options['entry_description']['summary'])
        for year in ('1337', '1429'):
            unavailable = starting_options('military', custom_year=year, **args)
            self.assertFalse(unavailable['available'])
        self.assertEqual(starting_options('military', custom_year='1415', **args)['selection_digest'], options['selection_digest'])

    def test_existing_historical_choice_controls_one_person_and_not_an_automatic_kingdom(self):
        args, options = historical_options()
        raw = initial_campaign('military', 'NEW-HYW', **args)
        world = initialize_player(raw, {'kind': 'existing', 'actor_id': 'HYW-HENRY-V'},
                                  selection_digest=options['selection_digest'])
        self.assertEqual(world.s['player_actor_ids'], ['HYW-HENRY-V'])
        self.assertEqual(world.s['starting_control']['powers'], ['declare_own_intent'])
        self.assertFalse(world.s['starting_control']['institutional_mandate_granted'])
        # New dated starts now receive only the sourced calendar checkpoint;
        # no historical briefing, operational scene or political news is seeded.
        self.assertEqual(set(world.s['knowledge']['HYW-HENRY-V']), {'setup:civil-date'})
        self.assertFalse(world.s['orders'])
        self.assertFalse(world.s['stocks'])
        self.assertEqual(world.s['historical_start'], raw.s['historical_start'])

    def test_missing_invalid_stale_and_ineligible_choices_are_rejected_without_mutation(self):
        args, options = historical_options()
        raw = initial_campaign('military', 'BAD-HYW', **args)
        before = raw.save()
        for character, signature in (
            (None, options['selection_digest']),
            ({'kind': 'existing', 'actor_id': 'HYW-ENGLAND'}, options['selection_digest']),
            ({'kind': 'existing', 'actor_id': 'not-present'}, options['selection_digest']),
            ({'kind': 'new', 'name': '', 'species': 'human'}, options['selection_digest']),
            ({'kind': 'new', 'name': 'Valid', 'species': 'human'}, '0' * 64),
            ({'kind': 'new', 'name': 'Valid', 'species': 'human'}, None)):
            with self.subTest(character=character), self.assertRaises(ValueError):
                initialize_player(raw, character, selection_digest=signature)
            self.assertEqual(raw.save(), before)

    def test_review_digest_is_stable_across_new_campaign_scopes_and_invalidates_changed_policy(self):
        first = initial_campaign('ast', 'FIRST')
        second = initial_campaign('ast', 'SECOND')
        self.assertEqual(options_for_world(first)['selection_digest'], options_for_world(second)['selection_digest'])
        old = options_for_world(first)['selection_digest']
        first.s['entity_registry']['eligibility']['individual:AST-01']['versions'][-1]['reason'] = 'Changed authored policy'
        with self.assertRaises(ValueError):
            initialize_player(first, {'kind': 'existing', 'actor_id': 'AST-01'}, selection_digest=old)

    def test_live_availability_never_reloads_a_historical_opening(self):
        args, options = historical_options()
        world = initialize_player(initial_campaign('military', 'DIVERGED', **args),
            {'kind': 'existing', 'actor_id': 'HYW-HENRY-V'}, selection_digest=options['selection_digest'])
        opening = copy.deepcopy(world.s['historical_start'])
        world.apply('simulation-dissolution', world.s['clock'] + 1, 'transition_entity',
                    campaign_id='DIVERGED', source_ref='explicit-simulation-outcome',
                    effective_at=world.s['entity_registry']['as_of'], entity_id='HYW-FRANCE', exists=False)
        loaded = CoreWorld.load(world.save())
        self.assertNotIn('HYW-FRANCE', {row['id'] for row in available_entities(loaded.s['entity_registry'])['factions']})
        self.assertEqual(loaded.s['historical_start'], opening)
        self.assertIn('HYW-FRANCE', {row['id'] for row in starting_options('military', **args)['factions']})

    def test_faction_choice_requires_a_permitted_representative_and_creates_no_mandate(self):
        args, _ = historical_options()
        raw = initial_campaign('military', 'FACTION-SCENARIO', **args)
        policy = raw.s['entity_registry']['eligibility']['individual:HYW-ENGLAND']['versions'][-1]
        policy.update(eligible=True, reason='Explicit authored scenario fixture',
                      control={'mode': 'institutional', 'actor_ids': ['HYW-HENRY-V'],
                               'powers': ['declare_own_intent']})
        options = options_for_world(raw)
        before = raw.save()
        with self.assertRaises(ValueError):
            initialize_player(raw, {'kind': 'faction', 'entity_id': 'HYW-ENGLAND',
                'actor_id': 'HYW-CHARLES-VI'}, selection_digest=options['selection_digest'])
        self.assertEqual(raw.save(), before)
        world = initialize_player(raw, {'kind': 'faction', 'entity_id': 'HYW-ENGLAND',
            'actor_id': 'HYW-HENRY-V'}, selection_digest=options['selection_digest'])
        self.assertEqual(world.s['player_actor_ids'], ['HYW-HENRY-V'])
        self.assertEqual(world.s['starting_control']['entity_id'], 'HYW-ENGLAND')
        self.assertFalse(world.s['starting_control']['institutional_mandate_granted'])
        self.assertFalse(world.s['orders'])
        self.assertFalse(world.s['stocks'])

    def test_shared_faction_lifecycle_runs_through_all_seven_profile_backends(self):
        for profile in ('ast', 'military', 'roman', 'fantasy', 'paf', 'shinobi', 'space'):
            with self.subTest(profile=profile):
                options = starting_options(profile)
                character = ({'kind': 'existing', 'actor_id': 'AST-01'} if profile == 'ast' else
                             {'kind': 'new', 'name': 'Profile representative', 'species': 'human'})
                world = initialize_player(initial_campaign(profile, 'CROSS-' + profile), character,
                                          selection_digest=options['selection_digest'])
                actor = world.s['player_actor_ids'][0]
                point = world.s['entity_registry']['as_of']
                campaign_time = copy.deepcopy(world.s['campaign_time'])
                operations = [
                    ('register_entity', {'entity_id': 'test-conflict', 'kind': 'conflict', 'identity': {'name': 'Test conflict'}}),
                    ('register_entity', {'entity_id': 'test-polity', 'kind': 'faction', 'identity': {'name': 'Test polity'}}),
                    ('transition_entity', {'entity_id': 'test-polity', 'identity': {'name': 'Renamed test polity'}}),
                    ('record_entity_relation', {'relation_id': 'test-participation', 'from_id': 'test-polity',
                         'to_id': 'test-conflict', 'relation_type': 'participation', 'status': 'active'}),
                    ('record_entity_eligibility', {'entity_id': 'test-polity', 'scenario_id': 'individual',
                         'eligible': True, 'reason': 'Explicit cross-profile test policy',
                         'control': {'mode': 'institutional', 'actor_ids': [actor], 'powers': ['declare_own_intent']}}),
                    ('select_entity_control', {'entity_id': 'test-polity', 'scenario_id': 'individual',
                         'actor_id': actor, 'instruction_ref': 'explicit-fixture-selection'}),
                    ('transition_entity', {'entity_id': 'test-polity', 'exists': False}),
                ]
                for index, (op, params) in enumerate(operations):
                    event_id, at = 'cross-entity-' + str(index), world.s['clock'] + 1
                    args = {'campaign_id': world.s['campaign_id'], 'effective_at': point,
                            'source_ref': 'synthetic-cross-profile-fixture', **params}
                    self.assertTrue(world.apply(event_id, at, op, **args))
                    before = world.save()
                    self.assertFalse(world.apply(event_id, at, op, **args))
                    self.assertEqual(world.save(), before)
                    world = CoreWorld.load(world.save())
                self.assertNotIn('test-polity', {row['id'] for row in available_entities(world.s['entity_registry'])['factions']})
                self.assertEqual(world.s['player_actor_ids'], [actor])
                self.assertFalse(world.s['starting_control']['institutional_mandate_granted'])
                self.assertEqual(world.s['campaign_time'], campaign_time)


if __name__ == '__main__':
    unittest.main()
