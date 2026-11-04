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


## Verified finite source result on the two selected true W34 minimum covers

The first complete GitHub-hosted true-original GF5 frozen-core specialist matrix #41867605339 reconstructed all eight source-shard outputs, with independent source-physical 28D witness checks and direct W32 brute-force falsifiers.

| Actual original fixed f/g map | Minimum ABSTRACT edit cover | Fixed original source core F | Single-source patterns tested | Patterns surviving all F-only original 2v2/3v3 constraints | Minimum surviving source domain | Maximum |
|---|---:|---:|---:|---:|---:|---:|
| lex | 25 | 400 | 1,275 | 463 | 6 | 32 |
| reverse-line | 26 | 399 | 1,326 | 479 | 11 | 28 |

Every one of the 25/26 source IDs retains at least one legal coefficient pattern against the 400/399 frozen original columns. No simple one-variable fixed-core obstruction was found for EITHER of these PARTICULAR minimum covers. The most restricted actual lex source is ORIGINAL ID25 with 6 of 51 physical patterns allowed (45 blocked). For reverse-line ORIGINAL ID343 retains 11 of 51 (40 blocked).

The Cartesian products of these INDEPENDENT NECESSARY domains have exact sizes 10752697353827425399603200000000 for lex and 350470701699920323408827305164800 for reverse-line. These are only *upper bounds on the potential candidate search space* after frozen-core filtering; they are NOT numbers of genuine valid joint assignments, and provide neither a success probability nor an ASET existence result.

Permanent inspectable finite source domain summary and all original target-ID counts: research/hyp105_w34_frozen_core_domain_certificates.json. It pins exact originating frozen source input SHA256 values, current research parent, true source ID lists, eight GitHub job references and precise count per original flag. The FULL per-pattern exact counts plus distinct original physical signed-event witnesses are published as specialist GitHub Actions artifacts and checked by the independent W34 physical verifier in the specialist workflow. The FINAL HEAD aggregation must match the permanent summary, and the standalone permanent source tests require exact 51-pattern totals and correct original symplectic W34 f,g source arrays.

**Critical next mathematical gate:** model constraints with at least TWO edited original IDs. The complete fixed-core one-source necessary gate does NOT imply a 25-edit or 26-edit full GF5 assignment; it eliminates only the zero/one-variable collision sectors. A genuine CSP over full signed 2v2/3v3 equations involving 2+ chosen sources, with independent final 12,704,100 triple-sum physical verification, is required before claiming existence or impossibility for even the selected fixed minimal covers. Alternative minimum covers are not ruled out.
