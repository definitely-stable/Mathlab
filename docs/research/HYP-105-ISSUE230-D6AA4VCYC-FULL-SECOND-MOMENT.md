# HYP-105 / issue #230 — D6-AA4-V-CYC: exact full genuine W(3,2) quenched D6 second moment

**Research scope:** Finish the finite conditional second moment of TRUE ORIGINAL six-incidence accepted GF(5) D6 motifs for each frozen complete globally injected point mapping f on W(3,2), averaging ONE uniformly random COMPLETE globally injected original line mapping g. Source original W32 has 15 points, 15 lines, 45 distinct actual incidences; 21,186 distinct admissible original six-incidence Q per fixed f. All shared-source-line cyclic pair gluing r=0,...,6 is handled by the previously established all-h D6-AA4-U-CYC kernel. This slice adds the **complete genuine ORIGINAL ordered Q×Q pair count** (not just one anchored row), finite \(\mathbb E_g D_6^2\), variance, and exact Paley–Zygmund positivity probability bound. Does NOT prove all-h variance or every-\(f,g\) GF5 minimax \(S_s=\Omega(s^6)\).

Strictly stacked research Draft on [D6-AA4-U-CYC / PR #487](https://github.com/definitely-stable/Mathlab/pull/487), exact parent HEAD \`1502844a49cea1631206b2b68144c65f879fc4c0\`. Never modify main, merge, or close issue #230 automatically. Original source line cycles here are genuine LEFT physical coordinate-to-six-original-column duals, with LINE vertices equal to actual ORIGINAL source line factor IDs; not physical proper-P3 proxies.

## 1. Exact compression theorem for FULL conditional D6 count

Fix genuine original W(3,2), a=6, K=C(6,2)=15, arbitrary complete source-point edge-injective f. Define \(\mathcal Q_f\) to be all TRUE original six-DISTINCT-incidence sets Q with SIX distinct actual ORIGINAL point factors, SIX distinct actual ORIGINAL line factors, and physical-left six-column connected cycle C6 under the SAME globally injected f. The #480 independent true-source enumeration proves \(|\mathcal Q_f|=21\,186\) for S68/S72.

For each Q, its fixed left coordinate dual induces an UNDIRECTED cycle on the six distinct ORIGINAL LINE factor IDs appearing in Q. Write \(C_f(Q)\) for that undirected six-vertex line graph, up to its 12 dihedral oriented edge traversal descriptions. Every globally injected right/source-line map g accepts Q as the historical seven-GF5 **D6** class if and only if the physical right coordinate dual induced by the SIX actual source line physical pair labels \(g(\ell)\), \(\ell\in C_f(Q)\), has the SAME original-six-column adjacency graph. This depends on Q only through its original-LINE C6 graph, not its six other original point factor IDs or original position ordering after the cycle is reconstructed. Consequently define the exact nonnegative ORIGINAL sixset multiplicity

\[
w_f(C)=\#\{Q\in\mathcal Q_f:C_f(Q)=C\}.
\]

For ANY one complete right globally injected g (without per-Q resampling):

\[
\boxed{D_6(f,g)=\sum_C w_f(C)\,\mathbf1\{g\text{ realizes original-LINE cycle }C\}.}
\]

This is an exact finite **event-fibre compression**, not an approximation. It automatically retains all \(21\,186\) genuine original Q with exact integer weights, and the full ordered pair count follows by \((\sum_Cw_f(C))^2=21\,186^2=\mathbf{448\,846\,596}\). Source LINE graph cyclic normalization fixes smallest actual original line ID as first and takes the lexicographically minimum of the forward/reverse six-cycles; it does NOT relabel original source factor IDs or globally injective physical images.

## 2. Combine exact all-h source-LINE gluing kernel with ALL finite ORIGINAL Q pairs

AA4-U-CYC #487 proved the all-h joint D6 event kernel for two fixed ORIGINAL line C6 graphs C,C' with exactly r shared true original LINE source IDs and canonical cyclic gluing \(\tau\):

\[
p_{\tau}(a,K)=\frac{(a)_6}{(K)_{12-r}}\sum_{k=0}^{6}c_{\tau,k}(a-6)_k.
\]

For genuine W(3,2), a=6, all terms with k>0 vanish and the exact probability simplifies to

\[
p_{\tau}(6,15)=\frac{720\,c_{\tau,0}}{(15)_{12-r}}.
\]

For every r=0,...,6, the denominator \((15)_{12-r}\) divides \(\mathscr D:=(15)_{12}=\mathbf{217\,945\,728\,000}\). Define the **nonnegative integer** original conditional pair numerator

\[
A_{\tau}:=\mathscr D\, p_{\tau}(6,15)
=720\,c_{\tau,0}\frac{\mathscr D}{(15)_{12-r}}
\in\mathbb Z_{\ge0}.
\]

Every relative original line-C6 cyclic glue diagram is encoded by a six-position tuple with digits 0,...,5 for a shared ORIGINAL line's first-cycle position and digit6 for a new original line. There are EXACTLY

\[
\boxed{\sum_{r=0}^{6}\binom6r(6)_r=13\,327}
\]

valid partial source-LINE bijections, represented in a sparse integer lookup of size \(7^6=117\,649\). Their dihedral canonicalization gives **125 possible abstract cyclic gluing isomorphism types** in total. The previous true ORIGINAL W32 anchored row realized only **112** of those 125 abstract types; an arbitrary abstract physical/source glue type is not automatically realizable in a fixed true GQ source family.

Define

\[
N_f(C,C'):=w_f(C)w_f(C').
\]

Then, with ONE globally shared right g,

\[
\boxed{
\mathbb E_g[D_6(f,g)^2]
=\frac1{\mathscr D}\sum_{C,C'} N_f(C,C')A_{\tau(C,C')}.
}
\]

The diagonal C=C' is fully included (including all multiplicities of genuinely distinct Q sharing an identical right-D6 event). All original LINE-support-overlap sectors r0..r6 and all their positional gluing compatibility/incompatibility patterns are included. No source pair is omitted, independently relabeled or sampled.

The exact conditional mean established by #480 is \(\mu_f=21\,186/5\,005=1\,926/455\) for S68/S72. The **actual finite conditional variance** is

\[
\boxed{\operatorname{Var}_g(D_6(f,g))=
\mathbb E_g[D_6(f,g)^2]-\left(\frac{21\,186}{5\,005}\right)^2.}
\]

Both are exact rational numbers, and the nonnegative variance must be a strict fail-closed invariant. This is a FINITE exact W32 result for the pinned full f, not an all-h variance statement.

An exact Paley–Zygmund/Cauchy lower on the probability of strictly positive D6 is

\[
\boxed{\Pr_g[D_6(f,g)>0]\ \ge\ 
\frac{(\mathbb E_g D_6)^2}{\mathbb E_gD_6^2}.}
\]

This remains a probabilistic **some full globally injected g** lower. The actual pinned complete globally injected g for S68/S72 has D6=0, so this cannot imply \(\forall g\,D_6(f,g)>0\), nor \(\inf_{f,g}S_s(f,g)\ge c s^6\).

## 3. Exact verified host algorithm and independent oracles

For each true ORIGINAL S68/S72 frozen global point source f:

1. Independently enumerate all 60 occupied physical connected C6 edge graphs of complete K6; inverse-map to six distinct actual source point IDs and choose actual distinct ORIGINAL source line IDs via TRUE 45-incidence GQ flags. Enumerate exactly **21,186** DISTINCT source incidence-ID Q, fail closed on source degree/line/point distinctness.
2. Reconstruct each Q's genuine six-ORIGINAL-column coordinate dual as a six-vertex C6 on its ACTUAL six original SOURCE LINE factor IDs (AA4-U-CYC positional oracle). Group by identical UNDIRECTED source line C6 with exact positive multiplicity \(w_f(C)\); verify sum of multiplicities=21,186.
3. Generate all 13,327 injective partial source line gluing diagrams, derive each pair's **EXACT integer numerator** via the already certified AA4-U-CYC all-h canonical color coefficient oracle; test r0=1/8,408,400, r6 equal-cycle=1/5005, r6 incompatible-cycle=0. Distinguish 125 abstract types from the 112 realized in ONE real W32 anchored source row.
4. Use the transparent small C++20 host-native counting kernel on **GitHub-hosted ubuntu-latest runners only**. It scans all distinct weighted real source LINE C6 event pairs; for each pair it constructs the original SOURCE common-line positional diagram in six O(1) digit lookups, obtains the exact integer \(A_\tau\), and increments positive/zero counts and seven original line-source-overlap r0..r6 sector moments weighted by the product of actual Q multiplicities. Its internal 128-bit integer accumulators prevent overflow. Check totals exactly \(448\,846\,596\) REAL ordered Q pairs and reconciliation of sectors to the full unconditional second-moment numerator. It does NOT enumerate 448m Python pairs or claim a mathematical symmetry that original f does not have.
5. As a hard independent regression, compute from the COMPLETE source-line group full pair engine the conditional joint-probability sum along the specific earlier ACTUAL ORIGINAL anchor Q0=(0,5,7,10,13,39). It MUST exactly match AA4-U-CYC's independently enumerated actual 21,186-sixset anchored value \(\boxed{19457/10810800}\), despite aggregating all second Q by event cycle weights. The independently implemented earlier positional pair enumeration is not reused to compute the full moment.
6. Separately check at least FIVE concrete COMPLETE globally injected right g maps (pinned original S68 and S72 plus three independent deterministic pseudo-random full source line K6 permutations): directly test whether each ORIGINAL right line set's physically induced six-column dual equals the genuine source-line cycle for every group C, count weighted multiplicities and compare the resulting integer D6 **against the established historical ORIGINAL seven-class GF5 classifier \`seven_census\`** on the same complete f/g and all 62,370 actual left-side original-six-incidence candidate Q. No artificial per-Q edge assignment.
7. Validate that the exact full second moment is at least the positive mean, variance nonnegative, and the exact finite Paley–Zygmund lower is strictly between zero and one. A specific original f has a genuine complete right g with D6=0, so the stochastic lower is correctly scoped.

The full second moment output also includes exact ordered pair counts by number r=0..6 of common **original source LINE IDs**, counts by sector of pairs whose conditional D6 joint probability is strictly positive, and each sector's own exact second-moment integer numerator. These are full all-ordered-pairs source histograms, unlike the single anchored line-source overlap row of #485/#487.

## 4. Hard limitations and independent acceptance

**OPEN_WITH_FORMAL_BLOCKER**: A true finite W32 \(D_6\) variance is not the theorem \(\min_{f,g}S_s(f,g)=\Omega(s^6)\). The all-seven exact two-sided join of #476 still requires a deterministic original geometry/physical global assignment inequality guaranteeing either many true D6 aligned Q or many NON-AA original incidence-ID joined positive GF5 sixsets. Positive \(D_6\) conditional expectation and second-moment concentration/probability cannot exclude a carefully constructed bad complete g. Do not conflate the 15-line W32 source problem with arbitrary s or a physical proper P3 motif proxy.

Next **D6-AA4-W-CYC** may derive full-second-moment ALL-h upper bounds from genuine W(3,s) source-line support intersection combinatorics or look for a deterministic right-map D6/non-AA compensator. Use the newly computed exact seven-sector full pair counts as a finite regression for any large-s combinatorial inequalities; independent peer mathematical review remains required.

Five additive files: small C++20 exact integer engine, Python source-original full-event aggregation/oracle, independent tests, this mathematical document, GitHub-hosted three-job workflow. Final exact SHA dedicated/INDEX/Proof Audit/full Research must complete SUCCESS before technical acceptance. main untouched, PR draft; no merges or issue closure.
