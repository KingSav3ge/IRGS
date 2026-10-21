# IRGS — ChatGPT Play Continuity Adapter

**ID:** `IRGS-CHAT-CONTINUITY@1.0`  
**Date:** 17 October 2026  
**Status:** Complete receiving specification implementing the user's requested checkpoint and recap behavior. Recording cadence is an adjustable editorial default. Scripted reference checks are separate from live playtesting.  
**Purpose:** Preserve what happened, what was said, what changed and what remains open before long conversations make those details difficult or impossible to recover.  
**Scope:** ChatGPT presentation and recoverable records during play; scene, session, day and chapter continuity. This is reusable across genres.  
**Dependencies:** Core 3.2 maintenance R3, especially §§2–4, 11–13, 63, 80–82, 85–86, 90–91, 97–99, 111–112. Selected campaign rules retain their existing authority.  
**Ownership:** An adapter to Core §98 and the compact journal contract in §86. It owns the recording/export procedure, not another clock, inventory, population, injury system or game-resolution loop.  
**Migration:** Prospective presentation change. No old day, chapter or save is reconstructed or certified merely by enabling it.

## 1. Problem and required behavior

A final state cannot explain every event that produced it. A person can return to the same place with the same possessions after an important conversation. A checkpoint that records only place, health and equipment loses that conversation. A short recap made from an earlier short recap compounds the loss.

During play, capture the history while its source is available. Preserve both the sequence of events and a restartable current-state view. Generate later recaps from that history, with explicit coverage, rather than asking the model to reconstruct an entire day from unrecorded recollection.

Use four connected views of the existing records:

| Record | Purpose | Does not do |
|---|---|---|
| Turn continuity entry | Capture the resolved exchange, dialogue meaning, consequences and open choice immediately | Invent another event or process the exchange twice |
| Scene record | Preserve the ordered exchanges and distinctive details of one scene | Replace the underlying source with a vague plot summary |
| Checkpoint | Export state at a named frontier, its source coverage and unresolved work | Erase earlier history or reinitialize the world |
| Day/chapter chronicle | Assemble the covered scenes into a chronological factual account | Invent connective events or treat an incomplete interval as complete |

These are projections/exports of one event and evidence history. A record of a payment is not a second payment. A scene record may refer to the authoritative turn entries; it need not duplicate stock ledgers.

## 2. Authority, evidence and record identity

Current user corrections and established campaign rules govern. Distinguish resolved occurrence, proposed action, authorized but unexecuted instruction, observed sign, testimony, interpretation, unresolved question and source gap. Label generated provisional capability or background separately from observed play.

Reuse actual campaign, actor, scene and event IDs when available. If the deployment has none, initialize campaign-scoped editorial handles prospectively, such as `<campaign>/S003/T012`; the handles are local record labels, not invented platform message IDs. Record the initial label and its scope. Do not attach a new label to a second copy of the same person or event.

Preserve two kinds of order:

- Source/record order: when a message or correction was recorded.
- Causal order: when the represented action, observation, transmission or receipt occurred in the game.

Simultaneous events can have different source positions but share one pre-event state. A late report belongs at its actual receipt time and references the earlier occurrence. Sequence numbers do not prove a time duration. When the source supplies only “later that afternoon,” retain that uncertainty; do not manufacture a clock minute or exact calendar day.

If an exact source locator is available, retain it. Otherwise record a local turn handle and the needed text/evidence in the record itself. A locator or hash pointing to inaccessible text does not recover that text. Do not claim a message can be retrieved solely because a handle exists.

## 3. Default recording schedule

The schedule measures output activity, not game time. It causes no additional actions, reactions, costs, elapsed time or dice rolls.

