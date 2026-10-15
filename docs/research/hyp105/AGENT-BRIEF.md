# HYP-105 — Research Work Brief

**Single-link handoff for continuing HYP-105 research.** Stable instructions, **not** a cached status report or an endorsement of any draft proof. Read from the current `main`, not a historical commit URL.

## Mathematical objective

[Root issue #230](https://github.com/definitely-stable/Mathlab/issues/230) is the authoritative mathematical model and Branch A/B/C acceptance gate. Preserve true original `W(3,2^h)` for every `h >= 1`, globally injective typed point/line maps to physical coordinate pairs, six **distinct original incidence IDs**, the same six source IDs on both sides, all seven accepted GF(5) classes, and all cross-map correlations.

Target one rigorously supported outcome:
- **A:** a uniform positive `Omega(s^6)` lower bound for the seven-class sum `S_s(f,g)` for **every** legal pair `f,g`.
- **B:** an explicit infinite correlated family with a rigorous `o(s^6)` bound for that sum (not, by itself, an R3/ASET upper bound).
- **C:** an exact reduction satisfying the requirements in root #230, with stated restrictions and independent falsifiers.

New exact identities, finite computations, conditional expectations, averaged bounds, or proof-method limitations are useful **partial progress**; none alone closes A/B/C. Passing CI validates artifacts, **not** an all-h proof.

## Procedure — run for each new assignment

1. Read [#230](https://github.com/definitely-stable/Mathlab/issues/230) and the [research index](START-HERE.md). Use [#474](https://github.com/definitely-stable/Mathlab/issues/474) for research-continuity tooling, not as a substitute for mathematical scope.
2. Refresh live GitHub state: `main` HEAD; all relevant open scientific and infrastructure PRs, **including parallel stacks**; exact PR head/base SHA, ancestry, proof files and selected exact-HEAD checks. Do not select a PR solely by recency or reuse a previous summary. Uninspected CI is `NOT_INSPECTED`, not PASS; GitHub inventory is non-atomic.
3. Read relevant [registered results](registry/RESULTS.md), [proof graph](registry/PROOF-GRAPH.md), [formulas](registry/FORMULAS.md), [known/stopped research](../KNOWN-AND-STOPPED-RESEARCH.md) and [decisions](../DECISIONS.md). The registry covers only **registered** results and can lag scientific Draft PRs. Inspect the actual source proof and no-go scope before relying on it.
4. If the assignment specifies a PR/slice, pursue that scope. Otherwise select the most useful **unresolved mathematical lemma, implication or counterfamily** toward A/B/C, checking for competing or overlapping work. State the missing step, exact quantifiers, and why it is not already proven. Prefer proof advancement over unrelated registry backfill unless missing provenance blocks the work.
5. Implement in a separate branch/compatible Draft PR: a proof or precisely scoped partial theorem, derivation, explicit assumptions and non-implications, source references, independent oracle/falsifier(s), adversarial tests and any finite witness. Validate locally where possible and with GitHub-hosted CI. Do not silently rewrite proof history, merge without the integration gate below, close #230 without its proof gate, or conflate exact-HEAD green checks with mathematical review.
6. Persist a slice-specific mathematical Markdown document and reproducible code/tests/fixtures in Git. For provenance/claim imports use the [Claim Registry](CLAIM-REGISTRY.md), [Evidence & No-Go Ledger](EVIDENCE-AND-NOGO.md), and [Proof Impact](PROOF-IMPACT.md). Canonical structured metadata is under `research/rcp/hyp105/`; rebuild derived `registry/*.md` with `python -m research.rcp.structured_docs --write` and validate with `--check`, never hand-edit generated pages. Separate draft documentation, independent proof review, and root gate acceptance.

To collect a fresh research snapshot (with GitHub read access configured):

```bash
python -m research.rcp.context_builder --output /tmp/hyp105-live --check-claim-prs
```

See [Living Context](LIVING-CONTEXT.md) for credentials, exact-HEAD checks and snapshot limitations. If live checks are unavailable, mark facts `UNKNOWN` instead of inventing current status.

## Integration gate — when the assignment asks to finish through merge

An explicit instruction to integrate authorizes pursuing the merge, **not** skipping acceptance. Treat each PR separately; do not merge scientific Draft stacks merely because a small documentation PR is ready.

1. **Scope and ancestry:** inspect the *current* target branch, final exact PR head SHA, complete diff, review state, permissions, required GitHub-hosted checks, parent PRs and base drift. For dependent stacks integrate or retarget in ancestor-to-descendant order; do not merge the deepest child against the wrong base, force-push shared history or silently discard an independent research branch.
2. **Scientific proof PR:** independently review the actual statement, all-h quantifiers, original six-ID semantics, complete-map correlation, proof dependencies and independent falsifiers. Require mathematical acceptance **separately** from CI before converting a proof Draft to ready/merging. For a partial theorem, state precisely what is and is not proved. Never auto-promote root Branch A/B/C or close #230 based on a merged partial claim.
3. **Documentation or research infrastructure PR:** verify the confined diff and source links, deterministic register parity if applicable, tests and exact-HEAD CI; confirm it introduces **no mathematical proof promotion**. An independently reviewable, non-scientific slice may merge directly into `main` when checks, repository protections and the requested integration scope permit it.
4. **Final merge:** recheck the exact head/base and review/CI state immediately before merge, use an expected-HEAD guard when available, and verify the merge result. Do not report `MERGED` unless GitHub confirms it.
5. **After merge:** fetch the updated `main` commit and confirm the intended files/results survived. Check post-merge `main` workflows on that exact commit if visible. If checks are pending or not queryable, state `POSTMERGE_CI_UNVERIFIED`, **not** SUCCESS. Preserve issue #230 as open until its own independent Branch A/B/C acceptance gate is met.

If any required approval, exact-head check, parent dependency or merge permission is absent, stop **that** integration with a concrete blocker and next allowed action; preserve the reviewed Draft PR rather than claiming an unperformed merge.

## Deliverables and handoff

Report concisely: **mathematical result and exact scope; what is not proved; files/PR changed; reproducible tests and CI SHA; next missing lemma; stacking and integration recommendation**. End with this *verified* block (unknowns are allowed):

```text
Last verified HEAD:
Current milestone:
Current slice:
Open PR:
Last CI:
Acceptance:
Known blockers:
Next allowed action:
Last updated from repository:
```

Only report `PROVED_A`, `COUNTEREXAMPLE_B` or `RESTRICTED_THEOREM_C` when the corresponding root #230 requirements are met. Otherwise say `OPEN_WITH_FORMAL_BLOCKER` or explicitly scoped partial progress.

## Additional reference, not a prerequisite reading list

[Full index](START-HERE.md) · [research matrix](registry/RESEARCH-MATRIX.md) · [protocols](registry/PROTOCOLS.md) · [integration plan](INTEGRATION-PLAN.md). Do not impose arbitrary limits on PR count, stack depth, or scientific exploration.
