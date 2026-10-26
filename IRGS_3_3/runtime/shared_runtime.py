"""Shared actor, capability, intention, information and receipt contracts.

Campaign adapters below select existing Core handlers, never rules from text.
The host authenticates sessions, supplies branch/restore identity and atomically
CAS-persists save + public result. No provider, key or Catalog checkout is used.
"""
from dataclasses import asdict
import copy
import json

from core_world import CoreWorld
from irgs_reference import InvalidEvent, canon, digest
from player_actions import _controlled, _failed_dependencies
from runtime_contracts import AcceptedIntent, ActionCapability, WorldScope
from response_depot import USAGE, draft_variants, render_exact

SCHEMA_VERSION = 'irgs-shared-runtime-1'
SCENE = 'execute_player_scene_action'
SETTLEMENT = 'execute_settlement_action'
DECLARE = 'record_player_action'


class SharedActionUnavailable(Exception):
    """Generic public code; attempted dependencies remain private to the host."""
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def _require(condition, code):
    if not condition:
        raise SharedActionUnavailable(code)


def _actor(world, actor):
    _require(_controlled(world.s,actor),'actor_denied')


def _capability(actor, operation, action, title, refs, family, values, authored):
    identity = 'cap:' + digest([actor,operation,action,title,refs,family,values,authored])
    return ActionCapability(identity,operation,canon(action),title,tuple(refs),family,canon(values),authored)


def capabilities(world, actor):
    """Received/selected options, without stock/blocker/permission filtering.

    Declaration is always explicit and unresolved. Supported execution options
    exist only where an actual adapter/selection supplies the selected handler.
    """
    _actor(world,actor)
    result = [_capability(actor,DECLARE,{},'Record an unresolved intention',
                         ['core:explicit-player-declaration'],'',{},'')]
    if world.s.get('binding',{}).get('campaign_profile') == 'rise' and actor == 'founder':
        from settlement_runtime import ACTIONS
        for key,title,_ in ACTIONS:
            family,values = 'player.choose', {'option_label':title}
            if key == 'wait_hour':
                family,values = 'player.wait', {}
            elif key == 'inspect':
                family,values = 'player.look_around', {}
            result.append(_capability(actor,SETTLEMENT,{'action_id':key},title,
                [world.s['rise']['source_ref']],family,values,'I would like to attempt: '+title+'.'))
    else:
        from scene_actions import scene_options
        for option in scene_options(world.s,actor):
            rules = world.s['scene_rules']  # The actual received selected map, never a genre template.
            action = rules['actions'][option['action_id']]
            family,values = 'player.choose', {'option_label':option['title']}
            if action['kind']=='move':
                family,values = 'player.travel', {'destination_label':rules['places'][action['to']]['title']}
            elif action['kind']=='observe':
                family,values = 'player.observe', {'target_label':rules['places'][action['from']]['title']}
            result.append(_capability(actor,SCENE,{'kind':'scene_action','action_id':option['action_id']},
                option['title'],[rules['receipt_evidence_id'],rules['source_ref']],family,values,option['text']))
    return tuple(result)


def received_records(world, actor, *, limit=64):
    """Detached actual received evidence/phases; no live world/truth projection."""
    _actor(world,actor)
    _require(type(limit) is int and 1<=limit<=128,'invalid_limit')
    rows=[]
    for key,receipt in world.s['knowledge'].get(actor,{}).items():
        evidence=world.s['evidence'].get(key)
        if not evidence or not evidence['recorded_at']<=receipt['received_at']<=world.s['clock']:
            continue
        rows.append({'record_id':key,'text':evidence['assertion'],'status':evidence['status'],
            'source_ref':evidence['source_ref'],'originator':evidence.get('originator'),
            'recorded_at':evidence['recorded_at'],'received_at':receipt['received_at'],
            'time_axis':'causal_sequence'})
    for key,receipt in world.s.get('settlement_receipts',{}).get(actor,{}).items():
        rows.append({'record_id':'settlement:'+key,'text':receipt['text'],'status':'received_record',
            'source_ref':world.s['rise']['source_ref'],'recorded_at':receipt['recorded_at'],
            'received_at':receipt['recorded_at'],'time_axis':'causal_sequence',
            'elapsed_total':receipt['elapsed_seconds']})
    for key,receipt in world.s.get('process_phase_receipts',{}).items():
        if receipt['actor'] != actor:
            continue
        rows.append({'record_id':'process-phase:'+key,'text':receipt['summary'],'status':'received_process_phase',
            'source_ref':receipt['source_ref'],'recorded_at':receipt['at'],'received_at':receipt['at'],
            'time_axis':'causal_sequence','process_status':receipt['status'],
            'worked_seconds':receipt['worked_seconds'],'remaining_seconds':receipt['remaining_seconds']})
    rows.sort(key=lambda r:(r['received_at'],r['record_id']))
    return {'records':copy.deepcopy(rows[-limit:]),'total':len(rows),'truncated':len(rows)>limit}


