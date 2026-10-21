"""Build execution-derived coverage over the declared R9 backend/operation pairs.

This replays only the synthetic runtime tests through a detached observer. It
never opens campaigns or overwrites inherited certification reports. A register
is coverage evidence, not adoption or all-branch certification.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
RUNTIME = ROOT / 'IRGS_3_3/runtime'
sys.path.insert(0, str(Path(__file__).resolve().parent))
from operation_inventory import inventory, owner_classification


def source_identity(root=ROOT):
    """Hash code and test inputs; copied historical logs supply no evidence."""
    paths = set((root / 'IRGS_3_3/runtime').glob('*.py'))
    paths.update(root / 'tools' / name for name in
                 ('operation_inventory.py', 'coverage_capture.py', 'build_operation_register.py'))
    paths.update((root / 'tools/tests').glob('test_*.py'))
    for directory in ('IRGS_3_3/data', 'IRGS_3_3/catalog', 'IRGS_3_3/Core', 'engine/Core'):
        paths.update(path for path in (root / directory).rglob('*') if path.is_file())
    release_path = root / 'IRGS_3_3/release.json'
    paths.add(release_path)
    release = json.loads(release_path.read_text(encoding='utf-8'))
    for name in release.get('host_sha256', {}):
        path = (root / name).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError('Release-bound test input escapes the project')
        paths.add(path)
    return {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(paths)}


def pointer(path):
    return '/' + '/'.join(str(part).replace('~', '~0').replace('/', '~1') for part in path)


def _paths(records, key):
    return sorted({tuple(path) for record in records for path in record.get(key, [])})


def owner_labels(paths, validation):
    """Keep complete access paths once; avoid repeating per-path prose."""
    annotated = owner_classification(paths, validation_paths=validation)
    return {key: annotated[key] for key in
            ('owners', 'mapping_scope', 'owner_reference', 'owner_reference_line', 'owner_reference_status')} | {
                'unmapped_paths': [pointer(path) for path in annotated['unmapped_paths']],
                'metadata_paths': [pointer(path) for path in annotated['metadata_paths']],
                'validation': {'owners': annotated['validation']['owners'],
                    'unmapped_path_count': len(annotated['validation']['unmapped_paths']),
                    'metadata_path_count': len(annotated['validation']['metadata_paths']),
                    'note': 'All validation paths remain in validation_reads; detailed namespace '
                            'labels can be reproduced with owner_classification.'}}


def merge_evidence(declarations, records, summary, identity, *, generated_at=None):
    keys = [(row['backend'], row['operation']) for row in declarations]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate backend/operation declarations')
    outcomes = summary.get('test_outcomes', {})
    rows = []
    for declared in declarations:
        matching = [record for record in records
                    if (record['backend'], record['operation']) ==
                       (declared['backend'], declared['operation'])]
        # A caller-supplied usable flag cannot turn a failed test into evidence.
        usable = [record for record in matching if record.get('usable') is True
                  and outcomes.get(record['test_id']) == 'passed']
        successes = [record for record in usable if record['status'] == 'success']
        rejected = [record for record in usable if record['status'] == 'failed_attempt']
        refused = [record for record in matching if record['status'] == 'observation_refused']
        reads, writes = _paths(successes, 'reads'), _paths(successes, 'writes')
        failed_reads = _paths(rejected, 'reads')
        attempted = _paths(rejected, 'attempted_writes')
        validation = _paths(successes + rejected, 'validation_reads')
        owners = owner_labels(reads + writes + failed_reads, validation)
        cases = []
        for record in matching:
            cases.append({key: record[key] for key in
                          ('test_id', 'status', 'executions', 'actual_backend', 'profile',
                           'capture_origin', 'usable', 'reason_code') if key in record} |
                         {'test_outcome': outcomes.get(record['test_id'], 'unknown')})
        row = dict(declared)
        row.update(coverage_status='OBSERVED_SUCCESS_AND_FAILURE' if successes and rejected else
                   'OBSERVED_SUCCESS_ONLY' if successes else
                   'OBSERVED_FAILURE_ONLY' if rejected else 'UNQUALIFIED',
                   successful_observations=sum(record['executions'] for record in successes),
                   rejected_observations=sum(record['executions'] for record in rejected),
                   actual_apply_successes=sum(record['executions'] for record in successes
                                              if record.get('capture_origin') == 'actual_apply'),
                   direct_observe_successes=sum(record['executions'] for record in successes
                                                if record.get('capture_origin') == 'direct_observe'),
                   all_branches_certified=False,
                   reads=[pointer(path) for path in reads],
                   writes=[pointer(path) for path in writes],
                   failed_attempt_reads=[pointer(path) for path in failed_reads],
                   failed_attempt_writes=[],
                   rolled_back_attempted_writes=[pointer(path) for path in attempted],
                   validation_reads=[pointer(path) for path in validation],
                   owner_annotations=owners,
                   test_cases=sorted(cases, key=lambda case: tuple(str(case.get(key, '')) for key in
                                     ('test_id', 'status', 'actual_backend', 'profile', 'capture_origin'))),
                   observation_refusals=len(refused),
                   decision_review='Read paths are execution-derived. Source and test references '
                                   'identify named decision cases; unexecuted branches remain unqualified.')
        rows.append(row)
    outside = [record for record in records
               if (record['backend'], record['operation']) not in set(keys)]
    return {'schema_version': 1, 'milestone': 'DEV-05',
            'generated_at_utc': generated_at or datetime.now(timezone.utc).isoformat(),
            'scope': 'Declared backend/operation inventory with current synthetic test execution; '
                     'not a per-campaign availability list or all-branch certification.',
            'source_sha256': identity,
            'tests': summary,
            'summary': {'operation_spellings': len({row['operation'] for row in rows}),
                        'backend_operation_pairs': len(rows),
                        'backends': sorted({row['backend'] for row in rows}),
                        'pairs_with_success': sum(row['successful_observations'] > 0 for row in rows),
                        'pairs_with_failed_path_evidence': sum(row['rejected_observations'] > 0 for row in rows),
                        'pairs_without_success': sum(row['successful_observations'] == 0 for row in rows),
                        'unqualified_pairs': sum(row['coverage_status'] == 'UNQUALIFIED' for row in rows),
                        'observations_outside_declared_backend_pairs': len(outside),
                        'all_branches_certified': False},
            'limitations': [
                'Observed paths are unions of executed cases, not declared event footprints.',
                'Failed-attempt writes are rolled back and never counted as committed effects.',
                'Tests that fail, error, skip or lack attribution cannot qualify an operation.',
                'A successful direct call must match the observer-selected backend post-state.',
                'Owner annotations interpret known namespaces; unmapped or mixed paths stay explicit.',
                'Validation scans are separate from allocation dependencies.',
                'Legacy aliases are compatibility spellings, not separate maintained engines.',
                'No saved campaigns or inherited coverage logs are inputs. Historical fixture '
                'content is hashed as test input; it does not schedule a historical future.',
                'Actual apply calls and detached observer probes are distinguished. Neither '
                'observation count proves a durable host commit.',
                'Review-handler instrumentation does not certify arbitrary Python plugins.'
            ], 'operations': rows,
            'outside_pair_diagnostics': [{key: record[key] for key in
                ('operation', 'backend', 'actual_backend', 'profile', 'test_id', 'status',
                 'capture_origin', 'reason_code', 'executions') if key in record} for record in outside]}


def check_register(report, *, root=ROOT):
    """Check freshness/completeness without pretending to replay the suite."""
    if report.get('schema_version') != 1 or report.get('milestone') != 'DEV-05':
        raise ValueError('Unsupported operation register')
    if report.get('source_sha256') != source_identity(root):
        raise ValueError('Operation evidence is stale: code, tests or capture tools changed')
    current = inventory(root / 'IRGS_3_3/runtime')
    expected = {(row['backend'], row['operation']) for row in current}
    actual = [(row['backend'], row['operation']) for row in report['operations']]
    if len(actual) != len(set(actual)) or set(actual) != expected:
        raise ValueError('Operation register has missing, extra or duplicate backend/operation pairs')
    for row in report['operations']:
        if row.get('all_branches_certified') is not False or row.get('failed_attempt_writes') != []:
            raise ValueError('Register overclaims qualification or failed effects')
        for case in row.get('test_cases', []):
            if case.get('usable') and case.get('test_outcome') != 'passed':
                raise ValueError('An unsuccessful test was marked as usable evidence')
    if not report['tests'].get('tests_successful'):
        raise ValueError('Captured test execution did not pass')
    return {'status': 'current', 'tests_replayed_by_check': False,
            'backend_operation_pairs': len(actual), 'campaigns_opened': False}


def markdown(report):
    count = report['summary']
    lines = ['# Operation coverage register — DEV-05', '',
             'This is a current-source inventory and execution record, not blanket certification. '
             'Run `python -B tools/build_operation_register.py --check '
             'engine/qualification/operation_register.json` to check freshness. '
             'That check does not rerun the tests.', '',
             f"{count['operation_spellings']} spellings across {count['backend_operation_pairs']} "
             f"backend/operation pairs. {count['pairs_with_success']} pairs have observed successful "
             f"cases; {count['pairs_without_success']} still lack one. "
             f"{count['pairs_with_failed_path_evidence']} pairs have named rejected-path evidence.", '',
             'The machine-readable [register](qualification/operation_register.json) records source '
             'locations, actual read/write paths, rejected reads, rolled-back attempts, owner '
             'annotations, test identities and observation refusals. Unmapped paths and unsupported '
             'backend/profile combinations remain explicit. AST compatibility names share CoreWorld; '
             'they are not a separately maintained engine.', '',
             '| Backend | Operation | Case coverage | Successful observations | Rejected observations |',
             '| --- | --- | --- | ---: | ---: |']
    for row in report['operations']:
        lines.append(f"| {row['backend']} | `{row['operation']}` | "
                     f"{row['coverage_status']} | {row['successful_observations']} | "
                     f"{row['rejected_observations']} |")
    lines += ['', '## Remaining qualification', '',
              'DEV-06–DEV-08 remain open. Expand specific collection, revocation, dissolution, '
              'resource/capacity and decision branches, and compare equivalent serial and simultaneous '
              'cross-engine frontiers. A coverage gap is a development target, not permission to '
              'invent a footprint or advertise an unavailable player action.', '',
              'Namespace-to-owner labels annotate observed access only; they are never used to '
              'authorize actions or determine independence. A test reference identifies an executed '
              'case, not complete branch coverage. The full C2 inventory remains separately preserved.', '']
    return '\n'.join(lines)


def safe_destination(value, suffix):
    path = value.resolve()
    if (not path.is_relative_to(ROOT.resolve()) or path.suffix != suffix or
            any(part.lower() in {'saves', 'trash', '.git', 'live'} for part in path.relative_to(ROOT).parts)):
        raise ValueError('Write qualification artifacts inside the project, outside campaign data')
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--output', type=Path)
    mode.add_argument('--check', type=Path)
    parser.add_argument('--markdown', type=Path)
    parser.add_argument('--test-log', type=Path)
    args = parser.parse_args()
    try:
        if args.check:
            print(json.dumps(check_register(json.loads(args.check.read_text(encoding='utf-8')))))
            return
        from coverage_capture import capture_suite
        before = source_identity()
        declared = inventory(RUNTIME)
        summary, records, log = capture_suite(RUNTIME)
        if args.test_log:
            safe_destination(args.test_log, '.txt').write_text(log, encoding='utf-8', newline='\n')
        if source_identity() != before:
            raise ValueError('Source changed while capturing evidence; rerun after edits stop')
        report = merge_evidence(declared, records, summary, before)
        check_register(report)
        output = safe_destination(args.output, '.json')
        output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
        if args.markdown:
            safe_destination(args.markdown, '.md').write_text(markdown(report), encoding='utf-8', newline='\n')
        print(json.dumps({'status': 'captured', **report['summary'],
                          'tests': {key: value for key, value in summary.items() if key != 'test_outcomes'}}))
    except Exception as error:
        print(json.dumps({'status': 'failed', 'error': str(error)}))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
