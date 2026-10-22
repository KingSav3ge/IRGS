"""Verify Kira source integrity and references without creating campaign state."""
from pathlib import Path, PurePosixPath
from zipfile import ZipFile
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(root=ROOT):
    root = Path(root).resolve()
    manifest = json.loads((root / 'source_manifest.json').read_text(encoding='utf-8'))
    raw = (root / 'source_text.json').read_bytes()
    require(hashlib.sha256(raw).hexdigest() == manifest['source_text_sha256'], 'Extracted text hash mismatch')
    texts = json.loads(raw)
    source_ids = [s['id'] for s in manifest['sources']]
    require(len(source_ids) == len(set(source_ids)) == 9 and set(source_ids) == set(texts),
            'All nine distinct original documents are required')
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    for source in manifest['sources']:
        relative = PurePosixPath(source['path'])
        require(not relative.is_absolute() and '..' not in relative.parts
                and relative.parts[0] == 'sources' and '\\' not in source['path'], 'Unsafe source path')
        path = root.joinpath(*relative.parts).resolve()
        require(path.is_relative_to(root), 'Source path escapes package')
        require(hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256'],
                'Original document hash mismatch: ' + source['id'])
        with ZipFile(path) as doc:
            tree = ET.fromstring(doc.read('word/document.xml'))
        paragraphs = [''.join(t.text or '' for t in p.findall('.//w:t', ns))
                      for p in tree.findall('.//w:p', ns)]
        require(paragraphs == texts[source['id']]['paragraphs']
                and len(paragraphs) == source['paragraph_count'], 'Extraction differs from original')

    maps = json.loads((root / 'map_catalogue.json').read_text(encoding='utf-8'))['maps']
    map_by_id = {m['id']: m for m in maps}
    require(len(map_by_id) == 6 and set(map_by_id) == {s['id'] for s in manifest['visual_sources']},
            'All six attributed map references are required')
    map_keys = {}
    for m, count in zip(maps, (66, 32, 11, 0, 0, 0)):
        keys = [e['key'] for e in m['entries']]
        require(len(keys) == len(set(keys)) == count, 'Missing or duplicate transcription key')
        require(m['original_image_file'] is None and m['original_image_hash'] is None
                and m['scale'] is None and m['date'] is None, 'No original image, scale or date was established')
        map_keys[m['id']] = set(keys)
    require([e['printed_number'] for e in maps[0]['entries']].count(25) == 2,
            'Original duplicate number 25 must be retained')
    require([e['label'] for e in maps[1]['entries'] if e.get('source_group') == 'Lupine Tribes']
            == ['Woshi Tribe', 'Foxti Tribe', 'Nekhamen Village', 'Coyota Tribe', 'Dingishi Tribe'],
            'Explicit Lupine map grouping must be preserved')

    world = json.loads((root / 'world.json').read_text(encoding='utf-8'))
    require(world['id'] == 'world-of-kira' and world['kind'] == 'campaign_world'
            and world['schema_version'] == 1, 'Unexpected world identity')
    binding = world['binding']
    require(binding['core'] == '3.3' and binding['genre_id'] == binding['campaign_profile_id'] == 'fantasy'
            and binding['library_ids'] == ['shared', 'fantasy'], 'Unexpected IRGS binding')
    require(all(binding[k] is False for k in (
        'numeric_adoption', 'automatic_state_initialization', 'automatic_future_history')),
        'No automatic rule adoption or initialization is authorized')
    ready = world['readiness']
    require(ready['guide_available'] is True and ready['ready'] is False and ready['playable'] is False
            and ready['starting_snapshots'] == [], 'Reference content is not a playable snapshot')
    records = world['records']
    ids = [r['id'] for r in records]
    require(len(ids) == len(set(ids)), 'Duplicate record identity')
    by_id = {r['id']: r for r in records}
    cal = by_id['calendar']
    require(cal['reference_year'] == 1342 and cal['precision'] == 'year'
            and all(cal[k] is None for k in ('month', 'day', 'hour')), 'No exact opening date is established')
    quoted_sources, quote_count = set(), 0
    for r in records + world['continuity_issues']:
        require(bool(r['source_refs']) or bool(r.get('map_source_ids')), 'Missing source reference')
        for ref in r['source_refs']:
            sid, para, quote = ref['source_id'], ref['paragraph'], ref['quote']
            require(sid in texts and type(para) is int and 1 <= para <= len(texts[sid]['paragraphs']),
                    'Invalid paragraph reference')
            require(isinstance(quote, str) and quote.strip() and quote in texts[sid]['paragraphs'][para-1],
                    'Quotation not found: ' + r['id'])
            quoted_sources.add(sid)
            quote_count += 1
        require(set(r.get('map_source_ids', [])) <= set(map_by_id), 'Unknown map source')
        for ref in r.get('map_refs', []):
            require(ref['source_id'] in map_keys and ref['entry_key'] in map_keys[ref['source_id']],
                    'Invalid map entry reference')
    require(quoted_sources == set(source_ids), 'Some original documents are unused')
    for r in records:
        require(r['status'] in ('legacy_source_reference', 'user_confirmed_reference'), 'Unexpected canon status')
        for field in ('people_ids', 'place_ids'):
            require(set(r.get(field, [])) <= set(ids), 'Invalid entity cross-reference')
        for field in ('people_id', 'leader_id', 'region_id'):
            require(r.get(field) is None or r[field] in by_id, 'Invalid entity link')
        if r['category'] == 'event':
            require(type(r['year']) is int and r['era'] in ('B.A.', 'A.A.')
                    and r['automatically_scheduled'] is False, 'Invalid reference event')
        if r['category'] == 'character':
            require(r['player_controlled'] is False, 'No player character was selected')
    issues = world['continuity_issues']
    require(len({i['id'] for i in issues}) == len(issues)
            and all(i['status'] == 'open' and i['resolution'] is None for i in issues),
            'Source conflicts cannot be silently resolved')
    for section in world['guide']['sections']:
        require(section['title'] and section['paragraphs']
                and all(isinstance(p, str) and p.strip() for p in section['paragraphs'])
                and set(section['record_ids']) <= set(ids), 'Invalid world-guide section')
    require(world['guide']['map_catalogues'] == [
        {key: m[key] for key in ('id', 'title', 'entries', 'notes')} for m in maps],
        'Displayed map gazetteer differs from transcription')
    statements = {s['id']: s for s in manifest['user_statements']}
    require(world['geography']['source_refs'] == ['KIRA-U01'] and 'KIRA-U01' in statements,
            'Shelf relationship requires the supplied user statement')
    for region_id in world['geography']['region_ids']:
        require(by_id[region_id]['geographic_relationship_to_other_regions'] == 'separate_continental_shelf'
                and by_id[region_id]['geography_source_refs'] == ['KIRA-U01'],
                'Separate shelf relationship must be preserved')
    expected_key = [('Light Blue', 'Scalian Scalix Imperium'), ('Red', 'Rolling Hills Tribe'),
                    ('Yellow', 'Mountain Peak Tribe'), ('Green', 'Eversong Hollow Tribe'),
                    ('Blue', 'Frozen Lake Tribe'), ('Purple', 'Primatarus Shenyan Republic')]
    require([(k['colour'], k['name']) for k in maps[2]['explicit_user_colour_key']] == expected_key,
            'Aldain must preserve the explicit user colour key')
    for entry in maps[2]['entries']:
        require(entry['political_group_id'] in by_id
                and by_id[entry['political_group_id']]['map_colour'] == entry['visual_group'],
                'Aldain place association must match its explicit colour key')
    return {'original_documents_verified': 9, 'source_records': len(records),
            'exact_quotations_verified': quote_count, 'map_references': len(maps),
            'transcribed_map_entries': sum(len(m['entries']) for m in maps),
            'continuity_questions': len(issues), 'guide_sections': len(world['guide']['sections']),
            'map_pixels_verified': False, 'campaign_state_created': False}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
