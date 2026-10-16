# HYP-105 / issue #230 — AA4-AV: universal genuinely source-distinct GOOD D wedges and exact four-port original incidence coupling tensor

**Strict stacked research-only Draft child of AA4-AU PR #552, frozen parent exact SHA \`ae926a8b6bd83b773573dc430761fff74c95e3f5\`.** This slice uses true ORIGINAL symplectic \(W(3,s)\), \(s=2^h\), ALL globally complete point-source and line-source physical unordered-pair injections \(f,g\), held fixed over all real original source incidence flags. No model averaging, per-wedge f/g redraw, fake source forests or unsigned RCP acceptance claim. The universal seven-positive-GF5 six-incidence-set lower \(S_s(f,g)=\Omega(s^6)\) remains **OPEN**.

## 1. Why AA4-AV differs from AA4-AR/AU

AA4-AR proved \(\Omega(s^6)\) GOOD source *two-D-edge centered three-flag wedges* (uncolored), but did not force their three original source point factors and three original line factors to be pairwise distinct. AA4-AU separately counted \(N s^2\ge s^6\) TRUE ORIGINAL *source B/B three-flag P4s*, but did not attach any physically compatible D edges or seven-GF5 selection. The two reservoirs cannot simply be added.

AA4-AV establishes a new deterministic **ALL-GLOBAL fixed-two-map positive** lower on the *source A/A* GOOD D-wedge reservoir for every \(h\ge16\), eliminating the source-factor repetition gate without needing two-typed physical opposite-port balance. It also creates a new direct algebraic ORIGINAL-incidence \(2\times2\) port-correlation tensor \(F^\top B G\) with the exact source-degeneracy corrections, which exposes precisely the remaining global f/g correlation, rather than relying on source-only or physical-only candidates.

## 2. NEW AA4-AV1 — exact ORIGINAL source three-type GOOD centered wedge partition

Let \(I\) be the set of \(N=V(s+1)=(s+1)^2(s^2+1)\) TRUE original incidence flag IDs \((p,\ell)\), and let \(\mathcal D_g(f,g)\) be the GOOD bilateral original \(D\)-pair graph of AA4-AP on \(I\), with \(E_g\) undirected true source edges and true source flag center vertex degree \(d_i\). Each edge \(\{(p,\ell),(q,m)\}\) requires \(p\neq q,\ell\neq m\), intersection of the original f(p),f(q) physical point coordinate pair labels, intersection of g(\ell),g(m) physical line labels, AND its globally fixed four free physical ports avoid the globally defined physically bad endpoint sets.

Every centered GOOD two-D-edge wedge \(\{j-i-k\}\) uses three distinct original flag IDs. Its two *outer* true source flags \(j,k\) may share one original point or one original line, but CANNOT share both: they would be the same original incidence flag ID. Their common TRUE source center shares neither point nor line with either outer flag by genuine bilateral D predicate. Thus the exact original source-factor-type partition of ALL GOOD centered wedges is

