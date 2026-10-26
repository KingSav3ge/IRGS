"""Actor-safe host interface over selected Core speech and stock offers.

Participants are received attributions, not a live presence/eligibility list.
Offer status comes from received communications, never live obligations. All
commands are attempts; the native handler owns authority, rejection and effects.
"""
import copy
import json

import communication_runtime as native
from core_world import CoreWorld
from irgs_reference import digest
from player_actions import _controlled
from runtime_contracts import WorldScope

SCHEMA_VERSION = 'irgs-communication-capabilities-1'
RESULT_FIELDS = ('actor', 'recipient', 'request_id', 'status', 'utterance', 'truth_status',
    'evidence_id', 'source_ref', 'at', 'elapsed_status', 'offer_id', 'terms', 'terms_digest', 'supersedes')


class CommunicationUnavailable(Exception):
    """Bounded public code; optional dependency evidence is host-private."""
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def _require(condition, code='communication_unavailable'):
    if not condition:
        raise CommunicationUnavailable(code)


def _actor(world, actor):
    _require(_controlled(world.s, actor), 'actor_denied')


def _scope(world, branch_id, restore_id):
    scope = WorldScope(world.s['campaign_id'], branch_id, restore_id, world.checksum())
    scope.validate()
    return scope


def _sources(world, actor):
    rows = []
    for key, receipt in world.s['knowledge'].get(actor, {}).items():
        evidence = world.s['evidence'].get(key)
        if not evidence or not evidence['recorded_at'] <= receipt['received_at'] <= world.s['clock']:
            continue
        rows.append({'record_id': key, 'text': evidence['assertion'], 'status': evidence['status'],
            'originator': evidence.get('originator'), 'source_ref': evidence['source_ref'],
            'receipt_source_ref': receipt['source_ref'], 'recorded_at': evidence['recorded_at'],
            'received_at': receipt['received_at'], 'occurrence_time': copy.deepcopy(evidence.get('occurrence_time')),
            'time_axis': 'causal_sequence'})
    return sorted(rows, key=lambda r: (r['received_at'], r['record_id']))


def received_sources(world, actor, *, limit=64):
    """Original received evidence, with separate attribution and receipt sources."""
    _actor(world, actor)
    _require(type(limit) is int and 1 <= limit <= 128, 'invalid_limit')
    rows = _sources(world, actor)
    return copy.deepcopy({'records': rows[-limit:], 'total': len(rows), 'truncated': len(rows) > limit})


def _received(world, actor):
    # Forwarded testimony identifies its speaker, not private structured terms or
    # the original audience. Only actual participants receive the contract DTO.
    return sorted((r for r in world.s.get('communication_results', {}).values()
        if native.has_received_contract(world.s, actor, r)), key=lambda r: (r['at'], r['request_id']))


def _rules(world):
    rules = world.s.get('communication_rules', {})
    if (rules.get('schema_version') != 1 or not native._text(rules.get('source_ref'))
            or rules.get('time_model') != 'causal_only_no_elapsed_rule'
            or not isinstance(rules.get('channels'), dict)):
        return {}
    return rules


def _channels(world, actor):
    rules = _rules(world)
    known = {}
    for source in _sources(world, actor):
        speaker = source['originator']
        if native._text(speaker, 256) and speaker != actor:
            known.setdefault(speaker, set()).add(source['record_id'])
    for result in _received(world, actor):
        other = result['recipient'] if result['actor'] == actor else result['actor']
        known.setdefault(other, set()).add(result['evidence_id'])
    stock_selected = (world.s.get('binding', {}).get('campaign_profile') == 'rise'
                      and rules.get('stock_profile') == 'settlement_free_stock')
    rows = []
    for key, channel in sorted(rules.get('channels', {}).items()):
        if channel.get('mode') != 'co_located' or actor not in channel.get('actors', []):
            continue
        participants = [{'actor_id': other, 'source_record_ids': sorted(known[other]),
            'basis': 'received_attribution', 'availability': 'attemptable',
            'supported_commands': ['speak', 'offer'] if stock_selected else ['speak']}
            for other in sorted(known) if other in channel['actors']]
        rows.append({'channel_id': key, 'mode': 'co_located', 'source_ref': rules['source_ref'],
            'elapsed_status': 'not_resolved', 'participants': participants,
            'requires_explicit_submission': True})
    return rows


