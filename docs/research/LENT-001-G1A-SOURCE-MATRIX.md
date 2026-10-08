# LENT-001-G1A — source-to-claim matrix

Status: **PLANNING / TO BE FILLED FROM PRIMARY SOURCES**

Purpose: prevent terminology similarity from being mistaken for theorem equivalence.

## Matrix schema

Every prior-art source must be recorded with:

| Field | Meaning |
|---|---|
| Source | Primary paper / monograph |
| Ambient object | Field, group, code, data structure |
| Input family | Full message space, sets of fixed size, sets up to d, multisets, etc. |
| Collision relation | +1 only, ±1, arbitrary field coefficients, OR/union, etc. |
| Repeated summands | Allowed / forbidden / convention-dependent |
| Side bounds | Whether positive/negative parts are separately bounded |
| Structural sparsity | Column/support/Hamming-weight restriction |
| Locality notion | Update writes, query reads, repair reads, decoder work, etc. |
| Guarantee | Exact all-input, randomized, high probability, channel error, etc. |
| Sharp theorem | Exact theorem imported from source |
| Mathlab relation | Equivalent / sufficient / necessary / incomparable / unknown |
| Novelty effect | STOP / BASELINE / GAP REMAINS |
| Confidence | VERIFIED / NEEDS PRIMARY CHECK |

## Cluster A — sparse parity-check matrices

### Hanno Lefmann (2005)

Source:
"Sparse Parity-Check Matrices over GF(q)",
Combinatorics, Probability and Computing 14 (2005), 147–169.

| Field | Current entry |
|---|---|
| Ambient object | \(GF(q)^m\) columns |
| Input family | column subsets |
| Collision relation | arbitrary nonzero field coefficients |
| Repeated summands | not the ASET set-sum model |
| Side bounds | no ASET positive/negative side split |
| Structural sparsity | at most \(r\) nonzero entries per column |
| Locality notion | column sparsity |
| Guarantee | deterministic linear independence |
| Mathlab relation | sufficient for ASET exactness; equivalent only in the frozen binary case after the \(2d\) map |
| Novelty effect | binary lane STOP; q>2 gap remains |
| Confidence | VERIFIED at abstract/definition level; theorem details to be pinned |

G1A action:

- pin exact theorem statements needed as lower/upper baselines;
- do not transfer Lefmann upper bounds to ASET unless a reduction proves necessity.

### Lefmann–Pudlák–Savický / Naor–Verstraete

Purpose:

- close binary prior art;
- identify which finite-field results are stronger than elementary LENT counting;
- record exact parameter conventions.

Pinned model separation: q=3, m=1, d=1, columns 1 and 2=-1 are ASET-exact for singleton inputs but linearly dependent. Literature classification beyond this model separation remains TO AUDIT.

## Cluster B — dissociated / Sidon / B_h

### k-dissociated / bounded-order dissociated families

Target question:

Does a standard bounded-order dissociated definition match

\[
\varepsilon\in\{-1,0,1\}^V,
\quad n_+\le d,
\quad n_-\le d
\]

or only a total support bound such as \(\|\varepsilon\|_0\le k\)?

Status: TO AUDIT.

Novelty-sensitive distinction:

\[
n_+\le d,\ n_-\le d
\]

is not automatically identical to

\[
n_+ + n_-\le 2d.
\]

### Sidon / weak Sidon / B_h

Required checks:

- distinct versus repeated summands;
- exactly h versus all cardinalities up to h;
- cross-cardinality collisions;
- finite-field torsion effects;
- bounded-support restriction.

Current relation: NEIGHBOR / EQUIVALENCE NOT ESTABLISHED.

## Cluster C — update-efficient coding

### Mazumdar–Chandar–Wornell (2014)

Source:
"Update-Efficiency and Local Repairability Limits for Capacity Approaching Codes".

| Field | Current entry |
|---|---|
| Ambient object | error-correcting codes |
| Input family | full information-message space |
| Locality notion | number of encoded bits changed by one information-bit change |
| Guarantee | channel coding / vanishing error |
| Structural link | low-density generator behavior |
| Mathlab relation | strong locality neighbor, not an exact ASET theorem |
| Novelty effect | requires model-specific reduction before importing lower bounds |
| Confidence | VERIFIED at abstract/model level |

G1A action:

- extract the exact update-efficiency definition;
- identify which statements rely on full message space or channel-capacity assumptions;
- compare row-weight orientation with Mathlab columns carefully.

### Mehrabi / LRC update complexity

Status: TO AUDIT FROM PRIMARY SOURCE.

Purpose:

- determine whether its update metric is closer than LCC/LDC query locality;
- record exact rate/distance/local-repair assumptions.

## Cluster D — rate-compatible / nested

### Huang et al. (2020)

Source:
"Syndrome-Coupled Rate-Compatible Error-Correcting Codes: Theory and Application".

Current effect:

- neighboring evidence against assuming a universal positive constant tax from nestedness alone;
- does not settle sparse-source exact sketches with bounded update support.

Mathlab relation: NEIGHBOR / NOT EQUIVALENT.

G1A action:

- pin the exact asymptotic existence statement;
- identify whether any finite penalty term can inform the later nested+locality model.

## Cluster E — mixed alphabets

### Yehezkeally et al.

Source:
"Bounds on Mixed Codes with Finite Alphabets", arXiv:2212.09314.

Current effect:

- heterogeneous alphabets are not an untouched coding setting;
- Mathlab mixed-cell counting remains a baseline derivation;
- a sharp locality-aware optimization is not yet classified.

G1A action:

- map their product alphabet and metric assumptions;
- determine which bounds survive when reachable states are support-constrained.

## Cluster F — randomized reconciliation comparators

### Minisketch / PinSketch

Classification:
algebraic reconciliation comparator; not constant-support as capacity grows.

### Stuffed IBLT

Classification:
randomized/high-probability additive comparator; not deterministic all-input ASET by default.

## G1A decision rule

A direction may be marked G1A_CONTINUE_ASET only if the matrix shows that no primary source already proves the intended theorem under an equivalent model.

A missing keyword match is not evidence of novelty.

A theorem under a stronger model can be used as a construction/lower baseline, but its upper bound does not automatically constrain ASET.

A theorem under a weaker model cannot be imported without a reduction.

## Immediate research order

1. Lefmann 2005 definition + theorem table.
2. k-dissociated / bounded-order signed relations.
3. weak Sidon / restricted \(B_h\) with distinct summands.
4. q=3 special case.
5. update-efficient coding.
6. nested + locality.
7. mixed alphabets.
