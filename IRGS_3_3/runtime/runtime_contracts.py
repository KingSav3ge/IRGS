"""Provider-independent identities shared by supported campaign adapters.

These are host contracts, not campaign authorities or model input packets.
The trusted host authenticates actors and binds branch/restore identities.
"""
from dataclasses import asdict, dataclass
import json
import re


@dataclass(frozen=True)
class WorldScope:
    campaign_id: str
    branch_id: str
    restore_id: str
    state_digest: str

    def validate(self):
        if not all(isinstance(v, str) and v.strip() and len(v) <= 256
                   for v in (self.campaign_id, self.branch_id, self.restore_id)):
            raise ValueError('Invalid world scope')
        if not isinstance(self.state_digest, str) or not re.fullmatch('[0-9a-f]{64}', self.state_digest):
            raise ValueError('Invalid state identity')


@dataclass(frozen=True)
class ActionCapability:
    capability_id: str
    operation_id: str
    action_json: str
    title: str
    source_refs: tuple[str, ...]
    draft_family: str
    draft_values_json: str
    authored_intention: str

    def public(self):
        result = asdict(self)
        result['action'] = json.loads(result.pop('action_json'))
        result['draft_values'] = json.loads(result.pop('draft_values_json'))
        return result


@dataclass(frozen=True)
class AcceptedIntent:
    """Prepared exact text/action pair; execution still requires explicit True."""
    request_id: str
    scope: WorldScope
    actor_id: str
    intention: str
    capability_id: str
    operation_id: str
    action_json: str
    source_ref: str

    def validate(self):
        self.scope.validate()
        for value in (self.request_id, self.actor_id, self.capability_id, self.operation_id, self.source_ref):
            if not isinstance(value, str) or not value.strip() or len(value) > 256:
                raise ValueError('Invalid intent identity')
        if not isinstance(self.intention, str) or not self.intention.strip() or len(self.intention) > 4096:
            raise ValueError('Invalid exact intention')
        if not isinstance(self.action_json, str) or len(self.action_json) > 4096:
            raise ValueError('Invalid selected action')
        if not isinstance(json.loads(self.action_json), dict):
            raise ValueError('Invalid selected action')

    def to_json(self):
        self.validate()
        return json.dumps(asdict(self), sort_keys=True, ensure_ascii=False, separators=(',', ':'))

    @classmethod
    def from_json(cls, raw):
        def pairs(items):
            result = {}
            for key, value in items:
                if key in result:
                    raise ValueError('Duplicate intent field')
                result[key] = value
            return result
        data = json.loads(raw, object_pairs_hook=pairs)
        data['scope'] = WorldScope(**data['scope'])
        result = cls(**data)
        result.validate()
        return result
