# Iteration 2 regression: iteration_1 fixes + full-cast character voices (premium)
import os
import time
import uuid
import concurrent.futures as cf
from datetime import datetime, timezone, timedelta

import pytest
import requests
from pymongo import MongoClient

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"
LONG = 240


def _s(token=None):
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    if token:
        s.headers["Authorization"] = f"Bearer {token}"
    return s


def _new_user():
    email = f"test_it2_{uuid.uuid4().hex[:8]}@example.com"
    r = requests.post(f"{API}/auth/register", json={"email": email, "password": "Passw0rd!"})
    assert r.status_code == 200, r.text
    return _s(r.json()["token"])


def _new_play(s, scenario="hyw-1415"):
    camp = s.get(f"{API}/campaigns/{scenario}").json()
    bg = camp["character_backgrounds"][0]
    r = s.post(f"{API}/characters", json={"scenario_id": scenario, "name": "Codex Draft",
                                          "background_id": bg["id"], "attributes": bg["attributes"]})
    assert r.status_code == 200, r.text
    r = s.post(f"{API}/playthroughs", json={"character_id": r.json()["character_id"]})
    assert r.status_code == 200, r.text
    return r.json()


@pytest.fixture(scope="module")
def admin():
    r = requests.post(f"{API}/auth/login", json={"email": "admin@irgs.app", "password": "chronicle123"})
    if r.status_code != 200:
        pytest.skip("admin login failed")
    return _s(r.json()["token"])


@pytest.fixture(scope="module")
def player():
    return _new_user()


@pytest.fixture(scope="module")
def mongo():
    from dotenv import dotenv_values
    env = dotenv_values("/app/backend/.env")
    return MongoClient(env["MONGO_URL"])[env["DB_NAME"]]


# (e) register validation
class TestRegisterValidation:
    def test_bad_email(self):
        r = requests.post(f"{API}/auth/register", json={"email": "not-an-email", "password": "Passw0rd!"})
        assert r.status_code == 400 and "email" in r.json()["detail"].lower()

    def test_short_password(self):
        r = requests.post(f"{API}/auth/register", json={"email": f"t_{uuid.uuid4().hex[:6]}@ex.com", "password": "123"})
        assert r.status_code == 400 and "6" in r.json()["detail"]


# (c) settings validation
class TestSettingsValidation:
    def test_unknown_engine_and_voice(self, player):
        pt = _new_play(player)
        pid = pt["playthrough_id"]
        assert player.patch(f"{API}/playthroughs/{pid}/settings", json={"voice_engine": "bogus"}).status_code == 400
        assert player.patch(f"{API}/playthroughs/{pid}/settings", json={"narrator_voice": "zzz"}).status_code == 400
        assert player.patch(f"{API}/playthroughs/{pid}/settings", json={"narrator_voice": "el-bard"}).status_code == 400
        r = player.patch(f"{API}/playthroughs/{pid}/settings", json={"narrator_voice": "onyx"})
        assert r.status_code == 200 and r.json()["narrator_voice"] == "onyx"
        assert player.get(f"{API}/playthroughs/{pid}").json()["narrator_voice"] == "onyx"


