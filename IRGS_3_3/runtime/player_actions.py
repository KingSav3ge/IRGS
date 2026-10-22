"""One bounded player action over the selected Core's existing stock handler.

Received orders describe choices, not omniscient eligibility reports. Execution
requires the selected character's actual control and an explicit current mandate
whose identity is the order's authority reference. No title, background prose or
order content is parsed into authority. Mandates are sourced selections, not a
claim that historical legal authority has been independently established.

The causal coordinate used here orders a commit; it is not elapsed time. Durable
submission/retry lookup belongs to the host's atomic campaign/request record.
"""
from __future__ import annotations

import copy

from irgs_reference import InvalidEvent, digest


OPERATION = 'execute_player_equipment_issue'
UNAVAILABLE = 'This received order cannot currently be carried out. No equipment was issued.'


class PlayerActionUnavailable(InvalidEvent):
    """Safe public reason with private execution evidence for the host ledger."""
    def __init__(self, dependencies):
        super().__init__(UNAVAILABLE)
        self.dependencies = dependencies


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _action(action):
    if (not isinstance(action, dict) or set(action) != {'kind', 'order_id'}
            or action.get('kind') != 'issue_equipment' or not _text(action.get('order_id'))):
        raise InvalidEvent('Choose a supported received equipment order')


def _present(state, actor_id):
    if actor_id not in state.get('actors', {}):
        return False
    registry = state.get('entity_registry')
    if registry is None:
        return True  # Legacy states have no temporal registry to query or invent.
    from temporal_registry import available_entities
    scenario = state.get('starting_control', {}).get('scenario_id', 'individual')
    return any(row['id'] == actor_id for row in
               available_entities(registry, scenario_id=scenario)['characters'])


def _controlled(state, actor_id):
    """Revalidate current selected-entity policy, not an old player-list entry.

    A faction representative needs the faction's current control policy; that
    person's unrelated individual eligibility neither grants nor removes the
    faction's powers. Legacy state has no registry policy to infer or install.
    """
    from core_world import CoreWorld
    if actor_id not in CoreWorld.player_ids(None, state) or not _present(state, actor_id):
        return False
    registry = state.get('entity_registry')
    if registry is None:
        return True
    from temporal_registry import available_entities
    selected = state.get('starting_control', {})
    if selected and selected.get('actor_id') != actor_id:
        return False
    available = available_entities(registry, scenario_id=selected.get('scenario_id', 'individual'))
    entity_id = selected.get('entity_id', actor_id)
    row = next((item for item in available['factions'] + available['characters']
                if item['id'] == entity_id), None)
    control = (row or {}).get('control') or {}
    return bool(row and row['eligible'] and actor_id in control.get('actor_ids', [])
                and 'declare_own_intent' in control.get('powers', [])
                and (not selected or control.get('mode') == selected.get('mode')))


def equipment_options(state, actor_id):
    """Project only structured directives actually received by this character.

    Stock, mandate validity, other actors' names and hidden rejection reasons are
    never read to select these choices. A stale order remains an attemptable
    received instruction until its execution result is known; execution always
    revalidates current authority and stock. This is not an eligibility oracle.
    """
    if (state.get('binding', {}).get('genre_id') not in {'military', 'roman'}
            or not _controlled(state, actor_id)):
        return []
    options = []
    for order_id, order in state.get('orders', {}).items():
        if (order.get('recipient') != actor_id or type(order.get('received_at')) is not int
                or order['received_at'] > state['clock'] or order.get('executed') is not False):
            continue
        directive = order.get('directives', {})
        people = directive.get('persons')
        if (directive.get('operation') != 'issue_equipment'
                or not isinstance(people, list) or not people or not all(_text(x) for x in people)
                or type(directive.get('quantity_each')) is not int or directive['quantity_each'] <= 0
                or not _text(directive.get('material')) or not _text(directive.get('from'))):
            continue
        text = (f"Carry out received order {order_id}: issue {directive['quantity_each']} "
                f"{directive['material']} to each of {len(people)} listed recipient(s) "
                f"from {directive['from']}.")
        options.append({'kind': 'issue_equipment', 'order_id': order_id,
                        'title': 'Issue equipment — ' + order_id,
                        'description': copy.deepcopy(order.get('content', 'Received equipment order')),
                        'text': text})
    return options


