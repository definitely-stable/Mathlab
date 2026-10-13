# HYP-105 issue #230 — JPKC-006: sharp ORIGINAL three-incidence seed charge and non-GQ complement taxonomy

**2026-10-13. STATUS: RESTRICTED_THEOREM_C (all-h J18–J21, no Root A/B) plus EXACT W32 original census and targeted source-complete W34 witnesses.** Strict stacked Draft child of fully 4/4 green JPKC-005 [#431](https://github.com/definitely-stable/Mathlab/pull/431), parent exact HEAD `8139eaf2692f26ee860f3b0fd08108e41657e92f`. Do NOT merge/change `main`. Original HYP-105 issue #230 stays OPEN.

## 1. Critical mathematical correction of the witness-count scale

JPKC-005 J14 proved a safe but very wasteful generic **320** upper bound: choose three of six source IDs, choose one of two physical diagonals on each, orient. It ignored that a **coordinate-proper** physical 3-path P projects to a physical simple P4 on EACH side, so source triple T must be a physically compatible path on BOTH sides.

JPKC-006 uses this compatibility and the TRUE source sixset's A/B/C half topology. Both proof and test use ONE same fully complete globally injective original point and line pair maps f,g and the actual ORIGINAL incidence matrix. No independent per-anchor maps, no made-up projected labels, no W34 full S enumeration.

## 2. THEOREM J18 (ALL h): at most TWO oriented proper physical P3s from a fixed original 3-ID source triple

Let T contain THREE DISTINCT ORIGINAL incidence IDs and let `P_T` be all coordinate-proper oriented graph P3s (simple four grid vertices, four different physical first and four different second symbols) using EXACTLY the three original physical graph incidence IDs T, each once. Then

```
|P_T| <= 2.                         J18
```

**Proof.** A coordinate-proper grid P3 projects on the first physical coordinate and separately on the second physical coordinate to an undirected SIMPLE three-edge P4, because its four row symbols and four column symbols are distinct. Consequently T's three physical first-factor edges and three second-factor edges, if they can support ANY such P3, are each a fixed undirected P4; in particular T has THREE distinct original point factors and THREE distinct original line factors. Each P4 has exactly TWO oriented traversals, BUT the original source incidence IDs label the three edges distinctly on BOTH row and column paths. An oriented physical graph path must traverse the SAME sequence of three original incidence IDs in both projections: for any chosen row orientation, there is at most ONE column orientation whose three-ID edge sequence agrees. Thus at most two oriented grid paths exist (the physical path and its exact reversal), not four independently chosen directions. If the row/column source edge orders are incompatible, no such path exists. This argument works for ALL h, needs no probabilistic assumption, and is independently verified by the local graph-edge oracle. QED.

**Implementation:** independent per-T local oracle enumerates both diagonal edges of all THREE original incidence IDs, all six edge orders, all eight diagonal choices, and independently tests graph-path connectivity and full coordinate properness; it MUST find <=2. This oracle neither imports nor trusts the global projection-path loop for its answer.

## 3. THEOREM J19 (ALL h): 12, not 320, proper P3s per positive ORIGINAL sixset Q

For an accepted original six-incidence set Q, the physical first-side and second-side six edges are each two-regular on EXACTLY six physical coordinate symbols. The ORIGINAL source factor frequency partitions are A=(1,1,1,1,1,1), B=(2,1,1,1,1), or C=(2,2,2), with only the seven certified GF5 classes allowed.

Each coordinate-proper P3 source triple T contained in Q projects to an undirected P4 on each side. The following **geometric restrictions are ALL-h**:

- **A side:** six physically distinct edges form C6 or two disjoint C3s; since an embedded P4 uses 4 connected physical symbols, the C3+C3 possibility contains NO P4. Hence only an actual C6 can occur and its P4 3-edge subset must be one of the SIX consecutive 3-edge runs.
- **B side:** the doubly occurring original factor edge contributes a 2-cycle between TWO vertices already of physical degree 2, disjoint from the four other singly occurring original edges. The four singles necessarily form a simple C4. A physical P4 cannot use the doubled factor edge and must use exactly three of the four C4 edges; at most FOUR candidate original 3-ID subsets.
- **C side:** three disjoint doubled physical edges (three 2-cycles), each with only two physical vertices. NO connected four-symbol P4 is possible, so zero seeds.

Combining J18 with the stronger half-side restriction yields an ALL-h charge independent of s:

| Accepted ORIGINAL class | Source half pattern | Max source T P4 triples | Max oriented physical P3 seeds per Q |
|---|---|---:|---:|
| D6 | A/A | 6 | **12** |
| B-left/A-right | B/A | 4 | **8** |
| A-left/B-right | A/B | 4 | **8** |
| B/B-overlap | B/B | 4 | **8** |
| B/B-disjoint | B/B | 4 | **8** |
| C/A | C/A | 0 | 0 |
| C/B | C/B | 0 | 0 |

These maxima are SAFE upper bounds. They are NOT necessarily attained by every assignment; however W32 lex attains the D6 upper 12, so the global J19 constant **12 is sharp for legal ORIGINAL maps**. The W32 source-triple maximum is exactly TWO, attaining J18. Every nonempty local source triple realization contains the two physical path reversals.

These maxima are SAFE upper bounds, not necessarily achieved. The D6 source cycle must match across both physical sides, which may further reduce its feasible seed count.

**THEOREM J19:** For ANY complete globally injected f,g at ANY h, every selected original sixset Q contains at most **12** oriented coordinate-proper physical P3 seeds, including endpoint-bad, nonincident original endpoints and any other special subclass:

```
H_E = # {(P,Q): P is endpoint-bad coordinate-proper physical P3,
                   Q is selected original positive sixset,
                   T(P) subset Q}
    <= 12 S.
```

Hence `# endpoint-bad seeds admitting >=1 positive sixset <=12S`. This strictly sharpens 320 to 12, a factor `26 2/3`, without claiming a new unconditional lower for S.

## 4. THEOREM J20 (ALL h): COMPLETE non-GQ U source topology taxonomy

For any endpoint-bad proper physical three-incidence seed T, take ANY **genuinely selected positive** sixset Q containing it and put U=Q\T (three ORIGINAL incidence IDs disjoint from T). JPKC005 J15 forbids both C classes and J17 + original GQ uniqueness forbids B/B completions (a 3-source factor P4 would have to be the canonical forbidden q–ell–p–r). Consequently, ONLY THREE motif types remain possible, with the following **exact original bipartite incidence graph U** shapes:

1. **D6 (A/A): `matching_3K2`**. The three U original point factors and three U original line factors are all DISTINCT: three disjoint original point–line incidence edges (matching).
2. **B-left/A-right (B/A): `point_wedge_plus_edge`**. The left physical C4+C2 requires U to contain **one original point factor q=f^-1({x0,x3})** once, and a distinct original point p' twice on its completely new edge f(p'), outside the physical row P4. The three right source line factors are ALL distinct, so the U original incidence graph is a two-edge wedge at p' plus an ORIGINAL isolated incidence (q,r') incident with q. This is not an original q–ell–p–r GQ 3-walk.
3. **A-left/B-right (A/B): `line_wedge_plus_edge`**, dual to the previous case. U contains one original line r=g^-1({y0,y3}) once, plus a distinct original line ell' twice with its physical edge g(ell') outside the column P4; the three U original points are distinct. U is a two-edge wedge at ell' plus an original isolated incidence.

