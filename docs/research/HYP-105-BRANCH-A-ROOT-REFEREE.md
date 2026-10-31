# HYP-105 #230 — AA4-ROOTREF: independent end-to-end Branch A audit and 2^58 dyadic root certificate

**Scientific Draft / proof referee, not external peer acceptance.** Stacked ONLY on frozen [#685](https://github.com/definitely-stable/Mathlab/pull/685), parent `5960497137f4eb9983b5f4b93a9e176852ed9195`. Re-examines published external SS6 graph input, exact ORIGINAL source-degree/conflict books, all complete correlated injections, physical-to-D6 and proper-path-to-B/B source IDs, FULL physical versus ORIGINAL core distinctions, four internal blocking positions, and all constants through the final ROOT disjunction. No claim of a real published numerical `C,c`, no merge, no external referee impersonation, and no ASET exponent.

## 1. Precise assertion and provenance boundary

For every integer `h>=1`, `s=2^h`, the **genuine symplectic generalized quadrangle** `W(3,s)` has `V=(s+1)(s²+1)` original point and line factors and `N=V(s+1)` actual source incidence flag IDs. Fix ANY legal complete separately injective physical pair maps `f:P->E(K_a)`, `g:L->E(K_a)`, with `a` minimal for `binom(a,2)>=V`; **arbitrary correlation** is allowed. For every flag (p,ell), retain its genuine original ID and both opposite-corner physical diagonals on `[a]²`.

The root statement (for sufficiently large h), given the explicitly cited external SS6 input and original GF5 classifier, is

\[
D_6(f,g)+U_{BB,\mathrm{overlap}}(f,g)\ge\delta s^6,
\qquad
\delta=\min(1/8,c_{\rm graph}2^{-108})>0.\tag{R1}
\]

All motifs count unordered **six distinct ORIGINAL flag IDs**, the same six IDs on each typed physical projection. Every statement is uniform in both fixed maps; auxiliary random selectors are applied *after* fixing them.

This manuscript is an **independent derivation/check of the logical composition and inequalities**. Inputs requiring third-party verification are called out, not silently promoted: (i) the classical balanced C6 supersaturation theorem with existential constants C,c; (ii) the standard genuine W(3,s) GQ incidence, eigenvalues, and source factor geometry; (iii) the historical GF(5) 51-column positive motif classifier, including the accepted D6 and B/B-overlap original six-ID classes. The independent W32/W34 oracle checks source factor *profiles and provenance*, not the complete 51-palette Fourier positivity proof. Hence this is NOT claimed to be qualified external peer review or final issue acceptance.

## 2. EXTERNAL theorem confirmed and exactly applicable

T. Jiang and L. Yepremyan, *Supersaturation of even linear cycles in linear hypergraphs*, Combinatorics, Probability and Computing 29(5), 698–721 (2020), DOI **10.1017/S0963548320000206**, explicitly states the graph case of Simonovits' theorem, including the `r=2` proof: for some absolute positive **unspecified** `C_graph,c_graph`, every *ordinary finite simple* graph `F` satisfying `e(F)>=C_graph*v(F)^(4/3)` has at least `c_graph*(e(F)/v(F))^6` **ordinary simple unoriented C6** copies. This is the balanced `k=3` statement, not an unproved unbalanced conjecture.

Source: https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/supersaturation-of-even-linear-cycles-in-linear-hypergraphs/240493C1F42618819DA9B16CE7F3E4BD

**Limits:** no assertion that `C=c=1` are actual constants; no explicit actual numerical threshold h0. We take arbitrary actual positive constants satisfying the theorem and prove a finite *symbolic* threshold. The independent implementation accepts only positive rational trial constants for exact falsification; existential real C,c require only the analytic argument.

## 3. Source ID integrity and a sharper heavy-tail dichotomy

Every original flag yields exactly two distinct physical edges and every physical edge uniquely determines its original f(p),g(ell), hence a unique original incidence ID. Thus the FULL H has exactly `2N` simple physical edges, `sum_v deg_H(v)=4N<=8s⁴` for `s>=64`. Set

\[
Q_T=\{v:\deg_H(v)>Ts\},\quad
E_T=\#\{\text{distinct FULL H physical edges touching }Q_T\}.
\]

Then `|Q_T|<=8s³/T`. Fix any `epsilon>0`, and call an ORIGINAL flag heavy if at least one of its two diagonals is counted by `E_T`. There are at least `L>=E_T/2` heavy original ID flags. For the true original source-book pencils,

\[
M_f,M_g\le C_s=(s²+1)(s²+a-2)<(3/2)s⁴\quad(s\ge64).
\]

**Independent derivation of the pencil-book constant, not an assumed random-map collision estimate.** Let B be the genuine point-line incidence matrix of W(3,s); its squared singular spectrum is d², 2s, 0 with d=s+1. For any ORIGINAL line-star L_y of size k_y (line factors whose physical g-label contains coordinate y), decompose 1_(L_y) into its constant part and orthogonal complement, obtaining ||B 1_(L_y)||² <= 2s k_y+(s²+1)k_y²/V. Separate global injection gives k_y<=a-1, sum_y k_y=2V, sum_y k_y²<=2V(a-1). Hence
`2M_g =sum_y||B1_(L_y)||²-2Vd <= 4sV+2(s²+1)(a-1)-2Vd`, so
`M_g<=(s-1)V+(s²+1)(a-1)=C_s`. The ORIGINAL point-star dual proves `M_f<=C_s` without independent f/g assumptions.

The ORIGINAL source-ID conflict graph has exactly `M_f+M_g<=2C_s` edges. Caro–Wei gives a nonconflicting original-flag subset of size at least `L²/(4C_s+L)`; two conditional-expectation bichromatic cuts retain at least one quarter with **both diagonals per ID**. For `E_T>=epsilon*s⁴`, the resulting selected graph contains at least `beta*s⁴` genuinely original flags and as many distinct heavy *witness edges*, `beta=epsilon²/2⁷`. It is a real simple physical graph G, and the conflict-free + two-cut construction ensures every simple physical C6 is coordinate-proper, has six distinct original IDs and produces an accepted ORIGINAL D6 sixset; different C6s have different sixsets.

**Explicit inverse for source-ID injectivity of physical C6.** A coordinate-proper physical sixcycle supplies six pairwise distinct ORIGINAL point IDs and six pairwise distinct ORIGINAL line IDs. The six f-pair labels form a single simple cycle on six distinct left coordinate symbols, and the six g-pair labels form one on six distinct right symbols. If the same ORIGINAL sixset produced another physical C6, its ORIGINAL flags prescribe exactly the same labeled edge sets in BOTH typed sixcycles; the consecutive original point-pair edge order of a simple C6 is unique up to cyclic rotation and reversal. The given original flag-to-line pairing then determines each simultaneous right-edge intersection uniquely. Therefore the two physical cycles coincide as unoriented undirected cycles. In particular the apparent two physical diagonals per flag create no extra multiplicity: the flag assignment plus the two coordinate C6s uniquely determine the selected physical cycle.

Assign witness endpoints to the FULL-H heavy Q_T. Half have heavy endpoints on the same one of two physical bipartite sides X. Put `R=Q_T intersect X`, `r=|R|<=8s³/T`, and partition the actual opposite side Y into at most `2n/r` chunks of size <=r (where `n=a²<=4s³`). A winning actual un-cloned subgraph `F=G[R,Y*]` satisfies

\[
e(F)\ge \beta r s/16,\qquad v(F)\le 16s³/T,
\qquad e(F)/v(F)\ge \beta s/32.\tag{R2}
\]

Therefore **the improved source-backed #684 criterion**

\[
T\ge 2^{40}C_{\rm graph}^3\epsilon^{-6}\tag{R3}
\]

makes F eligible for published balanced SS6. It gives

\[
D_6\ge \#C_6(F)\ge c_{\rm graph}\epsilon^{12}s^6/2^{72}.\tag{R4}
\]

The F subgraph may drop the second physical diagonal of an ID, but every retained edge still belongs to G with valid ORIGINAL provenance; applying SS6 to F does not require F itself to preserve complete ID pairs.

**ROOT fork:** fix `epsilon=1/8`, `T=max(1,ceil(2^58*C_graph^3))`, `delta=min(1/8,c_graph*2^-108)`. If `D6>=delta s6` we are done. Otherwise by the contrapositive of (R4) **for the SAME f,g** we have `E_T<s4/8`. The actual numerical `C_graph,c_graph` remain unspecified.

## 4. ORIGINAL dense core, source conflicts, and selector transfers

Delete entire original source ID flags touching the FULL heavy set; at most `E_T<s4/8` IDs are deleted. Remove any ORIGINAL flag whose degree in the full original source conflict graph exceeds `K=64`; this removes at most `4C_s/K<3s4/32` flags. Let I be the remaining genuine ORIGINAL flag core, with paired physical H0 and adjacency A0. The original FULL GQ projection anchors may lie outside I. Then

\[
N_0=|I|\ge N-7s⁴/32,\qquad
s⁴\le m_0=2N_0\le4s⁴,\quad
\Delta(H_0)\le Ts,\quad
\Delta_{\rm original\ conflict}(I)\le64.\tag{R5}
\]

For a fixed coordinate-proper physical r-path (`r=2,3`) in H0, its r original ID flags are pairwise nonconflicting. Assign uniform independent continuous priorities to original core IDs and retain the local minima. The events for the r target ID flags are NOT independent. Conditioned on their priority vector t, shared outside neighbors require priority >max of adjacent targets; multiplying these conditional probabilities and using `1-max(t_i)>=product_i(1-t_i)`, then integrating, gives a joint selection probability at least `(K+1)^(-r)`. Two independent coordinate bichromatic cuts retain the specific proper path with exact probability `4^(-r)`. Therefore

\[
\sigma_2=1/[16\cdot65²],\qquad
\sigma_3=1/[64\cdot65³].\tag{R6}
\]

For EVERY selector outcome G, every physical C6 is ORIGINAL D6, so `C6(G)<=D6<s6`. For a bipartite simple adjacency A_G, the elementary backtrack bound and spectral Cauchy give

\[
\begin{aligned}
\operatorname{tr}(A_G^6)
&\le12C_6(G)+6\Delta\operatorname{tr}(A_G^4),\\
\operatorname{tr}(A_G^4)^2
&\le2m_G\operatorname{tr}(A_G^6),\\
\operatorname{tr}(A_G^6)
&\le24C_6(G)+72m_G\Delta²
\le L_6s⁶,\qquad L_6=24+288T².
\end{aligned}\tag{R7}
\]

For every endpoint pair, expectation of the selected graph's length-r walk count is at least sigma_r times the fixed H0 coordinate-proper count P_r. Jensen on squared entries and symmetry give

\[
\|P_3\|_F²\le\sigma_3^{-2}L_6s⁶,\quad
\|P_2\|_F²\le\sigma_2^{-2}\sqrt{8L_6}s⁵.\tag{R8}
\]

These are first-moment inequalities on individual path survival, **not** unjustified independence of different paths.

## 5. Proper length-three walks with genuine endpoint provenance

Let `R0(p,y)` be the number of retained ORIGINAL flags at point p whose line label contains physical right coordinate y. Define core pencil books `Mf(I),Mg(I)`. Exact original count of improper physical two-walks is

\[
\sum_{u,v}B_2(u,v)=4N_0+4(M_f(I)+M_g(I)).
\tag{R9}
\]

Why: first-coordinate two-step returns count `4N0+4Mg(I)`; second-coordinate returns `4N0+4Mf(I)`; their overlap is exactly the physical backtracking `u-v-u` of size `2m0=4N0`, counted once. Each B2 cell is at most Delta. Since N0<=2s4 and Mf+Mg<=3s4,

\[
\operatorname{tr}(A_0^4)
=\|P_2+B_2\|_F²
\le L_4s⁵,\quad
L_4=2\sigma_2^{-2}\sqrt{8L_6}+40T.\tag{R10}
\]

The standard length-three walk convexity inequality on n physical vertices gives
`1^T A0^3 1 >= (2m0)^3/n² >=s6/2`. Initial/final improper 2-step returns and distance-three coordinate returns cost at most `68Ts⁵` by the exact original source books, not by a false assumption that H0 is bipartite. Consequently

\[
\sum_{u,v}P_3(u,v)\ge s⁶/2-68Ts⁵.\tag{R11}
\]

For all physical ordered first/last vertices `(x,y),(z,w)` with x≠z,y≠w, put `M=binom(a,2)`. There are exactly `4M²` possible physical endpoint cells. The ORIGINAL GQ source partitions these disjointly into missing physical pair labels; incident ORIGINAL q,r; original nonincident source-end bad; original nonincident source-end good. Let J be the ACTUAL intersection of left/right end-bad original q,r and let Mf,Mg be FULL original pencil books:

\[
E_{\rm exceptional}
=4(M²-V²)+4N+8s(M_f+M_g)-4J
\le21s⁵\quad(s\ge64).\tag{R12}
\]

The exact source identities are `leftbad=2s Mf`, `rightbad=2s Mg`, overlap J; they count true original source projections q--ell--p--r, not independent left/right events. To see `leftbad=2s Mf`, each unordered ORIGINAL collinear point pair `{q,p}` sharing one physical f-symbol lies on one original line ell and contributes the two directions `q->p`; for each, there are exactly s other original lines r through p (excluding ell), with q nonincident r by the GQ axiom. This gives `2s Mf` source endpoint pairs. The point-line dual proves `2s Mg`. Inclusion-exclusion subtracts the *actual joint* overlap J, not an independence product.

**Explicit 21s^5 arithmetic.** For s>=64, the minimal physical alphabet satisfies `a<=(ceil(3s sqrt(s)/2)) < (97/64)s sqrt(s)` (the integer trial binomial bound from #682). Since `0<=M-V<a-1` and `M+V<=a²`, the missing-label term is below `4a³ <= (1/2)(97/64)^3 s^5`. Also `4N<=s^5/8` and `C_s/s^4 <= (4097/4096)(609/512)`. Since J>=0 and Mf+Mg<=2C_s, the coefficient of s^5 in (R12) is strictly less than `(1/2)(97/64)^3+1/8+16(4097/4096)(609/512) <21`. No finite-h curve fitting or source-independent endpoint assumption enters this bound. The bound 21 uses the minimal-alphabet estimate and `Mf,Mg<=Cs` from the genuine GQ spectrum. Weighting the actual bad endpoint cells by P3 and using Cauchy with (R8), their total proper-path mass is at most

\[
L_E s^{11/2},\qquad L_E=\sqrt{21}\,\sigma_3^{-1}\sqrt{L_6}.\tag{R13}
\]

## 6. ALL FOUR internal positions, not a silent full/core substitution

For a remaining proper original-end-good core physical path `v0,v1,v2,v3`, its two physical endpoint pair labels decode a unique ORIGINAL nonincident q,r and hence the full-source projection q--ell--p--r. The original projection flags need NOT remain in the physical core.

For the first-inner-left blocked triples `(v0,v1,v3)`, expand an ORIGINAL FULL R(p,y) / CORE R0(u,y) source-book tensor. The exact original-source bijection gives the number of distinct triple cells `B_L=Phi_L-Psi_{original incident,L}<=Phi_L`. A separate dual identity holds for the right side. The first Cauchy factor of Phi, using the original point-collinearity spectrum, is at most `64s^(11/2)` in squared norm; its second squared factor is at most `32(K+1)Ts6`, since `sum Kpu=sum_v deg_full(v)deg_core(v)<=4N Delta` with `R0<=K+1`. Thus each side independently has

\[
B_L,B_R\le B_0 s^{23/4},
\qquad B_0=64\sqrt{(K+1)T}.\tag{R14}
\]

PR #685 independently strengthens the completion inequality. Let D0 be diag(core physical degrees) and `Theta=tr(D0 A0^4)`. Then `Theta<=Delta tr(A0^4)` and

\[
W_L²\le(\Phi_L-\Psi_L)\Theta,\qquad
W_R²\le(\Phi_R-\Psi_R)\Theta.\tag{R15}
\]

Reversing the same original path covers both inner positions on each side, and transposing physical coordinates together with ORIGINAL point/line types covers the right side without changing original source flags. The union bound therefore yields

\[
I_{\rm internal}\le2(W_L+W_R)
\le4\sqrt{B_0TL_4}s^{47/8}.\tag{R16}
\]

The exponent `47/8=5.875` is strictly below six. All path counts above are the SAME physical original-ID core; no independent resampling of either full source map.

## 7. Inverse ORIGINAL GF5 sixset: exactly two paths ON THE IMAGE

For each still-unblocked proper three-path with distinct original path IDs `(u_i,lambda_i)`, append the actual full original projection flags `(q,ell),(p,ell),(p,r)`. There are **six different original flags**: f(p) is disjoint from all four left physical path coordinates; g(ell) is disjoint from all four right physical path coordinates; the original source component is q--ell--p--r plus the three separate path flags. The left and right physical factor profiles are historical B/B with their unique repeated original factors p and ell overlapping exactly at the original flag (p,ell). This is an accepted strictly-positive historical GF5 six-coordinate class (the 51-column positivity is a cited classifier input, not deduced from a generic graph cycle).

Conversely, from a produced ORIGINAL sixset, the source multiplicities identify p,ell and their three anchor IDs. Removing f(q) from the left physical C4 identifies the three remaining original path edge labels up to reversal; the right C4 order must coincide on those SAME three IDs. Thus there are **at most two directed paths producing any original sixset** (exactly two on the produced image). No surjectivity onto the complete historical B/B-overlap population is asserted. Therefore

\[
U_{BB,\rm overlap}\ge\tfrac12
\bigl(\tfrac12s⁶-68Ts⁵-L_Es^{11/2}
  -4\sqrt{B_0TL_4}s^{47/8}\bigr)
\tag{R17}
\]

or

\[
U_{BB,\rm overlap}\ge s⁶/4-34Ts⁵-(L_E/2)s^{11/2}
    -2\sqrt{B_0TL_4}s^{47/8}.\tag{R18}
\]

## 8. Independent exact integer sufficient dyadic h0; NEW improved threshold

For actual positive (unspecified) graph-theorem C,c, take
`T=max(1,ceil(2^58 C³))`. The three error terms after the division by two are each <=s6/24 whenever respectively:

\[
s\ge816T,\qquad s\ge144L_E²,\qquad
s\ge48^8(B_0TL_4)^4.\tag{R19}
\]

Let `sigma2_inv=16*65²`, `sigma3_inv=64*65³`,
`L6=24+288T²`. Define integer upper coefficients

\[
\widehat B_0=64\lceil\sqrt{65T}\rceil,\qquad
\widehat L_4=2\sigma_2^{-2}\lceil\sqrt{8L_6}\rceil+40T.
\]

An exact *sufficient* universal root threshold is

\[
s_{0,\rm int}=\max\left\{
64,\ 816T,\ 144\cdot21\sigma_3^{-2}L_6,\
48^8(\widehat B_0T\widehat L_4)^4
\right\},\qquad
h_0=\max\{1,\lceil\log_2 s_{0,\rm int}\rceil\}.\tag{R20}
\]

All operations are integers except the externally existential positive C,c; the companion implementation checks any **positive rational illustrative** C,c exactly and independently from #683's calculator.

**New precise relative improvement:** #684's `2^58` in place of #659's `2^59`, when propagated through the WHOLE unchanged proof, cannot worsen h0, and for the deliberately **HYPOTHETICAL** test values `C=c=1` the sufficient old h0=826 becomes new h0=**816**. These are **NOT actual** Jiang–Yepremyan constants or an attainable finite W(3,2^816) experiment. They are integer-algebra regression inputs, not evidence of a numerical published threshold.

For all genuine sufficiently large dyadic s, (R18)–(R20) yield `U_BB>=s6/8` in the small-D6 branch. Otherwise `D6>=delta*s6`. Hence the conditional-on-inputs all-map result (R1) follows, with `S_seven>=delta*s6` and the historical original GF5 floor

\[
R_3(f,g)\ge \frac{5643\,\delta}{51^6}s^6.
\]

This is an obstruction **within the exact specified GQ / classical-alteration model**, not for every weighted ASET or general hypergraph method; no R2 upper or full signed R3 expression is established. The asymptotic Omega(s6) quantifier is `exists delta>0, exists h0, forall dyadic h>=h0, forall legal f,g`. A claim covering **every** finite h>=1 would require additional small-h bounds.

## 9. Truly independent falsification and scientific STOP

New `research/hyp105_branch_a_root_independent_referee.py` never calls previous source-count, mixed-blocker or root threshold calculators to compute expected values. It imports ONLY the genuine finite GQ source incidence generator. Its independent ORIGINAL-first proof-relevant audit:
- counts full pencil collision books Mf,Mg directly from original source line/point pairs;
- counts original flag conflict edges separately from ALL original flag-ID pairs, checks exact `|E(conflicts)|=Mf+Mg`;
- for genuine W32/W34 with arbitrary fixed correlated injected f,g, enumerates every nonincident q,r and its full original q--ell--p--r, checks `leftbad=2sMf`, `rightbad=2sMg`, exact overlap J, and all four ordered physical endpoint populations;
- builds Caro–Wei min-current-degree original source selection, independent exact conditional-expectation two coordinate cuts, preserves both physical diagonals, checks row/column-cherry-freeness and enumerates all actual simple physical C6 by graph DFS;
- for every C6, checks ORIGINAL six flag owners, distinct original point/line factors, physical coordinate-proper sixcycle, and injective cycle -> original sixset transfer;
- **positive nonvacuous planted genuine ORIGINAL matching of six true flags**, explicitly aligned six-coordinate physical f and g cycles on W32 and W34, to ensure the original source D6 oracle actually sees accepted sixsets; not merely zero-cycle synthetic controls;
- uses an entirely separate finite-graph loop over ALL 512 simple labeled 3×3 bipartite graphs for direct rooted 4/6 closed-walk counts, true C6 count, the two trace inequalities and the length-three convexity inequality;
- derives (R20) using Python exact big integers/Fraction and checks multiple adversarial rational C,c, old and new h0, including 816 vs 826 for hypothetical constants; malformed constants/maps/IDs fail closed.

The genuinely finite oracles **cannot** establish any all-h result alone. The written combinatorial proofs and the original external graph theorem support the asymptotic inference. **Residual independent peer-review obligations:** verify actual historical GF5 positivity for six distinct ORIGINAL IDs and all 51 columns; independently check the original #659/#652 all-map graph-to-sixset surjection/injectivity outside the tested s; check all full/core mixed source identities and double-counting; obtain an externally qualified referee verdict. This Draft does not promote #230 to PROVED_A, does not merge any stacked scientific PR, and leaves #230 **OPEN_WITH_FORMAL_BLOCKER** until its acceptance gate is met.
