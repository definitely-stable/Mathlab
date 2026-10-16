# HYP-105 / issue #230 — AA4-AR: true ORIGINAL D6 concentration with **both physical supports adversarially fixed**

**Research-only Draft, genuine symplectic original source W(3,s), s=2^h≥8, ANY complete global f, ANY occupied original line physical edge image, a single global random assignment of those occupied edges to original line factors. Not a theorem for every fixed global pair (f,g), not root Branch A/B/C, not a full seven-GF5 or ASET claim.**

Strict stacked child of [AA4-AQ quenched one-map mean PR #541](https://github.com/definitely-stable/Mathlab/pull/541), pinned exact original parent HEAD \`098b03a516c1fbba9df81f1ee9c89c4d9084ef54\`. Four additive math/test/proof/hosted-workflow research artifacts. No main edits, no fabricated large GQ, no per-original-Q independently redrawn global labels.

## 1. Prior art and sharpened scientific quantifiers

- Parent [#541](https://github.com/definitely-stable/Mathlab/pull/541) already proves a **ONE global map f fixed, other physical image support fixed** exact conditional mean \( \mathbb E_\pi S_{\mathrm{D6}}(f,g_\pi)=A_6(f)\,12C_6(G_g)/(V)_6\), with \(\mathbb E_\pi S_{\rm D6}\ge(2/3)s^6\) for every dyadic s≥4 and a uniformly exact leading constant \(16/3\). It does NOT prove variance, concentration or high probability.
- Parallel [W2-CYC #542](https://github.com/definitely-stable/Mathlab/pull/542) **already** proves relative variance \(O(s^{-3})\) for every fixed adversarial genuine-original point f with one uniform complete globally injected line factor image map g, but **does not condition on g's occupied physical pair-image support**. Its genuine-original six-line codegree \(\Delta_6\le103680d^3\), all r=0..6 source-line overlap decomposition, classical physical C6 path gluing and Cauchy/Chebyshev arguments are credited, not invented here. Earlier #487/#492 likewise already develop original line-overlap kernels and absolute second moment.
- **New AA4-AR objective:** preserve **both** typed physical pair-edge image supports adversarially, and sample ONLY one uniformly global original-line-factor-to-those-preselected-physical-edges **bijection**. Infer a uniform quantitative relative variance and high-probability bound for this strictly smaller conditional sample space. The crucial r=0 correction uses **the actual fixed occupied line C6 support** and cancels, rather than treating six right-hand physical edges as drawn independently or secretly averaging physical holes.

This is strictly stronger than #542 in physical-support conditioning, not a universal deterministic for-every-\(f,g\) theorem, and not a new abstract inequality beyond established combinatorial second-moment tools.

## 2. Exact genuine ORIGINAL probability space and overlap setup

Let W(3,s), s=2^h,h≥3, have \(V=(s+1)(s^2+1)\) actual ORIGINAL point source factors, V actual ORIGINAL line source factors, source degree \(d=s+1\), and complete globally injected physical pair maps into minimum \(K_a\), \(a=\min\{t:\binom t2\ge V\}\), \(K=\binom a2\), missing physical label count \(m=K-V\le a-2\). Fix ANY original f on point source factors, and ANY fixed set \(E_g\subset E(K_a)\) of V distinct physical unordered pairs to serve as the globally occupied physical image of the ORIGINAL line factors.

Sample ONE uniform bijection \(\pi\) from the V actual ORIGINAL line factor IDs onto exactly E_g. All actual original incidence flag IDs, all source sixsets and all point/line original factor memberships use this same \(\pi\) without per-Q redraw. Write \(D=S_{\rm D6}(f,g_\pi)\), where D6 means the **historical aligned** two-typed connected physical C6 dual on the SAME six genuine original incidence flag IDs. The source pool \(\mathcal Q_f\) is the actual original six-different-point, six-different-line incidence Q with fixed-f point physical dual C6, and \(N=|\mathcal Q_f|\).

Let \(C=C_6(E_g)\) be the number of physical simple undirected C6 in the **fixed** line physical image. For every \(\mathcal Q_f\) event \(X_Q\) the single-global-bijection marginal is the same:

\[
p=\frac{12C}{(V)_6},\qquad \mu=\mathbb E_\pi D=Np .
\]

For the exact globally injected original source GQ, the parent AA4-AQ gives

\[
L_6=\frac{(a)_6}{12}-m(a-2)_4,\quad
N\ge N_0:=L_6\,d^4(d^2-15),\quad
C\ge L_6,\quad
p\ge p_0:=\frac{12L_6}{(V)_6}
\]

for every s≥4. Consequently \(\mu\ge N_0p_0\ge\frac23s^6\).

## 3. NEW AQ/AR gluing conditional on a fixed physical image

Fix an actual original eligible source six-Q and condition on \(X_Q=1\). Its six distinct original line factors have been assigned six different physical edges in ONE physical C6 contained in E_g. The other V−6 line factor images are a uniform bijection onto the remaining V−6 **occupied edges of E_g**, not K−6 unrestricted physical edges.

For a second true original six-Q' with exactly \(r\in\{0,\ldots,6\}\) common original LINE factors, its fixed shared r physical images are prescribed. For r≥1 and r≤5, those prescribed physical edges, when extendable to a simple physical C6, decompose into c vertex-disjoint simple paths (\(c\le\min(r,6-r)\)), and the classical path extension count is

\[
M_{r,c}=2^{c-1}(5-r)!\binom{a-r-c}{6-r-c},
\qquad
M_r=\max_{1\le c\le\min(r,6-r)}M_{r,c}.
\]

Every such physical completion can be aligned to the prescribed six named original source line factor positions in at most 12 ways. Thus

\[
q_r:=\Pr(X_{Q'}=1\mid X_Q=1)\le
\min\left(1,\frac{12M_r}{(V-6)_{6-r}}\right)
\quad(1\le r\le5),\qquad q_6\le1.
\]

The key **fixed-support r=0 bound**, taking C6 only among the same already occupied E_g instead of ALL K_a edges, is

\[
q_0\le\frac{12C}{(V-6)_6},
\qquad
\boxed{\frac{q_0}{p}\le\frac{(V)_6}{(V-6)_6}.}
\]

Here the actual C cancels EXACTLY. This is the new support-preserving step relative to the #542 probability space; no false unconditional independence of disjoint source line factor sets and no replacement by a fake full physical K_a global image.

## 4. Actual ORIGINAL sixset line-codegrees and rigorous all-h second moment

Fix r distinct ACTUAL original LINE source factors of W(3,s). For r=1..5, at most d^r choices of genuine original neighboring points are incident to the named source lines, and any prescribed r global f physical edges can appear in at most M_r physical C6. Completing the other six−r genuine-original line IDs at their actual GQ neighbors gives:

\[
\Delta_r=\max_{|T|=r}\#\{Q\in\mathcal Q_f:T\subseteq L(Q)\}
\le d^6M_r,\quad 1\le r\le5.
\]

At r=6 the existing genuine-original [#542](https://github.com/definitely-stable/Mathlab/pull/542) sixline source codegree result applies unchanged to the fixed f and fixed physical image: six true original line factors touch at most 6d actual original point factors, and their images under **the one globally fixed injective f** have at most 6d edges. Each physical C6 is determined by an ordered triple of alternating oriented physical edges, so there are at most (2E)^3/12 C6 among E edges. Each such C6 supports at most 6! assignments of the six named real source line IDs, hence

\[
\boxed{\Delta_6\le\min(d^6,103680d^3).}
\]

This is **prior proof from #542**, here imported as a separately executable independently tested bound (no #542 runtime dependency). The present contribution is the support-quenched application of all source codegrees to the **same** full ORIGINAL source incidence flag Q sample space.

The number of ordered true-original eligible Q,Q' with exactly r≥1 common original line factors is at most \(\binom6r N\Delta_r\). For r=0 at most N². Therefore the exact uniform proof certificate for \(\varepsilon:=\operatorname{Var}_\pi(D)/\mu^2\) is

\[
\boxed{
\varepsilon\le\varepsilon^{\rm cert}_{s}:=
\frac{(V)_6}{(V-6)_6}-1
+
\sum_{r=1}^{6}
\frac{\binom6r\Delta_r}{N_0}\,
\frac{q_r}{p_0}.
}
\]

Every term is an exact rational, and the original-to-physical source label maps remain globally coherent. The displayed \(\varepsilon^{\rm cert}_s\) is an UPPER on the true variance, not the exact measured finite variance. Some bounds exceed one for small s, which does not invalidate the theorem but yields vacuous probability lower estimates until s grows.

## 5. NEW all-h analytic explicit two-support concentration theorem

For every dyadic s≥8, a≥35, d≥9, simple exact physical/minimum-palette estimates give:

\[
L_6\ge \frac{a^6}{30},\qquad
d^4(d^2-15)\ge\frac{22}{27}d^6,\qquad
N_0\ge\frac{a^6d^6}{40}.
\]

Also \(V\le a^2/2\), \(V\ge a^2/3\), \(V-11\ge a^2/6\), \((V)_6\le(a^2/2)^6\), and

\[
p_0\ge\frac{2a^6}{5(V)_6},\qquad
\frac1{p_0}\le\frac{5a^6}{128}.
\]

For 1≤r≤5, the exact physical path extension capacity obeys \(M_r\le a^{5-r}\); consequently

\[
\frac{\binom6r\Delta_r}{N_0}\frac{q_r}{p_0}
\le
\frac{75}{4}\binom6r\,6^{6-r}\frac1{a^2}.
\]

Numerators for r=1 through 5 respectively:
874,800; 364,500; 81,000; 10,125; 675. Their sum is **1,331,100**.

The disjoint source line correction satisfies
\[
\frac{(V)_6}{(V-6)_6}-1
\le(1+36/a^2)^6-1
\le 500/a^2
\]
for a≥35. The six-source-line overlap term is
\[
\Delta_6/(N_0p_0)\le162000/d^3.
\]

Thus the NEW all-h uniform **fixed physical support** relative variance bound:

\[
\boxed{
\frac{\operatorname{Var}_\pi(D)}{(\mathbb E_\pi D)^2}
\le\varepsilon^{\rm cert}_s
\le\frac{1\,331\,600}{a^2}+
\frac{162\,000}{(s+1)^3}
\le\frac{827\,800}{s^3}.
}
\]

The last step uses a²≥2V≥2s³ and d≥s. The NEW constant is independent of BOTH physically occupied f-image and g-image support choice. It is not a claim of optimal constants or new general concentration theory. The code proves every inequality using exact Fraction/BigInteger arithmetic for dyadic h1..80 and separately records the symbolic elementary bound and proof, not a numerical fitted regression.

Since parent AA4-AQ already proves \(\mu\ge\frac23s^6\) for all h≥2, standard Paley–Zygmund/Cauchy–Schwarz and Chebyshev applied to this support-quenched variance give

\[
\boxed{
\Pr_\pi[D>0]\ge\frac1{1+\varepsilon^{\rm cert}_s},
\qquad
\Pr_\pi\!\left[D\ge\frac13s^6\right]
\ge\max\{0,1-4\varepsilon^{\rm cert}_s\}.
}
\]

Hence as s→∞, **for EVERY arbitrary fixed global original point f AND EVERY arbitrary FIXED globally valid physical line-image support E_g**, a uniformly random ONE globally coherent original-line-factor assignment to the preselected occupied physical edges gives at least \(s^6/3\) genuine original aligned D6 source sixsets with probability \(1-O(s^{-3})\), uniformly in the two adversarial fixed physical supports.

This is **not** a theorem that every fixed full original line labeling g already has positive D6, and not a theorem for all seven original GF5 selected classes with both globally correlated f/g fixed. W32 genuine original S68 and S72 currently fixed full global g have D6=ZERO, despite the positive conditional means of AA4-AQ; there is no logical contradiction because the distribution allows exceptional permutations.

## 6. Falsifiers, evidence and missing gate

Four additive source/test/proof/hosted-CI artifacts:

1. Exact all h=3..80 original V,d,a,m, fixed physical two-support rational \(\varepsilon^{\rm cert}_s\) from all seven r=0,...,6 original LINE overlap sectors, symbolic upper 1331600/a²+162000/d³ and 827800/s³, parent exact conditional \(\mu_{\min}\ge2s^6/3\), derived positive/good-half probability lower, genuine source-model flags and no FALSE every-fixed-g conclusion. Only small genuine symplectic W32/W34/W38 instances are actually materialized; huge h remain algebraic all-h proofs.
2. Independent physical permutations K6,K7,K8 enumerate EVERY undirected connected 6cycle, then test fixed prescribed r=1..5 physical path subsets using unrelated vertex adjacency DFS, direct physical C6 extension inclusion, and exact old path-component capacity. No reliance on the new variance module for physical C6 generation.
3. Independent true ORIGINAL W(3,2) globally injected fixed point f for lex/S68/S72: build true six-incidence source Q from global physical point C6 and genuine original line neighbors, directly count actual source-line fixed-six-set codegree under f without the 103680d³ analytical bound.
4. True W32 S68 and S72 fixed fully global point/line maps have ZERO selected original D6 while parent AA4-AQ conditional first moment is positive; verify strict h≥3 scope and reject any false universal deterministic extrapolation.
5. Genuine original W(3,4) with global K14 and six physical pair holes, genuine W(3,8) with global K35 and ten physical pair holes, lex/random global maps: fixed E_g remains the SAME actual physical line edge support; check true original six-line SDR from actual W3 incidence, GQ uniform original source factor distinctness and all-h physical two-support codegree bounds (the variance theorem itself starts h≥3).
6. Source automorphism and distinct physical point/line alphabet permutations preserve original mapping validity. Invalid noninjective global pair labels, invalid original GQ incidence truncation, s=2/4 and non-dyadic orders fail closed.
7. Root nonimplication: no proof of inf over BOTH full adversarial globally injected f,g of selected seven-GF5 \(S_s(f,g)\ge cs^6\), no actual original infinite \(S=o(s^6)\) counterfamily, no root A/B/C, no full R3 or ASET exponent.

**Genuine next scientific gate AA4-AS:** A second-moment theorem over one globally permuted g, even with BOTH physical occupied supports adversarial, still permits a tiny but nonempty exceptional deterministic g set. To attack the root all-global minimax, derive a uniform **switching stability/defect compensation inequality** between original D6 and B/A, A/B, B/B and zero-D-anchor source C/* selected modes at the SAME fully fixed f,g; or construct a true-original globally complete infinite counterfamily killing the total selected seven-class mass. Merely more concentration with randomness in g does not close the root.

**Integration and provenance:** Strict Draft child of #541. Require exact FINAL HEAD hosted dedicated/INDEX/Proof Audit/Full Research SUCCESS and a separate independent mathematical referee before accepting scientific claims, registering SHA-pinned canonical RCP JSON and regenerating its five derived Markdown registers. Never hand-edit generated docs. Do not merge unreviewed research stack or close issue #230.