**No second original GQ 3-walk U is possible** (J17); its underlying source multiset shape B/B would force canonical and thus violate endpoint-bad J9. C/A and C/B cannot be reached because they contain a C physical side.

This is an **EXHAUSTIVE topology theorem for THIS positive extension construction**, not a classification of arbitrary three-incidence configurations or of all positive original sixsets. It is a new exact guide to what an eventual cross-anchor or source-capacity compensation theorem must count.

### Source witnesses and global image capacity

The new targeted source-completion oracle constructs each of the three possible types from the actual globally fixed ORIGINAL factor maps:
- A-half: from projected P4 coordinates `x0,x1,x2,x3`, enumerate the missing C6 edge path `x3–z4–z5–x0` for ALL ordered distinct `z4,z5` outside those four symbols. Resolve every edge to its exact ORIGINAL factor via f^-1 or g^-1; reject missing edges and reused T factors.
- B-half: choose which of the three additional A-half original factors supplies the unique original endpoint chord q (or r), and force the remaining two to meet at a TRUE common original point/line p' (or ell') by the actual original GQ incidence relation. Verify f(p') or g(ell') completely disjoint from the seed's physical P4 coordinates; no independently sampled labels.
- D6 (A/A): join left/right true original A-half three-edge completions into three genuine original incidences, check **actual source incidence matching** and require the exact connected matched ORIGINAL dual six-cycle D6; reject all physically two-regular but unmatched A/A cycles.

This enumerates **ALL selected Q of these permitted classes for each targeted input physical seed**, without constructing an all-sixset index at W34.

## 5. Exhaustive W32 double-oracle and bounded truthful W34 stress

The dedicated runnable implementation `research/hyp105_issue230_jpkc006_source_topology_sharp_charge.py`:
1. checks EVERY endpoint-bad proper physical seed in each W32 lex/reverse/S68/S72 input;
2. independently constructs ALL possible true-original positive completions of the three permitted motif classes directly from physical A-cycle + original wedge geometry (does not query selected sixset census for candidate discovery);
3. cross-checks its entire per-seed result with the separate **exhaustive 62,370 original-left candidate** seven-family GF5 positive-sixset index from JPKC005, with exact original Q incidence IDs;
4. independently enumerates local source three-incidence diagonal assignments from scratch for all accepted sixsets and checks per-class bound 12/8/0 versus the pre-existing global P3 oracle;
5. checks every successful U source graph is exactly matching / point wedge / line wedge as promised, with no GQ walk, repeated original incidences, or fake positive class.

