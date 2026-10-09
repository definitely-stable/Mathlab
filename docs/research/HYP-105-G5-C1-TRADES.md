# HYP-105 G5-C1 — Minimal signed-trade locality and split-pair circuits

Date: 2026-10-09. [Parent #95](https://github.com/definitely-stable/Mathlab/issues/95), [active G5-C #106](https://github.com/definitely-stable/Mathlab/issues/106), [G5-C0](HYP-105-G5-C0-SIGNED-ORACLE-FOUNDATION.md).

**PROVED_ELEMENTARY_FORBIDDEN_CORE / AUTHOR_HOSTED_PRIMARY_PAPER_VERIFIED / NO_NEW_EXPONENT / NO_NOVELTY_CLAIM.** These are proof-backed structural restrictions, NOT an improved full-ASET upper/lower bound or a Rust library authorization.

## 1. Frozen unrestricted model

Fix a finite field F and distinct nonzero vectors a_1,...,a_N in F^m, each of support size at most four, with all subset sums of cardinalities 0,1,2,3 required to be unique. A signed trade is a pair of disjoint column-index sets P,N, not both empty, such that |P|<=3, |N|<=3 and sum(P) a_i = sum(N) a_i. A trade is column-minimal if no *other* nontrivial bounded signed trade is supported on a proper subset of its participating columns (its signs need not be a restriction of the original assignment).

In Sections 3–4 we separately restrict to all-one support-exact-four columns with two support coordinates in each of a fixed pair of disjoint coordinate blocks L/R and field characteristic p>3. None of those narrower assumptions applies to the unrestricted result in Section 2.

## 2. G5-C1-L1: universal minimal signed-trade locality lemma

**Theorem (all finite fields, arbitrary nonzero weights).** If a signed trade contains t distinct participating columns, 1<=t<=6, and V denotes the union of their nonzero coordinate supports, then

    each coordinate v in V occurs in at least two participating columns,
    |V| <= floor((sum |supp(a_i)|)/2) <= 2t <= 12.

Moreover, if the signed trade is column-minimal, the bipartite incidence graph on participating columns and coordinates V is connected.

**Proof.** A coordinate incident to exactly one participating column would contribute either +a_i(v) or -a_i(v), nonzero in F, contradicting the signed equality. Consequently sum_v degree(v) >= 2|V|. The same sum counts column nonzero coordinates and is at most 4t, which proves |V|<=2t. If the incidence graph has two components, the original relation restricts independently to each component because the components use disjoint coordinates. Each nonempty component inherits at most three positive and at most three negative columns, so gives a signed trade on a proper nonempty subset. This contradicts the column-minimal definition. QED.

The converse (connected plus each degree>=2 implies a field trade) is FALSE without exact signed coefficient equations. These are necessary shape conditions, not sufficient certificates or asymptotic density bounds.

**Sharp witnesses with exact support four:**

- t=3, |V|=6, GF5, *unbalanced* 1-versus-2: a=(1,1,1,1,0,0), b=(1,1,0,0,1,1), c=(0,0,1,1,4,4). Then a=b+c, all six coordinates have support degree two, and none of the three proper column subfamilies collide. The weighted unrestricted model cannot ignore 1-versus-2.
- t=4, |V|=8, all-one GF5, 2-versus-2: for i mod 4 use a_i=e_i+e_(i+1)+e_(4+i)+e_(4+i+1) (indices reduced modulo 4 separately in each half). Alternating columns a_0+a_2=a_1+a_3; all eight coordinates have degree two. No proper GF5 trade exists.
- t=6, |V|=12, all-one GF5, 3-versus-3: use the same construction for i mod 6 with the second cycle shifted by 6. Alternating triples coincide, each of 12 coordinates has degree two, and in GF5 the incidence kernel of each 6-cycle has exactly its complete alternating relation. It has no proper trade.

These sharp examples are **invalid ASET families** by design. No finite witness certifies an improved exponent.

## 3. G5-C1-L2: balanced cardinalities only for uniform all-one columns

**Theorem.** For finite fields of characteristic p>3, if each column has exactly four entries **equal to one**, any trade with at most three columns per side must have |P|=|N|. Proof: apply the sum-of-all-coordinate functional. Each vector has coordinate sum 4; thus 4(|P|-|N|)=0 in F. As 4 is invertible and |P|-|N| is an integer in [-3,3], p>3 implies |P|=|N|. QED.

For distinct unit columns, 1-versus-1 and empty-versus-nonempty are impossible. Hence violations of ASET in this *restricted model* arise from 2-versus-2 or 3-versus-3 (possibly with a common column that cancels). The explicit GF5 weighted t=3 fixture above is a counterexample to transferring balanced-only checking to arbitrary weighted support-four ASET. The all-one proof also fails for nonuniform support sizes.

## 4. G5-C1-L3: alternating projected coordinate-pair circuits

**Theorem.** Fix all-one four-support columns having exactly two nonzeros in a global block L and two in a disjoint global block R, and field characteristic p>3. For disjoint selected column sets P,N of size at most three, build TWO edge-colored *multigraphs* H_L, H_R, with each column represented by an edge between its two support coordinates in that block, retaining edge IDs/multiplicities; color P edges red, N edges blue.

Then the columns make a signed trade iff BOTH H_L and H_R admit covers of their participating edges by edge-disjoint alternating red/blue **closed circuits**, each of length 2, 4 or 6. Length 2 includes distinct opposite-colored parallel edges. Larger circuits may repeat coordinate vertices, so this is NOT simply the girth of the canonical weighted pair-signature factor graph.

**Proof.** At each coordinate vertex v, the difference of red and blue incidences is an integer between -3 and 3. Since characteristic p>3, it vanishes in F precisely if red-degree(v)=blue-degree(v) in integers. When these degrees agree, arbitrarily pair red and blue *edge-ports* at each coordinate. Traverse an edge to its other endpoint, then continue on the uniquely paired opposite-colored port. Every edge has two ports and all are paired, so the finite traversal partitions the distinguishable edges into alternating closed circuits. The total participating edges are at most six, hence possible circuit lengths are 2,4,6. Conversely such a cover balances every coordinate's red and blue degrees and proves projected equality. As L/R are disjoint coordinate subspaces, full equality holds iff both projections vanish for the SAME P,N. QED.

**Essential boundaries.** This is a constructive formulation of the earlier G5-A split-kernel criterion, not a genuinely new extremal bound. A global L/R split must not be confused with each column's canonical first/last-two sorted coordinates when their coordinate ranges overlap across columns. A factor graph can be a *perfect matching* while both projected coordinate multigraphs contain alternating circuits, as the t=4 and t=6 witnesses show. Cycle cover in L alone is not enough; the same sign pattern must also balance R.

## 5. Exact executable evidence and reproducibility

[research/test_hyp105_g5c1_minimal_trades.py](../../research/test_hyp105_g5c1_minimal_trades.py) uses only standard Python.

- Direct disjoint-subset signed-oracle checks true GF5 sums (including unequal cardinalities) independently of C0's ternary pattern evaluation.
- An independent coordinate-degree and connected-component oracle checks localization and minimality against every proper participating column subfamily in bounded fixtures.
- An edge-port pairing/circuit-cover oracle checks the split-unit theorem against direct integer vertex-degree sums, including false positives if only one of L/R is checked.
- Sharp t=3,4,6 weighted/unit fixtures and a full deterministic collection of four-column candidates validate exact arithmetic; finite tests are NOT asymptotic proofs.
- GitHub-hosted research workflow at the *exact PR head* must complete before acceptance. No Lean proof is claimed.

## 6. Original 2008 full manuscript on the author's site: source priority confirmed

LIT-152 is Naor and Verstraete, *Parity check matrices and product representations of squares*, Combinatorica 28(2), 163-185 (2008), [publisher DOI](https://doi.org/10.1007/s00493-008-2195-2), [Princeton academic publication record](https://collaborate.princeton.edu/en/publications/parity-check-matrices-and-product-representations-of-squares).

**The authors' full manuscript, not a third-party transcript:** [Assaf Naor's Princeton-hosted PARITY.pdf](https://web.math.princeton.edu/~naor/homepage%20files/PARITY.pdf), printed pp. 5–6, **Theorem 2.2 and full proof**. Directly inspected. In their paper:

    M = sum_{j=0}^{floor(r/2)} (|F|-1)^j binom(n,j),
    N = sum_{j=0}^{ceil(r/2)}  (|F|-1)^j binom(n,j).

Their exact theorem asserts that |X| > 2k[M^(1/2) N^(1/2+1/k) + M + N] for a set X of distinct vectors of weight<=r guarantees *disjoint sets A,B each of size k with equal F-vector sums*. For k=3, r=4: M=N=1+(q-1)n+(q-1)^2 binom(n,2)=Theta_q(n^2), so threshold equals 6[M^(4/3)+2M]=O_q(n^(8/3)). This bounds genuine ASET, not merely arbitrary-coefficient linear independence.

Their **Theorem 1.1 requires k>=8**; it MUST NOT be substituted directly for our six-column case. The author-controlled full-text evidence upgrades the earlier G5-C0 third-party text audit but is still not a claim to have exhaustively reproduced the published 18-page article or collated publisher and author proofs line by line. LIT-152 remains the SAME canonical bibliographic identity; no duplicate research entry.

## 7. Honest result and next proof gate

The known bound remains

    Omega_q(m^(12/5) (log m)^(1/5))
      <= A_lin(q,m,4,6) <= A_set(q,m,4,3) <= O_q(m^(8/3)).

There is still NO proven o(m^(8/3)) or stronger power upper for unrestricted weighted ASET, no improvement over Lefmann's exponent from a true all-m construction, and no demonstrated ASET/lin divergence. G5-C1 builds a correct small-forbidden-configuration search space, **not** a density theorem.

**G5-C2 next evidence gate:** either quantitatively bound families excluding *simultaneous* coordinate-level alternating circuits/weighted signed trades beyond the 2008 cycle bound; or construct and prove an infinite ASET family beating the 12/5 lower exponent; or record a bounded STOP_NO_NEW_EXPONENT with source-complete limitations. None may be inferred from |V|<=12 or finite enumeration alone. Keep #95/#106 OPEN; no new Rust crate, no changes to other repositories.
