"""Selected travel through the public phase API and actual reviewed Rise setup."""
import copy
from dataclasses import replace
import tempfile
import unittest
from unittest.mock import patch

import phase_contract as api
from runtime_contracts import WorldScope
from settlement_setup import initialize, preview
from test_settlement import choices
from test_solo_provider import AtomicTestHost
from process_runtime import ProcessRequest
from settlement_runtime import execute as settlement_action
from irgs_reference import InvalidEvent


class TravelCapabilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        c = choices(); c['company'] = 'sibling'
        self.world = initialize(c, preview(c)['review_digest'], 'ordinary-travel')
        self.host = AtomicTestHost(self.temp.name, self.world); self.counter = 0
        for target in ('solo_provider.CapabilityBroker.dispatch', 'openai_proposals.OpenAIProposalTransport.__call__', 'socket.socket.connect'):
            guard = patch(target, side_effect=AssertionError('No provider or network')); guard.start(); self.addCleanup(guard.stop)

    def scope(self):
        return WorldScope(self.world.s['campaign_id'], 'branch-1', 'restore-1', self.world.checksum())

    def view(self):
        return api.actor_view(self.world, 'founder', branch_id='branch-1', restore_id='restore-1')

    def start(self, action='walk_clearing', parent='journey'):
        option = next(row for row in self.view()['start_options'] if row['kind']=='travel' and row['action_id']==action)
        self.counter += 1
        return api.prepare_start(self.world, actor='founder', capability_id=option['capability_id'],
            process_id=parent, phase_id='phase-'+str(self.counter), intention='I attempt '+action+'.',
            source_ref='explicit reviewed travel', branch_id='branch-1', restore_id='restore-1')

    def command(self, command, details=None):
        self.counter += 1
        return api.prepare_command(self.world, actor='founder', process_id='journey', phase_id='phase-'+str(self.counter),
            command=command, details=details or {}, intention='I request '+command+'.',
            source_ref='explicit reviewed travel', branch_id='branch-1', restore_id='restore-1')

    def execute(self, request, **overrides):
        args = {'current_scope': self.scope(), 'persist': self.host.persist, 'explicitly_accepted': True}
        args.update(overrides); return api.execute(self.world, request, **args)

    def test_selected_travel_uses_real_progress_pause_reload_arrival_and_original_retry(self):
        before = self.world.save(); options = self.view()['start_options']
        self.assertEqual({r['action_id'] for r in options if r['kind']=='travel'}, {'walk_clearing','walk_commons'})
        request = self.start(); self.assertEqual(self.world.save(), before)
        with self.assertRaises(api.PhaseUnavailable): self.execute(request, explicitly_accepted=False)
        with self.assertRaises(OSError): self.execute(request, persist=lambda *a: (_ for _ in ()).throw(OSError('save failed')))
        self.assertEqual(self.world.save(), before)
        start = self.execute(request); self.assertEqual(start['kind'], 'travel')
        self.assertNotIn('cancel', [row['command'] for row in start['supported_commands']])
        self.assertEqual(self.world.s['actors']['founder']['current']['location'], 'route:commons-clearing')
        self.assertEqual(self.world.s['actors']['rowan']['current']['location'], 'route:commons-clearing')
        self.assertEqual(self.world.s['stock_accounts']['founder-home']['site'], 'route:commons-clearing')
        stocks = copy.deepcopy(self.world.s['stocks'])
        self.execute(self.command('advance', {'seconds':100})); paused = self.execute(self.command('pause'))
        self.assertEqual(paused['worked_seconds'],100); self.assertNotIn('cancel', [x['command'] for x in paused['supported_commands']])
        with self.assertRaises(api.PhaseUnavailable): self.command('cancel')
        self.world = self.host.load(); self.execute(self.command('resume'))
        advance = self.command('advance', {'seconds':1000}); final = self.execute(advance)
        self.assertEqual((final['status'],final['elapsed_seconds'],final['elapsed_total']), ('completed',200,300))
        self.assertEqual(self.world.s['stocks'],stocks)
        self.assertEqual(self.world.s['stock_accounts']['founder-home']['site'],'clearing')
        self.assertEqual(self.world.s['actors']['rowan']['current']['location'],'clearing')
        self.assertIn('process-arrival:journey',self.world.s['settlement_receipts']['founder'])
        self.world = self.host.load(); saved = self.world.save(); writes = self.host.writes
        self.assertEqual(self.execute(ProcessRequest.from_json(advance.to_json())), final)
        self.assertEqual(self.world.save(),saved); self.assertEqual(self.host.writes,writes)
        with self.assertRaises(api.PhaseUnavailable):
            self.execute(advance,current_scope=replace(self.scope(),restore_id='restored-branch'))

    def test_actual_location_competing_claim_and_changed_rules_reject_atomically(self):
        bad = self.start('walk_commons'); before = self.world.save()
        with self.assertRaises(api.PhaseUnavailable): self.execute(bad)
        self.assertEqual(self.world.save(),before)
        self.execute(self.start()); before=self.world.save()
        with self.assertRaises(api.PhaseUnavailable): self.execute(self.start(parent='competing'))
        self.assertEqual(self.world.save(),before)
        with self.assertRaises(InvalidEvent):
            settlement_action(self.world,'second-walk','founder','walk_commons','explicit competing movement')
        self.assertEqual(self.world.save(),before)
        self.world.s['settlement_model']['travel_seconds'] += 1
        self.host.install(self.world); before=self.world.save()
        with self.assertRaises(api.PhaseUnavailable): self.execute(self.command('advance', {'seconds':1}))
        self.assertEqual(self.world.save(),before)

    def test_views_do_not_probe_private_location_and_reveal_no_internal_state(self):
        import json
        before=self.world.save(); view=self.view(); self.assertEqual(self.world.save(),before)
        selected=[r for r in view['start_options'] if r['kind']=='travel']
        self.assertTrue(all(r['availability']=='attemptable' for r in selected))
        for forbidden in ('state_digest','rule_digest','projects','stock_accounts','dependencies'):
            self.assertNotIn(forbidden,json.dumps(view))
        with self.assertRaises(api.PhaseUnavailable):
            api.actor_view(self.world,'oren',branch_id='branch-1',restore_id='restore-1')


if __name__ == '__main__': unittest.main()
