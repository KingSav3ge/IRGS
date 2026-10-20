# Iteration 4: pass-time, OG share cards (/api/s/{id}), HYW 3.3.2 merge (catalogue, history reference), testimony
import os
import re
import threading
import time
import uuid

import pytest
import requests
from pymongo import MongoClient

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"


def _s(token=None):
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    if token:
        s.headers["Authorization"] = f"Bearer {token}"
    return s


@pytest.fixture(scope="module")
def user():
    r = requests.post(f"{API}/auth/register", json={"email": f"test_it4_{uuid.uuid4().hex[:8]}@example.com", "password": "Passw0rd!"})
    assert r.status_code == 200, r.text
    return _s(r.json()["token"])


@pytest.fixture(scope="module")
def admin():
    r = requests.post(f"{API}/auth/login", json={"email": "admin", "password": "chronicle123"})
    if r.status_code != 200:
        pytest.skip("admin login failed")
    return _s(r.json()["token"])


def _new_play(s, scenario="hyw-1415", testimony=None):
    camp = s.get(f"{API}/campaigns/{scenario}").json()
    bg = camp["character_backgrounds"][0]
    body = {"scenario_id": scenario, "name": "TEST_Iter4", "background_id": bg["id"], "attributes": bg["attributes"]}
    if testimony is not None:
        body["testimony"] = testimony
    r = s.post(f"{API}/characters", json=body)
    assert r.status_code == 200, r.text
    ch = r.json()
    r = s.post(f"{API}/playthroughs", json={"character_id": ch["character_id"]})
    assert r.status_code == 200, r.text
    return ch, r.json()


def _wait_npc(s, pid, timeout=90):
    t0 = time.time()
    while time.time() - t0 < timeout:
        d = s.get(f"{API}/playthroughs/{pid}").json()
        if not d["view"]["npc_pending"]:
            return d
        time.sleep(2)
    return None


# ------------------------------------------------------------ pass-time
class TestPassTime:
    @pytest.mark.parametrize("span,days,band_same", [("hours", 0, False), ("day", 1, True), ("week", 7, True)])
    def test_spans(self, user, span, days, band_same):
        from datetime import date, timedelta
        _, p = _new_play(user)
        pid = p["playthrough_id"]
        v0 = p["view"]
        r = user.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": span})
        assert r.status_code == 200, r.text
        d = r.json()
        v1 = d["playthrough"]["view"]
        assert v1["clock"] == v0["clock"] + 1
        assert v1["npc_pending"] is True
        d0 = date.fromisoformat(v0["campaign_time"]["date"])
        d1 = date.fromisoformat(v1["campaign_time"]["date"])
        if band_same:
            assert v1["campaign_time"]["time"] == v0["campaign_time"]["time"]
            assert d1 == d0 + timedelta(days=days)
        else:
            assert v1["campaign_time"]["time"] != v0["campaign_time"]["time"]
        assert v1["character"]["condition"]["stamina"] <= 100
        ev = [e for e in d["playthrough"]["chronicle"] if e["id"] == d["event_id"]]
        assert ev and ev[0]["kind"] == "time_passes"
        done = _wait_npc(user, pid)
        assert done is not None, "npc_pending never cleared"

    def test_invalid_span(self, user):
        _, p = _new_play(user)
        r = user.post(f"{API}/playthroughs/{p['playthrough_id']}/pass-time", json={"span": "year"})
        assert r.status_code == 400

    def test_archived(self, user):
        _, p = _new_play(user)
        pid = p["playthrough_id"]
        assert user.post(f"{API}/playthroughs/{pid}/archive").status_code == 200
        r = user.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "hours"})
        assert r.status_code == 400

    def test_stamina_cap_week(self, user):
        _, p = _new_play(user)
        pid = p["playthrough_id"]
        r = user.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "week"})
        assert r.json()["playthrough"]["view"]["character"]["condition"]["stamina"] == 100

    def test_concurrent_act_409(self, user):
        _, p = _new_play(user)
        pid = p["playthrough_id"]
        res = {}
        t = threading.Thread(target=lambda: res.setdefault("act", user.post(
            f"{API}/playthroughs/{pid}/act", json={"declaration": "I look around the quay carefully."}, timeout=120)))
        t.start()
        time.sleep(1.5)
        r = requests.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "hours"}, headers=user.headers)
        t.join()
        assert r.status_code == 409, r.text
        assert res["act"].status_code == 200

    def test_other_user_404(self, user):
        _, p = _new_play(user)
        r2 = requests.post(f"{API}/auth/register", json={"email": f"test_it4b_{uuid.uuid4().hex[:8]}@example.com", "password": "Passw0rd!"})
        other = _s(r2.json()["token"])
        assert other.post(f"{API}/playthroughs/{p['playthrough_id']}/pass-time", json={"span": "hours"}).status_code == 404


