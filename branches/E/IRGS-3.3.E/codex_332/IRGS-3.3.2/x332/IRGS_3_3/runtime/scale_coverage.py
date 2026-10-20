"""IRGS R4 proposed cross-scale interval provenance and read-only aggregation fixture.

Not a physical production engine. It proves source-exclusive view accounting
and requires resolved contributor sets; source operations are recorded once.
"""
from __future__ import annotations
import copy
from irgs_reference import canon, digest, InvalidEvent

class Coverage:
    def __init__(self, records=None):
        self.records=copy.deepcopy(records or {})

    def record(self, *, source_id, contributors, stream, start, end, quantity, evidence_ref):
        if not source_id or not evidence_ref or not isinstance(stream,str) or not stream:
            raise InvalidEvent('source, stream and evidence required')
        if type(start)!=int or type(end)!=int or start>=end or type(quantity)!=int or quantity<0:
            raise InvalidEvent('invalid measured interval or quantity')
        if not contributors or len(contributors)!=len(set(contributors)) or not all(isinstance(x,str) and x for x in contributors):
            raise InvalidEvent('resolved disjoint contributor identifiers required')
        item={'source_id':source_id,'contributors':sorted(contributors),'stream':stream,
              'start':start,'end':end,'quantity':quantity,'evidence_ref':evidence_ref}
        if source_id in self.records:
            if self.records[source_id]!=item:raise InvalidEvent('source ID replay altered')
            return False
        for old in self.records.values():
            if old['stream']==stream and set(old['contributors'])&set(contributors) and start<old['end'] and old['start']<end:
                raise InvalidEvent('overlapping coverage of same contributor and stream')
        self.records[source_id]=item
        return True

    def view(self,start,end,stream):
        """Never prorate ambiguous partial spans or mutate authoritative records."""
        if type(start)!=int or type(end)!=int or start>=end:raise InvalidEvent('invalid view bounds')
        included=[];partial=[]
        for rec in self.records.values():
            if rec['stream']!=stream or rec['end']<=start or rec['start']>=end:continue
            if start<=rec['start'] and rec['end']<=end:included.append(rec)
            else:partial.append(rec['source_id'])
        return {'start':start,'end':end,'stream':stream,
                'quantity_from_complete_intervals':sum(x['quantity'] for x in included),
                'source_ids':sorted(x['source_id'] for x in included),
                'unattributed_partial_sources':sorted(partial),
                'complete':not bool(partial)}

    def save(self):return canon(self.records)
    def checksum(self):return digest(self.records)
