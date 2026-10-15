# HYP-105 / issue #230 — D6-AA4-Y-CYC: all-h mixed-support theorem and exhaustive ORIGINAL W32 106×106 paired-swap matrix

**Scope:** strict research-only follow-up to D6-AA4-X-CYC PR #493, pinned parent ae19078c7271f041fc2c0c9f4f88b3ed29250c6c, parent 4/4 exact-head CI SUCCESS. Original source W(3,s) point-line incidences and globally injected complete physical pair-label maps ONLY. No main edits or root #230 closure.

## 1. Motivation

The exact seven accepted historical positive GF5 classes satisfy S(f,g)=N_nonAA(f,g)+D6(f,g) on the SAME six ORIGINAL incidence IDs under ONE GLOBAL f,g. W-CYC's probability of positive D6 for uniform g when f is fixed does not imply a deterministic lower for arbitrary correlated pairs. X-CYC exhaustively verified that true-original S68/S72 are weak local minima (selected S AND weighted certified positive numerator) among the 210 one-sided original point or line swaps plus unchanged baseline. The missing experiment is simultaneous correlated point AND line swaps.

Original W32 has 15 point source factors, 15 line source factors, 45 genuine distinct incidence IDs and 15 physical K6 edges per typed map. There are exactly 105 transpositions on each side, so 106×106=11,236 globally coherent (f,g) maps including identity and all one-side changes; exactly 105²=11,025 have nontrivial changes to BOTH sides.

This is the complete radius-one two-typed-coordinate box around each anchor, not the full (15!)² permutation space nor an all-h asymptotic family.

## 2. Theorem: universal exact mixed finite-difference support (NO sign assertion)

Fix any genuine ORIGINAL W(3,s), s=2^h>=2, any complete globally injected physical pair maps f,g with minimal a and K=C(a,2)>=(s+1)(s²+1). Exchange images of two DIFFERENT actual original POINT factors to obtain f'; independently exchange images of two different actual original LINE factors to obtain g'. These are full global maps and all source incidences remain unchanged.

For any six distinct ORIGINAL incidence IDs Q and each original accepted seven-GF5 indicator I_t(Q;f,g), write

Delta I_t(Q) = I_t(Q;f',g') - I_t(Q;f',g) - I_t(Q;f,g') + I_t(Q;f,g).

Let P(Q) indicate that Q touches at least one swapped original point factor, and L(Q) likewise at least one swapped original line factor. Then

    Delta I_t(Q) = 0 whenever P(Q)*L(Q) = 0.

PROOF: If P(Q)=0, the left projection is EXACTLY unchanged between f and f'. Therefore the four terms cancel in pairs. If L(Q)=0, right projections remain unchanged and terms likewise cancel. No event independence or GQ automorphism assumption. The proof applies to EVERY original Q and all seven tags for all s=2^h.

Hence for each true-original class multiplicity C_t, the full selected S and the certified 51-palette selected seven-class numerator W=sum_t w_t C_t,

    Delta C_t = sum_{Q subset ORIGINAL I, |Q|=6, P(Q)=L(Q)=1} Delta I_t(Q)
    Delta S = sum_t Delta C_t
    Delta W = sum_t w_t Delta C_t

with exact historical selected integer weights:
D6 5643; B-left/A-right 45600; A-left/B-right 45600; C/A 43320; C/B 49050; B/B-overlap 51750; B/B-disjoint 45010.

The theorem is an **exact all-h identity without positivity, asymptotic, or root minimax conclusion**. It isolates actual ORIGINAL source support that may carry nonadditive correlated two-side effects.

## 3. Independent complete finite enumerator and original seven-class classification

