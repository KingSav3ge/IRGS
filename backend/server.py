import io
import os
import secrets
import base64
import copy
import asyncio
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, List

from fastapi import FastAPI, APIRouter, HTTPException, Request, Response, UploadFile, File, Depends
from fastapi.responses import Response as RawResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db import db, client, now_iso, new_id, init_storage, put_object, get_object, MIME_TYPES, APP_NAME
import auth
import engine
import ai_services as ai
from storybook import build_storybook
from seed_data import SCENARIOS, STORE_ITEMS, PAYMENT_PROVIDERS, HYW_CATALOGUE, HYW_BASELINE, CATALOGUE_V05, CATALOGUE_TO_SCENARIO, catalogue_theme

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("irgs.server")

app = FastAPI(title="IRGS")
api = APIRouter(prefix="/api")

SCENARIO_MAP = {s["id"]: s for s in SCENARIOS}
STORE_MAP = {i["id"]: i for i in STORE_ITEMS}
BIG_MOMENT_INTENTS = {"combat", "move"}
PAINT_STALE_SECONDS = 180
_locks: Dict[str, asyncio.Lock] = {}
_acting: set = set()
_bg_tasks: set = set()


def _lock(pid: str) -> asyncio.Lock:
    return _locks.setdefault(pid, asyncio.Lock())


def _spawn(coro):
    task = asyncio.create_task(coro)
    _bg_tasks.add(task)
    task.add_done_callback(_bg_tasks.discard)


# ---------------------------------------------------------------- models
class RegisterIn(BaseModel):
    email: str
    password: str
    name: Optional[str] = None


class LoginIn(BaseModel):
    email: str
    password: str


class GoogleSessionIn(BaseModel):
    session_id: str


class CharacterIn(BaseModel):
    scenario_id: str
    name: str
    background_id: str
    attributes: Dict[str, int]
    inventory: List[dict] = []
    description: str = ""
    testimony: Dict[str, str] = {}


class PortraitGenIn(BaseModel):
    prompt: Optional[str] = None


class PlaythroughIn(BaseModel):
    character_id: str
    provider: Optional[str] = None
    model: Optional[str] = None


class ActIn(BaseModel):
    declaration: str
    request_id: Optional[str] = None
    provider: Optional[str] = None
    model: Optional[str] = None


class SettingsIn(BaseModel):
    provider: Optional[str] = None
    model: Optional[str] = None
    narrator_voice: Optional[str] = None
    voice_engine: Optional[str] = None
    voice_cast: Optional[Dict[str, str]] = None


class SaveIn(BaseModel):
    label: Optional[str] = None
    kind: str = "manual"


class BranchIn(BaseModel):
    title: Optional[str] = None


class PassTimeIn(BaseModel):
    span: str
    request_id: Optional[str] = None


class NoteIn(BaseModel):
    kind: str = "note"
    title: str
    body: str = ""
    entity_ids: List[str] = []
    event_id: Optional[str] = None


