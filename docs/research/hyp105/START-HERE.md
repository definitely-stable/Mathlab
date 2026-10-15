# HYP-105 — start here

Root mathematics: [#230](https://github.com/definitely-stable/Mathlab/issues/230); parents [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169). The issue text is the normative model and Branch A/B/C gate. A CI success is not a theorem proof.

## Live branch and PR inventory

The repository `main` is **not** necessarily the latest research branch: many HYP-105 results are stacked in unmerged Draft PRs. Verify current HEADs and base links from GitHub rather than reusing a historical status summary.

Using Python 3.12 and a GitHub API token with read-only repository access:

```bash
GITHUB_TOKEN=... python -m research.rcp.github_inventory \
  --repo definitely-stable/Mathlab \
  --output /tmp/mathlab-rcp
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
This page documents RCP-001-A inventory, RCP-001-B Claim Registry, and RCP-001-C evidence escrow/no-go capabilities below. **It is not a live deployment or merge-status report.** Resolve branch HEADs, CI status and milestone acceptance from current GitHub metadata and tracking issue #474. Proof-impact analysis, semantic Research Delta and workflow consolidation are tracked as separate future slices; never infer their availability from the plan alone.

Validate locally or on GitHub-hosted CI:

```bash
python -m unittest research.test_rcp_inventory -v
```

## Structured claims and proof links

RCP-001-B adds the [Claim Registry](CLAIM-REGISTRY.md): explicit mathematical quantifiers, shared model definitions, immutable identifiers, SHA-pinned source proof blobs, DAG dependencies and non-implication boundaries. Rebuild the current deterministic research claim index with `python -m research.rcp.claim_index --output /tmp/rcp-claims --verify-sources` (GitHub API read token recommended). The claim index records draft-stage mathematics, **not** independent acceptance; the open PR ancestry/CI inventory is provided by RCP-001-A above.

## Durable evidence and negative results

RCP-001-C adds the [Evidence & No-Go Ledger](EVIDENCE-AND-NOGO.md): permanently identifiable Git object escrow of selected five proof documents, corresponding oracle and test sources and two frozen witness fixtures, as well as five machine-linked non-implication/no-go records. Run `python -m research.rcp.evidence_ledger --output /tmp/rcp001c` for an offline SHA-verified index or add `--verify-originals` to cross-check the 17 original files at their exact GitHub commit references. These gates verify byte identity, not the correctness or novelty of mathematical assertions; root #230 stays OPEN.

## Current research context and delta

RCP-001-D adds [Living Research Context](LIVING-CONTEXT.md): fresh L0/L1/L2 GitHub + mathematics + escrow views, a sealed snapshot and semantic change reports. From repository root run:

```bash
GITHUB_TOKEN=... python -m research.rcp.context_builder \
  --output /tmp/hyp105-current --check-claim-prs
```

The resulting `snapshot.json` has a SHA-256 self-integrity check and non-atomic provenance flags. Compare with a previous `snapshot.json` using `python -m research.rcp.context_delta --before OLD --after NEW --output DIR`. Do not substitute a cached snapshot for a current GitHub query; do not infer global mathematical acceptance, merge, or CI success from a changed timestamp.
