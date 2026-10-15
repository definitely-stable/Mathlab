# HYP-105 / issue #230 — D6-AA4-Q: exact two-sided ORIGINAL incidence join for all seven GF(5) families

**Scientific scope: NEW exact all-h two-sided positional GF(5) seven-class identity, a genuine all-h ORIGINAL GQ C/C obstruction by incidence-girth eight, and independently implemented exhaustive W(3,2) source-first/right-first 3×3 half-projection join. This is NOT the HYP-105 all-h Ω(s⁶) lower, nor an exact full GF5 R3/ASET theorem.**

Research-only Draft stacked on all-4-CI-green [D6-AA4-P / PR #472](https://github.com/definitely-stable/Mathlab/pull/472), parent exact SHA \`78f4748969c0f7e783cdb641bb07e589c004e882\`. No writes/merges to \`main\`; issue #230 OPEN.

## 1. Why global seven-class coupling rather than optimizing the B/A internal component

D6-AA4-O/P derived the exact source-quintic B(point)/A(line) true-original GF5 *internal line-pair charge*, then proved via real W(3,2) globally injected full maps that reducing that single charge may INCREASE total seven-class original GF5 S. Specifically, fixed original line g on true W32 S72, baseline full map \`I_BA_internal=23\`, \`S_seven=72\` is one-swap stationary; a valid globally injected full point map has \`I_BA_internal=14\`, yet \`S_seven=102\`. AA4-P completely enumerated 13,300 full globally coherent source point maps within exact Hamming changes 2/3/4 around S72, confirming that the first improving point-exchange support size is 3, best k4 internal charge17 while full S=92; there is no global all-15! minimum certificate. A source-charge-only objective is therefore NOT interchangeable with all-seven positive-Q minimax.

The correct next object is the **intersection of the two independent physical source half-projections on the SAME six original incidence positions**, with the complete seven-class positional labels, including D6's aligned dual-cycle requirement.

## 2. New all-h exact source/physical **two-sided join identity**

Fix ANY finite true ORIGINAL symplectic W(3,s), s=2^h>=2, and ANY two separately globally injective complete maps f: ORIGINAL points → physical unordered K_a edges and g: ORIGINAL lines → physical K_a edges. Let E be the actual set of true original point-line incidences (not physical paths or a synthetic 6-column proxy).

For each six-DISTINCT-original-incidence subset Q ⊂ E define the true original point-factor multiplicity profile and physical 2-regular six-coordinate projection on f. Call its type \`kind_P(Q)\` when this projection has EXACTLY six distinct physical coordinate symbols of degree 2 and original source factor multiplicity A=(1,1,1,1,1,1), B=(2,1,1,1,1), or C=(2,2,2). Define \`kind_L(Q)\` independently using the SAME Q and the complete physical original line map g.

Let \(\mathcal H_P(f)\) denote every actual Q for which kind_P∈{A,B,C}, and \(\mathcal H_L(g)\) every actual Q for which kind_L∈{A,B,C}. The only relevant simultaneous Q are in the **exact original incidence-ID join**

\[
J(f,g):=\mathcal H_P(f)\cap\mathcal H_L(g).
\]

Define \(\mathcal A_{AA}(f,g):=\{Q\in J:kind_P(Q)=kind_L(Q)=A\}\). Each such original six-incidence Q carries TWO coordinate-to-original-six-column-position dual simple 2-regular graphs, one from each physical source map. The accepted historical D6 criterion is EXACTLY that these two six-position coordinate-duals COINCIDE as edge multisets and that the common graph is a SINGLE connected 6-cycle. Let D(f,g) denote those accepted aligned connected AA configurations.

Then, for ALL true original W(3,s) and ALL globally coherent full f,g, the seven accepted GF5-positive structural original sixset count is

\[
\boxed{S_s(f,g)=|J(f,g)|-|\mathcal A_{AA}(f,g)|+|D(f,g)|.}
\]

Proof requires one genuine geometry lemma and the historical seven-class structural acceptance definition:
1. All accepted seven-Q have six different ACTUAL original incidence IDs, and belong to J by their independently verified A/B/C projections.
2. If kind_P=kind_L=C, each ORIGINAL side has exactly THREE source factors, each repeated exactly TWICE among the SAME six original incidences. These six actual original incidence edges form a simple 2-regular bipartite graph on 3 original point factors and 3 original line factors, hence a **six-cycle in the ORIGINAL GQ incidence graph**, which is impossible because every genuine generalized quadrangle incidence graph has girth 8. Therefore the actual original C/C simultaneous sector is EMPTY for every s, f, g.
3. Every simultaneous pair of types EXCEPT A/A and excluded C/C belongs to the accepted historical seven-class source/physical partition: (A,B) and (B,A) are oriented one-cherry, (A,C) and (C,A) are pooled C/A, (B,C) and (C,B) are pooled C/B; B/B splits into overlap and disjoint according to whether the unique repeated ORIGINAL point and line share ONE of the six actual selected incidences (two different original incidences with the same point-line factor pair would contradict source simplicity).
4. In the AA sector only exactly the connected column-dual coincident Q belong to D6; all other original AA Q are UNACCEPTED, regardless of physical 2factor marginals.
5. Every accepted Q is counted EXACTLY ONCE in the set intersection; no positive Q is counted twice under its seven tags.

The corresponding exact CERTIFIED seven-family GF5 selected numerator is

\[
W_{\mathrm{7GF5}}(f,g)=
\sum_{Q\in J(f,g)} w(\operatorname{tag}(Q))\,1_{\operatorname{tag}(Q)\in\mathcal T_7}
\]
where w is the already accepted certified 51-palette class numerator floor map \`R3_CERTIFIED_FLOORS\`. This remains a selected floor, not the exact full R3. Both \(S\) and \(W\) preserve all true original six-incidence positions, physical coordinate labels and full globally reused maps f,g.

**Root hypothesis not solved:** The equality reorganizes the positive-GF5 count but gives NO lower on |J|−|AA|+|D6| for arbitrary complete injections. In particular source-half marginal counts and their independent random-map average cannot be multiplied or used as a deterministic lower on J. This is a precise all-h **global coupling** object for future proof methods, not a new Ω(s⁶) inequality.

## 3. All-h exact source-half A/B/C **marginal count formula**

Write d=s+1 for the ORIGINAL GQ source factor incidence degree. For a fixed globally injected typed physical source-factor edge map h (point side or line side), let:
- N_A(h) be the number of SIX DISTINCT *occupied physical edges* forming a 2-regular six-coordinate physical graph (a simple C6 or two triangles);
- N_B(h) the number of occupied physical configurations consisting of ONE repeated source factor physical edge and FOUR other DISTINCT occupied physical edges forming a C4 on the other four physical coordinates;
- N_C(h) the number of occupied physical matchings of THREE distinct edges covering exactly six coordinates.

Every physically allowed source pattern chooses a UNIQUE set of original source factors via the inverse of one complete h. For each of its original source factors, ORIGINAL incident flags can be chosen independently from the d actual original incidences at that factor (point versus line), subject to within-factor multiplicity: each of six unique factors has d choices for A; a B root has C(d,2) distinct flag pairs and four others d single choices; three C sources each have C(d,2) ways of choosing a pair of actual flags. Since each original six-incidence Q has a unique source multiplicity type and physical occupied factor edge-pattern, these counts are EXACT:

\[
\boxed{
|\mathcal H_t^A|=N_A(h)d^6,\quad
|\mathcal H_t^B|=N_B(h)\binom d2 d^4,\quad
|\mathcal H_t^C|=N_C(h)\binom d2^3.
}
\]

These hold for ANY all-h true original GQ and globally injective h; they do not require all physical edges occupied. They only use the genuine original incident factor degree d and correct physical occupied patterns. They remain ONE-SIDE counts, not guarantees of any joined pair of real original Q.

For the minimal full-K6 W(3,2) case, each type map h is a bijection to ALL 15 physical K6 edges. Exactly 70 occupied simple six-edge 2factors, exactly 45 doubled-edge/C4 configurations, exactly 15 perfect matchings. With d=3, each type **independently** and **for EVERY full h** therefore admits

\[
\boxed{(|\mathcal H_t^A|,|\mathcal H_t^B|,|\mathcal H_t^C|)
=(70\cdot3^6,\;45\cdot\binom32\cdot3^4,\;15\cdot\binom32^3)
=(51\,030,\ 10\,935,\ 405),}
\]
total 62,370 distinct six ORIGINAL incidence subsets on EACH side. The two sets H_P,H_L are defined on the SAME original 45-ID universe, so their intersections can vary drastically with globally chosen f,g although these unilateral marginals are CONSTANT.

This produces a rigorous **marginal-only nonidentification result**: true full W32 global maps with identical complete half-side A/B/C populations can have wildly different seven-family counts, e.g. pinned S68 S=68 versus lex S=259, both original GQ and globally typed-injective complete K6. Thus the independent half marginal quantities alone cannot reconstruct the joint seven count or classify a map's global exact minimax behavior. This does not rule out valid stronger all-h inequalities that use ORIGINAL positional incidence correlations or complete-map injectivity.

## 4. Independent executable TRUE original two-sided 3×3 and full seven-class joint oracle

The new Python module does NOT use historical \`selected_left_six\` to generate its candidate Q. It separately enumerates both ORIGINAL point-side and original line-side six-incidence candidates by:
- physically enumerating all 70 different six-edge K6 degree-two 2factors, then taking one genuine original incidence ID per each of six distinct occupied source factors → 51,030 original A sixsets per side;
- independently enumerating 15 repeated physical-edge roots, 3 different C4 subgraphs of its complementary physical K4, choosing two actual original incidence IDs at the repeated original source factor and one at each of four other source factors → 10,935 original B sixsets per side;
- enumerating all 15 perfect physical K6 matchings, then choosing two actual original incidence IDs at each of three distinct original source factors → 405 C sixsets per side.

Each generated original Q is six DIFFERENT ACTUAL original incidence IDs; no source local relabelings or independent physical Q choices. Independently assert NO duplicate within a source half and both full globally injected K6 maps.

Intersect the TWO dictionaries \`{true_original_6_ids: kindP}\` and \`{same_true_original_6_ids:kindL}\`, construct the actual nine-cell A/B/C × A/B/C *joint original Q matrix*, with exact zero C/C. Independently compute connected coincident column-cycle D6 on the original six incidence **POSITION IDs**, pool C/A and C/B orientations but preserve orientations in matrix, and split B/B-overlap/disjoint by repeated ORIGINAL source endpoint IDs rather than physical coordinate overlap. Count each original positive Q ONCE for all seven accepted GF5 class tags and sum its independently accepted \`R3_CERTIFIED_FLOORS\` 51-palette numerator weight.

**Two logically independent oracles:** (1) direct half-by-half exact source-factor physical enumeration and ORIGINAL sixset map intersection, independent from the previous one-sided historical enumerator; (2) full historical \`seven_census(model,independent_checks=False,witness_sets=True)\` over all 62,370 left-side original Q candidates, independent per-Q classification and selected GF5 floor. Compare total S, all SEVEN tag counts, the EXACT original set→tag map when \`collect=True\`, and full selected certified GF5 numerator. Require *identity* \`S=joint_intersection - rejected_AA\`. Test pinned real W32 schemes \`lex\`, \`reverse\`, \`S68\`, \`S72\`, five independently randomly shuffled BOTH full K6 injections, and the AA4-O genuine S72 globally point-injective witness at the SAME original right g: original S72 \`S=72\` vs witness \`S=102\`. The two side marginal triple counts remain identical even though joined S changes.

The complete 3×3 joint matrix is evidence about ORIGINAL two-sided source/physical coupling; it must not be interpreted as independent Bernoulli half events, source-girth-only geometric control, or a universal lower across all s.


### Exact genuine ORIGINAL W32 3×3 joint-veto numerical certificates

Independent dedicated GitHub-hosted first run [#38680578506](https://github.com/definitely-stable/Mathlab/actions/runs/38680578506) is **SUCCESS all 3 jobs**, including seven independently coded tests, the separately evaluated full S68/S72 two-half matrices, and independent historical full 62,370 original GF5 classification. The exact separately recalculated 3×3 source joint and D6 veto scalar data are:

| Genuine globally injected W32 scheme | ORIGINAL six-ID two-half join | A/A joint | true connected coincident A/A D6 | rejected unaligned A/A | accepted seven S | certified 51-palette numerator |
|---|---:|---:|---:|---:|---:|---:|
| S68 | 331 | 263 | 0 | 263 | 68 | 3,112,510 |
| S72 | 358 | 286 | 0 | 286 | 72 | 3,283,610 |
| lex | 623 | 379 | 15 | 364 | 259 | 11,225,795 |
| reverse | 478 | 312 | 3 | 309 | 169 | 7,627,209 |

For S68: exact A/B=21, B/A=44, B/B=3, all A/C,C/A,B/C,C/B,C/C=0, true D6=0. Thus total S=21+44+3=68, but the *pure join* count is 331, almost FIVE times larger. For S72: A/B=31, B/A=36, B/B=3, C/A=2, all remaining non-AA cells zero, D6=0. Hence exact S=31+36+3+2=72 from the intersection 358. For lex, the A/A population 379 includes exactly 15 truly aligned D6, with remaining 364 rejected, and total S=259.

This is a particularly important new **mathematical transfer obstruction**: even if one could prove a large all-h bound on the RAW intersection \(|\mathcal H_P(f)\cap\mathcal H_L(g)|\), subtracting up to almost all of its unaligned A/A members can destroy its contribution to the seven-GF5 lower. One must bound either the **NON-AA joint** contribution or the exact connected coincident D6 agreement mass (or both), not merely the raw joined-sixset count. Large, exact per-side source physical A/B/C marginals do not help without the true original six-ID cross-correlations.

The independent fail-closed test also uses a SYNTHETIC **non-GQ** six-incidence cycle \((p,\ell)=(0,0),(1,0),(1,1),(2,1),(2,2),(0,2)\). Separate true-injective physical source labels \(0\mapsto(0,1),1\mapsto(2,3),2\mapsto(4,5)\) produce **C/C** physical degree-two projections on six coordinates for this fake source triangle. Therefore C/C is NOT excluded by physical half degree-two constraints or injections alone: the **genuine ORIGINAL GQ girth-eight axiom is necessary**. The fake source 6-cycle is never passed off as an actual original W(3,s) witness or proof about actual GF5 risk.

## 5. Acceptance, negative controls, and next rigorous research

Four additive research files: two-sided independent source join algorithm, independently authored unit tests, this all-h symbolic proof and scientific scope note, and dedicated three-job GitHub-hosted workflow with S68/S72 matrix jobs plus independent global all-seven oracle unit tests. All work remains on a new stacked D6-AA4-Q research branch; main untouched, draft only. Final exact SHA must pass dedicated, INDEX, Proof Audit, and full Research before technical acceptance, and independent mathematical peer review must still audit the general GQ incidence-girth argument and the all-h GF5 seven-tag structural definition.

**OPEN_WITH_FORMAL_BLOCKER:** This stage gives a correct exact reformulation, true original C/C exclusion, and an independently tested all-seven positional join. It does NOT prove every global f,g has positive \(S_s\), let alone \(S_s\ge c s^6\); does not prove full R3/ASET exponent; does not construct an infinite Branch B counterexample.

**Next D6-AA4-R:** Seek a TRUE lower bound on the simultaneously consistent original six-incidence **join \(|\mathcal H_P(f)\cap\mathcal H_L(g)|\)** after removing the nonaligned AA obstruction, or a true all-h complete globally injected counterfamily. Exact original source 3×3 overlap matrices and D6 cycle agreement are the correct two-type observables for a mathematical global certificate. A purported LP/SA/entropy relaxation must preserve shared original six incidence IDs, one f and one g across all Q, and globally injected physical edges. In particular, two separate exact half marginals do NOT imply the required joint positive lower. Continue to compare with JPKC original incidence support tensors and EICE-003 source-square and PR #466 local barrier countermodels before asserting any transfer theorem.
