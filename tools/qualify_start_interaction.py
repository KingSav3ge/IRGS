#!/usr/bin/env python3
"""Exercise new Engine starts through an explicitly selected existing App host.

This is HTTP/Engine contract evidence. It does not implement or qualify App mode
selection UI, and never changes App pins or historical Catalog consumer IDs.
"""
import argparse
from contextlib import ExitStack
import hashlib
import importlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import ProxyHandler, Request, build_opener

ROOT=Path(__file__).resolve().parents[1]
MODULES={}; SOURCES={}; EVIDENCE={}


def git(root,*args):
    return subprocess.check_output(['git','-C',str(root),*args],text=True).strip()


def initialize(app,catalog):
    app,catalog=app.resolve(),catalog.resolve()
    roots={'engine':ROOT,'app':app,'catalog':catalog}
    for owner,root in roots.items():
        clean=not git(root,'status','--porcelain')
        if owner!='engine' and not clean: raise ValueError('Select clean independent App/Catalog sources')
        SOURCES[owner]={'root':str(root),'commit':git(root,'rev-parse','HEAD'),'worktree_clean':clean}
    SOURCES['app']['committed_pins']={name:git(app,'rev-parse','HEAD:'+name) for name in ('Engine','Catalog')}
    os.environ['IRGS_ENGINE_ROOT']=str(ROOT/'IRGS_3_3')
    os.environ['IRGS_CATALOG_ROOT']=str(catalog/'IRGS_Catalog')
    sys.path[:0]=[str(app/'IRGS_Web'),str(ROOT/'IRGS_3_3/runtime'),str(catalog/'IRGS_Catalog')]
    for owner,names in {'app':('server','gameplay_views','local_presentation'),
        'engine':('core_world','starting_selection','start_readiness','historical_campaigns','scene_setup',
                  'scene_actions','shared_runtime','solo_provider','openai_proposals')}.items():
        for name in names:
            module=importlib.import_module(name)
            if not Path(module.__file__).resolve().is_relative_to(roots[owner]):
                raise ValueError('Import escaped selected source: '+name)
            MODULES[name]=module


class StartInteractionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='irgs-start-http-'); self.addCleanup(self.temp.cleanup)
        self.stack=ExitStack(); self.addCleanup(self.stack.close)
        self.broker=self.stack.enter_context(patch('solo_provider.CapabilityBroker.dispatch',side_effect=AssertionError('No provider calls')))
        self.transport=self.stack.enter_context(patch('openai_proposals.OpenAIProposalTransport.__call__',side_effect=AssertionError('No live transport')))
        self.stack.enter_context(patch('http.server.BaseHTTPRequestHandler.log_message'))
        self.server=MODULES['server']; self.store=self.server.Store(self.temp.name)
        self.host=self.server.make_server(0,self.store.folder,solo_configuration=None)
        self.thread=threading.Thread(target=self.host.serve_forever,daemon=True); self.thread.start()
        self.addCleanup(self.stop)
        self.url='http://127.0.0.1:'+str(self.host.server_port)
        self.opener=build_opener(ProxyHandler({}))
        self.token=self.http('/api/campaigns')[1]['token']
        preview=MODULES['historical_campaigns'].historical_entry('hyw-1415')
        self.selection={'profile_id':'military','scenario_id':'hundred-years-war',
                        'entry_id':'hyw-1415','snapshot_sha256':preview['snapshot_sha256']}
        status,self.options=self.http('/api/starting-options?'+urlencode(self.selection))
        self.assertEqual(status,200,self.options)

    def tearDown(self):
        self.broker.assert_not_called(); self.transport.assert_not_called()

    def stop(self):
        self.host.shutdown(); self.host.server_close(); self.thread.join(timeout=5)

    def http(self,path,body=None):
        request=Request(self.url+path,headers={'X-IRGS-Token':getattr(self,'token',''),'Content-Type':'application/json'},
                        data=None if body is None else json.dumps(body).encode())
        try:
            with self.opener.open(request,timeout=15) as reply: return reply.status,json.loads(reply.read())
        except HTTPError as error: return error.code,json.loads(error.read())

    def create(self,key,character):
        body={**self.selection,'name':'Synthetic '+key,'character':character,'selection_digest':self.options['selection_digest'],
              'request_id':'start-'+key,'mode':'player'}
        status,result=self.http('/api/create',body); self.assertEqual(status,200,result)
        return result['id'],body

    def view(self,key):
        status,view=self.http('/api/playthrough/'+key); self.assertEqual(status,200,view)
        return view

    def engine_view(self,key):
        world=MODULES['core_world'].CoreWorld(state=self.store.read(key)['state'])
        actor=world.s['player_actor_ids'][0]
        return MODULES['start_readiness'].actor_view(world,actor,branch_id=key,restore_id='synthetic-http-branch')

    def test_review_endpoint_distinguishes_readiness_without_creating_any_campaign(self):
        self.assertEqual(self.options['start_readiness']['schema_version'],'irgs-start-readiness-1')
        self.assertFalse(self.options['start_readiness']['reference_is_actor_knowledge'])
        people={r['id']:r for r in self.options['characters']}
        self.assertTrue(people['HYW-JOHN-BEDFORD']['eligible'])
        self.assertEqual(people['HYW-JOHN-BEDFORD']['start_modes'][0]['status'],'declaration_only')
        self.assertEqual([r['status'] for r in people['HYW-HENRY-V']['start_modes']],['declaration_only','supported_slice'])
        self.assertEqual(self.store.listing(),[])

    def test_henry_creation_core_observation_retry_and_continuation_through_actual_http(self):
        key,creation=self.create('henry',{'kind':'existing','actor_id':'HYW-HENRY-V','opening_id':'henry-1415-embarkation-v1'})
        self.assertEqual(self.http('/api/create',creation)[1]['id'],key)
        view=self.view(key); known=self.engine_view(key)
        self.assertEqual(known['current_mode'],'supported_slice'); self.assertEqual(known['civil_time']['date'],'1415-08-11')
        self.assertEqual(view['scene']['location'],'portchester-solent-embarkation')
        self.assertEqual(len(view['supported_actions']),1)
        self.assertEqual(self.store.read(key)['state']['stocks'],{})
        option=view['supported_actions'][0]
        body={'id':key,'actor':'HYW-HENRY-V','kind':'scene_action','action_id':option['action_id'],
              'revision':view['revision'],'request_id':'henry-observe','text':option['text']}
        code,result=self.http('/api/action',body); self.assertEqual(code,200,result)
        self.assertEqual(result['status'],'completed_successfully'); self.assertEqual(result['elapsed_time']['duration_seconds'],20)
        before=self.store.path(key).read_bytes()
        self.assertEqual(self.http('/api/action',body),(200,result))
        self.assertEqual(self.http('/api/action-result/'+key+'/henry-observe?actor_id=HYW-HENRY-V'),(200,result))
        self.assertEqual(self.store.path(key).read_bytes(),before)
        self.assertEqual(self.http('/api/action',{**body,'text':'Changed text'})[0],400)
        record=self.server.Store(self.temp.name).read(key)
        self.assertEqual(record['state']['elapsed_time']['seconds'],20)
        self.assertEqual(record['state']['stocks'],{})
        self.assertEqual(self.engine_view(key)['civil_time'],known['civil_time'])
        current=self.view(key)
        code,second=self.http('/api/action',{**body,'request_id':'henry-observe-again','revision':current['revision']})
        self.assertEqual(code,200,second)
        self.assertEqual(self.store.read(key)['state']['elapsed_time']['seconds'],40)
        self.assertEqual(self.http('/api/action-result/'+key+'/henry-observe?actor_id=HYW-HENRY-V'),(200,result))
        EVIDENCE['henry']={'created_from_http_review':True,'committed_observations':2,'selected_elapsed_seconds':40,
            'first_receipt_immutable':True,'save_reload':True,'retry_once':True,'stocks_created':0,
            'civil_precision':'day','civil_hour':None,'calendar_advanced':False}

    def test_default_john_new_default_and_authored_new_modes_remain_distinct(self):
        for name,character in (('john',{'kind':'existing','actor_id':'HYW-JOHN-BEDFORD'}),
            ('new-default',{'kind':'new','name':'Synthetic reader','species':'human'})):
            key,_=self.create(name,character); view=self.view(key)
            self.assertEqual(view['supported_actions'],[])
            self.assertEqual(self.engine_view(key)['current_mode'],'declaration_only')
            self.assertIsNone(view['scene']['location'])
        key,_=self.create('new-authored',{'kind':'new','name':'Synthetic courier','species':'human','opening_id':'quay-delivery-v1'})
        view=self.view(key); self.assertTrue(view['supported_actions'])
        self.assertEqual(self.engine_view(key)['current_mode'],'supported_slice')
        record=self.store.read(key)
        self.assertEqual(record['state']['stocks'][view['actor_id']]['sealed_dispatch'],1)
        EVIDENCE['mode_selection']={'existing_john':'declaration_only','new_default':'declaration_only',
                                    'new_authored':'supported_slice','existing_henry':'supported_slice'}


def qualify(app,catalog):
    initialize(app,catalog)
    log=io.StringIO(); result=unittest.TextTestRunner(stream=log,verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(StartInteractionTests))
    if not result.wasSuccessful() or result.skipped: raise RuntimeError(log.getvalue())
    return {'schema_version':1,'status':'PASS_START_CONTRACT_HTTP_WITH_LIMITS','date':'2026-10-26',
        'target_iteration':'IRGS 3.4.2 development','sources':SOURCES,
        'tests_run':result.testsRun,'passed':result.testsRun,'skipped':len(result.skipped),
        'evidence':EVIDENCE,'source_sha256':{str(Path(m.__file__).resolve()):hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest() for m in MODULES.values()},
        'qualification_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'provider_calls':0,'user_saves_used':False,'app_pins_changed':False,'catalog_fixture_identities_changed':False,
        'remaining':['App player mode selector and actor-known/civil-date presentation still need explicit adoption',
            'Current App HTTP observation uses its existing exact-listed-action route; general custom-intent mapping remains open',
            'Catalog new-schema consumer cases and coordinator exact-set browser/package qualification remain separate']}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app-root',required=True,type=Path); parser.add_argument('--catalog-root',required=True,type=Path)
    parser.add_argument('--output',type=Path); args=parser.parse_args()
    report=qualify(args.app_root,args.catalog_root)
    if args.output: args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({k:report[k] for k in ('status','tests_run','passed','skipped')}))
