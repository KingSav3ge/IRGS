"""Describe dispatch declarations without manufacturing dependency evidence.

Inventory rows identify backend/operation contracts. Source locations are found
in the current AST; they are navigation references, not transitive footprint or
branch-coverage proofs. ``owner_classification`` only annotates paths supplied
by an actual observation and must never become an allocation input.
"""
from __future__ import annotations

import ast
import importlib
from pathlib import Path
import sys


OWNER_REFERENCE = "engine/Core/IRGS_Core_3_3_3_E_C2.md"
MAPPING_SCOPE = (
    "Interpretive namespace annotation of supplied observed paths, not manually "
    "declared dependencies or proof of owner-qualified interfaces. Mixed or "
    "specialist namespaces remain unmapped. Metadata and validation reads are "
    "reported separately; no observed path may be discarded for allocation "
    "because of this annotation."
)


def _runtime_modules(runtime_dir):
    runtime = Path(runtime_dir).resolve(strict=True)
    names = ("r9_runtime", "r8_dependencies", "core_world", "r6_work",
             "r7_frontier", "r9_adapters", "genre_receivers", "temporal_registry",
             "economic_extension")
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(runtime))
    try:
        result = {name: importlib.import_module(name) for name in names}
        for name, module in result.items():
            if Path(module.__file__).resolve().parent != runtime:
                raise ValueError("Runtime module comes from another checkout: " + name)
        return runtime, result
    finally:
        sys.path.pop(0)
        sys.dont_write_bytecode = previous


