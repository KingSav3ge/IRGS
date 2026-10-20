"""Isolated browser QA; never uses the live campaign directory."""
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WORKSPACE / 'IRGS_Web'))
from server import make_server

folder = Path(__file__).resolve().parent / 'browser_test_store'
server = make_server(8766, folder)
print('Isolated IRGS preview ready at http://127.0.0.1:8766/', flush=True)
try:
    server.serve_forever()
finally:
    server.server_close()
