# Iteration 3: Living Characters (NPC actions) + shareable storybook + engine.apply_npc_actions unit tests
import os
import sys
import time
import uuid

import pytest
import requests

sys.path.insert(0, "/app/backend")
import engine  # noqa: E402

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"


def _s(token=None):
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    if token:
        s.headers["Authorization"] = f"Bearer {token}"
    return s


def _new_user():
    email = f"test_it3_{uuid.uuid4().hex[:8]}@example.com"
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


def _wait_npc(s, pid, timeout=60):
    t0 = time.time()
    while time.time() - t0 < timeout:
        d = s.get(f"{API}/playthroughs/{pid}").json()
        if not d["view"]["npc_pending"]:
            return d, time.time() - t0
        time.sleep(2)
    return d, None


# ------------------------------------------------------------ engine unit tests
def _state():
    return {
        "player_actor_id": "P", "clock": 3,
        "campaign_time": {"date": "1415-08-11", "time": "morning"},
        "actors": {
            "P": {"id": "P", "name": "Me", "current": {"location": "Quay", "condition": {"health": 100, "stamina": 90, "morale": 70}}},
            **{f"N{i}": {"id": f"N{i}", "name": f"Npc{i}", "current": {}} for i in range(8)},
        },
        "locations": {"Quay": {"id": "Quay", "name": "The Quay"}, "Fort": {"id": "Fort", "name": "Portchester Castle"}},
        "inventory": [{"name": "sword"}], "journal": [],
    }


class TestApplyNpcActions:
    def test_clamps_delta(self):
        st = engine.apply_npc_actions(_state(), [{"actor_id": "N0", "kind": "disposition", "delta": 99, "summary": "x"},
                                                 {"actor_id": "N1", "kind": "disposition", "delta": -99, "summary": "y"}])
        assert st["actors"]["N0"]["current"]["disposition"] == 15
        assert st["actors"]["N1"]["current"]["disposition"] == -15
        assert st["journal"][0]["effect"]["disposition_delta"] == 15

    def test_rejects_unknown_and_player_actor(self):
        st = engine.apply_npc_actions(_state(), [{"actor_id": "GHOST", "kind": "rumour", "summary": "x"},
                                                 {"actor_id": "P", "kind": "disposition", "delta": 5, "summary": "x"}])
        assert st["journal"] == []
        assert st["actors"]["P"]["current"]["condition"]["stamina"] == 90

    def test_rejects_unknown_kind_and_location(self):
        st = engine.apply_npc_actions(_state(), [{"actor_id": "N0", "kind": "move", "location": "Paris", "summary": "x"},
                                                 {"actor_id": "N1", "kind": "steal", "summary": "x"}])
        assert st["journal"] == []

    def test_move_by_name(self):
        st = engine.apply_npc_actions(_state(), [{"actor_id": "N0", "kind": "move", "location": "portchester castle", "summary": "went"}])
        assert st["actors"]["N0"]["current"]["location"] == "Fort"

    def test_caps_local_2_broad_6(self):
        acts = [{"actor_id": f"N{i}", "kind": "rumour", "summary": f"r{i}"} for i in range(8)]
        assert len(engine.apply_npc_actions(_state(), acts, "local")["journal"]) == 2
        b = engine.apply_npc_actions(_state(), acts, "broad")
        assert len(b["journal"]) == 6 and len(b["rumours"]) == 6

    def test_player_untouched(self):
        s0 = _state()
        st = engine.apply_npc_actions(s0, [{"actor_id": "N0", "kind": "rumour", "summary": "x"}], "broad")
        assert st["inventory"] == s0["inventory"]
        assert st["actors"]["P"] == s0["actors"]["P"]

    def test_robust_to_malformed_llm_output(self):
        # LLM output is untrusted: non-numeric delta / non-dict entries must not raise
        acts = ["junk", {"actor_id": "N0", "kind": "disposition", "delta": "five", "summary": "x"},
                {"actor_id": "N1", "kind": "rumour", "summary": "ok"}]
        try:
            st = engine.apply_npc_actions(_state(), acts)
        except Exception as e:
            pytest.fail(f"apply_npc_actions raised on malformed LLM output: {type(e).__name__}: {e}")
        assert any(e["actor_ids"] == ["N1"] for e in st["journal"])


