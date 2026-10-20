"""IRGS Core v3.3 R4 *proposed* selective event coordinator.

Bounded test adapter on top of R3. This is NOT a general production-grade
read/write scheduler: op-specific footprints need independent qualification.
Deferred original requests have no effects. A later authorized decision is a
new actual event, never backdated to the original submission.
"""
from __future__ import annotations
import copy
from collections import defaultdict
from irgs_reference import World, InvalidEvent, digest


def footprint(s, ev):
    """Conservative named owner/record/capacity keys; unfamiliar ops serialize."""
    op, p = ev['op'], ev['params']
    keys = set()
    def add(*xs): keys.add(':'.join(map(str, xs)))
    if op in ('transfer_cash', 'pay'):
        add('cash', p['from']); add('cash', p.get('to', p.get('person')))
        if op == 'pay': add('claim', 'wage', p['person'])
    elif op == 'accrue_pay': add('claim', 'wage', p['person'])
    elif op == 'authorize_budget': add('budget', p['name'])
    elif op == 'assess_tax': add('tax', p['tax_id'])
    elif op == 'pay_tax':
        add('tax', p['tax_id']); add('cash', 'treasury')
        claim=s.get('econ3', {}).get('tax_claims', {}).get(p['tax_id'])
        if claim: add('cash', claim['payer'])
        else: add('global','unknown-tax-payer')
    elif op in ('issue_kits', 'allocate_competing_kits'):
        add('equipment', 'depot', 'kit')
        if op == 'issue_kits':
            for pid in p['persons']: add('actor',pid);add('equipment',pid,'kit')
        else:
            for req in p['requests']: add('equipment',req['to'],'kit')
    elif op in ('authorize_mobilization','enroll','enroll_from_residual'):
        add('gov','mobilization');add('formation','army')
        if op=='enroll': add('actor',p['person'])
        if op=='enroll_from_residual': add('pop','residual')
    elif op in ('commit_shift','release_shift'):
        add('actor',p['person']);add('time',p['person'])
    elif op=='start_job':
        add('job',p['job_id']); add('site',s.get('econ3',{}).get('recipes',{}).get(p['recipe_id'],{}).get('site','unknown'))
        for pid in p['workers']: add('actor',pid);add('time',pid)
        spec=s.get('econ3',{}).get('recipes',{}).get(p['recipe_id'],{})
        for mat in spec.get('inputs',{}): add('stock',spec['site'],mat)
    elif op in ('complete_job','interrupt_job','accrue_job_wages'):
        add('job',p['job_id'])
        job=s.get('econ3',{}).get('active_jobs',{}).get(p['job_id']) or s.get('econ3',{}).get('completed_jobs',{}).get(p['job_id'])
        if job:
            if op!='accrue_job_wages':
                spec=s['econ3']['recipes'][job['recipe_id']]
                for mat in set(spec['inputs']) | set(spec['outputs']):add('stock',job['site'],mat)
            else:
                for pid in job['workers']:add('claim','wage',pid)
    elif op=='dispatch_stock':
        add('stock',p['from'],p['material']);add('shipment',p['shipment_id'])
    elif op=='receive_stock':
        add('shipment',p['shipment_id'])
        ship=s.get('econ3',{}).get('shipments',{}).get(p['shipment_id'])
        if ship: add('stock',ship['to'],ship['material'])
    elif op=='provision_meals': add('stock',p['household'],'meal');add('household',p['household'])
    elif op=='complete_care': add('household',p['household']);add('actor',p['person']);add('time',p['person'])
    elif op=='audit_needs': add('household',p['household'])
    elif op in ('issue_order','receive_order','execute_order'):add('order',p['order_id'])
    elif op in ('capture','escape','legal_status_change','recognize_status','person_claim','propose_release'):
        add('actor',p.get('person',p.get('subject')))
        if op=='legal_status_change': add('legal',p['person'],p['jurisdiction'])
    elif op=='simultaneous_exchange':
        add('engagement',p['engagement_id'])
        for hit in p['attacks']:add('actor',hit['from']);add('actor',hit['to'])
    elif op=='summarize_engagement':add('engagement',p['engagement_id'])
    elif op in ('report',): add('report',ev['id'])
    elif op=='review_no_change':add('review',ev['id'])
    elif op=='demobilize':
        add('actor',p['person']);add('formation','army');add('equipment','depot','kit');add('equipment',p['person'],'kit')
    else: add('global','unclassified-operation')
    return keys


def components(s, events):
    """Transitive owner/capacity conflict components, not lexical winner selection."""
    pending={e['id']:set(footprint(s,e)) for e in events}
    parent={e['id']:e['id'] for e in events}
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def merge(x,y):
        rx,ry=root(x),root(y)
        if rx!=ry:parent[max(rx,ry)]=min(rx,ry)
    # A missing footprint contract is not proof of independence.
    # Unknown operations therefore share a conservative global component.
    if any('global:unclassified-operation' in toks for toks in pending.values()):
        for eid in pending: pending[eid].add('global:unknown-conservative-barrier')
    token_owner={}
    for eid,tokens in sorted(pending.items()):
        for token in sorted(tokens):
            if token in token_owner:merge(eid,token_owner[token])
            else:token_owner[token]=eid
    groups=defaultdict(list)
    for e in events:groups[root(e['id'])].append(e)
    return [sorted(g,key=lambda x:x['id']) for _,g in sorted(groups.items())]


