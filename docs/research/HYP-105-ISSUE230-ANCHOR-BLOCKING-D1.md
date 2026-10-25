# HYP-105 issue #230 — D1: exact original-GQ anchor-blocking tensor and endpoint congestion

**2026-10-12. STATUS: RESTRICTED_THEOREM_C / EXACT_LEDGER / MAIN_ROOT_A_B_OPEN.** This stacked Draft is based on [PR #394](https://github.com/definitely-stable/Mathlab/pull/394) exact HEAD `aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d`, not on the falsified P2/P7 transport stack #386–393. The user-visible question is the obstruction to the all-label `S_s(f,g)=Omega(s^6)` Branch A. The global `f,g` are ONE SAME genuinely injective physical unordered-pair labeling of ORIGINAL `W(3,s)` point and line objects. No changes to main. Neither Branch A nor B is established.

## 1. The exact remaining gate from the parent result

PR #394 establishes (with the parent proof scope) a coherent subgraph H and at least `(16-o(1))s^6` proper oriented physical three-paths with complete physical endpoint pair labels. The ORIGINAL GQ projection fixes the unique original nonincidence anchor

    q -- l -- p -- r,

where q is the physical endpoint-pair point, r the endpoint-pair line, p the additional ORIGINAL point and l the additional ORIGINAL line. For nonincident (q,r), the original projection is unique.

The path closes to one accepted synchronized BB-overlap sixset iff `f(p)` is disjoint from all four physical left coordinates of the path and `g(l)` disjoint from all four physical right coordinates. Exact good closure multiplicity is TWO oriented paths by physical path reversal. Its complement in nonincident, endpoint-complete paths is the blocked mass `C`. The parent inequality is

    (16-o(1))*s^6 <= C+2*S+sqrt(192*m*S),  m=2V(s+1).

To close A it is sufficient to find a fixed eta>0 with `C <= (16-eta)s^6+o(s^6)`. The weaker **amortized** sufficient alternative is `C <= (16-eta)s^6+Lambda*S+o(s^6)` for any fixed Lambda>=0, because then `eta*s^6 <= (Lambda+2)S+sqrt(192mS)+o(s^6)`. If S=o(s^6), `sqrt(mS)=o(s^6)`, contradiction. These are PROPOSED proof gates, not proved inequalities.

## 2. New exact ALL-h 16-atom identity

Let a proper oriented physical path have grid vertices `(x0,y0),(x1,y1),(x2,y2),(x3,y3)`, with all four x coordinates distinct and all four y coordinates distinct. Its labeled endpoints are ORIGINAL `q=f^{-1}({x0,x3})`, `r=g^{-1}({y0,y3})`. For nonincident q,r let original projection be `(p,l)`.

Define Boolean indicators:

    LE:  f(p) intersects {x0,x3}     left ENDPOINT blocking
    LI:  f(p) intersects {x1,x2}     left INTERNAL blocking
    RE:  g(l) intersects {y0,y3}     right ENDPOINT blocking
    RI:  g(l) intersects {y1,y2}     right INTERNAL blocking

Encode `mask = LE + 2 LI + 4 RE + 8 RI`. Every nonincident endpoint-complete proper oriented three-path has EXACTLY ONE mask from 0 to 15, and reversal fixes its mask. Let `C_b` be its count for each mask b. Then

    all nonincident endpoint-complete paths = sum_{b=0}^{15} C_b,
    2*BB_sync(H) = C_0,
    C = sum_{b=1}^{15} C_b.

Crucially, disjoint EXACT atoms permit addition without false inclusion/exclusion or silently double counting a path whose anchors collide on both sides. Define disjoint categories

    C_endpoint_only = sum_{b: b&5!=0, b&10==0} C_b,
    C_internal_only = sum_{b: b&5==0, b&10!=0} C_b,
    C_mixed = sum_{b: b&5!=0, b&10!=0} C_b.

Then `C=C_endpoint_only+C_internal_only+C_mixed`. No positivity or rarity of any of these terms follows from this algebraic decomposition.

## 3. All-h ORIGINAL endpoint-pair identity (not a blocked-path estimate)

Let `B_L` denote all nonincident original pairs `(q,r)` with unique projection `q-l-p-r` for which `f(p)` meets `f(q)`, and `B_R` similarly when `g(l)` meets `g(r)`. These predicates depend ONLY on original endpoint pair q,r and the one fixed global f,g, not the internal path. The original GQ axiom gives the exact identity

    |B_L| = s*sum_{l,x} r_{l,x}(r_{l,x}-1),
      r_{l,x} = # {q original point on line l : x in f(q)}.

By line/point duality,

    |B_R| = s*sum_{p,y} t_{p,y}(t_{p,y}-1),
      t_{p,y} = # {r original line through p : y in g(r)}.

**Proof:** An ordered distinct pair q,p on one ORIGINAL line l with physical f(q),f(p) sharing coordinate x determines s choices of r through p other than l. The ORIGINAL generalized quadrangle projection of nonincident q,r is exactly (p,l). Conversely every left-bad nonincident pair has exactly that provenance; global injectivity of physical unordered pairs ensures at most one coordinate x is common. The right statement is the actual typed ORIGINAL dual, not an independent newly sampled graph. These counts are **exact all-h identities** and each is O(s^5) using the parent GQ pencil spectrum estimate.

Let `N_{q,r}` be the number of oriented physical proper endpoint-complete H three-paths with ORIGINAL endpoint pair q,r. Define the endpoint-bad weighted mass

    C_endpoint_mass = sum_{(q,r) in B_L union B_R} N_{q,r}.

Then the new sixteen-atom identity proves the EXACT all-h relation

    C_endpoint_mass = C_endpoint_only + C_mixed.

For each bad endpoint pair, ALL its proper paths are blocked at their endpoints, regardless of internal coordinates. The parent bound `|B_L union B_R|=O(s^5)` bounds only the NUMBER of pairs; it does not control `sum N_{q,r}`. An assertion `C_endpoint_mass=O(s^5)` would require uniform `N_{q,r}=O(1)`, which is NOT provided and is not assumed.

The remaining term

    C_internal_only = sum_{(q,r) not in B_L union B_R}
                     #(paths with LI or RI)

requires NEW cross-map information on the internal physical coordinates. Reducing only the endpoint-bad set cannot complete Branch A.

## 4. Independently falsifiable finite contract

Executable: [source](../../research/hyp105_issue230_anchor_blocking.py) and [tests](../../research/test_hyp105_issue230_anchor_blocking.py). Uses [parent canonical original GQ](../../research/hyp105_issue230_projection.py) for validity of same coherent global f,g and exact unique projection. It performs a separate complete physical three-path scan, without importing the parent classifier or its census result.

Every finite run verifies:
- the original and the TRUE original-dual `s*sum r(r-1)` pair counts by two structurally different algorithms (direct original projection and pencil aggregation);
- EXACT 16 disjoint atom totals, reversal-even multiplicities and no discarded paths;
- endpoint-bad pair weights via an independent grouping and a path-independent physical label predicate;
- zero mask / good ORIGINAL synchronized BB-overlap multiplicity 2;
- all original projection counts and unrestricted pair congestion (max and largest original (q,r) fibers);
- a genuinely INDEPENDENT second exhaustive enumeration for W32/W34 that fixes q,r FIRST, chooses first/last neighbors and tests the MIDDLE edge; its 16-atom array must exactly match the forward path scan;
- equality to parent canonical proper/missing/incident/blocked/unblocked totals on EVERY complete named fixture.

Pinned finite maps are W32 lex, reverse, known **S68** and S72; W34 lex and seeded random; W38 seeded random. S68 refutes universal exact unit-mean P2/P7 but does NOT refute all-h `S=Omega(s^6)`. W38 full finite scan runs only when the complete path budget fits; overbudget requests fail closed, never produce partial negative evidence.

No fixed finite W32/W34/W38 experiment can certify that the proportion of endpoint/internal blocking remains high or low as s grows. In particular the C16 and exact source support results are **not** a new universal bound on C.

## 5. Next mathematical step, D2

Investigate the weighted ORIGINAL endpoint relation `B_L union B_R`, not only its O(s^5) pair count. The existing mixed-book inequality for a candidate relation `B` is

    P_B <= 24*t*sum_v d_B(v)d_H(v) + sqrt(192*|B|*D6(H)),

and cannot close the gate from `|B|=O(s^5)` alone. D2 should either establish an ORIGINAL GQ-specific upper for `sum d_B*d_H` / the exact per-pair path congestion, or explicitly falsify a proposed scale. For internal-only blocking, derive an incidence-conditioned tensor and test compensation into other accepted positive families CA/CB/BB, rather than a generic random mean. A viable final amortized form is

    C <= (16-eta)s^6+Lambda*S+o(s^6),

where eta, Lambda are absolute and independent of f,g. This is a sufficient PROPOSAL only; proving the identity C=C_endpoint_mass+C_internal_only is not a proof of this inequality.

Acceptance: one focused GitHub-hosted Contract, INDEX, complete Research on the SAME final HEAD, and separate external mathematical review. Do not merge main, close #230/#176/#169, claim ASET exponent or reanimate false P2/P7.


## 6. Exact hosted finite result — calibrated split and per-pair congestion

The first dedicated hosted [Contract #38282150953](https://github.com/definitely-stable/Mathlab/actions/runs/38282150953) **SUCCESS** on the original full 16-atom ledger, including the independent endpair-first/middle-edge verification for W32 and W34, complete W38 global fixture, both ORIGINAL typed incidence pencil formulas, and agreement with the independent parent proper-path census. These data are all ORIGINAL globally coherent f,g; they are *not* independent physical f/g draws within a state.

| GQ state | blocked C | endpoint-only | internal-only | mixed endpoint/internal | endpoint-bad weighted mass |
| --- | ---: | ---: | ---: | ---: | ---: |
| W32 lex | 942 | 168 | 156 | 618 | 786 |
| W32 reverse | 898 | 142 | 222 | 534 | 676 |
| W32 S68 | 606 | 52 | 62 | 492 | 544 |
| W32 S72 | 658 | 68 | 58 | 532 | 600 |
| W34 lex | 55,384 | 22,056 | 17,364 | 15,964 | 38,020 |
| W34 random | 48,542 | 18,034 | 18,348 | 12,160 | 30,194 |
| W38 random | 1,888,776 | 851,208 | 869,548 | 168,020 | 1,019,228 |

Additional EXACT underlying ORIGINAL pair statistics:

| State | # nonincident ORIGINAL pairs | # endpoint-bad ORIGINAL pairs | Max paths / one pair | Max paths / endpoint-bad pair |
| --- | ---: | ---: | ---: | ---: |
| W32 S68 | 180 | 166 | 12 | 12 |
| W34 random | 6,800 | 3,203 | 36 | 34 |
| W38 random | 336,960 | 70,174 | 54 | 54 |

**Mechanistic reading:** in S68, endpoint conflicts affect 544/606 blocked paths, but another 62/606 are **internal-only** despite safe physical endpoint anchors. In random W38, internal-only accounts for 869,548 blocked paths, almost as many as all endpoint-only blockers (851,208); these internal-only paths cannot be controlled merely by eliminating the `B_L union B_R` endpoint-bad original pair relation. Conversely `|B_L union B_R|=70,174` contributes `1,019,228` distinct oriented physical P3s in W38, so *counting original endpoint pairs is mathematically not counting paths*.

The ratio changes across these small finite h and may reverse under adversarial globally coherent maps. No asymptotic statement about any of these ratios is claimed. A claim `C=o(s^6)` remains UNPROVED, and the known S68 counterexample to unit-mean P2/P7 remains intact.

**Concrete D2 proof split:** establish (or falsify) an upper or compensated estimate on
```
E(f,g) = sum_{(q,r) in B_L union B_R} N_{q,r},
I(f,g) = sum_{(q,r) not in B_L union B_R}
             #(proper original projected paths blocked internally),
C=E+I.
```
An upper on E alone is INSUFFICIENT. Both terms depend on the SAME globally coupled f,g. A valid useful result could bound E+I by `(16-eta)s^6+Lambda*S+o(s^6)`, or provide separate bounds whose constants add to less than16. None is yet proved.
