# HYP-105 #230 — AA4-MIX4REF: source-ID four-position blocker and degree-weighted trace referee

**Status:** separate, scientific **Draft**, stacked strictly on [#684](https://github.com/definitely-stable/Mathlab/pull/684) at immutable parent `adef32110e3f84fe2e914d631045b8696f4f89b4`. Does not modify ancestors or `main`, accept Branch A, establish an ASET exponent, assign external balanced-SS6 constants or replace a qualified external referee. This gives a new *embedding-sensitive strengthening*, a full four-position proof, and two independently implemented finite falsifiers; no new exponent is claimed.

## 1. Scope and a sharper finite-graph inequality

For **every** dyadic `s=2^h>=2`, the true ORIGINAL symplectic GQ `W(3,s)`, **every** complete separately globally injective and arbitrarily correlated typed point/line pair map `f,g` into the minimal physical `E(K_a)`, and **every** set `I` of distinct actual original incidence IDs, let `H0` contain BOTH distinct diagonal physical edges of each flag in `I`. Physical vertices are the actual `[a]×[a]` cells; original projection anchors ALWAYS come from the full source, including flags not in `I`. The underlying physical graph is simple by separate global injection.

Write `A=A(H0)`, `D=diag(deg_H0(v))`, `Delta=max_v deg(v)`, and define the nonnegative **exact degree-weighted fourth moment**

\[
\Theta(H_0)=\operatorname{tr}(D A^4)
 =\sum_v\deg(v)\sum_w (A^2)_{vw}^2
 \le \Delta\operatorname{tr}(A^4).
\tag{1}
\]

For the first **left** internal coordinate, `T_L` is the set of ordered actual triples `(v0,v1,v3)` with `v0-v1` an oriented ORIGINAL core physical edge, endpoint pair labels `{v0.left,v3.left}=f(q)`, `{v0.right,v3.right}=g(r)` for a genuine original **nonincident** pair `q,r`, and `v1.left in f(p)` for the unique *full-source* projection `q--ell--p--r`. Do NOT require a middle vertex `v2`, a proper 3-path or `p,ell` in `I` in the triple definition. Define

\[
 B_L=|T_L|,\qquad W_L=\sum_{(v_0,v_1,v_3)\in T_L}(A^2)_{v_1v_3}.
\tag{2}
\]

The `W_L` sum counts ALL physical 3-walk completions, including improper ones; hence it is a safe envelope for the proper blocked paths.

### New exact weighted multiplier (valid for EVERY finite simple H0)

For physical ordered endpoint cell `(u,w)`, let `m_L(u,w)` be the number of `v0` with `(v0,u,w) in T_L`. Then `0<=m_L(u,w)<=deg(u)`, and

\[
\begin{aligned}
W_L^2
&\le B_L\sum_{u,w}m_L(u,w)(A^2)_{uw}^2\\
&\le B_L\Theta(H_0)\\
&\le B_L\Delta\operatorname{tr}(A^4).
\end{aligned}\tag{3}
\]

**Proof without invoking #672's completion bound:** expand `W_L` as a sum over individual physical triples, apply Cauchy–Schwarz to that finite multiset, and bound the multiplicity `m_L(u,w)` by the number of possible directed first edges entering `u`. Because `A` is symmetric, `sum_w(A²)_{uw}²=(A⁴)_{uu}`. Thus the weighted trace follows by literal double counting; no independence of walks or of `f,g`, no bipartiteness and no extrapolation from finite `h`.

`Theta` is **never worse** than the old `Delta*tr(A^4)` envelope; it can be strictly better for non-regular physical cores. The intermediate exact cell energy `sum m_L(u,w)(A²)_{uw}²` may be smaller again. No uniform strict gain in the asymptotic exponent is claimed.

## 2. Exact original FULL/CORE subtraction, independently source-indexed

Use the same true-original `S_x` and pencil arrays as #678, whose identity is independently reproved here from original records:

\[
R(p,y)=\#\{r:p\in r, y\in g(r)\},\quad
R_0(u,y)=\#\{\lambda:(u,\lambda)\in I,y\in g(\lambda)\},
\quad K_{pu}=\sum_y R(p,y)R_0(u,y).
\]

With `C(p)` the ORIGINAL collinearity neighborhood of `p`, put

\[
\Phi_L=\sum_{u}\sum_{(x,k)\in\overrightarrow{f(u)}}
\sum_{p\in S_k}|C(p)\cap S_x|K_{pu}.
\tag{4}
\]

Expand (4) as ORIGINAL records `(i=(u,lambda), oriented f(u)=(x,k), oriented g(lambda)=(y,t), p,q,r)`, with `p in S_k`, `q in C(p)∩S_x`, `p incident r` and `y in g(r)`. Every record is from TRUE source flags and retains their original IDs. Partition records into `q incident r` and `q not incident r`. Let `Psi_L` be the count of incident records. For a nonincident record, the GQ unique projection forces the chosen `p` to be the unique projection of `q` onto `r`. The output physical triple is uniquely `((x,y),(k,t),(z,w))`, where `f(q)={x,z}`, `g(r)={y,w}`. Conversely a physical triple uniquely determines its first original source flag owner, orientations, q,r and their projection. Thus there is a **bijection** and

\[
\boxed{B_L=\Phi_L-\Psi_L.}\tag{5}
\]

Combining (3),(5) yields the new **all-h embedding-sensitive** inequality

\[
\boxed{W_L^2\le(\Phi_L-\Psi_L)\Theta(H_0).}\tag{6}
\]

This is a new weighted-moment strengthening of the previously established unweighted #676/#678 bound. It is not a new assertion of the full Branch A proof.

## 3. All FOUR internal positions — explicit involutions

For a physical directed length-three core walk `v0,v1,v2,v3`, endpoints decode ORIGINAL q and r **without orientation**. The unique full-source path `q--ell--p--r` also does not depend on the direction of that physical walk.

1. **First inner left:** `v1.left in f(p)` is enveloped by `W_L`.
2. **Last inner left:** reverse the same ORIGINAL-ID physical walk `(v3,v2,v1,v0)`. End labels `f(q),g(r)` and projection `p,ell` do not change; this event maps bijectively to first-inner-left. Its count is at most `W_L`.
3. **First inner right:** transpose every actual physical vertex `(x,y)->(y,x)`, swap ORIGINAL factor TYPES `point<->line` in the genuine self-dual GQ, and swap `f,g`. The SAME original flag ID `(p,r)` is now indexed as `(r,p)`; the physical graph becomes a coordinate-transposed graph with the SAME two original diagonals per ID. Applying (6) in the dual gives `W_R^2<=(Phi_R-Psi_R)Theta`. The full dual original projection recovers the source line `ell` as the anchor coordinate label `g(ell)`.
4. **Last inner right:** apply the same walk reversal after original type and physical transpose. The count is at most `W_R`.

The permutation of physical vertices preserves `tr(D A^4)` EXACTLY. No extra source relabeling, independent left/right randomness, or independence of overlaps between the four events is assumed. For the union `I_internal` of internally blocked coordinate-proper actual three-paths with ORIGINAL nonincident and end-good source endpoint projection, the union bound and (6) give

\[
\boxed{
I_{\rm internal}\le 2W_L+2W_R
\le 2\sqrt{\Theta(H_0)}
\bigl(\sqrt{\Phi_L-\Psi_L}+\sqrt{\Phi_R-\Psi_R}\bigr).
}\tag{7}
\]

This bound does **not** require the two sides to have equal book populations, and counts overlapped blocked paths only in a safe upper bound. For an empty core, all terms vanish.

## 4. Recovery of the historical ALL-h universal exponent

Under the separately established #672 dense-core hypotheses and their #676–#683 refinements, each side has `B_side<=B0*s^(23/4)`, `Delta<=Ts`, and `tr(A^4)<=L4*s^5`. Consequently, using (1),(7),

\[
I_{\rm internal}
\le 4\sqrt{B_0TL_4}\,s^{(23/4+6)/2}
=4\sqrt{B_0TL_4}\,s^{47/8}.
\tag{8}
\]

The strict `47/8<6` property and its quantified integration with historical ORIGINAL B/B-overlap are unchanged. The weighted proof provides a *stronger fixed-embedding certificate* and an independent four-position review, **not** a new root theorem, numerical graph constants, lower bound for all small dyadic h, R2/R3 equality, or ASET consequence. The historical six-ID / 51-column GF5 bridge is inherited, not reproved by this local lemma.

## 5. Two genuinely different exact finite falsifiers, and known limits

- `research/hyp105_four_internal_blocker_weighted_referee.py`: generates actual W(3,2) and W(3,4) ORIGINAL incidence IDs and physically injected complete labels. **SOURCE-first** enumerates all records in (4), including incident `Psi` and full anchors outside the core; **PHYSICAL-first** enumerates the actual blocked triples from physical edges and decoded q,r without using the source-book output. Requires equality of their entire triple sets, `Phi-Psi=|T|`, exact weighted-moment and cell-energy inequalities, source-ID preservation and physical point/line duality. Separately enumerates all physical three-walks, their original nonincident projected ends, and all four internal positions; checks both reversal equalities and two direct weighted-completion equalities.
- `research/test_hyp105_four_internal_blocker_weighted_referee.py`: brute-force **all 64** labeled 2×3 ordinary bipartite graphs, compare `tr(A^4)` and `tr(DA^4)` with independently rooted closed-four-walk enumeration, and test four adversarial candidate-triple selections per graph. Also tests multiple correlated complete W32 maps/full/sparse cores and genuine W34 correlated full/sparse cores with actual original flags; empty/invalid ID, duplicate ID, illegal injection and unsupported-h fail-closed cases.
- Dedicated GitHub-hosted Python 3.12 exact-head CI runs these independent tests. Full repository Research and INDEX are separate acceptance checks. A finite successful run is a falsifier of indexing/provenance mistakes, **never** an independent proof of `s->infinity` or external qualified mathematical peer-review.

## 6. Scientific conclusion and next work

The new contribution is (3)/(6)/(7): a degree-weighted, incident-defect-corrected, orientation-complete **deterministic theorem for all dyadic h** on true ORIGINAL W(3,s), not just a numerical W32 fit. Its dependencies are precisely original GQ uniqueness, global typed pair injections, ordinary finite-graph Cauchy, physical transpose and path reversal. The sharp uniform `s^(47/8)` corollary still depends on #672's full/core density and moment bounds, and the overall Branch A still depends on #659's balanced C6 source-ID injection, #677's true six-ID inverse, and other explicitly listed input lemmas. No root promotion, no scientific merge or issue closure. **Next:** prepare a self-contained independent qualified ROOTREF of the complete #659/#672/#684 stack, including the external balanced C6 hypotheses and all ORIGINAL GF5 six-ID transfer steps.
