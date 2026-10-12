# HYP-105 E1-K3-G2-C — all-h GQ projection-fiber geometry and seven-bin cross-origin certificate

Date: 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked child of [Draft PR #375](https://github.com/definitely-stable/Mathlab/pull/375), pinned HEAD `ee20998932ed4e8cfd07206b97c2899289ac3575`. No `main` changes, no merge.

**Status: RESTRICTED_THEOREM_C**: a new exact incidence-theoretic refinement of the off-diagonal K3-G2-B source-pair kernel. This is **not** an all-h bound `J_cross=o(s^6)`, not a proper-D6/seven-family S lower bound, and not an R3/ASET exponent.

## 1. Unique anchor projection: an all-h GQ(s,s) theorem

Let `s=2^h`, `V=(s+1)(s²+1)`, and let `ell` be any ORIGINAL source line. The generalized quadrangle axiom asserts that for every point q not on ell, there exists exactly one point t on ell collinear with q. Write `pi_ell(q)=t` and extend by `pi_ell(t)=t` for t on ell. The fibers indexed by the s+1 points t on ell are pairwise disjoint, cover all V original points, and have **exactly s²+1 points** each: t itself plus s other original lines through t, each containing s off-line points.

The point-line dual holds: fix an ORIGINAL point p, and each line q not through p has exactly one line through p meeting q. No symmetry assumption for arbitrary physical f,g is needed.

Distinct original points q,r in relation to anchor ell admit the following SEVEN mutually exclusive original geometry classes. Every formula is a count of **unordered original source pairs for one anchor**, independent of f,g:

| Class | Original geometry | Number per anchor |
|---|---|---|
| both_on_anchor | q,r both on ell | `(s+1)s/2` |
| one_on_projected | one on ell; the other projects onto it | `(s+1)s²` |
| one_on_other | one on ell; off-line origin has another foot | `(s+1)s³` |
| off_samefoot_collinear | q,r off ell, same foot, on one other line through that foot | `(s+1)s²(s-1)/2` |
| off_samefoot_noncollinear | q,r off ell, same foot, not collinear | `(s+1)s²(s²-s)/2` |
| off_differentfoot_collinear | q,r off ell, distinct feet, on a unique line disjoint from ell | `(s+1)s⁴/2` |
| off_differentfoot_noncollinear | q,r off ell, distinct feet, noncollinear | `(s+1)(s-1)s⁴/2` |

Their sum is `binom(V,2)` exactly.

### Why the collinearity counts are exact

For off-line q with foot t, the unique original line q-t contains s-1 other off-line points of the SAME foot. No second line through q can contain another point r with the same foot t, or the GQ incidence graph would contain a forbidden 6-cycle. Hence exactly s-1 same-foot collinear partners per off-line q.

The other s lines through q each contain s off-line points with DIFFERENT feet, so q has exactly s² different-foot collinear partners. Equivalently, the original lines disjoint from ell number exactly s³; each has s+1 points, whose projections onto ell are all different. Therefore the off-differentfoot-collinear count is `s³*binom(s+1,2)=(s+1)s⁴/2`. The dual argument applies to source lines and an anchor source point.

This proof uses ORIGINAL incidence, not a simulated graph with independent labels.

## 2. Exact refinement of critical K3-G2-B J_cross

For each anchor ell, retain K3-G2-B `T^g[q,ell]` closure counts and physical bridge kernel `K^f_ell(q,r)` from the ONE global original pair map. For each class C above define the integer weighted mass:

```
J_C^h = sum_ell sum_{q<r : class_ell(q,r)=C}
            T^g[q,ell] * T^g[r,ell] * K^f_ell(q,r).
```

The point-line dual defines J_C^v. Exactly `J_cross=sum_C(J_C^h+J_C^v)`; every term is nonnegative. The seven bins refine the previous four classes by splitting one-on-anchor according to the off-origin projection and both-off according to same or different projections. An independent GQ source-path oracle checks the classification and two completely separate endpoint-bridge calculations reconcile every weighted bin.

No single bin is claimed subcritical merely because its total possible ORIGINAL source-pair population is small: physical closure products can concentrate adversarially.

## 3. Exact projection-fiber second-moment decomposition

For a fixed anchor ell let `t_q=T^g[q,ell]`, and let

```
A_v = sum_{q:pi_ell(q)=v} t_q,
U   = sum_q t_q.
```

Then (before bridge-kernel weights) the ORIGINAL source-pair products satisfy:

```
SameFoot(ell) = (sum_v A_v² - sum_q t_q²)/2,
DifferentFoot(ell) = (U² - sum_v A_v²)/2.
SameFoot(ell)+DifferentFoot(ell)
               = (U² - sum_q t_q²)/2.
```

The new implementation verifies these integer identities independently for both point/line dual tensors, while retaining all seven exact weighted bins. Thus K3-G2-C identifies which source projection fibers actually contribute to cross-source collisions. Any subsequent bound must preserve the bridge kernel K and the original coherence of f,g.

## 4. Independent falsifiers and fixed complexity budgets

Reference `research/hyp105_g5e2b3e1k3g2c_projection_fibers.py`; independently constructed oracle `research/test_hyp105_g5e2b3e1k3g2c_projection_fibers.py`.

Independent tests follow original incidence paths to find projections instead of using the reference's shared-line intersection operation, enumerate all ORIGINAL source-pair classes W(3,2)/W(3,4) and verify their exact all-h formulas, reconstruct T from physically closed third-coordinate wedges, independently scan anchor-incidence physical edge labels to compute K, and compare every seven-bin weighted integer with the reference and K3-G2-B total. Budget overflow fails closed. No untrusted asymptotic regression or finite-s fit is promoted to a theorem.

Dedicated path-limited GitHub-hosted Contract, inherited INDEX/full Research; keep the PR Draft pending exact-head SUCCESS and independent proof review.

## 5. Next mathematically decisive step — K3-G2-D

Investigate a **projection-resolved charging inequality** from heavy `J_C` classes to positive proper D6 or one of the six other accepted S families, with ORIGINAL six distinct incidence columns, fixed GF5 palette, and bounded witness multiplicity. In parallel test a coupled full-R3 inequality `(L(P3)-Theta)/12-J_cross >= c*s^6`. The exact seven-bin ledger permits separate finite falsifiers for these routes. A universal statement must quantify all `s=2^h` and all globally coherent f,g; an exact finite census is not a proof.

Prior full-R3 and original seven-family S goals are separate. Neither issue #230 Branch A nor Branch B is settled; no ASET exponent is claimed.