| Trigger | Required output or update |
|---|---|
| Every GM reply that resolves or advances an in-world exchange | Add a concise visible continuity entry for that reply |
| Five GM gameplay replies since the last checkpoint | Emit a checkpoint, even if the scene continues |
| Actual scene transition or completion | Finish/update the scene record and emit a checkpoint before proceeding into the next scene |
| Critical continuity change | Emit a checkpoint in the same reply after recording the change |
| Explicit pause, session end or chat-transfer request | Checkpoint the actual frontier and open decision without advancing play |
| Actual in-world day closes, or user requests a day record | Compile the available day chronicle and its coverage |
| Chapter closes or user requests its record | Compile the chapter from source-backed scene/day records, retaining their coverage |
| User asks “checkpoint now” | Export the current supported records immediately; no further in-world action |

“Critical” includes consequential custody/resource transfers, appointment or changed authority, serious injury/death/capture, completed major work, a new continuing obligation, a decisive disclosure, a correction affecting continuation, and a choice whose exact state would be costly to reconstruct. Small changes still receive turn entries. Ordinary conversations still receive scene coverage.

Five replies is the initial editorial safety interval, not a calibrated memory guarantee. The profile may choose a shorter or longer interval. The counter increments once per GM gameplay reply, regardless of how many events it contains. OOC explanations, design discussion and recap-only replies do not increment it. All checkpoint triggers in one reply coalesce into one checkpoint listing every reason. Publishing a scene record and checkpoint in that reply does not create extra turns.

After a checkpoint, reset only the editorial reply counter. Keep the world clock, actions, conditions, commitments, stock and processed work untouched. Before a long authorized interval, scene transition or transfer would make the existing material hard to carry forward, checkpoint first even if five replies have not elapsed. Do not claim to detect a hidden platform context threshold.

## 4. Turn continuity entry

Write the scene normally. Show necessary uncertainty, actual effects and NPC reactions. After the narrative, add a separate, compact OOC record headed **Continuity**. Keep it factual and distinct from character speech. Then leave the next meaningful player decision open.

Each entry captures what the user declared and what the reply actually resolved. It should include:

1. Campaign/scene/turn handle and the best-supported game time/location.
2. Who was present or communicated, and the resolved action or exchange.
3. Dialogue meaning: questions, answers, refusals, promises, terms, information, corrections and unresolved points, attributed to the actual speaker.
4. Actual consequences and changes, referencing existing owners/instances; costs, transfers and rolls where material.
5. Continuing obligations, future appointments, held choices, unresolved uncertainty and the next player decision.

Usually one to three short bullets suffice. This is a readability target, not a hard truncation limit. If the reply contains more distinct events, preserve them and checkpoint early. Do not delete a unique interaction to fit a word cap.

Example layout, with placeholders rather than campaign facts:

```text
Continuity — <campaign / scene / turn> — <supported time and place>
- <Declared action and actual result; participants.>
- <Attributed dialogue, terms or information; material changes and pending work.>
- Open: <the actual unanswered question or next voluntary choice.>
```

Record routine kindness, introductions, disagreements, instruction, ordinary work and relationship interactions even if no numerical state changes. Record their actual content; do not invent an emotion, attitude meter or automatic relationship increase. A quiet conversation is not “nothing happened.” A repeated statement can be grouped only if its repetition and any changed response remain clear.

Do not restate the whole inventory every turn. Reference unchanged records and show the changes relevant to this exchange. A checkpoint has stricter portability requirements than this compact turn note.

## 5. Dialogue, exact wording and scene detail

Distinguish an exact quotation from a paraphrase. Preserve short exact wording when it controls an oath, service term, bargain, instruction, name, clue, insult, inscription, permission or later interpretation. Capture the speaker, addressee, status, source and reply. A suggestion is not acceptance; a quote for work is not a purchase; a conditional promise is not an unconditional commitment.

For other dialogue, preserve its specific meaning and response. “They discussed service” is insufficient if the exchange established who would approve the role, a condition of acceptance or an unresolved question. An offered action remains an offer until actually chosen and executed.

The scene record retains distinctive observations, gestures, atmosphere and motifs that matter to character continuity or later writing, together with the actual interactions. It does not infer a PC's private feelings from a smile, silence or prose style. NPC portrayal may record the words/actions actually established; concealed motives remain subject to the information boundary.

