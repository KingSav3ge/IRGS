"""Independent Alpha context assessment; no runtime authorization or rules."""
import copy
import hashlib
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = 'evaluation/alpha_contexts_v1'
CASES = ('historical-quay', 'rise-r00')
AREAS = ('actor_control', 'location', 'received_information', 'participants', 'resources_capacity',
         'movement_perception', 'dialogue_obligations', 'work', 'needs_recovery', 'npc_decisions',
         'local_institution', 'risk_conflict')
STATES = ('adopted_bounded', 'missing', 'uncertain', 'proposed')
_path = ROOT / 'response_depot_compatibility.py'
if any(p.is_symlink() for p in (_path, *_path.parents)):
    raise ValueError('Linked evaluation code')
_spec = importlib.util.spec_from_file_location('catalog_alpha_owned_json', _path)
source = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(source)


def load_fixture(root=ROOT):
    directory = Path(root) / FIXTURE
    doc = source.read_json(directory / 'manifest.json')
    source.keys(doc, 'schema_version fixture_id classification rights consumers contexts evaluator_only files_sha256')
    source.require(type(doc['schema_version']) is int and doc['schema_version'] == 1
        and doc['fixture_id'] == 'irgs-alpha-contexts-v1'
        and doc['classification'] == 'offline-synthetic-assessment', 'Invalid Alpha fixture identity')
    source.require(doc['rights'] == {'authorship': 'original-synthetic-instructions-and-assessment',
        'imported_prose': 'none', 'permitted_processing': ['local-validation', 'offline-synthetic-consumer-tests'],
        'external_processing': 'not-authorized-by-fixture'}, 'Offline-only rights required')
    source.require(doc['consumers'] == {'engine_commit': 'efc84364b86e640f5028bfac2dfd5ae3021695a9',
        'app_commit': 'de4e6926f6236f720365d552c69e02756ce18605',
        'app_catalog_pin': '6f927b00e12a3339861ac353bc38d03c68279662'}, 'Exact published 3.4.3 consumers required')
    expected = {'actor_inputs/' + name + '.json' for name in CASES} | {'evaluator_only/matrix.json'}
    source.require(doc['contexts'] == {name: 'actor_inputs/' + name + '.json' for name in CASES}
        and doc['evaluator_only'] == 'evaluator_only/matrix.json' and set(doc['files_sha256']) == expected,
        'Separate context instructions and evaluator matrix required')
    actual = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()
              and p.name not in ('manifest.json', 'README.md')}
    source.require(actual == expected, 'Unexpected Alpha assessment payload')
    values = {}
    for name in expected:
        path = directory / name; values[name] = source.read_json(path)
        source.require(hashlib.sha256(path.read_bytes()).hexdigest() == doc['files_sha256'][name],
            'Alpha payload hash mismatch')
    for case in CASES:
        actor = values[doc['contexts'][case]]
        source.keys(actor, 'case_id source_ref selection intentions')
        source.require(actor['case_id'] == case and actor['source_ref'] == 'authored-synthetic:irgs-catalog:alpha-contexts:v1'
            and isinstance(actor['selection'], dict) and isinstance(actor['intentions'], list)
            and all(isinstance(t, str) and 0 < len(t) <= 1000 for t in actor['intentions']), 'Invalid actor instructions')
        expected_selection = ({'profile_id': 'military', 'scenario_id': 'hundred-years-war',
            'entry_id': 'hyw-1415', 'character': 'new-human', 'opening_id': 'quay-delivery-v1'}
            if case == 'historical-quay' else {'template_id': 'R00', 'fixture_id': 'irgs-solo-r00-eval-v1'})
        source.require(actor['selection'] == expected_selection
            and all('PRIVATE_' not in text for text in actor['intentions']),
            'Actor selection must not inject privileged setup or evaluator truth')
    matrix = values[doc['evaluator_only']]
    source.keys(matrix, 'classification marker qualification contexts')
    source.require(matrix['classification'] == 'evaluator-only' and matrix['marker'] == 'PRIVATE_ALPHA_ORACLE'
        and matrix['qualification'] == 'candidates_not_alpha_qualified' and set(matrix['contexts']) == set(CASES),
        'Alpha claims must remain unqualified')
    for case, context in matrix['contexts'].items():
        source.keys(context, 'family source_scope ordinary_creation areas')
        source.require(context['ordinary_creation'] is True and set(context['areas']) == set(AREAS),
            'Each ordinary candidate requires a complete gameplay matrix')
        for area in context['areas'].values():
            source.keys(area, 'state owner evidence gap')
            source.require(area['state'] in STATES and area['owner'] in ('Engine', 'App', 'Catalog', 'Coordinator')
                and all(isinstance(area[k], str) and area[k] for k in ('evidence', 'gap')), 'Invalid scope or owner')
    source.require(matrix['contexts'][CASES[0]]['family'] != matrix['contexts'][CASES[1]]['family'],
        'Independent campaign families required')
    return doc


def export_actor_input(case, root=ROOT):
    doc = load_fixture(root); source.require(case in CASES, 'Unknown Alpha case')
    return copy.deepcopy(source.read_json(Path(root) / FIXTURE / doc['contexts'][case]))


def load_evaluator_data(root=ROOT):
    doc = load_fixture(root)
    return source.read_json(Path(root) / FIXTURE / doc['evaluator_only'])


def validate_fixture(root=ROOT):
    doc = load_fixture(root)
    return {'status': 'verified', 'fixture_id': doc['fixture_id'], 'contexts': 2,
        'alpha_qualified': False, 'runtime_execution_verified_by_schema': False}
