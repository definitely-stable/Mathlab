# HYP-105 / #230 — AA4-CQ: uniform ORIGINAL GQ 3-path cut substrate and six-palette spectral transfer barrier

**Scientific Draft / derived-classical partial theorem, NOT root Branch A, B or C.** Strict child of AA4-CP [PR #616](https://github.com/definitely-stable/Mathlab/pull/616) exact parent HEAD 59b8b33e9b12d3aab81cc843c39aad6574058b71. NO new all-seven historical GF(5) lower, no modification to the accepted seven positive class predicates, no changes to main. Original scientific root [#230](https://github.com/definitely-stable/Mathlab/issues/230) is OPEN_WITH_FORMAL_BLOCKER.

## 1. Why this step instead of another finite GF5 score

AA4-CP supplies independent full seven-positive **six distinct ORIGINAL incidence-ID** censuses for two complete original W(3,4) physical maps. Its 433525/401411 fixed-map S values do not bound the minimum over ALL complete arbitrary correlated globally injective original POINT f and LINE g maps for every s=2^h. Prior D6-AA4-Q/AA4-U already isolate the exact SAME-original-six-ID half-join and reject marginal Frechet extrapolation; prior AA4-CO demonstrates the missing five source buckets when looking at only two D6 fibers.

This slice tests a different proposed proof route: **the unique original nonincident-point-to-line length-three path in a generalized quadrangle, confined by arbitrarily chosen physical coordinate cuts**. We derive an explicit universal Omega(s^6) count for this original THREE-FLAG substrate, then quantify why the standard second-eigenvalue incidence mixing lemma alone cannot transfer that substrate at the physical six-coordinate resolution needed for GF5. A count of 3 original flags is NOT a count of six ORIGINAL distinct flags accepted by any historic GF5 class. This is an explicit proof-method gate, not a root-equivalent C reduction.

Relevant classical sources:
- GQ definition and parameters: https://mathworld.wolfram.com/GeneralizedQuadrangle.html
- Finite GQ nonincident point-line unique 3-path, cubic incidence identity and sqrt(2s) secondary spectrum: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i4p24/pdf/ (2012, large incidence-free sets in geometries).
These are established GQ spectral/girth facts; we DO NOT claim they are novel or invented by AA4-CQ. The new project-specific contribution is the exact minimal-physical-pair-cut quantitative transfer/no-go boundary, with genuine source model oracles.

## 2. Exact quantifiers and theorem

For EVERY integer h>=3 (s=2^h>=8), let G be genuine original symplectic W(3,s), with its V=(s+1)(s^2+1) ORIGINAL POINT factors, V ORIGINAL LINE factors, and V(s+1) DIFFERENT ORIGINAL incidence flags. Let a be the **minimal** integer with K=C(a,2)>=V, so the number H=K-V of missing physical pair edges obeys 0<=H<=a-2.

For EVERY complete globally injective typed map f:POINT(G)->C([a],2) and g:LINE(G)->C([a],2), without ANY independence hypothesis (the maps may be adversarially correlated), and for EVERY two physical coordinate subsets X,Y subset [a] of size k=floor(a/2), define
- P_X={original point p: f(p) is a physical pair wholly inside X};
- L_Y={original line l: g(l) is a physical pair wholly inside Y};
- T(X,Y;f,g) = number of ordered pairs (p,l) in P_X x L_Y that are **NOT** incident in ORIGINAL G. Equivalently, T counts genuine ORIGINAL SIMPLE length-3 incidence paths p--l0--p0--l between those endpoints, one per such pair.

**Scoped all-h theorem** (any correlated maps, any half-alphabet cuts, no asymptotic simulation):

    T(X,Y;f,g) >= m(m-(s+1)) >= V^2/128 > s^6/128,
    m=C(floor(a/2),2)-(K-V).

All inequalities hold for s>=8. Counts and constants are exact integer-combinatorial consequences of GQ axioms, minimal physical edge alphabet and injectivity. The path has exactly 3 distinct ORIGINAL incidence IDs, NOT a historical six-ID Q. Positivity of T, including Omega(s^6), is deliberately NEVER called root PROVED_A.

### Proof (all h, all f,g)

1. Minimality of a gives C(a-1,2)<V<=C(a,2), so H=C(a,2)-V is an integer with 0<=H<=a-2. Every k-coordinate clique has C(k,2) potential physical edges; any globally injective full f omits only H physical edges in the WHOLE K_a. Consequently |P_X|>=m, and independently |L_Y|>=m, for **every** X,Y, even when f and g are perfectly correlated. No random-label assumption.
2. s>=8 gives V>=(9)(65)=585, hence a>=35 (indeed C(34,2)=561<585). In particular a>=22. Since k=floor(a/2), C(k,2)>=(a-1)(a-3)/8. Therefore

       m >= (a^2-12a+19)/8 >= a(a-1)/16 = K/8 >= V/8,

   where the middle inequality is equivalent to a^2-23a+38>=0, true for every a>=22 (increasing there and positive at 22). Also V=(s+1)(s^2+1)>=16(s+1).
3. Write x=|P_X|, y=|L_Y|, and e=e_G(P_X,L_Y) actual original incidences crossing these TWO immutable original factor subsets. Degree s+1 on BOTH true original sides yields e<=(s+1) min(x,y). Thus

       T=xy-e >= xy-(s+1)min(x,y)
         >= m(m-(s+1))
         >= (V/8)*(V/8-V/16) = V^2/128.

   The second inequality holds because x,y>=m>=s+1 and xy-d min(x,y) is monotone separately on that quadrant. Finally V=(s+1)(s^2+1)>s^3 implies V^2/128>s^6/128.
4. By the genuine GQ nonincident-point/line axiom, every nonincident (p,l) has exactly ONE intermediate pair (l0,p0) with flags (p,l0),(p0,l0),(p0,l). The original incidence graph has girth 8, so the three edges are different and constitute a simple length-three path. Distinct endpoints give distinct paths. Conversely an original simple three-edge p-to-l path cannot close onto an already incident p,l (it would give a source 4-cycle); thus T counts exactly these true original simple paths. Crucially no six-ID Q appears in this step.

This proves the **macroscopic source anchor count only**. It is compatible with S_s=o(s^6), S_s=Omega(s^6), and both as-yet-unsettled root alternatives.

## 3. Stronger all-h SIX-DISTINCT-original-flag SOURCE B/B-overlap extension

The macro 3-path supply can be turned into a **sixflag ORIGINAL SOURCE configuration** theorem, but NOT into any count of sixflags accepted on the physical GF5 projections. The accepted historical B/B-overlap source forest class has path component lengths (3,1,1,1), according to the already documented genuine-original 9-cell classification in prior D6-AA4-U/PR #486. The source path and its three matching isolated flags have exactly this source profile.

Fix one genuinely original simple 3-edge path from the theorem (p,l0),(q,l0),(q,l), with original POINT vertices p,q and LINE vertices l0,l. Among all N=V(s+1) original incidence flags, exclude all flags touching these FOUR original source vertices. There are at most 4d excluded flags, d=s+1. Choose an extra flag e1; then disallow its two original source endpoints (at most another 2d flags). Choose e2, disallow its endpoints (another 2d); choose e3. Counting ordered triples of pairwise endpoint-disjoint actual original flags gives at least

    (N-4d)(N-6d)(N-8d)

valid triples. Each UNORDERED choice of three different singleton flags occurs 3!=6 times. It produces a TRUE six-DISTINCT-original-incidence-ID source forest containing the existing source path of length 3 plus THREE source-isolated edges. Both original typed multiplicity patterns are B=(2,1,1,1,1); the unique repeated original POINT is q, the unique repeated original LINE is l0, and they intersect in the ACTUAL ORIGINAL central flag (q,l0), giving B/B-overlap. The source sixflags are not automatically physically degree2. Conversely each original sixflag SOURCE forest of shape (3,1,1,1) has a **unique** such source 3-edge component, with a unique ordered (original point, original line) nonincident pair of path endpoints. Thus no source Q is counted twice across different anchored paths.

Let U_BBo(X,Y;f,g) be the number of distinct true ORIGINAL source sixflag Q of this forest shape whose unique source 3path point endpoint lies in P_X and LINE endpoint in L_Y. For ALL s=2^h>=8, ALL complete globally injected arbitrarily correlated f,g, ALL physical halfcoordinate cuts X,Y:

    U_BBo(X,Y;f,g)
       >= T(X,Y;f,g)*(N-4d)(N-6d)(N-8d)/6
       >= V^2*d^3*(V-4)(V-6)(V-8)/(128*6)
       > s^18/6144.

The final inequality uses d>s, V>s^3 and V-8>s^3/2 (s>=8). This is **universal source-only Omega(s^18)** for exact original sixflag incidence forests of the B/B-overlap SOURCE class. Historical accepted B/B-overlap GF5 motifs would require **both** associated physical sixcoordinate degree2 tests simultaneously under SAME fixed f,g. Neither those tests nor GF5 positivity is included in U_BBo. We do NOT divide U_BBo by a conjectural acceptance probability.

**Precise missing acceptance gate:** A proof that at least c/s^12 of THESE anchored true original B/B-overlap sixflag sources pass the full two-sided historical GF5 class test (for all f,g, with c>0 independent of h) would IMPLY the root Branch A bound S>=c*s^6/6144, because the physical and source overlap tags agree for accepted B/B-overlap Q. This is a **sufficient** condition, NOT equivalent to Branch A: other accepted GF5 classes could force S even when this B/B channel is empty.

Independent FULL real-original W(3,2) W32 unit test enumerates every genuine source p-to-l nonincident 3path and every matching triple of real extra source incidences, and reconstructs 910080 distinct original sixflag SOURCE B/B-overlap Q, exactly matching prior source-only 9-cell census in AA4-U. Each of its V(V-d)=180 source 3path anchors has 5056 exact original matching triples, and the test separately checks source Q uniqueness, point/line degree patterns and the restricted physical halfcoordinate endpoint cut ledger for complete W32 lex and S72 source maps. These numbers are **source-only** and do NOT equal W32 physically GF5-accepted B/B-overlap (which is much smaller and map-dependent). Numerical h=1 test validates the combinatorial construction, not the h>=3 uniform constant.

## 3. Cubic identity and why plain spectral mixing does NOT bridge GF5 micro-palettes

Let M be the actual V x V (0,1) point/line ORIGINAL incidence matrix, indexed by original IDs. For a NONINCIDENT pair (p,l), the number of length-three walks equals one, as proved above; for an INCIDENT pair, the walks either immediately backtrack at the point (s+1 choices of first line) or backtrack at the line (s+1 choices of middle point), with exactly one walk doubly counted, hence 2s+1. Thus the exact integer identity is

    M M^T M = J + 2s M.

By regularity M 1=(s+1)1, M^T 1=(s+1)1, this gives nontrivial singular values sqrt(2s) or zero; the trivial one is s+1. Hence ordinary expander mixing for ANY original point set P and line set L of sizes x,y is

    |e(P,L)-(s+1)xy/V|
        <= sqrt(2s)*sqrt(x(1-x/V)*y(1-y/V)).

A PHYSICAL six-coordinate palette holds at most C(6,2)=15 different original factor physical pair images on EACH typed side by global injectivity: x,y<=15. For every s>=4, V>15, and

    sqrt(2s)*(V-15) >= 15(s+1).

Therefore for EVERY nonempty x,y<=15,

    sqrt(2s)*sqrt(x(1-x/V)*y(1-y/V))
        >= (s+1)xy/V.

**The standard single-cut second-singular-value inequality gives a NONPOSITIVE lower for e(P,L), even for one original flag on a given six-coordinate physical palette.** It cannot, *by itself*, force the far more structured two-sided same-original-sixflag GF5-positive joint. This is a rigorous insufficiency of THIS PARTICULAR scalar spectral inequality at the required palette resolution — NOT an impossibility theorem for all spectral/tensor/6th-order methods, and NOT a lower/upper result for S.

The arithmetic micro condition follows from 2s(V-15)^2>=225(s+1)^2: true already for s=4 (V=85) and increasing faster for larger s. The formula is squared only with nonnegative quantities.

## 5. Reproducible genuine-original tests and two independent mathematical oracles

Files:
- research/hyp105_issue230_d6aa4cq_original_macro_path_cut_gate.py — validates complete actual ORIGINAL maps and full incidence degrees, computes two independent transposed direct true-original cut incidence sums, genuine nonincidence count, macro and micro exact integer gates.
- research/test_hyp105_issue230_d6aa4cq_original_macro_path_cut_gate.py — an **independent** walk enumerator, testing p--l0--q--l on real source line/point stars rather than inferring it from nonincidence; catches a violation of the GQ cubic identity. Explicit literal source incidences and distinct complete maps remain fixed for ALL paths and cuts.
- .github/workflows/hyp105-issue230-aa4cq-path-cut-gate.yml — GitHub-hosted Python 3.12 partitioned tests.

The executable original geometries are genuine symplectic W(3,2), W(3,4), W(3,8), imported via the already-existing original fixture and independently checked by actual point-to-line star traversals. For W32/W34, EVERY (p,l) pair on lex/S72 (W32) AND lex/random (W34) original maps is checked for 1 or 2s+1 walks; W38 checks deterministic diverse endpoint blocks. For each true original geometry and both complete maps, four independently fixed physical half-coordinate cut pairs (including disjoint, reversed and shifted) are checked by exact nonincidence enumeration and distinct 3-walk reconstructions. A second global typed incidence transpose independently checks e(P,L). Adversarial invalid source incidence deletion, repeated global physical labels and malformed cut coordinates must fail closed. A further independent literal W32 sixflag B/B-overlap source matching enumeration reconstructs 910080 previously catalogued original Q and asserts no duplicated anchored source Q under the same fixed complete maps. Pure integer independent arithmetic checks cover h=3..12 and all positive x,y<=15 exact micro inequalities cover h=2..5.

**Scope restrictions:** The h<=12 automated arithmetic run is a regression, not a substitute for the symbolic all-h proof. No search over all f,g; no W38 full seven-GF5 census (AA4-CP explicitly does not support that). No altered accepted GF5 51-column weights, no source-ID redrawing, no false claim of a sixflag motif from a threeflag path.

## 6. Hard missing mathematical transfer (next gate)

To advance root #230, establish a **uniformly positive source-to-PHYSICAL SIXFLAG transfer**, simultaneously across BOTH true typed global maps and historical GF5 positions. The current source 3path + three independent actual flags construction proves at least s^18/6144 genuine sixflag B/B-overlap SOURCE forest configurations in every halfcoordinate cut, but DOES NOT enforce either physical 2regular sixcoordinate property. Prove a uniform c/s^12 physical accepted fraction of THIS same-source-BBo collection (a sufficient, not necessary, criterion for root A), or establish a different joint sixflag lower across the other six accepted classes. Equivalently, find and independently certify a different all-h mechanism forcing one of the accepted non-AA source cells. The current result supplies a large reservoir but **NO minimum completion multiplicity**, and AA4-Q/AA4-U already show marginal/independence methods fail.

Proof acceptance status **DOCUMENTED_IN_DRAFT / DERIVED_CLASSICAL** pending independent qualified mathematical review, exact PR-head hosted dedicated and general CI, and ancestor stack acceptance. Root remains **OPEN_WITH_FORMAL_BLOCKER**. Neither A nor B nor qualifying root-equivalent C is claimed.