Use independently validated actual W32 fixture (S68 or S72 separately). The new self-contained C++20 engine:
1. Reads all 45 ORIGINAL point-line incidence IDs and two globally bijective source physical K6 pair-label maps; checks original regularity, partial linearity, both physical bijections and canonical K6 coordinate symbols.
2. Generates 106 full global typed maps on each side (identity plus 105 distinct source-factor transpositions).
3. For EACH global map and EACH side, independently reconstructs all 62,370 genuine ORIGINAL six-ID physical degree-two candidates as 51,030 type-A (70 physical six-edge 2-factors * 3^6), 10,935 type-B (45 doubled source patterns * C(3,2) * 3^4) and 405 type-C (15 perfect matchings * C(3,2)^3), using actual ORIGINAL incidence IDs only. No replacement of actual source geometry with synthetic physical 6-paths.
4. Sorts immutable 6-ORIGINAL-incidence-ID keys for all 106 per-side indexes and performs 106×106 exact sorted two-sided set joins. Connected A/A physical six-column duals must agree on the SIX SAME original incidence positions to be historical D6; disjoint two-triangle A/A projections remain rejected. All six other accepted original source forest classes use genuine source-factor incidence multiplicities. Source C/C is impossible by GQ girth eight.
5. Writes exactly 11,236 TSV rows per anchored original complete pair, each containing variant IDs, ALL SEVEN true-original accepted GF5 class multiplicities, unweighted S and selected certified GF5 numerator.

An independent Python verifier reads EVERY TSV row and checks nonnegative counts, S=sum seven classes, 51-palette weighted exact floor, no omissions/duplicate variant pairs. It checks ALL 210 one-side neighbors against the separate prior X-CYC original sparse-support seven-class oracle, with true source GQ point-line duality for point changes. Each selected minimum, all Pareto witnesses, plus predetermined mixed witnesses (1,1), (7,11), (35,78), (105,105), are independently recomputed by both AA4-Q's two-sided actual original six-ID join and the historical original seven GF5 classifier. This independently falsifies any erroneous native physical half enumeration, mixed source position or global map inconsistency.

## 4. Exact nonadditive mixed coupling diagnostics

For every 1<=i,j<=105, compute per accepted original class

    Delta_ij C_t = C_t(i,j) - C_t(i,0) - C_t(0,j) + C_t(0,0).

Then compute exact signed interaction counts and extrema for S and weighted W. Also find:
- minimum selected S among all 11,236;
- minimum selected S among 11,025 strictly simultaneous two-sided swaps;
- best D6=0 constrained global complete pair, and strictly-mixed constrained pair;
- minimum selected historical 51-palette weighted numerator;
- nondominated (D6,N_nonAA) Pareto frontier, with literal globally completable original transposition witnesses.

Any S improvement beyond S68/S72 means ONLY that a pair of correlated single-source transpositions escapes their previously certified one-sided local minima. No infinite counterexample, universal all-h obstruction or complete original W32 global minimum follows. If no pair improves, the finite rectangle still does not prove global optimality.

## 5. Reproduction

Use only Python 3.12, C++20 and GitHub-hosted runners; no external dependencies.

    python -m unittest discover -s research -p "test_hyp105_issue230_d6aa4ycyc_bilateral_original_matrix.py" -v
    g++ -std=c++20 -O3 -Wall -Wextra -pedantic -o /tmp/aa4y-native research/hyp105_issue230_d6aa4ycyc_bilateral_original_join.cpp
    python research/hyp105_issue230_d6aa4ycyc_bilateral_original_matrix.py --scheme S68 --engine /tmp/aa4y-native --matrix /tmp/S68.tsv --summary /tmp/S68.json
    python research/hyp105_issue230_d6aa4ycyc_bilateral_original_matrix.py --scheme S72 --engine /tmp/aa4y-native --matrix /tmp/S72.tsv --summary /tmp/S72.json

Hosted dedicated workflow: .github/workflows/hyp105-issue230-d6aa4ycyc-bilateral-original-11236.yml. Retain raw 11,236-row TSV evidence and signed mixed-interaction/Pareto JSON certificates for each anchor as 90-day hosted artifacts. Numerical results are only accepted when source HEAD and hosted workflow are verified; do not infer outcomes from code.

## 6. Acceptance and formal blocker

