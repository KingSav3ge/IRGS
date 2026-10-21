"""Regression checks for immutable event ownership and layered replay."""
import copy
import unittest

from irgs_reference import InvalidEvent
from r9_runtime import frontier
from test_r7_integration import world, new_item
from test_r9_runtime import receiver, military


class PayloadOwnershipTests(unittest.TestCase):
    def enrolled(self):
        w = world()
        w.apply('authority', 0, 'authorize_mobilization', mandate='fixture', target=1)
        w.apply('enroll', 1, 'enroll', person='farmer-a')
        return w

    def test_direct_submission_detaches_caller_list(self):
        w = self.enrolled()
        people = ['farmer-a']
        w.apply('issue', 2, 'issue_kits', persons=people)
        before = w.save()
        people.append('farmer-b')
        self.assertEqual(w.save(), before)
        self.assertEqual(w.s['journal'][-1]['params']['persons'], ['farmer-a'])

    def test_frontier_submission_detaches_caller_list(self):
        w = self.enrolled()
        event = {'id': 'issue', 'at': 2, 'op': 'issue_kits',
                 'params': {'persons': ['farmer-a']}}
        self.assertEqual(frontier(w, [event])['committed'], ['issue'])
        before = w.save()
        event['params']['persons'].append('farmer-b')
        self.assertEqual(w.save(), before)
        self.assertEqual(w.s['r9']['requests']['issue']['original']['params']['persons'], ['farmer-a'])

    def test_scheduled_request_detaches_caller_list(self):
        w = self.enrolled()
        people = ['farmer-a']
        w.schedule('issue', 2, 'issue_kits', persons=people)
        before = w.save()
        people.append('farmer-b')
        self.assertEqual(w.save(), before)
        self.assertEqual(w.s['pending'][-1]['params']['persons'], ['farmer-a'])

    def test_native_submission_detaches_outer_payload(self):
        w = receiver()
        event = military()
        w.apply(event['id'], event['at'], event['op'], **event['params'])
        before = w.save()
        event['params']['persons'].append('farmer-b')
        self.assertEqual(w.save(), before)
        self.assertEqual(w.s['journal'][-1]['params']['persons'], ['farmer-a'])

    def test_altered_direct_replay_is_rejected_atomically(self):
        w = self.enrolled()
        w.apply('issue', 2, 'issue_kits', persons=['farmer-a'])
        before = w.save()
        with self.assertRaises(InvalidEvent):
            w.apply('issue', 2, 'issue_kits', persons=['farmer-a', 'farmer-b'])
        self.assertEqual(w.save(), before)

    def test_saved_journal_payload_tampering_is_rejected(self):
        w = self.enrolled()
        state = copy.deepcopy(w.s)
        state['journal'][-1]['params']['person'] = 'farmer-b'
        with self.assertRaises(AssertionError):
            type(w)(state=state)


class LayeredReplayTests(unittest.TestCase):
    def loss(self, w, quantity=1):
        return w.apply('wip-loss', 9, 'physical_loss', location='wip:A',
                       material='unfinished-shield', quantity=quantity,
                       cause_ref='fixture-fire', evidence_ref='fixture-inspection')

    def test_wip_loss_replay_does_not_repeat_reconciliation(self):
        w = world()
        new_item(w)
        self.assertTrue(self.loss(w))
        w = type(w).load(w.save())
        before = w.save()
        self.assertFalse(self.loss(w))
        self.assertEqual(w.save(), before)
        self.assertEqual(w.s['r7_intermediates']['A']['physical_qty'], 1)
        self.assertEqual(len(w.s['r7_intermediates']['A']['losses']), 1)

    def test_altered_wip_loss_replay_is_rejected_atomically(self):
        w = world()
        new_item(w)
        self.loss(w)
        before = w.save()
        with self.assertRaises(InvalidEvent):
            self.loss(w, quantity=2)
        self.assertEqual(w.save(), before)

    def test_confirmed_loss_commits_while_same_time_work_stays_unexecuted(self):
        from test_work_recovery import start
        from test_r7_integration import milestone_p
        from r9_runtime import frontier
        w=world();start(w)
        events=[{'id':'mile','at':9,'op':'record_work_milestone','params':milestone_p(8,9)},
                {'id':'fire','at':9,'op':'physical_loss','params':{'location':'farm','material':'seed','quantity':9,'cause_ref':'fire','evidence_ref':'measured'}}]
        result=frontier(w,events)
        self.assertIn('fire',result['committed']);self.assertIn('mile',result['deferred'])
        self.assertEqual(w.s['econ3']['losses']['seed'],9)
        self.assertNotIn('mile',w.s['processed'])
        self.assertEqual(w.s['econ3']['produced']['grain'],0)

    def test_inconsistent_combined_losses_roll_back_frontier(self):
        from r9_runtime import frontier
        w=world();new_item(w);before=w.save()
        events=[{'id':str(n),'at':9,'op':'physical_loss','params':{'location':'wip:A','material':'unfinished-shield','quantity':2,'cause_ref':'test','evidence_ref':'test'}} for n in range(2)]
        with self.assertRaises(InvalidEvent):frontier(w,events)
        self.assertEqual(w.save(),before)

if __name__=='__main__':unittest.main()


