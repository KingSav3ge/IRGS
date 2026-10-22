"""Build authored lore projections from the two editable Markdown manuscripts.

This updates reference JSON only. It never opens saves or selects engine rules.
Run the package verifier and refresh intended release pins after authoring.
"""
import hashlib
import json
from pathlib import Path
import re
from canon_records import build_records, continuity_decisions

ROOT = Path(__file__).resolve().parent.parent
EXPANSION_ID = 'larius-canon-v0.5'
DOCUMENTS = ('larius/LARIUS_LOREBOOK.md', 'larius/KIERAN_PELLEAS.md')


def sections_from_markdown(path, relative):
    sections, current, paragraph = [], None, []
    parent = ''

    def flush():
        if paragraph and current is not None:
            text = ' '.join(paragraph)
            current['paragraphs'].append(re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text))
        paragraph.clear()

    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('## ') or line.startswith('### '):
            flush()
            if line.startswith('## '):
                parent = re.sub(r'^\d+\.\s*', '', line[3:])
                title = parent
            else:
                title = parent + ' — ' + line[4:]
            if relative.endswith('KIERAN_PELLEAS.md'):
                title = 'Kieran Pelleas — ' + title
            current = {'title': title, 'paragraphs': [], 'record_ids': [],
                       'authored_expansion_id': EXPANSION_ID,
                       'source_document': relative, 'canon_status': 'world_canon'}
            sections.append(current)
        elif not line.strip():
            flush()
        elif not line.startswith('# '):
            paragraph.append(line.strip())
    flush()
    return [s for s in sections if s['paragraphs']]


