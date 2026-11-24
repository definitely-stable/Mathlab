# GIO-003 / G6-F1 — Self-contained NUMERIC ordinary-graph C6 supersaturation

**Scope:** [#793](https://github.com/definitely-stable/Mathlab/issues/793), #790. The frozen parent is [G6-E4 Draft #816](https://github.com/definitely-stable/Mathlab/pull/816), HEAD 15dc474680686483d76bf950fcafcb7402effd53, with its specialist 22/22, INDEX and full Research verified green. This is a separate stacked Draft. Main and other PRs are not changed.

**Scientific contribution:** Replace the previous numerical **FORMAL_ONLY** ordinary-graph constants \`C0=c0=1\` with a **complete elementary quantitative proof** supplying deliberately conservative **VALID** rational/integer constants for every simple host graph. The existence of C6 supersaturation, as well as spectral walks and almost-regular reductions, is classical PRIOR ART; see Simonovits and Jiang–Yepremyan, [*Supersaturation of even linear cycles in linear hypergraphs*, CPC 29 (2020) 698–721](https://doi.org/10.1017/S0963548320000206), especially Theorem 1.1 (ordinary graphs are r=2) and their Sections 3 and 5. Their published proof *does not provide a specific convenient numeric pair* for the application. This F1 proof provides one and checks **every** dependency numerically rather than pretending 1,1 were published valid. This is an explicit quantitative witness for Mathlab, not a claim to have discovered the existence theorem.

## 1. Main unconditional GRAPH theorem (no source geometry, no regularity)

Let G be an arbitrary finite undirected **simple graph**, with n=v(G)≥1 vertices, m=e(G) edges, and denote by #C6(G) the number of **unoriented simple 6-cycles on SIX DISTINCT vertices**. Define

~~~
p=2^20=1,048,576
C_bip=p²=2^40
C_graph=2*p²=2^41=2,199,023,255,552
c_bip=1/1536
c_graph=c_bip/2^6=1/98,304.
~~~

**Theorem F1-C6 (all simple graphs, exact constants):**

~~~
    m>=C_graph*n^(4/3)
       ==> #C6(G) >= c_graph*(m/n)^6.
~~~

No maximum degree, minimum degree, almost regularity, bipartiteness, GQ, source projections or asymptotic unnamed threshold is assumed. The density comparison is EXACTLY checked without floating point via \`m³ >= C_graph³*n⁴\`. If the finite graph cannot satisfy the condition, no positive count is asserted.

The numerical threshold is deliberately HUGE, so it does not apply to typical experimental small graphs. Its role is a **fully proved positive all-order constant** that can replace the fake 1,1 entries in a mathematical existence proof. It gives a very large but finite derived r0 and very small rho,delta. It is not optimized.

## 2. Elementary exact noninjective six-walk lemma (bipartite)

Let G be any genuine simple **bipartite** graph on n vertices, with adjacency matrix A, maximum degree D, average degree d=2m/n. Let

~~~
 S4=tr(A^4), S6=tr(A^6).
~~~

Each ordered simple (injective) closed 6-walk corresponds to exactly one unoriented simple C6 and has **12** starting/direction choices. Any NONINJECTIVE ordered closed sixwalk must repeat two of the six positions. A repetition at cyclic distance 1 or 5 contradicts no loops; at distance 3 contradicts bipartiteness (odd walk from a vertex to itself). Therefore at least one of SIX distance-2 repetitions occurs. Requiring v_i=v_(i+2) creates exactly a two-edge backtrack at v_i, followed by a rooted closed fourwalk, hence at most

~~~
  sum_v degree(v)*(A^4)[v,v] <=D*S4
~~~

walks for that repetition. Union bounding over all six positions yields the **exact unconditional combinatorial bound**

~~~
  0 <=S6-12*#C6(G)<=6*D*S4.                 (F1-WALK)
~~~

Independently, spectral Rayleigh and elementary power-mean/Hölder inequalities imply

~~~
  S6 >= d^6,   S6 >= S4^(3/2)/sqrt(n).     (F1-SPECTRAL)
~~~

These are **not** numerical approximations. Every finite trace oracle in the tests calculates A², A³ over integer adjacency and independently brute-enumerates six distinct vertex paths then divides by 12; disconnected and asymmetric bipartite examples and odd-cycle fail-closed controls are included.

## 3. Explicit almost-regular bipartite C6 lemma

Suppose \`D<=L*d\` for a fixed number L>=1 and

~~~
  d^3>=1728*L^3*n, i.e. d>=12L*n^(1/3).
~~~

**Then**

~~~
  #C6(G)>=d^6/24=(8/3)*(m/n)^6.          (F1-REG)
~~~

**Proof:** Put X=S4. If \`X>=144D²n\`, the second (F1-SPECTRAL) inequality yields \`S6>=12D*X\`, so by (F1-WALK), \`12 #C6>=S6/2\`. Otherwise \`6DX<864D³n<=864L³d³n<=d^6/2<=S6/2\`, again \`12 #C6>=S6/2\`. In both cases \`S6>=d^6\`, proving F1-REG.

This is a **fully explicit** result in the important degree-bounded subcase. Example: the true complete bipartite graph K_(h,h) has d=D=h and the lemma applies for **h>=59**, but not necessarily h=58. Its EXACT cycle count is \`6*binom(h,3)^2\`; the 59 boundary and the count are verified using integer arithmetic. This lemma ALONE cannot be applied to an arbitrary HEAVY host of G6-C3 because that host has no proven maximum/average-degree ratio. The following step genuinely removes that restriction rather than concealing it.

## 4. All-graph inductive regularization with EXPLICIT constants

We prove a standalone lemma for any **bipartite** graph H with \`m(H)>=p²*n(H)^(4/3)\`. Such a graph has necessarily at least \`n>=p²\` vertices, because \`m<=n²/2\` implies \`n^(2/3)>=2p²\`.

Write \`Phi(H)=(m(H)/n(H))^6\`. By **strong induction on n**, construct a finite collection \`H_1,...,H_t\` of **edge-disjoint original subgraphs** of H with:

~~~
 (i)  e(H_i)>=(p²/4)*v(H_i)^(4/3),
 (ii) Delta(H_i)<=8p*d(H_i),
 (iii) sum_i Phi(H_i)>=4^(-6)*Phi(H).
~~~

Each H_i remains bipartite and has strictly fewer or no more than n vertices; in the base case of induction the construction terminates immediately. Only actual input edges are retained; no synthetic graph or completion is introduced.

**Case 1 — at most m/2 edges touch the p⁻¹ highest-degree vertices.**

Partition V(H) into p almost-equal groups, with A1 containing the highest-degree \`ceil(n/p)\` vertices. Remove A1. At least m/2 edges remain, and every remaining vertex has degree at most p*d_original (since |A1|>=n/p and total degree=nd_original). Iteratively remove vertices currently of degree below d_original/8. At most n*d_original/8=m/4 edges are lost in this pruning. The final nonempty H' has:

~~~
 e(H')>=m/4,  delta(H')>=d_original/8,
 Delta(H')<=p*d_original<=8p*d(H'),
 Phi(H')>=4^(-6)*Phi(H).
~~~

Its density is at least p²/4 times \`v(H')^(4/3)\`. It is one output leaf. This handles arbitrarily skewed degree distributions locally, without assuming the original H had a bounded maximum degree.

**Case 2 — more than m/2 edges touch A1.**

For i=2,...,p form an edge-disjoint H_i' on A1∪Ai containing ALL cross A1–Ai edges. Place every internal A1 edge **exactly once**, in H_2'. Then \`sum_i e(H_i')>m/2\`, no overlap between edge sets, and because n>=p² and groups are almost equal,

~~~
  n_i=v(H_i') <=2ceil(n/p)<=9n/(4p)<n.
~~~

Retain the indices with \`e(H_i')>=p²*n_i^(4/3)\`. Total density-failing edge mass is at most

~~~
 sum_bad e_i
  < p*p²*(9n/(4p))^(4/3)
  =p²*n^(4/3)*(9/4)^(4/3)/p^(1/3)
  <=m/4
~~~

because **\`4p>=9^4\`** (cubing the desired inequality). Therefore sum_good e_i>m/4. Let k<=p be the count of good H_i'. Convexity of \`x^6\`, the common bound \`n_i<=9n/(4p)\`, and the count k<=p imply

~~~
 sum_good Phi(H_i')
 >=(4p/(9n))^6*(sum_good e_i)^6/p^5
 >=(p/9^6)*Phi(H)
 >=Phi(H), since p=2^20>=9^6=531441.
~~~

Apply the strong induction hypothesis to EACH good H_i'. Their edge sets (and all resulting leaves) remain pairwise disjoint, and the extra induction factor 4^-6 yields the promised \`sum Phi(H_j)>=4^-6 Phi(H)\`. The induction **does not** count the same internal A1 edge across multiple H_i'.

Every leaf now has \`d_i>=2*(p²/4)*n_i^(1/3)=(p²/2)*n_i^(1/3)\`. With L=8p, the F1-REG hypothesis \`d_i>=12L*n_i^(1/3)\` is automatic because **\`p²>=192p\`**. Consequently

~~~
 sum_j #C6(H_j)
  >=(8/3)*sum_j Phi(H_j)
  >=(8/3)/4^6 *Phi(H)
  =(1/1536)*Phi(H).
~~~

Because leaf edge sets are DISJOINT, a simple C6 from one leaf cannot be the exact same six-edge C6 in another; all belong to the original H. This proves the explicit bipartite theorem, **for arbitrary degree distributions**, not only for nearly regular hosts.

## 5. Remove bipartiteness — all simple graph theorem

For arbitrary simple G choose a bipartition using a global random fair cut of its vertices. Every true edge crosses with probability 1/2. Therefore at least one deterministic cut has a **spanning bipartite subgraph H with m(H)>=m(G)/2**. If \`m(G)>=2p²*n^(4/3)\`, then \`m(H)>=p²*n^(4/3)\`, and the bipartite theorem gives

~~~
 #C6(G)>=#C6(H)
        >=(1/1536)*(m(H)/n)^6
        >=(1/(1536*64))*(m(G)/n)^6
        =(1/98304)*(m(G)/n)^6.
~~~

**No external unknown numeric C6 theorem constants are left.** The exact n,m input domain, all m³/C³/n⁴ comparisons and every proof-constant inequality are machine-checkable integers or rationals.

## 6. Wire into ACTUAL G6-C3/G6-D7 closure without misrepresenting proof status

Use once-and-for-all fixed

~~~
 external ordinary graph C0 = 2^41,
 external ordinary graph c0 = 1/98304.
~~~

These values meet precisely the ordinary graph theorem needed in G6-C3 HEAVY, for ANY simple physical F with e(F)>=C0*v(F)^(4/3), and are chosen **before** sources, labels, cut/priority selection, deletions and r. Inherited code \`closure_ledger\` (G6-C3) and \`integrated_local_ledger\` (G6-D7) accepts exact Fractions and recomputes all HEAVY/LOW constants R,T,rho,delta,r0. We check five concrete old proof regimes, all with the **SAME proven pair (C0,c0)**:

| Old mathematical source regime | Other fixed old gates |
|---|---|
| G6-C3 linear Moore excess | b=1, C=0 (GQ specialization) |
| G6-D7 E1 true published PDS source | b=1, C_excess=2, ell=2, M=0 |
| G6-D7 corrected odd q=7 source | b=1, C_excess=5, ell=4, M=0 |
| G6-D7 corrected odd/even q>=8 | b=1, C_excess=5, ell=3, M=0 |
| G6-D7 corrected odd/even q>=18 | b=1, C_excess=5, ell=2, M=0 |

The **legacy ledger objects deliberately preserve their \`FORMAL_ONLY\` field**, because the old generic functions also accept \`C0=c0=1\` WITHOUT independent certification. The NEW G6-F1 wrapper explicitly attaches \`graph_external_numeric_constants_CERTIFIED_from_explicit_proof=true\` to instances computed using *only* this new proven C0,c0. It checks positive exact rational rho,delta and all four LOW budget assertions inside inherited code.

**Important distinction:** this removes **ONE formerly unresolved numeric dependency**, namely the ordinary graph C6 existential constant pair. It does NOT independently reprove the G6-C2 original six-ID FULL/CORE and G6-C3 shared-priority HEAVY/LOW source-motif chain in this PR. Those prior mathematical dependencies are already implemented and tested, but remain explicitly IMPORTED and have not been Lean-certified or externally academically refereed. The FULL unrestricted abstract T3 (without source restrictions) and dependent GF5/ASET exponent are still **NOT established**. Because C0 is extremely large, the resulting all-order source threshold r0 is huge, and none of the finite q7/q8 fixtures is claimed to satisfy that asymptotic cutoff.

## 7. Independent tests, CI and follow-up

- \`research/gio_t3f1_explicit_c6.py\`: numerical self-contained proof with exact gate, independent brute six-vertex cycle enumerator, graph adjacency A²/A³ trace oracle, almost-regular K_(h,h) symbolic checks, dense source arithmetical feasibility, five actual old-lemma ledgers with proven numeric graph inputs.
- \`research/test_gio_t3f1_explicit_c6.py\`: 18 exact independent tests on genuine small bipartite graphs, stars, cycles, complete bipartite, disconnected graphs, odd-cycle and malformed adjacency fail-closed cases, sharp almostregular h=58/59 threshold, all regularization inequalities, exact proof metadata and real numeric inherited G6-C3/G6-D7 ledgers.
- \`.github/workflows/gio003-g6f1-explicit-ordinary-c6.yml\`: GitHub-hosted Ubuntu 24.04, Python 3.12, literal independent tests and JSON artifact checked against \`C0=2^41,c0=1/98304\`.

**Acceptance:** exact-head specialist + INDEX + full Research SUCCESS; independent critical scoped review of all mathematical inequalities, especially case2 edge-disjointness, noninjective walk count and explicit threshold. Keep PR Draft, #793 OPEN; no main or ancestor merge.

**Next highest-value step:** independently re-audit the inherited G6-C2/C3 original source projection inverse and shared-selector quantifiers *using these certified C6 constants*, ideally formalize the exact finite algebra and source combinatorial proof. Do not mistake this componentwise certification for full unrestricted T3 or external peer review.
