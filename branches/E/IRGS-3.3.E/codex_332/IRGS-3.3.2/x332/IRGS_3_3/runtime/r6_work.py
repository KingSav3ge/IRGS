"""IRGS R6 work-lifecycle research adapter; proposed, bounded, NOT production Core.

R6 specialist operations are synchronous explicitly staged events. The R5/R4
scheduler is NOT certified to schedule these operations and rejects attempts
instead of silently calling its older World dispatcher. Evidence strings in
fixtures are simulated assertions, not independent verification of labor.
"""
from __future__ import annotations
import copy
from irgs_reference import World, InvalidEvent
from r5_hazards import R5World
from economic_extension import physical, free, covered_shift

NEW_OPS={'start_tracked_job','record_work_milestone','settle_disrupted_job',
         'start_continuation','finalize_tracked_job'}
PROHIBITED_LEGACY={'complete_job','interrupt_job','accrue_job_wages'}


def _positive_reference(p,key):
    assert isinstance(p.get(key),str) and p[key].strip(),f'{key} required'


def _check_model(s, recipe_id, ref):
    assert ref and s['r6_model_bindings'].get(recipe_id)==ref, 'unselected milestone model'


def _new_progress(job,model,source_at,parent=None):
    return {'recipe_id':job['recipe_id'],'site':job['site'],
            'workers':list(job['workers']),'hours_planned':(job['end']-job['start'])*len(job['workers']),
            'hours_verified':0,'last_at':source_at,'model_ref':model,'milestones':[],
            'parent_job_id':parent,'continuation_id':None}


def _pay_verified(s,job,progress,at,p,status):
    _positive_reference(p,'wage_agreement_ref')
    _positive_reference(p,'competent_authority_ref')
    rate=p['wage_rate']
    assert type(rate) is int and rate>=0
    assert progress['hours_verified']%len(job['workers'])==0
    each=progress['hours_verified']//len(job['workers'])
    earned=[]
    for pid in job['workers']:
        owed=rate*each
        s['wage_due'][pid]=s['wage_due'].get(pid,0)+owed
        earned.append({'person':pid,'amount':owed,'actual_verified_hours':each,
                       'agreement_ref':p['wage_agreement_ref']})
    return earned


