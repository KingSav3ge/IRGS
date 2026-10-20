"""IRGS Core v3.3 R1: limited executable reference model, NOT an adopted game engine.

This contract fixture tests actual atomic owner writes, event replay, population
conservation, distinct legal/physical/social state, and bounded military workflows.
It deliberately does not simulate training efficacy, battlefield probabilities,
medical recovery, population ecology, or calibrated military readiness.
"""
from __future__ import annotations
import copy, hashlib, json
from economic_extension import ECON_OPS, validate_econ, preflight_econ, operate_econ, economy_fixture


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def digest(obj):
    return hashlib.sha256(canon(obj).encode()).hexdigest()


class InvalidEvent(Exception):
    pass


class World:
    def __init__(self, initial=None, state=None):
        self.origin = copy.deepcopy(initial) if initial is not None else None
        self.s = copy.deepcopy(state if state is not None else initial)
        if self.s is None:
            raise ValueError('Initial world required')
        self._validate(self.s)

    @classmethod
    def load(cls, serialized):
        return cls(state=json.loads(serialized))

    def save(self):
        return canon(self.s)

    def checksum(self):
        return digest(self.s)

    def _validate(self, s):
        assert s['clock'] >= 0
        assert s['population']['residual'] >= 0
        assert len(s['actors']) + s['population']['residual'] == s['population']['baseline'], 'population conservation'
        allmembers = list(s['formations']['army']['members'])
        assert len(set(allmembers)) == len(allmembers), 'duplicate military members'
        assert all(pid in s['actors'] for pid in allmembers)
        assert all(set(rec['members']).issubset(s['actors']) for rec in s['households'].values())
        assert all(q >= 0 and isinstance(q,int) for loc in s['equipment'].values() for q in loc.values()), 'negative equipment'
        assert sum(loc.get('kit',0) for loc in s['equipment'].values()) == s['kit_baseline'], 'equipment conservation'
        assert all(v >= 0 and isinstance(v,int) for v in s['cash'].values()), 'negative actual cash'
        assert sum(s['cash'].values()) == s['cash_baseline'], 'cash conservation'
        assert all(v >= 0 for v in s['wage_due'].values()), 'negative earned pay'
        assert all(e['id'] in s['processed'] for e in s['journal'])
        assert all(s['processed'][e['id']] == digest(e) for e in s['journal']), 'journal payload integrity'
        assert len({q['id'] for q in s['pending']}) == len(s['pending'])
        assert len({e['id'] for e in s['journal']}) == len(s['journal'])
        for pid, a in s['actors'].items():
            assert a['id'] == pid
            assert a['custody'] is None or isinstance(a['custody'],dict)
            assert 'person' not in s['equipment'].get(pid, {})
        validate_econ(s)
        for pid, shifts in s['commitments'].items():
            assert pid in s['actors']
            for i,(start,end,role) in enumerate(shifts):
                assert start < end
                for st,en,_ in shifts[:i]:
                    assert not (st < end and start < en), 'double-booked individual'

    def schedule(self, eid, at, op, **params):
        assert at >= self.s['clock'], 'past event scheduling forbidden'
        ev={'id':eid,'at':at,'op':op,'params':copy.deepcopy(params)}
        if eid in self.s['processed'] or eid in {q['id'] for q in self.s['pending']}:
            raise InvalidEvent('scheduled ID collision')
        self.s['pending'].append(ev)
        self.s['pending'].sort(key=lambda x:(x['at'],x['id']))
        self._validate(self.s)

    def _validate_concurrent_requests(self, group):
        """Preflight known shared constraints. Unknown same-time disputes need a selected policy."""
        bysource={}; wage_claims={}; tax_claims={}; kits=0; shifts={}; exclusive=set()
        for e in group:
            op,p=e['op'],e['params']
            if op in ('transfer_cash','pay'):
                bysource[p['from']]=bysource.get(p['from'],0)+p['amount']
            if op=='pay':
                wage_claims[p['person']]=wage_claims.get(p['person'],0)+p['amount']
            if op=='pay_tax' and 'econ3' in self.s:
                tax=self.s['econ3']['tax_claims'].get(p['tax_id'])
                if tax is None: raise InvalidEvent('tax claim not present at pre-event frontier')
                payer=tax['payer']
                bysource[payer]=bysource.get(payer,0)+p['amount']
                tax_claims[p['tax_id']]=tax_claims.get(p['tax_id'],0)+p['amount']
            if op=='issue_kits':
                kits+=len(p['persons'])
            if op=='commit_shift':
                shifts.setdefault(p['person'],[]).append((p['start'],p['end']))
            if op in ('capture','escape','legal_status_change'):
                token=('person_control',p['person']) if op in ('capture','escape') else ('law',p['person'],p['jurisdiction'])
                if token in exclusive: raise InvalidEvent('unresolved same-time competing person/legal writes')
                exclusive.add(token)
            if op in ('issue_order','receive_order'):
                token=('order',p['order_id'])
                if token in exclusive: raise InvalidEvent('same-time order creation and delivery needs causal staging')
                exclusive.add(token)
        # Reject only competing causal operations on the SAME referenced record.
        # Independent taxation, transportation and jobs may share an epoch.
        ops={e['op'] for e in group}
        if 'authorize_mobilization' in ops and {'enroll','enroll_from_residual'} & ops:
            raise InvalidEvent('a new mandate cannot create eligible mobilization at the same frontier')
        created_tax={e['params']['tax_id'] for e in group if e['op']=='assess_tax'}
        created_ship={e['params']['shipment_id'] for e in group if e['op']=='dispatch_stock'}
        created_order={e['params']['order_id'] for e in group if e['op']=='issue_order'}
        finished_jobs={e['params']['job_id'] for e in group if e['op'] in ('complete_job','interrupt_job')}
        due_changed={e['params']['person'] for e in group if e['op']=='accrue_pay'}
        for e in group:
            p=e['params'];op=e['op']
            if op=='pay_tax' and p['tax_id'] in created_tax:
                raise InvalidEvent('same-time newly assessed tax is not an existing claim')
            if op=='receive_stock' and p['shipment_id'] in created_ship:
                raise InvalidEvent('same-time dispatch cannot also arrive')
            if op=='receive_order' and p['order_id'] in created_order:
                raise InvalidEvent('same-time newly issued order is not received')
            if op=='accrue_job_wages' and p['job_id'] in finished_jobs:
                raise InvalidEvent('same-time job settlement is not a prior completed job')
            if op=='pay' and p['person'] in due_changed:
                raise InvalidEvent('simultaneous due/pay to one person requires qualified claim selection')
            if op=='pay':
                for wage in group:
                    if wage['op']=='accrue_job_wages':
                        job=self.s.get('econ3',{}).get('completed_jobs',{}).get(wage['params']['job_id'])
                        if job and p['person'] in job['workers']:
                            raise InvalidEvent('simultaneous job wage accrual/payment requires claim staging')
        for e in group:
            if e['op'] not in ('release_shift','commit_shift'): continue
            p=e['params']; st,en=p['start'],p['end']; pid=p['person']
            for other in group:
                if other is e: continue
                q=other['params']; op=other['op']
                if op=='start_job' and pid in q['workers'] and st<q['end'] and q['start']<en:
                    raise InvalidEvent('same-frontier assignment and execution needs staged decision')
                if op in ('release_shift','commit_shift') and pid==q['person'] and st<q['end'] and q['start']<en:
                    raise InvalidEvent('same-frontier competing shift writes need authorized ordering')
        for name,qty in bysource.items():
            if qty>self.s['cash'][name]:
                raise InvalidEvent('same-time cash contention requires explicit allocation authority')
        for person,amount in wage_claims.items():
            if amount>self.s['wage_due'].get(person,0):
                raise InvalidEvent('same-time claim on unpaid wages requires resolution')
        for taxid,amount in tax_claims.items():
            claim=self.s['econ3']['tax_claims'][taxid]
            if amount>claim['assessed']-claim['paid']:
                raise InvalidEvent('same-time payment exceeds one tax claim')
        if kits>self.s['equipment']['depot'].get('kit',0):
            raise InvalidEvent('same-time equipment contention requires explicit allocation authority')
        for person,periods in shifts.items():
            for i,(st,en) in enumerate(periods):
                for st2,en2 in periods[:i]:
                    if st < en2 and st2 < en:
                        raise InvalidEvent('same-time incompatible duty demands require decision')
        try:
            preflight_econ(self.s,group)
        except (AssertionError, ValueError, KeyError) as err:
            raise InvalidEvent(f'economic epoch: {err}') from err
        if sum(1 for e in group if e['op']=='simultaneous_exchange')>1:
            raise InvalidEvent('simultaneous engagements require common pre-event batch')

    def run_until(self, through):
        while True:
            eligible=[e for e in self.s['pending'] if e['at']<=through]
            if not eligible: break
            at=min(e['at'] for e in eligible)
            group=sorted([e for e in eligible if e['at']==at],key=lambda x:x['id'])
            self._validate_concurrent_requests(group)
            # All-or-nothing at each frontier: never leave a partial same-time batch.
            candidate=World(state=self.s)
            for ev in group:
                candidate.apply(ev['id'],ev['at'],ev['op'],**ev['params'])
            ids={x['id'] for x in group}
            candidate.s['pending']=[x for x in candidate.s['pending'] if x['id'] not in ids]
            candidate._validate(candidate.s)
            self.s=candidate.s
        if through > self.s['clock']:
            self.apply(f'frontier:{through}',through,'review_no_change')

    def apply(self, eid, at, op, **params):
        # The world owns committed payloads. Callers may reuse or mutate their
        # input structures after a submission without changing saved history.
        params = copy.deepcopy(params)
        ev = {'id':eid,'at':at,'op':op,'params':params}
        signature = digest(ev)
        current = self.s['processed'].get(eid)
        if current is not None:
            if current != signature: raise InvalidEvent('event ID reused with altered payload')
            return False
        if at < self.s['clock']: raise InvalidEvent('backdated event without rollback')
        s = copy.deepcopy(self.s)
        try:
            self._operate(s, at, op, params)
            s['clock'] = at
            s['processed'][eid] = signature
            s['journal'].append(ev)
            self._validate(s)
        except (AssertionError, KeyError, ValueError, TypeError, IndexError) as err:
            raise InvalidEvent(f'{op}: {err}') from err
        self.s = s
        return True

    def _operate(self,s,at,op,p):
        if op in ECON_OPS:
            operate_econ(s,at,op,p)
        elif op == 'review_no_change':
            pass
        elif op == 'authorize_mobilization':
            assert 'mobilization' not in s['gov']
            s['gov']['mobilization'] = {'mandate':p['mandate'],'target':p['target'],'at':at,'enrolled':0}
        elif op == 'enroll':
            assert 'mobilization' in s['gov']
            person = p['person']; army = s['formations']['army']['members']
            assert person in s['actors'] and person not in army
            assert s['gov']['mobilization']['enrolled'] < s['gov']['mobilization']['target']
            army.append(person); s['gov']['mobilization']['enrolled'] += 1
            s['actors'][person]['enlisted'] = True
        elif op == 'enroll_from_residual':
            assert 'mobilization' in s['gov']
            count = p['count']; assert isinstance(count,int) and count > 0
            assert s['population']['residual'] >= count
            assert s['gov']['mobilization']['enrolled']+count <= s['gov']['mobilization']['target']
            assert p['eligible_attestation'] != '' and p['source_cohort'] == s['population']['cohort_id']
            for i in range(count):
                person = f"{p['batch_id']}:{i:04d}"
                assert person not in s['actors']
                s['actors'][person] = actor(person)
                s['actors'][person]['enlisted'] = True
                s['formations']['army']['members'].append(person)
            s['population']['residual'] -= count
            s['gov']['mobilization']['enrolled'] += count
        elif op == 'attest_training':
            assert p['external_training_evidence'] and p['adapter_ref']
            members = set(s['formations']['army']['members'])
            for pid in p['persons']:
                assert pid in members
                s['actors'][pid]['training_evidence'] = p['external_training_evidence']
        elif op == 'issue_kits':
            for pid in p['persons']:
                assert pid in s['formations']['army']['members']
                assert s['equipment']['depot'].get('kit',0) >= 1
                assert s['equipment'].get(pid,{}).get('kit',0)==0
                s['equipment']['depot']['kit'] -= 1
                s['equipment'].setdefault(pid, {})['kit'] = 1
        elif op == 'commit_shift':
            pid=p['person']; assert pid in s['actors']
            st,en=p['start'],p['end']; assert st < en and at <= st, 'no retrospective commitments'
            shifts=s['commitments'].setdefault(pid,[])
            assert all(not (x < en and st < y) for x,y,_ in shifts)
            shifts.append([st,en,p['role']])
        elif op == 'authorize_budget':
            assert p['amount'] >= 0
            s['budgets'][p['name']] = {'authorized':p['amount'],'claimed_at':at}
        elif op == 'transfer_cash':
            amount=p['amount']; assert amount>0 and isinstance(amount,int)
            assert s['cash'][p['from']] >= amount
            s['cash'][p['from']] -= amount
            s['cash'][p['to']] += amount
        elif op == 'accrue_pay':
            assert p['amount']>0 and p['person'] in s['actors']
            s['wage_due'][p['person']] = s['wage_due'].get(p['person'],0)+p['amount']
        elif op == 'pay':
            amount=p['amount']; pid=p['person']
            assert amount>0 and s['wage_due'].get(pid,0)>=amount
            assert s['cash'][p['from']]>=amount
            s['cash'][p['from']]-=amount; s['cash'][pid]=s['cash'].get(pid,0)+amount
            s['wage_due'][pid]-=amount
        elif op == 'allocate_competing_kits':
            # A single transparent allocation transaction; priority is a fixture policy, not default IRGS law.
            assert p['resolution_policy']=='priority_then_request_id'
            requests=sorted(p['requests'],key=lambda r:(r['priority'],r['id']))
            audit=[]
            for req in requests:
                assert req['qty']>0
                available=s['equipment']['depot'].get('kit',0)
                delivered=req['qty'] if available >= req['qty'] else 0  # all-or-nothing fixture
                if delivered:
                    s['equipment']['depot']['kit']-=delivered
                    s['equipment'].setdefault(req['to'],{})['kit']=s['equipment'].get(req['to'],{}).get('kit',0)+delivered
                audit.append({'id':req['id'],'requested':req['qty'],'delivered':delivered})
            s['allocation_audit'].append({'at':at,'requests':audit,'policy':p['resolution_policy']})
        elif op == 'issue_order':
            oid=p['order_id']; assert oid not in s['orders']
            s['orders'][oid]={'issued_at':at,'deadline':p['deadline'],'recipient':p['recipient'],'received_at':None,'executed':False}
        elif op == 'receive_order':
            oid=p['order_id']; rec=s['orders'][oid]
            assert rec['received_at'] is None
            rec['received_at']=at
        elif op == 'execute_order':
            rec=s['orders'][p['order_id']]
            assert rec['received_at'] is not None and rec['received_at']<=at<=rec['deadline']
            rec['executed']=True
        elif op == 'capture':
            pid=p['person']; assert pid in s['actors']
            s['actors'][pid]['custody']={'by':p['by'],'at':at,'location':p['location']}
            s['actors'][pid]['location']=p['location']
        elif op == 'escape':
            pid=p['person']; assert pid in s['actors']
            s['actors'][pid]['custody']=None; s['actors'][pid]['location']=p['location']
        elif op == 'report':
            assert p['recipient'] != ''
            s['reports'].append({'at':at,'person':p['person'],'recipient':p['recipient'],'message':p['message']})
        elif op == 'propose_release':
            s['undertakings'].append({'subject':p['person'],'claimant':p['by'],'at':at,'terms':p['terms']})
        elif op == 'legal_status_change':
            assert p['authorized_decision_ref'] and p['jurisdiction'] and p['effective_at']==at
            s['gov']['legal_status'].setdefault(p['person'],{})[p['jurisdiction']]={'status':p['to'],'effective_at':at,'decision_ref':p['authorized_decision_ref']}
        elif op == 'recognize_status':
            assert p['audience'] and p['jurisdiction']
            s['recognitions'].append({'at':at,'person':p['person'],'audience':p['audience'],'jurisdiction':p['jurisdiction'],'claimed_status':p['claimed_status']})
        elif op == 'person_claim':
            # Institutional/economic claim ABOUT a person; never a transfer of that person as equipment.
            assert p['subject'] in s['actors']
            s['person_claims'].append({'at':at, 'subject':p['subject'],'claimant':p['claimant'],'basis':p['basis'],'disputed':p['disputed']})
        elif op == 'simultaneous_exchange':
            assert p['selected_effect_adapter']=='fixture_effects_only'
            pre=copy.deepcopy(s['actors'])
            for hit in p['attacks']:
                assert pre[hit['from']]['disabled'] is False
                assert pre[hit['to']]['disabled'] is False
                assert pre[hit['from']]['ammo']>=hit['ammo_used']>0
                assert hit['effect'] in ('disable','none')
            used={}
            for hit in p['attacks']:
                used[hit['from']]=used.get(hit['from'],0)+hit['ammo_used']
            for pid,quantity in used.items():
                assert pre[pid]['ammo']>=quantity
                s['actors'][pid]['ammo']-=quantity
            for hit in p['attacks']:
                if hit['effect']=='disable': s['actors'][hit['to']]['disabled']=True
            s['engagements'].append({'id':p['engagement_id'],'at':at,'attacks':p['attacks'],'adapter':p['selected_effect_adapter']})
        elif op == 'summarize_engagement':
            eid=p['engagement_id']; assert eid not in s['engagement_summaries']
            engagements=[e for e in s['engagements'] if e['id']==eid]
            assert len(engagements)==1
            s['engagement_summaries'][eid]={'at':at,'source_engagement_id':eid,'disabled_targets':sorted({a['to'] for a in engagements[0]['attacks'] if a['effect']=='disable'}),'writes_to_actor_state':False}
        elif op == 'demobilize':
            pid=p['person']; members=s['formations']['army']['members']
            assert pid in members
            members.remove(pid); s['actors'][pid]['enlisted']=False
            # Transfer actual issued kit to the specified depot, if still present.
            held=s['equipment'].get(pid,{}).get('kit',0)
            if held:
                s['equipment'][pid]['kit']-=held; s['equipment']['depot']['kit']+=held
        else:
            raise ValueError('unknown operation: '+op)

    def ready_subset(self, start, end):
        # Intentionally *not* a universal mission-ready percentage/model.
        result=[]
        for pid in self.s['formations']['army']['members']:
            a=self.s['actors'][pid]
            occupied=any(st<end and start<en for st,en,_ in self.s['commitments'].get(pid,[]))
            if a['training_evidence'] and self.s['equipment'].get(pid,{}).get('kit',0)>0 and not a['disabled'] and not occupied:
                result.append(pid)
        return result

    def display_population(self):
        return {'residual_unnamed':self.s['population']['residual'], 'named':len(self.s['actors']), 'total':len(self.s['actors'])+self.s['population']['residual'], 'enlisted_memberships':len(self.s['formations']['army']['members'])}


def actor(name, location='home'):
    return {'id':name, 'location':location,'custody':None,'enlisted':False,
            'training_evidence':None,'disabled':False,'ammo':0}


def initial_world():
    s={'campaign_id':'TEST-MOB-ONLY','clock':0,
       'population':{'baseline':1200,'residual':1198,'cohort_id':'region-residents-01'},
       'actors': {'caregiver-1':actor('caregiver-1'), 'person-B':actor('person-B')},
       'formations': {'army':{'members':[]}},
       'households': {'house-1':{'members':['caregiver-1'],'care_commitment':'care-shift-1'}},
       'equipment': {'depot':{'kit':300}},'kit_baseline':300,
       'cash':{'treasury':1000,'army':0,'caregiver-1':0,'person-B':0}, 'cash_baseline':1000,
       'wage_due':{},'budgets':{}, 'gov':{'legal_status':{}},
       'commitments': {'caregiver-1':[[8,12,'household_care']]},
       'orders':{},'reports':[], 'recognitions':[], 'person_claims':[], 'undertakings':[],
       'allocation_audit':[], 'engagements':[], 'engagement_summaries':{},
       'processed':{},'journal':[], 'pending':[]}
    return World(initial=s)
