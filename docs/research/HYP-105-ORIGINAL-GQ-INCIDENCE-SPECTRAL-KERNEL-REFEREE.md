# HYP-105 / #230 — AA4-GQSPECTRAL: independent original GQ spectrum and exact dual book kernel loss

Scientific Draft stacked on frozen PR #697, exact parent HEAD 75716c7e29ae25d3b96b3cf498c31992cf9e0e7a. Only genuine symplectic W(3,s), complete ORIGINAL point/line incidence flag IDs, and separately injective fixed but arbitrarily correlated physical pair maps f,g. No merges, main changes, or issue closure; OPEN_WITH_FORMAL_BLOCKER.

## 1. All-h independent combinatorial derivation

Let s=2^h, V=(s+1)(s²+1), and B be the ACTUAL V-by-V ORIGINAL point-line incidence matrix. The generalized quadrangle axiom gives: each point belongs to s+1 lines, two different points share at most one line, each point has k=s(s+1) other collinear points; for distinct adjacent points lambda=s−1 common collinear neighbors (all on their unique line), while distinct nonadjacent points have mu=s+1 common neighbors (one from each line through either point, by the unique-projection axiom).

For the ORIGINAL point-collinearity adjacency matrix A, the exact identity is

\[
\boxed{A^2=(s^2-1)I-2A+(s+1)J,\qquad BB^\top=(s+1)I+A.}\tag{S1}
\]

On the all-one vector A has eigenvalue k. On its orthogonal complement the first identity gives eigenvalues s−1 and −(s+1). Therefore the true original incidence Gram matrix BBᵀ has eigenvalues (s+1)², 2s, 0. Their exact multiplicities, derived using trace A=0 and dimension V, are respectively

\[
\boxed{1,\quad \frac{s(s+1)^2}{2},\quad \frac{s(s^2+1)}{2}.}\tag{S2}
\]

Because B is square, BᵀB has exactly the same eigenvalues and multiplicities. The ORIGINAL source singular values s+1, sqrt(2s), 0 used by #655/#659/#697 thus follow from first-principles GQ axioms; this is not a fitted finite-h numerical spectrum. The proof is equally valid after swapping original points and lines.

## 2. Exact dual spectral book EQUALITY, not just an upper

For any complete injective right map g on ORIGINAL lines, define L_y={ell: y belongs to g(ell)}, k_y=|L_y|<=a−1 and sum_y k_y=2V, where a is the minimal physical pair alphabet. On the original point pencils let r_py=number of ORIGINAL incident lines ell in L_y. The full original book is

\[
M_g=\sum_{p,y}\binom{r_{py}}2.
\]

It also equals the independent ORIGINAL-factor-pair-major count: choose two different original lines meeting at exactly one original point and sharing one physical g coordinate. Since the original geometry and physical pair labels are simple, each such unordered line pair is counted exactly once.

Let v_y be the 0–1 line-star vector, Q=BᵀB and P_0 the orthogonal projector onto the TRUE original incidence kernel. By (S2), without numerical diagonalization,

\[
\boxed{P_0=\frac{(Q-(s+1)^2I)(Q-2sI)}{2s(s+1)^2}.}\tag{S3}
\]

It is exactly idempotent and positive semidefinite; BP_0=0. Decomposing v_y into the all-ones, 2s-eigenspace and zero-eigenspace gives

\[
\|Bv_y\|^2=2s k_y+\frac{s^2+1}{V}k_y^2-2s\|P_0v_y\|^2.
\]

Since sum r_py=2V(s+1) over all p,y, substituting into the book definition yields the ALL-h EQUALITY

\[
\boxed{
M_g=(s-1)V+\frac{s^2+1}{2V}\sum_y k_y^2-s\sum_y\|P_0v_y\|^2.
}\tag{S4}
\]

The identical formula with the original point-factor Gram BBᵀ gives M_f for the fixed left map f. No f/g independence is needed.

## 3. New two-defect accounting and uniform unused-label strengthening

The prior source bound C_s=(s−1)V+(s²+1)(a−1) equals (s²+1)(s²+a−2). Rearranging (S4) with sum k_y=2V gives the EXACT nonnegative slack identity

\[
\boxed{
C_s-M_g=
\frac{s^2+1}{2V}\sum_y k_y(a-1-k_y)
+s\sum_y\|P_0v_y\|^2.
}\tag{S5}
\]

The two contributions independently quantify (i) unused physical coordinate pair labels and (ii) ORIGINAL incidence-nullspace mass. They are rational and nonnegative for EVERY fixed legal map, not only generic maps.

Put t=binom(a,2)−V, the exact count of unused pair labels. Minimality of a implies 0<=t<a−1. Let m_y=a−1−k_y be the degree of coordinate y in the unused-label graph. Because m_y<=t, and each missing pair {u,v} contributes k_u+k_v to sum_y k_y m_y,

\[
\sum_y k_y m_y
=\sum_{\{u,v\}\text{ unused}}(k_u+k_v)
\ge 2t(a-1-t).
\]

Consequently, entirely from the genuine source axioms and coordinate pair injection,

\[
\boxed{
M_f,M_g\le C_s-\frac{s^2+1}{V}t(a-1-t).
}\tag{S6}
\]

For W(3,4), V=85, a=14, t=6 and C_s=476, so the explicit gap from unused physical labels alone is 42/5 and BOTH full ORIGINAL books are <=floor(476−42/5)=467. This uniform bound strictly improves the parent whenever t>0, even without the further kernel contribution. At W(3,2), V=15,a=6,t=0, so all slack comes from the original incidence kernel. None of these changes the s^6 exponent, external unknown ordinary C6 supersaturation constants, or the full theorem acceptance.

## 4. Independently checkable source oracles, scope and STOP

The new Python module reconstructs true ORIGINAL W(3,2) and W(3,4) incidence from genuine_source ONLY; the historical book, conflict graph, spectral and selector implementations are NOT imported. It independently checks strong regular parameters k,lambda,mu on every ordered point pair and every ordered line pair and the genuine unique-projection axiom. For both global typed maps f,g, it computes each book two different ways: actual original pencil-coordinate binomial sums and source-factor-pair-major concurrence with coordinate overlap.

For every physical coordinate y it independently forms the exact original Gram products Qv and Q²v by real source-incidence neighbor loops, constructs the exact Fraction-valued polynomial kernel projector, verifies B P0v=0, norm²=inner product, nonnegative kernel mass, and all equalities (S4)–(S6). Original CORE source flag subsets are audited separately and can only reduce their pencil conflict populations; no ORIGINAL ID can appear twice.

The new tests cover multiple distinct fixed correlated g permutations and f/g duals on genuine W32/W34, original sparse/empty core subsets, source malformed/injective controls, and symbolic all-h spectrum parameters over 28 dyadic powers without constructing nonexistent large-s enumerations. These finite oracles falsify implementation and coefficient errors; the all-h theorem is the axiom derivation in §§1–3.

The previous source spectral book bound (a prior proof input of #659/#697) is therefore independently derived and made more exact. However the complete Branch A #230 proof still requires a qualified external mathematical referee of the heavy-tail, dense-core and original six-ID combinatorial steps; the published ordinary C6 theorem constants remain existential. No merge, root issue closure, newly claimed ASET exponent or external peer acceptance.