"""Explicit local speech and offers using Core evidence, obligations and stock.

A reviewed campaign must select communication_rules; no channel, time model,
custody right, NPC decision or historical fact is inferred. Spoken words remain
testimony. Structured settlement gifts require a current existing R9 mandate.
"""
from dataclasses import asdict, dataclass
import copy
import json

from irgs_reference import InvalidEvent, canon, digest
from player_actions import _controlled, _failed_dependencies, _present
from runtime_contracts import WorldScope

OPERATION = 'execute_local_communication'


def _text(value, limit=4096):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= limit


def _channel(s, actor, recipient, channel_id):
    from settlement_runtime import location
    assert actor != recipient and _controlled(s, actor)
    assert _present(s, recipient), 'actual recipient existence required'
    rules = s['communication_rules']
    assert rules['schema_version'] == 1 and _text(rules['source_ref'])
    assert rules['time_model'] == 'causal_only_no_elapsed_rule'
    channel = rules['channels'][channel_id]
    assert channel['mode'] == 'co_located'
    assert actor in channel['actors'] and recipient in channel['actors']
    site = location(s, actor)
    assert _text(site) and not site.startswith('route:') and site == location(s, recipient)
    return rules


def _authority(s, at, actor, terms):
    from settlement_runtime import household_of, location
    assert s['binding']['campaign_profile'] == 'rise'
    rules = s['communication_rules']
    assert rules['stock_profile'] == 'settlement_free_stock'
    assert set(terms) == {'from', 'to', 'material', 'quantity', 'authority_id'}
    assert type(terms['quantity']) is int and terms['quantity'] > 0 and _text(terms['material'], 256)
    assert terms['from'] == household_of(s, actor) and terms['from'] != terms['to']
    mandate = s['r9']['mandates'][terms['authority_id']]
    assert mandate['active'] and mandate['actor'] == actor and _text(mandate['source_ref'])
    assert 'transfer_stock' in mandate['operations'] and mandate['effective_at'] <= at
    assert mandate.get('valid_until') is None or at <= mandate['valid_until']
    assert terms['from'] in rules['stock_authorities'][terms['authority_id']]
    assert s['stock_accounts'][terms['from']]['site'] == location(s, actor)


def _receive(core, s, at, p, recipient):
    evidence_id = 'communication:' + p['request_id']
    core._operate(s, at, 'record_evidence', {'evidence_id': evidence_id, 'subject': p['actor'],
        'assertion': p['intention'], 'status': 'testimony', 'originator': p['actor'],
        'source_ref': p['source_ref']})
    for listener in (p['actor'], recipient):
        core._operate(s, at, 'receive_evidence', {'evidence_id': evidence_id, 'recipient': listener,
                                               'source_ref': p['source_ref']})
    return evidence_id


