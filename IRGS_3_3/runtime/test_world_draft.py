"""Data-only draft review delegates exclusively to the actual Rise initializer."""
import copy
import unittest
from test_settlement import choices
import world_draft as api


class WorldDraftTests(unittest.TestCase):
    def draft(self):
        return {'schema_version':api.SCHEMA_VERSION,'draft_id':'synthetic-world','classification':'fictional',
                'profile_id':'rise-r00','choices':choices()}

    def test_preview_and_explicit_initialization_match_existing_review(self):
        draft=self.draft();before=copy.deepcopy(draft);review=api.validate(draft)
        self.assertEqual(draft,before);self.assertFalse(review['committed'])
        with self.assertRaises(ValueError):api.initialize(draft,draft_digest=review['draft_digest'],
            review_digest=review['review_digest'],campaign_id='draft-test',explicitly_accepted=False)
        world=api.initialize(draft,draft_digest=review['draft_digest'],review_digest=review['review_digest'],
            campaign_id='draft-test',explicitly_accepted=True)
        self.assertEqual(world.s['binding']['campaign_profile'],'rise')
        self.assertEqual(world.s['player_actor_ids'],['founder'])
        self.assertEqual(draft,before)

    def test_invalid_fields_and_stale_review_are_rejected(self):
        draft=self.draft();review=api.validate(draft);draft['choices']['supplies']='stocked'
        with self.assertRaises(ValueError):api.initialize(draft,draft_digest=review['draft_digest'],
            review_digest=review['review_digest'],campaign_id='draft-test',explicitly_accepted=True)
        for key,value in [('script','run'),('classification','historical'),('profile_id','unknown')]:
            bad=self.draft();bad[key]=value
            with self.assertRaises(ValueError):api.validate(bad)
            self.assertEqual(api.inspect(bad)['status'],'invalid')
            self.assertFalse(api.inspect(bad)['committed'])

    def test_reviewed_mixed_quay_uses_actual_selected_snapshot_and_opening(self):
        from historical_campaigns import historical_entry
        from communication_contract import actor_view
        from shared_runtime import capabilities, prepare_intent, execute_intent
        from runtime_contracts import WorldScope
        from test_solo_provider import AtomicTestHost
        import tempfile
        draft={'schema_version':api.SCHEMA_VERSION,'draft_id':'quay','classification':'mixed',
               'profile_id':'historical-quay','choices':{'snapshot_sha256':historical_entry('hyw-1415')['snapshot_sha256'],
                 'character':{'kind':'new','name':'Synthetic courier','species':'human','opening_id':'quay-contact-v1'}}}
        before=copy.deepcopy(draft);review=api.validate(draft);self.assertEqual(draft,before)
        world=api.initialize(draft,draft_digest=review['draft_digest'],review_digest=review['review_digest'],
                             campaign_id='draft-quay',explicitly_accepted=True)
        actor=world.s['player_actor_ids'][0]
        self.assertEqual(world.s['gameplay_started']['authored_opening']['id'],'quay-contact-v1')
        self.assertEqual(world.s['evidence']['setup:civil-date']['source_ref'],world.s['campaign_time']['civil']['source_ref'])
        self.assertIsNone(world.s['campaign_time']['civil']['time'])
        self.assertEqual(actor_view(world,actor,branch_id='branch-1',restore_id='restore-1')['channels'][0]['participants'][0]['actor_id'],'FICTIONAL-QUAY-CONTACT')
        import json
        cap=next(c for c in capabilities(world,actor) if json.loads(c.action_json).get('action_id')=='look-quay')
        request=prepare_intent(world,request_id='observe',actor_id=actor,intention='Look around.',capability_id=cap.capability_id,
                               branch_id='branch-1',restore_id='restore-1')
        with tempfile.TemporaryDirectory() as temp:
            host=AtomicTestHost(temp,world);scope=WorldScope(world.s['campaign_id'],'branch-1','restore-1',world.checksum())
            result=execute_intent(world,request,current_scope=scope,persist=host.persist,explicitly_accepted=True)
            self.assertEqual(result['status'],'completed_successfully');self.assertEqual(world.s['elapsed_time']['seconds'],20)
            saved=host.load();self.assertEqual(saved.s,world.s)
        draft['choices']['snapshot_sha256']='0'*64
        self.assertEqual(api.inspect(draft)['status'],'invalid')

    def test_disposable_preview_is_scoped_and_does_not_publish_or_mutate_draft(self):
        from historical_campaigns import historical_entry
        rise=self.draft()
        quay={'schema_version':api.SCHEMA_VERSION,'draft_id':'quay-preview','classification':'mixed',
              'profile_id':'historical-quay','choices':{'snapshot_sha256':historical_entry('hyw-1415')['snapshot_sha256'],
                'character':{'kind':'new','name':'Synthetic courier','species':'human','opening_id':'quay-contact-v1'}}}
        def keys(value):
            if isinstance(value,dict):
                return set(value) | set().union(*(keys(v) for v in value.values()))
            if isinstance(value,list):return set().union(*(keys(v) for v in value))
            return set()
        for draft in (rise,quay):
            with self.subTest(profile=draft['profile_id']):
                original=copy.deepcopy(draft);preview=api.preview_initialization(draft)
                self.assertEqual(draft,original);self.assertEqual(preview['status'],'preview_only')
                self.assertFalse(preview['committed']);self.assertFalse(preview['preview_identities_reusable'])
                self.assertTrue(preview['requires_explicit_acceptance'])
                self.assertTrue({'state','stocks','historical_start','entity_registry','params_digest'}.isdisjoint(keys(preview['actor_view'])))
                selected=api.validate(draft)
                actual=api.initialize(draft,draft_digest=selected['draft_digest'],review_digest=selected['review_digest'],
                                      campaign_id='real-synthetic-'+draft['profile_id'],explicitly_accepted=True)
                if draft['profile_id']=='rise-r00':
                    self.assertEqual(actual.s['clock'],0)
                if draft['profile_id']=='historical-quay':
                    self.assertNotEqual(preview['actor_view']['actor_id'],actual.s['player_actor_ids'][0])


if __name__=='__main__':unittest.main()
