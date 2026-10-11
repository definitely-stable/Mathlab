# HYP-105 C24-B2 — genuine W(3,2) one-f / one-g full seven-family audit and right-C surrogate NO-GO

Date: 2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Based on accepted exact-head C24-B1 [PR #344](https://github.com/definitely-stable/Mathlab/pull/344) -> C24-A1 #340 -> C23 #334. This is a **FINITE, exact genuine original W(3,2) adversarial certificate**, not a new all-h positive lower or an infinite small-S witness. Work only on the scientific stacked branch; no main changes.

## 1. Why C24-B1 does not solve the root objective

C24-A1/B1 proved deterministic star-collision bounds and the exact third-order correction for ORIGINAL RIGHT endpoint multiplicity profile C=(2,2,2). They constructed a single global LEFT f with H_C=45 and a single complete global RIGHT g such that S_(R=C)(f,g)=0.

But S_seven contains seven mutually disjoint accepted B0 classes. The **symmetric class name** C/A also includes ORIGINAL LEFT C/ORIGINAL RIGHT A sources, not just right-C. Thus S_(R=C)=0 does not imply that the C/A or C/B class labels are both zero, and certainly does not imply S_seven=0. A proposed equality S_(R=C)=count(C/A)+count(C/B) is FALSE. The new code tracks the ORIGINAL right-line multiplicity independently of the symmetric seven class tag.

## 2. Freeze one genuine original W32 complete two-sided mapping

Use exactly the C24-B1 original GQ generation: nonzero GF(2)^4 vectors p=1..15, 15 sorted isotropic original three-point lines, and all 45 distinct ORIGINAL incidences. Lex K6 physical unordered pairs are indexed 0..14. The fixed **one complete global ORIGINAL LEFT** point map is

    f(p)=K6_PAIRS[f_perm[p-1]]
    f_perm=(13,4,2,14,0,11,1,7,10,6,9,5,12,3,8).

The **one complete global ORIGINAL RIGHT** line map is

    g(line_i)=K6_PAIRS[g_perm[i]]
    g_perm=(12,10,5,2,8,14,1,7,0,6,3,13,9,4,11).

Different original six-incidence sets MUST share these same global f,g and all repeated ORIGINAL endpoints map to the same physical pair. No local sixset-specific optimisation or fabricated independent right maps.

Two independent full finite methods count all 62,370 actual ORIGINAL six-incidence sets:
1. **LEFT-FIRST**: all 130 K6 six-edge physical 2factor multisets, then select different actual ORIGINAL right GQ incidence IDs per ORIGINAL left point. Freeze true original static endpoint multiplicity and strict D6 connected column-dual compatibility, compress only identical signatures with positive integer original-sixset multiplicities.
2. **RIGHT-FIRST**: all 130 physical RIGHT six-edge 2factor multisets, then select different actual ORIGINAL left GQ incidence IDs per ORIGINAL right line. Directly classify both physical halves with a separately implemented integer-degree / coordinate-to-position dual graph, not the first method's parity bitmask nor static schema. Each source orientation enumerates exactly 62,370 distinct real sixsets and yields identical complete seven-vectors.

For this SAME complete f,g, exactly

    D6                1
    B-left/A-right   80
    A-left/B-right   83
    C/A               4
    C/B               0
    B/B-overlap       2
    B/B-disjoint      7
    --------------------
    S_seven         177
    Q7 necessary GF5 numerator 8,030,293
    S_(ORIGINAL RIGHT=C) 0

The C/A=4 surviving cases here involve ORIGINAL LEFT C and ORIGINAL RIGHT A; therefore the right-C original-source count is zero with C/A nonzero. The B0 frozen GF5 lower weights are (5643,45600,45600,43320,49050,51750,45010), NOT exact full R3.

## 3. Exhaust all 105 one-global-right-line transpositions: a concrete joint-vs-surrogate conflict

Compile once the genuine full original LEFT 62,370 sixsets and retain 53,907 statically eligible original sixsets compressed into 51,506 original right-ID signatures. Freeze the above global g and swap the physical pair assignments of exactly two different ORIGINAL right GQ lines. Recompute ONLY original source records touching either swapped line; the untouched records cannot change their physical RIGHT classification. This exact locality follows the C22 all-h identity; it is not an assumption that motif successes are independent.

Compare all 105 complete globally coherent one-swap right maps on the SAME fixed left f, including every one of the seven accepted class counts, total S, Q7, and accepted **ORIGINAL RIGHT C** contribution.

| Criterion within exactly 105 complete right maps | Best full seven S | Best seven S conditioned on original right-C accepted=0 |
|---|---:|---:|
| Swapped original right-line indices | (6,14) | (10,14) |
| D6 | 1 | 1 |
| B-left/A-right | 64 | 74 |
| A-left/B-right | 52 | 51 |
| C/A | 4 | 2 |
| C/B | 0 | 0 |
| B/B-overlap | 2 | 3 |
| B/B-disjoint | 6 | 5 |
| Full S_seven | **129** | **136** |
| Accepted original right-C | **1** | **0** |
| Q7 necessary GF5 numerator | **5,842,083** | **6,172,583** |

Exactly 58/105 one-swap maps have zero accepted original right-C, 35 have one, 8 have two, 3 have three and 1 has four. All 105 original mappings are COMPLETE. The fixed baseline itself has right-C zero, total S=177 and is NOT included among the 105 one-swap neighbours.

**FINITE RESTRICTED NO-GO:** On this fixed genuine GQ host and fixed global f, demanding S_(R=C)=0 loses to the actual minimum full seven count over the checked 105-neighborhood (136 versus 129). Therefore a C-only zero/minimum objective is NOT a lossless surrogate for the full seven objective even locally. This is not a contradiction of a possible all-h universal lower, and does NOT show the global min over all 15! right maps or all f.

Independent RIGHT-FIRST full 62,370 original-incidence recounts separately verify the baseline, the global minimum S witness (6,14), the minimum conditional C=0 witness (10,14), and an additional (0,1) swap. The B0 GF5 weights and exact original sixset identities are frozen regression gates.

## 4. Mathematical decision for C24-B3

C24-B2 closes a **finite falsification** of C-only full-seven optimisation. The productive next proof target is an ALL-h joint seven-family *extremal certificate* that keeps ORIGINAL f,g globally shared; it may use conditional overlap types, the exact third-order tensor and cross-class tradeoff, or an explicit hypergraph rank/cycle inequality. Formulating such a certificate must first survive the actual global W32 witnesses C21-D, C22, C24-A1, C24-B1 and the 105-map C24-B2 envelope. Do NOT infer a universal minimum from 105 local maps, positive random means, or a D6 or right-C-only lower.

Status: **FINITE_RESTRICTED_NO_GO_C_ONLY_SURROGATE / OPEN_WITH_FORMAL_BLOCKER** for [#230](https://github.com/definitely-stable/Mathlab/issues/230). No PROVED_A, COUNTEREXAMPLE_B infinite sequence, full GF5 R3, or ASET exponent.

CI: C24-B2 dedicated Contract, full six GitHub-hosted Research shards and fail-closed seventh aggregate, plus INDEX, all at exact HEAD. Research preserves all 129 C24-B1 commands and adds exactly two C24-B2 scripts; preserve frozen hash. No self-hosted runners.
