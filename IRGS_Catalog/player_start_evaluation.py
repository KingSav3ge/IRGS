"""Catalog evaluation material, not a runtime capability or initialization API."""
import copy
import hashlib
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = 'evaluation/player_starts_v1'
FIXTURE_ID = 'irgs-player-starts-v1'
CASES = ('john-1415-existing', 'new-1415-default', 'new-1415-quay', 'rise-r00')
BOOL_FIELDS = ('reference_ready', 'actor_eligible', 'mode_confirmed',
    'actor_context_reviewed', 'actor_context_received', 'supported_operation_listed',
    'operation_confirmed', 'result_received', 'save_reload_verified', 'exact_retry_verified',
    'civil_date_matches_source')
LOOP_FIELDS = ('actor_eligible', 'actor_context_reviewed', 'actor_context_received',
    'supported_operation_listed', 'operation_confirmed', 'result_received',
    'save_reload_verified', 'exact_retry_verified')
MODES = ('unclassified', 'reference_only', 'declaration_only', 'executable_slice', 'unavailable')
_dependency = ROOT / 'response_depot_compatibility.py'
if any(p.is_symlink() for p in (_dependency, *_dependency.parents)):
    raise ValueError('Linked evaluation code')
_spec = importlib.util.spec_from_file_location('catalog_owned_start_json', _dependency)
source = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(source)


def assess_evidence(evidence):
    """Assess a synthetic evaluator report; never authorize or modify a world.

    The collector must verify each item against actual owner interfaces/results.
    Structurally valid caller claims alone are not executed acceptance evidence.
    Reference readiness and eligibility cannot imply a working gameplay loop.
    """
    source.keys(evidence, 'schema_version case_id explicit_mode ' + ' '.join(BOOL_FIELDS))
    source.require(type(evidence['schema_version']) is int and evidence['schema_version'] == 1
        and evidence['case_id'] in CASES and evidence['explicit_mode'] in MODES
        and all(type(evidence[key]) is bool for key in BOOL_FIELDS), 'Invalid start evaluation evidence')
    loop = all(evidence[key] for key in LOOP_FIELDS)
    mode = evidence['explicit_mode']
    labelled = evidence['mode_confirmed'] and mode != 'unclassified'
    if mode == 'executable_slice':
        labelled = labelled and loop
    civil_required = evidence['case_id'] != 'rise-r00'
    civil = not civil_required or evidence['civil_date_matches_source']
    return {'loop_verified': loop, 'mode_review_verified': labelled,
        'civil_date_required': civil_required, 'civil_date_verified': evidence['civil_date_matches_source'],
        'supported_start_accepted': loop and labelled and mode == 'executable_slice' and civil
            and evidence['reference_ready'],
        'runtime_authorization_granted': False}


