"""Published Engine start-context qualification, separate from old baseline data."""
import copy
import hashlib
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = 'evaluation/start_context_v1'
FIXTURE_ID = 'irgs-start-context-v1'
ENGINE_COMMIT = 'cc450a6f00a249d2169cdacdfc9c4b1e03f67cc8'
ENGINE_SCHEMA = 'irgs-start-readiness-1'
CASES = ('henry-1415-observation', 'henry-1415-default', 'john-1415-limited',
         'new-1415-default', 'new-1415-quay', 'rise-r00')
BASELINE = 'evaluation/player_starts_v1/manifest.json'
BASELINE_SHA256 = 'a230fa6e78c8be97d24ec4d7e6fbf01308e1663898c612b86f6903a24d56dbee'
_dependency = ROOT / 'player_start_evaluation.py'
if any(p.is_symlink() for p in (_dependency, *_dependency.parents)):
    raise ValueError('Linked evaluation code')
_spec = importlib.util.spec_from_file_location('catalog_owned_start_baseline', _dependency)
baseline = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(baseline)
source = baseline.source


def load_fixture(root=ROOT):
    root = Path(root)
    directory = root / FIXTURE
    doc = source.read_json(directory / 'manifest.json')
    source.keys(doc, 'schema_version fixture_id classification rights engine_contract baseline_fixture '
        'contexts evaluator_only app_adoption files_sha256')
    source.require(type(doc['schema_version']) is int and doc['schema_version'] == 1
        and doc['fixture_id'] == FIXTURE_ID and doc['classification'] == 'offline-synthetic-contract-qualification',
        'Invalid start-context fixture identity')
    source.require(doc['rights'] == {'authorship': 'original-evaluation-instructions-and-citation-review',
        'imported_articles_or_images': 'none', 'permitted_processing': ['local-validation', 'offline-synthetic-consumer-tests'],
        'external_processing': 'not-authorized-by-fixture'}, 'Explicit offline qualification rights required')
    engine = doc['engine_contract']
    source.keys(engine, 'commit schema api_path files_sha256')
    source.require(engine['commit'] == ENGINE_COMMIT and engine['schema'] == ENGINE_SCHEMA
        and engine['api_path'] == 'engine/START_READINESS_API.md', 'Select the published Engine start contract')
    source.require(set(engine['files_sha256']) == {'engine/START_READINESS_API.md',
        'IRGS_3_3/runtime/start_readiness.py', 'IRGS_3_3/data/henry_1415_observation.json',
        'IRGS_3_3/data/hyw_1415_opening.json'} and all(isinstance(v, str) and len(v) == 64
        and all(c in '0123456789abcdef' for c in v) for v in engine['files_sha256'].values()),
        'Exact published Engine source bindings required')
    source.require(doc['baseline_fixture'] == {'path': BASELINE, 'sha256': BASELINE_SHA256},
        'Original baseline binding changed')
    baseline.load_fixture(root)
    source.require(hashlib.sha256((root / BASELINE).read_bytes()).hexdigest() == BASELINE_SHA256,
        'Original baseline bytes changed')
    expected = {'actor_inputs/' + case + '.json' for case in CASES}
    expected.update(('evaluator_only/oracle.json', 'source_review.json', 'app_acceptance.json'))
    source.require(set(doc['files_sha256']) == expected
        and doc['contexts'] == {case: 'actor_inputs/' + case + '.json' for case in CASES}
        and doc['evaluator_only'] == 'evaluator_only/oracle.json', 'Six separate actor inputs and oracle required')
    actual = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()
        and p.name not in ('manifest.json', 'README.md')}
    source.require(actual == expected, 'Unexpected start-context payload')
    payloads = {}
    for name in sorted(expected):
        payloads[name] = source.read_json(directory / name)
        source.require(hashlib.sha256((directory / name).read_bytes()).hexdigest() == doc['files_sha256'][name],
            'Start-context payload hash mismatch')
    for case in CASES:
        actor = payloads[doc['contexts'][case]]
        source.keys(actor, 'case_id source_ref selection actions intention')
        source.require(actor['case_id'] == case
            and actor['source_ref'] == 'authored-synthetic:irgs-catalog:start-context:v1'
            and isinstance(actor['intention'], str) and 0 < len(actor['intention']) <= 4096
            and isinstance(actor['actions'], list) and all(isinstance(a, str) and a for a in actor['actions']),
            'Invalid actor instruction')
        selection = actor['selection']
        if case == 'rise-r00':
            source.require(selection == {'kind': 'rise', 'fixture_id': 'irgs-solo-r00-eval-v1', 'template_id': 'R00'},
                'Keep original reviewed R00 setup')
            continue
        source.keys(selection, 'kind profile_id scenario_id entry_id character')
        source.require({k: selection[k] for k in ('kind', 'profile_id', 'scenario_id', 'entry_id')} == {
            'kind': 'historical', 'profile_id': 'military', 'scenario_id': 'hundred-years-war', 'entry_id': 'hyw-1415'},
            'Keep the reviewed dated selection')
        character = selection['character']
        if case.startswith(('henry-', 'john-')):
            expected_character = {'kind': 'existing', 'actor_id': 'HYW-JOHN-BEDFORD' if case.startswith('john-') else 'HYW-HENRY-V'}
            if case == 'henry-1415-observation':
                expected_character['opening_id'] = 'henry-1415-embarkation-v1'
            source.require(character == expected_character, 'Opening must remain explicitly actor-bound')
        else:
            source.keys(character, 'kind name species background' + (' opening_id' if case == 'new-1415-quay' else ''))
            source.require(character['kind'] == 'new' and character['species'] == 'human'
                and character['background'] == '' and isinstance(character['name'], str) and bool(character['name']),
                'Explicit synthetic new human required')
            if case == 'new-1415-quay':
                source.require(character['opening_id'] == 'quay-delivery-v1', 'Retain reviewed new-person fiction')
    oracle = payloads['evaluator_only/oracle.json']
    source.keys(oracle, 'classification hidden_marker cases civil_checkpoint john_playable_context')
    source.require(oracle['classification'] == 'evaluator-only' and oracle['hidden_marker'] == 'PRIVATE_START_CONTEXT_ORACLE'
        and set(oracle['cases']) == set(CASES) and oracle['john_playable_context'] == 'held'
        and oracle['civil_checkpoint'] == {'date': '1415-08-11', 'calendar': 'julian', 'precision': 'day',
            'ordinal': 2238109, 'time': None, 'current_calendar_binding': False, 'elapsed_calendar_binding': False},
        'Actor scope, initial civil day and John hold must remain explicit')
    review = payloads['source_review.json']
    source.require(review['classification'] == 'citation-review-not-actor-knowledge'
        and review['accepted_precision'] == 'broad_embarkation_region_only'
        and review['boarding_date_resolution'] == 'unresolved'
        and review['opening_hour'] is None and review['john_personal_context'] == 'not_established'
        and review['articles_reproduced'] is False and review['primary_documents_independently_collated'] is False,
        'Do not resolve the source uncertainty or manufacture personal context')
    pending = {'status': 'pending_adopted_app_revision', 'qualified_app_commit': None,
        'required_cases': list(CASES), 'unexecuted_acceptance': 'app_acceptance.json'}
    source.require(doc['app_adoption'] == pending, 'Do not claim App adoption without a separate exact selection')
    app = payloads['app_acceptance.json']
    source.require(app['status'] == 'not_executed_pending_adoption' and app['qualified_app_commit'] is None
        and app['engine_schema'] == ENGINE_SCHEMA and app['required_cases'] == list(CASES),
        'Pending App acceptance cannot become executed evidence')
    return doc


def export_actor_input(case_id, root=ROOT):
    doc = load_fixture(root)
    source.require(case_id in CASES, 'Unknown start-context case')
    return copy.deepcopy(source.read_json(Path(root) / FIXTURE / doc['contexts'][case_id]))


def load_evaluator_data(root=ROOT):
    doc = load_fixture(root)
    return source.read_json(Path(root) / FIXTURE / doc['evaluator_only'])


def validate_fixture(root=ROOT):
    doc = load_fixture(root)
    return {'status': 'verified', 'fixture_id': doc['fixture_id'], 'cases': 6, 'engine_schema': ENGINE_SCHEMA,
        'app_adoption': doc['app_adoption']['status'], 'actor_oracle_separation': True,
        'engine_execution_verified_by_schema': False, 'app_execution_qualified': False}


if __name__ == '__main__':
    import json
    print(json.dumps(validate_fixture()))
