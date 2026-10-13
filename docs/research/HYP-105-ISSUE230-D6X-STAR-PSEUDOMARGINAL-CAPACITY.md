# HYP-105 / issue #230 — D6-X: projective local-star pseudomarginals and lifted occupancy-cut falsifier

**2026-10-13. New ALL-h restricted theorem C / formal model-specific
NO-GO. Branch A and Branch B OPEN.** Draft stacked on D6-W [PR #422],
pinned base HEAD \`fcb2556afd6045c95e5959105296d3a025bd2f3b\`
(all four GitHub-hosted parent CI SUCCESS). No main changes, merges
or closure of issues #230/#176/#169.

## 1. Why overlap consistency alone still cannot prove the root

D6-T/U showed independent single-factor proper-scope conditional
minimum proofs vanish. D6-V showed even unconditioned min of any
bounded cluster of true ORIGINAL sixsets vanishes. D6-W introduced
nonseparable signed typed overlap-separator potentials and a genuine
**conditioned** finite W32 exact six-state certificate, but required
a **full-three-site anchor** and frozen f/12 right factors.

The next question is whether overlap-consistent local distributions
that simultaneously zero every original Q could exist WITHOUT
extending to globally injective assignments. D6-X answers YES, even
with projective consistency across scope ranks increasing as
a_s-1=Theta(s^(3/2)). More importantly, it pinpoints a **degree-two
lifted physical-column capacity inequality** that EXCLUDES the
constructed pseudo-solution. Do NOT misdescribe this as an SA
integrality gap or an impossibility for generic SA.

## 2. Theorem X1 — all-h projective local-star zero pseudomarginals

Take s=2^h,h>=2, V=(s+1)(s²+1), and
a=min{a:binom(a,2)>=V}. Then a>=14, a-1>=13.
The ORIGINAL W(3,s) GQ has V ORIGINAL typed points, V ORIGINAL typed
lines, and degree s+1. Each ORIGINAL distinct-six-incidence Q has
at most six ORIGINAL point and at most six ORIGINAL line factors,
so total scope r_Q<=12<=a-1; repeated ORIGINAL incidence positions
are *retained*, including the B/B-overlap and D6 classes.

For EVERY set U of at most a-1 distinct ORIGINAL typed factor
vertices (with separate point/line namespaces) define a probability
measure mu_U on physical pair labels:

1. Pick a uniformly random center c in [a].
2. For the point factors of U assign **different** spokes
   {c,j},j!=c, by a uniform ordered injection of their factor IDs
   into the a-1 spokes of that star.
3. Independently assign the line factors of U by uniform injection
   into K=binom(a,2) physical pairs, with no restriction on
   physical overlap between different TYPES.

Each mu_U is supported on locally injective assignments within each
type. Projecting mu_U to U' subset U gives **EXACTLY mu_U'** because
uniform ordered injections are projectively consistent under
forgetting factors, and the center distribution remains uniform.
This holds for arbitrary overlapping regions up to a-1 ORIGINAL
typed variables (and, separately, larger right-only ranks are
possible but not claimed).

Take ANY original Q, and project mu_scope(Q). On its left physical
projection coordinate c occurs SIX times across the six ORIGINAL
incidence positions, even when a point original factor repeats.
Every one of the seven previously accepted strictly positive
six-coordinate GF(5) classes requires **six physical coordinates of
degree exactly TWO** on BOTH sides. Therefore the accepted
chi_Q=0 with mu_Q-probability one, and its selected nonnegative
class-specific GF5 necessary numerator has expectation zero.

Thus all Q simultaneously admit locally consistent zero-cost
marginals, including all seven classes, at region rank up to a-1.
**This is NOT one globally realized map f,g and NOT Branch B.**

### Closed exact local distribution

For distinct assigned ordered physical point edges e_1,...,e_k,
k<=a-1, the probability of that ordered assignment under mu is

    #{c in intersection of endpoint sets e_i}
       / [a * (a-1)_k],

with (n)_k=n(n-1)...(n-k+1). Repeated pairs have probability zero.
For k=0 it equals 1. Right typed edges have probability 1/(K)_r
when distinct, independently. Exact integer/Fraction oracles
check all these identities without floating-point sampling.

## 3. Theorem X2 — exact degree-two column occupancy-cut falsifier

For any **genuine global injection** of ORIGINAL points f into
E(K_a), define zero-one x_{p,e} indicating f(p)=e. For every
physical pair e', its column capacity is

    sum_{q=1}^{V} x_{q,e'} <= 1.

Fix a DIFFERENT adjacent physical pair e (sharing exactly one
physical coordinate with e'), and ORIGINAL point p. The
following **degree-two lifted capacity inequality** holds
POINTWISE for every actual complete f:

    x_{p,e} (1 - sum_{q != p} x_{q,e'}) >= 0.

Under the explicit local-star distribution:

    E x_{p,e} = 2 / [a(a-1)] = 1/K,
    E x_{p,e} x_{q,e'} = 1/[a(a-1)(a-2)]
                      for p!=q, e∩e' one coordinate.

Consequently

    E[sum_{q!=p} x_{q,e'} | x_{p,e}=1]
      = (V-1) / [2(a-2)].

For the minimal a, since V > C(a-1,2),

    V-1 >= C(a-1,2) = (a-1)(a-2)/2
        > 2(a-2)   for a>=6,

so the conditional expected occupancy is **STRICTLY GREATER THAN 1**.
Hence the valid lifted inequality has expectation

    E[x_{p,e}(1-sum_{q!=p}x_{q,e'})]
       = 2/[a(a-1)] - (V-1)/[a(a-1)(a-2)] < 0.

This explicitly REFUTES feasibility of these zero-cost projective
star marginals under a standard assignment encoding containing
column capacity constraints lifted by x_{p,e}. The **unlifted**
column inequality alone DOES hold in expectation, since V/K<=1.

**Crucial caution:** this falsification shows the star solution is
NOT a feasible standard Sherali--Adams pseudoexpectation for the
complete assignment formulation at level two. It neither proves
nor disproves existence of OTHER feasible SA pseudo-solutions of
zero GF5 cost. It does NOT show fixed-rank SA is insufficient,
nor prove positive GF5 obstruction for all f,g.

## 4. Independent true-ORIGINAL finite falsification

The hosted verifier checks full original W(3,4) (V=85, a=14,
425 incidences) and W(3,8) (V=585,a=35,5265 incidences).
Six DISTINCT true ORIGINAL incidences include examples with six
distinct point factors and ones with repeated points.
Every locally star-labelled Q gives degree exactly SIX at
the center and no accepted seven-GF5-positive class can occur.
These are TRUE ORIGINAL factor incidences, not synthetic six cycles,
and this statement is only a local pseudo-oracle check.

Separately enumerate EVERY star center/ordered spoke assignment
on 4 point sites for a=7 and 3 for a=14; verify full exact
projection of the higher-scope distribution onto every proper
subset, and independently count all a(a-1)(a-2) two-site
assignments at a=6/7/14. Compare to exact rational formulas.
Check original all-h physical minimal a for s=2,4,...,256.

### Exact smallest h>=2 control

For s=4, (a,V,K)=(14,85,91). For distinct adjacent physical
edges (e,e'):

    E[x_p,e]=1/91,
    E[x_p,e x_q,e']=1/2184,
    E[sum_{q!=p}x_q,e' | x_p,e=1] = 7/2,
    lifted inequality expectation = -5/182.

Thus the projective pseudo satisfies E(sum_p x_p,e')=85/91<=1
but violates the VALID lifted capacity cut, whose conditional
right-hand side is 1.

## 5. Scientific interpretation and D6-Y gate

An enormous collection of mutually consistent finite-dimensional
zero-cost local marginal distributions can be globally impossible,
even while every local six-incidence condition and all ordinary
one-column capacity expectations pass. The exact missing constraint
is NOT another individual sixset condition; it is the interaction
of physical COLUMN CAPACITY with an assignment conditioned on
another physical edge.

Next research: combine full ORIGINAL factor distributions with
**lifted global assignment constraints** (both typed physical
alphabets), not only overlap-consistent pair separators. Implement
a mathematically valid sparse restricted primal/dual relaxation,
and independently test whether occupancy-lift inequalities alone
force positive GF5 contribution or whether a different zero-cost
pseudodistribution survives. Do not extrapolate finite W32/W34
data or promise an all-h positive constant until proved.

**Outcome: RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.**
Original universal Branch A and infinite Branch B remain OPEN.
No R3 upper, ASET exponent, or full all-h positive certificate.
