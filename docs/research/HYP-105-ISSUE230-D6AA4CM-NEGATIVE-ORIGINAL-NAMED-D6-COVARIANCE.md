# HYP-105 / #230 — AA4-CM: negative historical D6 covariance from TWO genuine-original sixflags under ONE correlated 96-map POINT orbit

**Scientific Draft**, strict child of [AA4-CL PR #612](https://github.com/definitely-stable/Mathlab/pull/612), parent exact HEAD `19ee07ae3836661821647c6665b844d38da5405b`. Do not modify main or accepted historic seven-GF5 registry. Root #230 **OPEN_WITH_FORMAL_BLOCKER**.

## Mathematical objective, prior art, decision

#612 AA4-CL established exact covariance of two ENTIRE source-POINT-A sixfactor families sharing four genuine original POINT factors, within the same 96 legal complete original f maps, and the upper bound `|Cov|²≤(9/16)D4(u)D4(v)`. Its positive W32/W34/W38 examples and one zero W34 example do **NOT** establish universal nonnegative covariance, mandatory GF5 compensation, or arbitrary fixed-map S>=c s6.

**AA4-CM proves a strict NEGATIVE signed historical D6 covariance for TWO SELECTED TRUE-original six-ID Q**, with the same eight genuine original POINT factor IDs and one whole complete injected f,g. The two Q use four common original POINT factors but **zero common original incidence IDs**: at every shared original POINT source ID the two sixflags use **different actual original LINE source IDs**. This distinction from #607's four-common-INCIDENCE-ID construction is vital. Do not conflate the selected two-Q contribution with the HISTORICAL full-source POINT-A sixflag family score or complete all-seven S.

The underlying finite-cycle pigeonhole argument, Hall marriage and covariance of disjoint indicator supports are classical elementary combinatorics. The issue-specific increment is an **all-h realizable genuine W(3,2^h), globally injected complete f,g** sign counterexample, with two distinct actual source Q whose original same-incidence-column GF5 D6 classifier (weight5643) is evaluated for each of 96 coherent global whole-POINT source image permutations; no per-Q image redraw and no source-Q independence assumption.

## 1. ALL-h conditional graph geometry

For every h>=2, s=2^h, the minimal physical edge-label alphabet a satisfying C(a,2)>=V=(s+1)(s²+1) has a>=12 (indeed a>=14 when s>=4). Choose eight different actual original POINT factor IDs `p0..p7` and complete a GLOBAL injected source f with their physical images

```text
p0  01      p4  45      p6  46
p1  12      p5  05      p7  06
p2  23
p3  34
```

These eight complete original POINT factor physical pair images are DISTINCT and give TWO connected sixedge physical C6 families `A=(p0,p1,p2,p3,p4,p5)`, `B=(p0,p1,p2,p3,p6,p7)`, both using ONE unchanged complete original f map. Their four common original POINT image edges have the physical fifth-vertex cherry replacement structure from #607.

Apply the single jointly legal complete original f permutation subgroup `G=S4(p0..p3)×S2(p4,p5)×S2(p6,p7)`, 24×2×2=96 legal GLOBAL f maps, and keep ONE complete global original LINE map g untouched.

Every state `x=(sigma,alpha,beta)` yields an ORIGINAL labeled six-position physical left C6 dual `C_A(x)` and `C_B(x)`. The first depends on sigma,alpha, not beta; the second on sigma,beta, not alpha. Exact literal 96-map enumeration reveals **24 different labeled dual cycles for A and 24 for B, each appearing at exactly FOUR of the 96 states**.

Thus the 24×24 pairs (c_A,c_B) of individually realizable right labeled D6 cycles yield 576 possible choices. For any fixed c_A its four f states can co-occur with right B cycles at no more than four of B's 24 different orbit types. Therefore at least 20 c_B choices are simultaneously REALIZABLE somewhere but NEVER at the SAME complete f state as c_A. In the concrete cherry completion geometry, exact enumerator finds **528 out of 576** pairs with disjoint accepting state supports, giving strict negative covariance of the two named positive D6 indicator functions.

## 2. All-h ORIGINAL incidence Hall matching and globally injected correlated f,g

Use two actual true original incidence flags at each of the four shared POINT sources p0..p3, with TWO DIFFERENT original LINE sources; use one true original flag at each exclusive source p4,p5,p6,p7. These are exactly twelve original flag slots at eight original POINT factors. In a genuine original symplectic GQ W(3,s), each source POINT is incident with s+1 distinct LINE factors, and any two different original POINT LINE-neighbor stars meet in at most ONE LINE.

For ANY nonempty subset of the twelve slots, if its POINT support contains:
- one POINT: ≤2 requested slots and ≥s+1≥5 original available LINE neighbors;
- two POINTs: ≤4 requested slots and ≥2(s+1)−1≥9 neighbors;
- at least three POINTs: ≤12 total requested slots and ANY three of their original LINE stars contain at least 3(s+1)−3≥12 different LINE neighbors by simple 3-set inclusion-exclusion lower bound.

Hall's marriage theorem therefore gives TWELVE globally DISTINCT real original LINE source factor IDs, each truly incident with its corresponding POINT. This holds for EVERY h>=2; no independent original Q redraw or synthetic bipartite incidence generator.

Form two genuine six-distinct-original-incidence sets Q_A and Q_B with six selected slots in each family; every Q is source POINT-A / LINE-A. The Q share four original POINT source IDs but ZERO original incidence IDs, because their four shared POINTs each select different TRUE original LINE IDs. Hence these two Q are different and entirely disjoint original 6flag subsets of the genuine GQ.

Select one c_A,c_B pair of actual reachable left-dual types with **no jointly accepting f state**. Build original complete globally injected g as follows:
- map the SIX ACTUAL original LINE factor IDs used by Q_A injectively to the six edges of a physical right C6 on physical coordinates `0..5` whose six original flag-position dual is EXACTLY c_A;
- map the SIX OTHER real original LINE factor IDs used by Q_B injectively to a DISJOINT physical right C6 on physical coordinates `6..11`, with original position dual c_B;
- injectively complete all remaining original LINE source factors using unused physical K_a simple edges. Since the two chosen right cycles use disjoint coordinate alphabets, all 12 selected physical right edges are distinct. The complete f and g are globally injected separately; g is the SAME WHOLE original map under all 96 global f permutations.

For one fixed true ORIGINAL sixflag Q in source A/A, the immutable historical selected seven-GF5 classifier returns `D6` iff its left actual physical C6 incidence-position dual equals the right actual C6 dual. Define **named positive weighted indicator** `X(x)=5643 I_D6(Q_A;f^x,g)`, likewise `Y(x)=5643 I_D6(Q_B;f^x,g)`. Each is nonzero at exactly 4/96 actual complete globally legal original f maps, but NEVER both nonzero:

```text
E_G X = E_G Y = 5643/24;
E_G[XY] = 0;
Cov_G(X,Y) = -5643^2 / 576 = -31,843,449/576 < 0.
```

**This is an all-h EXISTENTIAL true-original mathematical counterexample to a universal NONNEGATIVE covariance claim for two selected historical accepted D6 source-Q contributions.** It is NOT a counterexample to a nonnegative covariance claim about their ENTIRE source-POINT-A fibers (which may include many other genuine original Q and historical source-right B/C classes), and NOT a construction with globally small `S_s(f,g)=o(s^6)` or root Branch B.

## 3. Independent finite true symplectic original W34 and W38 falsifiers

The original W34 (s4,V85,425 real incidence IDs,minimal physical K14) and W38 (s8,V585,5265 real incidence IDs) tests reconstruct actual source LINE stars and run independent augmenting-path matching for the 12 original LINE factor slots. They construct ONE whole original f with the two overlapping left C6s, and one **FULL globally injected** original g with 12 pinned original LINE images forming two disjoint physical right sixcycles, then complete all other source factor IDs injectively. Both true Q_A and Q_B have SIX DISTINCT actual original source incidence IDs, 12 distinct flags collectively, four common true POINT factors and ZERO common true incidence IDs.

For **EACH** 96 global original f map states, independently reconstruct literal left and right physical six-coordinate degree-2 original incidence-position dual graphs from actual original Q and full f,g and test connectedness/equality WITHOUT using the generalized historical sevenclass tagger. Separately compare with the independently authored true-original historical seven GF5 tagger on each Q; all 192 comparisons per geometry agree, each original Q historically D6-positive in exactly four states and NEVER together. The exact negative rational covariance is independently recomputed.

A SEPARATE test enumerates the ENTIRE historical accepted original source-POINT-A sixflag score for BOTH complete sixfactor families on the **SAME 96 whole f maps**, not just the two pinned Q, and compares its actual covariance to the negative named-Q covariance. It makes NO universal claim about the sign of the whole-fiber covariance without observed evidence; the entire original full-seven S across ALL source-Q types is not computed. If the entire original covariance is positive or zero for this witness, that is a substantive barrier against lifting the named-Q negative sign to the full set of real original motifs.

The pure 96-map code also independently checks all 24 source-original dual bins per family and all 576 pair orientations, exact 528 disjoint-support right dual type pairs and covariance `-5643²/576` without floating point.

## 4. Scope, prior art, next scientific gate

No new generic theorem about covariance of disjoint indicator supports or Hall marriage is claimed. Existing #608 provided original D6 fan erasure, #609 exact source fiber dual hist, #610 exact global POINT swap class flux, #611 one-fiber spectral energy, #612 twofiber covariance and a zero full-fiber counterexample. This new AA4-CM detects a genuinely **negative** covariance in actual original GF5 historical named Q from the SAME coherent complete original map orbit, establishing that even pairwise GF5-positive selected motifs need not be synchronously realizable at a common global f. The negative sign cannot be inferred merely from the positive original physical right 2factor support.

To close root Branch A one needs a uniform lower bound for COMPLETE global original all-seven `S_s(f,g)` for EVERY fixed f,g, not signed covariance of a chosen finite Q pair over a subgroup orbit. It remains possible for other original Q and source types POINT-B/C to compensate. This work neither proves universal original `Omega(s^6)` nor constructs a qualifying infinite `o(s^6)` correlated original pair sequence nor root-equivalent Branch C or full R3/ASET. Root remains `OPEN_WITH_FORMAL_BLOCKER`.

**Next research gate:** independently test whether a strict negative covariance of the TWO COMPLETE source POINT-A fibers is realizable on a full original W34/W38 through an adversarial yet globally injected original LINE g, and if yes, derive the exact cross-fiber signed-compensation bounds involving true source-POINT-B/C Q. If NOT found, the distinction between named and entire-family covariance is itself a reason to investigate mandatory extra original Q arising from genuine GQ incidence and complete injections. Keep DRAFT pending exact-head GH-hosted CI, qualified independent math referee, and actual parent chain integration.
