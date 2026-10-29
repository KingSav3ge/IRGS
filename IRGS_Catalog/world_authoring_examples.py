"""Validate Catalog-authored requirements, not Engine world-draft contracts."""
from copy import deepcopy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent / 'evaluation/authoring_examples_v1'


def validate(doc):
    if not isinstance(doc, dict) or set(doc) != {'fixture_id', 'classification', 'sources', 'examples'}:
        raise ValueError('Unexpected example content')
    if doc['fixture_id'] != 'irgs-authoring-examples-v1' or doc['classification'] != 'original-fictional-draft-requirements':
        raise ValueError('Invalid identity')
    sources, examples = doc['sources'], doc['examples']
    if not isinstance(sources, list) or len(sources) != 1 or sources[0] != {
        'id': 'catalog-fiction-v1', 'status': 'fictional', 'author': 'IRGS Catalog', 'asset_imports': []}:
        raise ValueError('Only original fictional sources are selected')
    if not isinstance(examples, list) or len(examples) != 2:
        raise ValueError('Two distinct examples required')
    ids, families = set(), set()
    for ex in examples:
        if not isinstance(ex, dict) or set(ex) != {'id', 'family', 'source', 'units', 'places', 'links',
            'actors', 'proposed_items', 'initial_knowledge', 'actor_instructions'}:
            raise ValueError('Invalid example fields')
        if not isinstance(ex['id'], str) or not ex['id'] or ex['id'] in ids:
            raise ValueError('Invalid or duplicate example ID')
        ids.add(ex['id']); families.add(ex['family'])
        if ex['source'] != 'catalog-fiction-v1' or ex['units'] != 'unselected':
            raise ValueError('Unselected source or unit')
        places = ex['places']
        if not isinstance(places, list) or len(places) != 2 or any(not isinstance(p, dict) or set(p) != {'id', 'label'}
            or not all(isinstance(p[k], str) and p[k] for k in ('id', 'label')) for p in places):
            raise ValueError('Two named places required')
        place_ids = {p['id'] for p in places}
        if len(place_ids) != 2 or not isinstance(ex['links'], list) or len(ex['links']) != 1:
            raise ValueError('Duplicate place or missing topology')
        link = ex['links'][0]
        if not isinstance(link, dict) or set(link) != {'from', 'to', 'rules'} or {link['from'], link['to']} != place_ids or link['rules'] != 'unselected':
            raise ValueError('Invalid link or assumed rules')
        actors = ex['actors']
        if not isinstance(actors, list) or len(actors) != 2 or any(not isinstance(a, dict) or set(a) != {'id', 'role'}
            or not isinstance(a['id'], str) or not a['id'] for a in actors):
            raise ValueError('Distinct actors required')
        actor_ids = {a['id'] for a in actors}
        if len(actor_ids) != 2 or {a['role'] for a in actors} != {'player', 'contact'}:
            raise ValueError('Invalid actor roles')
        items = ex['proposed_items']
        if not isinstance(items, list) or len(items) != 1:
            raise ValueError('One proposed item required')
        item = items[0]
        if not isinstance(item, dict) or set(item) != {'id', 'quantity', 'custody_actor', 'initialization'} or not isinstance(item['id'], str) or not item['id'] or type(item['quantity']) is not int or item['quantity'] != 1 or item['custody_actor'] not in actor_ids or item['initialization'] != 'unselected':
            raise ValueError('Invalid proposed item')
        knowledge = ex['initial_knowledge']
        if not isinstance(knowledge, list) or len(knowledge) != 1:
            raise ValueError('Selected initial knowledge required')
        k = knowledge[0]
        player = next(a['id'] for a in actors if a['role'] == 'player')
        if not isinstance(k, dict) or set(k) != {'actor', 'source', 'assertion', 'status'} or k['actor'] != player or k['source'] != ex['source'] or k['status'] != 'fictional-introduction' or not isinstance(k['assertion'], str) or not k['assertion']:
            raise ValueError('Invalid initial knowledge')
        if not isinstance(ex['actor_instructions'], list) or not ex['actor_instructions'] or any(not isinstance(x, str) or not x or 'PRIVATE_' in x for x in ex['actor_instructions']):
            raise ValueError('Invalid actor instructions')
    if families != {'personal-adventure', 'settlement'}:
        raise ValueError('Two distinct families required')
    return {'status': 'verified', 'examples': 2, 'engine_validation_performed': False,
            'world_creation_performed': False, 'alpha_qualified': False}


def load(root=ROOT):
    data = json.loads((Path(root) / 'actor_inputs/examples.json').read_text())
    validate(data)
    return deepcopy(data)


def validate_fixture(catalog_root):
    root = Path(catalog_root) / 'evaluation/authoring_examples_v1'
    actor = load(root)
    oracle = json.loads((root / 'evaluator_only/expectations.json').read_text())
    if (set(oracle) != {'classification', 'marker', 'expectations', 'unresolved'}
        or oracle['classification'] != 'evaluator-only' or oracle['marker'] != 'PRIVATE_AUTHORING_EVALUATOR'
        or oracle['marker'] in json.dumps(actor)
        or set(oracle['expectations']) != {e['id'] for e in actor['examples']}
        or not isinstance(oracle['unresolved'], list) or not oracle['unresolved']):
        raise ValueError('Invalid evaluator separation')
    return validate(actor)
