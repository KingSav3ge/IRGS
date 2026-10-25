"""Publication boundaries and package identities follow the user release policy."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import json
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from check_publication_version import permitted
from versioning import release_metadata, archive_name
import watch_component_qa as watcher


class VersionPolicyTests(unittest.TestCase):
    def test_patch_rollover_and_candidate_requirements(self):
        for old, new, allowed in [('3.4.0','3.4.1',True), ('3.4.1','3.4.1',False),
                ('3.4.1','3.4.3',False), ('3.4.9','3.5.0',True),
                ('3.4.9','3.4.10',False), ('3.4.1','4.0.0',False)]:
            with self.subTest(old=old, new=new):
                self.assertEqual(permitted({'version':old}, {'version':new}), allowed)
        self.assertTrue(permitted({'version':'3.4.1'}, {'version':'4.0.0-candidate.1',
            'channel':'candidate', 'candidate_assessment_ref':'MILESTONE.md'}))

    def test_package_uses_metadata_and_records_previous_release(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            (root/'VERSION.json').write_text(json.dumps({'schema_version':1,
                'version':'3.4.1','previous_version':'3.3.3','channel':'development'}))
            self.assertEqual(archive_name(root), 'IRGS_3_4_1_Development.zip')
            self.assertEqual(release_metadata(root)['previous_version'], '3.3.3')
            (root/'VERSION.json').write_text('{"schema_version":1,"version":"../oops"}')
            with self.assertRaises(ValueError):archive_name(root)

    def test_watcher_retains_report_without_a_commit_or_push(self):
        from types import SimpleNamespace
        import hashlib
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);report=root/'report.json'
            report.write_text('{"status":"passed"}')
            refs=dict(joined='j',engine='e',app='a',catalog='c')
            signature=hashlib.sha256((watcher.ROOT/'tools/qa_irgs.py').read_bytes()+Path(watcher.__file__).read_bytes()).hexdigest()
            identity='e:a:c:'+signature
            state={'runs':{identity:{'report_path':str(report),'attempted_at':0}}}
            args=SimpleNamespace(**refs)
            def read_pin(repo,*args,**kw):
                self.assertEqual(repo,'a')
                self.assertEqual(args[0],'rev-parse')
                return SimpleNamespace(stdout=b'e' if args[1].endswith(':Engine') else b'c')
            with patch.object(watcher,'tip',side_effect=lambda repo:repo), patch.object(watcher,'git',side_effect=read_pin) as commands:
                self.assertTrue(watcher.cycle(args,state))
                self.assertTrue(state['runs'][identity]['retained_locally'])
                self.assertFalse(watcher.cycle(args,state))
                self.assertNotIn('last_publication',state)
                self.assertEqual(commands.call_count,4)
