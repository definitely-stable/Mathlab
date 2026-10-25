# HYP-105 / issue #230 — D6-P exact seven-positive ORIGINAL right-label cylinders

**2026-10-13. Model-equivalent restricted theorem C / OPEN_WITH_FORMAL_BLOCKER.** Base is all-four-GitHub-hosted-green D6-O Draft PR #414 at pinned HEAD `0c8343865b4339da0e54f881801c2c057ea5aeb8`. Do not modify main or merge stacked PRs. Root #230/#176/#169 remain open. Independent mathematical review and exact-final-HEAD hosted Research acceptance are required.

## 1. Why the next theorem cannot merely generalize D6-O's six-line support sum

D6-M gave an exact C-left/A-right right-random expectation; D6-N gave its exact second moment; D6-O computed mixed B-left/A-right plus C-left/A-right covariance. Those two directions are structurally special: both have **six distinct ORIGINAL right factor lines** and the right condition is simply that their unordered physical g-image *set* forms a six-edge A 2-factor.

The full accepted seven family has both original endpoint repetition and **column-to-column alignment** requirements. Replacing each original six-incidence set by its six-right-line *unordered support* is **insufficient for D6**: for two physical A 2-factors, D6 requires the six original incidence-column dual adjacency edges to agree as a single C6, not merely the existence of physical A graphs. This information remains necessary even when all six ORIGINAL right lines are distinct. The B/B overlap/disjoint sectors additionally require remembering whether the incidence positions of the repeated ORIGINAL left point and repeated ORIGINAL right line intersect. The disjoint ORIGINAL sixsets must not be identified by a physical automorphism or by their ten signed GF5 events.

A minimal synthetic non-GQ test makes the information loss explicit: fix six incidence positions with a physical left C6 and exactly six ORIGINAL right line identities. Permuting two right physical pair labels **preserves the unordered right physical A six-edge set** and the full right-original support, but changes the column-dual C6 adjacency alignment and hence can toggle D6. This is a structural information counterexample, not a finite or infinite original GQ Branch B counterexample.

## 2. ALL-h original-incidence deterministic cylinder identity

Fix any s=2^h, h>=1, the actual ORIGINAL W(3,s) incidence graph, and any complete globally injective left point map f and right line map g into unordered coordinate-pair labels of minimal K_a, K=binom(a,2)>=V=(s+1)(s²+1). Consider every unordered six-subset Q of **DISTINCT ORIGINAL incidences** whose LEFT physical projection occupies exactly six coordinate symbols, each twice. Its left original factor multiplicity type is necessarily A=(1^6), B=(2,1^4), or C=(2^3), since f is injective and each physical pair contributes both endpoints. There are no other possible types: threefold reuse of any physical pair would force some coordinate degree >=3.

Order the six original incidences of Q by immutable ORIGINAL incidence IDs. Define a **right cylinder signature** tau_f(Q) consisting of the following finite data:

1. left original multiplicity kind A/B/C;
2. the **ordered six ORIGINAL right factor line identities** in those incidence positions, repetitions **retained**;
3. if left kind A, the left physical six-coordinate column-dual pairing among six incidence positions, provided this pairing is a connected C6 (otherwise an empty marker);
4. if left kind B, the positions of its repeated ORIGINAL left factor point (an unordered pair of local incidence positions); otherwise empty.

Let m_f(tau) be the number of genuinely different ORIGINAL incidence sixsets whose signatures agree. For any globally injective complete g, let chi_tau(g) be the exact accepted GF5-positive seven-class tag obtained by checking the physical right half (six-coordinate 2-regularity and original right multiplicity A/B/C), the stored left A column-dual against right A column-dual for D6, or the stored left B repeated positions against right B repeated positions for B/B. It takes **one of seven mutually exclusive tags or none**. Because identical signatures retain every datum on which the accepted classifier depends, for ALL finite h, ALL globally injective f,g:

    S_seven(f,g) = sum_tau m_f(tau) * 1[chi_tau(g) is accepted]
    51^6 * R3_selected_positive_lower(f,g)
        = sum_tau m_f(tau) * R3_CERTIFIED_FLOORS[chi_tau(g)]

where the coefficient of the none tag is defined to be zero. This is a **model-equivalent exact all-g identity**; it does not establish a nontrivial positive lower bound for the sum. The GF5 weights are the accepted lower-floor coefficients 5643, 45600 twice, 43320, 49050, 51750, 45010; this expression is only the previously known **selected necessary lower contribution**, NOT total GF5 R3.

**Proof of the identity:** The input Q original sixset is unique and has exactly one stored cylinder. On each side, the physical six-coordinate test depends only on the original factor endpoint sequence and its physical pair images; f fixes the left type and the local column-dual, while g fixes the right type and its local column-dual. Every accepted sector is decided as follows:

| Left original physical kind | Right original physical kind | Accepted GF5 sector |
| --- | --- | --- |
| B | A | B-left/A-right |
| A | B | A-left/B-right |
| C / A | A / C | C/A (both orientations) |
| C / B | B / C | C/B (both orientations) |
| B | B | B/B-overlap if repeated ORIGINAL point and line share an incidence position; else B/B-disjoint |
| A | A | D6 if the stored left and newly computed right six-column dual C6 are identical; otherwise none |
| C | C | no certified seven-positive class |

