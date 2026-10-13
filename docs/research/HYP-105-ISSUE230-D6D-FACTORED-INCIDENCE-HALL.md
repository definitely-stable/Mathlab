# HYP-105 #230 — D6-D: one-incidence factorization, exact Hall cuts, full-seven vs partial targets

**2026-10-13. RESTRICTED_THEOREM_C / NEW ALL-h EXACT TRANSPORT EQUIVALENCE / ROOT BRANCH A,B OPEN.**
Stacked over [D6-C Draft #402](https://github.com/definitely-stable/Mathlab/pull/402) pinned head `2ebe9d5faebc14d9d55489a89d70a15cf330a7a1` (all four GitHub-hosted final-head CI SUCCESS). No main modifications or scientific-stack merges.

## 1. Why the next inference is NOT "finite K=9 implies universal Lambda"

D6-C showed that r>=2 original-source-incidence-preserving repair is impossible in the true W32 S68 map, even when all seven ORIGINAL GF5-positive sixset classes are available: eight blocked oriented paths have no such recipient. A much weaker one-incidence overlap is feasible on tested W32 full-G examples, with exact finite optimal maximum recipient loads K=4 (lex) and K=9 (S68). But nothing yet shows an h-independent bound K on an actual PR394 high-h coherent H, nor controls the complete all-seven count S for s>=4.

For a universal compensation proof, one would need an all-h absolute K satisfying `C_H <= K*S_s(f,g)` on the specified retained H, or an exceptional source set of asymptotic mass at most `(16-eta)*s^6+o(s^6)`. This would imply the required gate `C_H <= (16-eta)*s^6 + Lambda*S` in the original projection argument. Neither assertion is established here.

## 2. New all-h exact factorization theorem: common ORIGINAL incidence

Let `I` be any finite set of ORIGINAL point-line incidences in a genuine GQ, `T` a family of three-distinct-incidence source subsets, and `w(T)` their nonnegative INTEGER oriented blocked-path demands. Let `A` be an arbitrary family of **accepted positive** ORIGINAL six-distinct-incidence sets; in the intended application this is the complete accepted seven-class family for the SAME complete globally injective original f,g (not seven GF5 signs or abstract physical-coordinate sixsets).

The **one-source-incidence rule** is `T -> Q` iff `T∩Q!=empty`. A legal assignment sends each of w(T) individual oriented paths to a target Q and caps total paths charged to any Q by INTEGER K.

The following are exactly equivalent for every finite original incidence universe and integer K>=0:

(i) All `sum_T w(T)` oriented demands admit such a charge of congestion <=K.

(ii) The integral **factorized network** admits a complete flow:

```
source -> [T] -> [original incidence e] -> [original sixset Q] -> sink
           w_T      unbounded                unbounded         K each Q
```

with T->e present iff e in T, e->Q present iff e in Q. Capacities called "unbounded" may be assigned `1+sum_T w(T)`, a finite integral integer. Every integral unit of s-t flow traces a T-e-Q path, so it retains at least one genuine ORIGINAL incidence shared by source and recipient. Conversely every one-overlap assignment chooses a shared e and yields such an integer path flow. No capacity is imposed on e because the same ORIGINAL incidence may legitimately be shared by many distinct charges, but Q's TOTAL capacity K is enforced ONCE across all incidences e in Q. **This is NOT a flawed per-incidence capacity multiplication.**

(iii) The exact weighted source Hall inequalities hold for **EVERY** subset U of source triples:

```
    sum_{T in U} w(T) <= K * |N(U)|,
    N(U)={Q in A: Q∩(union_{T in U} T)!=empty}.
```

This follows from the standard integral maxflow/mincut equivalence, since the factorized network represents the exact source-to-recipient eligibility graph. If a source triple T has no target sharing even one incidence, no finite K works, and the algorithm emits an actual unsupported ORIGINAL source witness.

An equivalent **incidence-union** formulation can reduce the analytic object under study: for any U put `F=union_{T in U}T`; the source-closed family `U_F={T in source-support: T⊆F}` contains U and has the SAME union F. Therefore U_F has the SAME recipient neighborhood N(U) and at least as much source demand. It suffices to check the inequalities for all source-closed F (i.e., unions of source triples satisfying F=union_{T⊆F}T):

```
    M(F):=sum_{T⊆F}w(T)
    <= K * B(F),
    B(F):=|{Q in A:Q∩F!=empty}|.
```

The condition is also necessary by taking U=U_F. This theorem is exact for EVERY finite h and every f,g; it is a structural equivalence, **not** a proof that a fixed K exists.

An immediate nontrivial design question is whether the genuine original GQ geometric source demand M(F), including both endpoint and internal-only blocker masks, can be bounded by K times the positive sixset incidence support B(F) with absolute K independent of h, or whether one can isolate a controlled O(s^6) exceptional source demand. This is the correct analytical target for a one-incidence repair, rather than ungrounded guesses from W32 K=4/9.

## 3. Exact finite proof certificates and reconstruction

[Independent code](../../research/hyp105_issue230_d6d_incidence_factored_charging.py) and [unit tests](../../research/test_hyp105_issue230_d6d_incidence_factored_charging.py).

The factorized network has at most `3*|T|+6*|A|` eligibility arcs plus source and sink arcs, compared with up to `|T|*|A|` in explicit pair-to-pair overlap enumeration. Every edge references a real original incidence ID and an original accepted sixset. Input validators reject repeated source/target incidences and invalid negative/noninteger source demand. Integral flow and a failing K-1 maxflow give the minimum exact congestion. The residual source-side cut is reconstructed as an explicit subset U of ORIGINAL source triples, and the algorithm checks

```
  sum_{T in U} w(T) - (K-1)*|N(U)|
      == totalDemand - maxFlow(K-1) > 0.
```

This is an **independently checkable Hall-certificate equality**, not a mere best-effort greedy assignment. For W32, the existing D6-C **direct** T-Q O(|T||A|) flow is rerun and its optimal K MUST agree with the new factored algorithm. Thus the test includes algorithmically distinct flow topologies on the same genuine original data.

## 4. What can and cannot be checked using original finite GQs

**Scope W32 (full seven):** All FOUR genuine globally pair-injective original W(3,2) models (lex, reverse, S68, S72) have the complete accepted seven-positive family census computed independently on the SAME frozen f,g. Full physical G blocked paths are reconstructed independently from their ORIGINAL 3-incidence sources. Both endpoint and internal-only path masses are included. The one-incidence factorized minimum K is compared with the independent direct Hall solver. Separately, delete each individual positive family from the *target pool* and compute unsupported original source-path mass. This is a target ablation experiment, NOT a true new physical graph or a proof that one class is unnecessary.

**Scope W34 (PARTIAL positive subclass):** Build TWO genuine original symplectic-spread W(3,4) complete global models (balanced and reversed g), enumerate the true accepted synchronized BB-overlap sixsets from **original unblocked projected physical paths**, each with exactly two oriented completions. This is a *strictly certified positive subset*, so it is safe to use the targets themselves but FORBIDDEN to equate their count with the unknown complete W34 positive S. Compute original full-G blocked source P3 and the separately labelled relaxed D6B finite-calibration H, both with E+I exact counts. Test one-incidence coverage and possibly exact K **only against this BB subset**. If it fails, the conclusion is only that *BB-only repair* cannot handle the source — no inference about whether a full seven-class repair could work. If it succeeds, it gives a FINITE inequality C<=K*BB_sync<=K*S (for those specific finite maps), but never an all-h bound. Literal PR394 tiny W34 retained H is empty and is excluded from nonvacuous tests.

**No W38 fake S.** There is no accepted complete seven-positive W34 or W38 enumeration; the code never substitutes partial BB or an independent map's count into S.

## 5. First TRUE ORIGINAL GitHub-hosted exact-Hall certificates

Initial successful [D6-D Contract #38342658597](https://github.com/definitely-stable/Mathlab/actions/runs/38342658597) on intermediate HEAD `c9a6c09364a78133552aaa343b78da8441bc6577`: all three dedicated tests SUCCESS in 31.150s and full executable report succeeded on the GitHub-hosted runner. A prior initial test failure was caused ONLY by counting nonempty motif classes instead of all seven allowed class labels during target ablation; the fixed implementation explicitly includes zero-count accepted categories.

For all **four full-seven original W32** maps, the exact minimum K agrees with the separate, independently implemented, uncompressed D6-C T-Q flow and the global pigeonhole lower K>=ceil(C/S):

| TRUE ORIGINAL W32 f,g | E | I | C=E+I | EXACT complete S | K factorized | K independent direct | Excess above ceil(C/S) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| lex | 786 | 156 | 942 | 259 | **4** | **4** | 0 |
| reverse | 676 | 222 | 898 | 169 | **6** | **6** | 0 |
| S68 | 544 | 62 | 606 | 68 | **9** | **9** | 0 |
| S72 | 600 | 58 | 658 | 72 | **10** | **10** | 0 |

For these four W32 maps, deleting any **single** positive class from the *eligible recipient pool* still leaves every blocked source triple with at least one recipient sharing one ORIGINAL incidence; this is exact one-overlap COVERAGE only and does not assert finite capacity K remains unchanged. Several families have zero recipients under S68/S72; the diagnostic includes all seven names and does not silently omit them.

For TWO TRUE ORIGINAL spread-based W34 global pair-injective f,g models, target pool is **only** the genuinely accepted synchronized BB-overlap ORIGINAL sixsets constructed from all original unblocked projection paths in full G (multiplicity exactly TWO), and **never** the unknown full seven-family S:

| TRUE ORIGINAL W34 f,g | Source physical H | E | I | C | True accepted BB_sync sixsets | Exact K using only this BB subset | Excess above ceil(C/BB) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| D5 spread, balanced g | FULL G | 35,190 | 17,570 | 52,760 | 7,649 | **7** | 0 |
| D5 spread, reverse g | FULL G | 36,014 | 17,224 | 53,238 | 7,479 | **8** | 0 |
| D5 spread, balanced g | RELAXED finite-calibration H, NOT PR394 | 6,702 | 3,588 | 10,290 | 7,649 | **2** | 0 |
| D5 spread, reverse g | RELAXED finite-calibration H, NOT PR394 | 6,170 | 3,016 | 9,186 | 7,479 | **2** | 0 |

Every W34 source triple in these FOUR finite regimes has an ORIGINAL incidence in common with at least one of the limited BB_sync recipients. The integral flows achieve the cardinality lower ceil(C/BB) in all four cases and have verified strict K-1 residual Hall cuts. The FULL balanced W34 factorized network has 26,380 actual original source triples and 7,649 BB recipients, using **125,034 eligibility arcs**, with all 52,760 oriented blocked paths allocated at K=7. Reverse FULL has 26,619 original triples and 7,479 recipients and allocates all 53,238 blocked paths at K=8.

**Why this is genuinely new but NOT a root proof:** The W34 positive-recipient set is a STRICT subset of the full unknown all-seven `S`, so these are valid finite upper bounds `C<=7*BB_sync<=7*S` and `C<=8*BB_sync<=8*S` for those exact complete f,g and full-G H, with smaller constants for the two finite calibration H policies. But they do NOT apply to arbitrary correlated maps, all h, or the PR394 spectral pruned H. The eight examples all saturate the trivial K>=ceil(C/targets) floor; no positive h-uniform geometric source-expansion theorem follows. This is a potential constructive direction for analytic research, not evidence of Branch A resolution.

All eight exact K values and certified positive recipient scope are frozen in the new unit tests. Re-run the final HEAD CI after the pinning commit before marking the child slice accepted.

## 6. Acceptance, claims and next mathematical proof requirement

D6-D source states only `all_h_transport_factorization_and_exact_Hall_identity=PROVED`; `all_h_uniform_bounded_congestion=OPEN`, `all_h_original_seven_lower=OPEN`, `all_h_infinite_small_S_counterfamily=OPEN`.

A successful hosted CI validates finite exact counts, integrality, conservation and oracle agreement, but is not a formal verification of the ALL-h mathematical theorem. The analytic network factorization and incidence-union Hall equivalence must receive independent mathematical review before any stronger claim or merge.

For D6-E, derive a genuine all-h analytic bound on M(F)/B(F) from original GQ source and positive-sixset geometry, with explicit separate control of E and internal-only I, or produce a new infinite coherent labeling family that disproves a precisely pinned bounded-congestion conjecture. A finite W32 class ablation, unsupported W34 BB-only source, or the crude K>=C/S pigeonhole ratio are not substitutes for this. Keep Draft, ROOT #230/#176/#169 open, and leave main unchanged.
