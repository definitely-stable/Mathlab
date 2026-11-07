# HYP-105 #230 — AA4-ROOTGATE: independent exact heavy/low proof-DAG audit

**Scientific scope:** Draft child of frozen #735 (ce7a9a88784257fc261e499e6d454b0227fa9804). No changes to main, ancestors, issue closure or ASET exponent. This is a new **conditional all-h implication theorem** and independent arithmetic audit, **not independent formal acceptance of all inherited source/selector lemmas**.

## 1. Quantifiers and external assumption

Fix dyadic \(s=2^h\), \(h\ge h_0\). Work on the genuine ORIGINAL symplectic \(W(3,s)\), whose point and line counts are \(V=(s+1)(s^2+1)\), original named point-line incidence flags \(I\) with \(N=(s+1)V\), and smallest globally injective unordered physical pair alphabet \(a=\min\{b:\binom b2\ge V\}\). **Any** fixed, complete, separately pair-injective physical maps f,g are allowed, including arbitrary correlation. After choosing f,g, **any adversarial deleted set Z of original incidence IDs** of size \(|Z|\le\rho s^4\) is allowed. Each original flag owns both original physical opposite diagonals.

Simonovits' ordinary graph six-cycle supersaturation theorem is explicitly stated in Jiang–Yepremyan, Combinatorics, Probability and Computing 29 (2020), 698–721, DOI https://doi.org/10.1017/S0963548320000206, including r=2, k=3:

\[
e(F)\ge C_{\mathrm{graph}}v(F)^{4/3}
\implies
C_6(F)\ge c_{\mathrm{graph}}(e(F)/v(F))^6.
\]

Here **the published constants are positive but existential; numerical values are not 1 by assumption**. Normalize \(C_{\rm graph}\ge1\), \(0<c_{\rm graph}\le1\). The exact program takes FORMAL rational \(C_0\ge C_{\rm graph}\), \(0<c_0\le c_{\rm graph}\), not invented numerical published constants. All conditional bounds below depend on such bounds.

Define

\[
K=64,\quad T=\lceil2^{64}C_0^3\rceil,\quad
q_r=4^r\binom{r(K+1)}r\quad (r=2,3),\quad
L_6=24+288T^2,
\]

\[
L_4=2q_2^2\lceil\sqrt{8L_6}\rceil+56T,\quad
B_0=\lceil\sqrt{1280(K+1)T}\rceil,\quad
E=8q_3\lceil\sqrt{L_6}\rceil,\quad
D=4\lceil\sqrt{B_0TL_4}\rceil,
\]

\[
\boxed{\rho=\frac1{12q_3^2L_6},\quad
\delta=\frac{c_0}{2^{120}},\quad
s_0=\max\{64,672T,(8E)^2,(8D)^8\},\quad
h_0=\lceil\log_2s_0\rceil.}\tag{ROOT-1}
\]

All numbers are exact rational/integer, including rounded integer radicals and the *least dyadic* threshold. Formal tests with C0=c0=1 are **NOT claims** about numeric published constants.

## 2. Independently checked genuine source envelope

For every dyadic \(s\ge64\),

\[
s^4\le N\le2s^4,\quad a^2\le4s^3,\quad
C_s=(s^2+1)(s^2+a-2)\le\frac32s^4.
\]

The original full conflict graph between named incidence flags has at most \(2C_s\le3s^4\) conflict pairs; this is not an ordinary physical maximum-degree claim. The new exact checker independently reconstructs the minimal a with an integer square root and verifies the source envelope for multiple dyadic s, separately from the parent code. The all-h source count is an algebraic consequence of the true W(3,s) point-line sizes.

## 3. HEAVY source and external SS6 proof obligation

Freeze full ORIGINAL physical high-Q vertices before deleting Z. If the true full physical high-Q edge total \(E_T\ge s^4/8\), each deleted ORIGINAL ID destroys at most TWO original diagonals and therefore

\[
E_A\ge(1/8-2\rho)s^4\ge s^4/16,\quad
L_{\rm heavy}\ge s^4/32.
\]

The prior original Caro–Wei source-conflict independent-set plus two whole-flag coordinate cuts implies

\[
|I_G|\ge \frac{L_{\rm heavy}^2}{4(L_{\rm heavy}+2e_J)}
\ge\frac{s^4}{2^{15}}.
\]

