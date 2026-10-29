# Reviewed ordinary offers and two-context drafts

29 October 2026; 3.4.5 Pre-Alpha. This bounded A4-ENG-03/A4-ENG-01 and
WB-ENG-01 increment extends existing Core contracts. It does not qualify an
Alpha gate, supply autonomous NPC choices, or implement a general world editor.

## Optional fictional Rise offer profile

A normal R00 setup may explicitly add `offer_profile` with value
`founder-household-offer-v1` to the existing choices. The normal preview then
adds `offer_setup` with the selected fictional source, mandate ID, permitted
account and a clear no-consent/no-transfer notice. It is included in the review
digest. Omitted profile retains the original default and no offer capability;
a changed selection invalidates the old review. Only explicit reviewed creation
installs the `settlement_free_stock` channel profile and a founder mandate
`founder-household-offer` limited to `founder-home`. The mandate covers the
communication operation with an explicit household-offer/account scope; it
does not authorize raw `transfer_stock` through the decision workflow. The selected source is
`authored-fictional:greywater-reach:founder-household-offer:v1`. This is a
fictional selected rule, not inferred rank, another actor's authority or a claim
about historical law. Existing campaigns are never modified or reseeded.

The existing `communication_contract` and `supported_intent.offer_prerequisites`
show an attemptable offer to a received channel participant. The player supplies
exact terms, their own reviewed account and the mandate; Core rechecks control,
recipient household and co-location, custody and actual authority. An offered
proposal reserves or transfers no stock and does not check free stock; fulfillment
uses the existing actual free-stock and authority checks. Speech and an offer are
not acceptance. A user can explicitly withdraw their proposal; no NPC decides or
consents automatically. Current native acceptance requires the actual controlled
recipient; this increment does not make an NPC player-controlled.

The existing App HTTP host accepts a reviewed explicit selection via the normal
R00 preview/create endpoints and existing communication prepare/execute endpoints.
The current setup UI does **not** expose the optional profile; App must add an
explicit choice and display its review before ordinary UI users can select it.
No App source or pin changes are made here.

## Selected two-context draft

The additive `irgs-world-draft-1` contract now accepts, alongside fictional
`rise-r00`, the tightly selected `historical-quay` profile with classification
`mixed`. Its choices must contain the exact verified `hyw-1415` snapshot SHA and
a named new human selecting `quay-contact-v1`. Validation uses actual historical
source selection, Engine starting options and `review_start`; the resulting
review and draft digests fence later initialization. It creates a fresh candidate
through the existing `initial_campaign` and `initialize_player`, only after
explicit acceptance and a second source/options review. Historical reference and
fictional player/scene context remain separately identified. The received civil
day has no historical hour or elapsed-calendar binding. Drafts cannot edit live
campaigns, arbitrary geography, people, stock, rules or executable scripts.

Host atomic creation/persistence, duplicate acceptance, restored branch handling,
portable packages, arbitrary maps, authoring of custom entities and Catalog's
independent content examples remain separate. The initial preview is
out-of-character; player views must use their actual received records.

## Evidence and handoff

`test_ordinary_offer_profile` covers explicit selection and stale review, proposal,
withdrawal, original-result retry, no stock transfer, wrong recipient and
unauthorized account rejection and refusal of raw-transfer authority.
`test_world_draft` covers both selected profiles,
source digest rejection, real non-Rise observation and saved continuation.
`test_supported_intent` retains actual selected actions/refusals and immutable
retry across both ordinary contexts. [HTTP qualification](../tools/qualify_ordinary_offer_http.py)
uses real App preview/create/prepare/execute and exact retry/reload in a synthetic
temporary store, with zero provider calls. It is an API journey, not a completed
browser setup journey. [Exact source and checks](OFFER_AND_DRAFT_VALIDATION.json)
record the selected App/Catalog and their unchanged pins.

Remaining: App review controls and compatible pins, separately selected Catalog
consumer qualification and pack design, richer intent/offer UX, genuine NPC and
institution decisions, arbitrary world authoring and the coordinator's exact-set
Alpha checks. No live provider, Windows, package or browser qualification is claimed.
