"""Read-only historical references and conditional-plan assessment.

This module never schedules, executes, advances time, installs plans, or decides
that a recorded historical outcome occurred in a campaign. Baseline truth,
prospective expectations and actual Core journal records remain distinct.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path

from temporal_registry import julian_day, validate_registry

CLASSIFICATIONS = {"documented", "design_inference", "authored_policy", "research_inference"}
TERMINAL = {"PREVENTED", "SUPERSEDED", "EXPIRED"}
PLAN_STATES = TERMINAL | {"UNASSESSED", "DATA_REQUIRED", "UNBOUND", "AT_RISK", "BLOCKED"}
RECORD_ROOTS = {"actors", "entity_registry", "evidence", "knowledge", "orders", "stocks",
                "capacities", "activities", "delegations", "obligations", "designs"}
ROOT = Path(__file__).resolve().parent.parent


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _canon(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def _hash(value):
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _refs(record, source_ids):
    refs = record.get("source_refs")
    _require(isinstance(refs, list) and refs and all(_text(ref) for ref in refs)
             and len(refs) == len(set(refs)) and set(refs) <= source_ids,
             "Every baseline assertion needs valid, unique source references")


def _classified(record, source_ids):
    _require(record.get("classification") in CLASSIFICATIONS, "Evidence classification is required")
    _refs(record, source_ids)


def _day(value):
    _require(isinstance(value, str) and re.fullmatch(r"[0-9]{4,}-[0-9]{2}-[0-9]{2}", value),
             "An exact date must use YYYY-MM-DD")
    return julian_day(*map(int, value.split("-")))


def _bounds(date):
    """Inclusive possible-day bounds, never a falsely precise occurrence date."""
    _require(isinstance(date, dict) and _text(date.get("calendar")), "A date needs an explicit calendar")
    precision = date.get("precision")
    _require(precision in {"day", "day_range", "month", "year", "unknown"}, "Unsupported date precision")
    if precision == "unknown" or date["calendar"] != "julian":
        return None
    start = date.get("start")
    if precision == "day":
        low = high = _day(start)
        _require(date.get("end") in (None, start), "A day cannot conceal a date range")
    elif precision == "day_range":
        low, high = _day(start), _day(date.get("end"))
    elif precision == "month":
        _require(isinstance(start, str) and re.fullmatch(r"[0-9]{4,}-[0-9]{2}", start), "Month precision needs YYYY-MM")
        year, month = map(int, start.split("-"))
        low = julian_day(year, month, 1)
        high = julian_day(year + (month == 12), 1 if month == 12 else month + 1, 1) - 1
        _require(date.get("end") is None, "Month precision cannot conceal a wider range")
    else:
        _require(isinstance(start, str) and re.fullmatch(r"[0-9]{4,}", start), "Year precision needs YYYY")
        year = int(start)
        low, high = julian_day(year, 1, 1), julian_day(year + 1, 1, 1) - 1
        _require(date.get("end") is None, "Year precision cannot conceal a wider range")
    _require(low <= high, "Date interval ends before it starts")
    return low, high


def validate_baseline(baseline):
    """Validate structure/provenance, without certifying historical truth."""
    _require(isinstance(baseline, dict) and type(baseline.get("schema_version")) is int
             and baseline["schema_version"] == 1, "Unsupported historical baseline schema")
    _require(_text(baseline.get("id")) and type(baseline.get("revision")) is int
             and baseline["revision"] >= 1, "Baseline identity and revision are required")
    _require(isinstance(baseline.get("scope"), dict) and _text(baseline["scope"].get("scenario_id")), "Baseline scope is required")
    sources, events = baseline.get("sources"), baseline.get("events")
    _require(isinstance(sources, list) and sources and isinstance(events, list), "Baseline sources and events are required")
    source_ids = set()
    for source in sources:
        _require(isinstance(source, dict) and _text(source.get("id")) and source["id"] not in source_ids
                 and _text(source.get("title")) and _text(source.get("url")), "Source identity/title/URL is invalid")
        source_ids.add(source["id"])
    event_ids = set()
    for event in events:
        _require(isinstance(event, dict) and _text(event.get("id")) and event["id"] not in event_ids
                 and _text(event.get("title")) and _text(event.get("description")), "Historical event identity is invalid")
        event_ids.add(event["id"])
    for event in events:
        bounds = _bounds(event.get("date"))
        _classified(event, source_ids)
        _require(event.get("research_status") in {"researched_reference", "proposed_research"}, "Explicit research status is required")
        outcome = event.get("historical_outcome_reference")
        _require(isinstance(outcome, dict) and _text(outcome.get("statement")), "Historical outcome must remain a reference assertion")
        _classified(outcome, source_ids)
        participants = event.get("participants", [])
        _require(isinstance(participants, list), "Participants must be reference records")
        for participant in participants:
            _require(isinstance(participant, dict) and _text(participant.get("entity_id")), "Participant needs a stable entity reference")
            _classified(participant, source_ids)
            if "validity" in participant:
                interval = _bounds(participant["validity"])
                if bounds and interval:
                    _require(max(bounds[0], interval[0]) <= min(bounds[1], interval[1]), "Participant identity interval cannot intersect this event")
        conditions = event.get("conditions", [])
        _require(isinstance(conditions, list), "Conditions must be explicitly authored records")
        condition_ids = set()
        for condition in conditions:
            _require(isinstance(condition, dict) and _text(condition.get("id")) and condition["id"] not in condition_ids
                     and _text(condition.get("type")) and condition.get("requirement") in {"hard", "supporting"}, "Condition identity/type/requirement is invalid")
            condition_ids.add(condition["id"])
            _classified(condition, source_ids)
            if condition["type"] in {"entity_exists", "entity_identity"}:
                _require(_text(condition.get("entity_id")), "Entity condition needs a stable identity")
            if condition["type"] == "entity_identity":
                _require(_text(condition.get("field")) and "expected" in condition, "Identity comparison must be explicit")
            if condition["type"] == "record_assertion":
                path = condition.get("path")
                _require(isinstance(path, list) and path and all(_text(p) or type(p) is int and p >= 0 for p in path)
                         and "expected" in condition, "Record assertion needs an exact path and expected value")
        dependencies = event.get("dependencies", [])
        _require(isinstance(dependencies, list), "Dependencies must be a list")
        seen = set()
        for dependency in dependencies:
            ref = dependency.get("event_id")
            _require(ref in event_ids and ref != event["id"] and ref not in seen
                     and dependency.get("requirement") in {"hard", "supporting"}, "Dependency reference is invalid")
            seen.add(ref)
            _classified(dependency, source_ids)
    graph = {event["id"]: [dep["event_id"] for dep in event.get("dependencies", [])] for event in events}
    done, visiting = set(), set()

    def visit(node):
        _require(node not in visiting, "Historical event dependencies contain a cycle")
        if node in done:
            return
        visiting.add(node)
        for dependency in graph[node]:
            visit(dependency)
        visiting.remove(node)
        done.add(node)

    for node in graph:
        visit(node)
    _canon(baseline)
    return True


def _state(world):
    state = world if isinstance(world, dict) else getattr(world, "s", None)
    _require(isinstance(state, dict) and _text(state.get("campaign_id")), "An actual campaign state is required")
    return state


def _cutoff(state):
    registry = state.get("entity_registry")
    if not isinstance(registry, dict) or registry.get("source_mode") != "playthrough":
        return {"status": "unbound", "reason": "No committed playthrough temporal registry"}
    validate_registry(registry, state.get("actors"))
    axis = registry["axis"]
    result = {"axis": copy.deepcopy(axis), "ordinal": registry["as_of"]}
    if axis.get("id") != "julian-day" or axis.get("calendar") != "julian" or axis.get("unit") != "day":
        return {**result, "status": "unbound", "reason": "No converter from this committed axis to baseline Julian dates"}
    return {**result, "status": "committed", "precision": "day", "same_day_order": "unknown"}


def _window_relation(date, cutoff):
    bounds = _bounds(date)
    if cutoff["status"] != "committed" or bounds is None:
        return "unknown"
    point = cutoff["ordinal"]
    return "past_reference" if bounds[1] < point else "future" if bounds[0] > point else "overlaps_cutoff"


def _baseline_ref(baseline):
    return {"id": baseline["id"], "revision": baseline["revision"], "sha256": _hash(baseline)}


def initialize_plans(baseline, world):
    """Return a prospective template; install nothing and replay no past events."""
    validate_baseline(baseline)
    state = _state(world)
    cutoff = _cutoff(state)
    matching = state.get("binding", {}).get("scenario_id") == baseline["scope"]["scenario_id"]
    result = {"schema_version": 1, "campaign_id": state["campaign_id"], "baseline_ref": _baseline_ref(baseline),
              "branch_id": state.get("branch_id"),
              "scope_status": "matching" if matching else "not_applicable", "cutoff": cutoff,
              "status": "preview_not_installed", "plans": [], "held_at_cutoff": [], "past_reference_ids": [],
              "simulation_writes": False, "execution_available": False, "calendar_execution_bound": False,
              "resolver_bound": False, "actual_occurrence_refs": [], "knowledge_scope": "creator_reference_only"}
    if not matching:
        return result
    for event in baseline["events"]:
        relation = _window_relation(event["date"], cutoff)
        if relation == "past_reference":
            result["past_reference_ids"].append(event["id"])
            continue
        record = {"id": "plan:" + state["campaign_id"] + ":" + event["id"], "campaign_id": state["campaign_id"],
                  "baseline_event_id": event["id"], "title": event["title"], "date": copy.deepcopy(event["date"]),
                  "window_relation": relation, "status": "UNASSESSED", "actual_occurrence_refs": []}
        result["plans" if relation == "future" else "held_at_cutoff"].append(record)
    return result


def validate_plan(plan, baseline, campaign_id=None):
    validate_baseline(baseline)
    _require(isinstance(plan, dict) and _text(plan.get("id")) and _text(plan.get("campaign_id")), "Plan identity and campaign scope are required")
    _require(campaign_id is None or plan["campaign_id"] == campaign_id, "Cross-campaign historical plan")
    _require(plan.get("baseline_event_id") in {event["id"] for event in baseline["events"]}, "Plan refers to a missing baseline event")
    _require(plan.get("status") in PLAN_STATES, "Unsupported plan state; a reference cannot certify an occurrence")
    if plan["status"] in TERMINAL:
        _require(_text(plan.get("change_ref")), "Terminal plan status requires an explicit source/decision reference")
    refs = plan.get("actual_occurrence_refs", [])
    _require(isinstance(refs, list) and all(_text(ref) for ref in refs) and len(refs) == len(set(refs)), "Occurrence links must be unique explicit journal references")
    _canon(plan)
    return True


def _condition(state, condition):
    record = {"id": condition["id"], "type": condition["type"], "requirement": condition["requirement"],
              "classification": condition["classification"], "result": "unknown", "reason": "Required binding is absent",
              "observed_refs": [], "missing_refs": [], "unsupported_refs": []}
    kind = condition["type"]
    if kind in {"entity_exists", "entity_identity"}:
        registry = state.get("entity_registry")
        ref = ["entity_registry", "entities", condition["entity_id"]]
        if not isinstance(registry, dict) or registry.get("source_mode") != "playthrough":
            record["missing_refs"].append(ref)
            return record
        validate_registry(registry, state.get("actors"))
        entity = registry["entities"].get(condition["entity_id"])
        if entity is None:
            record["missing_refs"].append(ref)
            return record
        version = next((v for v in reversed(entity["versions"]) if v["start"] <= registry["as_of"] and (v["end"] is None or registry["as_of"] < v["end"])), None)
        if version is None:
            record["missing_refs"].append(ref)
            return record
        record["observed_refs"].append({"path": ref, "as_of": registry["as_of"], "version_start": version["start"], "source_ref": version["source_ref"]})
        if not version["exists"]:
            record.update(result="unsatisfied", reason="The required identity does not exist at the committed point")
        elif kind == "entity_exists":
            record.update(result="satisfied", reason="Identity exists at the committed point; this grants no resources or authority")
        elif condition["field"] not in version["identity"] or version["identity"][condition["field"]] is None or condition["expected"] is None:
            record["missing_refs"].append(ref + ["identity", condition["field"]])
        else:
            same = _canon(version["identity"][condition["field"]]) == _canon(condition["expected"])
            record.update(result="satisfied" if same else "unsatisfied", reason="Exact dated identity comparison")
    elif kind == "record_assertion":
        path = condition["path"]
        if path[0] not in RECORD_ROOTS or any(isinstance(p, str) and p.startswith("__") for p in path):
            record["unsupported_refs"].append(copy.deepcopy(path))
            record["reason"] = "This path is outside the allowlisted live record owners"
            return record
        value = state
        try:
            for part in path:
                if isinstance(value, dict) and part in value:
                    value = value[part]
                elif isinstance(value, list) and type(part) is int:
                    value = value[part]
                else:
                    raise KeyError(part)
        except (KeyError, IndexError, TypeError):
            record["missing_refs"].append(copy.deepcopy(path))
            return record
        record["observed_refs"].append({"path": copy.deepcopy(path), "value_sha256": _hash(value)})
        if value is None or condition["expected"] is None:
            record["reason"] = "Unknown/null data cannot satisfy a causal condition"
            record["missing_refs"].append(copy.deepcopy(path))
            return record
        same = _canon(value) == _canon(condition["expected"])
        record.update(result="satisfied" if same else "unsatisfied", reason="Exact configured live-record comparison; no inferred causal completeness")
    else:
        record["unsupported_refs"].append(kind)
        record["reason"] = "No read-only condition adapter exists for this type"
    return record


def affected_plans(baseline, changed_event_ids):
    """Changed nodes plus descendants only; no global divergence percentage."""
    validate_baseline(baseline)
    ids = {event["id"] for event in baseline["events"]}
    _require(isinstance(changed_event_ids, (list, set, tuple)) and set(changed_event_ids) <= ids, "Unknown changed baseline event")
    affected = set(changed_event_ids)
    while True:
        added = {event["id"] for event in baseline["events"] if any(d["event_id"] in affected for d in event.get("dependencies", []))}
        if added <= affected:
            break
        affected.update(added)
    return sorted(affected)


def assess_plans(world, baseline, plans=None):
    """Assess present bindings; never treat missing data or a date as victory."""
    state = _state(world)
    initialized = initialize_plans(baseline, state)
    if plans is None:
        result = initialized
    else:
        _require(isinstance(plans, dict) and plans.get("campaign_id") == state["campaign_id"], "Cross-campaign plan collection")
        _require(plans.get("branch_id") == state.get("branch_id"), "Cross-branch plan collection")
        _require(plans.get("baseline_ref") == _baseline_ref(baseline), "Historical baseline edition/hash changed")
        _require(initialized["scope_status"] == "matching", "Historical plan belongs to another scenario")
        result = copy.deepcopy(plans)
        result.update(cutoff=initialized["cutoff"], simulation_writes=False, execution_available=False,
                      calendar_execution_bound=False, resolver_bound=False, status="preview_not_installed",
                      knowledge_scope="creator_reference_only")
        _require(isinstance(result.get("plans"), list) and isinstance(result.get("held_at_cutoff"), list), "Plan collection needs prospective and held lists")
    event_map = {event["id"]: event for event in baseline["events"]}
    seen, changed = set(), set()
    journal_ids = {event["id"] for event in state.get("journal", [])}
    all_refs = []
    for plan in result["plans"] + result["held_at_cutoff"]:
        validate_plan(plan, baseline, state["campaign_id"])
        _require(plan["id"] not in seen, "Duplicate campaign plan identity")
        seen.add(plan["id"])
        event = event_map[plan["baseline_event_id"]]
        relation = _window_relation(event["date"], result["cutoff"])
        plan.update(title=event["title"], date=copy.deepcopy(event["date"]), window_relation=relation)
        conditions = [_condition(state, condition) for condition in event.get("conditions", [])]
        unverified = event["research_status"] != "researched_reference" or event["classification"] != "documented"
        hard_false = any(c["result"] == "unsatisfied" and c["requirement"] == "hard" for c in conditions)
        soft_false = any(c["result"] == "unsatisfied" and c["requirement"] == "supporting" for c in conditions)
        unknown = not conditions or any(c["result"] == "unknown" for c in conditions)
        if plan["status"] in TERMINAL:
            status = plan["status"]
        elif hard_false:
            status = "BLOCKED"
        elif soft_false:
            status = "AT_RISK"
        elif unknown or unverified:
            status = "DATA_REQUIRED"
        else:
            status = "UNBOUND"
        if status in TERMINAL | {"BLOCKED", "AT_RISK"}:
            changed.add(event["id"])
        valid_refs = [ref for ref in plan.get("actual_occurrence_refs", []) if ref in journal_ids]
        missing_refs = [ref for ref in plan.get("actual_occurrence_refs", []) if ref not in journal_ids]
        all_refs.extend(valid_refs)
        plan["status"] = status
        plan["assessment"] = {"status": status, "conditions": conditions,
            "baseline_research_verified": not unverified, "historical_path_intact": None,
            "causal_completeness": "not_certified", "actual_outcome": None,
            "actual_occurrence_refs": valid_refs, "missing_occurrence_refs": missing_refs,
            "occurrence_link_note": "Explicit journal links only; no historical matching or outcome validation",
            "execution_available": False, "calendar_execution_bound": False, "resolver_bound": False,
            "reason": "Read-only assessment; no calendar-driven execution or historical outcome resolver"}
    affected = set(affected_plans(baseline, changed)) if changed else set()
    for plan in result["plans"] + result["held_at_cutoff"]:
        event_id = plan["baseline_event_id"]
        affected_by = sorted(parent for parent in changed if event_id in set(affected_plans(baseline, [parent])) - {parent})
        plan["assessment"]["dependency_reevaluation_required"] = bool(affected_by)
        plan["assessment"]["affected_by"] = affected_by
    result["affected_event_ids"] = sorted(affected)
    result["actual_occurrence_refs"] = list(dict.fromkeys(all_refs))
    result["note"] = "Past references are not replayed; future expectations are not actor knowledge, installed schedules, or actual occurrences."
    return copy.deepcopy(result)


def baseline_view(entry_id=None):
    """Creator-side reference loader; no active-campaign installation."""
    if entry_id is None or entry_id == 'hyw-1415':
        path = ROOT / 'data/hyw_historical_baseline.json'
    else:
        from historical_campaigns import SNAPSHOTS
        _require(entry_id in SNAPSHOTS, 'Unknown historical reference entry')
        path = ROOT / 'data/coc_conditional_references.json'
    baseline = json.loads(path.read_text(encoding='utf-8-sig'))
    if entry_id is not None and entry_id != 'hyw-1415':
        baseline['id'] += ':' + entry_id
        baseline['scope']['entry_id'] = entry_id
    validate_baseline(baseline)
    return baseline


def campaign_plan_view(world):
    state = _state(world)
    saved = state.get("historical_planning")
    if saved is None:
        report = assess_plans(state, baseline_view(state.get('historical_start', {}).get('entry_id')))
        report.update(storage="preview_only", baseline_source="current_reference_file", installed_schedule=False)
        return report
    _require(isinstance(saved, dict) and isinstance(saved.get("baseline_snapshot"), dict), "Saved historical reference needs its pinned baseline snapshot")
    # assess_plans verifies the source hash and campaign/branch scopes. It never
    # refreshes a saved edition from a newer disk baseline or writes into a save.
    report = assess_plans(state, saved["baseline_snapshot"], saved)
    report.pop("baseline_snapshot", None)
    report.update(storage="saved_prospective_reference", baseline_source="saved_baseline_snapshot", installed_schedule=False)
    return report


def fork_plan_reference(collection, new_campaign_id, origin_campaign_id):
    """Rebind an explicitly forked reference, preserving its edition and history.

    The caller owns actual campaign forking. This helper changes no world and
    creates no journal event; explicit occurrence links remain inherited links.
    """
    _require(isinstance(collection, dict) and collection.get("campaign_id") == origin_campaign_id,
             "Fork origin does not match this historical reference collection")
    _require(_text(new_campaign_id) and new_campaign_id != origin_campaign_id, "Fork needs a distinct new campaign identity")
    baseline = collection.get("baseline_snapshot")
    validate_baseline(baseline)
    _require(collection.get("baseline_ref") == _baseline_ref(baseline), "Fork source baseline edition/hash changed")
    _require(isinstance(collection.get("plans"), list) and isinstance(collection.get("held_at_cutoff"), list), "Fork needs valid plan lists")
    result = copy.deepcopy(collection)
    result["campaign_id"] = new_campaign_id
    for plan in result["plans"] + result["held_at_cutoff"]:
        validate_plan(plan, baseline, origin_campaign_id)
        plan["campaign_id"] = new_campaign_id
        plan["id"] = "plan:" + new_campaign_id + ":" + plan["baseline_event_id"]
    provenance = result.setdefault("fork_provenance", [])
    _require(isinstance(provenance, list), "Fork provenance must be a sequence")
    provenance.append({"origin_campaign_id": origin_campaign_id, "new_campaign_id": new_campaign_id,
                       "source_reference_sha256": _hash(collection),
                       "note": "Explicit reference fork; inherited journal links do not certify historical outcomes"})
    result.update(simulation_writes=False, execution_available=False, installed_schedule=False,
                  calendar_execution_bound=False, resolver_bound=False)
    return result
