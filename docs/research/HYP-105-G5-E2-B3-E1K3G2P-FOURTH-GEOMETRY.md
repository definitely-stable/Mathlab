# HYP-105 E1-K3-G2-P — exact fourth Johnson graphlets and GQ diamond exclusion

Date 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked Draft child of [PR #388](https://github.com/definitely-stable/Mathlab/pull/388), parent exact HEAD f5d61705bfae3c02e847952e9736a40b29da17f6. No merge/main modification; keep #230/#176/#169 OPEN. Contract/INDEX/full Research at final HEAD and independent mathematical review required before acceptance.

## 1. Why K3-G2-O does not resolve P2

Previous O proved all-a physical H3 on five triple-edge orbits and the genuine original-GQ sixth-order cherry restriction. It also constructed true ORIGINAL GQ×physical 4x5 triple tensors, independently recovering signed H3. However the target high-rank energies at a=6 are E3=710/1001 and E4+E5+E6=4966/77, so H3 covers only about 1.09% of ranks 3–6 target energy. We need to distinguish rank four and impose actual GQ structural restrictions; a generic source/target L2 Cauchy–Schwarz estimate is not enough.

## 2. Theorem P1: exact all-a fourth Johnson harmonic via 11 physical graphlet shapes

Let a>=6, K=C(a,2), k=6, target T_a be all 70*C(a,6) simple 6-edge physical 2-factors with exactly six physical coordinate vertices. Denote p=|T_a|/C(K,6), and h2,h3 the exact physical target lower harmonic coefficients proved in N and O.

Every set F of four distinct physical K_a pair edges belongs to exactly **eleven** simple unlabeled 4-edge graph types (isolated physical coordinate vertices ignored). For a shape with v occupied physical vertices and automorphism group of size Aut(F), the full physical orbit population is

    population_a(F) = (a)_v / |Aut(F)|, or 0 if a<v.

The complete shape representatives and automorphism factors are independently recovered by enumerating ALL C(28,4)=20,475 four-edge subsets of K8 once, grouping by connected-component edge count and component degree multiset, then counting true vertex automorphisms. These eleven signatures are complete (not arbitrary categories), and their populations sum exactly to C(C(a,2),4) for every a>=6.

For each physical shape F with v<=6, let c4,6(F) be the exact target codegree among the seventy K6 two-factors that CONTAIN its four edges; it is independent of the representative (S6 symmetry). Then the ALL-a true codegree equals

    c4,a(F)=c4,6(F)*C(a-v,6-v) if v<=6; zero otherwise.

This is a finite but complete classification proof, extended all a by choosing the remaining 6-v physical coordinates. It uses genuine simple 2-factors; the six target incidences are distinct, no artificial multiplicity or 6! normalization.

For H2(F)=sum_{B subset F,|B|=2}h2(B) and H3(F)=sum_{A subset F,|A|=3}h3(A), the unique rank-four Johnson down-harmonic coefficient is

    h4(F)=[
      c4,a(F) - p*C(K-4,2)
      - C(K-6,2)*H2(F)
      - C(K-7,2)*H3(F)
    ]/C(K-8,2).

This follows from the standard Johnson inclusion-matrix eigenvalue C(K-2j,k-j) on harmonic level j and the exact j=4 down-incidence residual. Consequently the physical target rank-four lift on a sixset S is

    t4(S)=sum_{F subset S, |F|=4} h4(F),

and its exact squared energy is

    E4(a)=C(K-8,2)*sum_{11 types F}population_a(F)*h4(F)^2.
    E_ge5(a)=|T_a|-|T_a|^2/C(K,6)-E2(a)-E3(a)-E4(a).

At a=6, independent complete Johnson ranks 0..6 from N give E4=86/7 and E5+E6=4020/77. The new eleven-orbit formula must independently reproduce the lift t4 on ALL C(15,6)=5005 physical sixsets, not only its energy, and all real physical 4-subset target codegrees for a=6 and a=9.

The graph orbit classification and all-a inclusion-matrix formulas are established combination/design methods; mathematical novelty relative to prior art is **not asserted** merely from applying them to this particular T_a target.

## 3. Theorem P2-GQ (not conjecture P2): all-h original induced diamond exclusion

In the ORIGINAL line-intersection graph of W(3,s) (balanced genuine generalized quadrangle), any three pairwise intersecting lines MUST be concurrent. Therefore four distinct original lines **cannot** induce the five-edge diamond graph K4-e. Proof: if A,B,C are mutually intersecting, they meet at a unique common original point x. If D intersects A and B, their triple is mutually intersecting and hence all three meet at x; D therefore intersects C too. This rules out the diamond on every four ORIGINAL lines for all s=2^h, independent of arbitrary physical labels.

The same concurrency argument implies each complete clique of intersecting original lines lies in one pencil and hence has size at most s+1. Consequently ORIGINAL W(3,2) with pencil size 3 cannot contain a K4. W(3,4) permits K4 from four of the five lines through an original point, but still forbids all diamonds.

This is a known corollary of the GQ no-triangle / unique-projection axiom, not a newly discovered general GQ theorem (see Brouwer & Haemers, *Spectra of Graphs*, §9.6.3 and contemporary literature on GQ collinearity clique geometry). Crucially it gives a genuine **structural zero row**, independent of physical global injections, in the next original/physical coupling tensor.

## 4. Exact 11x11 original GQ / physical graphlet fourth-order tensor

For each actual original W(3,s) pair injection f,g, each original right sixset R, and each four-subset Q of R, classify:
- original GQ line intersection graph induced on the four ORIGINAL line endpoints Q, into one of eleven unlabeled simple graphs on four vertices (canonical under S4);
- physical graph induced by the FOUR unordered pair labels g(Q), into one of eleven four-edge graphlet shapes.

The true coupled integer tensor is

    N_{u,v}(f,g)=sum_R w_f(R) sum_{Q subset R, |Q|=4}
                 1[original line graph(Q)=u]
                 1[physical four-edge graph(g(Q))=v].

It is computed from the SAME real original GQ incidences and the SAME global labels. Exact identities/restrictions:

    sum_{u,v} N_{u,v}=C(6,4)*sum_R w_f(R)=15*H_f
    N_{diamond,v}=0 for all 11 physical v and ALL legal s,f,g
    N_{K4,v}=0 when s=2
    C4(f,g)=sum_{u,v}N_{u,v} h4(v).

The exact rank-four contraction is checked independently against N's COMPLETE target Johnson J(15,6) rank-four spectrum, and against an entirely separate **source** rank-four projection using its zero-padded physical single, pair, triple and quadruple down-marginals. The general source formula is the triangular recursion

    h_j^W(A) = [m_j^W(A)
           - sum_{i<j} C(K-j-i,6-j)
             sum_{B subset A,|B|=i} h_i^W(B)
             ] / C(K-2j,6-j),  j=0..4,

where m_j^W(A)=sum_{S containing A}W(S), and unoccupied K_a physical pairs contribute zero source weights but remain in the denominator. Each source h_j down-kernel is independently tested and its energy E_j^W=C(K-2j,6-j)*sum_A h_j^W(A)^2 is exact. The residual E_ge5^W=||W||²-sum_{j=0}^4 E_j^W is nonnegative.

Consequently the precise remaining rank-five/six signed correlation satisfies

    C56^2 <= E_ge5^W * E_ge5^T.

This is again a rigorous upper bound on magnitude, not a source-specific signed coercivity theorem.

Both B/A and genuine ORIGINAL GQ dual A/B are re-evaluated from independent original-source C0 and complete B0 seven-family finite W32 oracles, with the same coherent global f,g. No independently sampled source and target or surrogate physical label multiplicities are substituted.

## 5. Fail-closed hosted acceptance and K3-G2-Q decision

Run dedicated focused Contract only, no redundant full 223-map corpus:
1. all 11 physical graphlet types, full physical K6 and K9 target 4-subset codegrees, and exact all-a target orbit populations;
2. rank4 target energy and lift on **every** 5005 physical K6 sixset, independently versus N's seventh-level exact Johnson decomposition;
3. ORIGINAL GQ W32 induced four-line counts and forbidden diamond, W34 independent *full triangle-plus-fourth-line* diamond witness check (tests every possible diamond without brute 2m original foursets), and W34 concurrent K4 check;
4. four real original/dual fourth-order tensors for the lex and previously sealed hard W32 source, exact three-way C4 equality, no-diamond/no-W32-K4 tensor row zero and independent source rank0..4 energies and residual CS rank5/6 inequality.

Required exact final HEAD dedicated Contract, INDEX and full Research SUCCESS plus independent mathematical review before PR acceptance. Keep stacked Draft and root issues OPEN.

**What this does not prove:** the universal all-h two-family conjecture U_BA+U_AB>=mu_f, the seven-family S>=mu_f, Branch A/B S=Omega(s^6), all-h charge K, full R3 upper or any ASET exponent. The new forbidden GQ tensor rows constrain the combinatorial **feasibility region**, but do not by themselves bound the signed C5+C6 enough to force P2.

**Next K3-G2-Q:** exploit the true ORIGINAL incidence geometry of five and six original right-line endpoint sets (including concurrent-pencil/cycle exclusions) and both real dual source hypergraphs to derive feasible inequalities for C5+C6, or find a legitimate actual coherent f,g counterexample. Avoid claiming that a new rank decomposition is already a positive obstruction.
