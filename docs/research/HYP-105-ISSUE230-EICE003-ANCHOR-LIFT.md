# HYP-105 #230 — EICE-003-A: exact GQ anchor-lifted collision tensor

Status: **RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER**. Parent: [PR #450](https://github.com/definitely-stable/Mathlab/pull/450) at frozen HEAD \`edd5ecc26531bcd4ffe58a5fd1e5f3d017219118\`. Original ROOT Branch A/B remain OPEN. This is an ALL-h necessary geometric theorem, NOT the EICE-003 universal collision-energy upper bound.

## Why the previous EICE-001 energy is too coarse

Original EICE-001 \`nu_f(r,x)\` and \`nu_g(q,y)\` forget the OTHER ORIGINAL endpoint. Its physical carrier \`C_f={(r,x):some p in r has x in f(p)}\` can contain many events unrelated to the actual unique projection of the endpoint pair. Thus a high value of the carrier W does not imply high internal anchor blocking. In true W32 S68 (EICE-001), \`theta_W≈0.967\` but \`theta_I≈0.021\`. EICE-001 is sound, but this gap is a genuine motivation to retain BOTH original endpoints.

## Exact models and distributions

Fix any \`s=2^h\`, \`V=(s+1)(s^2+1)\`, \`N=V(s+1)\`, and arbitrary globally injective \`f:P->pairs([a])\`, \`g:L->pairs([a])\` of ORIGINAL GQ points/lines. Let \`H\` be any physical graph assembled from WHOLE pairs of Kikuchi diagonals of original incidence IDs, and \`mu\` any normalized distribution on oriented physical NB3 walks that is invariant under path reversal. It may be the genuine stationary NB law of EICE-002 G* when active min degree >=2 or the correctly normalized surviving-walk conditional law on a finite graph with leaves.

For \`gamma=(z0,z1,z2,z3)\`, \`zj=(xj,yj)\`, only count when all 4 coordinates on each side are distinct, physical endpoints \`{x0,x3}=f(q)\`, \`{y0,y3}=g(r)\` exist, \`(q,r)\` is ORIGINAL NONINCIDENT, and the unique ORIGINAL projection \`q--ell--p--r\` is END CLEAN:

    f(p) intersect f(q) = empty,  g(ell) intersect g(r) = empty.

These are filter conditions, not assumptions about the entire distribution. They define subprobability distributions (with absent/invalid mass simply omitted)

    pi_f(q,r,x) = Pr_mu[eligible gamma and x1=x],
    pi_g(q,r,y) = Pr_mu[eligible gamma and y1=y].

Define energies

    A_f = sum_(q,r,x) pi_f(q,r,x)^2,
    A_g = sum_(q,r,y) pi_g(q,r,y)^2.

Each equals the probability that two INDEPENDENT mu walks land in the SAME TRIPLE of true original endpoints (q,r) plus one first internal physical coordinate (and both pass eligibility filters).

Let \`theta_I\` denote mu mass of eligible walks with \`x1 or x2 in f(p)\` or \`y1 or y2 in g(ell)\` (the D1 internal-only mask). Define \`C_clean\` as the exact number of original ordered point/line pairs (q,r) that are nonincident and have end-clean projection as above.

## Theorem A1 — exact all-h anchor support

    V^2 - N = N*s^2.

This is an EXACT ORIGINAL GQ identity, not an asymptotic relation, because
\`V-(s+1)=(s+1)s^2\`. Every nonincident pair has precisely one ORIGINAL projection \`(p,ell)\`. Each has exactly two left anchor physical coordinates \`f(p)\` and exactly two right anchor physical coordinates \`g(ell)\`. Consequently the geometric carrier sets

    A_f^all={(q,r,x): (q,r) nonincident, x in f(p(q,r))},
    A_g^all={(q,r,y): (q,r) nonincident, y in g(ell(q,r))}

have EXACT cardinality \`2*N*s^2\` EACH. Restricting to end-clean endpoint pairs gives EXACT cardinality \`2*C_clean\` EACH, with \`0<=C_clean<=N*s^2\`.

## Theorem A2-CLEAN — the stronger necessary obstruction

By reversal invariance, the first/second internal left events have equal mu mass once the original endpoint filters are included. An actual internally blocked eligible path must satisfy at least one of those two left coordinate tests or two right coordinate tests. Hence, with \`U_f=sum_(q,r,x in f(p(q,r))) pi_f(q,r,x)\` over the end-clean carrier and dually U_g,

    theta_I <= 2 U_f + 2 U_g.

On each side, source support Cauchy–Schwarz yields

    U_f^2 <= 2*C_clean*A_f,    U_g^2 <= 2*C_clean*A_g.

Applying Cauchy–Schwarz in the two-dimensional vector (sqrt A_f,sqrt A_g):

    theta_I^2 <= 16*C_clean*(A_f+A_g)
              <= 16*N*s^2*(A_f+A_g).             (A2-CLEAN)

All-h, every correlated f,g and every reversible mu. This is an actual mathematical proof of a NECESSARY inequality, **not** a proof of the missing universal upper bound.

The first inequality is sharper than a uniform coefficient by a factor \`C_clean/(N*s^2)\`, which depends on the SAME actual f,g, not on any random labeling. If \`C_clean=0\`, \`theta_I=0\` automatically.


## Theorem A3 — exact conditional-anchor Parseval decomposition

For each ORIGINAL end-clean nonincident pair (q,r), let

    t(q,r) = sum_x pi_f(q,r,x) = sum_y pi_g(q,r,y).

Both sums are exactly equal because every eligible path contributes exactly one internal x1 and one internal y1. Define the true-original endpoint-collision energy

    T2 = sum_(q,r) t(q,r)^2,

and the orthogonal internal-coordinate residuals

    R_f = sum_(q,r,x) [pi_f(q,r,x)-t(q,r)/a]^2,
    R_g = sum_(q,r,y) [pi_g(q,r,y)-t(q,r)/a]^2.

Then the following identity is exact for ALL f,g and every reversible normalized mu:

    A_f + A_g = (2/a)*T2 + R_f + R_g,         (A3)

with R_f,R_g >= 0. Proof: for each (q,r), sum_x pi_f=t, hence in the expansion of
sum_x [pi_f-t/a]^2 the cross term cancels and sum_x(t/a)^2=t^2/a. Repeat
independently for right internal coordinates and add.

Moreover, the t-mass is supported only on the EXACT C_clean true original endpoint pairs. For P_eligible=sum_(q,r)t(q,r),

    T2 >= P_eligible^2/C_clean       (C_clean>0).

This provides a genuine **mechanism dichotomy**, not a Branch A proof. If A2-CLEAN requires large A_f+A_g, it must arise from collision concentration among ORIGINAL endpoint pairs (large T2) and/or conditional internal-coordinate imbalance (large R_f+R_g). Future EICE-003-B can attack these **two independently testable quantities** using the original GQ spectrum; a bound on T2 alone is insufficient without the residual bound and vice versa. No universal upper for either term is claimed.

## Comparison with EICE-001, and what does NOT follow

The eligible \`pi_f\` tensor includes q as an additional original index. If we sum over q first, its squared L2 energy can only grow; hence

    A_f <= sum_(r,x)[sum_q pi_f(q,r,x)]^2,
    A_g <= sum_(q,y)[sum_r pi_g(q,r,y)]^2.

Moreover the eligible marginal is pointwise <= EICE-001's original unrestricted endpoint-interior mass; therefore \`A_f<=E_f\` and \`A_g<=E_g\` on the same mu. But A2-CLEAN has a larger support coefficient \`C_clean=O(s^6)\` instead of EICE-001's \`N=Theta(s^4)\`. Therefore A2-CLEAN is **NOT pointwise stronger as an upper bound on theta_I** on every input; it is structurally more specific, and its usefulness requires an independent triple-collision ENERGY UPPER of order \`o(s^-6)\` or strict constant below \`1/(16*C_clean)\`.

If EICE-002 theorem R were independently accepted in its full quantitative form, any hypothetical \`S=o(s^6)\` would force \`theta_I(G*)=1-o(1)\`, hence

    A_f(G*)+A_g(G*) >= (1-o(1))/(16*C_clean)
                   >= (1-o(1))/(16*N*s^2).

**THIS IS ONLY A NECESSARY PROFILE OF A COUNTEREXAMPLE.**

The new target is to prove that, for every complete true f,g, there exists a valid high-degree/density paired G* with \`16*C_clean*(A_f+A_g)<=(1-eta)^2\` for a uniform eta>0, OR to falsify this target with a genuine infinite coherent original-GQ family. A single small-s finite failure is NOT an asymptotic falsifier.

## Executable exact falsifiers

- \`research/hyp105_issue230_anchor_lift.py\`: canonical true ORIGINAL GQ projection and globally injective source validation reused from PR #394 and EICE-001, all physical NB3 walks with exact Fraction weights, ORIGINAL q/r endpoint identification, exact end-clean filter, anchor-lifted pi tensors, independently accumulated pair-collision recurrence, two carrier CS checks, scalar bound A2-CLEAN, ordinary A1, and unlifted same-filter marginal sanity comparisons.
- \`research/test_hyp105_issue230_anchor_lift.py\`: four ORIGINAL W32 global labeling fixtures, exact EICE-001 theta_I agreement, strict end-clean support size, whole-diagonal paired G* outputs, two TRUE ORIGINAL W34 instances, fail-closed corrupted maps and invalid path-budget / stationary-min-degree claims.
- \`.github/workflows/hyp105-issue230-eice003.yml\`: Github-hosted ubuntu-latest focused CI and EICE-001/002 regression; no self-hosted runners.

## Next slice: EICE-003-B (OPEN)

For true high-degree G*, develop spectral control of the JOINT ORIGINAL (q,r,x/y) triple-collision tensor. Preserve the GQ projection in the kernel, rather than bounding a projection-free physical carrier. A proof must handle arbitrary same-map correlations and structured symplectic-spread/Baer examples. Independently seek maximum normalized A2-CLEAN ratio across several different, still admissible paired G* constructions, not just one deterministic pruning. Compare against TRUE ORIGINAL GF5 C/B and B/C witnesses only after source incidence IDs and multiplicities are retained. Maintain no root Branch A assertion until a uniform all-h upper is proved.