class NotePatch(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    entity_ids: Optional[List[str]] = None


class GoalIn(BaseModel):
    title: str


class GoalPatch(BaseModel):
    status: str


class ReviewIn(BaseModel):
    declaration: str


class ShareIn(BaseModel):
    mode: str = "snapshot"


class TTSIn(BaseModel):
    text: str
    voice: Optional[str] = None
    engine: str = "openai"


class CheckoutIn(BaseModel):
    item_id: str
    provider: str


# ---------------------------------------------------------------- helpers
def _set_cookie(response: Response, name: str, value: str):
    response.set_cookie(name, value, httponly=True, secure=True, samesite="lax",
                        max_age=7 * 24 * 3600, path="/")


async def _entitlements(user_id: str) -> List[dict]:
    docs = await db.entitlements.find({"user_id": user_id}, {"_id": 0}).to_list(500)
    now = datetime.now(timezone.utc)
    out = []
    for d in docs:
        exp = d.get("expires_at")
        d["active"] = (not exp) or datetime.fromisoformat(exp) > now
        out.append(d)
    return out


async def _owns_scenario(user: dict, scenario: dict) -> bool:
    if not scenario.get("premium") or user.get("role") == "admin":
        return True
    ents = await _entitlements(user["user_id"])
    return any(e["active"] and e.get("scenario_id") == scenario["id"] for e in ents)


async def _has_premium_voice(user: dict) -> bool:
    if user.get("role") == "admin":
        return True
    ents = await _entitlements(user["user_id"])
    return any(e["active"] and e["item_id"] == "sub-elevenlabs-narration" for e in ents)


def _scenario_card(s: dict, locked: bool) -> dict:
    keys = ["id", "campaign_id", "title", "campaign_title", "genre", "era", "difficulty", "premium",
            "price", "tags", "cover_image", "summary", "briefing", "opening", "character_backgrounds",
            "default_inventory", "actors", "theme", "sources", "unknowns", "entry_catalogue", "catalogue"]
    card = {k: s.get(k) for k in keys}
    card["locked"] = locked
    card["store_item_id"] = next((i["id"] for i in STORE_ITEMS if i.get("scenario_id") == s["id"]), None)
    return card


async def _get_playthrough(pid: str, user: dict) -> dict:
    doc = await db.playthroughs.find_one({"playthrough_id": pid, "user_id": user["user_id"]}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Playthrough not found")
    return doc


def _file_url(path: Optional[str]) -> Optional[str]:
    return f"/api/files/{path}" if path else None


def _narrator_fallback(doc: dict) -> str:
    v = doc.get("narrator_voice", "fable")
    el = next((e for e in ai.ELEVEN_VOICES if e["id"] == v), None)
    return el["fallback"] if el else (v if v in ai.TTS_VOICES else "fable")


def _voice_cast(doc: dict) -> Dict[str, str]:
    narrator = _narrator_fallback(doc)
    pool = [v for v in ai.TTS_VOICES if v != narrator]
    view = engine.player_view(doc["state"])
    names = [view["character"]["name"]] + [a["name"] for a in view["known_actors"]]
    cast = {n: pool[i % len(pool)] for i, n in enumerate(names)}
    cast.update({k: v for k, v in (doc.get("voice_cast") or {}).items() if k in cast})
    return cast


NPC_STALE_SECONDS = 90


def _playthrough_out(doc: dict) -> dict:
    state = doc["state"]
    if state.get("npc_pending"):
        at = state.get("npc_pending_at")
        if not at or (datetime.now(timezone.utc) - datetime.fromisoformat(at)).total_seconds() > NPC_STALE_SECONDS:
            state = {**state, "npc_pending": False}
    return {
        "playthrough_id": doc["playthrough_id"], "title": doc.get("title"),
        "scenario_id": doc["scenario_id"], "character_id": doc.get("character_id"),
        "status": doc.get("status", "active"), "provider": doc.get("provider"), "model": doc.get("model"),
        "theme": SCENARIO_MAP[doc["scenario_id"]]["theme"],
        "narrator_voice": doc.get("narrator_voice", "fable"), "voice_engine": doc.get("voice_engine", "openai"),
        "portrait_url": _file_url(doc.get("portrait_path")),
        "voice_cast": _voice_cast(doc),
        "branched_from": doc.get("branched_from"),
        "created_at": doc.get("created_at"), "updated_at": doc.get("updated_at"),
        "view": engine.player_view(state),
        "chronicle": _chronicle(state),
    }


def _chronicle(state: dict) -> list:
    entries = engine.chronicle_view(state)
    for e in entries:
        e["image_url"] = _file_url(e.get("image_path"))
    return entries


def _scene_context(state: dict, scenario: dict) -> str:
    v = engine.player_view(state)
    recent = [e for e in state.get("journal", []) if e.get("narration")][-3:]
    lines = [
        f"Campaign: {scenario['campaign_title']} — {scenario['title']} ({scenario['era']})",
        f"Setting: {scenario['opening'].get('setting', '')}",
        f"Date/time: {v['campaign_time']['date']} ({v['campaign_time']['calendar']} calendar), {v['campaign_time']['time']}",
        f"Location: {v['character']['location']}",
        f"Player character: {v['character']['name']}, {v['background']}. Condition: {v['character']['condition']}",
        f"Inventory: {', '.join(i['item'] for i in v['inventory']) or 'nothing'}",
        "Known figures: " + "; ".join(f"{a['name']} ({a['role']})" for a in v["known_actors"]),
        "World facts: " + " ".join(f["statement"] for f in v["world_facts"]),
        f"Opening briefing: {scenario['briefing']}",
    ]
    testimony = state.get("testimony") or {}
    if testimony:
        lines.append("Player testimony about their own past (the player's account; not verified world fact, grants no "
                     "skills, ranks or resources): " + "; ".join(f"{k}: {v}" for k, v in testimony.items()))
    goals = [g["title"] for g in state.get("goals", []) if g["status"] == "active"]
    if goals:
        lines.append("The player's personal goals (aspirations only; never auto-achieve them): " + "; ".join(goals))
    if scenario.get("unknowns"):
        lines.append("Deliberately unknown at the opening (do not invent as settled fact): " + " ".join(scenario["unknowns"][:6]))
    if recent:
        lines.append("Recent events:\n" + "\n".join(f"- Player: {e['declaration']}\n  Outcome: {e['narration'][:600]}" for e in recent))
    return "\n".join(lines)


def _to_jpeg(data: bytes) -> bytes:
    from PIL import Image
    img = Image.open(io.BytesIO(data)).convert("RGB")
    img.thumbnail((1280, 1280))
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=84, optimize=True)
    return buf.getvalue()


async def _store_png(user_id: str, kind: str, data: bytes, ext: str = "png") -> str:
    if ext == "png":
        data, ext = await asyncio.to_thread(_to_jpeg, data), "jpg"
    path = f"{APP_NAME}/{kind}/{user_id}/{new_id('img')}.{ext}"
    await asyncio.to_thread(put_object, path, data, MIME_TYPES.get(ext, "image/png"))
    await db.files.insert_one({"path": path, "user_id": user_id, "kind": kind,
                               "content_type": MIME_TYPES.get(ext, "image/png"), "created_at": now_iso()})
    return path


async def _set_event_image(pid: str, event_id: str, fields: dict):
    async with _lock(pid):
        await db.playthroughs.update_one(
        {"playthrough_id": pid},
            {"$set": {f"state.journal.$[e].{k}": v for k, v in fields.items()}},
            array_filters=[{"e.id": event_id}],
        )


async def _paint_event(pid: str, user_id: str, event: dict, scenario: dict):
    await _set_event_image(pid, event["id"], {"image_status": "painting", "painting_started_at": now_iso()})
    prompt = (
        f"{scenario['art_style']}, cinematic composition, no text or letters. Era: {scenario['era']}. "
        f"Setting: {scenario['opening'].get('setting', '')}. Scene: "
        f"{(event.get('narration') or event.get('text') or event.get('declaration') or '')[:700]}"
    )
    try:
        data = await ai.generate_image(prompt)
        path = await _store_png(user_id, "scenes", data)
        await _set_event_image(pid, event["id"], {"image_status": "ready", "image_path": path})
    except Exception as e:
        logger.error(f"scene painting failed: {e}")
        await _set_event_image(pid, event["id"], {"image_status": "failed"})


def _merge_images(snapshot: dict, current: dict) -> dict:
    """Carry finished scene paintings into a restored snapshot; clear stale 'painting' flags."""
    snap = copy.deepcopy(snapshot)
    snap["npc_pending"] = False
    cur = {e["id"]: e for e in current.get("journal", [])}
    for e in snap.get("journal", []):
        live = cur.get(e["id"])
        if live and live.get("image_path"):
            e["image_path"], e["image_status"] = live["image_path"], "ready"
        elif e.get("image_status") == "painting" and not (live and live.get("image_status") == "painting"):
            e["image_status"] = "failed"
    return snap


async def _autosave(doc: dict):
    state = doc["state"]
    await db.saves.update_one(
        {"playthrough_id": doc["playthrough_id"], "kind": "auto"},
        {"$set": {"user_id": doc["user_id"], "label": "Auto-save", "clock": state["clock"],
                  "campaign_time": state["campaign_time"], "state": state, "created_at": now_iso()},
         "$setOnInsert": {"save_id": new_id("save")}},
        upsert=True,
    )


def _save_out(d: dict) -> dict:
    return {k: d.get(k) for k in ("save_id", "playthrough_id", "kind", "label", "clock", "campaign_time", "created_at")}


# ---------------------------------------------------------------- auth
@api.get("/")
async def root():
    return {"app": "IRGS", "version": "3.3.E", "line": "Emergent continuation of Core 3.3 (website & app)", "engine_reference": "3.3.C (Codex engine line)", "status": "ok"}


@api.post("/auth/register")
async def register(body: RegisterIn, response: Response):
    user, token = await auth.register_user(body.email, body.password, body.name)
    _set_cookie(response, "access_token", token)
    return {"user": user, "token": token}


@api.post("/auth/login")
async def login(body: LoginIn, response: Response):
    user, token = await auth.login_user(body.email, body.password)
    _set_cookie(response, "access_token", token)
    return {"user": user, "token": token}


@api.post("/auth/google/session")
async def google_session(body: GoogleSessionIn, response: Response):
    user, token = await auth.process_google_session(body.session_id)
    _set_cookie(response, "session_token", token)
    return {"user": user, "token": token}


@api.get("/auth/me")
async def me(user: dict = Depends(auth.get_current_user)):
    return user


@api.post("/auth/logout")
async def logout(request: Request, response: Response):
    token = request.cookies.get("session_token")
    if token:
        await db.user_sessions.delete_one({"session_token": token})
    response.delete_cookie("access_token", path="/", secure=True, samesite="lax")
    response.delete_cookie("session_token", path="/", secure=True, samesite="lax")
    return {"ok": True}


# ---------------------------------------------------------------- content
@api.get("/campaigns")
async def list_campaigns(user: dict = Depends(auth.get_current_user)):
    return [_scenario_card(s, not await _owns_scenario(user, s)) for s in SCENARIOS]


@api.get("/campaigns/{scenario_id}")
async def get_campaign(scenario_id: str, user: dict = Depends(auth.get_current_user)):
    s = SCENARIO_MAP.get(scenario_id)
    if not s:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return _scenario_card(s, not await _owns_scenario(user, s))


@api.get("/catalogue")
async def catalogue(user: dict = Depends(auth.get_current_user)):
    """Content Library v0.5 (IRGS-Catalog). Players see playable records only; admins also see unreleased concepts."""
    out = []
    for r in CATALOGUE_V05["records"]:
        sid = CATALOGUE_TO_SCENARIO.get(r["catalogue_id"])
        if not sid and user.get("role") != "admin":
            continue
        p = r["public"]
        out.append({"id": r["catalogue_id"], "tier": r["tier"], "title": r["title"], "tagline": r.get("tagline"),
                    "genres": p.get("genres", []), "setting": p.get("setting_label"), "period": p.get("period_label"),
                    "synopsis": p.get("synopsis"), "status": r["catalogue_status"], "launch": r["placement"].get("release_wave"),
                    "playable": bool(sid), "scenario_id": sid, "theme": catalogue_theme(p.get("genres", []), p.get("setting_label") or "")})
    return {"version": CATALOGUE_V05["catalogue_version"], "counts": CATALOGUE_V05["counts"], "records": out}


@api.get("/campaigns/{scenario_id}/entries")
async def campaign_entries(scenario_id: str, user: dict = Depends(auth.get_current_user)):
    s = SCENARIO_MAP.get(scenario_id)
    if not s or s.get("entry_catalogue") != "hyw":
        raise HTTPException(status_code=404, detail="This campaign has a single opening")
    c = HYW_CATALOGUE
    entries = [{**e, "playable": e["year"] == 1415, "scenario_id": "hyw-1415" if e["year"] == 1415 else None}
               for e in c["entries"]]
    return {"title": c["title"], "period": c["period"], "status": c["status"], "count_note": c.get("count_note"),
            "featured_years": c.get("featured_years", []), "periods": c["periods"], "entries": entries}


@api.get("/playthroughs/{pid}/history-reference")
async def history_reference(pid: str, user: dict = Depends(auth.get_current_user)):
    """Read-only comparison with the recorded history; never executes or schedules anything."""
    doc = await _get_playthrough(pid, user)
    if doc["scenario_id"] != "hyw-1415":
        return {"available": False}
    b = HYW_BASELINE
    return {"available": True, "note": b["note"], "calendar_note": b.get("calendar_note"), "status": b["status"],
            "current_date": doc["state"]["campaign_time"]["date"],
            "events": [{"id": e["id"], "title": e["title"], "date": e["date"].get("start"), "description": e["description"],
                        "classification": e["classification"],
                        "recorded_outcome": (e.get("historical_outcome_reference") or {}).get("statement")} for e in b["events"]],
            "sources": [{k: x.get(k) for k in ("id", "title", "url")} for x in b["sources"]]}


@api.get("/ai/providers")
async def providers():
    return {"providers": ai.PROVIDERS, "default_provider": ai.DEFAULT_PROVIDER, "default_model": ai.DEFAULT_MODEL}


# ---------------------------------------------------------------- characters & files
@api.post("/characters")
async def create_character(body: CharacterIn, user: dict = Depends(auth.get_current_user)):
    s = SCENARIO_MAP.get(body.scenario_id)
    if not s:
        raise HTTPException(status_code=404, detail="Campaign not found")
    if not await _owns_scenario(user, s):
        raise HTTPException(status_code=402, detail="This campaign must be unlocked in the Store first")
    bg = next((b for b in s["character_backgrounds"] if b["id"] == body.background_id), None)
    if not bg:
        raise HTTPException(status_code=400, detail="Unknown background")
    if not body.name.strip():
        raise HTTPException(status_code=400, detail="Name is required")
    attrs = {k: max(1, min(10, int(v))) for k, v in body.attributes.items()}
    if sum(attrs.values()) > sum(bg["attributes"].values()) + 4:
        raise HTTPException(status_code=400, detail="Attribute points exceed the allowed budget")
    doc = {
        "character_id": new_id("char"), "user_id": user["user_id"], "scenario_id": s["id"],
        "name": body.name.strip()[:60], "background_id": bg["id"], "background_label": bg["label"],
        "attributes": attrs, "inventory": body.inventory or copy.deepcopy(s["default_inventory"]),
        "description": body.description[:600], "portrait_path": None, "created_at": now_iso(),
        "testimony": {k: str(v).strip()[:800] for k, v in body.testimony.items() if k in ("origin", "family", "career") and str(v).strip()},
    }
    await db.characters.insert_one(doc)
    doc.pop("_id", None)
    return {**doc, "portrait_url": None}


def _char_out(d: dict) -> dict:
    d = {k: v for k, v in d.items() if k != "_id"}
    d["portrait_url"] = _file_url(d.get("portrait_path"))
    return d


@api.get("/characters")
async def list_characters(user: dict = Depends(auth.get_current_user)):
    docs = await db.characters.find({"user_id": user["user_id"]}, {"_id": 0}).sort("created_at", -1).to_list(200)
    return [_char_out(d) for d in docs]


async def _get_character(cid: str, user: dict) -> dict:
    doc = await db.characters.find_one({"character_id": cid, "user_id": user["user_id"]}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Character not found")
    return doc


@api.post("/characters/{cid}/portrait")
async def upload_portrait(cid: str, file: UploadFile = File(...), user: dict = Depends(auth.get_current_user)):
    await _get_character(cid, user)
    ext = (file.filename or "x.png").rsplit(".", 1)[-1].lower()
    if ext not in MIME_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported image type")
    data = await file.read(8 * 1024 * 1024 + 1)
    if len(data) > 8 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Image too large (max 8MB)")
    try:
        path = await _store_png(user["user_id"], "portraits", data, ext)
    except Exception as e:
        logger.error(f"portrait upload storage failed: {e}")
        raise HTTPException(status_code=502, detail="Could not store the portrait, please try again")
    await db.characters.update_one({"character_id": cid}, {"$set": {"portrait_path": path}})
    return {"portrait_url": _file_url(path)}


@api.post("/characters/{cid}/portrait/generate")
async def generate_portrait(cid: str, body: PortraitGenIn, user: dict = Depends(auth.get_current_user)):
    ch = await _get_character(cid, user)
    s = SCENARIO_MAP[ch["scenario_id"]]
    prompt = (
        f"A dramatic chest-up character portrait in the style of {s['art_style']}, "
        f"moody background, no text. Era: {s['era']}. Character: {ch['name']}, a {ch['background_label']}. "
        f"{body.prompt or ch.get('description') or ''}"
    )
    try:
        data = await ai.generate_image(prompt[:1500])
        path = await _store_png(user["user_id"], "portraits", data)
    except Exception as e:
        logger.error(f"portrait generation failed: {e}")
        raise HTTPException(status_code=502, detail="Portrait generation failed, please try again")
    await db.characters.update_one({"character_id": cid}, {"$set": {"portrait_path": path}})
    return {"portrait_url": _file_url(path)}


@api.get("/files/{path:path}")
async def serve_file(path: str):
    rec = await db.files.find_one({"path": path, "is_deleted": {"$ne": True}}, {"_id": 0})
    if not rec:
        raise HTTPException(status_code=404, detail="File not found")
    data, ctype = await asyncio.to_thread(get_object, path)
    return RawResponse(content=data, media_type=rec.get("content_type", ctype),
                       headers={"Cache-Control": "public, max-age=86400"})


# ---------------------------------------------------------------- playthroughs
@api.post("/playthroughs")
async def create_playthrough(body: PlaythroughIn, user: dict = Depends(auth.get_current_user)):
    ch = await _get_character(body.character_id, user)
    s = SCENARIO_MAP[ch["scenario_id"]]
    if not await _owns_scenario(user, s):
        raise HTTPException(status_code=402, detail="This campaign must be unlocked in the Store first")
    provider, model = ai._model_for(body.provider or ai.DEFAULT_PROVIDER, body.model)
    doc = {
        "playthrough_id": new_id("play"), "user_id": user["user_id"], "scenario_id": s["id"],
        "character_id": ch["character_id"], "title": f"{ch['name']} · {s['title']}",
        "status": "active", "provider": provider, "model": model, "narrator_voice": "fable",
        "voice_engine": "openai", "portrait_path": ch.get("portrait_path"),
        "state": engine.build_initial_state(s, ch), "created_at": now_iso(), "updated_at": now_iso(),
    }
    await db.playthroughs.insert_one(doc)
    await _autosave(doc)
    return _playthrough_out(doc)


@api.get("/playthroughs")
async def list_playthroughs(status: Optional[str] = None, user: dict = Depends(auth.get_current_user)):
    q = {"user_id": user["user_id"]}
    if status:
        q["status"] = status
    docs = await db.playthroughs.find(q, {"_id": 0}).sort("updated_at", -1).to_list(200)
    out = []
    for d in docs:
        st = d["state"]
        out.append({
            "playthrough_id": d["playthrough_id"], "title": d.get("title"), "scenario_id": d["scenario_id"],
            "status": d.get("status", "active"), "theme": SCENARIO_MAP[d["scenario_id"]]["theme"], "clock": st["clock"], "campaign_time": st["campaign_time"],
            "character_name": st["actors"][st["player_actor_id"]]["name"],
            "portrait_url": _file_url(d.get("portrait_path")), "branched_from": d.get("branched_from"),
            "updated_at": d.get("updated_at"),
        })
    return out


@api.get("/playthroughs/{pid}")
async def get_playthrough(pid: str, user: dict = Depends(auth.get_current_user)):
    return _playthrough_out(await _get_playthrough(pid, user))


@api.patch("/playthroughs/{pid}/settings")
async def update_settings(pid: str, body: SettingsIn, user: dict = Depends(auth.get_current_user)):
    doc = await _get_playthrough(pid, user)
    upd = {}
    if body.provider:
        upd["provider"], upd["model"] = ai._model_for(body.provider, body.model)
    if body.voice_engine and body.voice_engine not in ("openai", "elevenlabs"):
        raise HTTPException(status_code=400, detail="Unknown voice engine")
    engine_after = body.voice_engine or doc.get("voice_engine", "openai")
    allowed = ai.TTS_VOICES if engine_after == "openai" else [v["id"] for v in ai.ELEVEN_VOICES]
    if body.narrator_voice and body.narrator_voice not in allowed:
        raise HTTPException(status_code=400, detail="Unknown narrator voice")
    if body.voice_engine:
        if body.voice_engine == "elevenlabs" and not await _has_premium_voice(user):
            raise HTTPException(status_code=402, detail="ElevenLabs Narration requires the premium subscription")
        upd["voice_engine"] = body.voice_engine
    if body.narrator_voice:
        upd["narrator_voice"] = body.narrator_voice
    if body.voice_cast is not None:
        if not await _has_premium_voice(user):
            raise HTTPException(status_code=402, detail="Character voices are part of ElevenLabs Narration")
        names = set(_voice_cast(doc))
        if any(k not in names or v not in ai.TTS_VOICES for k, v in body.voice_cast.items()):
            raise HTTPException(status_code=400, detail="Unknown character or voice in cast")
        upd["voice_cast"] = {**(doc.get("voice_cast") or {}), **body.voice_cast}
    if upd:
        await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": upd})
        doc.update(upd)
    return _playthrough_out(doc)


@api.post("/playthroughs/{pid}/act")
async def act(pid: str, body: ActIn, user: dict = Depends(auth.get_current_user)):
    replay = _replay(await _get_playthrough(pid, user), body.request_id)
    if replay:
        return replay
    if pid in _acting:
        raise HTTPException(status_code=409, detail="Your previous action is still being resolved")
    _acting.add(pid)
    try:
        async with _lock(pid):
            return await _act_locked(pid, body, user)
    finally:
        _acting.discard(pid)


def _replay(doc: dict, request_id: Optional[str]):
    """Idempotent retries: a request id already committed returns the original result."""
    if not request_id:
        return None
    eid = (doc["state"].get("request_log") or {}).get(request_id)
    if not eid:
        return None
    return {"decision": None, "event_id": eid, "replayed": True, "playthrough": _playthrough_out(doc)}


def _log_request(state: dict, request_id: Optional[str], event_id: str):
    if request_id:
        log = dict(state.get("request_log") or {})
        log[request_id[:64]] = event_id
        state["request_log"] = dict(list(log.items())[-100:])


async def _act_locked(pid: str, body: ActIn, user: dict):
    doc = await _get_playthrough(pid, user)
    replay = _replay(doc, body.request_id)
    if replay:
        return replay
    if doc.get("status") in ("archived", "trashed"):
        raise HTTPException(status_code=400, detail="This playthrough is archived. Restore it to continue.")
    state = doc["state"]
    check = engine.validate_action(state, body.declaration)
    if not check["ok"]:
        raise HTTPException(status_code=400, detail=check["reason"])
    decision = await ai.jev_decide(body.declaration)
    if not decision["allowed"]:
        raise HTTPException(status_code=422, detail=f"Declaration rejected by content moderation: {decision['reason']}")
    scenario = SCENARIO_MAP[doc["scenario_id"]]
    provider, model = ai._model_for(body.provider or doc.get("provider"), body.model or doc.get("model"))
    narration = await ai.narrate(_scene_context(state, scenario), body.declaration, decision["intent"], provider, model)
    new_state = engine.resolve_and_commit(state, body.declaration, decision["intent"], narration)
    event = new_state["journal"][-1]
    big = decision["intent"] in BIG_MOMENT_INTENTS
    event["big_moment"] = big
    event["image_status"] = "painting" if big else None
    if big:
        event["painting_started_at"] = now_iso()
    event["provider"], event["model"] = provider, model
    new_state["npc_pending"] = True
    new_state["npc_pending_at"] = now_iso()
    _log_request(new_state, body.request_id, event["id"])
    await db.playthroughs.update_one(
        {"playthrough_id": pid},
        {"$set": {"state": new_state, "provider": provider, "model": model, "updated_at": now_iso()}},
    )
    doc.update({"state": new_state, "provider": provider, "model": model})
    await _autosave(doc)
    if big:
        _spawn(_paint_event(pid, user["user_id"], event, scenario))
    _spawn(_npc_turn(pid, scenario, new_state, event))
    return {"decision": decision, "event_id": event["id"], "playthrough": _playthrough_out(doc)}


async def _npc_turn(pid: str, scenario: dict, state: dict, event: dict, elapsed: str = ""):
    """Living Characters: NPCs react between turns; the engine bounds and commits their actions."""
    view = engine.player_view(state)
    try:
        latest = (event.get("text") if elapsed else
                  f"Player declared: {event.get('declaration')}\nOutcome: {event.get('narration')}")
        plan = await ai.npc_turn(_scene_context(state, scenario), latest, view["known_actors"],
                                 [loc.get("name", k) for k, loc in state.get("locations", {}).items()], elapsed)
    except Exception as e:
        logger.error(f"npc turn crashed: {e}")
        plan = {"scope": "local", "actions": []}
    async with _lock(pid):
        doc = await db.playthroughs.find_one({"playthrough_id": pid}, {"_id": 0})
        if not doc:
            return
        new_state = doc["state"]
        same_turn = new_state.get("clock") == state["clock"] and any(e["id"] == event["id"] for e in new_state["journal"])
        if same_turn:
            try:
                new_state = engine.apply_npc_actions(new_state, plan["actions"], plan["scope"])
            except Exception as e:
                logger.error(f"npc apply failed: {e}")
        new_state["npc_pending"] = False
        await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": {"state": new_state}})
        doc["state"] = new_state
        await _autosave(doc)


@api.post("/playthroughs/{pid}/review")
async def review_action(pid: str, body: ReviewIn, user: dict = Depends(auth.get_current_user)):
    """Review your action: classify and validate a declaration WITHOUT committing anything."""
    doc = await _get_playthrough(pid, user)
    if doc.get("status") != "active":
        raise HTTPException(status_code=400, detail="Restore this playthrough to continue.")
    check = engine.validate_action(doc["state"], body.declaration)
    if not check["ok"]:
        return {"ok": False, "reason": check["reason"]}
    decision = await ai.jev_decide(body.declaration)
    if not decision["allowed"]:
        return {"ok": False, "reason": f"Content moderation would reject this: {decision['reason']}"}
    return {"ok": True, "intent": decision["intent"], "big_moment": decision["intent"] in BIG_MOMENT_INTENTS,
            "time_note": "Time advances by about one part of the day when this commits.",
            "others_may_react": True}


@api.post("/playthroughs/{pid}/trash")
async def trash_playthrough(pid: str, user: dict = Depends(auth.get_current_user)):
    await _get_playthrough(pid, user)
    await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": {"status": "trashed", "trashed_at": now_iso(), "updated_at": now_iso()}})
    return {"status": "trashed"}


@api.delete("/playthroughs/{pid}")
async def delete_playthrough(pid: str, user: dict = Depends(auth.get_current_user)):
    doc = await _get_playthrough(pid, user)
    if doc.get("status") != "trashed":
        raise HTTPException(status_code=400, detail="Move the campaign to Trash before deleting it permanently")
    q = {"playthrough_id": pid, "user_id": user["user_id"]}
    for coll in (db.saves, db.notes, db.shares):
        await coll.delete_many(q)
    await db.playthroughs.delete_one(q)
    return {"ok": True}


@api.post("/playthroughs/{pid}/pass-time")
async def pass_time(pid: str, body: PassTimeIn, user: dict = Depends(auth.get_current_user)):
    if body.span not in engine.TIME_SPANS:
        raise HTTPException(status_code=400, detail="span must be hours, day or week")
    replay = _replay(await _get_playthrough(pid, user), body.request_id)
    if replay:
        return replay
    if pid in _acting:
        raise HTTPException(status_code=409, detail="Your previous action is still being resolved")
    _acting.add(pid)
    try:
        async with _lock(pid):
            doc = await _get_playthrough(pid, user)
            replay = _replay(doc, body.request_id)
            if replay:
                return replay
            if doc.get("status") in ("archived", "trashed"):
                raise HTTPException(status_code=400, detail="This playthrough is archived. Restore it to continue.")
            try:
                new_state = engine.pass_time(doc["state"], body.span)
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
            new_state["npc_pending"], new_state["npc_pending_at"] = True, now_iso()
            _log_request(new_state, body.request_id, new_state["journal"][-1]["id"])
            await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": {"state": new_state, "updated_at": now_iso()}})
            doc["state"] = new_state
            await _autosave(doc)
    finally:
        _acting.discard(pid)
    event = new_state["journal"][-1]
    _spawn(_npc_turn(pid, SCENARIO_MAP[doc["scenario_id"]], new_state, event, engine.TIME_SPANS[body.span]["label"]))
    return {"event_id": event["id"], "playthrough": _playthrough_out(doc)}


@api.post("/playthroughs/{pid}/events/{event_id}/paint")
async def paint_event(pid: str, event_id: str, user: dict = Depends(auth.get_current_user)):
    doc = await _get_playthrough(pid, user)
    event = next((e for e in doc["state"]["journal"] if e["id"] == event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    started = event.get("painting_started_at")
    fresh = started and (datetime.now(timezone.utc) - datetime.fromisoformat(started)).total_seconds() < PAINT_STALE_SECONDS
    if event.get("image_status") == "painting" and fresh:
        return {"status": "painting"}
    await _set_event_image(pid, event_id, {"image_status": "painting", "painting_started_at": now_iso()})
    _spawn(_paint_event(pid, user["user_id"], event, SCENARIO_MAP[doc["scenario_id"]]))
    return {"status": "painting"}


@api.get("/playthroughs/{pid}/chronicle")
async def chronicle(pid: str, user: dict = Depends(auth.get_current_user)):
    doc = await _get_playthrough(pid, user)
    return _chronicle(doc["state"])


@api.post("/playthroughs/{pid}/archive")
async def archive(pid: str, user: dict = Depends(auth.get_current_user)):
    await _get_playthrough(pid, user)
    await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": {"status": "archived", "updated_at": now_iso()}})
    return {"status": "archived"}


@api.post("/playthroughs/{pid}/restore")
async def restore(pid: str, user: dict = Depends(auth.get_current_user)):
    await _get_playthrough(pid, user)
    await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": {"status": "active", "updated_at": now_iso()},
                                                               "$unset": {"trashed_at": ""}})
    return {"status": "active"}


# ---------------------------------------------------------------- saves / checkpoints / branches
@api.post("/playthroughs/{pid}/saves")
async def create_save(pid: str, body: SaveIn, user: dict = Depends(auth.get_current_user)):
    doc = await _get_playthrough(pid, user)
    if body.kind not in ("manual", "checkpoint"):
        raise HTTPException(status_code=400, detail="kind must be manual or checkpoint")
    st = doc["state"]
    save = {
        "save_id": new_id("save"), "playthrough_id": pid, "user_id": user["user_id"], "kind": body.kind,
        "label": (body.label or ("Checkpoint" if body.kind == "checkpoint" else "Manual save")).strip()[:80],
        "clock": st["clock"], "campaign_time": st["campaign_time"], "state": st, "created_at": now_iso(),
    }
    await db.saves.insert_one(save)
    return _save_out(save)


@api.get("/playthroughs/{pid}/saves")
async def list_saves(pid: str, user: dict = Depends(auth.get_current_user)):
    await _get_playthrough(pid, user)
    docs = await db.saves.find({"playthrough_id": pid, "user_id": user["user_id"]}, {"_id": 0, "state": 0}).sort("created_at", -1).to_list(500)
    return [_save_out(d) for d in docs]


async def _get_save(sid: str, user: dict) -> dict:
    s = await db.saves.find_one({"save_id": sid, "user_id": user["user_id"]}, {"_id": 0})
    if not s:
        raise HTTPException(status_code=404, detail="Save not found")
    return s


@api.post("/saves/{sid}/load")
async def load_save(sid: str, user: dict = Depends(auth.get_current_user)):
    s = await _get_save(sid, user)
    doc = await _get_playthrough(s["playthrough_id"], user)
    cur = doc["state"]
    saved_ids = {e["id"] for e in s["state"]["journal"]}
    if any(e["id"] not in saved_ids for e in cur["journal"]):
        await db.saves.insert_one({
            "save_id": new_id("save"), "playthrough_id": doc["playthrough_id"], "user_id": user["user_id"], "kind": "safety",
            "label": f"Before restoring “{s['label']}”", "clock": cur["clock"], "campaign_time": cur["campaign_time"],
            "state": cur, "created_at": now_iso(),
        })
    state = _merge_images(s["state"], doc["state"])
    await db.playthroughs.update_one({"playthrough_id": doc["playthrough_id"]},
                                     {"$set": {"state": state, "updated_at": now_iso()}})
    doc["state"] = state
    await _autosave(doc)
    return _playthrough_out(doc)


@api.post("/saves/{sid}/branch")
async def branch_save(sid: str, body: BranchIn, user: dict = Depends(auth.get_current_user)):
    s = await _get_save(sid, user)
    parent = await _get_playthrough(s["playthrough_id"], user)
    doc = {k: v for k, v in parent.items() if k != "_id"}
    doc.update({
        "playthrough_id": new_id("play"), "state": _merge_images(s["state"], parent["state"]), "status": "active",
        "title": (body.title or f"{parent.get('title')} — branch @ turn {s['clock']}")[:120],
        "branched_from": {"playthrough_id": parent["playthrough_id"], "save_id": sid, "clock": s["clock"]},
        "created_at": now_iso(), "updated_at": now_iso(),
    })
    await db.playthroughs.insert_one(doc)
    await _autosave(doc)
    return _playthrough_out(doc)


@api.get("/saves/{sid}/preview")
async def preview_save(sid: str, user: dict = Depends(auth.get_current_user)):
    """Inspect a save before restoring it: what it contains and what would be replaced."""
    s = await _get_save(sid, user)
    doc = await _get_playthrough(s["playthrough_id"], user)
    sv, cur = s["state"], doc["state"]
    saved_ids = {e["id"] for e in sv["journal"]}
    later = [e for e in cur["journal"] if e["id"] not in saved_ids]
    view = engine.player_view(sv)
    return {
        **_save_out(s), "character": view["character"], "inventory": view["inventory"],
        "goals": sv.get("goals", []), "event_count": len(sv["journal"]),
        "last_events": [{"id": e["id"], "title": e.get("title"), "text": (e.get("narration") or e.get("text") or "")[:240],
                         "declaration": e.get("declaration")} for e in sv["journal"][-3:]],
        "current_clock": cur["clock"], "events_replaced": len(later),
        "replaced_preview": [e.get("declaration") or e.get("title") for e in later[-5:]],
    }


@api.delete("/saves/{sid}")
async def delete_save(sid: str, user: dict = Depends(auth.get_current_user)):
    s = await _get_save(sid, user)
    if s["kind"] == "auto":
        raise HTTPException(status_code=400, detail="The auto-save cannot be deleted")
    await db.saves.delete_one({"save_id": sid})
    return {"ok": True}


# ---------------------------------------------------------------- chronicle workspace: notes, entities, development, goals
NOTE_KINDS = ("note", "document")


def _note_out(d: dict) -> dict:
    return {k: d.get(k) for k in ("note_id", "kind", "title", "body", "entity_ids", "event_id", "at_clock",
                                  "campaign_date", "created_at", "updated_at")}


@api.get("/playthroughs/{pid}/notes")
async def list_notes(pid: str, user: dict = Depends(auth.get_current_user)):
    await _get_playthrough(pid, user)
    docs = await db.notes.find({"playthrough_id": pid, "user_id": user["user_id"]}, {"_id": 0}).sort("created_at", -1).to_list(500)
    return [_note_out(d) for d in docs]


@api.post("/playthroughs/{pid}/notes")
async def create_note(pid: str, body: NoteIn, user: dict = Depends(auth.get_current_user)):
    doc = await _get_playthrough(pid, user)
    if body.kind not in NOTE_KINDS or not body.title.strip():
        raise HTTPException(status_code=400, detail="A note needs a title and a kind of note or document")
    st = doc["state"]
    known = set(st["actors"]) | set(st.get("locations", {}))
    note = {"note_id": new_id("note"), "playthrough_id": pid, "user_id": user["user_id"], "kind": body.kind,
            "title": body.title.strip()[:120], "body": body.body[:8000],
            "entity_ids": [e for e in body.entity_ids if e in known], "event_id": body.event_id,
            "at_clock": st["clock"], "campaign_date": st["campaign_time"]["date"],
            "created_at": now_iso(), "updated_at": now_iso()}
    await db.notes.insert_one(note)
    return _note_out(note)


@api.patch("/notes/{nid}")
async def update_note(nid: str, body: NotePatch, user: dict = Depends(auth.get_current_user)):
    upd = {k: v for k, v in body.model_dump().items() if v is not None}
    if "entity_ids" in upd:
        note = await db.notes.find_one({"note_id": nid, "user_id": user["user_id"]}, {"_id": 0, "playthrough_id": 1})
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        st = (await _get_playthrough(note["playthrough_id"], user))["state"]
        known = set(st["actors"]) | set(st.get("locations", {}))
        upd["entity_ids"] = [e for e in upd["entity_ids"] if e in known]
    if "title" in upd and not upd["title"].strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    upd["updated_at"] = now_iso()
    res = await db.notes.find_one_and_update({"note_id": nid, "user_id": user["user_id"]}, {"$set": upd},
                                             projection={"_id": 0}, return_document=True)
    if not res:
        raise HTTPException(status_code=404, detail="Note not found")
    return _note_out(res)


@api.delete("/notes/{nid}")
async def delete_note(nid: str, user: dict = Depends(auth.get_current_user)):
    res = await db.notes.delete_one({"note_id": nid, "user_id": user["user_id"]})
    if not res.deleted_count:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"ok": True}


def _entity_events(state: dict, eid: str) -> list:
    actor = state["actors"].get(eid)
    loc = state.get("locations", {}).get(eid)
    name = (actor or loc or {}).get("name", eid)
    out = []
    for e in state["journal"]:
        text = f"{e.get('declaration') or ''} {e.get('narration') or e.get('text') or ''}"
        hit = eid in (e.get("actor_ids") or []) if actor else False
        hit = hit or (name and name.lower() in text.lower()) or (e.get("effect") or {}).get("location") == eid
        if hit:
            out.append({"id": e["id"], "at": e.get("at"), "kind": e.get("kind"), "title": e.get("title"),
                        "text": (e.get("narration") or e.get("text") or "")[:300], "declaration": e.get("declaration"),
                        "effect": e.get("effect"), "campaign_date": e.get("campaign_date"), "campaign_time": e.get("campaign_time")})
    return out


@api.get("/playthroughs/{pid}/entities")
async def list_entities(pid: str, user: dict = Depends(auth.get_current_user)):
    st = (await _get_playthrough(pid, user))["state"]
    people = [{"id": a["id"], "type": "person", "name": a["name"], "role": a.get("role", ""),
               "disposition": a.get("current", {}).get("disposition", 0), "location": a.get("current", {}).get("location"),
               "mentions": len(_entity_events(st, a["id"]))} for a in st["actors"].values() if a["id"] != st["player_actor_id"]]
    places = [{"id": k, "type": "place", "name": v.get("name", k), "role": v.get("kind", ""),
               "mentions": len(_entity_events(st, k))} for k, v in st.get("locations", {}).items()]
    return people + places


@api.get("/playthroughs/{pid}/entities/{eid}")
async def entity_history(pid: str, eid: str, user: dict = Depends(auth.get_current_user)):
    st = (await _get_playthrough(pid, user))["state"]
    if eid not in st["actors"] and eid not in st.get("locations", {}):
        raise HTTPException(status_code=404, detail="Unknown person or place")
    events = _entity_events(st, eid)
    notes = await db.notes.find({"playthrough_id": pid, "user_id": user["user_id"], "entity_ids": eid}, {"_id": 0}).to_list(100)
    trend = [{"at": e["at"], "disposition": e["effect"]["disposition"]} for e in events
             if (e.get("effect") or {}).get("disposition") is not None]
    rumours = [r for r in st.get("rumours", []) if r.get("by") == eid]
    return {"id": eid, "events": events, "notes": [_note_out(n) for n in notes], "disposition_trend": trend, "rumours": rumours}


@api.get("/playthroughs/{pid}/development")
async def development(pid: str, user: dict = Depends(auth.get_current_user)):
    st = (await _get_playthrough(pid, user))["state"]
    points = [{"at": e["at"], "date": e.get("campaign_date"), **e["condition_after"]}
              for e in st["journal"] if e.get("condition_after")]
    milestones = [{"id": e["id"], "at": e["at"], "date": e.get("campaign_date"), "text": e.get("text"),
                   "title": f"Big moment: {e['declaration'][:90]}" if e.get("big_moment") and e.get("declaration") else e.get("title")}
                  for e in st["journal"] if e.get("kind") in ("goal", "time_passes") or e.get("big_moment")]
    intents = {}
    for e in st["journal"]:
        if e.get("kind") == "player_action":
            intents[e.get("intent", "other")] = intents.get(e.get("intent", "other"), 0) + 1
    return {"points": points, "milestones": milestones, "intents": intents, "goals": st.get("goals", []),
            "testimony": st.get("testimony", {}), "attributes": st.get("attributes", {}), "background": st.get("background")}


async def _goal_commit(pid: str, user: dict, mutate):
    async with _lock(pid):
        doc = await _get_playthrough(pid, user)
        st = copy.deepcopy(doc["state"])
        title, text = mutate(st)
        st["journal"].append({"id": f"evt_{st['clock']:05d}_goal{len(st['journal'])}", "op": "goal", "kind": "goal",
                              "intent": "goal", "title": title, "text": text, "actor_ids": [st["player_actor_id"]],
                              "at": st["clock"], "status": "recorded", "campaign_date": st["campaign_time"]["date"],
                              "campaign_time": st["campaign_time"]["time"], "wall_clock": now_iso()})
        await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": {"state": st, "updated_at": now_iso()}})
        doc["state"] = st
        await _autosave(doc)
        return _playthrough_out(doc)


@api.post("/playthroughs/{pid}/goals")
async def add_goal(pid: str, body: GoalIn, user: dict = Depends(auth.get_current_user)):
    title = body.title.strip()[:160]
    if not title:
        raise HTTPException(status_code=400, detail="A goal needs a description")

    def mutate(st):
        if len([g for g in st.get("goals", []) if g["status"] == "active"]) >= 8:
            raise HTTPException(status_code=400, detail="You can hold at most 8 active goals")
        st.setdefault("goals", []).append({"id": new_id("goal"), "title": title, "status": "active",
                                           "set_at": st["clock"], "set_date": st["campaign_time"]["date"]})
        return "A personal goal is set", title
    return await _goal_commit(pid, user, mutate)


@api.patch("/playthroughs/{pid}/goals/{gid}")
async def update_goal(pid: str, gid: str, body: GoalPatch, user: dict = Depends(auth.get_current_user)):
    if body.status not in ("achieved", "abandoned", "active"):
        raise HTTPException(status_code=400, detail="status must be achieved, abandoned or active")

    def mutate(st):
        g = next((x for x in st.get("goals", []) if x["id"] == gid), None)
        if not g:
            raise HTTPException(status_code=404, detail="Goal not found")
        if body.status == "active" and g["status"] != "active" and \
                len([x for x in st.get("goals", []) if x["status"] == "active"]) >= 8:
            raise HTTPException(status_code=400, detail="You can hold at most 8 active goals")
        g["status"], g["resolved_at"] = body.status, st["clock"]
        label = {"achieved": "A personal goal is achieved", "abandoned": "A personal goal is set aside",
                 "active": "A personal goal is taken up again"}[body.status]
        return label, g["title"]
    return await _goal_commit(pid, user, mutate)


# ---------------------------------------------------------------- shareable storybook
def _share_out(d: dict) -> dict:
    return {k: d.get(k) for k in ("share_id", "playthrough_id", "mode", "active", "created_at")}


@api.post("/playthroughs/{pid}/shares")
async def create_share(pid: str, body: ShareIn, user: dict = Depends(auth.get_current_user)):
    if body.mode not in ("snapshot", "live"):
        raise HTTPException(status_code=400, detail="mode must be snapshot or live")
    doc = await _get_playthrough(pid, user)
    share = {"share_id": secrets.token_urlsafe(9), "playthrough_id": pid, "user_id": user["user_id"],
             "mode": body.mode, "active": True, "created_at": now_iso()}
    if body.mode == "snapshot":
        share["snapshot"] = build_storybook(doc, SCENARIO_MAP[doc["scenario_id"]], _file_url)
    await db.shares.insert_one(share)
    return _share_out(share)


@api.get("/playthroughs/{pid}/shares")
async def list_shares(pid: str, user: dict = Depends(auth.get_current_user)):
    await _get_playthrough(pid, user)
    docs = await db.shares.find({"playthrough_id": pid, "user_id": user["user_id"], "active": True},
                                {"_id": 0, "snapshot": 0}).sort("created_at", -1).to_list(100)
    return [_share_out(d) for d in docs]


@api.delete("/shares/{share_id}")
async def revoke_share(share_id: str, user: dict = Depends(auth.get_current_user)):
    res = await db.shares.update_one({"share_id": share_id, "user_id": user["user_id"]}, {"$set": {"active": False}})
    if not res.matched_count:
        raise HTTPException(status_code=404, detail="Share link not found")
    return {"ok": True}


@api.api_route("/s/{share_id}", methods=["GET", "HEAD"])
async def share_card(share_id: str, request: Request):
    """Link-preview page: Open Graph/Twitter meta for chat apps, then forwards people to the storybook."""
    from html import escape
    share = await db.shares.find_one({"share_id": share_id, "active": True}, {"_id": 0})
    host = request.headers.get("x-forwarded-host") or request.headers.get("host", "")
    proto = request.headers.get("x-forwarded-proto", "https")
    origin = f"{proto}://{host}"
    target = f"{origin}/story/{share_id}"
    if share:
        book = share.get("snapshot")
        if not book:
            doc = await db.playthroughs.find_one({"playthrough_id": share["playthrough_id"]}, {"_id": 0})
            book = build_storybook(doc, SCENARIO_MAP[doc["scenario_id"]], _file_url) if doc else None
    else:
        book = None
    if book:
        title = f"{book['scenario_title']} · the story of {book['character']['name']}"
        tail = "and counting" if share["mode"] == "live" else "(snapshot)"
        desc = (f"{book['campaign_title']} ({book['era']}). An illustrated IRGS storybook, "
                f"{book['turns']} turns {tail}.")
        scene = next((e["image_url"] for c in reversed(book["chapters"]) for e in reversed(c["entries"]) if e.get("image_url")), None)
        image = f"{origin}{scene}" if scene else book["cover_image"]
    else:
        title, desc, image = "IRGS storybook", "This storybook is no longer shared.", ""
    t, d, i, u = (escape(x, quote=True) for x in (title, desc, image, target))
    html = f"""<!doctype html><html><head><meta charset="utf-8"><title>{t}</title>
<meta name="description" content="{d}"><meta property="og:type" content="article"><meta property="og:site_name" content="IRGS">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{u}">
<meta property="og:image" content="{i}"><meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{i}">
<meta http-equiv="refresh" content="0;url={u}"></head><body><a href="{u}">{t}</a></body></html>"""
    return RawResponse(content=html, media_type="text/html")


@api.get("/public/stories/{share_id}")
async def public_story(share_id: str):
    share = await db.shares.find_one({"share_id": share_id, "active": True}, {"_id": 0})
    if not share:
        raise HTTPException(status_code=404, detail="This storybook is no longer shared")
    if share["mode"] == "snapshot":
        book = share["snapshot"]
    else:
        doc = await db.playthroughs.find_one({"playthrough_id": share["playthrough_id"]}, {"_id": 0})
        if not doc:
            raise HTTPException(status_code=404, detail="This storybook is no longer available")
        book = build_storybook(doc, SCENARIO_MAP[doc["scenario_id"]], _file_url)
    return {**book, "mode": share["mode"], "shared_at": share["created_at"]}


# ---------------------------------------------------------------- voice
@api.get("/voice/options")
async def voice_options(user: dict = Depends(auth.get_current_user)):
    return {
        "openai": ai.TTS_VOICES,
        "elevenlabs": ai.ELEVEN_VOICES,
        "premium_active": await _has_premium_voice(user),
        "elevenlabs_configured": bool(os.environ.get("ELEVENLABS_API_KEY")),
    }


@api.post("/voice/tts")
async def tts(body: TTSIn, user: dict = Depends(auth.get_current_user)):
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Nothing to read aloud")
    if body.engine not in ("openai", "elevenlabs"):
        raise HTTPException(status_code=400, detail="Unknown voice engine")
    mocked = False
    voice = body.voice or "fable"
    downgraded = False
    if body.engine == "elevenlabs" and not await _has_premium_voice(user):
        body.engine, voice, downgraded = "openai", "fable", True
    if body.engine == "elevenlabs":
        el = next((v for v in ai.ELEVEN_VOICES if v["id"] == voice), ai.ELEVEN_VOICES[0])
        voice = el["fallback"]
        mocked = True
    try:
        audio = await ai.tts_speak(body.text, voice)
    except Exception as e:
        logger.error(f"tts failed: {e}")
        raise HTTPException(status_code=502, detail="Narration voice is unavailable right now")
    return {"audio_base64": audio, "format": "mp3", "engine": body.engine, "mocked": mocked, "downgraded": downgraded}


@api.post("/playthroughs/{pid}/events/{event_id}/voice")
async def cast_voice(pid: str, event_id: str, user: dict = Depends(auth.get_current_user)):
    """Full-cast reading: narrator plus a distinct voice per character (premium)."""
    if not await _has_premium_voice(user):
        raise HTTPException(status_code=402, detail="Character voices are part of ElevenLabs Narration")
    doc = await _get_playthrough(pid, user)
    event = next((e for e in doc["state"]["journal"] if e["id"] == event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    text = event.get("narration") or event.get("text") or ""
    cast = _voice_cast(doc)
    narrator = _narrator_fallback(doc)
    cache_key = f"{narrator}|" + "|".join(f"{k}={v}" for k, v in sorted(cast.items()))
    if event.get("cast_audio_path") and event.get("cast_audio_key") == cache_key:
        segments = event.get("cast_segments", [])
        path = event["cast_audio_path"]
    else:
        segments = await ai.cast_segments(text, list(cast.keys()), engine.player_view(doc["state"])["character"]["name"])
        try:
            clips = await asyncio.gather(*[ai.tts_speak(sg["text"], cast.get(sg["speaker"], narrator)) for sg in segments])
        except Exception as e:
            logger.error(f"cast tts failed: {e}")
            raise HTTPException(status_code=502, detail="Narration voice is unavailable right now")
        audio = b"".join(base64.b64decode(c) for c in clips)
        path = f"{APP_NAME}/voice/{user['user_id']}/{new_id('cast')}.mp3"
        try:
            await asyncio.to_thread(put_object, path, audio, "audio/mpeg")
        except Exception as e:
            logger.error(f"cast audio storage failed: {e}")
            raise HTTPException(status_code=502, detail="Could not store the narration audio, please try again")
        await db.files.insert_one({"path": path, "user_id": user["user_id"], "kind": "voice",
                                   "content_type": "audio/mpeg", "created_at": now_iso()})
        await _set_event_image(pid, event_id, {"cast_audio_path": path, "cast_audio_key": cache_key,
                                               "cast_segments": segments})
    speakers = sorted({sg["speaker"] for sg in segments})
    return {"audio_url": _file_url(path), "speakers": [{"name": n, "voice": cast.get(n, narrator)} for n in speakers],
            "mocked": not bool(os.environ.get("ELEVENLABS_API_KEY"))}


@api.post("/voice/stt")
async def stt(file: UploadFile = File(...), user: dict = Depends(auth.get_current_user)):
    data = await file.read(25 * 1024 * 1024 + 1)
    if not data:
        raise HTTPException(status_code=400, detail="Empty recording")
    if len(data) > 25 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Recording too large (max 25MB)")
    try:
        text = await ai.stt_transcribe(data, file.filename or "audio.webm")
    except Exception as e:
        logger.error(f"stt failed: {e}")
        raise HTTPException(status_code=422, detail="Could not transcribe that recording, please try again")
    return {"text": text}


# ---------------------------------------------------------------- store (MOCKED checkout)
@api.get("/store/items")
async def store_items(user: dict = Depends(auth.get_current_user)):
    ents = await _entitlements(user["user_id"])
    owned = {e["item_id"] for e in ents if e["active"]}
    return {"items": [{**i, "owned": i["id"] in owned} for i in STORE_ITEMS], "providers": PAYMENT_PROVIDERS}


@api.post("/store/checkout")
async def checkout(body: CheckoutIn, user: dict = Depends(auth.get_current_user)):
    item = STORE_MAP.get(body.item_id)
    prov = next((p for p in PAYMENT_PROVIDERS if p["id"] == body.provider), None)
    if not item or not prov:
        raise HTTPException(status_code=400, detail="Unknown item or payment provider")
    ents = await _entitlements(user["user_id"])
    if any(e["active"] and e["item_id"] == item["id"] for e in ents):
        raise HTTPException(status_code=400, detail="You already own this")
    amount = round(item["price"] * prov.get("rate", 1), 2)
    order = {
        "order_id": new_id("order"), "user_id": user["user_id"], "item_id": item["id"], "title": item["title"],
        "provider": prov["id"], "currency": prov["currency"], "amount": amount, "status": "paid",
        "mocked": True, "created_at": now_iso(),
    }
    await db.orders.insert_one(order)
    expires = (datetime.now(timezone.utc) + timedelta(days=30)).isoformat() if item["kind"] == "subscription" else None
    await db.entitlements.update_one(
        {"user_id": user["user_id"], "item_id": item["id"]},
        {"$set": {"kind": item["kind"], "scenario_id": item.get("scenario_id"), "title": item["title"],
                  "order_id": order["order_id"], "granted_at": now_iso(), "expires_at": expires,
                  "cancelled": False}},
        upsert=True,
    )
    order.pop("_id", None)
    return {"order": order}


@api.get("/store/orders")
async def orders(user: dict = Depends(auth.get_current_user)):
    return await db.orders.find({"user_id": user["user_id"]}, {"_id": 0}).sort("created_at", -1).to_list(200)


@api.get("/store/entitlements")
async def entitlements(user: dict = Depends(auth.get_current_user)):
    return await _entitlements(user["user_id"])


@api.post("/store/subscriptions/{item_id}/cancel")
async def cancel_subscription(item_id: str, user: dict = Depends(auth.get_current_user)):
    res = await db.entitlements.update_one({"user_id": user["user_id"], "item_id": item_id, "kind": "subscription"},
                                           {"$set": {"cancelled": True}})
    if not res.matched_count:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"ok": True}


# ---------------------------------------------------------------- app wiring
app.include_router(api)
_cors_origins = [o.strip() for o in os.environ.get("CORS_ORIGINS", "").split(",") if o.strip() and o.strip() != "*"]
if _cors_origins:
    # the app is served same-origin; cross-origin access exists only for an explicit allowlist
    app.add_middleware(CORSMiddleware, allow_credentials=True, allow_origins=_cors_origins,
                       allow_methods=["*"], allow_headers=["*"])


@app.middleware("http")
async def csrf_origin_guard(request: Request, call_next):
    """Block cross-site state-changing requests that ride on the auth cookie (CSRF)."""
    if request.method not in ("GET", "HEAD", "OPTIONS") and request.cookies and \
            not request.headers.get("authorization"):
        origin = request.headers.get("origin")
        if origin:
            host = request.headers.get("x-forwarded-host") or request.headers.get("host", "")
            if origin.split("://", 1)[-1] != host and origin not in _cors_origins:
                return JSONResponse(status_code=403, content={"detail": "Cross-site request blocked"})
    return await call_next(request)


@app.on_event("startup")
async def startup():
    await auth.seed_admin()
    await db.users.create_index("email", unique=True)
    await db.users.create_index("username", unique=True, sparse=True)
    await db.login_attempts.create_index("identifier")
    await db.playthroughs.create_index("playthrough_id", unique=True)
    await db.saves.create_index("playthrough_id")
    await db.shares.create_index("share_id", unique=True)
    try:
        await asyncio.to_thread(init_storage)
    except Exception as e:
        logger.error(f"object storage init failed: {e}")


@app.on_event("shutdown")
async def shutdown():
    client.close()
