"""Bounded native receivers use the same Core state and transaction as campaigns."""
GENRE_OPS={'military_issue_equipment','roman_begin_delegated_activity','revoke_delegation'}

def operate(core,s,at,op,p):
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
            core._operate(s,at,'transfer_stock',{'from':p['from'],'to':cid,'material':p['material'],
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
        core._operate(s,at,'commit_activity',params)
    elif op=='revoke_delegation':
        d=s['delegations'][p['delegation_id']]
        assert d['principal']==p['principal'] and p['authority_ref']==d['authority_ref']
        if d['principal'] in core.player_ids(s):assert p.get('instruction_ref')
        d['active']=False;d['revoked_at']=at;d['revoke_source']=p['source_ref']
