# IRGS 3.4.0 — shared response integration and patches

The App now uses Engine-generated local receipt/draft data and the Catalog depot
in supported campaigns. Ordinary authored-scene and Rise actions share the public
response contract, save exact presentation atomically and recover the same result
after lost acknowledgements, retries, restart and restore. Selected semantic
drafts remain editable and require explicit submission. Missing libraries retain
the literal authorized result without inference.

Engine supplies common actor/capability/intent/receipt contracts and bundles the
exact 750-system/250-draft depot with 32 recipes, while retaining its compatibility
runtime. Catalog supplies separate actor/oracle evaluation material for actual
non-Rise and Rise consumers. Further semantic and process/communication adapters
retain their implementation requirements; not all families become gameplay.

Coordinator patches align the App dependency pins and make Catalog intake consume
the exact code and text bytes verified by their hashes. Both mid-load replacement
failures were reproduced and now pass regression checks. Fresh observed operation
evidence replaces the stale record; unqualified branches remain explicit.

Full joined tests, actual nine-case Catalog play, two-context Chromium and six
Creator-initialized synthetic profile checks passed. Non-Rise failures, scarce
dispatch delivery, zero Rise spans, draft editing, stale navigation and durable
results remain intact. Eight expected private-fixture/platform skips remain.
See [source and evidence](provenance/qa/shared_response_integration_3_4_0_review.json).

Run `python -B IRGS_Web/server.py --port 8766` or the Windows launcher. Default
AI remains unconfigured. Live/model-quality evaluation, general dialogue,
freeform/combat, wider DEV/C2 and additional App adapters remain unfinished.
Original archives and user campaigns remain preserved. Core compatibility is
3.3; the coordinated development version remains 3.4.0.
