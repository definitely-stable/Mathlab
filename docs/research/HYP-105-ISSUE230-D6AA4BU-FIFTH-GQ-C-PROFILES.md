# HYP-105 / #230 — AA4-BU: fifth-order source-GQ C/A and C/B bounds

**Scientific Draft**, strict child of [AA4-BT #591](https://github.com/definitely-stable/Mathlab/pull/591), pinned parent HEAD a7d18b7f907878035b1dc9799deac602130f613b. Keep the true symplectic W(3,2^h), h≥1, six DIFFERENT ORIGINAL incidence IDs, arbitrary correlated fixed complete globally injected typed physical f,g, seven historical GF(5) classes, and global source LINE-factor-image transposition cubes. Root issue #230 remains OPEN_WITH_FORMAL_BLOCKER.

## Previous research and missing lemma

AA4-BS #590 already proved exact source-local seven-class Walsh covariance, the support restriction of a six-flag acceptance indicator, and the general packet cap. AA4-BT #591 already proved a genuine GQ sixth-order filter and the absolute sixth-order source C/A sixflag bound 960, yielding Walsh coefficient cap 480. The fifth Walsh order is DIFFERENT: a sixflag Q touching five disjoint two-LINE-factor packets has FIVE required anchored original incidence flags but may have a sixth flag on a source LINE factor OUTSIDE those five packets. Ignoring that possibility yields an invalid uniform C/A fifth-order claim. GQ original line uniqueness and Walsh basics are classical, not discoveries of this PR.

Let d=s+1, V=(s+1)(s²+1), and five pairwise DISJOINT pairs of real original LINE factors P_i={u_i,v_i}. Their genuine source incidence packet B_i contains 2d different original incidence IDs. Define a Boolean cube by swapping the WHOLE physical LINE pair-edge images g(u_i),g(v_i) in any subset of the five packets; f, source incidence IDs, right occupied image edge support remain unchanged for all 32 cube vertices. For each historical class c, define the exact fully fixed-map fifth coefficient

\[
\widehat S_c([5])=2^{-5}\sum_{A\subseteq[5]}(-1)^{|A|}\,S_c(f,g^A).
\]

Every original sixflag Q contributing to this coefficient must touch EACH packet B_i, since a missing packet's global image swap acts trivially on the SAME Q. This is prior source-locality from #590.

## BU-CA: true original POINT C / LINE A ≤480d(d−1) Q

A source-C Q has exactly THREE pairs of same true original POINT factors, each selected original point factor repeated twice. Select one authentic incidence from each of the five packets hit by Q, leaving one extra incidence. Exactly TWO of the three equal-point pairs remain entirely among the five anchored flags and ONE anchored flag becomes a singleton. Choose singleton packet (5 possibilities), perfect pairing of the other four packet slots (3 ways), and one of the two source LINE factor IDs per packet (2^5=32 ways). The true GQ property that two distinct source LINE factors meet in AT MOST one source POINT determines both complete anchored equal-point pairs uniquely, if they are possible. Choose one of d true source points on the singleton line and another actual line through it DISTINCT from the selected singleton line (at most d−1), to supply the sixth actual incidence. Further original source distinctions, POINT C requiring three different repeated true POINTs, LINE A requiring six different true LINEs, and six-coordinate physical acceptance only reduce the count.

\[
\boxed{N_{5,C/A}\le 5\cdot3\cdot2^5d(d-1)=480d(d-1).}
\]

For any nonconstant {0,1} acceptance indicator on a five-swap cube, the magnitude of its fifth Walsh coefficient is at most 1/2. Therefore for EVERY correlated full f,g and every five genuine LINE-factor swap packets,

\[
\boxed{|\widehat S_{C/A}([5])|\le240d(d-1).}
\]

NO source independence, arbitrary random sixth flag, fake high-order GQ model or source-line selection without incidence is used.

## BU-CB: exact source intersection enumerator and UNIFORM bound 960

For a source C/B Q, the source POINT profile is (2,2,2) and the LINE profile is (2,1,1,1,1): there are five DIFFERENT true LINE factor IDs across six original incidences. Since all FIVE disjoint LINE-factor packets must be hit, each packet supplies exactly ONE distinct source LINE factor. The sixth incidence therefore lies on the SAME one repeated true original LINE factor already used by one packet, at a SECOND different genuine original POINT. A sixth flag on an outside LINE factor would instead force all six LINE factors distinct (source type A) and cannot be C/B.

Choose its doubled packet r (5 options), its repeated original line among the two in that packet (2), which UNORDERED two of the other four packet indices supply original lines intersecting that doubled line at the two selected distinct POINTs (6), and one actual LINE source ID from each of the four remaining packets (2^4=16). The remaining two packet lines must intersect each other at a THIRD source POINT. Every original POINT is uniquely determined, if it exists, by the intersection of two genuine distinct W3 source LINES; any triple with repeated POINTs or sixflag incidence duplication is rejected. The number of true source Q is therefore bounded **independently of s**:

\[
\boxed{N_{5,C/B}\le5\cdot2\cdot6\cdot16=960,\qquad
|\widehat S_{C/B}([5])|\le480.}
\]

The source enumerator in the accompanying Python module is EXACT, not just an upper bound: it constructs the repeated line, the three distinct original source intersections, and the six canonical sorted actual incidence IDs Q. The repeated original LINE ID is UNIQUE and choosing its two partners as an UNORDERED pair counts every Q once.

Let H_CB(f;P) be the subset of the enumerated real C/B Q for which the three doubled true original POINT factors have physical pair-edge images f(p) with pairwise disjoint endpoints. This is the necessary left physical C-profile condition and is independent of which of the 32 complete globally swapped right image maps is used. Then the sharper original fixed-map fifth coefficient bound is

\[
|\widehat S_{C/B}([5])|\le H_{CB}(f;P)/2\le480.
\]

The fifth order still permits other historical positive classes: NO unsupported fifth-order total class annihilation is claimed. The selected GF5 necessary R3-floor positive weights 43320 (C/A) and 49050 (C/B) give

\[
|43320\widehat S_{C/A}+49050\widehat S_{C/B}|
\le43320\cdot240d(d-1)+49050\cdot480.
\]

This is a source-GQ SENSITIVITY upper, **NOT** an unchanged-center S lower.

## Independent validation

The additive three-job GH-hosted workflow runs six independent groups:

1. Exact all dyadic h1..36,40/48/64/80 integer and Fraction C/A and C/B source capacity certificates; no fabricated high-h genuine W3 graph.
2. True original W32 symplectic complete K6 lex and S72: separate Cartesian product of one REAL original incidence from each of FIVE actual 2-LINE packets plus ANY SIXTH real source incidence ID from the entire original W32 source (approximately 350,000 raw selections). Independently compare exact C/B sixflag sets with the alternative line-intersection-based source GQ enumerator, and C/A source counts with 480d(d−1). Physical f-point C disjointness checked literally.
3. True original W34 symplectic GF4 nononto K14 lex/random: independently validate original source profiles of every GQ-intersection-constructed C/B Q, unique repeated actual LINE factor and all distinct original source incidence IDs.
4. True original W32 all 32 different globally injected complete LINE maps under five whole actual LINE factor swaps. Classify the SAME selected original physical-left six-Q at every cube vertex with the historical all-seven GF5 classifier; verify C/A and C/B fifth Walsh coefficients against source caps and left physical intersection filter.
5. SECOND historical oracle: for lex, enumerate ALL 62,370 historically physical-left-eligible six-original-ID Q at ALL 32 full global right-map vertices, WITHOUT prefiltering for packet hits, and compare each of seven class fifth Walsh signed numerators with the packet-sensitive source-only calculation.
6. Invalid/overlapping original LINE factor packets, broken source factor geometry or typed physical injection, wrong h and finite-only W32 scope fail closed.

## Scope and acceptance

The sixflag source class structure and true GQ LINE uniqueness are independent of physical map correlations. But high-order Walsh coefficient magnitudes do not force positivity of original S_seven(f,g) at the unchanged arbitrary original center, any all-h GQ counterfamily with o(s^6) seven counts, or Branch A/B/C of issue #230; they also imply no complete R3/ASET exponent. This is a scoped proof-method refinement, not claimed globally novel prior art. Keep scientific Draft pending exact final SHA specialist CI, INDEX, Proof Audit, Full Research, genuine independent mathematical referee and accepted parent research chain. Do not merge or promote canonical results based on CI PASS alone.
