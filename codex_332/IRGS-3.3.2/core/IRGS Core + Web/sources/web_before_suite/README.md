# IRGS local website

IRGS (Interactive Roleplaying Games Systems) is the top-level system. AST is the beta game used to test IRGS Core + engines, and is the first connected playable game in this host. AST is not the identity of the IRGS platform.

## Start

Double-click `Start-IRGS.cmd`, keep its terminal open, and visit http://127.0.0.1:8765. Stop the host with Ctrl+C. Alternatively run `python server.py` with Python 3.12 or newer (no third-party packages). Do not use Python's `-O` flag: the existing engine relies on assertions for validation.

Create a named campaign, declare player actions, inspect characters, or open the Game host tools below the campaign room to record scenes, evidence, inventory, obligations, designs, and received orders. All these events execute through the existing ASTWorld runtime. Player declarations are recorded as `declared_not_resolved`; this is a game-host interface, not an AI narrator or automatic outcome resolver.

Campaigns automatically resume from `saves/*.json`. Every accepted event is atomically saved. Branch campaign creates an independent copy at the current persisted state. Export save downloads a raw AST world JSON compatible with `ASTWorld.load`. Keep copies of the saves directory for backups. There is no import UI yet.

The host uses the adjacent `IRGS_Core_Unification_CMRR_R9/runtime` and `data` directories and leaves their files unchanged. Keep those folders beside `IRGS_Web` when moving the project. The AST profile reports Core 3.3; the inherited R9 README still describes R8 and says Core 3.2 is globally selected. This website makes no global adoption change.

The engine library distinguishes connected AST gameplay from the other source engines that have not yet been wired to this website. The synthetic strategy simulator is not connected to the player interface.

## Local hosting and verification

The server binds only to 127.0.0.1, checks Host/Origin, requires a per-process token for writes, and uses revision checks to reject stale event submissions from other tabs. It is intended for one local user. Public hosting, accounts, multiplayer, and remote access are future work.

Run `python -m unittest discover -s tests -v` from this directory to verify actual HTTP campaign creation, event validation, persistence, branching, stale-write rejection, and write protections.
