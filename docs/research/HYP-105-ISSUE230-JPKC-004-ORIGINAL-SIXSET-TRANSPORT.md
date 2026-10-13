# HYP-105 issue #230 — JPKC-004: exact ORIGINAL six-incidence transport of endpoint-storm collisions

**2026-10-13. STATUS: RESTRICTED_THEOREM_C / ORIGINAL finite source provenance. Root A/B OPEN.** Strict stacked child of [JPKC-003 Draft #427](https://github.com/definitely-stable/Mathlab/pull/427) at parent SHA `63991f778bf8b8665f914b056e15a6d7a5c0905f`. Work entirely on its own GitHub branch, `main` untouched, no mergers. Independent acceptance required.

## 1. Why this is the next proof gate

JPKC-003 proved a conditional necessary endpoint-source storm:
for any hypothetical globally complete original W(3,2^h) pair-map sequence with `S=o(s^6)`, either a BLOCKED endpoint-original-source `K_E=Omega(s^7)` collision term appears, or the internal-only `K_I=Omega(s^6)` defect persists. Neither conclusion alone is a contradiction. Simply renaming improper physical C6 paths as positive GF5 motifs would be invalid.

D6-Z (#428) separately proves that physical-image adjacency and whole-incidence wedge moments do not identify the seven selected GF5-positive original sixsets (W32 S68/S72 already refute that shortcut). Therefore JPKC-004 goes below aggregate moments: each physical path edge retains its EXACT ORIGINAL incidence ID, and every colliding path PAIR is classified by its six ORIGINAL incidence positions. ALL claims are for the SAME complete f,g and TRUE GQ geometry, with no resampling.

## 2. All-h theorem J9: canonical original GQ closure is a zero-conversion route for endpoint-bad anchors

Let q and r be NONINCIDENT ORIGINAL point and line. The GQ unique projection is q--ell--p--r. Denote the three ORIGINAL anchor incidence IDs by

`A(q,r) = ((q,ell),(p,ell),(p,r))`.

An oriented physical coordinate-proper simple three-path P with ORIGINAL grid endpoint labels (q,r) also has three ORIGINAL incidence IDs (these may or may not be among the three A incidence IDs). The canonical 6-position closure is the concatenation of the three P incidence positions and the three A incidence positions, **with multiplicity retained**; a true sixset may be taken only if all six IDs are different.

Define the ORIGINAL endpoint-bad predicate

`e(q,r) = [f(q) intersects f(p)] OR [g(r) intersects g(ell)]`.

**THEOREM J9 (ALL h, every globally injected original f,g):** If `e(q,r)` holds, then the six-position canonical closure has a physical coordinate degree at least **3** on the corresponding side. Therefore even if its six ORIGINAL IDs are all distinct, it CANNOT be six-coordinate 2-regular on both sides and CANNOT belong to any of the seven positive GF5 motif classes. This holds for each physical diagonal and every interior physical path, with no probabilistic assumptions.

**Proof.** If `x in f(q) intersection f(p)`, then among the three ORIGINAL anchor positions `(q,ell),(p,ell),(p,r)` alone, coordinate x occurs once at q and TWICE at p. Its left physical degree is therefore >=3 (any three P positions can only add degree). The dual argument uses a coordinate `y in g(r) intersection g(ell)` appearing once at r and TWICE at ell across the same three anchor incidences. Every accepted positive GF5 original sixset has six coordinate vertices of degree exactly 2 on each side. If the chosen six-position list repeats an ORIGINAL incidence ID, it is not even a valid sixset. QED.

**What J9 does NOT say:** It does not rule out **other** sixsets built from cross-anchor or alternative ORIGINAL incidences; it does not say that endpoint-bad original assignments have no seven-positive motifs. It specifically rules out the *direct unique-GQ 3+3 closure route* that works for unblocked B/B-overlap paths. This is a concrete local NO-GO for trying to convert the JPKC-003 endpoint storm by appending its own unique ORIGINAL anchor.

## 3. J10: exact original-sixset transport taxonomy, and a universal disjoint-pair multiplicity cap

For each oriented graph endpoint pair (u,v) that corresponds to an ENDPOINT-BAD original nonincident (q,r), enumerate all ORIGINAL blocked coordinate-proper simple paths `u-b-c-v`. For each two DISTINCT paths with identical oriented endpoints, retain their individual three ORIGINAL incidence IDs in the same original order; do not collapse repeated point/line factors and do not independently redraw labels.

Every ORDERED distinct collision contributes to EXACTLY one physical class:
- `shared_internal`: at least one common internal physical vertex;
- `improper_C6`: interior-disjoint simple graph six-cycle, but the six graph vertices repeat a first or second physical coordinate;
- `proper_C6`: interior-disjoint simple graph six-cycle, six distinct first and second physical coordinates.

Their ordered counts sum **exactly** to `K_E` from JPKC-003 and JPKC-002, on the same original f,g.

For each pair, form the union of the original incidence ID lists from the two paths. Partition into disjoint source states:
1. `original_incidence_repeat`: fewer than six distinct original incidence IDs (not a genuine sixset);
2. `left_not_2reg`: six distinct IDs but the LEFT six original incidence-position pair-label projection is NOT degree-two on precisely six physical coordinates;
3. `right_not_2reg`: LEFT passes but RIGHT does not;
4. `seven_selected`: both pass and the TRUE ORIGINAL W32 seven-family classifier accepts the sixset;
5. `two_reg_nonseven`: both pass but the W32 full original classifier rejects it (e.g. incorrectly matched original factor topology);
6. `two_reg_unresolved`: both pass but the general-h full source topology / GF5 charge was NOT evaluated. Never turn this state into a positive seven count.

For W32, the full original seven-census and selected GF5 lower numerator are cross-checked independently. W34 and true D4 W34 symplectic-spread are SOURCE-PROVENANCE and two-regularity proxies ONLY, not fake full-h seven classifiers.

**THEOREM J10 (ALL h, finite-to-all-h combinatorial cap):** Fix any set Q of six distinct ORIGINAL incidence IDs. The number of ORDERED interior-disjoint physical 3-path-pair collisions with the same ORIENTED endpoints whose six participating graph edges have exactly these ORIGINAL six IDs is at most

```
12 * 2^6 = 768.
```

**Proof.** The original injective pair maps generate exactly TWO physical graph diagonal edges per ORIGINAL incidence. Any given physical undirected graph C6 using Q selects one of at most 2^6 diagonal-edge assignments. Each assignment fixes six distinct physical graph edges and, if they form a simple C6, identifies at most ONE undirected cycle. Each simple undirected C6 yields exactly 12 ordered antipodal three-path pairs: 3 antipodal choices ×2 endpoint orientations ×2 path orders. Additional constraints (common ORIGINAL q,r anchor, endpoint-badness, coordinate-proper paths) only discard pairs. QED.

This is an **UPPER** multiplicity bound, not a proof that many endpoint collisions yield ANY accepted Q. It does not apply to shared-internal-vertex pairs, which may fail to form a simple C6; those are separately classified. The bound allows a future certified positive accepted-witness submass T to imply at least `T/768` distinct original sixsets, but it says nothing useful unless one first proves a lower bound for **TRUE accepted** T (including signed GF5 conditions), not just all endpoint collisions.

## 3a. Stronger all-h structural theorem J11/J12: ONLY D6 can survive direct two-path sixset transport

The initial exact original sixset transport gate revealed a much sharper
statement, which is independently provable for **every** h, not an
extrapolation of the W32/W34 tables.

**THEOREM J11 (ALL h, disjoint internal vertices).** Let P and P' be
distinct simple length-three paths in the TRUE Kikuchi physical graph G,
with identical ordered endpoints, and disjoint sets of internal graph
vertices. Their six physical graph edges form a simple graph C6.
Suppose all six ORIGINAL incidence IDs of these edges are distinct,
so they define a genuine ORIGINAL six-incidence set Q. Then:

```
Q has exactly SIX physical coordinates of degree TWO on EACH side
                 if and only if
the physical six-cycle is coordinate-proper (six distinct rows
AND six distinct columns).
```

**Proof.** The six original point-label pair edges `f(p_i)` are
exactly the six FIRST-coordinate transitions of the physical C6,
with multiplicity of the six ORIGINAL incidence positions preserved.
They therefore form a connected six-edge multigraph because the
physical graph C6 projects to a closed walk traversing all six
edges. If this multigraph is 2-regular on six vertices, it is a
connected simple C6; the six-coordinate projected CLOSED six-step
walk traverses that cycle and visits each projected vertex exactly once.
Hence the six original graph vertices of the physical C6 have six
different first coordinates. Conversely, six distinct first
coordinates on the physical C6 obviously imply exactly degree 2
on each of those six coordinates. The second-coordinate argument
is identical. By the independently proved Kikuchi K1 identity,
a coordinate-proper physical C6 of the ORIGINAL graph is precisely
the accepted ORIGINAL **D6** class. QED.

**THEOREM J12 (ALL h, shared internal graph vertex).** Two distinct
length-three paths with identical ordered graph endpoints and
sharing at least one internal graph vertex have at most FIVE distinct
physical graph vertices in their union (two common endpoints and
at most three distinct internal vertices). Each first-coordinate
or second-coordinate physical projection therefore has at most
five touched distinct symbols. Consequently their six ORIGINAL
incidence positions, even if pairwise distinct, CANNOT have exactly
six physical coordinates of degree 2 on either side. QED.

These two cases are exhaustive. Repeated ORIGINAL incidence IDs
are not a sixset at all. Thus **no** direct union of two physical
three-paths with identical oriented endpoints can be one of the
OTHER SIX accepted GF5 seven-family classes. The ONLY possible
genuine positive-class sixset is D6 arising from a physical
coordinate-proper C6.

This no-go is NOT the claim that other six classes are impossible
in the full ORIGINAL model: those classes do exist. It says
that the PARTICULAR two-path endpoint collision witness map used
by JPKC-001/002/003 cannot supply them.

**THEOREM J13 (ALL h exact accepted witness identity and necessary
loss).** Let T_E be the number of ORDERED endpoint-bad BLOCKED
three-path-pair collisions whose union is SIX DISTINCT ORIGINAL
incidences and whose left and right physical projections are
both six-coordinate 2-regular. Theorems J11/J12 show

```
T_E = K_E(proper physical C6) <= 12 D6 <= 12 S.
K_E - T_E = K_E(shared internal) + K_E(improper physical C6).
```

This is an EXACT identity of oriented ordered witness counts for
every legal complete original f,g, not an assertion that all
original S seven-family motifs are represented in the collision
system. If a HYPOTHETICAL small-S counterfamily follows JPKC-003's
endpoint branch (`K_E >= (4-o(1))s^7` and `S=o(s^6)`), then

```
0 <= T_E/K_E <= 12S/[(4-o(1))s^7] = o(1/s).
```

That is, essentially the ENTIRE leading endpoint storm is
*provably nonconvertible by the direct six-incidence two-path
union*. This does not rule out a NEW higher-order witness map
using extra ORIGINAL incidences or multiple GQ anchors, and
does not prove Root A/B.

### Exact true ORIGINAL finite controls

All values below are ORIENTED ORDERED endpoint-bad BLOCKED
three-path collision counts on the SAME complete f,g. Both J9
and J11/J12 hold for ALL h; the finite values merely independently
falsify an incorrect implementation.

| TRUE original f,g | K_E total | Source-positive direct T_E (ONLY D6) | Unconvertible direct source collisions |
|---|---:|---:|---:|
| W32 lex | 1,456 | 64 | 1,392 |
| W32 reverse | 1,060 | 24 | 1,036 |
| W32 S68 | 444 | 0 | 444 |
| W32 S72 | 624 | 0 | 624 |
| W34 lex | 128,912 | 47,400 | 81,512 |
| W34 random | 87,996 | 33,400 | 54,596 |
| W34 D4 real symplectic spread | 116,600 | 42,940 | 73,660 |

On W32, actual FULL original GF5 seven-class oracle certifies that
the only accepted collision-union sixset tag is D6. On W34, the
all-h J11/J12 structural proof certifies D6 for source-distinct
coordinate-proper cycles WITHOUT misrepresenting that as execution
of a full W34 seven-class GF5 enumeration. The W34 code marks
the OTHER class evaluation as unavailable, and refuses to infer
any additional positive motifs from its broader ORIGINAL
six-incidence population.

**Research decision:** the naive JPKC-004 idea of using endpoint
storm pairs to produce the OTHER SIX classes is a rigorously
**closed restricted route**. Do not keep enlarging its finite
collision tables. Next study a NEW original witness architecture
using at least one extra source incidence or a second ORIGINAL
GQ anchor, and prove nontrivial bounded multiplicity before
claiming any root all-h compensation.

## 4. Computational independent falsification contract

`research/hyp105_issue230_jpkc004_original_sixset_transport.py`:
- pulls ONLY complete true-original globally injective W(3,s) point/line physical pair maps and keeps all original incidence IDs;
- applies theorem J9 to EVERY endpoint-bad coordinate-proper physical path's canonical 3+3 ORIGINAL GQ closure, with independent degree frequencies for each original physical coordinate and repeated-ID rejection;
- enumerates all endpoint-bad ordered collision pairs and exact physical graph intersection types, then partitions by source-repeat and genuine original physical 2-regularity;
- at W32 alone, uses the independent FULL original seven-class classification and checks positive witnesses against the separate exhaustive true-original seven-census;
- checks each original sixset's interior-disjoint ordered witness multiplicity <=768, and overall `sum typed=K_E` against independent JPKC-003;
- fails closed on illegal global maps, path budget, endpoint-pair enumeration budget, source-sixset cache budget and any scope outside W32 for the exact seven-class checker.

Real fixtures: W32 lex/reverse/S68/S72; W34 lex/random; genuine original Desarguesian symplectic-spread W34 with independent D4 `M_f` measurement. `W(3,8)` is not represented as a complete source-sixset transport computation; graph-only work at W38 must not be relabeled as a full census.

## 5. Acceptance and next analytic decision

The research contribution is an ORIGINAL provenance transfer and an **ALL-h zero-route theorem J9** plus small universal cap J10, not an all-h unconditional S lower bound.

The crucial question is now falsifiable: among the `K_E` source-collision storm, how much (if any) already maps to:
- six DISTINCT original incidence IDs;
- 2-regular physical projections on both sides;
- a PROVED seven-positive GF5 original class?

Classify the losses in this order. If W32 low-S cases destroy the naive proxy, prioritize finding a **different** source combination (cross-anchor or extra original incidences) before claiming any all-h source compensation. If true GF5-positive witnesses occur in the shared-internal sector, quantify their original source multiplicities and whether they can be charged with a uniform all-h bound. Do NOT treat the physical all-image Ahlswede–Katona bound or a 2-regularity proxy as a seven-positive certificate.

**Acceptance:** final PR HEAD specialized GitHub-hosted CI, INDEX, Proof Audit, and full Research must all PASS, and an independent mathematical audit remains mandatory prior to merger. Branch A/B and issues #230/#176/#169 OPEN. No `main` changes, no merge, no ASET exponent, no full R3 upper.
