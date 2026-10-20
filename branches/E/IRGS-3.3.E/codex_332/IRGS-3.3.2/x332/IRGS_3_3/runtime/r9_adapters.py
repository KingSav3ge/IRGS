"""New proposed receiver operations, not existing/adopted native engine releases.

Military command receipt and Roman delegated work use the same Core state.
Profile and delegation records are explicit synthetic fixture selections.
"""
import copy
from irgs_reference import InvalidEvent, digest
from r7_frontier import R7World

NATIVE_OPS={'mil_issue_received_order','rom_start_delegated_job','rom_revoke_delegation'}

class ReceiverWorld(R7World):
    def apply(self,eid,at,op,**p):
        if op not in NATIVE_OPS:return super().apply(eid,at,op,**p)
        # Native receivers append their own outer event, so they must also
        # detach nested parameters from caller-owned data before committing.
        p=copy.deepcopy(p)
        event={'id':eid,'at':at,'op':op,'params':p}; signature=digest(event)
        prior=self.s['processed'].get(eid)
        if prior is not None:
            if prior!=signature:raise InvalidEvent('native ID reused with changed payload')
            return False
        if at<self.s['clock']:raise InvalidEvent('native event backdated')
        candidate=ReceiverWorld(state=self.s)
        try:
            bindings=candidate.s['r9_engine_bindings']
            if op=='mil_issue_received_order':
                assert bindings['military']=='R9-proposed-receiver-v1'
                order=candidate.s['orders'][p['order_id']]
                assert order['recipient']==p['commander']
                assert order['received_at'] is not None and order['received_at']<=at<=order['deadline']
                assert not order['executed']
                directive=candidate.s['r9_issue_directives'][p['order_id']]
                assert directive['authorized'] and directive['persons']==p['persons']
                super(ReceiverWorld,candidate).apply(eid+':issue',at,'issue_kits',persons=p['persons'])
                super(ReceiverWorld,candidate).apply(eid+':execute',at,'execute_order',order_id=p['order_id'])
            else:
                assert bindings['roman']=='R9-proposed-receiver-v1'
                delegation=candidate.s['r9_delegations'][p['delegation_id']]
                if op=='rom_revoke_delegation':
                    assert p['authority']==delegation['grantor'] and p['decision_ref']
                    delegation['active']=False;delegation['revoked_at']=at
                else:
                    assert delegation['active'] and delegation['delegate']==p['delegate']
                    assert delegation['start']<=at and p['end']<=delegation['end']
                    assert delegation['recipe_id']==p['recipe_id'] and delegation['workers']==p['workers']
                    assert delegation['site']==candidate.s['econ3']['recipes'][p['recipe_id']]['site']
                    params={k:p[k] for k in ('job_id','recipe_id','workers','start','end')}
                    super(ReceiverWorld,candidate).apply(eid+':work',at,'start_job',**params)
            candidate.s['clock']=at;candidate.s['processed'][eid]=signature;candidate.s['journal'].append(event)
            candidate._validate(candidate.s)
        except (AssertionError,KeyError,ValueError,TypeError) as err:
            raise InvalidEvent(f'{op}: {err}') from err
        self.s=candidate.s;return True