class ProgressWorld(World):
    def _validate(self,s):
        super()._validate(s)
        progress=s.get('r6_progress',{})
        assert set(progress).issubset(set(s['econ3']['active_jobs'])|set(s['econ3']['completed_jobs']))
        for jid,rec in progress.items():
            assert 0<=rec['hours_verified']<=rec['hours_planned']
            assert sum(m['worker_hours'] for m in rec['milestones'])==rec['hours_verified']
            assert len({m['event_id'] for m in rec['milestones']})==len(rec['milestones'])
            assert all(m['worker_hours']>0 for m in rec['milestones'])
            if jid in s['econ3']['active_jobs']:
                job=s['econ3']['active_jobs'][jid]
                assert job['recipe_id']==rec['recipe_id']
                assert job['workers']==rec['workers']
                assert job.get('status','active') in ('active','suspended_unallocated')
        for jid,settlement in s.get('r6_settlements',{}).items():
            assert jid in s['econ3']['completed_jobs']
            assert settlement['hours_verified']==progress[jid]['hours_verified']
            assert settlement['status'] in ('interrupted_settled','completed_settled')

    def _operate(self,s,at,op,p):
        if op not in NEW_OPS:
            return super()._operate(s,at,op,p)
        e=s['econ3']; progs=s['r6_progress']
        if op=='start_tracked_job':
            rid=p['recipe_id']; _check_model(s,rid,p['selected_model_ref'])
            assert p['job_id'] not in progs
            super()._operate(s,at,'start_job', {k:p[k] for k in ('job_id','recipe_id','start','end','workers')})
            jid=p['job_id'];progs[jid]=_new_progress(e['active_jobs'][jid],p['selected_model_ref'],at)
        elif op=='record_work_milestone':
            jid=p['job_id'];job=e['active_jobs'][jid]; rec=progs[jid]
            assert job.get('status','active')=='active','suspended work has no qualified production'
            _positive_reference(p,'work_evidence_ref');_positive_reference(p,'output_acceptance_ref')
            _check_model(s,rec['recipe_id'],p['selected_model_ref'])
            assert p['from_at']==rec['last_at'] and p['to_at']==at,'unresolved process span'
            assert p['from_at']<at<=job['end'],'milestone outside active shift'
            hours=(at-p['from_at'])*len(job['workers'])
            assert rec['hours_verified']+hours<=rec['hours_planned']
            for pid in job['workers']:
                assert covered_shift(s,pid,p['from_at'],at,'work:'+rec['recipe_id'])
                assert not s['actors'][pid]['disabled'] and s['actors'][pid]['location']==job['site']
            spec=e['recipes'][job['recipe_id']]
            spent={m:rate*hours for m,rate in spec['inputs'].items()}
            made={m:rate*hours for m,rate in spec['outputs'].items()}
            for m,q in spent.items():
                assert job['reserved_inputs'][m]>=q and physical(e,job['site'],m)>=q
            for m,q in spent.items():
                e['stocks'][job['site']][m]-=q; e['consumed'][m]+=q
                job['reserved_inputs'][m]-=q
            for m,q in made.items():
                e['stocks'][job['site']][m]=physical(e,job['site'],m)+q
                e['produced'][m]+=q
            rec['hours_verified']+=hours;rec['last_at']=at
            rec['milestones'].append({'event_id':s.get('_r6_eid'), 'from_at':p['from_at'],
                'to_at':at,'worker_hours':hours,'inputs_consumed':spent,'accepted_output':made,
                'work_evidence_ref':p['work_evidence_ref'],'output_acceptance_ref':p['output_acceptance_ref']})
        elif op=='settle_disrupted_job':
            jid=p['job_id'];job=e['active_jobs'][jid];rec=progs[jid]
            assert job.get('status')=='suspended_unallocated'
            short=s['r5_shortfalls'][jid];assert at>=short['detected_at']
            _positive_reference(p,'assessment_ref')
            earned=_pay_verified(s,job,rec,at,p,'interrupted_settled')
            unassessed_start=rec['last_at'];unassessed_end=short['detected_at']
            assert unassessed_end>=unassessed_start
            complete={**copy.deepcopy(job),'hours_planned':rec['hours_planned'],
                      'hours_done':rec['hours_verified'],'settled_at':at,'interrupted':True,
                      'wages_accrued_for':earned, 'partial_output_already_committed':True}
            e['completed_jobs'][jid]=complete;del e['active_jobs'][jid]
            short['status']='settled_with_unfulfilled_claim';short['settled_at']=at
            s['r6_settlements'][jid]={'status':'interrupted_settled','at':at,
                'hours_verified':rec['hours_verified'], 'hours_remaining':rec['hours_planned']-rec['hours_verified'],
                'unassessed_elapsed_interval':[unassessed_start,unassessed_end],
                'unassessed_work_is_not_assumed_performed':True,
                'wages_accrued_for_verified_hours':earned,'wage_claim_for_unassessed_time':'unresolved',
                'assessment_ref':p['assessment_ref'],'source_shortfall_event':short['cause_ref']}
        elif op=='start_continuation':
            prior=p['parent_job_id'];old=s['r6_settlements'][prior];orig=progs[prior]
            assert old['status']=='interrupted_settled' and orig['continuation_id'] is None
            assert at>old['at'],'continuation must be prospective'
            _positive_reference(p,'authorization_ref')
            assert p['recipe_id']==orig['recipe_id'] and p['selected_model_ref']==orig['model_ref']
            remain=old['hours_remaining']; assert remain>0
            assert p['workers']==orig['workers'],'changed personnel requires separate qualification case'
            assert (p['end']-p['start'])*len(p['workers'])==remain, 'remaining work cannot be invented'
            super()._operate(s,at,'start_job',{k:p[k] for k in ('job_id','recipe_id','start','end','workers')})
            jid=p['job_id'];assert jid not in progs
            progs[jid]=_new_progress(e['active_jobs'][jid],p['selected_model_ref'],at,parent=prior)
            orig['continuation_id']=jid
        elif op=='finalize_tracked_job':
            jid=p['job_id'];job=e['active_jobs'][jid];rec=progs[jid]
            assert job.get('status','active')=='active'
            assert rec['hours_verified']==rec['hours_planned']
            assert rec['last_at']==job['end'] and at>=job['end']
            _positive_reference(p,'acceptance_ref')
            earned=_pay_verified(s,job,rec,at,p,'completed_settled')
            assert all(q==0 for q in job['reserved_inputs'].values()),'unconsumed reservation must be reconciled'
            e['completed_jobs'][jid]={**copy.deepcopy(job),'hours_planned':rec['hours_planned'],
                'hours_done':rec['hours_verified'],'settled_at':at,'interrupted':False,
                'wages_accrued_for':earned,'partial_output_already_committed':True}
            del e['active_jobs'][jid]
            s['r6_settlements'][jid]={'status':'completed_settled','at':at,
                'hours_verified':rec['hours_verified'],'hours_remaining':0,
                'wages_accrued_for_verified_hours':earned,'acceptance_ref':p['acceptance_ref']}
            # A completed authorized continuation satisfies the outstanding
            # planned-work claim, without deleting its historical loss record
            # or deciding the unassessed-time wage entitlement.
            parent=rec.get('parent_job_id')
            if parent is not None:
                short=s['r5_shortfalls'][parent]
                assert short['status']=='settled_with_unfulfilled_claim'
                short['status']='fulfilled_by_continuation'
                short['fulfilled_at']=at
                short['fulfilling_job_id']=jid
        else: raise ValueError('unknown R6 operation')

    def apply(self,eid,at,op,**params):
        # Atomic event commit must own the milestone ID for its source record.
        if op in NEW_OPS:
            original=self.s.get('_r6_eid')
            self.s['_r6_eid']=eid
            try:
                return super().apply(eid,at,op,**params)
            finally:
                if original is None:self.s.pop('_r6_eid',None)
                else:self.s['_r6_eid']=original
        return super().apply(eid,at,op,**params)


