# HYP-105 B3.2-E1-C9 — all-h zero barrier for the 0/1/2-pin C8 rearrangement

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked research: C0 #249 merged → C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → C7 adversarial #279 → C8 #284 → C9. Parallel C7 conditional selector #280 is **not** an ancestor.

**TYPE: RESTRICTED_THEOREM_C / ALL-h_METHOD_BARRIER.** This is a valid negative theorem about the **specific C8 independent-per-fiber rearrangement bound**, not a theorem that any actual valid GQ right map g has U_B/A=0. It does NOT prove or disprove the seven-family (S_s=Ω(s^6)) obstruction, full GF5 R3, or an ASET exponent.

## 1. Precise result, with quantifiers

Let (s=2^h), (h\ge4), (V=(s+1)(s^2+1)), (a=\min\{a:\binom a2\ge V\}). For EVERY legal original GQ-left physical-pair embedding (f), EVERY occupied right physical-pair image (F\subseteq E(K_a)) of cardinality (V), EVERY subset (D\subseteq L_s) of at most **two** original right lines, and EVERY injection (p:D\hookrightarrow F), the C8 frozen-fiber independent-sixset rearrangement lower is exactly

\[
L_D(p)=0.
\]

Therefore the min-over-p certificate (L_D=0) too, even though the **actual** B/A overlap may be strictly positive for every common right bijection. This is a genuine all-h **bounded-2-pin-method NO-GO**: no larger left GQ size, choice of D, adaptive selection of its two pins, or physical target occupancy can rescue this specific relaxation for s>=16. It makes **NO assertion for k>=3**.

## 2. GQ concurrence and distinguished-pair support cover

It suffices to prove the claim for |D|=2. For k=0,1 extend any partial pin map to a 2-pin map, and use the C8 refinement monotonicity (0\le L_D(p)\le L_{D'}(p')=0\).

Fix |D|=2, an arbitrary p, and a class (X_A=\{R:|R|=6,R\cap D=A\}\), (r=|A|\in\{0,1,2\}). Let (n=V-2), (m=6-r); its capacity is (N_r=\binom n m\), independent of f,F,p. A necessary condition for a positive source weight (m_f(R)>0) is that R contain a concurrent pair of ORIGINAL GQ right lines (C1).

The original line-concurrence graph has degree (d=s(s+1)) and (E=Vd/2) undirected edges. Every positive-support R has a concurrent pair in one of three categories:

1. Both ends outside D: at most (E\binom{n-2}{m-2}\) sixsets by an exact union bound.
2. One end in A and one end outside D: at most (r d\binom{n-1}{m-1}\).
3. Both ends in A: only possible when r=2 and A is a concurrent pair. If this pinned pair is the UNIQUE distinguished doubled-point witness of the source motif, its total source multiplicity is at most (W=3\binom{a-2}{4}(s+1)^4\) by C3; the number of positive sixsets with that witness is no greater. If it is NOT the distinguished pair, its motif's actual distinguished pair lies in categories 1 or 2 and was already counted.

Thus for every class:

\[
|\operatorname{supp}(m_f)\cap X_A|\le
B_r:=E\binom{n-2}{m-2}
+r d\binom{n-1}{m-1}
+\mathbf1_{r=2}W.
\]

C0 provides the full physical 2-factor target count (T=70\binom a6\). Occupancy can only REMOVE physical targets, so every physical pinned fiber contains at most (T) target sixsets. If

\[
\boxed{B_r+T < \binom n{6-r}\quad(r=0,1,2),}
\]

each source class contains STRICTLY more zero-weight sixsets than the target class has occupied targets. Hence the C8 sum of the (t_A) smallest source weights is exactly zero, simultaneously for ALL p, all f,F. **This conclusion concerns the relaxation, not the realizability of the independently chosen class-level sixset permutations as ONE original-vertex map.**

## 3. All-h integer cases and non-extrapolated analytic tail

The [integer reference](../../research/hyp105_g5e2b3e1c9_two_pin_barrier.py) computes the exact three inequalities above for s=16 and 32, without any floating point approximation. For s>=64 the proof is symbolic and uniform, not inference from additional finite powers:

