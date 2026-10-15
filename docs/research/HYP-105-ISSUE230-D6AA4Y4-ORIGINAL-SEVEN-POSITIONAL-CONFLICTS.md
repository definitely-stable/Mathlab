# HYP-105 / issue #230 — D6-AA4-Y4: same-ORIGINAL-Q seven-class signed positional collisions and connected AA capacity

**Classification:** new rigorous ALL-h connected original-AA physical source-pattern capacity lemma, exact immutable-tag sign-quadrant decomposition (not a universal positivity theorem), and independently tested complete true-original finite W(3,2) seven-class collision matrices. Strict research-only Draft child of exact 4/4-green Y3 PR #501, pinned parent HEAD `208dd8d20de14b3bbbe5516841df7660eb608d96`. Root #230 A/B/C remains OPEN. No edits to main.

## 1. Scientific obstacle: Y3 mixed source-star bound is class-blind

Y2 proves that for every quadruple of complete globally injected true-original typed maps f0,f1,g0,g1 on genuine W(3,s), s=2^h>=2, the accepted positive original seven-class counts admit a common same-Q binary feature Gram representation. Each mode is indexed by (actual six-DISTINCT-original-incidence-ID Q, immutable source seven-GF5 tag, positional mode). Non-AA has exactly one scalar mode per source-tagged Q; original source AA has 60 CONNECTED positional C6 modes, not the ten disconnected pairs of triangles. Signed source gradients lie in {-1,0,+1}. The four nonnegative quadrant counts per tag t are F_t^{++},F_t^{--},H_t^{+-},H_t^{-+}, and EXACTLY:

    Delta C_t = F_t^{++}+F_t^{--}-H_t^{+-}-H_t^{-+}.
    Delta S = SUM_t Delta C_t,
    Delta W = SUM_t w_t Delta C_t.

Here W is ONLY the selected historical 51-palette GF5 positive seven-class numerator, with certified weights D6=5643; B-left/A-right=45600; A-left/B-right=45600; C/A=43320; C/B=49050; B/B-overlap=51750; B/B-disjoint=45010. The same six actual original incidences Q and the same one full global point map and one full global line map are used at each corner; no physical-label resampling per Q.

Y3 bounded the TOTAL harmful modes H by original source-star physical pattern capacities, strengthened to O(s^11) for all correlated point-line original two-factor transpositions and to O(s^(21/2)) when no marked point-line source incidence exists. This remains coarse since it counts disconnected AA physical factors and non-AA-ineligible source shapes in the D6 capacity.

## 2. NEW universal connected AA/C6 physical root counts

Set V=(s+1)(s²+1), d=s+1, a=min{n:C(n,2)>=V}, K=C(a,2). Fix an actual original point or line source factor mapped by any complete globally injected physical pair map to one physical K_a edge e.

For an arbitrary given set of SIX physical coordinates, there are 60 undirected Hamiltonian C6 edge sets and ten disconnected two-triangle 2-factors. The 60 connected cycles have exactly 6 physical edges per cycle and the complete K6 has 15 physical edges. Therefore exactly 60*6/15=24 connected C6 patterns contain prescribed e, rather than 28 from the full 70 2-factors. For TWO marked distinct physical edges in a K6:

- If they are adjacent (share one physical coordinate), exactly SIX connected C6 contain both. This follows by contracting a prescribed consecutive two-edge path in the Hamiltonian cycle (or by 60*6/60=6 double counting the 60 adjacent physical-edge pairs and 6 adjacent edge pairs in every C6).
- If they are disjoint, exactly TWELVE connected C6 contain both. Every C6 has 9 disjoint unordered edge pairs and K6 has 45 such pairs, yielding 60*9/45=12.

