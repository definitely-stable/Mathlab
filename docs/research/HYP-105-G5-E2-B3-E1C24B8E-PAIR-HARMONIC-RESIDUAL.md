# HYP-105 C24-B8-E — exact pair-feature Johnson spectrum and genuine nonlinear residual

Research root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Parent stacked [C24-B8-D PR #360](https://github.com/definitely-stable/Mathlab/pull/360), exact parent HEAD `5e13aa08f4a1322e6255139aa14c68457a895823`. **RESTRICTED_THEOREM_C**, not a universal seven-score lower, infinite coherent counterfamily or full GF(5) R3/ASET result. All tests use GitHub-hosted runners only. No main modification or merge.

## 1. The next real mathematical obstruction

B8-D computes every `I_f(i,j)=E[S(f,g)|g(i),g(j) adjacent]-E[S(f,g)|g(i),g(j) disjoint]` for ONE uniform complete RIGHT injection g and ANY fixed complete original LEFT injection f. This is a covariance with `Z_ij=1_{g(i) meets g(j)}`, not a statement of independence between original sixsets. The 105 W32 pair influences are nonzero and have zero rows, but their magnitudes alone cannot separate linear correlated pair effects from remaining nonlinear effects.

**Do not confuse full realized pair data with first-order pair CONDITIONAL MEANS.** For full K6-edge bijections the collection of ALL observed `Z_ij(g)` describes the relabeled host line graph and determines g up to a physical coordinate permutation; the nonlinear residual below therefore need not involve new data beyond pairs. It is nonlinear dependence on these pair indicators, not an unexplained probability variable or a proven necessity for new 3-incidence structures.

## 2. All-h theorem: complete-right-injection pair covariance Gram

For each original W(3,s), s=2^h >=2, let n=(s+1)(s^2+1), a=min{a:C(a,2)>=n}, m=C(a,2), and f ANY admissible complete original left physical-edge injection. Draw g as ONE uniformly random complete original right-to-K_a-edge injection. Put `Z_ij=1{g(i) intersects g(j)}`, `p=4/(a+1)`, `X_ij=Z_ij-p`, `v=p(1-p)`.

**The exact ALL-h covariance between two ORIGINAL unordered right-line index pairs e,t is:**

    G[e,t] = v                                       if e=t
           = -v/(m-2)                                if |e∩t|=1
           = 2v/((m-2)(m-3))                        if e∩t=empty.

*Proof:* the line graph H=L(K_a) has m vertices and regular degree d=2(a-2). The images under one uniform complete global injection of two, three, or four DISTINCT original right lines have the exact uniform ordered sampling-without-replacement marginals from these m vertices. Hence `E Z=p=d/(m-1)` and `Var Z=v`. Given one fixed original line image, the adjacent images assigned to the other two original lines are two distinct draws from its remaining m-1 host edges, of which exactly d are neighbors. Their covariance is therefore `-v/(m-2)`. For two disjoint original index pairs use the SAME universal four-line marginal: imagine a uniform labeling of all m host edges (the marginal agrees). In a complete labeling the number of adjacent host-edge pairs `sum_{e}Z_e=md/2` is exactly constant. Covariance with one fixed Z_e gives `0=v+2(m-2)cov_share+C(m-2,2)cov_disjoint`, hence `cov_disjoint=2v/((m-2)(m-3))`. This does NOT condition one original sixset separately from another. QED.

## 3. Three exact Johnson eigenspaces and singular gates

Let `E_n=C(n,2)` and regard G as an `E_n×E_n` matrix indexed by unordered original RIGHT line pairs. Let B be the n×E_n unsigned vertex-edge incidence matrix of K_n and J the all-ones matrix. With `t=-v/(m-2)` and `u=2v/((m-2)(m-3))`,

    G=(v-2t+u) Identity + (t-u) B^T B + u J.

The orthogonal decomposition of edge-vectors into (0) constant, (1) centered vertex-additive `z_ij=w_i+w_j`, sum w_i=0, and (2) row-zero `sum_{j!=i} z_ij=0` gives the EXACT eigenvalues

    lambda_0 = v (m-n)(m-n-1) / ((m-2)(m-3)), multiplicity 1
    lambda_1 = v (m-1)(m-n) / ((m-2)(m-3)),     multiplicity n-1
    lambda_2 = v (m-1)/(m-3),                   multiplicity n(n-3)/2.

For any n>=4, 4<=n<=m, these are nonnegative. At n=m, lambda0=lambda1=0 and lambda2>0. At n=m-1, lambda0=0 only. At n<=m-2, all are positive.

**True W(3,2):** a=6, m=n=15, p=4/7, v=12/49, lambda2=2/7 with rank 90 out of 105; the exact zero-row identities of B8-D are precisely the nullspace constraints. These are algebraic physical-host consequences, not empirical spectra inferred from a 15×15 floating-point matrix.

## 4. Exact all-h L2-orthogonal linear pair projection

For the genuine fixed-f seven-score define `mu=E S`, and `b_ij=Cov(S,X_ij)=v I_f(i,j)` via B8-D's ORIGINAL source-multiplicity-preserving D6-aware global-injection computation. Let `b=b0+b1+b2` be its orthogonal decomposition under the eigenspaces above. Define the unique minimum-Euclidean-norm pair coefficient vector

    gamma = sum_(k:lambda_k>0) b_k / lambda_k.

For zero lambda_k the input b_k MUST be exactly zero (else it is incompatible with any score sampled under the asserted global-injection law). Then

    P_2(f,g) = sum_(i<j) gamma_ij (Z_ij(g)-p),
    R_nonlinear(f,g) = S(f,g)-mu-P_2(f,g).

**ALL-h structural theorem:** `E P_2=E R=0` and `Cov(R,X_ij)=0` for every original right line pair. Moreover,

    E[P_2^2] = sum_(k:lambda_k>0) ||b_k||_2^2 / lambda_k

exactly, and `E[(S-mu)^2]=E[P_2^2]+E[R^2]` when the variance of S is finite (it is, in the finite host). No source-sixset independence, concentration, entropy assumption or approximation appears. **No bound on the pointwise magnitude, variance, or maximum of R is obtained solely from this orthogonality.**

When n=m, b is row-zero and `gamma = (v/lambda2) I`. In genuine W32,

    gamma_ij = (6/7) I_f(i,j)
    P_2(f,g) = (6/7) sum_(i<j) I_f(i,j) (Z_ij(g)-4/7).

The code independently verifies `G gamma=b` by the incidence-matrix expression without dense rational matrix inversion or generic eigenvalue solvers. No physically arbitrary per-source reassignments are allowed.

## 5. Genuine original W32 nonlinear-residual finite witness

Fix exactly the original complete f0 and legal global g68 from B6/B8. Run the independent ORIGINAL right-first census and compressed original-source score; both must equal 68. Obtain the full exact 105-pair B8-D matrix, exact Gram projection, and rational

    r68 = 68 - (870476/5005) - P_2(f0,g68).

If r68 is nonzero, it certifies **for the ACTUAL seven-family W32 score** that no affine linear function of the 105 physical adjacency indicators equals the score on every complete right injection. Moreover

    ||R_nonlinear(f0,.)||_infinity >= |r68|.

If r68 happens to vanish, a separately budgeted check of up to 105 globally valid one-swap right maps may find a nonzero actual score residual. A finite actual nonzero witness is proof only at s=2 and only for this f0, not a lower on the full residual variance (unless independently derived), all-f worst-case, or asymptotic all-h obstruction.

**Independent falsifiers:** for n=4 original right labels, enumerate ALL 15P4=32,760 complete K6-edge partial injections and independently compute 6×6 covariance entries, synthetic invariant nonlinear score means/covariances, projection orthogonality and positive nonlinear residual variance. Also test exact Gram singularities at n=14,15 and fail-closed incompatible covariance vectors. This n=4 synthetic score does NOT pose as a genuine W32 source. Genuine W32 requires the separate dedicated original GQ scorer, not generic `unittest discover`.

## 6. Decision and explicit formal blocker

No linear projection variance or zero-row spectral theorem by itself establishes a bound on

    D_s(f) = mu_s(f) - min_g S_s(f,g).

For a Branch-A sufficient bound one needs for ALL complete f at large h both `mu_s(f)>=c0*s^6` and a **uniform pointwise** bound on the negative combined deviation `-P_2(f,g)-R_nonlinear(f,g)`, with constant strictly less than c0*s^6. In particular, even `E R²=o(s^12)` by itself is insufficient for the worst-case minimum over an injection space with extremely small point masses. Uniform all-f original-source geometry and the nonlinear residual's signed extremal structure remain formal blockers.

**Verdict:** `RESTRICTED_THEOREM_C_EXACT_PAIR_GRAM_L2_PROJECTION` and, only if an independently verified original W32 nonzero residual is produced, `FINITE_ORIGINAL_W32_PAIR_AFFINE_NO_GO`. Root #230 remains `OPEN_WITH_FORMAL_BLOCKER` with neither Branch A nor Branch B proved. No complete GF(5) R3 bound or ASET improvement follows.