# (d) non-premium gating + downgrade, cancel keeps entitlement until expiry
class TestPremiumGating:
    def test_non_premium(self, player):
        pt = _new_play(player)
        pid = pt["playthrough_id"]
        r = player.post(f"{API}/voice/tts", json={"text": "Hello there.", "engine": "elevenlabs", "voice": "el-bard"}, timeout=LONG)
        assert r.status_code == 200, r.text
        d = r.json()
        assert d["downgraded"] is True and d["engine"] == "openai" and len(d["audio_base64"]) > 100
        eid = pt["chronicle"][-1]["id"] if pt["chronicle"] else pt["view"].get("last_event_id")
        ev = player.post(f"{API}/playthroughs/{pid}/events/{eid}/voice", timeout=LONG)
        assert ev.status_code == 402
        name = list(pt["voice_cast"].keys())[0]
        assert player.patch(f"{API}/playthroughs/{pid}/settings", json={"voice_cast": {name: "nova"}}).status_code == 402
        assert player.patch(f"{API}/playthroughs/{pid}/settings", json={"voice_engine": "elevenlabs"}).status_code == 402

    def test_cancel_keeps_active(self):
        s = _new_user()
        r = s.post(f"{API}/store/checkout", json={"item_id": "sub-elevenlabs-narration", "provider": "paypal"})
        assert r.status_code == 200
        assert s.post(f"{API}/store/subscriptions/sub-elevenlabs-narration/cancel").status_code == 200
        ents = s.get(f"{API}/store/entitlements").json()
        e = next(x for x in ents if x["item_id"] == "sub-elevenlabs-narration")
        assert e["cancelled"] is True and e["active"] is True
        assert datetime.fromisoformat(e["expires_at"]) > datetime.now(timezone.utc) + timedelta(days=29)
        assert s.get(f"{API}/voice/options").json()["premium_active"] is True
        # re-buy while active is rejected
        assert s.post(f"{API}/store/checkout", json={"item_id": "sub-elevenlabs-narration", "provider": "paypal"}).status_code == 400


# NEW full-cast voices (premium subscriber)
class TestFullCast:
    def test_cast_flow(self):
        s = _new_user()
        assert s.post(f"{API}/store/checkout", json={"item_id": "sub-elevenlabs-narration", "provider": "paypal"}).status_code == 200
        pt = _new_play(s)
        pid = pt["playthrough_id"]
        r = s.patch(f"{API}/playthroughs/{pid}/settings", json={"voice_engine": "elevenlabs", "narrator_voice": "el-chronicler"})
        assert r.status_code == 200, r.text
        cast = r.json()["voice_cast"]
        assert "Codex Draft" in cast and len(cast) >= 2
        assert s.patch(f"{API}/playthroughs/{pid}/settings", json={"voice_cast": {"Nobody": "nova"}}).status_code == 400
        assert s.patch(f"{API}/playthroughs/{pid}/settings", json={"voice_cast": {"Codex Draft": "zzz"}}).status_code == 400
        r = s.patch(f"{API}/playthroughs/{pid}/settings", json={"voice_cast": {"Codex Draft": "echo"}})
        assert r.status_code == 200 and r.json()["voice_cast"]["Codex Draft"] == "echo"
        assert s.get(f"{API}/playthroughs/{pid}").json()["voice_cast"]["Codex Draft"] == "echo"
        a = s.post(f"{API}/playthroughs/{pid}/act", json={"declaration": 'I say aloud, "We sail at dawn, friends!"'}, timeout=LONG)
        assert a.status_code == 200, a.text
        eid = a.json()["event_id"]
        t0 = time.time()
        v = s.post(f"{API}/playthroughs/{pid}/events/{eid}/voice", timeout=LONG)
        t1 = time.time() - t0
        assert v.status_code == 200, v.text
        d = v.json()
        assert d["mocked"] is True and d["audio_url"].startswith("/api/files/") and d["audio_url"].endswith(".mp3")
        assert isinstance(d["speakers"], list) and len(d["speakers"]) >= 1
        print("speakers", d["speakers"], "first call", round(t1, 1))
        f = requests.get(f"{BASE_URL}{d['audio_url']}", timeout=60)
        assert f.status_code == 200 and f.headers["content-type"].startswith("audio/mpeg") and len(f.content) > 1000
        t0 = time.time()
        v2 = s.post(f"{API}/playthroughs/{pid}/events/{eid}/voice", timeout=LONG)
        t2 = time.time() - t0
        print("second call", round(t2, 2))
        assert v2.status_code == 200 and v2.json()["audio_url"] == d["audio_url"]
        assert t2 < 3
        # changing cast invalidates cache
        s.patch(f"{API}/playthroughs/{pid}/settings", json={"voice_cast": {"Codex Draft": "nova"}})
        v3 = s.post(f"{API}/playthroughs/{pid}/events/{eid}/voice", timeout=LONG)
        assert v3.status_code == 200 and v3.json()["audio_url"] != d["audio_url"]
        assert s.post(f"{API}/playthroughs/{pid}/events/nope/voice", timeout=LONG).status_code == 404