For complete K_a, choose the remaining coordinates first, obtaining exact connected physical pattern counts:

    P_C6(e)      = 24 C(a-2,4)
    P_C6(e,e')   = 6 C(a-3,3), when adjacent,
    P_C6(e,e')   = 12 C(a-4,2), when disjoint.

Every chosen set of six distinct physical edges represents six different original globally injected source factors, and each original factor has exactly d original incident flags. Thus the number of TRUE ORIGINAL Q with connected physical half, containing a particular source factor, is at most

    U_conn,star = 24 C(a-2,4) d^6,

and for two prescribed different source factors with adjacent or disjoint physical images, their connected physical Q union is at most

    U_conn,pair(rel) = 2 U_conn,star - P_C6(e,e';rel) d^6.

These bounds are attained at true W(3,2) because every source half maps bijectively onto all physical K6 edges. Note they are HALF-PROJECTION bounds; true historical D6 also requires immutable ORIGINAL source-AA on the OPPOSITE side and equality of connected positional six-incidence C6 modes. Therefore the inequalities remain safe and can overcount real positive D6.

## 3. NEW class-specific same-Q harmful-capacity corollary

For a genuine ORIGINAL source Q accepted by the historical seven-positive GF5 classifier, its source multiplicity type on each typed side is immutable across all physical map changes. Specifically, D6 has connected A on both sides; B-left/A-right has B on original points and A on original lines; A-left/B-right reverses those; C/A pools (A,C) and (C,A); C/B pools (B,C) and (C,B); each B/B tag has B on both original sides. A non-AA source A half may use any 2-regular physical 2-factor, including disconnected 2C3; ONLY D6 demands connected C6.

Let U_pair,A/B/C(rel) be Y3's COMPLETE physical adjacent/disjoint two-marked-source half capacities, and U_pair,connA(rel) the just-proven connected C6 half capacity. For a class t with corresponding allowed point and line physical half types T_P(t),T_L(t), a genuine original signed mode gradient is supported on source Q touching at least one affected original source factor and has at most two nonzero signed entries per such Q (one old mode and one new mode). Consequently, in every globally complete original source transposition quadruple:

    H_t <= min(E^P_t,E^L_t)
        <= 2 min( SUM_{type in T_P(t)} U_pair,type(P relation),
                 SUM_{type in T_L(t)} U_pair,type(L relation) ).

The sum for C/A or C/B safely pools both possible original source orientations, which are mutually exclusive on each Q. No class-conditional physical position independence is assumed.

### Connected D6 improvement with true original GQ crossed incidences

For a true original (p,ell) flag with p an affected source point and ell an affected source line, the one-source connected-AA physical projection cap with this exact flag fixed is `24 C(a-2,4) d^5`. If p is NOT the point endpoint q of a genuine flag (q,ell), but q is some other actual original neighbor of ell, the two-physical-source-edge connected-AA cap with that q flag pinned is `6 C(a-3,3)d^5` or `12 C(a-4,2)d^5`, depending on the physical adjacency of f(p) and f(q).

For two marked source points and two marked source lines, let m be the actual original 2×2 source incidence count. Genuine GQ girth eight forbids m=4, so 0<=m<=3. The all-h crossed connected-AA source capacity is:

    U_cross,connAA(m) = m*24 C(a-2,4)d^5
                   + (4d-m)*max(6 C(a-3,3),12 C(a-4,2))d^5.

Thus for original historical D6 harmful opposite-sign shared positional modes:

    H_D6 <= 2 min(U_conn,pair(P), U_conn,pair(L), U_cross,connAA(m)).

This is strictly no worse than Y3's ALL-seven untagged crossed bound, and often smaller due to discarding disconnected A 2-factors. Its asymptotic order remains at most O(s^11), or O(s^(21/2)) for m=0; it does NOT by itself prove root S_s=Omega(s^6). The quantitative obstruction still requires jointly eliminating impossible true original forest cells and physical C6 alignment modes on the SAME Q.

## 4. Independent entire 7×4×11,236 signed original W32 census

New C++20 source engine reconstructs original AA4-Y2 six-ID physically projected feature-mode sets, separately and globally for all 106 source point label variants and all 106 source line label variants. Its *new* independent seven-tag signed-mode sort/merge counts four quadrants (++),(--),(+-),(-+) for each tag, preserving the exact ORIGINAL Q and AA connected positional C6 mode key. It emits a machine-readable 11,236-line TSV (28 unsigned quadrant counters plus two source variant IDs).

Python independently regenerates the entire exact historical original GF5 seven-class 106×106 matrix via the earlier AA4-Y-CYC 62,370-by-62,370 original six-ID two-sided join; also reruns the separate AA4-Y2 aggregated signed source mode engine (11,236×4) for direct independent total quadrant reconciliation. For each of 11,236 global pairs and all SEVEN classes it validates:

    F_t^{++}+F_t^{--}-H_t^{+-}-H_t^{-+}
    == C_t(i,j)-C_t(i,0)-C_t(0,j)+C_t(0,0).

It compares all 11,236 source-aggregated quadrant vectors to the separately implemented Y2 native engine, all 11,236 historical selected 51-palette weighted mixed changes, and true-original D6 connected all-h harmful caps for EACH nontrivial 105×105 globally coherent paired transposition. Seven-class maximum harmful witnesses undergo a separate complete AA4-Q independent-history true-original six-ID census. The summary records for EACH immutable historical GF5 tag: signed-positive/negative counts, total H_t/F_t, largest true-original harmful mode count, and exact original point/line source swap witnesses. These finite statistics identify research bottlenecks; they are NOT all-h exponent proofs.

Independent Python physical brute-force over all connected K6/K7 six-edge two-factors verifies the 24,6,12 constants. Independently enumerate all actual ORIGINAL 62,370 half Q for both point and line sides of S68/S72 and count physically connected A modes, including exact W32 60*3^6=43,740 connected Q per side and 24*3^6=17,496 containing each actual original source factor. Fail closed on malformed global injections, source C/C impossible by GQ girth eight, missing original six-Q, inconsistent quadrant tags or any schema mismatch.

## 5. Reproducibility / acceptance

Run the GitHub-hosted workflow `.github/workflows/hyp105-issue230-d6aa4y4-original-positional-class-conflicts.yml` (Python 3.12, g++ C++20, no external dependencies). It runs independent mathematical unit tests and separate S68/S72 complete 11,236-grid historical/tags/aggregates; archives signed 28-column TSV, original seven GF5 matrix and JSON per scheme with 90-day retention. Commands from repository root:

    python -m unittest discover -s research -p 'test_hyp105_issue230_d6aa4y4_original_seven_positional_capacity.py' -v
    g++ -std=c++20 -O3 -o /tmp/y4 research/hyp105_issue230_d6aa4y4_original_seven_signed_quadrants.cpp
    g++ -std=c++20 -O3 -o /tmp/y2 research/hyp105_issue230_d6aa4y2_original_signed_conflicts.cpp
    g++ -std=c++20 -O3 -o /tmp/y research/hyp105_issue230_d6aa4ycyc_bilateral_original_join.cpp
    python research/hyp105_issue230_d6aa4y4_original_seven_positional_capacity.py --scheme S68 --original /tmp/y --tagged /tmp/y4 --aggregate /tmp/y2

Root #230 Branch A (universal deterministic six-positive motifs), Branch B (infinite correlated o(s^6) family) and Branch C (model-equivalent restricted reduction) all remain OPEN. A finite exact seven-class positional collision census does not justify extending a W32 observation to ALL s. Before integration require exact-head Dedicated, INDEX, Proof Audit, Full Research PASS and independent mathematical referee. Leave this PR Draft; no direct main changes. Next research gate: combine true-original forest occupancy and positional cycle collision capacities, avoiding classblind source-star products.