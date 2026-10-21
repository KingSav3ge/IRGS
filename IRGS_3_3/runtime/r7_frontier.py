"""R7 BOUNDED candidate adapter: certified-in-fixture operations, not general runtime.

Same-frontier pre-state footprints protect selective execution. Known conflicts
are unresolved (not lexical winners); supported physical loss is committed
on its own occurrence frontier and ambiguous same-time work is preserved as
unexecuted evidence/ordering claim. Hand-declared footprints are NOT proof
of complete transitive dependency capture in independent genre adapters.
"""
from __future__ import annotations
import copy
from collections import defaultdict
from irgs_reference import World, InvalidEvent, digest
from r6_work import R6World, ProgressWorld, NEW_OPS, PROHIBITED_LEGACY
from selective_coordinator import footprint as legacy_footprint, components
from economic_extension import physical, free

FAB_OPS={'make_intermediate','inspect_intermediate','accept_intermediate','salvage_intermediate'}
ALLOWED_WORK=NEW_OPS|FAB_OPS

def _required(p,*names):
    for k in names:
        assert isinstance(p.get(k),str) and p[k].strip(),f'{k} must identify supporting source'

def _materials(e,spec):
    for mat in (spec['input'],spec['intermediate'],spec['finished'],spec['salvage']):
        assert mat in e['opening'],f'physical material missing from selected ledger: {mat}'

def validate_intermediates(s):
    records=s.get('r7_intermediates',{})
    for jid,rec in records.items():
        assert rec['status'] in ('uninspected','inspected_accept','inspected_reject','damaged','accepted','salvaged')
        assert type(rec['physical_qty']) is int and rec['physical_qty']>=0
        assert rec['site'] in s['econ3']['sites']
        assert physical(s['econ3'],'wip:'+jid,rec['intermediate'])==rec['physical_qty']
        assert rec['status'] in ('accepted','salvaged') or rec['physical_qty']>=0
        if rec['status'] in ('accepted','salvaged'):assert rec['physical_qty']==0
        assert rec['source_event_id'] in s['processed'] or rec['source_event_id']==s.get('_r7_event_id')
        assert digest(rec['profile_snapshot'])==rec['profile_digest'], 'profile binding altered retroactively'
    assert len(set(records))==len(records)

class FabricationWorld(ProgressWorld):
    def _validate(self,s):
        super()._validate(s)
        validate_intermediates(s)
    def _operate(self,s,at,op,p):
        if op not in FAB_OPS:return super()._operate(s,at,op,p)
        e=s['econ3']; records=s['r7_intermediates']
        jid=p['item_id']
        if op=='make_intermediate':
            _required(p,'profile_ref','work_evidence_ref','material_source_ref')
            assert jid not in records
            spec=s['r7_profiles'][p['profile_ref']]
            _materials(e,spec)
            site=p['site'];assert site in e['sites']
            assert type(spec['input_qty']) is int and spec['input_qty']>0
            assert type(spec['intermediate_qty']) is int and spec['intermediate_qty']>0
            assert free(e,site,spec['input'])>=spec['input_qty'], 'cannot take reserved inputs'
            e['stocks'][site][spec['input']]-=spec['input_qty']
            e['consumed'][spec['input']]+=spec['input_qty']
            wip_loc='wip:'+jid
            assert physical(e,wip_loc,spec['intermediate'])==0
            e['stocks'].setdefault(wip_loc,{})[spec['intermediate']]=spec['intermediate_qty']
            e['produced'][spec['intermediate']]+=spec['intermediate_qty']
            records[jid]={'profile':p['profile_ref'],'site':site,'intermediate':spec['intermediate'],
                'physical_qty':spec['intermediate_qty'],'initial_qty':spec['intermediate_qty'],
                'source_event_id':s['_r7_event_id'],'profile_snapshot':copy.deepcopy(spec),
                'profile_digest':digest(spec),'status':'uninspected','inspection_ref':None,
                'inspection_outcome':None,'losses':[],'disposition_ref':None}
        elif op=='inspect_intermediate':
            _required(p,'inspection_ref','inspector_authority_ref')
            rec=records[jid]
            assert rec['status'] in ('uninspected','damaged')
            outcome=p['outcome'];assert outcome in ('accept','reject')
            if rec['physical_qty']!=rec['initial_qty']:
                assert outcome=='reject','damaged batch cannot be presumed conforming'
            rec['status']='inspected_accept' if outcome=='accept' else 'inspected_reject'
            rec['inspection_ref']=p['inspection_ref'];rec['inspection_outcome']=outcome
        elif op=='accept_intermediate':
            _required(p,'acceptance_ref','competent_authority_ref')
            rec=records[jid];spec=rec['profile_snapshot']
            assert rec['status']=='inspected_accept'
            assert rec['physical_qty']==spec['intermediate_qty']
            assert type(spec['finished_qty']) is int and spec['finished_qty']>0
            loc='wip:'+jid; q=rec['physical_qty']
            e['stocks'][loc][spec['intermediate']]-=q; e['consumed'][spec['intermediate']]+=q
            site=rec['site'];mat=spec['finished']
            e['stocks'][site][mat]=physical(e,site,mat)+spec['finished_qty']
            e['produced'][mat]+=spec['finished_qty']
            rec['status']='accepted';rec['physical_qty']=0;rec['disposition_ref']=p['acceptance_ref']
        elif op=='salvage_intermediate':
            _required(p,'salvage_authority_ref','salvage_assessment_ref')
            rec=records[jid];spec=rec['profile_snapshot']
            assert rec['status']=='inspected_reject'
            assert type(spec['salvage_per_unit']) is int and spec['salvage_per_unit']>=0
            q=rec['physical_qty'];assert q>0
            loc='wip:'+jid
            e['stocks'][loc][spec['intermediate']]-=q;e['consumed'][spec['intermediate']]+=q
            recovery=q*spec['salvage_per_unit']
            site=rec['site'];mat=spec['salvage']
            e['stocks'][site][mat]=physical(e,site,mat)+recovery;e['produced'][mat]+=recovery
            rec['status']='salvaged';rec['physical_qty']=0
            rec['disposition_ref']=p['salvage_assessment_ref'];rec['recovered_quantity']=recovery

    def apply(self,eid,at,op,**params):
        if op not in FAB_OPS:return super().apply(eid,at,op,**params)
        # Set reference event ID only on ephemeral candidate, never as an
        # authoritative persistent source of truth.
        shadow=copy.deepcopy(self.s);shadow['_r7_event_id']=eid
        prior=self.s
        self.s=shadow
        try:
            result=super().apply(eid,at,op,**params)
            self.s.pop('_r7_event_id',None)
            validate_intermediates(self.s)
            return result
        except Exception:
            self.s=prior
            raise


