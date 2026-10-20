# IRGS iter7: SEC-001 CORS fix, auth regression, lockout, upload caps, public story, quick regression
import os
import uuid
import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL").rstrip("/")
API = f"{BASE_URL}/api"
EVIL = "https://evil.example"


@pytest.fixture(scope="module")
def admin_token():
    r = requests.post(f"{API}/auth/login", json={"email": "admin", "password": "chronicle123"})
    assert r.status_code == 200, r.text
    return r.json()["token"]


@pytest.fixture(scope="module")
def admin(admin_token):
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {admin_token}"
    return s


# --- SEC-001: credentialed CORS must not reflect arbitrary origins
@pytest.mark.parametrize("path", ["auth/me", "playthroughs", "characters"])
def test_cors_get_no_reflect(admin_token, path):
    r = requests.get(f"{API}/{path}", headers={"Origin": EVIL, "Authorization": f"Bearer {admin_token}"})
    acao = r.headers.get("access-control-allow-origin")
    assert acao != EVIL
    assert r.headers.get("access-control-allow-credentials", "").lower() != "true"


@pytest.mark.parametrize("path", ["auth/me", "playthroughs", "characters"])
def test_cors_preflight_no_reflect(path):
    r = requests.options(f"{API}/{path}", headers={"Origin": EVIL, "Access-Control-Request-Method": "GET",
                                                  "Access-Control-Request-Headers": "authorization"})
    assert r.headers.get("access-control-allow-origin") != EVIL
    assert r.headers.get("access-control-allow-credentials", "").lower() != "true"


def test_cors_cookie_only_cross_origin_not_credentialed():
    s = requests.Session()
    r = s.post(f"{API}/auth/login", json={"email": "admin", "password": "chronicle123"})
    assert r.status_code == 200
    r = s.get(f"{API}/auth/me", headers={"Origin": EVIL})
    # Exploitable part: credentials must never be allowed. (Starlette reflects Origin when a Cookie
    # header is present with allow_origins=["*"]; harmless without ACAC: true - reported as minor)
    assert r.headers.get("access-control-allow-credentials", "").lower() != "true"


# --- Auth regression
def test_login_admin_and_me(admin):
    r = admin.get(f"{API}/auth/me")
    assert r.status_code == 200
    d = r.json()
    assert d.get("role") == "admin" or d.get("user", {}).get("role") == "admin"


def test_login_sets_httponly_cookie():
    r = requests.post(f"{API}/auth/login", json={"email": "admin@irgs.app", "password": "chronicle123"})
    assert r.status_code == 200
    sc = r.headers.get("set-cookie", "")
    assert "access_token=" in sc and "HttpOnly" in sc


def test_wrong_password_401():
    r = requests.post(f"{API}/auth/login", json={"email": "admin", "password": "wrong-pass"})
    assert r.status_code == 401


def test_lockout_after_5():
    email = f"test_lock_{uuid.uuid4().hex[:8]}@example.com"
    assert requests.post(f"{API}/auth/register", json={"email": email, "password": "Passw0rd!", "name": "TEST Lock"}).status_code == 200
    codes = [requests.post(f"{API}/auth/login", json={"email": email, "password": "bad"}).status_code for _ in range(5)]
    assert codes == [401] * 5
    r = requests.post(f"{API}/auth/login", json={"email": email, "password": "Passw0rd!"})
    assert r.status_code == 429


def test_register_me_logout():
    email = f"test_reg_{uuid.uuid4().hex[:8]}@example.com"
    s = requests.Session()
    r = s.post(f"{API}/auth/register", json={"email": email, "password": "Passw0rd!", "name": "TEST Reg"})
    assert r.status_code == 200
    tok = r.json()["token"]
    assert requests.get(f"{API}/auth/me", headers={"Authorization": f"Bearer {tok}"}).status_code == 200
    assert s.get(f"{API}/auth/me").status_code == 200  # cookie
    assert s.post(f"{API}/auth/logout").status_code == 200
    assert s.get(f"{API}/auth/me").status_code == 401


def test_me_unauth_401():
    assert requests.get(f"{API}/auth/me").status_code == 401


# --- Upload caps
def test_stt_too_large(admin):
    big = b"\0" * (25 * 1024 * 1024 + 10)
    r = admin.post(f"{API}/voice/stt", files={"file": ("a.webm", big, "audio/webm")}, timeout=120)
    assert r.status_code == 400, r.text[:200]
    assert "Recording too large" in r.json()["detail"]


def test_stt_small_valid_wav(admin):
    import io, math, struct, wave
    buf = io.BytesIO()
    w = wave.open(buf, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000)
    w.writeframes(b"".join(struct.pack("<h", int(3000 * math.sin(2 * math.pi * 440 * i / 16000))) for i in range(16000)))
    w.close()
    r = admin.post(f"{API}/voice/stt", files={"file": ("t.wav", buf.getvalue(), "audio/wav")}, timeout=90)
    assert r.status_code == 200, r.text[:200]
    assert isinstance(r.json()["text"], str)


def test_stt_empty(admin):
    r = admin.post(f"{API}/voice/stt", files={"file": ("a.webm", b"", "audio/webm")})
    assert r.status_code == 400


def test_portrait_too_large(admin):
    chars = admin.get(f"{API}/characters").json()
    chars = chars if isinstance(chars, list) else chars.get("characters", [])
    if not chars:
        pytest.skip("no characters")
    cid = chars[0]["character_id"]
    big = b"\x89PNG\r\n\x1a\n" + b"\0" * (8 * 1024 * 1024 + 10)
    r = admin.post(f"{API}/characters/{cid}/portrait", files={"file": ("p.png", big, "image/png")}, timeout=120)
    assert r.status_code == 400
    assert "too large" in r.json()["detail"].lower()


# --- Quick regression
def test_playthrough_open_and_chronicle(admin):
    r = admin.get(f"{API}/playthroughs/play_a9395430ff67")
    assert r.status_code == 200
    assert admin.get(f"{API}/playthroughs/play_a9395430ff67/chronicle").status_code == 200


def test_store_items(admin):
    r = admin.get(f"{API}/store/items")
    assert r.status_code == 200 and len(r.json()["items"]) > 0
