# Iteration 8: Content Library v0.5 catalogue, Review-before-commit, idempotent saved request, Trash/delete forever, CSRF/CORS/STT security
import os
import io
import uuid

import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"
EVIL = "https://evil.example"
HOST = BASE_URL.split("://", 1)[-1]


def _s(token):
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
    return s


@pytest.fixture(scope="module")
def admin():
    r = requests.post(f"{API}/auth/login", json={"email": "admin", "password": "chronicle123"})
    assert r.status_code == 200, r.text
    return _s(r.json()["token"])


@pytest.fixture(scope="module")
def player():
    r = requests.post(f"{API}/auth/register", json={"email": f"test_it8_{uuid.uuid4().hex[:8]}@example.com", "password": "Passw0rd!"})
    assert r.status_code == 200, r.text
    return _s(r.json()["token"])


def _new_play(s):
    camp = s.get(f"{API}/campaigns/hyw-1415").json()
    bg = camp["character_backgrounds"][0]
    ch = s.post(f"{API}/characters", json={"scenario_id": "hyw-1415", "name": "TEST_Iter8", "background_id": bg["id"], "attributes": bg["attributes"]})
    assert ch.status_code == 200, ch.text
    p = s.post(f"{API}/playthroughs", json={"character_id": ch.json()["character_id"]})
    assert p.status_code == 200, p.text
    return p.json()


def _journal_len(s, pid):
    d = s.get(f"{API}/playthroughs/{pid}").json()
    st = d.get("state") or d
    return len(st.get("journal", [])), d


# --- Catalogue v0.5
class TestCatalogue:
    def test_admin_catalogue(self, admin):
        r = admin.get(f"{API}/catalogue")
        assert r.status_code == 200
        d = r.json()
        assert d["version"] == "0.5.0"
        assert len(d["records"]) == 44
        playable = [x for x in d["records"] if x["playable"]]
        assert len(playable) == 1 and playable[0]["id"] == "MC-01" and playable[0]["scenario_id"] == "hyw-1415"
        assert all(x.get("theme") for x in d["records"])

    def test_player_catalogue_only_playable(self, player):
        d = player.get(f"{API}/catalogue").json()
        assert len(d["records"]) == 1 and d["records"][0]["playable"]

    def test_hyw_campaign_tier(self, admin):
        camps = admin.get(f"{API}/campaigns").json()
        camps = camps if isinstance(camps, list) else camps.get("campaigns", [])
        hyw = next(c for c in camps if c.get("scenario_id", c.get("id")) == "hyw-1415")
        assert hyw["catalogue"]["tier"] == "Major Campaign"

    def test_catalogue_requires_auth(self):
        assert requests.get(f"{API}/catalogue").status_code == 401


# --- Review / Act / Trash on a throwaway playthrough
@pytest.fixture(scope="module")
def pt(player):
    return _new_play(player)


