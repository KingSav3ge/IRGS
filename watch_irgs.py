#!/usr/bin/env python3
"""Watch published IRGS commits and publish isolated QA artifacts.

Never checks out or edits Engine/App branches. Candidate trees are disposable
verification extracts. The QA branch contains reports and test tooling only.
"""
import argparse
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tarfile
import time
from datetime import datetime, timezone

BRANCHES = ('main', '3.3.3.A', '3.3.3.E')
QA_BRANCH = 'qa/engine-validation'


def timestamp(): return datetime.now(timezone.utc).isoformat()


def git(repo, *arguments, data=None, check=True):
    result = subprocess.run(['git', '-C', str(repo), *arguments], input=data,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, check=False)
    if check and result.returncode:
        raise RuntimeError('git ' + arguments[0] + ': ' + result.stderr.decode(errors='replace')[-1800:])
    return result


def extract_candidate(repo, commit, source):
    if source.exists():
        # Never overwrite a prior snapshot or any user-owned directory.
        raise RuntimeError('Candidate directory already exists; use a fresh run identity')
    source.mkdir(parents=True)
    data = git(repo, 'archive', '--format=tar', commit).stdout
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:') as archive:
        entries = archive.getmembers()
        if len(entries) > 20000 or sum(e.size for e in entries) > 1024**3:
            raise RuntimeError('Candidate archive exceeds QA extraction bounds')
        for entry in entries:
            path = PurePosixPath(entry.name)
            if path.is_absolute() or '..' in path.parts or '\\' in entry.name:
                raise RuntimeError('Unsafe candidate path')
            if not (entry.isfile() or entry.isdir()):
                raise RuntimeError('QA does not extract links or special files')
            if any(part.lower() in {'saves', 'trash', 'live', '__pycache__', '.git', '.aws', '.ssh', '.codex', 'credentials'} for part in path.parts):
                continue
            target = source.joinpath(*path.parts)
            if entry.isdir(): target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(entry) as incoming, target.open('xb') as outgoing:
                    shutil.copyfileobj(incoming, outgoing)


def publish(repo, directory, report, state):
    """Commit only known QA artifacts, using Git objects rather than checkout edits."""
    remote = git(repo, 'ls-remote', '--heads', 'origin', 'refs/heads/' + QA_BRANCH).stdout.decode().strip()
    parent = None
    if remote:
        expected = remote.split()[0]
        git(repo, 'fetch', 'origin', 'refs/heads/' + QA_BRANCH)
        parent = git(repo, 'rev-parse', 'FETCH_HEAD').stdout.decode().strip()
        if parent != expected:
            raise RuntimeError('QA report branch advanced during publication; retry next cycle')
    history = []
    if parent:
        old = git(repo, 'show', parent + ':HISTORY.json', check=False)
        if old.returncode == 0: history = json.loads(old.stdout)
    history.append({key: report[key] for key in ('candidate_commit', 'candidate_branches', 'status', 'finished_at_utc')})
    files = {'README.md': (directory/'README.md').read_bytes(),
             'qa_irgs.py': (directory/'qa_irgs.py').read_bytes(),
             'watch_irgs.py': (directory/'watch_irgs.py').read_bytes(),
             'LATEST.json': (json.dumps(report, indent=2)+'\n').encode(),
             'LATEST.md': (Path(report['report_path']).with_suffix('.md')).read_bytes(),
             'HISTORY.json': (json.dumps(history[-200:], indent=2)+'\n').encode(),
             'CURRENT_REFS.json': (json.dumps(state['remote_refs'], indent=2)+'\n').encode()}
    rows = []
    for name, data in sorted(files.items()):
        blob = git(repo, 'hash-object', '-w', '--stdin', data=data).stdout.decode().strip()
        rows.append(f'100644 blob {blob}\t{name}\n')
    tree = git(repo, 'mktree', data=''.join(rows).encode()).stdout.decode().strip()
    arguments = ['commit-tree', tree]
    if parent: arguments += ['-p', parent]
    arguments += ['-m', f"QA {report['candidate_commit'][:12]}: {report['status']}"]
    commit = git(repo, *arguments).stdout.decode().strip()
    # No force push. A simultaneous writer is retained and causes a retry.
    git(repo, 'push', 'origin', commit + ':refs/heads/' + QA_BRANCH)
    git(repo, 'update-ref', 'refs/remotes/origin/' + QA_BRANCH, commit)
    return commit


