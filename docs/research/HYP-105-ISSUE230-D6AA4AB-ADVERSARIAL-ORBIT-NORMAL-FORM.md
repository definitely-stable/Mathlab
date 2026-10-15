# HYP-105 / issue #230 — AA4-AB-SYM: exact adversarial orbit normal form

**Status: research-only restricted theorem and exact finite falsifiers.** Strict child of AA4-AA-SRC PR #504 at source parent SHA af43c0ce25259e141dfe1d9cbbfdc3fa260d03ec. No production changes, no prior source-count rewrite, no RCP generated Markdown edits, and NO all-adversarial lower bound asserted. Root Branch A/B/C remains OPEN_WITH_FORMAL_BLOCKER.

## 1. Exact model, seven tags, and prohibited shortcuts

For each h>=1 let s=2^h, V=(s+1)(s^2+1), a=min{t: C(t,2)>=V}, K=C(a,2), and E_a=C([a],2). The ORIGINAL point/line factors P,L are the true typed vertices of the symplectic generalized quadrangle W(3,s) with authentic original incidence graph I subseteq P x L. Each full physical pair-map is an injection f:P->E_a and g:L->E_a, not independent choices per original sixset Q.

For Q subseteq I with six DIFFERENT actual original incidence IDs, project its six columns through f and g, respectively. Each side can have the historical physical A (six distinct source factors, six-edge physical 2-factor), B (one repeated original source factor with physical double-edge and complementary C4), C (three repeated factors each of degree two, physical matching), or none. Six-coordinate degree exactly two on each side is required. Historical GF(5) positive tags: D6 with both side A AND the identical connected C6 on the SAME six original incidence positions, B-left/A-right, A-left/B-right, C/A, C/B, B/B-overlap, B/B-disjoint. Original C/C cannot occur by genuine GQ girth eight. All seven counts refer to original Q, not signed GF5 events or arbitrarily reindexed coordinate-only patterns.

Let C_t(f,g) count actual accepted original Q of tag t. The selected scalar and fixed historical 51-palette numerator are

\[
S_s(f,g)=\sum_{t=1}^{7}C_t(f,g),\qquad
W_s(f,g)=\sum_{t=1}^{7}w_tC_t(f,g),
\]

where w_t are the immutable historical coefficients used by the original seven-signature oracle. Do NOT replace W with a uniform seven-tag weight.

## 2. Theorem AB-1: exact all-h two-map orbit invariance

Let sigma=(sigma_P,sigma_L) be ANY **single type-preserving automorphism of the ACTUAL original incidence geometry**, with (p,l) in I iff (sigma_P(p),sigma_L(l)) in I. Let pi and rho be arbitrary, INDEPENDENT, permutations of the physical coordinate alphabet [a]. Define new COMPLETE, GLOBALLY coherent maps by

\[
f'(\sigma_P(p))=\{\pi(x):x\in f(p)\},\qquad
g'(\sigma_L(l))=\{\rho(y):y\in g(l)\}.
\]

Then, for ALL h>=1, EVERY original seven-tag t and EVERY admissible f,g,

\[
\boxed{C_t(f',g')=C_t(f,g).}
\]

Consequently S_s(f',g')=S_s(f,g) and W_s(f',g')=W_s(f,g). The entire nine-cell original source forest and all original side profiles are transported to exactly corresponding source Q sets.

**Proof.** The map Q -> sigma(Q) is a bijection of size-six subsets of authentic original incidence IDs. Both original typed source endpoint multiplicity profiles and original B/B repeated-root overlap are invariant. On a side, the physical permutation maps every unordered pair to one unordered pair, preserving intersection sizes, distinct coordinate counts, six-coordinate degree-2 structure, C4, matching, connected physical C6, and two-triangle alternatives. Crucially, for type A/A, both physical coordinate-to-original-incidence-position dual graphs have edges on the **same transported Q positions**, so their equality and connectedness are invariant. Thus every historical tag indicator on Q equals the same tag indicator on sigma(Q), even though pi and rho are independently chosen. Sum over the bijection and apply the fixed integer w_t.

**Dangerous false shortcut:** arbitrary independent source permutations on P and L are NOT allowed; they need to form one common authentic incidence automorphism. Nor may one permute source incidence columns Q separately for f and g. The executable negative control rejects an unrelated source permutation that breaks authentic I.

## 3. Theorem AB-2: exact all-h anchored minimax normal form

Fix **any** actual original point p_* and any actual original line l_*. They need not be incident (choosing an incidence anchor simplifies later Hall/JPKC integration). The symmetric group S_a acts transitively on E_a, hence there are independent physical coordinate permutations pi,rho such that

\[
f'(p_*)=\{0,1\},\qquad g'(l_*)=\{0,1\}.
\]

By AB-1 this can be done WITHOUT changing any C_t, S_s, W_s or global injectivity. Therefore the minimum of S or W over all genuine complete two-map injections equals the minimum restricted to these TWO prescribed anchored physical edge images:

\[
\boxed{
\min_{f:P\hookrightarrow E_a,\ g:L\hookrightarrow E_a}S_s(f,g)
=
\min_{\substack{f,g\ \mathrm{globally\ injective}\\
f(p_*)=g(l_*)=\{0,1\}}}S_s(f,g).
}
\]

The same exact equality holds for W_s and for every functional of the entire seven-count vector. This is a true every-adversarial-map reduction, NOT a lower bound on either minimum.

