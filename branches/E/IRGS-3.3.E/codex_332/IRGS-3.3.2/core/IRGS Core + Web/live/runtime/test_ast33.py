import copy
import unittest
from ast_runtime import initial_ast, ASTWorld
from r9_runtime import frontier, observe, conflicts
from irgs_reference import InvalidEvent

def event(eid,op,at=1,**p):
    return {'id':eid,'op':op,'at':at,'params':{'campaign_id':'AST','source_ref':'test-only',**p}}
def apply(w,e):return w.apply(e['id'],e['at'],e['op'],**e['params'])

class ASTTests(unittest.TestCase):
    def test_registry_exact_identities(self):
        w=initial_ast();self.assertEqual(len(w.s['actors']),37)
        self.assertEqual(sum(a['species']=='human' for a in w.s['actors'].values()),36)
        self.assertEqual(w.s['actors']['AST-04']['name'],'Abel')
        self.assertEqual(w.s['registry']['deprecated_spellings']['Able'],'AST-04')
        self.assertNotIn('AST-38',w.s['actors']);self.assertNotIn('AST-39',w.s['actors'])
    def test_no_invented_current_quantities_or_day3_actions(self):
        w=initial_ast();self.assertFalse(w.s['stocks']);self.assertFalse(w.s['player_actions'])
        self.assertEqual(w.s['campaign_time']['day'],2)
        self.assertFalse(w.s['designs']['coopian']['manufactured'])
    def test_source_numerical_ratings_not_adopted(self):
        w=initial_ast()
        self.assertTrue(all(not r['provisional_ratings_adopted'] for r in w.s['registry']['characters'].values()))
        self.assertNotIn('skills',w.s['actors']['AST-01'])
    def test_guard_names_and_title(self):
        w=initial_ast();self.assertEqual(w.s['actors']['AST-36']['name'],'Roger Kett')
        self.assertEqual(w.s['actors']['AST-37']['name'],'Adam Lark')
        self.assertEqual(w.s['actors']['AST-35']['name'],'Master Nicholas Rookwood')
    def test_evidence_not_omniscient_knowledge(self):
        w=initial_ast();e=event('e','ast_record_evidence',evidence_id='claim',subject='AST-35',assertion='An allegation',status='testimony')
        frontier(w,[e]);self.assertEqual(w.s['knowledge'],{})
        frontier(w,[event('receipt','ast_receive_evidence',2,evidence_id='claim',recipient='AST-08')])
        self.assertIn('claim',w.s['knowledge']['AST-08']);self.assertNotIn('AST-01',w.s['knowledge'])
    def test_testimony_cannot_change_character_state(self):
        w=initial_ast();apply(w,event('e','ast_record_evidence',evidence_id='claim',subject='AST-35',assertion='Knight?',status='testimony'))
        before=w.save()
        with self.assertRaises(InvalidEvent):apply(w,event('confirm','ast_confirm_character_field',2,evidence_id='claim',subject='AST-35',field='service',value='knight',authority_ref='fixture'))
        self.assertEqual(w.save(),before)
    def test_player_declaration_has_no_automatic_cost_or_outcome(self):
        w=initial_ast();apply(w,event('choice','ast_record_player_action',actor='AST-01',instruction_ref='player-message',declaration='I inspect the shield'))
        self.assertEqual(w.s['player_actions'][0]['status'],'declared_not_resolved');self.assertFalse(w.s['stocks'])
    def test_no_player_choice_without_instruction(self):
        w=initial_ast()
        with self.assertRaises(InvalidEvent):apply(w,event('choice','ast_record_player_action',actor='AST-01',instruction_ref='',declaration='I spend money'))
    def test_cross_campaign_rejected_before_replay(self):
        w=initial_ast();e=event('d','ast_record_design',design_id='test',name='draft');apply(w,e)
        e['params']['campaign_id']='OTHER'
        with self.assertRaises(InvalidEvent):apply(w,e)
    def test_replay_no_duplicate_effect(self):
        w=initial_ast();e=event('d','ast_record_design',design_id='test',name='draft');apply(w,e);before=w.save()
        self.assertFalse(apply(w,e));self.assertEqual(w.save(),before)
    def test_shared_stock_contention(self):
        w=initial_ast();apply(w,event('init','ast_establish_stock',location='store',material='grain',quantity=10,inventory_evidence_ref='count'))
        a=event('house','ast_transfer_stock',2,**{'from':'store','to':'household','material':'grain','quantity':8,'authority_ref':'fixture'})
        b=event('army','ast_transfer_stock',2,**{'from':'store','to':'military','material':'grain','quantity':8,'authority_ref':'fixture'})
        r=frontier(w,[a,b]);self.assertEqual(set(r['deferred']),{'house','army'});self.assertEqual(w.s['stocks']['store']['grain'],10)
    def test_stock_transfer_conserves(self):
        w=initial_ast();apply(w,event('init','ast_establish_stock',location='store',material='grain',quantity=10,inventory_evidence_ref='count'))
        e=event('move','ast_transfer_stock',2,**{'from':'store','to':'household','material':'grain','quantity':3,'authority_ref':'fixture'})
        c=observe(w.s,e);frontier(w,[e]);self.assertEqual(w.s['stocks']['household']['grain'],3)
        self.assertIn(('stocks','store','grain'),c['reads'])
    def test_unknown_stock_is_not_zero_or_created(self):
        w=initial_ast();before=w.save()
        with self.assertRaises(InvalidEvent):apply(w,event('move','ast_transfer_stock',**{'from':'unknown','to':'house','material':'grain','quantity':1,'authority_ref':'fixture'}))
        self.assertEqual(before,w.save())
    def test_offer_not_agreement(self):
        w=initial_ast();apply(w,event('offer','ast_record_obligation',obligation_id='sort',subject='AST-01',description='Sort hinges',status='offered'))
        self.assertEqual(w.s['obligations']['sort']['quantity'],None)
        with self.assertRaises(InvalidEvent):apply(w,event('accept','ast_record_obligation',obligation_id='sort2',subject='AST-01',description='Sort hinges',status='agreed'))
    def test_received_order_not_executed(self):
        w=initial_ast();apply(w,event('order','ast_receive_order',order_id='o',recipient='AST-07',authority_ref='fixture',content='Example'))
        self.assertFalse(w.s['orders']['o']['executed'])
    def test_scene_does_not_invent_wakeup(self):
        w=initial_ast();before=copy.deepcopy(w.s['actors']['AST-01'])
        apply(w,event('scene','ast_set_scene',day=3,time=None,precision='unresolved',description='Day 3',instruction_ref='player-message'))
        self.assertEqual(w.s['actors']['AST-01'],before)
    def test_ast_save_load(self):
        w=initial_ast();self.assertEqual(ASTWorld.load(w.save()).checksum(),w.checksum())
    def test_established_evidence_can_confirm_npc_field(self):
        w=initial_ast();apply(w,event('e','ast_record_evidence',evidence_id='seen',subject='AST-08',assertion='At the gate',status='established'))
        apply(w,event('confirm','ast_confirm_character_field',2,evidence_id='seen',subject='AST-08',field='location',value='gate',authority_ref='fixture-observer'))
        self.assertEqual(w.s['actors']['AST-08']['current']['location']['value'],'gate')

if __name__=='__main__':unittest.main()
