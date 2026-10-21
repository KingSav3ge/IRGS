"""Current Fantasy Library 2.0 receiving checks; no archived engine is required."""
from pathlib import Path
import collections,copy,csv,hashlib,json,re,sys

ROOT=Path(__file__).resolve().parent
PACKAGE=ROOT.parent
SHA=lambda b:hashlib.sha256(b).hexdigest()


def projection_errors(projection,registry):
    errors=[]
    current={x["entry_id"]:x for x in registry["source_bindings"] if x["source"]=="FL"}
    source={x["entry_id"]:x for x in projection["source_bindings"]}
    if set(source)!=set(current):errors.append("source reference set")
    for eid,b in source.items():
        if current.get(eid)!=b:errors.append(eid+": source-qualified binding differs")
    return errors


def archetype_errors(binding,projection,registry):
    errors=[]
    source={x["id"]:x for x in projection["new_proposed_archetypes"]}
    target={x["id"]:x for x in binding["new_fantasy_archetype_bindings"]}
    if set(source)!=set(target):errors.append("archetype identity set")
    published={a["alias"].split("@")[0] for a in registry["aliases"]}
    for eid,x in source.items():
        b=target.get(eid,{})
        if x["requirements"]!=b.get("requirements") or x["limitations"]!=b.get("limitations"):
            errors.append(eid+": requirements/limits changed")
        if b.get("shared_alias") is not None or b.get("spawns_actual_state") is not False or "Proposed" not in b.get("source_status",""):
            errors.append(eid+": automatic promotion/creation")
        if eid in published:errors.append(eid+": invented published SCL alias")
    return errors


