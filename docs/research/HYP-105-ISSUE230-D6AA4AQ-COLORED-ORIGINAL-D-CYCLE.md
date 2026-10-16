# HYP-105 / issue #230 — AA4-AQ: exact TRUE ORIGINAL D6 as two-color rainbow cycles in the genuine D-pair graph

**Research-only.** Strict stacked Draft child of [AA4-AP #538](https://github.com/definitely-stable/Mathlab/pull/538), frozen parent exact HEAD \`e75b2e3df2c8959c6034e57f9596b2ec316f959e\`. True ORIGINAL symplectic W(3,s), s=2^h≥2; actual original source point/line incidence flag IDs; two complete GLOBALLY FIXED and separately typed physical injective unordered-pair maps f,g into the minimal physical K_a palette. NEVER redraw maps per selected source Q. **NO all-map S_s(f,g)=Ω(s^6), no accepted six-ID source Hall lower, no original issue #230 Branch A/B/C, no signed GF5/ASET exponent.**

## 1. Frontier after AA4-AP and novelty boundary

AA4-AP proved \`D_good(f,g)>=s^5/10\` for all genuine W(3,2^h), h>=14 and EVERY complete correlated fixed f,g. Its corresponding two-typed globally occupied P5×P5 PHYSICAL template mass is large but lacks a true-original six-flag Hall/positive selected GF5 lower. Earlier [AA4-T](research/hyp105_issue230_d6aa4t_quenched_aligned_d6.py) already proved exact positional D6 tensor overlap \`D6=∑_{H,Q} A_f[H,Q]A_g[H,Q]\`; [AA4-V](research/hyp105_issue230_d6aa4v_positional_twofactor_alignment.py) already studied same-sixposition physical twofactor adjacency intersections and 70 twofactors, and so their results are **NOT claimed new** in AA4-AQ.

**New representation:** Use only REAL original incidence FLAGS as vertices and bilateral AA4-AL D-compatible original flag pairs as EDGES. This is a global original-source/correlated-two-physical-map problem with colored paths, not separate physical half-pattern enumeration. It exposes exactly the extra geometric obstruction preventing a large number of good D pairs from forcing original selected D6.

## 2. NEW all-h exact two-colored D6 = rainbow 6-cycle theorem

Let \`I=I(W(3,s))\` be the set of genuine original distinct point-line incidence flags \`i=(p_i,l_i)\`; number of real original flag IDs is
    N=V(s+1)=(s+1)^2(s²+1).
Build a SIMPLE undirected graph \`G_D(f,g)\` on the ACTUAL original N source flag IDs, where \`{i,j}\` is an edge if and only if

1. \`p_i!=p_j\`, \`l_i!=l_j\` — truly distinct original source factor IDs;
2. original physical point pair-label images share exactly ONE coordinate: \`f(p_i)∩f(p_j)={c_{ij}}\`;
3. original physical line pair-label images share exactly ONE coordinate: \`g(l_i)∩g(l_j)={e_{ij}}\`.

A real original D edge has a UNIQUE typed physical coordinate COLOR PAIR \`(c_ij,e_ij)\`. Its total undirected graph edge count is precisely the AA4-AL genuine \`D(f,g)\`, not a random physical or source-factor graph. The vertices themselves are guaranteed true ORIGINAL incidences.

**THEOREM, exact for ALL h≥1 and EVERY globally fixed f,g:**

A set Q of six DIFFERENT actual original incidence flag IDs contributes one selected original seven-GF5 \`D6\` if and only if its six flags admit a simple undirected cycle \`i0-i1-i2-i3-i4-i5-i0\` in \`G_D\` such that ALL SIX shared physical point-coordinate colors on its six consecutive D edges are PAIRWISE DISTINCT and ALL SIX shared physical line-coordinate colors are PAIRWISE DISTINCT.

Furthermore, this compatible rainbow cycle on the six original source flag IDs is UNIQUE up to cyclic rotation and reversal. In ordered-rooted form,

    **12*S_D6(f,g) = count of directed rooted original G_D six-cycles with
                      six DIFFERENT true original flag vertices AND
                      six distinct point-edge physical colors AND
                      six distinct line-edge physical colors.**

Proof forward: genuine selected D6 means SIX distinct original source point factors and SIX distinct original source line factors mapped to physical 2regular connected C6 projections whose ORIGINAL flag-position physical coordinate-column duals coincide as the SAME sixcycle H (AA4-T). Exactly the H six position-edges join two different original source points AND lines at their common physical point and line coordinates, hence those edges belong to \`G_D\`. Both physical colored columns are six distinct real physical coordinates, therefore both edge-color cycles are rainbow.

Proof backward: every directed simple rainbow cycle has six distinct TRUE ORIGINAL flag IDs by vertex simplicity and the construction of \`G_D\`. At each cycle vertex i, the two incident D edges share two DIFFERENT point coordinates \`c_{i-1},c_i\`, because all six point edge colors are distinct. The physical pair image f(p_i) contains BOTH, and has exactly TWO endpoints, so it must equal \`{c_{i-1},c_i}\`. Thus the SIX globally fixed source point physical factor edge images constitute one connected physical C6 on six distinct point physical coordinates, and the physical coordinate-column dual adjacency graph on the six ORIGINAL incidence positions is EXACTLY the cycle H. Repeat independently on LINE physical g: the six actual original line factors form a connected C6 with the SAME position-dual H. No duplicated actual original point or line source factor is possible, since no two distinct adjacent rainbow-color pairs of six distinct colors are equal. The classifier therefore accepts precisely genuine original D6; there can be no second different rainbow cycle on the same set Q because the connected dual physical six-position graph is unique. There are six possible roots and two directions, giving factor 12.

**This is a new exact SOURCE-GRAPH REFORMULATION of the previously known all-h AA4-T positional D6 acceptance condition**, not discovery of a new positive all-map D6 bound, and the graph-theoretic rainbow-cycle concept itself is textbook.

## 3. NEW actual original directed complementary-port transport

Take any DIRECTED original compatibility D arc \`i→j\` with typed edge colors \`(c,e)\`. The next arc \`j→k\` can lie in a REAL selected D6 only if its point color is the OTHER endpoint of physical original point label \`f(p_j)\` and its line color is the OTHER endpoint of physical original line label \`g(l_j)\`. One may NOT simply choose arbitrary physical/source D neighbors of j: wrong color reuse violates the six-coordinate degree-two rule before GF5 source Hall.

This two-typed complementary-port condition forces the next REAL original incidence flag k to lie in the same-global-source coordinate CELL

    \`M[c',e']=(F^T B G)[c',e']\`,

where c' is the other endpoint of \`f(p_j)\` and e' of \`g(l_j)\`. By the CLASSICAL original W(3,s) source incidence expander-mixing SINGULAR norm (already used in AA4-AP), every such cell obeys

    \`M[c',e']<=K=d(a-1)^2/V+ceil(sqrt(2s))*(a-1)\`.

This supplies an explicit ALL-h **UPPER** on typed-color legal one-step directed D transitions, and explains exactly why merely knowing edge mass \`D_good=Ω(s^5)\` does not imply any lower on six-step CLOSED rainbow walks. The new executable algorithm first constructs D on genuine original incidence IDs, builds every edge's unique point/line color pair, enforces complementary physical endpoints and global six-color injectivity while enumerating closed simple six-walks, and canonicalizes 12 directed cycles to one real source Q. It preserves the original global f and g throughout.

Do not infer D6≥1 or S≥c*s^6 from K; a source-cell upper and many edges do not imply positive rainbow closure under adversarial physical labels.

## 4. Strong two-part obstruction: REAL finite original nonrainbow + ABSTRACT infinite extremal edge-count

**(a) Genuine finite ORIGINAL W(3,2), one full global fixed f,g:** The earlier AA4-AM W32 seven-GF5 oracle proves selected positive D6 is ZERO for S68 and S72, while their TRUE AA4-AL original D graphs respectively contain 257 and 261 undirected compatibility edges on exactly 45 real original source flag vertices. The new AA4-AQ literal simple graph DFS explicitly constructs at least ONE ordinary SIMPLE 6-CYCLE inside each of these REAL globally coherent source incidence/physical two-map D graphs. NONE is a six-coordinate two-color rainbow D6 cycle (indeed the full original D6 oracle is zero). Hence even genuine original source-incidence-compatible ordinary C6 is NOT sufficient for D6: the six DISTINCT physical coordinate colors of BOTH types and actual positional alignment are essential. These are only s=2 counterexamples; no eventual all-h failure is inferred.

**(b) Independent ABSTRACT ALL-large-h C6-free edge-mass no-go:** Before considering the colored original source geometry, perhaps one tries to prove AA4-AP D_good≥s^5/10 forces an ordinary sixcycle by graph extremal number. This is invalid as a GENERAL graph-edge-count argument, at least with the known s5 edge floor. For every integer h≥48, set \`s=2^h, q=2^(floor(4h/3)-3)\`. The classical genuine W(3,q) incidence bipartite graph has

    \`n_q=2(q+1)(q²+1)\` real vertices,
    \`e_q=(q+1)²(q²+1)\` real edges,

and GIRTH EIGHT, so NO simple C6. These classical graph constructions have

    \`n_q<=4q³<=N=(s+1)²(s²+1)\`
    \`e_q>=q^4>=s^5\`  (since \`4(floor(4h/3)-3)>=5h\` for h≥48).

Pad the abstract graph with isolated vertices to EXACTLY N source-flag-vertex-count slots if desired. This constructs an ABSTRACT simple undirected C6-free graph on the same number N of vertex SLOTS with even more than s5 edges. **It is NOT the actual G_D(f,g) for any globally injected original W(3,s) physical maps; absolutely no infinite original #230 Branch B counterexample is constructed.** Its only logically supported conclusion is that a generic graph argument using the numerical edge lower alone cannot force an uncolored C6, even before demanding TWO independently rainbow color types.

**Prior art explicitly acknowledged:** incidence graphs of generalized quadrangles have girth 8 and order roughly n~q³, edges~q⁴, giving the known extremal C6 lower order n^(4/3) (Benson 1966); Bondy–Simonovits (1974) proved the matching upper order n^(4/3). See [Erdős Problems, Problem 572, literature timeline Benson/Bondy–Simonovits](https://erdosproblems.ai/wiki/problems/extremal_graph_theory/E0572), and [Füredi–Simonovits, Extremal Graph Problems survey, §4](https://www.renyi.hu/~miki/FureSimSurvC.pdf). No novel high-girth graph construction is claimed.

## 5. Exact genuine-source independent tests and original GF5 truth

1. Five fully globally fixed true ORIGINAL W(3,2) typed physical K6 bijections dual-zero, lex, reverse, S68, S72. TRUE graph D edges are 277,307,300,257,261 respectively. The new all-source-flag rainbow D graph DFS returns EXACT accepted source D6 six-ID Q SET, independently equal ON EACH SIX-ID Q (not just counts) to earlier historical source 62,370-six-Q \`seven_census\` and separate AA4-Q \`_column_physical_dual\` original positional D6 classifier. Expected genuine D6 counts are **1,15,3,0,0**. Each reconstructed cycle is unique up to its 12 directed root/orientation walks; exact original six-ID set and true source factor inequalities enforced.
2. S68/S72 finite-source ACTUAL ordinary D-graph 6cycles are independently extracted with an uncolored DFS, while full TRUE ORIGINAL selected D6 from the separate historical oracle is ZERO. This is the strongest finite limitation of an "ordinary C6 suffice" shortcut.
3. ALL directed original D arcs in true W32 dual-zero/S68 and W34 lex/random (real GF4 symplectic W(3,4) source, two globally injected non-surjective K14 typed physical maps with 6 holes each) have independently audited exact complementary-point/line port next-step counts. Every observed count is bounded above by the independent original-AA4-AP source-cell spectral K, and sum of directed states =2D.
4. TRUE ORIGINAL W34 partial root-limited rainbow DFS samples accepted six-ID Q and independently checks actual AA4-Q original D6 dual classification on EACH generated Q. Its result is explicitly NOT a full W34 D6 census and not an original positive lower.
5. TRUE original W32 symplectic source automorphism and independently typed physical coordinate permutation preserve D edges and D6 selected counts under the fixed relabeled full global model.
6. The abstract GQ girth-eight benchmark verifies exact HUGE power-of-two integer inequalities h48..80 without pretending to materialize gigantic projective geometry.
7. Fake original source incidence IDs, non-injective physical original source factor pair maps, duplicate/invalid root requests, and unbounded full-W34 enumeration are rejected.

Versioned executable math: \`research/hyp105_issue230_d6aa4aq_colored_original_D_cycle.py\`; versioned independent test suite: \`research/test_hyp105_issue230_d6aa4aq_colored_original_D_cycle.py\`; four dedicated GitHub-hosted CI jobs and mandatory INDEX, Proof Audit, Full Research on exact frozen PR HEAD. Mathematical referee separate; strict Draft stack; do not merge to main or modify formal accepted RCP claim registry. Original issue #230 **OPEN**.

### Frozen first independent W32/W34 actual-original evidence

The first [dedicated AA4-AQ #38850559446](https://github.com/definitely-stable/Mathlab/actions/runs/38850559446) passed **4/4 GitHub-hosted jobs**. On FIVE complete global source point/line typed physical maps of actual W(3,2), every original D6 selected six-incidence-ID Q generated by the new colored D-cycle DFS was verified to match EXACTLY the independent pre-existing original seven-GF5 62,370-six-candidate source oracle, and AA4-Q six-position dual connected original classifier was checked on each witness.

| Genuine original W32 full global f,g | D edges | Exact accepted original D6 | Colored original D path extensions inspected |
|---|---:|---:|---:|
| dual-zero | 277 | **1** | 4,844 |
| lex | 307 | **15** | 9,553 |
| reverse | 300 | **3** | 7,805 |
| S68 | 257 | **0** | 2,985 |
| S72 | 261 | **0** | 3,568 |

**Concrete true-original finite ordinary-C6 but NO positive D6 witnesses:** W32 S68 original 45-flag-index physical-compatible sixcycle (0,15,1,3,2,29), and W32 S72 original flag sixcycle (0,9,2,3,1,10). Each is an ordinary genuine-original bilateral D compatibility graph C6 under one globally fixed source f,g. Every globally color-rainbow D6 original six-Q is absent on these two full original W32 models, independently exhaustively checked. The ordinary cycles do NOT satisfy the two-color six distinct coordinates requirement. This rejects the naive statement 'any genuine original D graph C6 yields accepted positive D6' at s=2, not any large-h universal theorem.

**True original W34 GF4 symplectic source**, global lex/random K14 point/line edge pair images each with six globally missing physical edges: maximum original-source physically complementary typed D-arc outgoing transition count 22 (lex), 14 (random); earlier true W32 dual-zero and S68 counts 6 and 5. The original source GQ spectral coordinate-cell K upper is 832/17 at s=4 and 15 at s=2, thus no wrong direction of spectral inequality is inferred. Explicitly TRUNCATED root-set {0,1,2} and witness-budget 3 produced 3 actual source original D6 Q per W34 lex/random, each independently verified by the earlier original AA4-Q source six-position D6 classifier. Not a full W34 D6 census.

The abstract original-GQ-girth-eight graph vertex and edge counts passed exact large-integer inequalities h48..80. This is only a GENERAL-GRAPH existence/prior-art no-go, not a pair of actual global physical source maps. Genuine source symplectic and physically independent point/line relabel invariance, fake-model controls and strict sample-scope checks passed.

## 6. Next material theorem gate AA4-AR

**A positive all-f,g original six-ID GF5 theorem still needs structural information beyond GOOD D edge mass** — for instance a nontrivial universal lower on the NUMBER of two-color RAINBOW directed closed six-walks in the **special** original-incidence globally injected bicolored D graph, or a genuine non-D6 sector U/E lower proving the full seven-family obstruction. General C6 extremal arguments are ruled out by high-girth counterexamples; ordinary true-original D cycles are ruled out as a sufficient GF5 witness by finite S68/S72. The next effort should derive ORIGINAL SOURCE incidence four-point/two-type correlations controlling these rainbow closures, or pivot to B/A,A/B and C/A,C/B positive source family that is not confined to D6; do not relabel an upper source-cell transition cap as a lower.
