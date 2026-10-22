# Current component QA

Independent Engine/App changes are tested as disposable assembled candidates. Reports at `current_report.md` and `current_report.json` identify both published component commits, the App's declared Engine pin and the local candidate commit. A proposed newer Engine/App pair is not the same as an integrated or deployed release.

Run from joined IRGS with clean component repositories available:

```bash
python -B tools/watch_component_qa.py --interval 60
```

The watcher fetches only `main` from the Engine, App and joined repositories. New Engine/App commits or QA-tool revisions trigger current regression and independent HTTP checks. A separate process assembles exact committed source into a new temporary verification directory, uses temporary synthetic campaigns and preserves runner failures as blocked. Component source is neither changed nor merged.

The watcher publishes only reports and their development-manifest entries to joined `main` using an isolated Git index and normal fast-forward pushes. Concurrent writers are retained; publication retries against the newer parent. It creates no report branch and does not move the App dependency pin or the joined component pointers. The local checkout may then be behind `origin/main`; inspect and fast-forward normally when clean.

Checks run only while this cloud machine and watcher process remain active. Start it again after restoration; no process survival or automatic restart is assumed. Existing scripted checks do not qualify every future mechanic or all C2 cases. New capabilities need additional active review and appropriate cases.

Engine development owns mechanics fixes. This QA workflow runs them and reports results; it sends no direct messages to an inaccessible development chat. See `provenance/qa_handoff` for the retired report branch's inherited evidence.
