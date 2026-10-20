"""Campaign libraries initialize shared Core state; they are not simulators."""
import copy,json,uuid
from pathlib import Path
from core_world import CoreWorld
from historical_campaigns import prepare_opening, apply_opening
ROOT=Path(__file__).resolve().parent.parent

def catalog():
    path=ROOT/'data/catalog.json'
    if not path.exists():
        raise RuntimeError('Build the suite catalog before starting the live host')
    return json.loads(path.read_text(encoding='utf-8'))

def initial_campaign(profile_id='ast',campaign_id=None,*,scenario_id=None,entry_id=None,snapshot_sha256=None):
    profiles={p['id']:p for p in catalog()['campaign_profiles']}
    if profile_id not in profiles:raise ValueError('Unknown campaign profile')
    historical_selection=prepare_opening(profile_id,scenario_id,entry_id,snapshot_sha256)
    profile=profiles[profile_id]
    registry=json.loads((ROOT/'data/ast_registry.json').read_text(encoding='utf-8')) if profile_id=='ast' else {
        'characters':{},'deprecated_spellings':{},'withdrawn_duplicate_ids':[],
        'ratings_status':'No character ratings selected','title_disputes':{}}
    actors={cid:{'id':cid,'name':r['name'],'species':r['species'],'current':{},'registry_ref':cid}
            for cid,r in registry['characters'].items()}
    s={'profile':'IRGS-CORE-3.3','core_version':'3.3','campaign_id':campaign_id or ('AST' if profile_id=='ast' else 'IRGS-'+uuid.uuid4().hex),
        'binding':{'core':'3.3','genre_id':profile['genre_id'],'library_ids':copy.deepcopy(profile['library_ids']),
                   'campaign_profile':profile_id,'source_statuses_preserved':True},
        'player_actor_ids':['AST-01'] if profile_id=='ast' else [],'clock':0,
        'campaign_time':{'day':0,'time':None,'precision':'unresolved','phase':'Campaign setup; no events advanced'},
        'registry':registry,'actors':actors,'evidence':{},'knowledge':{},'orders':{},'stocks':{},'opening_stock':{},
        'obligations':{},'designs':{},'player_actions':[],'capacities':{},'activities':{},
        'journal':[],'processed':{},'pending':[]}
    if profile_id=='ast':
        s['campaign_time']={'day':2,'time':'approximately 21:45','precision':'approximate',
                           'phase':'post-Day-2 checkpoint; awaiting declared Day 3 events'}
        actors['AST-01']['current']={'location':'Lord Camoys household shared lodging, Southampton',
            'last_confirmed_activity':'asleep at the end of Day 2; no Day 3 action yet declared',
            'right_palm':'injured; cleaned and redressed, not established healed',
            'service':'personally accepted prospective squire; formal appointment and wages unresolved',
            'parental_letter':'unfinished and unsent'}
        actors['AST-04']['current']={'care':'Oswin Tanner; fed, watered and settled at end of Day 2',
            'tack':'existing saddle unsuitable for riding; held in storage by Oswin',
            'stall_catch':'temporary securing in place; permanent repair pending'}
        s['designs']['coopian']={'name':'Coopian Shield','status':'approved design draft','manufactured':False,
                               'source_ref':registry['source_sha256']}
    s=apply_opening(s,historical_selection)
    from starting_selection import initial_entity_registry
    s['entity_registry']=initial_entity_registry(s)
    return CoreWorld(state=s)

def presentation_binding(state):
    """Infer legacy AST presentation without modifying a persisted save."""
    if state.get('binding'):return copy.deepcopy(state['binding'])
    if state.get('profile')=='AST-CORE-3.3':
        return {'core':'3.3','genre_id':'military','library_ids':['shared','military','ast'],
                'campaign_profile':'ast','legacy_profile_alias':True}
    return {'core':'3.3','genre_id':None,'library_ids':[],'campaign_profile':None}
