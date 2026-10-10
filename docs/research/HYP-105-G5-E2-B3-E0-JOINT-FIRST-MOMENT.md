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
