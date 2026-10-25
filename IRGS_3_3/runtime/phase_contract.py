"""Actor-safe host contract over existing selected Core continuations.

Availability means an attempt under selected rules, never a feasibility probe.
Status/commands derive only from received phases. Native Core execution still
owns actual reservations, authority, progress, rejection and durable effects.
"""
import copy
import json

from core_world import CoreWorld
from irgs_reference import digest
from player_actions import _controlled
import process_runtime as native
from runtime_contracts import WorldScope

SCHEMA_VERSION = 'irgs-phase-capabilities-1'
KINDS = frozenset({'observation', 'work'})
PHASE_FIELDS = ('process_id', 'phase_id', 'phase_index', 'actor', 'kind', 'status',
    'terminal', 'original_intention', 'phase_intention', 'summary', 'at', 'source_ref',
    'elapsed_seconds', 'elapsed_total', 'worked_seconds', 'remaining_seconds')
COMMANDS = {'active': ('advance', 'pause', 'cancel', 'inspect'),
            'paused': ('resume', 'cancel', 'inspect'),
            'held': ('pause', 'cancel', 'inspect'), 'completed': ('inspect',), 'cancelled': ()}


class PhaseUnavailable(Exception):
    """Bounded public code; optional dependency evidence is host-private."""
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def _require(condition, code='phase_unavailable'):
    if not condition:
        raise PhaseUnavailable(code)


def _actor(world, actor):
    _require(_controlled(world.s, actor), 'actor_denied')


def _scope(world, branch_id, restore_id):
    scope = WorldScope(world.s['campaign_id'], branch_id, restore_id, world.checksum())
    scope.validate()
    return scope


def _starts(world, actor):
    rows = []
    if world.s.get('binding', {}).get('campaign_profile') == 'rise' and actor == 'founder':
        try:
            rules = native._rules(world.s, 'work', actor)
        except (AssertionError, KeyError, TypeError, ValueError):
            return []
        from settlement_runtime import ACTIONS
        for action, title, description in ACTIONS:
            if action in ('build', 'delegate', 'resume'):
                rows.append({'kind': 'work', 'action_id': action, 'title': title,
                             'description': description, 'source_refs': [rules['source_ref']]})
    else:
        from scene_actions import scene_options
        try:
            rules = native._rules(world.s, 'observation', actor)
        except (AssertionError, KeyError, TypeError, ValueError):
            return []
        for option in scene_options(world.s, actor):
            if rules['actions'][option['action_id']]['kind'] == 'observe':
                rows.append({'kind': 'observation', 'action_id': option['action_id'],
                    'title': option['title'], 'description': option['description'],
                    'source_refs': [rules['source_ref'], rules['receipt_evidence_id']]})
    return [{**row, 'capability_id': 'phase-start:' + digest([actor, row]),
        'operation_id': native.OPERATION, 'command': 'start', 'availability': 'attemptable',
        'requires_explicit_submission': True} for row in rows]


def _received(world, actor, process_id=None):
    return [r for r in world.s.get('process_phase_receipts', {}).values()
            if r['actor'] == actor and r['kind'] in KINDS
            and (process_id is None or r['process_id'] == process_id)]


def _commands(receipt):
    return [{'command': command, 'details_schema': ({'seconds': {'type': 'integer', 'minimum': 1}}
            if command == 'advance' else {}), 'availability': 'attemptable',
            'requires_explicit_submission': True}
            for command in COMMANDS.get(receipt['status'], ())]


def _public(world, actor, receipt, branch_id, restore_id):
    from shared_runtime import committed_receipt
    public = {key: copy.deepcopy(receipt[key]) for key in PHASE_FIELDS}
    public.update(schema_version=SCHEMA_VERSION, status_basis='received_phase', live_status_probed=False,
                  supported_commands=_commands(receipt))
    public['receipt'] = committed_receipt(world, actor, 'process:' + receipt['phase_id'],
                                         branch_id=branch_id, restore_id=restore_id)
    public['presentation'] = public['receipt']['presentation']
    return public


def received_phase(world, actor, phase_id, *, branch_id, restore_id):
    """Retrieve the original received phase, never append live project facts."""
    _actor(world, actor)
    _scope(world, branch_id, restore_id)
    receipt = world.s.get('process_phase_receipts', {}).get(phase_id)
    _require(receipt is not None and receipt['actor'] == actor and receipt['kind'] in KINDS)
    return _public(world, actor, receipt, branch_id, restore_id)


def status(world, actor, process_id, *, branch_id, restore_id):
    _actor(world, actor)
    _scope(world, branch_id, restore_id)
    receipts = _received(world, actor, process_id)
    _require(bool(receipts))
    return _public(world, actor, max(receipts, key=lambda r: r['phase_index']), branch_id, restore_id)