# ------------------------------------------------------------ share card
class TestShareCard:
    def test_card_html(self, user):
        _, p = _new_play(user)
        pid = p["playthrough_id"]
        sh = user.post(f"{API}/playthroughs/{pid}/shares", json={"mode": "live"}).json()
        r = requests.get(f"{API}/s/{sh['share_id']}", allow_redirects=False)
        assert r.status_code == 200
        assert r.headers["content-type"].startswith("text/html")
        h = r.text
        for tag in ['property="og:title"', 'property="og:description"', 'name="twitter:card" content="summary_large_image"']:
            assert tag in h
        img = re.search(r'property="og:image" content="([^"]*)"', h).group(1)
        assert img.startswith("http"), img
        assert f'http-equiv="refresh" content="0;url=' in h and f"/story/{sh['share_id']}" in h
        refresh = re.search(r'content="0;url=([^"]*)"', h).group(1)
        assert refresh.startswith(BASE_URL), refresh
        # revoke -> generic
        assert user.delete(f"{API}/shares/{sh['share_id']}").status_code == 200
        g = requests.get(f"{API}/s/{sh['share_id']}").text
        assert "no longer shared" in g

    def test_unknown(self):
        r = requests.get(f"{API}/s/doesnotexist123")
        assert r.status_code == 200 and "no longer shared" in r.text


# ------------------------------------------------------------ HYW 3.3.2
class TestHYW:
    def test_campaign(self, user):
        c = user.get(f"{API}/campaigns/hyw-1415").json()
        assert c["entry_catalogue"] == "hyw"
        assert c["sources"] and c["unknowns"]
        names = " ".join(a.get("name", "") for a in c["actors"])
        assert "Louis" in names
        assert len(c["actors"]) == 5

    def test_world_facts(self, user):
        _, p = _new_play(user)
        assert len(p["view"]["world_facts"]) == 11

    def test_entries(self, user):
        r = user.get(f"{API}/campaigns/hyw-1415/entries")
        assert r.status_code == 200
        d = r.json()
        assert len(d["entries"]) == 37
        assert len(d["periods"]) == 3
        playable = [e for e in d["entries"] if e["playable"]]
        assert all(e["year"] == 1415 for e in playable) and playable

    def test_entries_non_hyw_404(self, admin):
        others = [c["id"] for c in admin.get(f"{API}/campaigns").json() if c["id"] != "hyw-1415"]
        assert admin.get(f"{API}/campaigns/{others[0]}/entries").status_code == 404

    def test_history_reference(self, user):
        _, p = _new_play(user)
        d = user.get(f"{API}/playthroughs/{p['playthrough_id']}/history-reference").json()
        assert d["available"] is True
        assert len(d["events"]) == 3 and d["sources"]

    def test_history_reference_non_hyw(self, admin):
        others = [c["id"] for c in admin.get(f"{API}/campaigns").json() if c["id"] != "hyw-1415"]
        _, p = _new_play(admin, others[0])
        d = admin.get(f"{API}/playthroughs/{p['playthrough_id']}/history-reference").json()
        assert d == {"available": False}


# ------------------------------------------------------------ testimony
class TestTestimony:
    def test_saved(self, user):
        t = {"origin": "Born in Southampton", "family": "Two brothers", "career": "Archer", "bogus": "x", "empty": ""}
        ch, p = _new_play(user, testimony=t)
        assert ch["testimony"] == {"origin": "Born in Southampton", "family": "Two brothers", "career": "Archer"}
        db = MongoClient(os.environ.get("MONGO_URL", "mongodb://localhost:27017"))["test_database"]
        doc = db.playthroughs.find_one({"playthrough_id": p["playthrough_id"]})
        assert doc["state"]["testimony"]["career"] == "Archer"

    def test_blank_is_empty(self, user):
        ch, _ = _new_play(user, testimony={"origin": "   "})
        assert ch["testimony"] == {}
