# HYP-105 / #230 — AA4-HEAVYADAPT: independent heavy-source Caro–Wei audit and new 93313 denominator

**Scientific status:** strict Draft child of frozen green [#743](https://github.com/definitely-stable/Mathlab/pull/743), HEAD 2714a70dd036ef7fbf6a3dcf11f8f0a34056a16f. Main, parent PRs and root issue unchanged; no merge, issue closure or general ASET exponent. Root stays OPEN_WITH_FORMAL_BLOCKER pending final independent all-order predecessor-lemma acceptance.

The issue's **primary Branch A goal** is the UNWEIGHTED sum of SEVEN positive classes of DISTINCT ORIGINAL incidence-ID sixsets, \(S_s(f,g)=\Omega(s^6)\), uniformly over all legal *fixed* correlated maps f and g. The GF5 signed-event \(R_3\) is a separate additive-probability SUM corollary, not the definition of S. The new result is an independent exact strengthening of the source-heavy no-clone density step. It obtains **R_NEW=93313** instead of R_OLD=370944 and **more than 3900-fold improvement** in the true-original D6, seven-class S and signed GF5 R3 sufficient sextic constants, at a much lower sufficient dyadic threshold, without new assumptions on f,g,Z or graph supersaturation.

## 1. Correct ORIGINAL source model and fixed quantifiers

For all \(s=2^h\ge64\) take the genuine symplectic \(W(3,s)\), \(V=(s+1)(s^2+1)\) original points and lines, \(N=(s+1)V\) ORIGINAL named point-line incidence flags, and minimal a with \(\binom a2\ge V\). Fix ANY separately complete globally pair-injective maps \(f:P\to\binom{[a]}2\), \(g:L\to\binom{[a]}2\), with unrestricted correlation, no relabeling/resampling. One original flag owns **exactly two** real opposite physical diagonals; every physical edge has a unique source owner. Fix ANY original incidence ID deletion set Z, including f/g-dependent Z, of size \(|Z|\le\rho s^4\). For the full original physical graph H, **freeze before Z** the high-degree physical vertices

\[
Q_T=\{v:d_H(v)>Ts\},\quad E_T=\#\{e:e\cap Q_T\ne\varnothing\}.
\]

HEAVY means \(E_T\ge s^4/8\); LOW means strictly below, a complete deterministic dichotomy on the same source and maps.

## 2. New ALL-h deletion-adaptive HEAVY lemma

Every deleted original flag removes at most two distinct source-owned physical edges, so at least \(E_T-2|Z|\ge(1/8-2\rho)s^4\) heavy edges survive. Each genuine owner contributes at most two of them. Thus the number L of DISTINCT named surviving heavy source owner IDs obeys

\[
\boxed{L\ge\lambda(\rho)s^4,\qquad
\lambda(\rho)=\frac1{16}-\rho.}\tag{HD-1}
\]

The original point/line SRG source conflict theorem #737 gives for ANY fixed correlated f/g \(e(J)\le(5/2)s^4\). Apply Caro–Wei on the induced graph of those real L owners and retain the actual \(\rho\)-dependent L instead of substituting its worst-case value at \(\rho=1/32\):

\[
\alpha(J)\ge \frac{L^2}{L+2e(J)}
\ge \frac{\lambda^2}{\lambda+5}s^4.
\tag{HD-2}
\]

Two coherent, independent, typed physical-coordinate binary cuts retain at least half of the original-source independent flags on the first cut, and half of these WHOLE source flags on the second cut, never just one physical diagonal. The retained set S has

\[
|S|\ge\frac{\lambda^2}{4(\lambda+5)}s^4.
\tag{HD-3}
\]

Choose for each actual surviving source flag i one REAL heavy source-owned physical edge and one high-degree endpoint in frozen Q. The majority of true source-heavy first-coordinate bits contains at least |S|/2 distinct heavy-edge witnesses. Let R_Q be ALL existing Q vertices with that majority first bit, r=|R_Q|>0, and let Y be existing selected physical opposite-bit vertices. Partition Y into at most \(\lceil a^2/r\rceil\le2a^2/r\) sets of size at most r. A winning chunk defines a genuine simple ordinary physical F, using **only selected real physical edges and real distinct physical vertices**, with \(m_F\ge |S|r/(4a^2)\), \(v_F\le2r\). Therefore

\[
\boxed{\frac{e(F)}{v(F)}\ge\frac{|S|}{8a^2}
\ge\frac{\lambda(\rho)^2}{72(\lambda(\rho)+5)}s
=\frac{s}{R(\rho)},\
R(\rho)=72\frac{\lambda(\rho)+5}{\lambda(\rho)^2}.}
\tag{HD-4}
\]

From original real graph degree sum \(4N\le(17/4)s^4\) and high-Q threshold \(Ts\), the old independently proved vertex cap remains

\[
\boxed{v(F)\le2|Q_T|\le(17/2)s^3/T.}\tag{HD-5}
\]

The new formula is exact for THIS Caro–Wei/two real cuts/chunk proof budget; not claimed optimal among all possible alternative constructions.

## 3. A uniform cap on the actual admissible deletion radius

The actual accepted original source LOW/R3 signed risk Pareto radius from #742 is

\[
\rho_\star=
\frac{t_\star^2}{12q_3^2L_6},\quad
t_\star=\frac{119}{24}-2\frac{54162}{53838}\delta,\quad
q_3=64\binom{195}{3},\quad L_6=24+153T^2\ge24,
\]

where \(\delta>0\) is the HEAVY source-sixset sextic lower (its R denominator is being improved here). Since \(0<t_\star<119/24\) for 0<c0≤1 and R≥93313, a bound UNIFORM in every external graph constant and every T is

\[
\boxed{0<\rho_\star<
\frac{(119/24)^2}{12q_3^2\cdot24}
=\frac{14161}{1006143020717624524800}
<2^{-32}.}
\tag{HD-6}
\]

No circular dependence: (HD-6) uses only \(L_6\ge24\), the fixed source selector \(q_3\), and \(\delta\le1/93313^6\), not T or an assumed numerical published graph theorem constant.

Set \(\rho_{\rm cap}=2^{-32}\) and the worst case \(\lambda_{\min}=1/16-\rho_{\rm cap}\). Direct **exact rational** calculation yields

\[
\boxed{R_{\rm NEW}=\left\lceil72\frac{\lambda_{\min}+5}
{\lambda_{\min}^2}\right\rceil=93313.}
\tag{HD-7}
\]

At exactly Z=empty (and thus rho=0) the same formula gives **R(0)=93312**. The single integer 93313 works for all named original Z within the genuinely admitted \(\rho_\star s^4\); this is almost the best zero-deletion value achievable from the unchanged Caro–Wei proof budget.

## 4. Exact SS6 application and all-h conclusion

Fix once for all \(C_0\ge\max(1,C_{\rm graph})\) and \(0<c_0\le\min(1,c_{\rm graph})\), rational bounds on the positive EXISTENTIAL (NOT NUMERICALLY KNOWN) external ordinary graph C6 supersaturation constants. Source: Jiang–Yepremyan (2020), DOI https://doi.org/10.1017/S0963548320000206, r=2/k=3 graph case: for a SIMPLE ordinary F with \(e(F)\ge C_{\rm graph}v(F)^{4/3}\), at least \(c_{\rm graph}(e(F)/v(F))^6\) distinct unoriented C6s exist. All vertices of F here are actual physical corners: NO CLONES.

Put R=93313 and

\[
\boxed{T=\left\lceil(17/2)R^3C_0^3\right\rceil.}
\]

Combining (HD-4–5) gives \(e(F)\ge C_0 v(F)^{4/3}\). The original selector forbids typed-coordinate returns on simple C6 at distance two by SOURCE pencil conflict and at distance three by two typed bichromatic cut bits. Every physical C6 has six distinct original source flag IDs and injects in one original aligned D6 sixset (one physical unoriented C6 at most per named six-ID source set, independent #734 source-first inverse). Thus

\[
\boxed{D6_{\bar Z}\ge\delta_{\rm new}s^6,\qquad
\delta_{\rm new}=\frac{c_0}{93313^6}.}
\tag{HD-8}
\]

Relative to old #743 universal \(c_0/370944^6\),

\[
\boxed{\frac{\delta_{\rm new}}{\delta_{\rm old}}
=\left(\frac{370944}{93313}\right)^6
\approx3946.36446.}
\tag{HD-9}
\]

LOW remains valid with exactly its original geometric and spectral proof, but T and all dependent error constants update consistently:

\[
\begin{gathered}
K=64,\quad q_r=4^r\binom{r(K+1)}r,\quad
L_6=24+153T^2,\\
L_4=q_2^2\lceil\sqrt{\lceil17L_6/4\rceil}\rceil+19T,\quad
B_0=\lceil\sqrt{360(K+1)T}\rceil,\\
E=5q_3\lceil\sqrt{L_6}\rceil,\quad
D=4\lceil\sqrt{B_0TL_4}\rceil,\quad
s_0=\max(64,444T,(8E)^2,(8D)^8).
\end{gathered}
\tag{HD-10}
\]

The new \(\rho_\star\) still satisfies both original source restrictions \(\rho_\star<1/32\) and \(\rho_\star<3/64\). Under LOW with D6 smaller than \(\delta_{\rm new}s^6\), the previous already proved original physical proper 3path→BBo 2-to-1 inverse and the three separate ≤s6/8 errors give

\[
BBo_{\rm produced,\bar Z}
\ge\frac12(119/24-t_\star)s^6
=\frac{54162}{53838}\delta_{\rm new}s^6.
\tag{HD-11}
\]

Since these are true ORIGINAL distinct six-ID B/B-overlap class members and D6 source sixsets are disjoint original source keys, the **PRIMARY issue #230 seven-motif-unweighted** obstruction follows for every sufficiently large dyadic s, ANY fixed separately pair-injective arbitrarily correlated f/g and ANY adversarial original Z with \(|Z|\le\rho_\star s^4\):

\[
\boxed{S_s(f,g)\ge\frac{c_0}{93313^6}s^6.}
\tag{HD-12}
\]

The accepted GF5 risk \(R_3\) is a SUM of indexed unordered 3v3 signed-event probabilities, not their union probability; exact full-ten GF5 weights 54162 per D6 and 53838 per physical-produced BBo give the separate corollary

\[
\boxed{R_3(f,g)\ge
\frac{54162c_0}{93313^6\,51^6}s^6.}
\tag{HD-13}
\]

No new ASET exponent, no new extraction algorithm, no published numerical graph constants. Positive absolute existence of c0 suffices for Omega(s^6).

### Exact FORMAL example ledgers, NOT numerically certified published graph constants

| FORMAL C0,c0 | old #743 h0 | new h0 |
|---|---:|---:|
| (1,1) | 810 | **751** |
| (2,1/5) | 840 | **781** |
| (7/3,1/17) | 847 | **787** |

These extremely large thresholds are conditionally computed from algebraic inputs; none of the three numeric C0/c0 pairs has been established by the paper. Do not present these h0 values as real world finite proofs.

## 5. Independent mathematics and real-original finite falsification

The new independent [source/heavy certifier](../../research/hyp105_original_heavy_adaptive_ss6_referee.py) reconstructs ALL exact Fraction constants T,L6,L4,B0,E,D,s0,h0,delta,rho_star and checks 19 precise quantified budget equations, including the uniform \(\rho_\star<2^{-32}\), equality R(0)=93312, integer ceiling 93313, same-branch low-tail GF5 risk exact match and >3900x source S coefficient. It does **not** import old heavy, energy, GF5, selector or root modules. Older #743 ledger imported TEST ONLY to catch errors.

A separate independently written real-original physical heavy witness algorithm uses only trusted genuine symplectic W(3,2)/W(3,4) source and globally pair-injective label fixture constructors. For each nonempty original Z and DIAGNOSTIC small threshold T=1 (this is deliberately NOT the universal all-h T), it rebuilds BOTH true physical diagonals for each original flag, full Q before Z, full surviving heavy physical edges, exact distinct original heavy source owners, and a real source conflict subgraph J. It selects a deterministic MIN-residual-degree independent set meeting the Caro–Wei bound, then explicitly produces BOTH actual coordinate binary cuts by exact conditional expectation, retaining entire original source flags and their real source-owned diagonals. For every selected source ID it picks one surviving REAL heavy edge witness, takes a genuine physical-heavy majority-bit side, partitions existing opposite physical vertices into balanced actual blocks, and verifies for the resulting TRUE simple no-clone F:

\[
\frac{e(F)}{v(F)}\ge \frac{|S|}{8a^2},
\qquad
\text{no invented owners, vertices or physical edges}.
\]

The tests do NOT assert the asymptotic original-s sextic theorem for finite small s=2 or 4; they are independent structural falsifiers only. Dedicated GitHub-hosted Ubuntu 24.04 Python 3.12 workflow runs 12 negative/positive tests and a fail-closed single complete true-original JSON, plus INDEX and full Research on the SAME final HEAD. No user PC.

**Scientific STOP:** A new nontrivial ALL-h quantitative original source-heavy theorem and stronger seven-class Branch A coefficient are proved conditional on the individually identified previous source geometric/selector/inverse lemmas and a genuine published ordinary C6 supersaturation result. It does not mechanically verify all 18 cited mathematics inputs and does not itself authorize merging, closing root #230, changing root PROVED_A or a general ASET exponent. Next allowed step is complete independent mathematical referee acceptance/precise falsifier of all predecessor source lemmas, not another unscoped numeric-only benchmark.
