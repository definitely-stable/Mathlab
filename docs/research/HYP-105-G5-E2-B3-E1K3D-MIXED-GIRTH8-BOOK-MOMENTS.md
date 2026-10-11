# HYP-105 B3.2-E1-K3-D — mixed-coordinate GQ compatibility, girth-eight paths and cubic book moment

Date: 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Scientific parent [PR #368](https://github.com/definitely-stable/Mathlab/pull/368), pinned exact HEAD 3b29892ca1f35d29b25a7a8213753ba9d6b6148b; earlier #367/#366. Standalone stacked Draft only, no main change.

**STATUS RESTRICTED_THEOREM_C_ALL_h_LOCAL_GIRTH8 / EXACT_AGGREGATE_FIRST_MOMENT / OPEN_WITH_FORMAL_BLOCKER_GLOBAL_MIXED_BOOKS.** NO universal Omega(s^6) for D6 or seven-family S. NO all-h o(s^6) estimate for Bmixed. NO ASET exponent.

## 1. Original-source compatibility graph

Fix s=2^h, h>=1 and ONE legal GLOBAL pair of injective physical edge labelings f, g on W(3,s). Let a be the minimal host alphabet and Ghat be the accepted Kikuchi graph. For two vertices u=(x,y), v=(x',y') satisfying x!=x' and y!=y', set

    Z=[a] \ {x,x'}, T=[a] \ {y,y'}, |Z|=|T|=r=a-2.

Use F_xz for the ORIGINAL point with f(point)={x,z} if assigned, G_yt for the ORIGINAL line with g(line)={y,t} if assigned; unassigned pairs contribute zero. Define a simple bipartite H_uv=(Z,T,E) by

    z--t iff I(F_xz,G_yt)*I(F_x'z,G_y't)=1.

The two independent original incidences both produce Kikuchi edges from u and v to w=(z,t); conversely any common neighbor w of u,v determines exactly this z,t. Hence the exact identity

    m_uv := |E(H_uv)| = codeg_Ghat(u,v).

It holds for EVERY s=2^h and EVERY globally coherent legal f,g. The first incidence subgraph (z,t) -> (F_xz,G_yt) embeds H_uv in the ORIGINAL incidence graph of W(3,s). The map is injective on BOTH parts because physical pair labels are injective.

The original W(3,s) incidence graph has girth 8 and degree s+1. Therefore H_uv is bipartite, has no 4- or 6-cycles, and max degree <=s+1.

Important transfer firewall: H_uv is not an arbitrary bipartite graph, but merely proving this local subgraph property does not control the collective overlap of H_uv across all u,v. The two original incidences at each edge remain coupled through the same fixed f,g.

## 2. C4-free quadratic capacity, exact integer form

For r-by-r bipartite graph H_uv, write d_z for left degrees, e_t for right degrees. As two distinct right vertices have at most one common left neighbor, and vice versa,

    sum_z binom(d_z,2) <= binom(r,2),
    sum_t binom(e_t,2) <= binom(r,2).

By Jensen (or Cauchy-Schwarz):

    sum_z binom(d_z,2) >= (m^2/r-m)/2.

Therefore

    m(m-r) <= r^2(r-1),

so

    m <= floor[ r*(1+sqrt(4*r-3))/2 ].

Integer computation uses isqrt without floating point. The further exact degree bound m<=r*(s+1) is immediate.

This is a universal all-h restriction for a mixed GQ codegree, not a global positive D6 bound. As r~sqrt(2)*s^(3/2), this C4-free bound permits order s^(9/4) and is too loose to close the cubic mixed book term. The C6 prohibition adds another LOCAL path inequality below; an unproved sharp s^2 edge bound is NOT asserted here.

## 2b. Full girth-eight Moore cap (strengthens C4 alone)

The K1 Alon–Hoory–Linial nonbacktracking path bound is applicable to
the bipartite graph H after peeling its vertices of degree <=1.
For the initial average degree d=m/r >=3, its 2-core peeling lemma
preserves the lower bound NB3 >=2m(d-1)^2. By the 3-path endpoint
injection proved in Section 3, NB3 <=2(r^2-m). Thus, in the regime
m>=3r, necessarily

    m*((m-r)^2+r^2) <= r^4.                              (MOORE8)

When m<3r we do NOT assert (MOORE8); we retain the exact integer
cap m<=3r-1. Define rho(r) as the largest integer m<=r^2
satisfying (MOORE8). A valid unconditional all-h cap is

    M_Moore(r)=min(r^2, max(3r-1,rho(r))).

It is computed by an exact integer binary search; no floating point,
asymptotic assumption or incorrect low-degree extension. Combining
the restrictions gives

    m_uv <= Cmax := min(M_C4(r),M_Moore(r),r*(s+1)),

where M_C4 is Section 2's integer C4-free cap. For r=12
(W(3,4)), M_C4=46 but M_Moore=35. For large r the path bound
has order O(r^(4/3))=O(s^2), still too weak as a collective
mixed-book theorem. The K1 entropy/Moore argument is prior art,
not claimed as a novel generic graph theorem.

## 3. Girth-eight injection of oriented 3-paths

Every non-backtracking 3-walk in H_uv is a simple path (no triangles in a bipartite graph). For each ordered left endpoint z0 and right endpoint t3:

* if they are adjacent, any length-3 path between them would create a C4 (forbidden);
* if they are nonadjacent, TWO distinct length-3 paths would create either a C4 (shared internal vertex) or a C6 (internally disjoint paths).

Thus at most one oriented 3-path left-to-right exists per non-edge, and the exact count satisfies

    P3_LR(H_uv)
      = sum_(zt in E) (d_z-1)*(e_t-1)
      <= r^2-m.

This is an all-h statement checked by independent exhaustive left-to-right three-path enumeration and brute C4/C6 absence on true W(3,2) and sampled/high-book W(3,4) compatible pairs.

## 4. Exact GLOBAL first codegree moment and coarse book upper

For all unordered graph vertex pairs (not only mixed), the exact identity

    sum_{u<v} codeg_Ghat(u,v)
      = sum_{w in V(Ghat)} binom(deg_Ghat(w),2)

holds by counting common-neighbor wedges. Each degree can be independently reconstructed from ORIGINAL W(3,s) star incidences, as implemented in K3-A/B.

Let M1_mixed be the sum of codegrees over all MIXED unordered Kikuchi pairs and Bmixed=3*sum_mixed binom(codeg,3). Then the exact decomposition is

    M1_mixed = sum_w binom(deg_Ghat(w),2)-M1_aligned.

Let Cmax=min(M_C4(r),M_Moore(r),r*(s+1)), r=a-2. As all mixed codegrees c satisfy c<=Cmax,

    Bmixed = sum_mixed c(c-1)(c-2)/2
          <= M1_mixed*(Cmax-1)*(Cmax-2)/2.

This is a genuine deterministic all-h upper bound and a new auditable aggregation of the individual C4-free restrictions. But its scale is generally TOO WEAK; in particular it is NOT shown to be o(s^6) and does not satisfy any acceptance criterion for Branch A/B.

Implementation compares mixed moments and exact cubic book mass against independent K3-C book_moments; every c>=3 original GQ mixed compatibility is rebuilt from physical inverse pairs and checked against Ghat common-neighbor counts. Budgets for pair counts and witness checks fail CLOSED; no synthetic scores masquerade as genuine GQ data.

## 5. Independent falsifiers and scoped acceptance

Reference: research/hyp105_g5e2b3e1k3d_mixed_girth8.py.
Independent tests: research/test_hyp105_g5e2b3e1k3d_mixed_girth8.py.

Two-independent-construction checks: (i) inverse physical label map original-incidence product, (ii) slow scan over original point/line incidence lists, plus a third adjacency oracle common-neighborhood check. Exhaustive true W(3,2) mixed pairs, source-girth C4/C6 checks, left-to-right 3-path uniqueness, true W(3,4) high-book witnesses and deterministic low-book samples, and exact K3-C previous masses 90/21/333. No numpy, no local machine tests, GitHub-hosted CI only. Dedicated path-limited Contract + inherited Research and INDEX; do not add a second full suite.

## 6. Next mathematically decisive question (K3-E)

Even the strengthened C6-free Moore pointwise cap allows too much total Bmixed. Need a SHARED-SOURCE collision/packing lemma that exploits the simultaneous use of ONE original f,g across every mixed pair; quantitatively bound

    sum_mixed binom(codeg_Ghat(u,v),3)

relative to exact A, T and K4, or construct an explicit all-h conversion of this mass into distinct-incidence six-cycles with a bounded multiplier. For Branch A, the cycles must be proper D6 or be counted within the seven original six-motif S families. For a full R3 lower one may use K2 GF5 for six DISTINCT original incidences, with the repeated-column term charged separately.

No LIT/new ASET exponent or PROVED_A/COUNTEREXAMPLE_B claims arise from K3-D. Issue #230, #176, #169 remain OPEN.
