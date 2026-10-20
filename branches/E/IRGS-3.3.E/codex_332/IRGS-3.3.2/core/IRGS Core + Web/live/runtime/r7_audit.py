"""Independent read-only R7 invariant/provenance audit; NOT independent simulator."""
from collections import Counter
from irgs_reference import digest
from economic_extension import total, physical
from r6_audit import audit_r6

def audit_r7(s):
    base=audit_r6(s)
    e=s['econ3'];source_by_id={ev['id']:ev for ev in s['journal']}
    made=Counter();accepted=Counter();salvaged=Counter();damaged=Counter()
    inputs=Counter();intermediate_used=Counter()
    for jid,rec in s.get('r7_intermediates',{}).items():
        spec=rec['profile_snapshot']
        if digest(spec)!=rec['profile_digest']:raise ValueError('profile snapshot corrupted')
        src=source_by_id.get(rec['source_event_id'])
        if not src or src['op']!='make_intermediate' or src['params']['item_id']!=jid:
            raise ValueError('workpiece has no fabrication source')
        if physical(e,'wip:'+jid,rec['intermediate'])!=rec['physical_qty']:
            raise ValueError('physical intermediate differs from recorded workpiece')
        made[spec['intermediate']]+=spec['intermediate_qty']
        inputs[spec['input']]+=spec['input_qty']
        loss=sum(x['quantity'] for x in rec['losses'])
        for x in rec['losses']:
            ev=source_by_id.get(x['event_id'])
            if not ev or ev['op']!='physical_loss' or ev['params']['quantity']!=x['quantity']:
                raise ValueError('intermediate loss lacks journal evidence')
        damaged[spec['intermediate']]+=loss
        if rec['status']=='accepted':
            accepted[spec['finished']]+=spec['finished_qty']
            intermediate_used[spec['intermediate']]+=spec['intermediate_qty']
        if rec['status']=='salvaged':
            salvaged[spec['salvage']]+=rec['recovered_quantity']
            intermediate_used[spec['intermediate']]+=rec['initial_qty']-loss
        remaining=rec['physical_qty']
        assert spec['intermediate_qty']==remaining+loss+ (spec['intermediate_qty']-loss if rec['status'] in ('accepted','salvaged') else 0)
    for m,q in made.items():
        if q>e['produced'][m]:raise ValueError('workpiece source exceeds intermediate production')
    for m,q in inputs.items():
        if q>e['consumed'][m]:raise ValueError('workpiece input exceeds actual consumption')
    for m,q in accepted.items():
        if q>e['produced'][m]:raise ValueError('accepted goods exceed actual production')
    for m,q in salvaged.items():
        if q>e['produced'][m]:raise ValueError('salvage exceeds recorded recovered output')
    for m,q in damaged.items():
        if q>e['losses'].get(m,0):raise ValueError('workpiece damage is not recorded as loss')
    return {**base,'r7_workpieces':len(s.get('r7_intermediates',{})),
        'r7_input_consumed':dict(inputs),'r7_intermediate_created':dict(made),
        'r7_finished_accepted':dict(accepted),'r7_salvage_recovered':dict(salvaged),
        'r7_intermediate_physically_lost':dict(damaged),
        'r7_material_conservation':{m:total(e,m)==e['opening'][m]+e['produced'][m]-e['consumed'][m]-e.get('losses',{}).get(m,0) for m in e['opening']}}
