# HYP-105 / #230 — AA4-AW: true-original point/line minority-port forcing, sharp integer 2×2 transport, and explicit remaining global gates

**Strict research-only DRAFT child of [AA4-AV #554](https://github.com/definitely-stable/Mathlab/pull/554); parent HEAD frozen at \`c877702263d7dc1d94f4a374495a86ec49685445\`.** The subject remains the actual symplectic \(W(3,s)\), \(s=2^h\), its actual original point-line incidence flag IDs, and ONE global complete injected original-source point physical map \(f\) and original-source line physical map \(g\), without per-wedge relabeling or factor independence. Original HYP-105 issue #230 universal seven-positive-GF5 six-distinct-source-flag lower \(S_s(f,g)=\Omega(s^6)\) is OPEN.

## 1. NEW ALL-h deterministic TRUE-original two-sided port-support theorem

Fix any actual original incidence flag \(i=(p,\ell)\). Let \(\mathcal D_{\rm good}(i)\) be its genuine bilateral GOOD source \(D\)-neighbors from AA4-AP/AA4-AR. The TWO endpoint physical point coordinates of original source factor \(f(p)\) are \(c_0,c_1\); the TWO independent endpoint line coordinates of \(g(\ell)\) are \(e_0,e_1\). Each true original GOOD \(D\)-neighbor has exactly one shared physical point coordinate and one shared physical line coordinate. Set the actual ORIGINAL four nonnegative integer color-bin occupancies \(x_{ab}=\#\{j\in\mathcal D_{\rm good}(i):\text{point shared}=c_a,\text{line shared}=e_b\}\) for \(a,b\in\{0,1\}\).

The genuine original centered GOOD two-edge **opposite in BOTH point and line physical ports** count is

\[
R_i=x_{00}x_{11}+x_{01}x_{10}.
\]

Define ONE-SIDED, readily checkable ACTUAL ORIGINAL GOOD neighbor marginals (point and line separately)

\[
r_0=x_{00}+x_{01},\quad r_1=x_{10}+x_{11},\quad
c_0=x_{00}+x_{10},\quad c_1=x_{01}+x_{11}
\]
and their minority counts \(k_i=\min(r_0,r_1)\), \(\lambda_i=\min(c_0,c_1)\), \(m_i=\min(k_i,\lambda_i)\).

**Theorem AA4-AW1 (all-h, all-global actual original point/line maps, NO independence):**

\[
\boxed{
R_i\ \ge\ k_i\lambda_i-\left\lfloor \frac{m_i^2}{2}\right\rfloor
\ \ge\ \frac{k_i\lambda_i}{2}.
}
\]

Furthermore,

\[
\boxed{
R_i>0\quad\Longleftrightarrow\quad k_i>0\ \ \text{AND}\ \ \lambda_i>0.
}
\]

Thus positive SAME-CENTER both-type opposite physical two-D-edge wedge continuation requires and is implied by **each physical original source factor type seeing BOTH of its own ports among its ACTUAL GOOD original D-neighbors**. Even perfectly adversarial microscopic correlation between point and line physical labels cannot destroy ALL both-type opposite pairs once BOTH original one-sided port supports occur at that center. This is an elementary exact 2×2 integer transportation fact applied to ACTUAL original W3 source flags, not a stochastic independence or generic new spectral theorem.

**Proof, with the stronger sharp minority inequality:** Swapping physical endpoints independently on the point and line side preserves \(R_i\). Thus assume \(r_0=k=\min(r_0,r_1)\) and \(c_0=\lambda=\min(c_0,c_1)\). Write \(t=x_{00}\), \(n=r_0+r_1=c_0+c_1\), and the rest of the table is \(x_{01}=k-t\), \(x_{10}=\lambda-t\), \(x_{11}=n-k-\lambda+t\). Because the chosen row and column are minorities, \(n\ge2\max(k,\lambda)\), so \(n-k-\lambda\ge|k-\lambda|\). Therefore

\[
\begin{aligned}
R_i&=t(n-k-\lambda+t)+(k-t)(\lambda-t)\\
&\ge t(|k-\lambda|+t)+(k-t)(\lambda-t)\\
&=k\lambda-2\min(k,\lambda)t+2t^2\\
&\ge k\lambda-\frac{\min(k,\lambda)^2}{2}.
\end{aligned}
\]

Since \(R_i\) is integer, round the latter expression up to obtain \(k\lambda-\lfloor m^2/2\rfloor\). As \(m^2\le k\lambda\), the second weaker bound follows. When one minority is zero, every opposite-point/line product is zero. When both minorities are positive, \(R_i\ge k\lambda/2>0\), proving iff. Equality in the fractional factor \(1/2\) is realized by the completely balanced abstract nonnegative integer table \(\begin{pmatrix}t&t\\t&t\end{pmatrix}\): \(k=\lambda=2t,R=2t^2=k\lambda/2\). This is a **SHARP numerical inequality**, NOT a claim that every abstract 2×2 table is globally realizable as a genuine symplectic-source f/g physical model.

## 2. NEW AA4-AW2 — EXACT SHARP original local opposite wedge minimum given ONLY one-sided port marginals

Fix original point one-sided GOOD margins \(r_0,r_1\) and original line \(c_0,c_1\), with total \(n\). The 2×2 joint table varies by ONE integer \(t=x_{00}\) with sharp feasible interval

\[
t_-= \max(0,r_0+c_0-n),\qquad
t_+=\min(r_0,c_0).
\]

For this t, the opposite centered two-edge count is the convex integer quadratic

\[
Q(t)=t(n-r_0-c_0+t)+(r_0-t)(c_0-t)
=2t^2+(n-2r_0-2c_0)t+r_0c_0.
\]

Thus, for those ACTUAL original one-sided marginal counts, the exact SHARP margin-only lower is obtained by evaluating Q at the feasible integers nearest \(t_\star=(2r_0+2c_0-n)/4\), clipped to \([t_-,t_+]\). The sharp margin-only upper is \(\max(Q(t_-),Q(t_+))\) since Q is convex. Every table with the specified margins can be reconstructed in the *abstract integer transportation polytope*; no assertion that arbitrary such table can be realized by some globally coherent true W3 maps is made. The new \`exact_two_type_integer_port_marginal_minimum\` reports BOTH the exact sharp local margin-only minimum and the simple \(k\lambda-\lfloor m^2/2\rfloor\) analytic floor.

**Exact re-polarization of AA4-AR:** writing point marginal imbalance \(A=r_0-r_1\), line marginal imbalance \(B=c_0-c_1\), and diagonal contrast \(G=x_{00}+x_{11}-x_{01}-x_{10}\),

\[
\boxed{8R_i=n^2+G^2-A^2-B^2.}
\]

AA4-AR's seemingly two-sided defect \(\Delta=(x_{00}-x_{11})^2+(x_{01}-x_{10})^2\) obeys the exact **ONE-SIDED simplification** \(2\Delta=A^2+B^2\). The joint correlation \(G^2\) is **NONNEGATIVE**. This is a rigorous explanation of why a sufficiently favorable **ONE-SIDED** point and line minority-port profile suffices to force genuine both-type opposite wedges without a point/line independence hypothesis.

## 3. NEW exact global GOOD source flag support census and conditional all-h bridge

Let \(\mathcal I_s\) denote all genuine original incidence flag IDs, and at each center let the above k_i and lambda_i be computed from ACTUAL GLOBAL SAME f/g physical GOOD-neighbor bins, not independent physical source factor copies. Then deterministic ALL-h all-global:

\[
\boxed{R_{\rm GOOD}=\sum_iR_i
\ \ge\sum_i\left(k_i\lambda_i-\lfloor m_i^2/2\rfloor\right)
\ \ge\frac12\sum_i k_i\lambda_i.}
\]

**EXACT support theorem:** Number of genuine original source flag centers supporting at least ONE physically opposite two-typed GOOD wedge equals the number of centers where BOTH independently typed marginal minima are POSITIVE. Every source-typed opposite wedge has three distinct original source point factors and three distinct line factors, so it qualifies as source A/A, but may fail original residual 3×3 Hall and final seven-GF5 selection.

The separate direct original GOOD D adjacency routine \`exact_true_original_good_minority_port_certificate\` reports for every actual source incidence flag ID: four x bins, one-sided point/line port marginals, minority product, sharp margin-only integer lower and actual R_i; sums these across ALL genuine original source flags. Independent direct outer-neighbor physical port pair enumeration verifies exact opposite wedges without using sharp minimization at all. For each real original W32/W34 global map, report center support counts grouped by whether both point and line one-sided ports are active, only one side active, or neither. All numerical results are tied to exactly the globally fixed actual original maps and no source factor remapping.

**Two explicit still-UNPROVED but SUFFICIENT all-global gate hypotheses:** For some constants \(\alpha\in(0,1/4]\), \(\beta\in(0,1]\), all sufficiently large h>=16 and EVERY original globally fixed f,g, let
- H1 (point/line one-sided **minority mass**): \(\sum_i k_i\lambda_i\ge\alpha\sum_i(\deg_{\rm GOOD}i)^2\).
- H2 (TRUE SIX ORIGINAL incidence-ID selected-GF5 source extension): at least beta fraction of all REAL physically opposite two-type GOOD 3-flag wedges appears as a 3-subset of at least one **ACCEPTED genuine original seven-GF5 six-ID Q**, using same global f/g.

By AA4-AV unconditional genuine source A/A GOOD wedge bound \(W_{AA}\ge s^6/10\), \(\sum_i\deg_{\rm GOOD}(i)^2=2W_{\rm GOOD}+2E_{\rm GOOD}\ge2W_{AA}\ge s^6/5\). By the new minority theorem and existing AA4-AR true original accepted Q capacity of at most SIX centered GOOD wedges per accepted Q:

\[
R_{\rm GOOD}\ge\tfrac12\sum_i k_i\lambda_i
\ge\tfrac\alpha2\sum_i\deg_{\rm GOOD}(i)^2
\ge \tfrac\alpha{10}s^6,
\]

\[
\boxed{
\text{H1 and H2 together}\quad\Longrightarrow\quad
S_s(f,g)\ge\frac{\alpha\beta}{60}s^6.
}
\]

The first condition is STILL a nontrivial simultaneous global f/g physical-port activity/mass theorem not proved, and the second condition is STILL an independent true original 3-new-flag Hall and final GF5 sixset selection theorem not proved. The displayed accepted S lower is **STRICTLY CONDITIONAL**. AA4-AT/AU already demonstrated finite genuine original source Hall zeros even for completely occupied physical K6, so H2 cannot be inferred from H1.

### 3.1. Independently verified same-global ORIGINAL W32/W34 all-source-center one-sided port support census

The first [AA4-AW dedicated GitHub-hosted exact HEAD #38878211672](https://github.com/definitely-stable/Mathlab/actions/runs/38878211672) completed **4/4 SUCCESS**. Its independent all-abstract 2x2 integer transportation oracle examined **3,876** different nonnegative four-bin integer source-port tables with total degree 0..15, matching the exact sharp fixed-marginals convex optimizer and minority forcing theorem on each. The actual original W(3,2) complete global typed maps and W(3,4) global typed maps with six missing physical pair images per type were compared to a SECOND true-original literal two-flag GOOD D neighbor-pair source oracle. These are real original flag IDs from actual symplectic W3s and ONE fixed f and g per model, not synthetic source geometry.

For every real ORIGINAL source flag center i, the local support theorem verified in all seven actual symplectic models: at least one physically opposite two-type GOOD two-edge centered wedge **iff** each of its own two point-typed physical endpoint ports and two line-typed physical endpoint ports is used by some genuine GOOD original D-neighbor.

| Actual ORIGINAL W(3,2) fixed complete global point f/line g | True source GOOD D edges | Source A/A GOOD threeflag wedges | \(\sum_i k_i\lambda_i\) | \(\sum_i[k_i\lambda_i-\lfloor m_i^2/2\rfloor]\) elementary lower | \(\sum_i R_i^{\min}\) SHARP fixed-marginal original-port lower | ACTUAL two-type physically opposite GOOD source wedges |
|---|---:|---:|---:|---:|---:|---:|
| dual-zero | 277 | 2,675 | **1,292** | 702 | 821 | **870** |
| lex | 307 | 3,259 | **1,575** | 871 | 1,000 | **1,105** |
| reverse | 300 | 3,141 | **1,553** | 873 | 968 | **1,013** |
| S68 | 257 | 2,268 | **1,003** | 561 | 683 | **697** |
| S72 | 261 | 2,346 | **1,078** | 616 | 714 | **750** |

Every one of the TRUE 45 original W32 source incidence flag centers in EACH of these five globally complete typed K6 physical maps had both one-sided physical point ports and both line ports active. This finite low-h observation DOES NOT prove every such original source center remains two-sided active for any sufficiently large h or for ALL injected f,g.

| Actual symplectic ORIGINAL W(3,4) same global physically injected K14 point f/line g (six missing pair images each side) | Actual GOOD original D edges | Source A/A GOOD threeflag wedges | \(\sum_i k_i\lambda_i\) | Sharp fixed-marginal opposite wedge lower | ACTUAL physically opposite GOOD original source wedges |
|---|---:|---:|---:|---:|---:|
| lex | 2,072 | 20,650 | **4,344** | 3,174 | **3,544** |
| random | 147 | 158 | **8** | 8 | **10** |

The real ORIGINAL 425 source center flag IDs break down by which two typed **one-sided** port supports are active:

| W34 fixed point f/line g | Both point & line ports active | Point ports only | Line ports only | Neither side both ports |
|---|---:|---:|---:|---:|
| lex | **118** | 107 | 106 | 94 |
| random | **6** | 5 | 20 | **394** |

These EXACT 425-point-line-flag partitions agree with an independent literal source-neighbor support referee and hence directly explain the observed loss under correlated globally injected physical hole patterns. In particular random globally fixed W34 has 394/425 true original source incidence centers without both ports active on either type, and only SIX centers with simultaneously active point and line ports, but all observed ten R_good physically opposite wedges occur at those six centers. Since W34 has h=2, the data do not show that positive simultaneous port support can be destroyed asymptotically for all large h.

**Low GF5 transfer control:** Actual original W32 globally injected S68 has 697 real GOOD physically opposite source threeflag wedges and a rigorous sharp margin-only lower 683, yet the INDEPENDENT true six-distinct original source ID seven-GF5 oracle finds only SIX distinct GOOD source wedges that lie in any accepted original sixset. For S72 actual R_good=750, sharp marginal floor=714, but only 11 GOOD source wedges covered by selected original GF5 sixsets. This is an explicit finite *second* obstruction: once the physical two-port gate is certified, genuine original source 3×3 Hall and final sevenclass selection are separate and may still wipe out almost all GOOD source wedges.

**Scientific interpretation:** The all-h exact biconditional is a local **support** theorem that avoids proving any point/line JOINT local color independence; it does not yield an all-map lower on the number or strength of source centers that possess BOTH one-sided physical port supports. The global quantity \(\sum_i k_i\lambda_i\), rather than a full 2x2 covariance/mixed physical port assignment, is the next precise source×global-physical bottleneck. Even if a uniform lower for it is eventually proved, the independent original Hall + selected seven-GF5 bridge remains open.

## 4. Testing strategy and rigorous limits

1. Exhaustively enumerate ALL small abstract 2×2 nonnegative integer tables of total degree 0..15 and independently compare the new closed-form sharp original transport margin minimum to a completely SEPARATE brute scan over all feasible t, with positive-port support equivalence. Explicit abstract balanced examples attain the half minority-product bound (sharp coefficient). Such tables are solely combinatorial counter/positive examples, not fabricated original W3 data.
2. Actual ORIGINAL W32 five complete globally bijective typed K6 source physical f/g maps dual-zero/lex/reverse/S68/S72, ALL true original GOOD D-source pairs and ALL actual original 45 flag centers; independent literal GOOD D neighbor pairs verify R and per-center point/line one-sided support masks; historical AA4-AR 3-flag source and port counts used only for crosschecks. The TRUE original source selected GF5 coverages 6/2715 S68 and 11/2811 S72 demonstrate that H1 / locally positive R does not imply H2.
3. Genuine ORIGINAL symplectic W34 GF4 global fully injected typed K14 point/line maps lex/random (six missing global physical pair edges each type), all source GOOD D original flag-centered port bins and independent literal original source opposite centered wedges. No false full W34 seven-GF5 census.
4. Original source symplectic transvection and independent typed physical vertex coordinate permutations must preserve every global minority-product and sharp fixed margins count. Reject malformed original source incidence lists, duplicate global physical factor labels and noninteger negative arbitrary 2×2 inputs.
5. Exact Fraction rational conditional all-h>=16 alpha beta bridge verified symbolically through h60, with unsupported h<16 explicitly gated.

**Scientific integrity:** 2×2 nonnegative matrix transportation, convex quadratic minimization and the half-minority product inequality are elementary mathematics, not a new general field theorem. Their useful specific outcome for issue #230 is the **EXACT genuine original same-GLOBAL two-type physical port support iff** and the quantitative certificate that **cross-map correlation cannot eliminate local opposite port wedges once both one-sided physical original source point/line minority-port populations are present at that center**. It replaces an uncontrolled local joint-color covariance assumption by a simpler simultaneous one-sided support/mass gate. It does not resolve that global gate or the independent original Hall/GF5 extension. Main untouched; Draft stacked child; issue #230 OPEN; require exact-HEAD dedicated GitHub-hosted, INDEX, Proof Audit, Full Research and independent mathematical referee before integration.

**Next AA4-AX:** prove an ALL-original-GQ ALL-complete-global-f/g positive lower for the new simultaneous single-sided minority-port energy \(\sum_i k_i\lambda_i\) from the true symplectic original incidence source graph and physical pair injection constraints. That would give unconditional physically opposite GOOD A/A wedges. Separately obtain source 3-new-flag Hall and selected GF5 positive extension or independent U-class lower. Exact W32/W34 per-center marginal counters and rigorous adversarial one-sided monochromatic-port obstruction cases should guide attempts. Avoid extrapolating finite W32 S68 low selected coverages to an infinite f_s,g_s counterfamily.
