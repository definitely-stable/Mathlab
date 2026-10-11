# HYP-105 C24-B8-A — exact physical-motif tensor and signed cross differences

Root: [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked parent: [C24-B7 PR #354](https://github.com/definitely-stable/Mathlab/pull/354) exact HEAD `c35d6e4f9c1f60d8d5ae0b84a8e1995b08fbb75c` (B7 Contract, six-shard Research + aggregate, INDEX SUCCESS). Separate branch; **no main change or merge**.

## Scope and frozen original requirements

For each h>=1 set s=2^h, let W(3,s) be the ORIGINAL point-line generalized quadrangle, with V=(s+1)(s^2+1) points and V lines. Its incidence set I has |I|=(s+1)^2(s^2+1). Fix a=min{a: C(a,2)>=V}; **one injective global** physical K_a-edge map f for ALL original points and **one injective global** map g for ALL original lines. Both share the same coordinate universe but may assign physical pairs independently by side.

An original source J is a **set of exactly six distinct incidence edges**, not a signed-flow event, compression record, or physical automorphism orbit. Its original point- and line-endpoint multiplicity profiles identify seven disjoint necessary GF(5) families:

1. D6: A/A with connected and matching left/right six-position dual cycles.
2. B-left/A-right; A-left/B-right.
3. C/A (A/C or C/A), C/B (B/C or C/B).
4. B/B-overlap; B/B-disjoint, distinguished by the single repeated-point/repeated-line original edge.

A=(1,1,1,1,1,1), B=(2,1,1,1,1), C=(2,2,2). This is EXACTLY the seven-family static partition in C24-B2. It is a necessary GF(5) floor, never asserted equal to entire R3.

## Theorem B8-A1: exact all-h seven-family tensor

For a six-source J with ordinary tag, let L_J(f), R_J(g) be Boolean indicators that the six images on that side form a physical 2-regular six-coordinate multigraph: exactly six physical coordinates, each of degree two (multiplicity retained). Its accepted ordinary indicator is **exactly**

    X_J(f,g) = L_J(f) R_J(g).

The sole exception is D6, whose physical 2-factors must be **connected six-cycles with the same dual incidence-position adjacency**, not merely two accepted 2-factors. The dual cycle on the SIX ORDERED ORIGINAL INCIDENCE POSITIONS is an element sigma of the 60 undirected Hamiltonian C6 cycles on six labels.

Let L_{J,sigma}(f) and R_{J,sigma}(g) be the one-hot indicators for such connected physical dual-cycle signatures, zero when physical eligibility or connectivity fails. Then

    X_J^D6(f,g) = sum_{sigma in C6} L_{J,sigma}(f) R_{J,sigma}(g).

All-h exact score:

    S_s(f,g) =
        sum_{J with one of 6 ordinary tags} L_J(f) R_J(g)
      + sum_{J with D6 tag} sum_{sigma in C6} L_{J,sigma}(f) R_{J,sigma}(g).

**Proof.** For ordinary tags the original static profile is independent of f,g, and acceptance imposes only the two physical 2-factor conditions, one for each side. For D6 the necessary positive GF(5) family requires both sides to have the same six-position connected dual cycle. Global injectivity ensures six distinct physical edge images for six different original point/line labels; a connected degree-two six-position dual graph is therefore a uniquely identified Hamiltonian C6. Hence at most one nonzero sigma on either side, and the dot product equals the exact acceptance Boolean. Sum over disjoint original sixset tags. No independence of distinct J or individual assignment to J is used. QED.

## Theorem B8-A2: exact all-h signed left/right mixed finite difference

Let A swap physical assignments of TWO original points in f, and B swap assignments of TWO original lines in g. These typed global actions commute. Use delta_A L = L(f^A)-L(f), delta_B R=R(g^B)-R(g). For the four true complete global maps,

    kappa_{A,B}^{LR} = S(f^A,g^B)-S(f^A,g)-S(f,g^B)+S(f,g)

and the exact signed decomposition is

    kappa =
        sum_{ordinary J} (delta_A L_J)(delta_B R_J)
      + sum_{D6 J} sum_{sigma in C6}
            (delta_A L_{J,sigma})(delta_B R_{J,sigma}).

**Proof.** For each scalar product uv apply (u+du)(v+dv)-(u+du)v-u(v+dv)+uv=du*dv. The D6 cycle signature sum is finite, so interchange differences and summation without any independence assumption. QED.

**A physically filtered deterministic support cap** follows:

    |kappa| <=
        #{ordinary J: delta_A L_J !=0 and delta_B R_J !=0}
      + 2 #{D6 J: delta_A L_J-vector !=0 and delta_B R_J-vector !=0}.

For each ordinary source, both Boolean differences are in {-1,0,+1}; for D6 each one-hot difference is zero, one unit vector, or a difference of two unit vectors and the scalar mixed product has absolute value <=2. This cap is a *true physical-change* bound, unlike B7's raw incident sixset touch universe. It is still a NON-SIGNED upper bound; no s^6 rate has been derived.

## Independent finite falsification

- Core code: `research/hyp105_g5e2b3e1c24b8a_physical_tensor.py`; all-h algebra is implemented on arbitrary original sixset input with two fixed globally coherent map pairs. No modification to the accepted B7 source and B2 classifiers.
- Fast independent tests: `research/test_hyp105_g5e2b3e1c24b8a_physical_tensor.py`. Tests seven original profiles, D6 connected/disconnected C6-vs-two-C3, an explicit true |kappa_D6|=2 example even though all four physical 2-factor Booleans are 1, and a finite ORIGINAL W32 subuniverse against the *separate B2* `reference_classifier` on all four maps. No full 11,236 orbit in unittest.
- Explicit isolated hosted witness: `research/hyp105_g5e2b3e1c24b8a_w32_tensor_witness.py`. Independently enumerate physical-left original sixsets under BOTH f0 and f^A, take the UNION (never unsafe reuse of one f-dependent compiled source), evaluate four maps with the new tensor. Compare four full scores to the preexisting compressed LEFT-first oracle and check decisive result with independently implemented RIGHT-FIRST 62,370-original-sixset census.
- Freeze actual previously certified B7 mixed examples: A=(3,8), B=(0,14), genuine (S00,S10,S01,S11)=(68,95,97,70), kappa=-54; and A=(4,14), B=(4,11), kappa=-70. Both test only ONE common global f,g rectangle per witness, not separately optimized maps.

The *independent reference* is a different original incidence enumerator/classifier, not another call to tensor code. The standalone heavy witness is not invoked in broad Unit tests.

## Why this is useful, and what is OPEN

B7 unrestricted mixed-source envelope M_c=C(E,6)-2C(E-d,6)+C(E-2d+c,6), E~s^4, d~2s, is Theta(s^18) when c=0 and Theta(s^20) when c>0, drastically looser than the desired S~s^6 obstruction. B8-A removes sixsets which fail the relevant *change of physical 2-factor* tests; D6 additionally demands a matched connected cycle signature. This is a rigorous identity and narrower search space, but **not** a proof that the filtered cap is O(s^6), not a signed descent lemma, and not a universal lower bound.

**Next B8-B theoretical target** (not asserted): estimate the signed six-incidence correlation tensor uniformly for all admissible f,g and all s=2^h, or construct a correlated infinite family f_s,g_s with o(s^6) seven-score. Exact mean-over-complete-injections identities could help, but a mean is not an infimum. In particular no replacement of six-way structure by pairwise GQ spectral statistics is justified (Pasch counterexample in C24-B1).

Status: **RESTRICTED_THEOREM_C (tensor identity only)** once latest-head hosted dedicated Contract + full Research aggregate + INDEX succeed. Until then **IMPLEMENTED_CI_PENDING**. Root issue #230 stays OPEN_WITH_FORMAL_BLOCKER; no all-h Branch A, no infinite Branch B, no full GF5 R3 upper, no claimed ASET improvement, no merge.
