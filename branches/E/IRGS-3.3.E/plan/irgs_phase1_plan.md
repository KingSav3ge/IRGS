# IRGS Phase 1 — Execution Plan

## User choices (confirmed)
- Payments: build Content Store with SIMULATED checkout (PayPal / Paystack / Razorpay buttons → mock order → entitlement). Real providers wired later when user supplies keys.
- Voice: OpenAI TTS now; ElevenLabs added later when key is supplied (UI shows "premium voices — coming soon").
- Plan A→D: user skipped confirmation → proceed with defaults.

## Existing backend modules (done)
db.py (Mongo + object storage), auth.py (JWT + Emergent Google session, admin seed, brute force),
engine.py (build_initial_state / validate / resolve_and_commit / player_view / chronicle_view),
ai_services.py (narrate multi-provider, jev_decide, generate_image, tts_speak, stt_transcribe), seed_data.py.

## Step A — server.py (overwrite=True) + backend verification
1. Rewrite /app/backend/server.py: APIRouter prefix /api, CORS, startup (seed_admin, seed campaigns, init_storage try/except).
2. Routes:
   - Auth: POST /auth/register, /auth/login, /auth/google/session, GET /auth/me, POST /auth/logout (httpOnly cookie + token in body).
   - Content: GET /campaigns, GET /campaigns/{id} (locked flag from entitlements), GET /ai/providers.
   - Characters: POST/GET /characters, POST /characters/{id}/portrait (upload → object storage), POST /characters/{id}/portrait/generate (gpt-image-1 → storage), GET /files/{path}.
   - Playthroughs: POST /playthroughs (build_initial_state), GET /playthroughs, GET /playthroughs/{id} (player_view), POST /playthroughs/{id}/act (jev_decide → validate → narrate → resolve_and_commit → autosave), GET /playthroughs/{id}/chronicle.
   - Persistence: POST/GET /playthroughs/{id}/saves (manual / checkpoint), POST /saves/{id}/load, POST /saves/{id}/branch (new playthrough from snapshot), POST /playthroughs/{id}/archive | /restore.
   - Voice: POST /voice/tts, POST /voice/stt (multipart).
   - Store: GET /store/items, POST /store/checkout {item_id, provider} → MOCKED order + entitlement, GET /store/orders.
3. Install deps (emergentintegrations, bcrypt, pyjwt, requests) → pip freeze > requirements.txt; restart backend.
4. Test: curl register/login/me, list campaigns, create character + playthrough, one /act call (narration returns), chronicle has 2 events, save/load/branch, tts returns base64.
5. Write /app/memory/test_credentials.md (admin@irgs.app / admin123).

## Step B — Frontend ("Living Chronicle Tome", design_guidelines.json)
Use existing CRA + shadcn setup (don't migrate stack). Pages:
Landing/Login (email + Google), AuthCallback (session_id hash), Library, Campaign detail, Character Creator
(attributes, background, inventory, portrait upload/generate), Play screen (narration feed, action input,
mic → Whisper, play narration → TTS, provider picker, condition/inventory sidebar), Chronicle, Saves panel
(save/checkpoint/load/branch/archive), Store + mock checkout dialog. data-testid on all interactive elements.
Smoke screenshot once.

## Step C — Store polish
Entitlement gating of premium campaigns; order history. Label checkout as MOCKED in UI.

## Step D — testing_agent (backend + frontend), fix all findings, update PRD.md, finish.

## Deferred
Real PayPal/Paystack/Razorpay, ElevenLabs, NPC autonomy, Campaign Workshop, admin AI console.
