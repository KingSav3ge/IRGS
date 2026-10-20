# IRGS Core 3.3 live AST release

**Selected for this local AST installation by the user’s direction on 18 October 2026.** The user clarified that the goal is a live 3.3 version and that it is for AST. This supersedes the earlier instruction to leave this receiving release unselected. Other installations and existing campaign save files have not been migrated.

The interface uses the audited registry as the post–Day 2 guide to existing characters entering Day 3. There are 37 identities: 36 humans and Abel. “Able” was an accidental spelling and is retained only as a deprecated lookup for archival material. Roger Kett is AST-36 and Adam Lark AST-37; AST-38/39 remain withdrawn duplicates. Master Nicholas Rookwood’s disputed knighthood is not resolved by artwork. Provisional capability numbers remain source material, not adopted statistics.

The starting context retains the approximately 21:45 Day 2 checkpoint and Ian’s last confirmed state. Loading this release does not wake him, move him, spend his money, manufacture his shield, heal his palm or send a letter. The user can record a new declaration explicitly. The complete registry record for every character is accessible in the interface; only the supported checkpoint fields are structured as current context. Unknown balances, stocks and physical parameters are not filled with zero or invented defaults.

## What is live

`Start-AST-3.3.ps1` starts a loopback-only local interface at `http://127.0.0.1:8763`. It opens the actual persistent AST state at `live/ast_state.json`. The launcher validates the runtime and registry hashes against `release.json` before serving. State changes use optimistic checksum checks, serialized transactions and atomic file replacement. A session token protects mutation requests from unsolicited cross-site submissions.

The AST receiver supports ten explicitly bounded operations: record evidence, receive evidence, record player declaration, set scene context, confirm a supported character field from established evidence, establish a sourced actual stock record, transfer actual stock, record an obligation, record a design reference, and receive an order. Unknown operations are refused. Recording a declaration is not resolving an action. Narrative or combat outcomes still require the selected Core/AST procedure and actual supported inputs; no general-purpose AI game master is running inside the server.

## Dependency and decision changes from R8

The observer follows the complete selected `apply` chain, including R5 physical loss, R6 tracked work and R7 fabrication reconciliation. It captures negative lookups, collection scans, state preconditions and actual write differences. Transaction clones retain the observer. Whole-list accesses conservatively reserve the list except initialization/validation reads; this deliberately sacrifices some parallelism. Broad invariant reads are retained in a separate evidence set and checked again against the complete candidate.

The supported code is reviewed deterministic JSON-state Python. This instrument is not a sandbox for hostile plugins, external side effects, hidden globals or arbitrary C-level reads. Certificate code hashes bind the implementation; observed cases do not prove every branch. The supported runtime operation inventory spans shared, loss, work, fabrication, proposed Military/Roman receiver operations and AST operations. `results/r9_certification_matrix.json` records exact observed-case status, example traces, read/write unions and remaining limitations. The old R8 matrix is historical evidence only.

Requests and their original payloads are durable in the same world state. Conflicts preserve intent without selecting a lexical winner. Decisions require a scoped active mandate and a genuinely later time, revalidate against then-current resources, and execute at most once. Denied requests stay recorded. Unsupported physical-occurrence, milestone and player-action adjudications cannot be turned into delayed automatic approvals; they need a new specialist event with the necessary evidence. Saved decision history is supported; replay from only the legacy domain journal is not a complete reconstruction of workflow mandates and decisions.

## Cross-engine and strategic evidence

Military equipment issue checks received orders, directive authority and actual holdings. Roman delegated work checks the active delegation, time, recipe, workers and site before using the shared reservation procedure. These are new bounded receiver operations, not certification of every operation in the original native documents. AST institutional stock contention and knowledge receipt are exercised against its one authoritative state. Other Fantasy, PAF, SNWE and Space native operations remain unqualified and cannot execute through these receivers.

The R9 synthetic strategic scenario advances 14 days, commits 77 institutional operations and produces/consumes 42 meals; checkpointed and uninterrupted execution match. Its cash/population totals remain conserved, and a saved conflict is later approved/denied without double effects. R8’s historical 90-day evidence remains preserved. These synthetic figures are not the AST economy. Autonomous day advancement is not enabled for the actual AST campaign without supported inventories, institutional policies, rates, work evidence and information access selections.

## Reproduce and use

```powershell
.\Start-AST-3.3.ps1
# Open http://127.0.0.1:8763
```

With Python 3, from `runtime`:

```text
python -m unittest discover -p "test_*.py" -q
python run_r9_certification.py
python run_r9_scenario.py
python irgs_r9.py status --state ../live/ast_state.json
```

`build_release_3_3.py` rebuilds the local selection and immutable runtime manifest after checks pass. Back up `live/ast_state.json` to preserve actual new events. The downloadable archive includes the initial post–Day 2 guide state; later local gameplay writes are not retroactively included in that archive.