For full dialogue transcription or manuscript reconstruction, retain the actual source text in a supported archive. A factual scene record is not a word-for-word transcript. If the original wording is no longer available, quote only preserved exact excerpts and paraphrase the rest explicitly. Never create reconstructed dialogue and label it verbatim.

## 6. Scene record procedure

Open a scene record with its editorial ID, starting frontier, participants, location and supported purpose. Extend it as the turn entries arrive. At a scene break, or when a checkpoint is due mid-scene, consolidate all available entries since the prior consolidation.

Required scene contents:

- Scene identity, date/time bounds and whether it is open or complete.
- Ordered list of exchanges/actions, with covered turn/event handles and accessible source text or durable factual entries.
- Participants and changes in presence; distinguish a message from physical arrival.
- Specific dialogue, choices, commitments, information and distinctive details under §§4–5.
- Roll outcomes and material effects when used; unchanged uncertainties stay retained.
- Actual state changes and continuing conditions, linked to existing instances/owners.
- Open choices, unresolved terms, pending tasks and information not yet received.
- Coverage gaps, corrections and the evidence that supports the record.

Do not record only the last five replies at a scene break. Include the earlier segments of that same scene. A long scene can have several checkpoint segments under one scene ID. Scene closure does not erase its interior checkpoints or split one continuing conversation into multiple invented encounters.

Compression may remove duplicate phrasing, redundant panels and repeated unchanged state. Preserve every distinct resolved exchange, consequential observation, decision, relationship interaction, commitment and unresolved thread. The coverage map must still identify which source units a grouped entry represents. A scene synopsis used for quick reading is an additional view, not the only surviving record.

## 7. Checkpoint procedure and minimum content

A checkpoint is a named snapshot/export at the current committed frontier. It is not a rest, save-point heal, day advance or decision by the PC.

Record:

| Field | Requirement |
|---|---|
| Identity and profile | Campaign, checkpoint ID/revision, selected rules/adapter, visibility, source boundary and checkpoint reasons |
| Clock and frontier | Best-supported game time, place, causal frontier and last processed events/intervals |
| Current scene | Open/completed scene, actual participants, immediate situation and current unresolved player decision |
| Actor and asset state | Relevant persistent conditions, equipment configuration, ownership/custody, location, finite quantities and unresolved values |
| Work and commitments | Active tasks, reservations, labor conflicts, completed fractions, processed spans, retained rolls and pending obligations |
| Information | What the represented audience knows, relevant evidence status, messages in transit and unanswered questions |
| History coverage | Scene/turn/event ranges, accessible scene records and any missing ranges; source-detail level |
| Open threads | Promises, invitations, appointments, service terms, relationships, investigations and ordinary-life matters still active |
| Storage and recovery | Actual persisted files/version or “posted in chat only”; previous checkpoint reference and what can actually be recovered |

Include actual payloads or a verified accessible source for fields necessary to resume. A transfer-only checkpoint pointing to “the earlier sheet” is not standalone when that sheet is unavailable. Use a full portable snapshot at session/chat handoff, incorporating earlier deltas and accessible records rather than leaving an unresolved chain of “unchanged” fields.

“Full” is scoped: identify the represented actors, records and source frontier. Do not claim that a public player checkpoint includes the entire hidden world. Keep unknown distinct from zero, absent, unrestricted and not applicable. Existing actor sheets remain the authoritative detailed records when they are accessible; this snapshot references/exports them without creating duplicate people or competence.

A checkpoint's current state and its history are separate coverage dimensions. One may be available while the other has a gap. A surviving latest checkpoint may permit limited continuation but not a complete day recap. Conversely, a chronicle may preserve the day's conversations without all fields needed for exact mechanical restart. Label those limits rather than using one as proof of the other.

## 8. Day and chapter recaps

A request to recap freezes play under Core §82. It does not close an unfinished day, make the PC sleep, finish a pending conversation, travel, pay an outstanding bill or resolve an open choice.

