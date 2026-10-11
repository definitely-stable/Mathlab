# HYP-105 E1-K3-A/B — endpoint-local path collisions and the book obstruction

Date: 2026-10-11. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Scientific parent [PR #366](https://github.com/definitely-stable/Mathlab/pull/366), exact base HEAD 0b21fd51187268e0ffbc3cb19335277103b4e80f.

**STATUS: RESTRICTED_THEOREM_C_LOCAL_IDENTITY / OPEN_WITH_FORMAL_BLOCKER.**
This note establishes an exact local identity for every simple graph and
a separate star-incidence contraction for genuine W(3,s) Kikuchi graphs.
It does NOT prove all-h positivity, D2* book control, Branch A/B, the
seven-family obstruction or a new ASET exponent. All tests are falsifiers,
not replacements for a mathematical proof.

## 1. Problem

In K1/K2, the ordered three-edge-path count P(u,v) satisfies

    sum_{u != v} P(u,v)^2 = P3 + 12*C6 + Theta.

The global Cauchy-Schwarz floor loses to Theta in adversarial four-cycle
books. Restricting Cauchy-Schwarz to endpoint pairs with small codegree
c(u,v) sounds promising, but it is false as a general collision-control
principle: the shared vertices lie INSIDE the paths, not necessarily in
N(u) intersect N(v).

## 2. The K3-A exact all-graph theorem

For every ordered distinct endpoint pair (u,v), let H_uv be the set of
simple directed 3-paths u-b-c-v. Put p_uv = |H_uv|, and define:

* k_z(u,v) = #{(b,c) in H_uv : z in {b,c}}, the internal-vertex load.
* b_uv = number of unordered edges {b,c} for which BOTH ordered paths
  u-b-c-v and u-c-b-v occur.

Let theta_uv count **ordered distinct** pairs of paths in H_uv that share
at least one internal vertex, and d_uv those with disjoint internal
vertex sets. Then for every finite simple undirected graph:

    theta_uv^(two internal vertices) = 2*b_uv,
    theta_uv^(exactly one)         = sum_z k_z(k_z-1) - 4*b_uv,
    theta_uv                      = sum_z k_z(k_z-1) - 2*b_uv,
    d_uv                          = p_uv*(p_uv-1) - theta_uv.

Proof: sum_z k_z(k_z-1) counts each ordered distinct pair of paths
once for EACH shared internal vertex. Every ordered pair of paths with
both internal vertices shared consists of the two possible orientations
of the same central edge, giving exactly 2*b_uv such ordered pairs.
These pairs are double-counted, so subtract 2*b_uv to count the union.
No other pair of distinct simple 3-paths with fixed ordered endpoints
can have two common internal vertices.

For ANY nonempty set U of ordered distinct endpoints, define

    M_U = sum_(u,v in U) p_uv,
    Theta_U = sum_(u,v in U) theta_uv,
    D_U = sum_(u,v in U) d_uv.

The K3-A LOCALIZED CERTIFICATE is:

    D_U = sum_U p_uv^2 - M_U - Theta_U
        >= M_U^2/|U| - M_U - Theta_U,
    12*C6 >= D_U.

The last inequality follows because each oriented pair of internally
vertex-disjoint 3-paths defines a simple six-cycle. Every such cycle
accounts for exactly twelve ordered pairs over ALL endpoint pairs;
restricting endpoints to U can only discard contributions.

This remains a deterministic theorem when U is chosen AFTER observing
the graph. For U empty the implementation returns only the trivial
lower bound zero, without applying Cauchy-Schwarz to a zero denominator.

The K3 fast counter uses internal-vertex loads and unordered-central-edge
orientation masks, not quadratic pairs of paths. An INDEPENDENT test
oracle explicitly compares every ordered pair of 3-paths and sorts by
the number of shared internal vertices.

## 3. Exact book obstruction — endpoint codegree is insufficient

Let G = K_{2,t}, t>=3, with hubs on the size-two side. It contains
no simple six-cycle. Every nonzero 3-path endpoint pair joins a hub
and a leaf, and c(u,v)=|N(u) intersect N(v)|=0 for all these pairs.

Direct counting gives:

    P3               = 4*t*(t-1),
    sum_(u,v) P(u,v)^2 = 4*t*(t-1)^2,
    Theta            = 4*t*(t-1)*(t-2),
    C6               = 0.

Thus the endpoint-codegree-zero filter RETAINS ALL 3-paths and ALL
of Theta. It cannot turn the K1 conditional bound into a universal
C6 theorem. This falsifies that candidate all-graph D2* lemma, not
the actual W(3,s) constrained theorem: arbitrary K_{2,t} need not
be a valid entire Kikuchi graph of a globally injective GQ labeling.

The internal-load selector does exclude some such pairs, but its loss
of M_U must be charged. The report always includes BOTH retained mass
and remaining Theta, as well as the exact six-cycle certificate.

## 4. K3-B original incidence tensor and future geometric D2*

Let F_{xz} be the unique ORIGINAL GQ point assigned to physical pair
{x,z}, if any; G_{yt} the unique ORIGINAL GQ line assigned to {y,t},
if any. Write I(p,l)=1 for genuine incidence and zero if a pair is
unassigned. For a Kikuchi vertex w=(x,y), define n(x,y):

    n(x,y) = sum_(z != x, t != y) I(F_{xz},G_{yt}).

This is exactly deg_Ghat(x,y), counting the incidences in the
intersection of the physical point star X_x and physical line star Y_y.
For distinct u=(x,y), v=(x',y'):

    codeg_Ghat(u,v) =
      sum_(z not in {x,x'}, t not in {y,y'})
         I(F_{xz},G_{yt})*I(F_{x'z},G_{y't}).

If x=x' or y=y', the excluded sets remain sets, so this formula
also covers those degenerate coordinate relations. It requires ONE
coherent pair of full injective labelings, never independent
per-motif choices.

The implementation reconstructs these values from ORIGINAL
incidences and compares them with the graph adjacency degrees and
common neighborhoods; the contraction does not use Kikuchi graph
adjacency, permitting independent falsification.

These identities supply explicit input to future book packing.
They DO NOT bound the sum of high codegrees or Theta for arbitrary
physical labels.

## 5. Falsification matrix and budget

* K_{2,t}, t=2/3/5/8/10: closed-form book formulas and the codegree-zero
  counterexample.
* 24 deterministic random dense/sparse graphs, order 5..8: independently
  enumerate pairs of directed 3-paths and verify each exact endpoint
  collision partition, all-graph K2 identity and all selected inequalities.
* True W(3,2) lex/reverse-line and W(3,4) seeded random coherent global
  labels: check sum_U d_uv = 12*C6 via the independent K1 six-cycle
  census and independently compute the original star tensors.
* Fail-closed malformed graphs, invalid selectors, endpoint/path budgets,
  empty endpoint subset, and empty graph.
* Separate dedicated GitHub-hosted stdlib-only K3 contract. No new full
  Research matrix, no npm/numpy requirement and no claimed s=8
  exhaustive CI result; s=8 exceeds the explicit default pair budget.

Selectors: ALL ordered distinct pairs, only ACTIVE pairs p_uv>0,
ACTIVE pairs with endpoint-codegree <= threshold, and ACTIVE pairs
with max internal path load <= threshold. The certificate contains
selected P3, selected Theta, both collision types, exact selected
internally disjoint count, retained P3 ratio and rational CS floor.
All units are original ordered path/cycle multiplicities.

## 6. Relation to K2, R3 and issue #230

Theorem K' of #366 is still:

    51^6 R3 >= (5643/4)*[(L(P3)-Theta)/12 - C6_rep].

By substituting the local K3-A certificate for the total C6 floor
one obtains a separate pointwise conditional estimate of the FULL
R3 risk using only the distinct-column six-cycles. It remains necessary
to subtract C6_rep, and the resulting floor may be zero.

Do not conflate this with proving Omega(s^6) for the accepted
seven-family sum S, which requires a proper-cycle or seven-motif
bound rather than unrestricted full R3. The small W32 instances may
also be handled separately by exact cylinder proof trees; neither
localization nor a W32 observation supplies an all-h constant.

## 7. Next slice: D2* structural book dichotomy

To progress toward all-h, a NEW all-h inequality must exploit the
GQ incidence tensor above. Candidate fork:

* Either Theta_U is small enough and enough path mass survives the
  localization for a positive Omega(s^6) six-cycle contribution;
* Or excess book mass can be converted into distinct-column Kikuchi
  six-cycles (and ideally proper D6 or accepted seven motifs) with
  an explicit multiplicity cap and rigorous control of forbidden
  repeated-column cycles.

The K_{2,t} obstruction shows this CANNOT be stated for all arbitrary
simple graphs without additional geometric hypotheses. Next work:
classify common-central-edge/c4 intersection types, give exact injection
maps and finite falsifiers, then attempt a W(3,s)-specific packing
lemma valid for ALL global f,g. Do not assume a positive constant
based on optimizing finite models.

**Acceptance:** dedicated exact-HEAD Contract SUCCESS, inherited Research
SUCCESS, code/documentation review, and post-merge main Research if merged.
Until a valid all-h book-packing theorem is proved: RESTRICTED_THEOREM_C /
OPEN_WITH_FORMAL_BLOCKER. Keep #230, #176 and #169 open.