This slice establishes an exact all-h signless support identity and independently checked finite actual-original matrix, not a positive all-h deterministic transfer bound. Root #230 Branch A (all pairs S>=c*s^6), Branch B (infinite correlated S=o(s^6) family) and Branch C (model-equivalent quantified restricted theorem) remain OPEN_WITH_FORMAL_BLOCKER. Require exact HEAD Dedicated/INDEX/Proof Audit/Full Research SUCCESS and independent mathematical referee before research Draft integration. Keep main unchanged. Next stage should trace any negative nonadditive interaction to true source forest cells and connected AA positional duals, then formulate a falsifiable all-h charge-transfer inequality; alternatively test higher-radius global permutations if no paired swap improves.


## 7. Verified genuine-original finite results: first exact grid CI

Initial full-grid GitHub-hosted dedicated run: https://github.com/definitely-stable/Mathlab/actions/runs/38705972846 ; three out of three jobs SUCCESS. Independent actual ORIGINAL tests, S68 11,236 configurations and S72 11,236 configurations independently PASS with native half-index plus historical class census for all nominated minima and fixed mixed probes. The numerical table below was read directly from hosted logs, not extrapolated from source or earlier PRs.

| Genuine ORIGINAL finite field | S68 | S72 |
|---|---:|---:|
| Baseline S | 68 | 72 |
| Baseline D6 | 0 | 0 |
| Complete global point-line pairs checked | 11,236 | 11,236 |
| Strictly simultaneous point+line swaps checked | 11,025 | 11,025 |
| Minimum S over all 11,236 | **68 (unchanged baseline)** | **72 (unchanged baseline)** |
| Minimum S among strictly simultaneous pairs | 70 | 74 |
| Representative best strictly-mixed source POINT swap | (3,8) | (1,14) |
| Representative best strictly-mixed source LINE swap | (0,14) | (4,10) |
| D6 for representative strictly-mixed winner | 0 | 0 |
| Number of all 11,236 pairs with D6=0 | 6,014 | 4,562 |
| Minimum selected historical 51-palette weighted numerator | **3,112,510 (unchanged baseline)** | **3,283,610 (unchanged baseline)** |
| Number of mixed pairs with negative exact Delta S | **8,286 / 11,025** | **8,642 / 11,025** |
| Nondominated objective (D6,N_nonAA) frontier | {(0,68)} | {(0,72)} |

**Finite proposition (exhaustive matrix, independently falsified):** The original S68 and S72 globally coherent complete W32 maps are *weak local minima* of selected S and selected historical weighted GF5 numerator over the entire 106×106 box of source-factor physical label permutations obtained by at most one transposition on EACH typed side, including all simultaneous point+line changes. In both cases their original objective pair is the unique nondominated (D6,N_nonAA) value over this finite box.

**First separate nonadditivity observation:** Thousands of true-original mixed pairs have Delta S < 0 even though NO complete paired map in this box has S below its anchor. Thus the stronger candidate claim that mixed finite differences are always nonnegative is false already on the genuine ORIGINAL W(3,2) 51-palette seven-class model. Negative interactions DO NOT imply an improvement below the baseline; one-sided costs can offset them. This is a finite all-seven same-Q fact, not a random expectation or independent projection effect.

The enhanced independent falsifier (following this initial dedicated run) explicitly verifies all FOUR historical same-global-map corners for the most negative and most positive native mixed finite-difference witnesses, and records the literal swapped source IDs and exact four S corner counts in both JSON and hosted job logs. Final exact-head CI acceptance must be checked on the last code/documentation revision. Do not confuse a previous green run with green checks on a newer HEAD.

### Consequence and next possible Y2 scope

The naive optimization approach of testing all single source-label swaps AND all pairs of simultaneous one-point-transposition plus one-line-transposition is now exhausted for BOTH pinned anchors, with no improvement. The candidate universal sign claim Delta S>=0 is simultaneously falsified by genuine original finite negative Hessians. The remaining mathematical gap is to quantitatively bound the *negative* mixed coupling relative to the one-sided penalties under SOURCE forest and physical-column cyclic constraints, or to look beyond the radius-one-per-side neighborhood (multi-step permutation cycles and changes to the initial f,g).

Neither the observed local minima nor the observed negative interactions proves the root all-h minimax bound S>=c*s^6 or an infinite adversarial o(s^6) family.
