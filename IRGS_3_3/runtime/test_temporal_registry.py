"""Temporal registry fixtures: historical dates are synthetic unless stated."""
import copy
import json
import unittest

from temporal_registry import (ENTITY_OPS, available_entities, julian_day,
                               operate_entity, snapshot_registry, validate_registry)


def entity(entity_id, kind, name, start=1200, end=None, **identity):
    return {"id": entity_id, "kind": kind, "formed_at": None,
            "versions": [{"start": start, "end": end, "exists": True,
                          "identity": {"name": name, "category": kind, **identity},
                          "source_ref": "fixture-identity-source"}]}


def policy(entity_id, scenario_id, start=1300, eligible=True, actor_ids=None, mode="individual"):
    return {"entity_id": entity_id, "scenario_id": scenario_id,
            "versions": [{"start": start, "end": None, "eligible": eligible,
                          "reason": "Explicit fixture policy" if eligible else "Existence does not select control",
                          "control": {"mode": mode, "actor_ids": actor_ids or [],
                                      "powers": ["declare_own_intent"] if eligible else []},
                          "source_ref": "fixture-policy-source"}]}


def template():
    # The collapsed polity's first version starts at its observation date;
    # this does not imply that its actual formation date is known.
    old = entity("old-polity", "faction", "Former Crown", end=1390)
    old["versions"].append({"start": 1390, "end": None, "exists": False,
        "identity": {"name": "Former Crown", "category": "faction"}, "source_ref": "documented-dissolution"})
    nation = entity("realm", "faction", "Earlier Realm", leader_ids=["hero"])
    nation["versions"][0]["end"] = 1400
    nation["versions"].append({"start": 1400, "end": None, "exists": True,
        "identity": {"name": "Renamed Realm", "category": "polity", "government": "council", "leader_ids": ["other"]},
        "source_ref": "sourced-rename-and-office-change"})
    reg = {"schema_version": 1, "source_mode": "historical_template",
           "axis": {"id": "synthetic-year-ordinal", "unit": "year", "calendar": "fixture-only"},
           "as_of": 1415,
           "entities": {"hero": entity("hero", "character", "Alice", species="human"),
                        "other": entity("other", "character", "Bob", species="human"),
                        "realm": nation, "old-polity": old,
                        "conflict": entity("conflict", "conflict", "The Fixture Conflict"),
                        "future": entity("future", "faction", "Future Polity", start=1500),
                        "future-person": entity("future-person", "character", "Future Person", start=1500),
                        "future-war": entity("future-war", "conflict", "Future Conflict", start=1500)},
           "relations": {
               "realm-war": {"id": "realm-war", "from_id": "realm", "to_id": "conflict", "type": "participation",
                   "versions": [{"start": 1300, "end": None, "status": "active", "source_ref": "entry-into-conflict"}]},
               "old-war": {"id": "old-war", "from_id": "old-polity", "to_id": "conflict", "type": "participation",
                   "versions": [{"start": 1300, "end": 1390, "status": "active", "source_ref": "former-participation"},
                                {"start": 1390, "end": None, "status": "ended", "source_ref": "participation-ended"}]},
               "affiliation": {"id": "affiliation", "from_id": "hero", "to_id": "realm", "type": "affiliation",
                   "versions": [{"start": 1300, "end": None, "status": "active", "source_ref": "membership-source"}]},
               "future-alliance": {"id": "future-alliance", "from_id": "realm", "to_id": "future", "type": "alliance",
                   "versions": [{"start": 1500, "end": None, "status": "active", "source_ref": "future-alliance-source"}]}},
           "eligibility": {"solo-hero": policy("hero", "individual", actor_ids=["hero"]),
                           "solo-realm": policy("realm", "individual", eligible=False, mode="institutional"),
                           "war-realm": policy("realm", "war", actor_ids=["hero"], mode="institutional"),
                           "future-policy": policy("future-person", "future-scenario", start=1500, actor_ids=["future-person"])},
           "scenarios": {"individual": {"id": "individual", "title": "Individual play", "character_creation_allowed": True},
                         "war": {"id": "war", "title": "Fixture conflict", "character_creation_allowed": False, "conflict_id": "conflict"},
                         "future-scenario": {"id": "future-scenario", "title": "Future scenario", "character_creation_allowed": False, "conflict_id": "future-war"}}}
    return reg


