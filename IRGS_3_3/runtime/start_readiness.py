"""Versioned readiness, selected starting context and received civil-date view.

Review metadata is out of character. A verified dated reference or eligible
person never implies an executable campaign. Live views use saved state and
received records only; they never initialize or consult a historical template.
"""
import copy
import json
from pathlib import Path

from irgs_reference import digest
from player_actions import _controlled

SCHEMA_VERSION = 'irgs-start-readiness-1'
PACK = Path(__file__).resolve().parents[1]/'data/henry_1415_observation.json'


def existing_opening_options(state):
    historical = state.get('historical_start', {})
    if historical.get('entry_id') != 'hyw-1415':
        return []
    pack = json.loads(PACK.read_text(encoding='utf-8'))
    if historical.get('snapshot_sha256') != pack['snapshot_sha256']:
        return []
    return [{key: copy.deepcopy(pack[key]) for key in
        ('id','actor_id','title','description','requirements','classification','source_refs','review')}
        | {'content_sha256': digest(pack), 'mode': 'supported_slice',
           'supported_actions': [{'operation_id':'execute_player_scene_action',
                                  'action_id':'observe-embarkation','kind':'observe'}]}]


def existing_pack(state, actor, opening_id):
    selected = next((row for row in existing_opening_options(state)
                     if row['actor_id'] == actor and row['id'] == opening_id), None)
    if selected is None:
        raise ValueError('No reviewed existing-person opening matches this actor and dated snapshot')
    pack = json.loads(PACK.read_text(encoding='utf-8'))
    if digest(pack) != selected['content_sha256']:
        raise ValueError('The reviewed existing-person opening changed')
    return pack


def _mode(opening_id=None, *, supported=False, reason='no_selected_execution_adapter'):
    return {'mode_id': opening_id or 'declaration-only',
        'status': 'supported_slice' if supported else 'declaration_only',
        'playable_slice': supported, 'reason_code': 'selected_bounded_handler' if supported else reason,
        'freeform_resolution': False, 'requires_explicit_submission': True}


def annotate_options(state, options):
    """Add public review metadata without querying feasibility or hidden truth."""
    existing = existing_opening_options(state)
    options['existing_character_openings'] = existing
    for actor in options['characters']:
        actor['start_modes'] = [_mode(reason='existing_context_not_established')]
        if not actor['eligible']:
            actor['start_modes'][0].update(status='held', reason_code='character_ineligible')
        else:
            actor['start_modes'] += [_mode(row['id'], supported=True)
                for row in existing if row['actor_id'] == actor['id']]
    options['start_readiness'] = {'schema_version': SCHEMA_VERSION,
        'reference_status': 'verified_dated_reference' if state.get('historical_start') else 'profile_reference',
        'civil_reference': copy.deepcopy(state.get('campaign_time',{}).get('civil')),
        'reference_is_actor_knowledge': False, 'eligibility_is_playability': False,
        'presentation_opening': {'status':'presentation_only', 'grants_capabilities':False},
        'new_character_modes': [_mode()] + [_mode(row['id'], supported=True) for row in options['playable_openings']],
        'authored_new_character_requires': {'kind':'new','species':'human','scenario_id':'individual'}}


def _review(options, character):
    if not isinstance(character, dict) or character.get('kind') not in ('existing','new','faction'):
        raise ValueError('Select a character and explicit starting perspective')
    kind, opening = character['kind'], character.get('opening_id')
    if kind == 'new':
        eligible = options['character_creation_allowed']
        available = [row['id'] for row in options['playable_openings']]
        compatible = str(character.get('species','')).strip().casefold() == 'human'
        reason = 'character_creation_not_allowed'
        actor = None
    else:
        actor = character.get('actor_id')
        key, selected = ('characters', actor) if kind == 'existing' else ('factions', character.get('entity_id'))
        row = next((r for r in options[key] if r['id'] == selected), {})
        eligible = row.get('eligible') is True and (kind != 'faction' or actor in (row.get('control') or {}).get('actor_ids',[]))
        available = [r['id'] for r in options['existing_character_openings'] if r['actor_id'] == actor] if kind == 'existing' else []
        compatible = True; reason = 'character_ineligible'
    mode = _mode(reason='existing_context_not_established' if kind == 'existing' else 'no_selected_execution_adapter')
    if opening:
        mode = _mode(opening, supported=eligible and compatible and opening in available)
        if not mode['playable_slice']:
            mode.update(status='held', reason_code='opening_not_available_for_selection')
    if not eligible:
        mode.update(status='held', playable_slice=False, reason_code=reason)
    return {'schema_version':SCHEMA_VERSION, 'character_kind':kind, 'actor_id':actor,
        'reference_status':options['start_readiness']['reference_status'],
        'reference_is_actor_knowledge':False, 'character_eligible':eligible,
        'selected_mode':mode, 'presentation_opening':copy.deepcopy(options['start_readiness']['presentation_opening']),
        'playable_context': {'status':'selected' if mode['playable_slice'] else 'held',
            'reason_code':mode['reason_code']},
        'known_time_at_creation': {'status':'selected_reference_only','label':options['as_of']['label'],
            'civil':copy.deepcopy(options['start_readiness']['civil_reference']),
            'opening_hour':None,'elapsed_calendar_binding':False}}


