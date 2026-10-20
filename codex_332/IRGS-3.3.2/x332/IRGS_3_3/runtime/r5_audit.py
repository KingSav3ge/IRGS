"""Independent formulas for auditing R5 fixture ledgers; not a second engine.

Deliberately avoids calls to World._validate/economic_extension validators.
Only guarantees listed invariants, not authority, combat models or time laws.
"""
from collections import Counter, defaultdict


def independent_audit(s, *, initial_ammo=None):
    econ=s['econ3']; stocks=defaultdict(int)
    for location,amounts in econ['stocks'].items():
        for material,q in amounts.items():
            if type(q) is not int or q<0:raise ValueError('negative physical material')
            stocks[material]+=q
    loss_sources=Counter()
    for ev in s['journal']:
        if ev['op']=='physical_loss':
            loss_sources[ev['params']['material']]+=ev['params']['quantity']
    for material,opening in econ['opening'].items():
        expected=opening+econ['produced'][material]-econ['consumed'][material]-econ.get('losses',{}).get(material,0)
        if stocks[material]!=expected:raise ValueError('external material identity mismatch')
        if loss_sources[material]!=econ.get('losses',{}).get(material,0):
            raise ValueError('loss record does not match occurrence journal')
    for jid,rec in s.get('r5_shortfalls',{}).items():
        if jid not in econ['active_jobs'] or econ['active_jobs'][jid].get('status')!='suspended_unallocated':
            raise ValueError('shortfall lacks suspended owning job')
        for material in rec['remaining_claim']:
            if econ['active_jobs'][jid]['reserved_inputs'][material]!=0:
                raise ValueError('suspended claim was still booked against physical backing')
    spend=Counter()
    incapacitation_source=set()
    for ev in s['journal']:
        if ev['op']=='simultaneous_exchange':
            for hit in ev['params']['attacks']:
                spend[hit['from']]+=hit['ammo_used']
                if hit['effect']=='disable':incapacitation_source.add(hit['to'])
    if initial_ammo is not None:
        for actor,opening in initial_ammo.items():
            if s['actors'][actor]['ammo']!=opening-spend[actor]:
                raise ValueError('ammo source mismatch; fixture excludes resupply')
    return {'material_totals':dict(stocks),'losses_by_journal':dict(loss_sources),
            'original_claim_count':len(s.get('r5_shortfalls',{})),
            'ammunition_spent_by_source':dict(spend),
            'ever_disabled_by_source':sorted(incapacitation_source),
            'event_count':len(s['journal'])}
