# HYP-105 / #230 — AA4-LCR: local return witnesses for the physical C6 defect

**Scientific status:** scoped ALL-\(h\) exact combinatorial decomposition, sharp logical exclusion and a universal constant-factor local-witness reduction. Independent finite certificates use genuine symplectic \(W(3,2)\) and \(W(3,4)\). Original root #230 remains **OPEN_WITH_FORMAL_BLOCKER**; no universal seventh-family obstruction or ASET exponent proved.

## 1. Problem and established baseline

A prior result (stacked Draft #652 / AA4-RC6) gives

\[
D_6(f,g)=C_6(H)-\operatorname{Defect}_6(H),
\]

where \(H(f,g)\) is the simple physical-corner graph created from EVERY **genuine original incidence flag** of \(W(3,s)\), \(s=2^h\), \(h\ge1\), with arbitrary correlated **complete and separately injective** source POINT and LINE pair-label maps. Here \(D_6\) counts **accepted historical GF(5) six-original-incidence-ID** aligned C6/C6 motifs, and \(\operatorname{Defect}_6\) counts physical simple unoriented six-cycles that repeat at least one coordinate along either physical axis. The ordinary physical adjacency trace and even nonbacktracking closed-walk trace are not equal to this accepted squarefree trace.

The new task is to understand, **without inventing a false source-girth transfer**, exactly which local events make a physically simple C6 nonrainbow.

## 2. All-h local return theorem (no independence)

Fix a simple physical six-cycle \(C=(v_0,\ldots,v_5)\) in \(H\), \(v_i=(x_i,y_i)\), indices modulo six. Physical edges always change **both** coordinates. Define the two-step return sets

\[
B_x(C)=\{i\in\mathbb Z/6:x_i=x_{i+2}\},\qquad
B_y(C)=\{i\in\mathbb Z/6:y_i=y_{i+2}\},
\]

and the three-step opposite-corner return sets

\[
T_x(C)=\{i\in\{0,1,2\}:x_i=x_{i+3}\},\qquad
T_y(C)=\{i\in\{0,1,2\}:y_i=y_{i+3}\}.
\]

**Theorem (complete local defects).** A physical simple C6 is coordinate-rainbow iff *all four* of these sets are empty. Thus every defective C6 has a local two-step and/or opposite-three-step return. For each i, \(i\notin B_x\cap B_y\) and \(i\notin T_x\cap T_y\), because such a simultaneous return would make the **physical corners themselves equal**, contradicting a simple six-cycle.

*Proof:* In a cycle of length six the smallest cyclic distance between any two distinct vertex indices is one, two or three. Distance-one coordinate coincidences are forbidden by the definition of physical graph edges; any remaining coincidence is a two-step or three-step return. Simplicity forbids a coincidence in both physical axes between the same pair of corners. \(\square\)

Let \(F\) count defective cycles. Let \(F_B\) count those with \(|B_x|+|B_y|>0\), and \(F_T\) count those with no two-step return but with \(|T_x|+|T_y|>0\). Then the following **all-h exact partition** holds:

\[
\boxed{\operatorname{Defect}_6(H)=F_B+F_T.}
\]

Define local witness sums over all **simple undirected unrooted** physical C6:

\[
W_2=\sum_C(|B_x(C)|+|B_y(C)|),\qquad
W_3=\sum_C(|T_x(C)|+|T_y(C)|).
\]

Since the return indices on opposite axes are disjoint, \(|B_x|+|B_y|\le6\), \(|T_x|+|T_y|\le3\), so **at most nine** local return witnesses can belong to any one defective physical six-cycle. Every defect has at least one witness. Therefore the new **universal constant-factor reduction** is

\[
\boxed{\frac{W_2+W_3}{9}\le\operatorname{Defect}_6(H)\le W_2+W_3.}
\]

A future source-sensitive bound on the local two- and three-step return energies would control the global defect up to a fixed constant, independent of \(s\) and of correlations. The inequalities are *not* a bound on the magnitude of either \(W_2\) or \(W_3\), so they do **not** show \(\operatorname{Defect}_6=o(s^6)\).

## 3. Rigorous source-flag meaning of local returns

For each oriented physical edge of the six-cycle let \(e_i=(p_i,l_i)\) denote its **uniquely determined genuine original incidence ID**, where \(p_i\) is a source POINT and \(l_i\) a source LINE, and the physical edge is the pair \(f(p_i)\times g(l_i)\) matched diagonally.

By global typed injection:

\[
\boxed{
x_i=x_{i+2}\iff p_i=p_{i+1},\quad
y_i=y_{i+2}\iff l_i=l_{i+1}.
}
\]

The equalities compare distinct actual source flags: if both source factors were equal then \(v_i=v_{i+2}\) would be forced, impossible for a simple physical cycle. A two-step first-coordinate return is precisely a pair of *consecutive original flags sharing the source POINT factor* (a point cherry); a two-step second-coordinate return is precisely a source LINE cherry. This is much more precise than just counting physical arcs.

A three-step first-coordinate return means the first-coordinate edges of **three consecutive original incidence flags** form a triangle of three distinct physical point-pair edges of \(K_a\); their source point IDs are distinct. The second-coordinate statement is symmetric on source line factors. These coordinate triangles need not be source incidence triangles: the original bipartite incidence graph retains girth eight, while the physical corner graph may have triangles.

## 4. Structural no-go for reusing the same defective sixset

Every one of the seven original leading GF(5) accepted six-ID classes requires **six occupied physical coordinate symbols on each half**.

A defective physical cycle has at most five distinct coordinates on at least one half, and the point/line images of the six physical edges are exactly the coordinate pairs between adjacent cycle corners. Thus:

> **All-h exclusion:** If the six genuine source incidence IDs carried by a defective physical simple six-cycle are distinct, their *same unordered original sixset* cannot be classified as **any** of the historical seven accepted GF(5) original six-coordinate classes. If some source IDs repeat, it fails the six-distinct-ID root requirement already.

This is a no-go for a naive *local compensation-by-reclassification of exactly the same six physical edges*. It does NOT preclude other accepted original sixsets on the same fixed label maps, including the coherent D6 compensation found in PR #651, and does NOT negate root Branch A.

## 5. Genuine finite source-ID falsifiers: most defects do NOT repeat source IDs

Independent GF(2)/GF(4) symplectic geometry, complete globally injected typed maps, all original incidence IDs recovered physical edge-by-edge. The finite oracle canonically enumerates every simple physical C6 once; validates each return's source-factor interpretation; tests the **historical seven-family classifier** directly on *every* defective sixset with six distinct original source incidence IDs; cross-checks total physical C6 and D6 against the AA4-RC6 independent oracle.

| Genuine complete map | All C6 | D6 | Coordinate defect | Defects with two-step return | Pure three-step defects | Defect with six distinct original flags | Defect repeating flag ID |
|---|---:|---:|---:|---:|---:|---:|---:|
| W(3,2) lex | 730 | 15 | 715 | 634 | 81 | 677 | 38 |
| W(3,2) reverse-line | 485 | 3 | 482 | 422 | 60 | 451 | 31 |
| W(3,4) original adversarial injected K14 | 30,306 | 4,972 | 25,334 | 20,869 | 4,465 | 25,182 | 152 |

W(3,4) exhibits an especially strong **finite counterexample to the proposed universal shortcut** "all physically defective C6 necessarily reuse an original flag ID": **25,182 of 25,334 defective cycles** do not reuse a source flag ID. No finite-to-all-\(h\) extrapolation is claimed.

The two-step return flags for the same finite inputs are counted independently, preserving original source POINT/LINE identities. For W(3,4), 12,987 defective cycles have an x two-step return, 12,531 a y two-step; 5,620 contain x opposite-three-step returns and 5,620 contain y opposite-three-step returns. Those marginal categories *overlap*, so their sums must not be interpreted as disjoint cycle counts.

## 6. Next mathematically meaningful step

The former physical graph spectral and uncorrected six-cycle route discards the local return constraints and is empirically extremely loose. The above theorem compresses every coordinate defect into a **finite catalogue of local source-factor cherries and three-factor physical triangles**, with a uniform multiplicity cap nine. An actual advance toward the root must obtain source-geometric inequalities on their six-cycle **completion masses** \(W_2,W_3\), *or* prove a **same-fixed-f,g compensation inequality** involving additional, distinct original accepted GF(5) sixsets.

Neither has been established here. In particular, lower-bounding the ordinary physical C6 count is not enough if \(W_2+W_3\) remains comparable, and filtering repeated original source flag IDs does not isolate D6. Keep PR Draft, all original incidence quantifiers, exact-head hosted CI and an independent qualified mathematical referee gate.


## 7. NEW all-h original-source pencil wedge conservation theorem (AA4-LCR-W)

The preceding defect witness reduction leaves the quantitative size of the two-step witness sum \(W_2\) open. A more primitive quantity has a **rigorous \(\Theta(s^5)\) universal upper envelope**: the number \(J_x\) of all **unoriented length-two wedges of H** whose start and end have the SAME first coordinate, counted once by their physical middle corner and two physical endpoint corners. Let \(J_y\) count the analogous second-coordinate wedges. These count local *wedges*, NOT their C6 completions.

For each genuine original source point \(p\) and physical second-coordinate symbol \(y\), write

\[
d_p(y)=|\{l\text{ an ORIGINAL line incident to }p:y\in g(l)\}|.
\]

For each genuine original line \(l\) and first-coordinate symbol \(x\) put

\[
e_l(x)=|\{p\text{ an ORIGINAL point on }l:x\in f(p)\}|.
\]

**Theorem (all-h, fixed arbitrary correlated injections):**

\[
\boxed{
J_x=2\sum_{p,y}\binom{d_p(y)}2,\qquad
J_y=2\sum_{l,x}\binom{e_l(x)}2,
}
\]

and separately

\[
\boxed{0\le J_x,J_y\le 2V\binom{s+1}{2}=Vs(s+1)=O(s^5).}
\]

*Proof of equality.* A two-edge wedge with first-coordinate return \(x_0=x_2\) uses two consecutive genuine ORIGINAL source flags \((p,l_1),(p,l_2)\) with the same point factor \(p\) by the all-h return theorem. Let \(y_1\) be the second coordinate of its central physical corner. Both physical g-line edges contain \(y_1\), and because \(g\) is injective, the two different source lines have distinct other physical endpoints \(y_0\ne y_2\). Each unordered pair of original incident lines meeting at a particular symbol \(y_1\) produces exactly TWO physically distinct wedges: one for each possible central first-coordinate endpoint of \(f(p)\). Hence \(J_x=2\sum_{p,y}\binom{d_p(y)}2\). The line-side proof is dual.

*Proof of upper bound.* Each original point is incident to exactly \(d=s+1\) different source lines, with \(d\) **different** physical edges under global \(g\)-injectivity. Two distinct physical pair-edges intersect in at most one coordinate. Consequently for each source point \(p\), \(\sum_y\binom{d_p(y)}2\le\binom d2\), counting each unordered pair of incident source lines at most once. Sum over \(V\) source points and multiply by 2. Repeat dually on the original source lines. No random labels, no independence, no uniform physical-degree premise. \(\square\)

For each wedge \(w\) let \(\operatorname{comp}_6(w)\) be the number of physically simple unoriented C6s containing that **particular** x/y-coordinate returning wedge. By literal double counting:

\[
\boxed{
W_{2,x}=\sum_{w\in\mathcal J_x}\operatorname{comp}_6(w),
\qquad
W_{2,y}=\sum_{w\in\mathcal J_y}\operatorname{comp}_6(w).
}
\]

Therefore a **separately proved** uniform or average \(O(s)\) bound on completions per original-source pencil wedge would imply \(W_2=O(s^6)\). This additional bound is NOT proved. In particular, \(J_x,J_y=O(s^5)\) alone cannot be presented as any \(O(s^6)\) bound for the **total 6-cycle defect**.

### Independent source/physical finite source-ID evidence

Two completely different counting methods agree exactly: (i) sum original GQ incidence-pencil coordinate degrees \(\binom{d_p(y)}2\), and (ii) enumerate every simple physical two-edge wedge around a corner and group physical neighbors by equal opposite-axis coordinate. Both maintain the original source flags and independently injected point/line pair labels.

| Legal true-source map | \(J_x\) | \(J_y\) | Universal bound for each | Largest original point-pencil symbol degree | Largest original line-pencil symbol degree |
|---|---:|---:|---:|---:|---:|
| W(3,2) lex K6 | 64 | 52 | 90 | 3 | 3 |
| W(3,2) reverse-line K6 | 42 | 52 | 90 | 2 | 3 |
| W(3,4) full adversarial K14 | 624 | 602 | 1,700 | 5 | 5 |

The exact arithmetic is independently frozen in [the pencil-wedge module](../../research/hyp105_original_source_pencil_wedges.py) and [dual-method tests](../../research/test_hyp105_original_source_pencil_wedges.py).

**Updated next P0:** prove or falsify a meaningful source-sensitive upper bound for physical C6 completions per pencil returning wedge. The most promising local object is a length-four simple physical path between two given physical corners with a shared first or second coordinate. Generic degree-norm bounds discard the GQ incidence-pair constraints and currently remain too weak. The parallel pure-three-step return class still needs a separate source-physical triangle-completion analysis, and full seven-class *same-map* compensation remains open.
