# HYP-105 G5-B — Girth-eight pair-graph relaxation has sharp exponent, but not ASET

Date: 2026-10-09 · [issue #103](https://github.com/definitely-stable/Mathlab/issues/103) · parent [HYP-105 G5 #95](https://github.com/definitely-stable/Mathlab/issues/95) · predecessor [G5-A](HYP-105-G5-A-TRADE-INTERSECTION.md).

**DERIVED_CLASSICAL / GRAPH_RELAXATION_SHARP / NOT_ASET_LOWER / NO_GROWING_RATIO_PROOF.** Scientific originality **NOT ESTABLISHED**. The theorem isolates a false research strategy; it does not improve the proven exponent bound on full four-sparse exact three-sum families.

## 1. Frozen full mathematical objects

For a fixed finite field GF(q), \(A_q^{set}(m,4,3)\) counts the largest set of distinct, nonzero vectors of support at most four whose sums over every distinct subset of cardinality at most three (including the empty subset) are pairwise different. \(A_q^{lin}(m,4,6)\) requires linear independence of every at-most-six columns under arbitrary GF(q) coefficients.

Mathlab's [G4 proof](HYP-105-G4-CHARACTERISTIC-W4.md) established the necessary condition that the **canonical weighted 2+2 factor graph** of the support-exactly-four columns in any ASET family has **no C4 or C6**. This and the classical girth-eight graph extremal bound give

    Ω_q(m^(12/5) (log m)^(1/5)) ≤ A_q^lin(m,4,6)
                  ≤ A_q^set(m,4,3) ≤ O_q(m^(8/3)).

The upper bound is a theorem about ASET. The hypothesis that its graph-only relaxation is sufficient to construct ASET families is **FALSE**, as proved in [G5-A](HYP-105-G5-A-TRADE-INTERSECTION.md). G5-B quantifies how misleading that relaxation can be.

## 2. Theorem G5-B1 — every bipartite graph is a canonical pair factor graph

**Statement.** Fix integers a,b≥2. Let G=(X⊔Y,E) be any finite **simple bipartite graph** with

    |X| ≤ binom(a,2),   |Y| ≤ binom(b,2).

Over **every** finite field GF(q), including characteristic 2, there exists a family of |E| pairwise distinct **unit** support-exactly-four columns in GF(q)^(a+b) whose canonical 2+2 factor graph is isomorphic to G **after deleting isolated vertices**. In particular, every simple bipartite graph *without* isolated vertices is realized exactly.

**Proof.** Partition the m=a+b ordered coordinates into P={0,...,a-1} and Q={a,...,a+b-1}. Inject X into the two-element subsets of P by \(\phi:X\hookrightarrow\binom{P}{2}\) and Y into the two-element subsets of Q by \(\psi:Y\hookrightarrow\binom{Q}{2}\). For every graph edge (x,y), define

    v_xy = ∑_{i∈φ(x)} e_i + ∑_{j∈ψ(y)} e_j.

Each v_xy has exactly four distinct nonzero entries equal to 1 in GF(q). Its **first two nonzero coordinates** are precisely \(\phi(x)\), its **last two** are \(\psi(y)\). Thus the canonical factor edge is exactly (\(\phi(x),\psi(y)\)). Injectivity of the two vertex maps and simplicity of G imply distinct original edges produce distinct columns. The graph induced by the actually occurring factor edges is isomorphic to G with isolates deleted. QED.

**What this does and does not prove:**
- Even the ordered-support and globally-separated-coordinate constraints of canonical factorization impose **no extra restriction on which finite bipartite graphs occur** beyond part sizes, when 4-support/unit columns are allowed.
- It does **not** assert that arbitrary realized G yields a family with unique subset sums. Graph-girth is **necessary, NOT sufficient**.
- No arbitrary field-weight choice or support overlap is needed for the graph realization: it already holds for all-one columns.

## 3. Theorem G5-B2 — \(\Theta(m^{8/3})\) edges survive all *graph-only* checks

**Statement (classical graph constructions plus B1).** For every fixed finite field GF(q) there exist arbitrarily large m and in fact examples for **all sufficiently large m** consisting of

    N = Ω(m^(8/3))

distinct unit support-four columns whose canonical pair factor graph has girth eight. Conversely any such canonical factor graph with C4 and C6 forbidden has at most O_q(m^(8/3)) edges. Therefore **the exponent 8/3 is sharp for the canonical-factor-graph/girth-only relaxation**, but this is **NOT** a lower bound on \(A_q^{set}(m,4,3)\).

**Proof.** Let s range over powers of two (hence prime powers). The classical symplectic generalized quadrangle of order (s,s) has bipartite incidence graph G_s of **girth 8**, with

    n_s = (s+1)(s²+1) vertices in EACH part,
    E_s = (s+1)²(s²+1) edges.

These formulas and existence are known and pinned in [G1](HYP-105-G1-W2D3-GIRTH8.md), literature **LIT-136**, with classic girth bounds **LIT-148** (Hoory 2002).

Let a_s be the smallest integer with \(\binom{a_s}{2}\ge n_s\). Then \(a_s=\Theta(s^{3/2})\). By B1, embed G_s as the canonical factor graph of E_s distinct unit four-sparse columns in \(m_s=2a_s=\Theta(s^{3/2})\) coordinates. Since E_s=\Theta(s^4), this yields

    E_s = Θ(m_s^(8/3)),

while the factor graph still has girth 8. To obtain all sufficiently large m, choose the largest power of two s with m_s≤m, and pad with zero coordinates at the end. The next power of two increases m_s by at most a constant factor for all sufficiently large s, hence m_s=Ω(m) and E_s=Ω(m^(8/3)). The upper follows from the elementary girth-eight Moore bound on at most O_q(m²) weighted pair vertices. QED.

**Important:** The exact subset sums of these vector families have **not** been proved injective; the smallest member below explicitly has a collision. This refutes the suggestion that canonical pair ordering/realizability *alone* might improve the upper exponent. **It does not prove that the true ASET upper exponent is optimal.**

## 4. A finite 45-column counterexample within the girth-eight construction

For s=2 the symplectic generalized quadrangle W(3,2) can be built from the 15 nonzero GF(2)^4 vectors as projective points and its 15 totally isotropic two-dimensional projective lines. The incidence graph has **30 vertices, 45 edges and girth 8**. Since \(\binom{6}{2}=15\), map the 15 points to the 15 two-element subsets of P={0,...,5} and the 15 lines to the 15 two-element subsets of Q={6,...,11}. Thus the construction yields **45 distinct support-four unit columns on m=12 coordinates** with factor graph *isomorphic* to the 30-vertex girth-eight graph.

However, the column family contains the explicit four columns with supports

    A={2,3,6,7},    B={0,5,8,9},
    C={0,2,6,8},    D={3,5,7,9}.

The equalities of integer coordinate counts give

    1_A + 1_B = 1_C + 1_D

over **every** field. The columns all occur in the deterministically defined W(3,2) pair mapping, verified by an independent exact subset-sum oracle in [test_hyp105_g5b_graph_realization.py](../../research/test_hyp105_g5b_graph_realization.py). The pair-signature graph contains neither C4 nor C6; the collision happens through a **coordinate-level signed trade**, not a short cycle of pair signatures.

This witness strengthens [G5-A](HYP-105-G5-A-TRADE-INTERSECTION.md): graph-girth incompleteness appears **inside a canonical exponent-matching dense girth-eight family**, not only a six-edge matching.

## 5. Primary-source correction: Lefmann's *logarithmic* lower factor

The original publisher abstract of **Lefmann (2005), existing LIT-043** ([Cambridge original](https://doi.org/10.1017/S0963548304006625)) contains a stronger lower construction than the bare exponent repeatedly quoted in the historical G4 and early G5 notes. For even k≥4 with gcd(k−1,r)=1, the abstract states

    A_q^lin(m,r,k) = Ω_q(m^(kr/[2(k-1)]) (log m)^(1/(k-1))).

Substituting k=6 and r=4 gives gcd(5,4)=1, kr/[2(k−1)]=24/10=12/5 and exponent 1/(k−1)=1/5. Thus for every fixed field q,

    A_q^lin(m,4,6) = Ω_q(m^(12/5) (log m)^(1/5)).

Since ASET contains every such six-wise independent family, the **currently strongest *source-verified* lower** is

    Ω_q(m^(12/5) (log m)^(1/5))
       ≤ A_q^lin(m,4,6) ≤ A_q^set(m,4,3)
       ≤ O_q(m^(8/3)).

The old weaker Ω_q(m^(12/5)) bound remains true but incomplete as a best-known summary. This logarithmic correction is **published 2005 prior art**, not a Mathlab discovery, and does not affect the exponent interval [12/5,8/3] or establish a superconstant ASET/linear *ratio*.

## 6. Research decision, remaining gap, and source novelty

**G5-B accepted scope:** An unrestricted *bipartite graph on pair signatures*, including large-girth extremal graphs, is structurally realizable in the canonical sorted 2+2 column factorization. The graph-only relaxation has exactly order \(\Theta_q(m^{8/3})\). It is **not** a correct substitute for genuine exact three-sum distinctness.

The mathematical target of parent **[#95](https://github.com/definitely-stable/Mathlab/issues/95)** remains the real interval:

    Ω_q(m^(12/5) (log m)^(1/5)) ≤ A_q^lin(m,4,6)
                  ≤ A_q^set(m,4,3) ≤ O_q(m^(8/3)),

with **no new exponent, no proven growing ratio**. Further work must use **signed-coordinate-trade avoidance** or another structural property not implied by ordinary factor-graph girth. Proposed G5-C order:
1. Search for source-backed restrictions and/or extremal theorems forbidding additive signed trades in sparse support-four/q-ary families, not generic girth-eight graph results.
2. Freeze separate **genuine ASET** and **arbitrary-coefficient six-wise linear independence** benchmark oracles to test any candidate construction; do not promote graph-only dense examples.
3. Only attempt a theorem changing one end of the exponent interval or prove a matching lower/upper; stop finite extrapolation, and do not open a Rust crate.

**Literature:** No additional identities are necessary here. Reuse existing verified **LIT-136** Abreu et al. (girth-8/generalized quadrangles), **LIT-148** Hoory (bipartite girth bound), **LIT-043** Lefmann (sparse six-wise independence), and existing G5-A references. This is elementary realization + **old** geometric graph construction; a new scientific theorem **is not claimed**.

**Evidence labels:** The B1 mapping is proved algebraically; B2's geometric infinite-family existence is attributed to classical literature; CI tests reproduce only the **s=2** instance (not the infinite geometry theorem) and finite exhaustive small graph embeddings. No Lean proof, source-completeness claim, security property, product performance, or cross-repository modification.