def actor_view(world, actor, *, branch_id, restore_id):
    """Pure selected options and last received outcomes; no private feasibility."""
    _actor(world, actor)
    scope = _scope(world, branch_id, restore_id)
    latest = {}
    for receipt in _received(world, actor):
        key = receipt['process_id']
        if key not in latest or receipt['phase_index'] > latest[key]['phase_index']:
            latest[key] = receipt
    phases = [_public(world, actor, latest[key], branch_id, restore_id) for key in sorted(latest)]
    starts = _starts(world, actor)
    return {'schema_version': SCHEMA_VERSION, 'actor_id': actor,
        'snapshot_id': 'phases:' + digest([scope.campaign_id, branch_id, restore_id, actor, starts, phases]),
        'start_options': starts, 'processes': phases,
        'render_usage': {'provider_calls': 0, 'model_tokens': 0}}


def _prepare(world, **args):
    from solo_provider import CapabilityUnavailable
    try:
        return native.prepare(world, **args)
    except CapabilityUnavailable as error:
        raise PhaseUnavailable(error.code) from None


def prepare_start(world, *, actor, capability_id, process_id, phase_id, intention,
                  source_ref, branch_id, restore_id):
    _actor(world, actor)
    _scope(world, branch_id, restore_id)
    selected = next((row for row in _starts(world, actor) if row['capability_id'] == capability_id), None)
    _require(selected is not None and process_id not in world.s.get('processes', {}))
    return _prepare(world, actor=actor, process_id=process_id, phase_id=phase_id,
        command='start', details={'kind': selected['kind'], 'action_id': selected['action_id']},
        intention=intention, source_ref=source_ref, branch_id=branch_id, restore_id=restore_id)


def prepare_command(world, *, actor, process_id, phase_id, command, details, intention,
                    source_ref, branch_id, restore_id):
    current = status(world, actor, process_id, branch_id=branch_id, restore_id=restore_id)
    _require(command in {row['command'] for row in current['supported_commands']})
    _details(command, details)
    return _prepare(world, actor=actor, process_id=process_id, phase_id=phase_id,
        command=command, details=details, intention=intention, source_ref=source_ref,
        branch_id=branch_id, restore_id=restore_id)


def _details(command, details):
    _require(isinstance(details, dict), 'invalid_command')
    if command == 'advance':
        _require(set(details) == {'seconds'} and type(details['seconds']) is int
                 and details['seconds'] > 0, 'invalid_command')
    else:
        _require(details == {}, 'invalid_command')


def execute(world, request, *, current_scope, persist, explicitly_accepted):
    """Reuse native phase execution; atomically persist only its safe public DTO.

    The private pending request remains native ProcessRequest JSON. After a lost
    acknowledgment reload the host save and retry that exact request. Public
    projections contain neither private parameter hashes nor dependency evidence.
    """
    _require(isinstance(request, native.ProcessRequest), 'invalid_request')
    _require(explicitly_accepted is True, 'acceptance_required')
    _require(callable(persist), 'persistence_required')
    request.scope.validate()
    current_scope.validate()
    _require((current_scope.campaign_id, current_scope.branch_id, current_scope.restore_id) ==
        (request.scope.campaign_id, request.scope.branch_id, request.scope.restore_id), 'stale_scope')
    _require(current_scope.campaign_id == world.s['campaign_id'], 'stale_scope')
    _actor(world, request.actor)
    prior = world.s.get('process_phase_receipts', {}).get(request.phase_id)
    if prior is None:
        if request.command == 'start':
            details = json.loads(request.details_json)
            _require(any(details == {'kind': row['kind'], 'action_id': row['action_id']}
                         for row in _starts(world, request.actor)))
        else:
            current = status(world, request.actor, request.process_id,
                branch_id=current_scope.branch_id, restore_id=current_scope.restore_id)
            _require(request.command in {row['command'] for row in current['supported_commands']})
            _details(request.command, json.loads(request.details_json))
    else:
        _require(prior['actor'] == request.actor and prior['kind'] in KINDS)

    def bridge(expected_scope, candidate_save, raw):
        candidate = CoreWorld.load(candidate_save)
        public = _public(candidate, request.actor, raw, current_scope.branch_id, current_scope.restore_id)
        persist(expected_scope, candidate_save, public)

    from solo_provider import CapabilityUnavailable
    try:
        raw = native.execute(world, request, current_scope=current_scope,
                             persist=bridge, explicitly_accepted=explicitly_accepted)
    except CapabilityUnavailable as error:
        public_error = PhaseUnavailable(error.code)
        if hasattr(error, 'dependencies'):
            public_error.dependencies = error.dependencies  # Host-private, never part of a DTO.
        raise public_error from None
    return _public(world, request.actor, raw, current_scope.branch_id, current_scope.restore_id)
