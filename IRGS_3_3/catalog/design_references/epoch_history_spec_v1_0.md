# IRGS website: epoch-based historical memory and summary consolidation

Version: 1.0 · Prepared: 18 October 2026 · Audience: website-development Codex

## 1. Purpose, scope, and status

Implement a historical memory view that remains manageable over long campaigns without erasing history, replacing authoritative state, or changing simulation outcomes. Completed years consolidate into five-year summaries, then twenty-five-year summaries, then an expanding cumulative history of the current century increments. Every completed 500-year epoch becomes a separate sealed historical summary. The process restarts inside the next epoch.

**This is a complete implementation handoff, not adoption of new IRGS mechanics.** The hierarchy below records the user's confirmed website direction. Technical choices introduced here remain proposed until accepted. This document does not establish a new Core release, select a database, migrate a campaign, or certify a working implementation.

Status labels:

- **Confirmed direction:** stated in the current request or visible user messages from the referenced conversation.
- **Established constraint:** supplied project instructions, especially authoritative state, causality, continuity, agency, and no automatic migration.
- **Derived requirement:** necessary consequence of the confirmed direction; interpretation is made explicit.
- **Proposed implementation:** a concrete engineering contract offered for review, not a recovered prior decision.
- **Unresolved:** evidence does not settle the choice.

Normative words such as MUST apply within the stated status. A MUST inside a proposed contract describes how that proposal would work if accepted; it does not promote the proposal into adopted rules.

## 2. Source authority and reconciliation

