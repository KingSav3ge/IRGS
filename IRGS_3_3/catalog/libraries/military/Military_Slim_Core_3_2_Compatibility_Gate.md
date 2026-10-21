# Military Slim v1.0 — Core 3.2 Compatibility Gate

**Status:** Review checklist only. No complete compatibility bridge is established or adopted here.

The uploaded `IRGS-MLS-SLIM-1.0` explicitly pins `IRGS-CORE-3.0` and `IRGS-SCL-0.1`. The new Military Content Library uses Core 3.2 and SCL 1.0 as its **reference environment**, but does not repin or change the Soldier/Military Slim edition. Its own Section 2.1 contains exact Core 3.0 procedure numbers; those require a bidirectional semantic review against Core 3.2, not a filename or number substitution.

## Required receiving review

| Military source section | Function to preserve | Core 3.2 bridge gate |
|---|---|---|
| §1 | Scope, agency, civilian and service play | Role and campaign authority unchanged |
| §2 | Core references, conditional profiles and manifest | Re-resolve all owner labels, source scope, lifecycle and event contracts |
| §3 | Recruitment, appointment, service terms | Contract, eligibility, actual enrollment, issue remain distinct |
| §4 | Duty, training, doctrine | Commitments, qualification, rollout and time remain equivalent |
| §5 | Rank, appointment, career | Skill, institutional authority and job assignments separate |
| §6 | Comrades, mentors, unit culture | Morale/cohesion, knowledge and interpersonal agency preserved |
| §7 | Orders/command | Issue, transmit, receive, execution, response separate |
| §8 | Conduct and recognition | Allegation, decision, executed sanction and award independent |
| §9 | Deployment, operation, aftermath | Shared causality, loss, logistics, relief and scale continuity |
| §10 | Pay, provisions and issued property | ECO claims and stock/asset transfers neither duplicated nor inferred |
| §11 | Leave, fitness, captivity/missing | Injury, status, custody, available role, information distinct |
| §12 | Household service consequences | Remittances, delayed delivery and autonomous households retained |
| §13 | Separation, retirement, succession | Terms, pay, issued property and state continuity preserved |
| §14 | Branch profile, 6 eras and 12 categories | Replace catalogue references only through exact qualified source bindings |
| §15 | Military records and event subscriptions | Authoritative write owners and event idempotence unchanged |
| §16 | 30 source acceptance requirements | Preserve and re-execute under exact selected profiles |
| §17 | Adoption, provenance, prospective migration | No retroactive state changes or unapproved adoption |

## Acceptance and signoff

For each difference: map `source section → Core 3.2 clause → owner → record schema → trigger → unit/status → acceptance test → adoption authority`. Preserve the original thirty `SML-01`–`SML-30` cases, execute relevant source and receiving behavior tests with actual settings, handle simultaneous conflicting inputs and save/replay, then explicitly pin the selected versions and effective time. Until passed, the Core 3.0 genre edition remains the only declared pinned combination. Missing model parameters block only dependent operations; ordinary supported work continues.
