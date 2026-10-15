# HYP-105 / issue #230 — D6-AA4-W-CYC: uniform all-h quenched ORIGINAL D6 second-moment upper and dimension-free conditional success

**NEW rigorous all-h theorem; scientific classification: conditional/probabilistic, NOT adversarial all-map lower.** Work in genuine ORIGINAL symplectic generalized quadrangles \(W(3,s)\), \(s=2^h\ge8\), on actual distinct point-line source incidence IDs. Let \(V=(s+1)(s^2+1)\) true source points / true source lines, \(d=s+1\) actual incidence degree, and let \(a\) be the **minimal** physical coordinate alphabet with \(K=\binom a2\ge V\). Fix absolutely ANY full globally injective physical edge-pair map \(f\) of ALL original point factors, and draw ONE uniform full globally injected ORIGINAL source-line edge map \(g\), common to EVERY actual original six-incidence Q. Then, where \(D_6(f,g)\) is the TRUE historical accepted seven-GF5 ORIGINAL six-ID A/A class with coincident CONNECTED six-position coordinate-dual C6 on both sides,

\[
\boxed{\forall f\quad \mathbb E_gD_6(f,g)^2\le B_s\le 25\,793\,703\,936\,s^{12}<3\cdot10^{10}s^{12}.}
\]

