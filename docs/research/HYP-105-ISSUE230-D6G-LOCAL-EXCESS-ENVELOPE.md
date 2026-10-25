# HYP-105 #230 — D6-G: local Hall-excess envelope

**2026-10-13. Restricted theorem C / finite diagnostic only. Root Branch A/B remain open.**

D6-F computed the exact exception mass for a fixed one-incidence Hall capacity `K`:

```text
exception_K = C - maxflow_K.
```

D6-G separates the part forced by global cardinality from a genuine local Hall obstruction:

```text
local_excess_K = exception_K - max(0, C - K*S).
```

Here `C` is blocked oriented source demand and `S` is the number of accepted positive recipient sixsets in the target family under test. For true complete W32 this is the complete seven-family `S`. For W34/W38 this slice still does not substitute BB-only subsets for unknown complete seven-family `S`.

## 1. Interpretation

`max(0, C-K*S)` is the unavoidable pigeonhole deficit. If `C>K*S`, no assignment can route more than `K*S` units no matter how favorable the local support graph is.

A positive `local_excess_K` means something stronger: even after accounting for total capacity, the source-to-recipient incidence support is locally too narrow. Equivalently, some Hall obstruction is worse than the global cardinality floor.

Thus D6-G isolates the next compensation problem:

```text
C <= K*S + global_deficit + local_excess_K,
```

and asks whether one can prove an all-h bound on the local part, or whether an infinite family has unbounded or too-large local excess.

## 2. What changed

New executable:

```text
research/hyp105_issue230_d6g_local_excess_envelope.py
```

It provides:

1. `global_capacity_deficit(...)` — exact `max(0,C-K*S)`.
2. `local_excess_for_capacity(...)` — exact exception budget from D6-F minus the global deficit.
3. `local_excess_frontier(...)` — finite envelope over multiple candidate capacities.
4. Complete W32 all-seven diagnostic report for lex, reverse, S68, and S72.

New tests:

```text
research/test_hyp105_issue230_d6g_local_excess_envelope.py
```

The synthetic tests deliberately include a local Hall obstruction where global capacity alone does not explain the exception mass. This prevents the oracle from degenerating into a restatement of `C-KS`.

## 3. Complete W32 finite result

For the four true complete W32 all-seven cases, the first failed capacity `K-1` remains purely global:

| W32 map | C | complete S | zero-exception K | exception at K-1 | local excess at K-1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| lex | 942 | 259 | 4 | 165 | 0 |
| reverse | 898 | 169 | 6 | 53 | 0 |
| S68 | 606 | 68 | 9 | 62 | 0 |
| S72 | 658 | 72 | 10 | 10 | 0 |

This says only that these finite W32 examples do not expose a local Hall penalty at the first failed capacity. It does not prove all-h expansion, all-h exception control, or any lower bound on complete `S`.

## 4. Non-claims

D6-G does **not** prove:

* all-h uniform `K`;
* all-h local-excess bound;
* all-h exception-mass bound;
* complete W34/W38 seven-family `S`;
* Branch A or Branch B;
* ASET/R3 exponent claims.

## 5. Next mathematical target

The useful next theorem would be one of:

```text
local_excess_K = o(s^6)
```

for a fixed `K` on the genuine all-h object, or a structural counterexample family where local excess remains too large for the compensation route.

A weaker useful step is a source-support classification theorem describing which `F` can have positive local excess after subtracting the global pigeonhole floor.
