# HYP-105 / issue #230 — D6-AA4-Y3: ALL-h original source-star physical capacity

**Scope and classification.** Strict research-only successor of D6-AA4-Y2 PR #498, pinned parent HEAD `19fb53117b1ba850665d86ede8ae31c17cf82533` with all four workflows SUCCESS. New exact combinatorial physical K_a anchored-pattern theorem for genuine original symplectic W(3,s), s=2^h >=2; independent real ORIGINAL W(3,2) exhaustive six-flag tests. Universal root lower S_s=Omega(s^6) remains OPEN. No main writes or PR merge.

## 1. The missing quantitative estimate

Y2 proved for EVERY four globally injected point and line physical edge labellings the exact historical original seven-GF5 mode identity Delta S = F-H, where F counts favorable same-sign (+,+)/(-,-) shared original six-incidence modes and H counts harmful opposite-sign (+,-)/(-,+) shared modes. The minimum finite S68/S72 local-box lower obtained from this decomposition is +6/+2, not a bound for all maps or all s. The ALL-h Y3 objective is an explicit geometry-dependent cap on how many half-projection modes can change around an actual original source factor or a pair of such factors; then it bounds harmful H for any correlated two transpositions. Critically, an upper on H ALONE does not establish root Omega(s^6).

## 2. Notation

Use V=(s+1)(s²+1) ACTUAL original source point factors and V line factors, original degree d=s+1, minimal a with K=C(a,2)>=V, q=C(d,2). Each f or g maps all V actual source factors injectively into physical unordered coordinate pairs of [a]. A left or right half candidate is a genuine ORIGINAL Q of SIX DISTINCT original point-line incidence IDs whose six physical coordinate symbols each have degree two. Source multiplicity shapes are A=(1^6), B=(2,1^4), C=(2^3), with physical A a six-edge 2-factor (connected C6 OR two triangles), physical B a doubled pair plus disjoint C4, and physical C three disjoint doubled pairs. Every original source factor has d distinct actual incident flags, so after selecting distinct source factors the choices multiply EXACTLY by d or C(d,2). Physical K_a patterns using absent pair labels in a partial injection are discarded.

## 3. ALL-h one-root physical pattern theorem

Fix one ACTUAL original source factor x with globally injected physical pair f(x)=e. In COMPLETE physical K_a, the numbers of eligible physically projected patterns in which e occurs by source role are

    P_A(e)=28*C(a-2,4),
    P_Broot(e)=3*C(a-2,4),
    P_Bsingle(e)=2*C(a-2,2)*C(a-4,2),
    P_Croot(e)=3*C(a-2,4).

PROOF. Select 4 further physical coordinates beyond the fixed pair. For a prescribed K6, among its 70 2-factors, 28 contain one given edge (24 connected cycles and 4 two-triangle modes), giving P_A. For B-root, choose four disjoint coordinates and one of 3 C4s. For B-single, choose the remaining 2 C4 vertices and one of the two C4s containing e, then a root edge on two physical vertices outside the chosen C4. For C, choose four additional vertices and one of their 3 perfect matchings. ALL expressions are integer counts and hold in complete physical K_a.

Multiplying by ACTUAL source incidence choices yields **universal source-star upper** (exact for s=2 where the injected physical K6 is complete):

    U_A=P_A*d^6,
    U_Broot=P_Broot*C(d,2)*d^4,
    U_Bsingle=P_Bsingle*C(d,2)*d^4,
    U_C=P_Croot*C(d,2)^3,
    U_star=U_A+U_Broot+U_Bsingle+U_C.

The B-root physical source occurs twice, whereas B-single occurs once; this distinction is required for original incidence counts. For a FIXED ACTUAL original flag (x,l), exact complete-physical upper counts are

    V_A=P_A*d^5,
    V_Broot=P_Broot*(d-1)*d^4,
    V_Bsingle=P_Bsingle*C(d,2)*d^3,
    V_C=P_Croot*(d-1)*C(d,2)^2,
    V_flag=V_A+V_Broot+V_Bsingle+V_C.

Every original candidate is counted once in U_star for a marked source factor, and once in V_flag if that fixed original flag occurs. The consistency identity d*V_flag=U_A+2 U_Broot+U_Bsingle+2 U_C follows by original incidence double-counting. The U/V bounds are upper bounds at ALL orders because an actual incomplete injection occupies only a subset of physical K_a patterns.

## 4. ALL-h TWO-root physical adjacency/disjoint theorem

