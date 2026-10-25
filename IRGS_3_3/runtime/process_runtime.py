"""Durable continuations over selected Core work, travel and observation rules.

Work progress remains in Core.projects. A journey persists the local variables
of the existing selected settlement walk; no distances, rates or clocks are
invented. Phase receipts are immutable received outcomes, not another world.
"""
from dataclasses import asdict, dataclass
import copy
import json

from irgs_reference import InvalidEvent, canon, digest
from player_actions import _controlled, _failed_dependencies
from solo_provider import WorldScope

OPERATION = 'continue_player_process'


def _text(value, limit=4096):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= limit


def _status(s, process):
    if process.get('cancelled'):
        return 'cancelled'
    if process['kind'] == 'work':
        return s['projects'][process['project_id']]['status']
    return process['task']['status']


def _rules(s, kind, actor):
    if kind == 'observation':
        from scene_actions import _rules as scene_rules
        rules = scene_rules(s, actor)
        assert s.get('binding', {}).get('campaign_profile') != 'rise', 'no mixed elapsed scheduler binding'
        assert s['elapsed_time']['axis'] == rules['elapsed_axis'] and _text(s['elapsed_time']['source_ref'])
        return rules
    assert s['binding']['campaign_profile'] == 'rise' and s['rise']['review_digest']
    assert actor == 'founder'
    assert s['settlement_model']['id'] == s['rise']['version'] and _text(s['settlement_model']['source_ref'])
    return s['settlement_model']


def reserved_actors(s, excluding=None):
    """Actual unfinished journeys/observation, including paused commitments."""
    return {actor for key, process in s.get('processes', {}).items()
        if key != excluding and process['kind'] != 'work'
        and process['task']['status'] in ('active', 'paused')
        for actor in process['task']['members']}


def _travel_start(s, actor, action):
    from settlement_runtime import _worker_free, household_of, location
    assert action in ('walk_clearing', 'walk_commons')
    household, origin = household_of(s, actor), location(s, actor)
    destination = 'clearing' if action == 'walk_clearing' else 'commons'
    assert origin in ('commons', 'clearing') and origin != destination
    moving_household = 'camp' not in s['settlements']
    members = list(s['households'][household]['members']) if moving_household else [actor]
    route = 'route:' + origin + '-' + destination
    for member in members:
        _worker_free(s, member)
    for member in members:
        s['actors'][member]['current']['location'] = route
    if moving_household:
        assert s['stock_accounts'][household]['site'] == origin
        s['stock_accounts'][household]['site'] = route
    duration = s['settlement_model']['travel_seconds']
    assert type(duration) is int and duration > 0
    return {'status': 'active', 'worked': 0, 'duration': duration, 'origin': origin,
        'destination': destination, 'route': route, 'members': members,
        'household': household if moving_household else None}


def travel_boundaries(s, now):
    return [now + p['task']['duration'] - p['task']['worked']
        for p in s.get('processes', {}).values()
        if p['kind'] == 'travel' and p['task']['status'] == 'active']


def advance_travel(s, delta, at):
    from settlement_runtime import location, notice
    for process_id, process in s.get('processes', {}).items():
        if process['kind'] != 'travel' or process['task']['status'] != 'active':
            continue
        task = process['task']
        assert all(location(s, member) == task['route'] for member in task['members'])
        if task['household'] is not None:
            assert s['stock_accounts'][task['household']]['site'] == task['route']
        assert delta <= task['duration'] - task['worked']
        task['worked'] += delta
        if task['worked'] == task['duration']:
            for member in task['members']:
                s['actors'][member]['current']['location'] = task['destination']
            if task['household'] is not None:
                s['stock_accounts'][task['household']]['site'] = task['destination']
            task['status'] = 'complete'
            notice(s, process['actor'], at, 'process-arrival:' + process_id,
                   'You arrive at the ' + task['destination'] + '.')


def _work_action(core, s, at, p, action):
    from settlement_runtime import operate_settlement_action
    operate_settlement_action(core, s, at, {'campaign_id': p['campaign_id'],
        'actor': p['actor'], 'action': action, 'request_id': 'process-phase:' + p['phase_id'],
        'source_ref': p['source_ref'], 'instruction_ref': p['instruction_ref']})


