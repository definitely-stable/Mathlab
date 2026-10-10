# HYP-105 B3.2-E1-B1-B — exact correlated right label exchange, W(3,2) finite oracle

Date: 2026-10-10. [Parent #230](https://github.com/definitely-stable/Mathlab/issues/230), [#176](https://github.com/definitely-stable/Mathlab/issues/176); builds on merged [#233](https://github.com/definitely-stable/Mathlab/pull/233). Compatible with independent uniform-quantifier B1-A [#238](https://github.com/definitely-stable/Mathlab/pull/238).

**STATUS: mathematical exact swap-locality identity for arbitrary finite original incidence systems; exhaustive finite W(3,2), a=6, 105 possible RIGHT factor-label transpositions. Not a new asymptotic ASET theorem, not a universal two-sided lower, not even a full positive GF5 R3 minimization.**

## 1. Two transformations that MUST NOT be confused

For the 15 original right GQ line-factor vertices in W(3,2), a right labeling is a bijection to the 15 K6 physical pair-edge labels.

1. A permutation of the **six physical coordinate symbols** moves every right pair label by the same graph automorphism. For every original six-incidence set, the multiset of physical coordinate incidence degrees, the column-dual adjacency graph, class of GF5 signed patterns, and the full 51-palette exact GF5 flow count are all invariant. This is a pure gauge; searching it does not change S_seven, Q4 or the exact weighted selected risk.
2. A transposition of the **right pair-edge labels assigned to two ORIGINAL factor line vertices** typically is NOT induced by a physical-coordinate permutation. It can modify the right physical 2-regular projection on original sixsets containing either of these two line endpoints; it can change the seven-family risk floor. This is the smallest nontrivial correlated-label move.

Thus optimizing only physical symbol relabelings, or interpreting coordinate gauge as independent physical K6 pair assignment, would be mathematically incorrect. Even at a=6, the full K-edge-permutation space has size 15!, much larger than the physical coordinate gauge S6, and exhaustively searching it is not claimed here.

## 2. Exact swap-locality identity

Fix left label injection f, right label injection g, and original incidence graph H. Let C_f be the set of original six-incidence subsets passing the required LEFT six-coordinate degree-two test. For each E in C_f let I_g(E) be the indicator that its RIGHT projection and original factor multiplicity profile place E in one of the seven accepted strictly positive GF5 six-motif classes. Define S_7(f,g)=sum_{E∈C_f} I_g(E).

Let g' result from swapping only right-factor original vertices u,v. Set C_f[u,v]={E∈C_f: E has an incidence with original right endpoint u or v}. Then EXACTLY, without probabilistic assumptions:

```text
S_7(f,g') - S_7(f,g) =
  sum_{E∈C_f[u,v]} [I_g'(E)-I_g(E)].
```

Proof: for E outside C_f[u,v], every right original endpoint is different from u,v, hence all assigned physical pair labels are identical under g and g'. Its left assignment is unchanged, so I_g'=I_g termwise. This is cancellation, not an approximation. Replacing I by the class-specific accepted full-GF5 minimum weights gives the analogous exact integer *necessary-floor numerator* delta.

For W(3,2), accepted E1-A proved |C_f|=62,370 and the right pair alphabet covers all 15 K6 edges. There are exactly binom(15,2)=105 distinct right original line-factor pair-assignment swaps. The reference code constructs all 62,370 left candidates once, indexes each by its set of right original factor endpoints, and checks only swap-affected candidates (with no sampling or silently omitted sixsets). Every candidate is an actual unordered six-original-incidence set; the classes D6/B-left/B-right/C/A/C/B/B/B are mutually disjoint by accepted #233.

The primary optimization objective is **S_7**. Ties use the accepted min-weight GF5 seven-family risk floor and lexicographic swap ID. This does NOT imply minimized full 51-palette six-event risk. The code verifies the best predicted swap by a completely independent full 62,370-candidate seven-family oracle and independent physical C6/C4 incidence joins; then computes the exact selected 10-sign full-palette GF5 risk of the chosen new right labeling. It neither claims a certified local optimum over several swaps nor runs a multi-generation search.

## 2A. All-h uniform bounded-influence theorem for one correlated right-label swap

**Theorem E1-B1B-U (proved, elementary).** For every s=2^h, all left/right pair injections f,g of the W(3,s) source and every swap of two original RIGHT factor line-vertex physical pair labels, the seven-class selected S and its accepted minimum-weight GF5 risk numerator satisfy explicit finite-h bounds depending ONLY on the host parameters.

Let V=(s+1)(s²+1), Δ=s+1, a=min{n:binom(n,2)>=V}, K=binom(a,2). Let c_A=70,c_B=45,c_C=15, F_k=c_k binom(a,6). Let λ_A=Δ^6, λ_B=binom(Δ,2)Δ^4, λ_C=binom(Δ,2)^3 and L^+ = Σ F_k λ_k, the accepted all-h upper on LEFT six-coordinate leafless original sixsets (#238).

Fix one *specific original incidence* (p,l) with fixed physical edge e=f(p). Over ALL K_a physical A/B/C templates, count the multiplicity of occurrence of e as an ORIGINAL left factor column (once for A singles; twice for B/C duplicated pair labels). Every physical template has exactly six factor-incidence columns, so the sum of these column-occurrence counts over all K physical edges is 6F_k. By full-K_a edge-transitivity, **each physical edge occurs with total multiplicity exactly 6F_k/K**. Conditional on a template that uses left factor p with multiplicity m=1 or 2, the probability that a uniformly chosen valid m-subset of its Δ distinct original incident edges includes the specified original incidence (p,l) is exactly m/Δ. Therefore an actual (p,l) lies in **at most**

```text
(6/(K*Δ)) Σ_k F_k λ_k = 6 L^+/(K Δ)
```

left-qualified original sixsets, with no assumption on the right labeling. This is a full-K_a upper, so omitting physical pair labels cannot invalidate it.

One original right line factor l has Δ distinct incident original edges. Union-bounding over those Δ edges gives <=6L^+/K left-qualified original sixsets touching l. Thus swapping two distinct right line factors u,v touches at most

```text
B_s = min{L^+, floor(12 L^+/K)}
```

original sixsets. Since every selected seven-class E contributes an indicator in {0,1}, and all other E are unchanged,

```text
| S(f,g')-S(f,g) | <= B_s.
```

For the class-specific accepted GF5 **minimum-weight floor** numerator W(f,g)=Σ_E w_class(E), with possible weights 0,5643,43320,45010,45600,49050,51750, each individual E changes W by at most 51750. Therefore

```text
|W(f,g')-W(f,g)| <= 51750 B_s.
```

Using K=(1+o(1))s³ and L^+=(151/144+O(1/s))s^15, the upper is

```text
B_s = (151/12+o(1))s^12.
```

For s=2, L^+=62,370, K=15, giving B_2=min(62370, floor(12*62370/15))=49,896. The exact 105-neighbor W32 oracle verifies *every* affected-set count and both delta inequalities against the all-h integer bound. For s→∞ the per-swap influence is o(L_s(f)), but its O(s^12) scale is MUCH larger than the conjectured obstruction Ω(s^6). It therefore proves neither a universal all-correlated lower bound nor a constructive infinite counterexample.

This all-h bound is elementary double-counting, not a new spectral theorem or a new exact full 51-pattern GF5 risk upper. It places a rigorous constraint on how a LOCAL right factor-label exchange can change the selected structural GF5 obstruction.

## 3. Independent falsifiers and significance

The independent CI test runs the complete all-105 one-swap landscape on the fixed `reverse-line` W(3,2) input, verifies all 105 physical right factor-pair swaps are present exactly once and that the reported minimum is a genuine minimum over every neighbor. It tests the incremental predicted S and weighted GF5 lower numerators against three complete original-sixset re-enumerations for hand-selected swaps, *not* just the winner. The winner is independently recounted by a separate full structural/original-incidence oracle. A further test proves the two-swaps involution (including rebuilt full physical four-coordinate supports) and checks arbitrary physical coordinate-label gauge preserves S, Q4 and the weighted floor exactly.

The output supplies a finite certificate for how correlated pair-edge reassignment alters joint left/right motif counts. It is **only at s=2**, not an infinite family. A better S or Q4 value cannot refute `S_s(f_s,g_s)=Omega(s^6)` with an absolute constant as s→∞; a zero finite count would not disprove a sufficiently-large-s asymptotic claim either.

The previous [B1-A](https://github.com/definitely-stable/Mathlab/pull/238) mathematically proved a (140+O(s^-1))s^6 mean B/A for uniform INDEPENDENT g given arbitrary f. An *adversarial* selected swap does not contradict it: the mean quantifier and minimization over right label permutations differ. This finite experiment precisely tests that quantifier separation.

### Prior-art transfer
Recent rainbow/properly colored cycle work such as [Kim, Lee, Liu and Tran, *Rainbow Cycles in Properly Edge-Colored Graphs* (Combinatorica 2024)](https://doi.org/10.1007/s00493-024-00101-7) does not establish our exact two-color coupled GF5 moment inequality. In the original GQ model, each incidence edge at one factor vertex inherits the same physical pair label; the induced coloring is *not proper*. No automatic rainbow-cycle/expander or spectral theorem may be imported into the proof without first changing and proving a model-preserving reduction.

## 4. Acceptance and open barrier

Acceptance requires GitHub-hosted full Research CI on EXACT PR HEAD, including independent original-sixset recount, exact selected full 51-palette GF5 risk and separate full GQ provenance checks; postmerge main Research must pass separately. Parent #230/#176 remain OPEN. The next B1-C theorem target is a **uniform-in-h lower for ALL correlated right injections** on the transfer fraction S/L (or an explicit infinite counterexample); finite exchange search only generates useful falsifiers and constraints.
