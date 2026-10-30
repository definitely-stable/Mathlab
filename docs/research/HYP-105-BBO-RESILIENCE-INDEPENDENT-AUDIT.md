# Independent adversarial audit of the universal sextic proof

Date: 2026-10-30. Reviewer: independent mathematical audit agent. This is a
independent internal review. It was first written outside the repository,
then included with this follow-up without changing the parent manuscript. The base manuscript is
[the immutable PR #672 manuscript](https://github.com/definitely-stable/Mathlab/blob/9c54f3c16af201ebf6d915de207d21d201da28d6/docs/research/HYP-105-UNIVERSAL-SEXTIC-OBSTRUCTION.md).

**Finding:** I found no fatal gap in the claimed uniform Branch A argument,
conditional on the explicitly cited source and balanced C6 supersaturation
inputs. I also checked the full degree-tail argument's use of that graph
theorem. This is an internal mathematical audit, not external acceptance.

## Critical implications checked

1. **Full degree tail (input (TAIL), lines 44–51).** In the cited tail
   manuscript, retained flags keep their preassigned heavy physical edge.
   Cutting the opposite bipartition into chunks of size at most the number
   of heavy vertices gives an ordinary graph F with
   `e(F)/v(F) >= beta*s/32` and `v(F) <= 32*s^3/T`. The stated threshold
   `T >= 2^20*C^3*beta^(-3)` is sufficient for balanced supersaturation.
   All its simple C6s remain proper in the coherent graph, and hence give
   distinct original D6 sixsets. This does not require a conjectural
   unbalanced supersaturation theorem.
2. **Truncations (lines 80–105).** At most E_T whole flags are lost in the
   physical-degree truncation, since a chosen heavy edge has unique flag
   provenance. The conflict graph has at most 2*C_s edges, so deleting its
   vertices of degree greater than K loses at most 4*C_s/K flags. Both
   physical diagonals are retained or removed together. The resulting
   pencil populations are at most K+1 by the clique argument.
3. **Simultaneous proper-path survival (lines 125–136).** Distinct first
   coordinates along a proper 2/3-path imply distinct original point
   labels, and likewise for lines. Thus its flags are independent in the
   conflict graph. Requiring these r flags to be the first r elements of
   their combined closed neighborhoods is sufficient even when those
   neighborhoods overlap. The two coordinate cuts cost exactly 4^(-r).
   The stated sigma2 and sigma3 are conservative lower bounds.
4. **Moments (lines 141–182).** A nonsimple closed 6-walk in a simple
   bipartite graph has a cyclic distance-two repetition. Deleting that
   backtrack gives the bound `6*Delta*tr(A^4)`; Cauchy then absorbs it and
   establishes (5). Jensen is used on endpoint entries, so (7) requires
   no independence between paths. For the core, `B2(u,v)<=Delta` and
   `sum B2<=Qx+Qy` give the separate improper-walk correction in (9).
   The exact identity is `Qx=2*sum R0^2=4*N0+4*M_g(core)`.
5. **Three-walk floor and odd coordinate returns (lines 188–208).** The
   edge-distribution/Jensen proof gives `(2*m0)^3/n^2`, including isolated
   vertices in n. The quadratic-form bound (10) uses only
   `||A0||_op<=Delta`; it does not require bipartiteness of the core.
   The total improper correction is at most
   `3*Delta*(Qx+Qy)<=84*T*s^5`.
6. **Exceptional endpoint weights (lines 210–227).** Each typed pair of
   distinct unordered coordinate labels gives four ordered physical
   endpoint pairs. The exceptional population is O(s^5), and (7) then
   bounds its *weighted* proper-path population by O(s^(11/2)). No
   assumption of uniform endpoint distribution is made.
7. **Mixed full/core internal blocking (lines 242–295).** Formula (13)
   counts every actual blocked triple: q determines the last first
   coordinate, and the two line labels sharing y determine the remaining
   second coordinates. It is valid to drop the projection/distinctness
   constraints. In (14), fixed x,p admits at most two k in f(p); the
   off-principal collinearity eigenvalues have absolute value at most d.
   In (15), rearranging sums gives exactly
   `sum_(k,y) D_full(k,y)*D_core(k,y)`. Therefore the *core* degree cap
   bounds this by `4*N*Delta`, even when p or its projection flags lie
   outside the core. The other cap gives
   `max K_pu<=2*d*(K+1)`. These prove the two squared-factor orders
   s^(11/2) and s^6, hence B=O(s^(23/4)). Finally
   `sum_(v0v1 oriented edge,v3) (A0^2(v1,v3))^2
   <=Delta*tr(A0^4)`, so the blocked-path order is s^(47/8), as claimed.
8. **Original-ID bridge and multiplicity (lines 310–337).** Properness
   makes the three path-point IDs and three path-line IDs distinct.
   The unblocked conditions make the appended factors distinct from
   those IDs. Their six-flag source graph is a P4 and three isolated
   edges. Each physical half is a doubled pair plus a disjoint C4.
   The two repeated factors' flag pairs meet exactly at (p,l), precisely
   the historical classifier's B/B-overlap condition (the unchanged
   classifier checks intersection size one). The repeated factors
   recover the P4; removing its closing pair from the left C4 orders
   the remaining three flags up to reversal. Their right labels then
   give a unique coordinate path for either order. Multiplicity is at
   most two, so (20) is sound.
