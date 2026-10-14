# HYP-105 / issue #230 — EICE-003-I: exact four-quadrant TRUE ORIGINAL source matching capacity

**Acceptance:** \`RESTRICTED_THEOREM_I / OPEN_WITH_FORMAL_BLOCKER\`. Strict child of fully green [EICE-003-H PR #464](https://github.com/definitely-stable/Mathlab/pull/464), pinned parent \`65f1acb45999bee44b73bfa69b479b3457eea088\`. Draft only, main untouched. No universal o(s⁴) capacity, no GF5 seven-sixset transfer, no Branch A/B and no ASET claim.

## I1 — a necessary AND sufficient exact local 5-ORIGINAL-incidence physical template

Fix globally injective f,g on true W(3,s), and one true middle original incidence e=(p₂,ℓ₂), with f(p₂)={x₀,x₁} and g(ℓ₂)={y₀,y₁}. Retain BOTH physical diagonals of every original incidence source. By H2-MATCH, every arm source a=(p,ℓ) in any five-source paired-coherent 2×2 NB3 plaquette must satisfy p≠p₂ and ℓ≠ℓ₂. In addition, its point label f(p) shares exactly ONE coordinate x_i with f(p₂), and its line label g(ℓ) shares exactly ONE y_j with g(ℓ₂). So every genuine arm source of the true double-star fibre has an EXACTLY UNIQUE quadrant

    Q_{ij}(e) = {a=(p,ℓ) in F_e :
       p≠p₂, ℓ≠ℓ₂,
       f(p)∩f(p₂)={x_i}, g(ℓ)∩g(ℓ₂)={y_j}},   i,j∈{0,1}.

Write its external partner coordinates as ξ(a)=the other f(p) coordinate and υ(a)=the other g(ℓ) coordinate. Both exclude the middle x₀,x₁ and y₀,y₁; if not, a would equal the middle original point or line by global injectivity. The four quadrant source ID sets are disjoint and partition the H2-MATCH filtered external arm pool \`F_e^arm\`.

**Exact local equivalence:** A fixed unordered set of FIVE distinct TRUE original incidences containing e realizes a paired-coherent coordinate-proper physical 2×2 NB3 square with e as the middle source **if and only if** its other four incidences consist of two members of Q_{00} and two of Q_{11}, OR two of Q_{01} and two of Q_{10}, and their four ξ coordinates are pairwise distinct while their four υ coordinates are pairwise distinct.

*Necessity:* a middle physical diagonal connects opposite quadrants. The two external neighbors at each physical endpoint must use two different original source incidences; coherent physical neighbor uniqueness forces distinct outside left/right coordinates at each end, and each of the four 3-paths must also have distinct outside left/right coordinates across opposite ends.

*Sufficiency:* choose the unique middle physical diagonal connecting the two occupied opposite quadrants. Each of the four selected genuine incidence sources contributes one physical diagonal edge incident to its unique corner, hence two genuine outer physical neighbors at both endpoints and all four 3-paths. The partner-coordinate disjointness makes every path coordinate-proper. The original point and line factors of the FIVE sources are pairwise distinct: inside one quadrant, equal source point/line would yield equal ξ/υ, while across opposite quadrants equality would imply f(p)={x₀,x₁}=f(p₂) or its dual. The left-coordinate graph of the five ORIGINAL point physical pairs is a tree consisting of the central x₀x₁ pair plus four distinct pendant ξ's; the right-coordinate graph is its y dual, so both admit global bipartitions and EVERY retained physical edge crosses both cuts. Since no two ORIGINAL sources share a point or line, no physical vertex can have two neighbors with equal partner-left/partner-right coordinates, so no cherries arise anywhere, including at the unused paired diagonals. Thus the complete five-source graph retaining both diagonals is coherent. Every claimed term is a true original incidence ID; no artificial independent coupling is introduced.

This is a physical **template theorem**, not a statement that any of its four original endpoint pairs is nonincident/end-clean/blocked or that an accepted positive original GF5 sixset exists.

## I2 — exact true quadrant pair-capacity formula and intermediate upper bound

For each quadrant Q, regard its true source incidences as edges in a bipartite graph between their external physical partner coordinates ξ and υ. Define \`T(Q)\` as the number of two-arm choices having distinct ξ and distinct υ. Since every true original source is a distinct (point,line) incidence, each (ξ,υ) entry is unique for fixed Q. Thus exact finite-integer counting gives

    T(Q) = binom(|Q|,2)
           - sum_ξ binom(deg_Q(ξ),2)
           - sum_υ binom(deg_Q(υ),2).                (I2-PAIR)

There is no double subtraction: two distinct source incidences sharing both ξ and υ would have identical point label f(p) and identical line label g(ℓ), hence be the same original incidence ID. Let \`A_e\` denote the number of TRUE original five-source physical 2×2 templates with middle e, without imposing any endpoint/GQ anchor/blocking statuses.

The naive opposite-quadrant two-arm capacity is

    U_e = T(Q00)T(Q11) + T(Q01)T(Q10).              (I2-UPPER)

To make this exact, consider each two-arm choice in opposite quadrant pair. Retain it ONLY when their two ξ-sets are disjoint and their two υ-sets disjoint. The count of these successful pairs is EXACTLY A_e, by I1:

    A_e = sum_{(Q,Q')=(Q00,Q11),(Q01,Q10)}
          sum_{a∈Match2(Q),b∈Match2(Q')}
            1[Ξ(a)∩Ξ(b)=empty AND Υ(a)∩Υ(b)=empty]
        <= U_e.                                     (I2-EXACT)

Both sums are independent of the ORIGINAL GQ anchor and GF5 positivity; they count all physical source-coherent 2×2 five-source TEMPLATES. The genuine all-four-end-clean internally blocked five-source set count H_e necessarily obeys \`H_e<=A_e\`. The exact oracle enumerates quadrants directly from true GQ incidence IDs and physical labels, compares H_e from the independently enumerated FULL original physical G2 source census, then reconstructs actual five-incidence graphs with both diagonals and verifies a physical coordinate-proper 2×2 square. Every budget is fail closed.

The I2 upper is NOT a universal o(s⁴) estimate. Each F_e still may contain O(s²) arm incidences, allowing pair-product upper of order O(s⁸). A finite large gap between A_e and H_e does not justify extrapolating it to all h.

## I3 — sharper all-h theorem: EXACTLY TWO orientations, UNIQUE original middle source

Fix a set F of exactly five TRUE original incidence IDs which satisfies the I1 template criterion for some central original e. The full physical graph H(F) retaining BOTH diagonals of EVERY source has exactly TEN undirected physical edges, and in fact decomposes into:

- exactly ONE connected five-edge **double-star TREE**: its two central physical vertices u,v have physical degrees THREE; they are joined by the unique middle physical edge from e, and have two distinct degree-one outer physical neighbors apiece;
- FIVE further isolated undirected physical edges: the other physical diagonal of e, plus the complementary physical diagonal of each of the four outer source incidences.

**All 16 nonisolated physical vertices are distinct.** The five main edges form a tree on six physical vertices. Complementary diagonal endpoints have one central left or right coordinate and one external opposite coordinate; they cannot be any main outside corner (which has BOTH coordinates external), nor either main center (both coordinates central), nor the other physical diagonal of e (both coordinates central but cross-paired). The four external left coordinates and four external right coordinates are pairwise distinct by I1, so all eight complementary outer-diagonal endpoints are distinct from each other and from the other middle diagonal's two endpoints.

Hence exactly TWO physical vertices have degree>=2, namely u and v, and they have degree three. Their connecting edge is the **only physical edge capable of being the middle of ANY 2×2 NB3 plaquette** supported on these exact five original source IDs. Its TRUE original incidence ID is e, uniquely determined by F. Reversing u→v yields the only other oriented representation. Thus:

    multiplicity_oriented(F; all possible true original middle IDs) = EXACTLY 2.   (I3)

The prior G4 all-h bound 20, and the preliminary I3 bound 10, were valid but unnecessarily weak. The empirical two-to-one incidence from W34 lex/random is now an independently proved all-h theorem FOR I1-valid five-source templates. This statement does not claim every arbitrary five-original-incidence set admits a source template, and does not yield a positive original GF(5) sixset.

The code reconstructs the complete ten-edge, five-source graph and checks precisely two degree-three vertices, fourteen degree-one vertices, one genuine central middle source and exactly five disconnected paired diagonals, besides the true physical four-path square. These are executable falsifiers of the all-h proof, not substitutes for it.

## I4 — sharpened all-h \u03a9(s\u2078) and heavy-middle implications

Prior F5+F6 (on a FIXED same-map high-degree stationary paired G* with \`delta=10^-6\`, s=2^h>=2^22) gave the number of oriented all-four-blocked true-original physical squares

    P4 >= [delta^4*s^8/1,280,000]*
          q,  q=max(0,4theta_I-3,theta_I^4-2/(delta*s-1)).

Use I3's NEW all-h exact TWO rather than older <=20 (or preliminary <=10) to obtain

    # DISTINCT true original blocked five-incidence sets
      >= [delta^4*s^8/2,560,000]*q.               (I4-GLOBAL)

With the same unique middle source and exactly TWO orientations, pigeonhole over N=(s+1)^2(s²+1) middle TRUE original incidence IDs gives

    max_e H_e >= [delta^4*s^8/(2,560,000*N)]*q.    (I4-HEAVY)

For any fixed \`theta_I>=epsilon>0\`, I4-HEAVY implies a genuine middle original incidence supports Omega_epsilon(s⁴) distinct physical-source-compatible blocked original five-incidence sets. Both global source diversity and heavy-middle constants improve TENFOLD over the original G4/H3 bound 20, without claiming the missing uniform upper on the realized blocked-source load.

A sufficient missing theorem would still be

    max_e H_e=o(s^4) for ALL true global injections and
                        valid EICE-002 same-map G*.        (OPEN)

Nothing proved here supplies this upper. I1/I2 are exact *physical-possibility parametrizations* that finally isolate where the missing restriction must come from: simultaneous original GQ endpoint/anchor end-cleanness and internal blocking across four source-coherent paths, NOT merely source star spectral size or paired physical cuts.

## I5 — finite original-source evidence and implementation limits

Frozen true ORIGINAL globally injective maps W32 lex/reverse/S68/S72 and W34 lex/random are used to audit every middle source, all four quadrants, partner coordinates and exact pair-product/coordinate-cross disjointness. Every observed G2 allblocked five-source family and every actually realized middle original source ID must belong to I1's exact template candidate set. Additional independent reconstruction verifies sample new I1 candidates on the TRUE original five-incidence paired-diagonal subgraph with the existing EICE-003-E original endpoint/anchor oracle.

No GF5 classification on W34: the frozen seven-class sixset verifier is W32/K6-specific. All local results are source templates and exact finite counting; no fictitious GF5 witness and no promotion of any finite observed o(s⁴) ratio to a universal theorem.

Research-only files:
- \`research/hyp105_issue230_quadrant_matching_capacity.py\`
- \`research/test_hyp105_issue230_quadrant_matching_capacity.py\`
- \`docs/research/HYP-105-ISSUE230-EICE003I-QUADRANT-MATCHING.md\`
- \`.github/workflows/hyp105-issue230-eice003i.yml\`

**Next EICE-003-J:** use the I1 exact true-source candidate parametrization to compute conditional ORIGINAL GQ anchor-blocking obstruction **inside** each source partner-coordinate rectangle. Seek a true all-h upper \`H_e=o(s^4)\`, or find a dense structured counterfamily disproving this auxiliary bound; alternatively develop the full all-h seven-class positive-sixset oracle and a validated many-to-one transfer. No merges/main changes or root issue close.
