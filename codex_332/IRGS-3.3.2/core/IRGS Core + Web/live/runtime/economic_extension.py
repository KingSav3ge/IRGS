"""IRGS R3 proposed bounded economic / household work adapter.

Not an adopted or production engine. Each rate and site is a synthetic fixture
parameter, not a universal agricultural / labor / care / economic rule.
"""
from __future__ import annotations
import copy

ECON_OPS = {
 'release_shift','start_job','complete_job','interrupt_job',
 'complete_care','audit_needs','provision_meals',
 'dispatch_stock','receive_stock','assess_tax','pay_tax','accrue_job_wages'
}


def covered_shift(s, pid, start, end, role):
    return any(a <= start and end <= b and r == role
               for a,b,r in s['commitments'].get(pid,[]))


def physical(e, loc, material):
    return e['stocks'].get(loc,{}).get(material,0)


def reserved(e, loc, material):
    return sum(job['reserved_inputs'].get(material,0)
               for job in e['active_jobs'].values() if job['site']==loc)


def free(e, loc, material):
    return physical(e,loc,material)-reserved(e,loc,material)


def total(e, material):
    return sum(d.get(material,0) for d in e['stocks'].values())


def validate_econ(s):
    if 'econ3' not in s: return
    e=s['econ3']
    assert set(e['opening'])==set(e['produced'])==set(e['consumed'])
    for loc, materials in e['stocks'].items():
        assert isinstance(loc,str) and loc
        for material,q in materials.items():
            assert material in e['opening'] and type(q) is int and q>=0, 'stock nonnegative integer'
    losses=e.get('losses',{})
    assert all(m in e['opening'] and type(q) is int and q>=0 for m,q in losses.items()), 'invalid loss ledger'
    for material,opening in e['opening'].items():
        assert type(opening) is int and opening>=0
        assert type(e['produced'][material]) is int and e['produced'][material]>=0
        assert type(e['consumed'][material]) is int and e['consumed'][material]>=0
        assert total(e,material)==opening+e['produced'][material]-e['consumed'][material]-losses.get(material,0), 'material stock identity'
    for jobid,job in e['active_jobs'].items():
        assert jobid not in e['completed_jobs']
        assert job['start'] < job['end']
        assert job['site'] in e['sites']
        assert all(pid in s['actors'] for pid in job['workers'])
        assert len(set(job['workers']))==len(job['workers'])
        assert all(type(q) is int and q>=0 for q in job['reserved_inputs'].values())
    for loc,materials in e['stocks'].items():
        for material in materials:
            assert free(e,loc,material)>=0, 'unbacked reservation'
    for jid,rec in e['completed_jobs'].items():
        assert jid not in e['active_jobs']
        assert rec['hours_done']>=0
        assert rec['hours_done']<=rec['hours_planned']
    assert len(set(e['shipments']))==len(e['shipments'])
    for sid,shipment in e['shipments'].items():
        if shipment['status']=='transit':
            assert physical(e,'transit:'+sid,shipment['material'])==shipment['quantity']
        assert shipment['quantity']>0 and shipment['arrival_not_before']>shipment['departed_at']
    for item in e['care_delivered']:
        assert item['person'] in s['actors'] and item['start']<item['end']
    assert len(e['needs_audit'])==len({a['audit_id'] for a in e['needs_audit']})
    for pid,abilities in e['qualifications'].items():
        assert pid in s['actors'] and isinstance(abilities,list)
    for claim in e['tax_claims'].values():
        assert claim['assessed']>=claim['paid']>=0


