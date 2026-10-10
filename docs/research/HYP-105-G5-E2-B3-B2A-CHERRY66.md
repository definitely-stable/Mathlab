# HYP-105 B3.1-B2-A — positive GF(5) flows for nonmatching factor-cherry forests

Date: 2026-10-10. Parent [#176](https://github.com/definitely-stable/Mathlab/issues/176). Extends [complete factor-MATCHING classification](HYP-105-G5-E2-B3-B-FULL-MATCHING-FLOWS.md), [six-forest projection polynomials](HYP-105-G5-E2-B3-FOREST-PROJECTION.md), and [independent 782-state GF(5) character oracle](HYP-105-G5-E2-B3-B1B-FIVE-SIX-EXACT.md).

**PROVED RESTRICTED NONMATCHING SIX-EDGE FOREST GF5 POSITIVITY / EXACT 66-ORBIT COMPUTER-AIDED CERTIFICATE / ALL-h RANDOM-CLASS EXPECTATION THETA(s^6) / NO FULL FOREST CLASSIFICATION / NO INDIVIDUAL ALL-h R3 UPPER / NO NEW ASET EXPONENT / NO PRIORITY CLAIM.**

## 1. Why the prior completed matching classification does not apply

Six *distinct original* edges of the W(3,s) incidence graph, s=2^h, always induce a forest because girth is eight, but need not be pairwise factor-disjoint. Focus on a **single cherry**: exactly two edges share one left point p; their two right line endpoints are distinct; all remaining four original edges are disjoint from the cherry and each other. Then exactly FIVE distinct left factor point endpoints and SIX distinct right line endpoints occur. Under injective pair labels, two left projected pair edges are identical, while the right six pair edges are distinct. This is **not** among the 610 simple projected matching profiles of PR #214.

Further restrict both physical projections to exactly SIX touched coordinates, all of positive degree at least two. Each has six column edge-occurrences, total physical degree twelve, hence every physical vertex has degree **exactly two**.

On the left the doubled pair must be an isolated weighted double edge (two physical coordinates of degree two); the remaining four distinct edges form a C4 on the four other coordinates. In the dual graph of six named columns this is TWO parallel edges joining the repeated-point column pair, plus a simple C4 on the other four columns. The right simple six-edge two-regular projection is C6 or 2C3. This is an elementary structural if-and-only-if for the precise stratum above, not for arbitrary six-forests.

Fix repeated columns (0,1), a representative left C4=(2,3,4,5,2), and retain physical colors. Other named left C4 adjacency patterns: 3. Other choices of the repeated pair of column IDs: 15. The right projection has 70 named 2-factors and 10 unordered 3v3 sign partitions.

## 2. Exact finite GF5 certificate

Each physical vertex is incident to exactly two columns, so eliminate coordinate conservation as in accepted B3.1-A to obtain a 12-edge contracted multigraph on six columns, with **two parallel LEFT edges**. This case cannot be represented by the old simple-factor classifier, but the exact existing prescribed-boundary inclusion-exclusion formula applies without modification.

The stabilizer of the fixed left multigraph is S2 x D8 (size 16). For each of the 70 right 2-factors and 10 balanced unordered signs, quotient by this action on the **same six column IDs**; the two physical colors are not exchanged. The **700 signed named cases** reduce to **66 orbits** with exact masses summing to 700.

Exact results:

| Right projection | Signed labeled cases (one left representative) | Sum of 51-pattern GF5 flow counts |
| --- | ---: | ---: |
| C6 | 600 | 3,354,936 |
| 2C3 | 100 | 547,128 |
| **Total** | **700** | **3,902,064** |

Every one of the 66 orbits is **positive**. Across all 700 signed cases the exact GF5 flow count is between **4,560** and **6,786**, with NONE zero. Three left C4 patterns contribute the exact integer coefficient **11,706,192**. These are full GF5 checksum4 flow counts with 51 admissible nonzero coefficient choices *per column*, not unit-only collisions. The independent tests compare selected templates to a separate integer **782-state dual Fourier solver** and an exact **51^3-per-side meet-in-middle** GF5 solver; they also check every left stabilizer symmetry.

This is exhaustive only for the one-cherry / left six coordinates / right six coordinates model, not for all 11,663 general abstract forest shapes.

## 3. Fixed-label necessary obstruction, every h

Let U_L(f,g) be the number of genuine six-edge original factor-cherry forests with exactly one repeated left point, all six right line endpoints distinct, and both physical projections having six touched coordinates with no degree-one vertices. Let U_R be the symmetric repeated-right-line class. The two forest classes are disjoint as six-column sets.

Each such six-set has **TEN** distinct unsigned 3-versus-3 signed events. The above finite exact classification guarantees at least 4,560 admissible 51-pattern GF5 weight assignments **per event**. Therefore, for every s=2^h and every fixed injective labelling:

    R3(B_s(f,g)) >= 45600*(U_L(f,g)+U_R(f,g))/51^6.

Distinct six-column sets and distinct unsigned sign partitions are distinct summands in the defined risk functional, not an assertion of disjoint sample events in a union probability. We have **not** proved U_L+U_R is positive for every labeling, and this is a lower bound, not an upper.

## 4. Exact independent-label expected risk identity

Let V=(s+1)(s^2+1), Delta=s+1, N=V Delta, K=binom(a,2), where a is the minimum integer with K>=V. Define M_cherry(G_s) as the *actual* number of unordered six-edge forests with exactly one repeated LEFT point and four other independent original factor incidences. Every such forest has a unique cherry (the center and its two edges), so this definition has no multiplicity overcount.

For the fixed two named cherry columns, the left projection's three possible C4 dual patterns each has **(a)_6 / 2** physical coordinate realizations. The factor 1/2 matters: the two left coordinates with identical column-incidence mask {0,1} are indistinguishable when actual physical coordinate symbols are assigned. This exactly matches the previously accepted six-forest probability coefficient **3/2** for v=6 and endpoint multiplicities (2,1,1,1,1). The right projected two-factor of each named graph has **(a)_6** physical coordinate realizations.

There are (K)_5 independent injective left endpoint pair-label choices and (K)_6 right choices. The exact expected 51-pattern risk contribution of this *nonmatching cherry six-by-six class*, for every s=2^h, is

    E[R3_cherry66]
      = M_cherry(G_s) * 11706192 * (a)_6^2
        / (2 * 51^6 * (K)_5 * (K)_6).

Here 11,706,192 is the exact sum of GF5 signed flow coefficients over all three left C4 and seventy right 2-factor patterns and ten sign partitions. The displayed formula is **exact**, including all (a)_6 realizations and the left automorphism factor 1/2; no finite-s power fitting is used.

A greedy lower bound is

    M_cherry(G_s) >=
      V * binom(Delta,2) / 4! *
      product_{j=0}^3 (N - (3+2j)*Delta),

by choosing a left point and two incident lines, then four more factor edges disjoint from all previously selected factor vertices. Conversely

    M_cherry(G_s) <= V*binom(Delta,2)*binom(N,4).

Both grow as Theta(s^21); the per-forest label expectation is Theta(s^-15) because a=Theta(s^(3/2)), K=Theta(s^3). Consequently

    E_independent_uniform_injections[R3_cherry66] = Theta(s^6).

**Interpretation:** the old leading random-model exponent s^6 survives even after restricting to a concrete NONMATCHING factor-forest class. Eliminating or optimizing only factor-disjoint matching positive motifs cannot by itself certify o(s^6). This is a model-specific expected-risk lower, not a fixed-label universal lower nor a new extremal ASET theorem.

## 5. Precise remaining steps

- **B3.1-B2-B:** extend the repeated-factor-endpoint classification to other leafless physical coordinate sizes vL or vR = 4/5/6 and to both-side repeated endpoints and larger components. The previous 11,663 forest-shape catalog is only NECESSARY leaflessness and is not a complete positive-flow census.
- **B3.2-E:** obtain a common **fixed, explicit, all-h correlated geometry map** bounding full positive four- and six-column GF5 motif multiplicities and hence strict joint R2/R3 upper exponents. Finite GF2/GF4 records and average random estimates are not such a proof.
- **Novelty:** the GF5 prescribed-boundary flow identity, exact finite character summation, and greedy matching counts are classical tools. This specialized combined stratum and coefficient are verified for the present model, without external scientific-priority claim.

Implementation: [exact 66-orbit checker](../../research/hyp105_g5e2b3b2_cherry66.py); [independent tests](../../research/test_hyp105_g5e2b3b2_cherry66.py). Parent issue [#176](https://github.com/definitely-stable/Mathlab/issues/176) remains **OPEN**.
