# AI provider foundation backlog

Status: IRGS 3.4.0 development under `solo-runtime-01` now has typed scoped requests, the initial registry/Capability Broker, conservative concurrent reservations, durable attempt/replay accounting and explicit acceptance through existing local/Rise Core handlers. See [the version 1 API](SOLO_PROVIDER_API.md), [opt-in direct adapter review](OPENAI_ADAPTER_REVIEW.md) and [pinned Catalog R00 execution](SOLO_CATALOG_VALIDATION.json). HTTP integration is implemented with synthetic tests; no paid inference, model-quality result or connected App qualification is claimed. Historical Details is integrated. Follow the current root work order and the coordinator's [Solo completion plan](https://github.com/KingSav3ge/IRGS/blob/main/SOLO_COMPLETION_PLAN.md).

The coordinator's [master-spec addendum](https://github.com/KingSav3ge/IRGS/blob/main/AI_PROVIDER_STRATEGY.md), [checked research](https://github.com/KingSav3ge/IRGS/blob/main/AI_PROVIDER_REVIEW.md) and [16 evaluation requirements](https://github.com/KingSav3ge/IRGS/blob/main/provenance/qa/ai_provider_strategy/EVALUATION_CASES.json) were reviewed. These extend master Part XI; the original AI-01–AI-12 sections retain their identities. Research observations and token-price examples do not activate runtime configuration or establish a model-quality winner.

## Completed preparation

- Recorded the Engine requirements, stages, ownership and verification gates below.
- Preserved the existing six Director categories: Game Master, World, National, Regional, Local and Scene. The twelve proposed responsibilities are logical task types, not additional Directors, mandatory calls or state owners.
- Kept Core and the nine existing K-owners authoritative. Model output can propose an intention or present authorized committed records; it cannot grant permission, supply an unsupported rule or commit an outcome through narration.

## Required implementation

All nine broader items remain open. AIP-01–AIP-06 and AIP-08–AIP-09 have the bounded implementation described in the API: approved local/Rise proposals, static explicit routing and conservative lifetime ceilings. AIP-07 now uses Catalog `2e4f389882df0807fc8064c1a0b533aaa3b1bcd3` R00 inputs plus local synthetic cases; this is integration evidence, not model evaluation. The direct adapter's official contract and fake HTTP paths are checked. Connected App/session persistence, policy/price/account review, reconciliation and model-quality evidence retain their separate gates.

The [24 October lifecycle increment](SOLO_LIFECYCLE_VALIDATION.json) qualifies early cancellation, serialized admission, independent rejected duplicates and cached expiry/cancellation. These strengthen AIP-02/AIP-04–AIP-06/AIP-08 without enabling dispatch by default, refunding uncertainty or claiming App/live-model qualification.

| ID | Engine work | Completion evidence |
| --- | --- | --- |
| AIP-01 | Disabled-by-default provider/model registry: developer, gateway, actual host, exact API ID, known/unknown version, claimed/tested capabilities, limits, lifecycle, workload approvals, policies and versioned rates. | Missing configuration stays unavailable; candidate entries do not authorize dispatch. |
| AIP-02 | Typed request/result/access contracts, fake transport, bounded deadlines/output/retries/cancellation; then one opt-in direct adapter with server-only credential references. | Offline failures and recovery pass before direct integration; check the exact current official API/model contract before implementing that adapter. |
| AIP-03 | Map logical responsibilities to the scoped Director design and planned Capability Broker. Record task contracts, qualified candidates, validators and explicit fallback lists. | No competing registry, extra Director, broader access scope or assumed character fidelity. |
| AIP-04 | Route only among capability-, workload-, information-policy- and budget-eligible candidates; use measured evidence for later ranking. | Finite concurrent reservations, bounded retries and fallbacks; no route widening or intelligence/mechanics changes by access tier. |
| AIP-05 | Validate output structure, actual supported operation, intent/source references, caller authority, actor knowledge and state/restore freshness. | Use selected Core handlers for effect/recovery claims. Mechanical and agency failures reject output regardless of prose quality. |
| AIP-06 | Attempt ledger separating requested and reported actual model/developer/gateway/host, versions, request IDs, timings, validation, token estimates/reports and known/unknown charges. | Failed, cancelled and retried attempts remain accounted for without leaking secrets or treating unknown usage as free. |
| AIP-07 | Versioned synthetic evaluation harness with actor-authorized input, evaluator-only oracles, exact prompt/schema/adapter/model versions and repeated measurements. | Run the applicable AIP-E01–AIP-E16 requirements; keep integration tests, human/blinded character review and measured model results distinct. |
| AIP-08 | Reviewed model/routing migration, provenance-preserving receipts and cache scoping by campaign/branch, actor, permission, state/source, prompt/schema and model configuration. | No historical rewrite, implicit model substitution, cross-actor cache reuse or stale result after restore. |
| AIP-09 | Enforce source rights/classification and actor knowledge alongside gateway/downstream host workload, retention/training and geography requirements. | Missing required policy/host identity makes a route ineligible; retrieved content cannot instruct execution or grant data-transfer rights. |

## Delivery sequence

1. **AIP-S1, offline foundation:** implement registry/access/request/result contracts, fake transport, response validation, attempt identities and finite dispatch reservations. Exercise rejection, replay, timeout/cancellation, stale state/restore, disallowed fallback, actual/requested identity and concurrent budget use. Keep character intention distinct from its expression. Existing supported Core operations retain their actual effects and receipts; general freeform remains unresolved.
2. **AIP-S1, direct adapter:** check an exact official API and account-model contract, then add one disabled-by-default opt-in adapter. OpenAI is an initial integration candidate. The models exposed to Codex supply no IRGS API entitlement or measured quality result. Deliver Engine APIs for App qualification; keys and administration remain server-side.
3. **Conditional live smoke:** require configured server credentials, an authorized workload and a finite explicit budget. None is supplied by the work order. Offline tests must not imply paid-call approval, policy approval, benchmark success or an active narrator network.
4. **AIP-S2/S3:** compare other direct/gateway candidates, then add measured conditional routing, eligible failover and migration under the same contracts. Vercel Python/HTTP access is a candidate for the existing host; no hosting/framework rewrite or mandatory stacked gateways are selected.
5. **AIP-S4:** consider dedicated/open-weight hosting and fine-tuning only with measured demand, licenses and total operating costs. Fine-tuning never stores authoritative campaign state.

App owns protected developer status, disabled/error presentation and later consumption of the reviewed Engine API. Catalog owns independently reviewed source rights and evaluation material. The coordinator reviews exact Engine/App/Catalog commits and the pinned pair before joined publication. This backlog grants no additional authority over campaign state or another component repository.
