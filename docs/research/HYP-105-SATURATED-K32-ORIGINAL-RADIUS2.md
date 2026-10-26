# HYP-105 / #230 — AA4-K32R2: saturated \(K_{3,2}\) six-original-flag radius-two exclusion

**Status:** rigorous restricted all-\(h\) no-go theorem on one proposed *local compensation step*, with a real complete \(W(3,4)\) eight-original-flag **sharpness witness**. The unqualified universal \(S_{\mathrm{seven}}=\Omega(s^6)\) statement remains OPEN_WITH_FORMAL_BLOCKER. This does **not** construct a Branch B counterfamily, show that saturated \(K_{3,2}\) must be numerous, or rule out compensation involving two or more changed original incidence IDs.

## 1. Motivation and actual new frontier

The immediate predecessor AA4-HALL2 in Draft PR #661 proves: in a genuine-original source-ID coherent selected physical graph, an all-codegree-\(\ge2\) left-vertex triple can avoid ordinary physical C6 **only** by being an exactly saturated \(K_{3,2}\) with the same two right common neighbors. Since every ordinary physical C6 in this graph is accepted original GF(5) D6, the hypothetical small-seven-class family must have almost all double-codegree triangles saturated (unless there are few).

The crucial next scientific issue is whether those **saturated six-edge configurations themselves**, or six-original-flag sets differing in one position, automatically transfer to one of the **other six historically accepted GF(5)** original six-incidence classes. The answer is **NO**, for a structural reason that can be rigorously proved and falsified on **true original symplectic \(W(3,4)\)**, not by substituting a source-free graph. The first potentially productive compensation must use at least **two distinct new original source flags** (or a global mechanism beyond a single saturated block).

## 2. Whole original source IDs, two physical diagonals and parity blocks

Take the **genuine original** \(W(3,s)\), \(s=2^h\), with *complete separately globally injected typed physical pair-label maps* \(f(p)=\{x_p,x'_p\}\), \(g(\ell)=\{y_\ell,y'_\ell\}\), allowed to be **arbitrarily correlated**. Select actual ORIGINAL incidence IDs \(I\) free of the #659 source-pencil conflict graph. Two separate physical symbol 2-colorings split the coordinate symbols of each used \(f(p)\) pair and each used \(g(\ell)\) pair across opposite colors. This is the original source-ID coherent selection/coordinate-cut model of PRs #659–661; both physical diagonals for every selected source ID are retained.

For each \((p,\ell)\in I\), its two physical edges join four corners:

\[
(x_p,y_\ell)-(x'_p,y'_\ell),\qquad
(x_p,y'_\ell)-(x'_p,y_\ell).
\]

The first coordinates change colors and the second coordinates change colors across either edge. The physical graph has two **disjoint color-parity subgraphs**: vertices with \((\text{first-color})\oplus(\text{second-color})=0\) and with parity \(=1\). Of the two physical diagonals from **every one original source ID**, exactly **one belongs to each parity**. Consequently, **within each parity block, all different physical edges carry different original source incidence IDs**, even though the entire graph contains both diagonals for each ID.

The selected source-pencil conflict-freeness ensures local physical coordinate properness: two different neighbors of the same physical vertex differ on both typed axes. Each physical selected edge also changes both axes and both assigned colors.

## 3. Sharp all-h saturated \(K_{3,2}\) no-go theorem

Suppose that one parity component of this *genuine-source coherent physical graph* contains a **complete \(K_{3,2}\)** with hub corners \(h_1,h_2,h_3\) and free corners \(z_1,z_2\), and all six physical edges derive from selected source IDs. For saturation in AA4-HALL2 we additionally require **no other common physical neighbor** for any hub pair, but saturation is not needed for the following exclusion theorem.

**Lemma 1 (five distinct physical coordinates).** The five corners have **pairwise distinct first coordinates and pairwise distinct second coordinates**.

