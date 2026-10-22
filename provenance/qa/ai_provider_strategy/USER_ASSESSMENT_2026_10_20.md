# IRGS — AI Provider Research & Optimal Deployment Strategy

Research assessment · October 20, 2026 · Proposed architecture v0.1

## Executive recommendation

IRGS should become a multi-provider AI platform with its own intelligence coordinator, direct access to selected model developers, and secondary access through independent inference providers.

I would not make OpenAI, Anthropic, Google, BLACKBOX, or any other company the exclusive provider.

The objective is to select the best-performing model for each IRGS responsibility while maintaining control over simulation accuracy, narrative quality, intellectual property, availability, and operating costs.

The initial shortlist should extend beyond mainstream AI companies to include DeepSeek, Mistral, Inception, Qwen, Z.ai, Moonshot AI, and specialized inference providers.

Two emerging options are particularly interesting:

- DeepSeek V4.1 Flash: A relatively inexpensive model with tool calling, JSON output, long context, and substantial potential for routine autonomous simulation tasks. Its official API pricing is currently $0.15–$0.30 per million uncached input tokens and $0.60–$1.20 per million output tokens, depending on peak periods.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://www.deepseek.com\&sz=32)

  deepseek.com

  +1

- Inception Mercury 3: A newly released diffusion-based language model optimized for extremely fast generation. Its introductory API price is $0.10 input / $0.35 output per million tokens, with a million-token context window. Those characteristics make it an especially interesting candidate for interactive dialogue, routing, and other latency-sensitive tasks, although its actual roleplaying quality still needs testing.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://www.inceptionlabs.ai\&sz=32)

  Inception

  +1



The central recommendation is to separate AI quality selection from inference infrastructure selection.

A model might be excellent at character reasoning, but another company could provide the best infrastructure for running that model. IRGS should be able to choose both independently.

## 1. Provider landscape: mainstream and independent developers

I researched model developers separately from companies that host or route their models. The distinction matters because a hosted DeepSeek or Qwen model can have different costs, latency, privacy conditions and availability depending on where IRGS accesses it.

The prices below are USD per million input/output tokens, generally standard uncached API rates. They are not prices for consumer chat subscriptions.

### Mainstream model developers

| Provider  | Models worth evaluating                | Published pricing (input / output) | Potential IRGS role                                                       |
| --------- | -------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------- |
| OpenAI    | GPT-6.1 Sol, GPT-6 Luna, GPT-6 Astra   | $2/$10; $0.10/$0.50; $10/$50       | Director, complex actor decisions, validation, development                |
| Anthropic | Claude Sonnet 5.5, Opus 5.5, Haiku 5.5 | $2/$10; $4/$20; $0.10/$0.50        | Characterization, dialogue, narration, critical reasoning                 |
| Google    | Gemini 4 Argon, Gemini 3.8 Flash       | $2/$10; $0.75/$3.75                | World reasoning, long-context work, strategic and institutional decisions |
| xAI       | Grok 4.6                               | $2/$6                              | Alternative reasoning, character and dialogue evaluation                  |
| Meta      | Llama and other open-weight models     | Host-dependent                     | Self-hosting and specialized lower-cost workers                           |

Prices and model capabilities checked against provider documentation. Gemini 4 Argon's $2/$10 introductory price is scheduled to increase after November 30, 2026; Gemini 3.8 Flash's $0.75/$3.75 promotional pricing runs through December 2026.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://developers.openai.com\&sz=32)

OpenAI API

+4

OpenAI and Anthropic are strong initial candidates for the most demanding parts of the player-facing experience. Google's models deserve substantial evaluation for reasoning over large institutional and world contexts. None has yet demonstrated superiority on IRGS-specific long-form character fidelity or persistent-world tests.

### Independent and less-mainstream model developers

