# HYP-105 G5-E2-B3.1-B1 — complete five-versus-six physical-coordinate GF(5) flow class

Date: 2026-10-10. Parents [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169). The preceding [B3.1-A](HYP-105-G5-E2-B3-B1-CRITICAL-FLOWS.md) classified only **6+6** two-factor physical-coordinate projections. [B3.2-D](HYP-105-G5-E2-B3-D-JOINT-RISK.md) gives distinct four-column (Q_4) risks and exact seven-column weighted checks. This slice classifies a genuinely **different, 5+6 / 6+5 coordinate** six-column family.

**ALL-h FIXED-LABEL NECESSARY R3 FLOOR FOR RESTRICTED FACTOR-MATCHED 5×6/6×5 / EXACT 2100 FINITE TEMPLATE EVALUATIONS / THREE K5 GRAPH TYPES / INDEPENDENT FULL-GF5 51³ MITM / CLASSICAL CHARACTER ORTHOGONALITY / NO OTHER DEGREE PROFILE COMPLETENESS / NO ALL-h FULL-R3 UPPER / NO NEW ASET POWER.**

## 1. Precisely frozen mathematical setting

Let (s=2^h), (h\ge1), and let (G_s=W(3,s)) be the classical symplectic generalized-quadrangle incidence graph, with (V=(s+1)(s^2+1)) point and (V) line vertices, (N=V(s+1)) factor edges and degree \(\Delta=s+1\). Independently of how the two injective physical pair label maps \(f:P\to\binom{[a]}2\) and \(g:L\to\binom{[a]}2\) were chosen, select six factor-incidence edges **forming a factor matching**, i.e. all six point and six line endpoints are distinct. Then each physical coordinate half has six *distinct* unordered pair-edges, one per selected column, each local physical column has two coordinates from each half, and every column uses independent uniformly chosen full-nonzero checksum4 weights in GF(5) from its 51-pattern palette.

For a selected six-factor-matching define \(U_{5,6}(f,g)\) as the number of unordered six-edge sets with:
- exactly five touched **left** physical coordinates and minimum touched degree at least two;
- exactly six touched **right** physical coordinates and minimum touched degree two.

Define \(U_{6,5}\) by swapping the coordinate blocks, and \(U_{56}=U_{5,6}+U_{6,5}\). The two conditions are mutually exclusive on a given six-edge set. In each class **every** one of the ten unordered balanced 3-versus-3 sign partitions has a strictly positive exact GF(5) flow count. The values of \(U_{56}\) for arbitrary real GQ labelings have NOT been computed, bounded from below uniformly, or claimed to be nonzero.

## 2. Complete combinatorial reduction for this class

Six distinct pair-edges on *five* touched physical coordinate vertices of minimum degree two must form one of **three** graph isomorphism types. Exhaustively enumerate all \(\binom{\binom52}{6}=210\) edge sets in \(K_5\), reject sets not touching all five vertices with all degrees \(\ge2\), then quotient by all \(5!=120\) physical vertex permutations. Exactly **85** edge sets remain, and their three unlabeled types have **15, 60 and 10** labeled physical-coordinate images. Their degree multisets are one (4,2,2,2,2) type and two (3,3,2,2,2) types.

On the other side six distinct pair-edges occupying exactly six touched physical vertices, each degree two, necessarily form a simple two-factor \(C_6\) or \(C_3\sqcup C_3\). On the six **named column vertices**, physical coordinates are dual edges between the two columns touching each coordinate. There are exactly **70** two-factors: 60 labeled \(C_6\) and 10 labeled two-triangle graphs. Balanced signed 3v3 partitions modulo global sign reversal have **10** types.

Fix the lex-sorted physical edge order of ONE representative of each of the three left \(K_5\) graph types as column names 0..5. For each of 70 labeled right two-factors on these column names and each of ten normalized balanced sign masks (column0 positive), reconstruct the true six physical split-2+2 supports and count the exact GF5 flows. This gives **3×70×10 = 2,100 complete covering representative configurations**. They are **not** claimed to be 2,100 pairwise nonisomorphic sign/color orbits; redundancies under automorphisms of the fixed left graph are harmless for proving minimum positivity. An arbitrary physical 5x6 image is mapped to one such template by independently relabeling the physical coordinate symbols within each half and permuting the six column IDs. Swapping the two color blocks covers 6x5.