def operate(core, s, at, p):
    assert set(p) == {'campaign_id', 'source_ref', 'instruction_ref', 'actor', 'process_id',
                     'phase_id', 'phase_index', 'command', 'details', 'intention'}
    assert all(_text(p[key]) for key in ('source_ref', 'instruction_ref', 'intention'))
    assert all(_text(p[key], 256) for key in ('actor', 'process_id', 'phase_id'))
    assert type(p['phase_index']) is int and p['phase_index'] >= 0
    assert _controlled(s, p['actor']), 'actual current actor control required'
    assert isinstance(p['details'], dict)
    processes = s.setdefault('processes', {})
    receipts = s.setdefault('process_phase_receipts', {})
    assert p['phase_id'] not in receipts, 'phase identity already used'
    key, actor, command, details = p['process_id'], p['actor'], p['command'], p['details']
    elapsed_before = s['elapsed_time']['seconds']
    if command == 'start':
        assert key not in processes and p['phase_index'] == 0
        assert set(details) == {'kind', 'action_id'}
        kind = details['kind']
        assert kind in ('work', 'travel', 'observation')
        rules = _rules(s, kind, actor)
        process = {'kind': kind, 'actor': actor, 'original_intention': p['intention'],
            'source_ref': p['source_ref'], 'rule_digest': digest(rules), 'phases': [],
            'started_at': at, 'cancelled': False}
        if kind == 'work':
            assert details['action_id'] in ('build', 'delegate', 'resume')
            assert not any(existing['kind'] == 'work' and existing['project_id'] == 'shelter'
                           and not existing['cancelled'] for existing in processes.values())
            _work_action(core, s, at, p, details['action_id'])
            process['project_id'] = 'shelter'
        elif kind == 'travel':
            process['task'] = _travel_start(s, actor, details['action_id'])
        else:
            from scene_actions import _location, scene_options
            assert actor not in reserved_actors(s)
            assert not any(actor in activity['actors'] for activity in s.get('activities', {}).values())
            action_id = details['action_id']
            assert action_id in {row['action_id'] for row in scene_options(s, actor)}
            action = rules['actions'][action_id]
            assert action['kind'] == 'observe'
            duration = action['duration_seconds']
            assert type(duration) is int and duration > 0
            process['task'] = {'status': 'active', 'worked': 0, 'duration': duration,
                'members': [actor], 'action_id': action_id, 'location': _location(s, actor)}
        processes[key] = process
        # Traced containers detach newly inserted values; mutate the actual
        # stored record so ordinary and observed executions remain identical.
        process = processes[key]
        summary = 'The requested process is scheduled; its work is not complete.'
    else:
        process = processes[key]
        assert process['actor'] == actor and not process['cancelled']
        assert p['phase_index'] == len(process['phases']), 'next phase required'
        assert digest(_rules(s, process['kind'], actor)) == process['rule_digest'], 'selected rule changed'
        kind = process['kind']
        state = _status(s, process)
        if kind == 'work':
            from settlement_runtime import location
            assert location(s, actor) == s['projects'][process['project_id']]['site'], 'local work instruction required'
        if command == 'advance':
            assert set(details) == {'seconds'} and type(details['seconds']) is int and details['seconds'] > 0
            assert state == 'active'
            if kind in ('work', 'travel'):
                from settlement_runtime import _advance
                assert details['seconds'] <= s['settlement_model']['max_advance_seconds']
                span = details['seconds']
                if kind == 'travel':
                    span = min(span, process['task']['duration'] - process['task']['worked'])
                _advance(s, span, causal_at=at)
            else:
                from scene_actions import _location, operate_scene_action
                task = process['task']
                assert _location(s, actor) == task['location']
                delta = min(details['seconds'], task['duration'] - task['worked'])
                task['worked'] += delta
                s['elapsed_time']['seconds'] += delta
                if task['worked'] == task['duration']:
                    task['status'] = 'complete'
                    operate_scene_action(core, s, at, {'campaign_id': p['campaign_id'], 'source_ref': p['source_ref'],
                        'instruction_ref': p['instruction_ref'], 'actor': actor,
                        'action': {'kind': 'scene_action', 'action_id': task['action_id']},
                        'action_event_id': 'process-observation:' + p['phase_id']}, committed_duration=task['duration'])
            summary = 'The selected elapsed process reaches its next committed boundary.'
        elif command in ('pause', 'resume', 'cancel'):
            assert not details
            if kind == 'work':
                if command == 'cancel':
                    assert state in ('active', 'paused', 'held')
                    if state != 'paused':
                        _work_action(core, s, at, p, 'pause')
                    process['cancelled'] = True
                else:
                    _work_action(core, s, at, p, command)
            else:
                task = process['task']
                if command == 'resume':
                    assert state == 'paused'
                    task['status'] = 'active'
                elif command == 'pause':
                    assert state == 'active'
                    task['status'] = 'paused'
                else:
                    # No invented return-trip rule or teleportation from transit.
                    assert kind == 'observation' and state in ('active', 'paused')
                    task['status'] = 'cancelled'
                    process['cancelled'] = True
            summary = 'The process is ' + _status(s, process) + '; committed progress is retained.'
        elif command == 'inspect':
            assert not details
            if kind == 'work':
                _work_action(core, s, at, p, 'inspect')
            summary = 'You review the process at its current local boundary.'
        else:
            raise AssertionError('unsupported process command')
    process['phases'].append(p['phase_id'])
    state = _status(s, process)
    progress = s['projects'][process['project_id']] if process['kind'] == 'work' else process['task']
    result = {'process_id': key, 'phase_id': p['phase_id'], 'phase_index': p['phase_index'],
        'actor': actor, 'kind': process['kind'], 'status': 'completed' if state == 'complete' else state,
        'terminal': state in ('complete', 'cancelled'), 'original_intention': process['original_intention'],
        'phase_intention': p['intention'], 'summary': summary, 'at': at,
        'source_ref': p['source_ref'],
        'elapsed_seconds': s['elapsed_time']['seconds'] - elapsed_before,
        'elapsed_total': s['elapsed_time']['seconds'], 'worked_seconds': progress['worked'],
        'remaining_seconds': progress['duration'] - progress['worked'], 'params_digest': digest(p)}
    receipts[p['phase_id']] = result


