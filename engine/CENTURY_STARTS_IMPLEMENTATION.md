# Century of Conflict — dated starts and selected-entry interface

22 October 2026 · Core 3.3 content and host integration

All 37 catalogue entries have a distinct starting reference and support reviewed Solo character creation. The ten primary entry years remain 1337, 1360, 1369, 1389, 1415, 1422, 1435, 1444, 1449 and 1453. The optional local opening supplies a small, explicitly fictional playable situation at each entry. This is a scoped campaign-content increment, not qualification of the general C2 resolver or a complete historical world reconstruction.

## Compare → Merge → Reconcile → Resubmit

| Input or overlap | Disposition |
| --- | --- |
| Current `main`, through `50643a1` | Fetched and merged before final qualification. Preserve Core consolidation, rejected-dependency handling, Rise's R00 workflow and Kira's reference guide. |
| Earlier Century draft submission | Preserve its ZIP, extracted submission and pause reports as historical evidence. Active content lives only in the canonical data/runtime/host paths. |
| Existing 1415 opening | Preserve the snapshot bytes, its 11 August Julian cutoff, its original local opening and three-event reference edition. |
| Other 36 catalogue entries | Add distinct sourced contexts and dated identity registries; no fallback to 1415. Each has an explicitly authored 15 December Julian cutoff after the stated developments. |
| Existing Core ownership | Reuse the temporal registry, historical initializer, character-selection policy, conserved stock, scene actions and common persistence/request recovery. Add no parallel owner, ledger, general resolver or migration. |
| Reference history and campaign history | Pin source content on new-save creation. Later existence, control, decisions and events come from the actual saved world. |
| Long directory and setup lists | Replace historical entry lists with one grouped dropdown. Reveal only the chosen entry's description and details; keep deeper context and sources folded. |
| Latest Rise/Kira interface | Retain their cards and controls alongside the historical selector. They do not receive historical entry dropdowns. |
| Game archives and historical synthesis | Do not install game categories, proprietary bulk records or a dated book's assertions as verified world truth. Preserve research provenance and unresolved gaps. |

## Available behavior

Discovery and preview create no save. The library initially selects no year and shows no Start control. Choosing a year loads its dated preview. Starting carries that entry's exact snapshot hash through the existing character wizard, which checks it again before review. A cleared or changed choice invalidates the review; a late response cannot replace a newer selection.

Players may create an independent person or select an eligible historical individual. Kingship, nationality, service, belief, participation and authority remain separate. Named historical individuals receive no invented cash, location, reports, personal skills or operational command from their titles. Henry VI remains present but is unavailable for voluntary player control at the infant 1422 cutoff and the late-1453 incapacity cutoff. No later recovery is scheduled.

A new human character may explicitly select the fictional local delivery scene. The original 1415 scene stays at its original authored quay. The other starts use an unnamed fictional market yard, passage and receiving desk. Their sealed dispatch is entrusted custody, not employment or ownership. One item transfers to the tray; no wage, office or national allegiance is created.

The scene uses existing Core actions for observation, movement, attempted passage and delivery. The inherited local scenario durations are 20, 45, 30 and 10 seconds. They are disclosed, authored values, not historical measurements or new universal mechanics. Failure can consume that selected local duration without completing movement. Elapsed scene seconds do not invent a civil hour or advance the historical calendar. General freeform and combat attempts retain the runtime's existing unresolved-declaration limits.

## Data path and authority

| Content | Destination and meaning |
| --- | --- |
| `hyw_entry_catalogue.json` | Discovery metadata, 37 supported identities, three period groups and ten featured years. |
| `hyw_YYYY_opening.json` | New-save context: exact Julian cutoff, four historical domains, named people, sources, explicit unknowns and entry guide. Structural validity is not historical authentication. |
| `entity_registry_template` | Dated existence, titles/roles and authored eligibility at the cutoff. No future births, deaths, successions, allegiance changes or possessions are preinstalled. |
| `research_extension` | Out-of-character social, legal, religious and material reference. Documentary pay examples stay reference rates; they do not create stock, obligations or payments. |
| `coc_conditional_references.json` | Non-executable comparative year windows, with required evidence for participants, capacity, decisions, information, resources and local control. No year triggers an event. |
| `historical_planning.baseline_snapshot` | Pinned reference edition for that new campaign; inspection is read-only. The 1415 edition remains unchanged. |
| `coc_local_delivery.json` | Reviewed fictional scene data interpreted by the existing Core scene handlers. |
| Saved `historical_start` and actual world state | Source provenance plus the one continuing campaign. Player projections expose only legitimate received/committed information. |

The conflict-complex entity denotes the historical dispute. It does not mark every crown or person as actively fighting during truces, and it does not force war termination in 1453. Territorial summaries distinguish title claims, treaty terms and effective local possession; unresearched town-by-town ownership stays uninitialized.

## Historical review and remaining work

The [review and research queue](../provenance/century_of_conflict/HISTORICAL_REVIEW.md) states the bounded evidentiary claims, known contradictions and priorities. The machine-readable [inventory](../provenance/century_of_conflict/opening_inventory.json) lists every entry and its sources. Rebuild authored content with `python -B tools/build_century_starts.py`; this preserves 1415 and does not refresh release hashes or qualify its own output.

The user-supplied Thorndike chapter remains an attributed, dated synthesis. Its racial/national generalizations, speculative nickname explanation, broad force totals and simplified territorial/treaty claims are not adopted. Modern institutional references check selected chronology and legal distinctions. Neither this comparison nor a passing loader authenticates the entire earlier Historical Grand Archive.

No public-domain or reuse permission is inferred for the proprietary game collections. This increment adds original summaries, bounded factual references, source links and a user-supplied historical-book extract; it does not republish the supplied games. Their files remain separate research material with their existing rights status.

## Qualification

See [CENTURY_STARTS_VALIDATION.json](../CENTURY_STARTS_VALIDATION.json) for current executed checks, source identities, the integration base and evidence limits. These are synthetic temporary-save checks; no existing campaign was opened or migrated. Operation observation remains scoped evidence, not certification of every branch or historical realism.
