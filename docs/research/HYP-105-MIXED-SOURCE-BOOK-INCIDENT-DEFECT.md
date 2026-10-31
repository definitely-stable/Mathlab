# HYP-105 / #230 — AA4-MIXBOOK: EXACT all-h incident-source defect for the mixed full/core blocker

**Status:** A NEW all-\(h\) deterministic combinatorial equality strengthening the original-source mixed-blocker *inequality* in scientific Draft [#672](https://github.com/definitely-stable/Mathlab/pull/672). It is independently obtained from the defining true \(W(3,s)\) generalized-quadrangle axiom, complete globally injected original point/line maps, and arbitrary ORIGINAL incidence flag cores. It does NOT independently prove the entire universal sextic root Branch A, its path density bound, or a new ASET exponent; #230 remains OPEN_WITH_FORMAL_BLOCKER pending qualified external mathematical referee. Previous local original-sixset inverse [#677](https://github.com/definitely-stable/Mathlab/pull/677) addresses a separate (exactly-two-preimages-onto-image) issue.

## 1. Precise all-h problem with fully correlated physical pair maps

Let \(s=2^h\ge2\), \(V=(s+1)(s^2+1)\), and take the genuine ORIGINAL \(W(3,s)\) point set \(P\), line set \(L\), and **actual original incidence flag IDs** \(F=\{(u,\lambda):u\in\lambda\}\). Fix ANY complete, separately globally injective, potentially arbitrarily correlated typed physical pair assignments
\[
 f:P\hookrightarrow E(K_a), \qquad
 g:L\hookrightarrow E(K_a),
 \qquad a=\min\{t:\tbinom t2\ge V\}.
\]
Fix ANY actual ORIGINAL flag core \(I\subseteq F\). Core flags contribute BOTH paired physical diagonals. All source GQ data and projections are from the **full** ORIGINAL \(F\); projected anchor flags need not belong to I.

For each physical left coordinate \(x\), put \(S_x=\{p:x\in f(p)\}\). Write \(C(p)\) for the true ORIGINAL source point-collinearity neighbor set (not an abstract synthetic graph). A core flag \(i=(u,\lambda)\in I\), oriented physical f pair \((x,k)\in\overrightarrow{f(u)}\), and oriented physical g pair \((y,t)\in\overrightarrow{g(\lambda)}\) specifies one actual directed core physical first edge
\[
 (v_0,v_1)=((x,y),(k,t)).
\]
Every such edge has a UNIQUE original flag ID by the separate global injections; there are exactly two diagonal edges per retained flag, oriented in two directions.

Define an **ORIGINAL source book witness** to be the following ORIGINAL objects:
\[
 (i,u,\lambda;\ x,k;\ y,t;\ p,q,r)
\]
with
\[
 \begin{cases}
 i=(u,\lambda)\in I,\ (x,k)\in\overrightarrow{f(u)},\
 (y,t)\in\overrightarrow{g(\lambda)},\\
 p\in S_k,\quad q\in S_x\cap C(p),\\
 (p,r)\in F,\quad y\in g(r).
 \end{cases}\tag{MIXBOOK-SOURCE}
\]
The variables \(q,p\) are true source **point** factors and \(r,\lambda\) true source **line** factors. The source witness includes both an arbitrary ORIGINAL flag through p and a core ORIGINAL flag at u. No independent randomness or physical edge reassignment is used.

Let \(\mathcal W\) be the finite set of all these SOURCE book records, and let \(\Psi_{\rm inc}\) be the number of records where **q is ORIGINAL incident with r**, i.e. \((q,r)\in F\).

Let \(\mathcal T\) be the set of all actual PHYSICAL ordered triples of vertices
\((v_0,v_1,v_3)\), whose first directed edge is in the core physical graph, whose physical endpoint first pair \(\{v_0^L,v_3^L\}\) decodes a genuine ORIGINAL point q via f, whose physical endpoint right pair \(\{v_0^R,v_3^R\}\) decodes a genuine ORIGINAL line r via g, with q NOT incident r, and whose UNIQUE original projection \(q-\ell-p-r\) satisfies \(v_1^L\in f(p)\). This is exactly the first-inner-left-coordinate blocked-triple population bounded by equation (13) of #672; it does **not** impose the extra condition that a middle vertex v2 exist, nor physical properness of a later four-vertex path. Those conditions only **reduce** the number of paths blocked and are handled subsequently through the \(A_0^2\) fourth-moment step.

## 2. New exact theorem

For EVERY dyadic \(s\), all complete correlated f,g and every ORIGINAL core I,
\[
\boxed{\qquad
 \Phi(f,g,I)=|\mathcal T(f,g,I)|+
             \Psi_{\rm inc}(f,g,I).
 \qquad}\tag{MIXBOOK-EXACT}
\]
Here \(\Phi\) is the old full-source/core mixed bilinear tensor on the right of #672 equation (13):
\[
\begin{aligned}
 R(p,y)&=\#\{r:(p,r)\in F,\ y\in g(r)\},\\
 R_0(u,y)&=\#\{\lambda:(u,\lambda)\in I,\ y\in g(\lambda)\},\\
 K_{pu}&=\sum_y R(p,y)R_0(u,y),\\
 \Phi&=
 \sum_u\sum_{(x,k)\in\overrightarrow{f(u)}}
 \sum_{p\in S_k}\bigl|C(p)\cap S_x\bigr|\,K_{pu}.
\end{aligned}\tag{MIXBOOK-PHI}
\]
Thus the source mixed blocker estimate \(B=|\mathcal T|\le\Phi\) from #672 is a consequence of an exact TRUE-ORIGINAL-source equality. The new nonnegative, embedding-sensitive **incidence defect** \(\Psi_{\rm inc}\) is an explicit additional subtraction and is independent of whether the core was obtained by the #672 selector.

### Proof of the book/tensor identity \(|\mathcal W|=\Phi\)

Fix \(u\), oriented \((x,k)\), and \(p\in S_k\). There are exactly \(|C(p)\cap S_x|\) possible ORIGINAL points q. For each physical y, the choices of a FULL original line \(r\) through p with \(y\in g(r)\) number \(R(p,y)\). Independently, choices of a **CORE original line** \(\lambda\) through u with \(y\in g(\lambda)\) number \(R_0(u,y)\). The second physical orientation \((y,t)\) of that \(\lambda\) is uniquely determined by y. Summing over y gives precisely \(K_{pu}\). No candidate is double-counted as a SOURCE book record: each variable is retained in the witness tuple. Summing all choices proves \(|\mathcal W|=\Phi\) **exactly for all h**.

### Proof that the surviving books are in bijection with blocked triples

Partition \(\mathcal W\) by whether q is incident with r.

If \(q\in r\), the endpoint pair (q,r) is NOT eligible for the original **nonincident** GQ projection. These are exactly the \(\Psi_{\rm inc}\) incident witnesses, and they must be discarded.

Otherwise \(q\notin r\), but the source book already explicitly chose a point \(p\in r\) collinear with q. By the defining generalized-quadrangle uniqueness axiom, for every nonincident original point q and line r there is **exactly ONE** point on r collinear with q. It follows that the already chosen p is precisely the **unique** point in the projection \(q-\ell-p-r\). There is NO possible independent “wrong nonincident source anchor” defect! Thus every nonincident book is eligible.

Because \(q\in S_x\) and globally injected f assigns each source point a TWO-coordinate physical edge, \(f(q)=\{x,z\}\) fixes the other physical left endpoint z uniquely. Likewise \(g(r)=\{y,w\}\) fixes w. Define
\[
 (v_0,v_1,v_3)=((x,y),(k,t),(z,w)).
\]
The first edge is by construction a true CORE physical diagonal of the original flag \(i=(u,\lambda)\), and the two endpoint pair labels decode the original q,r, with \(v_1^L=k\in f(p)\). It is therefore one eligible blocked triple in \(\mathcal T\).

This map is **injective**: the triple's first directed physical edge determines the unique core original owner flag i, as a consequence of the separately globally injected f and g and the original source flags' uniqueness; it also determines the two physical orientations \((x,k),(y,t)\). The triple's endpoint first pair \(\{x,z\}\) uniquely determines q via f and the endpoint second pair \(\{y,w\}\) uniquely determines r via g. Finally the GQ axiom determines p. Hence the entire source book record is uniquely recoverable from the triple.

The map is **surjective**: given any triple in \(\mathcal T\), read its original first-core-edge owner \(i=(u,\lambda)\), oriented pair coordinates \(x,k,y,t\), original endpoint q,r and original projection p. Then the incidence \((p,r)\in F\), collinearity \(q\in C(p)\), and both physical star conditions hold by the triple's very definition. These objects therefore form a qualifying nonincident book record mapping to that triple.

This establishes a bijection \(\mathcal W\setminus\mathcal W_{\rm inc}\longleftrightarrow\mathcal T\) and proves MIXBOOK-EXACT.

**Special case:** if \(I=\varnothing\), all three quantities vanish exactly. **Point–line dual:** W(3,s) has the same GQ axiom on its dual; exchange ORIGINAL points and lines, and exchange left/right physical alphabets, preserving the same original flag IDs. The identity holds unchanged for all internal coordinate blocker orientations.

## 3. New *exact* source-incidence correction

The defect is not just an abstract missing-projection set. Because q and p are collinear and \(r\) is a line through p, the condition “q incident r” says that q is one of the \(s\) other ORIGINAL source points on the very ORIGINAL line r. Consequently \(\Psi_{\rm inc}\) admits the direct source-pencils expression
\[
\boxed{
\begin{aligned}
\Psi_{\rm inc}
=\sum_{i=(u,\lambda)\in I}
\sum_{(x,k)\in\overrightarrow{f(u)}}
\sum_{(y,t)\in\overrightarrow{g(\lambda)}}
\sum_{p\in S_k}
\sum_{\substack{r\ni p\\ y\in g(r)}}
  \bigl|(r\setminus\{p\})\cap S_x\bigr|.
\end{aligned}}\tag{MIXBOOK-INC}
\]
This count is **nonnegative and can be strictly positive** for genuine source embeddings. The new exact bound
\[
 B_{\rm blocked}
 =\Phi-\Psi_{\rm inc}
 \le\Phi\le\sqrt{A_f B_{f,g,I}}
\]
retains explicit f,g,I-dependent information that the old argument discarded. The first squared factor has already been independently strengthened by exact SRG geometry in [#676](https://github.com/definitely-stable/Mathlab/pull/676):
\[
 A_f\le4V[s^2-1+(s+1)(a-1)]-8E_f.
\]
Combining the independent two correction mechanisms is legal: they concern different steps, source star energy and source book incidence rejection. Neither has a **uniform positive lower bound** asserted for its correction, so no stronger asymptotic exponent than \(23/4\) for mixed triples or \(47/8\) for completed blocked paths is claimed.

## 4. Independent original-source and physical-source implementation

The four new files in the Draft:
- \`research/hyp105_mixed_source_book_defect.py\`: **THREE mathematically independent finite evaluators**, all on the ACTUAL ORIGINAL W(3,2) or W(3,4) symplectic incidences:
  (a) \`exact_source_book_partition\` enumerates ORIGINAL books by core flag and the original point/line incidence pencils, categorizing incident q∈r versus nonincident true GQ projection, WITHOUT CONSTRUCTING physical paths;
  (b) \`independent_physical_first_blocked_triples\` independently constructs the retained SOURCE-BACKED physical graph, scans its actual directed first edges and decodes original endpoint q,r and the original GQ projection, WITHOUT USING source books, mixed Phi or Psi;
  (c) \`independent_original_book_phi_tensor\` independently computes R,R0,Kpu and Phi through the full/core source pencil tensor, WITHOUT book or physical graph enumeration. Each scans actual original six-ID geometry, not a synthetic GQ or iid physical graph.
- \`research/test_hyp105_mixed_source_book_defect.py\`: compares the THREE exact result objects AND the independent earlier #676 Cauchy-referee for five globally injected, differently correlated W32 right pair maps (full, empty, alternating, sparse actual ORIGINAL cores, BOTH original dual orientations) and real W34 adversarial full/sparse/reassigned-g cores (both dual orientations). Checks exact book-triple bijection **with matching source owner tuple (i,p,q,r)**, not merely equal scalar totals; exact decomposition of positive incident and valid books, malformed core and map rejection.
- \`.github/workflows/hyp105-mixed-source-book-defect.yml\`: one GitHub-hosted Python 3.12 specialized fail-closed job; exact final-head Research and INDEX separately required.

The exact mathematical proof is independent of finite cases because GQ original nonincidence projection uniqueness and global pair injection prove the book-to-triple bijection for EVERY h. The finite checks can detect a hidden erroneous source factor orientation, use of core R where full R is required, miscounting of two physical diagonals per original flag, a wrong original point–line dual, and illicit inference that p might be a second valid nonincident projection. They cannot independently accept the global Branch A all-h path density or the external balanced C6 supersaturation theorem.

**Acceptance:** Local exact identity and its nonnegative correction proven analytically; full Branch A scientific acceptance remains pending a qualified independent external reviewer of #672's dense-core selection, sixth/fourth-moment transfer, and physical-to-original GF(5) completion. No merge, issue closure or ASET exponent claims.
