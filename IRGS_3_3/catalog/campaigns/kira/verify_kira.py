"""Verify adopted Kira canon and its superseded archive without creating campaign state."""
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
    archive = json.loads((root / 'archive/legacy_reference.json').read_text(encoding='utf-8'))
    policy = json.loads((root / 'canon.json').read_text(encoding='utf-8'))
    require(archive['status'] == 'superseded_archive' and archive['canon_authority'] is False
            and policy == world['canon_policy']
            and policy['status'] == 'adopted_world_canon'
            and policy['adoption_source_refs'] == ['KIRA-U06']
            and policy['original_documents_canon_authority'] is False
            and world['archival_sources']['canon_authority'] is False
            and world['content_status'] == 'expanded_setting_canon',
            'Expanded lore is adopted canon; superseded originals cannot overrule it')
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
    for r in archive['records'] + archive['continuity_issues']:
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
        require(r['status'] == 'world_canon' and r['canon_source_refs'] == ['KIRA-U06'],
                'Current setting records require adopted canon provenance')
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
            and all(i['status'] in ('resolved_in_current_canon', 'further_development') for i in issues),
            'Continuity decisions must distinguish resolved canon from further development')
    decisions = {d['id']: d['resolution'] for d in policy['editorial_decisions']}
    require(all(i['resolution'] == decisions[i['id']] for i in issues if i['id'] in decisions)
            and {i['id'] for i in issues if i['status'] == 'resolved_in_current_canon'} == set(decisions)
            and by_id['kieran']['people_id'] == 'flatland-elves'
            and by_id['kieran']['wartime_service_years'] == 228
            and by_id['flatland-elves']['reference_lifespan_years'] == 1000,
            'Current chronology, names and the Long Renewal must follow recorded canon decisions')
    for section in world['guide']['sections']:
        require(section['title'] and section['paragraphs']
                and all(isinstance(p, str) and p.strip() for p in section['paragraphs'])
                and set(section['record_ids']) <= set(ids), 'Invalid world-guide section')
    require([{key: m[key] for key in ('id', 'title', 'entries')}
             for m in world['guide']['map_catalogues']] == [
        {key: m[key] for key in ('id', 'title', 'entries')} for m in maps]
        and any('Current canon uses Karkaria' in note
                for note in world['guide']['map_catalogues'][0]['notes']),
        'Map labels must retain the transcription while current naming follows adopted canon')
    statements = {s['id']: s for s in manifest['user_statements']}
    require('Scratch the Originals. The expanded lore is more ideal.' in statements['KIRA-U06']['text']
            and policy['setting_canon_initializes_live_state'] is False
            and policy['story_possibilities_are_completed_events'] is False
            and policy['beliefs_are_proven_cosmology'] is False,
            'Creator adoption changes setting authority while preserving open outcomes and live state')
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
    expansion = json.loads((root / 'larius/setting.json').read_text(encoding='utf-8'))
    require(world['version'] == expansion['version'] == '0.5'
            and expansion['status'] == 'world_canon'
            and expansion['region_id'] == 'larius'
            and expansion['authorization_refs'] == ['KIRA-U02', 'KIRA-U03', 'KIRA-U04', 'KIRA-U05', 'KIRA-U06']
            and {'KIRA-U02', 'KIRA-U03', 'KIRA-U04', 'KIRA-U05', 'KIRA-U06'} <= set(statements),
            'The adopted setting must retain its scope and creator provenance')
    require(set(expansion['historical_source_ids']) <= set(source_ids), 'Unknown historical source')
    for document in expansion['documents']:
        relative = PurePosixPath(document['path'])
        require(not relative.is_absolute() and '..' not in relative.parts
                and relative.parts[0] == 'larius', 'Invalid manuscript path')
        manuscript = root.joinpath(*relative.parts).resolve()
        require(manuscript.is_relative_to(root)
                and hashlib.sha256(manuscript.read_bytes()).hexdigest() == document['sha256'],
                'Authored manuscript differs from its reference projection')
    projected = [s for s in world['guide']['sections'] if s.get('authored_expansion_id') == expansion['id']]
    require(len(projected) == len(expansion['sections']) + 1
            and projected[1:] == expansion['sections']
            and all(s['canon_status'] == 'world_canon' for s in projected),
            'Displayed canon must match the adopted setting projection')
    central = expansion['central_character']
    require(central == by_id['kieran']['narrative_role']
            and central['role'] == 'continental_main_character' and central['status'] == 'user_confirmed'
            and all(central[k] is False for k in ('player_selected', 'guaranteed_survival',
                                                'predetermined_outcomes', 'automatic_authority')),
            'Narrative centrality does not select player control or guaranteed outcomes')
    require(expansion['engine_rules_adopted'] is False and expansion['campaign_state_initialized'] is False,
            'Worldbuilding cannot silently initialize playthrough effects')
    require(all(r['status'] == 'world_canon' and r['beliefs_prove_cosmology'] is False
                and r['mandatory_by_species'] is False for r in expansion['religions']),
            'Adopted faith traditions remain attributed, noncompulsory beliefs')
    require(expansion['established_explanations'][0]['id'] == 'long-renewal'
            and expansion['established_explanations'][0]['status'] == 'world_canon'
            and expansion['established_explanations'][0]['resolves_source_issue'] is True,
            'The adopted Long Renewal resolves Kieran’s longevity in current canon')
    foundations = json.loads((root / 'larius/national_inspirations.json').read_text(encoding='utf-8'))
    require(expansion['real_world_inspirations']['status'] == 'creator_confirmed'
            and expansion['real_world_inspirations']['creator_confirmed_national_analogues'] == foundations['nations']
            and {p['polity_id'] for p in foundations['nations']} == {'sadion', 'estru', 'akaria', 'evalia', 'kyrinus'},
            'The five creator-confirmed national foundations must be preserved')
    for profile in foundations['nations']:
        expected_refs = ['KIRA-U03', 'KIRA-U05'] if profile['polity_id'] == 'estru' else ['KIRA-U03']
        require(profile['status'] == 'user_confirmed' and profile['source_refs'] == expected_refs
                and by_id[profile['polity_id']]['creator_confirmed_profile'] == profile,
                'A national design profile must retain its creator provenance')
    caste = foundations['everwood_caste']
    require(caste == expansion['everwood_caste'] == by_id['evalia']['creator_confirmed_caste']
            and caste['sea_elves']['position'] == 'highest_caste'
            and caste['plains_and_tree_elves']['recognized_as_equals_by_sea_elves'] is True
            and caste['plains_and_tree_elves']['not_an_automatically_subordinate_tier'] is True
            and caste['mountain_elves']['people_id'] == 'mountain-elves'
            and all(caste[k] is None for k in ('ice_elves_position', 'desert_elves_position',
                                             'mixed_sub_race_classification')),
            'The nuanced caste relationship must not become an invented linear hierarchy')
    require(statements['KIRA-U05']['source_kind'] == 'user_chat_statement'
            and 'The Desert Elves were a component of how Estru formed culturally' in statements['KIRA-U05']['text']
            and 'The Ice Elves have superior magic to even the Sea Elves' in statements['KIRA-U05']['text'],
            'The latest creator clarification must retain its own source statement')
    communities = foundations['elven_communities']
    require(communities == expansion['elven_communities']
            == by_id['larius']['creator_confirmed_elven_communities']
            and {c['people_id'] for c in communities} == {'desert-elves', 'ice-elves'},
            'Both elven communities must reach the world and expansion references')
    for community in communities:
        require(community['status'] == 'user_confirmed' and community['source_refs'] == ['KIRA-U05']
                and community == by_id[community['people_id']]['creator_confirmed_community'],
                'Community records must preserve creator provenance beside the legacy source')
    desert = next(c for c in communities if c['people_id'] == 'desert-elves')
    estru = next(p for p in foundations['nations'] if p['polity_id'] == 'estru')
    require(desert['resident_polity_ids'] == ['estru', 'kyrinus', 'evalia']
            and desert['estru']['long_resident'] is True
            and desert['estru']['initial_participation'] == 'unwilling'
            and desert['estru']['formative_cultural_contribution'] is True
            and desert['estru']['exact_arrangement_and_dates'] is None
            and desert['estru']['present_legal_status'] is None
            and desert['ancestry_determines_nationality'] is False
            and estru['cultural_formation_people_ids'] == ['estrusians', 'desert-elves'],
            'Desert Elves must remain formative residents without invented dates or legal status')
    ice = next(c for c in communities if c['people_id'] == 'ice-elves')
    require(ice['magic']['comparison_people_id'] == 'sea-elves'
            and ice['magic']['relative_capability'] == 'superior'
            and ice['life_history']['maturation'] == 'faster'
            and ice['life_history']['lifespan'] == 'slightly shorter'
            and ice['life_history']['numeric_maturity_age'] is None
            and ice['life_history']['new_numeric_lifespan'] is None
            and ice['isolation']['primarily_isolationist'] is True
            and ice['isolation']['most_of_larius_suitable'] is False
            and ice['isolation']['suitable_region_under_dwarven_dominion'] is True
            and ice['isolation']['exact_boundaries'] is None
            and ice['isolation']['cause_or_date_of_dwarven_dominion'] is None
            and ice['independent_nation_established'] is False,
            'Ice Elven capability and habitat limits must not invent ages, boundaries or a sixth nation')
    require(caste['magic_and_status']['source_refs'] == ['KIRA-U04', 'KIRA-U05']
            and caste['magic_and_status']['sea_elves_highest_caste'] is True
            and caste['magic_and_status']['ice_elves_magically_superior_to_sea_elves'] is True
            and caste['magic_and_status']['ice_elves_caste_position_established'] is False,
            'Greater Ice Elven magic must remain distinct from Evalian caste precedence')
    population = foundations['population_scope']
    require(expansion['population_scope'] == by_id['larius']['population_scope']
            and all(expansion['population_scope'][key] == value for key, value in population.items())
            and population['dominant_peoples_are_nonexhaustive'] is True
            and population['other_minor_peoples_exist'] is True
            and population['intelligence_and_sentience_vary'] is True
            and population['named_minor_peoples_confirmed_by_creator'] == []
            and expansion['population_scope']['adopted_minor_peoples'] == ['Sivren', 'Keld', 'Vesh']
            and all(p['status'] == 'world_canon' and p['adoption_source_refs'] == ['KIRA-U06']
                    for p in expansion['minor_peoples']),
            'Expanded minor peoples are adopted canon within a nonexhaustive population')
    require({'sivren', 'keld', 'vesh', 'lethra-senn', 'dorrun-valehammer', 'rovan-kest',
             'neris-tal', 'vessa-morn', 'sera-vael', 'taren-ash'} <= set(by_id)
            and all(r['id'] in by_id for r in expansion['religions']),
            'Adopted minor peoples, religions and supporting cast need current canon records')
    return {'archived_original_documents_verified': 9, 'canonical_records': len(records),
            'archival_source_records': len(archive['records']),
            'exact_quotations_verified': quote_count, 'map_references': len(maps),
            'transcribed_map_entries': sum(len(m['entries']) for m in maps),
            'resolved_canon_decisions': len(decisions),
            'further_development_topics': sum(i['status'] == 'further_development' for i in issues),
            'guide_sections': len(world['guide']['sections']),
            'authored_manuscripts': len(expansion['documents']),
            'authored_words': sum(d['word_count'] for d in expansion['documents']),
            'religious_traditions': len(expansion['religions']),
            'creator_confirmed_national_profiles': len(foundations['nations']),
            'creator_confirmed_elven_communities': len(communities),
            'map_pixels_verified': False, 'campaign_state_created': False}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
