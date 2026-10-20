"""Build the selected Core + genre + library release only from verified evidence."""
import hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'runtime'))
from r8_dependencies import code_identity
from core_world import CoreWorld,CORE_OPS
from ast_runtime import ASTWorld
from genre_receivers import GENRE_OPS

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name):return json.loads((ROOT/name).read_text(encoding='utf-8-sig'))
def write(name,value):
    path=ROOT/name;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def passed_log(name):
    text=(ROOT/name).read_text(encoding='utf-8-sig')
    assert re.search(r'^OK\s*$',text,re.M) and not re.search(r'^FAILED',text,re.M),name
    return int(re.search(r'Ran (\d+) test',text).group(1))

def preserved_path(record):
    path=ROOT.parent/record['path']
    if path.is_file():return path
    # Users may move a campaign between the active list and recoverable Trash.
    # That is a location change, not a lost or rewritten saved world.
    save_root=ROOT.parent/'IRGS_Web/saves'
    if path.is_relative_to(save_root):
        for candidate in (save_root/path.name,save_root/'trash'/path.name):
            if candidate.is_file():return candidate
    raise FileNotFoundError('Preserved campaign is absent from active saves and Trash: '+record['path'])

def build():
    matrix=read('results/r9_certification_matrix.json');scenario=read('results/r9_scenario_summary.json')
    catalogue=read('data/catalog.json');sources=read('catalog/source_manifest.json')
    assert matrix['tests_passed'] and matrix['observed_count']==matrix['operation_count']
    operations={row['operation']:row for row in matrix['operations']}
    assert all(row['status']=='PASS_OBSERVED_CASES' for row in operations.values())
    assert {row['example']['code'] for row in operations.values()}=={code_identity()},'certificates need current code'
    assert all('CoreWorld' in operations[op]['backends'] for op in CORE_OPS|GENRE_OPS)
    assert passed_log('results/r9_instrumented_tests.txt')==matrix['test_count']
    sustained=passed_log('results/sustained_unit_test.txt');http=passed_log('results/suite_http_tests.txt')
    http_log=(ROOT/'results/suite_http_tests.txt').read_text(encoding='utf-8-sig')
    assert http>=19 and all(name in http_log for name in (
        'test_delete_and_restore_preserve_exact_save_bytes',
        'test_campaign_trash_survives_http_server_restart',
        'test_stale_missing_and_invalid_trash_requests_preserve_saves',
        'test_restore_collision_preserves_active_and_trashed_campaigns',
        'test_delete_and_restore_require_local_token_host_and_origin')),'campaign deletion checks required'
    assert http >= 93, 'Current discovery, opening, role, creation and historical-reference checks required'
    ui = read('results/gameplay_ui_verification.json')
    assert ui['status'] == 'PASS' and ui['passed'] >= 22, 'Current integrated interface evidence required'
    for name, expected in ui['source_sha256'].items():
        assert sha(ROOT.parent/name)==expected, 'Solo interface evidence is stale: '+name
    stage1_tests = passed_log('results/stage1_backend_tests.txt')
    assert stage1_tests >= 12
    sys.path.insert(0, str(ROOT.parent/'IRGS_Web'))
    from features import content_library, feature_registry
    listing = content_library()
    assert [c['id'] for c in listing['campaigns']] == ['hundred-years-war']
    creator_features = feature_registry(mode='creator')['features']
    player_features = feature_registry(mode='player')['features']
    assert len(creator_features) >= 130 and len(player_features) < len(creator_features)
    reuse = read('data/ast_mechanics_reuse.json')
    assert reuse['standalone_ast_engine'] is False and reuse['standalone_campaign_maintenance'] is False
    assert sustained==1 and len(matrix['instrumentation_excludes'])==1
    assert scenario['save_resume_identical'] and scenario['days']==14 and scenario['committed_operations']==77
    assert scenario['meals_produced']==scenario['meals_consumed']==42
    assert len(catalogue['genre_engines'])==6 and len(catalogue['content_libraries'])==8 and len(catalogue['campaign_profiles'])==7
    assert 'ast' not in {g['id'] for g in catalogue['genre_engines']} and ASTWorld is CoreWorld
    for source in sources['files']:assert sha(ROOT/source['path'])==source['sha256'],source['path']
    # Receiving bindings must identify the actual kernel/receiver source bytes.
    for genre in catalogue['genre_engines']:
        binding=read(genre['receiving_binding'])
        for path,expected in binding['runtime_sources_sha256'].items():assert sha(ROOT/path)==expected,path
    registry=read('data/ast_registry.json')
    assert len(registry['characters'])==37 and registry['characters']['AST-04']['name']=='Abel'
    assert registry['deprecated_spellings']['Able']=='AST-04'
    preservation=[]
    for record in read('results/save_preservation_before.json'):
        current=preserved_path(record);backup=ROOT/record['backup']
        assert sha(current)==record['sha256']==sha(backup),'existing campaign save changed: '+record['path']
        preservation.append({**record,'current_path':current.relative_to(ROOT.parent).as_posix(),'after_sha256':sha(current),'unchanged':True})
    write('results/save_preservation_verified.json',preservation)
    historical=read('data/hyw_entry_catalogue.json');opening=read('data/hyw_1415_opening.json')
    assert len(historical['entries'])==37 and len(historical['featured_years'])==10
    assert opening['id']=='hyw-1415' and opening['opening']['date']=='1415-08-11'
    assert opening['opening']['calendar']=='julian' and opening['opening']['time'] is None
    for reference in read('data/hyw_design_references.json'):assert sha(ROOT/reference['path'])==reference['sha256']
    historical_tests=passed_log('results/hyw_runtime_tests.txt')
    update_preservation=[]
    for record in read('results/hyw_save_preservation_before.json'):
        current=preserved_path(record)
        assert sha(current)==record['sha256']==sha(ROOT/record['backup'])
        update_preservation.append({**record,'current_path':current.relative_to(ROOT.parent).as_posix(),'unchanged':True})
    write('results/hyw_save_preservation_verified.json',update_preservation)
    gameplay_preservation=[]
    for record in read('results/gameplay_save_preservation_before.json'):
        current=preserved_path(record)
        assert sha(current)==record['sha256']==sha(ROOT/record['backup'])
        gameplay_preservation.append({**record,'current_path':current.relative_to(ROOT.parent).as_posix(),
                                     'after_sha256':sha(current),'unchanged':True})
    write('results/gameplay_save_preservation_verified.json',gameplay_preservation)
    stage1_preservation=[]
    for record in read('results/stage1_save_preservation_before.json'):
        current=preserved_path(record)
        assert sha(current)==record['sha256']==sha(ROOT/record['backup'])
        stage1_preservation.append({**record,'current_path':current.relative_to(ROOT.parent).as_posix(),
                                   'after_sha256':sha(current),'unchanged':True})
    write('results/stage1_save_preservation_verified.json',stage1_preservation)
    notes=(ROOT/'SUITE_RELEASE.md').read_text(encoding='utf-8')
    prior=(ROOT/'IRGS_Core_Engine_v3_3_Unification_Candidate_R8.md').read_text(encoding='utf-8')
    core=ROOT/'Core/IRGS_Core_Engine_v3_3.md';core.parent.mkdir(exist_ok=True)
    core.write_text('# IRGS Core 3.3 selected local receiving edition\n\n'
        'Current selection and operational limits follow. The complete inherited rule baseline is retained afterwards; historical candidate labels describe their original scope. '
        'Unresolved profiles and numerical proposals remain unresolved unless explicitly selected.\n\n'
        +notes+'\n\n# Preserved complete rule baseline\n\n'+prior,encoding='utf-8')
    write('Core/IRGS_Core_3_3_Binding.json',{'document_id':'IRGS-CORE-3.3','status':'SELECTED_LOCAL_SUITE',
        'document':core.relative_to(ROOT).as_posix(),'sha256':sha(core),'ancestor':'IRGS-CORE-3.2',
        'source_owner_ids':['K-TIME','K-ACTOR','K-STOCK','K-ASSET','K-WORK','K-INFO','K-ORG','K-NET','K-POP'],
        'runtime':'core_world.CoreWorld','genre_bindings':[g['receiving_binding'] for g in catalogue['genre_engines']],
        'ast_classification':'campaign_library','automatic_numeric_adoption':False,'existing_save_migration':False})
    (ROOT/'README.md').write_text('# IRGS Core 3.3 live local suite\n\n'
        'Double-click `Start-IRGS-3.3.cmd` whenever you want to play. It starts IRGS in the background and opens '
        'http://127.0.0.1:8765, or reuses the running website. Codex need not be open. '
        'Keep `IRGS_3_3` beside `IRGS_Web`.\n\n'
        'Core 3.3 supplies the shared kernel. Six genre engines, eight technical libraries and seven installed profile adapters remain available internally. '
        'The player Content Library lists The Hundred Years’ War. A Scot’s Tale is a named 1415 starting reference; '
        'its reusable mechanics belong to shared Core/genre handlers, and its legacy adapter is archived.\n\n'
        'Read `SUITE_RELEASE.md` for exact capabilities and limits, `CMRR_3_3_Release.md` for reconciliation, '
        'and `results/completion_audit.json` for evidence. Existing campaign files are preserved, and library lookup advances no game state.\n\n'
        'Select a campaign and choose **Delete campaign** to move it to recoverable Trash. '
        'Use **Campaign Trash** to restore its complete save.\n\n'
        'The Content Library offers **The Hundred Years’ War**: ten featured years, all 37 supplied dates, '
        'and a developed 1415 opening. Other dates remain proposals. Later history is not scripted.\n',encoding='utf-8')
    with (ROOT/'README.md').open('a',encoding='utf-8') as readme:
        readme.write('\nSolo setup proceeds from campaign and entry through scenario, character and review before saving. '
            'Story, World and Chronicle share the same saved world. Historical selections have sourced briefings; '
            'date-aware faction and character availability follow the actual playthrough after initialization. '
            'Optional origin, family and career drafts are received player testimony, not automatic jobs, skills or resources. '
            'The historical comparison is read-only and never executes a future event. '
            'Freeform declarations are saved exactly; general narration and automatic calendar advancement are not implemented. '
            'Creator tools require explicit mode selection. Co-Op remains deferred.\n')
    fixed={}
    for folder in ('runtime','data','catalog','Core'):
        for path in sorted((ROOT/folder).rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix!='.pyc':fixed[path.relative_to(ROOT).as_posix()]=sha(path)
    for name in ('README.md','SUITE_RELEASE.md','CMRR_3_3_Release.md','DESIGN_INTEGRATION_2026_10_20.md','Start-IRGS-3.3.ps1','Start-IRGS-3.3.cmd','build_suite_catalog.py','build_release_3_3.py','package_release.py'):
        fixed[name]=sha(ROOT/name)
    host={}
    for name in ('server.py','features.py','opening_scene.py','gameplay_views.py','history_views.py','README.md','Start-IRGS.ps1','Start-IRGS.cmd'):
        path=ROOT.parent/'IRGS_Web'/name;host['IRGS_Web/'+name]=sha(path)
    for folder in ('static','tests'):
        for path in sorted((ROOT.parent/'IRGS_Web'/folder).rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix!='.pyc':host[path.relative_to(ROOT.parent).as_posix()]=sha(path)
    validation={'runtime_tests':matrix['test_count']+sustained,'instrumented_tests':matrix['test_count'],
        'separate_sustained_test':sustained,'http_tests':http,'observed_operations':matrix['observed_count'],
        'common_operations':len(CORE_OPS),'campaign_native_receivers':len(GENRE_OPS),'strategy_days':14,
        'campaign_deletion':'Recoverable Trash with exact-byte restore, revision and collision checks',
        'historical_opening_tests':historical_tests,'historical_catalogue_entries':37,'developed_historical_openings':1,
        'solo_interface_checks':ui['passed'],'player_mode':'Server-filtered Solo projection',
        'character_before_first_save':True,'temporal_entity_operations':5,
        'easy_launch':'On-demand background host and browser; running IRGS reused',
        'player_campaign_listings':1,'feature_routes_creator':len(creator_features),'feature_routes_player':len(player_features),
        'stage1_backend_checks':stage1_tests,'structured_background_status':'Received player testimony only',
        'historical_plan_assessment':'Read-only, pinned reference edition; no executable historical schedule',
        'general_action_resolution':False,'full_stage_one_gameplay_gate':'UNMET: actual resolved interaction and autonomous reaction remain unconnected',
        'certification_scope':'Current code, executed cases and named profile backends; not all native effects or every branch'}
    release={'release_id':'IRGS-CORE-3.3-SUITE','version':'3.3','selected_core':'3.3','scope':'CORE_GENRES_LIBRARIES',
        'status':'SELECTED_LOCAL_SUITE','host':'IRGS_Web','port':8765,'genre_count':6,'library_count':8,'campaign_profiles':7,
        'ast_is_engine':False,'ast_role':'named_1415_start_reference_with_archived_legacy_adapter',
        'content_edition':'DESIGN-PATCH-2026-10-20',
        'historical_settings':[{'id':'hundred-years-war','profile_id':'military','catalogue_entries':37,'featured_entries':10,'developed_entries':['hyw-1415']}],
        'selection_authority':'User requested live Core 3.3 plus genre engines/libraries, with AST as campaign content',
        'validation':validation,'files_sha256':fixed,'host_sha256':host,'existing_save_migration':False}
    write('release.json',release)
    audit={'status':'OFFLINE_REQUIREMENTS_VERIFIED','release_id':release['release_id'],'code_identity':code_identity(),
        'requirements':{'core_kernel':'PASS','six_genre_bindings':'PASS','eight_content_libraries':'PASS','ast_campaign_library':'PASS',
            'supported_full_path_observations':'PASS','durable_resolution':'PASS','institution_observations_and_rights':'PASS',
            'strategic_checkpoint_parity':'PASS','launch_interface_http':'PASS','recoverable_campaign_deletion':'PASS','existing_save_preservation':'PASS',
            'historical_catalogue_37_entries':'PASS','sourced_1415_opening':'PASS','historical_update_save_preservation':'PASS',
            'solo_character_before_first_save':'PASS','filtered_player_views':'PASS','declaration_retry_safety':'PASS',
            'shared_temporal_entity_registry':'PASS','playthrough_availability_not_historical_reset':'PASS',
            'chronicle_scoped_retrieval':'PASS','gameplay_update_save_preservation':'PASS','solo_interface_checks':'PASS',
            'one_campaign_discovery':'PASS','exact_entry_launch_propagation':'PASS','authorized_feature_routes':'PASS',
            'actor_known_opening_presentation':'PASS','independent_background_and_career_testimony':'PASS',
            'read_only_historical_plan_assessment':'PASS','ast_named_start_and_mechanics_reuse':'PASS',
            'patch_update_save_preservation':'PASS'},
        'validation':validation,'source_files_verified':len(sources['files']),'preserved_existing_saves':len(preservation),
        'live_activation':'PENDING_VERIFIED_LAUNCH','remaining_certification_limits':catalogue['certification_limits'],
        'historical_evidence_gap':catalogue['missing_historical_evidence']}
    write('results/completion_audit.json',audit)
    print(json.dumps({'release':release['release_id'],**validation,'source_files':len(sources['files']),'preserved_saves':len(preservation)}))
if __name__=='__main__':build()
