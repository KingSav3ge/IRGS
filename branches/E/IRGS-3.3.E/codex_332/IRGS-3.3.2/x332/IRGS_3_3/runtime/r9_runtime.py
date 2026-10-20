"""R9 proposed full-dispatch instrumentation and durable decision workflow.

Reviewed JSON handlers only. This is not a sandbox for arbitrary Python plugins.
"""
import copy
import sys
from irgs_reference import World, InvalidEvent, digest
from r7_frontier import R7World, FAB_OPS
from r6_work import NEW_OPS
from r8_dependencies import SUPPORTED as BASE_OPS, changed, conflicts, code_identity
from r9_adapters import ReceiverWorld, NATIVE_OPS
from ast_runtime import ASTWorld, AST_OPS
from core_world import CoreWorld, CORE_OPS
from genre_receivers import GENRE_OPS

SUPPORTED = BASE_OPS | NEW_OPS | FAB_OPS | {'physical_loss'} | NATIVE_OPS | AST_OPS | CORE_OPS | GENRE_OPS
META = {'clock','journal','processed','_r6_eid','_r7_event_id'}

def plain(value):
    if isinstance(value, dict):
        return {k:plain(v) for k,v in dict.items(value)}
    if isinstance(value,list): return [plain(v) for v in value]
    return value

class Trace:
    def __init__(self):
        self.reads=set(); self.writes=set(); self.validation_reads=set()
    def add(self,path,write=False):
        # Validators are checked on the final combined candidate. Their broad
        # invariant scans are retained as evidence, not allocation dependencies.
        frame=sys._getframe(1)
        validation=False
        while frame:
            name=frame.f_code.co_name
            if name=='_validate' or name.startswith('validate_'):
                validation=True; break
            frame=frame.f_back
        if validation:
            if write: raise InvalidEvent('validator attempted mutation')
            self.validation_reads.add(path)
        else: (self.writes if write else self.reads).add(path)

class TracedDict(dict):
    def __init__(self,data,trace,path=()):
        self.trace,self.path=trace,path
        for k,v in dict.items(data): dict.__setitem__(self,k,self.wrap(v,path+(str(k),)))
    def wrap(self,v,path):
        if isinstance(v,dict): return TracedDict(plain(v),self.trace,path)
        if isinstance(v,list): return [self.wrap(x,path+(str(i),)) for i,x in enumerate(v)]
        return v
    def __getitem__(self,key):
        path=self.path+(str(key),)
        self.trace.add(path+('@exists',))
        value=dict.__getitem__(self,key)
        if not isinstance(value,dict): self.trace.add(path)
        if isinstance(value,list):
            # Lists are opaque mutable containers. Reserve the whole subtree;
            # validators only read them, so do not invent validation writes.
            self.trace.add(path)
            frame=sys._getframe(1); validation=False; constructing=False
            while frame:
                if frame.f_code.co_name=='__init__':constructing=True
                if frame.f_code.co_name=='_validate' or frame.f_code.co_name.startswith('validate_'):
                    validation=True; break
                frame=frame.f_back
            if not validation and not constructing: self.trace.add(path,True)
        return value
    def __contains__(self,key):
        self.trace.add(self.path+(str(key),'@exists'))
        return dict.__contains__(self,key)
    def get(self,key,default=None):
        try:return self[key]
        except KeyError:return default
    def __setitem__(self,key,value):
        path=self.path+(str(key),); self.trace.add(path,True)
        dict.__setitem__(self,key,self.wrap(value,path))
    def __delitem__(self,key):
        self.trace.add(self.path+(str(key),),True); dict.__delitem__(self,key)
    def __iter__(self):
        self.trace.add(self.path); return dict.__iter__(self)
    def __len__(self):
        self.trace.add(self.path); return dict.__len__(self)
    def keys(self):
        self.trace.add(self.path); return dict.keys(self)
    def items(self):
        self.trace.add(self.path)
        return ((k,self[k]) for k in dict.__iter__(self))
    def values(self):
        self.trace.add(self.path)
        return (self[k] for k in dict.__iter__(self))
    def setdefault(self,key,default=None):
        if key not in self: self[key]=default
        return self[key]
    def pop(self,key,*default):
        if key not in self:
            if default:return default[0]
            raise KeyError(key)
        value=self[key]; del self[key]; return value
    def update(self,*args,**kwargs):
        for k,v in dict(*args,**kwargs).items():self[k]=v
    def __deepcopy__(self,memo):
        # Transaction cloning is not a domain read. Copying an actual nested
        # record is a read of that subtree, even if later detached and changed.
        if self.path:
            self.trace.add(self.path)
            return copy.deepcopy(plain(self),memo)
        return TracedDict(plain(self),self.trace)

