# Playable Solo opening — Opening1

**A dispatch before departure** is an optional playable opening for a newly created human character at the developed 1415 entry. The player selects and reviews it before the first save. Its quay, clerk's tray, dispatch, route conditions and durations are authored fiction within the historical setting. The historical snapshot is unchanged. No existing campaign or historical figure receives these circumstances automatically.

## Actual play

The character begins at the quay with custody of one sealed dispatch and received directions. Listed actions support local observation, walking through a covered passage, trying a potentially blocked shortcut, delivering the actual dispatch and returning. A blocked route records an unsuccessful attempt with elapsed cost. A fresh empty-handed delivery also fails without moving stock. Choices are drawn from the received local map without consulting hidden blockers or carried quantities to predict success.

Durations are explicitly selected local gameplay rules: observation 20 seconds, passage walking 45 seconds per leg, shortcut attempt 30 seconds and delivery 10 seconds. They are not historical measurements or universal defaults. Each bounded action commits its entire duration atomically. Interruptible travel, scheduled phases, civil-date advance, historical hour and automatic expedition departure are not implemented.

`scene_actions.py` operates on the same Core actors, current location, evidence/receipts and conserved stocks. Scene rules are selected configuration; they own no parallel actor or resource state. Movement records and delivers the immediate arrival description. Observation is a new physical look with a cost; reading an existing record or retrieving its receipt performs no new observation. The dispatch moves from actual character custody to the tray and grants no pay, appointment or institution-wide authority.

Execution rechecks current control, existence, received map, established location, selected route, actual condition, actual stock and explicit elapsed axis. Existing legacy activity spans have no binding to scene seconds; an existing commitment involving this actor refuses scene execution rather than being silently bypassed. The profile is bounded local play, not a general geography, hidden-search, combat or arbitrary-command resolver.

## Durable result and presentation

R9 observes actual handler execution and checks agreement with ordinary execution. Private certificates retain control, location, map, condition, stock, timing and decision reads. Named coverage is separate from all-branch or all-engine certification.

The existing `/api/action` path validates a kind-specific identifier and exact listed text. It saves the request, committed world, outcome, private dependencies and public receipt together before acknowledgement. Successful and unsuccessful completed attempts have durable receipts. An identical retry retrieves the original result before stale-revision and current-world validation, repeating no elapsed work, information, movement or transfer. A new identity is a genuinely new attempt. Invalid requests and failed persistence leave the saved world unchanged.

The website displays the actual location, legitimate observations, scene elapsed total, saved outcomes and next actions. Separate written drafts remain editable. Freeform declarations remain unresolved intent; dialogue, combat, general narration and autonomous advancement remain unavailable. Continuing play uses saved rules and actual committed state, never a reloaded historical or scene template.

## Evidence and remaining scope

- `runtime/test_scene_actions.py`: control/knowledge boundaries, real dependencies, blocked/depleted outcomes, replay, rollback and existing commitments.
- `runtime/test_scene_setup.py`: real pack execution, explicit selection, changed-review rejection and continuing-world isolation.
- `IRGS_Web/tests/test_scene_play.py`: real loopback creation, repeated play, conserved delivery, failed completion, reload/restart/retry, concurrent duplicate, stale/altered requests and failed persistence.
- `IRGS_Web/tests/test_gameplay_ui.js`: exact scene submission, setup review, failed outcome and retained custom drafts.

Actual run counts and distribution checks are recorded in `OPENING1_VALIDATION.json`. DEV-10, DEV-12–DEV-14, DEV-18 and DEV-25 advance within this scope and remain open for their broader requirements. Phase interruption/recovery, restore fencing, wider geography, hidden searches, NPC agency and sustained institutions remain unfinished. The immutable C2 inventory is unchanged.
