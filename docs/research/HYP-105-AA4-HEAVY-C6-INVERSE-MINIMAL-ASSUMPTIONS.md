# HYP-105 #230 — AA4-HEAVY-C6-INVERSE-MINIMAL: independent original six-ID lift theorem and genuine necessity counterexamples

**Scientific state:** local SOURCE reconstruction theorem **all orders**, plus NEW TRUE original W(3,2)/W(3,4) falsifiers that separately establish the necessity of BOTH typed coordinate cuts and original pencil-conflict independence for the claimed unconditional selected-C6 properness implication. Strict child of [#771](https://github.com/definitely-stable/Mathlab/pull/771) at frozen exact HEAD 2453291e3db84dd76c5122c50343e203040fc349. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230) **OPEN_WITH_FORMAL_BLOCKER**. No main or ancestor mutation, no merge, no ASET or strict b6 claim. Ancestors [#734](https://github.com/definitely-stable/Mathlab/pull/734) and [#750](https://github.com/definitely-stable/Mathlab/pull/750) ALREADY claimed this injection: the scientific contribution of this slice is **independent necessity/sufficiency audit, a dual source-first lift and genuine-original minimal assumption falsifiers**, not dishonest rediscovery.

## 1. Strict ORIGINAL source versus physical edge provenance

Let I={(p,ell):p lies on ell} be named ORIGINAL flags in true symplectic W(3,s), s=2^h. Let f:P→binom([a],2) and g:L→binom([a],2) be separately globally pair-injective complete maps, fixed arbitrarily and correlated without restriction. A true flag i=(p,ell) owns exactly TWO vertex-disjoint diagonals of the real rectangle f(p)×g(ell), each an ordinary simple physical undirected edge.

**Lemma 1, unique physical owner.** From any actual physical edge {(x,y),(z,w)} with x≠z,y≠w recover its unique ORIGINAL owner, if it exists, as the only point p with f(p)={x,z} and the only line ell with g(ell)={y,w}; verify (p,ell)∈I. Because BOTH maps are globally injected, at most one owner exists. The two diagonal edges of a fixed flag are disjoint, not parallel or interchangeable clones. Therefore any true heavy witness graph F constructed by DELETING edges/vertices from this original graph stays simple, loopless and uniquely source-owned. It may retain only one of the two diagonals of a flag; this is legitimate because its proof is a subgraph of an initially paired selected graph, not a claim that F itself retains whole flags.

Fix a true subset S of named ORIGINAL flags **independent in the actual pencil-conflict graph J**, where i,j conflict precisely when they have the same original point p and their physical g-line label pairs intersect, or they have the same original line ell and their physical f-point pairs intersect. Require TWO separately fixed physical bit colorings b_x,b_y with every retained S flag crossing the x-cut along f(p) and crossing the y-cut along g(ell). The full two-diagonal physical graph H(S) is edge-preserving for both cuts; any F⊆H(S) may drop edges. These are exactly the HEAVY selector hypotheses in #750; no probabilistic independence or fake physical copies are assumed.

## 2. Local all-order C6 coordinate-properness: three distances, three DIFFERENT arguments

Let C=(v0,v1,...,v5) be any ordinary simple unoriented length-six cycle in F, with indices mod 6 and v_j=(x_j,y_j). We prove separately that all six x's are pairwise distinct and all six y's are pairwise distinct.

- **Cyclic distance 1:** every genuine physical diagonal changes BOTH coordinates. So x_j≠x_{j+1} and y_j≠y_{j+1}.
- **Cyclic distance 2:** suppose x_j=x_{j+2}. The two consecutive physical edges necessarily have the same unordered x pair {x_j,x_{j+1}}, and injectivity of f forces their ORIGINAL point owners to coincide. They cannot be the two physical diagonals of the SAME named flag: those diagonals share no physical vertex, while consecutive cycle edges share v_{j+1}. Thus they are **different original flags** with the same point p. Their distinct g-line pairs both contain y_{j+1}, hence the flags conflict in genuine SOURCE J, contradicting S independence. The dual argument for y_j=y_{j+2} uses equality of the line owner and overlapping f-point pairs at x_{j+1}.
- **Cyclic distance 3:** suppose x_j=x_{j+3}. Each of the three consecutive genuine source-owned diagonal edges crosses the SAME physical x-cut, so b_x(x_{j+3})=b_x(x_j)+3 (mod 2) ≠b_x(x_j), contradiction. Dual y-cut forbids y_j=y_{j+3}.

Every two different vertices of a C6 are at cyclic distance 1,2, or 3. Therefore

\[
\boxed{|\{x_0,\ldots,x_5\}|=|\{y_0,\ldots,y_5\}|=6.}
\tag{HC-R1}
\]

The proof uses no asymptotic GQ spectral input, no specific physical degree, no integer T, no graph supersaturation and no random label correlations: it is a finite combinatorial theorem for ANY true ORIGINAL paired-source graph with this J and two cuts, including any edge-deleted simple F.

Each actual C6 edge e_j gets its named ORIGINAL flag i_j=(p_j,ell_j), with f(p_j)={x_j,x_{j+1}} and g(ell_j)={y_j,y_{j+1}}. Since all x's and all y's are distinct, all six original point factors p_j are different, all six original line factors ell_j are different, and hence all six ORIGINAL incidence IDs i_j are different. The six f factor edges form one simple x-symbol C6, and the six g factor edges form one simple y-symbol C6 **in the same sequence of named ORIGINAL flags**: the historically accepted aligned ORIGINAL D6 topology. Genuine W(3,s) incidence is still enforced: those are six named flags from I, not synthetic pair couplings.

## 3. NEW minimal factor-lift lemma: the unordered original six-ID set admits at most one physical unoriented C6

In fact the **source-first uniqueness** requires strictly less than the full selected-graph hypotheses:

**Lemma 2 (factor-cycle lift, all lengths).** Let B be any unordered set of k≥3 different named ORIGINAL flags, with pair-injective f/g, all k ORIGINAL point factors distinct and all k line factors distinct. Suppose their k f pair labels form one connected simple k-cycle on exactly k physical x symbols. Consider real physical k-cycles using exactly those k original edge owners. **At most one** unoriented actual physical k-cycle exists, independent of color cuts, GQ geometry or J independence.

**Proof.** The unordered f factor edge set is a uniquely determined simple cycle C_k. Its cyclic order of source edge IDs is fixed up to global rotation and reversal. For each consecutive pair of original source owners i_{j-1},i_j, the physical y coordinate at their common factor-cycle vertex must belong to g(ell_{j-1})∩g(ell_j). Distinct line factors plus injective g imply those two two-element label pairs are distinct, so their intersection has size **at most one**. Thus every y_j is either forced or impossible. If any intersection is empty, no lift. Otherwise the ENTIRE oriented vertex sequence (x_j,y_j) is forced. The edge-owner verification checks each actual physical edge is in the allowed physical graph and owned by i_j; simple vertex and coordinate distinctness can be checked separately when D6 is required. Rotation/reversal of the x cycle produces the SAME unoriented lifted cycle. Therefore at most one physical unoriented k-cycle exists. QED.

**Independent DUAL proof** starts instead from the unordered g factor cycle and forces x_j from adjacent f pair intersections. It must recover the same actual unoriented physical cycle. The new referee implements BOTH independent inverses and compares their outputs against an entirely different real physical graph DFS; it never consults the historical six-motif classifier or old source-inverse implementations.

For HEAVY-selected proper C6 the lemma applies with k=6. Every such C6 maps to exactly one set of six original source IDs, and **distinct physical C6 cannot have the same set of six IDs**. Consequently

\[
\boxed{\#C_6(F)\le D_{6,\overline Z}(f,g)}
\tag{HC-R2}
\]

for any F satisfying Lemma 1/HC-R1, assuming all its named ORIGINAL owners avoid Z. This is an **injection, not a bijection**: a historical D6 source sixset need not possess a physical lift in the selected F. No factor 6, 12 or 6! is inserted into the right side: the published ordinary graph C6 theorem counts **unoriented distinct simple copies**, and each such unoriented physical C6 maps to ONE original source sixset.

**Local STOP:** the condition "six different points and lines" alone would not guarantee that factor edge sets are cycles; conversely, a factor cycle with repeated other-side ORIGINAL line ID can have two-symbol intersections, destroying unique reconstruction. All assumptions are explicitly checked; neither fake factor-cycle order nor physical diagonal clone is allowed.

## 4. NEW true W32/W34 ORIGINAL source counterexamples: why every premise matters

The new independent constructor builds genuine symplectic original flags, not an abstract synthetic rectangle graph, and assigns COMPLETE separately globally injected physical pair maps of actual MINIMAL alphabet a to all V original points and V original lines. It uses a true matching of six named ORIGINAL incidence flags (or one true repeated point where explicitly indicated). **All other source factors are also assigned distinct unused real pair labels**, not omitted or reassigned during selection. The six selected original flags each retain both opposite real diagonals, and the planted physical C6 has six distinct physical vertices and six real original owner edges. Therefore each fixture is a VALID physical W(3,s) experiment; only ONE target selection hypothesis is switched off per negative case.

| Original W(3,s) case | Original J independent | x-cut | y-cut | Genuine selected simple C6 | Six distinct x and y coordinates? |
|---|---|---|---|---|---|
| **proper** | YES | YES | YES | YES | YES, true D6 |
| **drop_left_cut** | YES | **NO** | YES | YES | **NO**: x0=x3 |
| **drop_right_cut** | YES | YES | **NO** | YES | **NO**: y0=y3 |
| **drop_J_independence** | **NO** | YES | YES | YES | **NO**: x0=x2 |

The actual planted coordinate sequences, taken cyclically:

- positive: x=(0,1,2,3,4,5), y=(0,1,2,3,4,5);
- no x-cut: x=(0,1,2,0,3,4), y=(0,1,2,3,4,5);
- no y-cut: x=(0,1,2,3,4,5), y=(0,1,2,0,3,4);
- no source J independence: x=(0,1,0,2,3,4), y=(0,1,2,3,4,5).

In the fourth case the first TWO distinct real ORIGINAL flags share the same original point p and have g-line physical pairs meeting at the actual middle y symbol. They are a **real source J-conflict**. Both bit cuts can still be simultaneously satisfied because the first-factor edge is traversed forward and then backward; source independence is what excludes this specific coordinate-improper two-edge cherry. In the second/third cases six owner points and six owner lines remain distinct, so source J is **actually empty** for those selected flags; the missing cut alone allows a gap-three coordinate return, with all six physical vertices still distinct.

These four fixtures exist separately on BOTH genuine W(3,2) (45 ORIGINAL flags, minimal a=6) and W(3,4) (425 ORIGINAL flags, minimal a=14). They disprove any stronger proposal that one cut is redundant or that both cuts remove the need for J. **They do not refute the properly scoped all-order theorem** with ALL three hypotheses, and they are not root Branch A counterexamples.

## 5. Three fully independent finite census routes, no shared cycle normalizations

The new module research/hyp105_original_heavy_c6_inverse_minimal.py implements:

1. **Physical-first graph C6 DFS:** actual physical vertices of true paired ORIGINAL source edges, canonical unoriented sixvertex cycles modulo 6 rotations and reversal. No source first-cycle inverse is used to discover the cycles.
2. **Original source-first x-factor lift:** from the UNSORTED six named ORIGINAL source IDs, make the x factor adjacency, demand one connected simple C6 with six different point and line factors, deduce each y coordinate by the intersections of adjacent original g-line pairs; verify each required real physical edge and its original owner. No DFS physical cycle discovery is used.
3. **Independent original source-first y-factor lift:** repeat the entire factor reconstruction with g as primary, f as forced intersections. The two source inverses must match the physically enumerated C6, not simply have the same counts.
4. A SEPARATE test implements the graph-only **unordered two internally-disjoint 3paths census**, divided by exactly three, as a second completely independent physical C6 oracle (cf. already audited graph identity in [#749](https://github.com/definitely-stable/Mathlab/pull/749)).
5. A no-clone edge-deletion test retains ONLY ONE genuine physical diagonal per original source flag in F (rather than both), verifies both source-first inverses still recover the one real C6, and rejects any missing necessary physical edge. This tests actual HEAVY winning-block edge deletion, not an invented assumption that F must still be paired.
6. Malformed/missing/duplicate named ORIGINAL flags, source J cherry, and projection to five original IDs are rejected. Both actual coordinate cuts and actual named original conflict graph are checked separately.

These finite oracles are falsifiers of the **written all-h combinatorial proofs**, not their justification. The code imports only the independently audited genuine symplectic source constructor \`hyp105_original_defect_factor_referee.genuine_symplectic_source\`, not prior inverse, HEAVY, B75, LOW, GF5, C6-census or historical source-selector implementations.

## 6. Scientific acceptance boundary and next step

This slice completes a **separately auditable all-h source-level correctness proof** of the candidate HEAVY C6→D6 interface and independently demonstrates WHY the exact selection hypotheses are indispensable. The proof is algebraic and graph-combinatorial and applies for every h, arbitrary correlated fixed f/g and arbitrary Z as long as the retained selected source owners avoid Z. The actual quantum of ordinary C6 from Jiang–Yepremyan, the existence of a sufficiently dense HEAVY simple F, and the no-Z R=93312 source density construction are **previous/inherited mathematical steps** from #744/#749/#750, not newly proved by these tests.

**Root HYP-105 #230 remains OPEN_WITH_FORMAL_BLOCKER.** To declare global Branch A PROVED_A would additionally require publication-level independent validation of all inherited LOW GQ endpoint/source fourth/sixth-moment and Blakley–Roy errors, P3→produced ORIGINAL BBo 2-to-1 source inverse, uniform HEAVY/LOW partition/quantifiers, and the accepted mapping to seven ORIGINAL positive six-ID classes. Green CI and this particular local theorem do not settle those remaining dependencies; no ASET exponent or GF5 event bound is claimed.

**Next allowed action:** independent quantitative end-to-end ROOT Branch A dependency DAG audit (including exact LOW source-endpoint and P3→BBo matching), with the FIRST false or unproven all-h implication promoted to an explicit STOP before any ancestor merge. No parent/main changes, no issue closure, no PR merge based on this one local acceptance.