9. **Constants and uniformity (lines 345–364).** The tail threshold at
   epsilon=1/8 is `2^59*C^3`, and its D6 floor is `c*2^(-108)*s^6`.
   The three s0 requirements make the three errors in (21) at most
   s^6/24 each. All constants are fixed before choosing maps or h, so
   the stated sufficiently-large uniform quantifier follows.

## Low-D6 coefficient-eight extension

Let `D6(f_s,g_s)=o(s^6)` along any admissible sequence, and let
`Z_s` be arbitrary original-ID sets with `|Z_s|=o(s^4)`. Fix small
epsilon>0. Choose fixed T=T(epsilon) by (TAIL), and a fixed large conflict
cap K=K(epsilon). Eventually E_T<epsilon*s^4. Delete flags in Z_s as
well as the two truncation populations. Then

    N0 >= N - epsilon*s^4 - 6*s^4/K - |Z_s|.

The exact minimal-alphabet asymptotics are
`a^2=(2+o(1))*s^3` and `N=(1+o(1))*s^4`. Since `m0=2*N0`, the
three-walk floor is therefore at least

    [16*(1-epsilon-6/K)^3-o(1)]*s^6.

For each fixed epsilon,T,K all the original exceptional/internal errors
remain o(s^6). The source projection masks caused by Z_s also have
o(s^6) weighted mass, by the following count. Each original flag appears
in each of the three positions of `q--l--p--r` for exactly s^2 typed
nonincident endpoint pairs (q,r). Hence at most `3*s^2*|Z_s|` typed
pairs have a projection touching Z_s. **The ordered physical endpoint
population needs the four-orientation factor**, so its bound is
`12*s^2*|Z_s|`. Using `||P3||_F<=M(T,K)*s^3` gives lost paths at most

    sqrt(12)*M(T,K)*sqrt(|Z_s|/s^4)*s^6 = o(s^6).

Thus, writing U_avoid for B/B-overlap sixsets all six of whose original
flags avoid Z_s,

    liminf U_avoid/s^6 >= 8*(1-epsilon-6/K)^3.

Take the s-limit with epsilon,T,K fixed; next choose K(epsilon) tending
to infinity and send epsilon down to zero. This proves
`liminf U_avoid/s^6>=8`. No uniform-in-epsilon error estimate, and no
choice epsilon=epsilon(s), is required or justified by this argument.

## Fixed positive deletion fraction and packing

Keep the base manuscript's K,T,delta,s0. Put

    M = sigma3^(-1)*sqrt(L6),
    rho = min{1/8, 1/(768*M^2)}.

If D6<delta*s^6, s>=s0, and |Z|<=rho*s^4, deleting Z as well leaves
`N0>=(25/32-rho)*s^4>=21*s^4/32`, so `m0>=s^4` and every base bound
continues to hold with the same constants. Before the additional
projection mask the old estimates leave at least s^6/4 directed
unblocked paths. The mask removes at most

    sqrt(12)*M*sqrt(rho)*s^6 <= s^6/8.

At least s^6/8 directed paths, hence s^6/16 distinct original B/B-overlap
sixsets, remain. A maximal disjoint family of B/B-overlap sixsets has a
union of 6*nu original IDs hitting every such sixset. If
`nu<=rho*s^4/6`, the preceding deletion statement contradicts maximality.
Thus in the low-D6 branch `nu>rho*s^4/6`. This argument does not assert
the same B/B-overlap packing in the complementary large-D6 branch.

No finite test or CI execution was used as a substitute for the mathematical
checks above. The reviewer did not change repository files or publication state. Root included
this audit in the separate resilience follow-up after checking its arguments.
