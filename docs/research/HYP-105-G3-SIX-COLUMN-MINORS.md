# HYP-105 G3 — grid-freeness exactly characterizes six-wise independence

Date: 2026-10-09 · [issue #86](https://github.com/definitely-stable/Mathlab/issues/86) · predecessor [HYP-105 G2](HYP-105-G2-GRID-FREE-QUADRATIC.md).
**SELF-CONTAINED COMPUTER-ASSISTED FINITE CORE CLASSIFICATION + DERIVED CLASSICAL ASYMPTOTIC CONSEQUENCE.** Scientific originality **NOT VERIFIED**. No Lean formalization, Rust API, performance or security claim.

## 1. Statement and complete scope

Let H be any **linear 3-uniform hypergraph** on m vertices: all edges have exactly three vertices, and any two distinct edges share at most one vertex. Give each edge e its **unit incidence column** a_e∈GF(q)^m with entries 0 and 1.

**Theorem G3-A (finite forbidden-configuration criterion, computer-assisted).**
For *every field of prime characteristic p≥5* (including all finite extensions), the family {a_e : e∈E(H)} has **every at-most-six distinct columns linearly independent over GF(q)** if and only if H does not contain a 3×3 grid.

The grid has three pairwise disjoint left triples and three pairwise disjoint right triples, all nine cross-intersections nonempty and distinct. Its alternating ±1 coefficients always make a six-column dependence, proving the easy necessity.

The hard direction is proved by a complete, tiny, **integer arithmetic** enumeration of all minimal dependency cores of at most six triple columns; see proof sections 2–4 and executable enumerator.

**Corollary G3-B (capacity parity, derived from existing dense constructions).**
For every fixed finite field GF(q) of characteristic p≥5,

    A_q^{lin}(m,3,6) = Theta_q(m²)
    A_q^{set}(m,3,3) = Theta_q(m²),

and therefore for all sufficiently large m,

    1 ≤ A_q^{set}(m,3,3) / A_q^{lin}(m,3,6) ≤ C_q.

Here the **upper** bound is Mathlab HYP-002-B for ASET through d=2, and the **lower** bound is Gishboliner–Shapira (Proc. AMS 2022, LIT-137) dense Ω(m²) grid-free *linear* 3-uniform hypergraphs. Our G3-A converts their unit columns directly into k=6 linear-independence witnesses. No claim that the 2022 authors stated this exact capacity corollary, and no claim that the corollary is scientifically original.

This fully refutes the HYP-105 **unbounded set/linear ratio in the w=3,d=3 slice for characteristic≥5**. It does **not** refute the global existential hypothesis for w≥4/d≥4 or for characteristics 2/3, and does not cover arbitrary nonunit column weights or arbitrary 3-support hypergraphs that are not linear.

## 2. Reduction of an arbitrary minimal dependence to finite masks

Suppose some at-most-six selected unit columns are linearly dependent. Delete zero coefficients to obtain a nontrivial relation involving t∈{1,...,6} distinct edges E_1,...,E_t with every coefficient λ_i≠0.

For every original coordinate v occurring in one of these edges, the row equation is

    sum_{i:v in E_i} λ_i = 0.

If exactly one selected edge contained v, this equation would force its coefficient λ_i to vanish, contradicting minimal support. Therefore every *used* vertex lies in **at least two** of the t chosen edges. Unused vertices can be discarded.

Represent each used vertex v by its incidence mask

    S_v = {i∈[t]:v∈E_i}, with |S_v|≥2.

Linearity of H means no pair of selected edge IDs i,j belongs to more than one such mask, because that would mean those two hyperedges share two distinct vertices. In particular identical masks with size≥2 cannot repeat.

Exactly-three-uniform edges impose, for every i∈[t],

    number of masks S_v containing i = 3.

All assumptions are now finite, independent of m, field cardinality or the values of the nonzero λ_i. The collection of masks is considered up to **permutation of vertices** only; edge IDs stay labeled 1..t. Sorting masks by their integer encoding fixes one unique order for every allowed configuration.

The enumerator [research/hyp105_minor.py](../../research/hyp105_minor.py) runs an increasing-mask backtracking search, adding a mask only when it (i) has size≥2, (ii) will not make any column degree exceed 3, and (iii) introduces no second occurrence of any edge-ID pair. When every column degree becomes exactly 3, it outputs precisely one admissible row-unlabeled core. These conditions are necessary and sufficient for the finite model above; therefore the enumeration is **complete**, not a heuristic/SAT sample.

## 3. Certified integer determinant classification

For each admissible core with t edges and v used vertices, construct the v×t zero-one integer incidence matrix M. Consider every t×t square minor of M. Define the **maximal determinantal divisor**

    Δ_t(M) = gcd{det(M_I) : I subset of its rows, |I|=t},

with Δ_t=0 if all minors vanish or v<t. An integer matrix has full column rank over a field of prime characteristic p **iff** at least one maximal minor survives modulo p, i.e.

    rank_{GF(p^s)}(M)=t  <=>  Δ_t(M) mod p != 0.

The code uses fraction-free **Bareiss elimination with exact-divisibility assertions** to compute each integer determinant and exact integer gcd over all maximal minors (early termination at gcd=1 is logically sound).

The exhaustive classification, with counts of row-unlabeled cores indexed by labeled edges, is:

| t selected edges | Δ=0 | Δ=1 | Δ=2 | Δ=3 | Δ=4 | Total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1–3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 1 | 0 | 0 | 1 |
| 5 | 0 | 0 | 0 | 10 | 0 | 10 |
| 6 | **10** | 360 | 60 | 60 | 30 | **520** |

There are **531** nonempty core candidates across t≤6. The only ones with zero maximal determinantal divisor are ten labeled representations of the **3×3 grid**, detected independently from its incidence bipartition: nine degree-two vertex masks, each connecting exactly one left ID and one right ID. All nonzero divisors lie in {1,2,3,4}; none is divisible by any prime p≥5.

Therefore if H is grid-free, every possible minimal dependent core has Δ∈{1,2,3,4}, so it has full column rank over every characteristic p≥5 — contradiction. Together with the grid dependency, this proves theorem G3-A for arbitrary size m.

**Important distinction:** this is a **complete computer-assisted proof of a universal quantified result** because every possible local obstruction is covered by the finite enumeration; it is *not* merely checking finitely many small input instances in hopes of asymptotic generality. The trusted component is the short enumerator + integer determinant implementation + their mathematical completeness arguments. It is **not** independent machine-checking in Lean/Coq and must be peer reviewed before any scientific-originality claim.

## 4. Independent cross-validation

[research/test_hyp105_minor.py](../../research/test_hyp105_minor.py) verifies:

1. Exactly the complete histogram above for t=1..6; zero minors iff a *separate graph-structure test* recognizes 3×3 grid.
2. **Every core independently over primes 2,3,5,7,11,13,17,19,23** using a different modular Gaussian-elimination implementation, with agreement against the determinantal divisor criterion. The theorem then holds for *all* primes p≥5 from the **integer gcd**, not because a finite list of primes was sampled.
3. Fraction-free Bareiss determinants against an entirely separate Leibniz permutation formula for every binary square matrix of order at most three.
4. Expected characteristic-specific border: four-edge cores have divisor 2 (Pasch obstruction in characteristic 2); five-edge cores have divisor 3 (characteristic 3 obstruction); six-edge grids have divisor 0 (every characteristic).
5. Original G2 [finite AG(2,3) grid-vs-set-sums](../../research/test_hyp105_grid.py) remains a separate independent oracle for the *signed set* side.

GitHub-hosted CI checks these finite statements. The 2022 Ω(m²) **existence result is imported from the primary published theorem**, not independently constructed or replicated by the core-classification test.

## 5. G3 decision, research economics and source boundary

The original HYP-105 intuition was "the small signed-subset criterion is strictly weaker than six-wise independence, therefore its optimal sparse capacity might grow asymptotically faster." The first implication (different **finite families**) is true; the second (different **maximal exponents**) is **false for all p≥5, w≤3 at d=3** once G1/G3 are combined:

- w=1, q=5: exact factor 2, not diverging (G1).
- w=2, all fixed fields: matching Θ_q(m^(4/3)) exponents (G1).
- w=3, characteristic p≥5: matching Θ_q(m²) exponents (G3).

This is **not** a proof that the two maximizers always coincide, that leading constants agree, or that decoding/query algorithms are equally efficient. Both capacities are optimized over *all* allowed sparse columns, but the dense grid-free construction provides a stronger witness specifically with **unit support-exactly-three** columns.

**Primary source identities already in catalog** (do not duplicate):
- LIT-137: [Gishboliner–Shapira, *Constructing Dense Grid-Free Linear 3-Graphs* (2022)](https://doi.org/10.1090/proc/15673): quadratic density and grid avoidance.
- LIT-138: [Naor–Verstraëte, *Improved bounds on the size of sparse parity check matrices* (2005)](https://doi.org/10.1109/ISIT.2005.1523645): coding-theory baseline and source-overlap audit.
- LIT-043: [Lefmann 2005 sparse parity-check matrices](https://doi.org/10.1017/S0963548304006625): preexisting k-wise independence extremal techniques.
- LIT-135/136: girth-8 graph constructions and G1 weight-two asymptotics.

**Novelty:** literature is only audited to metadata/selected theorem statements. The exact finite determinantal-divisor characterization is derived here, but a claim that it was never published elsewhere has NOT been verified. The Ω(m²) construction is **explicitly NOT original**. The resulting no-gap exponent is a derived mathematical result, not a new Rust primitive.

**STOP_GAP_W3D3_P>=5** and **NO_GO immediate Rust library**. Next legitimate original theorem search requires **another independently pinned regime**, e.g. larger hard support w≥4, larger active count d≥4, weighted-encoding constant-factor improvements, or a true time/space/decode tradeoff with a real product benchmark. Do not reopen stopped w=3,d=3 purely by renaming a six-edge dependency as a "signed certificate."

No LENT/G2 production changes, and no DELSK, DeltaMeter, ChunkShift modifications.
