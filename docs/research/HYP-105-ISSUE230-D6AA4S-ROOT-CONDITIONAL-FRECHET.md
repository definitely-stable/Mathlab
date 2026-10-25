# HYP-105 / issue #230 — D6-AA4-S: all-h ORIGINAL root-conditioned Fréchet marginal NO-GO

**STRICT research-only Draft stacked on AA4-R PR #477 at exact parent HEAD d2c06af97e17a4f3eddff6bcc95df203b843e4e1. Main not modified.** This is an all-h negative theorem about a mathematically precise class of marginal-only lower-bound strategies, not a counterexample to the universal seven-GF5 positive lower conjecture. The independent TRUE W(3,2) oracle uses the original 45 incidence IDs, both complete K6 globally injected physical maps, and source-geometry validation including all GQ unique-anchor axioms. No finite s-to-infinity fitting.

## 1. Mathematical problem: can a fixed TRUE original repeated point root force B/A?

Let s=2^h>=2, V=(s+1)(s²+1), d=s+1, E the N=Vd ACTUAL original point-line incidences of W(3,s), and a the **minimal** positive integer with C(a,2)>=V. Let f (points) and g (lines) be ANY independently type-preserving **complete globally injective** maps to physical unordered K_a edges. Fix a true original point p.

Define U_p, source-only and independent of physical f,g, to be the set of six-DISTINCT ORIGINAL incidence ID subsets Q for which the point factors have multiplicities (2,1,1,1,1) with unique repeated ORIGINAL point p, and the line factors have multiplicities (1,1,1,1,1,1). All six original line IDs are distinct.

Define L_p(f)=U_p∩H_P^B(f), where the physical left half is six-coordinate degree-two type B. Define R_p(g)=U_p∩H_L^A(g), where the physical right half is six-coordinate degree-two type A. These preserve the original p and actual six incidence IDs. The historical seven-GF5 **B-left/A-right accepted source sixsets** rooted at p are EXACTLY

    J_p^{BA}(f,g)=L_p(f) ∩ R_p(g).

The naive (root-conditioned) Fréchet lower guarantee based ONLY on the true source-root universe size and two unilateral marginal sizes is

    lower_p(f,g) = max(0, |L_p(f)| + |R_p(g)| - |U_p|).

This is always a valid deterministic lower on |J_p^{BA}|. It is mathematically sharp in the *relaxed* model of arbitrary subsets of U_p with these sizes, by taking subsets with minimal overlap. **The relaxation does not necessarily admit globally injected physical maps.** Therefore a zero lower says these marginal data cannot prove positive overlap; it emphatically does NOT imply a real injection attaining zero.

## 2. New universal all-h source-root conditioned no-go theorem

**Theorem S1 (all h>=1, ALL genuine W(3,s), ALL global f,g, EVERY true original point p):**

    |U_p| >= M_p(s)
          := C(d,2) * PROD_{j=0..3}[d*(V-3-2j)] / 24.

    |L_p(f)| <= B_p(s)
              := 3*C(a-2,4)*C(d,2)*d^4.

    |R_p(g)| <= A(s)
              := 70*C(a,6)*d^6.

    M_p(s) > B_p(s) + A(s).

In particular

    for every p,f,g,s: max(0, |L_p(f)|+|R_p(g)|-|U_p|) = 0.

By point-line duality the identical result holds for the source-**line** root of A-left/B-right.

**Proof of the genuine source lower M_p.** Choose two distinct actual original incident lines through fixed p in C(d,2) ways. Choose four more actual original incident flags with four fresh original point factors (none equal p, pairwise distinct) and four fresh original line factors (different from the two root lines, pairwise distinct). After j additional flags, at most (3+2j)*d actual source incidences touch any already used point or line. At least d(V-3-2j) valid next actual flag choices remain. Divide ordered four-flag selections by 4!=24; all generated sixsets are distinct, have exactly one original point repetition at p and six distinct source line endpoints, so are in U_p. This argument is all-h and uses no artificially chosen physical labels.

**Proof of B_p physical upper.** The physical edge f(p) has two coordinate endpoints. Its complementary physical coordinates contain at most C(a-2,4) choices of four distinct symbols, and precisely THREE simple C4 physical patterns on these four. In a global injection each such physical edge determines at most one true original point factor; at most C(d,2) choices of genuine incidences at root p and d^4 choices at the other four distinct point factors. Ignoring extra original line uniqueness only INCREASES the upper. This holds simultaneously for ONE complete f.

**Proof of A physical upper.** Each chosen six-coordinate physical alphabet admits exactly 70 six-distinct-edge two-factors (C6 or two triangles), and their six distinct original line source factors each have d genuine source incidence choices. Thus |H_L^A(g)|<=70*C(a,6)*d^6, so |R_p(g)| is no larger. This holds simultaneously for ONE complete g. No independent per-Q physical relabeling occurs.

