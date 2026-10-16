# HYP-105 / issue #230 — AA4-AQ: one-adversarial-global-map original D6 conditional mean

**Research-only theorem, genuine symplectic ORIGINAL W(3,s), all dyadic powers, no solution of root Branch A/B/C.** Strict Draft child of [AA4-AP #537](https://github.com/definitely-stable/Mathlab/pull/537), parent pinned exact HEAD \`92c824a3d2c10f5780a452a0fb3632d1f67fe995\`.

## 1. Scientific contribution and old work

[AA4-AA #504](https://github.com/definitely-stable/Mathlab/pull/504) already proved the EXACT mean of all seven GF(5) selected classes under **two independent uniformly randomized complete global factor maps** f and g, with \(\mathbb E S_s=(1070/3+o(1))s^6\). Its D6 contribution is an ordinary double-global random-map mean of a source A/A six-matching. This result is **not relabeled** a new unconditional deterministic bound here.

[AA4-AP #537](https://github.com/definitely-stable/Mathlab/pull/537) already gave the exact **fixed** two-map, true original D6 source four-neighbor oriented P5×P5 Boolean acceptance kernel, and true W32 S68/S72 fixed two-map examples with **D6=ZERO**. [AA4-AO #535](https://github.com/definitely-stable/Mathlab/pull/535) and [AA4-AP #538](https://github.com/definitely-stable/Mathlab/pull/538) separately prove robust physical port occupancy and uniform many good true-original D anchor pairs, WITHOUT true original Hall-positive GF5 transfer.

**NEW AA4-AQ** is an intermediate **QUENCHED / ONE-GLOBAL-MAP-ADVERSARIAL** theorem:
- The ORIGINAL point-factor physical map f is arbitrary and FIXED;
- The occupied physical line-edge image \(E_g=\mathrm{im}(g)\subset E(K_a)\) is arbitrary and FIXED, including all holes;
- Only the assignments of those same occupied line physical edges to the ORIGINAL line source-factor IDs are permuted by ONE uniformly chosen permutation \(\pi\in S_V\); the resulting full global \(g_\pi\) is held fixed for ALL ORIGINAL source incidence Q simultaneously.
- The exact conditional mean \(\mathbb E_\pi S_{\rm D6}(f,g_\pi)\) has an explicit formula, a universal positive \(\Omega(s^6)\) bound for **EVERY** such f and occupied g-image, and in fact a UNIFORM leading constant \((16/3+o(1))s^6\) as \(h\to\infty\).

This is strictly stronger in adversarial quantifiers than randomizing BOTH global typed maps, but strictly weaker than the root HYP-105 requirement **FOR EVERY fixed pair f,g**. It is a theorem of the original incidence geometry + nearly complete physical label supports + one-sided random global factor correspondence, not an upper bound on a per-source Hall matching count.

## 2. EXACT conditional mean, no independent per-flag resampling

Let genuine symplectic GQ \(W(3,s)\), \(s=2^h\ge2\), have \(V=(s+1)(s^2+1)\) actual ORIGINAL point source factors and V actual ORIGINAL line factors. Its TRUE ORIGINAL incidence graph is \(d=s+1\) regular on both sides, has girth eight (no original C4/C6), and each two different original points share at most one original line neighbor.

Let \(a=\min\{n:\binom n2\ge V\}\), \(K=\binom a2\) and \(m=K-V\le a-2\). Fix ANY global complete injections of source point factors f:P→E(K_a) and line factors g:L→E(K_a), with EXACTLY V distinct images of each typed factor class. Write \(G_f\), \(G_g\) for these simple undirected physical **occupied EDGE SET** graphs. Their edge sets are fixed and almost complete, but which original source factors have these labels is adversarial for f and initially arbitrary for g.

Let \(C_6(G)\) count the UNORIENTED physically simple six-edge six-vertex connected cycles of a physical edge image graph G, each undirected cycle counted ONCE (12 vertex sequences represent one physical undirected C6). Let \(\mathcal Q_f\) be the set of SIX different TRUE ORIGINAL source incidence IDs Q satisfying:
1. its six original source POINT factors are pairwise distinct;
2. its six original source LINE factors are pairwise distinct;
3. the six globally assigned point physical edges f(p) form one connected simple physical C6 with six distinct physical coordinates.

Put \(A_6(f)=|\mathcal Q_f|\). This is an exact original source quantity, not just \(C_6(G_f)\): each physical six-point-factor cycle may support many different selections of six DISTINCT original line neighbors, or theoretically none; the genuine source incidence relation is explicitly used.

A selected six-Q contributes to historical aligned D6 precisely when the physical line edges assigned to its six DISTINCT original line factors have the SAME column-dual connected C6 on its SIX original flag positions as its point-side physical C6. Under one uniformly chosen permutation of the V occupied line physical edges among V original line factors, the six line factors in Q receive a uniform ORDERED tuple of SIX DIFFERENT edges from \(G_g\), denominator \((V)_6=V(V-1)\cdots(V-5)\). Each occupied physical C6 of \(G_g\) supports exactly 12 assignments from its six physical edge labels to these six fixed ordered original line source positions producing the fixed D6 column-dual cycle (the 12 automorphisms of C6). Thus **without** independent flag sampling or original-source geometry randomization:

\[
\boxed{\mathbb E_{\pi\in S_V}S_{\rm D6}(f,g_\pi)
=A_6(f)\frac{12\,C_6(G_g)}{(V)_6}.}
\]

The only expectation is over a SINGLE GLOBAL PERMUTATION of the line-source physical-edge factor assignment, used unchanged over ALL source six-Q. Line image holes stay absent.

By point/line duality the corresponding statement holds for a fixed adversarial global g and a single randomized global point-factor image assignment preserving its physical image edge set.

## 3. NEW AQ-1: genuinely all-global physical C6 lower for arbitrary fixed supports

The complete physical K_a has precisely \((a)_6/12\) undirected simple six-cycles, where \((n)_k=n(n-1)\cdots(n-k+1)\).

Every missing physical unordered pair edge belongs to exactly \((a-2)_4\) undirected physical six-cycles: first select four other physical vertices and count 24 distinct undirected Hamiltonian cycles on those six vertices containing the specified physical edge, giving \(24\binom{a-2}4=(a-2)_4\).

Removing m physical edges from K_a destroys at most \(m(a-2)_4\) six-cycles by the **elementary union bound**. Thus EVERY full globally injected typed original source image graph G with V occupied physical edges obeys:

\[
\boxed{C_6(G)\ge L_6(a,m):=\frac{(a)_6}{12}-m(a-2)_4.}
\]

This is a deterministic **physical** projection statement independent of original GQ source geometry. It is not falsely promoted to original GF5 acceptance when both original f,g fixed. For actual dyadic s=2,4,8,..., the bound is positive; minimum-physical-alphabet m≤a−2, and for a≥35 the ratio to the complete physical K_a C6 count is at least \(2/3\).

Prior-art attribution: cycle deletion union bounds and counting Hamiltonian cycles through a fixed edge are elementary combinatorics. The research content is the quantified nearly-complete ORIGINAL globally assigned physical label support and its combination with actual source geometry and an exact one-sided global permutation expectation.

## 4. NEW AQ-2: original GQ source six-flag injective neighbor lower, NO fake independence

Fix any SIX DIFFERENT genuine ORIGINAL points p0,...,p5. There are exactly d⁶ choices of incident true-original line factors \((\ell_0,\ldots,\ell_5)\in\prod_i N_{\rm GQ}(p_i)\) with no distinctness requirement. For a fixed pair i<j, a collision \(\ell_i=\ell_j\) can occur ONLY when pi,pj share an ORIGINAL line neighbor; genuine W(3,s) admits at most ONE common line for any two distinct original points (GQ source C4-free). Hence the number of six-tuples with a collision at that fixed pair is at most d⁴. Taking a union bound over 15 pairs gives

\[
\boxed{\#\{\text{six pairwise different ORIGINAL incident line factors}\}
\ge d^6-15d^4=d^4(d^2-15)}
\]

for d=s+1≥5, i.e. all s≥4. Every such tuple selects exactly six DISTINCT TRUE ORIGINAL source incidence ID flags and has six distinct point and line sources; no global physical map changes.

For s=2, d=3, the union bound is negative and MUST NOT be applied. Instead the original bipartite d-regular source graph satisfies Hall's theorem: every set of six distinct original points has at least six distinct actual neighboring original lines (\(d|S|\) source incidences cross to at most d per line), so some six-distinct-line-factor matching exists. The implemented all-h theorem uses the valid **at-least-one** source matching bound only for s=2, with no false 2/3 s⁶ claim.

Thus, uniformly over arbitrary fixed f and g-occupied support:

\[
A_6(f)\ge C_6(G_f)\,q_s,\qquad
q_s=\begin{cases}1,&s=2,\\ d^4(d^2-15),&s\ge4.\end{cases}
\]

This is a joint ORIGINAL-source/physical projection theorem. In particular all actual physical cycles under f contribute real original six-incidence matchings, but they may require DIFFERENT line-source labels, and no acceptance under the unchanged adversarial g is inferred.

## 5. NEW AQ-3: uniform conditional genuine ORIGINAL D6 expectation \(\Omega(s^6)\)

Combining the preceding EXACT conditional mean identity with BOTH adversarial fixed physical edge-support cycle lower bounds gives for EVERY \(h\ge1\), every point f, every fixed line occupied support E_g:

\[
\boxed{
\mathbb E_\pi S_{\rm D6}(f,g_\pi)
\ \ge\ \frac{12L_6(a,m)^2\,q_s}{(V)_6}.
}
\]

This is a completely explicit finite rational function, no vague high-probability approximation. For all dyadic s≥4 we moreover prove:

\[
\boxed{
\mathbb E_\pi S_{\rm D6}(f,g_\pi)\ge\frac23s^6.
}
\]

**Proof for s=4:** \(V=85,d=5,a=14,m=6,L_6=108900,q_s=6250\), giving EXACT rational conservative lower
\[
\frac{12\cdot108900^2\cdot6250}{(85)_6}
=\frac{1\,143\,828\,125}{404\,957}
>\frac23\cdot4^6.
\]

**Proof for all s=2^h≥8:** a≥35,d≥9. From m≤a−2, the full-physical C6 deletion fraction obeys
\[
\frac{L_6(a,m)}{(a)_6/12}
=1-\frac{12m}{a(a-1)}
\ge\frac23.
\]
The exact physical falling product satisfies \((a)_6/a^6\ge\prod_{j=1}^5(1-j/35)>3/5\). The genuine original line SDR union bound gives \(q_s/d^6=1-15/d^2\ge22/27\), and \(V\le\binom a2<a^2/2\), so \((V)_6\le V^6<a^{12}/64\). Consequently,
\[
\begin{aligned}
\mathbb E_\pi S_{\rm D6}
&\ge \frac{(a)_6^2}{12(V)_6}\Big(\frac23\Big)^2 d^6\frac{22}{27}\\
&\ge\frac{16}{3}\Big(\frac35\Big)^2\Big(\frac23\Big)^2\frac{22}{27}d^6\\
&=\frac{1408}{2025}d^6
>\frac23 s^6.
\end{aligned}
\]
Every step is a genuine all-h exact integer/Fraction or elementary analytic inequality. The **old combined-uniform-ensemble** result #504 is NOT used to infer the stronger **one-map-fixed** statement.

**Existence corollary by the probabilistic method:** for EVERY fixed complete global point f and EVERY allowed fixed physical occupied line support E_g, there exists at least ONE complete globally injective reassignment \(g_\pi\) of those very same physical line edges to actual original line factor IDs such that \(S_{\rm D6}(f,g_\pi)\ge\lceil\frac23s^6\rceil\) for every dyadic s≥4. This is an EXISTENCE of a **favorable** global assignment, not a claim that ALL adversarial \(g\) attain the bound, nor an efficient constructive algorithm for finding the permutation.

## 6. NEW AQ-4: uniform first-moment leading constant, irrespective of adversarial fixed f and line support

The exact same source/combinatorial counting provides an UPPER for EVERY fixed f and line physical support:

\[
A_6(f)\le \frac{(a)_6}{12}\,d^6,\quad C_6(G_g)\le\frac{(a)_6}{12},
\]

so
\[
\boxed{
\frac{12L_6(a,m)^2\,q_s}{(V)_6}
\ \le\ \mathbb E_\pi S_{\rm D6}(f,g_\pi)\
\le\ \frac{(a)_6^2\,d^6}{12(V)_6}.
}
\]

Uniformly over all global f and occupied g-support, m=O(a), \(a^2/(2V)\to1\), \(d/s\to1\), \(q_s/d^6\to1\), and \((a)_6/a^6\to1\). Both explicit bounds are asymptotic to \((16/3)s^6\), hence the **quenched uniform leading constant theorem**:

\[
\boxed{
\mathbb E_\pi S_{\rm D6}(f,g_\pi)
=\left(\frac{16}{3}+o(1)\right)s^6
}
\]

as s=2^h→∞, with the o(1) UNIFORM over every adversarial complete global f and every allowed occupied line pair-edge support. This refines the interpretation of the previously known D6 contribution to the full global-uniform seven-family expectation, without claiming a new unrestricted full-seven deterministic theorem.

The result is technically meaningful because the point f is fixed BEFORE the conditional expectation, and the physical image edge holes on the line side stay fixed. Uniform asymptotic first moment by itself gives neither concentration nor a lower tail against a fixed adversarial global g.

## 7. Independent falsification protocol and limitation ledger

The FOUR additive files are a mathematical executor, seven independent true-source test groups, this proof Markdown, and a dedicated GitHub-hosted workflow.

- **Symbolic all-h h=1..80** exact large integer minimal physical alphabet a, V,d,m, number of complete K_a physical C6, exact per-missing-edge cycle deletion count, source genuine Hall/union-bound injection q_s, exact rational conditional expectation lower AND upper, finite 2/3 s⁶ lower for s≥4 and exact rigorous 1408/2025 s⁶ proof for s≥8. No fabricated huge finite GQ source models.
- **TRUE ORIGINAL W(3,2) five globally injected typed K6 maps** zero-split, lex, reverse, S68, S72: independent (1) source-physical-C6-FIRST enumeration using all 6cycle physical edges then actual original incident SIX different line SDR matchings via a six-bit LINE-FIRST DP, and (2) SOURCE ORIGINAL point-six-subset-FIRST enumeration over all \(\binom{15}{6}=5005\) distinct original point factor sets, checking their physical f six-vertex degree two+connectivity without using cycle enumerator, followed by source SDR DP. Plus an unrelated actual original recursive line-factor assignment oracle to independently validate every source original six-line SDR count, instead of reusing the bitset recurrence. Both independently compute EXACT conditional Fraction \(A_6(f)\cdot12C_6(G_g)/(V)_6\) and must agree. Independent 720 physical 6-vertex permutations enumerate 60 K6 simple cycles and validate the exact 12 physical cycle isomorphisms used in the probability count.
- **TRUE W(3,4), W(3,8)** lex/random nononto globally complete original point/line K14,K35 pair-label maps with 6 and 10 holes respectively: take genuine actual D source anchors and globally occupied oriented physical P5 source factor lists from #537, generate genuine six original points forming a physical connected C6, then compute the exact number of distinct original line SDRs using genuine source line-major DP. Check >=d⁴(d²−15) and use the independent recursive original-source 6line assignment oracle for real W34. W38 is an explicit single-cycle original source-neighbor witness, NOT a full W38 sixset count.
- Original source symplectic point+line automorphism on true W32 and separately permuted physical point and line alphabets preserve exact conditional expectation and real original source SDR count; fake original incidence graph and noninjective typed physical label maps rejected.
- **Strict counterexample to a stronger adversarial statement:** historical fixed true-original W32 global S68/S72 have **zero D6**, while their conditional mean over the allowed line-source label permutations is strictly positive. This shows why the result is an ENSEMBLE conditional theorem despite holding for EVERY fixed point f and physical line image support.

**Root #230:** Branch A remains UNPROVED; Branch B no infinite actual source globally injected witness; Branch C equivalence not established; no full R3 bound or ASET exponent. Research finding category: **RESTRICTED_THEOREM — one-map-adversarial quenched conditional original D6 first moment**. Never claim \(S_s(f,g)\ge c s^6\) FOR EVERY fixed f,g from an average over permutations. No self-hosted runners, no Deep Research delegation, no unreviewed accepted formal RCP JSON promotion.

**Next meaningful scientific step:** test or prove variance/second-moment / deterministic permutation-discrepancy controlling how the D6 distribution under ONE global line-factor permutation can concentrate near zero, then couple D6 to B/A, A/B, B/B and original source C/* zero-D-anchor U under the SAME fixed maps. Such an independent second moment theorem could reveal whether typical globally permuted g (not just some favorable one) has D6=Ω(s⁶), but it still does NOT close the completely adversarial g model without additional anti-correlation or joint compensation.

**Acceptance:** exact FINAL HEAD dedicated + INDEX + Proof Audit + Full Research GitHub-hosted green and independently reviewed mathematics required before registering frozen SHA in canonical RCP JSON and regenerating the five derived Markdown registry pages. Keep Draft child of #537, do not merge into main or close #230 based on this first-moment theorem.