def operate(core, s, at, p):
    assert set(p) == {'campaign_id', 'source_ref', 'instruction_ref', 'actor', 'recipient',
                     'request_id', 'command', 'details', 'channel_id', 'intention'}
    assert all(_text(p[key]) for key in ('source_ref', 'instruction_ref', 'intention'))
    assert _text(p['request_id'], 256) and isinstance(p['details'], dict)
    actor, recipient, command, details = p['actor'], p['recipient'], p['command'], p['details']
    rules = _channel(s, actor, recipient, p['channel_id'])
    offer_id, offer = None, None
    if command == 'speak':
        assert not details
        status = 'testimony_received'
    elif command in ('offer', 'counteroffer'):
        expected = {'offer_id', 'terms'} | ({'counter_to'} if command == 'counteroffer' else set())
        assert set(details) == expected and _text(details['offer_id'], 256)
        offer_id, terms = details['offer_id'], details['terms']
        assert offer_id not in s['obligations']
        _authority(s, at, actor, terms)
        from settlement_runtime import household_of, location
        assert terms['to'] == household_of(s, recipient)
        assert s['stock_accounts'][terms['to']]['site'] == location(s, recipient)
        if command == 'counteroffer':
            previous = s['obligations'][details['counter_to']]
            assert previous['status'] == 'offered'
            assert previous['offer']['recipient'] == actor and previous['subject'] == recipient
            previous['status'] = 'superseded'
        core._operate(s, at, 'record_obligation', {'obligation_id': offer_id, 'subject': actor,
            'description': p['intention'], 'status': 'offered', 'source_ref': p['source_ref'],
            'quantity': terms['quantity']})
        offer = s['obligations'][offer_id]
        offer['offer'] = {'recipient': recipient, 'terms': copy.deepcopy(terms),
            'terms_digest': digest(terms), 'channel_id': p['channel_id'],
            'rule_digest': digest(rules), 'proposed_at': at, 'proposal_ref': p['source_ref']}
        status = 'offered'  # No stock check, reservation, payment or acceptance by prose.
    elif command in ('accept', 'decline', 'withdraw'):
        assert set(details) == {'offer_id', 'terms_digest'}
        offer_id = details['offer_id']
        offer = s['obligations'][offer_id]
        contract = offer['offer']
        assert offer['status'] == 'offered' and details['terms_digest'] == contract['terms_digest']
        assert contract['channel_id'] == p['channel_id'] and digest(rules) == contract['rule_digest']
        if command == 'withdraw':
            assert offer['subject'] == actor and contract['recipient'] == recipient
            offer['status'] = 'withdrawn'
        else:
            assert contract['recipient'] == actor and offer['subject'] == recipient
            if command == 'accept':
                assert _controlled(s, recipient), 'offerer no longer under the selected control'
                terms = contract['terms']
                _authority(s, at, recipient, terms)
                from settlement_runtime import _free, household_of, location
                assert terms['to'] == household_of(s, actor)
                assert s['stock_accounts'][terms['to']]['site'] == location(s, actor)
                assert _free(s, terms['from'], terms['material']) >= terms['quantity']
                core._operate(s, at, 'transfer_stock', {'from': terms['from'], 'to': terms['to'],
                    'material': terms['material'], 'quantity': terms['quantity'],
                    'authority_ref': terms['authority_id'], 'source_ref': p['source_ref']})
                offer['status'] = 'fulfilled'
            else:
                offer['status'] = 'declined'
        offer['closed_at'] = at
        offer['closing_intention'] = p['intention']
        status = offer['status']
    else:
        raise AssertionError('unsupported communication command')
    evidence_id = _receive(core, s, at, p, recipient)
    result = {'actor': actor, 'recipient': recipient, 'request_id': p['request_id'], 'status': status,
        'utterance': p['intention'], 'truth_status': 'testimony', 'evidence_id': evidence_id,
        'source_ref': p['source_ref'], 'at': at, 'elapsed_status': 'not_resolved',
        'params_digest': digest(p)}
    if offer is not None:
        result['offer_id'] = offer_id
        result['terms'] = copy.deepcopy(offer['offer']['terms'])
        result['terms_digest'] = offer['offer']['terms_digest']
    if command == 'counteroffer':
        result['supersedes'] = details['counter_to']
    s.setdefault('communication_results', {})[p['request_id']] = result


def validate(s):
    events = {e['params']['request_id']: e for e in s['journal'] if e['op'] == OPERATION}
    assert set(events) == set(s.get('communication_results', {}))
    for key, result in s.get('communication_results', {}).items():
        assert result['params_digest'] == digest(events[key]['params'])
        evidence = s['evidence'][result['evidence_id']]
        assert evidence['status'] == 'testimony' and evidence['originator'] == result['actor']
        assert evidence['assertion'] == result['utterance']
        assert all(result['evidence_id'] in s['knowledge'][a] for a in (result['actor'],result['recipient']))
    for obligation in s['obligations'].values():
        if 'offer' not in obligation:
            continue
        offer = obligation['offer']
        assert offer['terms_digest'] == digest(offer['terms'])
        assert obligation['status'] in ('offered','fulfilled','withdrawn','declined','superseded')
        assert obligation['subject'] in s['actors'] and offer['recipient'] in s['actors']


