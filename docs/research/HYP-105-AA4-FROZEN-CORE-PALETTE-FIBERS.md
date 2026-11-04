# HYP-105 #230 AA4-FROZEN — exact fixed-core GF5 palette obstruction

Scientific Draft stacked ONLY on frozen #721 SHA 25178580d7c820bdfc0c909c4f72df70ad38d2c2. Original true W(3,4), source ID provenance, global pair-injective f,g and all 51 legal nonzero checksum4 GF5 palettes are unchanged. Root #230 OPEN_WITH_FORMAL_BLOCKER.

## New all-N necessary theorem

Fix N original full GF(5)^m source columns and a proposed edit-support T. Let F be the complementary set of FROZEN original IDs. For each edited source i in T, and k=2,3, define H^F_{i,k}(p) as the number of pairs A,B of subsets of F with |A|=k-1, |B|=k, A disjoint B and the COMPLETE physical equality

  c_i(p) + sum_{a in A} c_a = sum_{b in B} c_b.

Each such equality is a true 2k-DISTINCT-ORIGINAL-ID signed event containing i and no other edited original IDs. The orientation placing i on the positive side is unique. Define D_i(F) as all legal source coefficient palettes with H^F_{i,2}(p)=H^F_{i,3}(p)=0.

**Theorem A:** Any final collision-free 0-to-3 source assignment changing only original IDs from T MUST use a palette in D_i(F) for EVERY i in T. An empty domain for one i is an unconditional obstruction for THIS T, irrespective of edit order, simultaneous coefficient changes, intermediate conflicts or monotonicity. Proof: every witness uses exclusively frozen original vectors besides i, so its physical signed equality persists under all changes outside i. QED.

**Theorem B:** If the frozen F source columns have no equal 2-subset or equal 3-subset sums and all chosen edited palettes lie in their D_i(F), then NO final equal-size signed event with at most one ID in T is possible. The remaining event sectors have at least two edited IDs. This does not prove overall ASET feasibility. Proof: zero edited IDs are internal frozen conflicts; exactly one edited ID would have to satisfy an H^F equation. QED.

Neither theorem assumes independent f,g labels, independent palettes or random six-event witnesses. Both are exact for every finite N.

## Genuine W34 application and complete physical census

PR #721 independently certified two MINIMUM ABSTRACT source-ID covers of the actual original W34 initial 2v2/3v3 hypergraphs, lex 25 and reverse-line 26. The previous genuine finite GF5 0-to-3 constructions from PR #719 use 27 and 29 original coefficient edits, respectively. Minimum abstract covers need NOT admit legal 51-pattern coefficient assignments.

For each selected actual T, the C++ oracle reconstructs exact outside-support 24D and inside-support four-GF5-digit projections, indexes every pair of F sources and enumerates EVERY F triple, checking disjoint original IDs. Equality of full outside projections and the four inner residual digits uniquely identify a legal 51-palette. The same method checks fixed-singleton/fixed-pair equalities for true R2. There is no random hash, sampled triple or invented source incidence flag.

For lex |F|=400; for reverse-line |F|=399. Each target requires all C(|F|,2) fixed-source pairs and C(|F|,3) triples. The exact output contains 51 membership decisions, H2/H3 multiplicities and a direct physical 28D signed original-ID witness for EACH blocked pattern. A completely independent Python checker rebuilds actual original symplectic W34 f,g, 425 original vectors, verifies true support, original ID distinctness, and every witness coordinate equation. All original target IDs from T must be covered by four exhaustive CI shards per map; every shard must report full pair/triple counts. Reports are saved as GitHub-hosted artifacts, not mistaken for all-h proofs.

An independent W(3,2) finite original-source unit test directly brute-force evaluates all full 12D physical disjoint 2v2 and 3v3 equations with a frozen 11-source core, for all 51 patterns and all edited IDs, and checks against the C++ residual oracle.

## Scope and next mathematical gate

If ANY D_i(F) is empty, this proves NO legal final source assignment supported on THAT particular T, but says nothing about alternative minimum covers. If ALL D_i(F) are nonempty, it proves only one-variable necessary feasibility. Interactions involving two or more editable source IDs require a separate sound source CSP and independent full 12,704,100-triple final GF5 audit of any resulting candidate. Neither the old nor current finite W34 results establish root HYP-105 Branch A/B/C, all-h safe recoloring existence, or an improved ASET exponent.

Keep status OPEN_WITH_FORMAL_BLOCKER.