Choose TWO distinct ACTUAL original source factors x,y; their different physical edge images e,f must either share one physical coordinate (adjacent) or be disjoint. Number of COMPLETE physical K_a patterns containing BOTH e,f:

| Source class | Adjacent physical edges | Disjoint physical edges |
|---|---|---|
| A | 7 C(a-3,3) | 14 C(a-4,2) |
| B | (a-3) C(a-4,2) | 6 C(a-4,2) |
| C | 0 | C(a-4,2) |

PROOF: For A, fixed adjacent edges use 3 physical vertices, choose the remaining 3, and K6 has exactly 7 two-factors containing the marked adjacent edges. Fixed disjoint edges use 4 vertices, choose 2 and K6 has exactly 14 two-factors containing both. For B, two adjacent marked edges cannot be root and C4 simultaneously (root is disjoint from C4), so both must be in C4: choose its fourth vertex, the unique C4 containing both, then disjoint root edge. For disjoint marked edges, both can lie in C4 (2 choices) or one is root and the other is a C4 edge (2 choices for each orientation), total 6 per disjoint outside pair. For C, two adjacent physical edges cannot both be in a physical matching; two disjoint edges determine 4 of the 6 vertices, with C(a-4,2) choices for the last edge.

Each A/B/C pattern containing both marked edges maps to real ORIGINAL six-flag choices in exactly d^6 / C(d,2)d^4 / C(d,2)^3 ways, respectively. Let T_A,T_B,T_C be these physical both-edge counts times their flag-choice factors. Let U_B=U_Broot+U_Bsingle. The complete-physical two-root union is EXACTLY

    U_pair^rel = 2*(U_A+U_B+U_C) - (T_A^rel+T_B^rel+T_C^rel).

Every actual physically injected ORIGINAL half-projection pattern is contained in the complete-K_a family; therefore **# of actual Q touching either marked source factor <= U_pair^rel** for all s and every complete globally injected f or g. Equality holds for ALL globally bijective K6 physical source maps in genuine W(3,2). The two-root bound refines naive 2 U_star and explicitly accounts for adjacency/disjoint geometry of ORIGINAL source factor images.

## 5. ALL-h harmful original seven-mode capacity corollary

Fix any genuine original GQ and two independent complete globally injected map changes: point images differ only at two actual source POINT factors and line images differ only at two actual source LINE factors (e.g., global transpositions). The two marked physical pairs on a side retain their adjacent/disjoint relation under a swap. Every TRUE ORIGINAL seven-positive GF5 half-feature mode is tied to ONE six-original-flag Q, and each physical half has at most one active source-mode feature per Q. Unaffected Q contribute zero to the signed gradient. Thus on each side, the number of nonzero changed mode entries E_P and E_L is at most the sum of the two endpoint-map active source-pair-supported Q sets, each <= U_pair^rel. Hence

    E_P <= 2*U_pair(point relation),
    E_L <= 2*U_pair(line relation).

Y2 exact harmful shared-mode count H counts an intersection of nonzero signed ORIGINAL half-mode features and consequently

    0 <= H <= min(E_P,E_L) <= 2*min(U_pair(point),U_pair(line)).

This is a genuine explicit all-h bound for the ORIGINAL GF5 harmful mixed-charge term, even when the mixed interaction Delta S is negative, and does not assume any independent per-Q source labellings. It is asymptotically **too weak** to prove the root S_s>=c*s^6; the star envelope U_star ~ (287/48)*s^12 for minimal a ~ sqrt(2)*s^(3/2). A new simultaneous original point+line overlap-capacity or source-forest charge lower is required to improve the gap.

## 6. Pinned full-original W(3,2) numeric exact checks

For s=2, d=3, a=6, K=15 (full K6), the formulas are EQUALITIES for every source and global injection, not statistical averages:

| Quantity | Actual original six-ID candidates |
|---|---:|
| One original source A | 20,412 |
| One source B, repeated root | 729 |
| One source B, once-used C4 | 2,916 |
| One source C | 81 |
| TOTAL for one source star | **24,138** |
| One ACTUAL original incidence A | 6,804 |
| One ACTUAL incidence B repeated-root | 486 |
| One ACTUAL incidence B C4-once | 972 |
| One ACTUAL incidence C | 54 |
| TOTAL for one ACTUAL original incidence | **8,316** |
| Two physical-edge-adjacent original sources, union | **42,444** |
| Two physical-edge-disjoint original sources, union | **36,585** |