| Provider       | Candidate                             | Published pricing (input / output)     | Reason to test                                            |
| -------------- | ------------------------------------- | -------------------------------------- | --------------------------------------------------------- |
| DeepSeek       | V4.1 Flash                            | $0.15/$0.60 off-peak; $0.30/$1.20 peak | Cheap reasoning, autonomous actors, structured actions    |
| Mistral AI     | Small 4                               | $0.15/$0.60                            | General-purpose tasks, dialogue, open-weight deployment   |
| Mistral AI     | Large 3                               | $0.50/$1.50                            | Affordable narrative and language generation              |
| Inception Labs | Mercury 3                             | $0.10/$0.35 introductory               | Very fast conversational output and specialized workers   |
| Z.ai           | GLM-5.3 Flash                         | $0.15/$0.50                            | Low-cost structured tasks and agent work                  |
| Z.ai           | GLM-5.1                               | $1.40/$4.40                            | Complex planning and technical tasks                      |
| MiniMax        | M2.7                                  | $0.30/$1.20                            | Agentic workflows, coding and general reasoning           |
| Moonshot AI    | Kimi K3                               | $3/$15                                 | Complex long-context reasoning and independent evaluation |
| Alibaba Cloud  | Qwen 3.8 family                       | Regional or host-dependent             | Adaptable open-weight models and possible self-hosting    |
| Cohere         | Command / Command R, reranking models | Task/model-dependent                   | Retrieval, semantic search and knowledge organization     |

Pricing from direct-provider documentation; Mercury 3 promotional pricing may expire. Qwen's Alibaba Cloud regional billing includes CNY-denominated schedules, so an unverified USD equivalent is intentionally omitted.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://api-docs.deepseek.com\&sz=32)

DeepSeek API Docs

+7

### Three smaller providers deserve particular attention

