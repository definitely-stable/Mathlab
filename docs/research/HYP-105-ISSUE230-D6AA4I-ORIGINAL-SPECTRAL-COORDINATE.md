# HYP-105 / issue #230 — D6-AA4-I: ORIGINAL GQ spectral physical-coordinate coupling

**Classification: all-h unconditional mixed source/physical \(\Omega(s^5)\) theorem + two-type source-incidence physical-coordinate capacity; ROOT Branch A/B STILL OPEN.** These are applications of classical strongly-regular-graph eigenvalues / expander mixing; standalone novelty of spectral technique is not claimed. No implication that true ORIGINAL seven-class GF5 \(S_s\) is positive or \(\Omega(s^6)\). No full \(R_3\), ASET exponent, infinite counterexample, or conventional Sherali-Adams/SOS feasibility claim.

Research Draft, strictly stacked on [D6-AA4-H / PR #448](https://github.com/definitely-stable/Mathlab/pull/448), pinned parent SHA `006839457641e7fbb52dbad43ff01e991cab1ce2` (4/4 hosted exact-SHA workflows SUCCESS). Do not touch main or merge. Independently review proof before acceptance.

## 1. Why this is an actually SOURCE/PHYSICAL MIXED invariant

Previous AA4-H established exact original six-right-line-profile four-witness covers on two pinned 24-state W32 fibers, but its scalar occupied-physical-image adjacency cut D6-Y has ZERO slack for EVERY true complete W32 injection because physical K6 is fully occupied. The next useful all-h gate is **not** a repeated scalar image-edge inequality. It must carry genuine W(3,s) source relationships.

At the same time parallel JPKC-014 [PR #447](https://github.com/definitely-stable/Mathlab/pull/447) studies ORIGINAL singleton-line source stars and matching cover (conditional 7 to 8 positives); the EICE-003-C [PR #453](https://github.com/definitely-stable/Mathlab/pull/453) studies original middle-path Gram operators. This slice analyzes a different, directly verifiable source/physical **collinearity adjacency quadratic cut** on ALL ORIGINAL point and ALL ORIGINAL line factors, and an independent **incidence bipartite** source/physical spectral bound. It does not import unmerged code from the parallel branches. The original source geometry, NOT the physical K_a graph, defines collinearity.

## 2. All-h unconditional source-to-physical collinearity spectral theorem

For arbitrary \(s=2^h\), \(h\ge 1\), in the genuine symplectic GQ \(W(3,s)\), let \(V=(s+1)(s^2+1)\), source point-collinearity graph \(G_P\) and line-concurrency graph \(G_L\), with source collinearity adjacency matrix \(A\). They are the classical strongly regular graphs with:

- regular degree \(k=s(s+1)\);
- adjacent common-neighbor count \(\lambda=s-1\);
- nonadjacent common-neighbor count \(\mu=s+1\);
- adjacency eigenvalues \(k, r=s-1, t=-(s+1)\).

For ANY source vertex subset \(U\) of size \(n\) (point type OR line type) the standard spectral quadratic upper is

\[
e_G(U)=\frac{\mathbf1_U^TA\mathbf1_U}{2}
\le\frac12\left((s-1)n+\frac{s^2+1}{V}n^2\right).
\]

**Exact proof:** write \(\mathbf1_U=(n/V)\mathbf1+z\), \(z\perp\mathbf1\), \(\|z\|^2=n-n^2/V\). The eigenvalue of \(A\) on the all-ones direction is \(k\); the maximum on the orthogonal complement is \(r=s-1\). Hence \(\mathbf1_U^TA\mathbf1_U\le k n^2/V+r(n-n^2/V)\). Since \(k-r=s^2+1\), the bound follows. Per-coordinate integer-valued \(e_G(U)\) is at most the exact rational floor of this expression.

Now let \(f\) be ANY globally injective ORIGINAL point map to physical K_a edges, \(a\) the smallest integer with \(K=\binom a2\ge V\), and define exact ORIGINAL source/physical coordinate sets

\[
P_c=\{p\in W(3,s):c\in f(p)\},\quad n_c=|P_c|.
\]

Since physical pairs are UNIQUE for that source type, \(n_c\le a-1\) and \(\sum_c n_c=2V\). Let \(\Phi_P(f)\) be the number of **distinct ORIGINAL collinear source point pairs** whose assigned physical edges share a coordinate. Two different physical edges share at most one coordinate, so there is an EXACT identity

\[
\Phi_P(f)=\sum_{c=0}^{a-1}e_{G_P}(P_c).
\]

Therefore

\[
\Phi_P(f)\le
\sum_c\left\lfloor\frac{(s-1)n_c+(s^2+1)n_c^2/V}{2}\right\rfloor
\le (s-1)V+(s^2+1)(a-1).
\]

The dual statement holds for ANY true complete original LINE map \(g\), with the source line concurrence graph, independently of f.

Let \(D_P(f)\) and \(D_L(g)\) be counts of ORIGINAL collinear or line-concurrent pairs whose assigned distinct physical pair labels are **DISJOINT**. Each original source type contains EXACTLY \(Vk/2\) such pairs in its original collinearity/concurrence graph. Thus for BOTH types separately, with NO frozen outside labels or finite map search,

\[
\boxed{
D_{P,L}\ge \frac{V(s^2-s+2)}2-(s^2+1)(a-1).}
\]

For s>=4, the minimal physical alphabet obeys \(a-1\le s^2\), since \(\binom{s^2+1}{2}\ge(s+1)(s^2+1)\) holds whenever \(s^2\ge2s+2\). Consequently

\[
D_{P,L}\ge\frac{(s^2+1)(s^3-2s^2+s+2)}2
\ge\frac{s^5}4\qquad(s=2^h,\ h\ge2).
\]

The last inequality follows from \(s^3-4s^2+2s+4\ge0\) for all \(s\ge4\). This is a genuine ALL-h source/physical assignment-independent \(\Omega(s^5)\) fact, NOT the Root HYP-105 GF5 seven-sixset lower \(\Omega(s^6)\). It counts SOURCE PAIRS rather than original six-incidence Q, and there is no known sound bounded-multiplicity charge from these disjoint pairs to positive seven-class GF5 Q under arbitrary f,g.

**Explicit small parameters:** at real W32, \(V=15,a=6,K=15,k=6\). Total original collinear pairs 45; the uniform upper on physically adjacent original-collinear pairs is 40, forcing at least **5** disjoint. Since EVERY physical coordinate has exactly five typed source labels, the per-coordinate FLOOR yields at most 6 source-collinear pairs on each of six physical centers, hence \(\Phi_{P,L}\le36\), forcing at least **9** original collinear/line-concurrent pairs to be physically disjoint on EVERY W32 labeling. At real W34, \(V=85,a=14,K=91,m=6,k=20\), total collinear 850; the uniform spectral upper is 476, forcing at least **374** original source-collinear pairs physically DISJOINT per type.

## 3. All-h SOURCE-incidence/physical-coordinate bipartite cut

Let B be the TRUE original V-by-V point–line incidence matrix, with exactly \(V(s+1)\) ORIGINAL incidences. True W(3,s) incidence gives

\[
BB^T=(s+1)I+A_P,
\]

so the largest singular value of B is \(s+1\) and all nontrivial singular values are at most \(\sqrt{2s}\). For physical coordinate c define \(P_c=\{p:c\in f(p)\}\), \(L_c=\{l:c\in g(l)\}\), \(p_c=|P_c|\), \(l_c=|L_c|\), and \(I_c=\#\{(p,l)\in\mathcal I:p\in P_c,l\in L_c\}\). Cauchy–Schwarz on the source incidence matrix plus the exact rational weighted AM-GM bound yields for EVERY positive rational eta,

\[
I_c\le \left\lfloor
\frac{(s+1)p_cl_c}{V}
+\frac12\left[
\eta\left(p_c-\frac{p_c^2}V\right)
+\frac{2s}{\eta}\left(l_c-\frac{l_c^2}V\right)
\right]\right\rfloor.
\]

This is a **two-typed source-physical** cut: it cannot be derived just from the two independent physical image edge sets, because it includes ORIGINAL incidence identity. The executable oracle evaluates the minimum over several rational eta values, all of which are valid upper bounds, and compares directly to the number of actual ORIGINAL incidences whose left and right physical labels share a given physical coordinate. For W32 each type has five ORIGINAL source factors per physical coordinate; with eta=2 this yields \(I_c\le11\). Over all six physical coordinates the sum is at most 66, but source incidences can count 0, 1 or 2 times depending on cross-type physical pair overlaps. There is NO direct positive-seven-GF5 lower inference from this incidence count.

## 4. Exact-genuine finite falsification and GF5 calibration

- Independently reconstruct/validate the entire point and line ORIGINAL GQ adjacency from the actual 45 W32 / 425 W34 original incidences. Fail closed unless every source point/line degree is s(s+1), each original adjacent pair shares exactly s-1 source common neighbors, and each original nonadjacent pair shares exactly s+1.
- For REAL W32 lex/reverse/S68/S72 and W34 lex/random check physical-coordinate degrees, ORIGINAL source collinear physically adjacent and disjoint pair counts, the per-coordinate integral spectral floors, and true-original two-type incidence physical-coordinate spectral upper.
- Verify 48 independent randomly generated complete W32 globally injective point/line K6 maps with true original GQ geometry, and input mutation/invalid typed map and budget controls.
- For S68 and S72, recover first genuine all-four-POINT ORIGINAL critical source transversal (53/119 original critical four-factor supports respectively), enumerate exactly all **24 globally injective complete** point-block label assignments with all other ORIGINAL factor labels frozen, and rerun historical ORIGINAL seven_census of all 62,370 genuine original six-incidence candidate sets in EACH map. In the same complete map, independently record the original source-to-physical spectral pair counts AND the real seven-GF5 positive Q count and certified 51-column numerator. Verify no invalid assignment or mismatch across real historical original census.
- Comparing the spectral observables to S68/S72 seven-GF5 counts is diagnostic, NOT a proven monotone or bounded-charge transfer. No W34 complete GF5 seven-census, no arbitrary-start-map or all-h motif lower certificate.

## 5. Prior art, significance, next gate

Spectral strongly regular GQ graphs and expander mixing are classical; the novel-to-this-work application of original-GQ relations to the physical K_a injection alphabet is a transparent corollary rather than a claimed newly discovered general graph theorem. Related parallel EICE original incidence Gram/transport, D6-X/Y physical image capacity and JPKC-014 source star original-label allocation must be distinguished. The two-type spectral cut is a necessary admissibility constraint, not by itself a method proving original GF5 positivity.

**Acceptance:** exact-final-head dedicated source spectral tests + two W32 original GF5 24-state jobs, INDEX, Proof Audit, full Research GitHub-hosted CI and independent mathematical proof review. No main writes or merge.

**Next D6-AA4-J:** test whether source-collinear physical-DISJOINT pairs (guaranteed \(\Omega(s^5)\)) can be charged to ORIGINAL six-incidence GF5-positive Q under BOTH mappings with controlled multiplicity and true six-position positional signature. First search a rigorous GQ geometry/physical label transfer lemma, then falsify on W32 S68/S72, W34 targeted patterns, JPKC-011 P3-invisible Q and EICE-003 covariance pseudo models. A transfer from pair obstructions to positive ORIGINAL sixsets is still the open scientific gate; do not infer \(\Omega(s^6)\) or ASET exponent.