def footprint_r7(s,ev):
    op,p=ev['op'],ev['params']
    if op not in NEW_OPS|FAB_OPS|{'physical_loss'}:
        return legacy_footprint(s,ev)
    keys=set()
    def touch(*parts): keys.add(':'.join(map(str,parts)))
    if op=='physical_loss':
        touch('stock',p['location'],p['material'])
        return keys
    if op in FAB_OPS:
        jid=p['item_id'];touch('intermediate',jid)
        if op=='make_intermediate':
            spec=s.get('r7_profiles',{}).get(p.get('profile_ref'),{})
            if spec:
                touch('stock',p['site'],spec['input']);touch('stock','wip:'+jid,spec['intermediate'])
                # Additive ledger totals are commutative; physical pool keys arbitrate scarce stock.
            else:touch('global','unclassified-operation')
        else:
            rec=s.get('r7_intermediates',{}).get(jid)
            if rec:
                spec=rec['profile_snapshot']
                if op!='inspect_intermediate':
                    touch('stock','wip:'+jid,spec['intermediate'])
                    mat=spec['finished'] if op=='accept_intermediate' else spec['salvage']
                    touch('stock',rec['site'],mat)
            else:touch('global','unclassified-operation')
        return keys
    jid=p.get('job_id',p.get('parent_job_id'))
    touch('job',jid)
    if op=='start_continuation':touch('job',p.get('job_id'))
    job=s.get('econ3',{}).get('active_jobs',{}).get(jid)
    spec=None
    if op in ('start_tracked_job','start_continuation'):
        spec=s.get('econ3',{}).get('recipes',{}).get(p.get('recipe_id'))
        workers=p.get('workers',[])
    elif job:
        spec=s['econ3']['recipes'][job['recipe_id']];workers=job['workers']
    else:workers=[]
    for pid in workers:
        touch('actor',pid);touch('time',pid)
        if op in ('settle_disrupted_job','finalize_tracked_job'):touch('claim','wage',pid)
    if spec:
        site=spec['site'];touch('site',site)
        for mat in set(spec['inputs'])|set(spec['outputs']):
            touch('stock',site,mat)
    else:touch('global','unclassified-operation')
    return keys


def independent_components(s,events):
    """Use conservative read/write token intersection, preserve pre-event snapshot."""
    pending={e['id']:footprint_r7(s,e) for e in events}
    if any('global:unclassified-operation' in v for v in pending.values()):
        for tokens in pending.values():tokens.add('global:unknown-conservative-barrier')
    parent={eid:eid for eid in pending}
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def link(a,b):
        a,b=root(a),root(b)
        if a!=b:parent[max(a,b)]=min(a,b)
    seen={}
    for eid,tokens in sorted(pending.items()):
        for token in sorted(tokens):
            if token in seen:link(eid,seen[token])
            else:seen[token]=eid
    out=defaultdict(list)
    for e in events:out[root(e['id'])].append(e)
    return [sorted(g,key=lambda x:x['id']) for _,g in sorted(out.items())]

