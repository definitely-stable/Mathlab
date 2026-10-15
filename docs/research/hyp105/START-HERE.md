# HYP-105 — start here

Root mathematics: [#230](https://github.com/definitely-stable/Mathlab/issues/230); parents [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169). The issue text is the normative model and Branch A/B/C gate. A CI success is not a theorem proof.

## Live branch and PR inventory

The repository `main` is **not** necessarily the latest research branch: many HYP-105 results are stacked in unmerged Draft PRs. Verify current HEADs and base links from GitHub rather than reusing a historical status summary.

Using Python 3.12 and a GitHub API token with read-only repository access:

```bash
GITHUB_TOKEN=... python -m research.rcp.github_inventory \
  --repo definitely-stable/Mathlab \
  --output /tmp/mathlab-rcp \
  --check-pr 471
```

Produces `inventory.json` (full open-PR record, parent DAG, exact head/base SHAs, scoped CI and diagnostics) and `inventory.md` (human-readable HYP-105 open PR and ancestry index). `--checks-all` optionally verifies GitHub check runs for **every open PR**; this makes additional API requests, so it is not the default. Each `--check-pr` must identify a currently open PR. Missing CI examination means `NOT_INSPECTED`, not success. `UNKNOWN` means no checks returned for the selected SHA.

GitHub REST pagination is followed to completion and duplicates fail closed. The result is explicitly **non-atomic**, because GitHub can change while multiple API pages are read. Exact HEAD check successes only cover the queried SHA; they do not independently validate mathematical claims. Missing/deleted open parents, base SHA drift and forks are reported instead of silently inferred.

## How to continue research safely

1. Read the unchanged root Branch A/B/C target in issue #230.
2. Build a fresh inventory and inspect the latest relevant PR, parent SHA, proof document and check runs.
3. Read any superseding statements and known counterexamples (see [known/stopped registry](../KNOWN-AND-STOPPED-RESEARCH.md) and [decisions](../DECISIONS.md)).
4. Identify the *precise* missing lemma or counterfamily without upgrading a conditional or finite result to a universal theorem.
5. Preserve source ORIGINAL six distinct incidence IDs, true W(3,2^h), typed global injections, physical projections and GF(5) palette semantics.

## RCP implementation

Tracking: [HYP105-OPS-001 #474](https://github.com/definitely-stable/Mathlab/issues/474).
Current implemented slice: **RCP-001-A**, only PR ancestry inventory and optional CI checks. Claim registry, durable certificates, proof-impact analysis, research delta and research workflow consolidation are later independent slices; this document makes no claim those are implemented.

Validate locally or on GitHub-hosted CI:

```bash
python -m unittest research.test_rcp_inventory -v
```