def build(root=ROOT):
    root = Path(root)
    world = json.loads((root / 'world.json').read_text(encoding='utf-8'))
    manifest = json.loads((root / 'source_manifest.json').read_text(encoding='utf-8'))
    foundations = json.loads((root / 'larius/national_inspirations.json').read_text(encoding='utf-8'))
    policy = json.loads((root / 'canon.json').read_text(encoding='utf-8'))
    archive = json.loads((root / 'archive/legacy_reference.json').read_text(encoding='utf-8'))
    world['records'] = build_records(archive, foundations, policy)
    world['continuity_issues'] = continuity_decisions(archive, policy)
    statement = {'id': 'KIRA-U02', 'source_kind': 'user_chat_statement',
        'text': 'Starting with Larius, flesh out Lore, history, culture, religions, etc, etc. Kieran Pelleas is the continent\'s "Main Character"',
        'interpretation': 'Authorize new Larius worldbuilding and establish Kieran as the central narrative character, without assigning a player avatar.'}
    statements = manifest.setdefault('user_statements', [])
    statements[:] = [s for s in statements if s['id'] != statement['id']] + [statement]
    documents, chapters = [], []
    for relative in DOCUMENTS:
        path = root / relative
        documents.append({'path': relative, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                          'word_count': len(path.read_text(encoding='utf-8').split())})
        chapters.extend(sections_from_markdown(path, relative))
    religions = [('first-hearth', 'The First Hearth'), ('turning-bough', 'The Turning Bough'),
        ('lantern-covenant', 'The Lantern Covenant'), ('open-horizon', 'The Open Horizon'),
        ('concord-of-the-veil', 'The Concord of the Veil'),
        ('shared-table', 'The Shared Table'), ('last-door', 'The Keepers of the Last Door'),
        ('continuance', 'The Doctrine of Continuance')]
    expansion = {'schema_version': 1, 'id': EXPANSION_ID, 'version': '0.5',
        'region_id': 'larius', 'reference_year': 1342, 'status': 'world_canon',
        'authorization_refs': ['KIRA-U02', 'KIRA-U03', 'KIRA-U04', 'KIRA-U05', 'KIRA-U06'],
        'adoption_source_refs': ['KIRA-U06'],
        'real_world_inspirations': {'status': 'creator_confirmed',
            'source_refs': ['KIRA-U03', 'KIRA-U05'], 'source_file': 'larius/national_inspirations.json',
            'creator_confirmed_national_analogues': foundations['nations']},
        'everwood_caste': foundations['everwood_caste'],
        'elven_communities': foundations['elven_communities'],
        'population_scope': next(r for r in world['records'] if r['id'] == 'larius')['population_scope'],
        'minor_peoples': [{'name': name, 'status': 'world_canon',
                          'origin': 'expanded_lore', 'adoption_source_refs': ['KIRA-U06']}
                                   for name in ('Sivren', 'Keld', 'Vesh')],
        'historical_source_ids': ['KIRA-S01','KIRA-S02','KIRA-S03','KIRA-S04',
                                 'KIRA-S06','KIRA-S07','KIRA-S08','KIRA-S09'],
        'documents': documents, 'sections': chapters,
        'central_character': {'record_id': 'kieran', 'role': 'continental_main_character',
            'status': 'user_confirmed', 'source_refs': ['KIRA-U02'],
            'player_selected': False, 'guaranteed_survival': False,
            'predetermined_outcomes': False, 'automatic_authority': False},
        'religions': [{'id': identity, 'name': name, 'status': 'world_canon',
            'adoption_source_refs': ['KIRA-U06'],
            'beliefs_prove_cosmology': False, 'mandatory_by_species': False} for identity,name in religions],
        'established_explanations': [{'id': 'long-renewal', 'status': 'world_canon',
            'resolves_source_issue': True, 'source_issue_id': 'longevity',
            'adoption_source_refs': ['KIRA-U06'],
            'summary': 'The Long Renewal extends Kieran’s life beyond an ordinary Plains Elven lifespan through sustained healing.'}],
        'engine_rules_adopted': False, 'campaign_state_initialized': False}
    intro = {'title': 'Larius: expanded lore and its central character',
        'paragraphs': ['The expanded Larius lorebook and Kieran Pelleas dossier are the adopted setting canon. Sadion combines Roman and Holy Roman design; Estru combines fragmented medieval German politics with Etruscan and Carthaginian culture; Akaria draws on Sasanian and Byzantine heavy cavalry and insular post-William England; Everwood combines French-influenced prestige, elven supremacy and a sub-race caste system; Kyrinus is a more accepting mercantile elven society influenced by medieval Italians. The expanded religions, supporting cast, minor peoples and Kieran’s Long Renewal belong to this canon. Earlier documents are a superseded archive.',
            'Sea elves hold the highest recognized caste but recognize the numerous Plains and Tree elves as equals despite their own sense of superiority. Mountain elves are few and valued militarily, yet looked down on for their weaker magic. Desert Elves are long-resident contributors to Estru’s cultural formation, following initially unwilling involvement in the history of Sadire settlement; communities also live in Kyrinus and Evalia. Ice Elves exceed Sea Elves in magic, mature faster and live slightly less long. Their isolation is shaped by unsuitable habitat across most of Larius and dwarven dominion over the suitable region. Exact Ice and Desert caste ranks remain open. These dominant peoples do not exhaust Larius: other minor races with varying intelligence and sentience also exist.'],
        'record_ids': ['larius','kieran'], 'authored_expansion_id': EXPANSION_ID,
        'source_document': DOCUMENTS[0], 'canon_status': 'world_canon'}
    base_sections = sections_from_markdown(root / 'WORLD_GUIDE.md', 'WORLD_GUIDE.md')
    for section in base_sections:
        section.pop('authored_expansion_id')
    world['guide']['sections'] = base_sections + [intro] + chapters
    world['guide']['subtitle'] = 'Larius and the lands beyond · adopted setting canon v0.5'
    world['guide']['scope_note'] = 'The expanded setting is the working canon. Older documents are a superseded creative archive. Browsing remains an out-of-character reference and creates no playthrough or character knowledge.'
    for catalogue in world['guide']['map_catalogues']:
        catalogue['notes'] = [
            'Current canon uses Karkaria for the map’s Karwathis, Evalia for its Evalian label, and Ikarion for the older Ikrarion spelling. Transcribed map labels remain unchanged.'
            if 'these have not been silently merged' in note else note
            for note in catalogue['notes']]
    world['version'] = '0.5'
    world['content_status'] = 'expanded_setting_canon'
    world['summary'] = 'A homebrew fantasy world spanning Larius, TalmahKah, Aldain, Azaloth, Falkion and Bendara. The expanded Larius setting is its working canon: dwarven industry, elven republics and human kingdoms share a continent whose living history centres on Kieran Pelleas in 1342 A.A.'
    world['canon_policy'] = policy
    world['archival_sources'] = {'path': 'archive/legacy_reference.json', 'canon_authority': False}
    world['unprovided'] = [s for s in world['unprovided'] if s != 'Creation history, gods, religions and cosmology']
    if 'A complete creation history and proven cosmology' not in world['unprovided']:
        world['unprovided'].append('A complete creation history and proven cosmology')
    world['authored_expansions'] = [{'id': EXPANSION_ID, 'path': 'larius/setting.json',
                                    'status': 'world_canon', 'region_id': 'larius'}]
    kieran = next(r for r in world['records'] if r['id'] == 'kieran')
    kieran['narrative_role'] = expansion['central_character']
    kieran['authored_dossier'] = DOCUMENTS[1]
    by_id = {r['id']: r for r in world['records']}
    for profile in foundations['nations']:
        by_id[profile['polity_id']]['creator_confirmed_profile'] = profile
    by_id['evalia']['creator_confirmed_caste'] = foundations['everwood_caste']
    for community in foundations['elven_communities']:
        by_id[community['people_id']]['creator_confirmed_community'] = community
    by_id['larius']['creator_confirmed_elven_communities'] = foundations['elven_communities']
    by_id['forest-elves']['aliases'] = list(dict.fromkeys(
        by_id['forest-elves'].get('aliases', []) + ['Tree Elves']))
    by_id['forest-elves']['creator_terminology_source_refs'] = ['KIRA-U04']
    for path, value in [(root/'world.json',world), (root/'source_manifest.json',manifest),
                        (root/'larius/setting.json',expansion)]:
        path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'documents': len(documents), 'words': sum(d['word_count'] for d in documents),
            'authored_sections': len(chapters), 'religious_traditions': len(religions)}


if __name__ == '__main__':
    print(json.dumps(build(), indent=2))
