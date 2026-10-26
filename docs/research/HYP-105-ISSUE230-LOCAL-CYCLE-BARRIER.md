# Universal seven-family lower: an exact local transfer obstruction

Status: **OPEN_WITH_FORMAL_BLOCKER** for Branch A/B. The result below is a
rigorous all-h embedding theorem for a fixed local source pattern, together
with two exact finite selectors. It is **not** a full-map small-S sequence,
not an EICE-002 high-minimum-degree G*, and not a GF5 signed-flow result.
Root issue #230 remains open; full-model S is uncomputed for the extension.

## 1. Main finding

For every s=2^h >= 8 there are legal complete global injections f,g and an
induced 18-incidence source subuniverse I for which:

* Five coordinate-proper three-edge physical paths have the same endpoints.
* The endpoint pair labels decode the same genuine nonincident original
  point q and line r, with their unique original projection q--ell--p--r
  also entirely present in I.
* All five paths are end-clean but their unique projection completions are
  internally blocked.
* Both diagonals of every incidence in I are retained.
* The entire local physical graph is bipartite, has no row/column cherries,
  no triangles and no C4; it has exactly ten C6, each with six distinct
  original source incidence IDs.
* All ten C6 are improper: five have physical-coordinate profile 5/6 and
  five have profile 6/5.
* Every one of the seven accepted original-sixset counts on I is zero.

Thus neither an individual improper six-cycle nor the union of several
same-endpoint paths plus their genuine unique GQ projection has a universal
positive local transfer to the accepted seven families. Any successful
transfer must use additional original incidences outside this pattern or
a global density/minimum-degree/cut property.

The local graph has degree-one vertices, lacks a bicolor cut on **either**
physical coordinate alphabet, and has some improper NB3s away from the five
specified endpoint paths. It does not contradict the EICE-002 theorem.

## 2. Explicit labels and source factors

Use seven left physical symbols alpha,beta,z_0,...,z_4 and seven right
symbols gamma,delta,w_0,...,w_4. Subscripts are modulo 5. Take fifteen
original incidences A_i,B_i,C_i whose original point and line endpoints
are all distinct; the source subgraph on these factors is a matching.
Assign their pair labels as follows:

| Incidence | Original left pair label | Original right pair label |
| --- | --- | --- |
| A_i | {alpha,z_i} | {gamma,w_i} |
| B_i | {z_i,z_(i+1)} | {w_i,w_(i+2)} |
| C_i | {z_(i+1),beta} | {w_(i+2),delta} |

Add four different original factors q,p,ell,r and the original path

    D=(q,ell), E=(p,ell), F=(p,r).

Their labels are

    f(q)={alpha,beta},       g(r)={gamma,delta},
    f(p)={z_0,z_2},          g(ell)={w_0,w_1}.

There are seventeen distinct original point labels and seventeen distinct
original line labels. They are indeed pairwise distinct within each side:
the B_i labels form a 5-cycle on z's on the left and a step-two 5-cycle
on w's on the right; f(p) is a complementary left chord, g(ell) is a
complementary right chord. All other labels involve fresh endpoint symbols.

Let u=(alpha,gamma), v=(beta,delta), a_i=(z_i,w_i),
b_i=(z_(i+1),w_(i+2)). The first physical diagonal of A_i,B_i,C_i is

    u -- a_i -- b_i -- v.

Every such path uses four distinct coordinates in each alphabet. Its
endpoint pair labels are exactly f(q),g(r). Both anchor labels avoid those
endpoint symbols, so the paths are end-clean. The left anchor is blocked
for i in {0,1,2,4}; the right anchor is blocked for i in {0,1,3,4}. Hence
all five paths are blocked, with three both-blocked, one left-only and one
right-only.

## 3. All-h genuine GQ embedding and global extension

Write d=s+1 and N=Vd=(s+1)^2(s^2+1). First choose a genuine original
nonbacktracking length-three source path q--ell--p--r. For example, choose
two distinct original lines ell,r through p and q in ell minus p.
Partial linearity gives q not incident with r. The GQ projection axiom
then says that this is the unique original length-three path between q,r.

