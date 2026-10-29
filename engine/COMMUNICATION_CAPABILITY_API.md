# Selected communication capabilities — API 1

IRGS 3.4.1 development; Core compatibility 3.3. Import `communication_contract`
from the Engine runtime. Schema: `irgs-communication-capabilities-1`. It needs no
App/Catalog checkout, API token or provider. The existing Core
`execute_local_communication` handler owns speech, evidence, obligations and
conserved transfers. This interface creates no NPC decision or new channel rule.

| API | Returned contract |
| --- | --- |
| `actor_view(world, actor, branch_id=..., restore_id=...)` | Selected local channels, participants attributed in received evidence, received offer status/commands, bounded sources, editable own-response field and actor/branch/restore snapshot. Also available as `shared_runtime.actor_view(...)["communications"]`. |
| `received_sources(world, actor, limit=64)` | Detached exact evidence text, status, originator, evidence source and reception source, recorded/received causal times and original occurrence-time value. Maximum limit 128; total/truncation explicit. |
| `offer_status(world, actor, offer_id, branch_id=..., restore_id=...)` | Original received public terms/digest, proposal sources/time, latest received status/source/time and role-dependent command attempts. Never reads live obligations. |
| `received_communication(world, actor, request_id, branch_id=..., restore_id=...)` | Original immutable received communication, exact words as testimony, public terms if actually delivered, shared committed receipt and local presentation. |
| `prepare(...)` | Existing immutable native `CommunicationRequest`; exact edited words and independently chosen structured command, participant, channel, source and private scope. No effects. |
| `execute(world, request, current_scope=..., persist=..., explicitly_accepted=True)` | Existing observed Core execution with mandatory host CAS and a sanitized public result. `CommunicationUnavailable.code` is public; any `.dependencies` is host-private. |

The host authenticates the current actor, serializes campaign writers, supplies
actual branch/restore identity and retains pending native JSON privately.
Caller-supplied scope, evidence references, words or terms grant no authority.
Plain text must be escaped at the display surface. Private state/parameter/rule
digests, dependency certificates, raw obligations, mandates and saves are absent
from the public contracts. A terms digest binds the exact already received
public terms and is intentionally public.

## Participants and sources

Only reviewed `communication_rules` selecting the existing co-located channel
and causal-only time model expose a channel. Its raw actor roster is never
published. Participant IDs must occur in the actor's received attribution or
actually received participant communication, and belong to the selected channel.
The interface never parses a name from prose, looks up a hidden actor name or
whereabouts, or invents an introduction to populate a menu. A received attribution
can be uncertain or out of date; it establishes no current presence or authority.
An empty participant list is an honest possible result.

`speak` is supported for these selected channels. New `offer` and `counteroffer`
commands additionally require the existing Rise `settlement_free_stock` profile.
No mandate IDs, stock accounts or quantities are discovered from hidden world
state. The player/host supplies explicit terms from legitimate information; Core
validates them. Availability means **attemptable**, with explicit submission;
hidden stock, seed/work reservations, permissions and remote locations do not
select a winning menu. Current existence, control, co-location, policy and custody
checks remain in the actual Core handler and its R9-observed rejection paths.

Forwarding speech evidence delivers its exact words, original attribution/status
and reception provenance. It does **not** deliver the private structured offer or
original audience. This boundary is also enforced in existing native
`received`/`presentation`, compatibility rendering and shared committed receipts.
Actual original participants retain their existing receipts. There is no new
rule for forwarding contracts or granting another participant's rights.

## Commands, meaning and execution

The structured details remain those of the
[native communication API](CONTINUATION_COMMUNICATION_API.md):

| Command | Details and meaning |
| --- | --- |
| `speak` | `{}`. Exact words are testimony; words of acceptance create no transfer or acceptance. |
| `offer` | `offer_id`, `terms` containing `from`, `to`, `material`, positive integer `quantity`, `authority_id`. Proposes an actual selected transfer; no stock feasibility check, booking or payment. |
| `accept` | Received `offer_id`, exact public `terms_digest`. Recipient explicitly attempts the actual current custody/stock transfer; success is `fulfilled` in the same transaction. |
| `decline` | Same ID/digest, original recipient only. Records `declined`; no transfer. |
| `withdraw` | Same ID/digest, original offerer only. Records `withdrawn`; no transfer. |
| `counteroffer` | New `offer_id`, explicit reverse-direction `terms`, received original ID as `counter_to`. Proposes a new offer and records the original as `superseded`; accepts neither. |

