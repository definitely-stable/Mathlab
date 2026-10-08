# LENT-001-G1B — primary-source matrix

Status: **OPEN / AUDIT 01 RECORDED**

Issue: #6

Rows marked VERIFIED_PRIMARY have been checked against a primary paper,
author PDF, proceedings page, or arXiv manuscript. They may still require a
second theorem-level audit before a final asymptotic decision.

## A. Sparse parity-check / small-column independence

| Source | Exact model | Relation to ASET | Transfer | Confidence |
|---|---|---|---|---|
| Lefmann–Pudlák–Savický (1996), *On sparse parity check matrices* | binary bounded column weight + short linear independence | q=2 direct overlap | binary baseline | VERIFIED at model level |
| Lefmann (2005), *Sparse Parity-Check Matrices over GF(q)* | support ≤r, every k columns independent over GF(q), arbitrary nonzero coefficients | stronger than ASET for q>2 | constructions/lower baseline transfer; upper bounds do not automatically transfer | VERIFIED_PRIMARY |
| Naor–Verstraete (2005) | sparse parity-check extremal bounds | binary/finite-field neighbor | theorem map still needed | NEEDS_PRIMARY_CHECK |

## B. Dissociated / free families

| Source/object | Exact definition found | Relation to ASET | Confidence |
|---|---|---|---|
| Shkredov, arXiv:2205.07296 | k-dissociated means coefficient magnitude \(|\varepsilon_\lambda|\le k\), not relation length | k=1/full dissociation is stronger than every finite-d ASET; "k-dissociated" is not our bounded-order term | VERIFIED_PRIMARY |
| Nešetřil–Rödl–Sales (2024), free | all distinct finite subsets have distinct sums | stronger than every finite-d ASET | VERIFIED_PRIMARY |
| Nešetřil–Rödl–Sales (2024), h-free | collision excluded when one side has size ≤h, other side unrestricted | stronger than ASET_h | VERIFIED_PRIMARY |
| bounded-support finite-field dissociated families | unknown | highest-priority remaining gap | NEEDS_PRIMARY_CHECK |
| two-sided h-free / both-side-bounded signed systems | unknown | potentially definitionally closest | NEEDS_PRIMARY_CHECK |

## C. Sidon / B_h / restricted-sum families

| Source/object | Exact model | Relation to ASET | Confidence |
|---|---|---|---|
| Nešetřil–Rödl–Sales \(B_h^*\) | sums of h distinct elements unique | ASET_d implies \(B_h^*\) for every h≤d; converse absent | VERIFIED_PRIMARY |
| Kiss–Sándor, arXiv:2006.02783 | explicitly distinguishes distinct-term and repetition-allowed h-sum representation functions | confirms convention split; fixed-cardinality only | VERIFIED_PRIMARY |
| Huang–Tait–Won, arXiv:1809.05117 | Sidon/2-cap in \(\mathbb F_3^n\); includes repeated-summand equations | not equivalent to ASET d=2; neither blanket upper-bound transfer nor converse established | VERIFIED_PRIMARY |
| Sima–Li–Shomorony–Milenkovic, arXiv:2303.12990 | binary constant-weight vectors, real-valued sums of distinct pairs unique | weight-constrained equal-cardinality neighbor; not modular/all≤d | VERIFIED_PRIMARY |
| q-ary bounded-support \(B_h\) inside Hamming balls | unknown | critical remaining source class | NEEDS_PRIMARY_CHECK |

## D. Signature / detecting / adder codes

| Source | Exact model | Relation to ASET | Confidence |
|---|---|---|---|
| Lindström (1965), detecting/sum-distinct vectors | ordinary integer/rational sum detection | all-pattern ordinary-addition neighbor | VERIFIED_PRIMARY |
| Jevtić (1995), sum-distinct integral vectors | all representative sums distinct; \(\{0,x_i\}\) gives subset-sum uniqueness | ordinary-integer all-subset neighbor | VERIFIED_PRIMARY |
| Fan–Gu–Hachimori–Miao, arXiv:1905.10180 / TIT 2021 | t-signature and constant-weight t-signature codes for weighted binary adder channel | close extremal constant-weight neighbor; arithmetic/model differ | VERIFIED_PRIMARY |
| Erdoğan–Maringer–Polyanskii, arXiv:2206.10735 | q-ary codewords; any active subset identifiable from **integer** sum | all-subset integer-addition neighbor, not modular ASET | VERIFIED_PRIMARY |
| bounded-active-user finite-field/mod-q signature codes | not closed | potentially direct ASET overlap | NEEDS_PRIMARY_CHECK |

## E. Additive / quantitative group testing

| Source/object | Exact model | Relation to ASET | Confidence |
|---|---|---|---|
| Chang–Chen–Guo–Huang, arXiv:1303.6020 / TIT 2015 | additive \((D,d)\)-separability for d-sparse vectors under standard arithmetic | for \(D=\{0,1\}\), ordinary-arithmetic bounded-d analogue; modular ASET implies ordinary separability | VERIFIED_PRIMARY |
| quantitative group testing with bounded column weight | integer/count measurements, sparse binary source | potentially a valid ASET super-class upper-bound source when support conventions match | NEEDS_PRIMARY_CHECK |
| modulo-q quantitative/group-testing separability | unknown | potentially definitionally direct | NEEDS_PRIMARY_CHECK |

## F. q=3 special case

Verified facts:

- G1A: q=3 ASET is strictly weaker than ordinary short linear independence.
- Huang–Tait–Won Sidon/2-cap includes repeated-summand equations.
- Hence standard q=3 Sidon maxima cannot be imported as ASET maxima without a reduction.

Remaining:

- q=3 distinct-summand/all≤d systems;
- q=3 bounded-support two-sided signed relations.

## G. Secondary locality/nested/mixed sources

These do not decide ASET novelty unless a direct reduction appears.

| Source | Role |
|---|---|
| Mazumdar–Chandar–Wornell (2014) | update/write locality comparator |
| Mehrabi / LRC update complexity | update-complexity comparator |
| Huang et al. (2020) | warning against pure nestedness-tax |
| mixed-alphabet coding literature | secondary mixed-cell lane |
| Minisketch / PinSketch | algebraic reconciliation comparator |
| Stuffed IBLT | randomized/high-probability comparator |

## H. Arithmetic transfer rules

For the same columns/input domain, after choosing integer representatives:

\[
\text{mod-}q\text{ ASET}
\Longrightarrow
\text{ordinary-integer bounded-d separability}.
\]

Reason: integer equality implies equality modulo \(q\).

Therefore a compatible **upper bound** for ordinary bounded-d separability can
upper-bound modular ASET.

An ordinary-addition construction does not automatically give a modular
ASET construction, because distinct integer sums may coincide modulo \(q\).

All-subset integer signature codes and bounded-d modular ASET are generally
incomparable in strength because one changes both arithmetic and cardinality
scope.

## I. Final decision table

| Regime | Valid baseline known now | Remaining unclosed gap | Decision |
|---|---|---|---|
| q=2 | sparse parity-check; integer constant-weight B2/signature neighbors | novelty already poor | STOP as primary target |
| q=3 | Lefmann lower baseline; standard Sidon/2-cap neighbor; exact ASET separation | two-sided signed + bounded support | OPEN |
| odd q>3 | Lefmann lower baseline; integer signature/additive-separable neighbors | coefficient restriction + bounded sides + bounded support | OPEN |
| char 2, q>2 | arbitrary-coefficient sparse-linear baseline | field-specific signed relation behavior | OPEN |

Final G1B status remains **OPEN**.