def operate_equipment_action(core, state, at, params):
    """Called inside Core.apply's cloned transaction and R9's traced execution."""
    action = params['action']
    _action(action)
    actor = params['actor']
    assert _controlled(state, actor), 'actual current player control required'
    assert _text(params.get('instruction_ref')), 'explicit player instruction required'
    order = state['orders'][action['order_id']]
    assert (order['recipient'] == actor and type(order['received_at']) is int
            and order['received_at'] <= state['clock']), 'received order required'
    assert order.get('revoked', False) is False, 'order is revoked'
    authority = order['authority_ref']
    mandate = state.get('r9', {}).get('mandates', {})[authority]
    assert mandate.get('active') is True and mandate['actor'] == actor, 'current scoped authority required'
    assert (type(mandate['effective_at']) is int
            and mandate['effective_at'] <= state['clock']), 'authority is not effective'
    assert _text(mandate.get('source_ref')), 'sourced authority required'
    assert (isinstance(mandate['operations'], list)
            and 'military_issue_equipment' in mandate['operations']), 'authority does not cover equipment issue'
    if mandate.get('valid_until') is not None:
        assert type(mandate['valid_until']) is int and at <= mandate['valid_until'], 'authority expired'
    directive = order['directives']
    people = directive['persons']
    assert isinstance(people, list) and people, 'explicit recipients required'
    assert all(_present(state, person) for person in people), 'a recipient no longer exists'
    core._operate(state, at, 'military_issue_equipment', {
        'order_id': action['order_id'], 'commander': actor,
        'persons': list(people), 'material': directive['material'],
        'from': directive['from'], 'quantity_each': directive['quantity_each'],
        'authority_ref': authority, 'source_ref': params['source_ref']})


def _failed_dependencies(state, event):
    """Retain attempted reads without describing rolled-back writes as effects.

    Both ordinary and instrumented execution must reproduce the same atomic
    rejection. A mismatch remains unqualified. This private diagnostic record is
    not a successful certificate; conservative collection granularity remains.
    """
    from r8_dependencies import code_identity
    from r9_runtime import observe_rejection
    try:
        return observe_rejection(state, event)
    except (InvalidEvent, AssertionError, KeyError, TypeError, ValueError):
        # An observer mismatch is not evidence that ordinary execution rejects.
        # Keep the public action unavailable without manufacturing qualification.
        pass
    return {'event': copy.deepcopy(event), 'snapshot': digest(state), 'code': code_identity(),
            'status': 'observation_refused', 'successful_certificate': False,
            'reason_code': 'rejection_not_qualified', 'reads': [], 'writes': [],
            'attempted_writes': [], 'validation_reads': []}


def execute_equipment_action(world, event_id, actor_id, action, instruction_ref):
    """Observe, validate and atomically execute one fresh supported request.

    Host persistence must save the returned outcome/receipt with world.s in one
    atomic campaign write before acknowledging it. Existing request lookup must
    occur before this function; a reused event identity is never a new action.
    """
    from core_world import CoreWorld
    from r9_runtime import observe
    _action(action)
    if not _text(event_id) or not _text(actor_id) or not _text(instruction_ref):
        raise InvalidEvent('Action identity, character and explicit instruction required')
    if not isinstance(world, CoreWorld):
        raise InvalidEvent('This action requires the selected campaign-state kernel')
    if event_id in world.s['processed']:
        raise InvalidEvent('Retrieve the original request result instead of repeating this event')
    event = {'id': event_id, 'at': world.s['clock'] + 1, 'op': OPERATION,
             'params': {'campaign_id': world.s['campaign_id'], 'actor': actor_id,
                        'action': copy.deepcopy(action), 'instruction_ref': instruction_ref,
                        'source_ref': instruction_ref}}
    try:
        certificate = observe(world.s, event)
    except (InvalidEvent, AssertionError, KeyError, TypeError, ValueError) as error:
        raise PlayerActionUnavailable(_failed_dependencies(world.s, event)) from error
    candidate = CoreWorld(state=world.s)
    candidate.apply(event['id'], event['at'], event['op'], **event['params'])
    directive = candidate.s['orders'][action['order_id']]['directives']
    transfers = [{'from': directive['from'], 'to': person, 'material': directive['material'],
                  'quantity': directive['quantity_each']} for person in directive['persons']]
    summary = (f"Issued {directive['quantity_each']} {directive['material']} to each of "
               f"{len(transfers)} listed recipient(s) under received order {action['order_id']}.")
    outcome = {'summary': summary, 'transfers': transfers}
    receipt = {'event_id': event_id, 'at': event['at'], 'operation': OPERATION,
               'actor': actor_id, 'order_id': action['order_id']}
    world.s = candidate.s
    return {'status': 'completed_successfully', 'outcome': outcome,
            'receipt': receipt, 'dependencies': certificate}
