# HYP-105 E1-K3-F2 — weighted C4 diagonal operator, exact cuts, and chord-to-motif extraction

Date: 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked scientific child of [PR #371](https://github.com/definitely-stable/Mathlab/pull/371), pinned parent HEAD 8d3eae4c1529f37d66b8e8aec8762bdcdd561139. Inherited K3-A/B/C/D/E/F1. Only the K3-F2 research branch changes, not main.

**Status: RESTRICTED_THEOREM_C_ALL_GRAPHS_WEIGHTED_OPERATOR / EXACT_GQ_CHORDED_MOTIF_LEDGER / OPEN_WITH_FORMAL_BLOCKER_GLOBAL_PACKING.** Neither Branch A (seven-family S >=Omega(s^6)) nor Branch B (infinite correlated counterexample) is decided, and no ASET exponent or full R3 lower bound is claimed.

## 1. Why K3-F1 failed as an extraction

K3-F1 proved an all-h shared original-incidence spectral transport bound for physical star degrees. Its coarse extraction to C4-weighted tails is weaker than K3-E in every pinned real W(3,2)/W(3,4) labeling because merely bounding the NUMBER of high-degree physical stars forgets WHERE the opposite four-cycle diagonals occur.

Instead, explicitly maintain the symmetric positive-entry weighted adjacency matrix on Kikuchi vertices:

    W_uv = choose(c_Ghat(u,v),2)
         if u!=v and u=(x,y),v=(x',y') satisfy x!=x',y!=y',
         else 0.

It has zero diagonal, integral nonnegative entries, and is based on ONE actual global legal f,g. Define its strength rho_u=sum_v W_uv. The number of mixed C4 diagonal incidences M2mix=sum_{u<v}W_uv is exact and at most 2*C4; equality need not hold because aligned diagonals may contribute.

## 2. Exact weighted cut theorem (any finite simple graph)

For ANY subset H of graph vertices, with binary indicator h, define

    Q(H) = sum_{u<v;u,v in H} W_uv = (1/2) h^T W h,
    Cut(H,H^c) = sum_{u in H,v notin H} W_uv.

Then the following is an exact finite-graph identity:

    2Q(H)+Cut(H,H^c)=sum_{u in H}rho_u.              (CUT)

Set M2mix=sum_{u<v}W_uv and E2mix=sum_{u<v}W_uv^2. With t=|H|,
wmax=max_{u<v}W_uv, Cauchy-Schwarz on the choose(t,2)
selected unordered vertex pairs gives the deterministic bounds

    Q(H) <= floor[(sum_{u in H}rho_u)/2],
    Q(H) <= floor sqrt( choose(t,2)*E2mix ),
    Q(H) <= choose(t,2)*wmax,
    Q(H) <= M2mix.                                      (OP-CAP)

All quantities are integers; the square-root cap uses exact integer
isqrt, not floating-point estimates. Every bound holds for arbitrary
graph-adaptive H, including empty H. The row cap uses the TRUE
placement of C4 diagonal mass, not the total number of high
physical vertices alone.

An independent all-graph double-counting representation of rho_u is

    rho_u = sum_{unordered {b,c} subset N(u)}
                # {v !=u : v in N(b) intersect N(c),
                   v mixed with u}.

This counts every C4 containing u exactly once for each eligible
opposite vertex, and does not require the common-endpoint codegree
implementation to be trusted.

For H_k={u:deg_Ghat(u)>=k}, K3-E's source-star tail is EXACTLY Q(H_k)
for k>=3, so

    Bmix <= sum_{k=3}^{Cmax}Q(H_k)
          <= sum_{k=3}^{Cmax} OP-CAP(H_k).            (OP-LAYER)

The first inequality is K3-E's original-source-star bound. In a
FIXED graph where Q(H_k) has already been computed exactly, the
second, relaxed operator bound cannot improve K3-E. It may,
however, be substantially stronger than K3-F1's coarse
choose(H_k,2)*choose(Cmax,2) because it preserves the actual
C4 diagonal placement. Numeric evidence must report both.

