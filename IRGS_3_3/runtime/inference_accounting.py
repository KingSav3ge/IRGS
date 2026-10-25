"""Explicit operator charge reconciliation; never campaign money or inference.

External billing evidence/units and operator authorization are trusted host
inputs. This module does not verify a provider bill or infer zero from failure.
It only records an immutable reviewed final charge and applies its budget effect.
"""
from dataclasses import asdict, dataclass
import json
import re
import time

from irgs_reference import canon
from solo_provider import nonempty, require


@dataclass(frozen=True)
class FinalCharge:
    attempt_id: str
    reconciliation_id: str
    charged_units: int
    price_revision: str
    evidence_ref: str
    evidence_sha256: str
    authority_ref: str
    final: bool = False


def _authorized(callback, *args):
    try:
        return callable(callback) and callback(*args) is True
    except Exception:
        return False


def reconcile(ledger, charge, *, authorize=None, clock=time.time):
    """Server-only operation; authorize checks the current Creator/operator session.

    A final charge uses the ledger's configured reservation units. Missing bill,
    unit/rate review or authorization must not be replaced with a guessed zero.
    Only a finished, nonprocessing attempt can be reconciled. Replays are exact;
    another final value cannot silently rewrite an earlier accounting decision.
    """
    require(isinstance(charge, FinalCharge) and charge.final is True, 'final_charge_required')
    require(_authorized(authorize,charge), 'operator_denied')
    require(all(nonempty(value) for value in (charge.attempt_id,charge.reconciliation_id,
        charge.price_revision,charge.evidence_ref,charge.authority_ref)), 'accounting_evidence_required')
    require(isinstance(charge.evidence_sha256,str) and
            re.fullmatch(r'[0-9a-f]{64}',charge.evidence_sha256) is not None, 'accounting_evidence_required')
    require(type(charge.charged_units) is int and 0 <= charge.charged_units <= 2**63-1, 'invalid_charge')
    payload=canon(asdict(charge))
    with ledger.connection() as db:
        db.execute('BEGIN IMMEDIATE')
        original=db.execute('SELECT payload FROM reconciliations WHERE attempt_id=? OR reconciliation_id=?',
                           (charge.attempt_id,charge.reconciliation_id)).fetchone()
        if original:
            require(original[0]==payload,'reconciliation_conflict')
            return json.loads(original[0])
        row=db.execute('SELECT status,finished,route_config FROM attempts WHERE id=?',
                       (charge.attempt_id,)).fetchone()
        require(row is not None,'unknown_request')
        require(row[0]!='processing' and row[1]==1,'attempt_in_doubt')
        require(row[2] is not None,'rate_provenance_unknown')
        config=json.loads(row[2])
        require(config['price_revision']==charge.price_revision,'rate_revision_mismatch')
        db.execute('INSERT INTO reconciliations VALUES (?,?,?,?,?)',
                   (charge.attempt_id,charge.reconciliation_id,charge.charged_units,payload,clock()))
    return json.loads(payload)


def budget_status(ledger, *, authorize=None):
    require(_authorized(authorize),'operator_denied')
    with ledger.connection() as db:
        ceiling=db.execute('SELECT budget FROM limits WHERE id=1').fetchone()[0]
        rows=db.execute('SELECT a.reserved,r.charged_units FROM attempts a'
                        ' LEFT JOIN reconciliations r ON a.id=r.attempt_id').fetchall()
    held=sum(reserved for reserved,charged in rows if charged is None)
    charged=sum(charged for _,charged in rows if charged is not None)
    unknown=sum(charged is None for _,charged in rows)
    return {'ceiling_units':ceiling,'held_units':held,'known_charged_units':charged,
            'unknown_attempts':unknown,'available_units':max(0,ceiling-held-charged),
            'overrun_units':max(0,held+charged-ceiling)}
