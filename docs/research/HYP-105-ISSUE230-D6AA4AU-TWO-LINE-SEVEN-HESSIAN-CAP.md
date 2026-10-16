# HYP-105 / issue #230 — AA4-AU: true-original two-LINE-source overlap capacity and signed seven-GF5 mixed curvature

**Research-only partial theorem.** Strict scientific child of [AA4-AT PR #549](https://github.com/definitely-stable/Mathlab/pull/549). The ORIGINAL genuine W(3,2^h) symplectic incidence factor IDs, six DISTINCT ORIGINAL incidence flag IDs, the same fixed source Q on both typed physical sides, full global injective f/g, all seven historical positive GF(5) classes, and cross-map dependence are preserved. No merger/main edits or promotion into accepted RCP research claims. Issue #230 Branch A/B/C remains OPEN_WITH_FORMAL_BLOCKER.

## 1. Mathematical next obstacle and prior-art boundary

PR #549 derived a signed class-resolved boundary for at most FIVE globally legal original LINE label transpositions with source-factor support T at most ten: a universal O(s^12) upper on the seven-class absolute delta, far too loose for the target uniform Omega(s^6). The exact mixed finite-difference / transposition Hessian SOURCE-INTERSECTION IDENTITY is **already known** and credited to [D6-R PR #417](https://github.com/definitely-stable/Mathlab/pull/417) and subsequent [#497](https://github.com/definitely-stable/Mathlab/pull/497). Those identities do not supply an explicit, useful all-h capacity of the original six-Q source support when TWO different genuine original LINE factors must both be present.

NEW here: a rigorous **two-source-line mixed incidence** capacity and explicit O(s^11) bound for the absolute signed ALL SEVEN class mixed Hessian, one order better than #549's O(s^12) full support cap. The heart is TWO fixed physical edges in a six-edge degree-two multigraph and the fact that TWO different source LINE factors of a true generalized quadrangle share at most ONE ORIGINAL POINT factor.

No claim of genuinely new abstract graph enumeration, Hall theorem, or independent scientific referee acceptance.

## 2. Exact doubly pinned physical 2-regular multigraph counts

A six-edge physical unordered-pair MULTISET on six distinct coordinate symbols, each coordinate with physical degree exactly two, is A (simple C6 or two C3), B (one parallel edge used twice plus C4), or C (three edges each used twice). The total previously counted in #549 is 70 A / 45 B / 15 C, 130 distinct six-edge multisets on K6. For two fixed physically possible source flag slots their physical image edges can be:

* SAME physical pair image e=(0,1), with **two occurrences required**. Exactly 3 B templates and 3 C templates, total **6**.
* DISTINCT ADJACENT physical edges e=(0,1), f=(0,2), each occurring at least once. Exactly 7 A and 3 B templates, total **10**.
* DISTINCT DISJOINT physical edges e=(0,1), f=(2,3), each occurring at least once. Exactly 14 A, 6 B and 1 C templates, total **21**.

These counts exhaust the physical six-coordinate degree-two universe, INCLUDING repeated pair edges. In particular the same source POINT factor repeated in two genuine original incidences is a legitimate B/C possibility and MUST NOT be silently dropped. Independent source implementation enumerates ALL 5005 six-edge K6 multisets and independently checks the 3 cases. The test oracle redoes these counts for **every** pair of 15 K6 edges, distinct adjacent or distinct disjoint, verifying permutation symmetry with no fitted constants.

When a root physical pair edge is repeated, four other physical coordinate symbols must be selected: at most 6*binom(a−2,4) formal physical templates. For distinct adjacent pinned pair edges sharing one coordinate, three remaining coordinates must be chosen: exactly 10*binom(a−3,3) formal templates. For disjoint pinned pair edges, two remaining coordinate symbols must be selected: exactly 21*binom(a−4,2) templates.

## 3. Genuine original W(3,s) TWO source LINE factor capacity theorem

Fix s=2^h>=2, d=s+1, and a=min{a:binom(a,2)>=(s+1)(s²+1)}. Choose ANY pair ell != m of ACTUAL ORIGINAL W(3,s) LINE factors and ANY completely globally injected original source POINT map f (the original LINE map g is irrelevant to this left physical upper). Let N_{ell,m}(f) be the count of TRUE sets Q of SIX DIFFERENT ORIGINAL incidence-flag IDs such that:
- at least one actual incidence in Q is on ell and at least one actual incidence in Q is on m;
- the SIX original point factor physical image edge OCCURRENCES under ONE GLOBAL f form a six-coordinate physical degree-two multigraph, one of A/B/C.
- There is NO assumption the right g passes the seven-GF5 acceptance filter. Restricting Q to accepted positive GF5 can only decrease N.

**All-h NEW bound:**

\[
\boxed{
N_{\ell,m}(f)\le
24d^4\left[
6\binom{a-2}{4}
+d^2\left(10\binom{a-3}{3}+21\binom{a-4}{2}\right)
\right]=:\mathcal M_2(s).
}
\]

**Complete genuine-original proof:** Given eligible Q, mark one of its actual different incidence IDs (p,ell) and another (q,m). For p=q, the two distinct ORIGINAL W(3,s) line factors ell,m can have at most ONE common real ORIGINAL source point: otherwise these two actual source lines with two actual original common points create a forbidden original source C4 in the incidence graph (a classical generalized quadrangle has girth 8). Therefore the number of possible repeated-POINT root pairs is <=1, and their globally injected physical point image edge is necessarily the SAME. This case contributes at most six physical multiset templates on any extra 4 physical coordinates, multiplied by 4! ways to assign remaining four distinct incidence-column positions, and at most d^4 actual original adjacent LINE factors from their inverse-image actual original point factors.

For p != q, there are at most d^2 actual original root incidences (p,ell),(q,m), each independently selected from the true source degree-d neighborhoods. Global injectivity of f ensures f(p) != f(q), so their physical edges are either adjacent or disjoint. The adjacent case has <=10*binom(a−3,3) templates, disjoint case <=21*binom(a−4,2). Add their capacities to bound both possibilities, then 4! remaining positional assignments and at most d^4 actual original neighboring LINE factor choices through each unique f-inverse-mapped original point factor. Every valid actual Q has at least one encoding; repeated Q and invalid source factor pairings only create overcount, so the bound is rigorous. **One single f** is used for all source Q and NO new fake source edges or independent g labels appear.

For s>=4, the exact true dyadic physical palette inequality a^2<=4s^3 holds (see previous #549), while d<=5s/4. Hence binom(a−2,4)<=2s^6/3, binom(a−3,3)<=4s^(9/2)/3 and binom(a−4,2)<=2s^3. For s>=4, use s^(9/2)<=s^5 to get the exact rational bound

\[
\mathcal M_2(s)
\le24(5/4)^4s^4
\left[4s^6+(25/16)s^2\left((40/3)s^5+42s^3\right)\right]
\le(1356875/256)s^{11}
<5400s^{11}.
\]

This bound is honest but crude: keeping the half-integer exponent yields O(s^(21/2)) as the actual leading-order size of these elementary terms; the explicit O(s^11) integer-exponent statement is convenient for comparison with #549. No asymptotic result about actual full seven S minimum follows.

## 4. Global disjoint TWO source-LINE swap seven-class signed Hessian

Choose two disjoint legal original source LINE factor transpositions sigma=(ell1,ell2) and tau=(m1,m2), all four LINE factor IDs different; swap their physical unordered pair image labels under ONE original g to form g^sigma, g^tau, g^(sigma tau). Since they are disjoint, both global transformations commute and every map remains a complete injection onto EXACTLY the SAME original right physical pair-image support. The point map f remains fixed.

For each historical positive seven-GF5 accepted class k and same original real six-incidence Q, let I_k(Q;f,g) be its {0,1} indicator. Define the exact signed mixed Hessian

\[
H_{\sigma,\tau}S_k(f,g)=
S_k(f,g^{\sigma\tau})-S_k(f,g^\sigma)-S_k(f,g^\tau)+S_k(f,g).
\]

The already-known genuine ORIGINAL support identity says this sum is entirely supported on Q which touch at least ONE original line ID from sigma AND at least ONE from tau. Such Q contains a cross-pair (ell_i,m_j) for one of at most FOUR pairs i,j in {1,2}; thus its TRUE original source Q count is at most 4*M2(s), with NO per-source-Q resampling. The absolute mixed finite difference of a binary accepted indicator is at most TWO for each actual original Q. Since the selected seven classes are disjoint, the combined S_7 original sixset indicator is also binary.

**New all-h quantitative signed source Hessian bound:**

\[
\boxed{
|H_{\sigma,\tau} S_7(f,g)|\le8\mathcal M_2(s)
\le43200s^{11}\qquad(s=2^h\ge4).
}
\]

This is a true same-global-original-pair, seven-GF5 bound, not a statement that the mixed curvature must be positive or negative. The historical selected **necessary** 51-palette GF5 R3 lower numerator is W_7=sum_k w_k S_k, with immutable class weights 5643 D6; 45600 B-left/A-right and A-left/B-right; 43320 C/A; 49050 C/B; 51750 BB-overlap; 45010 BB-disjoint. The left type A/B/C maximum weights are 45600/51750/49050. Using the same three physical doubly rooted templates yields the class-weighted pair bound

\[
\mathcal M_{2,W}(s)=24d^4[
302400\binom{a-2}{4}+
d^2(474450\binom{a-3}{3}+997950\binom{a-4}{2})
],
\]
\[
\boxed{|H_{\sigma,\tau}W_7(f,g)|\le8\mathcal M_{2,W}(s).}
\]

These concern the accepted SEVEN-class necessary GF5 floor numerator, NOT the total actual GF5 R3, and do not solve ASET.

## 5. Independent exact genuine W32 falsifiers and original same-Q sign

Files: versioned source research/hyp105_issue230_d6aa4au_two_line_seven_hessian.py, six independent unit groups, and dedicated hosted workflow (four additive research files total).

1. Complete K6 5005 physical sixmultisets and EVERY of its 15 same-root or 15*14 adjacent/disjoint root choices: exactly same B3,C3, adjacent A7,B3, disjoint A14,B6,C1.
2. All dyadic genuine order powers h=1..32,40,48,64,80 exact integer formulas, correct m/a minimal palette, explicit |H|<=43200s^11 for h>=2; no invented high-h symplectic geometry or empirical fit.
3. Real ORIGINAL W(3,2) source symplectic 45 actual incidences, verify its original source line partial linearity on ALL 105 source line pairs; count source-Q overlap for six selected line-ID pairs by DIRECT TRUE ORIGINAL 62,370 left-eligible six-flag ID enumeration, independently checking each against M2.
4. For each of ORIGINAL W32 S68/S72/lex/reverse completely fixed globally injected f,g, choose six prescribed pairs of genuinely disjoint original source LINE label swaps. Construct the FOUR fully globally injected maps g,g^sigma,g^tau,g^(sigma tau); score all 62,370 actual original six-ID left-eligible Q at all four maps with historical seven GF5 classifier, then independently re-evaluate only the true original Q touching BOTH swapped source-line ID pairs and check the EXACT per-class signed Hessian tensor and weighted floor numerator. Every source-Q outside this true original intersection contributes zero.
5. Independent all-physical-coordinate typed relabel invariance of EVERY original candidate seven-GF5 Q on true W32 under two different physical K6 coordinate permutations, preserving original source geometry. Malformed original data/synthetic fake source C4 and a fully fake big source geometry never count as evidence.

The boolean Hessian source support identity per Q and the older PR #417 numerical finite curvature are recognized as PRIOR ART; novelty is solely the new double-rooted original-GQ capacity and its all-h O(s^11) realization, separately independently validated.

## 6. Fundamental open gap

The root issue asks that every ORIGINAL FIXED adversarial global (f,g) satisfy S_7(f,g)>=c*s^6, or a rigorous infinite correlated counterfamily, or an accepted model-equivalent reduction. The new O(s^11) bound still exceeds desired Omega(s^6) by FIVE integer powers; even the asymptotic refined O(s^(21/2)) is much too loose. **This is NOT Branch A/B/C.** A genuine lower from the original pair requires some type of **signed geometric compensation** under the ORIGINAL global maps, an aligned original source Hall closure theorem, or a rigorously constructed infinite original counterfamily, not simply applying an absolute-value or two-swap Hessian magnitude estimate. Earlier PR #493/#497 have genuine original mixed curvature of both signs. Keep Draft unmerged, independent math referee and exact final SHA hosted checks required.


## 7. Frozen genuine ORIGINAL W32 signed Hessian certificate (exact source)

The first exact-code-head GitHub-hosted dedicated CI [#38872051432](https://github.com/definitely-stable/Mathlab/actions/runs/38872051432) completed **two jobs SUCCESS**: all K6 physical root pairs, h1..80 exact symbolic original GQ proof arithmetic, literal true W32 source-line partial linearity, six globally legal pairwise-disjoint true original LINE transposition pairs for EACH of S68/S72/lex/reverse, all four fully globally injected right map states per pair, independent 62,370 TRUE six-original-ID full seven-GF5 census and independent double-source-LINE-touch sparse signed Hessian, plus typed physical-coordinate permutation invariance. All SIX test methods passed. The complete independent finite-sample Hessian vectors are now **frozen in source test assertions** rather than relying only on a textual table.

In each cell H7 is the signed unweighted SEVEN positive class count mixed finite difference, and HW is the signed historical selected 51-palette **necessary** GF5 seven-class R3-floor numerator difference. Each is computed at exactly one ORIGINAL fixed global source point map f and 4 related, individually fully global source LINE maps g, gσ, gτ, gστ. No source Q physical redraw; the same true six-original-incidence-ID Q is used in all 4 terms.

| Two DISJOINT real-original LINE swaps (σ,τ) | S68 H7 / HW | S72 H7 / HW | lex H7 / HW | reverse H7 / HW |
|---|---:|---:|---:|---:|
| (0,1) ; (2,3) | 0 / −46,107 | +1 / +35,580 | +11 / +251,938 | −4 / −394,485 |
| (0,2) ; (3,4) | −6 / −268,450 | −18 / −815,730 | +8 / +524,628 | −3 / −124,893 |
| (0,3) ; (1,4) | −21 / −877,586 | +6 / +291,040 | +20 / +931,450 | +16 / +609,139 |
| (0,5) ; (6,7) | −16 / −712,660 | −13 / −540,363 | +22 / +943,246 | −6 / −333,007 |
| (4,5) ; (8,9) | −6 / −275,290 | −19 / −864,630 | −2 / +27,671 | +5 / +135,716 |
| (1,2) ; (10,11) | −13 / −638,827 | −20 / −923,040 | −1 / +65,021 | −42 / −1,804,676 |

The actual original doubly touched source six-Q shadow populations (same for S68/S72 and separately same for lex/reverse under the frozen global f) are 19,262 / 22,974 / 20,948 / 21,743 / 22,114 / 20,760 in the six ordered swap-pair rows for S68/S72; for lex/reverse 21,042 / 19,012 / 21,300 / 20,261 / 19,974 / 20,316. The mixed signed seven-S curvature can have BOTH SIGNS even with one fixed original f,g (S72, lex, reverse). In lex's fifth and sixth row the UNWEIGHTED seven-Hessian is negative while the SELECTED GF5 weighted numerator Hessian is positive, independently disproving any universal assumption that their signs must agree.

This is **FINITE true original W32**, never an all-h counterfamily. The new all-h O(s11) bound is absolute, not an all-h sign law. The previous PR #417 established formal support and finite curvature identities; no claim this physical signed finite difference phenomenon was newly discovered from scratch. What is NEW to this slice is the **physical doubly-rooted 6/10/21 ORIGINAL GQ partial linearity bound**, its explicit all-h mixed-curvature capacity, and independently auditable exact W32 true-original signed numerical regression certificates. Root issue #230 and all A/B/C gates remain OPEN; author checks do not substitute for an independent mathematical referee.
