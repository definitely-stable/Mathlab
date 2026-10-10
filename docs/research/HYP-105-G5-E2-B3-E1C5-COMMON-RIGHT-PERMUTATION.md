# HYP-105 B3.2-E1-C5 — ONE shared right permutation, seven-overlap moments, occupied target almost-completeness

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), #176. Stack: #249 C0 → #260 C1 → #261 C2 → #266 C3 → #269 C4 → C5.

**TYPE: RESTRICTED_THEOREM_C / exact all-h single-common-permutation first/second moments, plus fixed-physical-image random-right mean Omega(s^6). This is NOT the all-correlated deterministic obstruction of #230, NOT a seven-family count, NOT a full 51-GF5-column R3 bound, and NOT an ASET exponent.**

## 1. Fix all physical labels at once — correct C4's quantifier weakness

For every h>=1, s=2^h, V=(s+1)(s²+1), let f be ANY injected original-left point → physical edge K_a map and let F⊆E(K_a) be ANY physically occupied right pair-label set of size V (including those chosen adversarially, perhaps correlated with f). Minimal a with K=C(a,2)>=V; missing labels t=K−V<a.

The genuine B-left/six-distinct-original-right weighted original 6-hypergraph is m_f(R), one ORIGINAL 6-incidence set per unit as in C0/C1/C4, |R|=6 and R⊆L_s. The PHYSICALLY OCCUPIED target is

```text
T(F) = {Q⊆F: |Q|=6 and Q is a simple six-edge 2-regular physical graph}.
```

Fix one abstract index set [V] for F; let Pi be **one uniform bijection of all V original right lines onto all V occupied physical pair labels**. Define

```text
U(Pi) = Σ_{R⊆L_s,|R|=6} m_f(R) 1[Pi(R)∈T(F)].
```

Crucial improvement over C4: **EVERY original distinguished concurrent pair and EVERY conditional four-line continuation uses this SAME Pi.** Thus U(Pi) is the correct global B/A overlap with the selected occupied physical image F under one sampled right injection. No inconsistent per-P conditional randomizations enter the calculation.

The fixed adversarial g remains ONE deterministic member of this bijection space. Its U(g) is not bounded below merely by E[U(Pi)].

## 2. Universal all-h density of occupied targets (NEW fixed-image random mean result)

The physical T_a has T=70*C(a,6) six-edge 2factors. A given physical edge occurs in D=28*C(a−2,4) targets, exactly by C0's 1-design. Every target absent from T(F) contains at least one missing physical edge. With t=K−V missing physical labels, elementary union bound yields for ALL F

```text
|T(F)| >= T − t D
       = 70*C(a,6) − 28*t*C(a−2,4)
       = 70*C(a,6) * [1 − 12*t/(a*(a−1))],
```

truncated at zero if necessary. No random F, no independence of f and F, and no structural knowledge of missing-label placement is required. Since minimality yields t<a and a~sqrt(2)s^(3/2),

```text
|T(F)|/|T_a| >= 1−O(1/a) = 1−O(s^(−3/2)).
```

This does NOT contradict C4's anchor-level q_F(z)=0 example: a few particular anchors may lose all completions while globally almost all target sixsets survive.

Conditional on fixed original source m_f and occupied F, every original sixset R maps under the ONE uniform Pi to each unordered sixset of F equiprobably, so

```text
E_Pi U = M(f)*|T(F)|/C(V,6).
```

C0's accepted all-h original-sixset mass floor H_B^−(s) is uniform over ALL f, with H_B^−=(1/4−o(1))s^15, a=(sqrt(2)+o(1))s^(3/2), and V=(1+o(1))s³. Hence the new **fixed-image** all-h lower theorem:

```text
E_Pi U >= H_B^−(s)*[70*C(a,6)−28*t*C(a−2,4)]_+ / C(V,6)
       = (140−o(1))*s^6,
```

uniformly over all f,F. It strengthens C0's random-right expectation by conditioning on an arbitrary *fixed right-image set* F. It does NOT prove U(f,g)=Omega(s6) for every g nor bound the remaining six positive motif families.

## 3. Exact global second moment under ONE common Pi: seven overlap classes

Let the ORIGINAL source and occupied physical target sixsets be respectively indexed on abstract vertex sets of size V. For j=0,..,6 define the full ordered weighted source intersection spectrum and physical target spectrum:

```text
S_j = Σ_{R,R':|R∩R'|=j} m_f(R)m_f(R'),
Q_j = #{(A,B)∈T(F)^2: |A∩B|=j}.
```

For any ordered source pair R,R' with j common original right factors, its joint image (Pi(R),Pi(R')) is UNIFORM over the

```text
D_j = C(V,6)*C(6,j)*C(V−6,6−j)
```

ordered physical target candidates sharing exactly j physical edge labels (when D_j>0). This yields

```text
E_Pi U² = Σ_{j:D_j>0} S_j*Q_j / D_j,
Var_Pi U = E_Pi U² − (E_Pi U)² >=0.
```

