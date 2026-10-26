"""Sourced historical openings within existing campaign profiles.

Catalogue inspection is read-only. An explicitly selected snapshot initializes
a new world; reference history does not schedule its later historical outcomes.
The causal clock remains distinct from the snapshot's dated opening boundary.
"""
import copy
import hashlib
import json
import re
from pathlib import Path
from temporal_registry import julian_day, validate_registry

ROOT = Path(__file__).resolve().parent.parent
SCENARIO_ID = 'hundred-years-war'
SNAPSHOTS = {f'hyw-{year}': f'data/hyw_{year}_opening.json' for year in (
    1337,1340,1341,1343,1345,1346,1347,1355,1356,1357,1359,1360,
    1364,1366,1369,1372,1373,1375,1377,1385,1389,1396,1399,1400,
    1403,1411,1415,1417,1419,1420,1422,1429,1435,1444,1449,1450,1453)}


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def historical_catalogue():
    data = json.loads((ROOT / 'data/hyw_entry_catalogue.json').read_text(encoding='utf-8-sig'))
    if data.get('id') != SCENARIO_ID or not _text(data.get('title')):
        raise ValueError('Historical catalogue identity is invalid')
    periods = data['periods']
    entries = data['entries']
    if not isinstance(periods, list) or not isinstance(entries, list):
        raise ValueError('Historical catalogue periods and entries must be lists')
    period_ids = {p['id'] for p in periods}
    if len(period_ids) != len(periods) or any(not _text(p['id']) or not _text(p['name']) for p in periods):
        raise ValueError('Historical period identities must be unique')
    ids, years = set(), set()
    for entry in entries:
        if (not _text(entry.get('id')) or entry['id'] in ids or type(entry.get('year')) is not int
                or entry['year'] in years or entry.get('period_id') not in period_ids
                or not _text(entry.get('title')) or not _text(entry.get('description'))
                or entry.get('status') not in ('proposed', 'developed_historical_setup')):
            raise ValueError('Historical entry identity, year, period or status is invalid')
        ids.add(entry['id'])
        years.add(entry['year'])
    featured = data['featured_years']
    if (not isinstance(featured, list) or any(type(y) is not int for y in featured)
            or len(featured) != len(set(featured)) or not set(featured) <= years):
        raise ValueError('Featured historical years must identify unique catalogue entries')
    return data


def _source_ids(record, sources):
    refs = record.get('source_ids')
    if not isinstance(refs, list) or not refs or len(refs) != len(set(refs)) or not set(refs) <= sources:
        raise ValueError('Historical record requires valid source references')


def validate_entry_guide(guide, source_ids):
    """Shared completeness contract for a developed historical-entry briefing.

    These checks establish structure and traceable references, not factual truth.
    Historical review must still verify the claims against their named sources.
    """
    if not isinstance(guide, dict):
        raise ValueError('A developed historical entry requires a detailed player briefing')
    for section in ('summary', 'immediate_situation', 'player_options',
                    'practical_pressures', 'not_yet_established'):
        paragraphs = guide.get(section)
        if not isinstance(paragraphs, list) or not paragraphs or not all(_text(p) for p in paragraphs):
            raise ValueError('Historical entry briefing requires ' + section)
    if not _text(guide.get('future_rule')):
        raise ValueError('Historical entry briefing must explain the status of later events')
    _source_ids(guide, set(source_ids))


def _validate_snapshot(snapshot, entry):
    if (snapshot.get('schema_version') != 1 or snapshot.get('id') != entry['id']
            or snapshot.get('scenario_id') != SCENARIO_ID
            or snapshot.get('status') != 'developed_historical_setup'
            or entry['status'] != 'developed_historical_setup'
            or type(snapshot.get('revision')) is not int or snapshot['revision'] < 1):
        raise ValueError('Historical snapshot identity, scope, revision or readiness is invalid')
    opening = snapshot['opening']
    date = opening.get('date')
    expected = entry.get('opening_date', '1415-08-11' if entry['id'] == 'hyw-1415' else None)
    if (not isinstance(date, str) or not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', date)
            or int(date[:4]) != entry['year'] or date != expected
            or opening.get('calendar') != 'julian' or opening.get('precision') != 'day'
            or opening.get('time') is not None or not _text(opening.get('boundary'))
            or not _text(opening.get('label'))):
        raise ValueError('Historical snapshot requires its exact selected Julian opening cutoff')
    ordinal = julian_day(*map(int, date.split('-')))
    sources = snapshot['sources']
    if not isinstance(sources, list) or not sources:
        raise ValueError('Historical snapshot requires source provenance')
    source_ids = {source['id'] for source in sources}
    if len(source_ids) != len(sources) or any(not _text(source['id']) or not _text(source.get('title')) for source in sources):
        raise ValueError('Historical source identities must be unique')
    validate_entry_guide(snapshot.get('entry_guide'), source_ids)
    actors = snapshot['actors']
    if not isinstance(actors, list) or len({actor['id'] for actor in actors}) != len(actors):
        raise ValueError('Historical actor identities must be unique')
    for actor in actors:
        if not all(_text(actor.get(key)) for key in ('id', 'name', 'species', 'role')):
            raise ValueError('Historical actor needs an identity and sourced role')
        _source_ids(actor, source_ids)
    domains = snapshot['domains']
    if not isinstance(domains, dict) or set(domains) != {'political', 'military', 'territorial', 'diplomatic'}:
        raise ValueError('Historical opening requires all four declared context domains')
    fact_ids = set()
    for facts in domains.values():
        if not isinstance(facts, list) or not facts:
            raise ValueError('Developed historical context requires sourced domain facts')
        for fact in facts:
            if (not _text(fact.get('id')) or fact['id'] in fact_ids or not _text(fact.get('statement'))
                    or fact.get('knowledge_scope') != 'historical_setup_reference'
                    or not _text(fact.get('effective_not_after'))
                    or fact['effective_not_after'] > opening['date']):
                raise ValueError('Historical context must remain scoped to the selected opening cutoff')
            fact_ids.add(fact['id'])
            _source_ids(fact, source_ids)
    if not isinstance(snapshot.get('unknowns'), list) or not isinstance(snapshot.get('simulation_rules'), list):
        raise ValueError('Historical opening must disclose unknowns and simulation limits')
    registry = snapshot.get('entity_registry_template')
    if not isinstance(registry, dict) or registry.get('as_of') != ordinal or registry.get('axis') != {'id':'julian-day','unit':'day','calendar':'julian'}:
        raise ValueError('Historical registry must match the exact opening coordinate')
    validate_registry(registry, {actor['id']: actor for actor in actors})


