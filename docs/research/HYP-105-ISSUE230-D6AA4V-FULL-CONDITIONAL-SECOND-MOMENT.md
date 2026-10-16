# HYP-105 / issue #230 — AA4-V: exact full-family quenched D6 second moment

**Research-only Draft.** Parent scientific [PR #487](https://github.com/definitely-stable/Mathlab/pull/487), exact starting HEAD 1502844a49cea1631206b2b68144c65f879fc4c0. Branch A/B/C of #230 is **OPEN_WITH_FORMAL_BLOCKER**. This is a *partial exact identity*, not a universal obstruction, not an ASET exponent, and not an independent peer review.

## 1. Frontline and nonduplication

Earlier [PR #480](https://github.com/definitely-stable/Mathlab/pull/480) and [PR #484](https://github.com/definitely-stable/Mathlab/pull/484) establish one-sided conditional D6 mean bounds. [PR #485](https://github.com/definitely-stable/Mathlab/pull/485) handles disjoint ORIGINAL line-factor overlap; [PR #487](https://github.com/definitely-stable/Mathlab/pull/487) derives the exact paired gluing kernel for **every** original line-overlap r=0,...,6 and evaluates ONE full 21,186-event genuine W32 anchored row. We claim no novelty for these results.

This slice closes a different *algebraic aggregation gate*: the exact conditional second moment over **all ordered pairs** of a given family of sixsets, with repeated identical right events and positive/negative cross-correlations handled, not artificially independent. Full numeric W32 evaluation is not claimed.

## 2. Theorem, quantifiers, proof

For EVERY h>=1 let s=2^h, V=(s+1)(s²+1), a=min{t:binom(t,2)>=V}, K=binom(a,2). For EVERY fixed complete globally injected point source-factor map f on the **genuine original W(3,s)**, let Q_f contain every set Q of **six distinct actual original incidence IDs** with six distinct original point factors, six distinct original line factors and a connected simple physical-left six-coordinate C6. For ANY explicitly specified finite subfamily A of Q_f, sample ONE uniformly random complete globally injected line map g shared across ALL Q in A.

The positional left C6 on the original incidence IDs induces a six-cycle on the six ORIGINAL line factor IDs. For Q in A define X_Q(g)=1 iff the SAME six source incidence IDs have the aligned right physical C6; this is the historically accepted positive GF(5) D6 class. Let D_A(g)=sum_Q X_Q(g), and p=(a)_6/(K)_6.

The parent #487 proves for ANY ordered Q,R with r shared genuine original LINE factor IDs and full cyclic overlap type tau:

P_tau=Pr(X_Q=X_R=1 | f)
      =(a)_6/(K)_(12-r) * sum_{k=0}^6 c_(tau,k)*(a-6)_k.

Here c_(tau,k) are canonical nonnegative integer gluing coefficients, respecting global equality on shared line factors and injectivity across distinct factors, and (n)_k is the falling factorial (zero when k>n). Tau depends on SHARED POSITIONS, not only r. Shared original point factors are permitted because f is fixed.

**Exact all-h full-family identities (AA4-V):**

E_g D_A = |A|*p;
E_g D_A² = sum_(Q,R in A ordered) P_tau(Q,R);
Var_g D_A = E_g D_A² - (|A|*p)².

For nonempty A, by Cauchy–Schwarz,
Pr_g(D_A>0) >= (|A|*p)² / E_g D_A².
For empty A, the moments and this lower bound are zero.

**Proof:** Expand the first and second powers of sum_Q X_Q. E X_Q=p by uniform injection of the six true source line IDs. For each (Q,R), the exact parent pair gluing kernel applies to the SAME full global g. By finite linearity, sum of all such kernels is the second moment, and subtracting the square of the mean gives exact variance. Cauchy–Schwarz on D_A*1_{D_A>0} yields the probability bound. If different original Q yield the SAME cyclic line source event, their indicators are identical, not independent. Grouping multiplicities m_gamma gives ordered pair weights m_gamma² for diagonal event types and 2*m_gamma*m_eta off diagonal; total ordered-pair weight must equal |A|². This quotient is exact without conflating distinct original incidence IDs.

Taking A=Q_f gives the complete conditional D6 second moment **as a mathematical formula** for every h, f. It is NOT a numerical claim that we have enumerated all 21,186² actual W32 pair terms.

## 3. Adversarial falsifiers

1. Two DISTINCT original Q may induce identical cyclic line events: D=2X, so E[D²]=4p, **not** 2p+2p². Repeated-event weights are essential.
2. Different physical C6 cyclic requirements on the SAME six original line factors are mutually incompatible: P_joint=0, and Var(X+Y)=2p-4p². The covariance can be negative.
3. Source r=2 permits both zero and positive joint kernels for different positional gluings (exact parent #487 fixtures); an r-only kernel is invalid.
4. Source r=0 uses the historical complement-C6 gluing result (prior #458/#485), not p². Dihedral rotations/reflections of a line cycle do not produce additional events.
5. All ordered pair weights sum to |A|², variance is an exact nonnegative rational, and the computed Cauchy lower is in [0,1]. Fail closed otherwise.

Tests include genuine ORIGINAL symplectic W(3,2) with **45 actual original incidences**, globally injected physical K6 source point/line labels, and schemes S68/S72. The historical predecessor enumerates 21,186 full left-D6 eligible sixsets for each. Here the CI evaluates **8 explicitly validated authentic Q per scheme**, or 64 ordered pairs each, plus exhaustive algebraic two/three-event identities. It does not claim complete W32 second-moment execution.

## 4. Files and checks

- research/hyp105_issue230_d6aa4v_full_conditional_second_moment.py — exact original event-cycle quotient and arbitrary-family second moment, with true W32 adapter.
- research/test_hyp105_issue230_d6aa4v_full_conditional_second_moment.py — independent direct ordered-pair contraction, impossible and possible gluing, diagonal and true original incidence regressions.
- .github/workflows/hyp105-issue230-aa4v-second-moment.yml — GitHub-hosted Python 3.12 dedicated checks.

From repo root: PYTHONPATH=research python -m unittest discover -s research -p "test_hyp105_issue230_d6aa4v_full_conditional_second_moment.py" -v

Diagnostic: PYTHONPATH=research python research/hyp105_issue230_d6aa4v_full_conditional_second_moment.py --scheme S68 --count 8

## 5. Literature and stop gate

Classical graph homomorphism correlation inequalities, e.g. [Sidorenko 1994](https://doi.org/10.1016/0012-365X(94)90388-3) and [Lüchtrath–Mönch 2025](https://doi.org/10.1017/S000497272500019X), do not automatically establish the globally coherent *injective* physical edge-label gluing and same-g original six-incidence positions here. AA4-V is a problem-specific **assembly of the prior #487 pair kernel**, not a claim of a new general second moment inequality or externally verified novelty.

The probability bound is for randomly chosen full g **conditional on one fixed f**. It does not imply a positive lower bound on D6(f,g) for EVERY correlated adversarial pair, nor on seven-class S(f,g). Next significant mathematical blocker: an all-h, every-f upper control for actual original cyclic tau-gluing multiplicity distributions strong enough for a useful relative variance bound or an *adversarial* seven-family alignment inequality. Root Branch A/B/C remains OPEN.


## 6. Exact hosted finite certificates (first validated proof HEAD)

The dedicated [GitHub-hosted run #38850770597](https://github.com/definitely-stable/Mathlab/actions/runs/38850770597) passed BOTH algebra and genuine W32 jobs at SHA bab0ccfb54ab474012d4f1b5d2e4b2fce3ab1219. The first job ran **10 tests, 10 OK**. The second independently executed S68 and S72 original W32 fixtures using **8 actual distinct six-incidence Q and 64 ordered Q pairs per fixed f**.

The two selected deterministic W32 subfamilies give the SAME exact diagnostics (not a universal inference): E[D_A]=8/5005, E[D_A²]=2/1001, Var(D_A)=49986/25050025, Cauchy lower Pr(D_A>0)>=32/25025. Of the **64 ordered pair terms**, **54 have zero joint gluing probability**. These numbers are exact Fraction evaluations, not Monte Carlo. The full original source candidate family remains 21,186 Q per f and its **448,846,596 ordered pairs have NOT been evaluated** by this run.

This section records evidence for the PINNED SHA above; any subsequent documentation or code changes require NEW exact-HEAD CI verification. Passing hosted CI is NOT independent mathematical peer review, root Branch A/B/C acceptance or a claim of full W32 covariance computation.
