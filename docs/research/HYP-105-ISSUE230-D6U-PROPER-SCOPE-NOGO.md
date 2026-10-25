# HYP-105 / #230 — D6-U: exact proper-scope projection-minimum NO-GO

**2026-10-13. RESTRICTED_THEOREM_C, stronger proof-method NO-GO.** Strict
Draft stack on D6-T [PR #419](https://github.com/definitely-stable/Mathlab/pull/419)
at HEAD `126fb06d1c4d775bb241a7b3447df36299a38d34`. No main edits,
no merge. Branches A/B and #230/#176/#169 remain OPEN.

## Scope and crucial distinction

D6-T proved that its unconditional **one-site** conditional minima for each
nonnegative seven-GF5-positive ORIGINAL sixset factor vanish. Here the
barrier is strengthened to **every proper local subset**, in particular
every conditioned joint subset of at most SIX ORIGINAL typed factors.

This does **not** show that Sherali–Adams level 6, local-marginal
consistency, generic SOS/SDP, geometric cycle constraints, or any other
stronger global relaxation has value zero. Those constructions do not
necessarily reduce to individual-factor conditional minima.

## Theorem U1 (free-site completion, ALL a>=6)

Let `t=(t_1,...,t_6)` be any six ORIGINAL factor positions on one
physical side; repetitions of the same ORIGINAL factor are retained.
For any injectively prelabelled proper subset of its distinct factors
by edges of K_a, a>=6, there exists an injective completion for which
the six **position-wise** physical pair edges are **not** 2-regular on
exactly six coordinates.

**Proof.** First choose injectively, without constraints, all remaining
free factor labels except ONE free factor `v`. At most five other
ORIGINAL factors are now assigned, consuming at most five distinct pair
edges. Let `k` be the multiplicity of v among the six positions.

* `k>=3`: any edge chosen for v puts degree >=3 on both endpoints.
* `k=2`: the four remaining positions have at least one used physical
  coordinate u. Of the a-1 >=5 edges incident with u, at most FOUR
  are already used: only four incidence positions other than v can
  contribute an occupied incident edge. Choose an unused (u,w).
  Then u has degree at least 1+2=3.
* `k=1`: five fixed incidences have degree sum 10. To complete exactly
  six physical coordinates each of degree 2, the final edge must join
  the UNIQUE two coordinates of fixed degree 1; all others must already
  have degree 2 or 0. Consequently at most ONE pair label can yield a
  valid projection. At least K_a-5 >=10 pair labels remain available;
  choose any other available pair.

All cases give a locally injective bad physical projection. QED.

The constructive implementation deterministically chooses the final
free factor, checks the candidate edge(s), preserves every prescribed
physical label, and fails closed if the condition is not met. The
algorithm never relies on a probability or independence assumption.

## Theorem U2 (ORIGINAL GQ six-incidence forest, ALL s=2^h)

Let Q be SIX DISTINCT ORIGINAL point-line incidences in W(3,s) for
s=2^h, h>=1. Since this generalized quadrangle's bipartite incidence
graph has girth 8, a six-edge subgraph contains no cycle; it is a
FOREST. Therefore the union of ORIGINAL typed point and line endpoints
of Q has cardinality `r_Q>=6+1=7`. The left/right typed namespaces
remain separate even if integer IDs happen to coincide.

Fix injectively ANY PROPER subset `T` of these `r_Q` ORIGINAL typed
factors, on their own respective K_a physical pair alphabets. A free
ORIGINAL factor exists on at least one typed side. By U1, choose the
remaining physical labels on that side so its six physical incidence
columns are NOT six-coordinate 2-regular. Complete the other typed
side injectively arbitrarily. Every accepted seven-GF5-positive class
requires 2-regularity on BOTH physical sides; hence this completion
has `chi_Q=0` and the nonnegative selected GF5 numerator is also 0.

The complete ORIGINAL GQ has V=(s+1)(s²+1) factors on each side, and
a=min{a: C(a,2)>=V}, so every local injection extends to a complete
ORIGINAL globally injective map on its own side. In particular,
the completion is globally admissible for the chosen Q (without
asserting that other ORIGINAL sixsets vanish simultaneously).

**Exact consequence:** for every h>=1, every Q, every proper subset
T of its ORIGINAL factor scope, and every injective pinned assignment
`eta_T`,

`min_{phi locally injective, phi|T=eta_T} chi_Q(phi)=0`

and the same holds for the selected nonnegative GF5 coefficient.
Every conditional minimum for |T|<=6 therefore vanishes (because
r_Q>=7); indeed every **proper-scope** minimum vanishes, even when
r_Q>7 and |T|>6.

## Corollary U3: a precise certificate family is identically zero

Any nonnegative local-factor lower-certificate pipeline whose ONLY
usable per-Q evidence consists of (a) unconditional minima and
(b) proper-scope conditional minima, subsequently aggregated as
nonnegative potentials or via global injective assignment, receives
only zero local-minimum information on the unconditioned ORIGINAL root
problem. Such a pipeline CANNOT infer a positive Omega(s^6) bound
from these minima alone. Even six-way joint pins do not fix it.

This corollary **does not cover** cross-factor overlap consistency,
nonseparable dual constraints, conditional expectations rather than
conditional minima, inequalities involving sums of overlapping Q's,
or full-scope penalties. In particular it is NOT a blanket
Sherali–Adams / Lasserre / SOS lower-bound impossibility theorem.

## Independent falsifiers, finite only

* Exhaustive Bell(6)=203 ORIGINAL endpoint multiplicity patterns,
  with locally injective adversarial prefix/suffix pins for every
  proper cardinality, a=6/14/35; degree multisets checked by a separate
  implementation rather than trusting the witness's boolean.
* Independent 30-vertex/45-incidence original W(3,2) bipartite
  short-cycle DFS (no 4- or 6-cycles).
* True W32 selected ORIGINAL sixsets of physical left types A/B/C
  and at least one genuinely **positive** accepted seven-GF5 class in
  each S68 and S72 model. Preserve original incidence positions.
  For arbitrary pinned actual labels up to SIX ORIGINAL typed sites,
  construct full local injections with zero positive GF5 contribution,
  even when the original complete assignment contributed positively.
* Explicit rejection of fully pinned scopes, duplicated physical pair
  labels, noncanonical edges, repeated ORIGINAL incidence IDs, and a
  six-edge synthetic cycle falsely presented as an ORIGINAL GQ forest.

No 62,370-row re-enumeration claim for all conditional pin patterns;
the theorem is all-h mathematical and the W32 experiments are only
independent spot/falsification controls, not asymptotic evidence.

## Next action and acceptance

The next admissible step is to search for a **coupled cross-Q**
inequality with a genuine overlap/correlation constraint (e.g. local
pseudo-distributions consistent over shared ORIGINAL sites), or an
explicit all-h geometry argument whose positive certificate cannot
be factored through individual-Q proper-scope minimum tables. Require
exact original incidence-position retention, all seven accepted
GF5 classes, both globally injective label families, and independent
falsification. PROVED_A/COUNTEREXAMPLE_B are NOT claimed.
