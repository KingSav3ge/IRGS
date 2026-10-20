import copy,json,unittest
from pathlib import Path
from campaign_library import catalog,initial_campaign,presentation_binding
from core_world import CoreWorld
from content_library import lookup
from r9_runtime import frontier,observe,conflicts,grant,resolve
from irgs_reference import InvalidEvent

def event(w,eid,op,at=None,**params):
    return {'id':eid,'op':op,'at':w.s['clock']+1 if at is None else at,
            'params':{'campaign_id':w.s['campaign_id'],'source_ref':'explicit synthetic test',**params}}
def apply(w,e):return w.apply(e['id'],e['at'],e['op'],**e['params'])
def setup(profile):
    w=initial_campaign(profile)
    for actor in ('owner','delegate','worker'):
        apply(w,event(w,'register-'+actor,'register_actor',actor_id=actor,name=actor,species='human'))
    return w

class SuiteTests(unittest.TestCase):
    def test_legacy_names_and_canonical_operations_have_same_domain_effects(self):
        from core_world import ALIASES
        base=setup('military')
        apply(base,event(base,'player','register_actor',actor_id='player',name='Player',species='human',player_controlled=True,instruction_ref='explicit player selection'))
        apply(base,event(base,'e','record_evidence',evidence_id='established',subject='worker',assertion='At the yard',status='established'))
        apply(base,event(base,'stock','establish_stock',location='store',material='grain',quantity=10,inventory_evidence_ref='count'))
        samples={
            'record_evidence':dict(evidence_id='e2',subject='worker',assertion='A report',status='testimony'),
            'receive_evidence':dict(evidence_id='established',recipient='owner'),
            'record_player_action':dict(actor='player',declaration='I look around',instruction_ref='player declaration'),
            'set_scene':dict(day=1,time=None,precision='unresolved',description='A new scene',instruction_ref='player scene selection'),
            'confirm_character_field':dict(subject='worker',field='location',value='yard',evidence_id='established',authority_ref='source observer'),
            'establish_stock':dict(location='yard',material='timber',quantity=3,inventory_evidence_ref='count'),
            'transfer_stock':{'from':'store','to':'yard','material':'grain','quantity':2,'authority_ref':'owner'},
            'record_obligation':dict(obligation_id='o',subject='worker',description='An offer',status='offered'),
            'record_design':dict(design_id='draft',name='A draft'),
            'receive_order':dict(order_id='o',recipient='worker',authority_ref='owner',content='Example instruction')}
        for alias,canonical in ALIASES.items():
            with self.subTest(operation=canonical):
                a=CoreWorld(state=base.s);b=CoreWorld(state=base.s)
                apply(a,event(a,'new',canonical,**samples[canonical]));apply(b,event(b,'new',alias,**samples[canonical]))
                domain=lambda s:{k:v for k,v in s.items() if k not in ('journal','processed')}
                self.assertEqual(domain(a.s),domain(b.s))
    def test_completed_bookings_share_one_capacity_and_actor_ledger(self):
        w=setup('military');apply(w,event(w,'cap','record_capacity',capacity_id='site',site='yard',quantity=1,unit='concurrent_people'))
        now=w.s['clock']+1
        apply(w,event(w,'booking','commit_activity',activity_id='work',actors=['worker'],site='yard',capacity_id='site',start=now,end=now+4,role='craft',authority_ref='owner'))
        self.assertEqual(w.s['activities']['work']['actors'],['worker'])
        before=w.save()
        with self.assertRaises(InvalidEvent):apply(w,event(w,'conflict','commit_activity',activity_id='second',actors=['owner'],site='yard',capacity_id='site',start=now+1,end=now+3,role='guard',authority_ref='owner'))
        self.assertEqual(w.save(),before)
    def test_genres_are_six_and_ast_is_campaign_library(self):
        data=catalog();self.assertEqual({x['id'] for x in data['genre_engines']},{'military','roman','fantasy','paf','shinobi','space'})
        self.assertEqual(next(x for x in data['content_libraries'] if x['id']=='ast')['type'],'campaign_library')
    def test_all_profiles_share_the_same_kernel(self):
        for profile in catalog()['campaign_profiles']:
            w=initial_campaign(profile['id']);self.assertIs(type(w),CoreWorld)
            self.assertEqual(w.s['binding']['genre_id'],profile['genre_id'])
            self.assertEqual(w.s['stocks'],{});self.assertFalse(w.s['journal'])
    def test_each_genre_can_establish_an_actor_and_evidence(self):
        for genre in ('military','roman','fantasy','paf','shinobi','space'):
            w=setup(genre)
            apply(w,event(w,'report','record_evidence',evidence_id='report',subject='worker',assertion='A local observation',status='testimony'))
            self.assertEqual(w.s['knowledge'],{});self.assertEqual(w.s['evidence']['report']['status'],'testimony')
    def test_legacy_ast_save_load_does_not_rewrite(self):
        path=Path(__file__).resolve().parents[2]/'IRGS_Core_Unification_CMRR_R9/live/ast_state.json'
        if not path.exists():self.skipTest('historical local save not packaged')
        raw=path.read_text(encoding='utf-8');s=json.loads(raw);w=CoreWorld(state=s)
        self.assertEqual(w.s,s);self.assertEqual(presentation_binding(w.s)['campaign_profile'],'ast')
        self.assertEqual(path.read_text(encoding='utf-8'),raw)
    def test_content_lookup_preserves_source_status_and_state(self):
        w=initial_campaign('ast');before=w.save();result=lookup('shared','',5)
        self.assertFalse(result['lookup_creates_state']);self.assertFalse(result['numerical_models_adopted'])
        self.assertTrue(result['results']);self.assertEqual(w.save(),before)
    def test_deprecated_horse_lookup_returns_canonical_identity(self):
        result=lookup('ast','Able',1)
        self.assertEqual(result['results'][0]['identity']['name'],'Abel')
    def test_unknown_native_numeric_effect_is_refused(self):
        w=setup('shinobi');before=w.save()
        with self.assertRaises(InvalidEvent):apply(w,event(w,'unknown','convert_legacy_million_unit_chakra',amount=999999))
        self.assertEqual(w.save(),before)
    def test_actor_registration_caller_ownership(self):
        w=setup('military');e=event(w,'report','record_evidence',evidence_id='e',subject='worker',assertion='Observed',status='established')
        apply(w,e);e['params']['assertion']='changed'
        self.assertEqual(w.s['journal'][-1]['params']['assertion'],'Observed')
    def test_able_not_created_as_second_horse(self):
        w=initial_campaign('ast')
        with self.assertRaises(InvalidEvent):apply(w,event(w,'wrong','register_actor',actor_id='new-horse',name='Able',species='horse'))
    def test_common_site_capacity_detects_competing_institutions(self):
        w=setup('military');apply(w,event(w,'cap','record_capacity',capacity_id='site',site='yard',quantity=1,unit='concurrent_people'))
        now=w.s['clock']+1
        a=event(w,'housework','commit_activity',at=now,activity_id='house',actors=['owner'],site='yard',capacity_id='site',start=now,end=now+4,role='household',authority_ref='fixture')
        b=event(w,'armywork','commit_activity',at=now,activity_id='army',actors=['worker'],site='yard',capacity_id='site',start=now,end=now+4,role='military',authority_ref='fixture')
        self.assertTrue(conflicts(observe(w.s,a),observe(w.s,b)))
        self.assertEqual(set(frontier(w,[a,b])['deferred']),{'housework','armywork'})
    def test_military_equipment_reads_received_directive_and_preserves_stock(self):
        w=setup('military');apply(w,event(w,'stock','establish_stock',location='depot',material='kit',quantity=3,inventory_evidence_ref='count'))
        apply(w,event(w,'order','receive_order',order_id='issue',recipient='owner',authority_ref='commander',content='Issue one kit',
            directives={'operation':'issue_equipment','deadline':30,'persons':['worker'],'material':'kit','from':'depot','quantity_each':1}))
        e=event(w,'issue','military_issue_equipment',order_id='issue',commander='owner',persons=['worker'],material='kit',quantity_each=1,authority_ref='commander',**{'from':'depot'})
        c=observe(w.s,e);frontier(w,[e]);self.assertEqual(w.s['stocks']['worker']['kit'],1)
        self.assertEqual(w.s['stocks']['depot']['kit'],2);self.assertTrue(w.s['orders']['issue']['executed'])
        self.assertIn(('orders','issue','directives','deadline'),c['reads'])
    def test_roman_delegation_revoke_conflict_and_expiry(self):
        w=setup('roman');apply(w,event(w,'cap','record_capacity',capacity_id='site',site='yard',quantity=1,unit='concurrent_people'))
        apply(w,event(w,'delegate','record_delegation',delegation_id='d',principal='owner',delegate='delegate',authority_ref='owner-authority',start=5,end=30,actors=['worker'],role='craft',site='yard'))
        now=w.s['clock']+1
        a=event(w,'work','roman_begin_delegated_activity',at=now,delegation_id='d',delegate='delegate',activity_id='w',actors=['worker'],site='yard',capacity_id='site',start=now,end=now+3,role='craft',authority_ref='owner-authority')
        b=event(w,'revoke','revoke_delegation',at=now,delegation_id='d',principal='owner',authority_ref='owner-authority')
        self.assertTrue(conflicts(observe(w.s,a),observe(w.s,b)))
        other=CoreWorld(state=w.s);frontier(other,[a]);self.assertEqual(other.s['activities']['w']['actors'],['worker'])
        frontier(w,[b]);self.assertFalse(w.s['delegations']['d']['active'])
        with self.assertRaises((InvalidEvent,AssertionError)):observe(w.s,event(w,'late','roman_begin_delegated_activity',delegation_id='d',delegate='delegate',activity_id='w',actors=['worker'],site='yard',capacity_id='site',start=now+5,end=now+8,role='craft',authority_ref='owner-authority'))
    def test_common_conflict_decisions_durable_and_revalidate(self):
        w=setup('military');apply(w,event(w,'stock','establish_stock',location='depot',material='grain',quantity=10,inventory_evidence_ref='count'))
        now=w.s['clock']+1
        events=[event(w,label,'transfer_stock',at=now,material='grain',quantity=8,authority_ref='owner',**{'from':'depot','to':label}) for label in ('house','army')]
        frontier(w,events);grant(w,'m','owner',['transfer_stock'],now,'selected authority')
        w=CoreWorld.load(w.save());resolve(w,'d','house',now+1,'m','owner',True)
        before=w.save()
        with self.assertRaises((InvalidEvent,AssertionError)):resolve(w,'d2','army',now+2,'m','owner',True)
        self.assertEqual(w.save(),before);self.assertEqual(w.s['stocks']['depot']['grain'],2)
    def test_unknown_request_can_be_denied_but_not_executed(self):
        w=setup('fantasy');frontier(w,[event(w,'unknown','unbound_magic_effect')]);now=w.s['clock']
        grant(w,'deny','owner',['deny_unqualified'],now,'local reviewing authority')
        with self.assertRaises(InvalidEvent):resolve(w,'approve','unknown',now+1,'deny','owner',True)
        resolve(w,'deny','unknown',now+1,'deny','owner',False)
        self.assertEqual(w.s['r9']['requests']['unknown']['status'],'denied')

if __name__=='__main__':unittest.main()
