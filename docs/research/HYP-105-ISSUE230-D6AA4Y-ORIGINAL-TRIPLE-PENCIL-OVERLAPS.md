# HYP-105 / issue #230 — D6-AA4-Y-SRC: exact ALL-h original GQ triple-pencil collision enumeration and selected GF5 contribution

**Scope and integration.** Research-only strict stacked child of [D6-AA4-X-SRC #496](https://github.com/definitely-stable/Mathlab/pull/496), pinned parent HEAD \`6ea96e58d029700f5db95ebf18ba8431ac1725d5\`. Genuine ORIGINAL symplectic GQ W(3,s), s=2^h (h>=1), with its V=(s+1)(s²+1) points and V lines, d=s+1 incident original neighbors per source vertex and source incidence graph girth eight. Source sixsets mean **SIX DIFFERENT actual original point–line incidence IDs**, never locally fabricated or independently resampled. HYP-105 Root A/B/C #230 remains OPEN. Separate [AA4-Y-CYC #497](https://github.com/definitely-stable/Mathlab/pull/497) is performing finite globally correlated swaps; this independent source-theory slice does not duplicate it.

## 1. NEW all-h exact A/C and C/A ORIGINAL source six-incidence capacities

A source A/C six-Q uses six distinct genuine original points (A=(1^6)) and exactly three distinct genuine original lines, each appearing twice (C=(2,2,2)). Its source incidence graph is a disjoint union of three genuine two-edge line-centered paths. The three repeated original source line centers are **unordered**, and at each source line choose an unordered pair of two distinct original incident source points. To satisfy point source type A, all six selected original source points must be different.

For three distinct original source lines L1,L2,L3, an unordered pair of source lines meets in at most ONE original point (GQ original partial linearity). If all three source-line pairs meet at three different original points, the original source incidences give a SIX-CYCLE. This cannot occur in a genuine generalized quadrangle (girth eight). Consequently exactly four and only four source triple types exist:
- **0** intersecting pairs, three pairwise disjoint original line centers.
- **1** intersecting pair of original lines.
- **2** intersecting pairs at TWO distinct original source points, with one middle line meeting the two others.
- **3** intersecting pairs — necessarily all THREE lines concurrent at ONE common original point (not a prohibited original source triangle).

Write \(V=(s+1)(s^2+1)\), \(d=s+1\), \(q=\binom d2\), \(r=d-1\). The four EXACT counts of unordered actual original line-center triples, depending only on original GQ regularity and girth eight, are

\[
\begin{aligned}
N_3 &= V\binom d3,\\
N_2 &= V\binom d2(d-1)^2,\\
N_1 &= V\binom d2(V-2)-2N_2-3N_3,\\
N_0 &= \binom V3-N_1-N_2-N_3.
\end{aligned}
\]

Proof: each meeting pair of original lines is uniquely rooted at its one original source point, so exactly \(V\binom d2\) meeting pairs exist. Summing over all line triples, the number of meeting-pair occurrences is \(V\binom d2(V-2)=N_1+2N_2+3N_3\). A two-meeting triple has a UNIQUE center original line and TWO distinct original points along that line; selecting its two distinct points and one of the \(d-1\) other lines through each gives \(N_2\), and the third pair cannot meet due to source girth eight. Three-meeting triples have all three source lines concurrent, counted as \(N_3\). Subtraction gives \(N_1,N_0\). No independence assumptions are used.

## 2. NEW exact finite collision correction for six different original source points

For each fixed unordered triple of distinct original source lines, choosing two unordered actual original points from each line gives \(q^3\) potential selections *before* enforcing source point type A. Every pairwise meeting of original lines can produce an inadmissible six-Q only if both selected original line-neighbor pairs contain their shared actual source point.

By explicit inclusion-exclusion, the number of **admissible pair-of-original-neighbor selections per fixed source line triple** is:

\[
\begin{aligned}
W_0&=q^3,\\
W_1&=q^3-r^2q,\\
W_2&=q^3-2r^2q+r^2,\\
W_3&=q^3-3r^2q+2r^3.
\end{aligned}
\]

The \(+r^2\) in \(W_2\) is the intersection of two collision events at two DIFFERENT original points of their central line. Both points must be selected, uniquely filling its selected neighbor pair. For \(W_3\), every collision uses the SAME concurrent original point, pairwise event intersections and the threefold event intersection all have \(r^3\) selections, yielding total \(+2r^3\). This handles the genuine high-correlation triple concurrency and rejects a false independent-pencils model.

Every actual ORIGINAL A/C six-Q determines exactly one unordered triple of its three twice-repeated line sources and one pair of its distinct point neighbors per source line. Thus no overcounting, and we obtain for **every** \(h\ge1\):

\[
\boxed{
U_{A/C}(s)
=\sum_{j=0}^{3}N_j W_j.
}
\]

Under point↔line duality of genuine W(3,s), the dual source C/A cell is exactly equal:

\[
\boxed{U_{C/A}(s)=U_{A/C}(s).}
\]

This is a full all-h source-only formula. It does not assert these original source Q are physically accepted by arbitrary f,g; there is still the AA4-U adversarial physical intersection obstruction.

### Exact genuine W32 and W34 identities

| True source GQ | N0 | N1 | N2 | N3 | W0 | W1 | W2 | W3 | U_A/C = U_C/A |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| W(3,2) | 80 | 180 | 180 | 15 | 27 | 15 | 7 | 7 | **6,225** |
| W(3,4) | 43,520 | 40,800 | 13,600 | 850 | 1,000 | 840 | 696 | 648 | **87,808,400** |

For W(3,2), the independent source-only AA4-U census of all \(\binom{45}6=8,145,060\) actual original six-incidence sets yields U_A/C=U_C/A=6,225 exactly. A SECOND completely independent brute-force original W32 source oracle enumerates all \(\binom{15}{3}=455\) original line-center triples and all their \(3^3=27\) possible actual original point-neighbor choices, accepting iff all SIX actual source points are different. It recovers the four cell contributions 2,160, 2,700, 1,260, 105.

For W(3,4), the independent code enumerates ALL \(\binom{85}{3}=98,770\) genuine original line-center triples directly from the TRUE 425 original incidences, checks actual source point-neighbor intersections, rejects any source three-meetings at three different point IDs and identifies all four source triple classes with their exact theoretical counts. For a separately sampled root-triple subset, it independently brute-forces all neighbor 2-subset combinations to check each W_j. There is **no** claim of a complete \(\binom{425}6\) six-source set enumeration.

The actual original GQ finite checks require the full unique nonincident point-line projection axiom, not simply regularity or absence of source C4. A deliberately fake 15+15 degree-three regular source graph with forbidden GQ C6 and a globally noninjective physical map both fail closed.

## 3. NEW exact true-original selected seven GF5 C/A expectation — ALL h

Use the independently established AA4-W exact physical source-factor response probabilities for **one uniformly sampled COMPLETE globally injected typed ORIGINAL point map f** and an independent **one uniformly sampled COMPLETE globally injected typed ORIGINAL line map g**, SHARED across every genuine original six-Q:

\[
p_A=\frac{70(a)_6}{(K)_6},\quad
p_C=\frac{(a)_6}{8(K)_3},\qquad
K=\binom a2\ge V,\quad a=\min\{b:\binom b2\ge V\}.
\]

The original A/C Q require physical A on original points and physical C on original lines; dual C/A require physical C on original points and physical A on original lines. Because **f and g are mutually independent by type**, for any one FIXED original Q the joint physical acceptance probability is \(p_Ap_C\); because each type uses ONE global map over all Q, within-type Q events are correlated and no independence across Q is assumed. Linearity of expectation gives for ALL genuine W(3,s):

\[
\boxed{
\mathbb E_{f,g}N_{C/A}^{\mathrm{selected}}
=2U_{A/C}(s)\,p_Ap_C.
}
\]

(Here \(N_{C/A}^{\mathrm{selected}}\) is the ONE pooled historical selected GF5 C/A tag, joining both source orientations.)

Exact rational complete-global-both-uniform examples:
- True W(3,2): \( \mathbb E N_{C/A}=74700/13013\).
- True W(3,4): \( \mathbb E N_{C/A}=202837404000/9877487\).

Both are STRICTLY ensemble results. W32 is independently compared with AA4-W's previously proven full seven historical GF5 original Q ensemble vector and immutable selected 51-palette coefficients. No implication for \(\inf_{f,g}S_s(f,g)\) follows; actual complete globally injected S68/S72 have very different selected seven S despite positive expected selected GF5 count.

### Exact new asymptotic selected GF5 leading constant

The source triple formula has

\[
U_{A/C}(s)=\left(\frac1{48}+o(1)\right)s^{15}.
\]

From the minimal physical coordinate pair alphabet \(a\sim\sqrt2\,s^{3/2}\), AA4-W's response satisfies \(p_A=(560+o(1))s^{-9}\), \(p_C=1-o(1)\). Therefore

\[
\boxed{
\mathbb E_{f,g}N_{C/A}^{\mathrm{selected}}
=\left(\frac{70}{3}+o(1)\right)s^6.
}
\]

Combine with the distinct two historically accepted source classes covered in AA4-X-SRC:
- selected C/B expectation \(=(6+o(1))s^6\);
- selected B/B-overlap expectation \(=(24+o(1))s^6\).

The three selected GF5-positive original tags are distinct and add without duplication. Thus a NEW precise complete-global ensemble theorem for **three of the seven historical selected positive classes** is

\[
\boxed{
\mathbb E_{f,g}\big[N_{C/A}+N_{C/B}+N_{B/B\text{-overlap}}\big]
=\left(\frac{160}{3}+o(1)\right)s^6.
}
\]

The W32 exact three-tag total is \(\frac{14\,976\,180}{1\,002\,001}\). This is a first moment over TWO independent UNIFORM COMPLETE global typed injections, not a worst-case deterministic lower, not the full seven S leading constant, and not a 51-palette GF5 R3/ASET theorem. The other four selected source/GF5 sectors remain separate, nonnegative and uncomputed by this particular new closed source formula.

## 4. Scope, proof boundaries, acceptance and next stage

**ALL-h source theorem:** exact true ORIGINAL GQ line-center triple types, collision-corrected six-point selection and source A/C,C/A population. **ALL-h expectation theorem:** exact both-complete-global-uniform GF5 C/A tag and exact sum of three historically accepted GF5 tags, with rational W32/W34 values and asymptotic leading constant. **Finite-independent verification:** complete genuine W32 original full sixset source comparison, independent complete genuine W32 line-center+actual neighbor-pair brute force, complete genuine W34 original center-triple 98,770 enumeration and sample brute-force point-neighbor assignments, counterfeit GQ/noninjective fake rejection. Only actual original point-line incidence IDs used; physical labels not used in source count.

What is NOT proven: any statement requiring an adversarial fixed pair of globally injected maps f,g to have selected positive C/A; an all-h deterministic \(\inf_{f,g}S_s=\Omega(s^6)\); a full selected seven-GF5 asymptotic constant; a full GF5 R3 exponent; an infinite counterfamily. In particular root #230 remains OPEN.

This child adds exactly four additive files: the mathematical Python source/certifier, 10-test independently checked suite, this proof Markdown with exact source/GF5 tables, and a GitHub-hosted-only three-job dedicated workflow. Require final-exact-HEAD dedicated, INDEX, Proof Audit and FULL Research SUCCESS plus separate independent mathematical peer review. No merge to main or root scientific acceptance from automated CI alone.

**Next AA4-Z-SRC candidate:** count the remaining source six-path forest cells A/A (six genuine source incident pair matchings), A/B & B/A (one two-edge path plus four isolated source original incidence edges), B/B-disjoint (two disjoint two-edge paths + two isolated original incidence edges) to obtain the WHOLE seven-class source-only all-h ensemble baseline, using genuine GQ high-girth matching and source path-girth identities. But scientific priority remains a truly deterministic source/physical positional Hall/JPKC/EICE compensation theorem for every globally injected f,g, not more independent-ensemble expectations. A future source-complete ensemble reference is useful only as a falsification and quantitative benchmarking tool. Retain SHA-pinned mathematical source statements in the RCP-001-E source JSON claim/formula/evidence ledger and regenerate its five permanent Markdown documents after independent review; do not hand-edit generated Markdown.