def preflight_econ(s, group):
    if 'econ3' not in s: return
    e=s['econ3']; claims={}; new_jobs=[]; jobs_to_finish=set(); care=[]
    for ev in group:
        op,p=ev['op'],ev['params']
        if op=='start_job':
            spec=e['recipes'].get(p['recipe_id'])
            if not spec: continue
            h=(p['end']-p['start'])*len(p['workers'])
            for material,rate in spec['inputs'].items():
                token=(spec['site'],material)
                claims[token]=claims.get(token,0)+h*rate
            new_jobs.append((spec['site'],p['start'],p['end'],p['workers']))
        elif op=='dispatch_stock':
            token=(p['from'],p['material'])
            claims[token]=claims.get(token,0)+p['quantity']
        elif op=='provision_meals':
            token=(p['household'],'meal')
            claims[token]=claims.get(token,0)+p['quantity']
        elif op in ('complete_job','interrupt_job'):
            jid=p['job_id']
            if jid in jobs_to_finish: raise ValueError('competing settlement of same job')
            jobs_to_finish.add(jid)
        elif op=='complete_care':
            care.append((p['person'],p['start'],p['end']))
    for (loc,material),qty in claims.items():
        if qty>free(e,loc,material):
            raise ValueError('unresolved same-time stock contention; no output from due events counts as prior stock')
    for i,(loc,st,en,people) in enumerate(new_jobs):
        for loc2,st2,en2,people2 in new_jobs[:i]:
            if st<en2 and st2<en and set(people)&set(people2):
                raise ValueError('same-time competing worker claims')
    # Aggregate capacity for every overlapping time segment, not merely pairs.
    # Three one-person jobs can exceed a two-person site without any pair doing so.
    for loc in {x[0] for x in new_jobs}:
        at_site=[x for x in new_jobs if x[0]==loc]
        checkpoints=sorted({t for _,st,en,_ in at_site for t in (st,en)})
        for t in checkpoints[:-1]:
            seats=sum(len(workers) for _,st,en,workers in at_site if st<=t<en)
            if seats>e['sites'][loc]['workers_capacity']:
                raise ValueError('same-time aggregate workstation contention')
    for i,(person,st,en) in enumerate(care):
        for person2,st2,en2 in care[:i]:
            if person==person2 and st<en2 and st2<en:
                raise ValueError('same-time duplicate care work')


def _work_settle(s,e,job_id,at,interrupted):
    assert job_id in e['active_jobs'], 'not an active job'
    job=e['active_jobs'][job_id]
    assert job.get('status','active')=='active', 'disrupted job cannot complete without requalification'
    assert job['start'] < at <= job['end']
    if not interrupted: assert at==job['end'], 'job cannot complete early'
    for pid in job['workers']:
        assert not s['actors'][pid]['disabled'], 'person now disabled: must record interruption rather than full completion'
        assert s['actors'][pid]['location']==job['site'], 'worker absent from worksite'
    hours=(at-job['start'])*len(job['workers'])
    spec=e['recipes'][job['recipe_id']]
    for mat,rate in spec['inputs'].items():
        used=rate*hours
        assert job['reserved_inputs'][mat]>=used
        e['stocks'][job['site']][mat]-=used
        e['consumed'][mat]+=used
    for mat,rate in spec['outputs'].items():
        qty=rate*hours
        e['stocks'][job['site']][mat]=physical(e,job['site'],mat)+qty
        e['produced'][mat]+=qty
    e['completed_jobs'][job_id]={**job,'hours_planned':(job['end']-job['start'])*len(job['workers']),
                                  'hours_done':hours,'settled_at':at,'interrupted':interrupted,
                                  'wages_accrued_for':[]}
    del e['active_jobs'][job_id]


