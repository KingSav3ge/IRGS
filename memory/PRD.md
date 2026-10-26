# IRGS — PRD

## Original problem statement
IRGS is a playable simulation engine with accounts, AI voice and media, and a content store. It builds on the uploaded Codex repo and patch. Phase 1 covers:
- Accounts: Google and email/password
- Content Library and Store: PayPal, Paystack and Razorpay checkout
- Character creation: attributes, background, inventory, AI-generated or uploaded portrait
- Story engine: intent → validate → resolve → commit
- Narration: LLM (OpenAI/Gemini/Claude)
- Voice: OpenAI TTS is free; ElevenLabs is an in-app subscription; Whisper handles voice input
- Jev: intent classification and moderation
- Persistence: auto-save, manual saves, checkpoints, branching, archive/restore
- Chronicle

## Version lines
- This app is **IRGS 3.3.E** (the Emergent continuation of Core 3.3: website/app). **3.3.C** is the Codex engine line. See memory/CODEX_332_MERGE.md

## User choices
- Payments: MOCKED (simulated checkout) until the user provides PayPal, Paystack and Razorpay keys
- Voice: OpenAI TTS is free. ElevenLabs Narration ($5.99/month subscription) is SIMULATED with OpenAI fallback voices until a key is provided. The subscription includes full-cast character voices
- Illustrated Chronicle: big moments (combat/move) are painted automatically, and any event has a "Paint this moment" button
- Visuals:
  - Main UI uses the neutral "Oxblood & Bone" ledger theme (Fraunces / Newsreader / Instrument Sans / IBM Plex Mono)
  - Each campaign has its own genre skin via data-theme: manuscript (HYW 1415), tablet stone (Rome), grimoire (Eldoria), pda (sci-fi Meridian)

## Architecture
- Backend (FastAPI): server.py, auth.py, engine.py, ai_services.py, db.py (Mongo + Emergent object storage), seed_data.py (4 scenarios + THEMES/art_style, store items, providers)
- Frontend (React 19, Vite, Tailwind v4, shadcn, react-query): Auth, AuthCallback, Library, CharacterCreator, Play, Chronicle, Saves, Store pages
- Theme tokens: CSS vars in index.css (--c-*, --f-*)
- Concurrency: a per-playthrough asyncio lock covers act and image writes; a concurrent act returns 409; stale painting restarts after 180s

## Implemented
- 2026-06: full backend and frontend, all Phase 1 flows (iteration_1: 94-95% pass, then fixes)
- 2026-06: genre themes, sci-fi campaign, JPEG image compression, race fix, settings/register validation, subscription cancel-at-period-end, fallback when TTS is downgraded, mobile nav, full-cast premium voices with cached mp3 (iteration_2: 43/43 backend, frontend pass)

- 2026-06: Living Characters (free). NPCs react between turns (disposition/move/rumour, engine-bounded, 0-2 local and up to 6 for broad news) and show in the feed, Chronicle (an 'others act' filter) and the status panel (disposition, rumours)
- 2026-06: Shareable storybook. Snapshot or live public links at /story/:id, with a genre-skinned cover and chapters, and a revoke option
- 2026-06: Genre-neutral login. A joint choice screen ("Do you have a journey to return to? Or are you setting about your first?") leads to the Sign in or Sign up form. Sign in accepts an email OR a username (admin / chronicle123, ADMIN_USERNAME in .env)
- iteration_3: 52/53 passed, then the NPC hardening fixes. Backend suite 53/53

- 2026-06: Let time pass (a few hours / a day / a week; NPCs act and rumours spread, with broad scope allowed). Rich link previews (/api/s/{id} serves OG/Twitter meta, then forwards to /story/{id}). Cinematic front page (rotating genre-skinned showcase, glass sign-in panel, features strip). Codex 3.3.2 merge: researched HYW 1415 opening, 37-entry catalogue, read-only historical record panel, player testimony, reading settings

- 2026-06: Master Instructions v1.4 work.
  - Milestone G, Chronicle workspace tabs: Timeline; People & places with entity history (disposition changes, rumours, linked notes); Notes & in-world documents; Development & goals (condition chart, intent mix, turning points, personal goals recorded as journal events)
  - Milestones C/H: idempotent act/pass-time via request_id (replay, one safe client retry); save preview (contents and the number of events that would be replaced); a safety save before any load that would replace events
  - Marketplace placeholder page (Stage Three)
  - Branches compared: 3.3.C is identical to the 3.3.2 merge; 3.3.E is this codebase. iteration_5: 91/93, then fixes; pytest 93/93

- 2026-06: Security audit fixes. No credentialed CORS (the app adds CORSMiddleware only for an explicit allowlist); csrf_origin_guard blocks cookie-only cross-site writes; SameSite=lax; STT 25MB cap (422 on bad audio); admin seed fails closed. Verified in iteration_7
- 2026-06: IRGS 3.4.1 repo integration (github KingSav3ge/IRGS-APP-WEB, IRGS-Catalog, IRGS-Engine, IRGS; cloned to /app/upstream)
  - Content Library v0.5 (44 records, backend/data/catalogue_v0_5.json; players see playable only: MC-01→hyw-1415; admins see all concepts)
  - Review your action (POST /review, no commit) with Confirm/Edit/Withdraw, and "Check / retry saved request" (localStorage + idempotent request_id)
  - Campaign Trash (trash/restore/delete forever)
  - 3.4.1 genre looks: military, shinobi, settlement themes
  - The jev "understandable" gibberish gate
  - Image generation switched to Gemini Nano Banana (gemini-3.1-flash-image-preview), because gpt-image-1 and dall-e-3 were rejected by the proxy
  - iteration_7: 129/133 (image outage + gibberish, both fixed after it and verified only by direct calls, NOT re-run through the testing agent)

## Backlog
- P1: real PayPal, Paystack and Razorpay checkout (keys needed); real ElevenLabs API (key needed)
- P1 (instructions v1.4): My Campaigns hub + Account/Admin nav (Milestone B); Quick/Guided/Detailed creation (E); World workspace: Atlas, Economy, Politics, Military (I)
- P2: Campaign Workshop (Stage 2), Marketplace for real (Stage 3), AI Network console (backend-only, deferred); split server.py into routers
