# CI-OPT-001 — fail-closed scoped PR Research and INDEX (2026-10-11)

Parent [issue #355](https://github.com/definitely-stable/Mathlab/issues/355). **Infra branch only, never modify `main` or merge without review.**

## Verified baseline and root causes

At verified main `179d4b93ae9aaea8f837a6aeb9bf4843380d5764` there are **35 workflow YAML files**. Many dedicated DAG / UCT / import workflows already use `pull_request.paths`; changing their triggers wholesale would risk currently required checks and launch a large storm of self-triggered workflow runs.

The unconditional central workflows were:
- `.github/workflows/research.yml`: `pull_request`, `push main`, `workflow_dispatch`. Runs **four hosted independent Research shards** every PR plus a fail-closed fifth aggregate. The full main run #38127982456 (October 11) took about **10 minutes wall clock**. Many distinct named commands run inside these four jobs; the *141 named commands* in stacked HYP-105 #354 do **not** mean 141 concurrent runners, and those commands are NOT in main yet.
- `.github/workflows/index001-c5-page-epochs.yml`: unconditionally triggers its two independent INDEX math steps on every PR and main push.

Both workflows **already have PR concurrency cancellation**. Do not claim this change introduces that preexisting functionality. GitHub App does not have branch-protection read permission (403), so avoid deleting/renaming stable check identities.

## Chosen implementation, restricted evidence and acceptance

### Central Research routing

A dedicated short `scope` job now runs for **every event**. For PR events it checks out the ephemeral GitHub-constructed merge ref at `fetch-depth: 2`, demands a genuine 2-parent merge commit, and obtains the **actual changed file list vs its FIRST (base) parent** using the argument-array command `git diff --no-renames --name-only -z HEAD^1 HEAD`. Both the old and new paths of a rename are classified (`--no-renames` prevents rename detection from hiding a removed shared path). No untrusted PR title or path is interpreted in shell. Git checkout/diff errors or non-merge checkout FAIL the `scope` job and required aggregate instead of reporting a false green docs-only check.

`research/ci_scope.py` contains a conservative, explicit, **allowlist** with default FULL behavior:

| PR file scope | Hosted Research shards | INDEX C5 computations |
|---|---|---|
| Explicit safe prose (`README.md`, `docs/CURRENT_STATE.md`, research README, this policy note) | None; scope and aggregate still run | Skipped with visible message |
| Only `docs/research/catalog/**` Markdown/JSON | Foundation unit/source gates + catalog | Skipped |
| Only `research/hyp105_*.py` and `test_hyp105_*.py` | Foundation unit/source gates + both HYP shards | Skipped |
| Only `research/uct005_*.py` / `test_uct005_*.py` or `dag002_*.py` / `test_dag002_*.py` | LENT / UCT / INDEX foundation | Skipped |
| Only `research/index001_*.py` / `test_index001_*.py` | LENT / UCT / INDEX foundation | Runs |
| Known mixed changes | Union of directly relevant shards | Runs only if INDEX relevant |
| Unlisted scientific Markdown, shared / unknown code, manifests, scripts, YAML / CI policy | ALL FOUR shards | Runs |
| Full `push main`, `workflow_dispatch` or any unknown event | ALL FOUR shards (unchanged scientific coverage) | Runs |

Unknown/unsupported input is NEVER treated as safe documentation. The allowlist deliberately errs towards extra work to protect research soundness. In particular shared Python utilities, workflow and routing-contract edits always fall back to FULL. A scoped HYP PR still has its dedicated domain Contract whenever applicable. This implementation does NOT try to prove transitive Python dependency coverage; newly discovered cross-family imports must be added to the full-mode triggers before claiming safe isolation. Scientific Markdown is NOT intrinsically documentation-only: source-gate tests load files such as `docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md` and `docs/research/INDEX-001-G2-B4-C2-ADAPTIVE-PARTITIONS.md`. Unlisted docs therefore run FULL. Catalog and HYP changes retain the foundation all-unit gate, because otherwise existing source/pin or newly-added domain tests may not run.

### Required check compatibility and fail-closed results

The original `research-full-suite` **job name is unchanged**, and there is no workflow-level PR `paths` filter that could leave a required check stuck at Pending. It now depends on scope plus all four original shard jobs and uses `if: always()` (mandatory when prerequisites may be skipped).

- In FULL mode, every one of the four original jobs MUST return `success`, exactly as before.
- In scoped mode every explicitly selected job MUST be `success`, every unselected job MUST be `skipped`; any failure, cancellation, unknown selection or scope failure makes aggregate FAIL.
- In docs-only mode **all** four scientific shards must be skipped. The aggregate prints **SCOPED**, never dishonestly calls itself a full scientific pass.
- No original research command is removed, renamed or made optional for main pushes and manual full dispatch. Tests inspect the YAML job structure and keep the earlier shard invariants.

The original INDEX `exact-pins-and-crash-oracles` job remains present on every PR. It now fails on missing or invalid `index` output instead of silently skipping both mathematical steps. For unrelated/docs-only PRs, the **scientific INDEX steps** are skipped and the job prints a visible scope-exclusion reason. Both INDEX steps still run on relevant INDEX edits and all full events. This is intentionally different from workflow `paths` filtering, which could leave existing branch requirements waiting for a check that never appeared.

### Regression tests

New lightweight `research/test_ci_scope.py` includes adversarial path/mixed/unknown test cases, PR two-parent checkout and NUL-delimited diff mock checks, full-mode force checks, actual small-family route table, and verification that both original INDEX math steps share the same gate. `research/test_ci_research_shards.py` is amended to ensure the five old Research jobs and exact named commands remain, and that the new scope + aggregate detect an unsafe skip. These fast regression tests run in the lightweight scope job before routing is produced.

### Cache and concurrency: deliberate nonchanges

- **No cache of scientific outputs or frozen finite enumerations.** A cache key that omits a proof assumption, source, compiler or oracle version could incorrectly convert stale results into accepted evidence.
- The scripts inspected are pure Python standard-library for this slice; enabling a generic pip cache with no pinned package installation would not materially help.
- Existing PR cancel-in-progress in the two central workflows remains. Dedicated topic workflows lacking concurrency will be reviewed as a separate slice; touching every workflow at once would self-trigger many irrelevant Contract checks and make diagnosis harder.
- No self-hosted runner. Still `ubuntu-latest`, `actions/checkout@v4`, `actions/setup-python@v5` for scientific jobs.

## Expected savings versus proof contract

Pure docs PR: four heavy Research shards → **zero** heavy Research shards; INDEX's two scientific steps → zero. A narrow HYP PR: four Research shards → **three** (foundation including all unit/source checks + both HYP shards). A narrow INDEX/UCT PR: four → **one**. Catalog metadata: four → **two** (foundation + catalog). Explicit safe prose: four → **zero**. Unlisted scientific Markdown remains FULL until its doc/source dependencies are statically audited. Unknown changes still do FULL. `push main` and manually invoked Research continue to run all four unchanged.

These are **logical job-count reductions**, not claimed measured runner-minute speedups. Exact latest PR HEAD hosted checks must verify the new semantics and previous Research acceptance before integration. Also note that **already-open stacked PRs #347–#354 do not automatically inherit this main-based infra branch**: they will see the improvement only after their branch history incorporates the final merged implementation.

## Rollout and rollback

1. Execute dedicated fast scope-regression tests and the required Research four-shard FULL run on the CI-OPT PR (workflow modifications are explicitly unknown → FULL). INDEX also runs on the CI policy edit (fail-closed).
2. Verify the exact HEAD GitHub-hosted Research and INDEX outcomes. Exercise docs-only, HYP-only, INDEX-only, unknown path classifications in standalone tests; a real PR of each class can later exercise scheduling end to end.
3. After explicit merge authorization, monitor job names, branch protection and queue time. Rollback consists of reverting the routing and original INDEX steps, not deleting any mathematical oracle or evidence.

No mathematical HYP-105, UCT, DAG or catalog proofs are changed in this PR.
