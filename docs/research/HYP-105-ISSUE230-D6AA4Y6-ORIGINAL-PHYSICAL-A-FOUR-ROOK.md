# HYP-105 / issue #230 — D6-AA4-Y6: exact ORIGINAL B/A opposite physical-A 2-factor × 4-rook alignment

**Research status.** This slice proves an exact ALL-h same-original-Q joint physical-A gate and a sharp ALL-h `per(4x4)<=3` source-GQ incidence bound, with independent finite exhaustive W(3,2) validation. It does **not** prove universal `S_s(f,g)=Omega(s^6)` or supply an infinite adversarial counterfamily. Strict research-only child of [Y5 PR #507](https://github.com/definitely-stable/Mathlab/pull/507), pinned parent HEAD `1e21d8a8f25e023f627afa5ebe0d72e39c5e391d`. Root #230 remains OPEN; main untouched.

## 1. Y5's missing gate

Y5 counted genuine ORIGINAL B/A source forests after fixing an actual source B factor p, two different actual incidences `(p,ell_1),(p,ell_2)`, and a *physically realized* C4 on four singly used original source factors `q_1..q_4`. For each i the genuine opposite original source neighbor set `N(q_i)\{ell_1,ell_2}` supplies an injective four-neighbor rook assignment. However, even when that source A forest exists, historical selected positive GF(5) acceptance ALSO requires the six physical edges assigned by the one complete globally fixed opposite map g to ell_1,ell_2 and the four other genuine opposite factors to be 2-regular on exactly six physical coordinate symbols. The two conditions are correlated through the SAME original incidence IDs Q and the same globally injected g. No independence or multiplication of marginals is permitted.

## 2. NEW all-h exact physical 2-factor–four-rook joint identity

Fix any genuine symplectic original generalized quadrangle W(3,s), s=2^h>=2, original source degree d=s+1, V=(s+1)(s^2+1) actual source factors of each typed side, minimal physical alphabet size a with C(a,2)>=V, and ONE global injective physical pair map f for source points and ONE g for original source lines. The argument dualizes point and line. Fix actual original source point p, two distinct genuine lines ell_1,ell_2 incident to p, and four different other source point factors q_1..q_4 whose f-images form the physically realized four-edge C4 complementary to f(p) within a physically B-valid six-incidence half pattern. Define e_1=g(ell_1), e_2=g(ell_2), two distinct canonical physical K_a edges.

Let `F_a(e_1,e_2)` denote all six-edge 2-regular physical 2-factors H of K_a containing BOTH edges e_1,e_2, each on exactly six physical coordinate symbols. For H, define its four other physical edges R(H)=H\{e_1,e_2}. If ANY edge in R(H) is unoccupied in the global opposite map g, the pattern contributes 0. Otherwise use the unchanged inverse global map g^{-1} and write the FOUR *distinct actual original opposite source* factors t_1..t_4 whose g-images are the four canonical physical edges in R(H). Their order is deterministic but irrelevant to the permanent. Form the 4×4 binary matrix

    M(H)_(i,j) = 1_{(q_i,t_j) is an ACTUAL original point-line incidence}.

**Exact theorem (all h, every complete global f,g):** The number of historical positive original B-left/A-right GF(5) six-incidence Q rooted at precisely this real p, this exact pair of p-incidence IDs, and these exact four physical B-source factors q_i is

    A(p;ell_1,ell_2;q_1..q_4;f,g)
       = sum_{H in F_a(e_1,e_2)}
           1_{R(H) subset of physically occupied image(g)} * permanent(M(H)).

An empty or unsupported set yields exactly zero. In the dual orientation swap original point/line roles and f/g. No source flags or labels are independently resampled per H or Q. The historical B/A tag is immutable by the source endpoint multiplicity (one repeated B root on one side and all distinct A endpoints on the other); there is NO additional positional C6 test for B/A.

**Proof — bijection, no averaging.** Every positive historical B/A Q fixes the two distinct actual p-incidences and four other actual point sources q_i, so it assigns each q_i to a distinct genuine original opposite line t_j using real source incidences. The six original opposite line factors are therefore distinct. Their physical edges under the single g form a degree-two six-edge physical 2-factor H of K_a containing the already pinned g(ell_1),g(ell_2); its other four edge images must be physically occupied, and the source assignments define one perfect matching in M(H). Conversely, each occupied H and each perfect matching in its genuine original incidence 4×4 submatrix produce exactly one six-distinct-original-incidence Q of the specified B/A source forest class with physically 2-regular A opposite projection, hence accepted historically. These constructions are inverse, and distinct H or matchings yield distinct original Q. The formula is exact for all h and ANY globally complete f,g, not a W32 extrapolation.

## 3. NEW SHARP all-h original-GQ four-rook permanent lemma

**Lemma:** Every 4×4 0/1 incidence submatrix of a genuine original generalized quadrangle has at most THREE perfect matchings, i.e. `per(M)<=3`. The constant 3 is sharp among all abstract 4×4 source incidence submatrices with no K2,2; it need not be attained inside every fixed W(3,s). This improves the a priori `4!=24` upper by factor eight.

**Combinatorial proof (not dependent on computation).** Genuine GQ incidence girth >=8 forbids any two different point sources sharing two line factors, so each pair of rows of M has at most one shared 1-column.

Classify by row degrees, after arbitrary permutations of rows and columns.

1. If a row has degree zero, there are no perfect matchings. If a row has degree one, that row forces its unique assigned column and the residual 3×3 binary incidence matrix is still K2,2-free. Every such 3×3 matrix has at most TWO perfect matchings: with a degree-one row reduce again to a 2×2 K2,2-free matrix with at most one perfect matching; otherwise all three rows have degree >=2, but a degree-three row would share >=2 columns with every other degree>=2 row and create forbidden K2,2. Thus every row has degree exactly 2. Fixing one perfect matching as diagonal leaves one off-diagonal choice per row; an alternative perfect matching is a directed cycle of length >=3 (a length-2 cycle would produce K2,2 with the diagonal), and on three rows at most one such cycle exists. So the 3×3 maximum is 2.

2. Now assume all four rows have degree at least two. If a row has degree four, every other row of degree at least two shares two columns with it, prohibited. If some row r has degree three, let its three neighbors be columns c1,c2,c3 and let c4 be the remaining column. Each of the other three rows can meet {c1,c2,c3} in at most one column, and degree>=2 forces c4 to be present; since they all contain c4, their other allowed neighbors are DISTINCT. Thus all three other rows have exactly two neighbors, c4 plus one distinct c_i, and there are exactly THREE perfect matchings (one for each choice of the row assigned to c4).

3. Otherwise all four rows have degree exactly two. Fix one perfect matching as diagonal, if none exists the permanent is zero. Each row has one other off-diagonal 1-entry; view that entry as an outgoing directed arc to its column. Every alternative perfect matching corresponds to one directed cycle of length at least three, since any directed 2-cycle together with the two diagonal matched entries would create a forbidden K2,2. A functional digraph on four vertices has at most one such nontrivial cycle (two disjoint cycles would both have length at least three), so there are at most TWO perfect matchings.

These cases prove `per(M)<=3`. Sharp witness via source row-neighbor masks in column order `[14,9,5,3]`: row0 sees columns {1,2,3}, row1 {0,3}, row2 {0,2}, row3 {0,1}; each pair of rows intersects in <=1 column, and the matrix admits three matchings.

**Independent finite exhaustive falsifier:** scan all 2^16=65,536 possible 4×4 binary matrices, retain the 18,521 with no K2,2, and compute exact permanents. The complete distribution is `0:11,993; 1:5,688; 2:744; 3:96` with maximum 3. This is a reproducible finite sanity check for the independent mathematical row-degree proof, not the sole foundation of the all-h claim.

## 4. All-h physical two-pinned 2-factor count and conditional historical upper

Two distinct globally injected opposite physical edge labels e1,e2 are either adjacent (share one physical coordinate) or disjoint. The exact number of 2-regular six-edge physical 2-factors in FULL K_a containing both is already established by Y3's physical pattern enumeration:

    Adjacent: |F_a(e1,e2)| = 7*C(a-3,3).
    Disjoint: |F_a(e1,e2)| = 14*C(a-4,2).

By the new genuine-GQ four-rook bound every H contributes 0,1,2,or3, so for EACH fixed true original repeated B root, distinct two p-incidence IDs and one physically realized B-C4 on four other actual point sources:

    0 <= accepted historical GF5 B/A count
         <= 3*7*C(a-3,3)    if g(ell1),g(ell2) adjacent;
         <= 3*14*C(a-4,2)  if g(ell1),g(ell2) disjoint.

In the real W32 complete K6 case, this is 21 versus 42 per realized B-root C4, respectively, compared to a naïve 168 versus 336 from `4!`. For the 3 C4 source patterns per fixed original W32 repeated source/two-flag root cohort, the summed bounds are 63 or126, but they can be dramatically loose. These are source-GQ-supported **UPPER bounds**, never a positive lower on physically accepted B/A under an adversarial opposite global map g. For all h, the number of physical occupied 2-factors may be zero even when source-forest rook candidates exist.

## 5. Independent genuine ORIGINAL W32 validation

The module `research/hyp105_issue230_d6aa4y6_physical_A_four_rook.py` independently enumerates the physical six-edge K6 2-factors containing each selected pair of pinned physical opposite line labels, retrieves the four other actual line source IDs through the ONE globally complete inverse label map g, and evaluates the exact original 4×4 permanent against the TRUE source graph incidence sets. For every original W32 pinned anchor S68/S72/lex/reverse, on both B-left and B-right:

- 15 actual source B roots ×3 pairs of distinct genuine original incidence IDs ×3 actual complementary physically valid B-C4 source patterns = 135 tested rooted B-C4s per typed side, 45 source root/two-flag cohorts per side;
- each physical anchored opposite A completion uses 7 or 14 six-edge 2-factors according to the actual globally assigned pinned opposite physical edge relation;
- the 4×4 GQ incidence rook permanent is proven to lie between 0 and 3;
- every cohort's acceptance is independently compared with the Y5 literal 3^4 actual-original-neighbor source Q enumeration and its independent actual AA4-Q historical selected GF5 seven-class join. Cohort support and both per-class positive GF5 totals must match exactly;
- all nonzero permanent values, zero-accepted-rooted-cohort counts, physical edge pair adjacency classes and literal global rooted witnesses are preserved in machine-readable JSON.

Separately, another implementation enumerates the **physical edge sixset first**, then checks vertex degree two, over every physical 6-subset of K6 and K7. This confirms the adjacent 7*C(a-3,3) and disjoint 14*C(a-4,2) counts without sharing the enumeration logic. Independent random K2,2-free 4×4 literal permanent tests, hostile fake incidence rejection and the full 16-bit universe provide additional fail-closed evidence.

## 6. What remains open

While Y6 closes the exact algebraic **physical-A gate** for ONE already realized B-root C4, it does NOT supply the decisive positive intersection lower over all globally injected original f,g, nor a bound coupling B/A and A/B failures with inevitable contributions from other GF5 classes. In particular, source-forest positivity `T>0` does not imply any occupied physical A completion with positive 4-rook permanent. A universal all-h `S_s(f,g)=Omega(s^6)` statement cannot be deduced by multiplying source counts, physical 2factor marginals or upper bound 3. Root issue #230 Branch A/B/C remain OPEN.

Next scientific gate: derive a nonzero lower on the **sum of these four-rook permanents** across all true original rooted B-C4 cohorts OR a compensating quantified contribution from other accepted source forest classes, under arbitrary globally coherent f,g; alternatively find an explicit infinite adversarial correlated family. The new precise 4×4 matrices provide exact finite falsifiers for proposed positive charge-transfer inequalities.

**Acceptance:** keep this child PR Draft; require exact-head Dedicated/INDEX/Proof Audit/Full Research SUCCESS, retained full numerical JSON evidence, and independent mathematical referee. Do not modify main or close issue #230.