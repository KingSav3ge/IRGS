# Direct OpenAI proposal adapter — reviewed 2026-10-23

IRGS 3.4.0 development delivery. Adapter ID: `openai-responses-local-1`.
This is an opt-in transport candidate with offline HTTP evidence, not a measured
model winner, an account entitlement or authorization for a paid call.

## Checked official contract

- [Responses create reference](https://developers.openai.com/api/reference/resources/responses/methods/create):
  `POST https://api.openai.com/v1/responses`, explicit output-token ceiling,
  structured text configuration, completion status, output messages and usage.
  The adapter sends one nonstreaming request and never retries it.
- [Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs):
  Responses uses `text.format` with `type: json_schema`, `strict: true`, required
  fields and `additionalProperties: false`. Refusal and incomplete output need
  separate handling. IRGS still performs its own deterministic validation;
  structured JSON does not establish semantic intent fidelity.
- [GPT-5.4 mini model page](https://developers.openai.com/api/docs/models/gpt-5.4-mini):
  the checked snapshot is `gpt-5.4-mini-2026-03-17`, with Responses, structured
  output and `reasoning.effort: none` support. This first adapter accepts only that
  exact API ID/version. An alias, new snapshot or replacement requires reviewed
  configuration and regression, never silent substitution. The IRGS output limit
  is deliberately smaller than the model limit.
- [API overview](https://developers.openai.com/api/reference/overview):
  bearer authentication stays on the server. The HTTP `x-request-id` and JSON
  response `id` are separate trace fields. Neither is guessed after a timeout.
- [Error codes](https://developers.openai.com/api/docs/guides/error-codes):
  permission failures, exhausted/rate-limited access and server failures need
  explicit handling. IRGS returns bounded codes, retaining conservative accounting;
  provider error/refusal bodies are never diagnostics or narration.
- [Data controls](https://developers.openai.com/api/docs/guides/your-data):
  `store: false` is not a guarantee of zero retention or a processing geography.
  Approval for retention/training/geography and this exact workload remains an
  operator policy decision. Fixture rights metadata does not select a provider.

These pages were checked before implementation. Account-available models, live
responses, billing, regional processing and model quality were **not** checked
through a credentialed call. Prices are not automatically imported from research.

## Adapter behavior and configuration

`OpenAIProposalTransport()` defaults to disabled and reads no credential while
disabled. Its server-only default credential reader obtains `OPENAI_API_KEY` at
dispatch. Tests inject an unmistakably synthetic credential and HTTP sender;
they do not inspect a configured live key or open a provider connection.

The host must separately enable the broker, qualify the route and enable the
adapter. A direct route uses developer `OpenAI`, gateway `direct`, host
`api.openai.com`, the checked snapshot for both `model` and `model_version`, and
`adapter_version: openai-responses-local-1`. Configure allowed operations,
classification, workload, approval/policy/config and price revision plus a finite
worst-case reservation. The reservation must cover the complete bounded wire
input (including prompt/schema), permitted output and applicable fees. It is not
a verified dollar estimate or automatic account-billing control.

The request contains only the trusted actor input and fixed instructions/schema.
It sets `store: false`, no conversation/previous response, no tools, no streaming,
no truncation, `service_tier: default`, `reasoning.effort: none` and an explicit
output ceiling. The wire body is capped at 64 KiB or the route's smaller limit;
the response is read with a 128 KiB cap. Deadline is enforced by the broker as
well as the HTTP timeout. TLS/proxy trust retains platform defaults. Redirects
are refused; the credential cannot follow an alternate endpoint.

Only the response's model/version are provider-reported identity fields. Developer,
gateway and host identify this fixed direct HTTPS connection, not independently
attested downstream geography. The ledger preserves requested and reported model
identity, route/config/adapter/price versions, HTTP request and response IDs,
known input/output/cached/reasoning token reports and unknown actual charges.
Model mismatch rejects the proposal without erasing the reported identity.

HTTP 401/403, 429, 408/504 and server failures have bounded unavailable codes;
other failures remain explicit. Error bodies are not read. Incomplete, refusal,
malformed, ambiguous/duplicate-key, oversized and unexpected tool output cannot
produce a proposal. Missing/invalid usage never becomes zero cost. Failed,
timed-out, cancelled and late attempts retain their reservation and never trigger
another paid request. Full route metadata is added compatibly to the first offline
ledger; earlier unknown metadata stays null, without resetting attempts or budget.

## Evidence and limits

`test_openai_proposals.py` has 14 synthetic HTTP cases, including actual request
construction and bounded reader/error/redirect behavior, success through the real
local Core acceptance handler, denial/rate limit/timeout, refusal/incomplete output,
reported model mismatch, missing/invalid usage, malformed/tool output, credential
absence/header injection and technical-ledger upgrade. All network responses and
credentials in these tests are fake. Generic broker tests additionally cover
concurrent dispatch, stale state/restore/session closure, late completion and
exhausted reservations. See [the delivery report](SOLO_PROVIDER_VALIDATION.json).

Live smoke remains pending an approved server credential, account-available exact
model, permitted input/workload, current reviewed route/price ceiling and a finite
explicit budget. No such permission is inferred from this work order. App session
integration, exact joined qualification, semantic/character review and model
benchmarks remain separate work.
