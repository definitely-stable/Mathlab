# HYP-105 G5-E1 — Finite signed-flow motif reduction, zero-risk bridges and a random-label method barrier

Date: 2026-10-09. Parent [#162](https://github.com/definitely-stable/Mathlab/issues/162), [#106](https://github.com/definitely-stable/Mathlab/issues/106), [#95](https://github.com/definitely-stable/Mathlab/issues/95), [#136](https://github.com/definitely-stable/Mathlab/issues/136). Predecessors [GF5 weighted D1–D5](HYP-105-G5-D-AFFINE-WEIGHTS.md) and [exact boundary flows E0](HYP-105-G5-E0-BOUNDARY-FLOWS.md).

**PROVED_MODEL_SPECIFIC_NECESSARY_ZERO-RISK_RULES / FINITE_MOTIF_REDUCTION / RANDOM-LABEL_EXPECTED_FIRST-MOMENT_NO-GO / NO_NEW_ASET_EXPONENT / SCIENTIFIC_ORIGINALITY_NOT_ASSESSED.**

This is a proof-first structural step, not a substitute for the hard all-s bound on the actual exact collision-risk totals R₂ and R₃.

## 1. Mathematical objects and critical model separation

Let B be a collection of N DISTINCT supports of EXACTLY four coordinates each, over a fixed ambient m. For each support choose independently uniformly one of the 51 all-nonzero GF(5) coefficient quadruples whose sum is 4. This is the actual weighted GF5 ASET model, NOT a random signed graph and NOT a choice of field GF(2^h) coefficients.

For k=2,3 an unordered pair {P,Q} of disjoint k-sets of column IDs is a potential forbidden event. Its signed incidence graph H(P,Q) has 2k column vertices (sign +1 on P and -1 on Q) and one coordinate vertex for each physically touched coordinate; each column vertex has degree four. There is an incidence edge for each nonzero support membership. Let F_H(b;5) be its prescribed-boundary nowhere-zero GF5 flow count with column demands b(c_i)=4 sign_i and coordinate demands zero, as proved in E0. Its actual probability is F_H(b;5)/51^(2k).

For the **restricted globally split 2+2 support model** only, each support has two coordinates in a fixed left a-coordinate block and two in a disjoint right a-coordinate block. The two coordinate projections are edge MULTIGRAPHS on their coordinate symbols: each column produces one unordered two-coordinate edge per projection; several different original columns may share a projected edge. Girth eight of the independent GQ point-line factor graph is not the girth of either projected coordinate graph. Confusing those two graphs is a major proof error.

The exact expected-risk sum is over ALL potential signed k-vs-k events, including events that did not occur with all-one unit weights. Never substitute unit collision counts T₄/T₆ for the new weighted exact R₂/R₃.

## 2. E1-A: proved all-m zero-risk structural theorems

**Proposition E1.1 — singleton coordinate obstruction.** If any coordinate in the 2k-column signed incidence H(P,Q) appears in precisely one participating column, then F_H(b;5)=0.

Proof: its coordinate vertex has one incident edge z, and its prescribed divergence is zero. Therefore the unique edge flow value must equal zero, violating the nowhere-zero condition. QED.

**Proposition E1.2 — bridge-zero-boundary obstruction (strictly more general).** Consider any bridge e of the bipartite column-coordinate incidence graph H(P,Q). Delete e, obtaining two connected components of the ORIGINAL component cut by e. If the sum of prescribed b(v) on either separated side equals zero in GF5, then F_H(b;5)=0. For our checksum-4 model, it is sufficient that the separated side contain equally many + and - column vertices. This is NOT a sufficient condition for F_H(b;5)>0 when all bridges pass.

Proof: sum the oriented divergence equations over all vertices in the separated side. Every edge internal to the side cancels; the only remaining edge is e, with its flow equal to the signed sum of the boundary demands. If this sum is zero, e is forced to zero, contradicting nowhere-zero. In characteristic five, b(column)=4 sign, so zero sum is equivalent to zero signed column count mod5. With at most three positive and three negative columns in a G5-E trade, this is exactly equal signed counts. QED.

**Proposition E1.3 — balanced components.** In each connected component of H(P,Q), the number of positive and negative column vertices is equal, otherwise F_H(b;5)=0.

Proof: sum divergence over the entire connected component; all internal edge contributions cancel, so 4(#positive−#negative)=0 mod5. The signed difference lies in [-3,3], so it must be exactly zero. QED.

**Corollary E1.4 — projected leafless two-color multigraphs.** Assume globally split 2+2 supports, and F_H(b;5)>0. In BOTH coordinate projections every used coordinate vertex has degree at least two. With t=2k participating columns and exactly t pair-edges in each projected multigraph, each projection has at most t=2k vertices (four for 2v2, six for 3v3), every nonempty projected component contains a cycle (a two-edge parallel cycle counts), and the TOTAL number of used coordinates is at most 2t=4k.

Proof: singleton coordinates are forbidden by E1.1. Each projection has t pair-edges, hence sum of degrees 2t. Minimum degree at least two implies number of used vertices at most t, and a finite multigraph with all degrees at least two contains a cycle in every component. QED.

**Necessity-only warning:** these filters do NOT imply that a nowhere-zero flow exists, nor that its count is positive. Their role is to discard rigorously impossible configurations before expensive rank or flow calculations. The bridge criterion is genuinely stronger than just checking singleton coordinates; a separately checked six-column signed incidence has no singleton coordinates but has a zero-demand bridge.

## 3. E1-B: all-m finite motif-class decomposition (a reduction, not an exponent)

Define a *signed two-color motif* as the bipartite incidence graph of 2k signed column vertices and its touched coordinate vertices, where:
- column vertices are colored + or -, k of each;
- coordinate vertices are colored LEFT or RIGHT;
- all incidence edges connect columns to coordinate vertices;
- graph isomorphisms may freely permute column vertices within the same sign and coordinates within the same color;
- a simultaneous exchange of all + and - signs is allowed because it merely multiplies every flow by -1;
- the LEFT and RIGHT coordinate colors remain distinguished (exchanging left and right is not required).

For a given motif isomorphism class τ, let M_k(τ;B) be the number of distinct unordered potential k-vs-k events in B with that signed two-color incidence motif, and F_τ(5) its actual GF5 prescribed-boundary nowhere-zero flow count. The previous E0 exact reduction implies

    R_k(B) = 51^(-2k) SUM_{τ in types_k} M_k(τ;B) * F_τ(5),

an **exact equality for every m**. More importantly, by E1.1–E1.4 **every positive-weight motif** has at most 2k coordinate vertices of each color. Thus the number of possible relevant τ is a **finite constant depending only on k**, NOT on m, s or the number N of supports. Every excluded motif contributes exactly zero. The coefficient F_τ(5) is a nonnegative integer bounded by 51^(2k) and can in principle be computed once for each τ by published finite-group nowhere-zero flow methods.

**Proof.** Every event belongs to exactly one signed two-color graph-isomorphism class. A graph isomorphism preserving the indicated vertex types transports all edge flows bijectively: it preserves the zero coordinate divergence, and permutes the column demands 4 or -4 within their sign class. Reversing all signs transports flow z↦-z bijectively. Therefore F_H(b;5) is constant on τ. Group the exact E0 event-risk sum by these classes. For any class contributing positively, the projected degree and cardinality bounds above give at most 2k column vertices and 4k coordinate vertices, each with at most 4 incidences; only finitely many colored bipartite multigraphs are possible. QED.

This is a **finite-template reduction of an all-size risk problem to all-size MOTIF MULTIPLICITIES**. It is mathematically valid but NOT a proof that those multiplicities have a favorable growth rate. We still must prove upper bounds for M_k(τ;B_s) for a specified infinite s-dependent geometry/labeling, especially templates with F_τ>0. An all-m algebraic counting theorem for these multiplicities, rather than re-enumerating 2^24 flow edge deletions, is the actual opportunity.

## 4. E1-C: comparison with unit forbidden supports and an all-s method STOP

**Proposition E1.5 — unit signed-trade floor for weighted exact risk.** Suppose the supports in B are distinct and all-one columns (four coefficient values 1, hence checksum 4) contain T₄ distinct inclusion-minimal forbidden size-four supports and T₆ distinct inclusion-minimal forbidden size-six supports (true physically verified equal-sum GF5 trade cores). Then

    R₂(B) >= T₄ / 51^4,
    R₃(B) >= T₆ / 51^6.

Proof: each t-column minimal unit signed-trade support, t=4 or 6, has at least one partition into t/2 positive and t/2 negative columns witnessing an actual equal-sum event. Distinct supports imply distinct unordered potential events. The event has positive probability at least 51^(-t) under independent nonzero checksum4 weights, because the **single concrete all-one coefficient choice** realizes that trade and occurs with probability 51^(-t). Sum these distinct event probabilities within R_(t/2). QED.

For the existing W(3,2) 45-column original-labeled unit fixture, the independent frozen exact oracle had T₄=69 and T₆=1,940. Therefore the NEW weighted risk has at least R₂>=69/51^4 and R₃>=1940/51^6 **at this single m=12 only**. This bound is rigorously valid even though the greedy nonunit coefficients make all 45 columns ASET: it is a probability over ALL possible weight choices, not an assertion that every assignment collides. The two facts are compatible.

**Conditional all-s corollary E1.6 — RANDOM-LABEL EXPECTATION-FIRST-MOMENT obstruction.** C2-D already proves for the independently uniformly injected coordinate-pair labels on published GQ(s,s), s=2^h, that E_label[T₆]=Omega(m^4). Combining with E1.5,

    E_label[R₃(B_s)] >= E_label[T₆(B_s)]/51^6 = Omega(m^4).

Since N_s=Theta(m^(8/3)), the *expected value across label assignments* of the numeric weighted first-moment/alteration certificate

    L(p,B_s)=pN_s-p^4 R₂(B_s)-p^6 R₃(B_s)

is upper bounded by p*N_s-c p^6 m^4, for some fixed positive c. Its maximum over p∈[0,1] is **O(m^(12/5))**, as can be proved using derivative or the weighted AM-GM inequality: the maximizing p is O(m^(-4/15)), giving pN=O(m^(12/5)). This is a precisely scoped STOP for extracting a better POWER by **first optimizing the expectation of this certificate under independent uniform pair labels**.

**Critical logical scope:** The expectation bound does **NOT** show that every coordinate-pair labeling has R₃=Omega(m^4), that good labelings are absent, that the probability of obtaining a good labeling is small, that actual randomly weighted ASET size is upper-bounded, or that a stronger independence method cannot work. It rules out only the specified *average first-moment certificate* proof strategy. Exceptional/structured labels, correlated weights, conditional selection and hypergraph degree/codegree methods remain wide open. This is a method barrier, NOT a full ASET theorem or a universal combinatorial no-go.

## 5. Independent falsification and reproducible exact code

- [HYP-105 E1 motif and bridge code](../../research/hyp105_g5e1_motifs.py) implements the signed incidence graph, component-local boundary balance, bridges, true two-block degree core, a canonical exact signed two-color motif isomorphism signature and a small capped direct motif-enumerator.
- [Independent E1 tests](../../research/test_hyp105_g5e1_motifs.py) locate actual 2-vs-2 and 3-vs-3 unit GF5 witness orientations **by direct full-vector physical equality**, independently confirm all necessary structural rules and that an exact small four-column flow count is positive; include a six-column example with NO singleton coordinates but a forbidden bridge, test 24 coordinate renamings with sign swap, and verify every candidate event enters either an excluded class or precisely one motif class.
- The exact numerical W32 t4/t6 floor is verified by calling the independent previous [C2 exact collision oracle](../../research/hyp105_g5c2_density.py); no exponent is fitted from m=12.
- Direct motif k=3 enumeration is capped at nine candidate columns. It is intentionally **NOT** called for GF4 GQ with 425 graph edges: that would enumerate Omega(N^6) candidate signed events and is not an engineering substitute for all-s motif-counting theorems.
- The new canonical signature is a complete invariant of the **signed two-block incidence motif**, not of symplectic projective isomorphism, not a certificate of existence of nonzero GF5 flows, and not an exact Rk probability by itself.

## 6. Fully specified next proof plan E2–E5

### E2-A — three explicit all-s candidate labeling classes

For each s=2^h, use the actually verified symplectic W(3,s) with V=(s+1)(s²+1), E=(s+1)²(s²+1), degree s+1. Set a=min{r:binom(r,2)>=V}, m=2a=Theta(s^(3/2)). Required: two point/line injections into the a-coordinate-pair palette, not the impossible direct FULL-duad-disjointness model. Test three distinguishable schemes:
1. **Combinatorial number system baseline:** normalize GF(s)^4 projective points, rank the points, rank totally isotropic lines, map each rank injectively to a distinct unordered coordinate pair by exact binomial unranking. This is deterministic all-s and definitely injective, but *does not* by itself improve any risk exponent.
2. **Symplectic orbit-labelled ordering:** before pair unranking, organize points and lines by nondegenerate symplectic collineation invariants/canonical flags, and prove the induced permutation properties. A mere common global coordinate permutation is a gauge symmetry and MUST be rejected as a false improvement.
3. **Correlated two-sided labeling:** use a shared algebraic rule on point/line incidence rather than independent shuffles; define the exact invariant/correlation and require all-s injectivity proof. If a proposed explicit rule cannot be specified rigorously, do not label it a construction.

### E2-B — count embeddings of positive flow templates

For each relevant signed two-color motif τ from E1, prove an upper bound for the number M_k(τ;B_s) of its realizations in the actual explicit family, with correct symmetry division (unordered P/Q, within-sign column permutations, coordinate label automorphisms). Require constants uniform over all h and all t=4,6 types; do not count sign assignments as independent column-ID supports. With F_τ known, sum exact risks R_k. Seek b4<52/15 and b6<4; these are sufficient strict targets, not results. Partial bounds should also be recorded with full quantifiers even if no total improvement.

### E3 — exact flow counts and cancellation-aware probabilities

Use Fu–Ren–Wang 2025 Theorem 1.1 for F_τ(b;5), with canonical type-level memoization, forced-edge reduction, b-balanced bridge detection and explicit runtime caps. Distinguish **Rk (exact)** from Uk (D4 upper) and T4/T6 (unit exact minimal supports). An exact full-formula fixed-template computation may cost exponential time in 4t; it is a constant in m but should not be repeated O(N^6) times. Review 2025 assigning polynomial primary and classical flow/Tutte polynomial literature for already-proven claims before announcing novelty.

### E4 — alternative to first-moment when positive-motif multiplicity is too large

Derive maximum event degree, pair-codegree and higher overlap counts for the true *weighted* forbidden-event hypergraph, keeping coefficient randomness and retained support randomness separate. Check the exact hypotheses of any LLL/nibble/container theorem; produce a proved independence-size bound and compare to Lefmann's existing Omega(m^(12/5)(log m)^(1/5)). If method fails, issue a STOP only for that precisely modeled method, not for HYP-105.

### E5 — original extremal theorem and product boundary

An improved asymptotic ASET lower (or upper) must specify fixed q, weight≤4, all subset sizes 0..3, nonzero coefficients, quantifiers over unbounded m and proven constants. An all-m proof that only re-establishes already published 12/5 or 8/3 is a valid independent verification but not a novel exponent. A product decision about a Rust primitive is separate and forbidden until a genuinely useful, independently checked mathematical improvement or complete practical primitive specification exists.

## Sources / novelty boundaries

- Fu–Ren–Wang, *Counting flows of b-compatible graphs*, *Advances in Applied Mathematics* 168 (2025) 102901, DOI [10.1016/j.aam.2025.102901](https://doi.org/10.1016/j.aam.2025.102901), provides the general prescribed-boundary flow inclusion-exclusion formula. NOT Mathlab novelty.
- Naor–Verstraëte, *Parity check matrices and product representations of squares*, *Combinatorica* 28 (2008), DOI [10.1007/s00493-008-2195-2](https://doi.org/10.1007/s00493-008-2195-2), contains published actual ASET upper exponent 8/3.
- Lefmann (2005) provides already-known sparse six-wise-linear lower exponent 12/5 with a logarithmic factor.
- C2-D earlier in Mathlab proved expected signed unit six-trade floor Omega(m^4) for **uniformly independently injected random** pair labels. E1.6 is an elementary consequence, not a general deterministic impossibility theorem.
- The elementary bridge-cut and finite motif decomposition statements follow standard finite graph flow and colored graph isomorphism reasoning; worldwide priority has NOT been independently established. Never label these as new scientific world-first theorems without a serious original-source audit.

**Acceptance:** fully formal E1.1–E1.6 proofs, independent signed GF5 field oracles and deliberate balanced-bridge countermodel, complete small exact motif isomorphism tests, no accidental random/all-label quantifier transfer, no expensive GF4 k3 brute force, hosted exact PR-head Research SUCCESS. #162, #106 and #95 remain OPEN for the actual original asymptotic bound. No other repositories changed.
