# HYP-105 / #230 — AA4-AT: unique genuine-original 3×3 residual Hall on a GQ incidence forest

**Strict research-only Draft child of AA4-AS PR #546, pinned parent SHA \`0683dfb6be79fe3f140d7fd0ed159d070a53cc79\`.** Mathematics concerns true symplectic ORIGINAL \(W(3,s)\), \(s=2^h\ge2\), actual original source point-line incidence flags and two independent, completely globally injected typed physical source-factor image maps \(f,g\) held fixed across all flags. No imaginary original geometry, no per-Q randomized physical labels. Source Hall and final seven-GF5 selection are separate gates. Issue #230's \(S_s(f,g)=\Omega(s^6)\) remains **OPEN**.

## 1. Research frontier after AA4-AS

Earlier AA4-AR proved that every original \(W(3,s)\), \(h\ge14\), and every globally correlated complete \(f,g\) has at least \(s^6/200\) genuine good 3-original-incidence-ID centered two-D-edge wedges. AA4-AS proved that every wedge with opposite physical point ports and opposite line ports on three original source flags has precisely two typed physical pinned shapes, **T** (physical triangle) or **P** (physical path), and exactly \(\binom{a-3}{3}\) or \(3\binom{a-4}{2}\) formal three-edge physical residuals per side. For each GLOBALLY OCCUPIED point residual and line residual, the last three original incidence flag IDs must be constructed by matching three ORIGINAL point-factor slots to three ORIGINAL line-factor slots, respecting multiplicity, and must be distinct from the pinned original flags. Previously AA4-AS tested at most \(3!=6\) slot assignments. It did **not** use the strongest fact about the true original \(W(3,s)\) incidence relation: **incidence girth eight**.

**AA4-AT NEW all-h theorem — uniqueness, not positivity:** For ANY genuine symplectic \(W(3,2^h)\), all \(h\ge1\), ANY globally complete injected original \(f,g\), ANY original pinned opposite-typed 3-flag wedge, and ANY ONE fixed pair of globally occupied typed AA4-AS residual physical three-edge multisets, there are **at most ONE** distinct three-new-original-incidence-ID sets completing the wedge to a six-distinct-original-flag Hall-compatible Q. Even if a type-B residual duplicates a source point factor or source line factor, it remains 0/1. This is an EXACT **Boolean** original Hall gate, not a universal positive Hall survival fraction.

## 2. Proof: induced ORIGINAL 3+3 source-factor graph must be a forest

