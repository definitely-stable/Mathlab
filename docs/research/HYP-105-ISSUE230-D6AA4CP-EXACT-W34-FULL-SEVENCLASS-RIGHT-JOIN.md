# HYP-105 #230 — AA4-CP: exact all-seven ORIGINAL W34 source-incidence right-to-left join

**Scientific Draft, not root closure.** Strict child of [AA4-CO #615](https://github.com/definitely-stable/Mathlab/pull/615), parent pinned SHA `8bb574755ac15dd77bb27558f8c58204167384f5`. Research-only additive C++17 exact join, Python fixture/validation wrapper, independent regression, GitHub-hosted workflow, proof. main and the accepted historical original seven GF5 weights unchanged.

## Problem and why another local covariance will not help

Root [#230](https://github.com/definitely-stable/Mathlab/issues/230) asks for an explicit ALL-h positive `S_s(f,g)>=c*s^6` for EVERY complete globally injected arbitrary correlated original typed POINT f, LINE g on authentic symplectic W(3,2^h), OR a concrete infinite genuine original S=o(s^6) counterfamily, OR model-equivalent reduction. `S_s` is the UNWEIGHTED count of all seven disjoint historically accepted true six-DISTINCT original incidence-ID GF5-positive leading source classes. The historical positive GF5 necessary-weighted numerator `W_s` is a separate metric and not full R3. AA4-CO/#615 constructed complete genuine W32 fixed-map 96-map selected sevenclass S countercontrols (127..190, 72..167); prior AA4-CL–CN covered just two overlapping POINT-A sixfactor source fibers. The actual next gap is making a fast-enough **full sevenclass exact original Q oracle work on W34**, without treating physical degree2 as historical positive.

## Exact all-h combinatorial representation behind the algorithm

For any genuine W(3,s) original factor incidence graph and ANY complete injective physical maps f,g, every HISTORICALLY ACCEPTED original sixflag Q necessarily has RIGHT physical degree2 on exactly six physical coordinate vertices. The complete right original LINE source multiplicity is necessarily one of:

* **A = six different original LINE factors.** Their SIX different occupied physical right edges form a 2regular simple graph on exactly six physical coordinates. On six vertices this is either a connected C6 or disjoint pair of C3. List each unordered set of six physical right coordinates, then its 70 simple sixedge 2factors (60 C6 and 10 C3+C3). Check all six edges are actually assigned to distinct full original LINE source factors by the fixed complete g. For each LINE source, independently select ONE of its s+1 ACTUAL original incident POINT factor IDs and retain the true distinct original sixflag Q=(p_i,l_i). These actual original Q each appear exactly once in source-right A.
* **B = one original LINE factor used TWICE and four others used ONCE.** The repeated physical right edge saturates its two coordinates; the four remaining coordinate vertices must form a simple physical C4 with four different occupied right line edges, of which there are exactly THREE per fourset. Choose TWO distinct actual original POINT incident IDs from the repeated original LINE source factor (`binom(s+1,2)`), one from each other LINE source (s+1), and retain the six true original Q. Each right-source B Q appears once and never under A/C enumeration.
* **C = three original LINE factors each used TWICE.** The three distinct globally injected physical right line edges form a perfect matching of six physical coordinates (exactly 15 matchings per coordinate sixset). Choose TWO distinct actual original POINT neighbours per original LINE source, each exactly once as an unordered selection. Each right-source C Q appears once and never under A/B.

The case of EXACTLY TWO doubled original source factors is impossible for any physical sixcoordinate degree2 projection: it leaves two physical vertices and two single original source edges; injectivity forbids the two distinct edges using the same remaining physical pair. Threefold LINE source multiplicity is impossible because it gives physical vertex degree >=3. This is precisely the A/B/C classification used previously on the LEFT side, now implemented symmetrically as a RIGHT-first enumeration. Since every accepted original Q has one of these types, the right-first candidate generator is exhaustive for accepted classes. Since every genuine source Q has a UNIQUE right original LINE source multiset and actual distinct original incidence-ID set, the enumerator is also nonduplicating.

**Important restriction:** Enumerating the right physical degree2 projection is a COMPLETE physical **necessary** candidate generator but does **NOT** itself count a historical GF5-positive Q. Every selected true original Q must additionally pass the original LEFT physical degree2 test on exactly six coordinates, and the ORIGINAL historical sevenclass predicates including aligned incidence-position dual connectedness for D6 and actual sixflag repeated-source overlap. All unaccepted necessary shapes are excluded from S and W.

## Genuine original join implementation

A Python wrapper builds the actual complete original source GQ fixture using existing `_original_source` (checks complete typed injection, actual original LINE stars, unique six-incidence IDs, GQ C4-freeness), then writes the actual physical pair images of **ALL original POINT and ALL original LINE factors** and the complete original incidence table to a temporary input for a deterministic standard-library C++17 exact integer join engine. No per-Q, per-pattern or correlated g redraw.

For right source A/B/C patterns each actual source LINE has respectively one or two selection slots, and each uses its true original s+1 incident POINT neighbours. A DFS expands only this list of legal original-incidence choices and tracks the cumulative physical LEFT degree vector in 4-bit packed coordinate counters. If any accumulated coordinate degree exceeds 2 it is impossible to repair by adding more original incidence flags, so the branch is safely pruned. On exactly six selected actual original flags, require exactly six left physical coordinates each degree2. Apply the original same-six-incidence historical seven-GF5 classification:

```text
left A, right A -> D6 only if connected left/right six-column
                   labeled original incidence-position duals coincide;
left B, right A -> B-left/A-right;
left A, right B -> A-left/B-right;
left C, right A or left A, right C -> C/A;
left B, right C or left C, right B -> C/B;
left B, right B -> original repeated-POINT and repeated-LINE flag
                   position sets intersect at exactly one: B/B-overlap;
                   otherwise B/B-disjoint.
```

Each accepted original Q contributes exactly one historical positive class and its immutable weight `(5643,45600,45600,43320,49050,51750,45010)`; two integer sums are reported: full root UNWEIGHTED S and separate historical accepted GF5 necessary W. Using 64-bit packed 4-bit-per-coordinate counters is EXACT for six-edge patterns when physical alphabet a<=16; higher h/W38 is rejected, not silently approximated. C++ counts use uint64 counters checked against original W32 accepted sevenclass total; no source geometry independent-random assumptions. This initial fast engine targets W32 (a6) and W34 (a14), not an asymptotic fast all-h census algorithm.

**Algorithmic cost:** right physical sixcoordinate palettes `binom(a,6)`; each palette has at most 70 right A edge patterns, 45 right B patterns and 15 right C matchings. Expansion of actual original LINE factor neighbour selections costs `(s+1)^6`, `binom(s+1,2)(s+1)^4`, `binom(s+1,2)^3` respectively BEFORE LEFT degree pruning, so exact high-h runtime is large and **no polynomial-in-s complexity guarantee is claimed**. Nevertheless right-to-left degree pruning, compiled deterministic integer joins, and a direct single pass make this viable for a finite genuine W34 full accepted-sevenclass audit on hosted Linux.

## Independent validation and falsification plan

1. Real original W32 (s=2, V15, 45 original incidence IDs, physical K6), complete f,g lex: run the new *RIGHT-first* C++ original incidence join and compare **each of the seven accepted historical classes individually** with the pre-existing independent *LEFT-first* `seven_census` oracle (plus their unweighted root S and weighted GF5 W). This independently certifies class partition and no duplication.
2. Repeat on genuine original W32 S72 complete correlated f,g, which breaks artificial source alignment and exercises right factor repeated source categories.
3. Compute **ENTIRE W34 s4,V85,425 original incidence IDs** original sevenclass S and W for complete lex f,g using this right-to-left exact source join, not source-point-A subset. Repeat on independent shuffled complete f,g W34 fixture. Pin exact category vectors, candidate count and runtime-independent regression results from GitHub-hosted CI. Full W34 is the decisive next finite root-statistic data, not a theorem of universal root A or B.
4. Fail closed for true original W38 (a>16) rather than claim an unsupported complete arbitrary high-h candidate count. Validate immutable original accepted GF5 class weights and actual GQ pair factor injections.

**Kill criteria:** any single accepted W32 category differs from independent legacy classifier, any result depends on source Q per-pattern redrawing, any true-original W34 right-origin shape misses a positive accepted class, or any claim finite W34 implies global all-h lower: NO-GO. No main merge until exact-head dedicated hosted check, proof audit, general Research, qualified independent human mathematical review, and ancestor scientific PR integration.

## Exact final ORIGINAL source-W34 results and independent proof-audit boundary

The following are complete **fixed-map** observations for TWO globally injected physical labeling configurations on genuine symplectic W(3,4), each with 85 POINT factors, 85 LINE factors, 425 different ORIGINAL incidence IDs and physical pair alphabet K14. They use TWO different complete globally injected pairs f,g (a deterministic `lex` source-label assignment, and a genuinely correlated deterministic shuffled `random` assignment). Every ORIGINAL six-incidence-ID Q is held fixed on both physical projections. Unweighted ROOT-relevant accepted seven-motif `S` is separately reported from the historical accepted GF5 necessary weighted numerator `W`.

| Accepted historical positive class | Original W34 lex | Original W34 random |
| --- | ---: | ---: |
| D6 (5643) | 8,481 | 7,295 |
| B-left/A-right (45,600) | 181,793 | 164,462 |
| A-left/B-right (45,600) | 171,203 | 162,557 |
| C/A (43,320) | 22,913 | 20,351 |
| C/B (49,050) | 3,973 | 4,356 |
| B/B-overlap (51,750) | 22,111 | 24,168 |
| B/B-disjoint (45,010) | 23,051 | 18,222 |
| **ROOT selected original seven-motif UNWEIGHTED S** | **433,525** | **401,411** |
| **Selected historic seven-GF5 NECESSARY weighted numerator W** | **19,513,712,453** | **18,119,365,425** |

For the same actual original host and its **completely unchanged full maps**, the engine independently examined all right-source physical A/B/C cases then checked the LEFT degrees, obtaining **1,036,770** (lex) or **981,639** (random) physically eligible six-coordinate Q on BOTH typed sides. Those counts include both accepted and rejected historic GF5 Q: lex has 603,245 rejected and random 580,228 rejected. **No physically eligible Q is automatically accepted**: original six-position dual matching for source A/A is required, as are the accepted seven source multiplicity tags.

### Independent FULL 6ID-set POINT↔LINE dual check, not a numerical symmetry guess

For EACH complete real original W34 f,g input, a separate run exchanges *all* typed POINT and LINE source factor IDs, all complete physical pair f,g images, and all actual original incidences (p,l)→(l,p) IN THE SAME ORIGINAL flag index order. This enumerates candidates starting with the OTHER physical side (an independent transposed traversal of the source incidence graph). It must reproduce EXACTLY the SAME set of **1,036,770 or 981,639 sorted ORIGINAL six-ID Q tuples**, not merely the same count. It does.

The class frequencies under typed duality obey D6↔D6, B-left/A-right↔A-left/B-right, C/A↔C/A, C/B↔C/B, B/B-overlap↔itself and B/B-disjoint↔itself. Both original and dual W34 passes report identical S and W, and the exact class transpositions above. An independent existing ALL-coordinate genuine-original historic classifier, separate from the new C++ pattern construction and degree2 packed engine, is then run against **EVERY one of the million original sixflag Q accepted PHYSICALLY on BOTH sides**. It reconstructs the same seven accepted tag histogram plus explicit rejected count 603,245 /580,228. This exceeds a sampling-only test: it checks EACH actual TRUE original Q even when it is historically rejected.

The regression pins all seven absolute counts, two totals, the exact two-sided physical candidate count, complete matching original six-ID sets under typed duality, and independent historic classifier agreement. W32 `lex` and `S72` retain separate prior LEFT-first `seven_census` acceptance with all seven individual categories; a wrong W34-only size assumption cannot hide behind W32's V=15.

### Critical implementation bug independently falsified and corrected

The first GitHub-hosted W34 run was **not valid**: C++ originally declared a fixed array of 16 `fcode` values indexed by ORIGINAL POINT factor ID, although W34 has `V=85` original POINT factors. It therefore read/wrote OUT OF BOUNDS and produced spurious intermediate `S=0` (lex) and `S=107` (random) values. These intermediate values are **RETRACTED**; they are NOT genuine W34 counterexamples or scientific evidence of a root B construction. The issue was detected because true source POINT↔LINE dual candidate sets were inconsistent, even when historical sevenclass output itself looked plausible. A pinned missing original sixflag Q was traced independently through physical right pattern, real source LINE star alternatives, and the packed physical LEFT degree sum, which exposed corruption of `fcode`.

The corrected implementation uses a dynamically sized `std::vector<uint64_t> fcode` with EXACTLY `V` entries indexed by true original POINT source ID, separately from the fixed physical coordinate packing capacity `a<=16`. W34 full original bidirectional source Q-set checks and the independent historical class tagger now agree to the exact original sixflag level. Regression fails if a future change reintroduces V-vs-a confusion or mismatched original Q enumeration.

### Runtime scope and root verdict

This is an EXACT practical finite W34 full sevenclass original sixflag solver but **NOT** a new uniform efficient all-h counting theorem. Its RIGHT enumeration examines roughly 1.4 billion completed candidate source-Q combinations per genuine W34 input **at the terminal recursion level after early-degree pruning** (the C++ `source_Q_right_deg2_tested` counter), and source factor LINE A/B/C shape constraints plus monotone LEFT physical degree pruning make it tractable on GitHub-hosted Linux. The input source remains the original symplectic GQ and the historical fixed sevenpositive GF5 taxonomy, never an independently sampled physical surrogate.

A positive finite W34 `S` from two fixed complete f,g schemes, even alongside positive W32, does not prove a universal infimum `S_s>=c*s^6` as h→∞, since no all-h c>0 for *every* fixed complete correlated f,g is derived. It also does NOT refute the possibility that other original f_s,g_s at larger h give S=o(s^6). No full R3 or ASET bound is implied. Root #230 **OPEN_WITH_FORMAL_BLOCKER**.

**Next mathematically meaningful research gate:** AA4-CQ — use the now-audited full original W34 sevenclass source counts to identify exact original GQ incidence joins with polynomial algebraic lower bounds under arbitrary complete correlated f,g, including all source POINT-A/B/C. Alternative: build a qualified original globally injected infinite correlated small-S construction. A finite W34 lex/random comparison is a falsifier, not an asymptotic proof.

## Roadmap after this step

**AA4-CQ:** identify which source-POINT-A/B/C classes, and especially original incidence-local 3path projections, dominate the entire W34 seven-count for different f,g; seek exact model-equivalent inequality useful for root Branch C or an explicit all-h c>0 bound / genuine correlated infinite small-S counterfamily. New local covariance/Gram work alone is not an allowed substitute.

Root #230: **OPEN_WITH_FORMAL_BLOCKER**.
