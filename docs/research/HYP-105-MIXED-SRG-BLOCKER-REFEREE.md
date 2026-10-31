# HYP-105 #230 — AA4-MIXSRG: exact all-h collinearity-matrix correction and independent mixed full/core blocking referee

**Scientific scope:** Fixed true original \(W(3,s)\), \(s=2^h\), every complete separate globally injected original point and line pair maps \(f,g\) into physical \(K_a\) edge labels, with arbitrary correlations. This document gives a NEW exact analytic identity improving the **source** spectral part of #672's mixed full/core blocker (13)-(19), and independent exact finite proof-falsifying oracles targeting the actual original blocked triples and their two-walk completions. It does **NOT** independently establish root Branch A, does not improve the presently proved order \(s^{47/8}\), and inherits the parent [#672](https://github.com/definitely-stable/Mathlab/pull/672) all-h proof dependencies. Parent [#674](https://github.com/definitely-stable/Mathlab/pull/674) and [#675](https://github.com/definitely-stable/Mathlab/pull/675) are scientific Drafts, not externally accepted; root #230 remains OPEN_WITH_FORMAL_BLOCKER.

## 1. Why previous mixed-blocker finite tests are insufficient

The full universal proof in #672 controls internally blocked original B/B-overlap constructions using a product of two squared source/physical sums, a mixed full-source/core bound and a fourth-moment completion. Existing tests check selected W32 and W34 fixed maps; subsequent #674/#675 tests focus on deletion and support transversals. Repeating those fixtures alone would not independently verify that the first mixed squared factor is controlled by **genuine GQ original collinearity**, including both point/line duals, after arbitrarily reshuffling globally injected line pair labels.

This slice rederives that squared factor from the actual **strongly regular graph identity** of the original W(3,s), with an *explicit subtractive correction* tied to the physical embedding f.

## 2. NEW exact all-h strongly regular source identity

Let \(V=(s+1)(s^2+1)\), \(d=s+1\). Let \(C\) be the original point-collinearity adjacency matrix: \(C_{p,q}=1\) exactly when \(p\ne q\) and the two ORIGINAL W(3,s) points lie on a common ORIGINAL line. The genuine generalized quadrangle has strongly regular parameters
\[
 v=V,\quad k=s(s+1),\quad
 \lambda=s-1,\quad \mu=s+1.
\]
Hence, by counting length-two source-collinearity walks **for each ordered original point pair**, we have the exact matrix identity, for ALL dyadic \(s\):
\[
 \boxed{\quad C^2=(s^2-1)I-2C+(s+1)J.\quad}\tag{MIX-SRG}
\]
Indeed the diagonal entries are \(k=s(s+1)\); off-diagonal collinear entries are \(\lambda=s-1\); off-diagonal noncollinear entries are \(\mu=s+1\). The right-hand side reproduces all three cases exactly. This is a proof from the defining GQ incidence property, not finite-h interpolation. The dual ORIGINAL line-collinearity graph satisfies the identical equality, by point–line duality of W(3,s).

For any legal globally injected source point map f, let \(S_x=\{p:x\in f(p)\}\) for each LEFT physical coordinate x. Every original point contributes to exactly two \(S_x\); by global injection into the simple edges of \(K_a\), \(|S_x|\le a-1\). Define
\[
 E_f=\sum_x \#\{\{p,q\}\subseteq S_x:
          p\ne q,\ C_{p,q}=1\}.
\]
Here \(E_f\) counts **unordered collinear ORIGINAL point pairs sharing one physical coordinate in their f pair labels**, summed over x. Since distinct legal f pair labels intersect in at most one physical coordinate, a collinear pair contributes to at most one summand. It is a nonnegative, actual source-to-physical correlation statistic, not a random occupancy assumption.

For the vector \(\mathbf1_{S_x}\) and symmetry of C:
\[
\begin{aligned}
\|C\mathbf1_{S_x}\|_2^2
 &=\mathbf1_{S_x}^{T}C^2\mathbf1_{S_x}\\
 &=(s^2-1)|S_x|+(s+1)|S_x|^2
      -2\,\mathbf1_{S_x}^{T}C\mathbf1_{S_x}\\
 &=(s^2-1)|S_x|+(s+1)|S_x|^2-4 E_f(x).
\end{aligned}
\]
Summing over physical x yields the new exact ALL-h source-energy identity
\[
\boxed{\quad
 \sum_{x=0}^{a-1}\|C\mathbf1_{S_x}\|_2^2
 =2(s^2-1)V+(s+1)\sum_{x=0}^{a-1}|S_x|^2-4E_f.
 \quad}\tag{MIX-ENERGY}
\]
The \(-4E_f\) term is an explicit *f-dependent nonnegative subtraction* discarded by #672's more conservative spectral estimate. It is NOT assumed to be strictly positive uniformly in arbitrary f or sufficient to reduce the exponent of the error term. It also gives a simple new exact diagnostic for the quality of a particular f embedding: the source spectral energy and hence a Cauchy ingredient can be measured using original collinear same-coordinate collisions instead of constructing the large C matrix.

