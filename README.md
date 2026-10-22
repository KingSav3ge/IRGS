# IRGS Engine Development ↔ independent QA

The user assigned Engine Development to implement/fix mechanics, and this cloud task to run IRGS, test and report. This branch is the shared QA handoff. It contains reports and testing tools only; it is not an Engine/App source branch or an IRGS release.

Read [LATEST.md](LATEST.md) for the latest tested candidate and reproduction steps. [LATEST.json](LATEST.json) contains named results, [CURRENT_REFS.json](CURRENT_REFS.json) identifies the observed source tips, and [HISTORY.json](HISTORY.json) records completed cycles. Previous reports remain in this branch's Git history. A green result applies only to its exact candidate commit and executed cases.

## Working cycle

1. Engine Development pushes a candidate/fix to `3.3.3.E` or integrated `main`. App candidates on `3.3.3.A` are also observed.
2. While the cloud environment and QA watcher remain running, it checks GitHub every 60 seconds. New commit/test-tool combinations are tested once in immutable verification extracts, through the canonical Engine and HTTP host with temporary synthetic save directories.
3. QA publishes results here, including stable finding IDs, the exact tested SHA, expected/actual behavior and reproduction steps. Raw logs and synthetic saves remain outside source in the cloud workspace.
4. Engine Development fixes the reported cause, adds suitable regression coverage, updates affected release hashes and manifest/evidence as required by AGENTS.md, and pushes a new candidate. It should retain the finding ID in its fix summary.
5. QA reruns the same contract on the new commit. A finding is marked `not_reproduced` only when its explicit check passes. New mechanics and changed public contracts also need active review and additional QA cases; the watcher cannot invent tests for every future system.

QA does not edit mechanics, silently merge code, refresh a candidate's integrity hashes, copy user saves, activate unfinished content, or certify full C2/Rise acceptance from the existing suite. Setup/infrastructure failures remain distinct from observed mechanics failures.

## Reproduce a report locally

Keep your canonical source checkout on the candidate branch; do not switch it to this report-only branch. Fetch the report branch and extract this small test script outside the source checkout:

```bash
git fetch origin refs/heads/qa/engine-validation:refs/remotes/origin/qa/engine-validation
git show origin/qa/engine-validation:qa_irgs.py > /tmp/irgs-qa.py
python -B /tmp/irgs-qa.py --source-root /path/to/IRGS --commit YOUR_FULL_CANDIDATE_SHA --output /tmp/irgs-qa/report.json
```

Use Python 3.12+ without `-O` and Node.js for the existing interface checks. `--independent-only` runs the additional live HTTP cases without replaying the ordinary regression suites. All instantiated campaigns are synthetic and temporary. The external historical-save fixture is explicitly skipped during the ordinary runtime suite.

The watcher is cloud/Linux tooling. To resume it in a running cloud environment after restoring its scripts:

```bash
python3 -B /workspace/irgs-cloud/qa/watch_irgs.py --repo /workspace/IRGS --storage /workspace/irgs-cloud/qa --interval 60
```

It needs the existing authenticated Git HTTPS proxy and permission to push only this QA artifact branch. It writes Git objects and that branch's reports without changing the checkout's HEAD, index, working files or Engine/App remote branches. Its lock prevents duplicate watchers. Fetch/publish errors are recorded and retried; failed publications reuse their completed results rather than repeating effects. Test processes and the watcher do not survive environment shutdown automatically; restart and verify them after restoration.

## Communication availability

Direct desktop thread reads currently return `connection closed before server request was answered`; no tool for sending to the existing Engine Development thread is available in this cloud session. This branch is therefore the actual shared communication channel. No message to that chat is claimed. Engine Development must read this handoff to participate in the cycle.
