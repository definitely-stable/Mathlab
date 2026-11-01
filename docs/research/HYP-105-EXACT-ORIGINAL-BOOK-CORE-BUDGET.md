# HYP-105 / #230 — AA4-BOOKBUD: independent exact ORIGINAL source-book retention budget

**Scientific Draft; NOT root acceptance or qualified external peer review.** This slice follows the frozen [AA4-EPSOPT #689](https://github.com/definitely-stable/Mathlab/pull/689) exact HEAD `ab6e6deb64a5bfc92a42ffe8394707fe1e799e92`. It preserves the TRUE `W(3,2^h)`, six different ORIGINAL source incidence flags, both physical diagonals per original flag and every complete separately globally injective arbitrarily correlated fixed typed f,g. Source-full and physical-core maps are never resampled. No parent `main` or ancestor PR changes; #230 remains `OPEN_WITH_FORMAL_BLOCKER`.

## 1. Exact frontier and the limit of previous "optimal" wording

[#689](https://github.com/definitely-stable/Mathlab/pull/689) proved `epsilon=13/32` is the **MAXIMUM permitted by its specifically chosen COARSE constant input** `N>=s4`, `Cs<=3s4/2`, `K=64`, `m0>=s4`. This was correctly scoped to that *particular coarse budget*, NOT an optimization of the real source quantities. The present step relaxes precisely that coarsening, using actual ORIGINAL counts `N=(s+1)^2(s²+1)` and the spectral ORIGINAL book bound `Cs=(s²+1)(s²+a-2)`, `a=min{j:binom(j,2)>=(s+1)(s²+1)}`. Thus there is **no counterexample** to #689's restricted maximality statement. The new source-aware budget is strictly stronger, for every sufficiently large dyadic source.

Fix `s=2^h>=64`, all admissible **fixed** original typed physical injections f,g, and `K=64`. The full H has TWO distinct physical diagonals per ORIGINAL source flag. Let `E_T` be its **full** high-degree incident edge count; if `E_T<epsilon*s4`, deleting ALL original flags owning such physical edges loses at most `epsilon*s4` original flags. Deleting ORIGINAL flags of degree above 64 in the full source conflict graph loses at most `4 Cs/64=Cs/16` more flags. The actual paired original core consequently obeys

\[
m_0=2N_0>2\left(N-\epsilon s^4-C_s/16\right).
\tag{B1}
\]

Nothing changes about the proofs of core physical `Delta<=T*s` or source conflict `Delta_original<=64`, which work for ALL injections and ANY epsilon.

The already proved #672/#686 universal proper three-path, sixth/fourth moment, ORIGINAL endpoint exception, all-four mixed blockers and six-ID B/B inverse need only `m0>=s4`. A sufficient exact source-aware criterion is

\[
\epsilon \le E_{\rm budget}(s)
:=\frac{N}{s^4}-\frac12-\frac{C_s}{16s^4}.
\tag{B2}
\]

This uses the TRUE original point/line incidence count and genuine symplectic source book, not empirical W32/W34 estimates.

## 2. Independent ALL-h rational analytic lower bound — no fitting

Write `u=s^{-1/2}`, so `0<u<=1/8` for all `s>=64`. Independently derive the TRUE label alphabet upper bound

\[
a\le\left\lceil \frac32 s\sqrt{s}\right\rceil
\le \frac{97}{64}s\sqrt{s}.
\tag{B3}
\]

To prove the first inequality, put `a_*=ceil(1.5*s*sqrt(s))`. Then

\[
\binom{a_*}{2}\ge\frac98s^3-\frac34s^{3/2}
\ge(s+1)(s^2+1)=V
\quad (s\ge64).
\]

The second follows from `ceil(x)<=x+1` and `s sqrt(s)>=512`. **No assumption that h is even** or `sqrt(s)` is integral.

Now the genuine exact source population satisfies `N/s4=(1+1/s)^2(1+1/s²)>=1+2u²`. Meanwhile

\[
\frac{C_s}{s^4}
=(1+u^4)\left(1+\frac{a-2}{s^2}\right)
\le(1+u^4)(1+b u),\quad b=97/64.
\]

Insert both into (B2):

\[
E_{\rm budget}(s)\ge
\frac7{16}+2u^2-\frac{bu}{16}
-\frac{u^4}{16}-\frac{bu^5}{16}.
\tag{B4}
\]

Complete the square **for all real** `u>0`:

\[
2u^2-\frac{bu}{16}
=2\left(u-\frac b{64}\right)^2-\frac{b^2}{2048}
\ge-\frac{b^2}{2048}.
\]

The remaining terms satisfy `u^4<=1/4096` and `u^5<=1/32768`. Therefore there is a uniform **rational, source-independent** lower certificate

\[
\boxed{
E_{\rm budget}(s)\ge
\frac7{16}-\frac{b^2}{2048}
-\frac1{65536}-\frac b{524288}
=\frac7{16}-\frac{38245}{33554432}
>\frac{1787}{4096}.
}
\tag{B5}
\]

This holds for **every real s>=64** and in particular ALL dyadic s, regardless of any global relabeling or correlation f,g. It is not an extrapolation from checked finite h. It is NOT claimed optimal for the exact N,Cs or any redesigned argument.

**New certified choice:**

\[
\boxed{\varepsilon_{\rm source}=\frac{1787}{4096}
\approx0.4362793 >\frac{13}{32}=0.40625.}
\tag{B6}
\]

The improvement is strict and preserves `m0>s4` throughout the original proof. The old #689 statement remains valid in the narrower coarse setting, but its constant is now superseded for the source-aware setting.

## 3. Original full heavy tail, root threshold and actual logical scope

The independently established original-source heavy-tail-to-D6 bound from [#659](https://github.com/definitely-stable/Mathlab/pull/659)/[#684](https://github.com/definitely-stable/Mathlab/pull/684) applies for **every epsilon**. Here the only changed numerical inputs are

\[
\begin{aligned}
T_{\rm source}&=\max\left\{1,
\left\lceil 2^{40}C_{\rm graph}^3
\left(\frac{4096}{1787}\right)^6\right\rceil
\right\},\\
\alpha_{\rm source}&=c_{\rm graph}
\left(\frac{1787}{4096}\right)^{12}2^{-72},
\qquad
\delta_{\rm source}=\min\{1/8,\alpha_{\rm source}\}.
\end{aligned}\tag{B7}
\]

As before, the **independently known**, positive but numerically unspecified graph theorem constants `C_graph,c_graph` must be supplied; the published Jiang–Yepremyan graph supersaturation statement makes them existential, not `C=c=1`. If `D6>=delta_source*s6` we finish; otherwise the contrapositive with the SAME fixed f,g guarantees `E_T<epsilon_source*s4`, and (B5) guarantees the inherited paired ORIGINAL core meets `m0>=s4`. ALL other proper-path and original sixset steps are those of the frozen #672–#689 stack. No silent strengthening of those lemmas is asserted.

The unchanged three loss thresholds produce the exact integer sufficient certificate

\[
\begin{aligned}
s_0=\max\{&
64,816T,144\cdot21(64\cdot65^3)^2L_6,\\
&48^8(\widehat B_0 T\widehat L_4)^4\},\quad
h_0=\max\{1,\lceil\log_2s_0\rceil\},\\
L_6&=24+288T^2,\qquad
\widehat B_0=64\lceil\sqrt{65T}\rceil,\\
\widehat L_4&=2(16\cdot65^2)^2\lceil\sqrt{8L_6}\rceil+40T.
\end{aligned}\tag{B8}
\]

In the `D6` branch the #688 sharp full-ten-sign GF5 coefficient is `54162`, in the `B/B-overlap` branch the exact universal coefficient is `53526`. Conditional on the COMPLETE geometric Branch A proof chain, for all dyadic s above the symbolic s0,

\[
\boxed{
R_3(f,g)\ge
\frac{\min\{54162\delta_{\rm source},53526/8\}}{51^6}s^6.
}\tag{B9}
\]

This is a **risk lower**, not a signed union probability, or upper bound for R2/R3, or ASET exponent outside the specified W(3,s)/classical alteration model.

### HYPOTHETICAL finite algebra regression — *not* published constants

If we substitute illustrative `C_graph=c_graph=1` (NOT asserted by the paper), the exact new integer certificate gives:

| Input | #689 coarse eps=13/32 | NEW source-aware eps=1787/4096 |
|---|---:|---:|
| Exact T | 244590498757546 | **159445475251527** |
| Sufficient dyadic h0 | 714 | **708** |
| Heavy D6 coefficient | `c*(13/32)^12/2^72` | **`c*(1787/4096)^12/2^72`** |

The exact T and h0 values are only symbolic-coefficient arithmetic falsifiers. Nothing in this PR supplies or claims *actual* published graph-theorem numerical constants or an attainable source order `W(3,2^708)`.

## 4. Two independent original input checks and acceptance boundary

The all-h analytic inequality (B3)–(B5) is the proof; finite runs serve only as falsifiers:

1. **Symbolic / integer oracle** computes exact `a,N,C_s` using integer square root and binomial minimality, with ZERO floating-point arithmetic. Verifies (B2) strictly above (B5) at dyadic exponents 6–26 (including both even/odd h); exact source labels; every rational factor of (B5); multiple C,c rational symbolic input pairs; exact h0 rounding and threshold dominance.
2. **Independent genuine ORIGINAL W32/W34 source-book check** rebuilds original flags with actual `genuine_source`, assigns two **complete separately globally injected correlated** typed f,g maps, independently counts each original point-pencil and line-pencil physical coordinate population, their binomial collision books and all ORIGINAL flag-pair conflict edges; requires the exact identity `|conflicts|=M_f+M_g` and each spectral book <=the true formula `C_s`. Exercise multiple cyclic right-label correlations and invalid inputs.
3. **Original six-ID and physical transfer** are inherited from previously independently tested frozen [#684–#688](https://github.com/definitely-stable/Mathlab/pull/688), NOT rebranded as newly independently proved by the two items above. The new code does not import the prior #689 threshold calculator.

**STOP and next gate:** Root #230 remains `OPEN_WITH_FORMAL_BLOCKER` until a qualified independent extremal-combinatorics referee checks the ENTIRE main geometric proof, including the external simple-C6 input and true-original physical/source sixset bijections. Passing new source budget tests or PR CI is not a substitute. No automatic merges, root closure, or unqualified `PROVED_A` claim.
