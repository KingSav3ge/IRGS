"""Loopback web host for the existing IRGS AST engine. Standard library only."""
import argparse
import json
import secrets
import sys
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'IRGS_Core_Unification_CMRR_R9' / 'runtime'))
from ast_runtime import ASTWorld, AST_OPS, initial_ast
from irgs_reference import InvalidEvent


class Store:
    def __init__(self, folder):
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.lock = threading.RLock()

    def path(self, key):
        if not isinstance(key, str) or len(key) != 32 or any(c not in '0123456789abcdef' for c in key):
            raise ValueError('Invalid campaign ID')
        return self.folder / (key + '.json')

    def read(self, key):
        return json.loads(self.path(key).read_text(encoding='utf-8'))

    def write(self, record):
        path = self.path(record['id'])
        tmp = path.with_suffix('.tmp')
        tmp.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
        tmp.replace(path)

    def create(self, name):
        name = str(name).strip()
        if not name or len(name) > 100:
            raise ValueError('Use a campaign name between 1 and 100 characters')
        record = {'id': uuid.uuid4().hex, 'name': name, 'revision': 0, 'state': initial_ast().s}
        self.write(record)
        return record

    def listing(self):
        return [{k: r[k] for k in ('id', 'name', 'revision')} for r in
                (json.loads(p.read_text(encoding='utf-8')) for p in sorted(self.folder.glob('*.json')))]

    def event(self, key, revision, op, params):
        record = self.read(key)
        if revision != record['revision']:
            raise ValueError('This campaign changed in another tab. Reload before submitting again.')
        if op not in AST_OPS or not isinstance(params, dict):
            raise ValueError('Unsupported event')
        world = ASTWorld(state=record['state'])
        world.apply('web:' + uuid.uuid4().hex, world.s['clock'] + 1, op,
                    **{**params, 'campaign_id': 'AST'})
        record['state'] = world.s
        record['revision'] += 1
        self.write(record)
        return record


def make_server(port=8765, folder=None):
    store = Store(folder or ROOT / 'saves')
    token = secrets.token_urlsafe(32)

    class Handler(BaseHTTPRequestHandler):
        def reply(self, status, data, content_type='application/json'):
            raw = json.dumps(data, ensure_ascii=False).encode() if content_type == 'application/json' else data
            self.send_response(status)
            self.send_header('Content-Type', content_type + '; charset=utf-8')
            self.send_header('Content-Length', str(len(raw)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Content-Security-Policy', "default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self' data:; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
            self.end_headers()
            self.wfile.write(raw)

        def valid_host(self):
            return self.headers.get('Host') in {f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}'}

        def do_GET(self):
            if not self.valid_host():
                return self.reply(403, {'error': 'Local access only'})
            path = urlparse(self.path).path
            try:
                with store.lock:
                    if path == '/api/campaigns':
                        return self.reply(200, {'campaigns': store.listing(), 'token': token})
                    if path.startswith('/api/campaign/'):
                        return self.reply(200, store.read(path.rsplit('/', 1)[1]))
                files = {'/': ('index.html', 'text/html'), '/app.js': ('app.js', 'text/javascript'), '/style.css': ('style.css', 'text/css')}
                if path not in files:
                    return self.reply(404, {'error': 'Not found'})
                name, mime = files[path]
                self.reply(200, (ROOT / 'static' / name).read_bytes(), mime)
            except FileNotFoundError:
                self.reply(404, {'error': 'Campaign not found'})
            except ValueError as err:
                self.reply(400, {'error': str(err)})

        def do_POST(self):
            if not self.valid_host() or self.headers.get('X-IRGS-Token') != token:
                return self.reply(403, {'error': 'Reload the website to establish a local session'})
            if self.headers.get('Origin') not in (None, f'http://127.0.0.1:{self.server.server_port}', f'http://localhost:{self.server.server_port}'):
                return self.reply(403, {'error': 'Origin rejected'})
            try:
                length = int(self.headers.get('Content-Length', '0'))
                if not 0 < length <= 100000:
                    raise ValueError('Request is empty or too large')
                data = json.loads(self.rfile.read(length))
                with store.lock:
                    if self.path == '/api/create':
                        result = store.create(data['name'])
                    elif self.path == '/api/event':
                        result = store.event(data['id'], data['revision'], data['op'], data['params'])
                    elif self.path == '/api/fork':
                        original = store.read(data['id'])
                        result = {**original, 'id': uuid.uuid4().hex, 'name': original['name'][:85] + ' (branch)'}
                        store.write(result)
                    else:
                        return self.reply(404, {'error': 'Not found'})
                self.reply(200, result)
            except (InvalidEvent, ValueError, TypeError, KeyError, AssertionError, FileNotFoundError) as err:
                self.reply(400, {'error': str(err) or 'The engine rejected this event. Check the required references and values.'})

    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    return server


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('IRGS requires Python validation: do not launch with -O.')
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    server = make_server(args.port)
    print(f'IRGS ready at http://127.0.0.1:{server.server_port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
