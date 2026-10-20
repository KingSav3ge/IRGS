# Codex 3.3.2 merge notes (20 Oct 2026 upload)

## What Codex 3.3.2 contained
- A local Python suite (`IRGS_3_3/IRGS_Web` with server.py and a static app.js/index.html/style.css) on port 8765, plus the Core 3.3 runtime (temporal registry, strategic execution, economic extension, R5–R9 certification fixtures).
- The Codex UI it was building: a dark teal/green palette (--base #111a1a, accent #d6ba81) with a cream "reading" page (#f3eedf). Its screens:
  - Story / World / Chronicle tabs
  - "Choose an entry point" → scenario → character ("Identity & origin", "Life path", "Starting career intent") → review → "Start campaign"
  - "Submit declaration" / "Withdraw pending attempt"
  - Branch, Export view, Campaign Trash (recoverable delete), Reading settings, Creator workspace
- Data: the HYW entry catalogue (37 dates, 10 featured years, 3 periods), the researched 1415 opening (revision 2, with sources and unknowns) and the historical baseline (3 documented 1415 reference events, read-only).
- Its README states that general narration and automatic calendar advancement were NOT implemented in 3.3.2.

## Brought in (Codex was better or this build lacked it)
- The researched 1415 opening: briefing, the 5th actor (Louis of France), 11 sourced world facts across 4 domains, opening unknowns (fed to the narrator as "do not invent"), sources and simulation rules → backend/data/hyw/*.json and seed_data._apply_hyw_332.
- The entry catalogue: GET /api/campaigns/hyw-1415/entries. A Library dialog lists all 37 dates by period. Only 1415 is playable; the rest are labelled Proposed.
- Historical record comparison: GET /api/playthroughs/{pid}/history-reference, shown as a read-only panel in the Chronicle. It never executes events.
- Player testimony (origin/family/career): optional fields in character creation. They are passed to the narrator as the player's own account and grant nothing.
- Reading settings: text size and a cream "paper" reading mode on the Play feed.

## Kept from this build (superior to 3.3.2)
- AI narration, Jev, NPC autonomy, time passing, voice, images, store, accounts, the save/branch system, genre skins. Archive/restore covers Codex's Campaign Trash.
