"""Token-free presentation of actual Core receipts and editable intentions.

Trusted hosts authenticate the actor before calling this API. This module then
checks current control and received records; callers cannot supply outcome facts.
No provider, transport, credential or inference ledger participates in rendering.
Returned text is plain text and must be escaped by the display surface.
"""
from functools import lru_cache
import hashlib
import json

from player_actions import _controlled
from routine_format import compose_recipe, load_library

LIBRARY_ID = 'irgs-engine-routine-responses-v1'
LIBRARY_VERSION = '1.0.0'


@lru_cache(maxsize=1)
def _library():
    # Cache only authored text. Actor/world responses are never shared or cached.
    return load_library()


def _identity(*parts):
    return hashlib.sha256(json.dumps(parts, ensure_ascii=False).encode()).hexdigest()


def _guard(world, actor, scope):
    if not _controlled(world.s, actor):
        raise ValueError('Response unavailable for this actor')
    if scope is not None and (scope.campaign_id != world.s['campaign_id']
                             or scope.state_digest != world.checksum()):
        raise ValueError('Response scope is stale')


def _render(actor, snapshot, recipe, packets, exact, *, seed=0):
    """Format trusted facts; unavailable text never triggers a provider retry."""
    selections = {}
    try:
        library = _library()
        families = {f['id']: f for f in library['families']}
        contexts = {}
        for identity, values in packets.items():
            family = families[identity]
            contexts[identity] = {'actor_id': actor, 'snapshot_id': snapshot,
                'source_ref': 'receipt:' + _identity(snapshot, identity),
                'source_kind': family['source_kind'], 'state': family['state'], 'values': values}
            selections[identity] = int(_identity(actor, snapshot, identity, seed)[:16], 16) % len(family['variants'])
        text = compose_recipe(library, recipe, contexts, variants=selections)
        mode = 'scripted'
    except (OSError, ValueError, KeyError, TypeError):
        # The original authorized receipt is the fallback, never an invented
        # success, a truncated quotation, a new action or a paid narration call.
        text, mode, selections = exact, 'literal_receipt', {}
    return {'mode': mode, 'text': text, 'format': 'plain_text', 'actor_id': actor,
        'snapshot_id': snapshot, 'library_id': LIBRARY_ID, 'library_version': LIBRARY_VERSION,
        'variants': selections, 'render_usage': {'provider_calls': 0, 'model_tokens': 0}}


def receipt_facts(world, actor, event_id, *, scope=None):
    """Read one immutable committed result from this world, scoped to its actor.

    No current stocks/projects are appended to an older receipt. Restored hosts
    supply their actual world; optional scope additionally checks campaign/state.
    Branch/restore authentication and durable result lookup remain host duties.
    """
    _guard(world, actor, scope)
    event = next((e for e in world.s['journal'] if e['id'] == event_id), None)
    if event is None:
        raise ValueError('Response receipt unavailable')
    params, operation = event['params'], event['op']
    snapshot = 'receipt:' + _identity(world.s['campaign_id'], event_id, event['at'])
    recipe, packets = 'routine.result', {}
    if operation == 'execute_local_communication':
        result = world.s['communication_results'][params['request_id']]
        if result['evidence_id'] not in world.s['knowledge'].get(actor, {}):
            raise ValueError('Response receipt unavailable')
        # Keep words as testimony, even when they claim acceptance or success.
        words = result['utterance']
        exact = 'Testimony from ' + result['actor'] + ':\n' + words
        recipe = 'engine.communication'
        packets = {'engine.speech': {'speaker': result['actor']},
                   'receipt.exact': {'receipt_text': words}}
        if 'terms' in result:
            terms = result['terms']
            terms_text = (str(terms['quantity']) + ' ' + terms['material'] + ' from '
                          + terms['from'] + ' to ' + terms['to'] + '.')
            packets['engine.offer'] = {'offer_status': result['status'], 'terms_text': terms_text}
            exact += '\nRecorded offer status: ' + result['status'] + '. Terms: ' + terms_text
        # Speech has no selected elapsed rule. Never label causal ticks seconds.
    else:
        if params.get('actor') != actor:
            raise ValueError('Response receipt unavailable')
        if operation == 'execute_player_scene_action':
            result = world.s['scene_action_results'][event_id]
            outcome = result['outcome']
            exact = '\n'.join([outcome['summary'], *outcome['observations']])
            packets['elapsed.action'] = {'elapsed_seconds': outcome['elapsed_seconds']}
        elif operation == 'execute_settlement_action':
            records = world.s['settlement_receipts'][actor]
            key = params['request_id']
            exact = '\n'.join(records[k]['text'] for k in (key, key + ':inspection') if k in records)
            # Settlement receipts store cumulative elapsed time, not action span.
        elif operation == 'continue_player_process':
            result = world.s['process_phase_receipts'][params['phase_id']]
            exact = result['summary']
            observed = world.s.get('scene_action_results', {}).get('process-observation:' + params['phase_id'])
            if observed is not None:
                outcome = observed['outcome']
                exact += '\n' + '\n'.join([outcome['summary'], *outcome['observations']])
            recipe = 'engine.phase'
            packets['engine.phase'] = {'phase_status': result['status'],
                'worked_seconds': result['worked_seconds'],
                'required_seconds': result['worked_seconds'] + result['remaining_seconds']}
            packets['elapsed.action'] = {'elapsed_seconds': result['elapsed_seconds']}
            # Literal fallback retains phase status/progress and actual elapsed.
            fallback = (exact + '\nRecorded phase status: ' + result['status'] + '; progress: '
                + str(result['worked_seconds']) + '/' + str(result['worked_seconds'] + result['remaining_seconds'])
                + ' seconds. Elapsed in this phase: ' + str(result['elapsed_seconds']) + ' seconds.')
        else:
            raise ValueError('No offline receipt adapter for this operation')
        packets['receipt.exact'] = {'receipt_text': exact}
        if operation == 'continue_player_process':
            exact = fallback
    return {'actor_id': actor, 'snapshot_id': snapshot, 'recipe': recipe,
            'packets': packets, 'literal_text': exact}