Default a day/chapter recap to a chronological factual account of all available recorded scenes in the requested scope. If the user requests a brief recap, produce that additional condensed view and retain the underlying chronicle. Do not replace the full record with the brief version.

Procedure:

1. Establish the requested boundaries without inventing dates or equating real-world chat dates with game dates. If the chapter boundary is unknown, state the actual covered range rather than fabricate one.
2. Inventory the source transcript spans, scene records, continuity entries and checkpoints actually available. Retrieve accessible originals where needed; do not claim unseen source coverage.
3. Build a coverage list for every scene/segment and known missing interval. Deduplicate the same event appearing in multiple views. Apply scoped corrections while keeping their audit trail.
4. Reconcile chronological actions, dialogue, terms, mundane interactions and distinctive details against the source. Do not use only dramatic milestones or current inventory as the history.
5. Write the chronicle from those records. Preserve who initiated, what was said/decided, what actually happened and the response. Separate testimony and interpretation from independently established events.
6. Close with the actual current frontier, persistent changes and open threads. List omissions/gaps and declare whether the recap is complete for its stated scope and detail level.

Use a coverage table with `scene/segment | source range | account location | coverage/gap`. Every covered unit needs a substantive account entry; a completeness flag or a list of IDs alone is insufficient. Repeated source views do not create extra coverage. Do not claim completeness while a known scene is missing or only its heading survives.

A checkpoint is evidence about its frontier, not permission to overwrite a later valid save. A recap is a view of events, not a replay of them. Dialogue effects and actual resource transfers remain recorded once.

## 9. Persistence, capacity and missing records

The procedure must state what this deployment can actually persist. Unrecorded reasoning is not a ledger. Text posted in chat is visible evidence while accessible; it is not a verified external archive or a guarantee that every earlier message will remain available to the model.

When supported file tools are available and saving is authorized, update the actual current journal/scene archive and checkpoint files, inspect the returned save result and include the saved reference. Save through the existing identity/version where applicable. A failed write leaves the last successful durable frontier unchanged. Keep the newly posted entry marked unsaved until a later confirmed save includes it.

Without such tools, publish the checkpoint and complete export text in the conversation. Label it **posted in chat only**. At transfer or session close, provide the export needed for the user to retain and supply to the next chat. Do not claim a background file write, cross-chat memory update, project-source update or future retrieval that was not performed. Mention this storage boundary at initialization/checkpoints, not as repeated interruptions inside every narrative paragraph.

Use small append segments or complete scene files when that preserves retrievable detail better than one indefinitely growing synopsis. Track which segments are durable and which are still only visible in chat. Do not discard the scene history after producing a day summary. Archive resolved threads as closed history rather than silently deleting their occurrence.

If records are already missing, establish an initial recovery checkpoint from visible/retrieved sources only. Name the earlier unknown ranges. User-provided corrections can repair supported facts with provenance; do not disguise a reconstructed interval as a contemporaneous log. Request the missing source only when needed for the requested recap or consequential continuation. Continue independent supported activity where possible; missing history does not authorize fabricated bridge events.

## 10. Privacy and actor knowledge

Public continuity notes and checkpoints contain only information appropriate to the represented viewer. Do not reveal secret motives, hidden inventories, unrevealed events or concealed modifiers to make a public record more complete. Distinguish the player's OOC knowledge from a character's in-world knowledge when the campaign permits such separation.

Private continuity requires a genuinely private, recoverable store. A file accessible to the player, a collapsed section, encoded text or a hash is not private merely because it is labelled GM-only. If private persistence is unavailable, record that limitation without exposing secrets or claiming exact hidden-state recovery. Do not invent or revise secret past actions to fill the gap later.

## 11. Corrections, replay and resumption

A correction identifies its source, scope, affected entry and current valid wording. Preserve the original event identity. An erroneous representation is amended; no fictional refund, repair or extra conversation is invented. If the actual resolved history is explicitly retconned, record that distinct authority and its consequences rather than calling it routine editing.