# (a) act/paint race + 409, (b) stale paint restart, (g) JPEG
class TestPaintRace:
    def test_move_then_act_keeps_image(self, player, mongo):
        pt = _new_play(player)
        pid = pt["playthrough_id"]
        a = player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I march down to the docks of Southampton Water."}, timeout=LONG)
        assert a.status_code == 200, a.text
        eid = a.json()["event_id"]
        intent = a.json()["decision"]["intent"]
        print("intent", intent)
        b = player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I look around at the ships."}, timeout=LONG)
        assert b.status_code == 200, b.text
        if intent not in ("move", "combat"):
            pytest.skip(f"classifier returned {intent}; no paint")
        status = None
        for _ in range(60):
            ev = next(e for e in player.get(f"{API}/playthroughs/{pid}/chronicle").json() if e["id"] == eid)
            status = ev.get("image_status")
            if status in ("ready", "failed"):
                break
            time.sleep(4)
        assert status == "ready", status
        img = requests.get(f"{BASE_URL}{ev['image_url']}", timeout=60)
        assert img.status_code == 200 and img.headers["content-type"] == "image/jpeg" and img.content[:2] == b"\xff\xd8"
        print("jpeg size KB", len(img.content) // 1024)

    def test_concurrent_act_409(self, player):
        pt = _new_play(player)
        pid = pt["playthrough_id"]

        def go(t):
            return player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": t}, timeout=LONG).status_code
        with cf.ThreadPoolExecutor(2) as ex:
            f1 = ex.submit(go, "I wait quietly.")
            time.sleep(1.5)
            f2 = ex.submit(go, "I hum a tune.")
            codes = sorted([f1.result(), f2.result()])
        print("codes", codes)
        assert codes == [200, 409]

    def test_stale_paint_restart(self, player, mongo):
        pt = _new_play(player)
        pid = pt["playthrough_id"]
        eid = pt["chronicle"][-1]["id"]
        old = (datetime.now(timezone.utc) - timedelta(seconds=600)).isoformat()
        mongo.playthroughs.update_one({"playthrough_id": pid},
                                      {"$set": {"state.journal.$[e].image_status": "painting",
                                                "state.journal.$[e].painting_started_at": old}},
                                      array_filters=[{"e.id": eid}])
        r = player.post(f"{API}/playthroughs/{pid}/events/{eid}/paint")
        assert r.status_code == 200 and r.json()["status"] == "painting"
        doc = mongo.playthroughs.find_one({"playthrough_id": pid})
        ev = next(e for e in doc["state"]["journal"] if e["id"] == eid)
        assert ev["painting_started_at"] != old
        fresh = ev["painting_started_at"]
        r = player.post(f"{API}/playthroughs/{pid}/events/{eid}/paint")
        doc = mongo.playthroughs.find_one({"playthrough_id": pid})
        ev = next(e for e in doc["state"]["journal"] if e["id"] == eid)
        assert ev["painting_started_at"] == fresh  # fresh painting not restarted


# (f) fantasy calendar increments
class TestCalendar:
    def test_eldoria_wraps(self, admin):
        pt = _new_play(admin, "eldoria-shadows")
        pid = pt["playthrough_id"]
        assert pt["view"]["campaign_time"]["date"] == "0000-00-03"
        for t in ("I rest by the fire.", "I sleep until morning."):
            r = admin.post(f"{API}/playthroughs/{pid}/act", json={"declaration": t}, timeout=LONG)
            assert r.status_code == 200, r.text
        ct = r.json()["playthrough"]["view"]["campaign_time"]
        print(ct)
        assert ct["date"] == "0000-00-04" and ct["time"] == "dawn"
