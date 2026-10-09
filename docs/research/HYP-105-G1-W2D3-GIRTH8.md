# HYP-105 G1 — Fixed weight two: asymptotic capacity parity at d=3

Date: 2026-10-09 · [issue #80](https://github.com/definitely-stable/Mathlab/issues/80) · Mathlab only.
**DERIVED_CLASSICAL PROOF / NEW TO OUR AUDIT, NOT ORIGINAL SCIENTIFIC THEOREM.** This builds from known graph extremal bounds and generalized-quadrangle constructions, **not** a new exponent, cryptographic theorem or Rust authorization. HYP-105's existential conjecture for *other* w,d is **NOT** refuted.

## Definitions and model

Let q be an arbitrary fixed finite prime power (for original HYP-105, q is odd). For m≥1, finite family F of nonzero, distinct column vectors in GF(q)^m with at most w nonzero entries per vector:

- A_set(q,m,w,d): maximum N for which S -> sum_{a in S} a is injective for **all subsets S⊆F with |S|≤d**, including empty/singleton/different cardinalities. No repeated identifiers or arbitrary coefficients.
- A_lin(q,m,w,k): maximum N for which every at-most-k element subfamily of columns is linearly independent over GF(q), i.e. no nonzero coefficient relation with support≤k. For N<k, still demand independence of all available columns.
- For all q,m,w,d, A_lin(q,m,w,2d) ≤ A_set(q,m,w,d). Proof: subtract colliding subset sums and cancel shared columns to obtain a nonzero relation with at most 2d nonzero coefficients ±1.

Use distinct symbols q_field and s_geometry: geometric q from the external sources is a *construction order s*, not the GF(q_field) used for vector arithmetic.

## General d≥2 upper bound (elementary reduction to girth)

**Lemma.** For fixed q and integer d≥2:

    A_set(q,m,2,d) = O_{q,d}(m^{1+1/d}).

**Proof.** Columns of support one contribute ≤(q-1)m; support-zero is disallowed. Among the N2 support-exactly-two columns, independently place each coordinate into L or R with probability 1/2. There is a cut retaining at least N2/2 crossing columns. For crossing column with one coordinate on L and one on R, its coefficient pair (a,b) belongs to (GF(q)^*)² of size (q-1)². One pair labels ≥N2/[2(q-1)²] columns. Because full vectors are distinct, these columns form a simple undirected bipartite graph G on ≤m coordinate vertices (at most one edge per pair).

If G contains a cycle of length 2h with 2≤h≤d, the two disjoint alternating h-edge matchings on that cycle give equal vector sums: each incident L vertex receives exactly coefficient a, each R vertex exactly coefficient b, from either matching. That would violate A_set injectivity through d. Thus G has NO cycle of length ≤2d (it is bipartite, so all cycles are even), i.e. girth≥2d+2.

A finite graph on m vertices, girth≥2d+2 and E edges, satisfies E=O_d(m^{1+1/d}): if average degree exceeds 2D, iterative deletion of vertices with degree below D leaves a nonempty subgraph with minimum degree ≥D. Starting from any vertex in this subgraph, all non-backtracking paths of length ≤d form a tree (a collision would give a cycle of length≤2d); for D≥2 at least D(D-1)^{d-1} distinct vertices appear at depth d. So m≥D(D-1)^{d-1} and D=O_d(m^{1/d}). Therefore original average degree O(m^{1/d}), E=O_d(m^{1+1/d}). Hence N2≤2(q-1)² O_d(m^{1+1/d}), and adding O_q(m) singleton columns proves the lemma. QED.

The finite-color reduction and standard Moore/girth BFS estimate are elementary. THIS IS NOT A DISCOVERY OF THE general even-cycle extremal bound; sharp constants require separate literature.

## Exact asymptotic theorem for w=2,d=3

**Theorem (derived classical).** For every fixed finite field GF(q) with q≥2,

    A_lin(q,m,2,6) = Θ_q(m^{4/3})
    A_set(q,m,2,3) = Θ_q(m^{4/3})

and thus

    1 ≤ A_set(q,m,2,3)/A_lin(q,m,2,6) ≤ C_q

for a finite constant C_q and all sufficiently large m.

**Upper:** general lemma at d=3 bounds A_set=O_q(m^{4/3}); A_lin≤A_set also.

**Lower:** For every geometric prime power s, the incidence graph of a generalized quadrangle of order (s,s) is simple, bipartite, (s+1)-regular, girth 8 with

    M_s = 2(s+1)(s²+1) vertices,
    E_s = (s+1)²(s²+1) edges.

This is a **known** construction; see Abreu–Araujo-Pardo–Balbuena–Labbate, 2011, and Wenger 1991. Index its vertices by rows; for each edge e=(u,v) choose a column a_e=e_u-e_v in GF(q)^M_s (for characteristic two, minus equals plus). Each column has support exactly 2; distinct edges give distinct columns. Any subset of at most six edges is acyclic because girth=8. The oriented incidence columns of a forest are linearly independent over **every** field: in any putative nonzero relation, choose a leaf vertex of the forest; its unique incident edge forces that coefficient to zero; peel the forest inductively. Hence every ≤6 columns are independent.

For M_s=Θ(s³), E_s=Θ(s⁴)=Θ(M_s^{4/3}). To obtain the lower bound for **all** sufficiently large m rather than only a subsequence, use s=2^t ≤c m^{1/3} maximal with M_s≤m; geometric powers of two grow at bounded ratio, so s=Ω(m^{1/3}). Pad with zero rows to dimension m. This yields A_lin(q,m,2,6)=Ω(m^{4/3}). Combine with the upper bounds. QED.

**Consequences:**
1. An asymptotic unbounded A_set/A_lin ratio is **FALSE** for the previously promising entire slice (fixed q, w=2,d=3), including q=5. The original existential HYP-105 for *some* w≥3 or d≥4 is **still OPEN**.
2. This derivation extends the Mathlab d=2 exponent Θ(m^{3/2}) to a d=3 **known graph-girth exponent**; it must never be promoted as a new fundamental encoding theorem.
3. For w=2 and any larger fixed d, only the O_{q,d}(m^{1+1/d}) general upper follows from this proof. A matching general lower for all d is **NOT** claimed. This gets entangled with classical forbidden-short-cycle / high-girth graph constructions.
4. Even when ratios of maximal capacities differ by only a constant factor, individual finite instances, coefficients and fast decoding may differ. This theorem proves no new practical encoding or performance advantage.

## Independent tiny exact corner: GF(5), w=1, d=3

    A_set(5,m,1,3)=2m, A_lin(5,m,1,6)=m for all m≥1.

**Proof:** Each coordinate can hold no more than two different nonzero scalar columns: three would generate 2³=8 distinct subsets, but their sums live in only five scalar values. For each coordinate use coefficients 1 and 2; all per-coordinate sums of their two possible columns are 0,1,2,3 and distinct, so across coordinates every subset sum is injective, even without the |S|≤3 constraint. Therefore A_set=2m. Linear independence forbids two columns supported on the same coordinate, and m independent standard basis vectors attain the bound. Thus the ratio is exactly **2**, not unbounded. QED.

This is not a novel claim; it is an elementary calibration that reveals why the original finite GF(5) witness does not imply growth.

## Primary sources and strict claim boundaries

| Source | Established source-level fact | Non-transfer |
| --- | --- | --- |
| [Wenger 1991, *Extremal graphs with no C4's, C6's, or C10's*](https://doi.org/10.1016/0095-8956(91)90097-4), new LIT-127 | Infinite algebraic graph constructions avoiding short even cycles; groundwork for dense girth constructions | Not a proof of a novel ASET capacity theorem or a general algebraic decoding speedup |
| [Abreu et al., 2011, *An explicit formula for obtaining (q+1,8)-cages and others small regular graphs of girth 8*](https://arxiv.org/abs/1111.3279), new LIT-128 | Explicit girth-8 cages for geometric prime-power order and an independent construction reference | Geometric order s is NOT the vector coefficient field q; the transfer goes via edge incidence |
| [Lefmann 2005, *Sparse Parity-Check Matrices over GF(q)*](https://doi.org/10.1017/S0963548304006625), existing LIT-043 | Direct prior art for k-wise independence with support cap r; broad d=2 exponents already known | Generic lower-bound exponent at k=6,r=2 may be weaker than these explicit girth-8 constructions; do not misquote the stronger special-case bound as Lefmann's exact result |
| [Mathlab THEOREM-GAP-004](THEOREM-GAP-004-FOUR-STAGE-AUDIT.md), existing | HYP-001/002 exponent prior-art and exactly why arbitrary-coefficient linear independence is stronger than additive subset injectivity | The earlier 2-column GF(5) witness gives ONLY finite separation, no growing asymptotic ratio |

These are peer-reviewed 1991/2005 source records and an original 2011 author preprint; full source proofs have not been independently formalized. Our elementary reductions above are self-contained conditional on the known existence of generalized quadrangles.

## Reproducibility and no false promotions

[Independent exact finite tests](../../research/test_hyp105_girth.py) build the W(3,2) symplectic quadrangle using 15 nonzero GF(2)^4 projective points and all 15 totally isotropic lines. The resulting incidence graph has 30 vertices, 45 edges, all degrees 3 and girth 8. Enumerating every ≤3 edge subset gives distinct sums of signed edge-incidence vectors modulo 5. Additional independent graph tests verify that even cycles C4,C6 create collision via alternating matchings, as required by upper-bound reduction. No attempt to prove an asymptotic geometry-existence theorem solely from a 30-vertex finite test.

**Gate:** STOP HYP-105 fixed-q w=2,d=3 *unbounded ratio* as REFUTED_BY_CLASSICAL_ASYMPTOTICS. Do not stop all HYP-105 cases; next test w=3 or d=4 with matched denominator lower bounds and a source-to-theorem matrix BEFORE heavy enumeration. No Rust, DELSK, DeltaMeter, ChunkShift or production changes.
