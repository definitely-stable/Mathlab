# HYP-105 / issue #230 — Branch A external mathematical referee dossier and source-provenance gate

**ACCEPTANCE: OPEN_WITH_FORMAL_BLOCKER**

**Scope:** a reviewer-facing map of the claimed asymptotic **ORIGINAL six-incidence-ID** obstruction for the genuine symplectic generalized quadrangle \(W(3,2^h)\). This dossier is not a new proof, an endorsement of the proof, a proof-assistant output or a substitute for independent expert review. All scientific descendant PRs are Draft and must remain unmerged. The current manuscript integrates material from #652, #659, #672, #679, #684–#686, #688, #690, #695–#704. A qualified reviewer must inspect original proofs and reconcile references, not merely accept this dependency summary or CI.

**Upstream source:** [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). **Immediate immutable parent:** [Draft #704](https://github.com/definitely-stable/Mathlab/pull/704), HEAD \`6792e1f8460cd815cac66a957f9a640ca4d64b03\`. This new review slice is intentionally placed in a separate stacked Draft PR, without modifying this parent or main.

## 1. Exact question, quantifiers and objects

For **every** sufficiently large dyadic \(s=2^h\), let \(V=(s+1)(s^2+1)\), \(N=(s+1)V\), and \(a=\min\{j:\binom j2\ge V\}\). Take the **actual ORIGINAL** \(N\) incidence flags \((p,\ell)\) of \(W(3,s)\), with \(p\) a genuine original point incident with a genuine original line \(\ell\). Fix any pair of **complete separately globally pair-injective**, potentially **arbitrarily correlated** labelings \(f:p\mapsto\{x,z\}\), \(g:\ell\mapsto\{y,w\}\) into unordered physical alphabet pairs in \(\binom{[a]}2\).

Every original incidence flag generates exactly **two true physical diagonals** on the physical vertex set \([a]\times[a]\): \((x,y)-(z,w)\) and \((x,w)-(z,y)\). The physical graph is simple, and global separate pair-injectivity gives unique original edge owner IDs. **No cloned vertices, independently sampled edge-owners, synthetic incidences, f/g random completion or lost original IDs.**

Two object categories must never be conflated:

* \(\mathcal F_{\mathrm{full}}\): ALL original source flag IDs of genuine \(W(3,s)\), used for projective GQ source projections and source book counts, even after deleting flags from a graph.
* \(I\subseteq\mathcal F_{\mathrm{full}}\): the retained original-ID physical CORE, with two real diagonals per retained flag. The random **selector** produces a further whole-flag subset of \(I\), then the balanced heavy chunk is an **ordinary physical subgraph** and may retain only one of those diagonals.

Two counted source subfamilies are:

* \(D_6(f,g)\): genuine unordered sixsets of six DISTINCT original incidence IDs with six distinct original point IDs and line IDs and aligned named-source six-cycle pair adjacency.
* \(U_{BB,\mathrm{overlap}}(f,g)\): accepted genuine unordered sixsets of six DISTINCT original incidence IDs having a B/B source profile with repeated genuine point/line incident factors at one true ORIGINAL flag. The constructed three-walk image \(U_{\mathrm{produced}}\) is only a SUBCOUNT.

**Target, with all quantifiers explicit and in the right order:**

\[
\exists\,\delta>0,\ \exists\,h_0<\infty:\qquad
\forall h\ge h_0,\ \forall\text{ legal fixed }f,g,\
D_6(f,g)+U_{BB,\mathrm{overlap}}(f,g)\ge\delta\,(2^h)^6.
\tag{R0}
\]

Here \(h_0,\delta\) may depend on the EXISTENTIAL positive graph-theorem constants but **not** on \(h,f,g\). The original signed GF(5) risk \(R_3\) is a subsequent, strictly model-scoped **lower bound**, not an identity or a general ASET exponent statement.

## 2. Complete dependency graph — explicit source proofs and open review obligations

The new executable machine-readable claim graph (in \`research/hyp105_branch_a_external_referee_proof_obligation_gate.py\`) contains **13** necessary nodes in strict topological order and **8** original-source object or theorem-transfer gates. Its job is to detect unsupported claim promotion, missing evidence files or hidden cyclic citations, NOT to declare any mathematical lemma correct.

| Claim | Source-level content and principal evidence | Dependency / risk |
|---|---|---|
| **GQ** | Genuine \(W(3,s)\), original point/line pencils and unique nonincident \(q-\ell-p-r\) projective closure; \`HYP-105-UNIVERSAL-SEXTIC-OBSTRUCTION.md\` §§1,5–7 | ORIGINAL geometry, not an arbitrary incidence hypergraph; source input may need human verification |
| **BOOK** | Exact original pencil collision books \(M_f,M_g\), \(|E(H_{\mathrm{conflict}})|=M_f+M_g\), the uniform \(C_s\) and exact \(K=64\) pruning; \`HYP-105-EXACT-ORIGINAL-BOOK-CORE-BUDGET.md\` | Consecutive source flags with shared ORIGINAL point/line, not arbitrary pair intersection |
| **SS6** | Published Simonovits ordinary-graph \(C_6\) supersaturation, via Tao Jiang and Liana Yepremyan, *Supersaturation of even linear cycles in linear hypergraphs*, Combinatorics, Probability and Computing 29 (2020), 698–721; DOI [10.1017/S0963548320000206](https://doi.org/10.1017/S0963548320000206) | EXTERNAL published theorem, arbitrary finite simple ordinary graph, \(e(G)\ge C_{\mathrm{graph}}v(G)^{4/3}\); the constants are **positive existential and numerically unspecified** |
| **TAIL** | From heavy FULL physical vertex-degree edges to genuine original source conflict-free flags, two typed cuts, ordinary C6 and injective \(D_6\); \`HYP-105-FULL-PHYSICAL-DEGREE-TAIL.md\`, #697, #696 | Heavy edge threshold must refer to FULL H, not selected G or pruned H0; balanced chunk may be one-diagonal |
| **CORE** | If heavy case fails, delete ORIGINAL heavy owners and degree-\(>64\) conflicted original IDs, preserving two REAL diagonals/flag; \`HYP-105-EXACT-ORIGINAL-BOOK-CORE-BUDGET.md\` | Actual \(m(H_0)\ge s^4,\Delta(H_0)\le Ts\), original conflict cap K; separate full anchors from CORE |
| **D6** | Coordinate-rainbow physical C6 injects into unique genuine ORIGINAL D6 sixset; \`HYP-105-D6-CANONICAL-SOURCE-SIX-ID-INVERSE-REFEREE.md\`, #652/#699 | Need independent source named-edge cyclic order and **no row/column cherries + both typed cuts** |
| **SELECTOR** | Original ID priority local minima and whole-flag two bichromatic cuts, path marginals for r=2,3; \`HYP-105-SELECTOR-PATH-PAIR-COVARIANCE-REFEREE.md\`, #679/#695 | **Do NOT** assume distinct path survival events are independent or have positive covariance; transfer only via linearity + Jensen |
| **WALK6** | Sixth spectral walk moment vs ordinary six-cycles, bounded non-simple 6-walk correction; \`HYP-105-BIPARTITE-SIXWALK-MOBIUS-MOMENT-REFEREE.md\`, #686/#703 | True ordinary simple **bipartite** selected graph; not the external SS6 theorem |
| **ENDPOINT** | Exact proper physical three-walk count and FULL-source \(q-\ell-p-r\) endpoint defect; \`HYP-105-UNIVERSAL-SEXTIC-OBSTRUCTION.md\` §§5,7, #694 | Original source endpoint factor maps are COMPLETE, FULL projected anchors not necessarily CORE |
| **BLOCKER** | Four internal blocking positions and exact FULL/CORE mixed source contraction \(\Phi,\Psi,K_{pu},F_1,F_2\); \`HYP-105-MIXED-SOURCE-COLLINEARITY-ENERGY-REFEREE.md\`, #685/#701 | FULL \(R(p,y)\) vs CORE \(R_0(u,y)\), both exact source owner IDs; same \(f,g\) throughout |
| **BBO** | Only the THREE non-anchor true original flags belong to a physical three-edge path; full source contributes THREE anchor IDs, with exact 2-to-1 reversal fibers; \`HYP-105-BBO-ORIGINAL-CORE-CUBIC-POLYNOMIAL-REFEREE.md\`, #677/#694/#700 | \(T(Q)\subseteq I\) **does not** require all \(Q\subseteq I\); source six-ID profile cannot be replaced by projected surrogate |
| **ROOT** | Heavy/dense all-\(h\) global original six-ID disjunction; \`HYP-105-ORIGINAL-SELECTOR-SIXWALK-JOINT-ROOT-GATE.md\`, #702/#704 | Constants independent of h,f,g; external \(C,c\) positive unknown; test-only numeric substitutions not proof constants |
| **GF5** | Original 51 allowed GF(5) columns, all ten sign masks, finite exact \(D_6\)/B/B color current coefficients and disjoint original ID families; \`HYP-105-SHARP-TEN-SIGN-R3-FLOOR.md\`, #688 | Independent source ID sixset identity BEFORE multiplying sign contributions; scoped signed risk lower not unrestricted ASET claim |

The table maps evidence **available in the repository**, not external human-review acceptance. The code validates evidence-file presence and selected claim markers; such syntactic presence is not proof correctness.

## 3. One complete theorem trace with every typed boundary visible

1. **True original FULL geometry.** \(N=(s+1)^2(s^2+1)\) TRUE flags, physical \(2N\) real uniquely owned diagonals. Complete maps f,g remain fixed through all branches.
2. **Published ordinary graph input.** For unknown existential \(C_{\mathrm{graph}},c_{\mathrm{graph}}>0\), simple ordinary graphs \(F\) with \(e(F)\ge C_{\mathrm{graph}}v(F)^{4/3}\) have at least \(c_{\mathrm{graph}}(e(F)/v(F))^6\) copies of ordinary C6. This statement is not an explicit numerical bound without chosen valid actual constants.
3. **Heavy case.** For fixed \(\varepsilon=1787/4096\), source-conserving heavy-edge selection yields a witness-typed, physically balanced ordinary subgraph F. Its C6 cycles must map injectively to TRUE ORIGINAL D6 sixsets; heavy implies \(D_6\ge\alpha s^6\), where \(\alpha=c_{\rm graph}(\beta/32)^6\), \(\beta=5\varepsilon^2/(384+40\varepsilon)\), and the T used in the tail threshold is fixed from the SAME \(C_{\rm graph},\beta\).
4. **Dense case by actual contrapositive.** If \(D_6<\delta s^6\), \(\delta=\min(1/8,\alpha)\), the FULL physical heavy tail is \(<\varepsilon s^4\). ORIGINAL heavy-owner and conflict-pruning deletes actual source flags, leaving real \(H_0\) with \(m_0\ge s^4\), physical \(\Delta_0\le Ts\), original conflict max degree \(K=64\). Projection uses FULL W(3,s) even if flags were deleted.
5. **Original selector.** For any ONE fixed proper 2/3 physical path in H0 with genuine original flag owner IDs, source priorities and the two independent typed coloring cuts give \(\sigma_r\ge 4^{-r}(K+1)^{-r}\). DIFFERENT path survival events need not be independent: full second-moment transfer goes through Jensen.
6. **Selected physical sixth moment.** On true source-coherent selected G, every ordinary C6 lifts injectively to an ORIGINAL D6; \(\operatorname{tr}(A_G^6)\le24 C_6(G)+72m(G)\Delta(G)^2\). Then \(\|P_3(H_0)\|_F^2\le \sigma_3^{-2}L_6s^6\), \(L_6=24+288T^2\), with original \(s^6\) quantifiers intact.
7. **Proper path count.** Actual \(\mathbf1^\top A_0^3\mathbf1\ge s^6/2\), subtract \(\le84Ts^5\) coordinate-improper walks; subtract FULL-source missing/incident/end-bad endpoint weighted mass \(\le8\sigma_3^{-1}\sqrt{L_6}s^{11/2}\).
8. **Internal FULL/CORE blocks.** Original FULL \(R\), retained CORE \(R_0\), true point-collinearity energy, and exact incident subtraction \(\Psi\) bound FOUR positions by \(4\sqrt{B_0TL_4}s^{47/8}\), \(B_0=15\sqrt{65T}\). This is a bound for actual physical proper three-walks, not a synthetic path distribution.
9. **Original source six-ID B/B.** Every surviving proper unblocked directed length-three physical path gives SIX genuine original flag IDs: three owners from the actual CORE path and three FULL-source \(q-\ell-p-r\) anchors. For each accepted produced ORIGINAL sixset exactly TWO reverse-directed paths exist, so \(U_{BB,\mathrm{overlap}}\ge\frac12\,\#\mathrm{good\ unblocked\ directed\ paths}\).
10. **Exact all-h closure.** Together:
\[
2U_{BB,\mathrm{produced}}\ge
s^6/2-84Ts^5-
8\sigma_3^{-1}\sqrt{L_6}s^{11/2}-
4\sqrt{B_0TL_4}s^{47/8}.
\]
All normalized losses are \(O(s^{-1})+O(s^{-1/2})+O(s^{-1/8})\) for fixed T; the exact rational joint upper at a sufficiently large dyadic \(2^{h_0}\) is at most \(1/4\). Then \(U_{BB,\mathrm{produced}}\ge s^6/8\) in the dense branch. Heavy/dense yields (R0).
11. **Signed GF(5) only after original six-ID proof.** From disjoint ORIGINAL D6/BBo families, the exact 51-column ten-sign coefficients give the conditional \(R_3(f,g)\ge [\min(54162\delta,53526/8)/51^6]s^6\) within the specified original source-alteration model. The denominator and sign coefficient are not a general R2/R3 exponent or an ASET construction impossibility theorem.

## 4. Reviewer question bank — require a written proof or explicit counterexample

**R1 — Original source provenance.** Independently reconstruct \(W(3,s)\) flags, physical paired diagonal owners, and source point/line adjacency. Can an unordered physical pair label be inverted to a genuine original point or line uniquely under the **separate** global injections? Check every subgraph/selected edge has an original provenance ID. Confirm all quantified maps are fixed, including the adversarial correlated case.

**R2 — Heavy branch.** Does the true full physical heavy-edge tail give sufficiently many DISTINCT original owner flags, even when both diagonals or high-degree vertices overlap? Do source Caro–Wei independence and BOTH typed whole-flag cuts retain the claimed \(\beta s^4\) without replacing physical vertices, and does the resulting balanced ordinary F meet the **actual published** \(e(F)\ge C_{\rm graph}v(F)^{4/3}\)? Does each ordinary C6(F) inject to a different genuine ORIGINAL D6? A failure in any of these invalidates the heavy contrapositive.

**R3 — Core pruning.** Verify EXACT source book-to-conflict graph equality \(M_f+M_g\), the true original incidence cap \(C_s\), and the two ORIGINAL deletion operations on potentially overlapping IDs. Check \(m_0\ge s^4\), physical \(\Delta_0\le Ts\), and original conflict degree K=64 for every correlated map. Verify the original FULL source geometry is still accessible after pruning.

**R4 — Selector and moments.** Check the local-minimum joint probability integral for pairwise NONCONFLICTING source IDs, allowing overlapping external conflict neighborhoods, and the independent TWO typed coloring cuts along ONE proper path. Do **not** assume that different path-survival events are independent: #695 explicitly demonstrates negative covariance. Derive moment-transfer inequalities using **linearity of first moments + Jensen**. Independently check the sixth moment and fourth moment transfer constants, including graph isolates.

**R5 — FULL/CORE mixed blockers.** Examine every summation index in \(\Phi\), the incident defect \(\Psi\), and the squared-factor \(F_1,F_2\). Why are FULL \(R(p,y)\) and CORE \(R_0(u,y)\) used in different places? Check that the true GQ projection flag \((p,r)\) is available even if outside CORE and that \(B=\Phi-\Psi\) counts the intended unique source triples. Check the four internal positions separately, including reversal and point/line dualization, and the exponent \(47/8<6\).

**R6 — Original six-ID inverse.** Reconstruct the two separate named-ID factor graphs on SIX original source flags. For each produced B/B sixset, identify the UNIQUE repeated original point/line, all THREE original full anchors and the THREE other actual physical core edge owners; prove the physical directed three-path fiber is exactly two reversals. Critically: does the construction ever require the three anchor flags to be retained in CORE? It must **NOT**.

**R7 — Signed GF(5).** Check 51 permissible nonzero column patterns, all ten three-plus/three-minus sign masks, consistency of original six-ID factor graphs, coefficient enumeration and disjointness of D6 and B/B source sixsets. Distinguish exact finite arithmetic from the conditional global geometric \(s^6\) lower. Recheck sign weights separately instead of trusting historical round figures.

**R8 — Global quantifiers.** Does every constant \(\varepsilon,\beta,K,T,\delta,h_0\) have the correct dependence, and is T chosen once before all h and f,g? Do the heavy and dense cases cover all genuine maps at each sufficiently large dyadic h? Is \(h_0\) existential because real \(C_{\rm graph},c_{\rm graph}\) are numerically unknown? Are any finite W32/W34 tests, toy probability examples, or hypothetical \(C=c=1\) values misrepresented as general proofs? Does the signed conclusion stay inside the original GQ/GF5 model?

**Required reviewer output:** per R1–R8, record \`ACCEPT\`, \`MAJOR_REVISION\`, \`COUNTEREXAMPLE\` or \`NOT_REVIEWED\` with exact theorem line, source path, hypothesized failure/correction and which dependent conclusions are affected. A reviewer must be a real qualified independent mathematician; GitHub CI status is not a reviewer verdict.

## 5. External source boundary and reproducible arithmetic

The available published source is Jiang & Yepremyan (2020), DOI **10.1017/S0963548320000206**, whose abstract explicitly states the Simonovits ordinary-graph theorem for even cycles, including its \(r=2\) proof. At k=3 it supplies positive **existential** \(C_{\rm graph},c_{\rm graph}\), not their numerical values. **No fabricated numerical h0**: the \(h=684,682,668,666\) numbers from #704 are ONLY hypothetical \(C_{\rm graph}=c_{\rm graph}=1\) integer arithmetic regressions; they do not establish that either hypothetical value is valid for the published theorem. Likewise h values differing by one due only to rational root rounding are not new mathematical results.

**How to reproduce (GitHub-hosted, no local PC needed):**

1. Review this exact parent #704 head, the current separate Draft PR and each source proof hyperlink in §2, in original dependency order.
2. In GitHub Actions, the dedicated \`hyp105-branch-a-external-referee-proof-obligation-gate\` workflow runs \`python -m unittest discover -s research -p 'test_hyp105_branch_a_external_referee_proof_obligation_gate.py' -v\` on its exact head. Its output only certifies no MISSING EVIDENCE / missing typed source gate / contradictory machine-readable source assumptions.
3. Optionally run \`python research/hyp105_branch_a_external_referee_proof_obligation_gate.py\` on the checkout to produce a JSON list of the **13** claims, exact referenced files, external theorem status and the required topological dependency order. The output explicitly retains \`OPEN_WITH_FORMAL_BLOCKER\`, \`external_qualified_review_completed=false\`, and \`formal_proof_assistant_verification=false\`.
4. Inspect frozen historical specialist workflows and FULL Research/INDEX on the precise SHA for any mathematical claim. **A green workflow cannot certify R1–R8.**
5. Send the manuscript and this R1–R8 question bank to an independent qualified external referee, record their actual authored decision and resolve any counterexamples before changing repository acceptance.

## 6. Scientific STOP and acceptance criterion

The present evidence is sufficient to **prepare and audit a referee handoff**, not to assert the theorem has been independently peer-reviewed. The checker rejects the following invalid scope promotions: requiring all FULL source anchors to remain in CORE; treating distinct path indicators as independent; substituting fictitious published \(C_{\rm graph}=c_{\rm graph}=1\); promoting finite W32/W34 tests to an all-h proof; equating physical edges with original IDs without an injective owner map; invoking the ordinary-C6 theorem without its graph-density threshold; equating passing CI with qualified peer review; and extending a GQ/GF5 risk lower to an unrestricted ASET exponent conclusion.

**Release decision:** retain \`OPEN_WITH_FORMAL_BLOCKER\`. **DO NOT merge** any stacked scientific Draft PRs or close #230 based only on this dossier, exact-head green CI or successful syntax/graph-of-claims checking. Acceptance requires a real independent qualified human mathematical referee of the entire original all-\(h\) chain, documented findings and fixes of any major objections, and separate verification of final repository CI on the approved proof SHA. The source of truth must distinguish conditional theorem mathematics from the scientific acceptance gate.