The full true-original W32 test uses the independent AA4-Q per-half index of **62,370 distinct actual original six-flag subsets** for each typed source side and every pinned lex, reverse, S68, S72 labelling. It enumerates all 15 actual source stars, 45 actual source incidences and 105 unordered source-factor pairs per typed side, verifies EVERY class A/B/C count and relation-specific union count, and validates the 60 adjacent +45 disjoint physical marked-pair classes. A second independent physical K6/K7 enumerator tests the underlying 2-factor, C4-root, matching anchored counts. The complete 11,236 signed ORIGINAL Y2 conflict rows per anchored S68/S72 are independently checked against the all-h explicit two-source harmful H upper.

## 7. Acceptance and follow-up

Executable theorem/ORIGINAL verification: research/hyp105_issue230_d6aa4y3_original_source_star_capacity.py; independent tests research/test_hyp105_issue230_d6aa4y3_original_source_star_capacity.py; GitHub-hosted dedicated CI .github/workflows/hyp105-issue230-d6aa4y3-original-source-star-capacity.yml. No source-girth shortcut beyond genuine GQ regularity, six distinct original incidences and forbidden C/C. The result is an ALL-h upper capacity theorem, not Branch A universal obstruction, Branch B infinite o(s^6) construction or model-equivalent Branch C.

Next mathematical gate: tighten the mixed capacity by counting the ACTUAL shared ORIGINAL Q requiring BOTH modified point and modified line factors with connected six-position AA modes and/or a positive non-AA source forest class. Two independent one-sided source stars leave an O(s^12) envelope versus the desired Omega(s^6) positive floor, so claiming universal root acceptance would be mathematically unjustified. Keep PR Draft until exact-head Dedicated + INDEX + Proof Audit + Full Research PASS and independent mathematical review; no merge/main modification, issue #230 remains OPEN.
## 8. Strengthening: ORIGINAL point-line crossed stars and GQ no-4cycle capacity

**This strengthens the initial one-typed-side O(s^12) envelope to a genuine ALL-h O(s^11) bound on harmful GF5 shared-mode conflicts under one source-factor transposition on EACH side. It still does NOT reach the s^6 scale required by root Branch A.**

### 8.1 One marked source p plus one opposite source ℓ

Fix an actual source POINT factor p and an actual source LINE factor ℓ (the point/line dual argument is identical). Let Q be a true six-distinct-original-incidence subset whose physically 2-regular POINT half uses p and whose actual source LINE support contains ℓ. Since ℓ has exactly d distinct original point-neighbors N(ℓ), Q contains at least one original flag (q,ℓ) for some q∈N(ℓ). Union-bound by the choice of this actual original flag; no replacement by independent synthetic point/line samples.

If q=p, which is possible only when the true GQ contains original (p,ℓ), the number of Q is bounded by V_flag derived in §3. For q≠p, their global distinct physical source images are adjacent or disjoint. The complete physical pattern counts using BOTH physical edges are the T_A,T_B,T_C from §4. With ONE exact original flag (q,ℓ) fixed, the ORIGINAL neighbor-choice upper per physical two-source pattern is:

    A: d^5,
    B: max((d-1)*d^4, C(d,2)*d^3)=(d-1)*d^4,
    C: (d-1)*C(d,2)^2.

Explanation: A uses q exactly once, leaving five other independent source flag choices. In B, if q is the repeated root then choose its second ORIGINAL incidence in d-1 ways and choose the four single factors in d^4 ways; if q is single then choose the doubled-root flags C(d,2) and three further single flags d^3, exactly half the conservative root-bound, so taking the root bound is safe for either source role. In C, q is repeated twice and its second actual flag has d-1 choices, with C(d,2) each for two other repeated original factors.

Let T_flag^rel be the sum over A/B/C physical two-edge pattern counts times these corresponding flag-choice weights. Then for arbitrary globally injected POINT map f:

    U_cross(p,ℓ; f) <=
      1_{(p,ℓ)∈I} * V_flag
      + sum_{q∈N(ℓ), q≠p} T_flag^relation(f(p),f(q)).

This is an exact all-h upper for actual source Q jointly involving p and ℓ; it uses real original GQ incidence-neighbor sets and the physical image relation in ONE globally coherent f. In particular, with T_max=max(T_flag^adj,T_flag^dis),

    U_cross(p,ℓ) <= I(p,ℓ)*V_flag + (d-I(p,ℓ))*T_max.

### 8.2 Two original point sources × two original line sources

