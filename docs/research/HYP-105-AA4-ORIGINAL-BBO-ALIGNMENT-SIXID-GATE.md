# HYP-105 #230 — AA4-ORIGINAL-BBO-ALIGN-DAG: independent exact six-incidence-ID B/B-overlap inverse and signed-class audit

**Scientific status: OPEN_WITH_FORMAL_BLOCKER.** Strict Draft child of frozen [PR #780](https://github.com/definitely-stable/Mathlab/pull/780), exact parent commit \`cb8747e6fa20e80d454ae3c8047ecce015379fef\`. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) remains OPEN. No parent or main changes, merges, automatic publication/PROVED_A promotion, invented numeric ordinary-graph C6 supersaturation constants, or new ASET exponent.

This is a **focused independent mathematical referee** of the source-sixset inverse and its interface to the actual positive GF(5) motif class. Previous [#734](https://github.com/definitely-stable/Mathlab/pull/734), [#751](https://github.com/definitely-stable/Mathlab/pull/751), [#758] and \`research/hyp105_BBo_inverse_source_bridge.py\` already proposed/proved source sixset reconstruction; \`research/hyp105_original_aligned_bbo_gf5_fourier_referee.py\` already identified 3 aligned out of 9 B/B C4×C4 configurations and their signed mass. These discoveries are **not** presented as novel. Here the contribution is an independent complete necessary-and-sufficient **original flag and physical factor** criterion, a separately implemented exhaustive physical-first inverse over actual W32/W34 CORE and deletion masks, and an independent **integer** GF5 character oracle that validates the membership and positivity of the very same sixsets used by Branch A. The goal is to close the *scientific acceptance gate* without quietly extrapolating finite experiments.

## 1. Precise original source, full anchors versus smaller physical CORE

For any dyadic \(s=2^h\) consider **genuine** symplectic W(3,s). The original named source flag set is

\[
I=\{(u,\ell):u\in\ell\},\quad |P|=|L|=(s+1)(s^2+1),\quad |I|=(s+1)^2(s^2+1).
\]

Let \([a]\) be the **minimal** physical symbol alphabet with \(\binom a2\ge|P|\). Fix ANY two **complete** separately globally pair-injective maps \(f:P\to\binom{[a]}2\), \(g:L\to\binom{[a]}2\), with arbitrary correlation. Let \(A=I\setminus Z\) be the full allowed original source (for root choose Z=empty), and \(C\subseteq A\) the actually selected named CORE. Every flag i=(u,ell_u)∈C owns **two** opposite, vertex-disjoint, undirected physical diagonals of its actual rectangle \(f(u)\times g(\ell_u)\); each physical edge has ONE source owner, determined uniquely by the unordered x-difference and y-difference, thanks to f/g global injectivity.

The six original incidence IDs considered in the B/B-overlap class are **UNORDERED SIX DISTINCT original flags**, not six coordinate occurrences, six physical edges or GF5 signed assignments. The accepted ROOT seven-class sum counts each distinct original sixset ONCE. A fully produced original sixset below has exactly TWO directed physical 3path preimages, and hence contributes exactly 1 to the unweighted B/B-overlap count.

## 2. Canonical six ORIGINAL flags and unique three-flag GQ projection anchor

Given ANY unordered six original flag IDs \(\Sigma\subset I\), first compute exact original point and line factor multiplicities:

\[
|\operatorname{supp}_P\Sigma|=|\operatorname{supp}_L\Sigma|=5,\quad
\{m_P\}=\{2,1,1,1,1\},\quad\{m_L\}=\{2,1,1,1,1\}.
\tag{BI-1}
\]

If this fails, the sixset is NOT the B/B-overlap candidate subfamily. Let p be the **unique repeated** original point and ell the **unique repeated** original line. In the overlap case their common flag \((p,\ell)\) MUST be a member of \(\Sigma\). Then exactly one more flag in \(\Sigma\) lies on original p, written \((p,r)\), and exactly one more flag belongs to original line ell, written \((q,\ell)\). The three unique anchor IDs are

\[
\boxed{J_{\Sigma}=\{(q,\ell),(p,\ell),(p,r)\},\qquad
H_{\Sigma}=\Sigma\setminus J_{\Sigma},\quad |H_{\Sigma}|=3.}
\tag{BI-2}
\]

No other anchor choice is possible. The all-order original GQ projection theorem #780 then demands \((q,r)\) is genuinely NONINCIDENT and that \(\pi(q,r)=(p,\ell)\) in the **full** true GQ geometry. All three flags in \(J_{\Sigma}\) must belong to FULL A, but **not necessarily physical C**. Every flag in the three-element HΣ must lie in the **paired physical CORE C**, and none of the six source IDs may lie in the deletion set Z. Otherwise \(\Sigma\) has ZERO accepted physical preimages for this CORE, irrespective of its standalone GF5 positivity.

The distinct original factor multiplicity profile BI-1 and unique anchor BI-2 ensure p,ell,q,r and the three other original point/line factors are all distinct where required; no source owner appears under a second physical label.

## 3. NEW independent factor-graph certificate: necessary and sufficient for exactly 0/2 physical inverses

From the three residual ORIGINAL flags \(H_\Sigma=\{i_1,i_2,i_3\}\), build two **ordinary simple factor graphs**, with no physical path enumeration:

\[
G_x(\Sigma)=\{f(\operatorname{point}(i)):i\in H_\Sigma\},\quad
G_y(\Sigma)=\{g(\operatorname{line}(i)):i\in H_\Sigma\}.
\tag{BI-3}
\]

A physical coordinate-proper 3path requires each of \(G_x,G_y\) to be a 4-vertex **three-edge simple PATH** (degree multiset 1,1,2,2), and its endpoints to equal the two original physical symbols in f(q) and g(r) respectively. The factor graph of the four source flags {q-anchor + three residual owners} must consequently be one ordinary C4 in K_a, likewise on the line side {r-anchor + three residual owners}. The repeated original p and ell own labels completely **disjoint** from the respective four physical symbols, or the endpoint-good/inner-blocker acceptance fails.

If either three-edge graph is not a true P4, the endpoint pairs do not close the original q/r factors, or p/ell contains one of their physical path coordinates, declare zero. There is no smuggling in a synthetic factor edge. The first factor P4 has precisely **two possible directed orientations**, reversals of each other. In one orientation its actual ORIGINAL three source owner edge order is a permutation \(\sigma_x=(i_a,i_b,i_c)\); in the other it is its reversal. The second factor P4 analogously has \(\sigma_y=(i_d,i_e,i_f)\) and its reverse.

One physical edge corresponding to source owner i must move one step in BOTH first and second physical symbols, so a physical directed 3path can exist **if and only if**

\[
\boxed{\sigma_x=\sigma_y\quad\text{for some choice of the two side orientations}.}
\tag{BI-4}
\]

This is the **source middle-owner alignment** criterion: because each P4 has exactly three distinct edge IDs, it is equivalent to the central source owner i_b in the first factor P4 being the same as the central source owner i_e in the second factor P4. If center IDs disagree, no possible pairing of the opposite physical diagonals can produce a proper physical length-3 path under one original owner sequence. If they agree, there are exactly TWO aligned orientation pairs: one forward, one reverse. Every physical ordered corner path \((v_0,v_1,v_2,v_3)\) is **FORCED** by matching the first/second ordered symbol sequences, and each step is one of the two REAL source-owned physical diagonals of its corresponding HΣ owner flag. No other order, starting vertex, independent y-sign choice or physical source copy exists. Thus the exact **all-h finite-combinatorial theorem** is

\[
\boxed{
\#\{\text{admissible directed physical P3 owned by C and decoding to }\Sigma\}
=
\begin{cases}
2,&\text{genuine anchors, C/Z, both P4 closures and center alignment},\\
0,&\text{otherwise}.
\end{cases}
}\tag{BI-5}
\]

The two paths in the first case are EXACT reversals. The proof does not assume any distribution of fixed f/g, any graph eigenvalues, W32/W34 pattern fitting, path-event independence, or any numerical external C6 theorem. The GQ assumption is used only for unique original anchor projection; the factor alignment lemma itself is purely finite graph combinatorics.

**Do not overclaim surjectivity:** a HISTORICAL positive B/B-overlap six-ID set may be C4×C4 with different original middle residual owner IDs in the two typed factor paths, or its three residual flags may not lie in CORE C. It then has ZERO physical preimages and is NOT produced; Branch A only needs the produced subset.

## 4. All NINE true B/B-overlap typed C4×C4 templates

For a fixed set of six genuine original flags with 3 unique anchors and three residual flags, their q-anchor + residual first factor pairs form a true C4 on four first-coordinate symbols. There are precisely **three** undirected Hamiltonian 4cycles in K4, equally for the true original line-r anchor + residual factor pairs. Therefore there are NINE possible ORIGINAL typed C4×C4 physical label patterns, even with completely correlated fixed f/g. Each C4 has one uniquely defined residual edge **opposite** its q/r anchor edge. This is the middle-owner ID along the residual P4. For any chosen first C4, exactly ONE of the three second C4 arrangements has the same middle-owner ID. Hence **three aligned** and **six unaligned** patterns.

The independent new source module generates all nine from ACTUAL W(3,2) incidence flags, including a genuine q--ell--p--r original projection, plus three actual other mutually distinct original source flags; it assigns exactly five designated distinct physical unordered factor pair labels on each side of the minimal alphabet and COMPLETES f and g to fully pair-injective maps on EVERY original point and line, not just the six selected flags. It enumerates from scratch both P4 factor graphs, independently builds all two-diagonal physical owner edges, then separately runs a complete PHYSICAL-FIRST directed 3walk census of the CORE. The source and physical count MUST agree **0 or 2** and the sixset count MUST agree **0 or 1**. At least one true W(3,4) positive and one unaligned negative are included, plus full W32 CORE, seed-plus CORE, and explicit deletion of the original middle projection anchor.

The resulting all-nine exact count is

| True original source template property | Number of C4×C4 types | Actual physical P3 count per six-ID set |
|---|---:|---:|
| Same middle ORIGINAL owner (aligned) | 3 | **2**, reversals |
| Different middle ORIGINAL owner (unaligned) | 6 | **0** |

This validates a necessary and sufficient original-source alignment criterion; not all original B/B-overlap motifs are counted as produced.

## 5. Independent INTEGER GF(5) positive-original-sixset audit (a distinct mathematical gate)

Issue #230 defines S_s as seven positive **GF(5)** original six-ID classes, not as arbitrary six source incidence flags satisfying a combinatorial pattern. Merely finding a literal pair of physical 3paths is insufficient unless the corresponding six source IDs indeed belong to a positive B/B-overlap GF5 class. Earlier \`hyp105_original_aligned_bbo_gf5_fourier_referee.py\` already proved a sharpened signed-mass statement. Here independently verify the SOURCE patterns against GF5 without importing that program or copying pretabulated flow vectors.

For any six actual original flags \(\Sigma=\{i_0,\ldots,i_5\}\), construct the 12 true pairwise source coordinate-sharing **edges among the SIX original flag columns**: six edges from the first typed factor symbol occurrences, six from the second typed factor. Every one of the six columns uses exactly TWO distinct first-coordinate and TWO distinct second-coordinate symbols. In all nine true templates each of the six physical symbols on each side appears exactly twice, hence this really is a 12-edge multigraph on six **distinct ORIGINAL column positions**, not a physical fake factor graph. For 10 balanced sign patterns with the first canonical column positive and two of the other five positive, count **nonzero** GF5 edge currents satisfying source conservation with signed demand.

The independent character-orthogonality oracle fixes one potential φ_0=0, sums over all 5^5 values of the other φ_j∈GF5, and uses the exact integer Fourier edge factor 4 if φ_u=φ_v, else −1. The four nonzero fifth-root Fourier coefficients agree by scaling φ↦tφ, t∈GF5*, so if b_j is the signed 4-demand and C_k is the corresponding integer phase bucket, each sign count is exactly

\[
\boxed{\frac{C_0-C_1}{5^5}\in\mathbb Z_{\ge0}.}\tag{BI-6}
\]

No complex arithmetic, floating phases or Monte Carlo is used. Sum over all TEN sign patterns. The expected independently verified exact totals for the nine-source-template family are

\[
\boxed{
\text{aligned produced BBo}=53838,\qquad
\text{unaligned nonproduced BBo}=53526.
}
\tag{BI-7}
\]

Both are **strictly positive**, including the entire produced subset, and 53838 is strictly stronger than issue #230's conservative global U_BB_overlap floor **51750**. These integer Fourier values are NOT claimed new in this slice; the added research acceptance is that **this exact newly independently produced source sixset** has the necessary positive-original class membership, rather than relying on a motif name alone. Note that the palette denominator is 51^6 and 53838/51^6 is a SIGNED EVENT MASS lower bound only; it does not turn the root unweighted \(\Omega(s^6)\) statement into a new strict ASET exponent.

## 6. Root proof-DAG compatibility and the exact remaining blocker

The new inverse does not depend on the value of HEAVY constant R, physical alphabet envelope A_H, core K or selected-moment bound L6/L4. Hence it is compatible with the most recent exact parent #779 constants:

- Fixed even H=32; true original GQ spectrum and full J book from #775.
- Improved combined no-clone HEAVY R=33281 and globally fixed T=ceil[(17/2) R^3 C0^3], unknown existential ordinary C6 graph constants C0,c0, from #778.
- Exact one-global-source-priority LOW selected expected moment \(\mathbb E m=W_C/2\) and L6=24+ceil(36ν_H T²), L4=q2²ceil_sqrt(ceil(ν_HL6))+19T from #779.
- GQ endpoint/full original A versus smaller paired CORE C proof and strictly sharper clean source mixed books from #780.
- The present source-only original sixset BI-1–BI-5 plus independent physical-first and GF5 BI-6/BI-7.

For the root, let \(\mathcal B_\mathrm{prod}(C)\) be the set of unordered six distinct original ID sets \(\Sigma\) satisfying BI-5, with all 3 residual IDs in C. The exact disjoint path partition and inverse imply

\[
\boxed{
W_3(H_C)=
I_{\mathrm{improper}}+
P_{\mathrm{missing}}+
P_{\mathrm{incident}}+
P_{\mathrm{endbad}}+
P_{\mathrm{deleted}}+
P_{\mathrm{fourblocker\ union}}+
2|\mathcal B_\mathrm{prod}(C)|.
}
\tag{BI-8}
\]

Every produced \(\Sigma\) belongs to the genuine original U_BB_overlap positive class by BI-7, and therefore \(|\mathcal B_\mathrm{prod}(C)|\le U_{BB,\mathrm{overlap}}\le S_s\). For root Z=empty the deleted anchor term vanishes identically. The global conditional LOW inequality thus translates to an **unweighted original source sixset** lower bound with no 2/6/12/6! ambiguity. The mathematical **local source-to-factor inverse gate** is settled, but the full seven-class global all-h proof is still restricted by the independent acceptance of all remaining source→physical bounds and their exact quantifiers; CI on small W32/W34 does not prove them. Do **NOT** set issue #230 to PROVED_A automatically.

**Next allowed scientific step:** one consolidated independently reviewed **original seven-class HEAVY/LOW proof-DAG** that checks EVERY prerequisite at its exact original hypotheses, external graph C6 theorem and fixed C0/c0 quantifiers, the latest original LOW improved L6/L4 plus full A/C books, original HEAVY D6 and original LOW BBo source sixsets, and the precise inequality S_s≥D6+BBo_prod with disjoint historical classes. The final deliverable should be either a complete publication-style proof with no inherited unsupported gate, or the FIRST explicitly isolated failed premise/counterexample. No merge, root issue closure or ASET exponent until then.

### Strict original D6 versus produced BBo disjointness

The inequality needed by the Branch A root is \(S_s\ge D_6+|\mathcal B_{\rm prod}|\), not just two unrelated motif estimates. This is valid because **every** original D6 six-incidence-ID set has six pairwise distinct original point factors and six distinct original line factors, while **every** produced BBo sixset has five distinct original point factors with one repeated p and five distinct original line factors with one repeated ell, with the repeated factors meeting in an ORIGINAL anchor (p,ell). These are mutually exclusive named-incidence factor-degree profiles, regardless of the physical pair labels, f/g correlation or GF5 sign pattern. The new independent \`original_sixset_factor_profile\` verifies that no generated or physically accepted BBo source sixset can have the necessary D6 profile; a TRUE original six-flag matching provides a nonvacuous disjoint-profile negative control. **This does not call every six-distinct-factor set a positive D6**; distinct factor degrees are only a necessary D6 condition.

Consequently, as long as the separately inherited actual D6 physical C6 inverse and ordinary graph supersaturation theorem hypotheses hold, the HEAVY D6 and LOW produced BBo bounds count distinct original source sixsets without double-charging the seven-class S_s. The finite original source checks and root dependency annotations verify this precise algebraic interface but do not automatically accept the entire upstream HEAVY/LOW all-h theorem.

## 7. Independent true source finite falsifiers and CI

The new standalone \`research/hyp105_original_bbo_alignment_dag_referee.py\` imports ONLY a genuine independently constructed W(3,2)/W(3,4) original symplectic incidence fixture; no existing BBo inverse, original six-ID root, GF5 Fourier/GF5 risk or historical physical path code is imported. All new source factor chains, their alignment, physical-first paths, true original q--ell--p--r GQ projection, unique original edge ownership, full original source pair label completion and GF5 character orthogonality are reimplemented independently. The paired CORE C can be seed-only, seed-plus, full W32 or empty; original Z may delete the middle projected anchor; every such alteration has a clear fail-closed expected result.

The 21-test independent workflow on GitHub-hosted Ubuntu24 / Python3.12 requires all nine *real-original* W32 source C4×C4 templates and their 3/6 alignment split, a positive TRUE W34 sixset, an unaligned W34 counterexample to naïve all-BBo production, explicit full W32 CORE physical-first path census, accepted exact original source six-ID 2-to-1 inverse, 10 original GF5 sign counts with integer Fourier total, strict failure of malformed six IDs/negative root promotion, and exact source/physical certificate artifact.

CI acceptance must be on the EXACT FINAL child HEAD, including specialist, INDEX and full Research SUCCESS; a preceding green ancestor or first intermediate run is not sufficient. Keep Draft, no merge or root close. This slice is a proof/referee of a local mathematical equivalence and a meaningful acceptance of the ORIGINAL BBo class, not a new root asymptotic exponent.
