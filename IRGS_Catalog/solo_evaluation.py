"""Versioned synthetic test content. No initialization, execution or provider calls.

Only export_actor_input is an actor/model input boundary. The evaluator loader
deliberately has a different API and reads physically separate files.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

DEFAULT_ROOT = Path(__file__).resolve().parent / 'evaluation/solo_r00_v1'
FIXTURE_ID = 'irgs-solo-r00-eval-v1'
SOURCE_REF = 'authored-synthetic:irgs-catalog:solo-r00:v1'
PROCESSING = 'synthetic-evaluation-actor-input-only'
OPERATION = 'execute_settlement_action'
SUPPORTED_ACTIONS = ('request_grant', 'accept_grant', 'walk_clearing', 'walk_commons',
    'found', 'build', 'delegate', 'pause', 'resume', 'invite', 'arrange_departure',
    'wait_hour', 'inspect')
RIGHTS = {
    'authorship': 'original-synthetic-evaluation-content',
    'permitted_processing': ['local-offline-evaluation', 'external-evaluation-of-actor-exports'],
    'scope': 'fixture-authored-text-only',
    'imported_material': 'none',
    'transfer_authority': 'Engine authorization still required; metadata selects no provider',
}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _keys(value, names):
    _require(isinstance(value, dict) and set(value) == set(names.split()),
             'Unexpected or missing schema fields')


def _number(value):
    _require(type(value) is int and value >= 0, 'Expected a nonnegative integer')


def _text(value):
    _require(isinstance(value, str) and 0 < len(value) <= 1000
             and value == value.strip() and all(ord(c) >= 32 for c in value),
             'Expected bounded printable text')


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        _require(key not in result, 'Duplicate JSON field')
        result[key] = value
    return result


def _read(root, name, prefix=None, sha256=None):
    _require(isinstance(name, str), 'Expected a relative fixture path')
    path = PurePosixPath(name)
    _require(not path.is_absolute() and path.as_posix() == name
             and '..' not in path.parts and '\\' not in name and ':' not in name
             and (prefix is None or path.parts[0] == prefix), 'Invalid fixture path or audience')
    target = Path(root).joinpath(*path.parts)
    _require(not any(p.is_symlink() for p in (target, *target.parents)), 'Linked fixture path')
    _require(target.stat().st_size <= 65536, 'Fixture file exceeds schema limit')
    data = target.read_bytes()
    if sha256 is not None:
        _require(hashlib.sha256(data).hexdigest() == sha256, 'Fixture hash mismatch')
    return json.loads(data, object_pairs_hook=_pairs)


def _binding(value, prefix):
    _keys(value, 'path sha256')
    _require(isinstance(value['path'], str)
             and re.fullmatch(prefix + r'/[a-z0-9_-]+\.json', value['path']),
             'Invalid fixture path or audience')
    _require(isinstance(value['sha256'], str)
             and re.fullmatch(r'[0-9a-f]{64}', value['sha256']), 'Invalid SHA-256')


def load_manifest(root=DEFAULT_ROOT):
    doc = _read(root, 'manifest.json')
    _keys(doc, 'schema_version fixture_id version source_ref provenance rights classification '
          'public_discovery canon playable_start release_approved contracts actor_inputs evaluator_only')
    _require(type(doc['schema_version']) is int and doc['schema_version'] == 1
             and doc['fixture_id'] == FIXTURE_ID and doc['version'] == '1.0.0'
             and doc['source_ref'] == SOURCE_REF, 'Unsupported fixture identity/version')
    _require(doc['rights'] == RIGHTS and doc['classification'] == 'synthetic-evaluation-only',
             'Explicit synthetic rights/processing classification required')
    _require(all(doc[k] is False for k in ('public_discovery', 'canon', 'playable_start',
                                          'release_approved')), 'Evaluation content cannot grant release')
    _keys(doc['provenance'], 'author derived_from historical_calibration')
    _require(doc['provenance'] == {'author': 'IRGS Catalog',
        'derived_from': 'authored-fictional:greywater-reach:v1 / rise-foundation-1 / R00',
        'historical_calibration': False}, 'Unrecognized synthetic provenance')
    _keys(doc['contracts'], 'engine_commit app_commit operation_id supported_action_ids')
    for key in ('engine_commit', 'app_commit'):
        _require(isinstance(doc['contracts'][key], str)
                 and re.fullmatch(r'[0-9a-f]{40}', doc['contracts'][key]), 'Exact dependency SHA required')
    _require(doc['contracts']['operation_id'] == OPERATION
             and doc['contracts']['supported_action_ids'] == list(SUPPORTED_ACTIONS),
             'Unrecognized operation contract')
    inputs = doc['actor_inputs']
    _require(isinstance(inputs, dict) and inputs, 'Actor inputs required')
    for case_id, binding in inputs.items():
        _require(re.fullmatch(r'solo-[a-z0-9-]+', case_id), 'Invalid case ID')
        _binding(binding, 'actor_inputs')
        _require(binding['path'] == 'actor_inputs/' + case_id + '.json', 'Case/path identity mismatch')
    _keys(doc['evaluator_only'], 'setup oracle')
    for key, binding in doc['evaluator_only'].items():
        _binding(binding, 'evaluator_only')
        _require(binding['path'] == 'evaluator_only/' + key + '.json', 'Invalid evaluator binding')
    return doc


def _actor(doc, case_id):
    _keys(doc, 'schema_version fixture_id case_id source_ref intent_ref processing_classification '
          'actor_id user_intent context')
    _require(type(doc['schema_version']) is int and doc['schema_version'] == 1
             and doc['fixture_id'] == FIXTURE_ID and doc['case_id'] == case_id
             and doc['source_ref'] == SOURCE_REF
             and doc['intent_ref'] == SOURCE_REF + ':' + case_id
             and doc['processing_classification'] == PROCESSING
             and doc['actor_id'] == 'founder', 'Actor input identity/classification mismatch')
    _text(doc['user_intent'])
    context = doc['context']
    _keys(context, 'revision location elapsed_seconds own_inventory reserved_for_work '
          'protected_seed_grain accepted_rights camp_established shelter_worked_seconds')
    for key in ('revision', 'elapsed_seconds', 'protected_seed_grain', 'shelter_worked_seconds'):
        _number(context[key])
    _require(context['location'] in ('commons', 'clearing')
             and type(context['camp_established']) is bool
             and context['accepted_rights'] == ['camp', 'temporary_dwelling'], 'Invalid visible context')
    for key in ('own_inventory', 'reserved_for_work'):
        _keys(context[key], 'grain timber axe')
        for value in context[key].values():
            _number(value)
    for material, reserved in context['reserved_for_work'].items():
        _require(reserved <= context['own_inventory'][material], 'Reserved resources exceed inventory')
    _require(context['protected_seed_grain'] <= context['own_inventory']['grain'], 'Seed exceeds inventory')
    _require('EVALUATOR_ONLY_' not in json.dumps(doc), 'Hidden oracle leaked into actor input')
    return doc


def export_actor_input(case_id, root=DEFAULT_ROOT):
    """Return one hash-checked actor document; never open setup or oracle files.

    A trusted manifest/release and validate_fixture are required at intake. This
    is a content boundary, not a sanitizer for arbitrary unreviewed prose.
    """
    manifest = load_manifest(root)
    _require(case_id in manifest['actor_inputs'], 'Unknown actor case ID')
    binding = manifest['actor_inputs'][case_id]
    return _actor(_read(root, binding['path'], 'actor_inputs', binding['sha256']), case_id)


def load_evaluator_data(root=DEFAULT_ROOT):
    """Evaluator only. Do not place this return value in actor/provider input."""
    manifest = load_manifest(root)
    return {key: _read(root, binding['path'], 'evaluator_only', binding['sha256'])
            for key, binding in manifest['evaluator_only'].items()}


def validate_fixture(root=DEFAULT_ROOT):
    manifest = load_manifest(root)
    actors = {case: export_actor_input(case, root) for case in manifest['actor_inputs']}
    evaluator = load_evaluator_data(root)
    setup, oracle = evaluator['setup'], evaluator['oracle']
    _keys(setup, 'schema_version fixture_id source_ref choices')
    _keys(oracle, 'schema_version fixture_id source_ref hidden_markers hidden_facts cases final_state')
    for doc in (setup, oracle):
        _require(type(doc['schema_version']) is int and doc['schema_version'] == 1
                 and doc['fixture_id'] == FIXTURE_ID and doc['source_ref'] == SOURCE_REF,
                 'Evaluator identity/version mismatch')
    _keys(setup['choices'], 'template_id founder_name household_name settlement_name region_name '
          'date_label company permission supplies')
    _require(setup['choices']['template_id'] == 'R00' and setup['choices']['company'] == 'solo'
             and setup['choices']['permission'] == 'held' and setup['choices']['supplies'] == 'basic',
             'Unsupported fixture setup')
    for value in setup['choices'].values():
        _text(value)
    _keys(oracle['hidden_facts'], 'opening_npc_inventory standing_project')
    _keys(oracle['hidden_facts']['opening_npc_inventory'], 'grain timber axe')
    for value in oracle['hidden_facts']['opening_npc_inventory'].values():
        _number(value)
    _text(oracle['hidden_facts']['standing_project'])
    markers = oracle['hidden_markers']
    _require(isinstance(markers, list) and markers, 'Hidden boundary markers required')
    for marker in markers:
        _text(marker)
        _require(len(marker) >= 16 and marker.startswith('EVALUATOR_ONLY_'),
                 'Invalid evaluator boundary marker')
    actor_bytes = json.dumps(actors, sort_keys=True)
    _require(all(marker not in actor_bytes for marker in markers), 'Hidden oracle leaked into actor input')
    cases = oracle['cases']
    _require(isinstance(cases, list) and cases, 'Evaluation cases required')
    seen, outcomes, requests = set(), [], {}
    for case in cases:
        _keys(case, 'case_id kind request_id request_revision action_id source_ref intent_ref '
              'replay_of expected')
        case_id = case['case_id']
        _require(case_id in actors and case_id not in seen, 'Unknown or duplicate evaluator case')
        _require(case['source_ref'] == SOURCE_REF and case['intent_ref'] == actors[case_id]['intent_ref'],
                 'Missing source/intent binding')
        _require(isinstance(case['request_id'], str)
                 and re.fullmatch(r'[A-Za-z0-9_-]{1,128}', case['request_id']), 'Invalid request ID')
        _number(case['request_revision'])
        kind = case['kind']
        _require(kind in ('legitimate', 'denied', 'unsupported', 'stale', 'replay', 'changed_replay'),
                 'Unknown case kind')
        _require(isinstance(case['action_id'], str)
                 and (case['action_id'] not in SUPPORTED_ACTIONS if kind == 'unsupported'
                      else case['action_id'] in SUPPORTED_ACTIONS), 'Action/support classification mismatch')
        prior = case['replay_of']
        if kind in ('replay', 'changed_replay'):
            _require(prior in seen and requests[prior]['kind'] == 'legitimate', 'Replay needs a prior accepted request')
            original = requests[prior]
            _require(case['request_id'] == original['request_id']
                     and ((case['action_id'] == original['action_id']) == (kind == 'replay')),
                     'Replay request identity/payload mismatch')
        else:
            _require(prior is None and case['request_id'] not in {r['request_id'] for r in requests.values()},
                     'Duplicate request ID without replay binding')
        expected = case['expected']
        _keys(expected, 'revision clock elapsed_seconds location camp_established '
              'founder_timber npc_timber shelter_status shelter_worked_seconds')
        for key in ('revision', 'clock', 'elapsed_seconds', 'founder_timber', 'npc_timber', 'shelter_worked_seconds'):
            _number(expected[key])
        _require(expected['location'] in ('commons', 'clearing')
                 and type(expected['camp_established']) is bool
                 and expected['shelter_status'] in ('absent', 'active', 'complete'), 'Invalid outcome schema')
        seen.add(case_id)
        requests[case_id] = case
        outcomes.append(kind)
    _require(seen == set(actors), 'Actor/evaluator coverage mismatch')
    _require(outcomes.count('legitimate') >= 2 and all(kind in outcomes for kind in
             ('denied', 'unsupported', 'stale', 'replay', 'changed_replay')), 'Required runtime coverage missing')
    _keys(oracle['final_state'], 'elapsed_seconds founder_inventory npc_inventory material_consumption shelter_places')
    for key in ('elapsed_seconds', 'shelter_places'):
        _number(oracle['final_state'][key])
    for key in ('founder_inventory', 'npc_inventory', 'material_consumption'):
        _keys(oracle['final_state'][key], 'grain timber axe')
        for value in oracle['final_state'][key].values():
            _number(value)
    return {'status': 'verified', 'fixture_id': FIXTURE_ID, 'cases': len(cases),
            'legitimate_actions': outcomes.count('legitimate'), 'actor_oracle_separation': True,
            'runtime_execution_verified_by_schema': False, 'public_discovery': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    parser.add_argument('--export-actor', metavar='CASE_ID')
    args = parser.parse_args()
    result = (export_actor_input(args.export_actor, args.root) if args.export_actor
              else validate_fixture(args.root))
    print(json.dumps(result, ensure_ascii=False))
