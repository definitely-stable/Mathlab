# HYP-105 / issue #230 — AA4-CODEGSEL: exact ORIGINAL priority-codegree and strict source-aware B75 envelope

**Science status:** OPEN_WITH_FORMAL_BLOCKER. This is the next strict Draft child of [AA4-JOINT3 PR #764](https://github.com/definitely-stable/Mathlab/pull/764), exactly frozen at source HEAD **5fc43bead110d2f25de7f13c08d40ed0257ff581**. We do NOT edit the parent, main, or any ancestor, merge any PR, close the root issue, or claim a new ASET exponent. Results are all-order identities and pointwise inequalities, plus independently verified finite true-original certificates once exact-head GitHub CI succeeds.

## 1. Research decision after AA4-JOINT3

PR #764 correctly replaced the ≈96%-ghost two-endpoint independent-coordinate GQ incidence projection by a real physical first/middle/last three-ORIGINAL-owner port contraction, with a single shared source-priority selector. Its proven pointwise owner minimum selector bound uses only the three individual conflict degrees:

\[
\frac{1}{64\prod_{t=1}^3(1+d_t)}
\le w_\gamma=\frac{\Pr(A_1\cap A_2\cap A_3)}{64}
\le\frac{1}{64(1+\max d_t)}.
\]

The missing source information is the **true codegree** between these three ORIGINAL owners in the original physical-label and incidence-dependent source conflict graph \(J_C\). Distinct source owners may share actual competing original incidence IDs. Treating their minimum events as independent is wrong: a *single shared outsider* produces \(\Pr(A_1\cap A_2\cap A_3)=1/4\), whereas independent singleton multiplication gives \(1/8\). One-sided bounds can be upgraded without treating any physical f/g labels as random.

The high-leverage next step is to derive the **exact two-owner joint priority law** for ANY fixed original J, then use positive association and containment to produce strictly stronger but provably valid THREE-owner lower and upper intervals. This directly improves the quantitative source charge needed to test a global \(B/M<3/4\) sufficient certificate. It is not a universal all-label theorem by itself.

## 2. Precise genuine original model and quantifiers

For every \(h\ge1\), \(s=2^h\), take genuine symplectic \(W(3,s)\) with its **named ORIGINAL** incidence IDs \(I=\{(p,\ell):p\sim\ell\}\). Take arbitrary complete, separately globally injective physical pair label maps

\[
f:P\hookrightarrow\binom{[a]}2,\quad
g:L\hookrightarrow\binom{[a]}2,
\]

with arbitrary fixed mutual correlation. Take arbitrary named source deletion \(Z\subseteq I\) and paired retained source CORE \(C\subseteq I\setminus Z\). Assume the valid original conflict graph \(J_C\) and actual paired opposite physical diagonals as in #764. An actual coordinate-proper P3 uses three **distinct, pairwise J-independent** source owner IDs \(i,j,k\), with real physically connected first, middle, last ports. Each true path's two typed physical cut constraints contribute exactly \(4^{-3}=1/64\), separate from the uniform **one global permutation** of genuine source ID priority ranks.

For a vertex/owner \(i\in C\), put \(d_i=|N_J(i)|\), and for independent \(i\neq j\) put \(c_{ij}=|N_J(i)\cap N_J(j)|\). All neighbors and common neighbors are actual named ORIGINAL flags retained in this source conflict graph, not the classical GQ point-collinearity graph and not a synthetic copy. Their values can depend arbitrarily on the fixed f and g.

## 3. NEW exact all-order two-owner codegree probability

Assign every retained original incidence owner ID an independent continuous priority \(U_x\sim\mathrm{Unif}(0,1)\), which induces one common uniform permutation. Let \(A_i=\{U_i<U_v\ \forall v\in N_J(i)\}\). Since i,j are J-independent, conditioning on their ranks \(U_i=t\), \(U_j=u\) leaves exactly \(d_i-c\) private neighbors of i, \(d_j-c\) private neighbors of j, and \(c=c_{ij}\) common neighbors. Thus

\[
\Pr(A_i\cap A_j)=\int_0^1\!\!\int_0^1
(1-t)^{d_i-c}(1-u)^{d_j-c}
(1-\max\{t,u\})^c\,dt\,du.
\tag{C-1}
\]

Split the domain into \(t\ge u\) and \(u\ge t\), integrate both elementary monomials exactly. Put \(q=d_i+d_j-c+2\). Then the exact RATIONAL identity valid for every finite genuine J is

\[
\boxed{
P_{ij}:=\Pr(A_i\cap A_j)=
\frac{\frac1{d_i+1}-\frac1q}{d_j-c+1}
+
\frac{\frac1{d_j+1}-\frac1q}{d_i-c+1}.
}
\tag{C-2}
\]

Checks: \(P_{ij}\) is symmetric; if \(c=0\), it reduces **exactly** to \(1/[(1+d_i)(1+d_j)]\), while \(c=1,d_i=d_j=1\) yields \(1/3\), not \(1/4\). Universal consistency:

\[
\frac1{(1+d_i)(1+d_j)}
\le P_{ij}\le\min\left\{\frac1{1+d_i},\frac1{1+d_j}\right\}.
\tag{C-3}
\]

The right side follows from event containment; the left from the same independent-priority positive association in #754, not from product independence. The source program uses only exact Python Fraction integers and sets of genuine source J IDs, no Monte Carlo or assumed original-label independence.

**Prior art/nomenclature:** order statistics, conditioning, local-minimum events and Harris/FKG product association are classical. We do not claim these standalone facts as a new probability theorem; the new scoped deliverable is the exact codegree-controlled selector transfer and independently falsified quantitative calculation for the TRUE correlated-original #230 source.

## 4. NEW pointwise all-order three-owner rank envelope

For a proper path with pairwise J-independent owner triple \(S=\{i,j,k\}\), \(\Pr(A_i)=1/(1+d_i)\). For any pair \(i,j\in S\), trivially

\[
\Pr(A_i\cap A_j\cap A_k)\le P_{ij}.
\tag{C-4}
\]

For the lower, transform independent priorities simultaneously for **ALL owner IDs in S** via \(Y_i=1-U_i\) while leaving outsider ranks \(Y_v=U_v\). Because S is J-independent, each event \(A_t\) is coordinatewise increasing in the same independent transformed vector Y: every source minimum inequality is \(Y_t+Y_v>1\). Thus both \(A_i\cap A_j\) and \(A_k\) are increasing events. Elementary positive association yields

\[
\Pr(A_i\cap A_j\cap A_k)\ge P_{ij}\Pr(A_k)
=\frac{P_{ij}}{1+d_k}.
\tag{C-5}
\]

Maximize over the three pair choices in C-5 and minimize over them in C-4. **All-order true ORIGINAL source theorem:**

\[
\boxed{
\frac1{64}\max_{\{i,j\}\subset S}\frac{P_{ij}}{1+d_k}
\ \le w_\gamma \le\
\frac1{64}\min_{\{i,j\}\subset S}P_{ij}.
}
\tag{C-6}
\]

This **dominates both of #764's pointwise bounds**. It is valid for every legal fixed correlated f,g, any adversarial named Z and retained C and every actual coordinate-proper physical P3. No step assumes pair-event independence or independent physical labels. If all THREE source J neighborhoods are pairwise disjoint, the three events are actually independent and the two sides of C-6 agree with the exact path weight \(1/[64\prod(1+d_t)]\). The implementation checks this exact equality against the established exact 6-order three-owner Fraction rank oracle.

## 5. NEW exact-source weighted risk charging consequence

Use **only actual physical source-port paths** constructed by AA4-JOINT3; label their exact weights \(w_\gamma\), C-6 lower weights \(\ell_\gamma^{(2)}\), and upper \(u_\gamma^{(2)}\), with the superscript indicating pair-codegree information. In each ordered physical endpoint bin \(uv\), set \(L_{uv}^{(2)}=\sum_\gamma\ell_\gamma^{(2)}\) and \(U_{uv}^{(2)}=\sum_\gamma u_\gamma^{(2)}\). Then, for the exact #764 source selector physical endpoint energy \(M\),

\[
\sum_{uv}(L_{uv}^{(2)})^2\le M
\le M_U^{(2)}:=\sum_{uv}(U_{uv}^{(2)})^2
\le M_U^{(1)}
\le\frac{\sum_{uv}n_{uv}^2}{4096}.
\tag{C-7}
\]

From the earlier **exact** original middle-owner second-moment identity (#759/#760), the compatible mass \(G\) equals a sum of nonnegative products over the true compatible ordered physical path pairs. Therefore replacing **each** actual weight \(w_\gamma\) by \(\ell_\gamma^{(2)}\) yields a genuine lower \(G_L^{(2)}\). It dominates the old singleton-Harris compatible mass \(G_L^{(1)}\), and all these source probabilities are rational, not expected over labels:

\[
0<G_L^{(1)}\le G_L^{(2)}\le G,\quad
M_U^{(2)}\le M_U^{(1)}.
\tag{C-8}
\]

For \(B=M-G\), the globally valid **all-h** sufficient certificate is

\[
\boxed{
\frac{B}{M}\le
1-\frac{G_L^{(2)}}{M_U^{(2)}}
\le 1-\frac{G_L^{(1)}}{M_U^{(1)}}.
}
\tag{C-9}
\]

If a specified original fixed source satisfies \(4G_L^{(2)}>M_U^{(2)}\), its **global** \(B/M<3/4\) follows; if not, there is no counterexample and no universal conclusion. Exact finite data and any newly certified SOURCE cases are recorded by the specialist workflow, not projected to infinite h.

**Important quantifier firewall:** Even universal global \(B/M<3/4\) for this original physical P3 selector is only one load-bearing LOW proof step. Root #230 requests an all-label seven-family six-motif \(\Omega(s^6)\) obstruction or infinite correlated counterexample, plus full GF5/ASET separation. This slice claims none of those ultimate conclusions.

## 6. Independent falsification and acceptance

- The independent **literal priority permutation oracle** counts ALL permutations for 2-owner and 3-owner events over synthetic shared-neighbor patterns. It does not import the derived C-2 formula for counting.
- Separate exact rank integration from existing #764 is compared against the completely independent enumeration in several adversarial neighbor-sharing examples, including all shared, pair shared, asymmetric and disjoint neighborhoods.
- True ORIGINAL symplectic W(3,2) retained J owner triples are checked pointwise against the EXACT established source rank and both inherited #764 singleton-degree bounds.
- Eight complete genuine original W(3,2) / W(3,4) fixed source scenarios must reproduce exactly \((1346,1154,838,83892,82846,79404,9966,66418)\) real coordinate-proper directed P3 counts and the source exact Fraction B/M. Each strict improvement must be monotone: \(G_L^{(2)}\ge G_L^{(1)}\), \(M_U^{(2)}\le M_U^{(1)}\), and the C-9 risk upper must not worsen. The independent finite fully source-based machine-readable JSON reports strict selector improvement counts and all-old/new risk fractions.

Host: GitHub-hosted ubuntu-24.04 Python 3.12 only, code+docs+unit tests and exact eight-case certificate. REQUIRE **specialist + INDEX + FULL Research SUCCESS at identical final PR HEAD**; until all finish, acceptance is pending. No local PC or fabricated CI result.

## 7. Remaining real proof gate

Even C-6 cannot force every legal adversarial f,g into the global safe regime; source-specific pair-codegrees alone do not control where the **endpoint physical middle-owner overlap weight** concentrates. The genuine unresolved mathematical target is a uniform same-endpoint ORIGINAL-GQ charge controlling \(R=\sum_{uv,i}w_{uv,i}N_{uv,i}\), retaining the positive Dirichlet correction of #761, together with the **real** physical ports and **correlated** source selector. Alternatively exhibit a legal infinite dyadic low-six-motif labeling. Do not transfer the classical GQ incidence spectral gap to the arbitrary physical-label-overlap graph.
