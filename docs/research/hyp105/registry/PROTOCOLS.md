# HYP-105 — Research Protocols & Acceptance Gates

> Generated from pinned research registries; do not edit by hand.
> DOCUMENTED_IN_DRAFT is not independently reviewed/proven mathematics.
> HYP-105 issue [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains unresolved by these registered results.
> GitHub PR HEAD and CI are live data; none are hardcoded here.

## Mathematical and operational sources

| Layer | Source of truth | Acceptance boundary |
|---|---|---|
| Original mathematics | Root #230 and commit-pinned proof documents | Separate mathematical review |
| Claims | research/rcp/hyp105/claims/*.json | Metadata-valid only |
| Formulas | research/rcp/hyp105/formulas.json and cited proof | Not mechanically algebra-verified |
| Evidence | research/rcp/hyp105/evidence and archive/ | Git blob SHA and SHA-256 |
| No-go | research/rcp/hyp105/no_go | Scoped inference blockers only |
| Live state | GitHub PRs, issues and SHA checks | Non-atomic observation |
| Impact | research/rcp/proof_impact.py | Review candidates, not contradictions |

## Reproduce and validate

```bash
python -m unittest research.test_rcp_proof_impact -v
python -m research.rcp.structured_docs --check
python -m research.rcp.evidence_ledger --output /tmp/hyp105-evidence
GITHUB_TOKEN=... python -m research.rcp.context_builder --output /tmp/hyp105-live --check-claim-prs
python -m research.rcp.proof_impact --snapshot /tmp/hyp105-live/snapshot.json --output /tmp/hyp105-impact
```

## Update process

1. Update the pinned mathematical claim and evidence only after auditing exact source provenance; green CI does not promote the claim.
2. Record formulas with full scope, model, quantifiers and non-implications.
3. Maintain precise no-go scope and reopening conditions.
4. Regenerate these Markdown files using `python -m research.rcp.structured_docs --write`; CI checks `--check` to prevent drift.
5. Compare snapshots and review changed proofs and all downstream claims.
6. Integrate infrastructure PRs from ancestor to descendant only after review; no automated merge.

## Hard boundaries

No averaging-to-adversarial-minimum inference, local-to-global transfer, W32-to-all-h promotion, or conflation of CI and proofs.
No cap on claim count, PR count or stack depth.

