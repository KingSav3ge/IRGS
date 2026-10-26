"""Solo starting review over shared temporal entities and the actual Core world.

Only a new world is initialized here. Continuing games never call a historical
template loader to answer availability questions. New player identities and
their declarations of background are recorded through the same Core journal.
"""
import copy
import json

from irgs_reference import digest
from character_background import background_schema, validate_background


SCENARIO_ID = 'individual'


def _scenario():
    return {'id': SCENARIO_ID, 'title': 'Solo · individual character',
            'character_creation_allowed': True,
            'description': 'Control one character. Institutional orders still require actual authority and resources.'}


def _version(point, source_ref, **fields):
    return {'start': point, 'end': None, 'source_ref': source_ref, **fields}


def initial_entity_registry(state):
    """Initialize new-profile metadata; never use this to migrate a saved game."""
    from temporal_registry import snapshot_registry, validate_registry
    snapshot = state.get('historical_start', {}).get('snapshot', {})
    template = snapshot.get('entity_registry_template')
    if template is not None:
        registry = snapshot_registry(template, template['as_of'])
        validate_registry(registry, state['actors'])
        return registry
    point = state.get('campaign_time', {}).get('day', 0)
    profile = state['binding']['campaign_profile']
    registry = {'schema_version': 1, 'source_mode': 'playthrough',
                'axis': {'id': 'campaign-day', 'unit': 'day'}, 'as_of': point,
                'entities': {}, 'relations': {}, 'eligibility': {},
                'scenarios': {SCENARIO_ID: _scenario()},
                'origin': {'kind': 'new_profile_initialization', 'profile_id': profile,
                           'elapsed_calendar_binding': False}}
    for actor_id, actor in state['actors'].items():
        source = 'profile:' + profile + ':' + actor_id
        registry['entities'][actor_id] = {'id': actor_id, 'kind': 'character',
            'versions': [_version(point, source, exists=True,
                identity={'name': actor['name'], 'category': 'person', 'species': actor['species']},
                formation_time=None, resources_status='uninitialized', territory_refs=[], resource_refs=[])]}
        eligible = actor_id in state.get('player_actor_ids', [])
        registry['eligibility'][SCENARIO_ID + ':' + actor_id] = {
            'entity_id': actor_id, 'scenario_id': SCENARIO_ID,
            'versions': [_version(point, source, eligible=eligible,
                reason='The profile designates this player character.' if eligible else 'This profile has not selected this person for player control.',
                control={'mode': 'individual', 'actor_ids': [actor_id] if eligible else [],
                         'powers': ['declare_own_intent'] if eligible else []})]}
    validate_registry(registry, state['actors'])
    return registry


def options_for_world(world, starting_scenario_id=SCENARIO_ID):
    """New-world review data, not a permission projection for a continuing PC."""
    from temporal_registry import available_entities, validate_registry
    state = world.s
    registry = state.get('entity_registry')
    if registry is None:
        raise ValueError('This starting profile has no temporal entity registry')
    validate_registry(registry, state['actors'])
    if starting_scenario_id not in registry['scenarios']:
        raise ValueError('The selected starting scenario is not defined for this world')
    availability = available_entities(registry, scenario_id=starting_scenario_id)
    opening = state.get('historical_start', {}).get('opening', {})
    label = opening.get('label') or ('Campaign day ' + str(state['campaign_time'].get('day', 0)))
    scenario = registry['scenarios'][starting_scenario_id]
    result = {'available': True,
        'source': 'historical_template' if state.get('historical_start') else 'profile_setup',
        'profile_id': state['binding']['campaign_profile'],
        'as_of': {'ordinal': availability['as_of'], 'axis': copy.deepcopy(availability['axis']), 'label': label},
        'scenarios': [copy.deepcopy(item) for item in registry['scenarios'].values()],
        'default_scenario_id': starting_scenario_id,
        'factions': copy.deepcopy(availability['factions']),
        'characters': copy.deepcopy(availability['characters']),
        'character_creation_allowed': scenario.get('character_creation_allowed') is True,
        'background_schema': background_schema(),
        'play_mode': 'solo', 'automatic_national_control': False,
        'snapshot_sha256': state.get('historical_start', {}).get('snapshot_sha256'),
        'entry_description': copy.deepcopy(state.get('historical_start', {}).get('snapshot', {}).get('entry_guide')),
        'control_note': 'Control covers the selected person’s voluntary declarations. It does not supply possessions, expertise or institutional authority.'}
    from scene_setup import opening_options
    result['playable_openings'] = opening_options(state)
    from start_readiness import annotate_options
    annotate_options(state, result)
    result['selection_digest'] = digest(result)
    return result


