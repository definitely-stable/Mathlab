# HYP-105 / #230 — AA4-BV-C/A: exact fourth-order source anchor multiplicity and true GQ line intersections

Scientific DRAFT, strict child of AA4-BU #592, corrected parent head d456cd98d47be793eca1b1f1a5131b4ad683c641. Parallel AA4-BU #593 and AA4-BV #594 form a separate stack; #594 already bounds the original fourth-order historical C/B class through authentic GQ line transversals by O(d²), and this research explicitly does NOT repeat or claim that result. This AA4-BV-C/A branch targets the remaining original C/A fourth-order sixflag source-GQ bound and a separately falsifiable EXACT anchor-counting identity. Earlier #476 seven-class taxonomy, #587 all-seven disjoint source-factor swap locality, #590 source Walsh covariance and #591/#592 sixth/fifth incidence bounds are prior. Keep main, root and accepted registry untouched.

## Correct input quantifiers

For EVERY genuine symplectic original W(3,s), s=2^h, h>=1, arbitrary potentially correlated completely fixed globally injected typed physical POINT image map f and LINE image map g, and FOUR mutually disjoint pairs of WHOLE ORIGINAL LINE source-factor pair-edge image transpositions, set V=(s+1)(s²+1) true original POINTs and LINES, d=s+1 genuine original incidence flags per factor. Exactly six DISTINCT ORIGINAL incidence IDs Q are retained across both physical projections and all 16 complete global swap states.

Each original six-Q with nonzero fourth Walsh character on all FOUR selected source-factor swap bits must contain at least one original incidence flag from each of the four distinct actual two-LINE source-factor packets. Choose ONE genuine original incidence flag from each packet, called its marked ANCHOR quadruple. TWO other source Q flags can come from anywhere in the genuine original incidence system, INSIDE or OUTSIDE all chosen packets.

## BV-ANCHOR POINT-C classification and upper

Suppose original SOURCE POINT factor multiplicity is C=(2,2,2): the six true original incidence flags occur in three disjoint pairs at three different original POINT factors. The four marked genuine anchor flags can then have only POINT-profile (2,1,1) or (2,2). Four distinct POINT factors cannot be paired using only TWO more flags. A triple POINT occurrence cannot be completed to profile C.

GQ classical axiom: two distinct original LINE factors meet at at most one original POINT, even when taken from the same selected two-LINE packet; two packets consist of just two original LINEs each. Thus one pair of anchor positions repeating the same original POINT has at most 4 actual source flag-pairs.

CASE (2,1,1): choose which TWO of the four different source packets share one genuine original POINT (C(4,2)=6), their true original meeting flags in at most 4 ways; choose one source flag from each of two other actual packets in at most (2d)² ways. Every completed C-sixQ then requires one additional original incidence flag at each of the two singly used original POINTs. These are DISTINCT original POINTs, each already uses one genuine source flag, hence exactly d−1 choices at each such point. Number of MARKED anchor+completion occurrences bounded by
 6*4*(2d)²*(d−1)² = 96 d²(d−1)².

CASE (2,2): four marked source incidences consist of two pairs at two distinct original POINTs. Choose which perfect matching of four selected source packet positions pairs them (3 matchings), choose genuine LINE/LINE original point intersection flags for each pair in <=4² ways; hence <=48 genuine marked anchor quadruples. Two unmarked Q flags must lie on a THIRD original POINT distinct from the two anchor points, so there are V−2 choices of that genuine source POINT and C(d,2) choices of its two distinct original incidence IDs. Total <=48(V−2)C(d,2) marked completions.

Therefore TRUE original six-distinct-ID source POINT C candidates are at most the sum of these two numbers. Each source Q is counted AT LEAST ONCE, never zero, because it touches all four source packets. As a result

  N4_C <= 96d²(d−1)² + 48(V−2)C(d,2).

The fixed original POINT physical map f can ONLY reduce source candidates, since an accepted historical LEFT physical C shape requires three distinct original SOURCE POINT factor pair edges f(p1),f(p2),f(p3) occupying exactly six different physical endpoints. Also at fourth order the six original LINE factors must include at least four different IDs, so source right-C=(2,2,2) (only three distinct line factors) is IMPOSSIBLE. Historical original POINT-C left and right A or B give C/A or C/B positive classes only. Each genuine-original Q's fourth Walsh coefficient has magnitude <=1/2, yielding for C/A:

  |hat S_C/A(T)| <= 48d²(d−1)² + 24(V−2)C(d,2), for |T|=4.

