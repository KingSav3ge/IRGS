#!/usr/bin/env python3
"""Qualify the actor-safe selected communication/offer contract offline."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import platform
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'IRGS_3_3/runtime'))


def qualify():
    suite = unittest.defaultTestLoader.loadTestsFromName('test_communication_contract')
    names = []
    def inventory(items):
        for item in items:
            if isinstance(item, unittest.TestSuite): inventory(item)
            else: names.append(item.id())
    inventory(suite)
    output = io.StringIO()
    result = unittest.TextTestRunner(stream=output, verbosity=1).run(suite)
    if not result.wasSuccessful() or result.skipped:
        raise RuntimeError(output.getvalue())
    paths = ['IRGS_3_3/runtime/'+name for name in (
        'communication_contract.py', 'test_communication_contract.py', 'communication_runtime.py',
        'shared_runtime.py', 'runtime_contracts.py', 'player_actions.py', 'core_world.py',
        'scene_actions.py', 'settlement_runtime.py', 'r9_runtime.py', 'r8_dependencies.py',
        'offline_responses.py', 'response_depot.py', 'routine_format.py')]
    paths += ['IRGS_3_3/data/responses/'+name for name in (
        'depot_v1/library.json', 'depot_v1/SOURCE.json', 'engine_routine_v1.json')]
    return {'schema_version': 1, 'status': 'PASS_SELECTED_COMMUNICATION_CAPABILITY_CONTRACT_WITH_LIMITS',
        'date_utc': '2026-10-26', 'target_iteration': 'IRGS 3.4.1 development',
        'python': platform.python_version(), 'api_schema': 'irgs-communication-capabilities-1',
        'pulled_base_commit': 'aa30bb63a3828cbaeb5ee3d1db57edd388a8dc86',
        'tests_run': result.testsRun, 'passed': result.testsRun, 'skipped': len(result.skipped), 'test_ids': names,
        'actual_handler': 'Core execute_local_communication through native typed execution and mandatory host CAS',
        'contexts': {
            'non_rise': 'Synthetic authored-quay speaker and witness; exact attributed testimony, unchanged selected elapsed axis',
            'rise': 'Synthetic reviewed local channel and custody mandates; actual conserved two-grain fulfillment',
            'participants': 'Received attributions only, no names/whereabouts/existence/stock feasibility oracle',
            'sources': 'Exact received evidence, original status/originator, separate evidence and reception sources/times; explicit truncation',
            'offers': 'Original public terms/digest and received offered/declined/withdrawn/superseded/fulfilled statuses',
            'unsupported': 'Absent/unselected channels expose no operation; stock offers require existing selected Rise stock profile'},
        'privacy_regression': 'Reproduced native received() leaking private terms/audience to a third party after forwarding testimony; participant guard now shared by native receipts/presentation, compatibility/offline/shared rendering and the new DTO',
        'dependencies': 'Real R9 execution/rejection reads; actual attempted writes retained on late rollback and never included in public DTOs',
        'scarcity': 'Two ten-grain offers may be proposed against the same free stock; competing acceptance frontier defers both in either order',
        'recovery': ['Exact native CommunicationRequest JSON pending restart', 'Same safe persisted and returned DTO',
            'Explicit boolean acceptance and mandatory CAS', 'Failed save leaves original state unchanged',
            'Lost acknowledgment reload/replay without repeated transfer', 'Concurrent delivery commits once',
            'Changed identity rejected', 'Current control/authority/channel rechecked by Core', 'Stale state and branch/restore fences'],
        'source_sha256': {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in paths},
        'provider_calls': 0, 'model_tokens': 0, 'user_saves_used': False,
        'remaining': ['App-owned communication UI/host adapter, compatible pins and coordinator exact-set qualification',
            'Next Engine increment: host-safe selected Rise travel capabilities over the existing native lifecycle',
            'No new NPC decision, remote channel, universal speech duration, deferred debt or generic dialogue resolver',
            'Broader DEV-06–DEV-17/C2, institutions and distributed host durability remain open',
            'No live inference or model/human-quality qualification']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = qualify()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({key: report[key] for key in ('status', 'tests_run', 'passed', 'skipped')}))
