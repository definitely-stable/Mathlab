# HYP-105 / #230 — AA4-BD: deterministic adaptive global original-LINE assignment by exact GOOD conditional expectation

**STRICT research-only, genuine ORIGINAL symplectic W(3,s), s=2^h. Conditional constructive theorem for h>=5, not original all-fixed (f,g) minimax, not selected original six-incidence seven-class GF(5).** Child of parallel [AA4-BC #564](https://github.com/definitely-stable/Mathlab/pull/564) frozen exact HEAD \`76e67d85603cd7f8316b58b6d0a0d055b0392fb0\`. No main/accepted registry edits. Root issue #230 Branch A/B/C remains OPEN_WITH_FORMAL_BLOCKER.

## 1. Current parallel frontier, provenance and why this is not a repeated stochastic bound

After prior [#559 AA4-AX](https://github.com/definitely-stable/Mathlab/pull/559) source-GQ mixed FᵀBG GOOD port activation analysis, the parallel PR chain advanced:
- [#560 AA4-AY](https://github.com/definitely-stable/Mathlab/pull/560): exact all-D one-whole-original-LINE-bijection conditional mean with globally fixed f and right occupied image support.
- [#561 AA4-AZ](https://github.com/definitely-stable/Mathlab/pull/561): fixed physical support and original AA4-AO CLEAN support right, true source GOOD centered 3flag mean \(\mathbb E_g R_{\rm GOOD}\ge s^6/128\), all h>=5.
- [#562 AA4-BA](https://github.com/definitely-stable/Mathlab/pull/562) and [#563 AA4-BB](https://github.com/definitely-stable/Mathlab/pull/563): increasingly sharp true-original overlapping LINE-ID covariance and O(s^-3) relative GOOD variance for ONE complete global random right map.
- **Immediate parent [#564 AA4-BC](https://github.com/definitely-stable/Mathlab/pull/564)**: if any k≤floor(V/1024) true ORIGINAL source LINE factor physical images are assigned arbitrarily and injectively, while original f and the physical occupied right support E are fixed adversarially, some COMPLETE right assignment extending the pins yields at least s⁶/512 genuine ORIGINAL GOOD physically opposite centered THREE-flag wedges. Parent further proves the conditional mean \(≥s^6/512\), relative variance O(1/V), and probability bound for uniform full completion. Its #564 result is nonconstructive in the sense of giving no deterministic all-original-source-ID map construction without random sampling or factorial search.

**NEW AA4-BD goal**: implement a **finite, deterministic, proof-certified construction** of such a complete legal right source-factor map \(g\), using exact whole-global conditional expectations, while allowing an **adversary to choose the next not-yet-assigned original LINE factor ID adaptively at every step**. The algorithm (not the adversary) must retain the right to select that factor's globally occupied physical pair image. This *constructs* a legal original global g, rather than merely proving that a good g exists. The general conditional-expectation method is classical; research novelty is deliberately restricted to exact TRUE-ORIGINAL symplectic incidence 3flag source weights + globally injected CLEAN two-typed physical C6/D wedge constraints under adversarial pins and source-order.

## 2. True-original mathematical setup and fixed supports

For actual original \(W(3,s)\), \(s=2^h\), set \(V=(s+1)(s^2+1)\), source degree \(d=s+1\), and minimal physical alphabet \(a=\min\{t:\binom t2\ge V\}\). Fix **arbitrary** complete globally injected ORIGINAL point factor physical unordered-pair map \(f:P\to E(K_a)\). Fix **arbitrary** complete right physical image \(E\subseteq E(K_a)\) with exactly V pair edges. Fix any k true ORIGINAL LINE factor IDs \(J\subseteq L\), k≤floor(V/1024), and any one-to-one partial original source LINE assignment \(\phi:J\hookrightarrow E\), potentially adversarially correlated with f and true-original GQ source incidence.

The AA4-AO physical BAD-coordinate sets are determined ONCE from the TWO full occupied physical source factor supports im(f) and E. Removing pinned right physical edges from the *currently free* pool must NOT redefine BAD vertices: globally all right physical pair edges remain occupied after the algorithm completes.

Parent #564 gives an actual source weight dictionary of **ordered, distinct** original source LINE factor triples \((\ell,k_0,k_1)\) with integer multiplicities
\[
w(\ell,k_0,k_1)\ge1.
\]
Each weight counts true original triples of incidence flag IDs with six distinct source factors across its THREE actual original flags (three point IDs and three line IDs), with fixed globally f-labeled point physical pair edges CLEAN and opposite on the two center physical point ports. All actual ORIGINAL source incidence flag IDs are held fixed in the dictionary; these are not freely rewired. For the guaranteed statistic \(R_{\rm free}\), discard source weight keys using any originally pinned LINE factor ID in J. The real selected GF5 six-incidence-ID statistic is not involved.

From the **full fixed** physical E, enumerate precisely the CLEAN ordered physically opposite triple images \((e,x,y)\) with distinct physically occupied original line pair edges and
\[
e\cap x=\{u\},\quad e\cap y=\{v\},\quad u\ne v.
\]
Call this physical set \(\mathcal F(E)\). Both line-side clean physical conditions and point-side original source incidences are explicitly enforced, and no event independently redraws any physical edge. Parent #564's exact conditional initial mean is
\[
\mu_0=\mathbb E_{g\supset\phi}R_{\rm free}
=B_{\rm free}\frac{|\mathcal F(E\setminus\phi(J))|}{(V-k)_3}
\ge s^6/512\qquad(h\ge5).
\]

## 3. NEW BD-1 exact conditional global GOOD expectation for ARBITRARY partial states

Let \(\psi\) be ANY intermediate injective true original LINE source factor map into E, extending the original pins; write n=V−|\operatorname{dom}\psi|. The remaining original LINE factor IDs are jointly uniformly bijected to the n currently unused physical occupied edges of the SAME globally fixed E. For every actual ordered source line triple \(\tau=(\ell,k_0,k_1)\) in the ORIGINAL weight dictionary, let A⊆{0,1,2} denote the subset of positions whose original LINE factor IDs are already prescribed under \(\psi\). For the tuple of physical images prescribed at those positions, let
\[
N_{\psi}(\tau)=\bigl|\{(e,x,y)\in\mathcal F(E):
  \text{prescribed positions equal }\psi(\tau),
  \text{other positions use distinct currently FREE physical edges}\}\bigr|.
\]
Then **EXACT, not an independent-triple approximation**:
\[
\boxed{\displaystyle
\Phi(\psi)=\mathbb E[R_{\rm free}\mid\psi]
=\sum_{\tau} w(\tau)\,
\frac{N_{\psi}(\tau)}{(n)_{3-|A|}}.
}
\]
This is the same single global permutation of all remaining source factor labels for EVERY source 3flag event. Different source triples can overlap arbitrarily. Linearity of expectation, not event independence, justifies the formula. It remains exact at n=0: all original LINE factor pair images are fixed, denominators are 1, and \(\Phi(g)=R_{\rm free}(f,g)\) is an **integer** literal TRUE original physical GOOD threeflag count.

The executor computes the \(N_\psi\) from an independent literal complete physical ordered triple list in the original FULL right CLEAN support, conditioned on prescribed and remaining source image positions; it caches 8 positional pin masks and aggregates all real original source triple weights for matching 3-position masks. It uses Python integer and Fraction arithmetic throughout.

## 4. NEW BD-2 adaptive-source-order deterministic global completion theorem

Let \(j\) be ANY not-yet-pinned ACTUAL original LINE factor ID, chosen even by an adversary based on all prior physical decisions. Under the ONE-GLOBAL-bijection conditional model, its physical edge image is uniformly distributed among the n remaining edges \(e\). The classical tower identity holds EXACTLY:
\[
\boxed{\displaystyle
\frac1n\sum_{e\in E\setminus\operatorname{im}\psi}
\Phi(\psi\cup\{j\mapsto e\})=\Phi(\psi).
}
\]
This statement holds for **every possible** choice of next original source line ID j, no oblivious ordering or independent sample assumption. Select a physical edge image \(e_*\) maximizing the explicitly calculated rational \(\Phi(\psi\cup\{j\mapsto e\})\), breaking ties lexically (by fixed original E image order). Then
\[
\Phi(\psi\cup\{j\mapsto e_*\})\ge\Phi(\psi).
\]

Repeat until every one of the V original LINE factors is globally assigned. Every step preserves the original pins, uses a previously unassigned physical pair edge in E, changes NO original source incidence flag ID or f, and fixes exactly one additional whole original LINE factor image for all of its original flags. Thus after V−k iterations we have one **CONSTRUCTED globally injected complete original LINE map** \(g_*\) with precisely im(g_*)=E and
\[
R_{\rm GOOD}(f,g_*)\ge
R_{\rm free}(f,g_*)=\Phi(g_*)\ge\Phi(\phi)=\mu_0.
\]
Together with the *already proved* parent #564 initial mean bound, this gives:

\[
\boxed{
\begin{array}{l}
\forall h\ge5,\ \forall f,\ E,\ \forall \phi:J\hookrightarrow E,\quad
|J|\le\lfloor V/1024\rfloor,\\[2pt]
\forall\text{ adaptive orders choosing only the NEXT SOURCE LINE ID},\\
\text{the deterministic exact-martingale algorithm constructs a}\\
\text{complete globally injected original LINE map }g_*\supseteq\phi:\\[2pt]
\qquad R_{\rm GOOD}(f,g_*)\ge s^6/512.
\end{array}}
\]

**Scope warning:** If an adversary chooses the NEXT physical edge assignment itself, the monotonicity argument no longer applies. If all V original LINE labels are fixed by an adversary at input, the algorithm has no choices and makes no positivity promise. This is not original #230 Branch A, not an infinite negative counterfamily and not a selected seven-GF5 six-source-incidence motif lower.

## 5. Algorithmic complexity and exact QA

Given the genuine original true-source weight dictionary of size W and a list of F favorable fully physical ordered pair triples (with F≤V(V−1)(V−2)), the implemented exact conditional expectation evaluator groups source triples by at most eight positional fixed-mask patterns and scans favorable physical triples by eight masks. The naïve greedy constructor evaluates at most V(V+1)/2 candidate conditional expectations, so its arithmetic operation count is polynomial, bounded by \(O(V^2(W+8F))\) after the source weights and physical witnesses have been materialized. Construction of the original source weights from actual incidence flags is likewise finite polynomial in the source input size, but very expensive for large s. Exact huge Fractions, actual source size \(N=Vd\) and physical F enumeration mean **NO PRACTICAL large-h runtime or memory efficiency is claimed**. This is a constructive theoretical result plus finite verifications, not a production solver or performance optimization.

Independent falsifiers:
1. Pure combinatorial K4/E(K4) edge-image support with six abstract (explicitly **NOT original W3s**) source LINE IDs, nontrivial overlapping positive source triple weights and ONE arbitrarily locked source→edge assignment: compare the new exact conditional mean with an entirely independent literal exhaustive enumeration of ALL 5!=120 globally bijective full maps. Subsequently choose an adaptive arrival source ID alternating min/max according to prior state; at EVERY step check the exact tower identity across ALL currently legal physical edge choices and nondecreasing selected expectation. At n=0, an independently literal physical triple evaluator must equal the exact rational terminal charge.
2. Genuine original W(3,2) S68 and S72: locked actual original source LINE factor image to a DIFFERENT occupied physical right edge, adaptively complete all 14 unpinned original source LINE labels in reverse order, preserving original point f, source incidence ID list and entire right K6 support. Initial exact GOOD mean independently crosschecked with parent #564's pinned source/physical factor certificate. Final actual threeflag GOOD charge checked by an unrelated **direct literal loop over TRUE ORIGINAL incidence triple flag IDs**, not just the source weight dictionary or the conditional-expectation formula. Parent source R_free≤full R_GOOD verified.
3. Genuine original W(3,4) lex/random with incomplete K14 physical right support (six missing physical edges): take TWO arbitrarily prescribed distinct original LINE source factor images, run two greedy steps, verify exact tower, monotonicity, literal true-source exact conditional initial mean from parent #564, and explicitly do NOT claim a complete map or any s=4 universal floor. The original FULL right support determines BAD coordinates throughout.
4. All dyadic h=5,...,80 in parameter-only exact BigInteger/Fraction arithmetic: import parent #564's rigorous arbitrary k=0,1,floor(V/1024) lower \(\mu_0\ge s^6/512\) and relative-variance certificate as hypothesis; combine with BD-2 proof for a deterministic exact potential-preserving algorithm without ever fabricating huge finite source GQ adjacency matrices.
5. Negative tests for repeated pins/non-injected global edge support, source line factors outside original range, invalid three-distinct-line original weight keys, out-of-support images, illegal second assignment of an already pinned original line, invalid explicit order and negative partial-step budget.
6. Strict scientific nonimplications: even a constructed original full g with \(R_{\rm GOOD}\ge s^6/512\) counts physical GOOD **three-original-incidence-flag** objects, not accepted six-distinct-incidence selected GF5 motifs; the original 3×3 Hall, residual T/P physical template and final seven-GF5 selection remain open. This certificate is for the **constructed** g, not every adversarial preexisting fully fixed right map. No original R3/ASET exponent.

**Acceptance:** strict Draft child of #564, pinned exact parent HEAD. Require final HEAD dedicated GitHub-hosted CI, INDEX, Proof Audit and Full Research and a separate independent mathematics referee before any scientific acceptance, SHA-pinned canonical RCP claim registration or regeneration of derived five research indexes. Do not edit main or merge without ancestor approvals. Next AA4-BE: attempt to derandomize source 3flag→original residual 3×3 source Hall / selected GF5 six-ID transfer under constrained maps, or find original joint f/g deterministic obstruction; **do not** mistake this conditional-expectation algorithm for a fixed-adversarial-full-g positive theorem.
