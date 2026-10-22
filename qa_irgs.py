#!/usr/bin/env python3
"""Independent IRGS QA. Runs candidate code; changes only synthetic test saves.

Usage: python -B qa_irgs.py --source-root PATH --commit SHA --output REPORT.json
This is a QA artifact, not a Core implementation or an alternative simulator.
"""
import argparse
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from urllib.error import HTTPError
from urllib.request import ProxyHandler, Request, build_opener

FINDINGS = {
    'test_new_material_does_not_break_committed_campaign': {
        'id': 'IRGS-QA-001', 'severity': 'P1',
        'title': 'Accepted Core material establishment breaks Rise playthrough views',
        'expected': 'Reject an unsupported material atomically, or retain a readable campaign with explicit unknown unit support.',
        'reproduction': ['Create a reviewed R00 Rise campaign.',
            'Creator POST /api/event: establish_stock(location=founder-home, material=water, quantity=2, inventory_evidence_ref=synthetic-measured-water).',
            'Observe the successful save and valid CoreWorld state.',
            'GET /api/playthrough/<id> with the normal session token.'],
        'boundary': 'IRGS_Web/rise_campaigns.py view indexes model.units[material]; Core stock establishment accepts material IDs without that unit binding.'},
    'test_core_location_confirmation_remains_usable': {
        'id': 'IRGS-QA-002', 'severity': 'P1',
        'title': 'Canonical Core location records are incompatible with Rise location consumers',
        'expected': 'A supported, established location confirmation must leave local inventory and supported movement usable.',
        'reproduction': ['Create R00 at the commons.',
            'Creator records and delivers established evidence placing the founder at commons.',
            'Creator confirms founder.location=commons through confirm_character_field with authority and player instruction references.',
            'Inspect local inventory and submit walk_clearing.'],
        'boundary': 'Core confirm_character_field writes {value,evidence_id,at}; settlement_runtime.location and Rise view consume the whole record as a site string.'}}


