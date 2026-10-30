"""Separately bound 3.4.6 evaluation inputs; never runtime authority."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = 'evaluation/adopted_consequences_v1'
BASELINE = 'evaluation/intent_world_draft_v1/manifest.json'
BASELINE_SHA = '48c64ac631e5d74007649ac67d70261dfba89c653edcba5365f270ba50834e98'
SELECTION = {'engine': 'fe9c2c10ec3a66f1be590e1b34860119670b22cb',
             'app': '746c9a381e64b7f985d37edd39a91b5b79b2e027',
             'app_engine_pin': 'fe9c2c10ec3a66f1be590e1b34860119670b22cb',
             'app_catalog_pin': 'cf69a6cf628a6d9249124cc6b0700dfc59287677',
             'catalog': 'containing-commit', 'engine_override': False, 'catalog_override': True}
FILES = {'actor_inputs/cases.json', 'evaluator_only/expectations.json'}
PENDING = {'sustained_consequences', 'npc_decisions', 'institution_decisions', 'needs_recovery',
           'risk_conflict', 'general_world_authoring', 'pack_import_export', 'live_provider_quality'}


def read(path):
    path = Path(path)
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('Linked evaluation source')
    return json.loads(path.read_text(encoding='utf-8'))


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_fixture(root=ROOT):
    root = Path(root); folder = root / FIXTURE
    manifest = read(folder / 'manifest.json')
    if (set(manifest) != {'schema_version', 'fixture_id', 'classification', 'selection', 'baseline', 'files_sha256'}
        or type(manifest['schema_version']) is not int or manifest['schema_version'] != 1
        or manifest['fixture_id'] != 'worldward-adopted-consequences-v1'
        or manifest['classification'] != 'offline-independent-consumer' or manifest['selection'] != SELECTION
        or manifest['baseline'] != {'path': BASELINE, 'sha256': BASELINE_SHA}
        or set(manifest['files_sha256']) != FILES):
        raise ValueError('Invalid selection or identity')
    read(root / BASELINE)
    if sha(root / BASELINE) != BASELINE_SHA: raise ValueError('Prior fixture changed')
    for name in FILES:
        read(folder / name)
        if sha(folder / name) != manifest['files_sha256'][name]: raise ValueError('Payload changed')
    actor, truth = read(folder / 'actor_inputs/cases.json'), read(folder / 'evaluator_only/expectations.json')
    if (set(actor) != {'fixture_id', 'classification', 'drafts', 'journeys', 'stock_offer'}
        or actor['fixture_id'] != manifest['fixture_id'] or actor['classification'] != 'original-synthetic-offline'
        or set(actor['drafts']) != {'rise', 'quay'} or set(actor['journeys']) != {'rise', 'quay'}
        or set(truth) != {'classification', 'marker', 'quay', 'rise', 'unmet_requirements'}
        or truth['classification'] != 'evaluator-only' or truth['marker'] != 'PRIVATE_ADOPTED_CONSEQUENCES'
        or truth['marker'] in json.dumps(actor) or set(truth['unmet_requirements']) != PENDING
        or any(not isinstance(v, str) or not v for v in truth['unmet_requirements'].values())):
        raise ValueError('Invalid actor/evaluator scope or missing owners')
    for context, profile, classification in [('rise', 'rise-r00', 'fictional'), ('quay', 'historical-quay', 'mixed')]:
        draft = actor['drafts'][context]
        if (set(draft) != {'schema_version', 'draft_id', 'classification', 'profile_id', 'choices'}
            or draft['schema_version'] != 'irgs-world-draft-1' or draft['profile_id'] != profile
            or draft['classification'] != classification): raise ValueError('Unselected draft')
        actions = actor['journeys'][context]
        if not isinstance(actions, list) or not actions or any(not isinstance(a, dict) or set(a) != {'action', 'intention'}
            or any(not isinstance(a[k], str) or not a[k] or 'PRIVATE_' in a[k] for k in ('action', 'intention')) for a in actions):
            raise ValueError('Invalid actor instructions')
    return deepcopy(manifest)


def validate_fixture(root=ROOT):
    doc = load_fixture(root)
    return {'status': 'verified', 'fixture_id': doc['fixture_id'], 'contexts': 2,
            'runtime_execution_verified_by_schema': False, 'semantic_judgments_verified': False, 'alpha_qualified': False}