The genuine **no-clone** balanced ordinary graph chunk \(F\) from #730 then satisfies

\[
e(F)/v(F)\ge s/2^{20},\qquad v(F)\le16s^3/T.
\]

To apply the actual external supersaturation theorem it suffices that

\[
(s/2^{20})^3\ge C_0^3(16s^3/T)
\iff T\ge2^{64}C_0^3.\tag{ROOT-HSS6}
\]

The new proof engine independently checks this cubic condition with exact rational arithmetic, without assuming unknown published constants. Under the inherited no-clone source construction and six-original-ID D6 injection from #730/#734, the conditional HEAVY conclusion is

\[
D_{6,\bar Z}\ge c_0(s/2^{20})^6=\delta s^6.\tag{ROOT-H}
\]

## 4. LOW true-original paired core and explicit error budget

When \(E_T<s^4/8\), remove every true ORIGINAL flag touching frozen Q, every original flag with FULL original conflict-degree \(>64\), and every original flag in Z. As \(|Z|\le\rho s^4\le s^4/32\),

\[
|C|\ge N-E_T-4C_s/64-|Z|
\ge(1-\tfrac18-\tfrac3{32}-\rho)s^4
\ge\tfrac34s^4.
\]

All two physical diagonals of each kept original source flag remain; the physical core has \(\Delta\le Ts\), full original source conflict degree at most K and \(m=2|C|\le4s^4\). By the Blakley–Roy 3-walk bound on the genuine full \(a^2\) physical corners,

\[
W_3=\mathbf1^\top A_C^3\mathbf1
\ge(4|C|)^3/a^4\ge 27s^6/16.
\]

If the surviving original D6 count already exceeds \(\delta s^6\), the root sixset claim follows. Otherwise \(D_{6,\bar Z}<\delta s^6\le s^6\). The separate source selector, SRG energy and blocker lemmas from #731/#732 provide

\[
\|P_3\|_F^2\le q_3^2L_6s^6,\quad
\operatorname{tr}(A_C^4)\le L_4s^5,\quad
B_x,B_y\le B_0s^{23/4}.
\]

The genuine original GQ projection uses THREE named source flags. Each original flag occurs \(s^2\) times in EACH of its three roles, and up to four oriented physical endpoints occur per projection, so the deleted-original-ID endpoint union has cardinality at most \(12s^2|Z|\). The original non-Z endpoint union has at most \(64s^5\) endpoints. This gives the accepted path-energy error

\[
E s^{11/2} + q_3\sqrt{12L_6\rho}\,s^6.
\]

The chosen rho spends at most **ONE sextic unit** on actual SOURCE deletions (this is O(s^6), not little-o); 84T s^5 coordinate-improper paths and D s^(47/8) internal blockers are each separately at most s^6/8 once \(s\ge s_0\). Therefore the one-sided source six-ID B/B-overlap lift of #731/#734 implies

\[
2BBo_{\bar Z}\ge
(27/16-1-3/8)s^6=5s^6/16,
\quad BBo_{\bar Z}\ge5s^6/32.\tag{ROOT-L}
\]

The entire BBo historical sixset class is NOT equal to the physical 3path image; the prior #734 genuine W32 counterexamples disprove such a surjectivity assertion. The argument uses only the produced physical subset, so the correct implication is one-sided.

## 5. NEW exact branch-aware full 51-palette GF(5) weighted implication

The independent source GF(5) 51-pattern tree-flow and full palette crosschecker from #735 proved exact **ten unordered balanced sign** counts \(w_{\rm D6}=54162\) and \(w_{\rm BBo}\ge53526\) on every actual ORIGINAL six-ID source motif of those respective classes. The different classes are disjoint by original point/line incidence profiles. Thus

\[
R_3\ge
\frac{54162 D_{6,\bar Z}+53526 BBo_{\bar Z}}{51^6}.
\]

A generic minimum-weight approach gives only \(\ge53526\,\delta s^6/51^6\) from the joint sixset mass theorem. The NEW sharper proof is branch-aware:

* HEAVY supplies \(D_{6,\bar Z}\ge\delta s^6\), giving \(R_3\ge54162\,\delta s^6/51^6\).
* LOW and small surviving D6 supply \(BBo_{\bar Z}\ge5s^6/32\), giving \(R_3\ge(53526\cdot5/32)s^6/51^6\). As \(\delta=c_0/2^{120}\le2^{-120}\), the latter is STRONGLY larger than \(54162\,\delta s^6/51^6\).