class Mechanics(unittest.TestCase):
    """Black-box HTTP paths plus validation of this test's own persisted world."""
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='irgs-independent-qa-')
        self.store = SERVER.Store(self.tmp.name)
        self.opener = build_opener(ProxyHandler({}))
        self.counter = 0
        self.start_host()

    def start_host(self):
        self.host = SERVER.make_server(0, self.tmp.name)
        self.worker = threading.Thread(target=self.host.serve_forever, daemon=True)
        self.worker.start()
        self.base = f'http://127.0.0.1:{self.host.server_port}'
        self.token = None
        self.token = self.call('/api/campaigns')['token']

    def stop_host(self):
        self.host.shutdown(); self.host.server_close(); self.worker.join()

    def tearDown(self):
        self.stop_host(); self.tmp.cleanup()

    def call(self, path, data=None):
        headers = {'Content-Type': 'application/json'}
        if self.token: headers['X-IRGS-Token'] = self.token
        request = Request(self.base + path, headers=headers,
                          data=None if data is None else json.dumps(data).encode())
        with self.opener.open(request, timeout=10) as response:
            return json.load(response)

    def create(self, *, company='solo', permission='held'):
        choices = {'template_id': 'R00', 'founder_name': 'QA founder', 'household_name': 'QA household',
            'settlement_name': 'QA camp', 'region_name': 'QA fictional reach', 'date_label': 'QA Year 1',
            'company': company, 'permission': permission, 'supplies': 'basic'}
        review = self.call('/api/rise/preview', {'choices': choices})
        self.model = review['model']
        self.creation = {'name': 'Independent QA campaign', 'choices': choices,
            'review_digest': review['review_digest'], 'request_id': 'qa-create'}
        return self.call('/api/rise/create', self.creation)

    def body(self, record, action, request=None):
        self.counter += 1
        return {'id': record['id'], 'revision': record['revision'], 'actor': 'founder',
                'action': action, 'request_id': request or f'qa-action-{self.counter}'}

    def act(self, record, action, request=None):
        result = self.call('/api/rise/action', self.body(record, action, request))
        record['revision'] = result['revision']
        return result

    def event(self, record, operation, **parameters):
        result = self.call('/api/event', {'id': record['id'], 'revision': record['revision'], 'mode': 'creator',
            'op': operation, 'params': {'source_ref': 'independent-qa-synthetic-evidence', **parameters}})
        record['revision'] = result['revision']
        return result

    def raw(self, record):
        result = self.store.read(record['id'])
        CORE(state=result['state'])  # accepted states must retain Core invariants
        return result

    def view(self, record): return self.call('/api/playthrough/' + record['id'])
    def bytes(self, record): return self.store.path(record['id']).read_bytes()

    def camp(self, record):
        self.act(record, 'walk_clearing'); self.act(record, 'found')

    def assert_conserved(self, state):
        for material, opening in state['opening_stock'].items():
            physical = sum(account.get(material, 0) for account in state['stocks'].values())
            consumed = sum(f['quantity'] for f in state['material_flows'].values() if f['material'] == material)
            self.assertEqual(physical + consumed, opening, material)

    def test_founding_delegation_migration_and_material_continuity(self):
        r = self.create(company='sibling', permission='seek')
        original_people = set(self.raw(r)['state']['actors'])
        self.act(r, 'request_grant')
        self.assertEqual(self.raw(r)['state']['grants']['founding']['status'], 'offered')
        self.act(r, 'accept_grant'); self.camp(r); self.act(r, 'delegate')
        self.act(r, 'walk_commons')
        for _ in range(5):
            if self.raw(r)['state']['projects']['shelter']['status'] == 'complete': break
            self.act(r, 'wait_hour')
        self.assertEqual(self.raw(r)['state']['projects']['shelter']['status'], 'complete')
        self.assertIsNone(self.view(r)['settlement']['inventory'])
        self.act(r, 'invite')
        self.assertNotIn('oren-home', self.raw(r)['state']['settlements']['camp']['households'])
        self.act(r, 'arrange_departure')
        before = copy.deepcopy(self.raw(r)['state']['stocks'])
        self.act(r, 'walk_clearing'); self.act(r, 'wait_hour')
        state = self.raw(r)['state']
        self.assertEqual(state['migrations']['oren-move']['status'], 'arrived')
        self.assertEqual(set(state['actors']), original_people)
        self.assertEqual(state['stocks'], before)
        self.assertEqual(state['player_actor_ids'], ['founder'])
        self.assert_conserved(state)
        camp = self.view(r)['settlement']['camp']
        self.assertEqual(camp['residents'], 3)
        self.assertEqual(camp['shelter_places'], self.model['shelter_places'])
        self.assertEqual(camp['shelter_shortfall'], max(0, 3-self.model['shelter_places']))

    def test_concurrent_retry_has_one_commit_and_one_elapsed_span(self):
        r = self.create(); body = self.body(r, 'wait_hour', 'qa-concurrent-wait')
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: self.call('/api/rise/action', body), range(2)))
        self.assertEqual(results[0], results[1])
        state = self.raw(r)
        self.assertEqual(state['revision'], 1)
        self.assertEqual(state['state']['elapsed_time']['seconds'], results[0]['elapsed_time']['seconds'])
        saved = self.bytes(r)
        self.assertEqual(self.call('/api/rise/action', body), results[0])
        self.assertEqual(self.bytes(r), saved)

    def test_results_survive_host_restart_and_trash_restore(self):
        r = self.create(permission='seek')
        result = self.act(r, 'request_grant', 'qa-durable-offer'); saved = self.bytes(r)
        self.stop_host(); self.start_host()
        self.assertEqual(self.call(f'/api/action-result/{r["id"]}/qa-durable-offer?actor_id=founder'), result)
        self.assertEqual(self.bytes(r), saved)
        self.call('/api/delete', {'id': r['id'], 'revision': r['revision']})
        self.assertEqual(self.call('/api/rise/create', self.creation)['status'], 'trashed')
        self.assertEqual(self.call('/api/campaigns')['campaigns'], [])
        self.call('/api/restore', {'id': r['id'], 'revision': r['revision']})
        self.assertEqual(self.bytes(r), saved)

    def test_pause_resume_preserves_work_and_finishes_once(self):
        r = self.create(); self.camp(r); self.act(r, 'build'); self.act(r, 'wait_hour')
        partial = self.raw(r)['state']['projects']['shelter']['worked']
        self.assertGreater(partial, 0)
        self.assertLess(partial, self.model['shelter_seconds'])
        self.act(r, 'pause'); self.act(r, 'wait_hour'); self.act(r, 'wait_hour')
        self.assertEqual(self.raw(r)['state']['projects']['shelter']['worked'], partial)
        self.act(r, 'resume')
        for _ in range(5):
            if self.raw(r)['state']['projects']['shelter']['status'] == 'complete': break
            self.act(r, 'wait_hour')
        state = self.raw(r)['state']; self.assertEqual(state['projects']['shelter']['status'], 'complete')
        self.assertEqual(state['stocks']['founder-home']['timber'], 6-self.model['shelter_timber'])
        saved = self.bytes(r)
        with self.assertRaises(HTTPError): self.act(r, 'build', 'qa-second-physical-completion')
        self.assertEqual(self.bytes(r), saved); self.assert_conserved(state)

    def test_private_state_and_hidden_permission_do_not_select_player_options(self):
        r = self.create(company='sibling'); self.camp(r); self.act(r, 'delegate'); self.act(r, 'walk_commons')
        raw = self.raw(r); raw['state']['private_policy'] = 'QA-PRIVATE-POLICY-MARKER'
        raw['state']['stocks']['oren-home']['grain'] += 997
        raw['state']['opening_stock']['grain'] += 997
        self.store.write(raw)
        projected = self.view(r); text = json.dumps(projected)
        self.assertNotIn('QA-PRIVATE-POLICY-MARKER', text)
        self.assertNotIn('1001', text); self.assertNotIn('state', projected)
        self.assertIsNone(projected['settlement']['inventory'])
        self.assertFalse(any(p['worker'] == 'Rowan' for p in projected['settlement']['projects']))
        actions = projected['settlement']['actions']
        raw['state']['grants']['founding']['active'] = False; self.store.write(raw)
        self.assertEqual(self.view(r)['settlement']['actions'], actions)
        saved = self.bytes(r)
        body = self.body(r, 'wait_hour'); body['actor'] = 'oren'
        with self.assertRaises(HTTPError): self.call('/api/rise/action', body)
        self.assertEqual(self.bytes(r), saved)

    def test_freeform_is_retained_intent_with_no_automatic_elapsed_effect(self):
        r = self.create(); before = self.raw(r)['state']['elapsed_time']['seconds']
        result = self.call('/api/declaration', {'id': r['id'], 'revision': r['revision'], 'actor': 'founder',
            'request_id': 'qa-freeform', 'declaration': 'I consider trading for more supplies.'})
        r['revision'] = result['revision']; self.assertEqual(result['status'], 'declared_not_resolved')
        self.assertEqual(self.raw(r)['state']['elapsed_time']['seconds'], before)
        saved = self.bytes(r)
        with self.assertRaises(HTTPError): self.act(r, 'wait_hour')
        self.assertEqual(self.bytes(r), saved)
        result = self.call('/api/withdraw-declaration', {'id': r['id'], 'revision': r['revision'], 'actor': 'founder',
            'request_id': 'qa-withdraw', 'action_request_id': 'qa-freeform'})
        r['revision'] = result['revision']; self.act(r, 'inspect')
        self.assertEqual(self.raw(r)['state']['elapsed_time']['seconds'], before)

    def test_new_material_does_not_break_committed_campaign(self):
        r = self.create(); saved = self.bytes(r)
        try:
            self.event(r, 'establish_stock', location='founder-home', material='water', quantity=2,
                       inventory_evidence_ref='synthetic-measured-water')
        except HTTPError as error:
            self.assertIn(error.code, (400, 422))
            self.assertEqual(self.bytes(r), saved); self.view(r)
            return  # a missing unit/provider may explicitly hold this write
        self.raw(r)
        try: projected = self.view(r)
        except Exception as error:
            self.fail('IRGS-QA-001: the stock write committed and Core validates, but the playthrough request failed: ' + repr(error))
        water = next((q for q in projected['settlement']['inventory'] if q['material'] == 'water'), None)
        self.assertIsNotNone(water, 'Committed inspectable water disappeared from the known local inventory')
        self.assertEqual(water['quantity'], 2)
        self.act(r, 'inspect')

    def test_core_location_confirmation_remains_usable(self):
        r = self.create()
        self.event(r, 'record_evidence', evidence_id='qa-place', subject='founder', status='established',
                   assertion='QA founder is at the commons.')
        self.event(r, 'receive_evidence', evidence_id='qa-place', recipient='founder')
        self.event(r, 'confirm_character_field', subject='founder', evidence_id='qa-place', field='location',
                   value='commons', authority_ref='synthetic-location-observation', instruction_ref='explicit-qa-instruction')
        self.raw(r)
        self.assertIsNotNone(self.view(r)['settlement']['inventory'],
            'IRGS-QA-002: a canonical same-site location confirmation made the founder appear absent from their own stores')
        self.act(r, 'walk_clearing')
        self.assertEqual(self.view(r)['settlement']['location'], 'clearing')


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs); self.cases = []

    def record(self, test, status, error=None):
        row = {'test': test._testMethodName, 'status': status}
        if error: row['detail'] = self._exc_info_to_string(error, test)[-3000:]
        if test._testMethodName in FINDINGS: row['finding_id'] = FINDINGS[test._testMethodName]['id']
        self.cases.append(row)

    def addSuccess(self, test): super().addSuccess(test); self.record(test, 'passed')
    def addFailure(self, test, error): super().addFailure(test, error); self.record(test, 'failed', error)
    def addError(self, test, error): super().addError(test, error); self.record(test, 'error', error)
    def addSkip(self, test, reason): super().addSkip(test, reason); self.record(test, 'skipped')


