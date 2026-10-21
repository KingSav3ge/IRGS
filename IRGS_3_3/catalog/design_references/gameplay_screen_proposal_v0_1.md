# IRGS — Gameplay Screen Design Specification

Interactive Roleplay Game Systems · Website UX/UI Design · Proposed v0.1

Design objective: Create a professional, browser-based roleplaying interface that combines interactive storytelling, persistent world simulation, character development, and grand-strategy capabilities without overwhelming the player.

The Gameplay Screen will be the central interface of IRGS. It must accommodate everything from a private conversation between two characters to the administration of a civilization spanning centuries.

The governing principle is:

One simulated world. Multiple ways to interact with it.

The website must never maintain an independent version of the game mechanics. It displays, controls, and queries the authoritative IRGS simulation.

## 1. Overall gameplay screen design

I recommend three primary interface views, accessible without leaving the campaign.

The Hundred Years' War

1415 · Last Push of the English · A Scot's Tale

StoryWorldChronicle

SCENE · RECRUITMENT YARD

Steel rings across the training yard. Beyond the gathering soldiers, a knight watches the proceedings.

SIR RICHARD WYCLIFFE

"And what brings you into our company?"

Describe what your character says or does...

Interactive conceptual preview. The tabs illustrate different views of one playthrough; no simulation is connected.

These three views share the same world clock, campaign state, player character, and permission system.

| View      | Main purpose                                                          | Advances simulation time?                                      |
| --------- | --------------------------------------------------------------------- | -------------------------------------------------------------- |
| Story     | Character actions, conversations, exploration, and immediate events   | Only when actions or authorized time advancement are processed |
| World     | Maps, institutions, territory, resources, projects, and management    | Inspection does not; submitted orders may                      |
| Chronicle | Personal history, world history, biographies, and historical research | No, unless the player initiates a separate action              |

A player can switch between them whenever appropriate. Changing views must not itself trigger a turn, simulate an action, or alter world state.

## 2. Desktop layout

The proposed desktop interface has three principal columns and one persistent header.

```
┌────────────────────────────────────────────────────────────────────────┐
│ IRGS  | Campaign / Scenario | World Time | Save | Settings | Profile  │
├───────────────┬───────────────────────────────────────┬────────────────┤
│ NAVIGATION    │ STORY | WORLD | CHRONICLE             │ CONTEXT PANEL  │
│               ├───────────────────────────────────────┤                │
│ Story         │                                       │ Character      │
│ Character     │ SCENE TITLE / LOCATION                │ Condition      │
│ Inventory     │                                       │ Equipment      │
│ Relationships │ Narrative text                        │                │
│ Journal       │                                       │ Relevant NPCs  │
│ Map           │ NPC dialogue                          │                │
│ Projects      │                                       │ Current Tasks  │
│ Factions      │ Event and action outcomes             │                │
│ Chronicle     │                                       │ Known Facts    │
│               │                                       │                │
│               ├───────────────────────────────────────┤                │
│               │ ACTION INPUT                          │                │
│               │ [Describe your action...     ] [Send] │                │
├───────────────┴───────────────────────────────────────┴────────────────┤
│ System status / Notifications / Simulation feedback                    │
└────────────────────────────────────────────────────────────────────────┘
```

Structural wireframe, not a pixel-accurate mockup.

### Desktop regions

| Region              | Proposed behaviour                                                              |
| ------------------- | ------------------------------------------------------------------------------- |
| Top header          | Persistent campaign identity, navigation, in-world time, connection/save status |
| Left navigation     | Access to available character and world-information panels                      |
| Central workspace   | Primary gameplay content, including the narrative feed                          |
| Right context panel | Relevant character, scene, encounter, or management information                 |
| Bottom composer     | Player declarations, actions, dialogue, and contextual controls                 |

The centre should always receive the most screen space.

Suggested responsive dimensions, subject to usability testing:

- Large desktop, 1440px and wider: Three columns; navigation approximately 220–250px, context panel approximately 280–340px, remaining space allocated to the centre.
- Tablet and smaller desktop, 768–1439px: Collapsed navigation with contextual information in a drawer.
- Mobile, under 768px: One primary content column, with panels opened through tabs, sheets, or drawers.

