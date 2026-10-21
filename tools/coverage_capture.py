"""Collect named synthetic runtime executions without replacing historical reports.

This records observed examples and explicit refusals, never all-branch proof.
The caller chooses where to save the returned summary, evidence and test log.
"""
from __future__ import annotations

import copy
import io
from pathlib import Path
import sys
import threading
import unittest


EXTERNAL_FIXTURE_TEST = 'test_suite.SuiteTests.test_legacy_ast_save_load_does_not_rewrite'


class _PolicySkip(unittest.TestCase):
    def __init__(self, identity):
        super().__init__('runTest')
        self.identity = identity

    def id(self):
        return self.identity

    def runTest(self):
        self.skipTest('Coverage capture uses synthetic fixtures only; external historical saves are not opened')


def _flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from _flatten(item)
        else:
            yield item


def capture_suite(runtime_dir: Path):
    """Return ``(summary, records, log_text)`` from current synthetic tests.

    Records contain path sets and test identities, not state, event parameters,
    raw private errors or manually declared footprints. Only passing tests make
    evidence usable. Counts describe captured executions/probes, not unique
    world commits. A replay returning False creates no fresh execution evidence.
    All patched methods and imported observe aliases are restored in finally.
    """
    runtime_dir = Path(runtime_dir).resolve(strict=True)
    saved_path = list(sys.path)
    sys.path.insert(0, str(runtime_dir))
    import r9_runtime as runtime
    from core_world import CoreWorld
    from irgs_reference import World, digest
    from r7_frontier import R7World
    from r9_adapters import ReceiverWorld

    classes = tuple(dict.fromkeys((World, R7World, ReceiverWorld, CoreWorld)))
    originals = {cls: cls.__dict__['apply'] for cls in classes}
    original_observe = runtime.observe
    supported = set(runtime.SUPPORTED)
    local = threading.local()
    lock = threading.RLock()
    active_test = [None]
    rows = {}
    excluded_unknown = [0]
    aliases = []
    outcomes = {}

    def context():
        return active_test[0] or 'outside_test'

    def probing():
        frame = sys._getframe(1)
        while frame:
            if (frame.f_code.co_name == 'observe'
                    and frame.f_globals.get('__name__') in ('r9_runtime', 'r8_dependencies')):
                return True
            frame = frame.f_back
        return False

    def backend_for(state):
        # Current R9 selection policy. Successful evidence uses the certificate's
        # actual backend; this helper is only for refused/failed detached probes.
        if state.get('profile') in ('IRGS-CORE-3.3', 'AST-CORE-3.3'):
            return CoreWorld
        if 'r9_engine_bindings' in state:
            return ReceiverWorld
        if 'econ3' in state:
            return R7World
        return World

    def add(operation, state, actual_backend, status, *, certificate=None,
            reads=(), writes=(), validation_reads=(), attempted_writes=(), reason=None,
            capture_origin='actual_apply', actual_committed=False):
        certificate = certificate or {}
        backend = certificate.get('backend', backend_for(state).__name__)
        profile = certificate.get('profile', state.get('profile', 'legacy_research_fixture'))
        key = (operation, backend, actual_backend, profile, context(), status, capture_origin, actual_committed)
        with lock:
            row = rows.setdefault(key, {'operation': operation, 'backend': backend,
                'actual_backend': actual_backend, 'profile': profile, 'test_id': context(),
                'capture_origin': capture_origin, 'actual_committed': actual_committed,
                'status': status, 'executions': 0, 'reads': set(), 'writes': set(),
                'validation_reads': set(), 'attempted_writes': set(), 'reason_codes': set()})
            row['executions'] += 1
            for name, values in (('reads', certificate.get('reads', reads)),
                    ('writes', certificate.get('writes', writes)),
                    ('validation_reads', certificate.get('validation_reads', validation_reads)),
                    ('attempted_writes', attempted_writes)):
                row[name].update(tuple(path) for path in values)
            if reason:
                row['reason_codes'].add(reason)

    def rejected_probe(state, event, actual_backend, *, expected_failure, reason,
                       capture_origin='actual_apply', actual_committed=False):
        """Try the selected R9 backend detached; scratch writes are not effects."""
        trace = runtime.Trace()
        cls = backend_for(state)
        plain_worker = None
        plain_error = None
        plain_constructed = False
        try:
            plain_worker = cls(state=state)
            plain_constructed = True
            plain_worker.apply(event['id'], event['at'], event['op'], **copy.deepcopy(event['params']))
        except Exception as error:
            plain_error = error
        plain_unchanged = plain_constructed and digest(plain_worker.s) == digest(state)
        traced_error = None
        trace_installed = False
        worker = None
        try:
            worker = cls(state=state)
            worker.s = runtime.TracedDict(worker.s, trace)
            trace_installed = True
            worker.apply(event['id'], event['at'], event['op'], **copy.deepcopy(event['params']))
        except Exception as error:
            traced_error = error
        probe_unchanged = trace_installed and digest(runtime.plain(worker.s)) == digest(state)
        matching_rejection = (plain_error is not None and traced_error is not None
                              and type(plain_error) is type(traced_error)
                              and plain_error.args == traced_error.args)
        status = ('failed_attempt' if expected_failure and matching_rejection
                  and plain_constructed and trace_installed and plain_unchanged and probe_unchanged
                  else 'observation_refused')
        if not plain_constructed or not trace_installed:
            reason = 'backend_state_not_instrumentable'
        elif plain_error is None:
            reason = 'plain_backend_did_not_reject'
        elif not plain_unchanged or traced_error is not None and not probe_unchanged:
            reason = 'probe_atomicity_violation'
        elif traced_error is None:
            reason = 'instrumented_backend_did_not_reject'
        elif not matching_rejection:
            reason = 'instrumented_rejection_mismatch'
        add(event['op'], state, actual_backend, status,
            reads=runtime.effect_paths(trace.reads), writes=(),
            validation_reads=sorted(trace.validation_reads),
            attempted_writes=runtime.effect_paths(trace.writes),
            reason=reason if status == 'observation_refused' else None,
            capture_origin=capture_origin, actual_committed=actual_committed)

    def capture_actual(state, event, actual_backend, *, post_state=None, failed=False):
        local.busy = True
        try:
            if failed:
                if digest(state) != digest(post_state):
                    add(event['op'], state, actual_backend, 'observation_refused',
                        writes=runtime.effect_paths(runtime.changed(state, post_state)),
                        reason='atomicity_violation')
                    return
                rejected_probe(state, event, actual_backend, expected_failure=True,
                               reason='failed_execution_not_reproduced')
                return
            try:
                certificate = original_observe(state, event)
            except Exception as error:
                rejected_probe(state, event, actual_backend, expected_failure=False,
                               reason='observer_' + type(error).__name__, actual_committed=True)
                return
            if certificate.get('post_state') != digest(post_state):
                add(event['op'], state, actual_backend, 'observation_refused',
                    reads=certificate.get('reads', ()),
                    validation_reads=certificate.get('validation_reads', ()),
                    attempted_writes=certificate.get('writes', ()), reason='post_state_mismatch',
                    actual_committed=True)
                return
            add(event['op'], state, actual_backend, 'success', certificate=certificate, actual_committed=True)
        finally:
            local.busy = False

    def wrap_apply(original):
        def audited(self, eid, at, op, **params):
            top = not getattr(local, 'depth', 0) and not getattr(local, 'busy', False) and not probing()
            if top and op not in supported:
                with lock:
                    excluded_unknown[0] += 1
                top = False
            before = copy.deepcopy(self.s) if top else None
            local.depth = getattr(local, 'depth', 0) + 1
            event = {'id': eid, 'at': at, 'op': op, 'params': copy.deepcopy(params)} if top else None
            try:
                result = original(self, eid, at, op, **params)
            except Exception:
                if top:
                    capture_actual(before, event, type(self).__name__, post_state=self.s, failed=True)
                raise
            finally:
                local.depth -= 1
            if top and result:
                capture_actual(before, event, type(self).__name__, post_state=self.s)
            return result
        return audited

    def audited_observe(state, event):
        if getattr(local, 'busy', False) or getattr(local, 'depth', 0):
            return original_observe(state, event)
        if event.get('op') not in supported:
            with lock:
                excluded_unknown[0] += 1
            return original_observe(state, event)
        local.busy = True
        actual_backend = backend_for(state).__name__
        before_digest = digest(state)
        try:
            try:
                certificate = original_observe(state, event)
            except Exception as error:
                if digest(state) != before_digest:
                    add(event['op'], state, actual_backend, 'observation_refused',
                        reason='observer_mutated_source', capture_origin='direct_observe')
                else:
                    rejected_probe(state, event, actual_backend, expected_failure=True,
                                   reason='observer_' + type(error).__name__, capture_origin='direct_observe')
                raise
            if digest(state) != before_digest or certificate.get('snapshot') != before_digest:
                add(event['op'], state, actual_backend, 'observation_refused',
                    reason='observer_snapshot_mismatch', capture_origin='direct_observe')
            else:
                add(event['op'], state, actual_backend, 'success', certificate=certificate,
                    capture_origin='direct_observe')
            return certificate
        finally:
            local.busy = False

    def patch_aliases():
        for module in list(sys.modules.values()):
            filename = getattr(module, '__file__', None)
            if not filename:
                continue
            try:
                relevant = Path(filename).resolve().is_relative_to(runtime_dir)
            except (OSError, ValueError):
                continue
            if relevant:
                for name, value in list(vars(module).items()):
                    if value is original_observe:
                        aliases.append((module, name, value))
                        setattr(module, name, audited_observe)

    class Results(unittest.TextTestResult):
        def startTest(self, test):
            active_test[0] = test.id()
            outcomes[test.id()] = 'running'
            super().startTest(test)

        def stopTest(self, test):
            super().stopTest(test)
            active_test[0] = None

        def addSuccess(self, test):
            outcomes[test.id()] = 'passed'
            super().addSuccess(test)

        def addFailure(self, test, error):
            outcomes[test.id()] = 'failed'
            super().addFailure(test, error)

        def addError(self, test, error):
            outcomes[test.id()] = 'error'
            super().addError(test, error)

        def addSkip(self, test, reason):
            outcomes[test.id()] = 'skipped'
            super().addSkip(test, reason)

        def addSubTest(self, test, subtest, error):
            if error is not None:
                outcomes[test.id()] = 'failed' if issubclass(error[0], test.failureException) else 'error'
            super().addSubTest(test, subtest, error)

        def addExpectedFailure(self, test, error):
            outcomes[test.id()] = 'expected_failure'
            super().addExpectedFailure(test, error)

        def addUnexpectedSuccess(self, test):
            outcomes[test.id()] = 'unexpected_success'
            super().addUnexpectedSuccess(test)

    log = io.StringIO()
    try:
        for cls, original in originals.items():
            cls.apply = wrap_apply(original)
        patch_aliases()
        # Discover after patching, so newly imported direct observe aliases point
        # at audited_observe. Patch once more for modules cached from prior runs.
        discovered = unittest.TestLoader().discover(str(runtime_dir), pattern='test_*.py')
        patch_aliases()
        suite = unittest.TestSuite(_PolicySkip(test.id()) if test.id() == EXTERNAL_FIXTURE_TEST else test
                                   for test in _flatten(discovered))
        result = unittest.TextTestRunner(stream=log, verbosity=1, resultclass=Results).run(suite)
    finally:
        for cls, original in originals.items():
            cls.apply = original
        # Newly imported modules may have retained the temporary wrapper.
        for module in list(sys.modules.values()):
            filename = getattr(module, '__file__', None)
            if not filename:
                continue
            try:
                relevant = Path(filename).resolve().is_relative_to(runtime_dir)
            except (OSError, ValueError):
                continue
            if relevant:
                for name, value in list(vars(module).items()):
                    if value is audited_observe:
                        setattr(module, name, original_observe)
        for module, name, value in aliases:
            setattr(module, name, value)
        runtime.observe = original_observe
        sys.path[:] = saved_path

    records = []
    for key in sorted(rows):
        row = rows[key]
        emitted = {name: value for name, value in row.items()
                   if name not in ('reads', 'writes', 'validation_reads', 'attempted_writes', 'reason_codes')}
        for name in ('reads', 'writes', 'validation_reads', 'attempted_writes'):
            emitted[name] = sorted(row[name])
        emitted['usable'] = outcomes.get(row['test_id']) == 'passed'
        if row['reason_codes']:
            emitted['reason_code'] = '|'.join(sorted(row['reason_codes']))
        records.append(emitted)
    summary = {'tests_run': result.testsRun, 'passed': sum(value == 'passed' for value in outcomes.values()),
        'skipped': len(result.skipped), 'failures': len(result.failures), 'errors': len(result.errors),
        'tests_successful': result.wasSuccessful(), 'test_outcomes': dict(sorted(outcomes.items())),
        'capture_records': len(records), 'captured_executions': sum(row['executions'] for row in records),
        'capture_origin_counts': {origin: sum(row['executions'] for row in records
                                             if row['capture_origin'] == origin)
                                 for origin in ('actual_apply', 'direct_observe')},
        'actual_committed_apply_count': sum(row['executions'] for row in records if row['actual_committed']),
        'excluded_unknown_operations': excluded_unknown[0],
        'external_fixture_policy_skips': [EXTERNAL_FIXTURE_TEST],
        'scope': 'Current synthetic test executions and detached probes; no all-branch certification',
        'limits': ['Repeated probes are observations, not unique committed world events.',
                   'Failed-attempt writes are scratch attempts, never committed effects.',
                   'Paths are unioned per operation/backend/profile/test/status, not branch-complete.',
                   'Rejected probes mirror the current R9 backend selection policy.']}
    return summary, records, log.getvalue()