def regression_check(name, command, source, logs):
    output = logs / (name + '.txt')
    env = dict(os.environ, IRGS_TEST_PYTHON=sys.executable, PYTHONDONTWRITEBYTECODE='1')
    started = time.monotonic()
    with output.open('w', encoding='utf-8') as stream:
        try:
            result = subprocess.run(command, cwd=source, env=env, stdout=stream,
                                    stderr=subprocess.STDOUT, timeout=420, check=False)
            code = result.returncode
        except subprocess.TimeoutExpired: code = 124
    body = output.read_text(encoding='utf-8', errors='replace')
    count = re.search(r'Ran (\d+) tests?', body)
    skips = re.search(r'OK \(skipped=(\d+)\)', body)
    row = {'name': name, 'status': 'passed' if code == 0 else 'failed', 'exit_code': code,
           'duration_seconds': round(time.monotonic()-started, 2), 'log': str(output)}
    if count:
        row['tests_run'] = int(count[1]); row['skipped'] = int(skips[1]) if skips else 0
        if row['tests_run'] == 0: row['status'] = 'not_executed'
    ui = re.search(r'(\d+) frontend checks passed', body)
    if ui: row['checks_passed'] = int(ui[1])
    if code: row['diagnostic_tail'] = body[-3000:]
    return row