The narrative text should occupy a readable central width rather than stretching across an entire large monitor.

## 3. Visual identity and readability

The universal IRGS interface should use restrained dark colours and a professional presentation inspired by interactive fiction, game launchers, and simulation dashboards.

Proposed IRGS colour system

Base

Panel

Accent

Text

Status

For readability, the Story View should support adjustable text size, line spacing, narration width, and a serif/sans-serif reading preference. A light or parchment-inspired reading theme should be available independently of the global dark interface.

Different campaigns can change their artwork, decorative accents, and atmosphere, but the location of core controls and the meaning of status indicators should remain consistent.

The player should never need to relearn the interface when moving from a medieval campaign to a science-fiction one.

## 4. Story View — detailed functionality

The Story View is the default interface. It should present events like a living interactive novel, rather than a series of conventional chatbot messages.

### 4.1 Narrative presentation

The main narrative feed should support multiple types of content.

| Content type            | Presentation                                                                      |
| ----------------------- | --------------------------------------------------------------------------------- |
| Environmental narration | Full-width prose, divided into readable paragraphs                                |
| NPC dialogue            | Speaker identification and dialogue; optional portrait                            |
| Player declarations     | Distinct, compact entries showing what the player actually submitted              |
| Action outcomes         | Narrative explanation of what occurred                                            |
| Mechanical feedback     | Expandable details about consequential resolution                                 |
| State notifications     | Small updates for changes the character can perceive                              |
| Incoming information    | Letters, reports, messages, rumours, and observations with appropriate provenance |
| Scene transitions       | Location or time headings that clearly establish the new context                  |

Not all of these should look like chat bubbles. Environmental narration should read like prose, NPC dialogue like conversation, and simulation feedback like an unobtrusive game-system notification.

### 4.2 Scene header

At the top of the active scene, a compact header would display information such as:

The Recruitment Yard

England · 1415

Characters nearby

Scene information

Only information observable or known to the character should appear. Hidden observers, undiscovered threats, and secret NPC intentions must not be included.

The header could remain visible while scrolling, but it should collapse to a smaller form so that it doesn't occupy excessive reading space.

### 4.3 Narrative history

The system needs a distinction between the recent narrative feed and the authoritative historical archive.

Recent scenes can retain their full text for readability and continuity. Older sessions should be loaded on demand, while the campaign's historical consolidation system handles the long-term narrative record.

A player revisiting an earlier scene should retrieve its original available narrative or an archived account. The AI must not invent a reconstructed conversation and present it as an exact transcript.

The feed should support bookmarks, search, jump-to-latest, scene boundaries, and unread-event indicators when returning from another screen.

## 5. Player action composer

This is probably the single most important interactive component of the website.

IRGS uses natural language as its principal gameplay input. That means the action composer must accommodate short commands, complex requests, spoken dialogue, and delegated orders without arbitrarily constraining the player.

Proposed action composer

&#x20;Copy example action

Input behaviour demonstration only. It copies the entered example rather than submitting it to a campaign.

### Composer requirements

Freeform text remains the default. Players can declare an attempt, address another character, describe a complex sequence, or issue an instruction to an authorized subordinate.

Optional contextual assistance can be shown below the input. It might suggest talking to a visible NPC, inspecting nearby equipment, opening the map, or continuing a paused project. These are aids, not restrictions.

For input semantics, I recommend that Enter inserts a new line and Ctrl/Cmd+Enter submits an action, with a user preference for alternative keyboard behaviour.

During action processing, IRGS should prevent accidental duplicate submissions. The player may inspect information or edit an unsent draft, but a new state-changing declaration should not be silently added to an unresolved action.

### Important distinction: speech versus intent

If a player types:

> "I ask Sir Richard whether I can inspect the available weapons."

The simulator should process the declared request. It should not invent a longer speech, an additional promise, or a subsequent action supposedly chosen by the player.

By contrast, NPCs may speak or react autonomously according to their own state and the ongoing simulation.

### Suggested actions

I would make optional suggested actions collapsible and subordinate to the text box.

