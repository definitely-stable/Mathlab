# HYP-105 / issue #230 — D6-AA4-U-CYC: ALL-h exact shared-original-LINE cycle-gluing kernel, and a genuine W32 21,186-event anchored joint row

**Research-only, strictly stacked on 4/4-GitHub-hosted-success [D6-AA4-T-CYC #485](https://github.com/definitely-stable/Mathlab/pull/485), pinned exact parent HEAD \`07a60d1f9e7b9faa0e9de276d58913006240479b\`. No main modifications, issue #230 OPEN, no merge, no inflated all-maps theorem.**

## 1. Research gap and new all-h statement

The preceding D6-AA4-R-CYC #480 proved \(\forall f\,\mathbb E_g D6(f,g)\ge s^6/8\) for all real ORIGINAL W(3,s), s=2^h>=8, and D6-AA4-T-CYC #485 gave the exact pair probability when two D6 candidate source-original six-incidence Q0,Q1 have DISJOINT source-original LINE factor sets, allowing original point-factor overlap. The 64-term physical C6 complement count \(H_a\) used in the disjoint kernel was already introduced in JPKC-016 #458 and independently reverified in #485. **It is not a new physical cycle counting theorem.**

The missing conditional covariance cases consist of two actual six-DISTINCT-original-incidence Q0,Q1, each having SIX DISTINCT original point factor IDs and SIX DISTINCT original line factor IDs and physically connected C6 on the LEFT under ONE fixed globally injected source point map f, but possibly SHARING r=1,...,6 original line factor IDs. One globally injected source-line physical edge map g must assign exactly the SAME physical pair label to each shared source line factor, and different original line factor IDs must receive different physical pair labels. This makes the exact location of each shared line in the two original six-column C6s essential.

## 2. New genuinely all-h exact falling-factorial gluing polynomial

Represent each original Q_i by its physical-left six-column D6 dual, now understood as an abstract simple 6-cycle C_i on the SIX true source ORIGINAL LINE factor IDs of Q_i. This is legitimate because all six original source LINE factors are distinct and each original incidence position corresponds to exactly one such line. Choosing six injective physical right coordinates on the six EDGES of C_i uniquely determines the unordered physical g(line) pair at each source-line vertex from its two incident edge coordinate symbols. Conversely any right physical image satisfying historical aligned D6 comes uniquely from this edge coloring.

Let r=|L(Q0)∩L(Q1)|. Up to independent dihedral symmetries of both six-cycles and renumbering the nonshared original line vertices, their relative glued cyclic line graph has a canonical signature \(\tau\). Exactly one underlying common physical coordinate map g is required; the two source cycles MAY overlap in original POINT factors, but g sees their shared ORIGINAL LINE factor IDs.

Fix one of the \((a)_6\) possible injective right physical coordinate assignments to C0, normalized by physical coordinate symmetry to colors 0,..,5. For C1, choose an injective assignment to its six cyclic edges. Each coordinate symbol is either one of those SIX already used or a **NEW** symbol; exactly k new symbols can occur for 0≤k≤6, and each fresh symbol is used at most once in the second six-edge color injection.

Define \(c_{\tau,k}\) to be the **nonnegative INTEGER count** of all valid canonical second-cycle coordinate choices with exactly k abstract fresh symbols appearing in their first-occurrence order, such that:
1. C1 uses exactly six pairwise-distinct physical coordinate symbols;
2. for each shared original line vertex, its unordered pair of incident physical colors is EQUAL in both cycles;
3. no two DISTINCT original source LINE factor vertices in \(V(C0)\cup V(C1)\) receive the same unordered physical pair label (global type injection).

Each canonical second assignment with k new symbols has exactly \((a-6)_k\) concrete realizations in any physical alphabet with a≥6 symbols; no other multiplicity factor is missing, since canonical fresh names track the new positions in their increasing C1 cyclic order. Consequently **for every TRUE original W(3,s), every fixed full global f and every eligible pair Q0,Q1 of actual original incidences**, the exact conditional probability under ONE full uniform global right physical map g is

\[
\boxed{
\Pr_g[D6(Q_0)\wedge D6(Q_1)\mid f]
=
\frac{(a)_6}{(K)_{12-r}}
\sum_{k=0}^{6}c_{\tau,k}(a-6)_k,
\quad K=\binom a2,\ r=|L(Q_0)\cap L(Q_1)|.
}
\]

The denominator is the exact number of ordered globally INJECTIVE physical edge-label assignments to the 12−r distinct TRUE original source line factor IDs. Every term counts such assignments once. This is an exact integer falling-factorial polynomial, **not** an independent product, asymptotic or statistical approximation. It requires no source-point-factor-disjoint assumption because f is held fixed; all six ORIGINAL incidence IDs remain true and shared across the two projections.

The coefficients are computed by a finite, alphabet-independent **13,327-pattern enumeration**: for each of six cyclic C1 edge coordinate positions, select one of the not-yet-used original six coordinate symbols or the next canonical new symbol. Reject assignments violating equality of the pair labels of shared original LINE vertices or distinctness of labels for all 12−r source line factor IDs. Every valid k-fresh-symbol pattern increments \(c_{\tau,k}\). At arbitrary larger a, evaluate only \(\sum_k c_{\tau,k}(a-6)_k\) in exact integer arithmetic (no huge physical graph or huge original GQ source enumeration required). The canonical signature minimizes over 12×12 dihedral orientations of the two line cycles with independent relabeling of nonshared line vertices, and is invariant under arbitrary presentation of the same actual cyclic line graph.

### Strict edge-case consistency

- r=0: exactly recovers the earlier #485 source-line-disjoint joint kernel \(p\cdot12H_a/(K-6)_6\), where \(H_a\) is the physical C6 count avoiding the first accepted six-image C6.
- r=6, SAME cyclic edge adjacency on all six true source line vertices: the two GF5 D6 events are IDENTICAL (even if original incidence positions/point factors differ), and the joint probability is exactly \(p=(a)_6/(K)_6\).
- r=6, DIFFERENT cyclic adjacency on the same six true source line vertices: the two D6 requirements on one global right map g are mutually incompatible; joint probability is **zero**.
- **r=2 can yield BOTH zero and positive joint probabilities** even with EXACTLY the same overlap cardinality, depending on relative original line positions of the shared vertices. E.g. \(\tau=(0,2,6,7,8,9)\) has all \(c_{\tau,k}=0\) and hence joint probability 0 for EVERY a; \(\tau=(0,6,3,7,8,9)\) has positive coefficients and joint probability positive at a=6. A numeric r-only kernel is UNSOUND.

## 3. Independent finite genuine ORIGINAL W32 joint original line-cycle oracle

Fix S68 or S72 actual W(3,2) with 45 true ORIGINAL incidence IDs and complete globally injected K6 point f. From the earlier #480/#485 physically connected source enumeration recover exactly 21,186 actual six-distinct-original-incidence Q, each with physically LEFT connected six-column C6 and six different true ORIGINAL source line factor IDs.

Independently reconstruct the abstract six-line cycle from the SIX actual source original incidence columns: for each of the six physical LEFT coordinate symbols find the TWO incidence columns using it; connect the actual ORIGINAL LINE factor IDs of those two columns. Strict fail-closed checks demand six distinct original point and line factors, degree exactly two at every line factor, no premature shorter cycle, and connected C6 on the six actual original line IDs. This retains genuine source topology and a single full global point map.

Choose ONE deterministic true original Q0, enumerate ALL other 21,186 true original Q1, classify every pair by exact canonical \(\tau\) (not merely r), and count class sizes. Compute the **exact entire ANCHORED row of the conditional two-D6 expected count**:

\[
\boxed{
R_{Q_0}(f)=
\sum_{Q_1\in\mathcal Q_f}
\Pr_g(D6(Q_0)\wedge D6(Q_1)\mid f).
}
\]

This is an **entire anchored row** of the 21,186×21,186 pair matrix, including all r=0,...,6 source-line overlap sectors, with mixed line-sharing probabilities evaluated by the all-h gluing polynomial. It is STRICTLY NOT the full pair sum or full variance (requires every Q0, not a single row). Regrouping by only r would conflate the exact incompatible/compatible gluing signatures. Frozen predecessor #485 genuine W32 source-line overlap row is the independent benchmark: r0:305,r1:3,061,r2:7,934,r3:7,173,r4:2,426,r5:279,r6:8.

The dedicated tests independently enumerate all 6! physical right coordinate assignments for fixed first six colors, **without using the 13,327 canonical old/new pattern enumeration**, on selected r=0,1,2,3,6 types, and demand equality with the polynomial constant \(c_{\tau,0}\) at a=6. For a selected genuine W32 r=2 type with positive kernel, construct ONE COMPLETE globally injected right K6 map g, assigning all TRUE original source line factors consistently, and require the historical ORIGINAL seven-GF5 classifier \`classify_seven_prechecked\` to return D6 for BOTH original six-incidence Q0 and Q1. For another genuine r=2 type with zero kernel, prove impossible to accept both by the zero nonnegative-coefficient polynomial (not by failure of randomized search). Both examples have exactly TWO shared ORIGINAL line factors, thus prove rigorously that overlap cardinality is insufficient.

## 3A. Hosted verified exact REAL W32 21,186-source-Q anchored pair result

The initial corrected dedicated [GitHub-hosted #38690494064](https://github.com/definitely-stable/Mathlab/actions/runs/38690494064) completed **SUCCESS 3/3 jobs**, including seven independent tests, actual real S68/S72 all-original six-ID source geometry, and a true globally injected right map under which two actual r=2 Q have D6 simultaneously. On both S68 and S72, with the frozen exact same genuine original anchor \(Q_0=(0,5,7,10,13,39)\), the complete **one-anchored-row** values are:

| Source-statistic on 21,186 genuine Q' | EXACT |
|---|---:|
| Actual left-connected C6 source Q' in this anchored row | 21,186 |
| Non-isomorphic cyclic line-gluing signatures under 12×12 dihedral symmetry | **112** |
| Genuine Q' for which the joint historical GF5 D6 probability is strictly positive | **6,192** |
| Genuine Q' for which the joint historical GF5 D6 probability is provably zero | **14,994** |
| \(\displaystyle\sum_{Q'}\Pr_g(D6(Q_0)\land D6(Q')\mid f)\) | \(\boxed{19457/10810800}\) |
| \(\displaystyle\mathbb E_g[D6(f,g)\mid D6(Q_0),f]\) | \(\boxed{19457/2160}\) |
| Expected total \(D6\) under uniform complete right map from predecessor #480 | \(1926/455\) |

The positive count includes the true diagonal Q'=Q0, with probability p=1/5005. The 112 gluing-class exact-signature weighted row covers r=0,...,6 and is not a second-moment or covariance of total D6. The conditional expected count given this **specific** original Q0 accepted is ≈9.00787 versus the unconditional expected D6 count ≈4.23297. These conditional numbers depend on holding the ENTIRE globally injected original point map f fixed and using ONE random complete global right map g.

**Actual compatible/incompatible same-r=2 original six-incidence pair witnesses:**

- Fixed Q0 original incidence IDs \([0,5,7,10,13,39]\).
- Compatible Q1 original incidence IDs \([0,14,21,25,27,34]\), with exactly two common original LINE source IDs, and a COMPLETE globally injected right physical K6 source-line map \`[(0,5),(3,4),(0,1),(4,5),(1,2),(0,2),(0,3),(0,4),(3,5),(1,3),(1,4),(2,4),(1,5),(2,3),(2,5)]\` assigned in original source line ID order l=0..14. The historical original six-ID GF5 classifier returns **D6 for BOTH Q0 and Q1** using ONE f and this same g.
- Incompatible Q1 original incidence IDs \([0,13,21,25,34,42]\), also exactly two shared actual original LINE source IDs, but with canonical cyclic type \(\tau=(0,6,2,7,8,9)\). The corresponding \(c_{\tau,k}\) are all zero. **No physical alphabet and no globally injected g can make both original Q D6 simultaneously**, despite the matching overlap cardinality r=2. This is a genuine ORIGINAL W32 positional obstruction.

The numbers and complete-map witness are pinned in independent dedicated tests. The first initial CI attempt exposed and fixed a source-line-cycle adjacency validator bug (iterating dict vertex keys instead of adjacency sets); only corrected all-three-success runner evidence is accepted.

## 4. Limits, independent acceptance, and next research

This is a new ALL-h exact **pair gluing** formula across every possible shared-original-LINE source support positional pattern, generalizing the previously known disjoint sector #485. It does NOT establish a positive universal lower on original seven GF5 S_s for every f,g and does NOT prove original Branch A/B, full R3 or ASET exponent. It does NOT establish the complete conditional \(\mathbb E_g D6(f,g)^2\) for arbitrary fixed f, because an anchored row or a partial original source family is not an all-source-pair histogram; the full W32 source family pair count 21,186² remains unaggregated.

**Next AA4-V-CYC:** develop exact histogram over ALL true original left-C6 Q0,Q1 gluing signatures for fixed real f (or a symmetry-reduced/original incidence orbit proof of histogram invariance), then combine it with the proven kernel to get FULL actual finite W32 conditional second moment and variance. General all-h variance will require global source overlap histogram bounds, and even a full variance is not a \(\min_{f,g}S_s=\Omega(s^6)\) theorem. Continue parallel AA4-T #484 and JPKC source Hall tensor studies without conflating conditional expectation with global worst-case.

All work stored as four additive files: executable original gluing oracle, independent brute and genuine GF5 tests, this mathematical proof/limits document, GitHub-hosted dedicated workflow. Final SHA dedicated/INDEX/Proof Audit/Research must succeed, followed by independent mathematical peer review, before technical acceptance. main unchanged, Draft only, #230 OPEN.
