# HYP-105 / issue #230 — AA4-BM: deterministic FOUR-global-source-swap repair of original rooted B/A on MOST roots of EVERY fixed f,g

**Scoped scientific Draft; strict child of [AA4-BL PR #577](https://github.com/definitely-stable/Mathlab/pull/577), pinned parent HEAD 749a9c1cafb0eea32bdd7e1c866c099004bf8ae6.** Preserve the *authentic original* symplectic generalized quadrangle W(3,2^h), complete typed physical factor injections into E(K_a), six **DISTINCT actual original source incidence flag IDs**, and the SAME IDs on both sides. Root original issue #230 OPEN_WITH_FORMAL_BLOCKER; no accepted RCP or main modifications.

## Prior work and the remaining quantifier gap

Parent [#577](https://github.com/definitely-stable/Mathlab/pull/577) already proves an EXACT expectation of accepted original GF5 B/A sixflag motifs through any specified genuine source cherry conditional on preserving its TWO genuine original opposite factor physical pair images. When the missing physical right-edge degree at their physical endpoints is ≤floor((a−4)/8), that mean is ≥4(s+1), but ONLY when a new ONE complete global opposite map is uniformly resampled on all other V−2 original factors. Parent also proves that >3/4 of true source point cherry roots satisfy that physical endpoint regularity for EVERY already fixed original line map g. These are **PRIOR** and do not imply accepted motifs on the already unmodified g.

[#545](https://github.com/definitely-stable/Mathlab/pull/545), [#547](https://github.com/definitely-stable/Mathlab/pull/547), [#548](https://github.com/definitely-stable/Mathlab/pull/548), [#550](https://github.com/definitely-stable/Mathlab/pull/550) already prove proximity/repair of DIFFERENT genuine original A/A-D6 selected sixflag configurations by up to FIVE original source LINE-image swaps, sometimes with a five-swap cut or geometric distance certificate. We do NOT claim generic transposition-based derandomization, target assignment via swaps, or the existence of small-swap positive GF5 maps as novel in general.

**NEW precise strengthened quantifier:** for EVERY arbitrary **already FULLY fixed** original f,g, and EVERY individually chosen source cherry whose TWO physically pinned opposite images satisfy parent's deterministic physical endpoint regularity, a concrete ≤4 original source LINE-factor image swap sequence creates ONE truly accepted six-original-incidence B/A motif through that particular original cherry, WITHOUT changing f, the occupied right physical support or EITHER of its previously fixed original source LINE physical pair images. Consequently >3/4 of ALL genuine source point cherries of EVERY fully fixed f,g admit such a ≤4-swap local repair (and dually for line cherries via point-map swaps). This is a **local neighborhood/correction theorem** from the given fixed map, not positivity on the unmodified map itself or one repaired map satisfying all roots simultaneously.

## Exact all-h theorem

Let s=2^h≥32, d=s+1, V=(s+1)(s²+1), a=min{a:binom(a,2)≥V}. Fix ANY genuine original W(3,s) incidence graph, ANY globally injected COMPLETE original POINT source pair-edge map f and ANY globally injected COMPLETE original LINE source pair-edge map g; f,g may be adversarially correlated with the original incidence and each other. Let E=im(g) with exactly V distinct occupied right physical pair edges.

Fix ANY actual original source point p, and ANY two DISTINCT genuine ORIGINAL incidence flag IDs α=(p,l1), β=(p,l2), with l1≠l2. Denote the original right physical pair images e1=g(l1), e2=g(l2). Let \(m_u\) be the number of missing physical right pair edges incident to physical coordinate u in K_a\setminus E. Call this particular source cherry **regular** if

\[
\max_{u\in e_1\cup e_2}m_u
\le t=\left\lfloor\frac{a-4}{8}\right\rfloor.
\tag{BM-REG}
\]

### AA4-BM1 — EACH physically regular source root is repaired in at most FOUR swaps

**For every fully fixed legal original pair f,g and every genuine original source point cherry αβ satisfying BM-REG, there exists a COMPLETE globally injected genuine original LINE-factor physical map g' such that:**

1. The entire original source point map is IDENTICALLY f, and the occupied right physical pair-edge support is IDENTICALLY E=im(g')=im(g).
2. BOTH original source LINE factor physical images e1,e2 are **exactly unchanged**: g'(l1)=g(l1), g'(l2)=g(l2).
3. The original source LINE map g' is reached by **at most FOUR TRANSPOSITIONS of physical images of actual original LINE source factor IDs** starting from the original arbitrary g, with BOTH pins unchanged at EVERY intermediate transposition; no image duplication or lost occupied support at any step.
4. There exist SIX DISTINCT ACTUAL ORIGINAL incidence flag IDs Q containing α,β such that the true original projected GF(5) seven-family classifier accepts this SAME Q as positive **B-left/A-right** under the final ONE complete global pair f,g'.

In particular,

\[
\boxed{
\forall f,g\quad\forall\text{ physically regular actual root }\alpha\beta,
\quad
\exists g'\in B^{\rm swap}_4(g;e_1,e_2):
H_{B/A}(\alpha\beta;f,g')\ge1.
}
\tag{BM-4}
\]

Here the swap ball restricts ALL intermediate source maps to preserve both pinned ORIGINAL source line-factor images.

### Constructive proof and exact algorithm

**Step A — one true-original source sixflag Q:** By parent #576 true GQ source regularity and arbitrary first-side f, there are at least

\[
N_{B/A}(\alpha\beta;f)\ge
C4_p(f)\,(d-2)(d-3)(d-4)(d-5)>0.
\]

Enumerate an occupied simple physical C4 on four coordinates outside the two already saturated endpoints of physical image f(p), invert its four distinct occupied pair edges through f to four DIFFERENT actual ORIGINAL point source factors q0,q1,q2,q3, and choose genuine original LINE source neighbors \(\ell(q_i)\) one by one avoiding the two pinned l1,l2 and all previously chosen \(\ell(q_j)\). There are at least d−2−i positive choices at step i, h≥5. The six ACTUAL original incidence flags Q={(p,l1),(p,l2),(q_i,\ell(q_i)):i=0..3} are DISTINCT; they have exactly ONE original source point repeated (p) and SIX different genuine original LINE factor IDs.

On original physical POINT side, f(p) appears twice and the other four distinct point physical pair edges form an occupied C4 disjoint from f(p)'s coordinates, so the point physical projection is precisely 2-regular on six coordinates, with SOURCE-B original point type. The original source incidence IDs do not change in later steps.

**Step B — one full physical right C6 target preserving BOTH pinned opposite images:** By the parent's EXACT positive adjacent/disjoint two-pin physical bound, BM-REG and m=binom(a,2)−V≤a−2 ensure existence of an occupied simple physical C6 in E containing e1 AND e2. It can be found by a finite explicit enumeration using the two concrete cycle families from #577:

- If e1={u,v},e2={v,w} share v, enumerate distinct x,y,z outside u,v,w for cycle u-v-w-x-y-z-u.
- If e1={u,v},e2={w,x} are disjoint, enumerate orientations of e1,e2 and distinct y,z outside the four pinned endpoints for cycle u-v-y-w-x-z-u.

At least one such true physically occupied six-edge 6-coordinate C6 exists under BM-REG. Its six occupied right pair edges contain the ORIGINAL fixed e1,e2 and four other different occupied right pair edges t0,t1,t2,t3, all distinct from e1,e2. The connected physical cycle is sufficient; no two-disjoint-triangles case is required. There is NO assumption of independence between the two physical global maps and no random resampling.

**Step C — deterministic ≤4 global source LINE-image transpositions:** Let the four free ACTUAL original source LINE factor IDs of the chosen Q be r0,..,r3. Prescribe an arbitrary bijection r_i↦t_i from those four genuine original source line factors to those four remaining occupied target right physical pair edges. Start from the FULL already fixed original source LINE physical bijection g. For i=0,1,2,3 in order, if the current physical image of r_i is already t_i, do nothing; otherwise let d_i be the unique ACTUAL original source LINE factor ID currently owning physical pair edge t_i (exists by GLOBAL injectivity onto fixed support E), and SWAP the images of r_i and d_i. This is a transposition of WHOLE original source LINE factor images, not the alteration of one incidence flag only. Because t_i is never either pinned e1 or e2, d_i cannot be l1 or l2. Because all desired t_i are distinct and previous source factors r_j for j<i already own their own target edge, d_i cannot be any earlier repaired r_j. Hence every swap preserves both pins and all previously repaired target assignments; no more than FOUR are required. Each intermediate complete original g_i is a bijection onto the SAME occupied E.

After the final swap, original source Q has six distinct actual original LINE factors whose physical images are exactly the six occupied edges of a simple right C6, yielding a 2-regular six-coordinate physical LINE projection with original LINE type A. Together with the original physical POINT source type B and six unchanged genuine original source incidences, the independently accepted historical seven-GF5 classifier returns **B-left/A-right**. This proves BM-4.

The line-root / point-map-swaps dual statement follows from the typed self-dual original symplectic incidence graph W(3,s): fix any two true original flags with one original LINE source factor, keep those two original POINT pair-images fixed, and modify at most four other whole original POINT factor images. The result is historically accepted A-left/B-right.

### AA4-BM2 — strict majority of roots of EVERY fully fixed f,g admits one such repair

Parent [#577](https://github.com/definitely-stable/Mathlab/pull/577) proves that for EVERY complete arbitrary original g, the number of physical right coordinates with >floor((a−4)/8) missing incident occupied pair edges is ≤16 (because total missing physical edge count m≤a−2). Each such bad physical coordinate is present in at most (a−1) occupied right pair-edge images, affecting at most (a−1) actual original source LINE factors. Each affected LINE source factor participates in d actual source incidence flags, and each flag in d−1 actual source POINT cherry pairs. Consequently the fraction of all V·binom(d,2) original point cherry roots touched by a bad physical right endpoint is **strictly less than 64/(a−2)≤64/259<1/4** for all h≥5.

For each of the remaining more-than-three-quarter true source cherry roots apply BM-4. Thus

\[
\boxed{
\forall\text{ already fixed }f,g,\quad
\#\{\text{genuine original POINT cherry roots }\alpha\beta:
\exists\text{ legal root-pin-preserving }g'
\text{ within FOUR source-image swaps and }H_{B/A}(\alpha\beta;f,g')\ge1
\}
>\frac34 V\binom d2.
}
\tag{BM-MAJ}
\]

The neighborhood witness g' **MAY DIFFER FOR EACH ROOT**. This strictly stronger deterministic fixed-pair LOCAL-REPAIR quantifier is not an all-roots common global completion, not a bound on the number of accepted original Q on the original UNMODIFIED g, and not a uniform root #230 seven-class minimax positive lower.

### AA4-BM3 — four steps are target-specific sharp but NOT GF5-optimality

Consider an **abstract ten-original-source-ID permutation instance**, not asserted to come from a true W(3,s) physical coloring: there are two immutable source pins, four selected source factors r0..r3, and four EXTERNAL source factors d0..d3 that initially OWN the four particular desired target images t0..t3. Each physical-image transposition can import at most ONE of those four desired target edges into the selected set {r0,..,r3} because all four target images begin OUTSIDE that set. Therefore at least four swaps are necessary for THIS **specified exact target assignment**; the four donor-swaps above meet it. A finite independent exhaustive breadth-first search over the eight unpinned abstract source labels confirms no ≤3-swaps path to this exact prescribed four-label image tuple. **It does NOT prove that some OTHER positive GF5 B/A physical target cannot be reached in fewer swaps on an actual original W3 map**, and it does not prove four-swap optimality for the positive historical class itself.

## Independent genuine-original falsifiers

1. **All dyadic h5..35,40,48,64,80:** exact-rational/integer parameter certificates of strict >75% genuine source cherry regularity, and formal construction invariant: one chosen source sixflag Q with SIX true source incidence IDs, one occupied right C6 containing BOTH original root images, then at most four source-FACTOR transpositions of the already fixed g preserving initial pins, E, f and original source incidence IDs. No fabricated high-order symplectic GQ model.
2. **Five REAL original W32 complete globally injected f,g** (dual_zero,lex,reverse,S68,S72): iterate ALL 90 actual source POINT/LINE cherry roots of each model; when the true original C4/six-distinct-opposite-factor source pool exists, execute the explicit full global swap-construction and check ≤4 steps, BOTH original pinned source factor images unchanged at EVERY intermediate original full injection, identical image support before/after, immutable genuine-original sixincidence Q, exact physical two-side 2regularity on six physical coordinates, and positive historical original B/A or A/B tag on the SAME final map. For first selected roots, independently run the older complete W32 seven_census on the actual repaired model and confirm its original six-ID witness set and historical selected tag, not merely the new physical target construction.
3. **Actual original W34 GF4, nononto K14 physical supports** under original lex/random full typed point and line maps: sample genuine source point/LINE cherries, independently verify the repaired full map's SAME physical support, pinned images, ≤4 transpositions and selected class via the separately authored original two-sided independent seven-GF5 join classifier. Finite s=4 is a constructive test, NOT an application of the all-h s>=32 majority proof.
4. **Physical typed gauge invariance:** independent permutation of original physical POINT and LINE coordinate palettes on real W32 preserves source Q and accepted original class after independent global source-factor repairs.
5. **Abstract target-specific four-swap sharpness:** exhaustive permutation BFS on eight unpinned abstract source labels proves four external target owners force at least four swaps to THIS EXACT target assignment, with no assertion about global GF5 class minimality or genuine original W3 realization.
6. Malformed actual GQ source IDs, non-injective or partial original physical factor labelings, duplicate pinned source incidence IDs, invalid physical support or false h<5 all-h quantifiers fail closed.

## What this does NOT solve

The main issue [#230](https://github.com/definitely-stable/Mathlab/issues/230) requires a universal lower bound for the **UNCHANGED** arbitrary fully fixed correlated original pair f,g on ALL SEVEN accepted GF5 six-incidence classes, an all-h genuine original correlated o(s6) counterfamily, or an accepted precise model-equivalent obstruction. A map repair, even from every given map and most source roots with at most four swaps, is NONE of these. It cannot rule out that the original f,g has extremely few accepted motifs; it does not force ONE nearby map simultaneously to repair >75% roots; and it makes no full R3 / ASET strict exponent claim.

The new mathematically meaningful open step is to quantify overlap of the many per-root **four-swap neighborhoods** at the SAME original map g, or prove a quantitative global lower on the original all-fixed two-sided source-cherry Hall survival using genuine W3 geometry and the D6 bicolored squarefree trace, rather than merely knowing that every root has a close correction witness. The prior [#545/#547/#550](https://github.com/definitely-stable/Mathlab/pull/547) original D6 five-swap repairs are separate original classes and should not be retroactively credited to this slice.

**Acceptance gate:** keep Draft, with exact final HEAD dedicated GH-hosted Research / INDEX / Proof Audit / Full Research SUCCESS, intact ancestor gate and independent mathematical review. No merge or accepted root A/B/C promotion from test PASS alone.
