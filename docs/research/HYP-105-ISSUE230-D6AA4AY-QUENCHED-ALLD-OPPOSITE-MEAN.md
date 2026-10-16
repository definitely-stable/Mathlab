# HYP-105 / issue #230 — AA4-AY: exact quenched source-original ALL-D opposite-port wedge mean, uniform ≥s⁶/2

**STRICT partial stochastic theorem.** Research Draft child of parallel true-original mixed-cell [PR #559](https://github.com/definitely-stable/Mathlab/pull/559), pinned parent exact HEAD 8bbb39eac461d673c64cab75a343f24f591ddddf. Source geometry is the real symplectic W(3,2^h), ALL h>=1; every counted three-source-flag event uses three distinct ACTUAL original incidence IDs and three different original point factor and original line factor IDs. Fixed complete point map f and right globally occupied physical edge image set E_g may be fully adversarial and correlated with the original GQ. Only ONE entire globally coherent original LINE factor image bijection is uniformly sampled; no per-six-ID rerandomization or fake high-order source geometry. Root #230 Branch A/B/C remains OPEN_WITH_FORMAL_BLOCKER.

**Important distinction:** This theorem concerns all original bilateral D source flag pairs and their **physical point+line opposite-port centered THREE-source-flag wedges**, R_ALL, previously defined exactly by the coupled source corrected tensor in #554. It does NOT concern the stricter globally GOOD physical port filtered subset, and does NOT prove any accepted historical seven-positive-GF5 SIX distinct-original-incidence-ID motif lower at fixed adversarial original g. Prior #544 already proved stronger stochastic abundance of genuine selected D6 under a different event; we claim neither precedence nor replacement of that result. New contribution here is the independently factored **point-side true-source original triple capacity times global fixed-right-support edge energy**, an explicit universal s⁶/2 quantitative bridge to #559's missing physical opposite-port structure in a distinct stochastic quantifier.

## 1. Exact original SOURCE point-opposite threeflag potential (fixed f)

Fix s=2^h>=2, d=s+1, V=(s+1)(s²+1), physical coordinate alphabet a minimal with K=binom(a,2)>=V and m=K−V<=a−2. Original source incidence set I={(p,l):p∈l} has exactly Vd different flags. Choose ANY full globally injected actual original point physical pair edge map f:P(W(3,s))→E(K_a), with im(f)=E_f of size V.

For each actual original incidence center i=(p,l), write its physical point image f(p)={u,v}. Define the **two disjoint real original point factor port neighbors**

P_u(p)={q≠p:u∈f(q)}, P_v(p)={q≠p:v∈f(q)}.

They are disjoint because one entire f is injected and the ONLY physical edge with both u and v already belongs to p. Define the **true original source-only** candidate count at center i:

\[
B_i(f)=\sum_{\substack{q_0\in P_u(p)\\q_1\in P_v(p)}}
\#\{(k_0,k_1):q_0\in k_0,\ q_1\in k_1,\
k_0\ne l,\ k_1\ne l,\ k_0\ne k_1\}.
\]

These are all ACTUAL genuine original three-flag tuples
(i=(p,l),j_0=(q_0,k_0),j_1=(q_1,k_1)); all three original POINT factor IDs and all three LINE factor IDs different, both physical left point ports opposite. One shared original f is used, source neighborhoods determined solely by true incidence W(3,s), NOT by physical label sampling. Put B(f)=Σ_{i∈I} B_i(f). For all q0,q1, each has d genuine incident original lines; exclude at most center l and one extra k0 from q1. Therefore

\[
B_i(f)\ge (d-1)(d-2)\, |P_u(p)|\, |P_v(p)|.
\]

Sum over the actual d center original line neighbors of every original point p:

\[
\boxed{B(f)\ge d(d-1)(d-2) T(E_f),}
\]
where for ANY occupied physical pair image support E⊂E(K_a),

\[
\boxed{T(E)=\sum_{\{u,v\}\in E}
(\deg_E u-1)(\deg_E v-1).}
\]

No independence or hidden duplicate original incidence IDs is used; every q0 belongs to one port, every q1 to the other, and k0≠k1 ensures true original SOURCE A/A triple.

## 2. EXACT right complete-global quenched permutation average

Fix any adversarial occupied physical right support E_right⊂E(K_a) of exactly V edges. Let g be ONE uniformly chosen *complete bijection* from ALL V ACTUAL original LINE factor IDs to this SAME set E_right. For any three distinct actual original LINE IDs (l,k0,k1), their ordered physical images (g(l),g(k0),g(k1)) are uniformly distributed over all V(V−1)(V−2) ordered triples of DISTINCT physical occupied right pair edges. These distinct original line images are NOT sampled independently, and the SAME random g is shared by ALL original source triple events.

