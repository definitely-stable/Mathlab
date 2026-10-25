# HYP-105 / issue #230 — D6-AA4-W: exact ALL-h ORIGINAL seven-GF5 one-global-map transfer kernel

**Research-only proof and executable, strict stacked child of [AA4-V #491](https://github.com/definitely-stable/Mathlab/pull/491), parent pinned at exact HEAD \`482cf14c90fac775f041464fafd8154abb743fd0\`.** This result is an *all-h conditional ensemble theorem*, not a universal deterministic all-f,g lower, not Branch A or infinite Branch B, nor an all-h GF5 R3/ASET exponent. The original GQ geometry, all six distinct original incidence IDs Q, the two typed complete globally injected source maps, and the selected seven positive 51-palette GF5 tags remain unchanged.

## 1. What is not captured by AA4-V

The exact all-h AA4-Q/AA4-V identity is

\[
S_s(f,g)=|J\setminus AA|+D_6(f,g),\quad
J=H_P(f)\cap H_L(g)
\]

where **both halves use the SAME six genuine original point-line incidences Q**. AA4-U determined the nine source-forest classes; all nine cell-conditioned Fréchet lower bounds vanish on full ORIGINAL W32 S68/S72 even though true S=68/72. AA4-V classified 70 physical original-position 2-factors, obtained the valid fixed-pair D6 lower via their common-edge overlap, and proved the latter insufficient on S68/S72 (the positional surplus is negative). PR #492 in the separate CYC stack studies a genuine second-moment upper for the ALIGNED D6 class under one random global g. Neither AA4-V nor the parallel D6 second-moment branch gives the entire **seven-class** conditional transfer, including A/B/C, the two original B/B classes and selected GF5 weights.

AA4-W closes this *specific transfer bookkeeping gap*: exact expectation of each of the SEVEN selected GF5-positive original Q classes given **one arbitrary fixed FULL global typed injection**, averaging the other side as ONE uniform complete global injection (same random mapping simultaneously for every Q). It is a formal correctness/reference identity against which any future original positional/Hall/EICE all-f,g inequality can be tested. It does not resolve the adversarial correlation obstruction.

## 2. Four exact all-h one-global-injection physical response probabilities

Let \(s=2^h,\ h\ge1\), \(V=(s+1)(s^2+1)\), let \(a=\min\{b:\binom b2\ge V\}\), and \(K=\binom a2\). Falling factorial \((n)_k=n(n-1)\cdots(n-k+1)\). For one fixed selection of actual original source factors, the uniform injection of ALL \(V\) source factors into physical unordered K_a pairs restricts to a uniform ordered *without-replacement* tuple of physical images on those factors. Thus the following response probabilities are exact, regardless of Q's other original incidence factors:

| Genuine opposite-source profile | Required physical class | Exact probability under ONE complete uniform global source map |
|---|---|---|
| Six DISTINCT source factors (A) | any 2-factor, 60 connected C6 + 10 disconnected C3+C3 | \(p_A = 70(a)_6/(K)_6\) |
| One source factor appears twice (B), four once | physical duplicated edge + C4 on complementary physical coordinates | \(p_B = 72K\binom{a-2}{4}/(K)_5\) |
| Three different factors each appear twice (C) | three physical unordered coordinate pairs forming a matching on six different coordinates | \(p_C=(a)_6/[8(K)_3]\) |
| Six source factors all DISTINCT (A) AND fixed-side connected positional cycle H on SAME original Q | unique aligned connected D6 on those original Q positions | \(p_H=(a)_6/(K)_6\) |

Derivations:
1. A: \(\binom{15}{6}\) choices of six physical column-position edges are checked directly for degree two; exactly 70 qualify; each of 70 original-position labelled 2-factors has \((a)_6\) physical-coordinate assignments; each produces a unique ordered tuple of six original-source physical unordered pairs. Thus exactly \(70(a)_6\) of \((K)_6\) possibilities.
2. B: choose K possible physical images of the doubled original factor, then four physical coordinates among a−2 remaining, then one of THREE different 4-cycles, then a bijection of the four other DISTINCT original source factors to those four physical C4 edges (4!=24 choices); total \(72K\binom{a-2}4\), out of \((K)_5\) ordered distinct assignments.
3. C: inject six different physical coordinates into THREE *labelled* disjoint unordered physical pair labels; each matching assignment has \(2^3=8\) coordinate orientations and there are \((a)_6/8\) valid ordered triples among \((K)_3\) total.
4. D6: on the six immutable original Q positions the fixed side has ONE connected original-column dual H; each injective physical-coordinate assignment of H's SIX positional edges produces one unique ordered tuple of six right-source physical unordered pair labels; \((a)_6\) choices among \((K)_6\). The right map is shared globally, not sampled independently for each Q.

The proof needs no independence across different Q. Q correlations under one globally shared random physical assignment are strong, but by linearity of expectation they **do not affect the first moment**. This is the precise quantifier limitation.

At s=2 (true original W(3,2), a=6,K=15), exact reduced fractions:

\[
p_H=\frac1{5005},\quad p_A=\frac2{143},\quad
p_B=\frac3{1001},\quad p_C=\frac3{91}.
\]

Tests independently enumerate the 70 physical six-edge 2-factors, all K6 five-source duplicated-root/C4 patterns and all three-labelled-factor physical matching triples, rather than simply reusing the rational formulas.

## 3. NEW every-fixed-f exact seven-tag class-resolved conditional identity — all h

Let \(f\) be **ANY** complete globally point-injective map of genuine original GQ points. Let \(L_F(f)\) denote the point-physically-acceptable ORIGINAL six-Q population with immutable original point/line source-forest cell F among the nine cells AA,AB,BA,AC,CA,BC,CB,BB-overlap,BB-disjoint, and let \(n_F=|L_F(f)|\). Note that some one-sided valid physical Q do not have a permissible original A/B/C profile on the opposite source type; these are counted separately and **excluded** because no globally injected physical image on the opposite side can join them into a positive original seven class. This resolves AA4-U's domain issue.

Let \(t_{AA,C}(f)\le n_{AA}\) be those original AA Q whose *fixed physical point* coordinate-column dual H is a CONNECTED C6 on the same six actual original Q ID positions, not two triangles.

Now sample ONE full random complete globally-injective line-factor physical map \(g\), uniform and independent of f. Define \(\mathcal E_{\rm tag}(f):=\mathbb E_g[\#\{\text{original selected six-Q of tag}\}]\). Then for all h and ALL f:

\[
\begin{aligned}
\mathcal E_{D6} &= p_H\,t_{AA,C},\\
\mathcal E_{B\text{-left}/A\text{-right}}&=p_A n_{BA},\\
\mathcal E_{A\text{-left}/B\text{-right}}&=p_B n_{AB},\\
\mathcal E_{C/A}&=p_A n_{CA}+p_C n_{AC},\\
\mathcal E_{C/B}&=p_B n_{CB}+p_C n_{BC},\\
\mathcal E_{BB\text{-overlap}}&=p_B n_{BB\text{-overlap}},\\
\mathcal E_{BB\text{-disjoint}}&=p_B n_{BB\text{-disjoint}}.
\end{aligned}
\]

This is an EXACT finite all-h vector equation, not an asymptotic estimate. Full seven \(\mathbb E_g S_s(f,g)=\sum_{\rm 7\,tags}\mathcal E_{\rm tag}(f)\). With the positive, fixed, certified R3 51-palette GF5 weights \(w_{\rm tag}\) already registered upstream,

\[
\boxed{
\mathbb E_g[\mathrm{GF5}^{(51)}_{\rm selected}(f,g)]
=\sum_{\rm seven\,tags}w_{\rm tag}\,\mathcal E_{\rm tag}(f).
}
\]

The same theorem holds with the right global line map \(g\) fixed and one independent complete uniform point map f, with point/line source role exchanged (so A/B and B/A probabilities are applied to the **other** original factor multiplicity). The source geometry and six original IDs remain exactly the same.

**Dependency/novelty distinction:** AA4-T proved the D6 component in the fixed-point direction; AA4-N proved the reversed fixed-line B/A component; AA4-U proved the nine source-forest partition; AA4-V proved the deterministic positional factor split. The new AA4-W theorem is their COMPLETE combined seven-tag/51-palette exact transfer and includes the C/A, C/B, B/B-overlap and B/B-disjoint classes with one FULL random global source map. It does **not** improve the worst-case infimum quantifier.

## 4. ALSO new exact BOTH-full-global-uniform full seven mean (all h, source census input)

Let \(U_F(s)\) denote the TRUE source-only number of six-DISTINCT original incidence Q in cell F. All other source profile Q are irrelevant to the selected seven tags. Sample one uniform complete f and an **independent** one uniform complete g. The two global typed maps are independent of each other, though for each type all Q share ONE global map. Thus the exact all-h expression is:

\[
\begin{aligned}
\mathbb E_{f,g} S_s
={}&60p_H^2 U_{AA}
+p_Ap_B(U_{AB}+U_{BA})
+p_Ap_C(U_{AC}+U_{CA})\\
&+p_Bp_C(U_{BC}+U_{CB})
+p_B^2(U_{BB\text{-overlap}}+U_{BB\text{-disjoint}}).
\end{aligned}
\]

The exact seven individual expected tag populations and weighted 51-palette numerator are obtained by tagging each term and multiplying by the certified \(w_{\rm tag}\). This formula is exact for every genuine W(3,s), h≥1, with its *actual* source universe \(U_F(s)\). It is NOT a closed all-h count for all nine \(U_F\) by itself; the physical coefficient theorem is independent of a complete source-geometry enumeration at large h. No fitting a finite source census to all h is performed.

For genuine original W(3,2), AA4-U's independently exhaustively counted ALL C(45,6)=8,145,060 original six-Q provides the nine exact original source universe populations:

| SOURCE only forest cell | True W32 six-Q count |
|---|---:|
| A/A | 1,566,360 |
| A/B, B/A | 1,666,980 each |
| A/C, C/A | 6,225 each |
| B/C, C/B | 5,220 each |
| B/B-overlap | 910,080 |
| B/B-disjoint | 707,580 |

Substitution yields the **NEW complete seven-tag BOTH-full-global-uniform expectation**

\[
\mathbb E_{f,g}D6=\frac{3\,759\,264}{1\,002\,001},
\qquad
\boxed{\mathbb E_{f,g}S_s=\frac{165\,129\,984}{1\,002\,001}
\approx164.8002\quad (s=2).}
\]

This number is for **two independent UNIFORM COMPLETE globally injected typed maps** and is NOT equal to the actual selected full seven count of either S68 (68), S72 (72), lex (259), or reverse (169). In particular it is NOT an all-global adversarial minimum.

## 5. True original W32 independent tests and exact-head reproducibility

The research executable works on the actual W32 45 immutable original source flags with the strict original GQ nonincident point-line unique-anchor axiom and complete K6 pair-image typed injections. For EACH of original S68/S72/lex/reverse:
1. Build the 62,370 point or line physically valid ORIGINAL Q once from the corresponding complete globally injected typed map.
2. For every Q classify BOTH actual ORIGINAL point and line factor multiplicity profiles, including B/B overlap versus disjoint; exclude and COUNT Q outside the nine BOTH-source feasible cells. Do not conflate one-half candidate populations with dual source universes.
3. Among actual AA source Q with physical fixed-side A classify connected positional H versus disconnected two triangles on immutable Q positions.
4. Compute exact Fractions for ALL SEVEN per-class expected counts, total selected seven S and weighted 51-palette numerator, for any fixed global point map f averaging uniform complete line g, and vice versa.
5. Separately check the single **specified** true global f,g pair using AA4-Q original same-six-Q physical two-sided join and the historical original seven-GF5 classifier. Never claim actual selected S equals the expected S.
6. Require exact invariance of the conditional expected seven-vector when ONLY the random-target original factor labels in the specified fixture are replaced by independent seeded complete full-global image permutations. Repeat with typed factors reversed.
7. Use independent actual K6 physical pattern enumeration, a fake regular source host with original C6 but no true GQ unique anchors, and non-injective physical pairs as negative controls.
8. Check the W32 source-only full-nine census expectation rational as a fixed regression independent of the f,g conditional fixture values.

The source code and tests use pure standard Python 3.12 integer combinatorics/Fraction, with no per-Q independent artificial labeling, no numeric approximations in proofs, no local W32-to-infinity statistical inference. Three dedicated GitHub-hosted jobs, plus INDEX, Proof Audit and full Research, must succeed at the exact final child HEAD. A green automated CI is NOT an external mathematical review.

### Verified exact fixed-side W32 conditional versus actual seven-GF5 scores

The first hosted TRUE ORIGINAL W32 jobs S68 and S72 passed full independently recomputed Q-tag and 51-palette GF5 checks. These exact rational results are conditioned on one original factor type's **entire fixed global injection**:

| Genuine original W32 fixed map | Exact expectation of seven S with OTHER entire map uniformly random | Actual S under the specified OTHER complete global map | Fixed AA-connected original Q |
|---|---:|---:|---:|
| S68: fix complete point map f, random complete line g | 870476/5005 ≈173.92 | 68 | 21,186 |
| S72: fix complete point map f, random complete line g | 870476/5005 ≈173.92 | 72 | 21,186 |
| S68: fix complete line map g, random complete point f | 162908/1001 ≈162.75 | 68 | 18,310 |
| S72: fix complete line map g, random complete point f | 818106/5005 ≈163.46 | 72 | 18,616 |

Every number is from the same source-exact 45 original incidences, not artificially independent sixset projections. The conditional f-fixed expectations coincide for S68 and S72 because their FIXED complete point map and source-half forest data are the same; their ACTUAL seven S differ because their specified complete right global line images differ. That is an explicit finite genuine-original example of the precise **probabilistic-vs-adversarial quantifier separation**. All four exact fractions are frozen as independent regression test golden values; they must remain separate from actual full seven S and from the both-random-global expectation 165129984/1002001.

## 6. Scope, RCP retention, and next deterministic compensation gate

**What this result closes:** a seven-tag all-h first-moment/weighted-GF5 **bookkeeping** gap between true source-forest marginal populations and physical pair-image injection probabilities. It yields reference values against which a proposed coupled deterministic JPKC/EICE positional all-f,g lower can be audited.

**What it does NOT close:** the missing \(\inf_{f,g}S_s(f,g)=\Omega(s^6)\) deterministic all-label bound. A fixed-side positive expectation cannot be reversed to \(\forall\) opposite maps. The AA4-V genuine ORIGINAL S68/S72 positional thresholds are negative while those maps have positive selected S only through separately correlated non-AA. No universal \(\mathrm{Var}(S)\), lower-tail probability, concentration or joint positive minimax is proved here. The CYC PR #492 analyzes D6, not the entire seven-class S, and should not be duplicated or retargeted.

**Next AA4-X candidate:** seek a genuinely deterministic source-physical coupling inequality relating the nine original source-forest \(n_F(f)\) populations, Hall/JPKC three-anchor compatibility, EICE internally blocked GQ 2×2 plaquettes, and the AA4-V common positional dual signatures for two **adversarial** globally coherent physical injections. Independently falsify proposed components on S68/S72 and globally injected random maps before any all-h leap. A conditional expected all-seven vector by itself is NEVER the missing lower.

**Integration:** Keep this child stacked Research Draft, do not merge into main or close HYP-105 #230. Once scientific review is granted, register immutable SHA-pinned quantifier-correct proof and formulas in RCP-001-E JSON claim/formula DAG sources and regenerate the five version-controlled derived Markdown registry files. Do not hand-edit generated docs or confuse the separate PR #492 branch with this source-forest/positional branch.
