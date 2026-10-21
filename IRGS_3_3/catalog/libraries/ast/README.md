# A Scot's Tale — ChatGPT continuity edition 0.5

**Date:** 17 October 2026. **Parent:** Core 3.2 maintenance R3 and SCL 1.0, unchanged. **New adapter:** IRGS ChatGPT Play Continuity 1.0.

The engine now specifies recording during play, so a day/chapter recap has a source-backed history to use. The current-state checkpoint and the chronological scene record have different jobs; this edition requires both.

Use the three separate current project files:

- [AST Engine 0.5](AST_Engine_v0_5.md)
- [AST Content Library 0.5](AST_Content_Library_v0_5.md)
- [AST Art Direction 0.5](AST_Art_Direction_v0_5.md)

The [shared adapter](IRGS_ChatGPT_Play_Continuity_Adapter_v1_0.md) is reusable with other IRGS genres. Its section 12 contains a ready-to-use instruction for a play chat. Load this edition in the play chat, or copy that instruction there; creating this package does not by itself modify another conversation's instructions or project sources.

The default is a short separate Continuity note after each GM gameplay reply, a checkpoint at every scene break and after five gameplay replies, and an early checkpoint for critical changes, pauses and transfers. Coincident triggers produce one checkpoint. OOC discussion and recap work advance no game time. Five replies is an adjustable editorial default rather than a memory guarantee.

Scene records retain conversations, ordinary work, promises, questions and relationships as well as mechanical changes. Day/chapter recaps account for every available scene and name missing source ranges. Missing dialogue is not reconstructed as exact speech. A recap cannot close an unfinished day, choose the PC's response or process transfers twice.

At checkpoints, the play chat must distinguish a confirmed file save from text posted in chat only. Without available file tools it publishes an export for retention; it cannot truthfully promise an automatic background save. Original transcripts remain necessary for full dialogue/manuscript transcription. Secret-state continuity requires actual private storage.

The package contains no actual current campaign save, retrospective day reconstruction or new numerical combat model. Existing AST historical facts, source status, shield correction, action bands, model gaps and all 75 inherited acceptance specifications are retained. The requested recording procedure is a prospective presentation change; other inherited proposals remain proposals.

[The receiving binding](AST_Receiving_Binding_v0_5.json) pins the adapter and bundled providers. [The reconciliation record](CMRR_Chat_Continuity_v0_5.md) accounts for the changes. [Verification results](verification/RESULTS_v0_5.json) identify the scripted checks and their limits.

To repeat the checks with Python 3.12 or later, standard library only, run:

```text
python -X utf8 verification/verify_ast_v0_5.py
python -X utf8 verification/check_chat_continuity.py
```

The inherited verification suite checks package/source preservation and bounded reference examples. The new suite checks deterministic checkpoint, scene, coverage, quote, correction and storage examples. Neither is a live test of long-chat recall.

The [29 character-board references](references/Visual_References.md) remain linked to their separate existing archive. The imperfect shield reference remains bundled and subordinate to the written correction. Image bytes and content definitions are unchanged. Older full engine editions, previous reports and source ZIPs are not bundled as competing current files.