def cycle(args, directory, state):
    fetch = ['fetch', 'origin']
    fetch += ['refs/heads/' + branch + ':refs/remotes/origin/' + branch for branch in BRANCHES]
    git(args.repo, *fetch)
    refs = {branch: git(args.repo, 'rev-parse', 'refs/remotes/origin/' + branch).stdout.decode().strip()
            for branch in BRANCHES}
    state['remote_refs'] = refs
    state['last_checked_at_utc'] = timestamp()
    signature = hashlib.sha256((directory/'qa_irgs.py').read_bytes()).hexdigest()
    pending = list(dict.fromkeys(refs.values()))
    processed = 0
    for commit in pending:
        if not re.fullmatch('[0-9a-f]{40}', commit): raise RuntimeError('Invalid candidate identity')
        identity = commit + ':' + signature
        previous = state.setdefault('runs', {}).get(identity)
        if previous and previous.get('published_commit'): continue
        if previous:
            output = Path(previous['report_path'])  # retry a failed publication without retesting
        else:
            run = args.storage/'runs'/(commit[:12] + '-' + str(time.time_ns()))
            source = run/'candidate'; output = run/'report.json'
            extract_candidate(args.repo, commit, source)
            print(timestamp(), 'Testing', commit, 'branches', [b for b,v in refs.items() if v == commit], flush=True)
            command = [sys.executable, '-B', str(directory/'qa_irgs.py'), '--source-root', str(source),
                       '--commit', commit, '--output', str(output)]
            with (run/'runner.txt').open('w') as log:
                result = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                        timeout=1500, check=False)
            if result.returncode not in (0, 1) or not output.is_file():
                raise RuntimeError('QA runner did not finish; inspect ' + str(run/'runner.txt'))
            previous = {'report_path': str(output)}
            state['runs'][identity] = previous
        report = json.loads(output.read_text())
        report['candidate_branches'] = [b for b,v in refs.items() if v == commit]
        report['report_path'] = str(output)
        published = publish(args.repo, directory, report, state)
        previous['published_commit'] = published
        previous['status'] = report['status']
        state['last_publication'] = {'candidate': commit, 'qa_commit': published, 'status': report['status']}
        args.state.write_text(json.dumps(state, indent=2)+'\n')
        print(timestamp(), 'Published', report['status'], 'for', commit, 'QA commit', published, flush=True)
        processed += 1
    return processed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path('/workspace/IRGS'))
    parser.add_argument('--storage', type=Path, default=Path('/workspace/irgs-cloud/qa'))
    parser.add_argument('--interval', type=int, default=60)
    parser.add_argument('--once', action='store_true')
    args = parser.parse_args()
    if args.interval < 60: raise SystemExit('Use at least 60 seconds between GitHub checks')
    args.repo = args.repo.resolve(strict=True); args.storage = args.storage.resolve()
    if args.storage.is_relative_to(args.repo): raise SystemExit('Keep QA state and synthetic saves outside source')
    args.storage.mkdir(parents=True, exist_ok=True)
    args.state = args.storage/'watch-state.json'
    directory = Path(__file__).resolve().parent
    with (args.storage/'watch.lock').open('w') as lock:
        try: fcntl.flock(lock, fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: raise SystemExit('An IRGS QA watcher is already active')
        lock.write(str(os.getpid())); lock.flush()
        state = json.loads(args.state.read_text()) if args.state.exists() else {'runs': {}}
        print(timestamp(), 'IRGS QA watcher started; interval', args.interval, 'seconds', flush=True)
        while True:
            state['pid'] = os.getpid()
            try:
                processed = cycle(args, directory, state)
                state.pop('last_error', None)
                if processed == 0 and not state.get('idle_reported'):
                    print(timestamp(), 'No untested published commits; waiting for development updates.', flush=True)
                    state['idle_reported'] = True
                if processed: state['idle_reported'] = False
            except (RuntimeError, OSError, ValueError, subprocess.TimeoutExpired) as error:
                state['last_error'] = {'at': timestamp(), 'message': str(error)}
                print(timestamp(), 'QA infrastructure error:', str(error), flush=True)
                if args.once:
                    args.state.write_text(json.dumps(state, indent=2)+'\n'); return 2
            args.state.write_text(json.dumps(state, indent=2)+'\n')
            if args.once: return 0
            time.sleep(args.interval)


if __name__ == '__main__': raise SystemExit(main())
