"""Catalog qualification of published process starts; historical records stay fixed."""
import hashlib
import importlib.util
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
_dependency = ROOT / 'development_interop_compatibility.py'
if any(path.is_symlink() for path in (_dependency, *_dependency.parents)):
    raise ValueError('Linked compatibility code')
_spec = importlib.util.spec_from_file_location('catalog_owned_development_interop', _dependency)
baseline = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(baseline)
CONTRACT = 'evaluation/phase_responses_v1/compatibility.json'
SOURCE = 'evaluation/development_interop_v1/compatibility.json'
SOURCE_SHA256 = '0b6fe6eb24a67e5b3e37d52da5fe38a98f1892ef6a67c495075692ac4e7f3e85'


def load_contract(root=ROOT):
    root = Path(root)
    original = baseline.baseline.original
    doc = original.read_json(root / CONTRACT)
    original.keys(doc, 'schema_version compatibility_id classification rights source_compatibility '
        'consumers presentation_contract process_contract context_ids qualification_scope')
    original.require(type(doc['schema_version']) is int and doc['schema_version'] == 1
        and doc['compatibility_id'] == 'irgs-phase-responses-v1'
        and doc['classification'] == 'offline-synthetic-consumer-qualification',
        'Unsupported phase response identity')
    original.require(doc['source_compatibility'] == {'path': SOURCE, 'sha256': SOURCE_SHA256},
        'Original interoperability binding changed')
    source = baseline.load_contract(root)
    original.require(hashlib.sha256((root / SOURCE).read_bytes()).hexdigest() == SOURCE_SHA256,
        'Original interoperability bytes changed')
    original.require(doc['rights'] == source['rights'], 'Original offline evaluation rights required')
    consumers = doc['consumers']
    original.keys(consumers, 'engine_commit app_commit app_engine_pin app_catalog_pin')
    original.require(all(isinstance(v, str) and re.fullmatch(r'[0-9a-f]{40}', v)
        for v in consumers.values()), 'Exact phase consumer commits required')
    original.require(consumers['engine_commit'] == consumers['app_engine_pin'],
        'Phase qualification must select the App-pinned Engine')
    original.require(consumers['app_commit'] != source['consumers']['app_commit'],
        'Published starts require a separate App selection')
    presentation = doc['presentation_contract']
    original.require(presentation == {**source['presentation_contract'],
        'phase_engine_library_id': 'irgs-response-depot-v1'}
        and all(type(presentation[key]) is int for key in ('schema_version', 'provider_calls', 'model_tokens')),
        'Native and phase presentation identities and zero usage required')
    process = doc['process_contract']
    original.require(process == {'view_field': 'process_control', 'schema_version': 1,
        'engine_schema': 'irgs-phase-capabilities-1', 'public_start_available': True,
        'commands': ['start', 'advance', 'pause', 'resume', 'inspect', 'cancel']}
        and type(process['schema_version']) is int and process['public_start_available'] is True,
        'Only published Engine-selected phase controls may be qualified')
    original.require(doc['context_ids'] == source['context_ids']
        and doc['qualification_scope'] == 'explicit_candidate_compatibility_not_joined_approval',
        'Both original contexts and separate candidate qualification required')
    return doc


def validate_compatibility(root=ROOT):
    doc = load_contract(root)
    return {'status': 'verified', 'compatibility_id': doc['compatibility_id'],
        'contexts': 2, 'public_process_starts': True,
        'runtime_execution_verified_by_schema': False}


if __name__ == '__main__':
    import json
    print(json.dumps(validate_compatibility()))
