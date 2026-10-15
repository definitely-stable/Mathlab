# HYP-105 / RCP-001-E — Proof Impact and Mathematical Compatibility

Research tracking: [#474](https://github.com/definitely-stable/Mathlab/issues/474). Scientific root: [#230](https://github.com/definitely-stable/Mathlab/issues/230). This slice extends [RCP-001-D](LIVING-CONTEXT.md).

## What the impact graph means

Nodes represent **registered and SHA-pinned mathematical claims**; an edge P -> Q means claim Q explicitly identifies claim P as a dependency. Under a change in the mathematical statement, quantifier list, definition of a model, original proof reference, evidence receipt, no-go entry or the byte identity of an escrow object, the program selects directly affected nodes and their **transitive descendants**, preserving both old and new edges to catch removed dependencies.

Outputs:

- `impact.json`: typed changed-proof triggers, dependency edges, direct and transitive impacted claims, changed proof source, review flags, coverage and uncertainty.
- `impact.md`: readable proof-impact report, candidate model compatibility review and exact source PR HEAD versus pinned proof commit.
- [Registered Results](registry/RESULTS.md), [Formula Catalog](registry/FORMULAS.md), [Proof Graph](registry/PROOF-GRAPH.md), [Research Matrix](registry/RESEARCH-MATRIX.md), [Protocols](registry/PROTOCOLS.md): deterministic, **committed** Markdown research documentation, generated from canonical claim/formula/evidence/no-go JSON.

## Commands

```bash
python -m research.rcp.structured_docs --check
python -m research.rcp.structured_docs --write
python -m unittest research.test_rcp_proof_impact -v

GITHUB_TOKEN=... python -m research.rcp.context_builder \
  --output /tmp/hyp105-current --check-claim-prs

python -m research.rcp.proof_impact \
  --snapshot /tmp/hyp105-current/snapshot.json \
  --output /tmp/hyp105-impact

python -m research.rcp.proof_impact \
  --snapshot /tmp/hyp105-current/snapshot.json \
  --previous /tmp/hyp105-earlier/snapshot.json \
  --output /tmp/hyp105-impact-delta
```

The Markdown registry is derived, but **versioned in Git** so it remains readable without live external services. CI runs `--check` to refuse stale documentation. The dynamic snapshot L0/L1/L2 is produced on demand and should not be committed with outdated PR/CI state.

## Meaning of compatibility diagnostics

- `MODEL_SCOPE_BRIDGE_REVIEW`: a prerequisite references a model definition omitted from the dependent claim. The dependent proof may be an independent deterministic proof or a valid reduction; the mismatch is **not a contradiction**.
- `EXPECTATION_TO_DETERMINISTIC_BRIDGE_REVIEW`: an expected-value parent is linked to a deterministic child. The connection must be checked for proper quantifier preservation, but a child may be proved independently.
- `DOMAIN_TRANSFER_REVIEW`: changed or different h domains. Text differences are not mechanically established inclusions or mathematical counterexamples.
- Original pinned proof SHA and observed PR HEAD may differ. This is **not proof invalidation** or an assertion of a new scientific result.
- Changes to open PRs and check-runs are **operational**; they do not automatically mark mathematical results as impacted unless their actual registered mathematical content/evidence changes.

The current scientific registry is a **pilot** (seven claims, not every open HYP-105 PR), and the cross-branch model audit therefore has **partial coverage**. No program can honestly diagnose every scientific conflict before the relevant statements are registered. Extend the claim graph incrementally without imposing limits on PRs or proof depth.

## What is not certified

None of the flags asserts a mathematical contradiction, external prior-art novelty, all-h universal GF(5) proof, global minimax, or formal scientific acceptance. Source documents remain authoritative; CI and SHA checks establish reproducible metadata only.
