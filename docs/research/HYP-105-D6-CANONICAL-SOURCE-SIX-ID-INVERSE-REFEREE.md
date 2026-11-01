# HYP-105 / #230 — AA4-D6INV: constructive canonical ORIGINAL six-ID inverse and ordinary-C6 source-lifting referee

**Scientific Draft**, stacked on frozen [#698](https://github.com/definitely-stable/Mathlab/pull/698), exact parent HEAD \`5b7627084d7505ee0c08676734ca60397c8a928a\`. No ancestor/main modifications, no merges, no root #230 closure. Scientific status remains \`OPEN_WITH_FORMAL_BLOCKER\` pending qualified review of the complete all-map theorem.

## 1. Scope and novelty: independently re-prove, do not rename the earlier theorem

The physical coordinate-rainbow six-cycle ↔ accepted ORIGINAL D6 six-incidence-ID correspondence is ALREADY a theorem of [#652](https://github.com/definitely-stable/Mathlab/pull/652), documented in \`HYP-105-PHYSICAL-RAINBOW-C6.md\`. Later #659/#684/#691/#696 apply this after source conflict selection and two typed binary cuts. This slice does NOT claim the bijection was newly discovered.

The new referee closes a different proof obligation: it gives an explicit **SOURCE-FIRST, six-flag edge-labelled canonical inverse** that makes no search through the physical graph, and contrasts it with an independent **PHYSICAL-FIRST real six-vertex DFS**. It proves the no-cherry/two-cut graph property as a separate condition, tests the necessity of that condition, and checks the inverse on **unpaired ordinary physical subgraphs** where each original flag may contribute only one diagonal. These are genuine all-h structural lemmas; finite W32/W34 checks are falsifiers, not asymptotic evidence.

Throughout take the TRUE ORIGINAL symplectic \`W(3,2^h)\` with V=(s+1)(s²+1) original source points and V source lines, and all N=(s+1)V genuine incidence IDs. Fix complete **separately globally pair-injective, potentially maximally correlated** labels \`f:p↦{x,z}\`, \`g:ell↦{y,w}\`. Every actual source flag \`(p,ell)\` contributes precisely the real physical diagonals \`(x,y)--(z,w)\` and \`(x,w)--(z,y)\`. Because f and g are separately injective, each physical edge uniquely identifies its original source flag. There are no fabricated source IDs or cloned physical vertices.

## 2. First-principles all-h inverse directly from SIX original flag IDs

Consider a set \`S={i_0,...,i_5}\` of six DISTINCT original flag IDs. Reject it unless the six original point IDs are distinct and the six original line IDs are distinct. For each i in S retain its ACTUAL projected pair edges f(p_i) and g(ell_i). Construct independently on the **six flag IDs**:

\[
i\sim_f j\iff |f(p_i)\cap f(p_j)|=1,\qquad
i\sim_g j\iff |g(\ell_i)\cap g(\ell_j)|=1.
\]

Reject unless the six f-edges span exactly one **simple connected six-edge C6** on six distinct LEFT physical symbols: every physical left symbol has degree 2 within those six source-labelled edges. Apply the SAME condition independently on the RIGHT physical symbol pairs. Reject unless the two resulting **edge-ID adjacency graphs coincide exactly** on the same six original IDs:

\[
\boxed{\sim_f=\sim_g,\quad
\text{both are ONE connected six-cycle of named edges.}}\tag{INV1}
\]

This is precisely the historical D6 requirement of identical named-column adjacency on point and line projections. It does not merely test the two unordered projected graphs separately: two cycles with DIFFERENT edge-label orders must be rejected.

If (INV1) passes, order the six original flag IDs cyclically \`i_0,i_1,...,i_5\` starting with smallest ID and the smallest neighbor. For each consecutive pair define the UNIQUE physical corner

\[
\boxed{
v_j=
\big(
 f(p_{i_j})\cap f(p_{i_{j+1}}),
 g(\ell_{i_j})\cap g(\ell_{i_{j+1}})
\big),\qquad j\bmod 6.
}\tag{INV2}
\]

Both intersections consist of EXACTLY one coordinate. Because each projected side is an ordinary C6, the six first coordinates are distinct and the six second coordinates are distinct. For every j, the ACTUAL physical edge \`v_{j-1}--v_j\` is one of the two diagonals of the genuine source flag \`i_j\`, since its first coordinate pair is EXACTLY f(p_{i_j}) and its second EXACTLY g(ell_{i_j}). Thus (INV2) constructs one true physical coordinate-rainbow simple C6.

**Uniqueness (the acceptance-critical property).** Any other coordinate-rainbow physical C6 with exactly the same six original owner IDs projects to the same six ORIGINAL named edges on each side. Their left-side six-edge C6 forces the cyclic order of source IDs up to dihedral symmetry. For every adjacent named pair of original flag IDs, both shared coordinate symbols are uniquely determined by f/g pair intersections. Hence its physical six vertices are FORCED to be the six pairs (INV2). Cyclic rotation/reversal yields the same UNORIENTED unrooted physical C6. This proves an injective map

\[
\boxed{
\{\text{physical coordinate-rainbow C6}\}
\hookrightarrow
\{\text{distinct genuine ORIGINAL six-ID D6}\},
}\tag{INV3}
\]

and source-first reconstruction proves the inverse when all BOTH diagonal physical edges are present. If a smaller physical subgraph F contains only some original diagonals, the inverse cycle may be missing, but uniqueness of a cycle **already present** still gives the injection (INV3). Hence it is NOT necessary to preserve both diagonals in the balanced chunk F.

In fact the inverse construction is **purely combinatorial** for any original SIMPLE incidence relation with separately globally injective f/g. The special symplectic W(3,s) geometry is required for the dense/heavy population bounds, not for the inverse itself. In true W32/W34 tests, all source flags are loaded from the actual geometry; arbitrary toy relations are used solely to exhaustively falsify the combinatorial inverse.

## 3. Separate all-h proof: why selected *ordinary* C6 automatically satisfies (INV1)

An unselected FULL original physical graph H may have many ordinary C6 with repeated physical coordinate symbols. Therefore ordinary C6(H) **does NOT** automatically lower-bound original D6. This distinction was proved in #652 and remains essential; e.g. actual ORIGINAL W(3,2) lex has 730 ordinary physical C6 but only 15 coordinate-rainbow D6.

Now take the EXACT selected ORIGINAL flag ID set I of #659/#684/#696 satisfying:

* **no original source conflicts**: two selected flags with the same ORIGINAL point p have pairwise disjoint right physical labels g(ell); two selected flags with the same ORIGINAL line ell have disjoint left labels f(p);
* **two complete typed binary color cuts**: every selected original flag's two f(p) symbols have opposite left colors, and its two g(ell) symbols have opposite right colors;
* both real physical diagonals of EACH original retained flag belong to the selected whole graph G, and any physical F considered later is a simple edge-deletion/vertex-deletion subgraph of G.

**Original no-cherry lemma:** at any ACTUAL physical corner v=(x,y), no two distinct adjacent physical neighbors can have the same first coordinate. If they did, the two contributing real selected flags would have exactly the same unordered first physical pair \`{x,x'}\`, and global injectivity of f would force the same original point p. Since both edges touch v with right coordinate y, the two original line labels would share y, contradicting the exact selected original point-pencil conflict-free property. It cannot be the same original flag because its two physical diagonals are vertex-disjoint. The proof for the second coordinate is the true point/line dual argument. Therefore any actual length-2 physical walk has distinct first coordinates at its endpoints and separately distinct second coordinates. This remains true after any edge deletions from G.

**Typed-cut cycle lemma:** every physical edge of G and F flips left binary color and also right binary color. In any ordinary simple physical six-cycle its two opposite parity classes correspond to alternating positions 0,2,4 and 1,3,5. Two corners at odd cyclic distance have opposite color on each coordinate side and hence cannot repeat that symbol. Two corners at even cyclic distance are at cyclic distance 2 (or 4), and the no-cherry lemma prohibits coordinate repetition. Thus **ALL six first coordinates are distinct and ALL six second coordinates distinct**, for every ordinary physical C6 in every actual F⊆G.

Together with (INV3):

\[
\boxed{
\#C_6(F)\le \#C_6(G)\le D_6(f,g)
\quad\text{for every actual source-coherent double-cut }G
\text{ and any ordinary }F\subseteq G.
}\tag{INV4}
\]

This is the exact structural type/source bridge needed for the external ordinary graph supersaturation theorem in the heavy-tail branch. There is no assumption that F itself retains whole source flags or paired diagonals, is regular, is a generalized quadrangle, or satisfies an independent selected-source conflict condition beyond being an actual subgraph of G.

## 4. Independent falsifiers / precise scientific limitations

The NEW standalone implementation \`research/hyp105_d6_canonical_source_six_id_inverse_referee.py\` imports only the true ORIGINAL source generator \`genuine_source\` (for W32/W34 fixture loading). It DOES NOT import #652's rainbow C6 oracle, #691's codegree C6 oracle, #696's source-sector selector or the historical GF5 classifier in its proof logic. It:
- independently reconstructs every actual original physical flag diagonal and its ORIGINAL source owner, optionally only a real one-diagonal color-parity sector and optionally deleting arbitrary physical edges;
- independently enumerates each actual unoriented/unrooted simple physical C6 by a canonical six-vertex DFS and maps its six ACTUAL edge owner IDs to an original sixset;
- independently reconstructs from the SIX ORIGINAL owner IDs the unique possible physical C6 by comparing both named-edge adjacency six-cycles, without consulting the physical adjacency or DFS;
- checks exact agreement of the entire physical cycle, not merely counts, and verifies no two cycles share an original sixset; checks the source no-cherry plus two typed cuts are sufficient to make every ordinary C6 rainbow, and rejects invalid/coherent-claim inputs;
- tests **ALL 720** permutations of the six RIGHT named edge labels for a local original six-factor matching relation, with exactly **12** cyclic-order/dihedral-compatible permutations, checking source-first inverse ↔ physical-first C6 in each case. These toy relations are NOT spuriously treated as full symplectic GQ.
- independently audits the **TRUE original W32** full H in two correlated f/g label patterns with known exact physical counts \`730→15\` and \`485→3\`, preserving the distinction between ordinary vs D6;
- audits a TRUE protected ORIGINAL W34 16-flag K4,4 control with both real diagonals, 96 distinct original D6 sixsets, two one-diagonal color-parity sectors, and actual smaller sector subgraph with one MORE REAL edge deleted — still 60 positive distinct original sixsets;
- tests independently built true original W32/W34 conflict-free two-cut source selections for different correlated g maps and malformed/missing/duplicate source ID inputs.

**STOP:** this independently proves/certifies and makes constructive the ALREADY KNOWN all-h #652 source six-ID inverse and its source-coherent selected graph application. It is NOT a new uniform positive D6 count, does not prove the full dense-core B/B branch, does not determine numerical external ordinary C6 graph constants, and does not constitute qualified independent mathematical peer review of entire HYP-105. This result should be considered a high-confidence structural-referee slice rather than a new claim that the root theorem is complete. Leave all scientific Draft PRs unmerged and #230 OPEN_WITH_FORMAL_BLOCKER.