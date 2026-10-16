# HYP-105 / #230 — AA4-AT: exact optimum GLOBAL original-line factor transposition distance to aligned D6

**Scientific status: RESTRICTED exact algorithm and group-theoretic source theorem; genuine W32 finite optimization, not an all-h universal improvement of the parent 5-swap upper.** Research-only Draft child of [AA4-AS #548](https://github.com/definitely-stable/Mathlab/pull/548), pinned HEAD \`7796f52e6badcc520f3894bdd19845ec9dcb1aaa\`. Main untouched. Original #230 universal positive seven-GF5 lower remains OPEN.

## 1. Research frontier and distinctions

Parallel [#547](https://github.com/definitely-stable/Mathlab/pull/547) ALREADY proves every globally fixed genuine original (f,g) has at least s⁶/4 DIFFERENT complete globally injected original line physical factor map g' in the radius-five ball, each accepting ONE SAME source original sixflag Q. Parent [#548](https://github.com/definitely-stable/Mathlab/pull/548) ALREADY proves **EVERY** original eligible Q separately accepts D6 after at most five global line image swaps, and original source potential (2/3+o(1))s¹⁵. Parent [#545](https://github.com/definitely-stable/Mathlab/pull/545) originally established a single five-swap repair and exceptional physical edge coverage. No overlap/bulk-positivity of ONE fixed central map was shown.

**New AA4-AT:** treat the bound **five** as an optimization claim and derive the EXACT MINIMUM number of swaps of ENTIRE original line factor physical edge labels needed to realize ANY specified oriented six-edge physical C6 target on SIX actual original line source factor IDs, with all other original line sources free to change but the full globally occupied physical image fixed. On true original W(3,2) K6 this reduces the full optimization over ALL physically available original D6 repairs to a finite, exact 720-target enumeration for EACH actual original eligible six-ID source Q. It supplies a witness and an independently verifiable shortest-distance certificate, without confusing chosen parent constructive ≤5 with actual minimum.

The purely symmetric-group/permutation distance component is **classical**, not a claimed novel general theorem. The new research capability is its exact coupling to six real original symplectic incidence flag IDs, global K6 source physical edge images, historical selected GF5 D6 positional alignment and the ability to falsify asserted universal reductions of radius five by a **strict genuine-original witness**, should one be found. The existence/nonexistence of any W32 distance-five source Q is an empirical output of the hosted source tests, not assumed in the proof.

## 2. Exact true ORIGINAL partially constrained global swap theorem

Fix any genuine original W(3,s) point/line source maps, one actual eligible source sixflag Q with six DIFFERENT source LINE factor IDs \(I=\{\ell_0,\ldots,\ell_5\}\). Fix one oriented physically occupied connected C6 of six source LINE physical pair edge images \(\mathbf e=(e_0,\ldots,e_5)\) assigned in the SAME cyclic order as the point-side six-position physical C6 under f. Images \(e_i\) must be SIX different actually globally occupied physical line edge labels of original g, rather than invented K_a edges outside its image.

Let \(o(e)\) denote the UNIQUE original line factor ID currently owning physical edge e under g (global injection). Define the partial injective self-map of actual ORIGINAL factor IDs

\[
T:I\longrightarrow L_{\rm original},\qquad
T(\ell_i)=o(e_i).
\]

This map has no branching or mergers because target e_i are distinct and g is globally injective. It is a union of (a) paths from I to the first factor outside I; (b) directed cycles wholly contained in I; and (c) fixed loops. Let \(M=|\{i\in I:T(i)\ne i\}|\) and \(c_{\ge2}\) be the number of nontrivial directed internal cycles of T (length≥2).

**Exact source-factor global transposition distance theorem for a FIXED D6 physical target**:

\[
\boxed{\operatorname{dist}_{\rm whole\ source\ factor}(g,\mathbf e\ \text{at}\ I)
=M-c_{\ge2}.}
\]

Proof of achievability: for each indegree-zero constrained path, swap the physical edge images of consecutive original source factor IDs along the path until the desired terminal outside owner supplies its image; this freezes each path source once and costs one swap per nonfixed constrained vertex. For every remaining internal directed cycle of length k≥2, swap along k−1 successive source pairs to achieve the entire cycle target; a fixed loop costs zero. All swaps apply to WHOLE ORIGINAL line factor images and never change source incidence flags, while preserving the exact globally occupied physical line image support.

Proof of optimality, independent of the greedy construction: the final globally bijective source-factor label reassignment relative to g is a FULL permutation extending the partial assignment T on I. Every permutation requires exactly V minus its number of disjoint cycles whole-factor transpositions. The maximal possible cycle count among all such extensions closes each path separately and preserves every existing internal T cycle. This gives exactly \(M-c_{\ge2}\), achieved by the explicit path/cycle swaps. An **independent oracle** exhaustively enumerates every full permutation completion for V=7,8 and verifies this formula for all \((7)_6=5040\) and \((8)_6=20160\) ordered six-factor physical-owner targets. A separate literal global-transposition BFS on V=7 checks shortest paths without using the algebraic cycle count.

## 3. Exact TRUE ORIGINAL W(3,2) D6 minimum (all physical alternatives)

For a TRUE ORIGINAL W(3,2) full K6 globally injected typed f,g, the physically occupied ORIGINAL line physical pair edge image is ALL 15 edges of K6. Every oriented physical six-cycle is specified by a permutation of its six PHYSICAL coordinates, giving **exactly 6!=720** sequences of six different currently occupied physical line images. Each sequence, aligned to the same physical point C6 FLAG POSITIONS on the exact original Q, defines one valid fixed-source six-target partial bijection T.

Thus for each TRUE ORIGINAL eligible Q,

\[
\boxed{
d_{\rm D6}(Q;f,g)
=\min_{\text{all }720\text{ oriented physical }K_6\text{ cycles }\mathbf e}
\bigl(M(\mathbf e)-c_{\ge2}(\mathbf e)\bigr).
}
\]

No original incidence Q is modified and no original line factor source is redrawn. A shortest-target global source swap sequence is materialized and checked under the **existing actual original seven-GF5 D6 classifier** and a separate literal physical edge-intersection adjacency oracle. In particular \(d_{\rm D6}(Q;f,g)=0\) iff that Q was already accepted as D6 by the original globally fixed f,g; real original S68/S72 are historical D6-ZERO fixed maps, so every one of their eligible Q has strictly positive minimum distance.

This gives an EXACT local optimal distance to positive ORIGINAL D6 under the allowed global physical image-preserving transpositions, not a generic search-space heuristic. The known parent all-h bound ensures \(d_{\rm D6}\le5\) for EVERY such Q, while this W32 exact minimum reveals whether original Q actually require 0..5 exchanges. **It must not be extrapolated from s=2 to all h.** For larger a, the fixed-target \(M-c_{\ge2}\) formula still holds; exhaustive enumeration over all occupied a-coordinate six-cycles is intentionally NOT called "complete" on W34/W38 because it is combinatorially much larger.

## 4. Independent source model falsification and novelty limits

- Exhaustively all 5,040 and 20,160 injection targets of six constrained ORIGINAL source factor IDs into total global V=7,8 source factors. Compare the new partial graph \(M-c_{\ge2}\) with an unrelated FULL permutation-extension Cayley distance \(V-\#\text{cycles}\). Independently verify the actual global swap-construction output, full image preservation and original six targets for EVERY case. A restricted source-permutation BFS on S7 gives a separate shortest-distance oracle without using any cycle formula.
- Genuine true original W32 globally injected f/g maps lex, reverse, S68, S72: enumerate ALL physically admissible original source six-ID Q, select deterministic diverse Q subsamples, and compute exact distance over ALL 720 physical line-D6 target orientations for EACH sampled Q. Compare each observed distance to an actual constructed shortest full global map, historical true ORIGINAL selected seven-GF5 D6 and an unrelated physical original flag-position intersection oracle. Negative S68/S72 fixed original g has no D6 at distance zero, while other distances are independently optimized per original Q.
- Compare the PREEXISTING #548 ≤5 global-line-swap repair of the SAME true original Q against the NEW exact optimum; the constructive parent may use MORE swaps than optimum, but never fewer than a rigorous exact minimum.
- Reject fake repeated actual original Q incidence IDs, source line-factor repetitions, noninjective physical global map, synthetic invalid target owner tuples, incomplete target lists, wrong W34/W38 use of a W32-specific exhaustive procedure.
- All results stay scoped to TRUE ORIGINAL sixflag candidate Q and the selected D6 class only. There is NO lower on the entire seven-GF5 accepted sixset population for EVERY fixed f,g, no Branch A/B/C resolution, no full R3/ASET exponent. Prior true W32 zero D6 remains an important fixed-center countercontrol.
- The exact shortest-distance formula is elementary group combinatorics; its mathematical contribution is certification for HYP-105 true ORIGINAL global factor-label repair. A single W32 witness with distance5, if found, proves the earlier all-h bound FIVE cannot be uniformly lowered to FOUR across ALL orders; conversely an observed W32 max4 does NOT prove an all-h radius4 theorem.

## 5. Acceptance and next root-relevant step

Keep STRICT Draft child of #548. Require exact FINAL HEAD dedicated/INDEX/Proof Audit/Full Research hosted success and an INDEPENDENT mathematical referee before any scientific RCP canonical JSON claim registration, generation of five derived Markdown indexes, or merging stacked PRs. No main changes.

Next mathematically relevant AA4-AU gate: determine (by exact true W32 full original Q optimization or a genuinely all-h combinatorial theorem) whether five swaps are SHARP, and then bound **simultaneous** source-Q repairs per one common nearest global g'. For any full seven-GF5 root lower, source D6 and compensating source B/A,A/B,B/B,C modes must be counted in the SAME unmodified fully correlated pair f,g; optimizing candidate-by-candidate swaps changes g and cannot by itself close #230.
