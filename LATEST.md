# IRGS independent QA

Candidate: `bf6cf48b1c4f76589fb5854811f072e4bb9fda30`
Result: **needs_fixes** · 2026-10-22T14:11:26.805870+00:00

Engine Development owns mechanics fixes. QA runs isolated, synthetic campaigns and reports observed behavior.

| Finding | Priority | Status | Result |
| --- | --- | --- | --- |
| IRGS-QA-001 | P1 | open | Accepted Core material establishment breaks Rise playthrough views |
| IRGS-QA-002 | P1 | open | Canonical Core location records are incompatible with Rise location consumers |

Independent cases: 6 passed, 2 failed, 0 errors.

| Check | Status |
| --- | --- |
| source-integrity | passed |
| evidence-freshness | passed |
| runtime | passed |
| web | passed |
| interface | passed |
| tooling | passed |

## IRGS-QA-001

Accepted Core material establishment breaks Rise playthrough views

**Expected:** Reject an unsupported material atomically, or retain a readable campaign with explicit unknown unit support.

**Boundary:** IRGS_Web/rise_campaigns.py view indexes model.units[material]; Core stock establishment accepts material IDs without that unit binding.

Reproduce:

1. Create a reviewed R00 Rise campaign.
2. Creator POST /api/event: establish_stock(location=founder-home, material=water, quantity=2, inventory_evidence_ref=synthetic-measured-water).
3. Observe the successful save and valid CoreWorld state.
4. GET /api/playthrough/<id> with the normal session token.

Observed:

```text
Traceback (most recent call last):
  File "/workspace/irgs-cloud/qa/qa_irgs.py", line 234, in test_new_material_does_not_break_committed_campaign
    try: projected = self.view(r)
                     ^^^^^^^^^^^^
  File "/workspace/irgs-cloud/qa/qa_irgs.py", line 110, in view
    def view(self, record): return self.call('/api/playthrough/' + record['id'])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/irgs-cloud/qa/qa_irgs.py", line 76, in call
    with self.opener.open(request, timeout=10) as response:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/urllib/request.py", line 515, in open
    response = self._open(req, data)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/urllib/request.py", line 532, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/urllib/request.py", line 492, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/urllib/request.py", line 1373, in http_open
    return self.do_open(http.client.HTTPConnection, req)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/urllib/request.py", line 1348, in do_open
    r = h.getresponse()
        ^^^^^^^^^^^^^^^
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/http/client.py", line 1478, in getresponse
    response.begin()
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/http/client.py", line 343, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/http/client.py", line 312, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/workspace/irgs-cloud/qa/qa_irgs.py", line 236, in test_new_material_does_not_break_committed_campaign
    self.fail('IRGS-QA-001: the stock write committed and Core validates, but the playthrough request failed: ' + repr(error))
AssertionError: IRGS-QA-001: the stock write committed and Core validates, but the playthrough request failed: RemoteDisconnected('Remote end closed connection without response')

```

## IRGS-QA-002

Canonical Core location records are incompatible with Rise location consumers

**Expected:** A supported, established location confirmation must leave local inventory and supported movement usable.

**Boundary:** Core confirm_character_field writes {value,evidence_id,at}; settlement_runtime.location and Rise view consume the whole record as a site string.

Reproduce:

1. Create R00 at the commons.
2. Creator records and delivers established evidence placing the founder at commons.
3. Creator confirms founder.location=commons through confirm_character_field with authority and player instruction references.
4. Inspect local inventory and submit walk_clearing.

Observed:

```text
Traceback (most recent call last):
  File "/workspace/irgs-cloud/qa/qa_irgs.py", line 250, in test_core_location_confirmation_remains_usable
    self.assertIsNotNone(self.view(r)['settlement']['inventory'],
AssertionError: unexpectedly None : IRGS-QA-002: a canonical same-site location confirmation made the founder appear absent from their own stores

```

## Scope

Current Core/App regression suites plus independent HTTP checks. Contracts: R00 founding, shared Core interoperability, material continuity, replay, restart, privacy and retained intent.

This report is not full C2/T01–T37 certification. Skips and missing providers are not passes. No user campaign was loaded or migrated.
