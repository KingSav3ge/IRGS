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
from core_world import CoreWorld, CORE_OPS, GENRE_OPS

SUPPORTED = BASE_OPS | NEW_OPS | FAB_OPS | {'physical_loss'} | NATIVE_OPS | AST_OPS | CORE_OPS | GENRE_OPS
META = {'clock','journal','processed','_r6_eid','_r7_event_id'}

def plain(value):
    if isinstance(value, dict):
        return {k:plain(v) for k,v in dict.items(value)}
    # Flattening/cloning instrumentation is bookkeeping, not a domain read.
    if isinstance(value,list): return [plain(v) for v in list.__iter__(value)]
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


def _repath(value,path):
    """Retain held child references when list positions change."""
    if isinstance(value,TracedDict):
        value.path=path
        for key,child in dict.items(value):_repath(child,path+(str(key),))
    elif isinstance(value,TracedList):
        value.path=path
        for index,child in enumerate(list.__iter__(value)):_repath(child,path+(str(index),))


class TracedList(list):
    """Whole-list read dependencies, with writes only for actual mutator calls.

    Membership, indexing, order and length all retain the complete list as their
    read granularity. Standard mutations reserve the complete list as a write.
    Successful unoverridden C-level changes still have the actual-diff backstop.
    This is reviewed JSON-handler observation, not an arbitrary Python sandbox.
    """
    def __init__(self,data,trace,path):
        self.trace,self.path=trace,path
        list.__init__(self,(self.wrap(value,path+(str(index),))
                            for index,value in enumerate(list.__iter__(data))))
    def wrap(self,value,path):
        if isinstance(value,dict):return TracedDict(plain(value),self.trace,path)
        if isinstance(value,list):return TracedList(plain(value),self.trace,path)
        return value
    def read(self):self.trace.add(self.path)
    def write(self):self.read();self.trace.add(self.path,True)
    def reindex(self):
        for index,value in enumerate(list.__iter__(self)):_repath(value,self.path+(str(index),))
    def __iter__(self):self.read();return list.__iter__(self)
    def __reversed__(self):self.read();return list.__reversed__(self)
    def __len__(self):self.read();return list.__len__(self)
    def __getitem__(self,index):self.read();return list.__getitem__(self,index)
    def __contains__(self,value):self.read();return list.__contains__(self,value)
    def __eq__(self,other):self.read();return list.__eq__(self,other)
    def __ne__(self,other):self.read();return list.__ne__(self,other)
    def __lt__(self,other):self.read();return list.__lt__(self,other)
    def __le__(self,other):self.read();return list.__le__(self,other)
    def __gt__(self,other):self.read();return list.__gt__(self,other)
    def __ge__(self,other):self.read();return list.__ge__(self,other)
    def __repr__(self):self.read();return list.__repr__(self)
    def count(self,value):self.read();return list.count(self,value)
    def index(self,*args):self.read();return list.index(self,*args)
    def copy(self):self.read();return list.copy(self)
    def __add__(self,other):self.read();return list.__add__(self,other)
    def __radd__(self,other):self.read();return list.__add__(other,self)
    def __mul__(self,count):self.read();return list.__mul__(self,count)
    def __rmul__(self,count):self.read();return list.__mul__(self,count)
    def __setitem__(self,index,value):
        self.write()
        if isinstance(index,slice):value=[self.wrap(v,self.path) for v in value]
        else:value=self.wrap(value,self.path)
        list.__setitem__(self,index,value);self.reindex()
    def __delitem__(self,index):self.write();list.__delitem__(self,index);self.reindex()
    def append(self,value):
        self.write();list.append(self,self.wrap(value,self.path+(str(list.__len__(self)),)))
    def extend(self,values):
        self.write()
        if values is self:values=list.copy(self)
        list.extend(self,(self.wrap(value,self.path) for value in values));self.reindex()
    def insert(self,index,value):
        self.write();list.insert(self,index,self.wrap(value,self.path));self.reindex()
    def pop(self,index=-1):
        self.write();value=list.pop(self,index);self.reindex();return value
    def remove(self,value):self.write();list.remove(self,value);self.reindex()
    def clear(self):self.write();list.clear(self)
    def reverse(self):self.write();list.reverse(self);self.reindex()
    def sort(self,*args,**kwargs):self.write();list.sort(self,*args,**kwargs);self.reindex()
    def __iadd__(self,values):self.extend(values);return self
    def __imul__(self,count):self.write();list.__imul__(self,count);self.reindex();return self
    def __deepcopy__(self,memo):
        self.read()
        return copy.deepcopy(plain(self),memo)


