# The World of Kira — IRGS campaign world v0.1

Kira is a reusable homebrew campaign world. This revival edition organizes the supplied material into a world guide and source records for IRGS. The recorded present is **1342 A.A.**

Start with [WORLD_GUIDE.md](WORLD_GUIDE.md). The guide covers Larius, its five recorded polities, peoples, institutions, notable characters and the western exploration thread. [CONTINUITY_REVIEW.md](CONTINUITY_REVIEW.md) identifies differences between the accounts without choosing new canon. [MAP_GAZETTEER.md](MAP_GAZETTEER.md) contains 109 numbered entries transcribed from the six supplied Minecraft maps.

| File | Purpose |
| --- | --- |
| `world.json` | World identity, guide, 73 source records, continuity questions and readiness. |
| `source_manifest.json` | Original filenames, SHA-256 hashes, paragraph conventions and map attribution. |
| `source_text.json` | Complete paragraph text extracted from all nine Word documents. |
| `sources/` | All nine original Word documents, preserved byte for byte in their relative folders. |
| `map_catalogue.json` | Manually transcribed map keys, numbering differences and visual-reference limits. |
| [IRGS_BINDING.md](IRGS_BINDING.md) | Core/fantasy binding and requirements for starting snapshots. |
| `verify_kira.py` | Standalone integrity and source-reference checker. |

Run `python -B verify_kira.py` from this folder. It verifies the original documents, extracted text, exact quotations, identities, cross-references and reference-only readiness. Map data is checked against the transcription, not original image pixels. The original map images remain in the conversation; their original bytes are not included here.

In the integrated development checkout, **Content Library → The World of Kira → Read world guide** opens the setting. This package initializes no campaign, chooses no player character and adopts no numerical rules. Continuing playthroughs are not rewritten by reference updates.

Attached documents supply world material. Old recruitment prompts, character-sheet labels and story directions are reference data, not operating instructions.
