# HYP-105 / issue #230 — D6-W: overlap-consistent typed separator dual

**2026-10-13. RESTRICTED_THEOREM_C. Branch A/B remain OPEN.**
Strict Draft child of D6-V [PR #421](https://github.com/definitely-stable/Mathlab/pull/421),
base exact HEAD \`0c1023894ba239ed1c53d5c84356d8e9f839b8a9\`.
No merges, no \`main\` changes, no closure of #230/#176/#169.

## 1. Mathematical target beyond independent cluster minima

D6-U proved every individual ORIGINAL sixset proper-scope conditional
MINIMUM zero. D6-V proved even the true JOINT minimum of a cluster
of at most floor((a-1)/6) ORIGINAL sixsets is zero under arbitrary
complete f,g. Neither stops a nonseparable lower bound that uses
consistent overlap information **across all factors simultaneously**.

D6-W implements a transparent and independently checkable
**dual reparameterization over shared typed separators**. This
corresponds to a feasible dual of a local-consistency marginal LP,
but no assertion is made that our messages optimize that LP or that
fixed-rank Sherali--Adams proves the ORIGINAL global conjecture.

## 2. Theorem W1 — all-finite-h signed separator cost-shift certificate

For all h>=1, s=2^h, and arbitrary correlated globally injective
physical pair maps f and g of ORIGINAL W(3,s), take a finite collection
of ORIGINAL incidence-position-aware nonnegative factors F_Q. Each
factor has an EXACT COMPLETE local truth table over every locally
injective assignment of its ORIGINAL point/line factor scope to the
designated separate typed K_a alphabets. Classwise S_7 or the frozen
nonnegative selected GF5 numerator may be used; they are not total R3.

Let S be a **typed** ORIGINAL separator subset of a factor scope,
e.g. (('L',p),('R',l)), with 0<=|S|<=2 and signed integer message
\`theta_(Q,S)(eta_S)\`, defined for EVERY locally injective image
assignment of S (separately on left and right). The exact conservation
constraint is

    for EVERY (S,eta_S):
      sum_{Q containing S} theta_(Q,S)(eta_S) = 0.

Define G_Q(phi_Q)=F_Q(phi_Q)+sum_{S subset scope Q}
theta_(Q,S)(phi_Q|S). The G_Q may be NEGATIVE. For every complete
globally injective f,g, all message contributions cancel
pointwise, without assuming probabilistic independence, so

    sum_Q F_Q(f,g) = sum_Q G_Q(f,g)
                   >= sum_Q min_{locally injective phi_Q} G_Q(phi_Q).

Every individual minimum is EXACTLY enumerated. This is an
**all-h sound sufficient lower certificate** if a complete source
factor collection and truthful tables/messages are supplied.

The implementation refuses incomplete original local truth tables,
repeated or noncanonical typed sites, bool/noninteger costs,
missing/illegal separator keys, unbalanced message sums, and
unaffordable enumeration budgets. It does NOT generate full all-h
source sixset truth tables, cannot claim a positive root bound
by itself, and is NOT an optimized generic SA/SOS solver.

## 3. Genuine rank-one local marginal consistency gap

On exactly three original right sites assigned BIJECTIVELY to three
physical edges, every full assignment is one of the 3!=6
permutations. Take two nonnegative genuine-order-3 synthetic factors
charging complementary permutation parity, so their SUM is exactly
one on ALL six assignments. Each factor independently has minimum
zero. Assign each factor the uniform distribution on its three
zero-cost permutations. Both distributions have exactly the SAME
ONE-SITE marginals: probability 1/3 at every physical image.
Thus they satisfy one-site overlap consistency with expectation ZERO.
They disagree on every pair marginal. Therefore rank-one
consistency cannot certify the true positive objective in general.

This is a precise finite counterexample to treating one-site
marginal consistency as equivalent to global shared assignments.
It does NOT imply the ORIGINAL GQ root fails at rank one, nor
claim an all-h SA integrality gap.

## 4. Theorem W2 — exact paired-separator transfer on a SATURATED triple

Fix a left map f, all but three right ORIGINAL factors, and EXACTLY
three occupied physical right pair edges E=(e0,e1,e2) on the remaining
three ORIGINAL lines T=(t0,t1,t2). The legal right assignments to T
are all 3! bijections T->E. **Because the alphabet is saturated**,
the labels on t0 and t1 uniquely determine that on t2; a pair of
original site images (two-site separator) separates ALL six states.

Take a complete family of exact local cylinder factors F_c on
U_c subset T, with all ORIGINAL incidence-position metadata already
compiled (D6-T). Introduce an explicit ZERO-COST ANCHOR factor on
the FULL three-site scope T with complete six-row truth table.
For each factor F_c, choose separator
S_c=U_c if |U_c|<=2, or S_c=(t0,t1) if |U_c|=3.
Define h_c on S_c by its unique locally extendible cost table; for
|U_c|=3 the unique third image is inferred from the two-site pair.
Transfer messages -h_c on factor c and +h_c on the anchor.
Every separator function cancels exactly. After transfer,
EVERY original factor has shifted value identically ZERO; the
anchor equals the ENTIRE original cost for each of six complete
right assignments. Hence the W1 dual lower certificate is EXACT
for this **conditioned six-state suborbit**, unweighted and weighted.

This is an exact finite reparameterization, not a generic
rank-two Sherali-Adams theorem: a FULL THREE-SITE ANCHOR region
has been added explicitly, the physical image alphabet is saturated
(3 sites/3 labels), and the remaining 12 right sites plus ALL
15 left sites are FROZEN. None of those facts holds for the
unrestricted s=2^h root with K_a>=V_s and two moving typed maps.

## 5. True ORIGINAL W32 frozen-map independent controls

Source is the D6-T EXACT complete seven-positive cylinder partition
of all 62,370 ORIGINAL left-selected six-incidence candidates.
The cylinder classifier retains positions, D6 column alignment,
B/B overlap/disjoint, directional classes, and original site identity.
For S68, T=(3,11,12); for S72, T=(1,7,9). Original right IDs are
renumbered ONLY in the tiny certificate solver, not in source,
GF5 classifier, or true incidence geometry. Both physical pair
injections remain complete for every evaluated permutation.

For each row below, certificate = exact six-permutation primal min,
and the prior D6-V cluster-of-up-to-three-factors lower is preserved
as a separately recomputed control:

| Scheme / metric | D6-V <=3 cluster bound | D6-W paired dual | Exact conditioned primal | Improvement |
|---|---:|---:|---:|---:|
| S68 seven-S | 68 | 68 | 68 | 0 |
| S72 seven-S | 67 | 68 | 68 | +1 |
| S68 selected GF5 numerator | 3,112,510 | 3,112,510 | 3,112,510 | 0 |
| S72 selected GF5 numerator | 3,056,200 | 3,104,080 | 3,104,080 | +47,880 |

Independent checks: all six full right permutations preserve
pointwise original-vs-reparameterized totals; every separator
cancels on every locally injective typed image; true ORIGINAL
\`seven_census\` verifies the fixed baseline; D6-T original
cylinder compilation validates the 62,370 source sixsets; true
S68/S72 full six-state optimizers are reproduced; a synthetic
two-sided mixed point-line dual verifies typed separators.

## 6. What this achieves and what it does NOT

Achieved: a genuinely OVERLAP-COUPLED certificate, not a sum of
independent unconditioned block minima, with a mathematically sound
all-h conditional interface and a fully CLOSED finite conditioned
W32 right-three-line test for both objectives.

Not achieved: a nonzero universal inf_(f,g) S_s/s^6, an infinite
correlated counterexample, a complete R3 upper, an ASET exponent,
or any full all-h root truth-table enumeration. A three-site
SATURATED anchor is not an acceptable substitute for the entire
two-sided K_a-injection problem.

**D6-X gate:** Develop a checkable sparse/global ORIGINAL hyperfactor
cover and nontrivial separator messages without freezing f/g,
using geometry-specific aggregate inequalities that survive the
D6-V star obstruction. Do not grow finite right-permutation orbits
indefinitely; a uniform positive constant c independent of h is
needed for Branch A, or a coherent all-h family with S=o(s^6)
for Branch B.

Independent mathematical review remains open; do not merge until
dedicated, INDEX, Proof Audit, full Research all pass exact PR HEAD.
