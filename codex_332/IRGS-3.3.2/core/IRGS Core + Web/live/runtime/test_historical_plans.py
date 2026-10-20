"""Synthetic plan assessments; no event executor or historical replay fixture."""
import copy
import json
import unittest
from unittest.mock import patch

from historical_plans import (affected_plans, assess_plans, baseline_view, campaign_plan_view,
                              fork_plan_reference, initialize_plans, validate_baseline, validate_plan)
from temporal_registry import julian_day


SOURCE = "synthetic-test-source"


def condition(key="ready", kind="record_assertion", **fields):
    return {"id": key, "type": kind, "requirement": "hard", "classification": "design_inference",
            "source_refs": [SOURCE], **fields}


def event(key, date="1415-09-01", conditions=None, dependencies=None):
    return {"id": key, "title": "Synthetic " + key, "description": "A synthetic historical-reference assertion",
            "date": {"calendar": "julian", "precision": "day", "start": date},
            "classification": "documented", "research_status": "researched_reference", "source_refs": [SOURCE],
            "historical_outcome_reference": {"statement": "Synthetic reference outcome, not a simulation occurrence",
                "classification": "documented", "source_refs": [SOURCE]},
            "participants": [], "conditions": conditions or [condition(path=["evidence", "ready", "status"], expected="established")],
            "dependencies": dependencies or []}


def dependency(key, requirement="hard"):
    return {"event_id": key, "requirement": requirement,
            "classification": "design_inference", "source_refs": [SOURCE]}


def baseline():
    a = event("a", conditions=[condition("exists", "entity_exists", entity_id="hero"),
                              condition(path=["evidence", "ready", "status"], expected="established")])
    b = event("b", "1415-09-02", dependencies=[dependency("a")])
    c = event("c", "1415-09-03")
    same = event("same", "1415-08-11")
    past = event("past", "1415-08-10")
    overlap = event("overlap")
    overlap["date"] = {"calendar": "julian", "precision": "month", "start": "1415-08"}
    return {"schema_version": 1, "id": "synthetic-baseline", "revision": 1,
            "scope": {"scenario_id": "test-history"}, "sources": [
                {"id": SOURCE, "title": "Synthetic fixture evidence", "url": "fixture:synthetic"}],
            "events": [a, b, c, same, past, overlap]}


def world(campaign_id="TEST-CAMPAIGN"):
    point = julian_day(1415, 8, 11)
    actors = {"hero": {"id": "hero", "name": "Alice", "species": "human", "current": {}}}
    return {"campaign_id": campaign_id, "clock": 999999,
            "binding": {"scenario_id": "test-history"}, "actors": actors,
            "evidence": {"ready": {"status": "established"}}, "knowledge": {}, "journal": [],
            "historical_start": {"date": "1415-08-11"},
            "entity_registry": {"schema_version": 1, "source_mode": "playthrough",
                "axis": {"id": "julian-day", "unit": "day", "calendar": "julian"}, "as_of": point,
                "entities": {"hero": {"id": "hero", "kind": "character", "versions": [
                    {"start": point, "end": None, "exists": True, "identity": {"name": "Alice"}, "source_ref": SOURCE}]}},
                "relations": {}, "eligibility": {}, "scenarios": {
                    "individual": {"id": "individual", "title": "Individual", "character_creation_allowed": True}}}}


def find(report, event_id):
    return next(p for p in report["plans"] + report["held_at_cutoff"] if p["baseline_event_id"] == event_id)


class BaselineValidationTests(unittest.TestCase):
    def test_real_partial_baseline_has_three_sourced_1415_anchors(self):
        value = baseline_view()
        self.assertEqual(len(value["events"]), 3)
        self.assertEqual({e["date"]["start"] for e in value["events"]},
                         {"1415-09-18", "1415-09-22", "1415-10-25"})
        self.assertTrue(validate_baseline(value))
        self.assertTrue(all(c["classification"] == "design_inference" for e in value["events"] for c in e["conditions"]))
        self.assertNotIn("1453", value["scope"])

    def test_duplicate_ids_missing_sources_dangling_dependencies_and_cycles_rejected(self):
        changes = [lambda b: b["events"].append(copy.deepcopy(b["events"][0])),
                   lambda b: b["events"][0].update(source_refs=["missing"]),
                   lambda b: b["events"][0].update(dependencies=[dependency("missing")]),
                   lambda b: b["events"][0].update(dependencies=[dependency("b")]),
                   lambda b: b.update(schema_version=True),
                   lambda b: b["events"][0]["conditions"][0].update(classification="fact-because-history")]
        for change in changes:
            value = baseline()
            change(value)
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_baseline(value)

    def test_date_precision_and_identity_intervals_are_validated(self):
        for date in ({"calendar": "julian", "precision": "day", "start": "1415"},
                     {"calendar": "julian", "precision": "day_range", "start": "1415-09-02", "end": "1415-09-01"},
                     {"calendar": "julian", "precision": "day", "start": "1415-02-29"},
                     {"calendar": "julian", "precision": "month", "start": "1415-13"}):
            value = baseline()
            value["events"][0]["date"] = date
            with self.subTest(date=date), self.assertRaises(ValueError):
                validate_baseline(value)
        value = baseline()
        value["events"][0]["participants"] = [{"entity_id": "future-person", "classification": "documented", "source_refs": [SOURCE],
            "validity": {"calendar": "julian", "precision": "year", "start": "1500"}}]
        with self.assertRaises(ValueError):
            validate_baseline(value)


