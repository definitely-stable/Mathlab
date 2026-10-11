# HYP-105 B3.2-E1-C24-B5 — Exact second transposition sphere and right-template pullback

2026-10-11. Scientific child [C24-B4 #348](https://github.com/definitely-stable/Mathlab/pull/348) → [C24-B3 #347](https://github.com/definitely-stable/Mathlab/pull/347). Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). **Stacked PR only; no main modifications.**

## Research question and scope

C24-B4 established a *strict* true original W(3,2) single-RIGHT-transposition local minimum S_seven=72 with ONE unchanged complete original LEFT map f and the ONE complete original RIGHT pair-label permutation

    g72 = (12,9,11,2,8,6,0,13,5,14,3,7,4,10,1).

Its seven-vector is (0,36,31,2,0,1,2), necessary GF5 numerator Q7=3,283,610, right-C=0, all 105 one-transposition neighbors have S>=74.

**C24-B5 checks exactly every original global-right permutation at transposition Cayley distance two from g72.** Does a strictly improving double swap exist even though all first swaps increase S? If not, g72 is radius-2 locally stable for this particular f, still not globally minimal. If yes, record a complete two-move path and its transient barrier without claiming a universal all-h result.

## 1. Exact distance-two classification, all n

For any permutation g on n *named original right objects*, composition of two **distinct** original transpositions yields one of only two cycle types:

- Two directed 3-cycles on three chosen original lines: 2*C(n,3). Every resulting permutation admits exactly three ordered two-transposition factorizations.
- Two disjoint 2-cycles on four chosen original lines: 3*C(n,4). Every resulting permutation admits exactly two ordered factorizations, because disjoint transpositions commute.

These are disjoint, exhaust all distance-exactly-two maps and exclude identity (repeating the same transposition).

For n=15:

    2*C(15,3) = 910;
    3*C(15,4) = 4095;
    |sphere_2| = 5005;
    ordered distinct length-two paths = C(15,2)*(C(15,2)-1)
                                     = 105*104 = 10920
                                     = 910*3 + 4095*2.

The inclusive radius-two ball has exactly 1+105+5005=5111 maps, out of 15! possible right permutations **for this f**. Distinct-state quotienting is mandatory; 10,920 ordered paths are NOT 10,920 distinct endpoint maps. A unit oracle exhausts the analogous S4 quotient independently.

## 2. Exact physical-template pullback for a shared global right map

Let J range over **distinct ORIGINAL GQ six-incidence sets**, with its fixed *static* left-f and original endpoint tag t and integer weight. Write \rho(J) for its unordered original-right **multiset** (six line IDs, with multiplicities). A globally complete original-right injection g maps every original right line to ONE distinct physical pair-label; let \mathcal T_R be the physical right 2-factor multisets of size six supported by the occupied physical alphabet.

Each J whose right physical projection passes the six-coordinate degree-two test belongs to **exactly one** fiber g^{-1}(T), T in \mathcal T_R. Consequently the full exact count in every non-D6 tag equals a sum of the original, static source-fiber multiplicities evaluated at just those inverse multisets, with no duplicated or independently remapped J. For D6 the right physical projection must additionally have the *same ordered column-dual* as the already fixed original left projection; check that condition for each D6 candidate in the inverse fiber.

This identity is valid for **all s=2^h** and arbitrary legal occupied physical pair alphabets, but the size of \mathcal T_R and worst-case source D6 fibers may grow. **No asymptotically fast algorithm is asserted**. For the genuine finite original W(3,2), a=6 and the exact number of right six-edge multigraph 2-factor templates is only **130**. Compile source fibers once and compute each globally coherent right score by pulling back exactly those 130 templates, rather than rescanning ~51,506 compressed left-source signatures or recomputing 62,370 right-first source sixsets per map.

The separate exact right-first original 62,370-incidence-set enumerator and the full independent original left-first scorer validate the optimized oracle on the initial and decisive endpoint states. Checks also preserve the accepted original right-C projection, seven static tags and the frozen weighted GF5 **NECESSARY** numerator Q7, not whole GF5 R3.

## 3. Exact disjoint-swap curvature and escape barrier

For two **disjoint** original right transpositions A,B (therefore commuting), define the exact discrete mixed derivative

    kappa_AB(g) = S(g^(AB)) - S(g^A) - S(g^B) + S(g).

Writing d_A=S(g^A)-S(g), d_B=S(g^B)-S(g), the complete double swap improves g **if and only if**

    kappa_AB(g) < -(d_A + d_B).

This is an exact algebraic obstruction. Further, for any particular original six-incidence J whose original-right support misses the original line pair A or misses pair B, its individual mixed derivative vanishes. Thus only *joint-touch* source sixsets contribute to kappa_AB. Proving a universal lower bound would require a uniform bound on these correlated joint fibers, not merely the singleton gradient cuts of C24-B4.

For overlapping transpositions the final result is a 3-cycle; the ordered operations generally do **not** commute and the symmetric disjoint-pair Hessian definition is inapplicable. Enumerate the three ordered factorizations for each directed 3-cycle instead.

The path barrier for a candidate path (A,B) is `max(S(g), S(g^A), S(g^(AB))) - S(g)`. The code selects the lowest barrier among all ordered decompositions of the **minimum-scoring** exact distance-two endpoint and reports its intermediate S. It does NOT claim that this is the minimum barrier among all possible improving endpoints (if any), nor that two steps reach a global minimum.

## 4. Hosted original W32 outcome — exact strict two-swap escape 72 -> 68

The initial exact C24-B5 [GitHub-hosted Contract run #38128554258](https://github.com/definitely-stable/Mathlab/actions/runs/38128554258) completed **SUCCESS** on PR-head ac82828113c54965c4e7613a7fc5c61d593234c0, including all six fast tests and the full 5005-endpoint report with independent full original RIGHT-FIRST 62,370-sixset recount. The numerical result is **not** a guessed sample or a fit.

- Baseline S=72: all 105 single global-original-right swaps have S>=74.
- Complete 10,920 ordered distinct two-swap paths cover exactly 5,005 different endpoint right maps with multiplicities 3 (910 3-cycles) / 2 (4,095 disjoint transposition pairs).
- **Exact minimum among all 5,005 distance-two right maps = 68**. Exactly **TWO** distinct endpoints improve S=72; the next smallest score after the tied 68 endpoints is 73.
- The lex-first minimum right map (physical lex K6 pair indices by the 15 ORIGINAL right GQ lines) is **(12,9,11,4,1,6,0,13,5,14,3,7,2,10,8)**. Its complete accepted seven-vector in frozen tag order is **(0,44,21,0,0,2,1)**, accepted original-right-C=0, and necessary GF5 Q7 numerator **3,112,510**.
- Best two-step factorization of that map minimizes the temporary score barrier: **(4,14) -> S=82**, then **(3,12) -> S=68**. Since the swaps are disjoint, the opposite order is also valid but has first-score S=89 (the pinned first-gradient values are +10 and +17). Thus best transient barrier above the local minimum is **+10**.
- Mixed derivative for these two commuting original swaps is **kappa=-31**, so the endpoint identity is `S(gAB)=72+10+17-31=68`. Since both first step deltas are positive, the negative mixed interaction is exactly what breaks the one-swap trap.
- The optimized pullback census had 14,693 original-right multiset fibers holding 53,907 eligible original sixsets, obtained from **62,370 distinct ORIGINAL left-incidence sources** and **130** physical K6 right multigraph 2-factor templates. The full original LEFT scorer plus an independently implemented full original RIGHT-FIRST 62,370-sixset enumerator confirmed the decisive endpoint.

**Strict finite separation:** This original globally coherent f,g witness proves that **one-global-right-transposition stationarity does NOT imply two-transposition stationarity** for the accepted seven-class score even on a true GQ W(3,2). It is a counterexample to such a *restricted local-optimality implication*, **not** Branch B (which requires an infinite asymptotically small-S family). It does not establish the minimum over all 15! right permutations or any all-f/all-h lower bound.

The first C24-B5 Contract SUCCESS applied to an earlier PR HEAD. Later freeze/metadata commits must pass their own **exact final HEAD Contract/Research/INDEX SUCCESS** before acceptance. The parent issue #230 remains OPEN_WITH_FORMAL_BLOCKER.

## 5. Exact finite acceptance and no-go firewall

The dedicated C24-B5 Contract and a dedicated Research script must fully enumerate the 5005 distinct endpoint maps and verify:

1. All 10,920 ordered two-swap paths, exactly 910 three-cycle endpoints (multiplicity 3) and 4095 disjoint-double endpoints (multiplicity 2).
2. Exact S, full seven-vector, right-C and necessary GF5 Q7 by 130-template source pullback for every endpoint.
3. Direct independent original LEFT source recount of baseline, selected class representatives, final minimum and maximum; separate **RIGHT-FIRST original 62,370 sixset recount** of the exact best endpoint (and baseline if requested).
4. An actual improved map, if found, must have S<72. If the minimum exact distance-two S>=72, report radius-two stationarity for this ONE original W32 f, and nothing more.
5. Fast tests cover the original 130-template right-pullback oracle and S4 sphere group-count identities, but do not rerun 5005 endpoint enumeration in broad `test_*.py` discovery. Dedicated hosted heavy step is explicit.
6. The six-shard full hosted Research remains lossless and seventh aggregate fail-closed; preserve predecessor 135 named commands and append two B5 named commands (137 total with newly frozen independent FNV1a64). Require exact-head C24-B5 Contract/Research/INDEX SUCCESS. Do not claim earlier HEAD successes for new commits.

**Research outcome:** EXACT_ALL-n_DISTANCE_TWO_CYCLE_CLASSIFICATION + ALL-h_EXACT_OCCUPIED_RIGHT_TEMPLATE_FIBER_IDENTITY + FINITE_ORIGINAL_W32_FULL_5005_SPHERE_EXHAUSTION. **NOT PROVED_A, NOT COUNTEREXAMPLE_B, NOT GLOBAL_RIGHT_15_FACTORIAL, NOT UNIVERSAL_GF5_R3/ASET.** Issue #230 stays OPEN_WITH_FORMAL_BLOCKER.

