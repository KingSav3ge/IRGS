# Century of Conflict — pushed work-in-progress checkpoint

Stopped at the user's explicit request on **22 October 2026**. This checkpoint supersedes the work status in the retained 21 October paused submission. It is not a qualified release.

Implemented so far:

- All 37 catalogue entries have separate dated, source-attributed opening references. The ten primary years remain intact. New checkpoints use an explicit authored 15 December cutoff; the existing 11 August 1415 Julian opening is preserved.
- The campaign directory and setup screen now use dropdowns and display the selected entry's descriptions and details. Snapshot-hash checks and stale-response protection remain in place.
- New human characters can opt into an explicitly fictional local delivery scene at each start through the existing Core action handlers. Existing historical people receive no fictional possessions or automatic institutional authority.
- New entries receive pinned, read-only conditional research references. These never execute historical deaths, battles, treaties or a campaign end.
- Historical sources, proposed causal requirements, documentary rates, authored scene values and actual campaign state remain distinct. The archive has not become a fully reconstructed historical world.

Executed checks:

- **Runtime: 463 run, 462 passed, one expected external-fixture skip.** The added tests exercise each real opening, new-character setup, local scene actions, conservation, save/load and read-only historical references.
- **Interface: 51 checks passed before one new full-catalogue selector assertion failed (0 observed markup matches versus 37 expected).** This failure was not fixed after the stop request.
- **HTTP: not passed.** The sandbox denied loopback client connections with WinError 10013; the recorded run has 96 errors and five consequential failures. The newly added all-entry HTTP creation test still needs execution.
- No visual browser verification was performed. No general action resolver, combat system or autonomous calendar advancement was added.

Remaining qualification includes historical claim review, the failing interface assertion, permitted local HTTP tests, visual browser checks and updated operation-coverage evidence. Integrity hashes record the intentional checkpoint files; they do not make the checkpoint a verified release. Existing release-validation counts are inherited evidence, not current acceptance results.

No existing user campaign was opened or migrated. Saves, runtime logs, credentials and browser data are excluded from the commit. The accompanying JSON records the current results and local log hashes.
