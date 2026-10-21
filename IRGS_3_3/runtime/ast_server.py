"""Compatibility launcher: AST is a campaign library in the shared IRGS host."""
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'IRGS_Web'))
from server import make_server
from release_integrity import verify_release

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--port',type=int,default=8765)
    args=parser.parse_args();verify_release();server=make_server(args.port)
    print(f'IRGS Core 3.3 with AST campaign library: http://127.0.0.1:{server.server_port}',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:server.server_close()
