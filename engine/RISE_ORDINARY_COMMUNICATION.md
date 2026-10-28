# Rise ordinary-start communication — A4-ENG-01

27 October 2026; 3.4.3 Pre-Alpha. This bounded increment advances A4-G02/G05
and DEV-14–16/18/20. Neither Alpha gate is qualified. The existing non-Rise
`quay-contact-v1` path and fictional R00 are distinct ordinary campaign contexts;
communication here establishes no autonomous NPC decision or sustained-play claim.

## Review, initialization and projection

R00's ordinary `settlement_setup.preview(choices)` discloses two fictional
introductions in the existing `neighbors` text shown by the App, together with
local speech limits. It also returns `communication_setup`, version
`irgs-rise-local-introductions-1`, containing the source, channel, exact initial
testimony, supported command and unresolved elapsed status. The complete review
is covered by the existing review digest. Creation requires that digest and the
unchanged explicit choices; a changed introduction invalidates a prior review.

A newly initialized R00 receives `setup:local-introduction:elin` and
`setup:local-introduction:oren`, with founder as subject/recipient, the named
speaker as originator, status `testimony`, causal coordinate zero and source
`authored-fictional:greywater-reach:local-introductions:v1`. These are reviewed
fictional initial circumstances, not new autonomous choices. The initializer
selects `commons-local` as a co-located channel for founder, Elin and Oren.
The shared `irgs-communication-capabilities-1` actor view shows only participants
identified by received attribution, with `speak` as an attemptable command.
It does not expose hidden channel members, another household's private stock,
or availability decisions based on hidden current location. Other company
members are not silently attributed or added as communication participants.

The initializer introduces no stock, mandate, new grant, offer or consent. It
selects no Rise stock-offer profile; speech alone cannot negotiate, transfer goods
or make an NPC reply. Continuing/legacy saves are never reseeded on read, and
the original `rise-foundation-1` material and time rules remain in force.
The changed review digest correctly rejects a previously unconfirmed review;
existing committed campaigns retain their actual state and original receipts.

## Execution and host handoff

Use the existing [communication contract](COMMUNICATION_CAPABILITY_API.md):
read the actor view, prepare the exact words to a received participant, then
execute only on explicit boolean acceptance with host save/result CAS. Core
rechecks control, participant existence and co-location. Speech records testimony
received by the actual participants; it does not resolve elapsed work or advance
the civil calendar. A founder who walks away retains received knowledge but a
subsequent local speech attempt rejects atomically. A prepared request is not
an effect. Retrying a committed request after restart returns its original
result; restored branches need a fresh host identity.

[The actual HTTP qualification](../tools/qualify_rise_communication_http.py)
uses real App preview, ordinary create, creation retry, playthrough, prepare,
execute, exact result retry and fresh Store reload against explicitly selected
Engine/App/Catalog roots. It uses a temporary store/reference config and blocks
both provider dispatch and transport. Run from Engine:

```bash
IRGS_ENGINE_ROOT=/workspace/IRGS-Engine/IRGS_3_3 \
IRGS_CATALOG_ROOT=/workspace/IRGS-Catalog/IRGS_Catalog \
PYTHONPATH=/workspace/IRGS-APP-WEB/IRGS_Web:/workspace/IRGS-Engine/IRGS_3_3/runtime \
python -B tools/qualify_rise_communication_http.py
```

Five Engine cases additionally cover scoped attribution/privacy, no automatic
offer, exact accepted testimony/reload/replay, movement rejection, changed
review and legacy saves. Existing synthetic communication fixture tests still
exercise an intentionally unreceived channel roster after removing only the
fixture's initial receipts; the privacy assertions are retained.

See [exact executed results](RISE_ORDINARY_COMMUNICATION_VALIDATION.json).
The current App has the existing bridge and was selected at its checked-out
source with explicit Engine/Catalog overrides; its committed gitlinks are not
changed. Catalog's original and new independent evaluation identities remain
pinned to their own selected code and have not been repinned or requalified.
Catalog should publish a separately selected independent consumer that reviews
these initial receipts, tests both ordinary contexts and verifies privacy, stale
review, original-result recovery and actual co-location rejection.

A4-ENG-01 remains in progress: ordinary offer selection/authority and independent
Catalog qualification remain open, as do NPC decisions and continuing play.
A4-ENG-02 selected native travel and early A4-ENG-03 supported-intent DTOs remain
next. Coordinator review of an exact compatible set and all Alpha gates is separate.
