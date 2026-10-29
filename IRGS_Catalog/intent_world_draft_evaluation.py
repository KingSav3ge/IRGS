"""Versioned independent candidate selection; not Engine validation."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = 'evaluation/intent_world_draft_v1'
ORIGINAL = 'evaluation/authoring_examples_v1/actor_inputs/examples.json'
ORIGINAL_SHA = 'bc414257874bc7f811744c2ef98da5baeb28c58d312f8db0d03637faf94d2b37'
SELECTION = {'engine': '44ea8b0f66801c12a039c0046128177d2ea6d7d8',
             'app': '4f7cbd703d1207ae32db2bbc90d429415ae1e13f',
             'app_engine_pin': '296e46a1beed10d0ebf2841f133bb52fade83697',
             'app_catalog_pin': 'e97d87f0d17a16dbe0ce186badafe663188321a1',
             'catalog': 'containing-commit', 'engine_override': True, 'catalog_override': True}
FILES = {'actor_inputs/cases.json', 'evaluator_only/expectations.json'}
PENDING = ['npc_decisions', 'institution_reactions', 'needs_recovery', 'risk_conflict',
           'ordinary_offer_authority', 'live_provider_quality', 'two_context_world_draft',
           'world_pack_import_export', 'creator_editor']


def read(path):
    path = Path(path)
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('Linked fixture path')
    return json.loads(path.read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_fixture(root=ROOT):
    root = Path(root); folder = root / FIXTURE
    manifest = read(folder / 'manifest.json')
    if (set(manifest) != {'schema_version', 'fixture_id', 'classification', 'selection', 'original_example', 'files_sha256'}
        or type(manifest['schema_version']) is not int or manifest['schema_version'] != 1
        or manifest['fixture_id'] != 'irgs-intent-world-draft-v1'
        or manifest['classification'] != 'offline-synthetic-independent-consumer'
        or manifest['selection'] != SELECTION
        or manifest['original_example'] != {'path': ORIGINAL, 'sha256': ORIGINAL_SHA}
        or set(manifest['files_sha256']) != FILES):
        raise ValueError('Invalid candidate selection or fixture identity')
    read(root / ORIGINAL)
    if digest(root / ORIGINAL) != ORIGINAL_SHA:
        raise ValueError('Original authoring example changed')
    for name in FILES:
        read(folder / name)
        if digest(folder / name) != manifest['files_sha256'][name]:
            raise ValueError('Fixture payload changed')
    actor = read(folder / 'actor_inputs/cases.json'); oracle = read(folder / 'evaluator_only/expectations.json')
    if (set(actor) != {'fixture_id', 'classification', 'draft', 'journeys'}
        or actor['fixture_id'] != manifest['fixture_id'] or actor['classification'] != 'original-fictional-offline'
        or set(actor['draft']) != {'schema_version', 'draft_id', 'classification', 'profile_id', 'choices'}
        or actor['draft']['schema_version'] != 'irgs-world-draft-1'
        or actor['draft']['classification'] != 'fictional' or actor['draft']['profile_id'] != 'rise-r00'
        or set(actor['journeys']) != {'quay', 'rise'}
        or set(oracle) != {'classification', 'marker', 'draft', 'journeys', 'pending'}
        or oracle['classification'] != 'evaluator-only' or oracle['marker'] != 'PRIVATE_INTENT_WORLD_EVALUATOR'
        or oracle['marker'] in json.dumps(actor) or oracle['pending'] != PENDING
        or set(oracle['journeys']) != {'quay', 'rise'}):
        raise ValueError('Invalid draft, actor/evaluator separation or pending requirements')
    for context in ('quay', 'rise'):
        actions = actor['journeys'][context]
        if not isinstance(actions, list) or not actions or any(not isinstance(a, dict) or set(a) != {'action', 'intention'}
            or any(not isinstance(a[k], str) or not a[k] or 'PRIVATE_' in a[k] for k in ('action', 'intention')) for a in actions):
            raise ValueError('Invalid actor instructions')
    return deepcopy(manifest)


def validate_fixture(root=ROOT):
    doc = load_fixture(root)
    return {'status': 'verified', 'fixture_id': doc['fixture_id'], 'contexts': 2,
            'engine_validation_performed_by_schema': False, 'runtime_execution_verified_by_schema': False,
            'alpha_qualified': False}