class R7World(R6World):
    def __init__(self,initial=None,state=None):
        s=copy.deepcopy(state if state is not None else initial)
        if s is None:raise ValueError('initial world required')
        s.setdefault('r7_intermediates',{});s.setdefault('r7_profiles',{})
        super().__init__(state=s)
        validate_intermediates(self.s)

    def apply(self,eid,at,op,**params):
        if op in FAB_OPS:
            worker=FabricationWorld(state=self.s)
            out=worker.apply(eid,at,op,**params)
            validate_intermediates(worker.s)
            self.s=worker.s;return out
        if op=='physical_loss':
            worker=R6World(state=self.s)
            out=worker.apply(eid,at,op,**params)
            if not out:
                return False
            # Any physical loss against an intermediate is a change to that
            # same material's location/condition, not an independent report.
            for jid,rec in worker.s['r7_intermediates'].items():
                if params['location']=='wip:'+jid and params['material']==rec['intermediate']:
                    rec['physical_qty']-=params['quantity']
                    rec['losses'].append({'event_id':eid,'quantity':params['quantity'],
                        'cause_ref':params['cause_ref']})
                    rec['status']='damaged'
                    rec['inspection_outcome']=None;rec['inspection_ref']=None
            validate_intermediates(worker.s)
            self.s=worker.s;return out
        worker=R6World(state=self.s)
        out=worker.apply(eid,at,op,**params)
        validate_intermediates(worker.s)
        self.s=worker.s;return out

    def schedule(self,eid,at,op,**params):
        if eid in self.s['r4_request_ids']:
            raise InvalidEvent('duplicate request ID')
        # Bypass R6 guard, but NEVER bypass R7 execution/validation.
        World.schedule(self,eid,at,op,**params)
        self.s['r4_request_ids'].append(eid)

    def run_until(self,through):
        if through<self.s['clock']:raise InvalidEvent('cannot reverse time')
        result={'committed':[],'deferred':[],'physical_losses':[],'through':through}
        while True:
            eligible=[e for e in self.s['pending'] if e['at']<=through]
            if not eligible:break
            at=min(e['at'] for e in eligible)
            if at<self.s['clock']:raise InvalidEvent('backdated pending')
            epoch=[e for e in eligible if e['at']==at]
            # Freeze pre-event grouping. Work and physical loss are never
            # committed to authoritative state until the complete frontier
            # passes integrity checks. Rejection of impossible co-occurring
            # loss observations leaves this entire frontier unchanged.
            groups=independent_components(self.s,epoch)
            frontier=R7World(state=self.s)
            frontier_result={'committed':[],'deferred':[],'physical_losses':[],'through':through}
            for group in groups:
                losses=[e for e in group if e['op']=='physical_loss']
                others=[e for e in group if e['op']!='physical_loss']
                if losses:
                    pool=defaultdict(int)
                    for e in losses:
                        p=e['params']
                        q=p.get('quantity')
                        if type(q) is not int or q<=0:
                            raise InvalidEvent('invalid physical loss quantity')
                        pool[(p['location'],p['material'])]+=q
                    if any(q>physical(frontier.s['econ3'],loc,mat) for (loc,mat),q in pool.items()):
                        raise InvalidEvent('inconsistent evidence of co-occurring physical losses')
                    worker=R7World(state=frontier.s)
                    for ev in sorted(losses,key=lambda e:e['id']):
                        worker.apply(ev['id'],at,ev['op'],**ev['params'])
                    frontier.s=worker.s
                    frontier_result['committed'] += [e['id'] for e in losses]
                    frontier_result['physical_losses'] += [e['id'] for e in losses]
                    if others:frontier._defer(at,others,'causal_order_undetermined',frontier_result)
                elif len(group)==1:
                    ev=group[0];worker=R7World(state=frontier.s)
                    try:worker.apply(ev['id'],at,ev['op'],**ev['params'])
                    except InvalidEvent as err:
                        frontier._defer(at,group,'invalid_or_missing_prerequisite: '+str(err),frontier_result)
                    else:
                        if 'global:unclassified-operation' in footprint_r7(self.s,ev):
                            frontier._defer(at,group,'unqualified_operation_footprint',frontier_result)
                        else:
                            frontier.s=worker.s;frontier_result['committed'].append(ev['id'])
                else:
                    frontier._defer(at,group,'unresolved_same_time_dependency_or_authority',frontier_result)
            ids={e['id'] for e in epoch}
            frontier.s['pending']=[e for e in frontier.s['pending'] if e['id'] not in ids]
            if frontier.s['clock']<at:
                frontier.apply('frontier:r7:'+str(at),at,'review_no_change')
            validate_intermediates(frontier.s)
            # Commit frontier once all components have passed.
            self.s=frontier.s
            for name in ('committed','deferred','physical_losses'):
                result[name].extend(frontier_result[name])
        if self.s['clock']<through:
            self.apply('frontier:r7:'+str(through),through,'review_no_change')
        return result

    def _defer(self,at,group,reason,result):
        gid='r7:'+digest({'at':at,'ids':sorted(e['id'] for e in group)})[:22]
        assert gid not in self.s['r4_deferred']
        self.s['r4_deferred'][gid]={
            'at':at,'requests':copy.deepcopy(group),'status':'unresolved_unexecuted',
            'diagnostic':reason,'allocation_selected':False,'r7_footprint_status':'bounded_declared_not_certified'}
        result['deferred'].append(gid)
