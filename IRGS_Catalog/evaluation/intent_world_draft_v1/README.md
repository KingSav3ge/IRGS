# Independent intent and World Draft candidate v1

The first Engine world-draft contract `irgs-world-draft-1` currently selects
only the existing fictional Rise R00 initializer. This Catalog-authored draft
uses supported R00 choices; it maps the original Reed example's fictional name
and family to the selected profile, but does not map or invent custom geography,
actors, custody, an item, rules or knowledge. Those prior proposed authoring
requirements remain separate and unchanged. The fictional non-Rise Lantern
example remains unsupported by this DTO. No third-party assets or source records
are imported; the existing R00 profile and its sourced fictional introductions
remain Engine-owned. There is no general world-pack or editor qualification.
The [source dossier](SOURCE_DOSSIER.md) records the limited mapping and gaps.

Independent actor inputs and evaluator-only expectations are separate. The
selected candidate sources are Engine `44ea8b0f66801c12a039c0046128177d2ea6d7d8`
and App `4f7cbd703d1207ae32db2bbc90d429415ae1e13f`. App still pins Engine
`296e46a1beed10d0ebf2841f133bb52fade83697` and Catalog
`e97d87f0d17a16dbe0ce186badafe663188321a1`; both newer selected components are
explicit overrides, not adopted pins. The containing Catalog commit identifies
this fixture. Earlier fixture identities, selections and evidence are not changed.

The independent consumers exercise actual Engine draft validation/review and
explicit initialization and actual App HTTP ordinary creation and reviewed intent
execution in both contexts. Intent text remains exact; a reviewed choice is not
a success guarantee. Tests include no-effect review/decline, the real failed
shortcut and alternate delivery, actual R00 work, original retries after restart,
and restoration of an older synthetic checkpoint with future intent rejection.
The structural grounding comparison uses actual committed receipts and does not
infer unrestricted language semantics or establish live AI quality. No live
provider, user saves or creator editor is used. A draft initializer alone does
not establish atomic host persistence, package import/export or editor behavior.

```bash
IRGS_CANDIDATE_ENGINE_SOURCE=/path/to/Engine \
IRGS_CANDIDATE_APP_SOURCE=/path/to/App \
python -B -m unittest tools.tests.test_intent_world_draft_consumers -v
```

See root `INTENT_WORLD_DRAFT_VALIDATION.json` for executed results and open gaps.