class InitializationTests(unittest.TestCase):
    def test_only_after_cutoff_becomes_prospective_same_day_and_overlap_held(self):
        report = initialize_plans(baseline(), world())
        self.assertEqual([p["baseline_event_id"] for p in report["plans"]], ["a", "b", "c"])
        self.assertEqual([p["baseline_event_id"] for p in report["held_at_cutoff"]], ["same", "overlap"])
        self.assertEqual(report["past_reference_ids"], ["past"])
        self.assertEqual(report["status"], "preview_not_installed")
        self.assertEqual(report["actual_occurrence_refs"], [])
        self.assertFalse(report["execution_available"])

    def test_range_and_year_precision_do_not_invent_an_occurrence_day(self):
        value = baseline()
        value["events"][0]["date"] = {"calendar": "julian", "precision": "day_range", "start": "1415-08-10", "end": "1415-08-12"}
        value["events"][1]["date"] = {"calendar": "julian", "precision": "year", "start": "1415"}
        value["events"][2]["date"] = {"calendar": "julian", "precision": "year", "start": "1416"}
        report = initialize_plans(value, world())
        self.assertEqual(find(report, "a")["window_relation"], "overlaps_cutoff")
        self.assertEqual(find(report, "b")["window_relation"], "overlaps_cutoff")
        self.assertEqual(find(report, "c")["window_relation"], "future")

    def test_no_registry_or_custom_axis_cannot_use_opening_or_causal_clock(self):
        for change in (lambda w: w.pop("entity_registry"),
                       lambda w: w["entity_registry"]["axis"].update(calendar="custom", unit="cycle"),
                       lambda w: w["entity_registry"]["axis"].update(id="campaign-relative-day"),
                       lambda w: w["entity_registry"].update(source_mode="historical_template")):
            state = world()
            change(state)
            report = initialize_plans(baseline(), state)
            self.assertEqual(report["cutoff"]["status"], "unbound")
            self.assertEqual(report["plans"], [])
            self.assertTrue(report["held_at_cutoff"])
            self.assertEqual(report["past_reference_ids"], [])

    def test_current_committed_date_overrides_old_opening_and_never_replays_past(self):
        state = world()
        state["entity_registry"]["as_of"] = julian_day(1415, 9, 2)
        report = initialize_plans(baseline(), state)
        self.assertIn("a", report["past_reference_ids"])
        self.assertEqual(find(report, "b")["window_relation"], "overlaps_cutoff")
        self.assertEqual([p["baseline_event_id"] for p in report["plans"]], ["c"])
        self.assertEqual(state["journal"], [])

    def test_other_campaign_scenario_is_not_applicable(self):
        state = world()
        state["binding"]["scenario_id"] = "another-history"
        report = assess_plans(state, baseline())
        self.assertEqual(report["scope_status"], "not_applicable")
        self.assertEqual(report["plans"], [])


