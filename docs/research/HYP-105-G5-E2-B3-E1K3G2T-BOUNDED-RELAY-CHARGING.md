# HYP-105 E1-K3-G2-T — bounded original GQ point–line–point relay charging

2026-10-12. Root issue [#230](https://github.com/definitely-stable/Mathlab/issues/230); stacked Draft child of [PR #392](https://github.com/definitely-stable/Mathlab/pull/392), pinned S HEAD `6b7aafaf6131074fe9d14b998e467ecedefb3f16`. S final exact-head Contract/INDEX/Research **3/3 SUCCESS**. Main remains unmodified; never merge without mathematical review.

## 1. Why this is different from S

The original one-hop Hall gate in S is a *strictly sufficient candidate*, not equivalent to P2, and it is FALSE on the genuine coherent W32 hardest-M map. Despite scalar P2 positivity `757/143`, there exists an ORIGINAL point subset

    X={1,2,3,5,8,13,14}

with exactly `demand(X)=4820` vs `own_BA(X)=1144` and `adjacent_dual_AB(N(X))=3146` (all numerators scaled by 143), hence geometric Hall shortfall **530/143**. Independent exact integer maxflow and ALL 32768 Hall cuts certified this. Both signed joint Johnson C5 and C6 are negative, so a positive individual rank cannot be the new remedy.

## 2. New candidate: bounded 2-hop ORIGINAL GQ collinearity

Let `(P,L,E)` be TRUE ORIGINAL W(3,s), `s=2^h`. Let coherent globally injective `f,g` determine TRUE sixsource mass by original repeated-point anchor, and TRUE transposed ORIGINAL dual line anchor. Define

    M_p = original B/A source weight at repeated point p,
    A_p = its B/A physical target credits,
    B_l = genuine dual A/B physical target credits at repeated line l,
    rho_a = 70*binom(a,6)/binom(binom(a,2),6).

The demand `D_p=rho_a*M_p` may be satisfied by A_p on p, B_l for a TRUE original incidence (p,l) in E, or A_q transported from another point q along a TRUE ORIGINAL incidence path

    p -- l -- q, with (p,l),(q,l) in E.

Every unit at A_q is spent ONCE across all paths. Every B_l is spent ONCE across all direct source-to-dual routes. Each relay line l has a shared auxiliary bottleneck `kappa_l >= 0`:

    sum_{p,q : p--l--q} x_{p,l,q} <= kappa_l.

This is not an assertion that kappa_l=1 is geometrically implied or that the bounded model is always feasible. The parameter is an explicit **protocol hypothesis**. A relayed BA credit does **not** count as fresh positive resource: it was already counted as part of A_q, regardless of the route.

There are no edges between arbitrary original points; point-to-point transfers must share the same genuine ORIGINAL GQ line. Specifically, forbidden unrestricted three-hop point–line–point–line direct transfers would make all original points reach all original lines in a generalized quadrangle and erase meaningful geometric locality.

## 3. Exact all-h mincut/Hall characterization (model theorem, not P2)

For original point subset U, let N(U) be the set of original lines incident to at least one point in U. For a relay-gate activation subset J subseteq N(U), let P(J) be the original points incident to some l in J. The exact bounded-relay model is feasible **iff**, for EVERY pair (U,J), the following holds:

    sum_{p in U} D_p <=
      sum_{p in U union P(J)} A_p
      + sum_{l in N(U)} B_l
      + sum_{l in N(U) minus J} kappa_l.

Proof: build a directed flow network with source-to-point arcs D_p, point-to-own-BA credit and point-to-incident-original-dual-credit arcs of capacity INF; point-to-incident-original-relay-in arcs INF; original line relay-in->relay-out arc capacity kappa_l shared by ALL point pairs; relay-out to every BA credit at an original point q incident with l arc INF; each own BA and original-dual AB credit-to-sink has its exact physical witness capacity. All finite s-t cuts have the canonical form above, apart from removable unforced zero-cost vertices. Conversely every (U,J) creates a valid canonical finite cut. The max-flow/min-cut theorem proves equivalence for THIS auxiliary charging model.

U=P gives scalar P2, since every original line is in N(P), but the proposed family of Hall conditions is strictly stronger than P2. A counterexample to any (U,J) cannot refute P2 or the original seven-family claim.

At kappa=0, the best J is empty and the condition reduces EXACTLY to S's all-X original incidence-local Hall inequalities. This reduction is checked numerically against S's independently exhaustive 32768 subsets.

## 4. Two independent integer oracles and exact capacity calibration

W32 has 15 original points and 15 original lines. Multiply by exact density denominator 143: D_p=2M_p, own BA credit=143 A_p, original-dual AB credit=143 B_l. Every relay gate has a *single shared integer-scaled* capacity kappa, never one per physical route.

Independent algorithms:

- Dinic exact integer maxflow + all-node flow-conservation + mincut;
- a completely separate adjacency/matrix Edmonds–Karp maxflow;
- independent cut-capacity re-summation and direct evaluation of the generalized Hall inequality with the original point subset U and original relay activation subset J;
- reduction at kappa=0 to S's exact max-flow and separately exhaustive 32768 ordinary Hall cuts.

Test kappa=0, kappa=143 (one physical target-credit equivalent per ORIGINAL line), and discover the exact **minimum UNIFORM integer-scaled kappa** for the two genuine original/dual W32 maps by monotone binary search, with exact infeasibility at kappa-1 and feasibility at kappa (if finite). Store also the least whole number of physical target-credit units per original line. Calibrating minimum kappa is **finite reverse-engineering**, not an all-h theorem or a theoretically justified universal capacity.

The permanent-1/2 original source weights and exact rank5/6 correlations are independently preserved by S's full original+true-dual oracle. The output records exact finite Hall failures with original point IDs, original relay line IDs, the four original demand/credit/gate values and no extrapolation to all W32 physical labelings.

## 5. Model falsification and next substantive proof obligation

The reference tests include: a genuinely shared relay gate that cannot be double-spent by two demand points; a BA target credit that cannot be counted twice even via many relays; exact one-line threshold and its infeasibility at kappa-1; existing original-dual direct credit at kappa=0; and invalid GQ IDs and capacity types. The tests must fail on accidental independent per-path relay budgets or unrestricted complete bipartite transfers.

Interpreting results:

- If kappa=143 remains insufficient, report an exact counterexample for that *specific* capacity choice and inspect its new Hall cut.
- If a finite kappa is sufficient on two W32 maps, it certifies only those two maps and this auxiliary geometric flow.
- Even if both maps pass, a genuinely new all-h theorem would require a **uniform** justified bound kappa_l based on original GQ incidence properties and target-witness structure, and an all-f,g proof of the simultaneous generalized Hall inequalities. Choosing kappa from the instance itself cannot serve as that theorem.
- If all finite two-hop relay capacities fail, collinear BA transfer is structurally insufficient; explore explicitly bounded new positive families (P7), without inferring P2 false.

Root #230/#176/#169 remain OPEN. P2, P7, Branch A/B, full R3 upper, s^6 lower bound and ASET exponent remain OPEN. Dedicated Contract + INDEX + full Research must pass at exact FINAL HEAD. Independent mathematical proof review remains mandatory.
