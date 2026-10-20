"""R6 read-only accounting audit, separate formulas; NOT independent runtime or evidence verification."""
from collections import Counter,defaultdict

def audit_r6(state):
    e=state['econ3'];stock=defaultdict(int)
    for loc,items in e['stocks'].items():
        for m,q in items.items():
            if not isinstance(q,int) or q<0:raise ValueError('negative stock')
            stock[m]+=q
    sources=Counter()
    for entry in state['journal']:
        if entry['op']=='physical_loss':
            p=entry['params'];sources[p['material']]+=p['quantity']
    for m,n in e['opening'].items():
        if stock[m]!=n+e['produced'][m]-e['consumed'][m]-e.get('losses',{}).get(m,0):
            raise ValueError('material failed conservation')
        if sources[m]!=e.get('losses',{}).get(m,0):raise ValueError('loss provenance mismatch')
    for jid,short in state.get('r5_shortfalls',{}).items():
        if jid in e['active_jobs']:
            j=e['active_jobs'][jid]
            if j.get('status')!='suspended_unallocated' or any(j['reserved_inputs'].values()):
                raise ValueError('live shortfall incorrectly backed')
        else:
            if short.get('status') not in ('settled_with_unfulfilled_claim','fulfilled_by_continuation') or jid not in state['r6_settlements']:
                raise ValueError('inactive shortfall missing preserved claim or settlement')
    all_milestones={ev['id'] for ev in state['journal'] if ev['op']=='record_work_milestone'}
    expected_consumed=Counter();expected_produced=Counter();verified_hours=0
    for jid,p in state.get('r6_progress',{}).items():
        if p['hours_verified']!=sum(m['worker_hours'] for m in p['milestones']):
            raise ValueError('hours duplicated')
        verified_hours+=p['hours_verified']
        for m in p['milestones']:
            if m['event_id'] not in all_milestones:raise ValueError('orphaned milestone source')
            expected_consumed.update(m['inputs_consumed'])
            expected_produced.update(m['accepted_output'])
    for mat,num in expected_consumed.items():
        if num>e['consumed'][mat]:raise ValueError('milestone consumption larger than actual stock use')
    for mat,num in expected_produced.items():
        if num>e['produced'][mat]:raise ValueError('milestone output larger than accepted production')
    for jid,settlement in state.get('r6_settlements',{}).items():
        rec=state['r6_progress'][jid]
        if settlement['hours_verified']!=rec['hours_verified']:
            raise ValueError('settlement hour mismatch')
    return {'physical_totals':dict(stock),'loss_sources':dict(sources),
       'r6_verified_worker_hours':verified_hours,'r6_milestone_input':dict(expected_consumed),
       'r6_milestone_output':dict(expected_produced),
       'r6_job_settlements':len(state.get('r6_settlements',{})),
       'journal_events':len(state['journal'])}
