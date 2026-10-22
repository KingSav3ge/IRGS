# Century of Conflict — paused work submission

**Paused at the user's request · 21 October 2026 · Work in progress, not a qualified release**

This submission contains the actual edits made before the pause. No save was opened, migrated or edited. No commit, push, public publication, deployment or running-host replacement was performed.

## Written so far

- 36 new dated opening drafts, covering every previously undeveloped catalogue entry. The existing 1415 opening is unchanged, giving 37 structurally loadable entries including all ten featured years.
- Each draft contains political, territorial, diplomatic and practical context, source references, a small dated roster, an entity-registry template, player briefing, conditional research requirements and explicit unknowns.
- New drafts use an **authored 15 December checkpoint** after the stated year's developments. This is a scenario-design choice, not a newly discovered event date. The inherited 11 August 1415 Julian cutoff is preserved.
- The snapshot loader no longer accepts only 1415. It checks the selected entry's date, year, Julian calendar and registry coordinate.
- The 1403 presentation distinguishes the Welsh war and Channel conflict from the later 1404 alliance and major 1405 French expedition; the prior title is retained as provenance.
- An authoring/compiler tool and 28-source research register are included, together with the chapter of the supplied historical book used for broad context.

## Check actually performed at pause

All **37/37** catalogue entries loaded through the updated snapshot validator, including registry validation, without error. Their rosters contain 99 actor rows across the different dates, not 99 unique people. This was a structural/load check only. It did not create a campaign, resolve actions, independently verify every historical claim or test the interface.

## Not finished

- The requested **dropdown and selected-entry details interface has not been implemented**. The website files are unchanged.
- The optional local playable scene is still the existing 1415 scene. A scene for every other start was proposed but not written or connected.
- The new historical drafts have not received complete claim-by-claim review. Some references were available through institutional search extracts or abstracts, and the older book requires critical comparison. The source register is not a statement that every full document was downloaded or authenticated.
- The draft snapshots carry the existing developed-setup status so they can exercise the loader. This is **not** release qualification or evidence that all historical gaps are filled. Exact military stocks, finances, local populations, jurisdiction maps and individual circumstances remain incomplete.
- Campaign creation, character selection, save/load, independent allegiance, branch continuity, prospective history, action execution and browser checks have not been newly tested across the 37 entries.
- Existing tests that assume only 1415 is ready still need revision. Release hashes and the unified development manifest have not been refreshed. The changed checkout must not be described as a verified distributable release.
- The current historical-plan baseline still contains the earlier three 1415 references; it has not been expanded into a complete conditional framework for all starts.

## Resume sequence

1. Review and qualify the dated historical drafts, rosters and territorial statements; expand local social, economic and institutional evidence with clear uncertainty.
2. Replace the directory's large entry lists and the setup's button lists with a dropdown. Show only the selected entry's descriptions, details, sources and valid Start action. Preserve stale-response and exact-hash checks.
3. Connect explicitly reviewed authored local circumstances to each supported new-character start using the existing Core action owners. Keep historical evidence separate from fictional scene facts and conserve resources.
4. Add meaningful all-entry creation, identity, information, continuity and UI tests. Run relevant runtime, Web and interface suites.
5. Refresh release hashes and the development inventory only after the source changes and results are reviewed; verify and package through the unified workflow.

## Bundle use

This is a **change bundle**, not a complete runnable installation. Paths are relative to `IRGS_Development`. The Git patch contains tracked edits; newly added files are included separately at their repository paths. The unchanged 1415 snapshot is included for comparison. `submission_manifest.json` records hashes. Existing source and save directories should be preserved.
