#!/usr/bin/env python3
"""Offline qualification of selected player-start readiness and Core outcomes."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import platform
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'IRGS_3_3/runtime'))


def qualify():
    suite=unittest.defaultTestLoader.loadTestsFromName('test_start_readiness')
    names=[]
    def inventory(items):
        for case in items:
            if isinstance(case,unittest.TestSuite): inventory(case)
            else: names.append(case.id())
    inventory(suite)
    output=io.StringIO(); result=unittest.TextTestRunner(stream=output,verbosity=1).run(suite)
    if not result.wasSuccessful() or result.skipped: raise RuntimeError(output.getvalue())
    paths=['IRGS_3_3/runtime/'+n for n in ('start_readiness.py','test_start_readiness.py',
        'starting_selection.py','character_background.py','historical_campaigns.py','scene_setup.py',
        'scene_actions.py','shared_runtime.py','runtime_contracts.py','core_world.py','player_actions.py',
        'r9_runtime.py','r8_dependencies.py','phase_contract.py','process_runtime.py','offline_responses.py')]
    paths += ['IRGS_3_3/data/'+n for n in ('henry_1415_observation.json','hyw_1415_opening.json',
        'solo_quay_opening.json','coc_local_delivery.json','responses/depot_v1/library.json')]
    return {'schema_version':1,'status':'PASS_SELECTED_START_READINESS_WITH_LIMITS',
        'date':'2026-10-26','target_iteration':'IRGS 3.4.2 development','python':platform.python_version(),
        'api_schema':'irgs-start-readiness-1','instruction_base':'e283c57ad5b44ad688bc38586ca16980f4dd0bf1',
        'early_api_commit':'ea3b9a24f3254b4e230469b31843abad6c25fdf2',
        'tests_run':result.testsRun,'passed':result.testsRun,'skipped':len(result.skipped),'test_ids':names,
        'assessment_findings':['IRGS-PLAY-001','IRGS-PLAY-002','IRGS-PLAY-004'],
        'existing_person':{'actor':'HYW-HENRY-V','entry':'hyw-1415','opening_id':'henry-1415-embarkation-v1',
            'placement':'Sourced broad Portchester/Solent embarkation setting only; conflicting boarding accounts retained',
            'operation':'execute_player_scene_action','action_id':'observe-embarkation',
            'actual_effects':'One new actor-received established observation, 20 selected simulation seconds, no stock or authority grant',
            'duration_is_historical_measurement':False,'civil_calendar_advanced':False,
            'john_bedford':'Eligible personal declarations; playable context held for missing legitimate operational setting'},
        'review':'All 37 dated entries distinguish verified references and eligibility from declaration-only default existing modes; optional sourced Henry mode and authored new-character mode are explicit',
        'other_contexts':['Existing reviewed fictional quay observation with actual dispatch retained',
            'Actual Rise inspection through shared acceptance', 'Generic profile with unknown civil date'],
        'time':'Received initial Julian checkpoint, day precision, no hour; causal sequence/storage/selected elapsed/civil binding remain distinct',
        'information':['Public creation review is out of character','Actor DTO excludes pre-creation date/reference fields',
            'No received record means no context/calendar fallback from template', 'No full template or private dependency evidence',
            'No historical template/pack reload during view or restore', 'No hidden resource/authority feasibility menu'],
        'authority_and_conflicts':['Actual Core current-control check', 'Actual actor process reservation rejection retains R9 reads',
            'Conflicting observation frontier defers both in either order','Conserved stocks unchanged; no rank-based operational permissions'],
        'recovery':['Mandatory explicit acceptance and host CAS','Failed-save rollback','Native exact AcceptedIntent JSON restart',
            'Lost-ack reload/original-result replay','Concurrent delivery once','Changed identity/stale state rejection',
            'Discarded-future branch/restore fencing','No repeated initialization', 'Content change after review/install rejected'],
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'provider_calls':0,'model_tokens':0,'user_saves_used':False,
        'remaining':['App readiness/mode selection, actor-known and civil-date UI, compatible pins and coordinator exact-set qualification',
            'Catalog independent source requirements/consumer cases for this new schema',
            'John and other historical persons lack reviewed operational starts; no all-actor playability claim',
            'IRGS-PLAY-003 supported-intent mapping and general freeform/NPC resolution remain open',
            'Selected travel extension follows this start increment; broader DEV/C2 remains open']}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--output',type=Path)
    args=parser.parse_args(); report=qualify()
    if args.output: args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({k:report[k] for k in ('status','tests_run','passed','skipped')}))
