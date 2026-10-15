# HYP-105 / RCP-001-B — Mathematical Claim Registry

**Tracking:** [HYP105-OPS-001 #474](https://github.com/definitely-stable/Mathlab/issues/474), following [RCP-001-A PR #475](https://github.com/definitely-stable/Mathlab/pull/475).
**Scientific root:** [HYP-105 issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Nothing in this infrastructure slice proves Branch A/B/C.

## Design contract

A mathematical claim records one explicit statement, an ordered quantifier sequence, original model IDs, commit-pinned proof blob, logical dependencies, limitations, and separated mathematical/review/novelty status.

**One claim is not one PR.** AA4-N's conditional mean identity is distinct from its positive lower; AA4-O's polynomial is distinct from the transposition formula.

Records are marked `DOCUMENTED_IN_DRAFT` and `NOT_REVIEWED`, not independently accepted. A passing CI or pinned source blob does not establish mathematical truth.

## Source-to-model guardrails

- Genuine original W(3,2^h), shared complete typed global injections and minimal physical K_a are part of each claim's referenced models.
- Sixsets count SIX distinct true original incidence IDs, not signed events or physical label orbits.
- Ordered `forall g; expectation f` and `expectation (f,g)` do not imply `forall f,g`. Declared logical mode is mechanically checked.
- The PR #466 selected sparse local counterexample does not refute dense EICE-002 or universal root Branch A.
- Uniform-original-anchor marginal concentration cannot be transferred to a four-correlated conditional physical template law.
- Mathematical, independent-review and novelty statuses remain separate.

## Files and commands

- `research/rcp/hyp105/models.json` — versioned shared model references.
- `research/rcp/hyp105/claims/*.json` — stable mathematical claims and proof versions.
- `research/rcp/schema/claim.schema.json` and `models.schema.json` — JSON Schema metadata.
- `research/rcp/claim_registry.py` — structural, DAG and pinned proof source validation.
- `research/rcp/claim_index.py` — deterministic `claims.json`, `claims.md` and dependency edges.
- `research/test_rcp_claim_registry.py` — adversarial metadata tests.

From repository root on Python 3.12:

```bash
python -m unittest research.test_rcp_claim_registry -v
python -m research.rcp.claim_registry
GITHUB_TOKEN=... python -m research.rcp.claim_registry --verify-sources
GITHUB_TOKEN=... python -m research.rcp.claim_index --output /tmp/rcp001b-claims --verify-sources
```

The optional live check fetches proof files at **pinned commits** and confirms Git blob SHA. It checks byte identity, not mathematical correctness. Generated indexes are disposable outputs, never independent competing sources of truth.

## First mathematical claims

| Stable ID | Source | Mathematical scope |
|---|---|---|
| HYP105-JPKC015-D6-ENSEMBLE | PR #455 | Uniform full injection ENSEMBLE E[D6] ~ (16/3)s^6 |
| HYP105-LT-LOCAL-COUNTEREXAMPLE | PR #466 | For all s>=8 exists a selected local 18-incidence nontransfer witness |
| HYP105-EICE003K-DIRTY-ANCHOR | PR #469 | All f,g original source-anchor dirty marginal O(s^-1/2) |
| HYP105-AA4N-QUENCHED-IDENTITY | PR #470 | For every g, E_f B/A internal charge = p_B T_g |
| HYP105-AA4N-QUENCHED-LOWER | PR #470 | For every g, E_f B/A internal charge >= 3s^6/65536 for s>=8 |
| HYP105-AA4O-QUINTIC-IDENTITY | PR #471 | Deterministic B/A original five-factor charge identity |
| HYP105-AA4O-SWAP-IDENTITY | PR #471 | Deterministic full-map two-label transposition identity |

All seven are documented research-draft results without independent proof acceptance. Their existence does not close #230.

## Validation and extension

The validator catches missing or unpinned proof identity, unknown models, misordered or missing quantifiers, accidental expectation-to-worst-case upgrades, dependency DAG cycles, no-go scope omissions and unsupported root-proof promotion. Source checks and metadata correctness never certify novelty or a mathematical theorem.

No arbitrary limit on the number of claims, PRs, or stack depth is imposed. Preserve stable IDs; a substantive corrected theorem should use an explicitly linked successor rather than rewriting history. Existing `DECISIONS.md` and `KNOWN-AND-STOPPED-RESEARCH.json` are not replaced.

Remaining slices: C evidence receipts/no-go ledger; D living context/delta; E proof impact; F CI consolidation after parity assessment; G integration provenance.
