# HYP-105 B3.2-E1-C19 — two-anchor obstruction to bounded shared-left witness blocks

Date 2026-10-11. Parent theorem [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Scientific ancestors: C16 [#305](https://github.com/definitely-stable/Mathlab/pull/305), C17 [#308](https://github.com/definitely-stable/Mathlab/pull/308), C18 [#310](https://github.com/definitely-stable/Mathlab/pull/310). CI sharding [#306](https://github.com/definitely-stable/Mathlab/pull/306) is a **parallel** branch, NOT merged here.

**STATUS: RESTRICTED ALL-h NO-GO FOR SEPARATELY MINIMIZED BOUNDED ORIGINAL-LEFT-SUPPORT BLOCKS.** This strengthens C18: it rules out positive independent minima even when a block enforces ONE SHARED original-left injection over **many different** motif supports, plus arbitrary joint right coupling. It does NOT prove or refute that every complete global original W(3,s) labeling has S=Omega(s^6).

## 1. All-h theorem and exact target alphabet

For ALL integers h>=1, s=2^h, let V=(s+1)(s²+1), and let a be the MINIMAL integer with binom(a,2)>=V. Let F_L be ANY size-V set of OCCUPIED distinct physical unordered edges of K_a. Missing edges are allowed and adversarially placed. Right occupied images and right-line physical mapping are arbitrary.

Write t=binom(a,2)-V for the number of missing physical edges. By minimality,
0<=t< a-1. Thus sum of missing-edge degrees over all a physical coordinate vertices equals 2t<2(a-1). THERE MUST BE AT LEAST TWO distinct physical vertices x,y, EACH incident to at most ONE missing edge: otherwise at least a-1 vertices would have missing degree >=2 and 2t>=2(a-1), contradiction.

The union of occupied physical edges incident to x or y (the OCCUPIED TWO-ANCHOR DOUBLE-STAR) contains at least

    [deg_Ka(x)+deg_Ka(y)-1] - [missing_degree(x)+missing_degree(y)]
      >= (2a-3)-2 = 2a-5

distinct physical edge labels. For s=2, (V,a,t)=(15,6,0), so the exact double-star has 2a-3=9 physical pair edges. For s>=4, a>=7 and 2a-5>=9. Let

    B(s) = 9 if s=2;
           2a-5 if s>=4.

This is an explicit uniform all-h bound B(s)=Theta(s^(3/2)); since V=Theta(s³) and a=Theta(s^(3/2)), B(s)<<V.

## 2. Destruction of EVERY six-incidence witness in a shared named-left block

Fix NO original LEFT point pins. Take ANY family W of distinct original six-incidence sets J of the actual W(3,s) incidence graph, and let U be the UNION of ORIGINAL left points touched by any J in W. Suppose 1<=|U|<=B(s). W may include ANY mix of original sixset factor-left types, any original right-line endpoint correlations, any overlapping supports, and arbitrarily many distinct witnesses. It need NOT be a single C17 missing-left signature.

Choose a single COMMON INJECTIVE left physical assignment alpha:U→F_L mapping ALL named original points in U to |U| distinct edges of the occupied two-anchor double-star. Such alpha exists because the double-star has >=B(s) edges. The same alpha applies SIMULTANEOUSLY to every J∈W. The assignment extends to a complete legal original-to-occupied physical left bijection because exactly V source points and V occupied physical pair edges exist.

For each fixed J, the six ORIGINAL incidences yield six physical left pair-edge occurrences; EVERY occurrence is incident to at least one of x,y because its original left point lies in U. Therefore

    deg_(left-six-projection)(x) + deg_(left-six-projection)(y) >= 6.

The necessary accepted six-coordinate physical-left 2factor condition requires the degree of every physical coordinate to equal either ZERO or TWO; in particular deg(x)+deg(y)<=4. CONTRADICTION. Hence all J in W simultaneously have zero accepted seven-family indicator and accepted GF5 necessary numerator for the SAME alpha, regardless of the right map g and any right pins. No GF5 flow or original GQ automorphism assumption is used.

Thus any lower certificate of the form SUM over disjoint witness blocks W_b of MIN over independent legal full or local left/right assignments of sum_(J∈W_b) accepted nonnegative costs has its EVERY term identically ZERO whenever the union of original left points in each W_b has size <= B(s), at empty original-left prefix.

    L_block(S)=0; L_block(GF5 necessary numerator)=0,

for EVERY s=2^h and all right constraints. This kills not only C17's per-exact-left-support local minima but also bounded-SHARED-LEFT cluster minima that tie arbitrarily many distinct left-support signatures inside blocks of size <= B(s).

**Do not misinterpret:** the same physical left alpha need NOT work for different blocks. These may overlap in original factor points yet choose INCOMPATIBLE images when minimized separately. The theorem neither constructs one legal global f,g with zero S nor disproves issue #230 Branch A. It only proves that local blocks of sub-B(s) total named-left support are too small to exclude the TWO-ANCHOR sabotage.

## 3. Why two anchors are the precise elementary cover obstruction

One-anchor C18 had a physical degree=2 cap versus six repeated edge occurrences. Two-anchor C19 has combined physical degree <=4 but six edge occurrences. Three anchors would allow combined degree <=6, so the strict counting contradiction ceases automatically. This does not assert that alternative three-anchor obstructions are impossible, but explains why the elementary argument stops at two.

## 4. Independent executable scope and genuine original W32 controls

- Source: research/hyp105_g5e2b3e1c19_two_anchor_support.py
- Tests: research/test_hyp105_g5e2b3e1c19_two_anchor_support.py
- GitHub-hosted contract: .github/workflows/hyp105-c19-contract.yml

The source computes the exact integer all-h V,a,t,B(s) gate, deterministically finds a maximum occupied physical two-anchor cover using ACTUAL occupied pair-edge IDs (not arbitrary edge-ID permutations), validates distinct pair labels, and produces injective labels for the named left block.

Independent finite evidence: s=2 full K6 has a 9-edge two-anchor cover; s=4 V=85 and K14 has six missing physical edges, with several adversarial missing-edge placements including stars and disjoint matchings; every case has >=23-edge two-anchor cover. Synthetic six ORIGINAL incidence sets of various endpoint multiplicity types independently check the degree-sum contradiction.

**Stronger real W32 falsifier:** choose nine ORIGINAL GQ left points containing the left image of an actual full physical K6 six-cycle. Under the historical genuine W32 pair labels there are strictly positive original left 2factor source candidates supported entirely on those nine named original points. Reassign ALL nine original points at once into the nine occupied physical double-star edges, and complete the remaining six ORIGINAL point labels injectively. The independent preexisting 62,370-candidate source enumerator must then find EXACTLY ZERO accepted left-2factor sixsets supported entirely on that nine-point block. This directly challenges the claimed joint suppression on actual original GQ incidences, not just a toy sixset.

All-h arithmetic is proved symbolically for ALL h. Passing finite tests only validates implementation and examples; it does not supply missing asymptotic evidence.

## 5. Research decision and next allowed direction

The new obstruction forces ANY independently minimized left-coupled source block intended to give a **positive universal root floor** to include > B(s)=Theta(s^(3/2)) distinct named original LEFT points, OR impose genuine cross-block global left-image consistency so independently sabotaging blocks is no longer legal. Repeatedly adding pairwise/quartet witness couplings whose union support remains <= B(s) is mathematically incapable of closing issue #230 Branch A.

Next C20 should use shared-original-left overlap consistency across a growing connected support hypergraph, dual covering constraints or a global weighted cycle/packing inequality. Design C20 explicitly around the two-anchor counterconfiguration rather than brute-force W32 factorial maps. Do NOT claim a positive full R3, global 15!² W32 optimum, an ASET exponent, or a real all-h small-S family.

## 6. CI integration

Dedicated C19 Contract and Research on exact PR HEAD must both succeed. The existing monolithic ten-minute full Research CI is known to cancel; [parallel #306](https://github.com/definitely-stable/Mathlab/pull/306) is separately confirmed hosted SUCCESS but has not been merged into the C19 ancestry. Do not transfer CI acceptance between different commit SHAs and do not merge the scientific chain out of order.