For example, a dialogue scene might display Ask a question, Inspect surroundings, or End conversation.

Such suggestions are interface shortcuts. They must never become the only permissible actions, and selecting one should either populate a draft or explicitly submit the action the player has selected.

Potentially irreversible choices—such as declaring war, accepting an oath, transferring valuable property, or authorizing a large expenditure—should have a clear confirmation or review mechanism when appropriate.

## 6. Action processing and simulation feedback

The frontend must respect IRGS's established resolution sequence:

Declaration → Feasibility → Execution/Uncertainty → Effect → Exposure/Reaction → State Update → Player Control

For the player, that should appear as one coherent interaction rather than seven separate interruptions.

1\. Action submitted

The player's exact declaration is preserved.

2\. IRGS resolves the action

Checks capability, available resources, time, uncertainty, physical effects, and autonomous reactions.

3\. World state is committed

Changes to the authoritative simulation are recorded once.

4\. The result is presented

Narration, visible consequences, clock changes, and relevant notifications appear.

5\. Player control returns

The interface awaits the next meaningful player decision.

### Resolution display

I recommend two levels of feedback:

Narrative feedback, visible by default, describes what happened in context.

Mechanical feedback, accessible through an expandable section, identifies the action result, any consequential uncertainty, known resource expenditure, elapsed time, and relevant mechanical reasons.

Routine actions should not generate unnecessary dice animations or lengthy calculation displays. Qualified routine work normally succeeds while consuming the appropriate time and resources.

Where uncertainty genuinely requires a roll, the UI can expose the relevant dice and outcome without allowing the player-facing animation to determine the result.

The engine resolves the outcome; the interface presents it.

### Unsuccessful actions

The display should distinguish between:

| Outcome                | Required treatment                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------ |
| Infeasible             | Explain the known constraint without rolling to make impossibility possible          |
| Uncertain failure      | Present the resolved failure and its causally appropriate consequences               |
| Mixed outcome          | Present the achieved and failed portions without inventing new voluntary expenditure |
| Interrupted            | Identify what actually occurred before interruption and what remains incomplete      |
| Requires clarification | Preserve the declaration and request only information necessary for resolution       |

If the player lacks a suitable tool, a failure result must not be treated as though they used one.

If a project is only partly completed, the UI must not describe it as finished.

### Automatic saving

Every committed state-changing action should become a durable persistence checkpoint. The visible save indicator must distinguish between a local input draft, an acknowledged action, and server-confirmed persisted state.

An interrupted connection should never produce two copies of the same action, expense, or historical event.

## 7. Contextual right-hand panel

Rather than displaying every system at once, the right panel should respond to the active situation.

Scene Context

Character

View current condition

Nearby Characters

Known or visibly present people

Equipment

Carried and accessible items

Active Obligations

Known commitments and assigned tasks

Illustrative right-panel structure.

The panel's content should change based on the scene.

| Situation                | Relevant contextual information                                                         |
| ------------------------ | --------------------------------------------------------------------------------------- |
| Conversation             | NPC identity, established relationship, known affiliations, relevant prior interactions |
| Combat                   | Current participants, condition, equipment, positioning, accessible actions             |
| Travel                   | Known route, supplies, companions, weather observations, destination                    |
| Workshop                 | Available tools, materials, active research, projects                                   |
| Military command         | Orders, units, reports, logistics, command authority                                    |
| Business management      | Assets, workforce, obligations, operations, financial information                       |
| Political administration | Offices, institutions, proposals, agreements, known political circumstances             |

The simulation, not the frontend, determines what information and authority the player possesses.

A military commander could legitimately inspect several subordinate units. A civilian witnessing the same army might only see troops in the distance.

Those different interfaces must be derived from the same underlying world state.

## 8. Character Sheet and Inventory

A character sheet should be a permanent part of the interface, accessible from Story or World View without leaving the playthrough.

It should not resemble a traditional RPG sheet unless the selected engine and campaign actually require those mechanics.

### Character sheet structure

