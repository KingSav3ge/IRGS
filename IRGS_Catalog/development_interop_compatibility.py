"""Current development interoperability, separate from pinned historical evidence."""
import hashlib
import importlib.util
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
# Resolve only this Catalog's checked sibling, without changing sys.path or
# accepting a same-named module from another checkout or import cache.
_dependency = ROOT / 'integrated_response_compatibility.py'
if any(path.is_symlink() for path in (_dependency, *_dependency.parents)):
    raise ValueError('Linked compatibility code')
_spec = importlib.util.spec_from_file_location('catalog_owned_integrated_response_compatibility', _dependency)
baseline = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(baseline)
CONTRACT = 'evaluation/development_interop_v1/compatibility.json'
SOURCE = 'evaluation/integrated_responses_v1/compatibility.json'
SOURCE_SHA256 = 'daf1afc0f3dd9c60aaf3da0f69e7477cf5ae7b78e7233c529a7abb307d8da78c'


def load_contract(root=ROOT):
    root = Path(root)
    original = baseline.original
    doc = original.read_json(root / CONTRACT)
    original.keys(doc, 'schema_version compatibility_id classification rights source_compatibility consumers '
                       'presentation_contract process_contract context_ids qualification_scope')
    original.require(type(doc['schema_version']) is int and doc['schema_version'] == 1
        and doc['compatibility_id'] == 'irgs-development-interop-v1'
        and doc['classification'] == 'offline-synthetic-consumer-qualification',
        'Unsupported development interoperability identity')
    original.require(doc['source_compatibility'] == {'path': SOURCE, 'sha256': SOURCE_SHA256},
                     'Original compatibility binding changed')
    source = baseline.load_contract(root)
    original.require(hashlib.sha256((root / SOURCE).read_bytes()).hexdigest() == SOURCE_SHA256,
                     'Original compatibility bytes changed')
    original.require(doc['rights'] == source['rights'], 'Original offline evaluation rights required')
    consumers = doc['consumers']
    original.keys(consumers, 'app_commit engine_commits app_engine_pin app_catalog_pin catalog_at_pull')
    original.keys(consumers['engine_commits'], 'development app_pinned')
    commits = [v for k, v in consumers.items() if k != 'engine_commits'] + list(consumers['engine_commits'].values())
    original.require(all(isinstance(v, str) and re.fullmatch(r'[0-9a-f]{40}', v) for v in commits),
                     'Exact development and pinned commits required')
    original.require(consumers['engine_commits']['app_pinned'] == consumers['app_engine_pin'],
                     'Pinned Engine role must match the committed App pointer')
    original.require(doc['presentation_contract'] == source['presentation_contract']
        and all(type(doc['presentation_contract'][key]) is int
                for key in ('schema_version', 'provider_calls', 'model_tokens')),
        'Original native presentation contract required')
    process = doc['process_contract']
    original.require(process == {'view_field': 'process_control', 'schema_version': 1,
        'commands': ['advance', 'pause', 'resume'], 'public_start_available': False}
        and type(process['schema_version']) is int and process['public_start_available'] is False,
        'Only published received-process controls may be qualified')
    original.require(doc['context_ids'] == source['context_ids']
        and doc['qualification_scope'] == 'explicit_candidate_compatibility_not_joined_approval',
        'Candidate compatibility must remain distinct from joined approval')
    return doc


def validate_compatibility(root=ROOT):
    doc = load_contract(root)
    return {'status': 'verified', 'compatibility_id': doc['compatibility_id'],
            'engine_roles': 2, 'contexts': 2, 'public_process_starts': False,
            'runtime_execution_verified_by_schema': False}


if __name__ == '__main__':
    import json
    print(json.dumps(validate_compatibility()))