def validate(s):
    receipts = s.get('process_phase_receipts', {})
    occupied = set()
    for key, process in s.get('processes', {}).items():
        assert process['actor'] in s['actors'] and process['phases']
        assert process['kind'] in ('work', 'travel', 'observation')
        assert len(process['phases']) == len(set(process['phases']))
        for index, phase in enumerate(process['phases']):
            receipt = receipts[phase]
            assert receipt['process_id'] == key and receipt['phase_index'] == index
            assert receipt['actor'] == process['actor']
        if process['kind'] == 'work':
            assert process['project_id'] in s['projects']
            continue
        task = process['task']
        assert type(task['duration']) is int and type(task['worked']) is int
        assert 0 <= task['worked'] <= task['duration'] and task['duration'] > 0
        assert task['status'] in ('active', 'paused', 'complete', 'cancelled')
        assert (task['worked'] == task['duration']) == (task['status'] == 'complete')
        if task['status'] in ('active', 'paused'):
            assert not occupied.intersection(task['members']), 'actor already reserved by a process'
            occupied.update(task['members'])
            assert not any(set(task['members']).intersection(a['actors']) for a in s.get('activities', {}).values())
            assert not any(p['worker'] in task['members'] and p['status'] == 'active'
                           for p in s.get('projects', {}).values())
        if process['kind'] == 'travel' and task['status'] in ('active', 'paused'):
            from settlement_runtime import location
            assert all(location(s, actor) == task['route'] for actor in task['members'])
            if task['household'] is not None:
                assert s['stock_accounts'][task['household']]['site'] == task['route']
    events = {e['params'].get('phase_id'): e for e in s['journal'] if e['op'] == OPERATION}
    assert set(events) == set(receipts)
    for phase, receipt in receipts.items():
        assert receipt['params_digest'] == digest(events[phase]['params'])