Conditioning on the original center right edge g(l)=e={x,y}∈E_right, write r_x=deg_{E_right}(x)−1, r_y=deg_{E_right}(y)−1. Exactly 2r_xr_y ordered choices of the other two image edges intersect e in its TWO OPPOSITE physical line coordinate endpoints (one at x, one at y); the edge e itself is excluded from both. Because the physical graph is simple, those candidate two edge images cannot coincide. Consequently the exact probability for every prescribed point-opposite actual three-original-flag source event is

\[
p(E_{\rm right})=
\frac{2T(E_{\rm right})}{V(V-1)(V-2)}.
\]

By linearity of expectation, WITHOUT inter-event independence,

\[
\boxed{
\mathbb E_{g:\,I_{\rm LINE}\xrightarrow{\mathrm{bij}}E_{\rm right}}
R_{\rm ALL}(f,g)
=
\frac{2B(f)T(E_{\rm right})}{V(V-1)(V-2)}.
}
\]

Here \(R_{\rm ALL}\) is the number of actual true-original centered three-flag wedges with physical opposite ports in BOTH point and line projections. It equals the previously known exact coupled source incidence four-cell transport sum Σ_i(X00X11+X01X10) of #554. This exact factorization is a NEW source-point/physical-right-support specialized computation, not an all-fixed-(f,g) deterministic GF5 theorem. The initial original g used to describe E_right can be adversarial: the formula only uses its IMAGE support and ignores its placement, as required by uniform complete-permutation averaging.

## 3. Uniform adversarial support extremal port-edge energy and s⁶/2 bound

For ANY E⊂E(K_a) occupied edge set of size V=K−m with 0<=m<=a−2, let m_x be the number of missing edges incident to coordinate x. Each occupied edge e={x,y} has deg_E(x)−1=(a−2)−m_x and similarly for y. Expand its product and sum over all occupied e. The positive m_xm_y terms may be discarded and

Σ_{e={x,y}∈E}(m_x+m_y)=Σ_x m_x deg_E(x)≤(a−1)Σ_x m_x=2m(a−1).

Therefore uniformly in the missing physical edge pattern:

\[
\boxed{
T(E)\ge L=V(a-2)^2-2m(a-1)(a-2)>0.
}
\]

Both original physical supports E_f and E_right have exactly this same size V, but may have COMPLETELY unrelated holes; no physical gauge or GQ automorphism of arbitrary f,g is assumed.

Combining with exact mean yields the unconditional quantified STOCHASTIC mean:

\[
\boxed{
\mathbb E_g R_{\rm ALL}(f,g)\ge
\frac{2d(d-1)(d-2)L^2}{V(V-1)(V-2)}
\ge\frac12s^6
\qquad\text{for every dyadic }s\ge2,
}
\]

uniform over EVERY fully globally injected ORIGINAL fixed point map f and EVERY physical right support E_right.

**All-h arithmetic proof:** For s=2 the actual palette (V,a,m)=(15,6,0) and L=240, so exact right-hand bound exceeds s⁶/2=32. For all s>=4, a>=14, minimal palette implies V>= (a−1)(a−2)/2+1>=4(a−1), and (a−2)²>=K>=V, whence \(L=(a−2)^2 V−2m(a−1)(a−2)\ge(a−2)^2(V−2(a−1))\ge V²/2\). Therefore the exact stochastic mean is at least
\( \frac12 d(d-1)(d-2) V^4/[V(V-1)(V-2)]\ge\frac12 d(d-1)(d-2)V\).
For d=s+1, V=(s+1)(s²+1), the elementary integer expansion
\((s+1)^2(s-1)(s²+1)=s^5+s^4-s^3+s^2-s-1\ge s^5\) for s>=2 proves this is ≥s⁶/2. No fake large W3 source construction or W32 asymptotic extrapolation.

In fact the exact symbolic lower ratio approaches 8s⁶, but **we only formally promote the clean uniform 1/2 constant** without confusing the expected random map with EVERY adversarial fixed original g.

## 4. Independent source and physical falsifiers

Four additive research artifacts: source module, independent eight-group tests, this proof and two-job hosted exact-HEAD workflow.

