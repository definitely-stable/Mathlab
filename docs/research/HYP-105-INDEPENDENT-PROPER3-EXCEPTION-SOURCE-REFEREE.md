# HYP-105 / #230 — AA4-P3EXC: independent exact proper-three-path, endpoint and original six-ID accounting

**Scientific Draft**, stacked ONLY on frozen [#693](https://github.com/definitely-stable/Mathlab/pull/693) at immutable parent HEAD `542a18374400bcee096f5896f9288cc4e96a22ad`. No changes to any ancestor, `main`, original W(3,s) maps, source IDs, or root acceptance. Current science status `OPEN_WITH_FORMAL_BLOCKER`. This is a genuinely independent consistency audit of the three most delicate *combined* root transitions, not a new exponent, external proof of SS6 or qualified external mathematics peer review.

## 1. Why the next step is source-to-physical mass conservation, not new constants

The original universal Branch A #672/#681/#682/#686 combines three fundamentally different quantities ON THE SAME physical ORIGINAL core H0:

1. All actual directed length-three physical walks, bounded below by Blakley–Roy:
   \(W_3={\bf1}^TA_0^3{\bf1}\ge(2m_0)^3/n^2\), where the TRUE source complete grid has \(n=a^2\) physical cells and the original paired flag core has \(m_0=2N_0\).
2. Actual **coordinate-PROPER** three-walks P3 (the four visited LEFT physical symbols are pairwise distinct, separately all four RIGHT physical symbols). All improper walks are subtracted at most once in the TRUE count, though prior estimates permit union overcount.
3. Actual proper paths whose **ordered physical endpoints** decode either a missing physical factor label, an INCIDENT original point–line pair, or a nonincident original source projection with bad END factor overlaps. These exceptional endpoint cells are bounded by exactly the original FULL-source book populations, not by any probabilistic assumption that walks are uniformly distributed over physical endpoint cells.

One can independently test their interaction WITHOUT trusting the older respective P3, improper-intersection, exceptional-endpoint, or BBo forward code. This addresses the possibility that individually true inequalities are applied to different underlying populations or physical/source representatives.

## 2. NEW universal exact 64-mask Mobius certificate for proper physical 3-walks

For ANY finite simple undirected graph H with vertices on a typed two-coordinate grid and with EACH physical edge changing BOTH coordinate symbols, consider an actual directed length-three physical walk \(v_0v_1v_2v_3\). Adjacent coordinate equalities never occur. Consequently coordinate-properness is equivalent to forbidding exactly SIX primitive return events:

\[
\begin{array}{lll}
X_{02}:(v_0)_x=(v_2)_x,&
X_{13}:(v_1)_x=(v_3)_x,&
X_{03}:(v_0)_x=(v_3)_x,\\
Y_{02}:(v_0)_y=(v_2)_y,&
Y_{13}:(v_1)_y=(v_3)_y,&
Y_{03}:(v_0)_y=(v_3)_y.
\end{array}
\]

Assign to each actual walk its six-bit exact mask \(M\in\{0,\ldots,63\}\). For every subset mask S, define \(I(S)=\#\{v_0v_1v_2v_3: M\supseteq S\}\). Finite-lattice inclusion/exclusion yields the **all-graph, all-h EXACT identity**:

\[
\boxed{
\#P_3=\sum_{S\subseteq\{X_{02},X_{13},X_{03},Y_{02},Y_{13},Y_{03}\}}
(-1)^{|S|}I(S),\qquad
\#\mathrm{improper}=W_3-\#P_3.
}\tag{P3M}
\]

No independence of the six return events, source f/g coordinate assignments or walk distributions is used. In particular, a walk returning both physical coordinates at the same time is counted only ONCE after exact inclusion/exclusion.

The historical #681 upper bound \(\#\mathrm{improper}\le2\Delta B_2+\Delta(Q_x+Q_y)\le68T s^5\) for the dense original core is a conservative consequence, not claimed equality. The exact B2 identity is additionally checked physically:
\[
B_2=Q_x+Q_y-2m_0=4N_0+4(M_f(I)+M_g(I)).
\tag{B2}
\]
Here \(M_f(I),M_g(I)\) are independently recomputed books on TRUE original core flag IDs I, and the subtraction \(2m_0=4N_0\) removes physical backtracking overlap. Neither the six-mask proof nor the original book identity relies on any finite-h sample.

## 3. Independent endpoint-FIRST tensor, not a second walk DFS

The new reference computes the whole **ordered physical endpoint-indexed** proper-path matrix by a mathematically separate middle-edge contraction:
\[
\boxed{
P_3(v_0,v_3)=\sum_{v_1\in N(v_0)}\sum_{v_2\in N(v_3)}
\mathbf1_{v_1v_2\in E(H)}
\mathbf1_{x(v_0),x(v_1),x(v_2),x(v_3)\,\mathrm{all\ distinct}}
\mathbf1_{y(v_0),y(v_1),y(v_2),y(v_3)\,\mathrm{all\ distinct}}.
}\tag{P3T}
\]

This chooses the two ENDPOINTS FIRST and counts actual admissible middle-edge pairs, rather than walking forward \(v_0\to v_1\to v_2\to v_3\). The identity follows bijectively from reordering four actual physical vertices. Distinct physical source owner IDs are inherited from actual core physical edges, not inferred from an abstract path surrogate. The independent forward-walk enumerator additionally calculates the full six-mask histogram, total W3 and endpoint-indexed P3. Exact equality of entire P3 matrices is required, not only aggregate counts.

The exact all-graph three-walk identity
\[
W_3=\sum_{uv\in\overrightarrow E(H)}d(u)d(v)
\tag{W3D}
\]
is checked a THIRD way, independently from adjacency degree products. The standard all-finite-undirected-graph Blakley–Roy inequality \(W_3\ge(2m)^3/n^2\) is audited in exact rational arithmetic, including true isolated physical grid cells. Under the #672 true ORIGINAL dense core m0>=s^4 and n=a²<=4s³, this is at least s^6/2 as in root #686; the finite small-W controls are NOT claimed to satisfy asymptotic s>=s0 density premises.

## 4. Source-FIRST/physical-FIRST exact four-class END partition, including f/g correlation

Use true ORIGINAL complete symplectic W(3,s), with V=(s+1)(s²+1) point factors and V line factors, original N=(s+1)V actual incidence IDs and complete globally injected fixed typed pair labels f,g in minimal E(K_a). The true unique original nonincident point-line projection is q--ell--p--r, even when anchor flags are absent from the physical CORE. Put M=binom(a,2), and full ORIGINAL collinearity/pencil books M_f,M_g.

For any ordered physical endpoints \(v_0=(x,y),v_3=(z,w)\) with x≠z and y≠w, their coordinate pairs may be decoded by FULL original f,g. There are exactly \(4M^2\) such physical ordered endpoint cells and precisely FOUR disjoint classes:

\[
\boxed{
\begin{aligned}
E_{\mathrm{missing}}&=4(M^2-V^2),\\
E_{\mathrm{incident}}&=4N,\\
E_{\mathrm{bad}}&=4\big(2s(M_f+M_g)-J\big),\\
E_{\mathrm{good}}&=4\big(V^2-N-2s(M_f+M_g)+J\big),
\end{aligned}
}\tag{P3E}
\]

where J is the **ACTUAL**, not independently modeled, intersection of full source-left and source-right bad nonincident (q,r) projections. Their counts satisfy sum=4M². Two independent exact full-source original book identities
\[
\#\mathrm{bad}_{\mathrm{left}}=2sM_f,\qquad
\#\mathrm{bad}_{\mathrm{right}}=2sM_g
\]
are recomputed by directly looping all genuine original nonincident q,r and their unique source projection, and independently counting the full original source pencils. Their correct orientation multiplicity is exactly 4. No iid/uniform endpoint assumption is made.

Let \(P_3\) be the exact same ACTUAL physical CORE proper path matrix from (P3T). Then the true proper-path mass of the exceptional FULL-source endpoint cells is
\[
W_{\rm exc}=\sum_{(v_0,v_3)\in E_{\rm missing}\cup E_{\rm incident}\cup E_{\rm bad}}P_3(v_0,v_3).
\]
An **embedding-sensitive always-no-worse** exact Cauchy certificate is
\[
\boxed{W_{\rm exc}^2\le E_{\rm exc}
\sum_{(u,w)\in E_{\rm exc}}P_3(u,w)^2
\le E_{\rm exc}\|P_3\|_F^2.}\tag{P3CS}
\]
This is distinct from pretending every endpoint receives the same number of paths. It recovers the earlier conservative \(21s^5\) exceptional-endpoint bound and \(\sigma_3^{-2}L_6s^6\) path norm as valid inputs, without changing their exponents.

## 5. Critical exact TRUE ORIGINAL six-ID B/B-overlap image mass balance

The new independent source audit goes beyond checking the three scalar inequalities: it enumerates every ACTUAL proper physical CORE path with original nonincident END-GOOD projection q--ell--p--r. It then partitions this population by whether at least one of the FOUR internal coordinates belongs to its source anchor physical factor pair f(p) or g(ell). For every remaining path, it constructs all SIX actual original incidence IDs:

\[
Q(v_0v_1v_2v_3)=\{(q,\ell),(p,\ell),(p,r),
       \mathrm{owner}(v_0v_1),\mathrm{owner}(v_1v_2),
       \mathrm{owner}(v_2v_3)\}.
\]

Original global f/g injection, coordinate-properness and all four internal block exclusions ensure SIX DISTINCT genuine original source flag IDs, B/B-overlap source repeated-factor profile and both degree-two six-symbol physical factor projections, the accepted historical original motif. The previously proven #677 inverse yields exactly TWO directed physical path preimages onto the produced image, namely exact reversals. This new oracle builds and counts actual original flag-ID sixsets INDEPENDENTLY of #677's forward or inverse code, verifying **every** one has exactly two produced directed source paths in true W32/W34 cases.

The entire ACTUAL physical path mass has the exact finite decomposition

\[
\boxed{
W_3
= W_{\mathrm{improper}}
+ W_{\mathrm{proper,exc}}
+ W_{\mathrm{proper,good,intblock}}
+ 2\,|\mathrm{BBo\ original\ source\ sixsets\ produced}|.
}\tag{P3BAL}
\]

The identity follows from a disjoint partition and the independently proved two-preimage original BBo inverse, with NO assumption of surjectivity onto all accepted historical BBo motifs. At every tested finite original source instance all **FOUR** terms must agree, and per-sixset original owner multiplicity must be exactly two. In the general all-h proof, combine this exact source-image subcount with the existing published/traced inequalities:
\[
U_{BB,\rm overlap}\ge\frac12\Big[
\frac{s^6}{2}
-68Ts^5
-\sqrt{21}\,\sigma_3^{-1}\sqrt{L_6}\,s^{11/2}
-4\sqrt{B_0TL_4}\,s^{47/8}\Big].
\]
This merely RESTATES the already existing #682/#686 sufficient lower and its required independent proof inputs; it does **not** assert an improved universal exponent or newly accepted root theorem.

## 6. Independent falsifiers and scientific STOP

The standalone reference `research/hyp105_independent_proper3_exception_source_referee.py` uses ONLY the genuine original symplectic source `genuine_source` as shared incidence input. It neither imports earlier `#681 improper`, `#682 exceptional`, `#677 original BBo forward/inverse`, nor `#686 root` code. It:

* enumerates every actual paired physical source flag diagonal in the CORE, preserving original edge owner IDs;
* forward-scans all true physical 3-walks, records the SIX return-event masks (64 exact combinations) and true endpoint P3 cells;
* independently recomputes the P3 matrix from constrained endpoint-FIRST middle-edge contraction, full physical degree-product W3, all physical two-step coordinate-return books, and Möbius inclusion/exclusion;
* independently enumerates **all** `4M²` physical ordered endpoints, decodes source occupancies and unique original projection, computes ACTUAL classes and compares the original FULL-source book formula with the true f/g-correlated J, not with fabricated independence;
* on every proper good path, checks true original four internal positions and generates the SIX ORIGINAL source owner/anchor flags, their source multiplicity pattern, exact repeated-sixset count and the full path conservation identity;
* verifies genuine W32/W34 full/sparse cores, five distinct global correlated right maps on W32, real W34 source-control with 16 planted protected actual flags, and fail-closed invalid maps and duplicate core IDs.

The dedicated unittest checks ALL 64 legal opposite-diagonal physical subgraphs on a 2×3 typed grid, ALL 4096 legal opposite-diagonal subgraphs on a 2×4 grid, actual original W32 full/sparse source and W34 full/sparse sources, and precise negative controls. Exhaustive small graph checks are algorithmic falsifiers; the universally valid mask / tensor / path-conservation identities are proved abstractly above.

**Acceptance:** scientific Draft only. No numerical values for external balanced-C6 graph supersaturation C_graph,c_graph, no proof of BBo lower without the inherited heavy-tail/selector/mixed-blocker assumptions, no new R2/R3 upper, no unrestricted ASET exponent, no external qualified referee or original #230 closure. No parent/main changes or merges. The next strongest action is a genuinely independent adversarial REVIEW of the all-h selector positive-correlation lemma or an independent professional extremal-combinatorics referee of the complete source-indexed proof.
