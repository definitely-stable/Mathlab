# HYP-105 / issue #230 — AA4-BN: genuinely original three-factor-swap rooted B/A repair for large dyadic s

**SCIENTIFIC DRAFT, strict child of AA4-BM [PR #579](https://github.com/definitely-stable/Mathlab/pull/579), pinned parent HEAD 68cda53041075028055374086e6a9a8cc78d9098.** The parallel sibling [PR #578](https://github.com/definitely-stable/Mathlab/pull/578) already proves the earlier **FOUR** source-image-swap per-root repair with multiple distinct target whole maps. We claim neither its radius-four result nor generic swap-target combinatorics as new. New here is a true-original generalized quadrangle GQ incidence **pair-packing** argument ensuring one ALREADY-CORRECT third original opposite factor image, reducing the guaranteed distance from four to THREE for every locally regular root in ALL sufficiently large dyadic cases h≥22. Do not promote a scientific Draft to an accepted root A/B/C or merge to main on CI alone.

## Model and quantifiers

Fix every actual symplectic generalized quadrangle W(3,s) with s=2^h, h≥22, original valency d=s+1 and V=(s+1)(s²+1) genuine original POINT factors and the same number of original LINE factors. Fix a=min{n:binom(n,2)≥V}, m=binom(a,2)−V≤a−2. Fix **ANY TWO ALREADY FULLY FIXED**, possibly adversarially correlated globally injected original factor physical pair-edge maps f for original points and g for original lines into their separate typed E(K_a) physical coordinate alphabets. All original source incidences I are the **genuine W(3,s) incidence graph** with all 6 selected original source flag IDs immutable on BOTH sides.

Fix ANY genuine original source POINT factor p and ANY two DIFFERENT source incidence IDs α=(p,l1),β=(p,l2), l1≠l2. Their already fixed opposite physical images e1=g(l1),e2=g(l2) are distinct occupied physical K_a edges. We say this true root is **pin-regular** when every physical right coordinate vertex of e1∪e2 has at most

\[
t=\lfloor(a-4)/8\rfloor
\]

missing incident right physical pair-edges in K_a\im(g). This is EXACTLY the condition established in parent AA4-BL [#577](https://github.com/definitely-stable/Mathlab/pull/577), not a new hypothesis fitted from finite true W32 examples. By that theorem **more than 3/4 of ALL actual source POINT cherry twoflag roots are pin-regular for EVERY fully fixed original g**. The POINT↔LINE typed dual handles source LINE cherry roots with two opposite POINT images pinned.

## AA4-BN1 — almost every original point factor can occupy a rooted physical C4

Delete the TWO endpoints of the physical root point pair-edge e0=f(p) from the source POINT physical K_a alphabet, leaving n=a−2 physical vertices. Let F be the occupied point image edges from f induced on these n vertices. At most m≤a−2=n physical pair edges of K_n are absent. Let δ_x count physical missing edges **inside this root complement** incident to vertex x. Call complement coordinate x **bad** if 4δ_x≥n−3 (i.e. δ_x≥(n−3)/4). Since Σ_xδ_x≤2m, there are at most

\[
\left\lfloor\frac{8m}{n-3}\right\rfloor \le8
\]

bad complement coordinates, because n≥259 and 8n/(n−3)<9.

**New deterministic C4-completion lemma:** Every occupied physical pair edge xy∈F with BOTH endpoints good (4δ_x<n−3 and 4δ_y<n−3) lies on an occupied simple physical FOUR-edge C4 entirely inside F. Indeed in complete K_n there are exactly (n−2)(n−3) distinct C4 through xy. Each absent other edge incident to x or y kills at most n−3 such C4; each missing edge disjoint from {x,y} kills at most TWO C4. Therefore

\[
\#C4_F(xy)\ge(n-2)(n-3)-(\delta_x+\delta_y)(n-3)-2m
>\frac{(n-3)(n-1)}2-2n>0
\]

for n≥259. No source automorphism or random f assumption. It follows that an original POINT source factor q can fail to lie on ANY occupied root-disjoint physical source C4 only if f(q) touches one of the two root physical vertices OR one of the at most eight bad complement vertices. Complete injectivity therefore bounds the number of such original **bad source point factors** by

\[
\boxed{b_{\rm point}\le(2+8)(a-1)=10(a-1).}
\tag{BN-POINT}
\]

This bound holds for EVERY individual root p and EVERY fixed source point labeling f with arbitrary physical holes; it is neither an average over f nor the earlier unconditional number of C4s from AA4-BJ.

## AA4-BN2 — GQ point-pair uniqueness forces FEW totally bad original LINE factors

Call an actual original LINE source factor \(\ell\) **bad for this root** if *ALL its d=s+1 actual incident original point factors* q are among the ≤b_point source points that have NO occupied source physical C4 in the complement of f(p). Otherwise \(\ell\) is GOOD; there exists a genuine incidence flag (q,\ell) whose original point image f(q) lies on at least one such physical source C4.

The crucial true-GQ property is that **each unordered pair of DIFFERENT original POINT source factors belongs to AT MOST ONE actual original LINE factor** (incidence bipartite graph girth≥8). Each entirely bad original source LINE factor consumes binom(d,2) unordered pairs within the set of at most b_point bad original source points, and distinct original LINE factors consume DISJOINT collections of such original point-pairs. Thus for EVERY given original f and EVERY fixed original point root,

\[
\boxed{
B_{\rm LINE}
\le \frac{\binom{b_{\rm point}}2}{\binom d2}
\le \frac{10(a-1)\,[10(a-1)-1]}{d(d-1)}
\le 400s.
}
\tag{BN-BADLINE}
\]

The final coarse bound follows from a²≤4s³ (true minimal physical alphabet for s≥4) and d(d−1)=s(s+1)≥s². This is the new genuine-source geometric gain: the physical source C4 shortfall involves O(a) original point factors, yet only O(a²/d²)=O(s) source LINE factors can have ALL of their d genuine original incident source points unusable. A method ignoring original W(3,s) incidence uniqueness would only give O(a·d) bad original line incidences and would not suffice for the next all-h physical target count.

For ALL dyadic h≥22, sqrt(s)≥2048 and a²≥2V≥2s³, so

\[
\boxed{
B_{\rm LINE}\le400s<\frac{a-4}{4}.
}
\tag{BN-SPARSE}
\]

For clarity, the inequality 400s<(a−4)/4 is checked from a≥sqrt(2s³): 1600s+4<sqrt2·s^{3/2} for s≥2^22. This is a clean conservative proven h threshold, **NOT an optimized minimum h**. It makes no claim that true W32/W34 necessarily have only a three-swap radius for every root.

## AA4-BN3 — a pinned physical right C6 avoids ALL totally bad original LINE images

Under the parent pin-regularity condition and occupied original right physical support E=im(g), AA4-BL proves explicit genuinely occupied physical right 6cycle lower bounds, retaining the two already fixed e1,e2:

- **Adjacent physical pin edges** e1=(u,v),e2=(v,w): consider the canonical physical 6cycle u-v-w-x-y-z-u with x,y,z distinct from u,v,w. The family has at least half of (a−3)(a−4)(a−5) occupied candidates.
- **Disjoint physical pin edges** e1=(u,v),e2=(w,x): consider u-v-y-w-x-z-u with y,z outside the four fixed endpoints. It has at least half of (a−4)(a−5) occupied candidates.

Now REMOVE, purely for witness selection, the at most B_LINE occupied right physical edge images g(ell) of entirely bad ORIGINAL line factors ell. They are actual ORIGINAL line source IDs, not fictional holes and not changes to g. Every extra physical edge of a candidate pinned C6 is one of the four non-pinned edges.

A single newly forbidden physical right pair edge can destroy at most (a−4)(a−5) members of the canonical adjacent-pins family (if adjacent to a pinned endpoint; edges among free vertices destroy only O(a)) and at most a−5 of the canonical disjoint-pins family. Therefore, using BN-SPARSE, there remain at least

\[
\begin{aligned}
R_{\rm adjacent}
&\ge\tfrac12(a-3)(a-4)(a-5)
   -B_{\rm LINE}(a-4)(a-5)>0,\\
R_{\rm disjoint}
&\ge\tfrac12(a-4)(a-5)
   -B_{\rm LINE}(a-5)>0.
\end{aligned}
\]

Hence **for EVERY already fixed f,g and EVERY pin-regular actual root** there is a physical right C6 in the SAME occupied im(g) which contains e1,e2 and whose other FOUR physical right edges are ALL currently owned under g by GOOD original LINE source factors. No random global reallocation, no independence of original Q, no changes to the original incidence graph.

## AA4-BN4 — keep a THIRD authentic original LINE factor image fixed; only THREE swaps suffice

Choose ANY of the four free physical right C6 edges t=g(ell) from that surviving target. Its true original line source factor ell is GOOD, hence there exists a genuine original incidence (q,ell) with q a true original point factor f(q) contained in a source physical C4 entirely outside the anchored f(p) endpoints. Choose that physical source C4, comprising four DISTINCT genuine original point source factor IDs q,q1,q2,q3. Retain the ORIGINAL two rooted flags α=(p,l1), β=(p,l2) and the third ORIGINAL incidence (q,ell) whose right physical image t is **ALREADY** one of the desired four edges and will never be changed. Choose one actual original line neighbor ell_i of each other three distinct source point factors qi, avoiding l1,l2,ell and previously chosen ell_j. Since d=s+1≥2^22+1, at most 3+j excluded line factor IDs at step j and a choice certainly exists. The genuine selected original sixflag set

\[
Q=\{(p,l_1),(p,l_2),(q,\ell),
(q_1,\ell_1'),(q_2,\ell_2'),(q_3,\ell_3')\}
\]

contains **SIX DIFFERENT true ORIGINAL source incidence IDs**, one original POINT source factor repeated (p), and SIX distinct actual ORIGINAL source LINE factor IDs. The original f point projection is the double occupied f(p) edge plus a physical C4, hence 2regular on six point-side coordinates, source factor type B.

The chosen right physical C6 already contains the unchanged e1=g(l1), e2=g(l2), and t=g(ell), so exactly **THREE** further actual original line source IDs ell_i need be assigned to its three other physical right edges. Start from the *GIVEN FULL* original globally injected g. For each of those three original source LINE factor IDs, transpose its WHOLE pair-edge image with the current original LINE source factor owner of the corresponding desired physical target pair-edge. As the three targets are different and exclude ALL of e1,e2,t, neither a previously fixed original factor nor a previously repaired source factor can be touched. All intermediate maps remain complete global genuine original line-factor physical bijections onto EXACTLY the same occupied right edge set E, f never changes, and the source incidence Q never changes.

After at most THREE source-image transpositions, the entire TRUE original sixflag Q projects to original point physical B (root double image +4cycle) and original line physical A (6cycle), hence is HISTORICALLY ACCEPTED original positive GF(5) B-left/A-right. Both ORIGINAL root line factor images and the newly selected third actual original LINE factor image remain unchanged at every step. The proof is dual for an original source LINE cherry with original POINT image transpositions, yielding A-left/B-right.

**AA4-BN main theorem:**

\[
\boxed{
\begin{gathered}
\forall\,s=2^h,\ h\ge22,\quad
\forall\text{ authentic W(3,s) global injected }f,g,\\
\forall\text{ genuine-original pin-regular POINT cherry }\alpha,\beta,\\
\exists g'\in B_3^{\rm original\ LINE\ image\ transpositions}(g),\
g'(l_1)=g(l_1),\
g'(l_2)=g(l_2),\\
\exists Q\text{ SIX distinct ORIGINAL flag IDs through }\alpha,\beta:
\quad U_{B{\rm left}/A{\rm right}}(f,g')\ge1.
\end{gathered}}
\tag{BN-3}
\]

The repair also retains an additional authentic original line image g(ell) from Q throughout and preserves the occupied image set E. By the prior deterministic parent BL-MAJ, **more than 3/4 of ALL actual source POINT cherries admit such an individual ≤3-swap repair on EVERY already given full original f,g**, and dually >3/4 source LINE cherries when exchanging the original point and line factor types.

## AA4-BN5 — what is actually new, what is not

The previous sibling [#578](https://github.com/definitely-stable/Mathlab/pull/578) and parent [#579](https://github.com/definitely-stable/Mathlab/pull/579) already guarantee radius FOUR and at least multiple distinct repaired maps for each good original root. Previous #545/#547/#548/#550 give up to radius FIVE for the **different** original D6-A/A motif. Classical physical C4 cycle counting, generalized quadrangle no-4/6-cycle partial linearity, and greedy image transpositions are not claimed to be independently new concepts. This slice's **specific new theorem** is the original GQ point-pair PACKING conversion of a near-complete physical source C4 palette into an O(s) count of bad ORIGINAL LINE source factors, a second robust pinned physical right C6 avoiding ALL their images, and the **THREE-swap** local fixed-map guarantee for EVERY pin-regular true original source root for h≥22 while preserving its two old pins plus a third true original source line factor image.

This is still **NOT** the root universal Branch A/B/C solution: \(\forall f,g\ \forall{\rm regular\ root}\ \exists{\rm nearby}\ g'\) does NOT entail the seven-class accepted GF(5) sixflag sum S(f,g)≥c s^6 on the original **UNCHANGED** arbitrary f,g. Different roots may still demand different globally corrected maps. Nothing produces an infinite actual correlated source f_s,g_s counterfamily with S=o(s6), nor a full strict R3/ASET exponent. The proof only improves local correction radius and does not imply a uniform positive number of distinct GOOD full maps without further counting.

## Reproducible independent falsifiers

A dedicated 3-job GitHub-hosted workflow is included. The mathematical h≥22 theorem is checked with **EXACT integer arithmetic** on all dyadic h22..36 and h40/48/64/80; no fake large GQ source graph is synthesized. Physical threshold \(a^2\le4s^3\), bad complement physical vertex count ≤8, source bad point factors ≤10(a−1), actual W3 source line packing ≤400s, right anchored C6 positive after deleting ALL bad original line physical images all checked.

Finite model **algorithm** checks are deliberately distinct from an all-h theorem proof:
- ALL five genuine original W32 globally injected original source W(3,2) f,g fixtures dual_zero,lex,reverse,S68,S72, original POINT and LINE dual source cherry roots. An independently enumerated physical C4-on-four-source-image-coordinate oracle checks the set of true source good point/LINE factor IDs against the new implementation's rooted C4 index. On roots where a 3swap repair is found, each intermediate entire original pair map stays globally injected onto the same physical support with ALL THREE actual source factor images pinned. The final SAME genuine original six-flag Q is accepted by independent historical seven_census GF5 source classifier on sampled repairs, not solely the production B/A checker. Some finite h1 roots may require four swaps or fail the h≥22 hypothesis and are not mislabeled as a contradiction.
- Real genuine original W34 GF4 nononto K14 (six missing physical pair edges), typed lex and random complete original source f,g, both root types. Independent literal source-geometry checks of which actual GQ original opposite source factors have no incident source factor inside ANY root-disjoint physical C4, compare with GQ pair-packing bound; for representative roots a separate original all-seven source-Hall classifier independently validates the selected original six-ID B/A or A/B positive output and replay of ≤3 legal full original source-factor transpositions, retaining all THREE fixed original source factor images.
- Independent exact target-specific 3swap optimality only in an explicitly **ABSTRACT eight-factor permutation** with three selected source factor image targets initially all owned by external source factors. A global factor-image swap can import at most one; exhaustive ≤2-swap BFS checks it is impossible to obtain precisely that target in ≤2 swaps. **NOT** asserted an optimum to ANY accepted GF5 target or a genuine W(3,s) realization.
- False h<22 theorem domain, broken typed source ID, duplicated source physical pair images, broken original source incidence flag identities fail closed.

**Scientific gates:** keep Draft on the verified parent SHA, exact final-head specialist CI, INDEX, Proof Audit, Full Research and a genuinely independent mathematical referee; no merge/canonical accepted result purely from automated checks.