def actor_view(world, actor, *, branch_id, restore_id):
    """Host-only actor scope and public projection; private scope is separate."""
    _actor(world,actor)
    scope=WorldScope(world.s['campaign_id'],branch_id,restore_id,world.checksum())
    scope.validate()
    caps=capabilities(world,actor)
    received=received_records(world,actor)
    from phase_contract import actor_view as phase_view
    continuations=phase_view(world,actor,branch_id=branch_id,restore_id=restore_id)
    from communication_contract import actor_view as communication_view
    communications=communication_view(world,actor,branch_id=branch_id,restore_id=restore_id)
    from start_readiness import actor_view as start_view
    start_context=start_view(world,actor,branch_id=branch_id,restore_id=restore_id)
    # Snapshot binds host branch/restore plus only actor-visible facts/revision.
    snapshot='view:'+digest([scope.campaign_id,branch_id,restore_id,actor,
                            [asdict(c) for c in caps],received,continuations['snapshot_id'],
                            communications['snapshot_id'],start_context['snapshot_id']])
    return {'schema_version':SCHEMA_VERSION,'actor_id':actor,'snapshot_id':snapshot,
        'capabilities':[c.public() for c in caps],'received':received,
        'continuations':continuations,
        'communications':communications,
        'start_context':start_context,
        'drafts':[row for cap in caps for row in draft_variants(actor,snapshot,cap)],
        'custom_response':{'text':'','editable':True,'requires_explicit_submission':True},
        'render_usage':dict(USAGE)}


def prepare_intent(world, *, request_id, actor_id, intention, branch_id, restore_id,
                   capability_id=None, source_ref='explicit-player-submission'):
    """Retain the exact edited text and independently selected structured action.

    None selects only an unresolved declaration. A semantic tag or unknown ID
    cannot select an operation. The UI must show both text and action for review.
    """
    caps=capabilities(world,actor_id)
    selected=(caps[0] if capability_id is None else
              next((c for c in caps if c.capability_id==capability_id),None))
    _require(selected is not None,'capability_unavailable')
    request=AcceptedIntent(request_id,
        WorldScope(world.s['campaign_id'],branch_id,restore_id,world.checksum()),actor_id,intention,
        selected.capability_id,selected.operation_id,selected.action_json,source_ref)
    request.validate()
    return request


def _event_id(request):
    # One shared request namespace across adapters. Changing an operation cannot
    # turn an already accepted identity into a different event.
    return 'shared:'+request.request_id


def _instruction(request):
    return canon({'intention':request.intention,'accepted_intent_digest':digest(json.loads(request.to_json()))})


