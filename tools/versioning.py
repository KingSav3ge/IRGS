"""Coordinated edition metadata; Core and content versions remain independent."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def release_metadata(root=ROOT):
    document = json.loads((root / 'VERSION.json').read_text(encoding='utf-8'))
    if document.get('schema_version') != 1:
        raise ValueError('Unsupported edition metadata')
    for key in ('version', 'previous_version'):
        if not isinstance(document.get(key), str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?', document[key]):
            raise ValueError('Invalid edition ' + key)
    return document


def archive_name(root=ROOT):
    return 'IRGS_' + release_metadata(root)['version'].replace('.', '_') + '_Development.zip'
