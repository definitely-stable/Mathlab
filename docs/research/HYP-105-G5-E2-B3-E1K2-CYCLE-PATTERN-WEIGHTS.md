# HYP-105 B3.2-E1-K2 — GF5 weights of all Kikuchi cycle patterns and Theorem K′ for R3

Date: 2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Continues [E1-K1](HYP-105-G5-E2-B3-E1K1-KIKUCHI-C6-SUPERSATURATION.md) in the same main-based PR.

**STATUS: RESTRICTED_THEOREM_C.** The finite classifications K4 and K5 and the identity D2 hold for every s=2^h. Theorem K′ is a conditional R3 floor. The only open term is the coincidence mass Θ. No Branch A/B decision and no ASET exponent are claimed.

## 1. Why patterns are finite

Take a cycle of the Kikuchi graph Ĝ (K1) with vertices (x_i, y_i). Its i-th column has support {x_i, x_{i+1}} ∪ {y_i, y_{i+1}}. The coincidence pattern of the 12 endpoint symbols is therefore fixed by two *cyclic closed-walk patterns*. A cyclic closed-walk pattern is a sequence x_0…x_{n−1} with cyclically adjacent entries different, taken up to relabelling of symbols.

The exact 51-palette GF5 count of a signed column family depends only on this incidence pattern. It does not depend on s, a, f or g. So a finite enumeration gives an all-h statement. Patterns that cannot occur in W(3,s) (for example, two points sharing two lines) are included, which only enlarges the checked family.

## 2. Lemma K4 (six-cycles)

There are 41 cyclic walk patterns of length 6. Among the pattern pairs that form a cycle of a simple graph:
- **879** have six distinct columns;
- **50** use both diagonals of one column (the degenerate term C6_rep).

For each of the 879, the full-palette alternating 3v3 weight (signs +−+−+− along the cycle, `exact_dual_GF5_six_flow`) is at least **5643**. Equality holds exactly for proper cycles, which are the accepted D6 family. The minimum weight depends on the numbers of distinct x and y coordinates:

| #x × #y | 6×6 | 6×5 | 6×4 | 5×5 | 6×3 | 4×4 | 3×3 | 2×5 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| min weight | 5643 | 17955 | 57456 | 57456 | 182460 | 590998 | 6201744 | 2813206 |

At most **4** Kikuchi six-cycles use the same six columns.

## 3. Lemma K5 (four-cycles)

All 9 four-cycle patterns automatically have four distinct columns. Their alternating 2v2 weight is at least **531**, with equality exactly for proper four-cycles, which are the accepted Q4 family (`closed_form_c4_GF5_flow_weight`). At most **2** four-cycles use the same four columns. Hence

```text
51⁴·R2(f,g) ≥ (531/2)·C4(Ĝ).
```

So the four-cycle part of Θ is controlled by R2 itself.

## 4. Identity D2

For every simple graph,

```text
Σ_e C(c4(e),2) = #(six-cycle, antipodal chord) + #(C4 pairs sharing a 2-path) + #(other degenerate pairs),
```

because two four-cycles sharing exactly one edge (and no other vertex) form a six-cycle with that edge as an antipodal chord. Hence 3·C6 ≥ Σ_e C(c4(e),2) − book − degenerate, and Σ_e C(c4(e),2) ≥ 8·C4²/|E| − 2·C4.

## 5. Theorem K′

For every s=2^h and all legal f, g, combine K1–K3 with K4. Different cycles realise different six-incidence sets up to multiplicity 4. The alternating sign pattern is one of the ten balanced patterns counted in R3. Therefore

```text
51⁶·R3(f,g) ≥ (5643/4)·[ (L(P3) − Θ)/12 − C6_rep ],   L(x) = x(x/a⁴ − 1).
```

Compared with Theorem K, the improper-cycle term has disappeared. This bound is about the full R3, which is the quantity the extraction goal needs, rather than the seven-family S. Measured C6_rep/s⁶ is 0.66, 0.02 and 0.002 at s = 2, 4, 8.

**Remaining blocker.** Θ ≤ (48−ε)s⁶. By K5 and D2 this reduces to a regularity statement: the four-cycle mass of Ĝ must not concentrate on high-degree vertices ("hubs", meaning large star-incidence counts n(x,y)) or in books K_{2,t}. With C4=λs⁵ and C4-weighted mean degree κs, combining K and D2 gives C6 ≳ (4/3)λ*²s⁶ with λ*²+κλ*−3=0. For example, the right-hand side is (4/3)s⁶ at κ=2 and 0.39s⁶ at κ=5. This step is a sketch, not part of the checked lemmas.

## 6. Finite evidence

On W32 (report-pinned), the Kikuchi-cycle six-sets alone give R3 numerator lower bounds of 103,920,064 (lex, 671 distinct sets) and 63,531,068 (reverse-line, 435 sets). These exceed the accepted seven-family floors 11,225,795 and 7,627,209, because improper cycles are subleading but positive shapes.

The s=4 random model satisfies Theorem K′ inside the tests. The D2 identity holds exactly on W32 lex (299 = 299) and on 25 random graphs.

## 7. Independent checks

- **Weights.** Weights are recomputed by a 3+3 meet-in-the-middle palette count that does not use the Fourier dual. The checked patterns are the proper one, three 6×5/5×6 patterns and four random ones. All nine four-cycle weights are recomputed by enumerating three columns and solving for the fourth.
- **Walk patterns.** The walk-pattern counts are recomputed by brute-force canonicalisation over all colourings.
- **Fail-closed checks.** The multiplicity bound and Theorem K′ are asserted on four random W32 bijections and on the s=4 random map. Invalid inputs fail closed.

**Acceptance:** same as K1. Exact-head contract and Research must both succeed, followed by post-merge main Research. #230 stays open.
