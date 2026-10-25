# HYP-105 / #230 — D6-AA1–AA3: six-column positional collision tensor

**Scope:** exact all-h **LOCAL** factorization of the seven accepted six-coordinate GF(5) necessary motif classes, plus exact all-order one-sided and joint ORIGINAL-incidence moment identities. All seven floors remain those of #230; there is **NO** universal positive \(\Omega(s^6)\) certificate here, no full \(R_3\), no ASET exponent. Branch A/B OPEN; #230 OPEN.

**Parent:** D6-Z draft PR #428, fixed HEAD \`d3b78794e2bdd9ee47d4bf7419afd59a37cb5b1a\`. This is a stacked Draft, never merge into \`main\` without separate acceptance and review. The parent material is inherited exactly.

## Model and theorem AA1 — exact finite positional factorization

Let \(s=2^h\) with \(h\ge1\), \(V=(s+1)(s^2+1)\), \(\Delta=s+1\); let \(I_s\) be the ORIGINAL \(N=V\Delta\) pairwise-distinct point–line incidences of the symplectic generalized quadrangle \(W(3,s)\). Label original point and line factors with **independent globally injective** physical unordered coordinate pairs \(f(p)\), \(g(\ell)\), within \(K_a\), \(a=\min\{a:\binom a2\ge V\}\). No assumption of statistical independence between \(f\) and \(g\) or their assignments over ORIGINAL incidence positions.

For a six-distinct-incidence set \(Q=\{e_1,\ldots,e_6\}\), retain one consistent order for the six ORIGINAL positions on both typed sides. Define \(D_X(c)=\{i:c\in \lambda_X(e_i)\}\), \(d_X(c)=|D_X(c)|\). Compute

\[
B^X_{ij} = |\lambda_X(e_i)\cap\lambda_X(e_j)| \in\{0,1,2\},\qquad
W^X_k(Q)=\sum_c\binom{d_X(c)}k.
\]

In particular \(W^X_2=\sum_{i<j}B^X_{ij}\). Because \(\sum_c d_X(c)=12\) for exactly six physical pairs, we have the **if and only if**

\[
\boxed{\text{six distinct physical coordinates, each of degree 2}
\iff W^X_2=6\land W^X_3=0.}
\]

Proof: \(W_3=0\) forbids any \(d(c)\ge3\). Hence every positive degree is 1 or 2; \(W_2=6\) implies exactly six degree-2 coordinates, consuming all 12 physical occurrences. Conversely the 2-regular signature has six wedges and no triples. This is valid for *any* physical alphabet, including repeated physical pairs arising at repeated ORIGINAL factors.

When the test succeeds, each physical coordinate \(c\) is a pair of distinct ORIGINAL positions \(D_X(c)=\{i,j\}\). Take these six \(D_X(c)\), with multiplicity, as edges of a loopless 2-regular multigraph \(G_X(Q)\) on six **indexed incidence positions**. The matrix \(B^X\) is its complete weighted adjacency matrix.

Every degree-2 loopless multigraph on six named vertices decomposes into cycles of length at least two; a two-cycle is a doubled edge. The complete list:

| Positional graph | Count | Class |
|---|---:|---|
| One \(C_6\) | 60 | A |
| \(C_3\sqcup C_3\) | 10 | A |
| \(C_4\sqcup C_2\) | 45 | B |
| \(C_2\sqcup C_2\sqcup C_2\) | 15 | C |
| **Total** | **130** | |

Counts use *labeled* six positions, not graph-isomorphism classes. They can be independently enumerated as six-element multisets of the 15 unordered distinct position pairs with degree exactly two on all six vertices.

**Connection with ORIGINAL typed factor partitions:** globally injective \(f,g\) guarantee a doubled physical edge of two column positions is exactly two incidences with the same ORIGINAL typed factor; for A all typed factors are distinct. Under physical 2-regularity, any repeated original factor can occur only twice. Therefore A/B/C can be recovered from \(G_X\) without consulting any GF(5) routine.

Define the finite deterministic predicate \(\Phi(G_L,G_R)\) as follows:

