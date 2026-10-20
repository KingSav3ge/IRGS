"""Single navigation/feature registry and player-facing Content Library (directive v1.0 s.4.2, 4.2a).

The registry is the only navigation authority. Lifecycle values are honest: only entries whose
backend actually exists are 'functional'. Hiding for release is a flag, never a route removal.
Genre engines and technical content libraries are never campaign records here.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'IRGS_3_3' / 'runtime'))
from historical_campaigns import historical_catalogue

LIFECYCLES = ('planned', 'scaffold', 'in_development', 'functional', 'deferred')


def _f(id, label, order, area, lifecycle, desc, parent=None, backend=None, roles=('player',),
       release=False, deps=()):
    return {'id': id, 'label': label, 'parentId': parent, 'route': '#/' + id, 'order': order, 'area': area,
            'lifecycle': lifecycle, 'availableTo': list(roles), 'showInDevelopment': True,
            'showInPreview': lifecycle == 'functional', 'showInRelease': release,
            'requiredBackendCapability': backend, 'description': desc, 'dependencyIds': list(deps)}


FEATURES = [
    _f('content-library', 'Content Library', 10, 'player', 'functional',
       'Player-facing campaign directory. Lists only The Hundred Years’ War in this version.',
       backend='api/content-library', release=True),
    _f('my-campaigns', 'My Campaigns', 20, 'player', 'functional',
       'Saved playthroughs, resume and branches (existing campaign selector).', backend='api/campaigns',
       release=True),
    _f('workshop', 'Campaign Workshop', 30, 'creator', 'planned',
       'Reusable authoring tools. Stage Two; follows the Content Library.', roles=('creator',),
       deps=('content-library',)),
    _f('marketplace', 'Marketplace & Publishing', 40, 'creator', 'planned',
       'Publication, packaging and creator royalties. Stage Three; no listings or balances exist.',
       roles=('creator',), deps=('workshop',)),
    _f('ai-network', 'AI Network', 50, 'developer', 'planned',
       'Six-Director orchestration registry and traces. No Directors are registered yet.',
       roles=('developer',)),
    _f('account', 'Account', 60, 'player', 'planned',
       'Entitlements and solo progression. No account system exists in the local edition.'),
    _f('solo-exchange', 'Solo Cross-Campaign Exchange', 61, 'player', 'deferred',
       'Deferred. No wallet, conversion, rates or rewards are active.', parent='account'),
    _f('licences', 'Licences & Distribution', 62, 'player', 'planned',
       'Planned licence information. Never shows paid status and has no destructive behaviour.',
       parent='account'),
    _f('developer', 'Developer / Administration', 70, 'developer', 'planned',
       'Operations and diagnostics for authorized roles.', roles=('developer',)),
    _f('opening-diagnostics', 'Opening / First-Turn Diagnostics', 71, 'developer', 'planned',
       'Initialization and first-turn IDs. Not available until the opening scene exists.',
       parent='developer', roles=('developer',), backend='opening_scene'),
    _f('build-provenance', 'Build Provenance / Licence Verification', 72, 'developer', 'planned',
       'Planned, non-operational. Build integrity and licence checks need a trusted server policy.',
       parent='developer', roles=('developer',)),
]


def feature_registry(stage='development'):
    key = {'development': 'showInDevelopment', 'preview': 'showInPreview', 'release': 'showInRelease'}[stage]
    items = sorted((f for f in FEATURES if f[key]), key=lambda f: f['order'])
    return {'stage': stage, 'features': items, 'lifecycles': list(LIFECYCLES)}


def content_library():
    """Exactly one playable campaign record; periods and entries nested; engines excluded."""
    hyw = historical_catalogue()
    entries = hyw['entries']
    periods = [{**p, 'entries': [
        {'id': e['id'], 'year': e['year'], 'title': e['title'], 'description': e.get('description', ''),
         'playable': e['status'] == 'developed_historical_setup',
         'readiness': 'Developed sourced opening' if e['status'] == 'developed_historical_setup'
                      else 'Proposed reference only; cannot start a playthrough'}
        for e in entries if e['period_id'] == p['id']]} for p in hyw['periods']]
    playable = sum(e['playable'] for p in periods for e in p['entries'])
    return {'schema_version': 1, 'campaigns': [{
        'id': hyw['id'], 'title': hyw['title'], 'period': hyw['period'], 'status': hyw['status'],
        'summary': hyw['implementation_rule'], 'periods': periods,
        'entry_count': len(entries), 'playable_entry_count': playable,
        'starts_via': 'new-campaign'}],
        'note': 'Genre engines and technical content libraries are internal infrastructure and are not listed.'}