# ------------------------------------------------------------ API: NPC turn + shares
@pytest.fixture(scope="module")
def owner():
    return _new_user()


@pytest.fixture(scope="module")
def play(owner):
    return _new_play(owner)


class TestLivingCharactersAndShares:
    def test_flow(self, owner, play):
        pid = play["playthrough_id"]
        before = owner.get(f"{API}/playthroughs/{pid}").json()["view"]
        # snapshot share before acting
        r = owner.post(f"{API}/playthroughs/{pid}/shares", json={"mode": "snapshot"})
        assert r.status_code == 200, r.text
        snap = r.json()
        assert snap["mode"] == "snapshot" and snap["active"] is True
        live = owner.post(f"{API}/playthroughs/{pid}/shares", json={"mode": "live"}).json()
        pub0 = requests.get(f"{API}/public/stories/{snap['share_id']}")
        assert pub0.status_code == 200
        b0 = pub0.json()
        assert b0["theme"] and b0["chapters"] and b0["mode"] == "snapshot"
        n0 = sum(len(c["entries"]) for c in b0["chapters"])

        r = owner.post(f"{API}/playthroughs/{pid}/act", timeout=180, json={
            "declaration": "I climb onto a barrel and proclaim to the whole quay that the King's fleet sails at dawn and every man shall be paid double."})
        assert r.status_code == 200, r.text
        assert r.json()["playthrough"]["view"]["npc_pending"] is True
        cond_after_act = r.json()["playthrough"]["view"]["character"]["condition"]

        d, took = _wait_npc(owner, pid, 60)
        print(f"npc resolved in {took}s")
        assert took is not None, "npc_pending never cleared"
        v = d["view"]
        assert v["character"]["condition"] == cond_after_act
        assert v["inventory"] == before["inventory"]
        chron = owner.get(f"{API}/playthroughs/{pid}/chronicle").json()
        npc = [e for e in chron if e["kind"] == "npc_action"]
        print(f"npc events: {len(npc)} -> {[(e['npc_kind'], e['effect']) for e in npc]}")
        assert len(npc) <= 6
        for e in npc:
            assert e["npc_kind"] in ("disposition", "move", "rumour") and e["effect"]
        for a in v["known_actors"]:
            assert "disposition" in a and "location" in a
        if any(e["npc_kind"] == "rumour" for e in npc):
            assert v["rumours"]

        # snapshot frozen; live updated
        b1 = requests.get(f"{API}/public/stories/{snap['share_id']}").json()
        assert sum(len(c["entries"]) for c in b1["chapters"]) == n0
        bl = requests.get(f"{API}/public/stories/{live['share_id']}").json()
        assert bl["mode"] == "live" and bl["turns"] == 1
        assert sum(len(c["entries"]) for c in bl["chapters"]) > n0

        # listing
        ids = [x["share_id"] for x in owner.get(f"{API}/playthroughs/{pid}/shares").json()]
        assert snap["share_id"] in ids and live["share_id"] in ids

        # other user cannot list/revoke
        other = _new_user()
        assert other.get(f"{API}/playthroughs/{pid}/shares").status_code == 404
        assert other.delete(f"{API}/shares/{live['share_id']}").status_code == 404
        assert other.post(f"{API}/playthroughs/{pid}/shares", json={"mode": "live"}).status_code == 404

        # revoke
        assert owner.delete(f"{API}/shares/{snap['share_id']}").status_code == 200
        assert requests.get(f"{API}/public/stories/{snap['share_id']}").status_code == 404
        ids = [x["share_id"] for x in owner.get(f"{API}/playthroughs/{pid}/shares").json()]
        assert snap["share_id"] not in ids
        owner.delete(f"{API}/shares/{live['share_id']}")

    def test_invalid_mode(self, owner, play):
        r = owner.post(f"{API}/playthroughs/{play['playthrough_id']}/shares", json={"mode": "forever"})
        assert r.status_code == 400

    def test_unauth(self, play):
        assert requests.get(f"{API}/playthroughs/{play['playthrough_id']}/shares").status_code == 401
        assert requests.get(f"{API}/public/stories/doesnotexist").status_code == 404
