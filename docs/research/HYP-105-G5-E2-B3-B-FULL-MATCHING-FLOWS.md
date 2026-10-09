# HYP-105 G5-E2-B3.1-B1 — complete GF(5) classification of six-FACTOR-MATCHING leafless cores

Date: 2026-10-10. Parent [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169), [#162](https://github.com/definitely-stable/Mathlab/issues/162). Extends [B3.1-A 6+6 restricted census](HYP-105-G5-E2-B3-B1-CRITICAL-FLOWS.md), [B3.0 all-forest necessary shapes](HYP-105-G5-E2-B3-FOREST-PROJECTION.md) and [B3.2-D Q4/R2 and sampled exact R3](HYP-105-G5-E2-B3-D-JOINT-RISK.md).

**COMPLETED_ALL_SIX_FACTOR_MATCHING_LEAFLESS_TEMPLATES / EXACT_GF5_51_PALETTE / COMPUTER_CHECKED_FINITE_ORBIT_CERTIFICATE / ALL-h_MATCHING_EXPECTATION_IDENTITY / NONMATCHING_FORESTS_OPEN / NO_ALL-h_FIXED_LABEL_R3_UPPER / NO_ASET_EXPONENT / NO_CLAIM_OF_GLOBAL_NOVELTY.**

## 1. Model and exhaustive universe

Let W(3,s) be the classical symplectic generalized quadrangle, s=2^h. Fix six **vertex-disjoint original factor incidences** (six different points, six different lines). The physical pair injection in each half sends each of these six factor endpoints to a DIFFERENT unordered edge of K_a. Thus the projection on each side is a **simple** graph with six **named** edges. A nonzero GF(5) signed collision requires no physical coordinate of degree one, because it has one nonzero coefficient with no other term available to cancel. Sum degrees=12, so the number v of touched physical vertices is at most six. A simple six-edge graph requires at least four vertices. Necessarily v∈{4,5,6}, and every touched vertex has degree≥2.

This is a complete *structural* reduction for six-factor-edge matchings, not for all six-factor-edge forests (whose vertices may coincide). Every simple six-edge graph on v=4,5,6 with minimum degree two is constructed explicitly by enumerating K_v edge subsets and assigning its six **distinct** edges to the six named columns. Quotient only permutations of physical coordinate symbols by sorting each coordinate's six-bit incidence mask; no coordinate equality or different original columns are identified.

Exact named-column projection counts, independently cross-checked against validation that every column occurs in exactly two distinct masks and every pair label is unique:

| Physical vertices in one half | v=4 | v=5 | v=6 | Total |
|---|---:|---:|---:|---:|
| Canonical column-named projected pair graphs | **30** | **510** | **70** | **610** |

At v=6 the sixty C6 and ten 2C3 projected dual graphs recover precisely B3.1-A. At v=5 the degree sequence is either (4,2,2,2,2) or (3,3,2,2,2); at v=4 all six graph edges form K4.

Fix the ordered signs (+++---) on named columns. The stabilizer of the unordered balanced sign partition is H=(S3×S3)⋊C2 of order 72 (it may swap the sign classes globally). It acts **simultaneously** on both colored physical projections. Left/right colors are NOT exchanged. Canonicalize left under H; then canonicalize right under the subgroup fixing that left. This yields exactly **20 left-profile orbits, 5,486 two-color signed orbits**, jointly representing

```text
10 * 610 * 610 = 3,721,000
```

named-column, unordered-sign signed cases. Each double-orbit receives exact mass 10 × size(left orbit) × size(right orbit under left stabilizer). This is an **exhaustive finite matching-template universe**, not a count of actual six-factor-matchings in W(3,s).

## 2. Exact GF5 flow count in either physical half

Given one projection profile A, for each physical coordinate c let S_c be the subset of column IDs using it (size d=2,3 or4). Assign a nonzero weight x_(c,i)∈{1,2,3,4} to every incidence i∈S_c, constrained by

```text
sum_{i in S_c} sign(i)*x_(c,i) = 0 mod 5.
```

The number of allowed coordinate assignments is the elementary character-sum identity (4^d+4(-1)^d)/5, giving **4,12,52** for d=2,3,4. This is rederived by completely independent brute product(1..4)^d tests.

Define H_A(z) for z∈GF5^6 as the integer count of assignments to all six physical pair edges/12 incidences of that half obeying every coordinate cancellation equation, for which each column i receives partial **unsigned** weight sum z_i∈GF5. Every allowed GF5 checksum4 column has two nonzero weights in left and two in right and **sum of its four weights=4 mod 5**, hence for a left profile A and right profile B, the entire complete **51-per-column** signed trade count is exactly

```text
F(A,B) = sum_{z in GF5^6} H_A(z)*H_B(4-z).
```

This is a precise bijection: the coordinate cancellation equations are imposed independently in the two disjoint physical halves; the six column checksum4 equations are exactly the matching condition z_i+(4-z_i)=4. There is no all-one restriction, no unnecessary 51^6 brute force and no risk of treating the 51 GF5 patterns as a different palette.

The executable [census](../../research/hyp105_g5e2b3b_full_matching_flows.py) evaluates the finite formula with integer arithmetic. The independent [tests](../../research/test_hyp105_g5e2b3b_full_matching_flows.py) cross-check one example in every v_left×v_right cell against the existing **51³-side exact GF5 meet-in-the-middle** histogram; and check **every one** of the v_left=v_right=6 signed orbits against the independent exact 2^12-edge nowhere-zero prescribed-boundary flow checker accepted in B3.1-A. Validation also verifies orbit sizes, coordinate conservation, checksum4 local choices and fail-closed budgets.

## 3. Complete matching-case finite classification

All 5,486 sign/color-preserving orbits and their exact signed masses:

| v_L / v_R | Positive orbits | Zero orbits | Positive labeled events | Zero labeled events |
|---|---:|---:|---:|---:|
| 4/4 | 20 | 0 | 9,000 | 0 |
| 4/5 | 225 | 0 | 153,000 | 0 |
| 4/6 | 36 | 0 | 21,000 | 0 |
| 5/4 | 225 | 0 | 153,000 | 0 |
| 5/5 | 3,716 | 0 | 2,601,000 | 0 |
| 5/6 | 559 | 0 | 357,000 | 0 |
| 6/4 | 36 | 0 | 21,000 | 0 |
| 6/5 | 559 | 0 | 357,000 | 0 |
| 6/6 | 108 | 2 | 48,900 | 100 |
| **Total** | **5,484** | **2** | **3,720,900** | **100** |

The only zero-flow matching cases are the **already known** disconnected coincident 2C3/2C3 signed configurations in the v_L=v_R=6 branch. Thus the prior 6+6 positive/zero classification extends **to all leafless physically simple six-factor-matching cases** by exhaustive finite computation. All other matching cases have at least 4,806 full-GF5 coefficient assignments, maximum across all cases **135,001**.

These integers describe abstract matching projection templates, not the 11,663 general factor-forest shapes from B3.0. In particular, they do not imply that any fixed injective pair mapping has 3,720,900 trades, or that positivity implies existence of the corresponding GQ incidences.

## 4. Exact all-h independent-random matching-contribution expectation identity

Define C_(v,w) as the exact sum of GF5 weight counts F(A,B), **over all 10 balanced unordered signs and all column-named matching physical profiles with v left and w right coordinates**, counting every named template exactly once. The complete numeric coefficients are

| v_L / v_R | 4 | 5 | 6 |
|---|---:|---:|---:|
| **4** | 1,212,700,680 | 9,814,303,080 | 552,904,560 |
| **5** | 9,814,303,080 | 80,573,932,980 | 4,578,391,800 |
| **6** | 552,904,560 | 4,578,391,800 | 259,890,480 |

Fix s=2^h, V=(s+1)(s²+1), N=(s+1)V, a=min{r:binom(r,2)>=V}, K=binom(a,2), and let M6(G_s) be the **actual** number of unordered six-edge matchings of original GQ incidence edges. For one such original matching the six left-side endpoint pair labels and six right-side endpoint pair labels are independent uniform *ordered injective* six-tuples in K: (K)_6 possibilities per side.

For a particular column-named canonical physical projection profile with v distinct coordinate masks, there are **exactly (a)_v** realizations using actual coordinates in [a]: the distinct incidence masks distinguish the v physical positions. It is crucial **not** to divide again by v!, since the coordinate masks distinguish their roles. This yields the following exact mathematical identity valid for every s=2^h:

```text
E_independent[R3_matching(B_s)] =
    M6(G_s)/(51^6*(K)_6^2)
    * SUM_{v,w=4}^6 C_(v,w) * (a)_v * (a)_w.
```

This is the ENTIRE GF5 3v3 contribution from factor-matching six-sets only, not an expectation of the full R3. The coefficient computation is an independently checkable finite integer identity; the transfer to each h uses uniform injective labeling symmetry and exact probability counting, not asymptotic extrapolation from GF2/GF4.

Greedy matching construction yields M6 ≥ ∏_(j=0)^5 (N−2j(s+1))/6!, and trivially M6≤(N)_6/6!. The strictly positive leading coefficient C_(6,6)=259,890,480 gives, using a=Theta(s^(3/2)), N=Theta(s^4), **E[R3_matching]=Theta(s^6)**, in the independent-uniform-label model only. Thus this full matching class is not the source of any strictly better **random** R3 exponent. It does NOT preclude some structured nonuniform correlated labeling with smaller matching contribution.

## 5. Exact remaining research gap and STOP conditions

- **OPEN B3.1-B2:** complete positive GF5 classification for factor forests with repeated original endpoint vertices. A selected original GQ six-edge subgraph is a forest (girth8), but not necessarily a *matching*. Physical pair labels may repeat as projected edges, invalidating the simple-graph assumption of this B1 slice.
- **OPEN B3.2-E:** obtain actual **uniform-in-h upper** bounds on every positive six-column motif for the SAME geometry-aware injection, alongside the **R2 upper**. A bound on matching contribution alone cannot close R3.
- A complete 4–6 coordinate matching census cannot establish the proposed strict ε2/ε3 exponents or new ASET theorem. No world-priority claim for this specialized computer classification has been independently researched.

**Decision:** accept the exact all-h matching-class expectation polynomial and finite six-matching positivity certificate only. Keep HYP-105 roots OPEN. No Rust or production ASET construction.
