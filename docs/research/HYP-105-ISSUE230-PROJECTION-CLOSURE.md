# Uniform proper three-path theorem for coherent pair-label maps

**STATUS: RESTRICTED_THEOREM_C.** The original universal seven-family lower in [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains open. This document proves a new universal path-count theorem, reconstructs its exact ORIGINAL-incidence closure, and keeps the unproved compensation estimate separate. Companion to [the quartic source theorem](HYP-105-ISSUE230-QUARTIC-SOURCE.md).

This is an all-label theorem in the frozen model. It does not claim the
issue230 seven-family lower. No computational evidence enters the proof.

## Statement

Let s=2^h, V=(s+1)(s^2+1), Delta=s+1, and
a=min{b:binom(b,2)>=V}. For any globally injective pair-label maps f,g
on the point and line objects of W(3,s), form the rectangle-diagonal graph
H on [a] x [a]: the original incidence (p,l), whose labels are
f(p)={u,v}, g(l)={x,y}, gives the two undirected edges

    (u,x)--(v,y), (u,y)--(v,x).

There is a subgraph H' obtained by retaining BOTH diagonals of each
retained original incidence, such that the number of oriented three-edge
paths v0,v1,v2,v3 in H' satisfying the following conditions is at least

    (16-o(1))*s^6.

The four first coordinates are distinct; the four second coordinates are
distinct; the physical pair joining the endpoint first coordinates is
in f(P); and the physical pair joining the endpoint second coordinates
is in g(L). Every error term is uniform over f,g. Equivalently, for every
eta>0 there is h0(eta), independent of f,g, such that this count is at
least (16-eta)*s^6 for all h>=h0(eta).

H' has m'=(1-o(1))*2VDelta edges. The proof only needs regularity and
partial linearity on both sides, not the GQ projection axiom.

## Graph and block identities

The graph H is simple: one grid edge determines its unordered first-
coordinate pair, its unordered second-coordinate pair, and hence its
unique original incidence by injectivity. It has n=a^2 vertices and
m=2VDelta edges. As s tends to infinity,

    a=(sqrt(2)+o(1))*s^(3/2), n=(2+o(1))*s^3,
    m=(2+o(1))*s^4.

For a grid vertex (u,x) and prescribed first coordinate v, write
b((u,x),v) for its number of neighbors whose first coordinate is v.
If f^{-1}({u,v})=p exists, this is the number of original lines through
p whose g-label contains x. Otherwise the block is empty. Therefore

    sum_(u,x),v b((u,x),v)(b((u,x),v)-1)=4M_g
      <=4a binom(a-1,2),

where M_g counts unordered concurrent original line pairs whose physical
g-labels share a coordinate. Each physical intersecting edge pair has at
most one original concurrency point, by partial linearity. The factor
four is two orders of the line pair times two endpoints of f(p).
The column-block version gives the same bound with f and g exchanged.
Hence the sum for row and column blocks together is O(a^3).

For every fixed grid row u, its incident edge count is exactly
2Delta deg_f(u), at most 2Delta(a-1); the dual holds for grid columns.

## Coherent pruning

Let Fbar and Gbar be the missing-label graphs. Each has
t=binom(a,2)-V<a edges, by minimality of a. Set

    kappa=floor(s^(1/16)), L=s^(3/4), d_min=s^(31/32).

First remove all edges incident with a grid row whose Fbar degree exceeds
kappa, or a grid column whose Gbar degree exceeds kappa. Whenever an
edge is removed, remove its opposite diagonal too. There are fewer than
2a/kappa bad rows and fewer than 2a/kappa bad columns. The initial removed
edge count, including the possible factor two for coherent deletion, is
at most

    16Delta a(a-1)/kappa=O(s^(4-1/16))=o(m).

Next remove all edges in any row- or column-neighbor block of ORIGINAL H
having size >L, again deleting their opposite diagonals. For b>L,
b<=b(b-1)/(L-1). The block identities therefore show that this removes at
most

    16a binom(a-1,2)/(L-1)=O(s^(15/4))=o(m)

edges. All blocks in the remaining graph have size <=L.

Finally repeatedly remove a vertex of current degree <d_min, together
with all its incident edges and all their opposite diagonals. Charge
each initiating vertex at most 2d_min removed edges. Each vertex initiates
at most once, so this removes at most

    2a^2*d_min=O(s^(4-1/32))=o(m).

Delete isolated vertices. The result H' is coherent, has
m'=m(1-O(s^(-1/32))), n'<=a^2, minimum degree >=d_min, blocks <=L,
and every surviving first/second coordinate has missing degree <=kappa.
The constants in these bounds do not depend on the maps.

## Stationary-walk entropy

Let (X0,X1,X2,X3) be a stationary simple random walk on H'. Its vertex
stationary law is pi(v)=d(v)/(2m'). Its path entropy is exactly

    H(X0,X1,X2,X3)=log(2m')+2 sum_v pi(v)log d(v)
      >=log[2m'*(2m'/n')^2].

The inequality follows from convexity of x log x (or nonnegativity of
the relative entropy of pi against the uniform law on V(H')).

At any step and for any prescribed row or column, the conditional
probability that the next vertex belongs to it is at most L/d_min.
The first edge already has different first and second coordinates.
At step two forbid the initial row and column. At step three forbid the
first two rows and first two columns, together with at most kappa missing
closing neighbors of the initial row and at most kappa missing closing
neighbors of the initial column. The union bound gives

    p=P(path violates one of the four required conditions)
      <=(2kappa+6)L/d_min=O(s^(-5/32)).

Let E be the good event. The entire path support has at most n'^4
elements. The binary entropy decomposition gives

    H(path)=h(p)+(1-p)H(path|E)+p H(path|not E),
    H(path|not E)<=4log n'.

Consequently

    H(path|E)>=H(path)-O(p log n'+h(p))=H(path)-o(1).

For a discrete random variable, entropy is at most the logarithm of its
support size. Thus the NUMBER of good oriented paths is at least

    exp(H(path|E))
      >=(1-o(1))*2m'*(2m'/n')^2
      >=(1-o(1))*8m^3/a^4
      =(16-o(1))*s^6.

This completes the theorem.

## What it does and does not transfer to issue230

The three path edges have three DISTINCT original point endpoints and
three DISTINCT original line endpoints, since their physical labels form
simple P4s. Their endpoint pair labels determine original q and r.
When q is nonincident with r, the GQ axiom gives the unique original path

    q--l--p--r.

Its three anchor incidences plus the three grid-path incidences give an
accepted BB-overlap sixset provided f(p) is disjoint from all four used
first coordinates and g(l) from all four used second coordinates.
This also guarantees all six original incidences are distinct.
Each accepted sixset in this synchronized singleton-path subclass is
obtained from exactly TWO oriented grid paths, by global reversal. One
side's incidence-column order forces the orientation on the other side.

Equivalently the ORIGINAL point-line incidence matrix satisfies

    B B^T B = 2s B + J.

For a nonincident pair the cubic entry is one by the projection axiom.
For an incident pair its length-three walks are exactly the two types
with a repeated endpoint edge, giving 2Delta-1=2s+1. The executable
oracle independently counts all these original walks, including
backtracking, rather than inferring the identity from physical paths.

If q is incident with r, the grid path plus that incidence closes to a
proper synchronized C4, counted by Q4. If q is nonincident but one doubled
anchor label meets the four used coordinates, the candidate six-column
multiset has a physical coordinate of degree greater than two. It may
also repeat an original incidence. It is not an accepted sixset.
The theorem does NOT bound either of these two defect classes.

More precisely, the number I of incident-endpoint oriented paths is

    I=8 Q4_4(H')+2 Q4_3(H')<=8 Q4(f,g),

where Q4_j(H') counts original synchronized C4 foursets having exactly j
of their four original incidences retained. The closing original incidence
need not be retained, so Q4_3 contributes as well. A proper grid C4 is
uniquely determined by its original fourset. If all four incidences are
retained, it has four possible omitted closing edges and two traversal
orientations; if exactly three are retained, only that omitted edge is
possible, giving two orientations. In particular the
incident defect is o(s^6) whenever Q4(f,g)=o(s^6). This is a conditional
fact and does not control the anchor-blocked defect.

The unresolved lemma is a quantitative compensation estimate: from the
(16-o(1))*s^6 proper endpoint-complete paths, force c*s^6 unblocked
nonincident closures or c*s^6 original sixsets in the other selected
families, for one absolute positive c. Counting all ordinary grid C6s or
all leafless physical sixsets is not a substitute for this estimate.

## Concrete obstruction to a common auxiliary bound

A uniform O(s) bound on the maximum grid degree is false. For even h,
write s=t^2. The F_t-subgeometry W(3,t) embeds in W(3,t^2). Its V_t
points and V_t lines each fit in a single physical star because
V_t=(t+1)(t^2+1)=(1+o(1))*s^(3/2)<a-1. Map these original points to
distinct f-edges containing u and these original lines to distinct
g-edges containing x, then extend both maps by unused physical pairs.
The grid vertex (u,x) has degree at least V_t(t+1)=Theta(s^2).
Thus a C4-to-proper-C6 argument requiring max degree O(s) cannot be
used for arbitrary coherent maps without an additional regularization
argument. This construction is not a small-S counterexample.

## GQ spectral refinement of the physical pencil-block bound

Let B be the ORIGINAL V by V point-line incidence matrix of W(3,s),
where V=(s+1)(s^2+1), Delta=s+1. Its singular value on constants is
Delta, and its other singular values are sqrt(2s) or zero. Therefore
for any original line subset R,

    ||B 1_R||_2^2
      <=2s|R|+(Delta^2-2s)|R|^2/V
      =2s|R|+(s^2+1)|R|^2/V.                 (1)

For each physical coordinate y, let L_y be the set of original lines
whose g-label contains y, and let r_py=|L_y intersect N(p)|. Global
injectivity implies |L_y|<=a-1, and every original line belongs to exactly
two such stars. Thus

    sum_y |L_y|=2V,
    sum_y |L_y|^2<=2V(a-1).

Applying (1) and summing gives

    sum_(p,y) r_py^2<=4sV+2(s^2+1)(a-1),
    sum_(p,y) r_py=2VDelta.

Every concurrent pair of distinct original lines has a unique original
intersection point. Their distinct physical g-edges share at most one
physical coordinate. Consequently, if M_g is the number of concurrent
unordered original line pairs whose g-labels intersect, then exactly

    M_g=sum_(p,y) binom(r_py,2)
      <=(s-1)V+(s^2+1)(a-1)=:C_s=O(s^4).       (2)

This is uniform in g. The dual proof gives M_f<=C_s uniformly in f.
It improves the geometry-free O(a^3)=O(s^(9/2)) estimate by half a power.

In the rectangle-diagonal graph, the total row-neighbor block factorial
mass is 4M_g, and the total column-neighbor block factorial mass is 4M_f.
Thus their sum is at most 8C_s. If all original blocks larger than T>1
are removed, along with the opposite diagonal of every removed edge,
the total edge loss is at most

    16C_s/(T-1).                              (3)

In particular T=s^(1/10) loses O(s^(39/10))=o(m), where m=2VDelta.
The coherent stationary-walk proof may use this threshold in place of
s^(3/4). Keep kappa=floor(s^(1/16)) and d_min=s^(31/32). The probability
of a coordinate repeat or missing endpoint label is now at most

    (2kappa+6)T/d_min=O(s^(-129/160)),

since 1/16+1/10-31/32=-129/160. The same entropy proof therefore still
gives (16-o(1))*s^6 endpoint-complete proper oriented three-paths in a
coherent H' retaining (1-o(1))*m edges, now with block bound s^(1/10).

## Consequence for the independently reviewed incident-book inequality

For G the full rectangle-diagonal graph and H=H', the mixed-book lemma

    P_inc<=24T M2(G)+sqrt(192m z)

is valid, where z counts H' six-cycles with six distinct first coordinates
and six distinct second coordinates. The all-label bound
M2(G)<=258s^(11/2) yields

    24T M2(G)=O(s^(28/5))=o(s^6).

Hence if P_inc>=eta*s^6 for a fixed eta>0 and all sufficiently large s,
then

    z>=(eta^2+o(1))*s^12/(192m)=Omega_eta(s^8).

Every such proper cycle gives a unique D6 original six-incidence set;
conversely its physical column-dual synchronization determines its grid
cycle. Thus this proves the incident-endpoint compensation branch, with
no maximum-degree assumption and without requiring the endpoint closing
edge to survive in H'. The nonincident doubled-anchor blocking branch
is still a separate unresolved step.


The full [mixed-book proof](HYP-105-ISSUE230-INCIDENT-BOOK.md) was checked
independently. Thus the incident-endpoint case is resolved in this route;
the remaining issue is quantitative control of nonincident anchor blocking.

## Exact finite closure ledger

The [definition-level oracle](../../research/hyp105_issue230_projection.py)
validates complete original GQ incidence, both global pair injections,
and every nonincident unique projection before enumerating ALL proper
three-paths. The partition below is disjoint; missing labels are retained
in the finite calculation rather than silently discarded. Random fixtures
are reproducible complete injections, seed `230+h`, not minimizers.

| s | maps | proper oriented P3 | missing | incident | blocked | unblocked | synchronized BB-overlap sixsets |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | lex | 1346 | 0 | 400 | 942 | 4 | 2 |
| 2 | reverse | 1154 | 0 | 256 | 898 | 0 | 0 |
| 2 | S68 | 678 | 0 | 72 | 606 | 0 | 0 |
| 2 | S72 | 738 | 0 | 80 | 658 | 0 | 0 |
| 4 | lex | 83892 | 8860 | 4584 | 55384 | 15064 | 7532 |
| 4 | random | 78894 | 10198 | 4112 | 48542 | 16042 | 8021 |
| 8 | lex | 5461066 | 155034 | 100528 | 2292266 | 2913238 | 1456619 |
| 8 | random | 5167090 | 175222 | 78136 | 1888776 | 3024956 | 1512478 |

The frozen [JSON calculations](../../research/issue230-projection-closure.json)
also contain the separate left/right/both blocking counts. Tests recover
the original sixsets and compare every W32 closure to the independent
accepted seven-family census. Each recovered sixset occurs exactly twice;
the subclass is strictly smaller than all BB-overlap motifs. For full H,
incident count is exactly 8Q4. A complete path-budget overflow raises an
error; it never returns a partial count. Execution is explicitly capped
at V<=600.

S68 is a useful finite falsifier of simply treating the path theorem as
the theorem in issue230: all 678 paths are incident or blocked. It does
not refute the asymptotic seven-family assertion.

## The one remaining quantitative bound in this route

For the spectrally pruned H', let P be its endpoint-complete proper path
count and B its NONINCIDENT anchor-blocked path count. Write S for the
original full seven-family count. The proved statements give

    P=(at least 16-o(1))*s^6,
    P = B + P_inc + 2*BB_sync(H'),
    P_inc <=24T M2(G)+sqrt(192m D6(H')),
    D6(H')<=S, BB_sync(H')<=S.

In particular

    (16-o(1))*s^6 <= B+2S+sqrt(192mS).          (4)

Here BB_sync(H') counts original FULL sixsets whose three completion
incidences form an unblocked H' path. Its three anchor incidences need
not be retained. The identity remains valid when the projection anchor incidences lie
outside H': the accepted sixset is counted in the ORIGINAL full model.
If along an infinite sequence S=o(s^6), then (4) forces

    B >=(16-o(1))*s^6.                         (5)

Conversely a uniform upper B<=(16-eta)*s^6 for one fixed eta>0 would
prove Branch A through (4). A sufficient stronger result is B=o(s^6),
which would imply S>=(8-o(1))*s^6. NEITHER upper has been proved here.
The gate concerns a coupled count depending on both maps and the UNIQUE
original projection, not the number of bad source pairs or a random mean.

## Reproduction

Run `python -m unittest discover -s research -p 'test_hyp105_issue230_projection.py'`
and `python research/hyp105_issue230_projection.py`. The new analytic
proofs are independent of these finite checks and of hosted CI. The
original root issue remains open.