For the other fifteen original incidences we need an induced matching,
with no extra source edges to any of q,p,ell,r. Exclude the original
points in N(ell) union N(r) and the original lines in N(q) union N(p).
This excludes at most 4d^2 original incidences.

In a d-regular C4-free bipartite source, a greedy chosen matching edge
conflicts with at most

    2d^2 - 2d + 1 = 2s^2+2s+1

edges when enforcing an induced matching. Indeed edges incident with the
d point neighbors of its line contribute d^2, as do edges incident with
the d line neighbors of its point. Their intersection has exactly 2d-1
edges: a further cross-edge would make an original C4.

Consequently an induced matching disjoint from the anchor path can be
chosen with size at least

    ceil[ (N-4d^2)/(2d^2-2d+1) ].

For s>=8, N-4d^2=(s+1)^2(s^2-3)>s^2(s^2-3)>45s^2,
whereas 15(2s^2+2s+1)<=45s^2. The matching therefore has at least
fifteen edges. Select fifteen of them and assign A_i,B_i,C_i in any order.
The induced original source graph on the chosen seventeen points and
seventeen lines is exactly the fifteen-edge matching plus D,E,F.

The minimal allowed physical alphabet a is at least seven. Both prescribed
sets contain just seventeen distinct pair labels. Since binom(a,2)>=V,
each prescribed injection extends by any bijection between the remaining
original factors and an equally large unused subset of physical pairs.
Thus the pattern is compatible with complete legal maps for every
s=2^h>=8. The counts asserted here concern only the induced subuniverse I;
the full-model counts can receive contributions from all other incidences.

## 4. Exact physical cycle proof

For the fifteen matching sources, the graph consists of five internally
disjoint length-three u-v paths and fifteen isolated opposite-diagonal
edges. Hence the only cycles are the ten choices of two u-v paths.
For paths i,j, their left internal coordinate sets are {z_i,z_(i+1)}
and {z_j,z_(j+1)}. They intersect exactly when j-i is +/-1. Their right
internal coordinate sets are {w_i,w_(i+2)} and {w_j,w_(j+2)}. They
intersect exactly when j-i is +/-2. Every distinct pair has exactly one
kind of intersection. Five resulting C6 have profile 5/6 and five 6/5.

Adding D,F connects some isolated opposite-diagonal components into trees:
one chain joins the old components C_1,A_0,C_4,A_2, and another joins
A_1,C_3. It creates no cycle. The two E diagonals attach a two-edge
pendant path to a_0 and a leaf to b_4. They create no cycle either.
Therefore the full eighteen-source physical graph still has precisely
those ten improper C6, and no triangles or C4. Its degree distribution
is 22 vertices of degree one, 17 of degree two, 2 of degree three and 2
of degree five; there are 43 active vertices and 36 physical edges.

Every D6 produces a coordinate-proper physical C6 by the accepted exact
source-preserving correspondence. There are none, so D6(I)=0.

## 5. Analytic exclusion of all six other accepted families

The only original repeated point available is p, occurring in E,F. The
only original repeated line is ell, occurring in D,E. Thus C/A and C/B
are impossible, and B/B-disjoint is impossible.

For B-left/A-right a selected sixset must contain E,F, omit D, and select
four matching sources. The doubled edge {z_0,z_2} saturates both physical
coordinates, so the four matching source point labels must form a C4 on
the remaining coordinates. On {alpha,beta,z_1,z_3,z_4}, their available
edge graph is K_{2,3}, with parts {alpha,beta} and {z_1,z_3,z_4}, plus
the single edge {z_3,z_4}. Its C4s all consist of two A edges and two C
edges. The two A edges and F then give right physical coordinate gamma
degree three, violating the exact degree-two requirement. Hence B-left=0.

The dual argument for A-left/B-right uses D,E, omits F and deletes right
coordinates w_0,w_1. The remaining edge graph is K_{2,3} plus the single
edge {w_2,w_4}. A C4 uses two A sources. Together with D these make left
physical alpha degree three. Hence B-right=0.

