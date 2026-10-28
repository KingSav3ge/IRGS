"""Reviewed Rise initialization and real local speech through the shared contract."""
import copy
import tempfile
import unittest
from unittest.mock import patch

import communication_contract as communication
from core_world import CoreWorld
from runtime_contracts import WorldScope
from settlement_runtime import execute
from settlement_setup import initialize, preview, COMMUNICATION_SOURCE
from test_settlement import choices
from test_solo_provider import AtomicTestHost


class RiseOrdinaryCommunicationTests(unittest.TestCase):
    def create(self, **changes):
        selection = choices(); selection.update(changes)
        review = preview(selection)
        world = initialize(selection, review['review_digest'], 'ordinary-rise-communication')
        return world, review

    def view(self, world):
        return communication.actor_view(world, 'founder', branch_id='branch-1', restore_id='restore-1')

    def request(self, world, recipient='oren', key='speech'):
        return communication.prepare(world, request_id=key, actor='founder', recipient=recipient,
            channel_id='commons-local', command='speak', details={}, intention='I would like to ask about the clearing.',
            source_ref='explicit-player-speech', branch_id='branch-1', restore_id='restore-1')

    def test_reviewed_start_receives_only_disclosed_introductions_and_no_private_offer(self):
        world, review = self.create(company='two_households')
        self.assertIn('no response, consent or transfer is automatic', review['neighbors'])
        self.assertEqual(review['communication_setup']['version'], 'irgs-rise-local-introductions-1')
        before = world.save(); view = self.view(world)
        self.assertEqual(world.save(), before)
        self.assertEqual([p['actor_id'] for p in view['channels'][0]['participants']], ['elin', 'oren'])
        self.assertTrue(all(p['supported_commands'] == ['speak'] for p in view['channels'][0]['participants']))
        sources = {r['originator']: r for r in view['received_sources']['records']}
        for speaker in ('elin', 'oren'):
            self.assertEqual(sources[speaker]['status'], 'testimony')
            self.assertEqual(sources[speaker]['source_ref'], COMMUNICATION_SOURCE)
        self.assertEqual(view['offers'], [])
        self.assertNotIn('mira', [p['actor_id'] for p in view['channels'][0]['participants']])
        with self.assertRaises(communication.CommunicationUnavailable): self.request(world, 'mira')
        self.assertEqual(world.save(), before)

    def test_actual_speech_requires_acceptance_and_replays_after_reload_once(self):
        world, _ = self.create(); before = world.save(); request = self.request(world)
        self.assertEqual(world.save(), before)
        stocks = copy.deepcopy(world.s['stocks']); elapsed = copy.deepcopy(world.s['elapsed_time'])
        with tempfile.TemporaryDirectory() as directory:
            host = AtomicTestHost(directory, world)
            scope = WorldScope(world.s['campaign_id'], 'branch-1', 'restore-1', world.checksum())
            with self.assertRaises(communication.CommunicationUnavailable):
                communication.execute(world, request, current_scope=scope, persist=host.persist, explicitly_accepted=False)
            self.assertEqual(world.save(), before)
            result = communication.execute(world, request, current_scope=scope, persist=host.persist, explicitly_accepted=True)
            self.assertEqual(result['truth_status'], 'testimony')
            self.assertEqual(result['utterance'], request.intention)
            self.assertEqual(world.s['stocks'], stocks); self.assertEqual(world.s['elapsed_time'], elapsed)
            loaded = host.load(); saved = loaded.save()
            again = communication.execute(loaded, request, current_scope=WorldScope(
                loaded.s['campaign_id'], 'branch-1', 'restore-1', loaded.checksum()),
                persist=host.persist, explicitly_accepted=True)
            self.assertEqual(again, result); self.assertEqual(loaded.save(), saved); self.assertEqual(host.writes, 1)

    def test_actual_colocation_rechecked_after_founder_leaves(self):
        world, _ = self.create(); execute(world, 'walk', 'founder', 'walk_clearing', 'explicit walk')
        before = world.save(); request = self.request(world)
        with self.assertRaises(communication.CommunicationUnavailable):
            communication.execute(world, request, current_scope=WorldScope(world.s['campaign_id'], 'branch-1',
                'restore-1', world.checksum()), persist=lambda *args: self.fail('rejection must not save'),
                explicitly_accepted=True)
        self.assertEqual(world.save(), before)

    def test_changed_introduction_invalidates_prior_review(self):
        selection = choices(); review = preview(selection)
        with patch.dict('settlement_setup.INTRODUCTIONS', {'oren': 'Changed introduction.'}):
            with self.assertRaises(ValueError):
                initialize(selection, review['review_digest'], 'stale-reviewed-start')

    def test_legacy_saved_state_is_not_reseeded_by_read(self):
        world, _ = self.create(); state = copy.deepcopy(world.s)
        del state['communication_rules']
        for speaker in ('elin', 'oren'):
            key = 'setup:local-introduction:' + speaker
            del state['knowledge']['founder'][key]; del state['evidence'][key]
        old = CoreWorld(state=state); before = old.save()
        self.assertEqual(self.view(old)['channels'], [])
        self.assertEqual(old.save(), before)


if __name__ == '__main__': unittest.main()
