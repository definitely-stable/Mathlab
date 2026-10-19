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

## Roadmap after this step

**AA4-CQ:** identify which source-POINT-A/B/C classes, and especially original incidence-local 3path projections, dominate the entire W34 seven-count for different f,g; seek exact model-equivalent inequality useful for root Branch C or an explicit all-h c>0 bound / genuine correlated infinite small-S counterfamily. New local covariance/Gram work alone is not an allowed substitute.

Root #230: **OPEN_WITH_FORMAL_BLOCKER**.