\[
\begin{aligned}
W_{\rm good}
 &=W_{AA}+W_{BA}+W_{AB},\\
W_{BA}
 &=\sum_i\sum_{q\neq p_i}\binom{
   \#\{j\in N_g(i):\operatorname{point}(j)=q\}}{2},\\
W_{AB}
 &=\sum_i\sum_{m\neq \ell_i}\binom{
   \#\{j\in N_g(i):\operatorname{line}(j)=m\}}{2},\\
W_{AA}
 &=\sum_i\binom{d_i}{2}-W_{BA}-W_{AB}.
\end{aligned}
\]

The B/A or A/B symbols in these equations are **SOURCE factor multiplicity types on THREE flags**, NOT the old seven accepted GF(5) sixflag classes. **Every original source B/B threeflag P4 has ZERO centered two-D-edge wedges, GOOD or otherwise.** Why: the unique original B/B source P4 flag triple has two original point and two original line factor IDs; whichever source flag is chosen as center, at least one of the two required D edges shares its actual original source point or its original line with that center, violating the TRUE D source-factor inequality. Therefore AA4-AU's original \(N s^2\ge s^6\) source B/B population is **PROVABLY DISJOINT** from the AA4-AR / AA4-AV D-wedge route, NOT a second reserve that can be substituted into its continuation theorem.

The real original W(3,s) point and line factor valency is \(d=s+1\): a fixed outer original point factor can be used by at most d DISTINCT incident original flags, same for a fixed outer line. Applying \(\binom r2\le(d-1)r/2\) to each original factor fiber at every center, the two distinct true original source collision channels each have UPPER at most \((d-1)E_g\), because \(\sum_i d_i=2E_g\). Thus:

\[
\boxed{W_{AA}\ge\sum_i\binom{d_i}{2}-2(d-1)E_g
       \ge \frac{2E_g^2}{N}-(2d-1)E_g.}
\]

This is a deterministic all-h ALL-global original SOURCE/physical-coupled good-wedge bound, with no statistical assumptions. The first inequality is a source valency restriction; the second is Cauchy and true graph handshake, not a claim of a novel extremal combinatorial inequality.

Every GOOD physically two-typed **opposite-port** wedge is within source A/A: if two outer flags share their original source point q, they have the SAME fixed physical point pair f(q), so its intersection with the center's point physical pair f(p) is the same point physical coordinate on both center edges; hence the two point colors CANNOT be opposite. Likewise if outer line source factor repeats. Consequently source BA/AB wedges contribute exactly ZERO to the physically opposite port two-edge wedge count \(R_g\), but source A/A itself does NOT force physical port complement; arbitrary fixed global f,g could make physical colors correlate adversarially. No \(R_g=\Omega(s^6)\) follows yet.

## 3. NEW AA4-AV2 — universal source A/A GOOD real wedge lower \(\boxed{W_{AA}\ge s^6/10}\) for \(h\ge16\)

Use the STRONG exact original AA4-AP lower, rather than its much weaker printed corollary \(E_g\ge s^5/10\). Let \(V=(s+1)(s^2+1),d=s+1,N=Vd\), \(a\) the MINIMAL original physical coordinate palette such that \(\binom a2\ge V\), \(m=\binom a2-V\), \(b=\min(31,\lfloor32m/a\rfloor)\) and
\[
K = \frac{d(a-1)^2}{V}+\lceil\sqrt{2s}\rceil(a-1).
\]
AA4-AP previously proved for EVERY fixed complete original f,g,
\[
E_g\ge L_s=\max\left(0,\frac{8V^2d^2}{a^2}-2Vd^2-
                       8b(a-1)dK\right).
\]
The exact source-collision corrected Jensen function
\[
\Phi_s(E)=\frac{2E^2}{N}-(2d-1)E
\]
is strictly increasing whenever \(E>N(2d-1)/4\). For h>=16 the exact L_s exceeds this threshold (verified symbolically for h>=24 below, and by EIGHT exact Fraction inequalities for h=16,...,23). Therefore for every arbitrary globally injected real f,g,
\[
W_{AA}\ge\Phi_s(E_g)\ge\Phi_s(L_s)\ge s^6/10.
\]

**Exact FINITE-PARAMETER proof for h=16,...,23:** each one of the eight exact rational inequalities \(\Phi_{2^h}(L_{2^h})\ge2^{6h}/10\) is checked using full integer/combinatorial formulas and exact fractions in the new repository verifier. These checks are finite **parameter inequalities** supporting a mathematical all-map result at each h, NOT enumeration/materialization of \(W(3,2^h)\). The minimum observed among h16..23 occurs at **h17**, with \(\Phi_s(L_s)/s^6>0.13\); no approximate decimals are part of the proof.

**Symbolic proof for ALL h>=24:** write s=2^h, so \(\sqrt s\ge4096\). From minimality of a, \((a-1)(a-2)<2V\), hence \(a^2<2V+3a\). Thus
\[
\frac{8V^2d^2}{a^2}-2Vd^2
> 2Vd^2-6ad^2
\ge 2s^5-\frac{75}{4}s^{7/2},
\]
using \(a\le2s^{3/2}\), \(d\le5s/4\), and \(Vd^2\ge s^5\). The previously established AA4-AP all-h physical bad-port source-spectral upper is \(E_{\rm bad}\le3255s^{9/2}\); for h>=24,
\[
\frac{L_s}{s^5}\ge
 2-\frac{75}{4s^{3/2}}-\frac{3255}{\sqrt s}
 \ge 2-\frac{75}{4\cdot4096^3}-\frac{3255}{4096}
 \ge\frac{11}{10}.
\]
Also
\[
N=(s+1)^2(s^2+1)\le(1+4/s)s^4,\quad 2d-1=2s+1.
\]
Therefore \(2L_s/N-(2d-1)\) is at least
\[
\frac{11s/5}{1+4/s}-(2s+1)
\ge\frac{s}{5}-\frac{49}{5}
\ge\frac{s}{10},
\]
where \(1/(1+x)\ge1-x\), valid for positive x, and s>=2^24>98. Consequently
\[
W_{AA}\ge L_s\left(\frac{2L_s}{N}-(2d-1)\right)
\ge\frac{11}{10}s^5\cdot\frac{s}{10}
=\frac{11}{100}s^6>\frac{s^6}{10}.
\]

**Honest exceptional exponent:** The AA4-AP exact spectral good D lower at h=15 is too weak for this specific Cauchy-minus-source-collision proof to yield positive \(\Phi_s\): a negative calculable lower is not evidence of absence of actual source A/A GOOD wedges. At h=14 the same explicit rational formula happens to be >s6/10, but the clean all-sufficiently-large-h theorem claims **h>=16**, not any all-h>=14 extension. No genuine W(3,2^15) counterexample was constructed or implied, and there is NO accepted GF5 theorem.

This is a new *nontrivial SOURCE-factor-distinctness upgrade of the guaranteed GOOD original flag-wedge reservoir*, not an original GQ spectral theorem or general new Cauchy bound. It closes one earlier explicitly open structural gap: the total \(\Omega(s^6)\) true GOOD wedges cannot ALL be source BA/AB repeats when s is sufficiently large.

## 4. NEW AA4-AV3 — direct globally correlated ORIGINAL incidence 2×2 physical port coupling tensor

Let B be the ACTUAL \(V\times V\) source point-line incidence matrix; F and G the two globally fixed typed ORIGINAL source-factor incidence-to-physical-coordinate 0/1 matrices: \(F_{p,c}=1\) iff c belongs to the physical unordered pair f(p), \(G_{\ell,e}=1\) iff e belongs to g(\ell). For a true ORIGINAL center incidence flag \(i=(p,\ell)\) with ordered physical endpoint labels \(f(p)=\{c_0,c_1\}\), \(g(\ell)=\{e_0,e_1\}\), define

\[
X_i^{uv}
 = (F^\top B G)_{c_u,e_v}
 - (B G)_{p,e_v}
 - (F^\top B)_{c_u,\ell}
 + B_{p,\ell}.
\]

Since (p,l) is a genuine ORIGINAL source flag, \(B_{p,\ell}=1\). This is EXACTLY the number of REAL other ORIGINAL source incidence flag IDs \(j=(q,m)\) in physical D-neighbor bin (u,v), satisfying BOTH original source \(q\ne p,m\ne\ell\) and both typed physical overlaps. Inclusion/exclusion subtracts true original source repeated point and repeated line, and adds their common genuine center flag back; no assumption that F and G are independent.

The local corrected tensor gives the exact, globally quenched all-h physical opposite-port energy

\[
\boxed{R_{\rm all}(f,g)
=\sum_{i\in I}\bigl(X_i^{00}X_i^{11}
                 +X_i^{01}X_i^{10}\bigr).}
\]

This is NOT yet the AA4-AR GOOD wedge R_g: the latter additionally excludes actual globally physically bad free ports on both typed maps. It is, however, an exact 2×2 true-original source-incidence correlation formula containing the cross-type \(F^\top B G\) term and two essential source-degenerate subtractions. Source-factor-distinctness of its two-typed opposite wedges is automatic. There is no immediate positive all-f,g lower on the diagonal products; the first two-port physical opposite/anti-correlation gate remains OPEN. A generic four-bin same-color concentration makes R=0 while many SOURCE A/A uncolored good wedges may exist. Such a bin table is an ABSTRACT local countermodel only, not an infinite global genuine W3s source family.

The implementation independently constructs \(F^\top BG\) directly from each genuine original point-line incidence flag (four contributions per flag), constructs BG and \(F^\top B\) point- and line-repetition corrections directly from original source incidences, and obtains X without enumerating all O(N²) original D-neighbor pairs. A SEPARATE literal original source-first D-neighbor graph referee checks all four tensor bins PER EVERY true source center incidence ID, not merely the global D and opposite wedge totals. This method isolates the actual mixed global f/g correlation and is a more promising analytical object than another source-only or physical-only motif count.

## 5. Independent checks, prior art and next AA4-AW

- Exact Fraction all-h parameter theorem h16..60, eight exact h16..23 certificates plus all h24+ symbolic analytic inequalities as detailed above; h15 explicitly NOT certified and h14 excluded from the chosen all-large-h theorem. No fake huge GQ.
- FIVE complete globally bijective typed point/line original W32 models dual-zero, lex, reverse, S68, S72; exact original GOOD D source threeflag AA, BA, AB partition from per-outer-source-factor bucket calculation, independently equal to O(sum genuine degree²) literal two-neighbor original source triple enumeration. Every physically two-type opposite-port GOOD wedge in each model must be in source A/A. Existing AA4-AR independent true threeflag total and opposite-port counts used only as crosschecks, not as primary calculation.
- TRUE ORIGINAL symplectic W34 GF4, two complete globally injected but K14-nonsurjective typed physical maps lex/random; source AA/BA/AB GOOD D wedge split crosschecked with independent original source triple enumeration and true AA4-AP source-good pair totals (lex 2072, random 147). NOT a full W34 seven-GF5 census.
- Per-original-center corrected 2×2 mixed globally fixed \(F^\top BG\) physical port tensor against literal old original D graph all true source vertices under W32 five maps and W34 lex/random; independently check point/line physical endpoint bins, total good-free original D edges and two-color opposite degrees. Source symplectic transvection and separately typed physical coordinate renaming preserve the original source wedge type distribution and mixed tensor scalar energies, as required.
- Forged original source incidence lists, noninjective original typed physical source factor labels rejected; an ABSTRACT one-bin local table explicitly demonstrates that SOURCE A/A good count cannot automatically yield two-typed physical opposite wedge lower without a global correlation theorem.

**Prior art:** Original GQ source factor valency, classical Cauchy/Jensen wedge double counting and old AA4-AP GQ incidence spectral bound are pre-existing results, not novel basic mathematics. Our specialized universal SOURCE **A/A original Good D-wedge \(s^6/10\)** all-global fixed-label corollary is new to this issue and is not the same as the earlier AA4-AR GOOD wedge bound which included source BA/AB repeats. The mixed original source-incidence \(2\times2\) color tensor is a new project-level corrected reparameterization of AA4-AL's \(F^\top B G\) full coordinate matrix, not a novel tensor operator abstractly.

**NEXT AA4-AW:** Now h>=16 all real global f,g necessarily have at least \(s^6/10\) GOOD centered source A/A threeflag wedges. This source distinctness gate is closed. But a positive fraction may still fail the physically opposite two-typed port constraint; even when they pass, the AA4-AS T/T physical obstruction, original 3×3 AA4-AU Boolean Hall polynomials and final positive seven-GF5 source six-ID classifier remain. The next deep theorem should estimate the diagonal products \(X00X11+X01X10\) or a corrected GOOD version relative to the now-proven source A/A GOOD mass, then global original Hall and sevenclass selection. Alternatively an independent positive source seven-GF5 sixset lower from unanchored U classes, C/A,C/B etc, could bypass D wedges. No positive all-f,g original selected \(S_s(f,g)=\Omega(s^6)\), and no genuine infinite correlated f_s,g_s original obstruction, has been proved.

Keep exact-HEAD GitHub-hosted Dedicated, INDEX, Proof Audit, Full Research separately, independent mathematical referee separate. Strict Draft child atop #552. No main merge, no accepted registry and issue #230 OPEN.
