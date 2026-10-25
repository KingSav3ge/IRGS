"""Intake contract for R00 proposal consumer checks; no provider or world code."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
CONTRACT = 'evaluation/solo_r00_proposals_v1/compatibility.json'
FIXTURE = 'evaluation/solo_r00_v1/manifest.json'
FIXTURE_SHA256 = '2d30e863c4f769f0e2039469807ca0c6eeef3f30edd17d96778cebcba65bdbe5'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def keys(value, expected):
    require(isinstance(value, dict) and set(value) == set(expected.split()),
            'Unknown or missing proposal compatibility fields')


def load_contract(root=ROOT):
    root = Path(root)
    path = root / CONTRACT
    require(not any(p.is_symlink() for p in (path, *path.parents)), 'Linked compatibility source')
    require(path.stat().st_size <= 16384, 'Compatibility source exceeds size limit')

    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Duplicate compatibility JSON field')
            result[key] = value
        return result

    doc = json.loads(path.read_bytes(), object_pairs_hook=unique)
    keys(doc, 'schema_version compatibility_id classification source_fixture proposal_schema '
         'operation_id consumers narration_dialogue')
    require(type(doc['schema_version']) is int and doc['schema_version'] == 1
            and doc['compatibility_id'] == 'irgs-solo-r00-proposals-v1'
            and doc['classification'] == 'offline-synthetic-consumer-qualification'
            and doc['proposal_schema'] == 'solo-proposal-1'
            and doc['operation_id'] == 'execute_settlement_action', 'Unsupported compatibility identity')
    source = doc['source_fixture']
    keys(source, 'fixture_id manifest sha256')
    require(source == {'fixture_id': 'irgs-solo-r00-eval-v1', 'manifest': FIXTURE,
                       'sha256': FIXTURE_SHA256}, 'Original R00 fixture binding changed')
    fixture_path = root / FIXTURE
    require(not any(p.is_symlink() for p in (fixture_path, *fixture_path.parents)), 'Linked fixture source')
    require(hashlib.sha256(fixture_path.read_bytes()).hexdigest() == FIXTURE_SHA256,
            'Original R00 fixture hash mismatch')
    consumers = doc['consumers']
    keys(consumers, 'engine_commit app_commits')
    require(isinstance(consumers['engine_commit'], str)
            and re.fullmatch(r'[0-9a-f]{40}', consumers['engine_commit']), 'Exact Engine commit required')
    require(isinstance(consumers['app_commits'], dict)
            and set(consumers['app_commits']) == {'integrated_development', 'component_followup'},
            'Explicit App qualification roles required')
    for commit in consumers['app_commits'].values():
        require(isinstance(commit, str) and re.fullmatch(r'[0-9a-f]{40}', commit), 'Exact App commit required')
    require(len(set(consumers['app_commits'].values())) == 2, 'Duplicate App qualification commits')
    require(doc['narration_dialogue'] == {
        'contract_status': 'not_available', 'evaluation_status': 'awaiting_engine_app_contract'},
        'General narration/dialogue requires its own supported contract and evaluation')
    return doc


def validate_compatibility(root=ROOT):
    doc = load_contract(root)
    return {'status': 'verified', 'compatibility_id': doc['compatibility_id'],
            'app_source_selections': len(doc['consumers']['app_commits']),
            'runtime_execution_verified_by_schema': False,
            'narration_dialogue': doc['narration_dialogue']['evaluation_status']}


if __name__ == '__main__':
    print(json.dumps(validate_compatibility()))
