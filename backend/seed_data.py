"""Seed content: the Content Library scenarios and the Store catalog.

The Hundred Years' War 1415 opening is faithful to the uploaded IRGS source
(11 August 1415 Julian cutoff, before departure). Two additional seeded
scenarios (one historical, one medieval-fantasy) exercise the same engine.
"""

SCENARIOS = [
    {
        "id": "hyw-1415",
        "campaign_id": "hundred-years-war",
        "title": "The Lancastrian Invasion",
        "campaign_title": "Century of Conflict: The Hundred Years' War",
        "genre": "historical",
        "era": "1415 · Late Medieval",
        "difficulty": "Authentic",
        "premium": False,
        "price": 0,
        "tags": ["historical", "war", "england", "france", "sourced"],
        "cover_image": "https://images.pexels.com/photos/2873895/pexels-photo-2873895.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
        "summary": "A sourced historical opening frozen before Henry V's expedition crosses the Channel. Nothing beyond this dated cutoff has been decided — the war unfolds only through play.",
        "briefing": (
            "11 August 1415, before departure. Troops and shipping have gathered around Southampton, "
            "the Solent and Portchester. Henry V claims the French crown while Charles VI remains king of "
            "France, his government strained by the king's recurring incapacity and the rivalry of Armagnac "
            "and Burgundian interests. England already holds Calais and possessions in Gascony; broader "
            "claims do not amount to possession. The Winchester negotiations have failed. Embarkation is a "
            "live logistical undertaking — not proof that every contracted soldier, horse or vessel is "
            "present and ready. No crossing, landing, siege or battle has yet occurred in this playthrough."
        ),
        "opening": {
            "date": "1415-08-11",
            "calendar": "julian",
            "precision": "day",
            "time": "morning",
            "label": "11 August 1415 · before departure",
            "location": "Southampton Water",
            "setting": "The quays of Southampton Water, crowded with men, horses and provisioning barges.",
        },
        "actors": [
            {"id": "HYW-HENRY-V", "name": "Henry V", "role": "King of England; claimant to the French crown"},
            {"id": "HYW-CHARLES-VI", "name": "Charles VI", "role": "King of France"},
            {"id": "HYW-JOHN-FEARLESS", "name": "John the Fearless", "role": "Duke of Burgundy"},
            {"id": "HYW-JOHN-BEDFORD", "name": "John of Lancaster", "role": "Duke of Bedford; keeper of the realm"},
        ],
        "locations": [
            {"id": "Southampton Water", "name": "Southampton Water", "kind": "port"},
            {"id": "Portchester", "name": "Portchester Castle", "kind": "fortress"},
        ],
        "world_facts": [
            {"id": "HYW-1415-POL-01", "domain": "political",
             "statement": "Henry V rules England and asserts a claim to the French crown. His assertion is a claim, not evidence that France accepts his sovereignty.",
             "source_ids": ["HYW-SRC-ROYAL-HENRY", "HYW-SRC-JULY-DIPLOMACY"]},
            {"id": "HYW-1415-MIL-01", "domain": "military",
             "statement": "An English expeditionary force is assembling by contract. Embarkation is in progress; it is not complete.",
             "source_ids": ["HYW-SRC-APRIL-COUNCIL"]},
            {"id": "HYW-1415-TER-01", "domain": "territorial",
             "statement": "England holds Calais and possessions in Gascony. Wider claimed territory is not held.",
             "source_ids": ["HYW-SRC-CASTOR"]},
        ],
        "character_backgrounds": [
            {"id": "retinue-archer", "label": "Retinue Archer",
             "description": "A contracted longbowman in a lord's retinue, awaiting embarkation.",
             "attributes": {"strength": 6, "agility": 7, "wits": 4, "presence": 3}},
            {"id": "man-at-arms", "label": "Man-at-arms",
             "description": "A mounted soldier of some standing, bound by indenture.",
             "attributes": {"strength": 7, "agility": 5, "wits": 5, "presence": 5}},
            {"id": "clerk-victualler", "label": "Clerk of Victuals",
             "description": "A literate clerk managing provisioning accounts for the crossing.",
             "attributes": {"strength": 3, "agility": 4, "wits": 8, "presence": 6}},
        ],
        "default_inventory": [
            {"item": "Indenture roll", "qty": 1},
            {"item": "Travelling cloak", "qty": 1},
            {"item": "Few silver pennies", "qty": 1},
        ],
    },
    {
        "id": "rome-mercator",
        "campaign_id": "roman-republic",
        "title": "The Grain Fleet of Ostia",
        "campaign_title": "Mare Nostrum: The Late Republic",
        "genre": "historical",
        "era": "58 BCE · Roman Republic",
        "difficulty": "Measured",
        "premium": False,
        "price": 0,
        "tags": ["historical", "rome", "commerce", "politics"],
        "cover_image": "https://images.unsplash.com/photo-1724925742136-f620924e50b1?crop=entropy&cs=srgb&fm=jpg&q=85&w=940",
        "summary": "A merchant arrives at Ostia as grain ships ride at anchor and the politics of the late Republic churn ashore. Fortune and ruin are both a tide away.",
        "briefing": (
            "Late summer, 58 BCE. The harbour of Ostia is thick with grain ships from Sicily and Africa, "
            "their holds the lifeblood of the city upriver. Clodius agitates the plebs; the optimates mutter "
            "in the Curia. You are a trader with a modest cargo, a ledger of debts, and a name not yet made. "
            "Nothing here is decided for you — the markets, the mobs and the magistrates all move only once "
            "you act."
        ),
        "opening": {
            "date": "0058-08-20", "calendar": "roman", "precision": "day", "time": "midday",
            "label": "Late summer, 58 BCE · the harbour of Ostia",
            "location": "Ostia Harbour",
            "setting": "The crowded wharves of Ostia, salt and pitch in the air, the Tiber mouth glittering.",
        },
        "actors": [
            {"id": "ROM-CLODIUS", "name": "Publius Clodius", "role": "Tribune of the plebs"},
            {"id": "ROM-PORTMASTER", "name": "The Portmaster", "role": "Official of the Ostian docks"},
        ],
        "locations": [
            {"id": "Ostia Harbour", "name": "Ostia Harbour", "kind": "port"},
            {"id": "Forum Boarium", "name": "Forum Boarium", "kind": "market"},
        ],
        "world_facts": [
            {"id": "ROM-POL-01", "domain": "political",
             "statement": "The grain supply is a lever of Roman politics. Controlling it is controlling the mob's goodwill.",
             "source_ids": ["ROM-SRC-01"]},
        ],
        "character_backgrounds": [
            {"id": "merchant", "label": "Merchant (Mercator)",
             "description": "A trader with a modest cargo and ambitions larger than your purse.",
             "attributes": {"strength": 4, "agility": 4, "wits": 7, "presence": 7}},
            {"id": "freedman", "label": "Freedman",
             "description": "Recently freed, shrewd, and acutely aware of your place.",
             "attributes": {"strength": 5, "agility": 6, "wits": 6, "presence": 5}},
        ],
        "default_inventory": [
            {"item": "Wax ledger tablet", "qty": 1},
            {"item": "Purse of denarii", "qty": 1},
            {"item": "Letter of credit", "qty": 1},
        ],
    },
    {
        "id": "eldoria-shadows",
        "campaign_id": "eldoria",
        "title": "Shadows over Eldoria",
        "campaign_title": "The Riven Crown",
        "genre": "fantasy",
        "era": "The Age of Ash",
        "difficulty": "Perilous",
        "premium": True,
        "price": 9.99,
        "tags": ["fantasy", "dark", "magic", "premium"],
        "cover_image": "https://images.unsplash.com/photo-1514539079130-25950c84af65?crop=entropy&cs=srgb&fm=jpg&q=85&w=940",
        "summary": "The old king is dead, the Riven Crown unclaimed, and something stirs beneath the fog-drowned keep of Eldoria. A premium medieval-fantasy campaign.",
        "briefing": (
            "Fog lies thick upon the valley of Eldoria, and Burg Eltz — the keep they call the Riven Seat — "
            "has gone silent. The old king is three days dead; no heir has stepped forward to claim the crown. "
            "The garrison watches the treeline. The priests speak of omens. You arrive at the gate with your "
            "own reasons and your own blade. Nothing has been promised to you here. What Eldoria becomes is "
            "written only by what you choose to do."
        ),
        "opening": {
            "date": "0000-00-03", "calendar": "eldoria", "precision": "day", "time": "evening",
            "label": "Third night of the king's death · the fog-drowned keep",
            "location": "Eldoria Gate",
            "setting": "The outer gatehouse of Burg Eltz, torches guttering against a wall of fog.",
        },
        "actors": [
            {"id": "ELD-CAPTAIN", "name": "Captain Vaell", "role": "Commander of the keep's garrison"},
            {"id": "ELD-PRIESTESS", "name": "Sister Maren", "role": "Keeper of the keep's shrine"},
        ],
        "locations": [
            {"id": "Eldoria Gate", "name": "Eldoria Gatehouse", "kind": "fortress"},
            {"id": "Riven Hall", "name": "The Riven Hall", "kind": "hall"},
        ],
        "world_facts": [
            {"id": "ELD-LORE-01", "domain": "political",
             "statement": "The Riven Crown confers rule only to one who can hold the keep. Claiming it is not holding it.",
             "source_ids": ["ELD-SRC-01"]},
        ],
        "character_backgrounds": [
            {"id": "sellsword", "label": "Sellsword",
             "description": "A blade for hire, drawn to Eldoria by rumour of a reward.",
             "attributes": {"strength": 7, "agility": 6, "wits": 4, "presence": 4}},
            {"id": "hedge-mage", "label": "Hedge Mage",
             "description": "A self-taught practitioner of small, dangerous magics.",
             "attributes": {"strength": 3, "agility": 5, "wits": 8, "presence": 5}},
            {"id": "exiled-noble", "label": "Exiled Noble",
             "description": "Once of the court, now returned with a claim and a grudge.",
             "attributes": {"strength": 5, "agility": 4, "wits": 6, "presence": 8}},
        ],
        "default_inventory": [
            {"item": "Worn blade", "qty": 1},
            {"item": "Oil lantern", "qty": 1},
            {"item": "Sealed letter", "qty": 1},
        ],
    },
    {
        "id": "meridian-drift",
        "campaign_id": "meridian",
        "title": "Drift at Meridian Station",
        "campaign_title": "Outer Reach: The Meridian Accord",
        "genre": "scifi",
        "era": "2189 · Outer System",
        "difficulty": "Measured",
        "premium": False,
        "price": 0,
        "tags": ["sci-fi", "station", "mystery", "politics"],
        "cover_image": "https://images.unsplash.com/photo-1774382137454-60281271e0a5?crop=entropy&cs=srgb&fm=jpg&q=85&w=940",
        "summary": "A mining relay at the edge of the system has lost contact with its corporate charter. Air, water and loyalty are all rationed. Nothing is resolved until you act.",
        "briefing": (
            "14 March 2189, station time 06:00. Meridian Station turns slowly above the ice moon Kessa. "
            "Three days ago the relay to the Halvorsen Charter went dark; no supply tender has been confirmed. "
            "Station Director Okafor insists the outage is technical. The miners' union is not convinced. "
            "You have just come off a shift rotation with clearance to the lower decks, a personal terminal and "
            "a debt to the station commissary. No mutiny, rescue or discovery has occurred in this playthrough."
        ),
        "opening": {
            "date": "2189-03-14", "calendar": "gregorian", "precision": "day", "time": "dawn",
            "label": "14 March 2189 · station time 06:00",
            "location": "Ring C Concourse",
            "setting": "The curved concourse of Ring C, ration kiosks shuttered, ice-light glowing through the viewport.",
        },
        "actors": [
            {"id": "MER-OKAFOR", "name": "Director Adaeze Okafor", "role": "Station Director, Halvorsen Charter"},
            {"id": "MER-VOSS", "name": "Teo Voss", "role": "Miners' union steward"},
            {"id": "MER-ANSEL", "name": "ANSEL", "role": "Station operations intelligence"},
        ],
        "locations": [
            {"id": "Ring C Concourse", "name": "Ring C Concourse", "kind": "habitat"},
            {"id": "Relay Spire", "name": "Relay Spire", "kind": "comms"},
        ],
        "world_facts": [
            {"id": "MER-OPS-01", "domain": "logistics",
             "statement": "Contact with the Halvorsen Charter was lost three days ago. The cause is unconfirmed.",
             "source_ids": ["MER-SRC-01"]},
            {"id": "MER-POL-01", "domain": "political",
             "statement": "The Director holds legal authority aboard; the union controls most of the working crews. Authority is not the same as obedience.",
             "source_ids": ["MER-SRC-02"]},
        ],
        "character_backgrounds": [
            {"id": "salvage-engineer", "label": "Salvage Engineer",
             "description": "You keep old machines breathing and know every crawlspace on the lower decks.",
             "attributes": {"strength": 6, "agility": 5, "wits": 7, "presence": 3}},
            {"id": "station-security", "label": "Station Security",
             "description": "A contracted officer whose loyalty is being tested by both sides.",
             "attributes": {"strength": 7, "agility": 6, "wits": 4, "presence": 5}},
            {"id": "xenolinguist", "label": "Signals Analyst",
             "description": "You read the relay traffic, and lately you have noticed patterns that should not be there.",
             "attributes": {"strength": 3, "agility": 4, "wits": 8, "presence": 6}},
        ],
        "default_inventory": [
            {"item": "Personal terminal", "qty": 1},
            {"item": "Lower-deck access card", "qty": 1},
            {"item": "Ration chits", "qty": 3},
        ],
    },
]

