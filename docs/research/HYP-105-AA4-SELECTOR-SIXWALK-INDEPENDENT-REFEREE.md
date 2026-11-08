# HYP-105 / #230 — AA4-SEL6WALK: independent source selector and selected C6/six-walk referee

**Scientific scope:** Draft stacked strictly on frozen PR #744 HEAD 1c153e9d8b06b256ab7d8cf687ac876699d48105. Genuine ORIGINAL symplectic W(3,2^h), named point-line incidence flags, separately globally pair-injective fixed arbitrarily correlated f/g and arbitrary ORIGINAL deleted source IDs Z. No parent/main changes, merge or root closure; root remains OPEN_WITH_FORMAL_BLOCKER. This work independently reviews TWO particularly sensitive cited mathematical interfaces from #743/#744. It does not pretend to mechanically prove all 18 previous all-h source lemmas, the external graph theorem or an ASET exponent.

## 1. Exact original-source priority and two-coordinate-cut path survival

Let C be the actual retained ORIGINAL paired core and J_C its genuine original point/line pencil-conflict graph. Its maximum degree is K=64 after the FULL original source-J pruning. Let r∈{2,3} and let γ=(v0,...,vr) be a coordinate-proper physical r-path in C; all r+1 first physical symbols and all r+1 second physical symbols are distinct. Every edge has one true named ORIGINAL flag owner ui=(pi,ℓi). The r owners have pairwise distinct original point indices and separately distinct original line indices: a repeated point would repeat its globally injected f physical symbol pair on different path edges, contradicting coordinate-properness; similarly for g. Thus the source owners are pairwise NONCONFLICTING in J_C, without probabilistic assumptions on f/g.

Define the original closed source J-neighborhood union Uγ=∪i({ui}∪NJ(ui)), b=|Uγ|≤r(K+1). Draw ONE globally uniform priority ordering of the retained original CORE. A sufficient event for retaining ALL r true owners is that they are the FIRST r elements of Uγ in any order. Among the b! relative priority permutations exactly r!(b−r)! have this property, so the exact probability of the sufficient event is

\[
\boxed{\Pr(E_{\rm first-r})=\binom br^{-1}.}
\tag{SP-1}
\]

The actual source-priority survival event is the conjunction ui preceding every one of its genuine source-conflict neighbors. It can be more likely than (SP-1). The new independent referee constructs the precedence DAG on actual ORIGINAL IDs in Uγ and computes the EXACT number of its linear extensions with integer subset DP:

\[
D(0)=1;\quad
D(M\cup\{j\})\mathrel{+}=D(M)
\quad\text{iff all predecessors of j already occur in M}.
\tag{SP-2}
\]

Dividing the exact count by b! gives the genuine local probability for ONE globally shared source priority order. Finite W32/W34 source tests with r=2/3 and b≤20 independently confirm it is at least (SP-1). The proof (SP-1) is for ALL h, not an extrapolation.

For the left physical color cut, exactly TWO alternating binary assignments on the r+1 distinct first-coordinate symbols make ALL r consecutive factor edges bichromatic, so its probability is 2^(-r). Independently the true right physical color cut also has probability 2^(-r). There are EXACTLY FOUR acceptable two-factor assignments among 2^(2(r+1)); the new source tests enumerate all of them, r=2 and r=3. Source priorities and the two cut alphabets are independent, but retention of DIFFERENT paths is not claimed independent. Therefore for every genuine original coordinate-proper r-path

\[
\boxed{
\Pr(\gamma\text{ survives the true source priority and BOTH real cuts})
\ge\frac1{4^r\binom br}
\ge\frac1{4^r\binom{r(K+1)}r}
=:\sigma_r.
}
\tag{SP-3}
\]

Both real opposite diagonals of each retained ORIGINAL flag remain together. No source re-labeling or physical edge cloning.

For each ordered physical endpoint pair (u,v), let Pr(u,v) count proper original CORE r-paths, and Xω,r(u,v) count paths retained by the SAME global selector ω. Exact expectation linearity and Jensen, with no path independence, give

\[
\boxed{
\sigma_r^2\|P_r\|_F^2
\le\|\mathbb EX_{\omega,r}\|_F^2
\le\mathbb E\|X_{\omega,r}\|_F^2
\le\mathbb E\operatorname{tr}(A_{G_\omega}^{2r}).
}
\tag{SP-4}
\]

This directly validates the all-order selector/Jensen proof interface in #738.

## 2. Critical selected BIPARTITE graph sixth-walk theorem

Every retained source flag has its original physical f-pair bichromatic under the FIRST cut, so the selected physical graph Gω is UNDIRECTED, simple, and BIPARTITE, irrespective of whether the uncut CORE itself is bipartite. The second cut is needed for complete six-coordinate properness, not for this abstract 6-walk inequality.

For any finite ordinary simple BIPARTITE graph G, a closed directed 6walk without an immediate reversal must be a genuine simple 6-cycle. Otherwise any repeated vertex yields a shorter closed subwalk: in a simple bipartite graph it must have even length ≥2; a 2-return is already an immediate reversal and any 4-return within a sixwalk leaves a closed 2-return. Every unoriented simple C6 contributes EXACTLY 12 rooted oriented closed sixwalks.

