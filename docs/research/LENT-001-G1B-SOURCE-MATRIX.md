# LENT-001-G1B — primary-source matrix

Status: **OPEN**

Issue: #6

This matrix is the operative novelty-closure artifact. Rows marked
NEEDS_PRIMARY_CHECK cannot support a final G1B decision.

## A. Sparse parity-check / small-column independence

| Source | Model | Current relation to ASET | Confidence | G1B task |
|---|---|---|---|---|
| Lefmann–Pudlák–Savický (1996), *On sparse parity check matrices* | binary bounded-column-weight, short linear independence | q=2 direct overlap | VERIFIED at model level | pin exact theorem/exponent used as binary baseline |
| Lefmann (2005), *Sparse Parity-Check Matrices over GF(q)* | bounded support, arbitrary field coefficients | stronger than ASET for q>2 | VERIFIED at definition level | pin every relevant theorem with characteristic/gcd restrictions |
| Naor–Verstraete (2005), *Improved bounds on the size of sparse parity check matrices* | sparse parity-check extremal bounds | binary/finite-field neighboring baseline | NEEDS_PRIMARY_CHECK | map exact field and parameter scope |

Rule: arbitrary-coefficient upper bounds are not ASET upper bounds without a
reduction.

## B. Dissociated / bounded signed relations

| Source/object | Model question | Confidence | G1B task |
|---|---|---|---|
| dissociated sets | forbids all finite \(\{-1,0,1\}\) relations? | NEEDS_PRIMARY_CHECK | pin standard definition and ambient-group assumptions |
| k-dissociated / bounded-order dissociated | total relation support bound vs separate \(n_+,n_-\) bounds | NEEDS_PRIMARY_CHECK | determine exact implication to/from ASET |
| finite-group/vector-space dissociated variants | torsion/characteristic effects | NEEDS_PRIMARY_CHECK | locate sharp finite-field results |
| bounded-support dissociated families | generator Hamming-weight constraint | NEEDS_PRIMARY_CHECK | highest-priority novelty check |

Critical question:

\[
n_+\le d,\quad n_-\le d
\]

versus only

\[
n_++n_-\le2d.
\]

## C. Sidon / B_h / restricted-sum families

| Object | Definition point to verify | Confidence |
|---|---|---|
| Sidon / B_2 | repeated summands? equal-cardinality only? | NEEDS_PRIMARY_CHECK |
| weak Sidon | distinct summands only? | NEEDS_PRIMARY_CHECK |
| B_h | repetitions and exactly h | NEEDS_PRIMARY_CHECK |
| restricted B_h / distinct-summand variants | closest fixed-cardinality analogue | NEEDS_PRIMARY_CHECK |
| all-orders-through-d systems | controls cross-cardinality collisions? | NEEDS_PRIMARY_CHECK |
| bounded-support/Hamming-ball versions | preserves \(w\) | NEEDS_PRIMARY_CHECK |

No "ASET = Sidon/B_h" statement is currently accepted.

## D. q=3 special case

Known G1A fact:

\[
q=3,\ m=1,\ d=1,\ \{1,2\}
\]

is ASET-exact but linearly dependent.

Nontrivial frozen-grid evidence also gives q=3, d=2 ASET-exact families with
ordinary short dependencies.

G1B task:

- locate any literature whose relation model uses \(\pm1\) together with
  side bounds or an equivalent distinct-subset-sum condition;
- do not substitute ordinary linear independence.

## E. Bounded-support additive families

This is the most novelty-sensitive cluster.

Questions:

1. Are there sharp \(B_h\)/dissociated bounds when every generator lies in a
   q-ary Hamming ball of radius \(w\)?
2. Are supports exactly w or at most w?
3. Are coefficients fixed, signed, or arbitrary?
4. Are upper and lower exponents known for fixed \(d,w\)?
5. Are constructions algebraic, probabilistic, or code-derived?

Status: NEEDS_PRIMARY_CHECK.

## F. Secondary boundary sources

These do not decide ASET novelty unless a direct reduction appears.

| Source | Role |
|---|---|
| Mazumdar–Chandar–Wornell (2014) | update/write locality comparator |
| Mehrabi / LRC update complexity | update-complexity comparator |
| Huang et al. (2020) | warning against pure nestedness-tax claims |
| mixed-alphabet coding literature | secondary mixed-cell lane |
| Minisketch / PinSketch | practical algebraic reconciliation comparator |
| Stuffed IBLT | randomized/high-probability comparator |

## Final decision table

To be filled only after primary-source verification:

| Regime | Known construction/lower baseline | Valid upper baseline | Unclosed gap | Decision |
|---|---|---|---|---|
| q=2 | TBD | TBD | expected known territory | TBD |
| q=3 | TBD | TBD | side-bounded signed gap | TBD |
| odd q>3 | TBD | TBD | coefficient + side-bound gap | TBD |
| char 2, q>2 | TBD | TBD | field-specific gap | TBD |

Final status remains **OPEN**.
