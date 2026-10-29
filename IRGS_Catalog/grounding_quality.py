"""Conservative offline evaluation of annotated claims; never authorizes effects."""
from copy import deepcopy
import json
from pathlib import Path

DIMENSIONS = ('input_scope', 'source_and_uncertainty', 'intent_mapping', 'proposal_vs_effect',
              'receipt_fidelity', 'hidden_information', 'npc_response', 'narration_quality')


def validate_fixture(catalog_root):
    root = Path(catalog_root) / 'evaluation/grounding_quality_v1'
    actor = json.loads((root / 'actor_inputs/cases.json').read_text())
    oracle = json.loads((root / 'evaluator_only/requirements.json').read_text())
    if (set(actor) != {'fixture_id', 'classification', 'cases'}
        or actor['fixture_id'] != 'irgs-grounding-quality-v1'
        or actor['classification'] != 'original-fictional-offline'
        or set(actor['cases']) != {'quay-contact', 'rise-r00'}
        or set(oracle) != {'classification', 'marker', 'required_dimensions', 'pending_journey_requirements'}
        or oracle['classification'] != 'evaluator-only' or oracle['marker'] != 'PRIVATE_GROUNDING_EVALUATOR'
        or oracle['marker'] in json.dumps(actor) or oracle['required_dimensions'] != list(DIMENSIONS)
        or set(oracle['pending_journey_requirements']) != {'consequences_constrain_later_choices', 'npc_decisions',
            'institution_decisions', 'needs_recovery', 'risk_conflict', 'older_branch_restore', 'live_provider_quality'}):
        raise ValueError('Invalid grounding fixture')
    return {'status': 'verified', 'cases': 2, 'semantic_inference_performed': False, 'alpha_qualified': False}


def _judgment(value):
    if not isinstance(value, dict) or set(value) != {'status', 'evidence_refs'}:
        raise ValueError('Each judgment must contain status and evidence_refs')
    status, refs = value['status'], value['evidence_refs']
    if status not in ('pass', 'fail', 'unknown') or not isinstance(refs, list):
        raise ValueError('Invalid judgment')
    if any(not isinstance(ref, str) or not ref.strip() for ref in refs):
        raise ValueError('Invalid evidence reference')
    if status != 'unknown' and not refs:
        raise ValueError('A judgment needs evidence')
    return status


def assess_proposal(model_input, proposal, semantic_judgment):
    """Check exact whitelist bindings; intent semantics remain a human judgment."""
    if not isinstance(model_input, dict) or not isinstance(proposal, dict):
        raise ValueError('Input and proposal must be objects')
    if set(model_input) != {'actor_id', 'intention', 'context', 'allowed_actions', 'source_refs'}:
        raise ValueError('Unexpected model input fields')
    if set(proposal) != {'intention', 'action_id', 'source_refs'}:
        raise ValueError('Unexpected proposal fields')
    intention, actions, refs = model_input['intention'], model_input['allowed_actions'], model_input['source_refs']
    proposed_refs = proposal['source_refs']
    if not isinstance(intention, str) or not intention or not isinstance(actions, list) or not isinstance(refs, list):
        raise ValueError('Invalid model input')
    if any(not isinstance(v, str) or not v for v in actions + refs) or not isinstance(proposed_refs, list):
        raise ValueError('Invalid action or source references')
    if any(not isinstance(v, str) or not v for v in proposed_refs):
        raise ValueError('Invalid proposal source references')
    semantic = _judgment(semantic_judgment)
    problems = []
    if proposal['intention'] != intention:
        problems.append('changed_intention')
    if proposal['action_id'] not in actions:
        problems.append('unreceived_action')
    if not proposed_refs or len(set(proposed_refs)) != len(proposed_refs) or any(v not in refs for v in proposed_refs):
        problems.append('unreceived_source')
    if semantic == 'fail':
        problems.append('intent_mismatch_reported')
    return {'status': 'fail' if problems else ('unknown' if semantic == 'unknown' else 'reviewed_pass'),
            'violations': problems, 'semantic_judgment': semantic,
            'semantic_inference_performed': False, 'action_authorized': False}


def assess_receipt(receipt, rendered):
    """Compare explicit committed fields; don't infer claims from unrestricted text."""
    required = {'event_id', 'status', 'truth_status', 'utterance'}
    if not isinstance(receipt, dict) or set(receipt) != required or not isinstance(rendered, dict) or set(rendered) != required:
        raise ValueError('Exact structured receipt and rendering required')
    if any(not isinstance(receipt[k], str) or not receipt[k] for k in required):
        raise ValueError('Missing committed receipt evidence')
    mismatches = sorted(k for k in required if rendered[k] != receipt[k])
    return {'status': 'fail' if mismatches else 'exact_structured_match', 'mismatches': mismatches,
            'free_text_semantics_checked': False, 'live_model_quality_verified': False}


def assess_review(judgments):
    if not isinstance(judgments, dict) or set(judgments) != set(DIMENSIONS):
        raise ValueError('All dimensions must be explicitly assessed')
    statuses = {name: _judgment(judgments[name]) for name in DIMENSIONS}
    result = 'fail' if 'fail' in statuses.values() else 'unknown' if 'unknown' in statuses.values() else 'reviewed_pass'
    return {'status': result, 'dimensions': deepcopy(statuses), 'reviewer_claims_verified': False,
            'alpha_qualified': False, 'live_model_quality_verified': False}
