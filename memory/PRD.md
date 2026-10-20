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

## Backlog
- P1: real PayPal, Paystack and Razorpay checkout (keys needed); real ElevenLabs API (key needed)
- P2: NPC autonomy, Campaign Workshop, admin AI console; split server.py into routers
