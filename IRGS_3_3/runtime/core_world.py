"""Core 3.3 campaign-state kernel. Genre bindings and campaign libraries are data.
Legacy AST event spellings remain accepted for existing saved journals.
"""
import copy,json
from irgs_reference import InvalidEvent,canon,digest
GENRE_OPS={'military_issue_equipment','roman_begin_delegated_activity','revoke_delegation'}
from temporal_registry import ENTITY_OPS, operate_entity, validate_registry

ALIASES={"ast_"+op:op for op in (
"record_evidence","receive_evidence","record_player_action","set_scene",
"confirm_character_field","establish_stock","transfer_stock","record_obligation",
"record_design","receive_order")}
CORE_OPS=set(ALIASES.values())
CORE_OPS.update({'register_actor','record_capacity','commit_activity','record_delegation'})
CORE_OPS.update({'execute_player_equipment_issue','receive_response_prompt'})
CORE_OPS.add('execute_player_scene_action')
CORE_OPS.add('execute_settlement_action')
CORE_OPS.update(ENTITY_OPS)
SUPPORTED_OPS=CORE_OPS|set(ALIASES)|GENRE_OPS

class CoreWorld:
    def __init__(self,state=None,initial=None):
        if not __debug__: raise InvalidEvent('Core validation requires Python without -O')
        self.s=copy.deepcopy(state if state is not None else initial)
        self._validate(self.s)
    @classmethod
    def load(cls,text):return cls(state=json.loads(text))
    def save(self):return canon(self.s)
    def checksum(self):return digest(self.s)
    def _validate(self,s):
        assert s['profile'] in ('IRGS-CORE-3.3','AST-CORE-3.3') and isinstance(s['campaign_id'],str) and s['campaign_id']
        assert type(s['clock']) is int and s['clock']>=0
        assert all(a['id']==cid for cid,a in s['actors'].items())
        if 'entity_registry' in s:validate_registry(s['entity_registry'],s['actors'])
        registry=s.get('registry',{}).get('characters',{})
        assert set(registry).issubset(s['actors'])
        assert all(s['actors'][cid]['name']==r['name'] and s['actors'][cid]['species']==r['species'] for cid,r in registry.items())
        assert not set(s.get('registry',{}).get('withdrawn_duplicate_ids',[]))&set(s['actors'])
        players=self.player_ids(s)
        assert len(players)==len(set(players)) and all(cid in s['actors'] for cid in players)
        assert all(type(q) is int and q>=0 for loc in s['stocks'].values() for q in loc.values())
        materials={m for loc in s['stocks'].values() for m in loc}
        assert materials==set(s['opening_stock']), 'every physical material requires a conserved opening basis'
        for material,total in s['opening_stock'].items():
            assert type(total) is int and total>=0
            consumed=sum(f['quantity'] for f in s.get('material_flows',{}).values() if f['material']==material)
            assert sum(loc.get(material,0) for loc in s['stocks'].values())==total-consumed
        for flow in s.get('material_flows',{}).values():
            assert flow['kind']=='consumption' and type(flow['quantity']) is int and flow['quantity']>0
            assert flow['material'] in s['opening_stock'] and flow['source_ref'] and flow['purpose']
            assert flow['account'] in s['stocks']
        from settlement_runtime import validate_settlement
        validate_settlement(s)
        ids=[e['id'] for e in s['journal']]
        assert len(ids)==len(set(ids)) and set(ids)==set(s['processed'])
        assert all(s['processed'][e['id']]==digest(e) for e in s['journal'])
        for request in s.get('r9',{}).get('requests',{}).values():
            if 'original_digest' in request:assert digest(request['original'])==request['original_digest'],'durable request altered'
        for recipient,known in s['knowledge'].items():
            assert recipient in s['actors']
            assert all(eid in s['evidence'] and rec['received_at']>=s['evidence'][eid]['recorded_at'] for eid,rec in known.items())
        capacities=s.get('capacities',{})
        assert all(type(c['quantity']) is int and c['quantity']>=0 for c in capacities.values())
        activities=list(s.get('activities',{}).values())
        for i,a in enumerate(activities):
            assert a['start']<a['end'] and a['capacity_id'] in capacities
            assert a['site']==capacities[a['capacity_id']]['site']
            assert a['actors'] and len(a['actors'])==len(set(a['actors'])) and all(cid in s['actors'] for cid in a['actors'])
            assert all(not(set(a['actors'])&set(b['actors'])) for b in activities[:i] if a['start']<b['end'] and b['start']<a['end'])
        for cid,c in capacities.items():
            matching=[a for a in activities if a['capacity_id']==cid]
            for point in {a['start'] for a in matching}:
                assert sum(len(a['actors']) for a in matching if a['start']<=point<a['end'])<=c['quantity']
    def player_ids(self,s):
        return s.get('player_actor_ids',['AST-01'] if s.get('campaign_id')=='AST' else [])
    def apply(self,eid,at,op,**p):
        p=copy.deepcopy(p)
        event={'id':eid,'at':at,'op':op,'params':p}
        if not isinstance(eid,str) or not eid.strip():raise InvalidEvent('event identity required')
        if op not in SUPPORTED_OPS:raise InvalidEvent('operation not supplied by the selected Core/genre binding')
        # Mandatory campaign scope is checked before replay lookup.
        if p.get('campaign_id')!=self.s['campaign_id']:raise InvalidEvent('cross-campaign or missing scope')
        if eid in self.s['processed']:
            if self.s['processed'][eid]!=digest(event):raise InvalidEvent('event payload changed')
            return False
        if type(at) is not int or at<self.s['clock']:raise InvalidEvent('invalid causal sequence')
        s=copy.deepcopy(self.s)
        try:
            self._operate(s,at,ALIASES.get(op,op),p)
            s['clock']=at;s['journal'].append(event);s['processed'][eid]=digest(event);self._validate(s)
        except (AssertionError,KeyError,TypeError,ValueError) as err:raise InvalidEvent(f'{op}: {err}') from err
        self.s=s;return True
    def _operate(self,s,at,op,p):
        assert isinstance(p.get('source_ref'),str) and p['source_ref'].strip(),'source reference required'
        if op=='execute_player_equipment_issue':
            from player_actions import operate_equipment_action
            return operate_equipment_action(self,s,at,p)
        if op=='execute_settlement_action':
            from settlement_runtime import operate_settlement_action
            return operate_settlement_action(self,s,at,p)
        if op=='execute_player_scene_action':
            from scene_actions import operate_scene_action
            return operate_scene_action(self,s,at,p)
        if op=='receive_response_prompt':
            from response_options import operate_response_prompt
            return operate_response_prompt(self,s,at,p)
        if op in ENTITY_OPS:
            return operate_entity(self,s,at,op,p)
        if op in GENRE_OPS:
            return self._operate_domain(s,at,op,p)
        if op=='register_actor':
            cid=p['actor_id'];assert isinstance(cid,str) and cid.strip() and cid not in s['actors']
            assert cid not in s.get('registry',{}).get('withdrawn_duplicate_ids',[])
            assert isinstance(p['name'],str) and p['name'].strip() and isinstance(p['species'],str) and p['species'].strip()
            assert p['name'] not in s.get('registry',{}).get('deprecated_spellings',{}),'use the existing canonical identity for an archival spelling'
            if p.get('player_controlled'):
                assert p.get('instruction_ref'),'player control requires explicit user selection'
                s.setdefault('player_actor_ids',[]).append(cid)
            s['actors'][cid]={'id':cid,'name':p['name'],'species':p['species'],'current':{},'source_ref':p['source_ref']}
            if 'entity_registry' in s:
                point=s['entity_registry']['as_of']
                operate_entity(self,s,at,'register_entity',{
                    'entity_id':cid,'kind':'character','effective_at':point,'source_ref':p['source_ref'],
                    'identity':{'name':p['name'],'category':'person' if p['species'].strip().casefold()=='human' else 'creature','species':p['species']}})
                if p.get('player_controlled') and 'individual' in s['entity_registry']['scenarios']:
                    operate_entity(self,s,at,'record_entity_eligibility',{
                        'entity_id':cid,'scenario_id':'individual','effective_at':point,'source_ref':p['source_ref'],
                        'eligible':True,'reason':'Explicit player control was selected when this actor was registered.',
                        'control':{'mode':'individual','actor_ids':[cid],'powers':['declare_own_intent']}})
        elif op=='record_delegation':
            key=p['delegation_id'];assert key not in s.get('delegations',{})
            assert p['principal'] in s['actors'] and p['delegate'] in s['actors'] and p['authority_ref']
            assert type(p['start']) is int and type(p['end']) is int and at<=p['start']<p['end']
            assert p['actors'] and all(a in s['actors'] for a in p['actors'])
            assert p['role'] and p['site']
            if p['principal'] in self.player_ids(s):assert p.get('instruction_ref')
            s.setdefault('delegations',{})[key]={k:copy.deepcopy(p[k]) for k in ('principal','delegate','authority_ref','start','end','actors','role','site','source_ref')}
            s['delegations'][key]['active']=True
        elif op=='record_capacity':
            key=p['capacity_id'];assert key not in s.get('capacities',{})
            assert type(p['quantity']) is int and p['quantity']>=0 and p['unit'] and p['site']
            s.setdefault('capacities',{})[key]={'site':p['site'],'quantity':p['quantity'],'unit':p['unit'],'source_ref':p['source_ref']}
        elif op=='commit_activity':
            key=p['activity_id'];assert key not in s.get('activities',{})
            people=p['actors'];assert isinstance(people,list) and people and len(set(people))==len(people)
            assert all(cid in s['actors'] for cid in people)
            assert p['authority_ref'] and p['role']
            if set(people)&set(self.player_ids(s)):assert p.get('instruction_ref')
            start,end=p['start'],p['end'];assert type(start) is int and type(end) is int and at<=start<end
            capacity=s['capacities'][p['capacity_id']];assert capacity['site']==p['site']
            assert capacity['unit']=='concurrent_people','this receiver requires a people-capacity profile'
            overlaps=[a for a in s.get('activities',{}).values() if a['start']<end and start<a['end']]
            assert all(not(set(people)&set(a['actors'])) for a in overlaps),'individual already committed'
            relevant=[a for a in overlaps if a['capacity_id']==p['capacity_id']]
            boundaries=sorted({start,end}|{max(start,a['start']) for a in relevant}|{min(end,a['end']) for a in relevant})
            for point in boundaries[:-1]:
                used=sum(len(a['actors']) for a in relevant if a['start']<=point<a['end'])
                assert used+len(people)<=capacity['quantity'],'site capacity exceeded'
            s.setdefault('activities',{})[key]={'actors':list(people),'site':p['site'],'capacity_id':p['capacity_id'],
                'start':start,'end':end,'role':p['role'],'authority_ref':p['authority_ref'],'source_ref':p['source_ref']}
        elif op=='record_evidence':
            key=p['evidence_id'];assert key not in s['evidence'] and p['subject'] in s['actors']
            assert p['status'] in ('established','testimony','inference','provisional','unknown','superseded')
            assert isinstance(p['assertion'],str) and p['assertion'].strip()
            s['evidence'][key]={'subject':p['subject'],'assertion':p['assertion'],'status':p['status'],
                'source_ref':p['source_ref'],'recorded_at':at,'originator':p.get('originator'),
                'occurrence_time':p.get('occurrence_time'),'visibility':'only explicitly received knowledge'}
        elif op=='receive_evidence':
            key=p['evidence_id'];rec=s['evidence'][key];recipient=p['recipient'];assert recipient in s['actors']
            assert rec['recorded_at']<=at
            known=s['knowledge'].setdefault(recipient,{})
            assert key not in known,'receipt already recorded'
            known[key]={'received_at':at,'source_ref':p['source_ref']}
        elif op=='record_player_action':
            assert p['actor'] in self.player_ids(s) and p['instruction_ref'] and p['declaration']
            if 'entity_registry' in s:
                from temporal_registry import available_entities
                present=available_entities(s['entity_registry'],scenario_id=s.get('starting_control',{}).get('scenario_id','individual'))['characters']
                assert any(item['id']==p['actor'] and item['exists'] for item in present),'the selected character does not exist at the current committed world date'
            # Records what the player declared, not an automatic outcome/cost.
            s['player_actions'].append({'actor':p['actor'],'declaration':p['declaration'],
                'instruction_ref':p['instruction_ref'],'at':at,'status':'declared_not_resolved'})
        elif op=='set_scene':
            assert p['instruction_ref'] and type(p['day']) is int and p['day']>=s['campaign_time']['day']
            s['campaign_time']={'day':p['day'],'time':p.get('time'),'precision':p['precision'],
                                'phase':p['description'],'source_ref':p['source_ref']}
        elif op=='confirm_character_field':
            rec=s['evidence'][p['evidence_id']];assert rec['subject']==p['subject'] and rec['status']=='established'
            assert p['authority_ref'] and p['field'] in ('location','condition','custody','service','current_activity')
            if p['subject'] in self.player_ids(s) and p['field'] in ('location','service','current_activity'):
                assert p.get('instruction_ref'),'player declaration required'
            s['actors'][p['subject']]['current'][p['field']]={'value':p['value'],'evidence_id':p['evidence_id'],'at':at}
        elif op=='establish_stock':
            loc,mat,qty=p['location'],p['material'],p['quantity']
            assert type(qty) is int and qty>=0 and p['inventory_evidence_ref']
            assert mat not in s['stocks'].get(loc,{}),'existing stock requires an actual change event'
            s['stocks'].setdefault(loc,{})[mat]=qty
            s['opening_stock'][mat]=s['opening_stock'].get(mat,0)+qty
        elif op=='transfer_stock':
            src,dst,mat,qty=p['from'],p['to'],p['material'],p['quantity']
            assert src!=dst and type(qty) is int and qty>0 and p['authority_ref']
            assert s['stocks'][src][mat]>=qty
            s['stocks'][src][mat]-=qty
            s['stocks'].setdefault(dst,{})[mat]=s['stocks'].get(dst,{}).get(mat,0)+qty
        elif op=='record_obligation':
            assert p['obligation_id'] not in s['obligations'] and p['subject'] in s['actors']
            assert p['status'] in ('offered','agreed','due','disputed','fulfilled','unknown')
            if p['subject'] in self.player_ids(s) and p['status']=='agreed':assert p.get('instruction_ref')
            s['obligations'][p['obligation_id']]={'subject':p['subject'],'description':p['description'],
                'status':p['status'],'source_ref':p['source_ref'],'quantity':p.get('quantity')}
        elif op=='record_design':
            assert p['design_id'] not in s['designs']
            s['designs'][p['design_id']]={'name':p['name'],'status':'design reference',
                'manufactured':False,'source_ref':p['source_ref']}
        elif op=='receive_order':
            recipient=p['recipient'];assert recipient in s['actors'] and p['order_id'] not in s['orders']
            assert p['authority_ref'] and p['content']
            s['orders'][p['order_id']]={'recipient':recipient,'content':p['content'],'received_at':at,
                'authority_ref':p['authority_ref'],'executed':False,'source_ref':p['source_ref']}
            if 'directives' in p:s['orders'][p['order_id']]['directives']=copy.deepcopy(p['directives'])

    def _operate_domain(self,s,at,op,p):
        """Called Core routines; authority and effects use this same transaction."""
        if op=='military_issue_equipment':
            binding=s.get('binding',{})
            assert binding.get('genre_id') in ('military','roman'),'military/historical receiving profile required'
            order=s['orders'][p['order_id']]
            assert order['recipient']==p['commander'] and not order['executed']
            assert order['received_at']<=at
            directives=order['directives']
            assert directives['operation']=='issue_equipment' and at<=directives['deadline']
            assert directives['persons']==p['persons'] and directives['material']==p['material']
            assert directives['from']==p['from'] and directives['quantity_each']==p['quantity_each']
            assert p['authority_ref']==order['authority_ref']
            assert p['persons'] and len(set(p['persons']))==len(p['persons'])
            assert all(cid in s['actors'] for cid in p['persons'])
            assert type(p['quantity_each']) is int and p['quantity_each']>0
            for cid in p['persons']:
                self._operate(s,at,'transfer_stock',{'from':p['from'],'to':cid,'material':p['material'],
                    'quantity':p['quantity_each'],'authority_ref':p['authority_ref'],'source_ref':p['source_ref']})
            order['executed']=True;order['executed_at']=at
        elif op=='roman_begin_delegated_activity':
            assert s.get('binding',{}).get('genre_id')=='roman','Roman receiving profile required'
            d=s['delegations'][p['delegation_id']]
            assert d['active'] and d['delegate']==p['delegate']
            assert d['start']<=p['start']<p['end']<=d['end']
            assert p['site']==d['site'] and p['role']==d['role'] and p['actors']==d['actors']
            assert p['authority_ref']==d['authority_ref']
            params={k:p[k] for k in ('activity_id','actors','site','capacity_id','start','end','role','authority_ref','source_ref')}
            if 'instruction_ref' in p:params['instruction_ref']=p['instruction_ref']
            self._operate(s,at,'commit_activity',params)
        elif op=='revoke_delegation':
            d=s['delegations'][p['delegation_id']]
            assert d['principal']==p['principal'] and p['authority_ref']==d['authority_ref']
            if d['principal'] in self.player_ids(s):assert p.get('instruction_ref')
            d['active']=False;d['revoked_at']=at;d['revoke_source']=p['source_ref']
