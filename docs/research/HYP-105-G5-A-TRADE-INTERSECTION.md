# HYP-105 G5-A — trade intersection beyond girth-eight, and 2026 literature gate

Date: 2026-10-09 · parent [issue #95](https://github.com/definitely-stable/Mathlab/issues/95).
**Status:** PROVED_ELEMENTARY_COUNTERMODEL / EXACT_SPLIT_TRADE_CRITERION / STOP_GIRTH_SUFFICIENCY / W4_EXPONENT_OPEN.
No novel fundamental theorem claimed, no certified exponent improvement, no Rust product authorization; Mathlab only.

## 1. Frozen full model and what G4 actually proved

Let \(A_q^{set}(m,4,3)\) maximize distinct nonzero GF(q)^m columns with at most four nonzero coordinates whose sums over **all distinct subsets of cardinality 0,1,2,3** are pairwise different, including comparisons of different cardinalities. Let \(A_q^{lin}(m,4,6)\) demand independence of every at-most-six columns under arbitrary coefficients. The field q is held fixed.

G4 [proof](HYP-105-G4-CHARACTERISTIC-W4.md) gave

    Ω_q(m^(12/5)) ≤ A_q^lin(m,4,6) ≤ A_q^set(m,4,3) ≤ O_q(m^(8/3)).

The left bound is old Lefmann (LIT-043); the right follows by taking *each support-exactly-four column* \`a\`, canonically splitting its first two nonzero coordinate/coefficient pairs \`L(a)\` and final two \`R(a)\`. ASET forbids C4 and C6 in the **bipartite graph whose vertices are distinct two-sparse weighted vector signatures** \`L(a),R(a)\`, because alternating cycles force a two-vs-two or three-vs-three sum collision.

**Warning:** G4 proves \`ASET => factor graph girth ≥8\` only. The converse was never proved and is **false**.

## 2. G5-A theorem — a matching factor graph can contain an ASET 3-sum collision

**Exact all-fields countermodel.** Let \(m=12\). For each \(i\in\mathbb{Z}/6\mathbb{Z}\), define the four-sparse, all-one GF(q) column

    a_i = e_i + e_{(i+1) mod 6}
          + e_{6+i} + e_{6+((i+1) mod 6)}.

Every column has four *distinct* nonzero coordinates. With coordinate order 0,...,11, the canonical first-two and last-two support signatures are

    L_i = e_i + e_{(i+1) mod 6}       (supported in [0,5]),
    R_i = e_{6+i} + e_{6+((i+1) mod 6)} (supported in [6,11]).

Both sets \(\{L_i\}_{i=0}^5\) and \(\{R_i\}_{i=0}^5\) have six distinct pair signatures; therefore the G4 factor graph has six **disjoint edges** and contains **no cycle of any length** (stronger than girth eight).

Yet for every field, using ordinary integer coordinate incidence counts on both halves,

    a_0 + a_2 + a_4 = a_1 + a_3 + a_5
                   = sum_{j=0}^{11} e_j.

The two disjoint 3-element subsets produce the same exact sum. Therefore the canonical pair-graph girth condition is **not sufficient** even for six all-one columns and even for a matching factor graph.

This refutes an invalid attempted transfer: one C4/C6-free graph on at most O(m²) pair signatures \(\not\Rightarrow\) a valid ASET family of that edge cardinality. Any proposed \(\Omega(m^{8/3})\) ASET lower bound built *only* from a dense girth-eight factor graph must separately prove **absence of coordinate-level signed trades**.

The countermodel is an elementary double-cycle identity, not an original scientific discovery.

## 3. Exact projection-trade characterization in the *globally separated* 2+2 model

Freeze a partition of coordinates \([m]=P\sqcup Q\). Let each column \(a_i=\ell_i+r_i\), with \(\ell_i\) supported on P, \(r_i\) on Q; this encompasses globally separated canonical first/last two-sparse columns. No condition of support uniqueness on either side is needed for this identity.

Let \(\mathcal T_d\) be the family of integer sign sequences \(x\in\{-1,0,+1\}^N\setminus\{0\}\) with at most \(d\) entries equal to +1 and at most \(d\) equal to -1. For each projection define:

    K_P = {x∈T_d : sum_i x_i ell_i = 0 in GF(q)^P},
    K_Q = {x∈T_d : sum_i x_i r_i  = 0 in GF(q)^Q}.

**Theorem (elementary exact characterization):**

    F has distinct subset sums through d   <=>   K_P ∩ K_Q = ∅.

**Proof.** A collision \(sum_{i∈S} a_i=sum_{i∈T} a_i\) between two distinct subsets of cardinalities≤d yields a nonzero sign pattern x after cancelling shared IDs. Conversely each x∈T_d has positive and negative supports S,T of size≤d, giving exactly that collision. Because the P/Q coordinate subspaces are disjoint, sum x_i a_i=0 iff both projected sums separately vanish. QED.

This is an **exact combinatorial condition**, not a new lower bound. In particular:
- a bipartite C4/C6 cycle yields an x in the intersection because the two alternating matchings match the *pair signatures* exactly;
- a pair of *coordinate-level* cycles can yield x in the intersection even if the pair-signature factor graph is a matching (Section 2);
- achieving high density requires controlling the intersection of **signed trade families**, not merely ordinary short cycles in the factor graph.

**Model boundary:** This P/Q decomposition is global. For general canonical first-two/last-two splits the coordinate sets overlap across *different columns*, and the two projections need not land in disjoint coordinate subspaces. Do not apply \`K_P ∩ K_Q\` to the entire unrestricted canonical-split graph without first establishing such a global partition.

## 4. Union-free hypergraphs: 2026 result is adjacent, not a solution

For a 4-uniform **unit-incidence** hypergraph H, say H is 3-union-free when the *unions of all distinct subsets of ≤3 edges* differ. If field characteristic \(p>3\), every coordinate's incidence sum of ≤3 edges equals an ordinary count in {0,1,2,3}, so a nonzero coordinate in the sum is exactly a vertex in the union. Consequently,

    3-union-free 4-uniform unit H  =>  H satisfies ASET d=3 over GF(q), char p>3.

The reverse implication is FALSE **even for 4-uniform unit columns**. On coordinates {0,1,2,3,4} take three distinct 4-edges \(a=\{0,1,3,4\}\), \(b=\{1,2,3,4\}\), \(c=\{0,2,3,4\}\). These are a triangle of two-coordinate edges with two common hub vertices added to every edge. All eight subset sums through three edges are distinct over GF(5): the hub multiplicity identifies cardinality (0..3), and within each fixed cardinality the original triangle-coordinate counts separate subsets. But the unions of all different 2-edge subsets equal {0,1,2,3,4}. Thus **ASET does not imply 3-union-free even in the relevant r=4 submodel**. This source-model distinction is independently tested.

**Previously indexed 2026 primary literature (LIT-005, no duplicate import):** Liu–Shangguan–Zhang, *Sharp asymptotic bounds for uniform union-free hypergraphs*, arXiv:2605.11949v3 (revised July 2026), already represented by catalog LIT-005 under its **earlier-version title** *Sharp bounds for uniform union-free hypergraphs*. The same arXiv identity must not be indexed a second time. Theorem 1.1 explicitly **EXCEPTS** (t,r)=(3,4) from the new leading-constant asymptotic; it must NOT be cited as providing a sharp constant for U_3(m,4). The earlier Shangguan–Tamo 2020/21 source (LIT-151) already yields the correct exponent:

    U_3(m,4) = Theta(m²),

since their lower \(\Omega(m^{r/(t-1)})\) and known cover-free upper \(O(m^{\lceil r/(t-1)\rceil})\) both give exponent 2 for (t,r)=(3,4). Note this exponent is **far below** the existing general ASET/linear-independent lower \(\Omega_q(m^{12/5})\). Even sharp union-free r4 constructions are **asymptotically inadequate** for the unrestricted ASET capacity target.

The 2026 paper's locally sparse packings are relevant to potential construction methods, but the theorem alone **neither improves nor disproves** \(\Omega(m^{12/5})\le ASET\le O(m^{8/3})\).

## 5. Other source-model comparisons and novelty controls

| Source | What it actually establishes | G5 transfer limit |
| --- | --- | --- |
| LIT-152 [Naor–Verstraëte 2008, *Parity check matrices and product representations of squares*](https://doi.org/10.1007/s00493-008-2195-2) | Full journal treatment of sparse arbitrary-coefficient k-wise independent column bounds and graph-cycle reductions | Cannot upper-bound ASET simply by replacing signed ±1 relations with arbitrary field coefficients. Author abstract has poorly formatted exponent; **no claim of an improved k=6,r=4 bound until original complete theorem checked**. |
| LIT-153 [Alfarano 2026, *Additive codes arising from hypergraphs*](https://arxiv.org/abs/2609.39680) | Hypergraphic polymatroids, critical exponents and quasi-MDS conditions for additive/folded codes | Critical exponent/dual minimum folded distance is **not** the number of distinct sums of ≤3 sparse columns; thematic overlap, not a theorem transfer. |
| Existing LIT-043 [Lefmann 2005](https://doi.org/10.1017/S0963548304006625) | For k=6,r=4 every fixed GF(q), \(\Omega_q(m^{12/5})\) six-wise independent columns | This is a genuine ASET construction lower by model inclusion; unchanged. |
| Existing LIT-148 [Hoory 2002](https://doi.org/10.1006/jctb.2002.2123) | Girth-eight bipartite graph edge upper | Gives only the upper necessary condition, NOT a converse or dense ASET construction. |

Neither a new exponent nor a growing ratio has been proved in G5-A. The new **finite matching countermodel** is a model-quality and source-gate improvement.

## 6. Reproducibility, decision and next genuine mathematics

[research/test_hyp105_g5_trades.py](../../research/test_hyp105_g5_trades.py) verifies:
1. Six length-12 4-sparse all-one columns with disjoint weighted-pair graph edges; direct zero-C4/C6 graph oracle.
2. Independently enumerated all GF(2), GF(3), GF(5), GF(7), GF(11) subset-sum signatures through three, exhibiting the expected 3-vs-3 collision.
3. The exact separated-projection trade intersection equivalence on many bounded families, independently comparing direct subcube sums vs bounded signed kernel intersection.
4. A three-edge **4-uniform** doubled-hub triangle that is ASET over GF(5) but not union-free.

**Gate:** STOP_GRAPH_GIRTH_SUFFICIENCY / STOP_UNION_FREE_SUBSTITUTE / OPEN_FULL_WEIGHT4_EXPONENT_AND_DENOMINATOR. Scientific originality unverified. G5 parent #95 remains OPEN for the genuine asymptotic theorem search. No changes to other repos, no Rust implementation, no claim about memory/decode optimality, no full published-paper proof reproduction.