def starting_options(profile_id='ast', scenario_id=None, entry_id=None,
                     snapshot_sha256=None, starting_scenario_id=SCENARIO_ID, custom_year=None):
    from campaign_library import initial_campaign
    if custom_year not in (None, ''):
        if isinstance(custom_year, bool):
            raise ValueError('A custom year must be a whole calendar year')
        try:
            year = int(custom_year)
        except (TypeError, ValueError):
            raise ValueError('A custom year must be a whole calendar year')
        if str(year) != str(custom_year).strip():
            raise ValueError('A custom year must be a whole calendar year')
        from historical_campaigns import historical_entry
        if not entry_id:
            return {'available': False, 'source': 'historical_template', 'custom_year': year,
                    'reason': 'No designated, verified starting snapshot is selected for this date.'}
        preview = historical_entry(entry_id)
        if not preview['ready'] or preview['entry']['year'] != year:
            return {'available': False, 'source': 'historical_template', 'custom_year': year,
                    'reason': 'This year has no matching developed snapshot. A nearby year is never substituted.'}
    world = initial_campaign(profile_id, 'STARTING-PREVIEW', scenario_id=scenario_id,
                             entry_id=entry_id, snapshot_sha256=snapshot_sha256)
    return options_for_world(world, starting_scenario_id)


