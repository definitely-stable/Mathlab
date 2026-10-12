# HYP-105 E1-K3-G2-Q — original GQ anchor-square permanent identity and girth-eight cap

Date 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230); stack on [Draft PR #389](https://github.com/definitely-stable/Mathlab/pull/389), pinned parent exact HEAD 805e1145ff40287ed7759c27dc4126eb7eb6cd20. Keep main untouched; no merges; #230/#176/#169 OPEN. Parent exact-head Contract and INDEX SUCCESS, Research must be independently confirmed before acceptance. This gate is for *true original six-incidence supports*, not generic hypergraphs or independent physical label samples.

## 1. Reason to change direction from the fifth/sixth physical harmonics

P separated target Johnson levels through rank four, derived true 11x11 original-GQ/physical fourset coupling and proved the all-h induced-diamond exclusion. In the hardest real coherent W32 map, however, residual C5+C6 was strictly NEGATIVE in both independently checked original B/A and true GQ dual A/B (-56/11 and -167/42 respectively). Hence a generic termwise nonnegative high-harmonic lemma is FALSE. Bare Cauchy–Schwarz signed-residual estimates remain far too weak to prove the conjectured P2: U_BA(f,g)+U_AB(f,g)>=mu_f for every legal f,g.

This Q slice returns to the actual ORIGINAL six-incidence source construction. It discovers an exact local permanent expression with a **sharp universal constant 2** dictated by the GQ girth-eight incidence graph, obtaining a genuine quantitative pointwise improvement for W32 and a new physical/source-specific witness decomposition of ranks 5–6. It does NOT assert a universal positive P2/P7 theorem.

## 2. Theorem Q1 — ALL h exact original anchor-square identity

Let (P,L,E) be the ORIGINAL balanced generalized quadrangle W(3,s), s=2^h, V=(s+1)(s²+1), Delta=s+1, and f:P->E(K_a) a globally injective unordered physical pair map. Fix an unordered set R of six DISTINCT ORIGINAL right lines.

The B-left source weight w_f(R) is by definition the number of unordered ORIGINAL six-incidence supports with six distinct right line endpoints R, exactly five distinct left point endpoints, one left endpoint repeated twice, and a physical LEFT six-coordinate degree-two projection. No 6! weighting is included.

For any pair B={l_i,l_j} in R of meeting ORIGINAL lines, let p=p(B) be their UNIQUE intersection point. Define Sq_f(p) as the set of four-element sets Q of distinct ORIGINAL points such that the four distinct physical pair labels {f(q):q in Q} are the four edges of one SIMPLE physical C4 on four physical coordinate symbols completely disjoint from the physical pair f(p). There are at most 3*C(a-2,4) such squares (and exactly 3 if a=6 and f is a full K6 bijection).

For the remaining four lines D=R\B and the four square points Q, form the ORIGINAL 4x4 binary incidence matrix A(D,Q) with A_{l,q}=1 iff (q,l) belongs to the ORIGINAL E. Its permanent counts every distinct bijection matching the four residual lines to the four C4 point origins.

The exact identity for ALL h and any legal f is

    w_f(R) = sum_{B subset R, |B|=2, l_i intersects l_j}
                 sum_{Q in Sq_f(p(B))}
                    perm(A(R\B,Q)).

Proof of bijection: in any B-left accepted support the repeated original point p contributes two incidences and therefore consumes degree two at BOTH physical coordinates of f(p). The four other original points occur once each, have distinct physical pair labels by injectivity, and must form a simple four-edge degree-two graph on exactly FOUR disjoint physical coordinates; hence they form a C4. The two original right lines at the repeated point are uniquely determined, and the remaining four original incidences are a bijection between the four distinct right lines and the four distinct C4 points, counted exactly by the permanent. Conversely every such anchor pair, C4 square and perfect matching gives exactly one valid six-incidence support. There is no double counting between anchors because the repeated original left point is unique.

The genuine original GQ dual (L,P,E^op,g,f) obeys a SEPARATE exact identity of identical form for its source weights; physical target overlap is evaluated using the ORIGINAL complementary f or g, not fabricated independently optimized maps.

## 3. Theorem Q2 — sharp ALL-h girth-8 4x4 permanent bound

In the incidence graph of a generalized quadrangle there are NO cycles of length 4 or 6 (girth is 8). Hence every 4-by-4 sub-incidence matrix A formed from distinct original points and lines satisfies

    0 <= perm(A) <= 2.

Proof: two distinct perfect matchings in its bipartite graph have a symmetric difference comprising disjoint alternating cycles. Because cycles shorter than eight are forbidden and there are only eight vertices, they differ along a SINGLE alternating eight-cycle. Fixing M0 as identity, each other perfect matching is a permutation of relative cycle type (4), hence odd. If two other matchings M1,M2 existed, their relative permutation would be even, contrary to the required odd four-cycle. Thus there are at most TWO. A lone C8 achieves two, so this bound is sharp on the class of all girth-eight 4x4 bipartite graphs.

The independent finite proof gate additionally checks ALL 2^16=65536 possible binary matrices:
- 16217 have no 4- or 6-cycle;
- 11321 have permanent zero, 4824 have permanent one, and 72 have permanent two;
- ZERO have permanent exceeding two.

This enumeration certifies a fixed 4x4 combinatorial lemma, which then applies at arbitrary GQ order s, not merely at W32.

Combining the anchor-square identity, the 3*C(a-2,4) possible physical squares at each anchor, and Q2 gives the genuine all-h **pointwise source cap**

    0 <= w_f(R) <= 6*C(a-2,4)*e_GQ(R),

where e_GQ(R) counts ORIGINAL meeting line pairs among the six right lines. Taking the minimum with O's earlier Delta^4*e_GQ(R) gives

    w_f(R) <= min( (s+1)^4, 6*C(a-2,4) ) * e_GQ(R).

For W32/K6 this improves the former e_GQ coefficient **81 to 6**, a factor **13.5**. For W34/K14 the new coarse coefficient 2970 is WORSE than Delta^4=625, so the combined theoretical cap remains 625; it is crucial NOT to advertise an all-h asymptotic exponent improvement. Even where the coarse cap is not better, the exact geometry, Hall feasibility and individual permanent-1/2 terms remain valuable constraints.

A stronger local exact bound is w_f(R) <= 2 times the number of anchor-square pairs for which the four-line/four-point bipartite graph has a perfect matching. Hall-infeasible local squares contribute ZERO. This is much more specific than mere one-/two-point source moments or a generic nonnegative weighted rank-six hypergraph.

## 4. Exact finite independent original and dual W32 certification

The W32 oracle loops over ALL C(15,6)=5005 ORIGINAL distinct right-line source subsets R, not merely physical pair sixsets. For each real meeting pair of R it obtains its UNIQUE ORIGINAL shared point p and the 3 actual physical LEFT squares of f(p). It builds a 4-by-4 ORIGINAL incidence submatrix from four residual right line IDs and four distinct square-point IDs, independently checks its girth and counts its permanent exactly in {0,1,2}. It therefore constructs from first principles TWO source ledgers:

    n1(R) = # local anchor-square 4x4 matrices with perm=1
    n2(R) = # local anchor-square 4x4 matrices with perm=2
    w_f(R) = n1(R)+2*n2(R).

It independently rebuilds the full C0 source_weighted_BA_hypergraph from the unrelated preexisting original six-incidence generator, and FAILS on any sixset with a different weight, including omitted zero weights. This validates the new ALL-h identity on every W32 true original source R, NOT just the sample accepted physical overlap events.

For each same coherent original model (lex and previously sealed hardest correlated plus whole left original swap (13,14)) the oracle repeats on the genuine ORIGINAL incidence transpose for A/B and independently full B0 seven-family source census. It also partitions the signed physical target Johnson H5+H6 residual by local matching multiplicity:

    C56(f,g)= C56_perm1(f,g) + C56_perm2(f,g)
    C56_perm1 = sum_R n1(R)*(t5+t6)(g(R))
    C56_perm2 = sum_R 2*n2(R)*(t5+t6)(g(R)).

These terms come from TRUE original 4x4 permanent witnesses, not a synthetic independent rank-five sketch. Their sum must independently equal P's already sealed original/dual C56 (-56/11 and -167/42 on the hardest map, and -383/924 and 122/33 on lex), with separate complete original C0 weighted physical six-target overlap and B0 original seven-family checks.

The Q local decomposition shows exactly which *source incidence perfect matchings* carry negative rank5/6 residuals. It does NOT force these contributions to be nonnegative, and it does not turn the stronger source weight cap into a uniform target overlap minimum.

## 5. Acceptance, falsification and scientific status

Dedicated GitHub-hosted Contract only, no redundant 223-map prior corpus or repeated research test suite:
1. full 65536 matrix girth/permanent lemma with sharp two witness and invalid-cycle negative cases;
2. explicit GQ projection axiom validation for real W32/W34, all-h physical square catalog, non-surjective K7 map and fail-closed fake incidence/labels;
3. complete 5005 original right sixset source permanent weights independently equal to the prior original C0 six-incidence oracle, sharpened pointwise 6e cap;
4. independently full original and real dual B0/C0 for two coherent W32 models (four source maps), signed fifth/sixth rank split from local permanent-one/two counts, exact original full-Johnson spectral agreement;
5. SHA256/exact scalar seals after initial hosted green; exact-final-head Contract, INDEX and full Research must succeed, followed by independent mathematical review. Remain stacked Draft, no main change/merge.

**Proved ALL h:** exact original GQ source anchor-square/permanent identity, sharp 4x4 girth8 permanent cap two, improved source pointwise bound min(Delta^4,6*C(a-2,4))*e_GQ. **Finite exact:** W32 complete original and dual permanent source reconstructions and signed rank56 decomposition on stated maps, not exhaustive over global f,g injections. **NOT proved:** the conjectured all-f,g P2, seven-family P7, all-h S=Omega(s6), all-h charge K, full R3 upper, or any strict ASET exponent.

## 6. Next K3-G2-R decision

K3-G2-R should use this new small-permanent/Hall local structure to formulate a **genuinely joint ORIGINAL+DUAL coercivity lemma**, conditioning on global physical pair labels shared across f and g. Candidate: bound negative rank5/6 perfect-matching witnesses by positive original/dual 2-factor completions through an explicit common ORIGINAL incidence Hall/charging object. Test feasibility on the complete original sixsource ledgers first and prove all-h only if the geometric injection is truly uniform. Do NOT infer P2 from an upper bound on w_f, and do NOT turn a negative C56 or finite positive margin into an all-label universal conclusion.
