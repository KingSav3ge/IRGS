"""Synthetic HTTP contract checks, not live inference or quality measurements."""
from dataclasses import replace
import io
import json
from pathlib import Path
import sqlite3
import tempfile
import time
import unittest
from unittest.mock import Mock, patch
import urllib.error
import urllib.request

from irgs_reference import canon
from openai_proposals import (ADAPTER_VERSION, CHECKED_MODEL, ENDPOINT, HTTPReply,
    MAX_RESPONSE_BYTES, OpenAIProposalTransport, _http_post, _NoRedirect)
from solo_actions import accept_proposal, prepare_request
from solo_provider import AttemptLedger, CapabilityBroker, SpecialistRegistry, WorldScope
from test_scene_actions import fixture
from test_solo_provider import AtomicTestHost, route


def direct_route(**changes):
    selected = route(developer='OpenAI', gateway='direct', host='api.openai.com',
                     model=CHECKED_MODEL, model_version=CHECKED_MODEL, adapter_version=ADAPTER_VERSION)
    return replace(selected, **changes)


def response(proposal, **changes):
    data = {'id': 'resp_synthetic', 'model': CHECKED_MODEL, 'status': 'completed', 'error': None,
        'usage': {'input_tokens': 50, 'output_tokens': 30,
                  'input_tokens_details': {'cached_tokens': 8},
                  'output_tokens_details': {'reasoning_tokens': 0}},
        'output': [{'type': 'message', 'role': 'assistant', 'status': 'completed',
                    'content': [{'type': 'output_text', 'text': canon(proposal)}]}]}
    data.update(changes)
    return HTTPReply(200, canon(data).encode(), 'req_synthetic')


class OpenAIProposalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.world = fixture()
        self.host = AtomicTestHost(self.temp.name, self.world)
        self.request = prepare_request(self.world, request_id='http-1', actor_id='pc',
            intention='I take the passage.', branch_id='branch-1', restore_id='restore-1',
            allowed_routes=('offline',), classification='synthetic-approved',
            policy_ref='synthetic-transfer-approved-v1', config_version='config-v1', deadline=time.time()+20)
        self.proposal = {'intention': self.request.intention, 'action_id': 'enter-passage',
                         'source_refs': [self.request.source_refs[0]]}
        self.ledger = AttemptLedger(Path(self.temp.name) / 'http.sqlite', budget_units=100, max_inflight=2)
        self.registry = SpecialistRegistry([direct_route()])
        self.broker = CapabilityBroker(self.registry, self.ledger, enabled=True,
            scope_reader=lambda request: WorldScope(self.world.s['campaign_id'], 'branch-1', 'restore-1',
                                                    self.world.checksum()))

    def dispatch(self, reply=None, *, exception=None, key='SYNTHETIC-SERVER-SECRET', request=None):
        post = Mock(return_value=reply or response(self.proposal), side_effect=exception)
        transport = OpenAIProposalTransport(enabled=True, http_post=post, credential_reader=lambda: key)
        result = self.broker.dispatch(request or self.request, 'offline', transport)
        return result, post

    def test_success_is_strict_stateless_and_only_core_acceptance_changes_world(self):
        before = self.world.save()
        result, post = self.dispatch()
        self.assertEqual(result.status, 'proposal_ready')
        self.assertEqual(self.world.save(), before)
        self.assertEqual(post.call_count, 1)
        sent = post.call_args.args[0]
        self.assertEqual(sent.full_url, ENDPOINT)
        self.assertEqual(sent.get_method(), 'POST')
        self.assertEqual(sent.get_header('Authorization'), 'Bearer SYNTHETIC-SERVER-SECRET')
        payload = json.loads(sent.data)
        self.assertEqual(payload['model'], CHECKED_MODEL)
        self.assertIs(payload['store'], False)
        self.assertIs(payload['stream'], False)
        self.assertEqual(payload['tools'], [])
        self.assertEqual(payload['tool_choice'], 'none')
        self.assertEqual(payload['service_tier'], 'default')
        self.assertEqual(payload['reasoning'], {'effort': 'none'})
        self.assertEqual(payload['max_output_tokens'], 512)
        self.assertEqual(json.loads(payload['input'][0]['content'][0]['text']), self.request.model_input())
        self.assertNotIn('SYNTHETIC-SERVER-SECRET', sent.data.decode())
        schema = payload['text']['format']['schema']
        self.assertFalse(schema['additionalProperties'])
        self.assertEqual(schema['properties']['intention']['enum'], [self.request.intention])
        public = accept_proposal(self.world, self.ledger, request_id=self.request.request_id,
            proposal_digest=result.proposal.proposal_digest, actor_id='pc', intention=self.request.intention,
            branch_id='branch-1', restore_id='restore-1', explicitly_accepted=True,
            persist=self.host.persist, clock=time.time)
        self.assertEqual(public['outcome']['summary'], 'Completed enter-passage.')
        self.assertEqual(self.world.s['elapsed_time']['seconds'], 20)
        row = self.ledger.lookup(self.request.request_id)
        self.assertEqual(row['provider_request_id'], 'req_synthetic')
        self.assertEqual(row['provider_response_id'], 'resp_synthetic')
        self.assertEqual(json.loads(row['usage']), {'input_tokens': 50, 'output_tokens': 30,
                          'cached_input_tokens': 8, 'reasoning_tokens': 0})
        config = json.loads(row['route_config'])
        self.assertEqual(config['adapter_version'], ADAPTER_VERSION)
        self.assertEqual(config['price_revision'], 'synthetic-ceiling-v1')
        self.assertNotIn('SYNTHETIC-SERVER-SECRET', canon(row))

    def test_adapter_default_disabled_reads_no_key_and_sends_nothing(self):
        key, post = Mock(), Mock()
        reply = OpenAIProposalTransport(http_post=post, credential_reader=key)(
            self.request.model_input(), direct_route(), timeout=2, max_output_tokens=512)
        self.assertEqual(reply.error, 'provider_disabled')
        key.assert_not_called()
        post.assert_not_called()

    def test_missing_credential_is_unavailable_without_http(self):
        result, post = self.dispatch(key=None)
        self.assertEqual(result.code, 'credential_unavailable')
        post.assert_not_called()
        self.assertEqual(self.ledger.lookup('http-1')['reserved'], 10)

    def test_key_cannot_inject_headers(self):
        result, post = self.dispatch(key='fake\r\nX-Other: injected')
        self.assertEqual(result.code, 'credential_unavailable')
        post.assert_not_called()

    def test_unreviewed_model_host_gateway_version_or_adapter_never_reads_key(self):
        for change in ({'model': 'gpt-5.4-mini'}, {'host': 'unapproved.example'},
                       {'gateway': 'alternate-gateway'}, {'model_version': 'unknown'},
                       {'adapter_version': 'unreviewed-2'}):
            with self.subTest(change=change):
                key, post = Mock(), Mock()
                reply = OpenAIProposalTransport(enabled=True, http_post=post, credential_reader=key)(
                    self.request.model_input(), direct_route(**change), timeout=2, max_output_tokens=512)
                self.assertEqual(reply.error, 'route_unqualified')
                key.assert_not_called()
                post.assert_not_called()

    def test_http_denial_rate_limit_error_timeout_and_redirect_never_retry(self):
        statuses = {400: 'provider_error', 401: 'provider_denied', 403: 'provider_denied',
            404: 'provider_error', 429: 'rate_limited', 500: 'provider_unavailable',
            503: 'provider_unavailable', 504: 'transport_timeout', 307: 'provider_error'}
        before = self.world.save()
        for status, code in statuses.items():
            with self.subTest(status=status):
                request = replace(self.request, request_id='http-' + str(status))
                result, post = self.dispatch(HTTPReply(status, b'SECRET ERROR BODY'), request=request)
                self.assertEqual(result.code, code)
                self.assertEqual(post.call_count, 1)
                self.assertEqual(self.world.save(), before)
                row = self.ledger.lookup(request.request_id)
                self.assertEqual(row['reserved'], 10)
                self.assertEqual(json.loads(row['usage']), {})
                self.assertNotIn('SECRET ERROR BODY', canon(row))

    def test_network_timeout_and_exception_remain_unknown_and_do_not_redispatch(self):
        for index, error in enumerate((TimeoutError('private endpoint'),
                urllib.error.URLError(TimeoutError('private endpoint')), OSError('private endpoint'))):
            with self.subTest(error=type(error).__name__):
                request = replace(self.request, request_id='failure-' + str(index))
                result, post = self.dispatch(exception=error, request=request)
                self.assertEqual(result.code, 'transport_error' if index == 2 else 'transport_timeout')
                row = self.ledger.lookup(request.request_id)
                self.assertEqual(json.loads(row['usage']), {})
                self.assertEqual(row['reserved'], 10)
                self.assertNotIn('private endpoint', canon(row))
                self.assertEqual(self.broker.dispatch(request, 'offline', lambda *a, **k: self.fail()), result)
                self.assertEqual(post.call_count, 1)

    def test_incomplete_refusal_or_failed_response_never_becomes_a_proposal(self):
        cases = [
            ('incomplete_output', response(self.proposal, status='incomplete')),
            ('provider_error', response(self.proposal, status='failed', error={'message': 'private message'})),
            ('provider_refusal', response(self.proposal, output=[{'type': 'message', 'role': 'assistant',
                'status': 'completed', 'content': [{'type': 'refusal', 'refusal': 'private refusal prose'}]}]))]
        for index, (code, reply) in enumerate(cases):
            with self.subTest(code=code):
                result, post = self.dispatch(reply, request=replace(self.request, request_id='status-'+str(index)))
                self.assertEqual(result.code, code)
                self.assertIsNone(result.proposal)
                self.assertEqual(post.call_count, 1)

    def test_changed_actual_model_is_recorded_and_rejected(self):
        result, post = self.dispatch(response(self.proposal, model='different-model-1'))
        self.assertEqual(result.code, 'route_mismatch')
        row = self.ledger.lookup(self.request.request_id)
        self.assertEqual(json.loads(row['reported_identity'])['model'], 'different-model-1')
        self.assertEqual(json.loads(row['requested_identity'])['model'], CHECKED_MODEL)

    def test_absent_usage_stays_unknown(self):
        result, _ = self.dispatch(response(self.proposal, usage=None))
        self.assertEqual(result.status, 'proposal_ready')
        self.assertEqual(json.loads(self.ledger.lookup('http-1')['usage']), {})
        self.assertEqual(self.ledger.lookup('http-1')['reserved'], 10)

    def test_invalid_or_excessive_usage_does_not_qualify(self):
        usages = [({'input_tokens': -1}, 'malformed_output'),
                  ({'output_tokens': True}, 'malformed_output'),
                  ({'output_tokens': 1000}, 'output_limit'),
                  ({'input_tokens': 1, 'input_tokens_details': {'cached_tokens': 2}}, 'malformed_output')]
        for index, (usage, code) in enumerate(usages):
            with self.subTest(usage=usage):
                result, _ = self.dispatch(response(self.proposal, usage=usage),
                    request=replace(self.request, request_id='usage-' + str(index)))
                self.assertEqual(result.code, code)

    def test_malformed_oversize_duplicate_and_arbitrary_tool_output_are_rejected(self):
        replies = [(HTTPReply(200, b'not-json'), 'malformed_output'),
            (HTTPReply(200, b'x' * (MAX_RESPONSE_BYTES+1)), 'output_limit'),
            (HTTPReply(200, b'{"model":"x","model":"y"}'), 'malformed_output'),
            (response(self.proposal, output=[{'type': 'function_call', 'name': 'apply_arbitrary_event'}]),
             'malformed_output'),
            (response(self.proposal, output=[]), 'malformed_output')]
        for index, (reply, code) in enumerate(replies):
            with self.subTest(index=index):
                result, _ = self.dispatch(reply, request=replace(self.request, request_id='bad-' + str(index)))
                self.assertEqual(result.code, code)
                self.assertIsNone(result.proposal)

    def test_real_http_function_reads_bounded_success_and_no_error_body(self):
        request = urllib.request.Request(ENDPOINT, data=b'{}', method='POST')
        response_mock = Mock(status=200, headers={'x-request-id': 'req_test'})
        response_mock.read.return_value = b'{}'
        context = Mock()
        context.__enter__ = Mock(return_value=response_mock)
        context.__exit__ = Mock(return_value=False)
        opener = Mock()
        opener.open.return_value = context
        with patch('openai_proposals.urllib.request.build_opener', return_value=opener):
            self.assertEqual(_http_post(request, timeout=2), HTTPReply(200, b'{}', 'req_test'))
        response_mock.read.assert_called_once_with(MAX_RESPONSE_BYTES+1)
        opener.open.assert_called_once_with(request, timeout=2)
        error_stream = Mock(wraps=io.BytesIO(b'SECRET ERROR BODY'))
        opener.open.side_effect = urllib.error.HTTPError(ENDPOINT, 401, 'denied', {}, error_stream)
        with patch('openai_proposals.urllib.request.build_opener', return_value=opener):
            self.assertEqual(_http_post(request, timeout=2).status, 401)
        error_stream.read.assert_not_called()
        error_stream.close.assert_called_once()
        self.assertIsNone(_NoRedirect().redirect_request(request, None, 307, '', {}, 'https://elsewhere'))

    def test_offline_ledger_schema_upgrades_without_resetting_budget_or_attempt(self):
        path = Path(self.temp.name) / 'old.sqlite'
        with sqlite3.connect(path) as db:
            db.execute('CREATE TABLE limits (id INTEGER PRIMARY KEY, budget INTEGER, inflight INTEGER)')
            db.execute('INSERT INTO limits VALUES (1, 20, 1)')
            db.execute('CREATE TABLE attempts (id TEXT PRIMARY KEY, fingerprint TEXT NOT NULL,'
                'request TEXT NOT NULL, route TEXT NOT NULL, reserved INTEGER NOT NULL,status TEXT NOT NULL,'
                'finished INTEGER NOT NULL DEFAULT 0,result TEXT,requested_identity TEXT NOT NULL,'
                'reported_identity TEXT,usage TEXT,provider_request_id TEXT,started REAL NOT NULL,'
                'completed REAL,accepted TEXT,dependencies TEXT)')
            db.execute('INSERT INTO attempts (id,fingerprint,request,route,reserved,status,requested_identity,started)'
                       ' VALUES (?,?,?,?,?,?,?,?)', ('previous', 'hash', '{}', 'old', 10, 'processing', '{}', 1))
        reopened = AttemptLedger(path, budget_units=20, max_inflight=1)
        row = reopened.lookup('previous')
        self.assertEqual(row['reserved'], 10)
        self.assertEqual(row['status'], 'processing')
        self.assertIsNone(row['route_config'])
        self.assertIsNone(row['provider_response_id'])


if __name__ == '__main__':
    unittest.main()
