"""Core 3.3 suite CLI. Campaign state, library lookup and synthetic verification."""
import argparse,json,uuid
from pathlib import Path
from campaign_library import catalog,initial_campaign
from core_world import CoreWorld
from content_library import lookup
from r9_runtime import frontier,grant,resolve

def save(w,path):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    temp=p.with_suffix(p.suffix+'.tmp');temp.write_text(w.save()+'\n',encoding='utf-8');temp.replace(p)
def load(path):return CoreWorld.load(Path(path).read_text(encoding='utf-8-sig'))
def status(w):
    return {'core':'3.3','campaign_id':w.s['campaign_id'],'binding':w.s.get('binding'),
            'clock':w.s['clock'],'actors':len(w.s['actors']),'events':len(w.s['journal']),
            'unresolved':[k for k,r in w.s.get('r9',{}).get('requests',{}).items() if r['status']=='unresolved'],
            'checksum':w.checksum()}
def main():
    p=argparse.ArgumentParser(description=__doc__);subs=p.add_subparsers(dest='command',required=True)
    subs.add_parser('catalog');subs.add_parser('verify')
    new=subs.add_parser('create');new.add_argument('--profile',default='ast');new.add_argument('--output',required=True)
    show=subs.add_parser('status');show.add_argument('--state',required=True)
    content=subs.add_parser('library');content.add_argument('library_id');content.add_argument('--query',default='');content.add_argument('--limit',type=int,default=10)
    event=subs.add_parser('frontier');event.add_argument('--state',required=True);event.add_argument('--events',required=True);event.add_argument('--output',required=True)
    strategy=subs.add_parser('strategy');strategy.add_argument('--days',type=int,default=7);strategy.add_argument('--output',required=True)
    a=p.parse_args()
    if a.command=='catalog':result=catalog()
    elif a.command=='verify':
        from release_integrity import verify_release
        r=verify_release();result={'release':r['release_id'],'status':'verified','core':'3.3'}
    elif a.command=='create':
        if Path(a.output).exists():raise ValueError('Existing save requires an explicit event, not reinitialization')
        w=initial_campaign(a.profile,campaign_id='IRGS-'+uuid.uuid4().hex);save(w,a.output);result=status(w)
    elif a.command=='status':result=status(load(a.state))
    elif a.command=='library':result=lookup(a.library_id,a.query,a.limit)
    elif a.command=='strategy':
        from strategic_execution import strategic_world,advance
        if a.days<1:raise ValueError('Positive day horizon required')
        w=advance(strategic_world(),a.days*6);save(w,a.output)
        result={'core':'3.3','profile':'explicit synthetic institutional policies','days':a.days,'checksum':w.checksum()}
    else:
        # Web envelopes belong to the serialized live host; the offline CLI
        # handles only explicit raw save files, never active host files.
        source=Path(a.state).resolve();out=Path(a.output).resolve()
        if source==out:raise ValueError('Use the live host for in-place writes; offline CLI writes a new file')
        if out.exists():raise ValueError('Output already exists')
        w=load(source);events=json.loads(Path(a.events).read_text(encoding='utf-8-sig'))
        result=frontier(w,events);save(w,out)
    print(json.dumps(result,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
