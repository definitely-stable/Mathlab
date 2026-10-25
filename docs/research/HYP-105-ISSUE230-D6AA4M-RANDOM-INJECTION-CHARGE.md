# HYP-105 / issue #230 — D6-AA4-M: exact random GLOBAL-injection GF(5) charge expectation

**Status: ALL-h rigorously proved STOCHASTIC/EXISTENTIAL source-charge theorem; deterministic all-label lower remains OPEN_WITH_FORMAL_BLOCKER.** This slice is not another W32 finite radius expansion and not a claim that all admissible f,g have positive or Ω(s⁶) charge. It derives exact closed-form uniform complete-injection probabilities for genuine ORIGINAL B-left/A-right seven-GF5 motifs and a real ORIGINAL concurrent pair within each such motif, independent of any locally inconsistent Q label choice.

Research-only stacked Draft on [D6-AA4-L / PR #462](https://github.com/definitely-stable/Mathlab/pull/462) at pinned parent `03e36698072196a6c2ba715dd9391d797cd7e272` (all four hosted workflows SUCCESS). All writes to child research branch only; do not merge main or close #230.

## 1. Why this is a nontrivial next all-h source/physical coupling result

AA4-I proves ≥s⁵/4 original GQ-collinear but physically-disjoint source pairs per typed map for s>=4. AA4-K sharpens actual accepted GF5 source pair→positive sixset charging to I_L<=9 S and I_P+I_L<=18S. AA4-L builds an actual genuine positive W(3,8) D6 sixset with ZERO source pair charge on BOTH types, and establishes exact finite 0/1 pair–positive-Q Gram/moment oracles. None gives a universal deterministic lower I>=c*s⁶.

EICE-003-I / PR #465 and local-transfer-barrier PR #466 prove additional genuine source-square and five-flag local limitations; their accepted conditions cannot be silently promoted to GF5 seven-positive Q. Here we deliberately choose a simpler family with **exact and unconditional physical projection positivity**: every original sixset whose source point multiplicity pattern is B=(2,1,1,1,1) and line pattern A=(1,…,1) becomes an accepted historical B-left/A-right seven-GF5 motif whenever its two independent globally assigned physical half-projections are degree two on six physical coordinates. No physical proper-P3, square closure or extra source-pencil anchoring is assumed. The concurrent source-line pair is genuine because both incidences share a REAL original point; its physical disjointness is separately verified.

## 2. ALL-h exact source B(point)/A(line) sixset lower, NO labels assumed

Fix actual W(3,s), s=2^h>=2. Let V=(s+1)(s²+1), d=s+1, N=Vd distinct original point-line incidences. Choose a genuine ORIGINAL point p (V choices), then a pair of distinct original lines l0,l1 incident with p (C(d,2) choices). Choose in order four MORE true ORIGINAL flags (q_j,m_j), with four distinct new ORIGINAL points q_j!=p and four distinct new ORIGINAL lines m_j different from l0,l1 and one another.

After j such flags, at most (1+j)d original incidences have any already used original point and at most (2+j)d have any already used original line. Their union therefore removes no more than (3+2j)d of the N actual original incidence IDs. The jth choice has at least d*(V-3-2j) legal candidates, for j=0,1,2,3, each positive for ALL s>=2.

The repeated original point p is UNIQUE in the resulting sixset Q, and l0,l1 are its unique two incident chosen flags, while the other four flags are unordered. Every Q is counted exactly 4! times by its four ordered additional flags and exactly once by its p,l0,l1 root. Hence the number N_BA(s) of true original source-incidence sixsets with point multiplicity B and line multiplicity A satisfies

[
oxed{N_{BA}(s)ge
M_s:=rac{Vinom d2}{4!}
prod_{j=0}^{3}d(V-3-2j)>0.}
]

This is a rigorous genuine all-h source-incidence theorem, not a count of seven-GF5 accepted motifs for a single f,g. At W32 the oracle independently enumerates every actual source B/A sixset by root point/two-line pair and four additional genuine incidence IDs, and compares against M_2.

## 3. Independent UNIFORM FULL injections and exact physical A/B probability

Let a be the **minimal** physical coordinate alphabet size with K=C(a,2)>=V. Choose f, g independently and uniformly from ALL complete separately typed-injective maps from original V point/line factors to K physical pair labels, not one mapping per Q. For ANY fixed sixset Q of the above true source B/A class, five distinct original source point factors have uniform ordered injective physical K-edge labels, and six distinct original source line factors have an independent uniform ordered injective physical K-edge tuple.

For the SIX original right line physical edges to form projection A (degree two on exactly six coordinates): choose the six coordinate symbols C(a,6), one of 70 unlabeled 2-regular simple six-edge graphs on these coordinates (60 genuine C6 and 10 disjoint two-triangles), then assign the six physical edges to the six originally named source lines in 6! orders. Therefore exactly

[
p_A=rac{inom a6,70,6!}{(K)_6}.
]

For the source LEFT point B projection, the original point p occurs TWICE. Choose its physical repeated edge (K choices); choose four additional coordinate symbols disjoint from the two endpoints of p's physical edge (C(a-2,4) choices); choose one of 3 C4 edge sets on those remaining four symbols; assign those four distinct physical edges to the four other originally named source points in 4! orders. Therefore exactly

[
p_B=rac{Kinom{a-2}4,3,4!}{(K)_5}.
]

Here (K)_r is the descending falling factorial. Since independent complete f/g globally injected maps induce these exact marginals and accepted historical tag B-left/A-right has NO extra cross-half condition, every fixed genuine source B/A Q is accepted seven-GF5 with exact probability p_B*p_A. This is a genuine expectation for one SHARED globally coherent random map, justified by LINEARITY OF EXPECTATION, never by independent physically labeled Qs:

[
oxed{mathbb E_{f,g}, S_{BA}(f,g)=N_{BA}(s)p_B p_Age M_sp_Bp_A.}
]

Every such ORIGINAL source B/A Q has exactly TWO genuine original lines l0,l1 through repeated point p; the lines CONCUR at the original point. Conditional on projection A for these SIX distinct original line physical labels, the six edges have exactly nine disjoint unordered pairs among all C(6,2)=15; by uniform label-exchangeability every particular original line pair is physically disjoint with probability 9/15=3/5. The event of accepted LEFT B is independent of all line-edge image data. Therefore for the TRUE AA4-J/AA4-K original concurrent, physically-disjoint source-pair charge, the **internal B/A contribution** I_L^{BA,int} is counted once per actual positive Q whenever its two real original lines l0,l1 have disjoint physical images:

[
oxed{
mathbb E_{f,g}, I_L^{BA,mathrm{int}}
=rac35 N_{BA}(s)p_Bp_A
gerac35 M_sp_Bp_A.}
]

The right-hand side is an exact positive finite rational bound FOR EVERY s=2^h>=2. It involves TRUE original source GQ incidences, the accepted seven-GF5 B-left/A-right event, and complete GLOBAL injections. No pseudo-marginals, incomplete physical assignments or synthetic local Q events appear.

## 4. ALL-h stochastic Ω(s⁶) and an honest EXISTENTIAL consequence

As s tends to infinity over powers of 2, V~s³, d~s, and minimal a~sqrt(2)s^(3/2), K~s³. Elementary substitution in the **exact** rational expressions gives

[
M_s=(1/48+o(1))s^{21},quad
p_B=(12+o(1))s^{-6},quad
p_A=(560+o(1))s^{-9}.
]

Therefore:

[
oxed{mathbb E, S_{BA}ge(140+o(1))s^6,qquad
mathbb E,I_L^{BA,mathrm{int}}ge(84+o(1))s^6.}
]

Thus for all sufficiently large s there exists AT LEAST ONE genuine separately globally injected pair of maps (f,g) with `I_L(f,g)>= (84+o(1))*s^6`. This is a **high-charge existence witness by averaging**, never an all-maps minimum theorem. In particular, the random-model expectation does not preclude a sparse/low-charge adversarial assignment and does not prove root Branch A; the previously pinned s=2 zero-charge original line pair and s=8 zero-charge positive D6 Q remain valid.

This changes the research question from mere positive-charge possibility to a genuinely difficult **anti-concentration/minimax source-energy problem**: determine whether an adversary can suppress the real B/A internal source charges across all original incidence stars SIMULTANEOUSLY while respecting BOTH complete physical edge injections and all true ORIGINAL GQ incidences. Finite W32 realizations of the exact B/A class can diagnose this but cannot establish uniform s>=4 behavior.

## 5. Independent actual ORIGINAL W32 acceptance and controls

The new oracle evaluates the exact s=2 physical pattern counts directly by enumerating ALL 70 simple 2-factors on K6 and all K6 repeated-edge+C4 patterns (15*3=45 unoriented B physical configurations). It independently counts the exact genuine original W32 source B/A candidate sixsets, not by sampling physical maps but by literal true source root point/two-line pencil and four distinct original flag completions. The true exact uniform expectation is `N_BA*p_B*p_A` and exact internal charge expectation `3/5*N_BA*p_B*p_A`; independent probabilistic CI assertions validate the parameter-free formula.

Additionally for pinned S68 and S72 choose the genuine first four-POINT ORIGINAL source critical transversal, freeze all other factors, enumerate every one of the 24 globally injected typed label completions, and at every map run historical accepted GF5 `seven_census` of all 62,370 ORIGINAL W32 six-incidence candidate sets. For each real B-left/A-right Q independently identify its actual repeated original point, its TWO distinct original source lines incident with that point, and the disjointness of their assigned right physical edges. Assert internal line charge <= total exact AA4-K independently reconstructed line charge; record min/max of actual B/A class count and direct pencil charges.

**Protocol separation:** these 24 maps are a tiny fixed-outside fiber. Their AVERAGE is NOT the mathematical random expectation across ALL (15!)² complete W32 type bijections, and CI must assert no equivalence. The all-h probabilistic identity holds for fully independent uniform complete maps on the whole original geometry, not finite 24-state restricted labels or an independently chosen map per Q.


### Exact complete ORIGINAL W32 source count — independently hosted result

The independently implemented brute combinatorial source-incidence enumerator (NO physical GF5 classification in this count) verified that the genuine 45-incidence W(3,2) contains EXACTLY **1,666,980 distinct six-incidence sets of original point multiplicity B and original line multiplicity A**. There are 45 original choices of the repeated point and its pair of incident lines; all 45 root selections have EXACTLY **37,044** legal unordered four-flag completions. The valid all-h conservative greedy bound specializes to M_2=874,800, strictly below this true exact count. This is a count of potential ORIGINAL source configurations, not a claim that all are positive simultaneously.

Substituting EXACT fully uniform K6 physical-bijection probabilities gives independently checkable exact true-original W32 random-map expectations:

[
mathbb E_{mathrm{uniform FULL} (15!)^2} S_{BA}
=rac{1,428,840}{20,449}approx69.8733,qquad
mathbb E I_L^{BA,mathrm{int}}
=rac{857,304}{20,449}approx41.9240.
]

These are expectations over ALL full separately type-injective physical K6 edge-label bijections, NOT over the 24-source-factor frozen-outside fibers. Since any full map includes one shared injection f and one g across all Q, these expectations remain valid without assuming independent positive sixsets. The exact count supplements but does NOT improve the all-h leading 140/84 coefficients; the all-h formula uses only conservative M_s.

## 6. Limits and next research

This is a rigorous new use of exact random global injection probabilities for the specific accepted original B/A GF5 class; elementary enumerative probability and probabilistic method are standard and not claimed newly discovered general mathematics. Scientific value is an explicit all-h leading 84s⁶ lower for the AVERAGE actual original source-pair charge, showing the required scale is naturally present in real globally injected maps. It does not solve the adversarial minimum and supplies NO lower `I_P+I_L=Ω(s⁶)` for EVERY map.

Next D6-AA4-N: study a **uniform** lower bound on actual B/A internal charge, or independently construct a family of globally injective maps suppressing this particular B/A charge, using source-original point-pencil concentration, full physical C4/2-factor constraints, and EICE-003-I/PR #466 valid local falsifiers. Attempt an exact variance/covariance or conditional-expectation amplification over ORIGINAL source-incidence overlapping sixsets, rather than assuming random-mean=>every map. The source matching and acceptance oracles must stay genuine; no arbitrary independent Q relabeling, no physical-proper P3 proxy, and no unearned all-h S≥cs⁶ theorem.

Four research-only files, GitHub-hosted independent all-h theorem + original finite scheme matrix CI; require all four exact-head workflow gates and independent math peer review before acceptance. Root #230 OPEN, full R3/ASET exponent NOT proved, main never modified.