This exhaustiveness concerns **only** the five-versus-six profile with all six factor endpoints distinct on each side and physical minimum degree two. It does NOT exhaust 5x5, 4x6, repeated factor endpoint, or other six-column motifs, or the 11,663 abstract factor-forest shapes.

## 3. Exact GF5 integer Fourier dual formula, independent of 51³ meet-in-middle

For each of six columns \(i\), four coefficient incidences \(w_{ic}\in\mathbb F_5^*\) satisfy

\[
 \sum_{c\in S_i}w_{ic}=4\quad(\mathrm{mod}\ 5).
\]

For a balanced choice of signs \(\varepsilon_i\in\{+1,-1\}\) with \(\sum_i\varepsilon_i=0\), every physical coordinate \(c\) must satisfy \(\sum_{i:c\in S_i}\varepsilon_iw_{ic}=0\). The desired count \(F(S,\varepsilon)\) counts all \(51^6\) potential local weight choices satisfying these equations. Let \(C\) be the number of touched physical coordinates, and let \(\zeta=e^{2\pi i/5}\). By orthogonality of the five additive characters,

\[
 F=5^{-(6+C)}\sum_{\lambda\in\mathbb F_5^6,\,\mu\in\mathbb F_5^C}
 \zeta^{-4\sum_i\lambda_i}
 \prod_{(i,c)}\left(4\,\mathbf1_{\lambda_i+\varepsilon_i\mu_c=0}
                   -\mathbf1_{\lambda_i+\varepsilon_i\mu_c\ne0}\right).
\]

