# HYP-105 #230 — D6-AA4-E: global typed injection capacity and coherent dual

**Status: OPEN_WITH_FORMAL_BLOCKER.** All-h **conditional weak duality** and exact finite falsifiers, NOT a universal positive lower bound. Stacked draft from [D6-AA4-D #438](https://github.com/definitely-stable/Mathlab/pull/438), exact parent HEAD \`c81901450c736dd4643b205f2e51d37c8c4330b0\`. Do not touch \`main\`; #230/#176/#169 and Branch A/B remain OPEN.

## 1. Genuine physical capacity is almost saturated, but identities matter

For every \`s=2^h, h>=1\`, ORIGINAL W(3,s) has \`V=(s+1)(s²+1)\` point factors and independently \`V\` line factors. Physical pair alphabet: \`E=E(K_a)\`, \`K=binom(a,2)\`, \`a\` smallest with \`K>=V\`; \`m=K-V\`. Each type uses one globally injective source-to-pair assignment. The same physical pair may be used once on each type. By minimality,

\[
0\le m<a-1=O(\sqrt V)=O(s^{3/2}),\qquad V/K=1-O(V^{-1/2}).
\]

Consequently each type fills asymptotically almost all available physical pairs. This does not rule out an image-only lower bound; it rules out presuming that occupied-pair image density captures the source-to-pair configuration.

**Genuine ORIGINAL W32 falsifier:** the two pinned globally injective schemes S68/S72 use exactly the SAME entire K6 physical pair image separately for left and right, and the SAME original 45-incidence W(3,2) host, yet their accepted ORIGINAL GF(5) seven-class counts differ, \`68 != 72\`; certified necessary numerators differ, \`3,112,510 != 3,283,610\`. Thus no statistic depending **only** on the two occupied physical pair sets can reconstruct the true count S. This is **not** a counterexample to a potential universal positive lower bound.

## 2. Exact all-h dual/minorant bound

Let \`I_s\` be ORIGINAL incidences, and for **each distinct six-incidence set** \`Q⊂I_s\`, let \`T_Q\` be its ORIGINAL typed factor identities. \`c_Q(t_Q)∈{0,1}\` is the exact accepted seven-class GF(5) physical predicate with its ORIGINAL positional ordering, on a tuple \`t_Q\` injective separately within the P and L types. Every ORIGINAL factor is used with the **same** physical pair in ALL Q containing it. Set

\[
S_s(f,g)=\sum_Q c_Q((f,g)|_{T_Q}).
\]

Choose arbitrary rational, signed potentials \`u_{Q,v,e}\` for \`v∈T_Q\`, physical pair \`e∈E\`, and define

\[
\alpha_Q(u)=\min_{\substack{t_Q\\\mathrm{locally\ typed\ injective}}}
\left(c_Q(t_Q)-\sum_{v\in T_Q}u_{Q,v,t_Q(v)}\right),
\quad U_{v,e}=\sum_{Q:v\in T_Q}u_{Q,v,e}.
\]

For ORIGINAL factor type \`T=P\` or \`T=L\`, define independent rectangular min-cost injection

\[
A_T(U)=\min_{\phi:T\hookrightarrow E}\sum_{v\in T}U_{v,\phi(v)}.
\]

**All-h weak-duality theorem (exact and conditional):**

\[
\boxed{\forall h\ge1,\ \forall\text{ globally typed-injective } f,g:
\quad S_{2^h}(f,g)\ge
\mathcal L_{2^h}(u):=\sum_Q\alpha_Q(u)+A_P(U)+A_L(U).}
\]

**Proof:** the definition of each local minimum gives \`c_Q((f,g)|T_Q) >= alpha_Q + sum_{v∈T_Q} u_{Q,v,(f,g)(v)}\`. Sum for the same ORIGINAL sixsets. The potential terms telescope by each shared ORIGINAL source identity, and \`f\`, \`g\` are independently complete typed injections. Replacing each of the two resulting assignment costs with its respective exact minimum proves the bound. No factor independence, no \`Q\`-wise physical label reassignment and no unphysical cross-type all-different constraint are imposed. □

A **sufficient but presently unfulfilled** Branch A gate would be a rigorously constructed, locally verified family \`u^(h)\` and a uniform \`c>0\` with \`L_{2^h}(u^(h)) >= c 2^{6h}\` for ALL \`h>=1\`. Merely defining this Lagrangian bound does not establish the gate; \`u=0\` gives only zero.

The same weak dual can be applied to nonnegative weighted selected GF5 floor costs, with the EXACT class-dependent weights and no pretense to compute the entire GF5 R3.

## 3. Exact constructive successes and an analytic hard NO-GO

The three examples below are **synthetic tiny factor-cost systems**, NOT instances of seven-class ORIGINAL GQ motifs:

* **Capacity helps:** two distinct point factors bijectively take physical labels \`0,1\`; each separately incurs cost \`1[label=0]\`. Independent local minima sum to 0; every complete injection costs 1. Unary signed-potential dual attains 1.
* **Shared ORIGINAL source identity helps:** one point factor occurs in two costs \`1[label=0]\` and \`1[label=1]\`. Isolated minima are 0; every coherent complete assignment costs 1. Unary dual again attains 1.
* **Hard NO-GO for ALL unary prices:** three same-type factors \`x,y,z\` must bijectively take labels \`0,1,2\`. Three pair motifs are zero-cost respectively iff \`y=x+1 mod 3\`, \`z=y+1 mod 3\`, \`z=x+1 mod 3\`. Every global permutation violates at least one pair constraint; exact optimum is 1. However for EACH pair constraint the uniform measure on the three successor pairs \`(0,1),(1,2),(2,0)\` has zero cost, and its single-factor marginals are all uniform. These are exactly the marginals of the uniform measure on all six genuine global permutations. For **every possible choice of signed unary prices**, take the expectation of all the local minorant inequalities under the three locally feasible zero-cost measures; then replace the sum of their singleton price expectations by its global minimum-cost assignment, which is no larger than the uniform globally injective expectation. It follows that \`L(u)<=0\` for ALL \`u\`. Choosing all prices zero achieves \`L(0)=0\`, so \`sup_u L(u)=0 < min_global_cost=1\`. This is an **analytic integrality gap** of the unary global assignment dual, not Branch B of HYP-105.

This NO-GO proves that adding more unary price tuning cannot generally overcome shared pair/triple-factor incompatibility. It does NOT show that unary bounds must fail specifically on genuine GQ seven-GF5 motifs.

## 4. Implementation and acceptance criteria

\`research/hyp105_issue230_d6aa4e_global_assignment_dual.py\` provides minimal physical capacity, locally exhaustive small typed motif tables, exact signed rational Hungarian min-cost injection per type, universal local-minorant checking for tiny models, independent complete tiny typed global injection enumeration, and an actual W32 classifier comparison. \`research/test_hyp105_issue230_d6aa4e_global_assignment_dual.py\` tests the Hungarian solver independently against exhaustive permutations, exact arbitrary signed price bounds against globally complete assignments, legal same-edge reuse across types, analytic pair-cycle gap, invalid local tables, and actual S68/S72 seven-class count divergence.

**Computational boundary:** local \`K^{|T_Q|}\` tables are intentionally capped for small falsification, not a scalable W(3,s) GF5 solver. All-h mathematical weak duality is symbolic; no globally positive bound was computed from W32. Do not promote exact finite observations to all-h Branch A or infinite Branch B. Hosted acceptance requires dedicated exact test and report, INDEX, Proof Audit and Research on one final PR HEAD, plus independent mathematical review.

## 5. Decision

**OPEN_WITH_FORMAL_BLOCKER:** global physical capacity plus unary source coherence admits a provable gap on a small exact instance; no constructed all-h positive \`L\` certificate exists. The next slice D6-AA4-F should test **pair/triple ORIGINAL factor separators or cycle-consistent marginal constraints** on the analytic three-factor falsifier, prior D6-X/Y pseudodistributions, and the original W32 seven-class oracle. Only then attempt a source- and starting-map-independent asymptotic \`c 2^{6h}\` result. Root #230, #176, #169 remain OPEN; no full GF5 R3, ASET exponent or merge claim.