Combining with the already independently established all-h direct genuine D6 theorem from [D6-AA4-R-CYC #480](https://github.com/definitely-stable/Mathlab/pull/480), \(\forall f,\mathbb E_gD_6(f,g)\ge s^6/8\), yields, by Cauchy–Schwarz (the \(\theta=0\) Paley–Zygmund inequality),

\[
\boxed{\forall f\quad\Pr_{\text{ONE complete uniform }g}[D_6(f,g)>0]\ge
\frac{(\mathbb E_gD_6(f,g))^2}{\mathbb E_gD_6(f,g)^2}
\ge\frac1{1\,920\,000\,000\,000}.}
\]

By genuine ORIGINAL GQ point-line duality, the same bound holds \(\forall g,\Pr_f(D_6(f,g)>0)\). This gives a **dimension-free probability of REAL accepted GF5 D6 success against ANY frozen opposite side** for every \(s=2^h\ge8\), not merely a fixed W32 f. However it is **not \(\forall f,g\,D_6>0\)** and emphatically **does NOT prove** \(\min_{f,g}S_s(f,g)=\Omega(s^6)\) (root issue #230 OPEN). In real original W32 S68/S72, historically valid complete g with D6=0 already exist even though full-uniform-right expectation and finite variance are positive.

**Stack and scope:** Strict research-only Draft on 4/4-green [D6-AA4-V-CYC #489](https://github.com/definitely-stable/Mathlab/pull/489), pinned exact base \`8740a5fee63bc70e494538367b284f4ae1c69f68\`. Four additive files (Python rational proof engine, independent true GQ source incidence tests, this formal theorem/protocol doc, GitHub-hosted workflow). No writes/merge to main or issue closure. Not repeating #489's exact FINITE W32 \(448\,846\,596\) original ordered pair census; the new result is the first analytical bound on **ALL orders and EVERY possible complete f**.

## 1. The ALL-h uniform second-moment proof without a probabilistic independence assumption

Fix any genuine \(W(3,s)\) and complete original point map f. Let \(\mathcal Q_f\) consist of true six-DISTINCT-original-incidence-ID Q, each using SIX DIFFERENT genuine original source point factor IDs and SIX DIFFERENT original source line factor IDs, with physical-left connected single C6 column-dual. As proved independently in #480, each such Q is eligible for REAL right-side historical GF5 D6 with probability

\[
p=\frac{(a)_6}{(K)_6}
\]

under ONE uniformly random globally injected complete g. Write \(X_Q=\mathbf1\{Q\text{ accepted as historical original D6 under }g\}\), so \(D_6(f,g)=\sum_{Q\in\mathcal Q_f}X_Q\). We bound \(\sum_{Q,Q'}\mathbb E_g X_QX_{Q'}\) by a TRUE ORIGINAL line-factor-overlap partition r=0,...,6.

### A. Uniform upper bound on the number of eligible ORIGINAL six-ID configurations

The physically occupied image of arbitrary full f is a subgraph of K_a and has at most \((a)_6/12\) UNDIRECTED simple connected physical C6 edge sets. Each contains six different globally injected actual point factors; every factor has exactly d genuine ORIGINAL incident lines. Choosing one actual original incidence per factor gives at most \(d^6\) six-distinct-original-flag Q; requiring six distinct source lines can only reduce that number. Thus

\[
\boxed{|\mathcal Q_f|\le N_s:=\frac{(a)_6}{12}\,d^6.}
\]

This is a true original source-incidence upper, not a synthetic physical P3 candidate count. It does not require a random f.

### B. Genuine original source-LINE set intersection capacity

Fix r different ACTUAL ORIGINAL source line factors \(\ell_1,\dots,\ell_r\), \(1\le r\le6\). Count eligible Q that contain all these r lines. For each fixed original source line \(\ell\), choose the unique point-line incidence in Q involving \(\ell\): at most d actual source point choices. If two fixed lines select the same original point, reject it (all Q have six distinct points); thus at most \(d^r\) real incidence assignments survive. Their r fixed globally occupied physical f(point) edges must lie on the same physical simple six-coordinate C6.

For \(1\le r\le5\), any r distinct edges in one simple 6-cycle touch **at least r+1 distinct physical coordinate vertices**; for r=6 they touch all six. Complete to at most six coordinate symbols by choosing at most \(a^{\max(5-r,0)}\) new coordinates, and arrange a simple C6 in at most 6! possible orderings. Each remaining actual original point factor can choose at most d incident original lines; collisions among these lines are ignored only because we are computing an upper bound. Consequently, for every original line subset \(L_0\) of size r,

\[
\boxed{
\#\{Q\in\mathcal Q_f:L_0\subseteq L(Q)\}
\le\Delta_r:=6!\,d^6a^{\max(5-r,0)}.
}
\]

No line-source overlap events are assumed independent. This argument uses the TRUE GQ original source point-line degree d and the single globally reused f.

### C. Conditional D6 probability when r original SOURCE LINE factors are shared

Condition on any eligible Q being genuine accepted D6 under ONE global g, so its six actual original line factor physical pair labels form an occupied simple physical C6. For an eligible second Q' that shares **exactly r** original source line factor IDs with Q, the r shared line pair labels are already fixed; the other 6−r original line factor physical pair labels are a uniform ordered sample WITHOUT REPLACEMENT from K−6 physically unused edges.

For r=0, the second accepted connected C6 has at most \((a)_6\) physical coordinate-edge assignments, hence

\[
q_0:=\Pr_g(X_{Q'}=1\mid X_Q=1,f,L(Q)\cap L(Q')=\varnothing)
\le \min\Bigl(1,\frac{(a)_6}{(K-6)_6}\Bigr).
\]

For \(1\le r\le5\), each shared ORIGINAL source line factor is a VERTEX in Q's and Q''s right-coordinate six-column cycle, and its fixed unordered physical edge-pair label prescribes two incident cycle coordinate symbols. Each such pair gives at most two orientation choices, so at most \(2^r\) consistent orientations for r shared vertices; invalid inconsistencies are simply rejected. The r shared vertices of a connected simple C6 cover at least r+1 of its six distinct coordinate edge colors. Therefore at most \(5-r\) still-free colors can be chosen in at most \(a^{5-r}\) ways. For r=6 all six are fixed and at most \(2^6\) orientation choices remain, capped at probability1. Thus

\[
\boxed{
q_r:=\Pr_g(X_{Q'}=1\mid X_Q=1,f)\le
\min\left(1,\frac{2^r a^{\max(5-r,0)}}{(K-6)_{6-r}}\right),
\quad 1\le r\le6.
}
\]

The formula is a **genuine positional upper bound** for every actual original line-C6 gluing, not an assumption that gluing depends only on r. AA4-U-CYC #487 proved the exact probability depends on cyclic placement. The bound deliberately maximizes over all placements and remains valid for actual nonaligned or completely incompatible diagrams, whose true probability is zero.

### D. Complete ordered-Q pair decomposition and finite exact uniform upper

For r0, bound the number of eligible ordered pairs by \(N_s^2\) and their joint probability by \(p q_0\).

For any r>=1, fix Q0. Choose r of its six actual original LINE factor IDs in at most \(\binom6r\) ways. Any Q' with EXACTLY r shared lines includes this chosen set, and by the source incidence packing lemma there are at most \(\Delta_r\) candidates. Therefore, without assuming an independent source hypergraph,

\[
\#\{(Q,Q')\in\mathcal Q_f^2:|L(Q)\cap L(Q')|=r\}
\le N_s\binom6r\Delta_r.
\]

Combining the exact uniform p with honest source-line overlap and conditional positional upper bounds yields an explicit finite rational **all-h bound independent of f**:

\[
\boxed{
\mathbb E_g D_6(f,g)^2\le
B_s:=
N_s^2p q_0+
N_sp\sum_{r=1}^{6}\binom6r\Delta_r q_r.
}
\]

Every original ordered pair is covered, including the diagonal and original Q that have IDENTICAL line-C6 D6 events. The globally injected right g is ONE shared sample for every Q; no false per-Q independent image assignments. The six-source original C6 construction and line-injection capacity count are genuine source GQ bounds. This is an actual all-h closed-form rational certificate, not finite extrapolation.

## 2. Uniform constant proof by elementary inequalities for EVERY power of two s>=8

Let s≥8. The minimal physical alphabet satisfies \(a\le2s^{3/2}\): minimality gives \((a-1)(a-2)<2V\), hence \(a<\sqrt{2V}+2\). Since \(V/s^3=(1+1/s)(1+1/s^2)\le585/512<5/4\), \(\sqrt{2V}<\frac85s^{3/2}\), and \(2\le\frac25s^{3/2}\), the bound follows. The full physical capacity \(K\ge V\ge s^3\) gives \(K-11\ge s^3/2\); genuine original source incidence degree \(d=s+1\le9s/8\).

The following inequalities hold for ALL genuine \(s=2^h\ge8\); no finite trend extrapolation is used:

\[
\begin{aligned}
N_s&<11s^{15},\\
p&\le4096s^{-9},\qquad q_0\le4096s^{-9},\\
\Delta_r&<1460\cdot2^{5-r}s^{13.5-1.5r},\quad1\le r\le5,\\
q_r&\le2^{11-r}s^{-10.5+1.5r},\quad1\le r\le5,\\
\Delta_6&<1460s^6,\qquad q_6\le1.
\end{aligned}
\]

Insert into the full seven-sector B_s expression. The r0 term is at most \(2\,030\,043\,136s^{12}\). For 1≤r≤5 each contribution is at most \(11\cdot1460\cdot4096\binom6r2^{16-2r}s^9\); since \(s\ge8\), \(s^9\le s^{12}/512\). The r6 contribution is at most \(65\,781\,760s^{12}\). The exact elementary integer sector-coefficient table is:

| Number r of common TRUE original source LINE factors | Uniform coefficient of s¹² |
|---|---:|
| 0 | 2,030,043,136 |
| 1 | 12,630,097,920 |
| 2 | 7,893,811,200 |
| 3 | 2,631,270,400 |
| 4 | 493,363,200 |
| 5 | 49,336,320 |
| 6 | 65,781,760 |
| **Total** | **25,793,703,936** |

Therefore, rigorously for EVERY \(s=2^h\ge8\) and EVERY complete global original point map f,

\[
\mathbb E_gD_6(f,g)^2\le B_s\le
25\,793\,703\,936s^{12}<3\cdot10^{10}s^{12}.
\]

The same true original W(3,s) point-line duality gives the analogous conditional second-moment bound with fixed g and random complete point f. Combined with AA4-R-CYC's all-h mean lower, the conditional Paley–Zygmund lower is exactly at least \(1/1\,920\,000\,000\,000\) for ANY frozen complete opposite-side map, for ALL powers s>=8. No finite experiment substitutes for this symbolic s≥8 proof.

## 3. Independent executable evidence and grounded improvements

The Python source uses exact integer falling factorials and \`Fraction\` only, with no Monte Carlo simulation. It prints:
- the exact elementary all-h integer constant by all seven overlap sectors;
- a stronger true-source bound \(\mathbb E D_6^2\le B_s\) as an exact rational function of minimal a,K,d for any requested s;
- the already independently pinned #480 true original fixed-f expected D6 lower \(L_s\);
- the **stronger, order-specific** uniform-in-f Cauchy lower \(\Pr_g(D_6>0)\ge L_s^2/B_s\), generally far better than the intentionally conservative clean all-h constant.

Independent tests exercise powers s=8..2²³ with exact rational arithmetic, validate minimal physical alphabet and seven source overlap-sector arithmetic, prove coefficient sum symbolically, and for each genuine W32 S68/S72 enumerate all **21,186 actual six-ID left connected physical C6 candidate Q** to verify real source line subset capacities against \(\Delta_r\) for r=1..6. Additional tests compare q_r bounds against the **independently proved exact shared-global-g cyclic original LINE gluing kernels** from AA4-U-CYC for r0,1,2,3,6. The finite W32 exact second moment #489 is an independent calibration reference, but NOT used to infer uniform all-h proof.

This is a stronger theoretical conclusion than merely completing finite second moments: original-source line factor packing controls **ALL** overlap terms at every order, and global physical injection without replacement does not destroy a dimension-free conditional success probability. The result has direct mathematical content, while the remaining unrestricted adversarial counterexample/dichotomy gap is acknowledged.

## 4. Limitations, formal blockers, and next useful research

**The original HYP-105 #230 root remains OPEN.** The theorem \(\forall f,\Pr_g(D_6(f,g)>0)\ge c_0\) does NOT assert \(\forall f,g\,D_6(f,g)>0\), much less \(\forall f,g\,S_s(f,g)\ge c s^6\). In actual original W(3,2) pinned S68/S72 complete globally injected g, D6=0. The lower bound \(c_0=1/1.92\text{ trillion}\) is intentionally explicit, correct and very conservative; it is NOT the exact true probability, nor a claim of practical random search efficiency or concentration in high probability. Even a strong \(\Pr(D_6>0)\) theorem leaves adversarial jointly chosen full f,g potentially bad.

**Recommended next D6-AA4-X-CYC:** Improve the genuine original line packing constant to meaningful all-h lower-tail for D6, and in parallel prioritize the true ROOT-relevant **deterministic all-seven compensator**: for every globally injected f,g, either the actually accepted D6 mass is large OR the NON-AA accepted two-sided original incidence-ID join from AA4-Q must have mass Ω(s⁶). Any such claim must use the same actual W(3,s) source incidence positions and ONE full f/g, survive JPKC/EICE local-transfer barriers, and state its assumptions; a stochastic conditional theorem alone cannot prove it. New original-source capacity inequalities from W-CYC and full W32 variance #489 supply regression guards for counterexamples.

Five? **FOUR additive research files**: Python mathematical proof/evaluator, independent original-source tests, this formal md theorem and sharp scope, dedicated three-job GitHub-hosted CI (two exact rational all-h derivations plus TRUE W32 capacity and cyclic-gluing oracle checks). Final exact SHA dedicated, INDEX, Proof Audit, Research must all succeed; independent mathematical peer review still required. Main untouched, Draft only, root issue #230 remains OPEN.