[Oh noes!](https://images.openai.com/static-rsc-4/WFz31OYHK8HEgY9g-bnhyWcbFZMTD_Yt9_bPfefdJWY2V29IfkevA2gwdIHwd-yyxhN8LdkZoo50c7zxfb6WYzpB_riY1MBl44_jJZZOBIJ3M8heA-gkW2kcu10ygf4pWliKHwiTYXxCmNL9yVEAHK9BFeGJ-Z0IzMxYQBur76I?purpose=inline)

### Ian Tormod Cameron

Illustrative AST character panel

Personal Identity

Background · Affiliations · Current condition · Status

Capabilities

Condition

Equipment

Relationships

Finances & Property

Career & Standing

Each field must retain its actual rule-defined meaning. Social authority is not a substitute for expertise; an owned possession is not the same as an available possession; injury is not interchangeable with fatigue or exposure.

The inventory needs to distinguish ownership, custody, carried location, storage, accessibility, condition, reservations, and consumption where relevant. Transfers and expenditure are committed by Core, not inferred from descriptions or frontend counters.

## 9. World View — simulation dashboards

The World View should scale according to the nature of the campaign and the player's current authority.

A player who is exploring a village might primarily use a local map. A ruler could access provincial government records, an economic overview, military command information, and administrative projects.

These are panels over shared IRGS Core records.

[The Hunters A. D. 1492 by Officina Monstrorum - News #7! - Gamefound](https://images.openai.com/static-rsc-4/94IUZCwYxWOzuEAb1O2OIHXdgNHpm4T23NDP8mNsAE9hk3o8xECoY2qpHPnztEo0nAEd_S550CYyJGHusIwk7lCL4bjWLIdWjS44IRFGXbwoRQPT6X65aO3YP-WSGowiewQnMtkqSFQq7Y9ZpazKe1gPcxUV7WZkR3bQzpEruiE?purpose=inline)

World Atlas

Locations, geography, travel routes, known territorial borders, settlements, infrastructure, and discovered points of interest.

[The Beautiful Boards of Wargaming! – Nevsky: Teutons and Rus in Collision, 1240-1242 from GMT Games – The Players' Aid](https://images.openai.com/static-rsc-4/NGztwq9hOB_o8_KpYALnnqYGgGewAsz_LJe8D5RXj-0bARNI4-RMvhLFvVsBM3GeNZXbu200IPIMwZ2xwJHywTGr5QLtN8EVZ2eEvr_M_E5FY1WEvyW5Bq8qRgi6Sj8Nk-fyEfr9BKis2sHosKc4NkG6bwD0pD4iJ4kYxaPrKL8?purpose=inline)

Institutional Management

Military units, businesses, government offices, settlements, estates, and other organizations relevant to the player's responsibilities.

[Images of Sparks flying from the forge, a blacksmith carefully examining a horse's hoof, glowing red-hot iron in the fire, hammer... | Deep Dream Generator](https://images.openai.com/static-rsc-4/Ou53afpFMcxzrDLPoIcxXV3HXdTl-KhLIKfi541co2Y_hS_MfryCl44k2WK44DZ9A-SfcJ7GZutBR-e6AVPGxmqY6RQHWg0TTcBTOrs58jy-EC7gkC4VGEzBW9c6FwrSujsTniIaeLqgGd8E0d46Xr1kNrdB9_Skude0eFun4_s?purpose=inline)

Projects and Research

Construction, experimentation, technological development, manufacturing, training, and other extended activities.

The map itself should support layers, zooming, navigation, inspection, and access to known reports.

However, moving a map viewport must not move the player character, consume time, reveal undiscovered information, or issue an order.

A player could click a location to inspect it, then explicitly request travel to it. Those are separate operations.

### An important UI distinction

Inspection controls do not change the simulated world. Action controls can.

Selecting a military unit to view its condition is inspection. Ordering that unit to march is a state-changing action, and must go through Core resolution.

This distinction should be reflected consistently throughout the interface.

## 10. Time advancement and long-term play

Because IRGS campaigns may run indefinitely, the Gameplay Screen must accommodate radically different timescales.

A player may spend several real hours roleplaying a ten-minute conversation, then advance three months while their character conducts routine work.

### Proposed time controls

### Time Advancement

Illustrative control design. Durations are requests, not guaranteed outcomes.

Advance an hour

Advance a day

Advance a week

Advance a month

Advance a year

Continue until the next required decision

Requested advancement

One in-world day

IRGS must stop or interrupt advancement whenever continued execution would require a new player choice.

The player may specify activities that should continue during this period, including research, employment, travel, education, maintenance, or delegated projects.

The engine must then process actual time, activity, resource expenditure, NPC actions, and consequences.

The interface should show a progress report after the requested interval or interruption, rather than simply narrating that time has passed.

### Scale-change safeguards

No change in timescale may reset fatigue, injuries, project progress, ammunition, finances, casualties, or other persistent facts.

A time-advancement operation must stop before an unresolved consequential decision requiring player agency. Autonomous actors may continue acting within their authority and available resources.

For long-running simulations, the interface should support concise period reports with expandable details, rather than flooding the narrative feed with thousands of routine updates.

## 11. Chronicle View — generational history

The Chronicle should be one of the distinguishing features of IRGS.

Its purpose is not merely to store previous conversations. It should provide a usable historical interface for campaigns lasting decades, centuries, or longer.

### Chronicle navigation

| Area                  | Function                                                                           |
| --------------------- | ---------------------------------------------------------------------------------- |
| Personal Chronicle    | The current character's life, experiences, and known milestones                    |
| Biographies           | Known NPCs, relatives, historical figures, and previous player characters          |
| Relationships         | Family trees, alliances, marriages, patronage, and social connections              |
| Institutional History | Organizations, governments, businesses, military formations, and their development |
| Historical Timeline   | Chronological world events available to the player                                 |
| Historical Archive    | Annual and consolidated historical records                                         |
| Search                | Retrieve accessible events, characters, discoveries, and historical details        |

### Historical memory integration

The user-established system should be reflected in a timeline with these levels:

Historical records

5 annual records      → 1 five-year summary 5 five-year summaries → 1 twenty-five-year summary 4 twenty-five-year    → 1 hundred-year summary  100 → 200 → 300 → 400 cumulative years  500 completed years   → 1 sealed epoch Next 500-year interval → new consolidation cycle

Century summaries must receive expanding word budgets, and completed 500-year epochs remain distinct.

The Chronicle UI should expose this organization, while historical summaries, authoritative world state, and event archives remain separate backend structures.

A player searching for an old discovery should be able to retrieve its accessible historical context without requiring every previous narrative event to be loaded into the AI's active context.

It is also essential to distinguish what happened, what was observed, what was reported, and when that information became available to the character.

A secret event that occurred decades earlier must not become automatically visible merely because it entered a historical summary.

## 12. Mobile gameplay interface

IRGS needs a genuine mobile design rather than a compressed desktop layout.

The mobile interface should emphasize uninterrupted reading, quick information access, and easy natural-language input.

```
┌────────────────────────────┐
│ ←  Campaign         ⋮      │
│    In-world date           │
├────────────────────────────┤
│ Story | World | Chronicle  │
├────────────────────────────┤
│                            │
│ Scene Location             │
│                            │
│ Narrative                  │
│                            │
│ Character Dialogue         │
│                            │
│ Consequences               │
│                            │
│                            │
├────────────────────────────┤
│ Describe your action...    │
│                       Send │
├────────────────────────────┤
│ Character   Map   Journal  │
└────────────────────────────┘
```

The left navigation becomes a compact menu, while contextual information opens in a dismissible drawer or bottom sheet.

The action composer remains accessible near the bottom of the screen, adapting when the software keyboard appears.

On a phone, character and world-management panels should be able to expand into full-screen views when their information is too complex for a small drawer.

The Story View should preserve the player's reading position when they temporarily inspect their equipment or another panel. Returning to the active narrative must not automatically jump away from something the user was reading.

## 13. Information boundaries and player agency

These are architectural requirements, not optional UI preferences.

The interface must distinguish between what the simulation knows and what the player is entitled to see.

| Information                 | Player interface                          | Creator/debugger                    |
| --------------------------- | ----------------------------------------- | ----------------------------------- |
| Player-character condition  | Available as appropriate                  | Available                           |
| Known NPC identity          | Available                                 | Available                           |
| Hidden NPC intentions       | Restricted                                | Available with developer permission |
| Secret military orders      | Restricted until legitimately learned     | Available with developer permission |
| Rumours and reports         | Displayed with uncertainty and provenance | Full record accessible              |
| Actual world resource state | Only authorized or observed information   | Authoritative records               |
| Simulation trace            | Relevant mechanical explanation           | Full diagnostic trace               |

The frontend must receive a permission-filtered projection, not the entire secret world state with hidden fields merely concealed through CSS.

Player agency also remains binding across the entire UI. The interface must not choose dialogue, make voluntary movement, order purchases, spend resources, or select successors on the player's behalf.

Likewise, suggested responses must remain suggestions.

## 14. Backend integration requirements

The website's responsibility is to present the current simulation, submit declarations, receive authoritative results, and provide inspection tools.

A proposed interface contract would include:

| Interface            | Function                                                            |
| -------------------- | ------------------------------------------------------------------- |
| `GetPlaythroughView` | Retrieve the permission-filtered current scene and interface state  |
| `SubmitDeclaration`  | Send a player action for Core resolution                            |
| `GetCharacterView`   | Retrieve the character's accessible records                         |
| `GetWorldView`       | Retrieve accessible locations, organizations, and world information |
| `GetChronicle`       | Retrieve historical records and indexed history                     |
| `RequestTimeAdvance` | Submit an explicit timescale or waiting instruction                 |
| `CreateBranch`       | Create a separate playthrough branch from an eligible checkpoint    |
| `GetActionResult`    | Retrieve the outcome of an already submitted request                |

These names are proposed API interfaces, not claims about existing IRGS Core 3.3 endpoints.

Each state-changing request should carry an idempotent request identifier and the state version against which the player submitted it.

The response should identify whether the action was accepted, rejected as infeasible, resolved, interrupted, or requires clarification, together with the new committed state version where appropriate.

The frontend should never fabricate an inventory reduction, an NPC reaction, a world-clock change, or any other canonical result.

### Events and rendering

The backend should provide presentation-ready, permission-filtered observations containing enough information to explain what the player can legitimately know.

The AI narrative layer may transform a resolved simulation outcome into prose, but must not alter the outcome or append unsupported consequences.

Where possible, the underlying event system should preserve occurrence, observation, transmission, and receipt timestamps separately.

### Reliability states

The screen must account for loading, resolving, connection loss, duplicate submission, save failure, server conflict, and an unavailable narrator.

For example, if the simulation commits an action but the narrative response is interrupted, the website should recover the committed result by request identifier. It must not resubmit the same action as if it never happened.

## 15. Accessibility and player preferences

A text-centred simulation can be unusually accessible if designed properly.

The minimum product requirements should include keyboard navigation, semantic controls, visible focus indicators, screen-reader-compatible dialogue and notifications, adjustable typography, adequate contrast, reduced-motion settings, and usable mobile touch targets.

Additional preferences could include a compact interface, distraction-free reading mode, optional character portraits, narration density, mechanical feedback verbosity, and campaign-specific visual themes.

These must not alter game mechanics.

The accessibility goal should be WCAG 2.2 AA, with testing against actual assistive technologies rather than relying exclusively on automated checks.

## 16. Proposed development priority

| Priority                    | Components                                                                                                                                      |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| P0 — Essential              | Gameplay shell, narrative feed, freeform input, authoritative action handling, save/load, basic character panel, permissions, responsive layout |
| P1 — Core experience        | World View, Chronicle, inventory, relationships, time controls, contextual panels, state feedback, campaign branches                            |
| P2 — Expanded simulation UI | Research interfaces, institutional management, rich mapping, family trees, long-range chronology, creator inspection tools                      |
| P3 — Advanced platform      | Multiplayer interfaces, collaborative management, voice interaction, expanded visuals, external integrations                                    |

This priority order does not mean the backend can ignore long-term continuity until P2. World-state persistence and the historical record architecture need to be designed correctly from the outset, even where advanced visualization arrives later.

## 17. Acceptance and regression testing

The Gameplay Screen should not be considered implementation-ready until the following cases can be demonstrated.

| Test                                | Required result                                                                    |
| ----------------------------------- | ---------------------------------------------------------------------------------- |
| Player opens inventory              | No in-world time passes                                                            |
| Player switches Story to World      | Same simulation state persists                                                     |
| Player submits an impossible action | Engine rejects infeasibility without manufacturing success through dice            |
| Routine qualified action            | Appropriate time and resources are consumed without an unnecessary roll            |
| Player submits an ambiguous order   | The interface requests clarification without inventing intent                      |
| Mixed action outcome                | Only authorized resources and actions are applied                                  |
| NPC acts independently              | Player receives information only when appropriately observable or reported         |
| Military command panel              | Orders require legitimate authority and operational resources                      |
| Player advances one year            | All intermediate costs, consequences, and autonomous activity remain accounted for |
| Character dies                      | No automatic successor selection                                                   |
| Save is reloaded                    | Clock, resources, conditions, relationships, and progress are unchanged            |
| Duplicate request is retried        | No duplicate action, payment, casualty, or event                                   |
| Historical summary is generated     | Authoritative state is not modified                                                |
| Old secret is archived              | It remains hidden until legitimately discovered                                    |
| Two simultaneous events occur       | Core uses a consistent pre-event state and prevents double-counting                |
| Player opens two sessions           | State-version conflicts are handled without silent overwrites                      |

These are scripted acceptance cases, not evidence of calibration or live playtesting.

## 18. Recommended screen component architecture

For Codex implementation, I would separate the frontend into these components:

```
GameplayShell
├── CampaignHeader
├── PrimaryViewSwitcher
│   ├── StoryView
│   │   ├── SceneHeader
│   │   ├── NarrativeFeed
│   │   ├── DialogueRenderer
│   │   ├── OutcomeRenderer
│   │   ├── MechanicalDetail
│   │   └── ActionComposer
│   ├── WorldView
│   │   ├── WorldAtlas
│   │   ├── LocationInspector
│   │   ├── OrganizationPanels
│   │   └── ProjectDashboard
│   └── ChronicleView
│       ├── Timeline
│       ├── BiographyBrowser
│       ├── HistoricalArchive
│       └── HistoricalSearch
├── NavigationPanel
├── ContextPanel
│   ├── CharacterSummary
│   ├── InventorySummary
│   ├── RelationshipSummary
│   └── SituationSummary
├── TimeAdvanceControls
├── SaveStatus
├── Notifications
└── ResponsiveDrawerSystem
```

These should be presentation and interaction components. Domain logic belongs to IRGS Core or its valid extensions.

### Version and ownership

Established requirements: Simulation authority, player agency, persistent state, ahistorical freedom, campaign hierarchy, time continuity, and the historical memory consolidation model.

Proposed website design: The three-view layout, component structure, styling, contextual panels, navigation, responsive breakpoints, and the precise frontend contracts above.

Unresolved implementation decisions: Existing Core 3.3 API compatibility, backend infrastructure, narrator transport, exact UI permissions, save branching constraints, and the final visual design system. The current Core archive has not been directly audited for this screen specification, so those interfaces require reconciliation before implementation.

There should be no automatic migration of existing campaigns simply because the website adopts a revised layout.

## Overall recommendation

IRGS should open into a Story-first gameplay screen that is comfortable for someone who only wants to roleplay a single character.

As the character gains knowledge, property, relationships, institutional responsibilities, or political authority, the same website should reveal increasingly capable tools for interacting with the larger world.

Someone beginning A Scot's Tale as a young Highlander would primarily use dialogue, exploration, character information, and a journal.

That same character could eventually command soldiers, administer estates, develop businesses, or participate in political affairs. The interface would expand to accommodate those responsibilities without moving the player into a different game.

And if the campaign continues for another 500 years, the player's successors should still be using the same underlying simulation and historical continuity architecture.

The central design goal is progressive interface complexity over a persistent, causally consistent world—not separate interfaces that pretend to be separate games.

This constitutes a proposed Gameplay Screen v0.1 design suitable for review and CMRR reconciliation before Codex treats it as an implementation specification.