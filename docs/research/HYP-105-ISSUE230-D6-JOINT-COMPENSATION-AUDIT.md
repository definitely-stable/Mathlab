# HYP-105 / issue #230 — D6-A: coupled original-GQ compensation audit

**2026-10-13. Outcome: OPEN_WITH_FORMAL_BLOCKER; experimental FINITE audit, NOT Branch A or B.**
Stacked on [D5 Draft #399](https://github.com/definitely-stable/Mathlab/pull/399), pinned D5 HEAD `edf7bf95dc4abcb8cf0e74637f61d0d457805933`. Preserve `main` and keep #230, #176, #169 OPEN. Do not merge before an independent mathematical proof review and exact-head CI acceptance.

## 1. Why D5 does NOT resolve issue #230

D5 constructs one globally injective original spread-based `f_s` on the *minimal* physical alphabet and proves, for EVERY valid complete original `g_s` and EVERY retained `H_s⊆G_s` with `R_s=o(s^4)`, the true original endpoint-chord degree energy `W_H >= (9/32+o(1))s^6`. This rejects the **unconditional auxiliary small-energy lemma** `W_H=o(s^(59/10))` even on any pruning retaining all but `o(s^4)` original physical edges. It does NOT estimate the same constructions' seven-family original sixset count `S_s(f_s,g_s)`.

**Logical quantifiers.** D5 gives `exists f_s forall g_s forall H_s` a high-energy assertion. Root Branch A asks `forall f_s,g_s` a positive *motif* assertion. Root Branch B asks `exists a single infinite sequence of complete f_s,g_s` with `S=o(s^6)`. Neither follows from a degree-energy result. In particular D5 does not disprove the implication `S=o(s^6) => W_H=o(s^(59/10))`: the antecedent on the D5 family is unknown.

D3's exact signed decomposition `W_G=Wmean+Wcorr`, D5's unsigned retained energy, and D1's path-blocking count are different observables. A proof that substitutes one for another without a transfer bound is invalid.

## 2. The exact coupled model: what must be counted on ONE complete f,g

Given a globally valid pair-labeling of the TRUE ORIGINAL `W(3,s)`, let `H⊆G` be a genuine physical diagonal subgraph. For every proper oriented three-path in H whose endpoints correspond to a **nonincident original (q,r)**, let `q-l-p-r` be the unique ORIGINAL projection. Its four collision bits are:

- LE: `f(p)` meets the two first-coordinate endpoint values;
- LI: `f(p)` meets the two first-coordinate internal values;
- RE: `g(l)` meets the two second-coordinate endpoint values;
- RI: `g(l)` meets the two second-coordinate internal values.

Let `C_b(H)` be the count at bitmask `b=LE+2 LI+4 RE+8 RI`. The following are **exact identities**, valid all `s=2^h`, for fixed `f,g,H`, not new lower bounds:

```
P_nonincident_endpoint_complete(H) = sum(b=0..15) C_b(H)
G_good(H) = C_0(H) = 2*BB_sync(H)
E(H) = sum(b: b & 5 != 0) C_b(H)
I(H) = sum(b: b & 5 == 0 and b & 10 != 0) C_b(H)
C(H) = E(H) + I(H) = sum(b=1..15) C_b(H).
```

The physical energy `W_H=sum_grid d_Bbad*d_H` and `E(H)` use the same ORIGINAL bad (q,r) relation, but they are not equal. The exact D2 mixed-book bound is only

```
E(H) <= 24*t_H*W_H + sqrt(192*|B_bad|*D6(H)).
```

This upper can be vacuous even when `E(H)` is small. Also `I(H)` is absent from it. An unconditional upper on `E` alone never proves the root theorem.

## 3. The actual D6 proof gate, without circularity

The independent PR #394 physical path-reservoir theorem gives an appropriate *coherently pruned* graph H with at least `(16-o(1))s^6` oriented proper paths. Combining incident-endpoint compensation and the exact nonincident closure reduces the goal to

```
(16-o(1))*s^6 <= C(H) + 2*S(f,g) + sqrt(192*m*S(f,g)),
m=2*(s+1)*(s^2+1)*(s+1)=Theta(s^4).
```

A **SUFFICIENT UNPROVED** statement for some absolute `eta>0, Lambda>=0` is

```
C(H) <= (16-eta)*s^6 + Lambda*S(f,g) + o(s^6)
```

uniformly over complete globally injective same-map original `f,g` and a specified allowed PR #394 pruning H. The little-o must be uniform in the maps if used for a universal theorem. The sum `C=E+I` must be compensated JOINTLY, not as two unconnected numerical fits.

Alternatively the S-conditional auxiliary route

```
S(f_s,g_s)=o(s^6)  ==>  W_H=o(s^(59/10))
```

might rescue the endpoint part `E=o(s^6)` under t=O(s^(1/10)), but DOES NOT handle I. D5 does not falsify this conditional. Neither the conditional nor the direct compensation is proved here.

## 4. Strict finite falsification protocol

[Executable D6-A audit](../../research/hyp105_issue230_d6_joint_blocking_audit.py) joins three INDEPENDENT prior implementations on EXACTLY ONE same complete original f,g:

1. D1's oriented 16-mask ORIGINAL `q-l-p-r` full physical-three-path census, independently re-enumerated by endpoint-first/middle-edge traversal;
2. D2's ORIGINAL pencil-bad chord construction with exact `W_H` and actual coordinate-block `t_H`;
3. W32 only: accepted E1-B0 true ORIGINAL seven-positive-family sixset `S` and GF5 necessary floor.

The dataset is *four* coherent W(3,2) K6 maps (lex, reverse, S68, S72) and **two** complete D5 symplectic-spread original W(3,4) K14 maps with right `g` balanced/reversed. These are full **unpruned** G observations. They test how the large D5 energy relates to actual endpoint and internal blocking; they do not establish anything for the as-yet unmeasured D5 `H=PR394_pruned(G)`. Such transfer requires a new retained-subgraph path census in D6-B.

For W32, and ONLY W32, define an exact finite diagnostic at Lambda>=0 for the zero-remainder strengthening:

```
eta_max^finite(Lambda) = 16-C(G)/s^6+Lambda*S(f,g)/s^6 .
```

If a proposed finite inequality has `eta>eta_max^finite`, that **specific zero-remainder inequality** is refuted on the inspected map. Because the desired all-h inequality permits an unspecified `o(s^6)` remainder, NO finite eta ceiling is an asymptotic falsifier, nor can a positive finite margin prove Branch A. Code rejects an absent full S; the genuine W34 synchronized BB lower must NEVER be substituted for the complete seven-family S.

D6-A commits to the explicit primary metrics:

| Observable | W32 all 4 | D5 W34 both | All-h claim |
| --- | --- | --- | --- |
| Original W_H and physical block t_H | Exact | Exact | no small W guarantee |
| Sixteen masks, endpoint E, internal I, blocked C | Exact | Exact | identity C=E+I only |
| BB_sync | Exact | Exact | accepted subset, not full S |
| Entire seven-family S, accepted GF5 risk floor | Exact | **UNKNOWN**, not zero | OPEN |
| S-conditional W small or C compensation | Not inferred | Not inferred | OPEN |

## 5. Pre-registered GO/NO-GO for D6-B

1. **First:** inspect the completed exact-head D5 full Research run; its completion cannot be inherited from partial checks or an earlier SHA.
2. **Then:** run independent D6-A Contract on GitHub-hosted runner; pin the emitted real W32/W34 values after successful run, not before. If D6-A is RED, correct only the independently diagnosed issue on the D6 branch.
3. **Next substantive mathematical slice D6-B:** implement an exact original-geometry `H⊆G` path-census accepting a reproducible physical deletion policy, and check E/I/C/BB together with `W_H` on D5 spread maps. Compare (a) full G, (b) PR #394 coherent pruning, (c) adversarial selected-witness-edge deletion; do not treat an arbitrary every-nth deletion as the PR #394 algorithm.
4. **Search original sixset compensation:** construct per-obstruction source-to-target witnesses across ALL seven disjoint classes. Require injectivity or explicitly bounded congestion of a transfer `blocked paths -> selected positive original sixsets`, respecting the true original GQ projection and SAME global f/g. Any bound that only compares scalar aggregate counts with no charging certificate is not a proof.
5. For each proposed uniform lemma, pin exact quantifiers and seek finite original counterexamples first. If no proof, outcome `OPEN_WITH_FORMAL_BLOCKER`, NOT `PROVED_A` or `COUNTEREXAMPLE_B`.
6. External independent mathematical review must check D4–D5 classical spread, multiplicity and projected chords, and D6 conditional logic. Tests and GitHub-hosted CI are not a substitute for the review.

No source-wide claim of a new ASET exponent, complete R3 bound, Lean formalization or new mathematical universal theorem is made. This is evidence engineering to distinguish two mutually unproved D6 strategies.
