# HYP-105 B3.2-E1-C24-A1 — ALL-h right-C star collisions and original W(3,2) finite zero witness

Date: 2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked scientific child of C23 [PR #334](https://github.com/definitely-stable/Mathlab/pull/334), not main. This document proves two elementary **deterministic ALL-h lower inequalities** and freezes one independent genuine-GQ **finite counterexample to C-only positivity**. Neither establishes the seven-class global minimum or full GF(5) R3.

## 1. Model and accepted scope

Let s=2^h>=2, V=(s+1)(s^2+1), a=min{a: C(a,2)>=V}. Let f map all ORIGINAL points of W(3,s) bijectively onto an occupied physical left pair alphabet F_L subset K_a, |F_L|=V. Let g map all ORIGINAL right GQ lines bijectively onto an occupied F_R subset K_a, |F_R|=V. Both are ONE complete coherent global map each, never independent per source set.

Define J_C(f) as the set of DISTINCT six-original-incidence-ID source sets whose physical LEFT pairs form a six-coordinate degree-two 2-factor and whose ORIGINAL RIGHT endpoint profile is precisely C=(2,2,2): three distinct ORIGINAL lines each represented by two original incidence IDs. Let H_C(f)=|J_C(f)|. For each unordered distinct ORIGINAL right line pair i,j let W_f(i,j) be the number of members of J_C(f) containing both lines. Then W is symmetric with zero diagonal and sum_(i<j)W(i,j)=3H_C. This counts ORIGINAL SIXSETS, not physical automorphism orbits or GF5 signed events.

Each such J has an accepted B0 seven-family tag C/A or C/B if and only if g maps its three distinct original right lines to THREE MUTUALLY VERTEX-DISJOINT physical pairs. GQ has incidence girth eight, so an ORIGINAL left C=(2,2,2) and right C=(2,2,2) would imply a forbidden original incidence 6-cycle; no missing accepted C/C class is assumed. All fixed-left projection physical repeats are preserved.

Write S_(R=C)(f,g) for the number of these surviving J. Then always S_seven(f,g)>=S_(R=C)(f,g), for every legal f,g.

## 2. Exact ALL-h pointwise star-collision certificate

For physical coordinate x define L_x(g)={i: x in g(i)}. Since F_R is an occupied subset of K_a with distinct edges, |L_x(g)|<=a-1 and sum_x |L_x(g)|=2V.

A right-C source J fails the physical right 2-factor iff at least one of its THREE ORIGINAL right-line pairs has intersecting images under g. Apply the union bound **deterministically** to these three possible pair conflicts; count a conflicting original line pair (i,j) at its unique common physical coordinate x. This gives, for EVERY s,f,g:

    S_seven(f,g) >= S_(R=C)(f,g)
      >= H_C(f) - SUM_x SUM_{i<j; i,j in L_x(g)} W_f(i,j).              (C24.1)

No independence, positivity assumption, random permutation or concentration is involved. The right side may be negative and must not be interpreted as a positive guarantee. The exact finite implementation checks this for a full original right witness and all 105 complete global right transpositions.

## 3. Centered matrix and ALL-h spectral consequence

Let mu=6H_C/[V(V-1)] and B=W-mu*(J-I), so W has mean off-diagonal weight mu. With z_x the indicator vector of L_x(g), each physical coordinate contributes

    sum_{i<j in L_x(g)} W_ij
      = mu*C(|L_x|,2) + (1/2)*z_x^T B z_x
      <= mu*C(|L_x|,2) + (1/2)*||B||op*|L_x|.

Since |L_x|<=a-1 and sum_x|L_x|=2V:

    sum_x C(|L_x|,2) <= V*(a-2).

Therefore EVERY legal f,g satisfies

    S_seven(f,g) >= H_C(f)*(1-6(a-2)/(V-1)) - V*||B_f||op.             (C24.2)

This is a conditional structural certificate. To prove Branch A of issue #230 by this route one would STILL need a uniform all-f lower on H_C and a sufficiently strong all-f operator-norm control. Neither is established. The executable returns a computable exact-rational **upper** on the operator norm, using min(max absolute row sum, ceiling Frobenius norm); it does **not** claim to compute exact eigenvalues, and clamps negative certified lower results to zero.

For a~sqrt(2)*s^(3/2), V~s^3 the geometric factor tends to one with error O(s^(-3/2)). This favourable factor alone does NOT control V*||B||op.

## 4. Independent TRUE original W(3,2) right-C falsifier

We construct W(3,2) from nonzero GF(2)^4 vectors 1..15 and alternating form

    <x,y>=x0*y2+x2*y0+x1*y3+x3*y1 mod2.

An ORIGINAL line is an isotropic three-point set (p,q,p XOR q). Original lines are sorted lexicographically; point p in 1..15 maps to K6_PAIRS[p-1] in lexicographic physical pair order. There are 15 original points, 15 original lines, 45 original incidence IDs.

Two **different enumerator strategies** agree exactly:
- right-first: choose three distinct ORIGINAL lines, then two different ORIGINAL point incidences on each, and filter by physical-left degree two;
- left-first: enumerate ALL 130 physical K6 degree-two multigraph templates, choose distinct ORIGINAL right incidence IDs for every original physical left point use, then filter original-right endpoint profile C.

The left-first source contains EXACTLY 62,370 DISTINCT original sixsets: physical original-left profiles A=51,030, B=10,935, C=405. Both methods yield H_C=92 and 83 distinct ORIGINAL right-line triples with positive weights. The pair tensor has sum_(i<j)W_ij=276 and max pair weight=7.

Under the ONE SAME globally complete ORIGINAL right bijection

    original_line_i -> K6_PAIRS[perm[i]]
    perm = (1,13,3,6,10,9,8,0,7,2,11,5,14,12,4)

all 92 original right-C source sixsets FAIL their required physical right disjointness: S_(R=C)=0 exactly, whereas the uniform-global-right expectation is 92*(3/91)=276/91 > 0. The witness falsifies any claim that H_C>0, or its positive mean, suffices for strictly positive S_(R=C) at s=2. It does NOT show S_seven=0 (other six families remain), nor a counterexample for infinitely many s.

At s=2 the geometric coefficient in (C24.2) is -5/7, so the spectral certificate is vacuous; never extrapolate it to all h from finite tests.

## 5. Implementation, independent falsification, scientific gate

- research/hyp105_g5e2b3e1c24_right_c_certificate.py
- research/test_hyp105_g5e2b3e1c24_right_c_certificate.py
- .github/workflows/hyp105-c24-contract.yml

The tests demand BOTH enumerators, the 92/83/276/7 frozen source/tensor signatures, the global zero-C witness, all 105 complete right-line permutations obtained by one transposition of that witness, exact rational all-h geometry arithmetic for s=2..128, and fail-closed malformed global injections. Dedicated C24 Contract + full six GitHub-hosted Research shards + INDEX are required at the exact PR HEAD, with command preservation guard.

**Nontransfer:** This is RESTRICTED_THEOREM_C for a conditional certificate plus FINITE_C_ONLY_ZERO at s=2. No all-f asymptotic H_C bound, no all-f centered norm estimate, no universal S_seven lower, no infinite correlated small-S family, no full R3 or ASET exponent. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains OPEN_WITH_FORMAL_BLOCKER. Next C24-B should ask whether star-constrained weighted discrepancy admits a true all-f bound; only then proceed to a full seven-family joint structural certificate or exact overlap second moment.