Hence, **conditional on the inherited genuine source six-ID heavy/low inequalities and the real external graph theorem**, for every admissible dyadic \(s\ge s_0\), every complete correlated fixed f,g, and every adversarial \(|Z|\le\rho s^4\),

\[
\boxed{R_3\ge\frac{54162\,c_0}{2^{120}\,51^6}\,s^6.}\tag{ROOT-W}
\]

This is a strict \(54162/53526=9027/8921\) improvement over the old conservative *sufficient risk constant*, NOT a new sextic source abundance theorem, not an ASET exponent, and not a claim that numerical published graph constants equal 1.

## 6. Explicit proof DAG / research acceptance boundaries

| ID | Proof gate | Checked here | Remaining scope |
|---|---|---|---|
| G1 | Genuine \(W(3,s)\) original point/line and source dimensions, minimal physical alphabet, original collision budget | Fresh exact source envelope and inequality derivation | Original SRG/conflict structural lemma from prior branches |
| G2 | Freeze full original Q, adversarial original Z deletion ≤2 physical edges/flag | Exact algebra and source-owner accounting | Pair ownership must remain genuine for every source flag |
| G3 | Original Caro–Wei, whole flag cuts, no-clone balanced physical chunk | Fresh exact density and cubic SS6 threshold | Upstream original source/chunk geometry needs full line-level audit |
| G4 | Simonovits/Jiang–Yepremyan graph C6 supersaturation | Primary published statement verified | The true graph C,c are existential, not numeric |
| G5 | True original dense LOW core and Blakley–Roy 3walk floor | Exact retained mass and W3 constant | Original conflict and physical owner structure inherited |
| G6 | Original point/line energy, proper path selector, four blockers and deletion masks | Independent exponent and rational total error closure | Upstream all-h source-specific moment/book inequalities still need line-level acceptance |
| G7 | Six ORIGINAL incidence-ID D6 and BBo injections and 0/1, 0/2 inversion | Prior independent #734 constructive check | Root mathematical acceptance is still Draft |
| G8 | Original full-51 GF(5) D6/BBo signed weights | Prior #735 dual algorithm + independent 51-palette checks | Complete full R2/R3 ASET optimization is outside scope |
| G9 | Universal all-h root theorem | **Conditional derivation only** | Independent full source-lifting/SS6/selector proof acceptance and root issue closure NOT performed |

No code flag can promote the root to proved merely because the numeric implication tests are green. The new independent script uses only exact Python integers and Fraction and imports NONE of the parent implementation. A separate test compares its constants to the frozen #733 code to detect drift, without using the parent as the proof.

## 7. Adversarial falsifiers and GitHub-hosted evidence

* Exact rational algebra for formal graph-constant probes (C0,c0)=(1,1),(2,1/5),(7/3,1/17). These are algebraic sample parameters only; none is certified to dominate the actual published theorem constants.
* Exact minimal dyadic h0: the bound closes at h0 and fails as a **sufficient budget** at h0−1, without floating-point comparisons.
* Genuine original source point/line counts and collision bounds for several dyadic orders 64 through 16384.
* Four fail-closed counterfactual mutations: decrement T below the sufficient external SS6 threshold; double rho and break the source deletion-mask budget; replace the actual heavy 54162 or low 53526 GF(5) ten-sign weight with a weaker unjustified value. These failures do NOT imply the root hypothesis is false; only these particular *sufficient proof gates* no longer certify it.
* Distinct heavy vs low risk coefficients and the new exact 9027/8921 improvement checked without mixing class counts.
* Scientific root status remains OPEN_WITH_FORMAL_BLOCKER throughout the permanent machine JSON.

Specialist workflow uses GitHub-hosted Ubuntu 24.04, Python 3.12, eleven tests and a strict uniquely parsed all-order source-DAG certificate; full Research and INDEX also required on exact final PR HEAD. No local PC or speculative background run.

**Next allowed mathematical step:** independently audit each inherited all-order source geometric lemma (G3/G5/G6) line by line, not merely their arithmetic composition, then decide root acceptance. No merge or issue closure.
