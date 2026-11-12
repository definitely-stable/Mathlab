# HYP-105 / #230 — AA4-NBRCHARGE: all-h ORIGINAL source-middle overlap-neighborhood charge and Laplacian identity

**Scientific scope.** Strict Draft child of [#760](https://github.com/definitely-stable/Mathlab/pull/760), frozen HEAD \`f593e792d41229550f50ffacf36ab2b6eafc9be7\`, at which dedicated, INDEX and complete Research were all SUCCESS. The new result is an exact theorem about the ORIGINAL symplectic GQ physical pairing source and a new **necessary concentration obstruction** to local \(B_{uv}/M_{uv}>3/4\). Neither this result nor its complete finite W32/W34 tests prove global \(B/M<3/4\) for arbitrary fixed correlated \(f,g\), complete the original HEAVY/LOW/GF(5) seven-class DAG, or give an ASET exponent. Issue #230 remains OPEN_WITH_FORMAL_BLOCKER and main is untouched.

## 1. Choose the mathematically honest obstacle: conditional overlap weight, not global label sparsity

Parent #760 proved for every dyadic \(s=2^h\) and every fixed separately globally pair-injective, mutually correlated \(f:P\hookrightarrow\binom{[a]}2\) and \(g:L\hookrightarrow\binom{[a]}2\) on the true ORIGINAL symplectic generalized quadrangle \(W(3,s)\) that the weighted same-endpoint proper physical three-path tensor has an **exact** sparse-second-moment representation.

For each ordered physical endpoint bin \((u,v)\), write \(w_i=\sum_{\gamma:\,\operatorname{midOwner}(\gamma)=i}t_\gamma>0\) for the sum of real **positive** original-priority-and-cut path marginals of true proper P3s with retained ORIGINAL named middle incidence flag \(i=(p_i,\ell_i)\). Here paths are true physical walks \((u,a,b,v)\) with distinct typed vertices, paired physical opposite ORIGINAL diagonals, unique original edge owners, and actual source owner triple satisfying the J-proper constraint. Different path selection events are NOT assumed independent. By definition, the compatible/incompatible weights \(G,B\) below sum products \(t_\gamma t_\eta\).

Define \(W=\sum_i w_i\), \(M_{uv}=W^2\), physical path diagonal \(D=\sum_{\gamma}t_\gamma^2\), and \(G_{11}\ge0\) the exact shared FIRST/LAST interior corner source contribution proved in #759/#760. The parent exact theorem is

\[
\boxed{
G_{uv}=M_{uv}-R_{uv}+D_{uv}+G_{11,uv},
\qquad
B_{uv}=R_{uv}-D_{uv}-G_{11,uv}.
}
\tag{N-1}
\]

Here \(R_{uv}=\Omega_{x,uv}+\Omega_{y,uv}-\Omega_{xy,uv}\) is the **CORRECTED UNION** of first- or second-type middle ORIGINAL physical label overlaps; using the uncorrected \(\Omega_x+\Omega_y\) double counts both-overlap pairs and is invalid as an exact source obstruction.

Parent #760's global unweighted overlap capacity \(\Delta=O(s^{5/2})\) out of \(F=\Theta(s^4)\) genuine source flags under minimal pair alphabet is correct but cannot, by itself, control the **conditional-weighted** source overlap mass \(R_{uv}/M_{uv}\) at a fixed physical endpoint. A fixed source may concentrate its path marginals on a small overlap family. This slice instead identifies the **specific named ORIGINAL middle source neighborhood** that must be heavy whenever an endpoint is actually bad.

## 2. ALL-h exact closed ORIGINAL source middle-label neighborhood

For occupied named original middle incidence flags \(i=(p,\ell)\), \(j=(q,m)\), define the symmetric \(0/1\) kernel WITH self-loops

\[
H_{ij}=
\mathbf1\!\left[
f(p)\cap f(q)\ne\varnothing
\ \lor\
g(\ell)\cap g(m)\ne\varnothing
\right].
\tag{N-2}
\]

This uses the actual fixed physical labels of the original point and line; not the source selector J graph or a synthetic abstract edge substitute. Since \(i=j\) shares both label pairs, \(H_{ii}=1\). Let \(\mathcal N_i=\{j:H_{ij}=1\}\) be the CLOSED source physical-overlap neighborhood of i **restricted to the middle owner flags actually present at this endpoint**. Define its exact weight

\[
N_i=\sum_{j\in\mathcal N_i}w_j,\qquad
d_i=|\mathcal N_i|,\qquad
\delta=\max_i d_i,\qquad
\rho=\max_i\frac{N_i}{W}.
\tag{N-3}
\]

Because this is a symmetric kernel and the original second-moment union overlap counts ordered pairs including self, the following identity is EXACT, not an estimate:

\[
\boxed{
R_{uv}=\sum_{i,j}H_{ij}w_iw_j
=\sum_iw_iN_i.
}
\tag{N-4}
\]

This equation is true for ANY positive source path marginal weights (the true original priority marginals are an important special case), for every h and arbitrary f/g correlations. It requires no probabilistic independence or averaging over labels.

### New original-label postings formula — same exact N_i in O(1) occupied-moment reads per flag

Let \(X_x,Y_y,Z_{xy}\) be original middle weights grouped by the x symbol, y symbol, and simultaneous (x,y) rectangle corner as in #760. Let \(P_p,L_\ell,U_{p,y},V_{\ell,x}\) be the ORIGINAL point, line, mixed point-y and line-x occupancy. If \(f(p)=\{x_0,x_1\}\), \(g(\ell)=\{y_0,y_1\}\), then the exact weight of all OTHER original middle flags (plus i itself) whose x-pair overlaps f(p) is

\[
S_x(i)=X_{x_0}+X_{x_1}-P_p,
\]

because the original point-pair label \(f(p)\) shares both x symbols with itself and only one with any OTHER original point's pair by global pair injection. Likewise \(S_y(i)=Y_{y_0}+Y_{y_1}-L_\ell\).

The both-overlap common part is EXACTLY

\[
S_{xy}(i)=\sum_{x\in f(p),y\in g(\ell)} Z_{xy}
-\sum_{y\in g(\ell)}U_{p,y}
-\sum_{x\in f(p)}V_{\ell,x}
+w_i.
\]

The source mixed correction terms and the final plus \(w_i\) are essential. Thus

\[
\boxed{
N_i=S_x(i)+S_y(i)-S_{xy}(i).
}
\tag{N-5}
\]

This theorem gives a **source-specific weighted neighborhood charge** using only the already available exact sparse second moments, without enumerating source-middle flag pairs. The new independent referee evaluates N_i two mathematically different ways: (A) actual set union of four original x/y symbol postings and summing unique named source flag IDs; (B) independent algebra (N-5) with point/line correction terms. It requires exact Fraction equality for every occupied middle owner in every actual physical endpoint bin. A third independent check compares the total \(R=\sum_iw_iN_i\) with parent \(R=\Omega_x+\Omega_y-\Omega_{xy}\) computed from all symbol SECOND MOMENT squares.

## 3. NEW all-h quantitative 75% obstruction: one *heavy ORIGINAL source neighborhood*

Since \(R_{uv}/M_{uv}\) is a weighted average of the neighbor fractions \(N_i/W\) under weights \(w_i/W\), (N-4) gives

\[
\boxed{
\frac{R_{uv}}{M_{uv}}\le
\rho_{uv}=\max_i N_i/W.
}
\tag{N-6}
\]

Substituting into exact (N-1),

\[
\boxed{
\frac{B_{uv}}{M_{uv}}\le
\rho_{uv}-\frac{D_{uv}+G_{11,uv}}{M_{uv}}.
}
\tag{N-7}
\]

Thus **NEW all-h heavy-neighborhood necessity**:

\[
\boxed{
\frac{B_{uv}}{M_{uv}}>\frac34
\Longrightarrow
\exists i=(p,\ell):\
\frac{
  \sum_{j:\ f(p)\cap f(p_j)\ne\varnothing\
      \lor\ g(\ell)\cap g(\ell_j)\ne\varnothing}w_j
}{W}
>
\frac34+\frac{D_{uv}+G_{11,uv}}{M_{uv}}.
}
\tag{N-8}
\]

Every i and j here is a TRUE actual ORIGINAL middle physical P3 incidence owner for the FIXED ordered endpoint family; no cloned source motif is allowed. The right side is **strictly larger than 3/4** as D>0. In particular, the presence of an actual strict-B75 bad endpoint requires over three quarters of its middle flag weighted path mass to lie inside ONE small explicit ORIGINAL label-overlap neighborhood.

This has a concrete and valid global counterpart, with a necessary-vs-sufficient distinction: if the WHOLE fixed source satisfies global \(B/M\ge3/4\), then some nonempty endpoint bin has local \(B_{uv}/M_{uv}\ge3/4\), and some i in that bin has \(N_i/W\ge3/4+(D+G_{11})/M_{uv}\) by (N-7). This is a **LOCALIZED COUNTERFAMILY WITNESS requirement**, not a uniform proof ruling out that witness for every f/g. To prove global B/M<3/4 one still needs a source-geometric bound excluding sufficient aggregate risk or a direct global second-moment estimate.

Conversely, the strict inequality

\[
\boxed{
\rho_{uv}
<
\frac34+\frac{D_{uv}+G_{11,uv}}{M_{uv}}
}
\tag{N-9}
\]

is a sufficient LOCAL strict B75 safety certificate. Equality cannot be silently promoted. The program reports exact **M-weighted fractions**, not arbitrary numbers of bins, which are certified safe by N-9 versus the actual strict-bad M fraction.

## 4. NEW all-h GQ and minimal-alphabet small *support* of the heavy neighborhood

The root fixes the minimal physical pair alphabet

\[
V=(s+1)(s^2+1),\qquad
a_s=\min\{a:\binom a2\ge V\},\qquad
F=(s+1)V.
\]

For ANY original point p, its physical pair f(p) intersects no more than \(2(a_s-2)\) other separately pair-injective ORIGINAL point pair labels. Including p, at most \(2a_s-3\) distinct original points. Every ORIGINAL point is incident with exactly s+1 ORIGINAL flags. Consequently for each original middle flag i at most \((2a_s-3)(s+1)-1\) other original middle flags can overlap in the first symbol pair, and the same for the second factor; union bound:

\[
\boxed{
d_i\le \delta\le
d_{\rm global}=
1+\min\bigl(
F-1,\,
2[(2a_s-3)(s+1)-1]
\bigr).
}
\tag{N-10}
\]

This is an all-order deterministic **SOURCE LABEL SUPPORT** bound on the number of flags in any such heavy neighborhood. At minimal a_s it is \(O(s^{5/2})\) vs \(F=\Theta(s^4)\); therefore if global B/M≥3/4 an endpoint must concentrate more than 75% of weighted path middle-owner mass on **at most O(s^{5/2}) ORIGINAL incidence flags** belonging to one potential physical-label-overlap neighborhood. These are still quite numerous; this theorem is NOT an all-h contradiction by itself because weights may be extremely endpoint-biased.

The actual endpoint-specific \(\delta\) can be far smaller than the global capacity; the referee measures both and never substitutes a random-label bound or a normalized all-source degree for the conditional endpoint degree.

## 5. NEW exact source graph Laplacian quadratic identity and effective-support dichotomy

Let \(Q=\sum_iw_i^2\), \(\nu=M/Q\) the positive effective number of true original middle owner groups. Because H is a symmetric 0/1 matrix with self-loops, standard finite weighted graph algebra gives

\[
\boxed{
\sum_i d_iw_i^2-R_{uv}
=\sum_{\{i,j\}:i<j,\,H_{ij}=1}(w_i-w_j)^2
=\mathcal E_H(w)\ge0.
}
\tag{N-11}
\]

This **EXACT** source-original Dirichlet/Laplacian identity detects nonuniformity of middle-group weights along real source label-overlap edges (loops contribute zero). In particular, with \(\delta=\max_i d_i\),

\[
\boxed{
R_{uv}\le\sum_i d_iw_i^2\le\delta Q.
}
\tag{N-12}
\]

Other independent, universally valid source-only bounds are

\[
R_{uv}\le W\max_iN_i
\quad\text{and}\quad
R_{uv}\le W\,T_\delta,\qquad
T_\delta=\text{sum of the largest }\min(\delta,q)\text{ weights }w_i,
\tag{N-13}
\]

where \(q\) is the number of actually occupied original middle owner flags. Also \(R\le\delta W\max_iw_i\). Each yields a non-pairwise sufficient strict safety certificate when its upper bound minus D and G11 is strictly below \(3M/4\). These candidate bounds are **not all ordered by strength**: in particular the weighted degree square energy and maximum-neighborhood bound are incomparable in general. The test suite explicitly avoids assuming one always dominates the other.

From \(R/M>3/4+(D+G_{11})/M\) for strictly locally bad endpoint and \(R\le\delta Q\), another all-h necessary obstruction follows:

\[
\boxed{
\frac{B_{uv}}{M_{uv}}>\frac34
\Longrightarrow
\nu=\frac{M_{uv}}{Q}
<
\frac{\delta}{\frac34+(D_{uv}+G_{11,uv})/M_{uv}}.
}
\tag{N-14}
\]

This is a formal **effective source support** concentration condition. If an actual endpoint has sufficiently many effectively weighted true original middle flags relative to its measured overlap degree \(\delta\), the strict local-B75 violation is impossible. Under fixed f/g the source flags may be highly nonuniform and \(\delta\) may be large; no unconditional conclusion is smuggled into (N-14).

## 6. Independent original W32/W34 full census + failure gates

The new standalone source referee imports ONLY the independently audited true ORIGINAL \(W(3,s)\) symplectic incidence/paired physical edge builder, true original proper physical P3 enumerator and exact original 3-owner priority probability, plus the previously verified algebraic minimal-alphabet capacity. It does **NOT** reuse an earlier moment-collision kernel to calculate N_i, R or B. For each actual fixed ordered endpoint it:
1. Generates all true original physical P3s with exactly their owned original middle incidence flags and exact positive Fraction marginals.
2. Computes each actual source middle label overlap neighbor set by inverted physical symbol postings (real named source owner IDs).
3. Independently computes each weighted N_i from the new O(1) moment formula (N-5), then computes R by summing w_i N_i.
4. Separately computes R via x/y/both symbol-square moments, and G11 via an independent first/last physical inner-vertex owner-provenance inclusion–exclusion. It requires exact M=B+G and B=R-D-G11.
5. Audits the original source Laplacian energy \(\mathcal E_H\), unweighted minimal alphabet degree cap, spectral/top-weight/max-neighbor risk bounds, conditional bad-bin witness and strict source 75% candidate/safe bin population.
6. Exports for a genuine bad local bin the actual physical ordered endpoints, source middle ORIGINAL flag ID, original point/line labels, entire source neighbor list, the source neighbor mass fraction and exact local threshold. A fake SOURCE non-pair-injective label map or invalid marginal must fail closed.

The independent dedicated suite covers all EIGHT complete source cases, **W32** full lex/reverse/shift Z17 proper directed P3 counts 1,346 / 1,154 / 838, and **W34** full lex/reverse/shift/even CORE/shift Z17 CORE 83,892 / 82,846 / 79,404 / 9,966 / 66,418. No 2,000-path sampling, false small-Z extrapolation or substitution of unrelated graph edges. For W32, tests DIRECTLY enumerate EVERY same-endpoint ordered P3 pair and charge actual original middle-label overlaps independently of the new postings/moment method; for W34 all three FULL label schemes, tests compare EVERY endpoint bin's exact M/G/B/R/D/G11 against the already separately verified previous symbol-second-moment referee (#760). A separate algebra-only nonuniform reweighting adversarial test verifies N-11 without claiming arbitrary weights are actual selector marginals.

**Hosted CI:** Ubuntu24 Python3.12 specialist with 17 independent tests plus strict machine-readable eight-source Fraction JSON, alongside inherited INDEX and full Research workflows. Final-HEAD statuses must be checked before any success claim; no merge and root stays open.

## 7. Acceptance, scientific result and next permitted proof step

**Proved all-h analytically:** (N-4) exact original label-overlap neighborhood weighted charging; (N-5) independent O(1) per-middle-source-flag moment inversion; (N-8) heavy-neighborhood necessary obstruction to local strict B75; (N-10) source support degree upper under minimal alphabet; (N-11) EXACT source original overlap Laplacian identity; (N-12) spectral/effective-support obstruction; and quantified **conditional** strict-safe tests. Each is proven under all fixed legal f/g correlations and the original P3 source assumptions, not by fitting finite counts.

**NOT proved:** that no such heavy source neighborhood can exist with adversarial fixed labelings; an all-h universal global B/M<3/4, or complete original seven GF5 class motif Branch A acceptance. Even if every empirically bad endpoint belongs to a small source-weighted neighborhood, a global weighted P3 risk bound requires a true incidence/endpoint uniformity or direct sum-of-squared-source-moments charge. The new necessary obstruction may itself be numerically non-discriminating in some fixed sources; inspect the exact certified safe M fractions rather than claiming automatic progress.

**Next genuinely high-value step:** use true GQ incidence/projector structure and physical endpoint constraints to control \(\sum_{uv} w_iN_i\) *globally*, or prove a source-dependent upper on conditional neighborhood weights \(N_i/W\) for legal f/g, or construct an explicit legal dyadic infinite adversarial correlated family with heavy source neighborhoods. Distinguish these tasks from unweighted pair-label capacity alone. No merge, issue closure, external numeric graph supersaturation constant or new ASET extraction exponent.
