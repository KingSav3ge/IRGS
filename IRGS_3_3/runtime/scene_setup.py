"""Explicit opt-in authored circumstances for a NEW Solo character only.

The historical template is unchanged. This initializer is never a continuing
world migration or a source of facts about an actual historical person.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

from irgs_reference import digest


PACK = Path(__file__).resolve().parents[1] / 'data' / 'solo_quay_opening.json'


def _pack():
    return json.loads(PACK.read_text(encoding='utf-8'))


def _selected_pack(state):
    entry = state.get('historical_start', {}).get('entry_id') or state.get('binding', {}).get('entry_id')
    if entry == 'hyw-1415':
        return _pack()
    from historical_campaigns import SNAPSHOTS
    if (entry not in SNAPSHOTS or state.get('binding', {}).get('scenario_id') != 'hundred-years-war'
            or state.get('historical_start', {}).get('snapshot', {}).get('id') != entry):
        return None
    pack = json.loads((PACK.parent/'coc_local_delivery.json').read_text(encoding='utf-8'))
    original_id = pack['id']
    selected_id = 'coc-' + entry.removeprefix('hyw-') + '-delivery-v1'
    pack = json.loads(json.dumps(pack).replace(original_id, selected_id))
    label = state['historical_start']['opening']['label']
    pack['description'] += ' Selected checkpoint: ' + label + '.'
    return pack


def opening_options(state):
    pack = _selected_pack(state)
    if pack is None:
        return []
    return [{**{key: copy.deepcopy(pack[key]) for key in
                ('id', 'title', 'description', 'requirements', 'review', 'scope')},
             'content_sha256': digest(pack), 'fictional': True,
             'elapsed_origin_seconds': 0,
             'durations': {'observation_seconds': 20, 'walking_seconds': 45,
                           'shortcut_attempt_seconds': 30, 'delivery_seconds': 10}}]


def initialize_opening(world, character, actor_id, reference):
    opening_id = character.get('opening_id')
    if opening_id in (None, ''):
        return world
    species = world.s.get('actors', {}).get(actor_id, {}).get('species')
    if (character.get('kind') != 'new' or not isinstance(species, str)
            or species.strip().casefold() != 'human'
            or world.s.get('starting_control', {}).get('scenario_id') != 'individual'
            or opening_id not in {row['id'] for row in opening_options(world.s)}):
        raise ValueError('This authored opening requires a new human character in the selected historical individual Solo start')
    if world.s.get('scene_rules') or world.s.get('elapsed_time'):
        raise ValueError('An opening is initialized only once in a new world')
    if (world.s.get('gameplay_started', {}).get('actor_id') != actor_id
            or any(not event['id'].startswith('setup:') for event in world.s['journal'])):
        raise ValueError('Authored circumstances cannot be inserted into a continuing playthrough')
    from core_world import CoreWorld
    result = CoreWorld(state=world.s)
    pack = _selected_pack(world.s)
    source = pack['source_ref']

    def apply(key, op, **params):
        result.apply('setup:scene:' + key, result.s['clock'] + 1, op,
                     campaign_id=result.s['campaign_id'], source_ref=source, **params)

    def evidence(key, assertion):
        apply(key, 'record_evidence', evidence_id='setup:scene-' + key,
              subject=actor_id, assertion=assertion, status='established')
        apply(key + '-receipt', 'receive_evidence', evidence_id='setup:scene-' + key, recipient=actor_id)

    evidence('map', pack['map_text'])
    received_at = result.s['knowledge'][actor_id]['setup:scene-map']['received_at']
    place = pack['initial_place']
    evidence('location', 'Authored opening placement: ' + pack['places'][place]['title'] + '.')
    apply('location-confirmed', 'confirm_character_field', subject=actor_id, field='location',
          value=place, evidence_id='setup:scene-location', authority_ref=reference, instruction_ref=reference)
    evidence('activity', pack['places'][place]['description'])
    apply('activity-confirmed', 'confirm_character_field', subject=actor_id, field='current_activity',
          value=pack['places'][place]['description'], evidence_id='setup:scene-activity',
          authority_ref=reference, instruction_ref=reference)
    evidence('dispatch', 'You have custody of one sealed dispatch entrusted for the receiving clerk\'s tray. It supplies no ownership, pay or office.')
    apply('dispatch-stock', 'establish_stock', location=actor_id, material=pack['initial_material'],
          quantity=1, inventory_evidence_ref='setup:scene-dispatch')
    apply('receiving-tray', 'establish_stock', location=pack['destination'], material=pack['initial_material'],
          quantity=0, inventory_evidence_ref='setup:scene-map')
    # Initial authored physical condition and selected local rules belong to
    # this first world initialization, before its first atomic save. They are
    # never reinstalled when loading, inspecting or advancing an existing game.
    result.s['site_conditions'] = copy.deepcopy(pack['conditions'])
    result.s['scene_rules'] = {key: copy.deepcopy(pack[key]) for key in
                              ('schema_version', 'id', 'source_ref', 'elapsed_axis', 'places', 'actions')}
    result.s['scene_rules'].update(actor_id=actor_id, received_at=received_at,
        receipt_evidence_id='setup:scene-map', setup_instruction_ref=reference,
        content_sha256=digest(pack))
    result.s['elapsed_time'] = {'axis': pack['elapsed_axis'], 'seconds': 0, 'source_ref': source}
    # The setup explicitly gives this character ongoing inspection of the
    # object in their custody; a place name alone grants no inventory access.
    result.s.setdefault('gameplay_visibility', {}).setdefault(actor_id, {}).setdefault('inventory', []).append({
        'active': True, 'source_ref': source, 'received_at': result.s['clock'],
        'access': 'inspect_current', 'location': actor_id, 'material': pack['initial_material']})
    result.s['gameplay_started']['authored_opening'] = {
        'id': opening_id, 'fictional': True, 'instruction_ref': reference,
        'content_sha256': digest(pack), 'civil_calendar_advance': False}
    return CoreWorld(state=result.s)