On W34 lex/random and genuine D4 symplectic-spread global complete f,g, the script performs **ALL permitted true ORIGINAL alternate Q completions for a deterministically spread selection of 96 endpoint-bad proper seeds PER input** and records the actual accepted sources. This is a **complete per-seed** calculation on 96 selected seeds, NOT a complete W34 seven-family census, NOT a claim about all W34 endpoint-bad seeds, and NOT an all-h sampling theorem. The per-seed source query is physically and combinatorially complete in the three reachable classes, not a heuristic nearest-neighbor selection.

All finite tests run on GitHub-hosted runners; never run self-hosted hardware. Invalid global injections, full seven-Q scope outside W32, missing physical labels and path budgets fail closed.

## 5a. Exact source-positive completion controls and the crucial finite-size contrast

Every W32 row below is an **exhaustive** source-original survey of ALL
endpoint-bad coordinate-proper physical three-path seeds on that complete
original GQ. Every accepted completion was independently found twice:
once by the new matching/wedge constructive source algorithm, and
again by looking up all actual source-positive Q in the independent
62,370-candidate ORIGINAL W32 seven-family census.

| ORIGINAL map | Full endpoint-bad E | Physically checked | Seeds with >=1 selected Q | Accepted ordered (P,Q) hits | Max seed paths per accepted original Q |
|---|---:|---:|---:|---:|---:|
| W32 lex | 786 | 786 | 154 | 214 | **12** |
| W32 reverse | 676 | 676 | 86 | 90 | 8 |
| W32 S68 | 544 | 544 | **8** | 8 | 2 |
| W32 S72 | 600 | 600 | **10** | 10 | 2 |

The W32 lex attains J19's 12-charge upper bound, while every
nonempty true-original source triple checked has exactly two
physical oriented path realizations (the path and its reversal),
attaining J18's universal bound 2.

On W34, the new constructive oracle fully enumerates the permissible
source-completions for **96 deterministically evenly distributed**
eligible physical seeds from each complete original map, without
claiming either a random sample or a full original seven-family census:

| TRUE original W34 map | Full E (for context ONLY) | EXACT selected seed count | Seeds with >=1 accepted Q | Accepted (P,Q) hits | A-left/B-right | B-left/A-right | D6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| lex | 38,020 | 96 | 94 | 545 | 182 | 222 | 141 |
| random | 30,194 | 96 | 95 | 430 | 172 | 162 | 96 |
| genuine D4 symplectic spread | 35,190 | 96 | 94 | 537 | 212 | 193 | 132 |

The selected 96 source seeds are **not probabilistic observations**;
selection is uniformly spaced in the enumerator's deterministic
ordered full genuine endpoint-bad seed sequence. Every selected
seed receives a COMPLETE constructive all-target source completion
search, but NO inference about all unexamined W34 seeds, about
uniform extension coverage for s>=8, or about `S=Omega(s^6)`
is authorized. The W32 S68/S72 severe extension isolation
demonstrates why a naive universal pointwise extension claim is
unsafe despite these W34 finite targeted positive examples.

## 6. CONDITIONAL all-h isolation consequence J21 (NOT Root A/B)

Take any hypothetical unbounded family of legal complete f_s,g_s with `S_s=o(s^6)`, and suppose it falls into JPKC003's endpoint-dominated branch:

```
E_s >= (8-o(1))s^6.
```

J19 charges at most 12 endpoint-bad physical seeds per selected true original sixset. Therefore at least

```
E_s - 12 S_s = (8-o(1))s^6
```

endpoint-bad proper physical P3s have **ZERO** accepted ORIGINAL six-incidence completion whatsoever (not merely zero canonical/second-GQ completion). Indeed the fraction of seeds covered by ANY selected Q is <=12S/E=o(1). This conditional *isolation* theorem sharpens JPKC005 by 320/12 but is **not a contradiction**: the low-S adversarial maps could realize almost-completely isolated endpoint-bad seeds.

An eventual proof of Root A would need an independent all-h **extension-existence** inequality (`# covered endpoint-bad seeds >= epsilon s^6`) on the endpoint branch, or a new joint global geometry/occupied-image moment inequality that eliminates simultaneous isolation and internal-only defect concentration. J18–J21 only give charge/obstruction, NOT positive existence.

### Next mathematically defensible stage JPKC-007

Use the exact source `matching_3K2`, `point_wedge_plus_edge`, `line_wedge_plus_edge` taxonomy to derive source-demand constraints on the original incidence graph and physical pair-edge image capacity. Validate any candidate quantitative extension theorem against low-S W32 S68/S72 and D4 W34. Avoid further independent large CI sweeps or re-proving J9/J17.

**Acceptance gate:** FINAL PR HEAD specialist CI, INDEX, Proof Audit, and Research SUCCESS, plus independent mathematical review before merge. Original issue #230/#176/#169 OPEN. No main modification, merge, all-h Root A/B, ASET exponent or strict full R3 claim.
