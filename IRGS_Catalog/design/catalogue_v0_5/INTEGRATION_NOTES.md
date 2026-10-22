# IRGS Catalogue v0.5 — integration contract (proposal)

## What these records are

Forty-four **concept records** for review and future catalogue integration: 31 launch-target campaigns, 12 future campaign proposals, one separately classified Curated Simulation System. They are **not** complete Campaign Profiles, Campaign States, full content, payment entitlements, or runnable campaign implementations.

## Safe app adapter

1. Read `catalogue.json` or individual `records/<ID>.json` files. Validate against `SCHEMA.json`.
2. Use `catalogue_id` as stable app key. `app.preview_route` is a *proposed* slug path, not proof of an existing application endpoint.
3. Display title, tagline, synopsis, genres, setting, period, and `playable_perspectives` as editorial **previews**, not guarantees of implemented character entry.
4. Gate listing by `approval.public_preview` and a separate publisher-controlled boolean; **all preview_enabled_default=false** here. Do not make concept drafts public automatically.
5. Gate gameplay separately by release approval and verified runtime availability; **all launch_enabled_default=false** here. MC-01 records the user's prior playable designation without pretending the supplied suite was executed.
6. Do not display “Play”, “Owned”, a release date, or a price for an unverified or undecided product.
7. Add asset IDs only after original artwork or licensed art is approved. No thumbnails/third-party image URLs are supplied.
8. Treat `SS` free as a *launch entitlement intention*. No other prices are established.

## Data model interfaces

- Product catalogue and visibility: catalogue service owns editorial preview data and public status.
- Campaign identity/scope: Workshop/adoption pipeline owns approved campaign profile and entry configuration.
- Campaign runtime: Core owns persistent actor, property, resources, time, organizations, institutions, knowledge, and effect state.
- Genre/setting content: reusable libraries provide verified historical or fictional facts; engine layers provide specialized rules only where needed.
- User saves: state of an individual playthrough, **never** substitute the product preview JSON as save state.
- Creative authority and provenance: user direction overrides any assistant-generated proposal; research does not become adopted canon on retrieval alone.

## Core v3.3 review performed

Inspected the uploaded Core v3.3 archive index and its principal markdown rule headings, plus README and CMRR release note. Relevant numbered sections appear in record `design.core_reference_sections`. This validates **documentation presence**, not runtime implementation, calibration, complete historical support, or deployment readiness. Core release notes explicitly caution that numerical certification and some broader requirements remain incomplete.

## Kira source check performed

The World of Kira archive contains nine Word files: histories (Akaria, Sadion, Everwood, Kyrinus), race lists (Larius, TalmahKah), and character documents (Cathius Akarian, Daniel Conver file / Daniel Convor text, Kieran Pelleas). Sources are not edited. The campaign entry refers to existing lore without silently adjudicating naming or chronology conflicts. Preserve exact originals and conduct separate canon reconciliation.

## Nonnegotiable test interface

Every finished experience must pass feasibility and player agency checks, time/state accounting, autonomous actors, resource conservation, no double losses, historical or setting coherence, and peaceful/resolved outcomes where plausible. Tiers are cumulative in **breadth and interactions**, not exclusive mechanics. Any missing broadly reusable mechanic is a proposed Core contribution via CMRR, not campaign-local Core duplication.

## Editorial safety and historical care

- For `First Encounters`, research specific Indigenous nations and seek appropriate Indigenous cultural input; do not model North America as vacant land.
- For historical settings generally, date, cultural names, institutions and technology require verification before publication.
- For criminal/horror campaigns, treat violence as player-contingent scenario content, not mandatory player conduct.
