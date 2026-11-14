# HYP-105 #230 — AA4-PATHCHARGE: all-h ORIGINAL physical P3 pathwise corner witness

**Scientific status:** ROOT remains \`OPEN_WITH_FORMAL_BLOCKER\`. This is a strict new child of the frozen all-three-CI-green [AA4-SIGNCHARGE #766](https://github.com/definitely-stable/Mathlab/pull/766), exact parent HEAD \`5a0d0f24131339b09afba684057fade648d42b68\`. This document does **NOT** claim the all-label seven-family six-motif \(\Omega(s^6)\) dichotomy, unconditional \(B/M<3/4\), an ASET exponent, or a GF5 full-root proof. No main/parent mutation or merges.

## 1. Highest-priority unclosed link after #766

The accepted #766 all-h signed nonnegative pair-cone result upper-bounds bad source-pair energy \(B\) by \(B(u)\) and good energy \(G\) by \(G(\ell)\), giving
\[
 B/M\le B(u)/[B(u)+G(\ell)].
\]
It rigorously certifies strict \(B/M<3/4\) in eight COMPLETE genuine symplectic W32/W34 fixed-correlated source settings, but does not identify a concrete physical source-geometric reason for hypothetical \(B/M\ge3/4\) on a different adversarial fixed f/g. The all-h original middle-neighborhood #761 obstruction identified a heavy **middle source flag**, yet did not retain the **first and last physical P3 corners** in a single obstruction witness.

**Chosen next theorem:** derive a closed ORIGINAL source formula for the *good and bad neighborhood of EACH real individual physical P3*, preserving its three named original first/middle/last source owners and both actual physical interior vertices. This gives a more restrictive necessary geometric witness for any B75 violation than a generic heavy-middle mass assertion; it also yields a rigorously valid rowwise interval signed certificate that shares the outer actual pathweight and can be combined with #766 without degradation.

## 2. Quantified real ORIGINAL source setup

Let \(s=2^h\) for arbitrary \(h\ge1\). Use TRUE symplectic \(W(3,s)\), every legal named ORIGINAL deleted incidence set \(Z\), retained paired original CORE \(C\), any fixed separately globally pair-injective \(f:P\hookrightarrow\binom{[a]}2\) and \(g:L\hookrightarrow\binom{[a]}2\), with absolutely arbitrary *mutual correlation*. Real physical edges are the paired two opposite diagonals of each retained ORIGINAL source incidence flag; no cloned flag owners or independently projected fake physical edges.

For each ordered PHYSICAL endpoint bin \(uv\), \(\mathcal P_{uv}\) contains ALL actual coordinate-proper directed physical P3 \(\gamma=(u,a,b,v)\) with original first/middle/last owners \((j,i,k)\), with the known common ORIGINAL shared-priority positive marginal weight
\[
 w_\gamma=\pi_J(j,i,k)/64>0.
\]
The weighted energies are the already established algebraic \(M(z),G(z),B(z)\) from #759/#760 for arbitrary positive pathweights \(z_\gamma\). **These are sums of products of marginal selectors, NOT probabilities of joint path retention.** This distinction prevents an invalid independence step.

## 3. NEW ALL-h pathwise true-original sparse corner identity

Fix a nonempty real bin, any positive rational pathweights \(z\), and \(\gamma=(u,a,b,v)\) whose actual middle owner is ORIGINAL incidence flag \(i=(p,\ell)\). Write \(W=\sum_{\eta\in\mathcal P_{uv}}z_\eta\) and \(z_i=\sum_{\eta:i(\eta)=i}z_\eta\).

Define the closed ORIGINAL middle-source-label overlap neighborhood
\[
 H(i)=\{r=(p_r,\ell_r)\in C\cap\operatorname{Middle}(\mathcal P_{uv}):
 f(p_r)\cap f(p)\ne\varnothing\;\lor\;
 g(\ell_r)\cap g(\ell)\ne\varnothing\}.
\]
Put the exact nonnegative source middle-neighborhood mass
\[
 N_i(z)=\sum_{r\in H(i)}z_r.
\]
All owners above are actual named ORIGINAL incidence IDs; their f/g labels are fixed and correlated.

The physical first-inner-corner **positive compatibility correction** for this *specific path* is
\[
 T_\gamma(z)=
 \sum_{\eta: a(\eta)=a}z_\eta
 -\sum_{\eta: a(\eta)=a,\ p_\eta=p}z_\eta
 -\sum_{\eta: a(\eta)=a,\ \ell_\eta=\ell}z_\eta
 +\sum_{\eta: a(\eta)=a,\ i_\eta=i}z_\eta.
\]
Thus \(T_\gamma(z)\) is EXACTLY the nonnegative mass of other source paths sharing the same first internal PHYSICAL corner \(a\) but with a **different original middle point AND line**. Define \(H_\gamma(z)\ge0\) analogously at the real last inner PHYSICAL corner \(b\). These genuinely physical common-corner pairs are GOOD even when their middle f/g symbol pairs overlap; dropping them is exactly the overcount criticized in the earlier spectral-shadow stages.

The original source GOOD indicator of #759/#760 partitions the true paths \(\eta\) relative to fixed \(\gamma\) into disjoint classes:
- diagonal \(\eta=\gamma\), weight \(z_\gamma\);
- disjoint BOTH original middle physical pair symbols, weight \(W-N_i(z)\);
- middle x/y overlap but same first inner physical vertex and different middle p AND line, weight \(T_\gamma(z)\);
- corresponding last-inner physical corner correction \(H_\gamma(z)\).

The last two cannot both hold for distinct paths with the same first and last middle interior physical vertices: a genuine undirected physical middle edge has a UNIQUE original named owner, and then the different-p/line condition fails. Consequently they are disjoint and the exact **NEW pathwise source corner identity** is

\[
\boxed{\begin{aligned}
g_\gamma(z)&:=\sum_{\eta\text{ compatible with }\gamma}z_\eta
=z_\gamma+W-N_i(z)+T_\gamma(z)+H_\gamma(z),\\
b_\gamma(z)&:=\sum_{\eta\text{ incompatible with }\gamma}z_\eta
=N_i(z)-z_\gamma-T_\gamma(z)-H_\gamma(z),\\
g_\gamma(z)+b_\gamma(z)&=W,\qquad
0<z_\gamma\le g_\gamma(z)\le W,\quad 0\le b_\gamma(z)\le W-z_\gamma.
\end{aligned}}\tag{P1}
\]

This is an **exact all-h original source pathwise row identity** for ANY positive z, not an asymptotic estimate or a simulated source. Its implementation uses O(n+q²) sparse physical port and original-middle postings, **not** a path-pair loop.

Multiplying by zγ and summing gives the prior globally established exact sparse second-moment identity as a NEW, independently computed conservation check:
\[
 \boxed{G(z)=\sum_{\gamma}z_\gamma g_\gamma(z),\quad
 B(z)=\sum_{\gamma}z_\gamma b_\gamma(z),\quad
 G(z)+B(z)=\sum_{uv}W_{uv}^2=M(z).}\tag{P2}
\]

## 4. NEW universal necessary JOINT original THREE-owner path witness

Assume on some true source \(M(w)>0\), and hypothesize \(B(w)/M(w)>3/4\). Then at least one NONEMPTY real ordered physical endpoint bin satisfies \(B_{uv}(w)/W_{uv}^2>3/4\). In that bin
\[
 \frac{B_{uv}}{W_{uv}^2}
 =\sum_{\gamma\in\mathcal P_{uv}}\frac{w_\gamma}{W_{uv}}
   \cdot\frac{b_\gamma(w)}{W_{uv}}
\]
is a positive-weighted average of **ACTUAL** physical path-neighborhood bad fractions. Thus there exists a real path \(\gamma=(u,a,b,v)\) whose three original owners j,i,k and *both true interior physical corners* satisfy
\[
 b_\gamma(w)>\tfrac34W_{uv}
\quad\Longleftrightarrow\quad
\boxed{
N_i(w)>
\tfrac34W_{uv}+w_\gamma+T_\gamma(w)+H_\gamma(w).
}\tag{P3}
\]
This simultaneously forces heavy original middle-label concentration **and** constrains genuine first/last physical port overlap: the positive same-corner compatible terms raise the required overlap threshold. Replacing > by \(\ge\) yields a necessary witness if global ratio is \(\ge3/4\). Also \(w_\gamma<W_{uv}/4\) follows because \(N_i\le W\) and \(T,H\ge0\).

This is a structural **necessary** obstruction for a hypothetical adverse all-h family, not an inequality automatically forcing the obstruction absent. It refines the previously separate #761 heavy-middle-only and #764 joint-physical-port reductions into a SINGLE real source triple/corner witness.

## 5. NEW ALL-h conservative rowwise signed interval sufficient criterion

#765 gave pointwise source-codegree bounds \(0<\ell_\gamma\le w_\gamma\le u_\gamma\). Since each row charge is an actual sum of pathweights over an invariant GOOD or BAD support, each \(g_\gamma(z)\) and \(b_\gamma(z)\) is coordinatewise nondecreasing on nonnegative z. Thus
\[
 3g_\gamma(w)-b_\gamma(w)
 \ge L_\gamma:=3g_\gamma(\ell)-b_\gamma(u).
\]
Multiplying by wγ and using the sign of Lγ gives the *new valid source lower*
\[
\boxed{
3G(w)-B(w)\ge
L_{\rm row}:=
\sum_\gamma
\begin{cases}
\ell_\gamma L_\gamma,&L_\gamma\ge0,\\
u_\gamma L_\gamma,&L_\gamma<0 .
\end{cases}}\tag{P4}
\]
This is all-h exact-domain **interval arithmetic**, not an event-independence claim. The sufficient condition \(L_{\rm row}>0\) implies strict B/M<3/4 even if SOME local rows fail; if **every** row Lγ>0, it implies every true endpoint bin is safe. There is no claim it always dominates the earlier #766 criterion \(3G(\ell)-B(u)>0\). The right proof-grade combined certification is **max of independently valid source lower margins**, not an invented universal ordering.

For an explicit global risk upper when \(L_{\rm row}\ge0\), let \(M_U=M(u)\), so
\[
 \frac{B(w)}{M(w)}
 =\frac34-\frac{3G(w)-B(w)}{4M(w)}
 \le\frac34-\frac{L_{\rm row}}{4M_U}.
\tag{P5}
\]
For \(L_{\rm row}<0\) P5's denominator sign would reverse: **do not** use it with \(M_U\); the source program conservatively reports 1 for that optional bound. At any sign, combine with accepted #766 ratio upper via minimum. All tests check non-deterioration and direct exact risk.

## 6. Acceptance, falsifiers and prior-art honesty

The hosted specialist:
1. Independently builds all eight real W32/W34 complete genuine original physical three-owner source-port path populations, preserving exactly \(1346,1154,838,83892,82846,79404,9966,66418\) paths.
2. Applies exact codegree priority weight intervals and the new direct per-P3 original middle/corner posting formula at exact weights, lower weights, and upper weights.
3. Independently compares \(G,B,M\) to the **prior** original middle-owner sparse second-moment code for every endpoint and each of three weight assignments.
4. Uses a **separate literal O(n²) physical P3 pair-oracle from #766** to check the GOOD and BAD mass of EACH physical path on selected genuinely ORIGINAL W32/W34 endpoint bins, at all three weight assignments. This does not depend on the new identity or on the previous sparse source moment implementation.
5. Verifies all signed interval margins and the strict/weak bad-physical-path witness logic, including a clearly isolated synthetic *abstract* five-conflicting-vertex positive cone example which shows that the theorem is conditional; it is **NOT** presented as realizable original GQ.
6. Runs strict CI on GitHub-hosted ubuntu-24.04/Python3.12 only, plus INDEX and full Research, all on the SAME final PR HEAD. No PC, no merges, no root status edits.

Order-statistics, weighted averaging, sparse inclusion-exclusion and positive coefficient arithmetic are standard. What is scoped as useful new HYP-105 research is the all-h **true original incidence owner FIRST/MIDDLE/LAST physical-corner local witness identity** bridging the existing source endpoints, selector-weighted exact risk and one REAL path forced to carry the obstruction.

**Remaining root barrier:** show no such heavy true physical joint three-owner/corner witness can occur with enough total mass to spoil \(\Omega(s^6)\) for ALL correlated f/g/h, OR build a true legal infinite dyadic bad family. None of the current exact finite sources proves this.
