# HYP-105 / #230 — D6-AA4-AJ: two connected-C6 2+2 bridges, exact original six-channel Hall transfer

**Status:** RESEARCH DRAFT / scoped partial theorem. **Root #230: OPEN_WITH_FORMAL_BLOCKER.** This document is source mathematics, not an independently accepted A/B/C proof. Parent: [AA4-AI triple sector / PR #519](https://github.com/definitely-stable/Mathlab/pull/519), exact initial parent HEAD `fc82262efb3dc4da306bed482b71d93540f2bdb1`. Parallel quantitative precursor: [AA4-AI GQ sharp pencil / PR #518](https://github.com/definitely-stable/Mathlab/pull/518). Algebraic rank-six precursor: [AA4-AH / PR #517](https://github.com/definitely-stable/Mathlab/pull/517). Do not mistake another PR's green tests for scientific acceptance here.

## 1. Problem and exact quantifiers

For **every** integer `h>=1`, put `s=2^h`, `V=(s+1)(s^2+1)`, `a=min{n:binom(n,2)>=V}`. Use the genuine indexed source point/line incidence graph of the symplectic generalized quadrangle `W(3,s)`, degree `s+1`, girth eight. Assign all `V` original point factors and all `V` original line factors by two complete, separately globally injective physical unordered-coordinate-pair maps `f,g` into `E(K_a)`. These are *one pair of maps for the entire census*; they may be arbitrarily correlated. `m=binom(a,2)-V` physical pairs are unused on either typed side, independently.

Fix the B-side orientation (point B / line A, or its typed dual). Fix an **actual original** source root `p`, two distinct **actual original flags** `(p,l0),(p,l1)`, and four **other distinct original** B-side source factors `q0,...,q3` whose physical images form an occupied complementary physical C4. Fix the two **actual opposite physical pinned pair labels** `e0=g(l0),e1=g(l1)` (for dual swap `f/g`). Assume `e0={u,v}` and `e1={w,x}` are disjoint. If they touch, the *two-disjoint-pins 2+2 subfamily* defined below is empty; other A sectors are **not** empty in general.

We count **distinct six ORIGINAL incidence-ID sets**, not signed events, automorphism orbits, generic 4x4 binary matrices, or six independently sampled edge labels. Positive GF(5) classification is the previously frozen six-coordinate B/A or A/B class with the opposite physical edges forming a *connected simple* C6.

## 2. New exact connected 2+2 sector theorem (AJ-1)

Among opposite physical connected C6 carrying `e0,e1`, restrict to those where removal of `e0,e1` leaves two length-two paths. There are exactly **two disjoint** configurations, indexed `b=0,1`:

- `b=0`: bridges `v -- y -- w` and `x -- z -- u`;
- `b=1`: bridges `v -- y -- x` and `w -- z -- u`.

Each `y,z` belongs to the `a-4` physical coordinates outside `{u,v,w,x}`, and **`y != z`**. The four unpinned physical edges must all lie in the one *actual occupied* globally injected opposite typed image. In each configuration let `Y_b` be all valid left bridge sites `y`, `Z_b` all valid right bridge sites `z`. Under the physical-image inverse map, each site induces an **ordered pair of distinct actual opposite original source factors** (the two physical edges of that bridge).

Let `N(q)` be the *actual original* source incidence neighborhood, and let `S` range over the six 2-subsets of `{0,1,2,3}`. Define `Y_{b,S}` as those `y in Y_b` for which the 2x2 original source incidence submatrix on rows `q_i, i in S` and the two original line factors of the left bridge has a perfect matching; analogously `Z_{b,S^c}` on the other two rows and the right bridge. True original GQ girth eight excludes a source 4-cycle, so **each** 2x2 permanent is zero or one.

Then the EXACT accepted original six-incidence-ID count in this restricted connected sector is

```text
T_22(p,{flags},q0..q3; f,g)
  = sum_{b=0}^1 sum_{S in binom([4],2)}
      [ |Y_{b,S}| * |Z_{b,S^c}| - |Y_{b,S} intersect Z_{b,S^c}| ].
```

