"""Project adopted setting records while keeping superseded claims in the archive."""
import copy


def build_records(archive, foundations, policy):
    records = copy.deepcopy(archive['records'])
    for record in records:
        record.pop('source_refs', None)
        record['status'] = 'world_canon'
        record['canon_source_refs'] = ['KIRA-U06']
        record['archive_record_id'] = record['id']
        if 'recorded_lifespan_years' in record:
            record['reference_lifespan_years'] = record.pop('recorded_lifespan_years')
        if record['category'] == 'people' and record['summary'].startswith('A people entry'):
            record['summary'] = 'A people of the setting; its identity and cultural relationships follow the adopted worldbook.'
    by_id = {r['id']: r for r in records}
    by_id['kieran'].update({
        'people_id': 'flatland-elves', 'people_description': 'Plains Elf / Flatland Elf',
        'summary': 'Larius’s central character: a Plains Elf born in Forlathis in 1000 B.A., aged 2342 in the reference present, leader of the Rangers and a practitioner of the Long Renewal.',
        'longevity_status': 'The Long Renewal extends his life beyond the ordinary Plains Elven reference span; it confers no immunity or guaranteed resurrection.',
        'wartime_service_years': 228,
        'relationships': 'Friend of Cathius Akarian and Lord Eric Vornwolf; connected to the Evalian republic and Karthinian Council. These relationships confer no automatic mandate.'})
    by_id['flatland-elves'].update({
        'name': 'Plains / Flatland Elves', 'aliases': ['Plains Elves', 'Flatland Elves'],
        'alias_status': 'Canonical names for the same elven group',
        'summary': 'One of the most numerous elven groups in Evalia, alongside Tree Elves; recognized as equals by the highest-caste Sea Elves despite the latter’s sense of superiority.'})
    by_id['forest-elves']['aliases'] = ['Forest Elves', 'Tree Elves']
    by_id['desert-elves'].update({
        'name': 'Desert Elves',
        'summary': 'Long-resident contributors to Estru’s cultural formation, with initially unwilling involvement in the history of Sadire settlement; communities also live in Kyrinus and Evalia.'})
    by_id['ice-elves'].update({
        'name': 'Ice Elves',
        'summary': 'Elves whose magic exceeds that of Sea Elves, with faster maturation and slightly shorter lives. Scarce suitable habitat and dwarven dominion over the suitable region shape their isolation.'})
    by_id['estru']['people_ids'] = list(dict.fromkeys(by_id['estru']['people_ids'] + ['desert-elves']))
    by_id['estru']['summary'] = 'A pressured, politically divided society shaped by Sadire-descended humans and long-resident Desert Elves. Independent since 500 A.A., it lost its later war against Sadion in 600 A.A.; Southern Estru trades with Akaria.'
    by_id['estrusians'].update({
        'name': 'Human Estrusians',
        'summary': 'Estru’s Sadire-descended human population, part of a civic culture also formed by long-resident Desert Elves.',
        'classification_note': 'This record describes human ancestry; Estrusian civic identity includes Desert Elves and supplies no separate species classification.'})
    by_id['calendar']['arithmetic_policy'] = 'Ascension is the calendar turning; 1342 A.A. is the reference present. Exact civil months and time conversions remain undeveloped.'
    by_id['rangers']['strength']['precision'] = 'approximate_setting_reference'
    by_id['daniel']['name'] = 'Daniel Convor'
    by_id['daniel']['aliases'] = ['Dan', 'Fox']
    by_id['larius']['population_scope'] = {
        **foundations['population_scope'],
        'adopted_minor_peoples': ['Sivren', 'Keld', 'Vesh'], 'adoption_source_refs': ['KIRA-U06']}
    for record in records:
        if record['name'] == 'Karkaria':
            record['superseded_map_labels'] = ['Karwathis']
        for field in ('summary', 'note', 'notes'):
            if isinstance(record.get(field), str):
                record[field] = record[field].replace('His biography records', 'His history includes')
    additions = [
        ('first-hearth', 'religion', 'The First Hearth', 'Akarian faith of sound work, inherited obligation and shelter, with both imperial establishments and reforming traditions.'),
        ('turning-bough', 'religion', 'The Turning Bough', 'An elven tradition of memory and living responsibility, contested by defenders and critics of inherited caste.'),
        ('lantern-covenant', 'religion', 'The Lantern Covenant', 'A Sadire religious tradition of household, road, public service and contested national memory.'),
        ('open-horizon', 'religion', 'The Open Horizon', 'A maritime tradition of freely undertaken obligations, hospitality and responsibility beyond one’s own shore.'),
        ('concord-of-the-veil', 'religion', 'The Concord of the Veil', 'Estru’s civic and ancestral cults, shaped by both human and Desert Elven participation.'),
        ('shared-table', 'religion', 'The Shared Table', 'A popular Estrusian movement whose hospitality challenges the political price of charity.'),
        ('last-door', 'religion', 'The Keepers of the Last Door', 'A transnational fellowship concerned with death, identity and consent in restoration.'),
        ('continuance', 'religion', 'The Doctrine of Continuance', 'Varied movements of healing, restoration and resistance to death, with competing ethical commitments.'),
        ('sivren', 'people', 'Sivren', 'River and wetland communities with complex oral records of navigation, seasonal use and intercommunity agreements.'),
        ('keld', 'people', 'Keld', 'Small-bodied inhabitants of fissures and narrow stone country, distinct from Akarian clans and the historical Karthi.'),
        ('vesh', 'people', 'Vesh', 'A social people communicating through collective sound, movement and repeated patterns; precise individual capacities remain undeveloped.'),
        ('lethra-senn', 'character', 'Lethra Senn', 'An Evalian archivist committed to making important agreements publicly intelligible.'),
        ('dorrun-valehammer', 'character', 'Dorrun Valehammer', 'An Akarian works inspector concerned with standards that survive a change of patron.'),
        ('rovan-kest', 'character', 'Rovan Kest', 'A Sadire former quartermaster carrying petitions from soldiers’ households.'),
        ('neris-tal', 'character', 'Neris Tal', 'A Kyrinian navigator and negotiator associated with an Open Horizon house.'),
        ('vessa-morn', 'character', 'Vessa Morn', 'A Southern Estrusian Shared Table organizer and keeper of household accounts.'),
        ('sera-vael', 'character', 'Sera Vael', 'An elven Ranger responsible for practical company affairs and committed to accountability.'),
        ('taren-ash', 'character', 'Taren Ash', 'A Last Door healer concerned with consent and justified methods in restoration research.'),
    ]
    for identity, category, name, summary in additions:
        record = {'id': identity, 'category': category, 'name': name, 'summary': summary,
                  'status': 'world_canon', 'canon_source_refs': ['KIRA-U06'],
                  'canon_document': 'larius/LARIUS_LOREBOOK.md', 'region_id': 'larius'}
        if category == 'character':
            record['player_controlled'] = False
        if category == 'religion':
            record.update(beliefs_prove_cosmology=False, mandatory_by_species=False)
        records.append(record)
    return records


def continuity_decisions(archive, policy):
    resolved = {item['id']: item['resolution'] for item in policy['editorial_decisions']}
    issues = []
    for old in archive['continuity_issues']:
        item = {'id': old['id'], 'title': old['title'], 'canon_source_refs': ['KIRA-U06']}
        if old['id'] in resolved:
            item.update(status='resolved_in_current_canon', resolution=resolved[old['id']])
        else:
            item.update(status='further_development', resolution=None,
                        question=old['question'], archival_conflict_blocks_authoring=False)
        issues.append(item)
    return issues
