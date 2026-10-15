# HYP-105 / RCP-001-D — Living Research Context and Semantic Delta

Tracking: [HYP105-OPS-001 #474](https://github.com/definitely-stable/Mathlab/issues/474). Base: RCP-001-C, after [PR #481](https://github.com/definitely-stable/Mathlab/pull/481). Mathematical root: [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Source of mathematical truth remains the pinned original scientific documents and their actual proofs, not these generated summaries.

## Goal

Enable reconstruction of the actual current research frontier from **three separately validated data domains**: (A) all live GitHub open PRs/branches/check runs, (B) the claim registry with ordered quantifiers and an explicit proof dependency DAG, and (C) durable byte-identical Git proof/oracle/witness escrow with scoped no-go boundaries.

Generate **derived artifacts**, never hand-maintained status SHA copies.

## Commands

Use Python 3.12 and a GitHub token with read access to repository, issues, PRs and checks.

To capture a fresh live snapshot (no claim that GitHub supports atomic collection):

```bash
GITHUB_TOKEN=... python -m research.rcp.context_builder \
  --output /tmp/hyp105-current \
  --check-claim-prs
```

To include a selected research PR's exact HEAD check runs:

```bash
GITHUB_TOKEN=... python -m research.rcp.context_builder \
  --output /tmp/hyp105-current \
  --check-pr 471 --check-claim-prs
```

To compare with a preserved previous context (for example, a downloaded earlier GitHub-hosted CI artifact):

```bash
GITHUB_TOKEN=... python -m research.rcp.context_builder \
  --output /tmp/hyp105-next --previous /tmp/hyp105-previous/snapshot.json \
  --check-claim-prs
```

Compare arbitrary two previously verified snapshots **without GitHub access**:

```bash
python -m research.rcp.context_delta \
  --before /tmp/hyp105-previous/snapshot.json \
  --after /tmp/hyp105-next/snapshot.json \
  --output /tmp/hyp105-delta
```

Offline replay without claiming freshness:

```bash
python -m research.rcp.context_builder \
  --snapshot-in /tmp/hyp105-next/snapshot.json \
  --output /tmp/hyp105-replayed
```

## Output layout

- `snapshot.json` — complete machine-readable observation and research registry, with SHA-256 content self-check (integrity **only**, not authenticated provenance). Includes actual root #230 and operations #474 issue states; current main SHA; all open PRs; exact head and base SHAs; selected check-run states; parent DAG and drift warnings; 7 initial mathematical claim records; exact pinned proof references; 5 evidence receipts; 5 no-go records; 17 SHA-verified escrow identities.
- `L0.md` — short answer-first state: issue state, current main, PR overview, precise scientific status and five known invalid inferences. It deliberately does not present a claim as universally proven simply because a CI check succeeded.
- `L1.md` — mathematically exact frontier: full claim statements, ordered quantifiers, proof dependencies and no-go scopes. Includes **all** directly tagged open HYP-105 PRs and integrity warnings, without a fixed arbitrary PR-count cap.
- `L2.md` — archival provenance: pinned source commit paths/blobs, stored Git byte objects, computed SHA-256 digests, evidence boundaries and precise criteria for revisiting invalid proof routes.
- `delta.json` / `delta.md` — optional semantic changes between sealed snapshots. Separates PR state, HEAD/base, CI, issue activity and ancestry changes from mathematical statement/quantifier/proof/model/evidence/no-go changes.

All artifacts are generated. They do not represent authoritative independent mathematical review.

## Temporal semantics and fail-closed rules

1. **A GitHub snapshot is non-atomic.** Requests span separate pages and objects; the collector checks main both before and after the scan and fails if main moved. Other PRs may move during the scan. There is no unqualified global transaction or strict serializability guarantee.
2. **Only the observed commit is the checked commit.** Explicit `--check-pr` selects open PRs and fails if a requested PR is no longer open; `--check-claim-prs` checks the open source PRs from the pinned registry and leaves closed source PRs in `NOT_IN_OPEN_INVENTORY` state. Every unqueried check is `NOT_INSPECTED`, never successful by default.
3. **Pin ≠ HEAD.** A research proof pinned to PR #471 at commit SHA X continues to have that provenance even when the PR HEAD moves to Y. A change in PR HEAD generates a CI re-check requirement, not an automatic mathematical-claim revision or retroactive test pass.
4. **Absence ≠ merge.** A PR no longer in the open listing is represented as `PR_NO_LONGER_IN_OPEN_INVENTORY` with its closure reason **unverified**. Closing issue #230 is also not an independent proof; root acceptance remains subject to actual verified mathematical obligations.
5. **Freshness is explicit.** The timestamp and the data collection mode are recorded. `--snapshot-in` is a replay, not a live refresh; observation timestamp changes alone do not produce fabricated scientific discoveries in a delta.
6. **Registry deltas are semantic.** A claim statement, quantifier order, source proof SHA, model or dependency change is reported separately from an updated PR or issue comment. The delta cannot infer that a novel theorem has appeared from an issue edit.
7. **Byte provenance is local and independently pinned.** Context generation validates RCP-C escrow Git SHA and SHA-256 pins before claiming the archive present. The optional remote original-source verification is supplied by RCP-C; this D command does not silently perform remote verification of all originals.
8. **No auto-merge, branch mutation, issue closure or theorem promotion** is performed by the collector or delta generator.

## Coverage and future extension

All open PRs are present in the full snapshot. The mathematical claim registry remains an **explicit pilot subset** (seven linked claims from five proof PRs), not a complete registry of every result across 160+ open HYP-105 PRs. The L0/L1/L2 views must label the count, avoid claims of universal coverage and cite the true scientific #230 target. Future additions to the claim/no-go registry automatically flow into D without changing the context generator.

Tests include: 200+ PR synthetic snapshots, explicit CI selectivity, closed-root without false theorem, false PR-merge inference, changed HEAD invalidation, altered quantifiers, evidence or no-go changes, forged snapshot contents, deterministic offline replay, main race and unknown root issue failure.

Next: RCP-001-E proof-impact analysis and cross-branch model compatibility from the D semantic deltas, followed by CI integration and scientific workflow improvements. Never impose limits on research PR count, chain depth or number of scientific claims.
