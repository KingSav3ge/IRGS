# Quay contact decision validation — 29 October 2026

Engine baseline `74a185104d0d856e951e2e547a0a1d2d06d1499e`; this increment is
the commit containing this file. The local test source was reconstructed from
the verified previous remote tree `9592bc558b1761efa5a7e14559353e7b1e8a8484`;
ordinary Git fetch failed authentication, so the original checkout was preserved.

Fresh checks on synthetic temporary worlds and stores:

- Runtime unittest discovery: 812 run, 811 passed, one deliberate skip:
  `test_suite.SuiteTests.test_legacy_ast_save_load_does_not_rewrite` references an
  external private save excluded by development policy.
- Focused decision, draft, scene, communication, offer and Rise-decision suite:
  38 passed before the final additional player-control regression. The final
  decision module alone passed all 5 tests; the complete runtime suite above
  includes the added regression.
- `tools/qualify_shared_systems.py`: 35 passed;
  `tools/qualify_start_readiness.py`: 33 passed;
  `tools/qualify_communication_capabilities.py`: 32 passed. These overlap runtime discovery.
- Engine component integrity: 379 files verified, Core 3.3.
- Local App scene, intent, communication and setup-preview tests: 38 passed with
  this Engine source override, local App `4f7cbd703d1207ae32db2bbc90d429415ae1e13f`
  and local Catalog `abb7ab86f2aa12b1c6585aa7da10f5809209112e`. The local App
  committed gitlinks remain Engine `296e46a1beed10d0ebf2841f133bb52fade83697`
  and Catalog `e97d87f0d17a16dbe0ce186badafe663188321a1`; the test override
  does not alter them. These are not the latest coordinated App/Catalog sources.
- One independent synthetic HTTP journey through the existing App setup and
  action routes reviewed the new opening, ordinarily created the world, committed
  and replayed the refusal, delivered the actual dispatch, and replayed the
  original refusal after later play. One test passed, zero provider calls.
- Local Catalog `tools.tests.test_intent_world_draft_contract`: 3 passed against
  its own selected fixtures; it is not an independent adoption of this change.
- `git diff --check` passed with the existing release JSON CRLF convention
  recognized by `core.whitespace=cr-at-eol`.

Current WorldWard 3.4.6 joined pins observed: Engine
`fe9c2c10ec3a66f1be590e1b34860119670b22cb`, App
`746c9a381e64b7f985d37edd39a91b5b79b2e027`, Catalog
`cf69a6cf628a6d9249124cc6b0700dfc59287677`. The corresponding latest App and
Catalog development mains observed were `4ffd53a351a4d21c2005505076641c1827425147`
and `d8e2840ce0244c18da2512cabf9ef9785abcce3d`; neither was qualified here.

No browser, current App/Catalog pins, native Windows, packaged joined build or
live model was tested. No user campaigns were opened. Atomic draft hosting and
Creator playtest remain unimplemented; the coordinator owns the next joined gate.
