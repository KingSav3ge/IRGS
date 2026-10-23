# IRGS Engine model

IRGS is designed around a continuing world. People, households, businesses, governments and military organizations share resources, commitments and history. The Engine connects decisions at those scales through the same world state and established Core owners.

This overview explains the design in IRGS terms. Selected Core 3.3 supplies the executable foundation; the applied C2 specification includes requirements that still need implementation and qualification. The principles below do not expand a campaign's selected rules.

## One world across scales

A person working for a business and serving a military organization is the same person in both contexts. Their available time, equipment and obligations constrain both activities. Institutional planners propose operations against that shared state. They gain no separate stock, workforce or history by having their own planning view.

Existing Core owners retain authority over their domains. Genre adapters supply supported domain procedures; content libraries supply definitions and references. Neither creates a second world or grants resources through lookup.

## Action through actual authority

An intention records what someone wants to attempt. Authorization establishes what they can direct. Execution checks the relevant state and applies supported effects; the resulting record supports later presentation. These are distinct steps.

For example, requesting equipment requires the applicable authority and actual available stock. An accepted transfer changes custody through Core. A draft suggestion or a freeform request alone transfers nothing. Supported equipment operations and the general declaration interface have different implementation scopes: freeform gameplay currently returns `declared_not_resolved`.

## Resources and commitments have consequences

Work, transfers, payments and institutional decisions must use actual people, stock, funds and shared capacity. A planned activity is a commitment; completed work requires its own supported effects. Rejection must preserve atomicity, and a retry must recover an accepted result without repeating its effects.

The runtime contains bounded economic, strategic and recovery handlers with synthetic verification. Their supported operations do not establish a complete economy or universal production and wage rules. New procedures need explicit inputs, authority, resource accounting and evidence of their effects within the selected campaign.

## Information shapes decisions

Characters and institutions act on information they can legitimately receive. A known identity does not reveal private possessions or current plans. Testimony remains testimony, an offer remains an offer, and an obligation remains distinct from its fulfillment.

Player views draw from committed effects and permitted records. Institutional observations constrain planning before a proposed operation is validated against actual state. The interface can offer contextual intentions alongside an editable response without exposing hidden facts or promising success.

## Time and continuity remain explicit

Storage revision, causal sequence, elapsed world time, civil date and information time have separate meanings. Redisplaying a result or retrying an accepted request performs no additional work. A proposed action supplies no default duration merely by being submitted.

C2 specifies staged processes, interruption and recovery in greater detail. Those requirements need their own implementation evidence. The ordinary freeform gameplay loop currently records declarations without automatically advancing the calendar or resolving outcomes.

## History supplies a starting world

A new historical playthrough starts from a verified dated snapshot. Continuing play uses the actual committed world, including changed existence, leadership, relationships and control. Historical references provide context and conditional expectations; they do not force later events or reset changed state.

Source archives retain their original assertions, qualifications and attribution. Reading research creates no campaign fact, resource, character knowledge or scheduled event. Adopting a source concept requires an explicit IRGS rule and verification within its intended scope.

## Refining a system

Describe a proposed refinement by answering these questions:

1. Who acts, and what authority and received information support the decision?
2. Which existing Core owners validate and commit the effects?
3. What resources, commitments and elapsed work constrain the attempt?
4. What changes on acceptance, rejection, interruption and retry?
5. What can each participant subsequently know, and what evidence verifies that behavior?

These answers define the mechanic. Familiar concepts such as succession, trade, production and military command can be developed through these contracts, with names chosen to communicate what IRGS actually represents. Source terminology remains appropriate in attributed research records; current Engine explanations should describe their own behavior directly.

## Implementation references

- [Core 3.3 release scope](../IRGS_3_3/SUITE_RELEASE.md) describes supported behavior and operational limits.
- [Applied Engine specification](Core/IRGS_Core_3_3_3_E_C2.md) reconciles the inherited Core with C2 requirements.
- [C1/C2 incorporation register](C1_C2_INCORPORATION.md) distinguishes foundations, partial coverage and missing implementation.
- [C2 contracts and acceptance inventory](design/C2/README.md) define the required implementation evidence; their 121 cases are requirements, not a claim that all have passed.