Only an actor's last received `offered` status advertises role-dependent closure
attempts. `declined`, `withdrawn`, `superseded` and `fulfilled` remain distinct
terminal meanings with no further closure command. A live change unseen by the
actor cannot change the menu or status. A subsequent attempted command may be
rejected by Core without publishing the hidden reason. Receipt retrieval keeps
the original status: a proposal receipt still says `offered` after fulfillment.
The separate offer view follows the actor's actual received communications.

```python
import communication_contract as communication
from runtime_contracts import WorldScope

request = communication.prepare(world,
    request_id=unique_submission_id, actor=current_authenticated_actor,
    recipient=selected_received_participant, channel_id=selected_channel,
    command="speak", details={}, intention=exact_edited_words,
    source_ref=host_submission_source, branch_id=branch_id, restore_id=restore_id)
# Persist request.to_json() in the host's private pending store for recovery.
result = communication.execute(world, request,
    current_scope=WorldScope(world.s["campaign_id"], branch_id, restore_id, world.checksum()),
    persist=host_atomic_compare_and_save, explicitly_accepted=True)
```

`persist(expected_scope, candidate_save, public_result)` must atomically compare
campaign/branch/restore/state and durably save world plus result, or raise.
The persisted public DTO equals the successful acknowledgment. In-memory Core
publication follows persistence. Failed saves leave the original world unchanged.
After a lost acknowledgment, reload the actual saved world and deserialize the
original native pending request; replay returns the same receipt without another
effect or save. Changed payloads reject. New requests use current state; restores
rotate identity even when save bytes match. Authentication, cross-process writer
coordination and production durability remain host responsibilities.

The interface rechecks the actor and selected participant/channel/received
command for new attempts. Native execution rechecks actual Core authority/rules
and resources. No API authorizes a recipient/NPC choice from generated prose.
Speech records causal sequence, with `elapsed_status: not_resolved`; there is no
invented universal speech duration. Missing text preserves the exact literal
receipt without a provider fallback. Both existing response libraries retain
their original bytes and identities.

## Optional reviewed founder-offer selection — 29 October 2026

A new explicit fictional R00 option selects a scoped household-offer mandate;
its authority covers the communication handler and `founder-home`, not raw
stock-transfer decisions. The existing `transfer_stock` mandates remain
compatible. Proposal, acceptance, actual custody and resource checks retain their
separate native semantics. See [selection, limits and evidence](OFFER_AND_DRAFT_EXTENSION.md).

## Qualification and dependencies

Run `python -B tools/qualify_communication_capabilities.py`; use `--output` to
write [the execution record](COMMUNICATION_CAPABILITY_VALIDATION.json).
Its 32 tests block provider transports and socket connections and use temporary
synthetic saves. They exercise actual non-Rise quay speech and Rise offers,
information boundaries, exact terms/status meanings, current authority rejection,
late rollback, both scarcity frontier orders, host failure/concurrency, native
pending JSON restart, lost acknowledgment, stale state and restore fencing.

Executed delivery checks on 26 October: full standalone policy suite **740 run,
739 pass, one explicit private-save skip**; shared qualification **35 pass**;
phase qualification **28 pass**; combined new/native communication and offline
response regression **62 pass**; original pinned Catalog R00 **10 pass**. Engine
integrity verifies **364 source files**, Kira canon passes, and active
local documentation links resolve. The dedicated 32 cases are included in the
full suite and the 62-case regression; these counts are not additive.

[Current component evidence](COMMUNICATION_COMPONENT_INTERACTION_VALIDATION.json)
passes five Engine-owned HTTP checks against App
`919427cf16cf72574a581d7e6f712e638740a1df` and Catalog
`526404128830a99fe8ea5c2bce43b6ea7d45fe6f`, including actual phase start discovery
and continuation. App shared-response, process, start and current-Catalog suites
run **38 cases, all passing with zero skips**, under explicit Engine/Catalog root
selectors. App's committed Engine pin remains
`aa30bb63a3828cbaeb5ee3d1db57edd388a8dc86`; the new Engine candidate is identified
by its recorded module hashes and delivered commit. No App/Catalog source or pin
was edited or pushed. No new browser or clean-package qualification was run.

App-owned controls/host wiring, compatible dependency pins and coordinator
exact-set browser/package qualification remain separate. No connected
communication UI or new joined release is claimed. Next bounded Engine work is
host-safe selected Rise travel capabilities over its existing native lifecycle;
there is no newly selected return/cancellation rule. General dialogue, NPC
decisions, remote speech, deferred debt, broader DEV/C2 completion, sustained
institutions and live model/human evaluation remain open.
