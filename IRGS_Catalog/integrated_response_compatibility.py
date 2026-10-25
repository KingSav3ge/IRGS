"""Separate exact-consumer follow-up; original fixture identities stay intact."""
import hashlib
import importlib.util
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
# Resolve only this Catalog's checked sibling, without changing sys.path or
# accepting a same-named module from another checkout or import cache.
_dependency = ROOT / 'response_depot_compatibility.py'
if any(path.is_symlink() for path in (_dependency, *_dependency.parents)):
    raise ValueError('Linked compatibility code')
_spec = importlib.util.spec_from_file_location('catalog_owned_response_depot_compatibility', _dependency)
original = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(original)
CONTRACT = 'evaluation/integrated_responses_v1/compatibility.json'
SOURCE = 'evaluation/shared_responses_v1/manifest.json'
SOURCE_SHA256 = 'fc45e92af7c869924695450f4e995621779e4d4dae6058c72ebe416310ceded1'


def load_contract(root=ROOT):
    root = Path(root)
    doc = original.read_json(root / CONTRACT)
    original.keys(doc, 'schema_version compatibility_id classification rights source_fixture consumers presentation_contract context_ids')
    original.require(type(doc['schema_version']) is int and doc['schema_version'] == 1
        and doc['compatibility_id'] == 'irgs-integrated-responses-v1'
        and doc['classification'] == 'offline-synthetic-consumer-qualification',
        'Unsupported integrated response identity')
    original.require(doc['source_fixture'] == {'fixture_id': 'irgs-shared-responses-v1',
        'manifest': SOURCE, 'sha256': SOURCE_SHA256}, 'Original shared fixture binding changed')
    source = original.load_fixture(root)
    original.require(hashlib.sha256((root / SOURCE).read_bytes()).hexdigest() == SOURCE_SHA256,
                     'Original shared fixture manifest changed')
    original.require(doc['rights'] == source['rights'], 'Original offline evaluation rights required')
    original.keys(doc['consumers'], 'engine_commit app_commit app_catalog_pin')
    original.require(all(isinstance(v, str) and re.fullmatch(r'[0-9a-f]{40}', v)
                         for v in doc['consumers'].values()), 'Exact integrated consumer commits required')
    original.require(doc['consumers'] != source['consumers'], 'Follow-up must select its own consumer pair')
    presentation = doc['presentation_contract']
    original.require(presentation == {'schema_version': 1, 'view_field': 'local_responses',
        'saved_result_field': 'presentation', 'catalog_library_id': 'irgs-response-depot-v1',
        'engine_library_id': 'irgs-engine-routine-responses-v1', 'format': 'plain_text',
        'provider_calls': 0, 'model_tokens': 0}, 'Supported local/saved presentation contract required')
    original.require(type(presentation['schema_version']) is int
        and type(presentation['provider_calls']) is int and type(presentation['model_tokens']) is int,
        'Presentation version and usage counts must be integers')
    original.require(doc['context_ids'] == ['rise', 'quay'], 'Both independently initialized contexts required')
    return doc


def export_actor_input(context_id, root=ROOT):
    load_contract(root)
    return original.export_actor_input(context_id, root)


def load_evaluator_data(root=ROOT):
    load_contract(root)
    return original.load_evaluator_data(root)


def validate_compatibility(root=ROOT):
    doc = load_contract(root)
    return {'status': 'verified', 'compatibility_id': doc['compatibility_id'],
        'contexts': len(doc['context_ids']), 'source_cases': 9,
        'original_manifest_preserved': True, 'runtime_execution_verified_by_schema': False}


if __name__ == '__main__':
    import json
    print(json.dumps(validate_compatibility()))