\[
V\le\tfrac{11}{10}s^3,\quad d\le\tfrac{11}{10}s^2,\quad
E\le\tfrac{121}{200}s^5,\quad
n,n-1\ge\tfrac{99}{100}s^3,\quad
n-3\ge\tfrac{98}{100}s^3,\quad a^2\le4s^3.
\]

The final inequality follows from minimality of a: ((a-1)(a-2)<2V), whence (a<\sqrt{2V}+2\), and (\sqrt{11/5}+2/s^{3/2}<2\) for s>=64. The remaining bounds follow directly from the explicit V and d.

For (m=6-r\in\{4,5,6\}), (r m\le8), (Δ=s+1\le1.1s), and ( \binom{n}{m}\ge\binom{n}{4}\ge(n-3)^4/24\), direct exact combinatorial ratios give

\[
\frac{E\binom{n-2}{m-2}}{\binom nm}
=\frac{Em(m-1)}{n(n-1)}<\frac{19}{s},\qquad
\frac{r d\binom{n-1}{m-1}}{\binom nm}
=\frac{r d m}{n}<\frac9s,
\]

\[
\frac{W}{\binom nm}<\frac{77}{s^2},\qquad
\frac{T}{\binom nm}<\frac{163}{s^3}.
\]

All inequalities above use rational coefficient comparisons: (500/27<19), (80/9<9), (439230000/5764801<77), (400000000/2470629<163). Summing,

\[
\frac{B_r+T}{N_r}
<
\frac{28}{s}+\frac{77}{s^2}+\frac{163}{s^3}
\le\frac{28}{64}+\frac{77}{64^2}+\frac{163}{64^3}<1,
\quad s\ge64.
\]

Together with exact **s=16,32** integer cases this proves the claim for **ALL powers (s=2^h,h\ge4\)**. No checking finitely many s is substituted for the analytic tail. The supporting code checks the exact coefficient inequalities using Python Fractions and also outputs exact numerical integer diagnostics at powers 2..1024.

## 4. Falsifiers and honest scope

[Independent tests](../../research/test_hyp105_g5e2b3e1c9_two_pin_barrier.py) check s=16,32 exact integer margins, the symbolic tail coefficients, original-GQ W(3,2) finite source support (both genuine f), full K6 physical 2-factor target count 70, small-s lack of the claimed certificate, genuine W32 C8 conditional lower consistency, and the generic V=8 positive-star one-pin countermodel (which does NOT satisfy the GQ hypothesis). W32 s=2 is below threshold and **no** all-s theorem is inferred from its zero/positive low-pin observations.

The C8 two-pin relaxation loses essentially all information about joint occurrence of the remaining four original GQ lines under the same right map. The theorem rules out improving its all-h B/A obstruction merely by choosing two special pinned original lines, optimizing their images, or changing the physical F. It does **not** rule out a different representation, a multi-line group constraint, k>=3, or the possibility that a true positive (\min_g U_{B/A}\) holds.

## 5. Acceptance and next research slice

**Acceptance PENDING** exact PR-head GitHub-hosted `hyp105-c9-contract` and full Research SUCCESS, then ordered dependency integration through #284 and C9, followed by postmerge main Research SUCCESS. Parent #230, #176 stay OPEN_WITH_FORMAL_BLOCKER. No UCT/other repos changed.

**C10 choice:** either prove a stronger k>=3 barrier with additional GQ conditioned-line marginals, or replace per-fiber independent sixset permutations by a model-preserving coupled physical completion constraint for the remaining four right lines. A genuine all-h seven-family theorem would require simultaneous same-`f,g` arguments; avoid another standalone random-right moment.

## C10 strengthening — three pinned original lines are also insufficient

[C10 proof](HYP-105-G5-E2-B3-E1C10-THREE-PIN-ZERO-BARRIER.md) proves the same exact zero C8 lower relaxation for ANY pinned set of cardinality <=3, ALL s=2^h>=16, ALL legal GQ f, occupied physical F, and images p. The additional ingredient is a distinguished original concurrent pair witness cap conditioned on a fixed THIRD original singleton right line plus an occupied physical target ONE-edge codegree cap. The C9 two-pin no-go remains valid and is strictly subsumed. This says NOTHING about an actual zero-overlap g.
