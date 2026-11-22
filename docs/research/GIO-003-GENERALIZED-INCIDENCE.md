# GIO-001.3 — field-free obstruction and adversarial deletion on balanced generalized quadrangles

**Program:** [#790](https://github.com/definitely-stable/Mathlab/issues/790), target [#793](https://github.com/definitely-stable/Mathlab/issues/793). **Frozen already-integrated foundation:** [#230 two-class source theorem](HYP-105-AA4-BRANCH-A-INTEGRATED-TWO-CLASS-PROOF.md), [#791 source-deletion resilience](GIO-001-RESILIENCE.md), main \`f4355154ee70ea6d776b1b5f320c2e174238603c\`. This manuscript is a **new mathematical proof candidate** conditional on one **explicitly named published graph theorem**; it is not administrative acceptance, external independent peer review, Lean certification, proof of the open generalized ASET conjecture, or an existence claim for arbitrary GQ parameters. See the companion \`research/gio_generalized_gq.py\` and independently constructed genuine finite geometry fixtures.

## 1. Stronger T1/T2 statements with the correct quantifiers

Fix an **integer** b≥1 BEFORE the geometry (for any real requested balance B≥1, use b=ceil(B)). Let \(\mathcal Q\) be an arbitrary *existing finite thick generalized quadrangle* of order (s,t), meaning every line contains s+1 points, every point belongs to t+1 lines, a pair of distinct points lies on at most one common line, and every nonincident (point q,line r) has a **unique** point p of r collinear with q and an associated unique line ell joining q and p. The dual GQ axioms then also hold. Put

\[
r=\min(s,t),\qquad r\le s,t\le br,
\quad V_P=(s+1)(st+1),\quad V_L=(t+1)(st+1),
\quad N=(s+1)(t+1)(st+1).
\]

Each original *flag* (p,l) is a distinct named source ID in the N-element set I. Let

\[
a_P=\min\{a:\binom a2\ge V_P\},\quad
a_L=\min\{a:\binom a2\ge V_L\}.
\]

Fix arbitrary *complete*, globally injective point-label map f:P→\(\binom{[a_P]}2\) and line-label map g:L→\(\binom{[a_L]}2\), with completely unrestricted dependence/correlation. For arbitrary original flag deletion Z⊆I define A=I\Z. Retain the exact historical *distinct original six-ID* D6 and B/B-overlap definitions from #230, including their source-type multiplicities, physical dual-edge motifs, and independently sampled 51-pattern GF(5) coefficient palette. Define BBo_prod(A) as only **constructively produced aligned original BBo** sixsets from actual three-edge physical paths together with all three genuinely surviving FULL-GQ projection anchors; this is a subset of historical BBo(A).

**Theorem GQ-B, stronger than targets T1 and T2.** For each fixed integer b≥1 there exist *positive absolute-with-respect-to-the-GQ* rational constants \(\rho_b,\delta_b>0\) and integer \(r_{0,b}\), determined only by b and the external ordinary C6 graph supersaturation constants, such that for **every actual GQ(s,t)** with r≥r0,b and max(s,t)≤b r, for **every** admissible fixed f,g and every adversarial Z⊆I with

\[
|Z|\le \rho_b r^4,
\qquad
D6_A(f,g)+BBo_{\mathrm{prod},A}(f,g)\ge\delta_b r^6.
\]

Consequently the same lower bound holds for D6+BBo_historical. This statement is nonvacuous for any infinite existing balanced GQ family; we do **not** assert a GQ exists for every (s,t). In particular b=1 handles **every existing equal-order GQ(s,s)** in *any* characteristic and even any nonclassical isomorphism type for large s, no dyadic restriction whatsoever. s=t finite small orders may fail the lower count without contradicting the theorem.

**Packing and coefficient consequence:** Under the exact same fixed f/g, at least floor(\(\rho_b r^4/6\))+1 pairwise original-flag-disjoint sixsets of historical D6 or *produced aligned* BBo exist. Uniform independent 51-pattern checksum-four GF(5) coefficients admit a prechosen sign event of probability ≥5175/51^6 per such sixset. Let m be the packing size and X the number of these realized selected events. Then

\[
\Pr[X < 5175m/(2\cdot51^6)]
 \le \exp[-5175m/(8\cdot51^6)] = \exp[-\Omega_b(r^4)].
\]

All independence is on **disjoint named source coefficient IDs**, not f/g, not physical coordinate pairs, not labels after deletion, and not a dependent-coefficient ASET construction.

## 2. Pure GQ geometry: no field representation in any inherited lemma

The point collinearity graph of GQ(s,t) is strongly regular with

\[
(v,k,\lambda,\mu)_P=((s+1)(st+1),\,s(t+1),\,s-1,\,t+1),
\]

with nontrivial adjacency eigenvalues s−1 and −(t+1). The line collinearity graph is the genuine dual GQ(t,s), hence

\[
(v,k,\lambda,\mu)_L=((t+1)(st+1),\,t(s+1),\,t-1,\,s+1).
\]

These are immediate from the actual GQ projection axiom: adjacent points share s−1 other points on their unique line, and every line through a noncollinear point has exactly one projected collinear point. The adjacency identity is

\[
M_P^2=(s-1)(t+1)I+(s-t-2)M_P+(t+1)\mathbf 1\mathbf 1^\top
\]

and the dual swaps s,t. Importantly \(\lambda-\mu=s-t-2\), so **the exact equal-order \(-2M\) shortcut in #230 may NOT be transplanted unchanged** to GQ(s,t). This is the primary unequal-order proof hazard.

The full real simple physical graph H has vertices [a_P]×[a_L] and exactly two opposite rectangle diagonals per source flag. Complete injectivity of f and g makes every physical edge have a unique original flag owner. The original conflict graph J on flags has edges when two owners share the original point and their g-pairs intersect, or share the original line and their f-pairs intersect. These kinds are disjoint. Exactly

\[
e(J)=e_{\mathrm{col},P}(f)+e_{\mathrm{col},L}(g).
\]

The positive nontrivial eigenvalue bounds any physical symbol fibre S of d injected original factors by \(2e_{\mathrm{col}}(S)\le (k-\theta)d^2/V+\theta d\). For the point graph k−θ=st+1, θ=s−1; for the line graph k−θ=st+1, θ=t−1. Since each physical symbol occurs in at most (a−1) injected pairs and \(\sum d=2V,\sum d^2\le2V(a-1)\),

\[
e_{\mathrm{col},P}(f)\le(st+1)(a_P-1)+(s-1)V_P,
\]
\[
e_{\mathrm{col},L}(g)\le(st+1)(a_L-1)+(t-1)V_L.
\]

They need no automorphism symmetry or random-map independence. Every physical x/y corner graph identity and the unique original source sixset inverse from #230/#791 uses only this incidence structure, unique GQ projection, source girth ≥8 and injectivity—not the coordinates of a symplectic form or s a power of two. The independent GF(5) palette likewise does not require characteristic five of the GQ.

## 3. Conservative uniform integer envelopes in the fixed-balance regime

All inequalities below hold for integral r≥1, s,t∈[r,br]. To avoid invented sharp constants define

\[
v=(b+1)^3,\quad n=(b+1)^4,\quad
a_0=2v+2,\quad A_0=a_0^2,
\quad j_0=(b^2+1)a_0+bv,\quad J_0=2j_0.
\]

Elementary estimates: V_P,V_L≤v r³, r⁴≤N≤n r⁴, and minimal pair alphabet satisfies a_P,a_L≤a0 r^(3/2) (because a<sqrt(2V)+2). Hence physical corners nphys=a_Pa_L≤A0 r³. The preceding typed SRG fibre bounds imply

\[
e_{\mathrm{col},P},e_{\mathrm{col},L}\le j_0 r^4,
\qquad e(J)\le J_0 r^4.
\]

The asymmetry of a_P,a_L is real: all subsequent proofs use **their product**, never incorrectly set a_P=a_L when s≠t. Restricting to a surviving C does not enlarge e(J_C), full physical degrees or old collinearity energies.

Fix a conservative cap rho_cap=1/32 and a rational external pair C0≥max(1,C_graph), 0<c0≤min(1,c_graph), where C_graph,c_graph are the **existential** constants in the **ordinary graph** Simonovits C6 supersaturation theorem as quoted by Jiang–Yepremyan, *Combinatorics, Probability and Computing* 29 (2020), 698–721, DOI [10.1017/S0963548320000206](https://doi.org/10.1017/S0963548320000206). For ordinary simple F with e(F)≥C_graph v(F)^(4/3), at least c_graph(e(F)/v(F))^6 unoriented simple C6 occur; the chosen constants may absorb normalization. No numerical graph constants are claimed. The numerical examples C0=1,c0=1 in the companion ledger are **formal demonstrations only**, not necessarily admissible for the published theorem.

Define once

\[
K=16J_0+1,\quad c=1/2,\quad
R=512A_0(1+64J_0),\quad
T=\lceil8nR^3 C_0^3\rceil,\quad w=(4c)^3/A_0^2=8/A_0^2.
\]

All depend only on b and C0; not on actual r,s,t,\(\mathcal Q\), f/g, or Z. In particular rho_cap is an *a priori bound* for the proof architecture, not the resilience radius eventually claimed.

## 4. HEAVY — genuine C6 and original D6 survive arbitrary source deletion

Freeze Q_T={physical corner x:d_H(x)>Tr} in **FULL H**, before deletion, and E_T the number of distinct actual physical edges touching Q_T. In HEAVY E_T≥r⁴/8. Removing any |Z|≤rho_cap r⁴ original flags removes at most 2|Z| actual real edges. Therefore the surviving named-owner set L has

\[
|L|\ge E_T/2-|Z|\ge r^4/32.
\]

Caro–Wei on J[L], with full e(J)≤J0 r⁴, supplies an independent actual-owner set I0 with

\[
|I_0|\ge \frac{|L|^2}{|L|+2e(J[L])}
       \ge \frac{r^4}{32(1+64J_0)}.
\]

Choose a single coherent fair bit for each physical first symbol and a single coherent fair bit for each second symbol. Some two cuts preserve whole (both real diagonals) of at least |I0|/4 of these independent owners. Each has a surviving real edge touching frozen Q_T. One heavy endpoint per owner and one first-bit class provides at least |I0|/8 distinct real U–Y edges, with U⊆Q_T and U∩Y=∅. Keeping the top min(|U|,|Y|) genuine opposite-bit neighbors yields an actual simple bipartite F, no clones or random-map symmetry, with

\[
e(F)/v(F)\ge |I_0|/(16a_Pa_L)>r/R,
\qquad
v(F)\le2|Q_T|<8N/(Tr)\le 8n r^3/T
 \le(r/(RC_0))^3.
\]

This is enough for the published ordinary graph theorem. Every selected C6 has separately six distinct physical x and y symbols: cyclic gaps 1 change both, gap 2 repetition would mean a source J conflict, gap 3 repetition is forbidden by the two global cut parities. Consecutive owner pair-label intersections force the physical corners uniquely, hence a simple C6 injects into a **surviving** original six-ID historical D6. No s=t or symplectic field assumption is used. Thus in HEAVY \(D6_A\ge c_0 r^6/R^6\).

## 5. LOW — one core and one global selector

In LOW E_T<r⁴/8. Discard from FULL I all deleted original owners Z, all owners touching frozen heavy edges, and all FULL-J owners whose J degree exceeds K. The residual **paired** original owner core C obeys

\[
|C|> [1-1/8-\rho_{\rm cap}-2J_0/(K+1)]r^4
> c r^4=r^4/2.
\]

Every actual physical degree of H_C is ≤Tr and every J_C degree ≤K. The degree-biased oriented-edge Jensen bound (valid without bipartiteness) gives total ordered three-walks

\[
W_3(H_C)\ge (4|C|)^3/(a_Pa_L)^2 > w r^6.
\]

If D6_A≥δr⁶ already, stop. Otherwise D6_A<δr⁶≤r⁶. Use ONE common independent random priority on every named surviving C-owner; keep J_C local minima. Independently cut *all* first and second physical symbols globally. Proper two-/three-edge paths (their typed symbols all distinct separately) survive with probability at least 1/q_i where \(q_i=4^i(K+1)^i\); shared-neighbor overlap is handled by the same conditional product inequality and Jensen as the accepted #230 proof. No independence between path events.

Let P_i be ordered endpoint matrices of proper i-walks in H_C, and G the SAME selected bipartite graph. Then \(\|P_i\|_F^2\le q_i^2 \mathbb E\,{\rm tr}\,A_G^{2i}\). A selected simple C6 has a unique original D6 owner set and, for that source cycle, both coherent typed cuts succeed with probability exactly 1/1024 before priority filtering. Therefore \(\mathbb E C_6(G)\le D6_A/1024\). The closed-six-walk reversal calculation (valid for simple bipartite G) gives

\[
\mathbb E\, {\rm tr}A_G^6
 \le \frac3{128}D6_A+36(Tr)^2 W_C,\quad
 W_C=\sum_{i\in C}(1+d_{J_C}(i))^{-1}\le N\le n r^4.
\]

Set

\[
q_2=16(K+1)^2,\quad q_3=64(K+1)^3,\quad
L_6=1+\lceil36nT^2\rceil,\quad Q_0=8n+4J_0.
\]

In the underlying uncut C, the exact original coordinate-return identity is STILL \(Q_x+Q_y=8|C|+4e(J_C)\le Q_0r^4\); it relies solely on source-owner incidence and injectivity. Hence

\[
\|P_3\|_F^2\le q_3^2L_6r^6,\qquad
\|P_2\|_F^2\le q_2^2\sqrt{nL_6}\,r^5,
\quad {\rm tr}A_C^4\le L_4r^5,
\quad L_4=q_2^2\lceil\sqrt{nL_6}\rceil+Q_0T.
\]

The two gap-two coordinate returns and one gap-three PSD \(A_C^2(Tr I-A_C)\) return bound charge at most \(I_{\rm improper}\le3TQ_0r^5\). There is **no assumption that A_C itself is bipartite**.

## 6. LOW outer endpoints, including the new unequal deletion coefficient

An ordered off-coordinate pair of physical corners gives one original point pair f(q) and one original line pair g(r), if those pairs occur in the complete typed maps. A missing typed pair contributes at most

\[
4(M_PV_L+M_LV_P+M_PM_L)
 \le4(2a_0v+a_0^2)r^5,
\]

where \(M_P=\binom{a_P}2-V_P<a_P\), \(M_L=\binom{a_L}2-V_L<a_L\). Incident original q–r endpoints contribute exactly 4N≤4nr^5. For nonincident q,r the true original unique projection q–ell–p–r exists. If endpoint q has f(q) intersecting f(p), charge at most 8t\,e_col,P(f) ≤8b j0 r^5; if g(r) intersects g(ell), charge at most 8s\,e_col,L(g) ≤8b j0 r^5. Thus the **unchanged original** bad endpoint mask has size ≤\(E_0r^5\), for

\[
E_0=4(2a_0v+a_0^2)+4n+8bJ_0.
\]

For actual adversarial flag deletion Z, a single original flag (p,ell) can occur in a nonincident **unique GQ projection triple** as (q,ell), (p,ell), or (p,r). There are exactly \(st\) original nonincident (q,r) projections in **each** position: s other points on ell times t other lines through the projected point, or dual. The position sets are pairwise disjoint for that flag because the three anchors are distinct in a simple girth-eight source. Hence one flag appears in exactly 3st FULL projection triples, and any deletion Z invalidates at most \(3st|Z|\) projected nonincident pairs, or \(12st|Z|\le12b^2\rho r^6\) ordered physical endpoint pairs. **Using \(3s^2\) from the equal case here would be false.**

Cauchy with P3 gives

\[
I_{\rm endpoint}\le q_3\sqrt{L_6(E_0/r+12b^2\rho)}\,r^6
\le E r^{11/2}+q_3\sqrt{12b^2\rho L_6}\,r^6,
\quad E=q_3\lceil\sqrt{E_0L_6}\rceil.
\]

The second summand has leading order r⁶ and cannot be discarded asymptotically. Actual available anchors need only be in A=I\Z, **not** in the smaller low-degree C. FULL-GQ projections are not recomputed on the damaged incidence system.

## 7. LOW mixed FULL-A/CORE-C books and the unequal SRG Gram correction

The four possible inner blockers (two typed sides × two positions) use the exact three-corner **triple** injection from the frozen #230 proof, with actual nonnegative FULL-A/CORE-C book K_AC (not a false full-path injection). Deletions only decrease the A-side source book; it is upper-bounded by FULL-I. The C-side degree/owner weights are monotone and \(\Theta=\sum_{\rm physical\ corner}d_Hd_{H_C}\le4NTr\). As in #230, the first inner x book satisfies

\[
B_x^2\le16(t+1)(K+1)N(Tr)\,G_f,
\]

where \(G_f=\sum_{x,p}c_x(p)^2=\sum_x\|\!M_P1_{f^{-1}(x)}\!\|_2^2\) and the point-adjacency matrix identity from Section 2 yields EXACTLY

\[
G_f=2V_P(s-1)(t+1)
    +2(s-t-2)e_{\mathrm{col},P}(f)
    +(t+1)\sum_x d_x^2.
\]

The middle term is of **either sign** and is **not** \(-4e_{\rm col}\) unless s=t. Using \(\sum_x d_x^2\le2V_P(a_P-1)\), \(s,t\le br\), \(V_P\le vr^3\), \(e_{\rm col}\le j_0r^4\), we obtain

\[
G_f\le g_0 r^{11/2},\quad
g_0=2vb(b+1)+4(b+1)j_0+2(b+1)va_0.
\]

The line-side proof is the true dual \(s\leftrightarrow t\), with the same bound \(G_g\le g_0r^{11/2}\). It follows that for both inner book types

\[
B_x^2,B_y^2\le16(b+1)ng_0(K+1)T\,r^{23/2}.
\]

Let \(B_0=\lceil\sqrt{16(b+1)ng_0(K+1)T}\rceil\) and \(D=4\lceil\sqrt{B_0TL_4}\rceil\). Counting the missing middle two-walk via the original Cauchy/Gram argument gives

\[
I_{\rm fourblockers}\le D r^{47/8}=o(r^6).
\]

This is the exact mixed source-book place where a casual equal-order copy/paste would have invalidated the proof.

## 8. Uniform closure: positive rational deletion radius and original six-ID lift

Set \(\varepsilon=w/8\) and freeze, only **AFTER** choosing b,C0,c0,R,T,K and all moment constants,

\[
\rho_b=\min\left\{\frac1{32},
      \frac{\varepsilon^2}{12b^2q_3^2 L_6}\right\}>0,
\qquad
\delta_b=\min\left\{\frac{c_0}{R^6},\frac{w}{4}\right\}>0,
\]

\[
r_{0,b}=\max\{2^{32},
   \lceil3TQ_0/\varepsilon\rceil,\,
   \lceil(E/\varepsilon)^2\rceil,\,
   \lceil(D/\varepsilon)^8\rceil\}.
\]

The companion program enforces all four integer-power inequalities with exact rational arithmetic. For every integral r≥r0,b, the four LOW error terms—improper, original endpoints, deleted projection anchors and four mixed blockers—are **each** bounded by \(\varepsilon r^6\), totaling ≤(w/2)r⁶. In LOW with D6_A<δ_b r⁶, at least (w/2)r⁶ genuine original proper paths survive the tests. The three residual source flags are in C⊆A; the three unique original anchor flags are in A; every source ID is distinct and the repeated original point/line share the middle original flag. The frozen field-free source inverse shows two reverse directed paths per produced aligned BBo unordered sixset, or zero for other sixsets. Thus BBo_prod,A>(w/4)r⁶≥δ_b r⁶. In HEAVY D6_A≥c0 r⁶/R⁶≥δ_b r⁶. These cases are exhaustive on the SAME r,s,t,GQ,f,g,Z, with no interchange of expectation and infimum.

**The field-free proof is stronger than T1/T2:** it also tolerates any \(|Z|\le\rho_b r^4\) adversarial original incidence deletion for all *existing balanced* GQ(s,t). The corollaries in Section 1 use greedy **named source** removal and independence of independent original GF5 coefficient columns, not geometry automorphism distributions. T1 follows by setting b=1; the original #230 dyadic s condition is an artifact of its chosen symplectic fixture, not a hypothesis in these incidence arguments.

## 9. Finite independent falsifiers (not all-order proof)

The exact companion code generates:

- **W(3,2)** independently from isotropic projective 2-spaces in PG(3,GF2).
- **W(3,3)** independently from isotropic projective 2-spaces in PG(3,GF3), a non-dyadic odd-characteristic genuine GQ(3,3).
- **Q⁻(5,2)** as the 27 singular points and 45 totally singular 3-point projective lines of the nondegenerate minus-type quadratic form \(x_0^2+x_0x_1+x_1^2+x_2x_3+x_4x_5=0\) in PG(5,2): a genuine **unequal** GQ(2,4).
- **The actual dual** of this Q⁻ incidence structure: GQ(4,2), to test full point/line asymmetry.
- The independently constructed original W(3,4) fixture from #230 for further true classical comparison; full original W34 heavy census is already tested in #791, so only a bounded named subset is enumerated in the new independent source/physical crosscheck.

For each true geometry, code reconstructs exact incidences and checks **every** nonincident point-line unique projection, s+1 points/line, t+1 lines/point, no duplicate original point pairs on lines and BOTH SRG common-neighbor matrices. This rejects accidentally substituting an abstract SRG or false synthetic incidence fixture.

On separate point and line alphabets and lex/reversed/correlated actual maps, original conflict J is enumerated directly from flags and independently compared with both typed collinearity counts. The **unequal** SRG Gram identities for G_f/G_g are reconstructed by direct integer summation over point/line symbol fibres, rather than taking the symmetrical -4e identity on faith. Actual original D6 and produced BBo sixset sets are obtained by (1) physical simple-cycle DFS versus (2) original owner-corner DFS, and (3) physical proper-path traversal versus (4) original middle-owner join/source inverse. Genuine deletion masks compare original source-family filtering to physical surviving-owner reconstruction. Per-deleted-flag three-position projection enumeration is compared to direct unique FULL anchor testing, including both dual GQ(2,4) and GQ(4,2); a singleton has **exactly 3st** damaged nonincident projections and 12st ordered endpoint orientations. A bounded finite disjoint-packing builder and direct GF5 nonzero dual edge flow table complete the falsifiers.

The finite models support, but never prove, the eventual all-order statement. Rational ledgers with sample \((C_0,c_0)=(1,1)\) etc are explicitly FORMAL and should not be quoted as actual effective graph supersaturation constants. The **scientific acceptance gate** is an independent critical review of this whole proof (especially unequal SRG middle term, books, and C6 source inverse), exact HEAD hosted specialist+Research+INDEX, then guarded narrow merge and postmerge main Research. Until then, #793 stays OPEN; T3 (abstract incidence beyond GQ axioms) remains OPEN regardless of outcome.
