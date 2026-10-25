# HYP-105 / issue #230 — D6-N: exact original-line correlation and second moment

**2026-10-13 — RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.** Stacked exclusively on [D6-M Draft #412](https://github.com/definitely-stable/Mathlab/pull/412), HEAD `4454b4fcff63710ed6f82ee63e154ddb7273c46d`. No `main` changes or PR merges. Root #230, #176 and #169 remain open.

## Question and the missing deterministic object

D6-M proved a sharp exact first moment of the directional genuine ORIGINAL GQ C-left/A-right class for **every fixed globally injective left map** and **uniformly sampled globally injective right map**. Genuine W(3,2) lex/reverse have identical left map and mean 38/13, but actual right-g values 4/0. This falsifies the leap from a positive random-right mean to a positive fixed-right count. Another maximum-flow or first-moment argument cannot repair that gap.

For W(3,s), `s=2^h`, fix injective f on ORIGINAL points and complete injective g on ORIGINAL lines, each into distinct unordered coordinate-pair labels of `K_a`, `a=min{a: binom(a,2)>=V}`, `V=(s+1)(s^2+1)`. Let `X_f` be the ORIGINAL unordered six-incidence sets whose left physical projection is C and whose six ORIGINAL right factors are distinct. Write `L(x)` for its six ORIGINAL right line identities, and define integer weights

    w_f(L) = #{x in X_f : L(x)=L},  W_f=sum_L w_f(L).

Only nonzero supports matter. The weight must retain all different ORIGINAL sixsets; do not pass to orbits of physical relabelings or signed GF5 event counts.

For a complete right map g let `A_g(L)=1` exactly when the six *different* physical g-images of the six original lines in L form a simple 2-regular graph on exactly six physical coordinates (A); otherwise zero. A **deterministic identity for every fixed correlated pair** follows:

    U_C-left/A-right(f,g) = sum_L w_f(L) A_g(L).
    D_f(g) = U_C-left/A-right(f,g) - p_A W_f
           = sum_L w_f(L) (A_g(L)-p_A).

This is the missing weighted support-mask correlation. It is *not* a nontrivial uniform lower bound: for a given f the signed discrepancy can be `-p_A W_f` when the genuine support avoids every selected A_g(L). The all-g task is to prohibit that kind of suppression at scale `s^6` for the **union of all seven accepted positive families**, not merely this directional C/A subclass.

## All-finite-h exact right-injection second-moment theorem

Write `K=binom(a,2)`, and `F_a` for all simple 2-factors of six physical coordinates (exactly `70 binom(a,6)` physical edge subsets). Each such set contains exactly six distinct physical pair labels. For integer `t,k in [0,6]` define **finite universal constants** `T_{t,k}` as the number of ordered pairs of such 2-factors `(F,H)` on two **fixed** six-vertex coordinate sets having exactly `t` shared physical coordinates and exactly `k` shared physical **edges**. If `k>t`, the constant is zero. The `T_{t,k}` do not depend on a, f, g or s, and are computed by 7 enumerations of `70^2` physical pairs (not a large W(3,s) census). In particular `sum_k T_{t,k}=4900`, `T_{0,0}=4900`, `T_{6,6}=70`.

The number of ordered pairs of physical A-factors sharing k physical edges is the exact polynomial

    P_k(a) = binom(a,6) *
             sum_{t=0}^6 binom(6,t) binom(a-6,6-t) T_{t,k},

with `binom(n,r)=0` for invalid parameters, including `n<r`. For ANY two fixed distinct or identical unordered six-sets L,M of ORIGINAL right line identities whose intersection has size k, a uniformly random **complete injection** g satisfies

    q_k(a) := Pr_g[A_g(L)=1 and A_g(M)=1]
            = k! (6-k)!^2 P_k(a) / (K)_{12-k},

where `(K)_j = K!/(K-j)!`. This formula also works for k=6. Its diagonal is the D6-M probability:

    q_6(a)=p_A = 6! * 70*binom(a,6) / (K)_6.

**Proof:** choose an ordered pair of physical A-factors on two six-coordinate sets with precisely k shared physical edges. Exactly k shared original line identities must map bijectively to those k shared physical pair labels (`k!` ways), and the unshared identities on each side biject to its other six physical pair labels (`(6-k)!^2` ways). Conversely, any two accepted physical A images of two original right six-sets sharing k identities necessarily share exactly k physical edge labels because the global right g is injective. The restriction of a uniformly random complete injection to the `12-k` distinct original identities is uniform among `(K)_{12-k}` ordered injective placements. No unjustified independence is used. Summing over fixed physical vertex-set overlaps t proves the stated polynomial exactly.

Let the **ordered original support-overlap spectrum** be

    N_k(f)=sum_{L,M:|L intersect M|=k} w_f(L)w_f(M).

Thus `sum_k N_k=W_f^2` and `N_6=sum_L w_f(L)^2`. For EVERY valid original W(3,s) left f, and uniformly random complete right g,

    E_g U_C/A       = p_A W_f,
    E_g U_C/A^2     = sum_{k=0}^6 N_k(f) q_k(a),
    Var_g U_C/A     = sum_k N_k(f) q_k(a) - (p_A W_f)^2.

The second-moment theorem is exact for all finite h and for ANY fixed left f. It depends only on a and the TRUE ORIGINAL GQ six-line support multiplicities. Unlike replacing `q_k` with `p_A^2`, it correctly handles the negative or positive effects of global sampling without replacement. By Paley–Zygmund, **random-right only**,

    Pr_g(U_C/A>0 | f) >= (E_g U_C/A)^2 / (E_g U_C/A^2).

This probability lower bound establishes neither a deterministic minimum over all g nor a nonzero exponent for the full seven-family risk.

## Independent W(3,2) falsifiers

The `research` implementation reconstructs the ORIGINAL left-C sixsets using existing frozen-GQ incidence IDs, groups by six distinct ORIGINAL right-line identities, computes `N_k(f)` by integer bitmask intersections and tests fixed physical right-A membership. An **independent** test reconstructs the same weights with a different method: enumerate original point triples of pairwise-disjoint left physical edges and choose two genuine incident GQ lines at each point; reject repeated original right lines. It evaluates `N_k` again using set intersections (not bitmasks).

A second independent verifier directly enumerates all physical six-edge subsets of K6 and K7, retains precisely those that are 2-regular on six vertices, and compares ordered pair counts by shared physical edges with the universal `P_k(a)` formula. This is a genuine independent check of the 70-by-70 overlap kernel.

Pinned finite facts inherited from D6-M and independently rechecked:

| Genuine GQ + labeling | `W_f` | `E_g U_C/A` | Actual fixed `U_C/A` | Available physical right A-factors |
| --- | ---: | ---: | ---: | ---: |
| W(3,2) lex | 209 | 38/13 | 4 | 70 |
| W(3,2) reverse | 209 | 38/13 | **0** | 70 |
| W(3,2) S68 | 297 | 54/13 | **0** | 70 |
| W(3,2) S72 | 297 | 54/13 | 2 | 70 |

**Important distinction:** All four complete right maps use **all 15 pair labels of K6**, so ALL have exactly 70 physical right A-factors available. In reverse and S68 none intersects the weighted ORIGINAL C-support. Absence of a positive C-left/A-right event is therefore a **deterministic mismatch of genuine GQ six-line incidence support and the physical A-mask**, not a shortage of physical A-targets. This refutes any purported deterministic transfer using only separate counts of left C-mass and right A-mass. It does NOT refute Branch A, since other six positive classes may remain (and do remain in the known W32 examples).

## Boundaries, acceptance and next step

1. Exact formulas: ALL-h finite for each fixed f and uniform right injection g; fixed-g discrepancy is an **identity** only, not a universal lower bound. The currently executable complete sixset moment spectrum is capped at W(3,2). Genuine W(3,4)/W(3,8) full seven-positive S is not claimed.
2. All seven accepted GF(5)-positive classes are still required for Branch A. Do not add B/A and C/A covariance assuming independent events: both use the same g, so a future joint analysis requires their **cross-overlap spectrum** and correct physical pair-of-class kernels.
3. To obtain a real all-g theorem, establish a quantitative anti-correlation obstruction for **combined positive classes**, e.g. a uniform lower bound for a suitable weighted sum of original-support/physical-mask intersections, or exhibit an explicit coherent infinite adversarial family. Finite zero directional C/A values do not constitute Branch B.
4. CI is a code-contract check, not independent human proof review. Keep draft status and `#230/#176/#169` open. Do not merge until hosted dedicated, INDEX, Proof Audit and full Research checks are green at one exact HEAD and independent mathematical review is completed.

[Algorithm](../../research/hyp105_issue230_d6n_exact_correlated_ca_overlap.py) · [Independent falsifiers](../../research/test_hyp105_issue230_d6n_exact_correlated_ca_overlap.py) · [Dedicated GitHub-hosted contract](../../.github/workflows/hyp105-issue230-d6n-exact-correlated-ca-overlap.yml).
