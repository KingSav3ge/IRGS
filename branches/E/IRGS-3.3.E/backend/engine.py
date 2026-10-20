"""IRGS simulation core — the authoritative state model and action pipeline.

Faithful to the Master Codex intent: Core is the single source of truth. The AI
only narrates (presentation); it never mutates world state. Every committed
action advances the world clock, is journaled (the Chronicle source of truth)
and makes the state durably recoverable.

Pipeline: intent -> interpret -> validate -> resolve -> commit -> chronicle.
"""
import copy
from datetime import datetime, timezone

CLOCK_MINUTES_PER_ACTION = 30  # bounded, deterministic time advance per committed action

# action-intent categories produced by the Jev decision layer
INTENT_CATEGORIES = ("move", "speak", "observe", "interact", "combat", "rest", "other")


def _now():
    return datetime.now(timezone.utc).isoformat()


def build_initial_state(scenario: dict, character: dict) -> dict:
    """Construct the authoritative opening state from a validated scenario + player character.

    Presentation only for the opening block; applies no resolved effects.
    """
    player_id = "PLAYER-01"
    actor = {
        "id": player_id,
        "name": character["name"],
        "species": character.get("species", "human"),
        "role": character.get("background_label") or character.get("role") or "",
        "current": {
            "location": scenario["opening"]["location"],
            "condition": {
                "health": 100,
                "stamina": 100,
                "morale": 70,
            },
            "activity": "Awaiting your first decision.",
        },
    }
    npc_actors = {}
    for a in scenario.get("actors", []):
        npc_actors[a["id"]] = {
            "id": a["id"], "name": a["name"], "species": a.get("species", "human"),
            "role": a.get("role", ""), "current": {},
        }

    opening_block = {
        "kind": "opening_scene",
        "title": "Opening · " + scenario["opening"]["label"],
        "text": scenario["briefing"],
        "setting": scenario["opening"].get("setting", ""),
    }

    state = {
        "campaign_id": scenario["campaign_id"],
        "scenario_id": scenario["id"],
        "clock": 0,
        "campaign_time": {
            "date": scenario["opening"]["date"],
            "calendar": scenario["opening"].get("calendar", "gregorian"),
            "precision": scenario["opening"].get("precision", "day"),
            "time": scenario["opening"].get("time", "dawn"),
        },
        "player_actor_id": player_id,
        "actors": {player_id: actor, **npc_actors},
        "locations": {loc["id"]: loc for loc in scenario.get("locations", [])},
        "inventory": copy.deepcopy(character.get("inventory", [])),
        "world_facts": copy.deepcopy(scenario.get("world_facts", [])),
        "attributes": copy.deepcopy(character.get("attributes", {})),
        "background": character.get("background_label", ""),
        "testimony": copy.deepcopy(character.get("testimony") or {}),
        "opening": opening_block,
        "journal": [
            {
                "id": "evt_opening",
                "op": "set_scene",
                "kind": "opening_scene",
                "title": opening_block["title"],
                "text": scenario["briefing"],
                "actor_ids": [player_id],
                "at": 0,
                "status": "presented",
                "wall_clock": _now(),
            }
        ],
        "pending_action": None,
    }
    return state