def _offers(world, actor):
    rows = {}
    # The journal binds a received result to its selected channel. No live offer,
    # location, mandate, stock or current dependency certificate is projected.
    events = {e['params']['request_id']: e['params'] for e in world.s['journal'] if e['op'] == native.OPERATION}
    for result in _received(world, actor):
        if 'supersedes' in result and result['supersedes'] in rows:
            old = rows[result['supersedes']]
            old.update(status='superseded', latest_request_id=result['request_id'],
                last_received_at=world.s['knowledge'][actor][result['evidence_id']]['received_at'])
            old['source_refs'] = [result['source_ref'], result['evidence_id']]
        if 'offer_id' not in result:
            continue
        key = result['offer_id']
        if result['status'] == 'offered':
            rows[key] = {'offer_id': key, 'offerer': result['actor'], 'recipient': result['recipient'],
                'channel_id': events[result['request_id']]['channel_id'], 'terms': copy.deepcopy(result['terms']),
                'terms_digest': result['terms_digest'], 'proposed_at': result['at'],
                'proposal_source_refs': [result['source_ref'], result['evidence_id']]}
        if key in rows:
            rows[key].update(status=result['status'], latest_request_id=result['request_id'],
                last_received_at=world.s['knowledge'][actor][result['evidence_id']]['received_at'],
                source_refs=[result['source_ref'], result['evidence_id']])
    for row in rows.values():
        commands = []
        if row['status'] == 'offered':
            commands = ['withdraw'] if row['offerer'] == actor else ['accept', 'decline', 'counteroffer']
        row.update(status_basis='received_communication', live_status_probed=False,
            time_axis='causal_sequence',
            supported_commands=[{'command': c, 'availability': 'attemptable',
                'requires_explicit_submission': True} for c in commands])
    return [rows[key] for key in sorted(rows)]


def actor_view(world, actor, *, branch_id, restore_id):
    _actor(world, actor)
    scope = _scope(world, branch_id, restore_id)
    channels, offers, sources = _channels(world, actor), _offers(world, actor), received_sources(world, actor)
    return {'schema_version': SCHEMA_VERSION, 'actor_id': actor,
        'snapshot_id': 'communication:' + digest([scope.campaign_id, branch_id, restore_id, actor, channels, offers, sources]),
        'channels': channels, 'offers': offers, 'received_sources': sources,
        'custom_response': {'text': '', 'editable': True, 'requires_explicit_submission': True},
        'render_usage': {'provider_calls': 0, 'model_tokens': 0}}


def offer_status(world, actor, offer_id, *, branch_id, restore_id):
    _actor(world, actor)
    _scope(world, branch_id, restore_id)
    row = next((r for r in _offers(world, actor) if r['offer_id'] == offer_id), None)
    _require(row is not None)
    return row


def _public(world, actor, raw, branch_id, restore_id):
    from shared_runtime import committed_receipt
    _require(any(r['request_id'] == raw['request_id'] for r in _received(world, actor)))
    result = {key: copy.deepcopy(raw[key]) for key in RESULT_FIELDS if key in raw}
    result.update(schema_version=SCHEMA_VERSION, status_basis='received_communication', live_status_probed=False,
        received_at=world.s['knowledge'][actor][raw['evidence_id']]['received_at'], time_axis='causal_sequence')
    result['receipt'] = committed_receipt(world, actor, 'communication:' + raw['request_id'],
                                        branch_id=branch_id, restore_id=restore_id)
    result['presentation'] = result['receipt']['presentation']
    return result


def received_communication(world, actor, request_id, *, branch_id, restore_id):
    _actor(world, actor)
    _scope(world, branch_id, restore_id)
    row = next((r for r in _received(world, actor) if r['request_id'] == request_id), None)
    _require(row is not None)
    return _public(world, actor, row, branch_id, restore_id)


