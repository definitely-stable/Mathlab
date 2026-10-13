# HYP-105 #230 — D6-AA4-B: coherent globally injective shared-factor completion fibers

**Stage:** RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER. Based strictly on AA4-A draft PR #433, exact pinned head \`ea49fd31fc7aad26c5fa987caa0494342e627b02\`, all four GitHub-hosted parent workflows SUCCESS. No merge or main changes. #230/#176/#169 remain OPEN.

## 1. Why source-stratified Fréchet transport in AA4-A still fails

AA4-A rigorously kept both six-position ORIGINAL point and line endpoint equality partitions, and fixed the one-sided physical 2-regular cardinalities in each source stratum. But its reduced binary transportation model independently re-pairs different sixsets. On the actual ORIGINAL W(3,2), both S68 and S72 have conditional Fréchet floors exactly zero, although their actual seven-GF5-positive original sixsets number 68 and 72 respectively. This is NOT an infinite valid correlated f,g counterexample; it exposes omitted **cross-Q coherence**.

D6-P–S have already established full seven-class ORIGINAL right-label cylinders, one-right swap boundaries, commuting right/right Hessians, and oriented three-factor cycle identities. AA4-B intentionally **does not** duplicate those or declare a right-swap local optimum to be a global proof. Here the additional mathematical object is a whole **shared-factor injection-completion fiber** and its nonnegative *coherence gap*, defined by a globally common label choice across ALL touched ORIGINAL sixsets.

## 2. Exact ALL-h conditional completion theorem

Fix s=2^h (h≥1) and the actual ORIGINAL W(3,s). Fix a complete globally injective left original point map f and fix the right g restricted to all ORIGINAL line identities outside a finite block B (|B|=b). Define the **available physical pair labels**

\[
A_B = E(K_a)\setminus g(L\setminus B),\quad |A_B|=\binom a2 - (V-b)=m+b,
\]
where \(V=(s+1)(s^2+1)\), \(a=\min\{a:\binom a2\ge V\}\), \(m=\binom a2 -V\).

The legal completion set \(\mathcal J_B\) consists of all injective functions \(j:B\to A_B\). It has cardinality
\[
|\mathcal J_B|=(m+b)_{\underline b}.
\]
Every such completion yields one **complete globally injective** right label map \(g_j\). No physical edge label may be reused within the ORIGINAL right type; point and line images are separate typed injections. One \(g_j(\ell)\) is used **identically in every sixset containing the ORIGINAL line \(\ell\)**. This is the precise missing coupling in AA4-A.

Fix the FULL set \(\mathcal Q_f\) of distinct-ORIGINAL-incidence sixsets whose left physical projection is six-coordinate 2-regular, and index its correct original-incidence-position-preserving right cylinders \(\tau\) with multiplicities \(m_f(\tau)\) (D6-P). Let \(\chi_\tau(g_j)\) be the one-of-seven accepted GF(5) necessary class or none, and let \(w_\tau(j)\in\{0,1\}\) be its indicator. Define the weighted version \(v_\tau(j)\) using the already certified seven fixed GF(5) floor coefficients 5643,45600,45600,43320,49050,51750,45010.

Split cylinders into those whose ORIGINAL right factor support intersects B (affected), and its complement (fixed). Let F0 be the exact fixed part of the seven-count. The exact **conditional global fiber minimum** is
\[
\min_{j\in\mathcal J_B} S(f,g_j)
 = F_0 + \min_{j\in\mathcal J_B}\sum_{\tau\in A(B)}m_f(\tau) w_\tau(j).
\]
Nothing is optimized Q by Q in this expression. The corresponding selected necessary GF(5) numerator identity replaces w with v.

By elementary min–sum inequality (valid for any finite legal fiber and any nonnegative or signed integer costs),
\[
\boxed{\ \underbrace{\min_j\sum_{\tau\in A(B)} m_f(\tau)w_\tau(j)}_{\text{coherent shared-label fiber}}
\ge \underbrace{\sum_{\tau\in A(B)}m_f(\tau)\min_j w_\tau(j)}_{\text{independent original-cylinder choices}}\ }.
\]
Define the exact **fiber coherence gap** \(\Gamma_B\) as left minus right; \(\Gamma_B\ge0\). An identical formula applies to the selected fixed-GF(5)-weight numerator. Strict \(\Gamma_B>0\) is a **certificate that independently minimizing all affected original Q cylinders violates the requirement of one common globally injective physical assignment on B**, even though every considered candidate completion individually respects physical capacity.

