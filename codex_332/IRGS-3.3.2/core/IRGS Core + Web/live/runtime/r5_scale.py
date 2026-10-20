"""Read-only tactical-to-strategic projection from actual journal and actor state.

No residual-cohort casualty inference. Reports and engagement summaries are
information records, never physical writes. Does not model monthly combat.
"""
from __future__ import annotations
from irgs_reference import InvalidEvent,digest

class MilitaryProjection:
    def __init__(self,world):
        self.s=world.s
    def view(self,*,actors,through,from_time=0):
        if type(through) is not int or type(from_time) is not int or through<from_time:
            raise InvalidEvent('invalid interval')
        if through!=self.s['clock']:raise InvalidEvent('historical as-of view requires an archived state checkpoint')
        ids=list(actors)
        if len(ids)!=len(set(ids)) or not set(ids)<=set(self.s['actors']):
            raise InvalidEvent('actors must resolve exactly; aggregate membership cannot overlap')
        hits=[];events=[];reports=[];observed=set();ammo_spent={p:0 for p in ids}
        for ev in self.s['journal']:
            if not from_time<=ev['at']<=through:continue
            if ev['op']=='simultaneous_exchange':
                relevant=[h for h in ev['params']['attacks'] if h['from'] in ids or h['to'] in ids]
                if relevant:
                    events.append(ev['id'])
                    for h in relevant:
                        hits.append({'source_event_id':ev['id'],**h})
                        if h['from'] in ammo_spent:ammo_spent[h['from']]+=h['ammo_used']
            elif ev['op']=='summarize_engagement':
                # Summary is another information record, not an additional hit.
                if ev['params']['engagement_id'] in {v['params']['engagement_id'] for v in self.s['journal']
                              if v['op']=='simultaneous_exchange' and v['id'] in events}:
                    observed.add(ev['id'])
            elif ev['op']=='report' and ev['params']['person'] in ids:
                reports.append(ev['id'])
        # Current actual condition is authoritative; source effects are provenance.
        current={p:{'disabled':self.s['actors'][p]['disabled'],
                    'ammo_remaining':self.s['actors'][p]['ammo']} for p in ids}
        return {'actors':sorted(ids),'as_of':through,'from_time':from_time,
            'current_actor_state':current,'disabled_now':sorted(p for p,v in current.items() if v['disabled']),
            'actor_disablement_count_now':sum(v['disabled'] for v in current.values()),
            'ammunition_spent_from_sources':ammo_spent,'effect_source_ids':sorted(set(events)),
            'effect_count':len(hits),'information_summary_ids':sorted(observed),
            'report_ids':sorted(reports),'writes_to_world':False}
    def residual_population_view(self,*,excluded_named_actors):
        if len(excluded_named_actors)!=len(set(excluded_named_actors)) or not set(excluded_named_actors)<=self.s['actors'].keys():
            raise InvalidEvent('invalid named-actor exclusion')
        return {'unnamed_residual_people':self.s['population']['residual'],
                'detailed_actors_excluded':sorted(excluded_named_actors),
                'combat_losses_in_unnamed_cohort':'unknown_not_inferred',
                'writes_to_population':False}
