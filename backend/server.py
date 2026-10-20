import os
import copy
import asyncio
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, List

from fastapi import FastAPI, APIRouter, HTTPException, Request, Response, UploadFile, File, Depends
from fastapi.responses import Response as RawResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db import db, client, now_iso, new_id, init_storage, put_object, get_object, MIME_TYPES, APP_NAME
import auth
import engine
import ai_services as ai
from seed_data import SCENARIOS, STORE_ITEMS, PAYMENT_PROVIDERS

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("irgs.server")

app = FastAPI(title="IRGS")
api = APIRouter(prefix="/api")

SCENARIO_MAP = {s["id"]: s for s in SCENARIOS}
STORE_MAP = {i["id"]: i for i in STORE_ITEMS}
BIG_MOMENT_INTENTS = {"combat", "move"}


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


class PortraitGenIn(BaseModel):
    prompt: Optional[str] = None


class PlaythroughIn(BaseModel):
    character_id: str
    provider: Optional[str] = None
    model: Optional[str] = None


class ActIn(BaseModel):
    declaration: str
    provider: Optional[str] = None
    model: Optional[str] = None


class SettingsIn(BaseModel):
    provider: Optional[str] = None
    model: Optional[str] = None
    narrator_voice: Optional[str] = None
    voice_engine: Optional[str] = None


class SaveIn(BaseModel):
    label: Optional[str] = None
    kind: str = "manual"


class BranchIn(BaseModel):
    title: Optional[str] = None


class TTSIn(BaseModel):
    text: str
    voice: Optional[str] = None
    engine: str = "openai"


class CheckoutIn(BaseModel):
    item_id: str
    provider: str