*Proof.* Each free corner is adjacent to all three hub corners; by the source conflict-free physical properness, the three hubs have distinct coordinates on each axis. Each hub is adjacent to both free corners; thus the two frees have different coordinates on each axis. A first- or second-coordinate equality between a hub and any free is impossible: they are physically adjacent along an original source-pair diagonal, which changes both axes. These exhaust all pairs of the five corners. \(\square\)

**Lemma 2 (six distinct original point and line factors).** The six \(K_{3,2}\) edges come from **six distinct source incidence IDs**, and all six source point IDs and all six source line IDs are distinct.

*Proof.* The two parity components separate the paired diagonals of each original source ID, so the six physical edges in one component must have different incidence IDs. On the FIRST typed coordinate axis, the six pairs associated with these edges are exactly the six DISTINCT edges \(\{(h_i)_0,(z_j)_0\}\) of the ordinary coordinate \(K_{3,2}\). The globally injected source point map \(f\) assigns different original point IDs to all different pair labels. The same argument with SECOND typed coordinates and globally injected \(g\) gives different original source line IDs. Therefore the underlying six ORIGINAL flags form a point-line *matching* in the actual original source incidence graph. \(\square\)

**Theorem AA4-K32R2 (minimum two-ID replacement to obtain ANY seven-family acceptance).** Let \(F\subseteq I\) be exactly the six distinct original source incidence IDs underlying one such physical \(K_{3,2}\). Then:

\[
\boxed{
\operatorname{Class}_{\mathrm{GF5,seven}}(F)=\varnothing,
\qquad
\text{for every six-ID accepted }F'\text{ on the SAME }f,g,\
|F\setminus F'|\ge2.
}
\]

Equivalently, there is **no** accepted original GF(5) six-ID set with five or six IDs in common with \(F\).

*Proof.* Each original ID in \(F\) contributes a first-coordinate pair label equal to one of six coordinate \(K_{3,2}\) edges. Its six first-coordinate pairs have **five** occupied symbols with multiplicity/degree multiset \((2,2,2,3,3)\); the same holds on the second axis. Every historical one of the **seven accepted original GF(5) sixflag classes** requires **exactly six** occupied symbols on EACH axis, and each symbol must have degree **exactly two** (the A/B/C degree-two projection requirement used in the historical classifier). Thus \(F\) is rejected.

Now remove **one** source ID from \(F\), and insert **any** other original source incidence ID, with no independence, nonincidence or field assumption on that replacement beyond being a distinct actual source flag. One original source ID removes exactly one first-coordinate edge of the \(K_{3,2}\). The two original degree-three coordinates belong to the **free side** \(z_1,z_2\), which are nonadjacent, so a single removed edge can reduce the degree of **at most one** of these degree-three symbols. The other keeps degree 3. Adding one new original ID cannot reduce any coordinate degree. Thus the resulting projection has a symbol of degree at least 3, whereas every accepted historical class requires only degrees 2. Hence **no one-ID substitution can become accepted**. This already fails on the point axis alone, and also fails symmetrically on the line axis. \(\square\)

**Interpretation.** Saturated \(K_{3,2}\) configurations need not be an accepted original GF(5) motif. Even immediate source-ID *one-exchange* compensation is mathematically impossible. A proof relying on "each saturated triple directly supplies at least one of the other six accepted classes" or on "replace one selected incidence" is invalid. This is an exact source-quantified, fixed-map impossibility result, not just a synthetic physical graph example.

## 4. Even the paired physical companion edges cannot rescue the isolated six-ID block

For these six original flags, the **other** physical diagonal of each flag belongs to the opposite parity block. Write the hub first/second symbols as \(x_i,y_i\) and free symbols as \(X_j,Y_j\). The six first-parity edges are \((x_i,y_i)-(X_j,Y_j)\). Their six true companion physical edges are:

\[
(x_i,Y_j)-(X_j,y_i),\qquad i=1,2,3,\ j=1,2.
\]

