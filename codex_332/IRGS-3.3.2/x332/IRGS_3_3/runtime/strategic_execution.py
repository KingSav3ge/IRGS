"""Bounded autonomous institutions sharing one Core resource ledger.

All rates, subscriptions and rights installed by ``strategic_world`` are
explicitly synthetic source selections. A subscription exposes only its named
records after receipt. It is not a claim that real institutions know all local
stocks instantly. Planners receive detached observations, never a world object.
Shared handlers revalidate proposals against actual current state at commit.
"""
import copy
from dataclasses import dataclass

from irgs_reference import InvalidEvent, digest
from r8_dependencies import code_identity
from r8_strategy import strategic_world as fixture_world
from r9_runtime import frontier


INSTITUTIONS = ('business', 'household', 'government', 'military')
OPERATIONS = {
    'business': {'commit_shift', 'start_job', 'complete_job', 'accrue_job_wages'},
    'household': {'provision_meals'},
    'government': {'assess_tax', 'pay_tax'},
    'military': {'authorize_mobilization', 'enroll', 'issue_kits'},
}
DEFAULT_SCOPE = {
    'business': {'worker_ids': ['person-B'], 'recipe_ids': ['cook'],
                 'site_ids': ['house-1'], 'job_prefix': 'cook:', 'wage_rate': 1},
    'household': {'household_ids': ['house-1']},
    'government': {'payer_ids': ['farmer-b'], 'max_tax_amount': 2},
    'military': {'person_ids': ['farmer-a'], 'max_target': 1},
}
DEFAULT_PATHS = {
    'business': [('econ3', 'recipes', 'cook'), ('econ3', 'stocks', 'house-1'),
                 ('econ3', 'active_jobs'), ('econ3', 'completed_jobs'),
                 ('actors', 'person-B', 'disabled'), ('actors', 'person-B', 'location'),
                 ('commitments', 'person-B'), ('econ3', 'qualifications', 'person-B'),
                 ('econ3', 'sites', 'house-1')],
    'household': [('econ3', 'stocks', 'house-1', 'meal'), ('econ3', 'active_jobs'),
                  ('econ3', 'meals_delivered', 'house-1')],
    'government': [('econ3', 'tax_claims'), ('cash', 'farmer-b')],
    'military': [('gov', 'mobilization'), ('actors', 'farmer-a', 'enlisted'),
                 ('actors', 'farmer-a', 'disabled'), ('equipment', 'farmer-a', 'kit'),
                 ('equipment', 'depot', 'kit')],
}