@dataclass(frozen=True)
class CommunicationRequest:
    request_id: str
    actor: str
    recipient: str
    channel_id: str
    command: str
    details_json: str
    intention: str
    source_ref: str
    scope: WorldScope

    def to_json(self):
        return canon(asdict(self))

    @classmethod
    def from_json(cls, raw):
        data=json.loads(raw)
        data['scope']=WorldScope(**data['scope'])
        return cls(**data)


def prepare(world, *, request_id, actor, recipient, channel_id, command, details,
            intention, source_ref, branch_id, restore_id):
    from solo_provider import require
    require(_controlled(world.s, actor), 'actor_denied')
    require(all(_text(value,256) for value in (request_id, actor, recipient, channel_id, branch_id, restore_id)), 'invalid_request')
    require(_text(intention) and _text(source_ref) and isinstance(details,dict), 'invalid_request')
    return CommunicationRequest(request_id,actor,recipient,channel_id,command,canon(details),intention,source_ref,
        WorldScope(world.s['campaign_id'],branch_id,restore_id,world.checksum()))


def execute(world, request, *, current_scope, persist, explicitly_accepted):
    from core_world import CoreWorld
    from r9_runtime import observe
    from solo_provider import require, CapabilityUnavailable
    from offline_responses import render_receipt
    require(explicitly_accepted is True, 'acceptance_required')
    require(callable(persist), 'persistence_required')
    require((current_scope.campaign_id,current_scope.branch_id,current_scope.restore_id) ==
        (request.scope.campaign_id,request.scope.branch_id,request.scope.restore_id), 'stale_scope')
    require(current_scope.campaign_id == world.s['campaign_id'], 'stale_scope')
    params={'campaign_id':world.s['campaign_id'],'source_ref':request.source_ref,
        'instruction_ref':request.intention,'actor':request.actor,'recipient':request.recipient,
        'request_id':request.request_id,'channel_id':request.channel_id,'command':request.command,
        'details':json.loads(request.details_json),'intention':request.intention}
    event_id='communication:'+request.request_id
    if event_id in world.s['processed']:
        event=next(e for e in world.s['journal'] if e['id']==event_id)
        require(event['op']==OPERATION and event['params']==params,'request_identity_conflict')
        public = copy.deepcopy(world.s['communication_results'][request.request_id])
        public['presentation'] = render_receipt(world, request.actor, event_id)
        return public
    require(current_scope==request.scope and world.checksum()==request.scope.state_digest,'stale_state')
    event={'id':event_id,'at':world.s['clock']+1,'op':OPERATION,'params':params}
    try:
        certificate=observe(world.s,event)
        candidate=CoreWorld(state=world.s)
        candidate.apply(event_id,event['at'],OPERATION,**params)
        require(candidate.checksum()==certificate['post_state'],'observation_refused')
    except (InvalidEvent,AssertionError,KeyError,TypeError,ValueError):
        error=CapabilityUnavailable('communication_unavailable')
        error.dependencies=_failed_dependencies(world.s,event)
        raise error from None
    public=copy.deepcopy(candidate.s['communication_results'][request.request_id])
    public['presentation'] = render_receipt(candidate, request.actor, event_id)
    persist(request.scope,candidate.save(),public)
    world.s=candidate.s
    return public


def received(world, actor):
    from solo_provider import require
    require(_controlled(world.s,actor),'actor_denied')
    return [copy.deepcopy(result) for result in world.s.get('communication_results',{}).values()
            if result['evidence_id'] in world.s['knowledge'].get(actor,{})]


def presentation(world, actor, request_id):
    """Grounded structural narration from an actual received committed result."""
    from solo_provider import require
    result=world.s.get('communication_results',{}).get(request_id)
    require(result is not None and _controlled(world.s,actor) and
            result['evidence_id'] in world.s['knowledge'].get(actor,{}),'actor_denied')
    return {'status':result['status'],'utterance':result['utterance'],'utterance_status':'testimony',
        'speaker':result['actor'],'recipient':result['recipient'],'at':result['at'],'request_id':request_id,
        'source_refs':[result['source_ref'],result['evidence_id']],
        'committed_transfer':copy.deepcopy(result.get('terms')) if result['status']=='fulfilled' else None,
        'elapsed_status':result['elapsed_status']}
