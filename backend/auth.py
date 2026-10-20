"""Authentication: JWT email/password + Emergent-managed Google session login."""
import os
import re
import jwt
import bcrypt
import logging
from datetime import datetime, timezone, timedelta

import requests
from fastapi import HTTPException, Request

from db import db, now_iso, new_id

logger = logging.getLogger("irgs.auth")
JWT_ALGORITHM = "HS256"
EMERGENT_SESSION_URL = "https://demobackend.emergentagent.com/auth/v1/env/oauth/session-data"


def get_jwt_secret() -> str:
    return os.environ["JWT_SECRET"]


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False


def create_access_token(user_id: str, email: str) -> str:
    payload = {"sub": user_id, "email": email, "type": "access",
               "exp": datetime.now(timezone.utc) + timedelta(days=7)}
    return jwt.encode(payload, get_jwt_secret(), algorithm=JWT_ALGORITHM)


def _public_user(doc: dict) -> dict:
    return {
        "user_id": doc["user_id"], "email": doc.get("email"), "name": doc.get("name"),
        "picture": doc.get("picture"), "role": doc.get("role", "player"),
        "auth": doc.get("auth", "password"),
    }


async def _find_user(user_id=None, email=None, username=None):
    if user_id:
        q = {"user_id": user_id}
    elif username:
        q = {"username": username.lower()}
    else:
        q = {"email": (email or "").lower()}
    return await db.users.find_one(q, {"_id": 0})


async def register_user(email: str, password: str, name: str):
    email = (email or "").lower().strip()
    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required")
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        raise HTTPException(status_code=400, detail="Please enter a valid email address")
    if len(password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters")
    if await _find_user(email=email):
        raise HTTPException(status_code=400, detail="An account with this email already exists")
    user_id = new_id("user")
    doc = {
        "user_id": user_id, "email": email, "name": name or email.split("@")[0],
        "password_hash": hash_password(password), "role": "player", "auth": "password",
        "picture": None, "created_at": now_iso(),
    }
    await db.users.insert_one(doc)
    return _public_user(doc), create_access_token(user_id, email)


async def login_user(email: str, password: str):
    email = (email or "").lower().strip()
    identifier = email
    if not email or not password:
        raise HTTPException(status_code=400, detail="Enter your email or username and password")
    attempts = await db.login_attempts.find_one({"identifier": identifier}) or {}
    if attempts.get("count", 0) >= 5:
        locked_until = attempts.get("locked_until")
        if locked_until and datetime.fromisoformat(locked_until) > datetime.now(timezone.utc):
            raise HTTPException(status_code=429, detail="Too many attempts. Try again in a few minutes.")
    user = await _find_user(email=email) if "@" in email else await _find_user(username=email)
    if not user or not verify_password(password, user.get("password_hash", "")):
        new_count = attempts.get("count", 0) + 1
        await db.login_attempts.update_one(
            {"identifier": identifier},
            {"$set": {"count": new_count,
                      "locked_until": (datetime.now(timezone.utc) + timedelta(minutes=15)).isoformat()}},
            upsert=True,
        )
        raise HTTPException(status_code=401, detail="Invalid email or password")
    await db.login_attempts.delete_one({"identifier": identifier})
    return _public_user(user), create_access_token(user["user_id"], user.get("email") or email)


async def process_google_session(session_id: str):
    """Exchange an Emergent OAuth session_id for user data + session_token."""
    try:
        resp = requests.get(EMERGENT_SESSION_URL, headers={"X-Session-ID": session_id}, timeout=20)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logger.error(f"google session exchange failed: {e}")
        raise HTTPException(status_code=401, detail="Google sign-in failed")
    email = (data.get("email") or "").lower()
    user = await _find_user(email=email)
    if not user:
        user_id = new_id("user")
        doc = {
            "user_id": user_id, "email": email, "name": data.get("name"),
            "picture": data.get("picture"), "role": "player", "auth": "google",
            "created_at": now_iso(),
        }
        await db.users.insert_one(doc)
        user = doc
    else:
        await db.users.update_one({"user_id": user["user_id"]},
                                  {"$set": {"name": data.get("name"), "picture": data.get("picture")}})
    session_token = data["session_token"]
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    await db.user_sessions.insert_one({
        "user_id": user["user_id"], "session_token": session_token,
        "expires_at": expires_at.isoformat(), "created_at": now_iso(),
    })
    return _public_user(user), session_token


async def get_current_user(request: Request) -> dict:
    """Resolve the current user from a JWT (cookie/bearer) or a Google session token."""
    token = request.cookies.get("access_token")
    if not token:
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Bearer "):
            token = auth[7:]
    if not token:
        token = request.cookies.get("session_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # 1) try JWT
    try:
        payload = jwt.decode(token, get_jwt_secret(), algorithms=[JWT_ALGORITHM])
        user = await _find_user(user_id=payload.get("sub"))
        if user:
            return _public_user(user)
    except jwt.InvalidTokenError:
        pass

    # 2) try Google session token
    session = await db.user_sessions.find_one({"session_token": token})
    if session:
        expires_at = session["expires_at"]
        if isinstance(expires_at, str):
            expires_at = datetime.fromisoformat(expires_at)
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if expires_at > datetime.now(timezone.utc):
            user = await _find_user(user_id=session["user_id"])
            if user:
                return _public_user(user)
    raise HTTPException(status_code=401, detail="Invalid or expired session")


async def seed_admin():
    admin_email = (os.environ.get("ADMIN_EMAIL") or "").lower()
    admin_password = os.environ.get("ADMIN_PASSWORD") or ""
    admin_username = (os.environ.get("ADMIN_USERNAME") or "").lower()
    if not (admin_email and admin_username and len(admin_password) >= 8):
        logger.warning("Admin seeding skipped: ADMIN_EMAIL / ADMIN_USERNAME / ADMIN_PASSWORD (8+ chars) not configured")
        return
    existing = await db.users.find_one({"email": admin_email})
    if existing is None:
        await db.users.insert_one({
            "user_id": new_id("user"), "email": admin_email, "username": admin_username,
            "password_hash": hash_password(admin_password), "name": "Game Master",
            "role": "admin", "auth": "password", "picture": None, "created_at": now_iso(),
        })
    else:
        upd = {"username": admin_username, "role": "admin"}
        if not verify_password(admin_password, existing.get("password_hash", "")):
            upd["password_hash"] = hash_password(admin_password)
        await db.users.update_one({"email": admin_email}, {"$set": upd})
