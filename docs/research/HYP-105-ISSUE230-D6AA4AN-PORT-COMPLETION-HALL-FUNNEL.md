# HYP-105 / issue #230 — AA4-AN: exact original D-pair port completion and source-Hall funnel

**Research-only Draft child of [AA4-AM #530](https://github.com/definitely-stable/Mathlab/pull/530), pinned parent original HEAD \`2b1adc66145bc6e1af278f0d61b18a16f0b368ea\`.** All mathematical claims concern REAL source W(3,s), s=2^h≥2, true ORIGINAL distinct point-line incidence flag IDs, full globally injected point and line source-factor physical unordered-pair maps f,g, the same global two maps for every pair/sextuple. No synthetic forest or per-Q relabeling. This does NOT prove Branch A S=Ω(s^6), Branch B infinite original globally injected counterfamily, full signed GF5/ASET exponent, or a universal positive source Hall fraction. Independent mathematical referee required.

## 1. Global AA4-AM pair obstruction motivates local-to-global charging of ACTUAL SIX-ID extensions

AA4-AL proves every full globally injected original f,g yields D_unordered≥s^5 true bilateral ORIGINAL two-flag pairs e={(p,l),(q,m)}, p≠q,l≠m, physically sharing one point coordinate and one line coordinate. AA4-AM established exact seven-positive-GF5 genuine six-ID extension hypergraph E=Σ_{Q∈S}k(Q) and the valid U+E/6≤S≤U+E relation; importantly, a finite W(3,2) S68 global map has **193 of 257 D pairs with no seven-positive-GF5 extension**, so an all-h h≥1 every-pair positive original continuation lemma is FALSE.

The new mathematical task is to pinpoint WHICH step fails: (a) physically allowed/occupied both typed projections, (b) perfect matching of true-original source factors into four more genuine original incidence flags, or (c) GF5 seven-class classifier rejecting unaligned A/A. Previous D/E coverage counts alone could not distinguish these obstruction layers.

## 2. NEW all-h three-topology exact physical four-factor port completion theorem

Fix a genuine ORIGINAL AA4-AL D pair of actual distinct flags. On point physical label side f, the two distinct globally injected physical edges share one and only one physical coordinate c. Their other coordinates are distinct physical ports a,b. On line physical label side g, independently there are one closed center c' and two distinct ports a',b'. Since a selected GF5 six-Q physical projection requires precisely SIX distinct physical coordinates, each of degree TWO across six actual flag source factor labels, the center c has already received degree 2 (from the two D flags), each old port has remaining degree 1, and exactly THREE NEW physical vertices x,y,z each require degree 2. The remaining FOUR physical pair-edge slots are a loopless multigraph on five vertices {a,b,x,y,z}, with degrees (1,1,2,2,2). Repeated unordered physical pair-edge images are allowed ONLY as repeated use of the SAME globally injected original source factor, corresponding to different genuine original incidence IDs of that same source factor; they cannot be treated as distinct original factor labels.

The entire physical multigraph family contains precisely these THREE topologies for each unordered triple {x,y,z} disjoint from the closed center and ports:

1. **P5:** the two ports are joined by a FOUR-edge path through all three new vertices. Exactly 3!=6 distinct physical edge-multisets per new triple, determined by the order of x,y,z along port-a→port-b.
2. **K2+C3:** the ports a,b form the one edge ab, while the three new vertices form a physical triangle. Exactly 1 physical edge-multiset per new triple.
3. **P3 + parallel K2:** both ports a,b join the SAME new midpoint (one of three possibilities), and the other two new coordinates are joined by a physical edge used TWICE (one globally injected original source factor, two DIFFERENT true incidence flags). Exactly 3 physical multisets per new triple.

**Exhaustion proof:** If the ports connect directly, the remaining three degree-two vertices must form a triangle. If the ports connect to distinct new vertices, the remaining two edges must link those two through the third vertex, giving the P5. If the ports connect to the same new vertex, that vertex's degree quota is saturated and the remaining two new vertices require two copies of their mutual edge, giving the P3+parallel K2. No loops or third type possible. Each constructive case produces exactly six distinct physical coordinates with degree 2, and the three cases have different graph structures; all are unique.

There are a−3 available physical coordinates outside the three pinned coordinate vertices, so the **EXACT** formal physical completion counts for each typed projection under EVERY complete globally injected f,g, ALL s=2^h:

| Residual physical source pattern | Per original fixed typed D pair |
|---|---:|
| P5 | 6 C(a−3,3) |
| K2+C3 | C(a−3,3) |
| P3+parallel K2 | 3 C(a−3,3) |
| **TOTAL one typed side** | **10 C(a−3,3)** |
| **TOTAL formal point×line two-side patterns** | **100 C(a−3,3)²** |

**Crucial scope:** these are **FORMAL** physical multigraph completions. Every edge must be an ACTUALLY OCCUPIED globally injected typed original source-factor physical image in the corresponding same f,g. For minimal physical K_a injection, missing physical edges can eliminate arbitrary patterns. Even two-sided occupied physical patterns can fail TRUE original incidence matching. The count is absolutely NOT a lower bound for genuine accepted six-Q.

**Independent test:** an entirely DIFFERENT exhaustive implementation enumerates all possible four-edge physical multisets via \`combinations_with_replacement\` over the full allowed physical K_a edges, filters directly by degree=(1,1,2,2,2) on precisely five vertices, and compares the literal resulting multisets with the three constructive physical families. Exhaustively tested on K6, K7, K8. This is an enumeration witness, not a proof in itself; the case split above proves the general statement.

## 3. NEW exact genuine-original complete seven-positive-GF5 D-PAIR source Hall funnel

Fix one genuine D pair and the very same globally injected actual point f and line g.

- **Physical step:** construct all 10 C(a−3,3) point residual four-source-factor physical edge multisets, filter each by actual f-image occupancy, inverse map every edge occurrence to a real original source point factor ID. Independently construct line residual four-factor multisets from the corresponding physical line coordinate ports, filter by the SAME globally fixed opposite original line map g and inverse map to real original source line factor IDs. At K6 full global physical bijections the physical occupancy step leaves EXACTLY 10 point and EXACTLY 10 line patterns for EVERY actual D pair, giving EXACTLY 100 paired physical completion templates.
- **TRUE original Hall step:** for each pair of physically occupied point/line multisets of 4 factors, test all at most 4! assignments of the four actual source line factor slots to the four original source point factor slots. Accept only genuine \`(p_i,l_{\pi(i)}) ∈ I(W(3,s))\`; require the four additional actual incidence IDs to be distinct from each other and from the two pinned original D flag IDs. Repeated source factor slots are legal only when they yield different ORIGINAL incidence flag IDs. Deduplicate the accepted Q by its complete sorted set of six ORIGINAL incidence IDs; this prevents false multiplicity from permutations between two equal-source-factor slots.
- **TRUE original seven-GF5 selection step:** compute the actual original source factor multiplicity partition A/B/C on EACH type and invoke the independent exact seven-class original \`independent_joint_classify\` (AA4-Q). C/C is impossible due to original GQ girth eight. For A/A, accept ONLY truly aligned six-position original physical dual connected six-cycles D6; reject every other unaligned genuine A/A Q. Every other positive original seven-GF5 class is accepted. The exact source-Hall six-Q set is partitioned into accepted selected seven-family Q and rejected unaligned A/A Q, with no invented additional classes.

This gives an **EXACT all-h original six-ID source-physical pair-to-seven-six-Q identity for ONE fixed actual D pair**. It does NOT bound the number of TRUE source-compatible matchings below by a positive quantity for arbitrary f,g. Brute implementation per specified original D pair takes at most \`O(100*C(a−3,3)^2*4!)\` checks after globally fixed maps and original adjacency exist; it is not claimed practical to enumerate this for ALL D pairs at large s, and does not create fake large finite original GQs. The asymptotic analysis needs new bounds on the two-sided physically occupied port-pattern overlap and genuine-original source Hall matching rate.

## 4. Original W(3,2): entire D-first positive extension + genuine source Hall failure census

For every one of FIVE complete globally injected typed point/line original physical K6 map pairs (AA4-AI dual-zero, lex, reverse, S68, S72), for EVERY genuine AA4-AL D pair, the new independent physical-port-first algorithm reconstructs its complete six-ID true original Q extensions, partitions physical/Hall/7-GF5 stages, and compares the EXACT Q→tag map against the separate historical 62,370 original left sixcoordinate candidate source oracle. This is a stronger independent check than the earlier AA4-AM aggregate E/U/covered histogram matching: it must agree **on every ORIGINAL D pair's exact list of selected six-ID original Q**, not merely the final totals.

The source matching stage can be empty EVEN WHEN both physical projections offer all 10×10=100 occupied physical completion template pairs; such a D pair is a genuine source-Hall obstruction, not an absence of physical source factors or random physical labels. Conversely, source-matched actual six-Q may have two physical leafless typed projections but be unaligned A/A and hence not accepted in any of the seven positive GF5 selected classes. Their finite counts will be frozen in the document from the final first-pass independent GitHub-hosted CI logs.

Expected independent AA4-AM true sevenclass results that MUST be reproduced:

| W(3,2) globally fixed source f,g | All D | Selected S | Exact D→seven Q edge charge E | D covered by seven-Q | D unextendible into all seven |
|---|---:|---:|---:|---:|---:|
| dual-zero | 277 | 123 | 164 | 115 | 162 |
| lex | 307 | 259 | 517 | 212 | 95 |
| reverse | 300 | 169 | 246 | 166 | 134 |
| S68 | 257 | 68 | 79 | 64 | 193 |
| S72 | 261 | 72 | 75 | 59 | 202 |

This finite genuine original source evidence does NOT disprove any all-h asymptotic assertion restricted to sufficiently large h, and does NOT provide a full infinite counterfamily or Branch B. It is a rigorous falsifier of universal finite h>=1 "all D pair extend to accepted seven positive GF5 Q" and separates the THREE stages needed for a viable nonvacuous eventual extension-energy lower.

## 5. True W(3,4) local audit without fabricated global seven-family census

On actual original symplectic W(3,4), V=85, a=14, K14 physical palette contains exactly SIX missing edge images for each typed global injection. The same all-h formula yields 10*C(11,3)=**1650** FORMAL residual typed physical patterns per true D pair. The code explicitly reports how many remain globally occupied under lex/random physical typed injections; **no physical occupation positive guarantee for each D pair is assumed**.

The finite W34 test independently extracts a small selection of genuine accepted original B/A and A/B six-ID Q from the prior original Hall four-row complete physical A H enumerator. For each genuinely D-anchored Q, the code independently reconstructs the original residual point-typed and line-typed physical 4-edge multisets and identifies exactly one of P5, K2+C3, P3+parallel K2, and verifies the original pair is in the completely enumerated genuine AA4-AL D population. No unsupported full W34 seven-GF5 census, no physical factor redraw, no bogus large W(3,s) reconstruction.

## 6. Scientific conclusion / AA4-AO gate and integration

The all-h theorem is the exact THREE-pattern source-physical extension framework for ONE original D pair, with complete genuine point-line Hall and GF5 seven-class selection. It explains why the AA4-AL \`D=Omega(s^5)\` guarantee does not imply positive sevenclass E: two-sided occupation of 100*C(a−3,3)^2 physical templates and actual original four-incidence matching are DISTINCT hard constraints, and unaligned A/A originals are a third real selection gate.

**NEXT AA4-AO**: Derive a nontrivial ALL-f,g global lower on the number of D pairs with one or more physically occupied *and* source-Hall-compatible three-pattern completions; alternatively, prove a lower on total genuine extension multiplicity E or genuine unanchored class U. Study source neighborhood expansion of residual physical pattern factor lists (not one center-cell mixing alone), their adversarial correlation across point/line f,g, and the true original four-source Hall perfect matching. Before claiming a positive theorem, test it against known W32 all-seven zero-extension D pairs, and distinguish finite s=2 from eventual s≥s0.

Keep the child PR Draft on prior AA4-AM #530 and preserve the entire ordered dependency stack. No main merges, no formal accepted RCP claim or generated registry rebuild until exact-HEAD dedicated/INDEX/Proof Audit/Full Research and independent mathematical referee. Issue #230 remains OPEN. The prior ASET/GF5 exponent question remains unresolved.