def effect_paths(paths):
    return sorted(p for p in paths if not p or p[0] not in META)

def observe(state,event):
    if event['op'] not in SUPPORTED: raise InvalidEvent('native/unknown handler not qualified')
    if event['id'] in state['processed']:raise InvalidEvent('processed event is not a fresh request')
    cls=CoreWorld if state.get('profile') in ('IRGS-CORE-3.3','AST-CORE-3.3') else ReceiverWorld if 'r9_engine_bindings' in state else R7World if 'econ3' in state else World
    worker=cls(state=state)
    trace=Trace(); worker.s=TracedDict(worker.s,trace)
    worker.apply(event['id'],event['at'],event['op'],**copy.deepcopy(event['params']))
    observed=plain(worker.s)
    reference=cls(state=state)
    reference.apply(event['id'],event['at'],event['op'],**copy.deepcopy(event['params']))
    if observed!=reference.s:raise InvalidEvent('instrumented/uninstrumented execution mismatch')
    delta=changed(state,reference.s)
    # Real diff is a backstop for writes performed by inherited C-level methods.
    trace.writes.update(delta)
    return {'event':copy.deepcopy(event),'snapshot':digest(state),'code':code_identity(),
            'backend':cls.__name__,'profile':state.get('profile','legacy_research_fixture'),
            'reads':effect_paths(trace.reads),'writes':effect_paths(trace.writes),
            'validation_reads':sorted(trace.validation_reads),'post_state':digest(reference.s)}

def ensure_store(s):
    s.setdefault('r9',{'requests':{},'decisions':{},'frontiers':[], 'mandates':{}})

def frontier(world,events):
    """Persist submitted intent and conflicts atomically; never choose a winner."""
    if not events:return {'committed':[],'deferred':[]}
    events=copy.deepcopy(events)
    if any(not isinstance(e.get('id'),str) or not e['id'].strip() or type(e.get('at')) is not int for e in events):
        raise InvalidEvent('nonempty string identities and integer causal times required')
    if len({e['id'] for e in events})!=len(events) or len({e['at'] for e in events})!=1:
        raise InvalidEvent('unique request IDs and one timestamp required')
    candidate=type(world)(state=world.s); ensure_store(candidate.s)
    store=candidate.s['r9']; at=events[0]['at']
    if at<candidate.s['clock']:raise InvalidEvent('backdated frontier')
    for event in events:
        if event['id'] in store['requests'] or event['id'] in candidate.s['processed']:
            raise InvalidEvent('request identity already used')
    certificates={}; errors={}
    for e in events:
        try: certificates[e['id']]=observe(candidate.s,e)
        except (InvalidEvent,AssertionError,KeyError,ValueError,TypeError) as err:errors[e['id']]=str(err)
    # Qualified physical observations are occurrences, not allocation requests.
    # Verify their combined measured amount before committing any part of the
    # frontier. A reserved input can still physically be destroyed.
    losses=[e for e in events if e['op']=='physical_loss' and e['id'] in certificates]
    if losses:
        from economic_extension import physical
        totals={}
        for e in losses:
            p=e['params'];key=(p['location'],p['material'])
            totals[key]=totals.get(key,0)+p['quantity']
        for (location,material),quantity in totals.items():
            if quantity>physical(candidate.s['econ3'],location,material):
                raise InvalidEvent('incompatible combined physical observations; reconcile evidence')
    loss_ids={e['id'] for e in losses}
    edges=[]; blocked=set(errors)
    if errors: blocked.update(e['id'] for e in events)
    for i,a in enumerate(events):
        for b in events[:i]:
            if a['id'] in certificates and b['id'] in certificates and conflicts(certificates[a['id']],certificates[b['id']]):
                edges.append([a['id'],b['id']]);blocked.update((a['id'],b['id']))
    blocked.difference_update(loss_ids)
    accepted=[]
    execution=sorted(losses,key=lambda e:e['id'])+[e for e in events if e['id'] not in loss_ids]
    for e in execution:
        if e['id'] not in blocked:
            candidate.apply(e['id'],at,e['op'],**e['params']);accepted.append(e['id'])
    # apply replaces the state: reacquire the authoritative store afterwards.
    store=candidate.s['r9']
    for e in events:
        certificate=certificates.get(e['id'])
        if certificate:
            certificate={k:v for k,v in certificate.items() if k!='validation_reads'}
        store['requests'][e['id']]={'original':copy.deepcopy(e),'status':'unresolved' if e['id'] in blocked else 'committed',
            'original_digest':digest(e),
            'reason':errors.get(e['id'],'dependency conflict or unqualified peer' if e['id'] in blocked else None),
            'certificate':certificate}
    store['frontiers'].append({'at':at,'requests':[e['id'] for e in events],'edges':edges})
    candidate.s['clock']=at
    candidate._validate(candidate.s); world.s=candidate.s
    return {'committed':accepted,'deferred':sorted(blocked),'edges':edges,'errors':errors}

