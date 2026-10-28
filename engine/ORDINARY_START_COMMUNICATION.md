# Ordinary-start communication — A4-ENG-01 increment

27 October 2026; IRGS **3.4.3 Pre-Alpha**. This increment advances A4-G02/G05
and DEV-14–16, 18 and 20. It does not qualify those gates or close the broader
DEV/C2 criteria. The supported scope is one non-Rise ordinary opening; another
campaign context, NPC responses, negotiation and sustained play remain open.

## Reviewed creation and information

The 1415 new-human individual Solo starting options now include an explicitly
fictional `quay-contact-v1` alongside the unchanged `quay-delivery-v1`. Its
review describes a fictional quay worker, local speech, and the absence of an
established response, consent, possessions or authority. Its content digest is
included in the normal selection digest. The caller must review the options
and submit the exact digest with the explicit opening ID; stale reviews fail.
The historical snapshot and original opening pack are unchanged.

During new-world initialization only, the selected variant registers the
fictional contact through Core, establishes their initial quay location, records
and receives their introductory testimony, and selects the `quay-local`
co-located channel. The contact's identity is `FICTIONAL-QUAY-CONTACT`; the
source is `authored-solo-opening:quay-contact-v1`. The receipt identifies the
contact and its source, not their disposition or future decisions. The channel
contains only the selected player and fictional contact. Existing/default
starts, historical Henry and continuing worlds do not receive this setup.

Use the existing `irgs-communication-capabilities-1` contract, unchanged:

1. Get normal starting options, select the new opening, preview, and create with
   the reviewed selection digest and a stable creation request identity.
2. Get `shared_runtime.actor_view(...)["communications"]` or the existing App
   playthrough `communication_control`. The participant derives from actually
   received attribution. The view is read-only and says `attemptable`, not
   assured present or willing. Review retains fictional/source labels.
3. Prepare `speak` with the received participant, `quay-local`, exact player
   words, branch and restore identity. Preparation commits no game effect.
   Execute only after explicit boolean acceptance and through host atomic CAS.
4. Core rechecks actual actor control, recipient existence and co-location.
   Successful words become testimony received by both participants. They are
   not truth, consent, a completed offer, a response or an NPC decision. Speech
   has no selected elapsed duration; other clocks and resources do not change.
5. Retrieve the original result on duplicate delivery or after restart. A
   different payload under the same request ID rejects; a restore rotates host
   identity. Moving away keeps received knowledge but a speech attempt fails
   its actual co-location check without an effect or hidden-location disclosure.

The [communication API](COMMUNICATION_CAPABILITY_API.md) specifies DTO fields,
public failure status and existing CAS/recovery rules. This increment does not
select the Rise stock-offer profile, add remote speech, infer a mandate, introduce
an autonomous speaker or rewrite a previously created campaign. No provider is
needed for these actions or local response rendering.

## Reproducible qualification

Four new Engine tests in `runtime/test_ordinary_communication.py` cover normal
reviewed creation, legacy selection separation, actual accepted speech,
unauthorized acceptance, evidence/time/stock boundaries, retry/reload, stale
selection and co-location rejection. The temporary-host App HTTP executable
[qualify_ordinary_communication_http.py](../tools/qualify_ordinary_communication_http.py)
uses starting-options/preview/create and communication prepare/execute against
real selected sources. It verifies creation replay without reseeding, exact speech
result replay, fresh-store reload and zero provider calls:

```bash
IRGS_ENGINE_ROOT=/workspace/IRGS-Engine/IRGS_3_3 \
IRGS_CATALOG_ROOT=/workspace/IRGS-Catalog/IRGS_Catalog \
PYTHONPATH=/workspace/IRGS-APP-WEB/IRGS_Web:/workspace/IRGS-Engine/IRGS_3_3/runtime \
python -B tools/qualify_ordinary_communication_http.py
```

The working Engine runtime was tested atop parent
`abe6c479c8ec8b642cd6686e19e54cf0a543f506`; published code is identified by
its containing commit and [source hashes/results](ORDINARY_START_COMMUNICATION_VALIDATION.json).
App `b3a53cfd11bbd3745253520b4e8ed6718c826ab8` and Catalog
`fd2e84586431f3b516d48ce7936d80f5496abb85` were selected by explicit root
overrides. App's committed Engine/Catalog gitlinks remain respectively
`efc84364b86e640f5028bfac2dfd5ae3021695a9` and
`6f927b00e12a3339861ac353bc38d03c68279662`.

Full Engine discovery: **777 run, 776 pass, one private-save policy skip**.
Shared 35, start 33, communication 32, phase 28, and combined ordinary/native
communication/process 37 pass without skips; these overlap the full suite.
App start/communication regressions: **27 pass, zero skips**, with explicit
candidate roots. Engine integrity verifies 368 files; Kira canon verification
passes. The real App HTTP journey above passes without provider calls. The
full-suite excluded identity was replaced before execution; no user campaign
was used. Browser, Windows, package and live-provider checks were not run.

## Next dependencies

A4-ENG-01 remains in progress pending ordinary participation across the other
selected context and independent Catalog/App qualification. Catalog should
version independent actor inputs and evaluator expectations for this reviewed
fictional variant and its boundaries; App owns its pins and browser presentation.
A4-ENG-02 selected native travel and an early A4-ENG-03 intent contract remain
next; neither this increment nor a speech receipt establishes sustained Alpha
play. The coordinator owns compatible-set qualification and release.
