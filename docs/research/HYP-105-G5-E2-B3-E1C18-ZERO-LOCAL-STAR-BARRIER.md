# HYP-105 B3.2-E1-C18 — all-h star obstruction to the C17 pure-local lower

Date: 2026-10-11. Parent theorem issue #230, scientific stack C16 #305 -> C17 #308 -> C18. This is a **negative all-h theorem about a PARTICULAR RELAXATION**, not a construction of true maps f,g with small S. All accepted GF5 weights are nonnegative and vanish when the left physical six-projection fails its 2-factor condition.

## 1. Target model and precise universal quantifiers

Let s=2^h with h>=1. W(3,s) has exactly V=(s+1)(s²+1) original points and V original lines. Let a be the smallest integer with binom(a,2)>=V. The actual occupied physical pair-edge alphabet F_L is ANY size-V subset of the unordered edges of K_a, as determined by ANY complete injective original-point physical labeling f. There is no assumption of random labeling or coordinate/Sp(4,s) symmetry. Right occupied pair alphabet and right original injection may be arbitrary.

Fix **NO ORIGINAL LEFT POINT PINS**. Arbitrary ORIGINAL right-line pins g0 are allowed. The C17 pure-local certificate partitions distinct original six-incidence J by its exact touched ORIGINAL LEFT set U_J and touched unpinned ORIGINAL RIGHT set M_J, and minimizes each cluster's nonnegative accepted seven indicator or GF5 necessary numerator over local injective assignments of all left points in U_J and unpinned right lines M_J independently from the other clusters.

**Theorem C18.** For EVERY h>=1, EVERY allowed size-V occupied left pair-edge image F_L and EVERY partial genuine right map g0, the C17 pure-local L_poly on the empty LEFT pin set is EXACTLY ZERO, both for the seven-family S indicator and separately for the accepted GF5 necessary numerator. The zero holds irrespective of W(3,s) original incidence correlations or the right map, because the relaxation independently allows an incompatible left-label injection for each named U_J cluster.

## 2. Independent elementary two-part proof

**(A) Five-edge star always exists.** The physical occupied graph (a coordinates, V occupied pair-edges) has average degree 2V/a. For s=2 we have V=15, a=6 and 2V=30>4a=24. For s>=4, minimality gives a>=7 and

    V > binom(a-1,2) > 2a,

where the last strict inequality holds for every a>=7 (at a=7: 15>14, difference strictly increases). Thus in ALL cases V>2a. By handshaking sum degrees=2V>4a, so at least one coordinate x has deg_F(x)>=5. In addition V>=15 ensures an occupied edge distinct from any chosen five star edges.

**(B) A common killing LEFT assignment for an ENTIRE signature cluster.** Take ANY original six-incidence set J and let U be its set of k distinct ORIGINAL left endpoints, with 1<=k<=6 (each appears at least once). This U is the SAME named left support for EVERY J in its signature cluster, since no original left points are pinned.

- If k<=5, map all k distinct original points injectively to k distinct occupied pair-edges incident to the same x. Every one of J's six original incidences then contributes one occurrence of x in the physical LEFT projection. Hence the degree of x in that six-edge multigraph is EXACTLY 6.
- If k=6, map any five named original points to five distinct pair-edges incident to x, and the sixth point to any other unused occupied pair-edge. Each original left point appears exactly once among J's six different incidences. Therefore x has degree at least FIVE.

Both cases violate the NECESSARY accepted physical-left two-factor degree condition that each used coordinate has degree precisely two. Therefore EVERY original J in the whole fixed-left-support cluster has accepted seven indicator ZERO, and accepted GF5 necessary numerator ZERO, for this SINGLE local injection, regardless of which valid local right injection is chosen.

Every local injection of size k<=6 extends to a complete original-to-occupied-pair bijection; however **DIFFERENT CLUSTERS MAY REQUIRE INCOMPATIBLE LEFT ASSIGNMENTS**, and C18 does NOT assert that all clusters can be killed simultaneously by one genuine global f. It proves that each cluster's nonnegative independent minimum is exactly zero. Summing gives L_poly=0. This proof also applies to ANY nonnegative sixset family whose acceptance implies physical-left six-projection degree<=2; it uses no special GQ symmetry.

## 3. What is NOT proved

C18 is **NOT** a pair (f_s,g_s) with S_s(f_s,g_s)=0; NOT #230 counterexample Branch B; NOT a full GF5 R3 upper; NOT a restricted positive Omega(s^6) theorem; NOT a new ASET exponent. It destroys the **empty-left-pin pure-local relaxation** as a route to a positive universal S lower. C17's extra C15 common-right frozen-left term is also ZERO with no LEFT pins (no original sixset has empty left support), so it cannot save this particular root certificate. C16's global left-compatibility or nontrivial pinned-left constraints can still be positive and are NOT refuted by this theorem. The physical occupied F may have missing pair-edges; the proof uses only V and a and survives every allowed F.

## 4. Independent executable and hosted falsifiers

Module: research/hyp105_g5e2b3e1c18_zero_star_barrier.py
Tests: research/test_hyp105_g5e2b3e1c18_zero_star_barrier.py
Contract: .github/workflows/hyp105-c18-contract.yml

- Exact integer a,V and star-degree arithmetic for s=2,4,8,16,32,64. Analytic proof above covers ALL h and does not rely on sampling.
- All k=1..6 synthetic six-incidence original-left multiplicity distributions tested with a star-local injection that makes the physical coordinate degree 5 or 6.
- Occupancy adversaries for s=4, a=14 and 85 of 91 K14 pair-edges, several distinct missing-edge patterns. Handshaking proof covers arbitrary missing patterns.
- Independent **actual symplectic W(3,2) ORIGINAL incidence** controls from all three accepted left source A/B/C families; validates the star assignment also fails the pre-existing physical projection classifier.
- Invalid s, duplicate original local support, too few occupied physical pair-edges and wrong number of original six incidences must fail closed.
- Both standalone executable report and independent unit tests required to pass dedicated GitHub-hosted contract, followed by full Research on exact PR HEAD.

## 5. C19 next allowed scientific direction

Stop asking whether C17 pure independent LOCAL cell minima alone can prove global Omega(s^6); C18 gives an exact all-h NO. A productive future inequality MUST enforce one physically consistent left assignment across multiple distinct U source clusters (e.g. bounded overlap/hypergraph dual over shared original points, mandatory left pin geometry, or jointly coupled left-right structural cycles). Such a coupling must defeat the per-cluster star sabotage in a falsifiable all-h theorem or exhibit an explicit global counterexample. C16 finite shared-left/groupwise-right is a valid starting control, but computing factorial full joint minima on W32 is not a scalable proof by itself.
