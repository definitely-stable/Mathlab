# HYP-105 / #230 — AA4-HEAVYREF: independent ORIGINAL heavy Caro–Wei / two cuts / **no-clone** supersaturation with sharper constants

**Scientific status:** Draft PR strictly stacked on [#738](https://github.com/definitely-stable/Mathlab/pull/738) frozen parent HEAD \`5bb354736176ff4be01b18703fd65b710db9700b\`. The full source theorem is for true symplectic \(W(3,s)\), dyadic \(s\ge64\), arbitrary COMPLETE separately globally pair-injective physical point/line maps \(f,g\) with arbitrary correlation, and any adversarial deleted ORIGINAL incidence-ID set \(Z\) with \(|Z|\le\rho s^4\). All physical vertices/edges below refer to ORIGINAL, unchanged coordinate pairs; no clones, synthetic vertices or independent f/g randomization. Graph supersaturation supplies POSITIVE but UNKNOWN existential absolute \(C_{\rm graph},c_{\rm graph}\); algebraic rational trial values \(C_0,c_0\) are not published numerical constants. Main and ancestor PRs remain unchanged; no merge, no root #230 closure, no ASET exponent.

The purpose is twofold: an **independent all-order constructive proof** of the entire heavy source→ordinary no-clone graph→D6 implication, and a useful **strict improvement** in its all-order sufficient constants from tighter original geometry (without changing its hypotheses or risk-experiment definition).

## 1. Original algebraic envelope with STRICTLY better uniform bounds

For genuine \(W(3,s)\), \(s=2^h\ge64\),

\[
V=(s+1)(s^2+1),\quad N=(s+1)V=(s+1)^2(s^2+1),\quad
a=\min\left\{b:\binom b2\ge V\right\},
\]
\[
C_s=(s^2+1)(s^2+a-2),\quad
n= a^2=\#\{\text{all original physical coordinate-pair corners}\}.
\]

The previous heavy/root proof only used \(N\le2s^4\), \(a^2\le4s^3\), \(C_s\le3s^4/2\). Independent exact asymptotic-free improvements, for **every** \(s\ge64\), are:

\[
\boxed{
 V\le\frac{33}{32}s^3,\quad
 N\le\frac{17}{16}s^4,\quad
 a^2\le\frac94s^3,\quad
 C_s\le\frac54s^4,\quad
 e_J\le2C_s\le\frac52s^4.
}\tag{H-ENV}
\]

The bounds are **analytic**, not interpolated from small \(W(3,s)\). Indeed, for \(s\ge64\),

\[
V/s^3=1+s^{-1}+s^{-2}+s^{-3}
\le1+1/64+1/4096+1/262144<33/32,
\]

\[
N/s^4=1+2/s+2/s^2+2/s^3+1/s^4
\le1+2/64+2/4096+2/262144+1/64^4<17/16.
\]

Minimality \(\binom{a-1}2<V\) implies \(a<\sqrt{2V}+2\). Since
\(\sqrt{2V}\le(\sqrt{33}/4)s^{3/2}\le(23/16)s^{3/2}\) and \(2/s^{3/2}\le1/256\),

\[
a/s^{3/2}<23/16+1/256<3/2,
\]
hence \(a^2\le(9/4)s^3\). Finally,

\[
C_s/s^4
=(1+s^{-2})(1+(a-2)/s^2)
\le(1+1/4096)(1+3/16)<5/4.
\]

The final source conflict edge cap uses the independently established ORIGINAL point/line SRG spectral source bound \(e_J\le2C_s\) from [#737](https://github.com/definitely-stable/Mathlab/pull/737), with **no independence assumption on f,g**. The new implementation recomputes actual \(a,N,C_s\) using fast exact integer discriminants (not a linear loop), and checks all inequalities at multiple dyadic orders.

## 2. Freeze ORIGINAL full-heavy vertices **before** adversarial Z

Let \(H=H(f,g)\) be the full true ORIGINAL physical graph. Each actual named original incidence flag \(i=(p,\ell)\) owns BOTH opposite true diagonals of rectangle \(f(p)\times g(\ell)\), and every physical edge has a UNIQUE source owner: the two physical coordinates of its endpoints uniquely determine both injected original f(p) and g(ell).

For a true physical degree threshold \(Ts\), freeze

\[
Q_T=\{v\in V(H):d_H(v)>Ts\},\quad
E_T=\#\{e\in E(H):e\cap Q_T\ne\varnothing\}
\]
**before** deleting Z. In the heavy branch assume \(E_T\ge s^4/8\). Deleting a source flag destroys at most two physical edges, so the genuine surviving full-heavy edges \(E_A\) satisfy

\[
E_A\ge E_T-2|Z|
\ge(1/8-2\rho)s^4\ge s^4/16,
\quad \rho\le1/32.
\]

Let \(I_H\) be the set of **distinct actual source owners** of these surviving edges. Each such flag owns at most two of them, and therefore

\[
\boxed{L:=|I_H|\ge E_A/2\ge s^4/32.}\tag{H-L}
\]

This does not allow re-evaluating the degrees after Z or silently replacing original incidence IDs by physical edge IDs. The independent implementation uses the full owned edge map, records all source deletions and checks \(E_T-E_A\le2|Z|\).

## 3. Independent original-source Caro–Wei and **two coherent whole-flag cuts**

Let \(J\) be the TRUE ORIGINAL conflict graph on \(I_H\): two flags conflict precisely when they share their source point and their real line pair labels overlap, or share their source line and their real point pair labels overlap. The SRG lemma from #737 bounds \(e(J)\le2C_s\le(5/2)s^4\). A uniformly random original source-ID priority order gives a conflict-free local-minimum set with expected size \(\sum_{i\in I_H}(d_J(i)+1)^{-1}\), so

\[
\alpha(J)\ge\sum_{i\in I_H}\frac1{d_J(i)+1}
\ge\frac{L^2}{L+2e(J)}
\ge\frac{(s^4/32)^2}{s^4/32+5s^4}
=\boxed{\frac{s^4}{5152}}.
\tag{H-CW}
\]

The last inequality uses monotonicity of \(x^2/(x+5)\) for \(x>0\); importantly, it does **not** discard \(L\) by substituting the old crude upper bound \(N\le2s^4\) in the denominator.

A deterministic independent *min-residual-degree* source greedy selects at least the original Caro–Wei weight: with potential \(\Phi(J)=\sum_i1/(d_J(i)+1)\), removing a minimum-degree original vertex and all its neighbors decreases \(\Phi\) by at most one. This checks a genuine source-independent-set **constructively**, not just the expectation.

For the resulting independent set, independently assign fair binary bits to every REAL physical first-coordinate symbol. Each actual original \(f(p)\) label pair is bichromatic with probability 1/2, regardless of correlations between the pair labels. Fix a coloring retaining at least half the source IDs via exact conditional expectation. Repeat independently on the ACTUAL g(ell) line-pair physical symbols for the surviving WHOLE source flags; choose a coloring retaining at least half again. This retains a true original conflict-independent, doubly bichromatic source set \(S\), satisfying

\[
\boxed{|S|\ge\frac14\alpha(J)\ge\frac{s^4}{20608}.}\tag{H-S}

\]

Each selected named original flag retains its **BOTH original physical diagonals**, without random recoloring the f/g maps themselves.

## 4. Actual heavy witness, one TRUE physical side and an ordinary no-clone graph

Each selected \(i\in S\subseteq I_H\) has at least one genuine surviving full-heavy physical edge with owner i. Choose ONE **distinct physical edge** \(e_i\) per original owner as its witness, and choose one of that edge's physical endpoints \(q_i\in Q_T\). The first typed binary cut guarantees that the other endpoint of \(e_i\) has the **OPPOSITE first-coordinate bit**, even when both endpoints are physically heavy.

Of the two left-bit classes of chosen heavy witness endpoints, take the majority. Let \(R_Q\subseteq Q_T\) be ALL genuine physical heavy vertices of that majority bit (not cloned copies) and \(Y\) all existing selected physical vertices of the opposite bit. Their actual cross-physical-edge graph has

\[
E(R_Q,Y)\ge |S|/2.
\tag{H-WITNESS}
\]

In particular \(r=|R_Q|>0\) and \(r\le q=|Q_T|\). Both R and Y consist of literal distinct physical coordinate pairs. Let \(n=a^2\), and partition the actual Y vertices into at most \(\lceil |Y|/r\rceil\le\lceil n/r\rceil\le2n/r\) disjoint blocks each of at most r **actual** vertices. By pigeonhole, one block \(Y_*\) has at least

\[
m_F:=e_H(R_Q,Y_*)\ge\frac{E(R_Q,Y)}{\lceil |Y|/r\rceil}
\ge\frac{|S|r}{4n}.
\tag{H-CHUNK}
\]

Take the **ordinary simple physical graph**
\(F=H_{\rm selected}[R_Q,Y_*]\) on precisely the original physical vertices \(R_Q\cup Y_*\) and precisely their existing original selected edges. No copied physical vertices, no new edges, no replacement source owners; any selected owner may now retain only ONE of its previously paired two diagonals, which is allowed for the HEAVY ordinary C6→six-ID step.

As \(v_F\le2r\le2q\) and \(m_F/v_F\ge |S|/(8n)\), (H-ENV) and (H-S) yield

\[
\boxed{\frac{e(F)}{v(F)}\ge
\frac{s^4/20608}{8(9/4)s^3}
=\frac{s}{370944}.}\tag{H-DENSITY}
\]

The genuine full source graph has \(2N\) edges and degree sum \(4N\). Since every vertex in Q has degree greater than \(Ts\),

\[
q\,Ts<\sum_{v\in Q}d_H(v)\le4N\le\frac{17}{4}s^4
\quad\Longrightarrow\quad
\boxed{v_F\le2q\le\frac{17}{2}\frac{s^3}{T}.}
\tag{H-VERTICES}
\]

These are **independently derived all-order bounds on an actually constructible ordinary simple, no-clone physical graph**, not an artificial blow-up host.

The standalone red-team code independently reconstructs the true source graph, local greedy selection, both typed cuts, genuine heavy-edge witness, chosen heavy majority bit, and the actual balanced winner; it records each winning physical edge and its unchanged original owner.

## 5. Exact published ordinary C6 SS6 application and improved universal heavy constants

The published ordinary graph supersaturation theorem of Simonovits, in the self-contained graph case \(r=2,k=3\) of Jiang–Yepremyan, *Supersaturation of even linear cycles in linear hypergraphs*, Combin. Probab. Comput. 29 (2020), 698–721, DOI [10.1017/S0963548320000206](https://doi.org/10.1017/S0963548320000206), says there are **absolute but unspecified** positive \(C_{\rm graph},c_{\rm graph}\) such that

\[
e(F)\ge C_{\rm graph}\,v(F)^{4/3}
\quad\Rightarrow\quad
\#C_6(F)\ge c_{\rm graph}\big(e(F)/v(F)\big)^6.
\]

Select purely symbolic rational trial bounds \(C_0\ge\max(1,C_{\rm graph})\) and \(0<c_0\le\min(1,c_{\rm graph})\). **No numeric values of \(C_{\rm graph},c_{\rm graph}\) are asserted.** To guarantee the hypothesis for the actual physical F, by (H-DENSITY) and (H-VERTICES) it is sufficient that

\[
\left(\frac{s}{370944}\right)^3
\ge C_0^3\frac{17s^3}{2T}
\iff
\boxed{
T\ge T_{\rm sharp}:=
\left\lceil \frac{17}{2}(370944)^3C_0^3\right\rceil.
}
\tag{H-SS6}
\]

At formal C0=1 this has the EXACT (but not published physical graph theorem!) numerical value

\[
T_{\rm sharp}=433854371818635264,
\qquad T_{\rm old}=2^{64}=18446744073709551616,
\]

an improvement factor \(T_{\rm old}/T_{\rm sharp}\approx42.5183\). Under the **real** published ordinary C6 theorem and independently proved ORIGINAL six-ID proper cycle injection from #734/#738, every simple sixcycle in the genuinely selected winning ordinary F has six distinct original source owner point and line IDs (all avoid Z), and no two distinct physical C6 can map to the same named source six-ID set. Indeed, source conflict freedom excludes physical typed distance-two cherries and the two typed color cuts exclude any same-coordinate pair at cyclic distance three; together with distinct endpoints of physical diagonal edges this covers all cyclic distances 1,2,3. The physical C6 then induces aligned original f/g factor C6s and is a positive D6 motif under the independently evaluated original GF5 weights of #735.

Therefore the sharpened **conditional all-order ORIGINAL heavy conclusion** is

\[
\boxed{
D_{6,\bar Z}\ge
c_0\left(\frac{s}{370944}\right)^6
=:\delta_{\rm sharp}s^6,
\qquad
\delta_{\rm sharp}=\frac{c_0}{(370944)^6}.
}\tag{H-D6}
\]

Relative to the earlier valid safe \(c_0/2^{120}\), the multiplier improves by the exact ratio

\[
\boxed{\frac{\delta_{\rm sharp}}{\delta_{\rm old}}
=\frac{2^{120}}{370944^6}\approx510.21.}
\]

This does not prove any new exponent, unconditional graph-theorem constants, or an ASET construction.

## 6. Compatible original LOW bridge and new all-order formal h0

Use the **previously independently established** original-source LOW lemma and the sharper \(L_4\) proved in [#738](https://github.com/definitely-stable/Mathlab/pull/738); the new HEAVY proof does not relabel the source, change the Q definition or replace the moment selector. With the same K=64, put

\[
q_r=4^r\binom{r(K+1)}r\quad (r=2,3),\ 
L_6=24+288T_{\rm sharp}^2,
\]

\[
L_4^{\rm SHARP}
=q_2^2\lceil\sqrt{8L_6}\rceil+28T_{\rm sharp},\ 
B_0=\lceil\sqrt{1280(K+1)T_{\rm sharp}}\rceil,
\]

\[
E=8q_3\lceil\sqrt{L_6}\rceil,\quad
D=4\lceil\sqrt{B_0T_{\rm sharp}L_4^{\rm SHARP}}\rceil,
\quad
\rho_{\rm sharp}=\frac{1}{12q_3^2L_6},
\]

\[
s_{0,\rm sharp}=\max\{64,672T_{\rm sharp},(8E)^2,(8D)^8\},
\quad h_{0,\rm sharp}=\lceil\log_2s_{0,\rm sharp}\rceil.
\]

The rederived heavy bound \(\delta_{\rm sharp}\) is still much smaller than the genuine original LOW class count \(BBo_{\bar Z}\ge(5/32)s^6\). With the source-specific full 51-palette ten-sign weights from #735, the combined **CONDITIONAL** heavy/low result becomes

\[
\boxed{
R_3\ge
\frac{54162\,c_0}{370944^6\cdot51^6}s^6
}\quad\text{for all dyadic }s\ge s_{0,\rm sharp}.
\tag{H-RISK}
\]

This is approximately 510× the sufficient risk constant from #738 (same already-proved full D6 weight 54162); it also permits a larger Z deletion radius because \(L_6\) shrinks along with the T threshold.

Three strictly **FORMAL algebraic probes**, not the numerical C,c constants of the actual published graph theorem:

| Formal rational \(C_0,c_0\) | Previously improved #738 dyadic h0 | New HEAVY + SHARP-L4 dyadic h0 | Change |
|---|---:|---:|---:|
| (1,1) | 872 | **818** | −54 |
| (2,1/5) | 902 | **848** | −54 |
| (7/3,1/17) | 908 | **854** | −54 |

No practical s claim follows: the actual graph constants remain existential and the universal sufficient h0 remains astronomically large even for these fictional sample parameters.

## 7. Source-first code, 10 adversarial tests and scientific STOP

New [independent Python source referee](../../research/hyp105_original_heavy_no_clone_sharp_ss6.py) imports NONE of the previous source/heavy/selector/root certificates. It uses only the trusted actual-original symplectic source and fixed globally injected label constructors for real finite W32/W34 falsification. Implementations are independent:

- reconstruct the full true two-diagonal physical owner graph and freeze original full-Q **before** Z; each flag deletes at most 2 heavy physical edges;
- construct the actual source conflict adjacency from point/line incidence IDs (no synthetic physical vertex IDs), Caro–Wei min-residual-degree independent set and exact potential drop, and two separately derandomized full WHOLE-flag binary cuts;
- retain one actual full-Q edge witness per selected original ID, choose a genuine heavy physical majority bit side, and construct the explicit balanced no-clone block from actual remaining physical Y vertices;
- certify the instance-specific sharp density \(L^2/[32n(L+2e_J)]\), the exact physical sufficient C6 e³/v⁴ floor, and independent true original physical C6→six-ID D6 injection even when a winning chunk keeps only ONE original flag diagonal;
- compare historical #730 source/heavy finite outputs **only in a separate test**, not in the new production proof; additionally exhaust all 4096 bipartite K3×K4 edge sets and all seven nonempty R-subsets as an auxiliary **abstract** pigeonhole falsifier, not a replacement for the true source;
- use actual original W32/W34 lex/reverse-line, independent complete globally injected f/g cyclic shifts, arbitrary nonempty actual ORIGINAL Z sets and diagnostic small T values. These are nontrivial source tests and are not mistaken for the asymptotic heavy assumption;
- reject FIVE weakened-budget adversarial mutations: loosening source conflict cap, loosening physical n, loosening original N, dropping T below the exact ordinary C6 sufficient threshold, or inflating delta without supporting evidence.

The dedicated GitHub-hosted Ubuntu 24.04, Python 3.12 workflow runs **10 tests** and a strict unique complete JSON certificate, retains the source proof as an artifact. INDEX and FULL Research must also pass on exact final PR HEAD before engineering acceptance.

**Scientific STOP:** This slice independently proves the all-order ORIGINAL heavy *construction and graph-theorem-input implication*, as well as a sharper sufficient constant, with the actual published graph theorem applied as an **external positive-constant hypothesis**. This does not itself independently accept the entire LOW source/selector/energy proof chain, the full root #230 conclusion or an ASET exponent. Keep root issue OPEN_WITH_FORMAL_BLOCKER, PR Draft, no merge.
