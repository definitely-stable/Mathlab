# HYP-105 / issue #230 — AA4-AT: exact rooted seven-GF5 five-swap damage boundary

**Status:** partial **all-h upper-bound theorem / method limitation** on true original W(3,2^h) and independent finite genuine-source falsifiers. Research Draft, not independent mathematical referee acceptance. Scientific parent [AA4-AS #547](https://github.com/definitely-stable/Mathlab/pull/547); historical exact one-swap locality already established in [D6-AA4-X-CYC #493](https://github.com/definitely-stable/Mathlab/pull/493) and original joint signed-swap interactions in [#497](https://github.com/definitely-stable/Mathlab/pull/497). No main changes, registry promotion, or root #230 A/B/C closure.

## 1. The mathematically unresolved step

Previous [#545](https://github.com/definitely-stable/Mathlab/pull/545) and [#547](https://github.com/definitely-stable/Mathlab/pull/547) give at least one, or >=s^6/4 distinct, D6-positive full globally injected original source-LINE maps g' each within at most five original line-label transpositions of EVERY initial adversarial complete g. However those statements are about **changed** maps. They cannot be silently read as an ORIGINAL all-f,g seven-family lower.

This slice rigorously quantifies the maximum seven-class boundary support and upper change caused by five original source line-label swaps, with **one common complete full global g** at each end and six identical original incidence IDs on both physical sides. It deliberately does not claim a lower bound or favorable sign for these changes.

## 2. Rooted physical 2-factor lemma: exactly 52 versus 130

For a fixed six-element physical coordinate vertex set X, a six-edge unordered **multiset** M of unordered pairs of different coordinates has all SIX physical coordinate vertex degrees exactly TWO iff the connected components of the underlying degree-two multigraph are:

- A: a simple C6 or two disjoint C3, all six edge pairs occur ONCE. There are exactly **70** unrooted such physical edge multisets: 60 connected undirected C6 and 10 3+3 cycles.
- B: one 2-cycle formed by two **parallel occurrences** of one physical edge, plus a simple C4 on the other four vertices. Exactly **45** unrooted multisets: choose the pair of 2-cycle endpoints in 15 ways, and one of three C4s on the remaining four.
- C: three disjoint 2-cycles, each one physical edge occurring TWICE. Exactly **15** unrooted multisets, the 15 perfect matchings on six vertices.

There are exactly **130** such physical multisets. Fix one particular physical pair edge e among the 15 possible K6 edges and count pairs (M, occurrence of e in M), including two separate physical occurrences when M uses e twice. By the symmetry of all 15 physical edges, total edge incidences are 6*(70+45+15)=780, so there are **780/15=52 rooted physical edge occurrences** at e. Per original source left physical profile:
- A: (70*6)/15 = **28**;
- B: (45*6)/15 = **18**;
- C: (15*6)/15 = **6**.

Independent enumeration of all 5005 six-edge multisets of K6 using Python combinations_with_replacement, checking six degree-two coordinates, must reproduce exactly 70/45/15 and 28/18/6. This is a purely combinatorial physical pair-image lemma; the specialized use of the rooted slots for genuine ORIGINAL source incidence capacity is the research-specific contribution. Nothing here is independently claimed novel as abstract graph theory.

## 3. All-h ORIGINAL one-source-line support upper, class-resolved

For every s=2^h>=2, write d=s+1 and a=min{a:binom(a,2)>=(s+1)(s²+1)}. Fix ANY full globally injected original point map f; no assumption on the other complete global original line map g. Let F_t(ell) be the sets of exactly six **distinct original W(3,s) incidence IDs** Q containing at least one true original incidence from an ORIGINAL source LINE factor ell and whose six **left** physically mapped point pair edges under f form a six-coordinate physical 2-regular multigraph of original left profile t=A,B,C. (No original Q is fabricated; the original source incidence graph determines each line neighbor.)

For every genuine original source line ell:
1. Choose which of its exactly d true original neighboring point factors supplies the specified root source incidence (p,ell): at most d choices.
2. The physical pair f(p) is an occupied edge of a fixed injected point map. The other FOUR different physical coordinate symbols of an accepted six-coordinate 2-factor can be chosen in at most binom(a−2,4) ways.
3. On those six physical coordinate symbols there are exactly 28,18,6 rooted 2-factor edge-occurrence templates for A,B,C. These counts include all possible physically repeated original point-factor images, not only connected simple physical sixcycles.
4. Pin the occurrence of f(p) representing the chosen true incidence ID (p,ell), and assign the remaining five physical occurrences to the five other original incidence-column positions in at most 5!=120 orders. Each physical pair image has **at most one original point source-factor preimage** under the same f; every one of these real original point factors has at most d true incident original line factors. Thus at most d^5 remaining actual original incidence choices; invalid original source repetitions and any additional right GF5 constraints only eliminate assignments.

Every genuine Q in F_t(ell) has at least one encoding counted by these choices, so overcount is harmless. Consequently the exact universal class-resolved capacity inequalities are:

\[
\boxed{
|F_A(\ell)|\le3360\,d^6\binom{a-2}{4},
\quad
|F_B(\ell)|\le2160\,d^6\binom{a-2}{4},
\quad
|F_C(\ell)|\le720\,d^6\binom{a-2}{4}.
}
\]

Sum:
\[
\boxed{
|F_A(\ell)\cup F_B(\ell)\cup F_C(\ell)|
\le6240\,d^6\binom{a-2}{4}.
}
\]

These are upper bounds on **actual original six-ID sets**, not counts of synthetic physical templates passed off as source incidence sets. They are uniform in every original point f and in all original GQ source geometry.

## 4. Exactly one global five-swap signed seven-class boundary identity

Take any TWO arbitrary complete globally injected original physical LINE maps g and g' on the same true original LINE factors. Suppose g' is obtained from g by at most five transpositions exchanging physical pair images of exactly two genuine original LINE factor IDs at each step. Let T be the union of all ORIGINAL line IDs touched by those steps, so |T|<=10. The fixed globally injected original f is unchanged throughout.

Let I_k(Q;f,g)∈{0,1} be the accepted positive historical GF(5) indicator for class k among exactly SEVEN disjoint accepted classes, on the SAME six actual original incidence IDs Q. Then for Q whose real source line factor set is disjoint from T, all six g physical right pair images on those original incidence IDs are unchanged. Therefore all accepted class indicators are IDENTICAL before and after. This gives the exact mathematical identity, for each of the seven classes k,

\[
S_k(f,g')-S_k(f,g)=
\sum_{Q:\ L(Q)\cap T\ne\varnothing}
\bigl(I_k(Q;f,g')-I_k(Q;f,g)\bigr).
\]

This exact locality principle, especially for a single swap, is **preexisting** in #493 and #415. The new quantitative statement is a **class-resolved capacity bound** for this support. The A-left classes are D6 and A-left/B-right; B-left classes are B-left/A-right, B/B-overlap and B/B-disjoint; C-left classes are C/A and C/B. Every left profile of a positive seven-class Q belongs to A/B/C and hence the previous rooted bounds apply.

Let S_7=sum of all seven disjoint class counts. Since a Q switches at most one class or none and the change of its combined accepted indicator is in {-1,0,1}, we have for all h>=1, every original full f,g and every such edited g':

\[
\boxed{
|S_7(f,g')-S_7(f,g)|
\le |T|\,6240\,d^6\binom{a-2}{4}
\le 62400\,d^6\binom{a-2}{4}.
}
\]

This is a universally quantified **upper on damage**, NOT a quantitative reverse-transfer lower; its right side is generally huge, even when g' was selected from the repair process and D6(f,g')>=1.

## 5. Exact class-weighted accepted seven-GF5 necessary R3-floor boundary

The immutable historical selected 51-palette necessary R3 lower numerator weights in #230 are:

D6=5643; B-left/A-right=45600; A-left/B-right=45600; C/A=43320; C/B=49050; B/B-overlap=51750; B/B-disjoint=45010.

The MAXIMUM such weight conditional on left physical type is 45600 for A, 51750 for B, and 49050 for C. Since one six-original-incidence Q can be in at most one class at each global map, the absolute change in its selected seven-class weighted floor is at most the left-type maximum.

Combine with the rooted original source line fiber capacities:

\[
\boxed{
|\Delta W_7|\le
|T|\,120\,d^6\binom{a-2}{4}
\bigl(28\cdot45600+18\cdot51750+6\cdot49050\bigr)
=
|T|\,300312000\,d^6\binom{a-2}{4}.
}
\]

The numerator W_7 is the **previously accepted seven-class GF5 necessary lower numerator**, NOT the exact full R3 numerator and NOT the GF5 R3 total. Its change can have either sign, so no lower is implied.

## 6. Explicit asymptotic scale of the obstruction

For s>=4, the minimal true symplectic alphabet satisfies a²<=4s³. Elementary proof: V=s³+s²+s+1<= (85/64)s³ for s>=4, so the minimal integer a with K_a>=V obeys a<sqrt(2V)+2 <= sqrt(85/32)s^(3/2)+2 <2s^(3/2), using s^(3/2)>=8 and sqrt(85/32)<7/4. Also d=s+1<=5s/4. Hence

\[
62400\,d^6\binom{a-2}{4}
\le62400(5s/4)^6(2s^{3/2})^4/24
=\frac{5078125}{32}\,s^{12}
<160000\,s^{12}.
\]

The **universal five-swap net seven-family change upper** is therefore O(s^12), six powers of s above the target original universal Ω(s^6). The fact that *an upper bound is loose* does not refute the conjectured lower bound; it proves only that this **particular absolute-value/triangle-inequality reverse-transfer approach cannot establish it by comparing scales alone**, absent substantial new cancellation, sign, overlap, or source-Hall constraints. The preceding repaired Q guarantees D6(f,g')>=1, and even the many repaired-map abundance from #547 supplies no control of seven-family signs at g.

The s2 finite and all higher dyadic orders also have the exact integer bound 62400*d^6*binom(a-2,4), with no attempted all-h s>=4 inequality extrapolation to s2.

## 7. Reproducible independent finite ORIGINAL seven-GF5 controls

Source program research/hyp105_issue230_d6aa4at_seven_swap_boundary.py and tests research/test_hyp105_issue230_d6aa4at_seven_swap_boundary.py provide:

- Two independent rooted K6 2-regular multigraph enumerators across **all 5005 six-edge multisets**, with EVERY of the 15 possible fixed edges independently checked to have 28 A,18 B,6 C rooted edge occurrences. Counts are proof controls, not assumed.
- Exact rational/integer all true dyadic orders h1..34,40,64,80, for the 6240 and 300312000 class-resolved GF5-floor constants; h>=2 also checks universal 160000*s^12 explicitly without fake high-h geometry.
- Actual genuine original W32 full global S68/S72 source cases: enumerate the **62,370 true six-DISTINCT-original-incidence-ID left 2-regular physical candidates** independently of the repair source, measure the true per-original-line A/B/C support, and compare to the rooted theorem.
- For each fixed globally coherent W32 S68, S72, lex and reverse pair, construct the PR #545 actual five-or-fewer full global original LINE source-factor swap chain, record its set T of original line IDs, score every one of the 62,370 genuine original candidate Q directly at the starting g and final g'. Independently telescope every signed class delta by rescoring **only** real Q containing one of the two actual original LINE factor IDs swapped at that step, compare the seven-class vector and selected 51-palette GF5 floor weighted numerator. Further independently verify both endpoints with the existing historic full W32 seven_census oracle.
- Exact distinction between accepted Q first appearing, last disappearing, or changing its accepted class tag, preserving all original source incidence IDs, and explicit validation that Q outside the ORIGINAL T cut cannot change tag even when source line factors repeat.

**Limits:** The historical K6 seven-class scorer assumes six physical coordinate indices in one internal half classifier and is used ONLY for true W32/K6; no false claim of full seven-class W34/K14 or high-h census. Large dyadic h are exact integer formula checks rather than fabricated original GQ geometries. Passing hosted CI is not a mathematical referee verdict.

## 8. Prior-art and next genuine proof obligation

The tagged local-support derivative itself is credited to previous #415/#493/#497 and elementary finite differences. The physical 130 two-factors / 52 rooted occurrences follow from standard degree-two graph decompositions and are not claimed as a novel general combinatorial result. The specialized exact 28/18/6 true-original source-line support bound, seven-class weighted GF5 numeral, and empirical explicit finite signed five-swap transfer are new **within the inspected research stack** only; no independent publication/prior-art novelty audit has been completed.

**Next mathematical direction:** Seek a signed compensation inequality at the level of true original source incidence sixsets, or a seven-GF5 rank/moment/cycle closure certificate, so the loss of many repaired D6 witnesses under an adversarial original g forces enough OTHER positive classes **on that original SAME f,g**. A purely unsigned boundary capacity is too weak. Earlier genuine W32 global-swap experiments demonstrate mixed derivative signs; monotonicity cannot be assumed. Keep root #230 Branch A/B/C open, scientific Draft unmerged and independent mathematical referee gate separate.