class TracedDict(dict):
    def __init__(self,data,trace,path=()):
        self.trace,self.path=trace,path
        for k,v in dict.items(data): dict.__setitem__(self,k,self.wrap(v,path+(str(k),)))
    def wrap(self,v,path):
        if isinstance(v,dict): return TracedDict(plain(v),self.trace,path)
        if isinstance(v,list): return TracedList(plain(v),self.trace,path)
        return v
    def __getitem__(self,key):
        path=self.path+(str(key),)
        self.trace.add(path+('@exists',))
        value=dict.__getitem__(self,key)
        if not isinstance(value,dict): self.trace.add(path)
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
    def copy(self):
        # CPython's dict.copy/union/equality can read scalar values without
        # invoking __getitem__. Keep those decision reads explicitly visible.
        self.trace.add(self.path)
        return dict.copy(self)
    def _comparison_reads(self,other):
        self.trace.add(self.path)
        if isinstance(other,TracedDict):other.trace.add(other.path)
    def __eq__(self,other):
        self._comparison_reads(other);return dict.__eq__(self,other)
    def __ne__(self,other):
        self._comparison_reads(other);return dict.__ne__(self,other)
    def __or__(self,other):
        self._comparison_reads(other);return dict.__or__(self,other)
    def __ror__(self,other):
        self._comparison_reads(other);return dict.__ror__(self,other)
    def __ior__(self,other):
        if isinstance(other,TracedDict):other.trace.add(other.path)
        self.update(other);return self
    def clear(self):
        self.trace.add(self.path)
        if dict.__len__(self):self.trace.add(self.path,True)
        dict.clear(self)
    def popitem(self):
        self.trace.add(self.path)  # The selected item depends on insertion order.
        key,value=dict.popitem(self)
        self.trace.add(self.path+(str(key),),True)
        return key,value
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

def _backend(state):
    return (CoreWorld if state.get('profile') in ('IRGS-CORE-3.3','AST-CORE-3.3')
            else ReceiverWorld if 'r9_engine_bindings' in state
            else R7World if 'econ3' in state else World)


def observe_rejection(state,event):
    """Qualify a fresh rejected probe without converting scratch writes to effects.

    Both selected-backend executions must reject identically and leave their
    state unchanged. Unknown handlers, replay, normalization, mismatched errors
    and non-atomic failure are refused, never labelled a qualified rejection.
    This private evidence is not a successful execution certificate.
    """
    if event['op'] not in SUPPORTED:raise InvalidEvent('native/unknown handler not qualified')
    if event['id'] in state['processed']:raise InvalidEvent('processed event is not a fresh request')
    cls=_backend(state); snapshot=digest(state)
    errors=(InvalidEvent,AssertionError,KeyError,ValueError,TypeError)
    reference=cls(state=state)
    if digest(reference.s)!=snapshot:raise InvalidEvent('backend normalized the rejection snapshot')
    plain_error=None
    try:reference.apply(event['id'],event['at'],event['op'],**copy.deepcopy(event['params']))
    except errors as error:plain_error=error
    if plain_error is None:raise InvalidEvent('plain execution did not reject')
    if digest(reference.s)!=snapshot:raise InvalidEvent('rejected execution changed state')
    worker=cls(state=state);trace=Trace();worker.s=TracedDict(worker.s,trace)
    traced_error=None
    try:worker.apply(event['id'],event['at'],event['op'],**copy.deepcopy(event['params']))
    except errors as error:traced_error=error
    if traced_error is None:raise InvalidEvent('instrumented execution did not reject')
    if digest(plain(worker.s))!=snapshot:raise InvalidEvent('instrumented rejection changed state')
    if type(traced_error) is not type(plain_error) or traced_error.args!=plain_error.args:
        raise InvalidEvent('instrumented rejection differs from plain execution')
    return {'event':copy.deepcopy(event),'snapshot':snapshot,'code':code_identity(),
            'backend':cls.__name__,'profile':state.get('profile','legacy_research_fixture'),
            'status':'rejected_no_effects','successful_certificate':False,
            'rejection_type':type(plain_error).__name__,'post_state':snapshot,
            'reads':effect_paths(trace.reads),'writes':[],
            'attempted_writes':effect_paths(trace.writes),
            'validation_reads':sorted(trace.validation_reads)}

def observe(state,event):
    if event['op'] not in SUPPORTED: raise InvalidEvent('native/unknown handler not qualified')
    if event['id'] in state['processed']:raise InvalidEvent('processed event is not a fresh request')
    cls=_backend(state)
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
    certificates={}; errors={}; rejected={}; refusals={}
    for e in events:
        try: certificates[e['id']]=observe(candidate.s,e)
        except (InvalidEvent,AssertionError,KeyError,ValueError,TypeError) as err:
            errors[e['id']]=str(err)
            try:rejected[e['id']]=observe_rejection(candidate.s,e)
            except (InvalidEvent,AssertionError,KeyError,ValueError,TypeError) as refusal:
                refusals[e['id']]=str(refusal)
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
    evidence={**certificates,**rejected}
    for i,a in enumerate(events):
        for b in events[:i]:
            if a['id'] in evidence and b['id'] in evidence and conflicts(evidence[a['id']],evidence[b['id']]):
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
        certificate=evidence.get(e['id'])
        if certificate:
            certificate={k:v for k,v in certificate.items() if k!='validation_reads'}
        store['requests'][e['id']]={'original':copy.deepcopy(e),'status':'unresolved' if e['id'] in blocked else 'committed',
            'original_digest':digest(e),
            'reason':errors.get(e['id'],'dependency conflict or unqualified peer' if e['id'] in blocked else None),
            'certificate':certificate,
            'dependency_status':('qualified_successful_probe' if e['id'] in certificates
                                 else 'qualified_rejected_probe' if e['id'] in rejected else 'unqualified'),
            'dependency_refusal':refusals.get(e['id'])}
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