[AJAIA | AI Strategy, Engineering & Enterprise Enablement](https://images.openai.com/static-rsc-4/AA-yFCNyqZnhg04SmBjsuwjnPQ0ARUDYH-RWxmbl7--NZO5rcXUC7REZL2ptYmvv0BWtiODfQIjA4ay2DDAsONz8wuG4x0l4QxJea44kSsE-DuJKP3NKp-8PXrQvMQqhZhxQ1VLpKvZKwbOteEhLJA7BSZdDA_VfeJf_KZNeufA?purpose=inline)

Mistral AI — Best open-model candidate for initial experimentation

Mistral Small 4 provides tool calling, structured output and reasoning capabilities, with weights released under Apache 2.0. Large 3 is attractively priced for evaluating narrative tasks. Small 4 is also customizable, although running its full weights still requires substantial GPU resources.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://mistral.ai\&sz=32)

Mistral AI

+2



[DeepSeek AI - Guidance for Safe Use | Staff Gateway](https://images.openai.com/static-rsc-4/PmzUdcH1NRFQS50s3q_fRh5sUveTYu38a_vH3GnMZqyv_smXqhc8oko6w8F58qMAMpcN9y1YI2K9cn3b_okSuxjvBMZt0qB_yaB8BqaW0zjQFO1X6XqfBJtaMDd_VDY4UCan8HX7632smW3YTRMI0tDL9sB-dPK3JVJzPrlMKqg?purpose=inline)

DeepSeek — Strong candidate for economical world intelligence

V4.1 Flash supports tool calling, JSON output and up to one million tokens of context. Its released weights use the MIT license. I would test it on off-screen NPC decisions, organizational deliberation and campaign-state interpretation. Direct API privacy conditions must be reviewed before sending private creator content or player data.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://api-docs.deepseek.com\&sz=32)

DeepSeek API Docs

+1



[Inception Labs Review (2026): Mercury Diffusion LLM](https://images.openai.com/static-rsc-4/h6M8Ea2yYOvrHUJmgq5zVio1fBKODHqNHBJbOjbTG6-mg2BwTrgy7ZCaa4SLslw7SA_0_PEC-sI18xABMm_RRTeT4JxiJHctHCyfp01SNu7Eu_ckb0WT9EYd43YtU86fJSFJP3Ix0RQgI5EzYieiKFyhnbESKSWMBfHbDOdfw9E?purpose=inline)

Inception Labs — Most interesting speed-focused challenger

Mercury 3 uses diffusion-based text generation and advertises extremely high throughput. It supports tools and structured outputs through available API routes. If its dialogue quality proves suitable, it could reduce delays in multi-agent conversational sequences. However, it is newly released, and vendor speed claims are not a substitute for latency tests with IRGS prompts.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.inceptionlabs.ai\&sz=32)

Inception

+1



I would also keep MiniMax, Qwen, Z.ai, and Kimi in the evaluation pool. They offer useful alternatives for coding, structured reasoning and specialized AI work.

One qualification is important for IRGS's commercial future: open-weight does not always mean unrestricted commercial use. Mistral Small 4's Apache 2.0 license is comparatively straightforward, while some other model families have conditions tied to company revenue, usage or attribution. Kimi K3 and certain Qwen models require particular licensing attention as their commercial scale grows.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://help.mistral.ai\&sz=32)

Mistral Help Center

+2



## 2. Provider access: how IRGS should connect to models

This is separate from deciding which model is best.

There are three useful routes: directly through the model developer, through a multi-model gateway, or through an inference host operating open-weight models.

### Gateway and inference-platform comparison

| Platform                                                                  | Primary benefit                                                    | Recommended place in IRGS                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| [BLACKBOX Router](https://www.blackbox.ai/api?utm_source=chatgpt.com)     | Hundreds of models, unified API, routing and enterprise inference  | Gateway contender; multi-agent engineering  |
| [OpenRouter](https://openrouter.ai/?utm_source=chatgpt.com)               | Very broad model discovery, provider selection and privacy filters | Initial benchmarking gateway                |
| [Vercel AI Gateway](https://vercel.com/ai-gateway?utm_source=chatgpt.com) | No advertised token markup, model fallback, unified billing        | Strong production gateway candidate         |
| [DeepInfra](https://deepinfra.com/?utm_source=chatgpt.com)                | Low-priced open-weight inference and dedicated infrastructure      | Economical routine AI workloads             |
| [Fireworks AI](https://fireworks.ai/?utm_source=chatgpt.com)              | Serverless inference, model fine-tuning and dedicated deployment   | Production scaling and specialized models   |
| [GroqCloud](https://console.groq.com/?utm_source=chatgpt.com)             | High-throughput inference for supported models                     | Low-latency tasks and streaming             |
| [Cerebras](https://www.cerebras.ai/?utm_source=chatgpt.com)               | Specialized accelerated inference                                  | Benchmark for speed-sensitive models        |
| [Together AI](https://www.together.ai/?utm_source=chatgpt.com)            | Open-model hosting and customization                               | Alternative inference and training platform |

BLACKBOX currently advertises more than 300 models behind an OpenAI-compatible endpoint, with routing and enterprise options. OpenRouter offers more than 500 models and extensive provider-choice controls. Vercel advertises no markup on inference prices, while DeepInfra and Fireworks offer competitively priced hosted open models.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.blackbox.ai\&sz=32)

Blackbox

+4



### My preferred access pattern

IRGS Core + Intelligence Director

Owns routing decisions, knowledge permissions, workflow authority, budgets and validated state

IRGS Provider Abstraction

Standardized prompts, tool schemas, model registry, telemetry, fallback and security policy

Direct APIs

OpenAI, Anthropic, Google

Gateway APIs

Vercel, OpenRouter, BLACKBOX

Open inference

DeepInfra, Fireworks, Groq, later self-hosted

Specialized IRGS Intelligence Roles

Character intent, dialogue, narrative, strategic reasoning, memory and other specialized functions

This allows IRGS to select not only which model should perform a task, but also where it should run.

A DeepSeek model might be accessed directly during testing, through DeepInfra during ordinary operation, and eventually through privately controlled infrastructure without redesigning the agent.

### My gateway ranking for IRGS

1\. Vercel AI Gateway — preferred initial production contender. Its published lack of inference markup, explicit fallback configuration, routing controls and TypeScript ecosystem make it attractive for a web-first product. This preference depends on the mock website's actual technology and whether its privacy and API compatibility satisfy IRGS.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://vercel.com\&sz=32)

Vercel

+1



2\. OpenRouter — preferred research and model-discovery gateway. Its catalogue and provider controls make it particularly useful for evaluating many smaller model developers. Standard paid accounts charge a 5.5% fee when purchasing credits, while certain bring-your-own-key usage can avoid fees within specified limits.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://openrouter.ai\&sz=32)

OpenRouter

+1



3\. BLACKBOX — preferred additional evaluation for multi-agent engineering. Its Router is a credible production candidate, particularly if its pricing, enterprise isolation and model availability offer an advantage. I would not add it as another obligatory hop in front of an existing gateway.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.blackbox.ai\&sz=32)

Blackbox

+1



4\. Direct APIs — essential regardless of the winner. Keep direct integrations for the most important models so IRGS is not dependent on one gateway operator.

For the initial research stage, I would avoid buying enterprise contracts or committing to several subscription products. API access with small usage budgets is enough to establish comparative performance.

## 3. Optimal model assignments within IRGS

I would not assign all twelve of the previously proposed AI specialists to separate paid model calls.

Instead, I would maintain twelve logical specialist responsibilities, with a task router that can combine them when appropriate, execute them independently when necessary, and escalate difficult work.

The following is my proposed initial model-selection matrix.

| IRGS function           | Primary candidate             | Alternatives / challengers               |
| ----------------------- | ----------------------------- | ---------------------------------------- |
| AI Director             | GPT-6.1 Sol                   | Gemini 4 Argon, GLM-5.1                  |
| Character Intelligence  | Claude Sonnet 5.5             | Claude Opus 5.5, GPT-6.1 Sol, Grok 4.6   |
| Dialogue Intelligence   | Claude Sonnet 5.5             | Mistral Large 3, Mercury 3, MiniMax M2.7 |
| Narrative Intelligence  | Claude Sonnet 5.5             | Mistral Large 3, Kimi K3, GPT-6.1 Sol    |
| Scene Director          | GPT-6.1 Sol                   | Claude Sonnet 5.5, GLM-5.1               |
| Social Intelligence     | Claude Sonnet 5.5             | Claude Opus 5.5, GPT-6.1 Sol             |
| Strategic Intelligence  | Gemini 4 Argon                | GPT-6.1 Sol, GLM-5.1, Kimi K3            |
| World Intelligence      | DeepSeek V4.1 Flash           | Gemini 3.8 Flash, Mistral Small 4        |
| Knowledge Intelligence  | Retrieval + reranking         | Cohere, GPT-6 Luna, Gemini 3.8 Flash     |
| Memory Intelligence     | GPT-6 Luna                    | GLM-5.3 Flash, DeepSeek V4.1 Flash       |
| Continuity Intelligence | GPT-6.1 Sol                   | Claude Sonnet 5.5, Gemini 4 Argon        |
| Rules Intelligence      | Core validators + GPT-6.1 Sol | Gemini 3.8 Flash, GLM-5.1                |

These are testing assignments, not demonstrated winners. In particular, Claude is a strong hypothesis for character writing, but Mistral, MiniMax and Inception should receive the same objective tests. A cheaper model could outperform a flagship model on the narrow writing task IRGS actually needs.

### The key separation: Character Intelligence and expression

Your earlier requirement remains central.

The model determining what Sir Richard Wycliffe intends need not be the model writing his dialogue.

Character Intelligence would produce a structured intention, such as:

> Richard refuses independent command, offers supervised reconnaissance, and intends to correct Ian without publicly humiliating him.

Dialogue Intelligence converts that into appropriate speech. Narrative Intelligence describes visible behaviour and circumstances.

Continuity Intelligence verifies that the words and description have not changed the decision.

In a simple exchange, a single capable model might safely perform characterization and dialogue together. In a major political conversation, the Director should separate the two and validate their outputs independently.

This is how IRGS can retain sophisticated characterization without imposing an expensive multi-agent workflow on every minor interaction.

## 4. Actual AI usage: when each level should activate

I recommend four operating levels, selected according to simulation complexity rather than the customer's purchased access tier.

Level A — Routine interaction

Buying food, asking for directions, ordinary greetings, basic environmental descriptions.

A lightweight model handles the interaction using known NPC information. No expensive strategic or world deliberation is required.

Level B — Meaningful character interaction

Important conversations, relationships, professional negotiations, disagreements and personal decisions.

Character Intelligence determines intentions. Dialogue and Narrative Intelligence express them. Relevant validation ensures consistency.

Level C — Consequential simulation

Command decisions, institutional disputes, military operations, diplomatic negotiations, substantial economic projects.

Activate specialized reasoning, knowledge retrieval, Character Intelligence and mechanical validation according to the dependencies.

Level D — Large-scale autonomous simulation

Civilizational development, long-term institutional evolution, multiple connected regions, historical transitions and major geopolitical decisions.

Use bounded specialist reasoning and deterministic processing, including deferred calculations where appropriate. Complex character decisions can be evaluated individually without generating continuous prose for every actor.

The Director must assess which operations are genuinely required, not merely whether the situation sounds dramatic.

For example, if a thousand people relocate between two settlements, the Core can update aggregate population and logistics records. It does not need a thousand separate AI conversations.

If one of those individuals is a significant political leader deciding whether to flee, that decision may justify specialized character reasoning.

Simulation detail and AI inference volume must not be treated as the same thing.

## 5. What the costs actually look like

The inexpensive models are especially relevant to IRGS's permanent-purchase business model.

The following comparison assumes one API call with 10,000 uncached input tokens and 1,000 output tokens, repeated 100 times.

| Model                         | Estimated cost for 100 calls |
| ----------------------------- | ---------------------------- |
| Mercury 3, introductory rate  | $0.14                        |
| GPT-6 Luna                    | $0.15                        |
| GLM-5.3 Flash                 | $0.20                        |
| Mistral Small 4               | $0.21                        |
| DeepSeek V4.1 Flash, off-peak | $0.21                        |
| Mistral Large 3               | $0.65                        |
| GPT-6.1 Sol                   | $3.00                        |
| Claude Sonnet 5.5             | $3.00                        |
| Kimi K3                       | $4.50                        |

Illustrative USD calculation from published rates, not measured gameplay costs. Excludes additional model calls, hidden reasoning-token consumption, caching variations, tool fees, retries and other infrastructure expenses.

The point is not that IRGS should always choose the cheapest model. It is that a well-designed routing policy could provide sophisticated intelligence when needed while avoiding premium inference on tasks that do not benefit from it.

### Example blended interaction

Consider a consequential conversation using:

| Operation                | Model             | Illustrative tokens | Estimated cost |
| ------------------------ | ----------------- | ------------------- | -------------- |
| Director routing         | GPT-6 Luna        | 1,500 in / 150 out  | $0.00023       |
| Character decision       | GPT-6.1 Sol       | 4,000 in / 400 out  | $0.01200       |
| Dialogue                 | Claude Sonnet 5.5 | 2,000 in / 500 out  | $0.00900       |
| Narration                | Mistral Large 3   | 3,000 in / 700 out  | $0.00255       |
| Supporting state summary | GLM-5.3 Flash     | 2,000 in / 200 out  | $0.00040       |
| Total                    |                   |                     | $0.02418       |

At this hypothetical workload, 100 interactions would cost about $2.42 in model inference.

This is not a production forecast. Real interactions could require fewer calls, substantially more context, more reasoning, or additional validation.

It does show why I would focus on optimizing cost per correctly completed player interaction, not merely input/output token prices.

An inexpensive model that requires three retries can be less economical than a more capable model that succeeds immediately.

## 6. Open-weight and privately operated AI

For the long-term commercial platform, I would also maintain an open-model strategy.

The strongest potential advantage is operational control.

IRGS could eventually operate specialized AI workloads on infrastructure it controls, subject to licenses and hosting costs.

[NVIDIA DGX H200: 8 GPUs para Cloud e Data Center IA](https://images.openai.com/static-rsc-4/VUupFxW9ObqMmypKmbGSw99f4i016qHJBo8Nd8FfE2NMnpAVYYjjc_KISWQI5PIv_9m4dyXcugJcgfXiFxzlVn7HG8SaS9i_BJiGfWVBBamnMXuzv2nfj6Ytj-xKdBlX4o2dm5hn6o-aBzBJ6NBH5z6kxsgh8moxIT8KH_GVK2I?purpose=inline)

Dedicated inference hosting

Providers such as Fireworks and DeepInfra can host supported open-weight models using reserved or dedicated compute resources.

[AI Power Workstation - AMD Ryzen Threadripper PRO 9985WX 64C/128T, 2x NVIDIA RTX Pro 6000 Blackwell 96GB, 512GB DDR5 5600MHz ECC RAM, 2TB Gen5 SSD, 2200W PSU, 360mm Liquid Cooler Buy, Best Price in UAE, Dubai, Abu Dhabi, Sharjah](https://images.openai.com/static-rsc-4/6Nl7rWgQrQxFhd5w9ZmiOo-QVKrUeFxbWSj3Pc772Q0YN93uPs6IvFs3m_hHFAdMLhEFkjxwilTnZ-PHvz3uXmBgh0Qr2a6ZWuChHDhJZ2VxzVCVh85rZ4bYoRzxvzF6q32g3jE0mgiuoWsQIo6Bx1qQHsRjElbsWSFQqgoaDuU?purpose=inline)

Self-managed deployment

Tools such as NVIDIA NIM, vLLM and other compatible serving frameworks provide routes to independently operated model inference.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.nvidia.com\&sz=32)

NVIDIA NIM for LLM and VLM

+1



I would initially experiment with smaller models such as appropriately licensed Qwen variants, GPT-OSS, or Mistral-family models.

A hosted Qwen 27B-class model is especially interesting for economical specialist tasks, though its quality would need independent testing.

Large open-weight models are not automatically cheap to self-host. DeepSeek V4.1 Flash, despite its efficient inference architecture, has hundreds of billions of total parameters. Likewise, Mistral Small 4 is not a modest consumer-hardware deployment at full precision.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

Hugging Face

+1



I would move a workload to dedicated hosting only when measured volume, hardware utilization, licensing and support costs justify it.

### Avoid premature fine-tuning

The existing Character Intelligence architecture should first be built from structured character records and reliably retrieved memories.

Fine-tuning might later help establish a consistent dialogue style or compact specialist decision format, but it should not be the primary means of storing mutable campaign state.

A model's weights should not be responsible for remembering that a particular merchant currently owns seventeen sacks of grain.

That belongs in IRGS.

## 7. Security, privacy and intellectual-property requirements

Because IRGS intends to acquire published creator content, protect player campaigns, and develop proprietary simulation infrastructure, model-provider terms matter.

The model registry should record:

| Property             | Required evaluation                                                       |
| -------------------- | ------------------------------------------------------------------------- |
| Data retention       | Whether prompts or responses are stored and for how long                  |
| Training use         | Whether submitted data can be used to train provider models               |
| Processing geography | Where requests may be processed and stored                                |
| Commercial licensing | Restrictions on operating a commercial game                               |
| Output rights        | Rights and contractual restrictions applicable to generated material      |
| Reliability          | Availability, rate limits and failure behaviour                           |
| Model stability      | Version pinning, notice of retirement and migration terms                 |
| Tool capability      | Real support for the structured outputs and tool operations IRGS requires |

A provider advertising zero retention does not mean the entire end-to-end workflow is private. Other gateways, model hosts, application logs or tools may process or retain data. OpenRouter explicitly documents the distinction between zero retention, processing location and data-collection restrictions.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://openrouter.ai\&sz=32)

OpenRouter

+1



I would implement data-access policies by information classification:

Public/reference: reusable publicly distributable historical and setting content.

Restricted: unpublished creator projects and privately authored campaign data.

Confidential: user information, private player records, contractual materials and non-public proprietary IRGS data.

The Director should only send the minimum authorized information needed for a specialist's task.

A model that does not meet the applicable privacy requirements should be excluded from that task, regardless of its quality or cost.

For open-weight models, licenses must be tracked by actual model version—not assumed from the reputation of the model developer.

### A current infrastructure caution

LiteLLM is another possible self-hosted gateway, but recent security reporting identifies vulnerabilities affecting versions before 1.83.9, including access-control and request-routing issues. I would require a patched version, restricted access and security review before considering it for IRGS's production API keys.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.techradar.com\&sz=32)

TechRadar

+1



This is another reason to keep provider credentials behind an IRGS-controlled service rather than putting them in the browser or creator-facing Workshop.

## 8. How I would benchmark the providers

IRGS requires a specialized evaluation suite, not a generic benchmark leaderboard.

I would establish a reproducible test programme using the first text-based vertical slice and known campaign data.

| Test domain            | Example                                                 | Primary measure                                    |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------------- |
| Character fidelity     | Richard Wycliffe responds to an unexpected request      | Intent consistent with character profile           |
| Dialogue               | Several characters communicate the same basic message   | Distinct and appropriate voices                    |
| Social simulation      | A subordinate challenges established authority          | Plausible institutional and interpersonal response |
| Player agency          | Player refuses the expected mission                     | No forced compliance or invented player choices    |
| Knowledge boundaries   | NPC asked about an event they never observed            | No unauthorized knowledge                          |
| Mechanical validity    | Actor attempts an impossible or unaffordable action     | No fabricated capabilities                         |
| Persistent memory      | Character recalls an event after many intervening turns | Accurate retrieval and interpretation              |
| World reasoning        | Multiple settlements experience a supply disruption     | Causally coherent institutional response           |
| Cross-scale simulation | Regional conflict changes local commerce                | Valid consequences without duplicated effects      |
| Narrative delivery     | Describing an important event                           | Clarity, atmosphere, fidelity to resolved state    |
| Runtime efficiency     | Same workload across model hosts                        | Cost, latency, retries and availability            |

For a substantive model decision, I would use repeated test cases, blinded narrative comparisons where practical, and longer multi-turn simulations.

The registry should store model versions, prompts, input state, outputs, validity scores, latency and actual cost.

I would use a scoring framework that treats mechanical or agency violations as hard failures, not merely small deductions from prose-quality scores.

A model that writes beautiful dialogue but repeatedly invents player actions cannot be selected as the authoritative narration specialist.

## 9. Recommended deployment stages

## 1

Playable website — immediate

Connect the existing IRGS Core to an initial provider, preferably OpenAI GPT-6.1 Sol, with direct API support.

Establish structured action requests, real state validation, narrative delivery, persistence, and agent-cost logging.

Add a second model only after the basic gameplay loop works.

## 2

Multi-provider evaluation

Add Anthropic direct access, a multi-model gateway, and selected open-weight inference.

Test character, dialogue and narrative specialists separately, alongside DeepSeek, Mistral, Mercury and other relevant challengers.

Begin selecting defaults from measured results.

## 3

Production routing

Introduce conditional specialist invocation, provider failover, caching, per-task budgets and independent validation.

Ensure that gameplay access tiers do not change intelligence quality or available mechanics.

## 4

Commercial scaling and Workshop integration

Extend provider budgets and access controls to Workshop AI assistance, creator-content validation, marketplace packaging and autonomous world simulation.

Evaluate dedicated inference and private model deployment once measured demand justifies the expense.

## 10. What I would authorize Codex to implement

I would add the following requirements to the existing Codex master specification, without replacing its current gameplay-first priorities.

| Component               | Implementation requirement                                                               |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| Provider Registry       | Registered model, provider, version, capabilities, rate card, security policy and status |
| Provider Adapter        | Standardized interface for direct, gateway and hosted-model inference                    |
| Specialist Registry     | Maps IRGS responsibilities to tested models and fallback candidates                      |
| Task Router             | Selects models by required capability, state permissions, quality threshold and budget   |
| Response Validator      | Verifies schemas, intentions, knowledge boundaries and Core constraints                  |
| AI Usage Ledger         | Actual model calls, input/output tokens, cost, latency, errors and retries               |
| Evaluation Harness      | Reproducible IRGS-specific tests and comparative performance records                     |
| Model Migration Control | Controlled changes to providers/models without changing campaign state                   |
| Access Policy           | Restricts which information can reach each provider and specialist                       |

The rollout must not rely on automatic unrestricted model selection. Every provider and model needs explicit approval for the workloads it may process.

I would also require routing logs that identify both the requested model and the model actually used, since gateway fallback may change the provider handling a request.

## 11. Recommended initial provider access

Here is the concrete starting configuration I would establish.

Initial IRGS AI stack

Recommended

| OpenAI API                      | Primary functional integration and Director testing. GPT-6.1 Sol and Luna.             |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| Anthropic API                   | Independent characterization, dialogue and narration evaluation.                       |
| Vercel AI Gateway or OpenRouter | One initial multi-model access point for broad comparison and fallback experiments.    |
| DeepInfra                       | Economical open-model inference when advantageous versus gateway or developer pricing. |
| BLACKBOX                        | Evaluate separately for multi-agent coding and as a competing gateway.                 |

Selection is provisional pending IRGS benchmarking, legal terms, privacy review and comparison with the website's actual technology stack.

I would not activate recurring paid subscriptions to all these services. Start with the necessary API accounts and tightly bounded usage budgets; expand only when evidence supports the additional dependency.

### Final provider assessment

My current shortlist for the highest-impact IRGS gameplay roles is:

- Character minds: Anthropic Claude Sonnet 5.5 versus OpenAI GPT-6.1 Sol, with other candidates tested independently.
- Dialogue and prose: Claude Sonnet 5.5 versus Mistral Large 3 and Mercury 3.
- World and institutional reasoning: Gemini 4 Argon versus GPT-6.1 Sol and DeepSeek V4.1 Flash.
- Routine memory and supporting work: GPT-6 Luna, GLM-5.3 Flash, Mistral Small 4 and DeepSeek V4.1 Flash.
- Provider infrastructure: Vercel AI Gateway, OpenRouter and BLACKBOX evaluated on cost, reliability and compatibility rather than adopting all three.

These selections remain research recommendations, not adopted engine assignments or experimentally proven rankings.

The wider conclusion is that IRGS does not need to choose between premium AI quality and inexpensive inference. It needs a system capable of intelligently combining them.

The long-term competitive advantage should belong to IRGS's own Core, AI Director, persistent character cognition, knowledge controls and specialist evaluation system—not to any particular provider.

That arrangement would allow IRGS to take advantage of improvements from established AI laboratories, emerging independent developers and future private inference technologies without rebuilding its simulation platform each time the market changes.