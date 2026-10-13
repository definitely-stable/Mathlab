# HYP-105 / issue #230 — D6-Y: sharp global-image adjacency cut and precise pairwise lifted-occupancy relaxation gap

**2026-10-13. RESTRICTED_THEOREM_C.** Draft strictly stacked on
[D6-X #424](https://github.com/definitely-stable/Mathlab/pull/424)
pinned HEAD \`893f590cc583c7a23a402ad9cf856b780219699f\`.
No main mutation, merges, or closure of #230/#176/#169.
Branch A and B remain OPEN. The result is geometry-independent
physical-image capacity mathematics VALID for all typed ORIGINAL
W(3,s) injections, but is NOT a positive GF5 root bound.

## 1. Why D6-X left a missing global constraint

D6-X constructed projectively consistent common-star local zero-GF5
pseudomarginals, then correctly disproved their feasibility for a
standard globally lifted injection formulation by the rank-two
physical column capacity inequality. It also proved all unanchored
D6-W-style overlap-only factor-separator dual lower certificates
are <=0 in the root.

Does enforcing these lifted physical column inequalities alone
characterize the possible two-site distributions of a globally
injective original point/line map? D6-Y answers **NO**, in an
independently checked, quantitative and all-h-sharp sense, by deriving
a NEW global physical image adjacency cut.

## 2. Theorem Y1 — SHARP all-h deterministic physical-image inequality

Fix s=2^h, h>=1, V=(s+1)(s²+1); let a be the MINIMAL integer with
K=binom(a,2)>=V; let m=K-V. By minimality,
C(a-1,2)<V<=C(a,2), hence 0<=m<=a-2.

For ANY globally injective original point physical-pair map
f:P(W(3,s))->E(K_a), its occupied physical IMAGE E has |E|=V.
Define A(E)=#unordered pairs of DIFFERENT occupied physical edges
sharing a coordinate. Equivalently,

    A(E) = sum_{c=0}^{a-1} C(degree_E(c),2)
         = sum_{p<q} 1[ f(p) and f(q) intersect physically ].

Let H=E(K_a)\E be the missing physical-edge graph, |H|=m,
with degrees d_H(c). Expand degree_E(c)=a-1-d_H(c):

    A(E) = a C(a-1,2) - 2m(a-2)
                           + sum_c C(d_H(c),2).

The final summand counts unordered pairs of missing physical
edges sharing a coordinate. Since H has only m distinct edges,
it is <=C(m,2). Therefore for EVERY f:

    A(E) <= A_max =
       a C(a-1,2)-2m(a-2)+C(m,2).

**The inequality is SHARP for EVERY h:** remove m different
physical edges of ONE physical star, e.g. (0,1),...,(0,m).
Because m<=a-2, this is a valid simple missing graph H with
all C(m,2) pairs mutually adjacent. Assign the remaining V
physical edges bijectively to the V ORIGINAL point factors.
The right ORIGINAL line map can simultaneously be independently
injected into the same E(K_a) alphabet. No GQ factor automorphism
is assumed and no SOURCE incidence edge positions are altered.

The identical inequality separately holds for the ORIGINAL right
line typed map g. This is a genuine universal all-h statement
about every possible globally correlated f,g, not an orbit mean.

A uniformly selected unordered pair of distinct ORIGINAL
point factor identities has physical adjacency probability at
most

    P_global <= 2 A_max / [V(V-1)].

It is an exact global image-capacity upper bound, attainable by
the deleted-star physical IMAGE construction.

## 3. Theorem Y2 — exact pairwise lifted-column feasible distribution

The much weaker rank-two lifts
  E[x_(p,e)*(1 - sum_{q!=p} x_(q,e'))]>=0
for every point p and physical edge labels e,e', are genuine
necessary constraints for any globally injective map.
For e'!=e, x_(p,e)*x_(p,e')=0. Thus they imply, for the
exchangeable two-original-site marginal,

    (V-1) P(x_(p,e)=1,x_(q,e')=1)
       <= P(x_(p,e)=1) = 1/K.

A physical pair e is adjacent to t=2(a-2) other K_a pair
edges, and disjoint from d=C(a-2,2) others. Construct an exact
symmetric two-original-site distribution with ONE-SITE uniform
physical pair marginals:

    J(e,e') = 0, if e=e'
              1/[K(V-1)], if e,e' are adjacent
              [V-1-t]/[K(V-1)d], if e,e' disjoint.

Because t+d=K-1, each fixed-e row sums to 1/K.
Symmetry implies every fixed-e' column sums to 1/K.
Every original pair is locally injective, and its probability
table is exactly normalized. For ANY e,e', the lifted column
capacity condition above holds, with equality on distinct
adjacent physical labels; for disjoint labels the joint is
<=1/[K(V-1)] using V<=K. No outside LP optimizer or floating
point assumptions are used.

Yet the expected NUMBER of adjacent original point pairs
under this constructed pair distribution is

    E_pair[A] = C(V,2)*K*t*1/[K(V-1)]
              = V(a-2).

Compare to the global upper A_max:

    E_pair[A] - A_max
      = m(a-2)-C(m,2).

This is STRICTLY POSITIVE when m>0 because m<=a-2.
Therefore the pair distribution **cannot be the two-site
marginals of ANY distribution on complete globally injective
ORIGINAL point maps**, even though it obeys the SPECIFIED
single-site marginals, local two-site injectivity and EVERY
selected lifted physical column capacity inequality.

Equivalently, its random original pair physical adjacency
probability is

    P_pair=2(a-2)/(V-1),

and the exact gap to global realizability is

    P_pair-P_global =
      2[m(a-2)-C(m,2)]/[V(V-1)] > 0  (m>0).

**Critical scope:** This is an integrality/extendibility gap for
a SPECIFIED limited pair-marginal plus column-lift system.
It is NOT claimed feasible for the complete Sherali-Adams
level-two formulation, for other lifted global inequalities,
for a full nonnegative original-GF5 factor system, or for
a full all-h hierarchy. A genuine globally valid quadratic
capacity cut has now been exhibited that separates it.

## 4. Direct finite independent falsification and reproducibility

For s=4, V=85,a=14,K=91,m=6:
  * Total adjacent unordered pairs in full K_14: 1092.
  * Sharp upper for any global 85-edge image: A_max=963.
  * Uniform original pair physical adjacency <=321/1190.
  * Pairwise lifted column-cut upper =2/7.
  * Pairwise-capacity-only gap =19/1190, corresponding to
    57 excess adjacent original point pairs.
  * The symmetric pseudopair gives E[A]=1020 >963.

When s=2, K=V and m=0, this particular gap is EXACTLY ZERO.
For each h>=1, the formulas use exact integers and Fractions;
m can vary with h and no asymptotic fit is assumed.

Evidence:
  * Real ORIGINAL W(3,2), W(3,4), W(3,8) geometry with
    |incidences|=V(s+1); full physically injective ORIGINAL
    point and line maps obtained by deleting missing spokes.
  * Independent O(V²) physical pair brute force (not merely
    the degree histogram used in the implementation), testing
    equality of every sharp constructed witness.
  * EXHAUSTIVE missing physical image enumeration:
    (a,m)=(5,3), (6,4), (7,5), exact every subset of missing
    physical pairs; compare sharp A_max with actual max.
  * For s=2/4, enumerate all K(K-1) ordered unequal
    physical pairs of two ORIGINAL factor labels and check
    exact full two-site normalization and each lifted column
    inequality (including equal physical pairs).
  * Verify all-h formulas at powers h=1..9, explicit
    counterchecks for noncanonical physical edge assignments,
    duplicate images, out-of-budget exhaustive enumeration.

## 5. Relation to ORIGINAL GF5 / decision for D6-Z

Theorem Y1 is valid for any ORIGINAL W(3,s) globally injective
pair maps and gives a sharp constraint on their physical
adjacency structure. It does NOT count the seven accepted GF5
positive ORIGINAL sixsets and does not imply a positive
universal lower bound on S_s. Many physical non-2-regular
sixset projections are NOT common stars; bounding physical
adjacency is not equivalent to counting GF5-positive classes.

Nevertheless Y2 proves that simply repairing D6-X with the
previously identified *selected* degree-two lifted physical
column capacity constraints is **NOT ENOUGH** for global
realizability of pair marginals when m>0. The new sharp
quadratic image adjacency inequality supplies an explicit
further global coupling gate, strictly stronger than the
selected lifts in a finite exact model.

**D6-Z proposed:** Incorporate the exact quadratic-image cut
with the full ORIGINAL sixset position-aware positive-class
factors and globally lifted assignment constraints. Determine
if a sparse geometry-dependent nonnegative sum-of-constraints
certificate can force positive S_s for ALL correlated f,g,
or isolate another exact pseudo-falsifier. Do not presume
pairwise image adjacency forces any one GF5 sixset positive.
Branch A/B OPEN, no full R3 upper, no ASET exponent.