def operate_econ(s,at,op,p):
    assert 'econ3' in s, 'economic profile not selected'
    e=s['econ3']
    if op=='release_shift':
        pid,st,en,role=p['person'],p['start'],p['end'],p['role']
        assert at<=st, 'cannot cancel already begun work without settlement'
        assert p['authority_ref'], 'specific competent instruction required'
        match=[x for x in s['commitments'].get(pid,[]) if x==[st,en,role]]
        assert len(match)==1, 'exact commitment not found'
        assert not any(pid in j['workers'] and j['start']<en and st<j['end'] for j in e['active_jobs'].values())
        s['commitments'][pid].remove(match[0]);e['released_shifts'].append({'person':pid,'start':st,'end':en,'role':role,'at':at,'authority_ref':p['authority_ref']})
    elif op=='start_job':
        jid=p['job_id']; assert jid not in e['active_jobs'] and jid not in e['completed_jobs']
        rid=p['recipe_id']; spec=e['recipes'][rid]
        start,end=p['start'],p['end']; assert start==at and type(start) is int and type(end) is int and end>start
        people=p['workers'];assert people and len(set(people))==len(people)
        site=spec['site']; assert len(people)<=e['sites'][site]['workers_capacity']
        for pid in people:
            assert pid in s['actors'] and rid in e['qualifications'].get(pid,[]), 'qualified worker necessary'
            assert s['actors'][pid]['location']==site and not s['actors'][pid]['disabled']
            assert covered_shift(s,pid,start,end,'work:'+rid), 'commitment matching work required'
        for existing in e['active_jobs'].values():
            if start<existing['end'] and existing['start']<end:
                assert not(set(people)&set(existing['workers'])), 'worker already serving another job'
                if existing['site']==site:
                    assert len(people)+len(existing['workers'])<=e['sites'][site]['workers_capacity']
        hours=(end-start)*len(people)
        inputs={mat:per_hour*hours for mat,per_hour in spec['inputs'].items()}
        assert all(free(e,site,m)>=q for m,q in inputs.items()), 'physical free inputs at start required'
        e['active_jobs'][jid]={'recipe_id':rid,'site':site,'workers':list(people),'start':start,'end':end,'reserved_inputs':inputs}
    elif op in ('complete_job','interrupt_job'):
        _work_settle(s,e,p['job_id'],at,op=='interrupt_job')
    elif op=='complete_care':
        pid,house,st,en=p['person'],p['household'],p['start'],p['end']
        assert at==en and st<en
        assert 'care' in e['qualifications'].get(pid,[])
        assert pid in s['actors'] and not s['actors'][pid]['disabled'] and s['actors'][pid]['location']==house
        assert covered_shift(s,pid,st,en,'household_care')
        assert house in s['households'] and s['households'][house]['members']
        assert not any(x['person']==pid and st<x['end'] and x['start']<en for x in e['care_delivered'])
        e['care_delivered'].append({'person':pid,'household':house,'start':st,'end':en,'at':at})
    elif op=='provision_meals':
        house=p['household']; qty=p['quantity']
        assert type(qty) is int and qty>0 and house in s['households']
        assert free(e,house,'meal')>=qty
        e['stocks'][house]['meal']-=qty;e['consumed']['meal']+=qty
        e['meals_delivered'][house]=e['meals_delivered'].get(house,0)+qty
        e['provision_audit'].append({'at':at,'household':house,'actual_meals':qty})
    elif op=='audit_needs':
        aid=p['audit_id']; house=p['household'];need=e['needs'][house]
        assert not any(x['audit_id']==aid for x in e['needs_audit'])
        assert at>need['care_end'] and at>=need['meal_deadline'], 'audit due after assessed window'
        coverage=set()
        for record in e['care_delivered']:
            if record['household']==house:
                coverage.update(range(max(record['start'],need['care_start']),min(record['end'],need['care_end'])))
        actual_care=len(coverage)
        requested=need['care_required_hours']; meals=e['meals_delivered'].get(house,0)
        e['needs_audit'].append({'audit_id':aid,'at':at,'household':house,
          'care_required':requested,'actual_care_hours':actual_care,'unmet_care_hours':max(0,requested-actual_care),
          'meals_required':need['meal_required'],'meals_served':meals,
          'unmet_meals':max(0,need['meal_required']-meals), 'records_only_not_automatic_injury':True})
    elif op=='dispatch_stock':
        sid=p['shipment_id']; qty=p['quantity'];mat=p['material'];from_loc=p['from'];dest=p['to']
        assert sid not in e['shipments'] and type(qty) is int and qty>0
        assert p['route_ref'] and type(p['minimum_transit']) is int and p['minimum_transit']>=1
        assert from_loc != dest and free(e,from_loc,mat)>=qty
        e['stocks'][from_loc][mat]-=qty
        e['stocks'].setdefault('transit:'+sid,{})[mat]=qty
        e['shipments'][sid]={'material':mat,'quantity':qty,'from':from_loc,'to':dest,
            'route_ref':p['route_ref'],'departed_at':at,'arrival_not_before':at+p['minimum_transit'],'status':'transit'}
    elif op=='receive_stock':
        sid=p['shipment_id']; ship=e['shipments'][sid]
        assert ship['status']=='transit' and at>=ship['arrival_not_before']
        mat=ship['material']; q=ship['quantity']
        assert physical(e,'transit:'+sid,mat)==q
        e['stocks']['transit:'+sid][mat]-=q
        e['stocks'].setdefault(ship['to'],{})[mat]=physical(e,ship['to'],mat)+q
        ship['status']='received';ship['received_at']=at
    elif op=='assess_tax':
        tid=p['tax_id']; amt=p['amount']
        assert tid not in e['tax_claims'] and type(amt) is int and amt>=0
        assert p['payer'] in s['cash'] and p['authority_ref'] and p['basis_ref']
        e['tax_claims'][tid]={'payer':p['payer'],'assessed':amt,'paid':0,'assessed_at':at,
            'authority_ref':p['authority_ref'],'basis_ref':p['basis_ref']}
    elif op=='pay_tax':
        rec=e['tax_claims'][p['tax_id']];amt=p['amount']
        assert type(amt) is int and amt>0 and rec['assessed']-rec['paid']>=amt
        assert s['cash'][rec['payer']]>=amt
        s['cash'][rec['payer']]-=amt;s['cash']['treasury']+=amt
        rec['paid']+=amt
    elif op=='accrue_job_wages':
        rec=e['completed_jobs'][p['job_id']];rate=p['rate']
        assert type(rate) is int and rate>=0 and p['wage_agreement_ref']
        assert not rec['wages_accrued_for']
        actual_hours_each=rec['hours_done']//len(rec['workers'])
        for pid in rec['workers']:
            amt=actual_hours_each*rate
            s['wage_due'][pid]=s['wage_due'].get(pid,0)+amt
            rec['wages_accrued_for'].append({'person':pid,'amount':amt,'basis':p['wage_agreement_ref']})
    else:
        raise ValueError('unknown econ op')