def state_fixture():
    reg = snapshot_registry(template(), 1415)
    return {"actors": {"hero": {"id": "hero", "name": "Alice", "species": "human", "current": {}},
                       "other": {"id": "other", "name": "Bob", "species": "human", "current": {}}},
            "player_actor_ids": [], "entity_registry": reg}


def apply(state, op, **params):
    operate_entity(None, state, 10, op, {"effective_at": state["entity_registry"]["as_of"],
                                      "source_ref": "fixture-operation-source", **params})


class JulianCalendarTests(unittest.TestCase):
    def test_known_julian_day_and_consecutive_month_boundaries(self):
        self.assertEqual(julian_day(2000, 1, 1), 2451558)
        self.assertEqual(julian_day(1415, 8, 12) - julian_day(1415, 8, 11), 1)
        self.assertEqual(julian_day(1415, 9, 1) - julian_day(1415, 8, 31), 1)
        self.assertEqual(julian_day(1416, 3, 1) - julian_day(1416, 2, 28), 2)
        self.assertEqual(julian_day(1700, 3, 1) - julian_day(1700, 2, 28), 2)

    def test_invalid_or_unprovided_calendar_values_are_not_invented(self):
        for values in ((0, 1, 1), (-1, 1, 1), (True, 1, 1), (1415, 2, 29),
                       (1415, 0, 1), (1415, 13, 1), (1415, 8, 32), (1415, 8, 0),
                       (1415, 1.5, 1), ("1415", 8, 11)):
            with self.subTest(values=values), self.assertRaises(ValueError):
                julian_day(*values)