@dataclass(frozen=True)
class ProcessRequest:
    phase_id: str
    process_id: str
    actor: str
    phase_index: int
    command: str
    details_json: str
    intention: str
    source_ref: str
    scope: WorldScope

    def to_json(self):
        return canon(asdict(self))

    @classmethod
    def from_json(cls, raw):
        data = json.loads(raw)
        data['scope'] = WorldScope(**data['scope'])
        return cls(**data)


def prepare(world, *, phase_id, process_id, actor, command, details, intention,
            source_ref, branch_id, restore_id):
    from solo_provider import WorldScope, require
    require(_controlled(world.s, actor), 'actor_denied')
    require(all(_text(value, 256) for value in (phase_id, process_id, actor)), 'invalid_request')
    require(_text(intention) and _text(source_ref), 'invalid_request')
    require(_text(branch_id, 256) and _text(restore_id, 256), 'invalid_request')
    require(isinstance(details, dict) and len(canon(details).encode()) <= 65536, 'invalid_request')
    index = len(world.s.get('processes', {}).get(process_id, {}).get('phases', []))
    return ProcessRequest(phase_id, process_id, actor, index, command, canon(details), intention,
        source_ref, WorldScope(world.s['campaign_id'], branch_id, restore_id, world.checksum()))


def execute(world, request, *, current_scope, persist, explicitly_accepted):
    from core_world import CoreWorld
    from r9_runtime import observe
    from solo_provider import CapabilityUnavailable, require
    from offline_responses import render_receipt
    require(explicitly_accepted is True, 'acceptance_required')
    require(callable(persist), 'persistence_required')
    require((current_scope.campaign_id, current_scope.branch_id, current_scope.restore_id) ==
        (request.scope.campaign_id, request.scope.branch_id, request.scope.restore_id), 'stale_scope')
    require(current_scope.campaign_id == world.s['campaign_id'], 'stale_scope')
    params = {'campaign_id': world.s['campaign_id'], 'source_ref': request.source_ref,
        'instruction_ref': request.intention, 'actor': request.actor, 'process_id': request.process_id,
        'phase_id': request.phase_id, 'phase_index': request.phase_index, 'command': request.command,
        'details': json.loads(request.details_json), 'intention': request.intention}
    event_id = 'process:' + request.phase_id
    if event_id in world.s['processed']:
        event = next(e for e in world.s['journal'] if e['id'] == event_id)
        require(event['op'] == OPERATION and event['params'] == params, 'request_identity_conflict')
        public = copy.deepcopy(world.s['process_phase_receipts'][request.phase_id])
        public['presentation'] = render_receipt(world, request.actor, event_id)
        return public
    require(current_scope == request.scope and world.checksum() == request.scope.state_digest, 'stale_state')
    event = {'id': event_id, 'at': world.s['clock'] + 1, 'op': OPERATION, 'params': params}
    try:
        certificate = observe(world.s, event)
        candidate = CoreWorld(state=world.s)
        candidate.apply(event_id, event['at'], OPERATION, **params)
        require(candidate.checksum() == certificate['post_state'], 'observation_refused')
    except (InvalidEvent, AssertionError, KeyError, TypeError, ValueError):
        error = CapabilityUnavailable('process_unavailable')
        error.dependencies = _failed_dependencies(world.s, event)
        raise error from None
    public = copy.deepcopy(candidate.s['process_phase_receipts'][request.phase_id])
    public['presentation'] = render_receipt(candidate, request.actor, event_id)
    persist(request.scope, candidate.save(), public)
    world.s = candidate.s
    return public


def received_status(world, actor, process_id):
    from solo_provider import require
    require(_controlled(world.s, actor), 'actor_denied')
    process = world.s.get('processes', {}).get(process_id)
    require(process is not None and process['actor'] == actor, 'actor_denied')
    # Read the actual received phase, never reveal remote live project progress.
    return copy.deepcopy(world.s['process_phase_receipts'][process['phases'][-1]])
