# HYP-105 / #230 — AA4-BQ: one simultaneously corrected original POINT+LINE pair for mixed B/A and A/B roots

**Scientific Draft strict child of [AA4-BP PR #586](https://github.com/definitely-stable/Mathlab/pull/586), parent exact HEAD 40bc3ab8f81690e7141e39de97d66fb755909f90.** Genuine original symplectic W(3,s), s=2^h, all original source incidence IDs retained on BOTH sides, globally injected typed physical pair-edge maps, no artificial high-h GQ. No main/accepted registry edit or branch A/B/C closure.

## Frontiers and distinct novelty

[#580](https://github.com/definitely-stable/Mathlab/pull/580) already proves the exact global permutation assignment test and shortest image-owner transpositions for selected source IDs. [#583](https://github.com/definitely-stable/Mathlab/pull/583) already proves that TWO same-typed BL-regular true source cherries can simultaneously be repaired on ONE global right map. [#585](https://github.com/definitely-stable/Mathlab/pull/585) already extends same-typed original cherry simultaneous repair to k≤floor((s+1)/6); our direct parent [#586](https://github.com/definitely-stable/Mathlab/pull/586) gives k=Theta(s) same-typed repair with a smaller explicit budget. Separate [#581](https://github.com/definitely-stable/Mathlab/pull/581) and [#584](https://github.com/definitely-stable/Mathlab/pull/584) concern single-root distance-three and family-size refinements. None is rebranded as novel.

**New problem:** for some original source cherries the repeated source factor is a POINT, while for others it is a LINE. The FIRST category needs to modify the right original LINE map g to obtain B/A; the SECOND needs to modify the left original POINT map f to obtain A/B. If these two repairs are run independently, a new f may destroy point-side physical B of a previously selected POINT source cherry; a new g may destroy LINE-side physical B of a LINE source cherry. This cross-type mutual sabotage is the missing complication. A same-typed theorem cannot be applied twice without freezing all original B-side source factors used by the opposite category.

**AA4-BQ new scoped contribution:** a two-sided protected-original-factor source/physical Hall theorem that lets any k=Theta(s) arbitrarily chosen BL-regular roots of BOTH types be simultaneously accepted on ONE **corrected pair** (f',g'), in ≤4k total WHOLE original source-factor image transpositions, while the original entire source incidence graph, full occupied physical supports, every rooted opposite pin and EVERY originally constructed B-side source factor image remain fixed.

## Definitions and exact all-h theorem

Let s=2^h,h≥5; V=(s+1)(s²+1), d=s+1 and a the minimal physical palette with binom(a,2)≥V, m=binom(a,2)−V≤a−2. Fix ANY authentic original W(3,s) and ANY TWO complete globally injected (possibly adversarially correlated) typed original source factor pair-edge maps f: original POINT IDs→E(K_a), g: original LINE IDs→E(K_a). The two physical alphabets are typed and distinct. No GQ automorphism of f or g is assumed.

Select ANY k_P≥1 DIFFERENT actual original POINT cherry roots, each consisting of two DIFFERENT authentic incidence flags (p,l1),(p,l2) with the SAME original POINT source factor p. Also select ANY k_L≥1 DIFFERENT actual original LINE cherry roots, each consisting of two genuine source flags (p1,l),(p2,l) with the SAME original LINE source factor l. Let k=k_P+k_L.

Each point-root is called **opposite-pin regular** if every physical right vertex of its two original g(l1),g(l2) images has missing occupied RIGHT physical incident edge degree ≤floor((a−4)/8). Each line-root is called **opposite-pin regular** if every physical LEFT vertex of its two original f(p1),f(p2) images has missing occupied LEFT physical incident edge degree ≤the same threshold. This is the same AA4-BL local physical support condition, applied to the typed opposite map. Both physical supports independently have at most m missing pair edges. Existing #577 guarantees >3/4 of each typed source root population is individually eligible for EVERY full f,g, but says nothing about cross-type common repairs.

Set

\[
\boxed{
k_{\mathrm{mixed}}(s)=\min\left\{
\left\lfloor\frac{s-4}{8}\right\rfloor,
\left\lfloor\frac{a-4}{20}\right\rfloor
\right\}.
}
\]

For h≥5 this is at least 3 and grows Θ(s). Consider any 2≤k≤k_mixed(s), with k_P,k_L≥1 and the described rooted original incidence flag IDs all different *inside their twoflag pairs* (incidence flags may be shared among different roots).

**AA4-BQ theorem:** For every such completely given original f,g and EVERY mixed-type collection of k opposite-pin regular genuine cherry roots, there exists ONE pair of complete globally injected original source maps (f',g') such that

1. f' and g' use exactly the SAME respective occupied physical pair-edge supports as original f and g, and share the SAME source authentic W(3,s) graph and original source incidence flag IDs throughout.
2. Each original source factor ID occurring as an opposite-side **root pin** in any chosen cherry preserves its entire currently occupied original physical image, and every original source factor used on the B-shaped first physical side of each selected source witness is also frozen throughout the opposite-type repairs.
3. The pair (f',g') is reached from the GIVEN pair (f,g) by at most **4k_L WHOLE ORIGINAL POINT factor-image transpositions** to form f', and at most **4k_P WHOLE ORIGINAL LINE factor-image transpositions** to form g', total ≤4k. Every intermediate original typed map remains a complete global injection onto its same original occupied edge support.
4. On ONE SAME final (f',g') there are k DISTINCT sets Q_i of SIX authentic distinct original W(3,s) source incidence flag IDs. Every POINT-root's Q_i is historically accepted GF(5)-positive B-left/A-right, and every LINE-root's Q_i is historically accepted GF(5)-positive A-left/B-right. All k are true six-source-ID sets on the same source and physical maps, not separately corrected partial projections.

The theorem does **NOT** imply positive accepted GF(5) motifs on the original UNMODIFIED pair (f,g), does **NOT** allow one mixed fixed map to work for all possible root sets, and does NOT close root Branch A/B/C or a full R3/ASET bound.

## Constructive proof

### BP/BQ-1. Choose physical B-side original source skeletons on BOTH typed sides *BEFORE EITHER MAP IS MODIFIED*

For every selected original POINT-root, use the existing physical point pair-image f(p) to find an occupied simple physical C4 on four physical left vertices outside its two saturated endpoints. Previous #575/#576 prove such an occupied C4 exists under m≤a−2 for every f and every genuine original point root at h≥5. Invert its four distinct occupied physical pair-edges through the globally injective f to FOUR distinct additional authentic original POINT factor IDs. Together with root p, this gives **FIVE** original POINT source factors to freeze on the f side: every subsequent POINT-label transposition for LINE-root corrections MUST avoid these entire five physical images.

Symmetrically for every selected original LINE-root, find a physical line-edge C4 on four occupied right physical vertices outside the two saturated endpoints of g(l), invert through globally injected g to FOUR distinct other original LINE source factors. Together with root LINE factor l this gives **FIVE** original LINE source factor images frozen on g for the entire mixed correction.

In addition, freeze the opposite source factor IDs of EVERY chosen original pair of flags: each POINT-root supplies two genuine original LINE source factor IDs which are pinned on g; each LINE-root supplies two genuine original POINT source factor IDs pinned on f. The union F_P of frozen original POINT IDs and F_L of frozen original LINE IDs therefore obey

\[
\boxed{|F_P|\le5k_P+2k_L,\qquad |F_L|\le5k_L+2k_P.}
\tag{BQ-FROZEN}
\]

These are actual global source factor ID sets. The same factor can appear in several source skeletons and pins, and common factors are frozen consistently to their *existing unchanged* physical images. The two physical pair alphabets remain typed; the same integer source ID across types is not automatically the same factor.

### BQ-2. Complete actual source sixflag witnesses with globally disjoint free factor IDs

Process all selected roots in an arbitrary deterministic order. For a given source type B root, its B-side source skeleton consists of its two authentic original root flags on p or l plus four distinct extra B source factors q1,..,q4. Every genuine original W(3,s) source factor has exactly d=s+1 genuine incidence neighbors on the OPPOSITE original type. Choose ONE true incidence flag on each of the four extra B source factors, greedily avoiding ALL previously frozen authentic opposite source factor IDs F_opposite, the up-to-4(k_same−1) previously chosen free opposite factors for roots of this same type, and the at-most-three source factor IDs chosen earlier on this very witness. The number prohibited at any choice is bounded by

\[
\begin{aligned}
T_{\rm free\,LINE} &\le|F_L|+4(k_P-1)+3
\le 5k_L+6k_P-1\le6k-1,\\
T_{\rm free\,POINT} &\le|F_P|+4(k_L-1)+3
\le 5k_P+6k_L-1\le6k-1 .
\end{aligned}
\tag{BQ-HALL}
\]

For k≤floor((s−4)/8) and s≥32 these are STRICTLY LESS than d=s+1. Thus an actual distinct original neighbor always exists regardless of correlation of f,g or original source geometry. Every resulting sixflag Q has SIX different original incidence flag IDs and six different opposite SOURCE factor IDs, giving an original B/A source factor profile for point-roots and original A/B profile for line-roots. All 4k_P free original LINE IDs and all 4k_L free original POINT IDs are globally pairwise distinct within their own types and avoid the entire frozen opposite factor set.

### BQ-3. Occupied physical A-side target C6 with *extra B-protected source factor images*

On the opposite physical side of each rooted sixflag Q, its two previously fixed root opposite source factor images are distinct occupied physical edges of K_a and satisfy the BL-local missing physical edge degree condition. Parent #577 gives the same occupied physical canonical C6 counts, adjacent ≥(a−3)(a−4)(a−5)/2 and disjoint ≥(a−4)(a−5)/2, on its FIXED original occupied physical image support.

When choosing the target C6 of a POINT-root (target on g physical line side), forbid ALL other right physical images of the frozen true original LINE source factors F_L apart from its two exact root images, plus ALL previously selected free right physical pair edges for other POINT-root witnesses. Likewise, when choosing a LINE-root target C6 on f physical point side, forbid all other f(F_P) apart from that root's two images, plus previously selected free left physical target edges from other LINE-root witnesses.

For the last root of each type, these forbidden occupied physical edge budgets are at most

\[
\begin{aligned}
E_{\rm right}&\le|F_L|-2+4(k_P-1)
\le5k_L+6k_P-6\le6k-6,\\
E_{\rm left}&\le|F_P|-2+4(k_L-1)
\le5k_P+6k_L-6\le6k-6.
\end{aligned}
\tag{BQ-C6-FORBID}
\]

A single additional arbitrary physical pair edge exclusion destroys at most (a−4)(a−5) adjacent two-pin canonical C6 or (a−5) disjoint two-pin canonical C6 (pinned in parent #583 and repeated in #586). For k≤floor((a−4)/20), \(6k-6<(a-4)/2\). Both canonical 6cycle survivor bounds therefore remain STRICTLY positive, for every given opposite physical pair map and each actual root regardless of other typed map correlations.

Choose an occupied simple physical right C6 for each POINT-root and an occupied simple LEFT C6 for each LINE-root such that the four FREE physical target pair edges are disjoint from ALL frozen physical factor images on that type and from earlier target-free pair edges of that type. The two target maps are selected **together with a global cross-type protected-factor constraint**, not independently and later allowed to damage each other's B-side source projections.

### BQ-4. ONE simultaneous pair of full source image permutations

For each POINT-root's genuine Q, prescribe its four free ORIGINAL LINE factor IDs to the four free occupied right physical target edges of the chosen line-side C6. All such prescriptions on g are distinct in source and target and use neither frozen original LINE factor IDs in F_L nor their original occupied physical pair edges g(F_L). By the exact parent #580 partial owner-permutation theorem, ONE complete globally injected g' onto the old right support exists with at most 4k_P whole original LINE-factor image swaps, preserving the ENTIRE F_L (not merely the explicit LINE pins of point roots) at EVERY step.

Likewise, prescribe the four free ORIGINAL POINT factor IDs of every LINE-root's genuine Q to the four free occupied left physical C6 edges, disjoint from every frozen original POINT source factor F_P and f(F_P). The exact source owner matching produces ONE complete globally injected f' with at most 4k_L whole original POINT-factor image swaps, preserving the ENTIRE F_P at EVERY step.

Now observe the crucial cross-type protection: the physical POINT-side B projection of EVERY selected POINT-root Q is made entirely from original POINT source factors in F_P, hence is UNCHANGED under the f→f' process while the LINE-side A target is reached by g→g'. Conversely the LINE-side physical B projection of EVERY LINE-root Q is made entirely from original LINE source factors in F_L, hence is UNCHANGED under the g→g' process while its POINT-side A target is reached by f→f'. The actual original six-incidence-ID Q stay frozen.

Therefore ALL k accepted historical GF(5) B-left/A-right and A-left/B-right source sixsets survive **simultaneously on the SAME joint final (f',g')**. The two types of accepted original Q cannot collide as source six-element sets: a POINT-root B/A Q has original POINT B-source factor multiplicity (2,1,1,1,1) and original LINE A-source multiplicity (1,1,1,1,1,1), while a LINE-root A/B Q has exactly the opposite source multiplicities. Same-type Q are different because the unique repeated source factor and the two original flags of its cherry uniquely determine the root. This completes the all-h mixed theorem.

## Quantifiers, limitations, test methodology

The eligible set for each type contains MORE THAN 3/4 of its own N=V·binom(s+1,2) actual source cherry roots for EVERY already fully fixed pair f,g (prior #577 with source point/LINE dual). The theorem is for **ANY chosen mixed k-set** drawn from those TWO eligible typed root sets, up to k_mixed. It does not claim all original typed roots are individually eligible or that one corrected pair works for the combined entire eligible population. Since k_mixed is Θ(s), this goes beyond the fixed k=2 same-type theorem but retains an explicit root-dependent correction.

The proof is independent of any hypothesis that the physical source image maps f and g are probabilistically independent: they may be arbitrarily correlated. It uses no fictitious GQ models at large h, no per-source-Q redraw and no false replacement of source-incidence IDs.

Reproducibility includes exact integer/Fraction h5..80 source and physical budget tests; genuine original W34 GF4 nononto K14 full typed maps with BOTH source root types (lex/random): find one or more actual mixed-type original source root collections, replay every full original POINT and LINE source image transposition independently, verify F_P/F_L pinned B source factor images and global typed physical occupied edge supports unchanged, and verify the **SAME final corrected PAIR** accepts genuine six-ID B/A AND A/B by an independent source-class classifier and literal double-physical degree-two test. Actual original W32 W(3,2) finite mixed source roots are exploratory, with no false h>=5 promotion; malformed original flag IDs, wrong source type, broken factor injections reject.

**Root #230 remains OPEN_WITH_FORMAL_BLOCKER.** This is still an existential local repair \(\forall f,g\ \forall\text{ eligible mixed roots }\exists (f'_R,g'_R)\), not a lower on the original UNCHANGED f,g, not an infinite genuine original correlated source counterfamily, not a complete R3/ASET exponent and not an accepted Branch A/B/C result. Keep scientific Draft until exact final HEAD dedicated/INDEX/Proof Audit/Full Research and an independent mathematical referee, including parent stack review.


## Independent cross-type sabotage falsifier (true original W34)

The mixed theorem must freeze **every** five-factor B-side source skeleton, not only the two opposite root images. The new independent W34 negative test takes an authentic fully corrected GF(5) B/A and A/B witness Q on one genuine original W(3,4) (nononto K14) and, for each source B-side type separately, identifies its UNIQUE doubled original source factor p. It deliberately violates the frozen-factor rule by transposing the physical pair image of p with an original source factor whose physical pair edge lies entirely OUTSIDE the six physical coordinates occupied by that Q. This perturbation maintains the original typed physical pair-edge injection and its exact occupied support but removes the pair of original physical B-root coordinates and introduces foreign coordinates used twice, so the fixed six ORIGINAL incidence IDs of Q no longer have a physical six-coordinate 2-regular projection on that side. The independent raw source factor/physical degree oracle rejects the same Q; the unmodified corrected joint pair passes. This is an ACTUAL-original-source W34 witness of the need to impose cross-type B-side freezing, **not** a claim that every imaginable modification of any B-side factor necessarily destroys all accepted GF(5) motifs, nor a root A/B counterexample.
