"""Opt-in proposal capability and durable technical inference accounting.

This module owns no campaign facts. Only a trusted host builds requests and
supplies route/policy approvals. A transport receives ActorRequest.model_input,
never the world or its private binding. Reservations are conservative lifetime
ceilings, not reported bills. There are no automatic retries or fallbacks.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from contextlib import contextmanager
import json
import math
from pathlib import Path
import queue
import sqlite3
import threading
import time
from typing import Callable, Protocol

from irgs_reference import canon, digest

SCHEMA_VERSION = 'solo-proposal-1'
PROMPT_VERSION = 'solo-local-1'
TASK = 'propose_local_action'
DIRECTOR = 'Local'
LOCAL_OPERATION = 'execute_player_scene_action'
RISE_OPERATION = 'execute_settlement_action'
TRANSPORT_ERRORS = frozenset({'provider_error', 'provider_denied', 'rate_limited',
    'provider_unavailable', 'transport_timeout', 'transport_error', 'malformed_output',
    'provider_refusal', 'incomplete_output', 'output_limit', 'credential_unavailable',
    'provider_disabled', 'route_unqualified', 'limit_exceeded', 'invalid_request'})


class CapabilityUnavailable(Exception):
    """A bounded public code; private exception text must never be returned."""
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def require(condition, code='invalid_request'):
    if not condition:
        raise CapabilityUnavailable(code)


def nonempty(value, limit=256):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= limit


@dataclass(frozen=True)
class WorldScope:
    campaign_id: str
    branch_id: str
    restore_id: str
    state_digest: str


@dataclass(frozen=True)
class ActorRequest:
    request_id: str
    scope: WorldScope
    actor_id: str
    intention: str
    context_json: str
    allowed_actions: tuple[str, ...]
    source_refs: tuple[str, ...]
    allowed_routes: tuple[str, ...]
    classification: str
    policy_ref: str
    config_version: str
    deadline: float
    max_output_tokens: int = 512
    max_output_bytes: int = 16384
    prompt_version: str = PROMPT_VERSION
    schema_version: str = SCHEMA_VERSION
    task: str = TASK
    director: str = DIRECTOR
    operation_id: str = LOCAL_OPERATION

    def validate(self):
        require(all(nonempty(x) for x in (self.request_id, self.actor_id,
            self.scope.campaign_id, self.scope.branch_id, self.scope.restore_id,
            self.scope.state_digest, self.classification, self.policy_ref, self.config_version)))
        require(nonempty(self.intention, 4096))
        require(self.task == TASK and self.director == DIRECTOR and
                self.schema_version == SCHEMA_VERSION and self.prompt_version == PROMPT_VERSION)
        require(self.operation_id in (LOCAL_OPERATION, RISE_OPERATION), 'unsupported_action')
        require(type(self.deadline) in (int, float) and math.isfinite(self.deadline))
        require(type(self.max_output_tokens) is int and 1 <= self.max_output_tokens <= 4096)
        require(type(self.max_output_bytes) is int and 256 <= self.max_output_bytes <= 65536)
        for values in (self.allowed_actions, self.source_refs, self.allowed_routes):
            require(isinstance(values, tuple) and bool(values) and len(values) <= 128)
            require(all(nonempty(x) for x in values) and len(set(values)) == len(values))
        require(isinstance(self.context_json, str) and len(self.context_json.encode()) <= 65536)
        require(isinstance(json.loads(self.context_json), dict))

    def model_input(self):
        """The complete whitelist passed to a model, without private scope hashes."""
        return {'actor_id': self.actor_id, 'intention': self.intention,
                'context': json.loads(self.context_json),
                'allowed_actions': list(self.allowed_actions),
                'source_refs': list(self.source_refs)}

    def fingerprint(self):
        data = asdict(self)
        if self.operation_id == LOCAL_OPERATION:
            # Preserve the first published API's implicit local-operation binding.
            data.pop('operation_id')
        return digest(data)

    @classmethod
    def from_json(cls, value):
        data = json.loads(value)
        data['scope'] = WorldScope(**data['scope'])
        for key in ('allowed_actions', 'source_refs', 'allowed_routes'):
            data[key] = tuple(data[key])
        request = cls(**data)
        request.validate()
        return request


@dataclass(frozen=True)
class Route:
    route_id: str
    developer: str
    gateway: str
    host: str
    model: str
    model_version: str
    config_version: str
    policy_ref: str
    price_revision: str
    reservation_units: int
    classifications: tuple[str, ...] = ('synthetic-approved',)
    workloads: tuple[str, ...] = (TASK,)
    max_input_bytes: int = 65536
    max_output_tokens: int = 512
    enabled: bool = False
    approval_ref: str = ''
    lifecycle: str = 'candidate'
    tested_capabilities: tuple[str, ...] = ()
    adapter_version: str = 'offline-1'
    operations: tuple[str, ...] = (LOCAL_OPERATION,)

    def identity(self):
        return {key: getattr(self, key) for key in
                ('developer', 'gateway', 'host', 'model', 'model_version')}


class SpecialistRegistry:
    """The initial implementation of the planned registry; no extra Directors."""
    def __init__(self, routes=()):
        routes = tuple(routes)
        require(len({r.route_id for r in routes}) == len(routes), 'invalid_configuration')
        self.routes = {r.route_id: r for r in routes}

    def eligible(self, request, route_id):
        require(route_id in request.allowed_routes, 'route_denied')
        route = self.routes.get(route_id)
        require(route is not None and route.enabled, 'provider_disabled')
        require(route.lifecycle == 'qualified' and nonempty(route.approval_ref) and
                SCHEMA_VERSION in route.tested_capabilities, 'route_unqualified')
        require(all(nonempty(value) for value in route.identity().values()), 'route_unqualified')
        require(nonempty(route.adapter_version), 'route_unqualified')
        require(route.config_version == request.config_version and
                route.policy_ref == request.policy_ref and nonempty(route.price_revision), 'policy_denied')
        require(request.classification in route.classifications and
                request.task in route.workloads and request.operation_id in route.operations, 'policy_denied')
        require(type(route.reservation_units) is int and route.reservation_units > 0,
                'budget_unconfigured')
        require(len(canon(request.model_input()).encode()) <= route.max_input_bytes and
                request.max_output_tokens <= route.max_output_tokens, 'limit_exceeded')
        return route


@dataclass(frozen=True)
class TransportReply:
    body: str = ''
    reported_identity_json: str = '{}'
    usage_json: str = '{}'
    provider_request_id: str | None = None
    error: str | None = None
    provider_response_id: str | None = None


class ProposalTransport(Protocol):
    def __call__(self, model_input: dict, route: Route, *,
                 timeout: float, max_output_tokens: int) -> TransportReply: ...


@dataclass(frozen=True)
class ProposedAction:
    request_id: str
    intention: str
    action_id: str
    source_refs: tuple[str, ...]
    proposal_digest: str


@dataclass(frozen=True)
class ValidatedResult:
    request_id: str
    status: str
    code: str | None = None
    proposal: ProposedAction | None = None

    @classmethod
    def from_json(cls, value):
        data = json.loads(value)
        if data['proposal'] is not None:
            data['proposal']['source_refs'] = tuple(data['proposal']['source_refs'])
            data['proposal'] = ProposedAction(**data['proposal'])
        return cls(**data)


def _present(result):
    # Cancellation retains the original proposal privately for lost-ack receipt
    # recovery. An unavailable broker response must not present that draft.
    if result.status != 'proposal_ready' and result.proposal is not None:
        return ValidatedResult(result.request_id, result.status, result.code)
    return result


def validate_proposal(request, reply, route):
    require(reply.error is None, reply.error if reply.error in TRANSPORT_ERRORS else 'provider_error')
    require(json.loads(reply.reported_identity_json) == route.identity(), 'route_mismatch')
    require(json.loads(reply.usage_json).get('output_tokens', 0) <= request.max_output_tokens,
            'output_limit')
    require(isinstance(reply.body, str) and len(reply.body.encode()) <= request.max_output_bytes,
            'output_limit')
    try:
        # Duplicate keys are ambiguous even if an ordinary JSON parser accepts them.
        def unique(pairs):
            value = {}
            for key, item in pairs:
                require(key not in value, 'malformed_output')
                value[key] = item
            return value
        data = json.loads(reply.body, object_pairs_hook=unique)
        require(isinstance(data, dict) and set(data) == {'intention', 'action_id', 'source_refs'},
                'malformed_output')
        require(data['intention'] == request.intention, 'intent_changed')
        require(data['action_id'] in request.allowed_actions, 'unsupported_action')
        refs = data['source_refs']
        require(isinstance(refs, list) and bool(refs) and all(isinstance(x, str) for x in refs),
                'unknown_source')
        require(len(set(refs)) == len(refs) and set(refs) <= set(request.source_refs), 'unknown_source')
        return ProposedAction(request.request_id, request.intention, data['action_id'], tuple(refs),
                              digest({'request': request.fingerprint(), 'proposal': data}))
    except (ValueError, TypeError, KeyError):
        raise CapabilityUnavailable('malformed_output') from None


class AttemptLedger:
    """Local technical database, outside campaign saves. Never stores credentials.

    A processing attempt surviving restart is deliberately left in doubt. It
    consumes its ceiling and concurrency slot until an operator reconciles it;
    reopening the database cannot authorize another call for that request ID.
    """
    def __init__(self, path, *, budget_units, max_inflight=1):
        require(type(budget_units) is int and budget_units >= 0 and
                type(max_inflight) is int and max_inflight > 0, 'invalid_configuration')
        self.path = str(Path(path).resolve())
        with self.connection() as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('CREATE TABLE IF NOT EXISTS limits (id INTEGER PRIMARY KEY, budget INTEGER, inflight INTEGER)')
            db.execute('CREATE TABLE IF NOT EXISTS cancellations (id TEXT PRIMARY KEY)')
            db.execute('CREATE TABLE IF NOT EXISTS attempts (id TEXT PRIMARY KEY, fingerprint TEXT NOT NULL,'
                ' request TEXT NOT NULL, route TEXT NOT NULL, reserved INTEGER NOT NULL,'
                ' status TEXT NOT NULL, finished INTEGER NOT NULL DEFAULT 0, result TEXT,'
                ' requested_identity TEXT NOT NULL, reported_identity TEXT, usage TEXT,'
                ' provider_request_id TEXT, started REAL NOT NULL, completed REAL, accepted TEXT,'
                ' dependencies TEXT, route_config TEXT, provider_response_id TEXT, dispatch_started REAL,'
                " transport_state TEXT NOT NULL DEFAULT 'unknown')")
            # Compatible addition to the published offline technical ledger.
            columns = {row[1] for row in db.execute('PRAGMA table_info(attempts)')}
            for name in ('route_config', 'provider_response_id', 'dispatch_started'):
                if name not in columns:
                    db.execute('ALTER TABLE attempts ADD COLUMN ' + name +
                               (' REAL' if name == 'dispatch_started' else ' TEXT'))
            if 'transport_state' not in columns:
                # A legacy attempt may already have incurred a charge. Missing
                # admission telemetry never establishes that it was not sent.
                db.execute("ALTER TABLE attempts ADD COLUMN transport_state TEXT NOT NULL DEFAULT 'unknown'")
            db.execute('INSERT OR IGNORE INTO limits VALUES (1, ?, ?)', (budget_units, max_inflight))
            require(db.execute('SELECT budget,inflight FROM limits WHERE id=1').fetchone() ==
                    (budget_units, max_inflight), 'budget_configuration_changed')

    @contextmanager
    def connection(self):
        db = sqlite3.connect(self.path, timeout=10)
        try:
            db.execute('PRAGMA synchronous=FULL')
            with db:
                yield db
        finally:
            db.close()

    def lookup(self, request_id):
        with self.connection() as db:
            db.row_factory = sqlite3.Row
            row = db.execute('SELECT * FROM attempts WHERE id=?', (request_id,)).fetchone()
            return dict(row) if row else None

    def result(self, request_id):
        row = self.lookup(request_id)
        if row is None:
            if self.is_cancelled(request_id):
                return ValidatedResult(request_id, 'unavailable', 'cancelled')
            return ValidatedResult(request_id, 'unavailable', 'unknown_request')
        if row['result']:
            return ValidatedResult.from_json(row['result'])
        return ValidatedResult(request_id, 'unavailable', 'in_progress_or_in_doubt')

    def is_cancelled(self, request_id):
        with self.connection() as db:
            return db.execute('SELECT 1 FROM cancellations WHERE id=?', (request_id,)).fetchone() is not None

    def claim(self, request, route, now):
        with self.connection() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT fingerprint,route FROM attempts WHERE id=?', (request.request_id,)).fetchone()
            if row:
                require(row[0] == request.fingerprint(), 'request_identity_conflict')
                require(row[1] == route.route_id, 'route_denied')
                return False
            require(db.execute('SELECT 1 FROM cancellations WHERE id=?',
                               (request.request_id,)).fetchone() is None, 'cancelled')
            budget, inflight = db.execute('SELECT budget,inflight FROM limits WHERE id=1').fetchone()
            reserved, active = db.execute('SELECT COALESCE(SUM(reserved),0),'
                ' COALESCE(SUM(CASE WHEN finished=0 THEN 1 ELSE 0 END),0) FROM attempts').fetchone()
            require(reserved + route.reservation_units <= budget, 'budget_exhausted')
            require(active < inflight, 'concurrency_exhausted')
            db.execute('INSERT INTO attempts (id,fingerprint,request,route,reserved,status,'
                'requested_identity,started,route_config,transport_state) VALUES (?,?,?,?,?,?,?,?,?,?)',
                (request.request_id, request.fingerprint(), canon(asdict(request)), route.route_id,
                 route.reservation_units, 'processing', canon(route.identity()), now, canon(asdict(route)),
                 'not_started'))
            return True

    def finish(self, result, now):
        with self.connection() as db:
            db.execute('UPDATE attempts SET status=?, result=?, completed=? WHERE id=? AND status=?',
                (result.status, canon(asdict(result)), now, result.request_id, 'processing'))
        return self.result(result.request_id)

    def cancel(self, request_id):
        require(nonempty(request_id))
        with self.connection() as db:
            db.execute('BEGIN IMMEDIATE')
            old = db.execute('SELECT result,status,accepted FROM attempts WHERE id=?', (request_id,)).fetchone()
            if old is None or (old[2] is None and old[1] in ('processing', 'proposal_ready')):
                # A host may cancel while its dispatcher is still preparing the
                # request. Keep that decision across registration and restart.
                db.execute('INSERT OR IGNORE INTO cancellations VALUES (?)', (request_id,))
            proposal = ValidatedResult.from_json(old[0]).proposal if old and old[0] else None
            result = ValidatedResult(request_id, 'unavailable', 'cancelled', proposal)
            db.execute('UPDATE attempts SET status=?,result=? WHERE id=? AND accepted IS NULL'
                ' AND status IN (?,?)', ('unavailable', canon(asdict(result)), request_id,
                                        'processing', 'proposal_ready'))
        return self.result(request_id)

    def begin_transport(self, request_id, deadline, clock):
        """Serialize dispatch admission against cancellation. Never admit twice."""
        with self.connection() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT status,transport_state FROM attempts WHERE id=?',
                             (request_id,)).fetchone()
            if row is None or row[1] != 'not_started':
                return False
            if row[0] != 'processing':
                db.execute('UPDATE attempts SET finished=1 WHERE id=?', (request_id,))
                return False
            now = clock()
            if now >= deadline:
                result = ValidatedResult(request_id, 'unavailable', 'deadline_exceeded')
                db.execute('UPDATE attempts SET finished=1,status=?,result=?,completed=? WHERE id=?',
                           (result.status, canon(asdict(result)), now, request_id))
                return False
            db.execute("UPDATE attempts SET dispatch_started=?,transport_state='admitted' WHERE id=?",
                       (now, request_id))
            return True

    def finish_without_transport(self, result, now):
        """Release the in-flight slot only when this attempt never entered transport.

        Retain its conservative reservation. This does not assert zero usage or
        refund a possible charge, and cannot alter a dispatched attempt.
        """
        with self.connection() as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('UPDATE attempts SET status=?,result=?,completed=? WHERE id=?'
                " AND transport_state='not_started' AND status=?",
                (result.status, canon(asdict(result)), now, result.request_id, 'processing'))
            db.execute("UPDATE attempts SET finished=1 WHERE id=? AND transport_state='not_started'",
                       (result.request_id,))

    def record_transport(self, request_id, reply):
        # This may run after cancellation/deadline. It records accounting only;
        # a late reply never creates/replaces an accepted or available proposal.
        with self.connection() as db:
            db.execute('UPDATE attempts SET finished=1,reported_identity=?,usage=?,provider_request_id=?,provider_response_id=?'
                ' WHERE id=?', (reply.reported_identity_json, reply.usage_json,
                               reply.provider_request_id, reply.provider_response_id, request_id))


class CapabilityBroker:
    def __init__(self, registry, ledger, *, enabled=False, clock=time.time, scope_reader=None):
        self.registry, self.ledger, self.enabled, self.clock = registry, ledger, enabled, clock
        self.scope_reader = scope_reader

    def _fresh(self, request):
        require(callable(self.scope_reader), 'scope_unconfigured')
        try:
            scope = self.scope_reader(request)
        except Exception:
            raise CapabilityUnavailable('scope_unavailable') from None
        require(scope == request.scope, 'stale_scope_or_state')

    def dispatch(self, request: ActorRequest, route_id: str,
                 transport: ProposalTransport, *, cancelled: Callable[[], bool] = lambda: False):
        claimed = False
        try:
            request.validate()
            # Lookup precedes route/config revalidation: no retry after a crash,
            # even if configuration changed or this broker is now disabled.
            row = self.ledger.lookup(request.request_id)
            if row:
                require(row['fingerprint'] == request.fingerprint(), 'request_identity_conflict')
                require(row['route'] == route_id, 'route_denied')
                if self.ledger.result(request.request_id).status == 'proposal_ready':
                    if cancelled():
                        return _present(self.ledger.cancel(request.request_id))
                    require(self.clock() < request.deadline, 'deadline_exceeded')
                    require(self.enabled, 'provider_disabled')
                    current_route = self.registry.eligible(request, route_id)
                    if row['route_config'] is not None:
                        require(row['route_config'] == canon(asdict(current_route)), 'route_configuration_changed')
                    else:
                        require(row['requested_identity'] == canon(current_route.identity()),
                                'route_configuration_changed')
                    self._fresh(request)
                return _present(self.ledger.result(request.request_id))
            require(not self.ledger.is_cancelled(request.request_id), 'cancelled')
            require(self.enabled, 'provider_disabled')
            if cancelled():
                return _present(self.ledger.cancel(request.request_id))
            require(self.clock() < request.deadline, 'deadline_exceeded')
            require(request.deadline - self.clock() <= 300, 'limit_exceeded')
            self._fresh(request)
            route = self.registry.eligible(request, route_id)
            if not self.ledger.claim(request, route, self.clock()):
                return _present(self.ledger.result(request.request_id))
            claimed = True
            replies = queue.Queue(maxsize=1)

            def run():
                started = False
                try:
                    if cancelled():
                        self.ledger.cancel(request.request_id)
                    require(self.registry.eligible(request, route_id) == route, 'route_configuration_changed')
                    self._fresh(request)
                    started = self.ledger.begin_transport(request.request_id, request.deadline, self.clock)
                    if not started:
                        replies.put(TransportReply(error='transport_error'))
                        return
                    reply = transport(request.model_input(), route,
                        timeout=max(0.001, request.deadline - self.clock()),
                        max_output_tokens=request.max_output_tokens)
                    require(isinstance(reply, TransportReply), 'malformed_output')
                    # Bound technical reports and accept only numeric token reports.
                    identity = json.loads(reply.reported_identity_json)
                    usage = json.loads(reply.usage_json)
                    require(isinstance(identity, dict) and len(canon(identity)) <= 2048 and
                            set(identity) <= set(route.identity()), 'malformed_output')
                    require(all(isinstance(v, str) and len(v) <= 256 for v in identity.values()),
                            'malformed_output')
                    require(isinstance(usage, dict) and set(usage) <= {'input_tokens', 'output_tokens',
                        'cached_input_tokens', 'reasoning_tokens'} and
                        all(type(v) is int and v >= 0 for v in usage.values()), 'malformed_output')
                    require(reply.provider_request_id is None or nonempty(reply.provider_request_id),
                            'malformed_output')
                    require(reply.provider_response_id is None or nonempty(reply.provider_response_id),
                            'malformed_output')
                except CapabilityUnavailable as error:
                    safe_code = error.code if not started and error.code in {
                        'scope_unconfigured', 'scope_unavailable', 'stale_scope_or_state', 'provider_disabled',
                        'route_unqualified', 'policy_denied', 'limit_exceeded', 'route_configuration_changed',
                        'route_denied', 'budget_unconfigured'} else 'transport_error'
                    reply = TransportReply(error=safe_code)
                except Exception:
                    reply = TransportReply(error='transport_error')
                try:
                    if started:
                        self.ledger.record_transport(request.request_id, reply)
                    else:
                        self.ledger.finish_without_transport(
                            ValidatedResult(request.request_id, 'unavailable', reply.error), self.clock())
                finally:
                    replies.put(reply)

            threading.Thread(target=run, daemon=True).start()
            while True:
                if cancelled():
                    return _present(self.ledger.cancel(request.request_id))
                current = self.ledger.result(request.request_id)
                if current.code != 'in_progress_or_in_doubt':
                    return _present(current)
                remaining = request.deadline - self.clock()
                if remaining <= 0:
                    return _present(self.ledger.finish(ValidatedResult(request.request_id, 'unavailable',
                                                             'deadline_exceeded'), self.clock()))
                try:
                    reply = replies.get(timeout=min(0.01, remaining))
                    current = self.ledger.result(request.request_id)
                    if current.code != 'in_progress_or_in_doubt':
                        return _present(current)
                    require(not cancelled(), 'cancelled')
                    require(self.clock() < request.deadline, 'deadline_exceeded')
                    require(self.registry.eligible(request, route_id) == route, 'route_configuration_changed')
                    self._fresh(request)
                    proposal = validate_proposal(request, reply, route)
                    return _present(self.ledger.finish(ValidatedResult(request.request_id, 'proposal_ready',
                                                             proposal=proposal), self.clock()))
                except queue.Empty:
                    continue
        except CapabilityUnavailable as error:
            result = ValidatedResult(request.request_id, 'unavailable', error.code)
        except (ValueError, TypeError, KeyError):
            result = ValidatedResult(request.request_id, 'unavailable', 'malformed_output')
        row = self.ledger.lookup(request.request_id)
        if claimed and row and row['fingerprint'] == request.fingerprint():
            if row['status'] == 'processing':
                return _present(self.ledger.finish(result, self.clock()))
            return _present(self.ledger.result(request.request_id))
        return result