def grant(world,mandate_id,actor,operations,at,source_ref):
    """Explicit fixture authority installation; not proof of real legal authority."""
    if type(at) is not int or not mandate_id or not source_ref or not actor or not operations or not set(operations)<=(SUPPORTED|{'deny_unqualified'}):
        raise InvalidEvent('qualified actor, source and supported operation scope required')
    candidate=type(world)(state=world.s);ensure_store(candidate.s)
    if isinstance(world,CoreWorld) and actor not in candidate.s['actors']:
        raise InvalidEvent('mandate recipient must be an actual registered actor')
    if at<candidate.s['clock'] or mandate_id in candidate.s['r9']['mandates']:
        raise InvalidEvent('invalid mandate time/identity')
    candidate.s['r9']['mandates'][mandate_id]={'actor':actor,'operations':sorted(set(operations)),
                                             'effective_at':at,'source_ref':source_ref,'active':True}
    candidate.s['clock']=at;candidate._validate(candidate.s);world.s=candidate.s

def resolve(world,decision_id,request_id,at,mandate_id,actor,approve):
    if type(approve) is not bool or type(at) is not int or not decision_id:raise InvalidEvent('explicit decision identity, integer time and approve/deny required')
    payload={'id':decision_id,'request':request_id,'at':at,'mandate':mandate_id,'actor':actor,'approve':approve}
    candidate=type(world)(state=world.s);ensure_store(candidate.s); store=candidate.s['r9']
    if decision_id in store['decisions']:
        if store['decisions'][decision_id]['payload']!=payload:raise InvalidEvent('decision ID altered')
        return copy.deepcopy(store['decisions'][decision_id])
    request=store['requests'].get(request_id); mandate=store['mandates'].get(mandate_id)
    if not request or request['status']!='unresolved':raise InvalidEvent('no unresolved request')
    original=request['original']
    if request.get('original_digest',digest(original))!=digest(original):raise InvalidEvent('stored original request altered')
    if at<=candidate.s['clock'] or at<=original['at']:raise InvalidEvent('decision must be genuinely later')
    covered=mandate and (original['op'] in mandate['operations'] or (not approve and 'deny_unqualified' in mandate['operations']))
    if not mandate or not mandate['active'] or mandate['actor']!=actor or mandate['effective_at']>at or not covered:
        raise InvalidEvent('authority does not cover this decision')
    actual=None
    if approve:
        if original['op'] in {'physical_loss','record_work_milestone','make_intermediate','ast_record_player_action','ast_set_scene','record_player_action','set_scene'}:
            raise InvalidEvent('occurrence/evidence/player action needs a new specialist event, not delayed automatic approval')
        actual={'id':'r9:decision:'+decision_id,'at':at,'op':original['op'],'params':copy.deepcopy(original['params'])}
        # No parameter rewrite: expired work windows fail until a NEW request
        # with new evidence and prospective timings is submitted.
        observe(candidate.s,actual)
        candidate.apply(actual['id'],at,actual['op'],**actual['params'])
    store=candidate.s['r9'];store['requests'][request_id]['status']='approved_executed' if approve else 'denied'
    record={'payload':payload,'actual_event':actual,'original_request':request_id}
    store['decisions'][decision_id]=record;candidate.s['clock']=at
    candidate._validate(candidate.s);world.s=candidate.s
    return copy.deepcopy(record)
