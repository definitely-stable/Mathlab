# HYP-105 / #230 — AA4-SRGMIX: independently audited ORIGINAL collinearity, full-source collisions and mixed books

**Scientific status:** new Draft strictly stacked on frozen green [#736](https://github.com/definitely-stable/Mathlab/pull/736), parent SHA b8f8d588969797b68ed5c8fb20b630f082ed7154. Main and previous PRs are not changed; root #230 remains OPEN_WITH_FORMAL_BLOCKER; do not merge, close the issue or claim an ASET exponent. This slice supplies independent **ALL-ORDER** SRG collision and FULL-allowed/CORE mixed source double-counting proofs, and a NEW explicit all-order source-triple injection proving the four original physical internal-blocker Cauchy inequalities. The genuine-original W32/W34 oracle independently falsifies every step. This does **not** independently accept the ordinary graph supersaturation or the full root theorem.

## 1. Precise original geometry and fixed correlated maps

For every original symplectic \(W(3,s)\), \(s=2^h\), let \(V=(s+1)(s^2+1)\), \(I\) be the true point–line incidence flag IDs, and \(a=\min\{b:\binom b2\ge V\}\). Fix ANY complete globally pair-injective point labels \(f:P\to\binom{[a]}2\) and line labels \(g:L\to\binom{[a]}2\), with arbitrary correlation and without random reassignment during selection, pruning or deletion. Fix arbitrary adversarial deleted original flag IDs \(Z\), and an ORIGINAL paired physical core \(C\subseteq I\setminus Z\).

The genuine collinearity matrices \(M_P\) and \(M_L\) each have

\[
V=(s+1)(s^2+1),\quad k=s(s+1),\quad
\lambda=s-1,\quad\mu=s+1.
\]

Their ORIGINAL point/line collinearity identities, proven directly by the GQ axiom (two distinct collinear points lie on one common original line, and a point off a line has exactly one collinear point on it), are

\[
M^2=(s^2-1)I-2M+(s+1)J.
\tag{SRG-1}
\]

Thus \(M\mathbf1=k\mathbf1\), and the two nontrivial eigenvalues are \(r=s-1\) and \(t=-(s+1)\), independently for the point and line geometries.

## 2. NEW fully spelled out all-h spectral conflict lemma — no randomness in f/g

For either typed factor choose any fixed, globally pair-injective labeling \(h:P\to\binom{[a]}2\). Define \(S_x=\{p:x\in h(p)\}\), \(d_x=|S_x|\). Since every original unordered physical label pair occurs at most once, each physical symbol is present in at most \(a-1\) labels:

\[
\sum_xd_x=2V,\qquad
\sum_xd_x^2\le(a-1)\sum_xd_x=2V(a-1).
\tag{SRG-2}
\]

Let \(e_{\rm col}\) count unordered collinear original point pairs \(p,q\) with overlapping physical label pairs. Globally injected distinct pairs intersect in at most one physical symbol, so

\[
2e_{\rm col}=\sum_x1_{S_x}^{\mathsf T}M1_{S_x}.
\]

On the orthocomplement of \(\mathbf1\), the largest eigenvalue of \(M\) is \(r=s-1\). Orthogonally decompose each \(1_{S_x}=(d_x/V)\mathbf1+u_x\) to derive, for **each fixed choice of the label maps**,

\[
\begin{aligned}
2e_{\rm col}
&\le \frac{k}{V}\sum_xd_x^2+
r\sum_x(d_x-d_x^2/V)\\
&=2V(s-1)+\frac{s^2+1}{V}\sum_xd_x^2\\
&\le 2V(s-1)+2(s^2+1)(a-1).
\end{aligned}
\]

Therefore

\[
\boxed{
e_{\rm col}\le
V(s-1)+(s^2+1)(a-1)
=(s^2+1)(s^2+a-2)=C_s.
}
\tag{SRG-3}
\]

Apply this separately to the actual ORIGINAL point labels f and line labels g. Since each pair of distinct original flags sharing a point corresponds to two unique collinear original lines, and vice versa, the TOTAL ORIGINAL source conflict graph J has

\[
\boxed{e_J=e_{\rm col}(f)+e_{\rm col}(g)\le2C_s.}
\tag{SRG-4}
\]

There is no map independence, random relabeling, “typical” degree, synthetic host or induced-core spectral assumption. This is an all-order, purely deterministic SRG proof of the source conflict cap used in the heavy/low original source proofs. In particular it refutes a common invalid shortcut that bounds \(e_J\) by counting ALL overlapping K_a labels without the ORIGINAL GQ collinearity constraint; the latter would lose a significant power of s.

A stronger **instance-adaptive** bound also follows for each actually named labeling:

\[
e_{\rm col}\le V(s-1)+\frac{s^2+1}{2V}\sum_xd_x^2
\le C_s.
\tag{SRG-5}
\]

Both the actual \(e_{\rm col}\) and the occupancy-sensitive spectral ceiling are persisted separately for the two factors. In the heavy Caro–Wei selector, using the actual \(e_J\) (as in #730) may be substantially sharper than \(2C_s\), but this slice does NOT claim a new asymptotic power or a numeric universal improvement.

## 3. Independent exact original collinearity-energy identity

Let \(d_x=|S_x|\) and \(e_x\) denote actual ORIGINAL collinear pairs inside \(S_x\). The same SRG matrix identity yields

\[
\begin{aligned}
G_h&:=\sum_x\|M1_{S_x}\|_2^2\\
&=(s^2-1)\sum_xd_x-2\sum_x1_{S_x}^{\mathsf T}M1_{S_x}
 +(s+1)\sum_xd_x^2\\
&=\boxed{2V(s^2-1)-4e_{\rm col}+(s+1)\sum_xd_x^2.}
\end{aligned}
\tag{SRG-6}
\]

Crucially \(G_f\) and \(G_g\) must be recomputed independently. The new program reconstructs both full original SRGs, evaluates every \(\sum_x\|M1_{S_x}\|^2\) directly, and checks the exact identity and (SRG-3) on genuine W32/W34, including independently permuted globally injected f,g maps. Old source-energy code is imported ONLY by a separate test to detect disagreement.

## 4. NEW full-source-to-CORE mixed-book double counting

Write \(A=I\setminus Z\). For actual ORIGINAL source point p and physical second-coordinate symbol y define

\[
R_A(p,y)=\#\{(p,\ell)\in A:y\in g(\ell)\},\qquad
R_C(p,y)=\#\{(p,\ell)\in C:y\in g(\ell)\}.
\]

Let \(K_{AC}(p,u)=\sum_yR_A(p,y)R_C(u,y)\), and for the genuinely original point-collinearity \(c_x(p)=|S_x\cap N_{M_P}(p)|\). The source blocker book is

\[
B_x=\sum_{\substack{u\in P:C\cap I(u)\ne\varnothing\\
                      (x,k)\in\{\text{both orientations of }f(u)\}}}
\sum_{p:k\in f(p)}c_x(p)\,K_{AC}(p,u).
\tag{MIX-1}
\]

Set \(F_{1,x}=\sum c_x(p)^2\), \(F_{2,x}=\sum K_{AC}(p,u)^2\) over exactly the same index triples (u,x,k,p). Cauchy gives \(B_x^2\le F_{1,x}F_{2,x}\).

**First independent cap.** For each fixed (x,p), the physical pair f(p) has only TWO symbols k, and each pair {x,k} belongs to at most one original u by global injection. Therefore

\[
\boxed{F_{1,x}\le2\sum_{x,p}c_x(p)^2=2G_f.}
\tag{MIX-2}
\]

**Second independent cap.** The ORIGINAL full-source conflict maximum of the retained CORE is at most K. All original source flags on the same point u whose physical g line-pairs contain y form a clique of the source conflict graph. Hence \(R_C(u,y)\le K+1\), while \(R_A(p,y)\) summed over y is at most \(2(s+1)\) for every original p. So

\[
K_{AC}(p,u)\le2(s+1)(K+1).
\tag{MIX-3}
\]

For any physical vertex (k,y), let \(D_A(k,y)\), \(D_C(k,y)\) be its **actual** degrees in the full allowed A and paired core C two-diagonal physical graphs. Every original flag (p,ell) with k in f(p) and y in g(ell) contributes exactly one incident physical edge at (k,y); thus

\[
D_A(k,y)=\sum_{p:k\in f(p)}R_A(p,y),\quad
D_C(k,y)=\sum_{u:k\in f(u)}R_C(u,y).
\]

Exactly expanding the source summation proves the true original contraction

\[
\boxed{
\Theta_{AC}:=\sum_{u,(x,k)\in f(u)}\sum_{p:k\in f(p)}
K_{AC}(p,u)
=\sum_{k,y}D_A(k,y)D_C(k,y)
\le\Delta\sum_{k,y}D_A(k,y)
=4|A|\Delta,
}
\tag{MIX-4}
\]

where \(\Delta=\max_vD_C(v)\). Note: the projected original anchor source ID may lie in **A outside C**; replacing A by C would be an incorrect strengthening of the original path model.

Combining (MIX-3),(MIX-4) yields

\[
\boxed{
F_{2,x}\le2(s+1)(K+1)\Theta_{AC}
\le8(s+1)(K+1)|A|\Delta,
}
\tag{MIX-5}
\]

and hence the genuine original source upper, separately for the POINT and the true LINE dual:

\[
\boxed{
B_x^2\le16(s+1)(K+1)|A|\Delta G_f,\quad
B_y^2\le16(s+1)(K+1)|A|\Delta G_g.
}
\tag{MIX-6}
\]

All this is an independently written ALL-ORDER double-counting argument, not a numerical extrapolation or another call to the old program.

## 5. NEW independent ALL-ORDER four-blocker triple-to-source-book injection proof

The previously outstanding path-to-source-book Cauchy step can be proved by an explicit **injective source witness map**, without assuming statistical independence, equal point/line books, anchor flags lying in C, or random physical labels. This result is stronger than merely passing finite falsification tests.

### 5.1. FIRST interior x-coordinate blocker

Write \(H_C\) for the true paired CORE physical graph, with adjacency \(A_C\), degree cap \(\Delta\), and \(t_4=\operatorname{tr}(A_C^4)=\sum_{v_1,v_3}(A_C^2(v_1,v_3))^2\). Let \(T_{x,1}\) be the set of **ordered physical triples** \((v_0,v_1,v_3)\) with

1. \(v_0=(x_0,y_0)\) and \(v_1=(x_1,y_1)\) adjacent in the actual ORIGINAL paired core \(H_C\);
2. \(f^{-1}\{x_0,x_3\}=q\) and \(g^{-1}\{y_0,y_3\}=r\) both exist under the fixed complete *globally injected* ORIGINAL labels, with q **not** incident to r;
3. in the genuine FULL symplectic GQ the unique original projection of (q,r) is \(q-\ell-p-r\) with its three original source flags avoiding Z;
4. \(x_1\in f(p)\).

We deliberately do **not** require the interior middle two-walk to be coordinate proper; such overcounting only increases our upper bound. We also do **not** require the original projection flags to lie in C. The path's FIRST physical edge source ID \((u,\ell_u)\in C\) is unique, with \(f(u)=\{x_0,x_1\}\), \(g(\ell_u)=\{y_0,y_1\}\).

Now take any triple \((v_0,v_1,v_3)\in T_{x,1}\). Its original source data furnish a unique term in the combinatorial expansion of \(B_x\):

- retained first-edge ORIGINAL point u, pair orientation \((x,k)=(x_0,x_1)\);
- projected original p, where \(k=x_1\in f(p)\);
- unique projected original q, collinear with p, with \(x_0\in f(q)\), therefore counted by \(c_{x_0}(p)\);
- full allowed ORIGINAL incidence \((p,r)\in A=I\setminus Z\) and retained ORIGINAL incidence \((u,\ell_u)\in C\), sharing the actual physical symbol \(y_0\in g(r)\cap g(\ell_u)\), therefore counted by the \(y_0\) summand of \(K_{AC}(p,u)\).

The assignment from the ordered physical triple to its source-book witness is **injective**, not merely existence-preserving. Indeed, from the witness recover x0,x1 and u,p,q,r,ell_u,y0. The other endpoint \(x_3\) is uniquely forced as the remaining symbol of globally injected f(q), \(y_3\) as the remaining symbol of g(r), and \(y_1\) as the remaining symbol of g(ell_u). Thus the ORIGINAL physical triple \((v_0,v_1,v_3)\) is uniquely reconstructed from its source witness. This proves the all-order double-counting bound

\[
\boxed{|T_{x,1}|\le B_x.}\tag{BLOCK-1}
\]

Every true endpoint-good, Z-avoiding, coordinate-proper physical three-path with its first inner x-coordinate blocked by \(f(p)\) has a triple in \(T_{x,1}\). For a fixed triple the number of possible middle two-step completions \(v_1\to v_2\to v_3\) in the physical CORE graph is exactly \((A_C^2)(v_1,v_3)\). Therefore

\[
I_{x,1}\le\sum_{(v_0,v_1,v_3)\in T_{x,1}}
(A_C^2)(v_1,v_3).
\]

Use Cauchy–Schwarz over physical triples. For fixed ordered physical pair (v1,v3), at most deg(v1) <=Delta different first neighbors v0 can occur. This yields

\[
\begin{aligned}
I_{x,1}^2
&\le |T_{x,1}|
\sum_{T_{x,1}}(A_C^2)(v_1,v_3)^2\\
&\le B_x\,\Delta\sum_{v_1,v_3}(A_C^2)(v_1,v_3)^2
=\boxed{B_x\,\Delta\,t_4}.
\end{aligned}
\tag{BLOCK-2}
\]

This is a complete, explicit **ALL-ORDER** source-first proof of the difficult path-to-source mixed-book step of the original low-tail method. It depends only on genuine FULL GQ projection, unique original physical edge ownership and the original source FULL-allowed/CORE books already independently established in Sections 2–4.

### 5.2. OTHER THREE blocker positions

**Reversal** \(v_0,v_1,v_2,v_3\mapsto v_3,v_2,v_1,v_0\) is a bijection among the same admissible FULL-original-GQ endpoint-good directed physical proper paths: the original decoded q,r and their three named source anchors do not change, and the two endpoints have unchanged unordered factor labels. It exchanges the first and second inner x-blockers. Thus \(I_{x,2}=I_{x,1}\) and the same \(B_x\Delta t_4\) upper applies.

**Genuine ORIGINAL point-line duality** swaps all original source points and lines, physical x/y factors and their globally injected f/g pair labels, without remapping original incidence IDs or allowing a source anchor in Z. Reapply the same triple injection independently in the line dual to derive \(I_{y,1}^2\le B_y\Delta t_4\); path reversal gives \(I_{y,2}^2\le B_y\Delta t_4\). In particular there is no unjustified assumption that \(B_x=B_y\) under correlation.

Therefore, for every genuine \(W(3,s)\), any complete separately pair-injective correlated fixed maps f/g, any arbitrary deleted ORIGINAL source set Z and actual paired core \(C\subseteq I\setminus Z\):

\[
\boxed{
I_{x,j}^2\le B_x\Delta t_4,\qquad
I_{y,j}^2\le B_y\Delta t_4,\qquad j=1,2.
}
\tag{BLOCK-3}
\]

The sum of their four **possibly overlapping** blocker classes is consequently bounded by \(2\sqrt{B_x\Delta t_4}+2\sqrt{B_y\Delta t_4}\). This is the exact all-order four-position inequality used in the inherited LOWCERT proof; it does NOT assume the classes are disjoint.

### 5.3. Independent finite red-team of the injective source map

A second independent finite algorithm constructs all candidate triples in \(T_{x,1}\) directly from genuine physical first-core edges and independently decoded ORIGINAL q,r projection, even if no physical middle two-walk exists. It checks:

\[
|T_{x,1}|\le B_x,\qquad
\Big(\sum_{T_{x,1}}A_C^2(v_1,v_3)\Big)^2
\le |T_{x,1}|\sum_{T_{x,1}}(A_C^2(v_1,v_3))^2
\le B_x\Delta t_4,
\]

then separately confirms the actual original valid first-inner blocked proper physical path count is at most this source-triple middle-completion sum. Reapply with fully swapped original point/line factors for the LINE dual. All four actual blockers and the source triple inventory are recorded independently in the durable JSON. These genuine W32/W34 finite probes falsify accidental implementation errors but are not substituted for the injectivity proof above.

**Scientific boundary:** the previously pending *local* four-blocker source Cauchy injection is now an explicitly derived all-order lemma, but the **entire root #230 theorem** still requires review of other inherited G3 selector/chunk and G6 moment/supersaturation dependencies, correct quantifier composition and full acceptance. No automatic root/ASET promotion follows from this local closure.

## 6. Genuine-original adversarial finite trials and proof status

Seven real source cases use actual W(3,2) (45 flags) or W(3,4) (425 flags), lex/reverse-line base schemes and independent cyclic permutations of the COMPLETE globally injected point and line pair maps. All use explicit nonempty adversarial original source-ID deletion sets Z; K,T are diagnostic small values to exercise nonempty heavy/full-Q and retained CORE, not the asymptotically enormous universal theorem T. They independently reconstruct:

- BOTH original point and line SRGs and their true lambda/mu common-neighbor counts.
- The actual full ORIGINAL conflict graph and equality to the two separately computed SRG collision books; actual edges never exceed \(2C_s\).
- The entire full physical graph before deleting source IDs, high-Q touched flag set, high-source-conflict flag removal, real paired surviving core and its true \(\Delta\le Ts\).
- Point and line independently computed \(F_1,F_2,B,\Theta\) with FULL allowed A and smaller core C, including exact \(\Theta=\sum D_AD_C\), source max K and actual physical \(\Delta\).
- Every actual proper physical three-path, FULL original GQ projection and all FOUR blocker positions, with exact separate original-source Cauchy inequalities.
- Invalid duplicate source IDs, illegal fractional shifts, inappropriate dyadic s, and falsely claiming small K for an uncapped core are fail-closed.

Original source generator is shared as a trusted test fixture, but **all spectra, collisions, books, physical and projected path combinatorics are newly independently implemented**. Only TEST code uses the historical SRG G-energy evaluator for cross-checking.

All-order original source graph spectral/conflict cap, FULL/CORE F1/F2/Theta inequalities and the explicit source-first four-blocker Cauchy injection are now independently derived. **Remaining scientific blockers** are the independent audit of the full heavy-source selector and no-clone chunk, sixth-moment selector and its interface with the root lowtail, plus acceptance of the actual external SS6 theorem application with existential constants. Root Branch A stays OPEN_WITH_FORMAL_BLOCKER, no merge, no new ASET exponent.

Dedicated GitHub-hosted Ubuntu 24.04 Python 3.12 CI runs ten independent tests plus a strict complete ORIGINAL source JSON artifact. INDEX and full Research must be green at the **final exact PR HEAD** before engineering acceptance.