class TemporalQueryTests(unittest.TestCase):
    def test_collapsed_entity_is_not_resurrected_at_a_later_opening(self):
        reg = snapshot_registry(template(), 1415)
        current = available_entities(reg, "war")
        earlier = available_entities(reg, "war", at=1389)
        self.assertNotIn("old-polity", {e["id"] for e in current["factions"]})
        former = next(e for e in earlier["factions"] if e["id"] == "old-polity")
        self.assertTrue(former["exists"])
        self.assertEqual(former["participation"], "participating")
        self.assertFalse(former["eligible"])

    def test_existence_participation_and_scenario_eligibility_are_distinct(self):
        reg = snapshot_registry(template(), 1415)
        solo = available_entities(reg)
        solo_realm = next(e for e in solo["factions"] if e["id"] == "realm")
        self.assertTrue(solo_realm["exists"])
        self.assertFalse(solo_realm["eligible"])
        self.assertEqual(solo_realm["participation"], "unknown")
        war = available_entities(reg, "war")
        realm = next(e for e in war["factions"] if e["id"] == "realm")
        self.assertTrue(realm["eligible"])
        self.assertEqual(realm["participation"], "participating")
        hero = next(e for e in war["characters"] if e["id"] == "hero")
        self.assertEqual(hero["participation"], "unknown", "Affiliation must not imply personal participation")
        self.assertFalse(hero["eligible"], "No policy is different from known permission")

    def test_temporal_names_government_and_leaders_use_the_requested_point(self):
        reg = snapshot_registry(template(), 1415)
        old = available_entities(reg, at=1390)["factions"][0]
        new = available_entities(reg)["factions"][0]
        self.assertEqual(old["id"], new["id"])
        self.assertEqual(old["name"], "Earlier Realm")
        self.assertEqual(new["name"], "Renamed Realm")
        self.assertEqual(old["identity"]["leader_ids"], ["hero"])
        self.assertEqual(new["identity"]["leader_ids"], ["other"])
        self.assertEqual(new["identity"]["government"], "council")
        self.assertIsNone(new["formed_at"], "Observation/version start must not invent a formation date")

    def test_inspection_uses_only_registry_as_of_and_never_rehydrates_a_template(self):
        reg = snapshot_registry(template(), 1415)
        before = copy.deepcopy(reg)
        view = available_entities(reg, "war", kind="faction")
        self.assertEqual(view["as_of"], 1415)
        self.assertEqual(view["characters"], [])
        self.assertFalse(view["simulation_writes"])
        view["factions"][0]["identity"]["leader_ids"].append("altered-return-value")
        self.assertEqual(reg, before)
        for kwargs in ({"at": 1416}, {"at": "1415"}, {"at": True}, {"scenario_id": "unknown"}, {"kind": "country"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                available_entities(reg, **kwargs)

    def test_custom_axis_is_explicit_metadata_not_an_implicit_converter(self):
        reg = snapshot_registry(template(), 1415)
        reg["axis"] = {"id": "custom-turns", "unit": "stellar-cycle", "calendar": "unconverted-custom-calendar"}
        self.assertEqual(available_entities(reg)["axis"], reg["axis"])
        with self.assertRaises(ValueError):
            available_entities(reg, at="Cycle 1415")

    def test_relation_end_and_disputed_status_are_not_active_participation(self):
        state = state_fixture()
        apply(state, "record_entity_relation", relation_id="realm-war", from_id="realm", to_id="conflict", relation_type="participation", status="ended")
        realm = available_entities(state["entity_registry"], "war")["factions"][0]
        self.assertEqual(realm["participation"], "not_participating")
        apply(state, "record_entity_relation", relation_id="realm-war", from_id="realm", to_id="conflict", relation_type="participation", status="disputed")
        self.assertEqual(available_entities(state["entity_registry"], "war")["factions"][0]["participation"], "unknown")


class SnapshotTests(unittest.TestCase):
    def test_snapshot_excludes_future_entities_scenarios_relations_and_policies(self):
        original = template()
        before = copy.deepcopy(original)
        original["entities"]["hero"]["versions"][0]["end"] = 1450
        original["entities"]["hero"]["versions"].append({"start": 1450, "end": None, "exists": False,
            "identity": {"name": "Alice", "category": "character"}, "source_ref": "future-death-source"})
        selected = snapshot_registry(original, 1415)
        self.assertEqual(selected["source_mode"], "playthrough")
        self.assertNotIn("future", selected["entities"])
        self.assertNotIn("future-person", selected["entities"])
        self.assertNotIn("future-alliance", selected["relations"])
        self.assertNotIn("future-policy", selected["eligibility"])
        self.assertNotIn("future-scenario", selected["scenarios"])
        self.assertEqual(len(selected["entities"]["hero"]["versions"]), 1)
        self.assertIsNone(selected["entities"]["hero"]["versions"][0]["end"])
        self.assertNotIn("future-death-source", json.dumps(selected))
        self.assertNotIn("Future Person", json.dumps(selected))
        self.assertTrue(validate_registry(selected))
        selected["entities"]["realm"]["versions"][-1]["identity"]["name"] = "Changed locally"
        self.assertEqual(original["entities"]["realm"], before["entities"]["realm"])

    def test_historical_template_can_be_browsed_but_cannot_be_mutated_as_live(self):
        original = template()
        future = available_entities(original, "future-scenario", at=1500)
        self.assertIn("future", {e["id"] for e in future["factions"]})
        state = state_fixture()
        state["entity_registry"] = original
        before = copy.deepcopy(state)
        with self.assertRaises(ValueError):
            apply(state, "transition_entity", entity_id="realm", identity={"name": "Unapproved"})
        self.assertEqual(state, before)
        with self.assertRaises(ValueError):
            snapshot_registry(state_fixture()["entity_registry"], 1415)


class RegistryValidationTests(unittest.TestCase):
    def test_future_playthrough_data_overlaps_and_unsourced_versions_are_rejected(self):
        for mutation in (
            lambda r: r.update(schema_version=True),
            lambda r: r["axis"].update(id=""),
            lambda r: r["entities"]["realm"]["versions"][-1].update(start=1416),
            lambda r: r["entities"]["realm"]["versions"][-1].update(end=1450),
            lambda r: r["entities"]["realm"]["versions"][0].update(end=None),
            lambda r: r["entities"]["realm"]["versions"][-1].update(source_ref=""),
            lambda r: r["entities"]["realm"].update(formed_at=1500),
            lambda r: r["relations"]["realm-war"].update(to_id="missing"),
            lambda r: r["scenarios"]["war"].update(conflict_id="realm")):
            reg = state_fixture()["entity_registry"]
            mutation(reg)
            with self.subTest(reg=reg), self.assertRaises(ValueError):
                validate_registry(reg)

    def test_invalid_or_implicit_control_rights_are_rejected(self):
        for change in ({"actor_ids": []}, {"actor_ids": ["missing"]}, {"actor_ids": ["realm"]},
                       {"powers": ["declare_war"]}, {"powers": []}, {"mode": "nation-god"}):
            reg = state_fixture()["entity_registry"]
            reg["eligibility"]["solo-hero"]["versions"][0]["control"].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_registry(reg)
        state = state_fixture()
        with self.assertRaises(ValueError):
            validate_registry(state["entity_registry"], {"hero": state["actors"]["hero"]})


class EntityOperationTests(unittest.TestCase):
    def test_all_five_operations_use_one_committed_registry_point(self):
        state = state_fixture()
        apply(state, "register_entity", entity_id="new-realm", kind="faction", identity={"name": "New Realm", "category": "polity"})
        self.assertIsNone(state["entity_registry"]["entities"]["new-realm"]["formed_at"])
        apply(state, "transition_entity", entity_id="new-realm", identity={"name": "Renamed New Realm", "government": "assembly"})
        versions = state["entity_registry"]["entities"]["new-realm"]["versions"]
        self.assertEqual(versions[0]["start"], versions[0]["end"], "Same-point historical versions may have zero width")
        apply(state, "record_entity_relation", relation_id="new-war", from_id="new-realm", to_id="conflict", relation_type="participation", status="active")
        apply(state, "record_entity_eligibility", entity_id="new-realm", scenario_id="war", eligible=True,
              reason="Explicit campaign policy", control={"mode": "institutional", "actor_ids": ["hero"], "powers": ["declare_own_intent"]})
        apply(state, "select_entity_control", entity_id="new-realm", scenario_id="war", actor_id="hero", instruction_ref="explicit-user-choice")
        self.assertEqual(state["player_actor_ids"], ["hero"])
        self.assertFalse(state["starting_control"]["institutional_mandate_granted"])
        self.assertEqual(state["starting_control"]["powers"], ["declare_own_intent"])
        self.assertEqual(state["entity_registry"]["as_of"], 1415)
        self.assertNotIn("mandates", state)
        self.assertTrue(validate_registry(state["entity_registry"], state["actors"]))

    def test_new_character_must_reference_the_existing_actual_actor(self):
        state = state_fixture()
        for entity_id, name in (("ghost", "Ghost"), ("new-person", "Different Name")):
            candidate = copy.deepcopy(state)
            candidate["actors"]["new-person"] = {"id": "new-person", "name": "Actual Name"}
            before = copy.deepcopy(candidate)
            with self.assertRaises(ValueError):
                apply(candidate, "register_entity", entity_id=entity_id, kind="character", identity={"name": name})
            self.assertEqual(candidate, before)
        state["actors"]["new-person"] = {"id": "new-person", "name": "Actual Name"}
        apply(state, "register_entity", entity_id="new-person", kind="character", identity={"name": "Actual Name"})
        self.assertIn("new-person", {e["id"] for e in available_entities(state["entity_registry"])["characters"]})

    def test_future_backdated_unsourced_and_reused_identity_mutations_leave_state_intact(self):
        for params in ({"effective_at": 1416}, {"effective_at": 1414}, {"effective_at": "1415"},
                       {"source_ref": ""}, {"entity_id": "realm"}, {"formed_at": 1500}):
            state = state_fixture()
            before = copy.deepcopy(state)
            with self.subTest(params=params), self.assertRaises(ValueError):
                apply(state, "register_entity", **{"entity_id": "new", "kind": "faction", "identity": {"name": "New"}, **params})
            self.assertEqual(state, before)

    def test_lifecycle_does_not_select_successor_recreate_entity_or_rehydrate_source(self):
        state = state_fixture()
        apply(state, "select_entity_control", entity_id="hero", scenario_id="individual", actor_id="hero", instruction_ref="choose-alice")
        apply(state, "transition_entity", entity_id="hero", exists=False, successor_ids=["other"])
        self.assertEqual(state["player_actor_ids"], ["hero"], "Death must not choose a successor for the player")
        self.assertEqual(state["starting_control"]["actor_id"], "hero")
        self.assertNotIn("hero", {e["id"] for e in available_entities(state["entity_registry"])["characters"]})
        realm = available_entities(state["entity_registry"], "war")["factions"][0]
        self.assertFalse(realm["policy_eligible"])
        self.assertFalse(realm["eligible"], "Old control policy must not resurrect its dead actor")
        old_policy = state["entity_registry"]["eligibility"]["war-realm"]["versions"][0]
        self.assertTrue(old_policy["eligible"], "The earlier sourced assertion remains historical evidence")
        self.assertEqual(old_policy["end"], 1415)
        self.assertEqual(old_policy["end_source_ref"], "fixture-operation-source")
        before = copy.deepcopy(state)
        with self.assertRaises(ValueError):
            apply(state, "select_entity_control", entity_id="realm", scenario_id="war", actor_id="hero", instruction_ref="try-dead-control")
        self.assertEqual(state, before)
        self.assertEqual(set(state["actors"]), {"hero", "other"})

    def test_same_point_death_closes_prior_causal_policy_and_relations(self):
        state = state_fixture()
        # A fresh snapshot may have all observed assertions at the opening point.
        for entity_record in state["entity_registry"]["entities"].values():
            current = entity_record["versions"][-1]
            entity_record["versions"] = [{**current, "start": 1415}]
        state["entity_registry"]["entities"].pop("old-polity")
        state["entity_registry"]["entities"]["realm"]["versions"][0]["identity"]["leader_ids"] = ["hero"]
        state["entity_registry"]["relations"].pop("old-war")
        for record in list(state["entity_registry"]["relations"].values()) + list(state["entity_registry"]["eligibility"].values()):
            record["versions"][-1]["start"] = 1415
        apply(state, "select_entity_control", entity_id="hero", scenario_id="individual", actor_id="hero", instruction_ref="opening-choice")
        apply(state, "transition_entity", entity_id="hero", exists=False)
        self.assertEqual(state["player_actor_ids"], ["hero"])
        self.assertEqual(state["entity_registry"]["relations"]["affiliation"]["versions"][0]["end"], 1415)
        self.assertEqual(state["entity_registry"]["eligibility"]["solo-hero"]["versions"][0]["end"], 1415)
        realm = available_entities(state["entity_registry"], "war")["factions"][0]
        self.assertEqual(realm["identity"]["leader_ids"], ["hero"], "Death does not invent a leadership successor")
        self.assertFalse(realm["eligible"])
        self.assertTrue(validate_registry(state["entity_registry"], state["actors"]))
        apply(state, "transition_entity", entity_id="realm", exists=False)
        self.assertEqual(state["entity_registry"]["relations"]["realm-war"]["versions"][0]["end"], 1415)
        self.assertEqual(available_entities(state["entity_registry"], "war")["factions"], [])

    def test_dated_territory_and_resource_references_are_copied_and_not_quantities(self):
        state = state_fixture()
        refs = ["territory:canonical-record"]
        apply(state, "register_entity", entity_id="new-realm", kind="faction", identity={"name": "New"},
              territory_refs=refs, resource_refs=["capacity:canonical-record"], resources_status="uninitialized")
        refs.append("caller-mutation")
        state["entity_registry"]["as_of"] = 1416  # Fixture represents a separately committed calendar advance.
        apply(state, "transition_entity", entity_id="new-realm", resource_refs=["stock:canonical-record"], resources_status="referenced")
        old = next(e for e in available_entities(state["entity_registry"], at=1415)["factions"] if e["id"] == "new-realm")
        new = next(e for e in available_entities(state["entity_registry"])["factions"] if e["id"] == "new-realm")
        self.assertEqual(old["resource_refs"], ["capacity:canonical-record"])
        self.assertEqual(new["resource_refs"], ["stock:canonical-record"])
        self.assertEqual(new["territory_refs"], ["territory:canonical-record"])
        self.assertEqual(old["resources_status"], "uninitialized")
        self.assertEqual(new["resources_status"], "referenced")
        before = copy.deepcopy(state)
        new["territory_refs"].append("returned-mutation")
        self.assertEqual(state, before)
        for invalid in ([{"stock": 30}], ["duplicate", "duplicate"], "single-ref", [""]):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                apply(state, "transition_entity", entity_id="new-realm", resource_refs=invalid)
            self.assertEqual(state, before)

    def test_selection_requires_explicit_user_choice_and_allowed_actor_without_nation_powers(self):
        for params in ({"instruction_ref": ""}, {"actor_id": "other"}, {"scenario_id": "unknown"},
                       {"entity_id": "old-polity"}, {"scenario_id": "individual"}):
            state = state_fixture()
            before = copy.deepcopy(state)
            with self.subTest(params=params), self.assertRaises(ValueError):
                apply(state, "select_entity_control", **{"entity_id": "realm", "scenario_id": "war", "actor_id": "hero",
                                                         "instruction_ref": "explicit-player", **params})
            self.assertEqual(state, before)

    def test_mutation_does_not_treat_causal_sequence_as_elapsed_calendar(self):
        state = state_fixture()
        operate_entity(None, state, 999999, "transition_entity", {"entity_id": "realm", "effective_at": 1415,
            "identity": {"name": "Same-Point Rename"}, "source_ref": "explicit-source"})
        self.assertEqual(state["entity_registry"]["as_of"], 1415)
        self.assertEqual(available_entities(state["entity_registry"])["factions"][0]["name"], "Same-Point Rename")

    def test_ended_or_missing_entities_cannot_receive_new_relations_or_playability(self):
        state = state_fixture()
        with self.assertRaises(ValueError):
            apply(state, "record_entity_relation", relation_id="invalid", from_id="old-polity", to_id="realm", relation_type="alliance", status="active")
        with self.assertRaises(ValueError):
            apply(state, "record_entity_eligibility", entity_id="old-polity", scenario_id="individual", eligible=True,
                reason="Not actually existing", control={"mode": "individual", "actor_ids": ["hero"], "powers": ["declare_own_intent"]})


class CoreEntityDispatchTests(unittest.TestCase):
    def test_core_dispatches_all_five_in_one_state_and_retains_replay_idempotence(self):
        from campaign_library import initial_campaign
        from core_world import CoreWorld, SUPPORTED_OPS
        self.assertTrue(ENTITY_OPS <= SUPPORTED_OPS)
        world = initial_campaign("military", "ENTITY-DISPATCH")
        fixture = state_fixture()
        world.s["actors"] = fixture["actors"]
        world.s["entity_registry"] = fixture["entity_registry"]
        world.s["player_actor_ids"] = []
        world = CoreWorld(state=world.s)
        operations = [
            ("register_entity", {"entity_id": "new", "kind": "faction", "identity": {"name": "New Realm"}}),
            ("transition_entity", {"entity_id": "new", "identity": {"name": "New Name"}}),
            ("record_entity_relation", {"relation_id": "new-participation", "from_id": "new", "to_id": "conflict", "relation_type": "participation", "status": "active"}),
            ("record_entity_eligibility", {"entity_id": "new", "scenario_id": "war", "eligible": True, "reason": "User-selected fixture policy", "control": {"mode": "institutional", "actor_ids": ["hero"], "powers": ["declare_own_intent"]}}),
            ("select_entity_control", {"entity_id": "new", "scenario_id": "war", "actor_id": "hero", "instruction_ref": "explicit-user-choice"}),
        ]
        for sequence, (op, params) in enumerate(operations, 1):
            args = {"campaign_id": "ENTITY-DISPATCH", "effective_at": 1415, "source_ref": "dispatch-fixture", **params}
            self.assertTrue(world.apply("entity-op-" + str(sequence), sequence, op, **args))
            before = world.save()
            self.assertFalse(world.apply("entity-op-" + str(sequence), sequence, op, **args))
            self.assertEqual(world.save(), before)
        self.assertEqual(world.s["player_actor_ids"], ["hero"])
        self.assertEqual(len(world.s["journal"]), 5)
        self.assertEqual(world.s["entity_registry"]["as_of"], 1415)
        self.assertEqual(CoreWorld.load(world.save()).save(), world.save())


if __name__ == "__main__":
    unittest.main()
