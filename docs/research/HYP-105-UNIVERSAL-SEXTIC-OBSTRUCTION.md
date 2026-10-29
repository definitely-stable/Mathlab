# HYP-105 #230: universal sextic obstruction via a bounded physical core

Date: 2026-10-29. Base: PR #671, `afe8d0ba78261397df2a68c12f927054ad368441`.

**Mathematical claim:** Branch A, in its stated asymptotic meaning, follows
from the full physical degree-tail theorem of #659 and the argument below.
There are absolute constants `delta > 0` and `s0 < infinity` such that, for
every dyadic `s >= s0` and **every** pair of complete, separately injective,
arbitrarily correlated maps `f,g` allowed in #230,

    D6(f,g) + U_BB_overlap(f,g) >= delta s^6.             (THEOREM)

Consequently `inf_(f,g) S_seven(f,g) = Omega(s^6)`. All counts are of
unordered sets of six DISTINCT ORIGINAL incidence IDs. This is a uniform
asymptotic theorem, not a claim of a positive numerical bound at every
small `h`, and not an optimal constant. An explicit sufficient `s0` is
given in Section 8. The accepted GF(5) floor then gives
`R3 >= (5643 delta / 51^6) s^6` for these same maps and `s >= s0`.

**Repository acceptance:** scientific Draft; external qualified referee and
repository acceptance checks remain separate. The finite tests below audit
the combinatorial identities and original-ID transfer; they do not prove an
asymptotic assertion. No issue is closed and no ASET exponent is claimed.

## 1. Inputs, notation, and what changed after #671

Write

    V=(s+1)(s^2+1), d=s+1, N=Vd,
    a=min{t: choose(t,2)>=V},
    C_s=(s^2+1)(s^2+a-2).

The source is the genuine symplectic generalized quadrangle `W(3,s)`.
Its simple physical graph `H` on `[a]^2` contains BOTH opposite-corner
diagonals of each original flag `(p,l)`. Injection makes it simple and
gives each physical edge a unique original flag. It has `2N` edges.

We use the following already proved inputs, with their original scope:

* #652: coordinate-proper simple physical C6s biject with original D6.
* #655/#659: the source pencil books `M_f,M_g <= C_s`. Here
  `M_g=sum_(p,y) choose(R(p,y),2)` and
  `R(p,y)=#{l: p incident l, y in g(l)}`; `M_f` is the dual quantity.
* #659: let `E_T` count full-H edges touching degree greater than `Ts`.
  For absolute positive constants `C,c` in the proved balanced C6
  supersaturation theorem and `s>=64`,

        E_T >= epsilon s^4, T >= 2^41 C^3 epsilon^(-6)
          implies D6 >= c epsilon^12 s^6 / 2^72.        (TAIL)

  See [the complete proof and primary-source reference](HYP-105-FULL-PHYSICAL-DEGREE-TAIL.md).
* #427/#626/#659: among nonincident typed original pairs `(q,r)`, the
  unique original path is `q--l--p--r`. Pairs with
  `f(q) intersect f(p)` or `g(r) intersect g(l)` number at most
  `2s(M_f+M_g) <= 4s C_s`; see
  [the attributed endpoint identities](HYP-105-ENDPOINT-BOOK-NORMAL-FORM.md).
* The off-diagonal point-collinearity matrix `C_P` of `W(3,s)` has
  principal eigenvalue `s(s+1)` and other eigenvalues `s-1,-(s+1)`.
  This also follows from the source incidence spectrum used in #655.

The latest #669--671 estimates concern a random completion of `g` and
cannot by themselves establish (THEOREM). The proof here fixes BOTH maps
throughout. Auxiliary randomness only selects subgraphs of these same
maps; no source incidences or pair labels are reassigned. The new steps
are a path-preserving selector, transfer of its moments back to the core,
and the **mixed full-source/core** bound for internal blocking in Section 6.

For `s>=64` we use the convenient bounds proved in #659:

    a^2<=4s^3, N<=2s^4, C_s<=3s^4/2.                  (1)

## 2. A dense core with two fixed caps

Fix once and for all

    K=64,
    T=max{1,2^59 C^3},
    delta=min{1/8,c*2^(-108)}.

If `D6 >= delta s^6`, the conclusion is immediate. Otherwise (TAIL),
with `epsilon=1/8`, implies `E_T < s^4/8`.

Delete every ORIGINAL flag with either diagonal touching a full-H vertex
of degree greater than `Ts`. At most `E_T` flags are deleted: choose one
such edge per flag, using uniqueness of its original provenance.

The full original-flag conflict graph joins two different flags exactly
when they have the same original point and intersecting right labels, or
the same original line and intersecting left labels. Its edge count is
exactly `M_f+M_g <= 2C_s`. Delete also every original flag whose degree
in this conflict graph exceeds `K`. At most `4C_s/K <= 3s^4/32` flags
are deleted in this second operation.

