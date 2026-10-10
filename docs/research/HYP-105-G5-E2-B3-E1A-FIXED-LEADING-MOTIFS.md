# HYP-105 B3.2-E1-A — complete finite fixed-label leading six-motif census for W(3,2)

Date: 2026-10-10. Research parent: [#176](https://github.com/definitely-stable/Mathlab/issues/176). Builds on merged [#214](https://github.com/definitely-stable/Mathlab/pull/214), [#218](https://github.com/definitely-stable/Mathlab/pull/218), [#224](https://github.com/definitely-stable/Mathlab/pull/224). E0 [#225](https://github.com/definitely-stable/Mathlab/pull/225) is logically independent.

**EXACT FINITE W32 ALL-45-ORIGINAL-INCIDENCE-SIX-SET CLASSIFIER FOR NEW LEADING PHYSICAL 6+6 MODES / EXACT CLASS-SPECIFIC FULL GF5 PROVEN R3 FLOORS / INDEPENDENT 10-COLUMN BRUTE FALSIFIER / NO FULL R3 UPPER / NO GENERAL ALL-h FIXED-MAP MULTIPLICITY THEOREM / NO IMPROVED ASET EXPONENT.**

## 1. The essential obstacle: same-label motif multiplicities

The already accepted all-h GF(5) results supply the following necessary lower for EVERY individually fixed pair injection (f_s,g_s):

```text
51^6 * R3(f_s,g_s)
 >= 5643*D6
  + 45600*(U_B_left + U_B_right)
  + 43320*U_CA + 49050*U_CB
  + 51750*U_BB_overlap + 45010*U_BB_disjoint.
```

Here each U counts actual distinct six-original-incidence sets with a qualified leading physical coordinate projection and its corresponding ORIGINAL factor endpoint partition (not a signed-event multiplicity); D6 is the previously accepted coincident alternating simple C6 matching subclass. Family classes are mutually disjoint by the original factor multiplicity partitions. The 10×Fmin coefficients are correct because #224's entire C/A,C/B,B/B restricted signed catalogs have **all ten** global-sign-unordered 3v3 events strictly positive. The other accepted terms are disjoint from these four.

The all-h formula does **not** provide a universal lower unless one independently proves a bound on D6 or the U-terms for ALL allowed deterministic f_s,g_s. It also cannot give any R3 upper because **many** 3v3 events lie outside these classes.

## 2. Finite full-family algorithm (GF2 doily ONLY)

For s=2, W(3,2) has V=15 point vertices and 15 line vertices, each degree Delta=3, and N=45 **distinct original incidence** columns. Both physical pair mappings are bijections onto all 15 unordered physical K6 edges. For six selected incidence columns, a leading positive **six-physical-coordinate** projection on the left is necessarily one of:

- A: six different factor points whose physical K6 pair labels make a 2-factor. There are exactly 70 unlabelled physical 2-factor edge sets, times 3^6 choices of distinct incidence column at each point: **51,030** original six-column sets.
- B: exactly one twice-repeated original factor point. Choose its physical pair in 15 ways, one of three C4 on remaining four physical vertices, two among three incidences for the repeated point, and one of three for each of the remaining four points: **10,935** six-column sets.
- C: exactly three twice-repeated original factor points. Choose one of 15 perfect matchings of six physical vertices and two of three incidences at each of the three points: **405** six-column sets.

**Total: 62,370 distinct candidate six-original-incidence sets**, exhaustive for *left* physical projection touching exactly six symbols and no physical leaf. Each is enumerated EXACTLY ONCE, and checked on the right, whose projection must also have six 2-regular coordinate vertices. Consequently this is an efficient finite alternative to scanning `binom(45,6)=8,145,060` original six-subsets, not a sample. The candidate generator is independent of GF5 coefficients; it cannot falsely classify a physical leaf as a positive GF5 event.

The right and left original factor endpoint partitions determine C/A, C/B, B/B-overlap (the two repeated pairs share exactly one original incidence column), or B/B-disjoint. A six-column set whose same original factor point-line pair would repeat a second time cannot occur because original GQ incidences are unique. Classes A/A and A/B (previous accepted results) are intentionally outside the NEW four-class census; non-leading physical projections with 4 or 5 touched coordinate vertices are also outside its scope.

Per fixed labeling the source computes the **EXACT structural U-counts** in each new class, then the rigorously proven weighted full GF5 lower

```text
R3 >=
 (43320*U_CA + 49050*U_CB
 + 51750*U_BB_overlap + 45010*U_BB_disjoint) / 51^6.
```

For one example set in each nonempty new class, run the independent accepted integer 782-dual-state Fourier oracle on all ten 3v3 partitions. Every one must have positive exact count >= its class global minimum (full 51 nonzero-checksum4 weights; **not** unit-only collision counts).

### 2.1 Exact W32 control census — GitHub-hosted GF5 oracle

The independently hosted report on the complete 45 original W(3,2) incidences yields:

| Fixed map | U(C/A) | U(C/B) | U(B/B overlap) | U(B/B disjoint) | Total NEW original six-sets | Proven NEW-class GF5 R3 lower |
|---|---:|---:|---:|---:|---:|---:|
| Lex | 13 | 1 | 8 | 14 | 36 | 1,656,350 / 51^6 |
| Reverse-line | 1 | 1 | 7 | 6 | 15 | 724,680 / 51^6 |

These are exact **selected-family structural counts** for fixed W32 physical bijections, not Monte Carlo estimates. Both are based on the same explicit original GQ factor edges. The lex count 36 and reverse-line count 15 were observed in the hosted E1-specific SUCCESS run [#38026388632](https://github.com/definitely-stable/Mathlab/actions/runs/38026388632); now pinned as regression values in the independent test. Under the proven positive full-GF5 minimum flow constants for each class,

```text
R3_new(lex) >=
 [43320*13 + 49050*1 + 51750*8 + 45010*14]/51^6
 = 1,656,350 / 51^6;

R3_new(reverse-line) >=
 [43320*1 + 49050*1 + 51750*7 + 45010*6]/51^6
 = 724,680 / 51^6.
```

**Interpretation:** reversing the line coordinate order reduces this narrowly defined necessary floor from lex. It does NOT show a better full 51-pattern R3, nor does a comparison at s=2 show any saving as s=2^h grows. Full Q4 and D6 might change in a different direction, and there are missing full-matching/cherry and subleading six-flow classes. Exact-GF5 Fourier checks on witness six-sets independently confirmed strictly positive signed flow weights for all ten balanced signs in every nonempty class.

## 3. Independent falsification and covariance boundary

The independent tests reproduce the 62,370 left candidates and compare the optimized result against raw combinations of all six columns from multiple **explicitly witness-enriched 10-column subuniverses**. This comparison is a test of coverage restricted to each small subuniverse; it is not a claim that the 10-column distribution is representative.

The tests also verify invariance under a shared arbitrary permutation of six physical coordinates, the one-to-one original incidence map, exact fractions for each signed lower risk, and fail-closed errors on noninjection and on s=4 (GF4). The main finite census separately exercises exact lex and reverse-line controls. A finite W32 result cannot be extrapolated by fitting values to s4 or to s=2^h.

The score `Q4`, the coincident C6 obstruction D6, and the NEW four U counts can be used in a **same-map multiobjective diagnostics** pipeline, but only as lower-risk surrogates. Minimizing these positive motifs alone does not certify either a low total R3 or a strict exponent; full 51-pattern GF5 risk for all four/six events would require a separate complete event sum.

## 4. Next theorem gate — B3.2-E1-B (not silently assumed)

Propose a mathematically checkable disjunction:

A. Exhibit ONE explicit uniform-in-h physical pair map family with all-h direct positive-event count upper R3=O(s^(6-epsilon3)) and independently verified R2=O(s^(26/5-epsilon2)) on THE SAME mapping for fixed epsilon_i>0. This would pass the strict extraction gate.

B. Prove an ALL-label universal `D6 + U_B_left + U_B_right + U_CA + U_CB + U_BB_overlap + U_BB_disjoint = Omega(s^6)` (for every possible deterministic injective map). If true, the present GQ+simple alteration approach cannot satisfy strict R3 for ANY such maps. If false, exhibit an explicit sequence with a strict sub-six risk count on the FULL necessary family; a single W32 finite zero or negative result is insufficient.

C. Failing either, freeze the precise obstruction as open, investigate codegree-sensitive extraction and mathematical transfer of physical pair-label correlations; do not invent a theorem from finite W32 controls.

**No worldwide novelty or ASET improvement is established by this finite computational slice.** All parent issues stay open. Only GitHub-hosted runners permitted. Acceptance demands PR-head exact Research SUCCESS, then postmerge main CI.
