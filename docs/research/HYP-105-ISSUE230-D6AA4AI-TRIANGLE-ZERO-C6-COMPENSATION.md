# HYP-105 / issue #230 — AA4-AI: true-original global zero of split triangles, exact C6 compensation

**Research-only, stacked child of [AA4-AH PR #517](https://github.com/definitely-stable/Mathlab/pull/517), pinned parent HEAD \`09114a7be997207537c5bf75d318dc4fe61e362d\`.** All results preserve TRUE ORIGINAL W(3,2^h) point-line incidence IDs, full globally injective typed physical point map f and line map g, minimal K_a physical alphabets, and exactly six distinct real original incidence IDs Q. Nothing here proves issue #230 Branch A/B/C, full strict R3/ASET or an all-h counterexample to Branch A. Do not merge to main before independent proof review and complete CI.

## 1. Important correction: A has THREE physical sectors relative to two pinned opposite edges

AA4-AH's six-channel formula covers only the split-two-triangle sector, where pinned opposite physical images g(l0),g(l1) belong to **different** physical triangle components. The full six-physical-coordinate two-regular A pattern ALSO includes (i) two triangles with the two pinned opposite physical edges in the SAME triangle when those physical edges are adjacent, and (ii) one connected physical C6. Do not conflate the AH split subclass with the complete 70-mode physical A kernel.

For any two distinct actual physical K_a edges, with a>=6, write t equal to C(a-3,3) for adjacent pinned edges and (a-4)(a-5) for disjoint pinned edges. The following ALL-h EXACT physical pattern capacities apply BEFORE missing physical-edge occupancy and BEFORE original source Hall constraints:

| Pinned physical pair relation | Split triangles | Same-component triangles | Connected physical C6 | Total A |
|---|---:|---:|---:|---:|
| Adjacent | 0 | C(a-3,3) | 6 C(a-3,3) | 7 C(a-3,3) |
| Disjoint | (a-4)(a-5) | 0 | 6(a-4)(a-5) | 7(a-4)(a-5) |

Proof: In the adjacent case the first triangle is forced by the third edge closing the two pinned edges, the remaining triangle is on any triple of the a-3 unused physical coordinates; all remaining two-factors are connected C6. In the disjoint case the two triangles contain one pinned edge each and use two distinct auxiliary coordinates, giving (a-4)(a-5) ordered choices; the known ALL two-factor capacity 14*C(a-4,2)=7(a-4)(a-5) leaves six times as many connected C6. Equivalently, for adjacent pinned edges the known ALL count 7*C(a-3,3) leaves 6*C(a-3,3) connected C6. All physical edges of a chosen pattern must be globally occupied to inverse-map to actual original opposite factors.

**New exact TRUE ORIGINAL all-map transfer decomposition:** On any genuine physical B-source root, actual two flags, and occupied first-side C4, the previously proven exact acceptance identity \`T=sum_{H occupied} per(M_H)\` splits into disjoint exact nonnegative original 6-ID subcounts

    T_A_full = T_split_two_C3 + T_same_C3 + T_connected_C6.

Each physical H inverse-maps to FOUR distinct actual opposite source factors and its genuine original 4x4 incidence matrix has permanent 0,1,2. Each sector separately satisfies \`T_sector=F_Hall_sector+C8_sector\`. Neither the physical 1:6 capacity ratio nor the physical nonzero count implies any positive lower on the genuine original Hall-positive fraction.

## 2. AA4-AI1: a genuine finite W(3,2) TWO-ORIENTATION global counterexample to split-triangle positivity

Use the actual indexed symplectic W(3,2) geometry from \`hyp105_b1_symplectic.py\`, with 15 original point source factors, 15 line source factors, 45 actual point-line incidence IDs. Physical coordinates are 0..5 and the physical unordered-pair palette is the lexicographic \`list(combinations(range(6),2))\` (15 distinct pairs).

A concrete PAIR of globally complete, bijective, actual source factor maps, specified by the physical-palette INDEX of each original point and line factor:

    f_indices = (4,14,10,7,6,2,5,13,12,9,0,11,3,8,1)
    g_indices = (11,0,9,5,14,12,13,10,6,3,7,8,2,4,1)

**These are TWO fixed global permutations**, not newly drawn physical coordinates for different original six-sets. The finite source graph, its line order and real incidence ID order are unchanged. The functions \`zero_split_original_W32()\`, \`full_original_W32_sector_certificate()\` and \`independent_literal_original_W32_sector_census()\` reconstruct and check the actual model from first principles using two mutually independent acceptance algorithms:

1. For ALL 15 real original point roots (and dual line roots), ALL THREE pairs of actual distinct source flags per root, and ALL THREE occupied physical complement C4 per root, enumerate occupied full six-coordinate physical A 2-factors containing the two pinned real opposite physical images. Inverse-map all four remaining physical edges through the SAME global opposite typed map, compute the TRUE original GQ 4x4 four-rook permanent, classify physical A as split triangles, same triangles, or connected C6. There are 135 real B physical-C4 root+flag-pair cohorts per source orientation. No source quotient.
2. Independently enumerate actual four free SOURCE incidence flags \`(q_i,l_i)\` by Cartesian product of real GQ neighborhoods, remove the pinned two opposite source factors and discard all original factor collisions. This constructs six DISTINCT actual original source incidence IDs directly. Classify the resulting opposite physical A edges only if exactly six physical coordinates each have degree two and then independently traverse its physical connected components. Reject fake 5-coordinate degeneracies. Confirm exact per-sector equality with (1).

The independently obtained finite result is:

    T_split_B/A(f,g) = 0
    T_split_A/B(f,g) = 0.

The physical split triangle candidates are not vacuous; their complete physically occupied K6 counts are strictly positive, but ALL have zero actual original Hall transfer. This is a **genuine finite all-root two-orientation counterexample** to any proposed statement \`forall h>=1 forall f,g: T_split_BA+T_split_AB>0\`, including naive dual-direction supplementation of AH.

**Precise scope restriction:** a finite s=2 witness does **NOT** disprove an asymptotic \`forall sufficiently large 2^h\` lower, and does **NOT** yield an infinite globally injected all-h counterfamily or Branch B of #230. The FULL original B/A, A/B and entire seven selected GF5 classes MUST be checked separately under the SAME maps, using prior \`exact_two_sided_original_seven_join(..., independent_history=True)\` before claiming compensation counts. No total strict R3 or ASET consequence.

## 3. AA4-AI2: NEW all-h physical occupied connected C6 bridge theorem under EVERY global map

For genuine W(3,s), s=2^h>=2^19, every globally injected typed f,g pair, AA4-AG constructs at least N_good>=N/2 actual original intersecting source line pairs \`{l0,l1}\` through their unique real source point p, such that their two physically opposite pinned edges e0={u,v}, e1={w,x} are disjoint and each of their FOUR physical endpoints has opposite-map missing-edge degree <a/16. The minimal physical alphabet has K=C(a,2), exactly m=K-V<=a-2 missing physical images. AA4-AF guarantees for every actual original point p at least C4_floor>=a^4/128 occupied first-side complementary C4.

**NEW deterministic actual PHYSICAL connected-six-cycle construction:** For each such good pinned pair and ordered auxiliary coordinates y!=z outside its four endpoints, take the cycle

    u -- v -- y -- w -- x -- z -- u

containing BOTH pinned physical edges \`uv\`, \`wx\`. It is occupied by the SAME global opposite typed injection g whenever the four new edges \`vy\`, \`wy\`, \`xz\`, \`uz\` are in im(g). Because each pinned endpoint has missing degree <a/16, at least a-4-a/8 >=3a/4 choices of y and (after excluding y) at least a-5-a/8 >=a/2 choices of z are valid for a>=32. Thus at least a²/4 **distinct occupied simple connected physical C6** completions H exist per good genuine original root line pair under every single globally shared g. Each H has exactly six different physical coordinates and six occupied original opposite-factor physical edge images. Different (y,z) correspond to different edge sets, not just a redraw of one physical permutation orbit.

This gives the new uniform ALL-f ALL-g **PRE-HALL** lower

    P_C6_bridge(f,g) >= (N/2)*(a^4/128)*(a²/4)
                     >= s^14/256,  s=2^h>=2^19.

The earlier split-two-triangle AG subfamily P_triangle has the same s^14/256 floor. As both are disjoint actual PHYSICAL opposite A sectors,

    P_triangle(f,g) + P_C6_bridge(f,g) >= s^14/128.

This is an improvement of pre-Hall physical candidate mass and removes the idea that only two-triangle completions are robust to arbitrary globally correlated physical labels. **It DOES NOT imply ANY positive accepted original Q or S>=c*s^6**, since any selected true original 4x4 incidence matrix can have permanent zero. This all-h statement counts indexed actual original roots/pinned flags/first-side occupied original-factor-C4/second-side occupied opposite physical A patterns *before* original Hall acceptance.

Independent finite physical checks reconstruct each connected C6 bridge literally and by the separate common-neighbor identity \`|Y||Z|-|Y∩Z|\`, where Y is the set of shared occupied physical neighbors of (v,w), and Z of (x,u). The rank-six Hall transfer for two triangles does not directly apply to connected C6, which requires a genuinely new correlated source-incidence contraction.

## 4. Acceptance / scientific routing

The new FINITE dual-zero witness means that proving uniform positive AA4-AH split-triangle mass for **all h>=1** is mathematically impossible. The eventual asymptotic restricted all-h question remains open; do not silently promote the finite witness to an all-h failure. The new robust all-f,g connected-C6 occupancy theorem shows the full A transfer also has a physically well-populated connected source, but it is STILL a pre-Hall bound.

**Next allowed step AA4-AJ:** derive an exact original incidence source-physical connector for connected C6 physical completions, cross-check genuine ORIGINAL six-incidence sets, then seek aggregate Hall/JPKC/EICE compensation for (split triangle, same triangle, connected C6), with explicit tolerance for all other GF5 tags and genuine D6. Prove a uniform true original Hall-positive fraction or exhibit a valid infinite all-h full-seven-family counterexample. A purely physical capacity or another expectation estimate cannot close issue #230.

Run exact final PR-head GitHub-hosted dedicated, INDEX, Proof Audit and Full Research. Separate independent mathematical referee mandatory; keep stacked Draft, no automatic main merge, no RCP accepted claims until approval and five generated Markdown registry rebuilds.
