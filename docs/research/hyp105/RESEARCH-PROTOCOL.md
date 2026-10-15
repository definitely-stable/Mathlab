# RCP-001 — repository-native research continuity

Scope: Mathlab research provenance, initially HYP-105 / #230. Tracking issue: #474.

## Non-negotiable invariants

- Mathematical root objectives are owned by issues #169/#176/#230, not inferred from report text.
- Treat the mathematical status, CI status, and novelty status as separate dimensions.
- An exact SHA in the inventory is an *observed* PR head, not an acceptance certificate.
- No conversion of E_f, min_g E_f, finite W(3,2), local witnesses, or conditional density bounds into min_(f,g) or all-h universal results.
- Existing scientific code, model, GF(5) signed-flow oracle and seven positive classes are unchanged by the RCP inventory.
- GitHub-hosted runners only. No forced PR/stack limits.
- Merged and closed parent branches may not appear in open-PR inventory. Such links are explicitly unresolved until separately audited.

## RCP-001-A implementation contract

Input: live GitHub REST API main branch and *all* open pulls, paginated; optional requested PR check-runs by SHA.

Output: inventory.json and inventory.md. Untrusted link hosts or paths, duplicate identities, parent cycles, invalid HEAD SHA or malformed responses cause fail-closed errors. Ancestor edges require exact base repository/ref matches to an open parent head repository/ref. Distinct PRs with ambiguous branch identities remain marked ambiguous. For linked parents, base SHA mismatch is a diagnostic, not an assertion that either repository state is correct. The API does not expose one atomic multi-PR snapshot; all outputs carry this limitation.

Classification: direct HYP-105 titles/bodies with HYP-105 or #230; the human-readable index also shows any open ancestors needed to reconstruct that chain. All open repository PRs are retained in JSON, including other research families.

CI: check runs requested against exact observed head SHA. The script does not assume a check completed for other SHA values. A SUCCESS indicates the returned check-runs on that SHA all completed successfully, **not** that all project-required jobs were run, and never that a mathematical proof was reviewed. Subsequent changes invalidate any claim that old results cover a new HEAD.

## Subsequent protocol milestones (not implemented in slice A)

- B: immutable mathematical claim IDs, quantifier/order model, links to proofs and dependencies.
- C: durable evidence receipts and separate falsifier/no-go index connected to existing decisions.
- D: L0 current state, L1 proof-frontier, L2 evidence packages and semantic research deltas.
- E: proof-impact dependency DAG and cross-branch conflicts.
- F: shared CI workflows only after demonstrating current research coverage parity.
- G: integration provenance and systematic scientific review without automatic merges.

Do not duplicate main HEAD values in versioned documents. Derive current status from GitHub and represent unavailable information as unverified.