**Proof.** Removing two disjoint pinned edges from a simple C6 with 2+2 complement produces a unique pairing of their endpoints into two cross-pinned paths (the two `b` cases). For a fixed `b` and fixed `y!=z` the four unpinned physical pair labels are all distinct and different from the pins; global opposite-map injection therefore yields four different *actual original* opposite factors. The four original singleton rows are different from the source root and from one another. An actual six-ID original forest on these fixed factors corresponds bijectively to one permutation matching all four singleton rows to these four opposite factors. Laplace-expand this 4x4 permanent by the two left-bridge columns: the matching assigns exactly one 2-subset `S` to the left, the complementary rows to the right. The two local source-GQ 2x2 permanents are 0 or 1, so their product indicates membership of `y` and `z` in the corresponding site sets. Summing `y,z` over **distinct** sites gives the product of cardinalities minus the intersection (the diagonal). Each C6 has a unique bridge type `b`, so there is no between-bridge double count. This argument is point/line dual, works for `h=1` and all larger `h`, and nowhere separates or averages the globally coherent f,g. QED.

All twelve displayed channel terms are nonnegative. The underlying abstract two-bridge 4x4 permanent kernel has the **existing** rank-six decomposition of PR #517 separately for each bridge; **do not claim a new rank-12 lower rank theorem** for their sum. Exact positivity iff at least one channel has *one off-diagonal* compatible `(y,z)`.

## 3. Sharp raw physical sector and quantitative PRE-HALL theorem (AJ-2)

For a COMPLETE physical `K_a` palette and fixed disjoint pins, each bridge type has `(a-4)(a-5)` cycles. Thus

```text
raw connected C6, all types        = 6(a-4)(a-5)   (prior AA4-AI)
raw connected C6, the two 2+2 types = 2(a-4)(a-5)   (new sector)
exact share                         = 1/3.
```

The **remaining 2/3** are length-1+3 configurations (an unpinned direct edge between pinned endpoints plus a complementary three-edge path). They are EXCLUDED from AJ-1, although still counted by the older exact full-C6 permanent oracle. Adjacent pinned edges and both triangle sectors are also excluded.

For arbitrary globally injected `f,g`, combine the original GQ pencil safety lower certificate proved in the **parallel** PR #518 with the actual two bridge pairings. Define `d=s+1`, `K=binom(a,2)`, `m=K-V`, `H=floor(32m/a)` and

```text
N_safe = [V*binom(d,2) - a*binom(a-1,2) - H*(a-1)*d*(d-1)]_+.
C4_min = [3*binom(a-2,4) - m*(a-4)*(a-5)]_+.
P22_min = 2*N_safe*C4_min*ceil(a^2/4).
```

For any true ORIGINAL root-pair certified safe by that GQ argument, **all four endpoints of the two pinned opposite physical edges have missing-edge degree less than `a/16`**. Each of the four endpoint-cross site sets used across our two bridge schemes therefore has size at least `7a/8-4`. For each scheme,

```text
|Y||Z| - |Y intersect Z|
 >= (7a/8-4)^2 - a
 >= a^2/4    for a>=32.
```

The last inequality is elementary: its residual polynomial is `33a^2/64-8a+16>0` for `a>=32`. Each occupied original root C4 can therefore be paired with **at least** `2 ceil(a^2/4)` occupied physical 2+2 bridges. These indexed candidates are disjoint across original root/pinned-flag/C4 cohorts. Thus

```text
forall h>=4, s=2^h, forall complete globally injected actual f,g:
      P22(f,g) >= P22_min >= s^14/128.
```

The second inequality inherits the checked analytic and exact small-order bounds from sibling PR #518; `certified_two_bridge_prehall_floor` independently re-evaluates its *integer inputs* for all h=1..39. This is a **deterministic lower bound on occupied physical candidates BEFORE source Hall matching**. It is NOT `T_22>=s^14/128`: `T_22` may be much smaller and can locally be zero. It also relies on a parallel scientific Draft proof until that ancestor is accepted; its mathematics must not be promoted solely by our test passing.

