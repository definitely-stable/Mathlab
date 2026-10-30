# HYP-105 #230: deletion resilience, disjoint packing, and the coefficient-eight compensation limit

Date: 2026-10-30. Separate follow-up to the proof manuscript in
[PR #672](https://github.com/definitely-stable/Mathlab/pull/672), immutable
parent `9c54f3c16af201ebf6d915de207d21d201da28d6`.

**Scope.** Genuine `W(3,s)`, `s=2^h`, minimal coordinate alphabet,
arbitrary fixed complete separately injective and correlated f,g. All
sixsets consist of six DISTINCT ORIGINAL incidence IDs. Write `D=D6`
and `B=U_BB_overlap`; for an original-flag set Z write

    B_avoid(Z)=#{accepted original B/B-overlap sixsets Q: Q intersect Z is empty}.

This manuscript proves three extensions of #672:

1. There are fixed positive `delta,rho` and finite `s0`, all specified
   below, such that for every allowed map and dyadic `s>=s0`,

        D < delta s^6, |Z| <= rho s^4
          implies B_avoid(Z) >= s^6/16.                (RESILIENCE)

   Z is arbitrary, may depend on the full maps, and excludes ALL SIX
   source IDs of each counted motif, including projection anchors.
2. Under the same small-D premise, the original B/B-overlap hypergraph
   contains more than `rho s^4/6` pairwise original-incidence-disjoint
   motifs. This is a packing in the source IDs, not in physical symbols.
3. For every sequence of allowed maps with `s -> infinity`, if
   `D=o(s^6)` and `|Z|=o(s^4)`, then

        liminf B_avoid(Z)/s^6 >= 8.                    (STABILITY)

The coefficient 8 is a proved lower coefficient under the low-D premise;
no assertion of sharpness or of its attainability is made. In particular
this does not claim an unconditional `S_seven >= (8-o(1))s^6`.

These are analytic consequences of the complete argument of #672 and its
degree-tail input #659. They inherit those manuscripts' external-review
requirements. Scientific Draft, no change to issue acceptance state.

## 1. Exact exposure of forbidden ORIGINAL flags

Let `N=(s+1)^2(s^2+1)` be the number of original flags. For nonincident
typed endpoints `(q,r)` the GQ axiom gives the unique original path

    q -- ell -- p -- r,

with flags `(q,ell),(p,ell),(p,r)`. Define E_Z as the set of typed
nonincident endpoints whose three-flag projection meets Z. Then

    |E_Z| <= min{Ns^2, 3s^2 |Z|}.                     (1)

In fact EVERY fixed original flag occurs in EXACTLY `s^2` projections in
each of the three positions. For a first flag `(q,ell)`, choose
`p in ell minus {q}` and `r through p other than ell`: s choices each.
For a middle flag `(p,ell)`, choose `q in ell minus {p}` and
`r through p other than ell`. For a last flag `(p,r)`, choose
`ell through p other than r` and `q in ell minus {p}`. In each case q
is nonincident with r: otherwise a source 4-cycle would result.
Uniqueness of the GQ projection makes all choices distinct. A flag
cannot occupy two positions in one projection, so its three populations
are disjoint and its total exposure is exactly `3s^2`.

For arbitrary Z, summing these singleton exposures is a union bound;
overlaps are not assumed absent. There are FOUR ordered physical
endpoint pairs for each typed `(q,r)`, hence the corresponding physical
mask has size at most

    4|E_Z| <= 12s^2 |Z|.                              (2)

If P3 counts proper directed physical three-paths in any paired core,
the mass of paths whose original projection meets Z therefore satisfies

    M_Z <= sqrt(12s^2 |Z|) ||P3||_F.                  (3)

Here the Frobenius norm is over ORDERED physical corner pairs. Neither
uniform endpoint distribution nor independence of labels is used.

## 2. Quantitative positive-density resilience

Use EXACTLY the constants of [the complete #672 proof](HYP-105-UNIVERSAL-SEXTIC-OBSTRUCTION.md):

    K=64, T=max{1,2^59 C^3},
    delta=min{1/8,c*2^(-108)},
    sigma3=1/[64*27*(K+1)^3], L6=24+576T^2,
    M=sigma3^(-1) sqrt(L6),
    rho=min{1/8,1/(768 M^2)}.                          (4)

C,c are the positive constants of the proved balanced C6 supersaturation
theorem used in #659. Let s0 be the sufficient threshold in #672,
Section 8; it is unchanged here.

Assume `D<delta s^6`. The tail and conflict-degree deletions in #672
remove fewer than `(1/8+3/32)s^4` original flags. Delete Z as well,
BEFORE defining the core or applying the selector. At least

    N0 >= N-(1/8+3/32+rho)s^4
       >= (25/32-rho)s^4 >=21s^4/32

flags remain. Both physical diagonals of every surviving flag remain.
Thus `m0=2N0>=s^4`, exactly the density lower bound required in #672.
The maximum physical degree is still at most Ts, and the maximum source
conflict degree is still at most K. Further deletions cannot increase
either degree, the core pencil populations, or the source books.

All of #672's selector, moment, return, and internal-blocking estimates
therefore apply with the SAME constants to this new core. In particular

    ||P3||_F <= M s^3.                                (5)

For `s>=s0`, that proof leaves at least `s^6/4` unblocked directed paths,
BEFORE excluding forbidden projection anchors. Their three path flags
already avoid Z by construction. By (3)--(5), paths whose original
projection uses any flag of Z have mass at most

    M_Z <= sqrt(12) M sqrt(rho) s^6 <= s^6/8.          (6)

The last inequality follows directly from `rho<=1/(768M^2)`.
Thus at least `s^6/8` unblocked directed paths have ALL SIX source flags
outside Z. The original-ID reconstruction in #672, Section 7 maps them
to accepted B/B-overlap sixsets with multiplicity at most two. This gives

    B_avoid(Z) >= s^6/16,

proving RESILIENCE. The full/core mixed estimate from #672 is essential:
an anchor outside the retained core is permitted provided it is outside Z.
Merely requiring the three path flags to avoid Z would not prove this
six-ID resilience statement.

## 3. Source-ID-disjoint packing

Take a maximal matching in the 6-uniform hypergraph whose vertices are
the N original flags and whose edges are the accepted original
B/B-overlap sixsets. Let its size be nu and let Z be the union of its
flags, so `|Z|=6nu`. Maximality means every accepted motif meets Z.

If `6nu<=rho s^4`, RESILIENCE instead gives at least `s^6/16>0`
motifs disjoint from Z, a contradiction. Therefore

    nu > rho s^4/6.                                   (7)

No bound on the maximum number of motifs through one original flag is
needed. This is an existence theorem for an original-ID-disjoint packing;
it is not a claim that motifs have disjoint physical coordinate supports.

## 4. Recovering the leading coefficient: 8

Consider ANY sequence of complete maps with `D=o(s^6)` and ANY
map-dependent forbidden sets `|Z|=o(s^4)`. Fix `0<epsilon<1/4`.

Choose fixed `T_epsilon` large enough that #659 makes the full physical
tail at most `epsilon s^4` once s is sufficiently large. This is valid
because the term proportional to `(D/s^6)^(1/12)` tends to zero.
Choose fixed `K_epsilon>=6/epsilon`, so the conflict-degree deletion costs
at most `epsilon s^4`. Also delete Z. Hence the new core has

    N0 >= N-2epsilon s^4-|Z|,
    liminf N0/N >=1-2epsilon.                         (8)

Keep these two caps FIXED while taking the limit in s. The minimal
alphabet satisfies `a^2=(2+o(1))s^3`, and `N=(1+o(1))s^4`.
The exact length-three walk inequality therefore gives

    total directed three-walks >= (4N0)^3/a^4,
    liminf total/s^6 >=16(1-2epsilon)^3.              (9)

For the fixed caps, #672 bounds improper walks by O(s^5), exceptional
endpoint mass by O(s^(11/2)), and internal blocking by O(s^(47/8)).
All are o(s^6). Its proper-path moment bound is `||P3||_F=O(s^3)`;
the implicit constant may depend on epsilon, but not on the maps or s.
Equation (3) and `|Z|=o(s^4)` then show that projection anchors in Z cost
another o(s^6) paths. Dividing the survivors by their at-most-two
original-sixset multiplicity yields

    liminf B_avoid(Z)/s^6 >=8(1-2epsilon)^3.           (10)

This holds for EVERY fixed positive epsilon. Taking epsilon down to zero
AFTER the liminf proves STABILITY. No growing-cap substitution or
unjustified uniformity in epsilon is used. The coefficient is

    [ (4N)^3/a^4 ] / [2s^6] -> 8,

the original-flag/coordinate density coefficient followed by reversal
normalization. It is not inferred from finite observed motif counts.

In particular, when D is sub-sextic, forbidding any o(N) original flags
still leaves `(8-o(1))s^6` accepted original B/B-overlap motifs.

## 5. Independent checks and limits

The companion finite oracle reconstructs EVERY nonincident projection
from genuine source geometry, then independently enumerates its three
flag-position populations by flag-centered source choices. On W32 and
W34, every original flag has exactly s^2 endpoints at each position and
3s^2 distinct total endpoints. Forbidden-set exposure is compared by
inverted source postings and direct endpoint projection.

For full legal physical maps it additionally enumerates core paths,
checks weighted Cauchy (3), rebuilds all six original IDs, and checks the
unchanged historical GF(5) classifier. Every counted sixset is disjoint
from Z, and directed-path multiplicity remains exactly two. A separate
complete W32 seven-class census bounds the new subcount independently.
Empty, singleton, source-pencil, spread-out, and complete forbidden sets
are finite controls; none is alleged to verify an asymptotic premise.

The numerical examples have s=2 or s=4 and need not satisfy the low-D
asymptotic premise or the very large sufficient threshold. They test the
exposure identities and exact original-ID normalization, not the number
8 or a finite-h version of the asymptotic theorem. External qualified
review of #672 and this extension remains separate from tests and CI.
