# HYP-105 E1-K3-G2-R — unique physical 5-edge completion and full ALL-a Johnson spectrum

Date: 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked on Draft [PR #390](https://github.com/definitely-stable/Mathlab/pull/390), pinned exact parent HEAD d26574cd26fc247f874bdeb95cbf79270fe0dff3. Main unchanged, no merges. Keep #230/#176/#169 OPEN and pending mathematical peer review even after CI.

## 1. Why a fifth-order target theorem matters, but does not prove P2

K3-G2-Q proved the all-h exact ORIGINAL anchor-square incidence-permanent formula and sharp 4x4 girth-eight permanent cap. It decomposed ORIGINAL W32 and TRUE GQ dual A/B sixth-order weights into permanent-one and permanent-two witnesses and showed that negative physical fifth+sixth signed correlations on a hard globally coherent W32 state mainly arise from **permanent-one** witnesses. This falsifies the simplistic hypothesis that local multiple matchings cause all negative residuals.

The remaining target physical Johnson H5+H6 component is not a source-independent positive quantity. Rather than assuming its sign, R derives H5 analytically using a special and very sparse fact about genuine simple six-edge 2-factors. The new result closes the **physical target full rank-0..6 harmonic energy bookkeeping for every a>=6**, without constructing the exponentially large J(C(a,2),6). It does not close the **source-dependent adversarial overlap** and is NOT an all-h lower bound.

## 2. ALL-a Theorem R1: a physical five-edge set has at most ONE two-factor completion

Fix integer a>=6, K=C(a,2). Let T_a consist of the 70*C(a,6) genuine six-edge simple 2-regular graphs on **exactly six distinct physical coordinates**, embedded in K_a, without original-source labels.

Any target T is either a single undirected 6-cycle (60 per six coordinates) or the union of two vertex-disjoint triangles (10 per six coordinates). Delete one of its six edges. The remaining five-edge graph F has exactly six vertices and one of exactly TWO shapes:

1. A simple path P6 (5 edges, 6 distinct physical vertices), arising by deleting an edge from a 6-cycle.
2. A disjoint union C3+P3 (one triangle with 3 edges plus a path of 2 edges, 6 distinct physical vertices), arising by deleting one edge from the second triangle.

Conversely each physical five-edge subset F of either shape has **exactly one** completion in T_a: the missing edge is uniquely determined by the two degree-one endpoints of F. Every other five-edge shape has **zero** target completions. In particular the physical 5-subset codegree is exactly 1 or 0 and depends only on the graph's shape, **independently of a**. This classification is verified by exhaustive complete K6 and K9 actual target-derived five-subset enumeration, with an independent scan of every C(15,5)=3003 physical K6 five-edge subset.

This is a classical graph fact; its usefulness here is that almost all physical fifth-down-marginals vanish and we can compute H5 without enumerating their physical graphlet orbit types.

## 3. ALL-a Theorem R2: exact Johnson rank five and six

Let p=70*C(a,6)/C(K,6). Denote by h2(B),h3(A),h4(D) the **exact existing** physical target Johnson down-harmonic coefficients established in N/O/P for all a, and by H_j(F)=sum_{B subset F, |B|=j}h_j(B) their lifted lower-harmonic contribution on five-edge F.

The rank-five Johnson up/down eigenvalue for the 6-slice is K-10=C(K-10,1). The five-down-marginal of the lifted rank-j target harmonic is C(K-5-j,1)*H_j(F) for j<5. The rank-one target coefficient is identically zero.

Thus for *every* physical five-edge subset F and every a>=6, the UNIQUE rank-five harmonic coefficient is

    h5(F) = [
        c5(F) - p*(K-5)
        - (K-7)*H2(F)
        - (K-8)*H3(F)
        - (K-9)*H4(F)
    ]/(K-10),

where c5(F)=1 iff F is P6 or C3+P3 and is 0 otherwise. Its rank-five lift on a physical sixset S is simply t5(S)=sum_{F subset S,|F|=5}h5(F).

For a target T of 6-cycle type, its six five-edge deletions are ALL P6, so t5(T)=6*h5(P6). For a target T of two-triangle type, all six deletions are C3+P3, so t5(T)=6*h5(C3+P3). Johnson orthogonality gives the exact energy identity

    E5(a) = ||t5||² = <1_T, t5>
          = C(a,6)*[360*h5(P6)+60*h5(C3+P3)].

Only two representative five-edge graphs need be evaluated, for ANY a>=6. With exact target energies E0, E1=0, E2, E3, E4 from N/O/P, Parseval then gives the final rank-six energy

    E6(a)=70*C(a,6)-E0(a)-E2(a)-E3(a)-E4(a)-E5(a).

The new implementation checks E5,E6>=0 and complete seven-level Parseval across multiple a; an independent true target 5005-sixset Johnson projector checks **every** K6 rank-five and rank-six lifted value against R's explicit five-edge coefficient and residual formula, not just its energy.

For a=6 this MUST reproduce independently frozen energies

    [E0,E1,E2,E3,E4,E5,E6]
       = [140/143,0,42/11,710/1001,86/7,1182/77,258/7].

No unsupported all-a source control is inferred from this exact physical target identity.

## 4. Same-global-map joint ORIGINAL+DUAL GQ permanent-one/two by rank-five and rank-six

For each true ORIGINAL source map (f,g), use Q's independently reconstructed exact original right-sixset source weights w_f(R)=n1(R)+2n2(R), where n1 counts anchored 4x4 GQ permanent-1 witnesses and n2 counts anchored permanent-2 witnesses. It has a genuine transpose/dual version w_g^dual(P) independently reconstructed from E^op with whole maps f,g swapped.

With the SAME physical labels and original incidence endpoints, partition the signed rank-five and rank-six target overlaps *separately*:

    C_j^(BA)(f,g)
       = sum_R n1(R)*t_j(g(R))
         + 2*sum_R n2(R)*t_j(g(R)),
    j=5,6.

Compute independently again for TRUE ORIGINAL GQ dual A/B with f(P). This gives TWO exact 2-by-2 rational tables, with rows local permanent 1 and 2, columns Johnson rank 5 and 6. The row and column marginals must reproduce all of Q's original rank56 witness splits and the independently frozen N full target Johnson spectrum. The summation C5^BA+C5^AB and C6^BA+C6^AB is a genuine joint statistic of one coherent f,g state (not a surrogate independent random mapping).

A signed table is not a *nonnegative Hall-flow capacity* and does not by itself yield a positive lower bound. In fact the known hard original state has C56_BA=-56/11 and C56_AB=-167/42, so some negative signed contribution is unavoidable. Neither rank-five nor rank-six nonnegativity is assumed.

## 5. Acceptance / falsification / next mathematical obligation

- Prove and independently test unique physical five-edge 2-factor completion from both 6-cycle and two-triangle targets, with explicit forbidden shapes and all physical K6 five-edge subsets.
- Independently enumerate K6/K9 actual target five-edge codegrees, and compute complete K6 5005-sixset target rank5/6 vectors versus N frozen exact orthogonal projector.
- Compute all-a exact target physical energies E0..E6 for a=6,9,14, plus several extra a in focused tests; no full J(C(a,2),6) enumeration for large a.
- Reconstruct original and TRUE ORIGINAL GQ dual W32 sources using Q's exact ALL 5005 original right-sixsets; compare full B0/C0 accepted seven-family oracle on two coherent global maps only (lex and M-hardest), and independently split rank5 and rank6 by source original permanent 1/2. Never declare a partial probe a full W32 all-label result.
- Hosted dedicated Contract + INDEX + full Research SUCCESS at **exact FINAL HEAD**, plus independent mathematical review before acceptance. Remain Draft, main unchanged, no merges.

**Not proved:** universal P2 U_BA(f,g)+U_AB(f,g)>=mu_f for ALL coherent f,g, seven-family P7, all-h S=Omega(s^6), charging K, full GF5 R3 upper or an ASET exponent. Graph-theoretic unique completion and Johnson spectral identities are derivations using existing mathematical tools, NOT evidence of a new asymptotic combinatorial lower bound.

## 6. Next K3-G2-S decision

The physical target ranks 0..6 now have complete exact formulas, while Q's ORIGINAL 4x4 GQ permanent witnesses give a much finer SOURCE parametrization. Next genuine proof obligation is to use the **shared ORIGINAL incidence** between B/A and A/B witness systems to construct (or falsify) a bounded-capacity, nonnegative, explicitly geometric charging scheme for negative signed rank5/6 permanent-one contributions. Any proposed all-h inequality must be uniform in f,g and s, and ideally imply P2 or P7 using the OTHER positive motifs, not merely recompute a signed spectral identity. An exact W32 finite Hall failure would invalidate only the corresponding chosen charging graph, not universal P2.

## 7. First hosted exact all-a spectrum and same-map joint signed NO-GO — 2026-10-12

The corrected [dedicated hosted Contract #38248723614](https://github.com/definitely-stable/Mathlab/actions/runs/38248723614) is **SUCCESS** at intermediate R HEAD eb5038eb1c8fee40e4ec10f8b3d3a6c2c0799318. Five independent unit tests (25.201s), then two full genuine original+dual globally coherent W32 source reports. First attempt #38248574088 failed one **test-only canonical physical edge** mistake (test input (4,0) replaced by (0,4)); all other four independent tests succeeded on the initial run. No theorem or mathematical implementation was altered in that fix.

The new ALL-a exact full seven-rank physical TARGET squared energy table, in order E0..E6:

    a=6:  [140/143,0,42/11,710/1001,86/7,1182/77,258/7]
    a=9:  [102900/5797,0,0,35712/493,1436/11,
           273240/377,1988600/403]
    a=14: [7357350/110983,0,2102100/21199,
           1682278884/3641791,3853077228/2487593,
           3749500040/368271,260563803500/1316961].

At a=6 the two unique five-edge physical completion orbit coefficients are h5(P6)=18/385 and h5(C3+P3)=-19/770. These all-a target values exactly reproduce the entire independent N Johnson projection on all 5005 physical K6 sixsets, for BOTH rank 5 and rank 6; no large physical sixset enumeration was used for a=9/14 formulas.

For the previously accepted original hard correlated W32 global f,g state, ORIGINAL B/A and TRUE ORIGINAL DUAL A/B yield separately

    original B/A: C5=-260/77, C6=-12/7, C56=-56/11;
    genuine A/B: C5=-83/42, C6=-2, C56=-167/42.

The **joint original+dual** signed contributions are

    C5^(BA)+C5^(AB)=-2473/462 < 0;
    C6^(BA)+C6^(AB)=-26/7 < 0.

These values are for the SAME actual coherent original labels f,g. Thus BOTH proposed termwise bounds C5_BA+C5_AB>=0 and C6_BA+C6_AB>=0 are refuted on a genuine W32 labeling. This does NOT refute P2: true U_BA=36, U_AB=39, original fixed-left mean mu_f=9968/143, P2 margin 757/143>0, full S_seven=86.

Even at the ORIGINAL GQ local 4x4 matching level, the 2x2 rational rank5/rank6 decomposition is:

    hardest BA:      permanent-one [-8951/2310,-99/35],
                     permanent-two [1151/2310,39/35];
    hardest dual AB: permanent-one [-1703/770,-208/105],
                     permanent-two [272/1155,-2/105].

The rank5 negativity is predominantly from unique original matchings; the rank6 negativity is not uniformly attributable to only one of the two source multiplicities. The two-matching physical contribution is not universally positive (dual rank6 -2/105). A uniform all-h positivity or charging proof must exploit lower ranks, other positive motifs or actual incidence coupling and cannot require either joint signed high rank to be nonnegative.

The exact scalar regressions and full all-a target energies have been PINNED in the dedicated Contract after the first hosted green. The final revision after these docs is NOT accepted until its exact-head Contract/INDEX/full Research all SUCCESS and independent mathematical review. Main unchanged; #230/#176/#169 and stacked PRs remain OPEN / Draft. The next S step requires a bona fide geometric nonnegative Hall/charging construction or its falsifier; do not confuse signed harmonics with positive target capacities.