Number of unanchored full injections on one typed side = (K)_V. Exact number with fixed prescribed source image = (K-1)_{V-1}. Therefore the Cartesian two-sided **anchored assignment search space is reduced by precisely K^2**, independently of the original source incidence constraints; the objective is invariant under the normalized action.

\[
\begin{aligned}
|\mathcal I| &= ((K)_V)^2,\\
|\mathcal I_{\mathrm{anchored}}| &= ((K-1)_{V-1})^2,\\
|\mathcal I|/|\mathcal I_{\mathrm{anchored}}| &= K^2.
\end{aligned}
\]

These are **assignment counts, not orbit-counts**. Further quotienting by stabilizers of the anchor, and by authentic symplectic source automorphisms, requires canonicalization and orbit stabilizer multiplicities; it is mathematically wrong to divide the anchored count by |S_a|^2 |Sp(4,s)| without checking stabilizers.

W(3,2): V=K=15, a=6, so fixing the one point physical edge and one line physical edge eliminates the factor 15^2=225 and leaves (14!)^2 actual full assignments before additional valid symmetry reductions. Even this is enormous; exhaustive minimax search is NOT claimed.

## 4. True symplectic source isometries used by the oracle

The existing true projective symplectic GQ source generator uses GF(2^h)^4 and

\[
\langle x,y\rangle=x_0y_2+x_2y_0+x_1y_3+x_3y_1.
\]

For any nonzero projective seed v, the characteristic-two transvection

\[
T_v(x)=x+\langle x,v\rangle v
\]

preserves the alternating form, is a bijection, and obeys T_v^2=id. Consequently it maps authentic symplectic points to points and isotropic lines to isotropic lines, producing a **single common type-preserving source incidence automorphism**. The finite test constructs actual point and line index permutations by projective normalization and real line-set lookup; it rejects a fake source automorphism with unpaired point/line permutations.

The algebraic theorem holds for every h. This particular Python oracle intentionally supports only h=1,2,3, with the original GQ incidence model independently regenerated and compared; it must reject unverified larger finite input rather than silently treating any regular bipartite graph as a genuine W(3,s).

## 5. Finite independently falsifiable results, no extrapolation

1. TRUE W(3,2) source transvection checks: all original 45 incidences carried to original incidences; point and line maps are bijective involutions. Independently move both complete globally coherent physical edge maps by two DIFFERENT physical coordinate permutations. Anchor arbitrary actual source factor indices. Compare exact **entire seven-tag vector, S, D6 and the certified historical 51-palette weighted numerator** against the independent 62,370-original-Q per-side join and original historical GF5 signature. S68 remains S=68 with D6=0; S72 remains S=72 with D6=0.
2. A second independent true-original six-Q evaluator directly computes original source multiplicities, physical coordinate degrees and the connected AA positional C6. Transport each originally accepted S72 six-Q under the actual common source transvection and check tag-for-tag invariance, not merely aggregate equality.
3. TRUE W(3,4) uses the independently regenerated symplectic GQ, validates entire source incidence set and actual transvections, checks actual globally injected full maps and independently samples mapped original six-Q; this is **not** a complete C(425,6) enumeration.
4. Negative controls: non-bijective physical permutation, noninjective physical source map, duplicated original incidence ID, malformed six-Q, impossible physical edge, fake incidence geometry and unpaired point/line source swap. All fail closed.

The model already has S68=68 and S72=72 at true W(3,2) while the independently certified two-complete-global uniform expected S=165129984/1002001. Hence any proposed **pointwise** inequality S_2(f,g)>=theta E S_2 for theta>17034017/41282496 is already false on the genuine S68 fixture. This finite obstruction cannot be converted into an asymptotic theta impossibility for h->infinity.

## 6. What this does, and does NOT, settle

This is a nontrivial deterministic **search-space reduction**, acting on the *same* actual source-incidence Q sets and preserving full seven-mode positional correlation, so it avoids the Fréchet-only and mixed-Hessian-sign pitfalls of AA4-U/AA4-Y2. It also makes a future exact W32 SAT/PB solver smaller before adding JPKC/EICE and position-cycle inequalities.

It does **not** prove any positive inf_(f,g)S_s bound, nor a globally optimal W32 certificate, nor an infinite correlated counterfamily, nor a full equivalent model/spectral lower bound required to close root issue #230 Branch C. Research status: OPEN_WITH_FORMAL_BLOCKER.

**Next theoretical gate:** formulate a symmetry-respecting feasibility/infeasibility certificate for the **same Q** original source physical half-projection incidence tensor, retaining positional C6; prove all-h a positive joint charge transfer (Branch A) or exhibit rigorously globally injected infinite map families with o(s^6) (Branch B). The source nine-cell exact means from #504 are reference/calibration, not substitutes for minimax constraints.

**Acceptance / integration:** stay Draft and stacked, require exact-final-head dedicated CI, INDEX, Proof Audit, Full Research SUCCESS and independent mathematical review before any merge. The previous parent #504 Full Research run was CANCELLED with a research-full-suite failure; it must be fixed/rechecked, not misreported as green. Once independently accepted, canonical claims, source SHA, model quantifiers, formula records and evidence should go into authoritative RCP JSON before deterministic regeneration of all five permanent structured Markdown records. Do not hand-edit generated registry documentation.