def tick_time(tick):
    """Six explicit institutional reviews per synthetic 24-hour day."""
    return (tick // 6) * 24 + tick % 6 + 1


def _lookup(value, path):
    for key in path:
        if not isinstance(value, dict) or key not in value:
            return False, None
        value = value[key]
    return True, value


@dataclass(frozen=True)
class Observation:
    known: bool
    present: bool = False
    value: object = None


class Unobserved(Exception):
    pass


class ObservableView:
    """Detached selected records plus audited reads; no reference to world state."""
    def __init__(self, rows, unavailable=()):
        self._rows = copy.deepcopy(rows)
        self._unavailable = copy.deepcopy(list(unavailable))
        self.reads = []

    def read(self, *path):
        path = tuple(path)
        matches = [row for row in self._rows
                   if path[:len(row['path'])] == tuple(row['path'])]
        if not matches:
            reason = 'unreceived_or_inactive' if any(
                path[:len(p)] == tuple(p) for p in self._unavailable) else 'not_selected'
            self.reads.append({'path': list(path), 'status': 'unknown', 'reason': reason})
            return Observation(False)
        row = max(matches, key=lambda x: len(x['path']))
        present, value = _lookup(row.get('value'), path[len(row['path']):]) if row['present'] else (False, None)
        self.reads.append({'path': list(path), 'status': 'present' if present else 'observed_absent',
                           'grant_id': row['grant_id'], 'source_ref': row['source_ref']})
        return Observation(True, present, copy.deepcopy(value))

    def require(self, *path):
        item = self.read(*path)
        if not item.known or not item.present:
            raise Unobserved('/'.join(path))
        return item.value

    def optional(self, *path, absent=None):
        item = self.read(*path)
        if not item.known:
            raise Unobserved('/'.join(path))
        return item.value if item.present else copy.deepcopy(absent)

    def checksum(self):
        return digest({'rows': self._rows, 'unavailable': self._unavailable})


def observable_projection(state, selection, at):
    """Only trusted projection construction can read the authoritative state.

    Unreceived grants do not fetch their values, including for projection hashes.
    An observed absent record differs from an unobserved record. A planner may
    interpret observed absence using that selected ledger's documented semantics.
    """
    rows, unavailable = [], []
    for grant in selection['observations']:
        if not grant['active'] or grant['received_at'] is None or grant['received_at'] > at:
            unavailable.append(grant['path'])
            continue
        present, value = _lookup(state, grant['path'])
        rows.append({'path': grant['path'], 'present': present,
                     **({'value': copy.deepcopy(value)} if present else {}),
                     'grant_id': grant['id'], 'source_ref': grant['source_ref']})
    return ObservableView(rows, unavailable)


def default_observations(institution):
    return [{'id': f'{institution}:observation:{i}', 'path': list(path),
             'source_ref': 'synthetic:selected-current-ledger-subscription',
             'received_at': 0, 'active': True, 'mode': 'subscribed_current_records'}
            for i, path in enumerate(DEFAULT_PATHS[institution])]


def _validate_selection(selection):
    institution = selection['institution']
    if institution not in OPERATIONS or not all(isinstance(selection[k], str) and selection[k].strip()
                                              for k in ('source_ref', 'id')):
        raise InvalidEvent('institution, selection identity and source reference required')
    if type(selection['active']) is not bool or not set(selection['operations']) <= OPERATIONS[institution]:
        raise InvalidEvent('unsupported institutional rights')
    if type(selection['effective_at']) is not int or not isinstance(selection['scope'], dict):
        raise InvalidEvent('integer selection time and explicit scope required')
    grants = selection['observations']
    if not isinstance(grants, list) or len({g['id'] for g in grants}) != len(grants):
        raise InvalidEvent('unique observation grant identities required')
    for grant in grants:
        if not all(isinstance(grant[k], str) and grant[k].strip() for k in ('id', 'source_ref')) or grant.get('mode') != 'subscribed_current_records':
            raise InvalidEvent('each observation needs a selected current-record source')
        if not isinstance(grant['path'], list) or not grant['path'] or not all(isinstance(p, str) and p for p in grant['path']):
            raise InvalidEvent('observation must name a bounded non-root record path')
        received = grant['received_at']
        if type(grant['active']) is not bool or received is not None and (
                type(received) is not int or received < 0 or received > selection['effective_at']):
            raise InvalidEvent('receipt must be an actual nonfuture integer time or explicitly unreceived')


def select_institution(world, institution, selection_id, operations, observations, at,
                       source_ref, scope=None, active=True):
    """Install a new prospective source selection, preserving earlier selections.

    This is an explicit source/authority configuration action. It does not prove
    real legal authority, create inventory, or backdate receipt of a report.
    """
    if type(at) is not int or at < world.s['clock']:
        raise InvalidEvent('selection cannot precede the current causal checkpoint')
    candidate = type(world)(state=world.s)
    ledger = candidate.s.get('r8_strategy', {})
    if ledger.get('boundary_version') != 1:
        raise InvalidEvent('explicit institutional boundary binding required')
    if selection_id in ledger['selections']:
        raise InvalidEvent('selection identity already used')
    selection = {'id': selection_id, 'institution': institution,
                 'operations': sorted(set(operations)), 'observations': copy.deepcopy(observations),
                 'effective_at': at, 'source_ref': source_ref, 'active': active,
                 'scope': copy.deepcopy(DEFAULT_SCOPE.get(institution, {}) if scope is None else scope)}
    _validate_selection(selection)
    selection_hash = digest(selection)
    ledger['selections'][selection_id] = {'selection': selection, 'sha256': selection_hash}
    ledger['institutions'][institution] = selection_id
    ledger['selection_history'].append({'selection_id': selection_id, 'institution': institution,
                                        'at': at, 'source_ref': source_ref, 'sha256': selection_hash})
    candidate.s['clock'] = at
    candidate._validate(candidate.s)
    world.s = candidate.s
    return selection_id


def strategic_world(grain=240, fuel=120):
    """Seed the declared synthetic fixture, then bind explicit subscriptions."""
    world = fixture_world(grain, fuel)
    ledger = world.s['r8_strategy']
    ledger['profile'].update(id='synthetic-core33-institutions-v1', taxpayer='farmer-b',
                             military_person='farmer-a', business_job_prefix='cook:', business_wage_rate=1)
    ledger['profile_hash'] = digest(ledger['profile'])
    ledger.update(boundary_version=1, institutions={}, selections={}, selection_history=[])
    for institution in INSTITUTIONS:
        select_institution(world, institution, f'synthetic:{institution}:v1', OPERATIONS[institution],
                           default_observations(institution), 0,
                           'synthetic:explicit-selected-observations-and-decision-rights')
    return world


def _free(view, site, material):
    # Complete selected stock/reservation sources justify absent-entry zero.
    # Missing/unreceived sources instead raise Unobserved and stop this plan.
    quantity = view.optional('econ3', 'stocks', site, material, absent=0)
    jobs = view.require('econ3', 'active_jobs')
    reserved = sum(job['reserved_inputs'].get(material, 0)
                   for job in jobs.values() if job['site'] == site)
    return quantity - reserved


def _allowed(selection, op, params, view):
    if not selection['active'] or op not in selection['operations']:
        return False, 'operation_right_not_selected'
    scope = selection['scope']
    if op == 'provision_meals':
        allowed = params['household'] in scope.get('household_ids', [])
    elif op == 'commit_shift':
        allowed = params['person'] in scope.get('worker_ids', []) and params['role'] in (
            'work:' + rid for rid in scope.get('recipe_ids', []))
    elif op == 'start_job':
        recipe = view.require('econ3', 'recipes', params['recipe_id'])
        allowed = (set(params['workers']) <= set(scope.get('worker_ids', []))
                   and params['recipe_id'] in scope.get('recipe_ids', [])
                   and recipe['site'] in scope.get('site_ids', [])
                   and params['job_id'].startswith(scope.get('job_prefix') or '\0'))
    elif op in ('complete_job', 'accrue_job_wages'):
        collection = 'active_jobs' if op == 'complete_job' else 'completed_jobs'
        job = view.require('econ3', collection, params['job_id'])
        allowed = (params['job_id'].startswith(scope.get('job_prefix') or '\0')
                   and set(job['workers']) <= set(scope.get('worker_ids', []))
                   and job['recipe_id'] in scope.get('recipe_ids', [])
                   and job['site'] in scope.get('site_ids', []))
        if op == 'accrue_job_wages':
            allowed = allowed and params['rate'] <= scope.get('wage_rate', -1)
    elif op == 'assess_tax':
        allowed = (params['payer'] in scope.get('payer_ids', [])
                   and params['amount'] <= scope.get('max_tax_amount', -1))
    elif op == 'pay_tax':
        claim = view.require('econ3', 'tax_claims', params['tax_id'])
        allowed = claim['payer'] in scope.get('payer_ids', [])
    elif op == 'authorize_mobilization':
        allowed = params['target'] <= scope.get('max_target', -1)
    elif op == 'enroll':
        allowed = params['person'] in scope.get('person_ids', [])
    elif op == 'issue_kits':
        allowed = set(params['persons']) <= set(scope.get('person_ids', []))
    else:
        allowed = False
    return (True, None) if allowed else (False, 'decision_outside_selected_scope')


class Planner:
    def __init__(self, institution, selection, policy, view, tick):
        self.institution, self.selection, self.policy, self.view, self.tick = institution, selection, policy, view, tick
        self.at, self.day, self.phase = tick_time(tick), tick // 6, tick % 6
        self.events, self.withheld = [], []

    def add(self, op, **params):
        allowed, reason = _allowed(self.selection, op, params, self.view)
        if not allowed:
            self.withheld.append({'operation': op, 'reason': reason})
            return
        self.events.append({'id': f'irgs33:{self.tick}:{self.institution}:{op}',
                            'at': self.at, 'op': op, 'params': copy.deepcopy(params)})


def plan_business(plan):
    v, p = plan.view, plan.policy
    worker, rid = p['worker'], p['business_recipe']
    jid = p['business_job_prefix'] + str(plan.day)
    if plan.phase == 0:
        recipe = v.require('econ3', 'recipes', rid)
        site = recipe['site']
        if worker not in plan.selection['scope'].get('worker_ids', []) or site not in plan.selection['scope'].get('site_ids', []):
            plan.withheld.append({'operation': 'commit_shift', 'reason': 'decision_outside_selected_scope'})
            return
        if v.require('actors', worker, 'disabled') or v.require('actors', worker, 'location') != site:
            return
        if rid not in v.require('econ3', 'qualifications', worker):
            return
        if v.require('econ3', 'sites', site)['workers_capacity'] < 1:
            return
        if all(_free(v, site, material) >= quantity for material, quantity in sorted(recipe['inputs'].items())):
            shifts = v.optional('commitments', worker, absent=[])
            if not any(start < plan.at + 2 and plan.at + 1 < end for start, end, _ in shifts):
                plan.add('commit_shift', person=worker, start=plan.at + 1, end=plan.at + 2, role='work:' + rid)
    elif plan.phase == 1:
        if [plan.at, plan.at + 1, 'work:' + rid] in v.optional('commitments', worker, absent=[]):
            plan.add('start_job', job_id=jid, recipe_id=rid, start=plan.at, end=plan.at + 1, workers=[worker])
    elif plan.phase == 2:
        job = v.optional('econ3', 'active_jobs', jid)
        if job is not None and job['end'] == plan.at:
            plan.add('complete_job', job_id=jid)
    elif plan.phase == 4:
        job = v.optional('econ3', 'completed_jobs', jid)
        if job is not None and not job['wages_accrued_for']:
            plan.add('accrue_job_wages', job_id=jid, rate=p['business_wage_rate'],
                     wage_agreement_ref=plan.selection['source_ref'])


def plan_household(plan):
    if plan.phase != 3:
        return
    v, p = plan.view, plan.policy
    delivered = v.optional('econ3', 'meals_delivered', p['household'], absent=0)
    need = max(0, (plan.day + 1) * p['household_daily_meals'] - delivered)
    quantity = min(need, _free(v, p['household'], 'meal'))
    if quantity > 0:
        plan.add('provision_meals', household=p['household'], quantity=quantity)


def plan_government(plan):
    v, p = plan.view, plan.policy
    if plan.phase == 0 and plan.day % p['tax_period_days'] == 0:
        tid = 'tax:' + str(plan.day)
        if v.optional('econ3', 'tax_claims', tid) is None:
            v.require('cash', p['taxpayer'])  # Selected payer existence, not assumed.
            plan.add('assess_tax', tax_id=tid, payer=p['taxpayer'], amount=p['tax_amount'],
                     authority_ref=plan.selection['source_ref'], basis_ref=p['id'])
    elif plan.phase == 1:
        for tid, claim in sorted(v.require('econ3', 'tax_claims').items()):
            due = claim['assessed'] - claim['paid']
            if due and v.require('cash', claim['payer']) >= due:
                plan.add('pay_tax', tax_id=tid, amount=due)
                break


def plan_military(plan):
    v, p = plan.view, plan.policy
    person = p['military_person']
    if plan.phase == 0:
        if v.optional('gov', 'mobilization') is None:
            plan.add('authorize_mobilization', mandate=plan.selection['source_ref'], target=p['army_target'])
    elif plan.phase == 1:
        mandate = v.optional('gov', 'mobilization')
        if mandate is not None and not v.require('actors', person, 'enlisted') and not v.require('actors', person, 'disabled'):
            plan.add('enroll', person=person)
    elif plan.phase == 2:
        if v.require('actors', person, 'enlisted') and not v.optional('equipment', person, 'kit', absent=0):
            if v.require('equipment', 'depot', 'kit') > 0:
                plan.add('issue_kits', persons=[person])


PLANNERS = {'business': plan_business, 'household': plan_household,
            'government': plan_government, 'military': plan_military}
POLICY_KEYS = {
    'business': ('worker', 'business_recipe', 'business_job_prefix', 'business_wage_rate'),
    'household': ('household', 'household_daily_meals'),
    'government': ('id', 'taxpayer', 'tax_period_days', 'tax_amount'),
    'military': ('military_person', 'army_target'),
}


def _validate_boundary(ledger):
    if ledger.get('boundary_version') != 1:
        raise InvalidEvent('autonomous execution requires explicit institution observations and rights')
    if digest(ledger['profile']) != ledger['profile_hash']:
        raise InvalidEvent('selected policy changed without prospective rebinding')
    if type(ledger['next_tick']) is not int or ledger['next_tick'] < 0:
        raise InvalidEvent('invalid institutional review checkpoint')
    for sid, record in ledger['selections'].items():
        _validate_selection(record['selection'])
        if sid != record['selection']['id'] or digest(record['selection']) != record['sha256']:
            raise InvalidEvent('selected information or authority changed without a new source selection')
    if set(ledger['institutions']) != set(INSTITUTIONS):
        raise InvalidEvent('four explicit institution selections required')
    for institution, sid in ledger['institutions'].items():
        if sid not in ledger['selections'] or ledger['selections'][sid]['selection']['institution'] != institution:
            raise InvalidEvent('institution selection binding mismatch')
        history = [entry for entry in ledger['selection_history'] if entry['institution'] == institution]
        if not history or history[-1]['selection_id'] != sid or history[-1]['sha256'] != ledger['selections'][sid]['sha256']:
            raise InvalidEvent('institution binding changed without a new source selection')


def advance(world, through_tick):
    """Advance four bounded planners, then commit through the shared frontier."""
    if 'r8_strategy' not in world.s:
        raise InvalidEvent('no source-selected institutional policy for this campaign')
    _validate_boundary(world.s['r8_strategy'])
    if type(through_tick) is not int or through_tick < world.s['r8_strategy']['next_tick']:
        raise InvalidEvent('forward integer horizon required')
    while world.s['r8_strategy']['next_tick'] < through_tick:
        source_hash = digest(world.s)
        candidate = type(world)(state=world.s)
        ledger = candidate.s['r8_strategy']
        tick, at = ledger['next_tick'], tick_time(ledger['next_tick'])
        if at < candidate.s['clock']:
            raise InvalidEvent('next institutional review precedes current causal checkpoint')
        events, decisions = [], {}
        for institution in INSTITUTIONS:
            record = ledger['selections'][ledger['institutions'][institution]]
            selection = copy.deepcopy(record['selection'])
            view = observable_projection(candidate.s, selection, at)
            policy = {key: copy.deepcopy(ledger['profile'][key]) for key in POLICY_KEYS[institution]}
            plan = Planner(institution, selection, policy, view, tick)
            if not selection['active'] or selection['effective_at'] > at:
                plan.withheld.append({'reason': 'institution_rights_inactive'})
            else:
                try:
                    PLANNERS[institution](plan)
                except Unobserved as missing:
                    plan.withheld.append({'reason': 'required_information_unknown_or_absent', 'path': str(missing)})
            events.extend(plan.events)
            decisions[institution] = {'selection_id': selection['id'], 'selection_hash': record['sha256'],
                'selection_source_ref': selection['source_ref'], 'operations': selection['operations'],
                'scope': selection['scope'], 'projection_hash': view.checksum(), 'reads': view.reads,
                'proposals': plan.events, 'withheld': plan.withheld}
        result = frontier(candidate, events)
        candidate.apply('irgs33:strategy:review:' + str(tick), at, 'review_no_change')
        ledger = candidate.s['r8_strategy']
        for decision in decisions.values():
            ids = {e['id'] for e in decision['proposals']}
            decision['committed'] = [eid for eid in result['committed'] if eid in ids]
            decision['deferred'] = [eid for eid in result['deferred'] if eid in ids]
        ledger['decisions'].append({'tick': tick, 'at': at, 'policy_hash': ledger['profile_hash'],
            'code_hash': code_identity(), 'source_hash': source_hash, 'institutions': decisions,
            'reads': sorted({tuple(read['path']) for d in decisions.values() for read in d['reads']}),
            'proposals': events, 'committed': result['committed'], 'deferred': result['deferred'],
            'edges': result.get('edges', []), 'failures': result.get('errors', {})})
        ledger['next_tick'] = tick + 1
        candidate._validate(candidate.s)
        world.s = candidate.s
    return world
