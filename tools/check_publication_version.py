#!/usr/bin/env python3
"""IRGS unified-main pre-push guard; see VERSION_POLICY.md."""
import json,re,subprocess,sys

def version(value):
    found=re.fullmatch(r"(\d+)\.(\d+)(?:\.(\d+))?(?:-[A-Za-z0-9.-]+)?",value)
    if not found:
        raise ValueError("Invalid coordinated version")
    return tuple(int(number or 0) for number in found.groups())

def permitted(old,new):
    before,after=version(old['version']),version(new['version'])
    if old['version']==new['version']:
        return False
    if before[0]==3:
        if after==(4,0,0):
            return new.get('channel') in ('candidate','release-candidate','rc') and bool(new.get('candidate_assessment_ref'))
        if before[2]>9 or after[2]>9:
            return False
        expected=(3,before[1],before[2]+1) if before[2]<9 else (3,before[1]+1,0)
        return after==expected
    return after>=before

def load(commit):
    return json.loads(subprocess.check_output(['git','show',commit+':VERSION.json'],stderr=subprocess.PIPE))

def main():
    for line in sys.stdin:
        local_ref,local_oid,remote_ref,remote_oid=line.split()
        if remote_ref!='refs/heads/main' or set(remote_oid)=={'0'}:
            continue
        try:
            old,new=load(remote_oid),load(local_oid)
            if not permitted(old,new):
                raise ValueError('Every unified main push requires the next version; 3.4.0 -> 3.4.1, through 3.4.9 -> 3.5.0. A 4.0 candidate requires a recorded milestone assessment.')
            assessment=new.get('candidate_assessment_ref')
            if version(new['version'])==(4,0,0):
                if not isinstance(assessment,str) or assessment.startswith('/') or '..' in assessment.split('/'):
                    raise ValueError('Invalid candidate assessment reference')
                subprocess.check_output(['git','show',local_oid+':'+assessment],stderr=subprocess.PIPE)
        except (ValueError,KeyError,subprocess.CalledProcessError) as error:
            print('IRGS publication held: '+str(error),file=sys.stderr)
            print('QA reports remain local until included in a versioned coordinator publication.',file=sys.stderr)
            return 1
    return 0

if __name__=='__main__':
    raise SystemExit(main())