1. If either side fails \((W_2,W_3)=(6,0)\): reject.
2. A/A: accept **D6** iff both are a single \(C_6\) and their *indexed, multiplicity-sensitive positional graphs coincide*. Two \(C_3\)'s are not D6.
3. B/A: accept **B-left/A-right**; A/B: **A-left/B-right**.
4. C/A or A/C: accept **C/A**; C/B or B/C: accept **C/B**.
5. B/B: let \(D_L,D_R\subseteq\{1,\ldots,6\}\) be the respective unique doubled-edge endpoint pairs. Accept **B/B-overlap** iff \(|D_L\cap D_R|=1\); **B/B-disjoint** iff this cardinality is zero. \(|D_L\cap D_R|=2\) would repeat the same ORIGINAL \((p,\ell)\) incidence and is invalid under distinct Q.
6. C/C: reject. If three ORIGINAL points and three ORIGINAL lines each occur twice in six distinct incidences, the source incidence subgraph must be a simple 6-cycle (its 2-regular bipartite graph has six distinct vertices). That violates the girth-eight axiom of the genuine \(W(3,s)\).

Thus for every such genuine ORIGINAL \(W(3,s)\),

\[
\boxed{\mathbf1_{\rm seven}(Q)=
\Phi(B^L(Q),W^L_3(Q),B^R(Q),W^R_3(Q)).}
\]

This identity identifies only the **seven accepted necessary positive classes**, with weights
D6 5643, BA 45600, AB 45600, CA 43320, CB 49050, BBo 51750, BBd 45010. The fixed \(51^6R_3\) lower certificate is the weighted sum of the seven *ORIGINAL sixsets*, counted once each. No other GF(5) classes, sign cancellations, or full strict \(R_3\) are inferred from \(\Phi\).

**Important qualification:** the presence of a triple moment is not cosmetic. Two disjoint triangles and two disjoint \(K_{1,3}\) stars, with corresponding edge order, have identical 15 pairwise physical edge intersections and \(W_2=6\), but \(W_3=0\) versus \(W_3=2\). The positional matrix *without* the triple certificate cannot distinguish these. This is the classical Whitney line-graph ambiguity, not a new standalone graph theorem.

## Theorem AA3-S — one-sided moments of all six orders

For a physical coordinate \(c\), let \(n_c(f)\) count how many of the \(V\) *distinct ORIGINAL point factors* receive a physical pair containing \(c\). Since each ORIGINAL point is incident to exactly \(\Delta\) ORIGINAL lines, that coordinate appears in precisely \(D_c=\Delta\,n_c(f)\) ORIGINAL incidence positions. For \(1\le k\le6\),

\[
\boxed{
\sum_{\substack{Q\subseteq I_s\\|Q|=6}}
W_k^L(Q)
=\binom{N-k}{6-k}\sum_c\binom{\Delta n_c(f)}k.}
\]

The formula for the right side uses original lines and \(g\). Proof: double-count \((Q,c,A)\), with \(A\subseteq Q\), \(|A|=k\), and all \(k\) positions sharing \(c\). Fix \(c,A\) first, then choose the other \(6-k\) positions from \(N-k\) ORIGINAL incidences. This theorem is exact for ALL \(h\), not a random-label expectation. It holds on any regular incidence host with the stipulated degrees.

All these **aggregated one-sided** moments depend only on the physical image degrees \(n_c(f)\) or \(n_c(g)\), rather than the assignment of which original point/line receives each label. Their full *one-sided sixset distribution* also depends only on these degrees / physical image, by the formal generating polynomial \(\prod_{e\in\mathrm{Im}(f)}(1+t x_{e_1}x_{e_2})^\Delta\). They are not enough to reconstruct the correlated seven-class count.

## Theorem AA3-J — joint moments retain ORIGINAL source incidence

Set
\(M_r^L(Q)=\sum_c\binom{d_L^Q(c)}r\) and
\(M_t^R(Q)=\sum_d\binom{d_R^Q(d)}t\), \(1\le r,t\le6\).

For each physical coordinate pair \((c,d)\), partition the \(N\) ORIGINAL incidences according to whether their \(f(p)\) contains \(c\) and \(g(\ell)\) contains \(d\). Let \(n_{11},n_{10},n_{01},n_{00}\) be the four cell sizes (each **ORIGINAL incidence** is counted individually). Let

\[
H_{c,d}^{r,t,j} =
[x^{r-j}y^{t-j}z^j]\,
(1+x+y+z)^{n_{11}}\,
(1+x)^{n_{10}}\,
(1+y)^{n_{01}}.
\]

