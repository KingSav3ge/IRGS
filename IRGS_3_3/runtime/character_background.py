"""Explicit character drafts, separate from resources, control and employment.

These optional values are the creating player's testimony. They do not create
relatives, contracts, money, skills, equipment, nationality rules or authority.
"""
import copy

ARRANGEMENTS = ('independent', 'mercenary', 'retinue', 'civilian', 'institutional', 'undecided')
RELATIONSHIP_STAGES = ('undecided', 'seeking', 'offer_claimed', 'current_claimed', 'former', 'membership_claimed')
FIELDS = {
    'identity': {'origin': 500, 'birthplace': 500, 'nationality': 500, 'culture': 500},
    'life_path': {'family': 2000, 'upbringing': 2000, 'education': 2000},
    'career': {'arrangement': 40, 'relationship_stage': 40, 'organization_id': 160, 'aspiration': 2000},
}


def background_schema():
    return {'schema_version': 1, 'groups': copy.deepcopy(FIELDS),
            'arrangements': list(ARRANGEMENTS), 'relationship_stages': list(RELATIONSHIP_STAGES),
            'required': False, 'record_status': 'player_testimony',
            'employment_or_faction_control_granted': False,
            'note': 'Origin, control perspective and career are independent. An organization to approach is not an accepted appointment or a contract.'}


def validate_background(character, options):
    if not isinstance(character, dict):
        raise ValueError('Character selection must be an object')
    kind = character.get('kind')
    allowed = {'new': {'kind', 'name', 'species', 'background', 'opening_id', *FIELDS},
               'existing': {'kind', 'actor_id', 'opening_id'}, 'faction': {'kind', 'entity_id', 'actor_id'}}
    if kind not in allowed or set(character) - allowed[kind]:
        raise ValueError('Character selection contains unsupported fields for this control perspective')
    if kind != 'new':
        if kind == 'existing' and character.get('opening_id') not in (None, ''):
            if not any(row['id'] == character['opening_id'] and row['actor_id'] == character.get('actor_id')
                       for row in options.get('existing_character_openings', [])):
                raise ValueError('Select a reviewed opening for this existing historical person')
        return {}
    if ('opening_id' in character and (not isinstance(character['opening_id'], str)
            or character['opening_id'] not in ('', *(row['id'] for row in options.get('playable_openings', []))))):
        raise ValueError('Select a reviewed authored opening available for this starting world')
    result = {}
    for group, fields in FIELDS.items():
        if group not in character:
            continue
        source = character[group]
        if not isinstance(source, dict) or set(source) - fields.keys():
            raise ValueError('Unsupported character background fields in ' + group)
        values = {}
        for key, value in source.items():
            if not isinstance(value, str) or len(value) > fields[key]:
                raise ValueError('Character background ' + key + ' must be text within its length limit')
            if value.strip():
                values[key] = value
        if values:
            result[group] = values
    career = result.get('career', {})
    if career.get('arrangement') not in (None, *ARRANGEMENTS):
        raise ValueError('Unknown starting career arrangement')
    if career.get('relationship_stage') not in (None, *RELATIONSHIP_STAGES):
        raise ValueError('Unknown service relationship stage')
    organization = career.get('organization_id')
    if organization is not None and not any(row['id'] == organization and row.get('exists') is True
                                           for row in options.get('factions', [])):
        raise ValueError('Choose an organization that exists in this dated starting world')
    return copy.deepcopy(result)