def markdown(report):
    lines = ['# IRGS independent QA', '', f"Candidate: `{report['candidate_commit']}`",
             f"Result: **{report['status']}** · {report['finished_at_utc']}", '',
             'Engine Development owns mechanics fixes. QA runs isolated, synthetic campaigns and reports observed behavior.', '',
             '| Finding | Priority | Status | Result |', '| --- | --- | --- | --- |']
    for finding in report['findings']:
        lines.append(f"| {finding['id']} | {finding['severity']} | {finding['status']} | {finding['title']} |")
    lines += ['', f"Independent cases: {report['independent']['passed']} passed, {report['independent']['failed']} failed, {report['independent']['errors']} errors.", '',
              '| Check | Status |', '| --- | --- |']
    for check in report['regression_checks']: lines.append(f"| {check['name']} | {check['status']} |")
    for finding in report['findings']:
        lines += ['', '## ' + finding['id'], '', finding['title'], '', '**Expected:** ' + finding['expected'], '',
                  '**Boundary:** ' + finding['boundary'], '', 'Reproduce:', '']
        lines += [f'{i}. {step}' for i, step in enumerate(finding['reproduction'], 1)]
        if finding.get('observed'): lines += ['', 'Observed:', '', '```text', finding['observed'], '```']
    lines += ['', '## Scope', '', report['scope'], '',
              'This report is not full C2/T01–T37 certification. Skips and missing providers are not passes. No user campaign was loaded or migrated.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--independent-only', action='store_true')
    args = parser.parse_args()
    if sys.flags.optimize: raise SystemExit('Do not use -O; Core requires assertions')
    source = args.source_root.resolve(strict=True); output = args.output.resolve()
    if output.is_relative_to(source): raise SystemExit('Keep test artifacts outside the candidate source')
    output.parent.mkdir(parents=True, exist_ok=True)
    logs = output.parent / 'logs'; logs.mkdir(exist_ok=True)
    checks = []
    if not args.independent_only:
        # The external historical-save test is replaced by an explicit policy
        # skip without opening it. The ordinary test cases remain unmodified.
        runtime_command = ("import sys,unittest;from pathlib import Path;sys.path.insert(0,'tools');"
            "from coverage_capture import _flatten,_PolicySkip,EXTERNAL_FIXTURE_TEST;"
            "suite=unittest.defaultTestLoader.discover('IRGS_3_3/runtime');"
            "cases=[_PolicySkip(t.id()) if t.id()==EXTERNAL_FIXTURE_TEST else t for t in _flatten(suite)];"
            "result=unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(cases));"
            "sys.exit(0 if result.wasSuccessful() else 1)")
        commands = [('source-integrity', [sys.executable, '-B', 'tools/verify_development.py']),
                    ('evidence-freshness', [sys.executable, '-B', 'tools/build_operation_register.py', '--check', 'engine/qualification/operation_register.json']),
                    ('runtime', [sys.executable, '-B', '-c', runtime_command]),
                    ('web', [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'IRGS_Web/tests', '-v']),
                    ('interface', ['node', 'IRGS_Web/tests/test_gameplay_ui.js']),
                    ('tooling', [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tools/tests', '-p', 'test_*.py', '-v'])]
        for name, command in commands:
            print('Checking ' + name, flush=True)
            checks.append(regression_check(name, command, source, logs))
    global SERVER, CORE
    sys.path[:0] = [str(source/'IRGS_Web'), str(source/'IRGS_3_3/runtime')]
    import server as SERVER
    from core_world import CoreWorld as CORE
    text = io.StringIO()
    with (logs/'independent-http.txt').open('w', encoding='utf-8') as http_log, contextlib.redirect_stderr(http_log):
        result = unittest.TextTestRunner(stream=text, verbosity=2, resultclass=RecordedResult).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(Mechanics))
    (logs/'independent-tests.txt').write_text(text.getvalue(), encoding='utf-8')
    failures = {case['test']: case for case in result.cases if case['status'] in ('failed', 'error')}
    statuses = {case['test']: case['status'] for case in result.cases}
    findings = [{**record, 'status': ('open' if statuses.get(test)=='failed' else
                 'not_reproduced' if statuses.get(test)=='passed' else 'inconclusive'),
                 **({'observed': failures[test]['detail']} if test in failures else {})}
                for test, record in FINDINGS.items()]
    report = {'schema_version': 1, 'candidate_commit': args.commit,
        'finished_at_utc': datetime.now(timezone.utc).isoformat(),
        'status': 'passed' if result.wasSuccessful() and all(c['status']=='passed' for c in checks) else 'needs_fixes',
        'scope': ('Independent HTTP checks only. ' if args.independent_only else 'Current Core/App regression suites plus independent HTTP checks. ') +
                 'Contracts: R00 founding, shared Core interoperability, material continuity, replay, restart, privacy and retained intent.',
        'candidate_source_root': str(source), 'qa_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'regression_checks': checks, 'independent': {'tests_run': result.testsRun,
            'passed': sum(c['status']=='passed' for c in result.cases), 'failed': len(result.failures),
            'errors': len(result.errors), 'skipped': len(result.skipped), 'cases': result.cases},
        'findings': findings, 'user_saves_opened': False, 'mechanics_modified_by_qa': False}
    output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    output.with_suffix('.md').write_text(markdown(report), encoding='utf-8')
    print(json.dumps({'status': report['status'], 'candidate': args.commit,
        'independent_passed': report['independent']['passed'], 'independent_failed': report['independent']['failed'],
        'report': str(output)}), flush=True)
    return 0 if report['status']=='passed' else 1


if __name__ == '__main__': raise SystemExit(main())