class AssessmentTests(unittest.TestCase):
    def test_all_predicates_true_still_cannot_execute_or_certify_a_victory(self):
        report = assess_plans(world(), baseline())
        plan = find(report, "a")
        self.assertEqual(plan["status"], "UNBOUND")
        self.assertTrue(all(c["result"] == "satisfied" for c in plan["assessment"]["conditions"]))
        self.assertIsNone(plan["assessment"]["historical_path_intact"])
        self.assertIsNone(plan["assessment"]["actual_outcome"])
        self.assertEqual(plan["actual_occurrence_refs"], [])
        self.assertFalse(report["execution_available"])

    def test_missing_binding_is_unknown_never_intact(self):
        state = world()
        state["evidence"] = {}
        plan = find(assess_plans(state, baseline()), "a")
        self.assertEqual(plan["status"], "DATA_REQUIRED")
        self.assertEqual(plan["assessment"]["conditions"][1]["result"], "unknown")
        self.assertTrue(plan["assessment"]["conditions"][1]["missing_refs"])

    def test_null_does_not_satisfy_an_unknown_equals_unknown_comparison(self):
        state, value = world(), baseline()
        state["evidence"]["ready"]["status"] = None
        value["events"][0]["conditions"][1]["expected"] = None
        plan = find(assess_plans(state, value), "a")
        self.assertEqual(plan["status"], "DATA_REQUIRED")
        self.assertEqual(plan["assessment"]["conditions"][1]["result"], "unknown")

    def test_dead_required_participant_blocks_exact_path_and_only_descendants_recheck(self):
        state = world()
        state["entity_registry"]["entities"]["hero"]["versions"][0]["exists"] = False
        report = assess_plans(state, baseline())
        self.assertEqual(find(report, "a")["status"], "BLOCKED")
        self.assertTrue(find(report, "b")["assessment"]["dependency_reevaluation_required"])
        self.assertEqual(find(report, "b")["assessment"]["affected_by"], ["a"])
        self.assertFalse(find(report, "c")["assessment"]["dependency_reevaluation_required"])
        self.assertEqual(report["affected_event_ids"], ["a", "b"])
        self.assertNotIn("successor", json.dumps(report))

    def test_missing_identity_differs_from_dissolved_identity(self):
        state = world()
        state["entity_registry"]["entities"] = {}
        self.assertEqual(find(assess_plans(state, baseline()), "a")["status"], "DATA_REQUIRED")

    def test_supporting_change_marks_risk_without_automatic_cancellation(self):
        value = baseline()
        value["events"][0]["conditions"][1]["requirement"] = "supporting"
        state = world()
        state["evidence"]["ready"]["status"] = "disputed"
        report = assess_plans(state, value)
        self.assertEqual(find(report, "a")["status"], "AT_RISK")
        self.assertEqual(find(report, "b")["status"], "BLOCKED")
        self.assertTrue(find(report, "b")["assessment"]["dependency_reevaluation_required"])
        self.assertFalse(report["execution_available"])

    def test_identity_predicate_uses_dated_current_identity(self):
        value = baseline()
        value["events"][0]["conditions"] = [condition("name", "entity_identity", entity_id="hero", field="name", expected="Alice")]
        self.assertEqual(find(assess_plans(world(), value), "a")["status"], "UNBOUND")
        value["events"][0]["conditions"][0]["expected"] = "Bob"
        self.assertEqual(find(assess_plans(world(), value), "a")["status"], "BLOCKED")
        value["events"][0]["conditions"][0]["field"] = "unknown-office"
        self.assertEqual(find(assess_plans(world(), value), "a")["status"], "DATA_REQUIRED")

    def test_unsupported_predicates_and_reference_paths_are_not_evaluated(self):
        for predicate in (condition("script", "python", expression="raise RuntimeError()"),
                          condition(path=["historical_start", "date"], expected="1415-08-11"),
                          condition(path=["actors", "__class__"], expected="anything")):
            value = baseline()
            value["events"][0]["conditions"] = [predicate]
            item = find(assess_plans(world(), value), "a")["assessment"]["conditions"][0]
            self.assertEqual(item["result"], "unknown")
            self.assertTrue(item["unsupported_refs"])

    def test_proposed_research_and_empty_requirements_never_establish_intact_path(self):
        for change in (lambda e: e.update(research_status="proposed_research"),
                       lambda e: e.update(classification="research_inference"),
                       lambda e: e.update(conditions=[])):
            value = baseline()
            change(value["events"][0])
            item = find(assess_plans(world(), value), "a")
            self.assertEqual(item["status"], "DATA_REQUIRED")
            self.assertIsNone(item["assessment"]["historical_path_intact"])

    def test_terminal_status_does_not_resurrect_after_conditions_become_true(self):
        for status in ("PREVENTED", "SUPERSEDED", "EXPIRED"):
            value, state = baseline(), world()
            plans = initialize_plans(value, state)
            find(plans, "a").update(status=status, change_ref="explicit-prior-core-or-authoring-decision")
            report = assess_plans(state, value, plans)
            self.assertEqual(find(report, "a")["status"], status)
            self.assertFalse(report["execution_available"])

    def test_cross_campaign_and_changed_baseline_are_rejected(self):
        value, state = baseline(), world()
        plans = initialize_plans(value, state)
        with self.assertRaises(ValueError):
            assess_plans(world("OTHER-BRANCH"), value, plans)
        value["revision"] = 2
        with self.assertRaises(ValueError):
            assess_plans(state, value, plans)
        value = baseline()
        state["branch_id"] = "another-explicit-branch"
        with self.assertRaises(ValueError):
            assess_plans(state, value, plans)

    def test_no_automatic_historical_matching_or_outcome_certification(self):
        value, state = baseline(), world()
        state["journal"] = [{"id": "committed-1", "op": "record_evidence", "params": {"assertion": "Synthetic a happened"}}]
        plans = initialize_plans(value, state)
        self.assertEqual(assess_plans(state, value)["actual_occurrence_refs"], [])
        find(plans, "a")["actual_occurrence_refs"] = ["committed-1", "missing-journal-record"]
        report = assess_plans(state, value, plans)
        self.assertEqual(report["actual_occurrence_refs"], ["committed-1"])
        self.assertEqual(find(report, "a")["assessment"]["missing_occurrence_refs"], ["missing-journal-record"])
        self.assertIsNone(find(report, "a")["assessment"]["actual_outcome"])
        find(plans, "a")["status"] = "OCCURRED_AS_RECORDED"
        with self.assertRaises(ValueError):
            assess_plans(state, value, plans)

    def test_views_are_detached_and_byte_identical_inputs_survive_repeated_inspection(self):
        value, state = baseline(), world()
        plans = initialize_plans(value, state)
        before = json.dumps([value, state, plans], sort_keys=True)
        for _ in range(3):
            report = assess_plans(state, value, plans)
        report["plans"][0]["assessment"]["conditions"][0]["observed_refs"].clear()
        report["cutoff"]["axis"]["calendar"] = "changed-returned-data"
        self.assertEqual(json.dumps([value, state, plans], sort_keys=True), before)
        self.assertEqual(state["knowledge"], {})
        self.assertEqual(state["journal"], [])

    def test_graph_locality_and_no_unknown_nodes(self):
        self.assertEqual(affected_plans(baseline(), ["a"]), ["a", "b"])
        self.assertEqual(affected_plans(baseline(), ["c"]), ["c"])
        self.assertEqual(affected_plans(baseline(), []), [])
        with self.assertRaises(ValueError):
            affected_plans(baseline(), ["outside"])

    def test_saved_edition_is_pinned_and_old_world_is_preview_only(self):
        value, state = baseline(), world()
        with patch("historical_plans.baseline_view", return_value=copy.deepcopy(value)):
            preview = campaign_plan_view(state)
        self.assertEqual(preview["storage"], "preview_only")
        self.assertNotIn("historical_planning", state)
        saved = initialize_plans(value, state)
        saved.update(baseline_snapshot=copy.deepcopy(value), storage="saved_prospective_reference", installed_schedule=False)
        state["historical_planning"] = saved
        before = json.dumps(state, sort_keys=True)
        with patch("historical_plans.baseline_view", side_effect=AssertionError("A saved edition must not consult a newer baseline")):
            report = campaign_plan_view(state)
        self.assertEqual(report["storage"], "saved_prospective_reference")
        self.assertEqual(report["baseline_source"], "saved_baseline_snapshot")
        self.assertFalse(report["installed_schedule"])
        self.assertEqual(json.dumps(state, sort_keys=True), before)
        state["historical_planning"]["baseline_snapshot"]["revision"] = 2
        with self.assertRaises(ValueError):
            campaign_plan_view(state)

    def test_fork_rebinds_only_reference_scope_and_preserves_terminal_and_explicit_links(self):
        value, state = baseline(), world()
        saved = initialize_plans(value, state)
        saved["baseline_snapshot"] = copy.deepcopy(value)
        find(saved, "a").update(status="PREVENTED", change_ref="source-decision", actual_occurrence_refs=["inherited-journal-link"])
        before = json.dumps(saved, sort_keys=True)
        forked = fork_plan_reference(saved, "FORK", state["campaign_id"])
        self.assertEqual(forked["campaign_id"], "FORK")
        self.assertEqual(find(forked, "a")["id"], "plan:FORK:a")
        self.assertEqual(find(forked, "a")["status"], "PREVENTED")
        self.assertEqual(find(forked, "a")["actual_occurrence_refs"], ["inherited-journal-link"])
        self.assertEqual(forked["baseline_snapshot"], value)
        self.assertEqual(forked["baseline_ref"], saved["baseline_ref"])
        self.assertEqual(forked["fork_provenance"][0]["origin_campaign_id"], state["campaign_id"])
        self.assertEqual(json.dumps(saved, sort_keys=True), before)
        state["campaign_id"] = "FORK"
        state["historical_planning"] = forked
        self.assertEqual(find(campaign_plan_view(state), "a")["status"], "PREVENTED")
        with self.assertRaises(ValueError):
            fork_plan_reference(saved, "FORK-2", "wrong-origin")


if __name__ == "__main__":
    unittest.main()