Let `H0` be the paired physical graph on the remaining original flags.
Its vertex set is still `[a]^2`, including isolated corners. Write `A0`
for its adjacency, `m0` for its edge count, and `Delta` for its maximum
degree. Then

    m0 >= 2(N-s^4/8-3s^4/32) >= s^4,
    m0 <=2N<=4s^4,  Delta<=Ts.                         (2)

The induced original conflict graph has maximum degree at most `K`.
Every core pencil-coordinate population `R0(p,y)` is at most `K+1`,
because the flags counted there form a clique of that conflict graph.
The dual pencil populations obey the same bound. Projection flags used
later are allowed to lie outside this core.

## 3. A selector that preserves each proper short path

A directed physical path is **proper** if all its first coordinates are
distinct and, separately, all its second coordinates are distinct.
Give the retained original flags a uniform random ordering. Keep a flag
if it precedes all its conflict neighbors. The kept set is independent.
Next independently give all left and right coordinate symbols unbiased
binary colors. Keep a whole flag, with BOTH diagonals, only when both
its pair labels are bichromatic. Let `G` be the resulting physical graph.

`G` is bipartite and has no row/column cherries. In a simple C6, any
repeated coordinate occurs at distance 2 or 3. Distance 2 contradicts
conflict independence; distance 3 contradicts the coordinate cuts.
Thus every simple C6 in `G` is proper and

    C6(G) <= D6(f,g).                                  (3)

For `r=2,3`, the flags of a proper r-path have distinct original point
IDs and distinct original line IDs, hence are pairwise nonconflicting.
The union of their closed conflict neighborhoods has size at most
`r(K+1)`. If these r flags are the first r in that union, all survive;
the probability is `1/choose(b,r) >= [r(K+1)]^(-r)`.
Each coordinate path has `r+1` distinct symbols, so the two cuts preserve
it with probability `4^(-r)`. We may therefore use the uniform bounds

    sigma2=1/[64(K+1)^2],
    sigma3=1/[64*27(K+1)^3].                           (4)

Each proper r-path survives with probability at least `sigmar`.
Independence of different paths is neither asserted nor needed.

## 4. Sixth moments of G and fourth moments of H0

For ANY simple bipartite graph with adjacency `A`, maximum degree
`Delta`, and `m` edges, a nonsimple directed closed 6-walk repeats a
vertex at cyclic distance 2. There are six possible positions. Removing
the resulting two-step backtrack leaves a rooted closed 4-walk, and
reinsertion has at most `Delta` choices. Hence

    tr(A^6) <=12 C6 +6 Delta tr(A^4).

Cauchy on the real eigenvalues gives
`tr(A^4)<=sqrt(tr(A^2)tr(A^6))=sqrt(2m tr(A^6))`.
Solving this quadratic inequality yields, conservatively,

    tr(A^6) <=24 C6 +144m Delta^2.                      (5)

This absorbs the 4-cycle/backtrack term; bounding all nonsimple 6-walks
by a fixed multiple of `m Delta^2` directly would be invalid.

Since we are in the case `D6<delta s^6<=s^6`, every selector outcome obeys

    tr(A_G^6)<=L6 s^6,  L6=24+576T^2,
    tr(A_G^4)<=sqrt(8L6) s^5.                          (6)

Let `P_r(u,v)` count proper directed r-paths in H0 with ordered physical
endpoints `(u,v)`. Pointwise `E[(A_G^r)_(u,v)]>=sigmar P_r(u,v)`.
Jensen, summed over ordered endpoints, gives

    ||P3||_F^2 <= sigma3^(-2) L6 s^6,
    ||P2||_F^2 <= sigma2^(-2) sqrt(8L6) s^5.            (7)

To recover the fourth moment of the **core**, write `A0^2=P2+B2`.
The total number of directed two-walks returning to the same first
coordinate is exactly

    Qx=2 sum_(p,y) R0(p,y)^2=4N0+4M_g(core),           (8)

where `N0` is the retained original flag count. Dually define `Qy`.
Every improper two-walk is in one of these two populations. By (1),
`Qx+Qy<=28s^4`. Each entry of `B2` is at most `Delta`, the upper bound
on a common-neighbor population in a simple graph. Thus

    tr(A0^4) <= L4 s^5,
    L4=2 sigma2^(-2) sqrt(8L6)+56T.                    (9)

This step does NOT presume that H0 itself is coherent or bipartite.

## 5. Many proper paths; few exceptional endpoints