def review_start(world, character, *, starting_scenario_id='individual'):
    """Pure pre-creation review. Host recomputes options/digest for creation."""
    if world.s.get('gameplay_started') or world.s['clock'] != 0 or world.s['journal']:
        raise ValueError('Review a new world; continuing worlds use actor_view')
    from starting_selection import options_for_world
    return _review(options_for_world(world, starting_scenario_id), character)


def _receive_civil_date(world, actor, reference):
    """New-world calendar receipt before any later player background testimony."""
    from core_world import CoreWorld
    if any(not e['id'].startswith('setup:') for e in world.s['journal']):
        raise ValueError('Initial calendar reception is unavailable during continuing play')
    result = CoreWorld.load(world.save())
    civil = result.s['campaign_time'].get('civil')
    if civil:
        record = {'kind':'initial_civil_date','schema_version':1, **copy.deepcopy(civil)}
        at = result.s['clock']+1
        result.apply('setup:civil-date', at, 'record_evidence', campaign_id=result.s['campaign_id'],
            source_ref=civil['source_ref'], evidence_id='setup:civil-date', subject=actor,
            assertion=json.dumps(record,ensure_ascii=False,sort_keys=True), status='established')
        result.apply('setup:civil-date-received', at+1, 'receive_evidence', campaign_id=result.s['campaign_id'],
            source_ref=reference, evidence_id='setup:civil-date', recipient=actor)
    return result


def initialize_context(world, character, options, reference):
    """New-world setup only, called by initialize_player before first host save."""
    from core_world import CoreWorld
    started = world.s.get('gameplay_started', {})
    if (started.get('start_readiness') or not started or started.get('instruction_ref') != reference
            or any(not e['id'].startswith('setup:') for e in world.s['journal'])):
        raise ValueError('Starting context can initialize only once before gameplay')
    result = CoreWorld.load(world.save())
    actor = started['actor_id']
    selected = _review(options, character)
    selected['actor_id'] = actor
    result.s['gameplay_started']['start_readiness'] = selected
    if 'setup:civil-date' not in result.s['knowledge'].get(actor,{}):
        result = _receive_civil_date(result,actor,reference)
    return CoreWorld(state=result.s)


def actor_view(world, actor, *, branch_id, restore_id):
    """Current actual capabilities and received setup records, without reseeding."""
    from runtime_contracts import WorldScope
    from shared_runtime import capabilities
    if not _controlled(world.s, actor):
        raise ValueError('Starting context unavailable for this actor')
    scope = WorldScope(world.s['campaign_id'],branch_id,restore_id,world.checksum()); scope.validate()
    records = []
    for key in ('setup:scene-map','setup:scene-location','setup:civil-date'):
        receipt = world.s['knowledge'].get(actor,{}).get(key)
        evidence = world.s['evidence'].get(key)
        if (not receipt or not evidence or evidence['subject'] != actor
                or not evidence['recorded_at'] <= receipt['received_at'] <= world.s['clock']):
            continue
        records.append({'record_id':key,'text':evidence['assertion'],'status':evidence['status'],
            'source_ref':evidence['source_ref'],'recorded_at':evidence['recorded_at'],
            'received_at':receipt['received_at'],'time_axis':'causal_sequence'})
    civil = None
    date = next((r for r in records if r['record_id'] == 'setup:civil-date'), None)
    if date and date['status'] == 'established':
        try:
            received = json.loads(date['text'])
            if received.get('kind') == 'initial_civil_date' and received.get('schema_version') == 1:
                civil = {key:copy.deepcopy(received[key]) for key in
                    ('date','calendar','precision','time','ordinal','source_ref','elapsed_calendar_binding')}
                civil.update(record_id=date['record_id'],status='received_initial_checkpoint',
                    current_calendar_binding=False, opening_hour=None)
        except (ValueError, KeyError, TypeError, AttributeError):
            civil = None
    started = world.s.get('gameplay_started',{})
    saved = started.get('start_readiness',{}) if started.get('actor_id') == actor else {}
    # Creation review includes out-of-character date/reference information. It
    # cannot substitute for this actor's actual received context on later reads.
    selected = {key:copy.deepcopy(saved[key]) for key in
        ('schema_version','character_kind','actor_id','selected_mode','presentation_opening') if key in saved} or None
    caps = [cap.public() for cap in capabilities(world,actor)]
    supported = any(c['operation_id'] != 'record_player_action' for c in caps)
    result = {'schema_version':SCHEMA_VERSION,'actor_id':actor,'selected_start':selected,
        'current_mode':'supported_slice' if supported else 'declaration_only',
        'capability_scope':'shared_runtime_execution_adapters',
        'supported_capabilities':caps,'received_context':records,'civil_time':civil,
        'reference_is_actor_knowledge':False,'templates_reapplied':False,
        'render_usage':{'provider_calls':0,'model_tokens':0}}
    result['snapshot_id']='start:'+digest([scope.campaign_id,branch_id,restore_id,actor,result])
    return result
