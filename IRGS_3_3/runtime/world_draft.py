"""Bounded data-only draft contract for two existing reviewed initializers.

A draft is not a campaign. No paths, scripts, hidden rules or creator data are
executed. Durable storage, atomic publication and access control belong to host.
"""
import copy
from irgs_reference import digest
from settlement_setup import preview as rise_preview, initialize as rise_initialize

SCHEMA_VERSION = 'irgs-world-draft-1'
VALIDATION_VERSION = 'irgs-world-validation-1'


def inspect(draft):
    """Return a validation DTO, including a public diagnostic for invalid drafts."""
    try:
        return validate(draft)
    except ValueError as error:
        return {'schema_version': VALIDATION_VERSION, 'status': 'invalid',
                'errors': [{'code': 'invalid_draft', 'message': str(error)}], 'committed': False}


def _quay_review(choices, campaign_id):
    if not isinstance(choices, dict) or set(choices) != {'snapshot_sha256', 'character'}:
        raise ValueError('Select the dated snapshot and reviewed fictional character')
    character = choices['character']
    if (not isinstance(character, dict) or set(character) != {'kind', 'name', 'species', 'opening_id'}
            or character.get('kind') != 'new' or character.get('species') != 'human'
            or character.get('opening_id') != 'quay-contact-v1'
            or not isinstance(character.get('name'), str) or not character['name'].strip()
            or len(character['name']) > 100):
        raise ValueError('Select a named new human and the fictional quay contact opening')
    from campaign_library import initial_campaign
    from starting_selection import options_for_world
    from start_readiness import review_start
    world = initial_campaign('military', campaign_id, scenario_id='hundred-years-war',
                             entry_id='hyw-1415', snapshot_sha256=choices['snapshot_sha256'])
    options = options_for_world(world)
    review = {'selection_digest': options['selection_digest'],
              'character': copy.deepcopy(character), 'start_review': review_start(world, character),
              'snapshot_sha256': choices['snapshot_sha256']}
    return world, review


def validate(draft):
    if not isinstance(draft, dict) or set(draft) != {'schema_version', 'draft_id', 'classification', 'profile_id', 'choices'}:
        raise ValueError('Supply only the supported world draft fields')
    if draft['schema_version'] != SCHEMA_VERSION:
        raise ValueError('Unsupported world draft schema')
    if not isinstance(draft['draft_id'], str) or not draft['draft_id'].strip() or len(draft['draft_id']) > 128:
        raise ValueError('Invalid draft identity')
    if draft['classification'] == 'fictional' and draft['profile_id'] == 'rise-r00':
        review = rise_preview(copy.deepcopy(draft['choices']))
        review_digest = review['review_digest']
        initializer = 'settlement_setup.initialize'
    elif draft['classification'] == 'mixed' and draft['profile_id'] == 'historical-quay':
        _, review = _quay_review(copy.deepcopy(draft['choices']), 'world-draft-review')
        review_digest = digest(review)
        initializer = 'campaign_library.initial_campaign + starting_selection.initialize_player'
    else:
        raise ValueError('Select a supported fictional Rise or mixed historical-quay profile')
    return {'schema_version': VALIDATION_VERSION, 'draft_id': draft['draft_id'], 'status': 'valid',
            'classification': draft['classification'], 'profile_id': draft['profile_id'],
            'draft_digest': digest(draft), 'review_digest': review_digest,
            'review': review, 'proposed_initializer': initializer,
            'unsupported': ['arbitrary historical drafts', 'custom geography or entities',
                            'custom scripts and rules', 'world-pack import/export'],
            'committed': False}


def initialize(draft, *, draft_digest, review_digest, campaign_id, explicitly_accepted):
    if explicitly_accepted is not True:
        raise ValueError('Explicit draft acceptance is required')
    if not isinstance(campaign_id, str) or not campaign_id.strip() or len(campaign_id) > 128:
        raise ValueError('Invalid new campaign identity')
    reviewed = validate(draft)
    if draft_digest != reviewed['draft_digest'] or review_digest != reviewed['review_digest']:
        raise ValueError('Draft or selected rules changed; review again')
    if draft['profile_id'] == 'rise-r00':
        return rise_initialize(copy.deepcopy(draft['choices']), review_digest, campaign_id)
    from starting_selection import initialize_player
    world, review = _quay_review(copy.deepcopy(draft['choices']), campaign_id)
    if digest(review) != review_digest:
        raise ValueError('Selected source or starting options changed; review again')
    return initialize_player(world, review['character'], selection_digest=review['selection_digest'],
                             request_ref='explicit-reviewed-world-draft:' + draft_digest)


def preview_initialization(draft):
    """Build a disposable candidate and return only its controlled actor projection.

    This is not a persisted campaign or authorization. Preview identities cannot
    be used for creation or submission; a host must review actual creation anew.
    """
    reviewed = validate(draft)
    campaign_id = 'draft-preview-' + reviewed['draft_digest'][:24]
    candidate = initialize(draft, draft_digest=reviewed['draft_digest'],
        review_digest=reviewed['review_digest'], campaign_id=campaign_id, explicitly_accepted=True)
    actor = candidate.s['player_actor_ids'][0]
    from shared_runtime import actor_view
    known = actor_view(candidate, actor, branch_id='ephemeral-preview', restore_id='ephemeral-preview')
    return {'schema_version': 'irgs-world-initialization-preview-1',
            'draft_id': reviewed['draft_id'], 'draft_digest': reviewed['draft_digest'],
            'review_digest': reviewed['review_digest'], 'profile_id': reviewed['profile_id'],
            'status': 'preview_only', 'committed': False, 'requires_explicit_acceptance': True,
            'preview_identities_reusable': False, 'actor_view': known}
