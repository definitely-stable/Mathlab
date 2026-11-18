# HYP-105 #230 — AA4-ROOT-SRG-FRONTIER: publication-level independent GQ/SRG source audit, sharper full-original J, K=4 frontier and scale-aware Z0 root

**Scientific status:** the true ORIGINAL W(3,s) point/line SRG → source-collision counting premise is now independently rederived **for every s=2^h**, not inferred from sampled geometry. A NEW strictly sharper quantitative conclusion follows: **e(J)<(19/8)s^4** for all s≥64 (prior cap was 5s^4/2); already for s≥256 the original LOW pruning can use **K=4**, leaving a positive paired CORE. A further new rigorously scale-aware cap with fixed H=32 and source K=10 improves the PREVIOUS conditional root sufficient s0 ledger. This closes **the GQ-SRG premise only**, NOT the entire Branch A; inherited HEAVY no-clone/source C6 transfer, global LOW endpoint/four-blocker/sixth-moment and original BBo inversion still require full scientific acceptance.

Strict descendant of frozen [Draft #773](https://github.com/definitely-stable/Mathlab/pull/773), parent HEAD 0914954a702850140b31f349d2c646aab938b9a5. No prior branches, main or root issue were modified/merged. ROOT status **OPEN_WITH_FORMAL_BLOCKER**, not PROVED_A or ASET exponent. Current target is the original unweighted seven disjoint unordered six-incidence-ID motif sum S_s(f,g); set Z=empty for root Branch A, without claiming a stronger adversarial deletion theorem.

External geometry corroboration: the point collinearity graph of a generalized quadrangle of order (s,t) is strongly regular with parameters ((s+1)(st+1),s(t+1),s−1,t+1); see [the Cambridge University Press mathematical source](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/simple-groups-product-actions-and-generalized-quadrangles/0C81DBE9664CD88B40616CA7D656E7BC). The complete proof below DOES NOT rely on numerical eigenvalue software or this external text as an axiom.

## 1. Re-prove the true symplectic point- and line-side SRG identities from the GQ axioms

Let s=2^h≥2, and let W(3,s) be the REAL symplectic generalized quadrangle with original sets P,L, true incidence flags I={(p,ell):p∈ell}, all named. There are

\[
V=|P|=|L|=(s+1)(s^2+1),\qquad
N=|I|=(s+1)V.
\]

Each original point lies on s+1 original lines and each original line contains s+1 original points. Distinct collinear points determine one UNIQUE original line; two distinct lines share at most one point; for p outside an original line ell, exactly one q∈ell is collinear with p. These are the GQ axioms, not a claim about a synthetic strongly regular host.

On original points build M_P with M_P(p,q)=1 precisely when p≠q lie on an ORIGINAL common line. Degree is k=s(s+1). Two adjacent points share exactly s−1 common neighbors: the other points on their unique common line; any off-line common neighbor would create a forbidden triangle of GQ lines. Two nonadjacent points have exactly s+1 common neighbors, one projection onto each line through the first point. Hence

\[
v=V,\quad k=s(s+1),\quad\lambda=s-1,\quad\mu=s+1.
\]

From these *literal* walk counts,

\[
\boxed{M_P^2=(s^2-1)I_V-2M_P+(s+1)J_V.}\tag{SRG-A}
\]

EXACTLY the same proof under duality gives M_L with the same polynomial, and the labels f and g do not appear in either matrix.

Both matrices have the constant eigenvector with eigenvalue k. On the orthogonal complement of constants, J_V vanishes, so any other eigenvalue θ satisfies θ²+2θ−(s²−1)=0; its two roots are

\[
\boxed{r=s-1,\qquad t=-(s+1).}\tag{SRG-B}
\]

In particular, for any vector u perpendicular to 1, uᵀM_Pu ≤(s−1)||u||², and identically for M_L. This is a deterministic all-h spectral fact. Trace M=0 and dimensions also force the EXACT eigenvalue multiplicities m_r=s(s+1)²/2, m_t=V−1−m_r. The independent true W32/W34 oracles check the entire matrix common-neighbor formula and these multiplicities exactly (integer arithmetic), NOT merely a floating numerical spectrum fit.

## 2. Derive the exact ORIGINAL pencil-conflict formula, no map independence

Fix ANY two complete globally pair-injective real coordinate labelings

\[
f:P\hookrightarrow\binom{[a]}2,\qquad
g:L\hookrightarrow\binom{[a]}2,\qquad
a=\min\{b:\binom b2\ge V\}.
\]

Their correlation is unrestricted. For the point map f, for each physical symbol x define the ORIGINAL point subset S_x={p:x∈f(p)} and d_x=|S_x|. Because f consists of pairwise DISTINCT two-symbol label pairs,

\[
\sum_xd_x=2V,\quad d_x\le a-1,\quad
\sum_xd_x^2\le2V(a-1).\tag{SRG-C}
\]

Define e_col(f) as the number of unordered ORIGINAL collinear point pairs {p,q} whose physical f label pairs intersect. Two different physical unordered pairs intersect in at most one symbol, so there is an EXACT no-multiplicity identity

\[
2e_{\rm col}(f)=\sum_x 1_{S_x}^{\top}M_P1_{S_x}.
\]

Split each 1_S into its constant and orthogonal components. Use only SRG-B, not random or typical labels:

\[
\begin{aligned}
2e_{\rm col}(f)
&\le\sum_x\left[\frac{k}{V}d_x^2
 +(s-1)\left(d_x-\frac{d_x^2}{V}\right)\right]\\
&=2V(s-1)+\frac{s^2+1}{V}\sum_xd_x^2\\
&\le 2V(s-1)+2(s^2+1)(a-1).
\end{aligned}
\]

Therefore

\[
\boxed{e_{\rm col}(f)\le
  (s^2+1)(s^2+a-2)=:C_s.}\tag{SRG-D}
\]

Independently, **in the dual ORIGINAL line collinearity graph**, the same derivation yields e_col(g)≤C_s for any fixed g. No assumption f=g, independent f/g, group invariance or random relabeling occurs.

The true ORIGINAL source graph J on named flags i=(p,ell) has an edge for two distinct flags sharing the same point p with **overlapping g-line physical label pairs**, or sharing the same line ell with **overlapping f-point physical label pairs**. Two distinct ORIGINAL flags cannot share both their original point and line. Any two distinct ORIGINAL collinear lines have one original intersection point, and any two collinear points share one original line. Thus (no extra multiplicities)

\[
\boxed{
e(J)=e_{\rm col}(f)+e_{\rm col}(g)
\le2C_s.
}\tag{SRG-E}
\]

This equality is both the exact original source incidence-counting statement and the original manuscript's SRG-first mathematical input. It is **independently derived**, and is falsified in code by a wholly different direct named-flag pencil J enumeration; both counts must agree on true W32/W34. The same fixture independently checks the stronger exact Gram-energy identity for each source map:

\[
G_f=\sum_x\|M_P1_{S_x}\|_2^2
  =2V(s^2-1)-4e_{\rm col}(f)+(s+1)\sum_xd_x^2,
\]

and the point-line dual G_g. Source orientation mistakes, mixing f and g or collapsing actual flag owners fail these exact gates.

## 3. NEW strict all-h sharpening: 5/2 → 19/8 at dyadic s≥64

Old root ledgers replaced the exact 2C_s bound with e(J)≤(5/2)s^4, losing a fixed amount of slack. We instead bound the actual MINIMAL pair alphabet a from V exactly.

Because binom(a−1,2)<V,

\[
(a-2)(a-1)<2V,\quad\text{so}\quad a-2<\sqrt{2V}.
\tag{AL-1}
\]

For every s≥64,

\[
V=(s+1)(s^2+1)\le(33/32)s^3,
\quad
\sqrt{2V}\le\sqrt{33/16}s^{3/2}
<(23/16)s^{3/2}.
\tag{AL-2}
\]

The last strict inequality is verified exactly by 528/256<529/256. Since √s≥8 for s≥64,

\[
\frac{a-2}{s^2}<\frac{23}{128},
\qquad \frac1{s^2}\le\frac1{4096}.
\]

Substitute the ACTUAL symplectic source expression C_s into SRG-E:

\[
\frac{C_s}{s^4}
=\left(1+\frac1{s^2}\right)
  \left(1+\frac{a-2}{s^2}\right)
<
\frac{4097}{4096}\cdot\frac{151}{128}
=\frac{618647}{524288}
<\frac{19}{16}.
\]

Therefore the NEW **universal and strict** bound

\[
\boxed{e(J)<\frac{19}{8}s^4
\qquad(\text{all dyadic }s\ge64),}\tag{SRG-F}
\]

improves the prior 5s^4/2. Unlike a numerical fit to W32/W34, this is an exact symbolic proof for ALL h≥6, for ANY fixed globally pair-injective correlated f/g.

## 4. NEW source frontier: K=4 already valid for every dyadic s≥256

At dyadic s≥256, √s≥16, so the same exact argument gives (a−2)/s²<23/256 and 1/s²≤1/65536. Consequently

\[
\frac{C_s}{s^4}<
M_8:=\frac{279}{256}\frac{65537}{65536}
=\frac{18284823}{16777216}<\frac{35}{32}.
\tag{SRG-G}
\]

In LOW freeze full Q_T first, with actual E_T<s4/8. Delete all ORIGINAL flags owning one or more physical edges meeting Q_T (at most E_T owners), and every ORIGINAL flag with degree in the FULL true source J graph strictly greater than K. Handshaking and SRG-E give

\[
\#\{\deg_J>K\}\le\frac{2e(J)}{K+1}
<\frac{4M_8}{K+1}s^4.
\]

All surviving flags retain BOTH actual opposite physical diagonals. Thus

\[
\boxed{|C|>
\left(\frac78-\frac{4M_8}{K+1}\right)s^4.}
\tag{SRG-H}
\]

With the surprising **NEW admissible K=4** (the inherited #773 universal bound could only certify K≥5 using a rough 5/2 constant),

\[
\boxed{
|C|>\frac{65257}{20971520}s^4
\quad\text{for every dyadic }s\ge256.
}\tag{SRG-I}
\]

The fraction is strictly positive (~0.0031117); it is not a finite GQ observation. For K=3, even the LIMIT M→1 in this spectral/handshake argument gives 7/8−1<0, so this method cannot certify a positive universal core with K≤3. This is NOT a proof no stronger mathematics could ever do so.

**Important distinction:** K=4 is the smallest globally admissible threshold CERTIFIED by this improved source method, but the tiny K4 physical core makes the subsequent eight-power four-blocker s0 COSTLY. It is NOT the best threshold for the complete conditional root minimax; scientific significance is separating mathematically possible source pruning from quantitatively optimal root budgets.

## 5. NEW scale-aware exact rational source envelope, any fixed even dyadic H≥8

For every integer EVEN H≥8, define one explicit exact rational

\[
\boxed{
M_H=\left(1+2^{-2H}\right)
    \left(1+\frac{23}{16\cdot 2^{H/2}}\right).
}
\tag{SRG-J}
\]

When s=2^h≥2^H, the proof in sections 3–4 gives C_s/s4<M_H and

\[
\boxed{e(J)<2M_Hs^4,\quad
|C|>\left(\frac78-\frac{4M_H}{K+1}\right)s^4.}
\tag{SRG-K}
\]

H and K are FIXED ONCE BEFORE s,f,g. There is no circular dependence: a sufficient final dyadic s0 is chosen at least 2^H. M_H decreases monotonically to 1 with H, and the true asymptotic source conflict cap tends to 2s4 (not the historical 2.5s4). The proof makes no unjustified assertion of simultaneous eigenvalue extremality, merely a valid universal upper.

For a convenient fixed **H=32**, K=10 and the SAME inherited asymmetric error allocation α=(1/64,1/64,15/16), the original source pruned CORE has coefficient

\[
c_{10,32}=\frac78-\frac{4M_{32}}{11}>0,
\quad
w_{10,32}=\frac{16}{81}(4c_{10,32})^3>0,
\tag{SRG-L}
\]

and Harris source survival reciprocals q2=16·11²=1936, q3=64·11³=85184. No single inequality in the existing LOW source moment/mixed-book bundle requires the value 64; all K dependencies in the inherited formulas are made explicit. The remaining inherited source selector, spectral/endpoint/mixed-book and BBo inverses are still SCIENTIFIC REVIEW obligations, not certified anew in this slice.

Preserve the original no-Z HEAVY absolute density R=93312, fixed arbitrary *existential* ordinary C6 supersaturation constants C0,c0, T=ceil(17 R³ C0³/2), δ=c0/R⁶, and inherited full-source L6=24+153T², L4=q2²ceil_sqrt(ceil(17L6/4))+19T, B0=ceil_sqrt(360(K+1)T), E=5q3ceil_sqrt(L6), D=4ceil_sqrt(B0T L4). All these are exact integer mathematical expressions.

As in #773 (where the entire conditional root error ledger was derived independently), choose

\[
s_0=\max\left\{
2^H,64,
\left\lceil\frac{111T}{2\alpha_1w_{K,H}}\right\rceil,
\left\lceil\left(\frac{E}{\alpha_2w_{K,H}}\right)^2\right\rceil,
\left\lceil\left(\frac{D}{\alpha_3w_{K,H}}\right)^8\right\rceil
\right\}.
\tag{SRG-M}
\]

This gives, **conditional on the separately inherited all-h LOW moment, original FULL A=I mixed source blocker books, ORIGINAL GQ endpoint and exact produced-BBo two-direction inverse**,

\[
BBo_{\rm produced}\ge\frac12w_{K,H}(1-\alpha_1-\alpha_2-\alpha_3)s^6
>\delta s^6
\]

when LOW and D6<δs6. The same **unweighted seven ORIGINAL classes** include disjoint D6 and BBo, so HEAVY/LOW gluing yields the CONDITIONAL original root S_s≥δs6 for all dyadic s≥s0. Never promote conditional proof into actual root PROVED_A until each remaining inherited premise is independently accepted.

## 6. Exact all-h quantitative effect, without pretending formal graph constants are published

For all three purely **FORMAL** external C0/c0 probe values, re-evaluate original previous #773 K=11 with the rough 5/2 source constant versus new fixed H=32, K=10, and same exact rational α allocation, with no original ROOT solver imports:

| FORMAL placeholder (C0,c0) | Old #773 fixed K11 h0 | NEW H32/K10 h0 | Difference |
|---|---:|---:|---:|
| (1,1) | 673 | **667** | −6 |
| (2,1/5) | 703 | **697** | −6 |
| (7/3,1/17) | 710 | **704** | −6 |

The new dyadic cutoff is formally up to 2^6=64 times smaller at these hypothetical numerical inputs. **No published numeric** C_graph/c_graph is supplied by this paper or this repo. These are only exact algebraic examples; external constants remain existential. The improvement does not change the proven c0/R6 conditional HEAVY δ, the s6 exponent, B75 or any general ASET extraction exponent.

The implementation scans K=4,...,64 and reports **ties** for each of these probes; fixed K=10 is among the best h0 values for these 3 probes, not proclaimed optimal for unknown C0 or for arbitrary error allocations. H=32 is a legitimate fixed BEFORE-source threshold and comfortably below any listed formal s0, not computed from the map or a random instance.

## 7. Independent source code, negative guards and scientific dependency status

New standalone research/hyp105_root_srg_frontier_independent.py imports ONLY hyp105_original_defect_factor_referee.genuine_symplectic_source to construct actual 45/425 ORIGINAL named W(3,2)/W(3,4) incidence flags, no historical source J, SRG, ROOT, LOW, selector, GQ, HEAVY, GF5, full-sixset or physical inversion code. Its new source first principles:

- Build BOTH exact ORIGINAL point- and line-collinearity adjacency sets independently of map labels, verify for every ordered pair the true GQ SRG common-neighbor polynomial, exact eigenvalue multiplicities, and EACH nonincident point/line GQ unique projection (not merely a synthetic SRG host).
- For each lex/reverse/shift COMPLETE separately injected original f/g source map, count original point/line collinearity-overlap edges DIRECTLY, and **separately** count FULL named pencil-J edges from all original flag pairs. Require exact equality e(J)=e_col(f)+e_col(g), and both typed source counts independently.
- Build true physical symbol-fibre original source point/line subsets independently, calculate their sum of squared occupancies and true Gram-energy by direct M1_S squared sums, verify the ORIGINAL SRG exact source polynomial identity and numerical ceiling e_col≤V(s−1)+(s²+1)Σd²/(2V)≤C_s with exact Fraction.
- Independently evaluate true actual minimal alphabets a_s for s=64,128,256,512,1024; require strict 19/8 all-h proof envelope and positive K4 at s≥256. Preserve the explicit source distinction: exact finite C_s(s) and universally applicable symbolic M_H are different objects.
- With Fraction and integer arithmetic **only**, recompute old parent K11 root budgets, new H32/K10 root budgets, and independent K=4 source-feasible counterfactual root h0; reject invalid source maps, fake graph constants, odd/small H, illegal K, sign errors, false ROOT promotion, and failing thresholds.
- This is not independent reproof of source no-clone HEAVY→F, global LOW sixth moment and mixed A/C four-blocker, original produced P3→BBo source topology and full 7-class scientific acceptance. Those remain OPEN and are recorded as the next proof gates. Full Research CI, INDEX and specialist must be green at the FINAL exact PR HEAD for engineering acceptance only.

**Verdict:** independent all-h GQ-SRG/source-J first dependency accepted as a discrete mathematical result; the stronger original J bound, K4 asymptotic source frontier and strictly better H32/K10 conditional ROOT ledger are genuine NEW improvements. The main root issue stays OPEN_WITH_FORMAL_BLOCKER, and its next independently reviewable inherited prerequisite is **HEAVY_OWNER_AND_SELECTED_F**, not the already independently reconstructed GQ-SRG/source conflict cap.
