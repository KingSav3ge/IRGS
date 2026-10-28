"""Versioned multi-session evaluator input; never a gameplay authority."""
import copy
import hashlib
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = 'evaluation/alpha_journeys_v1'
CASES = ('quay-contact', 'rise-r00')
REQUIRED = ('npc_decisions', 'institution_reactions', 'needs_recovery', 'risk_conflict', 'live_provider',
    'older_restore_branch')
BASELINE = 'evaluation/alpha_contexts_v1/manifest.json'
BASELINE_SHA256 = '69472b54d1f4d9cf6bdac8698bce4a504fbbb3160302ce01a759f4cee007ff46'
_path = ROOT / 'alpha_context_evaluation.py'
if any(p.is_symlink() for p in (_path, *_path.parents)):
    raise ValueError('Linked evaluation code')
_spec = importlib.util.spec_from_file_location('catalog_owned_alpha_context', _path)
baseline = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(baseline)
source = baseline.source


def load_fixture(root=ROOT):
    root = Path(root); directory = root / FIXTURE
    doc = source.read_json(directory / 'manifest.json')
    source.keys(doc, 'schema_version fixture_id classification rights consumers baseline contexts evaluator_only files_sha256')
    source.require(type(doc['schema_version']) is int and doc['schema_version'] == 1
        and doc['fixture_id'] == 'irgs-alpha-journeys-v1'
        and doc['classification'] == 'offline-synthetic-journey-evaluation', 'Invalid journey identity')
    source.require(doc['rights'] == {'authorship': 'original-synthetic-journey-instructions',
        'imported_prose': 'none', 'permitted_processing': ['local-validation', 'offline-synthetic-consumer-tests'],
        'external_processing': 'not-authorized-by-fixture'}, 'Offline-only rights required')
    source.require(doc['consumers'] == {'engine_candidate': 'ea0631b8fbf94f425fa003d81b6907445a9a43c5',
        'app_commit': 'b3a53cfd11bbd3745253520b4e8ed6718c826ab8',
        'app_engine_pin': 'efc84364b86e640f5028bfac2dfd5ae3021695a9',
        'app_catalog_pin': '6f927b00e12a3339861ac353bc38d03c68279662'}, 'Exact candidate and committed pins required')
    source.require(doc['baseline'] == {'path': BASELINE, 'sha256': BASELINE_SHA256}, 'Baseline binding changed')
    baseline.load_fixture(root)
    source.require(hashlib.sha256((root / BASELINE).read_bytes()).hexdigest() == BASELINE_SHA256,
        'Baseline bytes changed')
    expected = {'actor_inputs/' + case + '.json' for case in CASES} | {'evaluator_only/oracle.json', 'evidence.schema.json'}
    source.require(doc['contexts'] == {case: 'actor_inputs/' + case + '.json' for case in CASES}
        and doc['evaluator_only'] == 'evaluator_only/oracle.json' and set(doc['files_sha256']) == expected,
        'Separate actor instructions and evaluator truth required')
    actual = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()
        and p.name not in ('README.md', 'manifest.json')}
    source.require(actual == expected, 'Unexpected journey payload')
    values = {}
    for name in expected:
        path = directory / name; values[name] = source.read_json(path)
        source.require(hashlib.sha256(path.read_bytes()).hexdigest() == doc['files_sha256'][name], 'Journey payload hash mismatch')
    for case in CASES:
        actor = values[doc['contexts'][case]]
        source.keys(actor, 'case_id source_ref selection actions')
        selection = {'profile_id': 'military', 'scenario_id': 'hundred-years-war', 'entry_id': 'hyw-1415',
            'character': 'new-human', 'opening_id': 'quay-contact-v1'} if case == 'quay-contact' else {
            'template_id': 'R00', 'fixture_id': 'irgs-solo-r00-eval-v1'}
        source.require(actor['case_id'] == case and actor['source_ref'] == 'authored-synthetic:irgs-catalog:alpha-journeys:v1'
            and actor['selection'] == selection and isinstance(actor['actions'], list)
            and all(isinstance(a, str) and a and 'PRIVATE_' not in a for a in actor['actions']),
            'Actor instructions cannot inject private or privileged state')
    oracle = values[doc['evaluator_only']]
    source.keys(oracle, 'classification marker cases unexecuted_requirements')
    source.require(oracle['classification'] == 'evaluator-only' and oracle['marker'] == 'PRIVATE_JOURNEY_ORACLE'
        and set(oracle['cases']) == set(CASES) and oracle['unexecuted_requirements'] == list(REQUIRED),
        'Unexecuted Alpha requirements must remain explicit')
    schema = values['evidence.schema.json']
    source.require(schema == {'schema_version': 1, 'classification': 'evaluator-observation-not-runtime-authority',
        'required_fields': ['case_id', 'engine_commit', 'app_commit', 'app_engine_pin', 'sessions',
            'receipt_ids', 'retry_verified', 'restore_verified', 'pending_requirements', 'alpha_qualified'],
        'case_ids': list(CASES), 'pending_requirements': list(REQUIRED), 'alpha_qualified': False},
        'Journey evidence scope changed')
    return doc


def export_actor_input(case, root=ROOT):
    doc = load_fixture(root); source.require(case in CASES, 'Unknown journey')
    return copy.deepcopy(source.read_json(Path(root) / FIXTURE / doc['contexts'][case]))


def load_evaluator_data(root=ROOT):
    doc = load_fixture(root)
    return source.read_json(Path(root) / FIXTURE / doc['evaluator_only'])


def assess_evidence(evidence):
    """Validate evaluator claims only; callers must independently verify actual receipts."""
    source.keys(evidence, 'case_id engine_commit app_commit app_engine_pin sessions receipt_ids '
        'retry_verified restore_verified pending_requirements alpha_qualified')
    source.require(evidence['case_id'] in CASES
        and evidence['engine_commit'] == 'ea0631b8fbf94f425fa003d81b6907445a9a43c5'
        and evidence['app_commit'] == 'b3a53cfd11bbd3745253520b4e8ed6718c826ab8'
        and evidence['app_engine_pin'] == 'efc84364b86e640f5028bfac2dfd5ae3021695a9'
        and type(evidence['sessions']) is int and evidence['sessions'] >= 2
        and type(evidence['retry_verified']) is bool and type(evidence['restore_verified']) is bool
        and evidence['alpha_qualified'] is False and evidence['pending_requirements'] == list(REQUIRED),
        'Invalid journey evidence or an unsupported Alpha claim')
    ids = evidence['receipt_ids']
    source.require(isinstance(ids, list) and len(ids) >= 2 and all(isinstance(v, str) and v for v in ids)
        and len(set(ids)) == len(ids), 'Distinct received result identities required')
    return {'structurally_valid': True, 'engine_override': True,
        'alpha_qualified': False, 'runtime_execution_verified_by_schema': False}


def validate_fixture(root=ROOT):
    doc = load_fixture(root)
    return {'status': 'verified', 'fixture_id': doc['fixture_id'], 'contexts': 2,
        'alpha_qualified': False, 'runtime_execution_verified_by_schema': False}
