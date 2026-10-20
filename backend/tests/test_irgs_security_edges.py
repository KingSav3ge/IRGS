# IRGS extra checks: 401 unauth, 400 empty declaration, user isolation, archived act, store edge cases, paint/act race
import os
import time
import uuid
import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"


def _new_user():
    email = f"test_edge_{uuid.uuid4().hex[:8]}@example.com"
    r = requests.post(f"{API}/auth/register", json={"email": email, "password": "Passw0rd!", "name": "TEST Edge"})
    assert r.status_code == 200, r.text
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {r.json()['token']}"
    return s


def _new_play(s):
    camps = s.get(f"{API}/campaigns").json()
    free = next(c for c in camps if not c["premium"])
    bg = free["character_backgrounds"][0]
    r = s.post(f"{API}/characters", json={"scenario_id": free["id"], "name": "TEST Edge Hero",
                                          "background_id": bg["id"], "attributes": dict(bg["attributes"])})
    assert r.status_code == 200, r.text
    r = s.post(f"{API}/playthroughs", json={"character_id": r.json()["character_id"]})
    assert r.status_code == 200, r.text
    return r.json()


@pytest.fixture(scope="module")
def a():
    s = _new_user()
    return {"s": s, "pt": _new_play(s)}


@pytest.fixture(scope="module")
def b():
    return _new_user()


# ---- unauthenticated
@pytest.mark.parametrize("method,path", [("get", "/campaigns"), ("get", "/playthroughs"), ("get", "/store/items"),
                                         ("get", "/auth/me"), ("post", "/voice/tts"), ("get", "/store/orders")])
def test_401_without_auth(method, path):
    r = getattr(requests, method)(f"{API}{path}", json={"text": "x"})
    assert r.status_code == 401


def test_empty_declaration_400(a):
    pid = a["pt"]["playthrough_id"]
    r = a["s"].post(f"{API}/playthroughs/{pid}/act", json={"declaration": "   "})
    assert r.status_code == 400
    assert "empty" in r.json()["detail"].lower()


def test_user_isolation(a, b):
    pid = a["pt"]["playthrough_id"]
    assert b.get(f"{API}/playthroughs/{pid}").status_code == 404
    assert b.get(f"{API}/playthroughs/{pid}/saves").status_code == 404
    assert b.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "steal"}).status_code == 404
    assert b.post(f"{API}/playthroughs/{pid}/archive").status_code == 404
    saves = a["s"].get(f"{API}/playthroughs/{pid}/saves").json()
    sid = saves[0]["save_id"]
    assert b.post(f"{API}/saves/{sid}/load").status_code == 404
    assert b.post(f"{API}/saves/{sid}/branch", json={}).status_code == 404
    assert b.delete(f"{API}/saves/{sid}").status_code == 404
    assert all(p["playthrough_id"] != pid for p in b.get(f"{API}/playthroughs").json())


def test_archived_cannot_act(a):
    s, pid = a["s"], a["pt"]["playthrough_id"]
    assert s.post(f"{API}/playthroughs/{pid}/archive").status_code == 200
    archived = s.get(f"{API}/playthroughs", params={"status": "archived"}).json()
    assert any(p["playthrough_id"] == pid for p in archived)
    r = s.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I look around"})
    assert r.status_code == 400 and "archived" in r.json()["detail"].lower()
    assert s.post(f"{API}/playthroughs/{pid}/restore").status_code == 200
    assert s.get(f"{API}/playthroughs/{pid}").json()["status"] == "active"


def test_checkout_unknown_item_and_double_buy(b):
    assert b.post(f"{API}/store/checkout", json={"item_id": "nope", "provider": "paypal"}).status_code == 400
    r = b.post(f"{API}/store/checkout", json={"item_id": "pack-portraits", "provider": "paystack"})
    assert r.status_code == 200 and r.json()["order"]["mocked"] is True
    r2 = b.post(f"{API}/store/checkout", json={"item_id": "pack-portraits", "provider": "paypal"})
    assert r2.status_code == 400


def test_cancel_subscription_not_owned_404(b):
    assert b.post(f"{API}/store/subscriptions/sub-elevenlabs-narration/cancel").status_code == 404


def test_settings_invalid_voice_engine(a):
    pid = a["pt"]["playthrough_id"]
    r = a["s"].patch(f"{API}/playthroughs/{pid}/settings", json={"voice_engine": "bogus-engine"})
    # expected: 400 validation; records actual behaviour
    assert r.status_code in (400, 422), f"accepted invalid voice_engine: {r.status_code} {r.json().get('voice_engine')}"


def test_paint_then_act_race_keeps_image(a):
    """A big-moment image that finishes while another act is in flight must not be lost."""
    s, pid = a["s"], a["pt"]["playthrough_id"]
    r = s.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I walk briskly to the nearest gate."}, timeout=150)
    assert r.status_code == 200, r.text
    ev = r.json()["event_id"]
    painting = r.json()["decision"]["intent"] in ("move", "combat")
    if not painting:
        pytest.skip("intent not move/combat")
    # keep acting while the painting is in progress
    deadline = time.time() + 150
    while time.time() < deadline:
        s.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I say a quiet word to myself."}, timeout=150)
        ch = s.get(f"{API}/playthroughs/{pid}/chronicle").json()
        e = next(x for x in ch if x["id"] == ev)
        if e["image_status"] != "painting":
            break
    time.sleep(10)
    ch = s.get(f"{API}/playthroughs/{pid}/chronicle").json()
    e = next(x for x in ch if x["id"] == ev)
    assert e["image_status"] == "ready" and e["image_url"], f"image lost/stuck: {e['image_status']}"


def test_load_save_reverts_state():
    s = _new_user()
    pt = _new_play(s)
    pid = pt["playthrough_id"]
    sv = s.post(f"{API}/playthroughs/{pid}/saves", json={"kind": "manual", "label": "TEST before"}).json()
    assert sv["clock"] == 0
    r = s.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I look at the sky."}, timeout=150)
    assert r.status_code == 200 and r.json()["playthrough"]["view"]["clock"] == 1
    loaded = s.post(f"{API}/saves/{sv['save_id']}/load").json()
    assert loaded["view"]["clock"] == 0 and len(loaded["chronicle"]) == 1
    got = s.get(f"{API}/playthroughs/{pid}").json()
    assert got["view"]["clock"] == 0
    auto = next(x for x in s.get(f"{API}/playthroughs/{pid}/saves").json() if x["kind"] == "auto")
    assert auto["clock"] == 0
