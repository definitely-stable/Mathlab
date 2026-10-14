# HYP-105 #230 — JPKC-014: choice-star and ORIGINAL incidence capacity transfer

**2026-10-14.** Strict research-only child of JPKC-013 PR #445, parent HEAD `c0d6401ad786b3da05c666b3b50c60fb82c24339`. Only `research/hyp105-issue230-jpkc014-source-factor-capacity`; main unchanged. No merge. Root A/B OPEN.

## 1. Explicit failure of the naive profile method

JPKC-012 / JPKC-013 found two complete true W32 four-ORIGINAL-right-line factor fibers of 24 legal global right pair injections. On S72 `min_g S(g)=68`, but `sum_m min_g S_m(g)=0`. JPKC-013 proves an **exact minimum cardinality 4 profile cover** and discovers four positive original right-line multisets with distinct images of one original source line 7 (each image leaves exactly six other legal permutations). Merely growing proper physical P3 or independent profile minima cannot explain the full seven-positive sixset lower bound.

This slice asks how to **transfer** factor-choice certificates into nonovercounted S bounds. The answer is conditional and all-h valid, with a stronger no-loss form when witnesses are original-block-one-line local.

## 2. J47 — source-factor image choice-star, all h CONDITIONAL

Let W(3,s), s=2^h, be the ORIGINAL GQ incidence host, and fix genuine f and all right line labels outside a finite moving source-line block B. Let E be an available physical-pair label image set with |E|>=|B| and disjoint from the fixed labels. Let F consist of **ALL injective** assignments g_B:B→E. For each actual six-source-line multiset m, J41–J42 define the exact nonnegative integer S_m(f,g) counting **true ORIGINAL six-incidence Q**, including the D6 source-line-named positional dual, with no proper-P3 requirement.

Assume for a particular anchor r∈B and EVERY legal possible physical image e∈E one can produce a genuine ORIGINAL line profile m_{r,e} satisfying:

1. `supp(m_{r,e}) ∩ B = {r}` (no other movable right line factor);
2. for every globally injected completion g with g(r)=e, `S_{m_{r,e}}(f,g) >= q_{r,e} >= 1`.

By J44 original line support locality, the profile's score is constant over g with g(r)=e, so checking one legal representative per image suffices. Define `q_r=min_e q_{r,e}>=1`. Then for **EVERY globally injected completion g∈F**, some ORIGINAL sixset profile attached to r has at least q_r genuine positive Q.

This is NOT a claim that such an anchor/profile choice exists for every W(3,s), original f, or arbitrary physical alphabet.

## 3. J48 — capacity transfer without the usual 6-fold loss

