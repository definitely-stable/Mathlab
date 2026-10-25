# HYP-105 #230 — D6-AA4-F: exact three-ORIGINAL-factor separator and pair-marginal NO-GO

**Classification:** ALL-h exact **conditional frozen-outside** 3-source-factor minimization hierarchy, independent synthetic analytic pair-consistency gap, and true ORIGINAL W(3,2) seven-class GF5 fiber checks. Neither all-h global `S_s >= c s^6` (Branch A) nor infinite correlated Branch B is established. No full R3 or ASET exponent. Issue #230/#176/#169 remain OPEN.

**Stack:** strictly above green [D6-AA4-E #441](https://github.com/definitely-stable/Mathlab/pull/441) pinned parent `b923eb4a186809908009a82d413c45c36fbe2ad4`. Work only on research branch; do NOT update main or merge automatically.

## 1. Why this gate, rather than more 5-/6-factor W32 permutations?

AA4-D rigorously excludes zero accepted-seven-count within 4 ORIGINAL typed-factor edits of two pinned W32 maps; AA4-E introduced a genuine global typed-injective unary Lagrangian certificate, but exhibited an analytic gap: all unary prices can certify at most zero even when coherent complete global cost is one. The next obligation is to identify the precise higher-order consistency needed, without assuming local motif Q assignments can be chosen independently.

The parallel [JPKC-011 #442](https://github.com/definitely-stable/Mathlab/pull/442) reports that 63/68 positive original Q on pinned S68 and 66/72 on S72 have NO coordinate-proper P3. Therefore **do not use** a physical-P3 observable as a stand-in for all seven GF5 classes. Here every actual source Q is classified by the historical accepted original-six-incidence positional seven-census; this branch does NOT import code from unmerged JPKC-011.

## 2. All-h conditional exact separator theorem

Fix arbitrary s=2^h, h>=1, genuine symplectic W(3,s), and arbitrary complete **separately injective** physical pair maps f,g. Fix an arbitrary block B of exactly three DISTINCT ORIGINAL typed factors; freeze all assignments outside B. The available physical pair-label pools of the two types are the truly unoccupied labels plus labels freed by B of that type. On any finite admissible B completion fiber `J(B)`, let `c_Q(t)` be the original seven-GF5 class indicator (or its accepted nonnegative certified 51-column numerator) of ORIGINAL six DISTINCT source incidences Q, with ONE common physical assignment to every occurrence of each factor.

For each Q let `D_Q = T(Q) intersection B`, the *true ORIGINAL* factor dependency in B, and retain the exact local `c_Q` table. For any partition of original Q into disjoint groups `G_12, G_13, G_23, G_3` such that every Q in a pair group depends only on factors of its named pair, define:

\[
L_{\mathrm{ind}}=\sum_Q \min_{t\in J(B)} c_Q(t),
\]
\[
L_{\mathrm{pair}}=\sum_{\{i,j\}}\min_{t\in J(B)}\sum_{Q\in G_{ij}}c_Q(t)
  +\sum_{Q\in G_3}\min_{t\in J(B)}c_Q(t),
\]
\[
L_{\mathrm{triple}}=\min_{t\in J(B)}\sum_Q c_Q(t).
\]

**THEOREM:** for ALL h>=1, arbitrary starting genuine global typed pair injections f,g, any genuine ORIGINAL three-factor B, any nonnegative accepted seven-GF5 six-incidence costs, and any partition satisfying the TRUE source dependency restriction,

\[
\boxed{0\le L_{\mathrm{ind}}\le L_{\mathrm{pair}}\le L_{\mathrm{triple}}\le S_s(f',g')}
\quad\forall (f',g')\in J(B).
\]

Proof: for each pair group, its common ORIGINAL factors must share one pair-label tuple in any coherent completion. The minimum of the sum is at least the sum of minima, and is no greater than that sum evaluated on any given global completion. The separate true-3-factor Q terms can be minimized independently only for the lower relaxation, whereas the 3-factor minimum uses one common globally coherent B-labeling for every ORIGINAL Q. Sum the disjoint original-Q groups, with no duplicate Q or coordinate/orbit overcount. The inequality holds equally for nonnegative accepted GF5 class weights. Equality at the right is attained by some actual B-completion, so `L_triple` is an exact conditional minimum, not a universal starting-label-independent lower certificate.

If B contains bP points and bL lines and each typed image has m unused physical pairs, the genuine full completion fiber size is `(m+bP)_{bP} (m+bL)_{bL}`; only for W32 (m=0) does the fixed-image completion fiber simplify to `bP!bL!`. The tiny executable oracle here intentionally covers W32 fixed-image three-factor blocks, NOT large-s free-label exhaustions.

**NO UNIVERSAL A from this theorem:** taking a minimum over all possible outside assignments may result in zero. Neither the conditional hierarchy nor measured fiber minima proves `inf_f,g S_s(f,g)>0`, much less a positive all-h `c s^6`. Pair-separator floors also need not dominate AA4-E's independent globally injective unary-price bound: retaining both as complementary lower bounds is legitimate; summing them would double-count ORIGINAL motifs.

## 3. Exact pairwise-consistent analytic falsifier

Take three same-type factors x,y,z in a complete 3-label bijection onto Z/3Z. Three nonnegative pair costs vanish iff respectively `y=x+1`, `z=y+1`, `z=x+1` mod 3. Pairwise, each relation admits three zero-cost tuples. Every one has each singleton marginal uniform over 0,1,2; thus the three zero-cost pair distributions satisfy exact singleton separator consistency and are compatible with the global all-different *singleton* marginals. Consequently `L_ind=L_pair=0`; however the first two relations force `z=x+2`, contradicting the third. Every genuine bijection violates at least one cost, and (e.g. 0,1,2) violates exactly one, so `L_triple=1`. This is rigorous separation of pairwise-local from common triple source coherence, **not** a GQ all-h counterexample.

Moreover it supplies a fail-closed criterion for a future 3-consistency/cycle-aware relaxation: it MUST reject all three zero-cost pair constraints simultaneously, and it MUST not claim positivity from the mere existence of pairwise marginal agreement.

## 4. True ORIGINAL W32 direct verifier

For each pinned complete W32 S68 and S72 map:
1. Recompute all ORIGINAL positive six-incidence Q and 30-typed-source transversals; require exactly AA4-C/AA4-D 53 or 119 critical original size-4 hitting blocks.
2. Select a deterministic genuine size-3 pure-point and pure-line subblock of critical size-4 ORIGINAL hitting sets. Freeze all ORIGINAL factor maps outside that block. Enumerate exactly each of the `3!=6` distinct **globally complete** K6 assignments of the three labels (12 per W32 map). No mix of unrelated Q physical choices.
3. For each of those maps independently run the accepted historical seven_census on ALL **62,370** actual ORIGINAL left candidates and the same original W32 45-incidence host. Preserve the actual GF5 class of every Q and its exact certified 51-palette numerator.
4. Construct per-Q tables from the union of ORIGINAL sixsets positive in at least one complete state; derive each Q's TRUE source intersection with B from the six original incidence endpoints. **Fail closed** if equal assignments to these factors ever yield different Q class-presence/weight (source support-invariance violation), or if recomposed scores differ from the independent complete full original census.
5. Compute and compare independent-Q, paired-separator, and triple-globally-coherent exact minima of seven-S and of the selected GF5 necessary numerator. Check every state ≥ the unchanged-positive source-support AA4-C lower bound. Record honest resulting numbers only after GitHub-hosted runs.

This is deliberately a targeted exact finite **conditional** test, not a whole W32 global search, a W34 full GF5 scan, or an all-h `S >= c s^6` certificate.

## 5. Acceptance / next mathematical question

Files: `research/hyp105_issue230_d6aa4f_three_factor_separator.py`, `research/test_hyp105_issue230_d6aa4f_three_factor_separator.py`, dedicated GitHub-hosted matrix workflow. Tests independently verify pair/triple hierarchy for random nonnegative functions of *only* declared ORIGINAL source supports, exact full typed fixed-image permutation fibers, fail-closed violation of declared dependencies, and the strict cyclic counterexample. Full W32 matrix jobs verify both genuine original source schemes independently and GF5 numerators by one consistent map per state.

Require exact final-HEAD dedicated, INDEX, Proof Audit, Research SUCCESS and independent math review before acceptance. Next **D6-AA4-G** should search an ALL-h source-independent third-order minorant with a tractable certified dual (or independently falsify it against D6-X/Y pseudodistributions and full seven-class W32), not widen brute-force edits and not infer GF5-positivity from physical-P3-only visibility.