def verify():
    checks=[]
    def ck(name,condition,scope):
        checks.append({"id":name,"pass":bool(condition),"scope":scope})
    guide=(ROOT/"IRGS_Fantasy_Content_Library_v2_0_Candidate.md").read_text(encoding="utf8")
    projection=json.loads((ROOT/"Fantasy_Native_Source_Projection_v2_0.json").read_text(encoding="utf8"))
    manifest=json.loads((ROOT/"VERIFY_MANIFEST.json").read_text(encoding="utf8"))
    binding=json.loads((PACKAGE/"IRGS_Fantasy_Binding_v1_2_Core3_2.json").read_text(encoding="utf8"))
    registry=json.loads((PACKAGE/"Core/IRGS_Shared_Content_Registry_v1_0.json").read_text(encoding="utf8"))
    engine=(PACKAGE/binding["engine_file"]).read_text(encoding="utf8")
    def csvread(name):
        with (ROOT/name).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
    crosswalk=csvread("Fantasy_SCL_Crosswalk_v2_0.csv")
    cases=csvread("Fantasy_Acceptance_Cases_v2_0.csv")
    cmrr=csvread("Fantasy_CMRR_93_Sections.csv")
    current={x["entry_id"]:x for x in registry["source_bindings"] if x["source"]=="FL"}
    ck("L01-source-components",len(manifest["preserved_source_components"])==5 and
       all(SHA((ROOT/n).read_bytes())==h for n,h in manifest["preserved_source_components"].items()),
       "five current v2.0 components retained byte-for-byte")
    ck("L02-source-status","IRGS-FANTASY-LIB-2.0" in guide and "**Status:** **Proposed" in guide and
       "IRGS-CORE-3.2" in guide and "IRGS-SCL-1.0" in guide,"source status/pins preserved")
    selected=binding["fantasy_library"]
    ck("L03-selected-library",selected["document_id"]=="IRGS-FANTASY-LIB-2.0" and selected["version"]=="2.0" and
       selected["native_profile_compatibility"]["receiving_engine"]==binding["engine_id"],
       "Fantasy engine 1.2 selects library 2.0")
    ck("L04-source-coverage",len(projection["source_bindings"])==111 and
       {x["entry_id"] for x in projection["source_bindings"]}==set(current),"111 original FL references")
    ck("L05-source-equivalence",not projection_errors(projection,registry),"exact full normative source-binding equality")
    ck("L06-crosswalk",len(crosswalk)==111 and all(
       row["shared_reference"]==(current[row["legacy_entry"]]["release_ref"] or "") and
       row["selector"]==(current[row["legacy_entry"]]["selector"] or "") and
       row["source_payload_ref"]==current[row["legacy_entry"]]["original_payload_ref"] and
       row["original_payload_sha256"]==current[row["legacy_entry"]]["payload_sha256"]
       for row in crosswalk),"exact current reference/selector/payload crosswalk")
    native={x["adapter_id"]:x for x in registry["genre_adapters"]}
    ck("L07-native-adapters",len(projection["native_adapters"])==61 and
       all(native.get(x["adapter_id"])==x for x in projection["native_adapters"]),"61 native adapter records unchanged")
    payloads={x["block_id"]:x for x in registry["source_payload_blocks"]}
    ck("L08-native-payloads",len(projection["source_payload_blocks"])==168 and
       all(payloads.get(x["block_id"])==x for x in projection["source_payload_blocks"]),"168 immutable native payload blocks")
    scoped={x["entry_id"]:x for x in registry["retained_extensions"] if x["source"]=="FL"}
    ck("L09-scoped-extensions",len(projection["fantasy_scoped_extensions"])==16 and
       all(scoped.get(x["entry_id"])==x for x in projection["fantasy_scoped_extensions"]),"16 retained Fantasy scopes")
    ck("L10-reference-gates",sum(bool(x["shared_reference"]) for x in crosswalk)==95 and
       collections.Counter(x["reference_gate"] for x in projection["source_bindings"])==
       {"source_backed_hold":83,"selected_qualitative":12,"scoped_extension":16},"95 shared / 16 scoped; no hold promoted")
    expected={f"FAN-EXT-{n:03}" for n in range(1,8)}|{f"FAN-CRT-{n:03}" for n in range(1,6)}
    ck("L11-new-template-identities",len(projection["new_proposed_archetypes"])==12 and
       {x["id"] for x in projection["new_proposed_archetypes"]}==expected,"twelve optional source templates")
    ck("L12-template-procedure-links",all(x["engine_sections"] and x["owner_fields"] and
       all(f'id="fantasy-{n}"' in engine for n in x["engine_sections"]) for x in binding["new_fantasy_archetype_bindings"]),
       "existing Fantasy procedures and owner-qualified fields")
    ck("L13-no-template-promotion",not archetype_errors(binding,projection,registry) and
       selected["new_archetypes_automatically_enabled"] is False,"requirements/limits retained; opt-in only")
    ck("L14-acceptance-inventory",len(cases)==40 and {x["case_id"] for x in cases}=={f"FAN-{n:02}" for n in range(1,41)}
       and all("not executed in live runtime" in x["status"] for x in cases),"forty specified cases retain unexecuted live status")
    ck("L15-source-sections",len(cmrr)==93 and {int(x["old_section"]) for x in cmrr}==set(range(1,94)),
       "ninety-three original library sections accounted")
    disposition=manifest["source_file_dispositions"]
    omitted=[x for x in disposition if x["source_file"].startswith("provenance/")]
    ck("L16-clean-source-accounting",len(disposition)==11 and len(omitted)==2 and
       all("Omitted" in x["disposition"] for x in omitted) and not (ROOT/"provenance").exists(),
       "two full prior editions omitted and accounted; source payloads preserved")
    ck("L17-library-integrity",len(manifest["files"])==8 and all(
       (ROOT/n).is_file() and SHA((ROOT/n).read_bytes())==h for n,h in manifest["files"].items()),
       "current nine-file library deployment integrity")
    expected_rows=[]
    for block in projection["source_payload_blocks"]:
        p=block["payload"]
        if block["kind"]=="original_entry_payload" and isinstance(p,dict) and str(p.get("ID","")).startswith(("WPN-","ARM-","SHD-")):
            expected_rows.append("| "+" | ".join(str(v) for v in p.values())+" |")
    ck("L18-native-tables",len(expected_rows)==47 and all(row in guide for row in expected_rows),
       "47 exact source-native equipment rows retained")
    compatibility=selected["native_profile_compatibility"]
    ck("L19-complete-receiving-profile",compatibility["source_profile"]=="F-1.0/FL-1.0" and
       "Resilience" in compatibility["material_parameters"] and not selected["core_modified"] and
       not selected["shared_registry_modified"],"native chains linked; material parameter holds explicit")
    ck("L20-source-scope-separation",all(x["semantic_type_source"]==current[x["legacy_entry"]]["semantic_type"] for x in crosswalk)
       and next(x for x in binding["content_references"] if x["source_entry"]=="WPN-M-001")["semantic_type"]=="method",
       "historical type metadata does not overwrite normative unarmed method")
    bad=copy.deepcopy(projection)
    next(x for x in bad["source_bindings"] if x["entry_id"]=="WPN-M-006A")["selector"]="modes.thrust"
    bad_reg=copy.deepcopy(registry)
    bad_reg["aliases"].append({"alias":"FAN-EXT-001@2.0"})
    faults=[
        {"id":"LF01-v2-selector-redirection","detected":bool(projection_errors(bad,registry)),
         "mechanism":"new library projection redirects sword cut to thrust"},
        {"id":"LF02-proposed-template-canonicalized","detected":bool(archetype_errors(binding,projection,bad_reg)),
         "mechanism":"proposed Fantasy archetype falsely published as a shared alias"},
    ]
    return {"checks":checks,"fault_controls":faults}


if __name__=="__main__":
    r=verify()
    failed=[x for x in r["checks"] if not x["pass"]]
    missed=[x for x in r["fault_controls"] if not x["detected"]]
    print(f"Fantasy Library 2.0 receiving checks: {len(r['checks'])-len(failed)}/{len(r['checks'])}; fault controls: {len(r['fault_controls'])-len(missed)}/{len(r['fault_controls'])}")
    for x in failed+missed:print("FAIL",x["id"])
    sys.exit(1 if failed or missed else 0)
