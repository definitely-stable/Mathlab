# HYP-105 B3.2-E0 — simultaneous non-strict all-h GF(5) risk, with exact conditional-mean selection

Date: 2026-10-10. Parents [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169), [#162](https://github.com/definitely-stable/Mathlab/issues/162), [#95](https://github.com/definitely-stable/Mathlab/issues/95). This slice is **proof-first**. It corrects a quantifier blind spot, NOT the missing strict exponent.

**PROVED: one and the SAME injective two-color labeling exists for every h with R2=O(s^4) and R3=O(s^6); deterministic but computationally impractical exact conditional-expectation selector; no strict R3 exponent, no improved ASET lower, no new global mathematical priority, no efficient explicit correlated finite-field construction.**

## 1. Frozen model / accepted premises

For s=2^h (h>=1), W(3,s) has V=(s+1)(s^2+1) factor vertices in each color class, N=(s+1)^2(s^2+1) incidence columns, and a=min{j:binom(j,2)>=V}, K=binom(a,2). The left and right physical coordinate blocks are disjoint, each vertex gets an injectively chosen unordered coordinate pair from K_a. The two injections are sampled independently and uniformly; this is ONE common probability space Omega_s of ((K)_V)^2 finite outcomes.

The GF(5) coefficient palette is the complete 51 all-nonzero checksum-4 weights per selected column. R2(f,g) and R3(f,g) are exact sums of all un-ordered signed 2v2 and 3v3 collision probabilities over independently chosen weights, respectively. They are finite, deterministic, nonnegative rationals for any physical pair labeling; NO unit-only events or seven-column witness selection substitutes for the full risks.

Accepted all-h inputs on the SAME Omega_s:
- [E2-B2](HYP-105-G5-E2-B2-RANDOM-R2-BOUND.md) proves mu2(s)=E_Omega[R2]=O(s^4).
- [E2-B3.0](HYP-105-G5-E2-B3-FOREST-PROJECTION.md) proves mu3(s)=E_Omega[R3]=O(s^6). Older matching/cherry positive motifs prove mu3(s)=Omega(s^6); GF5-positive matching motifs also imply mu2(s)>0. The mean upper exponents, not any fixed-label bounds, are the premises.

## 2. All-h simultaneous Pareto first-moment theorem

**Theorem E0-A.** Let two nonnegative functions X,Y on ONE finite probability space have finite positive means muX,muY. For every rational 0<lambda<1 there exists an outcome omega with

```text
lambda X(omega)/muX + (1-lambda) Y(omega)/muY <= 1.
Consequently:
X(omega) <= muX/lambda,
Y(omega) <= muY/(1-lambda).
```

Proof: The expectation of the weighted sum on the left is exactly 1. If every outcome exceeded 1, the mean would exceed 1. Both terms are nonnegative, so each obeys its own bound. If a mean is zero, its nonnegative function is identically zero on the finite full-support probability space; omit that term. The theorem is elementary linearity of expectation, not a new extremal geometry theorem.

**Corollary E0-B (joint non-strict all-h rates).** Choose lambda=1/2 and X=R2, Y=R3 on Omega_s. For every h>=1 there is ONE (f_s,g_s) such that simultaneously

```text
R2(f_s,g_s) <= 2*mu2(s) <= 2*C2*s^4,
R3(f_s,g_s) <= 2*mu3(s) <= 2*C3*s^6,
```

for constants C2,C3 independent of h, whose existence follows from the accepted expectation upper proofs. Hence the weak simultaneous target previously left implicit is now rigorously established. It is strictly weaker than the required R2=O(s^(26/5-eps2)), R3=O(s^(6-eps3)) for eps2,eps3>0, because the R3 bound has **no positive power saving**.

Importantly, taking the individually good R2 witness from one existential proof and an unrelated individually good R3 witness does NOT prove they are the same. This theorem works precisely because both random variables are defined on the same Omega_s, and it selects them by a JOINT nonnegative objective.

## 3. Deterministic selector by exact conditional expectations

Fix the existing deterministic ordering of all factor vertices in each color and the lexicographic ordering of all K_a pair labels. Reveal all left assignments, then all right assignments, always selecting a currently unused pair label within its own color. Starting from

```text
J_lambda = lambda*R2/mu2+(1-lambda)*R3/mu3, E[J_lambda]=1,
```

at every prefix consider ALL currently available candidate pair labels x; their conditional expected J values average to the current conditional expectation because a uniform random injection extends any fixed prefix uniformly over the remaining bijective choices. Select a minimizing candidate, using smallest pair label to break ties. This cannot increase the conditional expectation. Once 2V assignments are exposed, the conditional expectation is the exact realized J<=1. This gives a deterministic, fully specified all-h (f_s,g_s) obeying the joint bounds. Each selected map depends on all the source incidences and exact finite risks, not on an assumed Sp(4,s) symmetry.

**Complexity boundary:** the selector is generally prohibitively expensive: full R3 evaluations require GF5 exact signed-event accounting over N columns and conditional means range over enormously many remaining injections. It is an explicit finite *definition/algorithm*, not a practical polynomial-time or algebraic Pluecker/trace map. No claim that the selector improves R3 exponent or can be executed at realistic s=4/8 is allowed.

The Python reference [E0 finite conditional-expectation model](../../research/hyp105_g5e2b3e0_joint_first_moment.py) enumerates **all** two-sided injective assignments only for tiny bounded alphabets and computes an exact rational Pareto certificate from a supplied oracle. The [independent tests](../../research/test_hyp105_g5e2b3e0_joint_first_moment.py) reproduce the 36-outcome example without calling the model's enumeration, check all prefixes and lex ties, nonnegativity, zero-mean behavior, negative costs, and fail-closed state budgets. The example intentionally uses two **toy physical pair-label diagnostics**, not the full GF5 R2/R3; it validates only the generic derandomization machinery. The all-h HYP-105 result is the mathematical consequence of the independently accepted two actual expectation bounds.

## 3A. New sharp all-h random-leading GF(5) coefficient for the FOUR #224 classes

This is a second, distinct model-specific theorem, sharpening #224's separate Theta(s^6) random expectation assertions to a **fully specified leading coefficient**, without assuming exact finite-h GQ forest counts.

**Theorem E0-C (six-edge forest embedding asymptotic).** For any fixed typed bipartite six-edge **forest** F with c components, let Emb(F,W(3,s)) be the number of injective, color-preserving embeddings of its distinct abstract factor vertices, retaining all SIX prescribed incidence edges. Root each component in a prescribed side, choose each root from V=(s+1)(s^2+1) typed factor vertices and grow its tree children through Delta=s+1 neighbors. Since at most twelve factor vertices have been selected at any step, forbidding earlier vertex images removes at most twelve choices. Therefore, for s>=16,

```text
(V-12)^c*(Delta-12)^6
  <= Emb(F,W(3,s)) <= V^c*Delta^6.
```

This proves Emb(F)=V^c Delta^6 (1+O(1/s)) as s=2^h grows. It does not assert the number is EXACTLY V^c Delta^6 for finite s. Extra unselected incidences between already selected vertex images do not invalidate an embedding of the **selected** six-edge forest. This is an elementary greedy-counting result for a fixed bounded forest, and the valid bound depends on the incidence graph being typed, simple, V-vertex-per-side and Delta-regular, not on treating any Sp(4,s) automorphism as a physical-coordinate symmetry.

**Corollary E0-D (leading model-specific random GF5 risk constant).** The #224 six-coordinate leading physical projection classes are A=all six factor endpoints distinct, B=one repeated endpoint, and C=three disjoint repeated pairs. Every class tau below has exactly t_tau *named ORIGINAL factor endpoint-partition pairs* among six numbered selected column positions. Each un-ordered original six-incidence edge set has exactly 6! named orders, so

```text
M_tau(W(3,s))
  = (t_tau/6!) * V^(c_tau) * Delta^6 * (1+O(1/s)),
```

where t_tau=(30,360,120,90), c_tau=(3,2,4,4). Do **NOT** treat these t_tau as physical signed-template counts: those were 21,000/10,800/10,800/8,100. Multiplying by signed-template counts here would overcount 3v3 events.

Combine the accepted exact per-original-factor-forest sum S_tau, each physical-coordinate automorphism divisor d_tau, and the exact independent-injection formula from #224:

```text
E_random[R3_tau] = M_tau * S_tau*(a)_6^2
                   / [d_tau*51^6*(K)_rL*(K)_rR],
K=binom(a,2),  a=min{n:binom(n,2)>=V}.
```

Since rL+rR=c+6, a^2/V -> 2, K/V -> 1, and Delta/s ->1, all powers of V cancel; thus its leading coefficient is **exactly** 64*t_tau*S_tau/(720*d_tau*51^6).

| New class | t_tau | c | d_tau | S_tau | Leading numerator over 51^6 |
|---|---:|---:|---:|---:|---:|
| C/A (both orientations) | 30 | 3 | 8 | 4,243,968 | 1,414,656 |
| C/B (both orientations) | 360 | 2 | 16 | 173,682 | 347,364 |
| B/B intersecting pairs | 120 | 4 | 4 | 482,670 | 1,287,120 |
| B/B disjoint pairs | 90 | 4 | 4 | 558,080 | 1,116,160 |
| **TOTAL new four classes** | **600** | — | — | — | **4,165,300** |

Therefore for these four NEW restricted classes, and ONLY for uniformly independent two-color physical-pair injections,

```text
E_random[R3_new_leading] =
  (4,165,300 / 51^6) * s^6 * (1+O(1/s)).
```

This proves the exact leading constant for this additive **subset** of R3. It does not give an upper for global R3 (other 11,032 structural shape classes remain); it is NOT an all-label R3 lower and cannot rule out exceptionally correlated deterministic pair labels. The leading coefficient is a model-specific combinatorial calculation, not an assertion of publication priority.

The [independent rational certificate](../../research/hyp105_g5e2b3e0_random_intensity.py) derives all four leading numerators, checks finite-h positive lower/upper sandwiches without replacing actual M_tau by its asymptotic, and [tests](../../research/test_hyp105_g5e2b3e0_random_intensity.py) independently scan the 203x203 abstract endpoint partitions to reproduce t_tau and check convergence of the exact rational embedding bounds for large s. No binom(425,6) enumeration or fixed-label GF5 risk is claimed.

## 4. What this proves and what it does not

PROVED in this scope:
1. Simultaneous per-h existence for **non-strict** R2~s^4, R3~s^6 with constants uniform in h.
2. Deterministic lexicographic conditional-expectation construction (exponential/unbounded runtime).
3. Weighted two-risk Pareto trade-off for any fixed lambda; this cannot be inferred by picking separate witnesses.

NOT proved:
1. Uniform positive exponent epsilon3 in R3=O(s^(6-epsilon3)).
2. Any finite GF2/GF4 Pluecker map satisfies these all-h estimates.
3. An unconditional all-label fixed-map lower R3=Omega(s^6): independent-random mean Omega(s^6) permits exceptional maps.
4. A new ASET exponent, equality with A_lin, or novelty over the classical first-moment/conditional-expectation method.

**Next B3.2-E1:** choose a genuinely structured all-h correlated labeling family or derive a universal obstruction on physical six-motif multiplicities. Enumerating finite GF5-positive types and comparing two small s values is not an asymptotic geometric proof. Test the non-strict joint selector as a baseline only. A further rigorous path is to bound *for the same fixed map* all positive four- and six-column events, or derive exact degree/codegree conditions for stronger-than-alteration extraction. Keep #176/#169/#162/#106/#95 OPEN.

## 5. Source and CI scope

The mathematical technique is the classical first-moment / method of conditional probabilities, so this slice needs no new canonical literature ID and makes no original-priority claim. Existing GF5 flow reference is Fu–Ren–Wang 2025 as already cataloged; Naor–Verstraete and Lefmann comparator bounds remain unchanged.

Acceptance gate: Python standard-library exact Fraction/reference checks, independently enumerated tiny model, GitHub-hosted **Research SUCCESS on exact PR HEAD**, plus postmerge CI. A green finite toy does NOT independently establish the all-h premise; the two cited accepted mathematical lemmas are authoritative.