Suppose the J47 hypothesis holds for a set R⊆B of distinct original anchor lines. Fix one complete globally injected g. Each star r∈R supplies at least q_r distinct positive ORIGINAL six-incidence Q with `supp_right(Q)∩B={r}`. If r≠r', an original Q selected for r cannot be selected for r', since its true ORIGINAL line support cannot intersect B as both {r} and {r'}. Thus the witness Q families are pairwise disjoint and

`S_s(f,g) >= Σ_{r∈R} q_r`.

**There is NO /6 multiplicity penalty.** This is an exact all-h conditional source-incidence theorem, not a numerical finite fit and not an unconditional `S_s=Ω(s^6)`.

If one relaxes the one-line support condition and allows a selected ORIGINAL Q at several anchors, the direct incidence counting inequality still holds. For arbitrary anchor witness families `A_r(g)` made of true accepted six-incidence sets containing original right factor r, define multiplicity `d(g)=max_Q #{r:Q in A_r(g)}`. Since each Q contains only six ORIGINAL incidences, `d(g) ≤ 6`. Therefore

`S_s(f,g) >= |∪_r A_r(g)| >= ceil(Σ_r |A_r(g)|/d(g)) >= ceil(Σ_r |A_r(g)|/6)`

when the denominator is defined (empty population separately gives zero). This is a universal charge-cap *conditional on real witnesses*, not an all-h guarantee that many witnesses exist.

The Python oracle checks actual ORIGINAL incidence IDs, genuine original line factor support, Q distinctness, exact overlap d, and both general and block-one-source-disjoint capacity bounds, failing closed on any repeated Q within an anchor or invalid anchor support.

## 4. J49 — exhaustive true ORIGINAL W32 finite star portfolio

Use exactly one actual GQ W32 original-left f fixed on S68/S72, the frozen four-ORIGINAL-right-line block B, the occupied physical pair image E of size four, and **all 24** legal global permutations g_B. Compile JPKC-012 exact original incidence tensor once.

For all 24 states:
1. Compute all seven GF5 positive ORIGINAL six-incidence sets via independent complete original `seven_census(..., witness_sets=True)`, with true incidence IDs and positional D6, **not an endpoint-bad P3 proxy**.
2. Compare the exact Q-by-original-line-multiset dictionary with the JPKC-012 tensor's nonnegative source profile scores. Every selected Q appears exactly once in the independent seven-family census.
3. Extract profiles whose intersection with moving original block B is **exactly one source line r**. Verify full cylinder locality: all six legal permutations of the other three block factors have exactly the same profile score for a specified image of r.
4. For each r∈B and image e∈E, choose the profile with the **largest number of genuine positive ORIGINAL Q** (lexicographic tie-break). A star exists only when this value is positive for **all four images**. The per-anchor guarantee q_r is the minimum of the four positive maxima.
5. For every one of the 24 global states, independently collect the selected profile's ACTUAL ORIGINAL six-incidence Q sets, verify each has `supp_right(Q)∩B={r}`, verify disjointness across distinct stars, and certify the sum of star charges is <= the independent full S. If there are no stars, the valid guaranteed lower bound is zero, and it MUST NOT be advertised as a positivity theorem.

W32 is a deliberately small falsification laboratory. Partial fibers and W34 full seven-S requests are fail-closed. This is not exhaustive over all W32 left/right label bijections, not a random-assignment argument, and not a counterexample to Root A.

## 5. Growth obstruction and next research decision

For W(3,s), there are V=(s+1)(s²+1)=Θ(s³) ORIGINAL line factors. Even if every original right line had a J47 star (much stronger than what has been shown), guaranteeing only q_r=1 would give S≥Θ(s³), not the desired Ω(s⁶).

To reach Ω(s⁶) through the disjoint-block star mechanism, one would need **at least Θ(s³) distinct original anchor lines, each transferring Ω(s³) genuine positive six-incidence Q**, or an equivalent aggregate `Σ_r q_r=Ω(s⁶)` over a true original moving block B, for **every** legal f and all original outside right-factor images. The fixed four-line W32 star offers no evidence of this scale by itself.

Before claiming a new theorem, test whether larger original geometric blocks admit uniformly positive image-star portfolios under genuinely global injection, and whether per-factor q_r has any polynomial floor. A carefully constructed zero-star finite example would be a legitimate blocker to the J47 mechanism, not by itself Root B (which requires infinite low-S family).

## 6. Acceptance gate

Exact GitHub-hosted 5-test suite, independent 24-state original-seven census and exact Q-set comparison for S68/S72 matrix jobs, INDEX, Proof Audit, full Research all required SUCCESS on exact final HEAD. Independent mathematical review required before theorem acceptance. No main merges and no ASET exponent assertions.

## 7. Exact first hosted JPKC-014 results and frozen numerical falsifiers

The initial dedicated JPKC-014 GitHub-hosted check on SHA `12ffa4b22339007fccccbc84744f51bd4bc2b1b8` passed **all three jobs**: five negative/source-incidence tests plus both COMPLETE true-original 24-state seven-GF5-Q-set jobs.

**Four single-ORIGINAL-line stars were found in BOTH complete frozen four-line right blocks.** The value listed below is the minimum across ALL FOUR possible physical pair images of the anchor line of the **maximum count of genuine GF5-positive distinct ORIGINAL six-incidence Q** in any available one-moving-factor source-profile cylinder:

| Pinned globally injected original W32 fiber | Source line anchor r | Minimum genuine ORIGINAL Q per physical image q_r | True ORIGINAL Q disjoint from different anchors |
|---|---|---:|---|
| S68 | 0, 1, 2, 3 | **2, 2, 2, 1**, respectively | YES |
| S72 | 1, 7, 9, 12 | **2, 2, 2, 1**, respectively | YES |

For each of the two 24-state fibers the all-h-valid **conditional** block-disjoint factor choice theorem certifies **S ≥ 7** without a /6 loss. Across all 24 states, the actual **minimum number of selected distinct positive ORIGINAL sixsets is 8**, a stronger true-finite observed minimum but not the frozen uniform min-over-images bound. The independent FULL seven-family W32 minimum in both fibers is **68**. The 7 is thus a nontrivial strictly positive factor-choice-derived necessary bound, but it is much weaker than 68; do not conflate it with full S, all-h Ω(s^6), or exact GF5 R3.

Each independent seven_census gives **exact ORIGINAL Q six-ID sets** at each legal global image state. Group by the true original right-line multiset m, require complete equality with all JPKC-012 source profile integer scores; extract only profiles whose source-line support meets the movable four-line block in exactly one line; prove each image-cylinder's profile count invariant across the other 3!=6 legal permutations; finally check all chosen Q sets at their genuine source factor endpoints and their total incidence-ID deduplication. This is not 24 independent Q-wise solutions and not a local path charge.

The source-profile populations with exactly k moving original lines and positive on at least one legal state are:
- S68: k=0:6; k=1:93; k=2:175; k=3:36; k=4:1.
- S72: k=1:97; k=2:181; k=3:21 (k=0 and k=4 have zero active profiles).

The S72-only original line #7 4-way disjoint mask partition seen in JPKC-013 therefore extends to **all four original factor anchors**. The new structural observation is that the whole four-line source block has full per-image positive cylinders, not just one line; and those per-anchor Q witnesses are pairwise ORIGINAL-line-support-disjoint, enabling a sum of four guaranteed charges.

**Important generalization barrier:** for W(3,s), the number of original lines is Θ(s³); if every line contributes just O(1), even perfect disjointness only gives O(s³), not the target Ω(s⁶). Future work must prove Ω(s³) positive Q per anchor on average for Ω(s³) eligible anchors, or find a different amplifier. No universal existence of a choice-star has been proved.
