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
