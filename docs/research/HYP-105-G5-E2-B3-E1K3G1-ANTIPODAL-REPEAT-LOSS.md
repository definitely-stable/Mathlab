# HYP-105 E1-K3-G1 — antipodal repeated-column C6 and source-pencil triangles

2026-10-12. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Independent stacked Draft child of [PR #372](https://github.com/definitely-stable/Mathlab/pull/372), pinned HEAD `4129b88d7232060b55c8fc3a45050f23976d545e`. No changes to main.

**Status:** RESTRICTED_THEOREM_C / exact all-h source-repeat identity and o(s^6) **triple-repeat** bound; single-repeat and seven-family S remain OPEN_WITH_FORMAL_BLOCKER.

## 1. Antipodal repetition

Each original incidence (p,l), labeled by pairs {x,x'} and {y,y'}, contributes exactly two Kikuchi edges (x,y)-(x',y') and (x,y')-(x',y). They are disjoint. An edge connecting any corner of one to any corner of the other would preserve x or y and is forbidden in the Kikuchi graph. Thus if a SIMPLE six-cycle uses a given original incidence twice, those two edges must be opposite around the cycle.

For the rectangle corners A=(x,y), B=(x',y'), C=(x,y'), D=(x',y), define c_uv=|N(u) intersect N(v)|, and t(U,V)=|N(U) intersect N(V)|. Two matchings of aligned corners close the two antipodal column edges by two internally vertex-disjoint two-paths. Therefore the number of six-cycles containing BOTH edges of this column is EXACTLY

```
j(p,l) =
    c(A,C)*c(B,D) - |N(A)∩N(C)∩N(B)∩N(D)|
  + c(A,D)*c(B,C) - |N(A)∩N(D)∩N(B)∩N(C)|.
J = sum_{(p,l) in original incidences} j(p,l).
```

The subtractions enforce two different internal vertices. No cycle enumeration or independence of global maps is assumed.

## 2. Exhaustive universal six-walk shape lemma

A length-6 cyclic coordinate sequence is represented up to renaming its physical coordinate values by its canonical restricted-growth sequence, starting at 0, with consecutive values unequal. There are exactly **41** such sequences. For every pair of such sequences (first and second physical coordinates), reject repeated physical vertices and form each of six original incidence labels from unordered adjacent x-pairs and unordered adjacent y-pairs. This exhaustive 41x41 finite classification yields:
- 879 patterns with 0 repeated columns;
- 48 patterns with 1 repeated column;
- **0 patterns with 2 repeated columns**;
- 2 patterns with 3 repeated columns.

The two patterns with three repeats have physical coordinate footprints 2x3 or 3x2. There are no other degeneracy shapes. Because coordinate renaming is purely combinatorial, this exhaustive finite classification applies for EVERY s=2^h, ANY global legal f,g, and every simple Kikuchi six-cycle.

Write R_1 and R_3 for the numbers of six-cycles with exactly one and exactly three repeated original columns. Hence
```
J = R_1 + 3*R_3,
C6_repeated_original_column = R_1 + R_3 = J - 2*R_3.
```
The symbols R_1,R_3 denote repeated-column C6 counts, **not the GF5 risks R2/R3** in issue #230.

## 3. Triple repeats are source-pencil triangles

For each original POINT p, let G_p be the simple graph on physical LINE-coordinate alphabet [a] with exactly s+1 distinct edges g(l), l incident to p. For each original LINE l, let F_l have the physical POINT-coordinate edges f(p), p incident to l. A three-repeat C6 necessarily alternates across ONE fixed original physical point-edge f(p) and follows a triangle of three edges from G_p, OR alternates across one fixed line-edge g(l) and follows a triangle of F_l. Conversely, each such pencil triangle creates exactly one simple Kikuchi C6 with three repeated columns. The two cases have 2x3 and 3x2 distinct-coordinate footprints and cannot overlap:

```
R_3 = sum_p triangles(G_p) + sum_l triangles(F_l).
```

For any simple graph with m edges and adjacency eigenvalues lambda_i:
`6T=trace(A^3)<=lambda_max*trace(A^2)<= (2m)^(3/2)`.
Every source pencil has m=s+1 edges, and W(3,s) has V=(s+1)(s²+1) source points and V source lines. The integer universal bound is therefore

```
R_3 <= 2V * floor( sqrt((2(s+1))^3) / 6 )
     = O(s^(9/2)) = o(s^6).
```

This is a genuine uniform all-h result. It controls ONLY the triple-repeat part; it does not establish C6_repeated=o(s^6) because R_1=J-3R_3 is not yet universally bounded.


## 4. New all-h aligned codegree packing theorem — J=O(s^6)

Let `c_x(y,y')=codeg_Ghat((x,y),(x,y'))` for y!=y'. Fix a third physical line coordinate t different from y,y'. The two source lines mapped to physical pairs {y,t} and {y',t}, if they both exist, are distinct. By the GQ axiom they intersect in **at most one** original point p. For a common neighbor of the aligned Kikuchi pair, its first physical coordinate x must be one of the two endpoints of f(p); the other endpoint determines the neighbor uniquely. Hence this t contributes **at most two** to the total over all x:

```
sum_x c_x(y,y') <= 2*(a-2).
```

Dually, fix x!=x' and sum over y:
```
sum_y codeg_Ghat((x,y),(x',y)) <= 2*(a-2).
```
These are ALL-h GQ incidence-coupled aligned-codegree inequalities; unlike a pointwise codegree cap, they retain the collision budget shared by every physical star.

For each original line l with g(l)={y,y'}, its s+1 incident original points have **distinct** physical pair labels f(p)={x,x'}. Its horizontal contribution to the raw antipodal incidence upper is therefore at most `sum_{x<x'}c_x*c_x'`, itself at most `(sum_x c_x)^2/2 <= 2(a-2)^2`. Sum over V original lines, and use the dual result for the vertical contribution summed over V original points. The internal-middle-vertex overlap subtraction in J is nonnegative. We obtain the NEW universal explicit inequality:

```
0 <= J <= raw_aligned_products <=
  refined_aligned_marginal_cap <= 4*V*(a-2)^2
  = O(s^6),    V=(s+1)(s^2+1),
               a=min{a: binom(a,2)>=V}.
```

The refined exact-integer conditional cap is the sum, over each original-line physical pair y,y', of `((sum_x c_x)^2-sum_x c_x^2)/2`, plus the dual sum over each original-point physical pair x,x'. It can be computed from the single global Kikuchi graph and is independent of C6 enumeration. Independent tests reconstruct every c_x from original GQ line-line intersections (and its dual from original point-point collinearity), instead of trusting the Kikuchi codegree routine.

**Limit:** Since `a^2 ~ 2V`, the last bound has leading scale `<= 8s^6(1+o(1))`. This REMOVES one extraneous power compared to separately bounding two aligned codegrees by O(a) on each of N=Theta(s^4) original columns, which would give O(s^7). It does not prove J=o(s^6), so by itself it cannot be subtracted from a six-cycle supersaturation bound to force an all-h positive floor.

## 5. Relation to K3-F2 and precise remaining blocker

K3-F2 classifies **chorded** C6 by proper, improper-six-distinct-column, and repeated-source classes. This G1 identity counts **all** repeated-source six-cycles, chorded or not, independently of C4 adjacency. Thus it isolates the repeated-column loss in K2's complete-R3 cycle route, which is DIFFERENT from proving the seven-family S obstruction.

A promising K3-G2 goal is to prove an all-h joint-original-source inequality for **J**, preferably J=o(s^6) or a small explicit upper constant below the independent six-cycle supersaturation coefficient. Note that J depends on products of aligned codegrees across the SAME original incidence rectangle. Bounding each factor by a per-pair maximum gives O(s^7), too weak; a shared-pencil packing theorem is necessary. An alternative is to bound only R_1 directly, then combine with the proven R_3=o(s^6).

Even if all repeated C6 losses become o(s^6), a COMPLETE R3 lower bound would not by itself prove the ORIGINAL seven-family S lower bound required by Branch A. Proper-vs-improper distinct columns remain independent obstacles.

## 6. Independent reproducibility

Reference: `research/hyp105_g5e2b3e1k3g_repeat_loss.py`. Oracles: `research/test_hyp105_g5e2b3e1k3g_repeat_loss.py`. GitHub-hosted path-limited `hyp105-k3g1-contract.yml`, inherited Research/INDEX. Independent simple six-cycle DFS reconstructs original source columns from global labels; independent per-pencil triangle enumeration crosschecks both sides. Canonical 41x41 patterns are exhaustively falsified without using the reference implementation. Budgets fail closed. No merge or Branch A/B decision until reviewed and CI green.
