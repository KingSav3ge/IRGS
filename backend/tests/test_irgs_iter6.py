# Iteration 6 (testing agent): Chronicle workspace (entities, notes, development, goals), idempotent actions, save preview/safety, version re-checks
import os
import uuid

import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"


def _s(token):
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
    return s


def _register():
    r = requests.post(f"{API}/auth/register", json={"email": f"test_it6_{uuid.uuid4().hex[:8]}@example.com", "password": "Passw0rd!"})
    assert r.status_code == 200, r.text
    return _s(r.json()["token"])


def _new_play(s):
    camp = s.get(f"{API}/campaigns/hyw-1415").json()
    bg = camp["character_backgrounds"][0]
    ch = s.post(f"{API}/characters", json={"scenario_id": "hyw-1415", "name": "TEST_Iter6", "background_id": bg["id"], "attributes": bg["attributes"]}).json()
    p = s.post(f"{API}/playthroughs", json={"character_id": ch["character_id"]}).json()
    return p


@pytest.fixture(scope="module")
def ctx():
    a, b = _register(), _register()
    p = _new_play(a)
    return {"a": a, "b": b, "pid": p["playthrough_id"], "p": p}


# ---- entities
class TestEntities:
    def test_list_entities(self, ctx):
        r = ctx["a"].get(f"{API}/playthroughs/{ctx['pid']}/entities")
        assert r.status_code == 200
        ents = r.json()
        assert len(ents) > 0
        types = {e["type"] for e in ents}
        assert "person" in types and "place" in types
        for e in ents:
            assert isinstance(e["mentions"], int) and e["name"]
        ctx["ents"] = ents

    def test_entity_detail(self, ctx):
        ents = ctx["a"].get(f"{API}/playthroughs/{ctx['pid']}/entities").json()
        person = next(e for e in ents if e["type"] == "person")
        r = ctx["a"].get(f"{API}/playthroughs/{ctx['pid']}/entities/{person['id']}")
        assert r.status_code == 200
        d = r.json()
        assert d["id"] == person["id"]
        for k in ("events", "notes", "disposition_trend", "rumours"):
            assert isinstance(d[k], list)
        assert len(d["events"]) == person["mentions"]

    def test_unknown_entity_404(self, ctx):
        r = ctx["a"].get(f"{API}/playthroughs/{ctx['pid']}/entities/nope_xyz")
        assert r.status_code == 404

    def test_other_user_cannot_read_entities(self, ctx):
        r = ctx["b"].get(f"{API}/playthroughs/{ctx['pid']}/entities")
        assert r.status_code == 404


# ---- notes
class TestNotes:
    def test_note_crud_and_link(self, ctx):
        a, pid = ctx["a"], ctx["pid"]
        ents = a.get(f"{API}/playthroughs/{pid}/entities").json()
        eid = ents[0]["id"]
        r = a.post(f"{API}/playthroughs/{pid}/notes", json={"kind": "document", "title": "TEST_Letter", "body": "Dear sir", "entity_ids": [eid, "bogus_id"]})
        assert r.status_code == 200, r.text
        n = r.json()
        assert n["kind"] == "document" and n["title"] == "TEST_Letter" and n["entity_ids"] == [eid]
        nid = n["note_id"]
        lst = a.get(f"{API}/playthroughs/{pid}/notes").json()
        assert any(x["note_id"] == nid for x in lst)
        det = a.get(f"{API}/playthroughs/{pid}/entities/{eid}").json()
        assert any(x["note_id"] == nid for x in det["notes"])
        # patch
        r = a.patch(f"{API}/notes/{nid}", json={"title": "TEST_Letter2"})
        assert r.status_code == 200 and r.json()["title"] == "TEST_Letter2"
        assert a.patch(f"{API}/notes/{nid}", json={"title": "  "}).status_code == 400
        # other user
        assert ctx["b"].get(f"{API}/playthroughs/{pid}/notes").status_code == 404
        assert ctx["b"].delete(f"{API}/notes/{nid}").status_code == 404
        assert ctx["b"].patch(f"{API}/notes/{nid}", json={"title": "hack"}).status_code == 404
        # delete
        assert a.delete(f"{API}/notes/{nid}").status_code == 200
        assert a.delete(f"{API}/notes/{nid}").status_code == 404
        assert not any(x["note_id"] == nid for x in a.get(f"{API}/playthroughs/{pid}/notes").json())

    def test_note_validation(self, ctx):
        a, pid = ctx["a"], ctx["pid"]
        assert a.post(f"{API}/playthroughs/{pid}/notes", json={"kind": "note", "title": "  "}).status_code == 400
        assert a.post(f"{API}/playthroughs/{pid}/notes", json={"kind": "poem", "title": "x"}).status_code == 400

    def test_patch_drops_unknown_entity_ids(self, ctx):
        # create validates entity ids; PATCH should too
        a, pid = ctx["a"], ctx["pid"]
        n = a.post(f"{API}/playthroughs/{pid}/notes", json={"kind": "note", "title": "TEST_p"}).json()
        r = a.patch(f"{API}/notes/{n['note_id']}", json={"entity_ids": ["bogus_id"]})
        a.delete(f"{API}/notes/{n['note_id']}")
        assert r.status_code in (200, 400)
        if r.status_code == 200:
            assert "bogus_id" not in r.json()["entity_ids"], "PATCH /notes accepts unknown entity ids"


