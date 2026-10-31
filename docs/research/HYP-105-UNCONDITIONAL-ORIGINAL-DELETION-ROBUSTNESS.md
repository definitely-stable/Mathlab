# HYP-105 #230 — AA4-UDEL: unconditional original-six-ID deletion-robust universal sextic obstruction

**Status:** New quantitative all-\(h\) strengthening of scientific Drafts [#672](https://github.com/definitely-stable/Mathlab/pull/672) and [#673](https://github.com/definitely-stable/Mathlab/pull/673), requiring their cited balanced C6 supersaturation theorem and original-source combinatorial lemmas. The root assertion Branch A is *already claimed* in #672, NOT newly claimed here; this slice strengthens it to arbitrary positive-density deletion of ORIGINAL incidence IDs without any low-D6 premise. **Scientific Draft only, not externally refereed/accepted; root #230 remains OPEN_WITH_FORMAL_BLOCKER pending mathematical acceptance.** All estimates count six different ORIGINAL W(3,s) source incidences and use one fixed fully correlated f,g throughout. No full R3 identity, new ASET power, or arbitrary host extension.

## 1. Main theorem: arbitrary original-ID deletions with no D6 restriction

Let \(s=2^h\), \(V=(s+1)(s^2+1)\), \(N=(s+1)V\), and let \(f,g\) be **ANY** allowed complete separately globally injective typed coordinate-pair maps on true symplectic \(W(3,s)\), with arbitrary correlation. Let \(Z\subseteq E_{\rm orig}(W(3,s))\) be **ANY** set of genuine ORIGINAL point–line incidence flags, possibly determined by the complete maps. Define \(D_Z\) to count historically accepted ORIGINAL \(D6\) sixsets with NONE of their six original flag IDs in \(Z\), and \(B_Z\) similarly for the positive original \(B/B\)-overlap class. Both are **full source-class counts**, not physical cycles assigned arbitrary weights.

Assume fixed positive balanced six-cycle supersaturation constants \(C_{\rm graph},c_{\rm graph}>0\) satisfying the established graph theorem in [#659](HYP-105-FULL-PHYSICAL-DEGREE-TAIL.md), normalized without loss by \(C_{\rm graph}\ge1\) and \(0<c_{\rm graph}\le1\).

Define EXACT constants:
\[
\begin{gathered}
\epsilon=\frac18,\quad K=64,\quad
T=2^{65}C_{\rm graph}^{3},\\
\sigma_2^{-1}=64(K+1)^2,\quad
\sigma_3^{-1}=64\cdot27(K+1)^3,\\
L_6=24+576T^2,\quad M_3^2=\sigma_3^{-2}L_6,\\
\boxed{\rho=\min\Bigl\{\frac1{32},\,\frac{1}{768M_3^2}\Bigr\}>0},
\qquad
\boxed{\delta=\min\Bigl\{\frac1{16},\,\frac{c_{\rm graph}}{2^{120}}\Bigr\}>0}.
\end{gathered}
\]
Set
\[
\begin{gathered}
L_E^+=200\sigma_3^{-1}T,\quad
L_4^+=140\sigma_2^{-2}+56,\quad
L_B^+=24\lceil\sqrt{L_4^+}\rceil T^2,\\
s_0=\max\{64,1008T,(12L_E^+)^2,(48L_B^+)^8\}.
\end{gathered}
\]
All constants are finite, explicit and independent of \(s,f,g,Z\), although intentionally enormous. The square root ceiling in \(L_B^+\) is computed EXACTLY with integer square roots; no floating-point asymptotic argument is needed. The external graph theorem constants are INPUTS to this conditional proof, **not numerically known to equal 1**.

**Theorem AA4-UDEL (quantitative all-map positive-density ORIGINAL deletion):** For every dyadic \(s\ge s_0\), every valid complete correlated f,g, and **every map-dependent original incidence deletion set** \(Z\) with \(|Z|\le\rho s^4\),
\[
\boxed{\qquad D_Z+B_Z\ge\delta s^6.\qquad}\tag{UDEL}
\]
The family is counted on exactly the same genuine source after deleting Z, never by remapping labels or replacing original flags with a sampled/synthetic host.

Consequently a maximum pairwise-original-ID-disjoint packing of the union of accepted ORIGINAL D6 and B/B-overlap sixsets has cardinality
\[
\boxed{\quad \nu_{\rm source}> \frac{\rho}{6}s^4\quad}\tag{PACK}
\]
for every sufficiently large dyadic s and every allowed complete f,g. Indeed, any maximal packing \(\nu\) has a hitting set consisting of its \(6\nu\) original IDs. If \(6\nu\le\rho s^4\), (UDEL) produces an accepted sixset avoiding that hitting set, contradicting maximality. This is a packing in ACTUAL ORIGINAL incidence IDs, **not** a physical edge/coordinate support packing or assertion of disjoint f,g images.

## 2. The genuinely new lemma: robust full-physical-degree tail under arbitrary deletions

Build the FULL source-backed physical graph H on \([a]^2\) from BOTH diagonals of every original flag, with \(a=\min\{t:\binom t2\ge V\}\). It has \(2N\) distinct physical edges, each with a **unique ORIGINAL flag owner**. For the fixed \(T\) above, let
\[
Q_T=\{v:\deg_H(v)>Ts\},\qquad
E_T=|\{uv\in E(H): u\in Q_T\text{ or }v\in Q_T\}|.
\]
The heavy set is defined using the **unpruned full H**, and is never silently recomputed after deletion.

Suppose \(E_T\ge\epsilon s^4\). Removing \(Z\) WHOLE original flags removes at most \(2|Z|\le 2\rho s^4\le\epsilon s^4/2\) physical heavy edges. The surviving physical edges touching the unchanged Q_T number at least \((\epsilon/2)s^4\) and have source owners outside Z. Each surviving genuine original flag owns at most TWO of those edges; hence the owner set \(I_Z\) has
\[
|I_Z|\ge (\epsilon/4)s^4.
\]
This is the exact source provenance step: deleting a flag cannot remove more than its two diagonals, and no surviving heavy edge is reattributed to another flag.

The #659 global ORIGINAL pencil conflict books satisfy \(|E(K_{I_Z})|\le 2C_s\), \(C_s\le(3/2)s^4\), and \(|I_Z|\le N\le 2s^4\). The deterministic Caro–Wei selector has
\[
\alpha(K_{I_Z})\ge
\frac{|I_Z|^2}{4C_s+|I_Z|}
\ge\frac{|I_Z|^2}{8s^4}\ge \frac{\epsilon^2}{128}s^4.
\]
Two coordinate bichromatic cuts retain at least a quarter of this independent source set, **keeping BOTH paired diagonals** of each retained original flag. Thus the resulting properly colored, no-row/column-cherry physical graph G contains at least
\[
\beta s^4,\qquad \beta=\frac{\epsilon^2}{512}
=\frac{(\epsilon/2)^2}{128},
\]
distinct surviving physical HEAVY WITNESS edges touching Q_T. All retained original flags avoid Z. We may now repeat exactly the **balanced-chunk argument** in #659 Section 5: partition the opposite bipartition into chunks of size at most \(|Q_T\cap X|\); one ordinary chunk graph has average degree at least \(\beta s/32\) and at most \(32s^3/T\) vertices. The external balanced graph theorem applies provided
\[
 T\ge 2^{20}C_{\rm graph}^3\beta^{-3}
  = 2^{47}C_{\rm graph}^3\epsilon^{-6}
  = 2^{65}C_{\rm graph}^3.
\]
Every resulting simple physical C6 belongs to this coherent graph G with all its ORIGINAL source flags outside Z; the established original rainbow physical-C6 \(\leftrightarrow D6\) bijection holds unchanged. Therefore
\[
\boxed{
 E_T\ge\epsilon s^4,\ |Z|\le\rho s^4
 \Longrightarrow
 D_Z\ge c_{\rm graph}\,\frac{\epsilon^{12}}{2^{84}}s^6
       =c_{\rm graph}\,2^{-120}s^6\ge\delta s^6.
 }\tag{ROBUST-TAIL}
\]
This is NOT an application of #659 to the **new degree threshold** of the pruned graph. It is a source-ID-preserving re-run of its proof on the surviving original heavy witness IDs measured with the OLD full-H Q_T. The non-obvious difference between an original full heavy tail and the pruned graph's tail is dealt with explicitly.

## 3. The complementary low-tail case without any assumption on UNPRUNED D6

Now assume \(E_T<\epsilon s^4=s^4/8\). Form a paired physical core \(H_0\) by deleting (i) whole original flags with a diagonal touching the original full-H \(Q_T\), (ii) whole flags whose degree exceeds K in the original full source conflict graph, and (iii) **all** original IDs in Z. The first removal loses at most \(E_T\) flags, the second at most \(4C_s/K\le3s^4/32\), and the third at most \(\rho s^4\le s^4/32\); overlap of the deletion populations only helps.

As \(N\ge s^4\), the number of retained ORIGINAL flags obeys
\[
 N_0\ge
 (1-\tfrac18-\tfrac3{32}-\tfrac1{32})s^4
 =\tfrac34s^4;
\quad m_0=2N_0\ge s^4.
\]
The same source proof as in #672 supplies full physical degree \(\Delta(H_0)\le Ts\), source conflict max degree \(\le K\), and original pencil populations \(\le K+1\). We have kept **both physical diagonals** of every retained flag and deleted ALL flags in Z. Projection anchor flags q--ell--p--r, when reconstructing source motifs, may still lie **outside H0** but must avoid Z.

Apply #672's selector to this Z-free core. Since every selected original flag lies outside Z, **every simple C6 in every selector outcome is a genuine original D6 SIXSET avoiding Z**. Hence the correct pointwise charging bound is
\[
 C_6(G)\le D_Z,
\]
NOT the possibly enormous full \(D6(f,g)\). If \(D_Z\ge\delta s^6\), (UDEL) is already proved. Assume \(D_Z<\delta s^6\le s^6\). In that case #672 Sections 3–6 apply *literally to the new source-deleted core*, yielding:
\[
\begin{aligned}
\operatorname{tr}(A_G^6)&\le L_6s^6,\\
\|P_3\|_F&\le \sigma_3^{-1}\sqrt{L_6}\,s^3=M_3s^3,\\
\operatorname{tr}(A_0^4)&\le L_4s^5,
\quad L_4=2\sigma_2^{-2}\sqrt{8L_6}+56T,
\end{aligned}
\]
and the exact original-source full/core mixed-blocking transfer
\[
U_{B/B\text{-overlap}}\ \ge\
\frac14s^6-42Ts^5
-\frac{L_E}{2}s^{11/2}
-2\sqrt{B_0TL_4}\,s^{47/8},\quad
L_E=8\sigma_3^{-1}\sqrt{L_6},\
B_0=64\sqrt{(K+1)T}.
\]
Here this displayed count is the *pre-Z-anchor-mask source reconstruction*; its three path flags already avoid Z. The all-h path computations and mixed internal blocked-triple bound only require genuine source spectra/books, source conflict cap K, physical degree cap T, and the coherent selected graph's sixth moment; all still hold after deletion.

Our purely integer constants give the pointwise upper envelopes \(L_E\le L_E^+\), \(L_4\le L_4^+ T\), \(\sqrt{B_0TL_4}\le L_B^+\), for every \(T\ge1\). The explicit \(s_0\) ensures each of the three displayed errors is at most \(s^6/24\), so at least \(s^6/4\) suitable UNBLOCKED DIRECTED physical three-paths remain before excluding projection anchors in Z.

[#673](HYP-105-BBO-RESILIENCE-STABILITY.md) proves every original flag occurs in exactly \(s^2\) original nonincident source projections **in each of three path positions**. Thus at most \(3s^2|Z|\) typed nonincident source endpoint pairs have a projection anchor in Z, and at most \(12s^2|Z|\) ORDERED physical endpoint pairs. Weighted Cauchy (with \(\|P_3\|_F\le M_3 s^3\)) bounds the mass of proper core paths on such endpoints by
\[
 M_Z\le \sqrt{12s^2|Z|}\,M_3s^3
       \le\sqrt{12\rho}\,M_3s^6
       \le s^6/8.
\]
The final inequality follows from \(\rho\le1/(768M_3^2)\). Removing these paths eliminates ALL THREE projected anchor flags in Z. The three actual physical path flags were already in the Z-free core. Therefore at least \(s^6/8\) unblocked directed physical paths generate genuine accepted historical ORIGINAL B/B-overlap SIXSETS with **all six original IDs outside Z**. As in #672, every such sixset has at most two directed source-backed path representations:
\[
 \boxed{B_Z\ge s^6/16\ge\delta s^6.}\tag{ROBUST-LOW-TAIL}
\]

Together ROBUST-TAIL and ROBUST-LOW-TAIL establish (UDEL) *without any premise on the unpruned full-map D6 count*.

## 4. Asymptotic upgrade of #673: low *SURVIVING* D6 suffices

The original stability in [#673](HYP-105-BBO-RESILIENCE-STABILITY.md) assumes \(D6(f_s,g_s)=o(s^6)\) BEFORE deleting flags. That is stronger than needed.

Fix ANY sequence of legal complete correlated maps, any arbitrary \(Z_s\) with \(|Z_s|=o(s^4)\), and assume only
\[
 D_{Z_s}=o(s^6)
\]
for the D6 count that survives all source deletions. For ANY fixed \(\eta>0\), choose a fixed heavy-tail threshold
\(T_\eta\ge2^{47}C_{\rm graph}^3\eta^{-6}\). Eventually \(2|Z_s|\le\eta s^4/2\). If full-H heavy-edge mass were at least \(\eta s^4\) infinitely often, the ROBUST-TAIL argument with epsilon=\(\eta\) would force
\[
 D_{Z_s}\ge c_{\rm graph}\eta^{12}s^6/2^{84},
\]
contradicting \(D_{Z_s}=o(s^6)\). Therefore **for every fixed \(\eta>0\)**, full-H heavy-edge mass at that fixed \(T_\eta\) is below \(\eta s^4\) eventually.

Choose also a FIXED original conflict cap \(K_\eta\) so large that at most \(\eta s^4\) flags are removed, and delete Z. The new Z-free original core has
\(N_0\ge(1-2\eta-o(1))s^4\), with both caps fixed while \(s\to\infty\). Its physical directed 3-walk floor, using \(a^2=(2+o(1))s^3\), is
\[
 \frac{(4N_0)^3}{a^4}
       \ge(16(1-2\eta)^3-o(1))s^6.
\]
All #672 degree-return, exceptional-endpoint and mixed internal-blocking errors are **o(s^6)** with these FIXED caps and the selected graph moment charged to **SURVIVING D_{Z_s}=o(s^6)**. The #673 source-projection Z-mask costs \(\sqrt{12}s^3M(T_\eta,K_\eta)\sqrt{|Z_s|s^2}=o(s^6)\), since \(|Z_s|=o(s^4)\). Divide by the at-most-two directed paths per genuine original B/B-overlap sixset:
\[
 \liminf_{s\to\infty}\frac{B_{Z_s}}{s^6}
 \ge8(1-2\eta)^3.
\]
Finally send \(\eta\downarrow0\) **after** the liminf, keeping caps fixed during each s-limit:
\[
\boxed{\qquad
 |Z_s|=o(s^4),\ \ D_{Z_s}=o(s^6)
 \quad\Longrightarrow\quad
 \liminf_{s\to\infty}B_{Z_s}/s^6\ge8.
 \qquad}\tag{SURVIVING-D6-STABILITY}
\]

This strictly extends #673's original assumption on **unpruned** D6. It is a quantitative robust compensation theorem for the same fixed completed maps, not a random-completion first-moment estimate, although it remains conditional on the asymptotic smallness of surviving D6 for the sharper coefficient.

## 5. Independent reproducibility and claim limits

The code \`research/hyp105_unconditional_original_deletion.py\` implements exact integer/Fraction arithmetic for every sufficient constant and bound (formal normalizations \(C_{\rm graph},c_{\rm graph}\) are supplied, **not fitted or numerically asserted by tests**). Finite original-source verifier independently visits genuine physical C6 in true W32/W34 AFTER deleting original flags, checks the historical ORIGINAL D6 GF5 classifier and uniqueness of its six original flag IDs, and combines that family with the separately implemented [#673](../research/hyp105_bbo_resilience.py) original source B/B-overlap core-path oracle. A surviving D6 and a surviving B/B-overlap source sixset can never coincide by their distinct historical accepted source factor partitions.

The independent regression \`research/test_hyp105_unconditional_original_deletion.py\` checks:
- exact symbolic normalizations (T, delta, rho and upper moment envelopes), and reject illegal graph theorem constant inputs;
- COMPLETE genuine original W32 lex and reverse-line historical seven-class census (including source ID deletions), independently confirming our D6_avoid and containment of BBo source-path subfamily inside the original historical B/B-overlap count;
- true original W34 finite arbitrary-source-ID deletions (including sparse core with source anchors outside the path core), and the unchanged historical GF5 accepted-class witnesses;
- direct physical heavy witness edge accounting on genuine W32/W34 before and after removing an ORIGINAL flag set: heavy Q_T must be defined on the FULL H, and at most TWO heavy edges are removed per original flag; the surviving heavy original owner set is independent of the pruning convention;
- no claim that these small W32/W34 instances reach the astronomical s0 or verify graph SS6 coefficients.

Hosted CI uses Python 3.12 and GitHub-hosted runners only. Scientific Draft must receive independent external mathematical referee and root #230 acceptance review. No silent merge, issue closure or ASET exponent.

**Dependency scope:** #659's balanced graph six-cycle supersaturation + original source collision-book lemma; #652's physical cycle to original D6 bijection; #672's source path-preserving selector, moment transfer, mixed full/core source blocking and original B/B-overlap bridge; #673's exact original projection exposure and anchor avoidance. This new theorem does NOT assume independent random physical f or g, does NOT require low unpruned D6, and does NOT strengthen the underlying graph SS6 theorem itself.
