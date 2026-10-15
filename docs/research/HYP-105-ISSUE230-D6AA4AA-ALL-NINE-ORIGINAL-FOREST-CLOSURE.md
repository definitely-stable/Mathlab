# HYP-105 / issue #230 — D6-AA4-AA-SRC: exact ALL-h genuine ORIGINAL nine-forest closure and complete seven-GF5 global ensemble

**Research-only mathematical record.** Strict stacked child of [AA4-Z-SRC PR #502](https://github.com/definitely-stable/Mathlab/pull/502) pinned at exact parent commit \`2b1824a005167332db2b251325d06e125b32a8ca\`. No production/main changes, no root-issue closure and no integration assertion. Complete genuine ORIGINAL symplectic GQ W(3,s), s=2^h>=2; ALL six selected ORIGINAL point-line incidence IDs Q must be distinct; one point/line source factor must be the SAME original GQ factor across all Q. At the physical transfer stage, one uniformly sampled COMPLETE globally injected original point map f and an independent one uniformly sampled COMPLETE globally injected original line map g are reused across ALL Q — no per-Q fake randomness. Historical seven selected positive GF(5) tags and fixed 51-palette certified weights are reused, never changed.

**Result scope:** Exact ALL-h source-only cardinality of the **last missing original six-incidence forest cell B/B-disjoint**, followed by an exact complete **NINE-of-NINE genuine source forest catalog** and complete **SEVEN-of-SEVEN historically positive GF5 ensemble expected class counts** for every s=2^h. This is NOT the HYP-105 adversarial all-f,g \(\inf S_s=\Omega(s^6)\) theorem, NOT an infinite counterfamily, NOT an all-h GF5 R3 bound, NOT ASET. All source counting uses ordinary combinatorial inclusion-exclusion and genuine GQ unique projection/girth8; these general-purpose methods are not claimed new mathematical primitives. Distinct from the ongoing parallel CYC sign-robust and global-swap work.

## 1. Unique ORIGINAL B/B-disjoint six-edge forest and double-P2 decomposition

Let \(G\) be the ACTUAL original GQ incidence graph with \(V=(s+1)(s^2+1)\) original points, \(V\) original lines, \(d=s+1\), and \(N=Vd\) ACTUAL original point-line incidence edges. Its degree is d and its girth is 8. Every B/B-disjoint original six-incidence source Q has exactly one original **POINT** source factor repeated twice and one original **LINE** source factor repeated twice; these doubled sources do **not** share a selected original incidence Q edge.

Consequently exactly TWO *different-type*, vertex-disjoint, two-edge genuine-original source paths occur as the unique repeated-source components:
- an original line-centered P2: two distinct actual original points \(a,b\) incident with actual original source line \(L\), so Q contains \(\{(a,L),(b,L)\}\);
- an original point-centered P2: actual original point \(p\) incident with two distinct actual original source lines \(M,N\), so Q contains \(\{(p,M),(p,N)\}\);
- TWO additional original incidence edges, forming a 2-matching on the residual SOURCE graph obtained after deleting exactly these six original source vertices \(\{a,b,p,L,M,N\}\).

The two source P2 types differ (one repeated point vs repeated line), and their positions in Q are intrinsic: **each six-Q has exactly one such type-distinguished ordered root pair and exactly one residual two-edge matching**. It is wrong to divide this count by two or to include cross source edges that were not selected among Q.

The first line-centered P2 has exactly

\[
R=V\binom d2
\]

genuine original choices. Fix one, with original source line L and its selected two original points a,b. We count its possible type-opposite point-centered P2 partners \((M,p,N)\) while preserving all true GQ source incidences, then the residual original source two-edge matchings.

## 2. New exact three-class ORIGINAL root-pair geometry using the unique GQ projection

For a fixed genuine original source line-centered P2 \((a,L,b)\), a type-opposite source partner has p not among a,b, and M,N not equal L.

For actual original source point p *on* L but not a,b, its two selected original line partners must be chosen from the d−1 lines through p other than L. There are

\[
(d-2)\binom{d-1}{2}
\]

such B roots, and each induces exactly ONE additional source incidence \((p,L)\) between the six deleted root vertices, not selected among original Q.

For source point p NOT on L, the true generalized quadrangle projection axiom gives exactly ONE original source point \(q\in L\) collinear with p, through a UNIQUE original line \(T\neq L\). For each q in L there are exactly \((d-1)^2\) actual original p outside L projecting to it. There are two geometrically different possibilities:

1. \(q\in\{a,b\}\). If the partner line pair M,N includes T, exactly ONE extra original source incidence exists between the deleted root vertices, because T contains q and p. Number of such partners \(2(d-1)^2(d-1)=2(d-1)^3\). If M,N avoids T, there is NO extra deleted-root source incidence, but the removed original POINT vertices p and q have ONE common original **residual line** neighbor T; count \(2(d-1)^2\binom{d-1}2\).

2. \(q\in L\setminus\{a,b\}\). Number of p choices \((d-2)(d-1)^2\). If M,N includes T, there is NO extra deleted-root original incidence (because q is not among a,b,p), but removed original L and one of removed M,N meet in q, ONE common original **residual point** neighbor. Count \((d-2)(d-1)^3\). If M,N avoids T, there is neither an extra deleted-root incidence nor a common residual neighbor: count \((d-2)(d-1)^2\binom{d-1}2\).

Girth8 forbids a second independent deleted-root cross original incidence, or a residual point/line simultaneously adjacent to multiple unaccounted deleted root vertices: such a configuration would close a genuine ORIGINAL 4- or 6-cycle. Let t be the number of EXTRA original incidences between the six deleted root vertices beyond their four selected P2 source edges, and let H be the exact number of unordered pairs of deleted source vertices with a common still-remaining original source neighbor (aggregated across remaining point and line types, \(\sum_u\binom{k_u}2\)). All actual rooted pairs fall into exactly THREE possible types:

| Genuine ORIGINAL double-P2 class | Extra original deleted-root incidences t | Common residual source neighbor pair H | Exact number per fixed line-centered P2 |
|---|---:|---:|---|
| I: original cross-root extra | 1 | 0 | \(\alpha=(d-2)\binom{d-1}2+2(d-1)^3\) |
| II: one common residual neighbor | 0 | 1 | \(\beta=2(d-1)^2\binom{d-1}2+(d-2)(d-1)^3\) |
| III: no extra / no common | 0 | 0 | \(\gamma=(d-2)(d-1)^2\binom{d-1}2\) |

These are exact integers for EVERY s=2^h>=2, independent of how the original P2 is embedded in the TRUE original W(3,s).

## 3. Exact TWO-incidence residual matching count for each root-pair geometry

For any allowed (t,H), delete the three actual source points and three actual source lines from G. This deletes all incident original source edges. The four source P2 edges plus t additional original cross edges are internal among the six removed vertices. Therefore the number of ORIGINAL residual incidence edges is

\[
e_t = N-6d+(4+t).
\]

There are \(2V-6\) remaining original source vertices. For each such vertex u let \(k_u\) count its actual adjacent deleted ORIGINAL source factors; its original residual degree is \(d-k_u\). Exactly

\[
\sum_{u\text{ remaining}}k_u=6d-2(4+t)=6d-8-2t,
\qquad
\sum_{u\text{ remaining}}\binom{k_u}{2}=H.
\]

Crucially, **counting a pair of distinct residual edges that do NOT share an ORIGINAL point/line** requires nothing beyond e_t and the residual sum of degree-two stars. Since

\[
\binom{d-k}2=\binom d2-(d-1)k+\binom k2,
\]

the exact residual number of **two-edge source matchings** is

\[
\boxed{
M_2(t,H)=
\binom{N-6d+4+t}{2}
-(2V-6)\binom d2
+(d-1)(6d-8-2t)-H.
}
\]

No physical pair-image labels are involved. This is not a probabilistic independence approximation, not an abstract hand-picked subset universe. It is a deterministic combinatorial identity for the actual source GQ residual graph after deleting each actual pair of source P2 roots.

Combining the three types and exactly R root choices, we obtain the NEW ALL-h exact genuine-original sixset formula

\[
\boxed{
U_{B/B\text{-disjoint}}(s)
=V\binom d2\Big[
\alpha\,M_2(1,0)
+\beta\,M_2(0,1)
+\gamma\,M_2(0,0)
\Big].
}
\]

It is a fixed finite formula of original V,d alone, with no uncomputed source geometry or physical overlap factors.

## 4. Independent TRUE ORIGINAL W32 and W34 source geometry evidence

| Exact original source count | TRUE W(3,2), V=15,d=3 | TRUE W(3,4), V=85,d=5 |
|---|---:|---:|
| Root line-centered original P2, \(V\binom d2\) | 45 | 850 |
| Type-I opposite P2 partners \(\alpha\) | 17 | 146 |
| Type-II opposite P2 partners \(\beta\) | 16 | 384 |
| Type-III opposite P2 partners \(\gamma\) | 4 | 288 |
| Residual original \(M_2(1,0)\) | 440 | 78,240 |
| Residual original \(M_2(0,1)\) | 412 | 77,848 |
| Residual original \(M_2(0,0)\) | 413 | 77,849 |
| **SOURCE B/B-disjoint six ORIGINAL incidence Q** | **707,580** | **54,176,606,400** |

True ORIGINAL W(3,2): the AA4-U oracle independently exhaustively counted **ALL \(\binom{45}6=8,145,060\) actual six-original-incidence Q**, and measured original B/B-disjoint=707,580. This new formula is independent of that source-census implementation. A SECOND independently constructed TRUE ORIGINAL W32 geometry oracle enumerates **ALL 45 possible line-centered original P2**, and for each ALL 37 valid type-opposite point-centered original P2 partners (45×37=1,665 actual root pairs). Direct source adjacencies determine t and H WITHOUT referencing the new formulas. On selected roots it also enumerates all actual residual pairs of original incidence edges, accepting those without repeated source point/line IDs; these DIRECT residual M2 counts match the three theoretical values 440/412/413.

True ORIGINAL W(3,4): the same separately verified TRUE GQ unique-nonincident source-point/line projection validator constructs the actual 85+85 vertex, 425-original-flag incidence graph. Independently classify and count EVERY allowed opposite source P2 partner for several actual line-centered source P2 roots (each 818 partners) and directly count actual residual 2-matchings for representative types. This is real GQ local source evidence, NOT a fictitious GQ and NOT a claim that \(\binom{425}6\) original sixsets were fully enumerated. Fake 15+15 degree-3 graphs that contain forbidden 6-cycles and physically non-global-injective fixture labels both fail closed.

## 5. NEW exact COMPLETE all-nine-cell TRUE ORIGINAL GQ forest source catalog

For every order s=2^h>=2, the nine genuine ORIGINAL source six-incidence GQ forest populations are now ALL independently expressible by finite closed integer formulas:

| True ORIGINAL SOURCE forest | ALL-h formula source |
|---|---|
| A/A | AA4-Z-SRC: 6-edge source matching via Godsil SAW/regular tree moment Newton recurrence (prior-art mathematical method) |
| A/B, B/A | AA4-Z-SRC: source P2 root × residual source 4matching through exact formal cavity |
| A/C, C/A | AA4-Y-SRC: three original source pencils, exact GQ line triple collision inclusion-exclusion |
| B/C, C/B | AA4-X-SRC: true original P4 + source-disjoint P2 |
| B/B-overlap | AA4-X-SRC: true original P3 + 3matchings of residual GQ source graph |
| **B/B-disjoint** | **THIS AA4-AA-SRC: two typed original disjoint P2 roots + residual original two-matching above** |

True W32 complete nine-cell source vector in canonical source order:

\[
\begin{aligned}
&(U_{AA},U_{AB},U_{BA},U_{AC},U_{CA},U_{BC},U_{CB},U_{BBo},U_{BBd})\\
&=(1566360,1666980,1666980,6225,6225,5220,5220,910080,707580).
\end{aligned}
\]

All source counts are **not** universal physical pair-map accepted motif counts for a specific adversarial f,g. They are a source-geometry reservoir before physical projection. The resulting "nine cells" partition only the original SIX Q whose actual source point+line multiplicities are in A/B/C, not ALL \(\binom{N}6\) source Q; original six-Q outside this grid are correctly tracked and never confused with physically positive original seven-GF5 classes.

## 6. NEW exact COMPLETE seven-of-seven historical accepted original GF5 ensemble, all h

Apply the independently established AA4-W one-uniform-COMPLETE-global-map physical source multiplicity probabilities:

\[
p_H=\frac{(a)_6}{(K)_6},\quad p_A=70p_H,\quad
p_B=\frac{72K\binom{a-2}4}{(K)_5},\quad
p_C=\frac{(a)_6}{8(K)_3},
\]

where \(a\) is minimal with \(K=\binom a2\ge V\). Sample one uniformly random COMPLETE globally injected original point physical pair map f and ONE independent uniformly random COMPLETE globally injected original line physical pair map g; each is shared over **ALL source Q**. From the true ORIGINAL nine source populations, AA4-W's seven historically positive GF5 tag transfer identity yields the following exact all-h FULL seven-class expected count:

\[
\boxed{
\begin{aligned}
\mathbb E_{f,g}S_s
={}&60p_H^2\,U_{AA}
+p_Ap_B\,(U_{AB}+U_{BA})\\
&+p_Ap_C\,(U_{AC}+U_{CA})
+p_Bp_C\,(U_{BC}+U_{CB})\\
&+p_B^2\,(U_{BB\text{-overlap}}+U_{BB\text{-disjoint}}).
\end{aligned}
}
\]

The last NEW independently closed positive class has

\[
\boxed{
\mathbb E_{f,g}N_{BB\text{-disjoint}}
=U_{BB\text{-disjoint}}(s)\,p_B^2.
}
\]

The same exact SOURCE-conditioned formula with immutable historical positive seven-tag certified weights gives the FULL seven-class selected **51-palette GF5 numerator expectation**. Note: distinct A/B and B/A historical tags can have distinct weights even though their source populations are equal; the weighted evaluator uses the actual historical tag-specific fixed weights, not a uniform lumped weight.

Exact real SOURCE W32 independent full-seven mean:

\[
\begin{aligned}
\mathbb E_{f,g} N_{BBd}
 &=\frac{6\,368\,220}{1\,002\,001},\\
\mathbb E_{f,g} S_2
 &=\frac{165\,129\,984}{1\,002\,001}.
\end{aligned}
\]

The FULL W32 value agrees with the separate earlier AA4-W exact nine-cell-source-universe numeric oracle, which used the independently enumerated true W32 original 8,145,060 Q source census. This is NOT any fixed pair's actual seven S: genuine adversarial full map fixtures S68 and S72 have actual S=68 and S=72.

True W34 all-h exact example:

\[
\mathbb E_{f,g} N_{BBd}
=\frac{121\,897\,364\,400}{6\,661\,561},\qquad
\boxed{
\mathbb E_{f,g} S_4
=\frac{4\,960\,589\,766\,387\,600}{12\,317\,226\,289}.
}
\]

### New complete all-seven asymptotic leading constant

The exact source formula in Section 3 yields

\[
U_{BBd}(s)=\left(\frac18+o(1)\right)s^{18},
\qquad
p_B=(12+o(1))s^{-6},
\]

so its expected accepted seventh-tag contribution is

\[
\boxed{\mathbb E_{f,g}N_{BBd}=(18+o(1))s^6.}
\]

The six previously closed historically accepted GF5 tags from AA4-Z-SRC have combined expectation \((1016/3+o(1))s^6\). Thus **ALL SEVEN** classes now have the explicit all-h *ensemble* asymptotic:

\[
\boxed{
\mathbb E_{f,g} S_s
=\left(\frac{1070}{3}+o(1)\right)s^6.
}
\]

This is a COMPLETE seven-tag uniformly global ensemble leading constant and a finite exact formula for every order 2^h, not a deterministic all-physical-map lower. The positive selected historical 51-palette numerator also has an exact full expectation, with its own different constant obtained by applying the verified fixed tag coefficients. No new all-h R3/ASET lower or a fully correlated root counterexample is implied.

## 7. Acceptance, proof limitations, original vs physical invariants and next decisive gate

All claims are scoped to:
1. TRUE original generalized quadrangles W(3,2^h), all h>=1, six distinct original flag IDs Q;
2. ORIGINAL source GQ girth8/unique projection, NEVER merely a fake regular 15+15 source graph;
3. Exactly one complete GLOBAL type-specific physical unordered-pair injection f and another complete GLOBAL injection g whenever defining actual motif S_s(f,g), and independent full uniform COMPLETE global f,g only in expectation calculations;
4. Historical selected seven GF5 tags, fixed seven-tag 51-palette charge coefficients. No invented motifs or altered selected source-Q universe;
5. SOURCE counts versus PHYSICAL acceptance distinctly recorded, with original outside-grid source six-Q tracked.

Implementation: exactly four additive research-only files — all-h exact source/ensemble Python verifier, 10 independent original model tests (W32 full 8,145,060 source-Q census and actual 1,665 double-P2 root placements; W34 independent true original source root placements and representative direct residual 2matching enumeration), mathematical Markdown with all exact formulas/proofs/limitations, dedicated three-job GitHub-hosted workflow. Require dedicated, INDEX, Proof Audit and FULL Research SUCCESS for exact FINAL child HEAD plus **separate independent mathematical referee**. Parent AA4-Z #502 last verified dedicated 3/3, INDEX, Proof Audit SUCCESS; FULL Research was in progress; parent AA4-Y #499 had a cancelled research shard explicitly rerun. Until all are actually green, do NOT merge to main or claim chain scientific acceptance.

**Next substantive question:** the source-only nine-cell enumeration and complete all-seven uniform-ensemble reference are FINISHED by this slice. Do **NOT** extend the same source-count sequence endlessly; it has reached its natural stopping point. Prioritize original AA4-U/AA4-V, parallel CYC AA4-Y3, and genuine JPKC/EICE anchors to attack the STILL OPEN **deterministic every-adversarial-full-global f,g** joint physical-acceptance question:

\[
\inf_{\text{complete globally-injected }f,g}
S_s(f,g)\stackrel{?}{\ge}c\,s^6
\quad\text{for all }s=2^h.
\]

A necessary next mathematical theorem would force genuine SOURCE forest mass into PHYSICAL non-AA joint acceptance OR the same-source-position aligned connected D6 for *every* f,g, respecting source and physical global coherence simultaneously. Positive expectations over random f,g cannot do this. Compare with exact true-original W32 S68/S72 where aligned D6=0 and all positive seven charge comes from non-AA, and the parallel Y-CYC global swap/Gram controls. If an attempted compensation lemma fails, retain a valid concrete true full-global source counterexample and its quantified NO-GO scope. This remains HYP-105 #230 OPEN.

**Retention/integration:** immutable research code, proofs, formulas, full exact tables and mathematical limitations stay in versioned Markdown, Draft PR and issue comments. Register claims/formulas/evidence/proof graph via authoritative RCP JSON sources, then automatically regenerate the five structured Markdown registry docs *after* independent scientific acceptance; generated Markdown must never be hand-edited. Do not change main or parallel Y3-CYC work from this scientific Draft.
