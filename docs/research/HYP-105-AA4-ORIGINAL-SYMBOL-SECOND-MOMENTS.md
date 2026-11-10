# HYP-105 #230 — AA4-SYMMOM: exact all-h ORIGINAL M/G/B by physical symbol second moments; quantified source-label overlap sparsity and heavy-symbol risk gate

**Scientific status:** Draft research child of frozen [#759](https://github.com/definitely-stable/Mathlab/pull/759), parent HEAD \`3a6deb7f70a9c1c1558a6295baab8c8e2da245fb\`, with parent dedicated specialist, INDEX and full Research GitHub-hosted CI all **SUCCESS**. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains OPEN_WITH_FORMAL_BLOCKER. This slice does NOT alter main or parent, does NOT merge or close root, claim global all-label B/M<3/4, certify every HEAVY/LOW/GF(5) inherited source lemma, invent graph C6 numeric constants, or claim any improved ASET exponent.

## 1. Why this precise step, and what is actually new

Earlier #759 proved an important ALL-h source identity: for a fixed ordered physical endpoint family \(\Gamma_{uv}\) of real directed coordinate-proper P3s, the weighted **compatible** path-pair energy \(G_{uv}\) is exactly the physical path diagonal \(D_{uv}\) plus two positive cross-original-middle-owner contributions: middle f/g labels disjoint in BOTH typed coordinates (00) and middle labels intersecting in BOTH coordinates with a common first/last inner physical corner (11). Every distinct path pair with a shared genuine ORIGINAL middle point or line is incompatible. The middle source flags and path weights are real, and physical f/g pair labels are separately globally injective but may be arbitrarily correlated.

However #759's exact source-middle kernel still explicitly examines pairs of possible ORIGINAL middle owners \(i<j\) inside each physical endpoint bin. The new theorem in this slice algebraically removes **even this middle-owner-pair loop**. The entire original compatible and incompatible P3 tensor is now expressible solely through **sparse second moments** of true original source-point/line/symbol/corner marginal weights. For a supplied collection of already exact proper-path weights, the algebraic postprocessing uses O(number of true paths plus occupied marginal entries) sparse additions and squares, not O(number of path pairs) or O(number of middle flag pairs) collision lookups. Bit-complexity of arbitrary-precision Fraction operations and the independent priority marginal computation is accounted separately, not falsely claimed linear.

The new formulas hold for **ANY dyadic s**, ANY fixed separately globally pair-injective, mutually correlated f/g, ANY original retained paired incidence CORE and named deleted Z; no distribution of f/g or independence among different path events is assumed. The adjacent new all-h capacity result additionally uses the **specific minimal alphabet a_s in root issue #230**, and is explicitly separated from the all-alphabet moment identity.

## 2. Exact definitions on a genuine ORIGINAL endpoint bin

Let \(W(3,s)\), \(s=2^h\), have genuine named original point-line incidence flags \(I\). For fixed legal maps

\[
f:P\hookrightarrow\binom{[a]}2,\qquad
g:L\hookrightarrow\binom{[a]}2,
\]

every genuine retained original incidence flag \(i=(p,\ell)\in C\) owns exactly its two actual opposite physical diagonals across the four rectangle corners \(f(p)\times g(\ell)\).

Let \(\Gamma_{uv}\neq\varnothing\) be the set of all actual directed coordinate-proper physical 3paths \(\gamma=(u,a,b,v)\), whose three ORIGINAL named edge owners are pairwise J-independent. Each path has a **strictly positive exact** selector marginal \(t_\gamma\) under one shared original priority order and two shared typed fair-symbol cuts. Thus \(t_\gamma=\Pr(\text{three ORIGINAL owner priorities all local minima})/64\). These probabilities are NOT independent between different paths; the original B/G/M tensors use their products by definition.

For each genuine original **middle** incidence owner i, define

\[
w_i:=\sum_{\gamma\in\Gamma_{uv}: \operatorname{midOwner}(\gamma)=i}t_\gamma,\quad
W:=\sum_i w_i,\quad M_{uv}:=W^2,\quad
D_{uv}:=\sum_\gamma t_\gamma^2.
\]

Let \(P_p=\sum_{i:\operatorname{point}(i)=p}w_i\) and \(L_\ell=\sum_{i:\operatorname{line}(i)=\ell}w_i\). Define middle **physical symbol occupancy masses**

\[
X_x=\sum_{i:x\in f(p_i)}w_i,\qquad
Y_y=\sum_{i:y\in g(\ell_i)}w_i.
\]

The pair and mixed source-symbol occupancies are

\[
Z_{xy}=\sum_{i:x\in f(p_i),\ y\in g(\ell_i)}w_i,
\]
\[
U_{p,y}=\sum_{i:p_i=p,\ y\in g(\ell_i)}w_i,\qquad
V_{\ell,x}=\sum_{i:\ell_i=\ell,\ x\in f(p_i)}w_i,
\quad Q=\sum_iw_i^2.
\]

All are nonnegative sums of genuine weighted source P3s. Physical symbol occupancy satisfies exact marginal conservation \(\sum_xX_x=\sum_yY_y=2W\), \(\sum_{xy}Z_{xy}=4W\), \(\sum_pP_p=\sum_\ell L_\ell=W\), because an ORIGINAL middle pair has precisely two symbols in each factor. No assumptions on pair-label randomness enter these equalities.

## 3. NEW all-h inclusion–exclusion: exact physical middle-label overlap weights from squares

For two source middle incidence flags i,j, separate global pair-label injectivity implies \(|f(p_i)\cap f(p_j)|\) equals 0 or 1 if their genuine original points differ, and equals 2 if their points agree. Thus the **Boolean nonempty-overlap indicator** is exactly

\[
\mathbf1[f(p_i)\cap f(p_j)\neq\varnothing]
=|f(p_i)\cap f(p_j)|-\mathbf1[p_i=p_j].
\tag{SYM-1}
\]

The corresponding g/line identity is identical. Expand arbitrary positive weights \(w_iw_j\) over ALL **ordered** middle flag pairs, including i=j. No path-pair independence is used. The exact weights of ordered middle-pair x and y label intersection are

\[
\boxed{\Omega_x=\sum_xX_x^2-\sum_pP_p^2,\qquad
\Omega_y=\sum_yY_y^2-\sum_\ell L_\ell^2.}
\tag{SYM-2}
\]

Multiply the two Boolean identities in (SYM-1). When original points agree, y-shared-symbol multiplicity is captured by U; when original lines agree, x-shared-symbol multiplicity is captured by V; for both point AND line agree, genuine named original incidence IDs are equal. Thus the exact ordered pair weight of nonempty overlap in BOTH typed middle pair labels is

\[
\boxed{
\Omega_{xy}
=\sum_{x,y}Z_{xy}^2
-\sum_{p,y}U_{p,y}^2
-\sum_{\ell,x}V_{\ell,x}^2
+\sum_i w_i^2.
}
\tag{SYM-3}
\]

Every term is a sparse second moment of actual source marginal weights. Since simultaneous overlap implies each individual overlap, \(0\le\Omega_{xy}\le\min(\Omega_x,\Omega_y)\). Critically, the two subtractions are required: using only \(\sum_{xy}Z_{xy}^2\) would overcount every repeated ORIGINAL source point and line.

By **exact** Boolean inclusion–exclusion, the total ordered middle-flag pair weight with DISJOINT physical first AND second middle pair labels is

\[
\boxed{
G_{00}=W^2-\Omega_x-\Omega_y+\Omega_{xy}.
}
\tag{SYM-4}
\]

Because a true source flag overlaps itself in both typed labels, i=j never enters G00. By #759's genuine source compatibility theorem, **every** distinct proper physical path pair whose ORIGINAL middle labels are disjoint in both types is fully compatible even in the presence of a single shared priority selector, so SYM-4 is an exact positive source contribution to G, not a mere graph relaxation.

## 4. NEW all-h inclusion–exclusion for the FULLY compatible shared-corner 11 channel

For a physical vertex/corner z, define weighted middle FIRST-inner-vertex masses

\[
A_z=\sum_{\gamma:\ a_\gamma=z}t_\gamma,\quad
A_{p,z}=\sum_{\gamma:p_{\mathrm{mid}(\gamma)}=p,\ a_\gamma=z}t_\gamma,
\]
\[
A_{\ell,z}=\sum_{\gamma:\ell_{\mathrm{mid}(\gamma)}=\ell,\ a_\gamma=z}t_\gamma,\quad
A_{i,z}=\sum_{\gamma:\mathrm{mid}(\gamma)=i,\ a_\gamma=z}t_\gamma.
\]

Define exactly analogous LAST-inner-vertex masses \(H_z,H_{p,z},H_{\ell,z},H_{i,z}\) with \(b_\gamma=z\).

For two distinct original middle owners i,j whose genuine original point AND line differ, a shared FIRST inner physical corner z means their x/y pair labels each share precisely one symbol, and #759 proves the two true paths are fully compatible. The sum \(\sum_z A_z^2\) includes ALL ordered pairs sharing the first corner. We must exclude original source pairs sharing an original point or line, which are **always incompatible** if the paths differ, while adding back the doubly subtracted identical ORIGINAL flag IDs. This is exact set inclusion–exclusion on named original source flags:

\[
\boxed{
G_{11}^{\mathrm{tail}}
=\sum_z A_z^2-\sum_{p,z}A_{p,z}^2
-\sum_{\ell,z}A_{\ell,z}^2+\sum_{i,z}A_{i,z}^2.
}
\tag{SYM-5}
\]

Similarly,

\[
\boxed{
G_{11}^{\mathrm{head}}
=\sum_z H_z^2-\sum_{p,z}H_{p,z}^2
-\sum_{\ell,z}H_{\ell,z}^2+\sum_{i,z}H_{i,z}^2.
}
\tag{SYM-6}
\]

These two sets of cross-middle-owner pairs are DISJOINT: if two different physical P3s shared BOTH middle tail a and middle head b, they would use the identical true physical middle edge and hence have the SAME original named middle owner by separate global f/g pair-injection, which is excluded. Therefore \(G_{11}=G_{11}^{tail}+G_{11}^{head}\) is the exact full source-compatible 11 channel, and has no double counting.

## 5. Main NEW all-h theorem — TOTAL ORIGINAL M, G, B by O(source paths) second moments

From #759, **all fully compatible ordered path pairs** in a fixed physical endpoint bin are exactly (i) physical path diagonals \(\gamma=\eta\), (ii) cross-middle ORIGINAL point/line-disjoint source 00 pairs, or (iii) cross-middle ORIGINAL point/line-disjoint source 11 pairs sharing the first or last inner corner. Different paths with a shared original middle point or line are always incompatible. Combining SYM-4–6 proves the NEW identity:

\[
\boxed{
\begin{aligned}
M_{uv}&=W^2,\\
G_{uv}&=D_{uv}+
 \left(W^2-\Omega_x-\Omega_y+\Omega_{xy}\right)
 +G_{11}^{tail}+G_{11}^{head},\\
B_{uv}&=M_{uv}-G_{uv}.
\end{aligned}
}
\tag{SYM-7}
\]

This is not a heuristic/expectation or an inequality. It is an EXACT algebraic evaluation of the whole ORIGINAL same-endpoint P3 compatible/incompatible marginal-product tensor, for ALL legal source orders and correlations, using only:
- sums of weights grouped by real middle ORIGINAL flag, point and line;
- sums grouped by first/second physical middle symbol and their rectangle corners;
- sums grouped by physical FIRST or LAST inner vertex with ORIGINAL middle point/line provenance;
- the physical path-weight diagonal \(D\).

For supplied exact true path marginals, the formula requires **no O(P3²) path pair loop and no O(|C|²) middle flag pair loop**, and it does not inspect any original J cross-path edge. All original source constraints and properness remain prerequisites for the construction of the P3 set and exact marginal weights. In particular, this is an exact **computational/theoretical reduction**, not a proof that the resulting positive mass is \(\Omega(M)\) uniformly across arbitrary fixed f/g.

## 6. NEW all-h heavy-symbol necessary condition for large local/global B/M

Since \(\Omega_{xy}\ge0\) and \(G_{11}^{tail},G_{11}^{head}\ge0\), SYM-7 implies an all-h positive-source lower bound

\[
G_{uv}\ge D_{uv}+M_{uv}-\Omega_x-\Omega_y.
\tag{SYM-8}
\]

Let \(A_x^\ast=\max_xX_x\) and \(A_y^\ast=\max_yY_y\). By nonnegativity and exact occupancy conservation,

\[
\sum_xX_x^2\le2W A_x^\ast,\quad
\sum_yY_y^2\le2W A_y^\ast,
\]

and \(\Omega_x\le\sum_xX_x^2,\ \Omega_y\le\sum_yY_y^2\). Therefore

\[
\boxed{
\frac{G_{uv}}{M_{uv}}\ge
1+\frac{D_{uv}}{M_{uv}}-
2\left(\frac{A_x^\ast}{W}+\frac{A_y^\ast}{W}\right).
}
\tag{SYM-9}
\]

Hence an endpoint family with a **strict** violation \(B_{uv}/M_{uv}>3/4\), equivalently \(G_{uv}/M_{uv}<1/4\), NECESSARILY has

\[
\boxed{
\frac{A_x^\ast+A_y^\ast}{W}
>\frac38+\frac{D_{uv}}{2M_{uv}}.
}
\tag{SYM-10}
\]

In particular, at least one actual physical x/y middle symbol carries strictly more than

\[
\boxed{\frac3{16}+\frac{D_{uv}}{4M_{uv}}}
\]

of the local original path marginal weight. This is a genuinely quantifiable *source physical symbol concentration condition*, not an assertion that it must happen. Conversely, if the sum of maximum relative symbol masses is strictly less than the right side of SYM-10, that source endpoint family is rigorously safe: \(B_{uv}/M_{uv}<3/4\). Equalities MUST NOT be silently promoted to strict bounds.

Summing SYM-8 across bins yields another exact all-h proof gate: if for the true source total \(M=\sum M_{uv}\),

\[
\sum_{uv}(\Omega_{x,uv}+\Omega_{y,uv})
<\frac34 M+\sum_{uv}D_{uv},
\]

then \(G>M/4\) and consequently the **GLOBAL** \(B/M<3/4\) for THAT original source follows. This condition is only **sufficient** and has not been proved for all legal correlated labels; failure does not establish a bad family.

**What this changes for the next original research step:** any global 3/4 failure must be supported by a significant sum of source middle-symbol concentration second moments. It is now possible to state an exact analytic target involving only first-/second-factor symbol star squared masses and source point/line correction terms, instead of all same-endpoint physical path pairs. The next essential obstruction is to bound these star moments under genuine W(3,s) incidence and fixed adversarial f/g.

### 6.1. NEW useful sequential strict local B75 proof gate (D → D+G00 → full G)

The coarse largest-middle-symbol necessary condition (SYM-10) is mathematically correct but **not an effective discriminator on the current finite sources**: the initial full eight-case ORIGINAL W32/W34 scientific certificate found 100% of the same-endpoint M-mass satisfying that *necessary* high-symbol criterion and ZERO endpoint bins certified safe by its strict converse. This does **not** mean all bins are actually dangerous — even in FULL W34 only 8–24 endpoint bins have actual B/M>3/4. Reporting the heavy-symbol condition as a numerically successful adversarial classifier would be misleading.

The exact new source moment decomposition instead supplies a much sharper **monotone three-stage proof certificate** at the individual physical endpoint:

\[
G_{uv}\ge D_{uv},\qquad
G_{uv}\ge D_{uv}+G_{00,uv},\qquad
G_{uv}=D_{uv}+G_{00,uv}+G_{11,uv},
\tag{SYM-13}
\]

with both \(G_{00}\ge0\), \(G_{11}\ge0\). Thus a strict local B/M<3/4 is ALREADY proved if **any** of these successive lower bounds strictly exceeds \(M_{uv}/4\). Define the exact M-weighted fractions of all original endpoint families satisfying these strict tests as \(F_D,F_{D00},F_{FULL}\). They obey the universal inequalities

\[
\boxed{
0\le F_D\le F_{D00}\le F_{FULL}\le1,
\quad
F_{D00}-F_D\ge0,
\quad
F_{FULL}-F_{D00}\ge0.
}
\tag{SYM-14}
\]

The first positive difference measures the actual SOURCE contribution of globally DISJOINT middle-label pairs beyond simple self-compatible path diagonals; the second measures further ORIGINAL source geometry benefit of the shared physical corners where both first-/second-middle symbol pairs overlap. An actual strict locally bad endpoint cannot be certified safe by any of the three tests, and its M-weight share is therefore at most \(1-F_{FULL}\). The exact Fraction program now records each percentage and incremental gain, verifies every monotonicity condition and exports counts with root status unchanged.

For any fixed legal original f/g, the separately valid exact **GLOBAL** source certificate \(\sum_{uv}(D_{uv}+G_{00,uv})>M/4\) alone proves global B/M<3/4 — even without using G11 or individual cross-owner J. Current finite FULL W34 instances all satisfy this *instance* gate because their total D/M alone is approximately 42–44%; it is **NOT** proved uniformly for all legal original labelings and all dyadic orders. The intended next mathematical challenge remains proving such a uniform bound from true GQ source incidence and the weighted symbol collision moments, not extrapolating these fixed-instance tests.

## 7. Separate NEW all-h original source unweighted overlap capacity (minimal alphabet only)

The original #230 ROOT fixes

\[
V_s=(s+1)(s^2+1),\qquad
a_s=\min\{a:\binom a2\ge V_s\},\qquad
F_s=(s+1)V_s.
\]

For **ANY** source point p, its two-symbol pair f(p) can intersect at most \(2(a_s-2)\) OTHER distinct point-pair labels: choose one of the two symbols and the other symbol among the remaining \(a_s-2\). This bound uses only separate global injectivity. Including its own source point, at most \(2a_s-3\) original points have intersecting f pairs. Each original point is incident to exactly \(s+1\) ORIGINAL flags, so the number of other ORIGINAL middle flags whose first pair intersects f(p) is at most \((2a_s-3)(s+1)-1\). Symmetrically for the source line g pair. Thus the potential middle source-flag label-overlap graph has maximum degree

\[
\boxed{
\Delta_{\mathrm{middleOverlap}}
\le\min\{F_s-1,\ 2[(2a_s-3)(s+1)-1]\}.
}
\tag{SYM-11}
\]

Since \(a_s=\Theta(s^{3/2})\), \(F_s=\Theta(s^4)\), the bound yields the global unweighted sparsity ratio

\[
\boxed{
\frac{\Delta_{\mathrm{middleOverlap}}}{F_s-1}
=O(s^{-3/2})
\qquad(s=2^h\to\infty).
}
\tag{SYM-12}
\]

This is a genuine ALL-h incidence-and-minimal-label algebraic result, but **does NOT establish sparsity of source-PRIORITY-WEIGHTED path pairs conditioned on SAME physical endpoints**. Strong endpoint bias may concentrate on precisely those rare overlapping source flag pairs. Claiming \(B/M=o(1)\) directly from SYM-12 would be invalid. If the physical alphabet is larger than the minimal a_s, the degree formula still holds with actual a but the indicated \(O(s^{-3/2})\) consequence may no longer be valid; e.g. star-like pair-injective label maps are possible for a much larger alphabet. The root fixes the minimal alphabet, so the stated corollary applies there, and only there.

The strict machine source capacity certificate also evaluates s=2,4,8,16,32,64 formula-only minimal alphabet envelopes and independently enumerates EVERY ordered source flag neighbor for the two actual finite GQs. It never claims to construct an unsupported W(3,8) incidence fixture merely because its algebraic capacity expression was evaluated.

## 7.1. FINAL independent complete ORIGINAL W32/W34 observed symbol-moment and staged-B75 facts

A NEW dedicated GitHub-hosted code-head specialist [#42867514538](https://github.com/definitely-stable/Mathlab/actions/runs/42867514538) completed **SUCCESS — 19/19 independent tests**, including manual direct ORIGINAL J/typed pairwise enumeration over every same-endpoint P3 pair in W32, an independently implemented previous FULL W34 lex source pairwise referee, and the eight-case strict machine-readable exact Fraction symbol-moment certificate. The following percentages are **display-rounded outputs**, NOT the arithmetic used for acceptance: each exact fraction is preserved in the JSON artifact.

**Breakdown of the WHOLE original G/M source energy into three mathematically disjoint, nonnegative components:**

| TRUE ORIGINAL fixed complete W(3,4) | Physical path diagonal D/M | Middle labels disjoint in both typed coordinates G00/M | Both typed middle labels overlap and shared inner corner G11/M | Exact full B/M |
|---|---:|---:|---:|---:|
| FULL lex | 42.6023% | 21.2847% | 17.1881% | 18.9249% |
| FULL reverse | 41.8919% | 22.2626% | 15.3235% | 20.5221% |
| FULL shifted | 43.9149% | 20.3884% | 15.8328% | 19.8639% |

**The practical diagnostic that matters: exact M-weight of local endpoint bins where strict B_uv/M_uv<3/4 is already mathematically certified by each successive ORIGINAL source lower bound.**

| Fixed original complete W(3,4) | D only certifies safe M | D+G00 certifies safe M | Full exact D+G00+G11 certifies safe M | Actual M share with locally bad >3/4 |
|---|---:|---:|---:|---:|
| FULL lex | 78.2012% | **99.4182%** | 99.9737% | 0.0263% (24 endpoint bins) |
| FULL reverse | 75.5905% | **99.3395%** | 99.9525% | 0.0475% (24 bins) |
| FULL shifted | 79.6068% | **99.6928%** | 99.9855% | 0.0145% (8 bins) |

Therefore the NEW G00 source symbol-disjoint contribution alone increases the fraction of M on which strict local safety is **proved** by **21.2170, 23.7491, 20.0860 percentage points** in these three TRUE FULL W34 sources versus diagonal D alone. The additionally quantified G11 source inner-corner contribution provides **0.5555, 0.6130, 0.2926** percentage points of local-safe M respectively. These are FIXED original finite map source measurements, not guaranteed all-h gains. The safe fractions are **weighted by M_uv**, not fractions of endpoint bins or uniformly random middle flag pairs.

**Negative result for an earlier new proof tactic:** On ALL eight tested W32/W34 ORIGINAL source cases, the high-single-symbol necessary-risk criterion SYM-10 accepts 100% of the physical endpoint M as *potentially* dangerous, hence its strict-safe converse certifies 0% of M. It is mathematically valid but **numerically vacuous as a risk filter on these sources**. This is why the stagewise exact ORIGINAL source moments above, especially G00, are the meaningful next research frontier. Do not report the 100% heavy-symbol necessary condition as an achieved full risk bound.

**Separate all-h minimal-alphabet upper bound on unweighted SOURCE middle label overlap degree:**

| Algebraic original dyadic order s | Minimal physical pair alphabet a_s | ORIGINAL F flags | Maximum theoretical overlapping other flags for one source flag | Bound as fraction of possible other flags |
|---|---:|---:|---:|---:|
| 2 | 6 | 45 | 44 | 100% (vacuous) |
| 4 | 14 | 425 | 248 | 58.4906% |
| 8 | 35 | 5,265 | 1,204 | 22.8723% |
| 16 | 94 | 74,273 | 6,288 | 8.4662% |
| 32 | 261 | 1,116,225 | 34,252 | 3.0686% |
| 64 | 731 | 17,309,825 | 189,668 | 1.0957% |

For s=8 and above these are **algebraic universal capacity bounds**, NOT simulated/constructed higher-order symplectic geometry; only W32/W34 true source pair overlaps are independently scanned directly. Although the unweighted global source overlap density tends to zero, it is logically incorrect to infer the SAME-ENDPOINT selector-marginal-weighted \(B/M\) tends to zero without bounding the source concentration of paths and weights.

**Scientific STOP:** this slice achieves an exact full source sparse second-moment algorithm and exposes the precise high-risk source symbol collision term, but neither the observed 99% safe M certificate in fixed W34 nor the unweighted s^-3/2 incidence capacity proves universally fixed-correlated f/g B75, original seven-class Branch A, the GF5 event union or a new ASET extraction exponent.

## 8. Independent full original source validation and science STOP

The new MAIN referee imports only the independently audited genuine original symplectic W32/W34 incidence/physical paired flag builder and the exact genuine original 3-owner priority probability from #757, then implements the NEW sparse source-symbol-moment algebra **WITHOUT** using any previous path-pair collision, clique, middle-owner-pair kernel or GF(5) code. The exact source risk identity is independently tested against:
- all actual directed proper physical P3 and all actual same-endpoint ordered P3 pairs on full original W32 lex/reverse and original retained shifted-Z17;
- an INDEPENDENT older complete original full W34 lex J/typed pairwise referee;
- exact predeclared original global rational B/M for W32 lex and three FULL W34 labelings;
- all **eight** complete true original W32/W34 CORE cases with real 1,346/1,154/838 and 83,892/82,846/79,404/9,966/66,418 directed coordinate-proper P3s, no path sample cutoff;
- an exact one-path source marginal diagonal-only case and a forged negative/zero source path weight that MUST fail closed;
- source symbol marginals summing to 2W and rectangle corners summing to 4W, all mixed overlap second moment identities, nonnegative G00/G11/B, finite pure-original source flags and the all-h minimal alphabet overlap capacity;
- the heavy-symbol necessary risk condition and separate certification that actual locally bad bins are a subset of eligible high-symbol-concentration bins.

The strict dedicated GitHub-hosted Ubuntu24 Python3.12 specialist runs 19 separate source geometry, mathematical and regression tests and a machine-readable eight-case exact Fraction JSON certificate. INDEX and full Research run independently and must be green on FINAL PR HEAD before claiming complete CI acceptance. Code, tests, workflow and this proof document remain stacked on frozen parent #759; no merge or root issue closure.

**NEW accepted mathematics, subject to final independent hosted tests:** SYM-2/3 symbol-overlap moment identities, SYM-4/5/6 exact G00/G11 positive source weights, SYM-7 exact full-original M/G/B sparse second-moment kernel, SYM-10 source-weight heavy symbol necessary condition for strictly bad local B75, and SYM-11/12 minimal-alphabet **UNWEIGHTED** source-label overlap sparsity.

**Not accepted:** universal all-f/g all-h positive B75 gap or Branch A seven six-ID class theorem, positive global \(S_s(f,g)\ge cs^6\) inferred solely from this exact low-source P3 risk, accepted full HEAVY/LOW/GF(5) root proof DAG, any infinite correlated counterfamily, published numeric ordinary C6 constants, or ASET exponent.

**Next significant allowed step:** source-geometry charge of \(\sum_{uv}(\Omega_{x,uv}+\Omega_{y,uv})\) or the largest-symbol occupancy distribution against \(\sum_{uv}M_{uv}\), with explicit source GQ projection and original path endpoint restrictions, uniformly for every fixed arbitrarily correlated f/g over the minimal alphabet. A fallback is a rigorously valid original correlated infinite family exhibiting persistent middle-symbol star concentration. Do not infer weighted claims from the new unweighted SYM-12 capacity alone.