class _Sources:
    def __init__(self, runtime):
        self.runtime = runtime
        self.trees = {}

    def tree(self, filename):
        if filename not in self.trees:
            self.trees[filename] = ast.parse((self.runtime / filename).read_text(encoding="utf-8"))
        return self.trees[filename]

    def reference(self, filename, symbol, line, **extra):
        return {"path": "IRGS_3_3/runtime/" + filename,
                "symbol": symbol, "line": line, **extra}

    def symbol(self, filename, symbol):
        node = self.tree(filename)
        for part in symbol.split("."):
            node = next((item for item in node.body
                         if isinstance(item, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
                         and item.name == part), None)
            if node is None:
                return None
        return node

    def declaration(self, filename, symbol):
        """Find assignment/update locations for an imported declaration."""
        rows = []
        for node in self.tree(filename).body:
            assigned = (isinstance(node, ast.Assign)
                        and any(isinstance(target, ast.Name) and target.id == symbol for target in node.targets))
            updated = (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                       and isinstance(node.value.func, ast.Attribute)
                       and isinstance(node.value.func.value, ast.Name)
                       and node.value.func.value.id == symbol)
            if assigned or updated:
                rows.append(self.reference(filename, symbol, node.lineno))
        return rows or [self.reference(filename, symbol, None, status="SOURCE_NOT_RESOLVED")]

    def implementation(self, filename, symbol, operation=None, *, default_after=None):
        node = self.symbol(filename, symbol)
        if node is None:
            return self.reference(filename, symbol, None, status="SOURCE_NOT_RESOLVED")
        if operation is None:
            return self.reference(filename, symbol, node.lineno, status="FUNCTION_ENTRY")
        matches = []
        for branch in ast.walk(node):
            if not isinstance(branch, ast.If):
                continue
            for comparison in ast.walk(branch.test):
                if not (isinstance(comparison, ast.Compare)
                        and isinstance(comparison.left, ast.Name) and comparison.left.id == "op"
                        and len(comparison.ops) == 1 and len(comparison.comparators) == 1):
                    continue
                right = comparison.comparators[0]
                names = ([right.value] if isinstance(right, ast.Constant) and isinstance(right.value, str)
                         else [item.value for item in right.elts
                               if isinstance(item, ast.Constant) and isinstance(item.value, str)]
                         if isinstance(right, (ast.Tuple, ast.List, ast.Set)) else [])
                if operation in names and isinstance(comparison.ops[0], (ast.Eq, ast.In)):
                    matches.append(branch.lineno)
                if (default_after in names and default_after is not None
                        and isinstance(comparison.ops[0], ast.Eq) and branch.orelse):
                    matches.append(branch.orelse[0].lineno)
        if not matches:
            return self.reference(filename, symbol, node.lineno,
                                  status="BRANCH_NOT_RESOLVED", operation=operation)
        return self.reference(filename, symbol, min(matches),
                              status="GUARDED_DEFAULT_BRANCH" if default_after else "OPERATION_BRANCH")


def inventory(runtime_dir):
    """Return declared backend/operation pairs, including unobserved contracts.

    Importing these runtime modules reads code and declared operation sets only;
    it neither initializes a campaign nor opens any save. Existing modules from
    another checkout are refused. Set membership describes dispatch scope, not
    feasibility, player exposure or completed certification.
    """
    runtime, modules = _runtime_modules(runtime_dir)
    source = _Sources(runtime)
    base = set(modules["r8_dependencies"].SUPPORTED)
    work = set(modules["r6_work"].NEW_OPS)
    fabrication = set(modules["r7_frontier"].FAB_OPS)
    receivers = set(modules["r9_adapters"].NATIVE_OPS)
    core = modules["core_world"]
    genres = set(modules["genre_receivers"].GENRE_OPS)
    entities = set(modules["temporal_registry"].ENTITY_OPS)
    economic = set(modules["economic_extension"].ECON_OPS)
    r7 = base | work | fabrication | {"physical_loss"}
    backends = {"World": base, "R7World": r7,
                "ReceiverWorld": r7 | receivers, "CoreWorld": set(core.SUPPORTED_OPS)}
    declared = set().union(*backends.values())
    if declared != set(modules["r9_runtime"].SUPPORTED):
        raise ValueError("Backend declarations differ from R9's union; review the new dispatch route")
    selectors = {
        "CoreWorld": "state.profile is IRGS-CORE-3.3 or AST-CORE-3.3 (first selector)",
        "ReceiverWorld": "non-Core profile with r9_engine_bindings key (second selector)",
        "R7World": "non-Core profile without receiver binding and with econ3 key (third selector)",
        "World": "no selected Core profile, receiver binding or econ3 key (fallback selector)",
    }
    rows = []
    for backend, operations in sorted(backends.items()):
        for operation in sorted(operations):
            alias = core.ALIASES.get(operation) if backend == "CoreWorld" else None
            canonical = alias or operation
            support = source.declaration("r9_runtime.py", "SUPPORTED")
            chain = []
            limits = ["Declared dispatch only; valid actual state and parameters are required.",
                      "Implementation references are not complete transitive call or branch coverage."]
            if backend == "CoreWorld":
                support += source.declaration("core_world.py", "SUPPORTED_OPS")
                if alias:
                    support += source.declaration("core_world.py", "ALIASES")
                elif canonical not in genres:
                    support += source.declaration("core_world.py", "CORE_OPS")
                chain.append(source.implementation("core_world.py", "CoreWorld.apply"))
                if canonical in entities:
                    support += source.declaration("temporal_registry.py", "ENTITY_OPS")
                    chain.append(source.implementation("core_world.py", "CoreWorld._operate"))
                    implementation = source.implementation("temporal_registry.py", "operate_entity", canonical,
                        default_after="record_entity_eligibility" if canonical == "select_entity_control" else None)
                    limits.append("Temporal mutation requires the saved playthrough registry and its actual coordinate.")
                elif canonical in genres:
                    support += source.declaration("genre_receivers.py", "GENRE_OPS")
                    chain.append(source.implementation("core_world.py", "CoreWorld._operate"))
                    implementation = source.implementation("genre_receivers.py", "operate", canonical)
                    limits.append("Genre/binding, received instruction or delegation constraints are conditional.")
                elif canonical == "execute_player_equipment_issue":
                    chain.append(source.implementation("core_world.py", "CoreWorld._operate", canonical))
                    implementation = source.implementation("player_actions.py", "operate_equipment_action")
                    chain.append(source.implementation("genre_receivers.py", "operate", "military_issue_equipment"))
                    chain.append(source.implementation("core_world.py", "CoreWorld._operate", "transfer_stock"))
                    limits.append("Explicit received equipment action with current control, authority and stock checks.")
                elif canonical == "execute_player_scene_action":
                    chain.append(source.implementation("core_world.py", "CoreWorld._operate", canonical))
                    implementation = source.implementation("scene_actions.py", "operate_scene_action")
                    chain.append(source.implementation("core_world.py", "CoreWorld._operate", "transfer_stock"))
                    limits.append("Opt-in authored local movement, observation and dispatch delivery only; atomic scene durations, no general phases or calendar scheduler.")
                elif canonical == "receive_response_prompt":
                    chain.append(source.implementation("core_world.py", "CoreWorld._operate", canonical))
                    implementation = source.implementation("response_options.py", "operate_response_prompt")
                    limits.append("Received suggestions are drafts, not feasibility findings or combat outcomes.")
                else:
                    implementation = source.implementation("core_world.py", "CoreWorld._operate", canonical)
                exposure = ("BOUNDED_SOLO_ACTION" if canonical in {"execute_player_equipment_issue", "execute_player_scene_action"}
                            else "SOLO_DECLARATION_ONLY" if canonical == "record_player_action"
                            else "CREATOR_EVENT_OR_INTERNAL_CORE_INTERFACE")
                if alias:
                    limits.append("Compatibility spelling normalizes to the same Core handler; AST is not another engine.")
            else:
                chain.append(source.implementation("r9_adapters.py", "ReceiverWorld.apply")
                             if backend == "ReceiverWorld" else
                             source.implementation("r7_frontier.py", "R7World.apply")
                             if backend == "R7World" else
                             source.implementation("irgs_reference.py", "World.apply"))
                if operation in receivers:
                    support += source.declaration("r9_adapters.py", "NATIVE_OPS")
                    implementation = source.implementation("r9_adapters.py", "ReceiverWorld.apply", operation,
                        default_after="rom_revoke_delegation" if operation == "rom_start_delegated_job" else None)
                    limits.append("Proposed synthetic receiver bindings are required; not an adopted native engine release.")
                elif operation in fabrication:
                    support += source.declaration("r7_frontier.py", "FAB_OPS")
                    implementation = source.implementation("r7_frontier.py", "FabricationWorld._operate", operation)
                elif operation in work:
                    support += source.declaration("r6_work.py", "NEW_OPS")
                    implementation = source.implementation("r6_work.py", "ProgressWorld._operate", operation)
                elif operation == "physical_loss":
                    implementation = source.implementation("r5_hazards.py", "PhysicalWorld._operate")
                    chain.append(source.implementation("r7_frontier.py", "R7World.apply", operation))
                    limits.append("Physical stock ledger required; in-transit cargo loss is expressly unqualified.")
                elif operation in economic:
                    support += source.declaration("economic_extension.py", "ECON_OPS")
                    chain.append(source.implementation("irgs_reference.py", "World._operate"))
                    implementation = source.implementation("economic_extension.py", "operate_econ", operation)
                    limits.append("The economic ledger, fixture selections and operation-specific sources are required.")
                else:
                    support += source.declaration("r8_dependencies.py", "SUPPORTED")
                    implementation = source.implementation("irgs_reference.py", "World._operate", operation)
                if backend != "World" and operation in modules["r6_work"].PROHIBITED_LEGACY:
                    limits.append("Legacy settlement is rejected for tracked jobs, not universally for all jobs.")
                limits.append("R9 selects the observation backend from saved state shape, not caller class alone.")
                exposure = "RESEARCH_ADAPTER_NOT_SOLO_ROUTE"
            refs = [implementation] + chain
            support = list({(row["path"], row["symbol"], row["line"]): row for row in support}.values())
            rows.append({"backend": backend, "operation": operation,
                "canonical_operation": canonical, "alias_of": alias,
                "backend_scope": "selected_core" if backend == "CoreWorld" else "bounded_research_adapter",
                "backend_selector": selectors[backend],
                "support_sources": support, "implementation_sources": refs,
                "implementation_status": implementation["status"], "solo_exposure": exposure,
                "qualification_limits": limits})
    return rows


# These labels describe current JSON namespaces, not new owners or footprints.
# Broad mixed/specialist records intentionally remain unresolved.
_ROOT_OWNERS = {
    "actors": ("K-ACTOR",), "player_actor_ids": ("K-ACTOR",),
    "stocks": ("K-STOCK",), "opening_stock": ("K-STOCK",),
    "cash": ("K-STOCK",), "cash_baseline": ("K-STOCK",),
    "equipment": ("K-STOCK",), "kit_baseline": ("K-STOCK",),
    "activities": ("K-WORK",), "commitments": ("K-WORK",),
    "capacities": ("K-NET",),
    "evidence": ("K-INFO",), "knowledge": ("K-INFO",), "reports": ("K-INFO",),
    "response_prompts": ("K-INFO",), "recognitions": ("K-INFO",),
    "designs": ("K-INFO",), "player_actions": ("K-INFO",),
    "delegations": ("K-ORG",), "starting_control": ("K-ORG",),
    "population": ("K-POP",),
    "campaign_time": ("K-TIME",), "elapsed_time": ("K-TIME",), "clock": ("K-TIME",),
    "site_conditions": ("K-NET",),
    "journal": ("K-TIME",), "processed": ("K-TIME",), "pending": ("K-TIME",),
    "r6_progress": ("K-WORK",), "r6_model_bindings": ("K-WORK",),
    "r7_intermediates": ("K-WORK",), "r7_profiles": ("K-WORK",),
}
_ECON_OWNERS = {
    "stocks": ("K-STOCK",), "opening": ("K-STOCK",),
    "produced": ("K-STOCK",), "consumed": ("K-STOCK",), "losses": ("K-STOCK",),
    "active_jobs": ("K-WORK",), "completed_jobs": ("K-WORK",),
    "recipes": ("K-WORK",), "care_delivered": ("K-WORK",),
    "qualifications": ("K-ORG",), "sites": ("K-NET",),
}
_METADATA_ROOTS = {"campaign_id", "profile", "binding", "core_version", "gameplay_started",
                   "fork_origin", "_r6_eid", "_r7_event_id", "r4_request_ids", "r4_frontiers",
                   "scene_rules", "scene_action_results"}


def _classify(path):
    if not path:
        return None, "whole-state path is not attributable to one owner", False
    root = path[0]
    if root in _METADATA_ROOTS:
        return (), "configuration/workflow namespace; observed dependencies retained", True
    if root in _ROOT_OWNERS:
        return _ROOT_OWNERS[root], "current runtime namespace annotation", False
    if root == "r9":
        if len(path) > 1 and path[1] == "mandates":
            return ("K-ORG",), "actual R9 mandate namespace", False
        if len(path) > 1 and path[1] in {"requests", "decisions", "frontiers"}:
            return (), "coordination metadata; observed dependencies retained", True
    if root == "econ3" and len(path) > 1 and path[1] in _ECON_OWNERS:
        return _ECON_OWNERS[path[1]], "current economic-adapter namespace annotation", False
    if root == "registry" and len(path) > 1 and path[1] == "characters":
        return ("K-ACTOR",), "character identity registry namespace", False
    if root == "entity_registry" and len(path) > 1:
        if path[1] in {"axis", "as_of"}:
            return ("K-TIME",), "explicit saved registry coordinate, not inferred elapsed time", False
        if path[1] == "eligibility":
            return ("K-ORG",), "explicit control-policy namespace", False
        if path[1] in {"schema_version", "source_mode", "scenarios"}:
            return (), "registry configuration namespace; observed dependencies retained", True
        return None, "mixed temporal entities/relations need state-aware owner attribution", False
    return None, "mixed, specialist or unclassified runtime namespace", False


def owner_classification(paths, *, validation_paths=()):
    """Annotate actual path sets; keep validation and unmapped paths explicit.

    No value returned here is an inferred read, write, capacity reservation or
    authorization result. In particular, an unmapped path is not independent.
    ``K-ASSET`` is not inferred from a design reference or anonymous equipment.
    """
    def annotate(values):
        owners, unmapped, metadata, mappings = set(), [], [], []
        normalized = set()
        for value in values:
            if not isinstance(value, (tuple, list)) or not all(isinstance(part, str) for part in value):
                raise ValueError("Observed paths must be lists/tuples of string components")
            normalized.add(tuple(value))
        for path in sorted(normalized):
            labels, reason, is_metadata = _classify(path)
            row = {"path": list(path), "reason": reason}
            if labels is None:
                unmapped.append(list(path))
            elif is_metadata:
                metadata.append(list(path))
            else:
                owners.update(labels)
                row["owners"] = list(labels)
            mappings.append(row)
        return {"owners": sorted(owners), "unmapped_paths": unmapped,
                "metadata_paths": metadata, "path_annotations": mappings}
    allocation = annotate(paths)
    validation = annotate(validation_paths)
    return {**allocation, "validation": validation, "mapping_scope": MAPPING_SCOPE,
            "owner_reference": OWNER_REFERENCE,
            "owner_reference_line": 4075,
            "owner_reference_status": "interpretive labels, not an executable owner registry"}
