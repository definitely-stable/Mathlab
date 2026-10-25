# HYP-105 / issue #230 — AA4-BN: multi-root Hall compatibility and exact minimal global source-image swaps

**Scientific DRAFT**, strict child of parallel corrected [AA4-BM PR #579](https://github.com/definitely-stable/Mathlab/pull/579) at frozen HEAD `68cda53041075028055374086e6a9a8cc78d9098`. Separately authored earlier AA4-BM [#578](https://github.com/definitely-stable/Mathlab/pull/578) overlaps its four-swap theorem. This slice **does not** claim discovery of that theorem or independently promote either parent. No main/claim-registry edits; root #230 remains OPEN_WITH_FORMAL_BLOCKER.

## Prior results and actual missing step

AA4-BK #576: each genuine original B/C4 cherry has an eligible source sixflag Q with six distinct true opposite factor IDs. AA4-BL #577: under local physical pinned-endpoint hole-degree regularity a physical occupied 2factor A target containing both exact opposite pins exists. Parallel AA4-BM #578/#579: a DIFFERENT full global opposite map can realize ONE chosen root and one chosen target by ≤4 whole-source-image transpositions while preserving its actual two pins.

None establishes that the same global map can satisfy two chosen source Q/target witnesses simultaneously. This is a mathematically precise *coupling obstruction*, not remedied by adding expected counts. The present work isolates an **exact finite combinatorial necessary-and-sufficient compatibility condition**, plus the sharp **minimum** number of transpositions needed to realize **any finite family of preselected original source Q/physical target/slot assignments**. These are exact all-h statements but **candidate-specific**, not a universal two-root existence theorem or root Branch C-equivalence.

## Theorem BN-1: all-h typed original partial matching / optimal swap completion

For every `h>=1`, genuine symplectic original `W(3,2^h)`, every already fixed fully globally injected original physical typed factor map `g: L(W)->E` onto an arbitrary V-edge physical occupied support E in K_a (and its POINT dual), let `R` be any finite collection of actual source-root repair *proposals*, each containing genuine original six-distinct source incidence IDs Q, two original opposite factor pins, and one chosen occupied physical A/2factor on six physical coordinates with an explicit assignment of the other four true original opposite factors to its four remaining physical edges. The original point map f remains globally fixed. Put `P` equal to the UNION of original source-factor pins from **all** proposals.

For each proposed nonpin source factor i, record its desired occupied image edge e_i. The union of candidate prescriptions is *simultaneously realizable by ONE complete original global opposite map g' on the SAME occupied support E fixing every factor in P* **if and only if**:

1. A shared actual original source factor i never receives two different desired images across root proposals (SOURCE consistency).
2. Two different actual original factor IDs never require the same occupied physical edge (TARGET injectivity).
3. Any requested physical image currently belonging to a pinned actual original source ID can only be requested by that identical pinned ID, and every pinned source ID retains its original image (PIN protection).

These are exact conditions on **prescribed candidates**, not on whether a different choice of Q or physical A target could succeed.

Identify each requested target e_i with its current ORIGINAL source owner `j=g^{-1}(e_i)`; discard already-correct loops `i->i`. The directed arrows `i->j` form disjoint directed **open paths** and **nontrivial directed cycles** (indegree/outdegree at most one). Write `k` for the number of nontrivial arrows and `c` for the number of nontrivial closed components. Then the **exact shortest possible number** of unrestricted swaps of WHOLE original source-factor physical pair images to fulfill ALL prescriptions, with every pinned original factor image unchanged **at every intermediate state**, is

\[
\boxed{\operatorname{dist}_{\mathrm{swap}}(g,\mathcal P)=k-c.}\tag{BN-MIN}
\]

Construction: for every open path `i0->i1->...->ir` do successive factor-image swaps `(i0,i1),(i1,i2),...,(i(r-1),ir)` in **forward** order (r swaps). For every directed cycle `i0->...->i(r-1)->i0` do swaps `(i0,i1),...,(i(r-2),i(r-1))` (r-1 swaps). No donor can be pinned by condition 3. Distinct components have disjoint source IDs; every intermediate map is globally bijective, retains occupied support and pins, and both physical projections use the **same original six incidence IDs**.

**Optimality proof:** every eventual full source-owner permutation completing the directed partial matching must contain each complete nontrivial directed cycle as a permutation cycle (cost at least r-1); every open path with r arrows must close inside some permutation cycle of length at least r+1 (cost at least r). Combining two separate paths into one cycle adds at least one swap rather than reducing this sum. The standard Cayley transposition distance is the sum of (cycle length minus one) over nontrivial cycles. Consequently any valid completion costs at least k-c. The displayed explicit construction attains it with pins fixed at each step. This is the classical partial-permutation/cycle idea, **not** a newly discovered algebraic metric.

A connected 2-cycle can save one swap over processing its two requests separately; two open paths do not automatically save anything. If both source roots specify the same ORIGINAL line-factor ID differently, no entire g' can realize these **specific candidate pairs**, even though both were separately repairable.

## Theorem BN-2: exact same-original-sixflag GF(5) multi-root transfer

When every selected proposal really is a genuine original source B/C4 rooted sixflag Q, with six different original opposite factor IDs, and an occupied A/2factor target incorporating both physical original opposite pinned edges, compatibility conditions 1–3 are also sufficient for one **simultaneous** accepted historical GF(5) B-left/A-right motif for **each selected Q** in the same globally completed pair (f,g'). All source Q sets are fixed BEFORE completion, no independent physical label redraw per source set. The source profile, first physical C4 and both original maps have not been independently resampled; the target assignments force the second physical degree-two projection to be class A. Genuine LINE-rooted/POINT-map dual holds.

**Nonimplication:** Neither #577 nor #579 guarantees any chosen TWO roots admit mutually compatible eligible sixflag/target prescriptions, and BN-MIN alone does not bound the original `S_s(f,g)` from below or solve #230 Branch A/B/C. The result makes the exact obstruction executable rather than quietly assuming compatibility. No full R3/ASET implication.

## Independent falsifiers, provenance and limitations

`research/hyp105_issue230_d6aa4bn_multi_root_swap_compatibility.py` implements typed global matching, path/cycle optimal transpositions, pin rejection, and genuine-original incidence/GF(5) candidate verification. Six independent test groups include:

- **150 sampled partially prescribed mappings at each n=4,5,6**, independently EXHAUSTING all n! full permutations and computing minimum Cayley distance by a different permutation-cycle implementation (protected pins fixed), plus every intermediate global injection.
- Two concurrently prescribed source groups with 2-cycles saving swaps, open paths, conflicting shared ORIGINAL source IDs, competing targets, protected-source theft and malformed images.
- FIVE genuine original symplectic W32 complete typed schemes (both source directions): independent parent AA4-BM witnesses are reoptimized for their **exact original Q and selected six-physical-edge target**, preserving actual original factor IDs, and rechecked with the original two-sided GF5 classifier.
- Same *real* W32 original point-side example with two **different** original cherry roots accepted in **one** completed global g' and their preserved original pins, witnessed by the historical seven-class source-ID census; the actual chosen candidate certificates are run through BN-MIN, not synthetic large-h GQ.
- TRUE symplectic original GF4 W34 with occupied nononto physical K14 supports, both typed directions and six-incidence-ID corruption rejection.

Finite W32/W34 witnesses are **not** extrapolated to an all-h simultaneous two-root existence statement. The all-h proof uses only the combinatorial original complete injection and candidate validity; inheritance of source-Q eligibility and physical target existence is strictly from #576/#577 and not independently re-proved here.

Prior art for transposition distance: standard Cayley cycle formula `n - #cycles`; the exact partial-permutation completion follows the same classical proof, and no priority claim is made. Relevant references include Cayley-distance exposition (nLab, Diaconis cited there) and the documented complete-graph token swapping bound (academic token-swapping survey). New scoped contribution is the **typed GF(5) ORIGINAL same-sixflag cross-root constraint interface and rigorous obstruction accounting** within #230.

**Next missing root-facing lemma:** quantify the existence and intersection size of compatible candidate families for **two genuinely different roots** chosen from the >3/4 pin-regular original cherries of every fully fixed adversarial (f,g), not merely provide a candidate-level consistency test. In particular, replacing `forall good root exists repair` with `exists ONE repaired map for many roots` requires an actual lower bound on compatibility independent of original label correlations. Only then can cross-root moment/expansion techniques plausibly approach #230's all-fixed minimax.
