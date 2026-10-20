"""Read-only access to packaged source content. Lookup grants no effects or rights."""
import hashlib,json
from pathlib import Path
from campaign_library import ROOT,catalog

IDENTIFIERS=('id','content_id','template_id','record_id','family_id','document_id','name','title','label')

def lookup(library_id,query='',limit=30):
    if type(limit) is not int or not 1<=limit<=100:raise ValueError('limit must be 1–100')
    libraries={x['id']:x for x in catalog()['content_libraries']}
    if library_id not in libraries:raise ValueError('Unknown content library')
    library=libraries[library_id];q=query.casefold();results=[]
    manifest=json.loads((ROOT/'catalog/source_manifest.json').read_text(encoding='utf-8'))
    # Manifest shape is built by build_suite_catalog.py; use its declared rows.
    rows=manifest.get('files',manifest.get('sources',manifest.get('source_files',[]))) if isinstance(manifest,dict) else manifest
    expected={r.get('path',r.get('file')):r.get('sha256') for r in rows if isinstance(r,dict)}
    def walk(value,path):
        if isinstance(value,dict):
            if any(k in value and isinstance(value[k],(str,int)) for k in IDENTIFIERS):
                text=json.dumps(value,ensure_ascii=False,sort_keys=True)
                if not q or q in text.casefold():
                    yield {'record_path':path,'identity':{k:value[k] for k in IDENTIFIERS if k in value and isinstance(value[k],(str,int))},
                           'source_status_fields':{k:v for k,v in value.items() if ('status' in k.casefold() or 'hold' in k.casefold()) and isinstance(v,(str,int,bool,type(None)))},
                           'excerpt':text[:3000],'truncated':len(text)>3000}
            for key,child in value.items():
                if isinstance(child,(dict,list)):yield from walk(child,path+[str(key)])
        elif isinstance(value,list):
            for index,child in enumerate(value):yield from walk(child,path+[str(index)])
    files=sorted(library['source_files'],key=lambda name:0 if name==library.get('registry_file') else 1)
    for name in files:
        path=(ROOT/name).resolve()
        if not path.is_relative_to(ROOT.resolve()):raise ValueError('Content path outside suite')
        if name not in expected:raise ValueError('Content file has no source-integrity record')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected[name]:raise ValueError('Content hash mismatch')
        if path.suffix.lower()=='.json':
            document=json.loads(path.read_text(encoding='utf-8-sig'))
            if library_id=='ast' and name==library.get('registry_file'):
                for spelling,cid in document.get('deprecated_spellings',{}).items():
                    if q==spelling.casefold():q=cid.casefold();break
            matches=list(walk(document,[]))
            def relevance(row):
                values=[str(v).casefold() for v in row['identity'].values()]
                return 0 if q and q in values else 1 if q and any(q in value for value in values) else 2
            for row in sorted(matches,key=relevance):
                results.append({'source_file':name,**row})
                if len(results)>=limit:break
        elif path.suffix.lower() in ('.md','.txt','.csv'):
            for number,line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
                if q and q not in line.casefold():continue
                if not line.strip():continue
                results.append({'source_file':name,'line':number,'excerpt':line[:3000]})
                if len(results)>=limit:break
        if len(results)>=limit:break
    return {'library_id':library_id,'source_status':library.get('source_status',library.get('status')),
            'lookup_creates_state':False,'numerical_models_adopted':False,'results':results}

def classify_record(library_id,query='',limit=30):
    """Catalogue compatibility name: return source classification, never effects."""
    return lookup(library_id,query,limit)