This statement is all-h and includes arbitrary correlations between the original f,g. It is **conditional on the labels outside B and on f**, NOT an unconditional lower bound \(\inf_{f,g} S_s\ge c s^6\). Existing D6-P cylinders are used solely to compute the exact tag; no new full-51-palette flow proof is claimed.

## 3. Independent finite positive hitting-cover certificate (W32 only)

For W(3,2), V=15 and K=C(6,2)=15; m=0. Freezing all but four ORIGINAL right line labels leaves exactly \(4!=24\) globally legal completions, regardless of scheme. Fix actual ORIGINAL S68 or S72 and a *predeclared* ORIGINAL right block:
- S68: B=(0,1,2,3)
- S72: B=(1,7,9,12)

For every affected ORIGINAL right cylinder record its 24-bit **positivity mask**: bit j is one iff that cylinder is in one of seven accepted classes in completion j. The exact bitwise OR of masks is the set of completions for which some affected ORIGINAL sixset is seven-positive. If the OR equals \((1<<24)-1\), then every legal completion has a positive affected original sixset. Produce a **deterministic greedy finite COVER** consisting of selected actual ORIGINAL right cylinder signatures whose union of masks covers all 24 completions. No optimal-cardinality claim is made. Every selected cylinder has positive integer ORIGINAL sixset multiplicity; their full original sixset existence follows from the exact compiler. A positive cover is a *finite pinned-fiber positive witness* valid only under that exact f and those 11 frozen right factor labels, NOT a universal all-h theorem.

Record for each true fiber:
- Complete 24 authentic globally injective right pair-label maps (S and fixed GF5 selected numerator, all seven class counts);
- exact globally coherent affected-only minimum and weighted minimum;
- sum of each cylinder's independently attainable minimum;
- coherence gaps (nonnegative by construction, **strictness only if measured**);
- a finite explicit 24-bit cover if the minimum affected positive count is strictly >0;
- independent legacy full ORIGINAL six-incidence oracle comparisons on multiple completed global maps.

No random sampling, SA/SOS solver, unpinned geometry, or full \(R_3\) is used for any certificate.

## 4. Exact scope, remaining blocker and next step

This slice enforces real global injectivity and shared physical labels on the **single frozen block**, and counts all its affected original sixsets jointly. It avoids AA4-A's invalid per-Q choice. However, it does not resolve full global assignment optimization because f and the other V−b ORIGINAL right factor labels are pinned and the physical capacity is not simultaneously optimized over every original type.

Positive \(\Gamma_B\) or a 24-completion hitting cover demonstrates a genuine obstruction to the particular *fiberwise independent-min* relaxation. Neither is a lower \(c s^6\) valid for ALL f,g or all s. The next gate would need a **uniform combinatorial lower on these fiber certificates across every admissible outside assignment**, or a rigorous global inference combining overlapping fiber certificates. Avoid assuming one finite pinned fiber result transfers to arbitrary other label maps.

STOP if the coherent gap is zero: report that no strict improvement was established for that specific block and choose another mathematically justified constraint. STOP if full Research or independent legacy oracle disagrees. Do not close Branch A/B.

## CI / novelty controls

A dedicated GitHub-hosted workflow must (i) independently validate global physical injection in each of all 24 completions; (ii) compare actual historical seven_census on multiple different globally assigned completed maps; (iii) verify the exact min/sum inequalities and recompute the source-cylinder cover; (iv) run the heavier two-scheme finite 24-completion machine-report exactly once; (v) retain no future claim of all-h positive GF5 S. Shared INDEX, Proof Audit and Research must pass on the same exact final PR head. Independent mathematical review remains required.

This is a finite conditional exact constraint and computable obstruction to a stated relaxation, not a claimed novel general combinatorial theorem or result on total GF(5) R3.
