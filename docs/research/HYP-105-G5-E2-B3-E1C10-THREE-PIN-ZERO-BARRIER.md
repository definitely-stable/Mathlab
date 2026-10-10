# HYP-105 B3.2-E1-C10 — all-h zero barrier for three pinned right lines

Date 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked: C0 #249 merged → C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → C7 #279 → C8 #284 → C9 #285 → C10. C7 conditional-expectation PR #280 remains a separate complementary branch.

**TYPE RESTRICTED_THEOREM_C / METHOD_BARRIER.** Valid all-h theorem about the C8 independent-per-fiber rearrangement LOWER CERTIFICATE, not about the actual original-GQ min_g U_B/A or all-seven-motif S. **No claim** any true correlated g has zero overlap.

## 1. Strict improvement over C9

For every s=2^h>=16, every legal injective GQ left pair-label map f, every occupied right physical K_a pair-edge image F of size V, every set D of at most **THREE** original GQ right lines, and every injective partial physical mapping p:D→F,

\[
\boxed{L_D(p)=0.}
\]

Here L_D(p) is exactly the classwise *independent 6-set cell permutation rearrangement* relaxation defined in C8, NOT the optimum over genuine common vertex maps g extending p. Since the result holds for every p it also holds after minimizing over p. It covers D=0,1,2 by C8 monotonicity and extends C9's two-pin all-h NO-GO.

## 2. Conditioned original-GQ source-support cover

Fix three original right-line pins D and an arbitrary p. In each source class X_A={R:|R|=6,R∩D=A}, let r=|A|∈{0,1,2,3}, n=V-3, m=6-r, N_r=C(n,m). Original right concurrence graph Γ_s has degree d=s(s+1), E=Vd/2 edges (C1). Every positive original source sixset R contains a pair of concurrent ORIGINAL right lines. A pair not fully inside A is union-covered by

\[
E\binom{n-2}{m-2}+r d\binom{n-1}{m-1}.
\]

If the UNIQUE distinguished doubled-point original-line pair of an actual positive B-left source motif lies entirely among the pins, distinguish r=2 or r=3:

- For r=2, the source-support count is no larger than the C3 weighted witness cap W_2=3 C(a-2,4)(s+1)^4. This remains valid even when a pinned concurrent pair is not actually a distinguished pair.
- For r=3, choose the distinguished original pinned pair {u,v}, fixing their unique original doubled point x. The third pinned ORIGINAL right line w must occur at ONE of the four singleton original left points q. There are at most Δ=s+1 choices q incident to w; f(q) is one physical pair edge of a four-cycle disjoint from f(x), and belongs to exactly 2 C(a-4,2) physical C4 cycles on the remaining physical coordinate vertices. The other THREE singleton original line endpoints have at most Δ³ choices. Thus each fixed distinguished pair and pinned third line appears with multiplicity at most

\[
W_3 = 2\binom{a-4}{2}(s+1)^4.
\]

There are at most three choices of the distinguished pair among the three pins, giving ≤3W_3 positive sixsets (support≤weighted multiplicity). If its distinguished pair is NOT fully pinned, the motif was already union-counted by a pair outside/in crossing D. **The original-to-physical distinction is preserved throughout.**

Consequently,

\[
B_r=E\binom{n-2}{m-2}+r d\binom{n-1}{m-1}
+\mathbf{1}_{r=2}W_2+\mathbf{1}_{r=3}3W_3
\]

is a valid all-f, all-D upper bound on the number of positive source sixsets in X_A.

## 3. Physical target occupancy — the additional essential refinement

The complete physical K_a six-edge simple 2-factor target has T_0=70 C(a,6) sixsets (C0/C5). Every individual physical pair edge belongs to exactly

\[
T_1=28\binom{a-2}{4}
\]

of them. The fixed occupied physical image F can only remove target sixsets.

For a target conditional class with r=0, target count ≤T_0. For r≥1, **every target in that class contains the p-image of at least one pinned original line**, and target count ≤T_1 independently of any other pinned physical edge geometry. Set Q_r=T_0 if r=0, otherwise Q_r=T_1.

The certificate sufficiency condition is

\[
\boxed{
B_r+Q_r<\binom n{6-r} \quad(r=0,1,2,3).
}
\]

If true, every class X_A has at least Q_r zero-weight source cells. Every classwise source-target assignment in the C8 relaxed space can fill its target positions with zero source weight, so L_D(p)=0, uniformly over all D,p and f,F.

## 4. All-h proof, not numerical extrapolation

Exact integer evaluation of all FOUR strict inequalities proves them for s=16 and 32. For every real s≥64 the following elementary parameter bounds are uniform:

\[
V\le1.1s^3,\ d\le1.1s^2,\ E\le(121/200)s^5,\
n,n-1\ge0.99s^3,\ n-3\ge0.98s^3,\ a^2\le4s^3.
\]

The last bound follows from the minimality of the complete physical edge alphabet a, as proved in C9. With m=6-r, m(m-1)≤30, rm≤9, and binomial ratio identities, the unpinned/crossed concurrence counts contribute respectively less than 19/s and at most 10/s of N_r.

For r=2, W_2/N_r<77/s² (C9). For r=3, 3W_3/N_r<113/s² using 3W_3≤3 a² Δ⁴≤12(1.1)^4 s^7 and C(n,3)≥(0.98s³)^3/6. The new physical target degree-one bound gives, for r≥1, Q_r/N_r<119/s³ because Q_r≤(56/3)s^6 and N_r≥C(n,3)≥(0.98s³)^3/6. For r=0, T_0/C(n,6)<163/s³ as in C9. Thus

\[
\frac{B_r+Q_r}{N_r}
<
\frac{29}{s}+\frac{113}{s^2}+\frac{163}{s^3}
\le\frac{29}{64}+\frac{113}{64^2}+\frac{163}{64^3}<1.
\]

All coefficients are independently checked as exact rational fractions by [the reference](../../research/hyp105_g5e2b3e1c10_three_pin_barrier.py), not fitted to integer examples. Together with the exact two base cases this proves ALL s=2^h≥16, with **no assertion below s=16**.

## 5. Independent falsification, acceptance, next direction

[Independent finite tests](../../research/test_hyp105_g5e2b3e1c10_three_pin_barrier.py) compare the all-h integer capacity inequalities, rational coefficients, actual original GQ W32 B-left weighted support for both genuine left maps and multiple pinned triples, true K6 physical 2factor edge degree 28 and total 70, and concrete actual W32 right maps (s=2, below threshold) against C8 three-pin relaxation. All experiments remain lower-bound METHOD diagnostics; no all-g crossing inferred.

**Acceptance PENDING** exact-head hosted `hyp105-c10-contract` and complete Research SUCCESS; merge only after C1–C9 predecessor stack passes its respective CI and integrates in order. Parent #230/#176 OPEN_WITH_FORMAL_BLOCKER, no GF5 R3 or ASET exponent.

**C11 research gate:** three pins are provably insufficient for this relaxation; study higher k only with explicit support marginals and physical target orbit codegrees, or change to genuinely **coupled conditional four-original-line completion** rather than independent per-class sixset permutation. A proposed theorem must explicitly state whether it applies to true original-to-physical correlated g or merely to a lower relaxation.