THEMES = {
    "hyw-1415": ("manuscript", "a medieval illuminated-manuscript painting with rich vellum textures and rubricated borders"),
    "rome-mercator": ("tablet", "a Roman fresco painted on weathered plaster, earthy pigments, carved stone framing"),
    "eldoria-shadows": ("grimoire", "a dark-fantasy oil painting, ember light and drifting fog, painterly brushwork"),
    "meridian-drift": ("pda", "cinematic science-fiction concept art, cold volumetric light, hard-surface detail"),
}
for _s in SCENARIOS:
    _s["theme"], _s["art_style"] = THEMES[_s["id"]]

STORE_ITEMS = [
    {
        "id": "pack-eldoria",
        "title": "Shadows over Eldoria",
        "kind": "campaign",
        "scenario_id": "eldoria-shadows",
        "price": 9.99,
        "description": "Unlock the premium medieval-fantasy campaign — the Riven Crown and the fog-drowned keep.",
        "image": "https://images.unsplash.com/photo-1514539079130-25950c84af65?crop=entropy&cs=srgb&fm=jpg&q=85&w=940",
    },
    {
        "id": "sub-elevenlabs-narration",
        "title": "ElevenLabs Narration",
        "kind": "subscription",
        "interval": "month",
        "scenario_id": None,
        "price": 5.99,
        "description": "Monthly add-on: premium ElevenLabs narrator voices for cinematic story readings. Standard voice narration stays free.",
        "image": "https://images.pexels.com/photos/11882036/pexels-photo-11882036.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    },
    {
        "id": "pack-portraits",
        "title": "Illuminated Portrait Set",
        "kind": "cosmetic",
        "scenario_id": None,
        "price": 2.99,
        "description": "A curated set of hand-selected character portraits for your heroes.",
        "image": "https://images.unsplash.com/photo-1615376206384-99dc417d64f1?crop=entropy&cs=srgb&fm=jpg&q=85&w=940",
    },
]

# Payment providers and the currency each checks out in.
PAYMENT_PROVIDERS = [
    {"id": "paypal", "label": "PayPal", "currency": "USD", "symbol": "$"},
    {"id": "paystack", "label": "Paystack", "currency": "NGN", "symbol": "₦", "rate": 1600},
    {"id": "razorpay", "label": "Razorpay", "currency": "INR", "symbol": "₹", "rate": 83},
]


# ---- Codex 3.3.2 import: researched HYW 1415 opening, entry catalogue and historical reference ----
import json as _json
from pathlib import Path as _Path

_HYW_DIR = _Path(__file__).parent / "data" / "hyw"
HYW_OPENING = _json.loads((_HYW_DIR / "hyw_1415_opening.json").read_text())
HYW_CATALOGUE = _json.loads((_HYW_DIR / "hyw_entry_catalogue.json").read_text())
HYW_BASELINE = _json.loads((_HYW_DIR / "hyw_historical_baseline.json").read_text())


def _apply_hyw_332():
    s = next(x for x in SCENARIOS if x["id"] == "hyw-1415")
    s["briefing"] = HYW_OPENING["briefing"]
    s["actors"] = [{"id": a["id"], "name": a["name"], "role": a["role"]} for a in HYW_OPENING["actors"]]
    s["world_facts"] = [{"id": f["id"], "domain": dom, "statement": f["statement"], "source_ids": f.get("source_ids", [])}
                        for dom, facts in HYW_OPENING["domains"].items() for f in facts]
    s["unknowns"] = HYW_OPENING["unknowns"]
    s["sources"] = [{k: src.get(k) for k in ("id", "title", "url", "source_type")} for src in HYW_OPENING["sources"]]
    s["simulation_rules"] = HYW_OPENING["simulation_rules"]
    s["entry_catalogue"] = "hyw"


_apply_hyw_332()


# ---- IRGS 3.4.1 import: Content Library v0.5 (44 concept records from IRGS-Catalog) ----
CATALOGUE_V05 = _json.loads((_Path(__file__).parent / "data" / "catalogue_v0_5.json").read_text())
CATALOGUE_TO_SCENARIO = {"MC-01": "hyw-1415"}


def catalogue_theme(genres: list, setting: str) -> str:
    g = " ".join(genres + [setting]).lower()
    for key, theme in (("science fiction", "pda"), ("fantasy", "grimoire"), ("roman", "tablet"), ("sengoku", "shinobi"),
                       ("japan", "shinobi"), ("settlement", "settlement"), ("military", "military")):
        if key in g:
            return theme
    return "ledger"


for _s in SCENARIOS:
    _rec = next((r for r in CATALOGUE_V05["records"] if CATALOGUE_TO_SCENARIO.get(r["catalogue_id"]) == _s["id"]), None)
    if _rec:
        _s["catalogue"] = {"id": _rec["catalogue_id"], "tier": _rec["tier"], "title": _rec["title"], "tagline": _rec.get("tagline")}
