# HYP-105 / #230 — JPKC-010: coherent mixed D6/B–A/A–B ORIGINAL transfer

**14 October 2026 — research-only, strictly stacked on JPKC-009 PR #439 at pinned parent HEAD `a3b7d749604896dcbaeae5e594cc2ac6d087e49f`. Branch A/B OPEN, do not merge into main without independent review.**

## 1. What #230 actually requires

For **all** s=2^h, **all** complete globally injective original point/line maps f,g into physical coordinate pairs, seek either an all-h uniform `S_s=Omega(s^6)` positive ORIGINAL seven-family sixset obstruction, or an explicit infinite correlated counterfamily with `S_s=o(s^6)`, or a rigorous equivalent restricted reduction. The actual GF(5) necessary R3 floor counts seven **distinct ORIGINAL six-incidence** classes, not signed events. Finite W32/W34 or a lower bound for just three seed-reachable classes cannot by themselves close the issue.

JPKC-009 J30–J34 proved exact source triple capacities and showed W32 S68/S72 have substantial cross-anchor raw source demand and a few Hall cross pairs, but zero selected D6. Therefore an overlap→D6 inference is false. The next falsifiable question is whether **other actually accepted** B-left/A-right and A-left/B-right original Q compensate on the very same labeling. They must not be inferred from Hall alone.

## 2. J35 — exact mixed witness ledger, all h (conditional counting identity)

Fix one genuine W(3,s), one pair of globally injective complete original factor labels f,g and a collection of **actual coordinate-proper, endpoint-bad physical P3 seeds** t. Each carries three distinct original incidence IDs T(t) and its original GQ anchor (q,r). Define W_j as the number of *distinct ordered witnesses* (oriented physical path t, ORIGINAL six-incidence Q) for which T(t) is a subset of Q and Q satisfies accepted class j, for j in `D6, B-left/A-right, A-left/B-right`.

For each physical seed:
1. Independently enumerate exact original A/A demand pairs (P,L). On genuine original GQ incidence graph, J25–J26 yield at most one matched source incidence triple U. Only `general_seven_original(T union U) == D6` counts; raw/Hall-only demands do not.
2. Independently enumerate the actual source wedge (B/A or A/B) completions using JPKC-006. Both routes operate on **the same** globally held f,g and exact original incidence ID and GF(5) positional classification.
3. Demand D6 Q *sets*, not just counts, must agree with independently enumerated JPKC-006 D6 Q sets for every seed. No selected Q is counted twice under opposite class labels.

The two wedge complements must have genuine original `point_wedge_plus_edge` or `line_wedge_plus_edge` topology; positive D6 complement has matching `3K2` topology. J15/J17/J20 forbid C and B/B as completions of these endpoint-bad seeds; this does **not** mean full S has no C or B/B classes.

This is an exact decomposition for the declared real-seed collection, not an existence theorem ensuring any W_j>0.

## 3. J36 — certified class-sensitive all-h lower floor, *conditional on witness counts*

For fixed maps let S_j be the number of globally distinct positive ORIGINAL Q in class j, including Q that may have zero observed endpoint-bad witness. By J19, each such Q supports at most 12 oriented proper seeds for D6 and at most 8 for each B/A wedge class. Therefore

```text
W_D6 <= 12*S_D6
W_B-left/A-right <= 8*S_B-left/A-right
W_A-left/B-right <= 8*S_A-left/B-right

S_total >= ceil(W_D6/12) + ceil(W_B-left/A-right/8)
         + ceil(W_A-left/B-right/8).
```

These are genuine ORIGINAL incidence Q, class-disjoint, and no familywise independence is used. The bound follows from already-proved J19; claiming an asymptotically positive floor **requires** a separate lower bound on W, which remains OPEN.

An **incidence-overlap graph of *distinct positive original Q*** is also counted. An edge is counted exactly once if its Q share at least one original incidence ID and their observed original-seed anchor sets admit distinct anchors. Inverted original-incidence indexing and de-duplication prevent counting shared 2–3 IDs as multiple Q-pairs. This positive-source Q graph is distinct from JPKC-009's Hall-demand source-triple graph; the two are not conflated.

## 4. J37 — exact coherent finite-fiber minimax, all h as a conditional statement

Fix original f and all right labels outside a source block B. Let F be the **complete finite set** of globally injective completions (for general s with unoccupied physical pairs, use the falling factorial count from D6-AA4-B, not 4!). The same chosen right label of every original line is used for every original Q, seed, Hall matching and GF(5) position.

For each x in F, define L(x) by J36 and the exact full-original seven-S(x). Since `S(x)>=L(x)` pointwise, also

