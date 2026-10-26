# Iteration 10: creation_mode, wishlist/visibility, final pass (paint, Jev gibberish, trash lock)
import os
import time
import uuid

import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"
CONCEPT = None


def _s(token):
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
    return s


@pytest.fixture(scope="module")
def admin():
    r = requests.post(f"{API}/auth/login", json={"email": "admin", "password": "chronicle123"})
    assert r.status_code == 200, r.text
    s = _s(r.json()["token"])
    yield s
    s.put(f"{API}/admin/catalogue/visibility", json={"show_to_players": False})


@pytest.fixture(scope="module")
def player():
    r = requests.post(f"{API}/auth/register", json={"email": f"test_it10_{uuid.uuid4().hex[:8]}@example.com", "password": "Passw0rd!"})
    assert r.status_code == 200, r.text
    return _s(r.json()["token"])


@pytest.fixture(scope="module")
def concept_id(admin):
    recs = admin.get(f"{API}/catalogue").json()["records"]
    return next(r["id"] for r in recs if not r["playable"])


@pytest.fixture(scope="module")
def bg(player):
    return player.get(f"{API}/campaigns/hyw-1415").json()["character_backgrounds"][0]


# --- creation_mode
class TestCreationMode:
    @pytest.mark.parametrize("mode,expected", [("quick", "quick"), ("guided", "guided"), ("detailed", "detailed"), ("bogus", "detailed"), (None, "detailed")])
    def test_mode_stored(self, player, bg, mode, expected):
        body = {"scenario_id": "hyw-1415", "name": f"TEST_{mode}", "background_id": bg["id"], "attributes": bg["attributes"]}
        if mode:
            body["creation_mode"] = mode
        r = player.post(f"{API}/characters", json=body)
        assert r.status_code == 200, r.text
        assert r.json()["creation_mode"] == expected
        lst = player.get(f"{API}/characters").json()
        got = next(c for c in lst if c["character_id"] == r.json()["character_id"])
        assert got["creation_mode"] == expected


# --- wishlist & visibility
class TestWishlist:
    def test_player_forbidden_visibility(self, player):
        assert player.put(f"{API}/admin/catalogue/visibility", json={"show_to_players": True}).status_code == 403

    def test_hidden(self, admin, player, concept_id):
        assert admin.put(f"{API}/admin/catalogue/visibility", json={"show_to_players": False}).json()["concepts_visible"] is False
        d = player.get(f"{API}/catalogue").json()
        assert d["concepts_visible"] is False
        assert all(r["playable"] for r in d["records"])
        assert all("wishlist_count" not in r for r in d["records"])
        assert player.post(f"{API}/catalogue/{concept_id}/wishlist").status_code == 404

    def test_admin_sees_counts(self, admin):
        d = admin.get(f"{API}/catalogue").json()
        assert len(d["records"]) == 44, len(d["records"])
        assert all("wishlist_count" in r and "wishlisted" in r for r in d["records"])

    def test_playable_400(self, admin):
        assert admin.post(f"{API}/catalogue/MC-01/wishlist").status_code == 400

    def test_unknown_404(self, admin):
        assert admin.post(f"{API}/catalogue/NOPE-99/wishlist").status_code == 404

    def test_visible_flow(self, admin, player, concept_id):
        assert admin.put(f"{API}/admin/catalogue/visibility", json={"show_to_players": True}).status_code == 200
        d = player.get(f"{API}/catalogue").json()
        assert d["concepts_visible"] is True
        assert any(not r["playable"] for r in d["records"])
        before = next(r for r in admin.get(f"{API}/catalogue").json()["records"] if r["id"] == concept_id)["wishlist_count"]
        for _ in range(2):  # idempotent
            r = player.post(f"{API}/catalogue/{concept_id}/wishlist")
            assert r.status_code == 200 and r.json()["wishlisted"] is True
        rec = next(r for r in player.get(f"{API}/catalogue").json()["records"] if r["id"] == concept_id)
        assert rec["wishlisted"] is True and "wishlist_count" not in rec
        after = next(r for r in admin.get(f"{API}/catalogue").json()["records"] if r["id"] == concept_id)["wishlist_count"]
        assert after == before + 1
        for _ in range(2):
            r = player.delete(f"{API}/catalogue/{concept_id}/wishlist")
            assert r.status_code == 200 and r.json()["wishlisted"] is False
        rec = next(r for r in player.get(f"{API}/catalogue").json()["records"] if r["id"] == concept_id)
        assert rec["wishlisted"] is False
        admin.put(f"{API}/admin/catalogue/visibility", json={"show_to_players": False})