The length-three path inequality for a graph on n vertices gives
`1^T A0^3 1 >= (2m0)^3/n^2`. For completeness, choose a uniform directed
edge `(u,v)`. Convexity of `t log t` gives
`E log deg(u) >= log(2m0/n)`; Jensen applied to
`deg(u)deg(v)` gives the inequality, since
`1^T A0^3 1 =2m0 E[deg(u)deg(v)]`.
By (1)--(2) there are at least `s^6/2` directed three-walks.

Adjacent coordinates never coincide. Returns at distance 2 contribute
at most `2 Delta(Qx+Qy)`. For the distance-three first-coordinate return,
let `1_x` indicate the physical row x. Its exact count is

    sum_x 1_x^T A0^3 1_x
     =sum_x (A0 1_x)^T A0(A0 1_x)
     <=Delta sum_x ||A0 1_x||^2=Delta Qx.              (10)

The last equality is also (8), now obtained by summing rows. The dual
bound is `Delta Qy`. This handles the odd-coordinate-return paths even
though H0 has not been cut. In total,

    sum_(u,v) P3(u,v) >= s^6/2-84T s^5.               (11)

The two endpoint coordinate pairs of a proper path decode an original
point q and line r when the labels are occupied. Exclude three classes
of ordered physical endpoint pairs:

* one decoded label is missing: at most `8(a-1)choose(a,2)<=4a^3`;
* the decoded original q,r are incident: exactly `4N`;
* q,r are nonincident but original-end-bad: at most `16s C_s`.

The last bound is four orientations of the previously proved typed-pair
bound. Their union has size at most `64s^5` for `s>=64`. Cauchy and (7)
show that they carry at most

    L_E s^(11/2),  L_E=8 sigma3^(-1) sqrt(L6)          (12)

proper paths. These are actual path-weighted bounds, not unweighted
endpoint proportions. Paths remaining after (12) have the unique source
projection `q--l--p--r`, with f(p) disjoint from the two endpoint first
coordinates and g(l) disjoint from the two endpoint second coordinates.

## 6. Internal blocking: the mixed full/core estimate

Let `S_x={q:x in f(q)}`. Then `|S_x|<=a-1` and
`sum_x |S_x|=2V`. Consider a proper core path

    v0=(x,y), v1=(k,y1), v2, v3=(z,w),

with occupied nonincident q=`f^(-1){x,z}`, r=`g^(-1){y,w}` and source
projection `q--l--p--r`. We count those for which `k in f(p)`.
Put `u=f^(-1){x,k}`; its first physical edge is a core flag at u.
Use the FULL pencil array R at the anchor p, the CORE array R0 at u,
and define

    K_pu=sum_y R(p,y) R0(u,y).

The number B of possible triples `(v0,v1,v3)` satisfying this blocking
condition is at most

    B <= sum_(x,k: u=f^(-1){x,k})
          sum_(p in S_k) [C_P 1_(S_x)](p) K_pu.       (13)

Indeed, choose p in S_k and a point q in S_x collinear with p; q
determines z. Choose a core line through u and a full line r through p
whose physical labels contain the same y; these determine y1,w. Every
actual triple is counted in this construction. Dropping nonincidence,
properness and further distinctness restrictions only enlarges its count.
In particular the anchor flag `(p,r)` is NOT assumed retained.

Cauchy's first squared factor in (13) is at most

    sum_(x,k,u) sum_(p in S_k) [C_P1_(S_x)](p)^2
     <=2 sum_x ||C_P1_(S_x)||^2
     <=4d^2 [V+s^2(a-1)] <=64s^(11/2).               (14)

For the first inequality, for fixed x,p there are at most the two
coordinates k in f(p). For the second, separate the constant eigenspace
of C_P from the others and use

    ||C_P1_S||^2 <= s^2d^2 |S|^2/V+d^2 |S|,
    sum_x |S_x|^2 <=2V(a-1).

The second squared factor exploits BOTH caps in Section 2. First
`max_(p,u) K_pu <=2d(K+1)` because `R0(u,y)<=K+1` and
`sum_y R(p,y)=2d`. Next its unsquared sum is exactly

    sum_(x,k,u) sum_(p in S_k) K_pu
      =sum_(k,y) D_full(k,y) D_core(k,y)
      <=Delta sum_(k,y)D_full(k,y)=4N Delta,           (15)

where D denotes physical degree. Both orientations of each f(u) label
are included on the left. Combining the maximum with (15) gives

    sum_(x,k,u) sum_(p in S_k) K_pu^2
      <=8d(K+1)N Delta <=32(K+1)T s^6.               (16)

Therefore a convenient bound for the number of blocked triples is

    B <= B0 s^(23/4),  B0=64 sqrt((K+1)T).            (17)

