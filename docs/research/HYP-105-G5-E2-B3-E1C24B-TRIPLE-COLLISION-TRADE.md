# HYP-105 B3.2-E1-C24-B1 — exact third-order right-C collision formula and pair-tensor limitation

Date: 2026-10-11. Parent [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked on C24-A1 [PR #340](https://github.com/definitely-stable/Mathlab/pull/340), then C23 #334; **main is not modified**.

## 1. Exact ALL-h three-conflict identity

Retain every original W(3,s) original-incidence qualification and the ONE complete globally coherent f,g of C24-A1. For each unordered set t={i,j,k} of three distinct ORIGINAL right lines let omega_f(t) count distinct six-incidence left physical 2-factors with two original incidence IDs per right line. Let H_C=sum_t omega_f(t) and W_f(i,j)=sum_(t contains i,j) omega_f(t).

Write c_ij(g)=1 if the distinct physical pair labels g(i),g(j) share a physical coordinate, otherwise 0. For t let chi_t=c_ij+c_ik+c_jk in {0,1,2,3}. An original right-C source is accepted on the physical right precisely when chi_t=0. Counting every physical pair collision first, and restoring duplicate failed counts, gives for ALL h, f, g, and every legal occupied F_R:

    S_(R=C)(f,g)
      = H_C(f) - sum_(i<j) W_f(i,j)*c_ij(g)
        + sum_(i<j<k) omega_f(i,j,k)*max(chi_ijk(g)-1,0).

Equivalent exact inclusion-exclusion:

    correction = sum_t omega(t) [
        c_ij*c_ik + c_ij*c_jk + c_ik*c_jk - c_ij*c_ik*c_jk
    ].

When chi=2 the correction is one per original source; when chi=3 it is two. This **explains precisely** the nonnegative slack in the C24-A1 union/star bound. It is a finite combinatorial identity applying to arbitrary all-h legal original GQ f,g, NOT a new universal Omega(s^6) lower bound. Full independent tests check that the first-order sum equals C24-A1's physical-star collision count for 105 actual coherent right swaps.

## 2. Genuine original W(3,2) correlated left and right adversarial maps

Build the 15-point/15-line/45-incidence GF(2)^4 symplectic W(3,2) from independent A1 source. Original point p=1..15 maps to lex physical K6 edge at index f[p-1]:

    f=(13,4,2,14,0,11,1,7,10,6,9,5,12,3,8).

Original right line i in the fixed sorted isotropic-line order maps to lex K6 edge at index g[i]:

    g=(12,10,5,2,8,14,1,7,0,6,3,13,9,4,11).

Both maps are each one COMPLETE bijection, shared across ALL original incidences. Independent right-first and physical-left-first generators enumerate the whole 62,370 distinct original left physical 2factor sixset universe. They agree on EXACT H_C(f)=45 (versus 92 for A1 lex-f), 40 distinct original right-line triples, sum_(i<j)W_f(i,j)=135 and max W_f(i,j)=5. The same complete f,g yields S_(R=C)=0. The new H45 is a **witness upper on the minimum of H_C for s=2**, not an exhaustive minimum over all 15! left maps or an asymptotic counterexample.

## 3. Rigorous barrier: pair weights W do not determine full three-way correction

Consider two distinct abstract three-uniform source hypergraphs on six named right labels:

    A={012,034,135,245}
    B={013,024,125,345}.

Every unordered right-label pair occurs equally often in A and B (a Pasch 2-design trade), so they have the exact SAME pair-weight W. Yet on the ONE common complete physical right injection of six named lines into K6 physical pair edges at indices (5,7,3,11,12,0) their valid disjoint right-C triple counts are DIFFERENT:

    S_C(A,g)=0,   S_C(B,g)=1.

Their first-order star-collision sums are equal; their three-way correction differs. Therefore **no formula depending solely on W and the fixed right map can reconstruct the exact S_C for arbitrary three-uniform source weights**. This is an abstract pair-statistic information-loss theorem, NOT a claim that both Pasch source families themselves are realizable as full original GQ sixsets. It does not alone rule out special all-GQ inequalities that use only W.

## 4. Scientific gate and CI

Files:
- research/hyp105_g5e2b3e1c24b_three_collision.py
- research/test_hyp105_g5e2b3e1c24b_three_collision.py
- .github/workflows/hyp105-c24b-contract.yml

Required independently checked components: full right-first/left-first original W32 count; globally valid H45 source and C0 right witness; full 105 coherent right-transposition identities; frozen old H92 lex source; exact Pasch two-trade pair matrix with different accepted counts; malformed labels fail-closed; exact PR-head hosted Contract, six-shard Research plus seventh aggregator, and INDEX. No changed main, no independent right map per sixset and no estimates from samples relabelled as all-h proof.

**Scientific outcome:** restricted all-h exact identity, finite genuine W32 joint f,g C-only zero, abstract pair-only statistics incompleteness. Root #230 remains **OPEN_WITH_FORMAL_BLOCKER**: no full-seven global minimum, full GF(5) R3 or ASET exponent. Next C24-B2 is quantitative all-f source lower and star-constrained hypergraph discrepancy, with explicit attempt to falsify proposed bounds; third-order tensor must be retained where required.
