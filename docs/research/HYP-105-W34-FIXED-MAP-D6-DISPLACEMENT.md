# HYP-105 / #230 — AA4-FIXD6: genuine W34 same-map global D6 displacement

**Status:** exact finite original-source audit and an elementary all-h frozen-line conservation lemma. **OPEN_WITH_FORMAL_BLOCKER** for root Branch A/B/C. This document neither estimates the remaining six original GF(5) classes globally nor proves an all-h lower bound.

## 1. Gap addressed

Parent #664 establishes the **fixed-map** conditional inequality
`D6(f,g) >= 2 M(G,H(f,g))` for saturated K3,2 parents in one selected, source-ID-coherent G. Parent #665 exhibits TWO fully legal original symplectic W(3,4) maps with the *same complete point map f*, the same frozen 12 original selected source-line labels, the same twelve original selected incidence IDs and the same saturated parents, but with M=4 and M=0. Parent #666 derandomizes an **average** original line completion into a good EXISTENTIAL map. None of those results answers how much **global** historical accepted original D6 mass exists in the actually fixed ZERO completion.

This slice measures that global D6 sector exactly on BOTH unchanged fully specified W34 maps, independent of saturated parent expansions. It asks whether local cancellation can be distinguished from global six-ID disappearance without inventing edges, independent f/g label distributions or an asymptotic fit.

## 2. New all-h frozen-line conservation observation

Fix true symplectic W(3,s), s=2^h (h>=1), a minimal with choose(a,2)>=V, and a complete globally injective original **point** pair-label map f. Let g1 and g2 be two complete, separately globally injective original **line** pair-label maps, agreeing on a given subset J of original source lines. All physical labels are typed; all original incidence IDs and original source endpoint identities are unchanged.

**Lemma (exact, all h):** For ANY six distinct original incidence IDs I={ (p_i,l_i) }, if {l_i} is contained in J, the complete seven-family accepted GF(5) classifier, including the original incidence endpoint-multiplicity tags, gives **exactly the same value** (one of seven classes or rejected) on (f,g1,I) and (f,g2,I). Consequently every class's original-sixset census restricted to the sixsets using only original source lines J is **identical** between g1 and g2.

*Proof.* The six original source flags and point labels f(p_i) are the same. For every original source line in the sixset, g1(l_i)=g2(l_i). Thus both physical coordinate projections, original endpoint partition, and the historical GF(5) accepted-class predicate of the entire sixset are literally identical. This is a term-by-term equality, not a claim about random independent labels, and requires no source field symmetry.

This simple lemma is a conservation/sanity condition, **not** a global lower bound: the two completions can still change every sixset containing an unassigned original source line. The root seven-class sum can change arbitrarily outside this frozen-only sector within constraints not established here.

## 3. Two independent exact global D6 source oracles

For each completely fixed genuine original W34 map:

1. **Physical-path DFS (new):** Construct the full physical graph from ALL 425 genuine original incidence IDs, retaining BOTH diagonals per source flag and the unique directed-arc original source-ID provenance. Enumerate each simple coordinate-rainbow physical C6 exactly once: least physical corner as root and first successor smaller than last predecessor. Prune whenever either physical axis repeats. Invert each six-cycle to its six distinct original incidence IDs, require six distinct original point IDs and six original line IDs, and call the historical seven-family GF(5) classifier to require D6. Deduplicate *original* sixsets.
2. **Independent PC3 posting-list oracle (#657):** Build physical pair-common-neighbor postings and enumerate the three pair witnesses for coordinate-injective hub triples, again with source IDs and historical classifier. Each accepted original D6 appears **exactly twice** via alternating hub triples, so exact `2 D6` equals the oriented witness count. Compare its global D6 to the new DFS, including complete K3,3 versus non-K3,3 sectors.

The new DFS partitions ALL accepted original D6 by **k=0,...,6 unassigned original source-line IDs** in the sixset relative to the same J. It independently partitions by number of six original flags from the same 12-ID selected set. Summing either histogram must equal the exact global D6. At k=0, the **identical original sixsets** (not just their number) are verified for positive and zero maps, implementing the conservation lemma's D6 sector. The parent #664 source oracle separately checks both local saturated sectors, M=4 and M=0, and true two-flag accepted D6 lower sectors 8 and 0.

Every accepted original D6 is one term in the seven-family S. The certified necessary GF(5) R3 D6-only numerator is `5643 * D6` over `51^6`. This is **only a necessary D6 contribution**, not full R3 and not the exact weighted ten-sign D6 event sum.

## 4. Exact source conditions and reproducibility

- Genuine original W(3,4): 85 point IDs, 85 line IDs and 425 actual incidence IDs.
- Full minimal K14 pair-label alphabet: 91 possible physical pair labels and 85 injected labels of each source type.
- Frozen twelve selected actual source-line pair labels g_J and ALL 85 point-pair labels f identical in both maps. The 73 other original source lines are relabeled via the explicit, previously certified #665 permutation of 79 available slots; six pair slots may remain unused.
- Both maps use the same original incidence flags. All 850 physical undirected full-H edges retain their original source-ID provenance.
- An additional true W(3,2) K6 lex/relabel test checks the independent D6 inversion, exact original GF(5) acceptance and invariance of the completely frozen original sixsets.
- Noninjective physical labels and nonexistent original source-line identifiers fail closed.
- GitHub-hosted specialized test: `python -m unittest discover -s research -p 'test_hyp105_w34_fixed_map_d6_stratified.py' -v`. The exact numeric certificate is printed as `HYP105_AA4_FIXD6_CERTIFICATE=...` in the step log. Require exact-head passing specialized, INDEX and full Research checks; do not report pass before inspection.

### Expected interpretation

If the ZERO map still has positive accepted D6, then **zero saturated-parent extension mass is demonstrably not zero full-map D6**. The relative difference in the full-map D6 counts and the k-strata quantifies how unselected original line-label assignments redistribute accepted mass on these TWO actual maps. Even a large value of D6 at s=4 is finite evidence only; there is no all-h Omega(s^6) theorem. The remaining six classes might increase or decrease; this experiment does not compute them.

## 5. Specific next mathematical blocker

The original all-map conjecture asks for `inf_(f,g) S_seven(f,g) = Omega(s^6)` for all dyadic h. A local selected graph and frozen f/g_J cannot force its two-flag completion mass (#665). Even if exact full D6 remains large in the two finite W34 examples, a rigorous all-map lower certificate requires a quantitative **source-incidence correlation mechanism** for arbitrary adversarial unselected labels, or an explicit **compensation inequality for the OTHER six historically accepted original GF(5) classes**. No current local expectation, frozen conservation, finite census or positive example substitutes for that gate.

References: [root issue #230](https://github.com/definitely-stable/Mathlab/issues/230), [AA4-K32ZERO #665](https://github.com/definitely-stable/Mathlab/pull/665), [AA4-K32LIFT #666](https://github.com/definitely-stable/Mathlab/pull/666), original-source D6 identities [#652](https://github.com/definitely-stable/Mathlab/pull/652), [#657](https://github.com/definitely-stable/Mathlab/pull/657), [#658](https://github.com/definitely-stable/Mathlab/pull/658).