This counts ordered pairs of \(r\)- and \(t\)-subsets \((A,B)\) of ORIGINAL incidence positions such that all members of \(A\) carry \(c\) on the left, all members of \(B\) carry \(d\) on the right, and \(|A\cap B|=j\). In the first factor, \`z\` means a row selected in both sets; \`x,y\` select one side only.

Consequently, without any independence assumption,

\[
\boxed{
\sum_{\substack{Q\subseteq I_s\\|Q|=6}}
M_r^L(Q)M_t^R(Q)
=\sum_{j=\max(0,r+t-6)}^{\min(r,t)}
\binom{N-r-t+j}{6-r-t+j}
\sum_{c,d}H_{c,d}^{r,t,j}.}
\]

Proof: expand each moment as a sum over typed incidence subsets A and B; sort them by overlap \(j\), then choose the rest of Q outside their union, in \(\binom{N-(r+t-j)}{6-(r+t-j)}\) ways. The coefficient extracts the 4-cell subset choices exactly. Unlike the one-sided formula, \(n_{11}(c,d)=|\{(p,\ell)\in I_s:c\in f(p),d\in g(\ell)\}|\) encodes the *coupled original geometry*. Its row/column totals alone cannot generally determine higher joint statistics.

Both AA3 formulas are exact enumerative identities, **not positive bounds**. The scalar products \(M_rM_t\) still lose some positional information carried by \(\Phi\): an all-h seven-class proof must retain indexed physical pair/triple arrangements or strengthen the joint algebra to anchored positional tensors.

## Reproducible acceptance evidence

- Run the completely independent six-position 2-regular multigraph multiset enumerator: \(60+10+45+15=130\).
- Check the Whitney triangle/star collision with identical 15 pairwise entries but differing W3.
- Verify simultaneous six-column permutations preserve the tag; reject nonaligned A/A and impossible B/B identical double incidence.
- Compare the independent positional \(\Phi\) against the accepted historical classifier on **each of 62,370 left candidates** independently for both true ORIGINAL S68 and S72 W(3,2), including all rejected cases. Check all seven fixed GF(5) coefficients and total counts 68 and 72. An additional symplectic construction oracle enumerates independently with its own geometry and physical templates.
- Verify one-sided aggregate orders k=1,...,6 and brute-expand every sixset of an 8-incidence toy host; check joint (r,t) in 1,...,6 against a separate brute 8-incidence host enumeration, and real W32 source joint cells.
- The dedicated GitHub-hosted workflow, shared INDEX/Proof Audit/Research workflows must be inspected on the same final PR SHA. Never claim them green in advance.

## D6-AA4 — explicit global feasibility target (NOT solved)

Let \(\mathcal G\) be the 130 indexed 2-regular six-position multigraphs and let \(z_{G,H}\) be the number of sixsets whose two physical positional projections are \(G,H\), extended by nonregular states as required. The exact seven sum is

\[
S_s(f,g)=\sum_{G,H\in\mathcal G} z_{G,H}\Phi(G,H).
\]

A legitimate universal \(c>0\) would require **geometry-realizable** \(z\) obeying source GQ incidence constraints, both complete global-injectivity maps, and all relevant physical capacity and positional consistency inequalities, with \(\sum z\Phi\ge cs^6\) for *every* \(s=2^h\). The 130-by-130 pattern matrix alone does not impose those global constraints. In particular, independently optimizing sixset marginal frequencies is NOT justified: D6-T/U/V/X/Y already produce relaxations that do not certify the desired positive lower.

**AA4 disposition: OPEN_FEASIBILITY**, not PROVED_A, COUNTEREXAMPLE_B or a new ASET exponent. The next mathematical object should be an anchored *source-incidence* coupled positional tensor with all six columns and global assignment consistency; test any proposed LP/SOS relaxation against true S68/S72 before claiming strength. No automatic continuation into unrestricted enumeration of W(3,4).

## Research integrity gate

- Exact local factorization is proven from pair multiplicities, graph decomposition, and GQ girth; finite W32 tests are falsifiers, not the all-h proof.
- GF(5) fixed weights are imported unchanged from the previously accepted #230 bounds; no new full-palette Fourier proof is asserted here.
- The asymptotic target \(\forall h\ge1\;\forall f,g\) globally injective: \(S_{2^h}(f,g)\ge c\,2^{6h}\) with absolute \(c>0\) remains unproved.
- Do not close #230, #176 or #169, merge \`main\`, or imply global ASET consequences from this reduction.
