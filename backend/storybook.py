"""Shareable storybook: turns a playthrough's Chronicle into public, read-only chapters."""
from engine import player_view

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV",
         "XVI", "XVII", "XVIII", "XIX", "XX"]


def build_storybook(doc: dict, scenario: dict, file_url) -> dict:
    state = doc["state"]
    view = player_view(state)
    names = {aid: a["name"] for aid, a in state["actors"].items()}
    chapters, current = [], None
    for e in state.get("journal", []):
        date = e.get("campaign_date") or scenario["opening"]["date"]
        if not current or current["date"] != date:
            n = len(chapters)
            current = {"title": f"Chapter {ROMAN[n] if n < len(ROMAN) else n + 1}", "date": date, "entries": []}
            chapters.append(current)
        current["entries"].append({
            "id": e["id"], "kind": e.get("kind"), "declaration": e.get("declaration"),
            "text": e.get("narration") or e.get("text") or "",
            "time": e.get("campaign_time"),
            "image_url": file_url(e.get("image_path")),
            "actor": names.get((e.get("actor_ids") or [None])[0]) if e.get("kind") == "npc_action" else None,
        })
    return {
        "title": doc.get("title"), "campaign_title": scenario["campaign_title"], "scenario_title": scenario["title"],
        "era": scenario["era"], "theme": scenario["theme"], "calendar": view["campaign_time"]["calendar"],
        "cover_image": scenario["cover_image"], "portrait_url": file_url(doc.get("portrait_path")),
        "character": {"name": view["character"]["name"], "background": view["background"]},
        "turns": state["clock"], "chapters": chapters,
    }
