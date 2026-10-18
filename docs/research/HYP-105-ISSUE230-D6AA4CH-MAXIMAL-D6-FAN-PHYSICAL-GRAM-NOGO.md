# HYP-105 / #230 — AA4-CH: maximal original D6 fan and a physical-only compensation NO-GO

**Scientific Draft**. Parent [AA4-CG PR #607](https://github.com/definitely-stable/Mathlab/pull/607), pinned exact parent SHA `d351863151eab9f3eb38129e040b3565216f09c6`. No changes to main, historical 7-class GF5 registry, accepted theorem ledger or root issue status. Issue #230 **OPEN_WITH_FORMAL_BLOCKER**.

## Research question, frontier and why AA4-CH

HYP-105 Branch A requires a uniform ORIGINAL fixed-map `S_s(f,g)=Omega(s^6)` for ALL dyadic s and arbitrary correlated complete globally injected typed maps f,g, using the SAME SIX DISTICT TRUE ORIGINAL incidence IDs on both sides and all historical seven positive GF(5) classes. Branch B requires an explicit genuine original infinite correlated o(s^6) sequence; C requires an actual root-equivalent reduction.

Recent original #605 established one fixed-sixpacket physical XOR convolution and Gram. #606 established a five-common-packet 2factor no-go. #607 proved a four-common-packet dichotomy and existence of TWO simultaneously D6-positive original sixflags for every h>=2 by Hall marriage. These statements concern actual physical necessary conditions and narrow original-source witnesses; NONE transfers physical Gram constraints to all-seven historical GF5-positive abundance.

**New gap:** Does a physically coeligible original sixflag reservoir force historically positive sixflags when right physical supports, one complete LINE map g, and original f-side physical 2factor eligibility are frozen? The answer is **NO even for an extremal all-h fan**. AA4-CH builds a maximal `s+1` size exact D6-positive original fan and erases all of its actual historical seven-GF5 positives with ONE global source POINT-image transposition **without changing any right physical mask, right mixed Gram, occupied f edge set, or physical left sixcoordinate 2factor eligibility of any fan Q**.

Related prior original Mathlab #570 demonstrates other high-multiplicity original D6 constructions and #584–586 multi-cherry repair opportunities; neither means a physical-only mixed Gram already implies historical positivity at the SAME unchanged original f,g. The combinatorial argument uses classical Hall matching, generalized quadrangle point-star intersection and a classical sixcycle permutation; those ingredients are not generally new. The precise fixed-original-fan erasure / matched physical-geometry negative-transfer theorem and accompanying fully original W34/W38 oracles are the research slice.

## 1. ALL-h constructive maximal TRUE original D6 fan

For EVERY h>=2, s=2^h, let the actual original symplectic generalized quadrangle `W(3,s)` have V=(s+1)(s²+1) real POINT and LINE source factor IDs, each with s+1 original incidence flags. Every two distinct original POINT LINE-star neighborhoods have at most one common LINE. In fact, there exist noncollinear POINT source factors p4,p5 whose LINE stars are DISJOINT: for each given p4 there are exactly s³ noncollinear other POINTs. Choose four further distinct genuine POINT factors p0,..,p3.

Set m=s+1. Require ALL m original LINE flags at p4 and ALL m at p5, hence 2m distinct LINE factors because the stars are disjoint. To obtain four EXTRA common original LINE flags at p0,..,p3 that do not reuse these 2m factors, each of the four anchor POINT stars has at least `(s+1)-2=s-1` remaining LINE factors: it shares at most one with p4 and at most one with p5. Any two residual anchor LINE stars intersect in at most one original LINE. For any k in {1,2,3,4} anchors, inclusion-exclusion's first two terms give a union size ≥k(s-1)-C(k,2). Since s>=4, this lower bound is ≥k. Hall's marriage theorem therefore gives FOUR DISTINCT anchor original LINE IDs, all disjoint from the two complete heavy stars.

Let `L_i` (i=0..3) be these selected anchor LINE IDs; and enumerate the complete two noncollinear LINE stars as `L_{4,j}`, `L_{5,j}`, j=0..s. Define the EXACT same real original four fixed incidence IDs `(p_i,L_i)` i=0..3, and `m=s+1` **different SIX-DISTINCT original incidence ID sets**

```text
Q_j = { (p0,L0),(p1,L1),(p2,L2),(p3,L3),
        (p4,L4,j),(p5,L5,j) },  j=0,...,s.
```

Every pair of DISTINCT Q_j,Q_k shares EXACTLY four TRUE ORIGINAL flags. All m sixflags use six DIFFERENT original POINT factors and six DIFFERENT original LINE factors, so they lie in original source A/A. Their entire original source incidence flags, not independently remapped artifacts, are fixed.

The minimal physical alphabet size a is the least integer with C(a,2)>=V. For s>=4, `C(s+5,2)<V`, so a>=s+6. Therefore all distinct physical coordinates 0,..,s+5 exist. Select complete arbitrary but INJECTIVE f and g with the following pins, filling all other ORIGINAL source factors using the remaining unordered K_a pair edges:

```text
f(p0)=01,  f(p1)=12,  f(p2)=23,
f(p3)=34,  f(p4)=45,  f(p5)=05.

g(L0)=01, g(L1)=12, g(L2)=23, g(L3)=34,
g(L4,j)={4,5+j}, g(L5,j)={0,5+j},  j=0,...,s.
```

All pinned original f and g physical pair images are pairwise distinct WITHIN their typed maps; both completions are globally injective since `C(a,2)>=V`. Note g uses `4+2(s+1)=2s+6` actual distinct LINE images; in particular none is redrawn depending on j.

For each genuine sixflag Q_j the physical POINT projection is the SAME connected C6 `01,12,23,34,45,05` on physical vertices 0..5. The physical LINE projection is `01,12,23,34,4(5+j),0(5+j)`, also one connected C6, possibly on different six vertices for different j. Critically **the two coordinate-dual sixcycles on the ORIGINAL six incidence-column positions are IDENTICAL**, even as the LINE physical center changes. The authentic HISTORICAL accepted GF5 source A/A aligned-connected-D6 criterion therefore gives

```text
for EVERY h>=2, there exist ONE complete original f_h,g_h and
m=s+1 TRUE ORIGINAL distinct sixflag Q_j, such that
I_D6(Q_j;f_h,g_h)=1  for ALL j, and
|Q_j∩Q_k|=4 for j!=k.
```

This **attains a SHARP maximum m=s+1 IN THE DEFINED fixed-six-POINT, common-four-source-incidence, pairwise-only-four-intersection fan**: every Q_j must consume a different original LINE factor at p4 and p5; each POINT has only s+1 original LINE neighbors. Do not extrapolate this maximum to arbitrary D6 families with changing source POINT factors or other intersection patterns.

The fixed-map HISTORICAL ORIGINAL 51-column positively charged seven-class numerator of these m named Q_j, and ONLY these named Q_j, is at least (indeed their exact selected charge is) `5643(s+1)`. No claim is made that all other original Q are absent or that full S is this number. This is an existential `Theta(s)` star, NOT the universal `Omega(s^6)` of Branch A.

## 2. ALL-h negative transfer: one original global f swap erases ALL m named GF5 positives

Start with exactly the above ONE original complete f_h,g_h. Define `f'_h` by EXCHANGING ONLY the complete original POINT-factor images `f_h(p0)=01` and `f_h(p2)=23`, leaving EVERY other original POINT source-factor image unchanged; leave ALL original LINE map g_h unchanged. This is a globally injected WHOLE-source-factor transposition, not one independently redrawn source sixflag edge.

For every original Q_j, the MULTISET of left physical pair images is IDENTICAL before and after, merely permuted across two incidence-column positions. Thus:
- source POINT multiplicity still A, source LINE multiplicity still A;
- original physical left graph is STILL the SAME six-vertex C6;
- the physical right graph and every right-side factor-image-swap mask and mixed Gram are UNCHANGED for all global g permutations because g is literally unchanged;
- all the original six-incidence ID sets Q_j are unchanged, with their exact common four source flags.

However, swapping the 01 and 23 physical pair images between the original p0 and p2 source factors changes the left physical incidence-column dual cycle: original consecutive incidence-position adjacency includes {2,3}, while after swap its adjacency changes to {0,3} and the full left dual sixcycle NO LONGER equals the right dual on the SAME six incidence positions. The right dual is unchanged at the ORIGINAL global g. In source A/A, the historic seven-GF5 classifier accepts ONLY connected aligned D6, so for EVERY j

```text
I_D6(Q_j;f_h,g_h)=1,   I_all7(Q_j;f'_h,g_h)=0.
```

Thus EXACTLY the SAME named original Q fan changes its accepted weighted seven-class charge from `5643(s+1)` to **ZERO**, without changing ANY physical right 2factor masks, f-side six-coordinate 2factor eligibility, original source incidence pattern, or whole-map occupation sets. The left-to-right **incidence-column dual alignment** is indispensable; it cannot be reconstructed from physical-support-only Gram data.

**No-go interpretation:** Any proposed all-h proof step that depends ONLY on the original Q-family source membership, source-A/A tags, physical left 2factor eligibility, right packet physical support masks/Gram, and the occupied physical image edge sets but concludes a positive same-map historical GF5 count for this named original fan is FALSE. The two original instances are indistinguishable to those observables and have opposite fixed-fan positivity.

This does **NOT** construct a global root Branch B original `S_s(f,g)=o(s^6)` family. Outside the named fan, other sixflag sets may become positive after the transposition; the complete seven-class S is NOT counted or asserted to vanish. Nor does it falsify a proof method allowed to use full incidence-position dual alignment / GF5 algebra.

## 3. Finite independent original W34 and W38 falsifiers

The mathematical proof above is for EVERY dyadic h>=2; computation only independently falsifies errors at actual h=2 and h=3.

1. Load the authentic original symplectic W34 (s=4, V=85, 425 actual source incidence flags, minimal physical a=14) and W38 (s=8, V=585, 5265 actual source incidence flags, minimal physical K_a). Reconstruct true original source LINE stars, find two NONCOLLINEAR original POINT IDs with disjoint LINE stars, and solve exact four-anchor residual LINE-ID Hall matching using a separate augmenting-path algorithm. Build ONE complete globally injected original f,g, with all p4 and p5 original LINE stars pinned and all other original factors completed injectively.
2. W34 has a fan of EXACTLY `s+1=5` historical D6-positive TRUE original source sixflags with the SAME four original incidence IDs; W38 has EXACTLY 9. Their fan-only weighted selected GF5 contributions are `5*5643=28215` and `9*5643=50787`. One full original f(p0)↔f(p2) physical image swap leaves every original left six-edge physical multiset and ALL unchanged original right masks and g images untouched but makes EVERY named fan Q historical selected seven-GF5 negative.
3. An INDEPENDENT literal original-six-column source A/A + physical coordinate-degree-2 + sixcycle-connected-dual oracle is used in tests, NOT just invoking the new arbitrary-a historical GF5 classifier a second time. Compare before/after for EACH real original Q_j and every pair intersection cardinality exactly4. Verify the point/line whole map global injection and original source LINE-star noncollinearity.
4. For j=0,1 select their real eight distinct original LINE factors, add eight genuinely disjoint unused original LINE-factor swap partners, and check ALL 256 globally injected complete g maps. One 64x64 TRUE physical mixed Gram of the two sixpacket families and independent literal per-Q physical 2factor checks agree; same Gram before/after f swap. At x=0 the original historical Q0/Q1 have tags D6/D6 before and NONE/NONE after. Do not assert there are no other positive g^x states after the point swap.
5. Malformed injection/source slot Hall impossibility and unsupported finite power h=1 are rejected. The construction is all-h via genuine GQ and Hall; **W32 h=1 is deliberately excluded** because its original 15 LINE factors are insufficient for a common-four 8packet fan with disjoint swap partners.

## 4. Scientific acceptance gate

This is a narrow but strong **NO-GO** for positive historical GF5 transfer from physical-only crossfamily eligibility and a sharp fixed-point sixflag all-h construction. Classical Hall and graph-cycle transpositions are not individually novel mathematics; scientific scope lies in original W(3,2^h) global physical-factor-image model and historical seven-GF5 selected-motif behavior.

**ROOT #230 still open**: no proof that EVERY f,g has `S_s(f,g)>=c s^6`, no original infinite full `S=o(s^6)` pair sequence, no exact root-equivalent reduction, no general R3/ASET power claim. Pending independent qualified mathematics review, exact final PR HEAD three or more GH-hosted checks, and actual ancestor #601–607 acceptance/ancestry integration. No main or accepted registry modifications. Do NOT promote CI PASS to scientific acceptance.

**Next best scientifically relevant step**: formulate a *dual-aware* local compensation invariant that tracks both original point physical sixposition dual and right physical sixposition dual under correlated global f,g; immediately falsify a candidate scalar positivity transfer using this adversarial original fan. Without such a dual-aware coercivity inequality, repeating packet-code rank refinements or source-only Hall repair cannot close Branch A.
