"""Read-only presentation scopes over the actual saved world.

This local host has one campaign owner, with an explicit creator-inspection
capability. Player views still enforce character knowledge on the server. Raw
state, registry prose and historical setup references are never player context.
"""
import copy


RESULT_FIELDS = ('request_id', 'action_request_id', 'campaign_id', 'actor', 'declaration',
                 'status', 'revision', 'recorded_sequence', 'elapsed_time', 'narrative')


def player_ids(state):
    return state.get('player_actor_ids', ['AST-01'] if state.get('campaign_id') == 'AST' else [])


def character_exists(state, actor_id):
    """Use only the saved registry's current date; old saves stay read-only."""
    if actor_id is None:
        return False
    registry = state.get('entity_registry')
    if registry is None:
        return True
    from temporal_registry import available_entities
    scenario = state.get('starting_control', {}).get('scenario_id', 'individual')
    current = available_entities(registry, scenario_id=scenario)
    return any(row['id'] == actor_id for row in current['characters'])


def controlled_actor(state, actor_id=None, *, required=False):
    available = [key for key in player_ids(state) if key in state.get('actors', {})]
    if actor_id is None or actor_id == '':
        actor_id = available[0] if available else None
    if actor_id is not None and actor_id not in available:
        raise PermissionError('This actor is not a controlled player character')
    if required and actor_id is None:
        raise PermissionError('Select an actual player character before submitting a declaration')
    if required and not character_exists(state, actor_id):
        raise PermissionError('This player character does not exist at the committed playthrough date')
    return actor_id


def safe_result(record):
    return {key: copy.deepcopy(record[key]) for key in RESULT_FIELDS if key in record}


def pending_declaration(record, actor_id):
    for request in record.get('gameplay_requests', {}).values():
        if (request.get('campaign_id') == record['id'] and request.get('kind') == 'declaration'
                and request.get('actor') == actor_id and request.get('status') == 'pending'):
            return safe_result(request['result'])
    return None


def _identity(actor):
    return {key: copy.deepcopy(actor[key]) for key in ('id', 'name', 'species') if key in actor}


def _valid_access(record, clock):
    return (isinstance(record, dict) and record.get('active') is True
            and isinstance(record.get('source_ref'), str) and bool(record['source_ref'].strip())
            and type(record.get('received_at')) is int and record['received_at'] <= clock
            and record['received_at'] >= 0
            and (record.get('valid_until') is None or type(record['valid_until']) is int
                 and record['valid_until'] >= clock))


def _inventory(state, actor_id):
    """Only explicit ongoing inspection rights expose actual stock quantities.

    No ownership/access is inferred from location names or a prose assertion.
    These optional grants are trusted source selections in the existing state;
    inspecting a view never creates one. Received prose remains evidence rather
    than being parsed into a new inventory or an implicit current-stock right.
    """
    access = state.get('gameplay_visibility', {}).get(actor_id, {})
    records = []
    for grant in access.get('inventory', []):
        if not _valid_access(grant, state['clock']) or grant.get('access') != 'inspect_current':
            continue
        location, material = grant.get('location'), grant.get('material')
        stock = state.get('stocks', {}).get(location, {})
        if material in stock:
            records.append({'location': location, 'material': material, 'quantity': stock[material],
                            'source_ref': grant['source_ref'], 'access': 'inspect_current',
                            'ownership': 'not_inferred', 'custody': 'not_inferred'})
    return records


def _chronicle(state, actor_id, evidence, orders, creator=False):
    records = []
    for event in state.get('journal', []):
        params = event.get('params', {})
        op = event['op'].removeprefix('ast_')
        if creator or op == 'record_player_action' and params.get('actor') == actor_id:
            records.append({'id': event['id'], 'kind': 'player_declaration' if op == 'record_player_action' else op,
                'title': 'Player declaration' if op == 'record_player_action' else op.replace('_', ' '),
                'text': params.get('declaration', '') if not creator else str(params),
                'actor_ids': [params['actor']] if params.get('actor') else [],
                'recorded_at': event['at'], 'source_refs': [params['source_ref']] if params.get('source_ref') else [],
                'status': 'declared_not_resolved' if op == 'record_player_action' else 'recorded',
                'source_available': True})
    if not creator:
        for item in evidence:
            records.append({'id': 'receipt:' + item['id'], 'kind': 'evidence_received', 'title': 'Received evidence',
                'text': item['assertion'], 'actor_ids': [item['subject']], 'received_at': item['received_at'],
                'recipient': actor_id, 'areas': ['personal'],
                'source_refs': [item['receipt_ref']], 'status': item['status'], 'source_available': True})
        for item in orders:
            records.append({'id': 'order:' + item['id'], 'kind': 'order_received', 'title': 'Received order',
                'text': item['content'], 'actor_ids': [actor_id], 'received_at': item['received_at'],
                'source_refs': [], 'status': 'executed' if item['executed'] else 'received', 'source_available': True})
    return records