**Proof of strict numerical gap for all powers of two.** The cases s=2,4,8,16 have exact integer values below. For every s>=32 one has V>=s³, d>=s, V-9>=s³/2, C(d,2)>=s²/2, hence M_p>=s^18/768. Minimal physical a obeys a<=2s^(3/2) for s>=4: with b=floor(2s^(3/2)), b>=2s^(3/2)-1 and C(b,2)>=2s³-3s^(3/2)+1 >=V; thus a<=b. Also d<=5s/4. Consequently

    B_p <= (5/4)^6*s^12,
    A <= (56/9)*(5/4)^6*s^15,

and their sum is <=(65/9)*(5/4)^6*s^15. This is STRICTLY below s^18/768 when s³>1,015,625/48, as holds for EVERY s>=32. All displayed constants are exact rationals; no statistical extrapolation. This proves S1 all h>=1.

| s | minimal a | M_p, genuine source universe lower | B_p left root cap | A right global cap | certified strict gap M_p-B_p-A |
|---:|---:|---:|---:|---:|---:|
| 2 | 6 | 58,320 | 729 | 51,030 | 6,561 |
| 4 | 14 | 10,127,000,000 | 9,281,250 | 3,284,531,250 | 6,833,187,500 |
| 8 | 35 | 1,106,019,023,454,720 | 28,995,420,960 | 60,382,964,149,200 | 1,045,607,063,884,560 |
| 16 | 94 | 171,499,941,395,314,497,920 | 95,215,212,860,040 | 1,375,724,937,609,359,610 | 170,124,121,242,492,278,270 |

Note: M_p is a rigorous source universe LOWER bound, not an exact enumeration of |U_p| at general s. Since the sum of the unconditional point-root upper and the unrestricted right-A upper is already strictly below M_p, the argument is stronger than requiring just the separately observed root-conditioned half marginals.

## 3. Exact REAL ORIGINAL W(3,2) two-sided root experiment

Algorithm S2 independently enumerates the actual W32 source universe U_p for **every one of 15 actual original point IDs** by selecting a pair of original flags through p and four actual extra flags with pairwise fresh ORIGINAL point/line factors. It obtains all 15 true |U_p| without inspecting f/g. This is an independent source-only enumeration, not the same as the M_p elementary lower bound.

For each real complete global f and g, AA4-Q's left and right candidate six-ID maps independently enumerate 62,370 genuine source sixsets each, then filter by the source-only B/A point-root property. Report exact |L_p| and |R_p|, the actual seven-GF5 accepted B/A intersection, and the root-conditioned Fréchet lower. All 15 Fréchet floors must be identically ZERO for S68, S72, lex, reverse and globally shuffled BOTH injections, while real positive original B/A intersections are cross-checked against both the historical true-seven-GF5 original census and the independent two-sided full GF5 join.

**Measured genuine W32 source/result facts, reproduced by independent hosted enumerators on the exact experimental commit:** the exact actual source-only universe is **|U_p|=111,132 for EACH of all 15 genuine original source points**, which is strictly larger than the theoretical source lower 58,320. Nevertheless the full true jointly projected B-left/A-right six-GF5 class is **44 original sixsets for S68** and **36 for S72** (not zero). Their accepted original incidence ID sets are independently compared against the historical full original seven-class classifier, and **each** of the 15 root-wise marginal-only Fréchet lower bounds stays zero. This is an explicit positive-coupling vs zero-relaxed-certificate separation, not a construction of vanishing actual global GF5 charge.

This shows the **source-root conditioning strategy is mathematically incapable of certifying ANY single positive B/A joint original sixset based solely on these counts**, even though actual coherent examples can have positive genuine B/A joint charge. Same result for A/B by original GQ duality. It does not exclude better inequalities involving original INCIDENCE POSITIONS, true GQ Hall/cell correlations, coupled physical duals, aligned D6, nonlinear constraints, or all seven families together.

## 4. Decision gate, transfer to AA4-T and limitations

**Status classification:** RESTRICTED_THEOREM_C for a *negative result about a well-defined relaxed proof method*, **NOT** PROVED_A and NOT COUNTEREXAMPLE_B of the root all-seven S=Omega(s^6) hypothesis. No f,g with S=o(s^6) on infinite h has been constructed. No full GF5 R3/ASET bound obtained.

**Genuine next proof target:** root-conditioned *incidence-position* tensor capturing which exact original flags and original line factors carry the projected B/A charge, and how AA misalignment is compensated by non-AA or physical-dual aligned D6. It MUST use more than per-original-root marginal cardinalities: S1 makes every such root-only Fréchet lower exactly zero for ALL h. A future positive certificate must exploit some higher-order original source/physical correlation (e.g., JPKC or internally-blocked EICE-003 source-anchor constraints), not merely root frequencies, average charges or independent half counts.

**Fail closed:** original W32 validator checks actual source GQ unique-anchor axiom; full true global physical K6 injections per type; no per-Q pseudolabeling; seven-class historical check independent from two-sided projection enumeration; original Q preserved; all integer arithmetic. Separate independent mathematical proof review remains necessary. Require dedicated AA4-S + INDEX + Proof Audit + full Research GitHub-hosted success on exact final HEAD, postmerge Research only if ever merged, and no premature issue #230/#176/#169 closure.
