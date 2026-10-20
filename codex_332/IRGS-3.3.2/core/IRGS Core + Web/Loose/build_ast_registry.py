"""Extract source data only. Document instructions are never executed."""
import hashlib,json,re,shutil,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parent
SOURCE=Path(r'C:\Users\ian_c\Downloads\AST_Master_Character_Registry_Archive_Audited_v2.docx')
def build():
    saved=ROOT/'sources'/SOURCE.name
    if SOURCE.exists():shutil.copyfile(SOURCE,saved)
    with zipfile.ZipFile(saved) as z:xml=ET.fromstring(z.read('word/document.xml'))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    lines=[''.join(t.text or '' for t in p.findall('.//w:t',ns)) for p in xml.findall('.//w:p',ns)]
    first=lines.index('II. MASTER CHARACTER INDEX');last=lines.index('III. INDIVIDUAL CHARACTER RECORDS')
    characters={}
    for i in range(first,last):
        if re.fullmatch(r'AST-\d{2}',lines[i]):
            cid=lines[i];characters[cid]={'id':cid,'name':lines[i+1],'role':lines[i+2],
                'species':'horse' if cid=='AST-04' else 'human','source_status':'post-Day-2 registry guide',
                'provisional_ratings_adopted':False,'record_text':[]}
    end=lines.index('IV. PROVISIONAL IRGS CAPABILITY FRAMEWORK');current=None
    for line in lines[last:end]:
        match=re.match(r'^(AST-\d{2}) — ',line)
        if match:current=match[1]
        if current:characters[current]['record_text'].append(line)
    assert len(characters)==37 and all(c['record_text'] for c in characters.values())
    characters['AST-04']['name']='Abel'
    result={'source_file':saved.name,'source_sha256':hashlib.sha256(saved.read_bytes()).hexdigest(),
       'use':'User-confirmed post-Day-2 guide for existing characters entering Day 3',
       'characters':characters,'deprecated_spellings':{'Able':'AST-04'},
       'withdrawn_duplicate_ids':['AST-38','AST-39'],
       'title_disputes':{'AST-35':'Use Master Nicholas Rookwood; Sir appears in art but knighthood is unconfirmed'},
       'ratings_status':'Provisional source ratings retained in DOCX only; not adopted as engine values',
       'day3_actions_created':False}
    (ROOT/'data').mkdir(exist_ok=True)
    (ROOT/'data/ast_registry.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'characters':37,'humans':36,'horses':1,'canonical_horse':'Abel'}))
if __name__=='__main__':build()