def committed_receipt(world, actor, event_id, *, branch_id, restore_id, variant_seed=0):
    """A detached actual result, with neutral local text and original provenance."""
    _actor(world,actor)
    WorldScope(world.s['campaign_id'],branch_id,restore_id,world.checksum()).validate()
    event=next((e for e in world.s['journal'] if e['id']==event_id),None)
    _require(event is not None,'receipt_unavailable')
    op,p=event['op'],event['params']
    _require(p.get('actor')==actor or op=='execute_local_communication','actor_denied')
    if op==DECLARE:
        exact='Declared intention (unresolved):\n'+p['declaration']
        status='declared_not_resolved'
        source_refs=[p['source_ref']]
        elapsed=None
    elif op in (SCENE,SETTLEMENT,'continue_player_process','execute_local_communication'):
        from offline_responses import receipt_facts
        facts=receipt_facts(world,actor,event_id)
        exact=facts['literal_text']
        elapsed=facts['packets'].get('elapsed.action',{}).get('elapsed_seconds')
        source_refs=[p['source_ref']]
        if op==SCENE:
            status=world.s['scene_action_results'][event_id]['status']
        elif op==SETTLEMENT:
            status='completed_successfully'  # Submission, never a claim that its physical project finished.
        elif op=='continue_player_process':
            status=world.s['process_phase_receipts'][p['phase_id']]['status']
        else:
            result=world.s['communication_results'][p['request_id']]
            status=result['status'];source_refs.append(result['evidence_id'])
    else:
        # Existing equipment/general results keep their own honest API; no invented adapter.
        raise SharedActionUnavailable('receipt_adapter_unavailable')
    snapshot='receipt:'+digest([world.s['campaign_id'],branch_id,restore_id,actor,event_id,event['at'],exact])
    return {'schema_version':SCHEMA_VERSION,'actor_id':actor,'event_id':event_id,
        'operation_id':op,'outcome_status':status,'exact_text':exact,'source_refs':source_refs,
        'committed_at':event['at'],'time_axis':'causal_sequence','elapsed_seconds':elapsed,
        'presentation':render_exact(actor,snapshot,exact,elapsed_seconds=elapsed,variant_seed=variant_seed)}


def execute_intent(world, request, *, current_scope, persist, explicitly_accepted):
    """One current supported Core action, published only after mandatory host CAS.

    Lost acknowledgment: reload the actual host save, then retry the serialized
    request. Discarded-future requests fail the host restore/branch/state fence.
    """
    _require(isinstance(request,AcceptedIntent),'invalid_request')
    request.validate()
    _require(explicitly_accepted is True,'acceptance_required')
    _require(callable(persist),'persistence_required')
    current_scope.validate()
    _actor(world,request.actor_id)
    _require((current_scope.campaign_id,current_scope.branch_id,current_scope.restore_id)==
        (request.scope.campaign_id,request.scope.branch_id,request.scope.restore_id),'stale_scope')
    _require(world.s['campaign_id']==current_scope.campaign_id,'stale_scope')
    _require(request.operation_id in (SCENE,SETTLEMENT,DECLARE),'capability_unavailable')
    action=json.loads(request.action_json)
    event_id=_event_id(request)
    instruction=_instruction(request)
    params={'campaign_id':world.s['campaign_id'],'source_ref':request.source_ref,
            'instruction_ref':instruction,'actor':request.actor_id}
    if request.operation_id==SCENE:
        params.update(action=action,action_event_id=event_id)
    elif request.operation_id==SETTLEMENT:
        params.update(action=action.get('action_id'),request_id='shared:'+request.request_id)
    else:
        params['declaration']=request.intention
    prior=next((e for e in world.s['journal'] if e['id']==event_id),None)
    if prior is not None:
        _require(prior['op']==request.operation_id and prior['params']==params,'request_identity_conflict')
        return _public_result(world,request,event_id)
    _require(current_scope==request.scope and world.checksum()==request.scope.state_digest,'stale_state')
    current=next((c for c in capabilities(world,request.actor_id) if c.capability_id==request.capability_id),None)
    _require(current is not None and current.operation_id==request.operation_id
             and current.action_json==request.action_json,'capability_unavailable')
    event={'id':event_id,'at':world.s['clock']+1,'op':request.operation_id,'params':params}
    from r9_runtime import observe
    try:
        certificate=observe(world.s,event)
        candidate=CoreWorld(state=world.s)
        candidate.apply(event_id,event['at'],request.operation_id,**params)
        _require(candidate.checksum()==certificate['post_state'],'observation_refused')
    except (InvalidEvent,AssertionError,KeyError,TypeError,ValueError):
        error=SharedActionUnavailable('action_unavailable')
        error.dependencies=_failed_dependencies(world.s,event)
        raise error from None
    public=_public_result(candidate,request,event_id)
    persist(request.scope,candidate.save(),public)
    world.s=candidate.s
    return public


def _public_result(world,request,event_id):
    receipt=committed_receipt(world,request.actor_id,event_id,
        branch_id=request.scope.branch_id,restore_id=request.scope.restore_id)
    return {'schema_version':SCHEMA_VERSION,'request_id':request.request_id,
        'actor_id':request.actor_id,'intention':request.intention,
        'capability_id':request.capability_id,'status':receipt['outcome_status'],
        'receipt':receipt,'presentation':receipt['presentation']}
