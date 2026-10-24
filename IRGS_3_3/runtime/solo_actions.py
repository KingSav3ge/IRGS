"""Trusted host bridge from a validated proposal to existing local Core actions.

The host still owns authentication, save serialization/CAS and restore identity.
No provider can call accept or provide its own request/context. No new world,
resource ledger or arbitrary event dispatcher is introduced here.
"""
from dataclasses import asdict
import copy

from core_world import CoreWorld
from irgs_reference import InvalidEvent, canon
from player_actions import _controlled, _failed_dependencies
from scene_actions import OPERATION, SceneActionUnavailable, execute_scene_action, scene_options
from solo_provider import (ActorRequest, CapabilityUnavailable, RISE_OPERATION, WorldScope, require)

MAX_RECEIVED_RECORDS = 32


def _operation_and_options(world, actor_id):
    if world.s.get('binding', {}).get('campaign_profile') == 'rise':
        from settlement_runtime import ACTIONS
        require(actor_id == 'founder', 'actor_denied')
        # Published action descriptions are conditional attempts. Never inspect
        # grants, private stock/projects or feasibility to select a winning menu.
        return RISE_OPERATION, [{'kind': 'settlement_action', 'action_id': key,
            'title': title, 'description': description} for key, title, description in ACTIONS]
    return OPERATION, scene_options(world.s, actor_id)


def prepare_request(world, *, request_id, actor_id, intention, branch_id, restore_id,
                    allowed_routes, classification, policy_ref, config_version, deadline,
                    max_output_tokens=512):
    """Server-only builder. Source-transfer approval is supplied by the host.

    Options depend on the received map/location, never on hidden blockers or
    stock. Received testimony retains its evidence status and provenance.
    """
    require(isinstance(world, CoreWorld) and _controlled(world.s, actor_id), 'actor_denied')
    operation, options = _operation_and_options(world, actor_id)
    require(bool(options), 'unsupported_action')
    received = []
    refs = []
    for key, receipt in sorted(world.s.get('knowledge', {}).get(actor_id, {}).items()):
        evidence = world.s.get('evidence', {}).get(key)
        if not evidence or not (evidence['recorded_at'] <= receipt['received_at'] <= world.s['clock']):
            continue
        received.append({'id': key, 'assertion': evidence['assertion'], 'status': evidence['status'],
                         'source_ref': evidence['source_ref'], 'received_at': receipt['received_at']})
        refs.append(key)
    if operation == RISE_OPERATION:
        for key, record in sorted(world.s['settlement_receipts'].get(actor_id, {}).items()):
            if not 0 <= record['recorded_at'] <= world.s['clock']:
                continue
            reference = 'settlement-receipt:' + key
            received.append({'id': reference, 'assertion': record['text'], 'status': 'received_outcome',
                'source_ref': world.s['rise']['source_ref'], 'received_at': record['recorded_at'],
                'elapsed_total': record['elapsed_seconds']})
            refs.append(reference)
    total_received = len(received)
    received = sorted(received, key=lambda record: (record['received_at'], record['id']))[-MAX_RECEIVED_RECORDS:]
    refs = [record['id'] for record in received]
    request = ActorRequest(request_id,
        WorldScope(world.s['campaign_id'], branch_id, restore_id, world.checksum()),
        actor_id, intention, canon({'options': options, 'received': received,
            'received_window': {'limit': MAX_RECEIVED_RECORDS, 'total_received': total_received}}),
        tuple(option['action_id'] for option in options), tuple(refs), tuple(allowed_routes),
        classification, policy_ref, config_version, deadline, max_output_tokens, operation_id=operation)
    request.validate()
    return request


def _public_result(world, event_id, request, token):
    if request.operation_id == RISE_OPERATION:
        event = next(item for item in world.s['journal'] if item['id'] == event_id)
        records = world.s['settlement_receipts'][request.actor_id]
        primary, inspection = records[token], records[token + ':inspection']
        return {'status': 'completed_successfully',
            'outcome': {'summary': primary['text'], 'observations': [inspection['text']],
                        'kind': 'settlement_action', 'elapsed_total': primary['elapsed_seconds']},
            'receipt': {'event_id': event_id, 'at': event['at'], 'operation': RISE_OPERATION,
                        'actor': request.actor_id, 'action_id': event['params']['action']}}
    result = copy.deepcopy(world.s['scene_action_results'][event_id])
    result.pop('actor', None)
    # Only the committed handler's actor-legitimate outcome supplies narration.
    # Private dependency certificates and full validation reads are not output.
    return result


