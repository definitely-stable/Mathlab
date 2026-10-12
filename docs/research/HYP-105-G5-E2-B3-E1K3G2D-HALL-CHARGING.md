# HYP-105 E1-K3-G2-D — exact Hall charging gate and finite NO-GO for direct Jcross→D6 injection

Date: 2026-10-12. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked child of [PR #376](https://github.com/definitely-stable/Mathlab/pull/376) at pinned `7adc87e63938abe529d30cb90f802f0e4cb70905`. Remains Draft, no main updates, no merge.

**Scientific status:** EXACT FINITE COUNTEREXAMPLE TO UNIT-CAPACITY PROPER-D6 CHARGING, plus a GENERALLY VALID FINITE HALL/flow characterization of capacity-limited charge maps. This is **NOT** a counterexample to seven-family S=Omega(s^6), or to existence of a bounded multiplicity M>1 in a different charging relation.

## 1. Why K3-G2-C data expose a substantive proof obstruction

Every proper Kikuchi D6 has six *different first* and *different second* physical coordinates, so no two of its six edges can be the two original diagonals from one incidence column: such a repeated original column would repeat both physical coordinates. Every proper D6 therefore uses six DISTINCT ORIGINAL incidence columns, and is an accepted positive motif.

By contrast, each off-original-source witness of Jcross is an original Kikuchi 6-cycle with precisely one **repeated** original incidence column. It is an improper cycle and NOT a proper D6. No silent identification between these different objects is valid.

Already at h=1, the independent accepted K1+B0 exact census proved:
- W(3,2), lex physical labels: D6 = 15.
- W(3,2), reverse-line labels: D6 = 3.

The independently certified K3-G2-C weighted original source witnesses were:
- lex: Jcross=36, of which `off_differentfoot_noncollinear`=18.
- reverse-line: Jcross=28, of which the heavy class=6.

Therefore a globally injective map from EACH witness to a DISTINCT proper D6 is **impossible**, regardless of proximity. By the pigeonhole principle, for ANY assignment to proper D6, the maximum target load MUST be at least ceil(36/15)=3 and ceil(28/3)=10 respectively, and at least 2 in each case for the selected heavy class alone. These are *exact finite counterexamples* to the hypothesis of unit-capacity charging for all s and all global f,g, NOT to issue #230's seven-family obstruction.

This lower bound on charging multiplicity is a necessary condition only. It is not evidence that some specified local rule can attain multiplicity 3 or 10: local neighborhoods may have isolated witnesses or Hall-deficient subsets and require more multiplicity or be impossible to charge locally at any finite M.

## 2. Local same-original-incidence charging relation

To avoid claiming arbitrary nonlocal proximity, define one fixed, independently testable candidate charging graph for one legal model:
- Left vertices = **individual** original-source-pair Jcross witnesses. Reconstruct the exact Kikuchi 6-cycle around one repeated anchor incidence (p,l), including two actual middle physical vertices; identify their original point/line origins from the entire global f,g pair map; keep only different original sources. Classify with the actual GQ unique anchor projection from K3-G2-C.
- Right vertices = proper D6 cycles enumerated with distinct x/y coordinates. Map all six Kikuchi edges back to exact original incidence columns; reject repeated-column anomalies.
- Left witness w is adjacent to right D6 c **iff c contains w's exact original repeated ANCHOR INCIDENCE column** (p,l). This is a deliberately strong locality condition, neither a theorem nor a claim that every successful all-h charging must use this adjacency.

This is stronger science than comparing only total Jcross vs D6: a witness can have NO candidate D6 at the chosen exact original column, or a cluster can violate Hall.

## 3. Exact Hall/flow theorem, finite certificate

For any finite bipartite witness-to-positive-motif graph G=(W,D,E) and integer k>=1, there is an assignment of EVERY w in W to one adjacent d in D with at most k witnesses charged per d IF AND ONLY IF

```
for every subset X of W, |X| <= k*|N(X)|.
```

Proof: replace every positive motif d by k copies and invoke finite Hall marriage theorem; equivalently use integral maxflow in network source→W capacity1, W→D capacity1, D→sink capacity k. The implementation computes exact integer maximum flow, extracts the reachable residual minimum cut, independently certifies its capacity matches flow, and searches for the **least feasible k** if there are no zero-degree witnesses. If there are zero-degree witnesses, no finite k works under this PARTICULAR local rule. An exact maximal partial assignment and minimum cut still quantify the obstruction.

The model-specific results are **finite falsifiers**, not a bound uniform in h; successful finite matching cannot be extrapolated.

## 4. Computational independence and acceptance

`research/hyp105_g5e2b3e1k3g2d_charging_hall.py` constructs witness paths DIRECTLY from the Kikuchi physical graph and the original edge→(point,line) provenance, not from the previously used TKT quadratic contraction. It constructs proper D6 vertex cycles directly and checks their six original edge labels. Only after generating the independent witness set does it reconcile counts for each of seven projection classes with K3-G2-C and proper D6 count with K1.

`research/test_hyp105_g5e2b3e1k3g2d_charging_hall.py` validates integer maxflow vs fully brute force assignment on synthetic bipartite graphs, verifies independently established W32 proper D6=15/3 and per-bin Jcross=36/28, the proof-theoretic capacity floors 3/10, and exact source edge provenance. All budgets fail closed. Additional deterministic W32 random map is report-only.

Dedicated path-limited GitHub-hosted workflow, inherited INDEX and Research; no local/self-hosted runner. Keep Draft pending exact HEAD three green checks and independent review.

## 5. What to do after this finite NO-GO

**Do not** attempt to prove a false all-h one-to-one charging of ALL Jcross (or just its heavy class) into D6. For original seven-family S there are six other accepted families, and a bounded-multiplicity map to their true weighted positive GF5 witnesses may still exist. K3-G2-E should identify the true accepted motif targets (rather than all full R3), and test a new charging relation with explicit source-column overlap and bounded fiber multiplicity. Any universal bound needs all s=2^h and all legal global f,g; finite flow checks alone do not prove it.

Alternative K3 full-R3 route: the exact separate coupled bound `(L(P3)-Theta)/12 - Jcross >= c s^6`, after K3-G2-A o(s^6) local losses. These goals are not interchangeable. No ASET exponent or Branch A/B decision is claimed.


## 2026-10-12 exact hosted discovery: ORPHAN witnesses defeat this local rule at ANY k

The [first hosted K3-G2-D Contract](https://github.com/definitely-stable/Mathlab/actions/runs/38205330816) independently verified the following all-integer results for the precisely defined **same original anchor incidence** charging relation:

| Legal W(3,2) globally coherent labeling | Jcross | Proper D6 | Max matching, k=1 | Left witnesses without ANY proper-D6 sharing original anchor | Heavy off-differentfoot-noncollinear count | Heavy class anchor-orphans |
|---|---:|---:|---:|---:|---:|---:|
| lex | 36 | 15 | 13 | **9** | 18 | **5** |
| reverse-line | 28 | 3 | 3 | **20** | 6 | **6** |
| random(seed=20261012) | 17 | 1 | 1 | **14** | 5 | **4** |

In the reverse-line labeling, all six heavily weighted off-differentfoot-noncollinear witnesses are anchor-orphans. Even if every proper D6 could accept an arbitrarily large number of witnesses, such a charging map CANNOT cover any anchor-orphan. This is strictly stronger than the global cardinality pigeonhole obstruction at k=1. A failed Hall matching does NOT imply the original risk obstruction fails: only the chosen very local target relation is ruled out.

The exact orphan counts for lex and reverse-line are frozen in independent hosted regression tests, separate from the generic exact maxflow/mincut and seven-bin source-ledger tests. All source incidence anchors and six columns are original W(3,s) objects, not projected independent labels.

**Next design requirement:** either relax locality with a proven bounded witness-to-positive-motif multiplicity, or charge to other truly accepted GF5 S-family motifs. Do not add more cross-origin subclasses without a positive-motif bridge.

---