By Lemma 1 the five symbols on **each** typed axis are pairwise distinct; these six companion edges have **twelve different physical endpoints**, hence form an exact six-edge **matching**. In particular the physical subgraph containing **only those six original incidence IDs** is one \(K_{3,2}\) plus a disjoint six-edge matching: it has NO ordinary C6, including no C6 arising from the paired diagonals.

This says **nothing** about additional physical edges contributed by other genuine original IDs in the complete source map. It does not claim the entire complete map has no accepted motifs.

## 5. Sharp radius-two positive recovery on actual symplectic \(W(3,4)\)

This lower exclusion is **sharp** and not a vacuous local algebraic restriction. The independent finite construction:

1. Builds the actual \(W(3,4)\) source point-line incidence list, finds **eight mutually point-disjoint and line-disjoint REAL original incidence flags** by an augmenting-path bipartite matching, and does not create any synthetic incidence flag.
2. Assigns their eight original point labels and eight line labels to the physical pair edges
\[
(0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(0,5),(1,5)
\]
on the x-axis, and the translated versions \(+6\) on the y-axis. Completes ALL \(85\) original point and line labels separately as globally distinct \(K_{14}\) edges, retaining the actual original source \(W(3,4)\).
3. The **first six** original flags produce a physically coherent saturated \(K_{3,2}\) with six actual source-ID edges, and six source-preserving companion matching edges. Exactly zero accepted source D6 arise in this selected six-ID graph. Their ORIGINAL six-ID set is rejected by the full historical GF(5) seven-class classifier.
4. The **two extra** genuine original source flags complete the six-edge primary \(K_{3,2}\) to a \(K_{3,2}\) plus one right physical vertex adjacent to two hubs. Exactly **two** simple physical six-cycles appear, each accepted as **ORIGINAL GF(5) D6**. They give TWO distinct original accepted six-ID sets, each sharing exactly four old IDs and replacing **two** old source IDs.
5. The same code enumerates **all \(6(425-6)=2514\) one-original-flag swaps** of that saturated genuine sixset against the entire true \(W(3,4)\) incidence-flag population, with the completed fixed f/g held unchanged. **Zero** classify into any of the seven historical accepted classes. This is an independent finite falsifier, not the proof of the all-h impossibility.

The construction checks both original source-ID diagonals, empty original-pencil conflict graph, the two global physical-coordinate 2-cuts, exact \(K_{3,2}\) saturation, matching companion endpoints, all six old source point/line ID distinctions, the exact original six-coordinate degrees and the historical GF(5) classifier. The known AA4-HALL2 lower bound is sharp: adding the two extra original flags produces exactly 2 positive D6.

## 6. What genuinely remains open

The root requires an \(\Omega(s^6)\) **positive count among all seven** historical six-ID classes for every full admissible correlated fixed pair f/g. The no-go theorem here only shows that **a single saturated \(K_{3,2}\) and its one-ID neighborhood** have zero accepted mass. A global concentration of such saturated configurations may still force abundant accepted motifs built from **two or more different extra genuine incidence IDs**, as the real \(W(3,4)\) sharp construction demonstrates; or may force other accepted sixflag A/B/C source patterns through interactions between MANY saturated clusters.

Therefore the next genuine P0 is a **source-ID-preserving two-exchange extension/codegree theorem**: characterize interactions among saturated \(K_{3,2}\) source matchings that generate accepted six-coordinate two-regular motif projections, and bound the resulting distinct accepted sixsets without overcounting. A naive "per saturated triple one accepted motif" or "one source swap" argument is ruled out.

**Scientific caveats:** the Hall marriage and matching facts are classical prior art; the proposed HYP-105 contribution is the same-map original-source typed projection and radius-two obstruction under the actual source incidence ID/paired-diagonal constraints. The finite \(W(3,4)\) witness is not a universal adversarial infinite family. No root theorem, no ASET exponent, no conclusion on whether the seven-class \(\Omega(s^6)\) lower is true or false. Keep child PR Draft, exact-head GitHub-hosted Research/specialized/INDEX CI and independent qualified mathematical review.