Closed scene/day/chapter records need a correction annotation or new version when their underlying evidence changes. A replaced assertion cannot return through an older recap. Repeating “checkpoint now” at the same frontier produces a view/revision of that frontier, not duplicate events or new costs. Retain prior valid source coverage.

To resume, validate campaign identity, selected rules and actual checkpoint/source frontier. Load the supported current records and pending choices without replaying already committed events. Reconcile any later valid events before continuing. Stop at the actual open decision; do not select a convenient PC action to start a new scene.

## 12. Ready-to-use play instruction

The following block is complete enough to paste into a play chat. The full adapter above governs edge cases and storage limits.

```text
CONTINUITY AND RECAP PROCEDURE
Continue the existing game; do not restart or reconstruct missing events as facts.
After every GM reply that advances play, append a short separate Continuity note: scene/turn and supported time/place; what was actually done or said and by whom; material changes, promises and unresolved points; the open player decision. Preserve ordinary conversations and relationship interactions even when no stats change. Never invent the PC's feelings, speech or next action.
Checkpoint at every scene break, after five GM gameplay replies, after a critical continuity change, and on pause/transfer or request. Coalesce simultaneous triggers. These are editorial operations: no extra time, costs, rolls, healing, resource resets or NPC events. Do not close a day or scene merely to make a checkpoint.
Keep ordered scene records, not only a current-state summary. Carry earlier scene segments forward. Preserve actual wording where an oath, term, instruction, clue or other exact phrase matters; otherwise attribute accurate paraphrases. Do not fabricate quotations.
At day/chapter recap, inventory the available scene/source records and cover each scene chronologically. Include conversations, decisions, ordinary acts, promises, actual consequences and open threads. Do not recap only from the latest state or another short recap. State known gaps and the covered interval; never call a partial account complete. A brief recap is an additional view, not a replacement archive.
A portable checkpoint must include the supported current state, source coverage, retained uncertainty, pending events/work and the actual open choice, or verified accessible records containing them. Historical snapshots cannot overwrite later events. Logs and recaps never apply events twice.
Show only appropriate viewer knowledge. Save files only through available authorized tools and report success only after it is confirmed. Otherwise label checkpoints posted in chat only and provide the export for retention/transfer. Unrecorded reasoning and inaccessible links are not recoverable memory. Do not promise perfect recall or hidden-state persistence.
Apply this procedure from the supported current frontier forward. Earlier missing history remains a named gap until its source is recovered.
```

## 13. Acceptance specifications

These are requirements. The packaged verification report identifies the subset exercised by scripted reference checks. They are not all live-playtested cases.

| ID | Case | Required result |
|---|---|---|
| CC-01 | Quiet conversation with no stock changes | Dialogue and response captured; no invented relationship bonus |
| CC-02 | Fifth gameplay reply occurs inside an ongoing scene | One checkpoint; scene and open choice remain open |
| CC-03 | Fifth reply also transfers an asset and ends a scene | One checkpoint listing all reasons; one actual transfer |
| CC-04 | Five OOC/design/recap-only replies | No gameplay counter increment or game-time advance |
| CC-05 | Long scene spans several checkpoints | Scene record covers earlier and later segments once |
| CC-06 | Promise, conditional offer and accepted paid task differ | Their exact scopes and statuses remain distinct |
| CC-07 | Mixed inspection introduces a repair quote | Quote recorded; no automatic purchase or new PC action |
| CC-08 | Recap request during an unfinished day | Report ends at actual frontier; no automatic sleep/day closure |
| CC-09 | Day record covers all scenes, including ordinary work | Each covered scene has substantive chronological content |
| CC-10 | Known scene missing from a requested chapter | Partial coverage declared; no invented bridge or complete label |
| CC-11 | Same event appears in a turn note and checkpoint | One represented event; no doubled resources or scene count |
| CC-12 | Two simultaneous activities and a later report | Causal/pre-state relationship and receipt distinction retained |
| CC-13 | Recap paraphrases unavailable speech | No claim of verbatim quotation |
| CC-14 | Exact contractual wording remains available | Capture speaker, recipient, wording, conditions and response |
| CC-15 | Latest checkpoint available, earlier conversation absent | State recovery and history completeness reported separately |
| CC-16 | Portable handoff lacks a referenced actor sheet | Relevant dependent state incomplete; no “standalone” claim |
| CC-17 | File save fails after a visible record is posted | Durable frontier unchanged; entry marked unsaved |
| CC-18 | Tools unavailable in a normal play chat | Visible export, posted-only status; no claimed file update |
| CC-19 | Secret NPC intention matters | No public spoiler or invented private persistence |
| CC-20 | Correction applies to a closed chapter | Current record and affected recap amended with provenance |
| CC-21 | Repeated checkpoint at unchanged frontier | No event replay, cost, time, reset or reroll |
| CC-22 | Later valid save conflicts with older snapshot | Preserve later events; investigate scoped discrepancies |
| CC-23 | Day/chapter boundaries lack exact date/time | Retain bounded/unknown chronology; no invented precision |
| CC-24 | Prior events already outside accessible sources | Recovery baseline names gaps; no false retroactive logging |
| CC-25 | Source range claimed without substantive content | Reject completeness assertion |
| CC-26 | Very long reply contains many unique exchanges | Preserve all required details; shorten interval or checkpoint early |
| CC-27 | Character display name changes | Same stable actor identity and historical event references |
| CC-28 | Checkpoint review changes presentation scale | All current conditions, fractions, commitments and retained rolls persist |

