# UCT-001 G1 — October 2026 dynamic Boolean cell-probe theorem: exact statement and transfer barriers

Date 2026-10-08. Parent [#74](https://github.com/definitely-stable/Mathlab/issues/74). Catalog identity **LIT-119**. Primary source: [Young Kun Ko, ECCC TR26-047, revision 1, 2026-10-07](https://eccc.weizmann.ac.il/report/2026/047/revision/1/download), **36-page author manuscript**, especially page 3, Theorem 1.1; Appendix B, Definition B.1 and Theorem B.3. Source statement read from paper; **full derivation NOT independently rechecked and no proof formalization**.

## Precise prior art that directly narrows UCT-A and UCT-B
The source's "Multiphase Problem" fixes a preprocessed family S_1,...,S_m ∈ {0,1}^n with m=n^{1+Omega(1)} and a dynamic vector X ∈ {0,1}^n. One-bit updates set the bits of X, costing t_u cell probes *per update*; there are n such updates. Query q∈[m] outputs the Boolean function f(S_q,X) with t_tot total cell probes. Word size w=Theta(log n) bits is charged in the cell-probe model. `m` here is the number of preprocessed vectors, **NOT Mathlab LENT's code dimension**; `w` here is the word size, **NOT LENT's maximum changed coordinates**. These variable name collisions alone make naive theorem substitution unsafe.

**Source Theorem 1.1 (paper claim, not a new Mathlab theorem):** for f the inner product over F_2 and t_u=n^{o(1)}, its parameters satisfy

    t_tot >= Omega((log(n) / log(t_u * w))^2).

In particular, under the source's hypotheses,

    max(t_u, t_tot) >= Omega((log(n) / loglog(n))^2).

The author gives a communication-to-cell-probe lifting route for an explicitly specified class of hard functions (Theorem B.3); inner product satisfies the required hardness but **set disjointness does not** under the stated large-min-entropy product-distribution criterion.

**Important negative restriction:** the article says this bound is proved for the Multiphase/inner-product problem, NOT for every dynamic Boolean query problem. The original dynamic range-parity challenge is noted as still open in this paper. Nor does the polylogarithmic bound resolve the much stronger n^{Omega(1)} Multiphase conjecture.

## Why this matters for the proposed "unified" theory
1. The idea "verification in a communication protocol yields a stronger dynamic lower bound" is **not novel** as a blanket mathematical statement in 2026: Ko uses a **2.5-round communication game with a verification round**. Claiming this general technique as UCT-002 originality without further modelling would be inaccurate.
2. The verification round in Ko is an **auxiliary lower-bound proof device**, **not a cryptographic authenticated old-root witness**. It does not automatically prove an improvement for HYP-103 dynamic certificate generation.
3. The theorem explicitly couples update and query cost in a cell-probe setting, strongly restricting UCT-A's broad claim to originate a novel joint update/query tradeoff.
4. A genuinely separate UCT theorem must quantify a resource absent from this paper (e.g. physical write locality, communication bytes, verifier/prover costs, or precise current-observation quotient) **and prove an additional nontrivial bound** on an operation family not already covered by a reduction.

## Frozen source-level STOP and reopening gate
- `STOP_BROAD_UCT_A`: no claim that coupling update and query complexity is new.
- `STOP_BROAD_UCT_B`: no claim that an added verification round alone is new.
- `STOP_NAME_TRANSFER`: same symbols `m,w` are different resources; no automatic transfer between cell-probes and q-ary Hamming writes.
- `REOPEN_ONLY_IF`: statement has explicit quantified semantics, includes a new charged resource/observation model, is not implied by source Theorem 1.1/B.3 or Fredman–Saks/Pătraşcu–Demaine, and survives adversarial finite-oracle tests.

## Next feasible research operation (not a theorem claim)
Select exactly one dynamic task and freeze two competing representations with explicit time/space/write/query tradeoff. Produce a source-to-source theorem hypothesis matrix for Ko 2026, Fredman–Saks 1989, Pătraşcu–Demaine 2006 and cubical embedding. If every desired statement follows from existing theorems or cannot be formally compared, mark **STOP_G1**; do not manufacture a new "unified theory" claim.

Proof-tier: **PRIMARY_FULLTEXT_THEOREM_STATEMENT_SPOTCHECKED** / **AUTHOR_THEOREM_NOT_REPROVED** / **MODEL_TRANSFER_AUDIT**.
