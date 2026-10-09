# HYP-105 G5-E2-A — Explicit all-s GQ-to-coordinate-pair injections and GF(4) verification

Date 2026-10-09. Parent [#162](https://github.com/definitely-stable/Mathlab/issues/162), [#136](https://github.com/definitely-stable/Mathlab/issues/136), [#106](https://github.com/definitely-stable/Mathlab/issues/106), [#95](https://github.com/definitely-stable/Mathlab/issues/95). Predecessor [E1 proof and detailed E2–E5 plan](HYP-105-G5-E1-FLOW-MOTIFS-AND-NEXT-PROOF.md).

**EXPLICIT_ALL-h_SPARSE_SUPPORT_INJECTIONS / GF2_GF4_INDEPENDENT_FINITE_PROOFS / NO_ASYMPTOTIC_FLOW_RISK_ESTIMATE / NO_NEW_ASET_EXPONENT / NO_RUST.**

## 1. Scope and exact all-h theorem

Fix h>=1, the ordered finite field F_h=GF(2^h) and the symplectic generalized quadrangle W(3,s), s=2^h, whose points are normalized projective F_h^4 vectors and whose lines are totally isotropic projective 2-spaces. From the earlier independently proved classical symplectic theorem, each part has

    V_s = (s+1)(s^2+1) objects,

while the incidence graph has

    E_s = (s+1)^2(s^2+1) edges, all vertices degree s+1,
    girth exactly eight.

Put a_s = min{a>=2: binom(a,2)>=V_s} and m_s=2*a_s. Lexicographically list all binom(a_s,2) different unordered coordinate pairs (i,j), 0<=i<j<a_s; write U_a(r) for the pair of zero-based rank r. Give both point and line objects separately a specified total ordering (using fixed canonical field/projective representations) and map their ranks r=0,...,V_s-1 to U_a(r). Denote these maps f_s and g_s, with their images in DIFFERENT blocks of a_s coordinates. For each incidence (P,L), use a four-element GF5 sparse support consisting of pair f_s(P) plus pair a_s+g_s(L).

**Proposition E2-A1, for every h>=1 (ELEMENTARY CONSTRUCTION):** both f_s and g_s are injections. All E_s supports are distinct and each has exactly two coordinates in each block, so support weight four. Their two-pair factor graph is isomorphic to W(3,s), hence of girth eight. Also a_s=Theta(s^(3/2)), m_s=Theta(s^(3/2)), E_s=Theta(m_s^(8/3)).

**Proof:** The definition of a_s ensures at least V_s distinct pairs, and lexicographic pair unranking is a bijection. Distinct point/line ranks therefore have distinct pair labels. The blocks are disjoint. Equal physical four-supports imply equal their left pair labels AND equal their right pair labels, hence by injectivity equal point/line endpoints; since the original incidence graph is simple, the graph edges coincide. Inverting each pair map reconstructs every original incidence. The size estimates follow from binom(a,2)=a(a-1)/2 and V_s=Theta(s^3), E_s=Theta(s^4). QED.

**Crucial nonconclusion:** This proves a dense DISTINCT support universe for true GF5 four-sparse columns, NOT that the columns form an ASET family after assigning any weights. Graph girth eight does not prohibit signed GF5 collisions. No bound on R2 or R3 follows from this elementary mapping theorem.

## 2. Three explicit pair-label assignment controls

[Executable pair-injection module](../../research/hyp105_g5e2a_pair_embeddings.py) implements for h=1,2:

1. **lex:** sort normalized symplectic projective points and their isotropic line tuples lexicographically; independently inject the two rank sets into the same K_a pair alphabet in separate coordinate blocks.
2. **reverse-line:** retain point order but reverse the line list before pair-unranking; an independent reproducible permutation control, not a claimed improvement in asymptotic trade density.
3. **coordinate-flag:** choose a fixed polynomial-basis-dependent point sorting key involving p0*p2+p1*p3 in F_h, and an independent deterministic line key built from its incident point tuples and a field product aggregate. Ties are broken by the complete original tuple. These are explicit total orders, not a theorem of optimal symplectic group invariance. Coordinate-flag is a heuristic control, NOT a newly discovered all-s algebraic flow-risk suppression scheme.

Any ordinary permutation of the AMBIENT coordinate symbols alone leaves the signed-trade spectrum unchanged (C3-A). The fact that rank reorderings can produce distinct support sets does not show improved asymptotic risk. Future work must prove the typed motif multiplicity inequalities for a chosen explicit all-h rule.

The mathematical rank-to-pair definition is valid for all h once any reproducibly ordered GF(2^h) representation is selected. Our hosted executable intentionally caps full graph enumeration at h=1,2: computing GF(8) and all six-column trades by naive enumeration in GitHub CI would not constitute an asymptotic proof and risks unbounded runner cost.

## 3. Independent finite exact certificates and bounded diagnostics

| Graph field | s | Point vertices | Line vertices | Edge columns | Pair alphabet a | Ambient GF5 m |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| GF(2) | 2 | 15 | 15 | 45 | 6 | 12 |
| GF(4) | 4 | 85 | 85 | 425 | 14 | 28 |

[Independent regression](../../research/test_hyp105_g5e2a_pair_embeddings.py) verifies complete unranking of all pairs for a=2,6,14,35; three schemes at s=2 and s=4; exact injectivity on both sides; all 45 and 425 physical supports distinct and support-exact-four; inversion of every physical support back to its exact original GQ incidence endpoint pair; and graph girth eight. The graph arithmetic is true polynomial GF(4), not integers modulo four, and the actual sparse-column coefficient field remains GF(5).

A deterministic sample of EIGHT columns per scheme is classified using the E1 signed-flow core and canonical motif oracles; exactly

    binom(8,2)*binom(6,2)/2 = 210 distinct unordered 2-vs-2 events;
    binom(8,3)*binom(5,3)/2 = 280 distinct unordered 3-vs-3 events

are accounted for and either rigorously excluded by necessary structural rules or placed in a possible flow motif class. These samples are NOT unbiased estimators, do NOT cover all 425 columns, and establish no asymptotic upper risk bounds. Direct brute O(N^6) work on GF4 N=425 is explicitly prohibited.

Hosted reproducibility:

    python research/hyp105_g5e2a_pair_embeddings.py
    python -m unittest discover -s research -p "test_hyp105_g5e2a_pair_embeddings.py"

## 4. Detailed proof program E2-B through E5

**E2-B: genuine new all-h motif multiplicity theorem.** Let M_k(tau;B_s) count exact signed two-color coordinate-incidence motif realizations for the chosen s-dependent mapping. Already proved:

    R_k(B_s) = 51^(-2k) * sum_tau M_k(tau;B_s) F_tau(b;5).

All potentially positive motifs tau have at most 2k coordinate vertices in EACH coordinate half, so the motif TYPE SET is finite independent of s. This is not enough; find exact formulas or provable uniform upper bounds for the MULTIPLICITIES M_k. Use incidence geometry, projective flags, explicit collineation actions (ONLY if they preserve pair labels or if their induced change is controlled), and finite local graph embeddings. Prove constants uniform in h and both k=2 and k=3.

**Target sufficiency:** With N_s=Omega(m_s^(8/3)), prove R2=O(m^b4) with b4<52/15 and R3=O(m^b6) with b6<4 simultaneously, or prove a different stronger independent-set theorem. Only then can our existing alteration argument produce an actual new ASET LOWER power better than Lefmann's 12/5 with logarithmic factor. None of those inequalities is currently proved.

**E3: exact motif flow constants.** Use published Fu–Ren–Wang (2025), DOI 10.1016/j.aam.2025.102901, for exact prescribed-boundary nowhere-zero flow counts, and a certified small-template computation. An exact flow count per template is constant-cost in ambient m (but exponential in at most 24 incidence edges), unlike evaluating all O(N^6) events independently. Apply zero-demand bridge and singleton coordinate filters first; do not mistake a necessary filter for positive-flow sufficiency.

**E4: if simple totals fail, prove higher-order overlap control.** Develop degree/codegree bounds for the collision-event hypergraph, including shared random coefficient dependence, and check exact hypotheses before invoking LLL, hypergraph containers, semi-random nibble or derandomization. A new theorem improving the independent-set extraction would count even if the first-moment sufficient risk exponents fail.

**E5: separate genuine upper-bound theory.** Try stronger unrestricted ASET upper bounds via signed-sum additive energy and 4-uniform support incidence; do NOT silently replace full GF5 weighted ASET with all-one, graph girth or 3-union-free set systems. The published Naor–Verstraëte 2008 actual 8/3 upper is prior art.

**Method-level STOP already proved in E1:** Independent uniformly random pair labels along GQ have expected weighted R3=Omega(m^4) by the unit-collision floor, hence the AVERAGE weighted first-moment alteration certificate cannot beat O(m^(12/5)). This is NOT an obstruction to deterministic special labels, rare favorable random choices, correlated weights or stronger independence methods.

## 5. Source/novelty gates

Reused primary references: Lefmann 2005 six-wise sparse GF(q) lower with logarithm; Naor–Verstraëte 2008 genuine ASET upper 8/3; classical symplectic GQ; Fu–Ren–Wang 2025 assigning polynomials. None of the elementary pair ranking, GQ graph realization, projective basis sorting or finite sample results is claimed scientifically original. The intended genuinely new mathematical theorem is a **uniform all-h weighted GF5 nonzero-flow motif multiplicity/risk estimate**, or an independent improved upper bound.

**E2-A acceptance:** all-h injectivity/counts proof, s=2,4 independent exact finite tests, bounded reproducible motif diagnostics, exact PR-head GitHub-hosted Research SUCCESS. #162/#136/#106/#95 remain OPEN. No Rust; no non-Mathlab changes.
