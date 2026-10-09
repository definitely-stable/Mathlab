# HYP-105 G2 — quadratic three-sum capacity via grid-free linear triple systems

Date: **2026-10-09** · [issue #84](https://github.com/definitely-stable/Mathlab/issues/84) · G1 [weight-two theorem](HYP-105-G1-W2D3-GIRTH8.md).
**RESULT: DERIVED_CLASSICAL, A_set quadratic for w=3,d=3 and characteristic≥5; UNBOUNDED RATIO STILL UNPROVED.**
This is a new deduction in the Mathlab research record, **not** a claim of an original scientific discovery. External grid-free existence is pinned to the Gishboliner–Shapira 2022 theorem. No Rust library or product GO.

## Exact objects, no confusion with linear independence

Let \(\mathbb{F}_q\) be a fixed finite field of characteristic \(p\ge5\). Define \(A_q^{set}(m,w,d)\) and \(A_q^{lin}(m,w,2d)\) as in [LENT-G1A](LENT-001-G1A-PROOF.md):
- nonzero, pairwise distinct columns of support \(\le w\);
- **set**: every sum of distinct columns indexed by an arbitrary subset of size \(\le d\) is unique, including empty and singletons;
- **lin**: every \(\le2d\) distinct columns is linearly independent over the *full coefficient field* \(\mathbb{F}_q\).
Then \(A_q^{lin}\le A_q^{set}\), but these capacities need not be equal.

**Linear 3-graph:** a simple 3-uniform hypergraph \(H=(V,E)\) in which two different triples have at most one common vertex. Each edge \(e\) determines its **unit incidence vector** \(a_e=\mathbf{1}_e\in\mathbb{F}_q^{|V|}\) of hard support exactly 3.

**Grid \(GR_{3\times3}\):** six distinct edges \(L_1,L_2,L_3,R_1,R_2,R_3\), with the three \(L\)-edges pairwise disjoint, the three \(R\)-edges pairwise disjoint, and \(|L_i\cap R_j|=1\) for all \(i,j\). The intersections form exactly nine distinct vertices. Its collision is

    a_{L1}+a_{L2}+a_{L3}=a_{R1}+a_{R2}+a_{R3}.

The grid is NOT the four-edge Pasch configuration, NOT a general (9,6)-configuration, and NOT equivalent to arbitrary six-column field-linear dependence.

## G2 theorem A — exact grid characterization for linear unit triple systems

For every fixed finite field \(\mathbb{F}_q\) of characteristic **at least five**, the unit incidence vectors of a linear 3-uniform hypergraph \(H\) have distinct sums over **all subsets of at most three edges** if and only if \(H\) contains no \(GR_{3\times3}\).

**Proof.** A grid trivially gives a collision of two disjoint 3-edge subsets. Conversely, suppose two different subsets \(S,T\subseteq E\) of at most three edges have the same vector sum. Cancel their shared edges, leaving nonempty disjoint \(S',T'\) with the same sum.

At any coordinate \(v\), the number \(c_S(v)\) of edges of \(S'\) containing \(v\) lies in \(\{0,1,2,3\}\), as does \(c_T(v)\). Since the field characteristic is at least 5, equality modulo \(p\) forces **ordinary integer** equality \(c_S(v)=c_T(v)\), coordinate by coordinate. Summing these degrees over vertices yields \(3|S'|=3|T'|\); write their common cardinality \(r\in\{1,2,3\}\).

Every vertex of every left edge then lies in at least one right edge. Hence the total count of intersections of pairs \((s,t)\in S'\times T'\), including multiplicities, is at least \(3r\) (each of the \(3r\) left incidences must be met on the right). Linearity of \(H\) bounds every such edge-pair intersection by one, so it is at most \(r^2\).

For \(r=1\) or \(2\), \(3r>r^2\), a contradiction. Thus \(r=3\) and the lower and upper bounds both equal 9. Equality forces each of the nine left incidences to have **exactly one** meeting right edge; symmetrically every right incidence has exactly one meeting left edge. Further, all nine pairs of left and right edges meet exactly once. Since the right edges have no shared vertex on any left edge, and all vertices of each right edge occur on a left edge, two right edges cannot share a vertex. Likewise the left edges are pairwise disjoint. This is exactly a \(3\times3\) grid. QED.

**Scope:** This proof is elementary finite combinatorics. It covers fields of characteristic ≥5, including extensions of \(\mathbb F_5\); it does NOT automatically cover fields of characteristic 3 (e.g. \(\mathbb F_3\) or \(\mathbb F_9\)) because degrees 0 and 3 coincide modulo 3. In characteristic 2 the original ASET condition becomes 6-wise linear independence, a separate known model.

## G2 theorem B — exact asymptotic exponent for ASET, weight 3/activity 3

For every **fixed finite field of characteristic ≥5**,

    A_q^{set}(m,3,3) = Θ_q(m²).

**Upper.** Every family injective for subsets of size \(\le3\) is injective through \(\le2\). The self-contained [HYP-002-B finite bound](HYP-002-B-QUADRATIC-THEOREM.md) applies to all fields:

    A_q^{set}(m,3,3) ≤ A_q^{set}(m,3,2) = O_q(m²).

**Lower.** The original Gishboliner–Shapira 2022 theorem constructs *linear 3-uniform hypergraphs on m vertices with \(\Omega(m²)\) edges and no \(3\times3\) grid*. Apply theorem A: their unit incidence edge vectors are support-exactly-three columns and all \(\le3\)-edge subset sums are injective over every fixed field of characteristic at least five. Thus \(A_q^{set}(m,3,3)\ge\Omega(m²)\). Combine bounds. QED.

This **closes the exponent of the numerator** in HYP-105 for the indicated characteristic, not the asymptotic separation conjecture. In particular the headline \("perhaps A_set(m,3,3)=o(m²)"\) is FALSE over these fields due to **2022 prior art**, not a newly proved original construction.

## Denominator and remaining mathematical gap

The best lower bound directly available from the already pinned Lefmann 2005 abstract, for fixed q and k=6,r=3, is

    A_q^{lin}(m,3,6) = Ω_q(m^{(6*3)/(2*(6-1))}) = Ω_q(m^{9/5}).

By monotonicity \(A_q^{lin}\le A_q^{set}=O_q(m²)\), so we currently certify the **interval**

    Ω_q(m^{9/5}) ≤ A_q^{lin}(m,3,6) ≤ O_q(m²).

With the new exact numerator,

    1 ≤ A_q^{set}(m,3,3)/A_q^{lin}(m,3,6) ≤ O_q(m^{1/5}).

**The right-hand bound does not prove the ratio diverges.** Neither the 2022 grid-free paper nor the 2005 sparse parity-check paper proves that their respective extremizers coincide, that the denominator is \(o(m²)\), or that all grid-free constructions are six-wise independent. An original separation theorem would require **a new upper bound** \(A_q^{lin}(m,3,6)=o(m²)\) (at minimum), plus the present quadratic set construction; an \(\Omega(m^{9/5})\) lower bound alone cannot establish this.

### Grid trade vs arbitrary dependence

A grid gives a **\(+1,+1,+1,-1,-1,-1\)** linear dependency, so six-wise independence necessarily forbids grids. But grid-freeness only excludes this specific signed relation within linear unit-incidence hypergraphs; it does not exclude arbitrary six-column dependencies with non-\(\pm1\) coefficients. Therefore replacing \(A_q^{lin}\) by \(A_q^{set}\) in a known coding bound is invalid.

**Do NOT claim** that the Brown–Erdős–Sós (9,6) problem solves our denominator: its configurations are *any six edges spanning ≤9 vertices*, and proving the presence of such a configuration in a dense linear 3-graph would still require proving that a suitable field-linear dependency follows. Likewise dense **grid-free** linear hypergraphs already exist, so forbidding this one 9-vertex/6-edge configuration cannot imply \(o(m²)\) edges.

## Exact independent falsification evidence

[research/test_hyp105_grid.py](../../research/test_hyp105_grid.py) generates the entire affine plane \(AG(2,3)\), comprising **nine points, twelve three-point lines and four parallel classes**. It validates linearity, constructs the distinct three-horizontal versus three-vertical-line grid sum collision over GF(5), independently enumerates every ≤3 sum and every grid present in each of the \(2^{12}=4096\) edge subfamilies. The results should agree *exactly*, including when more than one grid is present. The test is a **finite formal-contract oracle**; it does not reprove the 2022 construction's asymptotic existence theorem.

## Source-to-claim / novelty gate

| Primary work | Original claim verified | Exact transfer/no-transfer |
| --- | --- | --- |
| **LIT-137**: [Gishboliner–Shapira, *Constructing Dense Grid-Free Linear 3-Graphs*, Proc. AMS 2022](https://doi.org/10.1090/proc/15673) | Existence of linear 3-uniform grid-free hypergraphs with \(\Omega(m²)\) edges | Combining this **known construction** with elementary lemma A proves quadratic ASET numerator; does not imply any six-wise independence. |
| **LIT-138**: [Naor–Verstraëte, *Improved bounds on the size of sparse parity check matrices*, ISIT 2005](https://doi.org/10.1109/ISIT.2005.1523645) | Theory and bounds on sparse matrices with any k columns independent; near-optimal upper bound in its model | An arbitrary-coefficient bound for \(A_q^{lin}\) cannot upper-bound \(A_q^{set}\). Publisher-rendered formula contains ambiguity in exponent formatting; **do not use it to claim a sharper specific \((6,3)\) rate without checking the mathematical PDF.** |
| **LIT-139**: [Santos–Tyomkyn, *Brown–Erdős–Sós conjecture in dense triple systems*, arXiv 2025](https://arxiv.org/abs/2508.09841) | The author's 2025 claim proves a high-density case of the Brown–Erdős–Sós conjecture for linear 3-graphs | Density \(>4/5\) of a particular normalization is **not** a general Ω(m²) exclusion, and an arbitrary \((9,6)\) configuration is not automatically a six-edge linear dependency. |
| **LIT-140**: [Frankl–Füredi–Goorevitch–Holzman–Simonyi, *Triangle-Free Triple Systems*, EJC May 2026](https://doi.org/10.37236/14115) | Classifies extremal forbiddance of combinations of four different triangle configurations in 3-uniform hypergraphs | Triangle-free/triple-system extremal results are adjacent source prior art, not an exact theorem for 3-vs-3 signed sum collisions. |
| **LIT-043**: [Lefmann 2005](https://doi.org/10.1017/S0963548304006625) | Sparse parity-check \(A^{lin}\) lower exponent \(9/5\) at k=6,r=3 | Does not upper-bound \(A^{set}\) or prove HYP-105 separation. |

**Evidence labels:** theorem A proven self-contained; theorem B derived using externally reported 2022 existence with abstract-level source verification; publication novelty NOT ESTABLISHED and unlikely for the exponent. CI tests do not verify the cited infinite construction's proof.

## Follow-up G3 — a genuine possibility, but not yet a theorem

Investigate the **6-wise-independent sparse-column denominator** as its own extremal problem. First audit the strongest Naor–Verstraëte 2005/2007 upper results and later improvements with exact k,r,field constraints, then search for either:
1. an \(o(m²)\) upper bound on \(A_q^{lin}(m,3,6)\), which *together* with theorem B would prove a superconstant ratio; OR
2. an \(\Omega(m²)\) six-wise-independent weight-three construction, which would kill the entire \(w=3,d=3\) superconstant separation.

Either would be substantial; a constant-factor witness, more finite solver points, or a generic graph-free source import alone are **not** G3.

**STOP**: never relabel 'grid-free' as 'dependency-free', never claim a new Rust crate, and never transfer \((9,6)\) extremal results without a proved model map. No DELSK/DeltaMeter/ChunkShift changes.
