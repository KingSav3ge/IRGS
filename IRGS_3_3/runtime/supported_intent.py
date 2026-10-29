"""Explicit, provider-independent review of selected shared Core actions.

A host authenticates the actor and retains the native request privately. Text is
never parsed into an operation and no review, rejection or draft commits a world.
"""
import copy
import json

from irgs_reference import digest
from runtime_contracts import AcceptedIntent, WorldScope
import shared_runtime as shared

SCHEMA_VERSION = 'irgs-supported-intent-1'
GRANT_PREREQUISITES_VERSION = 'irgs-grant-offer-prerequisites-1'


def grant_offer_prerequisites(world, *, actor_id):
    """Expose only selected grant attempts, not hidden offer or eligibility state."""
    capabilities = shared.capabilities(world, actor_id)
    selected = {json.loads(cap.action_json).get('action_id'): cap for cap in capabilities
                if cap.operation_id == shared.SETTLEMENT}
    actions = []
    for action in ('request_grant', 'accept_grant'):
        if action in selected:
            cap = selected[action]
            actions.append({'action_id': action, 'capability_id': cap.capability_id,
                            'title': cap.title, 'source_refs': list(cap.source_refs)})
    return {'schema_version': GRANT_PREREQUISITES_VERSION, 'actor_id': actor_id,
            'status': 'attempts_selected' if len(actions) == 2 else 'not_selected',
            'actions': actions if len(actions) == 2 else [],
            'offer_status': 'not_inspected', 'authority_and_location': 'checked_on_execution',
            'consent_status': 'not_inferred', 'explicit_acceptance_required': True, 'committed': False}


def offer_prerequisites(world, *, actor_id, channel_id, recipient, branch_id, restore_id):
    """Report received attemptable offer selection without probing hidden facts."""
    import communication_contract as communication
    view = communication.actor_view(world, actor_id, branch_id=branch_id, restore_id=restore_id)
    channel = next((row for row in view['channels'] if row['channel_id'] == channel_id), None)
    participant = next((row for row in (channel or {}).get('participants', [])
                        if row['actor_id'] == recipient), None)
    status = ('participant_unavailable' if participant is None else
              'attemptable' if 'offer' in participant['supported_commands'] else 'offer_not_selected')
    return {'schema_version': SCHEMA_VERSION, 'actor_id': actor_id, 'status': status,
            'channel_id': channel_id, 'recipient': recipient,
            'requires_explicit_terms': True, 'requires_explicit_acceptance': True,
            'authority_and_resources': 'checked_on_execution', 'committed': False}


def review_communication(world, *, actor_id, intention, channel_id, recipient, command, details,
                         branch_id, restore_id):
    """Review an explicit selected communication without testing hidden feasibility."""
    import communication_contract as communication
    if not isinstance(intention, str) or not intention.strip() or len(intention) > 4096:
        raise ValueError('Supply exact intention text using 1–4096 characters')
    for value in (channel_id, recipient, command):
        if value is not None and (not isinstance(value, str) or not value.strip() or len(value) > 256):
            raise ValueError('Invalid selected communication identity')
    if details is not None:
        if not isinstance(details, dict):
            raise ValueError('Communication details must be an object')
        try:
            encoded = json.dumps(details, ensure_ascii=False, allow_nan=False)
        except (TypeError, ValueError, RecursionError):
            raise ValueError('Communication details must be bounded data') from None
        if len(encoded) > 4096:
            raise ValueError('Communication details exceed the supported limit')
    scope = WorldScope(world.s['campaign_id'], branch_id, restore_id, world.checksum()); scope.validate()
    # Authenticate actor independently of whether the requested command exists.
    communication.actor_view(world, actor_id, branch_id=branch_id, restore_id=restore_id)
    selection = None
    if command is None or channel_id is None or recipient is None or details is None:
        status = 'clarification_required'
    elif command not in ('speak', 'offer', 'accept', 'decline', 'withdraw', 'counteroffer'):
        status = 'unsupported'
    else:
        try:
            communication.prepare(world, request_id='review-only', actor=actor_id, recipient=recipient,
                channel_id=channel_id, command=command, details=details, intention=intention,
                source_ref='explicit-communication-review', branch_id=branch_id, restore_id=restore_id)
        except communication.CommunicationUnavailable as error:
            status = 'clarification_required' if error.code == 'invalid_command' else 'unsupported'
        else:
            status = 'supported'
            selection = {'operation_id': 'execute_local_communication', 'channel_id': channel_id,
                         'recipient': recipient, 'command': command, 'details': copy.deepcopy(details)}
    identity = 'intent-review:' + digest([SCHEMA_VERSION, scope.campaign_id, branch_id, restore_id,
        scope.state_digest, actor_id, intention, channel_id, recipient, command, details, selection])
    return {'schema_version': SCHEMA_VERSION, 'review_id': identity, 'actor_id': actor_id,
            'intention': intention, 'status': status, 'selection': selection,
            'authorization': 'checked_on_execution', 'requires_explicit_acceptance': True,
            'committed': False, 'provider_calls': 0}