Crucial scientific distinction: this is NOT yet a map-independent
all-h bound on E2mix, rho_u or Q(H_k). Those require a new
shared-original-source mixing theorem at the C4-DIAGONAL level,
rather than applying the original first-order incidence spectrum
directly to vertex counts.

## 3. Exact chorded motif extraction from C4-pair overlaps

Reuse K3-C's exact four-square overlap partition, but independently
construct the H-class witness from unordered pairs of distinct C4
edge sets sharing EXACTLY ONE edge and exactly its two vertices.
Their symmetric difference is a simple six-cycle whose common
edge is an antipodal chord. Every six-cycle has at most three
antipodal chords.

For one globally coherent point-pair f and line-pair g, every
Kikuchi edge maps back to ONE original incidence column (p,l).
For each H chorded witness classify its six physical vertices and
six original incidence columns:

  - Hproper: all six FIRST and all six SECOND coordinates distinct.
    Such cycles are exactly accepted D6 by K1; six original columns
    are necessarily distinct.
  - Himproper_distinct: six original incidence columns distinct but
    at least one physical first or second coordinate repeats.
    These may support the full GF5-weighted R3 route, NOT
    automatically the accepted seven-family S.
  - Hrepeated: fewer than six original incidence columns; must be
    excluded from K2's six-DISTINCT-column GF5 count.

These three mutually exclusive classes partition the complete H
count and yield the exact CONDITIONAL lower floors

    D6 >= ceil(Hproper/3),
    C6_distinct_orig_columns >=
         ceil((Hproper+Himproper_distinct)/3).

No loss term is hidden: the repeated-column count is reported
explicitly. A direct independent quadratic C4-pair oracle checks
each overlap and physical/original column class, while the accepted
K3-C overlap oracle verifies H, Hproper and Hdistinct. Accepted K1
six-cycle census verifies the D6 bound, but no inference that
Himproper_distinct belongs to any of the other six accepted
six-motif families is made.

This is a precise chord-to-motif conversion for the H (six-cycle)
component, NOT a conversion of arbitrary B (book) mass to motifs.
K(2,t) remains a universal all-graph counterexample to that
unrestricted conversion. The decisive missing step is an all-h
GQ-specific relation forcing large mixed book mass to produce
enough Hproper or accepted non-D6 motifs after T, K4, improper and
repeated-column charging.

## 4. Falsifiers, numerical diagnostics, acceptance

Reference: research/hyp105_g5e2b3e1k3f2_diagonal_operator.py.
Independent tests: research/test_hyp105_g5e2b3e1k3f2_diagonal_operator.py.

One oracle directly enumerates all C4s by independent oriented
4-walks, places both opposite diagonal weights and compares them
to W_uv and its strengths. A separate neighbor-pair wedge join
recomputes row strength. Independent binary cut tests include
selected stars, empty/full and seeded random vertex subsets;
all integer operator bounds must dominate exact Q(H).

For motif extraction the reference uses shared-edge indexed
C4-pair enumeration, while tests use independent quadratic
all-C4-pair comparisons. Real coherent W(3,2) lex/reverse and
W(3,4) seeded random labelings are checked against K3-C H/Hproper
and K1 proper D6 counts. All budgets fail closed.

Use one dedicated path-limited GitHub-hosted Contract plus the
existing Research/INDEX checks; no duplicate full research matrix,
no local PC requirement. Do not merge without exact-HEAD hosted
SUCCESS, mathematical review and explicit user authorization.

**Next:** K3-G, a shared-original-source C4 diagonal row/energy
packing theorem (or new book-to-seven-motif geometric injection).
The theorem must bound rho_u and E2mix for ALL legal global f,g
with a positive all-h gain. A finite experimental improvement
alone is not a proof. Keep #230/#176/#169 OPEN.
