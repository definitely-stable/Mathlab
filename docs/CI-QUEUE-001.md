# CI-QUEUE-001 — Research queue deduplication policy

Issue: [#350](https://github.com/definitely-stable/Mathlab/issues/350).

## Verified diagnosis

The full Research suite is CPU-bound exact scientific validation, not an install-heavy dependency pipeline. It includes separately hosted independent shards and a fail-closed aggregate. The former generic trigger pair, `push: research/**` and `pull_request`, launched duplicate whole-suite runs for ordinary open research PRs. Generic INDEX-001/DAG-002 workflows had the same double trigger (some guarded by path filters). Multiple commits in a PR may enqueue superseded runs, competing for hosted workers.

No pip installation is performed in the Research workflow; adding `setup-python.cache: pip` without dependency files or package installs does not cache GF(5)/DAG computations. Exact census outputs are not safe to reuse as CI proof without a separately reviewed versioned input provenance, content binding, independent validation and adversarial negative tests. No scientific verdict is cached by this change.

## Scope — eight general workflows

- `research.yml` (full suite, all preserved shards)
- `index001-c5-page-epochs.yml`
- `dag002-g1c-online.yml`
- `dag002-g2a-source-gate.yml`
- `dag002-g2b2-felsner.yml`
- `dag002-g2b2c-paid-ledger.yml`
- `dag002-g2b-record-anchors.yml`
- `dag002-g2b2-power-anchors.yml`

For each, only the redundant generic research-branch push event is removed. `push: main`, existing `pull_request` and its path filters, all hosted jobs, timeout settings, command names, scientific inputs and the fail-closed full-suite gate remain unchanged. A `workflow_dispatch` event permits manual testing before a PR is opened.

## Concurrency semantics (no cross-PR cancellation)

Group by `github.workflow` plus PR number for pull requests; use the unique `github.run_id` for main pushes and manual dispatch. Set `cancel-in-progress` **true only for pull requests**.

| Event | Scheduled automatically | Cancel older run |
| --- | --- | --- |
| PR opened / updated, any branch | Yes (subject to existing paths) | Yes, only same workflow and same PR |
| Push to `main` | Yes (subject to existing paths) | No |
| Push to `research/**` without PR | No | N/A |
| Manually dispatched on a ref | Explicit action | No |

CI acceptance must still be based on the **exact latest PR HEAD** and all mandatory GitHub-hosted checks. A superseded commit's canceled run is not evidence of success; neither is a cached witness or a partial shard success.

## Scope exclusions and follow-up

Dedicated topic-specific workflow push triggers are intentionally unchanged. Some allow only `pull_request.branches: [main]` yet need branch push checks for stacked PRs; blanket deletion or cross-event cancellation could silently remove acceptance. An active stack based on an unmerged research branch will not inherit new workflow triggers until the relevant configuration is integrated into its base/head. Existing queued runs cannot be retroactively removed by this change.

This policy does not change GitHub-hosted runner capacity or guarantee shorter queue times under many distinct simultaneous PRs. Later investigate job timing distribution and deterministic intermediate-result reuse in a separate evidence-backed issue, before considering any cache. Test policy: `python -m unittest discover -s research -p 'test_ci_queue_dedup.py' -v`; full `research-full-suite` remains mandatory.