Let the remaining typed physical source-factor slots, after true global image inversion, be multisets \(P=(p_1,p_2,p_3)\), \(L=(\ell_1,\ell_2,\ell_3)\) of actual ORIGINAL point and line source factor IDs. A source factor may repeat (type B), and repeated physical edges correspond to repeated **factor slots**, not permission to reuse an identical ORIGINAL point-line flag ID twice. Define demand \(b_P(p)=\#\{i:p_i=p\}\), \(b_L(\ell)=\#\{i:\ell_i=\ell\}\). Each total demand is three. Work with the ACTUAL W(3,s) source incidence bipartite graph induced on the DISTINCT residual factor supports \(P^\sharp\), \(L^\sharp\), and remove any edges that correspond to already pinned real incidence-flag IDs. Each side has at most three vertices, so the induced graph has at most SIX vertices.

**Classical source theorem:** The incidence graph of a genuine generalized quadrangle has girth EIGHT. In particular it contains neither a four-cycle nor a six-cycle. Every cycle in a simple bipartite graph on at most three vertices per part would necessarily be length four or six, because a simple cycle uses an equal number of distinct points and distinct lines. Thus this ACTUAL original-source residual incidence graph is necessarily a **FOREST**. Deleting the already pinned original incidence flag edges cannot create cycles.

Every Hall-compatible original completion is a subset \(F\) of the edges of this forest such that
\[
\deg_F(p)=b_P(p),\qquad \deg_F(\ell)=b_L(\ell)
\]
on EVERY genuine original source factor in these residual supports. This is a simple edge-subset \(b\)-matching; choosing the same genuine original source point-line incidence edge twice is forbidden. A forest has **at most one** subgraph with a prescribed exact vertex-degree vector.

**Elementary proof by leaf elimination:** Pick a leaf \(v\) of the current source forest. If its required degree is zero, its unique edge cannot be selected. If its required degree is one, its unique edge MUST be selected, and subtract one from the demand of its neighbor. If its required degree exceeds the leaf's available degree, reject. An isolated vertex must have remaining required degree zero, otherwise reject. Delete the leaf and repeat; every step is forced by the source demands. At most three original edges can be selected in total. All leaves, edge incidences, remaining degrees, and the final six distinct original flag IDs are checked. The selected original Q is unique or there is no completion. No probabilistic source incidence sampling, independence of f and g, or physical label redraw is used.

**Equivalent linear-algebra proof:** On a forest, the unsigned incidence matrix from edge indicators to vertex degrees has full column rank (peeling any leaf exposes the coefficient of its unique edge). Therefore two different edge subsets cannot give the same demands. More concretely, symmetric difference of two b-matchings would contain an alternating even cycle; the true source-induced forest forbids one. This is a classical graph fact specialized to the correct original source threeflag domain.

**Prior art:** Incidence girth eight is standard generalized-quadrangle theory; see Godsil–Royle, *Algebraic Graph Theory*, Theorem 5.4.1 (generalized quadrangles characterized by diameter four and girth eight) and [Generalized Quadrangles, FU Berlin lecture notes](https://discretemath.imp.fu-berlin.de/DMIII-2019/finite_geometry.pdf). General forest leaf-peeling degree uniqueness is elementary graph theory. We do NOT claim either theorem or b-matching is newly invented. The new research object is their exact all-global-GQ \`three-original-pinned-flag / duplicated residual source factor / six ORIGINAL flag\` transfer and its consequence for the genuine AA4-AS Hall funnel.

## 3. Strong exact all-h original physical→source Hall reduction

Let \(O_P(w)\), \(O_L(w)\) be the ACTUALLY GLOBALLY OCCUPIED residual source-factor three-edge multisets of the two typed physical images of one real pinned original opposite wedge \(w\), as defined by AA4-AS. For each ordered pair \(A\in O_P(w), B\in O_L(w)\), the new source-forest leaf-peel gives a **Boolean** \(\eta_w(A,B)\in\{0,1\}\), with value one if it constructs the UNIQUE valid three added original incidence flags (all six original IDs distinct), zero if no such completion. Therefore the exact original-source-Hall distinct-six-Q count for this pinned wedge satisfies

\[
\boxed{\quad H(w)=\sum_{A\in O_P(w)}\sum_{B\in O_L(w)}\eta_w(A,B)
\quad\text{with each }\eta_w(A,B)\in\{0,1\}.\quad}
\]

**Injectivity of template→Q:** Suppose two different occupied point/line residual physical template pairs gave the same six ORIGINAL source incidence flags \(Q\). Since its pinned original wedge is fixed, the three added original flags are determined as \(Q\setminus w\). Their actual original source point and line factors determine their physical three-edge image multisets uniquely via the SAME globally fixed f and g. Hence both template pairs must be identical, contradiction. Thus the sum counts DISTINCT genuine original six-ID Hall Q without duplicate-source-slot inflation.

Consequently, for EVERY globally complete \(f,g\), EVERY real original opposite threeflag wedge and EVERY h,

\[
0\le H(w)\le |O_P(w)|\,|O_L(w)|
\le
\begin{cases}
\binom{a-3}{3}^2 & T/T,\\
3\binom{a-3}{3}\binom{a-4}{2} & T/P\text{ or }P/T,\\
9\binom{a-4}{2}^2 & P/P.
\end{cases}
\]

AA4-AS previously enumerated at most six incidence SLOT permutations per pair; this theorem gives a sharper structural **0/1 exact output per pair** and a deterministic leaf-forced source-first algorithm. It does **NOT** give a positive lower on \(\eta\), on Hall \(H(w)\) or on seven-GF5 accepted Q. The already proved TT structural zero under final GF5 selection remains true, even when \(\eta=1\) for some TT physical template pair. TRUE original AA4-AS W32 reverse contained six TT good wedges with nonzero Hall Q but zero accepted GF5.

## 4. Implementation and independent proof obligations

\`research/hyp105_issue230_d6aa4at_original_forest_unique_hall.py\` implements:
1. Strict true-original source potential graph construction from residual point-factor and line-factor multisets of exactly 3 slots each and true original source-index mapping, subtracting already pinned original flag IDs;
2. A **disjoint-set / union-find acyclicity guard** that rejects a synthetic residual C4 or C6. Genuine W(3,s) needs no adjustment: the induced original residual source graph is always a forest;
3. Deterministic degree-forced leaf removal with repeated typed source factor multiplicities. A source factor requiring degree two but having only one distinct genuine source incidence edge fails, rather than illegally reusing one ORIGINAL flag ID. It outputs ZERO or one canonical six-distinct-original-ID Q, and optional auditable selection trace;
4. Source-local \`exact_original_wedge_forest_Hall_audit\` over every physical globally occupied typed T/P residual pair for one genuine ORIGINAL wedge, recording total occupied template pairs, Hall-positive count, Hall-zero count, and an explicit uniqueness-checked original six-Q→physical template map. A separate old \`_original_threeflag_Hall_completions\` from AA4-AS, based on \`permutations\`, is invoked as an INDEPENDENT exact oracle and must yield precisely the SAME empty or singleton six-Q set;
5. All-h symbolic triangle/path formal capacities for each T/T, T/P, P/T, P/P shape, without pretending to construct huge fake original source geometry.

\`research/test_hyp105_issue230_d6aa4at_original_forest_unique_hall.py\` provides independent literal 3! old-oracle reference on hand-constructed **acyclic toy degree-forest subgraphs** with source factor repetition on both point and line types, forced and impossible degree demands, and a physically pinned duplicate flag rejection. It also constructs a **synthetic K2,2 four-incidence cycle** and a **synthetic 3-point/3-line six-incidence cycle**. Both are correctly REJECTED by the forest-validity gate; they must NEVER be presented as real symplectic W3s. The toy inputs illustrate mechanics and the absence of 4/6 source cycles required of actual W3s. Additional true-source tests verify independently against W32 and W34 real symplectic fixtures. The symbolic h≥14 / h≥24 theorem never builds a fictitious huge W3s.

**Full genuine ORIGINAL W32 five globals:** Enumerate ALL genuine GOOD two-typed opposite source wedges via actual original D-neighbor adjacency independently of source Hall; the earlier AA4-AS 3! genuine-original incidence oracle is run on EVERY globally occupied three-factor point×line physical pair per wedge and MUST return EXACTLY empty or a SINGLE six-Q, agreeing with the new forest algorithm. Independently freeze wedge count/occupied physical pair/Hall-Q charges:
- dual-zero 870 wedges, 5328 globally occupied physical template pairs, **150** source Hall Q-to-wedge incidences;
- lex 1105, 7233, **505**;
- reverse 1013, 6351, **232**;
- S68 697, 4041, **46**;
- S72 750, 4386, **85**.

**Actual independent GitHub-hosted first-run empirical 0/1 source-Hall breakdown, every same-global-map REAL W32:** All five maps were checked one physically occupied T/P pair at a time against the OLD separate AA4-AS 3! source-incidence oracle and yielded EXACTLY empty or one genuine ORIGINAL six-incidence-ID Q per physical template combination. Counts below distinguish residual PHYSICAL candidate mass, actual distinct original six-Q charges and the number of pinned true original wedges with at least ONE source-Hall Q; the last GF5 numbers come from the historical independent original selected-seven oracle.

| Complete globally fixed genuine W(3,2) f,g | Actual 2-typed opposite GOOD original source wedges | Occupied point×line physical residual template pairs | Forest-Hall TRUE pairs (0/1 each) | Forest-Hall FALSE pairs | Distinct original 3-flag wedges with any source Hall Q | Final accepted-seven-GF5 original Q-to-wedge incidences |
|---|---:|---:|---:|---:|---:|---:|
| dual-zero | 870 | 5,328 | **150** | 5,178 | 135 | 40 |
| lex | 1,105 | 7,233 | **505** | 6,728 | 360 | 237 |
| reverse | 1,013 | 6,351 | **232** | 6,119 | 216 | 68 |
| S68 | 697 | 4,041 | **46** | 3,995 | 44 | **6** |
| S72 | 750 | 4,386 | **85** | 4,301 | 79 | **11** |

In particular, the genuine W32 global S68 model has 3995/4041 *physically occupied* source-factor candidate template pairs with no valid actual ORIGINAL source Hall completion, despite K6 being PHYSICALLY complete, and only six accepted seven-GF5 original Q-to-wedge incidences among 46 real source Hall-complete pairs. It is a **finite** structural warning, never an alleged large-h uniform zero-Hall theorem or infinite original f_s,g_s counterfamily.

**Real original W34 symplectic GF4, two separately globally injected point/line K14 maps:** on independently witnessed actual original D6 wedge lex (0,6,120), all 11025 physical residual template pairs give precisely 11 true original six-incidence-ID Hall-complete Q; random original wedge (0,11,381) gives precisely 12 Hall Q among 13200 physically occupied pairs. Both contain the independently original positive GF5 D6 six-ID Q witnessed earlier, but these are **partial chosen-wedge** tests, NOT full original W34 six-Q census.

[First independent exact-head Dedicated AA4-AT GitHub-hosted workflow](https://github.com/definitely-stable/Mathlab/actions/runs/38866871976) finished **4/4 SUCCESS**: all-h symbolic h1..60, real original W32 complete all candidate template pair oracle, true original W34 partial D6 source Hall, and actual source symplectic/physically independent typed coordinates invariance all passed. Final-HEAD reruns and INDEX, Proof Audit, Full Research must be checked after this report commit; no independent mathematical acceptance has been granted.
The previous AA4-AS independently accepted seven-GF5 Q-to-wedge charges 40, 237, 68, 6, 11 are strictly smaller/equal, illustrating why forest-Hall uniqueness cannot infer positive final selected GF5.

**Genuine ORIGINAL W34 lex/random** globally complete injected (K14 with six missing physical source-factor image edges per typed map), choose one independently validated true-original source six-ID D6 witness per scheme from earlier AA4-AQ explicitly ROOT/BUDGET LIMITED scan; run old 3! and new forced-forest Hall on every globally occupied source-factor residual physical template pair for its fixed original triple. Must recover exactly the same genuine 11 and 12 original Hall six-Q respectively, include the independently accepted source D6 Q and retain identical global f/g. Absolutely NO full W34 selected seven-GF5 count or large-h nontrivial Hall fraction is claimed.

**Further controls:** true symplectic source automorphism and independent physical point/line coordinate permutations preserve all original local shape/Hall counts; malformed global source incidence lists and non-injected physical label maps rejected by prior original context validator. Dedicated GitHub-hosted jobs plus INDEX, Proof Audit and Full Research on the EXACT final child HEAD; independent mathematical referee separate; strict Draft PR, no main merge or accepted registry. The parent AA4-AS Full Research was CANCELLED and is NOT accepted as integration green.

## 5. Next genuine-original AA4-AU frontier and explicit limits

AA4-AT removes the redundant \(3!\) source-slot matching ambiguity and isolates the actual remaining original-source-Hall indicator \(\eta\) as **0/1 on a small acyclic residual incidence graph**, including repeated true source factors. It is a stronger exact reduction for analytical study, not a breakthrough positive probability theorem. The key open analytic statement is an ALL-f,g, all-sufficiently-large-h **positive lower on the sum of these ORIGINAL forest-Hall indicators** over good actual source wedges of allowed physical shapes, AND simultaneous alignment under the accepted seven-GF5 classifier. The earlier AA4-AR unconditional \(\Omega(s^6)\) mass is of all GOOD threeflag wedges, not guaranteed to pass opposite-port and not forbidden TT conditions. The W32 S68 counts show abundant physically occupied template pairs with zero original Hall. A possible independent route is accepted zero-good-wedge source classes B/B-disjoint, C/A, C/B whose mass the present anchored-good-wedge reduction cannot see. Do not promote exact forest uniqueness or an upper bound to positive \(S_s(f,g)=\Omega(s^6)\).

**The universal \(S_s(f,g)\ge c s^6\) of issue #230 is still UNSOLVED; no genuine infinite original two-map counterfamily was constructed.**