Let P={p1,p2} and L={ℓ1,ℓ2} be the source factors whose images are exchanged. The number m of ACTUAL source GQ incidences between P and L is at most THREE, since all four would form K2,2, an original bipartite 4-cycle prohibited by GQ girth >=8. Every Q used by a mixed mode difference touches at least one marked original point and one marked original line (Y-CYC support identity). Sum the four cross-star upper bounds to obtain

    U_cross_2x2(m) = m*V_flag + (4d-m)*T_max,     0<=m<=3.

Let U2^point, U2^line be the physical adjacent/disjoint marked-source pair union bounds from §4. Each BEFORE/AFTER physical half has at most one GF5 positional mode per actual Q, so the two half signed mode energy counts E_P, E_L satisfy:

    E_P <= 2*min(U2^point, U_cross_2x2(m)),
    E_L <= 2*min(U2^line, U_cross_2x2(m)).

Since every harmful mode is in the intersection of the signed point and line half gradients, the actual ORIGINAL historical GF5 harmful mixed term satisfies the NEW all-h deterministic cap

    0 <= H <= 2*min(U2^point, U2^line, U_cross_2x2(m)).

Crucially, as s→∞ with minimal physical alphabet a ~ sqrt(2)*s^(3/2), V_flag=O(s^11), T_flag^adj=O(s^(19/2)), T_flag^dis=O(s^8), so U_cross_2x2(m)=O(s^11). The earlier one-typed-side pair-star cap alone was O(s^12). When m=0 (no actual point-line marked incidences), the improved cross-star cap is O(s^(21/2)), whereas for m>0 it can be O(s^11). This is a meaningful one-power all-h structural improvement but does NOT prove H=O(s^6), let alone a positive source-forest charge floor sufficient for universal S_s=Omega(s^6).

### 8.3 Independent falsification

The new executable module research/hyp105_issue230_d6aa4y3_original_cross_source_capacity.py gives exact integer all-h formulas for both marked sources with ONE truly fixed opposite original flag, per-physical-relation source cross-stars, the no-GQ-K2,2 2×2 cap and all-h comparative orders. Its independent tests cover actual original incidence p↔ℓ, direct known W32 2-source+one-flag constants, all 11,025 genuine W32 marked 2point×2line source layouts (m=0,1,2,3, never 4), and all 15×15 source point-line cross-stars on both typed half projections using ALL 62,370 real original Q per side for S68/S72.

The existing original Y2 C++20 signed conflict engine independently generates all 11,236 TRUE complete globally injected W32 paired maps per S68/S72. The strengthened Y3 Python audit now checks each of the 11,025 nontrivial shared-mode harmful counts H against the NEW all-h crossed-star bound using the actual original source incidence count m for each physical pair swap. All outputs are source-pinned in CI artifacts. No statistical sampling or assumptions about independence.

Next allowed research gate after acceptance: replace this still-loose cross-star union estimate by exact multi-center source-forest and same-Q physical-position collision capacities (especially AA connected C6 and B/B repeated-source overlap) that reach the root s^6 scale, or produce a true infinite adversarial counterfamily. Maintain root A/B/C OPEN.

### 8.4 Explicit all-h leading constants (not a root lower bound)

All asymptotics below refer to the actual minimum physical alphabet a with C(a,2)>=V=(s+1)(s²+1), so a=(sqrt(2)+o(1))*s^(3/2), d=(1+o(1))*s, q=C(d,2)=(1/2+o(1))*s². They follow by expanding the exact finite binomial formulas above, not by empirical extrapolation:

    U_star = (287/48 + o(1)) * s^12,
    V_flag = (151/24 + o(1)) * s^11,
    T_flag^adjacent = (10*sqrt(2)/3 + o(1)) * s^(19/2),
    T_flag^disjoint = (81/4 + o(1)) * s^8.

Thus, for a fixed number m=1,2,3 of REAL original source incidences in the affected 2point×2line layout, the cross-star harmful upper is

    H <= (151*m/12 + o(1)) * s^11;

for zero such incidences, the stronger exponent is

    H <= (80*sqrt(2)/3 + o(1)) * s^(21/2).

In particular every genuine two-source-swap pair obeys H <= (151/4 + o(1))*s^11 in the worst source layout m<=3. These constants characterize the proven EXPLICIT cross-star upper and do NOT assert it is tight for adversarial physical maps, a lower on H, or a positive original seven-class S_s bound. The qualitative missing advance remains several powers of s between this harmful capacity and the desired universal Omega(s^6) seven-positive obstruction.
