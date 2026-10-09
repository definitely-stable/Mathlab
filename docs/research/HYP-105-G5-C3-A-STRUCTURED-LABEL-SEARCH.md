# HYP-105 G5-C3-A — Structured pair-label experiments and coordinate-gauge invariance

Date 2026-10-09 · [G5-C3 issue #119](https://github.com/definitely-stable/Mathlab/issues/119) · parent [#106](https://github.com/definitely-stable/Mathlab/issues/106) · [G5-C2 density gate](HYP-105-G5-C2-DENSITY-GATE.md).

**FINITE_EXACT_SEARCH_FOUNDATION / GAUGE_LEMMA_DERIVED_CLASSICAL / ASYMPTOTIC_GAP_OPEN / NO_NEW_EXPONENT / NO_RUST.** Do not label bounded optimization as a proven uniform construction.

## 1. Critical review and next mathematical target

The C2 conditional alteration bound says that for a true candidate universe B_m with N_m=Omega(m^a) and distinct inclusion-minimal forbidden supports T_t(m)=O(m^b_t), the classical method produces an exact ASET family of size Omega(m^(a-delta)), where delta=max(0,max_t((b_t-a)/(t-1))). GQ incidence family under **unit, globally separated 2+2 pair labels over GF5** has a=8/3; sufficient strict conditions for improving the existing ASET lower exponent 12/5 using that same method are b4<52/15 and b6<4. Neither exponent bound has been proved.

C2-D rigorously proved that **uniform, independent random injective left/right pair labels** have E[T6]=Omega(m^4) along GQ(s,s), s=2^h. **This is only an expectation, not a universal minimum, not concentration, and not a probability upper on all good outcomes.** Such an expectation blocks an argument asserting E[T6]=O(m^(4-epsilon)) under that distribution; it does NOT rule out exponentially rare favorable labelings, correlated random models or deterministic structured assignments. Any proof of nonexistence must independently show a lower bound for **every** allowed labeling, with exact m and graph/weight restrictions.

The next route is split into genuine alternative claims, never inferred from an experiment:
- G5-C3-A (this slice): exact finite optimization + invariance + held-out validation with nonrandom label assignments, explicit model transfer barriers and bounded search budget;
- G5-C3-B: construct algebraic/geometry-based **uniform-in-s** label assignments and prove T4 and T6 estimates, or prove an all-labeling lower bound restricted to GQ;
- G5-C3-C: if C3-B has no theorem, attempt hypergraph independent-set/containers/LLL methods using formally priced codegrees instead of first moment; stop the specific random/first-moment route when warranted;
- separate unrestricted weighted ASET upper or improved denominator: non-transferable by default.

## 2. Exact finite universe and two independent census algorithms

The W(3,2) incidence graph has 15 point vertices and 15 isotropic line vertices, 45 edges, regular degree 3 and girth eight. Choose independent **bijections** from both 15-vertex parts to all 15 unordered pairs of six distinct coordinate symbols. An edge (x,y) becomes a unit four-support column whose supports are L(x) union (6+R(y)). All selected columns are distinct, support-exact-four and use **m=12** coordinates. Their canonical pair-signature factor graph is the original girth-eight W(3,2), up to vertex relabeling, regardless of pair assignments.

The new fast exact census uses *base-five integer encoding* h(a)=sum_{j:a_j=1}5^j. For sums of at most three all-one columns, each coordinate digit lies between 0 and 3 and thus no carrying occurs; h(sum a_i)=sum h(a_i). Since p=5, equality of these integer signatures is equivalent to exact GF5 full-coordinate sum equality for this restricted model. Group all 990 pairs and 14190 triples by encoded signatures, enumerate disjoint equal pair/triple subsets and remove six-column support conflicts which contain a smaller four-column conflict. This counts **distinct inclusion-minimal column-ID supports**, not collision witnesses with multiplicities.

The independent slow reference oracle [G5-C2 collision_spectrum](../../research/hyp105_g5c2_density.py) constructs and compares *full 12-tuples of integer coordinate sums*, followed by independent direct GF5 all-subset oracle validation of any extracted family. The fast and slow returns are compared by full ordered tuples of support bitmasks (not just counts) on the original and held-out bijective labelings.

**Negative model check:** do not apply equal-cardinality counting to arbitrary weighted columns. The prior G5-C1 GF5 weighted rank-certified minimal 3-vs-2 trade is explicitly checked and rejected by the unit-only entry point.

## 3. Gauge symmetry theorem and model non-novelty

**Lemma C3-A1 (exact coordinate-permutation invariance).** Fix any GF(q), m, arbitrary nonzero weight palette and any family of columns a_i in GF(q)^m. If pi permutes coordinate positions and a'_i=pi(a_i) for every i, then each pair of subsets S,T with |S|,|T|<=3 has equal sums for the original family **iff** it has equal sums for the transformed family. In particular, the entire forbidden-trade hypergraph of indexed column supports (including sign pattern multiplicities) is unchanged. ASET validity, minimum forbidden-core counts T_t and maximal valid cardinality are invariant under such a global coordinate permutation.

**Proof.** Coordinate permutation is an invertible GF(q)-linear operator P. For any subsets S,T, P(sum_{i in S}a_i-sum_{j in T}a_j)=sum_{i in S}P(a_i)-sum_{j in T}P(a_j). Because P is injective, the original difference is zero iff its image is zero, for each pair of subsets, independent of weights or support bounds. Therefore exactly the same labeled column subsets are forbidden, and every finite cardinality conclusion follows. QED. This is an **elementary derived classical invariant**, not a new scientific theorem.

For the global 2+2 split, S6 separately permutes coordinate positions within the left and right block. An S6 action induces a permutation of the 15 pair labels. Hence left/right label bijections differing solely by these actions belong to the same invariant trade-spectrum orbit. **An S6 x S6 coordinate-gauge orbit cannot improve exact trade counts**; it is mathematically false to present such transformed labelings as different algorithmic improvements. A coordinate-pair permutation outside the image of the S6 action generally *can* change the trade hypergraph, because it is not induced by a coordinate permutation.

**Exact orbit count (elementary finite corollary).** The action of S6 on the 15 edges of K6 is faithful: if a permutation fixes every unordered pair, it fixes every vertex. A bijection between 15 graph vertices and all 15 pairs uses every pair, so its S6 stabilizer is trivial. Therefore every one-half labeling orbit under coordinate permutations has size exactly 6!=720. As there are 15! possible bijections, the number of one-half equivalence classes is exactly 15!/6!=1,816,214,400, and the number of two-half labelings modulo independent coordinate-permutation gauge transformations is exactly (15!/6!)^2. This is **not** the number of classes modulo abstract graph automorphisms, which may identify more labelings. The huge finite search quotient explains why a bounded heuristic cannot prove optimality.

This exact invariant is validated over held-out random bijections and randomly selected S6 x S6 actions; the 720 induced distinct K6 pair actions and exact factorial divisibility are also checked independently. W(3,2) automorphisms might give further quotient reduction, but are not assumed or proved in this slice.

## 4. Deterministic bounded descent (finite only)

[research/hyp105_g5c3_label_search.py](../../research/hyp105_g5c3_label_search.py) implements a seeded, fully reproducible finite search. Start from a prescribed pair of 15-label bijections (identity or fixed-seed shuffle). In each round evaluate up to a fixed number of candidate swaps of two graph vertices on either side. A swap preserves bijectivity and therefore preserves the abstract incidence graph and its girth. Accept the lexicographically earliest candidate with strict improvement of the **explicit finite heuristic**:

    score = T6 + 16*T4.

The multiplier 16 is a pragmatic finite optimization preference, NOT the true ASET objective, an alteration optimum, a rigorous exponent proxy or a physical cost measurement. The proof of monotonicity is immediate: the algorithm accepts a candidate only when its **exactly recomputed** score is smaller; otherwise leaves labels unchanged. It does not claim an optimum under *all* swaps or the global permutation group. The fixed finite budget (number of rounds, candidate probes, RNG seed) is part of reproducibility.

For the chosen final labeling: reconstruct full vectors, independently enumerate exact GF5 forbidden supports, derive the rational first-moment bound, deterministically extract a valid subfamily, independently test all sums cardinality 0..3 and serialize every label assignment and selected column ID. The output is a certificate for m=12 only. It does NOT prove an inequality for GQ(s,s) as s grows.

One command:

    python research/hyp105_g5c3_label_search.py --seed 1 --rounds 6 --probes 12

The hosted workflow runs the same command; its exact output should be recorded in this document **after** CI and pinned by regression tests only if the final code head is unchanged.

### 4.1 Frozen exact-head hosted finite evidence (W32; m=12)

The bounded search completed successfully on exact-head [GitHub-hosted Research #1052](https://github.com/definitely-stable/Mathlab/actions/runs/37895760910), running initial code HEAD `f584d97e6e36b0ffc352cd9843b50bcde2422070`. This was followed by a separate full-CI run after adding the coordinate-gauge orbit count (verify later SHA separately); numbers below are pinned in deterministic unit regression for reproducibility. Finite seed=1, 6 rounds, 12 proposed swaps per round, heuristic T6+16*T4:

| Exact model | Before | After |
| --- | ---: | ---: |
| Minimal forbidden t=4 supports | 46 | 42 |
| Minimal forbidden t=6 supports | 1722 | 1580 |
| Heuristic score | 2458 | 2252 |
| Extracted real GF5 ASET subfamily | 20 | 20 |

From 69 total trade-census evaluations (including the initial assignment), exactly **four strictly improving swaps** were accepted. The final 15-label maps, in original graph vertex order, are:

    L=(14,13,0,10,6,5,3,8,7,9,4,1,12,11,2)
    R=(6,3,11,12,8,1,5,4,7,14,9,10,2,13,0)

All 45 columns still have four ones and the same abstract W32 factor graph girth eight; the 20-column selected subfamily is independently certified ASET for all cardinalities 0..3 in GF5. **This is not an increase in proven maximum ASET cardinality**: the previous seed=1 construction already extracted 20 columns. Only the two finite *minimal trade support counts* and the chosen finite heuristic decreased. Neither an optimal permutation nor m-dependent improvement follows. The exact rational first-moment lower score is deliberately distinguished from the actual extracted 20; an alteration bound is not automatically tight.

## 5. Source/model mapping and missing theorems

| Literature (canonical ID) | Material relevance | Non-transfer condition |
| --- | --- | --- |
| LIT-043 Lefmann (2005), https://doi.org/10.1017/S0963548304006625 | Existing GF(q) support4 six-wise-linear **lower** Omega_q(m^(12/5)(log m)^(1/5)) | Does not imply ASET-vs-linear ratio grows |
| LIT-152 Naor–Verstraëte (2008), https://doi.org/10.1007/s00493-008-2195-2 | Published genuine ASET upper O_q(m^(8/3)), via exact disjoint three-sum Theorem 2.2 | Graph construction sharpness is not a better ASET family |
| LIT-136 generalized quadrangle source in catalog | Infinite girth-eight incidence graph family of size ~m^(8/3) in graph-only relaxation | A graph with no small cycles can still have signed coordinate trades |
| LIT-148 Hoory (2002) | Necessary extremal girth-eight pair graph bound | Not sufficient for signed-sum injectivity |
| LIT-005 Liu–Shangguan–Zhang (2026), https://arxiv.org/abs/2605.11949 | Nearby 3-union-free hypergraph bounds, near-optimal locally sparse hypergraph packings | Union-free is NOT equal to GF5 signed-sum-free and the published (3,4) theorem contains a parameter exception |

The source census is theorem/mode-scoped; no unsupported priority claim is made. No new literature ID is fabricated or duplicated in this slice. A separate full original-source novelty audit is necessary before announcing any genuinely novel exponent improvement. Other 2025–2026 hypergraph Turán/trace results need a certified model reduction before import as mathematical building blocks, not keyword resemblance.

## 6. Acceptance/STOP and next actions

G5-C3-A can be ACCEPTED on exact-head hosted Research SUCCESS, independent fast/slow exact forbidden-support agreement, validation of explicit actual ASET extraction, symmetry-preservation tests, invalid-injection and weighted-model negative tests, plus a reproducible search report. It is a **finite exact computer experiment and an elementary symmetry lemma only**.

The **real mathematical GO G5-C3-B** is an explicit or probabilistically certified infinite structured pair-label family with upper bounds for BOTH T4 and T6 strict enough to imply a genuine power improvement, OR a universal *all-labeling* quantitative barrier with properly stated GQ-only quantifiers, OR an improved theorem applying directly to full weighted ASET. The random expectation lower bound alone cannot do that.

If the bounded deterministic experiment improves some W32 sample, do **not** extrapolate a log-log slope. If it fails, do **not** claim an impossibility theorem. Keep [#119](https://github.com/definitely-stable/Mathlab/issues/119), [#106](https://github.com/definitely-stable/Mathlab/issues/106), and [#95](https://github.com/definitely-stable/Mathlab/issues/95) OPEN until a genuine all-m result or a properly scoped STOP. No Rust crate and no changes in DELSK/DeltaMeter/ChunkShift.