Remove a marked immediate reversal u→w→u from a nonsimple closed sixwalk; one obtains a closed directed 4walk, a choice of at most six positions and at most Δ choices for its deleted intermediate vertex. Counting by this explicit many-to-one injection gives

\[
\boxed{
\operatorname{tr}(A_G^6)\le
12C_6(G)+6\Delta\operatorname{tr}(A_G^4).
}
\tag{SW-1}
\]

For real symmetric A, spectral Cauchy yields [tr(A⁴)]²≤tr(A²)tr(A⁶)=2m tr(A⁶). Young 6Δ√(2mX)≤X/2+36mΔ² for X=tr(A⁶), hence

\[
\boxed{
\operatorname{tr}(A_G^6)\le24C_6(G)+72m\Delta^2.
}
\tag{SW-2}
\]

This proves the independent all-graph lemma required to control the TRUE selected physical C6 sixth moment. Crucial negative control: the NONBIPARTITE triangle has a closed sixwalk that traverses the triangle twice with NO immediate reversal, so the combinatorial backtrack classification is false for general nonbipartite uncut source cores. The separate original \(\Delta A_C^2-A_C^3\succeq0\) spectral source lemma #740 does work on such cores and is not being conflated with (SW-1).

### Independent exhaustive finite graph falsification

The new program independently enumerates ALL 64 bipartite subgraphs of K2,3 and ALL 512 bipartite subgraphs of K3,3 (including isolates), computes integer adjacency powers A⁴, A⁶, counts unoriented simple C6 by independent DFS quotienting rotations and reversals, and checks (SW-1),(SW-2) for EVERY graph. Full K3,3 has exactly SIX unoriented C6, trace A4=162, trace A6=1458. The triangle is an explicit NEGATIVE-SCOPE witness, not a counterexample to the correct bipartite statement.

### Genuine original W34 selected D6 physical witnesses

Three independent positive seeds from true W(3,4): lex six source IDs [111,116,203,224,383,412] and [129,146,224,366,412,417], and reverse-line [47,224,229,273,300,355]. The standalone referee reconstructs complete genuine original source flags and pair-injected labels, independent source J, exactly TWO real physical diagonals for each of the SIX original flags, and separately verifies source point and line owners are all distinct and conflict-free. It enumerates real physical simple unoriented C6s by DFS: exactly ONE physical cycle per seed is coordinate-proper in both factors and has all SIX named ORIGINAL owners. Literal alternating physical two-factor bit assignments on its vertices make all six original source flags bichromatic and preserve both diagonals; direct integer A4/A6 traces verify (SW-1),(SW-2) with nonzero true C6.

## 3. Scope and scientific acceptance matrix

| Predecessor interface | Current independent mathematical verdict |
|---|---|
| Proper r=2/3 physical source path has r distinct pairwise nonconflicting ORIGINAL flag owners | PROVED all h via global f/g pair-injection and physical coordinate-properness |
| Original priority first-r sufficient event | PROVED all h via exact b! count, additional exact local linear-extension DP |
| Two true physical-coordinate cut survival 4^(-r) | PROVED all h via alternating chains and exact exhaustive bit counting |
| Jensen proper source-path energy transfer | PROVED all h via linearity and convexity, no path independence |
| Selected ordinary bipartite sixwalk SW-1 and SW-2 | PROVED all finite graphs; full K33 exhaustive independent verification |
| Source proper physical C6 to six ORIGINAL D6 owner IDs | Independent true W34 finite checks; existing all-h source inverse manuscript #734 still required |
| Remaining full original HEAVY/LOW point/line SRG, mixed books and proper P3/BBo six-ID inverse | NOT certified merely by these tests; mathematical review remains |
| Root Branch A PROVED_A and general ASET exponent | NOT promoted; root scientific governance remains separate |

External ordinary graph C6 supersaturation used elsewhere in the proof (Jiang–Yepremyan 2020 DOI https://doi.org/10.1017/S0963548320000206) is indeed existential with absolute positive graph constants and copies lower c(e/v)^6; actual C0/c0 numerical values are not established by the paper.

## 4. Reproducible repository artifacts

Independent exact priority/source/physical C6 program: research/hyp105_original_selector_sixwalk_independent_referee.py. Independent 12 adversarial positive/negative tests: research/test_hyp105_original_selector_sixwalk_independent_referee.py. Standalone Ubuntu-24.04 Python 3.12 fail-closed unique JSON GitHub-hosted workflow, plus INDEX and full Research on the SAME final HEAD. Only trusted original symplectic source and complete physical pair-label fixture constructors are imported in the new main program; NO earlier selector/energy/source-inverse/root proof implementation is imported. Finite W32/W34 and K33 census checks do NOT replace all-h mathematical proofs in §§1–2.

No merge, no main changes, no automatic issue close or ASET exponent. **Next independent math review:** true full original GQ projection and mixed allowed-A vs paired-CORE C internal-book source injection, with explicit all-h negative-scope tests.
