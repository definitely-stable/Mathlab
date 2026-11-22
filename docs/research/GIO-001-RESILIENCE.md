# GIO-001.1 — robust two-class motif supersaturation and disjoint packing

**Root:** [#791](https://github.com/definitely-stable/Mathlab/issues/791), program [#790](https://github.com/definitely-stable/Mathlab/issues/790). Frozen foundation [#230](https://github.com/definitely-stable/Mathlab/issues/230), [#789](https://github.com/definitely-stable/Mathlab/pull/789), main a49e1de8a46b6afbeb668c4413647fd4eeb63d8a. The integrated manuscript [Branch A proof](HYP-105-AA4-BRANCH-A-INTEGRATED-TWO-CLASS-PROOF.md) and its [internal referee](HYP-105-AA4-BRANCH-A-FINAL-EVIDENCE-REVIEW.md) supply the source identities used below. Required prior main Research succeeded. This is a **new all-order proof candidate**, not an accepted or externally refereed extension, and not a finite extrapolation. The unrelated G2BB2 DRAT build failure is outside this model.

## 1. Statement and quantifiers

Let s=2^h, V=(s+1)(s²+1), N=(s+1)V, I the N genuine original point-line flags of W(3,s), a=min{b: binom(b,2)≥V}. Independently of all coefficient randomness, fix arbitrary COMPLETE separately globally pair-injective maps f and g into unordered pairs of [a], with arbitrary mutual correlation. Let Z⊆I be an arbitrary deleted set (possibly depending on f,g), A=I\Z. Denote by D_A and B_A the historical D6 and U_BB_overlap counts of distinct ORIGINAL unordered six-ID sets all of whose flags belong to A. Define B_A^prod ⊆ B_A to contain exactly those BBo sixsets constructively produced by an accepted original physical proper three-edge path with all six original flags in A and the three prescribed genuine GQ projection anchors. B_A^prod depends on f,g,A, but its definition never depends on a choice of LOW core or random selector. These are source sets, not oriented paths, signed events, or physical-edge multiplicities.

**Theorem R (resilience).** There exist absolute rational ρ>0, δ_r>0, and an integer h0 such that for EVERY h≥h0, EVERY legal f,g and EVERY Z⊆I with |Z|≤ρs^4,

    D_A + B_A^prod ≥ δ_r s^6, hence D_A + B_A ≥ δ_r s^6.

**Strengthened class statement.** The argument below proves the stronger displayed inequality with B_A^prod, because HEAVY produces genuine D6s while LOW produces BBo sets from actual paired proper paths; the source inverse is at most two-to-one even after deletion. This is needed for the coefficient-blind packing and ensures that its BBo sign-event bound uses the **actual aligned dual flow topology**, not a conjectured uniform per-sign bound for every nonproduced historical BBo sixset. The original desired D_A+B_A inequality is an immediate consequence.

The result is eventual in h. It does not claim a useful numerical threshold for small s or optimal ρ. In particular no random-deletion hypothesis, no spanning GQ axioms imposed on A, and no extension of labels after deletions. All GQ projection and spectrum identities refer to the true undeleted I.

**Corollary P (packing, already follows from R).** For every such fixed f,g and sufficiently large dyadic s, the full original family contains at least floor(ρs^4/6)+1 pairwise flag-disjoint witnesses, each either historical D6 or constructively produced historical BBo. More generally from an initial Z0 with |Z0|≤ρs^4 the guaranteed additional packing size is floor((ρs^4−|Z0|)/6)+1. This is Θ(s^4) for Z0=∅, since N=Θ(s^4) and each witness uses six flags. The proof is constructive by greedy removal but not a promise of a polynomial-time large-order enumerator.

**Corollary C (independent coefficient tail).** For the coefficient model of #230, uniform independent choices from the exact 51 support-four GF(5)* checksum-four patterns, there exists a coefficient-blind family of m≥floor(ρs^4/6)+1 distinct signed collision events with disjoint six-flag supports. If X counts successes among these chosen events, then with p*=5175/51^6,

    P[X < p*m/2] ≤ exp(−p*m/8),   p=p*.

Thus with probability 1−exp(−Ω(s^4)), at least Ω(s^4) pairwise flag-disjoint signed collisions occur. Any deletion set hitting every realized signed collision must have size at least X. This is a statement about the exact independent random coefficients and deletion-only collision cleanup, NOT an upper bound for ASET, not an arbitrary dependent coefficient model, not a bound on the probability of a sum of dependent signed events.

## 2. Frozen constants and source budgets

Use all original notation from Sections 1–2 of the frozen proof: physical H on [a]² owns exactly two opposite real diagonals per original flag, no repeated physical-edge owner. J on I conflicts if flags share one original factor and intersect in the other typed coordinate pair. Let H_C and J_C restrict to a named paired owner set C.

Freeze cap ρ_cap=1/32 before all other parameters. For h≥32, the original deterministic SRG and minimal alphabet estimates give, with u0=2^-32, t0=2^-16,

    v=(1+u0)(1+u0²), nu=(1+u0)v,
    M=(1+u0²)(1+23t0/16), A0=2v+23t0³/4+4t0^6,
    e(J)<2M s^4,  a²<A0 s³,   s^4≤N≤nu s^4,
    4nu<17/4, 8(nu+M)<17, 24(nu+M)<49.

The original SRG formula e_col(f),e_col(g)≤(s²+1)(s²+a−2) remains valid, since labels and original geometry do not change. All bounds for subsets use monotonicity in full I. In particular deletion cannot increase the physical degrees or e(J).

Use the published ordinary graph C6 supersaturation theorem with existential absolute C_graph,c_graph>0: e(F)≥C_graph |V(F)|^(4/3) implies at least c_graph(e(F)/|V(F)|)^6 unoriented simple cycles. This is the k=3 ordinary graph case of Simonovits' supersaturation result, as in Jiang–Yepremyan, *Combinatorics, Probability and Computing* 29 (2020), 698–721, DOI [10.1017/S0963548320000206](https://doi.org/10.1017/S0963548320000206), [arXiv:1707.03091](https://arxiv.org/abs/1707.03091). No published numerical constants are asserted.

Choose rational C0≥max(1,C_graph), 0<c0≤min(1,c_graph) ONCE. Set

    R=ceil(512 A0(1+128M)), T=ceil((17/2)R³C0³),
    K=10, c=7/8−ρ_cap−4M/(K+1), w=(4c)^3/A0²,
    δ_r=min(c0/R^6,w/4).

The positive c and w are checked by exact rational inequalities; δ_r>0 and δ_r≤1. T does not depend on the eventual optimized deletion fraction ρ, actual s, labels or Z.

## 3. HEAVY survives adversarial deletion

Freeze Q_T={x:d_H(x)>Ts} in the FULL graph H, and E_T the count of distinct real edges touching Q_T. In HEAVY, E_T≥s^4/8. Whole flag deletion removes at most 2|Z| of these edges, so the surviving original owner set L has at least

    |L| ≥ E_T/2−|Z| ≥ (1/16−ρ_cap)s^4 = s^4/32.

Caro–Wei and the full J bound give an independent set I0⊆L with

    |I0| ≥ |L|²/(|L|+2e(J[L])) > s^4/[32(1+128M)].

Use exactly the original global typed binary cuts: for each owner the probability both pairs cross is 1/4, so a coherent pair retains ≥|I0|/4 independent owners. Every retained owner has a surviving real heavy-touching edge. Choose one witness edge and one endpoint in Q_T per owner; some first-cut bit class has ≥|I0|/8 witness owners. Let U all Q_T vertices of this bit, r=|U|>0, Y their opposite-bit actual neighbors in the retained graph, E edges between them. E≥|I0|/8, Y∩U=∅, |Y|≤a².

Taking min(r,|Y|) actual vertices with largest U-degree retains ≥Er/a² edges in a real simple F with ≤2r vertices. Hence

    e(F)/|V(F)| ≥ |I0|/(16a²) > s/R,
    |V(F)| ≤ 2|Q_T| < 8N/(Ts) < (17/2)s³/T ≤ (s/(RC0))³.

Therefore e(F)≥C0 |V(F)|^(4/3) and the external theorem gives ≥c0(s/R)^6 C6s. Every edge owner belongs to A. The frozen original proof's C6 lift applies to ANY real subgraph of the paired J-independent cut graph: cyclic distance 1 changes both typed symbols; distance 2 repeats would give a conflict between distinct owners; distance 3 repeats violate cut parity. All six typed symbols are distinct separately, and the six source IDs uniquely determine the shared physical cycle up to reversal/rotation by named consecutive intersections. Thus D_A≥δ_r s^6. No deletion-dependent threshold, graph clone, or deleted owner used.

## 4. LOW paired CORE and same-global selected moments

In LOW, E_T<s^4/8. Remove Z, all full-H heavy-touching owners, and all owners whose FULL J degree exceeds K. Let C be what remains. As the number of heavy-touching owners is ≤E_T and high-J-degree owners ≤2e(J)/(K+1),

    |C| > c s^4,    max degree(H_C)≤Ts,   max degree(J_C)≤K,
    W3(H_C) ≥ (4|C|)^3/a^4 > w s^6.

The walk inequality is exactly Section 4 of the frozen proof (convexity x log x plus oriented-edge degree-biased marginals); no assumption that H_C is bipartite. If D_A≥δ_r s^6 we are done. Otherwise D_A<δ_r s^6≤s^6.

One shared global local-minimum priority selection in J_C plus both coherent typed cuts defines a bipartite graph G. Every proper rpath (all r+1 typed symbols distinct separately, r=2,3) survives with probability≥1/q_r, q_r=4^r(K+1)^r, by the same conditional overlap integral. For its uncut endpoint matrix P_r, Jensen on this SAME selector gives ||P_r||_F²≤q_r² E tr(A_G^(2r)). No independence between paths is asserted. Each selected ordinary C6 lifts injectively into D_A; each possible original D6 cycle passes both independent typed cuts with probability 1/1024 at most. Thus E C6(G)≤D_A/1024. Write W_C=sum_{i∈C}1/(d_JC(i)+1)≤N. The bipartite closed-sixwalk argument from the frozen proof yields

    E tr(A_G^6) ≤ (3/128)D_A +36(Ts)² W_C,
    (E tr(A_G^4))² ≤ W_C E tr(A_G^6).

Consequently choose q2=1936,q3=85184 and

    L6=1+ceil(36nu T²),
    L4=q2² ceil_sqrt(nu L6)+17T,
    ||P3||²≤q3²L6 s^6,  tr(H_C^4)≤L4 s^5.

Here tr(H_C^4) denotes the trace of the fourth power of the adjacency matrix. The last bound uses the proper-2path moment and literal ordered coordinate returns Qx+Qy=8|C|+4e(J_C)<17s^4, as in the frozen proof. The two gap-2 positions and PSD argument for gap-3 give

    I_improper ≤49T s^5.

These bounds are on one surviving paired C, including in the case that the deleted flags target the original physical degrees, conflicts, or every largest observed motif.

## 5. New exact projection-anchor deletion budget

For every NONincident original point q and line r in FULL I, let q–l–p–r be the unique three-edge GQ projection, so its respective anchor flags are (q,l),(p,l),(p,r). There are exactly four ordered off-coordinate physical endpoint pairs representing q,r. The original missing and incident pair masks and endpoint-overlap failures are unchanged from Section 5 of the frozen proof; their combined size is <17s^5.

Fix one original flag (a,b). Its occurrence among such projected anchor triples can be counted in three DISJOINT positions.

* Left outer: q=a,l=b; choose p≠a incident b (s choices), then r≠b through p (s choices). The GQ girth forbids q incident r; if two different p gave the same r, two original lines would contain two common points, impossible. Exactly s² different (q,r).
* Middle: p=a,l=b; choose q≠a on b and r≠b through a, giving s² distinct nonincident pairs.
* Right outer: p=a,r=b; choose l≠b through a and q≠a on l, again exactly s² distinct nonincident pairs (dual of the first).

The anchors are three distinct flags and the FULL nonincident projection is unique. Thus the position sets cannot overlap for a fixed flag. This is the exact 3s² single-flag projection load, independent of the labeling or any already deleted flags. For Z arbitrary, take the union of those sets; overlaps among different flags can only reduce its cardinality. The affected endpoint mask satisfies

    |E_deleted| = 4 |{(q,r): their FULL anchor triple meets Z}|
                ≤ 12s² |Z| ≤ 12ρ s^6.

The four orientations are distinct because both maps are injective unordered pairs of distinct symbols, and two different (q,r) cannot encode the same ordered physical ends. For singleton Z this bound is an equality for the deletion-only mask, including projections that might independently fail the original overlap test; we need only a union upper bound after combining with old masks. We do NOT assume the remaining A has a unique replacement projection; a missing original anchor is a failure.

By Cauchy on proper path endpoints and sqrt(x+y)≤sqrt(x)+sqrt(y), define E=q3 ceil_sqrt(17L6) and obtain

    I_endpoint ≤ q3 sqrt(L6(17/s+12ρ)) s^6
                ≤ E s^(11/2)+q3 sqrt(12ρ L6) s^6.

This additional term is order s^6, so it cannot be discarded by sending h→∞. This is why the original theorem with Z=∅ alone did not imply resilience.

## 6. Interior blockers and exact surviving BBo inverse

Only paths that pass the preceding masks enter the four interior-symbol tests. They use the same full original projection and all its anchors lie in A. The source book for first inner x uses q collinear p, actual anchor (p,r)∈A, actual first residual owner (j,m)∈C, and literal shared y; the three-corner triple and exact two-walk completion charge remain those of the frozen proof. The A-side book counts satisfy R_A(p,y)≤R_I(p,y) pointwise, and the C-side is the actual surviving core. All source terms, sum of nonnegative squared terms and multiplicities in the original proof can be bounded from above with **full I** on the A-side. In detail K_AC(p,j)≤K_IC(p,j), the degree product sum ≤sum_{(k,y)}d_H(k,y)d_HC(k,y)≤4N Ts, and the same original SRG G_f bound is valid. No projection uniqueness, degree or collinearity assumption is made on the damaged geometry itself. Thus the original mixed-book estimate remains

    Bx²,By² ≤ 46(K+1)T s^(23/2).

The Cauchy bound for four interior blockers is unchanged, with B=ceil_sqrt(46(K+1)T), D=4 ceil_sqrt(B T L4):

    I_fourblockers ≤ D s^(47/8).

An accepted proper directed 3path has its three distinct residual owners in C⊆A and its three genuine distinct projected anchors in A. The endpoint and interior tests make the repeated point/line pair disjoint from all respective path symbols. Therefore all six IDs distinct: historical B/B-overlap with repeated point and line sharing the central flag, doubled pair plus C4 on each typed side. The original source inverse gives exactly two directed paths per produced unordered sixset (simultaneous reversal), or zero for other BBo. That inverse still holds with deletions; both reverse paths use the identical three C-owners and identical A-anchors. In particular

    2B_A^prod ≥ W3−I_improper−I_endpoint−I_fourblockers.

We never count a deleted anchor merely because the corresponding physical paths survive, and never require an available anchor to belong to the smaller C.

## 7. Quantifier closure: explicit positive rational deletion fraction

Put b=w/8 and choose ONCE

    ρ = min(ρ_cap, b²/(12 q3² L6)) >0,
    s0 = max(2^32, ceil(49T/b), ceil((E/b)²), ceil((D/b)^8)),
    h0 = ceil(log2 s0).

All constants are finite and fixed. In particular T,L6,L4,w were fixed BEFORE ρ; there is no circularity. At every dyadic s≥s0, the four error pieces (improper, old endpoint, deleted-anchor, interior) are separately ≤b s^6 because 12ρ q3²L6≤b². Their sum is ≤w s^6/2. Thus in LOW with D_A<δ_r s^6,

    2B_A^prod > (w/2)s^6,    B_A^prod > (w/4)s^6 ≥ δ_r s^6.

Together with HEAVY and the already-large-D_A case this proves R under the published theorem input, uniformly for all h,f,g,Z. Correct quantifier order is cap → choose existential C0,c0 → R,T → K,c,w, moment/error constants → ρ → h0 → every s,f,g,Z. The exact rational ledger tests each inequality after raising fractional-power bounds to integer powers. Example ledgers with hypothetical C0,c0=(1,1),(2,1/5),(7/3,1/17) are arithmetic checks ONLY, not validated numerical graph constants. The cap is not the proved deletion fraction, and ρ is not an extremal threshold.

## 8. Packing and independent collisions

Start from any Z0 of size ≤ρs^4. At step j, if |Z0|+6j≤ρs^4, R gives at least one D6 or constructively produced BBo sixset all in the current available set. Choose, for instance, the lexicographically first such original typed motif, append it and delete its six original flags. This selection depends only on the maps, actual source flags and initial deleted set, not on future coefficients. For j=0,…,floor((ρs^4−|Z0|)/6) the inequality holds. Hence the stated packing with the +1 term; the final deletion may exceed the budget, and no extra invocation of R is made. All sets are disjoint by construction.

For each packed D6 fix its alternating sign event of mass 5643/51^6; for a **produced** historical BBo fix one balanced sign event using the independently verified produced topology and its uniform single-sign floor 5175/51^6 ([historical leading forests](HYP-105-G5-E2-B3-B2B-LEADING-FORESTS.md), [fixed-leading classes](HYP-105-G5-E2-B3-E1A-FIXED-LEADING-MOTIFS.md)). Also for all BBo produced by the proof, the direct tree-elimination coefficients in the frozen manuscript independently establish this minimum. Do not use the SUM of ten signs (51750 or 53838) as the probability of one union event. With disjoint source IDs, all chosen events are independent because the coefficient variables are independently sampled per source flag, even if physical coordinates are shared. For X the sum of their indicators, μ=E X≥p*m. The classical multiplicative Chernoff bound P[X≤μ/2]≤exp(−μ/8) gives the claimed bound for threshold p*m/2. A deletion set that destroys every realized collision must meet all X disjoint sets, hence has ≥X flags. No independence between arbitrary overlapping sixsets is required.

**Scientific gain:** the obstruction cannot be eliminated by a vanishing fraction of source-flag deletions; it also forces an extensive family of independently realizable collisions in the original coefficient model. This strengthens the expected-risk obstruction to a high-probability lower bound on necessary deletion-only cleanup. It does not determine the sharp deletion fraction, the true optimum of an altered construction, or prove any unrestricted ASET upper bound.

## 9. Independent finite falsifiers and acceptance

The new Python code keeps true W32/W34 geometry with immutable source flags and both complete maps. Direct full-projection scan versus per-deleted-flag pencil expansion checks exact damaged (q,r) sets (and all four typed endpoint orientations). Physical rainbow DFS versus source-owner/corner-index DFS obtains independent full six-ID D6 enumerations; source-only middle-owner BBo join (with the historical source inverse) versus physical 3walk traversal gives independent produced BBo sets. The source-full enumeration is filtered by exact surviving flag IDs and compared to a NEW actual physical walk enumeration for each deletion mask. For W32 the additional old factor-first and full source-B enumeration are crosschecks. Verify smaller paired CORE with A≠C separately, point-line duality, singletons, point/line stars, mixed star union, disjoint flags, a deterministic map-dependent high-degree deletion, seeded masks, deletion of a BBo central anchor alone when available, and delete-all as a finite diagnostic. Duplicate and invalid IDs, C not subset A, out-of-budget/all-deleted asymptotic requests must fail closed. Finite greedy packing asserts six distinct original IDs per set and no sharing.

Run the specialist hosted tests with python -m unittest discover -s research -p 'test_gio_resilience.py' -v; run python research/gio_resilience.py --out gio-resilience-certificate.json for exact JSON results. The ledger and finite tests are independent falsifiers, not a numerical proof of all dyadic orders. This draft does not itself close #791, change #230/#176/#169 or claim formal/external review. Next after exact-head CI: critical internal review of the new deletion transfer, constant closure and packing/probability corollaries, then narrow acceptance/integration per project rules.
