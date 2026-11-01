# HYP-105 / #230 — AA4-EPSOPT: maximal coarse-core heavy-tail budget `epsilon=13/32` and tighter Branch A constants

**Status:** rigorous deterministic optimization of an EXISTING all-h dichotomy, implemented as independent exact integer/rational certificate and genuine original-source falsifiers. **Scientific DRAFT**, stacked only on frozen [#688](https://github.com/definitely-stable/Mathlab/pull/688) HEAD `57a21adc0dac09a4ca46c7f151f24dc06e8f0b8b`, no changes to ancestors or `main`. This is an optimization of the current **coarse CORE-budget argument**, **NOT** a proof that the selected epsilon is globally optimal for genuine W(3,s), **NOT** a proof of the external ordinary C6 theorem, an independent qualified referee, a new exponent or a result for arbitrary weighted ASET constructions. #230 remains `OPEN_WITH_FORMAL_BLOCKER`.

## 1. Mathematical setting and the avoidable historical constant loss

Fix dyadic `s=2^h>=64`, true original symplectic generalized quadrangle `W(3,s)`, point and line factor counts `V=(s+1)(s²+1)`, ORIGINAL incidence flag count `N=(s+1)V`, minimal physical alphabet `a=min{t:binom(t,2)>=V}`. Fix **arbitrary complete separately globally injected, arbitrarily correlated** `f:P->E(K_a)`, `g:L->E(K_a)`. Every genuine original flag ID `(p,ell)` contributes BOTH opposite-corner physical diagonals; full physical graph H has exactly `2N` ordinary simple edges. All source-sixset and retained CORE counts refer to **actual original incidence IDs**.

Let `Q_T={v:deg_FULL_H(v)>T s}`; `E_T` counts distinct FULL-H physical edges touching `Q_T`. Under the externally proved balanced C6 graph supersaturation theorem with unspecified absolute C_graph,c_graph>0, the independently checked [#684](https://github.com/definitely-stable/Mathlab/pull/684) original-degree/no-clone result gives for **EVERY** `epsilon>0`, provided `T>=2^40 C_graph³ epsilon^(-6)`:

\[
E_T\ge\epsilon s^4
\Longrightarrow
D_6(f,g)\ge\alpha(\epsilon)s^6,\qquad
\alpha(\epsilon)=c_{\rm graph}\epsilon^{12}/2^{72}.\tag{E1}
\]

Here D6 counts six distinct ORIGINAL flags after the exact physical C6->original six-ID inverse; the graph theorem counts ordinary actual simple C6s, not a six-cycle surrogate. No i.i.d. assumptions on f or g are used.

The historical [#672](https://github.com/definitely-stable/Mathlab/pull/672), [#683](https://github.com/definitely-stable/Mathlab/pull/683), [#686](https://github.com/definitely-stable/Mathlab/pull/686) proof fixed `epsilon=1/8` without optimizing the amount of the actual ORIGINAL source that must remain after cutting the FULL physical heavy-degree tail and the original conflict book. Its heavy threshold was `T_old=max(1,ceil(2^58 C_graph³))` and the source-sixset floor `delta_old=min(1/8,c_graph/2^108)`.

## 2. NEW deterministic all-h maximal coarse-budget epsilon

Delete WHOLE ORIGINAL flag IDs owning any physical edge touching `Q_T`. At most `E_T` original IDs are deleted, since each such source flag owns at least one actual distinct heavy physical edge. Independently mark every full ORIGINAL source conflict-graph vertex with degree greater than fixed `K=64`, deleting at most

\[
\frac{2|E(\mathrm{conflict})|}{K}
\le \frac{4 C_s}{64}\le\frac{3}{32}s^4,\qquad
C_s=(s^2+1)(s^2+a-2)\le\frac32s^4.\tag{E2}
\]

These conflicts are ACTUAL same-point/shared-g-coordinate or same-line/shared-f-coordinate pairs of ORIGINAL flag IDs; the original full point-line pencil books each have at most C_s by the genuine W(3,s) incidence spectrum. This is not a conflict count per independent physical edge.

If the heavy tail is SMALL `E_T<epsilon*s4`, the surviving true-original paired core `I` satisfies

\[
N_0=|I|>N-\left(\epsilon+\tfrac3{32}\right)s^4,
\quad
m_0=2N_0>
2\left(1-\epsilon-\tfrac3{32}\right)s^4,\tag{E3}
\]

using **only** the all-h elementary `N>=s4`. The unchanged #672–686 moment proof requires

\[
m_0\ge s^4,\qquad \Delta(H_0)\le Ts,\qquad
\Delta(\mathrm{original\ conflict\ core})\le64.\tag{E4}
\]

Both degree caps remain unchanged: no retained flag has a diagonal at any FULL heavy vertex, and every retained original conflict-graph ID had FULL conflict degree <=64.

Consequently the **ENTIRE unchanged** proper-three-path / source book / endpoint / four-blocker / B/B six-ID proof carries through whenever

\[
2(1-\epsilon-3/32)\ge1
\iff
\boxed{\epsilon\le13/32}.\tag{E5}
\]

**NEW CHOICE:** `epsilon_opt=13/32`. This is the **largest constant allowed by these precise existing coarse bounds** (K=64, N>=s4, C_s<=1.5s4, m0>=s4). It is NOT a demonstrated optimal epsilon for the actual GQ or for a redesigned selector/moment analysis. In fact true N exceeds s4 and C_s is slightly below 1.5s4 at finite s, so sharper s-dependent bounds can allow slightly larger finite-s eps; their uniform asymptotic supremum within this coarse method is 13/32.

At the boundary eps=13/32, the strict small-tail `E_T<epsilon*s4` guarantees `m0>s4` even under these crude constants. Original source ID flags, all maps and the real unique full GQ projection are preserved. No original-projection flag is incorrectly required to lie in the core.

## 3. Improved heavy branch and geometric Branch A disjunction

Specializing (E1) to `epsilon=13/32` yields the NEW source-backed FULL degree threshold

\[
\boxed{
T_{\rm opt}=\max\!\left\{1,
\left\lceil \frac{2^{70}}{13^6} C_{\rm graph}^3\right\rceil
\right\},
}\tag{E6}
\]

because `2^40*(32/13)^6=2^70/13^6`. Under `E_T>=13s4/32`,

\[
\boxed{D_6\ge\alpha_{\rm opt}s^6,\qquad
\alpha_{\rm opt}=c_{\rm graph}\frac{13^{12}}{2^{132}}.}\tag{E7}
\]

This lower coefficient is `(13/4)^12=13^12/2^24` times the old heavy coefficient `c_graph*2^-108`, while the leading degree threshold is reduced by `(13/4)^6=13^6/2^12` before integer ceilings (respectively about **1.39 million** stronger and **1178** times smaller).

Let `delta_opt=min(1/8,alpha_opt)`. Partition on `D6>=delta_opt*s6` versus `D6<delta_opt*s6`. In the latter case, the contrapositive of (E7) ensures `E_T<epsilon_opt*s4`. The core obeys (E4) by (E3) and the exact ORIGINAL full/core argument of the stacked [#672–686](https://github.com/definitely-stable/Mathlab/pull/686) then gives (using historical not-yet-qualified-externally-accepted proof inputs)

\[
U_{BB,\rm overlap}\ge\frac{s^6}4-34Ts^5
   -\frac{L_E}2s^{11/2}
   -2\sqrt{B_0TL_4}\,s^{47/8}.\tag{E8}
\]

No exponent, selector, endpoint partition or four internal source blocker estimate is changed. The three negative terms become <=s6/24 each beyond the explicit all-h exact-integer threshold below, and hence

\[
D_6(f,g)+U_{BB,\rm overlap}(f,g)
\ge \delta_{\rm opt}s^6
\qquad\forall\text{ legal }f,g\text{ and }s\ge s_{0,\rm opt}.\tag{E9}
\]

The same ROOT `S_seven>=delta_opt*s6` follows, strictly conditional on the referenced geometric all-h and GF5 six-ID inputs. No acceptance gate is silently bypassed.

## 4. NEW exact-integer dyadic h0 certificate and stronger signed risk

Define, exactly as in #686 and with the NEW `T=T_opt`,

\[
\begin{aligned}
\sigma_2^{-1}&=16\cdot65^2,&
\sigma_3^{-1}&=64\cdot65^3,\\
L_6&=24+288T^2,&
\widehat L_4&=2\sigma_2^{-2}\lceil\sqrt{8L_6}\rceil+40T,\\
\widehat B_0&=64\lceil\sqrt{65T}\rceil.
\end{aligned}\tag{E10}
\]

The following integer is a **sufficient** threshold (not necessarily the smallest valid threshold):

\[
\boxed{
s_0=\max\left\{64,816T,
144\cdot21\sigma_3^{-2}L_6,
48^8(\widehat B_0 T\widehat L_4)^4
\right\},\quad
h_0=\max\{1,\lceil\log_2 s_0\rceil\}.
}\tag{E11}
\]

All displayed operations in the certificate use exact integers once actual positive C_graph is fixed; the accompanying reproducible reference accepts **positive rational placeholders** for C_graph,c_graph and does not assert the real external constants are rational or numerically known.

**Explicit test-only illustration, C_graph=c_graph=1, NOT values certified by the published theorem:**

| Parameter | Old eps=1/8 | NEW eps=13/32 |
|---|---:|---:|
| Required T | 288230376151711744 | **244590498757546** |
| Sufficient dyadic h0 | 816 | **714** |
| Geometric sixset floor delta | `2^-108` | **`13^12/2^132`** |
| Uniform R3 floor via #688 | `53526*delta_old/51^6` | **`53526*delta_new/51^6`** |

The exact-rational numeric T and h0 are reproducible INTEGER regression tests, **not** a proof of applicability of C=c=1, nor a construction of W(3,2^714). In particular, "h0=714" is a **conditional example only**. There is no numeric effective h0 from unspecified published C_graph,c_graph.

The independently accepted finite GF5 signed-event coefficient improvement from parent [#688](https://github.com/definitely-stable/Mathlab/pull/688) gives

\[
51^6R_3(f,g)\ge54162D_6+53526U_{BB,\rm overlap}
\quad\text{(all dyadic h, all legal fixed maps)}.\tag{E12}
\]

Therefore (E9) yields the already stronger simple corollary
`R3>=53526*delta_opt*s6/51^6`. Keeping the separate weighted contributions through the original Branch A dichotomy rather than discarding to the minimum yields the slightly stronger, exact alternative

\[
\boxed{
R_3(f,g)\ge\frac{
\min\{54162\delta_{\rm opt},\ 53526/8\}
}{51^6}s^6
\quad(s\ge s_{0,\rm opt}).
}\tag{E13}
\]

Indeed either `D6>=delta_opt*s6` or `U_BBo>=s6/8`, and their two distinct original-source-sixset families are disjoint. This is a lower bound for the EXPECTED NUMBER of signed 3-versus-3 events; it is NOT a probability-of-ANY-event union bound and requires NO independence between different signed events.

## 5. Independent finite test matrix and sharp scope

`research/hyp105_heavy_tail_epsilon_optimal_root.py` independently implements:

* exact `Fraction` `epsilon`, `T`, `alpha`, `delta`, all constants, exact integer ceiling roots and `h0` (does NOT import #683/#686 proof calculators);
* universal **source budget** for `s=64,128,...` from independently recomputed `a,V,N,C_s`, checking `N>=s4,C_s<=1.5s4,a²<=4s³`, and that the new maximal coarse epsilon preserves `m0>=s4`;
* mathematically meaningful STOP: eps greater than 13/32 loses the *coarse fixed-budget implication*; no claim of constructing a true original GQ counterexample to larger eps;
* independent **genuine ORIGINAL W(3,2)/W(3,4)** source generation only, full separate globally injective correlated maps, both actual physical diagonals per source flag, independently reconstructed FULL heavy vertex set and physical source owners, heavy-flag ID deletion, independently counted original conflict edges/degrees, original-ID core and inherited physical and source-conflict degree caps;
* exact trials of multiple symbolic positive C,c, both old/new eps and adversarial T,K, independently checked integer dyadic threshold off-by-one and fail-closed invalid maps/constants.

The `research/test_hyp105_heavy_tail_epsilon_optimal_root.py` suite checks genuine finite original-source identities, exact algebraic improvement, old 816 vs new 714 illustration, dyadic h0 guard, boundary and malformed inputs. Finite `W(3,2)` and `W(3,4)` tests verify indexing/provenance only; all-h derivation uses the algebraic proofs and the cited, established external graph theorem. The new dedicated GitHub-hosted CI must pass on the exact final PR HEAD; all Research/INDEX checks are separately audited.

## 6. Scientific acceptance and next action

This optimization is a new explicit **all-h quantitative strengthening** of the D6/BBo lower-BRANCH consequences, within the *same fixed* original GQ, and a new proof of maximality relative to the previous **specific coarse retention budget**. It remains dependent on the geometric correctness of the source-ID heavy-tail, physical C6 / original D6 injection, proper three-path selector, FULL-source-to-CORE mixed blockers, original B/B six-ID inverse and signed GF5 flow classifier, which are externally unreviewed as a complete chain.

Scientific status remains `OPEN_WITH_FORMAL_BLOCKER`. Do not mark root as formally accepted, close #230, merge stacked scientific PRs, generalize to all ASETs or assume explicit graph-theorem C,c. The appropriate next truly distinct task is a qualified external mathematical referee or an independent counterexample search on the original source-indexed global geometric chain, **not** repeatedly tweaking constants.
