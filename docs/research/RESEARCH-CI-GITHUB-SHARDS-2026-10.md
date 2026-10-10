# Research CI: lossless GitHub-hosted sharding, October 2026

**Motivation:** a run on PR #267, [run 38052499394](https://github.com/definitely-stable/Mathlab/actions/runs/38052499394), began executing on a hosted runner at 12:55:45 UTC and was cancelled at 13:05:45 UTC. It encountered the original research job's hard \`timeout-minutes: 10\` while executing the HYP-105 B3.2-E1-A full fixed-map census. The base research harness, unit tests, UCT-005 and INDEX-001 steps were already SUCCESS. This was **TIMEOUT**, not proof of failure in DAG-002, HYP-105 mathematics or acceptance of the whole suite.

## Implementation

Existing single 10-minute workflow job \`lent-001-foundation\` had **77 named sequential commands**. The workflows were split into four independently scheduled **GitHub-hosted ubuntu-latest** jobs, each with its own checkout and Python 3.x setup:

| Job | Existing commands preserved | Timeout |
|---|---:|---:|
| \`lent-001-foundation\` | 26 research harness, UCT-005 and INDEX-001 stages, including all \`unittest discover\` | 20 min |
| \`research-hyp105-foundation\` | 23 smaller HYP-105 stages | 30 min |
| \`research-hyp105-exact-census\` | 13 long HYP-105 census/flow stages | 90 min |
| \`research-catalog-and-primitives\` | 15 literature, catalog, TOM/HYP-002/G2B stages | 20 min |

**Mandatory aggregate status:** A fifth job, `research-full-suite`, runs after all four shards with `if: always()`. It inspects each `needs.<job>.result` and fails if any shard is FAILED, CANCELLED, SKIPPED, or otherwise not SUCCESS. It runs on GitHub-hosted `ubuntu-latest` and uses no checkout. **Branch protection should require `research-full-suite`** in addition to slice-specific checks; retaining only the legacy `lent-001-foundation` required status is insufficient. The aggregate verdict is not a fifth research workload and does not duplicate any of the 77 original commands.

**Change-time exact audit:** the old and new workflow each have **77** named steps and the original list of **77 run commands matches exactly in the same order**. Nothing in the mathematical scripts was modified. The existing \`lent-001-foundation\` required-check job name is preserved, but **it alone is not a sufficient acceptance gate**: all four research jobs and every focused slice workflow must conclude SUCCESS for the exact accepted SHA.

## Guarantees and limitations

- This is a CI orchestration refactor, not a scientific theorem or proof.
- Jobs are independent workspace snapshots; if an old command implicitly relied on an untracked artifact produced by a preceding command, that would be a dependency bug exposed by hosted runs. All newly separated scripts are intended to be self-contained, and **hosted CI must confirm this**.
- The longest HYP-105 census can still fail by its 90-minute timeout; do not auto-merge or substitute incomplete evidence.
- Parallel jobs increase concurrent runner demand but retain GitHub-hosted-only constraints.
- Regression test \`research/test_ci_research_shards.py\` checks the four research shard jobs and their aggregate verdict, Ubuntu runner setup, at least 77 unique checks, their required sentinels and placement of the time-consuming census. More research checks can be appended in future without requiring an exact count of 77.
- Do not use this refactor to override previously required full CI gates for PRs #267, #268, #271, #274, #275, #276. Those heads need appropriate post-integration runs (and any required branch update) before merge.

**Acceptance:** exact-head workflow CI succeeds on this branch; then merge this CI-only PR before updating pending research branches. No force-push or self-hosted runners.