For B/B a sixset must contain D,E,F plus three matching sources. On the
left these three labels must be an alpha-beta length-three path after
deleting z_0,z_2. Its middle edge must be B_3={z_3,z_4}. On the right
they must be a gamma-delta length-three path after deleting w_0,w_1,
whose middle edge must be B_2={w_2,w_4}. The same three original sources
cannot have two different middle-column IDs: the other two edges on
each side must be A/C edges, so B/B-overlap=0.

Thus S(I)=0 by the original-source definition, independently of the
physical graph cycle enumeration.

## 6. The sharp five-path local capacity

Here is the exact limit of one plain path-packing argument. Suppose m
coordinate-proper u-v three-edge paths have pairwise disjoint internal
vertices, and their first internal vertices have distinct first and
second coordinates, as do their second internal vertices. These last
conditions follow from no row/column cherries at u,v.

Fix a path (u,a,b,v). Its union with another path (u,c,d,v) is a simple
C6. It is improper only if one of

    x(a)=x(d), x(b)=x(c), y(a)=y(d), y(b)=y(c)

holds. Each equality can concern at most one other path. A path therefore
has at most four improper partners. At least

    max{0, m(m-5)/2}

path pairs produce coordinate-proper C6. The threshold m=5 is sharp: the
pentagon construction attains zero proper pairs. For m=5 with no proper
pair, both coordinate-conflict graphs must be edge-disjoint 2-regular
graphs on five path IDs, hence complementary C5s. Up to relabeling and
reversal this is the z-step-one / w-step-two arrangement above.

The full graph has n=(2+o(1))s^3 and at least (16-o(1))s^6 proper
oriented P3s in the existing pruned-path theorem. The mean per oriented
endpoint pair is approximately four. A sharp local capacity of five
therefore leaves room for that mean. This observation only explains why
the simplest endpoint pigeonhole calculation has no positive surplus;
it does not assert that a globally dense counterexample can attain the
pentagon capacity on enough endpoints.

## 7. Independent exact checks

Two standalone files in the research directory import no Mathlab code:

* `research/hyp105_issue230_local_cycle_pattern.py`: the fifteen-source pattern; direct examination
  of all binom(15,6)=5,005 original sixsets and independent physical
  simple-cycle enumeration.
* `research/hyp105_issue230_local_cycle_barrier.py`: the eighteen-source pattern; direct examination
  of all binom(18,6)=18,564 original sixsets, independent physical cycles,
  and a fresh GF(8) symplectic construction of all 585 original points
  and 585 original lines of W(3,8).

The genuine W38 construction uses GF(2)[T]/(T^3+T+1), normalized
projective vectors and totally isotropic two-dimensional subspaces for
the alternating form x_0 y_3+x_3 y_0+x_1 y_2+x_2 y_1. It independently
checks degree nine and original partial linearity, decodes the actual
unique anchor projection from all nine points of r, chooses the real
induced matching, confirms all edges in the seventeen-by-seventeen
induced original source block, and completes f,g into the minimal K_35.

Exact finite results: seven vector (0,0,0,0,0,0,0), ten physical C6 with
profiles 5/6 and 6/5, five specified end-clean proper P3s, all blocked.
There are exactly two leafless original A/A sixsets, neither accepted:

    {A0,C0,A1,B2,C2,E}: left C6, right 2C3;
    {B0,A1,B2,C2,D,F}: noncoincident left/right C6.

No signed GF5 count or positivity claim is made for these two uncharged
sixsets. No full-model S, R2 or R3 is computed for the global extension.

Run:

    python research/hyp105_issue230_local_cycle_pattern.py
    python research/hyp105_issue230_local_cycle_barrier.py

Both exit successfully with their stated exact ledgers. The all-h
embedding proof, rather than an asymptotic fit of these finite outputs,
establishes compatibility with the frozen original source model.

## 8. Consequence for Branch A

The existing full-graph C6 density theorem cannot be transferred to S by
a source-local statement asserting that every improper C6, every
five-path endpoint pool, or every such pool plus its unique GQ anchor
path contains an accepted sixset. The explicit pattern refutes all such
statements in the permitted source model.

The unproved step must exploit additional global source incidences and
their shared physical labels, or the stronger restrictions of a valid
EICE-002 G*. This result does not settle either branch of issue 230.
