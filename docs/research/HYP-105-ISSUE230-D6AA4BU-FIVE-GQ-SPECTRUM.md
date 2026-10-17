# HYP-105 / #230 AA4-BU — corrected fifth-order genuine-original GQ spectrum

**Scientific Draft, strict child of [AA4-BT #591](https://github.com/definitely-stable/Mathlab/pull/591), frozen parent SHA a7d18b7f907878035b1dc9799deac602130f613b.** No main or accepted registry edits; issue #230 remains OPEN_WITH_FORMAL_BLOCKER. Full seven original GF5 taxonomy and disjoint-source-transposition Walsh locality are reused from ancestors #476, #587, #590 and #591. Classical GQ axiom: any two genuine original LINES meet at most ONE actual POINT, and each LINE has exactly d=s+1 incident POINTs: [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Quadrangle). No original priority for elementary inclusion/exclusion, perfect matchings or Walsh algebra is claimed.

## Correction demanded by independent hosted CI

The FIRST AA4-BU draft erroneously assumed the sixth incidence of a true-original six-Q touching ALL FIVE chosen LINE-factor source packets must belong to the selected TEN original LINE factors. This is **FALSE**: exactly one flag may come from OUTSIDE ALL FIVE packets, while exactly one flag is chosen from EACH of the five packet incidence-ID fibers. The original incorrect fifth-order H5 formula and the incorrectly claimed **uniform in s** C/A fifth Walsh bound are REJECTED. A hosted all-h exact-count test detected this issue. This document and the amended production-research module preserve BOTH genuine-original cases and independent W32 full source enumeration.

## Exact all-h fifth source LINE-profile count: INSIDE versus OUTSIDE

Fix any TRUE symplectic original W(3,s), dyadic s>=2, and EVERY complete globally injected, arbitrarily correlated typed pair-image f,g. Choose FIVE pairwise disjoint original LINE-factor image swap pairs. Put d=s+1, V=(s+1)(s²+1), M=Vd actual ORIGINAL incidence IDs. Each of the five source two-LINE packets contains exactly 2d genuine original flags. Each Q potentially sensitive to ALL five swaps has SIX DISTINCT ACTUAL ORIGINAL incidence IDs, at least one from EACH packet. There are TWO and ONLY TWO cases:

**I. INSIDE (2,1,1,1,1)**: all six Q flags belong to the selected ten original LINE factors; exactly one of five packets supplies TWO flags and the other four supply ONE. The number is

H5_in = 5*C(2d,2)*(2d)^4.

Exactly H5_in,B = 10*C(d,2)*(2d)^4 have right ORIGINAL LINE source multiplicity B (both doubled flags lie on SAME one of packet's two LINE IDs); exactly H5_in,A=5*d²*(2d)^4 have source-right A (doubled flags lie on two DIFFERENT packet LINE factors).

**II. OUTSIDE (1,1,1,1,1;1)**: all five selected LINE packets supply one flag, and the sixth flag belongs to one of the remaining V−10 ORIGINAL LINE factor source IDs. There are M−10d=d(V−10) external genuine flags; therefore

H5_out=(M−10d)*(2d)^5.

Every such Q has right ORIGINAL source multiplicity A, since each selected packet source LINE ID is distinct and the external LINE ID is outside all ten. The complete and exact all-h source identities are

\[
\boxed{H_5=5\binom{2d}{2}(2d)^4+(M-10d)(2d)^5
=\sum_{j=0}^5(-1)^j\binom5j\binom{M-2dj}{6}.}
\]
\[
\boxed{H_{5,\mathrm{RIGHT}\,B}=10\binom d2(2d)^4,\qquad
H_{5,\mathrm{RIGHT}\,A}=5d^2(2d)^4+(M-10d)(2d)^5.}
\]

RIGHT source C is still IMPOSSIBLE, because Q necessarily uses at least five different actual ORIGINAL LINE source IDs.

## Correct all-h POINT-source C bounds using genuine W3 incidence line intersections

If six original source Q flags have left/source POINT multiplicity C=(2,2,2), their six ORIGINAL incidence IDs uniquely split into three pairs, each pair at the SAME true original POINT factor. For any pair of original LINE source two-factor packets, there are at most 2*2=4 possible distinct LINE/LINE meets since two original W3 lines meet at most once. Even within ONE doubled packet, two distinct original flags at the same POINT require two distinct packet lines; at most two ORDERED choices are possible, so the uniform four-choice cap remains sound.

**INSIDE**: choose the doubled packet (5 ways), choose one of 15 perfect matchings on the six packet slots, and for each of the three original repeated POINT pairs select at most four genuine LINE/LINE incidence intersections:

\[
\boxed{N_{5,C}^{in}\le 5\cdot15\cdot4^3=4800.}
\]

**OUTSIDE**: the six slots comprise five selected packet flags plus one flag from an actual original LINE ID OUTSIDE all ten selected factors. The outside flag must be in exactly ONE of the three repeated-POINT pairs. Choose which of five selected slots pairs with it (5 choices), pair the remaining four selected packet positions (3 matchings), choose each of their two source packet-packet common original POINTs in at most four ways each. Finally choose one actual flag from the selected packet partner (at most 2d genuine source incidences); for its point choose a true original incident LINE factor outside all ten selected LINE factors (at most d). Thus

\[
\boxed{N_{5,C}^{out}\le 5\cdot3\cdot4^2\cdot(2d)\cdot d=480d^2.}
\]

The complete true-original source C source-sixset cardinal is therefore <=4800+480d². An unchanged given globally injected original physical POINT map f filters to a potentially much smaller SOURCE POINT C support requiring the three distinct repeated original point factors' physical pair-edge images to be pairwise DISJOINT. The research module builds those genuine original C INSIDE and OUTSIDE sets separately via respectively 75 and 15 perfect-source-packet-matching GQ incidence constructions. For real W32 the exact sets are independently checked by full 97,200 INSIDE + (M−10d)(2d)^5 OUTSIDE genuine source sixflag Cartesian-product enumeration, not by the SAME algorithm.

Critically, a **right source B** can occur ONLY in INSIDE, because OUTSIDE contributes a sixth distinct original LINE factor. Thus original historical source C/B fifth Walsh remains uniformly bounded, but C/A need not:

\[
\boxed{|\widehat S_{C/B}(T)|\le2400,\qquad
|\widehat S_{C/A}(T)|\le 2400+240(s+1)^2,\quad |T|=5.}
\]

These bounds apply to arbitrary fully fixed correlated original (f,g). A **uniform O(1) C/A bound at fifth order is not proved** and was retracted.

## Fifth-order original POINT B and all-seven historical GF5 coefficient caps

Every genuine original POINT-B sixflag has ONE repeated-point pair among its six original source flags.

In INSIDE, select the doubled packet (5 ways), which slot-pair repeats a point (15), up to four original line intersection flag-pairs, and at most (2d)^4 other actual original flags. Hence B_inside≤min(H5_in,300*(2d)^4).

In OUTSIDE there are two mutually exclusive choices for the unique original repeated-POINT pair:
(a) both flags are in two of five selected packet positions: C(5,2)=10 pairs, each <=4 original line intersections, three other selected packet flags each <=2d, and arbitrary remaining outside flag <=M−10d. Upper 40*(2d)^3*(M−10d).
(b) outside flag repeats the original POINT of one of the five selected packet flags: five choices; <=2d choices for the selected packet incidence, <=d outside-line incidences through that true original point, and four other packet flags <=(2d)^4. Upper 10*d²*(2d)^4.
Thus B_out≤min(H5_out, 40*(2d)^3*(M−10d)+10*d²*(2d)^4).

Put U_B=B_inside+B_out and U_C=min(H5_in,4800)+min(H5_out,480d²). For nonempty Walsh T a true-original six-Q Boolean historical GF5 acceptance indicator has coefficient magnitude ≤1/2. The classwise valid upper bounds are:

- D6 ≤H5_A/2.
- B-left/A-right ≤min(H5_A,U_B)/2.
- C/A ≤min(H5_A,U_C)/2.
- A-left/B-right ≤H5_B/2.
- C/B ≤min(H5_B,B_inside? No: source-C INSIDE capacity min(H5_in,4800))/2.
- B/B-overlap and B/B-disjoint ≤min(H5_B,B_inside)/2.

The C/B bound is explicitly source-C INSIDE. Any use of whole U_B instead of B_inside for right-source-B classes is safe but weaker. We only compute **selected necessary** seven-GF5 R3 LOWER NUMERATOR Walsh bounds with these coefficients, not the full R3, original center absolute risk or entire ASET exponent.

## Authentic finite falsifiers and limitations

Three GitHub-hosted groups: exact all-h dyadic h1..80 source decomposition cross-checked against the earlier #591 exact inclusion/exclusion formula; genuine original W32/K6 with INDEPENDENT source product complete INSIDE/OUTSIDE enumeration and separate true GQ original LINE point-intersection C-source matchings; real original W34/GF4 nononto geometric matchings; historical all-seven original same-six-ID GF5 classification under 32 coherent complete globally injected g^x maps versus independent complete historical seven_census for EACH entire original map. Negative invalid flag/packet cases. No invented high-h W3 source fixture.

This is scoped fifth-order GQ source-incidence spectral progress. It **does not** prove a positive historical seven-motif lower for arbitrary UNCHANGED original f,g, nor an infinite genuine correlated W3 counterfamily or root #230 A/B/C, nor new R3/ASET exponent. Signed covariance and original-center positivity remain open; next candidate fourth-order source LINE packet intersection sieve must preserve the OUTSIDE cases. Keep Draft for independent mathematical referee and exact final-HEAD CI plus parent chain. Root #230 OPEN_WITH_FORMAL_BLOCKER.
