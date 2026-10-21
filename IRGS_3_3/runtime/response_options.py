"""Received contextual response drafts, without committing their proposed effects.

The prompt is a received information record. Its choices are supplied suggestions
for the player's next declaration, not verified feasibility, automatic decisions
or completed combat actions. No prompt is inferred from private world facts.
"""
from __future__ import annotations

import copy
import re


MAX_CHOICES = 8
CONTEXT_KIND = re.compile(r'[a-z][a-z0-9_-]{0,63}')


def _text(value, limit, *, empty=False):
    return isinstance(value, str) and len(value) <= limit and (empty or bool(value.strip()))


def _choices(value):
    if not isinstance(value, list) or len(value) > MAX_CHOICES:
        return False
    seen = set()
    for choice in value:
        if (not isinstance(choice, dict) or set(choice) != {'id', 'label', 'text'}
                or not _text(choice.get('id'), 128) or choice['id'] in seen
                or not _text(choice.get('label'), 160) or not _text(choice.get('text'), 2000)):
            return False
        seen.add(choice['id'])
    return True


def _present(state, actor_id):
    if actor_id not in state.get('actors', {}):
        return False
    registry = state.get('entity_registry')
    if registry is None:
        return True
    from temporal_registry import available_entities
    scenario = state.get('starting_control', {}).get('scenario_id', 'individual')
    return any(row['id'] == actor_id for row in available_entities(registry, scenario_id=scenario)['characters'])


def operate_response_prompt(core, state, at, params):
    """Receive one explicitly supplied prompt inside Core's atomic transaction."""
    allowed = {'campaign_id', 'source_ref', 'prompt_id', 'recipient', 'title',
               'description', 'context_kind', 'choices'}
    assert set(params) == allowed, 'response prompt requires its explicit information fields only'
    prompt_id, recipient = params['prompt_id'], params['recipient']
    assert _text(prompt_id, 128), 'bounded prompt identity required'
    assert isinstance(recipient, str) and _present(state, recipient), 'actual existing recipient required'
    assert _text(params['title'], 160), 'bounded prompt title required'
    assert _text(params['description'], 4000, empty=True), 'bounded prompt description required'
    assert isinstance(params['context_kind'], str) and CONTEXT_KIND.fullmatch(params['context_kind']), 'plain context kind required'
    assert _choices(params['choices']), 'at most eight distinct bounded response drafts are supported'
    prompts = state.setdefault('response_prompts', {})
    assert prompt_id not in prompts, 'response prompt identity already received'
    prompts[prompt_id] = {'id': prompt_id, 'recipient': recipient, 'title': params['title'],
        'description': params['description'], 'context_kind': params['context_kind'],
        'choices': copy.deepcopy(params['choices']), 'received_at': at,
        'status': 'received_prompt', 'active': True, 'source_ref': params['source_ref']}


def _combat_drafts():
    return [
        {'id': 'attempt-strike', 'label': 'Attempt a measured strike',
         'text': 'I attempt a measured strike at an opponent I can legitimately engage.'},
        {'id': 'protect-myself', 'label': 'Try to protect myself',
         'text': 'I try to protect myself while assessing the immediate danger.'},
        {'id': 'reposition', 'label': 'Try to reposition',
         'text': 'I try to move to a safer or more useful position, if a route is available.'},
        {'id': 'break-contact', 'label': 'Try to break contact',
         'text': 'I attempt to break contact and withdraw if circumstances allow.'},
        {'id': 'speak', 'label': 'Attempt to speak',
         'text': 'I try to speak to those involved, if I can make myself heard.'},
    ]


def response_choices(state, actor_id):
    """Return the unique newest active received prompt for this controlled actor.

    Tied newest causal coordinates do not establish priority; they select no
    single prompt. The player can still write their own response. The returned
    projection is detached and excludes private provenance and other recipients.
    Supplied risky or ill-advised responses are retained: this is neither a list
    of winning moves nor a hidden-state feasibility or probability assessment.
    """
    from core_world import CoreWorld
    if actor_id not in CoreWorld.player_ids(None, state) or not _present(state, actor_id):
        return None
    received = []
    for prompt in state.get('response_prompts', {}).values():
        if (not isinstance(prompt, dict) or prompt.get('recipient') != actor_id
                or prompt.get('active') is not True or prompt.get('status') != 'received_prompt'
                or type(prompt.get('received_at')) is not int
                or not 0 <= prompt['received_at'] <= state['clock']):
            continue
        if (not _text(prompt.get('id'), 128) or not _text(prompt.get('title'), 160)
                or not _text(prompt.get('description'), 4000, empty=True)
                or not isinstance(prompt.get('context_kind'), str)
                or not CONTEXT_KIND.fullmatch(prompt['context_kind']) or not _choices(prompt.get('choices'))):
            continue
        received.append(prompt)
    if not received:
        return None
    newest = max(prompt['received_at'] for prompt in received)
    latest = [prompt for prompt in received if prompt['received_at'] == newest]
    if len(latest) != 1:
        return None
    prompt = latest[0]
    choices = copy.deepcopy(prompt['choices'])
    if not choices and prompt['context_kind'] == 'combat':
        choices = _combat_drafts()
    return {'prompt_id': prompt['id'], 'title': prompt['title'], 'description': prompt['description'],
            'context_kind': prompt['context_kind'], 'received_at': prompt['received_at'],
            'status': 'received_prompt', 'choices': choices, 'own_response_allowed': True,
            'execution': 'draft_only'}
