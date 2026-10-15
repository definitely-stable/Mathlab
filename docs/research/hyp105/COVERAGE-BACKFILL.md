# HYP-105 — RCP-COV-001: research claim/evidence coverage audit

Tracking: [RCP-001 / issue #474](https://github.com/definitely-stable/Mathlab/issues/474); scientific [HYP-105 / #230](https://github.com/definitely-stable/Mathlab/issues/230). The A→E infrastructure is already integrated into main. **This tool discovers missing registrations but does not prove or automatically register a mathematical claim.**

## Why this audit matters

The initial production Claim Registry documents seven scoped mathematical claims from five original research PRs, with 17 pinned original proof/oracle/test/witness files and five no-go entries. Research has advanced through the exact all-seven ORIGINAL incidence-ID join, conditional D6 lower bounds and further source-forest/cycle kernels. A count of open PRs is not a count of claims or theorems.

Until new source proofs, quantifier scopes, model definitions, original source Incidence-ID semantics and certificates have been reviewed, these PRs must **not** be auto-imported as formally accepted theorems or merged into scientific main merely because their own CI succeeded.

## Live reproducible workflow

```bash
GITHUB_TOKEN=... python -m research.rcp.context_builder \
  --output /tmp/hyp105-cov-current --check-claim-prs

python -m research.rcp.coverage_audit \
  --snapshot /tmp/hyp105-cov-current/snapshot.json \
  --output /tmp/hyp105-cov-queue
```

Outputs:

- `coverage.json` — full open HYP-105 title/body-matched PR queue, evidence/claim registry counts, pinned-source coverage, exact parent/HEAD/CI observation metadata, stable evidence references, and information gaps.
- `coverage.md` — a searchable Markdown table of currently unregistered research PRs. Discovery tags `ALL_H`, `GF5`, `ORIGINAL`, `JOINT`, ```UENCHED` and `NO_GO` are **unverified title heuristics**, not semantic proof classification. Full queue, no arbitrary count cap.
- The input Qqsnapshot.json` is self-integrity-checked and explicitly represents non-atomic GitHub API state. Archived snapshots can be replayed, but should never be described as fresh.
- A source PR absent from the open inventory is `NOT_IN_OPEN_PR_INVENTORY` and **not** automatically labelled merged, rejected, or invalid.

## Immediate high-value scientific backfill candidates

Inspect the exact proof documents, not just PR descriptions. Suggested distinct records (scopes must be confirmed independently before adding to Claim Registry):

| Source | Logical work to register separately | Non-implication / major risk |
|---|---|---|
| [#476](https://github.com/definitely-stable/Mathlab/pull/476), AA4-Q | Exact all-h seven-GF5 ORIGINAL six-incidence-ID two-sided join and C/C source girth obstruction | Identity is not universal lower bound on joined intersections |
| [#480](https://github.com/definitely-stable/Mathlab/pull/480), AA4-R-CYC | Every-fixed-map conditional expected genuine D6 lower, with exact GQ model | Conditional expectation does not imply a worst-case simultaneous min(f,g) |
| [#479](https://github.com/definitely-stable/Mathlab/pull/479), AA4-S | All-h source-root marginal-only Fréchet method NO-GO | Defeats marginal-only inference, not all correlated source-root methods |
| [#484](https://github.com/definitely-stable/Mathlab/pull/484), AA4-T | All-h connected cycle tensor and aligned D6 quenched expectation | Fixed one side and random global opposite side; no deterministic all-f,g claim |
| [#486](https://github.com/definitely-stable/Mathlab/pull/486), AA4-U | Genuine six-original-incidence source forest and nine-cell Fréchet transport | Cell-level marginal inequalities may all have zero floors |
| [#487](https://github.com/definitely-stable/Mathlab/pull/487), AA4-U-CYC | Joint conditional original line-overlap cycle gluing kernel | Covariance kernel and W32 witness are not universal global lower |

Other valid research may be older or lack title/body tags; this is a **pilot triage** rather than a globally exhaustive mathematical census.

## Actual scientific record admission criteria

1. Validate source PR stage, exact HEAD, original proof path, Git blob SHA and the physical/source mathematical model directly. Separate **every mathematically distinct quantifier mode** (all-h deterministic, conditional expectation, finite witness, scoped no-go).
2. Record a unique mathematical claim ID, correct ordered quantifiers (including domain h and global injection), external proof dependencies, limitations and the status `DOCUMENTED_IN_DRAFT / NOT_REVIEWED / NOT_ASSESSED` until independently accepted.
3. Retain byte-exact original proof, oracle and independent test source under an archive alias in Git with original Git blob SHA and independent SHA-256 pins. Add a source-linked evidence receipt and negative-knowledge entry only when a genuine invalid inference is identified.
4. Add carefully scoped equations to the canonical formulas registry, regenerate five permanent Markdown registers (\`RESULTS.md\`, \`FORMULAS.md\`, \`PROOF-GRAPH.md\`, \`PROTOCOLS.md\`, \`RESEARCH-MATRIX.md\`) and verify their byte parity.
5. Rebuild live snapshot/impact and execute GitHub-hosted tests. Never turn a positive expected value or finite counterexample into root A/B/C theorem acceptance.

## Integrity and adoption boundaries

CI success, issue state, a PR title or a matching discovery keyword are not scientific evidence. The observer cannot prove its own completeness relative to all research statements in the repository. **No limit** on open PRs, branch depth or number of claims is imposed. Never use issue-closing keywords around the scientific root issue number in a PR body, even in a negated sentence: an earlier metadata description triggered an unintended GitHub closure which was explicitly corrected.

This COV-001 slice is a coverage **diagnostic**, not RCP-001-F workflow consolidation or a claim that the missing PRs are already imported.
