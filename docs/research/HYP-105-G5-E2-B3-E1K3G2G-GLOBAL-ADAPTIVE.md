# HYP-105 E1-K3-G2-G — adaptive complete-Jcross finite Hall and quantitative TRUE-S lower certificates

Date 2026-10-12. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked Draft child of fully hosted green [PR #379](https://github.com/definitely-stable/Mathlab/pull/379), exact parent `71434182bbce2aae0921b79a8e4f0bdfe74278a8`. Main unchanged, no merge.

**Scientific status: FINITE, exact positive witnesses; all-h universal Branch A/B OPEN.** The purpose is to test whether the actual entire finite W34 Jcross can be charged into actual accepted S motives with unit capacity, using shared target caching and an adaptively repaired matching. Every result is strict positive lower evidence even with truncated search; no truncated unmatched witness proves negative.

## 1. Main scientific gap following G2-F

K3-G2-E constructed exact injections from all W32 Jcross witnesses into all seven accepted positive GF5 target families, for three specific coherent global maps. K3-G2-F crossed to real W34 and produced unit-capacity injections for eight heavy witnesses in each of two maps, but only *8 of 128* lex and *8 of 75* random Jcross witnesses were selected. No all-witness or all-h theorem existed.

The universal theorem that would be useful has TWO independent proof obligations:
```
(1) Every Jcross source witness can be charged to a TRUE accepted
    seven-family six-incidence target with maximum target load <=K.
    Then Jcross <= K*S_s.
(2) A genuinely ACCEPTED-S quantitative alternative
    S_s >= alpha*s^6 - beta*Jcross, with alpha>0 and universal constants.
```
Together they imply `S_s>=alpha*s^6/(1+beta*K)`. Neither (1) nor (2) is proven for all h by finite Hall experiments. Importantly, K2's P3/Theta lower directly controls all C6 before subtracting improper C6, while the K3 full-R3 theorem controls ALL distinct-column positive GF5 motifs; it does **not** automatically prove (2) for the restricted seven accepted families. This implication must not be smuggled into the claim.

## 2. Adaptive indexed search on genuine original W(3,s)

Given ONE coherent global f,g of a true W(3,s) geometry, enumerate each individual Jcross improper Kikuchi six-cycle using actual physical edges and ORIGINAL (point,line) column provenance. Every such source uses exactly FIVE different ORIGINAL incidence columns. On a requested full run, include all Jcross witnesses in a deterministic heavy-class-first list; on a sampled run retain an explicit sample_limit in the report.

For each source, sort its TEN possible pairs of original source columns by their physical support relevance as in K3-G2-F. Complete the first pair into actual accepted six-column S motifs via the previous source-pair seeded DFS with necessary physical degree/source multiplicity pruning. **Cache** identical two-column seeds among witnesses. Store every genuinely accepted six-incidence target ONCE in one GLOBAL positive index. Each stored target must have strict accepted GF5 family per-template positivity with class-specific integer floor `R3_CERTIFIED_FLOORS`.

Construct the bipartite graph relating ALL considered source witnesses to EVERY discovered target having **at least two source original incidence columns in common**. Check exact maximum matching with the independently audited maxflow/mincut and also independently construct one injective matching using augmenting paths; validate every actual assigned edge and verify GF5 target family.

If some source witness is unmatched, search its next untried seed pair, reuse cached results where possible, add new actual positive targets and recompute the GLOBAL matching. Continue until all considered sources are matched or the specified seed-work/target budget is exhausted. A complete matching for all sources proves a *finite* `Jcross<=S` for that particular global map. A partial failure with truncated search is explicitly marked INCONCLUSIVE, not a counterexample.

Every seed pair actually explored has an explicit work/target cap; the algorithm never claims full enumeration of its neighborhood under truncation. Different physical target classes all count as one positive accepted six-original-column motif each, not as many targets as GF5 signed events.

## 3. Two exact positive lower certificates, even when search is truncated

For the deduplicated set `T` of actually constructed accepted original six-incidence sets, always:
```
S_s(f,g) >= |T|,
51^6 R3(f,g) >= sum_{C in seven families} n_C * w_C,
  n_C=# discovered DISTINCT ORIGINAL source sixsets of class C,
  w_C=previously certified 51-palette GF5 numerator lower per such sixset.
```
The second inequality is for the actual FULL six-column GF5 R3 risk (which sums all events, including the accepted ones), and is unconditional for that one map. It is not a complete evaluation of R3. The first counts the accepted seven-family source S, not repeated Kikuchi witnesses.

When complete source injection is obtained on a finite map, additionally `Jcross<=S_s` as an exact finite inequality. Neither establishes `S_s=Omega(s^6)` over all s. A universal S lower needs independent all-h analytic proof (2) even if a universal bound (1) is obtained.

## 4. Independent acceptance checks

- Revalidate full-W32 original source charge for lex/reverse; compare EVERY discovered genuine accepted sixset against independent exhaustive B0 `seven_census(witness_sets=True)`, including exact counted GF5 class floor and `S_seven` upper.
- Exercise independent selected-W34 actual source Hall for both lex/random and assert each discovered target is an actual globally labelled original accepted sixset.
- Independent finite W32 full-R3 risk floor consistency: discovered subfamily weighted numerator must not exceed the already accepted B0 weighted numerator over ALL genuine accepted sixsets.
- Enforce unique global target IDs, exact source-target physical original-column overlap, matching uniqueness, work and cached pair budgets.
- Explicit zero-node and ill-typed budget tests ensure a negative conclusion cannot be inferred from missing unenumerated targets.
- One path-limited dedicated GitHub-hosted contract with 4 independent test methods; inherited full Research and INDEX, no redundant full suites.

## 5. Next K3-G2-H proof gate

If the G2-G global W34 charge test succeeds, inspect the actual source-to-target assignments across classes and find a **uniform**, independent-of-s multiplicity bound or a symbolic source completion from global GQ incidence. If it fails due to budget, optimize anchored positive two-factor joins, but NEVER label such partial failure a counterexample. Separately derive (or rigorously refute) the S-restricted complementary inequality of point 1, rather than importing a full R3 theorem as an accepted-S theorem. Keep original Branch A/B and ASET exponent OPEN.


## 2026-10-12 exact all-witness W(3,4) charging theorem for two specific legal maps

After the original full-W34 experiment [Contract #38214269288](https://github.com/definitely-stable/Mathlab/actions/runs/38214269288) gave partial genuine-S injections (127/128 lex, 70/75 random) with 12,000 candidate nodes and at most 4 original source-pair seeds per unmatched witness, an enlarged **finite** proof search tested up to all 10 original source-column pairs for each remaining unmatched witness, with 30,000 candidate nodes per distinct seed and a fixed per-seed accepted-target cap of 12.

The independent GitHub-hosted [Contract #38214367141](https://github.com/definitely-stable/Mathlab/actions/runs/38214367141) PASSED and produced exact complete source-to-positive-S injections:

| Quantitative exact certificate | W(3,2) lex control | W(3,4) lex | W(3,4) random seed 20261012 |
|---|---:|---:|---:|
| ALL individual Jcross witnesses enumerated | 36 | **128** | **75** |
| Genuine distinct accepted S targets discovered | 150 | **374** | **203** |
| First-pass exact matching (capacity 1) | 36 | 126 | 73 |
| Final exact matching (capacity 1) | **36/36** | **128/128** | **75/75** |
| Additional adaptive rounds | 0 | 1 | 5 |
| Distinct original-pair seed completions used | 28 | 127 | 79 |
| Candidate nodes checked | 102,381 | 3,810,000 | 2,370,000 |
| Proven `S_s(f,g) >= discovered genuine targets` | >=150 | **>=374** | **>=203** |
| Proven `51^6 R3(f,g) >= discovered GF5 family floors` | >=6,359,976 | **>=16,504,153** | **>=8,814,887** |
| Complete Jcross=>true-S injective charging (THIS map) | YES | **YES** | **YES** |

For W34 lex, the 374 discovered distinct accepted original six-incidence sets split by family:
```
A-left/B-right 132; B-left/A-right 101; B/B-disjoint 58;
B/B-overlap 7; C/A 60; C/B 5; D6 11.
```
For W34 random:
```
A-left/B-right 84; B-left/A-right 36; B/B-disjoint 26;
B/B-overlap 3; C/A 42; C/B 3; D6 9.
```

The source witnesses include BOTH original point-origin and line-origin cross-source repeated-column sixcycles. They are not just heavy-class samples. For each actual original source witness, an entirely constructed six-distinct-incidence accepted-S target is assigned, with at least TWO original source columns in common, and no target is assigned twice. The exact max-flow/min-cut and independent augmenting-path assignments agree; the deterministic original-incidence target assignment SHA256 hashes are sealed in the hosted regression test.

This rigorously proves the **finite model-specific inequalities**
```
W34 lex legal global f,g:    128=Jcross <= S_4(f,g), and S_4(f,g)>=374.
W34 random legal global f,g:  75=Jcross <= S_4(f,g), and S_4(f,g)>=203.
```
The positive GF5 lower numerator is obtained by summing individually certified per-family floor weights over distinct actual ORIGINAL target sixsets. This is a lower bound on the FULL GF5 six-column R3 numerator for this map; the actual R3 can be larger.

**Strict limitations:** Most seed-pair searches are still target-budget or node-budget limited; no complete enumeration of ALL possible accepted S sixsets is asserted. However, an actual full matching is an existential witness, so incompleteness of the target census does not invalidate the full Jcross injection. These results concern ONLY these two coherent W34 labelings. They are NOT a universal all-h theorem, do NOT give S_s=Omega(s^6), do NOT provide an analytic dichotomy when Jcross is small, and do NOT resolve issue #230 Branch A/B or ASET exponent.

**Next mathematical gate:** Separate the syntactic two-original-column Hall relation from a PROVABLE GQ-based all-h charging construction with uniform capacity K. Even then, derive a distinct S-family restricted all-h complementary lower bound `S_s>=alpha*s^6-beta*Jcross` (not merely the earlier complete-R3 sixcycle inequality). Without BOTH, the original Omega(s^6) universal obstacle remains OPEN.