class R4World(World):
    def __init__(self, initial=None, state=None):
        value=copy.deepcopy(state if state is not None else initial)
        if value is None:raise ValueError('Initial world required')
        value.setdefault('r4_deferred', {})
        value.setdefault('r4_decisions', [])
        value.setdefault('r4_request_ids', [])
        super().__init__(state=value)

    def schedule(self,eid,at,op,**params):
        if eid in self.s['r4_request_ids']:
            raise InvalidEvent('duplicate original request even if deferred or decided')
        super().schedule(eid,at,op,**params)
        self.s['r4_request_ids'].append(eid)

    def run_until(self,through):
        if through<self.s['clock']:raise InvalidEvent('cannot run backwards')
        report={'committed':[],'deferred':[],'through':through}
        while True:
            eligible=[ev for ev in self.s['pending'] if ev['at']<=through]
            if not eligible:break
            at=min(ev['at'] for ev in eligible)
            if at<self.s['clock']:raise InvalidEvent('unprocessed backdated request')
            epoch=[e for e in eligible if e['at']==at]
            # Partition uses PRE-event state; no first-writer wins in a shared key.
            groups=components(self.s,epoch)
            selected=copy.deepcopy(self.s)
            accepted=[];blocked=[]
            for group in groups:
                work=World(state=selected)
                try:
                    work._validate_concurrent_requests(group)
                    for ev in group:
                        work.apply(ev['id'],ev['at'],ev['op'],**ev['params'])
                    selected=work.s
                    accepted += [e['id'] for e in group]
                except InvalidEvent as err:
                    gid='contested:'+digest({'at':at,'ids':sorted(e['id'] for e in group)})[:20]
                    if gid in selected['r4_deferred']:raise InvalidEvent('contest identifier collision')
                    selected['r4_deferred'][gid]={'at':at,'requests':copy.deepcopy(group),
                        'status':'unresolved_unexecuted', 'diagnostic':str(err),
                        'allocation_selected':False}
                    blocked.append(gid)
            ids={e['id'] for e in epoch}
            selected['pending']=[e for e in selected['pending'] if e['id'] not in ids]
            # No backdating; advance clock only after all independent groups handled.
            nextworld=World(state=selected)
            if nextworld.s['clock']<at:nextworld.apply('frontier:'+str(at),at,'review_no_change')
            self.s=nextworld.s
            report['committed'].extend(accepted)
            report['deferred'].extend(blocked)
        if through>self.s['clock']:
            World(state=self.s)._validate(self.s)
            new=World(state=self.s)
            new.apply('frontier:'+str(through),through,'review_no_change')
            self.s=new.s
        return report

    def decide_deferred(self,group_id,chosen_request_ids,*,at,authority_ref):
        """For monetary/equipment allocations only. Unchosen requests are denied.

        Legal/physical validity must be checked again at the actual decision time.
        An external decision is required; no default ordering or winner.
        """
        if not authority_ref or not isinstance(authority_ref,str):raise InvalidEvent('authority reference required')
        if at<=self.s['clock']:raise InvalidEvent('decision requires a future causal frontier')
        rec=self.s['r4_deferred'].get(group_id)
        if not rec or rec['status']!='unresolved_unexecuted':raise InvalidEvent('no unresolved contest')
        ids={e['id'] for e in rec['requests']}; chosen=set(chosen_request_ids)
        if len(set(chosen_request_ids))!=len(chosen_request_ids) or not chosen<=ids:raise InvalidEvent('selection must be unique subset')
        selected=[e for e in rec['requests'] if e['id'] in chosen]
        if any(e['op'] not in ('transfer_cash','issue_kits') for e in rec['requests']):
            raise InvalidEvent('contest type requires separate specialist decision procedure')
        nextworld=World(state=self.s)
        transformed=[{'id':'authorized:'+e['id'], 'at':at,'op':e['op'],'params':e['params']} for e in selected]
        nextworld._validate_concurrent_requests(transformed)
        for e in transformed:nextworld.apply(e['id'],at,e['op'],**e['params'])
        new=nextworld.s
        new['r4_deferred'][group_id]['status']='decided'
        new['r4_deferred'][group_id]['allocation_selected']=True
        new['r4_deferred'][group_id]['decision_at']=at
        new['r4_deferred'][group_id]['approved_ids']=sorted(chosen)
        new['r4_deferred'][group_id]['denied_ids']=sorted(ids-chosen)
        new['r4_deferred'][group_id]['authority_ref']=authority_ref
        new['r4_decisions'].append({'group_id':group_id,'at':at,'approved_ids':sorted(chosen),
                                   'denied_ids':sorted(ids-chosen),'authority_ref':authority_ref})
        new=World(state=new)
        new._validate(new.s)
        self.s=new.s
        return copy.deepcopy(self.s['r4_decisions'][-1])