```text
min_{x in F} S(x) >= min_{x in F} L(x).
```

This is conditional, and vacuous if the right-hand side is zero. In W32, K=V=15 and every physical K6 pair is occupied, so for pinned four-line B the complete fiber is precisely 4!=24 reassignments. JPKC-010 reproduces this fiber independently of the D6-AA4-B code; baseline S68/S72 and all maps are validated against full independent original `seven_census`, not by treating independently chosen per-Q labels as globally realizable.

**Inference firewall:** exact all-24 state computations are a **finite** coherent-fiber result. Any test of 1–23 states is explicitly marked incomplete. No zero-S exclusion outside the investigated fiber, no all-h global S lower bound, no full W34 census or R3/ASET exponent.

## 5. Acceptance, implementation, and remaining research blocker

The dedicated Python program outputs exact W32 lex/reverse/S68/S72 class-conditioned positive witness and Hall ledgers, original cross-anchor positive Q overlap by GF5 class, full W32 independent exact seven-set crosscheck, and genuine W34 lex/random/true symplectic-spread **distributed selected seeds only**. The dedicated tests include invalid injection and budget-negative cases. The GitHub-hosted fiber matrix separately evaluates ALL 24 right-factor states in S68 and S72 (each state uses one globally consistent actual model).

**Research blocker:** no inequality currently transfers `Cross(H)>0` or `Cross(D)>0` to `W_D6+W_BA+W_AB >= c*s^6`. Nor do the original-factor finite fiber gaps from D6-AA4-D imply this uniform bound. Finite family-class distribution may demonstrate that three-class seed-local transfer remains too weak and requires the B/B/C families or a genuinely new cross-seed/global occupancy inequality.

Status must remain `RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER` until independent proof review plus focused GitHub-hosted, INDEX, Proof Audit and full Research SUCCESS on the *exact final PR HEAD*. Do not modify `main`, #176 or #169.

## 6. Actual GitHub-hosted exact results on JPKC-010 initial implementation (14 Oct)

Independent original-W32/targeted-W34 **specialized oracle succeeded** after a regression-test message-pattern correction; the full two-matrix 24-state experiment was already successful before that correction. Recheck *final* commit CI again after updating these exact pins.

| Genuine scheme | Real endpoint-bad P3 examined | Positive seeds with wedge and no D6 | Positive seeds with D6 and wedge | DISTINCT reached original Q | J36 integer floor |
|---|---:|---:|---:|---:|---:|
| W32 lex | 786 (complete) | 94 | 24 | 68 | 26 |
| W32 reverse | 676 (complete) | 62 | 2 | 31 | 11 |
| W32 S68 | 544 (complete) | 8 | 0 | **4** | **2** |
| W32 S72 | 600 (complete) | 10 | 0 | **5** | **2** |
| W34 lex | 4 (selected only) | 2 | 2 | 17 | 3 |
| W34 random | 4 (selected only) | 3 | 1 | 29 | 5 |
| W34 original D4 symplectic spread | 4 (selected only) | 1 | 2 | 20 | 4 |

The seed-positive categories above classify **seeds**, whereas the reached-Q column deduplicates ORIGINAL six-incidence sets. Baseline complete seven-S is **68 for S68** and **72 for S72**: only 4/68 or 5/72 positive Q are seen through this particular endpoint-bad seed ledger. It is incorrect to identify all unobserved Q as B/B or C: even a three-class Q might simply have no eligible endpoint-bad P3 witness.

The **complete** coherent fiber matrix for both pinned four-original-line blocks, run independently on GitHub-hosted workers:

| Actual full fiber | All legal global completions | min complete seven-S | min seed-reached DISTINCT original Q | min J36 class-sensitive floor |
|---|---:|---:|---:|---:|
| S68 | 24 | 68 | 4 | 2 |
| S72 | 24 | 68 | 3 | 2 |

Both fibers have legal states with D6=0 and other legal states with D6>0. Therefore "no D6 on the starting S68/S72 map" is not a fiber-invariant, and the all-h argument cannot freeze the D6-zero property under coherent source-factor edits.

**Scientific interpretation:** W32 supplies a *real finite wedge rescue* (8/10 wedge-only positive seeds) but **disproves sufficiency of the proposed mixed charge to obtain the observed magnitude of S without an additional lower bound on original-positive witness multiplicity**: the sharp J19-derived integer certificate detects only 2 when full S is 68. No asymptotic no-go follows from these finite counts. An all-h transfer must additionally control seedless accepted sixsets or introduce a stronger global physical-occupancy/original-source coupling beyond Hall/J19.

