# HYP-105 / issue #230 — AA4-AK: exact all-h TRUE ORIGINAL full B/A and A/B Hall transfer

**Research-only.** Strict child of [AA4-AJ PR #521](https://github.com/definitely-stable/Mathlab/pull/521), pinned parent exact SHA \`195f80eb7d8770d6f0ddce0d59087f13c9f9e0e4\`. Applies to the ACTUAL symplectic original W(3,s), s=2^h, h>=1; full complete globally injective actual physical point f and line g maps, possibly with non-surjective minimal physical K_a palettes; all six true selected original incidence IDs must be DISTINCT. No redraw per original sixset, no independent label assumption. **NOT a proof of universal S_s=Ω(s^6), not an infinite counterfamily, not an ASET exponent result, not mathematical accepted until independent review.**

## 1. The last unhandled A-sector source Hall gate

AA4-AH proved an exact six-channel TRUE original source Hall transfer for **disjoint pinned edges / two separate physical triangles**; AA4-AJ extended this to **disjoint pinned edges / physically connected C6** via two crossed two-spoke templates and four internal-auxiliary-link templates. The missing physical A configurations have **adjacent opposite pinned physical edges**, including both:

- **same-component two-triangle sector**: pins (u,v) and (v,w) with common physical vertex v; the first triangle is forced on {u,v,w}, requiring closure physical edge (u,w). Another independent three-vertex triangle uses x<y<z outside {u,v,w};
- **physically connected C6 sector**: pins form the fixed 3-vertex path u-v-w. A connected physical six-vertex two-regular graph containing this exact path is UNIQUELY a complementary 4-edge path w-x-y-z-u, with three distinct auxiliary vertices x,y,z outside {u,v,w}.

The entire simple physical 6-vertex 2-factor space with pinned opposite images is thus EXACTLY:

| Physical pinned edge geometry | physical-A two-triangle | physical-A connected C6 |
|---|---|---|
| disjoint uv,wx | split triangles (AA4-AH) | two crossed two-spoke + four internal linked (AA4-AJ) |
| adjacent uv,vw | same triangle containing BOTH pins (this AA4-AK) | unique complementary three-auxiliary path (this AA4-AK) |

There are no further sectors; classification uses physical six distinct coordinates each of degree two. Earlier original AA4-AD Hall theorem independently says accepted Q equals sum of the TRUE ORIGINAL 4×4 source incidence permanent over occupied full physical A H; original GQ girth eight yields permanent 0,1,2 (2 iff actual induced original source C8).

## 2. NEW exact all-h source-Hall formula for adjacent-pinned TWO triangles

Fix one real original doubled source p, two distinct real original root flags through p, and four distinct real original source singleton factors q0,q1,q2,q3 whose physical point-side or line-side pair images form an actually occupied complementary physical C4. Under the SAME globally injected opposite type mapping, write pinned opposite physical edges (u,v), (v,w) with u,v,w all distinct and actual opposing factors pinned to the two real root source incidences.

If physical edge (u,w) is missing, the same-triangle sector is zero. Otherwise its actual inverse original factor \`c = g^-1({u,w})\` must be assigned to exactly one actual original source singleton row q_k with \`c∈N(q_k)\`, where \`N(q)\` is its TRUE ORIGINAL W(3,s) opposite factor neighborhood (degree d=s+1). The remaining physical triangle consists of \`xy\`,\`yz\`,\`xz\` with **canonical x<y<z**, all globally occupied (opposite) physical edges and outside {u,v,w}.

For each genuine accepted original six-incidence-ID Q the unique ORIGINAL singleton row q_i consuming physical edge \`xy\` and the unique q_j consuming \`yz\` satisfy that these opposite actual factors belong to \`N(q_i)\`,\`N(q_j)\`. Accordingly enumerate:

1. the unique q_k matched to the forced actual opposite closing factor c (at most 4 choices);
2. the actual source opposite neighbors of one of three distinct remaining source q_i (at most d factors) whose global pair image is canonically \`(x,y)\`, outside pinned coords;
3. one of the two remaining actual source q_j and at most d ORIGINAL opposite source neighbor factors whose global physical image is canonically \`(y,z)\` with y<z and z outside pinned coords;
4. verify that physical edge (x,z) is globally occupied, and its actual inverse original factor is genuinely adjacent to the uniquely last remaining source row q_r.

The selected original six-ID Q is uniquely recovered; every accepted same-triangle Q supplies exactly one ordered triple x<y<z and unique row owners k,i,j,r. This counts source matchings and hence correctly charges both matchings of any true source C8.

**All-f,g, all-h source-degree UPPER bound**, per fixed actual anchored root/flags/C4:

    T_same_triangle_adjacent <= (4 choices k)(3 choices i)(2 choices j)d²
                             = 24(s+1)².

This is a GENUINE ORIGINAL accepted-Q UPPER bound, not a positive lower.

## 3. NEW exact all-h source-Hall formula for adjacent-pinned CONNECTED C6

The physical pins force \`u-v-w\`. The unique remaining physical path is \`w-x-y-z-u\`, so unpinned physical opposite edges are

    [w-x, x-y, y-z, z-u],

with x,y,z all distinct and outside {u,v,w}; every edge must belong to the SAME globally fixed opposite physical image g, with actual inverse original opposite factors. Assign the physical edges \`xy\` and \`yz\` to two distinct genuine original singleton rows q_i and q_j, respectively. Necessarily \`g^-1(xy)∈N(q_i)\`, \`g^-1(yz)∈N(q_j)\`, with exact original GQ degree d=s+1. Enumerate:

1. four actual first internal-edge row choices q_i, and at most d actual opposite neighboring factor source IDs for \`xy\`; its physical pair (a,b) has exactly two possible path orientations (x,y)=(a,b) or (b,a), with neither coordinate among u,v,w;
2. one of three *other* genuine singleton source rows q_j, and at most d actual opposite neighbor factors whose globally fixed physical pair image shares exactly the oriented midpoint y; its other endpoint is z, different from x and outside pinned coordinates;
3. check that global physical \`w-x\` and \`z-u\` are occupied, inverse-map them to REAL original opposite factors, and count which of the two exact assignments of these columns to the other two genuine q rows are present in the ORIGINAL W(3,s) incidence graph.

Each genuine accepted original Q in this sector has a **unique** physical pinned u-v-w path, a unique reverse oriented complementary w-x-y-z-u path, and a unique original source matching owner for each internal edge xy,yz; thus it is counted ONCE. A single H with 2 original matchings legitimately contributes 2 genuine source Q (only genuine source C8 permits 2). No O(a³) physical auxiliary triple enumeration is required for original Hall: per fixed source C4 the direct algorithm uses O(d²) original factor adjacency tests after source index preparation.

**All-f,g all-h source-degree UPPER**, for one anchored actual root/flags/C4:

    T_adjacent_connected_C6 <= (4 choices qi)(d)(2 physical xy orientations)
                                (3 choices qj)(d)(2 matchings remaining)
                             = 48(s+1)².

Again this is genuine source-Hall count UPPER, NOT a lower or a free-standing Branch A proof.

## 4. AA4-AK full all-h TRUE ORIGINAL B/A and A/B identity — now complete

The new executable \`full_original_A_Hall_cohort(...,four=real_original_C4)\` selects the actual globally fixed pinned physical edge relation, and uses:

- disjoint pins: exact AA4-AH split two triangles + exact AA4-AJ all connected physical C6;
- adjacent pins: exact AA4-AK same-component two triangles + exact AA4-AK connected physical C6.

For EVERY actual original W(3,s), any actual globally injected complete f,g, real original rooted source B and any physically occupied original singleton-factor C4,

    T_B/A_cohort =
       T_split_disjoint_triangles
       + T_same_adjacent_triangles
       + T_disjoint_pins_connected_C6
       + T_adjacent_pins_connected_C6.

Each term is a **nonnegative integer** and counts selected actual ORIGINAL six DISTINCT incidence-ID Q, with true physical 6-coordinate 2-regular A and original 4-rook matchings, no independent labels, and no orbit quotient. Exactly one term can be nonzero for the physically fixed relation disjoint or adjacent (the two terms for the other relation are zero). There is NO fifth physical A sector. The type-dual construction applies for original A/B with line doubled source and point opposite factors.

Combining the genuine source degree bounds:

| Opposite pinned physical geometry | Genuine ORIGINAL true accepted single-root/C4 cohort bound |
|---|---|
| disjoint pins | \`T_split<=24d²\`, \`T_C6<=48d²+192d\`; total <=\`72d²+192d\` |
| adjacent pins | \`T_same<=24d²\`, \`T_C6<=48d²\`; total <=\`72d²\` |
| **universal either relation** | **\`T_B/A or T_A/B <=72(s+1)²+192(s+1)\`** |

These are source-degree-based **UPPER** bounds. They do NOT establish the source-Hall positive density needed for the original HYP-105 theorem. For large h the local accepted Q cap is O(s²) while earlier pre-Hall occupied opposite physical pattern mass can be much larger; the issue concerns aggregation and concentration across ACTUAL rooted first-side C4 and genuine global source geometries.

## 5. Independent finite evidence / scope

The dedicated four hosted CI groups include:
1. EVERY adjacent pinned pair in complete physical K6,K7,K8, enumerated using the independent earlier AA4-AD H enumerator; check exactly \`C(a-3,3)\` same-component physical triangles, \`6 C(a-3,3)\` connected physical C6; no split triangle leakage.
2. Genuine ORIGINAL W(3,2) across FIVE distinct complete globally bijective typed physical map pairs: the original AA4-AI dual-zero witness, lex, reverse, S68, S72. For EACH mapping and EACH type orientation ALL fifteen actual source roots × three genuine original flag pairs × three actually occupied first-side physical C4s = 135 anchored source cohorts. Compare NEW source-degree path-transfer, COMPLETE four-sector per-cohort counts, and independent earlier AA4-AI full original physical H × 24 genuine source rook matching oracle. Aggregate then matches historical accepted genuine ORIGINAL B/A / A/B counts respectively:
    - dual-zero: 46 / 61
    - lex: 98 / 110
    - reverse: 77 / 74
    - S68: 44 / 21
    - S72: 36 / 31.
3. The frozen dual-zero witness exact four-sector split (point B/line A vs line B/point A):

| TRUE ORIGINAL physical-A sector | point B / line A | line B / point A |
|---|---:|---:|
| disjoint pinned split-two-triangle | **0** | **0** |
| adjacent pinned same-triangle | **6** | **3** |
| disjoint pinned connected C6 | **17** | **41** |
| adjacent pinned connected C6 | **23** | **17** |
| **TOTAL** | **46** | **61** |

The dual-zero example explicitly demonstrates complete compensation of the split-triangle zero by valid original accepted A subtypes under one SAME complete globally fixed f,g, not fake source forests or physical orbital averaging.

4. TRUE ORIGINAL W(3,4) over actual symplectic GF(4) GQ and both typed orientations, lex/random complete globally injected but non-surjective K14 pair maps (exactly six missing physical edges per type), several real roots, flags and original actually occupied complementary C4. Every anchored cohort checked against earlier independent literal H and 24-permutation actual original source rook oracle.
5. Actual symplectic original source automorphism and TWO independently selected physical point and line coordinate relabelings preserve four-sector accepted true original totals. Malformed partial/fake originals, non-injective physical source factor maps and impossible physical C4 are rejected. Exact all-h integer degree-cap tests at h up to 25 do not simulate nonexistent large finite projective geometry.

The classical bipartite 4-rook permanent identity and GQ girth-eight source bound are earlier results; the mathematical contribution is their complete globally coherent source-incidence-anchored transfer through the final missing physical A sectors, with explicit exact all-h complexity and degree-based bounds. Do not claim the general combinatorial 4-rook/permanent theorem is novel.

## 6. Routing, acceptance, mathematical next steps

This is a **research-only exact all-h transfer theorem**, NOT independent final mathematical acceptance. Strict Draft PR on AA4-AJ #521; keep branch stack and full exact-HEAD GitHub-hosted dedicated, INDEX, Proof Audit, and Full Research check evidence. Separate independent mathematical referee and formal RCP JSON accepted claim review required before regenerating any five Markdown registry files or merging to main. **Issue #230 remains OPEN**, no Branch A/B/C or full R3/ASET result.

**Recommended next AA4-AL mathematical step:** the full physical-A sector is now exact and exhaustive; stop adding physical completions. Investigate genuine global source-incidence constraints that force the sum of the four sector true Hall counts over ALL actual original roots, flag pairs, and physically occupied first-side C4 to exceed c*s^6 for arbitrary complete correlated f,g, OR find a valid infinite asymptotic correlated map failure and separately analyze the other seven GF5/D6 classes. An unconditional universal lower is *not* inferred from the all-f,g exact transfer or the local upper. Work with a suitable aggregate incidence-spectral or four-index energy inequality, avoid resampling physical labels per Q.
