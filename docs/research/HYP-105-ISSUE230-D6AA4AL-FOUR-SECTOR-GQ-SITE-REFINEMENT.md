# HYP-105 / #230 — AA4-AL: true ORIGINAL four-sector B/A Hall cap from cross-spoke site injection

**Restricted all-h, all-globally-injected-maps deterministic UPPER on a full physical-A genuine-source B/A (dual A/B) cohort.** Child of [AA4-AK #525](https://github.com/definitely-stable/Mathlab/pull/525), exact pinned parent head \`5764f424c7fe90b920a6c4cdbd7211f325104393\`. This is not a positive lower bound for accepted GF5, not a counterfamily, and does not close HYP-105 issue #230 Branch A/B/C. Research-only four files, separate GitHub-hosted CI and mathematical independent referee required.

## 1. Precisely what is old, and what is newly proved

Prior sources and dependencies (do not misattribute their results):
- [AA4-AH #517](https://github.com/definitely-stable/Mathlab/pull/517): exact SIX true-original 2×2 source rook channels for *disjoint pinned* split two-triangle A patterns; no full positive Hall guarantee.
- [AA4-AJ #521](https://github.com/definitely-stable/Mathlab/pull/521): exact TWO crossed-spoke connected-C6 templates plus FOUR internal-link templates for disjoint physical opposite pins, source-degree upper \`48d²+192d\`.
- [AA4-AK #525](https://github.com/definitely-stable/Mathlab/pull/525): exact adjacent opposite pinned connected-C6 source-neighbor transfer, true source upper \`24d²\`, combined with the already exact AJ disjoint connected-C6.
- Parallel sibling [AA4-AK #524](https://github.com/definitely-stable/Mathlab/pull/524): exact **entire** genuine original physical-A transfer, including the *adjacent same-component two triangles* sector; uniform all-cohort accepted source six-Q cap \`72d²+192d\`. This sibling is NOT in the ancestry of #525; the adjacent same-triangle source-neighbor algorithm is independently reimplemented here solely for the purpose of combining the stricter bounds, and is **not** claimed as a novel independent theorem.

**NEW AL-1:** For each of the 2 crossed-spoke endpoint pairings and 6 true-original 2×2 row partitions, the genuine GQ/source GQ-girth8 and ONE global opposite physical factor injection imply at most **d, not 2d, physically eligible sites that pass the real original 2-rook condition**. This reduces the universal per-cohort crossed-spoke source-Q upper to \`12d²\`, versus the previous \`48d²\`. This is a real quantifier-preserving refinement, distinct from the analogous *split-two-triangle* site injection in parallel #523 and applies specifically to CROSSED-SPOKE C6 source channels.

**NEW AL-2:** Combine AL-1 with the previously accepted formulas for the other A sectors and with the adjacent C6 sharp bound of #525. Result: the entire genuine ORIGINAL A factor class conditional on a first B-source root+two actual original pinned flags+one occupied original B-C4 has the universal source-Q upper

\[
\boxed{
T_{\rm full\ A}(p,\{\ell_0,\ell_1\},\mathbf q;f,g)
\ \le\
\max\{18(s+1)^2+192(s+1),\,48(s+1)^2\}.
}
\]

In particular, for **all** \(s=2^h\ge8\), arbitrary TWO complete globally injected typed source factor physical pair maps f,g, and **each individually fixed genuine original source cohort**:

\[
\boxed{T_{\rm full\ B/A\ or\ A/B}\le48(s+1)^2.}
\]

This is numerically a strictly smaller all-h real-original cohort cap than the sibling #524's \`72(s+1)²+192(s+1)\`; for \(s=2,4\) the exact max expression is retained. The theorem is an **upper**: physical A/Hall acceptance can be ZERO in certain cohorts, and a universal \(S_s=\Omega(s^6)\) lower is NOT deduced.

## 2. Mathematical formalism: same ACTUAL source and ONE global pair of maps

Let original W(3,s), \(s=2^h,h\ge1\), have \(V=(s+1)(s²+1)\) points and lines, degree \(d=s+1\), source incidence graph girth EIGHT. Let \(a=\min\{t:\binom{t}{2}\ge V\}\) and \(K=\binom a2\). Fix **any** two complete independently typed but arbitrarily correlated global factor maps \(f:P\hookrightarrow E(K_a)\), \(g:L\hookrightarrow E(K_a)\), each globally injective across the original V typed factors. Their values remain fixed for EVERY selected original incidence Q, with physical unused edges \(K-V\) retained, no full-K_a surjectivity when K>V. Point/line duality is literal under swapping the typed factor maps and source incidence endpoints.

Select exactly six actual original incidence IDs: two source flags at one repeated B point p with two **different ACTUAL** opposite line factors \(\ell_0,\ell_1\), and four true original flags at FOUR different singleton B-side source factors \(q_0,\dots,q_3\), each with one selected opposite actual line factor. Require the globally fixed physical B images of \(p,q_0,\dots,q_3\) form B: root edge disjoint from one complete physically occupied C4 on q0..q3. On the opposite side require the actual six globally physical edges to form an A six-coordinate six-edge 2-regular graph. Such an A physical factor is either two disjoint C3 or one connected C6. The two pinned opposite physical edges are DISTINCT by g-injectivity and have either one physically shared coordinate (adjacent) or none (disjoint). These cases form a partition of the entire B/A (dual A/B) A geometry.

## 3. NEW AL-1 proof: crossed spoke site y injects into degree-d original source neighborhood

Fix the physically disjoint actual opposite pinned pair images \(e_0=\{u,v\}\), \(e_1=\{w,x\}\). The two crossed-spoke connected-C6 physical templates from #521 correspond to the physical endpoint pairings

\[
(\{u,w\},\{v,x\}),\quad
(\{u,x\},\{v,w\}).
\]

In one fixed endpoint pairing \((\{r,t\},\{r',t'\})\), an auxiliary physical site y different from all four pinned endpoints is eligible for a 2-spoke exactly if **both** globally physical edges \(\{r,y\}\), \(\{t,y\}\) belong to im(g). Because g is globally injective, they invert to TWO distinct actual original opposite source factors \(t_0(y),t_1(y)\).

Fix any original source row pair \(S=\{i,j\}\subset[4]\) with i≠j. The physical site y is **source-valid for S** iff the genuine original 2×2 bipartite incidence matrix between rows \(q_i,q_j\) and opposite source columns \(t_0(y),t_1(y)\) has a perfect matching. The true GQ **forbids source C4**, so this 2×2 matching is UNIQUE: simultaneous straight and crossed matchings would imply the two distinct real original B-source factors \(q_i,q_j\) share TWO different actual original opposite neighbors \(t_0,t_1\), impossible in a genuine GQ. Let \(\phi_S(y)\) be the actual opposite original factor assigned to \(q_i\) in that unique matching. Then

\[
\phi_S :Y_S\hookrightarrow N_{\rm ORIGINAL}(q_i)
\]

is **INJECTIVE**. Indeed, if y≠y' share \(\phi_S(y)=\phi_S(y')=t\), their global physically fixed pair image g(t) would have to be one of \(\{r,y\},\{t,y\}\), and also one of \(\{r,y'\},\{t,y'\}\). The pinned coordinates r,t are distinct from y,y', so those FOUR canonical unordered physical edges are all distinct for y≠y'. This contradicts global injectivity and the well-defined single image of the real source factor t. Importantly the physical pair map is **ONE shared g, NOT redrawn per y or per original incidence Q**.

Each genuine original row \(q_i\) has EXACTLY d=s+1 genuine original opposite neighbors, hence

\[
\boxed{|Y_S|\le d,\quad |Z_{S^c}|\le d.}
\]

For the two crossed-spoke templates and six possible original row bipartitions S, the actual ORIGINAL accepted six-distinct-incidence-ID source-Q count is **exactly** the sum of its corresponding six-channel occupancies, with y=z excluded to maintain SIX different physical coordinate vertices:

\[
T_{\mathrm{cross}}
=\sum_{b=1}^2\sum_{S\in\binom{[4]}2}
\bigl(|Y_{b,S}||Z_{b,S^c}|-|Y_{b,S}\cap Z_{b,S^c}|\bigr)
\le 2\cdot6d^2=\boxed{12d^2}.
\]

All six source incidences are genuine original source flags. No 2×2 original matching multiplicity is discarded: source girth8 gives at most ONE per 2×2 site, and original full induced C8 double completion across all four source rows appears as two separate S products. The all-h exact transfer algorithm in #521 is reused as an INDEPENDENT accepted-count reference, but a **different** code path constructs every y→real opposite source-factor witness and checks injectivity separately.

## 4. NEW AL-2 full physical A sector table and resulting universal upper

For each ACTUAL pinned original source pair and first physical B C4:

| Opposite pinned physical relation | A topology | True original accepted six-Q upper | Mathematical source |
|---|---|---:|---|
| Disjoint | Two separate physical C3 | \(6d^2\) | AH six unique 2-rook channels and actual per-site source degree |
| Disjoint | Connected C6: TWO crossed-spoke templates | **\(12d^2\)** | **NEW AL source-neighbor site injection above** |
| Disjoint | Connected C6: FOUR internal-link templates | \(192d\) | AJ one internal yz matched to genuine degree-d source edge |
| Adjacent | Two physical C3, pinned edges in SAME triangle | \(24d^2\) | Exact two source-neighbor canonical triangle edges, independently implemented; known sibling #524 |
| Adjacent | Connected physical C6 | **\(24d^2\)** | AK #525 12 ordered genuine-source internal row choices ×d² ×2 |

Totals are

\[
\begin{aligned}
T_{\rm disjoint}&\le6d^2+12d^2+192d
=\boxed{18d^2+192d},\\
T_{\rm adjacent}&\le24d^2+24d^2
=\boxed{48d^2},\\
T_{\rm full\ A}&\le\max(18d^2+192d,48d^2).
\end{aligned}
\]

The second bound dominates when \(48d^2\ge18d^2+192d\), i.e. \(d\ge6.4\). For dyadic true original GQ orders, this is exactly s≥8. At s=2 and s=4, do not falsely apply the 48d² specialization; use the displayed exact max. The parent/sibling earlier loose all-h 72d²+192d upper is thereby **strictly improved for every h≥1**, independently of the chosen maps, actual source root, pinned source flags and physically occupied B-C4. The bound is intentionally not described as sharp in the worst-case full original cohort; only the site ≤d lemma is an injection theorem, and its simultaneous saturation in all channels is not asserted.

## 5. Independent original-GQ exact finite evidence and negative controls

**Symbolic all h=1..43:** exact integer d, analytic per-sector cap, exact disjoint/adjacent max crossover, strictly smaller previous bound and explicitly FALSE all-map positive lower claim.

**W(3,2):** on FIVE genuine global typed injections: zero-split, lex, reverse, S68, S72, both original B/A and A/B orientations, iterate ALL true original 15 roots ×three actual selected root-flag pairs ×three fully occupied complementary B physical C4s =135 anchored original source cohorts per orientation and map. Every single new exact combined accepted source-Q count is compared against **unrelated** complete physical A twofactor enumeration followed by genuine original 4×4 source incidence permanent (0/1/2). Also independently aggregate and check historical full true-original B/A/A/B sector totals. The zero-split W32 true original totals are **46 accepted B/A Q** and **61 accepted A/B Q**, including split physical C3=0/0, adjacent same C3=6/3, disjoint connected C6=17/41, adjacent connected C6=23/17. Counts refer to actual six different ORIGINAL incidences, not distinct physical H only.

**W(3,4), true symplectic source:** lex/random globally complete but nononto K14=91 physical images of 85 true original source points/lines (six holes), both typed sides and both pinned opposite physical adjacency classes; independent physical H and original perfect matching vs full new exact source transfer. Source-mapped crossed-spoke auxiliary site y→actual original neighbor factor IDs must be INJECTIVE for each of six S and each of TWO crossed endpoint patterns and have size ≤5.

**W(3,8), true source:** lex/random K35=595 physical pair images of 585 genuine original source point/line factors (ten holes), both typed sides and both pin relations, independent physical A original-rook oracle for selected real source cohorts, with all per-site witnessed original factor sets size ≤9.

**Automorphism test:** a single common symplectic source automorphism on genuine W(3,2), accompanied by independent physical alphabet permutations on the two typed maps, preserves the original accepted full A source-Q count when tracking exactly the **same transported real source root, two true source flags and the same original B C4 quartet**. Negative fake source incidence truncation, noninjective opposite physical labels, repeated selected original source factors, missing first physical B-C4, non-dyadic powers fail explicitly.

No finite W32/W34/W38 empirical table is used to infer s→∞ all-map positive accepted mass; the all-h upper follows solely from true GQ source degree/girth plus globally coherent typed injection and already proved per-topology source assignment identities.

## 6. Decision and next genuinely open proof gate

**PROVED within true ORIGINAL selected six-Q model, all h, any globally complete typed pair maps f,g:** novel cross C6 source-site injection cardinality ≤d; tighter accepted crossed-spoke six-Q upper 12d²; all four physical-A sector accepted genuine original B/A/A/B global-map upper max{18d²+192d,48d²}; specialization full upper 48(s+1)² for all s≥8. These are scientifically RESTRICTED all-map UPPERS; independent mathematical referee needed for acceptance.

**NOT proved:** any positive all-global lower for true B/A or A/B, simultaneous compensation of other GF5 classes including D6, issue230 Branch A/B/C, full R3 and ASET exponent, an infinite counterexample family. Upper bounds may coexist with accepted count ZERO; physical pre-Hall mass does not automatically produce genuine original 4-rook matchings.

**Next meaningful route:** attempt a genuinely lower-bounding global **source-neighbor/physical-incidence tensor correlation** using all four exactly classified physical A sectors, and couple to other five chosen GF5 classes. The present stronger upper provides a tighter obstruction benchmark for any proposed constant or overoptimistic power-law Hall-transfer lemma. A sufficient safe indexed Hall-positive transfer lower of order s^-8 is NOT contradicted by an upper O(s^-1) or smaller; no false negative Branch A inference.

**Integration:** keep as Draft strictly atop #525; #524 sibling full-sector algorithm already overlaps but our tighter proof/certificates are additive and intentionally disclose it. Exact FINAL child SHA dedicated/index/proof-audit/full-research GitHub-hosted successful evidence AND independent mathematics review before canonical RCP JSON claim registration or rebasing/stack merging. Once accepted, regenerate five derived Markdown registry pages from authoritative JSON only. Root #230 stays OPEN.
