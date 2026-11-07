# HYP-105 / #230 — AA4-GF5TREE: independent ORIGINAL six-ID GF(5) proof by spanning-tree flows

**Status:** Scientific Draft, strictly stacked on the frozen original-source six-ID inverse referee [#734](https://github.com/definitely-stable/Mathlab/pull/734), exact parent HEAD e6db5514d2abaa9aea1262063d680594d6d79a41. **Scope:** the GF(5) coefficient of an individual **genuine ORIGINAL W(3,2^h)** six-incidence-ID D6 or B/B-overlap configuration, for arbitrary fixed complete separately globally pair-injective, arbitrarily correlated physical maps f,g. NO assertion of how many such configurations exist for all maps. No merge, no main/parent changes, no root #230 acceptance, no ASET exponent.

This is an independent third mathematical route to the previously accepted class-specific GF(5) coefficient floors: it uses neither the historical 782-state dual-Fourier oracle, nor the old inclusion-exclusion method, nor the numerical spectrum of the finite W32/W34 examples. The main module imports only the **original GQ source constructor** for actual finite witnesses, never the historic GF(5) evaluator or seven-family classifier. A separate TEST compares its output with the historic Fourier algorithm, and a separate FULL-PALETTE 51³-by-51³ meet-in-the-middle oracle checks direct weight counts.

## 1. Precise signed GF(5) event on six named ORIGINAL flags

Let \(i_0,\ldots,i_5\) be SIX DISTINCT actual original point–line incidence ID flags on genuine symplectic \(W(3,s)\), \(s=2^h\), with globally injected point and line pair-label maps f,g fixed together. Each source ID \(i\) has an actual four-position split physical support \(S_i=f(p_i)\sqcup (a+g(\ell_i))\), where a is the original alphabet size. For every support coordinate c its GF(5) entry \(w_{i,c}\) is in \(\mathbb F_5^\times=\{1,2,3,4\}\). A physical column is valid exactly when

\[
\sum_{c\in S_i}w_{i,c}=4\pmod5.
\tag{G1}
\]

The independently recomputed local 4-position palette is **51** distinct rows: of the 4³ arbitrary choices for the first 3 entries, the fourth is forced by (G1), and 13 of those choices force zero. Thus 51 admissible local rows per original incidence column.

For an unordered balanced \(3+3\) sign partition \(\varepsilon=(\varepsilon_i)_{0\le i<6}\), with three plus and three minus, the source event is

\[
\sum_{i:c\in S_i}\varepsilon_i w_{i,c}=0\pmod5
\quad\text{for every touched physical coordinate }c.
\tag{G2}
\]

There are exactly \(\binom{5}{2}=10\) unordered balanced signs (choose the side containing column 0). The associated exact integer weight \(F(S,\varepsilon)\) counts all 51⁶ independent palette choices satisfying (G2). The corresponding event probability is \(F/51^6\). No randomization of f,g is assumed or used.

## 2. NEW all-order graph-to-flow exact identity (no Fourier)

For an original source D6 or B/B-overlap sixset, **every** physical coordinate touched on each of the two typed sides occurs in exactly TWO of its six named original columns. Thus its total twelve distinct physical coordinates form the edges of a **4-regular undirected multigraph** \(\Gamma\) on SIX vertices labelled by the actual original source-column IDs (in the chosen order). A repeated factor pair produces two distinguishable parallel physical-coordinate edges, NEVER one collapsed physical edge. There are precisely 12 graph edges and four edge incidences at every column vertex.

Choose any orientation for each dual multigraph edge e=uv. The two original nonzero entries at its physical coordinate obey \(\varepsilon_u w_{u,e}+\varepsilon_v w_{v,e}=0\). Put \(t_e=\varepsilon_u w_{u,e}\) when u is the positive end of the chosen orientation. Then \(t_e\in\mathbb F_5^\times\) and the other endpoint has oriented contribution \(-t_e\). Multiplying (G1) by the sign \(\varepsilon_i\) produces the prescribed boundary equation

\[
\boxed{B_\Gamma t=b,\qquad b_i=4\varepsilon_i\pmod5,\qquad
t_e\in\mathbb F_5^\times\text{ for all 12 physical coordinate edges}.}
\tag{G3}
\]

The map from all six admissible original GF(5) 51-palette rows satisfying (G2) to a solution t of (G3) is a **BIJECTION**, including the correct treatment of parallel coordinates and every original source ID.

For any spanning forest T of \(\Gamma\) with c connected components, the \(12-(6-c)=6+c\) chord values are freely chosen in \(\{1,2,3,4\}\). The remaining 6-c tree-edge values are **uniquely** determined by (G3): eliminate tree leaves from the boundary residual; if a forced edge value is zero reject, otherwise continue. A component has any solution only if the sum of its boundary demands vanishes modulo five.

Therefore the following exact, all-order, elementary counting theorem holds, without any statistical hypothesis or Fourier transform:

\[
\boxed{
F(S,\varepsilon)=
\sum_{t\in(\mathbb F_5^\times)^{E\setminus T}}
\mathbf1\{\text{every uniquely forced tree edge is nonzero and all
component balances hold}\}.}
\tag{G4}
\]

The source code implements only (G4), with precise \(\mathbb Z\)-arithmetic and modulo-five residues. For connected D6/BBo dual graphs, c=1 and the entire sum has only \(4^7=16\,384\) assignments, rather than \(51^6\). The proof is independent of h, source label names, f/g correlation, and ORIGINAL core/deletion selection.

## 3. Complete original B/B-overlap dual template theorem: NINE shapes × TEN signs

An actual B/B-overlap six-ID original source motif has a unique repeated ORIGINAL point p, a unique repeated ORIGINAL line ell and exactly ONE shared original incidence flag at their intersection. Its first typed factor uses the same physical f(p) pair twice (two distinct physical coordinates, hence two dual parallel edges) and four other distinct original point-pair edges forming a simple physical C4. Dually, the second factor repeats g(ell) and has a C4 on the other four source-column IDs. The doubled source-column pair on the first side and on the second intersect in precisely one common **ORIGINAL incidence flag**, not merely a physical coordinate.

Simultaneously rename the six original flags so the shared incidence ID is 0, the other point-repeated incidence is 1, and the other line-repeated incidence is 2. The source-column dual graph has:

* first factor: TWO distinguishable parallel edges 0–1 plus one of exactly THREE simple C4 graphs on source-column vertices {2,3,4,5};
* second factor: TWO distinguishable parallel edges 0–2 plus one of exactly THREE simple C4 graphs on vertices {1,3,4,5}.

This gives EXACTLY 3×3=9 graph templates, with NO additional possible original source topology under the stated globally pair-injective complete f,g. The 10 balanced signs for each cover precisely 90 signed events; relabeling actual source IDs or physical coordinate symbols cannot change their GF(5) flow counts. This is a finite **template classification theorem for every dyadic h**, not an inference from small h data.

The independent non-Fourier algorithm returns:

\[
\boxed{
\begin{aligned}
\min_{\text{9 BBo templates, 10 signs}}F&=5175>0,\\
\min_{\text{9 BBo templates}}\sum_{\varepsilon}F&=53526,\\
\max_{\text{9 BBo templates}}\sum_{\varepsilon}F&=53838.
\end{aligned}}
\tag{G5}
\]

Of the nine graph templates, six have sum 53526 and three have sum 53838. Every single one of their 90 GF(5) events is positive. The full 90-event table, SHA-256 reproducibility digest and four direct-palette crosschecks are preserved in the mandatory GitHub-hosted machine certificate. These figures coincide with, but are NOT imported from, the older accepted GF(5) floor.

**New quantitative application relative to the older conservative per-sign product:** for EVERY genuine positive ORIGINAL B/B-overlap sixset (whether or not it has a physical 3-path realization, and also after deleting an arbitrary set Z of source IDs it does not meet),

\[
\boxed{
\sum_{\varepsilon}F(S,\varepsilon)\ge53526
>10\cdot5175=51750.
}
\tag{G6}
\]

This is a stronger uniform TEN-SIGN weight than multiplying the minimum per-sign weight by ten. It refines the class floor but does not create additional original six-ID motifs.

## 4. D6 exact original aligned C6 case

For the ORIGINAL D6 sixset, both factor column-duals are the SAME connected simple C6 on the six named source IDs, with six parallel physical-coordinate pairs across the two typed factors. Simultaneously relabel the six original IDs around the factor cycle as 0,1,2,3,4,5. Up to this relabeling there is one dual graph template. The ten exact unordered balanced signed weights in the program's fixed canonical sign order are

\[
(5265,5454,5454,5265,5454,5643,5454,5454,5454,5265).
\]

The designated alternating sign on source-column positions 0,2,4 has weight exactly 5643. Over ALL ten signs the exact integer sum is

\[
\boxed{\sum_{\varepsilon}F(D6,\varepsilon)=54162.}
\tag{G7}
\]

This recertifies the historical 5643 single-event floor and the full ten-sign 54162 by a direct tree/chord method. The unit tests rederive the alternating bipartition independently for arbitrarily ordered genuine W34 original D6 six-ID witnesses; rotating or reversing source ID order never changes the total.

## 5. Consequence for actual original fixed correlated maps

Let \(D_{6,\bar Z}\) and \(BBo_{\bar Z}\) count distinct accepted genuine ORIGINAL source six-ID D6/BBo motifs, all six IDs avoiding any adversarial Z. Since they have different original source point/line degree profiles, the classes are disjoint. Each ORIGINAL sixset represents a distinct choice of six source columns; different source sixsets cannot overcount the SAME signed event of the risk experiment. Therefore the exact 51-pattern signed event contribution satisfies the valid source-motif lower bound

\[
\boxed{
R_3^{\text{accepted-sixsets}}
\ge\frac{54162D_{6,\bar Z}+53526BBo_{\bar Z}}{51^6}.}
\tag{G8}
\]

This bound is for the accepted signed original six-ID events in the same fixed labeling; no addition over overlapping events outside the actual six-ID event definition is performed. For the full risk statistic, the nonnegative six-ID contribution is a valid lower bound by the previously established source event decomposition.

As a **conditional corollary only**, if the all-order original source heavy/low theorem of #733 is independently mathematically accepted and supplies \(D_{6,\bar Z}+BBo_{\bar Z}\ge\delta s^6\), then the nonnegative contribution is at least \(53526\delta s^6/51^6\). This is not a new proof of that combinatorial lower bound, not a new ASET exponent and not a completed full R2/R3 construction.

## 6. Genuine ORIGINAL W32/W34 independent falsification

The new source module independently creates actual original W(3,2)/W(3,4), checks complete separately injected f,g and builds the 12 dual physical-coordinate edges directly from six original incidence IDs. It does NOT consult the historical GF(5) class classifier when deriving topology, applying the 9-template theorem or counting flows.

* For genuine complete W32 lex and reverse-line original injections, it enumerates ALL 10,935 original LEFT-B incidence six-ID candidates and independently recognizes respectively 8 and 7 actual B/B-overlap source motifs. It calculates every one of their TEN signed GF(5) weights via (G4), including original source configurations with no physical 3-path image.
* For genuine W34 lex and reverse-line, it takes three spaced six-ID samples from each of the 1534/463 frozen produced original BBo sixsets, checks all six IDs avoid actual original Z and evaluates all ten exact GF(5) signed events.
* For the three nonempty genuine original heavy D6 witnesses from #730, it reconstructs the aligned source-column C6 graph from six named source incidence IDs, computes all ten exact weights by (G4) and independently recomputes the actual alternating sign floor 5643.

**Separate verification algorithm:** construct all 51 four-support column vectors directly, enumerate 51³ first-half and 51³ second-half three-column choices, group each side by its 12-coordinate mod-five signed-sum signature, and join complementary signatures. It has no graph tree, no Fourier, no inclusion-exclusion. Five nontrivial test events, including the BBo worst sign 5175 and D6 alternating 5643, compare this direct palette oracle to (G4). A third comparator, the pre-existing accepted Fourier GF(5) evaluator, is imported ONLY in separate tests on actual original six-ID witnesses; it is never imported by the new main proof code.

The specialized GitHub-hosted workflow runs TEN independent tests and a fail-closed permanent full original-source JSON, including all 90 BBo events, 10 D6 signs, the 51-pattern double-oracle control, complete genuine W32 source sixset census, and authentic original W34 D6/BBo witnesses. It does not treat hypothetical numerical C_graph=c_graph=1 as a published graph theorem constant. INDEX and full Research must be checked on the same exact final PR HEAD.

## 7. Scientific STOP

This slice independently closes the **GF(5) signed event positivity and exact weights** for every genuine original D6/BBo six-ID source configuration under the correct all-order structural classification. It does not independently recertify the entire combinatorial heavy/low source lower from #730/#731/#733, the applicable ordinary-graph supersaturation constant values, arbitrary optimized ASET constructions, or the full source R2/R3 dependence on other terms. All conditional root claims in #230 remain pending the complete mathematical proof dependency audit. Scientific Draft only; no merge, no issue closure, no ASET exponent.

**Next allowed step:** a complete independent proof dependency DAG acceptance audit of #730–#734 including the external C6 graph theorem normalization and source path lower error budget, with exact-head CI, rather than more limited finite W32 examples or optimizing already checked constants.
