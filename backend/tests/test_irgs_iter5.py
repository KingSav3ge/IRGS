# Iteration 5 (testing agent): gap coverage for 3.3.E — pass-time concurrency, testimony listing, share card snapshot, catalogue auth
import os
import re
import threading
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
def user():
    r = requests.post(f"{API}/auth/register", json={"email": f"test_it5_{uuid.uuid4().hex[:8]}@example.com", "password": "Passw0rd!"})
    assert r.status_code == 200, r.text
    return _s(r.json()["token"])


def _new_play(s, testimony=None):
    camp = s.get(f"{API}/campaigns/hyw-1415").json()
    bg = camp["character_backgrounds"][0]
    body = {"scenario_id": "hyw-1415", "name": "TEST_Iter5", "background_id": bg["id"], "attributes": bg["attributes"]}
    if testimony:
        body["testimony"] = testimony
    ch = s.post(f"{API}/characters", json=body).json()
    p = s.post(f"{API}/playthroughs", json={"character_id": ch["character_id"]}).json()
    return ch, p


# pass-time: two simultaneous pass-time calls -> one 200, one 409 (or both 200 if serialized fast)
def test_concurrent_pass_time(user):
    _, p = _new_play(user)
    pid = p["playthrough_id"]
    out = []

    def go():
        out.append(requests.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "hours"}, headers=user.headers).status_code)
    ts = [threading.Thread(target=go) for _ in range(4)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print("concurrent statuses", out)
    assert 200 in out
    assert set(out) <= {200, 409}
    v = user.get(f"{API}/playthroughs/{pid}").json()["view"]
    assert v["clock"] == p["view"]["clock"] + out.count(200)


# pass-time: missing span defaults to "hours" (PassTimeIn default)
def test_missing_span(user):
    _, p = _new_play(user)
    r = user.post(f"{API}/playthroughs/{p['playthrough_id']}/pass-time", json={})
    assert r.status_code == 200


# pass-time: chronicle divider + journal text
def test_pass_time_journal(user):
    _, p = _new_play(user)
    r = user.post(f"{API}/playthroughs/{p['playthrough_id']}/pass-time", json={"span": "day"})
    ev = [e for e in r.json()["playthrough"]["chronicle"] if e["id"] == r.json()["event_id"]][0]
    assert ev["title"] == "A day passes"


# testimony visible in GET /api/characters
def test_testimony_in_list(user):
    ch, _ = _new_play(user, testimony={"origin": "TEST origin Kent"})
    lst = user.get(f"{API}/characters").json()
    items = lst if isinstance(lst, list) else lst.get("characters", [])
    me = [c for c in items if c["character_id"] == ch["character_id"]]
    assert me and me[0]["testimony"] == {"origin": "TEST origin Kent"}


# history reference: before 18 Sep 1415
def test_history_dates(user):
    _, p = _new_play(user)
    d = user.get(f"{API}/playthroughs/{p['playthrough_id']}/history-reference").json()
    print(d["current_date"], [e["date"] for e in d["events"]])
    assert d["current_date"] < "1415-09-18"
    assert all(e["date"] for e in d["events"])


# share card: snapshot mode, og:image absolute
def test_share_card_snapshot(user):
    _, p = _new_play(user)
    sh = user.post(f"{API}/playthroughs/{p['playthrough_id']}/shares", json={"mode": "snapshot"}).json()
    h = requests.get(f"{API}/s/{sh['share_id']}").text
    assert "TEST_Iter5" in h
    img = re.search(r'property="og:image" content="([^"]*)"', h).group(1)
    assert img.startswith("https://")
    # share url returned by API should point to /api/s
    print("share payload", {k: v for k, v in sh.items() if k != "snapshot"})


# catalogue requires auth
def test_entries_auth():
    assert requests.get(f"{API}/campaigns/hyw-1415/entries").status_code == 401
