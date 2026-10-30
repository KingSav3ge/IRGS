# Invitation decision validation — 29 October 2026

Engine baseline: `fe9c2c10ec3a66f1be590e1b34860119670b22cb`; this increment
is the commit containing this file. Current coordinated 3.4.6 joined pins at
execution: Engine `fe9c2c10ec3a66f1be590e1b34860119670b22cb`, App
`746c9a381e64b7f985d37edd39a91b5b79b2e027`, Catalog
`cf69a6cf628a6d9249124cc6b0700dfc59287677`. These are dependency selections,
not qualification of this later Engine increment.

Fresh checks in a reconstructed Engine source snapshot based on GitHub's
comparison against the clean local `837660372e0fdc17f51b80af791e9da7e3dcc9bf`:

- Runtime unittest discovery: 807 run, 806 passed, one deliberate skip. The
  skipped `test_suite.SuiteTests.test_legacy_ast_save_load_does_not_rewrite`
  references an external private save excluded by development policy.
- Focused decision, settlement, intent, offer and draft tests: 32 passed.
- `tools/qualify_shared_systems.py`: 35 passed; `tools/qualify_start_readiness.py`:
  33 passed. These overlap the runtime suite.
- Engine release integrity: 378 selected files verified, Core 3.3.
- App intent, process, communication and Rise tests: 48 passed against this
  Engine source override, local App `4f7cbd703d1207ae32db2bbc90d429415ae1e13f`
  and local Catalog `abb7ab86f2aa12b1c6585aa7da10f5809209112e`. That App
  checkout's committed gitlinks are Engine `296e46a1beed10d0ebf2841f133bb52fade83697`
  and Catalog `e97d87f0d17a16dbe0ce186badafe663188321a1`; the test override
  did not change these pins. This is not the current coordinated App source.
- A synthetic local App HTTP journey created R00 normally, produced the refusal,
  retried it, waited for the actual repair, produced agreement on a new request,
  and retrieved the original refusal after later play. Twelve tests passed in
  that execution, including the imported Rise regression class. This exercises
  the existing Rise HTTP action path, not a new Creator or intent DTO endpoint.

No browser, native Windows, packaged joined build, live provider, current
coordinated App/Catalog source qualification or two-context NPC decision suite
was run. Temporary synthetic stores were used; no personal campaigns or
credentials were opened. The world-draft host contract is design-only; neither
these tests nor the HTTP path implement or qualify draft-host creation.
