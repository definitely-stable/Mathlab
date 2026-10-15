# HYP-105 / issue #230 — D6-AA4-T-CYC: exact conditional *fixed-f* two-D6 kernel and ORIGINAL right-line overlap frontier

**Research status:** rigorous all-h exact two-event probability under ONE globally injected random right/source-line map g with an adversarially FIXED complete left/source-point map f; the two TRUE ORIGINAL six-incidence D6-compatible source sets Q0,Q1 may SHARE original points, but must have DISJOINT original line factors. Genuine W32 finite ORIGINAL point-overlap/right-line-disjoint matching, a single complete globally injected right map making BOTH D6-positive, exact physical six-cycle-complement inclusion-exclusion and independent combinatorial brute. **NO** complete second moment, variance bound, concentration, or universal every-\(f,g\) \(S_s=\Omega(s^6)\) theorem.

Research-only new Draft based strictly on 4/4-CI-green [AA4-R-CYC / PR #480](https://github.com/definitely-stable/Mathlab/pull/480), exact parent \`53af9d2f03ef4fec147b633558a0e7bb96aea070\`. Separate parallel [AA4-S / PR #479](https://github.com/definitely-stable/Mathlab/pull/479) handles root-conditioned original B/A Fréchet marginal NO-GO, not this fixed-\(f\) right-source-line covariance. Earlier [JPKC-016 / PR #458](https://github.com/definitely-stable/Mathlab/pull/458) derives a TWO-SIDED random \(f,g\) exact kernel when both original POINT and LINE source supports between Q0,Q1 are disjoint. Its \(H_a\) physical C6 complement is prior art; **do not claim new invention of H_a nor independent new discovery of its 64-term inclusion-exclusion**. The contribution here is the exact ONE-SIDED **quenched conditional** GF5 kernel for any frozen \(f\), requiring only DISJOINT ORIGINAL LINE supports, ALLOWING real ORIGINAL POINT overlap. This is the missing covariance sector needed to examine AA4-R-CYC's \(\forall f\,E_g D6\) theorem.

## 1. The precise all-h ORIGINAL conditional two-event statement

Let \(W(3,s)\), \(s=2^h\ge2\), be a true symplectic generalized quadrangle with V=(s+1)(s²+1) original point/line source factors. Let \(a\) be minimal with \(K=\binom a2\ge V\). Fix **any complete globally injective** point-side physical edge labeling \(f\). Choose ONE uniformly random complete globally injective **line** labeling \(g\), shared across ALL true original six-incidence sets; never independently relabel Q. Choose two fixed (different) sets \(Q_0,Q_1\) of six DIFFERENT actual original point-line incidences each, each having six DISTINCT actual original points and six DISTINCT actual original lines, and each having a physical-left connected single-sixcycle column-dual under the SAME fixed f. Require the ORIGINAL LINE factor sets across Q0 and Q1 to be disjoint. Do **not** require the original point-factor sets to be disjoint or their original incidence sets to be globally disjoint beyond distinct line factors.

The earlier AA4-R-CYC exact marginal is

\[
p_s:=\Pr_g[Q_0 \text{ is TRUE ORIGINAL historical seven-GF5 D6}]
=\frac{(a)_6}{(K)_6},
\]
and the same is true for Q1. This counts physical right coordinate-symbol injections onto the six named edges of each connected left original six-column dual; all six true source line labels remain globally distinct.

Let \(F\subset E(K_a)\) be the six physical right source edge images of Q0 **conditioned on accepted D6**. They form a simple physical C6 graph. Let \(H_a\) denote the number of undirected simple physical six-cycles in the **edge-complement** \(K_a\setminus F\). Coordinate permutation transitivity shows \(H_a\) is independent of which first right six-cycle was chosen.

After conditioning on Q0, since the six true source-line factors of Q1 are distinct AND source-factor-DISJOINT from Q0, their SIX right physical edge images are uniformly sampled **without replacement** from the K−6 physical labels not already occupied by Q0. There are \((K-6)_6\) ordered such tuples. The number satisfying Q1's independent fixed-left *connected column-dual equality* is \(12H_a\): for each physical C6 edge set avoiding F, exactly twelve oriented cyclic isomorphisms map Q1's six named original column dual edges to the six physical coordinate edges. This holds even when Q0 and Q1 share original point factors: the left \(f\) is fixed and the two right six-source-factor maps are disjoint by assumption.

Thus the exact **one-sided fixed-\(f\)** pair kernel is

\[
\boxed{
\Pr_g(D_6(Q_0)\wedge D_6(Q_1)\mid f)
=
\frac{(a)_6}{(K)_6}\,
\frac{12H_a}{(K-6)_6}.
}
\]

The exact pair covariance is \(\operatorname{Cov}_g(1_{D6(Q0)},1_{D6(Q1)}\mid f)=p_s(q_s-p_s)\), with \(q_s:=12H_a/(K-6)_6\). In particular, disjoint original source LINE factors do **NOT** make two positive D6 events independent: the single globally injective g draws without replacement. The ratio of the true joint probability to the product of marginal probabilities is \(q_s/p_s\), which may be above or below one depending on the physical alphabet. This is an exact **conditional** probability, not the full all-seven GF5 class covariance.

## 2. A precise independent physical H_a computation (prior-art-aware)

Fix the six physical forbidden edges \(F=\{\{i,i+1\pmod6\}:i=0,\dots,5\}\). The complete K_a has \((a)_6/12\) undirected physical C6s. For each of the 64 subsets T⊆F of k required edges:
- For k=0, \(\# C6\supseteq T=(a)_6/12\).
- For k=6, \(\# C6\supseteq T=1\).
- For 1≤k≤5, T is a union of c disjoint nonempty paths using \(v=k+c\) fixed physical vertices. Contract each path. To obtain a simple six-cycle, choose 6−v new distinct physical vertices among a−v, order the 6−k cyclic units, then orient all c paths. The exact count is

\[
\#\{C_6\supseteq T\}=2^{c-1}(5-k)!\binom{a-k-c}{6-k-c}.
\]

The formula also correctly handles the k=5 single-path closure and k=4 two-unit closure. Inclusion-exclusion gives the exact integer
\[
\boxed{H_a=\sum_{T\subseteq F}(-1)^{|T|}\#\{C_6\supseteq T\}.}
\]
An **independent enumeration** of physical C6s in K6, K7, K8, K9 (not using the IE formula) checks \((H_6,H_7,H_8,H_9)=(3,45,327,1509)\), agreeing with established independent JPKC-016 data. No physical C6 or original source Q is assumed to be independent of another through a different global g.

On real W32, \(a=6,K=15\), \(p=720/(15)_6=1/5005\), \(H_6=3\), \(q=12\cdot3/(9)_6=1/1680\), and

\[
\boxed{
\Pr_g(D_6(Q_0)\wedge D_6(Q_1)\mid f)
=\frac1{5005\cdot1680}=\frac1{8\,408\,400}.
}
\]

This is about three times the independent-product p², confirming material conditional positive correlation at the saturated physical K6 alphabet. Do not assume the sign continues universally for all larger a.

## 3. Genuine ORIGINAL W32 source-line disjointness with overlapping original points

For separately pinned true original W(3,2) S68 and S72 fixed complete left point maps f, enumerate ALL 60 occupied six-coordinate connected physical C6 graphs on K6, recover their six original source point factors using the inverse of the same f, and select six TRUE ORIGINAL point-line incidences with six different original line factors. This yields exactly **21,186** true-original candidate Q per fixed f (independently checked against AA4-R-CYC and its historical selected-left oracle).

Choose a deterministic one ORIGINAL six-ID candidate Q0 as an anchor; compute the histogram of the other 21,186 candidate Q1 by the intersection size of their **original line factor** sets with Q0. Record the exact size of the r=0 row, but DO NOT label it as the full 21,186×21,186 pair histogram or as an exact conditional variance. In the r=0 source-line-disjoint row, independently find a second Q1 with a NONEMPTY **original point factor overlap** with Q0. This shows the newly proved conditional kernel applies beyond JPKC-016's fully source-P-and-L-disjoint case on a genuine original GQ.

Construct a **single REAL complete right global physical K6 injection g** realizing BOTH original Q0 and Q1 as actual full seven-GF5 D6:
1. Injectively align the right coordinate-to-original-column dual of Q0 onto a physical six-cycle F.
2. Enumerate right coordinate permutations for Q1, retaining assignments whose entire six-image physical C6 has NO physical edge in F.
3. Since H6=3, exactly 12×3=36 of its 720 right six-factor aligned tuples avoid F. Choose ONE and assign all twelve ORIGINAL source line factor images simultaneously.
4. Assign the remaining three physical edges to the other three true original source line factors to complete ONE globally consistent fifteen-line map g.
5. Directly verify using the **historical ORIGINAL six-incidence seven-GF5 classifier** that both Q0 and Q1 are D6 simultaneously, with all source factors/injection constraints intact.

This is an independently checkable **positive** two-Q original realization, not a global lower bound or universal D6 count. No fake local physical input is promoted to a true original W32 witness.

## 4. Partial second moment ONLY, and what remains

Write \(\mathcal Q_f\) for the finite true original six-incidence Q with connected physical-left column dual C6 and six DISTINCT original LINE factor IDs for the fixed f. Then
\(D6(f,g)=\sum_{Q\in\mathcal Q_f}1_{\{Q\text{ accepted D6 under g}\}}\).
Its full conditional second moment is

\[
\mathbb E_g[D6(f,g)^2]
=
|\mathcal Q_f|p
+\sum_{\substack{Q\ne Q'\\L(Q)\cap L(Q')=\varnothing}}p q
+\sum_{\substack{Q\ne Q'\\L(Q)\cap L(Q')\ne\varnothing}}
\Pr_g(D6(Q)\wedge D6(Q')\mid f).
\]

The first (diagonal) and second (genuine original-line source-disjoint) probability kernels are now exact. But the third, mixed source-line overlap, is **not evaluated** here; moreover the full source-line-disjoint pair count is not inferred from a single anchored row. Therefore **NO full conditional second-moment numerical value, variance, high-probability bound, Paley-Zygmund bound, or tail-to-minimax theorem is asserted**. At most, the exact nonnegative first two sectors supply a formally lower-bounding *partial* second moment, not a variance upper bound. A positive random mean with finite correlations still does not rule out a complete globally injected g where D6=0: true original S68 and S72 demonstrate it.

The precise next AA4-U-CYC is to classify genuine original Q,Q' by **how their shared ORIGINAL line factors occupy the six cyclic positions**, and compute exact shared-edge equality/coordinate-gluing kernels for each overlap configuration under a single full g. A mere integer overlap size r is insufficient for complete mixed physical compatibility in general. Only then can an actual full \(\mathrm{Var}_g(D6(f,g)\mid f)\) be evaluated or bounded for a fixed arbitrary f. Any claimed all-\(f,g\) lower will still require an independent adversarial mechanism linking aligned D6 deficits to large NON-AA original incidence-ID joint mass.

**Scientific classification:** new fixed-\(f\) conditional one-sided two-Q kernel with ORIGINAL right-line-disjoint but point-overlapping sources; the physical complement enumeration is prior art from JPKC-016 and is cross-validated, not newly claimed discovery. Dedicated + INDEX + Proof Audit + full Research CI on exact final SHA, independent mathematics review separately. Four research-only files, no main modifications/merge/issue closure.