### 2a. NEW: a **strictly stronger UNIFORM all-h bound** for the first source blocker

The exact SRG identity is not only a pointwise f-dependent correction. Combining it with the globally injected simple physical K_a pairs gives a **strictly better f-uniform** first-factor bound than #672's formula (14), for EVERY dyadic s≥2.

Since \(|S_x|\le a-1\) and \(\sum_x|S_x|=2V\), we have
\[
 \sum_x|S_x|^2\le(a-1)\sum_x|S_x|=2V(a-1).
\]
As \(E_f\ge0\), (MIX-ENERGY) implies
\[
 A_f
 \le4(s^2-1)V+4(s+1)V(a-1)-8E_f.
\]
In particular the new uniform all-h bound is
\[
 \boxed{\quad A_f\le U_{\rm SRG}(s)
   :=4V[s^2-1+(s+1)(a-1)].\quad}\tag{MIX-UNIFORM}
\]
Compare the previous #672 first squared-factor envelope
\[
 U_{\rm OLD}(s)=4(s+1)^2[V+s^2(a-1)].
\]
The exact difference simplifies to
\[
 \boxed{\quad U_{\rm OLD}-U_{\rm SRG}
 =4(s+1)[2V-(s+1)(a-1)].\quad}\tag{MIX-GAP}
\]
For every \(s\ge2\), take the *trial physical alphabet size* \(t=s^2+2\). A direct exact polynomial check yields
\[
 \binom{s^2+2}{2}-V
 =\frac{s(s-2)(s^2+1)}2\ge0.
\]
Since a is MINIMAL with \(\binom a2\ge V\), \(a\le s^2+2\) and hence
\[
 (s+1)(a-1)\le(s+1)(s^2+1)=V.
\]
Thus
\[
\boxed{\quad
 U_{\rm OLD}(s)-U_{\rm SRG}(s)
 \ge4(s+1)V>0\qquad(\forall s=2^h\ge2).\quad}
\]
This gives a **rigorous unconditional strict improvement of the finite uniform first-blocker squared constant**, even if \(E_f=0\). The extra \(-8E_f\) further improves the per-embedding bound when ORIGINAL collinear source points share physical f-coordinates. **The order remains \(O(s^{11/2})\)** and the mixed triple and completed-blocker error exponents \(23/4\) and \(47/8\) are unchanged; no inflated asymptotic claim follows.

