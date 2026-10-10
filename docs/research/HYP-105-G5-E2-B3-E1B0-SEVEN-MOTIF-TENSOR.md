# HYP-105 B3.2-E1-B0 — exact seven-motif same-label obstruction and all-h coefficient identity

Date: 2026-10-10. Scope: [#230](https://github.com/definitely-stable/Mathlab/issues/230), parent [#176](https://github.com/definitely-stable/Mathlab/issues/176). Inputs already accepted: PRs #214, #218, #224, #225, #227.

**STATUS: theorem-level exact multilinear reduction for ANY h; fully exhaustive finite W(3,2) evaluation of seven accepted positive subfamilies and Q4 on the SAME labeling. NO universal Omega(s^6), NO strict R3 upper, NO complete full-palette GF5 R2/R3, NO ASET exponent.**

## 1. The seven disjoint necessary six-event classes

For each fixed pair injection f:P_s→E(K_a), g:L_s→E(K_a), the selected original factor-incidences e=(p,l) correspond to support-4 columns f(p) in the left physical coordinate block and g(l) in the right block. A positive full-GF5 3v3 trade requires *every used physical coordinate* to have incidence degree >=2. In the restricted **exactly six coordinate vertices per side** regime every used coordinate therefore has degree exactly 2.

The necessary left/right factor endpoint profiles are only A=(1,1,1,1,1,1), B=(2,1,1,1,1), C=(2,2,2). We retain seven proven positive, mutually exclusive families, counting each ORIGINAL six-incidence unordered set ONCE:

| Family | Original factor profile | Necessary exact full-GF5 lower weight per set |
|---|---|---:|
| D6 | A/A with identical connected dual column C6 left and right | 5,643 (one alternating 3v3 signed event) |
| U_B-left | B/A and both leafless six-coordinate projections | 45,600 (10 balanced signs, each at least 4,560) |
| U_B-right | A/B and both leafless six-coordinate projections | 45,600 |
| U_CA | C/A or A/C, six coordinates both colors | 43,320 |
| U_CB | C/B or B/C | 49,050 |
| U_BB-cap | B/B repeated original factor column-ID pairs intersect in one index | 51,750 |
| U_BB-disjoint | B/B repeated original factor column-ID pairs are disjoint | 45,010 |

The **accepted fixed-label lower bound** is, for all h>=1,

```text
R3(f_s,g_s) >=
 [5643*D6 + 45600*(U_B-left+U_B-right) +
  43320*U_CA + 49050*U_CB +
  51750*U_BB-cap + 45010*U_BB-disjoint] / 51^6.
```

The D6 family is checked with a specific *connected* column-dual C6, not any 2+2+2 disjoint triangles. A/A with noncoincident cycles or 2C3 is uncharged by this selected lower, even if its GF5 risk is positive. The per-event numbers are minima rather than the actual sum of all positive GF5 signed flows for that set. No double counting due to factor-profile separation. All coefficients have full 51 nonzero checksum-4 patterns; no unit-GF5 substitution.

The independent exact four-motif necessary floor is

```text
R2(f_s,g_s) >= 531 * Q4(f_s,g_s) / 51^4,
```

where Q4 is the accepted coincident physical C4/C4 ORIGINAL factor-matching count, and 531 is the separately verified nonzero/full-51 GF5 signed count. Thus this slice supplies a **same-label pair of necessary risk floors**; it does not combine them into one asymptotic obstruction.

## 2. Exact multilinear coefficient identity — holds for every h

For the SAME two injected physical pair labels define a formal polynomial over the nonnegative integers,

```text
P(t; X,Y; U,V) =
  product over ORIGINAL incidences (p,l) of
  [1 + t * U_p * V_l *
    X_{f(p)_1} X_{f(p)_2} *
    Y_{g(l)_1} Y_{g(l)_2} ].
```

No GF5 addition or cancellation appears in P: this is a combinatorial count. Every selected original incidence set contributes exactly ONE product term, and because the original GQ is a simple bipartite graph there are no repeated factor incidence columns. For any subsets S,T of six DISTINCT coordinate symbols each, the sum of coefficients of all monomials

```text
t^6 * (prod_{i in S} X_i^2) *
       (prod_{j in T} Y_j^2) *
       (prod_{p} U_p^{alpha_p}) *
       (prod_{l} V_l^{beta_l})
```

over all sixsets S,T, with prescribed original endpoint degree vectors alpha,beta, is **exactly the number of six-incidence sets whose physical projections each use exactly six coordinates of degree two and whose original factor endpoint partition profiles are alpha,beta**.

This identity has no randomness and is valid uniformly in h for arbitrary legal f,g. It gives an exact algebraic *representation* of the original factor endpoint and physical Eulerian constraints. It is NOT a polynomial-time method to compute its coefficients at large s, nor a lower bound on nonzero coefficient mass.

A genuine universal obstruction for #230 would need, for all allowed f,g and s=2^h,

```text
D6 + U_B-left + U_B-right + U_CA + U_CB
+ U_BB-cap + U_BB-disjoint >= c * s^6
```

for an absolute c>0 (or a weaker flow-weighted version sufficient to block strict R3). The identity P alone does not supply it: all terms are nonnegative, but coefficients can vary drastically under physical pair relabelings. The burden is exactly an all-label lower on selected coefficients, not an average over independent labelings.

## 3. Complete W(3,2) computation, independent falsification

At s=2, the original factor graph has 15 vertices per color, 45 distinct original incidences and degree three. Physical K6 has exactly 15 unordered pair labels, so both maps are bijections. The accepted E1-A leafless LEFT projection constructor selects each and only each of 62,370 original six-incidence subsets once (A=51,030, B=10,935, C=405), avoiding binom(45,6)=8,145,060 scanning. On those sets the NEW seven-family classifier checks the RIGHT six-coordinate leafless projection, the original endpoint partition, and, only for D6, equality of CONNECTED column-dual simple C6s. It outputs exact seven-family counts and the accepted weighted minimum lower.

Two independent accepted algorithms on the SAME model are invoked as cross-checks: (i) D6, using a physical C6 DFS plus constrained original line neighbor join, not the sixset dual-graph classifier; (ii) Q4, using a physical C4 DFS plus original line neighbor join and independent full-51 GF5 MITM verification of coefficient 531.

Independent tests also check:
- brute six-combinations over multiple explicitly witness-enriched TEN original-column subuniverses for **all seven** types, without reuse of the new classifier (not a claim of representative sampling);
- separate physical-coordinate permutations in each color block, a legitimate gauge symmetry of these structural motif counts;
- a direct ten-column 2^10-term product expansion versus the t^6, all-degree-two polynomial coefficient selector;
- preservation of #227's independently accepted four-class fixed-label counts, risk floor and strict fail-closed checks.

Two fixed schemes `lex` and `reverse-line` are reported on the **same** factor incidence order and exact finite physical bijections. Differences in the counts are not evidence of an all-h exponent or of a smaller COMPLETE R2/R3.

## 3A. Exact FULL 51-palette GF5 signed risk of this selected seven-family subset

Beyond the accepted universal lower based on positive minima, the [same-label oracle](../../research/hyp105_g5e2b3e1b0_seven_signature.py) now evaluates the **exact restricted seven-family GF5 3v3 contribution** for finite W(3,2). After collecting each qualifying ORIGINAL six-incidence set once, it independently evaluates **all ten unordered balanced signed partitions** of that set with the accepted 782-state exact GF5 dual Fourier oracle on its actual twelve physical coordinates:

```text
R3_seven_selected(f,g)
 = (1/51^6) *
   sum_{sixset e in seven qualified families}
   sum_{10 unordered balanced sign patterns sigma}
   F_GF5(exact support(e),sigma).
```

This is an *exact sum of restricted events*, not a union probability. In particular, for coincident D6 sets it includes nine further sign patterns besides the one alternating event whose positive 5,643 count was used in the structural floor. Every original sixset is assigned to at most one of the seven structural families, so all these selected signed events are disjointly indexed. The program asserts

```text
R3_seven_selected(f,g) >=
 [5643 D6 + 45600(U_B-left+U_B-right)
  + 43320 U_CA + 49050 U_CB
  + 51750 U_BB-cap + 45010 U_BB-disjoint] / 51^6.
```

A hard cap of 5,000 exact GF5 events rejects oversized computations rather than reporting truncated risk. The CI independent tests validate all ten signs per qualifying original set, the exact per-class integer decomposition and this lower inequality for both pinned W(3,2) control labelings. Numerical full-event coefficients are accepted only after the exact PR-head GitHub-hosted Research success gate.

**CRITICAL:** This new `R3_seven_selected` is not the FULL `R3`: A/A non-D6 positive signatures, other positive six-projection signatures, and 11,032 subleading necessary forest types can contribute. Its comparison across finite controls does not imply any uniform-in-h asymptotic risk bound.

## 3B. Prior-art transfer firewall for the next all-label theorem

There are relevant extremal counting tools, but none presently implies the desired lower for our exact coupled coefficient mass:

- **Sidorenko/tree homomorphism inequalities.** Lüchtrath–Mönch, *A Very Short Proof of Sidorenko's Inequality for Counts of Homomorphisms Between Graphs*, published online 2025, journal issue 2026, DOI [10.1017/S000497272500019X](https://doi.org/10.1017/S000497272500019X). This gives an efficient prior-art route to nonnegative homomorphism counts in a **single target graph**. Our P-coefficient fixes SIX physical degree-two constraints in TWO separately injected K_a edge-label systems while coupling them via the same ORIGINAL W(3,s) incidence edges; the relevant coefficient selector is not a plain hom(F,G) or Sidorenko functional. No transfer asserted.
- **Properly edge-colored rainbow cycle supersaturation.** Kim–Lee–Liu–Tran, *Rainbow Cycles in Properly Edge-Colored Graphs*, *Combinatorica* 44 (2024), DOI [10.1007/s00493-024-00101-7](https://doi.org/10.1007/s00493-024-00101-7), and Alon, *Essentially Tight Bounds for Rainbow Cycles in Proper Edge-Colourings* (2025), DOI [10.1112/plms.70044](https://doi.org/10.1112/plms.70044). A **proper** incidence-edge coloring is NOT present in our model: all original incidences at a factor vertex inherit the same physical pair f(p) or g(l), so this naive coloring repeats at every factor neighbor. Neither rainbow-cycle theorem may be invoked without a proved model-preserving reduction to a proper edge coloring.
- **Finite GQ incidence spectral counting.** The incidence graph of W(3,s) has genuine expansion and girth eight, and s=2 is the Tutte 8-cage. However a spectral mixing bound for ordinary edge discrepancies is not an automatic sixth-order nonnegative coefficient lower when the two deterministic physical edge relabelings are allowed to be adversarial. A proposed transfer must explicitly define the multilinear contraction, the relevant spectral norms and error terms relative to s^6. No all-label theorem is claimed by citing expansion.

**Novelty discipline:** the formal coefficient extraction P is the elementary generating-function encoding of a set system, not a new named theorem. The finite W32 signed GF5 oracle and D6/Q4 join falsifiers are implementation contributions, not new asymptotic mathematics. Import scholarly papers canonically only after catalog deduplication; the DOI links here are prior-art candidates, not new LIT IDs or asserted imports.

## 4. Scientific gate and next action

This is an **E1-B0 RESTRICTED/REDUCTION THEOREM**, not a solution to the #230 all-h disjunction. Follow-up B1 should seek a real all-label lower or infinite correlated counterexample for the seven coefficient families, e.g. a spectral/tensor inequality or a concrete infinite family of gauge-inequivalent maps. A finite W32 discrepancy, a random-label expectation Θ(s^6), or a low Q4/D6 proxy does not close that gate. The 11,032 subleading forest types also remain relevant for any full GF5 R3 upper.

Acceptance: GitHub-hosted full Research SUCCESS on exact PR-head including independent tests; postmerge main CI separately. Keep parent #230/#176/#169/#162/#95 open until their own statements close.
