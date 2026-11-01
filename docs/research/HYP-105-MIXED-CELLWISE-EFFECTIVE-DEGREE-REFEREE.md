# HYP-105 / #230 — AA4-CELLREF: exact cell-supported effective-degree mixed FULL/CORE blocker

**Scientific Draft**, stacked ONLY on frozen [#692](https://github.com/definitely-stable/Mathlab/pull/692) at exact parent `b1013673a6eab9cd0921442d09e4439ec20ba1c4`. No changes to main or ancestors, no merge, no issue closure, and no qualified external mathematical review. This new all-h deterministic bound retains the TRUE original source W(3,2^h), the original six distinct incidence IDs, BOTH physical diagonals for every retained ORIGINAL source flag and all arbitrary correlations of complete separately globally injected fixed point/line maps f,g.

## 1. Exact independently identified proof frontier

Earlier [#685](https://github.com/definitely-stable/Mathlab/pull/685) and [#686](https://github.com/definitely-stable/Mathlab/pull/686) bounded internal original-source blockers with

\[
W_L^2\le B_L\Theta(H_0)\le B_L\Delta(H_0)\mathrm{tr}(A_0^4).
\tag{C1}
\]

Here H0 is the ORIGINAL physical CORE graph from actual source flag IDs I with BOTH real diagonals; A0 its symmetric adjacency, d(u) its physical degree, D=diag(d), and Theta=tr(DA0^4). The LEFT source blocker set T_L consists of physical **oriented actual first-core-edge** triples (v0,u,w) with endpoint labels f(q),g(r) for a TRUE ORIGINAL nonincident pair q,r and unique full-original GQ projection q--ell--p--r, where the first internal LEFT coordinate of u lies in f(p). Source projection anchors p,ell are from the **FULL** ORIGINAL source even if all their actual flag IDs have been removed from the core. B_L=|T_L|, W_L=sum_{(v0,u,w) in T_L}(A0²)[u,w]. Both GQ source-full/original-core Phi-Psi and the physical triples must agree, as independently verified in #685.

The old inequality (C1) discards the **actual** first-edge/last-vertex multiplicity and the physical A0² support. This slice proves a genuinely stronger **embedding-dependent** inequality without using the prior fourth-moment/Cauchy computation, any random completion of f/g, an external graph-theorem constant, or a homomorphism surrogate.

## 2. NEW universal finite graph theorem, exact rational proof

For ANY finite undirected simple graph H0 and ANY set T of distinct candidate ordered triples (v0,u,w) with actual physical first edge v0--u, define

\[
m(u,w)=\#\{v_0:(v_0,u,w)\in T\},\quad
B=|T|=\sum_{u,w}m(u,w),\quad 0\le m(u,w)\le d(u).
\]

Define exact nonnegative **rational** support-effective first-edge mass and the restricted degree-weighted fourth-moment energy

\[
\boxed{
\Xi_T=\sum_{m(u,w)>0}\frac{m(u,w)^2}{d(u)},\qquad
\Theta_T=\sum_{m(u,w)>0}d(u)\big[(A_0^2)_{uw}\big]^2.
}\tag{C2}
\]

Every denominator d(u) is positive on support, since an included candidate triple contains at least one real first edge to u. `Xi_T`, unlike the crude triple count B, responds to the **actual degree and multiplicity** of each supported physical endpoint cell.

Now expand the actual completion sum as a nonnegative bilinear form

\[
W_T=\sum_{u,w}m(u,w)(A_0^2)_{uw}.
\]

Apply Cauchy–Schwarz to the vectors `m(u,w)/sqrt(d(u))` and `sqrt(d(u))*(A0²)[u,w]` **only on cells with m>0**:

\[
\boxed{
W_T^2\le\Xi_T\Theta_T
\le B\Theta(H_0)
\le B\Delta(H_0)\mathrm{tr}(A_0^4).
}\tag{C3}
\]

The second inequality is exact from `m(u,w)<=d(u)` implying `m²/d<=m`, and the restricted support defining `Theta_T<=Theta`. The last follows from the elementary trace sum `Theta=sum_u d(u)sum_w(A0²)[u,w]²`. Thus (C3) **NEVER WEAKENS** the prior #685 estimate for ANY finite H0/T (including empty cores, nonbipartite H0, repeated physical endpoint cells with DIFFERENT first edges, irregular degrees, arbitrary source/cross-map correlations). The new bound can be strictly better with no asymptotic claim.

The improvement is not merely due to `Delta` versus degree-weighted `Theta`: `Xi_T<=B` and `Theta_T<=Theta` are TWO separate deterministic exact savings. For the actual K2,3 graph with a single selected oriented edge of source-multiplicity m(0,1)=1 at degree d(0)=3 and (A0²)[0,1]=3, one has `Xi=1/3, Theta_T=27, W=3`, so `W²=Xi*Theta_T=9` while the old `B Theta` is larger. Hence strict savings are realizable even in ordinary simple bipartite graphs.

## 3. TRUE original FULL/CORE blocker corollary and four positions

For ALL true W(3,2^h), every original physical CORE I and fixed injected f,g, apply (C3) to its TRUE original LEFT blocker set T_L. The inherited actual-original FULL-source identity from #685 is independently checked again in the finite reference:

\[
B_L=\Phi_L-\Psi_L,
\quad
\Phi_L=\sum_u\sum_{(x,k)\in\overrightarrow{f(u)}}
\sum_{p\in S_k}|C(p)\cap S_x|K_{pu},
\quad K_{pu}=\sum_y R(p,y)R_0(u,y).
\tag{C4}
\]

Source-first enumeration creates records using true core first flag IDs and full original original-GQ incidence q--ell--p--r; it partitions `Phi` into incident and nonincident q,r. Independently, physical-first enumeration starts at actual CORE edges, decodes the same real original q,r using endpoint physical pairs f(q),g(r), recovers the full-original projection, and checks the left internal coordinate in f(p). Exact equality of the **entire triple sets** (not only scalar totals) is required. No projection/anchor ID is invented or required to survive in I.

Write `Xi_L,Theta_L` for this T_L, and `Xi_R,Theta_R` for the exact **dual** source with swapped point and line factor types and transposed physical coordinates. For the FOUR internal blocking positions, physical directed-path reversal bounds the last-left by the first-left; original type/coordinate transpose treats the two right cases. Thus

\[
\boxed{
I_{\rm internal}\le
2\sqrt{\Xi_L\Theta_L}
+2\sqrt{\Xi_R\Theta_R}
\le 2\sqrt{(\Phi_L-\Psi_L)\Theta}
+2\sqrt{(\Phi_R-\Psi_R)\Theta}.
}\tag{C5}
\]

A stricter **exact integer computable** version uses `I_internal<=2(W_L+W_R)` where W_L/W_R are computed from actual physical cell multiplicities, not any norm bound. The all-h bound (C5) is an inequality, NOT a claim that we can calculate an infinite GQ by the finite oracle.

The parent all-h uniform estimates `B_side<=B0*s^(23/4)`, `Delta<=Ts`, `tr(A0^4)<=L4*s^5` still imply (with the NEW never-worse envelope) the SAME `O(s^(47/8))` internal error. No unproved strictly improved universal exponent is claimed, since configurations with `Xi/B` or `Theta_T/Theta` bounded away from zero may exist. The original Branch A condition `D6+U_BBo=Omega(s^6)` and the new all-map signed-GF5 coefficient #688 are NOT changed or independently globally accepted by this local strengthening.

## 4. New independently implemented adversarial validation

The new `research/hyp105_mixed_cellwise_effective_degree_referee.py` has TWO independently constructed objects:

* **Source-first:** build genuine ORIGINAL W32/W34 flag incidence and the complete full-source unique projection on EVERY q,r nonincident pair. Loop over actual ORIGINAL core IDs, both f/g orientations, true source collinearity q↔p, all full-original r through p. Count `Phi` and incident `Psi`, retain the ACTUAL nonincident triple set. It independently verifies `Phi-Psi=|T|`.
* **Physical-first:** construct both real physical diagonals for each original ID in core and their unique provenance. Build core physical edges and lookup full injected f/g labels. For every real oriented first edge and true decodable original q,r from endpoints, recover the FULL original projection and its INTERNAL blocker test, with no use of source-book tensor K_pu. Both full triple sets must agree EXACTLY. Recompute `A0²` by actual graph neighbor iteration, `Xi,Theta_T,Theta,tr(A0⁴)` by exact integer/Fraction arithmetic and verify EVERY link of (C3).

The new test suite independently evaluates 64 labeled 2×3 and 256 labeled 2×4 small ordinary bipartite graphs with multiple adversarial candidate triple subsets; explicit strict K2,3 certificate with exact equality of new Cauchy; genuine ORIGINAL W32 complete correlated maps with full, even, sparse and 4th-flag core subsets cross-checked with historical #685 scalar AND exact four-position counts; genuine W34 full/sparse arbitrary original cores and planted protected K4,4 source flags; empty and malformed source/cell controls.

**Scope:** input source generation is genuinely original W(3,2) or W(3,4). Finite tests falsify source/physical ID and coefficient mistakes, not asymptotic theorems. The generic graph proof in §2 and true original full/CORE source bijection in §3 are mathematical all-h statements. No reliance on finite h interpolation, no external SS6 input for the new local inequality, no human peer review.

## 5. Acceptance, integration and next step

Scientific #230 remains `OPEN_WITH_FORMAL_BLOCKER`. Passing a hosted workflow does not count as independent external extremal-combinatorics peer acceptance of #659/#672–#692, and this local strengthening is not a new ASET exponent, R2/R3 upper, numerical published graph supersaturation constants or all-small-h statement. No merge, parent mutation or issue closure.

**Next scientific step** after exact-head CI: an adversarial stress audit of the remaining root quantitative estimates `||P3||_F²`, original exceptional-endpoint weighted 21s5 bound, and all-h four-position loss, or a qualified outside scientific review of the COMPLETE original source proof. Avoid repeatedly optimizing root constants as a substitute for auditing original-ID correctness.