This is O(s^5), a genuine W3 source-degree and line-uniqueness improvement over unrestricted sixflag subset counts. It is much WEAKER for C/B than separate parallel PR #594's genuine O(s²) fourth bound; DO NOT misattribute C/B novelty.

## BV-MULT exact TRUE-original six-ID anchor-weighted identity

Let n_i(Q) be the number of ORIGINAL incidence IDs of Q whose actual LINE source factor belongs to selected packet i (i=1..4). All n_i>=1. A genuine Q has exactly prod_i n_i(Q) different marked anchor quadruples, one original ID chosen from each of four packets. For each marked anchor quadruple with POINT-profile (2,1,1) there is exactly one unordered completion pair consisting of the other two original flags Q at the two singly used true original POINTs. Likewise for profile (2,2), its unmarked flags form exactly one pair on a third original POINT. Thus every Q contributes exactly prod_i n_i(Q) marked completions to the anchor construction. The algebraic weighted sum

  sum_over_all_real_anchors_and_completions 1 / prod_i n_i(Q) = number of DIFFERENT REAL original six-ID Q with POINT profile C touching all four line packets,

is an **EXACT** all-h identity, including when Q's two unmarked flags are inside an originally selected packet and one true Q has multiple anchor choices. It avoids the incorrect UNIQUE anchor assumption that affected previous fifth-order research. Every term is a positive rational and no fake independent per-Q image redraw occurs.

## Original W32 independent exact numerical witnesses

For true symplectic W(3,2)/K6 and genuine four ORIGINAL LINE source-factor whole-image transpositions (0,1), (2,3), (4,5), (6,7), the geometric anchor algorithm and an independent 1,062,720-iteration brute source flag oracle give exactly 1,059 original six-flag Q of POINT source profile C that touch all four source packets. Their RIGHT source-profile historical accepted-type partition is 781 C/A, 269 C/B, plus NINE true original six-Q with valid POINT C but source LINE profile NOT IN ANY accepted historical seven-GF5 class. These NINE Q are retained in exact source identity counts but **excluded from historical GF5 acceptance coefficients**; the initial test assertion that every original POINT-C source Q must have positive-source historical C/A or C/B type was wrong and removed.

Under complete globally injected f in original lex labeling 31 of the source POINT-C Q have the physical LEFT six-coordinate C projection; for complete original S72 f 47 have this property. On 16 common, globally injected full original right-image mappings, independent historical full seven-class census yields:

- original lex: fourth historical GF5 C/A Walsh coefficient -1/8, C/B 0.
- original S72: fourth historical GF5 C/A Walsh coefficient 0, C/B +1/16.

These exact values are pinned in regressions, not extrapolated to high h. The sign/zero of an individual fourth Walsh coefficient does NOT determine the original unchanged-center class count or the universal lower in #230.

## Reproducibility and falsifiers

Versioned Python source research/hyp105_issue230_d6aa4bv_fourth_original_GQ_CA_anchors.py, independent six-group tests research/test_hyp105_issue230_d6aa4bv_fourth_original_GQ_CA_anchors.py and three-job GitHub-hosted workflow. Genuine original W32/K6 fixture lex and S72: independent full 6^4*C(41,2)=1,062,720 four-packet-anchor + any other two original distinct flags per scheme (2,125,440 loops total) to classify original POINT-C Q, compared EXACT full six-ID SET and original f physical left-C-eligible source SET against separate constructive point-multiplicity completion enumerator. That second source witness computes every original Q's multiplicity as prod_i n_i(Q) and verifies the inverse-weighted sum equals distinct source Q count exactly. True original W34/GF4 nononto source C and multiplicities lex/random, without inventing high-h fixture.

True original W32 history all seven-class source classifier on 16 separate COMPLETE globally injected original g maps, output historical C/A and C/B fourth Walsh source-local coefficients; compare both against independent exhaustive full original seven_census on ALL 62,370 left sixflag candidates on each of the 16 real global maps. All h1..80 exact BigInt upper arithmetic, invalid original source/overlapping packets/h guards. Classical Walsh/Parseval, original GQ line uniqueness and perfect matchings credited; no claim of general priority.

Root #230 Branch A universal ORIGINAL unchanged f,g S_s>=c s^6 remains UNKNOWN; no true-original infinite correlated o(s^6) family (B), no accepted equivalent reduction (C), no R3/ASET exponent. Spectral UPPER under local CHANGED maps alone cannot control the original center. Future meaningful stage must seek SIGNED cross-order inequalities or compare two-sided original source sums directly, not just descending coefficient orders. Keep research Draft pending exact HEAD specialized/INDEX/Proof Audit/Full Research and independent mathematical referee plus ancestor integration.