def accept_proposal(world, ledger, *, request_id, proposal_digest, actor_id,
                    intention, branch_id, restore_id, explicitly_accepted,
                    persist, clock):
    """Execute once on a clone, then publish through the host's atomic save CAS.

    persist(expected_scope, candidate_save, public_receipt) MUST atomically
    compare the current campaign/branch/restore/state, durably save the candidate
    and its receipt, or raise. It must serialize against all other host writers.
    A lost acknowledgment is recovered by reloading the host save before retry.
    The technical ledger contains no copy of the authoritative campaign save.
    """
    require(explicitly_accepted is True, 'acceptance_required')
    require(callable(persist) and callable(clock), 'persistence_required')
    row = ledger.lookup(request_id)
    require(row is not None, 'unknown_request')
    request = ActorRequest.from_json(row['request'])
    result = ledger.result(request_id)
    require(result.proposal is not None, 'proposal_unavailable')
    proposal = result.proposal
    require(actor_id == request.actor_id, 'actor_denied')
    require(intention == request.intention and proposal_digest == proposal.proposal_digest,
            'acceptance_changed')
    require((world.s['campaign_id'], branch_id, restore_id) ==
            (request.scope.campaign_id, request.scope.branch_id, request.scope.restore_id), 'stale_scope')
    token = 'solo:' + proposal.proposal_digest
    event_id = 'settlement:' + token if request.operation_id == RISE_OPERATION else token
    instruction = 'solo-intent:' + canon({'request_id': request_id, 'intention': intention,
                                         'proposal_digest': proposal_digest})
    action = (proposal.action_id if request.operation_id == RISE_OPERATION else
              {'kind': 'scene_action', 'action_id': proposal.action_id})
    # Core journal and result are the durable authority, including recovery
    # after the save succeeded but the technical acceptance acknowledgment failed.
    if event_id in world.s['processed']:
        event = next(item for item in world.s['journal'] if item['id'] == event_id)
        require(event['op'] == request.operation_id and event['params']['actor'] == actor_id and
                event['params']['action'] == action and event['params']['instruction_ref'] == instruction,
                'receipt_conflict')
        return _public_result(world, event_id, request, token)
    require(row['accepted'] is None, 'restored_future')
    require(result.status == 'proposal_ready', 'proposal_unavailable')
    require(clock() < request.deadline, 'deadline_exceeded')
    require(_controlled(world.s, actor_id), 'actor_denied')
    require(world.checksum() == request.scope.state_digest, 'stale_state')
    current_operation, options = _operation_and_options(world, actor_id)
    require(current_operation == request.operation_id and
            proposal.action_id in {option['action_id'] for option in options},
            'unsupported_action')
    candidate = CoreWorld(state=world.s)
    try:
        if request.operation_id == RISE_OPERATION:
            from settlement_runtime import execute
            certificate = execute(candidate, token, actor_id, action, instruction)['certificate']
        else:
            certificate = execute_scene_action(candidate, event_id, actor_id, action, instruction)['dependencies']
        require(candidate.checksum() == certificate['post_state'], 'observation_refused')
    except InvalidEvent as error:
        if isinstance(error, SceneActionUnavailable):
            dependencies = error.dependencies
        else:
            event = {'id': event_id, 'at': world.s['clock'] + 1, 'op': RISE_OPERATION,
                'params': {'campaign_id': world.s['campaign_id'], 'source_ref': instruction,
                    'instruction_ref': instruction, 'actor': actor_id, 'action': action, 'request_id': token}}
            dependencies = _failed_dependencies(world.s, event)
        with ledger.connection() as db:
            db.execute('UPDATE attempts SET dependencies=? WHERE id=?',
                       (canon(dependencies), request_id))
        raise CapabilityUnavailable('action_unavailable') from None
    public = _public_result(candidate, event_id, request, token)
    # Cancellation and competing acceptors serialize across processes sharing
    # this ledger. The host CAS additionally fences unrelated world writers.
    with ledger.connection() as db:
        db.execute('BEGIN IMMEDIATE')
        current = db.execute('SELECT status,accepted FROM attempts WHERE id=?', (request_id,)).fetchone()
        require(current == ('proposal_ready', None), 'acceptance_conflict')
        require(clock() < request.deadline, 'deadline_exceeded')
        persist(request.scope, candidate.save(), public)
        db.execute('UPDATE attempts SET accepted=?,dependencies=? WHERE id=?',
                   (canon(asdict(request.scope)), canon(certificate), request_id))
    world.s = candidate.s
    return public
