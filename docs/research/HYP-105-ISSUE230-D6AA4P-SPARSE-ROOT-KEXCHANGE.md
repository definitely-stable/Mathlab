# HYP-105 / issue #230 — D6-AA4-P: exact physical-root dual and genuinely GLOBAL source k-exchange neighborhood certificates

**Disposition:** exact all-h sparse-physical-support duality for ORIGINAL B(point)/A(line) seven-GF5 internal source charge; and rigorously COMPLETE k=2,3,4 *finite source-point exchange neighborhoods* on true W(3,2), using one full global physically injected point f and frozen complete globally injected line g. This does NOT prove the all-\(s\) HYP-105 root, does NOT certify the minimum over all \(15!\) W32 point assignments and does NOT turn positive expectation into adversarial all-map positivity.

Strictly stacked Draft on fully 4/4-GitHub-hosted-green [D6-AA4-O / PR #471](https://github.com/definitely-stable/Mathlab/pull/471), exact pinned parent HEAD \`b086566d8be17307b102e7bd89d28d4167af86a6\`. No main modifications, no merge or issue closure.

## 1. The bottleneck after O: a correct quintic but an intractable naïve assignment search

AA4-O proved for genuine \(W(3,s)\), \(s=2^h\), any globally injected point and line physical pair maps \(f,g\), the exact internal B/A charge is

\[
I_L^{BA,\mathrm{int}}(f,g)
=\sum_{p,A,\ |A|=4}w_g(p,A)\,
\chi_B(f(p),f(A)),
\]

where every \(w_g(p,A)\) is a nonnegative integer count of TRUE original six-DISTINCT-incidence Q using repeated source point \(p\), four other distinct original source points \(A\), six different ORIGINAL source line factors, a valid right physical A six-coordinate 2-factor under ONE fixed complete g, and PHYSICALLY DISJOINT right labels for the true original two-line pencil at p.

The indicator \(\chi_B\) is one iff the four physical edges assigned to the distinct factors in \(A\) form a C4 over four distinct physical coordinates, and the physical edge of root \(p\) is disjoint from all four coordinates. This was verified against the historical original all-62,370 true six-incidence GF5 classifier.

The full quintic coefficient array can contain many nominal five-factor supports (up to \(V\binom{V-1}4\)), but almost all \(\chi_B\)'s vanish at ANY one globally injected source labeling \(f\). The next proof-relevant improvement is to represent the **physically active supports** rather than iterate every possible five-factor term.

## 2. NEW all-h exact root-to-physical C4 dual — source-sparse evaluator

Let the physical coordinate alphabet have \(a\) symbols, and let \(f\) send all \(V\) true original source point factors injectively to distinct edges of \(K_a\). Fix one actual original source point \(p\), and denote its two-coordinate physical edge by \(e=f(p)\). Any accepted left-B Q root at \(p\) must use exactly FOUR other physical coordinates \(U\subset [a]\setminus e\). For a fixed unordered four-symbol set \(U=\{u_0,u_1,u_2,u_3\}\), there are EXACTLY THREE distinct simple four-edge C4 subgraphs of the complete K4 on U: remove one of the THREE perfect matchings of K4 from its six edges. The four physical edges of that C4 must ALL be present in the physical image \(f(\mathrm{OriginalPoints})\). Because \(f\) is globally injective, each occupied physical edge identifies ONE unique true original source point factor via the inverse map \(f^{-1}\).

Therefore for ANY true original W(3,s) complete injection f and fixed complete g:

\[
\boxed{
I_L^{BA,\mathrm{int}}(f,g)=
\sum_{p\in \mathrm{OriginalPoints}}
\ \sum_{\substack{U\subset[a]\setminus f(p)\\|U|=4}}
\ \sum_{\substack{C\subset E(K_U)\\C\text{ is a simple }C_4\\
 C\subset f(\mathrm{OriginalPoints})}}
w_g\bigl(p,\{f^{-1}(e):e\in C\}\bigr).
}
\]

This identity enumerates the exact same ORIGINAL six-incidence B/A charge and never assigns physical labels independently to Q. It uses only the inverse of the ONE globally coherent complete f, all four-source C4 patterns, and the exact genuine-original fixed-g coefficient tensor. Every physically admissible quintic term occurs **exactly once** (root p is unique; U is its four physical coordinates; the actual C4 edge-set is unique).

Consequently the number of physically active five-point support keys in ANY complete f is bounded by

\[
\boxed{
\#\mathrm{ActiveSourceKeys}(f)\le
3V\binom{a-2}{4}.
}
\]

This is a universal **computational sparsity upper**, NOT a lower on positive GF5 motifs and NOT a bound on \(I_L^{BA,\mathrm{int}}\) without the original \(w_g\) weights. Exact useful computational complexity is \(O(V\binom{a-2}{4})\) potential physical cycle probes plus coefficient-dictionary lookups rather than scanning nominal \(O(V^5)\) original five-support keys.

### SPECIAL TRUE W(3,2) K6 case: EXACTLY 45 physically compatible quintic source supports

For W(3,2), V=15 and the minimal alphabet is a=6 with K=C(6,2)=15. A complete globally injective source-point map f necessarily occupies **ALL 15** edges of the complete physical K6. For each of the 15 original source roots p, its physical edge occupies two symbols, leaving EXACTLY four other coordinate symbols; ALL three possible C4 subgraphs on those four symbols are occupied. Thus for EVERY globally allowed full original source point bijection f,

\[
\boxed{\#\mathrm{ActiveSourceKeys}(f)=15\cdot3=45},
\]
exactly three potentially active original five-factor support keys per true ORIGINAL source point, even though the universe has \(15\binom{14}4=15{,}015\) distinct root-plus-four-other-original-source-point keys. Most of the 45 active keys may have \(w_g=0\); they must not be counted as accepted positive Q without the real original tensor coefficients. The independent test enumerates ALL 15,015 candidate five-source supports by a separate original-factor-major physical-graph degree oracle for pinned real W32 f maps, and proves its list of 45 exactly matches the new physical-coordinate-major construction.

### Symmetry without false ROOT extrapolation

A permutation \(\sigma\in S_a\) applied to **all physical coordinate symbols of f only**, with the complete original-line g unchanged, preserves the C4/disjointness predicate \(\chi_B\) for every original quintic source support, and hence EXACTLY preserves this B/A internal charge \(I_L^{BA,\mathrm{int}}(\sigma f,g)=I_L^{BA,\mathrm{int}}(f,g)\). This is an exact all-h symmetry of the **particular internal BA quintic component**, not necessarily a symmetry of the COMPLETE seven-family full GF5 objective if it uses mixed physical endpoint alignment. On true complete W32 K6 labelings, the S6 action on all fifteen edge labels is faithful and free, hence every f has **720 distinct equally charged** globally injected images. This reduces the theoretical exact finite search from 15! to \(15!/720\) coordinate orbits. That quotient remains far too large to call the original W32 global optimum certified in this slice.

## 3. NEW exactly enumerated coherent 2/3/4-source exchange neighborhoods

For a fixed true complete W32 point physical-label assignment f (15 original point factors bijective to all 15 physical K6 edges), choose k distinct original point factors and PERMUTE their already assigned physical-edge labels by a derangement on those k factor IDs; leave every other original source point label and ALL original line g labels FIXED. This preserves the entire true ORIGINAL global f/g injection constraints. A nonidentity change is supported on EXACTLY k source factor IDs. Thus the sets of possible complete maps at Hamming support 2, 3, 4 respectively have EXACT sizes

\[
\binom{15}{2}\,!2=105,\qquad
\binom{15}{3}\,!3=910,\qquad
\binom{15}{4}\,!4=12{,}285,
\]
where \(!2=1,!3=2,!4=9\) are derangement numbers. Including all exact support sizes 2,3,4 gives **13,300 distinct valid complete globally point-injective maps**, every one sharing the exact same g.

The new sparse 45-support evaluator makes evaluating this ENTIRE radius-4 coherent exchange neighborhood practical, unlike repeatedly scanning all nominal quintic terms. It enumerates ALL 13,300 assignments with **no candidate sampling and no partial scope confusion**, computes the exact true original B/A charge for each, obtains the true best admissible k-source exchange, and separately checks the winner against:
1. AA4-O's independently implemented full nominal quintic tensor evaluator, and
2. the historical full 62,370 true-original-six-incidence **seven-family** GF5 classifier (for each per-k certified neighborhood winner).

The search gives an EXACT minimum for each explicitly stated k-exchange neighborhood. It does **NOT** give an all-\(15!\) global finite W32 minimum, does **NOT** imply positivity for arbitrary orders s>=4 and does **NOT** refute any original HYP-105 asymptotic root theorem. It specifically tests whether AA4-O's pinned S72 f0 with internal charge 23 and no improving 2-source swap has an improving 3- or 4-source *coherent* exchange, or whether even those stronger local neighborhoods remain trapped. In either case compare to the pinned true globally injected alternate f1 with charge 14 (AA4-O): a radius-4 optimum has no right to assert global optimality unless a wholly separate global certificate is obtained.

## 4. Exact verification, adversarial fail-closed rules and scientific next proof step

All physical cycle sets, source-point bijections, full original 45-incidence W32 model and original g/tensor are reproduced from frozen parent code. The new tests include independent original-source-factor brute enumeration of 15,015 possible five-point keys, all 105 original AA4-O swap gradients independently compared to exactly enumerated k2 changes, full 720-coordinate orbit cost checks, exhaustive k3/k4 neighborhoods, fail-closed noncanonical point labels and noninjection, all four original fixture baseline right maps, and two exact 62,370-candidate full-original GF5 checks per scheme for the k2/k3/k4 neighborhood winners.

**Result-classification constraint:** an exact radius-4 neighborhood minimum is not a GLOBAL full-injection minimum. Even if \(I_L^{BA,\mathrm{int}}>0\) for all 13,300 maps, that does not prove an all-\(f,g\) lower nor rule out one full-point assignment at Hamming distance >=5 with zero charge. The original full seven-family S may move in the opposite direction from BA internal charge as AA4-O already demonstrated. Root Branch A/B, full R3/ASET exponent, original #230 OPEN.

**Next mathematically productive step (D6-AA4-Q):** Use this exact physical-root dual to design a bona fide lower-bounding global assignment relaxation for all \(V\) original point sources, with either a hard obstruction guaranteeing positive five-support original weights under every full injection, or a genuine globally injected infinite low-charge counterfamily. Avoid treating k-exchange local stationarity and average-in-f positivity as minimax certificates. Source-specific genuine physical image C4s and original tensor coefficients must remain coupled, not independently optimized surrogate columns. The exact W32 13,300-point coherent neighborhoods serve as regression tests for candidate valid inequalities and global assignment relaxations, not as an all-h proof.
