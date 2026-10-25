# IRGS development coordination

Current integration: **shared-response-integration-02**, **3.4.0 development**.
Continue [shared IRGS scope](IRGS_SYSTEMS_SCOPE.md) across campaigns and themes.

| Reviewed component | Exact commit |
| --- | --- |
| Engine | `2f9476c6090878257d17cab3ad3a83a7ce18a5dc` |
| App | `aae8a25656c890181e0aa569df2c716968ec3642` |
| Catalog | `27fff8385d1c01fdfe9ad7254b7647e6bc12a01e` |

Engine publishes provider-independent actor/capability/intent/receipt contracts
and the exact neutral response depot. App now consumes Engine receipt/draft
interfaces and selected Catalog semantic drafts server-side. Ordinary actions,
optional assisted acceptance and saved results retain exact outcomes and local
presentation. Draft selection commits nothing. Additional shared intent/process/
communication App controls and semantic adapters remain separate work.

The coordinator aligned both pins and fixed a reproduced response-intake race:
loading now consumes the same bytes whose hashes were verified. Fresh actual
operation capture replaces stale joined evidence. Full regression, current
Catalog arcs, two-context Chromium and six synthetic profile checks passed.
See [exact review](provenance/qa/shared_response_integration_3_4_0_review.json).
Clean-package/browser qualification is recorded with the external release.

Original fixture contracts and archives remain preserved. The Catalog's eight
declared-consumer tests run against their original exact commits; new current
consumers have separate qualification. Content portability and unresolved generic
declarations establish no new campaign mechanics. No live inference was made.

Further imports require exact compatible three-component review and gated sync.
QA monitoring tests new pushes while this environment runs; repository work
orders provide handoffs without claiming chat dispatch.
