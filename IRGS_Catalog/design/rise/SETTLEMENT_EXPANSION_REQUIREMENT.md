# Rise settlement building limits and expansion permission

Requirement ID: **RISE-EXPANSION-01**. Recorded 31 October 2026.
Status: **User-adopted requirement; implementation and numerical profiles pending.**
This addendum extends the Rise v0.4 grant/construction design. It does not edit the
original specification, archives, existing saves or campaign release availability.

## Adopted requirement

The user requested: “For "Rise" There needs to be a limit to the amount of
buildings that can be constructed until permission is granted to increase the
size of your settlement”.

A settlement therefore has a finite building allowance. Reaching it prevents
starting additional construction until a valid expansion permission increases
that allowance. Population growth, available materials, money, a request, an
unaccepted offer or narration alone do not increase the allowance.

The initial allowance, expansion sizes and applicable granting authority must be
authored for each supported start. No universal numerical ladder, fee, time cost
or requirement for a particular kind of ruler is selected by this request.
The eight Rise families retain their existing qualification status.

## Implementation contract for the owners

Use the existing Core authority, rights, work, assets and institutional records.
Do not introduce an App-owned counter or a second settlement simulation.

- Bind the allowance to the actual settlement/site, grantees, effective permission,
  permitted construction and relevant land boundary. Permission to erect more
  buildings does not by itself grant neighboring land, forest rights, taxation,
  sovereignty, workers, supplies or completed structures.
- Count existing buildings and distinct committed new-building projects against
  the same allowance. Allocate the last available place atomically when a project
  starts. Completing a project converts its reservation into a building without
  counting it twice. Delegation and concurrent requests must use the same check.
- Pausing work retains the building reservation. Ordinary repair of the same
  building does not create a new building. Cancellation, demolition, replacement,
  ruins and enlargement need explicit rules for retained physical works and land;
  changing a UI label or deleting a project must not manufacture free allowance.
- Request, proposed terms, decision, acceptance where required, and effective
  permission remain separate events under the selected local procedure. The
  current legitimate authority can approve, refuse or offer authored conditions.
  New voluntary costs or obligations require player acceptance. A received grant
  reports the actual decision; it does not apply the capacity change again.
- Check valid rights, current allowance and physical feasibility again at commit.
  A failed admission changes no resources, commitments or elapsed work. Retrying
  the same committed request returns its original result and cannot raise the
  allowance twice. Expiry/revocation holds affected future work under its actual
  terms and does not erase buildings, history or earlier completed work.
- Keep legal building allowance separate from residential places, workforce,
  material stock, physical land fit and other service capacities.
- Expose actor-received allowance, completed/committed usage and known permission
  terms through Engine DTOs. Missing or undisclosed facts stay explicit. An absent
  allowance must not silently mean unlimited construction.
- Preserve saved grant/project identities and original receipts. Provide an
  explicit compatibility/migration policy for old Rise saves. Do not infer a new
  numerical cap from the one-shelter demonstration or silently reset a save.

These are implementation directions for delivering the adopted requirement;
particular state schemas, numbers, institutions and authored decision policies
remain owner deliverables requiring review and qualification.

## Current source finding

The reviewed published baseline is WorldWard 3.4.7. Engine
7f4ef150e2049c7718ac600680cb9c3633353a6a checks accepted active camp/temporary-
dwelling rights in IRGS_3_3/runtime/settlement_runtime.py, function _permission,
and admits one specifically identified shelter project in _start. Its setup
grants have no explicit general building allowance, and there is no expansion
request/decision path. That bounded one-project implementation is not this
system's delivery.

## Owner deliverables and acceptance

| Owner | Deliverable |
| --- | --- |
| Fulcrum-Engine | Profile-bound allowance/permission state, atomic project admission, expansion request/decision/effect, actor-safe DTOs, immutable retry and save compatibility through existing owners |
| WORLDWARD-APP-WEB | Engine-derived “buildings used / permitted”, committed-project usage, known terms/authority, a clear limit-reached explanation, and explicit request/review/acceptance controls in the existing story flow |
| WorldWard-Catalog | Authored start allowances and jurisdiction-specific procedures with provenance; independent actor/evaluator-separated acceptance journeys |

Required evidence: a build at the last available place; rejection beyond the
limit; two concurrent attempts competing for the last place; paused/delegated
work; project completion without double counting; request/offer/refusal leaving
the old limit unchanged; a valid effective expansion permitting the next build;
invalid/expired/wrong-site authority; unchanged stock/time after rejection;
original-result retry of expansion; save/reload and restore fencing; and an
existing non-Rise regression showing no accidental global construction rule.
Use synthetic campaigns. Specify fixture numbers explicitly as demonstration
choices, not as universal adopted values. A written work order does not pass
these tests or complete implementation.

## Publication boundary

This requirement is included as design/instructions in WorldWard 3.4.8. It
does not implement building allowances or expansion decisions. The coordinator
must review compatible owner commits/pins and run integration, fresh capture,
regression, browser/independent consumers and a clean extracted package before
each joined main publication. The following joined edition must be 3.4.9.
