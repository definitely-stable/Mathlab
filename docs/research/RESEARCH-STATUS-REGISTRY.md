# Active research status registry: authority and update protocol

This is a **metadata and navigation** layer, not a second theorem tree and
not a live GitHub issue/PR service. See the [generated status dashboard](RESEARCH-STATUS.md)
and [JSON Schema](RESEARCH-STATUS-REGISTRY.schema.json).

## Source-of-truth hierarchy

1. Scientific claim and theorem ancestry: [UCT-005 theorem tree](UCT-005-THEOREM-TREE.json)
   and the cited source-specific proof documents. The UCT-005 root remains
   `OPEN_UNPROVED`.
2. Cost, adversary, online semantics, historical PIN and error quantifiers:
   [F1 frozen model](UCT-005-G3-B2-D1B0-F1-MODEL.json).
3. Cross-domain nonimplications and proof transfer:
   [G4 typed bridges](UCT-005-G4-TYPED-BRIDGES.json); a bridge labelled
   `REDUCTION_REQUIRED` is **not** an established theorem implication.
4. Known, stopped and prior-art claims:
   [known/stopped registry](KNOWN-AND-STOPPED-RESEARCH.json).
5. Bibliographic identities: [literature catalog](catalog/literature.json).
   This active-status registry never duplicates the canonical LIT entries.

The active-status registry lists **ten selected research programs**, including
completed engineering issue slices, as a
reviewed snapshot. It does not claim to inventory every GitHub issue or proof.

**2026-10-11 scoped correction:** GitHub issues [#244](https://github.com/definitely-stable/Mathlab/issues/244) and [#254](https://github.com/definitely-stable/Mathlab/issues/254) are both **CLOSED** after the accepted upper-construction PRs [#248](https://github.com/definitely-stable/Mathlab/pull/248) and [#258](https://github.com/definitely-stable/Mathlab/pull/258). Both registry records are now `CLOSED_ISSUE / MODEL_ONLY`; this is not a proof of any fully priced F1 Pareto bound, and [#105](https://github.com/definitely-stable/Mathlab/issues/105) stays `OPEN_UNPROVED`. The baseline SHA is a **review checkpoint**, not proof of live GitHub state or CI. The dated issue inventory and successor evidence are separately tracked by [PR #257](https://github.com/definitely-stable/Mathlab/pull/257); no copied live-state database is introduced.


## Separate status dimensions

- `scientific_status`: whether the selected research objective is unproved,
  a restricted classical result, or a model-only implementation.
- `workflow_status`: the issue/PR position **at review time**, not a live API
  result. `OPEN_PR_UNVERIFIED` explicitly does not mean merged;
  `CLOSED_ISSUE` records issue lifecycle only and does not mean scientific proof.
- `proof_grade`: none, finite oracle, restricted classical proof, or checked
  formal proof. A finite oracle cannot promote a universal asymptotic theorem.
- `novelty_status`: prior-art classification separate from mathematical truth.
- `source_audit_grade`: metadata, partial original text, or full proof-level
  verification. A citation count is not a full-proof audit.
- `last_verified_sha`: SHA of the **metadata snapshot inspected**, not a
  cryptographic theorem proof and not an exact-head CI success.
- `ci.status`: `NOT_CHECKED` until an exact SHA and hosted workflow run URL
  are recorded and independently reviewed.

`parent` denotes organizational ownership, not logical implication.
`dependencies` denotes prerequisites and must be acyclic.
`typed_edges` may describe `APPLICATION_ONLY`, `REDUCTION_REQUIRED`,
or pending upper constructions; they are deliberately **not** treated as
theorem corollaries. The existing G4 register remains the detailed bridge atlas.

## Updating the registry

```sh
python research/research_status_registry.py --write
python research/research_status_registry.py --check
python -m unittest discover -s research -p 'test_research_status_registry.py' -v
```

Run the full `research.yml` workflow on the exact PR HEAD, and separately
verify post-merge main CI. The focused
[research-status-integrity workflow](../../.github/workflows/research-status-integrity.yml)
runs on GitHub-hosted `ubuntu-latest`; no local runner, Rust build, or Lean
formalization is implied.

**Scope of automated validation:** local schema/enum consistency, exact
document paths, unique IDs, acyclic dependencies, typed edge statuses, F1/G4
and UCT-005 root guardrails, and generated-dashboard freshness. It **cannot**
prove that GitHub issues remain open, that a workflow URL actually succeeded,
that primary-source proofs were read, or that any mathematical theorem is true.
Those claims require separate GitHub/API and source review.

**Rollback:** revert this additive metadata layer and its navigation changes;
the existing theorem, source, and known-work registers are not rewritten.
