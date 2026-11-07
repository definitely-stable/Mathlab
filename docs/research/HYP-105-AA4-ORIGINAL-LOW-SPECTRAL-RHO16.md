# HYP-105 #230 — AA4-LOWSPEC: independent all-order spectral third-coordinate-return lemma, genuine GQ endpoint union, 16× stronger deletion budget

**Scientific Draft strictly stacked on [#739](https://github.com/definitely-stable/Mathlab/pull/739), frozen head \`7f3f9a2392a767c6b139713338c5f6654ce1c422\`.** No parent/main changes, merges, issue closure or ASET exponent. Root remains **OPEN_WITH_FORMAL_BLOCKER**. This is a genuinely new proof/audit of the LOW original source-physical bridge under arbitrary fixed correlated globally injected f/g and adversarial ORIGINAL incidence-ID deletion; it is not a statistical extrapolation of W32/W34.

## 1. Exact universal quantifiers and original source

Let \(s=2^h\ge64\). Fix the full original symplectic GQ \(W(3,s)\), with named original point-line incidence flags \(I\); \(V=(s+1)(s^2+1)\) original points and lines; \(N=(s+1)V\) original source flags; \(a=\min\{b:\binom b2\ge V\}\) the **actual** minimal physical pair alphabet. Fix arbitrary separately globally pair-injective complete \(f:P\to\binom{[a]}2\), \(g:L\to\binom{[a]}2\), with unrestricted arbitrary correlation; maps are not randomized. Fix **any** adversarial original source flag-ID deletion set \(Z\subseteq I\) with the specified global radius; then define the actual full physical graph H using **both** true opposite diagonals of each source rectangle \(f(p)\times g(\ell)\), and the paired actual source core \(C\subseteq I\setminus Z\) using the **same original flags**.

The new proof uses the independent all-order original source SRG bound from #737, the all-order genuine heavy no-clone construction from #739 and the original selector and source inverses from #734/#738. The only external published theorem is Simonovits' ordinary graph C6 supersaturation, included in Jiang–Yepremyan (2020), DOI [10.1017/S0963548320000206](https://doi.org/10.1017/S0963548320000206). It establishes **existential**, not explicitly numerically known, positive \(C_{\mathrm{graph}},c_{\mathrm{graph}}\). Choose symbolic rational \(C_0\ge\max(1,C_{\mathrm{graph}})\), \(0<c_0\le\min(1,c_{\mathrm{graph}})\). Values used in machine arithmetic examples are *formal probes only*, not certified numerical constants of the theorem.

## 2. NEW independent ALL-GRAPH theorem: **3-step** typed-coordinate returns are controlled by 2-step returns

This is the substantive missing mathematical argument behind the previously used estimate that **coordinate-improper** physical length-three walks cost at most \(3\Delta(Q_x+Q_y)\).

Let A be the **uncut, possibly nonbipartite**, symmetric zero-diagonal adjacency matrix of the actual paired physical core \(H_C\), with \(\Delta=\max_vd_{H_C}(v)\). The spectral radius bound for an undirected graph yields \(\operatorname{spec}(A)\subseteq[-\Delta,\Delta]\). Therefore for every eigenvalue \(\lambda\),

\[
\lambda^2(\Delta-\lambda)\ge0,
\quad\text{so}\quad
\boxed{\Delta A^2-A^3=A^2(\Delta I-A)\succeq0.}
\tag{LS-1}
\]

This is **positive semidefinite for every simple undirected graph, including odd-cycle-containing, uncolored actual original cores**; it does not require a PSD adjacency matrix (A itself need not be positive semidefinite). For each first physical coordinate x let \(u_x\) be the indicator of all a physical vertices with first coordinate x. Then

\[
\sum_{u,v:\,u_x=v_x=x}(A^3)_{uv}
=u_x^\top A^3u_x
\le\Delta\,u_x^\top A^2u_x.
\]

Sum over every physical first-coordinate x. Do the same separately with true second-coordinate indicators \(v_y\). This yields

\[
\boxed{
\#\{\text{physical directed 3walks with }x_0=x_3\}
\le\Delta Q_x,\quad
\#\{\text{physical directed 3walks with }y_0=y_3\}
\le\Delta Q_y.}
\tag{LS-2}
\]

Here the **exact genuine original source-pencil two-step return books** are

\[
Q_x=2\sum_{p,y}R_C(p,y)^2
=\sum_{u,v:u_x=v_x}(A^2)_{uv},
\quad
Q_y=2\sum_{\ell,x}R_C^\vee(\ell,x)^2
=\sum_{u,v:u_y=v_y}(A^2)_{uv}.
\tag{LS-3}
\]

Proof of the source identity: an original flag (p,ell) contributes one edge at each actual physical corner \((x,y)\) with \(x\in f(p)\), \(y\in g(\ell)\), and its neighbor in that edge has the unique opposite first symbol in f(p). For any center \((x,y)\), ordered pairs of neighbors with the same first coordinate are exactly ordered pairs of original core flags through the same source point p containing the actual right physical y, hence \(R_C(p,y)^2\). Each source point label pair has two physical endpoints, giving the factor TWO. Duality gives the separate line formula, with no assumption \(f=g\) or \(Q_x=Q_y\).

For **gap-two** coordinate returns at path positions (0,2) and (1,3), each ordered 2walk with equal first OR second coordinate extends to at most \(\Delta\) 3walks by adding a physical edge on the other end. Hence these two position families together cost at most \(2\Delta(Q_x+Q_y)\). Every physical diagonal changes both typed coordinates at adjacent positions, so a 3walk with non-distinct typed coordinates must have a repeated typed coordinate at **gap 2 or gap 3** (there are no gap-1 returns). Combining with (LS-2) and the union bound:

\[
\boxed{
W_3-\sum_{u,v}P_3(u,v)
\le3\Delta(Q_x+Q_y).
}
\tag{LS-4}
\]

**Scientific trap explicitly rejected:** an x-return at gap THREE does *not* necessarily create any gap-TWO x-return on the same physical walk. Example coordinate path \((0,0),(1,1),(2,2),(0,3)\). The missing step is the spectral Loewner-order inequality (LS-1), **not** a false local combinatorial injection to a subwalk. The new finite implementation independently computes physical A²,A³, source Qx/Qy, all three return-position counts, and rejects any violation of (LS-1–4) on genuine original W32/W34 paired source cores.

## 3. NEW independent ALL-ORDER GQ count of non-Z endpoint exceptions: at most 24s⁵

For a physical endpoint pair \(((x,y),(z,w))\) with \(x\ne z,y\ne w\), its globally injected unordered pair factors are \(\{x,z\}\) and \(\{y,w\}\). Let \(B=\binom a2\), \(M=B-V\) be the exact number of missing factor pairs on EACH typed side. There are exactly four endpoint orientations for a given pair of unordered factor labels.

**Missing factor pair on either side:** exactly \(4(2BM-M^2)\le8BM\) ordered endpoints. Since \(B<a^2/2\le(9/8)s^3\) and \(M<a\le(3/2)s^{3/2}\) from the sharper true original physical envelope (#739), their total is at most \((27/2)s^{9/2}\le(27/16)s^5<2s^5\) for \(s\ge64\).

**Incident ORIGINAL q/r:** exactly \(4N\le(17/4)s^4<s^5\) ordered endpoints.

**End-bad ORIGINAL projection:** when q is not incident to r, the unique genuine GQ projection \(q-\ell-p-r\) is defined in the **FULL original GQ**. The first-factor failure \(f(p)\cap f(q)\ne\varnothing\) implies p and q are distinct ORIGINAL collinear points whose pair labels intersect. Let \(e_{\rm col}(f)\) be the actual number of unordered original collinear such point pairs with overlapping physical labels. There are \(2e_{\rm col}(f)\) ordered (q,p) pairs. For each there are **exactly s ORIGINAL outgoing r lines through p other than their common q-p line**, so at most \(2s e_{\rm col}(f)\) (q,r) projection pairs, with four physical endpoint orientations apiece: at most \(8s e_{\rm col}(f)\). The TRUE ORIGINAL line-dual second-factor end-bad set has likewise at most \(8s e_{\rm col}(g)\) physical endpoint orientations. The independent original SRG bound #737 gives

\[
e_{\rm col}(f),e_{\rm col}(g)\le C_s
=(s^2+1)(s^2+a-2)\le5s^4/4,
\]

so total end-bad endpoint union is bounded by \(8s(e_{\rm col}(f)+e_{\rm col}(g))\le20s^5\). This is **deterministic for each fixed pair of correlated maps**, not an average over f/g.

Thus, using a safe integer bound and disjoint missing/incident/end-bad categories,

\[
\boxed{e_{\rm bad,nonZ}\le24s^5.}
\tag{LS-5}
\]

**True named ORIGINAL deleted-source projection:** every genuine original flag i=(p,ell) occurs as each of THREE distinct anchor roles in exactly s² nonincident (q,r) source projections. The three independent choices are two other original points/lines of size s each; source flag roles are unchanged by physical labels. Four endpoint orientations per source (q,r) give

\[
\boxed{e_{\rm bad,Z}\le12s^2|Z|.}\tag{LS-6}
\]

Finite W32/W34 proof records enumerate the **entire** original point/line incidence GQ, all nonincident q,r and exact s² exposures of EACH actual source flag in EACH of three roles, then classify every physical endpoint into disjoint missing, incident, end-bad, deleted-projection and admissible categories. They do not require the projection's anchors to lie in a pruned C; they need only survive actual original Z.

The original proper path endpoint-energy control is consequently, using the existing all-order selector sixth moment,

\[
M_{\rm bad}\le \sqrt{(24s^5+12s^2|Z|)\|P_3\|_F^2}
\le 5q_3\lceil\sqrt{L_6}\rceil s^{11/2}
+q_3\sqrt{12L_6\rho}\,s^6.
\tag{LS-7}
\]

The two terms are split using \(\sqrt{a+b}\le\sqrt a+\sqrt b\), not an unjustified little-o estimate when \(|Z|=\rho s^4\).

## 4. NEW tight original source LOW geometric envelope, selector and mixed blocker constants

For the SAME frozen full original physical Q_T before Z as in #739, when the HEAVY case \(E_T\ge s^4/8\) does NOT occur, prune all original flags touching Q, all flags with FULL original source conflict degree \(>K=64\), and all flags in arbitrary original Z. The sharper true original source bounds \(N\ge s^4\), \(e_J\le(5/2)s^4\) show that at most \(E_T<s^4/8\) flags are Q-touching and at most \(2e_J/K\le(5/64)s^4\) exceed K. Thus if \(\rho\le3/64\),

\[
\boxed{
|C|\ge (1-\tfrac18-\tfrac5{64}-\rho)s^4
\ge\tfrac34 s^4.}
\tag{LS-8}
\]

The true CORE has BOTH physical diagonals per source flag, \(m=2|C|\le2N\le(17/8)s^4\), physical maximum degree \(\Delta\le Ts\), actual original source conflict max K, and its genuine source-pencil typed return books satisfy the exact full-flag count

\[
Q_x+Q_y\le8|C|+4e_J
\le8N+8C_s
\le\boxed{\tfrac{37}{2}s^4}.
\tag{LS-9}
\]

This improves the old \(28s^4\) return ceiling and makes the coordinate-improper threewalk penalty from the newly proved spectral lemma at most \((111/2)Ts^5\), rather than \(84Ts^5\).

**Selector selected-graph sixth moment.** If the number of surviving genuine D6 six-ID sets \(D_{6,\bar Z}<\delta s^6\le s^6\), every actual priority+both-cut selected graph has at most that many simple physical C6s via the independent true source C6 inverse #734 and selector proof #738. The independently rederived ordinary *bipartite selected* closed-walk inequality is

\[
\operatorname{tr}(A_G^6)\le24C_6(G)+72m_G\Delta^2.
\]

With \(m_G\le m\le(17/8)s^4\), \(\Delta\le Ts\),

\[
\boxed{\operatorname{tr}(A_G^6)\le
L_6s^6,\quad L_6=24+153T^2.}
\tag{LS-10}
\]

This is a strictly smaller sufficient coefficient than the inherited \(24+288T^2\); no new assumption on f/g or the random priority/cut selector was added.

**Sharper fourth.** Selected spectral Cauchy gives
\(\operatorname{tr}(A_G^4)\le\sqrt{2m_G\operatorname{tr}(A_G^6)}\le\sqrt{17L_6/4}\,s^5\). Combine with Jensen and the **exact disjoint** physical CORE proper/improper 2walk partition from #738 and (LS-9). A sufficient integer original fourth-moment constant is

\[
\boxed{
L_4^{\rm new}
=q_2^2\left\lceil\sqrt{\left\lceil17L_6/4\right\rceil}\right\rceil+19T,\quad
\operatorname{tr}(A_C^4)\le L_4^{\rm new}s^5.}
\tag{LS-11}
\]

**FULL original A/Core C mixed source books.** The independently derived #737 source \(F_1,F_2,\Theta\) bounds give, separately for actual original point and line collinearity books, \(F_1\le2G\le40s^{11/2}\) and
\[
F_2\le8(s+1)(K+1)|A|\Delta
\le8\cdot\frac{65}{64}\cdot\frac{17}{16}(K+1)Ts^6
\le9(K+1)Ts^6
\]
for \(s\ge64\), \(A=I\setminus Z\), \(|A|\le N\). Thus both original blocker books satisfy
\[
\boxed{
B_x,B_y\le B_0s^{23/4},\quad
B_0=\left\lceil\sqrt{360(K+1)T}\right\rceil.
}\tag{LS-12}
\]

By the NEW explicit source-first true-original 4-blocker injection from #737, their four physically blocked coordinate positions cost at most

\[
\boxed{D s^{47/8},\quad D=4\lceil\sqrt{B_0TL_4^{new}}\rceil.}
\tag{LS-13}
\]

## 5. New 16-unit deletion budget with a STRONGER source B/B-overlap sextic floor

The previous all-order LOW source proof spent one full sextic unit on adversarial ORIGINAL Z source projection and used the crude source alphabet \(a^2\le4s^3\), producing a leading W3 floor \(27s^6/16\). From the sharper **genuine original** alphabet \(a^2\le9s^3/4\) and the still-valid core size \(|C|\ge(3/4)s^4\), the actual **uncut, not necessarily bipartite** physical Blakley–Roy threewalk estimate instead gives

\[
\boxed{
W_3=\mathbf1^\top A_C^3\mathbf1
\ge\frac{(4|C|)^3}{a^4}
\ge\frac{27s^{12}}{(81/16)s^6}
=\frac{16}{3}s^6.
}\tag{LS-14}
\]

Choose the NEW exact source deletion radius

\[
\boxed{
\rho_{\mathrm{new}}
=\frac{16}{12q_3^2L_6},\quad
q_r=4^r\binom{r(K+1)}r\quad(r=2,3),\quad
L_6=24+153T^2.
}\tag{LS-15}
\]

The actual source deletion-masked endpoint loss in (LS-7) is now at most **FOUR** sextic units, because
\(q_3\sqrt{12L_6\rho_{\rm new}}=4\). Since \(q_3\ge1\) and \(T\ge1\), this rho is much smaller than \(1/32\) (needed in HEAVY) and \(3/64\) (needed in LOW dense core).

Define \(E=5q_3\lceil\sqrt{L_6}\rceil\),
\(D=4\lceil\sqrt{B_0TL_4^{new}}\rceil\), and exact sufficient

\[
\boxed{
s_{0,\mathrm{new}}=
\max\{64,\ 444T,\ (8E)^2,\ (8D)^8\},
\quad
h_{0,\mathrm{new}}=\lceil\log_2s_{0,\mathrm{new}}\rceil.
}\tag{LS-16}
\]

For every dyadic \(s\ge s_0\), the three remaining errors — \((111/2)Ts^5\) coordinate-improper, \(Es^{11/2}\) nondeleted endpoint, \(Ds^{47/8}\) four internal blockers — each cost at most \(s^6/8\). The deletion mask costs \(4s^6\), **not** little-o. The previous independently established genuine ORIGINAL one-sided physical proper 3path→six ORIGINAL incidence-ID B/B-overlap injection (#734), *not false surjectivity in the opposite direction*, then gives in the LOW case when \(D_{6,\bar Z}<\delta s^6\):

\[
\begin{aligned}
2BBo_{\bar Z}
&\ge\left(\frac{16}{3}-4-\frac38\right)s^6
=\frac{23}{24}s^6,\\
\boxed{BBo_{\bar Z}&\ge\frac{23}{48}s^6.}
\end{aligned}
\tag{LS-17}
\]

This is **more than three times** the previous \(5s^6/32\), while simultaneously allowing strictly more than **16 times** the prior deletion radius at fixed C0/c0 because the selected sixth moment \(L_6\) also drops from \(24+288T^2\) to \(24+153T^2\). The actual ratio
\(\rho_{\rm new}/\rho_{\#739}
=16(24+288T^2)/(24+153T^2)>16\), approaching \(\approx30.1176\) for large T. This is a stronger **deletion-resilient named ORIGINAL source sixset abundance** implication, not a new exponent.

The HEAVY branch keeps exactly #739's threshold

\[
T=\left\lceil\frac{17}{2}(370944)^3C_0^3\right\rceil,
\quad
\delta=\frac{c_0}{370944^6},
\tag{LS-18}
\]

and all its source D6/no-clone arguments, because \(\rho_{\rm new}\le1/32\). Thus **conditional on the independently named source lemmas and existential graph SS6**, for every dyadic s beyond the new sufficient s0, every complete arbitrarily correlated fixed f,g and any adversarial original \(|Z|\le\rho_{\rm new}s^4\),

\[
\boxed{D_{6,\bar Z}+BBo_{\bar Z}\ge\delta s^6},
\quad \delta=c_0/370944^6.
\tag{LS-19}
\]

More precisely: either HEAVY supplies \(D6_{\bar Z}\ge\delta s^6\), or LOW with \(D6_{\bar Z}\ge\delta s^6\) already completes, or LOW with smaller D6 supplies \(BBo_{\bar Z}\ge23s^6/48\gg\delta s^6\). The genuine original six-ID classes have disjoint source point/line degree profiles. For the **accepted six-ID full-ten balanced GF(5) signed-event sum** (as distinctly defined in #735), a conditional class-aware weighted contribution is bounded below by \(54162\,c_0\,s^6/(370944^6\,51^6)\). This last expression describes the additive accepted signed-sixset contribution; upgrading it to any differently defined union probability R3 requires an explicit separate no-overlap/linearity interface, not merely summing probabilities of overlapping events.

**No closed root #230, no numerical published SS6 constants, no new ASET exponent.**

## 6. Formal exact-rational quantitative table and independent source-level falsification

The program uses exact integer roots and Fraction, no floating point, and only three **FORMAL** graph constant probes \((C_0,c_0)\)=(1,1), (2,1/5), (7/3,1/17) that are NOT asserted to bound the actual published C_graph/c_graph.

| FORMAL C0,c0 | Prior #739 minimum dyadic h0 | New stronger LOW minimum dyadic h0 | Deletion radius relative to #739 |
|---|---:|---:|---|
| (1,1) | 818 | **810** | > 30× |
| (2,1/5) | 848 | **840** | > 30× |
| (7/3,1/17) | 854 | **847** | > 30× |

Independent true-original source finite falsifiers are implemented in [research/hyp105_original_low_spectral_rho16.py](../../research/hyp105_original_low_spectral_rho16.py), importing **only the trusted genuine symplectic source constructor and globally pair-injective map fixture generator**, no historical spectral, source-energy, selector, lowtail, GF5 or endpoint classifier.

For original W32/W34 lex and reverse-line, including **independent cyclic permutations of the complete fixed f/g maps**, actual nonempty adversarial Z and diagnostic high-Q/core T,K: independently construct full point/line GQ projection, all named ORIGINAL incidence-ID flags and their exact role exposures, classify the entire physical endpoint sample space, reconstruct paired full-Q-pruned original CORE and exact unique owned physical diagonals, compute source \(Q_x,Q_y\) and independently from physical A², compute actual physical A³ coordinate 3-return and PSD upper for EACH coordinate, and enumerate all physical directed length-3 walks and all three improper return positions. A second direct path-first oracle decodes the full GQ q--ell--p--r and actual Z-avoiding six ORIGINAL source-ID BBo sixsets, checking the two reversed physical 3path representations and recording ORIGINAL projection anchors outside the smaller C. A separate TEST ONLY validates produced original sixsets against the previous frozen historical GF5 seven-family classifier (not used to derive any bound).

The tests include a deliberately small abstract P4 coordinate path with x0=x3 but no gap2 return on that path; this forces rejection of an erroneous combinatorial gap3→gap2 subwalk argument. The rigorous all-h estimate relies instead on the spectral operator inequality (LS-1). All finite results serve as **falsifiers of the exact derivations**, never as a substitute for the all-h spectral/GQ proofs.

Dedicated GitHub-hosted Ubuntu 24.04 Python 3.12 CI runs **12 tests**, strict unique machine JSON with the three formal exact source ledgers, true original full projection classification and independent PSD/physical threewalk certificates. INDEX and full Research must be checked on the **same final PR HEAD** before engineering acceptance. Older Drafts and main remain untouched.

**NEXT SCIENTIFIC GATE:** an adversarial **global root proof acceptance review** must reconcile exact sixset additive GF(5) signed-event counting against the precise definition of risk \(R_3\), plus independently audit the source selector→four blocker→six-ID inverse under all quantifiers. The proofs above do not silently equate an expected count of signed-sixset events to a probability of their union. Root #230 remains OPEN_WITH_FORMAL_BLOCKER.
