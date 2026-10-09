# HYP-105 G4 — the field-characteristic boundary and the next actual capacity gap

Date: 2026-10-09 · [issue #90](https://github.com/definitely-stable/Mathlab/issues/90) · predecessor [G3 six-column minor classification](HYP-105-G3-SIX-COLUMN-MINORS.md).

**Status: PROVED_ELEMENTARY_SUBMODEL / CERTIFIED_FINITE_GF3_OBSTRUCTIONS / SOURCE_NOVELTY_NOT_CLAIMED / FULL_ASET_W4_OPEN.** Do not call this an original mathematical theorem or a practical Rust primitive. All constructions below use unit 0/1 vectors of edges of *linear uniform hypergraphs*, which is strictly narrower than unrestricted ASET allowing arbitrary nonzero weights and overlapping supports.

## G4-A — uniformity greater than activity gives exact sums (restricted model)

**Theorem (elementary).** Fix d≥1, r>d, a finite field \(\mathbb F_q\) of prime characteristic p>d, and any **linear r-uniform hypergraph** H: every edge contains exactly r distinct vertices, and every two distinct edges meet in at most one vertex. To each edge e attach its unit incidence vector \(\mathbf 1_e\in\mathbb F_q^{|V(H)|}\). Then

    S ↦ sum_{e∈S} 1_e

is injective for ALL edge subsets S with |S|≤d (including empty and differently sized subsets).

**Proof.** Suppose two different such edge subsets have the same sum. Cancel shared edges, leaving **disjoint** sets L,R (not both empty), of sizes a,b≤d, still with the same sum. At each vertex v the numbers of left/right incident selected edges belong to {0,…,d}⊂[0,p−1]; equality of their images in characteristic p implies equality **as integers**. If L is nonempty, each of its r·a edge–vertex incidences must be met at least once on the right. The number of left–right edge-pair intersections, counted with multiplicity over vertices, is consequently ≥r a. Hypergraph linearity gives at most ab, one per pair (e∈L,f∈R), so r a≤a b, and r≤b≤d, contradiction. If R was empty, any nonempty left edge already gives a positive vertex count, another contradiction. QED.

There is no dependency on the field's extension degree, the hypergraph's size or density, and no complexity-theoretic lower bound.

**Specific corollary:** over every fixed finite field of characteristic p≥5, *every* linear 4-uniform hypergraph's unit incidence columns have distinct 0-, 1-, 2-, and 3-edge subset sums. A column family with this property can nevertheless fail **six-wise linear independence** (for example over smaller characteristic); ASET and k-wise independence must not be conflated.

## G4-B — the characteristic cutoff is necessary

**Coned p×p grid (general exact countermodel).** Fix any prime p≥2. Introduce p² distinct grid vertices \(v_{ij}\) (0≤i,j<p), and two fresh hubs \(L_*\), \(R_*\). Form p left edges \(L_i=\{L_*\}\cup\{v_{ij}:0≤j<p\}\) and p right edges \(R_j=\{R_*\}\cup\{v_{ij}:0≤i<p\}\). This is a **linear (p+1)-uniform hypergraph**:

- two left edges meet only at L*, two right edges only at R*, and each left/right pair meets at exactly the one corresponding grid vertex;
- the sum of **all p** left incidence columns equals the sum of **all p** right columns over characteristic p, because each grid vertex is counted once on each side, and the relevant hub is counted p≡0 times.

Thus when d=p and r=p+1, the G4-A conclusion fails in characteristic p. In particular p=3 yields a completely explicit **11-vertex 6-edge linear 4-uniform** family for which 3-edge sums collide: **HYP-105 cannot transfer the odd-field G4-A corollary from characteristic≥5 to GF(3)**.

**GF(2) countermodel at r=4,d=3.** Take auxiliary graph \(K_6\) with one perfect matching deleted: it has 6 vertices, 12 edges, every vertex degree 4. Treat the graph's 12 edges as hypergraph *coordinate vertices* and take six hyperedges \(E_i\), each the four auxiliary edges incident to vertex i. Two \(E_i\)'s share at most one coordinate vertex, so this is a **linear 4-uniform hypergraph on 12 coordinates**. Every coordinate occurs in exactly two hyperedges, so summing all six unit incidence columns gives the zero vector over GF(2). Partition the six hyperedges into disjoint sets of three: their three-edge sums coincide. Over GF(5), theorem G4-A prohibits such collisions; the same construction poses no contradiction.

These examples refute an **all-fields** claim. They do not imply that *every* characteristic-3/-2 linear 4-graph is invalid; the ASET property is family-specific below the cutoff.

## G4-C — GF(3), linear 3-graphs: complete local signed obstruction census

The G3 [core enumeration](../../research/hyp105_minor.py) is *field-independent* and complete for **potential minimal dependencies among up to six columns** of a linear 3-uniform hypergraph. Its rows are masks of selected edge IDs, each row degree≥2, every column occurs in three masks, every edge-ID pair co-occurs in at most one mask. The complete canonical row-unlabelled core count is:

- t≤3: **0** cores; t=4: **1** core (minor gcd 2), which is not singular in characteristic 3;
- t=5: **10** cores (all minor gcd 3), each having exactly **two opposite sign assignments** with ≤3 positive and ≤3 negative coefficients, hence exact signed-set collisions in GF(3);
- t=6: **520** cores. Exactly **70** have a ±1 signed collision with three positive and three negative coefficients: **10** are conventional 3×3 grids, **60** are *distinct grid-free* local obstruction cores. The other 450 cannot support a GF(3) signed collision of two ≤3-element sets.

This census is verified by [independent signed-assignment enumeration](../../research/test_hyp105_g4_characteristic.py), not just inferred from the previous **arbitrary-coefficient** minor ranks. A singular determinant does not *automatically* yield a suitably balanced ±1 vector in other parameter ranges.

**Explicit characteristic-3 five-edge 3-versus-2 obstruction** on seven coordinates, with edges

    E0={0,1,2}, E1={0,3,4}, E2={1,3,5}, E3={2,3,6}, E4={4,5,6}.

Every edge has size 3, and every pair of edges meets in at most one vertex. Nonetheless

    1_E0 + 1_E4 = 1_E1 + 1_E2 + 1_E3   over GF(3),

because the center coordinate 3 occurs three times on the right, hence vanishes in GF(3); each other coordinate occurs once on each side. This is **grid-free automatically** because it has only five edges. It does **not** collide over GF(5).

**Universal submodel characterization (computer-assisted).** For unit columns of a linear 3-uniform hypergraph over any field of characteristic 3, exact signed-set three-sum injectivity holds **iff** none of its at-most-six-edge subfamilies contains one of the **10 five-edge or 70 six-edge labeled core types** above (up to row/edge relabeling). The finite core covers all possible collision witnesses because after canceling common IDs and eliminating absent coordinates every coordinate of a minimal signed relation must meet ≥2 chosen edges. Do not claim the 70 configurations form a *minimal-by-containment* forbidden family or that forbidding them gives an established asymptotic Turán exponent; some may contain other forbidden subfamilies when viewed in larger original hypergraphs.

### Current research gap in GF(3)

Does there exist a **quadratically dense family of linear unit 3-graphs excluding all those GF(3) signed obstructions**? If so it supplies \(A_3^{set}(m,3,3)=\Omega(m²)\); if every dense family must contain one, this submodel has o(m²) density. Neither claim follows solely from the 2022 grid-free result or the finite enumeration. Note that **the full ASET extremizer can use nonunit weights or nonlinear support hypergraphs**. The density question is a *separate extremal problem*, not automatically a new result about the full \(A_3^{set}\).

## G4-D — full w=4,d=3 capacities have NOT been solved

Over a fixed finite field (in particular q odd), existing **Lefmann 2005 LIT-043** lower bound for six-wise-independent r=4 columns is

    A_q^{lin}(m,4,6) = Ω_q(m^{12/5}).

Since six-wise independence implies exact three-set sums, this **already exceeds the quadratic exponent** of any *linear* 4-uniform hyperedge family. Therefore the simple linear-unit construction, even dense with Θ(m²) edges, is **not** an asymptotically competitive lower construction for the full ASET optimization at w=4!

**Sharpened derived upper bound via forbidden four- and six-cycles.**

    A_q^{set}(m,4,3) = O_q(m^{8/3}).

**Proof.** Consider the support-exactly-four columns. Each has a unique decomposition `v=L+R`: L contains the first two nonzero (coordinate, coefficient) pairs, and R contains the last two. There are at most `U=(q-1)^2*binom(m,2)=O_q(m²)` possible distinct weighted pairs on the left, and the same on the right. Treat the two sets of signatures as **disjoint bipartite vertex classes**, and represent each support-four column by its unique graph edge (L,R). The graph is simple.

A cycle of length 2h for h=2 or 3 splits into two disjoint alternating h-edge matchings. Each left and right endpoint contributes the **same weighted pair vector once** to each alternating matching. Hence the two different sets of h original columns have identical sums. Exact ASET injectivity up to d=3 forbids both C4 and C6.

The resulting bipartite graph has girth at least eight and at most 2U=O_q(m²) vertices. The elementary girth-eight Moore/BFS upper bound used in [HYP-105 G1](HYP-105-G1-W2D3-GIRTH8.md) gives at most `O_q((m²)^(4/3))=O_q(m^(8/3))` edges, hence that many support-four columns. Columns of support≤3 themselves form an ASET subfamily through d=2, so [HYP-002-B](HYP-002-B-QUADRATIC-THEOREM.md) bounds their number by O_q(m²). Sum these counts. QED.

The graph estimate is pinned to **LIT-148**, [Shlomo Hoory, *The Size of Bipartite Graphs with a Given Girth* (JCTB 2002)](https://doi.org/10.1006/jctb.2002.2123): bipartite girth extremal bounds apply to the two-pair factor graph. This is preexisting graph theory, not original to HYP-105.

The C6 exclusion is **essential**: using only C4 would produce merely O_q(m³). The upper bound holds in **every characteristic**, because alternating endpoint sums cancel in any abelian additive group. This is an application of classical girth extremal estimates, **not** a claimed new graph theorem.

Therefore the precise source-backed **full-capacity sandwich**, sharper than the previous m³ note, is

    Ω_q(m^{12/5}) ≤ A_q^{lin}(m,4,6)
                  ≤ A_q^{set}(m,4,3) ≤ O_q(m^{8/3}).

The remaining exponent interval is **8/3−12/5=4/15**; it is an open interval in known upper/lower bounds, **not** evidence of an actual growing capacity ratio.

Neither the r=4 grid-free hypergraph theorem nor the elementary G4-A lemma closes this gap. A strict exponent gap in currently *known bounds* is NOT evidence of a true asymptotic separation. A genuine next theorem needs a better exponent for either side, or an explicit constructed family with provably unequal optimal growth.

## Primary literature and model-transfer audit

- **LIT-145**: [Pohoata 2026, *Grid-free linear hypergraphs via Cayley-Bacharach*](https://arxiv.org/abs/2602.14716) gives Θ_r(m²) edge constructions for r-uniform linear hypergraphs with no *r×r* grid, for all r≥3. **For r=4 that grid uses 8 hyperedges (4+4)**. It does not characterize six-edge three-sum collisions, nor provide the superquadratic full ASET rate Ω(m^(12/5)).
- **LIT-146**: [Gyárfás–Sárközy 2022, *The linear Turán number of small triple systems or why is the wicket interesting?*](https://doi.org/10.1016/j.disc.2022.113025) covers small linear 3-graph forbidden configurations, relevant to the characteristic-three obstruction audit. A **wicket** has five edges on **nine** grid vertices; our 5-edge GF(3) obstruction has **seven** vertices and is NOT the wicket.
- **LIT-147**: [Solymosi 2024, *Wickets in 3-uniform hypergraphs*](https://doi.org/10.1016/j.disc.2024.114029) proves a wicket-free linear triple system has o(m²) edges. **This result cannot be transferred** to forbidding our different 7-vertex five-edge obstruction without a proved containment/reduction.
- **LIT-043** Lefmann 2005 and **LIT-138** Naor–Verstraëte 2005 already work directly with weighted sparse k-wise field-linear independence; their results are not automatically new ASET theorems.

**Source checks:** official abstracts/publisher pages/author manuscripts checked for model identities, not full reproduction of each paper's proof. No new original theorem or practical decoding guarantee asserted. Further research only after avoiding these model mismatches.

## Reproducibility and decision

[Standard-library-only tests](../../research/test_hyp105_g4_characteristic.py) check arbitrary prime p coned grids, the 12-coordinate GF(2) 4-graph, GF(5)/GF(7) three-sum injectivity in an affine 4-partite linear family, GF(3) explicit 2-vs-3 five-edge witness, and the complete GF(3) signed-collision census for all 531 original G3 core types.

G4 decision: **ACCEPT elementary submodel char threshold + finite characteristic-3 signed obstruction classification; STOP false all-field and false w4 quadratic-capacity claims; FULL_W4_CAPACITY_OPEN / GF3_DENSITY_OPEN.** No new Rust primitive, changes in DELSK/DeltaMeter/ChunkShift, or unsourced novelty announcements.