# --- final pass
@pytest.fixture(scope="module")
def pt(player, bg):
    ch = player.post(f"{API}/characters", json={"scenario_id": "hyw-1415", "name": "TEST_It10", "background_id": bg["id"], "attributes": bg["attributes"]}).json()
    p = player.post(f"{API}/playthroughs", json={"character_id": ch["character_id"]})
    assert p.status_code == 200
    return {"pid": p.json()["playthrough_id"], "cid": ch["character_id"]}


def _journal(s, pid):
    return s.get(f"{API}/playthroughs/{pid}/chronicle").json()


def _wait_image(s, pid, eid, timeout=120):
    end = time.time() + timeout
    ev = None
    while time.time() < end:
        ev = next((e for e in _journal(s, pid) if e["id"] == eid), None)
        if ev and ev.get("image_status") in ("ready", "failed"):
            return ev
        time.sleep(4)
    return ev


def _wait_idle(s, pid, timeout=60):
    end = time.time() + timeout
    while time.time() < end:
        d = s.get(f"{API}/playthroughs/{pid}").json()
        if not (d.get("state") or d.get("view") or d).get("npc_pending"):
            return
        time.sleep(2)


class TestGibberish:
    @pytest.mark.parametrize("text", ["asdkjh qwpoe zxmcn", "qwerty uiop", "xkcd zzzz plmq"])
    def test_review(self, player, pt, text):
        r = player.post(f"{API}/playthroughs/{pt['pid']}/review", json={"declaration": text})
        assert r.status_code == 200, r.text
        assert r.json()["ok"] is False, r.json()

    def test_act(self, player, pt):
        r = player.post(f"{API}/playthroughs/{pt['pid']}/act", json={"declaration": "asdkjh qwpoe zxmcn", "request_id": uuid.uuid4().hex})
        assert r.status_code in (400, 422), r.text


class TestPaint:
    def test_auto_paint_combat(self, player, pt):
        pid = pt["pid"]
        _wait_idle(player, pid)
        r = player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I draw my sword and charge the enemy scout", "request_id": uuid.uuid4().hex}, timeout=120)
        assert r.status_code == 200, r.text
        ev = _wait_image(player, pid, r.json()["event_id"])
        print("auto status", ev.get("image_status"))
        assert ev["image_status"] == "ready"
        url = ev["image_url"]
        img = requests.get(url if url.startswith("http") else f"{BASE_URL}{url}")
        assert img.status_code == 200 and img.headers["content-type"].startswith("image/")
        print("img bytes", len(img.content))

    def test_manual_paint(self, player, pt):
        pid = pt["pid"]
        _wait_idle(player, pid)
        r = player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I study the banners around the camp", "request_id": uuid.uuid4().hex}, timeout=120)
        assert r.status_code == 200, r.text
        eid = r.json()["event_id"]
        p = player.post(f"{API}/playthroughs/{pid}/events/{eid}/paint")
        assert p.status_code == 200 and p.json()["status"] == "painting"
        ev = _wait_image(player, pid, eid)
        assert ev["image_status"] == "ready", ev.get("image_status")


class TestTrashLock:
    def test_lock(self, player, pt):
        p = player.post(f"{API}/playthroughs", json={"character_id": pt["cid"]}).json()
        pid = p["playthrough_id"]
        assert player.post(f"{API}/playthroughs/{pid}/trash").json()["status"] == "trashed"
        assert player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I look around"}).status_code == 400
        assert player.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "hours"}).status_code == 400
        assert player.post(f"{API}/playthroughs/{pid}/review", json={"declaration": "I look around"}).status_code == 400
        sv = player.post(f"{API}/playthroughs/{pid}/saves", json={"kind": "manual", "label": "TEST"})
        print("save on trashed:", sv.status_code)
        assert sv.status_code in (400, 403, 409, 423), f"save allowed on trashed: {sv.status_code}"

    def test_restore_and_delete(self, player, pt):
        pid = player.post(f"{API}/playthroughs", json={"character_id": pt["cid"]}).json()["playthrough_id"]
        player.post(f"{API}/playthroughs/{pid}/trash")
        assert player.delete(f"{API}/playthroughs/{pid}").status_code == 200
        assert player.get(f"{API}/playthroughs/{pid}").status_code == 404
        pid2 = player.post(f"{API}/playthroughs", json={"character_id": pt["cid"]}).json()["playthrough_id"]
        assert player.delete(f"{API}/playthroughs/{pid2}").status_code == 400  # must trash first
        player.post(f"{API}/playthroughs/{pid2}/trash")
        assert player.post(f"{API}/playthroughs/{pid2}/restore").json()["status"] == "active"
        r = player.post(f"{API}/playthroughs/{pid2}/pass-time", json={"span": "hours"})
        assert r.status_code == 200, r.text
        assert player.post(f"{API}/playthroughs/{pid2}/saves", json={"kind": "manual", "label": "TEST"}).status_code == 200