def render_receipt(world, actor, event_id, *, scope=None, variant_seed=0):
    """Render the compatibility Engine library from actual receipt facts."""
    facts = receipt_facts(world, actor, event_id, scope=scope)
    return _render(actor, facts['snapshot_id'], facts['recipe'], facts['packets'],
                   facts['literal_text'], seed=variant_seed)


def player_drafts(world, actor, *, scope=None):
    """Return suggestions without committing, resolving or filtering feasibility.

    Editing text supplies an intention, not permission to execute its associated
    structured action. The host still requires explicit submission and review.
    """
    from solo_actions import _operation_and_options
    _guard(world, actor, scope)
    operation, options = _operation_and_options(world, actor)
    snapshot = 'draft:' + _identity(world.s['campaign_id'], actor, world.s['clock'], options)
    library = _library()
    families = {f['id']: f for f in library['families']}
    drafts = []
    for option in options:
        action_id = option['action_id']
        family_id = 'player.' + action_id if operation == 'execute_settlement_action' else 'engine.scene_draft'
        family = families.get(family_id)
        if family is None:
            continue  # Unsupported suggestions never dispatch or invent text.
        values = {} if operation == 'execute_settlement_action' else {'draft_text': option['text']}
        for variant in range(len(family['variants'])):
            context = {'actor_id': actor, 'snapshot_id': snapshot,
                'source_ref': 'draft:' + _identity(snapshot, action_id),
                'source_kind': 'player_request', 'state': family['state'], 'values': values}
            from routine_format import compose
            text = compose(library, [{'family_id': family_id, 'variant': variant, 'context': context}])
            drafts.append({'action_id': action_id, 'operation': operation, 'text': text,
                'family_id': family_id, 'variant': variant, 'editable': True,
                'requires_explicit_submission': True, 'automatic_execution': False})
    return {'actor_id': actor, 'snapshot_id': snapshot, 'format': 'plain_text',
        'drafts': drafts, 'custom_response': {'editable': True, 'text': '',
            'requires_explicit_submission': True},
        'render_usage': {'provider_calls': 0, 'model_tokens': 0}}


def render_status(*, actor_id, snapshot_id, status):
    """Render an explicit public host status, never private validator diagnoses."""
    allowed = {'proposal_ready': 'proposal.ready', 'declared_not_resolved': 'request.unresolved',
        'acceptance_required': 'request.acceptance', 'unavailable': 'request.unavailable'}
    identity = allowed.get(status, 'request.unavailable')
    from routine_format import render_fragment
    library = _library()
    family = next(f for f in library['families'] if f['id'] == identity)
    text = render_fragment(library, identity, {'actor_id': actor_id, 'snapshot_id': snapshot_id,
        'source_ref': 'public-host-status', 'source_kind': 'host_status',
        'state': family['state'], 'values': {}})
    return {'text': text, 'format': 'plain_text',
            'render_usage': {'provider_calls': 0, 'model_tokens': 0}}
