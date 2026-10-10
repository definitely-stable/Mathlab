# HYP-105 B3.2-E1-C16 — both-sided ORIGINAL incidence source coupling

Date: 2026-10-11. Parent [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Depends on [C15 PR #300](https://github.com/definitely-stable/Mathlab/pull/300); C16 is not targeted at main. C14/C15 are not merged as a consequence of this research. Separate engineering [CI PR #277](https://github.com/definitely-stable/Mathlab/pull/277) remains independent.

**Classification: RESTRICTED FINITE THEOREM + BOUNDED EXACT W(3,2) ORACLE. Status OPEN_WITH_FORMAL_BLOCKER.** This does not prove the universal all-h all-f,g lower `S_s=Omega(s^6)`, does not infer full GF5 R3, and does not change any ASET exponent.

## 1. Critical C15 omission and why an arbitrary filler is unsound

For the genuine original W(3,2), 15 original points and 15 original lines are independently injected into all 15 unordered physical edges of K6 on each side. The accepted E1-A *left 2factor* generator emits exactly 62,370 distinct ORIGINAL six-incidence sets for **each COMPLETE left mapping**. But the identity of these sixsets depends on that left mapping.

The previous C15 proof correctly restricts to 6,723 source sixsets whose every ORIGINAL left endpoint is already pinned by the partial map, so their eligibility is completion-invariant. It conservatively ignores 55,647 remaining source candidates in the 12+12 pinned W32 test. **Merely taking unpinned-left source candidates from the canonical filler would be incorrect**, since a different left completion can make the candidate ineligible. C16 never does this.

## 2. Exact original-sixset cost and disjoint complete-map identity

Let I denote the universe of all six-element subsets of the 45 ORIGINAL GQ incidences. For any full pair of TRUE common injections (f,g), define

`a_J(f,g) = 1` precisely when J is enumerated by the E1-A physical-left six-coordinate source for f AND the accepted B0 seven-class classifier succeeds on J using that SAME pair (f,g); otherwise `a_J(f,g)=0`.

Set `b_J(f,g)=R3_CERTIFIED_FLOORS[tag]` for an accepted tag, otherwise zero. No signed-event multiplicities, independent per-witness fake assignments or physical-orbit quotients are introduced. Non-source sixsets are **zero**, not incorrectly presumed selected. The accepted full-W32 census identity gives

`S_seven(f,g) = sum_(J in I) a_J(f,g)`, and `GF5_necessary_numerator(f,g) = sum_(J in I) b_J(f,g)`.

Both costs are nonnegative. Only sixsets belonging to the UNION of actually selected left sources over the bounded full-left completion domain need to be represented: all remaining J have cost zero for every allowable full descendant. Deduplication is by sorted six ORIGINAL incidence IDs, not by physical projection.

For a partial legal pair f0,g0 write L for unpinned ORIGINAL left points and R for unpinned ORIGINAL right lines. Partition the original universe into disjoint cells indexed by `(M_L(J),M_R(J)) = (points(J) intersect L, lines(J) intersect R)`. These named-original signatures are not arbitrary physical pair labels. Let A_uv(f,g) be the sum of a_J for cell (u,v), and `A_u = sum_v A_uv`. All full maps in a cell's minimization share actual left AND right assignments.

## 3. Certified two-sided nested hierarchy

Let F and G be the complete residual ORIGINAL-to-physical left and right bijections extending f0,g0. Every full-map pair is one member of F x G. Let `A_0(g)` be the total contribution from all J with `M_L(J)=empty`; this is independent of the left continuation. Define:

```text
L15 =                  min_g A_0(g)
L16_signature =        L15 + sum_(u != empty,v) min_(f,g) A_uv(f,g)
L16_left_group =       sum_u min_(f,g) A_u(f,g)
L16_shared_left =      min_f sum_u min_g A_u(f,g)
L16_full_joint =       min_(f,g) sum_u A_u(f,g)
```

**Restricted finite theorem (every actual full joint descendant):**

`0 <= L15 <= L16_signature <= L16_left_group <= L16_shared_left <= L16_full_joint <= S_seven(f,g)`.

**Proof.** Nonnegative costs justify omitting J with nonempty M_L to obtain L15, and justify adding independently minimized disjoint remaining cells for L16_signature. For any nonnegative arrays, `sum_v min_(f,g) A_uv <= min_(f,g) sum_v A_uv`; merging the right-signature cells for a fixed original left signature yields L16_left_group. Next `sum_u min_(f,g) A_u <= min_f sum_u min_g A_u`. Finally `sum_u min_g A_u(f,g) <= min_g sum_u A_u(f,g)` for each f, so L16_shared_left <= L16_full_joint. Every concrete descendant dominates the joint minimum. The identical proof holds separately for b_J, with potentially different minimizers; never claim simultaneous GF5/S-optimal maps.

**Monotonicity:** under a compatible new pin the full residual (f,g) domain is restricted. Signatures project by deleting the newly pinned named vertex, so previously disjoint cells MERGE and do not split; sum-of-minima cannot decrease. Sixsets absent from all remaining eligible left completions contribute zero to each new restricted map, so removing them from the representation cannot weaken the true cost. The distinguished u=empty block can only absorb previously nonempty-u cells, and no previously frozen-left sixset ceases to be frozen. Each of the four lower certificates and the full-joint optimum is therefore nondecreasing under legal prefix extension.

**Important strength limit:** L16_full_joint enumerates the entire bounded F x G domain and is consequently the EXACT minimum for this box; its agreement with independent enumeration is a valuable falsification gate, NOT an improvement in asymptotic running time or a new universal inequality. The useful nontrivial test is the numerical gap between L15, the intermediate C16 cell/group bounds, and the exhaustive endpoint.

## 4. Reproducible real-W32 implementation

Source: [two-sided oracle](../../research/hyp105_g5e2b3e1c16_two_sided_source.py). Tests: [independent full-map falsifiers](../../research/test_hyp105_g5e2b3e1c16_two_sided_source.py).

- Use the actual 45 original W32 incidences and full K6 physical pair palette on BOTH sides. Enumerate **each** of the at most 3! genuine left tails and 3! genuine right tails, never independent per-J physical assignments.
- For every complete left tail, reconstruct its true left physical map and enumerate 62,370 ORIGINAL sixsets; classify them under every actual complete right tail. Zero membership for unselected J is implicit, so no artificial filler determines eligibility.
- Allocate disjoint signature-array buckets for all joint map indices; both S indicator and the accepted GF5 necessary numerator use the same genuine map coordinates, but independent numerical minimization.
- Assert exactly 62,370 unique left candidates per left completion, invariant 6,723 all-left-pinned candidates, no duplicate original sets, exact cell partition totals, constant eligible-left base across all left tails, and the full hierarchy.
- Hard fail-closed caps: missing left<=3, missing right<=3, total legal maps<=36, classifications<=2,500,000. On budget overflow raise before yielding any certified answer. There is no Monte Carlo substitution or silent truncated result.
- Independent oracle recounts all 36 exact completed (f,g) models through the preexisting B0 `seven_census`; test also checks that changing left completion actually changes its candidate sixset universe. Check source signature monotonicity under extra genuine point+line pins, GF5 and seven separately, and exact fully pinned equality.
- Known C15 anchored baseline S=12 and accepted GF5 numerator=513,393; exact finite 36-box oracle S_min=148, GF5 numerator min=6,676,842. **Intermediate C16 numerical values and runtime must be read from a SUCCESSFUL exact-HEAD hosted run, not assumed here.**

## 5. Research acceptance and C17 decision

1. Dedicated `hyp105-c16-contract` hosted tests and a separate executable report on the exact PR HEAD must succeed.
2. Existing broad `research.yml` unit discovery automatically includes the new `test_hyp105_...c16...` suite; **full exact-head Research SUCCESS is additionally required**. The current monolithic research job has a known ten-minute timeout; the partition proposal #277 is NOT silently considered integrated or accepted.
3. Review C16 as a child of C15 with the full ordered C1–C15 ancestor chain; no direct main merge or CI bypass.
4. For C17, quantify gaps and cost for signature/group/shared-left. Any model-equivalent all-h reduction needs a polynomially describable incidence-tensor inequality or dual certificate whose support and computation do not grow as 15!² at W32 and factorial(s³) asymptotically. A positive finite root by itself cannot pass #230 Branch A.
5. Parent #230 remains **OPEN_WITH_FORMAL_BLOCKER** until its explicit PROVED_A / COUNTEREXAMPLE_B / RESTRICTED_THEOREM_C gate is genuinely satisfied. This C16 result is a finite-scope restricted theorem, not the all-h model-equivalent Branch C required there.
