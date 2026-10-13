# HYP-105 #230 — D6-E: source-closed support expansion profile

**2026-10-13. Restricted theorem C / finite certificate layer only. Root Branch A/B remain open.**

D6-D proved an exact transport equivalence: one-incidence-preserving repair is feasible with recipient load at most `K` if and only if the weighted Hall inequalities hold. D6-E does not claim a uniform all-h `K`. It turns the next analytic target into an explicit, reproducible support-expansion profile.

## 1. Correct analytic object

For a family of blocked original source triples `T` with integer oriented demand `w(T)`, and accepted positive original sixsets `Q`, D6-D reduces one-incidence repair to

```text
M(F) <= K B(F)
```

for source-closed original incidence supports `F`, where

```text
M(F) = sum_{T subset F} w(T),
B(F) = #{Q : Q intersects union_{T subset F} T}.
```

D6-E refines `M(F)` into the two source components needed by the issue #230 route:

```text
M(F) = M_E(F) + M_I(F),
```

where `M_E` is endpoint-bad path demand and `M_I` is internal-only path demand, matching the D6-B sixteen-mask split. The denominator deliberately uses the active source union `union_{T subset F}T`, not arbitrary extra incidences inserted into `F`. Otherwise a proof could be made artificially easier by adding incidences that carry no blocked source triple but touch many recipients.

The all-h target is therefore either:

```text
M_E(F)+M_I(F) <= K B(F)
```

with absolute `K`, uniformly over the genuine coherent maps and retained `H`, or a controlled exceptional-mass theorem where the failed supports have total mass small enough to preserve a compensation inequality. Neither is proved here.

## 2. What this slice implements

The new executable [`research/hyp105_issue230_d6e_support_expansion_profile.py`](../../research/hyp105_issue230_d6e_support_expansion_profile.py) provides:

1. `source_closed_support_profile(...)`: exact `M(F)`, split `M_E/M_I`, `B(F)`, local required `ceil(M(F)/B(F))`, and excess over a candidate `K`.
2. `factored_cut_profile(...)`: the same D6-D factorized network, but with the failing residual cut converted into a source-closed support profile. The residual mincut certificate remains exact, while the source-closed `F` is the analytic object to attack.
3. `split_blocked_sources_by_endpoint_internal(...)`: an independent path scanner that reconstructs endpoint/internal source-triple demand and checks it against `retained_path_census` before returning.
4. `finite_w32_support_expansion_report()`: complete W32 all-seven profiles for lex, reverse, S68, and S72.

Complete accepted seven-positive targets are used only for true W32, where they are actually enumerated. D6-E intentionally does not use W34 BB-only targets as if they were the full seven-family `S`.

## 3. First finite complete-W32 profile result

For the four genuine W32 complete all-seven finite instances, the global source support itself already forces the same `K` as D6-D's exact optimum:

| W32 map | C | E | I | complete S | D6-D/D6-E K |
| --- | ---: | ---: | ---: | ---: | ---: |
| lex | 942 | 786 | 156 | 259 | 4 |
| reverse | 898 | 676 | 222 | 169 | 6 |
| S68 | 606 | 544 | 62 | 68 | 9 |
| S72 | 658 | 600 | 58 | 72 | 10 |

Thus these finite W32 examples do not expose an additional local source-support expansion penalty beyond the global pigeonhole floor. This is useful diagnostically, but it is not a theorem for all `h`, not a PR394 retained-graph theorem, and not a proof that complete `S` is large.

The exact meaning is limited:

```text
finite W32 complete all-seven: local profiled obstruction = global floor;
all-h map-independent expansion: OPEN;
controlled exceptional mass: OPEN;
Branch A/B: OPEN.
```

## 4. Why this changes the next proof search

D6-C killed the natural two-incidence repair rule using a true S68 local witness. D6-D showed that one-incidence repair is exactly a Hall problem over original incidence support. D6-E now isolates the precise support families where any future proof must work:

```text
F -> (M_E(F), M_I(F), B(F), ceil((M_E(F)+M_I(F))/B(F))).
```

The next mathematical step is no longer to add more finite examples. It is to prove one of the following:

* a genuine expansion theorem for original GQ supports `F`, with complete seven-family positive recipients;
* a decomposition into good supports plus a bounded exceptional source mass;
* or a formal counterexample family where some source-closed `F_h` has `M(F_h)/B(F_h)` unbounded or grows too fast for compensation.

## 5. Acceptance boundary

D6-E is acceptable as a tooling and formalization slice if:

* synthetic source-closed Hall profiles detect zero-denominator and finite-deficit cases;
* exact factorized mincuts become source-closed support profiles;
* W32 complete all-seven profiles reproduce the D6-D optimal K values and exact E/I/C split;
* reports explicitly keep all-h support expansion, exception mass, and Branch A/B open.

It is not acceptable to infer any all-h constant from `K=4,6,9,10`, nor to use W34 BB-only recipients as a replacement for unknown complete W34 `S`.
