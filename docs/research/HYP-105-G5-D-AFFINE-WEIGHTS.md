# HYP-105 G5-D — Affine checksum-weighted sparse ASET, and a genuinely new construction direction

Date 2026-10-09 · related G5-C3 [#119](https://github.com/definitely-stable/Mathlab/issues/119), all-s [#136](https://github.com/definitely-stable/Mathlab/issues/136), root [#106](https://github.com/definitely-stable/Mathlab/issues/106), [#95](https://github.com/definitely-stable/Mathlab/issues/95).

**PROVED_ELEMENTARY_AFFINE_CHECKSUM / EXACT_FINITE_GREEDY_45_WITNESS_PENDING_HOSTED_ACCEPTANCE / NO_ASYMPTOTIC_BOUND / NO_NOVELTY_CLAIM.** The model is still the ORIGINAL full GF5 ASET target: arbitrary nonzero coefficients, support at most 4, unique sums for every subset of sizes 0,1,2,3. This is not a relaxed group or union-free proxy.

## 1. New direction instead of only relabeling unit pair graphs

Previous G5-C3-A and G5-C3-B0 optimized **support labels while fixing all four nonzero field coefficients to one**. C3-A extracted 20 valid GF5 columns from W(3,2) m=12; natural finite doily geometry extracted 18. That restrictive unit model is not inherent in the original HYP-105: full ASET permits arbitrary nonzero weights.

We can introduce weights without reintroducing unequal-cardinality signed trades by moving to a **single affine hyperplane** in GF5^m. For instance the linear functional L(v)=sum_j v_j in GF5. Select every support4 column a_i so that L(a_i)=c for the same c∈GF5^*, here c=4.

### Theorem D1 (affine checksum blocks unequal subset cardinalities)

Let F be any field of characteristic p>t, let L:F^m→F be any linear functional, and let a_1,...,a_N∈F^m satisfy L(a_i)=c with c≠0. If two subsets S,T⊆[N] with |S|,|T|≤t have equal vector sums then |S|=|T|.

**Proof.** Apply L to the equality: c(|S|-|T|)=0 in F. Since c≠0 and the integer difference lies between -t and +t with t<p, no nonzero difference is divisible by p. Hence |S|=|T|. QED.

The proof is all-m, any support shape and any weights. It is an elementary linear-function argument, **not a claim of original worldwide mathematical novelty**. For our actual GF5 target t=3, choose c=4. Thus 1-vs-2 and 3-vs-2 trades are rigorously impossible even with nonunit coefficients, and it suffices to test equal-size pair/triple sums. There remain genuine equal-size collisions, which must be checked independently.

### Theorem D2 (the 51 available support-four coefficient patterns)

Fix any support consisting of four different coordinate indices. Over GF5, require all four coefficients nonzero and their sum c=4. Exactly **51** assignments are possible, including (1,1,1,1).

**Proof.** The 4^4=256 sequences in (GF5^*)^4 are distributed among five additive sums. By the elementary orthogonality formula for additive characters, for each nonzero c the count is (4^4-1)/5=51 (for c=0 it is (4^4+4)/5=52). Alternatively enumerate the 4^3=64 first-three choices, and observe that exactly 13 make the required fourth coefficient zero. QED. The full finite palette is independently enumerated in regression tests.

This is **strictly more expressive** than the old unit model, while preserving its valuable cardinality barrier. The 45-source-column W(3,2) graph is unchanged, only GF5 coefficients are selected.

## 2. Exact incremental extension theorem and actual finite extraction algorithm

Let A_n={a_1,...,a_n} be ASET through size t in an abelian group (here GF5^m). Let x be a distinct new vector satisfying the same checksum condition. For each k=1,...,t define old subset-sum sets Σ_k(A_n). The newly formed k-subset sums are exactly x+Σ_{k-1}(A_n), which are mutually distinct because translation is injective and old Σ_{k-1} sums are distinct.

**Theorem D3 (exact extension criterion).** Under the shared nonzero-checksum condition and characteristic >t, A_n∪{x} is ASET through size t if and only if for EVERY k=1,...,t,

    (x+Σ_{k-1}(A_n)) ∩ Σ_k(A_n) = ∅.

**Proof.** By Theorem D1, cross-cardinality equalities cannot occur. Within cardinality k, old sums are pairwise distinct by induction; newly formed sums are pairwise distinct by injectivity of translation and the old Σ_{k-1} invariant; the only possible collision is between an old k-sum and a new k-sum. Their absence is exactly the stated set-disjointness test. QED.

This is a **finite exact greedy invariant**, not a heuristic or new exponent. It is computationally implementable with three hash sets, one each for 1/2/3-subset sums, plus {0}. When the allowed new x has support from a fixed original W32 edge, inspect all 51 checksum-preserving coefficient assignments in seeded deterministic order. Accept the first satisfying all three exact tests; else abandon/restart a bounded attempt. This is not a proof that greedy always succeeds for a given support order; every full certificate is checked after search.

Executable [HYP-105 G5-D finite weighted construction](../../research/hyp105_g5d_affine_weights.py) uses exact 12-digit base-five *field vector* representations. Important: addition is **coordinatewise modulo five**, not ordinary integer addition with carries. Every candidate is verified against all existing encoded k-subset sums, and a wholly separate prior full-vector GF5 oracle independently tests the final 0..3 sum family.

## 3. Exact finite target and scientific significance

The fixed W32 incidence graph has 45 edges, each representing a distinct 2+2 support of size four in ambient m=12. The earlier unit-weight C3-A search reduced four/six-column forbidden supports to T4=42,T6=1580 and then *extracted only 20* ASET columns. In a separate independent exploratory implementation, every tested checksum-preserving greedy attempt found weights for **all 45 original supports** that passed exact incrementally maintained subset sums. This motivates a testable finite PR target:

    GF5, m=12, support exactly four, nonzero coefficients,
    L(a_i)=4 for each of all 45 W32 edges,
    |A|=45, all subset sums of sizes 0..3 pairwise distinct.

If the GitHub-hosted independent direct full GF5 oracle confirms this, the finite witness is real: the actual ASET cardinality for THIS support universe increases from the previous 20-column *extracted subfamily* to 45. **It does not establish that maximum ASET size at m=12 is 45 or that the maximum over the full ambient GF5^12 is anything in particular.** Previous 20 was an algorithmic output, NOT a proved maximum. A larger witness also does not establish a growing ASET/linear gap or a new asymptotic lower bound.

The exact full verification checks

    1 + 45 + C(45,2) + C(45,3) = 15,226

**pairwise distinct GF5^12 signatures**, with 12 explicit field coordinates, not truncated hashes or approximate fingerprints. Mutation tests revert weights to the known invalid unit baseline, duplicate a vector or break its checksum, and require the independent oracle to fail. Multiple deterministic held-out RNG seeds are checked to rule out incidental dependence on one successful order.

## 3.1 D4 — Exact collision probability = bipartite incidence rank

This is a **fully proved all-size theorem for fixed signed trade patterns**, not a new asymptotic bound on the aggregate number of trades. It is a direct application of classical graph-incidence linear algebra, with exact model-specific GF5 probability and a nonzero-weight restriction.

Fix t original four-support columns with specified supports S_i (four distinct coordinates each) and prescribed trade signs ε_i∈{+1,-1}. Let U=union(S_i), v=|U|, and construct the bipartite incidence graph G whose left vertices are t columns, whose right vertices are v coordinate positions, and whose 4t edges are the occurrences (i,j) for j∈S_i. Let C be the number of connected components of G (including no isolated vertices, since all columns have exactly four support coordinates).

Independently choose each column's four coefficients **uniformly in the FULL GF5 affine checksum fiber**, i.e. all 5³=125 coefficient quadruples with sum 4. This sampling ALLOWS zero coefficients and is **not yet** the admissible support-exact-four model.

**Theorem D4 (exact unconditioned affine signed-trade probability).** Let E be the event that the chosen t vectors satisfy sum_i ε_i a_i=0 in GF5^m. Then:

- If some connected component K of G has sum_{i∈K} ε_i ≠0 (mod 5), then Pr[E]=0.
- Otherwise **Pr[E]=5^(C-v)** exactly.

**Proof.** Introduce one unknown w_{ij} per incidence edge. There are 4t unknowns. For each column i impose ∑_{j∈S_i} w_{ij}=4; for each touched coordinate j impose ∑_{i:j∈S_i} ε_i w_{ij}=0. Set z_{ij}=ε_i w_{ij}; the column equations become ∑ z_{ij}=4 ε_i, while coordinate equations become ∑ z_{ij}=0. The coefficient matrix is the *unsigned* incidence matrix of the bipartite graph G. Negating every coordinate-node row gives the usual oriented vertex-edge incidence matrix, which has rank t+v-C over **any** field (choose a spanning forest: every component has exactly one row dependency; forest edge columns establish rank t+v-C). The affine right-hand side is consistent precisely when its signed column-checksum sum vanishes in every component: 4∑_{i∈K} ε_i=0 in GF5. If consistent, the solution affine space has dimension 4t-(t+v-C)=3t-v+C, hence 5^(3t-v+C) points. All independent per-column affine choices total 5^(3t), giving Pr[E]=5^(C-v). QED.

For our t≤6, at most three signed columns per side, component balance mod5 is equivalent to **equal numbers of positive and negative columns in EACH component**. Thus even when the whole trade is balanced, a disconnected component with unbalanced sides makes it impossible. This strengthens the usable *component-local* obstruction while preserving the unrestricted weight model distinction.

**Corollary D4.1 (all-nonzero admissible palette).** Independently choose each column uniformly from its **51** four-nonzero coefficient tuples with checksum4. Let E_nonzero be the same collision. Then

    Pr[E_nonzero] <= min(1, (125/51)^t * 5^(C-v))

when every component is signed-balanced; otherwise it is 0. Moreover if **any touched coordinate has incidence degree exactly one**, the probability is precisely 0, since its sole coefficient would need to vanish, forbidden by the nonzero support restriction. The stated upper bound simply conditions an affine random event on all 4t coefficients being nonzero: Pr[E | all-nonzero] ≤ Pr[E]/Pr[all-nonzero], with Pr[all-nonzero]=(51/125)^t; no independence of the event and the conditioning is assumed.

**Independent exact tests:** [GF5 rank/probability oracle](../../research/hyp105_g5d_trade_rank.py), [tests](../../research/test_hyp105_g5d_trade_rank.py). The oracle builds the full (t+v)×4t *signed* coefficient matrix and checks its modular Gaussian rank AND augmented rank independently of union-find component counts. A two-column opposite-signed **identical support** example has t=2,v=4,C=1; the full affine collision probability is exactly 1/125 and the all-nonzero collision probability is exactly 1/51 (independently enumerated over all 125² and 51² assignments). Two disjoint mismatched-sign components are inconsistent. Cases with one-coordinate incidence degree one are filtered. Eighty held-out arbitrary signed support configurations test rank t+v-C.

**Research value and limitation:** We now have an *exact formula* for **each** potential local trade probability, and a transparent bridge from geometry/support incidence to weight-selection risk. This is a meaningful all-m quantitative lemma, but at fixed q=5 and t≤6 each local probability is constant with respect to ambient m. It is **not** by itself a new ASET power improvement: one must count configurations jointly as m grows, prove useful bounds on dependency/codegrees, or build weights with deterministic algebraic cancellation avoidance. Claiming an exponent merely from 5^(C-v) would be false. The use of incidence-matrix rank is classical; global scientific novelty remains unverified.

## 3.2 D5 — An explicit all-m weighted alteration existence theorem

The exact D4 local rank formula can now be combined with **random weighting and subset sampling** to obtain a genuine all-m constructive-existence bound. This is a classical probabilistic alteration proof applied to a newly specified GF5 trade-risk functional; not a claimed improvement of Lefmann's exponent.

Let B be ANY N pairwise distinct size-four **supports** in [m]. For k=2,3, enumerate every unordered pair {P,Q} of disjoint k-element subsets of support indices, each pair **only once** (P,Q and Q,P represent the same event). Form the signed 2k-column incidence graph for the assigned supports, count its touched coordinate vertices v_{P,Q} and connected components C_{P,Q}. Define its local risk bound b(P,Q):
- b=0 if the signed checksum fails to balance separately in any component;
- b=0 if any touched coordinate occurs in only one of those 2k column supports;
- otherwise b = min(1, (125/51)^(2k) * 5^(C_{P,Q}-v_{P,Q})).

Let U_k(B)=sum_{unordered disjoint P,Q, |P|=|Q|=k} b(P,Q).

**Theorem D5 (weighted support-risk alteration).** For every p∈[0,1] there exists a choice of four **nonzero** GF5 coefficients on some subset of the supports in B, each column having checksum 4, such that ALL subset sums of cardinalities 0..3 are distinct, and the number of retained supports is at least

    p*N - p^4 U_2(B) - p^6 U_3(B).

In particular optimize this bound over p and clamp to zero. The existence statement is mathematically valid for every m,N (with B having distinct supports); no all-m asymptotic improvement is implied until U_2,U_3 are actually estimated uniformly for a specified support family.

**Proof.** Independently assign to each candidate support one of its 51 admissible nonzero checksum4 patterns uniformly. Independently retain each column with probability p. Distinct supports ensure different vectors even after weighting. By D1 all unequal-cardinality sum equalities are impossible. A 1-vs-1 equality is also impossible because supports differ. For every disjoint equal-size P,Q of size k=2 or 3, let X_{P,Q} indicate that (i) all 2k columns survive sampling and (ii) their chosen weighted sums are equal. The two sources of randomness are independent; by D4.1, E[X_{P,Q}]≤p^(2k)b(P,Q). The expected number of retained columns is pN and the expected number of forbidden collision events is at most p^4 U_2+p^6 U_3. Thus some realization has |S| minus the number of its actual forbidden events at least the displayed expression. Delete one currently retained column from each remaining forbidden event. No deletion creates an event; at most the original number of forbidden events are removed, so at least the indicated many columns remain. Their sums of sizes 0..3 are all distinct by construction. QED.

**Critical difference from the unit T4/T6 accounting:** weighted patterns may introduce equal-size collisions that **did not exist** with all-one coefficients. Therefore U_2 and U_3 sum over ALL **potential** disjoint signed patterns, not only the previously counted unit-model minimal collision supports T4 and T6. Substituting the old small T4/T6 values into D5 is UNSOUND. D4's component balance and singleton exclusions are the exact filters that make U_k potentially manageable.

Exact *bounded* verifier [weighted_alteration_risk](../../research/hyp105_g5d_trade_rank.py) enumerates all unordered P/Q for at most 9 columns and evaluates each b as an exact Fraction; independent tests check combinatorial event counts (for n=7: 105 pair events and 70 triple events), rational score equality and a strict n>9 computation cap. The **theorem** is all-m, whereas this direct computation is intentionally finite and small. For large W(3,s) candidates we need exact combinatorial formulas/DP/spectral bounds on U_k rather than evaluating O(N^6) events directly.

**A real asymptotic GO from D5:** identify an all-s family B_m with N_m=Omega(m^(8/3)) and prove upper exponents U_2(B_m)=O(m^b4), U_3(B_m)=O(m^b6) such that b4<52/15 and b6<4, respectively. The same optimization used in C2 then implies an actual new GF5 ASET lower power >12/5. Conversely, if B_m has many dangerous low-rank supports, the risk sum may exceed the old unit trade counts and D5 need not help. That is an open quantitative mathematical question, not a solved bound.

## 4. WHY this does not yet solve the infinite problem

With GQ(s,s), N_s~s^4 and ambient dimension m~s^(3/2), the number of k-sum signatures that the greedy extension must avoid grows polynomially in N_s. Yet a fixed support-four pattern has **only 51** checksum-compatible choices over GF5, independent of m. The naive pigeonhole argument for availability of one of these 51 eventually fails: no theorem ensures one candidate survives all prior constraints.

A random weighting bound on any fixed at-most-six-column collision event has a **constant-size local system of field equations** (at most 24 nonzero coefficient variables, 12 touched coordinates); for fixed q=5, the probability scale per fixed combinatorial pattern is generally a constant rather than m^{-epsilon}. Consequently, random weights alone do not automatically reduce T6's *exponent*; any asymptotic gain must exploit dependence, constraints, geometry or an improved independence/deletion theorem. This is a concrete mathematical difficulty worth researching, not a reason to stop.

**Three hard follow-up directions and falsifiable claims:**

A. **Weighted-rank trade spectrum:** For every candidate signed pattern on <=6 columns, build the linear system in the 3 free GF5 coefficients per column after enforcing L(a_i)=4. Compute its exact rank, consistency and number of nonzero solutions; classify trade patterns of **all cardinalities**, using the checksum lemma to exclude imbalance. Prove uniform all-s bounds on the number of low-rank dangerous local configurations under a parameterized support graph, not finite extrapolation.

B. **Algebraic field-coefficient assignment:** Design a rule assigning 51-patterns using symplectic/geometric vertex labels, traces and projective invariants for all s=2^h, rather than a seeded bounded greedy ordering. Prove there are NO balanced 2-vs-2 or 3-vs-3 relations for enough of the E_s~m^(8/3) columns, or count their minimal supports sharply. The graph's GF(2^h) field and the target coefficient field GF5 are distinct and cannot be multiplied together as if they were the same field.

C. **Conflict-local hypergraph theorem:** Study degrees Δ_t and overlaps/codegrees of the *potential weighted collision event hypergraph*, not only total unit T4/T6. Constructive local lemma, containers, nibble or polynomial methods only when their exact hypotheses and dependency costs have been verified. A partial improvement of log factors over Lefmann 2005 would already be mathematical progress if original and proved.

## 5. Source priority and acceptance

Existing [Naor–Verstraëte 2008](https://doi.org/10.1007/s00493-008-2195-2), LIT-152, provides the genuine O(m^(8/3)) ASET upper. Existing Lefmann 2005, LIT-043, gives the linear and hence ASET lower Omega(m^(12/5)(log m)^(1/5)). [Liu–Shangguan–Zhang 2026](https://arxiv.org/abs/2605.11949), LIT-005, treats union-free hypergraphs, **not equal sums over GF5**; cannot claim a reduction without proof. These are reused without duplicate bibliography identities.

**Acceptance:** proved D1/D2/D3 statements, exact 51 palette, deterministic full 45-column W32 GF5 ASET witness with independent 15,226-signature verification (or an explicit falsified smaller result if the independent oracle finds a counterexample), corruption/held-out tests, and SUCCESS on exact PR-head GitHub-hosted research CI. Never promote a finite 45-vector result to an all-m theorem, original extremal discovery or Rust crate.
