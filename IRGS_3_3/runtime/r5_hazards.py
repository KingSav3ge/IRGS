"""Proposed R5 bounded physical-loss and shortfall reconciliation.

Loss is an event on physical stock, not a negotiable allocation request.
If an existing reservation cannot remain backed after loss, suspend all
competing active jobs for that material; never silently favor an event ID.
Ordinary same-frontier operations on the same physical pool require a declared
physical sequence. No selected general causality-stage policy is assumed.
"""
from __future__ import annotations
import copy
from collections import defaultdict
from irgs_reference import World, InvalidEvent, digest
from selective_coordinator import R4World, footprint
from economic_extension import physical, reserved


def loss_key(event):
    p=event['params'];return ('stock',p['location'],p['material'])

class PhysicalWorld(World):
    def _operate(self,s,at,op,p):
        if op!='physical_loss':
            return super()._operate(s,at,op,p)
        if 'econ3' not in s: raise ValueError('no selected physical stock ledger')
        loc,mat,qty=p['location'],p['material'],p['quantity']
        if not isinstance(loc,str) or not loc or not isinstance(mat,str) or not mat:
            raise ValueError('qualified stock locator required')
        if type(qty) is not int or qty<=0 or not p.get('cause_ref') or not p.get('evidence_ref'):
            raise ValueError('positive observed loss with cause/evidence required')
        if loc.startswith('transit:'):
            raise ValueError('in-transit cargo loss requires shipment-quantity reconciliation adapter')
        e=s['econ3']
        if mat not in e['opening'] or physical(e,loc,mat)<qty:
            raise ValueError('measured loss exceeds supported physical holdings')
        e['stocks'][loc][mat]-=qty
        e.setdefault('losses',{})[mat]=e.setdefault('losses',{}).get(mat,0)+qty
        s.setdefault('r5_loss_events',[]).append({'at':at,'location':loc,'material':mat,
            'quantity':qty,'cause_ref':p['cause_ref'],'evidence_ref':p['evidence_ref']})
        # No event order chooses which preexisting claimant gets the remainder.
        shortage_by_material={m:(reserved(e,loc,m)-physical(e,loc,m))
                             for m in e['opening'] if reserved(e,loc,m)>physical(e,loc,m)}
        if shortage_by_material:
            affected={jid for jid,job in e['active_jobs'].items() if job['site']==loc
                and any(job['reserved_inputs'].get(m,0)>0 for m in shortage_by_material)}
            # Expand when a reservation on another material would go unsupported;
            # suspended jobs release backing, but retain original contractual claims.
            for jid in sorted(affected):
                job=e['active_jobs'][jid]
                if job.get('status')=='suspended_unallocated': continue
                original=copy.deepcopy(job['reserved_inputs'])
                job['reserved_inputs']={m:0 for m in original}
                job['status']='suspended_unallocated'
                s.setdefault('r5_shortfalls',{})[jid]={
                    'job_id':jid,'detected_at':at,'site':loc,'original_reserved_inputs':original,
                    'remaining_claim':copy.deepcopy(original),'status':'needs_explicit_requalification',
                    'cause_ref':p['cause_ref'],'no_production_or_cancellation_implied':True}
        # Pool-level deficiency is retained even if all backing is now released.
        for mat2,deficit in sorted(shortage_by_material.items()):
            s.setdefault('r5_pool_shortfalls',[]).append({'at':at,'site':loc,'material':mat2,
                'shortfall_at_hazard':deficit,'resolution':'no_allocation_selected',
                'cause_ref':p['cause_ref']})

class R5World(R4World):
    def apply(self,eid,at,op,**params):
        if op=='physical_loss':
            worker=PhysicalWorld(state=self.s)
            result=worker.apply(eid,at,op,**params)
            self.s=worker.s
            return result
        return super().apply(eid,at,op,**params)

    def run_until(self,through):
        if through<self.s['clock']:raise InvalidEvent('cannot run backwards')
        summary={'committed':[],'deferred':[],'physical_losses':[],'through':through}
        while True:
            eligible=[ev for ev in self.s['pending'] if ev['at']<=through]
            if not eligible:break
            at=min(ev['at'] for ev in eligible)
            epoch=[ev for ev in eligible if ev['at']==at]
            losses=[ev for ev in epoch if ev['op']=='physical_loss']
            if not losses:
                nxt=R4World(state=self.s)
                out=nxt.run_until(at)
                self.s=nxt.s
                summary['committed']+=out['committed'];summary['deferred']+=out['deferred']
                continue
            # All physical observations at a frontier are checked together, from
            # pre-frontier holdings. An inconsistent combined claim is not resolved
            # by assuming a lexical winner.
            grouped=defaultdict(int)
            for ev in losses:
                q=ev['params'].get('quantity')
                if type(q) is not int or q<=0:raise InvalidEvent('unqualified physical loss quantity')
                grouped[loss_key(ev)]+=q
            for (kind,loc,mat),qty in grouped.items():
                if qty>physical(self.s['econ3'],loc,mat):
                    raise InvalidEvent('incompatible simultaneous loss measurements: reconcile evidence')
            # Other same-frontier demands touching a lost pool cannot be assumed
            # to have occurred before OR after it; defer until ordering is proven.
            keys={':'.join(k) for k in grouped}
            ambiguous=[ev for ev in epoch if ev['op']!='physical_loss'
                and bool(footprint(self.s,ev)&keys)]
            candidate=PhysicalWorld(state=self.s)
            for ev in sorted(losses,key=lambda v:v['id']):
                candidate.apply(ev['id'],at,ev['op'],**ev['params'])
            state=candidate.s
            ids={ev['id'] for ev in losses+ambiguous}
            state['pending']=[ev for ev in state['pending'] if ev['id'] not in ids]
            if ambiguous:
                gid='causal-order:'+digest({'at':at,'ids':sorted(x['id'] for x in ambiguous),
                                            'loss_ids':sorted(x['id'] for x in losses)})[:20]
                state.setdefault('r4_deferred',{})[gid]={
                    'at':at,'requests':copy.deepcopy(sorted(ambiguous,key=lambda x:x['id'])),
                    'status':'causal_order_undetermined','diagnostic':'same-time physical-loss ordering unqualified',
                    'allocation_selected':False,'loss_ids':sorted(x['id'] for x in losses)}
                summary['deferred'].append(gid)
            self.s=state
            summary['physical_losses'] += [ev['id'] for ev in losses]
            summary['committed'] += [ev['id'] for ev in losses]
            # Other independent proposals at the same frontier retain their
            # timestamp; they may execute without an unrelated warehouse blocking.
            runner=R4World(state=self.s)
            out=runner.run_until(at)
            self.s=runner.s
            summary['committed']+=out['committed'];summary['deferred']+=out['deferred']
        if self.s['clock']<through:
            runner=R4World(state=self.s)
            runner.run_until(through)
            self.s=runner.s
        return summary
