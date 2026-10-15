# HYP-105 — Formula Catalog

> Generated from pinned research registries; do not edit by hand.
> DOCUMENTED_IN_DRAFT is not independently reviewed/proven mathematics.
> HYP-105 issue [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains unresolved by these registered results.
> GitHub PR HEAD and CI are live data; none are hardcoded here.

Formula excerpts retain their original scoped quantifiers. Do not remove an expectation operator or silently generalize.

## HYP105-F-001 — Genuine source geometry and minimal physical alphabet

\[
s=2^h,\quad V_s=(s+1)(s^2+1),\quad a_s=\min\{a:\binom{a}{2}\ge V_s\},\quad N_s=\binom{a_s}{2}.
\]

**Applies under:** Common original W(3,s) typed global-injection model; h>=1. This defines the minimal alphabet, not an inequality about S_s.

**Cannot conclude:** A count of source vertices or physical labels alone is not a GF(5) obstruction.

**Linked claim:** HYP105-JPKC015-D6-ENSEMBLE

**Pinned source:** [PR #455 @ c02188a4d4f2](https://github.com/definitely-stable/Mathlab/blob/c02188a4d4f2e4e07440c4d7b25fc25c6dd31b3e/docs/research/HYP-105-ISSUE230-JPKC-015-ENSEMBLE-D6.md)

## HYP105-F-002 — D6 ensemble probability and expectation

\[
p_{D_6}(a)=60\left(\frac{(a)_6}{(N)_6}\right)^2,\qquad \mathbb E_{f,g}[D_6]=M_6(s)\,p_{D_6}(a)\sim\frac{16}{3}s^6.
\]

**Applies under:** h>=1, expectation over two independent UNIFORM COMPLETE globally injected original typed maps; M_6 is the original source six-edge matching count.

**Cannot conclude:** Positive average does NOT imply \inf_{f,g}D_6>0 or \inf_{f,g}S_s=\Omega(s^6).

**Linked claim:** HYP105-JPKC015-D6-ENSEMBLE

**Pinned source:** [PR #455 @ c02188a4d4f2](https://github.com/definitely-stable/Mathlab/blob/c02188a4d4f2e4e07440c4d7b25fc25c6dd31b3e/docs/research/HYP-105-ISSUE230-JPKC-015-ENSEMBLE-D6.md)

## HYP105-F-003 — Original GQ anchor dirty-pencil identities

\[
D_{\mathrm{left}}=s\sum_q t_f(q),\quad D_{\mathrm{right}}=s\sum_r t_g(r),\quad \Pr_{(q,r)\,\mathrm{unif}}[\mathrm{dirty}]\le\min\left\{1,\frac{4(a-2)}{s(s+1)}\right\}.
\]

**Applies under:** Every fixed legal globally injected f,g; probability ONLY over uniformly sampled ORIGINAL nonincident GQ point-line pairs.

**Cannot conclude:** Does not control four correlated original anchors conditional on a physical I1 template.

**Linked claim:** HYP105-EICE003K-DIRTY-ANCHOR

**Pinned source:** [PR #469 @ 73cfebed8042](https://github.com/definitely-stable/Mathlab/blob/73cfebed8042f0f9b6592bd318295fb0bdf69a5b/docs/research/HYP-105-ISSUE230-EICE003K-CLEAN-ANCHOR-CONCENTRATION.md)

## HYP105-F-004 — Quenched right-map exact B/A conditional identity

\[
\forall g:\quad \mathbb E_f\!\left[I_L^{BA,\mathrm{int}}(f,g)\mid g\right]=p_B(s)\,T_g,\quad p_B(s)=\frac{K\binom{a-2}{4}\,3\,4!}{(K)_5},\quad K=\binom{a}{2}.
\]

**Applies under:** h>=1; for each FIXED complete global right injection g, average over ONE independently drawn uniform complete global left injection f.

**Cannot conclude:** No individual-f or all-f,g guarantee follows from the identity.

**Linked claim:** HYP105-AA4N-QUENCHED-IDENTITY

**Pinned source:** [PR #470 @ 2af74df348a9](https://github.com/definitely-stable/Mathlab/blob/2af74df348a9c0921497757356199a609252f2c2/docs/research/HYP-105-ISSUE230-D6AA4N-QUENCHED-RIGHT-TRANSFER.md)

## HYP105-F-005 — All-right-map conditional expected B/A lower bound

\[
s=2^h\ge8:\quad \forall g,\quad \mathbb E_f[I_L^{BA,\mathrm{int}}(f,g)\mid g]\ge\frac{3s^6}{65536}.
\]

**Applies under:** h>=3; every fixed g, uniform random globally injected f. Implies min_g max_f lower; does NOT imply min_(f,g) lower.

**Cannot conclude:** Does not establish Root Branch A or bound the simultaneous adversarial minimax.

**Linked claim:** HYP105-AA4N-QUENCHED-LOWER

**Pinned source:** [PR #470 @ 2af74df348a9](https://github.com/definitely-stable/Mathlab/blob/2af74df348a9c0921497757356199a609252f2c2/docs/research/HYP-105-ISSUE230-D6AA4N-QUENCHED-RIGHT-TRANSFER.md)

## HYP105-F-006 — Deterministic all-h five-original-point quintic charge

\[
I_L^{BA,\mathrm{int}}(f,g)=\sum_{p,A:\,|A|=4}w_g(p,A)\,\chi_B\bigl(f(p);f(A)\bigr),\qquad w_g(p,A)\in\mathbb Z_{\ge0}.
\]

**Applies under:** h>=1; EVERY fixed coherent legal f,g, original six-incidence supports; quintic in constrained one-hot assignments.

**Cannot conclude:** Nonnegative coefficients do not imply the polynomial has a uniformly positive minimum.

**Linked claim:** HYP105-AA4O-QUINTIC-IDENTITY

**Pinned source:** [PR #471 @ b086566d8be1](https://github.com/definitely-stable/Mathlab/blob/b086566d8be17307b102e7bd89d28d4167af86a6/docs/research/HYP-105-ISSUE230-D6AA4O-QUINTIC-ADVERSARIAL-SWAP.md)

## HYP105-F-007 — Exact global-injection-preserving two-label swap

\[
\Delta_{u,v}I=\sum_{(p,A):\,\{u,v\}\cap(\{p\}\cup A)\ne\varnothing}w_g(p,A)\,\left[\chi_B\bigl(f^{u\leftrightarrow v}(p);f^{u\leftrightarrow v}(A)\bigr)-\chi_B\bigl(f(p);f(A)\bigr)\right].
\]

**Applies under:** h>=1; global swap of assigned physical pair labels on two distinct original points u,v with same fixed g.

**Cannot conclude:** One-transposition local optimality is not a global minimax or counterfamily certificate.

**Linked claim:** HYP105-AA4O-SWAP-IDENTITY

**Pinned source:** [PR #471 @ b086566d8be1](https://github.com/definitely-stable/Mathlab/blob/b086566d8be17307b102e7bd89d28d4167af86a6/docs/research/HYP-105-ISSUE230-D6AA4O-QUINTIC-ADVERSARIAL-SWAP.md)

## Formula review protocol

Verify original six-incidence constraints, alphabet, all-h range, global injection semantics, and quantifier order against the cited proof commit. CI does not mechanically check the algebra.