def historical_entry(entry_id):
    catalogue = historical_catalogue()
    entry = next((item for item in catalogue['entries'] if item['id'] == entry_id), None)
    if entry is None:
        raise ValueError('Unknown historical entry')
    result = {'entry': copy.deepcopy(entry), 'snapshot': None, 'snapshot_sha256': None, 'ready': False}
    if entry['status'] != 'developed_historical_setup' or entry_id not in SNAPSHOTS:
        return result
    path = ROOT / SNAPSHOTS[entry_id]
    if not path.is_file():
        return result
    raw = path.read_bytes()
    snapshot = json.loads(raw.decode('utf-8-sig'))
    _validate_snapshot(snapshot, entry)
    result.update(snapshot=snapshot, snapshot_sha256=hashlib.sha256(raw).hexdigest(), ready=True)
    return result


def prepare_opening(profile_id, scenario_id=None, entry_id=None, snapshot_sha256=None):
    """Validate one explicit preview selection before creating a save."""
    if scenario_id is None and entry_id is None and snapshot_sha256 is None:
        return None
    if profile_id != 'military' or scenario_id != SCENARIO_ID:
        raise ValueError('This historical scenario belongs to the existing military profile')
    if not _text(entry_id) or not isinstance(snapshot_sha256, str) or len(snapshot_sha256) != 64:
        raise ValueError('Select an entry and its exact preview snapshot hash')
    preview = historical_entry(entry_id)
    if not preview['ready']:
        raise ValueError('This historical entry is proposed; a developed opening snapshot is unavailable')
    if snapshot_sha256 != preview['snapshot_sha256']:
        raise ValueError('The historical opening changed. Refresh its preview before creating a campaign.')
    return preview


def apply_opening(state, selection):
    """Pure initialization into a new empty state; never migrate an existing save."""
    if selection is None:
        return state
    if (state['binding']['campaign_profile'] != 'military' or state['clock'] != 0
            or state.get('historical_start') or state['actors'] or state['player_actor_ids']
            or any(state[key] for key in ('stocks', 'opening_stock', 'capacities', 'activities',
                                          'knowledge', 'orders', 'journal', 'processed', 'pending', 'player_actions'))
            or any(state.get(key) for key in ('evidence', 'obligations', 'designs', 'delegations',
                                              'r9', 'r8_strategy'))):
        raise ValueError('A historical opening can initialize only a new empty military campaign')
    result = copy.deepcopy(state)
    snapshot = copy.deepcopy(selection['snapshot'])
    opening = copy.deepcopy(snapshot['opening'])
    result['binding'].update(scenario_id=SCENARIO_ID, entry_id=selection['entry']['id'],
                             snapshot_sha256=selection['snapshot_sha256'])
    result['historical_start'] = {
        'scenario_id': SCENARIO_ID, 'entry_id': selection['entry']['id'],
        'snapshot_sha256': selection['snapshot_sha256'], 'source_file': SNAPSHOTS[selection['entry']['id']],
        'snapshot': snapshot, 'opening': opening, 'calendar': opening['calendar'], 'date': opening['date'],
        'date_precision': opening['precision'],
        'clock_origin': {'causal_sequence': 0, 'elapsed_time_binding': False},
        'history_origin': {'status': 'unbound', 'partial_opening_year': True},
        'knowledge_scope': 'historical_setup_reference', 'automatic_future_history': False,
        'automatic_narration': False, 'automatic_consolidation': False,
    }
    for actor in snapshot['actors']:
        result['actors'][actor['id']] = {
            'id': actor['id'], 'name': actor['name'], 'species': actor['species'], 'role': actor['role'],
            'current': {}, 'source_ids': copy.deepcopy(actor['source_ids']),
            'source_ref': f'historical-opening:{selection["snapshot_sha256"]}:{actor["id"]}',
            'historical_reference_only': True,
        }
    result['campaign_time'] = {'day': 0, 'time': None, 'precision': 'unresolved',
        'phase': opening['label'] + '; no campaign events advanced',
        'civil': {'date': opening['date'], 'calendar': opening['calendar'],
            'precision': opening['precision'], 'time': None,
            'ordinal': julian_day(*map(int,opening['date'].split('-'))),
            'source_ref': 'historical-opening:'+selection['snapshot_sha256']+':opening',
            'elapsed_calendar_binding': False}}
    return result
