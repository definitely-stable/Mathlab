# HYP-105 / issue #230 — AA4-BL: exactly TWO pinned opposite source images in one original B/A cherry

**Scientific research DRAFT**, strict child of [AA4-BK PR #576](https://github.com/definitely-stable/Mathlab/pull/576), frozen parent HEAD c8755c5fd307c89e46d47594b314dd93c63153e0. TRUE ORIGINAL symplectic W(3,2^h), same six distinct actual source incidence IDs under BOTH typed physical maps, and ONE full globally coherent opposite right-factor bijection conditioned on TWO source LINE images. No main edits, accepted RCP registry promotions or root #230 closure.

## Frontier and bounded novelty

[#576](https://github.com/definitely-stable/Mathlab/pull/576) already proves unconditional opposite whole-global random B/A mean ≥72(s+1) for EACH genuine source point/LINE cherry, fixed f and arbitrary occupied opposite support E. [#575](https://github.com/definitely-stable/Mathlab/pull/575) already counts first-side true-original cherry-rooted C4/2C2 residuals and the same-Q bilateral Hall defect. [#238](https://github.com/definitely-stable/Mathlab/pull/238), [#334](https://github.com/definitely-stable/Mathlab/pull/334), [#468](https://github.com/definitely-stable/Mathlab/pull/468) already provide GLOBAL original B/A means, while [#568](https://github.com/definitely-stable/Mathlab/pull/568) provides positive selected D6 after up to V/16 arbitrary pinned source original LINE images **BY EXCLUDING the pinned LINE IDs from eligible Q**. This research does **not** conflate the latter guarantee with a rooted event whose TWO initial source LINE IDs MUST PARTICIPATE in every eligible Q.

**NEW precisely scoped result:** exact ROOTWISE conditional mean when the TWO opposite actual original source factors appearing in the selected original cherry are already fixed to TWO arbitrary occupied physical edges, a sharp physical-pair adjacency distinction, and a POSITIVE robust conditional lower under an EXPLICIT LOCAL missing-edge-degree hypothesis. An extreme abstract pendant-edge physical example shows why the prior unconditional one-global-map per-root mean cannot simply be conditioned on arbitrary right pins. It is NOT claimed to be an actual all-h original W(3,s) counterfamily, and classical edge-2factor counting and union bounds are not claimed as broad mathematical innovations.

## The all-h actual-original quantifiers and exact two-pin identity

Let s=2^h, h>=5, and W(3,s) be the ACTUAL symplectic generalized quadrangle. Put d=s+1, V=(s+1)(s²+1), a minimal with binom(a,2)>=V, K=binom(a,2), m=K−V<=a−2. Fix ANY complete globally injected ORIGINAL point-factor physical pair-edge map f and ANY occupied physical opposite right support E subset K_a of EXACTLY V distinct edges, arbitrarily correlated with f. Fix TWO DIFFERENT genuine original incidence IDs α=(p,l1), β=(p,l2) sharing ANY TRUE original source point p, with l1!=l2. Their anchored point image f(p) occurs twice, and four other distinct actual original source point factors can form an occupied physical C4 on four coordinates outside the endpoints of f(p).

Let N_BA(αβ;f) be the EXACT number of such true-original six-incidence flag Q including α and β, whose remaining four point physical pair edges form one occupied physical C4 and whose SIX actual original opposite LINE source factor IDs are DISTINCT. All six original incidence ID indices are immutable. This pool was established in the parent #576 and is independent of the choice of any right physical images for l1 or l2.

Now prescribe **ARBITRARY TWO DISTINCT occupied opposite physical pair edges** e1,e2 in E, requiring g(l1)=e1, g(l2)=e2, but leave all OTHER V−2 original right LINE source factor IDs uniformly bijective onto E\{e1,e2}, drawn as **ONE common uniformly random COMPLETE original global right map g**. This is legal whether physical e1,e2 are adjacent or disjoint in K_a and whether E omits other physical edges.

Write T_A(E;e1,e2) for the number of **UNORDERED** occupied physical six-edge simple two-regular subgraphs of E on six distinct physical right coordinates containing BOTH e1 and e2. The six-edge target graph may be a connected C6 or two disjoint triangles. Every such target has the two fixed physical images of ACTUAL original LINE IDs l1,l2 in precisely specified source positions, leaving FOUR different occupied edges to assign to the other FOUR original source LINE IDs. Exactly 4! physical assignments produce the historical accepted B-left/A-right GF5 original sixflag for one given eligible source Q. Under one global opposite permutation the remaining four original LINE IDs are a uniform ordered injection into V−2 remaining occupied right edges; the denominator is (V−2)_4. Therefore

\[
\boxed{
\mathbb E_{g:\,g(l_1)=e_1,g(l_2)=e_2}
H_{BA}(\alpha,\beta;f,g)
=N_{BA}(\alpha\beta;f)\,
\frac{4!\,T_A(E;e_1,e_2)}{(V-2)_4}.
}
\tag{BL-PIN}
\]

This is an EXACT finite all-h original B/A identity; it requires NO source-Q independence and NO separate global permutation per sixset. All true original six-incidence IDs remain identical on both physical sides. Original LINE-root / POINT-random dual statement holds by typed source duality.

For a FULL physical K6, an independent enumeration of all binom(15,6)=5005 six-physical-edge subsets gives T_A(K6;e1,e2)=**7** for two ADJACENT e1,e2 and **14** for two DISJOINT e1,e2, hence exact conditioned one-original-Q probabilities

\[
\boxed{
P(A\mid\hbox{two pinned adjacent edges})=\frac7{715},
\quad
P(A\mid\hbox{two pinned disjoint edges})=\frac{14}{715}.
}
\]

The preceding unpinned one-Q simple A probability 2/143 is their correctly weighted mean over 120 ordered adjacent and 90 ordered disjoint K6 edge pairs:

\[
(120(7/715)+90(14/715))/210=2/143.
\]

The two-pin probability can therefore differ by a factor of TWO even when E has no physical holes. This difference is a purely physical typed pair-edge constraint, not a fake source W3 effect.

## Additional LOCAL missing-edge-degree hypothesis and strengthened theorem

Write \(\overline E=E(K_a)\setminus E\) for the graph of unavailable right physical pair edges. Let \(\Delta_{\mathrm{pin}}\) be the **maximum number of missing right physical pair edges incident to any physical coordinate appearing as an endpoint of e1 or e2**. This is a LOCAL maximum at 3 coordinates for adjacent pins and at 4 coordinates for disjoint pins. A global missing-degree bound is sufficient but stronger than necessary.

Assume **in addition** to the exact original quantifiers:

\[
\boxed{
\Delta_{\mathrm{pin}}\le \left\lfloor\frac{a-4}{8}\right\rfloor .
}
\tag{BL-LOCAL}
\]

Only physical *right support* holes at the coordinates of the two pinned edges are constrained; the other physical coordinates can have arbitrarily concentrated missing pair edges, consistent with total m<=a−2. No GQ automorphism or random missing-edge assumption is made.

### Physical C6 count with two adjacent fixed physical edges

Suppose e1={u,v}, e2={v,w} with u,v,w distinct. For every ordered triple x,y,z of three **different** right physical coordinates outside {u,v,w}, consider the physical 6-cycle

\[
u-v-w-x-y-z-u.
\]

It uses BOTH pinned physical edges. The only four additional required occupied pair edges are wx, xy, yz, zu. In full K_a there are exactly (a−3)_3 distinct physical cycles of this *specific* rooted orientation. An edge wx or zu missing can eliminate at most Delta_pin*(a−4)_2 ordered triples each; a missing internal edge xy or yz can eliminate at most 2m(a−5) ordered triples each (the unordered missing edge has two possible ordered directions and at most a−5 remaining choices for the third new vertex). The union bound yields a VALID number of occupied physical C6 targets

\[
\boxed{
T_{C6}(E;e_1,e_2)
\ge (a-3)_3-2\Delta_{\rm pin}(a-4)_2-4m(a-5)
\ge\frac12(a-3)_3.
}
\tag{BL-ADJ}
\]

Proof of the final half: Delta_pin<=(a−4)/8 and m<=a−2; subtracting half of the full (a−3)_3 leaves the factor (a−5)(a−2)(a−20)/4>=0, for a>=261.

### Physical C6 count with two disjoint fixed physical edges

Suppose e1={u,v}, e2={w,x} with u,v,w,x all distinct. For every ordered pair y,z of remaining distinct physical coordinates, consider the physical 6-cycle

\[
u-v-y-w-x-z-u.
\]

It contains both pinned edges; its four extra required pair edges are vy,yw,xz,zu. Every one touches a physical endpoint of e1 or e2. Thus EACH missing-pinned-endpoint incidence excludes at most (a−5) ordered pairs and

\[
\boxed{
T_{C6}(E;e_1,e_2)
\ge (a-4)_2-4\Delta_{\rm pin}(a-5)
\ge\frac12(a-4)_2.
}
\tag{BL-DISJ}
\]

All displayed physical cycles for fixed rooted pin orientations are different. Since (a−3)_3≥(a−4)_2, BL-ADJ and BL-DISJ imply that **for either type of pinned physical edge pair**,

\[
\boxed{
T_A(E;e_1,e_2)\ge T_{C6}(E;e_1,e_2)\ge\frac12(a-4)(a-5).
}
\tag{BL-TARGET}
\]

These are simultaneous actual right support constraints and do not assume the two pinned edges or the right support to be randomly chosen.

### All-h positive expected rooted original GF5 sixflag theorem with TWO pinned source LINE IDs

The previous source-side bound from #576 remains valid with the SAME true original pinned source flags: any given occupied left source C4 has at least (d−2)(d−3)(d−4)(d−5) choices of four further actual genuine original incidence flags with no repeated opposite original LINE factor ID, and C4_p(f)>=a^4/10 for a>=261. For d=s+1>=33, (d−2)(d−3)(d−4)(d−5)>=d^4/2.

Combining with BL-PIN and BL-TARGET, using (V−2)_4<=V^4:

\[
\begin{aligned}
\mathbb E_g H_{BA}
&\ge
\frac{a^4}{10}\frac{d^4}{2}\,
\frac{24(a-4)(a-5)/2}{V^4}\\
&=\frac35\,\frac{d^4 a^4(a-4)(a-5)}{V^4}\\
&\ge\frac12\,\frac{d^4a^6}{V^4}\\
&\ge4\,\frac{d^4}{V}
\ge\boxed{4d=4(s+1)}.
\end{aligned}
\tag{BL-4D}
\]

The third inequality uses (a−4)(a−5)/a²>=5/6 for every a>=261; the fourth uses a²>=2V, so a^6>=8V³; the final inequality uses V=(s+1)(s²+1)<=d³. All exact all-h checks are integer or arbitrary-precision Fraction.

**Interpretation:** for EVERY specific ACTUAL original source cherry, ANY source-side physical f and ANY opposite E with the displayed LOCAL right-hole-degree condition, AND ANY specified TWO distinct original-root physical edge images in E, there exists SOME ONE complete globally bijective opposite original LINE map respecting both specific pins with at least ceil(4d) accepted genuine-original B/A six-incidence motifs through that root. It may differ for another pinned root. This is NOT a positive guarantee for a fully fixed adversarial pair f,g; the remaining V−2 source LINE assignments are still random/constructible.

## Counterexample to deleting the added physical endpoint-degree hypothesis: generic support, NOT dyadic W3

Consider **the abstract near-complete physical graph E' on a arbitrary physical coordinates** formed from K_a by deleting ALL a−2 edges incident to physical coordinate 0 except the one edge {0,1}. It has |E'|=binom(a−1,2)+1, exactly m=a−2 missing edges and a pendant occupied pair edge e1={0,1}. Any occupied graph on six physical coordinates with degree TWO at each coordinate cannot contain this pendant edge; thus T_A(E';{0,1},e2)=0 for every distinct second pinned occupied physical edge e2. Consequently the conditional B/A mean given this first pinned image is ZERO for ANY eligible original source Q pool, **irrespective of a positive source-side pool**.

This is an exact counterexample to a mathematical deduction from ONLY the numerical physical hole budget m<=a−2 to a rooted two-pinned support positivity claim. **It is NOT asserted to instantiate a dyadic genuine W(3,2^h) physically occupied support**, because the actual V=(s+1)(s²+1) may not equal binom(a−1,2)+1 for any dyadic s; in fact for sampled dyadic h through large values m is strictly smaller than a−2. Do not claim the abstract physical obstruction is an actual all-h root #230 counterfamily or even an actual finite W3 labeling.

## Independent finite falsification, exact provenance

- Genuine original W32 with ALL FIVE complete globally injected typed original physical maps dual_zero,lex,reverse,S68,S72. For EACH of all 90 actual source POINT/LINE cherry αβ roots, construct the exact TRUE original sixflag source C4 and six-distinct opposite source-factor ID pool. Independently enumerate all 5005 six-edge K6 physical subsets and the 6!=720/4!=24 common global (V−2)_4 marginal: two physical images pinned to adjacent edges give 7 targets; disjoint give 14 targets. Exact one-Q conditional probabilities 7/715 and 14/715. Compare computed TRUE original rooted expected B/A formula to N_source*probability for BOTH pin types, each actual original source cherry. Verify unpinned average 2/143 from 120 ordered adjacent and 90 ordered disjoint physical edge-pair choices, with no fake independent per-source-Q global maps.
- True original symplectic W34 GF4, six physical holes in nononto K14, complete typed original lex and random physical assignments. For BOTH typed source cherry directions and BOTH distinct pin-edge arrangements (adjacent and disjoint), compute source-Q pool on an actual original 4-coordinate physical root-complement subset and count physical targeted simple 6-edge right twofactors containing both exact pinned edges. Independently recompute those physical targets via an unrelated rooted physical C6 + triangle partition enumeration. Verify one-global-right conditional Fraction=24*T_A*N_source/(V−2)_4 on the SAME original source-Q pool. Small h4 is a finite formula test only, NOT a false all-h 4d theorem application.
- Abstract near-complete pendant support E'=K_a−(a−2) star edges proves target count exactly zero, explicitly labeled **NOT an actual dyadic W3 source model**. It falsifies any unsupported upgrade from mere “at most a−2 missing physical edges” to two-pin conditional success.
- Exact all-h h5..35 and h40/48/64/80 verifies source-bound arithmetic and BOTH adjacent/disjoint physical cycle deletion inequalities with local Delta_pin floor((a−4)/8), and the 4d bound; strict wrong source IDs, invalid pinned edges, duplicate right support, impossible false h<5 quantifiers reject.

## Root issue and next step

This research isolates a **LOCAL graph-complement degree obstruction** to trying to condition the rootwise stochastic theorem #576 on arbitrary actual original opposite pin images; and proves a new ALL-h positive conditional expectation when the pinned physical vertices have sufficiently many occupied right physical edges. It does NOT show that ANY already fixed complete f,g has Ω(s^6) original sevenGF5 accepted motifs; the positive conditional expectation does not constrain all the other V−2 adversarial original images. No actual infinite correlated original source counterfamily and no full R3/ASET exponent.

A genuinely root-facing next mathematical target is to quantify how many actual original source cherry roots in any fixed globally injected original line map g necessarily have their opposite pinned image endpoint neighborhoods dense, and then control the SAME remainder mapping's Hall defect jointly with D6. Another possibility is an exact all-h proof of conditioned-rooted B/A positivity without the local degree assumption for the actual dyadic-specific m, but this must not be inferred from the abstract near-complete support example.

Keep Draft until exact final-HEAD dedicated, INDEX, Proof Audit, Full Research and independent mathematical referee plus frozen parent chain; root #230 OPEN_WITH_FORMAL_BLOCKER.


## AA4-BL-MAJ — deterministic *majority* of real original root pins is locally regular for EVERY already fixed opposite g

The local missing-degree condition in BL-LOCAL looks restrictive in isolation, but the MINIMAL physical K_a pair alphabet limits how many source-root opposite image endpoints can fail it on ANY globally injected complete original right mapping g. Fix that ENTIRE adversarial g, not just its occupied right support E. For s>=32 let t=floor((a−4)/8), and call a physical coordinate vertex **bad** if it is incident to at least t+1 missing physical right pair-edges from E(K_a)\im(g). The sum of missing physical degrees is 2m, hence the number of bad physical vertices is at most

\[
B=\left\lfloor\frac{2m}{t+1}\right\rfloor\le16.
\]

The last bound holds for every a>=261 and m<=a−2: t+1>(a−4)/8, so 2m/(t+1)<16(a−2)/(a−4)<17, giving B<=16. Each bad physical vertex is incident to at most (a−1) OCCUPIED physical right pair edges, hence involves at most B(a−1) distinct ACTUAL original LINE source factor IDs under globally injective g. Each such original LINE factor belongs to d actual genuine-original source incidence flags (p,l), and such a flag participates in EXACTLY d−1 source POINT-cherry twoflag roots through p. Union bounding every bad original source LINE factor gives at most

\[
\boxed{B(a-1)d(d-1)}
\]

actual source point cherry roots whose TWO already fixed original LINE physical images touch even one bad right physical coordinate.

Since the total number of genuine source point cherries is

\[
V\binom d2=\frac{Vd(d-1)}2,
\]

and minimality of a implies V>binom(a−1,2), the BAD fraction is strictly less than

\[
\frac{2B(a-1)}{V}
<\frac{4B}{a-2}
\le\frac{64}{a-2}
\le\frac{64}{259}<\frac14.
\]

Therefore, for EVERY already completely fixed original LINE physical g and EVERY genuine source original W(3,s) with h>=5,

\[
\boxed{
\#\bigl\{
\text{actual source POINT cherry roots }(\alpha,\beta):
\Delta_{\rm pin}(g(l_1),g(l_2))\le t
\bigr\}
>\frac34 V\binom d2 .
}
\tag{BL-MAJ}
\]

For **each** of these more-than-75% real source cherry roots and ANY independently fixed globally injected original point physical f, IF one freezes only its two real original LINE images as pins and uniformly reallocates the REMAINING V−2 original LINE source factors onto the SAME occupied right support, BL-4D gives a conditional expected historical accepted rooted B/A count at least 4(s+1). Original LINE ↔ POINT duality yields the corresponding statement for more than 75% true original LINE cherry roots under any already fixed f.

**Critical logical limitation:** Although the membership of the good source-root set is a DETERMINISTIC fact about the given fully fixed g, the ≥4d bound is a conditional expectation over OTHER complete global maps extending two pinned images; it is NOT a bound on the actual rooted B/A count of the ORIGINAL unmodified g. A statement “>75% roots actually survive the joint Hall test on every fixed g” would be false already at small original W32 and is neither claimed nor proved here. In particular, BL-MAJ does not prove root issue #230 Branch A, does not turn quenched means into a minimax lower, and does not negate prior Hall-scarcity obstructions.

A separate all-h exact rational test verifies B<=16, good source-root count >3/4 of V binom(d,2), and the strict separation between determined fixed-g pin eligibility and any unproved fixed-g acceptance.
