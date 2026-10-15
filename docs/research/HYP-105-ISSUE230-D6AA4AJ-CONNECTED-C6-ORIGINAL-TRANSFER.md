# HYP-105 / issue #230 — AA4-AJ: exact genuine-original connected-C6 source/Hall transfer

**Research-only, strict child of [AA4-AI PR #519](https://github.com/definitely-stable/Mathlab/pull/519), pinned parent SHA \`fc82262efb3dc4da306bed482b71d93540f2bdb1\`.** No Branch A all-f,g \(S_s=\Omega(s^6)\), no infinite globally injected counterfamily, no full R3/ASET exponent result. Distinguish pre-Hall physical occupancy from actual acceptance of six DISTINCT original incidence IDs. This work explicitly fixes the incomplete cross-bridge-only argument: a connected physical C6 also has a family in which the two auxiliary vertices share an edge.

## 1. Exact pinned physical-C6 taxonomy (all h, all K_a alphabets)

Fix two real distinct opposite original factors l0,l1 from two source flags through a **real** original doubled source root p, and two distinct physically disjoint globally injected images \`g(l0)=uv\`, \`g(l1)=wx\`. Denote their four distinct physical endpoints by u,v,w,x; let y,z be two distinct physical auxiliary coordinates outside these endpoints.

A simple, connected, six-vertex, six-edge 2-factor H containing the two pinned edges is in exactly ONE of:

- **2 crossed two-spoke templates (NO yz edge).** All four remaining edges join y/z to the pinned four endpoints; thus y connects two endpoints and z connects the other two. The endpoint pairing must CROSS the pinned edges, i.e. exactly \`((u,w),(v,x))\` or \`((u,x),(v,w))\`. For each such matching, let y connect the first canonical endpoint pair and z the second; every valid ordered (y,z) gives a DISTINCT connected C6. Pairing \`((u,v),(w,x))\` instead produces two disjoint physical triangles, not C6. Raw complete-K_a count = 2(a-4)(a-5).
- **4 cross-link templates (WITH yz edge).** There is exactly one additional edge h between an endpoint of uv and an endpoint of wx, four choices. If the two remaining endpoints are r0,r1, the remaining three edges form the path r0-y-z-r1. The ordered orientation is uniquely determined by its attachment to r0/r1, and every valid ordered (y,z) gives a DISTINCT connected C6. Raw complete-K_a count = 4(a-4)(a-5).

No other possibility: y,z each have target degree two, the four pinned endpoints degree one after pinned edges; if yz is absent the four free degree slots must be supplied by four spoke edges, otherwise the edge yz consumes two auxiliary free slots and leaves one endpoint-link and two spokes. Each template is physically edge-distinct and unique. The total **6(a-4)(a-5)** agrees with existing AA4-AI exact all-physical-twofactor count. The taxonomy is tested independently for EVERY disjoint pinned pair in complete K6,K7,K8, by classifying actual literal complete physical H from the prior separate AA4-AD enumerator and checking uniqueness of H. This taxonomy concerns opposite **physical A** when its two pinned edges are physically DISJOINT; adjacent pinned edges and same-triangle physical A are separate sectors, not claimed to be covered.

## 2. NEW AA4-AJ1: all-h exact six-channel TRUE ORIGINAL crossed-spoke Hall formula

Fix four distinct REAL additional first-type source factors (q0,q1,q2,q3), inverse-mapped from an ACTUAL first-side occupied physical C4 under the ONE globally shared opposite typed map. Each of the two crossed endpoint templates (\`P=(r0,r1)\`,\`Q=(t0,t1)\`) has physical two-spoke auxiliary edge columns

    A_y = [g^-1(r0 y), g^-1(r1 y)],
    B_z = [g^-1(t0 z), g^-1(t1 z)]

ONLY if all four physical edges exist in im(g). Let \`Y_S\` contain those y where the *TRUE ORIGINAL* 2×2 rook permanent of rows q_S against columns A_y equals 1; let \`Z_{Sbar}\` contain those z where the permanent of rows q_Sbar against columns B_z equals 1. The classical source W(3,s) girth 8 forbids an original K_2,2, so each local 2×2 permanent is at most 1 for two distinct real source point and line factors (also for the type-dual orientation).

For that physical crossed pairing, the exact number of accepted six-DISTINCT-incidence-ID original Q is

    T_cross(P,Q) = sum_{S⊂{0,1,2,3}, |S|=2}
                       (|Y_S|*|Z_Sbar| - |Y_S ∩ Z_Sbar|).

The term y=z is excluded because an accepted A physical six-coordinate 2-factor needs SIX different actual physical coordinates. Sum over precisely the two crossed endpoint matchings for the true original connected C6 no-yz component. This is the AA4-AH rank-six Laplace permanent contraction applied to the CROSS endpoint attachment rather than the original pinned-edge-local triangle pattern. There are exactly 2×6=12 nonnegative channel summands and no assumption of independently drawn physical maps per Q.

For each fixed original C4, constructing these O(1) row-pair site sets costs O(a) and 2×6 exact source adjacency checks per site.

## 3. NEW AA4-AJ2: actual incidence-anchored TRUE ORIGINAL internal-link Hall transfer

Fix one of four physically possible cross-link edges \`h=pq\` between the two pinned opposite physical edges. If h is absent from global im(g), this template contributes nothing. Let r0,r1 denote the unused endpoints of the two pinned edges.

Every connected physical C6 completion of this template has opposite physical free factors with physical edges

    [h, r0-y, y-z, z-r1],

where y≠z and y,z are outside the four pinned endpoints and **all four** opposite physical pair images are globally occupied. For every accepted original 4-rook permutation, the *unique* original free source singleton row q_k matched to the physical edge yz must be genuinely incident to \`g^-1(yz)\` in the fixed TRUE ORIGINAL W(3,s). Therefore the actual yz edge can be taken from precisely the globally mapped source-neighbor set \`g(N(q_k))\`, which contains s+1 ORIGINAL opposite source factors per q_k.

An exact, no-probability algorithm enumerates:

- the four physical cross-link templates h;
- the four choices of which genuine ORIGINAL free source row q_k receives the genuine incidence yz;
- at most (s+1) actual ORIGINAL incident opposite factor IDs in N(q_k), and the two orientations (y,z);
- the 3! matchings of the other three genuine rows to the actual opposite original factor columns \`[g^-1(h),g^-1(r0y),g^-1(zr1)]\`.

It accepts only genuine source adjacency for all three remaining rows. Each accepted ORIGINAL six-ID Q occurs exactly once (the unique true original selected yz row k and physical edge orientation are determined by its six actual opposite factor images). If there are two original perfect matchings on the same physical H, source GQ girth eight forces a genuine induced source C8; BOTH matches are counted, in agreement with earlier AA4-AE \`T=F_Hall+C8\`. Conversely every true source matching in this family is enumerated. This is an exact **all-h original Hall transfer**, not a positive uniform Hall-density assertion.

The internal-link matching enumeration has O(4×4×2×6(s+1)) = O(s+1) actual adjacency checks for fixed first-side original C4. Source independent original f,g are NOT assumed random; they remain the same global physical maps across every term.

**Physical occupation without O(a²) pair iteration:** for one link h let

    Y={y outside pinned endpoints : r0-y is occupied}
    Z={z outside pinned endpoints : r1-z is occupied}
    M = physical unordered missing-edge pairs from K_a\im(g), m=|M|=C(a,2)-V.

Then the EXACT number of occupied internal-link cycles using h is

    |Y| |Z| - |Y∩Z|
      - sum_{ {i,j}∈M } (1_{i∈Y,j∈Z} + 1_{j∈Y,i∈Z}).

The first subtraction forbids y=z; the last subtracts ordered (y,z) whose needed yz physical edge does not belong to the single global physical injection g. For a fixed global g its m missing pairs can be precomputed once in O(a²) and cached; subsequent individual source-C4 counts take O(a+m). Minimal palette mapping guarantees m<=a-2; the source-geometric incidence anchored work is O(s), so total per specified anchored source C4 is O(a+m+s) AFTER amortizing the one-time physical complement preparation and not including original source-C4 enumeration.

## 4. NEW AA4-AJ3: all-h **UPPER** bound on TRUE accepted original C6 for a fixed cohort (not lower)

The genuine original GQ source degree d=s+1 and complete global injection force

    T_cross_spoke(p,pins,C4;f,g) <= 48 d^2
    T_internal_link(p,pins,C4;f,g) <= 192 d,
    T_connected_C6 <= 48(s+1)^2+192(s+1).

Reason for first term: for each of the two crossed endpoint matchings and six possible source two-row assignments S, a site y∈Y_S requires the first physical edge of y's spoke pair to be inverse-mapped to an original neighbor of one of the TWO source rows in S. The global map is injective, so each true original row supplies at most d such physical edges, hence |Y_S|<=2d and similarly |Z_Sbar|<=2d. Drop the nonnegative diagonal exclusion: 2×6×(2d)^2=48d². Second term: four cross-link choices, four possible ORIGINAL source rows receiving yz, ≤d actual original incidence IDs per row, two yz orientations, and at most 6 remaining permutations: 4×4×d×2×6=192d. Neither bound requires random physical labels, global surjectivity or an assumption of factor independence. They may not be sharp and are NOT accepted-Q lower bounds.

This separates the **very large physical pre-Hall index mass** from the much smaller *possible* source-compatible Hall mass per rooted source cohort. A physical lower bound \`P_C6_preHall>=s^14/256\` from AA4-AI CANNOT be promoted to any actual \(T_C6\) positive lower by mere physical capacity arithmetic.

## 5. Independent falsification plan

A. For all disjoint pinned pairs in complete K6/K7/K8, literally enumerate all C6 physical 2factors containing them using pre-existing independent AA4-AD oracle. Every H has exactly one non-yz or yz physical template; per pinned pair counts are **2(a-4)(a-5)** and **4(a-4)(a-5)**. Detect duplicate templates and missing patterns.

B. True ORIGINAL W(3,2): five actual full globally bijective physical mappings including the AA4-AI dual split-zero witness, lex, reverse, S68 and S72; BOTH typed source sides, ALL 15 original roots, 3 pairs of different genuine root incidences per root, ALL 3 physical genuine first-side C4s per root. For every one of these original cohorts, compare new decomposed EXACT accepted connected C6 source-Hall counts to an **independent** literal original four-row × actual four opposite-factor permutation over physically complete H. Compare the sum with pre-existing full original W32 A-sector accepted connected C6 census. The earlier AA4-AI FULL connected C6 count includes adjacent physical pins: **40 B/A** and **58 A/B** accepted original C6 Q, against **1,062/1,188** occupied physical C6 H. This AA4-AJ theorem is strictly limited to DISJOINT pinned physical pairs and its new exact counts are **17 B/A**, **41 A/B** genuine original accepted six-ID Q, against **504/756** occupied physical disjoint-pinned H. The remainder is **23/17** accepted actual original adjacent-pinned C6 Q, against **558/432** physically occupied adjacent-pinned H. NEVER compare AJ disjoint-only counts directly to AI full connected sector as if their domains coincide.

C. True ORIGINAL W(3,4): actual symplectic GF(4) point-line incidence, complete globally injective lex/random physical maps with m=6 physical holes in K14, both source orientations, several true source roots, actual flag pairs and real physically occupied first-side C4. Compare each individual decomposed true Hall count with separate AA4-AI \`single_original_A_sector_permanent\` as well as an independent literal H×all 24 genuine original four-column matchings.

D. True original source symplectic automorphism and two independent physical coordinate permutations must preserve exact full C6 accepted 40/58. Reject malformed noninjective source, fake C4s, invalid physical 2factors and non-powers of two. Integer upper bounds evaluated for h up to 25 with no finite fake W(3,2^h) construction.

Four GitHub-hosted Jobs on EXACT final PR HEAD; independently compare to earlier AA4-AI; ensure INDEX, Proof Audit, and Full Research statuses distinguished from proof acceptance.

## 5.1 Exact genuine W(3,2) split of CONNECTED C6 by physical pin relation

The genuine globally bijective W(3,2) AA4-AI counterexample is an important independent guard. For one fixed pair of complete global point/line physical maps, summing all actual original point and line roots, actual flag pairs and first-side occupied C4s gives:

| True ORIGINAL connected-C6 cohort | Point-B / Line-A | Line-B / Point-A |
|---|---:|---:|
| **Physical disjoint-pins H** counted by THIS AJ theorem | **504** | **756** |
| **Original accepted disjoint-pins Q** counted by THIS AJ theorem | **17** | **41** |
| Physical adjacent-pins H — NOT counted by this AJ theorem | 558 | 432 |
| Original accepted adjacent-pins Q — NOT counted by this AJ theorem | 23 | 17 |
| All physical connected-C6 H, independently established by AI | **1,062** | **1,188** |
| All original accepted connected-C6 Q, independently established by AI | **40** | **58** |

All table cells are indexed original source cohort counts with six distinct genuine original incidence IDs in selected Q. The 40/58 FULL connected-sector figure is NOT a theorem of the disjoint-pinned AJ transfer alone. The difference is a well-posed AA4-AK adjacent-pins source transfer and must NOT be implicitly assigned to either of the two AJ disjoint templates. The exact 17/41 and 504/756 disjoint totals were independently checked by the old AA4-AD complete physical A-twofactor H enumeration crossed with all source 4-rook perfect matchings, plus invariance under a genuine source symplectic automorphism and two independent physical coordinate relabelings.

## 5.2 AA4-AJ4: universal **upper** O(1/s) good-root Hall dilution

There is a new precise asymptotic all-f,g statement that is **not** an all-global lower. Fix s=2^h, h>=19 and ANY complete globally injected genuine original pair f,g. Fix ONE of the source intersecting line pairs selected by AA4-AG as *good*: its two globally labeled opposite physical edges are disjoint, and each of their four physical endpoints has missing-edge degree less than a/16 in the one globally fixed opposite physical map g. Fix ANY actual first-side physically occupied complementary C4 representing four distinct genuine original source singleton factors.

AA4-AI established at least a²/4 **globally OCCUPIED physical connected C6** completions of this actual pinned pair (using the single cross-bridge physical cycle \`u-v-y-w-x-z-u\`). The new AA4-AJ3 degree bound applies to **all** disjoint-pinned connected C6 source-Hall completions with the same root/C4 pair, not merely those physical bridge cycles. Therefore for this actual globally fixed rooted source cohort,

    accepted_original_Q_connected_C6 / occupied_physical_H_connected_C6
         <= [48(s+1)²+192(s+1)] / (a²/4)
         = 4[48(s+1)²+192(s+1)]/a².

The ratio counts source SIX-ID accepted Q with actual GQ matching multiplicity (0/1/2) over distinct occupied physical completion H. The *Hall-positive physical H fraction* is also <= this expression since each Hall-positive H contributes at least one selected original Q. For minimal a with C(a,2)>=V=(s+1)(s²+1), a²=(2+o(1))s³, hence

    limsup_(s->infinity, s=2^h)  s *
        [accepted_original_Q_connected_C6 / occupied_physical_H_connected_C6]
    <= 96.

In particular this ratio is O(1/s) for **every** complete f,g and every AA4-AG good pinned source cohort at h>=19. The exact rational bound is implemented in \`good_original_rootpair_hall_dilution_upper(s)\` and tested at powers h=19,20,22,26 with exact integers, no floating point.

This explains why even an extremely large universal PHYSICAL pre-Hall mass can coexist with source-Hall failures. **The estimate is an UPPER bound on Hall success density, never a LOWER bound, and does not establish or refute original issue #230 Branch A.** It neither produces an all-h globally injected counterfamily nor proves global S=o(s^6); many distinct source root/C4 cohorts can compensate despite sparse genuine Hall successes in each.

## 6. Integration and future theorem gate

Draft PR atop #519. The parent #519 is itself stacked on #517, #516, #514 and earlier. Do NOT merge or edit main, do NOT mark accepted in formal RCP JSON or generated research catalogs without separate independent mathematical review and all required final-HEAD CI. Original issue #230 stays OPEN.

**Next AA4-AK allowed theorem work:** extend the exact degree-anchored source transfer to PHYSICALLY ADJACENT pinned edges and same-triangle completion, then analyze an all-global-Hall-positive lower over all physical A modes plus the remaining GF5/D6 classes. A general \`C6 source acceptance >= c s^6\` is neither proved nor implied by the new transfer. Search also for genuine all-global correlation constraints or infinite counterfamily; finite original model evidence is not a Branch B certificate.
