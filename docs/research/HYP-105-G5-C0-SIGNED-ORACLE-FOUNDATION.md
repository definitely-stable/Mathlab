# HYP-105 G5-C0 — Exact weighted signed-trade and six-wise-linear oracle foundation

Date: 2026-10-09. Parent [HYP-105 #95](https://github.com/definitely-stable/Mathlab/issues/95); active [G5-C #106](https://github.com/definitely-stable/Mathlab/issues/106). Earlier [G5-A](HYP-105-G5-A-TRADE-INTERSECTION.md) and [G5-B](HYP-105-G5-B-GIRTH-RELAXATION.md).

**Status: MODEL_SEPARATION_PROVED / ORACLE_FOUNDATION / NO_EXPONENT_IMPROVEMENT / NO_NOVELTY_CLAIM.** This is the *first bounded, evidence-gated G5-C slice*, not completion of #106 or #95. A 2026 literature audit at theorem/model level remains open. Do not start a Rust library, promote a finite observation into a density theorem, or modify other repositories.

## 1. Exact objects, without graph-relaxation leakage

Fix q=5 for candidate construction and finite testing (more general q only when separately proved). Write A_set(q,m,4,3) for the maximum size of a family of distinct nonzero columns a_i in GF(q)^m, each with **support <=4**, for which every sum of *all subsets of cardinalities 0,1,2,3* is unique, including empty versus nonempty and different cardinalities. All **nonzero field weights**, not just unit-incidence columns, are allowed.

Write A_lin(q,m,4,6) for the maximum family with all subsets of up to six columns linearly independent under **arbitrary coefficients from GF(q)**. The latter is stronger: A_lin <= A_set, not conversely.

An exact ASET signed relation is a vector epsilon in {-1,0,1}^N \ {0} with **at most three +1 and at most three -1** and sum epsilon_i a_i = 0. Indices used positively and negatively must be disjoint (zero out any common indices). Include ALL allowed (positive-count, negative-count) pairs, including 1-vs-2, 1-vs-3, 2-vs-3, 3-vs-0 and 2-vs-0; exclude only (0,0). Neither a 2-vs-2 check nor a balanced 3-vs-3 check alone recognizes full ASET.

**Exact characterization (elementary, all q).** ASET through three holds iff no such nonzero bounded signed relation exists. Proof: cancel the intersection of a colliding pair of subsets to obtain epsilon; conversely form the two subsets from the plus and minus supports of epsilon. This is a precise acceptance rule, NOT a new exponent argument or source novelty claim. G5-A proved the related globally separated P/Q-projection intersection criterion; the full relation here makes **no global coordinate partition assumption**.

## 2. Explicit model-separation lemma: support-exactly-four ASET can be linearly dependent

**Statement.** Over GF(5), the three columns

    a = (1,1,1,1),
    b = (2,1,1,1),
    c = (3,1,1,1)

are all distinct and support-exactly-four. Their subset sums of *every cardinality 0..3* are injective, yet a - 2b + c = 0. Thus even **3-wise arbitrary-coefficient independence is not implied by ASET**, already inside weighted support-exactly-four GF(5) families.

**Proof.** The final three coordinates of a subset sum all equal the chosen cardinality k in GF(5). As k in {0,1,2,3}, two subsets of different sizes cannot collide. For each fixed k, the first coordinates of subset sums are pairwise different:
- k=0: {0}; k=1: {1,2,3};
- k=2: {1+2,1+3,2+3} = {3,4,0} mod 5;
- k=3: {1+2+3}={1}.
Therefore the 8 subset sums are distinct. Coordinatewise 1-2(2)+3=0 and 1-2+1=0 mod 5, proving the displayed non-signed dependence. QED.

**Interpretation.** Any bound specific to sparse *linear independence* can serve as a lower construction for ASET; a sparse linear-independence **upper** bound does NOT automatically bound ASET. A shared high-multiplicity "hub" in a small construction is not a uniform-in-m dense construction.

## 3. Signed-trade incidence agenda: mathematical targets not yet proved

An upper improvement must find a **necessary property of EVERY unrestricted weighted GF(5) ASET family** that is stronger than the G4 canonical factor-graph exclusion of C4/C6, then prove:

    A_set(5,m,4,3) = o(m^(8/3)), or O(m^(8/3-epsilon))

for a fixed epsilon>0, with all constants/quantifiers and coordinate overlaps accounted for. G5-B realizes *any* bipartite factor graph up to pair-signature vertex budgets; hence ordered canonical pair realizability alone is insufficient. Candidate extra structure: constrained intersections of signed coordinate-trade families, common-kernel bicircuits, and forbidden coordinate-overlap patterns. A constructive lower improvement must build a uniform-in-m family with:

    A_set(5,m,4,3) = Omega(m^(12/5+epsilon))

and independently check every permitted signed collision, not only C4/C6 or union-free properties. The two goals are disjoint research tracks and neither may be claimed from a finite random search.

The **denominator** must be independently bounded. A growing ratio A_set/A_lin would require a proved ASET lower and a proved A_lin upper with a positive exponent separation (or another rigorous unbounded factor); the currently separate A_lin lower and ASET upper do not prove any ratio growth.

## 4. Four independent algorithms and validation scope

Executable: [test_hyp105_g5c_signed_oracles.py](../../research/test_hyp105_g5c_signed_oracles.py).

1. **Subset-sum oracle A** enumerates each actual subset, cardinalities 0..3, accumulates vectors mod q, and uses equality of resulting full m-coordinate signatures.
2. **Signed annihilator oracle B** enumerates ternary patterns subject to *both* independent side bounds and evaluates all coordinate equations directly; it does not use subset-sum hashing.
3. **Linear oracle C** computes GF(q) column rank via modular elimination; when checking independence for N>6, it must enumerate all column subsets of sizes 1..6.
4. **Linear oracle D** enumerates all nonzero coefficient vectors in GF(q)^N, including 2,3,4 coefficients, to witness a dependence. This exponential reference is deliberately bounded to tiny N and is algorithmically separate from C.

Deterministic test families include 120 size-0..5 selections from a seven-element **weighted support-four GF5 pool**, unbalanced relations, explicit non-signed dependence, all-one/weighted two-versus-two trades, and held-out GF(7)/GF(11) cross-checks. Do not claim exhaustive testing over *all* m, N, supports or field weights. These oracles validate finite claims and catch incorrect algorithms but cannot prove any infinite-family extremal theorem.

**Regression gate:** GitHub-hosted research workflow on the *exact PR head*, unit-test discovery and all other repo checks; compare the two ASET oracles for admissible finite inputs and independently compare the two linear checks. If CI or a counterexample fails, reject this slice; no theorem promotion.

## 5. Source-to-model mapping and literature audit limitations

Existing canonical sources are reused without adding duplicate bibliographic records:

| Registry | Source and verified scope | Non-transfer condition |
|---|---|---|
| LIT-043 | [Lefmann, *Sparse Parity-Check Matrices over GF(q)* (2005)](https://doi.org/10.1017/S0963548304006625), original publisher abstract explicitly gives an extra log^(1/(k-1)) lower for even k>=4, gcd(k-1,r)=1 | At k=6,r=4: A_lin=Omega_q(m^(12/5)(log m)^(1/5)); no matching upper or ASET/lin ratio proof |
| LIT-152 | [Naor–Verstraëte, *Parity check matrices and product representations of squares* (2008)](https://doi.org/10.1007/s00493-008-2195-2), author/publisher bibliographic description: sparse arbitrary-coefficient independence and short graph cycles | Publisher abstract has a typographically ambiguous displayed comparison sign and an asymptotic c for large k. The exact strongest *k=6,r=4* numerical theorem has **NOT** been verified from full text; it may not be inserted as a precise denominator exponent or transferred to ASET |
| LIT-148 | Hoory (2002), classical bipartite girth extremal bound | Bounds the necessary graph relaxation, not all possible signed coordinate trades |
| LIT-136 | Generalized-quadrangle incidence girth-eight examples | G5-B proves graph-only sharpness, and exhibits a true ASET collision inside the finite model |
| LIT-151 | Shangguan–Tamo (2020), uniform union-free hypergraphs | Unit union-free is a stricter condition in the relevant odd characteristic; it cannot replace weighted ASET |
| LIT-005 | [Liu–Shangguan–Zhang, arXiv:2605.11949 v3](https://arxiv.org/abs/2605.11949), 2026 sharp union-free bounds | Explicit exceptional pair (t,r)=(3,4); no automatic sharp leading constant for our case |

Full 2025–2026 signed-additive hypergraph and separable-code source census is **not claimed complete**. In particular, an absent search hit is not evidence of scientific originality. Before any exponent theorem: exact original theorem statements, parameter substitution, publication priority and competing constructions must be pinned.

## 6. Current bound, stopping rule and next actual proof attempt

Source-verified current interval, for each fixed finite q:

    Omega_q(m^(12/5) (log m)^(1/5))
      <= A_lin(q,m,4,6) <= A_set(q,m,4,3) <= O_q(m^(8/3)).

**G5-C0 decision:** ACCEPT only the elementary GF5 separation lemma and the oracle-model foundation after exact-head CI; **NO_EXPONENT_IMPROVEMENT**. Keep #95 and #106 OPEN. The next proof slice must either (i) establish a quantitatively non-graph signed-trade incidence bound with a density consequence, (ii) construct an independently proven infinite ASET family improving exponent, or (iii) terminate a bounded original-source audit with explicit STOP_NO_NEW_EXPONENT. No new Rust crate, publicity as an original theorem, or cross-repository work.
