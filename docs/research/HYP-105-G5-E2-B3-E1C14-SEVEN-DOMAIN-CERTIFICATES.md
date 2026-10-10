# HYP-105 B3.2-E1-C14 — Sound seven-family domain-minimum certificates for partial joint GQ embeddings

Date: 2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked on C13 [#292](https://github.com/definitely-stable/Mathlab/pull/292), dependent on C0–C12 in their stated order. C7 conditional selector #280 is not an ancestor.

**TYPE: ALL-FINITE-NONNEGATIVE-MOTIF-OBJECTIVE SOUND-LOWER THEOREM / EXACT W(3,2) FULL-K6 CERTIFICATE + BOUNDED FINITE BOX OPTIMIZATION.** This implementation does **not** prove any new all-h positive Ω(s^6) lower for all f,g, all seven families, the full GF5 R3, or an ASET exponent. Only executable W(3,2) complete physical K6-left/K6-right mapping pairs are certified here. Partial mapping bounds are global over the **remaining completions in the chosen node**, not global over all possible root pairs.

## 1. Deep post-C13 diagnosis and choice among three C14 approaches

C13 showed an exact simultaneous original Sp4/GQ-left-physical/right-physical orbit of size 373,248,000 for the sample pair, yet even the maximally favorable full quotient of (15!)² possible left/right K6 assignments contains at least 4,581,437,148,288,000 distinct joint orbits. This makes unstructured orbit enumeration infeasible on GitHub-hosted CI. A C14 algorithm must legally discard whole subtrees without falsely assuming arbitrary physical edge permutations are symmetries.

Rejected:
- **Brute canonical pair sweep**, even with C13's entire 720³ group: the exact finite counting floor above rules it out.
- **Product of independent anchor-specific minima as an actual (f,g) witness**: C4, C8–C10 established the danger; incompatible local maps cannot be combined into an attainable globally consistent embedding.
- **Exact unrestricted full 15!² optimization in a single PR**: no manageable verification budget or mathematical pruning theorem justifies it.

Selected:
- Derive a genuinely **admissible, monotone, structural lower bound** on the complete seven-family objective, valid for every full joint (f,g) completion of an arbitrary partial left/right map. The lower must be computed from actual ORIGINAL six-incidence sets with physical left-side six-edge two-factor constraints and right-side injective-label residual domains, not probabilistic heuristics.
- Verify **independently** against all complete mappings in small exact W32 joint completion boxes (two free each: 2!²=4; three free each: 3!²=36).
- Combine that bound with an incumbent from a REAL complete (f,g) and exact joint branch-and-bound to prove a **box-specific** minimum. Prove monotonicity and strictly enforce computational budgets. Record whether any internal subtree was actually pruned rather than assuming it.
- The global all-f,g target remains OPEN; any finite bounded-box minimum must be labeled with its fixed partial embeddings and not extrapolated.

## 2. Abstract all-incidence additive certificate theorem

Let I be any finite ORIGINAL bipartite incidence edge set, and E_6={J⊆I : |J|=6}. Fix partial injective left physical pair-edge mapping f_0 and partial injective right mapping g_0, with arbitrary legal global injections f,g extending them. Let χ_7(J;f,g)∈{0,1} denote that J belongs to ONE OF the seven accepted six-incidence motif classes, and let w_7(J;f,g)≥0 be its previously proven GF(5) **necessary floor numerator** according to its actual class (0 for unselected J). Define

    S_7(f,g) = Σ_(J∈E_6) χ_7(J;f,g),
    N_GF5(f,g) = Σ_(J∈E_6) w_7(J;f,g).

Let C(f_0)⊆E_6 be ANY conservatively known set of original six-incidence subsets such that each J∈C has **ALL of its ORIGINAL left point endpoints assigned** in f_0. Then the exact physical-left-side verdict for J is fixed under ALL full extensions. For every such J, let R_J(g_0) be the set of all **injective local** assignments of the yet-unassigned ORIGINAL right lines that occur in J, into pair-edge labels not occupied by g_0. Since the full right mapping is a complete bijection onto its actual chosen physical palette, every local injection extends to a full right injection. For J where the fixed left half passes its physical structural filter, set:

    a_J(f_0,g_0) = min_(ρ∈R_J(g_0)) χ_7(J; f_0, g_0∪ρ),
    b_J(f_0,g_0) = min_(ρ∈R_J(g_0)) w_7(J; f_0, g_0∪ρ).

Then for **EVERY single legal common full** pair f,g extending both f_0,g_0:

    S_7(f,g) >= L_7(f_0,g_0) := Σ_(J∈C) a_J(f_0,g_0),
    N_GF5(f,g) >= L_GF5(f_0,g_0) := Σ_(J∈C) b_J(f_0,g_0).

**Proof:** For each considered ORIGINAL J, the restriction of the actual COMMON global right g to its unpinned right endpoints is one member of R_J(g_0), hence each actual 0/1 motif indicator is ≥a_J and each actual proven class numerator ≥b_J. Summing the inequalities over distinct ORIGINAL J gives the result. Unconsidered ORIGINAL sixsets contribute nonnegative objectives. There is NO assumption that choices attaining the individual minima belong to one global g. The inequality is valid precisely because min Σ≥Σ min for nonnegative, separately considered terms; it does NOT construct any map achieving L_7 or L_GF5.

The seven class labels may change with ρ. The GF5 numeric floor is minimized over those changes; it is **NOT** assumed a fixed GF5 coefficient across the local domain. A per-class count lower for class c is incremented only if **all** local options belong to that exact c. Thus a positive all-seven lower may coexist with zero per-class fixed-label lower.

## 3. Monotonicity and sound branch pruning

For a partial extension (f_1,g_1)⊇(f_0,g_0), consider any J∈C(f_0): all its original left points remain fixed, so its physical-left admissibility is unchanged, and it remains enumerated in C(f_1). Its locally allowed right assignment set R_J(g_1) is a nonempty **subset** of R_J(g_0), when interpreted as full values on all unpinned original right lines in J. Therefore

    a_J(f_1,g_1) >= a_J(f_0,g_0),
    b_J(f_1,g_1) >= b_J(f_0,g_0).

All newly eligible source sixsets have nonnegative floors. Consequently L_7 and L_GF5 are monotone nondecreasing under **any** legal original-left/right pin extension, even though the remaining right physical domains shrink globally. This is a theorem about certified bounds, not about the actual objective along different arbitrary map completions.

Take any **actually complete** joint map (f*,g*) in a fixed residual box as an incumbent with objective B. At any partial node, if the certified lower L_7(node)≥B (or L_GF5(node)≥B for a separate GF5-floor minimization), no descendant can improve on the already attainable B. Hence the entire subtree can be safely pruned. If a node's lower is >a global incumbent found in a **different** subtree, this is normal and must cause pruning, NOT an assertion failure. The solver separately runs a full independent exact seven_census at every unpruned leaf. It never certifies a complete-box optimum after exceeding a node or local-motif budget.

## 4. Independent complete W(3,2)/K6 realization

The pre-existing accepted seven_census generator has exactly 62,370 ORIGINAL six-incidence candidates whose **physical-left** projection is an A/B/C six-edge two-factor: 51,030 A + 10,935 B + 405 C. This is complete for EVERY full bijective physical-left labeling of the genuine W(3,2) original 15 point factors onto all 15 K6 pair edges. The C14 implementation creates an arbitrary canonical legal filler map only to invoke that exhaustive left template enumerator, and DISCARDS every candidate touching an unpinned ORIGINAL left point. For candidates touching only pinned left points, the labels and source eligibility are completely independent of how other left points were filled. Every such candidate is counted at most once, its ORIGINAL six actual incidence edge IDs are preserved, and the total generator count is asserted to be EXACTLY 62,370. No arbitrary filler edge assignment is mistaken for a universally representative left map.

For every eligible ORIGINAL sixset, enumerate ALL injective assignments of its remaining, touched, ORIGINAL right line IDs into the physically unoccupied right K6 edge labels (at most three unpinned original right lines in this C14 implementation). For each option evaluate the ALREADY ACCEPTED `classify_seven_prechecked`, with genuine fixed ORIGINAL incidences and physical endpoint labels, and use the accepted `R3_CERTIFIED_FLOORS` as a **necessary** GF5-floor numerator only. The reference emits separate values for frozen positives, locally inevitable positives, full guaranteed class counts, whole seven-family L_7, and GF5 necessary L_GF5.

The explicit executable gate requires at most THREE unpinned ORIGINAL right lines. Larger right-tail nodes fail closed rather than pretending to have computed a complete conditional envelope. Every considered local injection is counted toward a hard classification budget; a budget breach raises an exception with NO falsely complete certificate. These bounds are exact sound relaxations for the node, but **not** the exact minimum unless matched by an independent complete legal map with the same objective.

## 5. Bounded exact joint W32 completion boxes and independent oracle

The research reference fixes, using canonical actual ORIGINAL point and line indices, either:
- the first 13 original W32 left points and first 13 original right lines to their historical reverse-line full-K6 physical labels, leaving 2!×2!=4 COMPLETE legal joint maps; or
- the first 12 original W32 left points and first 12 original right lines, leaving 3!×3!=36 COMPLETE legal joint maps.

An **independent**, fully explicit enumeration constructs each legal full left/right physical mapping pair and calls the EXISTING full `seven_census` to compute exact S_7 and accepted GF5 necessary numerator. Separately, C14's sound branch-and-bound uses admissible local domain-minimum floors at partial nodes and genuine full `seven_census` at leaves. Its returned exact minimum is valid only WITHIN THAT FIXED PARTIAL BOX and only if the complete finite process terminates within the hard budgets; tests require agreement with the independent full enumeration. Metrics report visited nodes, explicit complete leaves and ACTUALLY pruned subtrees, so a no-pruning result is not disguised as an engineering win.

The 13+13 root, its one-step left/right extensions, and the fully pinned true reverse-line map are compared for monotonic L_7 and L_GF5; at zero missing pins the bound MUST equal the full independent S_7 and GF5 necessary-floor numerator exactly. Wrong duplicate physical images, boolean keys, unsupported objectives, too many free right lines, local evaluation exhaustion, incomplete-box size and tree node budget all fail closed.

## 6. Independent GitHub-hosted REAL W32 finite result — positive but weak early floor

Dedicated C14 Contract on first PR HEAD f25e145ce1d36cbc34e3e30620e8775d57944ba2 **SUCCESS: 6/6 independent tests** and complete exact report, run [#38081738228](https://github.com/definitely-stable/Mathlab/actions/runs/38081738228). In the genuine symplectic W32 reverse-line physical K6/K6 partial box whose first 12 ORIGINAL left points and first 12 ORIGINAL right lines are held fixed at their historical pair-edge labels, independent exhaustive enumeration checks EVERY 3!×3!=36 real complete joint maps. Separately the certified branch-and-bound agrees with the true box minimum.

| Honest finite metric | Exact independent value |
| --- | ---: |
| Every legal full joint map in this rooted box | 36 |
| Exact minimum S_seven across these 36 | **148** |
| Certified local-seven floor at the ROOT partial node | **2** |
| Actual frozen-both-halves motif count at ROOT | 2 |
| Exact minimum ACCEPTED GF5 necessary numerator in the box | **6,676,842** |
| Certified local GF5 necessary numerator at ROOT | **91,200** |
| Branch-and-bound nodes visited | **73** |
| Distinct complete leaf maps fully recounted | **3** |
| Pruned internal subtrees | **33** |

This distinguishes correctness from strength. The root partial certificate proves ONLY S_seven>=2, far weaker than the true exact box minimum148; the GF5 necessary lower91200 is similarly much weaker than 6676842. The solver pruned 33 subtrees only AFTER the remaining physical domains shrank enough during deeper decisions. The 73 visited nodes and 3 actually recounted leaf mappings are finite algorithmic observations for THIS rooted completion box and objective ordering, not a general complexity estimate. They are now pinned as exact CI regression assertions, as is the independent GF5 objective branch test on the 2!²=4 box. Acceptance of these frozen assertions on the NEW HEAD still requires dedicated+full Research CI.

This is NOT a global W32 min: a concrete C11 map outside this rooted 12+12 box has seven S=141, smaller than box min148. That concrete counterexample conclusively forbids promoting the box result S>=148 into any all-f,g statement. Likewise the bound 2 at the box root cannot be stated as a universal all-h lower, no matter how many subtrees were pruned.

## 7. Research interpretation, acceptance, next decision

A positive C14 lower for a 12+12 or 13+13 rooted residual box proves that every complete joint f,g EXTENDING those actual 24 or 26 assigned physical pins has at least that many accepted seven-family motifs. It does NOT prove the original issue's infimum over ALL possible f,g; most W32 full-map space lies outside that box, and the C13 quotient still contains >=4,581,437,148,288,000 global orbits. Likewise a positive GF5 necessary-floor numerator is a property of seven-family selected terms, not the entire signed GF5 R3.

**Acceptance** requires GitHub-hosted dedicated `hyp105-c14-contract` and full Research SUCCESS on exact PR HEAD, ordered integration of C1–C13 and postmerge main CI. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER. Avoid saying "all-h obstruction", "exact global W32 optimum", or "full GF5 R3" on the basis of a bounded box.

**C15 priority:** strengthen per-sixset local minima by retaining **coupling among several ORIGINAL six-incidence sets** (e.g. small shared-right-line clusters or exact constrained physical 2factor codegrees), using independent true joint-map falsifiers. The mathematical next target is a lower bound that remains positive *before* pinning most original GQ vertices, or a rigorously infinite counterfamily. Aggregate gains must be reported with empirical reduction in genuinely visited tree nodes; no heuristic candidate ordering is a proof.
