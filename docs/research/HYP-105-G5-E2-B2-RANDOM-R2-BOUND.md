# HYP-105 G5-E2-B2 — An all-s expected four-trade risk bound for random GQ pair labels

Date: 2026-10-09. Parent [G5-E2-B #169](https://github.com/definitely-stable/Mathlab/issues/169), [G5-E #162](https://github.com/definitely-stable/Mathlab/issues/162), [G5-C3 #119](https://github.com/definitely-stable/Mathlab/issues/119), [#106](https://github.com/definitely-stable/Mathlab/issues/106), [#95](https://github.com/definitely-stable/Mathlab/issues/95). Predecessors [G5-E1 finite signed flow motifs](HYP-105-G5-E1-FLOW-MOTIFS-AND-NEXT-PROOF.md), [G5-E2-A explicit embeddings](HYP-105-G5-E2-A-PAIR-INJECTION-MODELS.md), [G5-E2-B1 exact disjoint energy](HYP-105-G5-E2-B1-EXACT-DISJOINT-ENERGY.md).

**PROVED_ALL-s_RANDOM_LABEL_EXPECTED_R2_UPPER / ELEMENTARY_MODEL_SPECIFIC_FOREST_AND_PAIR_CYCLE_COUNT / R3_UPPER_NOT_PROVED / NO_NEW_ASET_EXPONENT / WORLDWIDE_PRIORITY_UNVERIFIED / NO_RUST.**

## 1. Frozen probabilistic/field model

For each s=2^h, h>=1, use the **classical** symplectic W(3,s) incidence bipartite graph G_s with V_s=(s+1)(s²+1) point vertices on one side and as many line vertices on the other, E_s=(s+1)²(s²+1) edges, maximum degree Delta_s=s+1, girth exactly 8. This known geometry is independently proved and field-checked in accepted B1.0.

Set a_s=min{a>=2:binom(a,2)>=V_s}, m_s=2a_s. Independently choose TWO uniform injective vertex labels into the binom(a_s,2) unordered coordinate pairs, one for each part of G_s; these are finite probability spaces with exactly (binom(a_s,2))_(V_s) choices per side. Every graph edge receives a DISTINCT four-coordinate support with two coordinates per block. Define R_2(B_s) as in E0: for all disjoint, unordered pairs of size-two column-ID sets, sum their exact signed GF5 collision probabilities when each column independently receives a uniformly chosen one of the 51 nonzero coefficient 4-tuples whose sum is 4. The expected value E_label[R_2(B_s)] is over the **random pair-label injections only**, while R_2 already averages over the independent coefficient assignments.

No independently random *supports*, no random GQ graph, and no GF(2^h) coefficient arithmetic: graph geometry over GF(2^h), actual weighted ASET vectors over GF(5).

## 2. E2-B2.1 — complete projected four-edge 2-core probabilities

Fix four DISTINCT graph edges, and consider one side of the factor graph. Their endpoints may have r=1,2,3,4 distinct factor vertices; their incidence multiplicities form a partition lambda of 4. Under uniformly random injective labels of these r distinct vertices to distinct coordinate PAIRS of K_a, the four resulting pair edges, with multiplicities lambda, form a multigraph on physical coordinates.

If ANY physical coordinate has projected degree ONE, then a nonzero GF5 2-vs-2 trade is impossible, by E1's exact nowhere-zero flow coordinate divergence constraint. Therefore we need the necessary *leafless* projected pair multigraph.

**Lemma B2.1 (EXACT, all a>=6).** Put B=binom(a,2), and (x)_r=x(x-1)...(x-r+1). The probability p_a(lambda) that the four projected pair-edge occurrences have NO coordinate of degree one is:

| Factor endpoint multiplicities lambda | Probability |
| --- | --- |
| 4 | 1 |
| 3+1 | 0 |
| 2+2 | 1 |
| 2+1+1 | (a)_3/(B)_3 |
| 1+1+1+1 | 3(a)_4/(B)_4 |

**Proof by exhaustive structural classification:** For 4, every one of the two endpoints has degree four. For 3+1, the unique other PAIR is distinct and has at least one unmatched coordinate of degree one. For 2+2, both distinct pair edges occur twice, so no physical endpoint has degree one. For 2+1+1, the two singly occurring distinct pair edges must meet at one fresh coordinate and attach their other endpoints to the endpoints of the twice-occurring pair: the three distinct pairs must form a triangle on exactly three physical vertices; there are (a)_3 ordered distinct labelled-edge assignments making a triangle among (B)_3 possible assignments. For 1+1+1+1, the four different unordered coordinate-pair edges form a SIMPLE four-edge graph with minimum nonzero degree two. It must be a simple 4-cycle: it cannot use <=3 vertices (at most three simple edges) or more than four vertices (sum degrees=8); there are 3 binom(a,4) simple squares, and 4! assignments to four named factors, hence 72 binom(a,4)=3(a)_4 favourable ordered maps out of (B)_4 total. QED.

Thus, with a=Theta(s^(3/2)), p_a(2+1+1)=O(s^(-9/2)), and p_a(1+1+1+1)=O(s^(-6)); the other nonzero probabilities are at most one. Constants are absolute, independent of h. The two projected coordinate-half label injections are independent, so conditional on any fixed four graph edges the two leafless events multiply EXACTLY.

**Independent finite checks:** the executable oracle enumerates all injective maps of r named pairs for a=4,5,6, checking each exact rational formula against literal coordinate degree computations, not against the symbolic formula itself.

## 3. E2-B2.2 — all-s four-edge FOREST upper-count theorem

Since the incidence graph G_s has girth eight, ANY subgraph on four distinct selected edges is a FOREST (the only possible cycle of length <=4 in a simple bipartite graph is a four-cycle, which G_s excludes). Let r_L,r_R be the numbers of distinct used left and right FACTOR graph vertices, and c=r_L+r_R-4>=1 the number of connected components in this forest. Each factor endpoint has one of the above multiplicity profiles lambda_L/lambda_R.

**Classical forest embedding bound.** For ANY fixed bipartite abstract four-edge forest with c components, the number of injective realisations as four distinct selected labelled incidence edges of a bipartite graph with at most V_s vertices on each side and maximum degree Delta_s is at most

    V_s^c * Delta_s^4

up to a UNIVERSAL finite factor for choosing edge/component labels (at most a constant depending only on the four-edge abstract shape, NEVER on s). Proof: choose one correctly typed root host vertex per component (at most V_s options each); orient each rooted tree outward and choose the neighbour of each already mapped parent along each of four edges (at most Delta_s options per edge). This may also count invalid/repeated candidates, so is a valid upper bound. Only finitely many abstract four-edge shapes exist.

For a forest factor shape with profiles lambda_L and lambda_R, multiply this embedding bound by the two exact independent pair-label leafless probabilities p_a(lambda_L)p_a(lambda_R). Write d(4)=d(2+2)=0, d(3+1)=infinity (excluded), d(2+1+1)=9/2 and d(1+1+1+1)=6, where p_a(lambda)=O(s^(-d(lambda))). Since V_s=Theta(s^3), Delta_s=Theta(s), each shape contributes at most

    O( s^[ 3(r_L+r_R-4)+4-d(lambda_L)-d(lambda_R) ] )

to the EXPECTED number of four-edge supports with BOTH coordinate projections leafless. The proof holds for EVERY h, not a fitted empirical exponent.

**Complete finite 4-edge shape audit:** there are Bell(4)=15 partitions of four named edge positions on each factor side, 15²=225 possible pairs before excluding duplicated edges, cycles, and zero-probability profiles. Up to exchange of left/right factor halves, all potentially positive profile combinations compatible with a forest yield the following worst-case powers of s:

| Left factor profile | Right factor profile | c | Maximum exponent in s |
| --- | --- | ---: | ---: |
| 4 | 1+1+1+1 | 1 | 1 |
| 2+2 | 2+1+1 | 1 | 5/2 |
| 2+2 | 1+1+1+1 | 2 | 4 |
| 2+1+1 | 2+1+1 | 2 | 1 |
| 2+1+1 | 1+1+1+1 | 3 | 5/2 |
| 1+1+1+1 | 1+1+1+1 | 4 | 4 |

No profile with 3+1 survives; no 4-edge factor four-cycle can occur, so 2+2 on both factor halves is impossible. Every positive shape has exponent <=4, therefore

    E_label[ number of four-edge supports that are leafless
             in BOTH coordinate projections ] = O(s^4).

Both the structural forest counting argument and the finite 225-case table are quantified for all s=2^h. The Python case generator is a falsification oracle for the finite table, not a stand-in for the all-s proof.

## 4. E2-B2.3 — genuine partial all-s weighted GF5 risk upper

**THEOREM (all s=2^h; random pair labels; true GF5 weighted risk).**

    E_label[R_2(B_s)] = O(s^4) = O(m_s^(8/3)).

**Proof.** A prescribed disjoint two-vs-two signed event consists of exactly four distinct factor edges, and there are exactly three unordered 2-vs-2 sign partitions per unordered four-edge set. Its probability under the 51-pattern GF5 nonzero coefficient assignment is between zero and one. By the physical-coordinate GF5 divergence obstruction, it is ZERO unless each of the TWO coordinate projected pair multigraphs has no vertex of degree one. Therefore for ANY fixed pair labeling,

    0 <= R_2(B_s) <= 3 * number_of_four_edge_sets_leafless_in_both_projections.

Take expectations over the two independent uniform injective vertex-pair labelings. By the complete all-s forest/projection analysis in Section 3, the right side is O(s^4). The relation m_s=Theta(s^(3/2)) from E2-A yields s^4=Theta(m_s^(8/3)). QED.

**Existential corollary (still not an ASET exponent).** Since R_2>=0 and its average is O(m^(8/3)), at least one deterministic pair labeling for every s has R_2=O(m^(8/3)), with an absolute constant uniform in s. Markov also yields a constant-probability comparable bound over uniform random labelings. **This says NOTHING about R_3 for the same selected labeling.**

This **DOES meet the b4<52/15 threshold for R2 by itself** (b4=8/3<52/15) within the average/there-exists-for-R2 model. It does NOT establish the simultaneous R3 threshold and hence does NOT prove any better ASET lower exponent. Existing C2-D and E1 prove that the SAME independent random labeling distribution has E_label[R_3]=Omega(m^4), i.e. fails the strict sufficient b6<4 threshold *in expectation*. This lower average does not exclude rare good labels, stronger extraction, or deterministic correlations.

## 5. Executable independent regression

- [Exact symbolic forest/projection table](../../research/hyp105_g5e2b2_random_r2.py) enumerates all 225 two-factor endpoint equality partitions, forbids repeated selected factor edges and factor cycles, enforces exact split coordinate projection probability formulas and proves the largest exponent among all positive templates is 4. It outputs a deterministic JSON theorem/caveat report.
- [Independent falsification tests](../../research/test_hyp105_g5e2b2_random_r2.py) independently enumerate all injective K4/K5/K6 coordinate-pair label assignments to check every possible four-edge multiplicity pattern (including 3+1 impossible), crosscheck every two-factor equality partition forest decision against an unrelated graph DFS component/edge-count oracle, pin maximal symbolic power=4, check field GF2/GF4 actual symplectic point/line edge quartets are forests, and assert no claim of an R3 upper/new ASET exponent.
- There is **no direct O(N^4) run** for N=425 symplectic GF4 edges; the classification is symbolic and quantified for ALL h.

Sources/priority: the finite symplectic generalized quadrangle is CLASSICAL; all such geometries have no 4/6-cycles in their incidence graphs. Basic forest embedding counting, random injective pair maps, triangle/C4 counts in complete graphs, and first-moment/Markov are classical combinatorial tools. This is an application to the HYP-105 model; independent worldwide scientific priority is NOT established. Lefmann 2005 prior ASET/linear lower, Naor–Verstraëte 2008 genuine ASET upper, Fu–Ren–Wang 2025 general nowhere-zero boundary flow all remain properly attributed.

**Next actual hard proof E2-B3:** find a special all-h correlated pair-label construction or a stronger signed-event hypergraph independence argument giving strict R3 exponent <4 in the SAME family as the proved R2 bound. It is logically invalid to combine a merely existential good R2 labeling with a separately existential good R3 labeling unless their simultaneous existence is established. Root #169/#162/#106/#95 stay OPEN. No Rust or changes outside Mathlab.
