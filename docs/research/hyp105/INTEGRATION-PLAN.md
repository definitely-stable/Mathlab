# RCP-001 — Integration and Retention Plan

Tracking: [#474](https://github.com/definitely-stable/Mathlab/issues/474); root [#230](https://github.com/definitely-stable/Mathlab/issues/230) is not resolved by these infrastructure changes. This file is **a procedure, not a live CI report**: recheck SHA, branch targets and workflow conclusions at integration time.

## Existing implementation chain

| Order | PR | Module | Base relationship |
|---|---|---|---|
| A | [#475](https://github.com/definitely-stable/Mathlab/pull/475) | Live GitHub PR inventory, integrity diagnostics and SHA checks | main |
| B | [#478](https://github.com/definitely-stable/Mathlab/pull/478) | Claim registry, mathematical models and ordered quantifiers | A |
| C | [#481](https://github.com/definitely-stable/Mathlab/pull/481) | Git proof-byte escrow, SHA-256 pins and scoped no-go ledger | B |
| D | [#482](https://github.com/definitely-stable/Mathlab/pull/482) | L0/L1/L2 living context and semantic delta | C |
| E | RCP-001-E child PR | Proof impact, model compatibility review and reproducible structured Markdown | D |

**This is already a legitimate stacked PR chain.** Do not create a second parallel duplicate stack, force-squash all research, or merge the deepest PR against main while its ancestors have not been integrated.

## Recommended integration after CI and review

1. Confirm the exact **current head SHA**, no parent base drift, no unresolved conflicts, and the required GitHub-hosted suites of the first PR. Review A diff **against main only** and merge A into main (a regular merge commit preserves ancestry and Git source objects; squashing is possible but requires careful subsequent rebasing/retargeting).
2. Retarget B against the new main **after A is integrated**, verify B's diff contains only the expected delta and run its checks on the new base. Merge B; repeat the same step for C, D and E.
3. Keep a parent branch until its dependent PR has been safely retargeted; avoid deleting a branch while an open child references it as its base.
4. For C explicitly verify that all 17 pinned original Git objects and the separate SHA-256 pin manifest are part of merged/retained history. A short-lived Actions artifact cannot substitute for this Git persistence.
5. Rebuild all five checked-in Markdown registers with the generator and assert `--check` PASS on the final integration tree.
6. Run a fresh RCP-D GitHub inventory, verify all sources, and perform the RCP-E impact pass comparing a retained before/after snapshot. Record integration SHAs and actual CI outcomes in the tracking issue; **do not fabricate acceptance status**.
7. Neither merging infrastructure nor 100% CI success closes scientific #230 or independently accepts any registered mathematical proof.

## Stacked PR versus a single integration PR

**Preferred:** five small, already-stacked PRs, integrated in A→B→C→D→E order with reviewable boundaries and retained Git ancestry. No added stack restriction is required.

**Alternative:** a single aggregate *review* of E's cumulative diff against main can aid a human auditor, but should not replace the individual semantic and CI checks. A separate aggregate merge PR would duplicate change tracking and could create conflicting branch bases; use only if a repository process explicitly requires it.

**Do not automatically merge:** administrative permission and green CI are necessary inputs, not unconditional authorization to publish or rewrite main. Always inspect merge conflicts, required checks, security and exact expected additions first.

## Stable documentation versus current-state artifacts

Five enduring generated Git files live in `docs/research/hyp105/registry/`: `RESULTS.md`, `FORMULAS.md`, `PROOF-GRAPH.md`, `PROTOCOLS.md`, `RESEARCH-MATRIX.md`. They contain mathematical statements, source links, equations in LaTeX, dependency tables, no-go scopes and operating protocols, with CI freshness checks.

Temporary *current-state* files `L0.md`, `L1.md`, `L2.md`, `snapshot.json` and `delta.md` are dynamically generated from GitHub and recorded scientific sources. Do not hardcode current PR numbers, current CI pass status, or main SHA inside the enduring formula/protocol documents.

The source of truth is registered JSON linked to original proof documents and retained Git blobs. The generated Markdown is deterministic readable navigation, not a new theorem acceptance authority.