def advance_time(campaign_time: dict, minutes: int, steps: int = 1) -> dict:
    """Deterministic, in-world clock advance. Save/navigation never calls this."""
    ct = copy.deepcopy(campaign_time)
    order = ["dawn", "morning", "midday", "afternoon", "evening", "night"]
    cur = ct.get("time") or "dawn"
    try:
        idx = order.index(cur)
    except ValueError:
        idx = 0
    # each step nudges the time band forward; every wrap advances the date
    new_idx = idx + steps
    for _ in range(new_idx // len(order)):
        ct["date"] = _increment_date(ct.get("date"))
    ct["time"] = order[new_idx % len(order)]
    return ct


def _increment_date(date_str):
    try:
        from datetime import date, timedelta
        y, m, d = (int(x) for x in str(date_str).split("-"))
        nd = date(y, m, d) + timedelta(days=1)
        return nd.isoformat()
    except Exception:
        parts = str(date_str).split("-")
        try:
            parts[-1] = f"{int(parts[-1]) + 1:02d}"
            return "-".join(parts)
        except ValueError:
            return date_str


def validate_action(state: dict, declaration: str) -> dict:
    """Core validation gate. Returns {'ok': bool, 'reason': str}."""
    if state.get("pending_action"):
        return {"ok": False, "reason": "An unresolved declaration is still pending. Withdraw it first."}
    if not declaration or not declaration.strip():
        return {"ok": False, "reason": "An action declaration cannot be empty."}
    if len(declaration) > 2000:
        return {"ok": False, "reason": "Declaration is too long."}
    player = state["actors"].get(state["player_actor_id"])
    if not player:
        return {"ok": False, "reason": "No controlled player character exists in this playthrough."}
    if player["current"]["condition"]["health"] <= 0:
        return {"ok": False, "reason": "Your character is incapacitated and cannot act."}
    return {"ok": True, "reason": ""}


def resolve_and_commit(state: dict, declaration: str, intent_category: str, narration: str) -> dict:
    """Apply the authoritative, bounded resolution and journal the committed event.

    The narration text is presentation supplied by the AI layer; the mechanical
    effects here are the Core's own deterministic resolution.
    """
    state = copy.deepcopy(state)
    player = state["actors"][state["player_actor_id"]]
    cond = player["current"]["condition"]

    # bounded deterministic effects by intent category
    if intent_category == "combat":
        cond["stamina"] = max(0, cond["stamina"] - 20)
        cond["morale"] = max(0, min(100, cond["morale"] - 3))
    elif intent_category == "move":
        cond["stamina"] = max(0, cond["stamina"] - 8)
    elif intent_category == "rest":
        cond["stamina"] = min(100, cond["stamina"] + 25)
        cond["morale"] = min(100, cond["morale"] + 5)
    else:
        cond["stamina"] = max(0, cond["stamina"] - 3)

    state["clock"] += 1
    state["campaign_time"] = advance_time(state["campaign_time"], CLOCK_MINUTES_PER_ACTION)
    player["current"]["activity"] = declaration.strip()[:240]

    event = {
        "id": f"evt_{state['clock']:05d}",
        "op": "record_player_action",
        "kind": "player_action",
        "intent": intent_category,
        "title": "Player declaration",
        "declaration": declaration.strip(),
        "narration": narration,
        "actor_ids": [state["player_actor_id"]],
        "at": state["clock"],
        "status": "resolved",
        "campaign_date": state["campaign_time"]["date"],
        "campaign_time": state["campaign_time"]["time"],
        "wall_clock": _now(),
        "condition_after": copy.deepcopy(cond),
    }
    state["journal"].append(event)
    state["pending_action"] = None
    return state


def player_view(state: dict) -> dict:
    """Player-safe projection of the authoritative state for the Play screen."""
    player = state["actors"][state["player_actor_id"]]
    known = [
        {"id": a["id"], "name": a["name"], "role": a.get("role", ""),
         "disposition": a.get("current", {}).get("disposition", 0),
         "location": a.get("current", {}).get("location")}
        for aid, a in state["actors"].items()
        if aid != state["player_actor_id"]
    ]
    return {
        "scenario_id": state["scenario_id"],
        "campaign_id": state["campaign_id"],
        "clock": state["clock"],
        "campaign_time": state["campaign_time"],
        "character": {
            "id": player["id"],
            "name": player["name"],
            "role": player.get("role", ""),
            "condition": player["current"]["condition"],
            "location": player["current"].get("location"),
            "activity": player["current"].get("activity"),
        },
        "attributes": state.get("attributes", {}),
        "background": state.get("background", ""),
        "inventory": state.get("inventory", []),
        "known_actors": known,
        "world_facts": state.get("world_facts", []),
        "opening": state.get("opening"),
        "pending_action": state.get("pending_action"),
        "rumours": state.get("rumours", [])[-5:],
        "npc_pending": state.get("npc_pending", False),
    }


def chronicle_view(state: dict) -> list:
    """The Chronicle — a navigable log of committed events derived from the journal."""
    out = []
    for e in state.get("journal", []):
        out.append({
            "id": e["id"],
            "kind": e.get("kind", e.get("op")),
            "intent": e.get("intent"),
            "title": e.get("title", ""),
            "text": e.get("narration") or e.get("text") or e.get("declaration", ""),
            "declaration": e.get("declaration"),
            "actor_ids": e.get("actor_ids", []),
            "at": e.get("at", 0),
            "status": e.get("status", "recorded"),
            "campaign_date": e.get("campaign_date"),
            "campaign_time": e.get("campaign_time"),
            "wall_clock": e.get("wall_clock"),
            "big_moment": e.get("big_moment", False),
            "image_status": e.get("image_status"),
            "image_path": e.get("image_path"),
            "npc_kind": e.get("npc_kind"),
            "effect": e.get("effect"),
        })
    return out


NPC_ACTION_KINDS = ("disposition", "move", "rumour")
NPC_MAX_LOCAL, NPC_MAX_BROAD = 2, 6


def apply_npc_actions(state: dict, actions: list, scope: str = "local") -> dict:
    """Core gate for autonomous NPC actions: bounded, never touches the player's inventory or condition."""
    state = copy.deepcopy(state)
    pid = state["player_actor_id"]
    locs = {k.lower(): k for k in state.get("locations", {})}
    locs.update({v.get("name", "").lower(): k for k, v in state.get("locations", {}).items()})
    cap = NPC_MAX_BROAD if scope == "broad" else NPC_MAX_LOCAL
    seen, n = set(), 0
    for a in actions:
        if n >= cap:
            break
        if not isinstance(a, dict):
            continue
        aid, kind = a.get("actor_id"), a.get("kind")
        actor = state["actors"].get(aid)
        if not actor or aid == pid or kind not in NPC_ACTION_KINDS or (aid, kind) in seen:
            continue
        cur = actor.setdefault("current", {})
        summary = str(a.get("summary", "")).strip()[:400]
        if not summary:
            continue
        effect = {}
        if kind == "disposition":
            try:
                delta = max(-15, min(15, int(float(a.get("delta", 0) or 0))))
            except (TypeError, ValueError):
                continue
            if delta == 0:
                continue
            cur["disposition"] = max(-100, min(100, cur.get("disposition", 0) + delta))
            effect = {"disposition_delta": delta, "disposition": cur["disposition"]}
        elif kind == "move":
            loc = locs.get(str(a.get("location", "")).lower())
            if not loc or loc == cur.get("location"):
                continue
            cur["location"] = loc
            effect = {"location": loc}
        else:
            rumour = str(a.get("rumour") or summary)[:240]
            state.setdefault("rumours", []).append({"by": aid, "text": rumour, "at": state["clock"]})
            effect = {"rumour": rumour}
        seen.add((aid, kind))
        n += 1
        state["journal"].append({
            "id": f"evt_{state['clock']:05d}_npc{n}",
            "op": "npc_act", "kind": "npc_action", "intent": "npc", "npc_kind": kind,
            "title": f"{actor['name']} acts", "text": summary, "actor_ids": [aid],
            "at": state["clock"], "status": "resolved", "effect": effect,
            "campaign_date": state["campaign_time"]["date"], "campaign_time": state["campaign_time"]["time"],
            "wall_clock": _now(),
        })
    return state


TIME_SPANS = {
    "hours": {"steps": 1, "label": "A few hours pass", "stamina": 10, "morale": 0},
    "day": {"steps": 6, "label": "A day passes", "stamina": 40, "morale": 3},
    "week": {"steps": 42, "label": "A week passes", "stamina": 100, "morale": 5},
}


def pass_time(state: dict, span: str) -> dict:
    """Let time pass without a player action: bounded recovery, clock advance, journaled."""
    if state.get("pending_action"):
        raise ValueError("An unresolved declaration is still pending.")
    cfg = TIME_SPANS[span]
    state = copy.deepcopy(state)
    player = state["actors"][state["player_actor_id"]]
    cond = player["current"]["condition"]
    if cond["health"] <= 0:
        raise ValueError("Your character is incapacitated.")
    cond["stamina"] = min(100, cond["stamina"] + cfg["stamina"])
    cond["morale"] = min(100, cond["morale"] + cfg["morale"])
    before = copy.deepcopy(state["campaign_time"])
    state["clock"] += 1
    state["campaign_time"] = advance_time(state["campaign_time"], 0, cfg["steps"])
    player["current"]["activity"] = "Waiting while time passes."
    loc = player["current"].get("location", "")
    state["journal"].append({
        "id": f"evt_{state['clock']:05d}", "op": "pass_time", "kind": "time_passes", "intent": "time",
        "span": span, "title": cfg["label"],
        "text": f"{cfg['label']} at {loc}. From {before['date']} {before['time']} to "
                f"{state['campaign_time']['date']} {state['campaign_time']['time']}, the world goes on without you.",
        "actor_ids": [state["player_actor_id"]], "at": state["clock"], "status": "resolved",
        "campaign_date": state["campaign_time"]["date"], "campaign_time": state["campaign_time"]["time"],
        "wall_clock": _now(), "condition_after": copy.deepcopy(cond),
    })
    return state
