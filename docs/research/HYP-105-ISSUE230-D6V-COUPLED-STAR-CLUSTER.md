# HYP-105 / issue #230 — D6-V: star obstruction to bounded joint-cluster minima

**2026-10-13: RESTRICTED_THEOREM_C plus exact globally extendible
finite controls; NOT PROVED_A or COUNTEREXAMPLE_B.** Strictly stacked on
D6-U Draft [#420](https://github.com/definitely-stable/Mathlab/pull/420);
base pinned HEAD \`c6c34e727a4b017880be7437afe4146b564f2e76\`.
No main mutation, no merge; #230/#176/#169 remain OPEN.

## Why D6-U is not enough

D6-U proved individual-Q proper-scope conditional minima vanish. Even
a sum of two individually zero-minimum factors need not have zero
minimum: the same ORIGINAL factor labels must work simultaneously.
D6-V analyzes unconditioned **joint MINIMA** of *clusters* of ORIGINAL
sixset factors, separating these from stronger overlap-consistent
pseudodistributions (e.g. full Sherali-Adams), which are NOT covered by
the NO-GO below. See Georgiou--Magen--Tulsiani (ECCC TR09-061) for the
importance of locally consistent distributions to SA integrality gaps.

## THEOREM V1 — exact all-h two-sided STAR ZERO

Fix s=2^h, h>=1, V=(s+1)(s²+1), a=min{a:C(a,2)>=V}.
Let C be ANY FINITE collection of six DISTINCT ORIGINAL GQ incidences
per factor Q. Define the typed vertex-support unions

    P(C)=union_{Q in C} {original POINT endpoints in Q},
    L(C)=union_{Q in C} {original LINE endpoints in Q}.

If EITHER |P(C)|<=a-1 OR |L(C)|<=a-1, then there exist **complete
globally injective** ORIGINAL assignments f,g of the V ORIGINAL points
and V ORIGINAL lines into separate copies of E(K_a) such that EVERY
Q in C has ZERO positive seven-GF5 contribution. The same statements
hold for the selected previously certified nonnegative class-specific
GF5 numerator.

PROOF. Suppose |P(C)|<=a-1. Injectively label these distinct ORIGINAL
point factors using different edges (0,1),...,(0,a-1) of K_a. On every
Q the physical point pair-edge appearing in EACH of its SIX ORIGINAL
incidence positions contains physical coordinate 0, including repeated
ORIGINAL factor vertices, so coordinate 0 has total degree EXACTLY SIX.
Every accepted seven-GF5-positive class requires a physical left
projection on exactly six coordinates ALL degree two. Thus NO Q in C
can contribute. Extend the partial assignment to all V ORIGINAL points
by unused physical K_a edges, possible because K=C(a,2)>=V. Assign
all ORIGINAL lines injectively in any order, independently from f:
the left projection alone already invalidates every Q. If instead
|L(C)|<=a-1, use the identical construction on the right. QED.

This does NOT require group invariance, random injection, independence,
loss of incidence position, or even the GQ girth property beyond
the definition of ORIGINAL six-incidence factors. It works for a
C chosen *adversarially* from the full ORIGINAL Q collection.

## COROLLARY V2 — unbounded necessary LOCAL cluster size

Every Q has at most six distinct ORIGINAL point vertices and six
distinct ORIGINAL line vertices. For every t=|C| with

    6t <= a-1,

both support unions have size at most a-1. Thus every such cluster
admits a globally injective assignment with all Q costs ZERO:

    min_{f,g} sum_{Q in C} chi_Q(f,g) = 0.

For selected nonnegative GF5 coefficients the same equality holds.
Therefore any individual-cluster-minimum-only proof that partitions
the unconditioned ALL-Q objective into blocks of at most
t=floor((a-1)/6) ORIGINAL sixsets has a provably ZERO lower bound.

As s -> infinity through powers of two,

    a=(sqrt(2)+o(1))s^(3/2),

so a local block must contain at least ceil(a/6)=Omega(s^(3/2))
sixsets before a **positive** unconditioned joint minimum is even
possible under this proof mechanism. The stated size is NECESSARY,
NOT SUFFICIENT; larger blocks can still have zero joint minimum.
For the special case of a single Q, D6-U additionally proves
the zero regardless of the threshold at s=2.

This result DOES NOT rule out SA at fixed level: overlapping local
pseudodistributions can enforce consistency across many clusters
without appealing to the independent minimum of each cluster. It
does NOT lower-bound the TRUE min S for arbitrary f,g.

## THEOREM V3 — sound EXACT coupled-cluster partition certificate

For nonnegative ORIGINAL factor truth tables with full locally
injective physical domains, partition their indices into disjoint
groups B_1,...,B_m (each group is a collection of **factors**, and the
variables in distinct groups may overlap). For each block compute

    b_B = min_{locally injective assignments to union scope}
                 sum_{Q in B} F_Q.

Then for every globally injective pair f,g,

    sum_Q F_Q(f,g) >= sum_B b_B.

Proof: every global pair restricts to an admissible union-scope
injection, so each block sum >=b_B; sum over blocks. The algorithm
checks every row in every original full table, rejects missing/extra
or non-integral/negative rows, enumerates injective union assignments,
and optimizes a **disjoint factor-block partition** via bitmask DP.
Increasing the maximum allowed number of factors in a block can only
increase the resulting bound. This is a valid but generally incomplete
packing dual; NOT generic SA, and not an all-h positive certificate.

## Exact finite actual ORIGINAL W32 experiment (S68 / S72)

Take the *complete, position-aware* 62,370 ORIGINAL left-selected
six-incidence candidates of D6-T, fix the true left f and 12 of 15
right original physical labels, and allow ALL six permutations of
the same three occupied right edges (T=(3,11,12) for S68 and
T=(1,7,9) for S72). Partition cylinders into <=8 exact ORIGINAL
right-support intersection groups U=R(Q)∩T. These 0..3-variable
tables are complete, independently validated by D6-T against the
seven-class ORIGINAL census and fixed weighted GF5 numerator.

Construct all singleton, pair and triple GROUP minima using
complete joint union-scope injections into three physical edges,
then optimize partitions. The resulting bounds are certified and
monotone, and cannot exceed the true minimum among all six complete
permutations. All claims are **conditional** on f and 12 original
right images being frozen. A synthetic exact third-order parity
frustration has two individual zero-minimum factors but paired
minimum=1; this proves that coupling is genuinely more expressive.

The numerical W32 pair/triple bounds are machine-produced, not
predeclared as a universal asymptotic theorem. Even a positive
W32 conditioned lower bound cannot be promoted to arbitrary
correlated f,g.

## Precise decision after D6-V

Unconditioned independent block minima of every FIXED number of
sixsets are identically zero for all sufficiently large h.
Consequently the only plausible next certificate class from this
route must be **nonlocal/global**: overlapping sixset-factor systems
with consistent marginals, or a structural incidence/geometry
inequality involving O(a) or more ORIGINAL support sites. A
full-scope nonzero block could solve finite instances but still
lacks a uniform all-h argument.

Fail-closed acceptance: no Branch A/B, no all-R3 upper, no ASET
exponent, no modified main. Require all exact-head CI checks and
independent mathematical review before merging.