Primary conversation: [Website design features](chatgpt-conversation://6ad522ee-72f8-83ea-aa78-3a4fcfe6901a).

The conversation retrieval returned five user turns and no older-page cursor. Assistant messages were unresolved content-reference placeholders, not readable design text. No attachment was returned. Therefore exact historical word counts, prior schemas, and any additional assistant wording could not be verified. Do not claim this document reproduces those unavailable details.

| Source | Recoverable requirement | Status and disposition |
|---|---|---|
| Current request | Exact hierarchy; yearly boundaries; growing century budgets; state/event separation; retrieval, continuity, interfaces, UI, timelines, tests | Confirmed scope of this handoff |
| User turn `905bb9ff-3a41-4230-8eb9-0152bd1145d7` | Annual records accumulate into five-year summaries; five five-year summaries become a twenty-five-year summary at a new-year boundary | Retained |
| User turn `2774ce5a-90cb-4a6a-8ed4-0b25ec1b0961` | Four twenty-five-year summaries form one hundred years | Retained as the century construction rule |
| User turn `24af6fe3-d8df-4c89-9b69-775a92a0cc77` | One hundred years becomes one summary; additional twenty-five-year blocks lead to a two-hundred-year summary, then onward | Retained as cumulative century increments |
| User turn `3ba3fec1-1735-45e2-9d65-3b5f39422e34` | Separate at 500-year intervals; five centuries merge; word count expands with each cumulative century | Retained; reconciled with cumulative coverage below |
| User turn `2f958457-40d0-4406-83c0-c3de83ab471e` | “Perfect, create a file…” | Confirms proceeding with the described direction; does not recover absent assistant details |
| Supplied project instructions | Summaries are views; one source of truth; preserve agency, resource totals, chronology and continuity; no retroactivity | Established constraints |
| This specification | Interval encoding, records, jobs, APIs, publication protocol, validation strategy | Proposed implementation unless explicitly identified otherwise |

**Reconciliation:** “five 100-year summaries merge” describes five disjoint centuries of historical coverage. “100, then 200, then onward” describes the active cumulative view within that epoch. Preserve disjoint century source bundles in the archive while showing one cumulative summary. Never merge overlapping 100-, 200-, 300-, and 400-year cumulative texts as if they were independent history.

Accounted removals and supersession:

- An indefinitely growing list of five-year entries is superseded by the full hierarchy.
- A fixed hundred-year terminal tier is superseded by cumulative 100/200/300/400-year coverage and a sealed 500-year epoch.
- A single cumulative summary expanding beyond 500 years is incompatible with the confirmed epoch separation.
- Retired active-view entries are not deleted historical records. Their unique valid information remains recoverable.
- No unavailable assistant proposal is assumed adopted or silently restored.

## 3. Ownership and dependencies

**Established constraint:** memory consolidation is a presentation and retrieval operation. It has no authority to execute simulation actions, spend resources, settle projects, change relationships, or invent PC choices.

**Proposed ownership:** a website history service owns summary versions, consolidation jobs, and the active-history manifest. The campaign runtime continues to own its clock, canonical state, events, resource ledgers, and knowledge/access controls. A retrieval service joins those records by stable identifiers. Genre and setting adapters supply terminology and calendar rendering, not separate copies of the consolidation algorithm.

Required interfaces: committed campaign clock; stable campaign and branch identity; authoritative state reads; historical events and correction lineage; entity identity; access/knowledge policy; versioned summary storage; durable job execution. Bind these to the actual adopted runtime during implementation. This handoff does not assert compatibility with an unread Core package.

## 4. Exact logical hierarchy

**Confirmed direction, with explicit boundary interpretation:** consolidation runs when a new campaign year begins, after the preceding year is closed. At the start of Year 6, Years 1–5 are complete. At the start of Year 26, Years 1–25 are complete. At the start of Year 501, Years 1–500 form the first sealed epoch.

The current, incomplete year remains a separate open record. It never counts toward a completed group.

| Tier | Complete inputs | Result in the active history |
|---|---|---|
| Annual | One closed campaign year | One annual summary |
| Five-year | Five adjacent annual summaries | One five-year summary |
| Twenty-five-year | Five adjacent five-year summaries | One twenty-five-year summary |
| First century | Four adjacent twenty-five-year summaries | One cumulative 100-year summary |
| Next century increments | Existing cumulative summary plus the next four twenty-five-year summaries | Replacement cumulative 200-, 300-, or 400-year summary |
| Epoch completion | First 400 years plus final four twenty-five-year summaries, with five disjoint century bundles as evidence | One sealed 500-year epoch summary |
| Next epoch | New annual records after the sealed epoch | Same hierarchy, reset within the next epoch |

“Replacement” means replacement in the active manifest; it does not mean destructive overwrite. There may be an internal 500-year candidate, but the published result is the sealed epoch, not an overlapping active 500-year cumulative entry as well.

Within a century, newer twenty-five-year blocks sit beside the previous cumulative summary. Example: at the start of Year 176, active history includes cumulative Years 1–100 plus Years 101–125, 126–150, and 151–175. At the start of Year 201, those blocks and Years 176–200 are represented by cumulative Years 1–200.

Epoch summaries remain separate. At the start of Year 1001, retain two sealed summaries: Years 1–500 and 501–1000. Do not silently merge them into a thousand-year tier.

### 4.1 Proposed interval representation

Use integer campaign-year ordinals and half-open intervals `[start, end)`. Let ordinal 0 identify Year 1. Thus Years 1–5 occupy `[0,5)`, and the first epoch occupies `[0,500)`. Keep display dates separate from ordinal arithmetic.

For `N` complete years since the chosen consolidation origin:

```text
sealed_epoch_count = N div 500
r = N mod 500
completed_centuries_in_open_epoch = r div 100
q = (r mod 100) div 25
f = (r mod 25) div 5
a = r mod 5
```

The compact active view contains:

- `sealed_epoch_count` separate epoch entries;
- at most one cumulative entry covering `100 × completed_centuries_in_open_epoch` years;
- `q` twenty-five-year entries, `f` five-year entries, and `a` annual entries;
- one separate current-year record.

The complete intervals MUST form a disjoint partition of `[0,N)`. There are no gaps, overlaps, or duplicated coverage. The current-year record is outside that partition.

This bounds the open epoch to at most twelve closed entries plus one open-year record. The sealed archive still grows by one entry per 500 years; neither storage nor full-history context is constant-size.

Calendar origin is unresolved. The timelines in this document use campaign-relative Year 1, not a claim that consolidation aligns to civil centuries or starts at historical year 1. A campaign beginning midyear, an imported history, or a calendar without a year zero requires an explicit adapter and origin decision.

## 5. Yearly boundary and publication procedure

**Proposed implementation:** subscribe to committed campaign-year transitions, not wall-clock New Year's Day, browser visits, session endings, or token pressure.

1. Obtain the committed boundary identifier, campaign/branch, calendar revision, and archive watermark. Use the runtime's established ordering for events at the boundary; do not invent an order for simultaneous events.
2. Close the preceding annual record against that committed snapshot. Open the new current-year record exactly once.
3. Plan all eligible promotions, lowest tier first: five years, twenty-five years, a century increment, then epoch sealing.
4. Generate candidates using exact source coverage, archived source links, and applicable continuity requirements. Existing summaries aid retrieval; they are not the sole evidence base.
5. Validate coverage, provenance, entity identity, required continuity anchors, access policy, budget, and source revision. Failed candidates remain unpublished.
6. Atomically publish a new active manifest. Retain the previous complete view until its replacement is valid. Mark generation lag explicitly; an old view must not masquerade as current.
7. Retain subordinate summaries and source references in the archive. Record job outcome and revision lineage.

At a boundary divisible by 500, all applicable tiers may form in the same job, but only the final disjoint representation is published. No transient mixture of parent and children should be counted as the active history.

Idempotency key: campaign + branch + boundary + policy revision + source revision. Retrying the same work must not create another epoch or replay events. Publication uses a manifest revision check to prevent a stale job overwriting newer work.

For a time advance crossing multiple years, process every crossed boundary in logical order or produce a demonstrably equivalent batched result. Empty years still have coverage and a supported “no recorded events” status; absence of records is not proof of peace or inactivity. The simulation must already have advanced autonomous actors. Summarization cannot freeze or simulate them itself.

Failure or budget overflow must not delete source records, invent a shorter history, or reset the campaign. Proposed default: queue retry, retain the last valid view, and expose pending coverage. Whether a particular AI interaction waits for fresh summaries is an unresolved product policy; it must never proceed on falsely current data.

## 6. Expanding word budgets

**Confirmed direction:** cumulative century word allowance grows with each additional century. A two-hundred-year summary must not be forced into the same allowance as a one-hundred-year summary.

No numerical allowances were recoverable. Do not fabricate “approved” word counts.

**Proposed configurable policy:**

```text
annual_budget = A
five_year_budget = F
twenty_five_year_budget = Q
cumulative_budget(k) = B + (k - 1) × D, for k = 1..5
sealed_epoch_budget = cumulative_budget(5)
constraints: A, F, Q, B are positive integers; D is a positive integer
```

This linear schedule is a proposal, not a confirmed formula. A configured strictly increasing table is another valid implementation. Under the linear proposal, 100/200/300/400/500-year allowances are `B`, `B+D`, `B+2D`, `B+3D`, and `B+4D`. The next epoch begins again at `B` for its first century. Earlier sealed epochs retain their own text and budget provenance.

Budgets are maximum allowances, not minimum filler quotas. A quiet century need not produce more text merely because it may. Define a versioned word-count function and language policy; model token limits and prompt overhead require a separate configuration. Suggested scope: count generated narrative text; store citations, identifiers, and continuity records as structured metadata outside that allowance. These metadata still consume storage and, when retrieved, context tokens.

Never silently truncate required continuity information to meet a prose cap. Preserve it in authoritative records and an explicitly retrieved continuity set; regenerate, defer publication, or request policy adjustment if required output cannot fit. Exact budgets, growth curve, and epoch allowance remain uncalibrated.

## 7. Authoritative records, archives, and continuity

**Established constraint:** a summary is a view. It is not a ledger, inventory, event database, or source of new facts.

Keep these responsibilities distinct:

| Record family | Authority and use |
|---|---|
| Current campaign state | Canonical current quantities, locations, conditions, actors, projects, obligations, and clock |
| Event archive | Canonical historical occurrences, their evidence/uncertainty, and correction lineage; retain occurrence, observation, transmission, and receipt distinctions where applicable |
| State history/checkpoints | Exact historical state where the runtime supports it; do not claim arbitrary reconstruction unless snapshots and/or sufficient events exist |
| Summary archive | Versioned derived prose, source coverage, provenance, and supersession links |
| Continuity index | Derived pointers to unresolved and still-relevant canonical facts; never an independent copy of their authority |
| Active manifest | Which summary versions currently constitute the compact historical view |

Logical separation is required; separate physical databases are not. Use the runtime's existing authoritative schema rather than creating competing inventories or event totals.

Continuity anchors include unresolved commitments, ownership and succession, persistent injuries or exposures, outstanding debts, ongoing projects, active relationships, institutional changes, known threats, and consequences that remain relevant. They survive age thresholds while applicable. Resolving one requires an authoritative state/event change, not a summarizer deciding it is old enough to forget.

Do not sum cumulative summary numbers to derive resources or casualties. Retrieve canonical records with units, effective time, and provenance. Reports of an event are not additional events. Conflicting reports remain attributed claims unless authority resolves them.

Sealing fixes an epoch's temporal extent and ends routine accumulation. **Proposed correction policy:** a correction produces a new version for the same epoch range, with explicit supersession and an audit reason. It does not silently mutate the original, unseal it for new centuries, or retroactively change campaign state. Whether this revision policy is accepted remains unresolved.

## 8. Retrieval and guarantees

**Derived requirement:** consolidation must reduce routine presentation/context load without making archived history inaccessible.

**Proposed retrieval procedure:**

1. Enforce campaign, branch, requester, and character-knowledge scope before searching or assembling context.
2. Retrieve current authoritative state for present-tense questions and active continuity anchors for ongoing consequences.
3. Use the compact history or relevant epoch as an orientation/index layer.
4. Expand to subordinate summaries and cited events by time interval, entity, topic, or dependency.
5. Resolve exact factual questions against authoritative records. If records are missing, inaccessible, or insufficient, return that limitation instead of guessing from prose.
6. Return evidence identifiers, effective times, revision/watermark, completeness, and any conflicts alongside the answer context.

Contracts:

- **Coverage:** every closed year appears exactly once in the active history, including quiet or incompletely recorded years.
- **Recoverability:** promotion removes no source evidence or subordinate summary needed for drill-down.
- **Continuity:** still-active obligations and consequences do not disappear because their originating epoch is sealed.
- **Authority:** no summary writes simulation state; a source correction follows the runtime's correction process.
- **Identity:** stable entity and branch IDs prevent renamed places, descendants, or divergent histories from being conflated.
- **Knowledge:** GM/world history must not leak unrevealed facts into a player/character view or AI context. Filtering a whole-world summary after generation may be insufficient; generate scoped views where necessary.
- **Honesty:** semantic compression is lossy. Archival access and validation are guarantees to implement; perfect retention of every nuance in short prose is not promised.

For AI runtime context, select relevant epochs and retrieved evidence rather than automatically inserting every sealed epoch. Do not evict active continuity solely because an epoch is old. If mandatory context exceeds capacity, expose a defined overflow/defer path instead of silently dropping obligations.

## 9. Proposed data interfaces

Names are illustrative and transport-neutral. Adapt to repository conventions without changing interval or authority semantics.

```typescript
type Range = { startYearOrdinal: number; endYearOrdinalExclusive: number };
type Scope = { campaignId: string; branchId: string; accessScopeId: string };
type Tier = "annual" | "five_year" | "twenty_five_year"
          | "cumulative_centuries" | "sealed_epoch";

interface SummaryVersion {
  id: string;
  revision: number;
  scope: Scope;
  range: Range;
  epochIndex: number;
  tier: Tier;
  centuryCount?: 1 | 2 | 3 | 4 | 5;
  sourceSummaryVersionIds: string[];
  sourceArchiveRef: string; // durable query/snapshot reference, not prose
  sourceWatermark: string;
  sourceDigest: string;
  continuityAnchorIds: string[];
  evidenceLinks: { claimId: string; recordIds: string[] }[];
  text: string;
  wordCount: number;
  budgetPolicyRevision: string;
  generatorRevision: string;
  validationReportId: string;
  status: "candidate" | "validated" | "published" | "superseded" | "failed";
  supersedesId?: string;
  createdAt: string; // processing time, not campaign occurrence time
}

interface HistoryManifest {
  scope: Scope;
  revision: number;
  consolidationOriginId: string;
  closedThroughYearOrdinalExclusive: number;
  summaryVersionIds: string[]; // ordered, disjoint closed-year coverage
  openYearRecordId: string;
  sourceWatermark: string;
  policyRevision: string;
}
```

Persist a job record containing boundary ID, idempotency key, expected manifest revision, candidate IDs, source revision, status, validation results, and retry/error information. Persist continuity pointers with canonical reference, effective interval, relevance reason, access scope, and source version. Do not store copied balances as independent continuity truth.

| Operation | Input | Output and obligations |
|---|---|---|
| `onYearBoundary` | Campaign/branch, committed boundary, source watermark | Existing or new job; idempotent |
| `planConsolidation` | Closed-year frontier, origin, policy, current manifest | Deterministic target ranges and dependencies; no state mutation |
| `buildSummary` | Exact range, scope, versioned sources, budget | Candidate plus evidence mapping; no automatic publication |
| `validateSummary` | Candidate, source snapshot, expected coverage | Structured pass/fail and unresolved semantic review flags |
| `publishManifest` | Validated candidates, expected revision | Atomic new manifest or conflict; no partial parent/child swap |
| `getHistory` | Scope, range, detail tier, cursor | Entries with coverage and pending/stale status |
| `expandHistory` | Summary version ID, requester scope | Archived children and source evidence, with access checks |
| `retrieveContext` | Question, entities, date range, scope, context limit | State references, continuity, relevant history, evidence, completeness |
| `rebuildDerivedHistory` | Explicit campaign selection, approved policy/source versions | Preview and new derived versions; no implicit migration |

Reject cross-branch inputs, nonadjacent coverage, incompatible scopes, duplicate source coverage, and invalid ranges. A summary dependency graph must be acyclic. A cumulative candidate must draw its new material from the next disjoint century, not replay the earlier cumulative content as additional events.

## 10. Website implications

**Proposed UI:** present a current-year panel, the compact open-epoch history, and a list of sealed epochs. Show date ranges, tier, status, and expandable source detail. Use explicit labels such as “Years 1–200 · cumulative history” and “Years 1–500 · sealed epoch.”

- Replace child cards with a parent card only after publication succeeds. Preserve a drill-down path and stable links to archived versions.
- Search across all authorized epochs by entity, date, and topic; do not restrict search to visible prose.
- Display pending consolidation, stale source revisions, failed generation, partial coverage, and corrected versions truthfully.
- Keep current quantities in state panels, historical claims in history views, and exact historical evidence behind source links.
- Keep still-relevant obligations visible across epoch changes. A fresh epoch does not imply a fresh campaign state.
- Paginate or virtualize long epoch lists. Do not add an unrequested thousand-year consolidation tier to solve UI load.
- Offer Markdown export with range, version, scope, and provenance. Do not expose inaccessible source titles or counts through export or search metadata.
- Ordinary users need dates and understandable statuses. Developer budget settings and job diagnostics belong in appropriate administrative views.

## 11. Worked timelines

These are scripted expected states, not playtests. `A` is an annual entry, `F` a five-year entry, `Q` a twenty-five-year entry, `C` a cumulative entry, and `E` a sealed epoch. The table shows state immediately after a successful new-year consolidation. The named new year is open and excluded from completed coverage.

| Start of year | Complete years | Compact closed history |
|---|---:|---|
| 1 | 0 | None |
| 2 | 1 | A1 |
| 5 | 4 | A1–A4 |
| 6 | 5 | F1–5 |
| 10 | 9 | F1–5 + A6–A9 |
| 11 | 10 | F1–5 + F6–10 |
| 21 | 20 | Four F entries covering 1–20 |
| 25 | 24 | Four F entries covering 1–20 + A21–A24 |
| 26 | 25 | Q1–25 |
| 51 | 50 | Q1–25 + Q26–50 |
| 76 | 75 | Three Q entries covering 1–75 |
| 100 | 99 | Three Q covering 1–75 + four F covering 76–95 + A96–A99 |
| 101 | 100 | C1–100 |
| 126 | 125 | C1–100 + Q101–125 |
| 151 | 150 | C1–100 + Q101–125 + Q126–150 |
| 176 | 175 | C1–100 + three Q covering 101–175 |
| 201 | 200 | C1–200 |
| 301 | 300 | C1–300 |
| 401 | 400 | C1–400 |
| 476 | 475 | C1–400 + three Q covering 401–475 |
| 500 | 499 | C1–400 + three Q covering 401–475 + four F covering 476–495 + A496–A499 |
| 501 | 500 | E1–500; no cumulative entry in the new epoch |
| 506 | 505 | E1–500 + F501–505 |
| 526 | 525 | E1–500 + Q501–525 |
| 601 | 600 | E1–500 + C501–600 |
| 701 | 700 | E1–500 + C501–700 |
| 1001 | 1000 | E1–500 + E501–1000 |
| 1101 | 1100 | E1–500 + E501–1000 + C1001–1100 |

At Year 201 the four new Q entries cover 101–200. They do not represent four additional centuries. C1–200 replaces C1–100 and those Q entries in the active view; all remain archived.

Continuity example: an obligation begins in Year 490 and remains active in Year 510. At Year 501 its origin moves into E1–500, but its canonical obligation and continuity pointer remain active. Retrieving its terms follows the original evidence. No new obligation, payment, or expiry is created by consolidation.

Correction example: a source record concerning Year 80 is corrected in Year 620 through the authorized correction process. The affected sealed epoch is marked stale and may receive an explicitly linked replacement version. The historical correction is not a new event occurring in Year 620 unless the runtime actually records such an event.

## 12. Acceptance and regression tests

The following are required implementation tests, not a claim they have passed in the website.

| Case | Expected result |
|---|---|
| Boundaries 4→5, 24→25, 99→100 complete years | Exactly one appropriate promotion at the following new-year boundary |
| 199→200 and 399→400 | One expanded cumulative entry; earlier coverage not counted twice |
| 499→500 | One sealed epoch; no overlapping cumulative entry; new current-year record |
| 999→1000 | Two separate sealed epochs; no thousand-year merge |
| Incomplete fifth/twenty-fifth/hundredth year | No premature promotion |
| Duplicate boundary delivery | Same logical manifest and no duplicate summaries/events |
| Concurrent jobs and stale retries | At most one valid publication; old job cannot overwrite newer sources |
| Crash before/after publication | Old or new complete manifest recoverable; no missing coverage |
| Generator failure, unsupported claim, or over-budget text | Candidate withheld; sources intact; failure/pending status visible |
| Quiet year and unknown year | Both covered; uncertainty retained; no invented events |
| Multi-year jump | Same ranges and authoritative state as sequential boundaries; no duplicate simulation |
| Current state before/after consolidation | Identical canonical state and ledger contents |
| Obligation spanning epochs | Remains retrievable and active until authoritatively resolved |
| Repeated report of one casualty/transfer | One canonical occurrence; no duplicated totals or costs |
| Mixed outcome or undeclared PC action in generated prose | Unsupported assertion rejected; no action written to state |
| Renamed entity, successor, or same-name entity | Stable identity and lineage preserved; no accidental merge |
| Branch fork and restricted character knowledge | No cross-branch contamination or unauthorized disclosure |
| Source correction in sealed epoch | Explicit stale/revision lineage; no silent mutation or retroactive state rewrite |
| Word budget increments | Configured century allowances strictly increase; no invented production values |
| Historical factual lookup omitted from prose | Underlying authorized evidence remains retrievable |
| Context overflow | Explicit completeness/overflow handling; no silent loss of required continuity |
| Custom calendar and nondefault origin | Correct boundary mapping independent of display year numbering |

Property tests should verify for many nonnegative `N`: exact coverage `[0,N)`, no overlaps, correct tier widths/alignment, at most one open-epoch cumulative entry, fixed 500-year sealed ranges, and preservation of archive IDs. Arithmetic tests do not validate narrative accuracy.

Semantic evaluation requires source-grounded fixtures: dense and sparse centuries, conflicting reports, long projects, unresolved consequences, and changing institutions. Check fidelity, attribution, retrieval success, and omission rates across repeated runs. LLM prose need not be byte-identical; interval plans, authority handling, and continuity outcomes must be reproducible.

## 13. Calibration and unresolved decisions

Resolve these in implementation review without inventing previously adopted answers:

1. Consolidation origin: campaign start, civil calendar, imported-history anchor, or explicit profile setting? How are initial partial years treated?
2. Actual annual, five-year, twenty-five-year, century, and epoch word allowances; linear versus table-based growth; counting rules and localization.
3. Accepted sealed-epoch correction policy and distinction between source correction, annotation, and campaign branch changes.
4. Existing authoritative archive capabilities: event retention, historical state snapshots, correction semantics, and whether exact past state is reconstructable.
5. Required continuity categories, authority for resolving them, and handling mandatory context overflow.
6. Generation model, prompt/version control, validation depth, semantic review thresholds, latency, cost, and rebuild policy.
7. Whether lagging history blocks any AI interaction; acceptable stale-view behavior and retrieval fallback.
8. Access scopes, character knowledge snapshots, shared versus per-scope summaries, and cache invalidation on permission changes.
9. Storage/retention policy, archival export, backups, and restoration. Do not delete underlying evidence as an incidental consolidation optimization.
10. Treatment of pre-campaign history and externally supplied narratives: provenance and uncertainty must remain distinguishable from simulated events.

No numerical performance, semantic fidelity, or balance claims are calibrated here. Worked cases are specification examples, not playtesting.

## 14. Migration, delivery, and change record

Version 1.0 rebuilds the visible decisions into one implementation-oriented specification. It adds an explicit reconciliation of disjoint century evidence with cumulative active views; symbolic budgets; proposed interfaces and publication procedures; retrieval/continuity constraints; timelines; and acceptance cases. Those additions are labeled rather than passed off as prior adoption.

**Migration impact:** none executed. Implement behind an explicit policy/version selection. Inventory existing history, origins, scope, source completeness, and incompatible ranges; produce a preview manifest and preservation report; obtain the applicable campaign migration authorization; then publish derived versions atomically. Preserve the prior manifest for rollback. Rollback changes the view, not the campaign's events or current state.

If historical sources are insufficient, mark gaps and unresolved claims. Do not fabricate annual records from a broad retrospective summary and then claim exact yearly evidence.

Definition of implementation completion: repository bindings and unresolved configuration choices are recorded; boundary/property tests pass; source-grounded semantic cases are reviewed; source retrieval and access controls work; failure recovery is demonstrated; UI exports disclose status and provenance; and migration remains separately authorized. Resubmission of this file is not adoption, deployment, or evidence of those outcomes.
