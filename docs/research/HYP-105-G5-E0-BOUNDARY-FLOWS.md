# HYP-105 G5-E0 — Exact nowhere-zero boundary-flow interpretation of GF5 signed trades

Date 2026-10-09 · [asymptotic research gate #162](https://github.com/definitely-stable/Mathlab/issues/162) · [merged weighted GF5 D1–D5 research #160](https://github.com/definitely-stable/Mathlab/pull/160) · parent [#106](https://github.com/definitely-stable/Mathlab/issues/106) and [#95](https://github.com/definitely-stable/Mathlab/issues/95).

**MODEL-SPECIFIC EXACT REDUCTION / REPROVED_CLASSICAL_BOUNDARY_FLOW_COUNT / NO_WORLDWIDE_ORIGINALITY / NO_NEW_ASET_EXPONENT / NO_RUST.**

## 1. Primary-source novelty audit BEFORE promoting a theorem

Our G5-D theorem D4 gives exact collision probability 5^(C-v) for full affine checksum4 weights including zeros, and a conditional upper bound for all-nonzero 51-pattern weights. We can do better: obtain an exact finite count of collision-producing **nonzero** weights. However the underlying graph-flow counting identity is already published and MUST be acknowledged.

- **Fu, Ren, Wang, *Counting flows of b-compatible graphs*, Advances in Applied Mathematics 168 (2025), 102901.** [Primary publisher DOI](https://doi.org/10.1016/j.aam.2025.102901), [authors' arXiv manuscript](https://arxiv.org/abs/2409.09634). Their Theorem 1.1 explicitly gives the prescribed-boundary nowhere-zero finite-group flow count via inclusion-exclusion over b-compatible spanning subgraphs. Theorem 1.3 addresses assigning polynomials. This general identity **precedes** Mathlab G5-E0.
- **Beck–Zaslavsky, *The number of nowhere-zero flows on graphs and signed graphs*, JCTB 96(6), 2006.** [Publisher DOI](https://doi.org/10.1016/j.jctb.2006.02.011), also discusses the classical flow-polynomial theory. Do not conflate signed-graph flows with the *signed coefficients* of our ordinary bipartite incidence graph without an explicit transformation.

**What we prove for Mathlab** is an exact *model translation* from nonzero checksum-constrained GF5 ASET signed trades to prescribed-boundary nowhere-zero flows, plus a independently implemented finite check. The idea may be useful, but independent publication novelty is NOT established. Both linked sources are relevant candidates for canonical LIT registration; bibliography currently has another open indexing PR, so do not assign fabricated IDs here.

## 2. E0 theorem: complete count of admissible GF5 trade coefficient assignments

Fix t columns of support exactly 4, prescribed signs ε_i∈{+1,-1}, and incidence bipartite graph G:
- left vertices c_i for the t columns;
- right vertices x_j for each distinct touched coordinate;
- an edge e=(c_i,x_j) whenever j lies in column i's four-support.

There are exactly E=4t incidence edges. Give each such edge an unknown coefficient w_e∈GF5^* (nonzero). Each column must have Σ_{e incident to c_i}w_e=4, and the requested signed collision must have Σ_{i:j in support(i)} ε_i w_{ij}=0 at every coordinate vertex x_j.

**Theorem E0.1 (exact GF5 boundary-flow bijection).** Put z_{ij}=ε_i w_{ij}, orient every graph edge **from its column vertex to its coordinate vertex**, and assign vertex divergence

    b(c_i) = 4*ε_i ∈ GF5,      b(x_j) = 0 ∈ GF5.

Then coefficient assignments satisfying **both** the affine checksum constraints and the requested signed collision are in one-to-one correspondence with **nowhere-zero GF5 edge flows with prescribed vertex divergence b** on this ordinary bipartite G.

**Proof.** The mapping z=ε_i w is invertible because ε_i=±1 is a unit. It preserves zero/nonzero. At column vertex c_i, Σ_j z_{ij}=ε_iΣ_jw_{ij}=4ε_i=b(c_i). At coordinate vertex x_j, using the chosen edge orientation, its divergence is -Σ_{i}z_{ij}=-Σ_i ε_i w_{ij}=0=b(x_j), precisely the signed-vector cancellation constraint. Conversely a nowhere-zero flow z with those divergences determines unique coefficients w_{ij}=ε_i z_{ij}, all nonzero, satisfying every original constraint. QED.

Denote by F_G(b;5) the number of such flows. Each of the t columns independently has **51** admissible checksum4 all-nonzero coefficient assignments, so

    Pr[the prescribed actual GF5 trade | 51-pattern random choices]
        = F_G(b;5) / 51^t,        EXACTLY.

Not a union bound, not asymptotic. D4 remains a separate easy upper bound.

**Theorem E0.2 (published classical flow expansion specialized and independently proved).** Let V be the vertex set of G and E its incidence edges. Then

    F_G(b;5) =
       SUM over Z subseteq E
         (-1)^|Z| * indicator[every component K of G-Z has Σ_{v∈K}b(v)=0]
                    * 5^( |E-Z| - |V| + components(G-Z) ).

**Proof.** Count edge flows with prescribed b that are **nonzero on every edge** by inclusion-exclusion on the bad events z_e=0. For any selected Z of edges forced to zero, the remaining graph G-Z has incidence-matrix rank |V|-components(G-Z), and the prescribed divergence linear system is consistent iff b sums to zero on each connected component. When consistent, the number of unconstrained remaining edge assignments is 5^(|E-Z|-|V|+components(G-Z)); otherwise zero. Multiply by (-1)^|Z| and sum. QED. This is exactly the style of b-compatible expansion already proved by Fu–Ren–Wang 2025; DO NOT claim discovery.

### E0.3: stronger exactly priced all-m weighted alteration

Let B_m consist of any N **distinct** size-four supports; choose all-nonzero GF5 checksum4 weights independently. For every unordered pair of disjoint k-subsets of column IDs, k=2,3, form its signed incidence G(P,Q), boundary b(P,Q) above and define the EXACT risk

    R_k(B_m) = SUM_{unordered P,Q, |P|=|Q|=k, P∩Q=empty}
                 F_{G(P,Q)}(b(P,Q);5) / 51^(2k).

The sum is over **all potential weighted events**, not merely those previously observed with all-one coefficients.

**Corollary E0.3 (all-m):** for each p∈[0,1] there exists an actual GF5 support4, nonzero-checksum4 ASET subfamily of cardinality at least

    p*N - p^4 R_2(B_m) - p^6 R_3(B_m).

**Proof.** Independently select each candidate weighted column, and then independently retain it with probability p. By the affine checksum lemma D1, no collision occurs between subsets of different sizes <=3. Distinct supports prevent singleton collisions. The expected number of retained columns is pN, while the expected number of disjoint balanced k-vs-k collision events is **exactly** p^(2k)R_k by E0.1 and independence of retention; shared-column equalities cancel down to a disjoint smaller event. Therefore some realization has score at least the displayed expectation, and deleting one retained column from each occurring collision produces an ASET subset at least that large. QED.

Since the previous D5 U_k uses **upper bounds** for each event probability, R_k<=U_k always. E0.3 can be strictly stronger than D5, but still has NO new power until R_2(m),R_3(m) are uniformly bounded in an actual infinite family.

## 3. Proof-carrying small finite oracle

[Exact small b-compatible flow enumerator](../../research/hyp105_g5e0_boundary_flows.py) evaluates E0.2 using GF5 components and rational exact arithmetic, with an explicit computational cap E<=16 (t<=4). It is a *proof checker* for bounded instances, NOT an all-s fast algorithm: evaluating every edge deletion is O(2^(4t)) and t=6 would already have 2^24 terms.

[Independent test oracle](../../research/test_hyp105_g5e0_boundary_flows.py) validates:
- two opposite-signed columns on identical four-support have **exactly 51** nonzero collision assignments out of 51²; this agrees with independent brute-force comparison of all 51² coefficient pattern pairs and is below the D4 affine upper;
- two independent identical-support opposite-signed pairs contribute **51²** assignments out of 51^4 (factorization over two graph components);
- different supports with singleton coordinate have **zero** nonzero flow count, even though zero-permitted affine solutions may exist;
- original actual four-column W32 unit 2-vs-2 signed trade yields **positive** nonzero flow count;
- malformed signs and requests exceeding the exact finite compute cap are rejected.

The program is an independent graph-algebraic interpretation of the existing full-vector GF5 collision oracle. All accepted finite witnesses (including the 45-column m12 JSON in G5-D) still require direct complete field sum verification, not flow counting alone.

## 4. The actual original frontier (not a theorem by renaming)

A proof of either of these is a substantive next project:
- an explicit infinite support4 family with N=Omega(m^(8/3)) but **exact flow-risk totals** R_2=O(m^b4), R_3=O(m^b6) satisfying b4<52/15 and b6<4, respectively, would via E0.3 beat the published Lefmann 12/5 power for **actual** ASET; or
- a new stronger all-m hypergraph independence theorem using the overlap geometry of these flow events to bypass the first-moment threshold, with fully justified codegree assumptions; or
- a universal upper bound on unrestricted weighted ASET stronger than the published 8/3 exponent.

Ordinary W(3,2^h) bipartite girth-eight geometry is already known. The exceptional doily s=2 pair-disjointness model cannot directly represent all s; naive lex injection of GQ vertices into coordinate pairs does not control R_k. Fixed field GF5 gives only 51 patterns per support, so one successful 45-column m12 greedy construction does **not** imply uniform all-s success. Our contribution must arise from a **new actual quantitative bound on aggregate prescribed-boundary flows or their correlations**, not from restating Fu–Ren–Wang 2025.

This is the research gate [#162](https://github.com/definitely-stable/Mathlab/issues/162). Parent #106/#95 stay OPEN; no Rust until a valid publishable original mathematical result exists.