No separate-P randomization, no independence between the two copies of U, and no claim that different original right-line pairs have independent image labels. This is classical intersection algebra, not a novel standalone Johnson-scheme theorem.

The Paley–Zygmund/Cauchy and Chebyshev consequences are exact:

```text
Pr_Pi[U>0] >= (E U)^2/(E U²),        if E U²>0;
Pr_Pi[U=0] <= min(1,Var U/(E U)^2), if E U>0.
```

These are claims about **fraction of ALL right bijections with fixed F**. They give no lower bound on the minimum over all g.

## 4. Exact polynomial-in-source-support oracle (no quadratic Cartesian-product scan)

For ANY nonnegative original-sixset source (including genuine GQ m_f) define for k=0,..,6

```text
d_k(Q)=Σ_{R⊇Q}m_f(R),           Q⊆L_s, |Q|=k,
A_k=Σ_{|Q|=k}d_k(Q)².
```

By double-counting ordered weighted original-sixset pairs,

```text
A_k = Σ_{j=k}^6 C(j,k) S_j.
```

Exact binomial inversion gives

```text
S_j = Σ_{k=j}^6 (-1)^(k−j)*C(k,j)*A_k.
```

Apply the same construction to indicator weights of all occupied physical target sixsets to calculate Q_j. The executable reference enumerates at most Σ_k C(6,k)=64 subsets of EACH stored sixset, accumulates seven exact integer marginal-squared totals and inverts, avoiding an O(|supp m_f|²) scan. For W32 this keeps ~3076 original right sixset source cells intact; no 6! weights are added.

The reference separately validates nonnegative S_j, Σ_j S_j=M², and every inverted A_k, and computes E, E², variance and both rigorous probability bounds using Fraction without floating error.

## 5. Independent finite falsification — including a GENUINE GQ fixed-g barrier

[Reference implementation](../../research/hyp105_g5e2b3e1c5_common_bijection.py) imports frozen C0 true ORIGINAL source, C0 GQ all-h mass floor, and the accepted 70 physical 2factor templates. The finite exact target generator only enumerates a≤9; the all-h occupancy and expectation theorem is symbolic with no finite-a cutoff.

[Independent tests](../../research/test_hyp105_g5e2b3e1c5_common_bijection.py) implement independent brute ordered-pair sixset intersection spectra, independently scan ALL physical six-edge subsets for a=6/7 (without 70-template generation), and exhaust **every one of the 8!=40320 common ORIGINAL-right permutations** for a toy occupied F⊆E(K6) with V=8, verifying E, E², variance and the exact positive-probability bounds against the brute distribution.

Genuine W(3,2) original six-incidence source m_f has exactly M=5000 and full occupied K6 physical T(F) has exactly 70 targets. Therefore E_Pi U=5000*70/5005 EXACTLY. The reverse-line physical map yields U=77, while swapping just original-right line physical labels (4,13) yields U=57. These TWO genuine correlated right maps use the **SAME m_f and the SAME occupied F**, so their entire global E/Var/overlap spectra are EXACTLY THE SAME. Nevertheless their actual fixed-g overlap differs. This establishes directly on the GQ-restricted source, not just an abstract hypergraph, that global mean/variance alone do NOT determine the fixed-g overlap. (Both observed overlaps happen to remain positive, so this does NOT refute the conjectured universal Omega(s6).)

An auxiliary abstract one-sixset pair of sources sharing all intersection spectra and global moments but with fixed identity overlap 1 vs 0 is a generic mathematical falsifier, explicitly NOT a GQ source.

## 6. Decision boundary and next permitted step

The now-known positive bound (140−o(1))s6 applies to **uniform one-common-Pi expectation conditioned on ANY occupied F** and makes physical image shortage an asymptotically negligible global problem. The missing theorem is one of:

1. A genuinely **GQ-specific uniform discrepancy inequality** for ANY SINGLE injective g, controlling the full sum of correlated source/target sixset overlaps with an error strictly smaller than the (140−o(1))s6 benchmark, OR
2. An infinite, explicitly described legal correlated f_s,g_s family with the sum of **all seven** GF5-positive motifs o(s6), accompanied by exact all-h proof and full-risk caveat.

Neither a pointwise Paley–Zygmund typical-map estimate nor a small second moment proves option (1), and neither an abstract six-hypergraph countermodel nor a finite W32 labeling proves option (2). Further model-restricted GQ convolution/orbit-rank inequalities or certified infinite all-class constructions are needed.

Acceptance: **RESTRICTED_THEOREM_C** after *exact HEAD* dedicated GitHub-hosted C5 CI SUCCESS and full Research CI SUCCESS, merge entire stack #249/#260/#261/#266/#269/C5 in that order with SHA safeguards, then postmerge main Research SUCCESS. Until then **PENDING CI / NOT MERGED**. #230, #176, #169 remain OPEN; no ASET exponent.