# ---------------------------------------------------------------- helpers
def _set_cookie(response: Response, name: str, value: str):
    response.set_cookie(name, value, httponly=True, secure=True, samesite="none",
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
    return any(e["active"] and e.get("kind") == "subscription" for e in ents)


def _scenario_card(s: dict, locked: bool) -> dict:
    keys = ["id", "campaign_id", "title", "campaign_title", "genre", "era", "difficulty", "premium",
            "price", "tags", "cover_image", "summary", "briefing", "opening", "character_backgrounds",
            "default_inventory", "actors"]
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


def _playthrough_out(doc: dict) -> dict:
    state = doc["state"]
    return {
        "playthrough_id": doc["playthrough_id"], "title": doc.get("title"),
        "scenario_id": doc["scenario_id"], "character_id": doc.get("character_id"),
        "status": doc.get("status", "active"), "provider": doc.get("provider"), "model": doc.get("model"),
        "narrator_voice": doc.get("narrator_voice", "fable"), "voice_engine": doc.get("voice_engine", "openai"),
        "portrait_url": _file_url(doc.get("portrait_path")),
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
    if recent:
        lines.append("Recent events:\n" + "\n".join(f"- Player: {e['declaration']}\n  Outcome: {e['narration'][:600]}" for e in recent))
    return "\n".join(lines)


async def _store_png(user_id: str, kind: str, data: bytes, ext: str = "png") -> str:
    path = f"{APP_NAME}/{kind}/{user_id}/{new_id('img')}.{ext}"
    await asyncio.to_thread(put_object, path, data, MIME_TYPES.get(ext, "image/png"))
    await db.files.insert_one({"path": path, "user_id": user_id, "kind": kind,
                               "content_type": MIME_TYPES.get(ext, "image/png"), "created_at": now_iso()})
    return path


async def _set_event_image(pid: str, event_id: str, fields: dict):
    await db.playthroughs.update_one(
        {"playthrough_id": pid},
        {"$set": {f"state.journal.$[e].{k}": v for k, v in fields.items()}},
        array_filters=[{"e.id": event_id}],
    )


async def _paint_event(pid: str, user_id: str, event: dict, scenario: dict):
    await _set_event_image(pid, event["id"], {"image_status": "painting"})
    prompt = (
        "A painterly illuminated-manuscript style illustration, rich candlelit oil-painting textures, "
        f"cinematic composition, no text or letters. Era: {scenario['era']}. "
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
    return {"app": "IRGS", "status": "ok"}


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
    response.delete_cookie("access_token", path="/", secure=True, samesite="none")
    response.delete_cookie("session_token", path="/", secure=True, samesite="none")
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
    data = await file.read()
    if len(data) > 8 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Image too large (max 8MB)")
    path = await _store_png(user["user_id"], "portraits", data, ext)
    await db.characters.update_one({"character_id": cid}, {"$set": {"portrait_path": path}})
    return {"portrait_url": _file_url(path)}


@api.post("/characters/{cid}/portrait/generate")
async def generate_portrait(cid: str, body: PortraitGenIn, user: dict = Depends(auth.get_current_user)):
    ch = await _get_character(cid, user)
    s = SCENARIO_MAP[ch["scenario_id"]]
    prompt = (
        "A dramatic painted character portrait, chest-up, illuminated-manuscript meets oil painting, "
        f"dark moody background, no text. Era: {s['era']}. Character: {ch['name']}, a {ch['background_label']}. "
        f"{body.prompt or ch.get('description') or ''}"
    )
    try:
        data = await ai.generate_image(prompt[:1500])
    except Exception as e:
        logger.error(f"portrait generation failed: {e}")
        raise HTTPException(status_code=502, detail="Portrait generation failed, please try again")
    path = await _store_png(user["user_id"], "portraits", data)
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
            "status": d.get("status", "active"), "clock": st["clock"], "campaign_time": st["campaign_time"],
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
    if body.voice_engine:
        if body.voice_engine == "elevenlabs" and not await _has_premium_voice(user):
            raise HTTPException(status_code=402, detail="ElevenLabs Narration requires the premium subscription")
        upd["voice_engine"] = body.voice_engine
    if body.narrator_voice:
        upd["narrator_voice"] = body.narrator_voice
    if upd:
        await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": upd})
        doc.update(upd)
    return _playthrough_out(doc)


@api.post("/playthroughs/{pid}/act")
async def act(pid: str, body: ActIn, user: dict = Depends(auth.get_current_user)):
    doc = await _get_playthrough(pid, user)
    if doc.get("status") == "archived":
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
    event["provider"], event["model"] = provider, model
    await db.playthroughs.update_one(
        {"playthrough_id": pid},
        {"$set": {"state": new_state, "provider": provider, "model": model, "updated_at": now_iso()}},
    )
    doc.update({"state": new_state, "provider": provider, "model": model})
    await _autosave(doc)
    if big:
        asyncio.create_task(_paint_event(pid, user["user_id"], event, scenario))
    return {"decision": decision, "event_id": event["id"], "playthrough": _playthrough_out(doc)}


@api.post("/playthroughs/{pid}/events/{event_id}/paint")
async def paint_event(pid: str, event_id: str, user: dict = Depends(auth.get_current_user)):
    doc = await _get_playthrough(pid, user)
    event = next((e for e in doc["state"]["journal"] if e["id"] == event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if event.get("image_status") == "painting":
        return {"status": "painting"}
    await _set_event_image(pid, event_id, {"image_status": "painting"})
    asyncio.create_task(_paint_event(pid, user["user_id"], event, SCENARIO_MAP[doc["scenario_id"]]))
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
    await db.playthroughs.update_one({"playthrough_id": pid}, {"$set": {"status": "active", "updated_at": now_iso()}})
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
    await db.playthroughs.update_one({"playthrough_id": doc["playthrough_id"]},
                                     {"$set": {"state": s["state"], "updated_at": now_iso()}})
    doc["state"] = s["state"]
    return _playthrough_out(doc)


@api.post("/saves/{sid}/branch")
async def branch_save(sid: str, body: BranchIn, user: dict = Depends(auth.get_current_user)):
    s = await _get_save(sid, user)
    parent = await _get_playthrough(s["playthrough_id"], user)
    doc = {k: v for k, v in parent.items() if k != "_id"}
    doc.update({
        "playthrough_id": new_id("play"), "state": copy.deepcopy(s["state"]), "status": "active",
        "title": (body.title or f"{parent.get('title')} — branch @ turn {s['clock']}")[:120],
        "branched_from": {"playthrough_id": parent["playthrough_id"], "save_id": sid, "clock": s["clock"]},
        "created_at": now_iso(), "updated_at": now_iso(),
    })
    await db.playthroughs.insert_one(doc)
    await _autosave(doc)
    return _playthrough_out(doc)


@api.delete("/saves/{sid}")
async def delete_save(sid: str, user: dict = Depends(auth.get_current_user)):
    s = await _get_save(sid, user)
    if s["kind"] == "auto":
        raise HTTPException(status_code=400, detail="The auto-save cannot be deleted")
    await db.saves.delete_one({"save_id": sid})
    return {"ok": True}


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
    mocked = False
    voice = body.voice or "fable"
    if body.engine == "elevenlabs":
        if not await _has_premium_voice(user):
            raise HTTPException(status_code=402, detail="ElevenLabs Narration requires the premium subscription")
        el = next((v for v in ai.ELEVEN_VOICES if v["id"] == voice), ai.ELEVEN_VOICES[0])
        voice = el["fallback"]
        mocked = True
    try:
        audio = await ai.tts_speak(body.text, voice)
    except Exception as e:
        logger.error(f"tts failed: {e}")
        raise HTTPException(status_code=502, detail="Narration voice is unavailable right now")
    return {"audio_base64": audio, "format": "mp3", "engine": body.engine, "mocked": mocked}


@api.post("/voice/stt")
async def stt(file: UploadFile = File(...), user: dict = Depends(auth.get_current_user)):
    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="Empty recording")
    try:
        text = await ai.stt_transcribe(data, file.filename or "audio.webm")
    except Exception as e:
        logger.error(f"stt failed: {e}")
        raise HTTPException(status_code=502, detail="Could not transcribe your voice, please try again")
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
                  "order_id": order["order_id"], "granted_at": now_iso(), "expires_at": expires}},
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
                                           {"$set": {"expires_at": now_iso()}})
    if not res.matched_count:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"ok": True}


# ---------------------------------------------------------------- app wiring
app.include_router(api)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await auth.seed_admin()
    await db.users.create_index("email", unique=True)
    await db.playthroughs.create_index("playthrough_id", unique=True)
    await db.saves.create_index("playthrough_id")
    try:
        await asyncio.to_thread(init_storage)
    except Exception as e:
        logger.error(f"object storage init failed: {e}")


@app.on_event("shutdown")
async def shutdown():
    client.close()
