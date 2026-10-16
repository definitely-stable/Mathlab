# HYP-105 / issue #230 — AA4-AW: nonlinear universal swap-sign rigidity on complete ORIGINAL label fibers

**Status:** RESEARCH-ONLY mathematical method theorem and genuine-original finite evidence, not a proof of #230 Branch A/B/C. Strict Draft descendant of [AA4-AV rank-7 PR #555](https://github.com/definitely-stable/Mathlab/pull/555), pinned parent full globally injected source-model SHA 0e69f6445afd98a79f7c29e2e5dd9a9657730806. Scope is every genuine W(3,s), s=2^h, h>=1, with six DISTINCT actual original incidence flag IDs identical on both physical projections, one complete globally injected original point assignment f and line assignment g, and ALL SEVEN historical accepted GF5 tags.

This slice is **NOT** a duplicate of the parallel AA4-AW two-port-marginal PR #556: here we classify the *entire nonlinear function space* on a fixed globally injected original source LINE-image permutation fiber and derive a gauge obstruction to ANY nonconstant invariant nonlinear seven-tag objective satisfying an everywhere-one-signed mixed second finite difference.

## 1. Why PR #555 fixed-linear no-go is insufficient

Previous [#555](https://github.com/definitely-stable/Mathlab/pull/555) exhibited seven genuine ORIGINAL W32 classwise mixed Hessian vectors spanning the full historical seven-tag space over the rational numbers, with exact pivot determinant -2650. Thus NO nonzero FIXED REAL LINEAR coefficient combination of the seven original accepted class counts has a universally positive or negative Hessian under any disjoint two original LINE-factor-image swaps. However adaptive nonlinear objectives F(f,g)=Phi(S_D6(f,g),...,S_BB-disjoint(f,g)) were not covered by that finite rank test.

The exact all-h sign anti-involution for two disjoint entire-original-LINE-factor swaps sigma,tau also proved in #555:
\[
H_{\sigma,\tau}F(g^\sigma)=-H_{\sigma,\tau}F(g)
\]
for ANY scalar F, not necessarily a linear sum. Therefore a universal mixed-Hessian sign law on a complete original LINE-image permutation fiber implies *every* disjoint mixed Hessian vanishes. The novel model-level remaining step is to classify the **complete kernel** of all those finite-difference constraints.

## 2. ALL-n classification theorem: zero disjoint-transposition Hessian iff additive assignment

**Theorem.** Let I and E be two arbitrary finite sets of the SAME cardinality n>=4; in the true source application I is the COMPLETE ORIGINAL symplectic GQ LINE factor set (|I|=V=(s+1)(s²+1)>=15), and E is one fixed actual globally occupied physical pair-edge image set E_g⊂E(K_a), |E_g|=V. Let Bij(I,E) be the set of ALL complete globally injective original LINE-image assignments with precisely that same physical image support. No original source incidence edges or point-label images are changed by the formal LINE permutations.

For ANY real-valued function F:Bij(I,E)→R, the following are EXACTLY equivalent:

(a) For EVERY complete global g∈Bij(I,E) and EVERY TWO DISJOINT transpositions sigma=(i,j), tau=(k,l) of four different actual original LINE factor IDs, the mixed second finite difference

\[
H_{\sigma,\tau}F(g)
=F(g^{\sigma\tau})-F(g^\sigma)-F(g^\tau)+F(g)=0.
\]

(b) There exist c∈R and numbers A_{i,e}∈R indexed by actual original source LINE factors i and occupied physical pair edges e∈E such that

\[
\boxed{F(g)=c+\sum_{i\in I}A_{i,g(i)}}
\]
for EVERY g in the entire complete right permutation fiber.

This is a finite permutation group / linear assignment structural theorem. Its abstract ingredients are classical algebra and are **NOT claimed as a novel general-purpose combinatorics theorem**. Its new value here is the exact restriction it imposes on hypothetical nonlinear seven-GF5 compensating functions over one full original GQ permutation fiber.

### Exact elementary proof, with no group representation prior assumption

**Step 1 — two-coordinate locality of a swap difference.** For distinct actual source LINE factor IDs i,j, define Δ_ij F(g)=F(g^(ij))−F(g). By (a), Δ_ij is unchanged if g is modified by swapping the physical image labels of any two DIFFERENT original LINE IDs k,l outside {i,j}. Transpositions on the remaining n−2 source IDs generate the FULL permutation group of those complementary positions. Hence Δ_ij is completely determined by the TWO current physical pair images a=g(i), b=g(j), and by the original positions i,j, not by the other n−2 assignments. Denote this well-defined quantity by D_ij(a,b). It obeys D_ij(b,a)=−D_ij(a,b) and, with the oriented index order reversed, D_ji(a,b)=−D_ij(a,b). This step requires n>=4 to have disjoint complement transpositions.

**Step 2 — braid relation kills value-side three-cocycles.** For three DISTINCT actual original LINE indices i,j,k and three DISTINCT currently assigned physical edges a,b,c, apply the basic symmetric group relation (ij)(jk)(ij)=(jk)(ij)(jk) to the same complete original g. Its two three-swap paths yield
\[
D_{ij}(a,b)+D_{jk}(a,c)+D_{ij}(b,c)
=D_{jk}(b,c)+D_{ij}(a,c)+D_{jk}(a,b).
\]
Define the oriented value-side curl
\[
C_{ij}(a,b,c)
=D_{ij}(a,b)+D_{ij}(b,c)-D_{ij}(a,c).
\]
The braid identity implies C_ij=C_jk for every triple of DISTINCT source indices. Since D_ji(a,b)=−D_ij(a,b), we also have C_ji=−C_ij. Choose FOUR distinct actual original source positions i,j,k,l. From triples (i,j,k),(j,k,l), (i,j,l), (j,l,k) we obtain
\[
C_{ij}=C_{jk}=C_{kl},\qquad
C_{ij}=C_{jl}=C_{lk}=-C_{kl}.
\]
Therefore **2C_ij=0**, so C_ij=0 for REAL-valued F. This crucial FOUR-source-index step uses no large-h artificial source GQ and explains the threshold n>=4.

**Step 3 — construct potential differences over physical labels.** Fix an occupied physical right edge e0∈E, and define for every oriented original source pair i,j
\[
u_{ij}(e)=D_{ij}(e_0,e).
\]
Curl zero gives the exact representation
\[
D_{ij}(a,b)=u_{ij}(b)-u_{ij}(a).
\]
For any three distinct original source indices i,j,k, compare the TWO legal transposition paths (ij) followed by (jk), and (jk) followed by (ik), from images (a,b,c) to the identical final triple (b,c,a). This yields
\[
D_{ij}(a,b)+D_{jk}(a,c)
=D_{jk}(b,c)+D_{ik}(a,b).
\]
With the value-side gradient identity above and any auxiliary c different from a,b, this simplifies to
\[
D_{ij}(a,b)+D_{jk}(a,b)=D_{ik}(a,b).
\]
Fix one actual original reference source LINE factor r. Let A_r(e)=0 and A_i(e)=u_{ir}(e) for i!=r. Then
\[
D_{ij}(a,b)
=[A_i(b)-A_i(a)]-[A_j(b)-A_j(a)]
\]
for every legal source pair and physical pair images.

**Step 4 — integrate the first differences globally.** The explicit assignment function G(g)=sum_i A_i(g(i)) has exactly the SAME one-swap difference Δ_ij as F at every complete global g. Thus F−G is invariant under every source LINE factor pair-image transposition. Since these transpositions connect ALL bijections with the prescribed physical support E, F−G is a constant c on that whole fiber. This proves (b). Conversely, swapping four different source factors in two disjoint transpositions affects DISJOINT summands of an assignment function; their mixed second difference vanishes identically, proving (a).

**Dimension corollary.** The assignment function subspace on n! full injection states has real dimension exactly
\[
\boxed{1+(n-1)^2}.
\]
Indeed it is the image of all n×n coefficient matrices under the permutation-matrix inner product, and row-constant and column-constant coefficient shifts are the familiar 2n−1 dimensional null relations between the n² indicator matrix coordinates. Thus its dimension is n²−(2n−1)=1+(n−1)² (the explicit intercept can be absorbed as a constant assignment matrix).

## 3. Any universal one-signed mixed Hessian forces assignment

By the all-h complete GLOBAL original swap anti-involution H(g^σ)=−H(g), a pointwise condition H_{σ,τ}F(g)>=0 on ALL g and ALL disjoint pairs requires H≡0 (similarly <=0). By the previous theorem, an arbitrary **nonlinear** statistic F on this original right support fiber can have a universal sign only if it is functionally assignment-additive in its current original LINE-factor physical pair-image labels. This is strictly stronger than the seven-fixed-coefficient rank no-go in #555. It is an IF-AND-ONLY-IF structure theorem, not a statement that every nonlinear function necessarily has a nonzero Hessian.

## 4. New gauge-rigidity theorem: one-sign + coordinate symmetry ⇒ F constant on TRUE W32

Suppose a group G of permutations of the physical coordinate alphabet induces automorphisms of the occupied physical right edge-image support E, acting TRANSITIVELY on all edges of E, and the scalar F is invariant under simultaneous renaming of all RIGHT-side physical coordinates on its entire complete globally injected g (while keeping the ORIGINAL source geometry and fixed point-side map f unchanged):
\[
F(\gamma\circ g)=F(g)\qquad(\gamma\in G).
\]

If F has a universally one-signed disjoint-two-source-LINE-image-swap Hessian, it is assignment-additive as above. Average this assignment representation over the finite transitive right-coordinate gauge group:
\[
F(g)
=c+\sum_{i\in I}{1\over|G|}
\sum_{\gamma\in G} A_{i,\gamma(g(i))}
=c+\sum_{i\in I}{1\over|E|}
\sum_{e\in E}A_{i,e}.
\]
This is **INDEPENDENT OF g** on its entire fixed occupied right image support fiber. There is no need to assume that F itself is linear in the original seven class counts.

In the genuine original W(3,2), **V=15, a=6, physical right image support E_g=E(K_6)** for EVERY full globally injected original source LINE map; G=S_6 acts transitively on all physical pair edges. Every historical seven positive GF5 class count and every nonlinear real expression Phi of the resulting seven-component motif count vector is invariant under independent global physical RIGHT coordinate renaming. Hence:

\[
\boxed{
\text{For fixed genuine ORIGINAL W32 point map }f,\;
\text{a nonlinear seven-tag functional }\Phi(S_1,\ldots,S_7)
\text{ with universal one-sign disjoint-swap Hessian
must be CONSTANT across every complete global right }g.
}
\]

Equivalently, whenever one can exhibit two actually globally injected original W32 right maps g,g' on this SAME fixed f with distinct nonlinear scalar Phi values, an everywhere-positive or everywhere-negative mixed swap Hessian law for Phi is mathematically IMPOSSIBLE, and actual legal opposite-signed Hessians MUST exist on its full right permutation fiber. This is an exact **method limitation**, and it does NOT prove that the seven-class counts themselves are constant (indeed they are not in the finite original examples), nor does it prove or refute the desired every-fixed-(f,g) S>=c*s6 universal min.

For true s>=4, the minimal global physical E(K_a) has m holes which may have a nontransitive or even trivial physical graph automorphism group. The theorem still characterizes zero Hessian as an assignment function for every occupied E, but the *gauge-implies-constant* corollary only applies if the actual **occupied physical edge support** admits a transitive physical coordinate automorphism group. We do NOT infer an all-h constant F in nononto palettes.

## 5. Independent falsifiers, exact original model and limitations

Files:
- research/hyp105_issue230_d6aa4aw_nonlinear_swap_rigidity.py — proof-scope exact validators, full permutation kernel reduction, small physical gauge oracle, actual ORIGINAL W32 nonlinear seven GF5 complete 4-global-map scorer.
- research/test_hyp105_issue230_d6aa4aw_nonlinear_swap_rigidity.py — independent 7 test groups with abstract S4/S5 (NOT fake original GQ), true original W32/W34, gauge invariance and class nonlinearity.
- This proof.
- Hosted workflow .github/workflows/hyp105-issue230-aa4aw-nonlinear-swap-rigidity.yml.

Independent finite S4/S5 **FULL permutations** and **EVERY disjoint source-swap pair at EVERY permutation** give a modular finite-field linear-system Hessian rank, to compare against independently computed assignment coefficient image rank. Expected exact checks:
- n=4: 24 full bijections, three disjoint swap pairs per bijection, 72 equations, Hessian matrix rank 14, kernel dimension **10** = 1+(4−1)^2.
- n=5: 120 full bijections, fifteen disjoint swap pairs, 1800 equations, rank 103, kernel dimension **17** =1+(5−1)^2.

The fully independent abstract physical K4 edge-transitive gauge example checks that the average of any assignment potential over all 24 S4 coordinate relabels is independent of the current assignment; this example is NOT called a genuine original W(3,s).

Actual original W32/K6 controls use 45 TRUE source symplectic incidence IDs, one complete globally injected original point f held FIXED, four globally legal complete line maps on all 15 real original LINE factor IDs, ALL 62,370 actual six-original-ID left-valid candidates per global map, the historical original seven accepted class classifier and its fixed GF5 51-palette necessary numerator weights. Their unweighted seven S, historical selected GF5 weighted numerator and **nonlinear squared-total S and sum of squared individual class counts** are independently rescored and their legal signed double-swap inversions verified. An actual K6 independent physical right coordinate permutation is also checked on original seven counts: no per-Q independent redraw and all historical tags remain unchanged.

This exact classification is closely related to classical permutation-matrix linear assignment statistics and interaction-free ANOVA ideas. A limited literature search found linear optimization over permutation groups and related representations, but NOT an independently verified novelty boundary for this precise disjoint-Hessian if-and-only-if characterization. No publication or original general permutation group theorem novelty is claimed. Prior project work #415/#417/#493/#497 had classwise exact local/mixed swap identities; #555 supplied one-signed involution and a FIXED-LINEAR seven-dim rank-7 witness. The new result is the **complete nonlinearly applicable permutation-fiber rigidity characterization**, plus its **TRUE ORIGINAL W32 transitive gauge corollary**.

**Non-implications:** No positive universal seven-GF5 lower for every fixed original f,g; no infinite correlated original source counterfamily; no source-GQ Hall survival rate; no full R3 or ASET exponent. Root issue #230 stays OPEN_WITH_FORMAL_BLOCKER. CI correctness is not independent human mathematical acceptance. No scientific Draft merge or accepted canonical RCP claim promotion without rigorous independent review. Next live mathematical front should prioritize the genuine all-map physical two-port minority-product / original 3×3 forest Hall density route of sibling PR #556 rather than another broad sign-of-Hessian construction.


## 6. First exact hosted evidence — FULL original W32 nonlinear four-state witness

The first exact source/test HEAD specialized [GitHub-hosted run #38878604052](https://github.com/definitely-stable/Mathlab/actions/runs/38878604052) completed **TWO JOBS SUCCESS**, all SEVEN independent mathematical unit groups PASS. The independent full-permutation constraints give:

| Finite abstract permutation group (NOT an invented original GQ) | Entire S_n states | All disjoint-swap pairs per state | Rank over F_1009 | Kernel dimension | Assignment image dimension |
|---|---:|---:|---:|---:|---:|
| S4 | 24 | 3 | 14 | **10** | 10 |
| S5 | 120 | 15 | 103 | **17** | 17 |

The rank checks use 72 and 1,800 original-permutation-square constraints respectively; separate direct independent assignment indicator matrix has S4 rank10. The ALL-n>=4 mathematical proof in §2 is not inferred from these finite numerical ranks.

More importantly, the true ORIGINAL W32/K6 S68 fixed globally injected point map f, **all 45 true original source incidence IDs**, and **62,370 unique true original six-ID f-left-valid sets** produced exact original historical seven-tag vectors for four individually fully globally injected source LINE-image assignments g,gσ,gτ,gστ, with σ=(0,1), τ=(2,3):

Historical coordinate order (D6,B-left/A-right,A-left/B-right,C/A,C/B,BB-overlap,BB-disjoint):

| Global original right state | Seven historical accepted true-original six-ID counts | Unweighted S7 |
|---|---|---:|
| g | (0,44,21,0,0,2,1) | 68 |
| gσ | (0,56,25,0,0,4,2) | 87 |
| gτ | (0,67,41,0,0,2,0) | 110 |
| gστ | (1,73,51,0,0,3,1) | 129 |

The exact mixed finite differences are:

\[
\begin{array}{rcl}
H_{\sigma,\tau}S_7 &=& 0,\\
H_{\sigma,\tau}\bigl(S_7^2\bigr) &=& \boxed{+1596},\\
H_{\sigma,\tau}\left(\sum_{k=1}^7 S_k^2\right)&=&\boxed{+368},\\
H_{\sigma,\tau}W_{\mathrm{GF5},7}&=&-46107,
\end{array}
\]

where \(W_{\mathrm{GF5},7}\) is the PREVIOUSLY CERTIFIED *selected necessary* 51-palette GF5 R3-floor NUMERATOR, **NOT** the complete R3. The two explicitly NONLINEAR functionals are truly different from the linear S7 and have NONZERO signed Hessian despite H(S7)=0. Replacing baseline g by the LEGAL full global gσ reverses EACH of these mixed Hessian signs without changing f, occupied right E(K6), source incidence identities or physically coherent factor assignments.

The exact four seven-component original vectors and all four signed Hessians are **pinned in independent regression tests** after the first run; exact final-child-HEAD validation must be performed again. A separate actual full coordinate relabel of ALL 15 original right pair-edge source factor images by one permutation of the SIX physical vertices leaves every historical original seven class unchanged; this concretely verifies the needed transitive right physical gauge invariance. Neither the physical coordinate relabels nor the four original g states redraw labels independently per original six-Q.

**Proper scientific conclusion:** this establishes a fully general nonlinear **proof-strategy constraint**, not the mathematically different every-fixed-(f,g) GF5 positive seven-family lower or any all-h ASET exponent. There may exist successful proof strategies using fixed-original f,g source geometric Hall density, nonlinear functionals with no supposed universal mixed-Hessian sign, favorable existential moves, and other original incidence constraints. This Draft requires exact final SHA dedicated, INDEX, Proof Audit and full Research CI plus independent mathematical referee before scientific acceptance; no automatic merge into main.
