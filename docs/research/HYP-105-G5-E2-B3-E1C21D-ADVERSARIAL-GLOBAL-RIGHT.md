# HYP-105 C21-D — genuine global W(3,2) right-label obstruction to D6-only worst-case transfer

Date: 2026-10-11. Parent [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Depends on [C21 #317](https://github.com/definitely-stable/Mathlab/pull/317) and scientific C20 [#315](https://github.com/definitely-stable/Mathlab/pull/315) / CI [#316](https://github.com/definitely-stable/Mathlab/pull/316). **RESTRICTED EXACT FINITE W32 D6-ONLY NO-GO**, not an infinite all-h low-S family.

## Complete original point and right line maps

Use the genuine symplectic W(3,2) incidence graph: 15 original points, 15 original lines, 45 original distinct incidences. PAIRS is the lexicographic 15-edge unordered physical K6 palette. Choose one complete global point-to-pair map f(p)=PAIRS[p]. On the right, use exactly ONE complete global original line-to-pair bijection g(line)=PAIRS[perm[line]] where

    perm = (4,13,2,9,14,3,6,0,8,1,11,5,7,12,10).

Every occurrence of an original right line has the SAME physical right label. No independent per-motif or per-source-block assignments.

**Two independent exact oracles on the SAME f,g:**
1. Direct enumerate all 60 physical LEFT C6 and all 3^6 true original incidence lifts for each (43,740 left C6 source sixsets), with exactly 18,716 containing six distinct ORIGINAL right lines. Compare left/right column-position cycle duals using independently computed pairwise physical edge intersections; strict D6 accepted **ZERO**.
2. Historical complete seven_census independently enumerates 62,370 original left 2factor incidence sixsets and returns the disjoint seven-family original multiplicities:

    D6=0; B-left/A-right=60; A-left/B-right=66; C/A=5;
    C/B=0; B/B-overlap=9; B/B-disjoint=6; S_seven=146.
    accepted GF5 seven necessary numerator=6,698,010.

A third oracle using original weighted B-left/right-distinct six-uniform source and the physical K6 two-factor target independently obtains B-left/A-right=60, matching the seven-family census.

For comparison, the SAME original left f with complete identity right global g(line)=PAIRS[line] gives D6=15, B-left/A-right=98 and S_seven=259. Both assignments are actual global bijections of all 15 original GQ lines.

## Exact restricted theorem and mathematical scope

For the fixed true original left f at s=2 above, nonnegativity implies D6(f,g)>=0 for every legal global g. Since the explicitly certified global permutation attains 0,

    min_{g a complete original-right bijection} D6(f,g) = 0.

Consequently also min_{f,g} D6(f,g)=0 at **s=2 only**. The exact one-common-random-right D6 mean at this SAME f is positive:

    E_g D6(f,g) = 18716/5005 > 0.

This is a concrete original-GQ counterexample to *inferring a positive fixed-g D6 minimum from a positive global-g mean at s=2*. It is NOT a counterexample to an asymptotic all-h D6 Omega(s^6) minimum: no infinite family is provided. In particular the same pair of true maps has S_seven=146 > 0, so this is NOT a counterexample to the seven-family obstruction of parent #230, full GF5 R3, or ASET exponent.

## Exact all-h D6 incidence tensor requiring a new extremal inequality

For any s=2^h and one fixed global left f, define J_C6,A(f) as all DISTINCT ORIGINAL six-incidence sets whose physical left projection is a simple six-cycle and whose six ORIGINAL right lines are distinct. Order the six original incidence columns consistently. Let D_L(J) be the connected six-cycle of column-position adjacencies induced by the physical left pairs, and D_R(J,g) the right column-position dual after ONE global right g. Then

    D6(f,g) = sum_{J in J_C6,A(f)} 1[D_R(J,g)=D_L(J)].

C21 averages this exact objective over ONE globally shared right permutation g. Its minimum is different. The explicit W32 witness shows the D6 objective can vanish even when the same-f mean is positive. This exact identity alone is NOT model-equivalent to the FULL seven-family issue #230 Branch C.

Future research must bound the full seven-class sum at a worst globally correlated f,g or present a rigorous infinite original GQ small-S family. C21-D does neither. Do not import finite W32 minima as all-h exponents.

## Exact evidence and acceptance

Scientific source: research/hyp105_g5e2b3e1c21d_adversarial_right.py
Tests: research/test_hyp105_g5e2b3e1c21d_adversarial_right.py
Hosted contract: .github/workflows/hyp105-c21d-contract.yml

Tests verify true 45-incidence geometry, both complete global injections, no duplicates, all 43,740 physical C6 lifts, 18,716 distinct-original-right subset, exact dual equality vs full seven census, independent original B-left overlap, necessary GF5 numerator, and identity-right comparison. Invalid permutations and incomplete source caps fail closed. Full Research retains prior 119 checks and appends two C21-D test/report checks (121 total), six GitHub-hosted shards plus fail-closed aggregate. No self-hosted runners. Exact HEAD dedicated+Research+INDEX required before any merge.

**Issue #230 stays OPEN_WITH_FORMAL_BLOCKER. Next C22:** joint original seven-class f,g tensor, cross-class adversarial tradeoffs, and structural inequalities beyond independent local C18/C19 or low-pin C9/C10 relaxations.
