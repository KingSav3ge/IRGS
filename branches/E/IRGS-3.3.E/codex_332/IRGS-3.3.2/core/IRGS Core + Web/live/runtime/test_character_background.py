"""Starting identity and career testimony cannot manufacture a career or family."""
import copy
import json
import unittest

from campaign_library import initial_campaign
from character_background import background_schema, validate_background
from core_world import CoreWorld
from historical_campaigns import historical_entry
from starting_selection import initialize_player, starting_options


def setup():
    preview = historical_entry('hyw-1415')
    args = {'scenario_id': 'hundred-years-war', 'entry_id': 'hyw-1415',
            'snapshot_sha256': preview['snapshot_sha256']}
    options = starting_options('military', **args)
    return initial_campaign('military', 'BACKGROUND-TEST', **args), options


class CharacterBackgroundTests(unittest.TestCase):
    def test_scottish_origin_and_seeking_english_service_remain_independent_testimony(self):
        raw, options = setup()
        fields = {'identity': {'nationality': 'Scottish', 'birthplace': 'Lochaber', 'culture': 'My own account'},
                  'life_path': {'family': 'A mother and father, as declared.\nNo siblings specified.',
                                'upbringing': 'Rural household', 'education': 'I seek further instruction.'},
                  'career': {'arrangement': 'mercenary', 'relationship_stage': 'seeking',
                             'organization_id': 'HYW-ENGLAND', 'aspiration': 'Apply for a paid contract.'}}
        char = {'kind': 'new', 'name': 'New person', 'species': 'human', **fields}
        before = raw.save()
        world = initialize_player(raw, char, selection_digest=options['selection_digest'])
        actor = world.s['player_actor_ids'][0]
        evidence = world.s['evidence']['setup:background-details']
        self.assertEqual(json.loads(evidence['assertion'])['details'], fields)
        self.assertEqual(evidence['status'], 'testimony')
        self.assertEqual(evidence['subject'], actor)
        self.assertIn('setup:background-details', world.s['knowledge'][actor])
        self.assertEqual(len(world.s['actors']), len(raw.s['actors']) + 1)
        for key in ('stocks', 'obligations', 'orders', 'capacities', 'activities', 'delegations'):
            self.assertFalse(world.s.get(key), key)
        self.assertFalse(world.s['actors'][actor]['current'])
        self.assertEqual(world.s['starting_control']['powers'], ['declare_own_intent'])
        self.assertFalse(world.s['starting_control']['institutional_mandate_granted'])
        self.assertEqual(world.s['campaign_time'], raw.s['campaign_time'])
        self.assertEqual(raw.save(), before)
        self.assertEqual(CoreWorld.load(world.save()).save(), world.save())

    def test_new_player_may_have_no_affiliation_or_career_information(self):
        raw, options = setup()
        world = initialize_player(raw, {'kind': 'new', 'name': 'Independent', 'species': 'human'},
                                  selection_digest=options['selection_digest'])
        self.assertNotIn('setup:background-details', world.s['evidence'])
        self.assertFalse(world.s['obligations'])

    def test_claimed_offer_or_employment_does_not_create_an_accepted_contract(self):
        for stage in ('offer_claimed', 'current_claimed', 'former', 'membership_claimed'):
            with self.subTest(stage=stage):
                raw, options = setup()
                world = initialize_player(raw, {'kind': 'new', 'name': 'Professional', 'species': 'human',
                    'career': {'arrangement': 'civilian', 'relationship_stage': stage,
                               'organization_id': 'HYW-FRANCE'}}, selection_digest=options['selection_digest'])
                self.assertFalse(world.s['obligations'])
                self.assertFalse(world.s['orders'])
                self.assertFalse(world.s['stocks'])

    def test_bad_fields_types_enums_and_nonexistent_organization_reject_atomically(self):
        raw, options = setup()
        before = raw.save()
        bad = [
            {'identity': {'wealth': '1000'}}, {'identity': {'nationality': 4}},
            {'life_path': {'family': 'x' * 2001}}, {'life_path': []},
            {'career': {'arrangement': 'automatic_knight'}},
            {'career': {'relationship_stage': 'accepted_without_a_contract'}},
            {'career': {'organization_id': 'not-in-this-world'}},
            {'career': {'organization_id': 'HYW-HENRY-V'}},
            {'unowned_starting_goods': ['armor']},
        ]
        for details in bad:
            with self.subTest(details=details), self.assertRaises(ValueError):
                initialize_player(raw, {'kind': 'new', 'name': 'Bad draft', 'species': 'human', **details},
                                  selection_digest=options['selection_digest'])
            self.assertEqual(raw.save(), before)

    def test_existing_historical_people_cannot_be_rewritten_by_new_character_background(self):
        raw, options = setup()
        before = raw.save()
        with self.assertRaises(ValueError):
            initialize_player(raw, {'kind': 'existing', 'actor_id': 'HYW-HENRY-V',
                                   'identity': {'nationality': 'Changed'}}, selection_digest=options['selection_digest'])
        self.assertEqual(raw.save(), before)

    def test_background_schema_and_returned_details_are_detached(self):
        raw, options = setup()
        schema = background_schema()
        schema['arrangements'].append('invented')
        self.assertNotIn('invented', background_schema()['arrangements'])
        fields = {'kind': 'new', 'identity': {'origin': 'Declared origin'}}
        result = validate_background(fields, options)
        result['identity']['origin'] = 'Changed outside'
        self.assertEqual(fields['identity']['origin'], 'Declared origin')

    def test_future_reference_is_pinned_without_becoming_an_event_or_actor_knowledge(self):
        raw, options = setup()
        world = initialize_player(raw, {'kind': 'new', 'name': 'Reader', 'species': 'human'},
                                  selection_digest=options['selection_digest'])
        plans = world.s['historical_planning']
        self.assertEqual(plans['storage'], 'saved_prospective_reference')
        self.assertFalse(plans['installed_schedule'])
        self.assertFalse(plans['execution_available'])
        self.assertFalse(plans['actual_occurrence_refs'])
        self.assertEqual(len(plans['plans']), 3)
        self.assertFalse(world.s['pending'])
        self.assertFalse(world.s['knowledge'])
        self.assertEqual(plans['campaign_id'], world.s['campaign_id'])
        self.assertTrue(all(p['window_relation'] == 'future' for p in plans['plans']))
        self.assertFalse(world.s['historical_start']['automatic_future_history'])


if __name__ == '__main__':
    unittest.main()
