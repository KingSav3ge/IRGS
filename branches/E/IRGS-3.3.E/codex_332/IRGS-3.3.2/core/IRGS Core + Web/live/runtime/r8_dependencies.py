"""Proposed R8 snapshot-specific access evidence, not an arbitrary-plugin sandbox."""
import ast
import copy
from collections.abc import MutableMapping
from pathlib import Path
from irgs_reference import World, InvalidEvent, digest
from r7_frontier import R7World
from economic_extension import ECON_OPS

def core_operations():
    tree = ast.parse(Path(__file__).with_name('irgs_reference.py').read_text())
    method = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == '_operate')
    return {n.value for c in ast.walk(method) if isinstance(c, ast.Compare)
            and isinstance(c.left, ast.Name) and c.left.id == 'op'
            for n in ast.walk(c) if isinstance(n, ast.Constant) and isinstance(n.value, str)} | set(ECON_OPS)

SUPPORTED = core_operations()
BOOKKEEPING = {'clock', 'processed', 'journal'}

class Access(MutableMapping):
    """Negative lookups, scans and list access are dependencies too.

    Container navigation uses an existence marker; enumeration reads the whole
    subtree. Existing handlers mutate raw lists, so list access reserves the
    entire list for both read and write, conservatively.
    """
    def __init__(self, data, reads, writes, path=()):
        self.data, self.reads, self.writes, self.path = data, reads, writes, path
    def __getitem__(self, key):
        path = self.path + (str(key),)
        self.reads.add(path + ('@exists',))
        value = self.data[key]
        if isinstance(value, dict):
            return Access(value, self.reads, self.writes, path)
        self.reads.add(path)
        if isinstance(value, list): self.writes.add(path)
        return value
    def __setitem__(self, key, value):
        self.writes.add(self.path + (str(key),))
        self.data[key] = copy.deepcopy(value)
    def __delitem__(self, key):
        self.writes.add(self.path + (str(key),))
        del self.data[key]
    def __iter__(self):
        self.reads.add(self.path)
        return iter(self.data)
    def __len__(self):
        self.reads.add(self.path)
        return len(self.data)
    def setdefault(self, key, default=None):
        try: return self[key]
        except KeyError:
            self[key] = default
            return self[key]
    def __deepcopy__(self, memo):
        self.reads.add(self.path)
        return copy.deepcopy(self.data, memo)

def changed(a, b, path=()):
    if isinstance(a, dict) and isinstance(b, dict):
        out = set()
        for key in a.keys() | b.keys():
            p = path + (str(key),)
            if key not in a or key not in b: out.add(p)
            else: out.update(changed(a[key], b[key], p))
        return out
    return {path} if a != b else set()

def domain(s):
    return {k: v for k, v in s.items() if k not in BOOKKEEPING}

def code_identity():
    import hashlib
    return digest({p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted(Path(__file__).parent.glob('*.py'))
                   if not p.name.startswith(('test_', 'run_'))})

def observe(state, event):
    if event['op'] not in SUPPORTED:
        raise InvalidEvent('uncertified handler: explicit serial execution required')
    if event['id'] in state['processed']:
        raise InvalidEvent('already processed event cannot be certified again')
    reads, writes = set(), set()
    scratch = copy.deepcopy(state)
    World._operate(None, Access(scratch, reads, writes), event['at'],
                   event['op'], copy.deepcopy(event['params']))
    actual = (R7World if 'econ3' in state else World)(state=state)
    actual.apply(event['id'], event['at'], event['op'], **event['params'])
    if domain(scratch) != domain(actual.s):
        raise InvalidEvent('untraced adapter-side effects: certification refused')
    writes.update(changed(domain(state), domain(actual.s)))
    return {'event': copy.deepcopy(event), 'snapshot': digest(state),
            'code': code_identity(), 'reads': sorted(reads), 'writes': sorted(writes)}

def overlaps(a, b):
    a, b = tuple(a), tuple(b)
    return a[:len(b)] == b or b[:len(a)] == a

def conflicts(a, b):
    return any(overlaps(x, y) for x in a['writes'] for y in b['reads'] + b['writes']) or any(
        overlaps(x, y) for x in b['writes'] for y in a['reads'])

def frontier(world, events, certificates=None):
    """Atomic selective commit; no lexical winners, no cached footprint trust."""
    if not events: return {'committed': [], 'deferred': [], 'certificates': []}
    if len({e['id'] for e in events}) != len(events) or len({e['at'] for e in events}) != 1:
        raise InvalidEvent('unique IDs and one causal frontier required')
    certs, failed = [], []
    for event in events:
        try: certs.append(observe(world.s, event))
        except (InvalidEvent, AssertionError, KeyError, ValueError, TypeError) as error:
            failed.append({'event': copy.deepcopy(event), 'reason': str(error)})
    if failed:
        return {'committed': [], 'deferred': copy.deepcopy(events), 'failures': failed, 'certificates': certs}
    if certificates is not None and certificates != certs:
        raise InvalidEvent('stale, altered or wrong-code certificate')
    blocked, edges = set(), []
    for i, left in enumerate(certs):
        for j in range(i):
            if conflicts(left, certs[j]):
                blocked.update((i, j)); edges.append([left['event']['id'], certs[j]['event']['id']])
    candidate = type(world)(state=world.s)
    committed = []
    for i, cert in enumerate(certs):
        if i in blocked: continue
        e = cert['event']
        candidate.apply(e['id'], e['at'], e['op'], **e['params'])
        committed.append(e['id'])
    candidate._validate(candidate.s)
    world.s = candidate.s
    return {'committed': committed, 'deferred': [copy.deepcopy(events[i]) for i in sorted(blocked)],
            'edges': edges, 'certificates': certs}
