# HYP-105 — Formula Catalog

> Generated from pinned research registries; do not edit by hand.
> DOCUMENTED_IN_DRAFT is not independently reviewed/proven mathematics.
> HYP-105 issue [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains unresolved by these registered results.
> GitHub PR HEAD and CI are live data; none are hardcoded here.

Formula excerpts retain their original scoped quantifiers. Do not remove an expectation operator or silently generalize.

## HYP105-F-001 — Genuine source geometry and minimal physical alphabet

\[
s=2^h,\quad V_s=(s+1)(s^2+1),\quad a_s=\min\{a:\binom{a}{2}\ge V_s\},\quad N_s=\binom{a_s}{2}.
\]

**Applies under:** Common original W(3,s) typed global-injection model; h>=1. This defines the minimal alphabet, not an inequality about S_s.

**Cannot conclude:** A count of source vertices or physical labels alone is not a GF(5) obstruction.

**Linked claim:** HYP105-JPKC015-D6-ENSEMBLE

**Pinned source:** [PR #455 @ c02188a4d4f2](https://github.com/definitely-stable/Mathlab/blob/c02188a4d4f2e4e07440c4d7b25fc25c6dd31b3e/docs/research/HYP-105-ISSUE230-JPKC-015-ENSEMBLE-D6.md)

## HYP105-F-002 — D6 ensemble probability and expectation

\[
p_{D_6}(a)=60\left(\frac{(a)_6}{(N)_6}\right)^2,\qquad \mathbb E_{f,g}[D_6]=M_6(s)\,p_{D_6}(a)\sim\frac{16}{3}s^6.
\]

**Applies under:** h>=1, expectation over two independent UNIFORM COMPLETE globally injected original typed maps; M_6 is the original source six-edge matching count.

**Cannot conclude:** Positive average does NOT imply \inf_{f,g}D_6>0 or \inf_{f,g}S_s=\Omega(s^6).

**Linked claim:** HYP105-JPKC015-D6-ENSEMBLE

**Pinned source:** [PR #455 @ c02188a4d4f2](https://github.com/definitely-stable/Mathlab/blob/c02188a4d4f2e4e07440c4d7b25fc25c6dd31b3e/docs/research/HYP-105-ISSUE230-JPKC-015-ENSEMBLE-D6.md)

## HYP105-F-003 — Original GQ anchor dirty-pencil identities

\[
D_{\mathrm{left}}=s\sum_q t_f(q),\quad D_{\mathrm{right}}=s\sum_r t_g(r),\quad \Pr_{(q,r)\,\mathrm{unif}}[\mathrm{dirty}]\le\min\left\{1,\frac{4(a-2)}{s(s+1)}\right\}.
\]

**Applies under:** Every fixed legal globally injected f,g; probability ONLY over uniformly sampled ORIGINAL nonincident GQ point-line pairs.

**Cannot conclude:** Does not control four correlated original anchors conditional on a physical I1 template.

**Linked claim:** HYP105-EICE003K-DIRTY-ANCHOR

**Pinned source:** [PR #469 @ 73cfebed8042](https://github.com/definitely-stable/Mathlab/blob/73cfebed8042f0f9b6592bd318295fb0bdf69a5b/docs/research/HYP-105-ISSUE230-EICE003K-CLEAN-ANCHOR-CONCENTRATION.md)

## HYP105-F-004 — Quenched right-map exact B/A conditional identity

\[
\forall g:\quad \mathbb E_f\!\left[I_L^{BA,\mathrm{int}}(f,g)\mid g\right]=p_B(s)\,T_g,\quad p_B(s)=\frac{K\binom{a-2}{4}\,3\,4!}{(K)_5},\quad K=\binom{a}{2}.
\]

**Applies under:** h>=1; for each FIXED complete global right injection g, average over ONE independently drawn uniform complete global left injection f.

**Cannot conclude:** No individual-f or all-f,g guarantee follows from the identity.

**Linked claim:** HYP105-AA4N-QUENCHED-IDENTITY

**Pinned source:** [PR #470 @ 2af74df348a9](https://github.com/definitely-stable/Mathlab/blob/2af74df348a9c0921497757356199a609252f2c2/docs/research/HYP-105-ISSUE230-D6AA4N-QUENCHED-RIGHT-TRANSFER.md)

## HYP105-F-005 — All-right-map conditional expected B/A lower bound

\[
s=2^h\ge8:\quad \forall g,\quad \mathbb E_f[I_L^{BA,\mathrm{int}}(f,g)\mid g]\ge\frac{3s^6}{65536}.
\]

**Applies under:** h>=3; every fixed g, uniform random globally injected f. Implies min_g max_f lower; does NOT imply min_(f,g) lower.

**Cannot conclude:** Does not establish Root Branch A or bound the simultaneous adversarial minimax.

**Linked claim:** HYP105-AA4N-QUENCHED-LOWER

**Pinned source:** [PR #470 @ 2af74df348a9](https://github.com/definitely-stable/Mathlab/blob/2af74df348a9c0921497757356199a609252f2c2/docs/research/HYP-105-ISSUE230-D6AA4N-QUENCHED-RIGHT-TRANSFER.md)

## HYP105-F-006 — Deterministic all-h five-original-point quintic charge

\[
I_L^{BA,\mathrm{int}}(f,g)=\sum_{p,A:\,|A|=4}w_g(p,A)\,\chi_B\bigl(f(p);f(A)\bigr),\qquad w_g(p,A)\in\mathbb Z_{\ge0}.
\]

**Applies under:** h>=1; EVERY fixed coherent legal f,g, original six-incidence supports; quintic in constrained one-hot assignments.

**Cannot conclude:** Nonnegative coefficients do not imply the polynomial has a uniformly positive minimum.

**Linked claim:** HYP105-AA4O-QUINTIC-IDENTITY

**Pinned source:** [PR #471 @ b086566d8be1](https://github.com/definitely-stable/Mathlab/blob/b086566d8be17307b102e7bd89d28d4167af86a6/docs/research/HYP-105-ISSUE230-D6AA4O-QUINTIC-ADVERSARIAL-SWAP.md)

## HYP105-F-007 — Exact global-injection-preserving two-label swap

\[
\Delta_{u,v}I=\sum_{(p,A):\,\{u,v\}\cap(\{p\}\cup A)\ne\varnothing}w_g(p,A)\,\left[\chi_B\bigl(f^{u\leftrightarrow v}(p);f^{u\leftrightarrow v}(A)\bigr)-\chi_B\bigl(f(p);f(A)\bigr)\right].
\]

**Applies under:** h>=1; global swap of assigned physical pair labels on two distinct original points u,v with same fixed g.

**Cannot conclude:** One-transposition local optimality is not a global minimax or counterfamily certificate.

**Linked claim:** HYP105-AA4O-SWAP-IDENTITY

**Pinned source:** [PR #471 @ b086566d8be1](https://github.com/definitely-stable/Mathlab/blob/b086566d8be17307b102e7bd89d28d4167af86a6/docs/research/HYP-105-ISSUE230-D6AA4O-QUINTIC-ADVERSARIAL-SWAP.md)

## HYP105-F-008 — Exact all-h seven-positive-class same-original-ID two-sided join

\[
S_s(f,g)=\bigl|\mathcal{H}_P(f)\cap\mathcal{H}_L(g)\bigr|-\bigl|\mathcal{A}_{AA}(f,g)\bigr|+\bigl|\mathcal{D}_6(f,g)\bigr|.
\]

**Applies under:** h>=1; every genuine original W(3,2^h) and every pair of separately globally injective complete f,g; intersections are sets of SAME six genuine original incidence IDs; D6 requires physical original-column cycle alignment.

**Cannot conclude:** Exact join identity is not an all-maps lower bound on simultaneous seven-GF5 positive original motifs.

**Linked claim:** HYP105-AA4Q-SEVEN-ORIGINAL-JOIN

**Pinned source:** [PR #476 @ a51ce5aeb788](https://github.com/definitely-stable/Mathlab/blob/a51ce5aeb7883dcd029b9275ce44eaca9a60370f/docs/research/HYP-105-ISSUE230-D6AA4Q-TWO-SIDED-SEVEN-JOIN.md)

## HYP105-F-009 — GQ original-incidence source C/C impossibility

\[
\mathcal{J}_{CC}(f,g)=\varnothing\qquad(\text{genuine ORIGINAL GQ girth }8>6).
\]

**Applies under:** h>=1; six DISTINCT genuine original incidence IDs, both typed ORIGINAL source multiplicity profiles C=(2,2,2), arbitrary complete physical global injections.

**Cannot conclude:** Forbids genuine original source C/C only; not a generic physical coordinate C/C intersection or a deterministic positive seven-GF5 minimum.

**Linked claim:** HYP105-AA4Q-CC-GIRTH-OBSTRUCTION

**Pinned source:** [PR #476 @ a51ce5aeb788](https://github.com/definitely-stable/Mathlab/blob/a51ce5aeb7883dcd029b9275ce44eaca9a60370f/docs/research/HYP-105-ISSUE230-D6AA4Q-TWO-SIDED-SEVEN-JOIN.md)

## HYP105-F-010 — Exact fixed-point-map original D6 conditional alignment probability and count

\[
K=\binom a2,\quad V=(s+1)(s^2+1),\quad p_{D_6}(a,K)=\frac{(a)_6}{(K)_6},\qquad \mathbb E_{g}[D_6(f,g)\mid f]=p_{D_6}(a,K)\,N_{\mathrm{left\,C6,AA}}(f).
\]

**Applies under:** s=2^h>=8; every fixed complete global original point injection f, one uniformly sampled complete globally injected original line map g, shared across all genuine six-distinct-incidence sets.

**Cannot conclude:** A positive expectation does not imply D6(f,g)>0 under an adversarially fixed right g.

**Linked claim:** HYP105-AA4RCYC-D6-QUENCHED-IDENTITY

**Pinned source:** [PR #480 @ 53af9d2f03ef](https://github.com/definitely-stable/Mathlab/blob/53af9d2f03ef4fec147b633558a0e7bb96aea070/docs/research/HYP-105-ISSUE230-D6AA4R-QUENCHED-ORIGINAL-D6.md)

## HYP105-F-011 — Deterministic occupied coordinate C6 and true original distinct-source-flag bound

\[
m=K-V,\quad 0\le m\le a-2,\quad C_s=\frac{(a)_6}{12}-m(a-2)_4,\quad N_{\mathrm{left\,C6,AA}}(f)\ge C_s(s+1)_6.
\]

**Applies under:** s=2^h>=8, physical alphabet a minimal with binom(a,2)>=V; fixed full globally injected original point map f; (s+1)_6 counts distinct original line choices via the true source incidence degree.

**Cannot conclude:** Occupied physical six-cycles are only left candidates, not individually accepted D6 motifs for every fixed globally injected g.

**Linked claim:** HYP105-AA4RCYC-D6-QUENCHED-LOWER

**Pinned source:** [PR #480 @ 53af9d2f03ef](https://github.com/definitely-stable/Mathlab/blob/53af9d2f03ef4fec147b633558a0e7bb96aea070/docs/research/HYP-105-ISSUE230-D6AA4R-QUENCHED-ORIGINAL-D6.md)

## HYP105-F-012 — Every fixed f direct original D6 conditional mean lower

\[
\forall f,\ s=2^h\ge8:\quad \mathbb E_g[D_6(f,g)\mid f]\ge\frac{(a)_6}{(K)_6}\left[\frac{(a)_6}{12}-(K-V)(a-2)_4\right](s+1)_6\ge\frac{s^6}{8}.
\]

**Applies under:** h>=3; fixed arbitrary complete original global point injection f and a SINGLE uniformly random complete original global line injection g; exact finite s=8..128 checks plus all s>=256 source inequalities.

**Cannot conclude:** min_f max_g S>=s^6/8 is not min_(f,g) S>=s^6/8; no probability concentration is asserted.

**Linked claim:** HYP105-AA4RCYC-D6-QUENCHED-LOWER

**Pinned source:** [PR #480 @ 53af9d2f03ef](https://github.com/definitely-stable/Mathlab/blob/53af9d2f03ef4fec147b633558a0e7bb96aea070/docs/research/HYP-105-ISSUE230-D6AA4R-QUENCHED-ORIGINAL-D6.md)

## HYP105-F-013 — True original GQ-dual fixed g direct D6 conditional lower

\[
\forall g,\ s=2^h\ge8:\quad \mathbb E_f[D_6(f,g)\mid g]\ge\frac{s^6}{8},\qquad \min_g\max_f S_s(f,g)\ge\frac{s^6}{8}.
\]

**Applies under:** h>=3; every fixed complete original globally injected line map g; f uniformly sampled from complete globally injected original point physical-edge maps using true original W(3,s) point-line incidence duality.

**Cannot conclude:** Does not imply a universal pointwise bound for every f,g nor a full seven-class root theorem.

**Linked claim:** HYP105-AA4RCYC-D6-DUAL-QUENCHED-LOWER

**Pinned source:** [PR #480 @ 53af9d2f03ef](https://github.com/definitely-stable/Mathlab/blob/53af9d2f03ef4fec147b633558a0e7bb96aea070/docs/research/HYP-105-ISSUE230-D6AA4R-QUENCHED-ORIGINAL-D6.md)

## HYP105-F-014 — True original B/A rooted universe lower and unilateral physical marginal capacities

\[
d=s+1,\quad V=(s+1)(s^2+1),\quad M_p=\binom d2\frac{\prod_{j=0}^3d(V-3-2j)}{24},\quad B_p=3\binom{a-2}{4}\binom d2 d^4,\quad A=70\binom a6d^6.
\]

**Applies under:** All h>=1; a is the minimal physical coordinate alphabet with binom(a,2)>=V, each p is a TRUE repeated original point root; M_p is a SOURCE UNIVERSE LOWER, B_p,A are unilateral PROJECTION UPPER bounds.

**Cannot conclude:** M_p is not exact |U_p| in general, and unilateral upper bounds do not determine actual globally coherent intersections.

**Linked claim:** HYP105-AA4S-ROOT-FRECHET-ZERO

**Pinned source:** [PR #479 @ 357b3d201e14](https://github.com/definitely-stable/Mathlab/blob/357b3d201e14713668fbd045b450ffd279610081/docs/research/HYP-105-ISSUE230-D6AA4S-ROOT-CONDITIONAL-FRECHET.md)

## HYP105-F-015 — All-h genuine original point-root Fréchet-only certificate is zero

\[
\forall h\ge1,\ \forall f,g,\ \forall p:\quad |U_p|\ge M_p>B_p+A\ge|L_p(f)|+|R_p(g)|,\quad \max\{0,|L_p|+|R_p|-|U_p|\}=0.
\]

**Applies under:** Genuine W(3,2^h) and six distinct ORIGINAL incidence IDs; all p, arbitrary COMPLETE globally injected f and g. The analogous original line-root A/B floor is zero by GQ duality.

**Cannot conclude:** The Fréchet lower bound zero is NOT an assertion that actual B/A physical-source intersections vanish for any global injection.

**Linked claim:** HYP105-AA4S-ROOT-FRECHET-ZERO

**Pinned source:** [PR #479 @ 357b3d201e14](https://github.com/definitely-stable/Mathlab/blob/357b3d201e14713668fbd045b450ffd279610081/docs/research/HYP-105-ISSUE230-D6AA4S-ROOT-CONDITIONAL-FRECHET.md)

## HYP105-F-016 — Finite true W32 root counts versus genuine positive joint B/A seven-GF5 motifs

\[
s=2,\quad |U_p|=111132\ (15\ \mathrm{true\ roots}),\quad \mathrm{FrechetFloor}_p=0,\quad |J^{BA}(f_{\mathrm{S68}},g_{\mathrm{S68}})|=44,\quad |J^{BA}(f_{\mathrm{S72}},g_{\mathrm{S72}})|=36.
\]

**Applies under:** FINITE W(3,2) only; all 45 true original incidence IDs and two fixed globally injected source f/g fixtures S68,S72, actual original seven-class census.

**Cannot conclude:** Finite genuine positive intersections do not extend to all-h minimax positivity; root-conditioned marginal-only zero does not imply actual zero.

**Linked claim:** HYP105-AA4S-W32-POSITIVE-JOINT-ZERO-MARGINAL

**Pinned source:** [PR #479 @ 357b3d201e14](https://github.com/definitely-stable/Mathlab/blob/357b3d201e14713668fbd045b450ffd279610081/docs/research/HYP-105-ISSUE230-D6AA4S-ROOT-CONDITIONAL-FRECHET.md)

## HYP105-F-017 — Exact 60-cycle six ORIGINAL incidence-position aligned D6 tensor

\[
\mathcal C_6=\{\text{60 labelled connected C6 on 6 ORIGINAL columns}\},\qquad D_6(f,g)=\sum_{H\in\mathcal C_6}\ \sum_{Q\in\mathcal Q_{AA}}A_f(H,Q)A_g(H,Q).
\]

**Applies under:** ALL h>=1, every pair of separately typed complete ORIGINAL globally injected f,g; same six genuine incidence IDs and fixed canonical source-column order on both sides.

**Cannot conclude:** Positive original-side 60-fibre tensor populations do NOT imply their exact aligned joint inner product is positive.

**Linked claim:** HYP105-AA4T-POSITIONAL-D6-TENSOR

**Pinned source:** [PR #484 @ c51448b4e47b](https://github.com/definitely-stable/Mathlab/blob/c51448b4e47b17737285ef8e6b7ea09991a8c289/docs/research/HYP-105-ISSUE230-D6AA4T-QUENCHED-ALIGNED-D6.md)

## HYP105-F-018 — All-h exact quenched original positional D6 expected inner product

\[
T_f=\sum_{H\in\mathcal C_6}\sum_{Q\in\mathcal Q_{AA}}A_f(H,Q),\qquad K=\binom a2,\quad V=(s+1)(s^2+1),\quad \mathbb E_g[D_6(f,g)\mid f]=\frac{(a)_6}{(K)_6}T_f.
\]

**Applies under:** h>=1; all fixed complete original point maps f; a is minimal with binom(a,2)>=V; expectation only over ONE uniformly sampled complete original global line map g.

**Cannot conclude:** Events across different original Q,H share one g and need not be independent; no pointwise bound.

**Linked claim:** HYP105-AA4T-QUENCHED-TENSOR-IDENTITY

**Pinned source:** [PR #484 @ c51448b4e47b](https://github.com/definitely-stable/Mathlab/blob/c51448b4e47b17737285ef8e6b7ea09991a8c289/docs/research/HYP-105-ISSUE230-D6AA4T-QUENCHED-ALIGNED-D6.md)

## HYP105-F-019 — All-h original C6 Hall candidate count and weaker global conditional floor

\[
m=K-V\le a-2,\quad T_f\ge\left[\frac{(a)_6}{12}-m(a-2)_4\right]\max\{1,(s+1)_6\},\quad \forall h\ge1\ \forall f:\ \mathbb E_g D_6(f,g)\ge\frac{s^6}{98304}.
\]

**Applies under:** True original d=s+1 regular incidence; d<6 requires Hall matching rather than falling-factorial positivity. h>=1, fixed globally injected f, random ONE complete g. For h>=3 existing AA4R 1/8 is stronger.

**Cannot conclude:** The weaker all-h constant does not supersede h>=3 1/8 bound, and does not imply inf_(f,g) D6 or S_s positivity.

**Linked claim:** HYP105-AA4T-ALLH-QUENCHED-D6-LOWER

**Pinned source:** [PR #484 @ c51448b4e47b](https://github.com/definitely-stable/Mathlab/blob/c51448b4e47b17737285ef8e6b7ea09991a8c289/docs/research/HYP-105-ISSUE230-D6AA4T-QUENCHED-ALIGNED-D6.md)

## HYP105-F-020 — All-h exact GQ dual fixed-right original D6 conditional floor

\[
\forall h\ge1\ \forall g:\qquad \mathbb E_f[D_6(f,g)\mid g]\ge\frac{s^6}{98304},\quad s=2^h.
\]

**Applies under:** Genuine ORIGINAL W(3,2^h) point-line source duality; every fixed globally injected line map g; expectation over ONE independently uniformly random complete point map f.

**Cannot conclude:** Does not imply a bound for each jointly fixed f,g; for h>=3 AA4RCYC 1/8 is stronger.

**Linked claim:** HYP105-AA4T-ALLH-DUAL-QUENCHED-LOWER

**Pinned source:** [PR #484 @ c51448b4e47b](https://github.com/definitely-stable/Mathlab/blob/c51448b4e47b17737285ef8e6b7ea09991a8c289/docs/research/HYP-105-ISSUE230-D6AA4T-QUENCHED-ALIGNED-D6.md)

## HYP105-F-021 — Genuine W32 60-position tensor mean-versus-realized-zero certificate

\[
s=2,\quad T_{f_{\mathrm{S68}}}=T_{f_{\mathrm{S72}}}=21186,\quad \mathbb E_g[D_6\mid f]=\frac{21186}{5005}=\frac{1926}{455}>0,\quad D_6(f,g_{\mathrm{S68/S72}})=0,\quad S_{\mathrm{S68/S72}}\in\{68,72\}.
\]

**Applies under:** FINITE true original W(3,2), six distinct original incidence IDs, 60 fixed source-column C6 fibres, full K6 global injection fixtures S68 and S72; conditional expectation differs from actual fixed g outcome.

**Cannot conclude:** D6=0 at s=2 does not establish S_s=0 (actually 68/72 here) or an infinite original low-S family.

**Linked claim:** HYP105-AA4T-W32-POSITIVE-MEAN-ZERO-D6

**Pinned source:** [PR #484 @ c51448b4e47b](https://github.com/definitely-stable/Mathlab/blob/c51448b4e47b17737285ef8e6b7ea09991a8c289/docs/research/HYP-105-ISSUE230-D6AA4T-QUENCHED-ALIGNED-D6.md)

## HYP105-F-022 — True original all-h six-edge source forests and nine eligible cells

\[
Q\subseteq E(W(3,2^h)),\ |Q|=6\Longrightarrow Q\ \text{is acyclic};\quad \mathcal F=\{AA,AB,BA,AC,CA,BC,CB,BB_{\rm overlap},BB_{\rm disjoint}\},\quad CC=\varnothing.
\]

**Applies under:** h>=1, every six DISTINCT actual source incidence ID. The nine cells partition only Q whose BOTH source endpoint multiplicity profiles are in A/B/C; other Q are outside the eligible grid.

**Cannot conclude:** A forest source type alone does not assert any physically accepted original six-GF5 motif.

**Linked claim:** HYP105-AA4U-NINE-ORIGINAL-FOREST

**Pinned source:** [PR #486 @ f49dcef044e8](https://github.com/definitely-stable/Mathlab/blob/f49dcef044e8a4f1bb17f080ffa11c7b365a077a/docs/research/HYP-105-ISSUE230-D6AA4U-SOURCE-FOREST-TRANSPORTATION.md)

## HYP105-F-023 — Deterministic source-forest conditioned two-side Fréchet lower

\[
X_F(f,g)=|L_F(f)\cap R_F(g)|\ge\max\{0,|L_F(f)|+|R_F(g)|-|U_F|\},\qquad LB_{\mathrm{nonAA}}=\sum_{F\in\mathcal F\setminus\{AA\}}\max\{0,|L_F|+|R_F|-|U_F|\}.
\]

**Applies under:** all h>=1, every complete original globally injected f,g, SAME original six-incidence Q on two sides, each eligible ORIGINAL forest cell F. Applies as lower to the accepted NON-AA count.

**Cannot conclude:** Abstract subset Fréchet sharpness does not supply a legal adversarial global injection attaining a zero floor; AA needs aligned D6 and is not certified.

**Linked claim:** HYP105-AA4U-FOREST-FRECHET-LOWER

**Pinned source:** [PR #486 @ f49dcef044e8](https://github.com/definitely-stable/Mathlab/blob/f49dcef044e8a4f1bb17f080ffa11c7b365a077a/docs/research/HYP-105-ISSUE230-D6AA4U-SOURCE-FOREST-TRANSPORTATION.md)

## HYP105-F-024 — Complete finite original W32 eligible forest source census

\[
|E(W(3,2))|=45,\quad \binom{45}{6}=8\,145\,060;\qquad \sum_{F\in\mathcal F}|U_F|=6\,540\,870,\quad 8\,145\,060-6\,540\,870=1\,604\,190.
\]

**Applies under:** FINITE genuine ORIGINAL W(3,2) only, full 45 choose 6 six-DISTINCT source original incidence-ID sets; 1,604,190 have source profiles outside the both-sides A/B/C eligibility filter.

**Cannot conclude:** Counts of physical projected sixsets are not source-only totals; nothing about s>=4 follows from this finite census.

**Linked claim:** HYP105-AA4U-W32-NINE-FOREST-CENSUS

**Pinned source:** [PR #486 @ f49dcef044e8](https://github.com/definitely-stable/Mathlab/blob/f49dcef044e8a4f1bb17f080ffa11c7b365a077a/docs/research/HYP-105-ISSUE230-D6AA4U-SOURCE-FOREST-TRANSPORTATION.md)

## HYP105-F-025 — W32 genuine nine-cell S68 joined count and zero marginal certificate

\[
s=2,\quad \sum_F X_F(S68)=331,\quad X_{AA}(S68)=263,\quad D_6(S68)=0,\quad S(S68)=331-263=68,\quad LB_{\rm nonAA}(S68)=0.
\]

**Applies under:** Finite genuine source W(3,2) S68 single pair of complete global point/line maps, exact common original-ID nine-cell physically joined sets and true D6 classifier.

**Cannot conclude:** Zero relaxed lower for eight non-AA source cells does not imply zero real non-AA charge; no infinite minimax counterfamily.

**Linked claim:** HYP105-AA4U-W32-ZERO-MARGINAL-POSITIVE-JOINT

**Pinned source:** [PR #486 @ f49dcef044e8](https://github.com/definitely-stable/Mathlab/blob/f49dcef044e8a4f1bb17f080ffa11c7b365a077a/docs/research/HYP-105-ISSUE230-D6AA4U-SOURCE-FOREST-TRANSPORTATION.md)

## HYP105-F-026 — W32 genuine nine-cell S72 joined count and zero marginal certificate

\[
s=2,\quad \sum_F X_F(S72)=358,\quad X_{AA}(S72)=286,\quad D_6(S72)=0,\quad S(S72)=358-286=72,\quad LB_{\rm nonAA}(S72)=0.
\]

**Applies under:** Finite genuine source W(3,2) S72 single pair of complete global point/line maps, exact common original-ID nine-cell physically joined sets and true D6 classifier.

**Cannot conclude:** An AA/A source joint candidate is not an accepted aligned physical D6, and zero marginal Fréchet cannot characterize real joint S.

**Linked claim:** HYP105-AA4U-W32-ZERO-MARGINAL-POSITIVE-JOINT

**Pinned source:** [PR #486 @ f49dcef044e8](https://github.com/definitely-stable/Mathlab/blob/f49dcef044e8a4f1bb17f080ffa11c7b365a077a/docs/research/HYP-105-ISSUE230-D6AA4U-SOURCE-FOREST-TRANSPORTATION.md)

## Formula review protocol

Verify original six-incidence constraints, alphabet, all-h range, global injection semantics, and quantifier order against the cited proof commit. CI does not mechanically check the algebra.

