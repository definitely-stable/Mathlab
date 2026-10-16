# HYP-105 / #230 — AA4-BD: Sharp CLEAN energy and one-tenth adversarial original LINE pins

**SCIENTIFIC DRAFT; original actual symplectic W(3,2^h); partial-map continuation only.** This is a strict child of [AA4-BC #564](https://github.com/definitely-stable/Mathlab/pull/564), pinned parent HEAD 76e67d85603cd7f8316b58b6d0a0d055b0392fb0. It is NOT Branch A/B/C, does NOT prove the accepted six-original-flag seven-GF(5) class lower, and does not change main or accepted registry.

## Precise theorem

Fix ANY dyadic s=2^h with h>=5; put d=s+1, V=(s+1)(s^2+1), a=min{a:binom(a,2)>=V}, t=a-2. Let the source be the TRUE original symplectic W(3,s); let f be ANY complete globally injected original POINT factor physical pair-edge assignment into K_a; E be ANY V-edge occupied right physical edge support. Take ANY k distinct ACTUAL original LINE-factor IDs and ANY injective physical assignment of these k source line IDs into E, with 0<=k<=floor(V/10). The pins, f and E may be arbitrarily correlated.

**BD-1 (DETERMINISTIC PARTIAL-MAP EXTENSION):** There exists a globally bijective COMPLETE original LINE factor right physical map g onto E extending ALL arbitrary pins, keeping f and E unchanged, such that

\[
\boxed{R_{\rm GOOD}(f,g)\ge s^6/80.}
\]

Here R_GOOD is the already-defined AA4-AO physically opposite GOOD wedge statistic on true source triples of exactly THREE distinct original incidence flags, with three different original point IDs and three different original LINE IDs. It is NOT the selected historical positive sixflag GF5 seven-class sum.

**BD-2 (CONDITIONAL QUENCHED MEAN AND SECOND MOMENT):** For ONE uniformly random COMPLETE original line bijection among all (V-k)! legal completions preserving the k arbitrary pins, the unpinned-source-only GOOD wedge count R_free has

\[
\mathbb E R_{\rm free}\ge s^6/80,\quad
\frac{\operatorname{Var}R_{\rm free}}{(\mathbb ER_{\rm free})^2}
\le\eta_{s,k}\le50\,000\,000/V=O(s^{-3}),
\]
\[
\Pr(R_{\rm GOOD}<s^6/160)\le\min(1,4\eta_{s,k}).
\]

The tail inequality may be vacuous for finite small s. The deterministic existence follows from the exact mean, NOT from assuming independent source flags.

## New exact ALL-h physical support lower bound

For ANY legal V-edge occupied support F of K_a, its missing-edge count m=binom(a,2)-V satisfies m<=a-2. AA4-AO bad coordinates depend on the original FULL occupied F:
\[
\operatorname{Bad}(F)=\{v:16\deg_{\overline F}(v)\ge a\},\quad |\operatorname{Bad}(F)|\le31.
\]
Let F° be induced on the NONBAD physical coordinates. Its rooted opposite-center CLEAN port energy is
\[
T_\circ(F)=\sum_{uv\in F^\circ}(\deg_{F^\circ}u-1)(\deg_{F^\circ}v-1).
\]

Parent #561 established, writing \(\tau=a-31\ge230\),
\[
T_\circ(F)\ge\bigl(\binom{\tau}2-m\bigr)(\tau-2)^2
-2m(\tau-1)(\tau-2).
\]
Since m<=a-2<a, this exceeds or equals
\[
L(\tau)=\bigl(\binom{\tau}2-(\tau+31)\bigr)(\tau-2)^2
-2(\tau+31)(\tau-1)(\tau-2).
\]

**BD-C — sharp all-h CLEAN support certificate:**
\[
\boxed{T_\circ(F)\ge 9V^2/8\qquad\forall h\ge5,\ \forall F.}
\]

Proof requires no finite-h fit. For u=τ−230>=0, direct exact polynomial expansion gives
\[
\boxed{
L(\tau)-\frac9{32}(\tau+31)^4
=\frac7{32}u^4+\frac{1287}{8}u^3+
\frac{637949}{16}u^2+\frac{27384651}{8}u+
\frac{737401095}{32}>0.
}
\]
Minimality implies V< a²/2, so L(τ)>=9 a^4/32>9V²/8. At the least allowed dyadic s=32 the exact constant term is already strictly positive. Thus #561 original \(V^2/16\) lower was conservative by a factor at least 18, and an improved physical estimate is available UNIFORMLY for both point and line complete occupied typed supports, without any assumed independence of their source maps.

## Genuine original source LINE pin-deletion lemma

Parent #561's genuine original source triple count B, with original physical point-side GOOD tests, satisfies
\[
B\ge d(d-1)(d-2)T_\circ(\operatorname{im}f).
\]
Parent #562 proved the ACTUAL original source maximal weight meeting a single specified original LINE-factor ID at most \(M_1\le 5d^3t^2\). This upper remains valid after restricting to unpinned originals. Deleting ALL triples using ANY of k arbitrarily pinned original LINE factors gives
\[
B_{\rm free}\ge \frac98 d(d-1)(d-2)V^2-5kd^3t^2.
\]
Since d>=33 implies (d−1)(d−2)>=(9/10)d² and minimal a implies t²<2V, for k<=V/10
\[
\boxed{B_{\rm free}\ge d^3 V^2
\bigl(\tfrac98\tfrac9{10}-\tfrac{10}{10}\bigr)
=d^3V^2/80.}\tag{BD-S}
\]
Every flag here is an actual W(3,s) original source incidence ID, not an artificial random source graph. The pinned original LINE subset can be chosen adversarially correlated with source incidence and with the point physical map.

## Physical pinned-edge deletion

For the original FULL E right occupied support, \(2T_\circ(E)\ge9V^2/4\) is the count of ordered three distinct physically opposite CLEAN pair-edge images. Each fixed physical pair edge occurs in at most \(2t^2\) such triples in each of three roles (center/outer0/outer1), by the genuine K_a opposite-port completion geometry established in #562. Deleting k arbitrary pinned physical edge images therefore removes at most \(6kt^2\) ordered favorable triples. Crucially use the CLEAN coordinates of ORIGINAL COMPLETE E; do NOT recompute Bad using the free support E minus pinned edges.

\[
A_{\rm free}\ge \frac94V^2-6kt^2
\ge(\frac94-\frac{12}{10})V^2
=\frac{21}{20}V^2\ge V^2.\tag{BD-F}
\]
No physical pair edge is reused; E remains the original globally injected image support of true original LINE factors.

## One complete global assignment: mean and existence

Condition on the given k fixed original LINE IDs and their k distinct physical edges. Sample a WHOLE bijection from the N=V−k other actual original LINE factors onto the N distinct remaining physical edges E_free. For any ordered triple of three distinct unpinned source LINE IDs the right image is uniformly distributed over \((N)_3\) ordered distinct free physical pair edges. Dependence between different source triples is permitted and preserved.

The exact conditional expected value is
\[
\mathbb E R_{\rm free}=B_{\rm free}A_{\rm free}/(N)_3
\ge \frac{d^3 V^2}{80}\frac{V^2}{V^3}
=d^3V/80\ge s^6/80.
\]
Therefore at least ONE legal globally injected full original line map g extending the GIVEN pins achieves \(R_{\rm free}\ge s^6/80\), hence \(R_{\rm GOOD}(f,g)\ge s^6/80\). This completes BD-1. No per-Q independent mapping has been sampled.

## Exact variance envelope and global all-h bound

#563 established the zero/one/two/three shared original LINE ID global permutation second moment. Removing source events touching pins can only DECREASE influence maxima:
\(M_1\le5d^3t^2,\ M_2\le8d^3t,\ M_3\le6d^3\).
Set
\[
B_*=\frac98d(d-1)(d-2)V^2-5kd^3t^2,\quad
A_*=\frac94V^2-6kt^2,\quad N=V-k,
\]
\[
p_*=\frac{A_*}{(N)_3},\quad q_N=\frac{(N-3)_3}{(N)_3},\
P_{1,N}=\frac{4t^4}{(N-1)_4},\
P_{2,N}=\frac{16Nt^3}{(N)_4}.
\]
Then the explicit EXACT rational certificate is
\[
\boxed{\eta_{s,k}=q_N^{-1}-1+
\frac{15d^3t^2P_{1,N}}{B_*p_*^2}+
\frac{24d^3tP_{2,N}}{B_*p_*^2}+
\frac{6d^3}{B_*p_*}.}\tag{BD-V}
\]

For h>=5 and k<=V/10: \(B_*\ge d^3V^2/80,\ p_*\ge1/V,\ N\ge9V/10,\ V\ge33825\). Consequently \(q_N^{-1}-1\le60/V\), \((N-j)\ge V/4\) for j=1..5, \(t^2<2V,\ t<2\sqrt V\),
\[
P_{1,N}\le4096/V^2,\quad
P_{2,N}\le8192/V^{3/2},\
M_1/B_*\le800/V,\
M_2/B_*\le1280/V^{3/2},\
M_3/B_*\le480/V^2.
\]
Substitution yields the fully explicit uniform all-h bound:
\[
\eta_{s,k}\le
[60+3(800)(4096)+3(1280)(8192)+480]/V
=41\,288\,220/V<50\,000\,000/V.
\]
Chebyshev at half the certified mean gives BD-2. This bound is conservatively large and may be vacuous at s=32; no nonvacuous finite-h success probability is asserted when the right-hand side >=1.

## Independent falsification and strict scientific scope

New versioned module/tests/proof/hosted workflow add: exact rational polynomial identity checked independently at all h=5..35,40,48,64,80 for k=0,1,floor(V/10); genuine physical K261 s=32 complete occupied supports with missing pair edges **clustered at a high degree coordinate** versus **spread across a matching**, separately subjected to concentrated, strided and coordinate-ranked frozen 10%-edge subsets; direct independent degree-product oracle for physical ordered CLEAN port triples, with independent #560/561 energy verification; genuine original symplectic W32 S68/S72/lex/reverse, and W34 GF4 lex/random partial original source LINE-ID assignments and nononto K14 support, retaining original FULL-support BAD coordinate set. W32/W34 are finite falsifiers, NOT falsely claimed to meet the h>=5 lower gate. Tests reject incorrect dyadic domain, fractional/negative/excessive k, and never claim root A/B/C.

**Scientific boundary and prior work:** The graph-degree calculation, a global permutation mean, source influence deletion and Chebyshev are standard combinatorial tools; do not assert independent novelty for these. #547/#548 already offer five-swap repairs of a DIFFERENT six-original-ID D6 motif (altering given full g). #544 already has an O(s^-3) stochastic bound on a different selected D6 sixflag variable. The new contribution is a precisely proved adversarial **one-tenth original source LINE map locking** theorem using the full-support physical CLEAN energy 9V²/8, for a THREE ORIGINAL flag variable.

**ROOT #230 REMAINS OPEN:** Neither ALL fully fixed original g (k=V) GOOD wedge lower nor selected historical positive seven-GF(5) six-original-ID lower nor residual true-original 3×3 Hall lift is proved. This is not an R3/ASET exponent. Independently review parent #561/#562/#563/#564 proof assumptions before accepting a child; exact HEAD dedicated, INDEX, Proof Audit, Research SUCCESS and a separate mathematical referee remain integration gates. Do not merge scientific Draft simply because its CI passes.

**Next most consequential step:** jointly exploit original source-incidence tensor and BOTH fixed physical pair labelings to approach fully pinned maps, or rigorously exhibit a fixed-g anti-alignment obstruction; separately perform original residual 3×3 Hall → accepted selected six-ID seven-GF5 lift. A partial-map existence theorem cannot be silently promoted to all-(f,g) deterministic root A.
