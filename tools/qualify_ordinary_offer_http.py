"""Reviewed optional fictional founder offer through the existing App HTTP host."""
import copy
import json
from pathlib import Path
import tempfile
import threading
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import ProxyHandler, Request, build_opener
from server import make_server, Store

with tempfile.TemporaryDirectory(prefix='irgs-offer-http-') as temporary:
    root=Path(temporary);store=Store(root/'saves')
    with patch('solo_provider.CapabilityBroker.dispatch',side_effect=AssertionError('provider called')), \
         patch('openai_proposals.OpenAIProposalTransport.__call__',side_effect=AssertionError('transport called')), \
         patch('http.server.BaseHTTPRequestHandler.log_message'):
        host=make_server(0,store.folder,reference_config=root/'no-personal-config.json',reference_cache=root/'cache',solo_configuration=None)
        thread=threading.Thread(target=host.serve_forever,daemon=True);thread.start()
        opener=build_opener(ProxyHandler({}));base='http://127.0.0.1:'+str(host.server_port);token=None
        def http(path,body=None):
            request=Request(base+path,headers={'Content-Type':'application/json',**({'X-IRGS-Token':token} if token else {})},data=None if body is None else json.dumps(body).encode())
            try:
                with opener.open(request,timeout=15) as reply:return reply.status,json.load(reply)
            except HTTPError as error:return error.code,json.load(error)
        try:
            code,session=http('/api/campaigns');assert code==200;token=session['token']
            choices={'template_id':'R00','founder_name':'Synthetic founder','household_name':'Synthetic home',
                'settlement_name':'Synthetic camp','region_name':'Greywater Reach','date_label':'Spring, Year 1',
                'company':'solo','permission':'seek','supplies':'basic','offer_profile':'founder-household-offer-v1'}
            code,review=http('/api/rise/preview',{'choices':choices});assert code==200,review
            assert 'no recipient consent' in review['offer_setup']['notice'] and not list(store.folder.glob('*.json'))
            body={'name':'Synthetic offer','choices':choices,'review_digest':review['review_digest'],'request_id':'offer-create'}
            code,created=http('/api/rise/create',body);assert code==200,created
            key=created['id'];saved=store.path(key).read_bytes();code,replay=http('/api/rise/create',body)
            assert code==200 and replay['id']==key and store.path(key).read_bytes()==saved
            state=store.read(key)['state'];stocks=copy.deepcopy(state['stocks']);elapsed=copy.deepcopy(state['elapsed_time'])
            code,view=http('/api/playthrough/'+key);assert code==200,view
            control=view['communication_control'];channel=next(c for c in control['channels'] if c['channel_id']=='commons-local')
            assert 'offer' in next(p for p in channel['participants'] if p['actor_id']=='oren')['supported_commands']
            terms={'from':'founder-home','to':'oren-home','material':'grain','quantity':1,'authority_id':'founder-household-offer'}
            attempt={'id':key,'actor':'founder','revision':view['revision'],'view_token':control['view_token'],
                'request_id':'offer-http','channel_id':'commons-local','recipient':'oren','command':'offer',
                'details':{'terms':terms},'intention':'I offer one portion of grain.'}
            code,prepared=http('/api/communication/prepare',attempt);assert code==200,prepared
            accept={'id':key,'actor':'founder','request_id':'offer-http','explicitly_accepted':True}
            code,result=http('/api/communication/execute',accept);assert code==200,result
            assert result['communication']['status']=='offered'
            saved=store.path(key).read_bytes();assert http('/api/communication/execute',accept)==(200,result)
            assert store.path(key).read_bytes()==saved
            state=Store(store.folder).read(key)['state'];assert state['stocks']==stocks and state['elapsed_time']==elapsed
            assert state['obligations'][result['communication']['offer_id']]['status']=='offered'
            print(json.dumps({'status':'PASS','ordinary_review_create_offer_retry_reload':True,'transfer':False,'npc_consent':False,'provider_calls':0}))
        finally:
            host.shutdown();host.server_close();thread.join(timeout=5)
