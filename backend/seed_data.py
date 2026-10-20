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
]

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
        "id": "pack-voice-bard",
        "title": "The Bard's Voice Pack",
        "kind": "voice",
        "scenario_id": None,
        "price": 4.99,
        "description": "Expressive ElevenLabs narrator voices tuned for dramatic story readings.",
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