For each such triple, the number of completions through v2 is at most
`(A0^2)_(v1,v3)`. Cauchy, followed by summing over ALL first edges and
last vertices, gives

    I_(first internal x)
     <=sqrt(B sum_(v0v1 oriented edge,v3) [(A0^2)_(v1,v3)]^2)
     <=sqrt(B Delta tr(A0^4))
     <=sqrt(B0 T L4) s^(47/8).                        (18)

Path reversal gives the second internal first coordinate. Interchanging
original points/lines and the two coordinate alphabets gives both
internal second coordinates; all bounds used above have the stated dual
form. The four events cover internal blocking on original-end-good paths:

    I_internal <=4 sqrt(B0 T L4) s^(47/8).             (19)

Since `47/8 < 6`, this is a sub-sextic error for fixed T,K. It is the
missing deterministic estimate; neither random completion of g nor a
uniform distribution inside its physical fibers is used.

## 7. From unblocked paths to accepted ORIGINAL B/B-overlap

For every surviving unblocked proper path, let its three original flags
be `(u_i,l_i)`, i=1,2,3. Append the genuine original projection flags

    (q,l), (p,l), (p,r).

The six original IDs are distinct. The closing pair f(q) is the edge
between the first-coordinate endpoints of a simple three-edge path,
so q differs from all u_i. The pair f(p) is disjoint from all four first
coordinates, so p differs from q and all u_i. Dually, r differs from
all l_i and l differs from r and all l_i. Their original source graph
is therefore the three-edge path q--l--p--r and three isolated edges.

The left physical projection is a doubled f(p) plus the C4 formed by
f(q),f(u_1),f(u_2),f(u_3), on six symbols of degree two. The right
projection is a doubled g(l) plus its analogous C4, also on six symbols
of degree two. Both source profiles are B; their repeated-factor flag
pairs intersect at the UNIQUE original flag `(p,l)`. This is precisely
the historical accepted positive GF(5) **B/B-overlap** class.

Given a produced sixset, its repeated source factors p,l identify the
three-edge source component and its endpoints q,r uniquely. The three
other original flags are then fixed. Removing f(q) from the left C4
orders them up to reversal. For each such order, their right pair labels
give at most one right coordinate sequence (the two adjacent edge
intersections are distinct). Thus at most two directed physical paths
produce the same original sixset. Consequently

    U_BB_overlap >= (unblocked proper directed paths)/2. (20)

This is a lower subcount, not equality with the entire B/B-overlap class.
It supplies the original-ID/GF(5) bridge that the old projected-path
surrogate notes deliberately did not assert.

## 8. Quantitative conclusion and exact quantifiers

Equations (11),(12),(19),(20), in the case `D6<delta s^6`, prove

    U_BB_overlap >= s^6/4 -42T s^5
                    -(L_E/2) s^(11/2)
                    -2 sqrt(B0 T L4) s^(47/8).        (21)

All constants defined above are independent of h, f and g. For example,

    s0=max{64,1008T,(12 L_E)^2,
               [48 sqrt(B0 T L4)]^8}                 (22)

is sufficient: each of the three errors in (21) is at most `s^6/24`.
Thus `U_BB_overlap >=s^6/8` when `s>=s0`. In the complementary case,
`D6>=delta s^6`. Since `delta<=1/8`, (THEOREM) follows in both cases.

This proves the Branch A quantifier

    exists delta>0, s0<infinity,
    for every h>=1 with 2^h>=s0,
    for every allowed complete correlated (f,g): S_seven>=delta (2^h)^6.

Equivalently, no admissible infinite sequence with h tending to infinity
has `S_seven=o(s^6)`. The proof does not promise a positive bound for the
finitely many dyadic sizes below s0, which is unnecessary for the stated
Omega(s^6) disjunction. It does not establish a sharp finite-h minimum,
total R3 equality, an R2 upper bound, or an obstruction to other ASET
constructions outside the specified GQ model.

## 9. Verification and review limits

The companion independent finite checks use genuine symplectic W32/W34
incidences and full injected labels, including sparse retained cores:

* direct path enumeration versus pencil and row-matrix return identities;
* original-source projection versus the mixed bound (13), including
  anchors outside the core, its exact degree-product identity (15), and
  the spectral squared-factor bound (14);
* each produced sixset checked by the unchanged historical GF(5) seven
  class classifier, with multiplicity exactly two;
* bipartite sixth-moment bounds versus exhaustive small graph walks and
  independent simple-cycle enumeration;
* exhaustive selector survival on small conflict graphs, including
  overlapping neighborhoods of prescribed independent paths.

The internal collaborators independently checked the mixed full/core
estimate and the original B/B-overlap reconstruction. A complete external
qualified referee has not yet reviewed this manuscript. Passing finite
tests or CI is not presented as a replacement for that review.