def initialize_player(world, character=None, starting_scenario_id=SCENARIO_ID,
                      selection_digest=None, request_ref=None):
    """Complete explicit Solo setup in memory before the first campaign save."""
    from core_world import CoreWorld
    options = options_for_world(world, starting_scenario_id)
    legacy_default = character is None and world.s['binding']['campaign_profile'] == 'ast'
    if legacy_default:
        character = {'kind': 'existing', 'actor_id': 'AST-01'}
    if not isinstance(character, dict):
        raise ValueError('Create a character or select an eligible existing character before starting the game')
    details = validate_background(character, options)
    if not legacy_default and selection_digest != options['selection_digest']:
        raise ValueError('Starting availability changed. Review the scenario and character choices again.')
    if selection_digest is not None and selection_digest != options['selection_digest']:
        raise ValueError('Starting availability changed. Review the scenario and character choices again.')
    if world.s['journal'] or world.s['clock'] != 0 or world.s.get('gameplay_started'):
        raise ValueError('Starting selection applies only to a newly initialized world')
    result = CoreWorld.load(world.save())
    reference = request_ref or 'explicit-solo-start:' + result.s['campaign_id']
    if not isinstance(reference, str) or not reference.strip():
        raise ValueError('An explicit player starting instruction is required')
    registry = result.s['entity_registry']
    effective = registry['as_of']
    sequence = result.s['clock']

    def apply(key, op, **params):
        nonlocal sequence
        sequence += 1
        result.apply('setup:' + key, sequence, op, campaign_id=result.s['campaign_id'],
                     source_ref=reference, **params)

    kind = character.get('kind')
    selected_entity_id = None
    if kind == 'new':
        if not options['character_creation_allowed']:
            raise ValueError('This scenario does not permit a newly created character')
        name, species = character.get('name'), character.get('species')
        background = character.get('background', '')
        if (not isinstance(name, str) or not name.strip() or len(name) > 100
                or not isinstance(species, str) or not species.strip() or len(species) > 80
                or not isinstance(background, str) or len(background) > 10000):
            raise ValueError('Supply a character name, species and a background of at most 10000 characters')
        actor_id = 'PC-' + digest(result.s['campaign_id'])[:24]
        apply('actor', 'register_actor', actor_id=actor_id, name=name.strip(), species=species.strip(),
              player_controlled=False)
        if actor_id not in result.s['entity_registry']['entities']:
            apply('entity', 'register_entity', entity_id=actor_id, kind='character', effective_at=effective,
                  identity={'name': name.strip(), 'category': 'person', 'species': species.strip()})
        apply('eligibility', 'record_entity_eligibility', entity_id=actor_id,
              scenario_id=starting_scenario_id, effective_at=effective, eligible=True,
              reason='The player explicitly created this Solo character.',
              control={'mode': 'individual', 'actor_ids': [actor_id], 'powers': ['declare_own_intent']})
        from start_readiness import _receive_civil_date
        result = _receive_civil_date(result, actor_id, reference)
        sequence = result.s['clock']
        if background.strip():
            apply('background', 'record_evidence', evidence_id='setup:background', subject=actor_id,
                  assertion=background, status='testimony', originator=actor_id)
            apply('background-receipt', 'receive_evidence', evidence_id='setup:background', recipient=actor_id)
        if details:
            apply('background-details', 'record_evidence', evidence_id='setup:background-details', subject=actor_id,
                  assertion=json.dumps({'kind': 'character_background', 'schema_version': 1, 'details': details},
                                       ensure_ascii=False, sort_keys=True),
                  status='testimony', originator=actor_id)
            apply('background-details-receipt', 'receive_evidence', evidence_id='setup:background-details', recipient=actor_id)
    elif kind == 'existing':
        actor_id = character.get('actor_id')
        chosen = next((item for item in options['characters'] if item['id'] == actor_id), None)
        if not chosen or chosen.get('eligible') is not True:
            raise ValueError('This character is not eligible in the selected date and scenario')
    elif kind == 'faction':
        selected_entity_id = character.get('entity_id')
        actor_id = character.get('actor_id')
        chosen = next((item for item in options['factions'] if item['id'] == selected_entity_id), None)
        if (not chosen or chosen.get('eligible') is not True
                or actor_id not in (chosen.get('control') or {}).get('actor_ids', [])):
            raise ValueError('Faction control requires an eligible scenario and an explicitly permitted character')
    else:
        raise ValueError('Choose an existing character or complete new-character creation')
    apply('control', 'select_entity_control', entity_id=selected_entity_id or actor_id, actor_id=actor_id,
          scenario_id=starting_scenario_id, effective_at=effective, instruction_ref=reference)
    if not result.s.get('player_actor_ids'):
        raise ValueError('A Solo campaign cannot start without a controlled character')
    result.s['gameplay_started'] = {'mode': 'solo', 'starting_scenario_id': starting_scenario_id,
        'actor_id': actor_id, 'availability_digest': options['selection_digest'],
        'instruction_ref': reference, 'background_status': 'player_testimony_not_automatic_capabilities'}
    if result.s.get('historical_start'):
        from historical_plans import baseline_view, initialize_plans
        baseline = baseline_view(result.s['historical_start']['entry_id'])
        plans = initialize_plans(baseline, result.s)
        plans.update(baseline_snapshot=copy.deepcopy(baseline), storage='saved_prospective_reference',
                     installed_schedule=False)
        result.s['historical_planning'] = plans
    from start_readiness import initialize_context
    result = initialize_context(CoreWorld(state=result.s), character, options, reference)
    from scene_setup import initialize_opening
    return initialize_opening(result, character, actor_id, reference, options=options)
