# HYP-105 E1-K3-G2-E — source-support charging into the TRUE accepted seven GF5 families

Date: 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked Draft child of [PR #377](https://github.com/definitely-stable/Mathlab/pull/377), exact parent HEAD `86dcc5e137230cb9f1843f3526f82ba3dea81d00` (Contract, INDEX, Research ALL SUCCESS). No merge and no `main` change.

**Scientific status: FINITE_W32_SEVEN_FAMILY_HALL_CERTIFICATE, not all-h S obstruction.** Valid only for legal complete W(3,2) physical pair bijections onto K6, for which the accepted seven-family enumerator is exhaustive. Every target is an actual six-element set of DISTINCT ORIGINAL incidences with an established strictly positive GF(5) class floor, not a freely constructed positive graph cycle or a weighted surrogate.

## 1. Audit of the preceding false approach

K3-G2-D found `Jcross=36` vs only `D6=15` in W32 lex, and `Jcross=28` vs `D6=3` in W32 reverse-line. More strongly, SAME ORIGINAL ANCHOR INCIDENCE local charging into proper D6 leaves 9 and 20 source witnesses without ANY allowed proper-D6 target respectively, and 5/18 and 6/6 anchor orphans inside the heavy off-differentfoot-noncollinear class. No target multiplicity can resolve isolated vertices. This is a NO-GO for a **particular locality rule**, not a counterexample to seven-family S.

Our next question is whether the SAME charging conditions behave differently when targets consist of every actually accepted GF(5) six-family motif, rather than D6 alone. This is a finite falsification gate: a passing W32 instance cannot be extended to all h without an independent theorem.

## 2. Exact actual-target and witness construction

Use the accepted B0 `seven_census(model,witness_sets=True)`. It scans exactly 62,370 candidate source six-incidence sets and retains precisely one classified six-set for each accepted motif:
`D6`, `B-left/A-right`, `A-left/B-right`, `C/A`, `C/B`, `B/B-overlap`, `B/B-disjoint`.
Every class has a strictly POSITIVE certified all-nonzero GF(5) risk numerator per ORIGINAL six-set, from the previously accepted `R3_CERTIFIED_FLOORS`. The accepted 51 full-palette checksum patterns are not replaced by a synthetic 0/1 motif. Selected actual six-set classes have certified weights; independent direct GF5 signed flow checks are performed on representative real W32 targets from all seven families.

Each individual K3-G2-D `Jcross` witness is reconstructed as an explicit physical Kikuchi six-cycle, EVERY physical edge is resolved to its UNIQUE ORIGINAL point-line incidence column via one coherent globally injective f,g, and the resulting multiset is required to have exactly five distinct original incidence columns, the anchor column twice and four other columns once. Let its **five-element ORIGINAL source-column support** be `S(w)`.

A target `D` has exactly six different ORIGINAL source columns and an accepted GF5 floor. We study the precise finite charging relations:
```
same_anchor(w,D): anchor(w) belongs to D;
overlap_ge_t(w,D): |S(w) intersect D| >= t,  t=1,2,3,4,5;
anchor_and_overlap_ge_t(w,D): anchor(w) in D AND |S(w) intersect D|>=t,
                              t=2,3.
```
These rules are **candidate proof relations** only, not consequences of positivity. Nothing asserts that witnessing a repeated C6 implies a positive target under ANY of these rules in every GQ.

## 3. Hall-k exact finite certificate

For each rule, form the bipartite graph with one left vertex per INDIVIDUAL Jcross witness and one right vertex per accepted six-set D. By capacity-k Hall, a full assignment exists iff every subset X of left witnesses has |X|<=k|N(X)|. Compute exact integral maxflow/mincut with unit source→w and w→D arcs, capacity k on D→sink. At k=1, report matched/unmatched, isolated witnesses, exact min cut. If no orphans, binary-search the *smallest integer k* allowing full coverage and independently reject k-1; otherwise set required k to null (all finite capacities fail). Repeat for the heavy off-differentfoot-noncollinear K3-G2-C class.

The ordinary cardinality floor `ceil(Jcross/S_seven)` is a lower bound on minimum k but NOT a Hall certificate. Source support overlap can create Hall-deficient subsets even when target count greatly exceeds witness count. A proper D6-only same-anchor subgraph is explicitly reconstructed as a strict subset and must reproduce K3-G2-D's counts.

The exact sums `S_seven=259` for W32 lex and `S_seven=169` for W32 reverse-line are inherited independently checked accepted research facts; W32 seeded global random mapping is another finite legal case. No false W(3,4) claim: full six-family B0 enumeration is defined here only for W32/K6 and the new gate fails closed outside it.

## 4. What a finite success or failure means

- If an anchor-conserving seven-family relation has **any isolated witness**, it is falsified for all finite k for that particular model. If it covers all witnesses at a small k in W32 it remains only a finite observation, not a theorem for all s.
- If non-anchor relations cover all witnesses with capacity k for W32, one still needs an all-h bound on the maximum charge multiplicity plus a theorem connecting the accepted GF5 source-set risks at all s. No inference from a W32 finite matching alone.
- No universality `Jcross=o(s^6)`, positive-coupled C6 bound, accepted seven-family `S_s=Omega(s^6)`, full GF5 R3 exponent, or ASET exponent is claimed.

## 5. Independent implementation evidence and follow-up

Reference `research/hyp105_g5e2b3e1k3g2e_seven_family_hall.py` and tests `research/test_hyp105_g5e2b3e1k3g2e_seven_family_hall.py`. The tests independently rebuild physical cyclic ORIGINAL edge provenance, validate all accepted source six-set targets and certified positive GF5 class floors, recompute true GF5 nonzero signed events for one representative from EACH seven family using the 782-orbit Fourier oracle, and check the actual Hall outcomes against the K3-G2-D proper-only subgraph and synthetic exact small capacity tests. Full deterministic report includes both entire Jcross and heavy-class gates.

Next decision: If any of the source-overlap rules is promising at finite h, derive a GLOBAL ALL-h geometric charging map with explicit bounded multiplicity. If each fails, prove a structural obstruction and return to the joint `(L(P3)-Theta)/12-Jcross` inequality or a different accepted-S positive motif extraction. Do not resume merely subdividing witnesses by GQ projection labels.

## 2026-10-12 exact Hosted Contract result — seven true GF5 targets overturn the D6-only locality NO-GO at s=2

The initial [dedicated K3-G2-E Contract #38207827789](https://github.com/definitely-stable/Mathlab/actions/runs/38207827789) PASSED all five checks, including actual signed positive GF5 six-set witness oracles from all seven accepted classes. Its output gives these exact W(3,2) finite charging certificates, one target capacity k=1:

| Coherent legal mapping | All seven actual positive targets | Source Jcross witnesses | Same original anchor covers | Any >=2 original columns covers | Anchor AND >=2 covers | >=3 covers | >=4 covers |
|---|---:|---:|---:|---:|---:|---:|---:|
| lex | 259 | 36 | **36** | **36** | 36 | 19 | 0 |
| reverse-line | 169 | 28 | **28** | **28** | 25 | 9 | 0 |
| random(seed=20261012) | 144 | 17 | **17** | **17** | 12 | 4 | 0 |

For the **heavy** original `off_differentfoot_noncollinear` class, all three maps also have a full injective charge under `same_anchor` and under `overlap_ge_2`, covering respectively 18, 6, and 5 witnesses. Results at higher overlap are smaller or zero and cannot be repaired by capacity when a witness has NO candidates.

**Important distinction:** K3-G2-D proved the D6-only SAME-original-anchor rule has isolated witnesses even when unlimited capacity is available. The full accepted seven GF5 target set has NO isolated witness for that same_anchor rule in all three finite W32 cases and admits an actual matching of target capacity 1. Consequently, any universal negative assertion that SAME-original-anchor charging is impossible regardless of allowed positive S-family would be false. Only the D6-only rule was refuted.

**More promising rule for generalized proof:** `|S(w)∩T|>=2` WITHOUT demanding that the repeated anchor column itself belong to T. It yields independent matchings at capacity 1 for three different coherent W32 models; its stricter anchor-and-second-column variant is falsified (3 and 5 isolated witnesses in reverse/random respectively), and `>=4` has no candidate whatsoever for these models. The new code constructs explicit deterministic injective witness→accepted-target index assignments via an augmenting path algorithm independent from maxflow, checks every edge/uniqueness condition, and records a SHA256 assignment certificate per finite model and rule. These positive finite outcomes are NOT an all-h Hall theorem; all s>=4 and adversarial global f,g remain unverified.

**Necessary next scientific proof:** Derive a symbolic injection/bounded-fiber map for every s=2^h from ORIGINAL GQ incidence and one globally coherent f,g into genuine positive accepted S_s six-column motifs, preserving a fixed (e.g. two-source-column) overlap. A witness-to-target map, even injective, establishes only `Jcross <= S_s` for that labeling. By itself this inequality would NOT establish the desired `S_s=Omega(s^6)`: one still needs either `Jcross=Omega(s^6)`, or a separate dichotomy showing small Jcross implies many positive S motifs. The full-R3 route `(L(P3)-Theta)/12-Jcross` remains independent.

