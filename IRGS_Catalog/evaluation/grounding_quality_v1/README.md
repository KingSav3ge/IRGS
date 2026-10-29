# Grounding and quality evaluation v1

Actor-facing fictional instructions and evaluator-only requirements are stored
separately. This rubric evaluates evidence; it grants no action, world fact,
provider permission or Alpha qualification. The published Engine
`solo-proposal-1` contract exposes actor ID, exact intention, received context,
allowed action IDs and received source references to a selected provider. Its
schema and reference checks do not establish semantic intent agreement. The
player explicitly reviews a proposal; only the actual committed receipt and
actor-legitimate outcome establish effects. Testimony is not established truth,
consent, autonomous NPC response or a transfer. A missing duration is unknown.

Evaluate eight dimensions individually: legitimate input scope; source status and
uncertainty; intent-to-action semantic agreement; proposal versus committed
effect; receipt fidelity; hidden-information leakage; meaningful NPC response;
and narration quality. A reviewer must identify the exact submitted material,
relevant actor-visible sources and committed receipt and cite evidence for every
judgment. Pass/fail/unknown are distinct; absence of a supported NPC response is
unknown, never a pass. Adversarial examples include a valid but semantically wrong
action, testimony represented as fact, a proposal claimed as an effect, leaked
private information, and a failed action narrated as success.

`grounding_quality.assess_proposal`, `grounding_quality.assess_receipt` and `grounding_quality.assess_review` implements a conservative deterministic check for
exact intent, allowed actions and source references, receipt identity, literal
committed summary and explicit per-dimension reviewer judgments. It cannot infer
semantics, truth, privacy or quality from free text and never establishes live AI
quality. Reviewer judgments are recorded claims, not independently certified by
the checker. An incomplete review remains unqualified. Structured violations fail
regardless of judgments. Synthetic transports, local rendering, and a real live
provider are separate categories of evidence. No live model call is authorized by
this fixture.

The ordinary-context consumer selects Engine
`296e46a1beed10d0ebf2841f133bb52fade83697`, App
`7e1a5929b2f30479aa315789f75bfa6c46761438`, and Catalog baseline
`e97d87f0d17a16dbe0ce186badafe663188321a1`. These match the App's committed
pins; this new Catalog candidate is explicitly selected for evaluation. The test
creates real synthetic worlds through App HTTP, reviews and accepts testimony,
checks structured committed outcomes and zero routine provider calls. A separate
in-process fake transport proposes actions in both ordinarily created contexts;
the rubric checks actor-visible action/source bindings and explicit reviewer
judgment, then acceptance checks actual locations, elapsed time and original
receipt recovery. Fake transport is not a live provider. It does not claim actual
model narration or complete sustained Alpha play. See root evidence.
