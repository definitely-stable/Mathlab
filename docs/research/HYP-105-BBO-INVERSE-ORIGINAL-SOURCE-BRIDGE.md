# HYP-105 #230 — AA4-BBOINV: independent all-\(h\) INVERSE reconstruction and exact 0/2 directed-path multiplicity

**Scientific scope:** genuine ORIGINAL symplectic \(W(3,2^h)\), \(h\ge1\), any complete legal separately globally injected pair maps f on original points and g on original lines, with arbitrary correlation, and the historical strictly-positive GF(5) **B/B-overlap** six-incidence-ID class. This proof begins with a **given ORIGINAL sixset**, independently of all prior physical path generators and original GQ source projection algorithms. The proof is local combinatorics valid for every dyadic \(s\), not an extrapolation of finite W32/W34. Previous forward construction appears in universal Branch A scientific [Draft #672](https://github.com/definitely-stable/Mathlab/pull/672), deletion stability [#673](https://github.com/definitely-stable/Mathlab/pull/673), and [#674](https://github.com/definitely-stable/Mathlab/pull/674). This slice isolates and independently proves its original-sixset multiplicity-normalization lemma, **not** the entire all-map global sextic theorem, source mixed/full-core blocker, full signed R3, or ASET exponent. Qualified external mathematical review is not supplied; #230 remains OPEN_WITH_FORMAL_BLOCKER.

## 1. Complete inverse statement, with the non-surjectivity made explicit

Let \(Q\) be any set of **six distinct ACTUAL ORIGINAL incidence IDs** \(\{(p_i,\ell_i)\}_{i=1}^6\) of the same \(W(3,s)\). Suppose its source point factor multiplicities are B=(2,1,1,1,1), its source line factor multiplicities are also B, and **the source point repeated twice and the source line repeated twice occur together in exactly one actual incidence ID of Q** (historical B/B-overlap, not B/B-disjoint). Suppose in addition both original-source physical pair projections have exactly six touched physical coordinates each with degree two, so Q passes the exact historical B/B-overlap sixset classifier.

Define \(\mathfrak P(Q;f,g)\) as the set of **directed coordinate-proper 3-edge physical paths** \(v_0v_1v_2v_3\) with each physical edge sourced from a different one of THREE IDs of Q, such that their endpoint physical coordinate pair labels decode the two non-middle source GQ projection factors, and the other three IDs are precisely its original \((q,\ell),(p,\ell),(p,r)\) source anchor. The path core \(I\) may contain the three path IDs but need NOT contain these three anchor IDs; a forbidden source ID set Z removes a candidate if it meets ANY of Q's six IDs.

**New exact ALL-h theorem:**
\[
\boxed{\qquad
 |\mathfrak P(Q;f,g)|\in\{0,2\},
 \quad
 |\mathfrak P(Q;f,g)|=2
 \iff
 \text{the two physical 3-edge chains have the SAME ordered sequence
 of three ORIGINAL flag IDs up to reversal}.
 \qquad}\tag{BBO-INV}
\]
The two nonzero paths are exact reversals of one another. More generally with any original core \(I\) and forbidden set \(Z\), the number of eligible directed original-source-backed paths remains **either 0 or 2**; the pair survives precisely when all three non-anchor IDs belong to I, none of Q's SIX source flag IDs belongs to Z, and the ordered-source-flag alignment criterion holds.

In particular the forward map from valid unblocked directed paths to accepted ORIGINAL B/B-overlap sixsets has EXACTLY TWO preimages **onto its image**, so the number of its *distinct* accepted original sixsets is exactly
\[
 \boxed{\quad \#\{\text{accepted ORIGINAL source sixsets produced}\}
       =\frac12\#\{\text{valid unblocked directed paths}\}.\quad}\tag{BBO-INV-2}
\]
**Important:** not every historical accepted ORIGINAL B/B-overlap sixset need appear in the image of this specific path-based construction; a sixset whose independent coordinate three-chains have incompatible flag orders has zero such paths. No surjectivity onto the whole historical B/B-overlap class is claimed. Thus this is a VALID positive **subcount**, and the normalization divisor two is not a synthetic physical multiplicity.

## 2. Independently find the unique ORIGINAL source anchor from the sixset

The source B/B profile determines a unique original point p repeated twice and a unique original line ell repeated twice. The B/B-overlap condition says Q contains the ACTUAL original incidence \((p,\ell)\).

There are exactly two ORIGINAL flags of Q with point p and exactly two with line ell. Because their intersection \((p,\ell)\) is a single actual flag ID (the genuine source has no parallel repeated original incidences), this uniquely partitions Q into:

- the **three anchor IDs**
  \[
    A(Q)=\{(q,\ell),(p,\ell),(p,r)\},
  \]
  where q is the only other original point using ell and r the only other original line through p within Q;
- the complementary **three non-anchor IDs** \(T(Q)=Q\setminus A(Q)\).

There can be no alternative choice of anchor using a different repeated point or line: the source multiplicity pattern already pins p and ell uniquely. Furthermore all six source IDs are distinct, and the three non-anchor IDs have pairwise distinct original point factors and pairwise distinct original line factors, each disjoint from p and ell. The original GQ incidence property ensures that q and r are nonincident: if q were incident with r, the three original source flags q—ell—p—r plus (q,r) would form a 4-cycle in the original incidence graph, forbidden by the generalized-quadrangle girth-eight axiom. The unique original nonincident source projection of (q,r) is precisely the displayed anchor.

This proves anchor uniqueness **from the sixset**, without invoking or assuming the physical endpoint projection used by the forward enumerator.

## 3. Recover both oriented physical three-edge chains independently

On the f-side, the two anchor flags with repeated original point p contribute twice its globally injected physical pair edge f(p). For the entire source sixset to touch exactly six physical coordinates of degree two, this repeated physical edge must occupy two coordinate symbols by itself; it must be disjoint from every other physical point pair edge. The four pair edges corresponding to the other four DISTINCT original point factors are simple pair edges on four other physical coordinate symbols, each of degree two; because each physical pair label is distinct and simple, those four edges form ONE simple \(C_4\) (there is no simple graph on four vertices with four pair edges, all vertex degrees two, other than \(C_4\)).

The four original point factors are q and the three point factors of the non-anchor IDs. Removing the actual edge f(q) from this \(C_4\) produces a **unique simple undirected path \(P_4\) on four physical left coordinate vertices** with exactly the THREE non-anchor IDs as its individually named edges. Such a simple \(P_4\) has exactly TWO directed vertex/edge traversals, which are exact reversals. Their ordered edge labels are the three *ORIGINAL SOURCE FLAG ID* values, not source point names, and there are no additional choices of left physical coordinates.

On the g-side, by exactly the same argument, the two anchor flags with repeated original line ell contribute g(ell) twice; removing the anchor edge g(r) from the simple right physical \(C_4\) on the four other ORIGINAL line factors produces the **unique right P4** with the SAME THREE non-anchor original flag IDs as its named edges. Again there are exactly TWO directed traversals.

Thus from any historically accepted B/B-overlap original sixset Q we can reconstruct, independently of any physical graph H, two explicit lists of at most two oriented coordinate sequences:
\[
\mathcal L(Q)=\{((x_0,x_1,x_2,x_3),(i,j,k)),
                ((x_3,x_2,x_1,x_0),(k,j,i))\},
\]
\[
\mathcal R(Q)=\{((y_0,y_1,y_2,y_3),(i',j',k')),
                ((y_3,y_2,y_1,y_0),(k',j',i'))\}.
\]

## 4. Align ACTUAL original flag identities, not only physical coordinates

To form a physical grid path \(v_t=(x_t,y_t)\), the t-th left physical edge and t-th right physical edge must arise from the **SAME original flag ID**, because the construction uses one common TRUE original incidence column on both sides. Therefore an orientation from \(\mathcal L(Q)\) and an orientation from \(\mathcal R(Q)\) form a valid source-backed directed three-edge path iff their triples of ORIGINAL flag IDs coincide **position by position**.

There are two possible left orientations and two possible right orientations. If the triples are incompatible even after reversal, there is no aligned pair. If one pair aligns, reversing both coordinate paths produces a second, distinct aligned physical directed path. There cannot be a third: for a fixed left orientation, the right named-edge sequence has a unique orientation if compatible, since its three distinct labels have two different reverse orders. Hence exactly ZERO or TWO directed paths arise.

For any aligned orientation the edge from \((x_t,y_t)\) to \((x_{t+1},y_{t+1})\) is one of the **two diagonals** physically produced by its source flag ID \((p_t,\ell_t)\), because its left coordinate difference is exactly f(p_t) and its right coordinate difference is exactly g(ell_t). Four left and four right coordinates are each distinct, so the resulting path is coordinate-proper. Its endpoint first pair is exactly f(q) (the missing C4 edge), and its endpoint second pair exactly g(r). Thus the original nonincident pair (q,r) is the precise forward-GQ-projection endpoint. The anchor p,ell has pair labels disjoint from the path's four left and four right coordinate symbols by the historical B/B acceptance criterion.

Consequently **each** of the aligned paths is legal for the forward #672/#673 original projection reconstruction, with exactly Q as its six-ID reconstructed image. In particular none of the six IDs are duplicated, and the actual source anchor is uniquely recovered.

If a chosen CORE retains all three non-anchor original flag IDs, the reconstructed physical path's three edges are present (both diagonals per retained original ID). The anchor IDs may lie OUTSIDE the core and are recovered from the FULL true source without replacement; the original invalidation Z is checked on all six IDs. Conversely any forward-produced path has all three non-anchor IDs in the core, its unique source anchor as above, and yields one of the two aligned orientations. This proves the forward map's exact two-to-one image multiplicity and its inverse characterization for all h.

## 5. Independent actual-original-source falsifiers

\`research/hyp105_BBo_inverse_source_bridge.py\` constructs the inverse of each ORIGINAL source sixset **without calling forward physical 3-walk enumeration, original source projection tables, or the published pinned W32/W34 outputs**. It:

1. checks true original six distinct incidence IDs and repeated source point/line B/B-overlap profiles;
2. uniquely partitions the three anchor IDs from the SIX genuine flags and obtains the remaining three source IDs;
3. checks the two physical degree-two six-symbol projections and that f(p),g(ell) are disjoint from the respective true C4s;
4. reconstructs the left and right source-ID-labeled three-edge coordinate paths by a separate graph-chain walk and aligns their THREE ACTUAL original flag ID sequences, returning zero or two reverse paths;
5. optionally requires all six actual IDs to avoid deleted source flags Z, while only the three non-anchor original IDs need belong to the sparse source core I.

\`research/test_hyp105_BBo_inverse_source_bridge.py\` uses the historical ORIGINAL GF(5) seven-class classifier to enumerate every historical B/B-overlap sixset from the full accepted W32 source left-sixset enumerator, for **FIVE distinct complete globally injected g reassignments**. It independently checks the inverse-produced original sixset population is EXACTLY the population obtained by forward #673's physical path construction, and verifies every inverse physical edge has its correct ORIGINAL flag provenance, for each complete full-map case. It also checks multiple sparsely retained original W32 cores with original deleted flags, W34 true-source sparse-core and forbidden-anchor controls (including anchors OUTSIDE the core), negative B/B-disjoint cases and malformed-source fail-closed behavior. This is a **bidirectional source-native** matching check, not merely comparing a new physical DFS with the original physical DFS.

No finite W32/W34 test can prove all-h asymptotic population bounds. The exact \(0/2\) inverse combinatorial lemma is proved abstractly in §§2–4 from the historical source B/B pattern, physical simple \(C_4\) factor degree-two condition, global pair-label injection, and original GQ no-4-cycle property. Those assumptions hold for every true original \(W(3,2^h)\). This result removes the source sixset-to-path multiplicity as an *unresolved internal review gate*, but does NOT independently reprove the mixed full/core source blocker or the entire universal Branch A. A qualified **external** scientific referee is still needed for #672–#676 and root #230 remains open.