The pure-integer helper \`exact_allh_first_mixed_factor_envelopes(s)\` computes both bounds and their positive integer difference for every dyadic s using the exact minimal alphabet; CI tests h=1,…,18 and h=25,40,64. Those checks are falsifiers of the implementation, while the algebraic proof above covers ALL dyadic h.

## 3. New pointwise sharpened source mixed-blocker bound

Fix any ORIGINAL core flag-ID set I and its physical paired graph \(H_0\). Put
\[
R(p,y)=\#\{\ell:(p,\ell)\text{ is an ORIGINAL flag, }y\in g(\ell)\},\quad
R_0(u,y)=\#\{\ell:(u,\ell)\in I,\,y\in g(\ell)\}
\]
and \(K_{pu}=\sum_y R(p,y)R_0(u,y)\). In the actual three-path blocker of #672's Section 6, a core first edge has original point source label u with \(f(u)=\{x,k\}\) in either physical orientation. The blocking p is an ORIGINAL point whose f label contains k, while q, the projected original first endpoint, lies among the original points collinear with p whose f label contains x.

Define the exact nonnegative sums, over **ordered** physical orientations (x,k) of every ORIGINAL point label f(u):
\[
\begin{aligned}
 A_f &= \sum_{u}\sum_{(x,k)\in\overrightarrow{f(u)}}\
       \sum_{p\in S_k} \bigl[(C\mathbf1_{S_x})(p)\bigr]^2,\\
 B_{f,g,I} &= \sum_{u}\sum_{(x,k)\in\overrightarrow{f(u)}}\
       \sum_{p\in S_k} K_{pu}^2,\\
 \Phi_{f,g,I} &= \sum_{u}\sum_{(x,k)\in\overrightarrow{f(u)}}\
       \sum_{p\in S_k} (C\mathbf1_{S_x})(p) K_{pu}.
\end{aligned}
\]
Every counted \((u,x,k,p)\) has an actual physical f(u) edge and source factor p. By Cauchy and the fact that any fixed original p has **exactly two** physical f(p) endpoints k, the following is exact for arbitrary f,g,I:
\[
 \Phi^2\le A_f B_{f,g,I},
 \quad
 A_f\le 2\sum_x\|C\mathbf1_{S_x}\|_2^2.
\]
Substituting (MIX-ENERGY):
\[
\boxed{\quad
 A_f\le
  4(s^2-1)V
 +2(s+1)\sum_x|S_x|^2
 -8E_f .
 \quad}\tag{MIX-FIRST-SHARP}
\]
This is a NEW *exact source-geometry-dependent* refinement of the first-factor bound (14) in #672. It does not replace the already valid coarser f-uniform bound, but can strengthen a particular source embedding certificate without any additional probabilistic assumption. The line-dual statement is identical, with the other physical pair map g.

For completeness, the second Cauchy factor retains the exact source/physical sum identity from #672:
\[
\sum_{u}\sum_{(x,k)\in\overrightarrow{f(u)}}\sum_{p\in S_k}K_{pu}
 =\sum_{(k,y)\in[a]^2}\deg_{H_{\rm full}}(k,y)\deg_{H_0}(k,y).
\]
Under physical \(\Delta(H_0)\le T s\) and source core conflict cap K, the right-hand side is at most \(4N\,Ts\) and \(K_{pu}\le2(s+1)(K+1)\). The proof of these inequalities uses the true original full pencil R and core pencil R0 (not an unjustified all-core truncation).

Let \(\mathcal T_{x,1}\) count actual distinct ORIGINAL source-backed blocked triples \((v_0,v_1,v_3)\) whose first physical core edge is \((v_0,v_1)\), \(v_0=(x,y),v_1=(k,y_1)\), whose physical endpoint coordinates decode genuine original nonincident q,r with unique original projection \(q-\ell-p-r\), and \(k\in f(p)\). The same source choices give the sound inclusion
\[
 |\mathcal T_{x,1}|\le \Phi.
\]
Let \(A_0\) be the physical adjacency of the SAME core, \(A_0^2(v_1,v_3)\) the number of two-edge physical completions, and \(\Delta=\Delta(H_0)\). The exact weighted count of those completions is \(W=\sum_{\mathcal T_{x,1}}(A_0^2)_{v_1,v_3}\). Cauchy on triples, then counting at most \(\Delta\) first-neighbor \(v_0\) per \(v_1\), gives
\[
\boxed{\quad
 W^2\le |\mathcal T_{x,1}|\Delta\operatorname{tr}(A_0^4)
 \le \Phi\,\Delta\operatorname{tr}(A_0^4).
 \quad}\tag{MIX-COMPLETE}
\]
It covers actual internally blocked proper three-paths and intentionally counts possible improper completions too. Its dual bounds the internal right physical coordinates; path reversal covers the other inner position. This is NOT a new all-h exponent, only an independently derived *exact finite/source-certified* inequality chain and sharper source term.

## 4. Independent finite adversarial referee, including the dual

New \`research/hyp105_mixed_srg_referee.py\` computes from scratch, on the ACTUAL original W(3,2) and W(3,4):
- the full original point- (and line-) collinearity graph, its \(s(s+1)\) regular degree, every exact strongly-regular pair-intersection count \(\lambda=s-1,\mu=s+1\);
- all original star sets \(S_x\), source pair collision count \(E_f\), and the exact squared source energy \(\sum_x\|C1_{S_x}\|^2\), checked independently against (MIX-ENERGY);
- full genuine original R and sparse-core genuine R0, the *exact* \(\Phi,A_f,B_{f,g,I}\), two independent derivations of the full/core degree product, and actual core conflict cap;
- explicit original nonincident endpoint projection with its genuine q−ℓ−p−r uniqueness, independent enumeration of actual physical blocked triples (not generated from \(\Phi\)), and weighted two-walk completions; checks the full chain \(|\mathcal T|\le\Phi\), \(W^2\le|\mathcal T|\Delta\operatorname{tr}(A_0^4)\), \(\Phi^2\le A_f B\);
- the **dually transposed** ORIGINAL line side, using exactly the same original source incidence IDs with the typed point and line factors and physical coordinate sides swapped.

Independent \`research/test_hyp105_mixed_srg_referee.py\` tests five genuinely distinct legal complete W32 right line-label permutations for both original-dual orientations, W32 empty/alternating/sparse/full original core sets, actual original W34 adversarial full and sparse source cores, and a globally reallocated W34 right injection. Tests DO NOT use #672's \`finite_source_certificate\` or its published JSON, nor use Monte Carlo. Invalid original source IDs and non-injective maps are rejected.

These finite controls **may falsify** wrong analytic source index orientation, dropped full/core term, a factor of two in source-pencil/physical-edge provenance, and a missing right-side dual. They do **not** constitute automatic verification of the all-h estimate or the external supersaturation input. The proof uses exact source incidence parameters, which independently establish the analytic (MIX-SRG) and (MIX-ENERGY) identities for every h. Parent all-h universal Branch A remains unaccepted until independent qualified scientific review.
