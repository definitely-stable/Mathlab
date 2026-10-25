# HYP-105 #230 — D6-F: exact exception-budget oracle

**2026-10-13. Finite certificate layer only. Root Branch A/B remain open.**

D6-D reduced one-incidence repair to exact weighted Hall flow. D6-E made the analytic support-expansion target explicit:

```text
M_E(F)+M_I(F) <= K B(F).
```

D6-F formalizes the fallback route mentioned at the end of D6-D/D6-E: if this inequality is too strong for a fixed `K`, how much blocked source mass must be left as an exception?

## 1. Exact finite statement

For fixed finite source triples `T`, accepted positive sixsets `Q`, and recipient capacity `K`, run the same ORIGINAL incidence-factored D6-D network:

```text
source -> T -> original incidence e -> Q -> sink,
                                      cap(Q->sink)=K.
```

Let `C=sum_T w(T)` and let `V_K` be the maxflow value. Then

```text
exception_K = C - V_K
```

is exactly the minimum oriented blocked-path demand that cannot be repaired under one-incidence overlap and capacity `K`.

This is exact because every routed unit is a valid one-incidence charge and maxflow is optimal. If a source triple has no eligible target at all, it becomes irreducible exception mass even for arbitrarily large `K`.

Thus every finite instance satisfies the exact compensation identity:

```text
chargeable_mass_K + exception_K = C,
chargeable_mass_K <= K * |Q|.
```

Equivalently:

```text
C <= K*S + exception_K
```

for the finite target set actually supplied. This is not an all-h theorem unless one separately proves `exception_K=o(s^6)` or an explicit bounded exceptional mass for the genuine PR394 high-h setting.

## 2. What the code adds

[`research/hyp105_issue230_d6f_exception_budget_oracle.py`](../../research/hyp105_issue230_d6f_exception_budget_oracle.py) provides:

1. `exception_budget_for_capacity(...)` — exact minimum exception mass for one `K`.
2. `exception_frontier(...)` — monotone frontier over several `K` values.
3. `minimal_capacity_for_exception_budget(...)` — smallest finite `K` meeting a specified exception budget, or a proof that no finite `K` can meet it because unsupported mass remains.
4. Complete W32 all-seven rows that reproduce D6-D zero-exception `K` and expose `K-1` exception mass.

The split fields `endpoint` and `internal` are diagnostic hints only. They do not claim a canonical decomposition of the actual removable exception set. They are used to inspect which source component dominates a mincut obstruction.

## 3. Complete finite W32 result

For true W32 complete all-seven target families:

| W32 map | C | complete S | zero-exception K | exact exception at K-1 |
| --- | ---: | ---: | ---: | ---: |
| lex | 942 | 259 | 4 | 165 |
| reverse | 898 | 169 | 6 | 53 |
| S68 | 606 | 68 | 9 | 62 |
| S72 | 658 | 72 | 10 | 10 |

For all four rows, the exact `K-1` exception mass equals the global source-closed support deficit:

```text
C - (K-1)S.
```

So in these finite W32 complete-all-seven cases, the first failed capacity is explained by the global pigeonhole obstruction, not by a smaller local support obstruction. This is useful evidence about the finite models, but it is still not an all-h proof.

## 4. Correct next analytic target

D6-F gives a sharper fork for D6-G:

1. Prove an all-h absolute `K` with zero exception:

```text
exception_K = 0.
```

2. Or prove a controlled exception theorem:

```text
exception_K <= (16-eta)s^6 + o(s^6)
```

or another bound strong enough to preserve the root compensation inequality.

3. Or construct a formal counter-support family where `exception_K` remains too large for every fixed `K` or for every proposed compensation regime.

## 5. Non-claims

D6-F does not prove:

- all-h uniform `K`;
- all-h exception mass bound;
- complete W34/W38 seven-family `S`;
- Branch A or Branch B;
- full GF5 R3 or ASET exponent.

W34 BB-only recipients remain forbidden as a substitute for complete seven-family `S`.