def _selection(world, actor, recipient, channel_id, command, details):
    participant = next((p for row in _channels(world, actor) if row['channel_id'] == channel_id
                        for p in row['participants'] if p['actor_id'] == recipient), None)
    _require(participant is not None)
    _require(isinstance(details, dict), 'invalid_command')
    if command in ('speak', 'offer'):
        _require(command in participant['supported_commands'])
        _require(set(details) == (set() if command == 'speak' else {'offer_id', 'terms'}), 'invalid_command')
    else:
        expected = {'offer_id', 'terms', 'counter_to'} if command == 'counteroffer' else {'offer_id', 'terms_digest'}
        _require(command in ('accept', 'decline', 'withdraw', 'counteroffer') and set(details) == expected, 'invalid_command')
        key = details['counter_to'] if command == 'counteroffer' else details['offer_id']
        row = next((r for r in _offers(world, actor) if r['offer_id'] == key), None)
        _require(row is not None and row['channel_id'] == channel_id
            and {row['offerer'], row['recipient']} == {actor, recipient}
            and command in {r['command'] for r in row['supported_commands']})
        if command == 'counteroffer':
            _require('offer' in participant['supported_commands'])
        else:
            _require(details['terms_digest'] == row['terms_digest'], 'invalid_command')
    if command in ('offer', 'counteroffer'):
        terms = details['terms']
        _require(native._text(details['offer_id'], 256) and isinstance(terms, dict)
            and set(terms) == {'from', 'to', 'material', 'quantity', 'authority_id'}
            and type(terms['quantity']) is int and terms['quantity'] > 0
            and all(native._text(terms[k], 256) for k in ('from', 'to', 'material', 'authority_id')), 'invalid_command')


def prepare(world, *, request_id, actor, recipient, channel_id, command, details,
            intention, source_ref, branch_id, restore_id):
    """No mutation: retain exact edited words and independently selected command."""
    _actor(world, actor)
    _scope(world, branch_id, restore_id)
    _selection(world, actor, recipient, channel_id, command, details)
    from solo_provider import CapabilityUnavailable
    try:
        return native.prepare(world, request_id=request_id, actor=actor, recipient=recipient,
            channel_id=channel_id, command=command, details=details, intention=intention,
            source_ref=source_ref, branch_id=branch_id, restore_id=restore_id)
    except CapabilityUnavailable as error:
        raise CommunicationUnavailable(error.code) from None


def execute(world, request, *, current_scope, persist, explicitly_accepted):
    """Native private pending request, Core authority, safe atomic public result."""
    _require(isinstance(request, native.CommunicationRequest), 'invalid_request')
    _require(explicitly_accepted is True, 'acceptance_required')
    _require(callable(persist), 'persistence_required')
    request.scope.validate(); current_scope.validate()
    _require((current_scope.campaign_id, current_scope.branch_id, current_scope.restore_id) ==
        (request.scope.campaign_id, request.scope.branch_id, request.scope.restore_id)
        and current_scope.campaign_id == world.s['campaign_id'], 'stale_scope')
    _actor(world, request.actor)
    if 'communication:' + request.request_id not in world.s['processed']:
        _selection(world, request.actor, request.recipient, request.channel_id,
                   request.command, json.loads(request.details_json))

    def bridge(expected_scope, candidate_save, raw):
        candidate = CoreWorld.load(candidate_save)
        public = _public(candidate, request.actor, raw, current_scope.branch_id, current_scope.restore_id)
        persist(expected_scope, candidate_save, public)

    from solo_provider import CapabilityUnavailable
    try:
        raw = native.execute(world, request, current_scope=current_scope,
                             persist=bridge, explicitly_accepted=explicitly_accepted)
    except CapabilityUnavailable as error:
        public_error = CommunicationUnavailable(error.code)
        if hasattr(error, 'dependencies'):
            public_error.dependencies = error.dependencies
        raise public_error from None
    return _public(world, request.actor, raw, current_scope.branch_id, current_scope.restore_id)