def prepare_communication(world, *, request_id, actor_id, intention, channel_id, recipient, command,
                          details, review_id, branch_id, restore_id, source_ref='explicit-player-submission'):
    import communication_contract as communication
    reviewed = review_communication(world, actor_id=actor_id, intention=intention, channel_id=channel_id,
        recipient=recipient, command=command, details=details, branch_id=branch_id, restore_id=restore_id)
    if reviewed['status'] != 'supported':
        raise shared.SharedActionUnavailable('intent_not_supported')
    if review_id != reviewed['review_id']:
        raise shared.SharedActionUnavailable('review_stale')
    return communication.prepare(world, request_id=request_id, actor=actor_id, recipient=recipient,
        channel_id=channel_id, command=command, details=details, intention=intention,
        source_ref=source_ref, branch_id=branch_id, restore_id=restore_id)


def execute_communication(world, request, *, current_scope, persist, explicitly_accepted):
    import communication_contract as communication
    from communication_runtime import CommunicationRequest
    if not isinstance(request, CommunicationRequest):
        raise shared.SharedActionUnavailable('invalid_request')
    if not callable(persist):
        raise shared.SharedActionUnavailable('persistence_required')
    def public(result):
        return {'schema_version': SCHEMA_VERSION, 'request_id': request.request_id,
                'actor_id': request.actor, 'intention': request.intention,
                'operation_id': 'execute_local_communication', 'status': result['status'],
                'communication': result, 'receipt': result['receipt'], 'presentation': result['presentation']}
    def bridge(expected_scope, candidate_save, result):
        persist(expected_scope, candidate_save, public(result))
    return public(communication.execute(world, request, current_scope=current_scope,
        persist=bridge, explicitly_accepted=explicitly_accepted))


def review(world, *, actor_id, intention, capability_id, branch_id, restore_id):
    if not isinstance(intention, str) or not intention.strip() or len(intention) > 4096:
        raise ValueError('Supply exact intention text using 1–4096 characters')
    scope = WorldScope(world.s['campaign_id'], branch_id, restore_id, world.checksum()); scope.validate()
    capabilities = shared.capabilities(world, actor_id)
    if capability_id is not None and (not isinstance(capability_id, str) or not capability_id.strip() or len(capability_id) > 256):
        raise ValueError('Invalid capability identity')
    capability = next((item for item in capabilities if item.capability_id == capability_id), None)
    status = ('clarification_required' if capability_id is None else
              'supported' if capability is not None and capability.operation_id != shared.DECLARE else 'unsupported')
    selection = None if status != 'supported' else {
        'capability_id': capability.capability_id, 'operation_id': capability.operation_id,
        'action': json.loads(capability.action_json), 'title': capability.title,
        'source_refs': list(capability.source_refs)}
    identity = 'intent-review:' + digest([SCHEMA_VERSION, scope.campaign_id, branch_id, restore_id,
                                        scope.state_digest, actor_id, intention, capability_id, selection])
    return {'schema_version': SCHEMA_VERSION, 'review_id': identity, 'actor_id': actor_id,
            'intention': intention, 'status': status, 'selection': selection,
            'authorization': 'checked_on_execution', 'requires_explicit_acceptance': True,
            'committed': False, 'provider_calls': 0}


def prepare(world, *, request_id, actor_id, intention, capability_id, review_id,
            branch_id, restore_id, source_ref='explicit-player-submission'):
    reviewed = review(world, actor_id=actor_id, intention=intention, capability_id=capability_id,
                      branch_id=branch_id, restore_id=restore_id)
    if reviewed['status'] != 'supported':
        raise shared.SharedActionUnavailable('intent_not_supported')
    if review_id != reviewed['review_id']:
        raise shared.SharedActionUnavailable('review_stale')
    return shared.prepare_intent(world, request_id=request_id, actor_id=actor_id, intention=intention,
        capability_id=capability_id, branch_id=branch_id, restore_id=restore_id, source_ref=source_ref)


def _result(native):
    return {'schema_version': SCHEMA_VERSION, 'request_id': native['request_id'],
            'actor_id': native['actor_id'], 'intention': native['intention'],
            'capability_id': native['capability_id'], 'status': native['status'],
            'receipt': native['receipt'], 'presentation': native['presentation']}


def execute(world, request, *, current_scope, persist, explicitly_accepted):
    if not isinstance(request, AcceptedIntent):
        raise shared.SharedActionUnavailable('invalid_request')
    if request.operation_id == shared.DECLARE:
        raise shared.SharedActionUnavailable('intent_not_supported')
    if not callable(persist):
        raise shared.SharedActionUnavailable('persistence_required')
    def bridge(expected_scope, candidate_save, result):
        persist(expected_scope, candidate_save, _result(result))
    return _result(shared.execute_intent(world, request, current_scope=current_scope,
                                         persist=bridge, explicitly_accepted=explicitly_accepted))
