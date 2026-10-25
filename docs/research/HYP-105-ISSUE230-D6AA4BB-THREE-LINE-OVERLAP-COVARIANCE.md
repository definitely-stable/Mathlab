# HYP-105 / issue #230 — AA4-BB: exact 0/1/2/3 shared-original-LINE overlap and GOOD threeflag variance O(s^-3)

**STATUS: strictly scoped partial theorem, scientific Draft.** Direct child of AA4-BA [PR #562](https://github.com/definitely-stable/Mathlab/pull/562), source parent HEAD c98ea5d0418d416c8a0a328f1a00809c1a051c91, in the scientific stack #561 → #560 → #559 → #556 → #554. This proof is not a proof of the root A/B/C issue #230. The original source remains genuine symplectic W(3,2^h), the point/line assignments are complete typed globally injected maps to unordered physical pairs of the minimal K_a, and ALL counted three flags are ACTUAL distinct original source incidence IDs with three distinct original point factors and three distinct line factors. These are GOOD *threeflag* wedges, NOT accepted historical seven-GF(5) *six-ID* classes.

## Mathematical selection and prior-art boundary

AA4-BA #562 already proved a uniform quenched relative-variance envelope O(s^-3/2) for physically GOOD opposite-port wedges under one whole random global original line map onto any adversarial fixed right physical support E, with any adversarial fixed point map f. Its proof grouped two and THREE shared original line factors together, bounding their joint probability by the single-event probability p. That discarded a geometric factor for **exactly two** shared line IDs. The present step refines the entire overlap partition, proving a uniform O(s^-3) bound for this SAME genuinely original GOOD statistic. This does not make the random g into an arbitrary fixed adversarial g and thus does not solve #230.

General U-statistic concentration under sampling without replacement is classical; see Ai, Kuželka and Wang (2022), *Statistics & Probability Letters* 187, 109528, https://doi.org/10.1016/j.spl.2022.109528. Parent project [PR #544](https://github.com/definitely-stable/Mathlab/pull/544) has already proved O(s^-3) quenched variance for a DIFFERENT selected genuine-original D6 six-incidence statistic. We claim no novelty for overlap counting, variance decomposition or the O(s^-3) exponent abstractly: only an explicit separately audited **GOOD threeflag source geometry and physical-port dependency tensor**.

## Definitions and exact quantified statement

Let s=2^h, h>=5, V=(s+1)(s²+1), d=s+1, a the least integer with binom(a,2)>=V, t=a-2. Fix an arbitrary complete genuine original globally injective POINT physical edge labeling f; fix any V-element globally occupied right physical edge support E ⊂ E(K_a). Draw ONE uniform complete global ORIGINAL LINE-factor bijection g onto E, without any independent per-flag or per-Q assignments.

The AA4-AO support-defined BAD coordinates are those with 16 * (missing physical pair-edge degree)>=a. Let F° and E° be induced CLEAN occupied physical edge supports on the complement of these BAD coordinate sets. All original source flags in one counted GOOD opposite wedge have three different source POINT and LINE factor IDs; the point-side physical center and two outer images are in F° and intersect in opposite ports, with analogous line-side images in E°. This is EXACTLY the previously specified AA4-BA GOOD event, not broader ALL-D.

Index true-original point-clean triples by their ordered three original line IDs (l,k0,k1); denote integer multiplicities w_{l,k0,k1}>=0, all three IDs different. Let B=sum w. Let M_j be the maximum aggregate weight over prescribed j-element UNORDERED sets of original LINE IDs that occur in one triple, j=1,2,3. In particular, M3 counts ALL up to 6 ordered permutations sharing that same fixed unordered original 3-line ID set. Define T°(E)=Σ_{uv∈E°}(deg_{E°}u−1)(deg_{E°}v−1), (V)_r=V(V−1)...(V−r+1),

\[
p=\frac{2T^\circ(E)}{(V)_3},\quad
q=\frac{(V-3)_3}{(V)_3},\quad
P_1=\frac{4t^4}{(V-1)(V-2)(V-3)(V-4)},\quad
P_2=\frac{16Vt^3}{(V)_4}.
\]

**AA4-BB1 — exact mean and sharp-overlap-indexed upper envelope:** For EVERY nonnegative valid three-distinct-source-LINE-ID weighted family and every fixed right occupied edge support of V>=6 edges of K_a (a>=4) with positive clean or unclean T, a single uniform complete right global permutation satisfies

\[
\boxed{
{\mathbb E}_g R=Bp,\qquad
\frac{\operatorname{Var}_g R}{({\mathbb E}_gR)^2}
\le \left(q^{-1}-1\right)
+\frac{3M_1P_1}{Bp^2}
+\frac{3M_2P_2}{Bp^2}
+\frac{M_3}{Bp}.
}
\tag{BB1}
\]

No independence of two original events is asserted; their common line source labels are counted exactly through the four overlap cases.

**AA4-BB2 — genuine original all-f/right-support GOOD concentration at cubic rate:** For every dyadic h>=5 and EVERY genuine original f and E,

\[
B\ge B_0=\frac{d(d-1)(d-2)V^2}{16},
\quad p\ge p_0=\frac{V^2}{8(V)_3},
\quad M_1\le5d^3t^2,\quad M_2\le8d^3t,\quad
\boxed{M_3\le6d^3}.
\tag{BB2}
\]

Consequently

\[
\boxed{\eta_s=
q^{-1}-1
+\frac{15d^3t^2P_1}{B_0p_0^2}
+\frac{24d^3tP_2}{B_0p_0^2}
+\frac{6d^3}{B_0p_0}
=O(V^{-1})=O(s^{-3})}.
\tag{BB3}
\]

An intentionally conservative completely explicit universal rational inequality also holds for all dyadic h>=5:

\[
\boxed{\eta_s\le\frac{220\,000\,000}{V}
\le\frac{220\,000\,000}{s^3}.}
\tag{BB4}
\]

The useful exact η_s formula is substantially smaller than this human-readable generous uniform constant. The older AA4-BA relative-variance upper is O(s^-3/2) and does not require the new two-line geometry; the present BB3 bound becomes strictly numerically sharper for sufficiently large s but may be weaker for small s because of generous P2 factors.

Because parent #561 had already proved \(\mathbb E_g R_{\rm GOOD}(f,g)\ge s^6/128\), Chebyshev gives the following **quenched** all-h-large statement, uniform over the fixed f and E but NOT over an adversarial individually fixed g:

\[
\boxed{
\Pr_{g:\operatorname{im}g=E}
\bigl[R_{\rm GOOD}(f,g)<s^6/256\bigr]
\le \min(1,4\eta_s)=O(s^{-3}).
}
\tag{BB5}
\]

## Proof — exact global permutation 2nd moment

Choose two source line triples independently according to weights w/B. If they share **ZERO** original LINE IDs, the six distinct right image edges form an ordered without-replacement 6-tuple. Two independently chosen internally distinct edge triples have probability q that their two sets are disjoint; the unconditional probability that BOTH opposite-port indicators are 1 is p². Conditioning on disjointness gives <=p²/q. This is true for clean filtering too, because the clean support is a fixed function of E, not of its line-ID assignment.

If they share **ONE** original LINE ID, freeze its physical image e. The physically opposite-port condition allows at most H=2t² ordered completions of the two other distinct edge images, regardless whether this shared image acts as center or outer; this gives at most V H²/(V)_5=P1. CLEAN filtering can only reduce the count.

**NEW exact-two-line physical joint bound.** If the triples share EXACTLY two distinct original line IDs, they collectively use four different line IDs and hence four distinct right image edges under the same global permutation. The two shared images can appear in two structural classes:

* If at least one of the two triples uses one shared line ID as center and the other as outer, the images of these two shared IDs must intersect in exactly one physical coordinate. For the ordered roles there are at most 2Vt possible shared physical image pairs. Conditional on these shared edges, **each** triple has at most 2t choices of its one remaining image edge (center+outer fixes the opposite port at most t; two outer images permit at most four center pair edges, at most 2t for a>=4). Ignoring clashes between these remaining edges is a safe overcount. Thus at most 8 V t³ favorable ordered 4-tuples.
* If BOTH triples use the two shared source lines as their two OUTER slots (the centers are the two different unshared lines), there are at most (V)_2 ≤V² ordered shared physical image pairs. Given any two distinct physical outer edges, at most FOUR physical center pair edges join one endpoint of each outer edge so as to meet opposite endpoints; therefore the two different center images admit at most 4²=16 ordered choices. All a>=4 satisfy t³=(a−2)³>=binom(a,2)>=V, hence total <=16V²<=16 Vt³.

The union is not added: each fixed overlap pattern is in **one** of those two alternatives. Therefore

\[
\boxed{ {\Pr}_g(J_1=J_2=1\mid \text{given exact shared original LINE positions})
\le \frac{16Vt^3}{(V)_4}=P_2.}
\tag{BB6}
\]

The bound holds without any physical source-line independence assumption; it follows from actual injective **single whole-global g** and K_a endpoint geometry.

If they share **THREE** original LINE IDs, the two indicators need not be identical because their ordered center/outer positions may be permuted. Nevertheless \(\Pr(J_1=J_2=1)\le\Pr(J_1=1)=p\).

Condition on the first weighted source triple: the probabilities that the second shares at least one, at least two, or all three unordered source LINE IDs are respectively ≤3M1/B, ≤3M2/B, and ≤M3/B by union bounds over its three singleton labels, its three pairs and its unique full unordered triple. These events overlap but the upper-bound decomposition deliberately **overcounts** nonnegative joint terms; no missing negative contributions result. Consequently

\[
\mathbb E R^2/B^2\le
\frac{p^2}{q}+
\frac{3M_1}{B}P_1+
\frac{3M_2}{B}P_2+
\frac{M_3}{B}p.
\]

Subtract the exact square of the mean B²p², normalize and obtain BB1.

## Proof of new all-h original source triple-overlap influence

Parent AA4-BA already bounded M1 by 5d³t² and M2 by 8d³t for ANY complete genuine symplectic source f and also for point-CLEAN restricted source triples (removing events cannot increase any raw overlap mass).

NEW: fix THREE different actual original LINE factor IDs {j,k,l}. Each ordered triple supporting exactly these three labels must choose one of the at most 3! = 6 permutations into center and two outer line slots. For every such permutation, the original center incidence (p,center-line) has at most d choices of ORIGINAL point p; the first outer original point has at most d choices on the fixed first outer line; the second has at most d choices on its fixed original second outer line. Thus at most d³ original point-factor triples for that permutation. Discarding physical point-opposite and CLEAN tests increases counts, and every source original incidence ID is fixed by its point+line factor. Therefore M3≤6d³ for EVERY fixed genuine original source f, independent of any globally injected original g, across ALL dyadic h>=1. This does not invent a synthetic incidence geometry or count flag-ID permutations as distinct motif sets.

Parent #561 proves the CLEAN induced physical support rooted energy T°(F)>=V²/16 for EVERY complete globally injected original physical support F when h>=5. Hence for both independent typed globally occupied original support images f and E, B≥B0 and p≥p0. Substitute the original source incidence influence and physical joint bounds to obtain BB3.

For BB4, use the following **actual all-h inequalities**, not a finite empirical extrapolation: minimal palette gives t(t+1)<2V, hence t²<2V and t≤2√V. For h>=5, V>=30 and d>=33 so (d−1)(d−2)>=d²/2. Thus B0>=d³ V²/32, p0>=1/(8V), M1/B0<=320/V, M2/B0<=512/V^(3/2), M3/B0<=192/V², P1<=256/V², P2<=2048/V^(3/2), and q^-1−1<=30/V. Inserting into BB3 yields at most

\[
\left(30+3\cdot320\cdot256\cdot64
+3\cdot512\cdot2048\cdot64
+192\cdot8\right)/V
=217\,056\,798/V<220\,000\,000/V.
\]

In particular the exponent is rigorously O(1/V)=O(s^-3). Chebyshev BB5 uses the true AA4-AZ GOOD expectation lower from #561, not an incorrectly presumed universal fixed-g value.

## Reproducible independent falsifiers

* **Independent physical kernel:** for K4/K5/K6, enumerate all exact two-common-original-line position patterns of two ordered 3-line events (18 patterns for each a) and ALL distinct right image 4-tuples; compare actual rational joint probability against the independently derived P2. No random sample is substituted for the full physical four-image census. A separate 6! complete-global-right-bijection census on K4 computes exact means, covariances and total variance for weighted source test triples.
* **True original W32:** four fully globally injected complete actual symplectic source f/g fixtures; separately enumerate original source center and two outer incidences directly (not calling new weighted source helper), with independent CLEAN physical bad-coordinate restriction, count full three-line overlap contributions and compare to the AA4-BA source w and AA4-AZ true-original GOOD expected mean.
* **True original W34 GF4:** lex/random complete source typed f/g with K14 support containing six missing physical pair edges; compare new exact mean against source #561 oracle and ensure original three-line overlap M3 obeys d³ factor cap; actual fixed-g GOOD opposite count remains distinct.
* **Large dyadic algebra:** exact integer and Fraction symbolic envelope for h=5..33 plus h40,48,64,80. Check η_s V≤220e6 as a falsifier of the manually derived all-h inequalities, NOT a substitute proof. Reject malformed repeated original LINE IDs, uninjective physical right edge supports, and unproved small h domain.
* **Gauge:** physical coordinate permutations on the RIGHT and all-original coherent source ID permutations leave the exact quenched mean and overlap envelope invariant. No per-source six-Q global map changes.

## Non-implications and next genuine deterministic blocker

This result is an **order-three original source GOOD-port permutation variance** theorem. Its stronger relative-variance decay does not rule out a fixed extremely rare adversarial globally injected original line map g with vanishing GOOD opposite wedges, and does not yield accepted six-source-ID seven-GF(5) motifs via the original 3×3 source Hall gate. Parent #544 already proved O(s^-3) for a distinct D6 six-source-ID objective; no general probability-method discovery or R3/ASET bound is claimed here.

**Next appropriate mathematical challenge:** prove anti-alignment cannot concentrate in ANY fixed original f,g using the full original symplectic incidence tensor, OR construct a genuine all-h globally injected correlated counterfamily. Then independently lift fixed-g GOOD opposite threeflag mass through the original physical T/P residual, true GQ forest 3×3 Hall selection and seven-GF5 accepted six-ID gate. An η_s→0 random-g theorem, regardless of its exponent, does not close this. Keep the scientific Draft stack and issue #230 OPEN_WITH_FORMAL_BLOCKER; final exact-HEAD hosted dedicated, INDEX, Proof Audit, Full Research and independent mathematics referee are separate gates.
