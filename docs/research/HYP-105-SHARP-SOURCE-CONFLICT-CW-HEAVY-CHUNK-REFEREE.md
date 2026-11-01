# HYP-105 / #230 — AA4-CWSHARP: independent ORIGINAL source-conflict / Caro–Wei / physical heavy-tail referee

**Scientific Draft**, stacked strictly on frozen [#696](https://github.com/definitely-stable/Mathlab/pull/696) exact HEAD `0eff0fa4ca7698141ab05acf8d06b846baf7ef01`. This is a new deterministic **all-h** quantitative strengthening of the real original symplectic `W(3,2^h)` heavy-tail source-selection lemma of #659/#684, including a critical independent referee of every loss in the original-source-to-balanced-ordinary-graph transition. It does **not** change point/line factors, original flag incidence IDs, full separately globally injected arbitrarily correlated fixed maps `f,g`, two true physical diagonals per original flag, the original GF5 class, any published graph-theorem constants, or the remaining dense-core moment arguments. All scientific Drafts are unmerged; root #230 remains `OPEN_WITH_FORMAL_BLOCKER`, pending independent qualified scientific review.

## 1. The precise prior step worth improving

For original `s=2^h>=64`, let `V=(s+1)(s²+1)`, `N=(s+1)V`, and `a=min{j: binom(j,2)>=V}`. Each ORIGINAL flag `(p,ell)` gives precisely TWO different physical opposite-corner simple edges, each with UNIQUE real original source flag ID owner. The original FULL physical graph H has `2N` actual edges and total degree `4N`.

Let `Q_T={v:deg_H(v)>T*s}` and `E_T` count the distinct actual FULL physical edges touching Q_T. In the heavy-tail premise `E_T>=epsilon*s^4`, at least `L>=E_T/2>=epsilon*s^4/2` DISTINCT ORIGINAL flag IDs own at least one heavy edge. Fix one actual physical heavy witness diagonal per each of these L original source flags. The original source conflict graph `K_I` on those L flag IDs has an edge precisely for same ORIGINAL point and intersecting right g-pair, or same ORIGINAL line and intersecting left f-pair. It has **exactly** `M_g(I)+M_f(I)` edges, by source uniqueness, with `M_g(I),M_f(I)<=C_s`. Original-pencil conflicts need not be independent nor must they have disjoint neighborhoods. Their sets are actual ORIGINAL incidence IDs.

The old #684 proof first used the coarse `C_s<=1.5s^4` and `L<=N<=2s^4` to bound `L²/(4C_s+L)` from below by `epsilon²s^4/32`. After two whole-flag binary cuts this produced `|I_G|>=beta_old*s^4`, `beta_old=epsilon²/128`. Both cuts leave **BOTH** real diagonal edges per selected original flag and preserve the previously assigned heavy physical witness. A further two-color side selection and un-cloned opposite-side physical chunk generated an actual balanced simple bipartite subgraph F with
\[
v(F)\le16s^3/T,\qquad e(F)/v(F)\ge\beta_{old}s/32.
\]
No independence between f and g is used. In this slice we retain the ACTUAL source conflict size in Caro–Wei rather than replacing its denominator by a loose bound.

## 2. NEW uniform original-source book certificate: `C_s<=6s^4/5`

The ORIGINAL source incidence singular values of the genuine `W(3,s)` point–line matrix are `s+1, sqrt(2s),0`, with the top singular value multiplicity 1. As already independently proved in #655/#659, for FULL original global distinct physical pair labelings,
\[
M_f,M_g\le C_s=(s^2+1)(s^2+a-2).
\tag{CW1}
\]
The proof uses only genuine source incidence, original pencil-coordinate books and `k_y<=a-1`; it does not treat arbitrary unrelated flag sets as a generalized quadrangle.

The earlier exact original-alphabet lemma #690 gives for all `s>=64`
\[
a\le\left\lceil\frac32s\sqrt{s}\right\rceil
\le\frac{97}{64}s\sqrt{s}.
\]
For the second inequality: `s sqrt(s)>=512`, so the ceiling's possible `+1` is dominated by `(1/64)s sqrt(s)>=8`. The first inequality follows since `binom(ceil(3s sqrt(s)/2),2)>=V` for `s>=64`, a direct expansion of `V=s^3+s^2+s+1`.

Set `u=1/sqrt(s)<=1/8`. Use the EXACT original book (CW1):
\[
\begin{aligned}
\frac{C_s}{s^4}
&=(1+s^{-2})\left(1+\frac{a-2}{s^2}\right)\\
&\le(1+u^4)\left(1+\frac{97}{64}u\right)\\
&\le\frac{4097}{4096}\frac{609}{512}
=\frac{2495073}{2097152}
<\boxed{\frac65}.
\end{aligned}
\tag{CW2}
\]
This upper is an all-h REAL original GQ theorem, not a numerical fit. It improves the unnecessarily coarse global source book constant `3/2` for every allowed dyadic `s>=64`. The inequality is checked with isqrt-based exact minimal alphabet and Fraction on dyadic s=2^6..2^25 in an independent implementation.

## 3. NEW size-aware ORIGINAL conflict selector and sharper source fraction

The source conflict graph of the L actual heavy original ID flags has `E_conf=M_g(I)+M_f(I)<=2C_s` actual edges. A uniform random ordering of these ORIGINAL flags and retention of every local priority minimum selects a genuine independent set of expected size
\[
\sum_{i\in I}\frac1{d_{K_I}(i)+1}
\ge\frac{L^2}{2E_{conf}+L}
\ge\frac{L^2}{4C_s+L}.
\]
Thus some deterministic independent ORIGINAL-ID set `J` has at least that many members. Greedy minimum-current-degree selection is one constructive option; its Caro–Wei guarantee is separately proved and independently exhaustively tested for every graph on 5 vertices. The two independent typed conditional-expectation binary cuts then preserve at least one quarter of J, keeping BOTH physical diagonals of every surviving flag. Hence the **stronger exact instance-sensitive bound**:
\[
\boxed{
|I_G|\ge\frac{L^2}{4(4C_s+L)}.
}\tag{CW3}
\]
This inequality is valid for ALL positive L of genuine heavy source flags, even where the population is strongly concentrated on one full physical heavy vertex.

For the uniform heavy premise `E_T>=epsilon*s^4` take `L>=epsilon*s^4/2`. The function `t²/(4(4C_s+t))` is increasing for `t>0`; using (CW2) yields
\[
\begin{aligned}
\frac{|I_G|}{s^4}
&\ge\frac{(\epsilon/2)^2}{4(4\cdot6/5+\epsilon/2)}\\
&=\boxed{\beta_{new}(\epsilon)
=\frac{5\epsilon^2}{384+40\epsilon}.}
\end{aligned}
\tag{CW4}
\]
The full physical graph has at most `2N<=4s^4` edges, so a possible heavy premise implies `0<epsilon<=4`. In this whole feasible range,
\[
\frac{\beta_{new}}{\beta_{old}}
=\frac{640}{384+40\epsilon}\ge\frac{640}{544}>1.
\]
Therefore **the old historical selector floor is strictly improved throughout the possible heavy range**, not only for one carefully chosen epsilon. In the actual #690 root candidate `epsilon=1787/4096`, the source fraction is about **1.5942× larger** than #684. This claim is exact rational algebra, not an estimation of any published external C6 graph constant.

**Independent original-source proof limits:** the *original spectral book bound* (CW1) is still one of the prior theorem inputs, now with a sharper provable purely algebraic postprocessing; finite W32/W34 computations falsify errors in original point and line conflict identities but do not prove (CW1) in all h. No assumption that Caro–Wei flags are independent samples or that two physical diagonals may be chosen separately is allowed.

## 4. Transfer to the SAME physical heavy graph and SAME un-cloned balanced F

Repeat the unchanged #684 witness argument with the NEW `|I_G|>=beta_new*s^4`. Choose for each retained ORIGINAL source flag exactly one of its OWN previously assigned real heavy physical diagonals. Each such diagonal touches original FULL Q_T. Assign the physical heavy endpoint to exactly one of two left binary-color classes, and retain the class with at least half of these source-owned physical witness edges. They are DISTINCT because all physical edges have UNIQUE original ID owners.

Let R be all original FULL heavy physical vertices in that chosen color class, with `r=|R|>=1`; its size is bounded independently of the selector:
\[
r\le|Q_T|\le\frac{4N}{Ts}\le\frac{8s^3}{T}.
\]
Let Y be the ACTUAL opposite left-cut color class of the selected graph G. The ACTUAL simple bipartite graph G[R,Y] contains `E>=beta_new*s^4/2` distinct physical selected edges. Partition actual Y into disjoint un-cloned vertex chunks of size at most r. Since total `|Y|<=a^2<=4s^3`, number chunks is at most `2a^2/r`. Select one chunk Y* with at least `Er/(2a²)` real edges to R. The ACTUAL ordinary F=G[R,Y*] has
\[
\boxed{
v(F)\le2r\le16s^3/T,\qquad
e(F)/v(F)\ge\frac{E}{4a^2}
\ge\frac{\beta_{new}s}{32}.
}\tag{CW5}
\]
No invented vertices, ordinary graph edge copies, stochastic label completions, loss of original source provenance or paired-diagonal requirement on the smaller F are introduced. #696 independently proves that **any actual F subset of this selected G retains C6→D6 source-six-ID injectivity**, even when F contains only one physical diagonal of any retained original source flag.

Let `C_graph,c_graph>0` remain the TRUE **UNKNOWN existential** external ordinary simple-C6 supersaturation constants (Simonovits' result incorporated in Jiang–Yepremyan). Then by the same graph-only sufficient condition,
\[
\boxed{
T\ge2^{19}C_{graph}^3\beta_{new}^{-3}
\quad\Longrightarrow\quad
D_6(f,g)\ge c_{graph}(\beta_{new}/32)^6s^6.
}\tag{CW6}
\]
The old #684 formula had `beta_old=epsilon²/128` and threshold `2^19 C_graph³ beta_old^{-3}=2^40 C_graph³ epsilon^{-6}`. Both new inequalities are strictly stronger, preserving the SAME original source and graph theorem:
\[
\frac{T_{new}}{T_{old}}=(\beta_{old}/\beta_{new})^3,
\qquad
\frac{\delta_{new}}{\delta_{old}}=(\beta_{new}/\beta_{old})^6.
\]
For epsilon=1787/4096, the new sufficient threshold coefficient relative to the old is approximately **0.2468**, and the original D6 guaranteed constant is approximately **16.42× larger**, conditional on the same unknown external `C_graph,c_graph`. The asymptotic power `s^6` is unchanged, no ASET exponent or full root acceptance is established, and no real numerical h0 can be determined without the graph theorem constants.

## 5. Independent finite falsifiers and review criteria

The new `research/hyp105_sharp_source_conflict_cw_heavy_chunk_referee.py` imports only the genuine ORIGINAL symplectic source constructor, NOT #659/#684's selector/conflict/physical graph code. It separately constructs every true physical flag diagonal and its unique ORIGINAL incidence owner, the full physical high-degree set Q_T, each original flag heavy-edge witness, and TWO independent original conflict censuses: (a) pairwise original ID comparisons at same ORIGINAL point or line and (b) completely separate source pencil-coordinate collision buckets. Both MUST produce identical counts `M_g(I),M_f(I)`.

It then independently builds an actual source-ID independent set via constructive min-current-degree Caro–Wei, TWO conditional-expectation typed coordinate cuts retaining WHOLE ORIGINAL flags and BOTH their physical diagonals, rechecks exact heavy original ID witnesses, assigns heavy endpoints to the two left-cut classes and constructs actual ordinary uncloned R/Y chunks. All selections use fixed original f,g without any reassignment. Tests include 1024 exhaustive five-source-conflict graphs against exact Caro–Wei, 4096 independent three-by-four physical pair-label bipartite edge selections against both typed-cut half guarantee, dyadic `s=64..2^25` exact original alphabet + C_s bound, symbolic positive exact rational eps/C/c tests, actual ORIGINAL W32 with five arbitrary globally injected correlated right maps and varying T, genuine W34 (full/sparse heavy tails) and the true protected W34 K4,4 source-labeled fixture, malformed cases fail closed. Finite checks are falsifiers, not all-h mathematical proofs. All-h mathematical statements are proved in Sections 2–4 with the original source spectral book result explicitly stated as prior input.

**Scientific STOP / acceptance:** no independent qualified human referee of the complete original source #659/#672–#697, no general explicit external C_graph,c_graph, no exact positive GF5 signed R3 theorem beyond the inherited conditional floors. Keep this Draft and all parents unmerged, main unchanged, #230 OPEN_WITH_FORMAL_BLOCKER. The right next scientific action is independent external peer review of source spectral/collision and Caro–Wei heavy witness geometry along with the dense-core 6-walk proof. Do not infer that a larger \(\beta\) resolves all remaining root acceptance barriers.