# ---- development & goals
class TestGoals:
    def test_goal_lifecycle(self, ctx):
        a, pid = ctx["a"], ctx["pid"]
        r = a.post(f"{API}/playthroughs/{pid}/goals", json={"title": "TEST_goal one"})
        assert r.status_code == 200, r.text
        goals = a.get(f"{API}/playthroughs/{pid}/development").json()["goals"]
        g = next(x for x in goals if x["title"] == "TEST_goal one")
        assert g["status"] == "active"
        for st in ("achieved", "active", "abandoned"):
            r = a.patch(f"{API}/playthroughs/{pid}/goals/{g['id']}", json={"status": st})
            assert r.status_code == 200
            assert next(x for x in a.get(f"{API}/playthroughs/{pid}/development").json()["goals"] if x["id"] == g["id"])["status"] == st
        journal = a.get(f"{API}/playthroughs/{pid}/chronicle").json()
        items = journal if isinstance(journal, list) else journal.get("chronicle", journal.get("entries", []))
        goal_events = [e for e in items if e.get("kind") == "goal"]
        assert len(goal_events) >= 4
        dev = a.get(f"{API}/playthroughs/{pid}/development").json()
        assert any(m["title"].startswith("A personal goal") for m in dev["milestones"])
        for k in ("points", "intents", "milestones", "testimony", "attributes"):
            assert k in dev

    def test_goal_validation(self, ctx):
        a, pid = ctx["a"], ctx["pid"]
        assert a.post(f"{API}/playthroughs/{pid}/goals", json={"title": "  "}).status_code == 400
        assert a.patch(f"{API}/playthroughs/{pid}/goals/goal_nope", json={"status": "achieved"}).status_code == 404
        g = a.get(f"{API}/playthroughs/{pid}/development").json()["goals"][0]
        assert a.patch(f"{API}/playthroughs/{pid}/goals/{g['id']}", json={"status": "weird"}).status_code == 400
        assert ctx["b"].post(f"{API}/playthroughs/{pid}/goals", json={"title": "x"}).status_code == 404

    def test_max_8_active(self):
        s = _register()
        pid = _new_play(s)["playthrough_id"]
        ids = []
        for i in range(8):
            r = s.post(f"{API}/playthroughs/{pid}/goals", json={"title": f"TEST_g{i}"})
            assert r.status_code == 200
        r = s.post(f"{API}/playthroughs/{pid}/goals", json={"title": "TEST_g9"})
        assert r.status_code == 400
        # abandon one, add 9th, then reactivate -> should not exceed 8 active
        goals = s.get(f"{API}/playthroughs/{pid}/development").json()["goals"]
        s.patch(f"{API}/playthroughs/{pid}/goals/{goals[0]['id']}", json={"status": "abandoned"})
        assert s.post(f"{API}/playthroughs/{pid}/goals", json={"title": "TEST_g9"}).status_code == 200
        r = s.patch(f"{API}/playthroughs/{pid}/goals/{goals[0]['id']}", json={"status": "active"})
        active = [g for g in s.get(f"{API}/playthroughs/{pid}/development").json()["goals"] if g["status"] == "active"]
        assert len(active) <= 8, f"reactivate bypasses 8-active cap: {len(active)} active (status {r.status_code})"


