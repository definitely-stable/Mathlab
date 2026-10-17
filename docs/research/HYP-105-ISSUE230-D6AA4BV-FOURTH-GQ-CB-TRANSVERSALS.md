# HYP-105 / issue #230 — AA4-BV: fourth-order genuine GQ C/B transversals and an O(s²) source cap

**Scientific Draft strict child of [AA4-BU #593](https://github.com/definitely-stable/Mathlab/pull/593)**, pinned exact parent HEAD b27293fa02506f2196b50f6639e8660ba1285732. Separate parallel [AA4-BU #592](https://github.com/definitely-stable/Mathlab/pull/592) already fixes the important fifth-order EXTERIOR-flag error; its corrected all-h fifth-order spectrum must not be misrepresented. New here is the FOURTH-order genuine original point-C/line-B source bound and explicit source-GQ fourth packet intersection oracle, not generic source-local Fourier analysis. No main or accepted registry edit; issue #230 OPEN_WITH_FORMAL_BLOCKER.

## Mathematical scope

Let s=2^h (h≥1), d=s+1, and let W(3,s) be the AUTHENTIC original symplectic generalized quadrangle with V=(s+1)(s²+1) genuine original POINT factors and V genuine original LINE factors, and exactly d real original incidence flag IDs per line. Fix ANY fully globally injected correlated original POINT map f and LINE map g from those source factors to separately typed physically occupied unordered pair edges of minimal K_a. They can depend adversarially on the original source geometry and on each other.

Choose FOUR PAIRWISE DISJOINT pairs of genuine original LINE source-factor IDs P_i={u_i,v_i}, i=1,...,4. Swapping the WHOLE original source-factor physical pair-edge images g(u_i),g(v_i) on arbitrary subsets of those pairs generates 16 genuine complete globally injected original right physical maps on the SAME original occupied physical edge support, with the SAME original incidence IDs and same f. For each one of seven historical GF5 classes c, the fourth Walsh coefficient is

\[
\widehat S_c([4])=2^{-4}\sum_{A\subseteq[4]}(-1)^{|A|}S_c(f,g^A).
\]

Source-locality from [#590](https://github.com/definitely-stable/Mathlab/pull/590) says that a genuine six DISTINCT-original-incidence-ID set Q can contribute to this coefficient ONLY if its actual ORIGINAL LINE factor set intersects ALL four LINE-source swap packets.

We study the historical positive class **C/B**: source POINT factor multiplicities C=(2,2,2), three distinct genuine POINT factors each repeated twice, and source LINE multiplicities B=(2,1,1,1,1), five distinct genuine LINE factors with exactly one LINE factor repeated. Every candidate Q contains six DIFFERENT actual ORIGINAL incidence flag IDs and its SIX physical coordinates are checked with the SAME source Q on both sides.

## Classical GQ transversal lemma (explicitly credited)

The generalized quadrangle axioms say two different authentic source LINE factors meet in at most ONE genuine original POINT, every line contains exactly d original POINT factors, every point lies on exactly d original LINE factors, no three distinct lines meet pairwise in three different points, and for each point P not on a line L there exists a UNIQUE original line through P meeting L. See [finite GQ axioms](https://link.springer.com/article/10.1007/s10623-018-00591-9) and [GQ incidence properties](https://people.math.sc.edu/laszlo/FPP.pdf). For any two distinct authentic original LINEs A,B there are at most d OTHER genuine original LINEs L meeting both A and B:

- If A,B intersect at P, a third line L meeting both at distinct P_A,P_B would create a forbidden original three-line triangle. Thus L must pass through P, and there are exactly d−2 such other lines.
- If A,B are disjoint, each of d genuine original points P∈A has exactly one original POINT Q∈B collinear with P and hence exactly one ORIGINAL line PQ meeting both A,B. The d constructed lines are different because a line meeting A at two points equals A. Therefore exactly d transversals.

This is a STANDARD GQ consequence, not a newly discovered theorem. The specific new application below is to constrain true-original SIX-incidence C/B fourth-order source packets.

## New fourth-order C/B theorem and fully explicit proof

Because Q has FIVE distinct source LINE IDs and hits all FOUR disjoint packets, its fifth distinct source LINE factor must be either **inside** one of those four packets (the previously unselected factor in that packet) or **exterior** to all eight packet LINE IDs. These cases are disjoint and exhaustive.

### BV-IN — all five source LINE factors belong to the four packets

Choose which packet contributes BOTH of its source LINE IDs (4 choices). Choose one of the two source LINEs from each of the other three packets (2³ choices). These choices yield exactly 4·2³=32 distinct five-original-LINE-ID sets. For each, choose its UNIQUE repeated original LINE factor L (5 choices), then choose which UNORDERED two of its four other LINE factors are the partners intersecting L at two different source POINTs (binom(4,2)=6). The remaining two source LINEs must intersect at the third genuine source POINT. All three distinct intersection points are now forced uniquely if they exist, because two genuine original LINEs meet at at most one point. Thus at most

\[
\boxed{N_{\rm in}\le4\cdot2^3\cdot5\cdot6=\mathbf{960}.}
\]

The generator first canonicalizes each FIVE-ORIGINAL-LINE-factor set to prevent double counting: when two original LINEs belong to the same packet, choosing either as that packet's first anchor is NOT two distinct Q.

### BV-OUT-R — the EXTERIOR fifth original LINE factor is the repeated source LINE

Choose one of two genuine original LINE IDs from each of the four packets: 2^4=16 sets. Choose the TWO of four selected packet original LINEs whose real intersection points with the exterior repeated LINE L are its two selected distinct source POINTs: binom(4,2)=6 choices. The other two anchored original LINEs must meet at the third source POINT, fixed uniquely if it exists. The exterior genuine LINE L must meet BOTH selected distinct packet LINEs at different actual source POINTs. By the *GQ transversal lemma*, for these TWO genuine packet LINEs there are at most d candidate L, whatever the given original W3 incidence geometry. Thus

\[
\boxed{N_{\rm outside,\ repeated}\le2^4\binom42 d=\mathbf{96d}.}
\]

An upper d, rather than the naive d² independent point-pair count, is where authentic GQ no-triangle + unique off-line projection makes a quantitative difference.

### BV-OUT-S — the EXTERIOR fifth original LINE factor is a SINGLETON

Again choose four genuine LINE IDs, one in each packet (2^4 choices), and choose which of those four becomes the repeated source LINE L (4 choices). Of the four other source LINE factors (three anchored, one exterior X), select the TWO which meet L at the distinct two true POINTs underlying L's repeated incidences. There are exactly two structural subcases:

1. **Exterior X is one of L's two partners:** choose which of the three remaining anchored lines is L's OTHER partner (3 choices). Its intersection P with L is fixed if it exists. The exterior X must meet L at a SECOND true source POINT Q≠P: at most d−1 choices Q∈L, each allowing at most d−1 other original LINEs X≠L through Q. Thus ≤(d−1)² possible X. The other two anchored packet lines must intersect at the third original point (forced, or none).
2. **Exterior X is NOT one of L's partners:** choose which TWO of the three anchored packet lines meet L (binom(3,2)=3 choices), at two distinct source points P,Q forced by source incidences. The remaining anchored line C must meet X at the third distinct actual source point R: choose R among at most d real points on C and one of d−1 other source LINEs through R, giving ≤d(d−1) choices X. Reject any cases where the third R equals P or Q or X is not exterior.

Hence

\[
\boxed{
N_{\rm outside,\ singleton}
\le2^4\cdot4\,[3(d-1)^2+3d(d-1)]
=\mathbf{192(2d-1)(d-1)}.
}
\]

### BV-MAIN — all-h fourth-order C/B spectral capacity

Summing the disjoint source cases gives **for EVERY genuine original W(3,2^h) and EVERY fully fixed possibly correlated f,g**:

\[
\boxed{
N_{4,C/B}\le
960+96d+192(2d-1)(d-1)
=O(d^2)=O(s^2).
}
\tag{BV-CB}
\]

Any real original historical C/B accepted sixflag on the 16 globally injected cube maps is drawn from this fixed list of at most N source Q. A Boolean accepted Q can contribute to nonzero fourth Walsh coefficient with magnitude at most 1/2. Hence

\[
\boxed{
|\widehat S_{C/B}([4])|
\le\frac{960+96d+192(2d-1)(d-1)}2.
}
\tag{BV-W}
\]

A sharper true-original map-dependent refinement uses **the unchanged f**: let H_CB(f;P_1,...,P_4) be the number among those source Q whose three repeated ORIGINAL source POINT images f(p) are PAIRWISE DISJOINT PHYSICAL PAIR EDGES, so the original LEFT C projection is already physical 2regular on six coordinates. The entire C/B class fourth Walsh coefficient obeys

\[
|\widehat S_{C/B}([4])|
\le H_{CB}(f;P_1,\ldots,P_4)/2
\le N_{4,C/B}/2.
\]

Both historic original RIGHT B source profile and physical acceptance can only remove those Q, and the physical LINE map g can be arbitrarily correlated with f. For issue #230's selected GF5 necessary 51-column weights, the class C/B fourth Walsh weighted absolute contribution is bounded by 49050 times the expression BV-W. This is a SENSITIVITY UPPER, NOT a positive accepted fixed-center S_s(f,g) lower.

### Complete fourth→fifth→sixth genuine-source C/B hierarchy

From the immediate parent [#593](https://github.com/definitely-stable/Mathlab/pull/593) at fifth order, N_5,C/B≤960 and |hat S_C/B([5])|≤480. From [#591](https://github.com/definitely-stable/Mathlab/pull/591) at SIXTH order, right source B is IMPOSSIBLE for six disjoint LINE swap packets: |hat S_C/B([6])|=0. Therefore

\[
\boxed{
\begin{array}{c|ccc}
\text{true original LINE swap order }t&4&5&6\\
\hline
\text{source C/B sixflag upper }N_t&
960+96d+192(2d-1)(d-1)&960&0
\end{array}
}
\]

This is a quantified genuine W3 incidence-restricted high-order source localization hierarchy. Its global mathematical novelty beyond this exact HYP-105 scope and classical GQ/transversal/fourier techniques is NOT established by repository CI or a peer-reviewed prior-art study.

## Independent proof falsifiers

1. **All dyadic h1..36 and h40/48/64/80:** exact integer and Fraction original GQ t4 source case caps and fourth Walsh half-cap, no synthetic high-h original W3 fixture, reject non-dyadic/invalid source inputs.
2. **TRUE original W32 symplectic full K6 lex and S72:** A completely separate Cartesian original source-ID oracle chooses one genuine incidence flag from EACH four disjoint 2-LINE source packets and two ANY OTHER original incidence flags, classifies true-original POINT C and LINE B multiplicities and compares the EXACT distinct six-ID Q set to the independent line-intersection generator (which canonicalizes five-LINE sets first). The W32 brute source oracle visits (2d)^4·binom(M−4,2)=6^4·binom(41,2)=1,062,720 paths per labeling, including INSIDE/OUTSIDE cases without assuming source GQ line geometry. Independent literal f-point pair-edge C eligibility is compared.
3. **REAL original W32 and symplectic W34 GF4 nononto K14 lex/random:** count the ACTUAL number of original other LINEs meeting each sampled pair of original LINE factors and confirm d−2 if pair meets, d if disjoint. In particular, this tests the GQ projection/transversal lemma and its nontrivial distinction from merely at-most-one-point intersection.
4. **TRUE original W34 nononto K14 full globally injected typed f,g lex/random:** re-enumerate the authentic original C/B six-flag sets via original LINE intersections and independently verify every Q has six distinct source incidence IDs, original POINT C and original LINE B source factor multiplicities, packet coverage and exact source-case cap. No false all-h large model simulation.
5. **Historical full original W32 seven-GF5 on 16 COMPLETE globally injected physical LINE-image maps, lex/S72:** classify the SAME original six-ID Q across all map states, check packet-hitting source filter, immutable GF5 original historical source type and C/B fourth absolute bound refined by the unchanged original f. Independent complete 62,370 left physical original sixflag Q ×16 right fully injected global map historical census (lex) gives ALL SEVEN exact fourth Walsh numerators and matches packet-filtered original source counting. No locally redrawn Q or f/g independent resampling.
6. Reject overlapping source swap packets, malformed original incidence IDs, bad typed physical source image injection, fake W34-as-W32 historical program input.

**Gate:** Keep independent research Draft until exact final HEAD specialist hosted CI, INDEX, Proof Audit, Full Research, independent mathematical referee and accepted parent ancestry. No main merge or accepted HYP-105 Branch A/B/C status promotion. This is NOT a true infinite correlated W3 counterfamily with o(s^6) selected GF5, not root C model-equivalent reduction, and not full R3/ASET strict bound.

## Prior literature

The original generalized quadrangle axioms, line intersections, no triangles and off-line unique projection are classical, see [generalized quadrangles and unique projection](https://link.springer.com/article/10.1007/s10623-018-00591-9) and [an incidence-geometry account of finite GQ](https://people.math.sc.edu/laszlo/FPP.pdf). The only scoped claim here is their explicit fourth-Walsh HYP-105 historical C/B use. No claim of originating GQ transversal counting or Walsh analysis.
