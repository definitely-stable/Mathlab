# HYP-105 #230 — AA4-PAIRRANK: exact joint survival of TWO true ORIGINAL selector paths and a source second moment

**Scope:** strict scientific child of [Draft PR #751](https://github.com/definitely-stable/Mathlab/pull/751), frozen parent SHA 476ca10207dc187e2258cfc2e5615c1c2d746b57. A self-contained ALL-ORDER mathematical lemma, independently tested on genuine W(3,2), W(3,4), for the exact joint behavior of TWO proper physical paths under ONE SHARED original source-priority order and TWO SHARED typed physical-coordinate cuts. This does not alter old parent/main, close issue #230, automatically accept the full Branch A theorem, assert new asymptotic exponents or pretend numerical graph supersaturation constants are known.

## 1. Why pair probabilities are the next nontrivial missing interface

Predecessors #738 and #745 correctly prove individual r=2,3 proper physical path source-survival lower bounds

\[
\Pr(\gamma\text{ selected}) \ge \frac{1}{4^r\binom{r(K+1)}r}
\]

without postulating independence of paths, and use Jensen to transfer this to an upper bound on the proper-path tensor second moment. That result is correct but is necessarily lossy: paths share physical coordinates, true original incidence flag owners, original J-conflict neighbors and binary-color assignments. Merely multiplying single-path probabilities for overlapping paths gives wrong covariance, potentially of BOTH signs. The new result supplies the exact pairwise source distribution, which yields the true selected second moment and its Jensen variance slack for arbitrary fixed correlated f and g. It uses no synthetic substitute for the actual original W(3,s) source in the finite positive and negative witnesses.

## 2. Full all-order source setup and exact statement

For each true symplectic W(3,s), s=2^h, take ANY fixed complete separately globally pair-injected label maps f:P→binom([a],2), g:L→binom([a],2), with arbitrary correlations, ANY original incidence-ID deleted set Z and ANY paired surviving ORIGINAL source core C⊆I\Z. Each original flag (p,ell)∈C owns both TRUE opposite physical rectangle diagonals. Let J_C be the ORIGINAL symmetric source-conflict graph on C: two different original flags conflict precisely when they share an original point and their physical g-line factor pairs overlap, or they share an original line and their physical f-point factor pairs overlap. For LOW, its original maximum degree is at most K=64; the theorem below does NOT require that particular bound.

One source selector experiment ω draws:
(1) one uniform total random priority order on the original flags C;
(2) one independent fair binary coloring of all first-typed physical alphabet symbols;
(3) one independent fair binary coloring of all second-typed physical alphabet symbols.
An original flag is retained iff it is earlier in the SAME global priority order than EVERY actual J_C-neighbor and its ACTUAL f and g factor pairs are both bichromatic. Both original physical diagonals survive together.

For two fixed true physical coordinate-proper directed r=3 paths γ and η, let S be the distinct ORIGINAL incidence-ID owners of their UNION (at most six). Their simultaneous selected-path event is EXACTLY the event that every original ID in S survives this common source selector. Define p_J(S) as the probability all S owners beat their actual J-neighbors, and c_f(S),c_g(S) as the probabilities all original factor-pair edges attached to S cross their respective typed cuts. Because the THREE random experiments are independent, but the two paths are NOT,

\[
\boxed{
\Pr(\gamma,\eta\ {\rm both\ selected})
 = p_J(S)\,c_f(S)\,c_g(S).
}\tag{PAIR-1}
\]

If S contains a true original J_C edge, then p_J(S)=0: two incident competitors can never both be first. This can force a ZERO joint path survival probability even when each path individually survives with positive probability.

## 3. NEW exact all-order global-source priority formula with at most SIX factorial terms

Suppose S is an independent set of J_C, with k=|S|≤6. Let U=S∪N_J(S), and N=U\S. Only these actual ORIGINAL local neighbors matter; any other source flags may be freely interleaved in the uniform global priority without affecting the event.

Represent the random source order by independent real priorities T_i uniform on [0,1], which almost surely induce a uniform permutation. Fix one ordering π=(π_1,...,π_k) of the owners by increasing T. For every original outside neighbor z∈N, define j_π(z) as the **largest** position j such that z is J-adjacent to π_j. Define

\[
c_j(\pi)=\#\{z\in N:j_\pi(z)=j\},
\qquad j=1,\ldots,k.
\]

Conditionally on the true owner priorities with 0<T_{π_1}<⋯<T_{π_k}<1, the **necessary and sufficient** priority constraints for all selected owners are T_z>max(T_i:i∈S∩N_J(z))=T_{π_{j_π(z)}} for each z∈N. As the outsider priorities are independent, the conditional probability is the product ∏_{j=1}^k (1−T_{π_j})^{c_j(π)}. The unconditional probability is integrated over the ordered simplex, with density 1, not multiplied by k! because we sum over the k! possible π.

Substitute t_j=1−T_{π_{k+1−j}} to reverse the simplex; integration of the successive powers from the smallest variable gives the EXACT rational closed form

\[
\boxed{
p_J(S)=
\sum_{\pi\in\mathfrak S(S)}
\ \prod_{j=1}^k
\frac{1}{\,k-j+1+\sum_{t=j}^{k}c_t(\pi)\,}.
}\tag{PAIR-2}
\]

For S=∅ set p_J(S)=1; for a non-independent S set p_J(S)=0.

**Important:** the source graph size |I| may grow with s and U may contain many neighbors, but PAIR-2 requires only k! permutation terms, with k≤6, and actual neighbor-union incidence counts. It is an exact deterministic rational expression for EACH fixed original f,g,C,Z, with no correlation assumptions, no Monte Carlo and no asymptotic approximation. The proof holds for arbitrary original source conflict graphs as long as S is the prescribed owner set.

Example of the genuinely necessary shared-neighbor correction: distinct independent original owners 1 and 2 both compete with a single outside original source neighbor 3. Then the exact probability both win is 1/3 (source neighbor is last of three), whereas the product of their separate win probabilities is (1/2)(1/2)=1/4. The latter would be wrong.

The new program evaluates PAIR-2 independently of the prior source selector programs and checks selected genuine-original witness cases against a **separate** integer bitmask dynamic program counting all linear extensions of the actual precedence poset i≺z for i∈S and z∈N_J(i). This independent calculation does NOT use the order-statistic integral or owner permutations.

## 4. NEW exact typed two-cut formula; odd cycles make selected paths mutually impossible

For side h∈{f,g}, form the small ACTUAL simple graph H_h(S) whose physical symbol vertices are the symbols present in the original factor pairs h(i), i∈S, and whose edges are those factor pairs (duplicate edges from shared original point/line factors are collapsed). It is NOT the original GQ incidence graph, but a precisely defined physical-coordinate alphabet constraint graph.

A binary coloring of those physical symbols makes every selected flag factor-pair bichromatic iff this graph is bipartite. If a connected component is bipartite, choosing the bit at any root uniquely forces all its other bits by alternation; exactly two assignments per nonempty connected component survive. For v_h used physical symbols and κ_h connected components,

\[
\boxed{
c_h(S)=
\begin{cases}
2^{\kappa_h-v_h}, & H_h(S)\ \text{bipartite},\\
0, & H_h(S)\ \text{contains an odd cycle}.
\end{cases}
}\tag{PAIR-3}
\]

The new independent oracle exhausts all 2^{v_h} literal assignments for selected original witnesses and compares to PAIR-3 separately for both actual typed physical label alphabets. This catches impossible joint paths from non-bipartite union even when there is no J conflict.

In a single coordinate-proper r-path, its original factor edges form an ordinary simple length-r physical symbol path, so c_f=c_g=2^{-r} and PAIR-1 recovers the established single-path probability formula exactly with p_J({r owners}). For TWO paths, no product c_h(S1)c_h(S2) is allowed without proving separation.

## 5. New exact selected P3 endpoint-tensor second moment and true Jensen gap

Let P3(u,v) count ALL directed coordinate-proper physical source CORE three-paths between actual physical vertices u and v. Let X_ω(u,v) count those surviving the same actual full selector ω; for each path γ let I_γ(ω) be its 0/1 survival indicator.

By finite linearity, with NO independence hypothesis,

\[
\mathbb E X_\omega(u,v)
 =\sum_{\gamma:u\to v}p_J(S_\gamma)c_f(S_\gamma)c_g(S_\gamma).
\tag{PAIR-4}
\]

Also by expanding the literal square and applying PAIR-1,

\[
\boxed{
\mathbb E\|X_\omega\|_F^2
 =\sum_{u,v}\sum_{\gamma,\eta:u\to v}
   p_J(S_\gamma\cup S_\eta)c_f(S_\gamma\cup S_\eta)c_g(S_\gamma\cup S_\eta).
}\tag{PAIR-5}
\]

The exact Jensen gap, equal to the sum of the endpoint variances, is

\[
\boxed{
\mathbb E\|X_\omega\|_F^2-\|\mathbb E X_\omega\|_F^2
 =\sum_{u,v}\sum_{\gamma,\eta:u\to v}
   \operatorname{Cov}(I_\gamma,I_\eta)\ge0.
}\tag{PAIR-6}
\]

Individual covariances can be POSITIVE OR NEGATIVE; only the entire grouped variance is nonnegative. The old uniform Jensen bound remains valid regardless of covariance sign:

\[
q_3^{-2}\|P_3\|_F^2
 \le\|\mathbb E X_\omega\|_F^2
 \le\mathbb E\|X_\omega\|_F^2
 \le\sup_\omega\operatorname{tr}(A_{G_\omega}^6),
\quad q_3=64\binom{3(K+1)}3.
\tag{PAIR-7}
\]

Thus PAIR-5 is an independently calculated **instance-exact** refinement of the proper-path source tensor interface, not a new claimed universal independent-path product bound.

For the WHOLE genuine-original W(3,2) lex physical CORE, the new program enumerates every coordinate-proper directed physical source 3path, groups all by ordered actual physical endpoints, computes ALL path-pair joint probabilities as exact fractions, checks sum-of-squares pair multiplicities, the exact full selected second moment, exact first moments, nonnegative Jensen gap and both positive/negative actual-source pairwise covariance witnesses. No sampled approximation is substituted for the W32 full tensor. For true W(3,4), full original or reduced cores are used for deterministic path/witness samples and individual source survival lower-floor falsification; no claim of a full W34 moment is made for sampled subsets.

## 6. Independent finite falsification and rigor limits

The main new script imports ONLY the true symplectic source fixture from AA4-DEGFACT/#748 to generate all 45/425 ORIGINAL incidence IDs, constructs its own complete globally pair-injected lex/reversed/shifted f/g maps, actual J_C point/line conflict edges, two real opposite physical diagonals per original ID, true coordinate-proper 3path enumeration, pairwise source owner unions, exact finite order-statistic formulas, exact typed symbol-bipartite formula, and exact full W32 physical P3 endpoint moment.

The tests use independent source ordinal DAG linear-extension subset dynamic programming and literal exhaustive physical symbol coloring, and insist on **distinct genuine-original positive and negative covariance path pairs**. Pure three-vertex abstract priority sanity checks are used ONLY as algebraic identities, never substituted for the real source experiments.

The new hosted specialist workflow performs 18 independent test methods, emits one strict JSON certificate with actual source path-pair witnesses, true all-endpoint second moment and constraints, and retains ROOT_STATUS=OPEN_WITH_FORMAL_BLOCKER; INDEX and full Research CI run on the SAME final GitHub SHA.

**Scientific limitation:** PAIR-1–PAIR-6 are rigorous exact all-order probability identities. They are new independent source-compatible auditing tools for the LOW proper-P3 energy step, but do not prove an improved absolute bound on the all-h seven-class original six-motif S_s, publish explicit external C6 graph constants, close #230 or justify an ASET extraction exponent. The final root acceptance still requires an adversarial all-h audit of the original selector/Moment/point-line source books and GF5 positive-class mapping together with the previous HEAVY chain.

## 7. New complete ORIGINAL W32 covariance stratification and exact certificate (empirical source result)

The full original symplectic W(3,2) lex source has 45 actual incidence flags, 90 real physical opposite-diagonal edges, maximum actual J source degree 4, and 1,346 genuine coordinate-proper directed physical threepaths, grouped into 624 ordered physical endpoint bins. There are exactly 4,370 ordered pairs (γ,η) of such physical paths with IDENTICAL ordered endpoints, counted with multiplicity including γ=η. These are NOT sampled; the executable enumerates every one.

The exact joint probability of every path pair is computed from PAIR-2/PAIR-3 on its original owner union. The independent exact second-moment/covariance ledger yields:

| Full W32 exact property | Value |
| --- | ---: |
| P3 proper directed paths | 1,346 |
| Source endpoint bins | 624 |
| Ordered same-endpoint path pairs, exactly ||P3||_F² | 4,370 |
| Ordered path pairs with positive covariance | 2,386 |
| Ordered path pairs with negative covariance | 1,984 |
| Mutually exclusive owing to TRUE J source-owner conflict | 1,348 |
| Mutually exclusive owing to true first-factor ODD physical symbol cycle without J conflict | 464 |
| Mutually exclusive owing to true second-factor ODD physical symbol cycle without J conflict or first-factor failure | 172 |

In this actual instance the three disjoint reasons for a zero joint survival probability total 1,348+464+172=1,984. Both first- and second-factor odd-cycle witnesses are SOURCE-GROUNDED: each pair of paths individually survives with positive probability, the union of their source owners is independently J-free, but the physical factor symbol graph of their UNION is not bipartite. Therefore even source-conflict independence alone does NOT make the two-path indicators jointly realizable.

Full exact rational selected second-moment values (on the same W32 true source, not a synthetic graph) are:

\[
\begin{aligned}
\mathbb E\Vert X\Vert_F^2
 &=\frac{2464778346891846823}{3826102303457280000},\\
\Vert\mathbb EX\Vert_F^2
 &=\frac{170009657654496199}{164130319761408000000},\\
\mathbb E\Vert X\Vert_F^2-\Vert\mathbb EX\Vert_F^2
 &=\frac{5489586524019325126911803}
 {8535269018552500224000000}.
\end{aligned}
\]

A genuinely **separate** sum over all 4,370 exact pairwise covariances equals that last fraction and is also partitioned by whether the two physical paths share at least one named ORIGINAL source owner. In this instance, the disjoint-owner path-pair group has negative total covariance while the shared-owner path-pair group has positive total covariance; they cancel partially and sum exactly to the nonnegative total variance.

The observed exact selected-second/Jensen ratio in W32 is

\[
\frac{\mathbb E\Vert X\Vert_F^2}{\Vert\mathbb EX\Vert_F^2}
 =\frac{5498427536246331892748400}{8841012227006765836597}.
\]

This illustrates a large Jensen slack at small finite source size, **not** a uniform all-h asymptotic improvement. Any attempted replacement of the uniform q3 selector factor must control both types of covariance and all possible correlated f,g, not merely match this W32 instance.

The GitHub-hosted strict certificate additionally requires all ordered pair covariance sign counts to sum to 4,370, all exclusive zero-joint source/typed-odd-cycle categories to have valid true-original source witnesses, and the exact sum of positive and negative pairwise covariances to equal the independently computed nonnegative full endpoint variance. A separate ordinal-bitmask DP and literal bit-color enumeration validate the genuine-source odd-cycle witnesses, independently of the closed-form rank and bipartite graph formulas.

## Next mathematically allowed action

Use PAIR-5 for a **structural** covariance/second-moment inequality that can replace or certify the lossy Jensen original-source bound uniformly in the adversarial fixed f,g setting, or complete independent line-by-line acceptance of the remaining all-h LOW and GF5 source proof DAG. Do not merge stacked Draft PRs or close #230 without these gates.