Sum first over each \(\mu_c\). Writing \(r_i=-\varepsilon_i\lambda_i\), and \(n_t=\#\{i:c\in S_i,\,r_i=t\}\) for \(t\in\mathbb F_5\), the exact integer local factor is

\[
 \Phi_c(\lambda)=\sum_{t\in\mathbb F_5}4^{n_t}(-1)^{d_c-n_t},
 \qquad d_c=\#\{i:c\in S_i\}.
\]

Because \(\sum_i\varepsilon_i=0\), shifting \(\lambda_i\mapsto\lambda_i+u\varepsilon_i\) leaves every local factor and \(\sum_i\lambda_i\) invariant. Fix \(\lambda_0=0\), gaining exactly a factor 5. Scaling all remaining \(\lambda_i\) by a common nonzero scalar preserves all \(\Phi_c\). The nonzero scalar orbit sums over the additive characters to **4 if \(\sum\lambda_i=0\)** and **−1 otherwise**, while the zero orbit contributes **1**. Therefore

\[
 \boxed{F(S,\varepsilon)=5^{-(5+C)}
  \left[\prod_c\Phi_c(0)+
  \sum_{\substack{\lambda_0=0,\,\lambda\ne0\\
                    \text{one representative of each }\mathbb F_5^*\text{ orbit}}}
     \big(4\mathbf1_{\sum\lambda_i=0}-\mathbf1_{\sum\lambda_i\ne0}\big)
     \prod_c\Phi_c(\lambda)\right].}
\]

There are exactly \(1+(5^5-1)/4=\mathbf{782}\) integer-only evaluations per signed template. The program checks **integer divisibility** by \(5^{5+C}\) and the absolute probability bound \(0\le F\le51^6\); it never uses floating-point complex arithmetic or infers positive flow from an incomplete graph topology gate. This finite-field character computation is a classical orthogonality technique specialized to the six-column checksum model, not a newly claimed general theorem.

The existing, algorithmically independent \(51^3\)-per-side GF5 meet-in-middle oracle cross-checks multiple genuine 5x6 signed representatives, the prior twelve-edge C6/C6 prescribed-boundary inclusion-exclusion cross-checks the older class, and permutation/sign/half-swap tests check equivalence.

## 4. Exact finite classification and all-h consequence

The independent 2,100 representative computations return **positive flow in every case**, with the following fixed minimum and maximum numbers of admissible GF5 coefficient assignments:

| K5 physical graph type (lex canonical edge representation) | K5 labeled images | Signed template cases | Minimum F | Maximum F |
| --- | ---: | ---: | ---: | ---: |
| Four-degree center with two attached triangles | 15 | 700 | **14,400** | **17,955** |
| First nonisomorphic (3,3,2,2,2) graph | 60 | 700 | **10,950** | **12,357** |
| Second nonisomorphic (3,3,2,2,2) graph | 10 | 700 | **11,685** | **12,405** |

Thus the complete 5x6/6x5 class has an **exact universal minimum \(F\ge10,950\)** for every one of ten balanced sign partitions. This is an exact *finite-template lemma* holding for the physical 5+6 pattern embedded in **ANY \(W(3,2^h)\)**, every \(h\ge1\), and every injective point/line pair labeling. Since distinct six-factor-matchings define distinct unordered signed risk events, all corresponding GF5 terms are nonnegative and disjoint in the sum defining \(R_3\). The all-h necessary bound is

\[
 \boxed{R_3(B_s(f,g))\ \ge\ \frac{109{,}500}{51^6}\,
             U_{56}(f,g).}
\]

The lower bound is useful **only if** \(U_{56}\) can itself be controlled from below for a particular fixed labeling, which is not known. It is not an upper bound on \(R_3\) and does not close HYP-105.

## 5. Exactly what the independent random model predicts

For each six-factor matching, independent uniformly random injections of left and right factor vertices into the same abstract pair palette \(K=\binom a2\) give exact probabilities

\[
 p_5=\frac{510(a)_5}{(K)_6},\qquad
 p_6=\frac{70(a)_6}{(K)_6}.
\]

The **510** and **70** coefficients coincide exactly with the previously accepted [B3.0 leafless six-edge projection polynomial](HYP-105-G5-E2-B3-FOREST-PROJECTION.md) for multiplicity profile \((1,1,1,1,1,1)\), providing an independent provenance cross-check. Let \(M_6(G_s)\) denote the exact number of factor six-matchings. The left/right projections are independent, and swapping their sizes gives disjoint events:

\[
 \mathbb E[U_{56}]
  =2M_6(G_s) p_5p_6.
\]

The known greedy bound \(M_6\ge\prod_{j=0}^{5}(N-2j\Delta)/6!\) gives
\(\mathbb E[R_3]\ge (109500/51^6)\mathbb E[U_{56}]
   =\Omega(s^{9/2})\) **for random independent labels only**. This is **subleading** to the already accepted \(\Omega(s^6)\) random-label lower obstruction from the 6+6 matching core. No improvement or conflict with the accepted random upper \(O(s^6)\) is claimed.

## 6. Explicit evidence and remaining gates

[Source/oracle](../../research/hyp105_g5e2b3b1b_five_six_flows.py) · [independent tests](../../research/test_hyp105_g5e2b3b1b_five_six_flows.py).

This is **B3.1-B1**, not a false claim of completing **B3.1-B**:
- Still open: **5×5**, **4×6**, **4×5**, smaller leafless coordinate profiles, repeated original factor endpoints, and their exact GF5 signed-flow positivity/counts. The 631 top-degree **random projection exponent** shapes from B3.0 need separate matching to actual GF5 motifs; this slice does not classify them.
- Still open: number of such positive motifs on the **same specific geometry-aware labeling** as HYP-105 B3.2-D, and a deterministic all-h upper for total \(R_2\) **and** total \(R_3\).
- All-h impact: a new restricted fixed-label *lower* obstruction, not an improved ASET lower exponent, not an original general Fourier counting identity, no use of Rust. Keep root issues OPEN. Next **B3.1-B2**: analyze 5×5 by color-symmetric graph pair orbits and/or factor-endpoint repetitions, then B3.2-E common-label upper gate.
