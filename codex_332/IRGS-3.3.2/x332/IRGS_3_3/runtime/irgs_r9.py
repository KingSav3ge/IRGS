"""Local CLI for proposed R9. All inputs/outputs are explicit candidate save files."""
import argparse
import json
from pathlib import Path
from r7_frontier import R7World
from r9_adapters import ReceiverWorld
from r9_strategy import strategic_world, advance
from r9_runtime import resolve
from ast_runtime import ASTWorld, initial_ast

def load(path):
    s=json.loads(Path(path).read_text(encoding='utf-8-sig'))
    return (ASTWorld if s.get('profile') in ('AST-CORE-3.3','IRGS-CORE-3.3') else ReceiverWorld if 'r9_engine_bindings' in s else R7World)(state=s)

def save(world,path):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(world.save()+'\n',encoding='utf-8');tmp.replace(path)

def status(w):
    if w.s.get('profile') in ('AST-CORE-3.3','IRGS-CORE-3.3'):
        return {'release':'IRGS Core 3.3 suite','selected_core':'3.3','campaign_id':w.s['campaign_id'],
            'checkpoint':w.s['campaign_time'],'registered_characters':len(w.s['actors']),
            'canonical_horse':w.s['actors'].get('AST-04',{}).get('name'),'checksum':w.checksum(),
            'events':len(w.s['journal']),'invented_day3_actions':False}
    e=w.s['econ3'];r=w.s.get('r9',{})
    return {'release':'Core 3.3 synthetic verification profile','selected_core':'3.3','clock':w.s['clock'],
            'checksum':w.checksum(),'population':w.display_population()['total'],
            'cash_total':sum(w.s['cash'].values()),'meals_produced':e['produced']['meal'],
            'unresolved_requests':[k for k,v in r.get('requests',{}).items() if v['status']=='unresolved']}

def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    demo=sub.add_parser('demo');demo.add_argument('--days',type=int,default=7);demo.add_argument('--output',required=True)
    resume=sub.add_parser('advance');resume.add_argument('--state',required=True);resume.add_argument('--through-day',type=int,required=True);resume.add_argument('--output',required=True)
    show=sub.add_parser('status');show.add_argument('--state',required=True)
    decision=sub.add_parser('resolve');decision.add_argument('--state',required=True);decision.add_argument('--decision',required=True);decision.add_argument('--output',required=True)
    args=parser.parse_args()
    if getattr(args,'output',None) and Path(args.output).exists():
        parser.error('Output exists. Use the serialized live host for in-place campaign changes.')
    if args.command=='demo':
        if args.days<1:parser.error('days must be positive')
        w=advance(strategic_world(),args.days*6);save(w,args.output)
    elif args.command=='advance':
        w=advance(load(args.state),args.through_day*6);save(w,args.output)
    elif args.command=='resolve':
        w=load(args.state);request=json.loads(Path(args.decision).read_text(encoding='utf-8-sig'))
        resolve(w,**request);save(w,args.output)
    else:w=load(args.state)
    print(json.dumps(status(w),indent=2))

if __name__=='__main__':main()
