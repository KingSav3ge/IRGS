"""Report whether a coordinator-reviewed three-component update may be joined."""
import argparse
import json
from pathlib import Path
import re
import subprocess

COMPONENTS = ('engine', 'app', 'catalog')
ROOT = Path(__file__).resolve().parent.parent


def assess(document, commits, pins):
    reasons = []
    if document.get('schema_version') != 1 or not document.get('cycle_id'):
        return {'status': 'held', 'ready': False, 'reasons': ['No valid coordinator cycle is recorded.']}
    baseline = document.get('baseline_components', {})
    reviews = document.get('reviews', {})
    for name in COMPONENTS:
        commit = commits.get(name, '')
        if not re.fullmatch(r'[a-f0-9]{40}', commit):
            reasons.append(name + ': no exact component commit selected.')
        if not re.fullmatch(r'[a-f0-9]{40}', baseline.get(name, '')):
            reasons.append(name + ': the integrated baseline commit is missing.')
        if commit == baseline.get(name):
            reasons.append(name + ': no update since the last integrated component set.')
        review = reviews.get(name, {})
        if (review.get('status') != 'approved' or review.get('commit') != commit
                or review.get('deliverable') != 'component_update'):
            reasons.append(name + ': this exact component update needs coordinator approval.')
        checks = review.get('checks', [])
        if not checks or any(c.get('status') != 'passed' for c in checks):
            reasons.append(name + ': passing review evidence is incomplete.')
    for name in ('engine', 'catalog'):
        if pins.get(name) != commits.get(name):
            reasons.append('app: its ' + name + ' dependency pin differs from the selected commit.')
    return {'cycle_id': document['cycle_id'], 'status': 'ready' if not reasons else 'held',
        'ready': not reasons, 'selected_components': commits, 'reasons': reasons}


def from_file(root, commits, pins):
    path = root / 'COORDINATION.json'
    document = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    return assess(document, commits, pins)


def require_ready(root, commits, pins):
    result = from_file(root, commits, pins)
    if not result['ready']:
        raise ValueError('Unified integration is held: ' + '; '.join(result['reasons']))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in COMPONENTS:
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    def git(path, revision):
        return subprocess.check_output(['git', '-C', str(path), 'rev-parse', revision], text=True).strip()
    commits = {name: git(getattr(args, name), 'HEAD') for name in COMPONENTS}
    pins = {name: git(args.app, 'HEAD:' + name.title()) for name in ('engine', 'catalog')}
    result = from_file(ROOT, commits, pins)
    print(json.dumps(result, indent=2))
    return 0 if result['ready'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
