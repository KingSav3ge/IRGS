# Iteration 9: Nano Banana image gen (scene paint + AI portrait), Jev gibberish gate (/review ok:false, /act 422), trashed status
import os
import time
import uuid

import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"


def _s(token):
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
    return s


@pytest.fixture(scope="module")
def player():
    r = requests.post(f"{API}/auth/register", json={"email": f"test_it9_{uuid.uuid4().hex[:8]}@example.com", "password": "Passw0rd!"})
    assert r.status_code == 200, r.text
    return _s(r.json()["token"])


@pytest.fixture(scope="module")
def character(player):
    camp = player.get(f"{API}/campaigns/hyw-1415").json()
    bg = camp["character_backgrounds"][0]
    ch = player.post(f"{API}/characters", json={"scenario_id": "hyw-1415", "name": "TEST_Iter9", "background_id": bg["id"], "attributes": bg["attributes"]})
    assert ch.status_code == 200, ch.text
    return ch.json()


@pytest.fixture(scope="module")
def pt(player, character):
    p = player.post(f"{API}/playthroughs", json={"character_id": character["character_id"]})
    assert p.status_code == 200, p.text
    return p.json()


def _journal(s, pid):
    return s.get(f"{API}/playthroughs/{pid}/chronicle").json()


def _wait_idle(s, pid, timeout=60):
    end = time.time() + timeout
    while time.time() < end:
        d = s.get(f"{API}/playthroughs/{pid}").json()
        if not (d.get("state") or d.get("view") or d).get("npc_pending"):
            return
        time.sleep(2)


def _wait_image(s, pid, eid, timeout=100):
    end = time.time() + timeout
    ev = None
    while time.time() < end:
        ev = next((e for e in _journal(s, pid) if e["id"] == eid), None)
        if ev and ev.get("image_status") in ("ready", "failed"):
            return ev
        time.sleep(3)
    return ev


# --- Jev gibberish gate
class TestGibberish:
    def test_review_gibberish_rejected(self, player, pt):
        r = player.post(f"{API}/playthroughs/{pt['playthrough_id']}/review", json={"declaration": "asdkj qwpoe zxmn"})
        assert r.status_code == 200
        d = r.json()
        assert d["ok"] is False, d
        assert "action" in d["reason"].lower()

    def test_act_gibberish_422(self, player, pt):
        pid = pt["playthrough_id"]
        before = len(_journal(player, pid))
        r = player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "asdkj qwpoe zxmn", "request_id": uuid.uuid4().hex})
        assert r.status_code == 422, r.text
        assert len(_journal(player, pid)) == before

    @pytest.mark.parametrize("text", ["qwerty uiop", "zzzz xxxx yyyy 123"])
    def test_review_more_gibberish(self, player, pt, text):
        d = player.post(f"{API}/playthroughs/{pt['playthrough_id']}/review", json={"declaration": text}).json()
        print(text, d)
        assert d["ok"] is False

    @pytest.mark.parametrize("text", ["I look around the camp", "Hello", "I attack the nearest soldier with my sword"])
    def test_review_normal_ok(self, player, pt, text):
        d = player.post(f"{API}/playthroughs/{pt['playthrough_id']}/review", json={"declaration": text}).json()
        print(text, d)
        assert d["ok"] is True, d


# --- Scene painting via review -> act (big moment) and Paint this moment
class TestScenePaint:
    def test_review_then_combat_paints(self, player, pt):
        pid = pt["playthrough_id"]
        _wait_idle(player, pid)
        decl = "I draw my sword and charge at the enemy scout"
        rv = player.post(f"{API}/playthroughs/{pid}/review", json={"declaration": decl}).json()
        assert rv["ok"] is True and rv["big_moment"] is True, rv
        r = player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": decl, "request_id": uuid.uuid4().hex}, timeout=120)
        assert r.status_code == 200, r.text
        eid = r.json()["event_id"]
        ev = _wait_image(player, pid, eid)
        assert ev["image_status"] == "ready", ev
        assert ev.get("image_url")
        img = requests.get(ev["image_url"] if ev["image_url"].startswith("http") else f"{BASE_URL}{ev['image_url']}")
        assert img.status_code == 200 and img.headers["content-type"].startswith("image/")

    def test_paint_non_big_event(self, player, pt):
        pid = pt["playthrough_id"]
        _wait_idle(player, pid)
        r = player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I look closely at the banners around me", "request_id": uuid.uuid4().hex}, timeout=120)
        assert r.status_code == 200, r.text
        eid = r.json()["event_id"]
        ev = next(e for e in _journal(player, pid) if e["id"] == eid)
        assert not ev.get("big_moment")
        p = player.post(f"{API}/playthroughs/{pid}/events/{eid}/paint")
        assert p.status_code == 200 and p.json()["status"] == "painting"
        ev = _wait_image(player, pid, eid)
        assert ev["image_status"] == "ready", ev
        assert ev.get("image_url")


# --- AI portrait
class TestPortrait:
    def test_generate_portrait(self, player, character):
        r = player.post(f"{API}/characters/{character['character_id']}/portrait/generate", json={"prompt": "weathered face"}, timeout=150)
        assert r.status_code == 200, r.text
        url = r.json()["portrait_url"]
        img = requests.get(url if url.startswith("http") else f"{BASE_URL}{url}")
        assert img.status_code == 200 and img.headers["content-type"].startswith("image/")
        assert len(img.content) > 5000


# --- Trashed playthrough blocks review/act
class TestTrashed:
    def test_trashed_blocks(self, player, character):
        p = player.post(f"{API}/playthroughs", json={"character_id": character["character_id"]}).json()
        pid = p["playthrough_id"]
        assert player.post(f"{API}/playthroughs/{pid}/trash").json()["status"] == "trashed"
        assert player.get(f"{API}/playthroughs/{pid}").json()["status"] == "trashed"
        assert player.post(f"{API}/playthroughs/{pid}/review", json={"declaration": "I look around"}).status_code == 400
        assert player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I look around"}).status_code == 400
        assert player.delete(f"{API}/playthroughs/{pid}").status_code == 200
