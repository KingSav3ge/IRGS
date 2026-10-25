# IRGS 3.4.1 development

Previous release: **3.3.3**. Earlier 3.4.0 development evidence remains labelled
with its original source identities; it is not a new acceptance run.

This coordinated update joins the three development repositories. Engine exposes
actor-safe start discovery and received phase commands over selected observation
and work handlers. App provides explicit Begin/review/continue controls, durable
private pending requests, atomic world/result persistence and recovery of the
original outcome after lost replies. Catalog adds separately versioned consumer
contracts while preserving original exact-consumer fixtures and archive records.
The coordinator aligns App dependency pins and fixes standalone Catalog
compatibility verification: sibling modules load from their exact owned paths,
without depending on sys.path or foreign cached modules. Current start discovery
is checked against the actual App/Engine contract before combined qualification.

All four repositories identify this edition as 3.4.1. Development manifests and
archive defaults read VERSION.json; automatic QA retains local reports for a
versioned coordinator publication. Every subsequent unified main push increments
the version through 3.4.9 then 3.5.0, unless a qualified 4.0 candidate is assessed.

The selected executable Core compatibility remains 3.3. Existing campaign rules,
archive bytes, schemas and independent content versions retain their identities.
General freeform/combat, wider DEV/C2, communication controls, operator setup,
live model evaluation, Windows and distributed hosting remain bounded/open work.
No live inference or user campaign migration is part of this update.

Fresh qualification results and exact component identities are recorded in
provenance/qa/phase_integration_3_4_1_review.json with the delivered build.