## 14. CMRR, provenance, calibration and unresolved work

| Existing function / source | Disposition | Result |
|---|---|---|
| Core §§11–12, 90–91 event/state ownership | Retain and inherit | Journal captures already resolved events; no parallel simulation writer |
| Core §13 contextual panels | Retain | Compact relevant notes; checkpoints provide the broader export |
| Core §63 reports | Retain and specialize | Day/chapter chronicles cover dialogue and ordinary life beyond operations |
| Core §81 response pacing | Extend for ChatGPT play | Story, bounded resolution/reaction, visible record, player control |
| Core §82 OOC boundary | Retain | Logging, recap and recovery consume no game time |
| Core §86 compact journals/private persistence | Implement deployment procedure | Explicit capture, checkpoints, source coverage, storage status and privacy limits |
| Core §98 presentation adapters | Use existing owner | One shared adapter usable by AST or other genres |
| Core §§97/99 corrections and migration | Retain | Prospective output change; scoped corrections; no automatic world migration |
| AST E4/E7 runtime and persistence | Bind to this adapter | Record during play rather than trying to recover a whole day at recap |
| Existing AST engine/content/art facts and numerical gaps | Retain | No changed action bands, shield facts, current state or model activation |

Accounted replacements: this adapter supersedes relying on occasional implicit recollection or a latest-state-only panel as sufficient history in the selected ChatGPT deployment. It does not remove the underlying journal, turn sources, actor sheets, private-state limits or chronological events. Brief summaries remain useful views; they are no longer treated as the sole historical archive.

Source basis: the last verified AST 0.4 R1 package and its bundled Core 3.2 maintenance R3/SCL 1.0 dependencies, plus the user's 17 October 2026 request to address loss of day/chapter history. No actual campaign day/chapter was replayed, migrated or reconstructed for this design task. No external research or platform-capacity measurement is claimed.

Editorial calibration remains open: reply interval, note density, checkpoint length, retrieval burden, ordinary-dialogue retention, interruption cost and export usability. Evaluate in a controlled play session by comparing its source transcript against the chronicle and a second runner's continuation. Count missing unique exchanges, unsupported facts, incorrect attribution, duplicated events, lost open choices and recovered state differences. Written compliance and synthetic tests do not establish reliable long-session recall.

Deployment questions remain explicit: actual file-write access, available source archive, private persistence, current save coverage and the user's preferred balance between visible note length and story pacing. Five replies is a starting default that can be changed without changing game time or mechanics. No fixed cadence can recover already missing text or guarantee unlimited context retention.
