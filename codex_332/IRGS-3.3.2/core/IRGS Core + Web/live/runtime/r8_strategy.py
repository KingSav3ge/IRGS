"""Bounded reactive institutional policies over ONE R7 ledger; synthetic profiles."""
import copy
from irgs_reference import initial_world, digest, InvalidEvent
from economic_extension import economy_fixture, free
from r7_frontier import R7World
from r8_dependencies import Access, frontier, code_identity

PROFILE = {'id': 'synthetic-r8-90d-v1', 'household_daily_meals': 3,
           'tax_period_days': 7, 'tax_amount': 2, 'army_target': 1,
           'authority_ref': 'fictional-selected-institution-policy',
           'business_recipe': 'cook', 'worker': 'person-B', 'household': 'house-1'}

def strategic_world(grain=240, fuel=120):
    s = economy_fixture(initial_world().s)
    s['commitments'] = {}
    s['econ3']['stocks']['house-1'].update(grain=grain, fuel=fuel)
    s['econ3']['opening'].update(grain=grain, fuel=fuel)
    s['r8_strategy'] = {'profile': copy.deepcopy(PROFILE), 'profile_hash': digest(PROFILE),
                        'next_tick': 0, 'decisions': []}
    return R7World(state=s)

def proposals(s, tick):
    """Select actions from actual stock, claims, commitments and membership.

    Six review stages per synthetic day. Time is hours, not six-hour days.
    Policy cannot manufacture work attestations for R6 tracked work.
    """
    p = s['r8_strategy']['profile']; day, phase = divmod(tick, 6)
    at = day * 24 + phase + 1
    out = []
    def add(institution, op, **params):
        out.append({'id': f'r8:{tick}:{institution}:{op}', 'at': at, 'op': op, 'params': params})
    e = s['econ3']; house = p['household']; worker = p['worker']
    jid = 'cook:' + str(day)
    recipe = e['recipes'][p['business_recipe']]
    if phase == 0:
        enough = all(free(e, house, m) >= q for m, q in recipe['inputs'].items())
        if enough and not s['actors'][worker]['disabled']:
            add('business', 'commit_shift', person=worker, start=at+1, end=at+2, role='work:'+p['business_recipe'])
    if phase == 1:
        if [at, at+1, 'work:'+p['business_recipe']] in s['commitments'].get(worker, []):
            add('business', 'start_job', job_id=jid, recipe_id=p['business_recipe'], start=at, end=at+1, workers=[worker])
    if phase == 2 and jid in e['active_jobs']:
        add('business', 'complete_job', job_id=jid)
    if phase == 3:
        target = (day+1)*p['household_daily_meals']
        need = max(0, target-e['meals_delivered'].get(house, 0))
        qty = min(need, free(e, house, 'meal'))
        if qty: add('household', 'provision_meals', household=house, quantity=qty)
    if phase == 4 and jid in e['completed_jobs'] and not e['completed_jobs'][jid]['wages_accrued_for']:
        add('business', 'accrue_job_wages', job_id=jid, rate=1, wage_agreement_ref=p['authority_ref'])
    if phase == 0 and day % p['tax_period_days'] == 0:
        add('government', 'assess_tax', tax_id='tax:'+str(day), payer='farmer-b', amount=p['tax_amount'],
            authority_ref=p['authority_ref'], basis_ref=p['id'])
    if phase == 1:
        for tid, claim in e['tax_claims'].items():
            due = claim['assessed']-claim['paid']
            if due and s['cash'][claim['payer']] >= due:
                add('government', 'pay_tax', tax_id=tid, amount=due)
                break
    if phase == 0 and 'mobilization' not in s['gov']:
        add('military', 'authorize_mobilization', mandate=p['authority_ref'], target=p['army_target'])
    elif phase == 1 and 'mobilization' in s['gov'] and not s['actors']['farmer-a']['enlisted']:
        add('military', 'enroll', person='farmer-a')
    elif phase == 2 and s['actors']['farmer-a']['enlisted'] and not s['equipment'].get('farmer-a', {}).get('kit', 0):
        if s['equipment']['depot']['kit']:
            add('military', 'issue_kits', persons=['farmer-a'])
    return out

def advance(world, through_tick):
    if type(through_tick) is not int or through_tick < world.s['r8_strategy']['next_tick']:
        raise InvalidEvent('strategic horizon must be a forward integer tick')
    while world.s['r8_strategy']['next_tick'] < through_tick:
        old = world.s['r8_strategy']; tick = old['next_tick']
        if digest(old['profile']) != old['profile_hash']:
            raise InvalidEvent('selected strategic profile changed without prospective rebinding')
        candidate = R7World(state=world.s)
        reads, writes = set(), set()
        view = copy.deepcopy(candidate.s)
        events = proposals(Access(view, reads, writes), tick)
        if view != candidate.s: raise InvalidEvent('planner attempted state mutation')
        result = frontier(candidate, events)
        at = (tick//6)*24 + tick%6 + 1
        candidate.apply('r8:review:'+str(tick), at, 'review_no_change')
        candidate.s['r8_strategy']['decisions'].append({
            'tick': tick, 'at': at, 'policy_hash': old['profile_hash'], 'code_hash': code_identity(),
            'source_hash': digest(world.s), 'reads': sorted(reads), 'proposals': events,
            'committed': result['committed'], 'deferred': result['deferred'],
            'edges': result.get('edges', []), 'failures': result.get('failures', [])})
        candidate.s['r8_strategy']['next_tick'] = tick+1
        world.s = candidate.s
    return world