class R6World(R5World):
    def __init__(self,initial=None,state=None):
        raw=copy.deepcopy(state if state is not None else initial)
        if raw is None:raise ValueError('world required')
        raw.setdefault('r6_progress',{})
        raw.setdefault('r6_settlements',{})
        raw.setdefault('r6_model_bindings',{})
        super().__init__(state=raw)
        ProgressWorld(state=self.s)._validate(self.s)

    def apply(self,eid,at,op,**params):
        if op in PROHIBITED_LEGACY and params.get('job_id') in self.s['r6_progress']:
            raise InvalidEvent('tracked work requires qualified R6 milestone and settlement operations')
        if op in NEW_OPS:
            worker=ProgressWorld(state=self.s)
            result=worker.apply(eid,at,op,**params)
            self.s=worker.s
            return result
        candidate=R5World(state=self.s)
        result=candidate.apply(eid,at,op,**params)
        ProgressWorld(state=candidate.s)._validate(candidate.s)
        self.s=candidate.s
        return result

    def schedule(self,eid,at,op,**params):
        if op in NEW_OPS or (op in PROHIBITED_LEGACY and params.get('job_id') in self.s['r6_progress']):
            raise InvalidEvent('R6 work events require explicit direct causal-frontier staging; scheduler adapter unqualified')
        return super().schedule(eid,at,op,**params)

    def run_until(self,through):
        if any(ev['op'] in NEW_OPS or (ev['op'] in PROHIBITED_LEGACY and ev['params'].get('job_id') in self.s['r6_progress']) for ev in self.s['pending']):
            raise InvalidEvent('unqualified legacy dispatcher cannot run tracked work')
        candidate=R5World(state=self.s)
        out=candidate.run_until(through)
        ProgressWorld(state=candidate.s)._validate(candidate.s)
        self.s=candidate.s
        return out
