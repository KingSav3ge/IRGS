"""Engine-owned runtime over the exact Catalog-authored neutral text depot.

Only authored text is cached. The caller supplies a trusted actor projection;
formatting grants no authority and never calls an inference or network service.
"""
from functools import lru_cache
import hashlib
import json
from pathlib import Path

from routine_format import _pairs, compose_recipe, render_fragment, validate_library

DEPOT = Path(__file__).resolve().parent.parent / 'data/responses/depot_v1/library.json'
SOURCE_SHA256 = '8b397ae8cd72cf5ed59c330c0572e34922579726740edbeed9fca957044a6ae4'
LIBRARY_ID = 'irgs-response-depot-v1'
USAGE = {'provider_calls': 0, 'model_tokens': 0}


@lru_cache(maxsize=1)
def _depot():
    if any(path.is_symlink() for path in (DEPOT,*DEPOT.parents)):
        raise ValueError('Linked response depot')
    with DEPOT.open('rb') as source:
        raw=source.read(1048577)
    if len(raw)>1048576 or hashlib.sha256(raw).hexdigest() != SOURCE_SHA256:
        raise ValueError('Response depot source mismatch')
    # Validate the same bytes whose identity was checked, even during a host update.
    library=json.loads(raw,object_pairs_hook=_pairs)
    validate_library(library)
    return library


def _packet(family, actor, snapshot, values):
    return {'actor_id': actor, 'snapshot_id': snapshot, 'source_ref': 'fact:' + family['id'],
            'source_kind': family['source_kind'], 'state': family['state'], 'values': values}


def _result(text, mode, variants):
    return {'text': text, 'mode': mode, 'format': 'plain_text', 'library_id': LIBRARY_ID,
            'library_version': '1.0.0', 'variants': variants, 'render_usage': dict(USAGE)}


def render_exact(actor, snapshot, exact_text, *, elapsed_seconds=None, variant_seed=0):
    """Trusted presentation helper; shared_runtime establishes actual facts."""
    try:
        library = _depot()
        families = {f['id']: f for f in library['families']}
        facts = {'receipt.exact': {'receipt_text': exact_text}}
        if elapsed_seconds is not None:
            facts['elapsed.action'] = {'elapsed_seconds': elapsed_seconds}
        variants = {key: int(hashlib.sha256(str((actor,snapshot,key,variant_seed)).encode()).hexdigest()[:16],16)
                    % len(families[key]['variants']) for key in facts}
        text = compose_recipe(library, 'routine.result',
            {key: _packet(families[key],actor,snapshot,values) for key,values in facts.items()},
            variants=variants)
        return _result(text, 'scripted', variants)
    except (OSError, ValueError, KeyError, TypeError):
        # No truncation, lost negation, implicit dispatch or action re-execution.
        return _result(exact_text, 'literal_receipt', {})


def draft_variants(actor, snapshot, capability):
    """Bound an actual adapter-selected capability; tags alone never route."""
    if not capability.draft_family:
        return []
    import json
    try:
        library = _depot()
        family = next(f for f in library['families'] if f['id']==capability.draft_family)
        if family['channel'] != 'player_draft':
            raise ValueError('Player draft family required')
        values = json.loads(capability.draft_values_json)
        rows = []
        for index in range(len(family['variants'])):
            text = render_fragment(library, family['id'], _packet(family,actor,snapshot,values),variant=index)
            rows.append({'text':text,'family_id':family['id'],'variant':index,
                         'intent_tag':family['intent_tag'],'mode':'scripted'})
    except (OSError, ValueError, KeyError, TypeError, StopIteration):
        rows = ([{'text':capability.authored_intention,'mode':'literal_draft','intent_tag':None}]
                if capability.authored_intention else [])
    return [{**row,'capability_id':capability.capability_id,'operation_id':capability.operation_id,
             'editable':True,'requires_explicit_submission':True,'automatic_execution':False}
            for row in rows]


def render_public_status(actor, snapshot, status):
    mapping = {'declared_not_resolved':('request.unresolved','Your declaration is recorded and remains unresolved.'),
        'acceptance_required':('request.acceptance','Explicit submission and acceptance are required.'),
        'unavailable':('request.unavailable','This response is unavailable.')}
    identity, literal = mapping.get(status,mapping['unavailable'])
    try:
        library = _depot()
        family = next(f for f in library['families'] if f['id']==identity)
        text = render_fragment(library,identity,_packet(family,actor,snapshot,{}))
        return _result(text,'scripted',{identity:0})
    except (OSError, ValueError, KeyError, TypeError, StopIteration):
        return _result(literal,'literal_status',{})