## 4. Exact remaining density obstruction (AJ-3)

For the globally indexed pre-Hall physical `P22(f,g)` tuples, partition by the permanent of the **actual source** 4x4 incidence matrix: `H0,H1,H2`. True original GQ girth eight implies no permanent beyond two (AA4-AE). Therefore

```text
P22 = H0+H1+H2,
T22 = H1+2*H2,
H1+H2 <= T22 <= 2*(H1+H2),
0 <= T22 <= (B/A+A/B accepted) <= S_seven.
```

Define the Hall-positive fraction `rho22=(H1+H2)/P22` whenever `P22>0`. The new pre-Hall lower gives, for `s>=16`, the **conditional implication**

```text
[forall f,g: rho22(f,g) >= c*s^(-8)]  =>  [forall f,g: S_s(f,g) >= c*s^6/128].
```

Conversely an adversarial infinite global family `S_s=o(s^6)` necessarily satisfies `rho22=o(s^(-8))` (for `s>=16`). The antecedent is the **UNPROVED** global Hall-density bound, and it is **sufficient, not equivalent** to Branch A: other five accepted GF(5) classes and the 1+3/same/split sectors may compensate even if `rho22=0`. No Branch A, Branch B, or model-equivalent Branch C is asserted.

## 5. Independent finite falsifiers and acceptance protocol

Versioned code: `research/hyp105_issue230_d6aa4aj_connected_22_hall.py`. Independent tests: `research/test_hyp105_issue230_d6aa4aj_connected_22_hall.py`.

- **Oracle 1 — six-channel physical site contraction:** use true source-GQ `N(q)`, actual global typed inverse map, both bridge endpoint pairings and off-diagonal `y!=z`. Count all twelve nonnegative channels.
- **Oracle 2 — unrelated enumeration order:** enumerate every pinned full physical 2factor, retain connected C6 with four nonpin edges each joining one pinned endpoint to one of exactly two outside sites, then count each REAL original 4x4 perfect matching by all 24 permutations. This oracle does **not** use `Y_S,Z_S`, rank-six decomposition or construction of bridge patterns.
- **Finite tests:** complete K6/K7/K8 physical ratio 1/3; missing physical labels with explicit common-neighbor diagonal subtraction; genuine symplectic W(3,2) exhaustive all 135 original root-C4 cohorts in **both** orientations on a single complete globally injected correlated witness from #519; original W32 S68/S72/lex; true original W(3,4) with physical K14 non-surjectivity; common original symplectic transvection and independent typed physical permutations; exact integer h=1..39; reject malformed input domains.
- **Cross-check:** for the explicit #519 true W32 witness, restricted `T22` cannot exceed the prior **full** connected-C6 original accepted counts 40 B/A and 58 A/B; the full seven-class accepted original census on that map remains **123**, not zero. No finite sample is used to infer all-h Hall positivity.

Reproduce via `PYTHONPATH=research python -m unittest -v research/test_hyp105_issue230_d6aa4aj_connected_22_hall.py` or dedicated hosted workflow. Record exact PR-head GitHub-hosted checks **after they finish**, never before; record independent mathematical review distinctly from CI. Do not close #230.

## 6. Next missing lemma and integration

The decisive unresolved statement is an **all-map true-original connected-2+2 Hall-positive density** `rho22(f,g)>=c*s^-8` for all sufficiently large `s=2^h`, *or a rigorously quantified counterfamily to that restricted claim*. An additional alternative is direct global S control via the other two-thirds of connected C6 and the six other GF(5) modes. The new finite evidence should be examined for which route is credible; **no expectation-to-minimum inference** is allowed.

Keep this scientific slice Draft child of #519, itself child of #517. **PR #518 is a parallel sibling**, not accidentally included in this branch. If integrated, first independently referee and integrate prerequisites in ancestry order, reconcile #518 via deliberate separate merge/cherry-pick/rebase without discarding history, and only then consider AJ-2's inherited inequality as accepted. Do not edit generated `registry/*.md` by hand or mark a Draft theorem as reviewed in RCP.
