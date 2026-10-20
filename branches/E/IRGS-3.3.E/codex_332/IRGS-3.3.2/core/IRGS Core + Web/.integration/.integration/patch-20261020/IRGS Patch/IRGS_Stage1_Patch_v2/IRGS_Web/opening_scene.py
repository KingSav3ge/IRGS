"""Bounded, deterministic opening scene for a new historical playthrough (directive v1.0 s.XI.b).

Built once inside Store.create, before its single atomic write, from the already-validated sourced
snapshot and the confirmed player character only. Presentation only: it applies no Core events,
clock change, resources, relationships or NPC speech, so a replayed create or a reload cannot
duplicate effects. It invents no historical fact and stops at the player's first voluntary decision.
"""
import copy

VERSION = 1
PROMPT = ('Nothing has been decided for you and no time has passed. Say or do whatever you choose. '
          'Your words are saved exactly as written. This build does not yet resolve outcomes automatically, '
          'so your first move is recorded as a pending attempt.')


def build_opening(state, player_id):
    """Return the opening record for a new historical state, or None for other campaigns."""
    start = state.get('historical_start')
    if not start or player_id not in state.get('actors', {}):
        return None
    snapshot, actor = start['snapshot'], state['actors'][player_id]
    guide, label = snapshot['entry_guide'], start['opening']['label']
    fact = snapshot['domains']['political'][0]
    role = actor.get('role')
    who = f"You are {actor['name']}" + (f", recorded as {role}." if role else '.')
    who += (' Only what was established when this character was created is true of you. '
            'No rank, oath, wage, post or possession has been assumed.')
    blocks = [
        {'kind': 'setting', 'text': f"{label}. {guide['immediate_situation'][0]}", 'source_ids': list(guide['source_ids'])},
        {'kind': 'character', 'text': who, 'source_ids': []},
        {'kind': 'world_hook', 'text': 'Known at this date: ' + fact['statement'],
         'source_ids': list(fact.get('source_ids', [])), 'fact_id': fact['id']},
        {'kind': 'first_decision', 'text': PROMPT, 'source_ids': []},
    ]
    return {'id': 'opening:' + state['campaign_id'], 'version': VERSION, 'actor_id': player_id,
            'title': 'Opening · ' + label, 'blocks': blocks, 'hook': {'fact_id': fact['id']},
            'snapshot_sha256': start['snapshot_sha256'], 'presented_at_sequence': state['clock'],
            'effects_applied': False, 'narration': 'deterministic_reference_text'}


def opening_view(state, actor_id):
    """Player-safe projection. Status is derived from the journal; nothing is written on read."""
    opening = state.get('opening_scene')
    if not opening or opening.get('actor_id') != actor_id:
        return None
    declared = any(e['op'].removeprefix('ast_') == 'record_player_action' and e.get('params', {}).get('actor') == actor_id
                   for e in state.get('journal', []))
    view = {k: copy.deepcopy(opening[k]) for k in ('id', 'version', 'title', 'blocks', 'effects_applied', 'narration')}
    view['status'] = 'first_action_declared' if declared else 'awaiting_first_action'
    return view
