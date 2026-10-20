# IRGS — PRD

## Original problem statement
IRGS: a playable simulation engine with accounts, AI voice and media, and a content store. It builds on the uploaded Codex repo and patch. Phase 1 covers: Google and email/password accounts; a Content Library and Store (PayPal, Paystack, Razorpay); character creation (attributes, background, inventory, AI or uploaded portrait); a story engine (intent → validate → resolve → commit); LLM narration (OpenAI/Gemini/Claude); voice (OpenAI TTS free, ElevenLabs as an in-app subscription, Whisper input); Jev intent classification and moderation; persistence (auto-save, manual saves, checkpoints, branching, archive/restore); the Chronicle.

## User choices
- Payments: SIMULATED checkout (MOCKED) until the user provides PayPal, Paystack and Razorpay keys
- Voice: OpenAI TTS is free. ElevenLabs Narration is a monthly subscription ($5.99) and is SIMULATED (OpenAI fallback voices) until a key is provided
- Scene images (Illustrated Chronicle): painted automatically for big moments (combat/move intents), plus a "Paint this moment" button on any event

## Architecture
- Backend (FastAPI): server.py (all /api routes), auth.py (JWT + Emergent Google session), engine.py (authoritative state), ai_services.py (narrate, jev_decide, gpt-image-1, TTS, Whisper), db.py (Mongo + Emergent object storage), seed_data.py (3 scenarios, store items, providers)
- Frontend (React 19 + Vite + Tailwind v4 + shadcn): pages Auth, AuthCallback, Library, CharacterCreator, Play, Chronicle, Saves, Store. Theme: "Living Chronicle Tome" (design_guidelines.json)
- Mongo collections: users, user_sessions, login_attempts, characters, playthroughs (with embedded state + journal), saves, files, orders, entitlements

## Implemented (Jun 2026)
- Backend complete and curl-verified: login, campaigns with premium locking, character creation, playthrough creation, an act turn (Jev + GPT narration + commit), automatic scene painting stored in object storage, checkpoint save, branching, TTS, ElevenLabs subscription gating, mocked checkout unlocking Eldoria
- Frontend: all pages written. NOT YET SCREENSHOT/E2E TESTED

## Next (P0)
- Smoke-test the frontend and run testing_agent (backend + frontend). Fix any findings
- Save /app/auth_testing.md (Google auth testing playbook)

## Backlog
- P1: real PayPal, Paystack and Razorpay checkout (keys needed); real ElevenLabs API (key needed); per-character voices
- P2: NPC autonomy, Campaign Workshop, admin AI console