This includes all seven accepted tags and no extra event. Summing m_f over accepted cylinders counts each original six-incidence subset once; the weights are class constants from the frozen GF5 registry. Physical coordinate automorphisms or sign assignments are never multiplied into the count.

## 3. New exact ORIGINAL right transposition-boundary theorem

Fix f and right g. Let g^(uv) denote the full complete right injection obtained by swapping the pair labels of two **distinct ORIGINAL right line vertices** u and v, with every other right label unchanged. Define the (right) cylinder boundary

    B_uv(f) = {tau : u occurs in tau.right_lines OR v occurs in tau.right_lines}.

Any cylinder outside B_uv(f) sees **identical right labels at all its ORIGINAL right endpoints**, so its chi indicator and GF5 selected weight are unchanged. Therefore the exact change under an actual global label transposition is

    Delta_uv S = sum_{tau in B_uv(f)} m_f(tau)
                     (1[chi_tau(g^(uv)) accepted]-1[chi_tau(g) accepted]),

    Delta_uv GF5_floor_num = sum_{tau in B_uv(f)} m_f(tau)
                     (weight[chi_tau(g^(uv))]-weight[chi_tau(g)]).

This is exact for ALL finite h, ALL f,g, all original right transpositions; the algorithm builds a sparse inverted index by **ORIGINAL right line IDs** and evaluates only affected cylinders, not all original sixsets.

**Critical sharpening and trap:** For the directed **B-left/A-right and C-left/A-right** classes (six DISTINCT right ORIGINAL lines), if **both u and v are present** in a cylinder, their transposition merely permutes the same six distinct right PHYSICAL pair edges. The right A indicator is unchanged and that individual class cannot change. But this strengthening is **FALSE for full seven S**, particularly D6, since the correspondence between original incidence positions and the right physical column-dual changes even though the unordered right physical pair set is identical. The correct full-seven update boundary is the union **at least one** u or v, not symmetric difference of supports.

This exact sensitivity statement is useful for deriving eventual deterministic swap-energy inequalities and for searching correlated suppression witnesses, but an absence of improving one-swap moves is only a local certificate; it is **not** an all-h lower bound or global optimality theorem.

## 4. Independent real-original acceptance and finite limitations

Only the **finite executable oracle** is restricted to genuine complete W(3,2) bijections: 15 original point factors, 15 original line factors, 45 distinct original incidences, 6 physical coordinate symbols. For each lex/reverse/S68/S72:

- Freeze all 62,370 genuinely distinct LEFT-selected original sixsets: A=51,030; B=10,935; C=405. Group by incidence-position-aware right cylinders, retaining integer multiplicity m_f.
- Compute every seven-class multiplicity and the weighted selected GF5 lower numerator **independently of the existing seven-class right classifier**. Compare exactly with the existing independent full original W32 seven_census oracle (all seven tags, S, and class weights); fail closed.
- For 4 pinned original right-factor swaps per map, use the cylinder inverted index for deltas, and independently rerun **the full previous seven-GF5 six-incidence classifier** on the swapped global right injection. Verify every one of seven deltas, total S and GF5 weighted floor numerator exactly.
- Audit all 105 possible ORIGINAL right-factor-pair physical-label transpositions of each genuine W32 right map through exact right-cylinder local increments. Report number of decreasing/increasing/unchanged swaps, extrema of S and GF5-weight changes, and cylinder compression. These counts are **finite exploratory data only**. A fixed-right transposition changes globally one complete g bijection to another.
- Reconcile B-left/A-right and directional C-left/A-right actual counts independently with D6-O original six-right-line support oracle, which is not sufficient alone to classify D6 or B/B. Explicit synthetic positional-D6 falsifier demonstrates why.
- No complete ORIGINAL W(3,4)/W(3,8) seven-class S claimed; no extrapolation of swap minima from h=1 to all h.

**Next genuine Branch A / Branch B proof gate:** find an all-h lower bound on the sum of these accepted seven-cylinder indicators that holds for **all** globally coherent f,g, or a rigorously described infinite coherent counterfamily yielding o(s^6). In particular, any proposed argument based only on the unordered six-right-line supports of B/A and C/A must justify why omitted positional A/A D6, B/B and opposing orientations are not essential. The new model identifies the exact lost information and makes correlated suppression testable without treating marginal class masses as independent.

## Acceptance

Files: `research/hyp105_issue230_d6p_seven_cylinder_swap_audit.py`, `research/test_hyp105_issue230_d6p_seven_cylinder_swap_audit.py`, and `.github/workflows/hyp105-issue230-d6p-seven-cylinder-swap-audit.yml`. No merged PR or main change. Require exact PR-head dedicated contract, INDEX, Proof Audit and full Research GitHub-hosted SUCCESS, plus independent mathematical peer review before considering acceptance. Root #230/#176/#169 remain OPEN; neither PROVED_A nor COUNTEREXAMPLE_B; no ASET exponent.