def playthrough(record, actor_id=None, *, mode='player'):
    if mode not in ('player', 'creator'):
        raise ValueError('Unknown presentation mode')
    state = record['state']
    creator = mode == 'creator'
    actor_id = controlled_actor(state, actor_id)
    actor = state.get('actors', {}).get(actor_id)
    evidence, orders = [], []
    known_ids = {actor_id} if actor_id else set()
    if actor_id:
        for eid, receipt in state.get('knowledge', {}).get(actor_id, {}).items():
            source = state.get('evidence', {}).get(eid)
            if not source or receipt['received_at'] > state['clock']:
                continue
            evidence.append({'id': eid, 'subject': source['subject'], 'assertion': source['assertion'],
                'status': source['status'], 'recorded_at': source['recorded_at'],
                'received_at': receipt['received_at'], 'receipt_ref': receipt['source_ref']})
            known_ids.add(source['subject'])
        access = state.get('gameplay_visibility', {}).get(actor_id, {})
        for grant in access.get('known_actors', []):
            if _valid_access(grant, state['clock']) and grant.get('actor_id') in state['actors']:
                known_ids.add(grant['actor_id'])
        for oid, order in state.get('orders', {}).items():
            if order.get('recipient') == actor_id and type(order.get('received_at')) is int and order['received_at'] <= state['clock']:
                orders.append({'id': oid, 'content': copy.deepcopy(order['content']),
                               'received_at': order['received_at'], 'executed': order['executed']})
    identities = [_identity(state['actors'][key]) for key in sorted(known_ids) if key in state['actors']]
    character = {**_identity(actor), 'current': copy.deepcopy(actor.get('current', {}))} if actor else None
    inventory = _inventory(state, actor_id) if actor_id else []
    activities = [{key: copy.deepcopy(activity[key]) for key in ('site', 'start', 'end', 'role') if key in activity}
                  for activity in state.get('activities', {}).values() if actor_id and actor_id in activity.get('actors', [])]
    # Own explicitly agreed commitments are known; a GM's uncommunicated offer is not.
    agreed = {e.get('params', {}).get('obligation_id') for e in state.get('journal', [])
              if e['op'].removeprefix('ast_') == 'record_obligation'
              and e['params'].get('subject') == actor_id and e['params'].get('status') == 'agreed'
              and e['params'].get('instruction_ref')}
    obligations = [{key: copy.deepcopy(value) for key, value in item.items() if key in ('subject', 'description', 'status', 'quantity')}
                   for oid, item in state.get('obligations', {}).items() if oid in agreed]
    current = character['current'] if character else {}
    location = current.get('location')
    if isinstance(location, dict):
        location = location.get('value')
    time = {key: copy.deepcopy(value) for key, value in state.get('campaign_time', {}).items()
            if key in ('day', 'time', 'precision')}
    binding = {key: copy.deepcopy(value) for key, value in state.get('binding', {}).items()
               if key in ('core', 'genre_id', 'library_ids', 'campaign_profile', 'scenario_id', 'entry_id')}
    pending = pending_declaration(record, actor_id) if actor_id else None
    exists = character_exists(state, actor_id)
    result = {'id': record['id'], 'name': record['name'], 'revision': record['revision'], 'mode': mode,
        'actor_id': actor_id, 'requires_character': actor_id is None,
        'character_available': exists,
        'controlled_actors': [_identity(state['actors'][key]) for key in player_ids(state) if key in state['actors']],
        'binding': binding, 'campaign_time': time,
        'scene': {'title': location or 'Current scene', 'location': location,
                  'description': copy.deepcopy(current.get('current_activity', current.get('last_confirmed_activity', 'No character-observed scene record is available.')))},
        'character': character, 'known_actors': identities, 'evidence': evidence, 'orders': orders,
        'inventory': inventory, 'pending_declaration': pending,
        'world': {'actors': identities, 'inventory': inventory, 'activities': activities,
                  'obligations': obligations, 'locations': [location] if location else []},
        'chronicle': _chronicle(state, actor_id, evidence, orders, creator),
        'capabilities': {'can_declare': exists and pending is None, 'can_withdraw': pending is not None,
                         'action_resolution': False, 'narrator': False, 'time_advance': False,
                         'creator_inspection': creator, 'inventory_scope': 'explicit_inspection_grants_only'}}
    if creator:
        result['clock'] = state['clock']
        result['state'] = copy.deepcopy(state)
        result['world'] = {key: copy.deepcopy(state.get(key, {})) for key in
                           ('actors', 'stocks', 'capacities', 'activities', 'obligations', 'designs', 'orders', 'evidence')}
        result['capabilities']['creator_tools'] = True
    from opening_scene import opening_view
    opening = opening_view(state, actor_id)
    result['opening'] = opening
    result['capabilities']['opening_scene'] = opening is not None
    if opening:
        result['chronicle'].insert(0, {'id': opening['id'], 'kind': 'opening_scene', 'title': opening['title'],
            'text': '\n\n'.join(block['text'] for block in opening['blocks']), 'actor_ids': [actor_id],
            'recorded_at': 0, 'status': 'presented', 'source_available': True,
            'source_refs': sorted({sid for block in opening['blocks'] for sid in block['source_ids']})})
        if not current.get('current_activity') and not current.get('last_confirmed_activity'):
            result['scene']['title'] = opening['title']
            result['scene']['description'] = opening['blocks'][0]['text']
    for request in record.get('gameplay_requests', {}).values():
        if request.get('campaign_id') != record['id'] or not creator and request.get('actor') != actor_id:
            continue
        if request.get('kind') == 'declaration' and request.get('status') == 'withdrawn':
            for entry in result['chronicle']:
                if entry['id'] == 'gameplay:' + request['result']['request_id']:
                    entry['status'] = 'withdrawn_not_executed'
        elif request.get('kind') == 'withdrawal':
            result['chronicle'].append({'id': 'withdrawal:' + request['result']['request_id'],
                'kind': 'declaration_withdrawn', 'title': 'Declaration withdrawn',
                'text': 'The player withdrew this unresolved attempt; the original declaration remains recorded.',
                'actor_ids': [request['actor']], 'recorded_at': request['result']['recorded_sequence'],
                'status': 'withdrawn_not_executed', 'source_available': True, 'source_refs': []})
    return result