def load_fixture(root=ROOT):
    root = Path(root)
    directory = root / FIXTURE
    manifest = source.read_json(directory / 'manifest.json')
    source.keys(manifest, 'schema_version fixture_id classification status rights consumers '
        'assessment contexts evaluator_only files_sha256')
    source.require(type(manifest['schema_version']) is int and manifest['schema_version'] == 1
        and manifest['fixture_id'] == FIXTURE_ID
        and manifest['classification'] == 'offline-synthetic-start-evaluation'
        and manifest['status'] == 'requirements_and_baseline_diagnostics', 'Invalid start fixture identity')
    source.require(manifest['rights'] == {
        'authorship': 'original-authored-evaluation-instructions-and-source-references',
        'imported_prose': 'none', 'permitted_processing': ['local-validation', 'offline-synthetic-consumer-tests'],
        'external_processing': 'not-authorized-by-fixture'}, 'Explicit offline evaluation rights required')
    source.require(manifest['consumers'] == {
        'engine_commit': '91b20056e7db651966c9e92925313494917f47b1',
        'app_commit': '00634b15f2d8d4a8626d3eb3cb0a139559ac1fcc',
        'app_catalog_pin': '3f921252e50a0976cb88321b6ff8249a5f12466d'}, 'Keep the evaluated baseline selection')
    source.keys(manifest['assessment'], 'joined_commit path sha256 runtime_fix_claimed')
    source.require(manifest['assessment']['joined_commit'] == 'ba551af285a6e1eb0766a9d06f83cbc0e5335b35'
        and manifest['assessment']['runtime_fix_claimed'] is False, 'Assessment is not an implemented fix')
    expected = {'actor_inputs/' + case + '.json' for case in CASES}
    expected.update(('evaluator_only/criteria.json', 'requirements/john_1415.json', 'evidence.schema.json'))
    source.require(set(manifest['files_sha256']) == expected
        and manifest['evaluator_only'] == 'evaluator_only/criteria.json', 'Actor/evaluator separation changed')
    actual = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()
        and p.name not in ('manifest.json', 'README.md')}
    source.require(actual == expected, 'Unexpected start evaluation payload')
    documents = {}
    for name in sorted(expected):
        documents[name] = source.read_json(directory / name)
        source.require(hashlib.sha256((directory / name).read_bytes()).hexdigest() == manifest['files_sha256'][name],
            'Start evaluation payload hash mismatch')
    source.require(manifest['contexts'] == {case: 'actor_inputs/' + case + '.json' for case in CASES},
        'All four independent starting paths required')
    for case in CASES:
        doc = documents[manifest['contexts'][case]]
        source.keys(doc, 'case_id source_ref selection actions declaration')
        source.require(doc['case_id'] == case and doc['source_ref'] == 'authored-synthetic:irgs-catalog:player-starts:v1'
            and isinstance(doc['declaration'], str) and 0 < len(doc['declaration']) <= 1000,
            'Invalid actor input')
        source.require(isinstance(doc['actions'], list) and all(isinstance(a, str) and a for a in doc['actions']),
            'Actions must select existing published operations')
        selection = doc['selection']
        if case != 'rise-r00':
            source.keys(selection, 'kind profile_id scenario_id entry_id character')
            source.require({k: selection[k] for k in ('kind', 'profile_id', 'scenario_id', 'entry_id')} == {
                'kind': 'historical', 'profile_id': 'military', 'scenario_id': 'hundred-years-war', 'entry_id': 'hyw-1415'},
                'Use the reported historical entry')
            character = selection['character']
            if case == 'john-1415-existing':
                source.require(character == {'kind': 'existing', 'actor_id': 'HYW-JOHN-BEDFORD'},
                    'Do not attach fictional circumstances to the historical person')
            else:
                fields = 'kind name species background' + (' opening_id' if case == 'new-1415-quay' else '')
                source.keys(character, fields)
                source.require(character['kind'] == 'new' and character['species'] == 'human'
                    and character['background'] == '' and isinstance(character['name'], str) and bool(character['name']),
                    'Explicit synthetic new human required')
                if case == 'new-1415-quay':
                    source.require(character['opening_id'] == 'quay-delivery-v1', 'Select the existing reviewed opening')
        else:
            source.keys(selection, 'kind fixture_id template_id')
            source.require(selection == {'kind': 'rise', 'fixture_id': 'irgs-solo-r00-eval-v1', 'template_id': 'R00'},
                'Reuse the original R00 setup without its private oracle')
    criteria = documents['evaluator_only/criteria.json']
    source.keys(criteria, 'classification hidden_marker findings cases positive_loop_requires pending_owner_contracts')
    source.require(criteria['classification'] == 'evaluator-only'
        and criteria['hidden_marker'] == 'PRIVATE_PLAYER_START_ORACLE'
        and set(criteria['findings']) == {'IRGS-PLAY-001', 'IRGS-PLAY-002', 'IRGS-PLAY-004'}
        and set(criteria['cases']) == set(CASES)
        and criteria['positive_loop_requires'] == list(LOOP_FIELDS), 'Required playability acceptance changed')
    dossier = documents['requirements/john_1415.json']
    source.keys(dossier, 'status actor_id entry_id source opening reference_claims gaps required_reviews forbidden_inferences')
    source.require(dossier['status'] == 'requirements_pending_owner_contract'
        and dossier['actor_id'] == 'HYW-JOHN-BEDFORD' and dossier['entry_id'] == 'hyw-1415',
        'Requirements do not establish an implemented historical start')
    source.require(dossier['source'] == {
        'repository': 'KingSav3ge/IRGS-Engine', 'commit': manifest['consumers']['engine_commit'],
        'path': 'IRGS_3_3/data/hyw_1415_opening.json',
        'sha256': 'eb182aef5f15ad199e8a54a8d9a7c6890b78ae26631c0125d04f6bb58dc43f34'},
        'Keep the adopted source and exact provenance')
    source.require(dossier['opening'] == {'date': '1415-08-11', 'calendar': 'julian', 'precision': 'day',
        'time': None, 'knowledge_scope': 'historical_setup_reference'}, 'Do not invent an hour or actor receipt')
    source.require(isinstance(dossier['reference_claims'], list) and bool(dossier['reference_claims'])
        and all(isinstance(claim, dict) and claim.get('access') == 'historical_setup_reference_not_actor_receipt'
            for claim in dossier['reference_claims']), 'Reference claims cannot grant player knowledge')
    source.require(set(dossier['gaps']) == {'location', 'received_information', 'resources', 'authority', 'operations', 'civil_time'},
        'Personal context and uncertainty gaps must remain explicit')
    schema = documents['evidence.schema.json']
    props = {'schema_version': {'const': 1, 'type': 'integer'}, 'case_id': {'enum': list(CASES)},
        'explicit_mode': {'enum': list(MODES)}, **{key: {'type': 'boolean'} for key in BOOL_FIELDS}}
    source.require(schema == {'$schema': 'https://json-schema.org/draft/2020-12/schema',
        'title': 'Offline evaluator evidence; not an Engine or App API', 'type': 'object',
        'additionalProperties': False, 'required': list(props), 'properties': props}, 'Evaluation evidence schema changed')
    return manifest


def export_actor_input(case_id, root=ROOT):
    manifest = load_fixture(root)
    source.require(case_id in CASES, 'Unknown player-start case')
    return copy.deepcopy(source.read_json(Path(root) / FIXTURE / manifest['contexts'][case_id]))


def load_evaluator_data(root=ROOT):
    manifest = load_fixture(root)
    return source.read_json(Path(root) / FIXTURE / manifest['evaluator_only'])


def validate_fixture(root=ROOT):
    manifest = load_fixture(root)
    return {'status': 'verified', 'fixture_id': manifest['fixture_id'], 'cases': 4,
        'delivery_scope': manifest['status'], 'actor_oracle_separation': True,
        'runtime_start_contract_implemented': False, 'runtime_execution_verified_by_schema': False}


if __name__ == '__main__':
    import json
    print(json.dumps(validate_fixture()))
