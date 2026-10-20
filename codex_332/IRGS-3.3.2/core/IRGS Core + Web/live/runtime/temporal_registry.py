"""Temporal identities, existence, relations and explicit control eligibility.

Calendar points are committed integer coordinates on an explicitly named axis.
They are never inferred from the Core causal sequence or a historical opening.
Templates are read-only sources; snapshots retain only evidence through a point.
"""
from __future__ import annotations

import copy
import json


ENTITY_OPS = {"register_entity", "transition_entity", "record_entity_relation",
              "record_entity_eligibility", "select_entity_control"}
KINDS = {"faction", "character", "conflict"}
RELATIONS = {"participation", "alliance", "rivalry", "vassalage", "affiliation"}
RELATION_STATUSES = {"active", "ended", "unknown", "disputed"}
SUPPORTED_POWERS = {"declare_own_intent"}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _point(value):
    return type(value) is int


def _ids(values, name):
    _require(isinstance(values, list) and all(_text(item) for item in values)
             and len(values) == len(set(values)), name + " must contain unique identities")
    return values


def julian_day(year, month, day):
    """Integer Julian-calendar civil-day ordinal (JDN convention), without time.

    Positive CE years only; no year zero, BCE or custom-calendar conversion is
    inferred. The returned integer does not establish a time of day.
    """
    _require(type(year) is int and year >= 1, "Julian year must be a positive CE integer")
    _require(type(month) is int and 1 <= month <= 12, "Julian month is invalid")
    lengths = (31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    _require(type(day) is int and 1 <= day <= lengths[month - 1], "Julian day is invalid")
    a = (14 - month) // 12
    y, m = year + 4800 - a, month + 12 * a - 3
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083


def _version_at(versions, point):
    for version in reversed(versions):
        if version["start"] <= point and (version["end"] is None or point < version["end"]):
            return version
    return None


def _entity_at(registry, entity_id, point):
    record = registry["entities"].get(entity_id)
    return _version_at(record["versions"], point) if record else None


def _exists(registry, entity_id, point):
    version = _entity_at(registry, entity_id, point)
    return bool(version and version["exists"])


def _versions(versions, reg, label):
    _require(isinstance(versions, list) and versions, label + " needs dated versions")
    previous = None
    for version in versions:
        _require(isinstance(version, dict) and _point(version.get("start")), label + " start must be an integer")
        end = version.get("end")
        _require(end is None or _point(end) and end >= version["start"], label + " interval is invalid")
        _require("end" in version and _text(version.get("source_ref")), label + " needs an explicit end and source")
        if previous is not None:
            _require(previous["end"] is not None and previous["end"] <= version["start"], label + " versions overlap or are unordered")
        if reg["source_mode"] == "playthrough":
            _require(version["start"] <= reg["as_of"] and (end is None or end <= reg["as_of"]),
                     "Playthrough registry cannot contain uncommitted future versions")
        previous = version


def _control(control, reg, point, actors, eligible, check_liveness=True):
    _require(isinstance(control, dict) and control.get("mode") in {"individual", "institutional"}, "Control mode is invalid")
    actor_ids = _ids(control.get("actor_ids"), "Control actors")
    powers = _ids(control.get("powers"), "Control powers")
    _require(set(powers) <= SUPPORTED_POWERS, "Unsupported control power; institutional mandates are separate")
    if eligible:
        _require(bool(actor_ids) and set(powers) == SUPPORTED_POWERS, "Playable eligibility requires actual actors and supported own-intent power")
    for actor_id in actor_ids:
        entity = reg["entities"].get(actor_id)
        _require(entity is not None and entity["kind"] == "character", "Control must reference an existing character identity")
        if eligible and check_liveness:
            _require(_exists(reg, actor_id, point), "Control actor does not exist at the policy's effective point")
        if actors is not None:
            _require(actor_id in actors, "Control actor is absent from authoritative Core actors")


def validate_registry(reg, actors=None):
    """Validate the whole registry without changing it or selecting control."""
    _require(isinstance(reg, dict) and type(reg.get("schema_version")) is int and reg["schema_version"] == 1, "Unsupported temporal registry schema")
    _require(reg.get("source_mode") in {"playthrough", "historical_template"}, "Registry source mode is invalid")
    axis = reg.get("axis")
    _require(isinstance(axis, dict) and _text(axis.get("id")) and _text(axis.get("unit")), "An explicit temporal axis and unit are required")
    _require("calendar" not in axis or axis["calendar"] is None or _text(axis["calendar"]), "Calendar identifier is invalid")
    _require(_point(reg.get("as_of")), "Registry as_of must be a committed integer point")
    for key in ("entities", "relations", "eligibility", "scenarios"):
        _require(isinstance(reg.get(key), dict), "Registry " + key + " must be an identity map")
    for entity_id, entity in reg["entities"].items():
        _require(_text(entity_id) and isinstance(entity, dict) and entity.get("id") == entity_id
                 and entity.get("kind") in KINDS, "Entity identity or kind is invalid")
        formed = entity.get("formed_at")
        _require(formed is None or _point(formed), "formed_at must be an explicit point or unknown/null")
        _versions(entity.get("versions"), reg, "Entity")
        for version in entity["versions"]:
            identity = version.get("identity")
            _require(type(version.get("exists")) is bool and isinstance(identity, dict) and _text(identity.get("name")), "Entity existence and name are required")
            _require("category" not in identity or _text(identity["category"]), "Entity category is invalid")
            _require("species" not in identity or _text(identity["species"]), "Entity species is invalid")
            for refs in ("territory_refs", "resource_refs"):
                _ids(version.get(refs, []), refs)
            _require(_text(version.get("resources_status", "uninitialized")), "Resource initialization status is invalid")
            if "leader_ids" in identity:
                for leader in _ids(identity["leader_ids"], "Entity leaders"):
                    _require(leader in reg["entities"] and reg["entities"][leader]["kind"] == "character", "Leader identity is not a registered character")
            for successor in _ids(version.get("successor_ids", []), "Successor references"):
                _require(successor in reg["entities"], "A successor reference cannot create a new entity")
            if formed is not None and version["exists"]:
                _require(formed <= version["start"], "Entity cannot exist before its sourced formation")
        if actors is not None and entity["kind"] == "character":
            _require(entity_id in actors, "Character identity is absent from authoritative Core actors")
    for scenario_id, scenario in reg["scenarios"].items():
        _require(_text(scenario_id) and isinstance(scenario, dict) and scenario.get("id") == scenario_id
                 and _text(scenario.get("title")) and type(scenario.get("character_creation_allowed")) is bool,
                 "Scenario identity and explicit creation policy are required")
        conflict = scenario.get("conflict_id")
        _require(conflict is None or conflict in reg["entities"] and reg["entities"][conflict]["kind"] == "conflict", "Scenario conflict identity is invalid")
    for relation_id, relation in reg["relations"].items():
        _require(_text(relation_id) and isinstance(relation, dict) and relation.get("id") == relation_id
                 and relation.get("type") in RELATIONS, "Relation identity or type is invalid")
        _require(relation.get("from_id") in reg["entities"] and relation.get("to_id") in reg["entities"], "Relation endpoints must exist as registered identities")
        _require(relation["from_id"] != relation["to_id"], "An entity cannot relate to itself through this interface")
        _versions(relation.get("versions"), reg, "Relation")
        for version in relation["versions"]:
            _require(version.get("status") in RELATION_STATUSES, "Relation status is invalid")
            if version["status"] == "active" and version["start"] != version["end"]:
                _require(_exists(reg, relation["from_id"], version["start"])
                         and _exists(reg, relation["to_id"], version["start"]), "Active relation endpoints do not exist at its effective point")
    policy_pairs = set()
    for key, policy in reg["eligibility"].items():
        _require(_text(key) and isinstance(policy, dict) and policy.get("entity_id") in reg["entities"]
                 and policy.get("scenario_id") in reg["scenarios"], "Eligibility requires existing entity and scenario identities")
        pair = (policy["entity_id"], policy["scenario_id"])
        _require(pair not in policy_pairs, "Eligibility has duplicate entity/scenario policies")
        policy_pairs.add(pair)
        _versions(policy.get("versions"), reg, "Eligibility")
        for version in policy["versions"]:
            _require(type(version.get("eligible")) is bool and _text(version.get("reason")), "Eligibility requires an explicit boolean and reason")
            _control(version.get("control"), reg, version["start"], actors, version["eligible"],
                     check_liveness=version["start"] != version["end"])
    try:
        json.dumps(reg, ensure_ascii=False, allow_nan=False)
    except (TypeError, ValueError) as err:
        raise ValueError("Temporal registry must contain finite JSON values") from err
    return True


def _query_point(reg, at):
    point = reg["as_of"] if at is None else at
    _require(_point(point), "Temporal query point must be an integer")
    _require(reg["source_mode"] != "playthrough" or point <= reg["as_of"], "Cannot query uncommitted playthrough future")
    return point


def _policy_at(reg, entity_id, scenario_id, point):
    for policy in reg["eligibility"].values():
        if policy["entity_id"] == entity_id and policy["scenario_id"] == scenario_id:
            return _version_at(policy["versions"], point)
    return None


def _participation(reg, entity_id, scenario, point):
    conflict = scenario.get("conflict_id")
    if conflict is None:
        return "unknown", [], "No conflict is configured for this scenario"
    if not _exists(reg, conflict, point):
        return "not_participating", [], "The selected conflict does not exist at this point"
    statuses, sources = [], []
    for relation in reg["relations"].values():
        if relation["type"] != "participation" or {relation["from_id"], relation["to_id"]} != {entity_id, conflict}:
            continue
        version = _version_at(relation["versions"], point)
        if version:
            statuses.append(version["status"])
            sources.append(version["source_ref"])
    status = ("participating" if "active" in statuses else "unknown" if not statuses or any(s in {"unknown", "disputed"} for s in statuses) else "not_participating")
    return status, list(dict.fromkeys(sources)), "Direct sourced participation relation only; affiliation does not imply participation"


def available_entities(reg, scenario_id="individual", at=None, kind=None):
    """Return current/past identity views; existence is not participation or control."""
    validate_registry(reg)
    point = _query_point(reg, at)
    _require(scenario_id in reg["scenarios"], "Unknown scenario")
    _require(kind is None or kind in KINDS, "Unknown entity kind")
    scenario = reg["scenarios"][scenario_id]
    factions, characters = [], []
    for entity_id, entity in sorted(reg["entities"].items()):
        version = _entity_at(reg, entity_id, point)
        if not version or not version["exists"] or entity["kind"] == "conflict" or kind is not None and entity["kind"] != kind:
            continue
        identity = version["identity"]
        policy = _policy_at(reg, entity_id, scenario_id, point)
        eligible = bool(policy and policy["eligible"])
        reason = policy["reason"] if policy else "No sourced eligibility policy is effective for this scenario"
        control = copy.deepcopy(policy["control"]) if policy else None
        if eligible and not all(_exists(reg, actor_id, point) for actor_id in control["actor_ids"]):
            eligible = False
            reason = "An authorized control actor no longer exists at this point; no successor is selected automatically"
        participation, participation_sources, participation_note = _participation(reg, entity_id, scenario, point)
        row = {"id": entity_id, "kind": entity["kind"], "name": identity["name"],
               "category": identity.get("category", entity["kind"]), "identity": copy.deepcopy(identity),
               "exists": True, "formed_at": entity.get("formed_at"),
               "territory_refs": copy.deepcopy(version.get("territory_refs", [])),
               "resource_refs": copy.deepcopy(version.get("resource_refs", [])),
               "resources_status": version.get("resources_status", "uninitialized"),
               "identity_effective_from": version["start"], "source_ref": version["source_ref"],
               "participation": participation, "participation_source_refs": participation_sources,
               "participation_note": participation_note, "eligible": eligible,
               "policy_eligible": bool(policy and policy["eligible"]), "eligibility_reason": reason,
               "eligibility_source_ref": policy["source_ref"] if policy else None, "control": control}
        (factions if entity["kind"] == "faction" else characters).append(row)
    return {"as_of": point, "axis": copy.deepcopy(reg["axis"]), "source_mode": reg["source_mode"],
            "scenario_id": scenario_id, "scenario": copy.deepcopy(scenario),
            "factions": factions, "characters": characters, "simulation_writes": False,
            "time_binding": "Explicit registry coordinate only; no elapsed time is inferred from the Core causal clock"}


def snapshot_registry(template, at):
    """Create a separate playthrough registry without future template knowledge."""
    validate_registry(template)
    _require(template["source_mode"] == "historical_template", "Only a historical template can seed a new snapshot")
    _require(_point(at), "Snapshot coordinate must be an integer")
    result = {"schema_version": 1, "source_mode": "playthrough", "axis": copy.deepcopy(template["axis"]),
              "as_of": at, "entities": {}, "relations": {}, "eligibility": {}, "scenarios": {}}

    def past_versions(versions):
        selected = []
        for version in versions:
            if version["start"] > at:
                continue
            item = copy.deepcopy(version)
            if item["end"] is not None and item["end"] > at:
                item["end"] = None
            selected.append(item)
        return selected

    for entity_id, entity in template["entities"].items():
        versions = past_versions(entity["versions"])
        if not versions or not any(version["exists"] for version in versions):
            continue
        selected = copy.deepcopy(entity)
        selected["versions"] = versions
        result["entities"][entity_id] = selected
    for entity in result["entities"].values():
        for version in entity["versions"]:
            if "leader_ids" in version["identity"]:
                version["identity"]["leader_ids"] = [i for i in version["identity"]["leader_ids"] if i in result["entities"]]
            if "successor_ids" in version:
                version["successor_ids"] = [i for i in version["successor_ids"] if i in result["entities"]]
    for scenario_id, scenario in template["scenarios"].items():
        if scenario.get("conflict_id") is None or scenario["conflict_id"] in result["entities"]:
            result["scenarios"][scenario_id] = copy.deepcopy(scenario)
    for relation_id, relation in template["relations"].items():
        versions = past_versions(relation["versions"])
        if versions and relation["from_id"] in result["entities"] and relation["to_id"] in result["entities"]:
            selected = copy.deepcopy(relation)
            selected["versions"] = versions
            result["relations"][relation_id] = selected
    for key, policy in template["eligibility"].items():
        versions = past_versions(policy["versions"])
        if versions and policy["entity_id"] in result["entities"] and policy["scenario_id"] in result["scenarios"]:
            for version in versions:
                _require(all(actor in result["entities"] for actor in version["control"]["actor_ids"]), "Eligibility includes a future control identity")
            selected = copy.deepcopy(policy)
            selected["versions"] = versions
            result["eligibility"][key] = selected
    validate_registry(result)
    return result


def _append_version(versions, version, point):
    if versions:
        previous = versions[-1]
        _require(previous["start"] <= point, "Cannot insert a version before existing history")
        _require(previous["end"] is None or previous["end"] <= point, "Existing history ends after this transition")
        if previous["end"] is None:
            previous["end"] = point
    versions.append(version)


def _close_lifecycle_references(reg, entity_id, point, source, sequence):
    """End effective references when an endpoint ceases to exist.

    Closing a sourced assertion is a direct lifecycle consequence. It grants no
    successor control and creates no replacement relation, actor or policy.
    Same-point earlier causal assertions remain as zero-width history.
    """
    records = [relation for relation in reg["relations"].values()
               if entity_id in (relation["from_id"], relation["to_id"])]
    records += [policy for policy in reg["eligibility"].values()
                if policy["entity_id"] == entity_id or any(
                    entity_id in version["control"]["actor_ids"]
                    for version in [_version_at(policy["versions"], point)] if version)]
    for record in records:
        current = _version_at(record["versions"], point)
        if current is not None:
            current["end"] = point
            current["end_source_ref"] = source
            current["end_recorded_sequence"] = sequence
            current["end_reason"] = "Referenced entity ceased to exist"


def operate_entity(world, s, at, op, p):
    """Apply one sourced operation inside the Core's existing atomic transaction.

    The registry's calendar point stays fixed. Core supplies its independent
    causal event sequence in ``at``; this function supplies no time-advance op.
    """
    _require(op in ENTITY_OPS, "Unsupported temporal entity operation")
    reg = s.get("entity_registry")
    _require(reg is not None, "A temporal registry must be explicitly configured")
    validate_registry(reg, s["actors"])
    _require(reg["source_mode"] == "playthrough", "Historical templates are read-only")
    point = p.get("effective_at")
    _require(_point(point) and point == reg["as_of"], "Entity mutation must use the registry's current committed coordinate")
    _require(_text(p.get("source_ref")), "A temporal operation needs a source reference")
    candidate = copy.deepcopy(reg)
    source = p["source_ref"]
    base = {"start": point, "end": None, "source_ref": source, "recorded_sequence": at}
    if op == "register_entity":
        entity_id, kind = p.get("entity_id"), p.get("kind")
        _require(_text(entity_id) and entity_id not in candidate["entities"] and kind in KINDS, "New entity identity and supported kind are required")
        identity = copy.deepcopy(p.get("identity"))
        _require(isinstance(identity, dict) and _text(identity.get("name")), "New entity needs a sourced name")
        if kind == "character":
            _require(entity_id in s["actors"] and identity["name"] == s["actors"][entity_id]["name"], "Character entity must match an existing Core actor identity")
        exists = p.get("exists", True)
        _require(type(exists) is bool, "Entity existence must be explicit boolean")
        candidate["entities"][entity_id] = {"id": entity_id, "kind": kind, "formed_at": p.get("formed_at"),
            "versions": [{**base, "exists": exists, "identity": identity,
                          "territory_refs": copy.deepcopy(p.get("territory_refs", [])),
                          "resource_refs": copy.deepcopy(p.get("resource_refs", [])),
                          "resources_status": p.get("resources_status", "uninitialized")}]}
    elif op == "transition_entity":
        entity_id = p.get("entity_id")
        _require(entity_id in candidate["entities"], "Cannot transition an unregistered entity")
        entity = candidate["entities"][entity_id]
        previous = _entity_at(candidate, entity_id, point)
        _require(previous is not None, "No identity version exists at this point")
        identity = copy.deepcopy(previous["identity"])
        if "identity" in p:
            _require(isinstance(p["identity"], dict), "Identity transition must be an object")
            identity.update(copy.deepcopy(p["identity"]))
        exists = p.get("exists", previous["exists"])
        _require(type(exists) is bool, "Entity existence must be explicit boolean")
        version = {**base, "exists": exists, "identity": identity}
        for refs in ("territory_refs", "resource_refs"):
            version[refs] = copy.deepcopy(p.get(refs, previous.get(refs, [])))
        version["resources_status"] = p.get("resources_status", previous.get("resources_status", "uninitialized"))
        if "successor_ids" in p:
            version["successor_ids"] = copy.deepcopy(p["successor_ids"])
        _append_version(entity["versions"], version, point)
        if previous["exists"] and not exists:
            _close_lifecycle_references(candidate, entity_id, point, source, at)
    elif op == "record_entity_relation":
        relation_id = p.get("relation_id")
        from_id, to_id = p.get("from_id"), p.get("to_id")
        relation_type = p.get("relation_type", p.get("type"))
        _require(_text(relation_id) and _text(from_id) and _text(to_id) and relation_type in RELATIONS and from_id != to_id,
                 "A relation needs a unique identity, distinct endpoints and supported type")
        _require(_exists(candidate, from_id, point) and _exists(candidate, to_id, point), "Current relation endpoints must actually exist")
        relation = candidate["relations"].get(relation_id)
        if relation is None:
            relation = {"id": relation_id, "from_id": from_id, "to_id": to_id, "type": relation_type, "versions": []}
            candidate["relations"][relation_id] = relation
        _require((relation["from_id"], relation["to_id"], relation["type"]) == (from_id, to_id, relation_type), "Relation identity cannot be reused for different endpoints or type")
        _append_version(relation["versions"], {**base, "status": p.get("status")}, point)
    elif op == "record_entity_eligibility":
        entity_id, scenario_id = p.get("entity_id"), p.get("scenario_id")
        _require(_exists(candidate, entity_id, point) and scenario_id in candidate["scenarios"], "Eligibility needs an existing entity and configured scenario")
        matches = [(key, value) for key, value in candidate["eligibility"].items()
                   if value["entity_id"] == entity_id and value["scenario_id"] == scenario_id]
        requested_key = p.get("eligibility_id", p.get("key"))
        key = requested_key or (matches[0][0] if matches else f"{scenario_id}:{entity_id}")
        _require(_text(key), "Eligibility identity is invalid")
        if matches:
            _require(key == matches[0][0], "The entity/scenario eligibility already has another identity")
        policy = candidate["eligibility"].get(key)
        if policy is None:
            policy = {"entity_id": entity_id, "scenario_id": scenario_id, "versions": []}
            candidate["eligibility"][key] = policy
        _require((policy["entity_id"], policy["scenario_id"]) == (entity_id, scenario_id), "Eligibility identity cannot be reused for another entity/scenario")
        control = copy.deepcopy(p.get("control"))
        if control is None and p.get("eligible") is False:
            control = {"mode": "individual" if candidate["entities"][entity_id]["kind"] == "character" else "institutional", "actor_ids": [], "powers": []}
        _control(control, candidate, point, s["actors"], p.get("eligible") is True)
        _append_version(policy["versions"], {**base, "eligible": p.get("eligible"), "reason": p.get("reason"), "control": control}, point)
    else:
        _require(_text(p.get("instruction_ref")), "Player control requires explicit user instruction")
        entity_id, scenario_id, actor_id = p.get("entity_id"), p.get("scenario_id"), p.get("actor_id")
        available = available_entities(candidate, scenario_id, point)
        row = next((item for item in available["factions"] + available["characters"] if item["id"] == entity_id), None)
        _require(row is not None and row["eligible"], "Entity is not currently eligible for this scenario")
        _require(actor_id in row["control"]["actor_ids"] and actor_id in s["actors"] and _exists(candidate, actor_id, point), "Choose an explicitly allowed actual control actor")
        selection = {"entity_id": entity_id, "scenario_id": scenario_id, "actor_id": actor_id,
                     "mode": row["control"]["mode"], "powers": copy.deepcopy(row["control"]["powers"]),
                     "source_ref": source, "instruction_ref": p["instruction_ref"], "effective_at": point,
                     "axis_id": candidate["axis"]["id"], "institutional_mandate_granted": False}
        s["player_actor_ids"] = [actor_id]
        s["starting_control"] = selection
        return
    validate_registry(candidate, s["actors"])
    s["entity_registry"] = candidate
