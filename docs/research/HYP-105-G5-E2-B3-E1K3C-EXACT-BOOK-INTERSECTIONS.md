# HYP-105 E1-K3-C — exact C4 book decomposition and GQ pencil cap

Date: 2026-10-11. Root issue #230, stacked child of PR #367 at parent HEAD d51f3c575ef8d633c3d62cece0cd91d55009dd7f, inherited K1/K2 from PR #366. No main changes.

**RESTRICTED_THEOREM_C_ALL_GRAPH_BOOK_IDENTITY / RESTRICTED_THEOREM_C_ALL_h_GQ_ALIGNED_CAP / OPEN_WITH_FORMAL_BLOCKER_MIXED_BOOKS.** No universal s^6 floor, Branch A/B, full R3 or ASET conclusion.

## 1. All-graph exact intersection theorem

For a finite simple undirected graph, let Q be the set of undirected 4-cycles (each is one edge set), c4(e) the number of 4-cycles through edge e and c(u,v)=|N(u) intersection N(v)|. Define A=sum_e binom(c4(e),2).

Two distinct squares sharing an edge have exactly one of four intersection signatures (shared edges, shared vertices):

* (1,2): H, a six-cycle with its antipodal chord given by the shared edge.
* (2,3): B, a genuine two-edge-path book.
* (1,3): T, a triangle-hook overlap.
* (2,4): K, two distinct 4-cycles inside one K4.

Any other signature is impossible: distinct 4-cycles cannot share 3 edges; two disjoint common edges require the same 4-vertex support. A counts each pair with multiplicity equal to its common-edge count, hence A=H+2B+T+2K.

For any unordered {u,v}, every triple of common neighbors makes EXACTLY three pairs of distinct squares sharing the two-edge path through one of the chosen triple vertices. Conversely every B pair has a unique pair of opposite endpoints and such a triple, hence

    B = 3 * sum_{u<v} binom(c(u,v),3).

Every K4 clique has three Hamiltonian C4s, hence three C4 pairs sharing opposite edges, and every K-type pair comes from a K4. Thus K=3*number_of_K4_cliques. The final universal exact identity is

    A = H + 6*sum_{u<v} binom(c(u,v),3) + T + 6*number_of_K4_cliques.

For m=|E|>0 and q=|Q|, Jensen yields A>=8*q^2/m-2*q. This is a conditional quantitative bound ONLY; the cubic book moment and triangle-hooks remain a-priori uncontrolled.

## 2. Chord-to-six-cycle lift

Every H pair produces a simple C6 from the symmetric difference of its two C4 edge sets; their unique shared edge is an antipodal chord. Every C6 has at most three such chords. Therefore H<=3*C6 and C6>=ceil(H/3).

For GQ Kikuchi Ghat every graph edge has a unique ORIGINAL (point,line) incidence. The implementation reconstructs it by independent inverse physical pair labels. H_proper counts the H cycles with 6 distinct first AND 6 distinct second physical vertex coordinates. By the accepted K1 bijection, H_proper<=3*D6. H_distinct counts H cycles with six different ORIGINAL incidence columns and bounds distinct-column C6 witnesses; applying K2 GF5 weights requires its separate multiplicity gate. H_proper<=H_distinct.

For total cycles, the exact-book-corrected conditional floor is

    3*C6 >= 8*C4^2/m - 2*C4
                  - 6*sum binom(c(u,v),3) - T - 6*K4.

This is NOT guaranteed positive. In particular pure K(2,t) books have H=0 while B grows cubically.

## 3. All-h GQ-aligned-codegree theorem

For every s=2^h, h>=1, genuine W(3,s) and arbitrary globally coherent injective physical label maps f,g into K_a, let Ghat be the Kikuchi graph on [a]x[a]. If two DISTINCT Ghat vertices share the first physical coordinate, u=(x,y), v=(x,y'), fix a common neighbor (z,t). Both contributing incidences share ORIGINAL point F_{xz}, but use ORIGINAL distinct lines G_{yt},G_{y't}. For a fixed t, two distinct original lines intersect in at most ONE original point, hence at most one z can give such a common neighbor. Since t differs from both y,y', at most a-2 t remain. Therefore

    c_Ghat((x,y),(x,y')) <= a-2.

By original point pair / unique common line duality, equally

    c_Ghat((x,y),(x',y)) <= a-2.

The proof does NOT assume symmetry of arbitrary physical labels; missing physical edges contribute zero. An independent ORIGINAL incidence contraction is checked against the Kikuchi adjacency result.

As there are a^2(a-1) unordered vertex pairs sharing exactly one physical coordinate, their cubic contribution is at most

    sum_aligned binom(c(u,v),3)
       <= a^2(a-1)*binom(a-2,3).

This valid all-h necessary bound is too coarse for the asymptotic problem. Pairs with BOTH coordinates different, the mixed book cubic moment, T triangle-hooks, K4, and repeated-column cycle losses remain uncontrolled.

## 4. Independent evidence and acceptance

Reference: research/hyp105_g5e2b3e1k3c_book_packing.py.
Independent tests: research/test_hyp105_g5e2b3e1k3c_book_packing.py.
Tests enumerate 4-cycles by an independent closed-walk oracle, compare all unordered square pairs and their intersections, compare cubic codegree and independent clique formulae, test K(2,t), K4 and seeded random graphs, then true global W(3,2) and W(3,4) Kikuchi graphs including full C6/D6 censuses and original incidence star contractions. Budgets fail closed.

A single GitHub-hosted path-limited Contract runs K3-C without another full CI matrix; Research and INDEX are inherited. No production changes, no PR merge authorization. Scope remains RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER for issue #230.

Next slice K3-D requires an all-h GQ-specific bound for MIXED books and triangle hooks, or an explicit injective/multiplicity-controlled conversion to accepted six-incidence motifs. Neither the universal book identity nor the coordinate-aligned cap by itself proves Omega(s^6).
