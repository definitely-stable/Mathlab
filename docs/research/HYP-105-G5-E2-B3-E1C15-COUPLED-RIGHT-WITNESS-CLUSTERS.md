# HYP-105 B3.2-E1-C15 — exact coupled-right witness clusters under one common original GQ line map

Date: 2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), stacked after C14 [#296](https://github.com/definitely-stable/Mathlab/pull/296). C7-B #280 remains a separate branch, not an ancestor.

**TYPE: RESTRICTED EXACT THEOREM / TRUE W(3,2) FINITE K6 IMPLEMENTATION.** An all-f,g all-h seven-class S>=Omega(s^6) or full GF5 R3 claim is NOT established. This phase strengthens the mathematically certified lower for each fixed partial original left/right K6 mapping and verifies exact finite joint completion boxes.

## 1. Research motivation and choice

C14 verified on genuine W32 original-GQ reverse-line 12 original-left/12 original-right fixed physical pair labels, with exactly 3!²=36 remaining genuine two-sided full map pairs:
- independent exact seven-family minimum across all 36 = 148;
- independent exact GF5 ACCEPTED NECESSARY numerator minimum across 36 = 6,676,842;
- C14 per-witness independent right minima at root give only S>=2 and GF5 numerator>=91,200;
- C14 proof-based branch visits 73 nodes, recounts 3 legal complete maps and correctly prunes 33 subtrees.

This shows a large correlation loss. Physical symmetry alone (C13) leaves >=4,581,437,148,288,000 full W32 joint mapping pair orbits, so expanding the symmetry sweep is not an adequate next step.

**Selected mechanism:** partition C14's left-pinned eligible ORIGINAL six-incidence witnesses into disjoint groups according to the exact set of their touched **currently unpinned ORIGINAL right lines**. Within each group, enforce ONE common right injection. Then optionally unify **all** eligible witnesses under the SAME full residual right bijection. This yields a provable three-level lower hierarchy. Independent score minima for different groups are LOWER CERTIFICATES, not simultaneously attainable global right-map witnesses. The last level does require one common right bijection and is the strongest possible bound given exactly C14's already eligible original-left-pinned witness subset and frozen left endpoints.

## 2. Three nested rigorous inequalities and proof

For any finite original bipartite incidence host and arbitrary legal partial injective f_0,g_0, let W(f_0) be ANY chosen set of distinct actual six-incidence sets J whose original left point endpoints are ALL already assigned under f_0. The true left physical structure of these sets is frozen, and their physical right projection depends only on g. Other original six-incidence sets are ignored; their accepted seven indicator and GF5 NECESSARY class-floor numerator are nonnegative.

Let U be the remaining ORIGINAL right lines; Q the remaining physical right-edge labels, and Π(U,Q) all bijections U→Q. For each J∈W define its right support M_J= {ORIGINAL right line endpoints appearing in J}∩U. For each π∈Π, let

    a_J(π) = 1[J belongs to one of the accepted seven ORIGINAL motif classes
                 under the fixed left f_0 and the SINGLE full right completion g_0∪π],
    b_J(π) = accepted GF5 NECESSARY lower numerator of this tag (0 if absent).

Both functions are NONNEGATIVE and apply to actual ORIGINAL incidence sixsets; classification labels may vary with π. Partition W by the EXACT named ORIGINAL signature M, with W_M={J∈W:M_J=M}. Define

    L_single(S) = SUM_J min_(π∈Π) a_J(π)       [C14's exact local envelope],
    L_cluster(S)= SUM_M min_(π∈Π) SUM_(J∈W_M) a_J(π),
    L_shared(S) = min_(π∈Π) SUM_(J∈W) a_J(π).

Then, with no distribution assumptions or made-up global independent maps,

    0 <= L_single(S) <= L_cluster(S) <= L_shared(S)
       <= S_seven(f,g)

for EVERY SINGLE legal full two-sided continuation (f,g) of the partial f_0,g_0.

**Proof:** (1) the restriction of any common full g to U is one π∈Π; (2) a_J and b_J are true nonnegative contributions of the same original six-incidence J; (3) the groups W_M form a DISJOINT partition of W with each original J included ONCE; (4) the elementary inequality Σ min ≤ min Σ applies both inside each group and across the groups; (5) ignored original J outside W contribute nonnegative amounts. The exact same inequality chain holds for b_J GF5 class-dependent accepted NECESSARY numerator.

Because every injection M_J→Q extends to a bijection U→Q, min_π a_J(π) equals C14's per-J local minimum EXACTLY. The new source oracle checks this equality numerically against independently implemented C14 for the same f_0,g_0, not only via this proof.

**Conditional sharpness:** L_shared equals the TRUE minimum, over all possible right-map continuations, of the ACCEPTED seven count from the chosen eligible left-pinned subset W with the left labels fixed. It is NOT necessarily the minimum of the FULL seven-family total, since sixsets touching unpinned original left points have been omitted. If all original left points are pinned and W is the full accepted-left 2factor source, L_shared is the exact best full-right-map seven objective (at that fixed original-left f_0 and partial g_0), for bounded right-tail dimension.

## 3. Monotonicity and exact branch decisions

Fix any legal partial extension f_1⊇f_0 and g_1⊇g_0. Every formerly eligible original sixset with all left endpoints pinned remains eligible with unchanged physical left projection; new ones may become eligible. The full permitted right-map completion domain is restricted, so

    L_single(f_1,g_1) >= L_single(f_0,g_0),
    L_cluster(f_1,g_1) >= L_cluster(f_0,g_0),
    L_shared(f_1,g_1) >= L_shared(f_0,g_0),

and likewise for the GF5 accepted necessary numerator. Under g extension the right-support signature groups can MERGE when a formerly unpinned original right line becomes pinned; a group never splits under that signature projection. This preserves the lower hierarchy and monotonicity. Under f extension the witness family only grows, each added cost nonnegative.

A bounded finite joint branch-and-bound compares THREE modes `single`, `cluster`, and `shared` using IDENTICAL legal full-map incumbent initialization, left-before-right original pin assignment order, independent accepted `seven_census` at every nonpruned full leaf, and HARD node and local motif-classification budgets. For the same objective ("S_seven" or "GF5_floor_numerator"), a node lower reaching the incumbent prunes the whole remaining subtree without discarding any strictly better solution. The solver never claims a completed certificate after budget exhaustion; it raises instead.

At any *same node*, the hierarchy guarantees stronger lower bounds; however different incumbent discovery histories and branch ordering can change observed runtime/node counts. The report compares exact modes and records actual visits, leaves, and pruned subtrees rather than assuming a measured speedup.

## 4. Exact implemented W32 test scope and adversarial falsifiers

Only complete K6 physical pair palettes on BOTH sides of actual symplectic W(3,2) are supported by the executable. The accepted E1-A left 2factor source generator yields exactly 62,370 candidates for every completed legal left K6 labeling. The implementation makes a valid filler only to enumerate these ORIGINAL incidence sets and **omits** those touching any not-yet-pinned ORIGINAL left point. It never presents the filler as a universal physical left mapping. Every eligible original incidence sixset J is evaluated for EVERY genuine shared completion π of the remaining at-most-three ORIGINAL right lines; right completions are true injective bijections into the remaining occupied physical K6 edges.

Independent proof gates:
- Every fully pinned model's C15 single/cluster/shared seven and accepted necessary GF5 numerator MUST exactly equal independent `seven_census`, with no positive sixsets omitted.
- On true original W32 12+12 partial model (3!²=36 full joint maps), all three levels of both scores must be ordered and the strongest shared lower valid for EVERY one of the 36 independently enumerated full pair maps; the independent exhaustive minimum is 148 for seven, and 6,676,842 for accepted GF5 NECESSARY numerator.
- On 13+13 (2!²=4) partial model, each of the three C15 branch policies must yield the same exact seven minimum and, separately, the same exact GF5 NECESSARY numerator minimum as the independent full enumeration.
- Under independent actual left and right original pin extensions, cluster/shared lower never decreases for either objective.
- Invalid noninjective original/physical mappings, excessive missing right dimension, budget truncation, unsupported objective and invalid branch mode all must FAIL CLOSED.

A dedicated C15 report separately benchmarks THREE modes on the SAME original 12+12 rooted 36-map box against one complete independent enumerator. It records root C14 singleton/cluster/shared lower, GF5 necessary root lower, actual left-pinned witness count, right-line signature clusters, total right completions, nodes visited, leaves recounted and pruned subtrees. No performance or numerical gain is predeclared before actual CI results.

## 5. Acceptance and mathematical decision

The dedicated GitHub-hosted `hyp105-c15-contract` and full `research` CI on the EXACT PR HEAD must both be SUCCESS; C0–C14 upstream dependency PRs are not merged by this phase. Parent #230 OPEN_WITH_FORMAL_BLOCKER; no full 15!² original GQ joint minimum, no GF5 full R3 and no all-h obstruction proven.

**Decision gate after results:** if right-signature/global right coupling remains weak at the ROOT (because most potentially positive original sixsets touch still-unpinned ORIGINAL left points), next research phase must use **two-sided witness domains**: provably safe groups of original source six-incidence sets sharing unpinned ORIGINAL left AND right factors, combined with physical K6 2factor-codegree and GQ-concurrency structure. Avoid continuing to increase only right correlation when the actual blocker is left eligibility. An exact finite 36-map solver by itself does not establish an all-h Ω(s^6) obstruction.
