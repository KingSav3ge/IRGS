"""Catalog-only intake and separation for shared response consumer fixtures."""
import copy
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
FIXTURE = 'evaluation/shared_responses_v1'
LIBRARY = 'responses/depot_v1/library.json'
LIBRARY_SHA256 = '8b397ae8cd72cf5ed59c330c0572e34922579726740edbeed9fca957044a6ae4'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def keys(value, expected):
    require(isinstance(value, dict) and set(value) == set(expected.split()),
            'Unknown or missing shared response fields')


def read_json(path):
    require(not any(p.is_symlink() for p in (path, *path.parents)), 'Linked evaluation source')
    require(path.stat().st_size <= 65536, 'Evaluation document exceeds size limit')

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'Duplicate evaluation JSON field')
            result[key] = value
        return result
    return json.loads(path.read_bytes(), object_pairs_hook=pairs)


def load_fixture(root=ROOT):
    root = Path(root)
    directory = root / FIXTURE
    manifest = read_json(directory / 'manifest.json')
    keys(manifest, 'schema_version fixture_id classification rights library consumers contexts evaluator_only files_sha256')
    require(type(manifest['schema_version']) is int and manifest['schema_version'] == 1
            and manifest['fixture_id'] == 'irgs-shared-responses-v1'
            and manifest['classification'] == 'offline-synthetic-consumer-qualification',
            'Unsupported shared response identity')
    require(manifest['rights'] == {
        'authorship': 'original-authored-evaluation-instructions', 'imported_material': 'none',
        'permitted_processing': ['local-validation', 'offline-synthetic-consumer-tests'],
        'external_processing': 'not-authorized-by-fixture'}, 'Explicit offline synthetic rights required')
    require(manifest['library'] == {'id': 'irgs-response-depot-v1', 'path': LIBRARY,
            'sha256': LIBRARY_SHA256}, 'Depot binding changed')
    library = root / LIBRARY
    require(not any(p.is_symlink() for p in (library, *library.parents)), 'Linked response depot')
    require(hashlib.sha256(library.read_bytes()).hexdigest() == LIBRARY_SHA256, 'Depot source hash mismatch')
    keys(manifest['consumers'], 'engine_commit app_commit app_catalog_pin')
    require(all(isinstance(v, str) and re.fullmatch(r'[0-9a-f]{40}', v)
                for v in manifest['consumers'].values()), 'Exact consumer commits required')
    require(isinstance(manifest['contexts'], dict) and set(manifest['contexts']) == {'rise', 'quay'},
            'Independent Rise and non-Rise contexts required')
    expected = {'actor_inputs/rise.json', 'actor_inputs/quay.json', 'evaluator_only/oracle.json'}
    require(isinstance(manifest['files_sha256'], dict) and set(manifest['files_sha256']) == expected
            and manifest['evaluator_only'] == 'evaluator_only/oracle.json', 'Actor/oracle separation changed')
    actual = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()
              and p.name not in ('manifest.json', 'README.md')}
    require(actual == expected, 'Unexpected evaluation payload')
    for name, sha in manifest['files_sha256'].items():
        path = directory / name
        read_json(path)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == sha, 'Evaluation payload hash mismatch')
    case_ids, request_ids = set(), set()
    for context, spec in manifest['contexts'].items():
        if context == 'rise':
            require(spec == {'operation': 'execute_settlement_action',
                'initializer': 'settlement_setup.initialize via rise_campaigns.create',
                'setup_fixture': 'evaluation/solo_r00_v1', 'actor_input': 'actor_inputs/rise.json'},
                'Rise fixture must use its existing initializer')
        else:
            require(spec == {'operation': 'execute_player_scene_action',
                'initializer': 'Store.create via starting_options and scene_setup.initialize_opening',
                'selection': {'profile_id': 'military', 'scenario_id': 'hundred-years-war',
                    'entry_id': 'hyw-1415', 'opening_id': 'quay-delivery-v1'},
                'actor_input': 'actor_inputs/quay.json'}, 'Non-Rise fixture must use its supported opening')
        doc = read_json(directory / spec['actor_input'])
        keys(doc, 'context_id source_ref cases')
        require(doc['context_id'] == context
                and doc['source_ref'] == 'authored-synthetic:irgs-catalog:shared-responses:v1',
                'Explicit actor-input source required')
        require(isinstance(doc['cases'], list) and doc['cases'], 'Action sequence required')
        for case in doc['cases']:
            keys(case, 'case_id action_id request_id')
            require(all(isinstance(v, str) and re.fullmatch(r'[a-z][a-z0-9_-]{0,127}', v)
                        for v in case.values()), 'Bounded case identities required')
            require(case['case_id'] not in case_ids and case['request_id'] not in request_ids,
                    'Duplicate case or request identity')
            case_ids.add(case['case_id'])
            request_ids.add(case['request_id'])
    oracle = read_json(directory / manifest['evaluator_only'])
    keys(oracle, 'classification hidden_marker cases quay_final rise_final')
    require(oracle['classification'] == 'evaluator-only'
            and isinstance(oracle['hidden_marker'], str) and oracle['hidden_marker'].startswith('PRIVATE_'),
            'Explicit evaluator-only marker required')
    require(isinstance(oracle['cases'], dict) and set(oracle['cases']) == case_ids, 'Oracle case coverage differs')
    for case in oracle['cases'].values():
        keys(case, 'status duration_seconds total_seconds')
        require(case['status'] in ('completed_successfully', 'completed_unsuccessfully')
                and all(type(case[k]) is int and 0 <= case[k] <= 10**12
                        for k in ('duration_seconds', 'total_seconds')), 'Invalid expected outcome')
    for context, fields in [('rise_final', 'elapsed_seconds'),
                            ('quay_final', 'elapsed_seconds dispatch_with_actor dispatch_in_tray')]:
        keys(oracle[context], fields)
        require(all(type(v) is int and 0 <= v <= 10**12 for v in oracle[context].values()),
                'Invalid final expectation')
    require(len(case_ids) == 9, 'Nine reference cases required')
    return manifest


def export_actor_input(context_id, root=ROOT):
    manifest = load_fixture(root)
    require(context_id in manifest['contexts'], 'Unknown response context')
    return copy.deepcopy(read_json(Path(root) / FIXTURE / manifest['contexts'][context_id]['actor_input']))


def load_evaluator_data(root=ROOT):
    manifest = load_fixture(root)
    return read_json(Path(root) / FIXTURE / manifest['evaluator_only'])


def validate_fixture(root=ROOT):
    manifest = load_fixture(root)
    return {'status': 'verified', 'fixture_id': manifest['fixture_id'], 'contexts': 2,
            'non_rise_contexts': 1, 'cases': 9, 'actor_oracle_separation': True,
            'runtime_execution_verified_by_schema': False}


if __name__ == '__main__':
    print(json.dumps(validate_fixture()))
