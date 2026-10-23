# AI provider assessment review

Checked 22 October 2026 against the sources below and the current four-repository setup. The user's original submission remains unchanged. [Research evidence and arithmetic](provenance/qa/ai_provider_strategy/RESEARCH_REVIEW.json) records retrieval times, body hashes, relevant excerpts and limitations. These are documentation observations, not provider benchmarks or account-specific quotes.

## Findings for IRGS

The provider-neutral architecture fits the existing master plan. It should extend its six Director categories and planned Capability Broker, keeping the twelve proposed responsibilities as task types. The current application is Python plus vanilla JavaScript; there is no reason to select infrastructure on TypeScript integration alone. Vercel explicitly supports Python/HTTP access from outside Vercel, so it remains a valid comparison candidate without a platform rewrite.

The model assignments are hypotheses. No candidate has been evaluated here for IRGS character fidelity, dialogue, knowledge boundaries or sustained play. Official context/tool/structured-output claims do not establish compliance with IRGS rules. No live inference requests were made and no model credentials are configured in this environment's observed bindings.

The submission's nine 100-call calculations are correct at their stated rates and rounding. Mercury's exact estimate is **$0.135**, displayed as $0.14. The blended example is **$0.024175 per interaction**, or **$2.4175 for 100**, correctly rounded to $0.02418 and $2.42. These are token-only scenarios, not measured gameplay costs or funding for unlimited lifetime AI use.

## Checked direct-provider rates

USD per million uncached input / output tokens, under the stated conditions. These are research records, never activated runtime rate cards.

| Model | Rates | Qualification and official source |
| --- | --- | --- |
| GPT-6.1 Sol; GPT-6 Luna; GPT-6 Astra | $2/$10; $0.10/$0.50; $10/$50 | Standard processing. Other processing modes, caching and eligible regional endpoints differ. [OpenAI pricing](https://developers.openai.com/api/docs/pricing) |
| Claude Sonnet 5.5; Opus 5.5; Haiku 5.5 | $2/$10; $4/$20; $0.10/$0.50 | Haiku's quoted low rate applies to prompts up to 100,000 tokens; above that the page lists $0.50/$2.50. [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing) |
| Gemini 4 Argon | $2/$10 through 30 November 2026 | Listed to become $4/$20 on 1 December. Paid standard tier; output includes thinking tokens. [Google pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Gemini 3.8 Flash | $0.75/$3.75 through 31 December 2026 | Listed to become $1.50/$7.50 on 1 January 2027. Paid and free data-handling conditions must be evaluated separately. [Google pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| DeepSeek V4.1 Flash 1017 | Off-peak $0.15/$0.60; peak $0.30/$1.20 | Current direct API ID is `deepseek-flash`; page identifies the underlying version separately. Peak windows are 01:00–04:00 and 06:00–10:00 UTC on weekdays excluding Chinese public holidays. An alias is not a guaranteed immutable version. [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing/) |
| Mistral Small 4 | $0.15/$0.60 | Page lists `mistral-small-2603`, 256k context and Apache 2.0. [Model documentation](https://docs.mistral.ai/models/mistral-small-4-0-26-03) |
| Mistral Large 3 | $0.50/$1.50 | Page lists `mistral-large-2512`, 256k context and Apache 2.0. [Model documentation](https://docs.mistral.ai/models/mistral-large-3-25-12) |
| Mercury 3 | Introductory $0.10/$0.35 | Page displays 50% off $0.20/$0.70, 1M chat context, tool calling and structured outputs. No promotion end date was established in this review. [Inception models](https://docs.inceptionlabs.ai/get-started/models) |
| GLM-5.3 Flash; GLM-5.1 | $0.15/$0.50; $1.40/$4.40 | Direct rates; distinguish cached input/storage and tool fees. [Z.ai pricing](https://docs.z.ai/guides/overview/pricing) |

The public [OpenRouter model catalogue](https://openrouter.ai/api/v1/models) also lists the major candidates, including MiniMax M2.7, Kimi K3 and Qwen 3.8 variants. Its per-token gateway prices are separate from direct-provider prices. For example, its retrieved Gemini 3.8 Flash entry lists $0.825/$4.125 per million, while Google's direct page lists $0.75/$3.75. The access route must therefore be part of every price and performance observation.

This pass does **not** substantiate every original claim. MiniMax's attempted direct pricing URL returned 404; the retrieved Kimi page did not expose the asserted K3 price in readable content. Their direct-price claims remain unverified here even though candidate models appear in OpenRouter's catalogue. Qwen regional prices, xAI, Cohere, inference-host comparisons, detailed licenses outside the cited Mistral pages, gateway purchase/BYOK fees and the specific LiteLLM vulnerability/version claim require separate source checks before use. A successful HTTP response or an empty dynamic page is not verification.

## Infrastructure and policy

[Vercel's documentation](https://vercel.com/docs/ai-gateway) states zero provider-token markup and access from any infrastructure, with Python/HTTP-compatible clients. This does not establish lower total cost after every applicable service or billing charge. [BLACKBOX's page](https://www.blackbox.ai/api) advertises 300+ models and an OpenAI-compatible endpoint. Its privacy marketing includes qualifications about downstream provider support; that is not an end-to-end contract review. [OpenRouter's policy documentation](https://openrouter.ai/docs/guides/privacy/provider-logging) distinguishes provider training, retention and regional controls.

For each enabled route, record the actual gateway and host terms, version, permitted workloads, data classification, processing region and reporting support. Browser keys, unrestricted fallback and assumptions that publicly accessible content is licensed for external processing do not satisfy the proposed policy. Such checks belong in the selected route's implementation and configuration; no provider approval or policy verification is implied by this research.

## Development disposition

Use the [master-spec addendum](AI_PROVIDER_STRATEGY.md) and the component work orders. First build and test the disabled-by-default adapter/access/ledger contract with fake transport, then qualify one opt-in direct integration beside an already supported gameplay operation. Add comparative providers and routing only after that bounded flow works. Keep unknown provider charges and unrun model evaluations explicit.

Historical Details was subsequently integrated with the complete archive and reviewed App dependencies. The user's 23 October priority is completion of the Solo runtime; follow [the completion plan](SOLO_COMPLETION_PLAN.md) and `solo-runtime-01` work orders. This research review establishes no provider implementation, paid service activation or model-quality result.