- Actual ORIGINAL symplectic W32 S68/S72/lex/reverse and W34 GF4 lex/random POINT physical injections, true 45 and 425 unique original incidence flags: compute B(f) via direct actual source neighborhood factorization, and a **different independent literal original three-flag source tuple enumeration** for every actual center i. All original factor IDs p0,p1,p2 and l0,l1,l2 verified distinct; global right images not touched.
- For each complete original W32 right image support K6, enumerate ALL V(V−1)(V−2)=2730 ordered distinct occupied right physical edge triples and independently count opposite right port cases. Likewise for true ORIGINAL W34 with nononto right K14 physical support, enumerate ALL 85×84×83=592,620 ordered triples and compare exact rational p_right with derived 2T/[V(V−1)(V−2)]. This checks actual sampling *without replacement* across THREE different original LINE IDs, not a spurious independence model.
- For genuine actual original W32 and W34 full global f,g (including adversarial K14 incomplete original W34 random physical image), independently LITERALLY enumerate all source threeflag physical opposite wedge configurations at the original FIXED g and check equality to the preexisting independent corrected original source mixed \`FᵀBG−BG−FᵀB+1\` physical four-bin tensor oracle #554. This validates exact event semantics, not the stochastic proof just on its own formulas.
- Exact symbolic integer dyadic all-h h1..35,40,48,64,80, and incomplete/adversarial missing physical edge patterns including pendant-star at the minimum allowed edge palette. No fabricated large original W3 model, no hand-generated source incidences. Real actual typed physical right gauge relabel and entire ORIGINAL source LINE factor exchange invariance of the quenched expected value.
- Negative non-global-injection, nonunique source incidence and nondyadic input controls. No model-equivalent Branch C is claimed.

## 5. Prior art, scientific meaning and strict nonimplications

The random-permutation triple marginal and linearity-of-expectation tools are elementary, and earlier project PR #544 already proved genuine selected D6 stochastic abundance under globally uniform right maps (and fixed both physical occupied supports); #554 first gave the TRUE source-corrected physical opposite-port ALL-D tensor; #556/#557 provided deterministic *GOOD-only* sharp port minority transfer; #559 gave SOURCE physical transport port forcing and scalar no-lift. The novelty here is **exact original point-only source three-flag potential B(f), its global right-image-support edge-energy factorization, and the all-h support-uniform spectral-free s⁶/2 stochastic bound for the broader physically opposite ALL-D THREE-FLAG variable**. Publication novelty against external graph theory prior art has not been fully independently checked; no broad novel general random-permutation theorem claim is made.

The new mean directly identifies a clean positive-density physical opposite source-threeflag bridge for ANY original fixed f under UNIFORM global right g, but **does not** imply R_GOOD≥cs⁶ for every adversarial fixed g, a source residual 3×3 forest Hall six-flag extension, an original six-ID selected positive seven GF5 minimum, full R3 / ASET exponent, root Branch A/B/C, or a counterexample to it. The exact right permutation mean can coexist with rare exceptional adversarial label maps. Never promote expected value to the given adversarial map or pretend physical ALL-D means GOOD-only.

Independent mathematical referee, final exact-HEAD Dedicated, INDEX, Proof Audit, Full Research and PR ancestry gates are separate from mathematical author proof. Leave Research Draft UNMERGED; main unchanged, root #230 OPEN_WITH_FORMAL_BLOCKER. Next truly deterministic blocker: show that GOOD physical two-type port minority products share positive support for EVERY fully fixed original f,g, or construct a mathematically genuine all-h correlated global small-S family. The separately selected original residual physical T/P, 3×3 forest Hall, and seven GF5 acceptance remain an independent second bottleneck.


## 6. First exact-hosted genuine original fixed-g versus ONE-global-right-permutation mean evidence

The initial [GitHub-hosted specialized run #38883195618](https://github.com/definitely-stable/Mathlab/actions/runs/38883195618) completed BOTH dedicated jobs **SUCCESS**, independent eight original math tests. Its previous source HEAD first failed an import from an unrelated scientific branch; that issue was corrected with a standalone exact integer minimal K_a palette calculator. This was a repository dependency failure, not evidence against the theorem. The final research HEAD further freezes **all five exact actual-source numbers** as regression assertions, including a ninth independent test, and requires a NEW exact-HEAD CI run before scientific acceptance.

| Genuine full original source f,g | Actually FIXED adversarial original g: literal R_ALL(f,g) | Exact mean E over ONE uniformly random complete global original right LINE map with SAME support E_g | All-support uniform symbolic floor |
|---|---:|---:|---:|
| W32 S68 | 697 | 87056/91 ≈956.66 | 23040/91 ≈253.19 |
| W32 S72 | 750 | 87056/91 ≈956.66 | 23040/91 |
| W32 lex | 1105 | 88992/91 ≈977.93 | 23040/91 |
| W34 lex (K14 with 6 missing edges) | 49,742 | 471930840/9877 ≈47,782.6 | 214990848/9877 ≈21,766 |
| W34 random (K14 with 6 missing edges) | 46,996 | 131596825/2822 ≈46,632.5 | 214990848/9877 |

These rational mean formulas are computed from independently enumerated ORIGINAL true-source point-opposite threeflag counts and ALL V(V−1)(V−2) physical ordered right triplets, not experimental sampling. The actual fixed-g real original threeflag ALL-D physically opposite counts are INDEPENDENT literal true-source triple enumerations compared against the upstream #554 full \(F^\top BG-BG-F^\top B+1\) original source-corrected four-port physical tensor. Note that W34 random can have a low **GOOD-filtered** opposite-wedge count 10 while its ALL-D opposite count is 46,996: they are DIFFERENT event families. No GOOD-only lower is inferred from this ALL-D mean.

This evidence explicitly separates three different quantities: an individual adversarial given global g (which can be above or below the quenched mean), the quenched mean over **whole global** original line assignments, and a universal support-only lower on that MEAN. Neither the average nor an existence statement for some other g implies the desired lower for EVERY given g. No finite S2/S4 observation is passed off as an original all-h proof.