def economy_fixture(base):
    """Seed scenario. The 1,200 residents are unchanged; 4 more are individualized."""
    from irgs_reference import actor
    s=copy.deepcopy(base)
    s['population']['residual']-=4
    for pid,place in [('farmer-a','farm'),('farmer-b','farm'),('child-1','house-1'),('standby-1','house-1')]:
        s['actors'][pid]=actor(pid,place)
    s['actors']['caregiver-1']['location']='house-1'
    s['actors']['person-B']['location']='house-1'
    s['households']['house-1']['members']=['caregiver-1','person-B','child-1']
    s['commitments']={
      'caregiver-1':[[8,12,'household_care']],
      'farmer-a':[[8,12,'work:grow']], 'farmer-b':[[8,12,'work:grow']],
      'person-B':[[8,12,'work:cook']]}
    s['cash']={'treasury':600,'army':0,'caregiver-1':100,'person-B':100,'farmer-a':100,'farmer-b':100,'standby-1':0,'child-1':0}
    s['cash_baseline']=1000
    s['econ3']={
      'stocks':{'farm':{'seed':12,'grain':0},'house-1':{'grain':8,'fuel':4,'meal':0}},
      'opening':{'seed':12,'grain':8,'fuel':4,'meal':0},
      'produced':{'seed':0,'grain':0,'fuel':0,'meal':0},
      'consumed':{'seed':0,'grain':0,'fuel':0,'meal':0},
      'recipes':{
        'grow':{'site':'farm','inputs':{'seed':1},'outputs':{'grain':3},'qual':'grow'},
        'cook':{'site':'house-1','inputs':{'grain':2,'fuel':1},'outputs':{'meal':3},'qual':'cook'}},
      'sites':{'farm':{'workers_capacity':2},'house-1':{'workers_capacity':1}},
      'qualifications':{'caregiver-1':['care'],'person-B':['care','cook'],
        'farmer-a':['grow'],'farmer-b':['grow'],'child-1':[],'standby-1':[]},
      'active_jobs':{},'completed_jobs':{},'released_shifts':[],
      'care_delivered':[], 'meals_delivered':{},'provision_audit':[],
      'needs':{'house-1':{'care_start':8,'care_end':12,'care_required_hours':4,
                         'meal_deadline':16,'meal_required':6}},
      'needs_audit':[], 'shipments':{},'tax_claims':{}}
    validate_econ(s)
    return s