# ---- idempotent actions
class TestIdempotency:
    def test_pass_time_replay(self, ctx):
        a, pid = ctx["a"], ctx["pid"]
        rid = str(uuid.uuid4())
        r1 = a.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "hours", "request_id": rid})
        assert r1.status_code == 200, r1.text
        clock1 = r1.json()["playthrough"]["view"]["clock"]
        r2 = a.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "hours", "request_id": rid})
        assert r2.status_code == 200
        d2 = r2.json()
        assert d2.get("replayed") is True
        assert d2["event_id"] == r1.json()["event_id"]
        assert d2["playthrough"]["view"]["clock"] == clock1

    def test_pass_time_missing_span_422(self, ctx):
        r = ctx["a"].post(f"{API}/playthroughs/{ctx['pid']}/pass-time", json={})
        assert r.status_code == 422

    def test_act_replay(self, ctx):
        a, pid = ctx["a"], ctx["pid"]
        rid = str(uuid.uuid4())
        r1 = a.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I look around the camp carefully.", "request_id": rid}, timeout=150)
        assert r1.status_code == 200, r1.text
        c1 = r1.json()["playthrough"]["view"]["clock"]
        r2 = a.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I look around the camp carefully.", "request_id": rid}, timeout=150)
        assert r2.status_code == 200, r2.text
        assert r2.json()["replayed"] is True and r2.json()["event_id"] == r1.json()["event_id"]
        assert r2.json()["playthrough"]["view"]["clock"] == c1


# ---- save preview & safety
class TestSavePreview:
    def test_preview_load_safety(self):
        s = _register()
        pid = _new_play(s)["playthrough_id"]
        sv = s.post(f"{API}/playthroughs/{pid}/saves", json={"kind": "manual", "label": "TEST_early"}).json()
        s.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "hours"})
        s.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "day"})
        r = s.get(f"{API}/saves/{sv['save_id']}/preview")
        assert r.status_code == 200
        p = r.json()
        assert p["events_replaced"] == 2
        assert isinstance(p["last_events"], list) and "condition" in p["character"]
        assert p["current_clock"] > p["clock"]
        # other user
        assert _register().get(f"{API}/saves/{sv['save_id']}/preview").status_code == 404
        r = s.post(f"{API}/saves/{sv['save_id']}/load")
        assert r.status_code == 200
        assert r.json()["view"]["clock"] == p["clock"]
        saves = s.get(f"{API}/playthroughs/{pid}/saves").json()
        safety = [x for x in saves if x["kind"] == "safety"]
        assert len(safety) == 1 and "TEST_early" in safety[0]["label"] and safety[0]["label"].startswith("Before restoring")
        assert safety[0]["clock"] == p["current_clock"]
        # restoring the safety brings us back
        pr = s.get(f"{API}/saves/{safety[0]['save_id']}/preview").json()
        assert pr["events_replaced"] == 0
        auto = [x for x in saves if x["kind"] == "auto"]
        if auto:
            assert s.delete(f"{API}/saves/{auto[0]['save_id']}").status_code == 400
        assert s.delete(f"{API}/saves/{safety[0]['save_id']}").status_code == 200


# ---- re-verify iteration 4 items
class TestShareHead:
    def test_head_and_og(self, ctx):
        a, pid = ctx["a"], ctx["pid"]
        sh = a.post(f"{API}/playthroughs/{pid}/shares", json={"mode": "snapshot"}).json()
        r = requests.head(f"{API}/s/{sh['share_id']}")
        assert r.status_code == 200
        html = requests.get(f"{API}/s/{sh['share_id']}").text
        import re
        m = re.search(r'property="og:description"\s+content="([^"]*)"', html)
        assert m and "(snapshot)" in m.group(1)
