#!/usr/bin/env python3
"""Probe Engine readiness against real App boundaries without changing owners.

Exit 0 means the probed App boundaries agree; exit 2 records adoption blockers.
Neither outcome approves Catalog consumers, UI behavior, pins or a joined release.
Engine contract/assertion failures raise rather than being recorded as blockers.
"""
import argparse
from contextlib import ExitStack
import copy
import hashlib
import importlib
import json
from pathlib import Path
import sys
import tempfile
import threading
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import ProxyHandler, Request, build_opener

# Reuse exact-root import checks; no App or Catalog source is patched.
from qualify_start_interaction import initialize, MODULES, SOURCES


def inspect(app, catalog):
    initialize(app, catalog)
    catalog = catalog.resolve()
    fixture = importlib.import_module('player_start_evaluation')
    assert Path(fixture.__file__).resolve() == catalog/'IRGS_Catalog/player_start_evaluation.py'
    baseline = fixture.load_fixture(catalog/'IRGS_Catalog')
    # Evaluator/oracle data never enters actor input or a presentation packet.
    inputs = {key:fixture.export_actor_input(key,catalog/'IRGS_Catalog')
              for key in ('john-1415-existing','new-1415-default','new-1415-quay')}
    api = MODULES['start_readiness']; server = MODULES['server']
    core = MODULES['core_world'].CoreWorld
    cases = [(key, copy.deepcopy(value['selection']['character'])) for key,value in inputs.items()]
    cases += [('henry-default',{'kind':'existing','actor_id':'HYW-HENRY-V'}),
              ('henry-selected',{'kind':'existing','actor_id':'HYW-HENRY-V','opening_id':'henry-1415-embarkation-v1'})]
    checks=[]; contexts=[]; examples={}; app_result_example={}; request_count=0
    def check(case, finding, label, expected, actual):
        # Compare the public JSON contract: native capability source references
        # may be tuples, while the HTTP representation necessarily uses arrays.
        # Keep real field/value differences visible after wire normalization.
        expected=json.loads(json.dumps(expected,ensure_ascii=False))
        actual=json.loads(json.dumps(actual,ensure_ascii=False))
        checks.append({'case':case,'finding':finding,'check':label,
                       'expected':expected,'actual':actual,'passed':actual==expected})
    with tempfile.TemporaryDirectory(prefix='irgs-start-adoption-') as temporary, ExitStack() as stack:
        data=Path(temporary); store=server.Store(data/'saves')
        broker=stack.enter_context(patch('solo_provider.CapabilityBroker.dispatch',side_effect=AssertionError('No inference')))
        transport=stack.enter_context(patch('openai_proposals.OpenAIProposalTransport.__call__',side_effect=AssertionError('No transport')))
        stack.enter_context(patch('http.server.BaseHTTPRequestHandler.log_message'))
        host=server.make_server(0,store.folder,reference_config=data/'no-personal-config.json',reference_cache=data/'cache',solo_configuration=None)
        assert host.server_address[0]=='127.0.0.1'
        thread=threading.Thread(target=host.serve_forever,daemon=True); thread.start()
        opener=build_opener(ProxyHandler({})); base='http://127.0.0.1:'+str(host.server_port); token=None
        def http(path, body=None):
            nonlocal request_count
            request_count+=1
            request=Request(base+path,headers={'Content-Type':'application/json',**({'X-IRGS-Token':token} if token else {})},
                            data=None if body is None else json.dumps(body).encode())
            try:
                with opener.open(request,timeout=15) as reply:return reply.status,json.loads(reply.read())
            except HTTPError as error:return error.code,json.loads(error.read())
        try:
            code,session=http('/api/campaigns'); assert code==200; token=session['token']
            entry=MODULES['historical_campaigns'].historical_entry('hyw-1415')
            selection={'profile_id':'military','scenario_id':'hundred-years-war','entry_id':'hyw-1415',
                       'snapshot_sha256':entry['snapshot_sha256']}
            code,options=http('/api/starting-options?'+urlencode(selection)); assert code==200
            for key,character in cases:
                raw=importlib.import_module('campaign_library').initial_campaign(
                    'military','synthetic-review-'+key,scenario_id=selection['scenario_id'],
                    entry_id=selection['entry_id'],snapshot_sha256=selection['snapshot_sha256'])
                before=raw.save(); review=api.review_start(raw,character); assert raw.save()==before
                expected_mode='supported_slice' if key in ('new-1415-quay','henry-selected') else 'declaration_only'
                assert review['selected_mode']['status']==expected_mode
                fields={**selection,'selection_digest':options['selection_digest'],'starting_scenario_id':'individual',
                        'character_kind':character['kind']}
                fields.update({k:v for k,v in character.items() if k in ('actor_id','entity_id','species','opening_id')})
                saved_before={p.name:p.read_bytes() for p in store.folder.glob('*.json')}
                code,preview=http('/api/starting-preview?'+urlencode(fields))
                preview_status=code
                assert {p.name:p.read_bytes() for p in store.folder.glob('*.json')}==saved_before
                check(key,'START-INT-002','preflight_http',200,code)
                if code==200:
                    check(key,'START-INT-002','preflight_mode',expected_mode,preview.get('status'))
                # Independent backend probe. Success here never turns a failed
                # preflight into a playable normal-UI journey.
                body={**selection,'name':'Synthetic adoption '+key,'request_id':'adoption-'+key,
                      'character':character,'selection_digest':options['selection_digest'],'mode':'player'}
                code,created=http('/api/create',body); assert code==200,(key,created)
                campaign=created['id']; record=store.read(campaign); world=core(state=record['state'])
                actor=world.s['player_actor_ids'][0]
                engine_view=api.actor_view(world,actor,branch_id=campaign,restore_id='synthetic-adoption')
                code,view=http('/api/playthrough/'+campaign); assert code==200
                context=view.get('start_context')
                check(key,'START-INT-003','actor_start_schema',api.SCHEMA_VERSION,
                      context.get('schema_version') if isinstance(context,dict) else None)
                if isinstance(context,dict):
                    check(key,'START-INT-003','actor_start_owner',actor,context.get('actor_id'))
                    for field in ('selected_start','current_mode','capability_scope','supported_capabilities',
                                  'received_context','reference_is_actor_knowledge','templates_reapplied'):
                        check(key,'START-INT-003','actor_start_'+field,engine_view[field],context.get(field,'missing'))
                civil=context.get('civil_time') if isinstance(context,dict) else None
                check(key,'START-INT-003','received_initial_civil',engine_view['civil_time'],civil)
                assert engine_view['civil_time']['date']=='1415-08-11'
                assert engine_view['civil_time']['time'] is None
                assert 'state' not in view and 'historical_start' not in view
                expected_records=({'setup:civil-date','setup:scene-map','setup:scene-location'} if key=='henry-selected'
                    else {'setup:civil-date','setup:scene-map','setup:scene-location','setup:scene-activity','setup:scene-dispatch'}
                    if key=='new-1415-quay' else {'setup:civil-date'})
                assert set(world.s['knowledge'][actor])==expected_records
                evidence={'case':key,'mode':expected_mode,'preflight_http':preview_status,
                          'app_reports_engine_contract':preview.get('engine_start_context_contract'),
                          'backend_creation':True,'engine_received_civil':'1415-08-11',
                          'backend_observations':0,'elapsed_seconds':0}
                if key=='henry-selected':
                    assert world.s['stocks']=={} and world.s['orders']=={}
                    assert not world.s['starting_control']['institutional_mandate_granted']
                    check(key,'START-INT-003','scene_scope',world.s['scene_rules']['context_kind'],view['scene'].get('scope'))
                    blocks=(view.get('opening') or {}).get('blocks',[])
                    prompt='\n'.join(b.get('text','') for b in blocks if b.get('kind')=='first_decision')
                    check(key,'START-INT-003','legacy_courier_prompt',False,'move, observe or deliver the dispatch' in prompt)
                    option=next(o for o in view['supported_actions'] if o['action_id']=='observe-embarkation')
                    action={'id':campaign,'actor':actor,'revision':view['revision'],'request_id':'adoption-observe',
                            'kind':'scene_action','action_id':option['action_id'],'text':option['text']}
                    status,result=http('/api/action',action); assert status==200,result
                    assert result['status']=='completed_successfully' and result['elapsed_time']['duration_seconds']==20
                    check(key,'START-INT-003','committed_result_elapsed_axis',world.s['scene_rules']['elapsed_axis'],
                          result['elapsed_time'].get('axis'))
                    saved=store.path(campaign).read_bytes()
                    assert http('/api/action',action)==(200,result) and store.path(campaign).read_bytes()==saved
                    assert http('/api/action-result/'+campaign+'/adoption-observe?actor_id='+actor)==(200,result)
                    reloaded=core(state=server.Store(store.folder).read(campaign)['state'])
                    assert reloaded.s['stocks']=={} and reloaded.s['elapsed_time']['seconds']==20
                    code,after=http('/api/playthrough/'+campaign); assert code==200
                    check(key,'START-INT-003','received_selected_elapsed_seconds',20,
                          after['elapsed_time'].get('seconds') if isinstance(after.get('elapsed_time'),dict) else None)
                    assert store.path(campaign).read_bytes()==saved
                    evidence.update(backend_observations=1,elapsed_seconds=20,reload_and_exact_retry=True,
                                    preflight_http=preview_status)
                    examples={'character_selection':character,'precreation_review':review,'actor_start_context':engine_view,
                        'engine_receipt':MODULES['shared_runtime'].committed_receipt(reloaded,actor,result['receipt']['event_id'],
                            branch_id=campaign,restore_id='synthetic-adoption'),
                        'selected_core_elapsed_axis':reloaded.s['elapsed_time']['axis']}
                    app_result_example={'status':result['status'],'elapsed_time':result['elapsed_time'],
                                        'summary':result['outcome']['summary']}
                contexts.append(evidence)
            # R00 stays an independently selected existing Core slice. Only the
            # fixture setup's choices enter creation; no evaluator oracle is used.
            solo=importlib.import_module('solo_evaluation'); solo.validate_fixture()
            choices=json.loads((catalog/'IRGS_Catalog/evaluation/solo_r00_v1/evaluator_only/setup.json').read_bytes())['choices']
            setup=importlib.import_module('settlement_setup')
            code,rise=http('/api/rise/create',{'name':'Synthetic adoption R00','choices':choices,
                'review_digest':setup.preview(choices)['review_digest'],'request_id':'adoption-r00'})
            assert code==200,rise
            code,view=http('/api/playthrough/'+rise['id']); assert code==200
            assert view['play_readiness']['status']=='supported_slice'
            rise_input=fixture.export_actor_input('rise-r00',catalog/'IRGS_Catalog')
            for index,action in enumerate(rise_input['actions']):
                code,result=http('/api/rise/action',{'id':rise['id'],'actor':'founder','revision':view['revision'],
                    'action':action,'request_id':'adoption-r00-'+str(index)})
                assert code==200,result
                code,view=http('/api/playthrough/'+rise['id']); assert code==200
            assert store.read(rise['id'])['state']['elapsed_time']['seconds']==3900
            contexts.append({'case':'rise-r00','mode':'supported_slice','backend_actions':5,'elapsed_seconds':3900})
            broker.assert_not_called(); transport.assert_not_called()
        finally:
            host.shutdown(); host.server_close(); thread.join(timeout=5)
    failed=[c for c in checks if not c['passed']]
    app_preview=importlib.import_module('start_preview')
    assert Path(app_preview.__file__).resolve()==app.resolve()/'IRGS_Web/start_preview.py'
    manifest=catalog/'IRGS_Catalog/evaluation/player_starts_v1/manifest.json'
    return {'schema_version':1,'status':'BLOCKED_CONSUMER_ADOPTION' if failed else 'PROBED_APP_BOUNDARIES_AGREE_WITH_LIMITS',
        'date':'2026-10-26','target_iteration':'IRGS 3.4.2 development','sources':SOURCES,
        'engine_api_schema':api.SCHEMA_VERSION,'engine_product_reference':'cc450a6f00a249d2169cdacdfc9c4b1e03f67cc8',
        'http_requests':request_count,'contexts':contexts,'adoption_checks':checks,'failed_adoption_checks':len(failed),
        'blocking_app_findings':sorted({c['finding'] for c in failed}),
        'catalog_baseline':{'fixture_id':baseline['fixture_id'],'consumers':baseline['consumers'],
            'manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),
            'original_selection_changed':False,'new_contract_consumer_qualified_by_this_probe':False},
        'isolation_and_limits':{'user_saves_used':False,'app_or_catalog_patched':False,'pins_changed':False,
            'world_templates_reseeded_on_read':False,'provider_calls':0,'browser_or_package_approval':False},
        'source_sha256':{str(Path(m.__file__).resolve()):hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest()
            for m in [*MODULES.values(),fixture,app_preview]},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'henry_engine_call_example':examples,'observed_app_action_result':app_result_example,
        'remaining':['App owns START-INT-002/003/004 adoption and its exact pin update START-INT-005',
            'Catalog owns separately versioned new-contract selection/consumers START-INT-006',
            'This diagnostic is not the Catalog consumer runner or the coordinator all-three gate',
            'Travel expansion follows actual adoption; no new scenario or runtime rule is introduced']}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app-root',type=Path,required=True); parser.add_argument('--catalog-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True); args=parser.parse_args()
    report=inspect(args.app_root,args.catalog_root)
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({key:report[key] for key in ('status','http_requests','failed_adoption_checks','blocking_app_findings')}))
    sys.exit(2 if report['failed_adoption_checks'] else 0)