class TestReviewAndTrash:
    def test_review_no_commit(self, player, pt):
        pid = pt["playthrough_id"]
        before, _ = _journal_len(player, pid)
        r = player.post(f"{API}/playthroughs/{pid}/review", json={"declaration": "I look around the camp carefully"}, timeout=90)
        assert r.status_code == 200, r.text
        d = r.json()
        assert d["ok"] is True and d["intent"]
        after, _ = _journal_len(player, pid)
        assert after == before

    def test_review_gibberish_rejected(self, player, pt):
        r = player.post(f"{API}/playthroughs/{pid_of(pt)}/review", json={"declaration": "asdkj qwpoe zxmn"}, timeout=90)
        assert r.status_code == 200
        print("gibberish:", r.json())
        assert r.json()["ok"] is False

    def test_review_too_long_rejected(self, player, pt):
        r = player.post(f"{API}/playthroughs/{pid_of(pt)}/review", json={"declaration": "I walk " * 400}, timeout=90)
        assert r.status_code == 200
        assert r.json()["ok"] is False

    def test_act_idempotent_replay(self, player, pt):
        pid = pid_of(pt)
        rid = f"req_{uuid.uuid4().hex[:10]}"
        body = {"declaration": "I look around the camp carefully", "request_id": rid}
        r1 = player.post(f"{API}/playthroughs/{pid}/act", json=body, timeout=180)
        assert r1.status_code == 200, r1.text
        n1, _ = _journal_len(player, pid)
        r2 = player.post(f"{API}/playthroughs/{pid}/act", json=body, timeout=180)
        assert r2.status_code == 200, r2.text
        assert r2.json().get("replayed") is True and r2.json()["event_id"] == r1.json()["event_id"]
        n2, _ = _journal_len(player, pid)
        assert n1 == n2

    def test_delete_non_trashed_400(self, player, pt):
        assert player.delete(f"{API}/playthroughs/{pid_of(pt)}").status_code == 400

    def test_trash_blocks_act_review_passtime(self, player, pt):
        pid = pid_of(pt)
        r = player.post(f"{API}/playthroughs/{pid}/trash")
        assert r.status_code == 200 and r.json()["status"] == "trashed"
        lst = player.get(f"{API}/playthroughs", params={"status": "trashed"}).json()
        assert any(p["playthrough_id"] == pid for p in lst)
        assert player.post(f"{API}/playthroughs/{pid}/act", json={"declaration": "I wait"}, timeout=60).status_code == 400
        assert player.post(f"{API}/playthroughs/{pid}/pass-time", json={"span": "hours"}).status_code == 400
        assert player.post(f"{API}/playthroughs/{pid}/review", json={"declaration": "I wait"}).status_code == 400

    def test_restore_then_delete_forever(self, player, pt):
        pid = pid_of(pt)
        r = player.post(f"{API}/playthroughs/{pid}/restore")
        assert r.status_code == 200 and r.json()["status"] == "active"
        _, d = _journal_len(player, pid)
        assert d.get("status") == "active"
        # add note + share, then trash + delete
        assert player.post(f"{API}/playthroughs/{pid}/notes", json={"title": "TEST_note"}).status_code in (200, 201)
        sh = player.post(f"{API}/playthroughs/{pid}/shares", json={"mode": "snapshot"})
        assert sh.status_code in (200, 201)
        share_id = sh.json()["share_id"]
        player.post(f"{API}/playthroughs/{pid}/trash")
        r = player.delete(f"{API}/playthroughs/{pid}")
        assert r.status_code == 200 and r.json()["ok"] is True
        assert player.get(f"{API}/playthroughs/{pid}").status_code == 404
        assert requests.get(f"{API}/public/stories/{share_id}").status_code in (404, 410) or \
            requests.get(f"{API}/story/{share_id}").status_code in (404, 410)
        saves = player.get(f"{API}/playthroughs/{pid}/saves")
        assert saves.status_code == 404

    def test_other_user_cannot_trash(self, admin, player):
        p = _new_play(player)
        assert admin.post(f"{API}/playthroughs/{p['playthrough_id']}/trash").status_code == 404
        player.post(f"{API}/playthroughs/{p['playthrough_id']}/trash")
        player.delete(f"{API}/playthroughs/{p['playthrough_id']}")


def pid_of(pt):
    return pt["playthrough_id"]


# --- Security
class TestSecurity:
    @pytest.mark.parametrize("path", ["auth/me", "playthroughs", "catalogue"])
    def test_no_acac_for_evil(self, admin, path):
        r = admin.get(f"{API}/{path}", headers={"Origin": EVIL})
        assert r.headers.get("access-control-allow-credentials", "").lower() != "true"
        r = requests.options(f"{API}/{path}", headers={"Origin": EVIL, "Access-Control-Request-Method": "POST"})
        assert r.headers.get("access-control-allow-credentials", "").lower() != "true"

    def _cookie_session(self):
        s = requests.Session()
        r = s.post(f"{API}/auth/login", json={"email": "admin", "password": "chronicle123"})
        assert r.status_code == 200
        assert s.cookies, "no auth cookie set"
        return s

    def test_logout_evil_origin_cookie_403(self):
        s = self._cookie_session()
        r = s.post(f"{API}/auth/logout", headers={"Origin": EVIL})
        assert r.status_code == 403, r.text

    def test_logout_own_origin_cookie_200(self):
        s = self._cookie_session()
        r = s.post(f"{API}/auth/logout", headers={"Origin": BASE_URL})
        assert r.status_code == 200, r.text

    def test_bearer_never_blocked(self, admin):
        r = admin.post(f"{API}/playthroughs/nonexistent_x/trash", headers={"Origin": EVIL})
        assert r.status_code == 404  # reached the handler, not 403

    def test_bearer_plus_cookie_evil_not_blocked(self):
        s = self._cookie_session()
        tok = requests.post(f"{API}/auth/login", json={"email": "admin", "password": "chronicle123"}).json()["token"]
        r = s.post(f"{API}/playthroughs/nonexistent_x/trash", headers={"Origin": EVIL, "Authorization": f"Bearer {tok}"})
        assert r.status_code == 404

    def test_stt_junk_422(self, admin):
        h = {"Authorization": admin.headers["Authorization"]}
        r = requests.post(f"{API}/voice/stt", headers=h, files={"file": ("a.webm", io.BytesIO(b"not audio at all" * 100), "audio/webm")}, timeout=90)
        assert r.status_code == 422, r.text
        assert "transcribe" in r.json()["detail"]

    def test_stt_too_big_400(self, admin):
        h = {"Authorization": admin.headers["Authorization"]}
        r = requests.post(f"{API}/voice/stt", headers=h, files={"file": ("a.webm", io.BytesIO(b"0" * (25 * 1024 * 1024 + 10)), "audio/webm")}, timeout=120)
        assert r.status_code in (400, 413), r.text
